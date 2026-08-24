"""Report generator: the ranked CSV and the Markdown report.

A pure read and export over the database. Nothing here calls an API, enriches
a candidate, or changes a stored value; SQLite is the single source of truth,
and this module only turns what is already there into two files
(TECHNICAL_DESIGN.md section 13).

Two files come out of one read pass over the same data, so they cannot
disagree with each other: `ranked-candidates.csv` for spreadsheet use, and
`dependency-map-report.md` as the actual "ranked table plus the query method"
artefact the task brief asks for, meant to be readable on its own without the
database open next to it.

The rule this module exists to enforce, more than any formatting choice: a
missing dimension is never smoothed into the number. Every candidate's entry
shows its score, its confidence, its evidence coverage as a fraction, and an
explicit "Unknown" line for anything that defaulted (SCORING_MODEL.md section
12, IMPLEMENTATION_PLAN.md phase 11). And every capped query is described as
the partial sample it is: "10 of 75,648" is not "75,648 inspected".
"""

from __future__ import annotations

import csv
import io
import re
import subprocess
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping

from . import storage
from .db import SCHEMA_VERSION, SCORING_DIMENSIONS
from .dedup import RunStats
from .dedup import run_stats as compute_run_stats

#: Reader-facing labels for the seven dimensions, in canonical order.
DIMENSION_LABELS: dict[str, str] = {
    "document_volume": "Document volume",
    "document_complexity": "Document complexity",
    "business_criticality": "Business criticality",
    "pipeline_complexity": "Pipeline complexity",
    "maintenance_burden": "Maintenance burden",
    "build_vs_buy_signal": "Build-vs-buy signal",
    "commercial_leverage": "Commercial leverage",
}

_MAX_ZERO_RESULT_EXAMPLES = 25
_MAX_QUERY_METHOD_EXAMPLES_PER_TIER = 1


class ReportError(Exception):
    """The report could not be generated from what is stored."""


# --- value objects -----------------------------------------------------------


@dataclass(frozen=True)
class DiscoveryHit:
    """One query that surfaced a candidate, with enough of the query's own
    record to describe its coverage honestly."""

    query: str
    discovery_source: str
    library_name: str | None
    discovery_tier: int | None
    search_window: str | None
    total_count: int | None
    returned_count: int
    capped: bool | None
    discovery_result_rank: int | None
    run_id: str
    discovered_at: str

    @property
    def coverage_note(self) -> str:
        return describe_query_coverage(self.total_count, self.returned_count, self.capped)


@dataclass(frozen=True)
class RankedCandidate:
    """One row of the ranked table, with everything its detail section needs
    already assembled from a single read pass."""

    rank: int
    row: Mapping
    unknown_dimensions: tuple[str, ...]
    discovery_hits: tuple[DiscoveryHit, ...]
    dependencies: tuple[Mapping, ...]
    evidence_trail: tuple[Mapping, ...]

    @property
    def candidate_id(self) -> str:
        return self.row["candidate_id"]

    @property
    def repo_full_name(self) -> str:
        return f"{self.row['repo_owner']}/{self.row['repo_name']}"

    @property
    def evidenced_count(self) -> int:
        return len(SCORING_DIMENSIONS) - len(self.unknown_dimensions)

    @property
    def evidence_coverage_fraction(self) -> str:
        return f"{self.evidenced_count}/{len(SCORING_DIMENSIONS)}"

    def dimension_score(self, name: str) -> int:
        return int(self.row[name])

    def is_unknown(self, name: str) -> bool:
        return name in self.unknown_dimensions

    @property
    def discovered_by_libraries(self) -> tuple[str, ...]:
        names = {h.library_name for h in self.discovery_hits if h.library_name}
        return tuple(sorted(names))

    @property
    def discovery_tiers(self) -> tuple[int, ...]:
        tiers = {h.discovery_tier for h in self.discovery_hits if h.discovery_tier}
        return tuple(sorted(tiers))

    @property
    def primary_evidence_url(self) -> str:
        if self.evidence_trail:
            return self.evidence_trail[0]["evidence_url"]
        return self.row["repo_url"]


@dataclass(frozen=True)
class ReportData:
    """Everything both output formats are rendered from. One read pass."""

    generated_at: str
    schema_version: int
    commit_hash: str | None
    runs: tuple[Mapping, ...]
    run_stats: dict[str, RunStats]
    all_queries: tuple[Mapping, ...]
    ranked: tuple[RankedCandidate, ...]
    total_candidates_ever: int
    keep_count: int
    investigate_count: int
    reject_count: int
    evidence_collected_count: int = 0
    sample_by_tier: Mapping[int, int] = field(default_factory=dict)
    #: The run this report describes, or None for a cumulative report.
    run_id: str | None = None
    #: Surfaced / new / previously_seen / enriched for that run.
    run_counts: Mapping[str, int] = field(default_factory=dict)
    #: Project-wide totals, always labelled as such where they are shown.
    cumulative: Mapping[str, int] = field(default_factory=dict)
    #: Scored candidates whose maintenance_burden rests on collected evidence.
    maintenance_enriched: int = 0

    @property
    def sample_size(self) -> int:
        """Candidates that actually reached qualification.

        This is the evidence-enriched sample, which is deliberately smaller
        than the discovery universe. Keeping the two as separate numbers is
        what stops the report implying every discovered repository was
        inspected.
        """
        return self.keep_count + self.investigate_count + self.reject_count

    @property
    def scored_count(self) -> int:
        return len(self.ranked)

    @property
    def capped_queries(self) -> tuple[Mapping, ...]:
        return tuple(q for q in self.all_queries if q["capped"])

    @property
    def zero_result_queries(self) -> tuple[Mapping, ...]:
        return tuple(q for q in self.all_queries if q["total_count"] == 0)

    @property
    def failed_queries(self) -> tuple[Mapping, ...]:
        return tuple(q for q in self.all_queries if q["total_count"] is None)

    @property
    def total_raw_results(self) -> int:
        return sum(q["returned_count"] for q in self.all_queries)


@dataclass(frozen=True)
class ReportSummary:
    """What the CLI prints after generating both files."""

    csv_path: Path
    markdown_path: Path
    ranked_count: int
    keep_count: int
    investigate_count: int
    reject_count: int
    total_queries: int
    capped_queries: int
    zero_result_queries: int

    def summary_lines(self) -> list[str]:
        return [
            f"ranked candidates      {self.ranked_count}",
            f"  keep                 {self.keep_count}",
            f"  investigate          {self.investigate_count}",
            f"  reject (excluded)    {self.reject_count}",
            f"discovery queries      {self.total_queries}",
            f"  capped               {self.capped_queries}",
            f"  zero-result          {self.zero_result_queries}",
        ]


# --- coverage honesty ---------------------------------------------------------


def describe_query_coverage(
    total_count: int | None, returned_count: int, capped: bool | None
) -> str:
    """The sentence that stops a sample being read as a census.

    A capped query's returned_count is a small fraction of total_count, and
    that gap has to be stated in words every time the number is shown, not
    left for a reader to notice on their own.
    """
    if total_count is None:
        return "Query failed before a total could be recorded."
    if total_count == 0:
        return "No matches. The query returned zero results."
    if capped:
        return (
            f"Sampled {returned_count} of {total_count:,} matches; the query "
            f"exceeded GitHub's 1,000-result pagination ceiling. This is a "
            f"partial sample, not an exhaustive result — the {total_count:,} "
            f"figure describes how many repositories matched, not how many "
            f"were inspected."
        )
    return (
        f"Retrieved {returned_count} of {total_count:,} matches; the full "
        f"result set was below GitHub's 1,000-result pagination ceiling at "
        f"collection time."
    )


def _commit_hash() -> str | None:
    """Best-effort local git hash. Never a network call, never fatal."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=5, check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


# --- assembling the data -------------------------------------------------


def _discovery_hits_with_query_data(conn, candidate_id: str) -> tuple[DiscoveryHit, ...]:
    """Every query that surfaced this candidate, with that query's own totals.

    `list_discovery_evidence_for_candidate` already joins to `discovery_queries`
    for the query text, source, tier and window; `total_count`, `returned_count`
    and `capped` are read from the same joined row rather than a second query.
    """
    rows = conn.execute(
        "SELECT e.discovery_result_rank, "
        "       q.query, q.discovery_source, q.library_name, q.discovery_tier, "
        "       q.search_window, q.total_count, q.returned_count, q.capped, "
        "       q.run_id, q.executed_at "
        "FROM discovery_evidence e "
        "JOIN discovery_queries q ON q.query_id = e.query_id "
        "WHERE e.candidate_id = ? "
        "ORDER BY q.executed_at, e.id",
        (candidate_id,),
    ).fetchall()
    return tuple(
        DiscoveryHit(
            query=row["query"],
            discovery_source=row["discovery_source"],
            library_name=row["library_name"],
            discovery_tier=row["discovery_tier"],
            search_window=row["search_window"],
            total_count=row["total_count"],
            returned_count=row["returned_count"],
            capped=bool(row["capped"]) if row["capped"] is not None else None,
            discovery_result_rank=row["discovery_result_rank"],
            run_id=row["run_id"],
            discovered_at=row["executed_at"],
        )
        for row in rows
    )


def _status_count(conn, status: str, run_id: str | None) -> int:
    """How many candidates hold a qualification status, optionally per run."""
    if run_id is None:
        return len(storage.list_candidates_by_status(conn, status))
    return int(
        conn.execute(
            "SELECT COUNT(DISTINCT de.candidate_id) FROM discovery_evidence de "
            "JOIN discovery_queries q ON q.query_id = de.query_id "
            "JOIN qualification g ON g.candidate_id = de.candidate_id "
            "WHERE q.run_id = ? AND g.qualification_status = ?",
            (run_id, status),
        ).fetchone()[0]
    )


def gather_report_data(conn, run_id: str | None = None) -> ReportData:
    """One read pass over the database, assembled into everything the two
    renderers need. Nothing here writes, scores, qualifies, or calls out.

    With `run_id`, every headline number describes that run: its queries, the
    candidates it surfaced, and the ones among those that were qualified and
    scored. Project-wide totals are still gathered, but they travel in
    `cumulative` and are only ever rendered under a heading that says so.
    Reporting one run's work using database-wide counts would credit run 2
    with everything run 1 found.
    """
    runs = tuple(storage.list_runs(conn))
    run_stats = {run["run_id"]: compute_run_stats(conn, run["run_id"]) for run in runs}
    all_queries = tuple(storage.list_all_discovery_queries(conn, run_id))

    ranked_rows = storage.list_ranked_candidates(conn, run_id)
    ranked: list[RankedCandidate] = []
    for index, row in enumerate(ranked_rows, start=1):
        unknown = tuple(storage.decode_unknown_dimensions(row["unknown_dimensions"]))
        ranked.append(
            RankedCandidate(
                rank=index,
                row=row,
                unknown_dimensions=unknown,
                discovery_hits=_discovery_hits_with_query_data(conn, row["candidate_id"]),
                dependencies=tuple(
                    storage.list_dependencies_for_candidate(conn, row["candidate_id"])
                ),
                evidence_trail=tuple(
                    storage.list_evidence_trail_for_candidate(conn, row["candidate_id"])
                ),
            )
        )

    counts = storage.run_candidate_counts(conn, run_id) if run_id else {}
    return ReportData(
        run_id=run_id,
        run_counts=counts,
        cumulative=storage.cumulative_counts(conn),
        generated_at=_utcnow(),
        schema_version=SCHEMA_VERSION,
        commit_hash=_commit_hash(),
        runs=runs,
        run_stats=run_stats,
        all_queries=all_queries,
        ranked=tuple(ranked),
        total_candidates_ever=(
            counts["surfaced"] if run_id else storage.count_candidates(conn)
        ),
        keep_count=_status_count(conn, "keep", run_id),
        investigate_count=_status_count(conn, "investigate", run_id),
        reject_count=_status_count(conn, "reject", run_id),
        evidence_collected_count=_count_evidence_collected(conn, run_id),
        maintenance_enriched=sum(
            1 for c in ranked
            if "maintenance_burden" not in c.unknown_dimensions
        ),
        sample_by_tier=_sample_by_tier(conn, run_id),
    )


def _count_evidence_collected(conn, run_id: str | None = None) -> int:
    """How many candidates have had evidence collected at all.

    Distinct from the qualified sample: evidence can exist for a candidate that
    was not part of the official sample, and reporting both numbers is what
    makes the gap auditable instead of invisible. Scoped to a run, it counts
    only candidates that run surfaced.
    """
    if run_id:
        row = conn.execute(
            "SELECT COUNT(DISTINCT de.candidate_id) FROM discovery_evidence de "
            "JOIN discovery_queries q ON q.query_id = de.query_id "
            "JOIN business_evidence b ON b.candidate_id = de.candidate_id "
            "WHERE q.run_id = ?",
            (run_id,),
        ).fetchone()
    else:
        row = conn.execute("SELECT COUNT(*) FROM business_evidence").fetchone()
    return int(row[0]) if row else 0


def _sample_by_tier(conn, run_id: str | None = None) -> dict[int, int]:
    """Qualified candidates per discovery tier.

    Tier is the strongest (lowest) tier of any query that surfaced the
    candidate, which is the same rule the sample was drawn with, so the
    published breakdown can be checked against the stated rule.
    """
    where = "WHERE q.run_id = ?" if run_id else ""
    params = (run_id,) if run_id else ()
    rows = conn.execute(
        "SELECT tier, COUNT(*) AS n FROM ("
        "  SELECT MIN(q.discovery_tier) AS tier"
        "  FROM qualification g"
        "  JOIN discovery_evidence de ON de.candidate_id = g.candidate_id"
        "  JOIN discovery_queries q   ON q.query_id = de.query_id"
        f" {where}"
        "  GROUP BY g.candidate_id"
        ") GROUP BY tier ORDER BY tier",
        params,
    ).fetchall()
    return {int(r[0]): int(r[1]) for r in rows if r[0] is not None}


# --- CSV -----------------------------------------------------------------

CSV_FIELDS = [
    "rank", "candidate_id", "repo_url", "repo_owner", "repo_name",
    "company_name", "product_name", "website_url", "industry_category",
    "first_seen_run_id", "discovered_by_libraries", "discovery_tiers",
    "qualification_status", "qualification_confidence", "qualification_reason",
    "document_volume", "document_complexity", "business_criticality",
    "pipeline_complexity", "maintenance_burden", "build_vs_buy_signal",
    "commercial_leverage", "raw_weighted_score", "final_score",
    "confidence_band", "evidence_coverage", "unknown_dimensions",
    "gate_cap_applied", "evidence_trail_count", "primary_evidence_url",
]


def render_csv(data: ReportData) -> str:
    """One row per ranked candidate. Rejects never appear here, by
    construction: `list_ranked_candidates` only returns keep/investigate rows
    that have a score, and a reject never has one."""
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()

    for candidate in data.ranked:
        row = candidate.row
        writer.writerow({
            "rank": candidate.rank,
            "candidate_id": row["candidate_id"],
            "repo_url": row["repo_url"],
            "repo_owner": row["repo_owner"],
            "repo_name": row["repo_name"],
            "company_name": row["company_name"] or "",
            "product_name": row["product_name"] or "",
            "website_url": row["website_url"] or "",
            "industry_category": row["industry_category"] or "unknown",
            "first_seen_run_id": row["first_seen_run_id"] or "",
            "discovered_by_libraries": "; ".join(candidate.discovered_by_libraries),
            "discovery_tiers": "; ".join(str(t) for t in candidate.discovery_tiers),
            "qualification_status": row["qualification_status"],
            "qualification_confidence": row["qualification_confidence"],
            "qualification_reason": row["qualification_reason"],
            "document_volume": candidate.dimension_score("document_volume"),
            "document_complexity": candidate.dimension_score("document_complexity"),
            "business_criticality": candidate.dimension_score("business_criticality"),
            "pipeline_complexity": candidate.dimension_score("pipeline_complexity"),
            "maintenance_burden": candidate.dimension_score("maintenance_burden"),
            "build_vs_buy_signal": candidate.dimension_score("build_vs_buy_signal"),
            "commercial_leverage": candidate.dimension_score("commercial_leverage"),
            "raw_weighted_score": row["raw_weighted_score"],
            "final_score": row["final_score"],
            "confidence_band": row["confidence_band"],
            "evidence_coverage": candidate.evidence_coverage_fraction,
            "unknown_dimensions": "; ".join(candidate.unknown_dimensions),
            "gate_cap_applied": row["gate_cap_applied"] if row["gate_cap_applied"] is not None else "",
            "evidence_trail_count": len(candidate.evidence_trail),
            "primary_evidence_url": candidate.primary_evidence_url,
        })
    return buffer.getvalue()


# --- Markdown --------------------------------------------------------------


#: Every character that would end a line, split a table row, or otherwise
#: break the surrounding Markdown structure. A company name lifted from a
#: README can contain any of them: run 1 produced 'Notice  \r\n\r\nKedo',
#: whose bare carriage return truncated one ranked-table row from ten
#: columns to four. Escaping the pipe alone is not enough, because a \r is
#: invisible in an editor but still ends a line for a Markdown parser.
_MD_CONTROL = re.compile(
    "[\\r\\n\\t\\v\\f\\x00-\\x08\\x0b\\x0c\\x0e-\\x1f\\x85\\u2028\\u2029]+"
)


def _md_escape(text: str) -> str:
    """Make arbitrary extracted text safe inside a Markdown table cell.

    Collapses every line-breaking and control character to one space, then
    escapes the cell separator. The CSV writer needs none of this because it
    quotes fields itself, so this stays Markdown-only.
    """
    collapsed = _MD_CONTROL.sub(" ", text or "")
    return collapsed.replace("|", "\\|").strip()


def _render_executive_summary(data: ReportData) -> list[str]:
    lines = [
        "## Executive summary", "",
        f"- Discovery runs recorded: **{len(data.runs)}**",
        f"- Discovery queries executed: **{len(data.all_queries)}**",
        f"  - Capped (exceeded GitHub's 1,000-result ceiling): **{len(data.capped_queries)}**",
        f"  - Zero-result: **{len(data.zero_result_queries)}**",
        f"  - Failed (no total recorded): **{len(data.failed_queries)}**",
        f"- Raw discovery hits (API results, before dedup): **{data.total_raw_results}**",
        f"- Unique repositories discovered: **{data.total_candidates_ever}**",
        f"- Qualification: keep **{data.keep_count}**, investigate "
        f"**{data.investigate_count}**, reject **{data.reject_count}**",
        f"- Scored candidates (keep or investigate with a score): "
        f"**{data.scored_count}**",
        "- Candidates with enhanced maintenance-burden evidence: **0** "
        "(the phase 14 targeted commit-history pass has not run yet; "
        "`maintenance_burden` defaults to unknown for every candidate)",
        "",
        "Raw hits and unique repositories are different numbers on purpose: "
        "several queries, or several file matches within one query, can all "
        "point at the same repository. The gap between them is deduplication "
        "working, not an error.",
        "",
    ]
    return lines


def _render_ranked_table(data: ReportData) -> list[str]:
    lines = ["## Ranked table", ""]
    if not data.ranked:
        lines += [
            "No candidates currently qualify for the ranked table. A candidate "
            "needs `qualification_status` of keep or investigate and a score "
            "row; none in the stored data meet both yet.",
            "",
        ]
        return lines

    lines += [
        "Sorted by score, highest first. Ties break on confidence "
        "(high, then medium, then low), then on candidate id, so the order is "
        "reproducible from the same data.",
        "",
        "| Rank | Repository | Company | Qualification | Score | Confidence | "
        "Evidence coverage | Unknown dimensions |",
        "|---:|---|---|---|---:|---|---|---|",
    ]
    for candidate in data.ranked:
        row = candidate.row
        unknown = ", ".join(
            DIMENSION_LABELS[d] for d in candidate.unknown_dimensions
        ) or "none"
        lines.append(
            f"| {candidate.rank} "
            f"| [{_md_escape(candidate.repo_full_name)}]({row['repo_url']}) "
            f"| {_md_escape(row['company_name'] or '—')} "
            f"| {row['qualification_status']} "
            f"| {row['final_score']}/100 "
            f"| {row['confidence_band']} "
            f"| {candidate.evidence_coverage_fraction} "
            f"| {_md_escape(unknown)} |"
        )
    lines.append("")
    return lines


def _render_candidate_detail(candidate: RankedCandidate) -> list[str]:
    row = candidate.row
    lines = [f"### {candidate.rank}. {_md_escape(candidate.repo_full_name)}", ""]

    lines += ["**Repository / product**", ""]
    lines += [
        f"- Repository: [{row['repo_url']}]({row['repo_url']})",
        f"- Company: {_md_escape(row['company_name']) or 'Unknown — not stated in the repository'}",
        f"- Product: {_md_escape(row['product_name']) or 'Unknown'}",
        f"- Industry: {row['industry_category'] or 'unknown'} "
        f"(keyword-derived; treat as low-confidence supporting evidence, "
        f"never a determining factor)",
        f"- Website: {_md_escape(row['website_url']) or 'Unknown'}",
        "",
    ]

    lines += ["**Qualification**", ""]
    lines += [
        f"- Status: **{row['qualification_status']}**",
        f"- Confidence: {row['qualification_confidence']}",
        f"- Reason: {_md_escape(row['qualification_reason'])}",
        "",
    ]

    lines += ["**Score**", ""]
    lines += [
        f"- Score: {row['final_score']}/100 (a score, not a probability)",
        f"- Raw weighted score: {row['raw_weighted_score']:.2f} / 5",
        f"- Confidence: {row['confidence_band']}",
    ]
    if row["gate_cap_applied"] is not None:
        lines.append(
            f"- Gate cap applied: **{row['gate_cap_applied']}** — the weighted "
            f"calculation produced a higher number, but a qualification-gate "
            f"condition capped it (SCORING_MODEL.md section 14)"
        )
    lines.append("")
    lines += ["| Dimension | Score (0-5) |", "|---|---:|"]
    for name in SCORING_DIMENSIONS:
        label = DIMENSION_LABELS[name]
        suffix = " *(unknown)*" if candidate.is_unknown(name) else ""
        lines.append(f"| {label}{suffix} | {candidate.dimension_score(name)} |")
    lines.append("")

    lines += ["**Evidence coverage**", ""]
    lines.append(f"Evidence coverage: {candidate.evidence_coverage_fraction} dimensions")
    lines.append("")
    if candidate.unknown_dimensions:
        for name in candidate.unknown_dimensions:
            lines.append(f"- {DIMENSION_LABELS[name]}: Unknown")
    else:
        lines.append("- No unknown dimensions; all seven were directly evidenced.")
    lines.append("")

    lines += ["**Discovery provenance**", ""]
    if not candidate.discovery_hits:
        lines.append("No discovery query record found for this candidate.")
    else:
        for hit in candidate.discovery_hits:
            library = hit.library_name or "(co-occurrence query, spans multiple libraries)"
            window = hit.search_window or "unsliced"
            lines.append(
                f"- Tier {hit.discovery_tier or '—'}, `{library}`, run `{hit.run_id}`, "
                f"window `{window}`, rank {hit.discovery_result_rank or '—'}"
            )
            lines.append(f"  - Query: `{hit.query}`")
            lines.append(f"  - {hit.coverage_note}")
    lines.append("")

    lines += ["**Dependency evidence**", ""]
    if not candidate.dependencies:
        lines.append("No dependency evidence recorded.")
    else:
        for dep in candidate.dependencies:
            lines.append(
                f"- `{dep['library_name']}` ({dep['library_category']}, "
                f"{dep['direction']}) — {dep['detection_method']} — "
                f"[{dep['manifest_file'] or 'code'}]({dep['evidence_url']})"
            )
    lines.append("")

    lines += ["**Evidence trail**", ""]
    if not candidate.evidence_trail:
        lines.append("No evidence trail entries recorded.")
    else:
        for entry in candidate.evidence_trail:
            excerpt = _md_escape((entry["evidence_excerpt"] or "")[:200])
            lines.append(
                f"- [{entry['evidence_type']}]({entry['evidence_url']}) "
                f"(source: {entry['source']}){': ' + excerpt if excerpt else ''}"
            )
    lines.append("")
    return lines


def _render_query_method(data: ReportData) -> list[str]:
    lines = [
        "## Query method", "",
        "This section documents how candidates were found, so the result can "
        "be checked and rerun (the task brief's \"query method\" requirement).",
        "",
        "**Discovery is tiered by measured precision, not library popularity.** "
        "Queries run in three tiers, read from `discovery_tier` in the library "
        "universe:",
        "",
        "1. **Infrastructure** — a deployed conversion service (for example "
        "Gotenberg), found by a Dockerfile or compose-file reference rather "
        "than a manifest line. The highest-precision tier measured.",
        "2. **Template generation** — libraries whose purpose is populating a "
        "template from data, so their presence implies a real pipeline.",
        "3. **Broad manifest** — a library declared in a dependency manifest. "
        "The most common signal, and also the noisiest.",
        "",
        "**Slicing.** GitHub returns at most 1,000 results for any single query, "
        "however it is paginated. Every tier-3 query is therefore run as a set "
        "of sliced queries, most often by date window (`search_window` in the "
        "record below), so a broad query's true coverage — and its gap — is "
        "visible rather than silently truncated. Tier 1 needs no slicing: the "
        "measured tier-1 query stayed under the ceiling on its own.",
        "",
        "**`total_count`** is what the source reported as the total number of "
        "matches for a query, independent of how many were actually "
        "retrieved. **`capped`** means that total exceeded GitHub's "
        "1,000-result pagination ceiling — it does **not** mean 1,000 results "
        "were retrieved, and in practice far fewer are. A capped query is "
        "always a partial sample; see the coverage note on each query below.",
        "",
        "**Deduplication.** The same repository found by different queries, in "
        "the same run or a later one, resolves to one candidate via a "
        "deterministic id derived from its normalized URL. Every query that "
        "found it still gets its own evidence record, so overlap between "
        "queries stays visible instead of being collapsed away.",
        "",
        "**Fresh-batch rotation (Run 2 and beyond).** A later run's date "
        "windows are shifted a full block further back than the run before "
        "it, so the two runs partition time rather than overlapping, and a "
        "run is refused outright if its planned queries were already executed "
        "by an earlier run. The exact rotation for each run is in the run "
        "information section below.",
        "",
    ]

    by_tier: dict[int, list] = {}
    for query in data.all_queries:
        tier = query["discovery_tier"]
        if tier is not None:
            by_tier.setdefault(tier, []).append(query)

    lines.append("**Example queries actually executed, one per tier:**")
    lines.append("")
    if not data.all_queries:
        lines.append(
            "No discovery queries have been recorded yet, so no worked "
            "example is available."
        )
        lines.append("")
    else:
        for tier in sorted(by_tier):
            examples = by_tier[tier][:_MAX_QUERY_METHOD_EXAMPLES_PER_TIER]
            for query in examples:
                lines.append(f"- Tier {tier}: `{query['query']}`")
                lines.append(
                    f"  - {describe_query_coverage(query['total_count'], query['returned_count'], bool(query['capped']) if query['capped'] is not None else None)}"
                )
        lines.append("")

    lines.append(
        "**This is not an exhaustive map of every document-processing "
        "repository on GitHub.** It is a reproducible sample built from a "
        "documented, versioned query set. Coverage is partial wherever a "
        "query is marked capped, and the size of that gap is stated rather "
        "than hidden."
    )
    lines.append("")
    return lines


def _render_zero_result_queries(data: ReportData) -> list[str]:
    lines = ["## Zero-result queries", ""]
    zeros = data.zero_result_queries
    lines.append(
        f"{len(zeros)} of {len(data.all_queries)} recorded queries returned no "
        f"results. An empty result can mean the library genuinely was not "
        f"found this way, or it can mean the query itself is malformed — "
        f"which is exactly what one earlier query in this project's history "
        f"turned out to be, until it was corrected. Zero-result queries are "
        f"therefore worth reviewing, not treated as uninteresting."
    )
    lines.append("")
    if zeros:
        shown = zeros[:_MAX_ZERO_RESULT_EXAMPLES]
        lines += ["| Query | Library | Tier | Run |", "|---|---|---:|---|"]
        for query in shown:
            lines.append(
                f"| `{_md_escape(query['query'])}` "
                f"| {query['library_name'] or '—'} "
                f"| {query['discovery_tier'] or '—'} "
                f"| {query['run_id']} |"
            )
        if len(zeros) > len(shown):
            lines.append("")
            lines.append(f"...and {len(zeros) - len(shown)} more.")
        lines.append("")
    return lines


def _render_run_information(data: ReportData) -> list[str]:
    lines = ["## Run information", ""]
    if not data.runs:
        lines += ["No runs recorded yet.", ""]
        return lines
    for run in data.runs:
        stats = data.run_stats.get(run["run_id"])
        lines += [
            f"### {run['run_id']}", "",
            f"- Started: {run['started_at']}",
            f"- Finished: {run['finished_at'] or 'not finished'}",
            f"- Rotation: {run['notes'] or '(none recorded)'}",
        ]
        if stats is not None:
            lines += [
                f"- Queries executed: {stats.queries_executed} "
                f"(failed: {stats.queries_failed})",
                f"- Raw results: {stats.raw_results}",
                f"- Unique repositories surfaced: {stats.unique_repositories}",
                f"- Previously seen (found by an earlier run): "
                f"{stats.previously_seen}",
                f"- New candidates: {stats.new_candidates}",
            ]
        lines.append("")
    return lines


def _render_reproducibility(data: ReportData) -> list[str]:
    return [
        "## Reproducibility", "",
        f"- Generated: {data.generated_at}",
        f"- Database schema version: {data.schema_version}",
        f"- Repository commit: {data.commit_hash or 'unavailable (not run inside a git checkout, or no commits yet)'}",
        "",
    ]


def _render_sampling(data: ReportData) -> list[str]:
    """State plainly how much of the discovery universe was actually inspected.

    Without this the report shows a large discovery count next to a much
    smaller set of qualification outcomes and leaves a reader to assume the
    difference was reviewed and dismissed. It was not: it was never looked at.
    """
    universe = data.total_candidates_ever
    sample = data.sample_size
    outside = max(data.evidence_collected_count - sample, 0)

    scope = f" ({data.run_id})" if data.run_id else ""
    lines = [f"## Coverage and sampling{scope}", ""]

    if data.run_id and data.run_counts:
        counts = data.run_counts
        lines += [
            f"Every number in this section describes **{data.run_id} only**. "
            "Totals across all runs are in the cumulative section at the end.",
            "",
            f"- Repositories **surfaced by {data.run_id}**: "
            f"**{counts['surfaced']:,}**",
            f"  - Found for the first time by this run: "
            f"**{counts['new']:,}**",
            f"  - Already seen by an earlier run: "
            f"**{counts['previously_seen']:,}**",
        ]
    else:
        lines.append(f"- Repositories **discovered**: **{universe:,}**")

    lines += [
        f"- Repositories **selected for evidence enrichment**: **{sample:,}**",
        f"- Repositories with evidence collected but outside the official "
        f"sample: **{outside:,}**",
        "",]

    if data.run_id and data.run_counts and data.run_counts["previously_seen"]:
        lines += [
            "**Where this run's evidence came from.** "
            f"{data.run_counts['previously_seen']:,} of the repositories above "
            "were first found by an earlier run, so any evidence held for them "
            "may have been collected then rather than during this run. The "
            "database records which run first saw a candidate "
            "(`candidates.first_seen_run_id`); it does not timestamp each "
            "evidence row, so that first-sighting is the whole provenance "
            "available and nothing finer is claimed here.",
            "",
        ]

    subject = (
        f"surfaced by {data.run_id}" if data.run_id else "discovered"
    )
    lines += [
        f"**Every qualification, scoring and ranking number in this report "
        f"describes the {sample:,}-repository evidence sample, not the "
        f"{universe:,} repositories {subject}.** The remaining "
        f"{universe - sample:,} were surfaced by a discovery query and stored, "
        "but no evidence was collected for them and they were never qualified, "
        "scored or ranked. They are absent from the results because they were "
        "not examined, which is not the same as having been examined and "
        "found wanting.",
        "",
    ]

    if data.sample_by_tier:
        lines += [
            "### How the sample was selected", "",
            "The sample is deterministic and stratified by discovery tier, so "
            "it can be reproduced exactly from stored discovery data. A "
            "candidate's tier is the strongest (lowest) tier of any query that "
            "surfaced it; within a tier, candidates are ordered by "
            "`candidate_id` ascending and taken from the front.", "",
            "| Tier | Selected |", "|---|---:|",
        ]
        for tier in sorted(data.sample_by_tier):
            lines.append(f"| {tier} | {data.sample_by_tier[tier]:,} |")
        lines += [
            f"| **Total** | **{sample:,}** |", "",
            "`candidate_id` is a hash of the normalised repository URL, so the "
            "ordering depends only on repository identity, never on the order "
            "results happened to arrive in.", "",
            "Because the sample is stratified rather than proportional, the "
            "tier mix here is not the tier mix of the discovery universe. "
            "Tier 1 and tier 2 are deliberately over-represented relative to "
            "their share of discovered repositories, so keep and reject rates "
            "quoted per tier should not be read as rates across all of GitHub.",
            "",
        ]
    return lines


def _render_maintenance_scope(data: ReportData) -> list[str]:
    """Say which candidates' maintenance burden actually rests on evidence.

    The maintenance pass is deliberately bounded to the highest-ranked
    candidates, so most of the ranked table carries `maintenance_burden = 0`
    meaning "never inspected". That zero costs a candidate 15 percent of the
    weight, and a reader comparing two rows needs to know when the difference
    between them is a difference in what was collected rather than in the
    repositories.
    """
    total = len(data.ranked)
    if not total:
        return []
    enriched = data.maintenance_enriched
    if enriched == 0:
        return [
            "> **Maintenance burden was not collected for this set.** Every "
            "candidate below scores 0 on that dimension because no source "
            "inspection has run for it, not because its document code is "
            "thin.", "",
        ]
    if enriched == total:
        return []
    return [
        "> **Maintenance-burden evidence was enriched for a bounded, "
        "highest-ranked candidate set; candidates outside that set may still "
        f"have unknown `maintenance_burden`.** {enriched} of the {total} "
        f"ranked candidates below rest on collected source evidence for that "
        f"dimension; the remaining {total - enriched} score 0 on it because "
        "it was never inspected, which is not a finding that their document "
        "code is thin. `maintenance_burden` carries 15 percent of the weight, "
        "so an un-enriched candidate is ranked below where its evidence might "
        "otherwise place it. Comparing a candidate inside the enriched set "
        "against one outside it compares different amounts of collection.",
        "",
    ]


def _render_cumulative(data: ReportData) -> list[str]:
    """Project-wide totals, under a heading that says they are project-wide.

    Only rendered for a run-scoped report, where the distinction matters. A
    reader who sees 8,013 next to one run's results should never have to guess
    which of the two the number describes.
    """
    if not data.run_id or not data.cumulative:
        return []
    c = data.cumulative
    return [
        "## Cumulative project state (all runs)", "",
        f"These totals cover **all {c['runs']} runs together**, not "
        f"{data.run_id}. They are here for context and are not this run's "
        "results.", "",
        "| Measure | All runs |", "|---|---:|",
        f"| Discovery runs | {c['runs']:,} |",
        f"| Discovery queries executed | {c['queries']:,} |",
        f"| Unique repositories discovered | {c['candidates']:,} |",
        f"| Repositories evidence-enriched and qualified | {c['enriched']:,} |",
        f"| Repositories scored | {c['scored']:,} |",
        "",
        "Unique repositories is a deduplicated count: a repository found by "
        "more than one run is one row, not two.", "",
    ]


def render_markdown(data: ReportData) -> str:
    heading = (
        f"# Dependency Map - {data.run_id}" if data.run_id else "# Dependency Map"
    )
    lines = [heading, ""]
    lines += _render_executive_summary(data)
    lines += _render_sampling(data)
    lines += _render_maintenance_scope(data)
    lines += _render_ranked_table(data)

    lines += ["## Candidate details", ""]
    if not data.ranked:
        lines += ["No qualified, scored candidates to detail.", ""]
    else:
        for candidate in data.ranked:
            lines += _render_candidate_detail(candidate)

    lines += _render_query_method(data)
    lines += _render_zero_result_queries(data)
    lines += _render_cumulative(data)
    lines += _render_run_information(data)
    lines += _render_reproducibility(data)

    return "\n".join(lines).rstrip() + "\n"


# --- entry point -----------------------------------------------------------


def write_report(
    conn, csv_path: Path | str, markdown_path: Path | str,
    run_id: str | None = None,
) -> ReportSummary:
    """Generate both files from the current database state and write them.

    The only side effect is writing these two files. Nothing is written back
    to the database, and no other module's data-fetching logic is duplicated
    here: everything comes from the storage layer's own read functions.
    """
    csv_path = Path(csv_path)
    markdown_path = Path(markdown_path)

    try:
        data = gather_report_data(conn, run_id)
    except Exception as exc:  # pragma: no cover - defensive, re-raised typed
        raise ReportError(f"Could not read report data from the database: {exc}") from exc

    csv_text = render_csv(data)
    markdown_text = render_markdown(data)

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.write_text(csv_text, encoding="utf-8", newline="")
    markdown_path.write_text(markdown_text, encoding="utf-8")

    return ReportSummary(
        csv_path=csv_path,
        markdown_path=markdown_path,
        ranked_count=data.scored_count,
        keep_count=data.keep_count,
        investigate_count=data.investigate_count,
        reject_count=data.reject_count,
        total_queries=len(data.all_queries),
        capped_queries=len(data.capped_queries),
        zero_result_queries=len(data.zero_result_queries),
    )
