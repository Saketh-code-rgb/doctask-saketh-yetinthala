"""The library universe loader, checked against LIBRARY_UNIVERSE.md itself.

Several tests parse the source Markdown directly and compare it to the YAML,
so a library added to one and not the other fails here rather than going
unnoticed. TECHNICAL_DESIGN.md section 24 flags keeping the two in sync as a
manual step; these tests are what make that drift visible.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

from dependency_map.library_universe import (
    DIRECTIONS,
    DISCOVERY_TIERS,
    LIBRARY_CATEGORIES,
    InfrastructurePattern,
    LibraryUniverseError,
    load_library_universe,
)

UNIVERSE_PATH = Path("data") / "library-universe.yaml"
SOURCE_DOC = Path("LIBRARY_UNIVERSE.md")

EXPECTED_ENTRY_COUNT = 30
EXPECTED_CATEGORY_COUNTS = {
    "docx": 8,
    "pdf": 8,
    "template_generation": 5,
    "conversion": 4,
    "other_processing": 5,
}


@pytest.fixture(scope="module")
def universe():
    return load_library_universe(UNIVERSE_PATH)


def _source_document_rows() -> list[str]:
    """Every library name from the five tables in LIBRARY_UNIVERSE.md."""
    names: list[str] = []
    in_table_section = False
    for line in SOURCE_DOC.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_table_section = bool(re.match(r"##\s+[1-5]\.", line))
            continue
        if not in_table_section or not line.startswith("|"):
            continue
        first = line.strip("|").split("|")[0].strip()
        if first in ("Library", "") or set(first) <= set("-: "):
            continue
        names.append(first)
    return names


def _write(path: Path, data) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    return path


# --- loading ---------------------------------------------------------------


def test_yaml_loads(universe):
    assert len(universe) == EXPECTED_ENTRY_COUNT


def test_missing_file_is_reported(tmp_path):
    with pytest.raises(LibraryUniverseError, match="No library universe file"):
        load_library_universe(tmp_path / "absent.yaml")


def test_loading_is_deterministic():
    """Repeated loads must be identical, so query ordering stays reproducible."""
    first = load_library_universe(UNIVERSE_PATH)
    second = load_library_universe(UNIVERSE_PATH)

    assert first == second
    assert first.names == second.names
    assert first.entries[0] == second.entries[0]


def test_order_follows_the_source_document(universe):
    assert list(universe.names) == _source_document_rows()


# --- every entry is represented --------------------------------------------


def test_every_row_in_the_source_document_is_present(universe):
    """The check that catches drift between the Markdown and the YAML."""
    from_doc = _source_document_rows()

    assert len(from_doc) == EXPECTED_ENTRY_COUNT
    assert set(universe.names) == set(from_doc)


def test_no_entry_was_added_beyond_the_source_document(universe):
    extra = set(universe.names) - set(_source_document_rows())
    assert extra == set(), f"YAML has libraries not in LIBRARY_UNIVERSE.md: {extra}"


def test_no_entry_was_dropped(universe):
    missing = set(_source_document_rows()) - set(universe.names)
    assert missing == set(), f"LIBRARY_UNIVERSE.md rows missing from YAML: {missing}"


def test_category_counts_match_the_five_source_tables(universe):
    assert universe.category_counts() == EXPECTED_CATEGORY_COUNTS
    assert sum(EXPECTED_CATEGORY_COUNTS.values()) == EXPECTED_ENTRY_COUNT


def test_no_duplicate_library_names(universe):
    assert len(set(universe.names)) == len(universe.names)


# --- known entries ---------------------------------------------------------


def test_python_docx(universe):
    entry = universe.by_name("python-docx")

    assert entry.category == "docx"
    assert entry.direction == "generation"
    assert entry.ecosystems == ("python",)
    assert "python-docx" in entry.package_names
    assert "requirements.txt" in entry.manifest_filenames
    assert "pyproject.toml" in entry.manifest_filenames
    assert not entry.is_infrastructure


def test_docxtemplater(universe):
    entry = universe.by_name("docxtemplater")

    assert entry.category == "docx"
    assert entry.direction == "generation"
    assert entry.ecosystems == ("javascript",)
    assert entry.package_names == ("docxtemplater",)
    assert entry.manifest_filenames == ("package.json",)
    assert not entry.is_infrastructure


def test_gotenberg(universe):
    """The infrastructure case: a service, so no manifest at all."""
    entry = universe.by_name("Gotenberg")

    assert entry.category == "conversion"
    assert entry.direction == "conversion"
    assert entry.manifest_filenames == ()
    assert entry.is_infrastructure

    patterns = {(p.detection, p.pattern) for p in entry.infrastructure_patterns}
    assert ("compose", "gotenberg/gotenberg") in patterns


def test_gotenberg_compose_pattern_matches_the_search_strategy(universe):
    """SEARCH_STRATEGY.md section 4:
    "gotenberg/gotenberg" filename:docker-compose.yml"""
    entry = universe.by_name("Gotenberg")
    compose = [p for p in entry.infrastructure_patterns if p.detection == "compose"]

    assert compose
    assert compose[0].filename == "docker-compose.yml"
    assert compose[0].pattern == "gotenberg/gotenberg"


def test_pandoc_is_infrastructure_not_a_manifest_dependency(universe):
    """"Pandoc is a CLI tool, not an importable library, so it won't show up in
    a manifest file." SEARCH_STRATEGY.md section 4."""
    entry = universe.by_name("Pandoc")

    assert entry.ecosystems == ("cli",)
    assert entry.manifest_filenames == ()
    assert entry.is_infrastructure

    detections = {p.detection for p in entry.infrastructure_patterns}
    assert "dockerfile" in detections
    assert "subprocess" in detections


def test_libreoffice_headless_is_infrastructure(universe):
    entry = universe.by_name("LibreOffice headless / unoconv / JODConverter")

    assert entry.category == "conversion"
    assert entry.is_infrastructure
    assert "unoconv" in entry.package_names


def test_exactly_three_infrastructure_entries(universe):
    """Pandoc, LibreOffice headless and Gotenberg, per SEARCH_STRATEGY.md
    section 2's list of tools that aren't code dependencies at all."""
    names = {e.library_name for e in universe.infrastructure_entries()}

    assert names == {
        "Pandoc",
        "LibreOffice headless / unoconv / JODConverter",
        "Gotenberg",
    }


# --- discovery tiers -------------------------------------------------------

EXPECTED_TIER_COUNTS = {1: 3, 2: 5, 3: 22}


def test_every_entry_has_a_valid_tier(universe):
    for entry in universe:
        assert entry.discovery_tier in DISCOVERY_TIERS, entry.library_name


def test_tier_counts(universe):
    assert universe.tier_counts() == EXPECTED_TIER_COUNTS
    assert sum(EXPECTED_TIER_COUNTS.values()) == EXPECTED_ENTRY_COUNT


def test_tier_one_is_exactly_the_infrastructure_entries(universe):
    """Tier 1 is defined by having an infrastructure pattern, so the two views
    must agree or one of them is wrong."""
    by_tier = {e.library_name for e in universe.by_tier(1)}
    by_pattern = {e.library_name for e in universe.infrastructure_entries()}

    assert by_tier == by_pattern


def test_tier_two_membership(universe):
    """SEARCH_STRATEGY.md section 4.2. Only the first two were measured in the
    phase 6A experiment; the rest were placed by reasoning."""
    assert {e.library_name for e in universe.by_tier(2)} == {
        "docxtemplater",
        "docxtpl (python-docx-template)",
        "Carbone.io",
        "JasperReports / Apache FOP",
        "docx-mailmerge / docxedit",
    }


def test_tier_is_independent_of_category(universe):
    """The reason the two fields exist separately.

    docxtemplater is a DOCX library but a tier-2 signal, because it fills
    templates from data. Puppeteer sits in the template category but is tier 3,
    because the package is overwhelmingly browser-test tooling.
    """
    docxtemplater = universe.by_name("docxtemplater")
    assert docxtemplater.category == "docx"
    assert docxtemplater.discovery_tier == 2

    puppeteer = universe.by_name("Puppeteer / Playwright (used for PDF)")
    assert puppeteer.category == "template_generation"
    assert puppeteer.discovery_tier == 3


def test_measured_tier_assignments(universe):
    """Anchored to the phase 6A measurements, 2026-08-20."""
    assert universe.by_name("Gotenberg").discovery_tier == 1        # 662, uncapped
    assert universe.by_name("docxtpl (python-docx-template)").discovery_tier == 2
    assert universe.by_name("python-docx").discovery_tier == 3      # 75,648, capped
    assert universe.by_name("Apache PDFBox").discovery_tier == 3    # 16,832, capped
    assert universe.by_name("ReportLab").discovery_tier == 3        # 90,240, capped


def test_by_tier_rejects_an_unknown_tier(universe):
    with pytest.raises(ValueError):
        universe.by_tier(4)


def test_invalid_tier_value_fails(tmp_path):
    entry = {**VALID_ENTRY, "discovery_tier": 4}
    path = _write(tmp_path / "u.yaml", {"libraries": [entry]})

    with pytest.raises(LibraryUniverseError, match="discovery_tier must be one of"):
        load_library_universe(path)


def test_non_integer_tier_fails(tmp_path):
    entry = {**VALID_ENTRY, "discovery_tier": "one"}
    path = _write(tmp_path / "u.yaml", {"libraries": [entry]})

    with pytest.raises(LibraryUniverseError, match="discovery_tier"):
        load_library_universe(path)


# --- directions ------------------------------------------------------------


def test_every_direction_is_valid(universe):
    for entry in universe:
        assert entry.direction in DIRECTIONS


def test_every_category_is_valid(universe):
    for entry in universe:
        assert entry.category in LIBRARY_CATEGORIES


def test_directions_stated_outright_in_the_source_note(universe):
    """"A DOCX or PDF generation library (python-docx, ReportLab, docxtpl,
    Carbone) ... An extraction library (Apache Tika, Unstructured, Docling)."""
    for name in ["python-docx", "ReportLab", "docxtpl (python-docx-template)",
                 "Carbone.io"]:
        assert universe.by_name(name).direction == "generation", name

    for name in ["Apache Tika", "Unstructured", "Docling"]:
        assert universe.by_name(name).direction == "extraction", name


def test_the_two_genuinely_bidirectional_entries_are_mixed(universe):
    """"Some libraries genuinely do both (PyMuPDF, pdf2docx)." That list names
    exactly two, so exactly two entries should be mixed."""
    mixed = {e.library_name for e in universe.by_direction("mixed")}

    assert mixed == {"PyMuPDF (fitz)", "pdf2docx"}


def test_conversion_tools_are_tagged_conversion(universe):
    """"A few conversion tools (Pandoc, Gotenberg, LibreOffice headless) sit in
    between, moving content from one format to another."""
    for name in ["Pandoc", "Gotenberg",
                 "LibreOffice headless / unoconv / JODConverter"]:
        assert universe.by_name(name).direction == "conversion", name


def test_pypdf_direction_matches_the_candidate_schema_example(universe):
    """CANDIDATE_SCHEMA.md section 10 records pypdf as extraction."""
    assert universe.by_name("pypdf / PyPDF2").direction == "extraction"


def test_weasyprint_matches_the_candidate_schema_example(universe):
    """CANDIDATE_SCHEMA.md section 10 records WeasyPrint as
    template_generation / conversion."""
    entry = universe.by_name("WeasyPrint")

    assert entry.category == "template_generation"
    assert entry.direction == "conversion"


def test_mammoth_is_extraction(universe):
    """"Different direction: this is about displaying Word content on the web,
    not generating documents."""
    assert universe.by_name("mammoth / python-mammoth").direction == "extraction"


# --- manifests and multi-package rows --------------------------------------


def test_every_non_infrastructure_entry_has_a_manifest(universe):
    for entry in universe:
        if not entry.is_infrastructure:
            assert entry.manifest_filenames, entry.library_name


def test_every_entry_is_findable_somehow(universe):
    """Either a manifest search or an infrastructure pattern must apply, or
    discovery has no way to look for it."""
    for entry in universe:
        targets = entry.discovery_targets()
        assert targets.has_manifest_signal or targets.has_infrastructure_signal


def test_multi_package_rows_keep_all_their_names(universe):
    """A row naming several packages stays one entry, not several."""
    assert set(universe.by_name("pypdf / PyPDF2").package_names) >= {"pypdf", "PyPDF2"}
    assert set(universe.by_name("Puppeteer / Playwright (used for PDF)").package_names) \
        >= {"puppeteer", "playwright"}
    assert set(universe.by_name("docx-mailmerge / docxedit").package_names) \
        >= {"docx-mailmerge", "docxedit"}


def test_multi_ecosystem_rows_are_preserved(universe):
    assert set(universe.by_name("Aspose.Words").ecosystems) == {
        "dotnet", "java", "python", "cpp"
    }
    assert set(universe.by_name("mammoth / python-mammoth").ecosystems) == {
        "javascript", "python"
    }
    assert set(universe.by_name("Apache Tika").ecosystems) == {"java", "python"}


def test_python_entries_use_python_manifests(universe):
    """SEARCH_STRATEGY.md section 2 maps ecosystems to manifest files."""
    for entry in universe:
        if entry.ecosystems == ("python",):
            assert "requirements.txt" in entry.manifest_filenames, entry.library_name


def test_java_entries_use_java_manifests(universe):
    for entry in universe:
        if entry.ecosystems == ("java",):
            assert "pom.xml" in entry.manifest_filenames, entry.library_name


# --- discovery_targets helper ----------------------------------------------


def test_discovery_targets_for_a_manifest_library(universe):
    targets = universe.by_name("python-docx").discovery_targets()

    assert targets.library_name == "python-docx"
    assert targets.has_manifest_signal
    assert not targets.has_infrastructure_signal
    assert "requirements.txt" in targets.manifest_filenames


def test_discovery_targets_for_an_infrastructure_tool(universe):
    targets = universe.by_name("Gotenberg").discovery_targets()

    assert not targets.has_manifest_signal
    assert targets.has_infrastructure_signal
    assert targets.infrastructure_patterns[0].filename == "docker-compose.yml"


# --- lookups ---------------------------------------------------------------


def test_by_name_raises_for_an_unknown_library(universe):
    with pytest.raises(KeyError):
        universe.by_name("not-a-real-library")


def test_by_category_rejects_an_unknown_category(universe):
    with pytest.raises(ValueError):
        universe.by_category("spreadsheets")


def test_by_direction_rejects_an_unknown_direction(universe):
    with pytest.raises(ValueError):
        universe.by_direction("sideways")


def test_by_category_returns_the_right_entries(universe):
    docx = {e.library_name for e in universe.by_category("docx")}

    assert "python-docx" in docx
    assert "ReportLab" not in docx
    assert len(docx) == EXPECTED_CATEGORY_COUNTS["docx"]


# --- malformed input -------------------------------------------------------


VALID_ENTRY = {
    "library_name": "example-lib",
    "ecosystems": ["python"],
    "category": "docx",
    "direction": "generation",
    "package_names": ["example-lib"],
    "discovery_tier": 3,
    "manifest_filenames": ["requirements.txt"],
}


def test_invalid_yaml_fails_clearly(tmp_path):
    path = tmp_path / "broken.yaml"
    path.write_text("libraries: [unclosed\n", encoding="utf-8")

    with pytest.raises(LibraryUniverseError, match="not valid YAML"):
        load_library_universe(path)


def test_missing_libraries_key_fails(tmp_path):
    with pytest.raises(LibraryUniverseError, match="missing the 'libraries' list"):
        load_library_universe(_write(tmp_path / "u.yaml", {"version": 1}))


def test_empty_libraries_list_fails(tmp_path):
    with pytest.raises(LibraryUniverseError, match="empty"):
        load_library_universe(_write(tmp_path / "u.yaml", {"libraries": []}))


def test_top_level_must_be_a_mapping(tmp_path):
    with pytest.raises(LibraryUniverseError, match="mapping at the top level"):
        load_library_universe(_write(tmp_path / "u.yaml", ["a", "b"]))


def test_duplicate_library_name_is_rejected(tmp_path):
    """Never silently accepted: it would double every query for that library."""
    path = _write(tmp_path / "u.yaml", {"libraries": [VALID_ENTRY, dict(VALID_ENTRY)]})

    with pytest.raises(LibraryUniverseError, match="duplicate library_name"):
        load_library_universe(path)


@pytest.mark.parametrize("field", ["library_name", "ecosystems", "category",
                                   "direction", "package_names",
                                   "discovery_tier"])
def test_missing_required_field_fails(tmp_path, field):
    entry = {k: v for k, v in VALID_ENTRY.items() if k != field}
    path = _write(tmp_path / "u.yaml", {"libraries": [entry]})

    with pytest.raises(LibraryUniverseError):
        load_library_universe(path)


def test_unknown_category_fails(tmp_path):
    entry = {**VALID_ENTRY, "category": "spreadsheets"}
    path = _write(tmp_path / "u.yaml", {"libraries": [entry]})

    with pytest.raises(LibraryUniverseError, match="category must be one of"):
        load_library_universe(path)


def test_unknown_direction_fails(tmp_path):
    entry = {**VALID_ENTRY, "direction": "sideways"}
    path = _write(tmp_path / "u.yaml", {"libraries": [entry]})

    with pytest.raises(LibraryUniverseError, match="direction must be one of"):
        load_library_universe(path)


def test_unknown_field_fails(tmp_path):
    """Guards against a typo silently doing nothing."""
    entry = {**VALID_ENTRY, "manifest_filename": ["requirements.txt"]}
    path = _write(tmp_path / "u.yaml", {"libraries": [entry]})

    with pytest.raises(LibraryUniverseError, match="unknown fields"):
        load_library_universe(path)


def test_empty_ecosystems_fails(tmp_path):
    entry = {**VALID_ENTRY, "ecosystems": []}
    path = _write(tmp_path / "u.yaml", {"libraries": [entry]})

    with pytest.raises(LibraryUniverseError, match="must not be empty"):
        load_library_universe(path)


def test_entry_with_no_way_to_find_it_fails(tmp_path):
    entry = {k: v for k, v in VALID_ENTRY.items() if k != "manifest_filenames"}
    path = _write(tmp_path / "u.yaml", {"libraries": [entry]})

    with pytest.raises(LibraryUniverseError, match="no way to search for it"):
        load_library_universe(path)


def test_string_where_a_list_belongs_fails(tmp_path):
    entry = {**VALID_ENTRY, "ecosystems": "python"}
    path = _write(tmp_path / "u.yaml", {"libraries": [entry]})

    with pytest.raises(LibraryUniverseError, match="must be a list"):
        load_library_universe(path)


def test_unknown_infrastructure_detection_fails(tmp_path):
    entry = {
        **VALID_ENTRY,
        "infrastructure_patterns": [{"detection": "telepathy", "pattern": "x"}],
    }
    path = _write(tmp_path / "u.yaml", {"libraries": [entry]})

    with pytest.raises(LibraryUniverseError, match="detection must be one of"):
        load_library_universe(path)


def test_infrastructure_pattern_without_a_pattern_fails(tmp_path):
    entry = {
        **VALID_ENTRY,
        "infrastructure_patterns": [{"detection": "dockerfile", "filename": "Dockerfile"}],
    }
    path = _write(tmp_path / "u.yaml", {"libraries": [entry]})

    with pytest.raises(LibraryUniverseError, match="pattern must be a non-empty string"):
        load_library_universe(path)


def test_a_valid_minimal_file_loads(tmp_path):
    universe = load_library_universe(
        _write(tmp_path / "u.yaml", {"libraries": [VALID_ENTRY]})
    )

    assert len(universe) == 1
    assert universe.by_name("example-lib").direction == "generation"


def test_infrastructure_pattern_filename_may_be_null(tmp_path):
    entry = {
        **VALID_ENTRY,
        "infrastructure_patterns": [
            {"detection": "subprocess", "filename": None, "pattern": "subprocess pandoc"}
        ],
    }
    universe = load_library_universe(_write(tmp_path / "u.yaml", {"libraries": [entry]}))
    pattern = universe.by_name("example-lib").infrastructure_patterns[0]

    assert pattern == InfrastructurePattern(
        detection="subprocess", pattern="subprocess pandoc", filename=None
    )


# --- no second library list in Python --------------------------------------


def _executable_source(path: Path) -> str:
    """Source with docstrings and comments stripped.

    The guard below is about a library list influencing behaviour, not about
    prose. A comment naming docxtemplater to explain why tier and category are
    separate concepts is documentation; the same name in a tuple would be a
    second source of truth. Only the latter is a defect.
    """
    source = path.read_text(encoding="utf-8")
    source = re.sub(r'"""(?:.|\n)*?"""', "", source)
    source = re.sub(r"(?m)#.*$", "", source)
    return source


def test_the_loader_does_not_hardcode_library_names():
    """The YAML is the machine-readable source. A second list in Python would
    drift from it silently."""
    source = _executable_source(Path("src/dependency_map/library_universe.py"))

    for name in ["python-docx", "docxtemplater", "reportlab", "docxtpl",
                 "pdf-lib", "PDFKit", "WeasyPrint"]:
        assert name not in source, f"{name} is hardcoded in the loader"


def test_loader_makes_no_network_calls():
    source = Path("src/dependency_map/library_universe.py").read_text(encoding="utf-8")

    for forbidden in ["requests", "urllib", "http", "socket"]:
        assert f"import {forbidden}" not in source


def test_loader_does_not_depend_on_the_database_layer():
    source = Path("src/dependency_map/library_universe.py").read_text(encoding="utf-8")

    assert "from .db" not in source
    assert "import sqlite3" not in source
