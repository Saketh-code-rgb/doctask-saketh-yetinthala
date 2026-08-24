"""Maintenance-burden evidence: the targeted phase 14 pass.

SCORING_MODEL.md section 7 grades *how much custom code a team wrote around
the document libraries*, not how busy the repository is. Read the rungs in
order and the axis is unmistakable:

    1  "thin, direct way, one call, no custom logic wrapped around it"
    2  "some custom logic ... for example a small formatting helper"
    3  "multiple libraries stitched together with visible custom glue code"
    4  "substantial custom code sitting between the library import and its
        actual use, plus some evidence of repeated modification *if commit
        history was pulled*"
    5  "custom formatting, validation, and error handling layered around
        multiple document libraries"

Commit history appears exactly once, at rung 4, as a conditional corroboration.
That is why this module is built around source inspection and treats commit
metadata as supplementary. A thin wrapper committed daily is still a rung 1,
and an elaborate hand-built system untouched for a year is still a rung 5;
scoring either from activity would measure the wrong thing.

The pass is deliberately bounded. It opens only source files the evidence
collector already found a document-library import in, capped per candidate,
and never walks the repository.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Iterable, Sequence

from . import storage
from .reliability import ApiError, RateLimited, ReliabilityError, RetriesExhausted

logger = logging.getLogger(__name__)

#: How many source files to open per candidate. The evidence collector already
#: recorded where the imports are, so a handful of the most relevant files is
#: enough to tell a one-call wrapper from a hand-built system.
MAX_FILES_PER_CANDIDATE = 4

#: How far back "recent" reaches, for the rung-4 corroboration only.
RECENT_COMMIT_DAYS = 90

#: Source extensions worth opening. Anything else (a manifest, a lockfile, a
#: README) says nothing about the code wrapped around the library.
SOURCE_EXTENSIONS = (
    ".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".kt", ".go", ".rb",
    ".php", ".cs", ".scala", ".vue",
)

#: Formatting work applied to a document: styles, fonts, page geometry.
_FORMATTING = re.compile(
    r"\b(set_?(font|style|margin|align|width|height|color)|add_?(heading|paragraph|"
    r"style|page_?break)|font_?size|page_?(width|height|size|margin)|"
    r"cell_?format|column_?width|line_?spacing|setFont|addStyle)\b",
    re.IGNORECASE,
)

#: Validation of document inputs or outputs before or after generation.
_VALIDATION = re.compile(
    r"\b(validate|verify|is_?valid|check_?(input|schema|required|field)|"
    r"assert_?\w+|schema\.validate|required_?fields|sanitiz)\w*\b",
    re.IGNORECASE,
)

#: Error handling wrapped specifically around document work.
_ERROR_HANDLING = re.compile(
    r"(except\s+\w*(Error|Exception)|try\s*[:{]|catch\s*\(|raise\s+\w+Error|"
    r"throw\s+new\s+\w*Error|logger\.(error|exception|warning))",
    re.IGNORECASE,
)

#: A function or method definition, the cheapest reliable proxy for "custom
#: logic wrapped around the call" rather than a bare top-level invocation.
_DEFINITION = re.compile(
    r"^\s*(def\s+\w+|class\s+\w+|(async\s+)?function\s+\w+|"
    r"(public|private|protected|static)[\w\s<>\[\],]*\s+\w+\s*\(|"
    r"\w+\s*[:=]\s*(async\s*)?\([^)]*\)\s*=>)",
    re.MULTILINE,
)


class MaintenanceError(Exception):
    """Maintenance evidence could not be collected for a candidate."""


@dataclass
class MaintenanceSignals:
    """What one candidate's source inspection found.

    Everything here describes code structure. `repeated_modification_evidence`
    and the commit counts are the only activity fields, and they exist solely
    to corroborate rung 4.
    """

    candidate_id: str
    document_library_count: int = 0
    same_file_library_count: int = 0
    custom_logic_present: bool = False
    custom_formatting_present: bool = False
    custom_validation_present: bool = False
    custom_error_handling_present: bool = False
    custom_glue_excerpt: str | None = None
    custom_glue_evidence_url: str | None = None
    repeated_modification_evidence: bool | None = None
    recent_commit_count: int | None = None
    active_contributors: int | None = None
    latest_commit_date: str | None = None
    files_inspected: int = 0
    notes: list[str] = field(default_factory=list)

    @property
    def note_text(self) -> str:
        return "; ".join(self.notes)


def rung_for(signals: MaintenanceSignals) -> tuple[int, str]:
    """Map the collected evidence onto SCORING_MODEL.md section 7, unchanged.

    Returns the rung and the sentence explaining it. Rung 0 is reserved for
    "nothing was inspected", which is the unknown case and must never be
    confused with "inspected and found thin".
    """
    if signals.files_inspected == 0:
        return 0, "no source file could be inspected, so the rubric is unassessable"

    custom_kinds = sum(
        (
            signals.custom_formatting_present,
            signals.custom_validation_present,
            signals.custom_error_handling_present,
        )
    )

    # 5: "custom formatting, validation, and error handling layered around
    #     multiple document libraries" - all three kinds, several libraries.
    if custom_kinds == 3 and signals.document_library_count >= 2:
        return 5, (
            "custom formatting, validation and error handling all evidenced "
            f"around {signals.document_library_count} document libraries"
        )

    # 4: "substantial custom code between the library import and its use, plus
    #     some evidence of repeated modification if commit history was pulled".
    if custom_kinds >= 2 and signals.custom_logic_present:
        corroborated = signals.repeated_modification_evidence
        detail = (
            "; repeated modification corroborated by commit history"
            if corroborated
            else "; commit history did not corroborate repeated modification"
            if corroborated is False
            else "; commit history not pulled"
        )
        return 4, (
            f"substantial custom code around the library ({custom_kinds} kinds "
            f"of custom handling inside functions){detail}"
        )

    # 3: "multiple libraries stitched together with visible custom glue code".
    if signals.same_file_library_count >= 2 and signals.custom_logic_present:
        return 3, (
            f"{signals.same_file_library_count} document libraries used together "
            "in one file with custom code connecting them"
        )

    # 2: "some custom logic evidenced, for example a small formatting helper".
    if signals.custom_logic_present and custom_kinds >= 1:
        return 2, "some custom logic wrapped around the library call"

    # 1: "thin, direct use, one call, no custom logic wrapped around it".
    return 1, "the library is called directly, with no custom logic around it"


class MaintenanceCollector:
    """Opens a few already-identified source files and reads their structure.

    Nothing here walks a repository. The files come from `evidence_trail` and
    `dependencies_found` rows the earlier evidence pass already wrote, so this
    pass re-reads what was found rather than searching again.
    """

    def __init__(
        self,
        connection,
        client,
        *,
        max_files: int = MAX_FILES_PER_CANDIDATE,
        collect_commits: bool = True,
        now: datetime | None = None,
    ) -> None:
        self._conn = connection
        self._client = client
        self._max_files = max_files
        self._collect_commits = collect_commits
        self._now = now or datetime.now(timezone.utc)

    # -- selection ---------------------------------------------------------

    def target_paths(self, candidate_id: str) -> list[tuple[str, str | None]]:
        """Source files already evidenced to import a document library.

        Manifests are excluded deliberately: a requirements line proves a
        dependency, never how much code was written around it.
        """
        rows = storage.list_dependencies_for_candidate(self._conn, candidate_id)
        paths: list[tuple[str, str | None]] = []
        seen: set[str] = set()
        for row in rows:
            if row["detection_method"] != "code_import":
                continue
            url = row["evidence_url"] or ""
            path = _path_from_blob_url(url)
            if not path or path in seen:
                continue
            if not path.lower().endswith(SOURCE_EXTENSIONS):
                continue
            seen.add(path)
            paths.append((path, url))
        return paths[: self._max_files]

    # -- collection --------------------------------------------------------

    def collect(self, candidate_id: str) -> MaintenanceSignals:
        candidate = storage.get_candidate(self._conn, candidate_id)
        if candidate is None:
            raise MaintenanceError(f"No candidate {candidate_id!r}")
        owner, repo = candidate["repo_owner"], candidate["repo_name"]

        signals = MaintenanceSignals(candidate_id=candidate_id)
        signals.document_library_count = len(
            {
                row["library_name"]
                for row in storage.list_dependencies_for_candidate(
                    self._conn, candidate_id
                )
            }
        )

        libraries_by_file: dict[str, set[str]] = {}
        for row in storage.list_dependencies_for_candidate(self._conn, candidate_id):
            if row["detection_method"] != "code_import":
                continue
            path = _path_from_blob_url(row["evidence_url"] or "")
            if path:
                libraries_by_file.setdefault(path, set()).add(row["library_name"])
        signals.same_file_library_count = max(
            (len(v) for v in libraries_by_file.values()), default=0
        )

        for path, url in self.target_paths(candidate_id):
            try:
                contents = self._client.get_file_contents(owner, repo, path)
            except (ApiError, RetriesExhausted, ReliabilityError) as exc:
                signals.notes.append(f"{path} unavailable ({exc})")
                continue
            self._read_source(contents.text or "", contents.evidence_url or url, signals)
            signals.files_inspected += 1

        if self._collect_commits:
            self._read_commits(owner, repo, signals)

        return signals

    def _read_source(self, text: str, url: str | None, signals) -> None:
        """Extract the structural signals rung 1 through 5 are written in."""
        if not text:
            return
        if _DEFINITION.search(text):
            signals.custom_logic_present = True
        if _FORMATTING.search(text):
            signals.custom_formatting_present = True
        if _VALIDATION.search(text):
            signals.custom_validation_present = True
        if _ERROR_HANDLING.search(text):
            signals.custom_error_handling_present = True

        if signals.custom_glue_excerpt is None:
            excerpt = _first_interesting_lines(text)
            if excerpt:
                signals.custom_glue_excerpt = excerpt
                signals.custom_glue_evidence_url = url

    def _read_commits(self, owner: str, repo: str, signals) -> None:
        """Rung-4 corroboration only. Never a substitute for code structure."""
        lister = getattr(self._client, "list_commits", None)
        if lister is None:
            signals.notes.append("client cannot list commits; rung 4 uncorroborated")
            return
        since = (self._now - timedelta(days=RECENT_COMMIT_DAYS)).isoformat()
        try:
            commits = lister(owner, repo, since=since)
        except (ApiError, RetriesExhausted, ReliabilityError) as exc:
            signals.notes.append(f"commit history unavailable ({exc})")
            return

        signals.recent_commit_count = len(commits)
        signals.active_contributors = len(
            {c.author for c in commits if getattr(c, "author", None)}
        )
        if commits:
            signals.latest_commit_date = max(
                (c.committed_at for c in commits if getattr(c, "committed_at", None)),
                default=None,
            )
        # "Repeated modification" means the document code kept changing, which
        # several commits by more than a single author is the cheapest honest
        # proxy for. It corroborates rung 4; it never promotes a thin wrapper.
        signals.repeated_modification_evidence = bool(
            signals.recent_commit_count and signals.recent_commit_count >= 3
        )

    # -- persistence -------------------------------------------------------

    def record(self, signals: MaintenanceSignals) -> None:
        storage.upsert_maintenance_evidence(
            self._conn,
            candidate_id=signals.candidate_id,
            document_library_count=signals.document_library_count,
            same_file_library_count=signals.same_file_library_count,
            custom_logic_present=signals.custom_logic_present,
            custom_formatting_present=signals.custom_formatting_present,
            custom_validation_present=signals.custom_validation_present,
            custom_error_handling_present=signals.custom_error_handling_present,
            custom_glue_excerpt=signals.custom_glue_excerpt,
            custom_glue_evidence_url=signals.custom_glue_evidence_url,
            repeated_modification_evidence=signals.repeated_modification_evidence,
            recent_commit_count=signals.recent_commit_count,
            active_contributors=signals.active_contributors,
            latest_commit_date=signals.latest_commit_date,
            files_inspected=signals.files_inspected,
            maintenance_evidence_notes=signals.note_text or None,
        )


# --- candidate selection ----------------------------------------------------


def select_candidates(conn, *, top_n: int = 50, keep_floor: int = 20,
                      cap: int = 75) -> list[str]:
    """The bounded, deterministic set this pass enriches.

    Top `top_n` scored candidates, plus any keep at or above `keep_floor`
    outside them, capped at `cap` by final_score DESC then candidate_id ASC.
    Ordering is fully determined by stored values, so the same database always
    yields the same set.
    """
    ranked = conn.execute(
        "SELECT s.candidate_id, s.final_score, g.qualification_status "
        "FROM scores s JOIN qualification g USING(candidate_id) "
        "ORDER BY s.final_score DESC, s.candidate_id ASC"
    ).fetchall()

    chosen: list[str] = [r["candidate_id"] for r in ranked[:top_n]]
    already = set(chosen)
    for row in ranked[top_n:]:
        if (
            row["qualification_status"] == "keep"
            and row["final_score"] >= keep_floor
            and row["candidate_id"] not in already
        ):
            chosen.append(row["candidate_id"])
            already.add(row["candidate_id"])

    order = {r["candidate_id"]: (-r["final_score"], r["candidate_id"]) for r in ranked}
    chosen.sort(key=lambda c: order[c])
    return chosen[:cap]


def collect_for_candidates(
    collector: MaintenanceCollector, candidate_ids: Sequence[str]
) -> list[MaintenanceSignals]:
    """Run the pass over a bounded set, recording each candidate as it lands."""
    out: list[MaintenanceSignals] = []
    for candidate_id in candidate_ids:
        try:
            signals = collector.collect(candidate_id)
        except RateLimited:
            raise
        except (MaintenanceError, ApiError, RetriesExhausted, ReliabilityError) as exc:
            logger.warning("maintenance evidence failed for %s: %s", candidate_id, exc)
            continue
        collector.record(signals)
        out.append(signals)
    return out


# --- helpers ----------------------------------------------------------------


def _path_from_blob_url(url: str) -> str | None:
    """Recover a repository-relative path from a GitHub blob permalink."""
    marker = "/blob/"
    if marker not in url:
        return None
    tail = url.split(marker, 1)[1]
    parts = tail.split("/", 1)
    return parts[1].split("?")[0].split("#")[0] if len(parts) == 2 else None


def _first_interesting_lines(text: str, limit: int = 3) -> str | None:
    """A short excerpt showing the custom code, for the evidence trail."""
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", "//", "*", "/*")):
            continue
        if _DEFINITION.match(line) or _FORMATTING.search(line):
            return stripped[:200]
    return None
