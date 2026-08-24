"""Thin wrappers around the external APIs.

Each client handles authentication, request shaping, and turning a response
into typed results. Pacing, retries, backoff, rate-limit handling and caching
all live in the shared reliability layer instead of being repeated per client
(TECHNICAL_DESIGN.md section 6).

No client judges a repository. Deciding whether something is a good prospect
belongs to the qualification engine, which reads stored evidence rather than
calling APIs at all.
"""

from .github_client import (
    CodeSearchResult,
    FileContents,
    GitHubClient,
    RepositoryMetadata,
    RepositorySearchResult,
)
from .libraries_io_client import (
    DependentRepository,
    LibrariesIOClient,
    PackageInfo,
)

__all__ = [
    "GitHubClient",
    "CodeSearchResult",
    "RepositorySearchResult",
    "RepositoryMetadata",
    "FileContents",
    "LibrariesIOClient",
    "DependentRepository",
    "PackageInfo",
]
