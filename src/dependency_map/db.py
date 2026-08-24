"""SQLite connection handling and schema setup.

The database is the working state of the pipeline, not an end-of-run export
(TECHNICAL_DESIGN.md section 16). Every stage commits as it completes, which is
what makes resumability fall out of the design rather than being a separate
feature.

Schema mirrors TECHNICAL_DESIGN.md section 3, which in turn mirrors
CANDIDATE_SCHEMA.md. One table per schema section.
"""

from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

# Bumped by hand whenever the DDL below changes. There is no migration tooling:
# a mismatch is a loud failure, not something the code repairs silently
# (IMPLEMENTATION_PLAN.md phase 2 task 3).
#
# 2: added discovery_queries, narrowed discovery_evidence to the candidate-hit
#    relationship, and replaced the hardcoded gate-cap constraint with a
#    nullable 0-100 range. See IMPLEMENTATION_PLAN.md phase 6, block A.
# 3: phase 14 evidence quality. discovery_evidence now keeps the file the hit
#    actually matched, which run 1 discarded and could not get back without
#    re-querying; pipeline_evidence separates "an infrastructure file was
#    found" from "the application actually uses that service"; business_evidence
#    carries structured repository-purpose signals; and maintenance_evidence
#    exists to make SCORING_MODEL.md section 7 computable from code structure.
SCHEMA_VERSION = 3

# Phase 3 replaces this with a configured path. Until the config system exists,
# callers pass a path explicitly and this is only the fallback.
DEFAULT_DB_PATH = Path("data") / "dependency_map.db"

# The seven scoring dimensions from SCORING_MODEL.md sections 3 through 9, in
# the order the document lists them. Used to validate scores.unknown_dimensions.
SCORING_DIMENSIONS: tuple[str, ...] = (
    "document_volume",
    "document_complexity",
    "business_criticality",
    "pipeline_complexity",
    "maintenance_burden",
    "build_vs_buy_signal",
    "commercial_leverage",
)


class SchemaVersionMismatch(RuntimeError):
    """The database on disk was built by a different version of this code."""


class DatabaseNotInitialized(RuntimeError):
    """The database file exists but has no schema_version table."""


# --- DDL -------------------------------------------------------------------
#
# Enum columns use CHECK constraints because SQLite has no enum type. The
# allowed values come from CANDIDATE_SCHEMA.md and are not restated anywhere
# else. Booleans are stored as INTEGER 0/1.
#
# A CHECK comparison against NULL evaluates to NULL rather than false, so
# nullable enum columns accept NULL without needing it spelled out.

SCHEMA_SQL = """
CREATE TABLE schema_version (
    id          INTEGER PRIMARY KEY CHECK (id = 1),
    version     INTEGER NOT NULL,
    applied_at  TEXT    NOT NULL
);

-- One row per discovery run. This is what makes the fresh-batch requirement
-- from SEARCH_STRATEGY.md section 7 enforceable.
CREATE TABLE runs (
    run_id      TEXT PRIMARY KEY,
    started_at  TEXT NOT NULL,
    finished_at TEXT,
    notes       TEXT
);

-- One row per unique repository, ever, across all runs.
CREATE TABLE candidates (
    candidate_id        TEXT PRIMARY KEY,
    repo_url            TEXT NOT NULL UNIQUE,
    repo_owner          TEXT NOT NULL,
    repo_name           TEXT NOT NULL,
    is_fork             INTEGER CHECK (is_fork IN (0, 1)),
    is_archived         INTEGER CHECK (is_archived IN (0, 1)),
    primary_language    TEXT,
    company_name        TEXT,
    company_name_source TEXT CHECK (company_name_source IN (
                            'readme', 'website_link', 'org_profile',
                            'external_search')),
    product_name        TEXT,
    website_url         TEXT,
    industry_category   TEXT CHECK (industry_category IN (
                            'legal_contracts', 'real_estate',
                            'healthcare_diagnostics', 'education',
                            'finance_investment', 'proposal_sales',
                            'events_weddings', 'software_technical_docs',
                            'other', 'unknown')),
    first_seen_run_id   TEXT REFERENCES runs(run_id),

    -- CANDIDATE_SCHEMA.md section 2: company_name_source is null if
    -- company_name is null.
    CHECK (company_name IS NOT NULL OR company_name_source IS NULL)
);

-- One row per query execution, whether or not it found anything.
--
-- A query is an entity in its own right: it has a total match count and a
-- coverage limitation that belong to the query rather than to any candidate it
-- happened to surface. It also has to be recorded when it surfaces nothing at
-- all. That is not hypothetical: the phase 6A experiment found an invalid
-- query in search-strategy.md precisely because a zero-result execution is
-- itself a finding, and a candidate-only model would have lost it.
CREATE TABLE discovery_queries (
    query_id         TEXT PRIMARY KEY,
    run_id           TEXT NOT NULL REFERENCES runs(run_id) ON DELETE CASCADE,
    discovery_source TEXT NOT NULL CHECK (discovery_source IN (
                         'github_code_search', 'github_dependents',
                         'github_repo_search', 'libraries_io',
                         'deps_dev', 'sourcegraph', 'manual')),
    -- Null for co-occurrence queries, which deliberately span more than one
    -- library.
    library_name     TEXT,
    discovery_tier   INTEGER CHECK (discovery_tier IN (1, 2, 3)),
    query            TEXT NOT NULL,
    -- Total matches the source reported, independent of how many were
    -- retrieved. Null when the source reports no total, as Libraries.io does.
    total_count      INTEGER,
    -- True when total_count exceeded GitHub's 1,000-result pagination ceiling.
    -- This says the query had more matches than can ever be retrieved; it does
    -- not mean 1,000 results were fetched, and in practice far fewer are.
    capped           INTEGER CHECK (capped IN (0, 1)),
    -- The slicing qualifier actually applied. Null means the query ran
    -- unsliced, not that the slice is unknown.
    search_window    TEXT,
    -- Raw results the API handed back. Allowed to exceed the number of
    -- discovery_evidence rows, since several hits can collapse onto one repo.
    returned_count   INTEGER NOT NULL DEFAULT 0 CHECK (returned_count >= 0),
    executed_at      TEXT NOT NULL,

    UNIQUE (run_id, query, search_window)
);

-- One row per candidate surfaced by a query. A candidate accumulates many of
-- these, one per query that found it, which is the mechanism dedup and
-- fresh-batch tracking read from.
--
-- Everything about the query is reached through query_id rather than repeated
-- on every hit, so there is one source of truth for what a query was and what
-- it covered. UNIQUE(query_id, candidate_id) means one query returning the
-- same repository twice, at two file paths, records one hit: that collapse is
-- exactly why returned_count is tracked separately.
CREATE TABLE discovery_evidence (
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    query_id              TEXT NOT NULL REFERENCES discovery_queries(query_id)
                              ON DELETE CASCADE,
    candidate_id          TEXT NOT NULL REFERENCES candidates(candidate_id)
                              ON DELETE CASCADE,
    discovery_result_rank INTEGER,
    -- The file the search actually matched, and its permalink. Null for rows
    -- written before schema 3, which did not record either; the evidence
    -- collector treats null as "unknown", never as "no file".
    file_path             TEXT,
    evidence_url          TEXT,

    UNIQUE (query_id, candidate_id)
);

CREATE TABLE dependencies_found (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id     TEXT NOT NULL REFERENCES candidates(candidate_id)
                         ON DELETE CASCADE,
    library_name     TEXT NOT NULL,
    library_category TEXT NOT NULL CHECK (library_category IN (
                         'docx', 'pdf', 'template_generation',
                         'conversion', 'other_processing')),
    direction        TEXT NOT NULL CHECK (direction IN (
                         'generation', 'extraction', 'conversion', 'mixed')),
    -- Null when the library was found through infrastructure evidence (a
    -- Dockerfile, a compose service) rather than a manifest.
    manifest_file    TEXT,
    detection_method TEXT NOT NULL CHECK (detection_method IN (
                         'manifest_declaration', 'code_import',
                         'infrastructure_reference')),
    evidence_url     TEXT NOT NULL,

    UNIQUE (candidate_id, library_name, detection_method, evidence_url)
);

-- The six fields from CANDIDATE_SCHEMA.md section 5. One row per candidate.
CREATE TABLE pipeline_evidence (
    candidate_id                    TEXT PRIMARY KEY
                                        REFERENCES candidates(candidate_id)
                                        ON DELETE CASCADE,
    code_usage_confirmed            INTEGER NOT NULL
                                        CHECK (code_usage_confirmed IN (0, 1)),
    template_directory_present      INTEGER NOT NULL
                                        CHECK (template_directory_present IN (0, 1)),
    multiple_document_types_handled INTEGER NOT NULL
                                        CHECK (multiple_document_types_handled IN (0, 1)),
    pipeline_stage_count            INTEGER NOT NULL
                                        CHECK (pipeline_stage_count >= 0),
    infrastructure_service_present  INTEGER NOT NULL
                                        CHECK (infrastructure_service_present IN (0, 1)),
    -- Deliberately separate from infrastructure_service_present. A compose
    -- file naming Gotenberg is a *reference*; a reference plus application code
    -- calling that service is *use*. Run 1 collapsed the two, so a catalogue
    -- repository listing hundreds of other people's services looked the same
    -- as a company running one. Null for rows written before schema 3.
    infrastructure_reference_present INTEGER
                                        CHECK (infrastructure_reference_present IN (0, 1)),
    pipeline_evidence_notes         TEXT
);

-- The nine fields from CANDIDATE_SCHEMA.md section 6. One row per candidate.
CREATE TABLE business_evidence (
    candidate_id                              TEXT PRIMARY KEY
                                                  REFERENCES candidates(candidate_id)
                                                  ON DELETE CASCADE,
    readme_describes_product                  INTEGER NOT NULL
                                                  CHECK (readme_describes_product IN (0, 1)),
    readme_excerpt                            TEXT,
    website_exists                            INTEGER NOT NULL
                                                  CHECK (website_exists IN (0, 1)),
    application_code_exists                   INTEGER NOT NULL
                                                  CHECK (application_code_exists IN (0, 1)),
    document_functionality_in_production_code INTEGER NOT NULL
                                                  CHECK (document_functionality_in_production_code IN (0, 1)),
    stars                                     INTEGER,
    last_commit_date                          TEXT,
    contributor_count                         INTEGER,
    -- Repository-purpose signals (phase 14). Evidence only: qualification does
    -- not branch on them yet. Null means "not assessed", which is not the same
    -- as false, and nothing may read a null as a negative finding.
    is_catalogue_repository                   INTEGER
                                                  CHECK (is_catalogue_repository IN (0, 1)),
    readme_indicates_example_or_tutorial      INTEGER
                                                  CHECK (readme_indicates_example_or_tutorial IN (0, 1)),
    has_examples_directory                    INTEGER
                                                  CHECK (has_examples_directory IN (0, 1)),
    business_evidence_notes                   TEXT,

    -- CANDIDATE_SCHEMA.md section 6: readme_describes_product "Requires a
    -- quoted excerpt to be set true".
    CHECK (readme_describes_product = 0
           OR (readme_excerpt IS NOT NULL AND TRIM(readme_excerpt) <> ''))
);

CREATE TABLE maintenance_evidence (
    candidate_id                 TEXT PRIMARY KEY
                                     REFERENCES candidates(candidate_id)
                                     ON DELETE CASCADE,

    -- SCORING_MODEL.md section 7 grades how much custom code surrounds the
    -- document libraries, not how busy the repository is. These first fields
    -- are what the rubric actually reads.
    document_library_count       INTEGER NOT NULL
                                     CHECK (document_library_count >= 0),
    same_file_library_count      INTEGER NOT NULL
                                     CHECK (same_file_library_count >= 0),
    custom_logic_present         INTEGER NOT NULL
                                     CHECK (custom_logic_present IN (0, 1)),
    custom_formatting_present    INTEGER NOT NULL
                                     CHECK (custom_formatting_present IN (0, 1)),
    custom_validation_present    INTEGER NOT NULL
                                     CHECK (custom_validation_present IN (0, 1)),
    custom_error_handling_present INTEGER NOT NULL
                                     CHECK (custom_error_handling_present IN (0, 1)),
    custom_glue_excerpt          TEXT,
    custom_glue_evidence_url     TEXT,

    -- Rung 4 alone says "plus some evidence of repeated modification if commit
    -- history was pulled". Commit data corroborates that one rung and must
    -- never stand in for the code-structure evidence above: a thin wrapper
    -- committed daily is still a rung 1.
    repeated_modification_evidence INTEGER
                                     CHECK (repeated_modification_evidence IN (0, 1)),
    recent_commit_count          INTEGER CHECK (recent_commit_count >= 0),
    active_contributors          INTEGER CHECK (active_contributors >= 0),
    latest_commit_date           TEXT,

    files_inspected              INTEGER NOT NULL DEFAULT 0
                                     CHECK (files_inspected >= 0),
    maintenance_evidence_notes   TEXT,
    collected_at                 TEXT NOT NULL
);

CREATE TABLE qualification (
    candidate_id         TEXT PRIMARY KEY REFERENCES candidates(candidate_id)
                             ON DELETE CASCADE,
    qualification_status TEXT NOT NULL CHECK (qualification_status IN (
                             'keep', 'investigate', 'reject')),
    qualification_reason TEXT NOT NULL,
    rejection_reason     TEXT CHECK (rejection_reason IN (
                             'single_incidental_use', 'tutorial_or_demo',
                             'fork_of_library', 'archived_no_signal',
                             'personal_project_no_customers', 'other')),
    confidence           TEXT NOT NULL CHECK (confidence IN (
                             'high', 'medium', 'low')),

    -- CANDIDATE_SCHEMA.md section 7: rejection_reason is "only set when
    -- qualification_status = reject".
    CHECK ((qualification_status = 'reject' AND rejection_reason IS NOT NULL)
        OR (qualification_status <> 'reject' AND rejection_reason IS NULL))
);

-- Only candidates that clear qualification ever get a row here. A reject does
-- not get a score of zero, it gets no row at all (SCORING_MODEL.md section 1).
-- That rule is enforced by the scoring engine in phase 10, not by this schema.
CREATE TABLE scores (
    candidate_id        TEXT PRIMARY KEY REFERENCES candidates(candidate_id)
                            ON DELETE CASCADE,
    document_volume     INTEGER NOT NULL CHECK (document_volume     BETWEEN 0 AND 5),
    document_complexity INTEGER NOT NULL CHECK (document_complexity BETWEEN 0 AND 5),
    business_criticality INTEGER NOT NULL CHECK (business_criticality BETWEEN 0 AND 5),
    pipeline_complexity INTEGER NOT NULL CHECK (pipeline_complexity BETWEEN 0 AND 5),
    maintenance_burden  INTEGER NOT NULL CHECK (maintenance_burden  BETWEEN 0 AND 5),
    build_vs_buy_signal INTEGER NOT NULL CHECK (build_vs_buy_signal BETWEEN 0 AND 5),
    commercial_leverage INTEGER NOT NULL CHECK (commercial_leverage BETWEEN 0 AND 5),
    raw_weighted_score  REAL    NOT NULL CHECK (raw_weighted_score BETWEEN 0 AND 5),
    final_score         INTEGER NOT NULL CHECK (final_score BETWEEN 0 AND 100),
    confidence_band     TEXT    NOT NULL CHECK (confidence_band IN (
                            'high', 'medium', 'low')),
    -- The cap from SCORING_MODEL.md section 14 that was applied, or NULL.
    -- Deliberately a range rather than today's specific caps: they live in
    -- weights.yaml so a person can retune them, and a schema hardcoding
    -- 20/25/40 would reject a retuned cap and make that configurability a
    -- fiction. Which cap applies is the scoring engine's decision, not this
    -- table's.
    gate_cap_applied    INTEGER CHECK (
                            gate_cap_applied IS NULL
                            OR gate_cap_applied BETWEEN 0 AND 100),
    -- JSON array of the dimension names that defaulted to 0 for being unknown.
    -- Kept so the report can show the gap explicitly rather than folding a
    -- missing dimension silently into the number.
    unknown_dimensions  TEXT NOT NULL DEFAULT '[]'
);

CREATE TABLE evidence_trail (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id     TEXT NOT NULL REFERENCES candidates(candidate_id)
                         ON DELETE CASCADE,
    evidence_url     TEXT NOT NULL,
    evidence_type    TEXT NOT NULL CHECK (evidence_type IN (
                         'code_permalink', 'manifest_line', 'readme_excerpt',
                         'website_page', 'api_response', 'dependents_page',
                         'other')),
    evidence_excerpt TEXT,
    source           TEXT NOT NULL,
    collected_at     TEXT NOT NULL
);

CREATE TABLE api_cache (
    cache_key     TEXT PRIMARY KEY,
    response_json TEXT NOT NULL,
    fetched_at    TEXT NOT NULL
);

CREATE INDEX idx_discovery_queries_run        ON discovery_queries(run_id);
CREATE INDEX idx_discovery_queries_library    ON discovery_queries(library_name);
CREATE INDEX idx_discovery_evidence_query     ON discovery_evidence(query_id);
CREATE INDEX idx_discovery_evidence_candidate ON discovery_evidence(candidate_id);
CREATE INDEX idx_dependencies_candidate       ON dependencies_found(candidate_id);
CREATE INDEX idx_evidence_trail_candidate     ON evidence_trail(candidate_id);
"""


def utcnow() -> str:
    """Current UTC time as an ISO 8601 string, the format every timestamp
    column in this schema stores."""
    return datetime.now(timezone.utc).isoformat()


def _configure(conn: sqlite3.Connection) -> None:
    conn.row_factory = sqlite3.Row
    # Off by default in SQLite, and must be set outside a transaction.
    conn.execute("PRAGMA foreign_keys = ON")


@contextmanager
def connect(db_path: Path | str) -> Iterator[sqlite3.Connection]:
    """Open a configured connection, committing on success.

    Rolls back and re-raises on any exception, and always closes. Performs no
    schema check; use open_database() for that.
    """
    conn = sqlite3.connect(db_path)
    _configure(conn)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


MAINTENANCE_EVIDENCE_DDL = """
CREATE TABLE maintenance_evidence (
    candidate_id                 TEXT PRIMARY KEY
                                     REFERENCES candidates(candidate_id)
                                     ON DELETE CASCADE,

    -- SCORING_MODEL.md section 7 grades how much custom code surrounds the
    -- document libraries, not how busy the repository is. These first fields
    -- are what the rubric actually reads.
    document_library_count       INTEGER NOT NULL
                                     CHECK (document_library_count >= 0),
    same_file_library_count      INTEGER NOT NULL
                                     CHECK (same_file_library_count >= 0),
    custom_logic_present         INTEGER NOT NULL
                                     CHECK (custom_logic_present IN (0, 1)),
    custom_formatting_present    INTEGER NOT NULL
                                     CHECK (custom_formatting_present IN (0, 1)),
    custom_validation_present    INTEGER NOT NULL
                                     CHECK (custom_validation_present IN (0, 1)),
    custom_error_handling_present INTEGER NOT NULL
                                     CHECK (custom_error_handling_present IN (0, 1)),
    custom_glue_excerpt          TEXT,
    custom_glue_evidence_url     TEXT,

    -- Rung 4 alone says "plus some evidence of repeated modification if commit
    -- history was pulled". Commit data corroborates that one rung and must
    -- never stand in for the code-structure evidence above: a thin wrapper
    -- committed daily is still a rung 1.
    repeated_modification_evidence INTEGER
                                     CHECK (repeated_modification_evidence IN (0, 1)),
    recent_commit_count          INTEGER CHECK (recent_commit_count >= 0),
    active_contributors          INTEGER CHECK (active_contributors >= 0),
    latest_commit_date           TEXT,

    files_inspected              INTEGER NOT NULL DEFAULT 0
                                     CHECK (files_inspected >= 0),
    maintenance_evidence_notes   TEXT,
    collected_at                 TEXT NOT NULL
);
"""


def create_schema(conn: sqlite3.Connection) -> None:
    """Create every table and stamp the schema version."""
    conn.executescript(SCHEMA_SQL)
    conn.execute(
        "INSERT INTO schema_version (id, version, applied_at) VALUES (1, ?, ?)",
        (SCHEMA_VERSION, utcnow()),
    )


def read_schema_version(conn: sqlite3.Connection) -> int | None:
    """Return the version stamped in the database, or None if uninitialized."""
    try:
        row = conn.execute(
            "SELECT version FROM schema_version WHERE id = 1"
        ).fetchone()
    except sqlite3.OperationalError:
        return None
    return None if row is None else int(row["version"])


def check_schema_version(conn: sqlite3.Connection) -> None:
    """Fail loudly when the database was built by different code.

    There is deliberately no migration path. A mismatch means the file and the
    code disagree about what the tables contain, and guessing which is right is
    exactly the kind of silent wrongness this project is trying to avoid.
    """
    found = read_schema_version(conn)
    if found is None:
        raise DatabaseNotInitialized(
            "Database has no schema_version table. It was never initialized, "
            "or it is not a Dependency Map database."
        )
    if found != SCHEMA_VERSION:
        raise SchemaVersionMismatch(
            f"Database schema version is {found}, but this code expects "
            f"{SCHEMA_VERSION}. There is no migration tooling. Rebuild the "
            f"database, or check out the code matching version {found}."
        )



class MigrationError(Exception):
    """A migration could not be applied safely."""


def migrate_v2_to_v3(conn: sqlite3.Connection) -> None:
    """The one-time schema 2 to 3 upgrade, applied in place.

    Deliberately not a migration framework: one function, one hop, additive
    only. Every change is an ADD COLUMN or a CREATE TABLE, so no existing row
    is rewritten and nothing can be lost. New columns are nullable on purpose -
    a run-1 row genuinely does not know its file path or its repository
    purpose, and inventing a default would turn "never asked" into a finding.
    """
    version = read_schema_version(conn)
    if version == SCHEMA_VERSION:
        return
    if version != 2:
        raise MigrationError(
            f"migrate_v2_to_v3 expects schema version 2, found {version!r}."
        )

    existing = {
        row["name"]
        for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    }

    additions = [
        ("discovery_evidence", "file_path", "TEXT"),
        ("discovery_evidence", "evidence_url", "TEXT"),
        ("pipeline_evidence", "infrastructure_reference_present",
         "INTEGER CHECK (infrastructure_reference_present IN (0, 1))"),
        ("business_evidence", "is_catalogue_repository",
         "INTEGER CHECK (is_catalogue_repository IN (0, 1))"),
        ("business_evidence", "readme_indicates_example_or_tutorial",
         "INTEGER CHECK (readme_indicates_example_or_tutorial IN (0, 1))"),
        ("business_evidence", "has_examples_directory",
         "INTEGER CHECK (has_examples_directory IN (0, 1))"),
    ]
    for table, column, decl in additions:
        columns = {r["name"] for r in conn.execute(f"PRAGMA table_info({table})")}
        if column not in columns:
            conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {decl}")

    if "maintenance_evidence" not in existing:
        conn.executescript(MAINTENANCE_EVIDENCE_DDL)

    conn.execute("UPDATE schema_version SET version = ? WHERE id = 1",
                 (SCHEMA_VERSION,))


def initialize_database(db_path: Path | str) -> None:
    """Create a new database file with the full schema.

    Refuses to touch a file that already has a schema, so an accidental second
    call can't clobber collected evidence.
    """
    path = Path(db_path)
    if path.parent and str(path.parent) not in ("", "."):
        path.parent.mkdir(parents=True, exist_ok=True)
    with connect(path) as conn:
        if read_schema_version(conn) is not None:
            raise RuntimeError(
                f"{path} is already initialized. Refusing to overwrite it."
            )
        create_schema(conn)


@contextmanager
def open_database(db_path: Path | str) -> Iterator[sqlite3.Connection]:
    """Open an existing database, validating its schema version first.

    This is the startup check. Every caller that reads or writes real data
    should come through here rather than connect().
    """
    with connect(db_path) as conn:
        check_schema_version(conn)
        yield conn
