"""Phase 15: reports scoped to one run, with cumulative totals labelled.

A report that says "run_2" must describe run 2. Before this, every headline
number was database-wide, so a second run's report credited it with everything
the first run had found.

Network-free: every test uses a temporary database and seeded rows.
"""

from __future__ import annotations

import csv
import io
from pathlib import Path

import pytest
import yaml

from dependency_map import storage
from dependency_map.dedup import make_candidate_id, normalize_repo_url
from dependency_map.report import (
    gather_report_data,
    render_csv,
    render_markdown,
    write_report,
)
from dependency_map.scoring import ScoringEngine

WEIGHTS = Path("config/weights.yaml")
DIMS = ("document_volume", "document_complexity", "business_criticality",
        "pipeline_complexity", "maintenance_burden", "build_vs_buy_signal",
        "commercial_leverage")


@pytest.fixture(scope="module")
def weights_and_caps():
    data = yaml.safe_load(WEIGHTS.read_text(encoding="utf-8"))
    return data["dimension_weights"], data["gate_caps"]


def _candidate(conn, run_id, name, *, first_seen, tier, status, score,
               query_id):
    """Seed one candidate surfaced by `run_id`, first seen by `first_seen`."""
    url = f"https://github.com/{name}"
    cid = make_candidate_id(url)
    owner, repo = name.split("/")
    storage.insert_candidate_if_new(
        conn, candidate_id=cid, repo_url=normalize_repo_url(url),
        repo_owner=owner, repo_name=repo, first_seen_run_id=first_seen)
    storage.insert_discovery_evidence(conn, query_id=query_id, candidate_id=cid)
    storage.upsert_qualification(
        conn, candidate_id=cid, qualification_status=status,
        qualification_reason="r",
        rejection_reason="tutorial_or_demo" if status == "reject" else None,
        confidence="medium")
    if status != "reject":
        # Baseline mirrors the real state before enrichment: maintenance
        # burden scores 0 because nothing inspected it, not because it is thin.
        storage.upsert_score(
            conn, candidate_id=cid, **{d: 1 for d in DIMS},
            raw_weighted_score=1.0, final_score=score, confidence_band="medium",
            unknown_dimensions=["maintenance_burden"])
    return cid


@pytest.fixture
def two_runs(conn):
    """Two runs with distinct queries, a shared candidate, and distinct results.

    run_1: 3 candidates (2 scorable, 1 reject)
    run_2: 3 candidates - one carried over from run 1, two genuinely new
    """
    storage.create_run(conn, "run_1", started_at="2026-01-01T00:00:00Z")
    storage.create_run(conn, "run_2", started_at="2026-02-01T00:00:00Z")
    q1 = storage.create_discovery_query(
        conn, run_id="run_1", discovery_source="github_code_search",
        query="q-one", discovery_tier=3, search_window="size:0..250",
        total_count=5000, returned_count=3)
    q2 = storage.create_discovery_query(
        conn, run_id="run_2", discovery_source="github_code_search",
        query="q-two", discovery_tier=3, search_window="size:2001..4000",
        total_count=900, returned_count=3)

    shared = _candidate(conn, "run_1", "org/shared", first_seen="run_1", tier=3,
                        status="keep", score=40, query_id=q1)
    _candidate(conn, "run_1", "org/only1", first_seen="run_1", tier=3,
               status="investigate", score=30, query_id=q1)
    _candidate(conn, "run_1", "org/rej1", first_seen="run_1", tier=3,
               status="reject", score=0, query_id=q1)
    # run 2 sees the shared candidate again, plus two of its own.
    storage.insert_discovery_evidence(conn, query_id=q2, candidate_id=shared)
    _candidate(conn, "run_2", "org/new1", first_seen="run_2", tier=3,
               status="keep", score=20, query_id=q2)
    _candidate(conn, "run_2", "org/new2", first_seen="run_2", tier=3,
               status="reject", score=0, query_id=q2)
    return conn


# --- scoping ----------------------------------------------------------------


def test_run_scoped_ranking_excludes_the_other_runs_candidates(two_runs):
    r1 = gather_report_data(two_runs, "run_1")
    r2 = gather_report_data(two_runs, "run_2")

    names1 = {c.repo_full_name for c in r1.ranked}
    names2 = {c.repo_full_name for c in r2.ranked}

    assert "org/only1" in names1 and "org/only1" not in names2
    assert "org/new1" in names2 and "org/new1" not in names1
    # The shared candidate belongs to both: run 2 genuinely surfaced it again.
    assert "org/shared" in names1 and "org/shared" in names2


def test_run_scoped_universe_counts_only_that_runs_candidates(two_runs):
    r2 = gather_report_data(two_runs, "run_2")

    assert r2.total_candidates_ever == 3          # shared + new1 + new2
    assert r2.run_counts["surfaced"] == 3
    assert r2.run_counts["new"] == 2
    assert r2.run_counts["previously_seen"] == 1


def test_run_scoped_qualification_counts_are_per_run(two_runs):
    r1 = gather_report_data(two_runs, "run_1")
    r2 = gather_report_data(two_runs, "run_2")

    assert (r1.keep_count, r1.investigate_count, r1.reject_count) == (1, 1, 1)
    assert (r2.keep_count, r2.investigate_count, r2.reject_count) == (2, 0, 1)


def test_run_scoped_queries_are_per_run(two_runs):
    assert len(gather_report_data(two_runs, "run_1").all_queries) == 1
    assert len(gather_report_data(two_runs, "run_2").all_queries) == 1
    assert len(gather_report_data(two_runs).all_queries) == 2


def test_an_unscoped_report_still_covers_everything(two_runs):
    """The default stays cumulative, so nothing that relied on it changes."""
    everything = gather_report_data(two_runs)

    assert everything.run_id is None
    assert everything.total_candidates_ever == 5
    assert {c.repo_full_name for c in everything.ranked} == {
        "org/shared", "org/only1", "org/new1"}


# --- cumulative vs per-run --------------------------------------------------


def test_cumulative_totals_are_present_and_differ_from_the_run(two_runs):
    r2 = gather_report_data(two_runs, "run_2")

    assert r2.cumulative["candidates"] == 5
    assert r2.cumulative["runs"] == 2
    assert r2.total_candidates_ever == 3, "the run's own universe is smaller"


def test_markdown_labels_the_cumulative_section_as_all_runs(two_runs):
    md = render_markdown(gather_report_data(two_runs, "run_2"))

    assert "## Cumulative project state (all runs)" in md
    assert "not run_2" in md
    assert "# Dependency Map - run_2" in md


def test_markdown_states_the_run_scope_in_the_coverage_section(two_runs):
    md = render_markdown(gather_report_data(two_runs, "run_2"))

    assert "## Coverage and sampling (run_2)" in md
    assert "describes **run_2 only**" in md
    assert "Repositories **surfaced by run_2**" in md


def test_a_cumulative_report_has_no_cumulative_section(two_runs):
    """Without a run to contrast against, the heading would be noise."""
    md = render_markdown(gather_report_data(two_runs))

    assert "Cumulative project state" not in md
    assert md.startswith("# Dependency Map\n")


# --- provenance -------------------------------------------------------------


def test_the_report_flags_that_carried_over_evidence_may_predate_the_run(two_runs):
    md = render_markdown(gather_report_data(two_runs, "run_2"))

    assert "Where this run's evidence came from" in md
    assert "first found by an earlier run" in md
    assert "first_seen_run_id" in md


def test_no_provenance_caveat_when_every_candidate_is_new(two_runs):
    """Run 1 saw nothing before it, so the caveat would be false there."""
    md = render_markdown(gather_report_data(two_runs, "run_1"))

    assert "Where this run's evidence came from" not in md


def test_the_report_does_not_invent_evidence_timestamps(two_runs):
    """The schema stores no per-evidence timestamp, so none may be claimed."""
    md = render_markdown(gather_report_data(two_runs, "run_2"))

    assert "does not timestamp each evidence row" in md


# --- outputs ----------------------------------------------------------------


def test_csv_and_markdown_agree_under_run_scoping(two_runs):
    data = gather_report_data(two_runs, "run_2")
    rows = list(csv.DictReader(io.StringIO(render_csv(data))))
    md = render_markdown(data)

    assert len(rows) == len(data.ranked) == 2
    for row, candidate in zip(rows, data.ranked):
        assert row["candidate_id"] == candidate.candidate_id
        assert row["rank"] == str(candidate.rank)
        assert candidate.repo_full_name in md


def test_rejects_never_appear_in_a_run_scoped_report(two_runs):
    data = gather_report_data(two_runs, "run_2")

    assert "org/new2" not in render_csv(data)
    assert "org/new2" not in render_markdown(data)


def test_write_report_passes_the_run_through(two_runs, tmp_path):
    summary = write_report(two_runs, tmp_path / "c.csv", tmp_path / "r.md",
                           run_id="run_2")

    assert summary.ranked_count == 2
    assert "run_2" in (tmp_path / "r.md").read_text(encoding="utf-8")


def test_two_run_scoped_reports_do_not_overwrite_each_other(two_runs, tmp_path):
    """The property that keeps run 1's committed artefacts safe: a run-2
    report is a different file with different content."""
    write_report(two_runs, tmp_path / "r1.csv", tmp_path / "r1.md", run_id="run_1")
    write_report(two_runs, tmp_path / "r2.csv", tmp_path / "r2.md", run_id="run_2")

    one = (tmp_path / "r1.csv").read_text(encoding="utf-8")
    two = (tmp_path / "r2.csv").read_text(encoding="utf-8")

    assert one != two
    assert "only1" in one and "only1" not in two
    assert "new1" in two and "new1" not in one


def test_regenerating_a_run_scoped_report_is_deterministic(two_runs, tmp_path):
    write_report(two_runs, tmp_path / "a.csv", tmp_path / "a.md", run_id="run_2")
    write_report(two_runs, tmp_path / "b.csv", tmp_path / "b.md", run_id="run_2")

    assert (tmp_path / "a.csv").read_text(encoding="utf-8") == \
        (tmp_path / "b.csv").read_text(encoding="utf-8")


# --- comparison arithmetic --------------------------------------------------


def test_run_candidate_counts_add_up(two_runs):
    counts = storage.run_candidate_counts(two_runs, "run_2")

    assert counts["new"] + counts["previously_seen"] == counts["surfaced"]
    assert counts["enriched"] <= counts["surfaced"]


def test_cumulative_candidates_is_deduplicated_not_a_sum(two_runs):
    """The shared candidate must be counted once across the project, even
    though both runs surfaced it."""
    r1 = storage.run_candidate_counts(two_runs, "run_1")
    r2 = storage.run_candidate_counts(two_runs, "run_2")
    cumulative = storage.cumulative_counts(two_runs)

    assert r1["surfaced"] + r2["surfaced"] == 6
    assert cumulative["candidates"] == 5, "the shared repository is one row"


def test_previously_seen_is_derived_from_first_sighting(two_runs):
    counts = storage.run_candidate_counts(two_runs, "run_2")
    shared = make_candidate_id("https://github.com/org/shared")

    assert storage.get_candidate(two_runs, shared)["first_seen_run_id"] == "run_1"
    assert counts["previously_seen"] == 1


# --- bounded maintenance enrichment note ------------------------------------


def _add_maintenance(conn, candidate_id):
    storage.upsert_maintenance_evidence(
        conn, candidate_id=candidate_id, document_library_count=2,
        same_file_library_count=1, custom_logic_present=True,
        custom_formatting_present=True, custom_validation_present=False,
        custom_error_handling_present=False, files_inspected=2)


def test_partial_maintenance_enrichment_is_disclosed(two_runs, weights_and_caps):
    """Most of a ranked table resting on an uninspected zero is a fact a
    reader needs, because that zero costs 15 percent of the weight."""
    weights, caps = weights_and_caps
    shared = make_candidate_id("https://github.com/org/shared")
    _add_maintenance(two_runs, shared)
    ScoringEngine(two_runs, weights, caps).score_one(shared)

    md = render_markdown(gather_report_data(two_runs, "run_2"))

    assert "Maintenance-burden evidence was enriched for a bounded" in md
    assert "may still have unknown `maintenance_burden`" in md
    assert "never inspected" in md
    assert "15 percent of the weight" in md


def test_the_note_counts_only_genuinely_enriched_candidates(
    two_runs, weights_and_caps
):
    weights, caps = weights_and_caps
    shared = make_candidate_id("https://github.com/org/shared")
    _add_maintenance(two_runs, shared)
    ScoringEngine(two_runs, weights, caps).score_one(shared)

    data = gather_report_data(two_runs, "run_2")

    assert data.maintenance_enriched == 1
    assert len(data.ranked) == 2
    assert "1 of the 2 ranked candidates" in render_markdown(data)


def test_no_note_when_nothing_was_enriched_but_a_warning_instead(two_runs):
    """A table where nothing was inspected needs the opposite warning, not
    silence."""
    md = render_markdown(gather_report_data(two_runs, "run_2"))

    assert "Maintenance burden was not collected for this set" in md
    assert "not because its document code is thin" in md


def test_no_note_when_every_candidate_was_enriched(two_runs, weights_and_caps):
    """With nothing missing there is no asymmetry to disclose."""
    weights, caps = weights_and_caps
    engine = ScoringEngine(two_runs, weights, caps)
    for name in ("org/shared", "org/new1"):
        cid = make_candidate_id(f"https://github.com/{name}")
        _add_maintenance(two_runs, cid)
        engine.score_one(cid)

    md = render_markdown(gather_report_data(two_runs, "run_2"))

    assert "Maintenance-burden evidence was enriched" not in md
    assert "Maintenance burden was not collected" not in md


def test_maintenance_enrichment_does_not_change_the_rubric(
    two_runs, weights_and_caps
):
    """Enriching evidence must move a score only through the existing rubric,
    never by re-weighting anything."""
    from dependency_map.maintenance import MaintenanceSignals, rung_for

    weights, caps = weights_and_caps
    shared = make_candidate_id("https://github.com/org/shared")
    _add_maintenance(two_runs, shared)
    result = ScoringEngine(two_runs, weights, caps).score_one(shared)

    expected, _ = rung_for(MaintenanceSignals(
        candidate_id=shared, document_library_count=2, same_file_library_count=1,
        custom_logic_present=True, custom_formatting_present=True,
        files_inspected=2))
    assert result.dimensions["maintenance_burden"].score == expected
