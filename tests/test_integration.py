"""Phase 12: full-pipeline integration, resumability, and security validation.

This file proves the pipeline's key invariants hold end to end rather than
per-module, which is what the individual test files already cover. Nothing
here adds a new discovery strategy, scoring rule, or qualification rule; every
test exercises the existing stages wired together, against mocked or seeded
data. No test opens a real socket.
"""

from __future__ import annotations

import base64
import csv
import io
import json
import re
import subprocess
from pathlib import Path

import pytest
import yaml
from click.testing import CliRunner

from dependency_map import storage
from dependency_map.clients.github_client import (
    DirectoryEntry,
    FileContents,
    GitHubClient,
    RepositoryMetadata,
)
from dependency_map.db import (
    SCHEMA_VERSION,
    SCORING_DIMENSIONS,
    DatabaseNotInitialized,
    SchemaVersionMismatch,
    connect,
    initialize_database,
    open_database,
)
from dependency_map.dedup import (
    FreshBatchError,
    make_candidate_id,
    normalize_repo_url,
    plan_rotation,
    verify_fresh_batch,
)
from dependency_map.discovery import (
    DiscoveryEngine,
    DiscoveryError,
    GeneratedQuery,
    QueryGenerator,
)
from dependency_map.evidence import EvidenceCollector, collect_for_candidates
from dependency_map.library_universe import load_library_universe
from dependency_map.qualification import QualificationEngine
from dependency_map.reliability import (
    ApiError,
    HttpResponse,
    MemoryCacheStore,
    RateLimited,
    ReliabilityPolicy,
    ReliableRequester,
    RequestsTransport,
    SqliteCacheStore,
    is_fresh,
)
from dependency_map.report import ReportError, gather_report_data, render_csv, render_markdown, write_report
from dependency_map.run_manager import STAGES, RunManager
from dependency_map.scoring import ScoringEngine

FAKE_TOKEN = "ghp_phase12fakeToken0000000000000000000"
FAKE_KEY = "libio_phase12_fake_key_0000"
WEIGHTS_PATH = Path("config/weights.yaml")


@pytest.fixture(scope="module")
def universe():
    return load_library_universe()


@pytest.fixture(scope="module")
def weights_and_caps():
    data = yaml.safe_load(WEIGHTS_PATH.read_text(encoding="utf-8"))
    return data["dimension_weights"], data["gate_caps"]


# =============================================================================
# Fakes shared by the integration tests below.
# =============================================================================


class Page:
    """Stands in for a GitHubClient.search_code() result."""

    def __init__(self, results, total=None, capped=False):
        self.results = tuple(results)
        self.total_count = len(self.results) if total is None else total
        self.capped = capped
        self.incomplete_results = False


class Hit:
    def __init__(self, full_name, rank=1, path="requirements.txt"):
        owner, _, name = full_name.partition("/")
        self.repo_full_name = full_name
        self.repo_url = f"https://github.com/{full_name}"
        self.repo_owner, self.repo_name = owner, name
        self.path = path
        self.rank = rank
        self.evidence_url = f"https://github.com/{full_name}/blob/main/{path}"
        self.excerpt = ""
        self.sha = "a"


def entry(name, type_="file", path=None):
    return DirectoryEntry(name=name, path=path or name, type=type_,
                          html_url=f"https://github.com/x/blob/main/{path or name}")


def repo_metadata(**kw):
    base = dict(full_name="acme/x", repo_url="https://github.com/acme/x",
               repo_owner="acme", repo_name="x", is_fork=False, is_archived=False,
               primary_language="Python", stars=10, forks=1, description="",
               homepage=None, default_branch="main", pushed_at="2026-07-01T00:00:00Z",
               created_at="2024-01-01T00:00:00Z")
    base.update(kw)
    return RepositoryMetadata(**base)


def file_at(full_name, path, text):
    return FileContents(
        path=path, text=text, sha="a", size=len(text),
        evidence_url=f"https://github.com/{full_name}/blob/main/{path}",
        repo_full_name=full_name)


class ScriptedClient:
    """A per-repository GitHub client stand-in, used for the full pipeline test.

    Distinguishes the discovery-style broad code search (any query not scoped
    to one repository) from the evidence-collector's repo-scoped search, since
    the two stages use search_code differently and a full pipeline test needs
    both to behave realistically.
    """

    def __init__(self, repos: dict, *, discovery_hits: list, fail=None):
        self._repos = repos
        self._discovery_hits = discovery_hits
        self._fail = fail or {}
        self.calls: list[tuple] = []

    def _repo(self, owner, name):
        return self._repos[f"{owner}/{name}"]

    def get_repository(self, owner, repo, use_cache=True):
        self.calls.append(("metadata", f"{owner}/{repo}"))
        if "metadata" in self._fail and f"{owner}/{repo}" in self._fail["metadata"]:
            raise self._fail["metadata"][f"{owner}/{repo}"]
        return self._repo(owner, repo)["metadata"]

    def list_directory(self, owner, repo, path="", ref=None, use_cache=True):
        self.calls.append(("listing", f"{owner}/{repo}:{path}"))
        return tuple(self._repo(owner, repo)["listing"] if not path else ())

    def get_file_contents(self, owner, repo, path, ref=None, use_cache=True):
        self.calls.append(("file", f"{owner}/{repo}:{path}"))
        files = self._repo(owner, repo)["files"]
        if path not in files:
            raise ApiError(404, f"https://x/{path}", "Not Found")
        return files[path]

    def search_code(self, query, per_page=30, page=1, use_cache=True):
        self.calls.append(("search", query))
        if query.startswith("repo:"):
            full_name = query.split(" ", 1)[0][len("repo:"):]
            return Page(self._repos.get(full_name, {}).get("code_hits", []))
        return Page(self._discovery_hits, total=len(self._discovery_hits))


def build_fake_transport(routes: dict) -> "type":
    """A generic Transport, keyed by URL substring, for CLI-level tests.

    routes maps a substring to either an HttpResponse or a callable taking the
    matched URL and returning one, so one fixture can serve every endpoint
    shape a CLI command touches without hitting the network.
    """

    class FakeTransport:
        def __init__(self):
            self.calls: list[str] = []

        def request(self, method, url, *, params=None, headers=None, timeout=30.0):
            self.calls.append(url)
            for substring, response in routes.items():
                if substring in url:
                    return response(url) if callable(response) else response
            return HttpResponse(status=404, headers={}, text='{"message":"not found"}', url=url)

    return FakeTransport


def json_response(body, status=200):
    return HttpResponse(status=status, headers={}, text=json.dumps(body), url="https://x")


def b64(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


# =============================================================================
# 1. Full mocked integration test: discovery -> evidence -> qualification ->
#    scoring -> report, with a real keep/investigate/reject mix.
# =============================================================================


@pytest.fixture
def full_pipeline_client():
    """One tier-1 discovery query surfaces three repositories, shaped to
    produce one keep, one investigate, and one reject once evidence and
    qualification run."""
    keeper_readme = ("# Keeper\n\nKeeper generates lease documents for our "
                     "customers automatically.\n")
    reject_readme = "# rejectme\n\nA fork of a document library.\n"
    investigate_readme = ("# Investigate\n\nInvestigate Me is a reporting tool "
                          "for our customers.\n")

    repos = {
        "acme/keeper": {
            "metadata": repo_metadata(
                full_name="acme/keeper", repo_url="https://github.com/acme/keeper",
                repo_owner="acme", repo_name="keeper", is_fork=False,
                homepage="https://keeper.example.com", stars=500),
            "listing": [entry("README.md"), entry("requirements.txt"),
                       entry("templates", "dir"), entry("app", "dir")],
            "files": {
                "README.md": file_at("acme/keeper", "README.md", keeper_readme),
                "requirements.txt": file_at("acme/keeper", "requirements.txt",
                                            "docxtpl==0.16.7\n"),
            },
            "code_hits": [Hit("acme/keeper", path="app/render.py")],
        },
        "acme/rejectme": {
            "metadata": repo_metadata(
                full_name="acme/rejectme", repo_url="https://github.com/acme/rejectme",
                repo_owner="acme", repo_name="rejectme", is_fork=True),
            "listing": [entry("README.md"), entry("requirements.txt")],
            "files": {
                "README.md": file_at("acme/rejectme", "README.md", reject_readme),
                "requirements.txt": file_at("acme/rejectme", "requirements.txt",
                                            "docxtpl==0.16.7\n"),
            },
            "code_hits": [],
        },
        "acme/investigate-me": {
            "metadata": repo_metadata(
                full_name="acme/investigate-me",
                repo_url="https://github.com/acme/investigate-me",
                repo_owner="acme", repo_name="investigate-me", is_fork=False,
                homepage="https://im.example.com"),
            "listing": [entry("README.md"), entry("requirements.txt")],
            "files": {
                "README.md": file_at("acme/investigate-me", "README.md",
                                     investigate_readme),
                "requirements.txt": file_at("acme/investigate-me",
                                            "requirements.txt", "docxtpl==0.16.7\n"),
            },
            "code_hits": [],
        },
    }
    discovery_hits = [Hit("acme/keeper", rank=1), Hit("acme/rejectme", rank=2),
                      Hit("acme/investigate-me", rank=3)]
    return ScriptedClient(repos, discovery_hits=discovery_hits)


def run_full_pipeline(conn, universe, client, weights_and_caps, *, run_id="run_1"):
    weights, caps = weights_and_caps
    generator = QueryGenerator(universe, windows=("pushed:2026-01-01..2026-03-31",),
                               include_co_occurrence=False)
    manager = RunManager(
        conn,
        discovery_engine=DiscoveryEngine(conn, client, generator),
        evidence_collector=EvidenceCollector(conn, client, universe),
        query_generator=generator,
        scoring_engine=ScoringEngine(conn, weights, caps),
    )
    return manager.run(run_id=run_id, stages=STAGES, tiers=[1], query_limit=1)


def test_1_full_pipeline_wires_discovery_through_scoring(
    conn, universe, full_pipeline_client, weights_and_caps
):
    report = run_full_pipeline(conn, universe, full_pipeline_client, weights_and_caps)

    keeper = make_candidate_id("https://github.com/acme/keeper")
    rejectme = make_candidate_id("https://github.com/acme/rejectme")
    investigate = make_candidate_id("https://github.com/acme/investigate-me")

    # Discovered -> evidence collected for all three.
    assert storage.get_pipeline_evidence(conn, keeper) is not None
    assert storage.get_pipeline_evidence(conn, rejectme) is not None
    assert storage.get_pipeline_evidence(conn, investigate) is not None

    # Evidence -> qualification, with the designed mix.
    assert storage.get_qualification(conn, keeper)["qualification_status"] == "keep"
    assert storage.get_qualification(conn, rejectme)["qualification_status"] == "reject"
    assert storage.get_qualification(conn, rejectme)["rejection_reason"] == \
        "fork_of_library"
    assert storage.get_qualification(conn, investigate)["qualification_status"] == \
        "investigate"

    # Qualification -> scoring: rejects never get a row.
    assert storage.get_score(conn, keeper) is not None
    assert storage.get_score(conn, investigate) is not None
    assert storage.get_score(conn, rejectme) is None

    # unknown_dimensions preserved (maintenance_burden is always unknown in
    # the MVP).
    unknown = storage.decode_unknown_dimensions(
        storage.get_score(conn, keeper)["unknown_dimensions"])
    assert "maintenance_burden" in unknown


def test_1_scored_candidates_appear_in_the_report_reject_does_not(
    conn, universe, full_pipeline_client, weights_and_caps
):
    run_full_pipeline(conn, universe, full_pipeline_client, weights_and_caps)
    data = gather_report_data(conn)
    csv_text = render_csv(data)
    md_text = render_markdown(data)

    assert len(data.ranked) == 2
    for text in (csv_text, md_text):
        assert "keeper" in text
        assert "investigate-me" in text
        assert "rejectme" not in text


def test_1_csv_and_markdown_agree(conn, universe, full_pipeline_client, weights_and_caps):
    run_full_pipeline(conn, universe, full_pipeline_client, weights_and_caps)
    data = gather_report_data(conn)
    csv_rows = list(csv.DictReader(io.StringIO(render_csv(data))))

    assert [c.candidate_id for c in data.ranked] == \
        [row["candidate_id"] for row in csv_rows]
    for candidate, row in zip(data.ranked, csv_rows):
        assert str(candidate.row["final_score"]) == row["final_score"]
        assert candidate.row["qualification_status"] == row["qualification_status"]


def test_1_output_is_deterministic_across_regeneration(
    conn, universe, full_pipeline_client, weights_and_caps
):
    run_full_pipeline(conn, universe, full_pipeline_client, weights_and_caps)

    first_csv = render_csv(gather_report_data(conn))
    first_md = render_markdown(gather_report_data(conn))
    second_csv = render_csv(gather_report_data(conn))
    second_md = render_markdown(gather_report_data(conn))

    assert first_csv == second_csv
    # Everything except the generation timestamp must be identical.
    strip_ts = lambda t: re.sub(r"Generated: .*", "Generated: X", t)
    assert strip_ts(first_md) == strip_ts(second_md)


# =============================================================================
# 2. Multi-run integration test.
# =============================================================================


def test_2_run_two_separates_new_from_previously_seen(conn):
    from dependency_map.dedup import run_stats

    storage.create_run(conn, "run_1", started_at="2026-01-01T00:00:00Z")
    q1 = storage.create_discovery_query(
        conn, run_id="run_1", discovery_source="github_code_search",
        query="q1", library_name="python-docx", discovery_tier=3)
    for repo in ("org/a", "org/b", "org/c"):
        cid = make_candidate_id(f"https://github.com/{repo}")
        owner, name = repo.split("/")
        storage.insert_candidate_if_new(
            conn, candidate_id=cid, repo_url=normalize_repo_url(f"https://github.com/{repo}"),
            repo_owner=owner, repo_name=name, first_seen_run_id="run_1")
        storage.insert_discovery_evidence(conn, query_id=q1, candidate_id=cid)
    storage.update_query_results(conn, q1, total_count=3, returned_count=3)

    storage.create_run(conn, "run_2", started_at="2026-02-01T00:00:00Z")
    q2 = storage.create_discovery_query(
        conn, run_id="run_2", discovery_source="github_code_search",
        query="q2", library_name="python-docx", discovery_tier=3)
    for repo in ("org/b", "org/c", "org/d", "org/e"):
        cid = make_candidate_id(f"https://github.com/{repo}")
        owner, name = repo.split("/")
        storage.insert_candidate_if_new(
            conn, candidate_id=cid, repo_url=normalize_repo_url(f"https://github.com/{repo}"),
            repo_owner=owner, repo_name=name, first_seen_run_id="run_2")
        storage.insert_discovery_evidence(conn, query_id=q2, candidate_id=cid)
    storage.update_query_results(conn, q2, total_count=4, returned_count=4)

    run1 = run_stats(conn, "run_1")
    run2 = run_stats(conn, "run_2")

    assert run1.new_candidates == 3
    assert run2.new_candidates == 2
    assert run2.previously_seen == 2
    assert storage.count_candidates(conn) == 5, "no duplicate candidate rows"

    b_id = make_candidate_id("https://github.com/org/b")
    b_evidence = storage.list_discovery_evidence_for_candidate(conn, b_id)
    assert len(b_evidence) == 2, "query-specific evidence preserved across runs"
    assert {e["run_id"] for e in b_evidence} == {"run_1", "run_2"}


# =============================================================================
# 3. Interrupt / resume: real persisted state, not a mocked flag.
# =============================================================================


def _discovered_candidates(conn, run_id, client, universe, n_repos=4):
    """Run discovery only, returning the n candidates it surfaced."""
    generator = QueryGenerator(universe, windows=("pushed:2026-01-01..2026-03-31",),
                               include_co_occurrence=False)
    DiscoveryEngine(conn, client, generator).run(run_id, tiers=[1], limit=1)
    return storage.list_candidate_ids_for_run(conn, run_id)


def test_3_interrupt_and_resume_matches_an_uninterrupted_run(conn, universe):
    """The core resumability claim: stopping partway through evidence
    collection and restarting produces byte-identical final state to running
    it straight through, and completed candidates are never touched again."""
    repos = {}
    for i in range(4):
        name = f"acme/repo{i}"
        repos[name] = {
            "metadata": repo_metadata(full_name=name, repo_owner="acme",
                                      repo_name=f"repo{i}"),
            "listing": [entry("README.md"), entry("requirements.txt")],
            "files": {
                "README.md": file_at(name, "README.md", "# x\n\nFor our customers.\n"),
                "requirements.txt": file_at(name, "requirements.txt", "docxtpl==1\n"),
            },
            "code_hits": [],
        }
    hits = [Hit(f"acme/repo{i}", rank=i) for i in range(4)]

    # --- Path A: uninterrupted, for comparison -----------------------------
    uninterrupted_db = conn
    storage.create_run(uninterrupted_db, "run_1")
    client_a = ScriptedClient(repos, discovery_hits=hits)
    ids_a = _discovered_candidates(uninterrupted_db, "run_1", client_a, universe)
    collect_for_candidates(EvidenceCollector(uninterrupted_db, client_a, universe), ids_a)
    uninterrupted_rows = {
        cid: dict(storage.get_business_evidence(uninterrupted_db, cid))
        for cid in ids_a
    }

    # --- Path B: interrupted after 2 of 4, then resumed --------------------
    db_path_b = Path(uninterrupted_db.execute("PRAGMA database_list").fetchone()[2])
    # Build a second, identical database for the interrupted path.
    import tempfile
    db_b_path = Path(tempfile.mkdtemp()) / "interrupted.db"
    initialize_database(db_b_path)
    with connect(db_b_path) as conn_b:
        storage.create_run(conn_b, "run_1")
        client_b = ScriptedClient(repos, discovery_hits=hits)
        ids_b = _discovered_candidates(conn_b, "run_1", client_b, universe)

        collector = EvidenceCollector(conn_b, client_b, universe)
        first_batch = ids_b[:2]
        collect_for_candidates(collector, first_batch)  # "crash" after these two

        calls_after_first_batch = list(client_b.calls)

        # "Restart": a fresh collector instance over the SAME connection,
        # asking the database what is still missing rather than being told.
        resumed_collector = EvidenceCollector(conn_b, client_b, universe)
        still_pending = resumed_collector.pending()

        assert set(still_pending) == set(ids_b) - set(first_batch), \
            "resume must process exactly the incomplete candidates"

        collect_for_candidates(resumed_collector, still_pending)

        # The two completed candidates were never touched again.
        calls_after_resume = client_b.calls[len(calls_after_first_batch):]
        touched_again = {
            call[1].split(":")[0] for call in calls_after_resume
            if ":" in call[1] or "/" in call[1]
        }
        for cid in first_batch:
            owner_repo = storage.get_candidate(conn_b, cid)
            full = f"{owner_repo['repo_owner']}/{owner_repo['repo_name']}"
            assert not any(full in t for t in touched_again), \
                f"{full} was re-fetched after already completing"

        interrupted_rows = {
            cid: dict(storage.get_business_evidence(conn_b, cid)) for cid in ids_b
        }
        assert resumed_collector.pending() == [], "nothing should remain pending"

    # --- Compare final state, ignoring the generated_at-equivalent noise ---
    def strip_volatile(row):
        return {k: v for k, v in row.items() if k not in ("candidate_id",)}

    assert {cid: strip_volatile(r) for cid, r in uninterrupted_rows.items()} == \
        {cid: strip_volatile(r) for cid, r in interrupted_rows.items()}, \
        "interrupted-then-resumed state must match an uninterrupted run"


def test_3_no_duplicate_evidence_rows_after_resume(conn, universe):
    repos = {"acme/one": {
        "metadata": repo_metadata(full_name="acme/one", repo_owner="acme", repo_name="one"),
        "listing": [entry("README.md")],
        "files": {"README.md": file_at("acme/one", "README.md", "# x\n")},
        "code_hits": [],
    }}
    client = ScriptedClient(repos, discovery_hits=[Hit("acme/one")])
    storage.create_run(conn, "run_1")
    ids = _discovered_candidates(conn, "run_1", client, universe)

    collector = EvidenceCollector(conn, client, universe)
    collect_for_candidates(collector, ids)
    collect_for_candidates(EvidenceCollector(conn, client, universe), collector.pending())

    rows = conn.execute(
        "SELECT COUNT(*) FROM pipeline_evidence WHERE candidate_id = ?", (ids[0],)
    ).fetchone()[0]
    assert rows == 1


def test_3_cached_responses_are_reused_across_a_resumed_run(conn):
    """Directly at the reliability layer: a request already cached before an
    interruption is served from cache after 'restarting', with no second
    network call."""
    class OneShotTransport:
        def __init__(self):
            self.call_count = 0

        def request(self, method, url, *, params=None, headers=None, timeout=30.0):
            self.call_count += 1
            return HttpResponse(status=200, headers={}, text='{"ok": true}', url=url)

    transport = OneShotTransport()
    policy = ReliabilityPolicy(intervals={}, max_attempts=1)
    cache = SqliteCacheStore(conn)

    # "Before the crash": the request succeeds and is cached.
    requester_before = ReliableRequester(transport, policy, cache=cache, sleep=lambda s: None)
    requester_before.get("https://api.example.com/repo", resource="github_core")
    assert transport.call_count == 1

    # "After restart": a brand new requester, same cache-backed database.
    requester_after = ReliableRequester(transport, policy, cache=cache, sleep=lambda s: None)
    outcome = requester_after.get("https://api.example.com/repo", resource="github_core")

    assert outcome.from_cache is True
    assert transport.call_count == 1, "no second network call after resuming"


# =============================================================================
# 4. Cache test.
# =============================================================================


class ClockedTransport:
    def __init__(self, *responses):
        self._queue = list(responses)
        self.call_count = 0

    def request(self, method, url, *, params=None, headers=None, timeout=30.0):
        self.call_count += 1
        return self._queue.pop(0)


def test_4_successful_response_is_cached_and_reused(conn):
    transport = ClockedTransport(
        HttpResponse(status=200, headers={}, text='{"n":1}', url="https://x"))
    policy = ReliabilityPolicy(intervals={}, max_attempts=1)
    requester = ReliableRequester(transport, policy, cache=SqliteCacheStore(conn),
                                  sleep=lambda s: None)

    requester.get("https://api.example.com/y", resource="github_core")
    second = requester.get("https://api.example.com/y", resource="github_core")

    assert transport.call_count == 1
    assert second.from_cache is True


def test_4_expired_ttl_triggers_a_fresh_request(conn):
    transport = ClockedTransport(
        HttpResponse(status=200, headers={}, text='{"n":1}', url="https://x"),
        HttpResponse(status=200, headers={}, text='{"n":2}', url="https://x"))
    policy = ReliabilityPolicy(intervals={}, max_attempts=1, cache_ttl_seconds=0.0)
    requester = ReliableRequester(transport, policy, cache=SqliteCacheStore(conn),
                                  sleep=lambda s: None)

    requester.get("https://api.example.com/z", resource="github_core")
    second = requester.get("https://api.example.com/z", resource="github_core")

    assert transport.call_count == 2
    assert second.from_cache is False


def test_4_ttl_is_measured_correctly_by_is_fresh():
    from datetime import datetime, timedelta, timezone

    now = datetime.now(timezone.utc)
    assert is_fresh((now - timedelta(days=1)).isoformat(), 7 * 24 * 3600) is True
    assert is_fresh((now - timedelta(days=10)).isoformat(), 7 * 24 * 3600) is False


def test_4_secrets_never_appear_in_cache_keys_or_data(conn):
    from dependency_map.reliability import cache_key

    transport = ClockedTransport(
        HttpResponse(status=200, headers={}, text='{"ok":true}', url="https://x"))
    policy = ReliabilityPolicy(intervals={}, max_attempts=1)
    requester = ReliableRequester(transport, policy, cache=SqliteCacheStore(conn),
                                  sleep=lambda s: None)

    requester.get("https://libraries.io/api/pypi/x", resource="libraries_io",
                  params={"api_key": FAKE_KEY})

    key = cache_key("GET", "https://libraries.io/api/pypi/x", {"api_key": FAKE_KEY})
    row = storage.get_api_cache(conn, key)

    assert FAKE_KEY not in key
    assert row is not None
    assert FAKE_KEY not in row["response_json"]

    raw_dump = "".join(
        str(dict(r)) for r in conn.execute("SELECT * FROM api_cache")
    )
    assert FAKE_KEY not in raw_dump


# =============================================================================
# 5. Report consistency (see also section 1's tests, which cover the same
#    ground against the full mixed-status pipeline).
# =============================================================================


def test_5_report_consistency_across_a_larger_seeded_set(conn, run_id, weights_and_caps):
    """CSV and Markdown generated once from one seeded database must agree on
    every field, for more candidates than the minimal fixtures use."""
    weights, caps = weights_and_caps
    for i in range(5):
        name = f"org/cand{i}"
        cid = make_candidate_id(f"https://github.com/{name}")
        owner, repo = name.split("/")
        qid = storage.create_discovery_query(
            conn, run_id=run_id, discovery_source="github_code_search",
            query=f"q{i}", library_name="docxtpl (python-docx-template)",
            discovery_tier=2)
        storage.insert_candidate_if_new(
            conn, candidate_id=cid, repo_url=normalize_repo_url(f"https://github.com/{name}"),
            repo_owner=owner, repo_name=repo, first_seen_run_id=run_id)
        storage.insert_discovery_evidence(conn, query_id=qid, candidate_id=cid)
        storage.insert_dependency_found(
            conn, candidate_id=cid, library_name="docxtpl", library_category="docx",
            direction="generation", detection_method="code_import",
            evidence_url=f"https://github.com/{name}/blob/main/a.py")
        storage.upsert_pipeline_evidence(
            conn, candidate_id=cid, code_usage_confirmed=True,
            template_directory_present=(i % 2 == 0),
            multiple_document_types_handled=False, pipeline_stage_count=1 + i % 3,
            infrastructure_service_present=False, pipeline_evidence_notes="")
        storage.upsert_business_evidence(
            conn, candidate_id=cid, readme_describes_product=True,
            readme_excerpt="For our customers.", website_exists=True,
            application_code_exists=True,
            document_functionality_in_production_code=True,
            stars=i * 10, last_commit_date="2026-07-01", contributor_count=None,
            business_evidence_notes="")
        status = "reject" if i == 4 else ("keep" if i == 0 else "investigate")
        storage.upsert_qualification(
            conn, candidate_id=cid, qualification_status=status,
            qualification_reason="r",
            rejection_reason="tutorial_or_demo" if status == "reject" else None,
            confidence="medium")
        if status != "reject":
            ScoringEngine(conn, weights, caps).score_one(cid)

    data = gather_report_data(conn)
    csv_rows = list(csv.DictReader(io.StringIO(render_csv(data))))
    md = render_markdown(data)

    assert len(data.ranked) == 4  # 5 minus the one reject
    assert len(csv_rows) == 4
    for candidate, row in zip(data.ranked, csv_rows):
        assert candidate.candidate_id == row["candidate_id"]
        assert str(candidate.row["final_score"]) == row["final_score"]
        assert candidate.row["confidence_band"] == row["confidence_band"]
        assert candidate.row["qualification_status"] == row["qualification_status"]
        assert candidate.evidence_coverage_fraction == row["evidence_coverage"]
        assert candidate.repo_full_name in md

    assert "cand4" not in md
    assert "cand4" not in render_csv(data)


# =============================================================================
# 6. Schema / data-integrity test.
# =============================================================================


def test_6_schema_version_is_3(conn):
    assert SCHEMA_VERSION == 3
    assert conn.execute("SELECT version FROM schema_version").fetchone()[0] == 3


def test_6_foreign_keys_are_active(conn):
    assert conn.execute("PRAGMA foreign_keys").fetchone()[0] == 1


def test_6_candidate_id_is_unique(conn, run_id):
    import sqlite3
    conn.execute(
        "INSERT INTO candidates (candidate_id, repo_url, repo_owner, repo_name) "
        "VALUES ('c_dup', 'https://x/a', 'a', 'a')")
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO candidates (candidate_id, repo_url, repo_owner, repo_name) "
            "VALUES ('c_dup', 'https://x/b', 'b', 'b')")


def test_6_query_id_is_unique_per_slice(conn, run_id):
    import sqlite3
    storage.create_discovery_query(conn, run_id=run_id, discovery_source="github_code_search",
                                   query="q", search_window="w1")
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO discovery_queries (query_id, run_id, discovery_source, "
            "query, search_window, executed_at) VALUES "
            "(?, ?, 'github_code_search', 'q', 'w1', 'now')",
            (storage.make_query_id(run_id, "q", "w1"), run_id))


def test_6_query_candidate_relationship_requires_both(conn):
    import sqlite3
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO discovery_evidence (query_id, candidate_id) VALUES "
            "('ghost_q', 'ghost_c')")


def test_6_score_relationship_is_one_to_one_with_candidate(conn, run_id, candidate_id):
    columns = {r["name"] for r in conn.execute("PRAGMA table_info(scores)")}
    pk = [r["name"] for r in conn.execute("PRAGMA table_info(scores)") if r["pk"]]
    assert pk == ["candidate_id"]


def test_6_qualification_relationship_is_one_to_one_with_candidate(conn):
    pk = [r["name"] for r in conn.execute("PRAGMA table_info(qualification)") if r["pk"]]
    assert pk == ["candidate_id"]


def test_6_invalid_industry_category_is_rejected(conn):
    import sqlite3
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO candidates (candidate_id, repo_url, repo_owner, repo_name, "
            "industry_category) VALUES ('c_x', 'https://x/y', 'x', 'y', 'not_real')")


def test_6_invalid_qualification_status_is_rejected(conn, candidate_id):
    import sqlite3
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO qualification (candidate_id, qualification_status, "
            "qualification_reason, confidence) VALUES (?, 'maybe', 'r', 'high')",
            (candidate_id,))


def test_6_invalid_dimension_score_is_rejected(conn, candidate_id):
    import sqlite3
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_score(
            conn, candidate_id=candidate_id,
            **{d: (6 if d == "document_volume" else 0) for d in SCORING_DIMENSIONS},
            raw_weighted_score=0.0, final_score=0, confidence_band="low")


@pytest.mark.parametrize("cap", [-1, 101])
def test_6_invalid_gate_cap_outside_0_100_is_rejected(conn, candidate_id, cap):
    import sqlite3
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_score(
            conn, candidate_id=candidate_id,
            **{d: 0 for d in SCORING_DIMENSIONS},
            raw_weighted_score=0.0, final_score=0, confidence_band="low",
            gate_cap_applied=cap)


@pytest.mark.parametrize("cap", [0, 20, 33, 100])
def test_6_gate_cap_within_0_100_is_accepted(conn, candidate_id, cap):
    storage.upsert_score(
        conn, candidate_id=candidate_id,
        **{d: 0 for d in SCORING_DIMENSIONS},
        raw_weighted_score=0.0, final_score=0, confidence_band="low",
        gate_cap_applied=cap)
    assert storage.get_score(conn, candidate_id)["gate_cap_applied"] == cap


# =============================================================================
# 7. Security test.
# =============================================================================


def test_7_fake_secret_never_appears_in_generated_outputs(
    conn, universe, full_pipeline_client, weights_and_caps, monkeypatch, caplog
):
    monkeypatch.setenv("GITHUB_TOKEN", FAKE_TOKEN)
    monkeypatch.setenv("LIBRARIES_IO_API_KEY", FAKE_KEY)
    caplog.set_level("DEBUG")

    run_full_pipeline(conn, universe, full_pipeline_client, weights_and_caps)
    data = gather_report_data(conn)
    csv_text = render_csv(data)
    md_text = render_markdown(data)

    for secret in (FAKE_TOKEN, FAKE_KEY):
        assert secret not in csv_text
        assert secret not in md_text
        assert secret not in caplog.text

    dump = "".join(
        str(dict(r)) for table in
        ("candidates", "scores", "qualification", "discovery_queries", "api_cache")
        for r in conn.execute(f"SELECT * FROM {table}")
    )
    for secret in (FAKE_TOKEN, FAKE_KEY):
        assert secret not in dump, f"{secret} leaked into the database"


def test_7_progress_md_contains_no_secret_pattern():
    text = Path("PROGRESS.md").read_text(encoding="utf-8")
    for pattern in [r"ghp_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}",
                    r"(?i)api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9]{16,}"]:
        assert not re.search(pattern, text), f"PROGRESS.md matches {pattern}"


def test_7_config_yaml_contains_no_secret_values():
    text = Path("config/config.yaml").read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    assert "GITHUB_TOKEN" not in data
    assert "LIBRARIES_IO_API_KEY" not in data
    assert "ghp_" not in text


def test_7_weights_yaml_contains_no_secret_values():
    text = Path("config/weights.yaml").read_text(encoding="utf-8")
    assert "GITHUB_TOKEN" not in text
    assert "ghp_" not in text
    assert "api_key" not in text.lower()


def _git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True,
                          cwd=Path(__file__).resolve().parents[1])


def test_7_env_remains_gitignored():
    result = _git("check-ignore", "-q", ".env")
    assert result.returncode == 0, "'.env' must be gitignored"


def test_7_database_files_remain_gitignored():
    result = _git("check-ignore", "-q", "data/dependency_map.db")
    assert result.returncode == 0, "'data/*.db' must be gitignored"


def test_7_venv_remains_gitignored():
    result = _git("check-ignore", "-q", ".venv/somefile")
    assert result.returncode == 0, "'.venv/' must be gitignored"


def test_7_outputs_directory_is_not_gitignored():
    """The opposite check: the deliverables must NOT be swept up by any of
    the ignore rules above."""
    result = _git("check-ignore", "-q", "outputs/ranked-candidates.csv")
    assert result.returncode == 1, "outputs/ must remain tracked"


# =============================================================================
# 9. CLI smoke / stage test, fully offline via a generic fake transport.
# =============================================================================


def _write_config(config_dir: Path, db_path: Path, out_dir: Path):
    config_dir.mkdir(parents=True, exist_ok=True)
    (config_dir / "config.yaml").write_text(f"""
paths:
  database: {db_path.as_posix()}
  library_universe: data/library-universe.yaml
  output_csv: {(out_dir / 'out.csv').as_posix()}
  output_markdown: {(out_dir / 'out.md').as_posix()}
cache:
  ttl_days: 7
pacing:
  github_code_search_min_interval_seconds: 0.0
  github_search_min_interval_seconds: 0.0
  github_rest_min_interval_seconds: 0.0
  libraries_io_min_interval_seconds: 0.0
retry:
  max_attempts: 3
  backoff_base_seconds: 0.0
  backoff_jitter_seconds: 0.0
  backoff_max_seconds: 1.0
""", encoding="utf-8")
    (config_dir / "weights.yaml").write_text(WEIGHTS_PATH.read_text(encoding="utf-8"),
                                             encoding="utf-8")


@pytest.fixture
def cli_env(tmp_path, monkeypatch):
    config_dir = tmp_path / "config"
    db_path = tmp_path / "t.db"
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    _write_config(config_dir, db_path, out_dir)
    initialize_database(db_path)
    monkeypatch.setenv("GITHUB_TOKEN", FAKE_TOKEN)
    return config_dir, db_path, out_dir


def test_9_cli_help():
    from dependency_map.cli import cli
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output


def test_9_cli_run_help():
    from dependency_map.cli import cli
    result = CliRunner().invoke(cli, ["run", "--help"])
    assert result.exit_code == 0
    assert "--stage" in result.output


def test_9_cli_run_discovery_stage_offline(cli_env, monkeypatch):
    from dependency_map.cli import cli
    config_dir, db_path, out_dir = cli_env

    routes = {
        "/search/code": json_response({
            "total_count": 1,
            "items": [{"path": "requirements.txt", "sha": "a",
                      "html_url": "https://github.com/acme/widget/blob/main/requirements.txt",
                      "repository": {"full_name": "acme/widget",
                                    "html_url": "https://github.com/acme/widget"}}],
        }),
    }
    monkeypatch.setattr("dependency_map.reliability.RequestsTransport",
                        build_fake_transport(routes))

    result = CliRunner().invoke(cli, ["--config-dir", str(config_dir), "run",
                                      "--stage", "discovery", "--tier", "1",
                                      "--query-limit", "1"])

    assert result.exit_code == 0, result.output
    with connect(db_path) as conn:
        assert storage.count_candidates(conn) >= 1


def test_9_cli_run_evidence_stage_offline(cli_env, monkeypatch):
    from dependency_map.cli import cli
    config_dir, db_path, out_dir = cli_env

    with connect(db_path) as conn:
        storage.create_run(conn, "run_1")
        qid = storage.create_discovery_query(
            conn, run_id="run_1", discovery_source="github_code_search",
            query="q", discovery_tier=1)
        cid = make_candidate_id("https://github.com/acme/widget")
        storage.insert_candidate_if_new(
            conn, candidate_id=cid, repo_url="https://github.com/acme/widget",
            repo_owner="acme", repo_name="widget", first_seen_run_id="run_1")
        storage.insert_discovery_evidence(conn, query_id=qid, candidate_id=cid)

    routes = {
        "/repos/acme/widget/contents/README.md": json_response({
            "path": "README.md", "sha": "a", "size": 10, "encoding": "base64",
            "content": b64("# widget\n\nFor our customers.\n"),
            "html_url": "https://github.com/acme/widget/blob/main/README.md"}),
        "/repos/acme/widget/contents": json_response([
            {"name": "README.md", "path": "README.md", "type": "file"},
        ]),
        "/repos/acme/widget": json_response({
            "full_name": "acme/widget", "name": "widget",
            "owner": {"login": "acme"},
            "html_url": "https://github.com/acme/widget", "fork": False,
            "archived": False, "language": "Python", "stargazers_count": 1,
            "forks_count": 0, "description": "", "homepage": None,
            "default_branch": "main", "pushed_at": "2026-01-01T00:00:00Z",
            "created_at": "2024-01-01T00:00:00Z"}),
        "/search/code": json_response({"total_count": 0, "items": []}),
    }
    monkeypatch.setattr("dependency_map.reliability.RequestsTransport",
                        build_fake_transport(routes))

    result = CliRunner().invoke(cli, ["--config-dir", str(config_dir), "run",
                                      "--run-id", "run_1", "--stage", "evidence"])

    assert result.exit_code == 0, result.output
    with connect(db_path) as conn:
        assert storage.get_business_evidence(conn, cid) is not None


def test_9_cli_run_qualification_stage_needs_no_token(cli_env, monkeypatch):
    """The bug this phase found and fixed: qualification makes no network
    calls, so it must not require GITHUB_TOKEN."""
    from dependency_map.cli import cli
    config_dir, db_path, out_dir = cli_env
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)

    with connect(db_path) as conn:
        storage.create_run(conn, "run_1")
        cid = make_candidate_id("https://github.com/acme/widget")
        storage.insert_candidate_if_new(
            conn, candidate_id=cid, repo_url="https://github.com/acme/widget",
            repo_owner="acme", repo_name="widget", first_seen_run_id="run_1")
        storage.upsert_pipeline_evidence(
            conn, candidate_id=cid, code_usage_confirmed=False,
            template_directory_present=False, multiple_document_types_handled=False,
            pipeline_stage_count=0, infrastructure_service_present=False,
            pipeline_evidence_notes="")
        storage.upsert_business_evidence(
            conn, candidate_id=cid, readme_describes_product=True,
            readme_excerpt="x", website_exists=False,
            application_code_exists=True,
            document_functionality_in_production_code=False,
            stars=1, last_commit_date="2026-01-01", contributor_count=None,
            business_evidence_notes="")

    result = CliRunner().invoke(cli, ["--config-dir", str(config_dir), "run",
                                      "--run-id", "run_1", "--stage", "qualification"])

    assert result.exit_code == 0, result.output
    with connect(db_path) as conn:
        assert storage.get_qualification(conn, cid) is not None


def test_9_cli_run_scoring_stage_needs_no_token(cli_env, monkeypatch):
    from dependency_map.cli import cli
    config_dir, db_path, out_dir = cli_env
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)

    with connect(db_path) as conn:
        storage.create_run(conn, "run_1")
        cid = make_candidate_id("https://github.com/acme/widget")
        storage.insert_candidate_if_new(
            conn, candidate_id=cid, repo_url="https://github.com/acme/widget",
            repo_owner="acme", repo_name="widget", first_seen_run_id="run_1")
        storage.upsert_qualification(
            conn, candidate_id=cid, qualification_status="keep",
            qualification_reason="r", confidence="high")

    result = CliRunner().invoke(cli, ["--config-dir", str(config_dir), "run",
                                      "--run-id", "run_1", "--stage", "scoring"])

    assert result.exit_code == 0, result.output
    with connect(db_path) as conn:
        assert storage.get_score(conn, cid) is not None


def test_9_cli_report(cli_env):
    from dependency_map.cli import cli
    config_dir, db_path, out_dir = cli_env

    with connect(db_path) as conn:
        storage.create_run(conn, "run_1")
        cid = make_candidate_id("https://github.com/acme/widget")
        storage.insert_candidate_if_new(
            conn, candidate_id=cid, repo_url="https://github.com/acme/widget",
            repo_owner="acme", repo_name="widget", first_seen_run_id="run_1")
        storage.upsert_qualification(
            conn, candidate_id=cid, qualification_status="keep",
            qualification_reason="r", confidence="high")
        storage.upsert_score(
            conn, candidate_id=cid, **{d: 3 for d in SCORING_DIMENSIONS},
            raw_weighted_score=3.0, final_score=60, confidence_band="high")

    result = CliRunner().invoke(cli, ["--config-dir", str(config_dir), "report",
                                      "--run-id", "run_1"])

    assert result.exit_code == 0, result.output
    assert (out_dir / "out.csv").exists()
    assert (out_dir / "out.md").exists()


# =============================================================================
# 10. Idempotency test.
# =============================================================================


def test_10_running_each_stage_twice_produces_no_duplicates(
    conn, universe, full_pipeline_client, weights_and_caps
):
    run_full_pipeline(conn, universe, full_pipeline_client, weights_and_caps)

    counts_before = {
        table: conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        for table in ("candidates", "pipeline_evidence", "business_evidence",
                      "qualification", "scores")
    }

    # Rerun evidence/qualification/scoring: everything is already complete, so
    # each engine's own pending() should find nothing left to do.
    weights, caps = weights_and_caps
    assert EvidenceCollector(conn, full_pipeline_client, universe).pending() == []
    assert QualificationEngine(conn).pending() == []
    assert ScoringEngine(conn, weights, caps).pending() == []

    QualificationEngine(conn).run()
    ScoringEngine(conn, weights, caps).run()

    counts_after = {
        table: conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        for table in counts_before
    }
    assert counts_before == counts_after


def test_10_report_generation_twice_produces_identical_files(
    conn, universe, full_pipeline_client, weights_and_caps, tmp_path
):
    run_full_pipeline(conn, universe, full_pipeline_client, weights_and_caps)

    write_report(conn, tmp_path / "a.csv", tmp_path / "a.md")
    first_csv = (tmp_path / "a.csv").read_text(encoding="utf-8")

    write_report(conn, tmp_path / "b.csv", tmp_path / "b.md")
    second_csv = (tmp_path / "b.csv").read_text(encoding="utf-8")

    assert first_csv == second_csv


# =============================================================================
# 11. Pipeline failure tests.
# =============================================================================


def test_11_one_candidate_failure_does_not_corrupt_others(conn, universe):
    repos = {
        "acme/good": {
            "metadata": repo_metadata(full_name="acme/good", repo_owner="acme",
                                      repo_name="good"),
            "listing": [entry("README.md")],
            "files": {"README.md": file_at("acme/good", "README.md", "# x\n")},
            "code_hits": [],
        },
    }
    client = ScriptedClient(
        repos, discovery_hits=[Hit("acme/good"), Hit("acme/bad")],
        fail={"metadata": {"acme/bad": ApiError(500, "https://x", "boom")}})
    storage.create_run(conn, "run_1")
    ids = _discovered_candidates(conn, "run_1", client, universe)

    outcomes = collect_for_candidates(EvidenceCollector(conn, client, universe), ids)

    ok = [o for o in outcomes if o.ok]
    failed = [o for o in outcomes if not o.ok]
    assert len(ok) == 1
    assert len(failed) == 1
    good_id = make_candidate_id("https://github.com/acme/good")
    assert storage.get_business_evidence(conn, good_id) is not None


def test_11_systemic_failure_stops_the_batch(conn, universe):
    from dependency_map.evidence import EvidenceError

    repos = {"acme/x": {
        "metadata": repo_metadata(full_name="acme/x", repo_owner="acme", repo_name="x"),
        "listing": [], "files": {}, "code_hits": [],
    }}
    client = ScriptedClient(
        repos, discovery_hits=[Hit("acme/x")],
        fail={"metadata": {"acme/x": RateLimited("budget exhausted")}})
    storage.create_run(conn, "run_1")
    ids = _discovered_candidates(conn, "run_1", client, universe)

    with pytest.raises(RateLimited):
        collect_for_candidates(EvidenceCollector(conn, client, universe), ids)


def test_11_malformed_search_result_does_not_corrupt_the_database(conn):
    """A code-search hit missing the 'repository' key must not produce a
    half-written candidate row."""
    client = GitHubClient(
        ReliableRequester(
            ClockedTransport(json_response({
                "total_count": 1,
                "items": [{"path": "x.py", "sha": "a", "html_url": "https://x"}],
            })),
            ReliabilityPolicy(intervals={}, max_attempts=1),
            cache=MemoryCacheStore(), sleep=lambda s: None),
        token=FAKE_TOKEN)

    page = client.search_code("q")
    # Missing repository -> empty full_name, not a crash and not a fabricated
    # candidate with a real-looking identity.
    assert page.results[0].repo_full_name == ""
    assert storage.count_candidates(conn) == 0


def test_11_report_generation_fails_cleanly_when_the_database_has_no_schema():
    import sqlite3
    import tempfile

    empty_db = Path(tempfile.mkdtemp()) / "empty.db"
    conn = sqlite3.connect(empty_db)
    conn.row_factory = sqlite3.Row
    try:
        with pytest.raises(ReportError):
            write_report(conn, empty_db.parent / "c.csv", empty_db.parent / "r.md")
    finally:
        conn.close()


def test_11_schema_version_mismatch_fails_clearly(tmp_path):
    db_path = tmp_path / "mismatched.db"
    initialize_database(db_path)
    with connect(db_path) as conn:
        conn.execute("UPDATE schema_version SET version = 99 WHERE id = 1")

    with pytest.raises(SchemaVersionMismatch):
        with open_database(db_path):
            pass


def test_11_uninitialized_database_fails_clearly(tmp_path):
    import sqlite3

    db_path = tmp_path / "blank.db"
    sqlite3.connect(db_path).close()

    with pytest.raises(DatabaseNotInitialized):
        with open_database(db_path):
            pass


# =============================================================================
# 12. Coverage / undercount test.
# =============================================================================


def test_12_a_75648_result_query_is_never_reported_as_fully_inspected(
    conn, universe, weights_and_caps
):
    weights, caps = weights_and_caps
    storage.create_run(conn, "run_1")
    qid = storage.create_discovery_query(
        conn, run_id="run_1", discovery_source="github_code_search",
        query='"python-docx" filename:requirements.txt', library_name="python-docx",
        discovery_tier=3, search_window="pushed:2026-04-01..2026-06-30",
        total_count=75648, returned_count=10, capped=True)
    cid = make_candidate_id("https://github.com/acme/widget")
    storage.insert_candidate_if_new(
        conn, candidate_id=cid, repo_url="https://github.com/acme/widget",
        repo_owner="acme", repo_name="widget", first_seen_run_id="run_1")
    storage.insert_discovery_evidence(conn, query_id=qid, candidate_id=cid,
                                      discovery_result_rank=1)
    storage.upsert_qualification(
        conn, candidate_id=cid, qualification_status="investigate",
        qualification_reason="r", confidence="low")
    ScoringEngine(conn, weights, caps).score_one(cid)

    md = render_markdown(gather_report_data(conn))

    assert "75,648" in md
    assert "Sampled 10 of 75,648" in md
    assert "partial sample" in md
    assert "75,648 repositories were inspected" not in md
    assert "75,648 inspected" not in md


# =============================================================================
# 13. Fresh-batch test.
# =============================================================================


def test_13_run_two_query_set_differs_from_run_one(universe):
    run1 = plan_rotation(1)
    run2 = plan_rotation(2)
    gen1 = QueryGenerator(universe, windows=run1.windows,
                          library_offset=run1.library_offset)
    gen2 = QueryGenerator(universe, windows=run2.windows,
                          library_offset=run2.library_offset)

    q1 = {q.query for q in gen1.generate(tiers=[3])}
    q2 = {q.query for q in gen2.generate(tiers=[3])}

    assert q1
    assert q1.isdisjoint(q2)


def test_13_fresh_batch_guard_blocks_a_duplicated_plan_before_any_api_call(conn):
    """The critical property: the guard must fire before a single request is
    sent, proven here by a transport that would raise if ever called."""
    class ExplodingTransport:
        def request(self, *a, **k):
            raise AssertionError("no request should have been sent")

    storage.create_run(conn, "run_1", started_at="2026-01-01T00:00:00Z")
    storage.create_discovery_query(
        conn, run_id="run_1", discovery_source="github_code_search",
        query="same query", search_window="w1", total_count=5, returned_count=5)

    storage.create_run(conn, "run_2", started_at="2026-02-01T00:00:00Z")
    planned = [GeneratedQuery("same query", 3, search_window="w1")]

    with pytest.raises(FreshBatchError):
        verify_fresh_batch(conn, "run_2", planned)

    # No transport was ever constructed into a client and called; the guard
    # fired purely from stored query records, before any engine ran.
    transport = ExplodingTransport()  # never invoked, by construction above


def test_13_partial_overlap_between_runs_is_allowed(conn):
    storage.create_run(conn, "run_1", started_at="2026-01-01T00:00:00Z")
    storage.create_discovery_query(
        conn, run_id="run_1", discovery_source="github_code_search",
        query="q1", search_window="w1")

    storage.create_run(conn, "run_2", started_at="2026-02-01T00:00:00Z")
    planned = [GeneratedQuery("q1", 3, search_window="w1"),
              GeneratedQuery("q2", 3, search_window="w2")]

    check = verify_fresh_batch(conn, "run_2", planned)
    assert check.is_fresh
    assert check.novel == 1


# =============================================================================
# 14. Phase 13 correction pass: valid tier-3 slicing, and discovery that
#     commits as it goes. Both cover defects the first live run exposed and
#     the mocked suite could not: a fake client answers whatever query it is
#     handed, so query *validity against the real API* was never checked here.
# =============================================================================


def test_14_no_generated_query_contains_pushed(universe):
    """The exact defect: 220 of run 1's 237 queries carried `pushed:` and all
    of them returned zero."""
    generator = QueryGenerator(universe, windows=plan_rotation(1).windows)

    for generated in generator.generate(tiers=(1, 2, 3)):
        assert "pushed:" not in generated.query, generated.query
        assert generated.search_window is None or \
            "pushed:" not in generated.search_window


@pytest.mark.parametrize("qualifier", [
    "pushed:2026-01-01..2026-03-31", "created:>2026-01-01", "stars:>100",
    "forks:>10", "fork:false", "topic:documents", "license:mit",
    "archived:false", "is:public",
])
def test_14_repository_only_qualifiers_are_refused(qualifier):
    """Code search does not implement these. It matches them as literal text
    and returns a truthful-looking zero, so generation must refuse them."""
    from dependency_map.discovery import InvalidQuery, validate_query

    with pytest.raises(InvalidQuery, match="repository search"):
        validate_query('"python-docx" filename:requirements.txt ' + qualifier)


def test_14_tier_three_queries_use_only_supported_slicing(universe):
    """Every tier-3 slice must be a `size:` bucket drawn from the pool."""
    from dependency_map.dedup import SIZE_BUCKETS

    generator = QueryGenerator(universe, windows=plan_rotation(1).windows)
    tier_three = list(generator.generate(tiers=[3]))

    assert tier_three
    for generated in tier_three:
        assert generated.search_window in SIZE_BUCKETS, generated.search_window
        assert generated.search_window in generated.query


def test_14_generated_queries_pass_their_own_validator(universe):
    """generate() validates, so this asserts the validator is actually wired
    in rather than merely present."""
    from dependency_map.discovery import validate_query

    generator = QueryGenerator(universe, windows=plan_rotation(1).windows)
    for generated in generator.generate(tiers=(1, 2, 3)):
        validate_query(generated.query)


def test_14_slicing_is_deterministic_across_generators(universe):
    """Same run index, same queries, in the same order."""
    plan = plan_rotation(1)
    a = QueryGenerator(universe, windows=plan.windows,
                       library_offset=plan.library_offset)
    b = QueryGenerator(universe, windows=plan.windows,
                       library_offset=plan.library_offset)

    assert [q.query for q in a.generate(tiers=(1, 2, 3))] == \
        [q.query for q in b.generate(tiers=(1, 2, 3))]


def test_14_multiple_manifest_and_size_slices_are_distinct(universe):
    """The manifest family and the size bucket are independent axes, so a
    library with several manifests yields distinct queries per bucket rather
    than collapsing them."""
    generator = QueryGenerator(universe, windows=plan_rotation(1).windows,
                               include_co_occurrence=False)
    by_library = {}
    for generated in generator.generate(tiers=[3]):
        by_library.setdefault(generated.library_name, []).append(generated.query)

    multi = {k: v for k, v in by_library.items() if len(v) > 4}
    assert multi, "expected at least one library with several manifest files"
    for library, queries in multi.items():
        assert len(queries) == len(set(queries)), library


class _FailingClient(ScriptedClient):
    """Discovery client that raises on one specific query."""

    def __init__(self, repos, discovery_hits, fail_on):
        super().__init__(repos, discovery_hits=discovery_hits)
        self._fail_on = fail_on

    def search_code(self, query, per_page=30, page=1, use_cache=True):
        if self._fail_on is not None and self._fail_on in query:
            raise ApiError(500, "https://api.github.com/search/code", "boom")
        return super().search_code(query, per_page=per_page, page=page,
                                   use_cache=use_cache)


_ONE_REPO = {
    "acme/one": {
        "metadata": None,  # filled in per test
        "listing": [],
        "files": {},
        "code_hits": [],
    }
}


def _one_repo():
    return {
        "acme/one": {
            "metadata": repo_metadata(full_name="acme/one", repo_owner="acme",
                                      repo_name="one"),
            "listing": [],
            "files": {},
            "code_hits": [],
        }
    }


def test_14_interrupted_discovery_keeps_the_queries_it_finished(tmp_path, universe):
    """The run-1 defect: the whole stage shared one transaction, so an abort
    in the twenty-sixth minute discarded twenty-six minutes of API budget.

    Uses a real on-disk database and a real rollback, not a mocked flag.
    """
    db_file = tmp_path / "interrupt.db"
    initialize_database(db_file)

    generator = QueryGenerator(universe, windows=("size:0..250",),
                               include_co_occurrence=False)
    planned = generator.generate(tiers=[3])
    assert len(planned) > 3, "need several queries to interrupt partway"
    doomed = planned[2].query

    class Boom(Exception):
        pass

    try:
        with connect(db_file) as conn:
            storage.create_run(conn, "run_1")
            conn.commit()
            client = _FailingClient(_one_repo(), [Hit("acme/one")], doomed)
            engine = DiscoveryEngine(conn, client, generator,
                                     max_consecutive_failures=1)
            try:
                engine.run("run_1", tiers=[3])
            except DiscoveryError:
                raise Boom()
    except Boom:
        pass

    with connect(db_file) as conn:
        completed = storage.completed_query_ids(conn, "run_1")

    assert len(completed) >= 2, (
        "only %d queries survived the interruption; completed work must not "
        "be rolled back" % len(completed)
    )


def test_14_resuming_discovery_does_not_repeat_completed_queries(tmp_path, universe):
    db_file = tmp_path / "resume.db"
    initialize_database(db_file)
    generator = QueryGenerator(universe, windows=("size:0..250",),
                               include_co_occurrence=False)

    with connect(db_file) as conn:
        storage.create_run(conn, "run_1")
        client = ScriptedClient(_one_repo(), discovery_hits=[Hit("acme/one")])
        first = DiscoveryEngine(conn, client, generator).run(
            "run_1", tiers=[3], limit=3)
        searches_first = len([c for c in client.calls if c[0] == "search"])

    with connect(db_file) as conn:
        client2 = ScriptedClient(_one_repo(), discovery_hits=[Hit("acme/one")])
        second = DiscoveryEngine(conn, client2, generator).run(
            "run_1", tiers=[3], limit=3)

    assert first.queries_executed == 3
    assert searches_first == 3
    assert second.queries_skipped == 3, "already-answered queries must be skipped"
    assert second.queries_executed == 0
    assert len([c for c in client2.calls if c[0] == "search"]) == 0, \
        "a resumed run must spend no API budget on completed queries"


def test_14_resume_creates_no_duplicate_queries_or_evidence(tmp_path, universe):
    db_file = tmp_path / "dupes.db"
    initialize_database(db_file)
    generator = QueryGenerator(universe, windows=("size:0..250",),
                               include_co_occurrence=False)

    for _ in range(3):
        with connect(db_file) as conn:
            if storage.get_run(conn, "run_1") is None:
                storage.create_run(conn, "run_1")
            DiscoveryEngine(
                conn, ScriptedClient(_one_repo(), discovery_hits=[Hit("acme/one")]),
                generator).run("run_1", tiers=[3], limit=3)

    with connect(db_file) as conn:
        queries = conn.execute(
            "SELECT COUNT(*) FROM discovery_queries WHERE run_id='run_1'"
        ).fetchone()[0]
        evidence = conn.execute(
            "SELECT COUNT(*) FROM discovery_evidence").fetchone()[0]
        candidates = storage.count_candidates(conn)

    assert queries == 3
    assert evidence == 3, "one row per (query, candidate), not one per attempt"
    assert candidates == 1


def test_14_a_resumed_run_preserves_its_stored_totals(tmp_path, universe):
    """create_discovery_query upserts, so re-creating a completed query's row
    would overwrite a real total_count with null. Skipping happens first."""
    db_file = tmp_path / "totals.db"
    initialize_database(db_file)
    generator = QueryGenerator(universe, windows=("size:0..250",),
                               include_co_occurrence=False)

    class BigPage(ScriptedClient):
        def search_code(self, query, per_page=30, page=1, use_cache=True):
            self.calls.append(("search", query))
            return Page([Hit("acme/one")], total=4242)

    with connect(db_file) as conn:
        storage.create_run(conn, "run_1")
        DiscoveryEngine(conn, BigPage(_one_repo(), discovery_hits=[]),
                        generator).run("run_1", tiers=[3], limit=1)

    with connect(db_file) as conn:
        DiscoveryEngine(conn, BigPage(_one_repo(), discovery_hits=[]),
                        generator).run("run_1", tiers=[3], limit=1)
        row = conn.execute(
            "SELECT total_count FROM discovery_queries WHERE run_id='run_1'"
        ).fetchone()

    assert row["total_count"] == 4242


def test_14_a_failed_query_is_retried_on_resume(tmp_path, universe):
    """A failure leaves total_count null on purpose, which is what marks it as
    unfinished rather than as a genuine zero."""
    db_file = tmp_path / "retry.db"
    initialize_database(db_file)
    generator = QueryGenerator(universe, windows=("size:0..250",),
                               include_co_occurrence=False)
    doomed = generator.generate(tiers=[3])[0].query

    with connect(db_file) as conn:
        storage.create_run(conn, "run_1")
        client = _FailingClient(_one_repo(), [Hit("acme/one")], doomed)
        report = DiscoveryEngine(conn, client, generator).run(
            "run_1", tiers=[3], limit=1)
        assert report.queries_failed == 1

    with connect(db_file) as conn:
        assert storage.completed_query_ids(conn, "run_1") == set()
        report = DiscoveryEngine(
            conn, ScriptedClient(_one_repo(), discovery_hits=[Hit("acme/one")]),
            generator).run("run_1", tiers=[3], limit=1)

    assert report.queries_executed == 1, "a failed query must be retried"
    assert report.queries_skipped == 0


def test_14_run_statistics_come_from_persisted_records(tmp_path, universe):
    from dependency_map.dedup import run_stats

    db_file = tmp_path / "stats.db"
    initialize_database(db_file)
    generator = QueryGenerator(universe, windows=("size:0..250",),
                               include_co_occurrence=False)

    with connect(db_file) as conn:
        storage.create_run(conn, "run_1")
        DiscoveryEngine(
            conn, ScriptedClient(_one_repo(), discovery_hits=[Hit("acme/one")]),
            generator).run("run_1", tiers=[3], limit=2)

    # A brand new connection: nothing in memory, everything from the database.
    with connect(db_file) as conn:
        stats = run_stats(conn, "run_1")

    assert stats.queries_executed == 2
    assert stats.unique_repositories == 1
    assert stats.new_candidates == 1


def test_14_the_production_database_path_is_never_a_test_fixture(db_path, tmp_path):
    """The replacement invariant for the retired existence check: tests must
    not write the production path, which is a different claim from the
    production database not existing."""
    from dependency_map.db import DEFAULT_DB_PATH

    assert db_path.resolve() != DEFAULT_DB_PATH.resolve()
    assert tmp_path in db_path.parents


def test_14_size_is_a_partition_and_never_a_ranking_signal():
    """The slice divides the search space. It says nothing about whether a
    repository is a good prospect, and must never leak into scoring.

    A large `requirements.txt` is not a better lead than a small one; it is
    only a different part of the result set. This asserts the separation at
    the module level so a future change that reads the slice back out as a
    signal fails here rather than quietly skewing the ranking.
    """
    import inspect

    from dependency_map import qualification, scoring

    # report.py is deliberately excluded: it *displays* the slice as coverage
    # provenance, which is how a reader checks which population a candidate
    # came from. Showing it is required; scoring on it is not allowed.
    for module in (scoring, qualification):
        source = inspect.getsource(module)
        for forbidden in ("search_window", "SIZE_BUCKETS", "size_windows"):
            assert forbidden not in source, (
                f"{module.__name__} references {forbidden}; the size slice is a "
                f"search-space partition, not a scoring or ranking input"
            )


# =============================================================================
# 15. Phase 13 quality corrections: sampling disclosure, Markdown escaping and
#     run-id safety. All three cover defects the first official run exposed.
# =============================================================================


# --- A. sampling disclosure -------------------------------------------------


def _seed_sampled_corpus(conn, weights_and_caps, *, discovered=40, qualified=12):
    """A corpus where far more was discovered than was ever evidenced.

    That gap is the whole point: the report has to say the difference was not
    examined, rather than leaving a reader to assume it was examined and
    dropped.
    """
    weights, caps = weights_and_caps
    storage.create_run(conn, "run_1")
    qid = {}
    for tier in (1, 2, 3):
        qid[tier] = storage.create_discovery_query(
            conn, run_id="run_1", discovery_source="github_code_search",
            query=f"q-tier{tier}", discovery_tier=tier,
            search_window=None if tier < 3 else "size:0..250",
            total_count=5000, returned_count=discovered)

    tier_of = {}
    for i in range(discovered):
        name = f"org/repo{i:03d}"
        cid = make_candidate_id(f"https://github.com/{name}")
        tier = 1 if i % 4 == 0 else (2 if i % 4 == 1 else 3)
        tier_of[cid] = tier
        storage.insert_candidate_if_new(
            conn, candidate_id=cid,
            repo_url=normalize_repo_url(f"https://github.com/{name}"),
            repo_owner="org", repo_name=f"repo{i:03d}", first_seen_run_id="run_1")
        storage.insert_discovery_evidence(conn, query_id=qid[tier], candidate_id=cid)

    # Only the first `qualified` candidates get evidence + qualification.
    sample = sorted(tier_of)[:qualified]
    for n, cid in enumerate(sample):
        storage.upsert_pipeline_evidence(
            conn, candidate_id=cid, code_usage_confirmed=True,
            template_directory_present=False, multiple_document_types_handled=False,
            pipeline_stage_count=1, infrastructure_service_present=False,
            pipeline_evidence_notes="")
        storage.upsert_business_evidence(
            conn, candidate_id=cid, readme_describes_product=True,
            readme_excerpt="For our customers.", website_exists=True,
            application_code_exists=True,
            document_functionality_in_production_code=True,
            stars=n, last_commit_date="2026-07-01", contributor_count=None,
            business_evidence_notes="")
        status = "reject" if n % 4 == 3 else ("keep" if n % 4 == 0 else "investigate")
        storage.upsert_qualification(
            conn, candidate_id=cid, qualification_status=status,
            qualification_reason="r",
            rejection_reason="tutorial_or_demo" if status == "reject" else None,
            confidence="medium")
        if status != "reject":
            ScoringEngine(conn, weights, caps).score_one(cid)
    return sample, tier_of


def test_15_report_states_discovery_universe_and_sample_separately(
    conn, weights_and_caps
):
    _seed_sampled_corpus(conn, weights_and_caps, discovered=40, qualified=12)
    data = gather_report_data(conn)
    md = render_markdown(data)

    assert data.total_candidates_ever == 40
    assert data.sample_size == 12
    assert "40" in md and "12" in md
    assert "Coverage and sampling" in md


def test_15_report_says_the_unexamined_remainder_was_not_examined(
    conn, weights_and_caps
):
    """The specific failure this guards: a reader inferring that everything
    discovered was inspected and the rest simply did not qualify."""
    _seed_sampled_corpus(conn, weights_and_caps, discovered=40, qualified=12)
    md = render_markdown(gather_report_data(conn)).lower()

    assert "no evidence was collected for them" in md
    assert "never qualified" in md
    assert "not examined" in md


def test_15_report_publishes_the_deterministic_sample_rule(conn, weights_and_caps):
    _seed_sampled_corpus(conn, weights_and_caps, discovered=40, qualified=12)
    md = render_markdown(gather_report_data(conn))

    assert "candidate_id" in md
    assert "ascending" in md.lower()
    assert "stratified" in md.lower()
    assert "strongest (lowest) tier" in md


def test_15_sample_tier_breakdown_matches_the_database(conn, weights_and_caps):
    sample, tier_of = _seed_sampled_corpus(
        conn, weights_and_caps, discovered=40, qualified=12)
    data = gather_report_data(conn)

    expected: dict[int, int] = {}
    for cid in sample:
        expected[tier_of[cid]] = expected.get(tier_of[cid], 0) + 1

    assert dict(data.sample_by_tier) == expected
    assert sum(data.sample_by_tier.values()) == data.sample_size


def test_15_report_never_claims_the_whole_universe_was_evidenced(
    conn, weights_and_caps
):
    _seed_sampled_corpus(conn, weights_and_caps, discovered=40, qualified=12)
    md = render_markdown(gather_report_data(conn))

    for claim in ("40 repositories were evidence", "40 repositories were inspected",
                  "all 40 repositories were reviewed", "40 repositories were reviewed"):
        assert claim not in md


def test_15_evidence_outside_the_sample_is_reported_separately(
    conn, weights_and_caps
):
    """Evidence can exist for a candidate that never entered the sample. That
    number is published rather than folded into either total."""
    sample, _ = _seed_sampled_corpus(conn, weights_and_caps, discovered=40, qualified=12)
    extra = sorted(
        r["candidate_id"] for r in conn.execute("SELECT candidate_id FROM candidates")
    )
    outsider = next(c for c in extra if c not in sample)
    storage.upsert_business_evidence(
        conn, candidate_id=outsider, readme_describes_product=False,
        readme_excerpt="", website_exists=False, application_code_exists=False,
        document_functionality_in_production_code=False, stars=0,
        last_commit_date=None, contributor_count=None, business_evidence_notes="")

    data = gather_report_data(conn)
    assert data.evidence_collected_count == 13
    assert data.sample_size == 12
    assert "outside the official sample: **1**" in render_markdown(data)


# --- B. Markdown control-character escaping ---------------------------------


@pytest.mark.parametrize("raw,expected", [
    ("plain text", "plain text"),
    ("a|b", "a\\|b"),
    ("a\nb", "a b"),
    ("a\rb", "a b"),
    ("a\r\nb", "a b"),
    ("Notice  \r\n\r\nKedo", "Notice   Kedo"),
    ("a\tb", "a b"),
    ("", ""),
])
def test_15_md_escape_handles_control_characters(raw, expected):
    from dependency_map.report import _md_escape

    assert _md_escape(raw) == expected


def test_15_md_escape_never_emits_a_line_breaking_character():
    from dependency_map.report import _md_escape

    for raw in ("a\rb", "a\nb", "a\r\n\r\nb", "a b", "ab", "a\x0bb"):
        out = _md_escape(raw)
        assert not any(ch in out for ch in "\r\n\v\f  "), repr(out)


def test_15_a_carriage_return_cannot_split_a_ranked_table_row(
    conn, run_id, weights_and_caps
):
    """The exact run-1 defect: one row rendered with four columns instead of
    ten because a company name carried a bare carriage return."""
    import re as _re

    weights, caps = weights_and_caps
    cid = make_candidate_id("https://github.com/acme/widget")
    storage.insert_candidate_if_new(
        conn, candidate_id=cid, repo_url="https://github.com/acme/widget",
        repo_owner="acme", repo_name="widget",
        company_name="Notice  \r\n\r\nKedo", product_name="Kedo\rExecutor",
        first_seen_run_id=run_id)
    storage.upsert_qualification(
        conn, candidate_id=cid, qualification_status="keep",
        qualification_reason="r", confidence="high")
    ScoringEngine(conn, weights, caps).score_one(cid)

    md = render_markdown(gather_report_data(conn))
    rows = [l for l in md.split("\n") if _re.match(r"^\| \d+ \|", l)]

    assert rows, "expected at least one ranked row"
    for row in rows:
        assert len(row.split("|")) == 10, f"row split into {len(row.split('|'))}: {row!r}"
    assert "\r" not in md


def test_15_csv_still_carries_the_raw_value_unescaped(conn, run_id, weights_and_caps):
    """The Markdown fix must not reach into the CSV, which quotes properly and
    should keep the value as stored."""
    import csv as _csv
    import io as _io

    weights, caps = weights_and_caps
    cid = make_candidate_id("https://github.com/acme/widget")
    storage.insert_candidate_if_new(
        conn, candidate_id=cid, repo_url="https://github.com/acme/widget",
        repo_owner="acme", repo_name="widget",
        company_name="Notice  \r\n\r\nKedo", first_seen_run_id=run_id)
    storage.upsert_qualification(
        conn, candidate_id=cid, qualification_status="keep",
        qualification_reason="r", confidence="high")
    ScoringEngine(conn, weights, caps).score_one(cid)

    text = render_csv(gather_report_data(conn))
    rows = list(_csv.DictReader(_io.StringIO(text, newline="")))

    assert len(rows) == 1
    assert rows[0]["company_name"] == "Notice  \r\n\r\nKedo"


# --- C. run-id safety -------------------------------------------------------


def _runs_in(db_path):
    with connect(db_path) as conn:
        return [r["run_id"] for r in conn.execute("SELECT run_id FROM runs")]


@pytest.mark.parametrize("stage", ["evidence", "qualification", "scoring"])
def test_15_continuing_stages_require_an_explicit_run_id(cli_env, stage):
    """Without --run-id these silently allocated a fresh run, which is how a
    stray empty run_2 appeared during the first official run."""
    from dependency_map.cli import cli
    config_dir, db_path, _ = cli_env

    before = _runs_in(db_path)
    result = CliRunner().invoke(
        cli, ["--config-dir", str(config_dir), "run", "--stage", stage])

    assert result.exit_code != 0
    assert "--run-id is required" in result.output
    assert _runs_in(db_path) == before, "a run was created despite the failure"


def test_15_report_requires_an_explicit_run_id(cli_env):
    from dependency_map.cli import cli
    config_dir, db_path, _ = cli_env

    before = _runs_in(db_path)
    result = CliRunner().invoke(cli, ["--config-dir", str(config_dir), "report"])

    assert result.exit_code != 0
    assert "--run-id is required" in result.output
    assert _runs_in(db_path) == before


def test_15_report_rejects_a_run_id_that_does_not_exist(cli_env):
    from dependency_map.cli import cli
    config_dir, db_path, _ = cli_env

    result = CliRunner().invoke(
        cli, ["--config-dir", str(config_dir), "report", "--run-id", "run_nope"])

    assert result.exit_code != 0
    assert "does not exist" in result.output


def test_15_supplying_a_run_id_works(cli_env, monkeypatch):
    from dependency_map.cli import cli
    config_dir, db_path, out_dir = cli_env
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)

    with connect(db_path) as conn:
        storage.create_run(conn, "run_1")
        cid = make_candidate_id("https://github.com/acme/widget")
        storage.insert_candidate_if_new(
            conn, candidate_id=cid, repo_url="https://github.com/acme/widget",
            repo_owner="acme", repo_name="widget", first_seen_run_id="run_1")
        storage.upsert_qualification(
            conn, candidate_id=cid, qualification_status="keep",
            qualification_reason="r", confidence="high")

    scoring = CliRunner().invoke(
        cli, ["--config-dir", str(config_dir), "run",
              "--run-id", "run_1", "--stage", "scoring"])
    assert scoring.exit_code == 0, scoring.output

    report = CliRunner().invoke(
        cli, ["--config-dir", str(config_dir), "report", "--run-id", "run_1"])
    assert report.exit_code == 0, report.output
    assert (out_dir / "out.csv").exists()
    assert _runs_in(db_path) == ["run_1"], "no extra run was invented"


def test_15_discovery_may_still_create_a_run_without_a_run_id(cli_env, monkeypatch):
    """Discovery semantics are deliberately unchanged: it is the one stage
    allowed to bring a run into existence."""
    from dependency_map.cli import cli
    config_dir, db_path, _ = cli_env

    routes = {
        "/search/code": json_response({
            "total_count": 1,
            "items": [{"path": "requirements.txt", "sha": "a",
                      "html_url": "https://github.com/acme/widget/blob/main/requirements.txt",
                      "repository": {"full_name": "acme/widget",
                                    "html_url": "https://github.com/acme/widget"}}],
        }),
    }
    monkeypatch.setattr("dependency_map.reliability.RequestsTransport",
                        build_fake_transport(routes))

    result = CliRunner().invoke(
        cli, ["--config-dir", str(config_dir), "run", "--stage", "discovery",
              "--tier", "1", "--query-limit", "1"])

    assert result.exit_code == 0, result.output
    assert _runs_in(db_path) == ["run_1"]
