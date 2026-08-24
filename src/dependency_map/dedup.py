"""Deduplication, cross-run tracking, and the fresh-batch mechanism.

Three related jobs live here, all of them pure functions over stored data with
no network access:

**Identity.** A repository must resolve to the same candidate however a query
happened to spell its URL, so the same repo found by six queries across two
runs is one row in `candidates` and six rows in `discovery_evidence`.

**Cross-run classification.** Whether a candidate is new to this run or was
already surfaced by an earlier one. A repeat sighting is recorded, never
suppressed: it is evidence that a query or slice surfaced that repository
again, which is exactly what makes the fresh-batch requirement checkable.

**Rotation.** SEARCH_STRATEGY.md section 7 requires Run 2 to surface candidates
Run 1 did not, and GitHub's best-match sort returns the same top hits for an
identical query every time. So a fresh batch means changing the query, not
rerunning it. The rotation here is deterministic rather than random: a run's
plan is a pure function of its index, and the slice it actually used is
recorded per query in `discovery_queries.search_window`, so anyone can read the
database and see precisely how Run 2 differed from Run 1.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Sequence
from urllib.parse import urlsplit, urlunsplit

from . import storage

#: How many slices each run covers before the next run moves past them.
WINDOWS_PER_RUN = 4

#: Every size bucket, in bytes, smallest first. Contiguous and open-ended at
#: the top, so a file falls in exactly one of them and no file falls outside.
#:
#: File size replaced the date walk after the first live run. `pushed:` is a
#: *repository* search qualifier; GitHub code search does not implement it and
#: treats it as literal text to match, so all 220 sliced tier-3 queries in run
#: 1 returned zero. Measured 2026-08-20 on
#: `"python-docx" filename:requirements.txt` (75,648 unsliced):
#: `size:0..500` -> 46,848, `size:500..2000` -> 19,872, `size:>2000` -> 12,352.
#: The parts sum to about the whole, which is what makes this a partition
#: rather than a filter. See SEARCH_STRATEGY.md section 4.5.
SIZE_BUCKETS: tuple[str, ...] = (
    "size:0..250",
    "size:251..500",
    "size:501..1000",
    "size:1001..2000",
    "size:2001..4000",
    "size:4001..8000",
    "size:8001..16000",
    "size:>16000",
)


class FreshBatchError(Exception):
    """A run's query set would replay an earlier run."""


# --- identity --------------------------------------------------------------


def normalize_repo_url(repo_url: str) -> str:
    """Canonical form of a repository URL.

    Deliberately conservative. GitHub owner and repository names are
    case-insensitive for resolution, so lowercasing them is safe and collapses
    real duplicates. Anything that could distinguish two genuinely different
    repositories is left alone rather than normalised away, since a collision
    here would silently merge two companies into one candidate, which is far
    worse than carrying a duplicate.

    Handles: scheme and host case, a trailing slash, a `.git` suffix, a `www.`
    host prefix, and query strings or fragments that don't identify a
    repository.
    """
    parts = urlsplit(repo_url.strip())

    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]

    path = parts.path.rstrip("/")
    if path.lower().endswith(".git"):
        path = path[: -len(".git")]

    return urlunsplit((parts.scheme.lower(), host, path.lower(), "", ""))


def make_candidate_id(repo_url: str) -> str:
    """Deterministic id from the normalized URL.

    Stable across queries, slices and runs, which is what lets the same
    repository resolve to one candidate no matter how often it resurfaces.
    """
    digest = hashlib.sha256(normalize_repo_url(repo_url).encode("utf-8")).hexdigest()
    return f"c_{digest[:16]}"


# --- slicing ---------------------------------------------------------------


def size_windows(
    count: int = WINDOWS_PER_RUN,
    *,
    skip: int = 0,
) -> tuple[str, ...]:
    """Contiguous file-size slices, smallest first.

    `skip` advances the whole set further up the bucket pool, which is what
    makes one run's slices disjoint from another's. Size is the most generally
    applicable axis code search actually supports: it partitions results
    without assuming anything about their content, and every file has exactly
    one size, so the slices neither overlap nor leave a gap.

    The pool is finite, unlike a date walk that can keep marching backwards, so
    the buckets wrap once every run has used them. With eight buckets and four
    per run, runs 1 and 2 are fully disjoint and run 3 begins reusing run 1's
    slices. `verify_fresh_batch` is what catches that, and SEARCH_STRATEGY.md
    section 4.5 records it as a known limit rather than a solved problem.
    """
    if count < 1:
        raise ValueError(f"count must be at least 1, got {count}")
    start = skip % len(SIZE_BUCKETS)
    doubled = SIZE_BUCKETS + SIZE_BUCKETS
    return tuple(doubled[start : start + count][:count])


# --- rotation --------------------------------------------------------------


@dataclass(frozen=True)
class RotationPlan:
    """How one run's query set differs from every earlier run's.

    Deterministic by construction: given the same run index and anchor date,
    the plan is identical. Nothing here is randomised to manufacture a
    difference.
    """

    run_index: int
    windows: tuple[str, ...]
    library_offset: int
    anchor: date

    @property
    def description(self) -> str:
        """A one-line summary, stored in `runs.notes` so the rotation is
        legible without reconstructing it."""
        return (
            f"run #{self.run_index}: "
            f"size slices {self.windows[0].removeprefix('size:')} "
            f"through {self.windows[-1].removeprefix('size:')}, "
            f"library order rotated by {self.library_offset}"
        )


def plan_rotation(
    run_index: int,
    *,
    anchor: date | None = None,
    windows_per_run: int = WINDOWS_PER_RUN,
) -> RotationPlan:
    """Build the rotation for a run.

    Two axes move together, both keyed off the run index:

    The **size slice** advances a whole block per run, so run 2's buckets sit
    entirely above run 1's and the two query sets cannot be identical. This is
    the axis that guarantees freshness.

    The **library order** rotates within each tier, so a run cut short by
    budget doesn't always spend it on the same libraries. Tier order itself is
    never rotated: tiers are ordered by measured precision, and shuffling them
    would trade a real gain for cosmetic variety.

    `anchor` is retained so a caller can record the date a plan was built. It
    no longer influences the slices, which is the point: the slices are now a
    property of the files being searched rather than of when the run happened.
    """
    if run_index < 1:
        raise ValueError(f"run_index starts at 1, got {run_index}")
    return RotationPlan(
        run_index=run_index,
        windows=size_windows(
            windows_per_run, skip=(run_index - 1) * windows_per_run
        ),
        library_offset=run_index - 1,
        anchor=anchor or date.today(),
    )


@dataclass(frozen=True)
class FreshBatchCheck:
    """Whether a planned query set genuinely differs from earlier runs."""

    run_id: str
    planned: int
    already_used: int

    @property
    def novel(self) -> int:
        return self.planned - self.already_used

    @property
    def is_fresh(self) -> bool:
        return self.already_used < self.planned


def verify_fresh_batch(
    conn, run_id: str, queries: Sequence
) -> FreshBatchCheck:
    """Refuse to start a run that would replay an earlier one.

    Compares the planned (query, slice) pairs against every pair an earlier run
    already executed. An overlap is fine and expected; a *complete* overlap
    means the run would return GitHub's same best-match hits again and record
    nothing new, which is the exact failure SEARCH_STRATEGY.md section 7
    exists to prevent.
    """
    previous = storage.query_signatures_before_run(conn, run_id)
    planned = {(q.query, q.search_window) for q in queries}
    used = planned & previous

    check = FreshBatchCheck(
        run_id=run_id, planned=len(planned), already_used=len(used)
    )
    if planned and not check.is_fresh:
        raise FreshBatchError(
            f"Every one of the {len(planned)} planned queries for {run_id} was "
            f"already executed by an earlier run. GitHub returns the same "
            f"best-match hits for an identical query, so this would replay "
            f"rather than discover. Rotate the slice or the library subset."
        )
    return check


# --- cross-run classification ----------------------------------------------

NEW_FOR_RUN = "new_for_run"
PREVIOUSLY_SEEN = "previously_seen"


def classify_candidate(conn, candidate_id: str, run_id: str) -> str:
    """Whether this candidate was already surfaced by an earlier run."""
    seen = storage.candidate_ids_discovered_before_run(conn, run_id)
    return PREVIOUSLY_SEEN if candidate_id in seen else NEW_FOR_RUN


@dataclass(frozen=True)
class RunStats:
    """What one discovery run actually did.

    Counts are deliberately separate rather than collapsed. "Raw results" and
    "unique repositories" differ because several hits can land on one
    repository; "unique repositories" and "new candidates" differ because a
    later run resurfaces earlier ones. Reporting one number for all three would
    hide both effects.
    """

    run_id: str
    queries_executed: int = 0
    queries_failed: int = 0
    zero_result_queries: int = 0
    capped_queries: int = 0
    raw_results: int = 0
    unique_repositories: int = 0
    previously_seen: int = 0
    new_candidates: int = 0

    def summary_lines(self) -> list[str]:
        return [
            f"run                   {self.run_id}",
            f"queries executed      {self.queries_executed}",
            f"queries failed        {self.queries_failed}",
            f"zero-result queries   {self.zero_result_queries}",
            f"capped queries        {self.capped_queries}",
            f"raw results returned  {self.raw_results}",
            f"unique repositories   {self.unique_repositories}",
            f"previously seen       {self.previously_seen}",
            f"new candidates        {self.new_candidates}",
        ]


def run_stats(conn, run_id: str) -> RunStats:
    """Everything a run's summary needs, derived rather than stored.

    Nothing here is a counter maintained during the run, so the numbers cannot
    drift from what was actually persisted.
    """
    totals = storage.run_query_totals(conn, run_id)
    surfaced = set(storage.list_candidate_ids_for_run(conn, run_id))
    seen_before = storage.candidate_ids_discovered_before_run(conn, run_id)

    previously_seen = surfaced & seen_before
    return RunStats(
        run_id=run_id,
        queries_executed=totals["queries_executed"],
        queries_failed=totals["queries_failed"],
        zero_result_queries=totals["zero_result_queries"],
        capped_queries=totals["capped_queries"],
        raw_results=totals["raw_results"],
        unique_repositories=len(surfaced),
        previously_seen=len(previously_seen),
        new_candidates=len(surfaced - seen_before),
    )
