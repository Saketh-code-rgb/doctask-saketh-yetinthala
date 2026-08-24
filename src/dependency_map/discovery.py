"""Discovery engine: generate queries, run them, record what came back.

This component records hits and makes no judgment about them
(TECHNICAL_DESIGN.md section 7). A repository that is obviously a tutorial, a
library's own tooling, or an AI project with an incidental document dependency
all enter discovery exactly like anything else. Deciding what they are is
qualification's job, working from stored evidence in a later phase.

Queries are generated in three tiers ordered by *measured* precision rather
than by library popularity, following the Phase 6A experiment recorded in
PROGRESS.md:

    tier 1  infrastructure       Gotenberg measured 662 results, uncapped
    tier 2  template generation  docxtpl measured 1,852, docxtemplater 3,256
    tier 3  broad manifest       python-docx 75,648, reportlab 90,240, capped

Tier membership is read from `discovery_tier` in the library universe, so it
stays reviewable data rather than a second library list living in code.

Three rules are enforced here rather than left to care: a tier-3 query without
a slice is refused, because six of eight trial queries exceeded GitHub's
1,000-result ceiling and an unsliced query silently sees a fraction of its
matches; a query combining `filename:` on a manifest with `language:` is
refused outright, because that combination returns zero rather than narrowing;
and a query carrying a repository-search-only qualifier such as `pushed:` is
refused, because code search matches it as literal text and returns a
truthful-looking zero. The third rule exists because run 1 lost 220 of its 237
queries to it.

Work is committed one query at a time. A query's record, the candidates it
surfaced and the evidence rows linking them are one unit; once committed, an
interruption cannot take them back. Before run 1 the whole stage shared a
single transaction, so a failure in the twenty-sixth minute discarded all
twenty-six minutes of API budget.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Iterable, Sequence

from . import storage
from .clients.github_client import GitHubClient
from .dedup import make_candidate_id, normalize_repo_url, size_windows
from .library_universe import (
    TIER_BROAD_MANIFEST,
    TIER_INFRASTRUCTURE,
    TIER_TEMPLATE_GENERATION,
    LibraryEntry,
    LibraryUniverse,
)
from .reliability import ApiError, RateLimited, ReliabilityError, RetriesExhausted

logger = logging.getLogger(__name__)

GITHUB_CODE_SEARCH = "github_code_search"

#: Compose files appear under both extensions. Handled here rather than by
#: duplicating a library-universe entry per extension.
COMPOSE_FILENAMES = ("docker-compose.yml", "docker-compose.yaml")

#: Files GitHub does not classify under a programming language. Combining
#: `filename:` on one of these with `language:` returns zero results, which is
#: how the ReportLab query in search-strategy.md came to be silently broken.
UNCLASSIFIED_FILENAMES = frozenset(
    {
        "requirements.txt",
        "package.json",
        "pom.xml",
        "build.gradle",
        "packages.config",
        "pyproject.toml",
        "dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
    }
)

#: Qualifiers GitHub implements for *repository* search and not for code
#: search. Code search does not reject them; it treats them as literal text to
#: find inside a file, so a query carrying one matches nothing and reports a
#: truthful-looking zero.
#:
#: This is not hypothetical. Run 1 (2026-08-20) generated 220 tier-3 queries
#: sliced with `pushed:` and every one returned zero, wasting 93% of the query
#: budget. Measured on the same query with and without the qualifier:
#: 75,648 matches became 0. `fork:` is here for a different reason: code search
#: rejects it outright with HTTP 422.
REPOSITORY_ONLY_QUALIFIERS = frozenset(
    {
        "pushed",
        "created",
        "stars",
        "forks",
        "fork",
        "topic",
        "topics",
        "license",
        "archived",
        "mirror",
        "is",
        "followers",
        "good-first-issues",
        "help-wanted-issues",
    }
)

#: The supplementary co-occurrence probe from search-strategy.md section 4.3.
#: Retained, but no longer treated as a high-confidence primitive: measured at
#: 11,552 results dominated by AI projects and student work.
CO_OCCURRENCE_QUERY = '"python-docx" "reportlab" filename:requirements.txt'


class DiscoveryError(Exception):
    """Discovery could not continue."""


class InvalidQuery(DiscoveryError):
    """A generated query would be malformed or is known to return nothing."""


# Candidate identity and slicing live in dedup.py, which owns deduplication and
# the fresh-batch rotation. Re-exported here because discovery is where callers
# reach for them.
__all__ = [
    "CO_OCCURRENCE_QUERY",
    "COMPOSE_FILENAMES",
    "DiscoveryEngine",
    "DiscoveryError",
    "DiscoveryReport",
    "GeneratedQuery",
    "InvalidQuery",
    "QueryGenerator",
    "make_candidate_id",
    "normalize_repo_url",
    "size_windows",
    "validate_query",
]


# --- query generation ------------------------------------------------------


@dataclass(frozen=True)
class GeneratedQuery:
    """One query to execute, with the metadata its record will carry."""

    query: str
    discovery_tier: int
    discovery_source: str = GITHUB_CODE_SEARCH
    library_name: str | None = None
    search_window: str | None = None


def _filename_qualifier(manifest: str) -> str:
    """Build a valid qualifier for a manifest filename.

    `filename:` does not handle a glob, so a pattern like `*.csproj` becomes an
    `extension:` qualifier instead. Emitting `filename:*.csproj` would be
    accepted by the API and quietly match nothing useful.
    """
    if manifest.startswith("*."):
        return f"extension:{manifest[2:]}"
    return f"filename:{manifest}"


def validate_query(query: str) -> None:
    """Refuse query shapes known to be broken.

    Two failures are guarded here, both of which cost the project a silent
    zero rather than an error:

    `"reportlab" filename:requirements.txt language:python` returns no results,
    because GitHub classifies a requirements file as text rather than Python,
    so the two qualifiers are mutually exclusive rather than complementary.

    `"python-docx" filename:requirements.txt pushed:2026-05-23..2026-08-21`
    also returns no results, because `pushed:` belongs to repository search.
    Code search matches it as literal text. Run 1 lost 220 of 237 queries to
    exactly this, so the check is a hard failure rather than a warning.
    """
    for token in query.split():
        qualifier, separator, value = token.partition(":")
        if not separator:
            continue
        if qualifier.lower() in REPOSITORY_ONLY_QUALIFIERS:
            raise InvalidQuery(
                f"Query uses {qualifier}:, which GitHub implements for "
                f"repository search but not for code search. Code search "
                f"matches it as literal text and returns zero rather than "
                f"failing, so this must never reach the API: {query!r}"
            )

    if "language:" not in query:
        return
    for token in query.split():
        if token.startswith("filename:"):
            filename = token[len("filename:") :].strip('"').lower()
            if filename in UNCLASSIFIED_FILENAMES:
                raise InvalidQuery(
                    f"Query combines filename:{filename} with a language "
                    f"qualifier, which returns zero results because GitHub does "
                    f"not classify that file under a language: {query!r}"
                )


class QueryGenerator:
    """Turns library-universe entries into the tiered query set."""

    def __init__(
        self,
        universe: LibraryUniverse,
        *,
        windows: Sequence[str] | None = None,
        include_co_occurrence: bool = True,
        library_offset: int = 0,
    ) -> None:
        self._universe = universe
        self._windows = tuple(windows) if windows is not None else size_windows()
        self._include_co_occurrence = include_co_occurrence
        self._library_offset = library_offset
        if not self._windows:
            raise DiscoveryError(
                "Tier-3 queries require at least one slicing window: an unsliced "
                "broad query sees a fraction of its matches and reports no gap."
            )

    def _ordered(self, tier: int) -> tuple[LibraryEntry, ...]:
        """Entries for a tier, rotated by the run's library offset.

        Rotation happens *within* a tier, never across tiers. Tier order is
        precision order, established by measurement, and shuffling it would
        trade a real gain for cosmetic variety. Rotating inside a tier means a
        run cut short by budget doesn't always spend it on the same libraries.
        """
        entries = self._universe.by_tier(tier)
        if not entries or not self._library_offset:
            return entries
        offset = self._library_offset % len(entries)
        return entries[offset:] + entries[:offset]

    def generate(self, tiers: Iterable[int] = (1, 2, 3)) -> list[GeneratedQuery]:
        """Every query to run, in tier order.

        Tier order is precision order, so a run cut short by budget spends what
        it had on the queries most likely to be worth it.
        """
        wanted = set(tiers)
        queries: list[GeneratedQuery] = []

        for tier, builder in (
            (TIER_INFRASTRUCTURE, self._infrastructure_queries),
            (TIER_TEMPLATE_GENERATION, self._template_queries),
            (TIER_BROAD_MANIFEST, self._manifest_queries),
        ):
            if tier not in wanted:
                continue
            for entry in self._ordered(tier):
                queries.extend(builder(entry))

        if self._include_co_occurrence and TIER_BROAD_MANIFEST in wanted:
            queries.extend(self._co_occurrence_queries())

        for generated in queries:
            validate_query(generated.query)
        return queries

    def _infrastructure_queries(self, entry: LibraryEntry) -> list[GeneratedQuery]:
        """Tier 1. The signal lives in a Dockerfile or compose file.

        No slicing: the one tier-1 query measured in the experiment returned
        662 results, comfortably inside the ceiling and fully enumerable.
        """
        out: list[GeneratedQuery] = []
        for pattern in entry.infrastructure_patterns:
            filenames: tuple[str, ...]
            if pattern.detection == "compose":
                filenames = COMPOSE_FILENAMES
            elif pattern.filename:
                filenames = (pattern.filename,)
            else:
                # A subprocess call has no filename to anchor to.
                out.append(
                    GeneratedQuery(
                        query=f'"{pattern.pattern}"',
                        discovery_tier=TIER_INFRASTRUCTURE,
                        library_name=entry.library_name,
                    )
                )
                continue
            for filename in filenames:
                out.append(
                    GeneratedQuery(
                        query=f'"{pattern.pattern}" filename:{filename}',
                        discovery_tier=TIER_INFRASTRUCTURE,
                        library_name=entry.library_name,
                    )
                )
        return out

    def _template_queries(self, entry: LibraryEntry) -> list[GeneratedQuery]:
        """Tier 2. Measured under the ceiling, so unsliced by default."""
        return [
            GeneratedQuery(
                query=f'"{package}" {_filename_qualifier(manifest)}',
                discovery_tier=TIER_TEMPLATE_GENERATION,
                library_name=entry.library_name,
            )
            for package in entry.package_names[:1]
            for manifest in entry.manifest_filenames
        ]

    def _manifest_queries(self, entry: LibraryEntry) -> list[GeneratedQuery]:
        """Tier 3. Always sliced, because every tier-3 query measured in the
        experiment exceeded what pagination can reach.

        The slice is a `size:` byte range. It replaced a `pushed:` date window
        after run 1, where the date form returned zero for all 220 queries
        because code search does not implement that qualifier. Size is the
        equivalent partition that code search does support: every file has one,
        the buckets are contiguous, and nothing falls outside them.
        """
        return [
            GeneratedQuery(
                query=f'"{package}" {_filename_qualifier(manifest)} {window}',
                discovery_tier=TIER_BROAD_MANIFEST,
                library_name=entry.library_name,
                search_window=window,
            )
            for package in entry.package_names[:1]
            for manifest in entry.manifest_filenames
            for window in self._windows
        ]

    def _co_occurrence_queries(self) -> list[GeneratedQuery]:
        """A supplementary probe, not a primary signal.

        library_name stays null: the query deliberately spans two libraries and
        attributing it to either would be a fiction.
        """
        return [
            GeneratedQuery(
                query=f"{CO_OCCURRENCE_QUERY} {window}",
                discovery_tier=TIER_BROAD_MANIFEST,
                library_name=None,
                search_window=window,
            )
            for window in self._windows
        ]


# --- the engine ------------------------------------------------------------


@dataclass
class DiscoveryReport:
    """What a discovery pass did. Counts only, no judgment."""

    run_id: str
    queries_executed: int = 0
    queries_failed: int = 0
    queries_skipped: int = 0
    zero_result_queries: int = 0
    capped_queries: int = 0
    total_raw_hits: int = 0
    unique_candidates: int = 0
    new_candidates: int = 0
    failures: list[tuple[str, str]] = field(default_factory=list)

    def summary_lines(self) -> list[str]:
        return [
            f"run              {self.run_id}",
            f"queries executed {self.queries_executed}",
            f"queries failed   {self.queries_failed}",
            f"queries skipped  {self.queries_skipped}",
            f"zero-result      {self.zero_result_queries}",
            f"capped           {self.capped_queries}",
            f"raw hits         {self.total_raw_hits}",
            f"unique candidates{self.unique_candidates:>4}",
            f"new candidates   {self.new_candidates}",
        ]


class DiscoveryEngine:
    """Runs the query set and records everything it returns.

    Every call goes through the supplied GitHubClient, which owns pacing,
    retries, backoff and caching. Nothing here issues HTTP directly, so the
    10-requests-per-minute code-search budget is respected by construction
    rather than by remembering to.
    """

    def __init__(
        self,
        connection,
        client: GitHubClient,
        generator: QueryGenerator,
        *,
        per_page: int = 30,
        max_consecutive_failures: int = 5,
    ) -> None:
        self._conn = connection
        self._client = client
        self._generator = generator
        self._per_page = per_page
        self._max_consecutive_failures = max_consecutive_failures

    def run(
        self,
        run_id: str,
        *,
        tiers: Iterable[int] = (1, 2, 3),
        limit: int | None = None,
    ) -> DiscoveryReport:
        queries = self._generator.generate(tiers)
        if limit is not None:
            queries = queries[:limit]

        report = DiscoveryReport(run_id=run_id)
        already_known = storage.all_discovered_candidate_ids(self._conn)
        seen_this_run: set[str] = set()
        consecutive_failures = 0

        # Resume, rather than replay. A query already answered for this run is
        # skipped before any budget is spent on it, and skipping it here also
        # protects its stored result: create_discovery_query upserts, so
        # recreating the row would overwrite a real total_count with null.
        completed = storage.completed_query_ids(self._conn, run_id)

        for generated in queries:
            query_id = storage.make_query_id(
                run_id, generated.query, generated.search_window
            )
            if query_id in completed:
                report.queries_skipped += 1
                continue

            storage.create_discovery_query(
                self._conn,
                run_id=run_id,
                discovery_source=generated.discovery_source,
                query=generated.query,
                query_id=query_id,
                library_name=generated.library_name,
                discovery_tier=generated.discovery_tier,
                search_window=generated.search_window,
            )

            try:
                page = self._client.search_code(
                    generated.query, per_page=self._per_page
                )
            except RateLimited as exc:
                # Systemic: the budget is gone for long enough that continuing
                # would burn the rest of the run producing nothing.
                logger.error("stopping run %s: %s", run_id, exc)
                report.failures.append((generated.query, str(exc)))
                report.queries_failed += 1
                self._conn.commit()
                raise DiscoveryError(
                    f"Discovery stopped after {report.queries_executed} queries: {exc}"
                ) from exc
            except (ApiError, RetriesExhausted, ReliabilityError) as exc:
                # Per-query: leave total_count null, which distinguishes "this
                # failed" from "this genuinely returned nothing", and means a
                # resumed run retries this query rather than skipping it.
                logger.warning("query failed: %s (%s)", generated.query, exc)
                report.failures.append((generated.query, str(exc)))
                report.queries_failed += 1
                consecutive_failures += 1
                self._conn.commit()
                if consecutive_failures >= self._max_consecutive_failures:
                    raise DiscoveryError(
                        f"{consecutive_failures} queries failed in a row, which "
                        f"looks systemic rather than incidental. Stopping."
                    ) from exc
                continue

            consecutive_failures = 0
            report.queries_executed += 1
            report.total_raw_hits += len(page.results)

            storage.update_query_results(
                self._conn,
                query_id,
                total_count=page.total_count,
                returned_count=len(page.results),
            )
            if page.total_count == 0:
                report.zero_result_queries += 1
            if page.capped:
                report.capped_queries += 1

            for result in page.results:
                candidate_id = self._record_candidate(result, run_id)
                if candidate_id not in already_known:
                    already_known.add(candidate_id)
                    report.new_candidates += 1
                seen_this_run.add(candidate_id)

                storage.insert_discovery_evidence(
                    self._conn,
                    query_id=query_id,
                    candidate_id=candidate_id,
                    discovery_result_rank=result.rank,
                )

            # One query, its candidates and its evidence rows are one unit of
            # work. Committing here is what makes the stage resumable: an
            # interruption after this point cannot undo what the query cost.
            self._conn.commit()

        report.unique_candidates = len(seen_this_run)
        return report

    def _record_candidate(self, result, run_id: str) -> str:
        """Create the candidate if this repository hasn't been seen before.

        Only identity is stored. Pipeline and business evidence belong to the
        evidence collector in phase 8, which reads what discovery recorded
        rather than duplicating its calls.
        """
        candidate_id = make_candidate_id(result.repo_url)
        storage.insert_candidate_if_new(
            self._conn,
            candidate_id=candidate_id,
            repo_url=normalize_repo_url(result.repo_url),
            repo_owner=result.repo_owner,
            repo_name=result.repo_name,
            first_seen_run_id=run_id,
        )
        return candidate_id
