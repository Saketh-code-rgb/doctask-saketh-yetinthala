"""The qualification engine: keep, investigate, reject.

Every test is a synthetic fixture over stored evidence. Nothing here touches
the network, and the real-product cases are modelled on what the phase 8 live
run actually observed rather than on invented records.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dependency_map import storage
from dependency_map.dedup import make_candidate_id, normalize_repo_url
from dependency_map.qualification import (
    ARCHIVED_NO_SIGNAL,
    FORK_OF_LIBRARY,
    HIGH,
    INVESTIGATE,
    KEEP,
    LOW,
    MEDIUM,
    PERSONAL_PROJECT_NO_CUSTOMERS,
    REJECT,
    SINGLE_INCIDENTAL_USE,
    TUTORIAL_OR_DEMO,
    CandidateEvidence,
    QualificationEngine,
    qualify,
)


# --- fixture builder -------------------------------------------------------


def seed(
    conn, run_id, name="acme/widget", *,
    is_fork=False, is_archived=False, company=None, industry="unknown",
    dependencies=(),
    code_usage=False, templates=False, multi_types=False, stages=0, infra=False,
    describes_product=False, excerpt=None, website=False, app_code=False,
    in_production=False, stars=10, contributors=None,
    pipeline_evidence=True, business_evidence=True,
):
    """Write one candidate's evidence, then return its id.

    Defaults are deliberately bare so each test states only the evidence it
    cares about.
    """
    url = f"https://github.com/{name}"
    cid = make_candidate_id(url)
    owner, _, repo = name.partition("/")

    query_id = storage.create_discovery_query(
        conn, run_id=run_id, discovery_source="github_code_search",
        query="q", library_name="python-docx", discovery_tier=3,
    )
    storage.insert_candidate_if_new(
        conn, candidate_id=cid, repo_url=normalize_repo_url(url),
        repo_owner=owner, repo_name=repo, first_seen_run_id=run_id,
        is_fork=is_fork, is_archived=is_archived,
        company_name=company,
        company_name_source="readme" if company else None,
        industry_category=industry,
    )
    storage.insert_discovery_evidence(conn, query_id=query_id, candidate_id=cid)

    for index, dep in enumerate(dependencies):
        storage.insert_dependency_found(
            conn, candidate_id=cid,
            library_name=dep.get("library", f"lib-{index}"),
            library_category=dep.get("category", "docx"),
            direction=dep.get("direction", "generation"),
            detection_method=dep.get("method", "manifest_declaration"),
            evidence_url=dep.get("url", f"https://github.com/{name}/blob/main/f{index}"),
            manifest_file=dep.get("manifest"),
        )

    if pipeline_evidence:
        storage.upsert_pipeline_evidence(
            conn, candidate_id=cid,
            code_usage_confirmed=code_usage,
            template_directory_present=templates,
            multiple_document_types_handled=multi_types,
            pipeline_stage_count=stages,
            infrastructure_service_present=infra,
            pipeline_evidence_notes="synthetic fixture",
        )
    if business_evidence:
        storage.upsert_business_evidence(
            conn, candidate_id=cid,
            readme_describes_product=describes_product,
            readme_excerpt=excerpt or ("A product for our customers."
                                       if describes_product else None),
            website_exists=website,
            application_code_exists=app_code,
            document_functionality_in_production_code=in_production,
            stars=stars, last_commit_date="2026-07-01",
            contributor_count=contributors,
            business_evidence_notes="synthetic fixture",
        )
    return cid


def decide(conn, cid):
    return qualify(CandidateEvidence.load(conn, cid))


MANIFEST = {"method": "manifest_declaration", "manifest": "requirements.txt"}
CODE = {"method": "code_import"}
INFRA_DEP = {"method": "infrastructure_reference", "category": "conversion",
             "direction": "conversion"}


# --- 1. clear keep ---------------------------------------------------------


def test_clear_keep(conn, run_id):
    """Real product, production document workflow, multiple signals."""
    cid = seed(
        conn, run_id, "clauseforge/lease-engine",
        dependencies=[
            {**CODE, "category": "template_generation", "direction": "generation"},
            {**CODE, "category": "pdf", "direction": "conversion"},
        ],
        code_usage=True, templates=True, multi_types=True, stages=3,
        describes_product=True, app_code=True, in_production=True, website=True,
        industry="real_estate",
    )
    decision = decide(conn, cid)

    assert decision.status == KEEP
    assert decision.rejection_reason is None
    assert decision.confidence == HIGH


def test_keep_reason_cites_real_field_values(conn, run_id):
    cid = seed(
        conn, run_id,
        dependencies=[{**CODE, "category": "template_generation"},
                      {**CODE, "category": "pdf"}],
        code_usage=True, templates=True, multi_types=True, stages=3,
        describes_product=True, app_code=True, in_production=True,
    )
    reason = decide(conn, cid).reason

    assert "readme_describes_product=true" in reason
    assert "application_code_exists=true" in reason
    assert "document_functionality_in_production_code=true" in reason
    assert "category_count=2" in reason


def test_keep_requires_all_four_gate_fields(conn, run_id):
    """CANDIDATE_SCHEMA.md section 6: they have to hold together."""
    for missing in ("describes_product", "app_code", "in_production"):
        kwargs = dict(
            dependencies=[{**CODE, "category": "template_generation"},
                          {**CODE, "category": "pdf"}],
            code_usage=True, templates=True, multi_types=True, stages=3,
            describes_product=True, app_code=True, in_production=True,
        )
        kwargs[missing] = False
        cid = seed(conn, run_id, f"org/{missing}", **kwargs)

        assert decide(conn, cid).status != KEEP, missing


def test_keep_needs_a_supporting_signal(conn, run_id):
    """All four gates met but nothing showing the workflow is more than an
    isolated utility."""
    cid = seed(
        conn, run_id, dependencies=[{**CODE, "direction": "extraction"}],
        code_usage=True, stages=1, describes_product=True, app_code=True,
        in_production=True,
    )
    decision = decide(conn, cid)

    assert decision.status == INVESTIGATE
    assert "isolated utility" in decision.reason


# --- 2 to 6. clear rejects -------------------------------------------------


def test_reject_tutorial_or_demo(conn, run_id):
    """The docutils-sandbox shape from SCORING_MODEL.md section 15: four
    document libraries, and none of them in a product."""
    cid = seed(
        conn, run_id, "someone/docutils-examples",
        dependencies=[MANIFEST, {**MANIFEST, "category": "pdf"},
                      {**MANIFEST, "category": "template_generation"}],
        describes_product=False, app_code=False, in_production=False,
    )
    decision = decide(conn, cid)

    assert decision.status == REJECT
    assert decision.rejection_reason == TUTORIAL_OR_DEMO
    assert "application_code_exists=false" in decision.reason


def test_reject_fork_of_library(conn, run_id):
    cid = seed(conn, run_id, "someone/python-docx", is_fork=True,
               dependencies=[MANIFEST])
    decision = decide(conn, cid)

    assert decision.status == REJECT
    assert decision.rejection_reason == FORK_OF_LIBRARY
    assert "is_fork=true" in decision.reason


def test_reject_archived_no_signal(conn, run_id):
    cid = seed(conn, run_id, "org/old-tool", is_archived=True,
               dependencies=[MANIFEST], describes_product=False)
    decision = decide(conn, cid)

    assert decision.status == REJECT
    assert decision.rejection_reason == ARCHIVED_NO_SIGNAL


def test_reject_personal_playground(conn, run_id):
    cid = seed(conn, run_id, "someuser/python-playground",
               dependencies=[MANIFEST], describes_product=False, app_code=False)
    decision = decide(conn, cid)

    assert decision.status == REJECT
    assert decision.rejection_reason == PERSONAL_PROJECT_NO_CUSTOMERS
    assert "playground" in decision.reason


def test_reject_single_incidental_use(conn, run_id):
    cid = seed(conn, run_id, "org/data-tool",
               dependencies=[{**CODE, "category": "docx"}],
               code_usage=True, stages=1, app_code=True, in_production=True,
               describes_product=False)
    decision = decide(conn, cid)

    assert decision.status == REJECT
    assert decision.rejection_reason == SINGLE_INCIDENTAL_USE
    assert "category_count=1" in decision.reason


# --- 7 and 8. investigate --------------------------------------------------


def test_investigate_real_product_unclear_document_integration(conn, run_id):
    """The docbase shape: a stated product, manifest-only document evidence."""
    cid = seed(conn, run_id, "org/docbase", dependencies=[MANIFEST],
               describes_product=True, app_code=True, website=True,
               in_production=False, code_usage=False)
    decision = decide(conn, cid)

    assert decision.status == INVESTIGATE
    assert decision.rejection_reason is None


def test_investigate_strong_document_evidence_weak_product_evidence(conn, run_id):
    """The PurpleOps shape: real pipeline, README never says who it is for."""
    cid = seed(
        conn, run_id, "org/reporting-tool",
        dependencies=[{**CODE, "category": "template_generation"}],
        code_usage=True, templates=True, stages=2, app_code=True,
        in_production=True, describes_product=False,
    )
    decision = decide(conn, cid)

    assert decision.status == INVESTIGATE
    assert "template_directory_present=true" in " ".join(decision.supporting_signals)


def test_investigate_when_no_evidence_was_collected(conn, run_id):
    """Nothing looked at is a gap, not a finding."""
    cid = seed(conn, run_id, "org/unknown", dependencies=[],
               pipeline_evidence=False, business_evidence=False)
    decision = decide(conn, cid)

    assert decision.status == INVESTIGATE
    assert decision.confidence == LOW


@pytest.mark.parametrize("pipeline,business", [(False, False), (True, False),
                                               (False, True)])
def test_uncollected_evidence_can_never_produce_a_rejection(
    conn, run_id, pipeline, business
):
    """Regression, and the most important rule in the module.

    Every negative field on a candidate whose evidence was never collected
    reads as false, so the rejection predicates would fire on a record nobody
    looked at. A repository named `org/examples` with no evidence rows matched
    tutorial_or_demo on three bare falses, which is confirmed absence
    manufactured out of an absent measurement.
    """
    cid = seed(conn, run_id, "org/examples", dependencies=[],
               pipeline_evidence=pipeline, business_evidence=business)
    decision = decide(conn, cid)

    assert decision.status == INVESTIGATE
    assert decision.rejection_reason is None
    assert "evidence not collected" in decision.reason
    assert decision.confidence == LOW


def test_a_tutorial_named_repo_without_evidence_is_not_rejected(conn, run_id):
    """The exact shape that exposed the bug."""
    cid = seed(conn, run_id, "someone/python-tutorial", dependencies=[],
               pipeline_evidence=False, business_evidence=False)

    assert decide(conn, cid).status == INVESTIGATE


def test_unclear_candidates_are_never_forced(conn, run_id):
    cid = seed(conn, run_id, "org/ambiguous", dependencies=[MANIFEST],
               describes_product=True, app_code=True)
    decision = decide(conn, cid)

    assert decision.status == INVESTIGATE


# --- 9. cases modelled on the phase 8 live evidence ------------------------


def test_live_shape_bigcapital(conn, run_id):
    """Deployed Gotenberg, confirmed code, product framing, but the collector
    read no application directory at the root of a monorepo."""
    cid = seed(
        conn, run_id, "bigcapitalhq/bigcapital",
        dependencies=[INFRA_DEP, {**CODE, "category": "conversion",
                                  "direction": "conversion"}],
        code_usage=True, infra=True, stages=1,
        describes_product=True, app_code=False, in_production=True,
        website=True, stars=3846, industry="finance_investment",
    )
    decision = decide(conn, cid)

    assert decision.status == INVESTIGATE
    assert "application_code_exists" in decision.reason
    assert "infrastructure_service_present=true" in " ".join(decision.supporting_signals)


def test_live_shape_purpleops(conn, run_id):
    cid = seed(
        conn, run_id, "CyberCX-STA/PurpleOps",
        dependencies=[MANIFEST, {**CODE, "category": "template_generation"}],
        code_usage=True, templates=True, stages=2, app_code=True,
        in_production=True, describes_product=False, website=True,
        stars=313, industry="legal_contracts",
    )
    decision = decide(conn, cid)

    assert decision.status == INVESTIGATE, "a real product must not be rejected"
    assert decision.rejection_reason is None


def test_live_shape_docbase(conn, run_id):
    cid = seed(
        conn, run_id, "alanagoyal/docbase", dependencies=[MANIFEST, MANIFEST],
        describes_product=True, excerpt="Docbase is an all-in-one Docsend alternative.",
        app_code=True, website=True, in_production=False, code_usage=False,
        stars=233, industry="unknown",
    )
    decision = decide(conn, cid)

    assert decision.status == INVESTIGATE
    assert decision.confidence == LOW, "manifest-only evidence is weakly supported"


def test_live_shape_sambanova(conn, run_id):
    """Four nested manifest declarations, no call site, a starter kit."""
    cid = seed(
        conn, run_id, "sambanova/ai-starter-kit",
        dependencies=[MANIFEST, MANIFEST, MANIFEST, MANIFEST],
        code_usage=False, app_code=False, in_production=False,
        describes_product=False, stars=251,
    )
    decision = decide(conn, cid)

    assert decision.status == REJECT
    assert decision.rejection_reason == TUTORIAL_OR_DEMO


def test_live_shape_traprange(conn, run_id):
    """A PDF tool: confirmed usage, application code, no product framing."""
    cid = seed(
        conn, run_id, "thoqbk/traprange",
        dependencies=[{**MANIFEST, "category": "pdf", "manifest": "pom.xml"},
                      {**CODE, "category": "pdf"}],
        code_usage=True, stages=1, app_code=True, in_production=True,
        describes_product=False, stars=340,
    )
    decision = decide(conn, cid)

    assert decision.status == REJECT
    assert decision.rejection_reason == SINGLE_INCIDENTAL_USE


# --- 17. regressions from the live-run lessons -----------------------------


def test_A_nested_manifests_without_code_are_not_code_confirmed(conn, run_id):
    cid = seed(conn, run_id, "org/nested",
               dependencies=[MANIFEST, MANIFEST, MANIFEST],
               code_usage=False, describes_product=True, app_code=True)
    evidence = CandidateEvidence.load(conn, cid)

    assert evidence.manifest_only is True
    assert evidence.code_usage_confirmed is False
    assert evidence.confirmed_dependency_count == 0
    assert decide(conn, cid).status == INVESTIGATE


def test_B_readme_evidence_never_counts_as_confirmed_usage(conn, run_id):
    """Enforced upstream in the collector; asserted here so qualification
    cannot quietly start treating a declaration as a call site."""
    cid = seed(conn, run_id, "org/readme-only",
               dependencies=[{**MANIFEST, "manifest": "README.md"}],
               code_usage=False, describes_product=True, app_code=True)
    evidence = CandidateEvidence.load(conn, cid)

    assert evidence.confirmed_dependency_count == 0
    assert evidence.produces_documents is False


def test_C_unknown_industry_never_rejects(conn, run_id):
    cid = seed(
        conn, run_id, "org/unknown-industry", industry="unknown",
        dependencies=[{**CODE, "category": "template_generation"},
                      {**CODE, "category": "pdf"}],
        code_usage=True, templates=True, multi_types=True, stages=3,
        describes_product=True, app_code=True, in_production=True,
    )
    decision = decide(conn, cid)

    assert decision.status == KEEP, "unknown industry must not block a keep"
    assert decision.rejection_reason is None


def test_C_industry_alone_never_determines_status(conn, run_id):
    """Same evidence, different industry, same answer."""
    statuses = set()
    for index, industry in enumerate(
        ["unknown", "legal_contracts", "healthcare_diagnostics", "other"]
    ):
        cid = seed(
            conn, run_id, f"org/industry-{index}", industry=industry,
            dependencies=[{**CODE, "category": "template_generation"},
                          {**CODE, "category": "pdf"}],
            code_usage=True, templates=True, multi_types=True, stages=3,
            describes_product=True, app_code=True, in_production=True,
        )
        statuses.add(decide(conn, cid).status)

    assert statuses == {KEEP}


def test_D_missing_company_name_never_rejects(conn, run_id):
    cid = seed(
        conn, run_id, "org/no-company", company=None,
        dependencies=[{**CODE, "category": "template_generation"},
                      {**CODE, "category": "pdf"}],
        code_usage=True, templates=True, multi_types=True, stages=3,
        describes_product=True, app_code=True, in_production=True,
    )
    decision = decide(conn, cid)

    assert decision.status == KEEP
    assert "company_name=null" in " ".join(decision.unknowns)


def test_E_real_product_with_unclear_document_use_investigates(conn, run_id):
    cid = seed(conn, run_id, "org/real-product", dependencies=[MANIFEST],
               describes_product=True, app_code=True, website=True,
               company="Acme Inc.", code_usage=False)
    decision = decide(conn, cid)

    assert decision.status == INVESTIGATE
    assert decision.rejection_reason is None


def test_F_a_tool_repository_rejects_despite_many_dependencies(conn, run_id):
    """Dependency count alone never rescues a candidate."""
    cid = seed(
        conn, run_id, "someone/pdf-toolkit",
        dependencies=[MANIFEST, MANIFEST, MANIFEST, MANIFEST, MANIFEST],
        code_usage=False, describes_product=False, app_code=False,
        in_production=False,
    )
    decision = decide(conn, cid)

    assert decision.status == REJECT


# --- fields that must never reject on their own ----------------------------


@pytest.mark.parametrize("field_kwargs,label", [
    ({"stars": 0}, "low stars"),
    ({"contributors": 1}, "one contributor"),
    ({"website": False}, "no website"),
    ({"company": None}, "no company"),
    ({"industry": "unknown"}, "unknown industry"),
])
def test_weak_signals_alone_do_not_reject(conn, run_id, field_kwargs, label):
    base = dict(
        dependencies=[{**CODE, "category": "template_generation"},
                      {**CODE, "category": "pdf"}],
        code_usage=True, templates=True, multi_types=True, stages=3,
        describes_product=True, app_code=True, in_production=True,
    )
    base.update(field_kwargs)
    cid = seed(conn, run_id, f"org/{label.replace(' ', '-')}", **base)

    assert decide(conn, cid).status == KEEP, label


def test_a_fork_that_became_a_product_is_not_auto_rejected(conn, run_id):
    cid = seed(conn, run_id, "org/forked-product", is_fork=True,
               dependencies=[{**CODE, "category": "template_generation"}],
               code_usage=True, templates=True, stages=2,
               describes_product=True, app_code=True, in_production=True)
    decision = decide(conn, cid)

    assert decision.status == INVESTIGATE
    assert decision.rejection_reason is None


def test_an_archived_product_with_signal_is_not_auto_rejected(conn, run_id):
    cid = seed(conn, run_id, "org/archived-product", is_archived=True,
               dependencies=[{**CODE, "category": "template_generation"}],
               code_usage=True, templates=True, stages=2,
               describes_product=True, app_code=True, in_production=True)

    assert decide(conn, cid).status != REJECT


def test_a_small_repository_is_not_a_tutorial(conn, run_id):
    cid = seed(conn, run_id, "org/small-product", dependencies=[MANIFEST],
               describes_product=True, app_code=True, stars=1)

    assert decide(conn, cid).status == INVESTIGATE


def test_a_demo_named_repo_with_a_product_is_not_rejected(conn, run_id):
    """A name token alone is never enough."""
    cid = seed(conn, run_id, "org/demo-platform",
               dependencies=[{**CODE, "category": "template_generation"}],
               code_usage=True, templates=True, stages=2,
               describes_product=True, app_code=True, in_production=True)

    assert decide(conn, cid).status != REJECT


def test_name_tokens_match_on_word_boundaries(conn, run_id):
    """"example" must not fire on "exampleforge"; the lesson from the phase 8
    substring bug applies to repository names too."""
    cid = seed(conn, run_id, "org/exampleforge", dependencies=[MANIFEST],
               describes_product=False, app_code=True, in_production=True,
               code_usage=True, templates=True, stages=2)
    decision = decide(conn, cid)

    assert decision.rejection_reason != TUTORIAL_OR_DEMO


# --- constraints and determinism -------------------------------------------


def test_rejection_reason_is_set_only_for_rejects(conn, run_id):
    reject = seed(conn, run_id, "someone/python-docx", is_fork=True,
                  dependencies=[MANIFEST])
    keep = seed(
        conn, run_id, "org/keeper",
        dependencies=[{**CODE, "category": "template_generation"},
                      {**CODE, "category": "pdf"}],
        code_usage=True, templates=True, multi_types=True, stages=3,
        describes_product=True, app_code=True, in_production=True,
    )

    assert decide(conn, reject).rejection_reason is not None
    assert decide(conn, keep).rejection_reason is None


def test_results_persist_and_satisfy_the_schema_constraint(conn, run_id):
    cid = seed(conn, run_id, "someone/python-docx", is_fork=True,
               dependencies=[MANIFEST])
    QualificationEngine(conn).qualify_candidate(cid)

    row = storage.get_qualification(conn, cid)
    assert row["qualification_status"] == REJECT
    assert row["rejection_reason"] == FORK_OF_LIBRARY
    assert row["confidence"] in (HIGH, MEDIUM, LOW)


def test_qualification_is_deterministic(conn, run_id):
    """Same evidence in, same decision out, every time."""
    cid = seed(conn, run_id, "org/stable", dependencies=[MANIFEST, CODE],
               code_usage=True, describes_product=True, app_code=True,
               in_production=True, templates=True, stages=2)

    decisions = [decide(conn, cid) for _ in range(5)]
    assert len({(d.status, d.reason, d.rejection_reason, d.confidence)
                for d in decisions}) == 1


def test_rerunning_the_engine_is_idempotent(conn, run_id):
    cid = seed(conn, run_id, "org/stable", dependencies=[MANIFEST],
               describes_product=True, app_code=True)
    engine = QualificationEngine(conn)

    engine.qualify_candidate(cid)
    first = dict(storage.get_qualification(conn, cid))
    engine.qualify_candidate(cid)
    second = dict(storage.get_qualification(conn, cid))

    assert first == second


def test_every_candidate_with_evidence_receives_a_status(conn, run_id):
    for index in range(4):
        seed(conn, run_id, f"org/repo-{index}", dependencies=[MANIFEST])
    report = QualificationEngine(conn).run()

    assert report.processed == 4
    assert report.keep + report.investigate + report.reject == 4


def test_pending_excludes_already_qualified(conn, run_id):
    cid = seed(conn, run_id, "org/one", dependencies=[MANIFEST])
    engine = QualificationEngine(conn)

    assert engine.pending() == [cid]
    engine.run()
    assert engine.pending() == []


def test_candidates_without_evidence_are_not_pending(conn, run_id):
    seed(conn, run_id, "org/no-evidence", pipeline_evidence=False,
         business_evidence=False)

    assert QualificationEngine(conn).pending() == []


# --- confidence ------------------------------------------------------------


def test_confidence_never_changes_the_status(conn, run_id):
    cid = seed(
        conn, run_id, "org/low-confidence-keep",
        dependencies=[{**CODE, "category": "docx", "direction": "extraction"}],
        code_usage=True, templates=True, stages=1,
        describes_product=True, app_code=True, in_production=True,
    )
    decision = decide(conn, cid)

    assert decision.status == KEEP
    assert decision.supporting_signals == ("template_directory_present=true",)
    assert decision.confidence == MEDIUM, "one supporting signal only"


def test_missing_evidence_rows_give_low_confidence(conn, run_id):
    cid = seed(conn, run_id, "org/thin", pipeline_evidence=False,
               business_evidence=False)

    assert decide(conn, cid).confidence == LOW


def test_unknowns_are_listed(conn, run_id):
    cid = seed(conn, run_id, "org/gappy", dependencies=[MANIFEST])
    unknown_text = " ".join(decide(conn, cid).unknowns)

    assert "manifest-only" in unknown_text
    assert "industry_category=unknown" in unknown_text


# --- scope and safety ------------------------------------------------------


def test_qualification_makes_no_network_calls():
    source = Path("src/dependency_map/qualification.py").read_text(encoding="utf-8")

    for forbidden in ["import requests", "urllib", "http.client", "socket",
                      "GitHubClient", "LibrariesIOClient", "ReliableRequester",
                      "RequestsTransport"]:
        assert forbidden not in source


def test_qualification_does_no_scoring():
    source = Path("src/dependency_map/qualification.py").read_text(encoding="utf-8")

    for term in ["final_score", "raw_weighted_score", "upsert_score",
                 "weights.yaml", "gate_cap", "confidence_band"]:
        assert term not in source


def test_the_report_module_now_exists():
    """report.py arrived at phase 11."""
    assert Path("src/dependency_map", "report.py").exists()
