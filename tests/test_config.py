"""Configuration loading, secret precedence, and weight validation.

Every test builds its own config directory under tmp_path and controls the
environment with monkeypatch. No test reads a real credential, and no test
depends on the developer's actual environment.
"""

from __future__ import annotations

from decimal import Decimal
from pathlib import Path

import click
import pytest
import yaml
from click.testing import CliRunner

from dependency_map.cli import cli, config_from_context
from dependency_map.config import (
    GITHUB_TOKEN_VAR,
    LIBRARIES_IO_KEY_VAR,
    CliOverrides,
    ConfigFileMissing,
    InvalidConfig,
    InvalidWeights,
    MissingSecret,
    load_config,
    load_secrets,
    load_weights,
)
from dependency_map.db import SCORING_DIMENSIONS

FAKE_TOKEN = "ghp_fake000000000000000000000000000000"
FAKE_KEY = "libraries_io_fake_key_0000"

VALID_SETTINGS = {
    "paths": {
        "database": "data/dependency_map.db",
        "library_universe": "data/library-universe.yaml",
        "output_csv": "outputs/ranked-candidates.csv",
        "output_markdown": "outputs/dependency-map-report.md",
    },
    "cache": {"ttl_days": 7},
    "pacing": {
        "github_code_search_min_interval_seconds": 6.5,
        "github_search_min_interval_seconds": 2.0,
        "github_rest_min_interval_seconds": 0.75,
        "libraries_io_min_interval_seconds": 1.0,
    },
    "retry": {
        "max_attempts": 3,
        "backoff_base_seconds": 2.0,
        "backoff_jitter_seconds": 0.5,
        "backoff_max_seconds": 60.0,
    },
}

VALID_WEIGHTS = {
    "dimension_weights": {
        "document_volume": 0.15,
        "document_complexity": 0.15,
        "business_criticality": 0.20,
        "pipeline_complexity": 0.20,
        "maintenance_burden": 0.15,
        "build_vs_buy_signal": 0.10,
        "commercial_leverage": 0.05,
    },
    "gate_caps": {
        "code_usage_unconfirmed": 20,
        "document_code_outside_production": 25,
        "single_category_no_infrastructure": 40,
    },
}


def _write(path: Path, data) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    return path


@pytest.fixture
def config_dir(tmp_path):
    """A valid config directory."""
    directory = tmp_path / "config"
    _write(directory / "config.yaml", VALID_SETTINGS)
    _write(directory / "weights.yaml", VALID_WEIGHTS)
    return directory


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    """No test inherits the developer's real credentials."""
    monkeypatch.delenv(GITHUB_TOKEN_VAR, raising=False)
    monkeypatch.delenv(LIBRARIES_IO_KEY_VAR, raising=False)


@pytest.fixture
def token(monkeypatch):
    monkeypatch.setenv(GITHUB_TOKEN_VAR, FAKE_TOKEN)
    return FAKE_TOKEN


# --- successful loading ----------------------------------------------------


def test_load_config_returns_every_section(config_dir, token):
    config = load_config(config_dir, env_file=None)

    assert config.paths.database == Path("data/dependency_map.db")
    assert config.paths.output_csv == Path("outputs/ranked-candidates.csv")
    assert config.cache.ttl_days == 7
    assert config.retry.max_attempts == 3
    assert config.pacing.github_code_search_min_interval_seconds == 6.5
    assert config.secrets.github_token == FAKE_TOKEN


def test_pacing_stays_under_the_ten_per_minute_code_search_cap(config_dir, token):
    """TECHNICAL_DESIGN.md section 14: roughly one call every 6 to 7 seconds."""
    interval = load_config(
        config_dir, env_file=None
    ).pacing.github_code_search_min_interval_seconds
    assert 60 / interval <= 10


def test_each_github_bucket_has_its_own_pacing(config_dir, token):
    """GitHub keeps three separate rate-limit buckets. Sharing one interval
    would throttle core REST to the pace of code search."""
    pacing = load_config(config_dir, env_file=None).pacing

    assert pacing.github_code_search_min_interval_seconds == 6.5
    assert pacing.github_search_min_interval_seconds == 2.0
    assert pacing.github_rest_min_interval_seconds == 0.75
    assert (
        pacing.github_rest_min_interval_seconds
        < pacing.github_search_min_interval_seconds
        < pacing.github_code_search_min_interval_seconds
    )


def test_backoff_is_bounded(config_dir, token):
    retry = load_config(config_dir, env_file=None).retry

    assert retry.backoff_max_seconds == 60.0
    assert retry.backoff_max_seconds > retry.backoff_base_seconds


def test_missing_config_file_is_reported(tmp_path, token):
    with pytest.raises(ConfigFileMissing, match="config"):
        load_config(tmp_path / "nowhere", env_file=None)


def test_missing_weights_file_is_reported(tmp_path, token):
    _write(tmp_path / "config" / "config.yaml", VALID_SETTINGS)
    with pytest.raises(ConfigFileMissing, match="weights"):
        load_config(tmp_path / "config", env_file=None)


@pytest.mark.parametrize("section", ["paths", "cache", "pacing", "retry"])
def test_missing_section_fails(tmp_path, token, section):
    settings = {k: v for k, v in VALID_SETTINGS.items() if k != section}
    directory = tmp_path / "config"
    _write(directory / "config.yaml", settings)
    _write(directory / "weights.yaml", VALID_WEIGHTS)

    with pytest.raises(InvalidConfig, match=section):
        load_config(directory, env_file=None)


def test_zero_cache_ttl_is_rejected(tmp_path, token):
    settings = {**VALID_SETTINGS, "cache": {"ttl_days": 0}}
    directory = tmp_path / "config"
    _write(directory / "config.yaml", settings)
    _write(directory / "weights.yaml", VALID_WEIGHTS)

    with pytest.raises(InvalidConfig, match="greater than zero"):
        load_config(directory, env_file=None)


# --- the real shipped files ------------------------------------------------


def test_the_repositorys_own_config_files_load(token):
    """Guards the actual config/ directory, not just synthetic fixtures."""
    config = load_config(Path("config"), env_file=None)

    assert config.cache.ttl_days == 7
    assert set(config.weights.dimension_weights) == set(SCORING_DIMENSIONS)


def test_the_repositorys_own_weights_sum_to_one():
    weights = load_weights(Path("config") / "weights.yaml")
    total = sum(Decimal(str(v)) for v in weights.dimension_weights.values())

    assert total == Decimal(1)


def test_the_repositorys_own_weights_match_the_scoring_model():
    """SCORING_MODEL.md section 10, transcribed exactly."""
    weights = load_weights(Path("config") / "weights.yaml").dimension_weights

    assert weights == {
        "document_volume": 0.15,
        "document_complexity": 0.15,
        "business_criticality": 0.20,
        "pipeline_complexity": 0.20,
        "maintenance_burden": 0.15,
        "build_vs_buy_signal": 0.10,
        "commercial_leverage": 0.05,
    }


def test_the_repositorys_own_gate_caps_match_the_scoring_model():
    """SCORING_MODEL.md section 14: caps of 20, 25 and 40."""
    caps = load_weights(Path("config") / "weights.yaml").gate_caps

    assert caps == {
        "code_usage_unconfirmed": 20,
        "document_code_outside_production": 25,
        "single_category_no_infrastructure": 40,
    }


def test_shipped_config_contains_no_secret_keys():
    """A credential must never be committed in a YAML file."""
    text = (Path("config") / "config.yaml").read_text(encoding="utf-8")
    data = yaml.safe_load(text)

    assert GITHUB_TOKEN_VAR not in data
    assert LIBRARIES_IO_KEY_VAR not in data
    assert "ghp_" not in text


# --- weights validation ----------------------------------------------------


def test_weights_that_do_not_sum_to_one_fail(tmp_path):
    """The check IMPLEMENTATION_PLAN.md phase 3 task 4 asks for."""
    broken = {
        **VALID_WEIGHTS,
        "dimension_weights": {**VALID_WEIGHTS["dimension_weights"],
                              "document_volume": 0.25},
    }
    path = _write(tmp_path / "weights.yaml", broken)

    with pytest.raises(InvalidWeights) as excinfo:
        load_weights(path)

    message = str(excinfo.value)
    assert "1.0" in message
    assert "1.10" in message  # the actual sum, so the typo is findable


def test_weights_summing_just_under_one_fail(tmp_path):
    """0.999 is wrong, and being close doesn't make it right."""
    broken = {
        **VALID_WEIGHTS,
        "dimension_weights": {**VALID_WEIGHTS["dimension_weights"],
                              "commercial_leverage": 0.049},
    }
    path = _write(tmp_path / "weights.yaml", broken)

    with pytest.raises(InvalidWeights, match="0.999"):
        load_weights(path)


def test_broken_weights_stop_load_config(tmp_path, token):
    """Invalid weights fail at startup, not later during scoring."""
    directory = tmp_path / "config"
    _write(directory / "config.yaml", VALID_SETTINGS)
    _write(
        directory / "weights.yaml",
        {**VALID_WEIGHTS,
         "dimension_weights": {**VALID_WEIGHTS["dimension_weights"],
                               "maintenance_burden": 0.5}},
    )

    with pytest.raises(InvalidWeights):
        load_config(directory, env_file=None)


def test_missing_dimension_fails(tmp_path):
    weights = dict(VALID_WEIGHTS["dimension_weights"])
    del weights["maintenance_burden"]
    path = _write(tmp_path / "weights.yaml", {**VALID_WEIGHTS,
                                              "dimension_weights": weights})

    with pytest.raises(InvalidWeights, match="maintenance_burden"):
        load_weights(path)


def test_unknown_dimension_fails(tmp_path):
    weights = {**VALID_WEIGHTS["dimension_weights"], "vibes": 0.0}
    path = _write(tmp_path / "weights.yaml", {**VALID_WEIGHTS,
                                              "dimension_weights": weights})

    with pytest.raises(InvalidWeights, match="vibes"):
        load_weights(path)


def test_negative_weight_fails(tmp_path):
    weights = {**VALID_WEIGHTS["dimension_weights"],
               "document_volume": -0.15, "business_criticality": 0.50}
    path = _write(tmp_path / "weights.yaml", {**VALID_WEIGHTS,
                                              "dimension_weights": weights})

    with pytest.raises(InvalidWeights, match="negative"):
        load_weights(path)


def test_non_numeric_weight_fails(tmp_path):
    weights = {**VALID_WEIGHTS["dimension_weights"], "document_volume": "heavy"}
    path = _write(tmp_path / "weights.yaml", {**VALID_WEIGHTS,
                                              "dimension_weights": weights})

    with pytest.raises(InvalidWeights, match="must be a number"):
        load_weights(path)


def test_weight_lookup_by_dimension(tmp_path):
    weights = load_weights(_write(tmp_path / "weights.yaml", VALID_WEIGHTS))

    assert weights.weight_for("business_criticality") == 0.20
    with pytest.raises(InvalidWeights):
        weights.weight_for("not_a_dimension")


# --- gate thresholds -------------------------------------------------------


def test_gate_caps_load(tmp_path):
    caps = load_weights(_write(tmp_path / "weights.yaml", VALID_WEIGHTS)).gate_caps

    assert caps["code_usage_unconfirmed"] == 20
    assert caps["document_code_outside_production"] == 25
    assert caps["single_category_no_infrastructure"] == 40


def test_missing_gate_cap_fails(tmp_path):
    caps = dict(VALID_WEIGHTS["gate_caps"])
    del caps["code_usage_unconfirmed"]
    path = _write(tmp_path / "weights.yaml", {**VALID_WEIGHTS, "gate_caps": caps})

    with pytest.raises(InvalidWeights, match="code_usage_unconfirmed"):
        load_weights(path)


def test_unknown_gate_cap_fails(tmp_path):
    caps = {**VALID_WEIGHTS["gate_caps"], "made_up_rule": 50}
    path = _write(tmp_path / "weights.yaml", {**VALID_WEIGHTS, "gate_caps": caps})

    with pytest.raises(InvalidWeights, match="made_up_rule"):
        load_weights(path)


def test_out_of_range_gate_cap_fails(tmp_path):
    caps = {**VALID_WEIGHTS["gate_caps"], "code_usage_unconfirmed": 140}
    path = _write(tmp_path / "weights.yaml", {**VALID_WEIGHTS, "gate_caps": caps})

    with pytest.raises(InvalidWeights, match="between 0 and 100"):
        load_weights(path)


def test_missing_gate_caps_section_fails(tmp_path):
    path = _write(tmp_path / "weights.yaml",
                  {"dimension_weights": VALID_WEIGHTS["dimension_weights"]})

    with pytest.raises(InvalidWeights, match="gate_caps"):
        load_weights(path)


# --- secrets ---------------------------------------------------------------


def test_secrets_come_from_the_environment(monkeypatch):
    monkeypatch.setenv(GITHUB_TOKEN_VAR, FAKE_TOKEN)
    monkeypatch.setenv(LIBRARIES_IO_KEY_VAR, FAKE_KEY)

    secrets = load_secrets(env_file=None)

    assert secrets.github_token == FAKE_TOKEN
    assert secrets.libraries_io_api_key == FAKE_KEY


def test_missing_github_token_fails_loudly(config_dir):
    with pytest.raises(MissingSecret) as excinfo:
        load_config(config_dir, env_file=None)

    message = str(excinfo.value)
    assert GITHUB_TOKEN_VAR in message
    assert ".env" in message  # the message names the fix


def test_blank_github_token_counts_as_missing(config_dir, monkeypatch):
    monkeypatch.setenv(GITHUB_TOKEN_VAR, "   ")

    with pytest.raises(MissingSecret):
        load_config(config_dir, env_file=None)


def test_offline_commands_can_load_without_a_token(config_dir):
    """Report generation reads a local database and needs no credential."""
    config = load_config(config_dir, env_file=None, require_github_token=False)

    assert config.secrets.github_token is None
    assert config.cache.ttl_days == 7


def test_libraries_io_key_is_optional(config_dir, token):
    config = load_config(config_dir, env_file=None)

    assert config.secrets.libraries_io_api_key is None


def test_require_github_token_helper(config_dir, token):
    assert load_config(config_dir, env_file=None).require_github_token() == FAKE_TOKEN


def test_require_github_token_helper_raises_when_absent(config_dir):
    config = load_config(config_dir, env_file=None, require_github_token=False)

    with pytest.raises(MissingSecret):
        config.require_github_token()


# --- .env loading and precedence -------------------------------------------


def test_dotenv_file_is_loaded(tmp_path, config_dir):
    env_file = tmp_path / ".env"
    env_file.write_text(
        f"{GITHUB_TOKEN_VAR}={FAKE_TOKEN}\n{LIBRARIES_IO_KEY_VAR}={FAKE_KEY}\n",
        encoding="utf-8",
    )

    config = load_config(config_dir, env_file=env_file)

    assert config.secrets.github_token == FAKE_TOKEN
    assert config.secrets.libraries_io_api_key == FAKE_KEY


def test_environment_beats_dotenv(tmp_path, config_dir, monkeypatch):
    """The required precedence: a real environment variable wins over the file,
    so CI or a deployed environment overrides whatever is on disk."""
    env_file = tmp_path / ".env"
    env_file.write_text(f"{GITHUB_TOKEN_VAR}=from_the_dotenv_file\n", encoding="utf-8")
    monkeypatch.setenv(GITHUB_TOKEN_VAR, "from_the_real_environment")

    config = load_config(config_dir, env_file=env_file)

    assert config.secrets.github_token == "from_the_real_environment"


def test_missing_dotenv_file_is_not_an_error(config_dir, monkeypatch, tmp_path):
    monkeypatch.setenv(GITHUB_TOKEN_VAR, FAKE_TOKEN)

    config = load_config(config_dir, env_file=tmp_path / "nope.env")

    assert config.secrets.github_token == FAKE_TOKEN


def test_secrets_never_come_from_yaml(tmp_path, monkeypatch):
    """A token planted in config.yaml must be ignored, not picked up."""
    directory = tmp_path / "config"
    _write(directory / "config.yaml",
           {**VALID_SETTINGS, GITHUB_TOKEN_VAR: "ghp_planted_in_yaml"})
    _write(directory / "weights.yaml", VALID_WEIGHTS)
    monkeypatch.setenv(GITHUB_TOKEN_VAR, FAKE_TOKEN)

    config = load_config(directory, env_file=None)

    assert config.secrets.github_token == FAKE_TOKEN


# --- secrets never reach a log ---------------------------------------------


def test_repr_of_secrets_hides_the_values(config_dir, monkeypatch):
    monkeypatch.setenv(GITHUB_TOKEN_VAR, FAKE_TOKEN)
    monkeypatch.setenv(LIBRARIES_IO_KEY_VAR, FAKE_KEY)
    secrets = load_secrets(env_file=None)

    for rendering in (repr(secrets), str(secrets), f"{secrets}"):
        assert FAKE_TOKEN not in rendering
        assert FAKE_KEY not in rendering
        assert "<set>" in rendering


def test_repr_of_config_hides_secret_values(config_dir, token):
    config = load_config(config_dir, env_file=None)

    assert FAKE_TOKEN not in repr(config)
    assert FAKE_TOKEN not in str(config)


def test_repr_distinguishes_set_from_unset(config_dir, token):
    rendering = repr(load_config(config_dir, env_file=None).secrets)

    assert "github_token=<set>" in rendering
    assert "libraries_io_api_key=<unset>" in rendering


# --- CLI overrides ---------------------------------------------------------


def test_override_output_paths(config_dir, token):
    overrides = CliOverrides(
        output_csv=Path("/tmp/custom.csv"),
        output_markdown=Path("/tmp/custom.md"),
    )
    config = load_config(config_dir, env_file=None, overrides=overrides)

    assert config.paths.output_csv == Path("/tmp/custom.csv")
    assert config.paths.output_markdown == Path("/tmp/custom.md")


def test_override_cache_ttl(config_dir, token):
    config = load_config(
        config_dir, env_file=None, overrides=CliOverrides(cache_ttl_days=1)
    )

    assert config.cache.ttl_days == 1


def test_overrides_are_partial(config_dir, token):
    """Overriding one setting leaves the rest of the file in force."""
    config = load_config(
        config_dir, env_file=None, overrides=CliOverrides(cache_ttl_days=2)
    )

    assert config.cache.ttl_days == 2
    assert config.paths.output_csv == Path("outputs/ranked-candidates.csv")


def test_no_overrides_uses_file_values(config_dir, token):
    config = load_config(config_dir, env_file=None, overrides=CliOverrides())

    assert config.cache.ttl_days == 7
    assert CliOverrides().is_empty()


def test_invalid_override_ttl_is_rejected(config_dir, token):
    with pytest.raises(InvalidConfig):
        load_config(
            config_dir, env_file=None, overrides=CliOverrides(cache_ttl_days=-5)
        )


def test_cli_flags_reach_the_override_object(config_dir, token):
    """The flags parse and produce a Config, end to end through click."""
    seen = {}

    @cli.command("probe")
    @click.pass_context
    def probe(ctx):
        seen["config"] = config_from_context(ctx)

    try:
        result = CliRunner().invoke(
            cli,
            [
                "--config-dir", str(config_dir),
                "--output-csv", "custom/out.csv",
                "--cache-ttl-days", "3",
                "probe",
            ],
        )
        assert result.exit_code == 0, result.output
        assert seen["config"].paths.output_csv == Path("custom/out.csv")
        assert seen["config"].cache.ttl_days == 3
        # Untouched settings still come from the file.
        assert seen["config"].paths.output_markdown == Path(
            "outputs/dependency-map-report.md"
        )
    finally:
        cli.commands.pop("probe", None)


def test_cli_help_works_without_a_token():
    """Config is not loaded at group level, so --help stays usable with no
    credential present. Phase 1's definition of done depends on this."""
    result = CliRunner().invoke(cli, ["--help"])

    assert result.exit_code == 0
    assert "--cache-ttl-days" in result.output
    assert "--output-csv" in result.output
