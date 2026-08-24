"""Configuration loading.

Three sources, with a deliberate split between them:

- config/config.yaml   non-secret runtime settings
- config/weights.yaml  scoring weights and gate thresholds, as data so a human
                       can tune them without touching code
- the environment      secrets, and nothing else

Secrets never come from a YAML file. A .env file is loaded for local
development, but a real environment variable always wins over it, so a
deployed or CI environment can override whatever happens to be on disk
(TECHNICAL_DESIGN.md sections 4 and 19).

Loading fails loudly rather than proceeding with something wrong: a missing
GITHUB_TOKEN or a weights file that doesn't sum to 1.0 stops startup, because
both produce silently incorrect results otherwise.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Mapping

import yaml
from dotenv import load_dotenv

from .db import SCORING_DIMENSIONS

#: Environment variable names. Values live only in the environment.
GITHUB_TOKEN_VAR = "GITHUB_TOKEN"
LIBRARIES_IO_KEY_VAR = "LIBRARIES_IO_API_KEY"

#: The three caps from SCORING_MODEL.md section 14.
GATE_CAP_NAMES: tuple[str, ...] = (
    "code_usage_unconfirmed",
    "document_code_outside_production",
    "single_category_no_infrastructure",
)

DEFAULT_CONFIG_DIR = Path("config")
DEFAULT_ENV_FILE = Path(".env")

_REDACTED = "<set>"
_ABSENT = "<unset>"


class ConfigError(Exception):
    """Base class for every configuration failure."""


class ConfigFileMissing(ConfigError):
    """A required YAML file isn't where it was expected."""


class MissingSecret(ConfigError):
    """A required secret isn't present in the environment."""


class InvalidWeights(ConfigError):
    """weights.yaml is malformed, or its weights don't sum to 1.0."""


class InvalidConfig(ConfigError):
    """config.yaml is malformed or missing a required setting."""


# --- value objects ---------------------------------------------------------


@dataclass(frozen=True)
class Paths:
    database: Path
    library_universe: Path
    output_csv: Path
    output_markdown: Path


@dataclass(frozen=True)
class Pacing:
    """Minimum spacing per rate-limit bucket.

    GitHub keeps three separate buckets (code search at 10/minute, other
    search at 30/minute, core REST at 5,000/hour), so one shared interval
    would throttle the cheap calls to the pace of the expensive ones.
    """

    github_code_search_min_interval_seconds: float
    github_search_min_interval_seconds: float
    github_rest_min_interval_seconds: float
    libraries_io_min_interval_seconds: float


@dataclass(frozen=True)
class Retry:
    max_attempts: int
    backoff_base_seconds: float
    backoff_jitter_seconds: float
    backoff_max_seconds: float = 60.0


@dataclass(frozen=True)
class Cache:
    ttl_days: int


@dataclass(frozen=True)
class Secrets:
    """Credentials read from the environment.

    Never rendered. repr() shows only whether each value is present, so a
    secret cannot reach a log line, a traceback, or a debugger transcript by
    accident (TECHNICAL_DESIGN.md section 19).
    """

    github_token: str | None = field(default=None, repr=False)
    libraries_io_api_key: str | None = field(default=None, repr=False)

    def __repr__(self) -> str:
        return (
            f"Secrets(github_token={_REDACTED if self.github_token else _ABSENT}, "
            f"libraries_io_api_key="
            f"{_REDACTED if self.libraries_io_api_key else _ABSENT})"
        )

    __str__ = __repr__


@dataclass(frozen=True)
class Weights:
    """Scoring weights and gate caps, validated at load time."""

    dimension_weights: Mapping[str, float]
    gate_caps: Mapping[str, int]

    def weight_for(self, dimension: str) -> float:
        try:
            return self.dimension_weights[dimension]
        except KeyError:
            raise InvalidWeights(f"No weight for dimension {dimension!r}") from None


@dataclass(frozen=True)
class Config:
    paths: Paths
    cache: Cache
    pacing: Pacing
    retry: Retry
    weights: Weights
    secrets: Secrets

    def require_github_token(self) -> str:
        """Return the token, or fail with a message that names the fix."""
        if not self.secrets.github_token:
            raise MissingSecret(_missing_token_message())
        return self.secrets.github_token


@dataclass(frozen=True)
class CliOverrides:
    """Per-run overrides for the settings the design calls out as likely to
    vary between runs: output paths and cache TTL.

    Deliberately narrow. This is not a generic override system for every
    setting in the file (IMPLEMENTATION_PLAN.md phase 3 task 3).
    """

    output_csv: Path | None = None
    output_markdown: Path | None = None
    cache_ttl_days: int | None = None

    def is_empty(self) -> bool:
        return (
            self.output_csv is None
            and self.output_markdown is None
            and self.cache_ttl_days is None
        )


# --- helpers ---------------------------------------------------------------


def _missing_token_message() -> str:
    return (
        f"{GITHUB_TOKEN_VAR} is not set. GitHub code search is unavailable "
        f"without it. Copy .env.example to .env and fill it in, or export "
        f"{GITHUB_TOKEN_VAR} in your environment. The value never goes into a "
        f"YAML file."
    )


def _load_yaml(path: Path, kind: str) -> dict[str, Any]:
    if not path.is_file():
        raise ConfigFileMissing(f"No {kind} file at {path}")
    try:
        loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ConfigError(f"{path} is not valid YAML: {exc}") from exc
    if loaded is None:
        loaded = {}
    if not isinstance(loaded, dict):
        raise ConfigError(f"{path} must contain a mapping, found {type(loaded).__name__}")
    return loaded


def _section(data: Mapping[str, Any], name: str, path: Path) -> Mapping[str, Any]:
    value = data.get(name)
    if value is None:
        raise InvalidConfig(f"{path} is missing the '{name}' section")
    if not isinstance(value, Mapping):
        raise InvalidConfig(f"{path}: '{name}' must be a mapping")
    return value


def _required(section: Mapping[str, Any], key: str, name: str, path: Path) -> Any:
    if key not in section:
        raise InvalidConfig(f"{path}: '{name}' is missing '{key}'")
    return section[key]


def _as_number(value: Any, where: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InvalidConfig(f"{where} must be a number, found {value!r}")
    return float(value)


def _as_positive_int(value: Any, where: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise InvalidConfig(f"{where} must be an integer, found {value!r}")
    if value <= 0:
        raise InvalidConfig(f"{where} must be greater than zero, found {value}")
    return value


# --- weights ---------------------------------------------------------------


def _exact(value: Any, dimension: str) -> Decimal:
    """Convert a YAML number to an exact decimal.

    Decimal(str(0.15)) is Decimal('0.15'), so summing this way asks whether the
    weights sum to exactly 1.0 as written, rather than to within some binary
    floating-point tolerance.
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InvalidWeights(
            f"Weight for {dimension!r} must be a number, found {value!r}"
        )
    try:
        return Decimal(str(value))
    except InvalidOperation:
        raise InvalidWeights(f"Weight for {dimension!r} is not a number: {value!r}") from None


def load_weights(weights_path: Path) -> Weights:
    """Load and validate weights.yaml.

    Refuses anything that would silently distort a ranking: a missing or extra
    dimension, a negative weight, a missing gate cap, or a set of weights that
    doesn't sum to exactly 1.0.
    """
    data = _load_yaml(weights_path, "weights")

    raw_weights = data.get("dimension_weights")
    if raw_weights is None:
        raise InvalidWeights(f"{weights_path} is missing 'dimension_weights'")
    if not isinstance(raw_weights, Mapping):
        raise InvalidWeights(f"{weights_path}: 'dimension_weights' must be a mapping")

    expected = set(SCORING_DIMENSIONS)
    found = set(raw_weights)
    if missing := sorted(expected - found):
        raise InvalidWeights(f"{weights_path} is missing weights for: {missing}")
    if extra := sorted(found - expected):
        raise InvalidWeights(f"{weights_path} has weights for unknown dimensions: {extra}")

    exact: dict[str, Decimal] = {}
    for dimension in SCORING_DIMENSIONS:
        value = _exact(raw_weights[dimension], dimension)
        if value < 0:
            raise InvalidWeights(f"Weight for {dimension!r} is negative: {value}")
        exact[dimension] = value

    total = sum(exact.values(), Decimal(0))
    if total != Decimal(1):
        breakdown = ", ".join(f"{d}={exact[d]}" for d in SCORING_DIMENSIONS)
        raise InvalidWeights(
            f"Dimension weights in {weights_path} sum to {total}, not 1.0. "
            f"A ranking built on these would be silently wrong. "
            f"Weights: {breakdown}"
        )

    raw_caps = data.get("gate_caps")
    if raw_caps is None:
        raise InvalidWeights(f"{weights_path} is missing 'gate_caps'")
    if not isinstance(raw_caps, Mapping):
        raise InvalidWeights(f"{weights_path}: 'gate_caps' must be a mapping")

    if missing_caps := sorted(set(GATE_CAP_NAMES) - set(raw_caps)):
        raise InvalidWeights(f"{weights_path} is missing gate caps for: {missing_caps}")
    if extra_caps := sorted(set(raw_caps) - set(GATE_CAP_NAMES)):
        raise InvalidWeights(f"{weights_path} has unknown gate caps: {extra_caps}")

    caps: dict[str, int] = {}
    for name in GATE_CAP_NAMES:
        value = raw_caps[name]
        if isinstance(value, bool) or not isinstance(value, int):
            raise InvalidWeights(f"Gate cap {name!r} must be an integer, found {value!r}")
        if not 0 <= value <= 100:
            raise InvalidWeights(
                f"Gate cap {name!r} must be between 0 and 100, found {value}"
            )
        caps[name] = value

    return Weights(
        dimension_weights={d: float(exact[d]) for d in SCORING_DIMENSIONS},
        gate_caps=caps,
    )


# --- settings --------------------------------------------------------------


def _load_settings(config_path: Path, overrides: CliOverrides) -> tuple[Paths, Cache, Pacing, Retry]:
    data = _load_yaml(config_path, "config")

    paths_section = _section(data, "paths", config_path)
    paths = Paths(
        database=Path(_required(paths_section, "database", "paths", config_path)),
        library_universe=Path(
            _required(paths_section, "library_universe", "paths", config_path)
        ),
        output_csv=overrides.output_csv
        or Path(_required(paths_section, "output_csv", "paths", config_path)),
        output_markdown=overrides.output_markdown
        or Path(_required(paths_section, "output_markdown", "paths", config_path)),
    )

    cache_section = _section(data, "cache", config_path)
    ttl = (
        overrides.cache_ttl_days
        if overrides.cache_ttl_days is not None
        else _required(cache_section, "ttl_days", "cache", config_path)
    )
    cache = Cache(ttl_days=_as_positive_int(ttl, "cache.ttl_days"))

    pacing_section = _section(data, "pacing", config_path)
    pacing = Pacing(
        github_code_search_min_interval_seconds=_as_number(
            _required(
                pacing_section,
                "github_code_search_min_interval_seconds",
                "pacing",
                config_path,
            ),
            "pacing.github_code_search_min_interval_seconds",
        ),
        github_search_min_interval_seconds=_as_number(
            _required(
                pacing_section,
                "github_search_min_interval_seconds",
                "pacing",
                config_path,
            ),
            "pacing.github_search_min_interval_seconds",
        ),
        github_rest_min_interval_seconds=_as_number(
            _required(
                pacing_section, "github_rest_min_interval_seconds", "pacing", config_path
            ),
            "pacing.github_rest_min_interval_seconds",
        ),
        libraries_io_min_interval_seconds=_as_number(
            _required(
                pacing_section, "libraries_io_min_interval_seconds", "pacing", config_path
            ),
            "pacing.libraries_io_min_interval_seconds",
        ),
    )

    retry_section = _section(data, "retry", config_path)
    retry = Retry(
        max_attempts=_as_positive_int(
            _required(retry_section, "max_attempts", "retry", config_path),
            "retry.max_attempts",
        ),
        backoff_base_seconds=_as_number(
            _required(retry_section, "backoff_base_seconds", "retry", config_path),
            "retry.backoff_base_seconds",
        ),
        backoff_jitter_seconds=_as_number(
            _required(retry_section, "backoff_jitter_seconds", "retry", config_path),
            "retry.backoff_jitter_seconds",
        ),
        backoff_max_seconds=_as_number(
            _required(retry_section, "backoff_max_seconds", "retry", config_path),
            "retry.backoff_max_seconds",
        ),
    )

    return paths, cache, pacing, retry


# --- secrets ---------------------------------------------------------------


def load_secrets(env_file: Path | None = DEFAULT_ENV_FILE) -> Secrets:
    """Read credentials from the environment, after loading .env if present.

    load_dotenv is called with override=False, so a variable already set in the
    real environment beats whatever the file says. That is the precedence the
    design asks for: .env is a local convenience, not the authority.
    """
    if env_file is not None and Path(env_file).is_file():
        load_dotenv(env_file, override=False)

    def _read(name: str) -> str | None:
        value = os.environ.get(name)
        if value is None:
            return None
        value = value.strip()
        return value or None

    return Secrets(
        github_token=_read(GITHUB_TOKEN_VAR),
        libraries_io_api_key=_read(LIBRARIES_IO_KEY_VAR),
    )


# --- entry point -----------------------------------------------------------


def load_config(
    config_dir: Path | str = DEFAULT_CONFIG_DIR,
    *,
    env_file: Path | str | None = DEFAULT_ENV_FILE,
    overrides: CliOverrides | None = None,
    require_github_token: bool = True,
) -> Config:
    """Load settings, weights, and secrets into one validated Config.

    require_github_token defaults to True so a run that will make API calls
    stops immediately rather than failing partway through. Commands that touch
    no network (report generation, for one) pass False, since demanding a
    credential to read a local database would be theatre.

    LIBRARIES_IO_API_KEY is never required: SEARCH_STRATEGY.md section 9 still
    lists obtaining one as unconfirmed, so its absence degrades discovery
    rather than blocking a run.
    """
    config_dir = Path(config_dir)
    overrides = overrides or CliOverrides()

    paths, cache, pacing, retry = _load_settings(config_dir / "config.yaml", overrides)
    weights = load_weights(config_dir / "weights.yaml")
    secrets = load_secrets(Path(env_file) if env_file is not None else None)

    if require_github_token and not secrets.github_token:
        raise MissingSecret(_missing_token_message())

    return Config(
        paths=paths,
        cache=cache,
        pacing=pacing,
        retry=retry,
        weights=weights,
        secrets=secrets,
    )
