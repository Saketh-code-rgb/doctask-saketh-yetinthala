"""Loads the library universe that discovery searches for.

LIBRARY_UNIVERSE.md is the human-readable source of truth and holds the
reasoning behind each entry. data/library-universe.yaml is the machine-readable
sibling this module reads (TECHNICAL_DESIGN.md section 5). There is deliberately
no second library list hardcoded here: if an entry isn't in the YAML, this
module doesn't know about it.

Pure and offline. No network calls, and no dependency on the database layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator, Mapping, Sequence

import yaml

#: From CANDIDATE_SCHEMA.md section 4, matching the five tables in
#: LIBRARY_UNIVERSE.md one for one.
LIBRARY_CATEGORIES: tuple[str, ...] = (
    "docx",
    "pdf",
    "template_generation",
    "conversion",
    "other_processing",
)

#: From CANDIDATE_SCHEMA.md section 4 and the closing note in
#: LIBRARY_UNIVERSE.md on generation versus extraction.
DIRECTIONS: tuple[str, ...] = ("generation", "extraction", "conversion", "mixed")

#: How an infrastructure tool shows up when it is not a package dependency.
#: SEARCH_STRATEGY.md section 2.
INFRASTRUCTURE_DETECTIONS: tuple[str, ...] = ("dockerfile", "compose", "subprocess")

#: Discovery tiers from SEARCH_STRATEGY.md section 4, ordered by measured
#: precision rather than by library popularity.
#:
#: Deliberately independent of library_category: a tier is a claim about how
#: precise a query for this entry will be, a category is a claim about what the
#: library does. docxtemplater is category docx but tier 2, because it fills
#: templates from data; Puppeteer is category template_generation but tier 3,
#: because the package is overwhelmingly browser-test tooling.
TIER_INFRASTRUCTURE = 1
TIER_TEMPLATE_GENERATION = 2
TIER_BROAD_MANIFEST = 3
DISCOVERY_TIERS: tuple[int, ...] = (
    TIER_INFRASTRUCTURE,
    TIER_TEMPLATE_GENERATION,
    TIER_BROAD_MANIFEST,
)

DEFAULT_UNIVERSE_PATH = Path("data") / "library-universe.yaml"

_REQUIRED_FIELDS = (
    "library_name",
    "ecosystems",
    "category",
    "direction",
    "package_names",
    "discovery_tier",
)
_ALLOWED_FIELDS = frozenset(
    _REQUIRED_FIELDS + ("manifest_filenames", "infrastructure_patterns")
)


class LibraryUniverseError(Exception):
    """The library universe file is missing or malformed."""


@dataclass(frozen=True)
class InfrastructurePattern:
    """A signal that lives in a Dockerfile or compose file rather than a
    manifest, for tools like Pandoc, Gotenberg and LibreOffice headless."""

    detection: str
    pattern: str
    filename: str | None = None


@dataclass(frozen=True)
class LibraryEntry:
    """One row from LIBRARY_UNIVERSE.md."""

    library_name: str
    ecosystems: tuple[str, ...]
    category: str
    direction: str
    package_names: tuple[str, ...]
    discovery_tier: int
    manifest_filenames: tuple[str, ...] = ()
    infrastructure_patterns: tuple[InfrastructurePattern, ...] = ()

    @property
    def is_infrastructure(self) -> bool:
        """True when the signal lives in infrastructure rather than a manifest.

        Pandoc is the clearest case: a CLI tool that never appears in a
        dependency file, so a manifest search would miss it entirely.
        """
        return bool(self.infrastructure_patterns)

    def discovery_targets(self) -> DiscoveryTargets:
        """Everything the query generator needs for this entry.

        Returns the manifest filenames worth searching and any
        infrastructure-reference patterns, so a caller doesn't have to know
        which kind of entry it is holding.
        """
        return DiscoveryTargets(
            library_name=self.library_name,
            package_names=self.package_names,
            manifest_filenames=self.manifest_filenames,
            infrastructure_patterns=self.infrastructure_patterns,
        )


@dataclass(frozen=True)
class DiscoveryTargets:
    """What to search for, for one library entry."""

    library_name: str
    package_names: tuple[str, ...]
    manifest_filenames: tuple[str, ...]
    infrastructure_patterns: tuple[InfrastructurePattern, ...]

    @property
    def has_manifest_signal(self) -> bool:
        return bool(self.manifest_filenames)

    @property
    def has_infrastructure_signal(self) -> bool:
        return bool(self.infrastructure_patterns)


@dataclass(frozen=True)
class LibraryUniverse:
    """The loaded universe, in source-document order."""

    entries: tuple[LibraryEntry, ...]
    version: int = 1

    def __len__(self) -> int:
        return len(self.entries)

    def __iter__(self) -> Iterator[LibraryEntry]:
        return iter(self.entries)

    @property
    def names(self) -> tuple[str, ...]:
        return tuple(entry.library_name for entry in self.entries)

    def by_name(self, library_name: str) -> LibraryEntry:
        for entry in self.entries:
            if entry.library_name == library_name:
                return entry
        raise KeyError(f"No library named {library_name!r} in the universe")

    def by_category(self, category: str) -> tuple[LibraryEntry, ...]:
        if category not in LIBRARY_CATEGORIES:
            raise ValueError(f"Unknown category {category!r}")
        return tuple(e for e in self.entries if e.category == category)

    def by_direction(self, direction: str) -> tuple[LibraryEntry, ...]:
        if direction not in DIRECTIONS:
            raise ValueError(f"Unknown direction {direction!r}")
        return tuple(e for e in self.entries if e.direction == direction)

    def infrastructure_entries(self) -> tuple[LibraryEntry, ...]:
        return tuple(e for e in self.entries if e.is_infrastructure)

    def by_tier(self, tier: int) -> tuple[LibraryEntry, ...]:
        if tier not in DISCOVERY_TIERS:
            raise ValueError(f"Unknown discovery tier {tier!r}")
        return tuple(e for e in self.entries if e.discovery_tier == tier)

    def category_counts(self) -> dict[str, int]:
        return {c: len(self.by_category(c)) for c in LIBRARY_CATEGORIES}

    def tier_counts(self) -> dict[int, int]:
        return {t: len(self.by_tier(t)) for t in DISCOVERY_TIERS}


# --- validation helpers ----------------------------------------------------


def _string_list(value: Any, field: str, where: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str) or not isinstance(value, Sequence):
        raise LibraryUniverseError(f"{where}: '{field}' must be a list, found {value!r}")
    items: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise LibraryUniverseError(
                f"{where}: '{field}' must contain non-empty strings, found {item!r}"
            )
        items.append(item)
    return tuple(items)


def _parse_patterns(value: Any, where: str) -> tuple[InfrastructurePattern, ...]:
    if value is None:
        return ()
    if isinstance(value, str) or not isinstance(value, Sequence):
        raise LibraryUniverseError(
            f"{where}: 'infrastructure_patterns' must be a list"
        )
    patterns: list[InfrastructurePattern] = []
    for raw in value:
        if not isinstance(raw, Mapping):
            raise LibraryUniverseError(
                f"{where}: each infrastructure pattern must be a mapping, found {raw!r}"
            )
        detection = raw.get("detection")
        pattern = raw.get("pattern")
        if detection not in INFRASTRUCTURE_DETECTIONS:
            raise LibraryUniverseError(
                f"{where}: infrastructure detection must be one of "
                f"{list(INFRASTRUCTURE_DETECTIONS)}, found {detection!r}"
            )
        if not isinstance(pattern, str) or not pattern.strip():
            raise LibraryUniverseError(
                f"{where}: infrastructure pattern must be a non-empty string, "
                f"found {pattern!r}"
            )
        filename = raw.get("filename")
        if filename is not None and not isinstance(filename, str):
            raise LibraryUniverseError(
                f"{where}: infrastructure filename must be a string or null, "
                f"found {filename!r}"
            )
        patterns.append(
            InfrastructurePattern(
                detection=detection, pattern=pattern, filename=filename
            )
        )
    return tuple(patterns)


def _parse_entry(raw: Any, index: int) -> LibraryEntry:
    where = f"library #{index + 1}"
    if not isinstance(raw, Mapping):
        raise LibraryUniverseError(f"{where} must be a mapping, found {type(raw).__name__}")

    name = raw.get("library_name")
    if not isinstance(name, str) or not name.strip():
        raise LibraryUniverseError(f"{where} is missing a usable 'library_name'")
    where = f"library {name!r}"

    if unknown := sorted(set(raw) - _ALLOWED_FIELDS):
        raise LibraryUniverseError(f"{where} has unknown fields: {unknown}")
    if missing := [f for f in _REQUIRED_FIELDS if f not in raw]:
        raise LibraryUniverseError(f"{where} is missing required fields: {missing}")

    category = raw["category"]
    if category not in LIBRARY_CATEGORIES:
        raise LibraryUniverseError(
            f"{where}: category must be one of {list(LIBRARY_CATEGORIES)}, "
            f"found {category!r}"
        )

    direction = raw["direction"]
    if direction not in DIRECTIONS:
        raise LibraryUniverseError(
            f"{where}: direction must be one of {list(DIRECTIONS)}, found {direction!r}"
        )

    tier = raw["discovery_tier"]
    if isinstance(tier, bool) or tier not in DISCOVERY_TIERS:
        raise LibraryUniverseError(
            f"{where}: discovery_tier must be one of {list(DISCOVERY_TIERS)}, "
            f"found {tier!r}"
        )

    ecosystems = _string_list(raw["ecosystems"], "ecosystems", where)
    if not ecosystems:
        raise LibraryUniverseError(f"{where}: 'ecosystems' must not be empty")

    package_names = _string_list(raw["package_names"], "package_names", where)
    if not package_names:
        raise LibraryUniverseError(f"{where}: 'package_names' must not be empty")

    manifests = _string_list(raw.get("manifest_filenames"), "manifest_filenames", where)
    patterns = _parse_patterns(raw.get("infrastructure_patterns"), where)

    # An entry nothing can be found by would be silently useless to discovery.
    if not manifests and not patterns:
        raise LibraryUniverseError(
            f"{where} has neither manifest_filenames nor infrastructure_patterns, "
            f"so discovery would have no way to search for it"
        )

    return LibraryEntry(
        library_name=name,
        ecosystems=ecosystems,
        category=category,
        direction=direction,
        package_names=package_names,
        discovery_tier=tier,
        manifest_filenames=manifests,
        infrastructure_patterns=patterns,
    )


def load_library_universe(
    path: Path | str = DEFAULT_UNIVERSE_PATH,
) -> LibraryUniverse:
    """Read and validate data/library-universe.yaml.

    Order is preserved from the file, so repeated loads return identical
    structures and any downstream query ordering stays reproducible.
    """
    path = Path(path)
    if not path.is_file():
        raise LibraryUniverseError(f"No library universe file at {path}")

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise LibraryUniverseError(f"{path} is not valid YAML: {exc}") from exc

    if not isinstance(data, Mapping):
        raise LibraryUniverseError(f"{path} must contain a mapping at the top level")

    raw_entries = data.get("libraries")
    if raw_entries is None:
        raise LibraryUniverseError(f"{path} is missing the 'libraries' list")
    if isinstance(raw_entries, str) or not isinstance(raw_entries, Sequence):
        raise LibraryUniverseError(f"{path}: 'libraries' must be a list")
    if not raw_entries:
        raise LibraryUniverseError(f"{path}: 'libraries' is empty")

    entries = tuple(_parse_entry(raw, i) for i, raw in enumerate(raw_entries))

    seen: set[str] = set()
    for entry in entries:
        if entry.library_name in seen:
            raise LibraryUniverseError(
                f"{path}: duplicate library_name {entry.library_name!r}. "
                f"Each row in LIBRARY_UNIVERSE.md maps to exactly one entry."
            )
        seen.add(entry.library_name)

    version = data.get("version", 1)
    if isinstance(version, bool) or not isinstance(version, int):
        raise LibraryUniverseError(f"{path}: 'version' must be an integer")

    return LibraryUniverse(entries=entries, version=version)
