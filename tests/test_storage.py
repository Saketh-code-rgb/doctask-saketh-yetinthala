"""CRUD for every table in the schema.

One section per table, mirroring IMPLEMENTATION_PLAN.md phase 2 tasks 4 to 10.
Every test runs against a temporary database from conftest.py.
"""

from __future__ import annotations

import sqlite3

import pytest

from dependency_map import storage
from dependency_map.db import SCORING_DIMENSIONS

# --- runs ------------------------------------------------------------------


def test_create_and_read_run(conn):
    storage.create_run(conn, "run_1", notes="first run")
    row = storage.get_run(conn, "run_1")

    assert row is not None
    assert row["run_id"] == "run_1"
    assert row["notes"] == "first run"
    assert row["started_at"]
    assert row["finished_at"] is None


def test_finish_run_sets_finished_at(conn):
    storage.create_run(conn, "run_1")
    storage.finish_run(conn, "run_1")

    assert storage.get_run(conn, "run_1")["finished_at"] is not None


def test_get_run_returns_none_when_absent(conn):
    assert storage.get_run(conn, "nope") is None


def test_run_ids_are_unique(conn):
    storage.create_run(conn, "run_1")
    with pytest.raises(sqlite3.IntegrityError):
        storage.create_run(conn, "run_1")


def test_list_runs(conn):
    storage.create_run(conn, "run_1", started_at="2026-08-01T00:00:00Z")
    storage.create_run(conn, "run_2", started_at="2026-08-02T00:00:00Z")

    assert [r["run_id"] for r in storage.list_runs(conn)] == ["run_1", "run_2"]


# --- candidates ------------------------------------------------------------


def test_insert_candidate_returns_true_when_new(conn, run_id):
    created = storage.insert_candidate_if_new(
        conn,
        candidate_id="c_new",
        repo_url="https://github.com/acme/widget",
        repo_owner="acme",
        repo_name="widget",
        first_seen_run_id=run_id,
    )
    assert created is True
    assert storage.count_candidates(conn) == 1


def test_insert_candidate_returns_false_when_already_known(conn, run_id):
    kwargs = dict(
        candidate_id="c_dup",
        repo_url="https://github.com/acme/widget",
        repo_owner="acme",
        repo_name="widget",
        first_seen_run_id=run_id,
    )
    assert storage.insert_candidate_if_new(conn, **kwargs) is True
    assert storage.insert_candidate_if_new(conn, **kwargs) is False
    assert storage.count_candidates(conn) == 1


def test_get_candidate_by_id_and_by_repo_url(conn, candidate_id):
    by_id = storage.get_candidate(conn, candidate_id)
    by_url = storage.get_candidate_by_repo_url(
        conn, "https://github.com/example-org/example-repo"
    )

    assert by_id is not None
    assert by_url is not None
    assert by_id["candidate_id"] == by_url["candidate_id"] == candidate_id


def test_get_candidate_returns_none_when_absent(conn):
    assert storage.get_candidate(conn, "ghost") is None
    assert storage.get_candidate_by_repo_url(conn, "https://x/y") is None


def test_booleans_round_trip_as_integers(conn, candidate_id):
    row = storage.get_candidate(conn, candidate_id)
    assert row["is_fork"] == 0
    assert row["is_archived"] == 0


def test_repo_url_is_unique_across_candidate_ids(conn, candidate_id):
    """Two different ids must not claim the same repository."""
    with pytest.raises(sqlite3.IntegrityError):
        storage.insert_candidate_if_new(
            conn,
            candidate_id="c_different",
            repo_url="https://github.com/example-org/example-repo",
            repo_owner="example-org",
            repo_name="example-repo",
        )


def test_industry_category_rejects_unknown_value(conn):
    with pytest.raises(sqlite3.IntegrityError):
        storage.insert_candidate_if_new(
            conn,
            candidate_id="c_bad",
            repo_url="https://github.com/a/b",
            repo_owner="a",
            repo_name="b",
            industry_category="crypto_casino",
        )


def test_company_name_source_requires_a_company_name(conn):
    """CANDIDATE_SCHEMA.md section 2: source is null if company_name is null."""
    with pytest.raises(sqlite3.IntegrityError):
        storage.insert_candidate_if_new(
            conn,
            candidate_id="c_bad2",
            repo_url="https://github.com/a/c",
            repo_owner="a",
            repo_name="c",
            company_name=None,
            company_name_source="readme",
        )


def test_update_candidate_identity(conn, candidate_id):
    storage.update_candidate_identity(
        conn,
        candidate_id,
        company_name="Acme Corp",
        company_name_source="website_link",
        industry_category="legal_contracts",
    )
    row = storage.get_candidate(conn, candidate_id)

    assert row["company_name"] == "Acme Corp"
    assert row["company_name_source"] == "website_link"
    assert row["industry_category"] == "legal_contracts"


def test_update_candidate_identity_rejects_unknown_column(conn, candidate_id):
    """Column names are allowlisted, never interpolated from caller input."""
    with pytest.raises(ValueError, match="Not updatable"):
        storage.update_candidate_identity(
            conn, candidate_id, **{"repo_name = 'x'; DROP TABLE runs; --": 1}
        )


def test_update_candidate_identity_refuses_immutable_columns(conn, candidate_id):
    with pytest.raises(ValueError):
        storage.update_candidate_identity(
            conn, candidate_id, repo_url="https://github.com/other/repo"
        )


# --- discovery_queries -----------------------------------------------------


def _query(conn, run_id, query="q", **kw):
    return storage.create_discovery_query(
        conn, run_id=run_id, discovery_source="github_code_search",
        query=query, **kw,
    )


def test_create_and_get_discovery_query(conn, run_id):
    query_id = _query(
        conn, run_id,
        query='"docxtpl" filename:requirements.txt',
        library_name="docxtpl (python-docx-template)",
        discovery_tier=2, total_count=1852, capped=True, returned_count=30,
    )
    row = storage.get_discovery_query(conn, query_id)

    assert row["query"] == '"docxtpl" filename:requirements.txt'
    assert row["library_name"] == "docxtpl (python-docx-template)"
    assert row["discovery_tier"] == 2
    assert row["total_count"] == 1852
    assert row["capped"] == 1
    assert row["returned_count"] == 30
    assert row["executed_at"]


def test_query_id_is_deterministic():
    a = storage.make_query_id("run_1", "q", None)
    b = storage.make_query_id("run_1", "q", None)

    assert a == b
    assert storage.make_query_id("run_1", "q", "size:501..1000") != a
    assert storage.make_query_id("run_2", "q", None) != a


def test_rerunning_the_same_slice_updates_rather_than_duplicates(conn, run_id):
    """What makes the discovery stage resumable."""
    first = _query(conn, run_id, query="q", total_count=10, returned_count=5)
    second = _query(conn, run_id, query="q", total_count=12, returned_count=6)

    assert first == second
    assert storage.count_queries_for_run(conn, run_id) == 1
    assert storage.get_discovery_query(conn, first)["total_count"] == 12


def test_a_zero_result_query_is_still_recorded(conn, run_id):
    """The phase 6A experiment found an invalid query precisely because a
    zero-result execution is itself a finding."""
    query_id = _query(
        conn, run_id,
        query='"reportlab" filename:requirements.txt language:python',
        total_count=0, returned_count=0, capped=False,
    )
    row = storage.get_discovery_query(conn, query_id)

    assert row["total_count"] == 0
    assert row["returned_count"] == 0
    assert row["capped"] == 0
    assert storage.list_discovery_evidence_for_query(conn, query_id) == []


def test_update_query_results_derives_capped_above_the_ceiling(conn, run_id):
    query_id = _query(conn, run_id)
    storage.update_query_results(conn, query_id, total_count=75648, returned_count=10)

    row = storage.get_discovery_query(conn, query_id)
    assert row["capped"] == 1
    assert row["total_count"] == 75648


def test_update_query_results_derives_uncapped_below_the_ceiling(conn, run_id):
    query_id = _query(conn, run_id)
    storage.update_query_results(conn, query_id, total_count=662, returned_count=10)

    assert storage.get_discovery_query(conn, query_id)["capped"] == 0


@pytest.mark.parametrize("total,expected", [(999, 0), (1000, 0), (1001, 1)])
def test_capped_boundary_is_strictly_above_one_thousand(conn, run_id, total, expected):
    query_id = _query(conn, run_id)
    storage.update_query_results(conn, query_id, total_count=total, returned_count=1)

    assert storage.get_discovery_query(conn, query_id)["capped"] == expected


def test_library_name_may_be_null_for_co_occurrence_queries(conn, run_id):
    query_id = _query(
        conn, run_id, query='"python-docx" "reportlab" filename:requirements.txt',
        library_name=None, discovery_tier=3,
    )
    assert storage.get_discovery_query(conn, query_id)["library_name"] is None


def test_search_window_is_stored(conn, run_id):
    query_id = _query(
        conn, run_id, search_window="size:251..500", discovery_tier=3
    )
    assert storage.get_discovery_query(conn, query_id)["search_window"] == \
        "size:251..500"


def test_same_query_with_different_slices_are_separate_records(conn, run_id):
    a = _query(conn, run_id, query="q", search_window="size:251..500")
    b = _query(conn, run_id, query="q", search_window="size:0..250")

    assert a != b
    assert storage.count_queries_for_run(conn, run_id) == 2


def test_list_queries_for_run(conn, run_id):
    storage.create_run(conn, "run_2")
    _query(conn, run_id, query="q1")
    _query(conn, run_id, query="q2")
    _query(conn, "run_2", query="q3")

    assert len(storage.list_queries_for_run(conn, run_id)) == 2
    assert len(storage.list_queries_for_run(conn, "run_2")) == 1


def test_discovery_tier_is_constrained(conn, run_id):
    with pytest.raises(sqlite3.IntegrityError):
        _query(conn, run_id, discovery_tier=4)


def test_negative_returned_count_is_rejected(conn, run_id):
    with pytest.raises(sqlite3.IntegrityError):
        _query(conn, run_id, returned_count=-1)


def test_discovery_source_rejects_unknown_value(conn, run_id):
    with pytest.raises(sqlite3.IntegrityError):
        storage.create_discovery_query(
            conn, run_id=run_id, discovery_source="google", query="q"
        )


def test_query_requires_a_real_run(conn):
    with pytest.raises(sqlite3.IntegrityError):
        storage.create_discovery_query(
            conn, run_id="ghost", discovery_source="manual", query="q"
        )


# --- discovery_evidence ----------------------------------------------------


def test_insert_and_list_discovery_evidence(conn, candidate_id, run_id):
    query_id = _query(conn, run_id, query='"docxtpl" filename:requirements.txt')
    storage.insert_discovery_evidence(
        conn, query_id=query_id, candidate_id=candidate_id, discovery_result_rank=12
    )
    rows = storage.list_discovery_evidence_for_candidate(conn, candidate_id)

    assert len(rows) == 1
    assert rows[0]["discovery_result_rank"] == 12
    # Query facts arrive through the join, not duplicated on the hit.
    assert rows[0]["query"] == '"docxtpl" filename:requirements.txt'
    assert rows[0]["run_id"] == run_id
    assert rows[0]["discovery_source"] == "github_code_search"
    assert rows[0]["discovered_at"]


def test_a_candidate_can_have_several_discovery_rows(conn, candidate_id, run_id):
    """One row per query that surfaced it. That history is what dedup and
    fresh-batch tracking read."""
    for q in ("q1", "q2"):
        query_id = _query(conn, run_id, query=q)
        storage.insert_discovery_evidence(
            conn, query_id=query_id, candidate_id=candidate_id
        )
    assert len(storage.list_discovery_evidence_for_candidate(conn, candidate_id)) == 2


def test_one_query_returning_a_repo_twice_records_one_hit(conn, candidate_id, run_id):
    """A query can match the same repository at two file paths. That is one
    hit, which is exactly why returned_count is tracked on the query."""
    query_id = _query(conn, run_id, query="same")
    first = storage.insert_discovery_evidence(
        conn, query_id=query_id, candidate_id=candidate_id, discovery_result_rank=3
    )
    second = storage.insert_discovery_evidence(
        conn, query_id=query_id, candidate_id=candidate_id, discovery_result_rank=7
    )

    assert first is not None
    assert second is None
    assert len(storage.list_discovery_evidence_for_query(conn, query_id)) == 1


def test_returned_count_may_exceed_recorded_hits(conn, candidate_id, run_id):
    query_id = _query(conn, run_id, returned_count=10)
    storage.insert_discovery_evidence(conn, query_id=query_id, candidate_id=candidate_id)

    assert storage.get_discovery_query(conn, query_id)["returned_count"] == 10
    assert len(storage.list_discovery_evidence_for_query(conn, query_id)) == 1


def test_list_candidate_ids_for_run_is_distinct(conn, candidate_id, run_id):
    for q in ("q1", "q2", "q3"):
        query_id = _query(conn, run_id, query=q)
        storage.insert_discovery_evidence(
            conn, query_id=query_id, candidate_id=candidate_id
        )
    assert storage.list_candidate_ids_for_run(conn, run_id) == [candidate_id]


def test_list_candidate_ids_for_run_excludes_other_runs(conn, candidate_id, run_id):
    storage.create_run(conn, "run_2")
    query_id = _query(conn, run_id, query="q")
    storage.insert_discovery_evidence(conn, query_id=query_id, candidate_id=candidate_id)

    assert storage.list_candidate_ids_for_run(conn, "run_2") == []


def test_all_discovered_candidate_ids(conn, candidate_id, run_id):
    query_id = _query(conn, run_id, query="q")
    storage.insert_discovery_evidence(conn, query_id=query_id, candidate_id=candidate_id)

    assert storage.all_discovered_candidate_ids(conn) == {candidate_id}


def test_evidence_requires_a_real_query(conn, candidate_id):
    with pytest.raises(sqlite3.IntegrityError):
        storage.insert_discovery_evidence(
            conn, query_id="q_ghost", candidate_id=candidate_id
        )


def test_deleting_a_query_cascades_to_its_hits(conn, candidate_id, run_id):
    query_id = _query(conn, run_id, query="q")
    storage.insert_discovery_evidence(conn, query_id=query_id, candidate_id=candidate_id)
    conn.execute("DELETE FROM discovery_queries WHERE query_id = ?", (query_id,))

    assert storage.list_discovery_evidence_for_candidate(conn, candidate_id) == []


# --- dependencies_found ----------------------------------------------------


def _dep(**overrides):
    base = dict(
        library_name="docxtpl",
        library_category="template_generation",
        direction="generation",
        detection_method="code_import",
        evidence_url="https://github.com/example-org/example-repo/blob/main/a.py#L18",
        manifest_file="requirements.txt",
    )
    base.update(overrides)
    return base


def test_insert_and_list_dependencies(conn, candidate_id):
    storage.insert_dependency_found(conn, candidate_id=candidate_id, **_dep())
    rows = storage.list_dependencies_for_candidate(conn, candidate_id)

    assert len(rows) == 1
    assert rows[0]["library_name"] == "docxtpl"
    assert rows[0]["direction"] == "generation"
    assert rows[0]["manifest_file"] == "requirements.txt"


def test_duplicate_dependency_fact_is_ignored(conn, candidate_id):
    first = storage.insert_dependency_found(
        conn, candidate_id=candidate_id, **_dep()
    )
    second = storage.insert_dependency_found(
        conn, candidate_id=candidate_id, **_dep()
    )

    assert first is not None
    assert second is None
    assert len(storage.list_dependencies_for_candidate(conn, candidate_id)) == 1


def test_same_library_via_different_detection_method_is_kept(conn, candidate_id):
    storage.insert_dependency_found(
        conn, candidate_id=candidate_id,
        **_dep(detection_method="manifest_declaration",
               evidence_url="https://x/requirements.txt#L7"),
    )
    storage.insert_dependency_found(
        conn, candidate_id=candidate_id, **_dep(detection_method="code_import")
    )
    assert len(storage.list_dependencies_for_candidate(conn, candidate_id)) == 2


def test_manifest_file_may_be_null_for_infrastructure_evidence(conn, candidate_id):
    """Gotenberg and friends live in a compose file, not a manifest."""
    storage.insert_dependency_found(
        conn, candidate_id=candidate_id,
        **_dep(library_name="Gotenberg", library_category="conversion",
               direction="conversion", detection_method="infrastructure_reference",
               manifest_file=None,
               evidence_url="https://x/docker-compose.yml#L12"),
    )
    rows = storage.list_dependencies_for_candidate(conn, candidate_id)
    assert rows[0]["manifest_file"] is None


@pytest.mark.parametrize(
    "field,value",
    [
        ("library_category", "spreadsheets"),
        ("direction", "sideways"),
        ("detection_method", "vibes"),
    ],
)
def test_dependency_enums_are_constrained(conn, candidate_id, field, value):
    with pytest.raises(sqlite3.IntegrityError):
        storage.insert_dependency_found(
            conn, candidate_id=candidate_id, **_dep(**{field: value})
        )


# --- pipeline_evidence -----------------------------------------------------


def test_upsert_and_get_pipeline_evidence(conn, candidate_id):
    storage.upsert_pipeline_evidence(
        conn,
        candidate_id=candidate_id,
        code_usage_confirmed=True,
        template_directory_present=True,
        multiple_document_types_handled=False,
        pipeline_stage_count=3,
        infrastructure_service_present=False,
        pipeline_evidence_notes="data -> docxtpl -> WeasyPrint",
    )
    row = storage.get_pipeline_evidence(conn, candidate_id)

    assert row["code_usage_confirmed"] == 1
    assert row["multiple_document_types_handled"] == 0
    assert row["pipeline_stage_count"] == 3
    assert row["pipeline_evidence_notes"] == "data -> docxtpl -> WeasyPrint"


def test_pipeline_evidence_upsert_replaces_not_duplicates(conn, candidate_id):
    for count in (1, 4):
        storage.upsert_pipeline_evidence(
            conn, candidate_id=candidate_id,
            code_usage_confirmed=True, template_directory_present=False,
            multiple_document_types_handled=False, pipeline_stage_count=count,
            infrastructure_service_present=False,
        )
    assert storage.get_pipeline_evidence(conn, candidate_id)["pipeline_stage_count"] == 4
    assert conn.execute("SELECT COUNT(*) FROM pipeline_evidence").fetchone()[0] == 1


def test_pipeline_evidence_has_all_schema_fields(conn):
    columns = {r["name"] for r in conn.execute("PRAGMA table_info(pipeline_evidence)")}
    assert columns == {
        "candidate_id",
        "code_usage_confirmed",
        "template_directory_present",
        "multiple_document_types_handled",
        "pipeline_stage_count",
        "infrastructure_service_present",
        # Schema 3 keeps "a file was found" separate from "the application
        # uses that service"; run 1 conflated them.
        "infrastructure_reference_present",
        "pipeline_evidence_notes",
    }


def test_pipeline_stage_count_cannot_be_negative(conn, candidate_id):
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_pipeline_evidence(
            conn, candidate_id=candidate_id,
            code_usage_confirmed=False, template_directory_present=False,
            multiple_document_types_handled=False, pipeline_stage_count=-1,
            infrastructure_service_present=False,
        )


def test_get_pipeline_evidence_returns_none_when_absent(conn, candidate_id):
    assert storage.get_pipeline_evidence(conn, candidate_id) is None


# --- business_evidence -----------------------------------------------------


def test_upsert_and_get_business_evidence(conn, candidate_id):
    storage.upsert_business_evidence(
        conn,
        candidate_id=candidate_id,
        readme_describes_product=True,
        readme_excerpt="Auto-generates state-specific lease agreements.",
        website_exists=True,
        application_code_exists=True,
        document_functionality_in_production_code=True,
        stars=41,
        last_commit_date="2026-07-30",
        contributor_count=4,
        business_evidence_notes="Customer-facing product.",
    )
    row = storage.get_business_evidence(conn, candidate_id)

    assert row["readme_describes_product"] == 1
    assert row["stars"] == 41
    assert row["contributor_count"] == 4
    assert row["last_commit_date"] == "2026-07-30"


def test_business_evidence_has_all_schema_fields(conn):
    columns = {r["name"] for r in conn.execute("PRAGMA table_info(business_evidence)")}
    assert columns == {
        "candidate_id",
        "readme_describes_product",
        "readme_excerpt",
        "website_exists",
        "application_code_exists",
        "document_functionality_in_production_code",
        "stars",
        "last_commit_date",
        "contributor_count",
        # Schema 3 repository-purpose signals: evidence only, nullable, and
        # never read as a negative when null.
        "is_catalogue_repository",
        "readme_indicates_example_or_tutorial",
        "has_examples_directory",
        "business_evidence_notes",
    }


def test_readme_describes_product_requires_an_excerpt(conn, candidate_id):
    """CANDIDATE_SCHEMA.md section 6: "Requires a quoted excerpt to be set
    true". The claim cannot be recorded without the evidence for it."""
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_business_evidence(
            conn, candidate_id=candidate_id,
            readme_describes_product=True, readme_excerpt=None,
            website_exists=False, application_code_exists=True,
            document_functionality_in_production_code=True,
        )


def test_blank_excerpt_does_not_satisfy_the_requirement(conn, candidate_id):
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_business_evidence(
            conn, candidate_id=candidate_id,
            readme_describes_product=True, readme_excerpt="   ",
            website_exists=False, application_code_exists=True,
            document_functionality_in_production_code=True,
        )


def test_false_readme_claim_needs_no_excerpt(conn, candidate_id):
    storage.upsert_business_evidence(
        conn, candidate_id=candidate_id,
        readme_describes_product=False, readme_excerpt=None,
        website_exists=False, application_code_exists=False,
        document_functionality_in_production_code=False,
    )
    assert storage.get_business_evidence(conn, candidate_id) is not None


def test_contributor_count_may_be_null(conn, candidate_id):
    storage.upsert_business_evidence(
        conn, candidate_id=candidate_id,
        readme_describes_product=False, website_exists=False,
        application_code_exists=True,
        document_functionality_in_production_code=False,
        contributor_count=None,
    )
    assert storage.get_business_evidence(conn, candidate_id)["contributor_count"] is None


def test_business_evidence_upsert_replaces_not_duplicates(conn, candidate_id):
    for stars in (1, 99):
        storage.upsert_business_evidence(
            conn, candidate_id=candidate_id,
            readme_describes_product=False, website_exists=False,
            application_code_exists=True,
            document_functionality_in_production_code=False, stars=stars,
        )
    assert storage.get_business_evidence(conn, candidate_id)["stars"] == 99
    assert conn.execute("SELECT COUNT(*) FROM business_evidence").fetchone()[0] == 1


# --- qualification ---------------------------------------------------------


def test_upsert_and_get_qualification_keep(conn, candidate_id):
    storage.upsert_qualification(
        conn,
        candidate_id=candidate_id,
        qualification_status="keep",
        qualification_reason="category_count=2, code_usage_confirmed=true",
        confidence="high",
    )
    row = storage.get_qualification(conn, candidate_id)

    assert row["qualification_status"] == "keep"
    assert row["rejection_reason"] is None
    assert row["confidence"] == "high"


def test_reject_requires_a_rejection_reason(conn, candidate_id):
    """CANDIDATE_SCHEMA.md section 7 ties the two fields together."""
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_qualification(
            conn, candidate_id=candidate_id,
            qualification_status="reject",
            qualification_reason="no product signal",
            confidence="high",
            rejection_reason=None,
        )


def test_non_reject_must_not_carry_a_rejection_reason(conn, candidate_id):
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_qualification(
            conn, candidate_id=candidate_id,
            qualification_status="keep",
            qualification_reason="looks fine",
            confidence="high",
            rejection_reason="tutorial_or_demo",
        )


@pytest.mark.parametrize(
    "reason",
    [
        "single_incidental_use",
        "tutorial_or_demo",
        "fork_of_library",
        "archived_no_signal",
        "personal_project_no_customers",
        "other",
    ],
)
def test_every_documented_rejection_reason_is_accepted(conn, candidate_id, reason):
    storage.upsert_qualification(
        conn, candidate_id=candidate_id,
        qualification_status="reject",
        qualification_reason=f"matched {reason}",
        confidence="medium",
        rejection_reason=reason,
    )
    assert storage.get_qualification(conn, candidate_id)["rejection_reason"] == reason


def test_qualification_status_is_constrained(conn, candidate_id):
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_qualification(
            conn, candidate_id=candidate_id,
            qualification_status="maybe",
            qualification_reason="r", confidence="low",
        )


def test_list_candidates_by_status(conn, candidate_id, run_id):
    storage.insert_candidate_if_new(
        conn, candidate_id="c_two", repo_url="https://github.com/a/two",
        repo_owner="a", repo_name="two", first_seen_run_id=run_id,
    )
    storage.upsert_qualification(
        conn, candidate_id=candidate_id, qualification_status="keep",
        qualification_reason="r", confidence="high",
    )
    storage.upsert_qualification(
        conn, candidate_id="c_two", qualification_status="investigate",
        qualification_reason="r", confidence="low",
    )

    assert storage.list_candidates_by_status(conn, "keep") == [candidate_id]
    assert storage.list_candidates_by_status(conn, "investigate") == ["c_two"]
    assert storage.list_candidates_by_status(conn, "reject") == []


# --- scores ----------------------------------------------------------------


def _score(**overrides):
    base = dict(
        document_volume=4,
        document_complexity=5,
        business_criticality=5,
        pipeline_complexity=5,
        maintenance_burden=4,
        build_vs_buy_signal=4,
        commercial_leverage=5,
        raw_weighted_score=4.60,
        final_score=92,
        confidence_band="high",
    )
    base.update(overrides)
    return base


def test_upsert_and_get_score(conn, candidate_id):
    storage.upsert_score(conn, candidate_id=candidate_id, **_score())
    row = storage.get_score(conn, candidate_id)

    assert row["final_score"] == 92
    assert row["raw_weighted_score"] == pytest.approx(4.60)
    assert row["confidence_band"] == "high"
    assert row["gate_cap_applied"] is None
    assert storage.decode_unknown_dimensions(row["unknown_dimensions"]) == []


def test_unknown_dimensions_round_trip(conn, candidate_id):
    """The whole point of the field: a dimension that defaulted to 0 stays
    visible instead of being folded silently into the number."""
    storage.upsert_score(
        conn, candidate_id=candidate_id,
        **_score(maintenance_burden=0, raw_weighted_score=2.30, final_score=46,
                 confidence_band="medium"),
        unknown_dimensions=["maintenance_burden"],
    )
    row = storage.get_score(conn, candidate_id)

    assert storage.decode_unknown_dimensions(row["unknown_dimensions"]) == [
        "maintenance_burden"
    ]


def test_unknown_dimensions_are_stored_in_document_order(conn, candidate_id):
    """Two candidates with the same unknowns must produce the same string."""
    storage.upsert_score(
        conn, candidate_id=candidate_id, **_score(),
        unknown_dimensions=["commercial_leverage", "document_volume"],
    )
    row = storage.get_score(conn, candidate_id)

    assert storage.decode_unknown_dimensions(row["unknown_dimensions"]) == [
        "document_volume",
        "commercial_leverage",
    ]


def test_all_seven_dimensions_may_be_unknown(conn, candidate_id):
    storage.upsert_score(
        conn, candidate_id=candidate_id,
        **_score(**{d: 0 for d in SCORING_DIMENSIONS},
                 raw_weighted_score=0.0, final_score=0, confidence_band="low"),
        unknown_dimensions=list(SCORING_DIMENSIONS),
    )
    row = storage.get_score(conn, candidate_id)

    assert len(storage.decode_unknown_dimensions(row["unknown_dimensions"])) == 7


def test_unknown_dimensions_rejects_an_unrecognized_name(conn, candidate_id):
    """A typo here would quietly defeat the point of the field."""
    with pytest.raises(ValueError, match="Not scoring dimensions"):
        storage.upsert_score(
            conn, candidate_id=candidate_id, **_score(),
            unknown_dimensions=["maintenance_burdon"],
        )


@pytest.mark.parametrize("cap", [20, 25, 40])
def test_gate_caps_from_the_scoring_model_are_accepted(conn, candidate_id, cap):
    storage.upsert_score(
        conn, candidate_id=candidate_id,
        **_score(final_score=cap), gate_cap_applied=cap,
    )
    assert storage.get_score(conn, candidate_id)["gate_cap_applied"] == cap


@pytest.mark.parametrize("cap", [0, 33, 50, 100])
def test_a_retuned_gate_cap_is_accepted(conn, candidate_id, cap):
    """Schema version 2 deliberately allows any 0-100 cap.

    The caps live in weights.yaml so a person can retune them after seeing real
    candidates. A schema hardcoding today's 20/25/40 would reject a retuned cap
    and make that configurability a fiction. Which cap applies stays the
    scoring engine's decision.
    """
    storage.upsert_score(
        conn, candidate_id=candidate_id,
        **_score(final_score=cap), gate_cap_applied=cap,
    )
    assert storage.get_score(conn, candidate_id)["gate_cap_applied"] == cap


@pytest.mark.parametrize("cap", [-1, 101])
def test_a_gate_cap_outside_the_score_range_is_rejected(conn, candidate_id, cap):
    """Still bounded: a cap has to be expressible as a final_score."""
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_score(
            conn, candidate_id=candidate_id, **_score(), gate_cap_applied=cap
        )


@pytest.mark.parametrize("bad", [-1, 6])
def test_dimension_scores_must_be_zero_to_five(conn, candidate_id, bad):
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_score(
            conn, candidate_id=candidate_id, **_score(document_volume=bad)
        )


@pytest.mark.parametrize("bad", [-1, 101])
def test_final_score_must_be_zero_to_one_hundred(conn, candidate_id, bad):
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_score(
            conn, candidate_id=candidate_id, **_score(final_score=bad)
        )


def test_score_upsert_replaces_not_duplicates(conn, candidate_id):
    storage.upsert_score(conn, candidate_id=candidate_id, **_score())
    storage.upsert_score(
        conn, candidate_id=candidate_id, **_score(final_score=46)
    )
    assert storage.get_score(conn, candidate_id)["final_score"] == 46
    assert conn.execute("SELECT COUNT(*) FROM scores").fetchone()[0] == 1


def test_list_scores_ranked_descending(conn, candidate_id, run_id):
    storage.insert_candidate_if_new(
        conn, candidate_id="c_low", repo_url="https://github.com/a/low",
        repo_owner="a", repo_name="low", first_seen_run_id=run_id,
    )
    storage.upsert_score(conn, candidate_id=candidate_id, **_score(final_score=46))
    storage.upsert_score(conn, candidate_id="c_low", **_score(final_score=92))

    assert [r["final_score"] for r in storage.list_scores_ranked(conn)] == [92, 46]


def test_get_score_returns_none_for_an_unscored_candidate(conn, candidate_id):
    """A reject gets no row at all, not a zero. This is what that looks like
    from the read side."""
    assert storage.get_score(conn, candidate_id) is None


# --- evidence_trail --------------------------------------------------------


def test_insert_and_list_evidence_trail(conn, candidate_id):
    storage.insert_evidence_trail(
        conn,
        candidate_id=candidate_id,
        evidence_url="https://github.com/example-org/example-repo/blob/main/a.py#L18",
        evidence_type="code_permalink",
        evidence_excerpt="from docxtpl import DocxTemplate",
        source="github_code_search",
    )
    rows = storage.list_evidence_trail_for_candidate(conn, candidate_id)

    assert len(rows) == 1
    assert rows[0]["evidence_type"] == "code_permalink"
    assert rows[0]["evidence_excerpt"] == "from docxtpl import DocxTemplate"
    assert rows[0]["collected_at"]


def test_evidence_trail_accumulates_many_entries(conn, candidate_id):
    for i in range(3):
        storage.insert_evidence_trail(
            conn, candidate_id=candidate_id,
            evidence_url=f"https://x/{i}", evidence_type="other", source="manual",
        )
    assert len(storage.list_evidence_trail_for_candidate(conn, candidate_id)) == 3


def test_evidence_type_is_constrained(conn, candidate_id):
    with pytest.raises(sqlite3.IntegrityError):
        storage.insert_evidence_trail(
            conn, candidate_id=candidate_id, evidence_url="https://x",
            evidence_type="hearsay", source="manual",
        )


def test_evidence_trail_requires_a_real_candidate(conn):
    with pytest.raises(sqlite3.IntegrityError):
        storage.insert_evidence_trail(
            conn, candidate_id="ghost", evidence_url="https://x",
            evidence_type="other", source="manual",
        )


# --- api_cache -------------------------------------------------------------


def test_put_and_get_api_cache(conn):
    storage.put_api_cache(
        conn, cache_key="sha256:abc", response_json='{"items": []}'
    )
    row = storage.get_api_cache(conn, "sha256:abc")

    assert row["response_json"] == '{"items": []}'
    assert row["fetched_at"]


def test_get_api_cache_returns_none_on_miss(conn):
    assert storage.get_api_cache(conn, "never-fetched") is None


def test_put_api_cache_replaces_an_existing_entry(conn):
    storage.put_api_cache(conn, cache_key="k", response_json="old")
    storage.put_api_cache(conn, cache_key="k", response_json="new")

    assert storage.get_api_cache(conn, "k")["response_json"] == "new"
    assert conn.execute("SELECT COUNT(*) FROM api_cache").fetchone()[0] == 1


def test_delete_api_cache(conn):
    storage.put_api_cache(conn, cache_key="k", response_json="v")

    assert storage.delete_api_cache(conn, "k") is True
    assert storage.get_api_cache(conn, "k") is None
    assert storage.delete_api_cache(conn, "k") is False


# --- cross-cutting ---------------------------------------------------------


def test_evidence_tables_reject_unknown_candidates(conn, run_id):
    """Foreign keys hold across every child table."""
    with pytest.raises(sqlite3.IntegrityError):
        storage.upsert_pipeline_evidence(
            conn, candidate_id="ghost", code_usage_confirmed=False,
            template_directory_present=False,
            multiple_document_types_handled=False, pipeline_stage_count=0,
            infrastructure_service_present=False,
        )


def test_deleting_a_candidate_cascades_to_its_evidence(conn, candidate_id, run_id):
    query_id = _query(conn, run_id, query="q")
    storage.insert_discovery_evidence(conn, query_id=query_id, candidate_id=candidate_id)
    storage.insert_evidence_trail(
        conn, candidate_id=candidate_id, evidence_url="https://x",
        evidence_type="other", source="manual",
    )
    conn.execute("DELETE FROM candidates WHERE candidate_id = ?", (candidate_id,))

    assert storage.list_discovery_evidence_for_candidate(conn, candidate_id) == []
    assert storage.list_evidence_trail_for_candidate(conn, candidate_id) == []
