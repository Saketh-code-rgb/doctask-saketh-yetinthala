"""company_name must name an organisation, never an individual.

The task brief is explicit: real companies may appear anywhere in this
repository, real people may not. Most open-source copyright lines name a
person, so the extractor has to tell the two apart before it stores anything.

The bias is deliberate and one-directional. A missed company is a null field a
human can fill in later; a stored personal name is a rule violation that ships
inside a submitted artefact. Where a name is genuinely ambiguous, these tests
expect it refused.
"""

from __future__ import annotations

import pytest

from dependency_map.evidence import detect_company_name, looks_like_person


# --- obvious individuals ----------------------------------------------------


@pytest.mark.parametrize("name", [
    "Jolie Zeng",
    "Ricardo Oliveira",
    "Jakub Dundalek",
    "Bruno Fortunato",
    "Orhan Engin Okay",
    # Hyphenated given names are ordinary and must not read as corporate.
    "Ka-Ping Yee",
    "Jean-Luc Picard",
    "Anne-Marie Smith",
    # Honorifics and generational suffixes settle it immediately.
    "Dr. Alan Turing",
    "Prof. Ada Lovelace",
    "John Smith Jr.",
])
def test_individuals_are_recognised(name):
    assert looks_like_person(name) is True


# --- organisations ----------------------------------------------------------


@pytest.mark.parametrize("name", [
    # Legal-form markers.
    "Acme Inc.", "Widget LLC", "Contoso Ltd", "Beispiel GmbH",
    "Physical Superintelligence PBC",
    # Sector words.
    "Redeyed Technologies", "HYPERION Consulting", "Free Software Foundation",
    "Arizona State University", "Alibaba Research Group",
    # Brand shapes: internal capitals, domains, digits, ampersands.
    "JetBrains", "BigBearTechWorld", "JupiterOne", "Kartoza.com",
    "302 AI", "P&G",
    # Single-word brands are too weak to refuse on.
    "Liferay", "Haulmont", "Cisco", "Symfony", "Atos", "Sangfor",
    # A hyphen alone must not make a person out of an acronym.
    "SK-CERT", "Hewlett-Packard Company",
])
def test_organisations_are_not_mistaken_for_people(name):
    assert looks_like_person(name) is False


# --- ambiguity is refused, not guessed --------------------------------------


@pytest.mark.parametrize("name", [
    "Marcus Aurelius",   # could be a consultancy; reads as a person
    "Taylor Morgan",     # either; refused rather than stored
    "Alexander Grant",
])
def test_ambiguous_two_word_names_are_treated_as_people(name):
    """Two bare capitalised words with no organisational marker is the shape of
    a personal name. Refusing costs a null; accepting risks the violation."""
    assert looks_like_person(name) is True


def test_empty_and_degenerate_values_do_not_crash():
    for value in ("", "   ", ",", "."):
        assert looks_like_person(value) is False


# --- end to end through the extractor ---------------------------------------


@pytest.mark.parametrize("readme", [
    "# Tool\n\nCopyright (c) 2024 Jolie Zeng\n",
    "# Tool\n\n(C) 2019-2024 Ka-Ping Yee. All rights reserved.\n",
    "# Tool\n\nBuilt by Ricardo Oliveira\n",
    "# Tool\n\nA product of Bruno Fortunato\n",
])
def test_a_person_in_a_copyright_line_is_not_stored(readme):
    name, source = detect_company_name(readme)

    assert name is None, f"stored a personal name: {name!r}"
    assert source is None


@pytest.mark.parametrize("readme,expected", [
    ("# Tool\n\nCopyright 2024 Haulmont\n", "Haulmont"),
    ("# Tool\n\nCopyright (c) 2024 Redeyed Technologies\n", "Redeyed Technologies"),
    ("# Tool\n\n© 2024 Free Software Foundation\n", "Free Software Foundation"),
    ("# Tool\n\nBuilt by JetBrains\n", "JetBrains"),
    ("# Tool\n\nCopyright (c) 2023 Acme Inc.\n", "Acme Inc."),
])
def test_an_organisation_is_still_stored(readme, expected):
    name, source = detect_company_name(readme)

    assert name == expected
    assert source == "readme"


@pytest.mark.parametrize("readme", [
    "# Tool\n\nCopyright 2024 Copyright\n",
    "# Tool\n\nCopyright (c) 2024 All Rights Reserved\n",
    "# Tool\n\nCopyright 2024 Notice\n",
    "# Tool\n\nCopyright 2024 Text\n",
    "# Tool\n\nCopyright 2024 Authors\n",
])
def test_boilerplate_is_not_stored_as_a_company(readme):
    """Run 1 stored 'Copyright', 'Text', 'Notice' and 'Engineers' as company
    names, harvested from licence boilerplate."""
    name, _ = detect_company_name(readme)

    assert name is None, f"stored boilerplate as a company: {name!r}"


def test_a_readme_with_no_attribution_yields_nothing():
    name, source = detect_company_name("# Tool\n\nIt converts documents.\n")

    assert (name, source) == (None, None)


def test_the_field_stays_conservative_rather_than_inferring():
    """No inference from a domain, a slug or an org handle - only what the
    README states outright."""
    readme = "# Tool\n\nSee https://acme-corp.example.com and @acme-corp\n"

    assert detect_company_name(readme) == (None, None)
