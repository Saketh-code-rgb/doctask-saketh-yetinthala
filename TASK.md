# How to work in this repository

This describes the working method for building the Dependency Map. It applies
to any contributor, human or AI.

Its sources are the SuperDocs Growth Task brief (which recommends a `TASK.md`,
a `PROGRESS.md`, checkpointing and resumability, fresh verification, and honest
documentation of trade-offs and limitations) and the "Claude operating rule"
section of [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md).

## Work phase by phase

[IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) defines 16 phases. They run
strictly in order. No skipping, no reordering, no starting a later phase early
because its code could technically be written now.

Two phases being independent is not a reason to parallelize them. The plan is
explicit about why: the human-checkpoint model needs a single linear thread to
review against, not several half-finished branches to reconcile.

### Before implementing a phase

1. Inspect the current repository state.
2. Read the design documents relevant to the phase.
3. State which files will be created or modified.
4. Identify any ambiguity or conflict between the documents.
5. Wait for approval where a human checkpoint is defined.

### After implementing a phase

1. Run the relevant tests.
2. Run lint or type checks where applicable.
3. Run the CLI or help command where applicable.
4. Summarize exactly what changed.
5. Record the outcome in [PROGRESS.md](PROGRESS.md).
6. **Stop.** Do not silently continue into the next phase.

## Human checkpoints

Six points require a person to review before work continues:

| After | What needs reviewing |
|---|---|
| Phase 2 | The database schema, especially the `unknown_dimensions` addition, before anything is built on it |
| Phase 8 | Real evidence records from live repositories, before qualification and scoring are built on that data |
| Phase 10 | That `weights.yaml` and the gate thresholds match SCORING_MODEL.md exactly |
| Phase 13 | The actual first-run output, before the deeper Phase 14 pass |
| Before 15 | That Phase 14's review and any rule changes are finished and documented |
| Before 16 | Final sign-off on everything going into the submission |

A checkpoint is a stop, not a notification. The Phase 10 one matters most: a
typo in a weight silently distorts every ranking that follows, and nothing
downstream will catch it.

## Evidence-first development

Nothing is recorded as true because it seems true. Every field in
[CANDIDATE_SCHEMA.md](CANDIDATE_SCHEMA.md) is either raw API metadata or is
backed by a specific `evidence_url` before it can be set.

This extends to the work itself:

- Never invent companies, repositories, scores, evidence, or research findings.
- Never report a phase as complete before its verification has actually run and
  passed. Report what the commands actually printed.
- `qualification_reason` cites the specific field values that drove the
  decision (`category_count=2, code_usage_confirmed=true`), not a summary.
- An unknown dimension scores 0 and is listed in `unknown_dimensions`. It is
  never smoothed over, redistributed, or hidden behind a bare number. The
  report must show the gap explicitly.

If something broke, [PROGRESS.md](PROGRESS.md) says so. An honest record of
what failed is worth more than a clean one that isn't true.

## No live API calls in tests

The test suite never touches a real API. Tests run against mocked, recorded, or
cached responses only.

This is partly about determinism and partly about budget: GitHub code search is
capped at 10 requests per minute even when authenticated, and that budget
belongs to real runs.

During development, live calls happen only when a human explicitly asks for
them — the small manual run at the Phase 8 checkpoint, and the real runs in
Phases 13 and 15.

## Secrets

- `GITHUB_TOKEN` and `LIBRARIES_IO_API_KEY` are read from the environment only.
- They never appear in `config/config.yaml`, `config/weights.yaml`, or any
  other tracked file. [.env.example](.env.example) documents the names with no
  values.
- `.env`, the SQLite database, and `.venv/` are gitignored. The database is
  treated exactly like `.env`: the `api_cache` table holds raw API responses,
  which is a second place something sensitive could land.
- The GitHub token uses minimum scope: public read, no write scopes. This
  system never modifies anything on GitHub.
- Logs never include full response bodies at default verbosity, and token-like
  strings are scrubbed before being written to a log line.
- No environment variable value is ever written into the database or into any
  exported CSV or Markdown report.

## No outreach capability

This system has no send capability of any kind — not messaging, not contact,
not email, not a draft-and-hold queue. This is a hard rule from the task brief,
not a scoping preference. SuperDocs does all outreach itself.

No real person or company is contacted at any point in this project's history.

## Do not silently change the architecture

The design documents are the source of truth. When implementation reveals a
document is wrong or incomplete, that is a finding to raise, not something to
route around in code.

Specifically:

- Scoring weights and gate thresholds live in `weights.yaml` as data precisely
  so a human changes them deliberately. The pipeline never adjusts its own
  scoring logic, and nothing auto-tunes against a proxy metric.
- Qualification always runs before scoring. A high raw score never overrides a
  reject, and a rejected candidate never receives a score row at all.
- Changes to rules or weights get documented in PROGRESS.md with the reasoning,
  never applied silently.

Where two design documents genuinely conflict, stop and get a decision. Record
the resolution rather than picking one quietly. Phase 1 hit exactly this:
TECHNICAL_DESIGN.md section 20 lists a `deps_dev_client.py`, while
IMPLEMENTATION_PLAN.md forbids building a deps.dev client in the MVP. That was
raised and resolved in favour of the plan, and written down.

## Do not build

From IMPLEMENTATION_PLAN.md's own list:

- Any dashboard or interactive UI.
- Any outreach, messaging, or contact capability, in any form, at any point.
- Commit-history pulling inside the Phase 8 evidence collector — it is deferred
  entirely to the targeted top-10-to-15 pass in Phase 14.
- GitHub dependents-page scraping in the MVP.
- Sourcegraph integration in the MVP.
- A deps.dev client in the MVP.
- Async or parallel handling for GitHub code-search calls specifically — the
  10-per-minute cap makes it pointless complexity.

## Checkpointing and resumability

The database is the working state, not an end-of-run export. Each candidate's
progress through each stage is committed to SQLite as it completes, rather than
held in memory and flushed at the end.

Resumability is not a separate feature. Each stage queries for candidates
missing that stage's output, so rerunning `run` picks up exactly where things
stopped. The evidence collector processes candidates with discovery evidence
but no evidence rows; qualification processes candidates with evidence but no
qualification row; scoring processes qualified-but-unscored candidates.

The `api_cache` table means a crashed run does not re-spend rate-limit budget
on responses it already retrieved successfully.

This behaviour is verified by an actual interrupt-and-resume test in Phase 12,
not asserted by design.

## Verification

Every phase has a definition of done in IMPLEMENTATION_PLAN.md. Run its checks
fresh and report the real results.

For Phase 1:

```bash
pip install -e ".[dev]"
python -m dependency_map --help
dependency-map --help
python -c "import dependency_map; print(dependency_map.__version__)"
pytest
git check-ignore -v .env data/dependency_map.db
git status --short
```

If a check fails: diagnose it, fix only issues belonging to the current phase,
rerun the check, and do not advance until it passes.

## PROGRESS.md

[PROGRESS.md](PROGRESS.md) is updated after each completed phase, with one
entry per phase recording what changed, what was verified, what broke, what was
decided, and which checkpoint comes next.

It records what actually happened. Real-world surprises, bugs, and rough edges
go in it, in the same blunt spirit the task brief asks for. It feeds directly
into the final write-up, which is expected to be honest about what was cut and
what broke rather than presenting only what worked.
