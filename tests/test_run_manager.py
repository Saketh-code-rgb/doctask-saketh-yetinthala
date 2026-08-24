"""The run manager: stage orchestration, resumability, and partial failure.

Every test uses a seeded temporary database and fake clients. Nothing here
touches the network.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from dependency_map import storage
from dependency_map.dedup import make_candidate_id, normalize_repo_url
from dependency_map.discovery import DiscoveryEngine, DiscoveryError, QueryGenerator
from dependency_map.evidence import EvidenceCollector
from dependency_map.library_universe import load_library_universe
from dependency_map.reliability import ApiError, RateLimited
from dependency_map.scoring import ScoringEngine
from dependency_map.run_manager import (
    STAGE_DISCOVERY,
    STAGE_EVIDENCE,
    STAGE_QUALIFICATION,
    STAGE_SCORING,
    STAGES,
    RunError,
    RunManager,
)
from test_evidence import FakeClient, README, REQUIREMENTS, entry, file_at, metadata

WINDOWS = ("size:0..250",)


@pytest.fixture(scope="module")
def universe():
    return load_library_universe()


# --- discovery fakes -------------------------------------------------------


class Page:
    def __init__(self, results, total=None):
        self.results = tuple(results)
        self.total_count = len(self.results) if total is None else total
        self.capped = self.total_count > 1000
        self.incomplete_results = False


class Hit:
    def __init__(self, full_name, rank=1):
        owner, _, name = full_name.partition("/")
        self.repo_full_name = full_name
        self.repo_url = f"https://github.com/{full_name}"
        self.repo_owner, self.repo_name = owner, name
        self.path = "requirements.txt"
        self.rank = rank
        self.evidence_url = f"https://github.com/{full_name}/blob/main/requirements.txt"
        self.excerpt = ""
        self.sha = "a"


class DiscoveryClient:
    """Returns the same repositories for every query."""

    def __init__(self, repos, fail=None):
        self._repos = repos
        self._fail = fail
        self.queries = []

    def search_code(self, query, per_page=30, page=1, use_cache=True):
        self.queries.append(query)
        if self._fail:
            raise self._fail
        return Page([Hit(r, i) for i, r in enumerate(self._repos, 1)])


class EvidenceClient(FakeClient):
    """An evidence client that answers for any repository."""

    def __init__(self, **kw):
        super().__init__(
            listing=[entry("README.md"), entry("requirements.txt"),
                     entry("app", "dir")],
            files={"README.md": file_at("README.md", README),
                   "requirements.txt": file_at("requirements.txt", REQUIREMENTS)},
            **kw,
        )


def build(conn, universe, repos=("acme/one",), *, discovery_fail=None,
          evidence_client=None, tiers_windows=WINDOWS):
    generator = QueryGenerator(universe, windows=tiers_windows,
                               include_co_occurrence=False)
    engine = DiscoveryEngine(
        conn, DiscoveryClient(repos, fail=discovery_fail), generator
    )
    collector = EvidenceCollector(
        conn, evidence_client or EvidenceClient(), universe
    )
    weights = yaml.safe_load(
        Path("config/weights.yaml").read_text(encoding="utf-8"))
    return RunManager(
        conn, discovery_engine=engine, evidence_collector=collector,
        query_generator=generator,
        scoring_engine=ScoringEngine(
            conn, weights["dimension_weights"], weights["gate_caps"]),
    ), engine, collector


# --- run setup -------------------------------------------------------------


def test_a_run_row_is_created(conn, universe):
    manager, _, _ = build(conn, universe)
    report = manager.run(stages=[STAGE_DISCOVERY], tiers=[1], query_limit=1)

    run = storage.get_run(conn, report.run_id)
    assert run is not None
    assert run["finished_at"] is not None


def test_the_rotation_is_recorded_on_the_run(conn, universe):
    manager, _, _ = build(conn, universe)
    report = manager.run(stages=[STAGE_DISCOVERY], tiers=[1], query_limit=1)

    assert "run #1" in storage.get_run(conn, report.run_id)["notes"]
    assert report.rotation


def test_run_ids_increment(conn, universe):
    """A second run uses tier 3, which is sliced, so its queries are fresh."""
    manager, _, _ = build(conn, universe)
    first = manager.run(stages=[STAGE_DISCOVERY], tiers=[3], query_limit=1)

    manager2, _, _ = build(conn, universe,
                           tiers_windows=("size:8001..16000",))
    second = manager2.run(stages=[STAGE_DISCOVERY], tiers=[3], query_limit=1)

    assert first.run_id == "run_1"
    assert second.run_id == "run_2"


def test_a_tier_one_only_rerun_is_refused_as_a_replay(conn, universe):
    """A known limitation, surfaced rather than hidden.

    Tier-1 queries carry no slice, because the one measured tier-1 query
    returned 662 results and is fully enumerable. That makes them byte
    identical between runs, so a second tier-1-only run genuinely would replay
    rather than discover, and the fresh-batch guard says so. Rotating tier 1
    would need a page-offset axis, which discovery does not yet have.
    """
    from dependency_map.dedup import FreshBatchError

    manager, _, _ = build(conn, universe)
    manager.run(stages=[STAGE_DISCOVERY], tiers=[1], query_limit=1)

    manager2, _, _ = build(conn, universe)
    with pytest.raises(FreshBatchError, match="already executed"):
        manager2.run(stages=[STAGE_DISCOVERY], tiers=[1], query_limit=1)


def test_starting_an_existing_run_id_is_refused(conn, universe):
    manager, _, _ = build(conn, universe)
    storage.create_run(conn, "run_1")

    with pytest.raises(RunError, match="already exists"):
        manager.start_run("run_1")


def test_an_unknown_stage_is_refused(conn, universe):
    manager, _, _ = build(conn, universe)

    with pytest.raises(RunError, match="Unknown stage"):
        manager.run(stages=["reporting"])


# --- stage isolation -------------------------------------------------------


def test_discovery_only_collects_no_evidence(conn, universe):
    manager, _, collector = build(conn, universe)
    report = manager.run(stages=[STAGE_DISCOVERY], tiers=[1], query_limit=1)

    assert report.discovery is not None
    assert report.evidence_completed == 0
    assert collector.pending(), "candidates should still be awaiting evidence"


def test_evidence_only_runs_without_discovery(conn, universe):
    manager, _, _ = build(conn, universe)
    manager.run(stages=[STAGE_DISCOVERY], tiers=[1], query_limit=1)

    manager2, _, _ = build(conn, universe)
    report = manager2.run(run_id="run_1", stages=[STAGE_EVIDENCE])

    assert report.evidence_completed >= 1
    assert report.discovery is None


def test_both_stages_run_in_order(conn, universe):
    manager, _, collector = build(conn, universe)
    report = manager.run(stages=STAGES, tiers=[1], query_limit=1)

    assert report.discovery is not None
    assert report.evidence_completed >= 1
    assert collector.pending() == []


def test_the_run_manager_holds_no_qualification_or_scoring_logic():
    source = Path("src/dependency_map/run_manager.py").read_text(encoding="utf-8")

    for term in ["qualification_status", "final_score", "upsert_score",
                 "upsert_qualification", "raw_weighted_score", "def qualify",
                 "def score"]:
        assert term not in source


def test_all_four_stages_exist_in_order():
    assert STAGES == ("discovery", "evidence", "qualification", "scoring")


# --- evidence population ---------------------------------------------------


def test_evidence_is_populated_for_discovered_candidates(conn, universe):
    manager, _, _ = build(conn, universe, repos=("acme/one",))
    manager.run(stages=STAGES, tiers=[1], query_limit=1)

    cid = make_candidate_id("https://github.com/acme/one")
    assert storage.get_pipeline_evidence(conn, cid) is not None
    assert storage.get_business_evidence(conn, cid) is not None
    assert storage.list_evidence_trail_for_candidate(conn, cid)


def test_multiple_candidates_are_all_collected(conn, universe):
    manager, _, _ = build(conn, universe, repos=("acme/one", "acme/two", "acme/three"))
    report = manager.run(stages=STAGES, tiers=[1], query_limit=1)

    assert report.evidence_completed == 3
    assert report.candidates_needing_evidence == 3


def test_evidence_limit_is_respected(conn, universe):
    manager, _, collector = build(conn, universe,
                                  repos=("acme/one", "acme/two", "acme/three"))
    report = manager.run(stages=STAGES, tiers=[1], query_limit=1, evidence_limit=2)

    assert report.evidence_completed == 2
    assert len(collector.pending()) == 1


# --- resumability ----------------------------------------------------------


def test_rerunning_evidence_skips_completed_candidates(conn, universe):
    """The stage asks what is missing, so a rerun has less to do rather than
    repeating itself."""
    manager, _, _ = build(conn, universe, repos=("acme/one", "acme/two"))
    manager.run(stages=STAGES, tiers=[1], query_limit=1)

    manager2, _, _ = build(conn, universe, repos=("acme/one", "acme/two"))
    second = manager2.run(run_id="run_1", stages=[STAGE_EVIDENCE])

    assert second.candidates_needing_evidence == 0
    assert second.evidence_completed == 0


def test_an_interrupted_run_resumes_from_where_it_stopped(conn, universe):
    """Half the candidates collected, then a rerun finishes only the rest."""
    manager, _, _ = build(conn, universe,
                          repos=("acme/one", "acme/two", "acme/three", "acme/four"))
    first = manager.run(stages=STAGES, tiers=[1], query_limit=1, evidence_limit=2)

    assert first.evidence_completed == 2

    evidence_client = EvidenceClient()
    manager2, _, collector = build(conn, universe, evidence_client=evidence_client)
    second = manager2.run(run_id="run_1", stages=[STAGE_EVIDENCE])

    assert second.evidence_completed == 2, "only the two that were missing"
    assert collector.pending() == []
    # The two already-complete candidates were never fetched again.
    assert evidence_client.count("metadata") == 2


def test_completed_evidence_survives_a_later_failure(conn, universe):
    manager, _, _ = build(conn, universe, repos=("acme/one", "acme/two"))
    manager.run(stages=STAGES, tiers=[1], query_limit=1, evidence_limit=1)

    done = [c for c in storage.candidates_needing_evidence(conn)]
    assert len(done) == 1, "one candidate still pending, one already committed"


def test_cached_responses_are_reused_on_resume(conn, universe):
    """Evidence for an already-complete candidate is not re-fetched at all,
    which is stronger than relying on the HTTP cache."""
    manager, _, _ = build(conn, universe, repos=("acme/one",))
    manager.run(stages=STAGES, tiers=[1], query_limit=1)

    client = EvidenceClient()
    manager2, _, _ = build(conn, universe, evidence_client=client)
    manager2.run(run_id="run_1", stages=[STAGE_EVIDENCE])

    assert client.calls == []


# --- partial and systemic failure ------------------------------------------


def test_one_candidate_failing_does_not_stop_the_others(conn, universe):
    class FlakyClient(EvidenceClient):
        def get_repository(self, owner, repo, use_cache=True):
            self.calls.append(("metadata", f"{owner}/{repo}"))
            if repo == "two":
                raise ApiError(404, "https://x", "Not Found")
            return metadata(repo_owner=owner, repo_name=repo,
                            full_name=f"{owner}/{repo}")

    manager, _, _ = build(conn, universe,
                          repos=("acme/one", "acme/two", "acme/three"),
                          evidence_client=FlakyClient())
    report = manager.run(stages=STAGES, tiers=[1], query_limit=1)

    assert report.evidence_completed == 2
    assert report.evidence_failed == 1
    assert report.failures


def test_a_failure_is_recorded_not_swallowed(conn, universe):
    class FailingClient(EvidenceClient):
        def get_repository(self, owner, repo, use_cache=True):
            raise ApiError(500, "https://x", "server error")

    manager, _, _ = build(conn, universe, repos=("acme/one",),
                          evidence_client=FailingClient())
    report = manager.run(stages=STAGES, tiers=[1], query_limit=1)

    assert report.evidence_failed == 1
    assert any("server error" in error for _, error in report.failures)


def test_a_failed_candidate_stays_pending_for_a_later_rerun(conn, universe):
    class FailingClient(EvidenceClient):
        def get_repository(self, owner, repo, use_cache=True):
            raise ApiError(500, "https://x", "server error")

    manager, _, collector = build(conn, universe, repos=("acme/one",),
                                  evidence_client=FailingClient())
    manager.run(stages=STAGES, tiers=[1], query_limit=1)

    assert len(collector.pending()) == 1


def test_a_systemic_rate_limit_stops_evidence_collection(conn, universe):
    class LimitedClient(EvidenceClient):
        def get_repository(self, owner, repo, use_cache=True):
            raise RateLimited("budget exhausted for 40 minutes")

    manager, _, _ = build(conn, universe, repos=("acme/one", "acme/two"),
                          evidence_client=LimitedClient())

    with pytest.raises(RateLimited):
        manager.run(stages=STAGES, tiers=[1], query_limit=1)


def test_a_systemic_discovery_failure_stops_the_run(conn, universe):
    manager, _, _ = build(conn, universe,
                          discovery_fail=RateLimited("budget exhausted"))

    with pytest.raises(DiscoveryError):
        manager.run(stages=[STAGE_DISCOVERY], tiers=[1], query_limit=1)


def test_discovery_results_survive_a_later_evidence_failure(conn, universe):
    class FailingClient(EvidenceClient):
        def get_repository(self, owner, repo, use_cache=True):
            raise ApiError(500, "https://x", "boom")

    manager, _, _ = build(conn, universe, repos=("acme/one",),
                          evidence_client=FailingClient())
    report = manager.run(stages=STAGES, tiers=[1], query_limit=1)

    assert storage.count_candidates(conn) == 1
    assert report.discovery.new_candidates == 1


# --- statistics ------------------------------------------------------------


def test_run_statistics_are_reported(conn, universe):
    manager, _, _ = build(conn, universe, repos=("acme/one", "acme/two"))
    report = manager.run(stages=STAGES, tiers=[1], query_limit=2)

    assert report.discovery.queries_executed == 2
    assert report.discovery.unique_repositories == 2
    assert report.discovery.new_candidates == 2
    assert report.candidates_needing_evidence == 2
    assert report.evidence_completed == 2


def test_summary_lines_cover_every_reported_number(conn, universe):
    manager, _, _ = build(conn, universe)
    report = manager.run(stages=STAGES, tiers=[1], query_limit=1)
    text = "\n".join(report.summary_lines())

    for label in ["run ", "stages", "rotation", "queries executed",
                  "discovered candidates", "candidates needing evidence",
                  "evidence completed", "evidence failed"]:
        assert label in text


def test_summary_contains_no_secret(conn, universe):
    manager, _, _ = build(conn, universe)
    report = manager.run(stages=STAGES, tiers=[1], query_limit=1)
    text = "\n".join(report.summary_lines())

    for pattern in ["ghp_", "github_pat_", "Bearer", "Authorization", "api_key"]:
        assert pattern not in text


# --- safety ----------------------------------------------------------------


def test_the_run_manager_makes_no_raw_http_calls():
    source = Path("src/dependency_map/run_manager.py").read_text(encoding="utf-8")

    for forbidden in ["import requests", "urllib.request", "http.client", "socket"]:
        assert forbidden not in source


def test_no_outreach_capability():
    source = Path("src/dependency_map/run_manager.py").read_text(encoding="utf-8")

    for term in ["smtp", "send_email", "mailto:", "sendmail"]:
        assert term not in source.lower()
