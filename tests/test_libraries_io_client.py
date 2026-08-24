"""Libraries.io client parsing, key handling, and error behaviour.

All responses are fixtures shaped like real Libraries.io payloads. No test
touches the network, and no test needs a real key.
"""

from __future__ import annotations

import json

import pytest

from dependency_map.clients.libraries_io_client import LibrariesIOClient
from dependency_map.config import MissingSecret
from dependency_map.reliability import (
    LIBRARIES_IO,
    ApiError,
    HttpResponse,
    MemoryCacheStore,
    ReliabilityPolicy,
    ReliableRequester,
    RetriesExhausted,
)

FAKE_KEY = "libio_fake_key_00000"


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
    return HttpResponse(status=status, headers={}, text=text,
                        url="https://libraries.io/api/x")


def make_client(*responses, api_key=FAKE_KEY, cache=None):
    transport = FakeTransport(*responses)
    policy = ReliabilityPolicy(
        intervals={LIBRARIES_IO: 0.0}, max_attempts=3,
        backoff_base_seconds=0.0, backoff_jitter_seconds=0.0,
    )
    requester = ReliableRequester(
        transport, policy, cache=cache or MemoryCacheStore(), sleep=lambda s: None,
    )
    return LibrariesIOClient(requester, api_key=api_key), transport


DEPENDENTS_PAYLOAD = [
    {
        "full_name": "clauseforge-io/lease-engine",
        "host_type": "GitHub",
        "description": "Lease agreement automation",
        "stargazers_count": 41,
        "language": "Python",
        "fork": False,
        "homepage": "https://clauseforge.example.com",
    },
    {
        "full_name": "someone/tutorial-fork",
        "host_type": "GitHub",
        "description": "",
        "stargazers_count": 0,
        "language": "Python",
        "fork": True,
    },
]

PACKAGE_PAYLOAD = {
    "name": "docxtpl",
    "platform": "Pypi",
    "description": "Python docx template engine",
    "homepage": "https://github.com/elapouya/python-docx-template",
    "repository_url": "https://github.com/elapouya/python-docx-template",
    "latest_release_number": "0.16.7",
    "stars": 1800,
    "language": "Python",
}


# --- dependent_repositories ------------------------------------------------


def test_dependent_repositories_parses():
    client, _ = make_client(response(DEPENDENTS_PAYLOAD))

    dependents = client.dependent_repositories("pypi", "docxtpl")

    assert len(dependents) == 2
    first = dependents[0]
    assert first.full_name == "clauseforge-io/lease-engine"
    assert first.repo_owner == "clauseforge-io"
    assert first.repo_name == "lease-engine"
    assert first.stars == 41
    assert first.primary_language == "Python"
    assert first.is_fork is False


def test_dependent_repositories_builds_a_github_url():
    client, _ = make_client(response(DEPENDENTS_PAYLOAD))

    first = client.dependent_repositories("pypi", "docxtpl")[0]

    assert first.repo_url == "https://github.com/clauseforge-io/lease-engine"
    assert first.is_github is True


def test_dependent_repositories_prefers_an_explicit_repository_url():
    payload = [{**DEPENDENTS_PAYLOAD[0],
                "repository_url": "https://github.com/other/name"}]
    client, _ = make_client(response(payload))

    assert client.dependent_repositories("pypi", "x")[0].repo_url == \
        "https://github.com/other/name"


def test_non_github_hosts_are_flagged():
    """v1 is GitHub-only for follow-up evidence, a known limitation."""
    payload = [{**DEPENDENTS_PAYLOAD[0], "host_type": "GitLab"}]
    client, _ = make_client(response(payload))

    assert client.dependent_repositories("pypi", "x")[0].is_github is False


def test_fork_flag_is_carried_through():
    client, _ = make_client(response(DEPENDENTS_PAYLOAD))

    assert client.dependent_repositories("pypi", "docxtpl")[1].is_fork is True


def test_dependent_repositories_hits_the_right_endpoint():
    client, transport = make_client(response(DEPENDENTS_PAYLOAD))

    client.dependent_repositories("pypi", "docxtpl")

    assert transport.calls[0]["url"].endswith("/pypi/docxtpl/dependent_repositories")


def test_dependent_repositories_supports_paging():
    """SEARCH_STRATEGY.md section 7: a later run asks for the next page rather
    than the first page again."""
    client, transport = make_client(response(DEPENDENTS_PAYLOAD))

    client.dependent_repositories("pypi", "docxtpl", page=3)

    assert transport.calls[0]["params"]["page"] == 3


def test_empty_dependents_list():
    client, _ = make_client(response([]))

    assert client.dependent_repositories("pypi", "unused") == ()


def test_unexpected_shape_returns_empty_rather_than_crashing():
    client, _ = make_client(response({"error": "something"}))

    assert client.dependent_repositories("pypi", "x") == ()


def test_missing_optional_fields_are_tolerated():
    client, _ = make_client(response([{"full_name": "a/b"}]))

    dependent = client.dependent_repositories("pypi", "x")[0]

    assert dependent.stars == 0
    assert dependent.description == ""
    assert dependent.primary_language is None


# --- package info ----------------------------------------------------------


def test_package_info_parses():
    client, _ = make_client(response(PACKAGE_PAYLOAD))

    info = client.package_info("pypi", "docxtpl")

    assert info.name == "docxtpl"
    assert info.platform == "Pypi"
    assert info.latest_release_number == "0.16.7"
    assert info.stars == 1800
    assert info.repository_url.endswith("python-docx-template")


def test_package_info_hits_the_right_endpoint():
    client, transport = make_client(response(PACKAGE_PAYLOAD))

    client.package_info("npm", "docxtemplater")

    assert transport.calls[0]["url"].endswith("/npm/docxtemplater")


def test_package_info_tolerates_a_sparse_payload():
    client, _ = make_client(response({}))

    info = client.package_info("pypi", "obscure")

    assert info.name == "obscure"
    assert info.platform == "pypi"
    assert info.homepage is None


# --- API key behaviour -----------------------------------------------------


def test_importing_the_module_needs_no_key():
    """Constructing a client without a key must work; only calling fails."""
    from dependency_map.clients import libraries_io_client

    client, _ = make_client(response([]), api_key=None)

    assert client.has_key is False
    assert libraries_io_client.API_ROOT.startswith("https://")


def test_missing_key_raises_a_clear_configuration_error():
    client, transport = make_client(response(DEPENDENTS_PAYLOAD), api_key=None)

    with pytest.raises(MissingSecret) as excinfo:
        client.dependent_repositories("pypi", "docxtpl")

    message = str(excinfo.value)
    assert "LIBRARIES_IO_API_KEY" in message
    assert "GitHub only" in message  # names the fallback, not just the failure
    assert transport.call_count == 0, "should fail before spending a request"


def test_missing_key_also_blocks_package_info():
    client, _ = make_client(response(PACKAGE_PAYLOAD), api_key=None)

    with pytest.raises(MissingSecret):
        client.package_info("pypi", "docxtpl")


def test_the_key_is_sent_as_a_query_parameter():
    """Unusual, and the reason redaction matters so much here."""
    client, transport = make_client(response(DEPENDENTS_PAYLOAD))

    client.dependent_repositories("pypi", "docxtpl")

    assert transport.calls[0]["params"]["api_key"] == FAKE_KEY


def test_the_key_never_reaches_the_cache():
    cache = MemoryCacheStore()
    client, _ = make_client(response(DEPENDENTS_PAYLOAD), cache=cache)

    client.dependent_repositories("pypi", "docxtpl")

    stored = "".join(k + v[0] for k, v in cache._entries.items())
    assert FAKE_KEY not in stored


def test_the_key_never_reaches_the_log(caplog):
    caplog.set_level("DEBUG")
    cache = MemoryCacheStore()
    client, _ = make_client(response(DEPENDENTS_PAYLOAD),
                            response(DEPENDENTS_PAYLOAD), cache=cache)

    client.dependent_repositories("pypi", "docxtpl")
    client.dependent_repositories("pypi", "docxtpl")

    assert FAKE_KEY not in caplog.text


def test_the_key_never_reaches_an_exception():
    client, _ = make_client(response({"error": "nope"}, status=404))

    with pytest.raises(ApiError) as excinfo:
        client.dependent_repositories("pypi", "docxtpl")

    assert FAKE_KEY not in str(excinfo.value)
    assert FAKE_KEY not in excinfo.value.url


def test_the_client_is_not_hardcoding_a_key():
    from pathlib import Path

    source = Path("src/dependency_map/clients/libraries_io_client.py").read_text(
        encoding="utf-8"
    )

    assert "api_key=" not in source.replace('"api_key": self._require_key()', "")
    assert FAKE_KEY not in source


# --- errors ----------------------------------------------------------------


def test_404_becomes_an_api_error():
    client, _ = make_client(response({"error": "Not Found"}, status=404))

    with pytest.raises(ApiError) as excinfo:
        client.package_info("pypi", "does-not-exist")

    assert excinfo.value.status == 404


def test_429_is_retried_then_gives_up():
    """Libraries.io returns 429 past 60 requests a minute."""
    client, transport = make_client(*[response("rate limited", status=429)
                                      for _ in range(3)])

    with pytest.raises(RetriesExhausted):
        client.dependent_repositories("pypi", "docxtpl")

    assert transport.call_count == 3


def test_5xx_is_retried_then_succeeds():
    client, transport = make_client(response("oops", status=503),
                                    response(DEPENDENTS_PAYLOAD))

    dependents = client.dependent_repositories("pypi", "docxtpl")

    assert transport.call_count == 2
    assert len(dependents) == 2


def test_the_client_makes_no_qualification_judgments():
    from pathlib import Path

    source = Path("src/dependency_map/clients/libraries_io_client.py").read_text(
        encoding="utf-8"
    )

    for term in ["qualification_status", "def qualify", "final_score"]:
        assert term not in source
