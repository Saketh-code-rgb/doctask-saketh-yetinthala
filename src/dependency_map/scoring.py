"""Scoring engine: seven rubrics, weighted, capped, 0 to 100.

A pure function over stored evidence, like qualification. It opens no
connection to anything outside the database (TECHNICAL_DESIGN.md section 11),
so the rubrics can be revised and every candidate rescored without spending an
API call.

Scoring never rescues a candidate. It only ranks the ones qualification already
let through, and a reject gets no row here at all rather than a score of zero,
because a numeric zero beside a company name still invites comparison
(SCORING_MODEL.md section 1).

Three rules from that document shape everything below and are worth stating
before the code:

**Unknown scores 0, and stays visible.** A dimension nobody could evidence is
not a middle value and is not dropped from the average. Its weight is not
redistributed, so missing evidence can only hold a candidate back, never help
it. The dimension name goes into `unknown_dimensions` so the gap is legible in
the report rather than folded into a bare number.

**A confirmed zero is not an unknown.** A candidate that demonstrably uses a
managed document engine scores 0 on build-vs-buy because that is the *answer*,
not because nobody looked. Only the first kind is listed. Conflating them would
make the report claim ignorance it does not have.

**Caps are ceilings applied after the arithmetic**, never folded into it, so
the weighted sum stays auditable on its own.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from decimal import ROUND_HALF_UP, Decimal
from typing import Mapping, Sequence

from . import storage
from .db import SCORING_DIMENSIONS
from .qualification import HIGH, INVESTIGATE, KEEP, CandidateEvidence

logger = logging.getLogger(__name__)

BAND_HIGH = "high"
BAND_MEDIUM = "medium"
BAND_LOW = "low"

#: Statuses that reach scoring at all. SCORING_MODEL.md section 14's hard rule.
SCORABLE_STATUSES = frozenset({KEEP, INVESTIGATE})

#: Gate names, matching config/weights.yaml.
GATE_CODE_USAGE = "code_usage_unconfirmed"
GATE_OUTSIDE_PRODUCTION = "document_code_outside_production"
GATE_SINGLE_CATEGORY = "single_category_no_infrastructure"

#: Managed document engines, named in SCORING_MODEL.md section 8 rung 0 as
#: tools that "already solve the document problem". Choosing one is the
#: opposite of a build-vs-buy opportunity, which is why a candidate can be
#: commercially valuable and still score 0 here.
MANAGED_DOCUMENT_TOOLS = frozenset(
    {"Carbone.io", "Gotenberg", "Aspose.Words", "Aspose / Spire.Office suites",
     "LibreOffice headless / unoconv / JODConverter"}
)

#: Language that evidences recurring or batched generation. Deliberately narrow:
#: the collector stores only a short README excerpt and its notes, so most
#: candidates will legitimately have no volume evidence at all.
VOLUME_FREQUENCY_PHRASES = (
    "every day", "daily", "weekly", "monthly", "nightly", "per day",
    "per month", "per week", "each month", "recurring", "on a schedule",
    "scheduled", "continuously", "ongoing",
)
VOLUME_SCALE_PHRASES = (
    "thousands of", "hundreds of", "millions of", "at scale", "high volume",
    "bulk", "in bulk", "batch", "batches",
)
MULTI_TENANT_PHRASES = (
    "multi-tenant", "multitenant", "tenants", "per tenant", "saas",
    "platform for", "for teams", "for businesses", "for companies",
    "our customers", "your customers", "customers", "clients",
    "organizations", "organisations",
)

#: Verticals graded by SCORING_MODEL.md section 5.
CRITICAL_VERTICALS = frozenset(
    {"legal_contracts", "healthcare_diagnostics", "finance_investment"}
)
HIGH_VERTICALS = frozenset(
    {"real_estate", "proposal_sales", "software_technical_docs"}
)
MODERATE_VERTICALS = frozenset({"education", "events_weddings"})

#: Language tying a document to an obligation or a delivered artefact, which
#: rungs 4 and 5 of section 5 require on top of the vertical.
CRITICALITY_PHRASES = (
    "contract", "compliance", "regulatory", "audit", "invoice", "patient",
    "diagnosis", "policy", "claim", "agreement", "statement", "certificate",
    "deliver", "delivered to", "sent to", "customer-facing", "client-facing",
)

CONFIRMED_METHODS = frozenset({"code_import", "infrastructure_reference"})


class ScoringError(Exception):
    """A candidate could not be scored."""


# --- results ---------------------------------------------------------------


@dataclass(frozen=True)
class DimensionResult:
    """One rubric's verdict, and whether it rests on evidence at all."""

    name: str
    score: int
    unknown: bool
    rationale: str

    def __post_init__(self) -> None:
        if not 0 <= self.score <= 5:
            raise ScoringError(f"{self.name} produced {self.score}, outside 0-5")
        if self.unknown and self.score != 0:
            raise ScoringError(
                f"{self.name} is unknown but scored {self.score}; an unknown "
                f"dimension is always 0"
            )


@dataclass(frozen=True)
class ScoreResult:
    candidate_id: str
    dimensions: Mapping[str, DimensionResult]
    raw_weighted_score: float
    uncapped_final_score: int
    final_score: int
    confidence_band: str
    unknown_dimensions: tuple[str, ...]
    gate_cap_applied: int | None
    gates_triggered: tuple[str, ...] = ()

    @property
    def evidenced_count(self) -> int:
        return sum(1 for d in self.dimensions.values() if not d.unknown)

    def score_for(self, dimension: str) -> int:
        return self.dimensions[dimension].score


# --- text helpers ----------------------------------------------------------


def _text_of(evidence: CandidateEvidence) -> str:
    """The stored prose a rubric may read.

    Only what the collector actually persisted: a short README excerpt and the
    two notes fields. The full README is deliberately not stored, so most
    candidates will have little here, and the rubrics are written to return
    unknown rather than to guess.
    """
    parts = [
        evidence.readme_excerpt or "",
        evidence.business_evidence_notes or "",
        evidence.pipeline_evidence_notes or "",
        evidence.product_name or "",
    ]
    return re.sub(r"\s+", " ", " ".join(parts)).lower()


def _mentions(haystack: str, phrases: Sequence[str]) -> str | None:
    for phrase in phrases:
        if re.search(rf"\b{re.escape(phrase)}s?\b", haystack):
            return phrase
    return None


def _has_explicit_number(haystack: str) -> bool:
    """A figure attached to documents, not just any digit."""
    return bool(
        re.search(
            r"\b\d[\d,]{2,}\+?\b|\b\d+\s*(?:k|m|million|thousand)\b", haystack
        )
    )


# --- dimension rubrics -----------------------------------------------------
#
# One function per dimension, each implementing SCORING_MODEL.md sections 3
# through 9 as written. Each returns a DimensionResult carrying the rung,
# whether it was evidenced at all, and why.


def score_document_volume(evidence: CandidateEvidence) -> DimensionResult:
    """SCORING_MODEL.md section 3.

    Volume language is not a stored field, so this reads the excerpt and notes
    the collector kept. In practice most candidates land on rung 0 as genuinely
    unknown, which the document anticipates: nothing here infers volume from
    stars, contributors or company size.
    """
    text = _text_of(evidence)
    scale = _mentions(text, VOLUME_SCALE_PHRASES)
    frequency = _mentions(text, VOLUME_FREQUENCY_PHRASES)
    tenancy = _mentions(text, MULTI_TENANT_PHRASES)
    explicit = _has_explicit_number(text) and (scale or frequency)

    if explicit and tenancy:
        return DimensionResult(
            "document_volume", 5, False,
            f"explicit volume language ({scale or frequency}) with a figure, "
            f"alongside multi-tenant framing ({tenancy})")
    if explicit or (tenancy and (scale or frequency)):
        return DimensionResult(
            "document_volume", 4, False,
            f"explicit volume or frequency language ({scale or frequency})")
    if frequency or tenancy:
        return DimensionResult(
            "document_volume", 3, False,
            f"recurring or multi-tenant framing ({frequency or tenancy}) "
            f"without a stated figure")
    if scale:
        return DimensionResult(
            "document_volume", 2, False,
            f"batch language ({scale}) with no numbers or scale claim")
    if evidence.produces_documents:
        return DimensionResult(
            "document_volume", 1, False,
            "confirmed generation with no batch construct or volume language "
            "in the stored evidence")
    return DimensionResult(
        "document_volume", 0, True,
        "no volume language and no batch behaviour in the stored evidence")


def score_document_complexity(evidence: CandidateEvidence) -> DimensionResult:
    """SCORING_MODEL.md section 4.

    Category count alone only reaches rung 2. Climbing higher requires
    confirmed code usage across the categories, which is what stops a
    requirements file full of document libraries from scoring as a pipeline.
    """
    if not evidence.dependencies:
        return DimensionResult(
            "document_complexity", 0, True,
            "no dependency evidence located, so complexity is unassessable")

    categories = {d["library_category"] for d in evidence.dependencies}
    confirmed_categories = {
        d["library_category"] for d in evidence.dependencies
        if d["detection_method"] in CONFIRMED_METHODS
    }
    count = len(categories)
    structure = bool(evidence.template_directory_present)

    if count >= 3 and len(confirmed_categories) >= 3:
        return DimensionResult(
            "document_complexity", 5, False,
            f"category_count={count} with confirmed code usage across "
            f"{len(confirmed_categories)} of them")
    if count >= 3:
        return DimensionResult(
            "document_complexity", 4, False,
            f"category_count={count}, not all confirmed in code")
    if count == 2 and evidence.multiple_document_types_handled \
            and len(confirmed_categories) >= 2:
        return DimensionResult(
            "document_complexity", 3, False,
            "category_count=2, multiple_document_types_handled=true, both "
            "confirmed via code usage")
    if count == 2:
        return DimensionResult(
            "document_complexity", 2, False,
            f"category_count=2 but only {len(confirmed_categories)} confirmed "
            f"in code, so the actual complexity is unconfirmed")
    if structure:
        return DimensionResult(
            "document_complexity", 1, False,
            "category_count=1 with a template directory evidencing structure")
    return DimensionResult(
        "document_complexity", 0, False,
        f"category_count={count}, multiple_document_types_handled="
        f"{str(evidence.multiple_document_types_handled).lower()}, no "
        f"structural evidence")


def score_business_criticality(evidence: CandidateEvidence) -> DimensionResult:
    """SCORING_MODEL.md section 5.

    Rungs 3 through 5 need a vertical *and* language tying the document to an
    obligation or a delivered artefact. The vertical alone never carries a
    rung: `industry_category` is keyword-derived and was wrong or dubious for
    three of five candidates in the phase 8 review, so it can support a score
    but must not decide one.
    """
    if not evidence.has_business_evidence:
        return DimensionResult(
            "business_criticality", 0, True,
            "no business evidence collected")

    if not evidence.document_functionality_in_production_code:
        return DimensionResult(
            "business_criticality", 0, False,
            "document_functionality_in_production_code=false")

    text = _text_of(evidence)
    tie = _mentions(text, CRITICALITY_PHRASES)
    vertical = evidence.industry_category
    real_product = (
        evidence.application_code_exists and evidence.readme_describes_product
    )

    if vertical in CRITICAL_VERTICALS and tie:
        return DimensionResult(
            "business_criticality", 5, False,
            f"industry_category={vertical} with language tying the document to "
            f"an obligation or deliverable ({tie})")
    if vertical in HIGH_VERTICALS and tie:
        return DimensionResult(
            "business_criticality", 4, False,
            f"industry_category={vertical} with delivery language ({tie})")
    if vertical in MODERATE_VERTICALS and evidence.readme_describes_product:
        return DimensionResult(
            "business_criticality", 3, False,
            f"industry_category={vertical} with customer-facing framing")
    if real_product:
        return DimensionResult(
            "business_criticality", 2, False,
            f"real product (application_code_exists=true, "
            f"readme_describes_product=true) but industry_category={vertical} "
            f"does not map cleanly onto a high-criticality vertical, or the "
            f"document-to-obligation link is not evidenced")
    if evidence.readme_describes_product or evidence.application_code_exists:
        return DimensionResult(
            "business_criticality", 1, False,
            "internal or customer-adjacent: only part of the real-product "
            "evidence holds")
    return DimensionResult(
        "business_criticality", 0, False,
        "no product framing and no application code")


def score_pipeline_complexity(evidence: CandidateEvidence) -> DimensionResult:
    """SCORING_MODEL.md section 6.

    Unconfirmed code usage is treated as unknown rather than as a confirmed
    zero, following CANDIDATE_SCHEMA.md section 8: when only the manifest was
    seen, the actual code path was never inspected, so nobody knows how complex
    the pipeline is.
    """
    if not evidence.has_pipeline_evidence:
        return DimensionResult(
            "pipeline_complexity", 0, True, "no pipeline evidence collected")

    if not evidence.code_usage_confirmed:
        return DimensionResult(
            "pipeline_complexity", 0, True,
            f"code_usage_confirmed=false with "
            f"pipeline_stage_count={evidence.pipeline_stage_count}; only "
            f"manifest evidence exists, so the code path was never inspected")

    stages = evidence.pipeline_stage_count
    methods = {
        d["detection_method"] for d in evidence.dependencies
        if d["detection_method"] in CONFIRMED_METHODS
    }

    if stages >= 3 and evidence.infrastructure_service_present:
        return DimensionResult(
            "pipeline_complexity", 5, False,
            f"pipeline_stage_count={stages} with a deployed conversion service")
    if stages >= 3 and len(methods) > 1:
        return DimensionResult(
            "pipeline_complexity", 4, False,
            f"pipeline_stage_count={stages} across {len(methods)} detection "
            f"methods")
    if stages >= 3:
        return DimensionResult(
            "pipeline_complexity", 3, False,
            f"pipeline_stage_count={stages}, all through a single detection "
            f"method")
    if stages == 2:
        return DimensionResult(
            "pipeline_complexity", 2, False,
            "pipeline_stage_count=2, both confirmed")
    if stages == 1:
        return DimensionResult(
            "pipeline_complexity", 1, False,
            "pipeline_stage_count=1 with code_usage_confirmed=true, a single "
            "confirmed step with nothing chained after it")
    return DimensionResult(
        "pipeline_complexity", 0, False,
        "pipeline_stage_count=0 despite confirmed code usage")


def score_maintenance_burden(evidence: CandidateEvidence) -> DimensionResult:
    """SCORING_MODEL.md section 7, unchanged.

    The rubric grades how much custom code a team wrote around the document
    libraries. Phase 14 added the targeted source-inspection pass that makes it
    computable; where that pass has not run, the dimension stays unknown and
    scores 0 rather than being guessed at.

    The mapping itself lives in maintenance.rung_for, next to the collector
    that produces its inputs. Nothing here reads commit activity directly: the
    rubric mentions history only at rung 4, as corroboration, and treating a
    busy repository as a complex one would measure the wrong thing.
    """
    from .maintenance import MaintenanceSignals, rung_for

    row = getattr(evidence, "maintenance", None)
    if row is None:
        return DimensionResult(
            "maintenance_burden", 0, True,
            "source inspection not run; deferred to the phase 14 targeted pass")

    signals = MaintenanceSignals(
        candidate_id=evidence.candidate_id,
        document_library_count=row["document_library_count"],
        same_file_library_count=row["same_file_library_count"],
        custom_logic_present=bool(row["custom_logic_present"]),
        custom_formatting_present=bool(row["custom_formatting_present"]),
        custom_validation_present=bool(row["custom_validation_present"]),
        custom_error_handling_present=bool(row["custom_error_handling_present"]),
        repeated_modification_evidence=(
            None if row["repeated_modification_evidence"] is None
            else bool(row["repeated_modification_evidence"])
        ),
        files_inspected=row["files_inspected"],
    )
    rung, reason = rung_for(signals)
    if rung == 0:
        return DimensionResult("maintenance_burden", 0, True, reason)
    return DimensionResult("maintenance_burden", rung, False, reason)


def score_build_vs_buy_signal(evidence: CandidateEvidence) -> DimensionResult:
    """SCORING_MODEL.md section 8.

    Note the direction, which reads backwards at first: adopting a managed
    engine scores *low*. Rung 0 names Gotenberg, Carbone and Aspose explicitly.
    The dimension asks how much of what SuperDocs sells this team is currently
    building for itself, so a team that already bought the solution has little
    left to buy. A candidate can be commercially valuable and score 0 here.
    """
    if not evidence.dependencies:
        return DimensionResult(
            "build_vs_buy_signal", 0, True,
            "no dependency evidence located, so build-versus-buy is "
            "unassessable")

    names = {d["library_name"] for d in evidence.dependencies}
    managed = names & MANAGED_DOCUMENT_TOOLS
    primitives = names - MANAGED_DOCUMENT_TOOLS
    confirmed_primitive_categories = {
        d["library_category"] for d in evidence.dependencies
        if d["library_name"] not in MANAGED_DOCUMENT_TOOLS
        and d["detection_method"] in CONFIRMED_METHODS
    }

    if managed and not primitives:
        return DimensionResult(
            "build_vs_buy_signal", 0, False,
            f"already using a managed document engine ({', '.join(sorted(managed))}), "
            f"which is the tool that solves this problem")
    if managed and primitives:
        if len(confirmed_primitive_categories) >= 2:
            return DimensionResult(
                "build_vs_buy_signal", 2, False,
                f"a genuine mix: managed ({', '.join(sorted(managed))}) "
                f"alongside custom work on {len(confirmed_primitive_categories)} "
                f"library categories")
        return DimensionResult(
            "build_vs_buy_signal", 1, False,
            f"mostly managed ({', '.join(sorted(managed))}) with a small amount "
            f"of custom glue")
    if len(confirmed_primitive_categories) >= 2:
        return DimensionResult(
            "build_vs_buy_signal", 4, False,
            f"fully custom: {len(confirmed_primitive_categories)} library "
            f"categories confirmed in code, no managed document tool present")
    if confirmed_primitive_categories:
        return DimensionResult(
            "build_vs_buy_signal", 3, False,
            "mostly custom, built directly on a lower-level library rather than "
            "a managed document engine")
    return DimensionResult(
        "build_vs_buy_signal", 1, False,
        "lower-level libraries declared but none confirmed in code, so little "
        "custom work is evidenced")


def score_commercial_leverage(evidence: CandidateEvidence) -> DimensionResult:
    """SCORING_MODEL.md section 9.

    Nothing here reads star count. A popular repository is not thereby a
    platform, and the phase brief rules the inference out explicitly.
    """
    if not evidence.has_business_evidence:
        return DimensionResult(
            "commercial_leverage", 0, True, "no business evidence collected")

    text = _text_of(evidence)
    tenancy = _mentions(text, MULTI_TENANT_PHRASES)
    scale = _has_explicit_number(text) or _mentions(text, VOLUME_SCALE_PHRASES)

    if tenancy and scale:
        return DimensionResult(
            "commercial_leverage", 4, False,
            f"platform framing ({tenancy}) with an indication of scale")
    if tenancy:
        return DimensionResult(
            "commercial_leverage", 3, False,
            f"some multi-tenant signal ({tenancy}), scale unclear")
    if evidence.company_name or (
        evidence.website_exists and evidence.readme_describes_product
    ):
        return DimensionResult(
            "commercial_leverage", 2, False,
            "a single identifiable organisation with a real product, no "
            "multi-tenant signal")
    return DimensionResult(
        "commercial_leverage", 0, True,
        "nothing visible distinguishes a platform from one company's own "
        "tooling")


#: Evaluated in the canonical order from SCORING_MODEL.md.
RUBRICS = {
    "document_volume": score_document_volume,
    "document_complexity": score_document_complexity,
    "business_criticality": score_business_criticality,
    "pipeline_complexity": score_pipeline_complexity,
    "maintenance_burden": score_maintenance_burden,
    "build_vs_buy_signal": score_build_vs_buy_signal,
    "commercial_leverage": score_commercial_leverage,
}


# --- arithmetic ------------------------------------------------------------


def compute_raw_weighted_score(
    scores: Mapping[str, int], weights: Mapping[str, float]
) -> Decimal:
    """sum(score_i * weight_i), in exact decimal arithmetic.

    Decimal rather than float so 4.60 is 4.60 and the fixture math in
    SCORING_MODEL.md section 15 reproduces exactly rather than to within a
    rounding error.
    """
    total = Decimal(0)
    for dimension in SCORING_DIMENSIONS:
        total += Decimal(scores[dimension]) * Decimal(str(weights[dimension]))
    return total


def compute_final_score(raw: Decimal) -> int:
    """round((raw / 5) * 100).

    Half-up rounding, because Python's built-in round() uses banker's rounding
    and would turn a .5 into the nearest even number. The document says round,
    and a reader checking the arithmetic by hand will round half up.
    """
    return int((raw / 5 * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def applicable_gates(evidence: CandidateEvidence) -> tuple[str, ...]:
    """Which of SCORING_MODEL.md section 14's three conditions hold."""
    gates = []
    if not evidence.code_usage_confirmed:
        gates.append(GATE_CODE_USAGE)
    if not evidence.document_functionality_in_production_code:
        gates.append(GATE_OUTSIDE_PRODUCTION)
    if evidence.category_count == 1 and not evidence.infrastructure_service_present:
        gates.append(GATE_SINGLE_CATEGORY)
    return tuple(gates)


def apply_gate_caps(
    final_score: int, gates: Sequence[str], caps: Mapping[str, int]
) -> tuple[int, int | None]:
    """Cap the score, returning (capped_score, cap_applied).

    When several gates hold, the smallest cap wins. The cap is only *applied*
    when it is actually below the score: a candidate scoring 12 with a cap of
    20 is not being capped, and recording one would misdescribe the record.
    """
    if not gates:
        return final_score, None
    smallest = min(caps[gate] for gate in gates if gate in caps)
    if final_score <= smallest:
        return final_score, None
    return smallest, smallest


def assess_confidence_band(
    evidenced: int, qualification_confidence: str | None
) -> str:
    """SCORING_MODEL.md section 13, including the corrected medium fallback.

    A well-evidenced candidate whose qualification was itself a close call does
    not inherit high confidence from its dimension count alone.
    """
    if qualification_confidence == BAND_LOW:
        return BAND_LOW
    if evidenced >= 6:
        return BAND_HIGH if qualification_confidence == HIGH else BAND_MEDIUM
    if evidenced >= 4:
        return BAND_MEDIUM
    return BAND_LOW


# --- the engine ------------------------------------------------------------


def score_candidate(
    evidence: CandidateEvidence,
    weights: Mapping[str, float],
    caps: Mapping[str, int],
    qualification_confidence: str | None = None,
) -> ScoreResult:
    """Score one candidate. Pure, deterministic, offline."""
    missing = sorted(set(SCORING_DIMENSIONS) - set(weights))
    if missing:
        raise ScoringError(f"weights are missing dimensions: {missing}")
    extra = sorted(set(weights) - set(SCORING_DIMENSIONS))
    if extra:
        raise ScoringError(f"weights contain unknown dimensions: {extra}")

    dimensions = {name: RUBRICS[name](evidence) for name in SCORING_DIMENSIONS}
    scores = {name: result.score for name, result in dimensions.items()}

    raw = compute_raw_weighted_score(scores, weights)
    uncapped = compute_final_score(raw)

    gates = applicable_gates(evidence)
    final, cap_applied = apply_gate_caps(uncapped, gates, caps)

    # Canonical order, so two candidates with the same gaps serialize alike.
    unknown = tuple(
        name for name in SCORING_DIMENSIONS if dimensions[name].unknown
    )
    evidenced = len(SCORING_DIMENSIONS) - len(unknown)

    return ScoreResult(
        candidate_id=evidence.candidate_id,
        dimensions=dimensions,
        raw_weighted_score=float(raw),
        uncapped_final_score=uncapped,
        final_score=final,
        confidence_band=assess_confidence_band(evidenced, qualification_confidence),
        unknown_dimensions=unknown,
        gate_cap_applied=cap_applied,
        gates_triggered=gates,
    )


@dataclass
class ScoringReport:
    """Counts only. The ranked table is the report generator's job."""

    scored: int = 0
    skipped_rejected: int = 0
    capped: int = 0
    confidence: dict = field(default_factory=dict)
    unknown_totals: dict = field(default_factory=dict)

    def record(self, result: ScoreResult) -> None:
        self.scored += 1
        if result.gate_cap_applied is not None:
            self.capped += 1
        self.confidence[result.confidence_band] = (
            self.confidence.get(result.confidence_band, 0) + 1
        )
        for name in result.unknown_dimensions:
            self.unknown_totals[name] = self.unknown_totals.get(name, 0) + 1

    def summary_lines(self) -> list[str]:
        lines = [
            f"candidates scored     {self.scored}",
            f"rejected, not scored  {self.skipped_rejected}",
            f"gate-capped           {self.capped}",
        ]
        for band in (BAND_HIGH, BAND_MEDIUM, BAND_LOW):
            lines.append(f"  confidence {band:<8}{self.confidence.get(band, 0)}")
        for name, count in sorted(self.unknown_totals.items()):
            lines.append(f"  unknown {name:<22}{count}")
        return lines


class ScoringEngine:
    """Scores qualified candidates and persists the results. No network access."""

    def __init__(self, connection, weights: Mapping[str, float],
                 caps: Mapping[str, int]) -> None:
        self._conn = connection
        self._weights = weights
        self._caps = caps

    def pending(self) -> list[str]:
        """Keep and investigate candidates with no score row yet.

        A reject is never returned here, so it cannot acquire a row by being
        rescored later.
        """
        return storage.candidates_needing_scoring(self._conn)

    def score_one(self, candidate_id: str) -> ScoreResult | None:
        qualification = storage.get_qualification(self._conn, candidate_id)
        if qualification is None:
            raise ScoringError(f"{candidate_id} has no qualification decision")
        if qualification["qualification_status"] not in SCORABLE_STATUSES:
            # Not an error, and deliberately not a zero. A rejected candidate
            # simply does not enter the ranked table.
            return None

        evidence = CandidateEvidence.load(self._conn, candidate_id)
        result = score_candidate(
            evidence, self._weights, self._caps, qualification["confidence"]
        )
        storage.upsert_score(
            self._conn,
            candidate_id=result.candidate_id,
            document_volume=result.score_for("document_volume"),
            document_complexity=result.score_for("document_complexity"),
            business_criticality=result.score_for("business_criticality"),
            pipeline_complexity=result.score_for("pipeline_complexity"),
            maintenance_burden=result.score_for("maintenance_burden"),
            build_vs_buy_signal=result.score_for("build_vs_buy_signal"),
            commercial_leverage=result.score_for("commercial_leverage"),
            raw_weighted_score=result.raw_weighted_score,
            final_score=result.final_score,
            confidence_band=result.confidence_band,
            unknown_dimensions=result.unknown_dimensions,
            gate_cap_applied=result.gate_cap_applied,
        )
        return result

    def run(self, candidate_ids: Sequence[str] | None = None) -> ScoringReport:
        report = ScoringReport()
        for candidate_id in (
            candidate_ids if candidate_ids is not None else self.pending()
        ):
            result = self.score_one(candidate_id)
            if result is None:
                report.skipped_rejected += 1
            else:
                report.record(result)
        return report
