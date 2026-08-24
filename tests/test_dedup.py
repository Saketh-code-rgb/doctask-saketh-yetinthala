"""Deduplication, cross-run tracking, and the fresh-batch mechanism.

Every test runs against a temporary database. Nothing here touches the network.
The cross-run scenarios use synthetic repositories, not real ones.
"""

from __future__ import annotations

from datetime import date

import pytest

from dependency_map import storage
from dependency_map.dedup import (
    NEW_FOR_RUN,
    PREVIOUSLY_SEEN,
    WINDOWS_PER_RUN,
    FreshBatchError,
    classify_candidate,
    make_candidate_id,
    normalize_repo_url,
    plan_rotation,
    SIZE_BUCKETS,
    size_windows,
    run_stats,
    verify_fresh_batch,
)
from dependency_map.discovery import GeneratedQuery, QueryGenerator
from dependency_map.library_universe import load_library_universe

ANCHOR = date(2026, 6, 30)


@pytest.fixture(scope="module")
def universe():
    return load_library_universe()


# --- A. URL normalization --------------------------------------------------


def test_trailing_slash_is_stripped():
    assert normalize_repo_url("https://github.com/acme/widget/") == \
        "https://github.com/acme/widget"


def test_case_is_normalized():
    """GitHub owner and repository names are case-insensitive for resolution,
    so lowercasing collapses a real duplicate rather than inventing one."""
    assert normalize_repo_url("https://GitHub.com/Acme/Widget") == \
        "https://github.com/acme/widget"


def test_git_suffix_is_stripped():
    assert normalize_repo_url("https://github.com/acme/widget.git") == \
        "https://github.com/acme/widget"


def test_www_prefix_is_stripped():
    assert normalize_repo_url("https://www.github.com/acme/widget") == \
        "https://github.com/acme/widget"


def test_query_string_and_fragment_are_dropped():
    assert normalize_repo_url("https://github.com/acme/widget?tab=readme#install") == \
        "https://github.com/acme/widget"


def test_surrounding_whitespace_is_ignored():
    assert normalize_repo_url("  https://github.com/acme/widget  ") == \
        "https://github.com/acme/widget"


def test_normalization_is_idempotent():
    """normalize(normalize(url)) == normalize(url), for every variant form."""
    variants = [
        "https://github.com/acme/widget",
        "https://GitHub.com/Acme/Widget/",
        "https://www.github.com/ACME/widget.git",
        "  https://github.com/acme/widget?tab=readme  ",
        "https://github.com/a-b_c.d/x.y-z",
    ]
    for url in variants:
        once = normalize_repo_url(url)
        assert normalize_repo_url(once) == once, url


def test_different_repositories_are_not_collapsed():
    """The dangerous failure is over-normalising two companies into one."""
    distinct = [
        "https://github.com/acme/widget",
        "https://github.com/acme/widgets",
        "https://github.com/acme-corp/widget",
        "https://github.com/other/widget",
        "https://gitlab.com/acme/widget",
        "https://github.com/acme/widget-pro",
    ]
    normalized = [normalize_repo_url(u) for u in distinct]

    assert len(set(normalized)) == len(distinct)


def test_hyphens_and_underscores_are_preserved():
    """Both are meaningful in a repository name; folding them would merge two
    genuinely different repositories."""
    assert normalize_repo_url("https://github.com/a/my-repo") != \
        normalize_repo_url("https://github.com/a/my_repo")


# --- B. candidate_id -------------------------------------------------------


def test_candidate_id_is_deterministic():
    assert make_candidate_id("https://github.com/acme/widget") == \
        make_candidate_id("https://github.com/acme/widget")


@pytest.mark.parametrize("variant", [
    "https://github.com/acme/widget",
    "https://github.com/acme/widget/",
    "https://GitHub.com/Acme/Widget",
    "https://www.github.com/acme/widget",
    "https://github.com/acme/widget.git",
    "  https://github.com/ACME/WIDGET/  ",
])
def test_equivalent_urls_share_a_candidate_id(variant):
    assert make_candidate_id(variant) == \
        make_candidate_id("https://github.com/acme/widget")


def test_different_repositories_get_different_ids():
    ids = {make_candidate_id(u) for u in [
        "https://github.com/acme/widget",
        "https://github.com/acme/widgets",
        "https://github.com/other/widget",
    ]}
    assert len(ids) == 3


def test_candidate_id_is_stable_across_queries_slices_and_runs():
    """The property the whole dedup scheme rests on."""
    url = "https://github.com/acme/widget"
    assert len({make_candidate_id(url) for _ in range(50)}) == 1


def test_candidate_id_has_a_readable_prefix():
    assert make_candidate_id("https://github.com/a/b").startswith("c_")


# --- helpers for the database scenarios ------------------------------------


def _record(conn, run_id, query, repos, *, window=None, total=None, source="github_code_search"):
    """Persist one query execution and the repositories it surfaced."""
    query_id = storage.create_discovery_query(
        conn, run_id=run_id, discovery_source=source, query=query,
        search_window=window, discovery_tier=3,
    )
    for rank, repo in enumerate(repos, 1):
        url = f"https://github.com/{repo}"
        candidate_id = make_candidate_id(url)
        owner, _, name = repo.partition("/")
        storage.insert_candidate_if_new(
            conn, candidate_id=candidate_id, repo_url=normalize_repo_url(url),
            repo_owner=owner, repo_name=name, first_seen_run_id=run_id,
        )
        storage.insert_discovery_evidence(
            conn, query_id=query_id, candidate_id=candidate_id,
            discovery_result_rank=rank,
        )
    storage.update_query_results(
        conn, query_id,
        total_count=len(repos) if total is None else total,
        returned_count=len(repos),
    )
    return query_id


def _run(conn, run_id, started_at):
    storage.create_run(conn, run_id, started_at=started_at)


# --- C. same-run deduplication ---------------------------------------------


def test_one_repository_across_two_queries_is_one_candidate(conn):
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "q1", ["acme/widget"])
    _record(conn, "run_1", "q2", ["acme/widget"])

    candidate_id = make_candidate_id("https://github.com/acme/widget")

    assert storage.count_candidates(conn) == 1
    assert len(storage.list_discovery_evidence_for_candidate(conn, candidate_id)) == 2


def test_overlap_information_is_preserved(conn):
    """Which queries found it, not merely that something did."""
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "q1", ["acme/widget"])
    _record(conn, "run_1", "q2", ["acme/widget"])

    candidate_id = make_candidate_id("https://github.com/acme/widget")
    evidence = storage.list_discovery_evidence_for_candidate(conn, candidate_id)

    assert {e["query"] for e in evidence} == {"q1", "q2"}


def test_result_rank_is_preserved_per_query(conn):
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "q1", ["other/repo", "acme/widget"])
    _record(conn, "run_1", "q2", ["acme/widget"])

    candidate_id = make_candidate_id("https://github.com/acme/widget")
    ranks = {e["query"]: e["discovery_result_rank"]
             for e in storage.list_discovery_evidence_for_candidate(conn, candidate_id)}

    assert ranks == {"q1": 2, "q2": 1}


def test_the_same_query_matching_a_repo_twice_records_one_hit(conn):
    """Phase 6's UNIQUE(query_id, candidate_id) rule, still in force."""
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    query_id = _record(conn, "run_1", "q1", ["acme/widget"])
    second = storage.insert_discovery_evidence(
        conn, query_id=query_id,
        candidate_id=make_candidate_id("https://github.com/acme/widget"),
        discovery_result_rank=9,
    )

    assert second is None
    assert len(storage.list_discovery_evidence_for_query(conn, query_id)) == 1


def test_equivalent_url_forms_collapse_to_one_candidate(conn):
    """Two queries spelling the same repository differently must not create
    two candidates."""
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    q1 = storage.create_discovery_query(
        conn, run_id="run_1", discovery_source="github_code_search", query="q1")
    q2 = storage.create_discovery_query(
        conn, run_id="run_1", discovery_source="github_code_search", query="q2")

    for query_id, url in [(q1, "https://github.com/Acme/Widget"),
                          (q2, "https://github.com/acme/widget/")]:
        candidate_id = make_candidate_id(url)
        storage.insert_candidate_if_new(
            conn, candidate_id=candidate_id, repo_url=normalize_repo_url(url),
            repo_owner="acme", repo_name="widget", first_seen_run_id="run_1",
        )
        storage.insert_discovery_evidence(
            conn, query_id=query_id, candidate_id=candidate_id)

    assert storage.count_candidates(conn) == 1


# --- D. cross-run behaviour ------------------------------------------------


@pytest.fixture
def two_runs(conn):
    """Run 1 finds A, B, C. Run 2 finds B, C, D, E."""
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "r1q1", ["org/a", "org/b", "org/c"],
            window="size:0..250")

    _run(conn, "run_2", "2026-02-01T00:00:00Z")
    _record(conn, "run_2", "r2q1", ["org/b", "org/c", "org/d", "org/e"],
            window="size:251..500")
    return conn


def _cid(name):
    return make_candidate_id(f"https://github.com/{name}")


def test_run_one_candidates_are_all_new(two_runs):
    stats = run_stats(two_runs, "run_1")

    assert stats.unique_repositories == 3
    assert stats.new_candidates == 3
    assert stats.previously_seen == 0


def test_run_two_separates_new_from_previously_seen(two_runs):
    stats = run_stats(two_runs, "run_2")

    assert stats.unique_repositories == 4
    assert stats.previously_seen == 2   # B and C
    assert stats.new_candidates == 2    # D and E


def test_repeat_candidates_are_classified_as_previously_seen(two_runs):
    for name in ("org/b", "org/c"):
        assert classify_candidate(two_runs, _cid(name), "run_2") == PREVIOUSLY_SEEN


def test_genuinely_new_candidates_are_classified_new(two_runs):
    for name in ("org/d", "org/e"):
        assert classify_candidate(two_runs, _cid(name), "run_2") == NEW_FOR_RUN


def test_run_one_candidates_are_new_within_run_one(two_runs):
    """Classification is relative to the run being asked about."""
    assert classify_candidate(two_runs, _cid("org/b"), "run_1") == NEW_FOR_RUN


def test_a_run_one_only_candidate_stays_a_run_one_candidate(two_runs):
    """A is never resurfaced, and is not disturbed by run 2."""
    evidence = storage.list_discovery_evidence_for_candidate(two_runs, _cid("org/a"))

    assert len(evidence) == 1
    assert evidence[0]["run_id"] == "run_1"
    assert storage.get_candidate(two_runs, _cid("org/a"))["first_seen_run_id"] == "run_1"


def test_previously_seen_evidence_is_still_recorded(two_runs):
    """A repeat sighting is not suppressed: it proves the slice surfaced that
    repository again, which is what makes fresh-batch checkable."""
    evidence = storage.list_discovery_evidence_for_candidate(two_runs, _cid("org/b"))

    assert len(evidence) == 2
    assert {e["run_id"] for e in evidence} == {"run_1", "run_2"}


def test_first_seen_run_is_not_rewritten(two_runs):
    assert storage.get_candidate(two_runs, _cid("org/b"))["first_seen_run_id"] == "run_1"


def test_total_candidates_across_both_runs(two_runs):
    assert storage.count_candidates(two_runs) == 5  # A B C D E


def test_ordering_uses_started_at_not_run_id(conn):
    """A later-named run that actually ran first must not be treated as
    later."""
    _run(conn, "run_zebra", "2026-01-01T00:00:00Z")
    _record(conn, "run_zebra", "q", ["org/a"])
    _run(conn, "run_alpha", "2026-02-01T00:00:00Z")
    _record(conn, "run_alpha", "q2", ["org/a"])

    assert run_stats(conn, "run_alpha").previously_seen == 1
    assert run_stats(conn, "run_zebra").previously_seen == 0


# --- E. multi-query duplication within run 2 -------------------------------


def test_a_new_candidate_found_by_three_queries_counts_once(conn):
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "r1q1", ["org/a"])

    _run(conn, "run_2", "2026-02-01T00:00:00Z")
    for q in ("r2q1", "r2q2", "r2q3"):
        _record(conn, "run_2", q, ["org/d"])

    stats = run_stats(conn, "run_2")

    assert stats.new_candidates == 1, "D must count once, not three times"
    assert stats.unique_repositories == 1
    assert stats.raw_results == 3, "raw results still reflect all three hits"
    assert len(storage.list_discovery_evidence_for_candidate(conn, _cid("org/d"))) == 3
    assert storage.count_candidates(conn) == 2


def test_a_previously_seen_candidate_found_repeatedly_counts_once(conn):
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "r1q1", ["org/b"])

    _run(conn, "run_2", "2026-02-01T00:00:00Z")
    for q in ("r2q1", "r2q2"):
        _record(conn, "run_2", q, ["org/b"])

    stats = run_stats(conn, "run_2")

    assert stats.previously_seen == 1
    assert stats.new_candidates == 0
    assert stats.raw_results == 2


# --- F. fresh-batch rotation -----------------------------------------------


def test_rotation_is_deterministic():
    a = plan_rotation(2, anchor=ANCHOR)
    b = plan_rotation(2, anchor=ANCHOR)

    assert a == b
    assert a.windows == b.windows


def test_run_two_windows_differ_from_run_one():
    one = plan_rotation(1, anchor=ANCHOR)
    two = plan_rotation(2, anchor=ANCHOR)

    assert set(one.windows).isdisjoint(two.windows)


def test_run_two_slices_sit_above_run_one():
    """The walk moves up the bucket pool, so runs partition file size rather
    than overlap."""
    one = plan_rotation(1, anchor=ANCHOR)
    two = plan_rotation(2, anchor=ANCHOR)

    assert SIZE_BUCKETS.index(two.windows[0]) > SIZE_BUCKETS.index(one.windows[-1])


def test_the_first_two_runs_never_repeat_a_slice():
    """Two runs is what the pool guarantees, and the guarantee that matters:
    run 2 must not replay run 1."""
    seen: set[str] = set()
    for index in (1, 2):
        windows = set(plan_rotation(index, anchor=ANCHOR).windows)
        assert seen.isdisjoint(windows), f"run {index} reused a slice"
        seen |= windows

    assert len(seen) == 2 * WINDOWS_PER_RUN
    assert seen == set(SIZE_BUCKETS), "two runs should cover the whole pool"


def test_the_bucket_pool_wraps_on_the_third_run():
    """A documented limit, asserted rather than left to be discovered.

    The date walk could march backwards forever; a size pool is finite. Run 3
    reuses run 1's slices, and `verify_fresh_batch` is what catches that. If
    the pool is ever widened, this test should fail and be updated on purpose.
    """
    assert plan_rotation(3, anchor=ANCHOR).windows == \
        plan_rotation(1, anchor=ANCHOR).windows


def test_library_offset_rotates_with_the_run():
    assert plan_rotation(1, anchor=ANCHOR).library_offset == 0
    assert plan_rotation(2, anchor=ANCHOR).library_offset == 1
    assert plan_rotation(3, anchor=ANCHOR).library_offset == 2


def test_rotation_description_is_human_readable():
    plan = plan_rotation(2, anchor=ANCHOR)

    assert "run #2" in plan.description
    assert "library order rotated by 1" in plan.description
    # The description names the actual window bounds, so the rotation is
    # legible from runs.notes without recomputing it.
    assert plan.windows[0].removeprefix("size:") in plan.description
    assert plan.windows[-1].removeprefix("size:") in plan.description


def test_rotation_is_not_random():
    """Nothing is varied merely to manufacture a difference."""
    plans = [plan_rotation(2, anchor=ANCHOR) for _ in range(10)]

    assert len({p.windows for p in plans}) == 1


def test_run_index_must_start_at_one():
    with pytest.raises(ValueError):
        plan_rotation(0, anchor=ANCHOR)


def test_windows_are_contiguous_within_a_run():
    windows = size_windows(3)

    assert windows[0] == "size:0..250"
    assert len(set(windows)) == 3


def test_generated_query_sets_differ_between_runs(universe):
    """The end-to-end point: two runs produce genuinely different queries."""
    one = QueryGenerator(universe, windows=plan_rotation(1, anchor=ANCHOR).windows,
                         library_offset=0)
    two = QueryGenerator(universe, windows=plan_rotation(2, anchor=ANCHOR).windows,
                         library_offset=1)

    q1 = {q.query for q in one.generate(tiers=[3])}
    q2 = {q.query for q in two.generate(tiers=[3])}

    assert q1
    assert q1.isdisjoint(q2), "run 2 would replay run 1's tier-3 queries"


def test_library_rotation_changes_order_not_membership(universe):
    base = QueryGenerator(universe, windows=("w",), library_offset=0)
    rotated = QueryGenerator(universe, windows=("w",), library_offset=2)

    a = [q.library_name for q in base.generate(tiers=[3])]
    b = [q.library_name for q in rotated.generate(tiers=[3])]

    assert set(a) == set(b), "rotation must not drop a library"
    assert a != b, "rotation must change which libraries lead"


def test_tier_order_is_never_rotated(universe):
    """Tiers are ordered by measured precision; shuffling them would trade a
    real gain for cosmetic variety."""
    generator = QueryGenerator(universe, windows=("w",), library_offset=3)
    tiers = [q.discovery_tier for q in generator.generate()]

    assert tiers == sorted(tiers)


def test_fresh_batch_check_passes_for_a_rotated_run(conn, universe):
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "shared query", ["org/a"], window="w1")

    _run(conn, "run_2", "2026-02-01T00:00:00Z")
    planned = [GeneratedQuery("shared query", 3, search_window="w2")]

    check = verify_fresh_batch(conn, "run_2", planned)

    assert check.is_fresh
    assert check.novel == 1


def test_fresh_batch_check_rejects_a_replay(conn):
    """An identical query set returns GitHub's same best-match hits and records
    nothing new, which is precisely what section 7 exists to prevent."""
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "same query", ["org/a"], window="w1")

    _run(conn, "run_2", "2026-02-01T00:00:00Z")
    planned = [GeneratedQuery("same query", 3, search_window="w1")]

    with pytest.raises(FreshBatchError, match="already executed"):
        verify_fresh_batch(conn, "run_2", planned)


def test_partial_overlap_is_allowed(conn):
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "q1", ["org/a"], window="w1")

    _run(conn, "run_2", "2026-02-01T00:00:00Z")
    planned = [
        GeneratedQuery("q1", 3, search_window="w1"),
        GeneratedQuery("q2", 3, search_window="w2"),
    ]
    check = verify_fresh_batch(conn, "run_2", planned)

    assert check.is_fresh
    assert check.already_used == 1
    assert check.novel == 1


def test_the_first_run_is_always_fresh(conn):
    _run(conn, "run_1", "2026-01-01T00:00:00Z")

    check = verify_fresh_batch(conn, "run_1", [GeneratedQuery("q", 3)])

    assert check.is_fresh
    assert check.already_used == 0


def test_the_rotation_is_readable_from_the_database(conn):
    """A person must be able to inspect the database and see how run 2
    differed, without rerunning anything."""
    rotation = plan_rotation(2, anchor=ANCHOR)
    storage.create_run(conn, "run_2", started_at="2026-02-01T00:00:00Z",
                       notes=rotation.description)
    _record(conn, "run_2", "q", ["org/d"], window=rotation.windows[0])

    run = storage.get_run(conn, "run_2")
    windows = {q["search_window"] for q in storage.list_queries_for_run(conn, "run_2")}

    assert "run #2" in run["notes"]
    assert windows == {rotation.windows[0]}


# --- G. run-level counts ---------------------------------------------------


def test_run_counts_are_reported_separately(conn):
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "q1", ["org/a", "org/b"], total=75648)
    _record(conn, "run_1", "q2", ["org/b"], total=662)
    _record(conn, "run_1", "q3", [], total=0)

    stats = run_stats(conn, "run_1")

    assert stats.queries_executed == 3
    assert stats.raw_results == 3          # two hits plus one
    assert stats.unique_repositories == 2  # B counted once
    assert stats.new_candidates == 2
    assert stats.previously_seen == 0
    assert stats.zero_result_queries == 1
    assert stats.capped_queries == 1       # only the 75,648 query


def test_failed_queries_are_counted_apart_from_empty_ones(conn):
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "ok", ["org/a"], total=5)
    storage.create_discovery_query(          # never updated: it failed
        conn, run_id="run_1", discovery_source="github_code_search", query="failed")
    _record(conn, "run_1", "empty", [], total=0)

    stats = run_stats(conn, "run_1")

    assert stats.queries_executed == 2
    assert stats.queries_failed == 1
    assert stats.zero_result_queries == 1


def test_raw_results_differ_from_unique_repositories(conn):
    """The two numbers measure different things and are reported separately."""
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    _record(conn, "run_1", "q1", ["org/a"])
    _record(conn, "run_1", "q2", ["org/a"])
    _record(conn, "run_1", "q3", ["org/a"])

    stats = run_stats(conn, "run_1")

    assert stats.raw_results == 3
    assert stats.unique_repositories == 1
    assert stats.new_candidates == 1


def test_stats_for_a_run_with_nothing_recorded(conn):
    _run(conn, "run_1", "2026-01-01T00:00:00Z")
    stats = run_stats(conn, "run_1")

    assert stats.queries_executed == 0
    assert stats.raw_results == 0
    assert stats.new_candidates == 0


def test_summary_lines_cover_every_count(conn, two_runs):
    text = "\n".join(run_stats(two_runs, "run_2").summary_lines())

    for label in ["queries executed", "raw results", "unique repositories",
                  "previously seen", "new candidates", "zero-result", "capped"]:
        assert label in text


# --- H. no network ---------------------------------------------------------


def test_dedup_makes_no_network_calls():
    from pathlib import Path

    source = Path("src/dependency_map/dedup.py").read_text(encoding="utf-8")

    for forbidden in ["import requests", "urllib.request", "http.client",
                      "socket", "GitHubClient"]:
        assert forbidden not in source


def test_dedup_implements_no_later_phase_logic():
    from pathlib import Path

    source = Path("src/dependency_map/dedup.py").read_text(encoding="utf-8")

    for term in ["qualification_status", "final_score", "upsert_score",
                 "pipeline_evidence", "business_evidence"]:
        assert term not in source


def test_discovery_no_longer_defines_identity_helpers():
    """Moved to dedup.py, imported rather than duplicated."""
    from pathlib import Path

    source = Path("src/dependency_map/discovery.py").read_text(encoding="utf-8")

    assert "def normalize_repo_url" not in source
    assert "def make_candidate_id" not in source
    assert "from .dedup import" in source


def test_discovery_still_re_exports_them():
    """Existing callers keep working."""
    from dependency_map import discovery

    assert discovery.make_candidate_id("https://github.com/a/b") == \
        make_candidate_id("https://github.com/a/b")
    assert discovery.normalize_repo_url is normalize_repo_url
