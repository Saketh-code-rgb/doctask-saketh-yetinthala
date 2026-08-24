"""Evidence collector: gather what a public repository actually shows.

This component fills in CANDIDATE_SCHEMA.md sections 2 through 6 and 9 for
candidates discovery has already found. It collects evidence and nothing else:
it does not decide whether a candidate is worth keeping, and it assigns no
score. Those are pure functions over what is stored here, built in later
phases, so the rules can be revised and rerun without spending API budget
again.

The governing rule is the one CANDIDATE_SCHEMA.md opens with: nothing is
recorded as true because it seems true. Every boolean this module sets to true
is backed by something specific that was actually fetched, and the URL it came
from goes into the evidence trail. Where the evidence is absent the field stays
false or null rather than being inferred, which is why a great many candidates
will legitimately look thin. An honestly thin record is more useful than a
confident invented one, because qualification can tell the difference.

**Budget.** This is the call-heaviest stage in the pipeline, so the shape of it
matters. Per candidate: one repository metadata call, one root directory
listing, one README fetch, one fetch per manifest actually present, and at most
a couple of targeted code searches. The directory listing is what keeps this
cheap: it answers "which manifest is here, is there a templates directory, what
does the root look like" from the core REST budget of 5,000 an hour, rather
than from the code-search bucket of 10 a minute. Nothing crawls a repository.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from typing import Iterable, Sequence

from . import storage
from .clients.github_client import GitHubClient
from .library_universe import LibraryEntry, LibraryUniverse
from .reliability import ApiError, RateLimited, ReliabilityError, RetriesExhausted

logger = logging.getLogger(__name__)

#: Paths whose contents are demonstrations rather than the running product.
#: Used to describe where evidence was found, not to filter it out.
NON_PRODUCTION_PREFIXES = (
    "example", "examples", "test", "tests", "demo", "demos",
    "doc", "docs", "sample", "samples", "tutorial", "tutorials",
    "script", "scripts", "benchmark", "benchmarks", "fixture", "fixtures",
)

#: Directory names that suggest an application rather than a script collection.
APPLICATION_DIRECTORIES = frozenset(
    {"src", "app", "apps", "lib", "api", "server", "backend", "services",
     "service", "cmd", "pkg", "internal", "core", "web", "frontend", "client"}
)

#: Monorepo container directories, which hold the application rather than
#: being it.
#:
#: These cannot join APPLICATION_DIRECTORIES unconditionally. A `packages/`
#: directory holding a docs site and nothing else is not an application, and
#: counting it as one would trade a false negative for a false positive. So
#: presence is not enough: the directory has to contain at least one member
#: that is not documentation.
#:
#: The gap this closes was real. `bigcapitalhq/bigcapital`, a monorepo rooted
#: at `packages/`, recorded application_code_exists = false, which was the
#: single field keeping a candidate with a deployed conversion service, five
#: confirmed dependencies and 3,846 stars out of the keep bucket.
WORKSPACE_DIRECTORIES = frozenset(
    {"packages", "modules", "workspaces", "libs", "components", "projects"}
)

#: Workspace members that do not make the workspace an application.
NON_APPLICATION_MEMBERS = frozenset(
    {"docs", "doc", "documentation", "website", "site", "examples", "example",
     "demo", "demos", "samples", "sample", "tutorial", "tutorials",
     "test", "tests", "e2e", "fixtures", "assets", "static", "images"}
)

#: Directory names that suggest stored document templates.
TEMPLATE_DIRECTORIES = frozenset(
    {"templates", "template", "reports", "report", "documents", "docs_templates",
     "letterheads", "forms"}
)

#: Filenames that carry an infrastructure signal.
INFRASTRUCTURE_FILES = (
    "dockerfile", "docker-compose.yml", "docker-compose.yaml",
    "compose.yml", "compose.yaml",
)

#: The same filenames, matched wherever they sit in the tree. Discovery
#: recorded the exact path it matched (schema 3), so the collector can open
#: that file instead of hoping an equivalent exists at the repository root.
#: 39 percent of run 1's recovered paths were not at the root.
NESTED_INFRASTRUCTURE_NAMES = frozenset(INFRASTRUCTURE_FILES)

#: Directory names that mark example material rather than a product.
EXAMPLE_DIRECTORIES = frozenset({"examples", "example", "demo", "demos", "samples"})

#: README phrasing that marks teaching material or a sample rather than a
#: product. Evidence only: nothing rejects on this, because a real product's
#: README can still use the word "example".
_PURPOSE_EXAMPLE = re.compile(
    r"^\s{0,3}#{1,3}\s*(examples?|demos?|tutorials?|getting started|quick ?start|"
    r"sample code|usage examples?)\s*$"
    r"|\bthis (?:repo|repository|project) (?:is|contains) (?:an? )?"
    r"(?:example|demo|sample|tutorial|starter|boilerplate|template)\b",
    re.IGNORECASE | re.MULTILINE,
)

#: A catalogue of other people's software: an app store, a homelab collection,
#: an awesome-list. Run 1 surfaced twelve of these from tier-1 compose queries,
#: where one entry among hundreds happened to name a document service.
_PURPOSE_CATALOGUE = re.compile(
    r"\b(?:awesome[- ]list|app[- ]?store|application catalogue|application catalog|"
    r"self[- ]hosted (?:apps|applications|catalogue|catalog)|"
    r"curated list of|list of awesome|collection of (?:docker|compose|apps)|"
    r"one[- ]click (?:apps|install)|app catalog)\b",
    re.IGNORECASE,
)

#: Manifest filenames recognised exactly, whatever directory they sit in.
MANIFEST_BASENAMES = frozenset(
    {"requirements.txt", "pyproject.toml", "package.json", "package-lock.json",
     "pom.xml", "build.gradle", "build.gradle.kts", "packages.config"}
)

#: Directories worth one extra listing when they exist at the repository root.
#: Bounded on purpose: this is a short look in likely places, not a walk.
LIKELY_MANIFEST_DIRS = (
    "requirements", "docker", "deploy", "deployment", "config",
    "src", "app", "server", "backend", "packages",
)

#: How many of those directories to actually list, per candidate.
MAX_MANIFEST_DIR_LISTINGS = 4

README_NAMES = ("readme.md", "readme.rst", "readme.txt", "readme")

#: Extensions that hold executable source. A code-search hit outside this set
#: is not a call site, whatever it contains.
#:
#: This distinction is load-bearing rather than cosmetic. GitHub code search
#: matches text in *any* file, so searching a repository for "python-docx"
#: returns its requirements.txt, its lockfiles, its dependabot config and its
#: README alongside any actual import. Recording those as `code_import` would
#: turn a manifest-only candidate into a confirmed-usage one, which is exactly
#: the fabricated "used" claim CANDIDATE_SCHEMA.md section 4 warns against, and
#: it would flow straight into the scoring gate that caps unconfirmed usage.
SOURCE_EXTENSIONS = frozenset(
    {"py", "js", "ts", "tsx", "jsx", "mjs", "cjs", "java", "kt", "scala",
     "cs", "go", "rb", "php", "rs", "swift", "vue", "svelte", "pyi"}
)

#: Phrases that mark a README as describing a product for someone, rather than
#: describing what a script does internally. A match supplies the quoted
#: excerpt CANDIDATE_SCHEMA.md section 6 requires before the flag can be true.
PRODUCT_PHRASES = (
    "for teams", "for businesses", "for companies", "for customers",
    "our customers", "our clients", "your customers", "your clients",
    "customers", "clients", "platform for", "solution for", "service for",
    "helps you", "lets you", "allows you to", "enables you to",
    "used by", "trusted by", "saas", "self-hosted", "open-source alternative",
    "all-in-one", "designed for", "built for", "made for",
)

#: Keywords per industry_category, drawn from BUSINESS_HYPOTHESIS.md section 1.
INDUSTRY_KEYWORDS: dict[str, tuple[str, ...]] = {
    "legal_contracts": ("contract", "legal", "law firm", "clause", "nda",
                        "agreement", "litigation", "paralegal", "compliance filing"),
    "real_estate": ("real estate", "property management", "property manager",
                    "lease", "tenant", "landlord", "proptech", "rental agreement",
                    "brokerage"),
    "healthcare_diagnostics": ("patient", "clinical", "diagnostic", "medical",
                               "healthcare", "laboratory", "radiology", "ehr",
                               "hl7", "hipaa"),
    "education": ("student", "school", "university", "course", "curriculum",
                  "transcript", "edtech", "learning management", "gradebook"),
    "finance_investment": ("invoice", "accounting", "financial", "investment",
                           "portfolio", "banking", "fintech", "ledger",
                           "bookkeeping", "insurance"),
    "proposal_sales": ("proposal", "rfp", "quotation", "quote", "sales enablement",
                       "pitch", "tender", "bid"),
    "events_weddings": ("wedding", "event management", "venue", "catering",
                        "itinerary", "guest list"),
    "software_technical_docs": ("api documentation", "technical documentation",
                                "developer portal", "docs site", "changelog",
                                "sdk", "openapi", "swagger"),
}

#: Pipeline stages that can actually be observed from what this stage fetches.
#: Deliberately short. A stage nobody saw evidence for is not counted, however
#: plausible it is that the repository performs it.
STAGE_TEMPLATE_POPULATION = "template_population"
STAGE_DOCUMENT_GENERATION = "document_generation"
STAGE_FORMAT_CONVERSION = "format_conversion"


class EvidenceError(Exception):
    """Evidence collection failed for one candidate."""


# --- results ---------------------------------------------------------------


@dataclass
class EvidenceOutcome:
    """What collecting evidence for one candidate produced."""

    candidate_id: str
    repo_full_name: str = ""
    ok: bool = False
    error: str | None = None
    dependencies_recorded: int = 0
    evidence_entries: int = 0
    code_usage_confirmed: bool = False
    notes: list[str] = field(default_factory=list)


@dataclass
class _Gathered:
    """Raw material fetched for one candidate, before anything is derived."""

    metadata: object | None = None
    readme_text: str = ""
    readme_url: str = ""
    root_entries: tuple = ()
    sub_listings: dict = field(default_factory=dict)   # dir path -> entries
    manifests: dict = field(default_factory=dict)      # filename -> FileContents
    infra_files: dict = field(default_factory=dict)    # filename -> FileContents
    # Schema 3: infrastructure files opened at the exact path a discovery hit
    # matched, which may sit anywhere in the tree. Keyed by full path.
    discovered_infra_files: dict = field(default_factory=dict)
    code_hits: list = field(default_factory=list)      # CodeSearchResult
    missing: list[str] = field(default_factory=list)



def _wired_reference(text: str, service: str) -> bool:
    """Whether a line references a service as something being *called*.

    Requires the service name next to a URL, host, port or configuration key,
    so a passing mention in a comment or a package name does not qualify.
    """
    if service not in text:
        return False
    return bool(
        re.search(
            r"(https?://[\w.\-]*" + re.escape(service) + r"|"
            + re.escape(service) + r"[\w.\-]*:\d{2,5}|"
            + r"[\w_]*" + re.escape(service) + r"[\w_]*_(url|host|port|endpoint|uri)|"
            + r"(url|host|port|endpoint|uri)[\w_]*[\s=:\"']+[\w.\-/:]*"
            + re.escape(service) + r")",
            text,
            re.IGNORECASE,
        )
    )


# --- text helpers ----------------------------------------------------------


def _sentences(text: str) -> list[str]:
    """Split prose into sentences, skipping markdown furniture."""
    cleaned: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", ">", "|", "```", "---", "===")):
            continue
        if re.match(r"^[\-\*\+]\s", stripped) or re.match(r"^\d+\.\s", stripped):
            stripped = stripped[2:].strip()
        # Drop badge-only lines.
        if stripped.startswith("[!["):
            continue
        cleaned.append(stripped)
    joined = " ".join(cleaned)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", joined) if s.strip()]


def detect_product_description(readme: str) -> tuple[bool, str]:
    """Does the README say what this does for a user, and which sentence says so?

    CANDIDATE_SCHEMA.md section 6 allows `readme_describes_product` to be true
    only alongside a quoted excerpt, and the database enforces that. So the
    excerpt is not a nicety here: without one the claim cannot be recorded at
    all, which is the intended pressure.
    """
    for sentence in _sentences(readme)[:40]:
        lowered = sentence.lower()
        if any(phrase in lowered for phrase in PRODUCT_PHRASES):
            if 20 <= len(sentence) <= 400:
                return True, sentence
    return False, ""


#: Tokens that mark a name as an organization rather than a person. A name
#: carrying one of these is safe to store even if it otherwise looks like two
#: capitalised words.
ORGANISATION_MARKERS = frozenset({
    "inc", "inc.", "llc", "l.l.c.", "ltd", "ltd.", "limited", "gmbh", "b.v.",
    "bv", "s.a.", "sa", "sas", "pty", "corp", "corp.", "corporation", "company",
    "co", "co.", "holdings", "group", "labs", "lab", "technologies", "technology",
    "tech", "software", "systems", "solutions", "services", "consulting",
    "studio", "studios", "digital", "media", "networks", "foundation",
    "institute", "university", "college", "school", "association", "society",
    "trust", "council", "committee", "agency", "department", "ministry",
    "hospital", "clinic", "bank", "insurance", "partners", "ventures",
    "capital", "industries", "enterprises", "international", "global",
    "worldwide", "team", "project", "community", "collective", "cooperative",
    "association", "org", "pbc", "plc", "ag", "oy", "ab", "as", "nv", "kk",
    "srl", "spa", "sarl", "ug", "kft", "doo", "dev", "io", "ai", "app",
})

#: Personal-name honorifics and generational suffixes. Their presence is a
#: strong signal that the match is an individual.
PERSON_MARKERS = frozenset({
    "mr", "mr.", "mrs", "mrs.", "ms", "ms.", "dr", "dr.", "prof", "prof.",
    "jr", "jr.", "sr", "sr.", "phd", "ph.d.", "md", "esq",
})


def looks_like_person(name: str) -> bool:
    """Whether a captured name reads as an individual rather than a body.

    The task brief is explicit that real companies may appear anywhere in this
    repository and real people may not, so this decides what is safe to store.
    It is deliberately biased toward *not* storing: a missed company is a blank
    field a human can fill, while a stored personal name is a rule violation
    that ships in an artefact.

    An organisation marker anywhere in the name settles it as an organisation.
    Failing that, two or three capitalised words with no marker at all is the
    shape of a personal name (two or three bare given/family words), and is refused.
    """
    tokens = [tok for tok in name.replace(",", " ").split() if tok]
    if not tokens:
        return False

    lowered = {tok.lower().strip(".,") for tok in tokens}
    lowered_with_dots = {tok.lower() for tok in tokens}

    if lowered & PERSON_MARKERS or lowered_with_dots & PERSON_MARKERS:
        return True
    if lowered & ORGANISATION_MARKERS or lowered_with_dots & ORGANISATION_MARKERS:
        return False

    # A domain, a slug, an ampersand or a digit is corporate shorthand, not a
    # person: "Kartoza.com", "P&G", "302 AI". A hyphen is deliberately not in
    # that set - it is ordinary inside a given name ("Jean-Luc" style),
    # and treating it as corporate would store exactly the names this guard
    # exists to keep out.
    if any(ch in name for ch in ".&/_") or any(ch.isdigit() for ch in name):
        return False
    # A single word is a brand as often as a surname; too weak to refuse on.
    if len(tokens) < 2:
        return False
    # An internally capitalised word is a brand, not a surname: "BigBear".
    # Hyphenated parts are judged separately so a hyphenated given name stays one.
    for token in tokens:
        for part in token.split("-"):
            if len(part) > 1 and part[1:] != part[1:].lower():
                return False

    return 2 <= len(tokens) <= 3 and all(tok[:1].isupper() for tok in tokens)


def _trim_at_sentence_break(name: str) -> str:
    """Cut a captured name at a sentence boundary it should not have crossed.

    "Inc.", "Ltd." and friends keep their period; anything else followed by a
    space and another word is the start of the next sentence.
    """
    match = re.search(r"\.\s+\S", name)
    if not match:
        return name
    head = name[: match.start() + 1]
    if re.search(r"(Inc|LLC|Ltd|Corp|Co|S\.A|B\.V|Pty|GmbH)\.$", head):
        rest = name[match.start() + 1 :].strip()
        return (head + " " + rest).strip() if rest else head
    return head.rstrip(".").strip()



def detect_company_name(readme: str) -> tuple[str | None, str | None]:
    """Find a company only where the repository states one.

    Returns (name, source) or (None, None). Deliberately narrow: it reads
    copyright lines and explicit attribution, and nothing else. Inferring a
    company from a domain name or a GitHub org slug would be a guess, and
    CANDIDATE_SCHEMA.md section 2 says this field is never guessed. A human
    resolves the rest, which is what `external_search` exists for.

    A match that reads as an individual is discarded rather than stored. Most
    open-source copyright lines name a person, and the task brief allows real
    companies to appear anywhere in this repository while real people may not.
    An unidentified organisation is therefore left null, which is also the
    honest answer: nobody established one.
    """
    # Case classes are spelled out rather than using IGNORECASE, because the
    # capture groups rely on a leading capital to tell a name from prose.
    patterns = (
        (r"(?:©|\(c\)|\(C\)|[Cc]opyright)\s*(?:\d{4}(?:\s*[-–]\s*\d{4})?)?\s*,?\s*"
         r"(?:by\s+)?([A-Z][\w&.\-]*(?:\s+[A-Z][\w&.\-]*){0,3}"
         r"(?:\s+(?:Inc|LLC|Ltd|GmbH|B\.V\.|S\.A\.|Pty|Limited|Corp)\.?)?)", "readme"),
        (r"(?:[Bb]uilt|[Mm]ade|[Mm]aintained|[Dd]eveloped|[Cc]reated)\s+by\s+"
         r"\[?([A-Z][\w&.\-]*(?:\s+[A-Z][\w&.\-]*){0,3})\]?", "readme"),
        (r"[Aa]\s+product\s+(?:of|by)\s+([A-Z][\w&.\-]*(?:\s+[A-Z][\w&.\-]*){0,3})",
         "readme"),
    )
    for pattern, source in patterns:
        match = re.search(pattern, readme)
        if match:
            name = match.group(1).strip().rstrip(",-").strip()
            # A greedy match can run past the end of the name and swallow the
            # next sentence (a name followed by ". All rights..."). Cut at the first period that
            # is not part of a legal form, so what follows is judged on the
            # name itself rather than on the punctuation it dragged in.
            name = _trim_at_sentence_break(name)
            # Keep the period in "Inc." and friends; strip a trailing sentence
            # period otherwise. Stripping unconditionally silently renames a
            # company.
            if name.endswith(".") and not re.search(
                r"\b(Inc|LLC|Ltd|Corp|Co|S\.A|B\.V|Pty)\.$", name
            ):
                name = name[:-1].strip()
            # Reject obvious non-companies picked up by a greedy match.
            if looks_like_person(name):
                # An individual, not an organisation. Leave the field null.
                continue
            if name and len(name) > 2 and name.lower() not in {
                "the", "all rights reserved", "me", "us", "copyright",
                "text", "notice", "engineers", "author", "authors",
                "contributors", "license", "licensed", "rights",
            }:
                return name, source
    return None, None


def detect_industry_category(readme: str, description: str = "") -> str:
    """Best-supported category, or `unknown`.

    A tie between two categories resolves to unknown rather than to whichever
    happened to sort first: a coin-flip recorded as a finding is worse than an
    honest absence.
    """
    # Whitespace is collapsed first. READMEs wrap at 80 columns, so a
    # two-word keyword like "property management" is routinely split across a
    # newline; matching the raw text would miss every wrapped phrase.
    haystack = re.sub(r"\s+", " ", f"{description}\n{readme}").lower()
    # Word boundaries matter more than they look. A bare substring match reads
    # "clause" inside a product called ClauseForge and files a lease-agreement
    # product under legal_contracts, on the strength of its own brand name.
    scores = {
        category: sum(
            1 for word in words
            # A trailing "s?" so "property manager" matches "property managers"
            # and "lease" matches "leases", without matching a longer word.
            if re.search(rf"\b{re.escape(word)}s?\b", haystack)
        )
        for category, words in INDUSTRY_KEYWORDS.items()
    }
    best = max(scores.values(), default=0)
    if best == 0:
        return "unknown"
    leaders = [c for c, s in scores.items() if s == best]
    return leaders[0] if len(leaders) == 1 else "unknown"


def manifest_kind(path: str) -> str | None:
    """Which manifest a path represents, or None if it isn't one.

    Recognises a manifest by convention rather than by exact root-level name.
    The live run found `sambanova/ai-starter-kit` keeping its dependencies in
    `base-requirements.txt` and
    `utils/parsing/unstructured-api/requirements/base.txt`, and recorded zero
    dependency evidence as a result. A blank record reads as absence of usage
    to anything downstream, which is a false negative rather than an honest gap.

    Deliberately not "any .txt is a manifest". A text file only counts when its
    name follows the requirements convention, or when it sits directly inside a
    directory named `requirements`.
    """
    parts = [p for p in path.replace("\\", "/").split("/") if p]
    if not parts:
        return None
    basename = parts[-1]
    parent = parts[-2].lower() if len(parts) >= 2 else ""
    lowered = basename.lower()

    if lowered in MANIFEST_BASENAMES:
        return lowered
    if lowered.endswith(".csproj"):
        return "*.csproj"

    # requirements-dev.txt, base-requirements.txt, requirements_test.txt
    if lowered.endswith(".txt"):
        if lowered.endswith(("-requirements.txt", "_requirements.txt")):
            return "requirements.txt"
        if re.fullmatch(r"requirements[-_.].+\.txt", lowered):
            return "requirements.txt"
        # requirements/base.txt, requirements/dev.txt
        if parent == "requirements":
            return "requirements.txt"
    return None


def is_source_file(path: str) -> bool:
    """True when a path is executable source rather than a manifest or document.

    Used to decide whether a code-search hit counts as a call site. See
    SOURCE_EXTENSIONS for why this matters more than it looks.
    """
    _, _, extension = path.rpartition(".")
    return bool(extension) and extension.lower() in SOURCE_EXTENSIONS


def is_production_path(path: str) -> bool:
    """True when a path looks like application code rather than a demonstration."""
    head = path.split("/")[0].lower() if "/" in path else ""
    return head not in NON_PRODUCTION_PREFIXES


def find_readme(entries: Iterable) -> object | None:
    for entry in entries:
        if not entry.is_dir and entry.name.lower() in README_NAMES:
            return entry
    return None


# --- the collector ---------------------------------------------------------


class EvidenceCollector:
    """Fills in a candidate's evidence from public repository data.

    Every call goes through GitHubClient, so pacing, retries, backoff and
    caching are the reliability layer's concern and cannot be bypassed from
    here.
    """

    def __init__(
        self,
        connection,
        client: GitHubClient,
        universe: LibraryUniverse,
        *,
        max_code_searches: int = 2,
        max_discovered_files: int = 3,
    ) -> None:
        self._conn = connection
        self._client = client
        self._universe = universe
        self._max_code_searches = max_code_searches
        self._max_discovered_files = max_discovered_files

    # -- public ------------------------------------------------------------

    def pending(self) -> list[str]:
        """Candidates with a discovery hit but no evidence yet."""
        return storage.candidates_needing_evidence(self._conn)

    def collect(self, candidate_id: str) -> EvidenceOutcome:
        candidate = storage.get_candidate(self._conn, candidate_id)
        if candidate is None:
            raise EvidenceError(f"No candidate {candidate_id!r}")

        owner, repo = candidate["repo_owner"], candidate["repo_name"]
        outcome = EvidenceOutcome(
            candidate_id=candidate_id, repo_full_name=f"{owner}/{repo}"
        )

        gathered = self._gather(owner, repo, candidate_id, outcome)
        self._record_identity(candidate_id, gathered, outcome)
        dependencies = self._record_dependencies(candidate_id, gathered, outcome)
        self._record_pipeline(candidate_id, gathered, dependencies, outcome)
        self._record_business(candidate_id, gathered, dependencies, outcome)

        outcome.ok = True
        return outcome

    # -- gathering ---------------------------------------------------------

    def _gather(self, owner, repo, candidate_id, outcome) -> _Gathered:
        """Fetch the small, targeted set of files this stage needs."""
        gathered = _Gathered()

        gathered.metadata = self._client.get_repository(owner, repo)
        self._trail(candidate_id, gathered.metadata.repo_url, "api_response",
                    f"stars={gathered.metadata.stars}, "
                    f"fork={gathered.metadata.is_fork}, "
                    f"archived={gathered.metadata.is_archived}", "github_api", outcome)

        # One listing answers several questions at once, from the cheap budget.
        try:
            gathered.root_entries = self._client.list_directory(owner, repo)
        except (ApiError, RetriesExhausted) as exc:
            gathered.missing.append(f"root listing unavailable ({exc})")

        readme_entry = find_readme(gathered.root_entries)
        if readme_entry is not None:
            try:
                contents = self._client.get_file_contents(
                    owner, repo, readme_entry.path
                )
                gathered.readme_text = contents.text
                gathered.readme_url = contents.evidence_url
            except (ApiError, RetriesExhausted) as exc:
                gathered.missing.append(f"README unavailable ({exc})")
        else:
            gathered.missing.append("no README found at repository root")

        self._fetch_manifests(owner, repo, gathered)

        root_names = {e.name.lower(): e for e in gathered.root_entries if not e.is_dir}
        for name in INFRASTRUCTURE_FILES:
            entry = root_names.get(name)
            if entry is None:
                continue
            try:
                gathered.infra_files[entry.name] = self._client.get_file_contents(
                    owner, repo, entry.path
                )
            except (ApiError, RetriesExhausted) as exc:
                gathered.missing.append(f"{entry.name} unavailable ({exc})")

        self._fetch_discovered_infrastructure(
            owner, repo, candidate_id, gathered, outcome)
        self._inspect_workspaces(owner, repo, gathered)
        gathered.code_hits = self._search_code_usage(owner, repo, candidate_id, outcome)
        return gathered

    def _fetch_discovered_infrastructure(self, owner, repo, candidate_id,
                                         gathered, outcome) -> None:
        """Open the exact infrastructure files discovery matched.

        Run 1 could not do this: the matched path was never stored, so the
        collector fell back to the repository root and missed every nested
        compose file. Schema 3 keeps the path, and 39 percent of run 1's
        recovered paths were not at the root.

        Bounded on purpose - only paths a query already matched, capped - and
        it never lists or walks a directory looking for more.
        """
        rows = storage.discovery_paths_for_candidate(self._conn, candidate_id)
        wanted = [
            row for row in rows
            if row["file_path"]
            and row["file_path"].rsplit("/", 1)[-1].lower() in NESTED_INFRASTRUCTURE_NAMES
        ][: self._max_discovered_files]

        for row in wanted:
            path = row["file_path"]
            if path in gathered.discovered_infra_files:
                continue
            try:
                contents = self._client.get_file_contents(owner, repo, path)
            except (ApiError, RetriesExhausted) as exc:
                # A path we cannot read is not evidence. Claiming the reference
                # anyway would assert something never seen.
                gathered.missing.append(f"{path} unavailable ({exc})")
                continue
            gathered.discovered_infra_files[path] = contents
            self._trail(candidate_id, contents.evidence_url or row["evidence_url"],
                        "code_permalink",
                        (contents.text or "")[:200], "github_api", outcome)


    def _inspect_workspaces(self, owner, repo, gathered: _Gathered) -> None:
        """Look inside a monorepo container, but only when it would decide.

        Skipped entirely when the root already shows a plain application
        directory, so the extra call is spent only on repositories where the
        answer actually hinges on it. At most one listing.
        """
        root_dirs = {e.name.lower() for e in gathered.root_entries if e.is_dir}
        if root_dirs & APPLICATION_DIRECTORIES:
            return

        for entry in gathered.root_entries:
            name = entry.name.lower()
            if not entry.is_dir or name not in WORKSPACE_DIRECTORIES:
                continue
            if name in gathered.sub_listings:
                return
            try:
                gathered.sub_listings[name] = self._client.list_directory(
                    owner, repo, entry.path
                )
            except (ApiError, RetriesExhausted) as exc:
                gathered.missing.append(f"{entry.name}/ listing unavailable ({exc})")
            return

    def _fetch_manifests(self, owner, repo, gathered: _Gathered) -> None:
        """Locate manifests at the root, then in a few likely directories.

        Bounded by design: one listing of the root, and at most
        MAX_MANIFEST_DIR_LISTINGS listings of directories that exist there and
        are named as somewhere a manifest plausibly lives. Deeper manifests are
        still reached, but through the code-search results the collector
        already has rather than by walking the tree.
        """
        candidates: list = [
            e for e in gathered.root_entries
            if not e.is_dir and manifest_kind(e.path)
        ]

        listed = 0
        for directory in LIKELY_MANIFEST_DIRS:
            if listed >= MAX_MANIFEST_DIR_LISTINGS:
                break
            match = next(
                (e for e in gathered.root_entries
                 if e.is_dir and e.name.lower() == directory),
                None,
            )
            if match is None:
                continue
            listed += 1
            try:
                children = self._client.list_directory(owner, repo, match.path)
                gathered.sub_listings[match.name.lower()] = children
                for child in children:
                    if not child.is_dir and manifest_kind(child.path):
                        candidates.append(child)
            except (ApiError, RetriesExhausted) as exc:
                gathered.missing.append(f"{match.name}/ listing unavailable ({exc})")

        for item in candidates:
            if item.path in gathered.manifests:
                continue
            try:
                gathered.manifests[item.path] = self._client.get_file_contents(
                    owner, repo, item.path
                )
            except (ApiError, RetriesExhausted) as exc:
                gathered.missing.append(f"{item.path} unavailable ({exc})")

    def _entries_for(self, candidate_id: str) -> list[LibraryEntry]:
        entries: list[LibraryEntry] = []
        for name in storage.libraries_that_surfaced_candidate(self._conn, candidate_id):
            try:
                entries.append(self._universe.by_name(name))
            except KeyError:
                logger.warning("library %r is not in the universe", name)
        return entries

    def _search_code_usage(self, owner, repo, candidate_id, outcome) -> list:
        """Look for the library actually being imported, scoped to this repo.

        A manifest line proves a dependency was declared, not that anything
        calls it. This is the one place the collector spends code-search
        budget, so it is capped and scoped with `repo:` rather than run per
        library across all of GitHub.
        """
        hits: list = []
        for entry in self._entries_for(candidate_id)[: self._max_code_searches]:
            token = entry.package_names[0] if entry.package_names else entry.library_name
            query = f'repo:{owner}/{repo} "{token}"'
            try:
                page = self._client.search_code(query, per_page=5)
            except (ApiError, RetriesExhausted) as exc:
                outcome.notes.append(f"code search failed for {token}: {exc}")
                continue
            for result in page.results:
                hits.append((entry, result))
        return hits

    # -- recording ---------------------------------------------------------

    def _record_identity(self, candidate_id, gathered: _Gathered, outcome) -> None:
        metadata = gathered.metadata
        readme = gathered.readme_text

        company, company_source = detect_company_name(readme)
        website = metadata.homepage or self._website_from_readme(readme)
        category = detect_industry_category(readme, metadata.description)

        fields = {
            "is_fork": metadata.is_fork,
            "is_archived": metadata.is_archived,
            "primary_language": metadata.primary_language,
            "website_url": website,
            "industry_category": category,
        }
        if company:
            fields["company_name"] = company
            fields["company_name_source"] = company_source
            self._trail(candidate_id, gathered.readme_url or metadata.repo_url,
                        "readme_excerpt", f"company stated as {company!r}",
                        "readme", outcome)
        else:
            outcome.notes.append("company_name not stated in the repository")

        product = self._product_name(readme, metadata)
        if product:
            fields["product_name"] = product

        storage.update_candidate_identity(self._conn, candidate_id, **fields)

    def _website_from_readme(self, readme: str) -> str | None:
        """Deliberately returns nothing.

        An earlier version took the first non-GitHub URL in the README. Run
        against real repositories that attributed a PDF-parsing library's
        website to a blog that had merely written about it. The first link in a
        README is as often a badge target, a dependency, or an article as it is
        the project's own site, so this was inventing an identity rather than
        recording one.

        `website_url` now comes only from the repository's declared homepage,
        which the owner set deliberately. Recovering a website from README prose
        is left to a human, alongside resolving company_name.
        """
        return None

    def _product_name(self, readme: str, metadata) -> str | None:
        """The first heading, when the README opens with one."""
        for line in readme.splitlines()[:10]:
            if line.startswith("# "):
                name = line[2:].strip()
                if 2 < len(name) <= 80:
                    return name
        return None

    def _record_dependencies(self, candidate_id, gathered: _Gathered, outcome) -> list:
        """One row per library located, tagged by how it was found."""
        recorded: list[dict] = []

        for entry in self._entries_for(candidate_id):
            found_for_entry = False

            for path, contents in gathered.manifests.items():
                if not self._declares(entry, contents.text):
                    continue
                found_for_entry = True
                recorded.append(self._save_dependency(
                    candidate_id, entry, "manifest_declaration",
                    contents.evidence_url, path, outcome,
                    excerpt=self._matching_line(entry, contents.text),
                ))

            # Root-level infrastructure files, and the exact files a discovery
            # hit matched anywhere in the tree. The second source is what run 1
            # lacked: the compose file naming the service often sits several
            # directories down, so a root-only scan found nothing to record.
            infra_sources = list(gathered.infra_files.items()) + list(
                gathered.discovered_infra_files.items()
            )
            for filename, contents in infra_sources:
                if not self._infrastructure_match(entry, contents.text):
                    continue
                found_for_entry = True
                recorded.append(self._save_dependency(
                    candidate_id, entry, "infrastructure_reference",
                    contents.evidence_url, filename if "/" in filename else None,
                    outcome,
                    excerpt=self._matching_line(entry, contents.text),
                ))

            # Code-search hits are routed by what kind of file they landed in.
            # The search matches text anywhere in the repository, so the same
            # result set contains genuine call sites, manifests nested too deep
            # to have been listed, and noise like READMEs and CI config. Each
            # needs a different answer, and conflating them is what made
            # code_usage_confirmed dishonest in the first place.
            for hit_entry, result in gathered.code_hits:
                if hit_entry.library_name != entry.library_name:
                    continue
                if result.path in gathered.manifests:
                    continue  # already recorded from the fetched file

                if is_source_file(result.path):
                    found_for_entry = True
                    recorded.append(self._save_dependency(
                        candidate_id, entry, "code_import",
                        result.evidence_url, None, outcome,
                        excerpt=result.excerpt or result.path, path=result.path,
                    ))
                elif manifest_kind(result.path):
                    # A manifest the listing never reached. The search already
                    # matched the package name inside it, so the declaration is
                    # evidenced without spending another call fetching it.
                    found_for_entry = True
                    recorded.append(self._save_dependency(
                        candidate_id, entry, "manifest_declaration",
                        result.evidence_url, result.path, outcome,
                        excerpt=result.excerpt or result.path,
                    ))
                # Anything else, a README, a lockfile, a CI config, is not
                # evidence of either declaration or use, and is dropped.

            if not found_for_entry:
                outcome.notes.append(
                    f"{entry.library_name}: surfaced by discovery but no evidence "
                    f"located in the manifest, infrastructure files or code sample"
                )

        return [r for r in recorded if r]

    def _declares(self, entry: LibraryEntry, text: str) -> bool:
        lowered = text.lower()
        return any(package.lower() in lowered for package in entry.package_names)

    def _infrastructure_match(self, entry: LibraryEntry, text: str) -> bool:
        lowered = text.lower()
        return any(p.pattern.lower() in lowered for p in entry.infrastructure_patterns)

    def _matching_line(self, entry: LibraryEntry, text: str) -> str:
        for line in text.splitlines():
            if any(p.lower() in line.lower() for p in entry.package_names):
                return line.strip()[:200]
        return ""

    def _save_dependency(
        self, candidate_id, entry, detection_method, evidence_url,
        manifest_file, outcome, *, excerpt="", path="",
    ) -> dict | None:
        if not evidence_url:
            return None
        inserted = storage.insert_dependency_found(
            self._conn,
            candidate_id=candidate_id,
            library_name=entry.library_name,
            library_category=entry.category,
            direction=entry.direction,
            detection_method=detection_method,
            evidence_url=evidence_url,
            manifest_file=manifest_file,
        )
        if inserted is not None:
            outcome.dependencies_recorded += 1
        self._trail(
            candidate_id, evidence_url,
            "manifest_line" if manifest_file else "code_permalink",
            excerpt, "github_api", outcome,
        )
        return {
            "entry": entry,
            "detection_method": detection_method,
            "path": path or (manifest_file or ""),
            "evidence_url": evidence_url,
        }

    def _record_pipeline(self, candidate_id, gathered, dependencies, outcome) -> None:
        confirmed = [
            d for d in dependencies
            if d["detection_method"] in ("code_import", "infrastructure_reference")
        ]
        code_usage_confirmed = bool(confirmed)
        outcome.code_usage_confirmed = code_usage_confirmed

        template_dir = [
            e for e in gathered.root_entries
            if e.is_dir and e.name.lower() in TEMPLATE_DIRECTORIES
        ]
        infrastructure = any(
            d["detection_method"] == "infrastructure_reference" for d in dependencies
        )
        # A reference is "we found the file naming this service". Use is
        # "and something here actually calls it". Run 1 had one flag for both,
        # so a catalogue listing hundreds of other people's compose files
        # looked identical to a company running one.
        reference_present = bool(
            infrastructure or gathered.discovered_infra_files or gathered.infra_files
        )
        infrastructure_used = infrastructure and self._infrastructure_is_used(
            gathered, dependencies
        )
        categories = {d["entry"].category for d in confirmed}

        stages = self._observed_stages(confirmed, template_dir, infrastructure_used)
        notes = self._pipeline_notes(
            gathered, dependencies, confirmed, stages, template_dir
        )

        storage.upsert_pipeline_evidence(
            self._conn,
            candidate_id=candidate_id,
            code_usage_confirmed=code_usage_confirmed,
            template_directory_present=bool(template_dir),
            multiple_document_types_handled=len(categories) >= 2,
            pipeline_stage_count=len(stages),
            infrastructure_service_present=infrastructure_used,
            infrastructure_reference_present=reference_present,
            pipeline_evidence_notes=notes,
        )
        if template_dir:
            self._trail(candidate_id, template_dir[0].html_url, "other",
                        f"directory {template_dir[0].name}/ present",
                        "github_api", outcome)

    def _infrastructure_is_used(self, gathered, dependencies) -> bool:
        """Whether application code is evidenced to actually call the service.

        A compose file proves a service is *declared*. It says nothing about
        whether anything in this repository talks to it - a self-hosting
        catalogue declares hundreds of services it never calls. The earlier
        version of this check accepted "a compose file exists and there is some
        application code somewhere", which is co-presence, not use, and it is
        why catalogue repositories read as though they ran a document pipeline.

        Only two things count here, both of which are direct:

        1. The service name appears in an actual source file. `code_import`
           rows are only written when the hit landed in a source file, so such
           a row for an entry that also has infrastructure patterns means the
           application references the service by name in its own code.
        2. The service's URL, host or configuration key appears in a source
           file - the service being wired into the application rather than
           merely deployed alongside it.

        When neither holds, this returns False and the reference is still
        recorded on its own column. Nothing is lost; it is filed as what was
        actually seen.
        """
        infra_entries = {
            d["entry"].library_name
            for d in dependencies
            if d["detection_method"] == "infrastructure_reference"
            and getattr(d["entry"], "infrastructure_patterns", ())
        }
        if not infra_entries:
            return False

        # 1. the service named in the application's own source
        for dependency in dependencies:
            if (
                dependency["detection_method"] == "code_import"
                and dependency["entry"].library_name in infra_entries
            ):
                return True

        # 2. the service wired into the application by URL or configuration
        return self._service_wiring_in_source(gathered, dependencies, infra_entries)

    def _service_wiring_in_source(self, gathered, dependencies, infra_entries) -> bool:
        """A source file referencing the service by URL, host or config key.

        Deliberately narrow. It looks only at source files already fetched or
        already matched by a search, never at the compose file itself: a
        service defining its own hostname proves nothing about the caller.
        """
        patterns: list[str] = []
        for dependency in dependencies:
            entry = dependency["entry"]
            if entry.library_name not in infra_entries:
                continue
            for pattern in getattr(entry, "infrastructure_patterns", ()):
                token = (pattern.pattern or "").lower().strip()
                if token:
                    # "gotenberg/gotenberg" wires up as a host called gotenberg
                    patterns.append(token.split("/")[-1])

        if not patterns:
            return False

        for hit_entry, result in gathered.code_hits:
            if not is_source_file(result.path):
                continue
            haystack = f"{result.excerpt or ''}".lower()
            if any(_wired_reference(haystack, token) for token in patterns):
                return True
        return False

    def _observed_stages(self, confirmed, template_dir, infrastructure) -> set[str]:
        """Only stages something was actually seen for.

        CANDIDATE_SCHEMA.md section 5 requires each counted stage to have its
        own evidence, and says stages that are assumed rather than seen do not
        count. A repository almost certainly retrieves source data before
        generating a document, but nothing fetched here observes that, so it is
        not counted.
        """
        stages: set[str] = set()
        for dependency in confirmed:
            entry = dependency["entry"]
            if entry.category == "template_generation" or template_dir:
                stages.add(STAGE_TEMPLATE_POPULATION)
            if entry.direction == "generation":
                stages.add(STAGE_DOCUMENT_GENERATION)
            if entry.direction in ("conversion", "mixed"):
                stages.add(STAGE_FORMAT_CONVERSION)
        if infrastructure:
            stages.add(STAGE_FORMAT_CONVERSION)
        return stages

    def _pipeline_notes(self, gathered, dependencies, confirmed, stages, template_dir):
        parts: list[str] = []
        if stages:
            parts.append("stages observed: " + ", ".join(sorted(stages)))
        else:
            parts.append("no pipeline stage observed in the evidence collected")
        manifest_only = [
            d["entry"].library_name for d in dependencies
            if d["detection_method"] == "manifest_declaration"
        ]
        if manifest_only and not confirmed:
            parts.append(
                "every hit was manifest-only; no call site was located, so the "
                "scope of any pipeline is unconfirmed"
            )
        if template_dir:
            parts.append(f"template directory: {template_dir[0].name}/")
        if gathered.missing:
            parts.append("not retrieved: " + "; ".join(gathered.missing[:3]))
        return " | ".join(parts)[:1000]

    def _record_business(self, candidate_id, gathered, dependencies, outcome) -> None:
        metadata = gathered.metadata
        describes, excerpt = detect_product_description(gathered.readme_text)

        application_code = self._application_code_exists(
            gathered.root_entries, gathered.sub_listings
        )
        # Only actual call sites count. CANDIDATE_SCHEMA.md section 6 asks
        # whether the document *code* lives in the application's main path, and
        # a requirements.txt at the repository root is a production path in the
        # trivial sense while proving nothing about where the code runs.
        call_sites = [
            d for d in dependencies
            if d["detection_method"] in ("code_import", "infrastructure_reference")
            and d["path"]
        ]
        in_production = any(is_production_path(d["path"]) for d in call_sites)
        website = metadata.homepage or self._website_from_readme(gathered.readme_text)

        notes: list[str] = []
        if not describes and gathered.readme_text:
            notes.append(
                "README present but no sentence found describing what the "
                "software does for a customer or user"
            )
        if not gathered.readme_text:
            notes.append("no README retrieved")
        if dependencies and not in_production:
            notes.append(
                "all document-library evidence sits outside production paths"
            )
        notes.extend(outcome.notes[:3])

        storage.upsert_business_evidence(
            self._conn,
            candidate_id=candidate_id,
            readme_describes_product=describes,
            readme_excerpt=excerpt or None,
            website_exists=bool(website),
            application_code_exists=application_code,
            document_functionality_in_production_code=in_production,
            stars=metadata.stars,
            last_commit_date=metadata.last_commit_date,
            contributor_count=None,
            **self._repository_purpose(gathered),
            business_evidence_notes=" | ".join(notes)[:1000] or None,
        )
        if describes:
            self._trail(candidate_id, gathered.readme_url, "readme_excerpt",
                        excerpt, "readme", outcome)

    def _repository_purpose(self, gathered) -> dict:
        """Structured evidence about what this repository is *for*.

        Three deterministic signals, no classifier and no scoring. They are
        recorded so a later phase can weigh them; qualification does not read
        them yet, and a signal that cannot be assessed stays null rather than
        becoming a false.
        """
        text = gathered.readme_text or ""
        description = getattr(gathered.metadata, "description", "") or ""
        haystack = f"{description}\n{text}"

        directories = {e.name.lower() for e in gathered.root_entries if e.is_dir}
        has_examples = bool(directories & EXAMPLE_DIRECTORIES) if gathered.root_entries else None

        return {
            "is_catalogue_repository": (
                bool(_PURPOSE_CATALOGUE.search(haystack)) if haystack.strip() else None
            ),
            "readme_indicates_example_or_tutorial": (
                bool(_PURPOSE_EXAMPLE.search(text)) if text.strip() else None
            ),
            "has_examples_directory": has_examples,
        }


    def _application_code_exists(self, entries, sub_listings=None) -> bool:
        """A real application, rather than a handful of demonstration scripts."""
        if not entries:
            return False
        directories = {e.name.lower() for e in entries if e.is_dir}
        if directories & APPLICATION_DIRECTORIES:
            return True

        if self._workspace_holds_an_application(directories, sub_listings or {}):
            return True

        source_files = [
            e for e in entries
            if not e.is_dir and e.name.rsplit(".", 1)[-1].lower() in
            {"py", "js", "ts", "java", "cs", "go", "rb", "php", "tsx", "jsx"}
        ]
        return len(source_files) >= 3

    def _workspace_holds_an_application(self, directories, sub_listings) -> bool:
        """Does a monorepo container hold something other than documentation?

        Requires the listing. Presence of `packages/` alone proves nothing, and
        a workspace whose only member is a docs site is not an application.
        Where the listing could not be fetched the answer is no, which keeps
        an unverified guess out of the record.
        """
        for name in directories & WORKSPACE_DIRECTORIES:
            members = sub_listings.get(name)
            if not members:
                continue
            if any(
                member.is_dir and member.name.lower() not in NON_APPLICATION_MEMBERS
                for member in members
            ):
                return True
        return False

    def _trail(self, candidate_id, url, evidence_type, excerpt, source, outcome):
        """Record one evidence entry, keeping the excerpt short.

        CANDIDATE_SCHEMA.md section 9 asks for the specific text being cited,
        kept short. Storing whole files would make the trail unreadable and the
        database large without making any claim more checkable.
        """
        if not url:
            return
        storage.insert_evidence_trail(
            self._conn,
            candidate_id=candidate_id,
            evidence_url=url,
            evidence_type=evidence_type,
            evidence_excerpt=(excerpt or "")[:300] or None,
            source=source,
        )
        outcome.evidence_entries += 1


# --- batch -----------------------------------------------------------------


def collect_for_candidates(
    collector: EvidenceCollector, candidate_ids: Sequence[str]
) -> list[EvidenceOutcome]:
    """Collect for each candidate, continuing past individual failures.

    A single candidate failing marks just that candidate's evidence missing and
    moves on, per TECHNICAL_DESIGN.md section 15. A systemic failure, meaning a
    rate limit that cannot be waited out, stops the batch instead of burning
    the remaining candidates producing nothing.
    """
    outcomes: list[EvidenceOutcome] = []
    for candidate_id in candidate_ids:
        try:
            outcomes.append(collector.collect(candidate_id))
        except RateLimited:
            raise
        except (ApiError, RetriesExhausted, ReliabilityError, EvidenceError) as exc:
            logger.warning("evidence failed for %s: %s", candidate_id, exc)
            outcomes.append(
                EvidenceOutcome(candidate_id=candidate_id, ok=False, error=str(exc))
            )
    return outcomes
