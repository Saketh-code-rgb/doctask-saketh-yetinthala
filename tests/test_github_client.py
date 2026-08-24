"""GitHub client parsing, headers, and error conversion.

All responses are fixtures shaped like real GitHub payloads. No test touches
the network.
"""

from __future__ import annotations

import base64
import json
from pathlib import Path

import pytest

from dependency_map.clients.github_client import (
    API_VERSION,
    MAX_SEARCH_RESULTS,
    GitHubClient,
)
from dependency_map.reliability import (
    GITHUB_CODE_SEARCH,
    GITHUB_CORE,
    GITHUB_SEARCH,
    ApiError,
    HttpResponse,
    MemoryCacheStore,
    ReliabilityPolicy,
    ReliableRequester,
    RetriesExhausted,
)

FAKE_TOKEN = "ghp_fake000000000000000000000000000000"


class FakeTransport:
    def __init__(self, *responses):
        self._queue = list(responses)
        self.calls: list[dict] = []

    def request(self, method, url, *, params=None, headers=None, timeout=30.0):
        self.calls.append({"method": method, "url": url,
                           "params": dict(params or {}),
                           "headers": dict(headers or {})})
        item = self._queue.pop(0)
        if isinstance(item, Exception):
            raise item
        return item

    @property
    def call_count(self):
        return len(self.calls)


def response(payload, status=200):
    text = payload if isinstance(payload, str) else json.dumps(payload)
    return HttpResponse(status=status, headers={}, text=text, url="https://api.github.com/x")


def make_client(*responses, token=FAKE_TOKEN):
    transport = FakeTransport(*responses)
    policy = ReliabilityPolicy(
        intervals={GITHUB_CODE_SEARCH: 0.0, GITHUB_SEARCH: 0.0, GITHUB_CORE: 0.0},
        max_attempts=3, backoff_base_seconds=0.0, backoff_jitter_seconds=0.0,
    )
    requester = ReliableRequester(
        transport, policy, cache=MemoryCacheStore(), sleep=lambda s: None,
    )
    return GitHubClient(requester, token=token), transport


# --- fixtures --------------------------------------------------------------

CODE_SEARCH_PAYLOAD = {
    "total_count": 2,
    "incomplete_results": False,
    "items": [
        {
            "name": "requirements.txt",
            "path": "app/requirements.txt",
            "sha": "abc123",
            "html_url": "https://github.com/clauseforge-io/lease-engine/blob/main/app/requirements.txt",
            "repository": {
                "full_name": "clauseforge-io/lease-engine",
                "html_url": "https://github.com/clauseforge-io/lease-engine",
            },
            "text_matches": [
                {"fragment": "docxtpl==0.16.7\nreportlab==4.0.4", "property": "content"}
            ],
        },
        {
            "name": "requirements.txt",
            "path": "requirements.txt",
            "sha": "def456",
            "html_url": "https://github.com/other-org/reports/blob/main/requirements.txt",
            "repository": {
                "full_name": "other-org/reports",
                "html_url": "https://github.com/other-org/reports",
            },
        },
    ],
}

REPO_SEARCH_PAYLOAD = {
    "total_count": 1,
    "incomplete_results": False,
    "items": [
        {
            "full_name": "clauseforge-io/lease-engine",
            "html_url": "https://github.com/clauseforge-io/lease-engine",
            "description": "Lease agreement automation",
            "stargazers_count": 41,
            "language": "Python",
        }
    ],
}

REPO_PAYLOAD = {
    "full_name": "clauseforge-io/lease-engine",
    "name": "lease-engine",
    "owner": {"login": "clauseforge-io"},
    "html_url": "https://github.com/clauseforge-io/lease-engine",
    "fork": False,
    "archived": False,
    "language": "Python",
    "stargazers_count": 41,
    "forks_count": 7,
    "description": "Lease agreement automation",
    "homepage": "https://clauseforge.example.com",
    "default_branch": "main",
    "pushed_at": "2026-07-30T11:02:00Z",
    "created_at": "2024-01-05T09:00:00Z",
    "open_issues_count": 3,
}


def file_payload(text="from docxtpl import DocxTemplate\n"):
    return {
        "path": "app/documents/lease_builder.py",
        "sha": "f00d",
        "size": len(text),
        "encoding": "base64",
        "content": base64.b64encode(text.encode()).decode(),
        "html_url": "https://github.com/clauseforge-io/lease-engine/blob/main/app/documents/lease_builder.py",
    }


# --- code search -----------------------------------------------------------


def test_code_search_parses_results():
    client, _ = make_client(response(CODE_SEARCH_PAYLOAD))

    page = client.search_code('"docxtpl" filename:requirements.txt')

    assert page.total_count == 2
    assert len(page.results) == 2

    first = page.results[0]
    assert first.repo_full_name == "clauseforge-io/lease-engine"
    assert first.repo_owner == "clauseforge-io"
    assert first.repo_name == "lease-engine"
    assert first.path == "app/requirements.txt"
    assert first.sha == "abc123"


def test_code_search_preserves_query_and_rank():
    """CANDIDATE_SCHEMA.md section 3 needs both recorded per hit."""
    query = '"docxtpl" filename:requirements.txt'
    client, _ = make_client(response(CODE_SEARCH_PAYLOAD))

    page = client.search_code(query)

    assert [r.rank for r in page.results] == [1, 2]
    assert all(r.query == query for r in page.results)


def test_code_search_rank_accounts_for_pagination():
    client, _ = make_client(response(CODE_SEARCH_PAYLOAD))

    page = client.search_code("q", per_page=30, page=3)

    assert [r.rank for r in page.results] == [61, 62]


def test_code_search_captures_the_evidence_permalink():
    """SEARCH_STRATEGY.md section 6 wants a permalink to the actual snippet,
    not just the manifest line."""
    client, _ = make_client(response(CODE_SEARCH_PAYLOAD))

    first = client.search_code("q").results[0]

    assert first.evidence_url.startswith("https://github.com/clauseforge-io/")
    assert "app/requirements.txt" in first.evidence_url


def test_code_search_captures_text_match_excerpts():
    client, _ = make_client(response(CODE_SEARCH_PAYLOAD))

    results = client.search_code("q").results

    assert "docxtpl==0.16.7" in results[0].excerpt
    assert results[1].excerpt == "", "no text_matches means no excerpt, not a crash"


def test_code_search_requests_the_text_match_media_type():
    client, transport = make_client(response(CODE_SEARCH_PAYLOAD))

    client.search_code("q")

    assert transport.calls[0]["headers"]["Accept"] == \
        "application/vnd.github.text-match+json"


def test_code_search_uses_the_code_search_bucket():
    client, transport = make_client(response(CODE_SEARCH_PAYLOAD))
    client.search_code("q")

    assert transport.calls[0]["url"].endswith("/search/code")


def test_code_search_requires_a_token():
    """Authentication has been mandatory for code search since April 2023."""
    client, transport = make_client(response(CODE_SEARCH_PAYLOAD), token=None)

    with pytest.raises(ApiError, match="requires authentication"):
        client.search_code("q")

    assert transport.call_count == 0, "should fail before spending a request"


def test_code_search_caps_per_page_at_one_hundred():
    client, transport = make_client(response(CODE_SEARCH_PAYLOAD))

    client.search_code("q", per_page=500)

    assert transport.calls[0]["params"]["per_page"] == 100


def test_search_page_flags_the_thousand_result_cap():
    """GitHub returns at most 1,000 results however you paginate, so a broad
    query undercounts. Worth surfacing rather than hiding."""
    payload = {**CODE_SEARCH_PAYLOAD, "total_count": 5000}
    client, _ = make_client(response(payload))

    page = client.search_code("python-docx")

    assert page.total_count == 5000
    assert page.capped is True
    assert MAX_SEARCH_RESULTS == 1000


def test_search_page_not_capped_for_small_totals():
    client, _ = make_client(response(CODE_SEARCH_PAYLOAD))
    assert client.search_code("q").capped is False


def test_empty_code_search_results():
    client, _ = make_client(response({"total_count": 0, "items": []}))

    page = client.search_code("nothing")

    assert page.results == ()
    assert page.total_count == 0


# --- repository search -----------------------------------------------------


def test_repository_search_parses_results():
    client, _ = make_client(response(REPO_SEARCH_PAYLOAD))

    page = client.search_repositories("contract automation platform")
    first = page.results[0]

    assert first.full_name == "clauseforge-io/lease-engine"
    assert first.stars == 41
    assert first.primary_language == "Python"
    assert first.rank == 1


def test_repository_search_uses_a_different_endpoint_than_code_search():
    client, transport = make_client(response(REPO_SEARCH_PAYLOAD))

    client.search_repositories("q")

    assert transport.calls[0]["url"].endswith("/search/repositories")


def test_repository_search_passes_sort_when_given():
    """SEARCH_STRATEGY.md section 7 rotates sort order between runs."""
    client, transport = make_client(response(REPO_SEARCH_PAYLOAD))

    client.search_repositories("q", sort="updated")

    assert transport.calls[0]["params"]["sort"] == "updated"


def test_repository_search_omits_sort_when_not_given():
    client, transport = make_client(response(REPO_SEARCH_PAYLOAD))

    client.search_repositories("q")

    assert "sort" not in transport.calls[0]["params"]


# --- repository metadata ---------------------------------------------------


def test_repository_metadata_parses():
    client, _ = make_client(response(REPO_PAYLOAD))

    repo = client.get_repository("clauseforge-io", "lease-engine")

    assert repo.full_name == "clauseforge-io/lease-engine"
    assert repo.repo_owner == "clauseforge-io"
    assert repo.is_fork is False
    assert repo.is_archived is False
    assert repo.primary_language == "Python"
    assert repo.stars == 41
    assert repo.forks == 7
    assert repo.homepage == "https://clauseforge.example.com"
    assert repo.default_branch == "main"


def test_repository_metadata_exposes_last_commit_date():
    """business_evidence stores a date, not a timestamp."""
    client, _ = make_client(response(REPO_PAYLOAD))

    assert client.get_repository("a", "b").last_commit_date == "2026-07-30"


def test_repository_metadata_handles_nulls():
    payload = {**REPO_PAYLOAD, "language": None, "homepage": None,
               "description": None, "pushed_at": None}
    client, _ = make_client(response(payload))

    repo = client.get_repository("a", "b")

    assert repo.primary_language is None
    assert repo.homepage is None
    assert repo.description == ""
    assert repo.last_commit_date is None


def test_fork_and_archived_flags_are_carried_through():
    payload = {**REPO_PAYLOAD, "fork": True, "archived": True}
    client, _ = make_client(response(payload))

    repo = client.get_repository("a", "b")

    assert repo.is_fork is True
    assert repo.is_archived is True


def test_repository_metadata_uses_the_core_bucket_not_code_search():
    client, transport = make_client(response(REPO_PAYLOAD))

    client.get_repository("a", "b")

    assert "/search/" not in transport.calls[0]["url"]
    assert transport.calls[0]["url"].endswith("/repos/a/b")


# --- file contents ---------------------------------------------------------


def test_file_contents_are_base64_decoded():
    client, _ = make_client(response(file_payload()))

    contents = client.get_file_contents("clauseforge-io", "lease-engine",
                                        "app/documents/lease_builder.py")

    assert contents.text == "from docxtpl import DocxTemplate\n"
    assert contents.sha == "f00d"
    assert contents.path == "app/documents/lease_builder.py"


def test_file_contents_expose_lines():
    client, _ = make_client(response(file_payload("a\nb\nc\n")))

    assert client.get_file_contents("a", "b", "f.py").lines == ["a", "b", "c"]


def test_file_contents_carry_a_permalink():
    client, _ = make_client(response(file_payload()))

    contents = client.get_file_contents("a", "b", "f.py")

    assert contents.evidence_url.startswith("https://github.com/")


def test_file_contents_pass_a_ref_when_given():
    client, transport = make_client(response(file_payload()))

    client.get_file_contents("a", "b", "f.py", ref="abc123")

    assert transport.calls[0]["params"]["ref"] == "abc123"


def test_requesting_a_directory_is_an_error():
    client, _ = make_client(response([{"name": "a.py"}, {"name": "b.py"}]))

    with pytest.raises(ApiError, match="directory"):
        client.get_file_contents("a", "b", "app")


def test_undecodable_content_does_not_crash():
    payload = {**file_payload(), "content": "!!!not base64!!!"}
    client, _ = make_client(response(payload))

    assert client.get_file_contents("a", "b", "f.py").text == ""


# --- headers and auth ------------------------------------------------------


def test_authenticated_requests_send_a_bearer_token():
    client, transport = make_client(response(REPO_PAYLOAD))

    client.get_repository("a", "b")

    assert transport.calls[0]["headers"]["Authorization"] == f"Bearer {FAKE_TOKEN}"


def test_api_version_header_is_pinned():
    client, transport = make_client(response(REPO_PAYLOAD))

    client.get_repository("a", "b")

    assert transport.calls[0]["headers"]["X-GitHub-Api-Version"] == API_VERSION


def test_unauthenticated_client_sends_no_authorization_header():
    client, transport = make_client(response(REPO_PAYLOAD), token=None)

    client.get_repository("a", "b")

    assert "Authorization" not in transport.calls[0]["headers"]
    assert client.is_authenticated is False


def test_token_is_never_a_query_parameter():
    """A token in the query string would land in the cache key and the URL."""
    client, transport = make_client(response(REPO_PAYLOAD))

    client.get_repository("a", "b")

    assert FAKE_TOKEN not in json.dumps(transport.calls[0]["params"])
    assert FAKE_TOKEN not in transport.calls[0]["url"]


def test_token_is_not_written_into_the_cache():
    transport = FakeTransport(response(REPO_PAYLOAD))
    cache = MemoryCacheStore()
    policy = ReliabilityPolicy(intervals={GITHUB_CORE: 0.0}, max_attempts=1)
    requester = ReliableRequester(transport, policy, cache=cache, sleep=lambda s: None)

    GitHubClient(requester, token=FAKE_TOKEN).get_repository("a", "b")

    stored = "".join(k + v[0] for k, v in cache._entries.items())
    assert FAKE_TOKEN not in stored


def test_token_does_not_appear_in_logs(caplog):
    caplog.set_level("DEBUG")
    client, _ = make_client(response(REPO_PAYLOAD), response(REPO_PAYLOAD))

    client.get_repository("a", "b")
    client.get_repository("a", "b")

    assert FAKE_TOKEN not in caplog.text


def test_token_does_not_appear_in_exceptions():
    client, _ = make_client(response({"message": "Bad credentials"}, status=401))

    with pytest.raises(ApiError) as excinfo:
        client.get_repository("a", "b")

    assert FAKE_TOKEN not in str(excinfo.value)


# --- error conversion ------------------------------------------------------


def test_404_becomes_an_api_error():
    client, _ = make_client(response({"message": "Not Found"}, status=404))

    with pytest.raises(ApiError) as excinfo:
        client.get_repository("ghost", "repo")

    assert excinfo.value.status == 404


def test_repeated_5xx_becomes_retries_exhausted():
    client, _ = make_client(*[response("oops", status=500) for _ in range(3)])

    with pytest.raises(RetriesExhausted):
        client.get_repository("a", "b")


def test_non_json_response_is_reported_clearly():
    client, _ = make_client(response("<html>gateway</html>"))

    with pytest.raises(ApiError, match="not JSON"):
        client.get_repository("a", "b")


# --- no judgment in the client ---------------------------------------------


def test_the_client_makes_no_qualification_judgments():
    """Deciding whether a repository is a good prospect belongs to the
    qualification engine, which reads stored evidence and calls no APIs."""
    source = Path("src/dependency_map/clients/github_client.py").read_text(
        encoding="utf-8"
    )

    for term in ["qualification_status", "def qualify", "keep", "reject",
                 "final_score", "is_good_prospect"]:
        assert term not in source, f"{term!r} suggests judgment leaking into the client"
