"""Persistence operations for every table in the schema.

All database access lives here or in db.py. Nothing else in the package issues
SQL. Every statement is parameterized; no query is assembled from caller-
supplied values.

Functions take an open connection as their first argument rather than opening
one themselves, so a caller can group several writes into a single transaction
(the connection context manager in db.py commits once, on clean exit).

Rows come back as sqlite3.Row, which supports both index and key access.
Typed dataclasses are deferred to the phase that first needs them.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
from typing import Any, Sequence

from .db import SCORING_DIMENSIONS, utcnow

#: GitHub returns at most this many results for any single search, however it
#: is paginated. A query whose total exceeds it can never be fully retrieved.
SEARCH_RESULT_CEILING = 1000


def _bool(value: Any) -> int:
    """Store booleans as SQLite integers."""
    return 1 if value else 0


def _encode_unknown_dimensions(dimensions: Sequence[str] | None) -> str:
    """Serialize the unknown-dimension list, rejecting unrecognized names.

    SCORING_MODEL.md section 12 is explicit that an unknown dimension scores 0
    and is neither dropped nor redistributed. This field is what lets the
    report show that gap instead of hiding it, so a typo in a dimension name
    would quietly defeat the point.
    """
    if not dimensions:
        return "[]"
    unknown = [d for d in dimensions if d not in SCORING_DIMENSIONS]
    if unknown:
        raise ValueError(
            f"Not scoring dimensions: {unknown}. "
            f"Expected any of {list(SCORING_DIMENSIONS)}."
        )
    # Store in the canonical document order rather than call order, so two
    # candidates with the same unknowns produce identical strings.
    ordered = [d for d in SCORING_DIMENSIONS if d in set(dimensions)]
    return json.dumps(ordered)


def decode_unknown_dimensions(raw: str) -> list[str]:
    """Read scores.unknown_dimensions back into a list."""
    return list(json.loads(raw))


# --- runs ------------------------------------------------------------------


def create_run(
    conn: sqlite3.Connection,
    run_id: str,
    *,
    started_at: str | None = None,
    notes: str | None = None,
) -> None:
    conn.execute(
        "INSERT INTO runs (run_id, started_at, finished_at, notes) "
        "VALUES (?, ?, NULL, ?)",
        (run_id, started_at or utcnow(), notes),
    )


def finish_run(
    conn: sqlite3.Connection, run_id: str, *, finished_at: str | None = None
) -> None:
    conn.execute(
        "UPDATE runs SET finished_at = ? WHERE run_id = ?",
        (finished_at or utcnow(), run_id),
    )


def get_run(conn: sqlite3.Connection, run_id: str) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM runs WHERE run_id = ?", (run_id,)
    ).fetchone()


def list_runs(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return conn.execute("SELECT * FROM runs ORDER BY started_at").fetchall()


# --- candidates ------------------------------------------------------------

_CANDIDATE_COLUMNS = (
    "candidate_id",
    "repo_url",
    "repo_owner",
    "repo_name",
    "is_fork",
    "is_archived",
    "primary_language",
    "company_name",
    "company_name_source",
    "product_name",
    "website_url",
    "industry_category",
    "first_seen_run_id",
)


def insert_candidate_if_new(
    conn: sqlite3.Connection,
    *,
    candidate_id: str,
    repo_url: str,
    repo_owner: str,
    repo_name: str,
    is_fork: bool | None = None,
    is_archived: bool | None = None,
    primary_language: str | None = None,
    company_name: str | None = None,
    company_name_source: str | None = None,
    product_name: str | None = None,
    website_url: str | None = None,
    industry_category: str | None = None,
    first_seen_run_id: str | None = None,
) -> bool:
    """Insert a candidate, or do nothing if that candidate_id already exists.

    Returns True when a row was created, False when the candidate was already
    known. A repeat sighting is recorded as a discovery_evidence row by the
    caller, never as a second candidate (TECHNICAL_DESIGN.md section 8).
    """
    cursor = conn.execute(
        "INSERT INTO candidates ("
        "candidate_id, repo_url, repo_owner, repo_name, is_fork, is_archived, "
        "primary_language, company_name, company_name_source, product_name, "
        "website_url, industry_category, first_seen_run_id"
        ") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(candidate_id) DO NOTHING",
        (
            candidate_id,
            repo_url,
            repo_owner,
            repo_name,
            None if is_fork is None else _bool(is_fork),
            None if is_archived is None else _bool(is_archived),
            primary_language,
            company_name,
            company_name_source,
            product_name,
            website_url,
            industry_category,
            first_seen_run_id,
        ),
    )
    return cursor.rowcount > 0


def get_candidate(
    conn: sqlite3.Connection, candidate_id: str
) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM candidates WHERE candidate_id = ?", (candidate_id,)
    ).fetchone()


def get_candidate_by_repo_url(
    conn: sqlite3.Connection, repo_url: str
) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM candidates WHERE repo_url = ?", (repo_url,)
    ).fetchone()


def update_candidate_identity(
    conn: sqlite3.Connection, candidate_id: str, **fields: Any
) -> None:
    """Fill in identity fields discovered after the candidate was created.

    Only the columns named in _CANDIDATE_COLUMNS may be set, and the primary
    key and repo_url are not rewritable. Column names are validated against
    that allowlist rather than interpolated from caller input.
    """
    immutable = {"candidate_id", "repo_url"}
    invalid = [k for k in fields if k not in _CANDIDATE_COLUMNS or k in immutable]
    if invalid:
        raise ValueError(f"Not updatable candidate columns: {invalid}")
    if not fields:
        return
    for key in ("is_fork", "is_archived"):
        if fields.get(key) is not None:
            fields[key] = _bool(fields[key])
    assignments = ", ".join(f"{name} = ?" for name in fields)
    conn.execute(
        f"UPDATE candidates SET {assignments} WHERE candidate_id = ?",
        (*fields.values(), candidate_id),
    )


def count_candidates(conn: sqlite3.Connection) -> int:
    return int(conn.execute("SELECT COUNT(*) FROM candidates").fetchone()[0])


# --- discovery_queries -----------------------------------------------------


def make_query_id(run_id: str, query: str, search_window: str | None) -> str:
    """Deterministic id for one query execution.

    Derived from the run, the query text and the slice, so re-running the same
    slice within a run resolves to the same row instead of duplicating it.
    That is what lets the discovery stage resume without redoing work.
    """
    payload = json.dumps([run_id, query, search_window], separators=(",", ":"))
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
    return f"q_{digest}"


def create_discovery_query(
    conn: sqlite3.Connection,
    *,
    run_id: str,
    discovery_source: str,
    query: str,
    query_id: str | None = None,
    library_name: str | None = None,
    discovery_tier: int | None = None,
    total_count: int | None = None,
    capped: bool | None = None,
    search_window: str | None = None,
    returned_count: int = 0,
    executed_at: str | None = None,
) -> str:
    """Record a query execution. Returns its query_id.

    Written whether or not the query found anything: a zero-result execution
    is a finding, not an absence worth discarding.
    """
    query_id = query_id or make_query_id(run_id, query, search_window)
    conn.execute(
        "INSERT INTO discovery_queries ("
        "query_id, run_id, discovery_source, library_name, discovery_tier, "
        "query, total_count, capped, search_window, returned_count, executed_at"
        ") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(query_id) DO UPDATE SET "
        "total_count = excluded.total_count, "
        "capped = excluded.capped, "
        "returned_count = excluded.returned_count, "
        "executed_at = excluded.executed_at",
        (
            query_id,
            run_id,
            discovery_source,
            library_name,
            discovery_tier,
            query,
            total_count,
            None if capped is None else _bool(capped),
            search_window,
            int(returned_count),
            executed_at or utcnow(),
        ),
    )
    return query_id


def update_query_results(
    conn: sqlite3.Connection,
    query_id: str,
    *,
    total_count: int | None,
    returned_count: int,
    capped: bool | None = None,
) -> None:
    """Fill in what a query actually returned, once it has run.

    `capped` is derived rather than passed when omitted, so the definition
    lives in one place: it is true when the total exceeds GitHub's 1,000
    pagination ceiling, which is a statement about the query's whole result
    set, not about how many rows were fetched.
    """
    if capped is None and total_count is not None:
        capped = total_count > SEARCH_RESULT_CEILING
    conn.execute(
        "UPDATE discovery_queries SET total_count = ?, returned_count = ?, "
        "capped = ? WHERE query_id = ?",
        (
            total_count,
            int(returned_count),
            None if capped is None else _bool(capped),
            query_id,
        ),
    )


def completed_query_ids(conn: sqlite3.Connection, run_id: str) -> set[str]:
    """Query ids this run already executed and got an answer for.

    "Completed" means `total_count` is filled in. A query that failed leaves it
    null on purpose, so a retry is not mistaken for redundant work, and a query
    that genuinely returned nothing has a zero rather than a null and is not
    retried. This is what lets an interrupted discovery stage resume without
    paying for the queries it already ran.
    """
    rows = conn.execute(
        "SELECT query_id FROM discovery_queries "
        "WHERE run_id = ? AND total_count IS NOT NULL",
        (run_id,),
    ).fetchall()
    return {row["query_id"] for row in rows}


def get_discovery_query(
    conn: sqlite3.Connection, query_id: str
) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM discovery_queries WHERE query_id = ?", (query_id,)
    ).fetchone()


def list_queries_for_run(
    conn: sqlite3.Connection, run_id: str
) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT * FROM discovery_queries WHERE run_id = ? ORDER BY executed_at, query_id",
        (run_id,),
    ).fetchall()


def count_queries_for_run(conn: sqlite3.Connection, run_id: str) -> int:
    return int(
        conn.execute(
            "SELECT COUNT(*) FROM discovery_queries WHERE run_id = ?", (run_id,)
        ).fetchone()[0]
    )


# --- discovery_evidence ----------------------------------------------------


def insert_discovery_evidence(
    conn: sqlite3.Connection,
    *,
    query_id: str,
    candidate_id: str,
    discovery_result_rank: int | None = None,
    file_path: str | None = None,
    evidence_url: str | None = None,
) -> int | None:
    """Record that a query surfaced this candidate.

    Returns the new row id, or None when this query already recorded this
    candidate. One query returning the same repository twice, at two file
    paths, is one hit; that collapse is why returned_count is tracked on the
    query rather than inferred from these rows.
    """
    cursor = conn.execute(
        "INSERT INTO discovery_evidence ("
        "query_id, candidate_id, discovery_result_rank, file_path, evidence_url"
        ") VALUES (?, ?, ?, ?, ?) "
        "ON CONFLICT(query_id, candidate_id) DO NOTHING",
        (query_id, candidate_id, discovery_result_rank, file_path, evidence_url),
    )
    return int(cursor.lastrowid) if cursor.rowcount > 0 else None


def list_discovery_evidence_for_query(
    conn: sqlite3.Connection, query_id: str
) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT * FROM discovery_evidence WHERE query_id = ? ORDER BY id",
        (query_id,),
    ).fetchall()


def list_discovery_evidence_for_candidate(
    conn: sqlite3.Connection, candidate_id: str
) -> list[sqlite3.Row]:
    """Every hit for this candidate, joined to the query that produced it.

    The join is the point: query facts live in one place, so a caller reading
    a candidate's discovery history still sees the query, source and run
    without those being copied onto every row.
    """
    return conn.execute(
        "SELECT e.*, q.run_id, q.query, q.discovery_source, q.discovery_tier, "
        "       q.search_window, q.executed_at AS discovered_at "
        "FROM discovery_evidence e "
        "JOIN discovery_queries q ON q.query_id = e.query_id "
        "WHERE e.candidate_id = ? ORDER BY e.id",
        (candidate_id,),
    ).fetchall()


def list_candidate_ids_for_run(
    conn: sqlite3.Connection, run_id: str
) -> list[str]:
    """Every candidate_id this run surfaced, new or already known."""
    rows = conn.execute(
        "SELECT DISTINCT e.candidate_id FROM discovery_evidence e "
        "JOIN discovery_queries q ON q.query_id = e.query_id "
        "WHERE q.run_id = ? ORDER BY e.candidate_id",
        (run_id,),
    ).fetchall()
    return [row["candidate_id"] for row in rows]


def candidate_ids_discovered_before_run(
    conn: sqlite3.Connection, run_id: str
) -> set[str]:
    """Every candidate surfaced by a run that started before this one.

    Ordered by `runs.started_at` rather than by run_id, so the answer doesn't
    depend on how runs happen to be named. This is what the "new candidates"
    count subtracts, and it is derived on read rather than tracked as a flag,
    so it cannot drift from what was actually recorded.
    """
    rows = conn.execute(
        "SELECT DISTINCT e.candidate_id "
        "FROM discovery_evidence e "
        "JOIN discovery_queries q ON q.query_id = e.query_id "
        "JOIN runs earlier      ON earlier.run_id = q.run_id "
        "JOIN runs current      ON current.run_id = ? "
        "WHERE earlier.run_id <> current.run_id "
        "  AND earlier.started_at < current.started_at",
        (run_id,),
    ).fetchall()
    return {row["candidate_id"] for row in rows}


def query_signatures_for_run(
    conn: sqlite3.Connection, run_id: str
) -> set[tuple[str, str | None]]:
    """The (query, slice) pairs this run executed."""
    rows = conn.execute(
        "SELECT query, search_window FROM discovery_queries WHERE run_id = ?",
        (run_id,),
    ).fetchall()
    return {(row["query"], row["search_window"]) for row in rows}


def query_signatures_before_run(
    conn: sqlite3.Connection, run_id: str
) -> set[tuple[str, str | None]]:
    """Every (query, slice) pair an earlier run already executed.

    What the fresh-batch check compares a planned query set against.
    """
    rows = conn.execute(
        "SELECT q.query, q.search_window "
        "FROM discovery_queries q "
        "JOIN runs earlier ON earlier.run_id = q.run_id "
        "JOIN runs current ON current.run_id = ? "
        "WHERE earlier.run_id <> current.run_id "
        "  AND earlier.started_at < current.started_at",
        (run_id,),
    ).fetchall()
    return {(row["query"], row["search_window"]) for row in rows}


def run_query_totals(conn: sqlite3.Connection, run_id: str) -> dict[str, int]:
    """Aggregate query-level counts for one run.

    A failed query is told apart from a genuinely empty one by `total_count`
    being null rather than zero, so a failure is never reported as a query that
    simply found nothing.
    """
    row = conn.execute(
        "SELECT "
        "  COUNT(*)                                            AS total_queries, "
        "  SUM(total_count IS NOT NULL)                        AS queries_executed, "
        "  SUM(total_count IS NULL)                            AS queries_failed, "
        "  SUM(total_count = 0)                                AS zero_result_queries, "
        "  SUM(COALESCE(capped, 0))                            AS capped_queries, "
        "  COALESCE(SUM(returned_count), 0)                    AS raw_results "
        "FROM discovery_queries WHERE run_id = ?",
        (run_id,),
    ).fetchone()
    return {key: int(row[key] or 0) for key in row.keys()}


def list_ranked_candidates(
    conn: sqlite3.Connection, run_id: str | None = None
) -> list[sqlite3.Row]:
    """Every candidate eligible for the ranked table: keep or investigate, with
    a score row.

    A reject is excluded by the join itself, not filtered afterwards: it has
    no row in `scores` at all (SCORING_MODEL.md section 1), so an inner join
    against `scores` already removes it. The `qualification_status` filter is
    kept anyway as a second, explicit guard, since the report is the last
    place a rejected candidate must never surface.

    Ordered by `final_score` descending. Ties break on `confidence_band`
    (high, then medium, then low) and then on `candidate_id` ascending, so the
    ranking is fully deterministic and reproducible from the same data.

    With `run_id`, only candidates that run surfaced are returned. A report for
    one run has to describe that run: showing every candidate the database has
    ever scored invites a reader to attribute another run's results to this
    one. Candidates an earlier run also surfaced stay in, because this run did
    genuinely find them again - `candidates.first_seen_run_id` is what
    distinguishes those from the ones it found first.
    """
    scope = (
        " AND EXISTS (SELECT 1 FROM discovery_evidence de "
        "             JOIN discovery_queries dq ON dq.query_id = de.query_id "
        "             WHERE de.candidate_id = c.candidate_id "
        "               AND dq.run_id = ?)"
        if run_id
        else ""
    )
    params = (run_id,) if run_id else ()
    return conn.execute(
        "SELECT c.*, "
        "       q.qualification_status, q.qualification_reason, "
        "       q.rejection_reason, q.confidence AS qualification_confidence, "
        "       s.document_volume, s.document_complexity, "
        "       s.business_criticality, s.pipeline_complexity, "
        "       s.maintenance_burden, s.build_vs_buy_signal, "
        "       s.commercial_leverage, s.raw_weighted_score, s.final_score, "
        "       s.confidence_band, s.unknown_dimensions, s.gate_cap_applied "
        "FROM scores s "
        "JOIN qualification q ON q.candidate_id = s.candidate_id "
        "JOIN candidates c ON c.candidate_id = s.candidate_id "
        "WHERE q.qualification_status IN ('keep', 'investigate')"
        + scope
        + " ORDER BY s.final_score DESC, "
        "         CASE s.confidence_band "
        "           WHEN 'high' THEN 3 WHEN 'medium' THEN 2 WHEN 'low' THEN 1 "
        "           ELSE 0 END DESC, "
        "         c.candidate_id ASC",
        params,
    ).fetchall()


def list_all_discovery_queries(
    conn: sqlite3.Connection, run_id: str | None = None
) -> list[sqlite3.Row]:
    """Query executions, across every run or scoped to one.

    Used for the report's coverage aggregates (total queries, capped queries,
    zero-result queries). Passing `run_id` keeps those aggregates describing
    the run being reported rather than the whole database.
    """
    if run_id:
        return conn.execute(
            "SELECT * FROM discovery_queries WHERE run_id = ? "
            "ORDER BY executed_at, query_id",
            (run_id,),
        ).fetchall()
    return conn.execute(
        "SELECT * FROM discovery_queries ORDER BY run_id, executed_at, query_id"
    ).fetchall()


def run_candidate_counts(conn: sqlite3.Connection, run_id: str) -> dict:
    """What one run surfaced, split into what it found first and what it saw
    again.

    `first_seen_run_id` is the only provenance the schema carries, and it is
    enough: a candidate whose first sighting was an earlier run had its
    evidence collected then, not now.
    """
    surfaced = conn.execute(
        "SELECT COUNT(DISTINCT de.candidate_id) FROM discovery_evidence de "
        "JOIN discovery_queries q ON q.query_id = de.query_id "
        "WHERE q.run_id = ?",
        (run_id,),
    ).fetchone()[0]
    new = conn.execute(
        "SELECT COUNT(*) FROM candidates WHERE first_seen_run_id = ?", (run_id,)
    ).fetchone()[0]
    enriched = conn.execute(
        "SELECT COUNT(DISTINCT de.candidate_id) FROM discovery_evidence de "
        "JOIN discovery_queries q ON q.query_id = de.query_id "
        "JOIN qualification g ON g.candidate_id = de.candidate_id "
        "WHERE q.run_id = ?",
        (run_id,),
    ).fetchone()[0]
    return {
        "surfaced": int(surfaced),
        "new": int(new),
        "previously_seen": int(surfaced) - int(new),
        "enriched": int(enriched),
    }


def cumulative_counts(conn: sqlite3.Connection) -> dict:
    """Project-wide totals, for the section that says so explicitly."""
    one = lambda sql: int(conn.execute(sql).fetchone()[0])
    return {
        "runs": one("SELECT COUNT(*) FROM runs"),
        "candidates": one("SELECT COUNT(*) FROM candidates"),
        "queries": one("SELECT COUNT(*) FROM discovery_queries"),
        "enriched": one("SELECT COUNT(*) FROM qualification"),
        "scored": one("SELECT COUNT(*) FROM scores"),
    }


def candidates_needing_evidence(conn: sqlite3.Connection) -> list[str]:
    """Candidates with a discovery hit but no evidence rows yet.

    This is the whole resumability mechanism (TECHNICAL_DESIGN.md section 16):
    the stage asks what is missing rather than being handed a resume pointer,
    so an interrupted run picks up exactly where it stopped without any
    separate bookkeeping to keep in sync.
    """
    rows = conn.execute(
        "SELECT DISTINCT e.candidate_id "
        "FROM discovery_evidence e "
        "LEFT JOIN pipeline_evidence p ON p.candidate_id = e.candidate_id "
        "LEFT JOIN business_evidence b ON b.candidate_id = e.candidate_id "
        "WHERE p.candidate_id IS NULL OR b.candidate_id IS NULL "
        "ORDER BY e.candidate_id"
    ).fetchall()
    return [row["candidate_id"] for row in rows]


def candidates_needing_qualification(conn: sqlite3.Connection) -> list[str]:
    """Candidates with evidence collected but no qualification decision yet.

    Same query-what-is-missing pattern as the evidence stage, so rerunning
    qualification after a rule change simply reprocesses whatever has no row.
    """
    rows = conn.execute(
        "SELECT p.candidate_id "
        "FROM pipeline_evidence p "
        "JOIN business_evidence b ON b.candidate_id = p.candidate_id "
        "LEFT JOIN qualification q ON q.candidate_id = p.candidate_id "
        "WHERE q.candidate_id IS NULL "
        "ORDER BY p.candidate_id"
    ).fetchall()
    return [row["candidate_id"] for row in rows]


def candidates_needing_scoring(conn: sqlite3.Connection) -> list[str]:
    """Keep and investigate candidates with no score row yet.

    Rejects are excluded by the join, not filtered afterwards, so a rejected
    candidate cannot acquire a score row by being rescored later. That is
    SCORING_MODEL.md section 1's hard rule expressed as a query: a rejection
    should exclude a candidate from ranking entirely rather than produce a
    misleadingly low number.
    """
    rows = conn.execute(
        "SELECT q.candidate_id FROM qualification q "
        "LEFT JOIN scores s ON s.candidate_id = q.candidate_id "
        "WHERE q.qualification_status IN ('keep', 'investigate') "
        "  AND s.candidate_id IS NULL "
        "ORDER BY q.candidate_id"
    ).fetchall()
    return [row["candidate_id"] for row in rows]


def libraries_that_surfaced_candidate(
    conn: sqlite3.Connection, candidate_id: str
) -> list[str]:
    """Which library-universe entries' queries found this candidate.

    Co-occurrence queries carry no library name and are excluded here, since
    attributing them to one library would be a fiction.
    """
    rows = conn.execute(
        "SELECT DISTINCT q.library_name "
        "FROM discovery_evidence e "
        "JOIN discovery_queries q ON q.query_id = e.query_id "
        "WHERE e.candidate_id = ? AND q.library_name IS NOT NULL "
        "ORDER BY q.library_name",
        (candidate_id,),
    ).fetchall()
    return [row["library_name"] for row in rows]


def all_discovered_candidate_ids(conn: sqlite3.Connection) -> set[str]:
    """Every candidate_id ever surfaced, across all runs.

    Phase 7 builds the full fresh-batch behaviour on top of this; discovery
    only needs it to avoid creating a duplicate candidate row.
    """
    rows = conn.execute(
        "SELECT DISTINCT candidate_id FROM discovery_evidence"
    ).fetchall()
    return {row["candidate_id"] for row in rows}


# --- dependencies_found ----------------------------------------------------


def insert_dependency_found(
    conn: sqlite3.Connection,
    *,
    candidate_id: str,
    library_name: str,
    library_category: str,
    direction: str,
    detection_method: str,
    evidence_url: str,
    manifest_file: str | None = None,
) -> int | None:
    """Record one located library. Returns the row id, or None if already known.

    The same library found the same way at the same URL is one fact, not two,
    so a repeat insert is ignored rather than duplicated.
    """
    cursor = conn.execute(
        "INSERT INTO dependencies_found ("
        "candidate_id, library_name, library_category, direction, "
        "manifest_file, detection_method, evidence_url"
        ") VALUES (?, ?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(candidate_id, library_name, detection_method, evidence_url) "
        "DO NOTHING",
        (
            candidate_id,
            library_name,
            library_category,
            direction,
            manifest_file,
            detection_method,
            evidence_url,
        ),
    )
    return int(cursor.lastrowid) if cursor.rowcount > 0 else None


def list_dependencies_for_candidate(
    conn: sqlite3.Connection, candidate_id: str
) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT * FROM dependencies_found WHERE candidate_id = ? ORDER BY id",
        (candidate_id,),
    ).fetchall()


# --- pipeline_evidence -----------------------------------------------------


def upsert_pipeline_evidence(
    conn: sqlite3.Connection,
    *,
    candidate_id: str,
    code_usage_confirmed: bool,
    template_directory_present: bool,
    multiple_document_types_handled: bool,
    pipeline_stage_count: int,
    infrastructure_service_present: bool,
    infrastructure_reference_present: bool | None = None,
    pipeline_evidence_notes: str | None = None,
) -> None:
    conn.execute(
        "INSERT INTO pipeline_evidence ("
        "candidate_id, code_usage_confirmed, template_directory_present, "
        "multiple_document_types_handled, pipeline_stage_count, "
        "infrastructure_service_present, infrastructure_reference_present, "
        "pipeline_evidence_notes"
        ") VALUES (?, ?, ?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(candidate_id) DO UPDATE SET "
        "code_usage_confirmed = excluded.code_usage_confirmed, "
        "template_directory_present = excluded.template_directory_present, "
        "multiple_document_types_handled = excluded.multiple_document_types_handled, "
        "pipeline_stage_count = excluded.pipeline_stage_count, "
        "infrastructure_service_present = excluded.infrastructure_service_present, "
        "infrastructure_reference_present = excluded.infrastructure_reference_present, "
        "pipeline_evidence_notes = excluded.pipeline_evidence_notes",
        (
            candidate_id,
            _bool(code_usage_confirmed),
            _bool(template_directory_present),
            _bool(multiple_document_types_handled),
            int(pipeline_stage_count),
            _bool(infrastructure_service_present),
            None if infrastructure_reference_present is None
                 else _bool(infrastructure_reference_present),
            pipeline_evidence_notes,
        ),
    )


def get_pipeline_evidence(
    conn: sqlite3.Connection, candidate_id: str
) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM pipeline_evidence WHERE candidate_id = ?",
        (candidate_id,),
    ).fetchone()


# --- business_evidence -----------------------------------------------------


def upsert_business_evidence(
    conn: sqlite3.Connection,
    *,
    candidate_id: str,
    readme_describes_product: bool,
    website_exists: bool,
    application_code_exists: bool,
    document_functionality_in_production_code: bool,
    readme_excerpt: str | None = None,
    stars: int | None = None,
    last_commit_date: str | None = None,
    contributor_count: int | None = None,
    is_catalogue_repository: bool | None = None,
    readme_indicates_example_or_tutorial: bool | None = None,
    has_examples_directory: bool | None = None,
    business_evidence_notes: str | None = None,
) -> None:
    """Store the business-evidence fields.

    The schema refuses readme_describes_product = true without a non-empty
    readme_excerpt, per CANDIDATE_SCHEMA.md section 6.
    """
    conn.execute(
        "INSERT INTO business_evidence ("
        "candidate_id, readme_describes_product, readme_excerpt, "
        "website_exists, application_code_exists, "
        "document_functionality_in_production_code, stars, last_commit_date, "
        "contributor_count, is_catalogue_repository, "
        "readme_indicates_example_or_tutorial, has_examples_directory, "
        "business_evidence_notes"
        ") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(candidate_id) DO UPDATE SET "
        "readme_describes_product = excluded.readme_describes_product, "
        "readme_excerpt = excluded.readme_excerpt, "
        "website_exists = excluded.website_exists, "
        "application_code_exists = excluded.application_code_exists, "
        "document_functionality_in_production_code = "
        "    excluded.document_functionality_in_production_code, "
        "stars = excluded.stars, "
        "last_commit_date = excluded.last_commit_date, "
        "contributor_count = excluded.contributor_count, "
        "is_catalogue_repository = excluded.is_catalogue_repository, "
        "readme_indicates_example_or_tutorial = "
        "    excluded.readme_indicates_example_or_tutorial, "
        "has_examples_directory = excluded.has_examples_directory, "
        "business_evidence_notes = excluded.business_evidence_notes",
        (
            candidate_id,
            _bool(readme_describes_product),
            readme_excerpt,
            _bool(website_exists),
            _bool(application_code_exists),
            _bool(document_functionality_in_production_code),
            stars,
            last_commit_date,
            contributor_count,
            None if is_catalogue_repository is None else _bool(is_catalogue_repository),
            None if readme_indicates_example_or_tutorial is None
                 else _bool(readme_indicates_example_or_tutorial),
            None if has_examples_directory is None else _bool(has_examples_directory),
            business_evidence_notes,
        ),
    )


def get_business_evidence(
    conn: sqlite3.Connection, candidate_id: str
) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM business_evidence WHERE candidate_id = ?",
        (candidate_id,),
    ).fetchone()


# --- qualification ---------------------------------------------------------


def upsert_qualification(
    conn: sqlite3.Connection,
    *,
    candidate_id: str,
    qualification_status: str,
    qualification_reason: str,
    confidence: str,
    rejection_reason: str | None = None,
) -> None:
    """Store a qualification decision.

    The schema enforces that rejection_reason is present for a reject and
    absent otherwise (CANDIDATE_SCHEMA.md section 7).

    A reject also clears any score already written for that candidate. The
    invariant is that a rejected candidate has no score row, and re-qualifying
    is the moment it can be broken: a candidate scored under earlier evidence
    can become a reject once better evidence arrives, and the old score would
    otherwise linger. Phase 14 hit exactly that - thirteen candidates moved to
    reject on corrected infrastructure evidence and kept their scores.

    Doing it here rather than in the scoring engine is deliberate. This is the
    one place a qualification decision is written, so every path that rejects
    a candidate cleans up, and repeating the call changes nothing.
    """
    conn.execute(
        "INSERT INTO qualification ("
        "candidate_id, qualification_status, qualification_reason, "
        "rejection_reason, confidence"
        ") VALUES (?, ?, ?, ?, ?) "
        "ON CONFLICT(candidate_id) DO UPDATE SET "
        "qualification_status = excluded.qualification_status, "
        "qualification_reason = excluded.qualification_reason, "
        "rejection_reason = excluded.rejection_reason, "
        "confidence = excluded.confidence",
        (
            candidate_id,
            qualification_status,
            qualification_reason,
            rejection_reason,
            confidence,
        ),
    )
    if qualification_status == "reject":
        delete_score(conn, candidate_id)


def delete_score(conn: sqlite3.Connection, candidate_id: str) -> int:
    """Remove a candidate's score row. Returns how many rows went.

    Safe to call when there is nothing to delete, which is what makes the
    reject cleanup idempotent.
    """
    cursor = conn.execute(
        "DELETE FROM scores WHERE candidate_id = ?", (candidate_id,)
    )
    return int(cursor.rowcount)


def get_qualification(
    conn: sqlite3.Connection, candidate_id: str
) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM qualification WHERE candidate_id = ?", (candidate_id,)
    ).fetchone()


def list_candidates_by_status(
    conn: sqlite3.Connection, status: str
) -> list[str]:
    rows = conn.execute(
        "SELECT candidate_id FROM qualification "
        "WHERE qualification_status = ? ORDER BY candidate_id",
        (status,),
    ).fetchall()
    return [row["candidate_id"] for row in rows]


# --- scores ----------------------------------------------------------------


def upsert_score(
    conn: sqlite3.Connection,
    *,
    candidate_id: str,
    document_volume: int,
    document_complexity: int,
    business_criticality: int,
    pipeline_complexity: int,
    maintenance_burden: int,
    build_vs_buy_signal: int,
    commercial_leverage: int,
    raw_weighted_score: float,
    final_score: int,
    confidence_band: str,
    unknown_dimensions: Sequence[str] | None = None,
    gate_cap_applied: int | None = None,
) -> None:
    """Store a candidate's seven dimension scores and the derived totals.

    unknown_dimensions names the dimensions that defaulted to 0 for lack of
    evidence. It is stored, not inferred, so the report can label them
    explicitly rather than presenting a bare number that hides the gap.
    """
    conn.execute(
        "INSERT INTO scores ("
        "candidate_id, document_volume, document_complexity, "
        "business_criticality, pipeline_complexity, maintenance_burden, "
        "build_vs_buy_signal, commercial_leverage, raw_weighted_score, "
        "final_score, confidence_band, gate_cap_applied, unknown_dimensions"
        ") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(candidate_id) DO UPDATE SET "
        "document_volume = excluded.document_volume, "
        "document_complexity = excluded.document_complexity, "
        "business_criticality = excluded.business_criticality, "
        "pipeline_complexity = excluded.pipeline_complexity, "
        "maintenance_burden = excluded.maintenance_burden, "
        "build_vs_buy_signal = excluded.build_vs_buy_signal, "
        "commercial_leverage = excluded.commercial_leverage, "
        "raw_weighted_score = excluded.raw_weighted_score, "
        "final_score = excluded.final_score, "
        "confidence_band = excluded.confidence_band, "
        "gate_cap_applied = excluded.gate_cap_applied, "
        "unknown_dimensions = excluded.unknown_dimensions",
        (
            candidate_id,
            document_volume,
            document_complexity,
            business_criticality,
            pipeline_complexity,
            maintenance_burden,
            build_vs_buy_signal,
            commercial_leverage,
            raw_weighted_score,
            final_score,
            confidence_band,
            gate_cap_applied,
            _encode_unknown_dimensions(unknown_dimensions),
        ),
    )


def get_score(
    conn: sqlite3.Connection, candidate_id: str
) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM scores WHERE candidate_id = ?", (candidate_id,)
    ).fetchone()


def list_scores_ranked(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    """Every scored candidate, highest final_score first."""
    return conn.execute(
        "SELECT * FROM scores ORDER BY final_score DESC, candidate_id"
    ).fetchall()


# --- evidence_trail --------------------------------------------------------


def insert_evidence_trail(
    conn: sqlite3.Connection,
    *,
    candidate_id: str,
    evidence_url: str,
    evidence_type: str,
    source: str,
    evidence_excerpt: str | None = None,
    collected_at: str | None = None,
) -> int:
    cursor = conn.execute(
        "INSERT INTO evidence_trail ("
        "candidate_id, evidence_url, evidence_type, evidence_excerpt, "
        "source, collected_at"
        ") VALUES (?, ?, ?, ?, ?, ?)",
        (
            candidate_id,
            evidence_url,
            evidence_type,
            evidence_excerpt,
            source,
            collected_at or utcnow(),
        ),
    )
    return int(cursor.lastrowid)


def list_evidence_trail_for_candidate(
    conn: sqlite3.Connection, candidate_id: str
) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT * FROM evidence_trail WHERE candidate_id = ? ORDER BY id",
        (candidate_id,),
    ).fetchall()


# --- api_cache -------------------------------------------------------------


def put_api_cache(
    conn: sqlite3.Connection,
    *,
    cache_key: str,
    response_json: str,
    fetched_at: str | None = None,
) -> None:
    """Store a raw API response, replacing any earlier entry for that key.

    Written before the response is parsed into anything else, so a crashed run
    never re-spends rate-limit budget on data it already retrieved
    (TECHNICAL_DESIGN.md section 14). Freshness is the reliability layer's
    concern; this only stores fetched_at alongside the payload.
    """
    conn.execute(
        "INSERT INTO api_cache (cache_key, response_json, fetched_at) "
        "VALUES (?, ?, ?) "
        "ON CONFLICT(cache_key) DO UPDATE SET "
        "response_json = excluded.response_json, "
        "fetched_at = excluded.fetched_at",
        (cache_key, response_json, fetched_at or utcnow()),
    )


def get_api_cache(
    conn: sqlite3.Connection, cache_key: str
) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM api_cache WHERE cache_key = ?", (cache_key,)
    ).fetchone()


def delete_api_cache(conn: sqlite3.Connection, cache_key: str) -> bool:
    cursor = conn.execute(
        "DELETE FROM api_cache WHERE cache_key = ?", (cache_key,)
    )
    return cursor.rowcount > 0


# --- maintenance_evidence (schema 3) ---------------------------------------


def upsert_maintenance_evidence(
    conn: sqlite3.Connection,
    *,
    candidate_id: str,
    document_library_count: int,
    same_file_library_count: int,
    custom_logic_present: bool,
    custom_formatting_present: bool,
    custom_validation_present: bool,
    custom_error_handling_present: bool,
    custom_glue_excerpt: str | None = None,
    custom_glue_evidence_url: str | None = None,
    repeated_modification_evidence: bool | None = None,
    recent_commit_count: int | None = None,
    active_contributors: int | None = None,
    latest_commit_date: str | None = None,
    files_inspected: int = 0,
    maintenance_evidence_notes: str | None = None,
    collected_at: str | None = None,
) -> None:
    """Record the code-structure evidence SCORING_MODEL.md section 7 grades.

    The commit fields are optional on purpose: rung 4 is the only rung that
    mentions history, and only as corroboration. A row with code structure and
    no commit data is complete enough to score; a row with commit data and no
    code structure is not.
    """
    conn.execute(
        "INSERT INTO maintenance_evidence ("
        "candidate_id, document_library_count, same_file_library_count, "
        "custom_logic_present, custom_formatting_present, "
        "custom_validation_present, custom_error_handling_present, "
        "custom_glue_excerpt, custom_glue_evidence_url, "
        "repeated_modification_evidence, recent_commit_count, "
        "active_contributors, latest_commit_date, files_inspected, "
        "maintenance_evidence_notes, collected_at"
        ") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(candidate_id) DO UPDATE SET "
        "document_library_count = excluded.document_library_count, "
        "same_file_library_count = excluded.same_file_library_count, "
        "custom_logic_present = excluded.custom_logic_present, "
        "custom_formatting_present = excluded.custom_formatting_present, "
        "custom_validation_present = excluded.custom_validation_present, "
        "custom_error_handling_present = excluded.custom_error_handling_present, "
        "custom_glue_excerpt = excluded.custom_glue_excerpt, "
        "custom_glue_evidence_url = excluded.custom_glue_evidence_url, "
        "repeated_modification_evidence = excluded.repeated_modification_evidence, "
        "recent_commit_count = excluded.recent_commit_count, "
        "active_contributors = excluded.active_contributors, "
        "latest_commit_date = excluded.latest_commit_date, "
        "files_inspected = excluded.files_inspected, "
        "maintenance_evidence_notes = excluded.maintenance_evidence_notes, "
        "collected_at = excluded.collected_at",
        (
            candidate_id,
            int(document_library_count),
            int(same_file_library_count),
            _bool(custom_logic_present),
            _bool(custom_formatting_present),
            _bool(custom_validation_present),
            _bool(custom_error_handling_present),
            custom_glue_excerpt,
            custom_glue_evidence_url,
            None if repeated_modification_evidence is None
            else _bool(repeated_modification_evidence),
            recent_commit_count,
            active_contributors,
            latest_commit_date,
            int(files_inspected),
            maintenance_evidence_notes,
            collected_at or utcnow(),
        ),
    )


def get_maintenance_evidence(
    conn: sqlite3.Connection, candidate_id: str
) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM maintenance_evidence WHERE candidate_id = ?", (candidate_id,)
    ).fetchone()


def discovery_paths_for_candidate(
    conn: sqlite3.Connection, candidate_id: str
) -> list[sqlite3.Row]:
    """Files a discovery query actually matched in this repository.

    This is what lets the evidence collector open the exact file a hit came
    from instead of guessing at the repository root. Rows written before
    schema 3 carry a null path and are skipped by callers rather than treated
    as an absence of evidence.
    """
    return conn.execute(
        "SELECT de.file_path, de.evidence_url, q.discovery_tier, q.query, "
        "       q.library_name "
        "FROM discovery_evidence de "
        "JOIN discovery_queries q ON q.query_id = de.query_id "
        "WHERE de.candidate_id = ? AND de.file_path IS NOT NULL "
        "ORDER BY q.discovery_tier, de.file_path",
        (candidate_id,),
    ).fetchall()
