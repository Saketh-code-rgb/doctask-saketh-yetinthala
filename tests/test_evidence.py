"""The evidence collector: what gets gathered, and what stays honestly absent.

Every response is a fixture. Nothing here touches the network, and no test
needs a real credential.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dependency_map import storage
from dependency_map.clients.github_client import (
    DirectoryEntry,
    FileContents,
    RepositoryMetadata,
)
from dependency_map.dedup import make_candidate_id, normalize_repo_url
from dependency_map.evidence import (
    EvidenceCollector,
    EvidenceError,
    collect_for_candidates,
    detect_company_name,
    detect_industry_category,
    detect_product_description,
    is_production_path,
)
from dependency_map.library_universe import load_library_universe
from dependency_map.reliability import ApiError, RateLimited, RetriesExhausted


@pytest.fixture(scope="module")
def universe():
    return load_library_universe()


# --- fakes -----------------------------------------------------------------


def metadata(**kw):
    base = dict(
        full_name="clauseforge/lease-engine",
        repo_url="https://github.com/clauseforge/lease-engine",
        repo_owner="clauseforge", repo_name="lease-engine",
        is_fork=False, is_archived=False, primary_language="Python",
        stars=41, forks=7, description="Lease agreement automation",
        homepage="https://clauseforge.example.com", default_branch="main",
        pushed_at="2026-07-30T11:02:00Z", created_at="2024-01-05T09:00:00Z",
    )
    base.update(kw)
    return RepositoryMetadata(**base)


def entry(name, type_="file", path=None):
    return DirectoryEntry(
        name=name, path=path or name, type=type_,
        html_url=f"https://github.com/clauseforge/lease-engine/blob/main/{path or name}",
    )


def file_at(path, text):
    return FileContents(
        path=path, text=text, sha="a", size=len(text),
        evidence_url=f"https://github.com/clauseforge/lease-engine/blob/main/{path}",
        repo_full_name="clauseforge/lease-engine",
    )


class CodeHit:
    def __init__(self, path, excerpt=""):
        self.path = path
        self.excerpt = excerpt
        self.rank = 1
        self.evidence_url = (
            f"https://github.com/clauseforge/lease-engine/blob/main/{path}"
        )


class SearchPage:
    def __init__(self, results):
        self.results = tuple(results)
        self.total_count = len(self.results)
        self.capped = False


class FakeClient:
    """Stands in for GitHubClient. Counts calls so budget can be asserted."""

    def __init__(self, *, meta=None, listing=(), files=None, searches=None,
                 fail=None, dirs=None):
        self._meta = meta if meta is not None else metadata()
        self._listing = listing
        self._files = files or {}
        self._searches = searches or {}
        self._fail = fail or {}
        self._dirs = dirs or {}
        self.calls: list[tuple[str, str]] = []

    def _maybe_fail(self, kind):
        if kind in self._fail:
            raise self._fail[kind]

    def get_repository(self, owner, repo, use_cache=True):
        self.calls.append(("metadata", f"{owner}/{repo}"))
        self._maybe_fail("metadata")
        return self._meta

    def list_directory(self, owner, repo, path="", ref=None, use_cache=True):
        self.calls.append(("listing", path))
        self._maybe_fail("listing")
        if path:
            return tuple(self._dirs.get(path, ()))
        return tuple(self._listing)

    def get_file_contents(self, owner, repo, path, ref=None, use_cache=True):
        self.calls.append(("file", path))
        self._maybe_fail(f"file:{path}")
        if path not in self._files:
            raise ApiError(404, f"https://x/{path}", "Not Found")
        return self._files[path]

    def search_code(self, query, per_page=30, page=1, use_cache=True):
        self.calls.append(("search", query))
        self._maybe_fail("search")
        for token, page_ in self._searches.items():
            if token in query:
                return page_
        return SearchPage([])

    def count(self, kind):
        return sum(1 for k, _ in self.calls if k == kind)


REQUIREMENTS = "flask==3.0.0\ndocxtpl==0.16.7\nreportlab==4.0.4\n"
README = """# ClauseForge Lease Engine

ClauseForge auto-generates state-specific lease agreements for property
managers and their customers from a single intake form.

Copyright 2026 ClauseForge Inc.
"""


@pytest.fixture
def seeded(conn, run_id):
    """A candidate discovered by a docxtpl query."""
    query_id = storage.create_discovery_query(
        conn, run_id=run_id, discovery_source="github_code_search",
        query='"docxtpl" filename:requirements.txt',
        library_name="docxtpl (python-docx-template)", discovery_tier=2,
    )
    url = "https://github.com/clauseforge/lease-engine"
    cid = make_candidate_id(url)
    storage.insert_candidate_if_new(
        conn, candidate_id=cid, repo_url=normalize_repo_url(url),
        repo_owner="clauseforge", repo_name="lease-engine",
        first_seen_run_id=run_id,
    )
    storage.insert_discovery_evidence(
        conn, query_id=query_id, candidate_id=cid, discovery_result_rank=1)
    return cid


def full_client():
    return FakeClient(
        listing=[
            entry("README.md"), entry("requirements.txt"),
            entry("Dockerfile"), entry("app", "dir"), entry("templates", "dir"),
        ],
        files={
            "README.md": file_at("README.md", README),
            "requirements.txt": file_at("requirements.txt", REQUIREMENTS),
            "Dockerfile": file_at("Dockerfile", "FROM python:3.12\nRUN pip install -r requirements.txt\n"),
        },
        searches={"docxtpl": SearchPage([
            CodeHit("app/documents/lease_builder.py",
                    "from docxtpl import DocxTemplate")])},
    )


def collect(conn, universe, cid, client=None):
    client = client or full_client()
    collector = EvidenceCollector(conn, client, universe)
    return collector.collect(cid), client


# --- text helpers ----------------------------------------------------------


def test_product_description_is_found_with_its_excerpt():
    found, excerpt = detect_product_description(README)

    assert found is True
    assert "property managers" in excerpt


def test_product_description_absent_from_an_internal_readme():
    found, excerpt = detect_product_description(
        "# utils\n\nInternal helper scripts for converting files.\n")

    assert found is False
    assert excerpt == ""


def test_product_description_ignores_badges_and_headings():
    readme = "# Thing\n\n[![build](https://img.shields.io/x)](https://y)\n"
    assert detect_product_description(readme) == (False, "")


def test_company_name_from_a_copyright_line():
    name, source = detect_company_name("Copyright 2026 ClauseForge Inc.")

    assert name == "ClauseForge Inc."
    assert source == "readme"


def test_company_name_from_built_by():
    name, source = detect_company_name("Built by Acme Corp for property teams.")

    assert name == "Acme Corp"
    assert source == "readme"


def test_company_name_stays_none_when_unstated():
    """CANDIDATE_SCHEMA.md section 2: never guessed."""
    assert detect_company_name("# tool\n\nGenerates documents.\n") == (None, None)


def test_company_name_is_not_inferred_from_a_domain():
    """A domain is not a stated company name. Inferring one would be a guess."""
    name, _ = detect_company_name("Visit https://acme-corp.example.com for docs.")

    assert name is None


def test_industry_category_from_keywords():
    assert detect_industry_category(
        "Generates lease agreements for property management companies"
    ) == "real_estate"


def test_industry_category_unknown_without_evidence():
    assert detect_industry_category("A small utility for files.") == "unknown"


def test_industry_category_ties_resolve_to_unknown():
    """A coin flip recorded as a finding is worse than an honest absence."""
    assert detect_industry_category("contract wedding") == "unknown"


@pytest.mark.parametrize("path,expected", [
    ("app/documents/builder.py", True),
    ("src/Chromiumly.ts", True),
    ("src/main/java/Extractor.java", True),
    # Everything below matched a real code search during the phase 8 live run
    # and was wrongly recorded as a call site.
    ("requirements.txt", False),
    ("base-requirements.txt", False),
    ("utils/parsing/unstructured-api/requirements/base.txt", False),
    (".github/dependabot.yml", False),
    (".env.example", False),
    ("README.md", False),
    ("package-lock.json", False),
    ("Dockerfile", False),
])
def test_source_file_detection(path, expected):
    from dependency_map.evidence import is_source_file

    assert is_source_file(path) is expected


@pytest.mark.parametrize("path,expected", [
    # Python, by convention rather than exact root-level name
    ("requirements.txt", "requirements.txt"),
    ("base-requirements.txt", "requirements.txt"),
    ("docker-requirements.txt", "requirements.txt"),
    ("requirements_test.txt", "requirements.txt"),
    ("requirements-dev.txt", "requirements.txt"),
    ("requirements/base.txt", "requirements.txt"),
    ("requirements/dev.txt", "requirements.txt"),
    ("docker/requirements.txt", "requirements.txt"),
    ("utils/parsing/unstructured-api/requirements/base.txt", "requirements.txt"),
    ("pyproject.toml", "pyproject.toml"),
    # JS, Java, .NET, including nested
    ("package.json", "package.json"),
    ("packages/server/package.json", "package.json"),
    ("package-lock.json", "package-lock.json"),
    ("pom.xml", "pom.xml"),
    ("services/api/pom.xml", "pom.xml"),
    ("build.gradle", "build.gradle"),
    ("build.gradle.kts", "build.gradle.kts"),
    ("packages.config", "packages.config"),
    ("src/App.csproj", "*.csproj"),
    # Not manifests: a .txt file is not a manifest just for being a .txt file
    ("README.txt", None),
    ("docs/notes.txt", None),
    ("LICENSE.txt", None),
    ("data/sample.txt", None),
    ("app/main.py", None),
    (".github/dependabot.yml", None),
    ("Dockerfile", None),
])
def test_manifest_kind_recognises_by_convention(path, expected):
    from dependency_map.evidence import manifest_kind

    assert manifest_kind(path) == expected


def test_a_nested_manifest_from_code_search_is_recorded_as_a_declaration(
    conn, universe, seeded
):
    """The sambanova case, reproduced.

    A manifest too deep for the bounded listing still gets recorded, because
    the code-search results already name it. It becomes a declaration, never a
    call site.
    """
    client = full_client()
    client._searches = {"docxtpl": SearchPage([
        CodeHit("utils/parsing/unstructured-api/requirements/base.txt",
                "docxtpl==0.16.7"),
        CodeHit("base-requirements.txt", "docxtpl==0.16.7"),
    ])}
    collect(conn, universe, seeded, client)

    deps = storage.list_dependencies_for_candidate(conn, seeded)
    declarations = [d for d in deps if d["detection_method"] == "manifest_declaration"]
    paths = {d["manifest_file"] for d in declarations}

    assert "utils/parsing/unstructured-api/requirements/base.txt" in paths
    assert "base-requirements.txt" in paths
    assert not [d for d in deps if d["detection_method"] == "code_import"]
    assert storage.get_pipeline_evidence(conn, seeded)["code_usage_confirmed"] == 0


def test_a_nested_requirements_directory_is_listed(conn, universe, seeded):
    """One bounded look into requirements/ at the root."""
    client = full_client()
    client._listing = [entry("README.md"), entry("requirements", "dir")]
    client._files["requirements/base.txt"] = file_at(
        "requirements/base.txt", REQUIREMENTS)
    client._dirs = {"requirements": [
        DirectoryEntry(name="base.txt", path="requirements/base.txt", type="file"),
    ]}
    collect(conn, universe, seeded, client)

    deps = storage.list_dependencies_for_candidate(conn, seeded)
    assert any(d["manifest_file"] == "requirements/base.txt" for d in deps)


def test_a_manifest_hit_is_never_recorded_as_a_call_site(conn, universe, seeded):
    """Regression, from the phase 8 live run.

    GitHub code search matches text in any file, so searching a repository for
    "python-docx" returns its requirements files, lockfiles and dependabot
    config. Recording those as code_import turned manifest-only candidates into
    confirmed-usage ones, which would have flowed straight into the scoring
    gate that caps unconfirmed usage.
    """
    client = full_client()
    client._searches = {"docxtpl": SearchPage([
        CodeHit("base-requirements.txt", "docxtpl==0.16.7"),
        CodeHit(".github/dependabot.yml", "docxtpl"),
        CodeHit("README.md", "we use docxtpl"),
    ])}
    collect(conn, universe, seeded, client)

    deps = storage.list_dependencies_for_candidate(conn, seeded)
    assert not [d for d in deps if d["detection_method"] == "code_import"]
    assert storage.get_pipeline_evidence(conn, seeded)["code_usage_confirmed"] == 0


def test_a_genuine_source_hit_is_still_recorded(conn, universe, seeded):
    client = full_client()
    client._searches = {"docxtpl": SearchPage([
        CodeHit("requirements.txt", "docxtpl==0.16.7"),
        CodeHit("app/render.py", "from docxtpl import DocxTemplate"),
    ])}
    collect(conn, universe, seeded, client)

    imports = [d for d in storage.list_dependencies_for_candidate(conn, seeded)
               if d["detection_method"] == "code_import"]

    assert len(imports) == 1
    assert imports[0]["evidence_url"].endswith("app/render.py")


def test_website_is_not_scraped_from_readme_prose(conn, universe, seeded):
    """Regression, from the phase 8 live run.

    The first non-GitHub link in a README is as often a badge target or an
    article as the project's own site. Taking it attributed a PDF library's
    website to a blog that had written about it.
    """
    client = full_client()
    client._meta = metadata(homepage=None)
    client._files["README.md"] = file_at(
        "README.md",
        "# tool\n\nSee the writeup at http://www.dzone.com/articles/thing\n")
    collect(conn, universe, seeded, client)

    candidate = storage.get_candidate(conn, seeded)
    assert candidate["website_url"] is None
    assert storage.get_business_evidence(conn, seeded)["website_exists"] == 0


def test_website_comes_from_the_declared_homepage(conn, universe, seeded):
    collect(conn, universe, seeded)

    assert storage.get_candidate(conn, seeded)["website_url"] == \
        "https://clauseforge.example.com"


@pytest.mark.parametrize("path,expected", [
    ("app/documents/builder.py", True),
    ("src/main.py", True),
    ("examples/demo.py", False),
    ("tests/test_x.py", False),
    ("docs/guide.py", False),
    ("scripts/run.py", False),
    ("demo/show.py", False),
])
def test_production_path_detection(path, expected):
    assert is_production_path(path) is expected


# --- metadata --------------------------------------------------------------


def test_repository_metadata_is_recorded(conn, universe, seeded):
    collect(conn, universe, seeded)
    candidate = storage.get_candidate(conn, seeded)

    assert candidate["is_fork"] == 0
    assert candidate["is_archived"] == 0
    assert candidate["primary_language"] == "Python"
    assert candidate["website_url"] == "https://clauseforge.example.com"


def test_stars_and_last_commit_are_recorded(conn, universe, seeded):
    collect(conn, universe, seeded)
    business = storage.get_business_evidence(conn, seeded)

    assert business["stars"] == 41
    assert business["last_commit_date"] == "2026-07-30"


def test_contributor_count_is_null_when_not_fetched(conn, universe, seeded):
    """Not invented: the collector never called the contributors endpoint."""
    collect(conn, universe, seeded)

    assert storage.get_business_evidence(conn, seeded)["contributor_count"] is None


def test_fork_and_archived_flags_are_carried_through(conn, universe, seeded):
    client = full_client()
    client._meta = metadata(is_fork=True, is_archived=True)
    collect(conn, universe, seeded, client)

    candidate = storage.get_candidate(conn, seeded)
    assert candidate["is_fork"] == 1
    assert candidate["is_archived"] == 1


# --- README / product evidence ---------------------------------------------


def test_readme_product_evidence_is_recorded(conn, universe, seeded):
    collect(conn, universe, seeded)
    business = storage.get_business_evidence(conn, seeded)

    assert business["readme_describes_product"] == 1
    assert "property managers" in business["readme_excerpt"]


def test_company_is_recorded_with_its_source(conn, universe, seeded):
    collect(conn, universe, seeded)
    candidate = storage.get_candidate(conn, seeded)

    assert candidate["company_name"] == "ClauseForge Inc."
    assert candidate["company_name_source"] == "readme"


def test_company_stays_null_when_the_readme_does_not_state_one(conn, universe, seeded):
    client = full_client()
    client._files["README.md"] = file_at(
        "README.md", "# tool\n\nConverts files for our customers.\n")
    collect(conn, universe, seeded, client)

    candidate = storage.get_candidate(conn, seeded)
    assert candidate["company_name"] is None
    assert candidate["company_name_source"] is None


def test_product_name_comes_from_the_first_heading(conn, universe, seeded):
    collect(conn, universe, seeded)

    assert storage.get_candidate(conn, seeded)["product_name"] == \
        "ClauseForge Lease Engine"


def test_industry_category_is_recorded(conn, universe, seeded):
    collect(conn, universe, seeded)

    assert storage.get_candidate(conn, seeded)["industry_category"] == "real_estate"


def test_a_missing_readme_is_noted_not_invented(conn, universe, seeded):
    client = FakeClient(listing=[entry("requirements.txt")],
                        files={"requirements.txt": file_at("requirements.txt",
                                                           REQUIREMENTS)})
    collect(conn, universe, seeded, client)

    business = storage.get_business_evidence(conn, seeded)
    assert business["readme_describes_product"] == 0
    assert business["readme_excerpt"] is None
    assert "no README" in business["business_evidence_notes"]


# --- dependency evidence ---------------------------------------------------


def test_manifest_declaration_is_recorded(conn, universe, seeded):
    collect(conn, universe, seeded)
    deps = storage.list_dependencies_for_candidate(conn, seeded)
    manifest = [d for d in deps if d["detection_method"] == "manifest_declaration"]

    assert manifest
    assert manifest[0]["library_name"] == "docxtpl (python-docx-template)"
    assert manifest[0]["manifest_file"] == "requirements.txt"
    assert manifest[0]["evidence_url"].endswith("requirements.txt")


def test_code_import_is_recorded_separately(conn, universe, seeded):
    """A manifest line proves declaration; only a call site proves use."""
    collect(conn, universe, seeded)
    deps = storage.list_dependencies_for_candidate(conn, seeded)
    imports = [d for d in deps if d["detection_method"] == "code_import"]

    assert imports
    assert imports[0]["evidence_url"].endswith("lease_builder.py")
    assert imports[0]["manifest_file"] is None


def test_library_category_and_direction_come_from_the_universe(conn, universe, seeded):
    collect(conn, universe, seeded)
    dep = storage.list_dependencies_for_candidate(conn, seeded)[0]

    assert dep["library_category"] == "template_generation"
    assert dep["direction"] == "generation"


def test_manifest_only_candidate_is_not_promoted_to_used(conn, universe, seeded):
    """The central honesty rule: no call site means no code_import row."""
    client = full_client()
    client._searches = {}          # code search finds nothing
    collect(conn, universe, seeded, client)

    deps = storage.list_dependencies_for_candidate(conn, seeded)
    assert deps
    assert all(d["detection_method"] == "manifest_declaration" for d in deps)
    assert storage.get_pipeline_evidence(conn, seeded)["code_usage_confirmed"] == 0


def test_a_library_with_no_evidence_is_noted(conn, universe, seeded):
    client = FakeClient(listing=[entry("README.md")],
                        files={"README.md": file_at("README.md", README)})
    outcome, _ = collect(conn, universe, seeded, client)

    assert any("no evidence located" in note for note in outcome.notes)
    assert storage.list_dependencies_for_candidate(conn, seeded) == []


def test_infrastructure_reference_is_recorded(conn, run_id, universe):
    query_id = storage.create_discovery_query(
        conn, run_id=run_id, discovery_source="github_code_search",
        query='"gotenberg/gotenberg" filename:docker-compose.yml',
        library_name="Gotenberg", discovery_tier=1)
    url = "https://github.com/acme/billing"
    cid = make_candidate_id(url)
    storage.insert_candidate_if_new(
        conn, candidate_id=cid, repo_url=normalize_repo_url(url),
        repo_owner="acme", repo_name="billing", first_seen_run_id=run_id)
    storage.insert_discovery_evidence(conn, query_id=query_id, candidate_id=cid)

    client = FakeClient(
        listing=[entry("README.md"), entry("docker-compose.yml"), entry("src", "dir")],
        files={
            "README.md": file_at("README.md", README),
            "docker-compose.yml": file_at(
                "docker-compose.yml",
                "services:\n  gotenberg:\n    image: gotenberg/gotenberg:8\n"),
        },
    )
    EvidenceCollector(conn, client, universe).collect(cid)

    deps = storage.list_dependencies_for_candidate(conn, cid)
    infra = [d for d in deps if d["detection_method"] == "infrastructure_reference"]

    assert infra
    assert infra[0]["manifest_file"] is None

    # The compose file is a *reference*. Nothing in this repository's source
    # was seen calling the service, so the stronger claim is withheld: a
    # declared service and some unrelated application code is co-presence,
    # not use. Phase 14 part A split these two meanings apart.
    pipeline = storage.get_pipeline_evidence(conn, cid)
    assert pipeline["infrastructure_reference_present"] == 1
    assert pipeline["infrastructure_service_present"] == 0


# --- pipeline evidence -----------------------------------------------------


def test_pipeline_evidence_is_populated(conn, universe, seeded):
    collect(conn, universe, seeded)
    pipeline = storage.get_pipeline_evidence(conn, seeded)

    assert pipeline["code_usage_confirmed"] == 1
    assert pipeline["template_directory_present"] == 1
    assert pipeline["pipeline_stage_count"] >= 1
    assert pipeline["pipeline_evidence_notes"]


def test_stages_are_only_counted_when_observed(conn, universe, seeded):
    """CANDIDATE_SCHEMA.md section 5: assumed stages do not count."""
    client = full_client()
    client._searches = {}
    collect(conn, universe, seeded, client)

    pipeline = storage.get_pipeline_evidence(conn, seeded)
    assert pipeline["pipeline_stage_count"] == 0
    assert "no pipeline stage observed" in pipeline["pipeline_evidence_notes"]


def test_manifest_only_is_called_out_in_the_notes(conn, universe, seeded):
    client = full_client()
    client._searches = {}
    collect(conn, universe, seeded, client)

    assert "manifest-only" in \
        storage.get_pipeline_evidence(conn, seeded)["pipeline_evidence_notes"]


def test_template_directory_is_detected(conn, universe, seeded):
    collect(conn, universe, seeded)

    assert storage.get_pipeline_evidence(conn, seeded)["template_directory_present"] == 1


def test_no_template_directory_when_absent(conn, universe, seeded):
    client = full_client()
    client._listing = [entry("README.md"), entry("requirements.txt")]
    collect(conn, universe, seeded, client)

    assert storage.get_pipeline_evidence(conn, seeded)["template_directory_present"] == 0


# --- business evidence -----------------------------------------------------


def test_application_code_detected_from_directories(conn, universe, seeded):
    collect(conn, universe, seeded)

    assert storage.get_business_evidence(conn, seeded)["application_code_exists"] == 1


def test_a_monorepo_rooted_at_packages_counts_as_application_code(
    conn, universe, seeded
):
    """Regression, from the phase 9 qualification review.

    `bigcapitalhq/bigcapital` is a monorepo whose application lives under
    `packages/`. The collector read no application directory at the root and
    recorded application_code_exists = false, which was the single field
    keeping a candidate with a deployed conversion service and five confirmed
    dependencies out of the keep bucket. A collector defect, not a property of
    the repository.
    """
    client = full_client()
    client._listing = [entry("README.md"), entry("requirements.txt"),
                       entry("packages", "dir")]
    client._dirs = {"packages": [
        DirectoryEntry(name="server", path="packages/server", type="dir"),
        DirectoryEntry(name="webapp", path="packages/webapp", type="dir"),
    ]}
    collect(conn, universe, seeded, client)

    assert storage.get_business_evidence(conn, seeded)["application_code_exists"] == 1


def test_a_documentation_only_packages_directory_does_not_count(
    conn, universe, seeded
):
    """The other half of the fix.

    Presence of `packages/` proves nothing. A workspace holding only a docs
    site is not an application, and counting it would trade a false negative
    for a false positive.
    """
    client = full_client()
    client._listing = [entry("README.md"), entry("requirements.txt"),
                       entry("packages", "dir")]
    client._dirs = {"packages": [
        DirectoryEntry(name="docs", path="packages/docs", type="dir"),
        DirectoryEntry(name="website", path="packages/website", type="dir"),
        DirectoryEntry(name="examples", path="packages/examples", type="dir"),
    ]}
    collect(conn, universe, seeded, client)

    assert storage.get_business_evidence(conn, seeded)["application_code_exists"] == 0


def test_an_unlistable_packages_directory_does_not_count(conn, universe, seeded):
    """No listing means no verified answer, so the claim is not made."""
    client = full_client()
    client._listing = [entry("README.md"), entry("packages", "dir")]
    client._dirs = {}
    collect(conn, universe, seeded, client)

    assert storage.get_business_evidence(conn, seeded)["application_code_exists"] == 0


def test_a_packages_directory_holding_only_files_does_not_count(
    conn, universe, seeded
):
    client = full_client()
    client._listing = [entry("README.md"), entry("packages", "dir")]
    client._dirs = {"packages": [
        DirectoryEntry(name="notes.md", path="packages/notes.md", type="file"),
    ]}
    collect(conn, universe, seeded, client)

    assert storage.get_business_evidence(conn, seeded)["application_code_exists"] == 0


def test_a_plain_application_directory_needs_no_workspace_listing(
    conn, universe, seeded
):
    """The extra call is spent only where the answer hinges on it.

    `modules/` is a workspace directory that manifest discovery has no reason
    to open, so any listing of it could only have come from the workspace
    inspection. With `src/` already at the root, that inspection must not run.
    """
    client = full_client()
    client._listing = [entry("README.md"), entry("src", "dir"),
                       entry("modules", "dir")]
    collect(conn, universe, seeded, client)

    assert storage.get_business_evidence(conn, seeded)["application_code_exists"] == 1
    assert ("listing", "modules") not in client.calls


def test_a_workspace_is_inspected_when_the_answer_hinges_on_it(
    conn, universe, seeded
):
    client = full_client()
    client._listing = [entry("README.md"), entry("modules", "dir")]
    client._dirs = {"modules": [
        DirectoryEntry(name="api", path="modules/api", type="dir"),
    ]}
    collect(conn, universe, seeded, client)

    assert ("listing", "modules") in client.calls
    assert storage.get_business_evidence(conn, seeded)["application_code_exists"] == 1


def test_application_code_false_for_a_bare_script_repo(conn, universe, seeded):
    client = full_client()
    client._listing = [entry("README.md"), entry("requirements.txt"),
                       entry("examples", "dir")]
    collect(conn, universe, seeded, client)

    assert storage.get_business_evidence(conn, seeded)["application_code_exists"] == 0


def test_production_path_flag_is_set_from_where_evidence_was_found(
    conn, universe, seeded
):
    collect(conn, universe, seeded)
    business = storage.get_business_evidence(conn, seeded)

    assert business["document_functionality_in_production_code"] == 1


def test_example_only_usage_is_flagged(conn, universe, seeded):
    client = full_client()
    client._searches = {"docxtpl": SearchPage([
        CodeHit("examples/demo.py", "from docxtpl import DocxTemplate")])}
    collect(conn, universe, seeded, client)

    business = storage.get_business_evidence(conn, seeded)
    assert business["document_functionality_in_production_code"] == 0
    assert "outside production paths" in business["business_evidence_notes"]


def test_website_exists_mirrors_the_url(conn, universe, seeded):
    collect(conn, universe, seeded)

    assert storage.get_business_evidence(conn, seeded)["website_exists"] == 1


# --- evidence trail --------------------------------------------------------


def test_evidence_trail_entries_are_created(conn, universe, seeded):
    outcome, _ = collect(conn, universe, seeded)
    trail = storage.list_evidence_trail_for_candidate(conn, seeded)

    assert len(trail) >= 3
    assert outcome.evidence_entries == len(trail)
    assert all(e["evidence_url"] for e in trail)
    assert all(e["collected_at"] for e in trail)


def test_evidence_trail_covers_the_readme_claim(conn, universe, seeded):
    collect(conn, universe, seeded)
    trail = storage.list_evidence_trail_for_candidate(conn, seeded)
    readme_entries = [e for e in trail if e["evidence_type"] == "readme_excerpt"]

    assert readme_entries
    assert any("property managers" in (e["evidence_excerpt"] or "")
               for e in readme_entries)


def test_excerpts_are_short(conn, universe, seeded):
    """Section 9 asks for the specific text cited, kept short. Dumping whole
    files would make the trail unreadable without making a claim checkable."""
    client = full_client()
    client._files["README.md"] = file_at("README.md", README + "x" * 5000)
    collect(conn, universe, seeded, client)

    for row in storage.list_evidence_trail_for_candidate(conn, seeded):
        assert len(row["evidence_excerpt"] or "") <= 300


# --- API budget ------------------------------------------------------------


def test_the_collector_does_not_crawl_the_repository(conn, universe, seeded):
    """Bounded lookups, not a tree walk.

    The root listing, plus at most MAX_MANIFEST_DIR_LISTINGS looks into
    directories that exist at the root and are named somewhere a manifest
    plausibly lives. Deeper manifests are reached through code-search results
    the collector already has, not by descending.
    """
    from dependency_map.evidence import MAX_MANIFEST_DIR_LISTINGS

    _, client = collect(conn, universe, seeded)

    assert client.count("metadata") == 1
    assert client.count("listing") <= 1 + MAX_MANIFEST_DIR_LISTINGS
    assert client.count("file") <= 6
    assert client.count("search") <= 2


def test_directory_listings_are_capped(conn, universe, seeded):
    """Even a repository whose root is all likely-manifest directories only
    gets the configured number of extra listings."""
    from dependency_map.evidence import MAX_MANIFEST_DIR_LISTINGS

    client = full_client()
    client._listing = [entry("README.md")] + [
        entry(name, "dir") for name in
        ("requirements", "docker", "deploy", "deployment", "config",
         "src", "app", "server", "backend", "packages")
    ]
    collect(conn, universe, seeded, client)

    assert client.count("listing") == 1 + MAX_MANIFEST_DIR_LISTINGS


def test_code_search_is_scoped_to_the_repository(conn, universe, seeded):
    """Unscoped searches would spend the 10-per-minute budget on all of
    GitHub rather than on this candidate."""
    _, client = collect(conn, universe, seeded)
    searches = [q for k, q in client.calls if k == "search"]

    assert searches
    assert all(q.startswith("repo:clauseforge/lease-engine") for q in searches)


def test_code_search_count_is_capped(conn, run_id, universe):
    query_id = storage.create_discovery_query(
        conn, run_id=run_id, discovery_source="github_code_search",
        query="q", library_name="python-docx", discovery_tier=3)
    url = "https://github.com/a/b"
    cid = make_candidate_id(url)
    storage.insert_candidate_if_new(
        conn, candidate_id=cid, repo_url=normalize_repo_url(url),
        repo_owner="a", repo_name="b", first_seen_run_id=run_id)
    storage.insert_discovery_evidence(conn, query_id=query_id, candidate_id=cid)

    client = full_client()
    EvidenceCollector(conn, client, universe, max_code_searches=0).collect(cid)

    assert client.count("search") == 0


# --- failures --------------------------------------------------------------


def test_a_missing_manifest_does_not_abort_collection(conn, universe, seeded):
    client = FakeClient(listing=[entry("README.md")],
                        files={"README.md": file_at("README.md", README)})
    outcome, _ = collect(conn, universe, seeded, client)

    assert outcome.ok
    assert storage.get_business_evidence(conn, seeded) is not None


def test_a_failed_listing_is_recorded_as_missing(conn, universe, seeded):
    client = full_client()
    client._fail = {"listing": ApiError(500, "https://x", "boom")}
    collect(conn, universe, seeded, client)

    assert "root listing unavailable" in \
        storage.get_pipeline_evidence(conn, seeded)["pipeline_evidence_notes"]


def test_a_failed_code_search_is_noted_not_fatal(conn, universe, seeded):
    client = full_client()
    client._fail = {"search": RetriesExhausted("3 attempts failed")}
    outcome, _ = collect(conn, universe, seeded, client)

    assert outcome.ok
    assert any("code search failed" in n for n in outcome.notes)


def test_metadata_failure_propagates(conn, universe, seeded):
    """Without metadata there is no candidate record worth writing."""
    client = full_client()
    client._fail = {"metadata": ApiError(404, "https://x", "Not Found")}

    with pytest.raises(ApiError):
        collect(conn, universe, seeded, client)


def test_an_unknown_candidate_is_an_error(conn, universe):
    with pytest.raises(EvidenceError, match="No candidate"):
        EvidenceCollector(conn, full_client(), universe).collect("c_missing")


def test_batch_continues_past_a_single_failure(conn, run_id, universe, seeded):
    outcomes = collect_for_candidates(
        EvidenceCollector(conn, full_client(), universe), [seeded, "c_missing"])

    assert len(outcomes) == 2
    assert outcomes[0].ok is True
    assert outcomes[1].ok is False
    assert outcomes[1].error


def test_a_rate_limit_stops_the_batch(conn, universe, seeded):
    client = full_client()
    client._fail = {"metadata": RateLimited("budget exhausted")}

    with pytest.raises(RateLimited):
        collect_for_candidates(
            EvidenceCollector(conn, client, universe), [seeded])


# --- pending / resumability ------------------------------------------------


def test_pending_lists_candidates_without_evidence(conn, universe, seeded):
    collector = EvidenceCollector(conn, full_client(), universe)

    assert collector.pending() == [seeded]


def test_pending_excludes_completed_candidates(conn, universe, seeded):
    collector = EvidenceCollector(conn, full_client(), universe)
    collector.collect(seeded)

    assert collector.pending() == []


# --- scope and safety ------------------------------------------------------


def test_evidence_makes_no_raw_http_calls():
    source = Path("src/dependency_map/evidence.py").read_text(encoding="utf-8")

    for forbidden in ["import requests", "urllib.request", "http.client",
                      "socket", "requests.get"]:
        assert forbidden not in source


def test_evidence_does_not_qualify_or_score():
    source = Path("src/dependency_map/evidence.py").read_text(encoding="utf-8")

    for term in ["qualification_status", "final_score", "upsert_score",
                 "upsert_qualification", "def qualify", "raw_weighted_score"]:
        assert term not in source


def test_no_outreach_capability_anywhere():
    """A hard rule from the task brief, not a scoping choice."""
    source = Path("src/dependency_map/evidence.py").read_text(encoding="utf-8")

    for term in ["smtp", "sendmail", "send_email", "mailto:", "twilio", "slack"]:
        assert term not in source.lower()


def test_no_secret_appears_in_stored_evidence(conn, universe, seeded, caplog):
    caplog.set_level("DEBUG")
    collect(conn, universe, seeded)

    stored = "".join(
        str(dict(row)) for row in
        storage.list_evidence_trail_for_candidate(conn, seeded)
    )
    for pattern in ["ghp_", "github_pat_", "Authorization", "Bearer "]:
        assert pattern not in stored
        assert pattern not in caplog.text
