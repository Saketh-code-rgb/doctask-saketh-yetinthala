"""Shared fixtures.

Every test runs against a temporary database created inside pytest's tmp_path.
Nothing here ever touches data/dependency_map.db.
"""

from __future__ import annotations

import sqlite3

import pytest

from dependency_map import db as db_module
from dependency_map import storage


def _production_db_state():
    """Enough of the production database's identity to notice a write.

    Returns None when the file does not exist, which is itself a state worth
    comparing: a suite that created it would move from None to a stat tuple.
    """
    path = db_module.DEFAULT_DB_PATH
    if not path.exists():
        return None
    stat = path.stat()
    return (stat.st_size, stat.st_mtime_ns)


@pytest.fixture(scope="session", autouse=True)
def production_database_is_never_written():
    """Guards rule 14 across the whole suite.

    Tests use temporary databases; none of them may touch the real one. The
    check is that the production file is unchanged from before the suite to
    after it, rather than that it is missing. A real run creates it deliberately
    (phase 13), so requiring its absence would make the guard fail for the one
    reason that is not a defect.
    """
    before = _production_db_state()
    yield
    after = _production_db_state()
    assert after == before, (
        f"{db_module.DEFAULT_DB_PATH} changed during the test suite "
        f"({before} -> {after}). No test may write the production database."
    )


@pytest.fixture
def db_path(tmp_path):
    """Path to a freshly initialized temporary database file."""
    path = tmp_path / "test.db"
    db_module.initialize_database(path)
    return path


@pytest.fixture
def conn(db_path):
    """An open connection to a temporary database, rolled back after the test."""
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    try:
        yield connection
    finally:
        connection.close()


@pytest.fixture
def run_id(conn):
    """A committed run, since most tables hang off one."""
    storage.create_run(conn, "run_1", notes="fixture run")
    return "run_1"


@pytest.fixture
def candidate_id(conn, run_id):
    """A committed candidate, since most evidence tables hang off one."""
    cid = "c_test01"
    storage.insert_candidate_if_new(
        conn,
        candidate_id=cid,
        repo_url="https://github.com/example-org/example-repo",
        repo_owner="example-org",
        repo_name="example-repo",
        is_fork=False,
        is_archived=False,
        primary_language="Python",
        first_seen_run_id=run_id,
    )
    return cid
