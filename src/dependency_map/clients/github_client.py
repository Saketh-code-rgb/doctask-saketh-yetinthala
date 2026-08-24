"""GitHub API client.

Four MVP operations: code search, repository search, repository metadata, and
file contents. Dependents-page fetching is deliberately absent, deferred with
the rest of the "Later" list in TECHNICAL_DESIGN.md section 22.

Each operation names the rate-limit bucket it spends from, so the reliability
layer paces it correctly. Code search is the tight one at 10 requests per
minute; repository metadata and file contents come from the core REST budget of
5,000 per hour and must not be slowed to code search's pace.

Results are typed and carry the metadata later phases need to record evidence:
the query that produced them, the result's rank, the repository URL, the file
path, and a permalink to the exact line.
"""

from __future__ import annotations

import base64
from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from ..reliability import (
    GITHUB_CODE_SEARCH,
    GITHUB_CORE,
    GITHUB_SEARCH,
    ApiError,
    ReliableRequester,
)

API_ROOT = "https://api.github.com"

#: Pinned so a future default change on GitHub's side can't quietly alter
#: response shapes underneath us.
API_VERSION = "2022-11-28"

#: The text-match media type returns the matching fragments alongside each
#: result, which is what makes an evidence excerpt possible without a second
#: fetch of the whole file.
TEXT_MATCH_ACCEPT = "application/vnd.github.text-match+json"
JSON_ACCEPT = "application/vnd.github+json"

#: GitHub caps any single search at 1,000 results however you paginate, so a
#: broad query undercounts. SEARCH_STRATEGY.md section 9 records this as a
#: known limitation to be handled by slicing queries, not by paging further.
MAX_SEARCH_RESULTS = 1000
MAX_PER_PAGE = 100


@dataclass(frozen=True)
class TextMatch:
    """One matching fragment from a code search hit."""

    fragment: str
    property_name: str = ""


@dataclass(frozen=True)
class CodeSearchResult:
    """One file matching a code search.

    Carries everything CANDIDATE_SCHEMA.md sections 3 and 4 need recorded:
    which query found it, where it ranked, the repository, the path, and a
    permalink to the specific file.
    """

    repo_full_name: str
    repo_url: str
    repo_owner: str
    repo_name: str
    path: str
    evidence_url: str
    sha: str
    query: str
    rank: int
    text_matches: tuple[TextMatch, ...] = ()

    @property
    def excerpt(self) -> str:
        """The first matching fragment, for use as an evidence excerpt."""
        return self.text_matches[0].fragment if self.text_matches else ""


@dataclass(frozen=True)
class RepositorySearchResult:
    full_name: str
    repo_url: str
    repo_owner: str
    repo_name: str
    description: str
    stars: int
    primary_language: str | None
    query: str
    rank: int


@dataclass(frozen=True)
class RepositoryMetadata:
    """Raw repository facts, straight from the API, with no judgment applied."""

    full_name: str
    repo_url: str
    repo_owner: str
    repo_name: str
    is_fork: bool
    is_archived: bool
    primary_language: str | None
    stars: int
    forks: int
    description: str
    homepage: str | None
    default_branch: str
    pushed_at: str | None
    created_at: str | None
    open_issues: int = 0

    @property
    def last_commit_date(self) -> str | None:
        """`pushed_at` as a plain date, matching business_evidence."""
        return self.pushed_at.split("T")[0] if self.pushed_at else None


@dataclass(frozen=True)
class DirectoryEntry:
    """One entry in a directory listing. No file content is fetched."""

    name: str
    path: str
    type: str  # "file" or "dir"
    size: int = 0
    html_url: str = ""

    @property
    def is_dir(self) -> bool:
        return self.type == "dir"


@dataclass(frozen=True)
class FileContents:
    path: str
    text: str
    sha: str
    size: int
    evidence_url: str
    repo_full_name: str = ""

    @property
    def lines(self) -> list[str]:
        return self.text.splitlines()


@dataclass(frozen=True)
class SearchPage:
    """A page of search results plus what the API said about the total."""

    results: tuple[Any, ...]
    total_count: int
    incomplete_results: bool = False
    query: str = ""

    @property
    def capped(self) -> bool:
        """True when the true total exceeds what any pagination can reach."""
        return self.total_count > MAX_SEARCH_RESULTS


class GitHubClient:
    """Authentication, request shaping, and typed results. Nothing else."""

    def __init__(
        self,
        requester: ReliableRequester,
        *,
        token: str | None = None,
        api_root: str = API_ROOT,
    ) -> None:
        self._requester = requester
        self._token = token
        self._api_root = api_root.rstrip("/")

    # -- headers ------------------------------------------------------------

    def _headers(self, accept: str = JSON_ACCEPT) -> dict[str, str]:
        """Build request headers.

        The token goes here and nowhere else. It is never a query parameter, so
        it cannot reach a cache key or a stored URL, and nothing in this module
        logs a header dict.
        """
        headers = {
            "Accept": accept,
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "dependency-map",
        }
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        return headers

    @property
    def is_authenticated(self) -> bool:
        return bool(self._token)

    # -- code search --------------------------------------------------------

    def search_code(
        self,
        query: str,
        *,
        per_page: int = 30,
        page: int = 1,
        use_cache: bool = True,
    ) -> SearchPage:
        """Search file contents across public repositories.

        Spends from the code-search bucket: 10 requests per minute, separate
        from every other GitHub limit, and authentication is mandatory.
        """
        if not self._token:
            raise ApiError(
                401,
                f"{self._api_root}/search/code",
                "GitHub code search requires authentication. Set GITHUB_TOKEN.",
            )

        outcome = self._requester.get(
            f"{self._api_root}/search/code",
            resource=GITHUB_CODE_SEARCH,
            params={"q": query, "per_page": min(per_page, MAX_PER_PAGE), "page": page},
            headers=self._headers(TEXT_MATCH_ACCEPT),
            use_cache=use_cache,
        )
        body = outcome.response.json()
        offset = (page - 1) * per_page

        results = tuple(
            _parse_code_hit(item, query=query, rank=offset + index + 1)
            for index, item in enumerate(body.get("items", []))
        )
        return SearchPage(
            results=results,
            total_count=int(body.get("total_count", 0)),
            incomplete_results=bool(body.get("incomplete_results", False)),
            query=query,
        )

    # -- repository search --------------------------------------------------

    def search_repositories(
        self,
        query: str,
        *,
        per_page: int = 30,
        page: int = 1,
        sort: str | None = None,
        use_cache: bool = True,
    ) -> SearchPage:
        """Search repository names, descriptions and topics.

        A different bucket from code search: 30 requests per minute. Listed in
        SEARCH_STRATEGY.md section 3 as a secondary, lower-precision channel.
        """
        params: dict[str, Any] = {
            "q": query,
            "per_page": min(per_page, MAX_PER_PAGE),
            "page": page,
        }
        if sort:
            params["sort"] = sort

        outcome = self._requester.get(
            f"{self._api_root}/search/repositories",
            resource=GITHUB_SEARCH,
            params=params,
            headers=self._headers(),
            use_cache=use_cache,
        )
        body = outcome.response.json()
        offset = (page - 1) * per_page

        results = tuple(
            _parse_repo_hit(item, query=query, rank=offset + index + 1)
            for index, item in enumerate(body.get("items", []))
        )
        return SearchPage(
            results=results,
            total_count=int(body.get("total_count", 0)),
            incomplete_results=bool(body.get("incomplete_results", False)),
            query=query,
        )

    # -- repository metadata ------------------------------------------------

    def get_repository(
        self, owner: str, repo: str, *, use_cache: bool = True
    ) -> RepositoryMetadata:
        """Fetch repository metadata from the core REST budget."""
        outcome = self._requester.get(
            f"{self._api_root}/repos/{owner}/{repo}",
            resource=GITHUB_CORE,
            headers=self._headers(),
            use_cache=use_cache,
        )
        return _parse_repository(outcome.response.json())

    # -- file contents ------------------------------------------------------

    def get_file_contents(
        self,
        owner: str,
        repo: str,
        path: str,
        *,
        ref: str | None = None,
        use_cache: bool = True,
    ) -> FileContents:
        """Fetch and decode one file.

        The contents endpoint returns base64, so decoding happens here rather
        than leaking an encoding detail into every caller.
        """
        params = {"ref": ref} if ref else None
        outcome = self._requester.get(
            f"{self._api_root}/repos/{owner}/{repo}/contents/{path}",
            resource=GITHUB_CORE,
            params=params,
            headers=self._headers(),
            use_cache=use_cache,
        )
        body = outcome.response.json()

        if isinstance(body, list):
            raise ApiError(
                200,
                f"{self._api_root}/repos/{owner}/{repo}/contents/{path}",
                f"{path} is a directory, not a file",
            )

        return FileContents(
            path=body.get("path", path),
            text=_decode_content(body),
            sha=body.get("sha", ""),
            size=int(body.get("size", 0)),
            evidence_url=body.get("html_url", "") or "",
            repo_full_name=f"{owner}/{repo}",
        )

    def list_commits(
        self,
        owner: str,
        repo: str,
        *,
        since: str | None = None,
        per_page: int = 100,
        use_cache: bool = True,
    ) -> tuple["CommitSummary", ...]:
        """Recent commit metadata for one repository, one page only.

        Used solely to corroborate SCORING_MODEL.md section 7 rung 4. One page
        is deliberate: the rubric asks whether the document code kept being
        modified, which a bounded recent window answers, and paging through a
        full history would spend the core budget on detail nothing reads.
        """
        params: dict[str, object] = {"per_page": min(per_page, MAX_PER_PAGE)}
        if since:
            params["since"] = since
        outcome = self._requester.get(
            f"{self._api_root}/repos/{owner}/{repo}/commits",
            resource=GITHUB_CORE,
            params=params,
            headers=self._headers(),
            use_cache=use_cache,
        )
        body = outcome.response.json()
        if not isinstance(body, list):
            return ()
        return tuple(_parse_commit(item) for item in body)

    def list_directory(
        self,
        owner: str,
        repo: str,
        path: str = "",
        *,
        ref: str | None = None,
        use_cache: bool = True,
    ) -> tuple[DirectoryEntry, ...]:
        """List one directory, without downloading any file in it.

        Same contents endpoint as get_file_contents, which returns a listing
        rather than a blob when the path is a directory. Spends from the core
        REST budget of 5,000 per hour, which matters: answering "is there a
        templates/ directory" through code search instead would cost from the
        10-per-minute bucket and be roughly nine times slower for a worse
        answer.
        """
        params = {"ref": ref} if ref else None
        outcome = self._requester.get(
            f"{self._api_root}/repos/{owner}/{repo}/contents/{path}".rstrip("/"),
            resource=GITHUB_CORE,
            params=params,
            headers=self._headers(),
            use_cache=use_cache,
        )
        body = outcome.response.json()
        if not isinstance(body, list):
            return ()
        return tuple(
            DirectoryEntry(
                name=item.get("name", "") or "",
                path=item.get("path", "") or "",
                type=item.get("type", "") or "",
                size=int(item.get("size", 0) or 0),
                html_url=item.get("html_url", "") or "",
            )
            for item in body
        )


# --- parsing ---------------------------------------------------------------


def _decode_content(body: Mapping[str, Any]) -> str:
    encoding = body.get("encoding", "base64")
    raw = body.get("content", "") or ""
    if encoding != "base64":
        return str(raw)
    try:
        return base64.b64decode(raw).decode("utf-8", errors="replace")
    except (ValueError, TypeError):
        return ""


def _owner_and_name(full_name: str) -> tuple[str, str]:
    owner, _, name = full_name.partition("/")
    return owner, name


def _parse_code_hit(item: Mapping[str, Any], *, query: str, rank: int) -> CodeSearchResult:
    repository = item.get("repository", {}) or {}
    full_name = repository.get("full_name", "") or ""
    owner, name = _owner_and_name(full_name)

    matches = tuple(
        TextMatch(
            fragment=match.get("fragment", "") or "",
            property_name=match.get("property", "") or "",
        )
        for match in item.get("text_matches", []) or []
    )

    return CodeSearchResult(
        repo_full_name=full_name,
        repo_url=repository.get("html_url", "") or f"https://github.com/{full_name}",
        repo_owner=owner,
        repo_name=name,
        path=item.get("path", "") or "",
        evidence_url=item.get("html_url", "") or "",
        sha=item.get("sha", "") or "",
        query=query,
        rank=rank,
        text_matches=matches,
    )


def _parse_repo_hit(
    item: Mapping[str, Any], *, query: str, rank: int
) -> RepositorySearchResult:
    full_name = item.get("full_name", "") or ""
    owner, name = _owner_and_name(full_name)
    return RepositorySearchResult(
        full_name=full_name,
        repo_url=item.get("html_url", "") or f"https://github.com/{full_name}",
        repo_owner=owner,
        repo_name=name,
        description=item.get("description") or "",
        stars=int(item.get("stargazers_count", 0) or 0),
        primary_language=item.get("language"),
        query=query,
        rank=rank,
    )


def _parse_repository(body: Mapping[str, Any]) -> RepositoryMetadata:
    full_name = body.get("full_name", "") or ""
    owner_field = body.get("owner") or {}
    owner = owner_field.get("login") or _owner_and_name(full_name)[0]
    return RepositoryMetadata(
        full_name=full_name,
        repo_url=body.get("html_url", "") or f"https://github.com/{full_name}",
        repo_owner=owner,
        repo_name=body.get("name", "") or _owner_and_name(full_name)[1],
        is_fork=bool(body.get("fork", False)),
        is_archived=bool(body.get("archived", False)),
        primary_language=body.get("language"),
        stars=int(body.get("stargazers_count", 0) or 0),
        forks=int(body.get("forks_count", 0) or 0),
        description=body.get("description") or "",
        homepage=body.get("homepage") or None,
        default_branch=body.get("default_branch", "main") or "main",
        pushed_at=body.get("pushed_at"),
        created_at=body.get("created_at"),
        open_issues=int(body.get("open_issues_count", 0) or 0),
    )


@dataclass(frozen=True)
class CommitSummary:
    """The little of a commit this project needs.

    Deliberately not the commit contents. SCORING_MODEL.md section 7 uses
    history only to corroborate rung 4's "repeated modification"; fetching
    diffs would spend budget on detail the rubric never reads.
    """

    sha: str
    author: str | None
    committed_at: str | None
    message_summary: str


def _parse_commit(item: dict) -> CommitSummary:
    commit = item.get("commit") or {}
    author_block = item.get("author") or {}
    committer = commit.get("author") or {}
    login = author_block.get("login") or committer.get("email")
    return CommitSummary(
        sha=item.get("sha", ""),
        author=login,
        committed_at=committer.get("date"),
        message_summary=(commit.get("message") or "").splitlines()[0][:120]
        if commit.get("message") else "",
    )
