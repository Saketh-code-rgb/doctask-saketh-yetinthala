"""Command-line entry point.

Commands: `discover`, `run`, `runs`, `report`.

Configuration is deliberately *not* loaded at group level. Loading requires a
GITHUB_TOKEN, and `--help` has to work without one.
"""

from __future__ import annotations

from pathlib import Path

import click

from . import __version__
from .config import DEFAULT_CONFIG_DIR, CliOverrides, load_config


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=__version__, prog_name="dependency-map")
@click.option(
    "--config-dir",
    type=click.Path(file_okay=False, path_type=Path),
    default=DEFAULT_CONFIG_DIR,
    show_default=True,
    help="Directory holding config.yaml and weights.yaml.",
)
@click.option(
    "--output-csv",
    type=click.Path(dir_okay=False, path_type=Path),
    default=None,
    help="Override the ranked CSV output path for this run.",
)
@click.option(
    "--output-markdown",
    type=click.Path(dir_okay=False, path_type=Path),
    default=None,
    help="Override the Markdown report output path for this run.",
)
@click.option(
    "--cache-ttl-days",
    type=int,
    default=None,
    help="Override how long a cached API response stays usable.",
)
@click.pass_context
def cli(
    ctx: click.Context,
    config_dir: Path,
    output_csv: Path | None,
    output_markdown: Path | None,
    cache_ttl_days: int | None,
) -> None:
    """Dependency Map.

    Discovers public repositories that show evidence of a homegrown document
    generation, editing, or conversion pipeline, then qualifies and ranks them.

    Run a pipeline stage with `run`, inspect recorded runs with `runs`, and
    publish a run's ranked table with `report`. `discover` is the standalone
    discovery stage. See DEMO.md for a worked sequence.
    """
    ctx.ensure_object(dict)
    ctx.obj["config_dir"] = config_dir
    ctx.obj["overrides"] = CliOverrides(
        output_csv=output_csv,
        output_markdown=output_markdown,
        cache_ttl_days=cache_ttl_days,
    )


@cli.command("discover")
@click.option("--run-id", default=None, help="Run identifier. Defaults to run_N.")
@click.option("--tier", "tiers", type=int, multiple=True,
              help="Restrict to these discovery tiers. Repeatable.")
@click.option("--limit", type=int, default=None,
              help="Stop after this many queries. Useful for a controlled pass.")
@click.option("--per-page", type=int, default=30, show_default=True,
              help="Results requested per query.")
@click.pass_context
def discover(ctx, run_id, tiers, limit, per_page):
    """Run the discovery stage and record what the queries returned."""
    from .db import open_database
    from .dedup import plan_rotation, run_stats, verify_fresh_batch
    from .discovery import DiscoveryEngine, QueryGenerator
    from .clients.github_client import GitHubClient
    from .library_universe import load_library_universe
    from .reliability import (
        ReliabilityPolicy, ReliableRequester, RequestsTransport, SqliteCacheStore,
    )
    from . import storage

    config = config_from_context(ctx)
    universe = load_library_universe(config.paths.library_universe)

    with open_database(config.paths.database) as conn:
        run_index = len(storage.list_runs(conn)) + 1
        run_id = run_id or f"run_{run_index}"

        # The rotation is planned before the run starts and recorded in
        # runs.notes, so how this run differs from the last is legible from the
        # database without reconstructing it.
        rotation = plan_rotation(run_index)
        storage.create_run(conn, run_id, notes=rotation.description)

        generator = QueryGenerator(
            universe,
            windows=rotation.windows,
            library_offset=rotation.library_offset,
        )
        planned = generator.generate(tiers or (1, 2, 3))
        if limit is not None:
            planned = planned[:limit]

        # Refuse to replay an earlier run rather than discovering.
        freshness = verify_fresh_batch(conn, run_id, planned)

        requester = ReliableRequester(
            RequestsTransport(),
            ReliabilityPolicy.from_config(config),
            cache=SqliteCacheStore(conn),
        )
        engine = DiscoveryEngine(
            conn,
            GitHubClient(requester, token=config.secrets.github_token),
            generator,
            per_page=per_page,
        )
        report = engine.run(run_id, tiers=tiers or (1, 2, 3), limit=limit)
        storage.finish_run(conn, run_id)

        stats = run_stats(conn, run_id)

    click.echo(rotation.description)
    click.echo(f"fresh queries         {freshness.novel}/{freshness.planned}")
    for line in stats.summary_lines():
        click.echo(line)
    for query, error in report.failures:
        click.echo(f"failed: {query} -> {error}")


@cli.command("run")
@click.option("--run-id", default=None, help="Run identifier. Defaults to run_N.")
@click.option("--stage", "stages", multiple=True,
              type=click.Choice(["discovery", "evidence", "qualification", "scoring"]),
              help="Run only these stages. Repeatable. Defaults to all.")
@click.option("--tier", "tiers", type=int, multiple=True,
              help="Restrict discovery to these tiers. Repeatable.")
@click.option("--query-limit", type=int, default=None,
              help="Stop discovery after this many queries.")
@click.option("--evidence-limit", type=int, default=None,
              help="Collect evidence for at most this many candidates.")
@click.option("--per-page", type=int, default=30, show_default=True)
@click.pass_context
def run_command(ctx, run_id, stages, tiers, query_limit, evidence_limit, per_page):
    """Run the pipeline: discovery, then evidence collection."""
    from .db import open_database
    from .dedup import plan_rotation
    from .discovery import DiscoveryEngine, QueryGenerator
    from .evidence import EvidenceCollector
    from .scoring import ScoringEngine
    from .run_manager import STAGE_DISCOVERY, STAGE_EVIDENCE, STAGES, RunManager
    from .clients.github_client import GitHubClient
    from .library_universe import load_library_universe
    from .reliability import (
        ReliabilityPolicy, ReliableRequester, RequestsTransport, SqliteCacheStore,
    )
    from . import storage

    # qualification and scoring are proven pure and offline (see their own
    # no-network tests), so a run touching only those stages needs no token.
    # Requiring one there would contradict that guarantee at the CLI boundary
    # and block an offline rerun over already-collected evidence.
    requested_stages = set(stages) if stages else set(STAGES)
    needs_token = bool(requested_stages & {STAGE_DISCOVERY, STAGE_EVIDENCE})

    # Only discovery may bring a run into existence. Every other stage works on
    # evidence an earlier run already produced, so leaving --run-id off there is
    # a mistake rather than a request for a new run. Allocating one silently is
    # what produced a stray, empty run_2 during Run 1 and fragmented the run
    # numbering; the next real run would then have been numbered run_3 and drawn
    # the wrong rotation slices.
    if run_id is None and STAGE_DISCOVERY not in requested_stages:
        raise click.UsageError(
            "--run-id is required for "
            f"{', '.join(sorted(requested_stages))}: these stages continue an "
            "existing run rather than starting one. Pass the run to work on, "
            "for example --run-id run_1. Use `dependency-map runs` to list them."
        )

    config = config_from_context(ctx, require_github_token=needs_token)
    universe = load_library_universe(config.paths.library_universe)

    with open_database(config.paths.database) as conn:
        rotation = plan_rotation(len(storage.list_runs(conn)) + 1)
        generator = QueryGenerator(
            universe, windows=rotation.windows,
            library_offset=rotation.library_offset,
        )
        requester = ReliableRequester(
            RequestsTransport(),
            ReliabilityPolicy.from_config(config),
            cache=SqliteCacheStore(conn),
        )
        client = GitHubClient(requester, token=config.secrets.github_token)

        manager = RunManager(
            conn,
            discovery_engine=DiscoveryEngine(conn, client, generator,
                                             per_page=per_page),
            evidence_collector=EvidenceCollector(conn, client, universe),
            query_generator=generator,
            scoring_engine=ScoringEngine(
                conn, config.weights.dimension_weights, config.weights.gate_caps
            ),
        )
        report = manager.run(
            run_id=run_id,
            stages=stages or STAGES,
            tiers=tiers or (1, 2, 3),
            query_limit=query_limit,
            evidence_limit=evidence_limit,
        )

    for line in report.summary_lines():
        click.echo(line)
    for subject, error in report.failures:
        click.echo(f"failed: {subject} -> {error}")


@cli.command("runs")
@click.pass_context
def list_runs_command(ctx):
    """Show each run's rotation and new-versus-seen counts."""
    from .db import open_database
    from .dedup import run_stats
    from . import storage

    config = config_from_context(ctx, require_github_token=False)

    with open_database(config.paths.database) as conn:
        runs = storage.list_runs(conn)
        if not runs:
            click.echo("no runs recorded")
            return
        for run in runs:
            stats = run_stats(conn, run["run_id"])
            click.echo(f"{run['run_id']}  started {run['started_at']}")
            click.echo(f"  rotation: {run['notes'] or '(none recorded)'}")
            click.echo(
                f"  queries {stats.queries_executed}"
                f"  raw {stats.raw_results}"
                f"  unique {stats.unique_repositories}"
                f"  seen {stats.previously_seen}"
                f"  new {stats.new_candidates}"
            )


@cli.command("report")
@click.option("--run-id", default=None,
              help="Run whose results are being published. Required.")
@click.pass_context
def report_command(ctx, run_id):
    """Generate the ranked CSV and Markdown report from stored evidence.

    Reads only the database. Makes no API calls and changes no stored value.

    --run-id is required and is checked to exist. The report is scoped to that
    run: its queries, the candidates it surfaced, and the ones among those that
    were qualified and scored. Project-wide totals still appear, under a
    heading that says they cover every run.
    """
    from . import storage
    from .db import DatabaseNotInitialized, SchemaVersionMismatch, open_database
    from .report import ReportError, write_report

    if run_id is None:
        raise click.UsageError(
            "--run-id is required: naming the run being published keeps an "
            "official artifact from being generated by reflex. Use "
            "`dependency-map runs` to list them."
        )

    config = config_from_context(ctx, require_github_token=False)

    try:
        with open_database(config.paths.database) as conn:
            if storage.get_run(conn, run_id) is None:
                raise click.UsageError(f"Run {run_id!r} does not exist.")
            summary = write_report(
                conn, config.paths.output_csv, config.paths.output_markdown,
                run_id=run_id,
            )
    except (ReportError, DatabaseNotInitialized, SchemaVersionMismatch) as exc:
        raise click.ClickException(str(exc))

    click.echo(f"csv       {summary.csv_path}")
    click.echo(f"markdown  {summary.markdown_path}")
    for line in summary.summary_lines():
        click.echo(line)


def config_from_context(ctx: click.Context, *, require_github_token: bool = True):
    """Load configuration using the flags parsed by the group.

    Commands call this when they actually need config, so a command that makes
    no API calls can pass require_github_token=False.
    """
    obj = ctx.obj or {}
    return load_config(
        obj.get("config_dir", DEFAULT_CONFIG_DIR),
        overrides=obj.get("overrides"),
        require_github_token=require_github_token,
    )


if __name__ == "__main__":
    cli()
