"""Libraries.io API client.

Two MVP operations: dependent_repositories and package info. Libraries.io is
the one source that answers "who depends on this" consistently across every
ecosystem in the library universe from a single API, which is why it is worth
a client at all (SEARCH_STRATEGY.md section 3).

Two things shape this client:

The API key travels as a query parameter rather than a header, which is unusual
and a hazard: an un-redacted URL would put the credential into the cache table,
the logs, and any exception quoting the URL. The reliability layer redacts
`api_key` everywhere, and tests here assert it.

Libraries.io does not reliably return rate-limit headers, so header-adaptive
backoff has nothing to read. Its 60-requests-per-minute limit is respected
purely through configured pacing, which makes that setting the only real
protection rather than a belt-and-braces addition.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from ..config import LIBRARIES_IO_KEY_VAR, MissingSecret
from ..reliability import LIBRARIES_IO, ReliableRequester

API_ROOT = "https://libraries.io/api"

#: Libraries.io platform names for the ecosystems in the library universe.
PLATFORMS = ("pypi", "npm", "maven", "nuget")


@dataclass(frozen=True)
class DependentRepository:
    """A repository Libraries.io reports as depending on a package."""

    full_name: str
    repo_url: str
    repo_owner: str
    repo_name: str
    host_type: str
    description: str = ""
    stars: int = 0
    primary_language: str | None = None
    is_fork: bool = False
    homepage: str | None = None

    @property
    def is_github(self) -> bool:
        """v1 is GitHub-only for follow-up evidence, per the known limitations."""
        return self.host_type.lower() == "github"


@dataclass(frozen=True)
class PackageInfo:
    name: str
    platform: str
    description: str = ""
    homepage: str | None = None
    repository_url: str | None = None
    latest_release_number: str | None = None
    stars: int = 0
    language: str | None = None


class LibrariesIOClient:
    """Thin wrapper. Importing it never requires a key; calling it does."""

    def __init__(
        self,
        requester: ReliableRequester,
        *,
        api_key: str | None = None,
        api_root: str = API_ROOT,
    ) -> None:
        self._requester = requester
        self._api_key = api_key
        self._api_root = api_root.rstrip("/")

    @property
    def has_key(self) -> bool:
        return bool(self._api_key)

    def _require_key(self) -> str:
        """Fail with a message that names the fix, not a bare KeyError.

        The key stays optional at construction time so discovery can degrade
        to GitHub-only rather than refusing to start, per the phase 3 decision
        that SEARCH_STRATEGY.md section 9 still lists obtaining one as
        unconfirmed.
        """
        if not self._api_key:
            raise MissingSecret(
                f"{LIBRARIES_IO_KEY_VAR} is not set, so Libraries.io lookups are "
                f"unavailable. Add it to .env or export it, or run discovery "
                f"against GitHub only. The value never goes into a YAML file."
            )
        return self._api_key

    def _params(self, **extra: Any) -> dict[str, Any]:
        return {"api_key": self._require_key(), **extra}

    def dependent_repositories(
        self,
        platform: str,
        name: str,
        *,
        page: int = 1,
        per_page: int = 100,
        use_cache: bool = True,
    ) -> tuple[DependentRepository, ...]:
        """Repositories declaring this package as a dependency.

        `page` is what makes the fresh-batch requirement workable here:
        SEARCH_STRATEGY.md section 7 asks for the next page on a later run
        rather than the first page again.
        """
        outcome = self._requester.get(
            f"{self._api_root}/{platform}/{name}/dependent_repositories",
            resource=LIBRARIES_IO,
            params=self._params(page=page, per_page=per_page),
            use_cache=use_cache,
        )
        body = outcome.response.json()
        if not isinstance(body, list):
            return ()
        return tuple(_parse_dependent(item) for item in body)

    def package_info(
        self, platform: str, name: str, *, use_cache: bool = True
    ) -> PackageInfo:
        """Basic metadata for one package."""
        outcome = self._requester.get(
            f"{self._api_root}/{platform}/{name}",
            resource=LIBRARIES_IO,
            params=self._params(),
            use_cache=use_cache,
        )
        return _parse_package(outcome.response.json(), platform=platform, name=name)


# --- parsing ---------------------------------------------------------------


def _owner_and_name(full_name: str) -> tuple[str, str]:
    owner, _, name = full_name.partition("/")
    return owner, name


def _parse_dependent(item: Mapping[str, Any]) -> DependentRepository:
    full_name = item.get("full_name", "") or ""
    owner, name = _owner_and_name(full_name)
    host_type = item.get("host_type", "GitHub") or "GitHub"

    repo_url = item.get("repository_url") or ""
    if not repo_url and full_name and host_type.lower() == "github":
        repo_url = f"https://github.com/{full_name}"

    return DependentRepository(
        full_name=full_name,
        repo_url=repo_url,
        repo_owner=owner,
        repo_name=name,
        host_type=host_type,
        description=item.get("description") or "",
        stars=int(item.get("stargazers_count", 0) or 0),
        primary_language=item.get("language"),
        is_fork=bool(item.get("fork", False)),
        homepage=item.get("homepage") or None,
    )


def _parse_package(
    body: Mapping[str, Any], *, platform: str, name: str
) -> PackageInfo:
    if not isinstance(body, Mapping):
        return PackageInfo(name=name, platform=platform)
    return PackageInfo(
        name=body.get("name", name) or name,
        platform=body.get("platform", platform) or platform,
        description=body.get("description") or "",
        homepage=body.get("homepage") or None,
        repository_url=body.get("repository_url") or None,
        latest_release_number=body.get("latest_release_number") or None,
        stars=int(body.get("stars", 0) or 0),
        language=body.get("language"),
    )
