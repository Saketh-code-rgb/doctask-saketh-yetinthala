"""Shared reliability layer: pacing, retries, backoff, rate limits, caching.

Every API client routes through this rather than duplicating the behaviour
(TECHNICAL_DESIGN.md section 14). The order of operations for one call is:

    cache lookup -> pace -> send -> classify -> retry or back off -> cache write

Two things here are worth knowing before reading the code.

**Pacing is per resource, not global.** GitHub code search is capped at 10
requests per minute in its own bucket, while the core REST API allows 5,000 per
hour, and non-code search allows 30 per minute. Applying the code-search spacing
to every call would throttle metadata and file fetches roughly ninefold for no
reason, which matters because evidence collection is the most call-heavy stage
in the pipeline. Each resource therefore keeps its own last-call timestamp.

**The cache stores raw responses, not parsed fragments.** A cached entry holds
the status, the body as received, and the headers worth keeping, which is enough
to rebuild a typed result without going back to the network. Secrets are
stripped before anything is written, since Libraries.io passes its API key as a
query parameter and it would otherwise land in both the cache key and the stored
URL.
"""

from __future__ import annotations

import hashlib
import json
import logging
import random
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Mapping, Protocol, Sequence
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

logger = logging.getLogger(__name__)

# --- resources -------------------------------------------------------------

#: GitHub code search. Its own bucket, 10 requests per minute, and the only
#: GitHub endpoint that has always required authentication.
GITHUB_CODE_SEARCH = "github_code_search"
#: Every other GitHub search endpoint. 30 requests per minute.
GITHUB_SEARCH = "github_search"
#: The general REST API. 5,000 requests per hour for an authenticated token.
GITHUB_CORE = "github_core"
#: Libraries.io. 60 requests per minute, and it does not reliably return
#: rate-limit headers, so its pacing has to be time-based rather than adaptive.
LIBRARIES_IO = "libraries_io"

RESOURCES: tuple[str, ...] = (
    GITHUB_CODE_SEARCH,
    GITHUB_SEARCH,
    GITHUB_CORE,
    LIBRARIES_IO,
)

#: Query parameters that must never reach a cache key, a stored URL, or a log.
SECRET_PARAMS = frozenset({"api_key", "access_token", "token", "client_secret"})
#: Deliberately URL-safe. A marker containing angle brackets survives
#: urlencode as %3C...%3E, which still hides the secret but makes a redacted
#: URL harder to read in a log or a cache row.
REDACTED = "REDACTED"

#: Response headers worth keeping in the cache. A whitelist rather than
#: everything, so nothing unexpected gets persisted.
CACHED_HEADERS = frozenset(
    {
        "content-type",
        "etag",
        "last-modified",
        "link",
        "retry-after",
        "x-ratelimit-limit",
        "x-ratelimit-remaining",
        "x-ratelimit-reset",
        "x-ratelimit-resource",
        "x-ratelimit-used",
    }
)

RETRYABLE_STATUSES = frozenset({500, 502, 503, 504})


# --- errors ----------------------------------------------------------------


class ReliabilityError(Exception):
    """Base class for every failure this layer raises."""


class TransportError(ReliabilityError):
    """A connection reset, timeout, or other transport-level failure."""


class ApiError(ReliabilityError):
    """A non-retryable error response from an API."""

    def __init__(self, status: int, url: str, message: str = "") -> None:
        self.status = status
        self.url = redact_url(url)
        self.message = message
        super().__init__(f"HTTP {status} from {self.url}: {message}".rstrip(": "))


class RetriesExhausted(ReliabilityError):
    """Every attempt failed. The call is marked failed, never silently dropped."""


class RateLimited(ReliabilityError):
    """A rate limit could not be waited out within the configured budget."""


# --- transport -------------------------------------------------------------


@dataclass(frozen=True)
class HttpResponse:
    """A response, independent of whichever HTTP library produced it."""

    status: int
    headers: Mapping[str, str]
    text: str
    url: str = ""

    def header(self, name: str) -> str | None:
        lowered = {k.lower(): v for k, v in self.headers.items()}
        return lowered.get(name.lower())

    def json(self) -> Any:
        try:
            return json.loads(self.text)
        except json.JSONDecodeError as exc:
            raise ApiError(self.status, self.url, f"response was not JSON: {exc}") from exc


class Transport(Protocol):
    """The seam that keeps this layer testable without real HTTP."""

    def request(
        self,
        method: str,
        url: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float = 30.0,
    ) -> HttpResponse: ...


class RequestsTransport:
    """The real transport, backed by `requests`.

    Connection and timeout failures are translated into TransportError so
    callers never have to know which HTTP library is underneath.
    """

    def __init__(self, session: Any | None = None) -> None:
        import requests

        self._requests = requests
        self._session = session or requests.Session()

    def request(
        self,
        method: str,
        url: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float = 30.0,
    ) -> HttpResponse:
        try:
            response = self._session.request(
                method, url, params=dict(params or {}),
                headers=dict(headers or {}), timeout=timeout,
            )
        except self._requests.RequestException as exc:
            # str(exc) can contain the full URL, so redact before it escapes.
            raise TransportError(redact_text(str(exc))) from None
        return HttpResponse(
            status=response.status_code,
            headers=dict(response.headers),
            text=response.text,
            url=redact_url(url),
        )


# --- redaction -------------------------------------------------------------


def redact_url(url: str) -> str:
    """Strip secret query parameters from a URL.

    Libraries.io takes its API key as `?api_key=...`, so an un-redacted URL
    would put the credential into the cache, the logs, and any exception that
    quotes it.
    """
    parts = urlsplit(url)
    if not parts.query:
        return url
    pairs = [
        (k, REDACTED if k.lower() in SECRET_PARAMS else v)
        for k, v in parse_qsl(parts.query, keep_blank_values=True)
    ]
    return urlunsplit(parts._replace(query=urlencode(pairs)))


def redact_params(params: Mapping[str, Any] | None) -> dict[str, Any]:
    return {
        k: (REDACTED if k.lower() in SECRET_PARAMS else v)
        for k, v in (params or {}).items()
    }


def redact_text(text: str) -> str:
    """Best-effort scrub of secret-looking query parameters in free text."""
    import re

    pattern = "|".join(sorted(SECRET_PARAMS))
    return re.sub(rf"(?i)\b({pattern})=[^&\s\"']+", rf"\1={REDACTED}", text)


# --- cache -----------------------------------------------------------------


def cache_key(
    method: str, url: str, params: Mapping[str, Any] | None = None
) -> str:
    """A deterministic key from the request's identity.

    Secrets are redacted first, so rotating a token doesn't invalidate the
    cache and, more importantly, no credential is ever part of a stored key.
    """
    payload = json.dumps(
        {
            "method": method.upper(),
            "url": redact_url(url),
            "params": sorted(redact_params(params).items()),
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class CacheStore(Protocol):
    def get(self, key: str) -> tuple[str, str] | None:
        """Return (response_json, fetched_at) or None."""

    def put(self, key: str, response_json: str) -> None: ...


class SqliteCacheStore:
    """Backs onto the api_cache table from phase 2.

    Holds a connection rather than opening one, so a caller can group cache
    writes into the same transaction as the evidence they belong to.
    """

    def __init__(self, connection: Any) -> None:
        self._conn = connection

    def get(self, key: str) -> tuple[str, str] | None:
        from . import storage

        row = storage.get_api_cache(self._conn, key)
        if row is None:
            return None
        return row["response_json"], row["fetched_at"]

    def put(self, key: str, response_json: str) -> None:
        from . import storage

        storage.put_api_cache(self._conn, cache_key=key, response_json=response_json)


class MemoryCacheStore:
    """An in-process cache, for tests and for callers with no database."""

    def __init__(self) -> None:
        self._entries: dict[str, tuple[str, str]] = {}

    def get(self, key: str) -> tuple[str, str] | None:
        return self._entries.get(key)

    def put(self, key: str, response_json: str) -> None:
        self._entries[key] = (response_json, _utcnow_iso())


def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def encode_response(response: HttpResponse) -> str:
    """Serialize a raw response for the cache.

    Deliberately the whole response, not a parsed fragment: a cache hit has to
    be able to rebuild the typed result without another network call.
    """
    return json.dumps(
        {
            "status": response.status,
            "url": redact_url(response.url),
            "headers": {
                k.lower(): v
                for k, v in response.headers.items()
                if k.lower() in CACHED_HEADERS
            },
            "body": response.text,
        },
        sort_keys=True,
    )


def decode_response(payload: str) -> HttpResponse:
    data = json.loads(payload)
    return HttpResponse(
        status=data["status"],
        headers=data.get("headers", {}),
        text=data.get("body", ""),
        url=data.get("url", ""),
    )


def is_fresh(fetched_at: str, ttl_seconds: float, now: float | None = None) -> bool:
    try:
        stamped = datetime.fromisoformat(fetched_at)
    except ValueError:
        return False
    if stamped.tzinfo is None:
        stamped = stamped.replace(tzinfo=timezone.utc)
    current = now if now is not None else time.time()
    return (current - stamped.timestamp()) < ttl_seconds


# --- pacing ----------------------------------------------------------------


class Pacer:
    """Enforces a minimum gap between calls, per resource.

    Separate buckets matter: code search allows 10 calls a minute while the
    core REST API allows 5,000 an hour. Sharing one gap between them would
    slow metadata and file fetches to roughly a ninth of what GitHub permits.
    """

    def __init__(
        self,
        intervals: Mapping[str, float],
        *,
        clock: Callable[[], float] = time.monotonic,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self._intervals = dict(intervals)
        self._clock = clock
        self._sleep = sleep
        self._last: dict[str, float] = {}

    def interval_for(self, resource: str) -> float:
        return self._intervals.get(resource, 0.0)

    def wait(self, resource: str) -> float:
        """Block until this resource may be called again. Returns seconds slept."""
        interval = self.interval_for(resource)
        now = self._clock()
        last = self._last.get(resource)
        slept = 0.0
        if last is not None and interval > 0:
            elapsed = now - last
            if elapsed < interval:
                slept = interval - elapsed
                self._sleep(slept)
        self._last[resource] = self._clock()
        return slept


# --- rate limits -----------------------------------------------------------


@dataclass(frozen=True)
class RateLimitState:
    """What a response's headers say about the budget it was charged to."""

    limit: int | None = None
    remaining: int | None = None
    reset_at: float | None = None
    resource: str | None = None
    retry_after: float | None = None

    @property
    def is_exhausted(self) -> bool:
        return self.remaining is not None and self.remaining <= 0


def parse_rate_limit(response: HttpResponse) -> RateLimitState:
    def _int(name: str) -> int | None:
        raw = response.header(name)
        try:
            return int(raw) if raw is not None else None
        except ValueError:
            return None

    retry_after_raw = response.header("retry-after")
    try:
        retry_after = float(retry_after_raw) if retry_after_raw is not None else None
    except ValueError:
        retry_after = None

    reset = _int("x-ratelimit-reset")
    return RateLimitState(
        limit=_int("x-ratelimit-limit"),
        remaining=_int("x-ratelimit-remaining"),
        reset_at=float(reset) if reset is not None else None,
        resource=response.header("x-ratelimit-resource"),
        retry_after=retry_after,
    )


def is_secondary_rate_limit(response: HttpResponse) -> bool:
    """GitHub returns 403 or 429 for a secondary limit, and says so in the body.

    Secondary limits call for backing off rather than retrying immediately,
    which is why they're told apart from an ordinary 403.
    """
    if response.status not in (403, 429):
        return False
    body = response.text.lower()
    if "secondary rate limit" in body or "abuse detection" in body:
        return True
    # A 429 with no explanatory body is still a rate limit.
    return response.status == 429


def is_primary_rate_limit(response: HttpResponse) -> bool:
    if response.status not in (403, 429):
        return False
    state = parse_rate_limit(response)
    return state.is_exhausted


# --- policy ----------------------------------------------------------------


@dataclass(frozen=True)
class ReliabilityPolicy:
    """Everything tunable, loaded from config rather than hardcoded."""

    intervals: Mapping[str, float]
    max_attempts: int = 3
    backoff_base_seconds: float = 2.0
    backoff_max_seconds: float = 60.0
    backoff_jitter_seconds: float = 0.5
    cache_ttl_seconds: float = 7 * 24 * 3600
    timeout_seconds: float = 30.0
    #: Refuse to sit waiting for a rate-limit reset longer than this.
    max_rate_limit_wait_seconds: float = 300.0

    @classmethod
    def from_config(cls, config: Any) -> "ReliabilityPolicy":
        pacing = config.pacing
        return cls(
            intervals={
                GITHUB_CODE_SEARCH: pacing.github_code_search_min_interval_seconds,
                GITHUB_SEARCH: pacing.github_search_min_interval_seconds,
                GITHUB_CORE: pacing.github_rest_min_interval_seconds,
                LIBRARIES_IO: pacing.libraries_io_min_interval_seconds,
            },
            max_attempts=config.retry.max_attempts,
            backoff_base_seconds=config.retry.backoff_base_seconds,
            backoff_max_seconds=config.retry.backoff_max_seconds,
            backoff_jitter_seconds=config.retry.backoff_jitter_seconds,
            cache_ttl_seconds=config.cache.ttl_days * 24 * 3600,
        )


def backoff_delay(
    attempt: int,
    policy: ReliabilityPolicy,
    *,
    rng: Callable[[float, float], float] = random.uniform,
) -> float:
    """Exponential backoff, bounded, with jitter.

    Jitter is added so that several calls failing at once don't all retry in
    lockstep. It is added after the cap, so the cap bounds the exponential part
    and the jitter stays a small, predictable addition on top.
    """
    exponential = policy.backoff_base_seconds * (2 ** max(attempt, 0))
    bounded = min(exponential, policy.backoff_max_seconds)
    return bounded + rng(0.0, policy.backoff_jitter_seconds)


# --- the requester ---------------------------------------------------------


@dataclass
class RequestOutcome:
    """A response plus how it was obtained, useful for tests and for logging."""

    response: HttpResponse
    from_cache: bool = False
    attempts: int = 1
    slept_seconds: float = 0.0


class ReliableRequester:
    """Runs one request through cache, pacing, retry, and rate-limit handling."""

    def __init__(
        self,
        transport: Transport,
        policy: ReliabilityPolicy,
        *,
        cache: CacheStore | None = None,
        clock: Callable[[], float] = time.monotonic,
        wall_clock: Callable[[], float] = time.time,
        sleep: Callable[[float], None] = time.sleep,
        rng: Callable[[float, float], float] = random.uniform,
    ) -> None:
        self._transport = transport
        self._policy = policy
        self._cache = cache
        self._sleep = sleep
        self._wall_clock = wall_clock
        self._rng = rng
        self._pacer = Pacer(policy.intervals, clock=clock, sleep=sleep)

    @property
    def pacer(self) -> Pacer:
        return self._pacer

    def get(
        self,
        url: str,
        *,
        resource: str,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        use_cache: bool = True,
    ) -> RequestOutcome:
        return self.request(
            "GET", url, resource=resource, params=params,
            headers=headers, use_cache=use_cache,
        )

    def request(
        self,
        method: str,
        url: str,
        *,
        resource: str,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        use_cache: bool = True,
    ) -> RequestOutcome:
        key = cache_key(method, url, params)

        if use_cache and self._cache is not None:
            cached = self._cache.get(key)
            if cached is not None:
                payload, fetched_at = cached
                if is_fresh(fetched_at, self._policy.cache_ttl_seconds,
                            now=self._wall_clock()):
                    logger.debug("cache hit for %s", redact_url(url))
                    return RequestOutcome(
                        response=decode_response(payload),
                        from_cache=True,
                        attempts=0,
                    )

        outcome = self._send_with_retries(
            method, url, resource=resource, params=params, headers=headers
        )

        # Written before anything parses it, so a crash mid-parse still leaves
        # the expensive part done.
        if use_cache and self._cache is not None and outcome.response.status < 400:
            self._cache.put(key, encode_response(outcome.response))

        return outcome

    def _send_with_retries(
        self,
        method: str,
        url: str,
        *,
        resource: str,
        params: Mapping[str, Any] | None,
        headers: Mapping[str, str] | None,
    ) -> RequestOutcome:
        safe_url = redact_url(url)
        slept = 0.0
        last_error: str = ""

        for attempt in range(self._policy.max_attempts):
            slept += self._pacer.wait(resource)

            try:
                response = self._transport.request(
                    method, url, params=params, headers=headers,
                    timeout=self._policy.timeout_seconds,
                )
            except TransportError as exc:
                last_error = redact_text(str(exc))
                logger.warning(
                    "transport failure on %s (attempt %d/%d): %s",
                    safe_url, attempt + 1, self._policy.max_attempts, last_error,
                )
                if attempt + 1 >= self._policy.max_attempts:
                    break
                slept += self._back_off(attempt)
                continue

            if response.status < 400:
                return RequestOutcome(
                    response=response, attempts=attempt + 1, slept_seconds=slept
                )

            if self._is_rate_limited(response):
                if attempt + 1 >= self._policy.max_attempts:
                    last_error = f"rate limited (HTTP {response.status})"
                    break
                slept += self._wait_out_rate_limit(response, attempt, safe_url)
                continue

            if response.status in RETRYABLE_STATUSES:
                last_error = f"HTTP {response.status}"
                logger.warning(
                    "retryable %s from %s (attempt %d/%d)",
                    last_error, safe_url, attempt + 1, self._policy.max_attempts,
                )
                if attempt + 1 >= self._policy.max_attempts:
                    break
                slept += self._back_off(attempt)
                continue

            # Anything else is the API telling us something we should not retry.
            raise ApiError(response.status, safe_url, _error_message(response))

        raise RetriesExhausted(
            f"{self._policy.max_attempts} attempts failed for {safe_url}: {last_error}"
        )

    def _is_rate_limited(self, response: HttpResponse) -> bool:
        return is_primary_rate_limit(response) or is_secondary_rate_limit(response)

    def _wait_out_rate_limit(
        self, response: HttpResponse, attempt: int, safe_url: str
    ) -> float:
        state = parse_rate_limit(response)

        # Retry-After wins whenever GitHub sends it.
        if state.retry_after is not None:
            delay = state.retry_after
            reason = "retry-after"
        elif state.is_exhausted and state.reset_at is not None:
            # Primary limit: the budget is gone until the window resets.
            delay = max(0.0, state.reset_at - self._wall_clock()) + 1.0
            reason = "primary rate limit reset"
        elif is_secondary_rate_limit(response):
            # No header to go on. GitHub's guidance is to wait at least a
            # minute rather than retry straight away.
            delay = max(60.0, backoff_delay(attempt, self._policy, rng=self._rng))
            reason = "secondary rate limit"
        else:
            delay = backoff_delay(attempt, self._policy, rng=self._rng)
            reason = "rate limit"

        if delay > self._policy.max_rate_limit_wait_seconds:
            raise RateLimited(
                f"{reason} on {safe_url} needs a {delay:.0f}s wait, over the "
                f"{self._policy.max_rate_limit_wait_seconds:.0f}s budget. "
                f"Stopping rather than blocking indefinitely."
            )

        logger.warning("%s on %s, waiting %.1fs", reason, safe_url, delay)
        self._sleep(delay)
        return delay

    def _back_off(self, attempt: int) -> float:
        delay = backoff_delay(attempt, self._policy, rng=self._rng)
        self._sleep(delay)
        return delay


def _error_message(response: HttpResponse) -> str:
    try:
        body = json.loads(response.text)
    except (json.JSONDecodeError, TypeError):
        return redact_text(response.text[:200])
    if isinstance(body, Mapping):
        return redact_text(str(body.get("message", ""))[:200])
    return ""
