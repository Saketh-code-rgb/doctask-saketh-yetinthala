"""Phase 1 smoke test: the CLI help path works.

Scope is deliberately limited to the bootstrap. No later-phase behaviour is
exercised here.
"""

import subprocess
import sys

from click.testing import CliRunner

from dependency_map import __version__
from dependency_map.cli import cli


def test_help_exits_zero():
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output


def test_help_mentions_what_the_tool_does():
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Dependency Map" in result.output


def test_version_option():
    result = CliRunner().invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_module_invocation_exits_zero():
    """`python -m dependency_map --help` is the Phase 1 definition of done."""
    completed = subprocess.run(
        [sys.executable, "-m", "dependency_map", "--help"],
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0
    assert "Usage:" in completed.stdout
