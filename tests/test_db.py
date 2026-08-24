"""Schema creation, the schema-version check, and connection behaviour."""

from __future__ import annotations

import sqlite3

import pytest

from dependency_map import db as db_module
from dependency_map.db import (
    SCHEMA_VERSION,
    SCORING_DIMENSIONS,
    DatabaseNotInitialized,
    SchemaVersionMismatch,
    check_schema_version,
    connect,
    initialize_database,
    read_schema_version,
)

EXPECTED_TABLES = {
    "runs",
    "candidates",
    "discovery_queries",
    "discovery_evidence",
    "dependencies_found",
    "pipeline_evidence",
    "business_evidence",
    "qualification",
    "scores",
    "evidence_trail",
    "api_cache",
}


def _tables(conn):
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table'"
    ).fetchall()
    return {row["name"] for row in rows}


# --- schema creation -------------------------------------------------------


def test_all_design_tables_exist(conn):
    assert EXPECTED_TABLES.issubset(_tables(conn))


def test_discovery_evidence_holds_only_the_candidate_hit_relationship(conn):
    """Query facts live in discovery_queries, never duplicated per hit."""
    columns = {r["name"] for r in conn.execute("PRAGMA table_info(discovery_evidence)")}

    # Schema 3 adds the file the hit matched. That is still the hit
    # relationship, not a copy of the query: it is what this row found, where.
    assert columns == {"id", "query_id", "candidate_id", "discovery_result_rank",
                       "file_path", "evidence_url"}
    for moved in ("run_id", "discovery_source", "discovery_query", "discovered_at"):
        assert moved not in columns, f"{moved} should live on discovery_queries"


def test_discovery_queries_has_the_coverage_fields(conn):
    columns = {r["name"] for r in conn.execute("PRAGMA table_info(discovery_queries)")}

    assert {"total_count", "capped", "search_window", "returned_count",
            "discovery_tier", "library_name"}.issubset(columns)


def test_schema_version_table_exists_and_is_stamped(conn):
    assert "schema_version" in _tables(conn)
    assert read_schema_version(conn) == SCHEMA_VERSION


def test_schema_version_table_holds_at_most_one_row(conn):
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO schema_version (id, version, applied_at) "
            "VALUES (2, 1, 'now')"
        )


def test_seven_scoring_dimensions_are_columns_on_scores(conn):
    columns = {
        row["name"] for row in conn.execute("PRAGMA table_info(scores)")
    }
    assert set(SCORING_DIMENSIONS).issubset(columns)
    assert len(SCORING_DIMENSIONS) == 7


def test_scores_has_unknown_dimensions_column(conn):
    columns = {
        row["name"] for row in conn.execute("PRAGMA table_info(scores)")
    }
    assert "unknown_dimensions" in columns


def test_initialize_refuses_to_clobber_an_existing_database(db_path):
    with pytest.raises(RuntimeError, match="already initialized"):
        initialize_database(db_path)


def test_initialize_creates_parent_directory(tmp_path):
    nested = tmp_path / "made" / "up" / "dir" / "x.db"
    initialize_database(nested)
    assert nested.exists()


# --- schema version check --------------------------------------------------


def test_version_check_passes_on_a_matching_database(db_path):
    with connect(db_path) as conn:
        check_schema_version(conn)  # must not raise


def test_version_check_fails_loudly_on_mismatch(db_path):
    """The core requirement: a stale database refuses to run, it doesn't
    silently half-work."""
    with connect(db_path) as conn:
        conn.execute("UPDATE schema_version SET version = ? WHERE id = 1",
                     (SCHEMA_VERSION + 1,))

    with connect(db_path) as conn:
        with pytest.raises(SchemaVersionMismatch) as excinfo:
            check_schema_version(conn)

    message = str(excinfo.value)
    assert str(SCHEMA_VERSION + 1) in message
    assert str(SCHEMA_VERSION) in message


def test_open_database_refuses_a_mismatched_database(db_path):
    with connect(db_path) as conn:
        conn.execute("UPDATE schema_version SET version = 99 WHERE id = 1")

    with pytest.raises(SchemaVersionMismatch):
        with db_module.open_database(db_path):
            pass


def test_version_check_fails_on_an_uninitialized_database(tmp_path):
    empty = tmp_path / "empty.db"
    sqlite3.connect(empty).close()

    with connect(empty) as conn:
        assert read_schema_version(conn) is None
        with pytest.raises(DatabaseNotInitialized):
            check_schema_version(conn)


def test_open_database_yields_a_usable_connection(db_path):
    with db_module.open_database(db_path) as conn:
        assert conn.execute("SELECT COUNT(*) FROM candidates").fetchone()[0] == 0


# --- connection behaviour --------------------------------------------------


def test_foreign_keys_are_enforced(conn):
    """Off by default in SQLite, so this is worth asserting rather than
    assuming."""
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO discovery_evidence (query_id, candidate_id) VALUES (?, ?)",
            ("does_not_exist", "nor_this"),
        )


def test_connect_commits_on_clean_exit(db_path):
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO runs (run_id, started_at) VALUES ('run_x', 'now')"
        )

    with connect(db_path) as conn:
        assert conn.execute(
            "SELECT COUNT(*) FROM runs WHERE run_id = 'run_x'"
        ).fetchone()[0] == 1


def test_connect_rolls_back_on_exception(db_path):
    class Boom(Exception):
        pass

    with pytest.raises(Boom):
        with connect(db_path) as conn:
            conn.execute(
                "INSERT INTO runs (run_id, started_at) VALUES ('run_y', 'now')"
            )
            raise Boom()

    with connect(db_path) as conn:
        assert conn.execute(
            "SELECT COUNT(*) FROM runs WHERE run_id = 'run_y'"
        ).fetchone()[0] == 0


def test_temporary_db_fixture_is_not_the_production_path(db_path):
    """Guards rule 14: tests never use the real database.

    The invariant is that no test *writes* the production path, not that the
    path is absent. A real run creates `data/dependency_map.db` on purpose, and
    an assertion that it does not exist can only hold until the tool is used
    for the thing it was built for. The suite-wide half of this check lives in
    conftest.py, which compares the production file before and after the run.
    """
    assert db_path != db_module.DEFAULT_DB_PATH
    assert db_module.DEFAULT_DB_PATH not in db_path.parents
    assert "tmp" in str(db_path).lower() or "temp" in str(db_path).lower(), (
        f"{db_path} does not look like a pytest temporary path."
    )
