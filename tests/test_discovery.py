"""The discovery engine: query generation, execution, and what gets recorded.

Every test drives a fake GitHub client or a fake transport. Nothing here
touches the network, and the integration test at the end is modelled on the
real Phase 6A measurements rather than on invented numbers.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pytest

from dependency_map import storage
from dependency_map.clients.github_client import GitHubClient
from dependency_map.discovery import (
    CO_OCCURRENCE_QUERY,
    COMPOSE_FILENAMES,
    DiscoveryEngine,
    DiscoveryError,
    GeneratedQuery,
    InvalidQuery,
    QueryGenerator,
    make_candidate_id,
    normalize_repo_url,
    size_windows,
    validate_query,
)
from dependency_map.library_universe import load_library_universe
from dependency_map.reliability import (
    GITHUB_CODE_SEARCH,
    ApiError,
    HttpResponse,
    MemoryCacheStore,
    RateLimited,
    ReliabilityPolicy,
    ReliableRequester,
)

UNIVERSE_PATH = Path("data") / "library-universe.yaml"
FAKE_TOKEN = "ghp_fake000000000000000000000000000000"
WINDOWS = ("size:0..250", "size:251..500")


@pytest.fixture(scope="module")
def universe():
    return load_library_universe(UNIVERSE_PATH)


@pytest.fixture
def generator(universe):
    return QueryGenerator(universe, windows=WINDOWS)


# --- fakes -----------------------------------------------------------------


class FakeSearchPage:
    def __init__(self, results, total_count, capped=None):
        self.results = tuple(results)
        self.total_count = total_count
        self.incomplete_results = False
        self.capped = (total_count > 1000) if capped is None else capped
        self.query = ""


class FakeResult:
    def __init__(self, full_name, rank=1, path="requirements.txt"):
        owner, _, name = full_name.partition("/")
        self.repo_full_name = full_name
        self.repo_url = f"https://github.com/{full_name}"
        self.repo_owner = owner
        self.repo_name = name
        self.path = path
        self.rank = rank
        self.evidence_url = f"https://github.com/{full_name}/blob/main/{path}"
        self.sha = "abc"
        self.excerpt = ""


class FakeClient:
    """Stands in for GitHubClient. Records every query it was asked to run."""

    def __init__(self, responses=None, default=None):
        self._responses = responses or {}
        self._default = default if default is not None else FakeSearchPage([], 0)
        self.queries: list[str] = []

    def search_code(self, query, per_page=30, page=1, use_cache=True):
        self.queries.append(query)
        outcome = self._responses.get(query, self._default)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


def hits(*names, start=1):
    return [FakeResult(n, rank=i) for i, n in enumerate(names, start)]


# --- candidate identity ----------------------------------------------------


def test_repo_url_is_normalized():
    assert normalize_repo_url("https://GitHub.com/Acme/Widget/") == \
        "https://github.com/acme/widget"


def test_normalization_strips_a_git_suffix():
    assert normalize_repo_url("https://github.com/acme/widget.git") == \
        "https://github.com/acme/widget"


def test_candidate_id_is_deterministic():
    assert make_candidate_id("https://github.com/acme/widget") == \
        make_candidate_id("https://github.com/acme/widget")


def test_candidate_id_survives_case_and_trailing_slash():
    """The same repository must resolve to the same record however a query
    happened to spell it."""
    base = make_candidate_id("https://github.com/acme/widget")

    assert make_candidate_id("https://GitHub.com/Acme/Widget") == base
    assert make_candidate_id("https://github.com/acme/widget/") == base
    assert make_candidate_id("https://github.com/acme/widget.git") == base


def test_different_repos_get_different_ids():
    assert make_candidate_id("https://github.com/a/b") != \
        make_candidate_id("https://github.com/a/c")


# --- tier assignment -------------------------------------------------------


def test_tier_one_queries_come_from_infrastructure_patterns(generator):
    queries = generator.generate(tiers=[1])

    assert queries
    assert all(q.discovery_tier == 1 for q in queries)
    assert any("gotenberg/gotenberg" in q.query for q in queries)


def test_tier_two_covers_the_five_approved_libraries(generator):
    libraries = {q.library_name for q in generator.generate(tiers=[2])}

    assert libraries == {
        "docxtemplater",
        "docxtpl (python-docx-template)",
        "Carbone.io",
        "JasperReports / Apache FOP",
        "docx-mailmerge / docxedit",
    }


def test_tier_three_covers_the_broad_manifest_libraries(generator):
    libraries = {q.library_name for q in generator.generate(tiers=[3])}

    assert "python-docx" in libraries
    assert "Apache PDFBox" in libraries
    assert "ReportLab" in libraries
    assert "docxtpl (python-docx-template)" not in libraries


def test_tiers_are_generated_in_precision_order(generator):
    tiers = [q.discovery_tier for q in generator.generate()]

    assert tiers == sorted(tiers), "tier 1 must run before tier 3"


def test_every_query_carries_its_metadata(generator):
    for q in generator.generate():
        assert q.query
        assert q.discovery_tier in (1, 2, 3)
        assert q.discovery_source == GITHUB_CODE_SEARCH


# --- infrastructure filename variants --------------------------------------


def test_compose_queries_cover_both_extensions(generator):
    gotenberg = [q.query for q in generator.generate(tiers=[1])
                 if "gotenberg/gotenberg" in q.query]

    assert any("filename:docker-compose.yml" in q for q in gotenberg)
    assert any("filename:docker-compose.yaml" in q for q in gotenberg)
    assert COMPOSE_FILENAMES == ("docker-compose.yml", "docker-compose.yaml")


def test_compose_variants_come_from_logic_not_duplicated_yaml(universe):
    """The YAML keeps one canonical pattern; the generator expands it."""
    entry = universe.by_name("Gotenberg")
    compose = [p for p in entry.infrastructure_patterns if p.detection == "compose"]

    assert len(compose) == 1
    assert compose[0].filename == "docker-compose.yml"


def test_dockerfile_patterns_are_not_expanded(generator):
    dockerfile = [q.query for q in generator.generate(tiers=[1])
                  if "filename:Dockerfile" in q.query]

    assert dockerfile
    assert not any("docker-compose" in q for q in dockerfile)


def test_subprocess_patterns_have_no_filename_anchor(generator):
    subprocess_queries = [q.query for q in generator.generate(tiers=[1])
                          if "unoconv" in q.query or "subprocess pandoc" in q.query]

    assert subprocess_queries
    assert any("filename:" not in q for q in subprocess_queries)


# --- slicing ---------------------------------------------------------------


def test_every_tier_three_query_is_sliced(generator):
    for q in generator.generate(tiers=[3]):
        assert q.search_window, f"unsliced tier-3 query: {q.query}"
        assert q.search_window in q.query


def test_tier_one_is_not_sliced(generator):
    """Measured at 662 results, comfortably inside the ceiling."""
    assert all(q.search_window is None for q in generator.generate(tiers=[1]))


def test_tier_two_is_not_sliced_by_default(generator):
    assert all(q.search_window is None for q in generator.generate(tiers=[2]))


def test_each_window_produces_its_own_query(universe):
    gen = QueryGenerator(universe, windows=WINDOWS, include_co_occurrence=False)
    python_docx = [q for q in gen.generate(tiers=[3]) if q.library_name == "python-docx"]
    windows = {q.search_window for q in python_docx}

    assert windows == set(WINDOWS)


def test_size_windows_are_contiguous_and_smallest_first():
    windows = size_windows(3)

    assert len(windows) == 3
    assert windows[0] == "size:0..250"
    assert all(w.startswith("size:") for w in windows)


def test_a_generator_with_no_windows_is_refused(universe):
    """An unsliced tier-3 query sees a fraction of its matches and reports no
    gap, which is the failure mode the experiment exposed."""
    with pytest.raises(DiscoveryError, match="at least one slicing window"):
        QueryGenerator(universe, windows=[])


# --- valid qualifier construction ------------------------------------------

def test_the_broken_reportlab_combination_is_refused():
    """The exact query that silently returned zero in the experiment."""
    with pytest.raises(InvalidQuery, match="returns zero results"):
        validate_query('"reportlab" filename:requirements.txt language:python')


@pytest.mark.parametrize("filename", ["requirements.txt", "package.json",
                                      "pom.xml", "pyproject.toml"])
def test_language_with_any_unclassified_manifest_is_refused(filename):
    with pytest.raises(InvalidQuery):
        validate_query(f'"x" filename:{filename} language:python')


def test_language_alone_is_allowed():
    validate_query("import docx language:python")  # must not raise


def test_filename_alone_is_allowed():
    validate_query('"reportlab" filename:requirements.txt')


def test_no_generated_query_pairs_language_with_a_manifest(generator):
    for q in generator.generate():
        validate_query(q.query)


def test_reportlab_query_is_corrected(generator):
    """The invalid `language:python` qualifier is gone.

    ReportLab produces queries for both requirements.txt and pyproject.toml:
    the second is what now covers the non-requirements.txt pinning that the
    set-aside import query was originally meant to catch.
    """
    reportlab = [q.query for q in generator.generate(tiers=[3])
                 if q.library_name == "ReportLab"]

    assert reportlab
    assert any("filename:requirements.txt" in q for q in reportlab)
    assert any("filename:pyproject.toml" in q for q in reportlab)
    assert not any("language:python" in q for q in reportlab)


def test_csproj_uses_an_extension_qualifier(generator):
    """filename: does not handle a glob, so *.csproj becomes extension:csproj."""
    csproj = [q.query for q in generator.generate(tiers=[3]) if "csproj" in q.query]

    assert csproj
    assert all("extension:csproj" in q for q in csproj)
    assert not any("filename:*.csproj" in q for q in csproj)


# --- excluded and demoted queries ------------------------------------------


def test_the_bare_import_query_is_never_generated(generator):
    """Measured at 690,176 results, set aside in search-strategy.md 4.4."""
    for q in generator.generate():
        assert "import docx" not in q.query


def test_co_occurrence_is_a_supplementary_tier_three_probe(generator):
    co = [q for q in generator.generate() if q.query.startswith(CO_OCCURRENCE_QUERY)]

    assert co
    assert all(q.discovery_tier == 3 for q in co)
    assert all(q.library_name is None for q in co), \
        "a query spanning two libraries must not claim either"
    assert all(q.search_window for q in co)


def test_co_occurrence_can_be_disabled(universe):
    gen = QueryGenerator(universe, windows=WINDOWS, include_co_occurrence=False)

    assert not any(q.query.startswith(CO_OCCURRENCE_QUERY) for q in gen.generate())


# --- query persistence -----------------------------------------------------


def _engine(conn, client, universe, **kw):
    return DiscoveryEngine(
        conn, client, QueryGenerator(universe, windows=WINDOWS[:1]), **kw
    )


def test_zero_result_query_is_still_persisted(conn, run_id, universe):
    client = FakeClient(default=FakeSearchPage([], 0))
    _engine(conn, client, universe).run(run_id, tiers=[1])

    rows = storage.list_queries_for_run(conn, run_id)
    assert rows
    assert all(r["total_count"] == 0 for r in rows)
    assert all(r["returned_count"] == 0 for r in rows)
    assert all(r["capped"] == 0 for r in rows)


def test_total_count_is_persisted(conn, run_id, universe):
    client = FakeClient(default=FakeSearchPage(hits("a/b"), 662))
    _engine(conn, client, universe).run(run_id, tiers=[1])

    row = storage.list_queries_for_run(conn, run_id)[0]
    assert row["total_count"] == 662
    assert row["returned_count"] == 1


def test_capped_is_derived_from_total_count(conn, run_id, universe):
    client = FakeClient(default=FakeSearchPage(hits("a/b"), 75648))
    _engine(conn, client, universe).run(run_id, tiers=[1])

    assert all(r["capped"] == 1 for r in storage.list_queries_for_run(conn, run_id))


def test_uncapped_below_the_ceiling(conn, run_id, universe):
    client = FakeClient(default=FakeSearchPage(hits("a/b"), 662))
    _engine(conn, client, universe).run(run_id, tiers=[1])

    assert all(r["capped"] == 0 for r in storage.list_queries_for_run(conn, run_id))


def test_returned_count_reflects_raw_api_results(conn, run_id, universe):
    """Raw results, deliberately allowed to exceed recorded hits."""
    client = FakeClient(default=FakeSearchPage(hits("a/b", "a/b", "c/d"), 500))
    _engine(conn, client, universe).run(run_id, tiers=[1])

    row = storage.list_queries_for_run(conn, run_id)[0]
    assert row["returned_count"] == 3
    assert len(storage.list_discovery_evidence_for_query(conn, row["query_id"])) == 2


def test_query_metadata_is_persisted(conn, run_id, universe):
    client = FakeClient(default=FakeSearchPage([], 0))
    _engine(conn, client, universe).run(run_id, tiers=[3])

    rows = storage.list_queries_for_run(conn, run_id)
    assert all(r["discovery_tier"] == 3 for r in rows)
    assert all(r["search_window"] for r in rows)
    assert all(r["discovery_source"] == "github_code_search" for r in rows)


def test_rerunning_the_same_query_set_does_not_duplicate(conn, run_id, universe):
    client = FakeClient(default=FakeSearchPage(hits("a/b"), 10))
    engine = _engine(conn, client, universe)

    engine.run(run_id, tiers=[1])
    first = storage.count_queries_for_run(conn, run_id)
    engine.run(run_id, tiers=[1])

    assert storage.count_queries_for_run(conn, run_id) == first


# --- candidates ------------------------------------------------------------


def test_candidates_are_created_from_hits(conn, run_id, universe):
    client = FakeClient(default=FakeSearchPage(hits("acme/widget"), 5))
    _engine(conn, client, universe).run(run_id, tiers=[1])

    candidate = storage.get_candidate_by_repo_url(conn, "https://github.com/acme/widget")
    assert candidate is not None
    assert candidate["repo_owner"] == "acme"
    assert candidate["repo_name"] == "widget"
    assert candidate["first_seen_run_id"] == run_id


def test_one_repository_across_two_queries_is_one_candidate(conn, run_id, universe):
    """Deduplication: one candidate row, one discovery_evidence row per query,
    so query overlap stays visible."""
    client = FakeClient(default=FakeSearchPage(hits("acme/widget"), 5))
    _engine(conn, client, universe).run(run_id, tiers=[1])

    candidate_id = make_candidate_id("https://github.com/acme/widget")
    queries = storage.list_queries_for_run(conn, run_id)
    evidence = storage.list_discovery_evidence_for_candidate(conn, candidate_id)

    assert storage.count_candidates(conn) == 1
    assert len(queries) > 1
    assert len(evidence) == len(queries)


def test_no_business_or_pipeline_evidence_is_written(conn, run_id, universe):
    """Those belong to phase 8, reading what discovery recorded."""
    client = FakeClient(default=FakeSearchPage(hits("acme/widget"), 5))
    _engine(conn, client, universe).run(run_id, tiers=[1])

    candidate_id = make_candidate_id("https://github.com/acme/widget")
    assert storage.get_pipeline_evidence(conn, candidate_id) is None
    assert storage.get_business_evidence(conn, candidate_id) is None
    assert storage.get_qualification(conn, candidate_id) is None
    assert storage.get_score(conn, candidate_id) is None


def test_result_rank_is_recorded(conn, run_id, universe):
    client = FakeClient(default=FakeSearchPage(hits("a/one", "b/two"), 5))
    _engine(conn, client, universe).run(run_id, tiers=[1])

    query_id = storage.list_queries_for_run(conn, run_id)[0]["query_id"]
    ranks = [r["discovery_result_rank"]
             for r in storage.list_discovery_evidence_for_query(conn, query_id)]

    assert sorted(ranks) == [1, 2]


# --- error handling --------------------------------------------------------


def test_a_failed_query_is_recorded_and_the_run_continues(conn, run_id, universe):
    """A failure leaves total_count null, which distinguishes "this failed"
    from "this genuinely returned nothing"."""
    gen = QueryGenerator(universe, windows=WINDOWS[:1])
    queries = gen.generate(tiers=[1])
    responses = {queries[0].query: ApiError(500, "https://x", "boom")}
    client = FakeClient(responses, default=FakeSearchPage(hits("a/b"), 5))

    report = DiscoveryEngine(conn, client, gen).run(run_id, tiers=[1])

    assert report.queries_failed == 1
    assert report.queries_executed == len(queries) - 1

    failed = [r for r in storage.list_queries_for_run(conn, run_id)
              if r["total_count"] is None]
    assert len(failed) == 1
    assert failed[0]["returned_count"] == 0


def test_a_failure_does_not_corrupt_successful_records(conn, run_id, universe):
    gen = QueryGenerator(universe, windows=WINDOWS[:1])
    queries = gen.generate(tiers=[1])
    responses = {queries[0].query: ApiError(500, "https://x", "boom")}
    client = FakeClient(responses, default=FakeSearchPage(hits("a/b"), 42))

    DiscoveryEngine(conn, client, gen).run(run_id, tiers=[1])

    succeeded = [r for r in storage.list_queries_for_run(conn, run_id)
                 if r["total_count"] is not None]
    assert succeeded
    assert all(r["total_count"] == 42 for r in succeeded)


def test_a_rate_limit_stops_the_run(conn, run_id, universe):
    """Systemic, not incidental: continuing would burn the run producing
    nothing."""
    client = FakeClient(default=RateLimited("budget exhausted for 40 minutes"))

    with pytest.raises(DiscoveryError, match="Discovery stopped"):
        _engine(conn, client, universe).run(run_id, tiers=[1])


def test_repeated_failures_stop_the_run(conn, run_id, universe):
    client = FakeClient(default=ApiError(500, "https://x", "boom"))

    with pytest.raises(DiscoveryError, match="looks systemic"):
        _engine(conn, client, universe, max_consecutive_failures=2).run(run_id, tiers=[1])


def test_failures_are_reported_not_swallowed(conn, run_id, universe):
    gen = QueryGenerator(universe, windows=WINDOWS[:1])
    queries = gen.generate(tiers=[1])
    responses = {queries[0].query: ApiError(422, "https://x", "bad query")}
    client = FakeClient(responses, default=FakeSearchPage([], 0))

    report = DiscoveryEngine(conn, client, gen).run(run_id, tiers=[1])

    assert len(report.failures) == 1
    assert "bad query" in report.failures[0][1]


# --- reliability layer usage -----------------------------------------------


def test_discovery_makes_no_raw_http_calls():
    """All pacing, retry and caching live in the reliability layer. A direct
    request here would bypass the 10-per-minute code-search budget."""
    source = Path("src/dependency_map/discovery.py").read_text(encoding="utf-8")

    for forbidden in ["import requests", "urllib.request", "http.client",
                      "requests.get", "requests.post", "socket"]:
        assert forbidden not in source, f"{forbidden} bypasses the reliability layer"


def test_discovery_goes_through_the_github_client(conn, run_id, universe):
    """Verified against a real GitHubClient over a fake transport, so the
    reliability layer is genuinely exercised rather than mocked away."""
    calls = []

    class Transport:
        def request(self, method, url, *, params=None, headers=None, timeout=30.0):
            calls.append((url, dict(params or {})))
            return HttpResponse(
                status=200, headers={},
                text=json.dumps({"total_count": 1, "items": [{
                    "path": "requirements.txt", "sha": "a",
                    "html_url": "https://github.com/acme/widget/blob/main/requirements.txt",
                    "repository": {"full_name": "acme/widget",
                                   "html_url": "https://github.com/acme/widget"},
                }]}),
                url=url,
            )

    policy = ReliabilityPolicy(intervals={GITHUB_CODE_SEARCH: 0.0}, max_attempts=1)
    requester = ReliableRequester(
        Transport(), policy, cache=MemoryCacheStore(), sleep=lambda s: None
    )
    client = GitHubClient(requester, token=FAKE_TOKEN)

    DiscoveryEngine(
        conn, client, QueryGenerator(universe, windows=WINDOWS[:1])
    ).run(run_id, tiers=[1], limit=1)

    assert calls
    assert calls[0][0].endswith("/search/code")
    assert storage.count_candidates(conn) == 1


def test_discovery_creates_no_qualification_or_scoring(conn):
    """Phase 7+ functionality must not leak in."""
    source = Path("src/dependency_map/discovery.py").read_text(encoding="utf-8")

    for term in ["qualification_status", "final_score", "def qualify",
                 "raw_weighted_score", "upsert_score", "upsert_qualification"]:
        assert term not in source


# --- integration, modelled on the Phase 6A experiment ----------------------


def test_integration_mirrors_the_real_experiment(conn, run_id, universe):
    """A pass over four queries shaped like the measured Phase 6A results.

    Covers a high-precision uncapped query, a noisy capped one, a zero-result
    one, and a repository surfaced by two different queries.
    """
    gotenberg = GeneratedQuery(
        query='"gotenberg/gotenberg" filename:docker-compose.yml',
        discovery_tier=1, library_name="Gotenberg",
    )
    python_docx = GeneratedQuery(
        query='"python-docx" filename:requirements.txt size:0..250',
        discovery_tier=3, library_name="python-docx",
        search_window="size:0..250",
    )
    broken = GeneratedQuery(
        query='"reportlab" filename:requirements.txt size:0..250',
        discovery_tier=3, library_name="ReportLab",
        search_window="size:0..250",
    )
    overlap = GeneratedQuery(
        query=f"{CO_OCCURRENCE_QUERY} size:0..250",
        discovery_tier=3, library_name=None,
        search_window="size:0..250",
    )

    class FixedGenerator(QueryGenerator):
        def generate(self, tiers=(1, 2, 3)):
            return [gotenberg, python_docx, broken, overlap]

    client = FakeClient({
        gotenberg.query: FakeSearchPage(hits("bigcapitalhq/bigcapital",
                                             "solidtime-io/solidtime"), 662),
        python_docx.query: FakeSearchPage(hits("sambanova/ai-starter-kit",
                                               "UKGovernmentBEIS/inspect_evals"), 75648),
        broken.query: FakeSearchPage([], 0),
        # inspect_evals also appeared in the co-occurrence query, as measured
        overlap.query: FakeSearchPage(hits("UKGovernmentBEIS/inspect_evals"), 11552),
    })

    engine = DiscoveryEngine(
        conn, client, FixedGenerator(universe, windows=WINDOWS[:1])
    )
    report = engine.run(run_id)

    assert report.queries_executed == 4
    assert report.zero_result_queries == 1
    assert report.capped_queries == 2
    assert report.total_raw_hits == 5
    assert report.unique_candidates == 4  # inspect_evals counted once

    rows = {r["query"]: r for r in storage.list_queries_for_run(conn, run_id)}

    # uncapped, high precision
    assert rows[gotenberg.query]["total_count"] == 662
    assert rows[gotenberg.query]["capped"] == 0
    assert rows[gotenberg.query]["search_window"] is None

    # capped, noisy
    assert rows[python_docx.query]["total_count"] == 75648
    assert rows[python_docx.query]["capped"] == 1
    assert rows[python_docx.query]["search_window"] == "size:0..250"

    # zero result, still recorded
    assert rows[broken.query]["total_count"] == 0
    assert rows[broken.query]["returned_count"] == 0
    assert storage.list_discovery_evidence_for_query(
        conn, rows[broken.query]["query_id"]) == []

    # the same repository from two queries: one candidate, two hits
    shared = make_candidate_id("https://github.com/UKGovernmentBEIS/inspect_evals")
    evidence = storage.list_discovery_evidence_for_candidate(conn, shared)
    assert len(evidence) == 2
    assert {e["query"] for e in evidence} == {python_docx.query, overlap.query}
    assert storage.count_candidates(conn) == 4


def test_integration_records_the_coverage_gap(conn, run_id, universe):
    """The reason the query table exists: the report must be able to say
    "10 of 75,648 inspected" rather than implying coverage it never had."""
    query = GeneratedQuery(
        query='"python-docx" filename:requirements.txt size:0..250',
        discovery_tier=3, library_name="python-docx",
        search_window="size:0..250",
    )

    class FixedGenerator(QueryGenerator):
        def generate(self, tiers=(1, 2, 3)):
            return [query]

    client = FakeClient({query.query: FakeSearchPage(hits(*[f"o{i}/r{i}" for i in
                                                            range(10)]), 75648)})
    DiscoveryEngine(conn, client, FixedGenerator(universe, windows=WINDOWS[:1])).run(run_id)

    row = storage.list_queries_for_run(conn, run_id)[0]
    assert row["returned_count"] == 10
    assert row["total_count"] == 75648
    assert row["capped"] == 1
    coverage = row["returned_count"] / row["total_count"]
    assert coverage < 0.001
