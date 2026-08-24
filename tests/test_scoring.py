"""The scoring engine: seven rubrics, weights, caps, confidence.

The three worked examples from SCORING_MODEL.md section 15 are literal
fixtures, and their expected numbers are authoritative. Nothing here touches
the network.
"""

from __future__ import annotations

from decimal import Decimal
from pathlib import Path

import pytest
import yaml

from dependency_map import storage
from dependency_map.db import SCORING_DIMENSIONS
from dependency_map.qualification import (
    CandidateEvidence,
    QualificationEngine,
    REJECT,
)
from dependency_map.scoring import (
    BAND_HIGH,
    BAND_LOW,
    BAND_MEDIUM,
    GATE_CODE_USAGE,
    GATE_OUTSIDE_PRODUCTION,
    GATE_SINGLE_CATEGORY,
    ScoringEngine,
    ScoringError,
    apply_gate_caps,
    assess_confidence_band,
    compute_final_score,
    compute_raw_weighted_score,
    score_candidate,
)
from test_qualification import CODE, INFRA_DEP, MANIFEST, seed


@pytest.fixture(scope="module")
def config_weights():
    data = yaml.safe_load(Path("config/weights.yaml").read_text(encoding="utf-8"))
    return data["dimension_weights"], data["gate_caps"]


@pytest.fixture
def weights(config_weights):
    return config_weights[0]


@pytest.fixture
def caps(config_weights):
    return config_weights[1]


def evidence_for(conn, cid):
    return CandidateEvidence.load(conn, cid)


# --- the three synthetic examples, SCORING_MODEL.md section 15 -------------
#
# Scored from dimension values directly, because these are the document's own
# worked examples: the point is that the arithmetic, weights and rounding
# reproduce its numbers exactly.


def raw_and_final(scores, weights):
    raw = compute_raw_weighted_score(scores, weights)
    return raw, compute_final_score(raw)


MEDREPORT = dict(
    document_volume=4, document_complexity=5, business_criticality=5,
    pipeline_complexity=5, maintenance_burden=4, build_vs_buy_signal=4,
    commercial_leverage=5,
)
ESTATEPROPOSAL = dict(
    document_volume=2, document_complexity=3, business_criticality=3,
    pipeline_complexity=3, maintenance_burden=0, build_vs_buy_signal=3,
    commercial_leverage=1,
)


def test_medreport_solutions_scores_92(weights):
    """SCORING_MODEL.md section 15, example 1. Authoritative."""
    raw, final = raw_and_final(MEDREPORT, weights)

    assert raw == Decimal("4.60")
    assert final == 92


def test_medreport_confidence_is_high():
    """All seven dimensions directly evidenced, qualification confidence high."""
    assert assess_confidence_band(7, "high") == BAND_HIGH


def test_estateproposal_scores_46(weights):
    """SCORING_MODEL.md section 15, example 2. Authoritative."""
    raw, final = raw_and_final(ESTATEPROPOSAL, weights)

    assert raw == Decimal("2.30")
    assert final == 46


def test_estateproposal_confidence_is_medium():
    """Six of seven evidenced, but the candidate only reached investigate, so
    the corrected section 13 fallback puts it at medium rather than high."""
    assert assess_confidence_band(6, "medium") == BAND_MEDIUM


def test_estateproposals_unknown_costs_it_exactly_its_weight(weights):
    """The unknown maintenance_burden is visibly costing 15 weighted points,
    which is the tradeoff section 12 accepts rather than hides."""
    raw_unknown, final_unknown = raw_and_final(ESTATEPROPOSAL, weights)
    raw_full, final_full = raw_and_final(
        {**ESTATEPROPOSAL, "maintenance_burden": 5}, weights)

    assert raw_full - raw_unknown == Decimal("0.75")   # 5 * 0.15
    assert final_full - final_unknown == 15


def test_docutils_sandbox_is_rejected_and_never_scored(conn, run_id, weights, caps):
    """SCORING_MODEL.md section 15, example 3. Four document libraries, more
    than either other example declares, and it still never reaches scoring."""
    cid = seed(
        conn, run_id, "someone/docutils-sandbox",
        dependencies=[MANIFEST, {**MANIFEST, "category": "pdf"},
                      {**MANIFEST, "category": "template_generation"},
                      {**MANIFEST, "category": "other_processing"}],
        describes_product=False, app_code=False, in_production=False,
    )
    QualificationEngine(conn).run()

    assert storage.get_qualification(conn, cid)["qualification_status"] == REJECT

    report = ScoringEngine(conn, weights, caps).run([cid])

    assert storage.get_score(conn, cid) is None, "a reject gets no row at all"
    assert report.scored == 0
    assert report.skipped_rejected == 1


def test_a_reject_is_not_scored_zero(conn, run_id, weights, caps):
    """Not a zero: a numeric zero beside a company name still invites
    comparison, which section 1 exists to prevent."""
    cid = seed(conn, run_id, "someone/python-docx", is_fork=True,
               dependencies=[MANIFEST])
    QualificationEngine(conn).run()
    ScoringEngine(conn, weights, caps).run([cid])

    assert storage.get_score(conn, cid) is None


def test_rejects_are_excluded_from_pending(conn, run_id, weights, caps):
    seed(conn, run_id, "someone/python-docx", is_fork=True, dependencies=[MANIFEST])
    keeper = seed(
        conn, run_id, "org/keeper",
        dependencies=[{**CODE, "category": "template_generation"},
                      {**CODE, "category": "pdf"}],
        code_usage=True, templates=True, multi_types=True, stages=3,
        describes_product=True, app_code=True, in_production=True)
    QualificationEngine(conn).run()

    assert ScoringEngine(conn, weights, caps).pending() == [keeper]


# --- the formula -----------------------------------------------------------


def test_weights_are_read_from_config_not_hardcoded():
    source = Path("src/dependency_map/scoring.py").read_text(encoding="utf-8")

    for literal in ["0.15", "0.20", "0.10", "0.05"]:
        assert literal not in source, f"{literal} is hardcoded in scoring.py"


def test_gate_caps_are_read_from_config_not_hardcoded():
    source = Path("src/dependency_map/scoring.py").read_text(encoding="utf-8")

    for literal in ["= 20", "= 25", "= 40", "(20", "(25", "(40"]:
        assert literal not in source


def test_unknown_weight_is_not_redistributed(weights):
    """Section 12's second rejected alternative. The missing 15 percent stays
    missing rather than flowing to the dimensions that were checked."""
    all_five = {d: 5 for d in SCORING_DIMENSIONS}
    one_unknown = {**all_five, "maintenance_burden": 0}

    raw_full = compute_raw_weighted_score(all_five, weights)
    raw_gap = compute_raw_weighted_score(one_unknown, weights)

    assert raw_full == Decimal("5.00")
    assert raw_gap == Decimal("4.25")   # not rescaled back up to 5


def test_perfect_and_empty_bounds(weights):
    assert compute_final_score(
        compute_raw_weighted_score({d: 5 for d in SCORING_DIMENSIONS}, weights)) == 100
    assert compute_final_score(
        compute_raw_weighted_score({d: 0 for d in SCORING_DIMENSIONS}, weights)) == 0


def test_rounding_is_half_up():
    """Python's built-in round() is banker's rounding and would give 46 for
    46.5. A reader checking the arithmetic by hand rounds half up."""
    assert compute_final_score(Decimal("2.325")) == 47   # 46.5 -> 47


def test_missing_weight_dimension_is_refused(conn, run_id, caps):
    cid = seed(conn, run_id, dependencies=[MANIFEST])
    partial = {d: 0.2 for d in list(SCORING_DIMENSIONS)[:5]}

    with pytest.raises(ScoringError, match="missing dimensions"):
        score_candidate(evidence_for(conn, cid), partial, caps)


def test_unknown_weight_dimension_is_refused(conn, run_id, weights, caps):
    cid = seed(conn, run_id, dependencies=[MANIFEST])

    with pytest.raises(ScoringError, match="unknown dimensions"):
        score_candidate(evidence_for(conn, cid), {**weights, "vibes": 0.0}, caps)


# --- gate caps -------------------------------------------------------------


def test_gate_a_code_usage_unconfirmed_caps_at_20(caps):
    capped, applied = apply_gate_caps(88, [GATE_CODE_USAGE], caps)

    assert capped == 20
    assert applied == 20


def test_gate_b_outside_production_caps_at_25(caps):
    capped, applied = apply_gate_caps(88, [GATE_OUTSIDE_PRODUCTION], caps)

    assert capped == 25
    assert applied == 25


def test_gate_c_single_category_caps_at_40(caps):
    capped, applied = apply_gate_caps(88, [GATE_SINGLE_CATEGORY], caps)

    assert capped == 40
    assert applied == 40


def test_multiple_gates_apply_the_smallest_cap(caps):
    capped, applied = apply_gate_caps(
        88, [GATE_SINGLE_CATEGORY, GATE_OUTSIDE_PRODUCTION, GATE_CODE_USAGE], caps)

    assert capped == 20, "smallest applicable cap wins"
    assert applied == 20


def test_no_gates_means_no_cap(caps):
    assert apply_gate_caps(88, [], caps) == (88, None)


def test_a_cap_above_the_score_is_not_recorded_as_applied(caps):
    """A candidate scoring 12 with a cap of 20 is not being capped, and saying
    so would misdescribe the record."""
    capped, applied = apply_gate_caps(12, [GATE_CODE_USAGE], caps)

    assert capped == 12
    assert applied is None


def test_a_retuned_cap_works(conn, run_id, weights):
    """Schema V2 accepts any 0-100 cap, so a retuned weights.yaml takes effect
    without a schema change."""
    retuned = {GATE_CODE_USAGE: 33, GATE_OUTSIDE_PRODUCTION: 25,
               GATE_SINGLE_CATEGORY: 40}
    capped, applied = apply_gate_caps(88, [GATE_CODE_USAGE], retuned)

    assert capped == 33 and applied == 33

    cid = seed(conn, run_id, "org/retuned", dependencies=[MANIFEST],
               describes_product=True, app_code=True, in_production=True)
    QualificationEngine(conn).run()
    ScoringEngine(conn, weights, retuned).run([cid])

    assert storage.get_score(conn, cid)["gate_cap_applied"] in (33, None)


def test_gates_are_detected_from_evidence(conn, run_id, weights, caps):
    cid = seed(conn, run_id, "org/manifest-only", dependencies=[MANIFEST],
               code_usage=False, in_production=False,
               describes_product=True, app_code=True)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "medium")

    assert GATE_CODE_USAGE in result.gates_triggered
    assert GATE_OUTSIDE_PRODUCTION in result.gates_triggered
    assert GATE_SINGLE_CATEGORY in result.gates_triggered


def test_infrastructure_prevents_the_single_category_gate(conn, run_id, weights, caps):
    """category_count=1 alone is not enough; the gate needs no infrastructure
    service either."""
    cid = seed(conn, run_id, "org/infra", dependencies=[INFRA_DEP],
               code_usage=True, infra=True, stages=1,
               describes_product=True, app_code=True, in_production=True)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "high")

    assert GATE_SINGLE_CATEGORY not in result.gates_triggered
    assert result.gate_cap_applied is None


# --- unknown versus confirmed zero -----------------------------------------


def test_unknown_maintenance_burden_is_listed(conn, run_id, weights, caps):
    cid = seed(conn, run_id, dependencies=[CODE], code_usage=True, stages=1,
               describes_product=True, app_code=True, in_production=True)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "high")

    assert result.score_for("maintenance_burden") == 0
    assert "maintenance_burden" in result.unknown_dimensions


def test_a_confirmed_zero_is_not_listed_as_unknown(conn, run_id, weights, caps):
    """A candidate using a managed engine scores 0 on build-vs-buy because that
    is the answer, not because nobody looked."""
    cid = seed(conn, run_id, "org/gotenberg-user",
               dependencies=[{**INFRA_DEP, "library": "Gotenberg"}],
               code_usage=True, infra=True, stages=1,
               describes_product=True, app_code=True, in_production=True)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "high")

    assert result.score_for("build_vs_buy_signal") == 0
    assert "build_vs_buy_signal" not in result.unknown_dimensions
    assert "managed document engine" in \
        result.dimensions["build_vs_buy_signal"].rationale


def test_unknown_dimensions_keep_canonical_order(conn, run_id, weights, caps):
    cid = seed(conn, run_id, "org/thin", dependencies=[], code_usage=False)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "low")

    order = [d for d in SCORING_DIMENSIONS if d in result.unknown_dimensions]
    assert list(result.unknown_dimensions) == order


def test_unknown_dimensions_round_trip_through_storage(conn, run_id, weights, caps):
    cid = seed(conn, run_id, dependencies=[CODE], code_usage=True, stages=1,
               describes_product=True, app_code=True, in_production=True)
    QualificationEngine(conn).run()
    ScoringEngine(conn, weights, caps).run([cid])

    row = storage.get_score(conn, cid)
    assert "maintenance_burden" in storage.decode_unknown_dimensions(
        row["unknown_dimensions"])


def test_an_unknown_dimension_can_never_carry_a_nonzero_score():
    from dependency_map.scoring import DimensionResult

    with pytest.raises(ScoringError, match="always 0"):
        DimensionResult("document_volume", 3, True, "contradictory")


# --- confidence ------------------------------------------------------------


@pytest.mark.parametrize("evidenced,qual,expected", [
    (7, "high", BAND_HIGH),
    (6, "high", BAND_HIGH),
    (7, "medium", BAND_MEDIUM),   # the corrected fallback
    (6, "medium", BAND_MEDIUM),
    (5, "high", BAND_MEDIUM),
    (4, "high", BAND_MEDIUM),
    (3, "high", BAND_LOW),
    (0, "high", BAND_LOW),
    (7, "low", BAND_LOW),         # low qualification confidence dominates
    (5, "low", BAND_LOW),
])
def test_confidence_bands(evidenced, qual, expected):
    assert assess_confidence_band(evidenced, qual) == expected


def test_confidence_does_not_change_the_score(conn, run_id, weights, caps):
    cid = seed(conn, run_id, dependencies=[CODE], code_usage=True, stages=1,
               describes_product=True, app_code=True, in_production=True)
    evidence = evidence_for(conn, cid)

    high = score_candidate(evidence, weights, caps, "high")
    low = score_candidate(evidence, weights, caps, "low")

    assert high.confidence_band != low.confidence_band
    assert high.final_score == low.final_score
    assert high.raw_weighted_score == low.raw_weighted_score


# --- individual rubrics ----------------------------------------------------


def test_document_volume_is_unknown_without_language(conn, run_id, weights, caps):
    cid = seed(conn, run_id, dependencies=[MANIFEST])
    result = score_candidate(evidence_for(conn, cid), weights, caps, "low")

    assert result.score_for("document_volume") == 0
    assert "document_volume" in result.unknown_dimensions


def test_document_volume_ignores_stars(conn, run_id, weights, caps):
    low = seed(conn, run_id, "org/unpopular", dependencies=[MANIFEST], stars=0)
    high = seed(conn, run_id, "org/popular", dependencies=[MANIFEST], stars=50000)

    a = score_candidate(evidence_for(conn, low), weights, caps, "low")
    b = score_candidate(evidence_for(conn, high), weights, caps, "low")

    assert a.score_for("document_volume") == b.score_for("document_volume")


def test_document_complexity_does_not_reward_dependency_count(
    conn, run_id, weights, caps
):
    """Four libraries in one category is still one category."""
    cid = seed(conn, run_id, "org/many-same-category",
               dependencies=[MANIFEST, MANIFEST, MANIFEST, MANIFEST])
    result = score_candidate(evidence_for(conn, cid), weights, caps, "low")

    assert result.score_for("document_complexity") <= 1


def test_document_complexity_two_categories_manifest_only_scores_2(
    conn, run_id, weights, caps
):
    cid = seed(conn, run_id, "org/two-cats",
               dependencies=[MANIFEST, {**MANIFEST, "category": "pdf"}])
    result = score_candidate(evidence_for(conn, cid), weights, caps, "low")

    assert result.score_for("document_complexity") == 2


def test_document_complexity_two_confirmed_categories_scores_3(
    conn, run_id, weights, caps
):
    cid = seed(conn, run_id, "org/two-confirmed",
               dependencies=[CODE, {**CODE, "category": "pdf"}],
               multi_types=True, code_usage=True)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "low")

    assert result.score_for("document_complexity") == 3


def test_pipeline_complexity_is_unknown_when_usage_unconfirmed(
    conn, run_id, weights, caps
):
    """CANDIDATE_SCHEMA.md section 8: only the manifest was seen, so the code
    path was never inspected."""
    cid = seed(conn, run_id, dependencies=[MANIFEST], code_usage=False)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "low")

    assert result.score_for("pipeline_complexity") == 0
    assert "pipeline_complexity" in result.unknown_dimensions


def test_pipeline_complexity_one_confirmed_stage_scores_1(
    conn, run_id, weights, caps
):
    """A single conversion stage stays a single stage however important the
    repository is commercially."""
    cid = seed(conn, run_id, dependencies=[CODE], code_usage=True, stages=1)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "low")

    assert result.score_for("pipeline_complexity") == 1


def test_pipeline_complexity_tops_out_with_infrastructure(
    conn, run_id, weights, caps
):
    cid = seed(conn, run_id, "org/full-pipeline",
               dependencies=[CODE, INFRA_DEP], code_usage=True, infra=True,
               stages=3)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "high")

    assert result.score_for("pipeline_complexity") == 5


def test_maintenance_burden_is_always_unknown_in_the_mvp(
    conn, run_id, weights, caps
):
    cid = seed(conn, run_id, dependencies=[CODE], code_usage=True, stages=3)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "high")

    assert result.score_for("maintenance_burden") == 0
    assert "maintenance_burden" in result.unknown_dimensions
    assert "phase 14" in result.dimensions["maintenance_burden"].rationale


def test_no_commit_history_fetching_exists_in_scoring():
    source = Path("src/dependency_map/scoring.py").read_text(encoding="utf-8")

    for term in ["commits", "get_commits", "commit_history", "GitHubClient"]:
        assert term not in source


def test_build_vs_buy_custom_primitives_score_high(conn, run_id, weights, caps):
    cid = seed(conn, run_id, "org/custom",
               dependencies=[{**CODE, "library": "python-docx", "category": "docx"},
                             {**CODE, "library": "ReportLab", "category": "pdf"}],
               code_usage=True, stages=2)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "high")

    assert result.score_for("build_vs_buy_signal") == 4


def test_build_vs_buy_never_reaches_five_automatically(conn, run_id, weights, caps):
    """Rung 5 requires judging that the pipeline duplicates SuperDocs, which no
    stored field evidences."""
    cid = seed(conn, run_id, "org/very-custom",
               dependencies=[{**CODE, "library": "python-docx", "category": "docx"},
                             {**CODE, "library": "ReportLab", "category": "pdf"},
                             {**CODE, "library": "WeasyPrint",
                              "category": "template_generation"}],
               code_usage=True, stages=3)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "high")

    assert result.score_for("build_vs_buy_signal") < 5


def test_commercial_leverage_ignores_stars(conn, run_id, weights, caps):
    low = seed(conn, run_id, "org/quiet", dependencies=[MANIFEST], stars=1)
    high = seed(conn, run_id, "org/famous", dependencies=[MANIFEST], stars=90000)

    a = score_candidate(evidence_for(conn, low), weights, caps, "low")
    b = score_candidate(evidence_for(conn, high), weights, caps, "low")

    assert a.score_for("commercial_leverage") == b.score_for("commercial_leverage")


def test_commercial_leverage_is_unknown_without_signal(conn, run_id, weights, caps):
    cid = seed(conn, run_id, "org/opaque", dependencies=[MANIFEST])
    result = score_candidate(evidence_for(conn, cid), weights, caps, "low")

    assert result.score_for("commercial_leverage") == 0
    assert "commercial_leverage" in result.unknown_dimensions


def test_industry_alone_does_not_lift_business_criticality(
    conn, run_id, weights, caps
):
    """industry_category is keyword-derived and was wrong for three of five
    reviewed candidates, so it supports a rung but never carries one."""
    scores = set()
    for index, industry in enumerate(
        ["unknown", "legal_contracts", "healthcare_diagnostics", "real_estate"]
    ):
        cid = seed(conn, run_id, f"org/vertical-{index}", industry=industry,
                   dependencies=[CODE], code_usage=True, stages=1,
                   app_code=True, in_production=True, describes_product=True,
                   excerpt="A tool.")
        result = score_candidate(evidence_for(conn, cid), weights, caps, "high")
        scores.add(result.score_for("business_criticality"))

    assert scores == {2}, "no vertical lifts the rung without a document tie"


def test_all_dimension_scores_are_within_range(conn, run_id, weights, caps):
    cid = seed(conn, run_id, "org/range", dependencies=[CODE, INFRA_DEP],
               code_usage=True, infra=True, stages=3, templates=True,
               multi_types=True, describes_product=True, app_code=True,
               in_production=True)
    result = score_candidate(evidence_for(conn, cid), weights, caps, "high")

    for name, dimension in result.dimensions.items():
        assert 0 <= dimension.score <= 5, name
        assert dimension.rationale


# --- determinism -----------------------------------------------------------


def test_scoring_is_deterministic(conn, run_id, weights, caps):
    cid = seed(conn, run_id, "org/stable", dependencies=[CODE, INFRA_DEP],
               code_usage=True, infra=True, stages=3,
               describes_product=True, app_code=True, in_production=True)
    evidence = evidence_for(conn, cid)

    results = [score_candidate(evidence, weights, caps, "high") for _ in range(5)]
    signatures = {
        (r.raw_weighted_score, r.final_score, r.confidence_band,
         r.unknown_dimensions, r.gate_cap_applied,
         tuple(sorted((k, v.score) for k, v in r.dimensions.items())))
        for r in results
    }

    assert len(signatures) == 1


def test_rescoring_is_idempotent(conn, run_id, weights, caps):
    cid = seed(conn, run_id, "org/stable", dependencies=[CODE], code_usage=True,
               stages=1, describes_product=True, app_code=True, in_production=True)
    QualificationEngine(conn).run()
    engine = ScoringEngine(conn, weights, caps)

    engine.run([cid])
    first = dict(storage.get_score(conn, cid))
    engine.run([cid])
    second = dict(storage.get_score(conn, cid))

    assert first == second


# --- fixtures from the reviewed phase 8/9 candidates ------------------------
#
# Stored evidence only, replayed as fixtures. These verify reproducible
# behaviour, not a business ranking.


def bigcapital(conn, run_id):
    return seed(
        conn, run_id, "bigcapitalhq/bigcapital",
        dependencies=[
            {**INFRA_DEP, "library": "Gotenberg"},
            {**CODE, "library": "Gotenberg", "category": "conversion",
             "direction": "conversion"},
        ],
        code_usage=True, infra=True, stages=1, templates=False,
        multi_types=False, describes_product=True,
        excerpt="To get started with self-hosted with Docker and Docker Compose.",
        app_code=True, in_production=True, website=True, stars=3846,
        industry="finance_investment",
    )


def test_bigcapital_scores_reproducibly(conn, run_id, weights, caps):
    """Observation, not an instruction to retune anything."""
    cid = bigcapital(conn, run_id)
    QualificationEngine(conn).run()
    result = ScoringEngine(conn, weights, caps).score_one(cid)

    assert result is not None
    assert storage.get_qualification(conn, cid)["qualification_status"] == "keep"

    # Deployed conversion service, so the single-category gate cannot fire.
    assert GATE_SINGLE_CATEGORY not in result.gates_triggered
    assert result.gate_cap_applied is None

    # Chose a managed engine, so build-vs-buy is a confirmed zero, not unknown.
    assert result.score_for("build_vs_buy_signal") == 0
    assert "build_vs_buy_signal" not in result.unknown_dimensions

    # One observed stage stays one stage.
    assert result.score_for("pipeline_complexity") == 1
    assert "maintenance_burden" in result.unknown_dimensions

    row = storage.get_score(conn, cid)
    assert row["final_score"] == result.final_score
    assert row["confidence_band"] == result.confidence_band


def test_purpleops_investigates_and_scores(conn, run_id, weights, caps):
    cid = seed(
        conn, run_id, "CyberCX-STA/PurpleOps",
        dependencies=[MANIFEST, {**CODE, "category": "template_generation"}],
        code_usage=True, templates=True, stages=2, app_code=True,
        in_production=True, describes_product=False, website=True, stars=313,
        industry="legal_contracts",
    )
    QualificationEngine(conn).run()
    result = ScoringEngine(conn, weights, caps).score_one(cid)

    assert result is not None
    assert result.score_for("pipeline_complexity") == 2
    assert storage.get_score(conn, cid) is not None


def test_docbase_is_capped_for_manifest_only_evidence(conn, run_id, weights, caps):
    """Manifest-only evidence triggers the code-usage gate at 20."""
    cid = seed(
        conn, run_id, "alanagoyal/docbase", dependencies=[MANIFEST, MANIFEST],
        describes_product=True,
        excerpt="Docbase is an all-in-one Docsend alternative.",
        app_code=True, website=True, in_production=False, code_usage=False,
        stars=233,
    )
    QualificationEngine(conn).run()
    result = ScoringEngine(conn, weights, caps).score_one(cid)

    assert GATE_CODE_USAGE in result.gates_triggered
    assert result.score_for("pipeline_complexity") == 0
    assert "pipeline_complexity" in result.unknown_dimensions


@pytest.mark.parametrize("repo", ["thoqbk/traprange", "sambanova/ai-starter-kit"])
def test_the_rejected_candidates_receive_no_score_row(
    conn, run_id, weights, caps, repo
):
    if "traprange" in repo:
        cid = seed(conn, run_id, repo,
                   dependencies=[{**MANIFEST, "category": "pdf", "manifest": "pom.xml"},
                                 {**CODE, "category": "pdf"}],
                   code_usage=True, stages=1, app_code=True, in_production=True,
                   describes_product=False, stars=340)
    else:
        cid = seed(conn, run_id, repo,
                   dependencies=[MANIFEST, MANIFEST, MANIFEST, MANIFEST],
                   code_usage=False, app_code=False, in_production=False,
                   describes_product=False, stars=251)
    QualificationEngine(conn).run()
    ScoringEngine(conn, weights, caps).run([cid])

    assert storage.get_qualification(conn, cid)["qualification_status"] == REJECT
    assert storage.get_score(conn, cid) is None


# --- scope and safety ------------------------------------------------------


def test_scoring_makes_no_network_calls():
    source = Path("src/dependency_map/scoring.py").read_text(encoding="utf-8")

    for forbidden in ["import requests", "urllib", "http.client", "socket",
                      "GitHubClient", "LibrariesIOClient", "ReliableRequester",
                      "RequestsTransport", "search_code", "get_repository"]:
        assert forbidden not in source


def test_scoring_does_not_modify_evidence():
    source = Path("src/dependency_map/scoring.py").read_text(encoding="utf-8")

    for term in ["upsert_pipeline_evidence", "upsert_business_evidence",
                 "insert_dependency_found", "upsert_qualification",
                 "update_candidate_identity"]:
        assert term not in source


def test_report_module_now_exists():
    """report.py arrived at phase 11, immediately after scoring."""
    assert Path("src/dependency_map", "report.py").exists()
