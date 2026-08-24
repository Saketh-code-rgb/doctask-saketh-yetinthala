"""Qualification engine: keep, investigate, or reject, from stored evidence.

A pure function over what the evidence collector already wrote. It opens no
connection to anything outside the database, which is what lets the rules be
revised and rerun over the whole corpus without spending a single API call
(TECHNICAL_DESIGN.md section 10).

Two principles shape every rule here.

**Qualification is not ranking.** It decides whether a candidate belongs in the
pool at all. How promising a candidate is, once it is in the pool, is the
scoring engine's question and is deliberately not asked here.

**Absence of evidence is never confirmed absence.** The collector records what
it saw; where it saw nothing, the field stays false or null. A false that means
"we looked and it was not there" and a false that means "we never got to look"
are indistinguishable once stored, so no rule may reject on a bare negative.
Every rejection has to rest on a *combination* of observations that positively
supports it. Where the evidence is thin, the answer is investigate, and a large
investigate pile is the expected outcome rather than a failure
(TECHNICAL_DESIGN.md section 17).

That conservatism is deliberate asymmetry. A wrong reject removes a company
from consideration silently and permanently; a wrong investigate costs someone
a few minutes of reading. Those errors are not equally bad, so the rules are
not calibrated as if they were.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Callable, Sequence

from . import storage

KEEP = "keep"
INVESTIGATE = "investigate"
REJECT = "reject"

HIGH = "high"
MEDIUM = "medium"
LOW = "low"

#: The rejection reasons from CANDIDATE_SCHEMA.md section 7.
SINGLE_INCIDENTAL_USE = "single_incidental_use"
TUTORIAL_OR_DEMO = "tutorial_or_demo"
FORK_OF_LIBRARY = "fork_of_library"
ARCHIVED_NO_SIGNAL = "archived_no_signal"
PERSONAL_PROJECT_NO_CUSTOMERS = "personal_project_no_customers"
OTHER = "other"

#: Repository-name tokens that positively indicate a teaching or demonstration
#: artefact. Used only alongside other evidence, never on their own: plenty of
#: real products have "demo" somewhere in their history.
TUTORIAL_NAME_TOKENS = (
    "tutorial", "tutorials", "example", "examples", "sample", "samples",
    "demo", "demos", "workshop", "course", "lesson", "exercise", "exercises",
    "bootcamp", "training", "kata", "howto", "getting-started", "starter-kit",
    "learn", "learning", "study", "practice", "assignment", "homework",
)

#: Tokens that positively indicate a personal scratch space.
PERSONAL_NAME_TOKENS = (
    "playground", "sandbox", "scratch", "hobby", "toy", "dotfiles",
    "my-", "-mine", "personal", "experiments", "experiment", "tinkering",
    "test-repo", "testing-",
)

#: Directions that mean the repository produces or transforms documents, as
#: opposed to only reading them (LIBRARY_UNIVERSE.md's closing note).
PRODUCING_DIRECTIONS = frozenset({"generation", "conversion", "mixed"})

CONFIRMED_METHODS = frozenset({"code_import", "infrastructure_reference"})


# --- the evidence a decision is made from ----------------------------------


@dataclass(frozen=True)
class CandidateEvidence:
    """Everything qualification reads, assembled once.

    The computed counts from CANDIDATE_SCHEMA.md section 4 are derived here
    rather than stored, so they cannot drift from the dependency rows they
    summarise.
    """

    candidate_id: str
    repo_name: str = ""
    repo_owner: str = ""
    is_fork: bool = False
    is_archived: bool = False
    company_name: str | None = None
    product_name: str | None = None
    website_url: str | None = None
    industry_category: str = "unknown"

    dependencies: tuple = ()
    category_count: int = 0
    generation_signal_count: int = 0
    extraction_signal_count: int = 0
    conversion_signal_count: int = 0
    confirmed_dependency_count: int = 0
    manifest_only: bool = True

    has_pipeline_evidence: bool = False
    code_usage_confirmed: bool = False
    template_directory_present: bool = False
    multiple_document_types_handled: bool = False
    pipeline_stage_count: int = 0
    infrastructure_service_present: bool = False
    pipeline_evidence_notes: str = ""

    has_business_evidence: bool = False
    readme_describes_product: bool = False
    readme_excerpt: str | None = None
    website_exists: bool = False
    application_code_exists: bool = False
    document_functionality_in_production_code: bool = False
    stars: int | None = None
    last_commit_date: str | None = None
    contributor_count: int | None = None
    business_evidence_notes: str = ""

    # Schema 3, phase 14. Read by scoring only; no qualification rule branches
    # on these, and a null stays null rather than becoming a negative finding.
    infrastructure_reference_present: bool | None = None
    is_catalogue_repository: bool | None = None
    readme_indicates_example_or_tutorial: bool | None = None
    has_examples_directory: bool | None = None
    maintenance: object | None = None

    @property
    def full_name(self) -> str:
        return f"{self.repo_owner}/{self.repo_name}".strip("/")

    @property
    def produces_documents(self) -> bool:
        """At least one confirmed dependency that generates or converts."""
        return any(
            d["direction"] in PRODUCING_DIRECTIONS
            and d["detection_method"] in CONFIRMED_METHODS
            for d in self.dependencies
        )

    @classmethod
    def load(cls, conn, candidate_id: str) -> "CandidateEvidence":
        candidate = storage.get_candidate(conn, candidate_id)
        if candidate is None:
            raise ValueError(f"No candidate {candidate_id!r}")

        dependencies = [
            dict(row)
            for row in storage.list_dependencies_for_candidate(conn, candidate_id)
        ]
        pipeline = storage.get_pipeline_evidence(conn, candidate_id)
        business = storage.get_business_evidence(conn, candidate_id)
        maintenance = storage.get_maintenance_evidence(conn, candidate_id)

        confirmed = [
            d for d in dependencies if d["detection_method"] in CONFIRMED_METHODS
        ]

        return cls(
            candidate_id=candidate_id,
            repo_name=candidate["repo_name"] or "",
            repo_owner=candidate["repo_owner"] or "",
            is_fork=bool(candidate["is_fork"]),
            is_archived=bool(candidate["is_archived"]),
            company_name=candidate["company_name"],
            product_name=candidate["product_name"],
            website_url=candidate["website_url"],
            industry_category=candidate["industry_category"] or "unknown",
            dependencies=tuple(dependencies),
            category_count=len({d["library_category"] for d in dependencies}),
            generation_signal_count=sum(
                1 for d in dependencies if d["direction"] == "generation"
            ),
            extraction_signal_count=sum(
                1 for d in dependencies if d["direction"] == "extraction"
            ),
            conversion_signal_count=sum(
                1 for d in dependencies
                if d["direction"] in ("conversion", "mixed")
            ),
            confirmed_dependency_count=len(confirmed),
            manifest_only=bool(dependencies) and not confirmed,
            has_pipeline_evidence=pipeline is not None,
            code_usage_confirmed=bool(pipeline["code_usage_confirmed"]) if pipeline else False,
            template_directory_present=bool(pipeline["template_directory_present"]) if pipeline else False,
            multiple_document_types_handled=bool(pipeline["multiple_document_types_handled"]) if pipeline else False,
            pipeline_stage_count=int(pipeline["pipeline_stage_count"]) if pipeline else 0,
            infrastructure_service_present=bool(pipeline["infrastructure_service_present"]) if pipeline else False,
            pipeline_evidence_notes=(pipeline["pipeline_evidence_notes"] or "") if pipeline else "",
            has_business_evidence=business is not None,
            readme_describes_product=bool(business["readme_describes_product"]) if business else False,
            readme_excerpt=business["readme_excerpt"] if business else None,
            website_exists=bool(business["website_exists"]) if business else False,
            application_code_exists=bool(business["application_code_exists"]) if business else False,
            document_functionality_in_production_code=bool(
                business["document_functionality_in_production_code"]) if business else False,
            stars=business["stars"] if business else None,
            last_commit_date=business["last_commit_date"] if business else None,
            contributor_count=business["contributor_count"] if business else None,
            business_evidence_notes=(business["business_evidence_notes"] or "") if business else "",
            infrastructure_reference_present=_opt_bool(
                pipeline, "infrastructure_reference_present"),
            is_catalogue_repository=_opt_bool(business, "is_catalogue_repository"),
            readme_indicates_example_or_tutorial=_opt_bool(
                business, "readme_indicates_example_or_tutorial"),
            has_examples_directory=_opt_bool(business, "has_examples_directory"),
            maintenance=maintenance,
        )


@dataclass(frozen=True)
class Decision:
    """One qualification outcome, ready to persist."""

    candidate_id: str
    status: str
    reason: str
    confidence: str
    rejection_reason: str | None = None
    supporting_signals: tuple[str, ...] = ()
    unknowns: tuple[str, ...] = ()


def _opt_bool(row, column: str) -> bool | None:
    """Read a nullable schema-3 flag without turning null into False.

    A null means the signal was never assessed. Collapsing that to False would
    manufacture a negative finding, which is the one thing the evidence rules
    forbid.
    """
    if row is None:
        return None
    try:
        value = row[column]
    except (IndexError, KeyError):
        return None
    return None if value is None else bool(value)


# --- helpers ---------------------------------------------------------------


def _name_matches(evidence: CandidateEvidence, tokens: Sequence[str]) -> str | None:
    """A repository-name token match, or None.

    Word-boundary matched where the token is a word, so "example" does not fire
    on "exampleforge" and "demo" does not fire on "democracy". The lesson from
    the phase 8 live run, where a substring match read "clause" inside
    ClauseForge, applies here just as much.
    """
    haystack = evidence.repo_name.lower().replace("_", "-")
    for token in tokens:
        pattern = re.escape(token)
        if token.endswith("-") or token.startswith("-"):
            if token in haystack:
                return token
        elif re.search(rf"(?:^|[-.]){pattern}(?:$|[-.])", haystack):
            return token
    return None


def _cite(evidence: CandidateEvidence, *fields: str) -> str:
    """Render the field values that drove a decision.

    CANDIDATE_SCHEMA.md section 7 requires the reason to reference specific
    field values rather than summarise, so a reader can check the decision
    against the record instead of taking it on faith.
    """
    parts = []
    for name in fields:
        value = getattr(evidence, name)
        if isinstance(value, bool):
            parts.append(f"{name}={str(value).lower()}")
        elif value is None:
            parts.append(f"{name}=null")
        else:
            parts.append(f"{name}={value}")
    return ", ".join(parts)


def supporting_signals(evidence: CandidateEvidence) -> tuple[str, ...]:
    """Evidence that the document workflow is more than an isolated utility."""
    signals = []
    if evidence.category_count >= 2:
        signals.append(f"category_count={evidence.category_count}")
    if evidence.multiple_document_types_handled:
        signals.append("multiple_document_types_handled=true")
    if evidence.pipeline_stage_count >= 2:
        signals.append(f"pipeline_stage_count={evidence.pipeline_stage_count}")
    if evidence.infrastructure_service_present:
        signals.append("infrastructure_service_present=true")
    if evidence.template_directory_present:
        signals.append("template_directory_present=true")
    if evidence.produces_documents:
        signals.append("confirmed generation/conversion code")
    return tuple(signals)


def unknowns(evidence: CandidateEvidence) -> tuple[str, ...]:
    """Evidence that is missing rather than negative.

    Recorded so a decision can say which way it was leaning blind. None of
    these is a rejection reason on its own, and several are explicitly ruled
    out as one.
    """
    gaps = []
    if not evidence.has_pipeline_evidence:
        gaps.append("no pipeline evidence collected")
    if not evidence.has_business_evidence:
        gaps.append("no business evidence collected")
    if not evidence.dependencies:
        gaps.append("no dependency evidence located")
    if evidence.manifest_only:
        gaps.append("all dependency evidence is manifest-only")
    if evidence.industry_category == "unknown":
        gaps.append("industry_category=unknown")
    if evidence.company_name is None:
        gaps.append("company_name=null")
    if evidence.contributor_count is None:
        gaps.append("contributor_count not collected")
    return tuple(gaps)


# --- rejection predicates --------------------------------------------------
#
# One function per rejection_reason in CANDIDATE_SCHEMA.md section 7. Each
# returns a citation string when it fires, or None. Each requires a positive
# combination of observations: none fires on a bare missing field.


def reject_fork_of_library(evidence: CandidateEvidence) -> str | None:
    """A fork that never became a product of its own.

    Not every fork: CANDIDATE_SCHEMA.md's "real product" rule requires
    is_fork = false, but a fork that grew into an independent application with
    its own product framing is exactly the case worth investigating rather than
    discarding, so it is passed through.
    """
    if not evidence.is_fork:
        return None
    if evidence.readme_describes_product and evidence.application_code_exists:
        return None
    return _cite(evidence, "is_fork", "readme_describes_product",
                 "application_code_exists")


def reject_tutorial_or_demo(evidence: CandidateEvidence) -> str | None:
    """A teaching or demonstration artefact.

    The primary form is the one SCORING_MODEL.md section 15 works through for
    docutils-sandbox: no product description, no application code, and the
    document code living outside any production path. All three together, never
    one alone.

    A repository name that says "tutorial" or "examples" strengthens the case
    but cannot make it by itself, since real products carry those words too.
    """
    if evidence.readme_describes_product:
        return None

    token = _name_matches(evidence, TUTORIAL_NAME_TOKENS)

    if not evidence.application_code_exists and not evidence.document_functionality_in_production_code:
        citation = _cite(evidence, "readme_describes_product",
                         "application_code_exists",
                         "document_functionality_in_production_code")
        if token:
            citation += f", repo_name contains {token!r}"
        return citation

    # A named demonstration repository with no product framing and no
    # confirmed production usage.
    if token and not evidence.document_functionality_in_production_code:
        return (f"repo_name contains {token!r}, "
                + _cite(evidence, "readme_describes_product",
                        "document_functionality_in_production_code"))
    return None


def reject_archived_no_signal(evidence: CandidateEvidence) -> str | None:
    """Archived, with nothing to suggest a product worth revisiting.

    Archive status alone is not disqualifying. An archived repository that
    describes a product and shows confirmed document usage is still evidence of
    a company that built a document workflow, so it goes to investigate.
    """
    if not evidence.is_archived:
        return None
    if evidence.readme_describes_product and evidence.code_usage_confirmed:
        return None
    return _cite(evidence, "is_archived", "readme_describes_product",
                 "code_usage_confirmed", "application_code_exists")


def reject_personal_project_no_customers(evidence: CandidateEvidence) -> str | None:
    """Someone's scratch space.

    Requires the repository to name itself as one. Star count, contributor
    count and whether the owner is a user rather than an organisation are all
    explicitly excluded: plenty of real products are small, and plenty of
    personal repositories are popular.
    """
    token = _name_matches(evidence, PERSONAL_NAME_TOKENS)
    if not token:
        return None
    if evidence.readme_describes_product or evidence.application_code_exists:
        return None
    return (f"repo_name contains {token!r}, "
            + _cite(evidence, "readme_describes_product",
                    "application_code_exists",
                    "document_functionality_in_production_code"))


def reject_single_incidental_use(evidence: CandidateEvidence) -> str | None:
    """One library, used in isolation, with no customer-facing workflow.

    All three of the conditions in IMPLEMENTATION_PLAN.md's phase 9 task 4 have
    to hold: the usage is isolated, there is no meaningful pipeline, and
    nothing suggests the documents reach a customer. This is the weak signal
    BUSINESS_HYPOTHESIS.md section 5 describes, and deliberately not a count of
    dependencies: a repository declaring four document libraries in one
    requirements file is not thereby a pipeline.
    """
    if not evidence.dependencies:
        # Nothing located is a gap, not a finding. Investigate instead.
        return None
    if evidence.readme_describes_product:
        # A stated product with thin document evidence is the investigate case,
        # not a rejection.
        return None

    isolated = (
        evidence.category_count <= 1
        and not evidence.multiple_document_types_handled
        and not evidence.template_directory_present
        and not evidence.infrastructure_service_present
        and evidence.pipeline_stage_count <= 1
    )
    if not isolated:
        return None

    return _cite(evidence, "category_count", "multiple_document_types_handled",
                 "template_directory_present", "infrastructure_service_present",
                 "pipeline_stage_count", "readme_describes_product")


#: Evaluated in this order. Structural facts about the repository come before
#: judgments about how the library is used, so the most direct explanation wins
#: when more than one would fire.
REJECTION_RULES: tuple[tuple[str, Callable[[CandidateEvidence], str | None]], ...] = (
    (FORK_OF_LIBRARY, reject_fork_of_library),
    (ARCHIVED_NO_SIGNAL, reject_archived_no_signal),
    (PERSONAL_PROJECT_NO_CUSTOMERS, reject_personal_project_no_customers),
    (TUTORIAL_OR_DEMO, reject_tutorial_or_demo),
    (SINGLE_INCIDENTAL_USE, reject_single_incidental_use),
)


# --- keep ------------------------------------------------------------------


def meets_keep_criteria(evidence: CandidateEvidence) -> tuple[bool, str]:
    """The four fields that must hold together, per CANDIDATE_SCHEMA.md
    section 6, plus at least one sign the workflow is not an isolated utility.
    """
    required = {
        "readme_describes_product": evidence.readme_describes_product,
        "application_code_exists": evidence.application_code_exists,
        "is_fork": not evidence.is_fork,
        "document_functionality_in_production_code":
            evidence.document_functionality_in_production_code,
    }
    missing = [name for name, held in required.items() if not held]
    if missing:
        return False, f"keep criteria not met: {', '.join(missing)}"

    if not supporting_signals(evidence):
        return False, (
            "keep criteria met but no evidence the document workflow is more "
            "than an isolated utility"
        )
    return True, ""


# --- confidence ------------------------------------------------------------


def assess_confidence(
    evidence: CandidateEvidence, status: str, signals: Sequence[str],
    gaps: Sequence[str],
) -> str:
    """How strongly the decision rests on directly observed fields.

    Reported alongside the status and never allowed to change it: a low-
    confidence keep is still a keep, flagged as worth checking rather than
    quietly demoted.
    """
    if not evidence.has_pipeline_evidence or not evidence.has_business_evidence:
        return LOW

    if status == KEEP:
        return HIGH if len(signals) >= 2 else MEDIUM

    if status == REJECT:
        # A rejection resting on structural facts is firmer than one resting on
        # the shape of the usage.
        if evidence.is_fork or evidence.is_archived:
            return HIGH if evidence.has_business_evidence else MEDIUM
        return MEDIUM if evidence.dependencies else LOW

    # Investigate. Confirmed usage means the uncertainty is about context
    # rather than about whether anything happens at all.
    if evidence.manifest_only or not evidence.dependencies:
        return LOW
    if evidence.code_usage_confirmed and len(gaps) <= 2:
        return MEDIUM
    return LOW if len(gaps) >= 4 else MEDIUM


# --- the decision ----------------------------------------------------------


def qualify(evidence: CandidateEvidence) -> Decision:
    """Classify one candidate. Pure, deterministic, and offline."""
    signals = supporting_signals(evidence)
    gaps = unknowns(evidence)

    # No rejection is possible without evidence to reject on.
    #
    # Every negative field on a candidate whose evidence was never collected
    # reads as false, so the predicates below would fire on a record nobody
    # looked at: an uncollected candidate matched tutorial_or_demo on three
    # bare falses. That is the "absence of evidence becomes confirmed absence"
    # failure this module exists to avoid, and it has to be blocked here rather
    # than guarded separately in each rule.
    if not evidence.has_pipeline_evidence or not evidence.has_business_evidence:
        return Decision(
            candidate_id=evidence.candidate_id,
            status=INVESTIGATE,
            reason=(
                "evidence not collected, so no rejection is supportable | "
                + "; ".join(gaps)
            ),
            rejection_reason=None,
            confidence=LOW,
            supporting_signals=signals,
            unknowns=gaps,
        )

    for rejection_reason, rule in REJECTION_RULES:
        citation = rule(evidence)
        if citation is None:
            continue
        return Decision(
            candidate_id=evidence.candidate_id,
            status=REJECT,
            reason=f"{rejection_reason}: {citation}",
            rejection_reason=rejection_reason,
            confidence=assess_confidence(evidence, REJECT, signals, gaps),
            supporting_signals=signals,
            unknowns=gaps,
        )

    keeps, why_not = meets_keep_criteria(evidence)
    if keeps:
        reason = _cite(
            evidence, "readme_describes_product", "application_code_exists",
            "is_fork", "document_functionality_in_production_code",
            "code_usage_confirmed", "category_count", "pipeline_stage_count",
        )
        if signals:
            reason += " | supporting: " + "; ".join(signals)
        return Decision(
            candidate_id=evidence.candidate_id,
            status=KEEP,
            reason=reason,
            rejection_reason=None,
            confidence=assess_confidence(evidence, KEEP, signals, gaps),
            supporting_signals=signals,
            unknowns=gaps,
        )

    reason = why_not + " | " + _cite(
        evidence, "category_count", "code_usage_confirmed",
        "pipeline_stage_count", "readme_describes_product",
        "application_code_exists",
        "document_functionality_in_production_code",
    )
    if signals:
        reason += " | supporting: " + "; ".join(signals)
    if gaps:
        reason += " | unknown: " + "; ".join(gaps)

    return Decision(
        candidate_id=evidence.candidate_id,
        status=INVESTIGATE,
        reason=reason,
        rejection_reason=None,
        confidence=assess_confidence(evidence, INVESTIGATE, signals, gaps),
        supporting_signals=signals,
        unknowns=gaps,
    )


# --- engine ----------------------------------------------------------------


@dataclass
class QualificationReport:
    """Counts only. Qualification does not rank."""

    processed: int = 0
    keep: int = 0
    investigate: int = 0
    reject: int = 0
    rejection_reasons: dict = field(default_factory=dict)
    confidence: dict = field(default_factory=dict)

    def record(self, decision: Decision) -> None:
        self.processed += 1
        setattr(self, decision.status, getattr(self, decision.status) + 1)
        if decision.rejection_reason:
            self.rejection_reasons[decision.rejection_reason] = (
                self.rejection_reasons.get(decision.rejection_reason, 0) + 1
            )
        self.confidence[decision.confidence] = (
            self.confidence.get(decision.confidence, 0) + 1
        )

    def summary_lines(self) -> list[str]:
        lines = [
            f"candidates qualified  {self.processed}",
            f"  keep                {self.keep}",
            f"  investigate         {self.investigate}",
            f"  reject              {self.reject}",
        ]
        for reason, count in sorted(self.rejection_reasons.items()):
            lines.append(f"    {reason:<32}{count}")
        for band in (HIGH, MEDIUM, LOW):
            lines.append(f"  confidence {band:<10}{self.confidence.get(band, 0)}")
        return lines


class QualificationEngine:
    """Applies the rules and persists the results. No network access."""

    def __init__(self, connection) -> None:
        self._conn = connection

    def pending(self) -> list[str]:
        return storage.candidates_needing_qualification(self._conn)

    def qualify_candidate(self, candidate_id: str) -> Decision:
        decision = qualify(CandidateEvidence.load(self._conn, candidate_id))
        storage.upsert_qualification(
            self._conn,
            candidate_id=decision.candidate_id,
            qualification_status=decision.status,
            qualification_reason=decision.reason,
            rejection_reason=decision.rejection_reason,
            confidence=decision.confidence,
        )
        return decision

    def run(self, candidate_ids: Sequence[str] | None = None) -> QualificationReport:
        report = QualificationReport()
        for candidate_id in (
            candidate_ids if candidate_ids is not None else self.pending()
        ):
            report.record(self.qualify_candidate(candidate_id))
        return report
