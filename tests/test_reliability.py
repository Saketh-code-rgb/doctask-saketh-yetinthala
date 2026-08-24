"""The reliability layer: pacing, retry, backoff, rate limits, caching.

Every test drives a fake transport. Nothing here touches the network, and the
clock and sleep function are injected so no test actually waits.
"""

from __future__ import annotations

import json
import time
from datetime import datetime, timedelta, timezone

import pytest

from dependency_map.reliability import (
    GITHUB_CODE_SEARCH,
    GITHUB_CORE,
    GITHUB_SEARCH,
    LIBRARIES_IO,
    REDACTED,
    ApiError,
    HttpResponse,
    MemoryCacheStore,
    Pacer,
    RateLimited,
    ReliabilityPolicy,
    ReliableRequester,
    RetriesExhausted,
    SqliteCacheStore,
    TransportError,
    backoff_delay,
    cache_key,
    decode_response,
    encode_response,
    is_fresh,
    is_primary_rate_limit,
    is_secondary_rate_limit,
    parse_rate_limit,
    redact_text,
    redact_url,
)

FAKE_TOKEN = "ghp_fake000000000000000000000000000000"
FAKE_KEY = "libio_fake_key_00000"


class FakeTransport:
    """Returns queued responses, or raises queued exceptions, in order."""

    def __init__(self, *responses):
        self._queue = list(responses)
        self.calls: list[dict] = []

    def request(self, method, url, *, params=None, headers=None, timeout=30.0):
        self.calls.append(
            {"method": method, "url": url, "params": dict(params or {}),
             "headers": dict(headers or {}), "timeout": timeout}
        )
        if not self._queue:
            raise AssertionError("FakeTransport ran out of queued responses")
        item = self._queue.pop(0)
        if isinstance(item, Exception):
            raise item
        return item

    @property
    def call_count(self) -> int:
        return len(self.calls)


class FakeClock:
    """A monotonic clock that only advances when something sleeps."""

    def __init__(self, start: float = 1000.0):
        self.now = start
        self.slept: list[float] = []

    def __call__(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.slept.append(seconds)
        self.now += seconds

    @property
    def total_slept(self) -> float:
        return sum(self.slept)


def ok(body="{}", status=200, headers=None):
    return HttpResponse(status=status, headers=headers or {}, text=body,
                        url="https://api.example.com/thing")


def policy(**overrides):
    defaults = dict(
        intervals={GITHUB_CODE_SEARCH: 6.5, GITHUB_SEARCH: 2.0,
                   GITHUB_CORE: 0.75, LIBRARIES_IO: 1.0},
        max_attempts=3,
        backoff_base_seconds=2.0,
        backoff_max_seconds=60.0,
        backoff_jitter_seconds=0.5,
        cache_ttl_seconds=7 * 24 * 3600,
    )
    defaults.update(overrides)
    return ReliabilityPolicy(**defaults)


def build(
    transport, *, cache=None, clock=None, rng=lambda a, b: 0.0,
    fake_wall_clock=False, **kw,
):
    """Assemble a requester over a fake transport.

    The pacing clock is always fake, so no test really sleeps. The *wall* clock
    stays real by default, because cache freshness compares against ISO
    timestamps written by the cache store; only the rate-limit-reset tests need
    it faked, and they ask for it explicitly.
    """
    clock = clock or FakeClock()
    wall = (lambda: clock.now) if fake_wall_clock else time.time
    return (
        ReliableRequester(
            transport, policy(**kw), cache=cache,
            clock=clock, wall_clock=wall,
            sleep=clock.sleep, rng=rng,
        ),
        clock,
    )


# --- cache -----------------------------------------------------------------


def test_cache_miss_performs_the_request():
    transport = FakeTransport(ok('{"ok": true}'))
    requester, _ = build(transport, cache=MemoryCacheStore())

    outcome = requester.get("https://api.example.com/x", resource=GITHUB_CORE)

    assert transport.call_count == 1
    assert outcome.from_cache is False


def test_successful_response_is_cached():
    cache = MemoryCacheStore()
    transport = FakeTransport(ok('{"ok": true}'))
    requester, _ = build(transport, cache=cache)

    requester.get("https://api.example.com/x", resource=GITHUB_CORE)

    assert cache.get(cache_key("GET", "https://api.example.com/x", None)) is not None


def test_cache_hit_avoids_the_network_entirely():
    """The point of the cache: a rerun never re-spends rate-limit budget."""
    cache = MemoryCacheStore()
    transport = FakeTransport(ok('{"n": 1}'))
    requester, _ = build(transport, cache=cache)

    first = requester.get("https://api.example.com/x", resource=GITHUB_CORE)
    second = requester.get("https://api.example.com/x", resource=GITHUB_CORE)

    assert transport.call_count == 1, "second call should not have hit the network"
    assert second.from_cache is True
    assert second.response.text == first.response.text


def test_cache_hit_does_not_pace():
    """A cached call spends no budget, so it should not wait either."""
    cache = MemoryCacheStore()
    transport = FakeTransport(ok('{"n": 1}'))
    requester, clock = build(transport, cache=cache)

    requester.get("https://x/y", resource=GITHUB_CODE_SEARCH)
    before = clock.total_slept
    requester.get("https://x/y", resource=GITHUB_CODE_SEARCH)

    assert clock.total_slept == before


def test_expired_cache_entry_refetches():
    cache = MemoryCacheStore()
    transport = FakeTransport(ok('{"n": 1}'), ok('{"n": 2}'))
    requester, _ = build(transport, cache=cache, cache_ttl_seconds=0.0)

    requester.get("https://api.example.com/x", resource=GITHUB_CORE)
    second = requester.get("https://api.example.com/x", resource=GITHUB_CORE)

    assert transport.call_count == 2
    assert second.from_cache is False


def test_error_responses_are_not_cached():
    cache = MemoryCacheStore()
    transport = FakeTransport(ok("boom", status=500), ok("boom", status=500),
                              ok("boom", status=500))
    requester, _ = build(transport, cache=cache)

    with pytest.raises(RetriesExhausted):
        requester.get("https://api.example.com/x", resource=GITHUB_CORE)

    assert cache.get(cache_key("GET", "https://api.example.com/x", None)) is None


def test_use_cache_false_bypasses_the_cache():
    cache = MemoryCacheStore()
    transport = FakeTransport(ok('{"n": 1}'), ok('{"n": 2}'))
    requester, _ = build(transport, cache=cache)

    requester.get("https://x/y", resource=GITHUB_CORE)
    requester.get("https://x/y", resource=GITHUB_CORE, use_cache=False)

    assert transport.call_count == 2


def test_cached_payload_can_rebuild_the_typed_result():
    """A raw-response cache, not parsed fragments: status, headers and body all
    survive the round trip."""
    response = ok('{"total_count": 3}', headers={"Link": "<next>", "ETag": "abc"})
    restored = decode_response(encode_response(response))

    assert restored.status == 200
    assert restored.json() == {"total_count": 3}
    assert restored.header("link") == "<next>"


def test_cache_stores_only_whitelisted_headers():
    response = ok("{}", headers={"Set-Cookie": "session=secret", "ETag": "x"})
    stored = json.loads(encode_response(response))

    assert "set-cookie" not in stored["headers"]
    assert stored["headers"]["etag"] == "x"


def test_is_fresh():
    now = datetime.now(timezone.utc)
    recent = (now - timedelta(hours=1)).isoformat()
    old = (now - timedelta(days=30)).isoformat()

    assert is_fresh(recent, 7 * 24 * 3600) is True
    assert is_fresh(old, 7 * 24 * 3600) is False
    assert is_fresh("not-a-timestamp", 100) is False


def test_sqlite_cache_store_round_trip(conn, candidate_id):
    """Uses the real api_cache table from phase 2, on a temp database."""
    store = SqliteCacheStore(conn)
    store.put("key-1", '{"status": 200, "body": "{}"}')

    payload, fetched_at = store.get("key-1")

    assert json.loads(payload)["status"] == 200
    assert fetched_at
    assert store.get("missing") is None


def test_requester_works_against_the_real_sqlite_cache(conn):
    transport = FakeTransport(ok('{"n": 1}'))
    requester, _ = build(transport, cache=SqliteCacheStore(conn))

    requester.get("https://api.example.com/x", resource=GITHUB_CORE)
    second = requester.get("https://api.example.com/x", resource=GITHUB_CORE)

    assert transport.call_count == 1
    assert second.from_cache is True


# --- cache keys and secrets ------------------------------------------------


def test_cache_key_is_deterministic():
    a = cache_key("GET", "https://x/y", {"q": "docxtpl", "page": 1})
    b = cache_key("GET", "https://x/y", {"page": 1, "q": "docxtpl"})

    assert a == b


def test_cache_key_changes_with_request_identity():
    base = cache_key("GET", "https://x/y", {"q": "a"})

    assert cache_key("GET", "https://x/y", {"q": "b"}) != base
    assert cache_key("GET", "https://x/z", {"q": "a"}) != base
    assert cache_key("POST", "https://x/y", {"q": "a"}) != base


def test_api_key_never_reaches_the_cache_key():
    """Libraries.io passes its key as a query parameter, so this is the exact
    place a credential would otherwise be persisted."""
    key = cache_key("GET", "https://libraries.io/api/pypi/docxtpl",
                    {"api_key": FAKE_KEY, "page": 1})

    assert FAKE_KEY not in key


def test_rotating_a_token_does_not_invalidate_the_cache():
    with_key_a = cache_key("GET", "https://x/y", {"api_key": "aaa", "page": 1})
    with_key_b = cache_key("GET", "https://x/y", {"api_key": "bbb", "page": 1})

    assert with_key_a == with_key_b


def test_redact_url_strips_secret_parameters():
    redacted = redact_url(f"https://libraries.io/api/pypi/x?api_key={FAKE_KEY}&page=2")

    assert FAKE_KEY not in redacted
    assert REDACTED in redacted
    assert "page=2" in redacted


def test_redact_url_leaves_ordinary_urls_alone():
    url = "https://api.github.com/repos/a/b"
    assert redact_url(url) == url


def test_redact_text_scrubs_secrets_in_free_text():
    scrubbed = redact_text(f"failed GET https://x/y?api_key={FAKE_KEY} timed out")

    assert FAKE_KEY not in scrubbed


def test_cached_body_does_not_contain_the_api_key():
    cache = MemoryCacheStore()
    transport = FakeTransport(ok('{"ok": true}'))
    requester, _ = build(transport, cache=cache)

    requester.get("https://libraries.io/api/pypi/docxtpl",
                  resource=LIBRARIES_IO, params={"api_key": FAKE_KEY})

    stored = "".join(payload for payload, _ in cache._entries.values())
    assert FAKE_KEY not in stored
    assert FAKE_KEY not in "".join(cache._entries.keys())


def test_transport_errors_do_not_quote_the_secret():
    transport = FakeTransport(
        TransportError(f"connection failed for https://x/y?api_key={FAKE_KEY}"),
        TransportError("connection failed"),
        TransportError("connection failed"),
    )
    requester, _ = build(transport)

    with pytest.raises(RetriesExhausted) as excinfo:
        requester.get("https://x/y", resource=LIBRARIES_IO,
                      params={"api_key": FAKE_KEY})

    assert FAKE_KEY not in str(excinfo.value)


def test_api_error_does_not_quote_the_secret():
    error = ApiError(404, f"https://x/y?api_key={FAKE_KEY}", "Not Found")

    assert FAKE_KEY not in str(error)
    assert FAKE_KEY not in error.url


def test_secrets_never_reach_the_log(caplog):
    caplog.set_level("DEBUG")
    cache = MemoryCacheStore()
    transport = FakeTransport(ok("{}"), ok("{}"))
    requester, _ = build(transport, cache=cache)

    url = "https://libraries.io/api/pypi/docxtpl"
    requester.get(url, resource=LIBRARIES_IO, params={"api_key": FAKE_KEY})
    requester.get(url, resource=LIBRARIES_IO, params={"api_key": FAKE_KEY})

    assert FAKE_KEY not in caplog.text


# --- pacing ----------------------------------------------------------------


def test_first_call_to_a_resource_does_not_wait():
    clock = FakeClock()
    pacer = Pacer({GITHUB_CODE_SEARCH: 6.5}, clock=clock, sleep=clock.sleep)

    assert pacer.wait(GITHUB_CODE_SEARCH) == 0.0


def test_second_call_waits_the_configured_interval():
    clock = FakeClock()
    pacer = Pacer({GITHUB_CODE_SEARCH: 6.5}, clock=clock, sleep=clock.sleep)

    pacer.wait(GITHUB_CODE_SEARCH)
    slept = pacer.wait(GITHUB_CODE_SEARCH)

    assert slept == pytest.approx(6.5)


def test_code_search_and_core_rest_are_paced_separately():
    """The design point: spending code-search budget must not slow core REST.
    A shared pacer would throttle file and metadata fetches roughly ninefold."""
    clock = FakeClock()
    pacer = Pacer({GITHUB_CODE_SEARCH: 6.5, GITHUB_CORE: 0.75},
                  clock=clock, sleep=clock.sleep)

    pacer.wait(GITHUB_CODE_SEARCH)
    assert pacer.wait(GITHUB_CORE) == 0.0, "core REST inherited the code-search wait"

    assert pacer.wait(GITHUB_CORE) == pytest.approx(0.75)
    assert pacer.wait(GITHUB_CODE_SEARCH) == pytest.approx(6.5 - 0.75)


def test_every_bucket_keeps_its_own_interval():
    clock = FakeClock()
    intervals = {GITHUB_CODE_SEARCH: 6.5, GITHUB_SEARCH: 2.0,
                 GITHUB_CORE: 0.75, LIBRARIES_IO: 1.0}
    pacer = Pacer(intervals, clock=clock, sleep=clock.sleep)

    for resource, expected in intervals.items():
        pacer.wait(resource)
        assert pacer.wait(resource) == pytest.approx(expected), resource


def test_code_search_pacing_respects_ten_per_minute():
    assert 60 / 6.5 <= 10


def test_enough_elapsed_time_means_no_wait():
    clock = FakeClock()
    pacer = Pacer({GITHUB_CORE: 0.75}, clock=clock, sleep=clock.sleep)

    pacer.wait(GITHUB_CORE)
    clock.now += 10.0

    assert pacer.wait(GITHUB_CORE) == 0.0


def test_unknown_resource_has_no_pacing():
    clock = FakeClock()
    pacer = Pacer({}, clock=clock, sleep=clock.sleep)

    pacer.wait("something_else")
    assert pacer.wait("something_else") == 0.0


def test_requester_paces_between_calls():
    transport = FakeTransport(ok("{}"), ok("{}"))
    requester, clock = build(transport)

    requester.get("https://x/1", resource=GITHUB_CODE_SEARCH)
    requester.get("https://x/2", resource=GITHUB_CODE_SEARCH)

    assert clock.total_slept == pytest.approx(6.5)


# --- retry -----------------------------------------------------------------


@pytest.mark.parametrize("status", [500, 502, 503, 504])
def test_5xx_is_retried(status):
    transport = FakeTransport(ok("err", status=status), ok('{"ok": true}'))
    requester, _ = build(transport)

    outcome = requester.get("https://x/y", resource=GITHUB_CORE)

    assert transport.call_count == 2
    assert outcome.attempts == 2
    assert outcome.response.status == 200


def test_connection_error_is_retried():
    transport = FakeTransport(TransportError("connection reset"), ok('{"ok": true}'))
    requester, _ = build(transport)

    outcome = requester.get("https://x/y", resource=GITHUB_CORE)

    assert transport.call_count == 2
    assert outcome.response.status == 200


def test_timeout_is_retried():
    transport = FakeTransport(TransportError("read timed out"), ok('{"ok": true}'))
    requester, _ = build(transport)

    assert requester.get("https://x/y", resource=GITHUB_CORE).response.status == 200


def test_retries_are_exhausted_after_max_attempts():
    transport = FakeTransport(*[ok("err", status=503) for _ in range(5)])
    requester, _ = build(transport)

    with pytest.raises(RetriesExhausted, match="3 attempts"):
        requester.get("https://x/y", resource=GITHUB_CORE)

    assert transport.call_count == 3, "should stop at max_attempts, not keep going"


def test_max_attempts_is_configurable():
    transport = FakeTransport(*[ok("err", status=503) for _ in range(10)])
    requester, _ = build(transport, max_attempts=5)

    with pytest.raises(RetriesExhausted):
        requester.get("https://x/y", resource=GITHUB_CORE)

    assert transport.call_count == 5


def test_404_is_not_retried():
    """A missing file is an answer, not a transient failure."""
    transport = FakeTransport(ok('{"message": "Not Found"}', status=404))
    requester, _ = build(transport)

    with pytest.raises(ApiError) as excinfo:
        requester.get("https://x/y", resource=GITHUB_CORE)

    assert excinfo.value.status == 404
    assert transport.call_count == 1


def test_422_is_not_retried():
    transport = FakeTransport(ok('{"message": "Validation Failed"}', status=422))
    requester, _ = build(transport)

    with pytest.raises(ApiError):
        requester.get("https://x/y", resource=GITHUB_CORE)

    assert transport.call_count == 1


def test_api_error_message_comes_from_the_body():
    transport = FakeTransport(ok('{"message": "Bad credentials"}', status=401))
    requester, _ = build(transport)

    with pytest.raises(ApiError, match="Bad credentials"):
        requester.get("https://x/y", resource=GITHUB_CORE)


# --- backoff ---------------------------------------------------------------


def test_backoff_grows_exponentially():
    p = policy(backoff_jitter_seconds=0.0)

    assert backoff_delay(0, p, rng=lambda a, b: 0.0) == pytest.approx(2.0)
    assert backoff_delay(1, p, rng=lambda a, b: 0.0) == pytest.approx(4.0)
    assert backoff_delay(2, p, rng=lambda a, b: 0.0) == pytest.approx(8.0)
    assert backoff_delay(3, p, rng=lambda a, b: 0.0) == pytest.approx(16.0)


def test_backoff_is_bounded():
    """Without a ceiling, a long retry chain would grow without bound."""
    p = policy(backoff_max_seconds=10.0, backoff_jitter_seconds=0.0)

    assert backoff_delay(20, p, rng=lambda a, b: 0.0) == pytest.approx(10.0)


def test_backoff_adds_jitter_within_bounds():
    """Jitter keeps simultaneous failures from retrying in lockstep."""
    p = policy(backoff_jitter_seconds=0.5)

    lowest = backoff_delay(0, p, rng=lambda a, b: a)
    highest = backoff_delay(0, p, rng=lambda a, b: b)

    assert lowest == pytest.approx(2.0)
    assert highest == pytest.approx(2.5)
    assert 0 <= highest - lowest <= 0.5


def test_real_jitter_stays_within_bounds():
    p = policy(backoff_jitter_seconds=0.5)

    for _ in range(200):
        delay = backoff_delay(1, p)
        assert 4.0 <= delay <= 4.5


def test_backoff_is_applied_between_retries():
    transport = FakeTransport(ok("err", status=503), ok('{"ok": true}'))
    requester, clock = build(transport)

    requester.get("https://x/y", resource=GITHUB_CORE)

    assert 2.0 in clock.slept


# --- rate limits -----------------------------------------------------------


def test_parse_rate_limit_headers():
    response = ok("{}", headers={
        "x-ratelimit-limit": "10",
        "x-ratelimit-remaining": "0",
        "x-ratelimit-reset": "1700000000",
        "x-ratelimit-resource": "code_search",
        "x-ratelimit-used": "10",
    })
    state = parse_rate_limit(response)

    assert state.limit == 10
    assert state.remaining == 0
    assert state.reset_at == 1700000000.0
    assert state.resource == "code_search"
    assert state.is_exhausted is True


def test_parse_rate_limit_tolerates_missing_headers():
    """Libraries.io does not reliably send these, so absence must not crash."""
    state = parse_rate_limit(ok("{}"))

    assert state.limit is None
    assert state.remaining is None
    assert state.is_exhausted is False


def test_retry_after_is_honoured():
    transport = FakeTransport(
        ok('{"message": "rate limited"}', status=429, headers={"retry-after": "17"}),
        ok('{"ok": true}'),
    )
    requester, clock = build(transport)

    outcome = requester.get("https://x/y", resource=GITHUB_CORE)

    assert 17.0 in clock.slept
    assert outcome.response.status == 200


def test_primary_rate_limit_waits_until_reset():
    """Budget exhausted: wait for the window to roll over, not a fixed delay."""
    clock = FakeClock(start=1000.0)
    transport = FakeTransport(
        ok('{"message": "API rate limit exceeded"}', status=403, headers={
            "x-ratelimit-remaining": "0",
            "x-ratelimit-reset": "1050",
            "x-ratelimit-resource": "core",
        }),
        ok('{"ok": true}'),
    )
    requester, _ = build(transport, clock=clock, fake_wall_clock=True)

    outcome = requester.get("https://x/y", resource=GITHUB_CORE)

    assert clock.slept[0] == pytest.approx(51.0)  # 50s to reset, plus 1s margin
    assert outcome.response.status == 200


def test_primary_rate_limit_is_detected():
    response = ok("{}", status=403, headers={"x-ratelimit-remaining": "0"})

    assert is_primary_rate_limit(response) is True
    assert is_primary_rate_limit(ok("{}", status=403,
                                    headers={"x-ratelimit-remaining": "42"})) is False


def test_secondary_rate_limit_is_detected():
    body = '{"message": "You have exceeded a secondary rate limit"}'

    assert is_secondary_rate_limit(ok(body, status=403)) is True
    assert is_secondary_rate_limit(ok(body, status=429)) is True
    assert is_secondary_rate_limit(ok('{"message": "Forbidden"}', status=403)) is False


def test_bare_429_counts_as_a_rate_limit():
    assert is_secondary_rate_limit(ok("", status=429)) is True


def test_secondary_rate_limit_backs_off_at_least_a_minute():
    """GitHub's guidance is to wait rather than retry immediately, and at least
    a minute when no retry-after is given."""
    transport = FakeTransport(
        ok('{"message": "You have exceeded a secondary rate limit"}', status=403),
        ok('{"ok": true}'),
    )
    requester, clock = build(transport)

    requester.get("https://x/y", resource=GITHUB_CORE)

    assert clock.slept[0] >= 60.0


def test_secondary_rate_limit_prefers_retry_after_when_present():
    transport = FakeTransport(
        ok('{"message": "secondary rate limit"}', status=403,
           headers={"retry-after": "5"}),
        ok('{"ok": true}'),
    )
    requester, clock = build(transport)

    requester.get("https://x/y", resource=GITHUB_CORE)

    assert clock.slept[0] == pytest.approx(5.0)


def test_a_rate_limited_endpoint_is_never_hammered():
    """Every attempt against a rate-limited endpoint must sleep first."""
    transport = FakeTransport(*[
        ok('{"message": "secondary rate limit"}', status=403) for _ in range(3)
    ])
    requester, clock = build(transport)

    with pytest.raises(RetriesExhausted):
        requester.get("https://x/y", resource=GITHUB_CORE)

    assert len([s for s in clock.slept if s >= 60.0]) == 2
    assert transport.call_count == 3


def test_an_absurd_reset_wait_stops_rather_than_blocking():
    clock = FakeClock(start=1000.0)
    transport = FakeTransport(
        ok("{}", status=403, headers={
            "x-ratelimit-remaining": "0", "x-ratelimit-reset": "99999",
        }),
        ok('{"ok": true}'),
    )
    requester, _ = build(transport, clock=clock, fake_wall_clock=True,
                         max_rate_limit_wait_seconds=300.0)

    with pytest.raises(RateLimited, match="over the"):
        requester.get("https://x/y", resource=GITHUB_CORE)


def test_rate_limit_error_does_not_leak_the_secret():
    clock = FakeClock(start=1000.0)
    transport = FakeTransport(ok("{}", status=403, headers={
        "x-ratelimit-remaining": "0", "x-ratelimit-reset": "99999",
    }))
    requester, _ = build(transport, clock=clock, fake_wall_clock=True)

    with pytest.raises(RateLimited) as excinfo:
        requester.get("https://libraries.io/api/pypi/x", resource=LIBRARIES_IO,
                      params={"api_key": FAKE_KEY})

    assert FAKE_KEY not in str(excinfo.value)


# --- policy from config ----------------------------------------------------


def test_policy_is_built_from_config(config_dir_for_reliability):
    from dependency_map.config import load_config

    config = load_config(config_dir_for_reliability, env_file=None,
                         require_github_token=False)
    built = ReliabilityPolicy.from_config(config)

    assert built.intervals[GITHUB_CODE_SEARCH] == 6.5
    assert built.intervals[GITHUB_SEARCH] == 2.0
    assert built.intervals[GITHUB_CORE] == 0.75
    assert built.intervals[LIBRARIES_IO] == 1.0
    assert built.max_attempts == 3
    assert built.backoff_base_seconds == 2.0
    assert built.backoff_max_seconds == 60.0
    assert built.cache_ttl_seconds == 7 * 24 * 3600


def test_nothing_is_hardcoded_that_config_should_own():
    """Pacing and retry numbers must come from config, not client logic."""
    from pathlib import Path

    source = Path("src/dependency_map/clients/github_client.py").read_text(
        encoding="utf-8"
    )
    assert "6.5" not in source
    assert "time.sleep" not in source


@pytest.fixture
def config_dir_for_reliability():
    return "config"
