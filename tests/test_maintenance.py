"""Phase 14: schema V3 migration, infrastructure paths, purpose, maintenance.

Every test runs against a temporary database and a fake client. Nothing here
opens a socket.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone

import pytest
import yaml
from pathlib import Path

from dependency_map import storage
from dependency_map.db import (
    SCHEMA_VERSION,
    MigrationError,
    connect,
    initialize_database,
    migrate_v2_to_v3,
)
from dependency_map.dedup import make_candidate_id, normalize_repo_url
from dependency_map.maintenance import (
    MaintenanceCollector,
    MaintenanceSignals,
    _path_from_blob_url,
    rung_for,
    select_candidates,
)
from dependency_map.scoring import ScoringEngine, score_maintenance_burden
from dependency_map.qualification import CandidateEvidence

WEIGHTS = Path("config/weights.yaml")


@pytest.fixture(scope="module")
def weights_and_caps():
    data = yaml.safe_load(WEIGHTS.read_text(encoding="utf-8"))
    return data["dimension_weights"], data["gate_caps"]


# =============================================================================
# Migration
# =============================================================================


def _v2_database(path):
    """A minimal schema-2 database carrying one row in each affected table."""
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.executescript(
        """
        CREATE TABLE schema_version (id INTEGER PRIMARY KEY CHECK (id = 1),
            version INTEGER NOT NULL, applied_at TEXT NOT NULL);
        INSERT INTO schema_version VALUES (1, 2, 'then');
        CREATE TABLE runs (run_id TEXT PRIMARY KEY, started_at TEXT NOT NULL,
            finished_at TEXT, notes TEXT);
        CREATE TABLE candidates (candidate_id TEXT PRIMARY KEY, repo_url TEXT,
            repo_owner TEXT, repo_name TEXT);
        CREATE TABLE discovery_queries (query_id TEXT PRIMARY KEY, run_id TEXT,
            query TEXT, discovery_tier INTEGER, library_name TEXT);
        CREATE TABLE discovery_evidence (id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_id TEXT, candidate_id TEXT, discovery_result_rank INTEGER,
            UNIQUE (query_id, candidate_id));
        CREATE TABLE pipeline_evidence (candidate_id TEXT PRIMARY KEY,
            code_usage_confirmed INTEGER, template_directory_present INTEGER,
            multiple_document_types_handled INTEGER, pipeline_stage_count INTEGER,
            infrastructure_service_present INTEGER, pipeline_evidence_notes TEXT);
        CREATE TABLE business_evidence (candidate_id TEXT PRIMARY KEY,
            readme_describes_product INTEGER, readme_excerpt TEXT,
            website_exists INTEGER, application_code_exists INTEGER,
            document_functionality_in_production_code INTEGER, stars INTEGER,
            last_commit_date TEXT, contributor_count INTEGER,
            business_evidence_notes TEXT);
        INSERT INTO runs VALUES ('run_1', 'then', NULL, NULL);
        INSERT INTO candidates VALUES ('c_1', 'https://github.com/a/b', 'a', 'b');
        INSERT INTO discovery_queries VALUES ('q_1', 'run_1', 'q', 1, 'Gotenberg');
        INSERT INTO discovery_evidence (query_id, candidate_id, discovery_result_rank)
            VALUES ('q_1', 'c_1', 3);
        INSERT INTO pipeline_evidence VALUES ('c_1', 1, 0, 0, 2, 1, 'notes');
        INSERT INTO business_evidence VALUES
            ('c_1', 1, 'excerpt', 1, 1, 1, 42, '2026-07-01', NULL, 'bnotes');
        """
    )
    conn.commit()
    return conn


def test_migration_moves_version_2_to_3(tmp_path):
    conn = _v2_database(tmp_path / "v2.db")
    assert conn.execute("SELECT version FROM schema_version").fetchone()[0] == 2

    migrate_v2_to_v3(conn)

    assert conn.execute("SELECT version FROM schema_version").fetchone()[0] == 3
    assert SCHEMA_VERSION == 3


def test_migration_preserves_every_existing_row(tmp_path):
    """The whole point of migrating in place rather than rebuilding."""
    conn = _v2_database(tmp_path / "v2.db")
    tables = ("runs", "candidates", "discovery_queries", "discovery_evidence",
              "pipeline_evidence", "business_evidence")
    before = {t: conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in tables}

    migrate_v2_to_v3(conn)

    after = {t: conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in tables}
    assert before == after
    row = conn.execute("SELECT * FROM discovery_evidence").fetchone()
    assert row["discovery_result_rank"] == 3, "existing values untouched"
    assert conn.execute(
        "SELECT pipeline_evidence_notes FROM pipeline_evidence"
    ).fetchone()[0] == "notes"


def test_migration_leaves_new_columns_null_rather_than_inventing_values(tmp_path):
    """A run-1 row genuinely does not know its file path or its purpose.
    A default would turn 'never asked' into a finding."""
    conn = _v2_database(tmp_path / "v2.db")
    migrate_v2_to_v3(conn)

    de = conn.execute("SELECT * FROM discovery_evidence").fetchone()
    assert de["file_path"] is None
    assert de["evidence_url"] is None

    pe = conn.execute("SELECT * FROM pipeline_evidence").fetchone()
    assert pe["infrastructure_reference_present"] is None

    be = conn.execute("SELECT * FROM business_evidence").fetchone()
    assert be["is_catalogue_repository"] is None
    assert be["readme_indicates_example_or_tutorial"] is None
    assert be["has_examples_directory"] is None


def test_migration_creates_maintenance_evidence(tmp_path):
    conn = _v2_database(tmp_path / "v2.db")
    migrate_v2_to_v3(conn)

    columns = {r["name"] for r in conn.execute("PRAGMA table_info(maintenance_evidence)")}
    assert {"candidate_id", "document_library_count", "same_file_library_count",
            "custom_logic_present", "custom_formatting_present",
            "custom_validation_present", "custom_error_handling_present",
            "repeated_modification_evidence", "recent_commit_count",
            "active_contributors", "latest_commit_date"}.issubset(columns)


def test_migration_is_idempotent(tmp_path):
    conn = _v2_database(tmp_path / "v2.db")
    migrate_v2_to_v3(conn)
    migrate_v2_to_v3(conn)  # must not raise or duplicate a column

    assert conn.execute("SELECT version FROM schema_version").fetchone()[0] == 3


def test_migration_refuses_a_database_that_is_not_version_2(tmp_path):
    conn = _v2_database(tmp_path / "v2.db")
    conn.execute("UPDATE schema_version SET version = 1")

    with pytest.raises(MigrationError, match="expects schema version 2"):
        migrate_v2_to_v3(conn)


def test_migration_keeps_integrity(tmp_path):
    conn = _v2_database(tmp_path / "v2.db")
    migrate_v2_to_v3(conn)
    assert conn.execute("PRAGMA integrity_check").fetchone()[0] == "ok"


# =============================================================================
# Recovered discovery paths and exact-path infrastructure retrieval
# =============================================================================


def test_discovery_evidence_stores_the_matched_file(conn, run_id, candidate_id):
    qid = storage.create_discovery_query(
        conn, run_id=run_id, discovery_source="github_code_search",
        query="q", discovery_tier=1)
    storage.insert_discovery_evidence(
        conn, query_id=qid, candidate_id=candidate_id,
        file_path="deploy/docker/docker-compose.yml",
        evidence_url="https://github.com/a/b/blob/main/deploy/docker/docker-compose.yml")

    rows = storage.discovery_paths_for_candidate(conn, candidate_id)
    assert len(rows) == 1
    assert rows[0]["file_path"] == "deploy/docker/docker-compose.yml"


def test_rows_without_a_path_are_skipped_not_treated_as_absence(
    conn, run_id, candidate_id
):
    qid = storage.create_discovery_query(
        conn, run_id=run_id, discovery_source="github_code_search", query="q")
    storage.insert_discovery_evidence(conn, query_id=qid, candidate_id=candidate_id)

    assert storage.discovery_paths_for_candidate(conn, candidate_id) == []


# =============================================================================
# The section 7 rubric
# =============================================================================


def _signals(**kw):
    base = dict(candidate_id="c_1", files_inspected=1)
    base.update(kw)
    return MaintenanceSignals(**base)


def test_rung_0_when_nothing_was_inspected():
    """Unknown must stay distinguishable from 'inspected and found thin'."""
    rung, reason = rung_for(_signals(files_inspected=0))
    assert rung == 0
    assert "unassessable" in reason


def test_rung_1_thin_direct_use():
    rung, _ = rung_for(_signals(document_library_count=1, custom_logic_present=False))
    assert rung == 1


def test_rung_2_some_custom_logic():
    rung, _ = rung_for(_signals(
        document_library_count=1, custom_logic_present=True,
        custom_formatting_present=True))
    assert rung == 2


def test_rung_3_multiple_libraries_with_glue_in_one_file():
    rung, reason = rung_for(_signals(
        document_library_count=2, same_file_library_count=2,
        custom_logic_present=True))
    assert rung == 3
    assert "one file" in reason


def test_rung_4_substantial_custom_code():
    rung, reason = rung_for(_signals(
        document_library_count=2, custom_logic_present=True,
        custom_formatting_present=True, custom_validation_present=True))
    assert rung == 4
    assert "commit history not pulled" in reason


def test_rung_4_records_commit_corroboration_when_available():
    rung, reason = rung_for(_signals(
        document_library_count=2, custom_logic_present=True,
        custom_formatting_present=True, custom_validation_present=True,
        repeated_modification_evidence=True))
    assert rung == 4
    assert "corroborated" in reason


def test_rung_5_full_hand_built_system():
    rung, _ = rung_for(_signals(
        document_library_count=2, custom_logic_present=True,
        custom_formatting_present=True, custom_validation_present=True,
        custom_error_handling_present=True))
    assert rung == 5


def test_commit_activity_alone_never_raises_the_rung():
    """The rubric grades custom code, not how busy the repository is. A thin
    wrapper committed daily is still a rung 1."""
    thin_and_busy = _signals(
        document_library_count=1, custom_logic_present=False,
        repeated_modification_evidence=True, recent_commit_count=500,
        active_contributors=40)

    assert rung_for(thin_and_busy)[0] == 1


def test_an_untouched_hand_built_system_still_scores_5():
    quiet = _signals(
        document_library_count=3, custom_logic_present=True,
        custom_formatting_present=True, custom_validation_present=True,
        custom_error_handling_present=True,
        repeated_modification_evidence=False, recent_commit_count=0)

    assert rung_for(quiet)[0] == 5


# =============================================================================
# Scoring integration
# =============================================================================


def test_missing_maintenance_evidence_scores_unknown():
    result = score_maintenance_burden(CandidateEvidence(candidate_id="c_1"))
    assert result.score == 0
    assert result.unknown is True


def test_present_maintenance_evidence_applies_the_rubric(conn, candidate_id):
    storage.upsert_maintenance_evidence(
        conn, candidate_id=candidate_id, document_library_count=2,
        same_file_library_count=2, custom_logic_present=True,
        custom_formatting_present=True, custom_validation_present=True,
        custom_error_handling_present=True, files_inspected=3)

    evidence = CandidateEvidence.load(conn, candidate_id)
    result = score_maintenance_burden(evidence)

    assert result.score == 5
    assert result.unknown is False


def test_inspected_but_thin_is_known_not_unknown(conn, candidate_id):
    """A repository we looked at and found thin scores 1 with unknown=False.
    Collapsing that back to unknown would discard a real finding."""
    storage.upsert_maintenance_evidence(
        conn, candidate_id=candidate_id, document_library_count=1,
        same_file_library_count=1, custom_logic_present=False,
        custom_formatting_present=False, custom_validation_present=False,
        custom_error_handling_present=False, files_inspected=2)

    result = score_maintenance_burden(CandidateEvidence.load(conn, candidate_id))

    assert result.score == 1
    assert result.unknown is False


def test_rescoring_is_deterministic(conn, run_id, candidate_id, weights_and_caps):
    weights, caps = weights_and_caps
    storage.upsert_maintenance_evidence(
        conn, candidate_id=candidate_id, document_library_count=2,
        same_file_library_count=2, custom_logic_present=True,
        custom_formatting_present=True, custom_validation_present=True,
        custom_error_handling_present=False, files_inspected=2)
    storage.upsert_qualification(
        conn, candidate_id=candidate_id, qualification_status="keep",
        qualification_reason="r", confidence="high")

    engine = ScoringEngine(conn, weights, caps)
    first = engine.score_one(candidate_id)
    second = engine.score_one(candidate_id)

    assert first.final_score == second.final_score
    assert first.dimensions["maintenance_burden"] == \
        second.dimensions["maintenance_burden"]


# =============================================================================
# Deterministic selection and bounded collection
# =============================================================================


def _scored(conn, run_id, name, score, status="investigate"):
    cid = make_candidate_id(f"https://github.com/{name}")
    owner, repo = name.split("/")
    storage.insert_candidate_if_new(
        conn, candidate_id=cid,
        repo_url=normalize_repo_url(f"https://github.com/{name}"),
        repo_owner=owner, repo_name=repo, first_seen_run_id=run_id)
    storage.upsert_qualification(
        conn, candidate_id=cid, qualification_status=status,
        qualification_reason="r", confidence="medium")
    storage.upsert_score(
        conn, candidate_id=cid,
        **{d: 0 for d in (
            "document_volume", "document_complexity", "business_criticality",
            "pipeline_complexity", "maintenance_burden", "build_vs_buy_signal",
            "commercial_leverage")},
        raw_weighted_score=0.0, final_score=score, confidence_band="medium")
    return cid


def test_selection_is_deterministic(conn, run_id):
    for i in range(20):
        _scored(conn, run_id, f"org/r{i:02d}", score=50 - i)

    assert select_candidates(conn, top_n=5, cap=10) == \
        select_candidates(conn, top_n=5, cap=10)


def test_selection_takes_the_top_scores_first(conn, run_id):
    for i in range(10):
        _scored(conn, run_id, f"org/r{i:02d}", score=10 * i)

    chosen = select_candidates(conn, top_n=3, keep_floor=99, cap=3)
    scores = [
        conn.execute("SELECT final_score FROM scores WHERE candidate_id=?", (c,))
        .fetchone()[0]
        for c in chosen
    ]
    assert scores == [90, 80, 70]


def test_selection_adds_keeps_above_the_floor_outside_the_top(conn, run_id):
    for i in range(5):
        _scored(conn, run_id, f"org/high{i}", score=90 - i)
    _scored(conn, run_id, "org/keeper", score=25, status="keep")
    _scored(conn, run_id, "org/lowkeep", score=5, status="keep")

    chosen = select_candidates(conn, top_n=5, keep_floor=20, cap=75)
    names = {
        conn.execute("SELECT repo_name FROM candidates WHERE candidate_id=?", (c,))
        .fetchone()[0]
        for c in chosen
    }
    assert "keeper" in names
    assert "lowkeep" not in names


def test_selection_respects_the_cap(conn, run_id):
    for i in range(30):
        _scored(conn, run_id, f"org/r{i:02d}", score=30 - i, status="keep")

    assert len(select_candidates(conn, top_n=50, keep_floor=0, cap=7)) == 7


# =============================================================================
# Collector behaviour, against a fake client
# =============================================================================


class FakeFile:
    def __init__(self, text, url="https://github.com/a/b/blob/main/app/render.py"):
        self.text = text
        self.evidence_url = url


class RecordingClient:
    """Answers file reads and records every call, so a test can prove the
    collector did not wander."""

    def __init__(self, files=None, commits=()):
        self._files = files or {}
        self._commits = commits
        self.calls: list[tuple[str, str]] = []

    def get_file_contents(self, owner, repo, path, ref=None, use_cache=True):
        self.calls.append(("file", path))
        if path not in self._files:
            from dependency_map.reliability import ApiError
            raise ApiError(404, f"https://x/{path}", "Not Found")
        return FakeFile(self._files[path], f"https://github.com/{owner}/{repo}/blob/main/{path}")

    def list_directory(self, *a, **k):
        self.calls.append(("listing", a[2] if len(a) > 2 else ""))
        return ()

    def list_commits(self, owner, repo, *, since=None, per_page=100, use_cache=True):
        self.calls.append(("commits", f"{owner}/{repo}"))
        return self._commits


def _with_dependency(conn, candidate_id, path, library="python-docx"):
    storage.insert_dependency_found(
        conn, candidate_id=candidate_id, library_name=library,
        library_category="docx", direction="generation",
        detection_method="code_import",
        evidence_url=f"https://github.com/example-org/example-repo/blob/main/{path}")


def test_collector_reads_only_files_already_evidenced(conn, candidate_id):
    _with_dependency(conn, candidate_id, "app/render.py")
    client = RecordingClient({"app/render.py": "def build():\n    set_font()\n"})

    collector = MaintenanceCollector(conn, client, collect_commits=False)
    collector.collect(candidate_id)

    opened = [c for c in client.calls if c[0] == "file"]
    assert opened == [("file", "app/render.py")]
    assert not any(c[0] == "listing" for c in client.calls), "must not crawl"


def test_collector_respects_the_file_cap(conn, candidate_id):
    for i in range(9):
        _with_dependency(conn, candidate_id, f"app/mod{i}.py", library=f"lib{i}")
    client = RecordingClient({f"app/mod{i}.py": "def f(): pass" for i in range(9)})

    MaintenanceCollector(conn, client, max_files=2, collect_commits=False).collect(
        candidate_id)

    assert len([c for c in client.calls if c[0] == "file"]) == 2


def test_manifest_evidence_is_never_opened(conn, candidate_id):
    """A requirements line proves a dependency, never how much code wraps it."""
    storage.insert_dependency_found(
        conn, candidate_id=candidate_id, library_name="python-docx",
        library_category="docx", direction="generation",
        detection_method="manifest_declaration",
        evidence_url="https://github.com/a/b/blob/main/requirements.txt")
    client = RecordingClient({})

    signals = MaintenanceCollector(conn, client, collect_commits=False).collect(
        candidate_id)

    assert client.calls == []
    assert signals.files_inspected == 0


def test_an_unreadable_file_is_not_counted_as_inspected(conn, candidate_id):
    _with_dependency(conn, candidate_id, "app/gone.py")
    client = RecordingClient({})

    signals = MaintenanceCollector(conn, client, collect_commits=False).collect(
        candidate_id)

    assert signals.files_inspected == 0
    assert rung_for(signals)[0] == 0, "unreadable must stay unknown"


def test_collector_extracts_the_structural_signals(conn, candidate_id):
    _with_dependency(conn, candidate_id, "app/render.py")
    source = (
        "def render(doc):\n"
        "    set_font(doc, 'Arial')\n"
        "    if not validate(doc):\n"
        "        raise ValueError('bad')\n"
        "    try:\n"
        "        save(doc)\n"
        "    except IOError:\n"
        "        logger.error('failed')\n"
    )
    client = RecordingClient({"app/render.py": source})

    signals = MaintenanceCollector(conn, client, collect_commits=False).collect(
        candidate_id)

    assert signals.custom_logic_present
    assert signals.custom_formatting_present
    assert signals.custom_validation_present
    assert signals.custom_error_handling_present
    assert signals.custom_glue_excerpt


class Commit:
    def __init__(self, author, when):
        self.author = author
        self.committed_at = when
        self.sha = "a"


def test_commit_history_is_recorded_as_corroboration(conn, candidate_id):
    _with_dependency(conn, candidate_id, "app/render.py")
    commits = [Commit("alice", "2026-08-01T00:00:00Z"),
               Commit("bob", "2026-08-05T00:00:00Z"),
               Commit("alice", "2026-08-09T00:00:00Z")]
    client = RecordingClient({"app/render.py": "def f(): pass"}, commits=commits)

    signals = MaintenanceCollector(conn, client).collect(candidate_id)

    assert signals.recent_commit_count == 3
    assert signals.active_contributors == 2
    assert signals.repeated_modification_evidence is True


def test_a_client_without_commit_support_still_collects_structure(conn, candidate_id):
    _with_dependency(conn, candidate_id, "app/render.py")

    class NoCommits(RecordingClient):
        list_commits = None

    client = NoCommits({"app/render.py": "def f():\n    set_font()\n"})
    signals = MaintenanceCollector(conn, client).collect(candidate_id)

    assert signals.custom_logic_present
    assert signals.recent_commit_count is None


def test_blob_url_path_extraction():
    assert _path_from_blob_url(
        "https://github.com/a/b/blob/abc123/src/app/render.py") == "src/app/render.py"
    assert _path_from_blob_url("https://github.com/a/b") is None


def test_maintenance_evidence_round_trips(conn, candidate_id):
    storage.upsert_maintenance_evidence(
        conn, candidate_id=candidate_id, document_library_count=3,
        same_file_library_count=2, custom_logic_present=True,
        custom_formatting_present=True, custom_validation_present=False,
        custom_error_handling_present=True, custom_glue_excerpt="def render():",
        recent_commit_count=12, active_contributors=4,
        latest_commit_date="2026-08-01", files_inspected=3)

    row = storage.get_maintenance_evidence(conn, candidate_id)

    assert row["document_library_count"] == 3
    assert row["custom_validation_present"] == 0
    assert row["recent_commit_count"] == 12


def test_maintenance_upsert_replaces_rather_than_duplicates(conn, candidate_id):
    for count in (1, 2, 3):
        storage.upsert_maintenance_evidence(
            conn, candidate_id=candidate_id, document_library_count=count,
            same_file_library_count=0, custom_logic_present=False,
            custom_formatting_present=False, custom_validation_present=False,
            custom_error_handling_present=False, files_inspected=1)

    rows = conn.execute("SELECT COUNT(*) FROM maintenance_evidence").fetchone()[0]
    assert rows == 1
    assert storage.get_maintenance_evidence(conn, candidate_id)[
        "document_library_count"] == 3


def test_no_secret_appears_in_maintenance_evidence(conn, candidate_id):
    fake = "ghp_phase14fakeToken000000000000000000"
    _with_dependency(conn, candidate_id, "app/render.py")
    client = RecordingClient({"app/render.py": "def f(): pass"})
    collector = MaintenanceCollector(conn, client, collect_commits=False)
    collector.record(collector.collect(candidate_id))

    dump = "".join(
        str(dict(r)) for r in conn.execute("SELECT * FROM maintenance_evidence")
    )
    assert fake not in dump


# =============================================================================
# Repository-purpose evidence (part B) and the reference/service split (part A)
# =============================================================================


def test_purpose_signals_detect_a_catalogue():
    from dependency_map.evidence import _PURPOSE_CATALOGUE

    for text in ("A curated list of self-hosted applications",
                 "Awesome-list of document tools",
                 "One-click apps for your homelab",
                 "app store for CasaOS"):
        assert _PURPOSE_CATALOGUE.search(text), text


def test_purpose_signals_do_not_fire_on_a_real_product():
    from dependency_map.evidence import _PURPOSE_CATALOGUE, _PURPOSE_EXAMPLE

    product = (
        "Acme Contracts generates lease agreements and invoices for our "
        "customers automatically. See the examples folder for sample output."
    )
    assert not _PURPOSE_CATALOGUE.search(product)
    # The bare word "examples" in a sentence must not mark a product as a demo;
    # only a heading or an explicit self-description does.
    assert not _PURPOSE_EXAMPLE.search(product)


def test_purpose_signals_detect_example_headings():
    from dependency_map.evidence import _PURPOSE_EXAMPLE

    assert _PURPOSE_EXAMPLE.search("## Examples\n")
    assert _PURPOSE_EXAMPLE.search("This repository is a demo of docxtpl")


def test_purpose_fields_are_null_when_nothing_could_be_assessed(conn, candidate_id):
    """Null means 'not assessed'. It must never be stored as false, which
    would be a finding nobody made."""
    storage.upsert_business_evidence(
        conn, candidate_id=candidate_id, readme_describes_product=False,
        readme_excerpt=None, website_exists=False, application_code_exists=False,
        document_functionality_in_production_code=False, stars=None,
        last_commit_date=None, contributor_count=None)

    row = storage.get_business_evidence(conn, candidate_id)
    assert row["is_catalogue_repository"] is None
    assert row["readme_indicates_example_or_tutorial"] is None
    assert row["has_examples_directory"] is None


def test_purpose_fields_round_trip(conn, candidate_id):
    storage.upsert_business_evidence(
        conn, candidate_id=candidate_id, readme_describes_product=False,
        readme_excerpt=None, website_exists=False, application_code_exists=True,
        document_functionality_in_production_code=False, stars=1,
        last_commit_date=None, contributor_count=None,
        is_catalogue_repository=True,
        readme_indicates_example_or_tutorial=False,
        has_examples_directory=True)

    row = storage.get_business_evidence(conn, candidate_id)
    assert row["is_catalogue_repository"] == 1
    assert row["readme_indicates_example_or_tutorial"] == 0
    assert row["has_examples_directory"] == 1


def test_qualification_does_not_branch_on_purpose_signals(conn, candidate_id):
    """Part B is evidence, not a rule. Flipping every purpose signal must not
    change the qualification outcome on identical pipeline evidence."""
    from dependency_map.qualification import qualify

    def outcome(**purpose):
        storage.upsert_pipeline_evidence(
            conn, candidate_id=candidate_id, code_usage_confirmed=True,
            template_directory_present=False,
            multiple_document_types_handled=False, pipeline_stage_count=1,
            infrastructure_service_present=False)
        storage.upsert_business_evidence(
            conn, candidate_id=candidate_id, readme_describes_product=True,
            readme_excerpt="For our customers.", website_exists=True,
            application_code_exists=True,
            document_functionality_in_production_code=True, stars=5,
            last_commit_date="2026-07-01", contributor_count=None, **purpose)
        return qualify(CandidateEvidence.load(conn, candidate_id))

    plain = outcome()
    flagged = outcome(is_catalogue_repository=True,
                      readme_indicates_example_or_tutorial=True,
                      has_examples_directory=True)

    assert plain.status == flagged.status
    assert plain.rejection_reason == flagged.rejection_reason


def test_infrastructure_reference_and_service_are_separate_columns(conn, candidate_id):
    storage.upsert_pipeline_evidence(
        conn, candidate_id=candidate_id, code_usage_confirmed=False,
        template_directory_present=False, multiple_document_types_handled=False,
        pipeline_stage_count=0, infrastructure_service_present=False,
        infrastructure_reference_present=True)

    row = storage.get_pipeline_evidence(conn, candidate_id)
    assert row["infrastructure_reference_present"] == 1
    assert row["infrastructure_service_present"] == 0


def test_infrastructure_reference_defaults_to_null_not_false(conn, candidate_id):
    storage.upsert_pipeline_evidence(
        conn, candidate_id=candidate_id, code_usage_confirmed=False,
        template_directory_present=False, multiple_document_types_handled=False,
        pipeline_stage_count=0, infrastructure_service_present=False)

    assert storage.get_pipeline_evidence(
        conn, candidate_id)["infrastructure_reference_present"] is None


def test_scoring_and_qualification_make_no_network_calls(conn, candidate_id):
    """Part F item 7, asserted at module level rather than trusted."""
    import inspect

    from dependency_map import qualification as q
    from dependency_map import scoring as s

    for module in (s, q):
        source = inspect.getsource(module)
        for forbidden in ("requests.", "urlopen", "socket.", "http.client",
                          "RequestsTransport"):
            assert forbidden not in source, f"{module.__name__} references {forbidden}"


# =============================================================================
# Part A: infrastructure_service_present requires direct evidence of use
# =============================================================================


@pytest.mark.parametrize("line,service,expected", [
    ('resp = requests.post("http://gotenberg:3000/forms/chromium")', "gotenberg", True),
    ('GOTENBERG_URL = os.environ["GOTENBERG_URL"]', "gotenberg", True),
    ('url = "http://libreoffice:8100/convert"', "libreoffice", True),
    ('libreoffice_host = settings["libreoffice"]', "libreoffice", True),
    # A passing mention is not a call site.
    ("# we could use gotenberg one day", "gotenberg", False),
    ("from reportlab import canvas", "gotenberg", False),
    # "port" hides inside "import"; the word boundary is what stops that.
    ("import gotenberg_helper", "gotenberg", False),
])
def test_wired_reference_needs_a_call_site_not_a_mention(line, service, expected):
    from dependency_map.evidence import _wired_reference

    assert _wired_reference(line.lower(), service) is expected


class _Entry:
    """Minimal stand-in for a library-universe entry."""

    def __init__(self, name, patterns=()):
        self.library_name = name
        self.category = "conversion"
        self.infrastructure_patterns = tuple(
            type("P", (), {"pattern": p, "filename": None, "detection": "compose"})()
            for p in patterns
        )


class _Hit:
    def __init__(self, path, excerpt):
        self.path = path
        self.excerpt = excerpt
        self.evidence_url = f"https://github.com/a/b/blob/main/{path}"


def _pipeline_inputs(code_hits=(), dependencies=()):
    from dependency_map.evidence import _Gathered

    gathered = _Gathered()
    gathered.code_hits = list(code_hits)
    return gathered, list(dependencies)


def _collector(conn):
    from dependency_map.evidence import EvidenceCollector
    from dependency_map.library_universe import load_library_universe

    return EvidenceCollector(conn, RecordingClient({}), load_library_universe())


def test_compose_reference_plus_unrelated_app_code_is_not_service_use(conn):
    """The exact over-claim: a compose file and some application code
    elsewhere is co-presence, not evidence the app calls the service."""
    entry = _Entry("Gotenberg", ["gotenberg/gotenberg"])
    gathered, deps = _pipeline_inputs(
        code_hits=[(entry, _Hit("src/app/main.py", "def home(): return render()"))],
        dependencies=[{"entry": entry, "detection_method": "infrastructure_reference"}],
    )

    assert _collector(conn)._infrastructure_is_used(gathered, deps) is False


def test_compose_reference_plus_direct_integration_code_is_service_use(conn):
    entry = _Entry("Gotenberg", ["gotenberg/gotenberg"])
    gathered, deps = _pipeline_inputs(
        code_hits=[(entry, _Hit(
            "src/convert.py",
            'r = requests.post("http://gotenberg:3000/forms/chromium/convert")'))],
        dependencies=[{"entry": entry, "detection_method": "infrastructure_reference"}],
    )

    assert _collector(conn)._infrastructure_is_used(gathered, deps) is True


def test_exact_integration_configuration_is_service_use(conn):
    entry = _Entry("LibreOffice", ["libreoffice"])
    gathered, deps = _pipeline_inputs(
        code_hits=[(entry, _Hit("app/settings.py",
                                'LIBREOFFICE_URL = env("LIBREOFFICE_URL")'))],
        dependencies=[{"entry": entry, "detection_method": "infrastructure_reference"}],
    )

    assert _collector(conn)._infrastructure_is_used(gathered, deps) is True


def test_reference_only_is_not_service_use(conn):
    entry = _Entry("Gotenberg", ["gotenberg/gotenberg"])
    gathered, deps = _pipeline_inputs(
        dependencies=[{"entry": entry, "detection_method": "infrastructure_reference"}])

    assert _collector(conn)._infrastructure_is_used(gathered, deps) is False


def test_the_service_named_in_source_counts_as_use(conn):
    """A code_import row is only written for a real source file, so it is
    direct evidence the application references the service itself."""
    entry = _Entry("Gotenberg", ["gotenberg/gotenberg"])
    gathered, deps = _pipeline_inputs(
        dependencies=[
            {"entry": entry, "detection_method": "infrastructure_reference"},
            {"entry": entry, "detection_method": "code_import"},
        ])

    assert _collector(conn)._infrastructure_is_used(gathered, deps) is True


def test_a_wiring_mention_in_a_non_source_file_does_not_count(conn):
    """A compose file naming its own hostname says nothing about the caller."""
    entry = _Entry("Gotenberg", ["gotenberg/gotenberg"])
    gathered, deps = _pipeline_inputs(
        code_hits=[(entry, _Hit("docker-compose.yml",
                                "GOTENBERG_URL: http://gotenberg:3000"))],
        dependencies=[{"entry": entry, "detection_method": "infrastructure_reference"}],
    )

    assert _collector(conn)._infrastructure_is_used(gathered, deps) is False


# =============================================================================
# A reject never keeps a score row
# =============================================================================


def _score_row(conn, candidate_id):
    return conn.execute(
        "SELECT * FROM scores WHERE candidate_id = ?", (candidate_id,)
    ).fetchone()


def _make_scored(conn, candidate_id, weights_and_caps):
    weights, caps = weights_and_caps
    storage.upsert_qualification(
        conn, candidate_id=candidate_id, qualification_status="keep",
        qualification_reason="r", confidence="high")
    ScoringEngine(conn, weights, caps).score_one(candidate_id)
    assert _score_row(conn, candidate_id) is not None


def test_a_scored_candidate_loses_its_score_when_it_becomes_reject(
    conn, candidate_id, weights_and_caps
):
    """The phase 14 case: better evidence turns a scored candidate into a
    reject, and the score written under the old evidence must not survive."""
    _make_scored(conn, candidate_id, weights_and_caps)

    storage.upsert_qualification(
        conn, candidate_id=candidate_id, qualification_status="reject",
        qualification_reason="r", rejection_reason="tutorial_or_demo",
        confidence="medium")

    assert _score_row(conn, candidate_id) is None


def test_re_running_qualification_keeps_the_score_absent(
    conn, candidate_id, weights_and_caps
):
    _make_scored(conn, candidate_id, weights_and_caps)
    for _ in range(3):
        storage.upsert_qualification(
            conn, candidate_id=candidate_id, qualification_status="reject",
            qualification_reason="r", rejection_reason="tutorial_or_demo",
            confidence="medium")

    assert _score_row(conn, candidate_id) is None


def test_rejecting_a_candidate_that_never_scored_is_harmless(conn, candidate_id):
    storage.upsert_qualification(
        conn, candidate_id=candidate_id, qualification_status="reject",
        qualification_reason="r", rejection_reason="tutorial_or_demo",
        confidence="medium")

    assert _score_row(conn, candidate_id) is None


def test_the_scoring_stage_skips_a_rejected_candidate(
    conn, candidate_id, weights_and_caps
):
    weights, caps = weights_and_caps
    storage.upsert_qualification(
        conn, candidate_id=candidate_id, qualification_status="reject",
        qualification_reason="r", rejection_reason="tutorial_or_demo",
        confidence="medium")

    engine = ScoringEngine(conn, weights, caps)
    assert engine.score_one(candidate_id) is None
    engine.run(candidate_ids=[candidate_id])

    assert _score_row(conn, candidate_id) is None


def test_a_keep_that_becomes_reject_and_back_is_scored_again(
    conn, candidate_id, weights_and_caps
):
    """Deleting on reject must not make the candidate permanently unscorable:
    if later evidence qualifies it again, scoring works normally."""
    weights, caps = weights_and_caps
    _make_scored(conn, candidate_id, weights_and_caps)
    storage.upsert_qualification(
        conn, candidate_id=candidate_id, qualification_status="reject",
        qualification_reason="r", rejection_reason="tutorial_or_demo",
        confidence="medium")
    assert _score_row(conn, candidate_id) is None

    storage.upsert_qualification(
        conn, candidate_id=candidate_id, qualification_status="keep",
        qualification_reason="r", confidence="high")
    ScoringEngine(conn, weights, caps).score_one(candidate_id)

    assert _score_row(conn, candidate_id) is not None


def test_delete_score_is_idempotent(conn, candidate_id, weights_and_caps):
    _make_scored(conn, candidate_id, weights_and_caps)

    assert storage.delete_score(conn, candidate_id) == 1
    assert storage.delete_score(conn, candidate_id) == 0


def test_no_rejected_candidate_holds_a_score_after_a_full_pipeline(
    conn, run_id, weights_and_caps
):
    """The invariant, checked over a mixed corpus rather than one candidate."""
    weights, caps = weights_and_caps
    engine = ScoringEngine(conn, weights, caps)

    ids = []
    for i in range(9):
        cid = _scored(conn, run_id, f"org/mix{i:02d}", score=10 + i,
                      status="keep" if i % 3 else "investigate")
        engine.score_one(cid)
        ids.append(cid)

    # Two thirds of them then turn out to be rejects.
    for cid in ids[::3]:
        storage.upsert_qualification(
            conn, candidate_id=cid, qualification_status="reject",
            qualification_reason="r", rejection_reason="single_incidental_use",
            confidence="medium")
    engine.run(candidate_ids=ids)

    orphans = conn.execute(
        "SELECT COUNT(*) FROM scores s JOIN qualification g USING(candidate_id) "
        "WHERE g.qualification_status = 'reject'"
    ).fetchone()[0]
    assert orphans == 0
