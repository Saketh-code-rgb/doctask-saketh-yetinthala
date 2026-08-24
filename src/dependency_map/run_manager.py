"""Run manager: orchestrates the stages, and nothing else.

Each stage owns its own logic; this module decides what runs, in what order,
and over which candidates. It holds no stage logic of its own.

**Resumability is not a feature this module implements.** Each stage asks the
database what is missing rather than being handed a resume pointer: discovery
records what it found, and evidence collection processes candidates that have a
discovery hit but no evidence rows. Rerunning simply picks up where things
stopped, because the query "what is missing" returns a shorter list the second
time. Nothing tracks progress separately, so there is no progress record that
can disagree with what was actually committed (TECHNICAL_DESIGN.md section 16).

Partial failure follows section 15: one candidate failing marks that
candidate's evidence missing and the run moves on, while a systemic failure,
meaning a rate limit that cannot be waited out, stops the run rather than
burning the remaining candidates producing nothing.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Iterable, Sequence

from . import storage
from .dedup import RunStats, plan_rotation, run_stats, verify_fresh_batch
from .discovery import DiscoveryEngine, DiscoveryError, QueryGenerator
from .evidence import EvidenceCollector, EvidenceOutcome, collect_for_candidates
from .qualification import QualificationEngine, QualificationReport
from .scoring import ScoringEngine, ScoringReport

logger = logging.getLogger(__name__)

STAGE_DISCOVERY = "discovery"
STAGE_EVIDENCE = "evidence"
STAGE_QUALIFICATION = "qualification"
STAGE_SCORING = "scoring"

#: Every stage, in the order they must run.
STAGES: tuple[str, ...] = (
    STAGE_DISCOVERY, STAGE_EVIDENCE, STAGE_QUALIFICATION, STAGE_SCORING,
)


class RunError(Exception):
    """The run could not continue."""


@dataclass
class RunReport:
    """What one orchestrated run did, per stage."""

    run_id: str
    stages: tuple[str, ...] = ()
    rotation: str = ""
    discovery: RunStats | None = None
    candidates_needing_evidence: int = 0
    evidence_completed: int = 0
    evidence_failed: int = 0
    evidence_skipped: int = 0
    qualification: QualificationReport | None = None
    scoring: ScoringReport | None = None
    failures: list[tuple[str, str]] = field(default_factory=list)

    def summary_lines(self) -> list[str]:
        lines = [
            f"run                        {self.run_id}",
            f"stages                     {', '.join(self.stages)}",
        ]
        if self.rotation:
            lines.append(f"rotation                   {self.rotation}")
        if self.discovery is not None:
            lines += [
                f"queries executed           {self.discovery.queries_executed}",
                f"queries failed             {self.discovery.queries_failed}",
                f"zero-result queries        {self.discovery.zero_result_queries}",
                f"capped queries             {self.discovery.capped_queries}",
                f"raw results                {self.discovery.raw_results}",
                f"unique repositories        {self.discovery.unique_repositories}",
                f"previously seen            {self.discovery.previously_seen}",
                f"discovered candidates      {self.discovery.new_candidates}",
            ]
        if STAGE_EVIDENCE in self.stages:
            lines += [
                f"candidates needing evidence{self.candidates_needing_evidence:>4}",
                f"evidence completed         {self.evidence_completed}",
                f"evidence failed            {self.evidence_failed}",
                f"already complete, skipped  {self.evidence_skipped}",
            ]
        if self.qualification is not None:
            lines += ["  " + line for line in self.qualification.summary_lines()]
        if self.scoring is not None:
            lines += ["  " + line for line in self.scoring.summary_lines()]
        return lines


class RunManager:
    """Creates a run and drives the stages over it."""

    def __init__(
        self,
        connection,
        *,
        discovery_engine: DiscoveryEngine | None = None,
        evidence_collector: EvidenceCollector | None = None,
        query_generator: QueryGenerator | None = None,
        qualification_engine: QualificationEngine | None = None,
        scoring_engine: ScoringEngine | None = None,
    ) -> None:
        self._conn = connection
        self._discovery = discovery_engine
        self._evidence = evidence_collector
        self._generator = query_generator
        # Qualification needs nothing but the database, so it is built here
        # rather than injected. It makes no network calls by construction.
        self._qualification = qualification_engine or QualificationEngine(connection)
        # Scoring needs weights, so unlike qualification it must be injected.
        self._scoring = scoring_engine

    # -- run setup ---------------------------------------------------------

    def next_run_id(self) -> str:
        return f"run_{len(storage.list_runs(self._conn)) + 1}"

    def start_run(self, run_id: str | None = None) -> tuple[str, object]:
        """Create the run row with its rotation already planned and recorded.

        The rotation is decided before any API budget is spent, and stored in
        `runs.notes`, so how this run differs from the last is readable from
        the database rather than reconstructed afterwards.
        """
        run_index = len(storage.list_runs(self._conn)) + 1
        run_id = run_id or f"run_{run_index}"
        if storage.get_run(self._conn, run_id) is not None:
            raise RunError(f"Run {run_id!r} already exists")

        rotation = plan_rotation(run_index)
        storage.create_run(self._conn, run_id, notes=rotation.description)
        return run_id, rotation

    # -- orchestration -----------------------------------------------------

    def run(
        self,
        *,
        run_id: str | None = None,
        stages: Sequence[str] = STAGES,
        tiers: Iterable[int] = (1, 2, 3),
        query_limit: int | None = None,
        evidence_limit: int | None = None,
    ) -> RunReport:
        for stage in stages:
            if stage not in STAGES:
                raise RunError(
                    f"Unknown stage {stage!r}. Available: {', '.join(STAGES)}"
                )

        rotation = None
        if run_id is None or storage.get_run(self._conn, run_id) is None:
            run_id, rotation = self.start_run(run_id)

        report = RunReport(run_id=run_id, stages=tuple(stages))
        if rotation is not None:
            report.rotation = rotation.description

        if STAGE_DISCOVERY in stages:
            self._run_discovery(run_id, tiers, query_limit, report)

        if STAGE_EVIDENCE in stages:
            self._run_evidence(run_id, evidence_limit, report)

        if STAGE_QUALIFICATION in stages:
            report.qualification = self._qualification.run()

        if STAGE_SCORING in stages:
            if self._scoring is None:
                raise RunError(
                    "Scoring stage requested but no engine was provided; it "
                    "needs the weights from weights.yaml"
                )
            report.scoring = self._scoring.run()

        storage.finish_run(self._conn, run_id)
        return report

    def _run_discovery(self, run_id, tiers, query_limit, report) -> None:
        if self._discovery is None:
            raise RunError("Discovery stage requested but no engine was provided")

        if self._generator is not None:
            planned = self._generator.generate(tiers)
            if query_limit is not None:
                planned = planned[:query_limit]
            # Refuse to replay an earlier run before spending any budget.
            verify_fresh_batch(self._conn, run_id, planned)

        try:
            outcome = self._discovery.run(run_id, tiers=tiers, limit=query_limit)
        except DiscoveryError as exc:
            # Discovery already persisted whatever it completed, so the run is
            # resumable. Surface the failure rather than swallowing it.
            report.failures.append(("discovery", str(exc)))
            raise
        report.failures.extend(outcome.failures)
        report.discovery = run_stats(self._conn, run_id)

    def _run_evidence(self, run_id, evidence_limit, report) -> None:
        if self._evidence is None:
            raise RunError("Evidence stage requested but no collector was provided")

        surfaced = set(storage.list_candidate_ids_for_run(self._conn, run_id))
        pending_all = self._evidence.pending()

        # Only candidates this run surfaced, unless the run discovered nothing,
        # in which case an evidence-only pass should work through the backlog.
        pending = [c for c in pending_all if c in surfaced] if surfaced else pending_all
        report.evidence_skipped = len(surfaced - set(pending_all)) if surfaced else 0

        if evidence_limit is not None:
            pending = pending[:evidence_limit]
        report.candidates_needing_evidence = len(pending)

        outcomes: list[EvidenceOutcome] = collect_for_candidates(
            self._evidence, pending
        )
        for outcome in outcomes:
            if outcome.ok:
                report.evidence_completed += 1
            else:
                report.evidence_failed += 1
                report.failures.append((outcome.candidate_id, outcome.error or ""))
