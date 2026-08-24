"""The report generator: CSV, Markdown, and the coverage-honesty rules.

Every test seeds a temporary database directly through storage functions.
Nothing here touches the network, and nothing here re-scores or re-qualifies:
the fixtures write scores and qualification decisions exactly as a real run
would have persisted them.
"""

from __future__ import annotations

import csv
import io

import pytest

from dependency_map import storage
from dependency_map.dedup import make_candidate_id, normalize_repo_url
from dependency_map.report import (
    ReportError,
    describe_query_coverage,
    gather_report_data,
    render_csv,
    render_markdown,
    write_report,
)

FAKE_TOKEN = "ghp_fake000000000000000000000000000000"
FAKE_KEY = "libio_fake_key_00000"


# --- fixture builder ---------------------------------------------------------


def seed_candidate(
    conn, run_id, name="acme/widget", *,
    status="keep", rejection_reason=None, qual_confidence="high",
    final_score=80, confidence_band="high", raw=4.0,
    scores=None, unknown_dimensions=(), gate_cap=None,
    company="Acme Inc.", product="Acme Widget", website="https://acme.example.com",
    industry="real_estate",
    library="docxtpl (python-docx-template)", tier=2, search_window=None,
    query="q", total_count=100, returned_count=5, capped=False, rank=1,
    dependency=True, evidence_trail=True,
):
    """Write one candidate through discovery, qualification and scoring, the
    way a real run would, so the report is exercised against a realistic
    shape rather than a hand-built row."""
    url = f"https://github.com/{name}"
    cid = make_candidate_id(url)
    owner, _, repo = name.partition("/")

    query_id = storage.create_discovery_query(
        conn, run_id=run_id, discovery_source="github_code_search",
        query=query, library_name=library, discovery_tier=tier,
        search_window=search_window, total_count=total_count,
        returned_count=returned_count, capped=capped,
    )
    storage.insert_candidate_if_new(
        conn, candidate_id=cid, repo_url=normalize_repo_url(url),
        repo_owner=owner, repo_name=repo, first_seen_run_id=run_id,
        company_name=company, company_name_source="readme" if company else None,
        product_name=product, website_url=website, industry_category=industry,
    )
    storage.insert_discovery_evidence(
        conn, query_id=query_id, candidate_id=cid, discovery_result_rank=rank)

    if dependency:
        storage.insert_dependency_found(
            conn, candidate_id=cid, library_name=library, library_category="docx",
            direction="generation", detection_method="code_import",
            evidence_url=f"https://github.com/{name}/blob/main/app.py")

    if evidence_trail:
        storage.insert_evidence_trail(
            conn, candidate_id=cid, evidence_url=f"https://github.com/{name}",
            evidence_type="readme_excerpt", source="readme",
            evidence_excerpt="A product for our customers.")

    storage.upsert_qualification(
        conn, candidate_id=cid, qualification_status=status,
        qualification_reason="category_count=1, code_usage_confirmed=true",
        rejection_reason=rejection_reason, confidence=qual_confidence)

    if status in ("keep", "investigate"):
        defaults = {d: 3 for d in ["document_volume", "document_complexity",
                                   "business_criticality", "pipeline_complexity",
                                   "maintenance_burden", "build_vs_buy_signal",
                                   "commercial_leverage"]}
        defaults.update(scores or {})
        storage.upsert_score(
            conn, candidate_id=cid, **defaults, raw_weighted_score=raw,
            final_score=final_score, confidence_band=confidence_band,
            unknown_dimensions=list(unknown_dimensions), gate_cap_applied=gate_cap)

    return cid


# --- 1-6: qualification / scoring shapes -------------------------------------


def test_1_keep_candidate_appears_ranked(conn, run_id):
    cid = seed_candidate(conn, run_id, "org/keeper", status="keep", final_score=85)
    data = gather_report_data(conn)

    assert len(data.ranked) == 1
    assert data.ranked[0].candidate_id == cid
    assert data.ranked[0].row["qualification_status"] == "keep"


def test_2_investigate_candidate_appears_ranked(conn, run_id):
    seed_candidate(conn, run_id, "org/maybe", status="investigate", final_score=40)
    data = gather_report_data(conn)

    assert len(data.ranked) == 1
    assert data.ranked[0].row["qualification_status"] == "investigate"


def test_3_reject_candidate_never_appears_ranked(conn, run_id):
    seed_candidate(conn, run_id, "someone/python-docx", status="reject",
                   rejection_reason="fork_of_library")
    data = gather_report_data(conn)

    assert data.ranked == ()
    assert data.reject_count == 1


def test_4_candidate_with_unknown_dimensions(conn, run_id):
    cid = seed_candidate(conn, run_id, "org/thin", status="investigate",
                         final_score=20, unknown_dimensions=["maintenance_burden",
                                                              "document_volume"])
    data = gather_report_data(conn)
    candidate = data.ranked[0]

    assert candidate.evidenced_count == 5
    assert candidate.evidence_coverage_fraction == "5/7"
    assert set(candidate.unknown_dimensions) == {"maintenance_burden", "document_volume"}


def test_5_candidate_with_a_gate_cap(conn, run_id):
    cid = seed_candidate(conn, run_id, "org/capped-candidate", status="keep",
                         final_score=20, gate_cap=20)
    data = gather_report_data(conn)

    assert data.ranked[0].row["gate_cap_applied"] == 20


def test_6_tied_scores_break_on_confidence_then_candidate_id(conn, run_id):
    a = seed_candidate(conn, run_id, "org/tie-a", status="keep", final_score=50,
                       confidence_band="medium")
    b = seed_candidate(conn, run_id, "org/tie-b", status="keep", final_score=50,
                       confidence_band="high")
    c = seed_candidate(conn, run_id, "org/tie-c", status="keep", final_score=50,
                       confidence_band="high")
    data = gather_report_data(conn)
    ids = [cand.candidate_id for cand in data.ranked]

    # high-confidence ties (b, c) sort before the medium one (a); within the
    # high group, candidate_id breaks the tie.
    assert ids.index(b) < ids.index(a)
    assert ids.index(c) < ids.index(a)
    assert ids[:2] == sorted([b, c])


# --- 7-9: query coverage -----------------------------------------------------


def test_7_zero_result_query_is_recorded(conn, run_id):
    storage.create_discovery_query(
        conn, run_id=run_id, discovery_source="github_code_search",
        query='"reportlab" filename:requirements.txt language:python',
        library_name="ReportLab", discovery_tier=3,
        total_count=0, returned_count=0, capped=False)
    data = gather_report_data(conn)

    assert len(data.zero_result_queries) == 1
    assert data.zero_result_queries[0]["query"].startswith('"reportlab"')


def test_8_capped_query_coverage_note_is_honest():
    note = describe_query_coverage(75648, 10, True)

    assert "10" in note
    assert "75,648" in note
    assert "partial sample" in note
    assert "not an exhaustive result" in note
    # must never claim the total was inspected
    assert "75,648 repositories were inspected" not in note
    assert "75,648 inspected" not in note


def test_9_uncapped_query_coverage_note_states_the_ceiling():
    note = describe_query_coverage(662, 10, False)

    assert "662" in note
    assert "pagination ceiling" in note
    assert "partial sample" not in note


def test_zero_result_note_is_distinct():
    assert describe_query_coverage(0, 0, False) == \
        "No matches. The query returned zero results."


def test_failed_query_note_is_distinct():
    assert describe_query_coverage(None, 0, None) == \
        "Query failed before a total could be recorded."


# --- 10: duplicate repository across queries ---------------------------------


def test_10_duplicate_repository_across_queries_is_one_candidate(conn, run_id):
    url = "https://github.com/org/shared"
    cid = make_candidate_id(url)
    storage.insert_candidate_if_new(
        conn, candidate_id=cid, repo_url=normalize_repo_url(url),
        repo_owner="org", repo_name="shared", first_seen_run_id=run_id)

    for query in ("q1", "q2"):
        qid = storage.create_discovery_query(
            conn, run_id=run_id, discovery_source="github_code_search",
            query=query, library_name="python-docx", discovery_tier=3,
            total_count=50, returned_count=5, capped=False)
        storage.insert_discovery_evidence(conn, query_id=qid, candidate_id=cid)

    storage.upsert_qualification(
        conn, candidate_id=cid, qualification_status="keep",
        qualification_reason="r", confidence="high")
    storage.upsert_score(
        conn, candidate_id=cid,
        **{d: 3 for d in ["document_volume", "document_complexity",
                          "business_criticality", "pipeline_complexity",
                          "maintenance_burden", "build_vs_buy_signal",
                          "commercial_leverage"]},
        raw_weighted_score=3.0, final_score=60, confidence_band="high")

    data = gather_report_data(conn)

    assert len(data.ranked) == 1
    assert len(data.ranked[0].discovery_hits) == 2, \
        "both queries that found it should appear in provenance"
    assert storage.count_candidates(conn) == 1


# --- 11: multiple runs --------------------------------------------------------


def test_11_multiple_runs_are_all_reported(conn):
    storage.create_run(conn, "run_1", started_at="2026-01-01T00:00:00Z",
                       notes="run #1: baseline")
    storage.create_run(conn, "run_2", started_at="2026-02-01T00:00:00Z",
                       notes="run #2: rotated window")
    seed_candidate(conn, "run_1", "org/from-run-1", status="keep", final_score=70)
    seed_candidate(conn, "run_2", "org/from-run-2", status="keep", final_score=60)

    data = gather_report_data(conn)

    assert len(data.runs) == 2
    assert set(data.run_stats) == {"run_1", "run_2"}
    assert len(data.ranked) == 2


# --- 12: empty ranking result -------------------------------------------------


def test_12_empty_ranking_result(conn, run_id):
    seed_candidate(conn, run_id, "someone/python-docx", status="reject",
                   rejection_reason="fork_of_library")
    data = gather_report_data(conn)

    assert data.ranked == ()
    csv_text = render_csv(data)
    assert csv_text.strip().count("\n") == 0, "header only, no data rows"

    md_text = render_markdown(data)
    assert "No candidates currently qualify" in md_text


def test_12_empty_database_produces_valid_output(conn):
    data = gather_report_data(conn)

    assert data.ranked == ()
    assert render_csv(data)  # header still present
    assert "# Dependency Map" in render_markdown(data)


# --- 13: CSV output -----------------------------------------------------------


def test_13_csv_has_the_expected_columns(conn, run_id):
    seed_candidate(conn, run_id, "org/csvcheck", status="keep", final_score=77)
    csv_text = render_csv(gather_report_data(conn))
    reader = csv.DictReader(io.StringIO(csv_text))

    expected = {
        "rank", "candidate_id", "repo_url", "repo_owner", "repo_name",
        "company_name", "product_name", "website_url", "industry_category",
        "qualification_status", "qualification_confidence", "qualification_reason",
        "document_volume", "document_complexity", "business_criticality",
        "pipeline_complexity", "maintenance_burden", "build_vs_buy_signal",
        "commercial_leverage", "raw_weighted_score", "final_score",
        "confidence_band", "evidence_coverage", "unknown_dimensions",
        "gate_cap_applied",
    }
    assert expected.issubset(set(reader.fieldnames))


def test_13_csv_row_values_match_stored_data(conn, run_id):
    seed_candidate(conn, run_id, "org/values", status="keep", final_score=91,
                   company="ValueCo", industry="legal_contracts")
    csv_text = render_csv(gather_report_data(conn))
    row = next(csv.DictReader(io.StringIO(csv_text)))

    assert row["final_score"] == "91"
    assert row["company_name"] == "ValueCo"
    assert row["industry_category"] == "legal_contracts"
    assert row["qualification_status"] == "keep"


def test_13_csv_excludes_rejected_candidates(conn, run_id):
    seed_candidate(conn, run_id, "someone/python-docx", status="reject",
                   rejection_reason="fork_of_library")
    seed_candidate(conn, run_id, "org/kept", status="keep", final_score=70)
    csv_text = render_csv(gather_report_data(conn))
    rows = list(csv.DictReader(io.StringIO(csv_text)))

    assert len(rows) == 1
    assert rows[0]["repo_name"] == "kept"


def test_13_csv_cells_are_not_unreasonably_large(conn, run_id):
    seed_candidate(conn, run_id, "org/compact", status="keep", final_score=70)
    csv_text = render_csv(gather_report_data(conn))
    row = next(csv.DictReader(io.StringIO(csv_text)))

    for key, value in row.items():
        assert len(value) < 2000, f"{key} cell is unreasonably large"


# --- 14: Markdown output -------------------------------------------------------


def test_14_markdown_has_required_top_level_sections(conn, run_id):
    seed_candidate(conn, run_id, "org/sections", status="keep", final_score=70)
    md = render_markdown(gather_report_data(conn))

    for heading in ["# Dependency Map", "## Executive summary", "## Ranked table",
                    "## Candidate details", "## Query method",
                    "## Zero-result queries", "## Run information",
                    "## Reproducibility"]:
        assert heading in md, heading


def test_14_markdown_shows_score_as_a_score_not_a_probability(conn, run_id):
    """The report may say the word "probability" once, to explicitly disclaim
    it (requirement 8's own wording: "a score, not a probability"). What must
    never appear is the score reframed as a percentage-likelihood claim."""
    seed_candidate(conn, run_id, "org/scorewording", status="keep", final_score=17)
    md = render_markdown(gather_report_data(conn))

    assert "17/100" in md
    assert "17%" not in md
    assert "likelihood" not in md.lower()
    assert "a score, not a probability" in md.lower()


def test_14_markdown_explicitly_labels_unknown_dimensions(conn, run_id):
    seed_candidate(conn, run_id, "org/unknowns", status="investigate",
                   final_score=15, unknown_dimensions=["maintenance_burden"])
    md = render_markdown(gather_report_data(conn))

    assert "Maintenance burden: Unknown" in md
    assert "not available" not in md.lower()


def test_14_markdown_shows_evidence_coverage_fraction(conn, run_id):
    seed_candidate(conn, run_id, "org/coverage", status="investigate",
                   final_score=30, unknown_dimensions=["maintenance_burden",
                                                        "commercial_leverage"])
    md = render_markdown(gather_report_data(conn))

    assert "Evidence coverage: 5/7 dimensions" in md


def test_14_markdown_shows_gate_cap_when_applied(conn, run_id):
    seed_candidate(conn, run_id, "org/gated", status="keep", final_score=20,
                   gate_cap=20)
    md = render_markdown(gather_report_data(conn))

    assert "Gate cap applied: **20**" in md


def test_14_markdown_omits_gate_cap_line_when_not_applied(conn, run_id):
    seed_candidate(conn, run_id, "org/ungated", status="keep", final_score=70,
                   gate_cap=None)
    md = render_markdown(gather_report_data(conn))

    assert "Gate cap applied" not in md


# --- CSV / Markdown consistency (section 13 of the brief) --------------------


def test_every_markdown_candidate_exists_in_the_csv(conn, run_id):
    seed_candidate(conn, run_id, "org/a", status="keep", final_score=90)
    seed_candidate(conn, run_id, "org/b", status="investigate", final_score=40)
    data = gather_report_data(conn)
    csv_rows = list(csv.DictReader(io.StringIO(render_csv(data))))

    md_ids = {c.candidate_id for c in data.ranked}
    csv_ids = {row["candidate_id"] for row in csv_rows}
    assert md_ids == csv_ids


def test_rank_and_order_are_consistent_between_outputs(conn, run_id):
    seed_candidate(conn, run_id, "org/first", status="keep", final_score=95)
    seed_candidate(conn, run_id, "org/second", status="keep", final_score=60)
    data = gather_report_data(conn)
    csv_rows = list(csv.DictReader(io.StringIO(render_csv(data))))

    for candidate, row in zip(data.ranked, csv_rows):
        assert str(candidate.rank) == row["rank"]
        assert candidate.candidate_id == row["candidate_id"]


def test_scores_match_between_outputs(conn, run_id):
    seed_candidate(conn, run_id, "org/matching", status="keep", final_score=83,
                   raw=3.5)
    data = gather_report_data(conn)
    md = render_markdown(data)
    row = next(csv.DictReader(io.StringIO(render_csv(data))))

    assert row["final_score"] == "83"
    assert "83/100" in md


def test_qualification_statuses_match_between_outputs(conn, run_id):
    seed_candidate(conn, run_id, "org/qualmatch", status="investigate",
                   final_score=33)
    data = gather_report_data(conn)
    row = next(csv.DictReader(io.StringIO(render_csv(data))))
    md = render_markdown(data)

    assert row["qualification_status"] == "investigate"
    assert "investigate" in md


def test_reject_appears_in_neither_output(conn, run_id):
    seed_candidate(conn, run_id, "someone/python-docx", status="reject",
                   rejection_reason="fork_of_library")
    data = gather_report_data(conn)
    csv_text = render_csv(data)
    md = render_markdown(data)

    assert "python-docx" not in csv_text.split("\n", 1)[1]  # past header
    assert "someone/python-docx" not in md


# --- 15: no secrets in outputs ------------------------------------------------


def test_15_no_secrets_in_csv_or_markdown(conn, run_id, monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", FAKE_TOKEN)
    monkeypatch.setenv("LIBRARIES_IO_API_KEY", FAKE_KEY)
    seed_candidate(conn, run_id, "org/safe", status="keep", final_score=70)
    data = gather_report_data(conn)

    csv_text = render_csv(data)
    md_text = render_markdown(data)

    for secret in (FAKE_TOKEN, FAKE_KEY, "Authorization", "Bearer "):
        assert secret not in csv_text
        assert secret not in md_text


def test_15_report_module_never_reads_environment_secrets():
    from pathlib import Path

    source = Path("src/dependency_map/report.py").read_text(encoding="utf-8")
    for forbidden in ["os.environ", "GITHUB_TOKEN", "LIBRARIES_IO_API_KEY",
                      "getenv", "GitHubClient", "LibrariesIOClient"]:
        assert forbidden not in source


def test_15_report_makes_no_network_calls():
    from pathlib import Path

    source = Path("src/dependency_map/report.py").read_text(encoding="utf-8")
    for forbidden in ["import requests", "urllib.request", "http.client",
                      "ReliableRequester", "RequestsTransport"]:
        assert forbidden not in source


def test_15_report_does_not_write_to_the_database(conn, run_id):
    seed_candidate(conn, run_id, "org/readonly", status="keep", final_score=70)
    before = {
        table: [dict(r) for r in conn.execute(f"SELECT * FROM {table}")]
        for table in ("candidates", "scores", "qualification", "discovery_queries")
    }
    gather_report_data(conn)
    render_csv(gather_report_data(conn))
    render_markdown(gather_report_data(conn))
    after = {
        table: [dict(r) for r in conn.execute(f"SELECT * FROM {table}")]
        for table in ("candidates", "scores", "qualification", "discovery_queries")
    }
    assert before == after


# --- 16: deterministic ordering ------------------------------------------------


def test_16_ordering_is_deterministic_across_repeated_generation(conn, run_id):
    seed_candidate(conn, run_id, "org/x", status="keep", final_score=80)
    seed_candidate(conn, run_id, "org/y", status="investigate", final_score=40)
    seed_candidate(conn, run_id, "org/z", status="keep", final_score=60)

    first = [c.candidate_id for c in gather_report_data(conn).ranked]
    second = [c.candidate_id for c in gather_report_data(conn).ranked]

    assert first == second
    assert first == sorted(first, key=lambda cid: -[
        c for c in gather_report_data(conn).ranked if c.candidate_id == cid
    ][0].row["final_score"])


def test_16_final_score_descending(conn, run_id):
    seed_candidate(conn, run_id, "org/low", status="keep", final_score=10)
    seed_candidate(conn, run_id, "org/high", status="keep", final_score=90)
    seed_candidate(conn, run_id, "org/mid", status="keep", final_score=50)

    scores = [c.row["final_score"] for c in gather_report_data(conn).ranked]
    assert scores == sorted(scores, reverse=True)


# --- write_report / file output -----------------------------------------------


def test_write_report_creates_both_files(conn, run_id, tmp_path):
    seed_candidate(conn, run_id, "org/filewrite", status="keep", final_score=70)
    csv_path = tmp_path / "out" / "ranked-candidates.csv"
    md_path = tmp_path / "out" / "dependency-map-report.md"

    summary = write_report(conn, csv_path, md_path)

    assert csv_path.exists()
    assert md_path.exists()
    assert summary.ranked_count == 1
    assert summary.keep_count == 1


def test_write_report_creates_parent_directories(conn, run_id, tmp_path):
    seed_candidate(conn, run_id, "org/nested", status="keep", final_score=70)
    csv_path = tmp_path / "a" / "b" / "c" / "ranked.csv"
    md_path = tmp_path / "d" / "e" / "report.md"

    write_report(conn, csv_path, md_path)

    assert csv_path.exists() and md_path.exists()


def test_write_report_summary_matches_the_data(conn, run_id):
    seed_candidate(conn, run_id, "org/summarised", status="keep", final_score=70)
    seed_candidate(conn, run_id, "someone/python-docx", status="reject",
                   rejection_reason="fork_of_library")

    import tempfile
    from pathlib import Path
    tmp = Path(tempfile.mkdtemp())
    summary = write_report(conn, tmp / "c.csv", tmp / "r.md")

    assert summary.ranked_count == 1
    assert summary.reject_count == 1


# --- output path / CLI wiring --------------------------------------------------


def test_report_command_is_registered():
    from dependency_map.cli import cli

    assert "report" in cli.commands


def test_report_command_requires_no_github_token(tmp_path, monkeypatch):
    """report reads only the database, so it must work with no token at all."""
    from click.testing import CliRunner
    from dependency_map.cli import cli
    from dependency_map.db import connect, initialize_database

    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    config_dir = tmp_path / "config"
    config_dir.mkdir()
    (config_dir / "config.yaml").write_text(f"""
paths:
  database: {(tmp_path / 't.db').as_posix()}
  library_universe: data/library-universe.yaml
  output_csv: {(tmp_path / 'out.csv').as_posix()}
  output_markdown: {(tmp_path / 'out.md').as_posix()}
cache:
  ttl_days: 7
pacing:
  github_code_search_min_interval_seconds: 6.5
  github_search_min_interval_seconds: 2.0
  github_rest_min_interval_seconds: 0.75
  libraries_io_min_interval_seconds: 1.0
retry:
  max_attempts: 3
  backoff_base_seconds: 2.0
  backoff_jitter_seconds: 0.5
  backoff_max_seconds: 60.0
""", encoding="utf-8")
    (config_dir / "weights.yaml").write_text("""
dimension_weights:
  document_volume: 0.15
  document_complexity: 0.15
  business_criticality: 0.20
  pipeline_complexity: 0.20
  maintenance_burden: 0.15
  build_vs_buy_signal: 0.10
  commercial_leverage: 0.05
gate_caps:
  code_usage_unconfirmed: 20
  document_code_outside_production: 25
  single_category_no_infrastructure: 40
""", encoding="utf-8")
    initialize_database(tmp_path / "t.db")
    # --run-id is required and validated, so the run has to exist first.
    with connect(tmp_path / "t.db") as conn:
        storage.create_run(conn, "run_1")

    result = CliRunner().invoke(
        cli, ["--config-dir", str(config_dir), "report", "--run-id", "run_1"],
        env={"GITHUB_TOKEN": ""})

    assert result.exit_code == 0, result.output
    assert (tmp_path / "out.csv").exists()
    assert (tmp_path / "out.md").exists()


def test_report_command_exits_nonzero_on_missing_database(tmp_path):
    from click.testing import CliRunner
    from dependency_map.cli import cli

    config_dir = tmp_path / "config"
    config_dir.mkdir()
    (config_dir / "config.yaml").write_text(f"""
paths:
  database: {(tmp_path / 'does-not-exist.db').as_posix()}
  library_universe: data/library-universe.yaml
  output_csv: {(tmp_path / 'out.csv').as_posix()}
  output_markdown: {(tmp_path / 'out.md').as_posix()}
cache:
  ttl_days: 7
pacing:
  github_code_search_min_interval_seconds: 6.5
  github_search_min_interval_seconds: 2.0
  github_rest_min_interval_seconds: 0.75
  libraries_io_min_interval_seconds: 1.0
retry:
  max_attempts: 3
  backoff_base_seconds: 2.0
  backoff_jitter_seconds: 0.5
  backoff_max_seconds: 60.0
""", encoding="utf-8")
    (config_dir / "weights.yaml").write_text("""
dimension_weights:
  document_volume: 0.15
  document_complexity: 0.15
  business_criticality: 0.20
  pipeline_complexity: 0.20
  maintenance_burden: 0.15
  build_vs_buy_signal: 0.10
  commercial_leverage: 0.05
gate_caps:
  code_usage_unconfirmed: 20
  document_code_outside_production: 25
  single_category_no_infrastructure: 40
""", encoding="utf-8")

    result = CliRunner().invoke(cli, ["--config-dir", str(config_dir), "report"])

    assert result.exit_code != 0


# --- discovery provenance / query method rendering ----------------------------


def test_query_method_section_uses_real_recorded_queries(conn, run_id):
    seed_candidate(conn, run_id, "org/provenance", status="keep", final_score=70,
                   query='"gotenberg/gotenberg" filename:docker-compose.yml',
                   tier=1, total_count=662, returned_count=10, capped=False)
    md = render_markdown(gather_report_data(conn))

    assert "gotenberg/gotenberg" in md


def test_query_method_section_handles_no_queries_honestly(conn):
    md = render_markdown(gather_report_data(conn))

    assert "No discovery queries have been recorded yet" in md


def test_discovery_provenance_shows_capped_status_per_candidate(conn, run_id):
    cid = seed_candidate(conn, run_id, "org/cappedprov", status="keep",
                         final_score=50, total_count=75648, returned_count=10,
                         capped=True)
    md = render_markdown(gather_report_data(conn))

    assert "75,648" in md
    assert "partial sample" in md


def test_run_information_shows_rotation_and_new_vs_seen(conn, run_id):
    seed_candidate(conn, run_id, "org/runinfo", status="keep", final_score=70)
    md = render_markdown(gather_report_data(conn))

    assert "Rotation:" in md
    assert "New candidates:" in md
    assert "Previously seen" in md


def test_reproducibility_section_has_no_secret_and_a_timestamp(conn, run_id,
                                                                monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", FAKE_TOKEN)
    seed_candidate(conn, run_id, "org/repro", status="keep", final_score=70)
    md = render_markdown(gather_report_data(conn))

    assert "## Reproducibility" in md
    assert "Generated:" in md
    assert "schema version" in md.lower()
    assert FAKE_TOKEN not in md
