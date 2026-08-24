# Progress Log

One entry per completed phase, per [TASK.md](TASK.md). Entries record what
actually happened, including what broke. Nothing here is written before the
work is done and verified.

Phase definitions and definitions of done live in
[IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md).

## Entry template

```
## Phase N - <name>

**Date:**
**What changed:**
**Verification:**
**Problems:**
**Decisions:**
**Next checkpoint:**
```

---

<!-- Entries below, oldest first. -->

## Phase 1 - Repository bootstrap

**Date:** 2026-08-20

**What changed:**

Created the package and repository scaffolding. No pipeline logic of any kind.

- `pyproject.toml` - setuptools src-layout, `requires-python = ">=3.11"`.
  Runtime dependencies: requests, click, pyyaml, python-dotenv. `pytest` under
  the `dev` optional group. Console script `dependency-map` and
  `[tool.pytest.ini_options] testpaths = ["tests"]`.
- `.gitignore` - `.env`, `.venv/`, `data/*.db`, `__pycache__/`, `*.py[cod]`,
  `*.egg-info/`, `build/`, `dist/`, `.pytest_cache/`. `outputs/` deliberately
  left tracked, with a comment explaining why.
- `.env.example` - `GITHUB_TOKEN` and `LIBRARIES_IO_API_KEY`, names only.
- `README.md` - what the project is, setup, the two CLI invocations, repository
  layout, and an index of the eight planning documents.
- `TASK.md` - the working method.
- `PROGRESS.md` - this file.
- `src/dependency_map/__init__.py` - `__version__ = "0.1.0"` only.
- `src/dependency_map/__main__.py` - enables `python -m dependency_map`.
- `src/dependency_map/cli.py` - a bare `click.Group` with `--version`. No
  subcommands.
- `tests/test_cli_smoke.py` - 4 tests covering only the help path.
- `.gitkeep` in `config/`, `data/`, `outputs/`, `tests/fixtures/`, and
  `src/dependency_map/clients/`.
- `.venv/` created locally (gitignored).

No existing file was modified. The eight design documents are untouched.

**Verification:**

All run in `.venv` (Python 3.14.4, pip 26.0.1) on Windows.

| Check | Result |
|---|---|
| `pip install -e ".[dev]"` | Success. Editable wheel built; click 8.4.2, requests 2.34.2, pyyaml 6.0.3, python-dotenv 1.2.3, pytest 9.1.1 |
| `python -m dependency_map --help` | exit 0, help printed |
| `dependency-map --help` | exit 0, help printed |
| `python -c "import dependency_map; print(dependency_map.__version__)"` | `0.1.0`, exit 0 |
| `pytest` | 4 passed in 0.76s, exit 0 |
| `git check-ignore -v .env data/dependency_map.db` | Both matched their rules |
| `outputs/ranked-candidates.csv` not ignored | exit 1, correct |
| `git status --short` | 24 files to be tracked; no `.venv`, `.env`, `__pycache__`, or `.egg-info` |
| Token-pattern scan across stage-able files | Clean |

**Problems:**

The task brief PDF (`SuperDocs-Task-Growth (2).pdf`) could not be read in this
environment. No PDF tooling is installed (no poppler, no pypdf/PyMuPDF), and a
stdlib-only extraction attempt recovered only headings - the body text is
35,783 hex-encoded CID strings across Type0/CIDFontType2 fonts, and resolving
them needs per-font ToUnicode CMaps from the PDF object graph. Merging the four
CMaps naively produced 52 conflicting entries, so the result was unusable.

The headings that did extract ("WHO IT SERVES", "WHAT TO BUILD", "WHAT STRONG
LOOKS LIKE", "DIFFICULTY BAND", "SURFACES IT TOUCHES", "WHERE THE FINISHED WORK
GOES") corroborate the brief's structure but carry no requirements.

Consequence: `TASK.md` was written from the brief requirements as stated by the
project owner (TASK.md, PROGRESS.md, checkpointing/resumability, fresh
verification, documenting trade-offs and limitations) plus
IMPLEMENTATION_PLAN.md's own operating rules, rather than from the brief
directly. Nothing was invented to fill the gap. **This is worth closing before
Phase 16**, which has to satisfy the brief's naming and collaborator
instructions precisely - installing `pypdf` or reading the PDF outside this
environment would settle it.

**Decisions:**

Six ambiguities were raised before implementation and resolved by the project
owner:

1. **Project root** - the repository root is the project root. No nested
   `dependency-map/` directory, despite TECHNICAL_DESIGN.md section 20 showing
   the tree rooted that way. The folder name `doctask-Saketh Yetinthala` is
   intentional and stays.
2. **Git identity** - left exactly as configured. Not modified, and not
   inferred from the folder name.
3. **Virtual environment** - local `.venv`, gitignored. Nothing installed into
   the global interpreter.
4. **`pytest` placement** - dev optional dependency, not runtime, even though
   IMPLEMENTATION_PLAN.md Phase 1 task 2 lists it alongside the four runtime
   libraries. Installing a test runner at runtime would be wrong.
5. **`__main__.py`** - added although TECHNICAL_DESIGN.md section 20's tree
   omits it. Phase 1 task 8 requires `python -m dependency_map --help` to work,
   which is impossible without it. Flagged rather than added silently.
6. **Pre-commit secret scanner** - deferred. TECHNICAL_DESIGN.md section 19
   specifies one but no phase owns it. MVP security for now rests on `.env` and
   the database being gitignored, secrets living only in environment variables,
   and the Phase 12 security test.

One document conflict was found and resolved: TECHNICAL_DESIGN.md section 20
and section 2 both include a `deps_dev_client.py`, while IMPLEMENTATION_PLAN.md
explicitly forbids a deps.dev client in the MVP and section 22 defers it. The
plan wins; the file was not created.

Two open items carried forward, neither blocking:

- Cross-document filename drift. Every design document refers to its siblings
  in lowercase-hyphen form (`technical-design.md`, `scoring-model.md`) while
  the actual files are UPPER_SNAKE. Left alone - renaming would break every
  cross-reference in all eight documents.
- `OBSERVATIONS.md` is absent from IMPLEMENTATION_PLAN.md Phase 16's list of
  documents to include in the submission, though the same section says "every
  working document produced across all eight planning steps". To settle at
  Phase 16.

**Next checkpoint:**

Phase 2 (storage layer) ends at a human checkpoint. The database schema, and
specifically the `unknown_dimensions` addition, must be confirmed before
anything is built on top of it.

Phase 2 has not been started.

## Phase 2 - Storage layer

**Date:** 2026-08-20

**What changed:**

Created the SQLite storage layer. No pipeline logic, no clients, no network
code of any kind.

- `src/dependency_map/db.py` - connection helper, DDL for all 11 tables, and
  the schema-version check. `SCHEMA_VERSION = 1`, `SCORING_DIMENSIONS` (the
  seven names from SCORING_MODEL.md, in document order), `connect()` as a
  context manager that commits on clean exit and rolls back on exception,
  `create_schema()`, `read_schema_version()`, `check_schema_version()`,
  `initialize_database()`, and `open_database()` (connect plus version check).
- `src/dependency_map/storage.py` - 30 CRUD operations covering every table.
  All SQL parameterized. Takes an open connection rather than opening one, so
  callers can group writes into one transaction.
- `tests/conftest.py` - `db_path`, `conn`, `run_id`, `candidate_id` fixtures,
  all built on pytest's `tmp_path`.
- `tests/test_db.py` - 16 tests: schema creation, version check, connection
  behaviour.
- `tests/test_storage.py` - 78 tests: CRUD plus constraint enforcement.

Modified `PROGRESS.md` only. No design document was touched.

**Schema created:**

The 10 tables from TECHNICAL_DESIGN.md section 3, plus `schema_version`:
`runs`, `candidates`, `discovery_evidence`, `dependencies_found`,
`pipeline_evidence` (the 6 fields from CANDIDATE_SCHEMA.md section 5),
`business_evidence` (the 9 fields from section 6), `qualification`, `scores`,
`evidence_trail`, `api_cache`. Four indexes on the foreign-key columns.

`scores.unknown_dimensions` stores a JSON array of the dimension names that
defaulted to 0 for lack of evidence, validated in Python against the seven
known names and written in canonical document order so two candidates with the
same unknowns serialize identically. Nothing normalizes a missing dimension
away.

CANDIDATE_SCHEMA.md's stated rules are enforced as CHECK constraints rather
than left to convention: every enum's allowed values, booleans as 0/1,
dimension scores 0-5, `final_score` 0-100, `gate_cap_applied` in (20, 25, 40),
and three cross-field rules - `company_name_source` null unless `company_name`
is set; `rejection_reason` present if and only if status is `reject`;
`readme_describes_product` true only alongside a non-empty `readme_excerpt`
("Requires a quoted excerpt to be set true", section 6).

`PRAGMA foreign_keys = ON` is set per connection, since SQLite defaults it off,
and child evidence tables cascade on candidate delete.

**Verification:**

All run in `.venv` (Python 3.14.4).

| Check | Result |
|---|---|
| Full suite (`pytest -q`) | **98 passed** in 8.07s |
| Phase 1 tests still pass | 4/4 in `test_cli_smoke.py` |
| Phase 2 tests | 16 in `test_db.py`, 78 in `test_storage.py` |
| Version match | new db stamps 1; `open_database` opens cleanly |
| Version mismatch | stamped 7 vs expected 1 -> `SchemaVersionMismatch`, message names both versions |
| Uninitialized file | -> `DatabaseNotInitialized` |
| CRUD coverage | 30/30 public operations exercised, 0 uncovered |
| Table coverage | 11/11 tables referenced in tests |
| `data/dependency_map.db` | absent; `data/` holds only `.gitkeep` |
| `*.db` anywhere in repo | none found |

Constraint behaviour is asserted, not assumed: foreign keys reject orphan rows,
`readme_describes_product = true` without an excerpt raises, a `keep` carrying
a `rejection_reason` raises, and all six documented rejection reasons are
accepted.

**Problems:**

None. No test failures at any point, and no rework was needed.

**Decisions:**

1. **`storage.py` is a new module.** TECHNICAL_DESIGN.md section 20 lists
   `db.py` as "SQLite connection + schema setup" and gives CRUD no home.
   Splitting connection/DDL from CRUD keeps both readable and matches the
   instruction to keep database functionality isolated in the storage layer.
   Raised before implementing.
2. **`models.py` deferred.** It is in section 20's tree but has no Phase 2
   consumer, and defining ~40 fields of dataclasses before anything reads them
   invites a rewrite. CRUD returns `sqlite3.Row`, which supports both index and
   key access. To revisit when Phase 8 or 9 needs typed records.
3. **`gate_cap_applied` typed `INTEGER NULL`** holding the applied cap value
   (20/25/40). This is the literal reading of the field name, but it records
   *what* ceiling applied rather than *which* of the three section 14 rules
   fired. If the Phase 11 report needs the rule, a companion column will be
   needed. **Flagged for the Phase 10 checkpoint.**
4. **CANDIDATE_SCHEMA.md section 4's computed fields** (`category_count`,
   `generation_signal_count`, `extraction_signal_count`,
   `conversion_signal_count`) are **not stored**. The document labels them
   "computed at the candidate level" and TECHNICAL_DESIGN.md section 3 gives
   them no column. Storing them would let them drift from
   `dependencies_found`. A derivation helper is deferred to the phase that
   consumes them (9 and 10).
5. **No natural-key uniqueness on `discovery_evidence`.** Phase 7's dedup test
   requires the same repository surfacing twice to produce two rows, so a
   unique constraint there would break a later phase. `dependencies_found`
   does get `UNIQUE (candidate_id, library_name, detection_method,
   evidence_url)`, since the same library found the same way at the same URL
   is one fact rather than two.
6. **"Rejects never get a `scores` row" is not enforced in-schema.** SQLite
   would need a trigger, and IMPLEMENTATION_PLAN.md Phase 10 task 7 assigns
   the rule to the scoring engine. Left to Phase 10.
7. **`connect()` takes an explicit path.** Phase 2 task 1 says the path is
   "read from config", but the config system is Phase 3. `DEFAULT_DB_PATH` is
   the fallback until Phase 3 wires config in.

**Next checkpoint:**

**Human checkpoint is ready now.** IMPLEMENTATION_PLAN.md requires confirming
the schema, and specifically the `unknown_dimensions` addition, before anything
is built on top of it.

Not committed - awaiting explicit approval for a Phase 2 commit. Phase 3
(config system) has not been started.

*Later note: Phase 2 was approved and committed as `3c883ae`.*

## Phase 3 - Config system

**Date:** 2026-08-20

**What changed:**

Created the configuration system. No clients, no discovery, no scoring, and
the database layer was not touched.

- `config/config.yaml` - non-secret settings only: the four paths (database,
  library universe, and the two outputs), cache TTL, pacing intervals, and
  retry/backoff parameters.
- `config/weights.yaml` - the seven dimension weights from SCORING_MODEL.md
  section 10 and the three gate caps from section 14, as data rather than
  constants, with the reasoning kept alongside them.
- `src/dependency_map/config.py` - `load_config()`, `load_weights()`,
  `load_secrets()`, the `Config`/`Paths`/`Cache`/`Pacing`/`Retry`/`Weights`/
  `Secrets` value objects, `CliOverrides`, and five error types
  (`ConfigError`, `ConfigFileMissing`, `MissingSecret`, `InvalidWeights`,
  `InvalidConfig`).
- `src/dependency_map/cli.py` - **modified** to add `--config-dir`,
  `--output-csv`, `--output-markdown`, and `--cache-ttl-days`, plus a
  `config_from_context()` helper. Config is deliberately *not* loaded at group
  level, so `--help` still works with no credential present.
- `tests/test_config.py` - 48 tests.

Modified `PROGRESS.md`. No design document, and no Phase 2 file, was touched.

**Verification:**

All run in `.venv` (Python 3.14.4).

| Check | Result |
|---|---|
| Full suite | **146 passed** in 8.77s |
| Phase 1 smoke tests | 4 passed |
| Phase 2 storage tests | 94 passed |
| Phase 3 config tests | 48 passed |
| Real `config/` loads | weights sum to exactly 1.0; caps 20/25/40; ttl 7 |
| Weights sum > 1.0 (0.15 -> 0.25) | `InvalidWeights`, message reports the actual sum (1.10) |
| Weights sum < 1.0 (0.05 -> 0.04) | `InvalidWeights`, reports 0.99 |
| Dimension removed | `InvalidWeights` naming `maintenance_burden` |
| Gate cap removed | `InvalidWeights` naming `code_usage_unconfirmed` |
| `GITHUB_TOKEN` absent | `MissingSecret`, message names the fix |
| Offline load (`require_github_token=False`) | succeeds, token is `None` |
| Secret in `repr(Config)` | absent; renders as `github_token=<set>` |
| Real `config/weights.yaml` after the broken-file run | byte-identical |
| `db.py` / `storage.py` | unmodified |
| All 8 planning documents | unmodified |
| Any `*.db` created | none |

The broken-weights checks ran against copies in a temp directory; the
repository's own `weights.yaml` was never edited.

**Problems:**

One real issue found, in the design rather than the code.

**`gate_caps` in `weights.yaml` collide with a Phase 2 CHECK constraint.**
`scores.gate_cap_applied` carries `CHECK (gate_cap_applied IN (20, 25, 40))`,
with the three values hardcoded in the DDL. The entire point of the caps living
in `weights.yaml` is that a human can retune them after seeing real candidates,
and SCORING_MODEL.md section 17 explicitly expects that ("round numbers chosen
for legibility, not derived from anything"). But retuning a cap to, say, 30
would now make the database reject the write. Config validation accepts any cap
from 0 to 100, so the two layers disagree.

Nothing is broken today, since the shipped values match the constraint. Not
fixed here because Phase 3 must not modify the database layer.

> **DEFERRED - PHASE 10 ARCHITECTURAL DECISION.** Reviewed and intentionally
> deferred at the Phase 3 approval. `scores.gate_cap_applied` accepts only
> 20/25/40 while `weights.yaml` is deliberately configurable, so retuning a cap
> would be accepted by config validation and then rejected by the database.
> **This must be resolved before the scoring engine writes real data.** The
> options are: widen the CHECK to a 0-100 range, drop the CHECK and let the
> scoring engine validate against the loaded config, or keep the CHECK and
> accept that changing a cap requires a schema version bump. Not to be decided
> silently in code - it belongs at the Phase 10 human checkpoint, alongside the
> manual verification that `weights.yaml` matches SCORING_MODEL.md.

**Decisions:**

1. **Weight sum validated with `Decimal`, not floats.** The seven weights do
   not reliably sum to exactly 1.0 in IEEE-754, so an `== 1.0` test on floats
   would be a coin flip. Each YAML number goes through `Decimal(str(value))`,
   which makes "sums to exactly 1.0" literally true rather than
   approximately. The error message reports the actual sum so a typo is
   findable.
2. **`require_github_token` defaults to True, but is a parameter.**
   IMPLEMENTATION_PLAN.md phase 3 task 4 says to refuse to start without the
   token. Applied unconditionally that would also block Phase 11's `report`,
   which reads only a local database, and would break `--help`. The default
   honours the plan; offline callers opt out.
3. **`LIBRARIES_IO_API_KEY` is optional.** Task 4 names only `GITHUB_TOKEN`,
   and SEARCH_STRATEGY.md section 9 still lists obtaining a Libraries.io key as
   unconfirmed. Its absence degrades discovery rather than blocking a run.
4. **`.env` loaded with `override=False`.** This is what gives the required
   precedence: a real environment variable beats the file, so CI or a deployed
   environment wins over whatever is on disk.
5. **Secrets are unprintable by construction.** `Secrets.__repr__` and
   `__str__` render `<set>` or `<unset>`, never the value, so a credential
   cannot reach a log line or traceback by accident. Asserted by test, and by
   a test that plants a token in `config.yaml` and confirms it is ignored.
6. **CLI overrides kept to three flags** - the output paths and cache TTL that
   IMPLEMENTATION_PLAN.md phase 3 task 3 names, plus `--config-dir`. No
   generic override system.
7. **`cli.py` was modified**, which was not in the phase's stated file list,
   because CLI overrides cannot be added without touching it.
8. **Pacing values for the REST API (0.75s) and Libraries.io (1.0s) are my
   numbers.** TECHNICAL_DESIGN.md section 14 gives exact figures only for code
   search (6-7s), retries (3), backoff (2s doubling with jitter), and cache TTL
   (~7 days). It describes the other two only as "looser" and "more generous
   but still rate-limited defensively". 0.75s is roughly 4,800 REST calls/hour,
   under the 5,000 limit. Worth revisiting against real rate-limit headers in
   Phase 13.
9. **Config paths are stored as written**, relative to the working directory,
   rather than resolved against a project root. Runs are expected from the
   repository root. Revisit if that assumption breaks.

**Next checkpoint:**

No human checkpoint is defined at the end of Phase 3. The next one is after
Phase 8, reviewing real evidence records before qualification and scoring get
built on them.

Not committed - awaiting explicit approval. Phase 4 (library universe loader)
has not been started.

*Later note: Phase 3 was approved and committed as `950f40f`.*

## Phase 4 - Library universe loader

**Date:** 2026-08-20

**What changed:**

Transcribed LIBRARY_UNIVERSE.md into machine-readable YAML and built the
loader discovery will consume. No clients, no queries, no network code.

- `data/library-universe.yaml` - **30 entries**, one per table row, in source
  order. Fields: `library_name`, `ecosystems`, `category`, `direction`,
  `package_names`, `manifest_filenames`, and `infrastructure_patterns` where
  applicable.
- `src/dependency_map/library_universe.py` - `load_library_universe()`,
  the `LibraryUniverse` / `LibraryEntry` / `InfrastructurePattern` /
  `DiscoveryTargets` value objects, and `LibraryUniverseError`. Lookups by
  name, category and direction. No network imports, and no dependency on the
  database layer.
- `tests/test_library_universe.py` - 59 tests.

Modified `PROGRESS.md`. LIBRARY_UNIVERSE.md and the other seven planning
documents were not touched, and neither was any Phase 1-3 file.

**Entry counts, verified against the source document:**

| Source table | category | Entries |
|---|---|---:|
| 1. DOCX / Word | `docx` | 8 |
| 2. PDF | `pdf` | 8 |
| 3. HTML / Template -> Document | `template_generation` | 5 |
| 4. Document Conversion | `conversion` | 4 |
| 5. Other Document Processing | `other_processing` | 5 |
| | **Total** | **30** |

Directions: 17 generation, 6 conversion, 5 extraction, 2 mixed.

Three infrastructure entries carry no manifest at all and are found through
Dockerfile or compose patterns instead: Pandoc, LibreOffice headless /
unoconv / JODConverter, and Gotenberg.

**Verification:**

| Check | Result |
|---|---|
| Full suite | **205 passed** in 9.06s |
| Phase 1 smoke | 4 passed |
| Phase 2 storage | 16 + 78 passed |
| Phase 3 config | 48 passed |
| Phase 4 universe | 59 passed |
| Row-by-row audit, Markdown vs YAML | 30 source rows, 30 YAML entries, no additions, no deletions |
| Category totals vs the five source tables | all five match exactly |
| Every row's category matches its source table | yes, all 30 |
| Planning documents | all 8 unmodified |
| Phase 1-3 code | unmodified |
| Any `*.db` created | none |

Several tests parse LIBRARY_UNIVERSE.md directly and compare it to the YAML,
so a library added to one and not the other now fails the suite. That is the
cheapest available guard against the manual-sync drift TECHNICAL_DESIGN.md
section 24 already flags as a known limitation.

**Problems:**

None blocking. One thing worth naming: keeping the Markdown and the YAML in
sync is still a manual step, and the tests only catch a *name* appearing in one
and not the other. A changed category or direction in the Markdown prose would
not be detected automatically, because the prose is not machine-readable.

**Decisions:**

1. **Multi-package rows stay one entry.** Eleven rows name several packages
   (`pypdf / PyPDF2`, `JasperReports / Apache FOP`, `Puppeteer / Playwright`,
   and so on). Splitting them would add libraries the source document does not
   list, so each stays a single entry with a `package_names` list.
2. **Three fields go beyond TECHNICAL_DESIGN.md section 5's five.**
   `ecosystems` is a list rather than a scalar, since rows span up to four
   (`Aspose.Words` covers .NET, Java, Python and C++). `package_names` is
   needed because of decision 1. `infrastructure_patterns` was required by the
   phase's own task 3. Forced by the source data, not invented.
3. **No reasoning field in the YAML.** TECHNICAL_DESIGN.md section 5 is
   explicit that LIBRARY_UNIVERSE.md "stays the human-readable source of truth
   for the reasoning behind each entry; the YAML is what code actually
   consumes."
4. **Two directions are fixed by CANDIDATE_SCHEMA.md section 10's worked
   example** rather than by prose: `pypdf` is extraction, and `WeasyPrint` is
   `template_generation` / `conversion`. Followed exactly.
5. **Four directions are inferred, not stated outright.** These are the only
   judgment calls in the transcription and are the thing most worth a human
   eye:
   - `mammoth / python-mammoth` -> **extraction**. The row says it is "about
     displaying Word content on the web, not generating documents", and the
     closing note defines extraction as consuming or parsing.
   - `Apache PDFBox` -> **generation**. Its description spans creating and
     extracting, but the closing note's "some libraries genuinely do both" list
     names only PyMuPDF and pdf2docx, deliberately excluding PDFBox, and
     SEARCH_STRATEGY.md section 4 frames it as "a common building block for
     homegrown PDF report pipelines".
   - `pikepdf` -> **generation**, from "Creates, repairs, and manipulates
     PDFs".
   - `Puppeteer / Playwright` -> **conversion**, the same HTML-to-PDF shape as
     WeasyPrint, which the schema fixes as conversion.
6. **A test asserts the loader hardcodes no library names**, so the YAML stays
   the only machine-readable list and a second one cannot quietly appear in
   Python.
7. **An entry with neither a manifest nor an infrastructure pattern is
   rejected at load time**, since discovery would have no way to search for it
   and the failure would otherwise be silent.

**Next checkpoint:**

No human checkpoint is defined at the end of Phase 4. The next one is after
Phase 8, reviewing real evidence records before qualification and scoring are
built on them.

Not committed - awaiting explicit approval. Phase 5 (reliability layer and API
clients) has not been started.

*Later note: Phase 4 was approved and committed as `9bc87fd`.*

## Phase 5 - Reliability layer and API clients

**Date:** 2026-08-20

**What changed:**

Built the shared reliability layer and the two MVP API clients. No discovery,
no dedup, no evidence collection, and no deps.dev, Sourcegraph, or
dependents-page scraping.

- `src/dependency_map/reliability.py` - per-resource `Pacer`, `Transport`
  protocol with a `requests`-backed implementation, `ReliableRequester`
  (cache -> pace -> send -> classify -> retry/back off -> cache write),
  `ReliabilityPolicy.from_config()`, rate-limit header parsing, primary and
  secondary limit detection, redaction helpers, and both `SqliteCacheStore`
  (over the phase 2 `api_cache` table) and `MemoryCacheStore`.
- `src/dependency_map/clients/__init__.py`, `github_client.py`,
  `libraries_io_client.py`.
- `tests/test_reliability.py` (61), `tests/test_github_client.py` (38),
  `tests/test_libraries_io_client.py` (25).
- `config/config.yaml` and `config.py` - two new settings (below).
- `tests/test_config.py` - fixture updated for the new settings, plus two
  tests covering them.
- Removed `src/dependency_map/clients/.gitkeep`, now that the package exists.

**API behaviour this was built against**, checked against current
documentation rather than assumed from the planning documents:

| Bucket | Limit | Source |
|---|---|---|
| GitHub core REST | 5,000/hour authenticated | REST rate-limit docs |
| GitHub search (non-code) | 30/minute | Search API docs |
| GitHub code search | **10/minute, separate bucket** | 2023-03-10 changelog |
| Libraries.io | 60/minute per key | Libraries.io API docs |

Also confirmed: code search has required authentication since 2023-04-10;
secondary limits return **403 or 429** with an optional `retry-after`, and the
guidance is to wait at least a minute when that header is absent;
`x-ratelimit-resource` names the bucket a response was charged to; search
returns at most 1,000 results however you paginate. Libraries.io does **not**
reliably return rate-limit headers, so its pacing is the only real protection
there.

**Verification:**

| Check | Result |
|---|---|
| Full suite | **331 passed** in 9.03s |
| Phase 1 smoke / Phase 2 storage | 4 / 94 passed |
| Phase 3 config / Phase 4 universe | 50 / 59 passed |
| Phase 5 reliability / GitHub / Libraries.io | 61 / 38 / 25 passed |
| **Suite with every outbound socket blocked** | **331 passed, 0 connection attempts** |
| `GITHUB_TOKEN` in logs, cache keys, cache bodies | absent in all three |
| `LIBRARIES_IO_API_KEY` in logs, cache keys, cache bodies | absent in all three |
| Forbidden modules (deps.dev, discovery, scoring, ...) | none created |

The no-network check runs the whole suite with `socket.connect`,
`connect_ex` and `create_connection` patched to raise, and reports how many
connections were attempted. Zero. This is stronger than asserting no live calls
by inspection, and the first attempt at it was wrong in an instructive way:
replacing the `socket` class outright broke `ssl`, which subclasses it, and
crashed pytest itself. Blocking the connect methods leaves the stdlib intact.

**Problems:**

Two test failures during development, both real and both fixed.

1. `redact_url` produced `api_key=%3Credacted%3E`, because `urlencode`
   percent-encodes the angle brackets in `<redacted>`. The secret was hidden
   either way, but a redacted URL in a log or cache row was harder to read than
   it should be. The marker is now the URL-safe `REDACTED`.
2. A cache-expiry test passed when it should have failed. The fake wall clock
   started at 1000.0 while `MemoryCacheStore` wrote real ISO timestamps, so
   the computed age came out hugely negative and every entry looked fresh. The
   test harness now keeps the wall clock real by default and fakes it only in
   the three rate-limit-reset tests that need a controlled `now`. Worth noting
   this was a test-harness defect rather than a production one, but it was
   masking a real assertion.

**Decisions:**

1. **Two new config settings, both necessary.**
   `pacing.github_search_min_interval_seconds` (2.0s) exists because
   repository search is a **third** bucket at 30/minute that neither the
   planning documents nor the phase brief names. Without it, repository search
   would inherit either code search's 6.5s (12x too slow) or core's 0.75s (too
   fast for its limit). `retry.backoff_max_seconds` (60.0) bounds the
   exponential growth, which the phase brief required and phase 3 had no
   setting for.
2. **Pacing is keyed by resource, and this is the central design point.**
   Applying code search's 6.5s spacing to core REST would cut it from a
   possible 80 calls a minute to about 9, an **8.7x** slowdown, verified
   against the shipped config. Evidence collection in phase 8 is the
   call-heaviest stage in the system and runs almost entirely on core REST, so
   a single global sleep would have been the most expensive kind of quiet
   mistake.
3. **The cache stores whole raw responses**, not parsed fragments: status,
   body as received, and a whitelist of headers (including `link`, which
   pagination needs). A cache hit rebuilds the typed result with no network
   call, and a test asserts the round trip.
4. **Secrets are handled differently per client, deliberately.** GitHub's token
   goes in an `Authorization` header, so it is structurally incapable of
   reaching a cache key or a URL. Libraries.io passes its key as a **query
   parameter**, which is the real hazard here, so `api_key` is redacted from
   cache keys, stored URLs, log lines, and exception messages. A consequence
   worth naming: because the key is redacted before hashing, rotating it does
   not invalidate the cache, which is the behaviour we want.
5. **Only response headers on a whitelist are cached.** A test plants a
   `Set-Cookie` header and asserts it is not persisted.
6. **A rate-limit wait longer than 300 seconds raises rather than sleeping.**
   Better to stop and report than to block a run indefinitely on a limit that
   will not clear soon.
7. **Clients carry no judgment.** Tests assert the client sources contain no
   qualification vocabulary (`qualification_status`, `final_score`, and so on),
   since that belongs to a pure function over stored evidence, not to anything
   holding an HTTP session.
8. **`SearchPage.capped` surfaces the 1,000-result ceiling** rather than hiding
   it, so a broad query's undercount (a known limitation in
   SEARCH_STRATEGY.md section 9) is visible to phase 6 instead of silent.
9. **Retry classification.** 500/502/503/504, connection errors and timeouts
   retry; 404 and 422 do not, because a missing file is an answer rather than a
   transient failure.

**Next checkpoint:**

No human checkpoint at the end of Phase 5. The next is after Phase 8, reviewing
real evidence records before qualification and scoring are built on them.

Not committed - awaiting explicit approval. Phase 6 (discovery engine) has not
been started.

*Later note: Phase 5 was approved and committed as `df2eaae`.*

## Phase 6A - Controlled real discovery experiment

**Date:** 2026-08-20

**What changed:** nothing in the repository. This was a measurement exercise
against the live GitHub API, run before implementing Phase 6, using the
existing `GitHubClient` and reliability layer with an in-memory cache so
nothing was written to a database. Nine live calls: eight planned queries plus
one diagnostic. Wall time 46.7s.

**Results, measured 2026-08-20, one page of 10 results per query:**

| # | Query | Total | Capped |
|---|---|---:|---|
| 1 | `"python-docx" filename:requirements.txt` | 75,648 | yes |
| 2 | `import docx language:python` | 690,176 | yes |
| 3 | `"docxtemplater" filename:package.json` | 3,256 | yes |
| 4 | `"docxtpl" filename:requirements.txt` | 1,852 | yes |
| 5 | `"reportlab" filename:requirements.txt language:python` | **0** | - |
| 6 | `org.apache.pdfbox filename:pom.xml` | 16,832 | yes |
| 7 | `"gotenberg/gotenberg" filename:docker-compose.yml` | **662** | **no** |
| 8 | `"python-docx" "reportlab" filename:requirements.txt` | 11,552 | yes |
| 9 | diagnostic: `"reportlab" filename:requirements.txt` | 90,240 | yes |

**Findings:**

1. **Query 5 was broken, and had been since the document was written.**
   `filename:requirements.txt` combined with `language:python` returns zero,
   because GitHub classifies a requirements file as text rather than Python.
   The diagnostic without the language qualifier returned 90,240. Had Phase 6
   shipped search-strategy.md section 4 verbatim, ReportLab would have
   contributed no candidates at all, silently.
2. **Six of eight queries hit the 1,000-result ceiling.** Slicing is a
   precondition for any coverage claim, not a later refinement.
3. **Infrastructure queries were by far the most precise.** Gotenberg returned
   662 results, the only uncapped query, with no library-adjacent or tutorial
   noise on the first page and recognisable products throughout.
4. **The bare code-import query is unusable**, at 690,176 results of which
   0.14 percent is reachable, and a first page of personal scripts.
5. **The co-occurrence query underperformed its billing.** It was described as
   the closest single-query proxy for the combined-libraries signal; measured,
   it returned 11,552 results dominated by AI projects and student work.
6. **Duplicate rate was 7.1 percent**, with only two repositories appearing in
   more than one query. Deduplication will be cheap, but the low overlap also
   means the queries are not corroborating each other: coverage is the harder
   problem, not redundancy.
7. **Four noise classes**, one of them unanticipated: library-adjacent tools
   (6 of 10 on the PDFBox page), incidental AI and LLM usage (the largest
   class), personal scripts, and nested or auxiliary manifests (21 percent of
   all results).
8. **Rate limits held.** No 403, 429 or secondary limit across nine calls.
   Pacing dominated: 46.7s for eight queries is the floor at 6.5s spacing, so
   backoff never fired. Per-call latency ranged 2.1s to 10.8s and scaled with
   result-set size. Core REST budget untouched.

**Problems:** the first no-network verification harness was wrong in an
instructive way and is worth recording. Replacing `socket.socket` outright
broke `ssl`, which subclasses it, and crashed pytest, producing a false
"suite needs network" result. Patching the connect methods instead leaves the
stdlib intact. Reported as a harness defect rather than a finding.

**Decisions:** none taken unilaterally. The findings were reported and the
design revision below was approved separately.

## Phase 6 design revision (pre-implementation)

**Date:** 2026-08-20

**What changed:** planning documents and library-universe data only. No
implementation code was touched.

- `SEARCH_STRATEGY.md` - section 4 restructured into three measured tiers with
  a new slicing subsection and a "tested and set aside" record for the import
  query; section 3 and section 9 updated from prediction to dated measurement;
  section 5 gained the four observed noise classes; section 7 records that
  slicing and fresh-batch rotation are one mechanism.
- `CANDIDATE_SCHEMA.md` - section 3 split into a query record (3a) and a
  candidate hit record (3b); section 10's example updated to match.
- `TECHNICAL_DESIGN.md` - section 3 gained `discovery_queries` and a rewritten
  `discovery_evidence`; the `scores` bullet now explains the nullable 0-100
  gate cap; section 7 gained tiered generation, slicing and compose-filename
  handling; section 22 drops bare import search from the MVP.
- `IMPLEMENTATION_PLAN.md` - Phase 6 rewritten into a schema-version-2 block
  followed by the discovery engine, 15 tasks.
- `data/library-universe.yaml` - `discovery_tier` added to all 30 entries.

**Decisions:**

1. **`discovery_queries` is a normalized table, not three extra columns on
   `discovery_evidence`.** The deciding argument was empirical: query 5
   returned zero candidates, so under a candidate-only model the single most
   valuable finding of the experiment would have left no trace in the database.
   A query execution is an entity with its own lifetime.
2. **Four fields dropped from `discovery_evidence`** (`run_id`,
   `discovery_source`, `discovery_query`, `discovered_at`). All are properties
   of the query, reachable through `query_id`. Keeping copies per hit would
   duplicate them across every result of a query.
3. **Gate-cap constraint fixed now rather than at Phase 10.** The conflict was
   found in Phase 3 and deferred; since schema version 2 was being cut anyway
   and no database file exists, fixing it here costs nothing and avoids a
   second bump. The database no longer hardcodes 20/25/40, which was making
   `weights.yaml`'s configurability a fiction. Scoring semantics stay in the
   scoring engine.
4. **`discovery_tier` is separate from `library_category`.** Two entries force
   the distinction: docxtemplater is category `docx` but tier 2 because it
   fills templates from data, and Puppeteer/Playwright is category
   `template_generation` but tier 3 because both packages are overwhelmingly
   browser-test tooling. Tier is a claim about query precision, category is a
   claim about what the library does.
5. **Tier 2 has five members, three of them unmeasured.** docxtemplater and
   docxtpl were measured in the experiment. Carbone.io, JasperReports/Apache
   FOP and docx-mailmerge/docxedit were placed by reasoning from their
   descriptions in LIBRARY_UNIVERSE.md, and are labelled as such in
   search-strategy.md rather than presented as findings.
6. **The import query is documented, not deleted.** The measurement is the
   reason for the decision, and a future reader considering reintroducing
   code-import search should see 690,176 rather than rediscover it.

**Problems:**

**The test suite is now red, expectedly.** Phase 4's library universe loader
validates entries against an allowlist and rejects unknown fields, a
deliberate choice at the time to stop a typo from silently doing nothing.
Adding `discovery_tier` therefore fails the loader. `library_universe.py` was
outside the permitted edit scope for this revision, so the fix rides with
Phase 6 implementation, exactly as the `db.py`, `storage.py` and Phase 2 test
updates do. The fix is one line: add `discovery_tier` to `_ALLOWED_FIELDS`,
plus validation that it is 1, 2 or 3.

This is data landing ahead of the code that reads it, which is a deliberate
consequence of splitting the design revision from the implementation, not an
oversight.

**Next checkpoint:**

No human checkpoint at the end of Phase 6. The next is after Phase 8, reviewing
real evidence records before qualification and scoring are built on them.

Not committed. Phase 6 implementation has not been started.

## Phase 6 - Discovery engine (implementation)

**Date:** 2026-08-20

### Block A - schema version 2

- `db.py` - `SCHEMA_VERSION` 1 -> 2; added `discovery_queries`; rewrote
  `discovery_evidence` down to `id`, `query_id`, `candidate_id`,
  `discovery_result_rank` with `UNIQUE(query_id, candidate_id)`; replaced the
  hardcoded `gate_cap_applied IN (20, 25, 40)` with a nullable 0-100 range;
  four indexes on the discovery foreign keys.
- `storage.py` - `make_query_id`, `create_discovery_query`,
  `update_query_results`, `get_discovery_query`, `list_queries_for_run`,
  `count_queries_for_run`, rewritten `insert_discovery_evidence`,
  `list_discovery_evidence_for_query`, `all_discovered_candidate_ids`.
  `list_discovery_evidence_for_candidate` and `list_candidate_ids_for_run` now
  join through `discovery_queries`.
- `library_universe.py` - `discovery_tier` accepted, required and validated as
  1, 2 or 3; `by_tier()` and `tier_counts()` added. The existing allowlist
  validation was extended, not relaxed.
- Phase 2 tests updated: the discovery section rewritten around the query
  table, and the gate-cap test that asserted 33 was rejected replaced with one
  asserting any 0-100 cap is accepted, since version 2 deliberately allows a
  retuned cap.

Block A checkpoint: **368 passed**, `SCHEMA_VERSION = 2` stamped correctly, 12
tables, `discovery_evidence` down to 4 columns, no hardcoded caps anywhere in
the DDL.

### Block B - discovery engine

- `src/dependency_map/discovery.py` - `normalize_repo_url`,
  `make_candidate_id`, `validate_query`, `quarterly_windows`, `QueryGenerator`
  (tiered, sliced), `DiscoveryEngine`, `DiscoveryReport`.
- `cli.py` - a `discover` command that runs the stage and prints a summary.
- `tests/test_discovery.py` - 54 tests.

**Verification:**

| Check | Result |
|---|---|
| Full suite | **422 passed** in 13.46s |
| Phase 1-5 files | 4 / 18 / 103 / 50 / 69 / 61 / 38 / 25 passed |
| Phase 6 discovery | 54 passed |
| Suite with every socket blocked | **422 passed, 0 connection attempts** |
| `SCHEMA_VERSION` | 2, stamped and read back |
| Any `*.db` created by the suite | none |
| CLI `--help` without a token | works |
| Phase 7+ modules | none created |

**Problems:**

Two test failures during development, both mine rather than the code's.

1. **The Phase 4 "no hardcoded library names" guard fired on a comment.** I
   named docxtemplater in a comment explaining why `discovery_tier` and
   `library_category` are separate concepts, and the guard greps raw source.
   The guard's intent is that no library list influences behaviour, and a
   comment is not a list, so the test now strips docstrings and comments before
   checking. That is a sharpening rather than a weakening: the same name in a
   tuple would still fail. Deleting the explanation instead would have removed
   the clearest statement of the design's most confusing point.
2. **A ReportLab assertion was too strict.** It required every generated
   ReportLab query to name `requirements.txt`, but the generator correctly
   produces one per manifest, so `pyproject.toml` also appears. The test now
   asserts both are present and neither carries `language:python`. Worth
   noting because that second query is exactly what covers the
   non-`requirements.txt` pinning the set-aside import query was meant to
   catch.

**Decisions:**

1. **`UNIQUE(query_id, candidate_id)` on `discovery_evidence`.** One query
   matching the same repository at two file paths is one hit, not two. The
   Phase 6A experiment saw this (`2296399932/our-docx` twice in one query).
   This is what makes `returned_count` meaningful as a separate number: the
   gap between raw results and recorded hits is real dedup signal.
2. **A failed query stores `total_count = NULL`, a zero-result query stores
   `0`.** The distinction matters and comes for free: null means "we do not
   know", zero means "we asked and there were none". Since
   `discovery_queries` has no error column, this is how a failure stays
   visible rather than looking like an empty result.
3. **Rate limiting is treated as systemic and stops the run**; a single API
   error is per-query and the run continues. Five consecutive failures also
   stop it, on the grounds that it has stopped being incidental.
4. **`filename:*.csproj` is emitted as `extension:csproj`.** `filename:` does
   not handle a glob; the API would accept the malformed version and quietly
   match nothing, which is the same failure mode as the ReportLab bug.
5. **`validate_query` refuses the `filename:`-plus-`language:` combination at
   generation time**, for any of the nine manifest filenames GitHub does not
   classify under a language, rather than only the one that was measured. The
   original bug was one instance of a general shape.
6. **Tier 1 and tier 2 are unsliced, tier 3 always sliced.** Tier 1 was
   measured at 662 results, comfortably enumerable. A `QueryGenerator`
   constructed with no windows raises rather than silently emitting unsliced
   tier-3 queries.
7. **`normalize_repo_url` and `make_candidate_id` live in `discovery.py` for
   now.** Phase 7 owns deduplication and will create `dedup.py`; these move
   there then. Discovery needs only enough to avoid creating a duplicate
   candidate row.
8. **The co-occurrence query carries `library_name = NULL`.** It spans two
   libraries and attributing it to either would be a fiction.

**Nothing changed from the approved plan.** No design contradiction was found
during implementation.

**Checkpoint examples**, from a real database with mocked responses shaped like
the Phase 6A measurements:

| | query | total | returned | capped | window |
|---|---|---:|---:|---|---|
| zero-result | `"reportlab" ... language:python` | 0 | 0 | false | null |
| capped | `"python-docx" filename:requirements.txt pushed:...` | 75,648 | 2 | **true** | set |
| uncapped | `"gotenberg/gotenberg" filename:docker-compose.yml` | 662 | 2 | false | null |

`UKGovernmentBEIS/inspect_evals` was surfaced by two different queries and
produced **one** candidate row with **two** `discovery_evidence` rows: overlap
preserved, duplication avoided.

**Next checkpoint:**

No human checkpoint at the end of Phase 6. The next is after Phase 8, reviewing
real evidence records before qualification and scoring are built on them.

Not committed. Phase 7 (deduplication and fresh-batch tracking) has not been
started.

*Later note: Phase 6 was approved and committed as `1ef7718`.*

## Phase 7 - Deduplication and fresh-batch tracking

**Date:** 2026-08-20

**What changed:**

- `src/dependency_map/dedup.py` - new. `normalize_repo_url` and
  `make_candidate_id` moved here from `discovery.py`; `quarterly_windows`
  moved here too, since slicing is a rotation concern. Added `RotationPlan`,
  `plan_rotation`, `verify_fresh_batch`, `FreshBatchCheck`, `FreshBatchError`,
  `classify_candidate`, `RunStats` and `run_stats`.
- `src/dependency_map/discovery.py` - imports the identity and slicing helpers
  rather than defining them, and re-exports them so existing callers keep
  working. `QueryGenerator` gained `library_offset` for within-tier rotation.
- `src/dependency_map/storage.py` - four derived read helpers:
  `candidate_ids_discovered_before_run`, `query_signatures_for_run`,
  `query_signatures_before_run`, `run_query_totals`.
- `src/dependency_map/cli.py` - `discover` now plans a rotation, verifies
  freshness before spending any API budget, and reports new-versus-seen. Added
  a `runs` command.
- `tests/test_dedup.py` - 62 tests.
- `tests/test_discovery.py` - one stale assertion updated (it asserted
  `dedup.py` did not exist, which was true until this phase).

**No schema change was needed.** `db.py` is untouched. The rotation is recorded
in `runs.notes`, which already existed as free text, and the slice each query
used is already in `discovery_queries.search_window`. Every run-level count is
derived on read rather than stored, so no counter can drift from what was
actually persisted.

**The fresh-batch algorithm:**

`plan_rotation(run_index)` is a pure function of the run's index and moves two
axes together.

The **date window** walks backwards a whole block per run: run 1 covers the
four most recent quarters, run 2 the four before those, and so on. Runs
therefore partition time rather than overlapping, which is what guarantees the
query strings differ. This is the axis that does the real work.

The **library order** rotates within each tier by the run index. Tier order is
never rotated, because tiers are ordered by measured precision and shuffling
them would trade a real gain for cosmetic variety. Rotating inside a tier means
a run cut short by budget does not always spend it on the same libraries.

Before a run spends any API budget, `verify_fresh_batch` compares the planned
(query, slice) pairs against every pair an earlier run executed and raises if
the overlap is total. Partial overlap is fine and expected; a complete overlap
would mean GitHub returns the same best-match hits again and the run records
nothing new, which is the exact failure SEARCH_STRATEGY.md section 7 exists to
prevent.

The whole rotation is legible from the database: `runs.notes` carries a
one-line description naming the window bounds and the library offset, and
`discovery_queries.search_window` records what each query actually used. Nobody
has to rerun anything to see how run 2 differed from run 1.

**Verification:**

| Check | Result |
|---|---|
| Full suite | **484 passed** in 17.45s |
| Phase 7 dedup tests | **62 passed** |
| Suite with every socket blocked | **484 passed, 0 connection attempts** |
| Schema (`db.py`) | unchanged |
| Planning documents and library universe | unchanged |
| Phase 8+ modules | none created |

Checkpoint scenario, run against a real SQLite database: run 1 finds A, B, C;
run 2 finds B, C, D, E with D surfaced by three separate queries.

| | run 1 | run 2 |
|---|---:|---:|
| raw results | 3 | 6 |
| unique repositories | 3 | 4 |
| previously seen | 0 | **2** |
| new candidates | **3** | **2** |

D produced one candidate row, three `discovery_evidence` rows, and counted once
as new. Run 1's windows and run 2's windows were disjoint.

**Problems:**

Two test failures during development, both stale assertions rather than
defects.

1. A rotation-description test asserted the string contained "2026". With an
   anchor of 2026-06-30 and four windows per run, run 2's block legitimately
   sits in 2025, so the assertion was wrong about the code rather than the
   other way round. It now asserts the description contains the actual window
   bounds, which is what makes it useful in `runs.notes`.
2. Phase 6's `test_discovery_creates_no_qualification_or_scoring` asserted
   `dedup.py` did not exist. True when written, and untrue as of this phase.
   Removed from that list, with the other five later-phase modules still
   asserted absent.

**Decisions:**

1. **Normalization is deliberately conservative.** It handles scheme and host
   case, a trailing slash, a `.git` suffix, a `www.` prefix, and query strings
   or fragments. It does **not** fold hyphens against underscores or attempt
   any cleverer equivalence, because a false merge would silently combine two
   companies into one candidate. Carrying a duplicate is a far cheaper mistake
   than losing a distinct prospect, so the tests assert both directions:
   equivalent forms collapse, and six genuinely different URLs stay separate.
2. **"Earlier run" is ordered by `runs.started_at`, not by `run_id`.** Run
   naming is a convention, and a test asserts that a run named `run_alpha`
   which started after `run_zebra` is still treated as the later one.
3. **Run-level counts are derived, never stored.** `raw_results`,
   `unique_repositories`, `previously_seen` and `new_candidates` are four
   different numbers and are reported separately: raw results exceed unique
   repositories because several hits collapse onto one repo, and unique
   repositories exceed new candidates because a later run resurfaces earlier
   ones. Collapsing them into a single "found" number would hide both effects.
4. **A failed query is still told apart from an empty one** in the run stats,
   via `total_count IS NULL` versus `= 0`, carried over from Phase 6.
5. **`quarterly_windows` moved to `dedup.py`.** Slicing is the rotation
   mechanism, so it belongs with rotation; `discovery.py` imports it. This also
   avoids a circular import, since rotation planning needs windows and query
   generation needs rotation.
6. **Rotation is deterministic and reproducible.** Nothing is randomised to
   manufacture a difference. A test asserts ten calls with the same arguments
   produce identical plans, and another walks five runs asserting no window is
   ever reused.

**Next checkpoint:**

**Human checkpoint at the end of Phase 8.** Real evidence records must be
reviewed, pulled from a handful of live repositories, before qualification and
scoring are built on that data.

Not committed. Phase 8 (evidence collector and run manager) has not been
started.

*Later note: Phase 7 was approved and committed as `25aac2c`.*

## Phase 8 - Evidence collector and run manager

**Date:** 2026-08-20

### Block A - evidence collector

- `src/dependency_map/evidence.py` - `EvidenceCollector`, `EvidenceOutcome`,
  `collect_for_candidates`, and the evidence-derivation helpers
  (`detect_product_description`, `detect_company_name`,
  `detect_industry_category`, `is_source_file`, `is_production_path`).
- `src/dependency_map/clients/github_client.py` - added `list_directory` and
  `DirectoryEntry`. One listing answers "which manifest is here, is there a
  templates directory, what does the root look like" from the core REST budget
  of 5,000 an hour. Asking those questions through code search would spend the
  10-per-minute bucket instead, for a worse answer.
- `src/dependency_map/storage.py` - `candidates_needing_evidence` and
  `libraries_that_surfaced_candidate`, both derived reads.
- `tests/test_evidence.py` - 78 tests.

### Block B - run manager

- `src/dependency_map/run_manager.py` - `RunManager`, `RunReport`, stage
  constants. Orchestration only: it decides what runs and over which
  candidates, and holds no discovery, evidence, qualification or scoring logic
  of its own.
- `src/dependency_map/cli.py` - a `run` command with `--stage`, `--tier`,
  `--query-limit` and `--evidence-limit`.
- `tests/test_run_manager.py` - 30 tests.

Resumability is not implemented here as a feature. Each stage asks the database
what is missing, so a rerun simply has less to do. There is no progress record
that can disagree with what was committed.

**Verification:**

| Check | Result |
|---|---|
| Full suite | **592 passed** |
| Block A evidence tests | 78 passed |
| Block B run manager tests | 30 passed |
| Suite with every socket blocked | 592 passed, 0 connection attempts |
| Later-phase modules | `qualification.py`, `scoring.py`, `report.py` all absent |

**Problems: two real bugs, both found only by the live run.**

The unit tests passed against both of them. That is the finding worth
recording, more than the bugs themselves: fixtures written by the same person
who wrote the code encode the same assumptions, and only real repositories
disagreed.

**1. `code_import` was being claimed for files that are not code.** GitHub code
search matches text in *any* file, so a repository-scoped search for
`python-docx` returns `base-requirements.txt`, `.github/dependabot.yml`,
`.env.example` and `README.md` alongside any real import. All of those were
recorded as call sites. The consequence was not cosmetic: `code_usage_confirmed`
became true for manifest-only candidates, and that field is exactly what
SCORING_MODEL.md section 14's first gate cap tests. Every one of those
candidates would have escaped the cap at 20 and scored as though its usage were
confirmed. Fixed by requiring a hit to carry a source-file extension before it
counts as a call site.

**2. `website_url` was invented from README prose.** The collector took the
first non-GitHub URL it found. On `thoqbk/traprange` that attributed the
project's website to `dzone.com`, a blog that had merely written about it. The
first link in a README is as often a badge target or an article as the
project's own site. `website_url` now comes only from the repository's declared
homepage, which the owner set deliberately; recovering one from prose is left
to a human, alongside `company_name`.

Fifteen regression tests were added covering the exact paths the live run
mis-classified.

**Evidence-quality observations from the live run** (5 real repositories,
29.3s, no qualification or scoring performed):

- **Manifest discovery only looks at root-level standard filenames.**
  `sambanova/ai-starter-kit` keeps its dependencies in `base-requirements.txt`
  and `utils/parsing/unstructured-api/requirements/base.txt`, so nothing was
  found and the candidate recorded **zero** dependency rows despite discovery
  having surfaced it. The note says so honestly rather than implying absence of
  usage, but this is a genuine coverage gap. **Not fixed, deliberately: it
  changes what this checkpoint is reviewing.** The cheap fix is to match
  root-level files ending in `requirements.txt` as well as the exact name.
- **`industry_category` from keywords is weak and should be treated as
  low-confidence.** `PurpleOps`, a security assessment tool, was filed under
  `legal_contracts`; `traprange`, a PDF table-extraction library, and
  `ai-starter-kit` both landed on `finance_investment` on the strength of a
  single word. The tie-to-unknown rule helps but does not rescue a
  single-keyword match.
- **`readme_describes_product` is conservative and misses real products.** It
  returned false for PurpleOps, which is a real product. It also produced a
  weak positive for `bigcapital`, quoting a Docker deployment sentence rather
  than a product description. The phrase list is doing crude work.
- **`company_name` was null for all five**, correctly. None of the five states
  a company in the repository, and the collector declined to infer one from the
  org slug or the domain. This is the intended behaviour and confirms
  TECHNICAL_DESIGN.md section 17's expectation that resolving identity stays a
  human step.
- **The tier ordering held up.** The tier-1 candidate (`bigcapital`, Gotenberg)
  produced the richest evidence: a deployed conversion service in
  `docker-compose.yml` plus four TypeScript call sites. The tier-3 noisy
  candidate produced almost nothing. That is the measured precision ordering
  behaving as SEARCH_STRATEGY.md section 4 predicts.

**Decisions:**

1. **`list_directory` was added to GitHubClient**, a fifth operation beyond the
   four Phase 5 approved. It replaces several code searches per candidate with
   one cheap core-REST call.
2. **A stage counts only when observed.** Only three stages are detectable from
   what this collector fetches (template population, document generation,
   format conversion). A repository almost certainly retrieves source data
   before generating a document, but nothing fetched here sees that, so it is
   not counted.
3. **`document_functionality_in_production_code` considers call sites only.** A
   `requirements.txt` at repository root is a production path in the trivial
   sense while proving nothing about where code runs.
4. **Industry keywords match on word boundaries with optional plurals, over
   whitespace-collapsed text.** Substring matching read "clause" inside a
   product named ClauseForge and filed a lease product under legal contracts;
   READMEs wrap at 80 columns, so "property management" is routinely split
   across a newline.
5. **A tier-1-only rerun is refused by the fresh-batch guard**, correctly.
   Tier-1 queries carry no slice because the one measured tier-1 query is fully
   enumerable, which makes them byte-identical between runs. Rotating tier 1
   would need a page-offset axis that discovery does not have yet. Recorded as
   a limitation, with a test asserting the refusal.

**Next checkpoint:**

**Human checkpoint is open now.** The real evidence records for five
repositories are ready for review before `qualification.py` and `scoring.py`
are built on this data.

Not committed. Phase 9 (qualification engine) has not been started.

## Phase 8 correction pass - manifest coverage

**Date:** 2026-08-20

**Why this was necessary.** The live evidence review found
`sambanova/ai-starter-kit` recording **zero** dependency rows despite discovery
having surfaced it for python-docx. Its dependencies live in
`base-requirements.txt` and
`utils/parsing/unstructured-api/requirements/base.txt`, and the collector only
recognised exact root-level manifest filenames.

The record was honest about the gap in its notes, but a blank dependency list
is not read as "we did not look there" by anything downstream. Qualification
reads `dependencies_found` and `code_usage_confirmed`, and an empty list is
indistinguishable from a repository that genuinely does not use the library.
Building qualification on that would have produced confident rejections
resting on a tooling limitation. This is a false negative, which is the
failure mode CANDIDATE_SCHEMA.md's evidence-first rule exists to prevent, and
it had to be fixed before Phase 9 rather than after.

**What changed:**

- `manifest_kind(path)` recognises a manifest by convention rather than exact
  name: `requirements.txt`, `base-requirements.txt`, `requirements-dev.txt`,
  `requirements_test.txt`, any `.txt` directly inside a `requirements/`
  directory, plus `pyproject.toml`, `package.json`, `package-lock.json`,
  `pom.xml`, `build.gradle`, `build.gradle.kts`, `packages.config` and
  `*.csproj` at any depth. Deliberately **not** "any `.txt` is a manifest":
  `README.txt`, `LICENSE.txt` and `docs/notes.txt` are all rejected.
- `_fetch_manifests` looks at the root, then takes **at most four** extra
  listings into directories that exist there and are plausibly where manifests
  live (`requirements/`, `docker/`, `src/`, `packages/`, and similar). Bounded
  by construction, not by convention.
- **Code-search hits are now routed by file type.** This is what actually fixed
  sambanova, and it costs nothing: the search results already named those deep
  manifest paths, which is how the gap was spotted in the first place. A hit in
  a source file becomes `code_import`; a hit in a manifest becomes
  `manifest_declaration`; anything else, a README, a lockfile that is not a
  manifest, a CI config, is dropped. No extra API calls, and no tree walk.

**Result of the critical re-check** (`sambanova/ai-starter-kit`, live):

| | before | after |
|---|---:|---:|
| dependency rows | **0** | **4** |
| all `manifest_declaration` | - | yes |
| `code_usage_confirmed` | false | **still false** |

The four are `base-requirements.txt`, `data_extraction/requirements.txt`,
`utils/parsing/unstructured-api/requirements/base.txt` and
`.../requirements/test.txt`. Crucially `code_usage_confirmed` stayed false:
the manifest evidence is now visible, and the absence of a call site is still
recorded as an absence. That distinction is the entire point of the change.

`alanagoyal/docbase` also gained a row (`package-lock.json` alongside
`package.json`). The three candidates with real code evidence were unchanged at
5, 2 and 4 rows, and a check across all five confirms **no `code_import` row
points at a non-source file**.

**Verification:**

| Check | Result |
|---|---|
| Full suite | **621 passed** (was 592) |
| Evidence tests | 107 passed (was 78) |
| All other Phase 1-8 files | unchanged counts |
| Sockets blocked | 621 passed, 0 connection attempts |
| Live re-check, sambanova | 0 -> 4 dependency rows |
| Non-source paths recorded as `code_import` | none, across all five |

**Preserved deliberately:**

- `manifest_declaration` still never implies use. Every new row from this
  change is a declaration, and `code_usage_confirmed` moved for nobody.
- `code_import` stays restricted to source extensions.
- `website_url` stays homepage-only.
- `company_name` stays conservative and null for all five.
- `industry_category` unchanged; still weak, still to be treated as
  low-confidence, and no classifier was introduced.

**Approved guidance for Phase 9**, recorded here at the Phase 8 sign-off so it
carries across the phase boundary rather than being rediscovered:

- `industry_category` is **evidence only, never a standalone qualification
  gate**.
- Ambiguous industry evidence stays `unknown` and low-confidence.
- `industry_category` **alone must never determine keep or reject.**

This follows directly from the live run, where three of five candidates were
filed under a wrong or dubious category on the strength of a single keyword. A
field that unreliable can contribute to a decision but must not carry one.

Phase 9 (qualification engine) has not been started.

*Later note: Phase 8 was approved and committed as `3521acb`.*

## Phase 9 - Qualification engine

**Date:** 2026-08-20

**What changed:**

- `src/dependency_map/qualification.py` - `CandidateEvidence` (loads and
  derives everything a decision reads, including CANDIDATE_SCHEMA.md section
  4's computed counts), five rejection predicates, `meets_keep_criteria`,
  `assess_confidence`, `qualify`, `QualificationEngine`, `QualificationReport`.
- `src/dependency_map/storage.py` - `candidates_needing_qualification`.
- `src/dependency_map/run_manager.py` - `qualification` stage.
- `src/dependency_map/cli.py` - `--stage qualification`.
- `tests/test_qualification.py` - 52 tests.
- Four stale later-phase assertions updated across existing test files.

**Verification:**

| Check | Result |
|---|---|
| Full suite | **673 passed** (was 621) |
| Qualification tests | 52 passed |
| Sockets blocked | 673 passed, 0 connection attempts |
| Determinism, real dataset | rerun produced identical rows |
| `scoring.py` / `report.py` | absent |

**Problems: one serious bug in the engine, caught by its own test suite.**

A candidate whose evidence was never collected was **rejected as
`tutorial_or_demo`**. Every negative field on such a record reads as false, so
`readme_describes_product`, `application_code_exists` and
`document_functionality_in_production_code` were all false, and the predicate
fired on three bare falses. That is precisely the "absence of evidence becomes
confirmed absence" failure the module was written to prevent, reproduced inside
the module meant to prevent it.

Fixed with a guard ahead of every rejection rule: if the pipeline or business
evidence row is missing, the answer is `investigate` at low confidence and no
rejection is reachable. Guarding centrally rather than per-predicate matters,
since any future rule would inherit the same flaw. Three regression tests cover
it, including the exact shape that exposed it, a repository named
`someone/python-tutorial` with no evidence rows.

Two further test failures were my fixtures being wrong rather than the code:
the traprange fixture used the default `docx` category for its manifest row
when the real candidate is single-category `pdf`, and a confidence test assumed
one supporting signal where the fixture produced two.

**Decisions:**

1. **No rejection is possible without evidence rows.** See above. This is the
   single most important rule in the module.
2. **Every rejection requires a positive combination of observations**, never a
   bare negative. `tutorial_or_demo` needs no product framing *and* no
   application code *and* no production usage together, which is the
   docutils-sandbox shape SCORING_MODEL.md section 15 works through.
3. **Repository-name tokens are supporting evidence only.** A name containing
   "demo" or "examples" strengthens a case that other fields already make, and
   can never carry one alone. Matched on word boundaries, so "example" does not
   fire on "exampleforge" - the same substring lesson as the phase 8
   ClauseForge bug.
4. **Forks and archived repositories are not auto-rejected.** A fork that grew
   into an independent product, or an archived repository that still describes
   a product with confirmed usage, goes to investigate. Archive status and fork
   status are facts, not verdicts.
5. **`personal_project_no_customers` requires the repository to name itself
   one.** Star count, contributor count and user-versus-organisation ownership
   are all explicitly excluded, per the phase brief.
6. **`single_incidental_use` never fires when the README describes a
   product.** A stated product with thin document evidence is the investigate
   case, which is what keeps `alanagoyal/docbase` out of the reject pile.
7. **`industry_category` is never consulted by any rule.** A test runs the same
   evidence through four different industry values and asserts the status is
   identical, which enforces the approved guidance mechanically rather than by
   convention.
8. **Confidence never changes status.** A low-confidence keep stays a keep,
   flagged as worth checking rather than quietly demoted.

**Qualification over the real phase 8 evidence** (5 candidates, no ranking, no
scoring):

| | count |
|---|---:|
| keep | **0** |
| investigate | **3** |
| reject | **2** |
| `single_incidental_use` | 1 |
| `tutorial_or_demo` | 1 |
| confidence high / medium / low | 0 / 4 / 1 |

Zero keeps is the honest outcome for this sample rather than a failure. Every
one of the three investigates fails the keep gate on a single field, and in two
cases that field is a known weakness in the *collector* rather than a fact
about the repository:

- **`bigcapitalhq/bigcapital`** fails only on `application_code_exists=false`.
  It has a deployed Gotenberg service, five confirmed dependencies and 3,846
  stars. The field is false because the collector's application-directory list
  omits `packages`, and this is a monorepo rooted at `packages/`. **This is an
  evidence-detection gap, not a property of the candidate.**
- **`CyberCX-STA/PurpleOps`** fails only on `readme_describes_product=false`,
  which is the conservative phrase list already recorded as weak in phase 8.
- **`alanagoyal/docbase`** fails on
  `document_functionality_in_production_code=false`, which is genuine: its
  docxtemplater evidence is manifest-only.

Both rejections look right. `sambanova/ai-starter-kit` is a starter kit with no
call site and no product framing; `thoqbk/traprange` is a PDF table-extraction
tool with single-category isolated usage and no customer-facing framing.

**Not fixed, deliberately:** the `packages` omission is phase 8 collector code,
and changing it now would alter the evidence this checkpoint is being reviewed
against. It is a one-word addition to `APPLICATION_DIRECTORIES` in
`evidence.py`, and it would likely move bigcapital from investigate to keep.
Worth a decision before the first full run.

## Phase 9 correction - evidence collector application directories

**Date:** 2026-08-20

**The defect.** `_application_code_exists` matched a fixed list of
application-directory names at the repository root. `packages` was not on it,
so a monorepo whose application lives under `packages/` recorded
`application_code_exists = false`.

**Why it was a false negative rather than a finding.** The field is not "we
looked and found no application"; it is "we looked in a fixed set of places and
none matched". `bigcapitalhq/bigcapital` has a deployed Gotenberg service, five
confirmed dependencies across TypeScript call sites, 3,846 stars and a stated
product, and its application is entirely real. It sits under
`packages/server`, `packages/webapp` and siblings, which the collector never
looked into. Qualification then read the false as a fact and withheld a keep on
that single field. The rule was right; the input was wrong.

**The correction.** `packages` could not simply join
`APPLICATION_DIRECTORIES`, because a `packages/` holding only a docs site is
not an application and counting it would trade a false negative for a false
positive. So a monorepo container is treated as a *question* rather than an
answer:

- `WORKSPACE_DIRECTORIES` (`packages`, `modules`, `workspaces`, `libs`,
  `components`, `projects`) count only when the directory is listed and holds
  at least one member that is not documentation, tests, examples or assets.
- `_inspect_workspaces` fetches that listing, at most once per candidate, and
  **only when the answer hinges on it**: if the root already shows a plain
  application directory, no call is made.
- Where the listing cannot be fetched, the answer is no. An unverified guess
  stays out of the record.

**Effect on bigcapital:**

| | before | after |
|---|---|---|
| `application_code_exists` | false | **true** |
| qualification | INVESTIGATE | **KEEP** |
| confidence | medium | **high** |

The keep is supported by `readme_describes_product=true`,
`application_code_exists=true`, `is_fork=false`,
`document_functionality_in_production_code=true`, with
`infrastructure_service_present=true` and confirmed generation/conversion code
as the two supporting signals that make the confidence high.

**No qualification rule changed.** The keep gate, the rejection predicates, the
confidence bands and the scoring model are all untouched. The candidate moved
because its evidence became correct, which is the only way a candidate should
ever move.

**No other candidate was affected.** The other four were replayed verbatim from
the phase 8 artifact and produced byte-identical decisions: PurpleOps
investigate/medium, docbase investigate/low, traprange
reject/`single_incidental_use`, sambanova reject/`tutorial_or_demo`.

**Qualification over the five real candidates, corrected:**

| | count |
|---|---:|
| keep | **1** |
| investigate | 2 |
| reject | 2 |
| confidence high / medium / low | 1 / 3 / 1 |

**Verification:**

| Check | Result |
|---|---|
| Full suite | **679 passed** (was 673) |
| Evidence + qualification | 165 passed |
| Live refresh scope | bigcapital only |
| Other candidates' decisions | unchanged |

Six regression tests were added: a `packages/` monorepo counting as
application code, a documentation-only `packages/` not counting, an unlistable
workspace not counting, a workspace holding only files not counting, no extra
listing when a plain application directory is already present, and a workspace
being inspected when the answer does hinge on it.

One test correction of my own: an assertion claimed `packages/` was listed by
the workspace inspection when manifest discovery had already listed it for its
own reasons. The test now uses `modules/`, which manifest discovery has no
reason to open, so a listing of it can only have come from the code path under
test.

Not committed. Phase 10 (scoring engine) has not been started.

*Later note: Phase 9 was approved and committed as `ecaa22b`.*

## Phase 10A - Scoring preflight and documentation correction

**Date:** 2026-08-20

A read-only preflight before implementation found weights, caps, formula and
database mutually consistent, and the two synthetic fixtures reproducing
exactly (4.60 -> 92, 2.30 -> 46). It also found **two contradictions inside
SCORING_MODEL.md**, both of which would have made the rubrics unimplementable
as written:

1. **What does "unknown" score?** Section 2 rung 1 said "genuinely unknown"
   scores 1, while sections 7, 12, 15 and IMPLEMENTATION_PLAN all say 0. Not
   academic: at 1, EstateProposal computes to 49, contradicting its own stated
   46.
2. **Section 13's confidence bands had a gap.** 6 or 7 dimensions evidenced
   with qualification confidence *not* high matched no band, and that is
   exactly the EstateProposal case, which section 15 resolves as medium.

Both were approved and corrected in SCORING_MODEL.md, targeted edits only:
section 2 now places unknown unambiguously at 0 and reserves rung 1 for
confirmed-but-minimal evidence, and section 13 spells out the medium fallback.
No weight, cap, formula or fixture value was touched.

## Phase 10 - Scoring engine

**Date:** 2026-08-20

**What changed:**

- `src/dependency_map/scoring.py` - seven rubric functions, `score_candidate`,
  `compute_raw_weighted_score`, `compute_final_score`, `applicable_gates`,
  `apply_gate_caps`, `assess_confidence_band`, `ScoringEngine`,
  `ScoringReport`.
- `src/dependency_map/storage.py` - `candidates_needing_scoring`.
- `src/dependency_map/run_manager.py` and `cli.py` - the `scoring` stage.
- `tests/test_scoring.py` - 66 tests.
- Four stale later-phase assertions updated, and `test_run_manager.py`'s
  harness now supplies a scoring engine.

**Verification:**

| Check | Result |
|---|---|
| Full suite | **745 passed** (was 673) |
| Scoring tests | 66 passed |
| Sockets blocked | 745 passed, 0 connection attempts |
| MedReport Solutions | raw 4.60, final **92** |
| EstateProposal | raw 2.30, final **46** |
| docutils-sandbox | rejected, **no score row** |
| Rescoring determinism | identical rows |
| Rejected candidates with a score row | **none** |

**Decisions:**

1. **Decimal arithmetic, not float.** 4.60 is exactly 4.60, so section 15's
   math reproduces rather than approximating.
2. **Half-up rounding.** Python's built-in `round` is banker's rounding and
   would turn 46.5 into 46. A reader checking by hand rounds half up.
3. **A cap is only recorded when it actually binds.** A candidate scoring 12
   under a cap of 20 is not being capped, and recording one would misdescribe
   the record. `gate_cap_applied` stays null there while
   `gates_triggered` still reports the condition held.
4. **Unknown and confirmed-zero are kept apart in code, not just in prose.**
   `DimensionResult` refuses to exist with `unknown=True` and a non-zero score,
   and only the unknown kind reaches `unknown_dimensions`. A candidate using a
   managed engine scores 0 on build-vs-buy because that is the answer, and is
   not listed as unknown.
5. **Weights and caps are read from `weights.yaml`.** Tests assert the literals
   `0.15`, `0.20`, `= 20`, `= 40` and so on do not appear anywhere in
   `scoring.py`.
6. **`pipeline_complexity` is unknown when code usage is unconfirmed**, per
   CANDIDATE_SCHEMA.md section 8: only the manifest was seen, so the code path
   was never inspected and nobody knows how complex the pipeline is.
7. **`industry_category` supports a rung but never carries one.** Rungs 3 to 5
   of section 5 need the vertical *and* language tying the document to an
   obligation or deliverable. A test runs four different verticals through
   identical evidence and asserts the rung does not move.
8. **Nothing reads star count.** Two tests assert that a repository with 90,000
   stars and one with 1 score identically on volume and leverage.
9. **`build_vs_buy_signal` never auto-assigns rung 5**, which requires judging
   that a pipeline duplicates SuperDocs. No stored field evidences that.

**Scoring over the real stored sample** (5 candidates, not a ranking):

| candidate | qual | vol | cplx | crit | pipe | maint | b/b | lev | raw | final | conf | cap |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| bigcapital | keep | 1 | 0 | 2 | 1 | 0 | 0 | 2 | 0.85 | **17** | high | - |
| PurpleOps | investigate | 1 | 1 | 1 | 2 | 0 | 3 | 0 | 1.20 | **24** | medium | - |
| docbase | investigate | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0.20 | **4** | low | - |
| traprange | reject | - | - | - | - | - | - | - | - | **no row** | - | - |
| ai-starter-kit | reject | - | - | - | - | - | - | - | - | **no row** | - | - |

`maintenance_burden` is unknown for all three scored candidates, as expected
for the MVP. No gate cap bound, because every score already sits below the
lowest cap of 20.

**Observations, recorded rather than acted on:**

The scores are low across the board, and two effects deserve naming before any
larger run.

**bigcapital, the only keep, scores 17 and ranks below an investigate.** Its
profile is coherent under the model as written: it uses Gotenberg, so
`build_vs_buy_signal` is a *confirmed* 0 by section 8 rung 0, which names
Gotenberg explicitly; its Gotenberg usage is conversion-only, so
`category_count=1` gives complexity 0 and one observed stage gives pipeline
complexity 1. The model asks how much of what SuperDocs sells a team is
currently building itself, and a team that already bought a conversion service
is building less of it. That is the model working, not a defect. Whether it
matches commercial intuition is a separate question, and one for the weight
review in section 17 of SCORING_MODEL.md rather than for code.

**PurpleOps outscores it at 24** largely on `build_vs_buy_signal=3`, because it
builds on docxtpl rather than adopting a managed engine.

Neither observation was allowed to influence the implementation. No weight,
cap or rubric was adjusted.

**Also worth flagging for the larger run:** four of the seven dimensions
(`document_volume`, `business_criticality` partly, `commercial_leverage`,
`maintenance_burden`) depend on text the collector does not store in full. Only
a short README excerpt and the notes fields are kept, so these rubrics will
return unknown or a low rung for most candidates. That is faithful to the
evidence-first rule and to section 12's unknown-as-0, but it means absolute
scores will cluster low, and the ranked table's value will come from relative
order rather than from the numbers reading as percentages.

Not committed. Phase 11 (report generator) has not been started.

*Later note: Phase 10 was approved and committed as `d91ba88`.*

## Phase 11 - Report generator

**Date:** 2026-08-20

**What changed:**

- `src/dependency_map/report.py` - `gather_report_data` (one read pass),
  `render_csv`, `render_markdown`, `write_report`, `describe_query_coverage`,
  the `RankedCandidate` / `DiscoveryHit` / `ReportData` / `ReportSummary`
  value objects.
- `src/dependency_map/storage.py` - `list_ranked_candidates` (the keep/
  investigate-with-a-score join, ordered and tie-broken) and
  `list_all_discovery_queries`.
- `src/dependency_map/cli.py` - a `report` command. Reads only the database;
  needs no `GITHUB_TOKEN`.
- `tests/test_report.py` - 47 tests, one per numbered scenario in the phase
  brief plus the CSV/Markdown consistency checks.
- Five stale "report.py must not exist yet" assertions retired across
  `test_discovery.py`, `test_evidence.py`, `test_qualification.py`,
  `test_run_manager.py`, `test_scoring.py`. Two of the five had become
  no-op tests with empty bodies once the guard was removed, and were deleted
  rather than left as hollow placeholders.

**Verification:**

| Check | Result |
|---|---|
| Full suite | **790 passed** (was 745) |
| Report tests | 47 passed |
| Sockets blocked | 790 passed, 0 connection attempts |
| Reject candidates in CSV or Markdown | none, in every fixture |
| CSV/Markdown rank, id, score, status | consistent across both outputs |
| Rescoring the same data twice | identical ranking |

**The tie-break rule** (final_score DESC, then confidence_band DESC treating
high > medium > low, then candidate_id ASC) is enforced in the SQL join
itself, in `list_ranked_candidates`, not recomputed in Python, so the CSV and
the Markdown table are reading the same already-ordered rows and cannot
disagree with each other.

**Coverage honesty is one function, called everywhere a query's numbers are
shown.** `describe_query_coverage` is the only place that turns
`(total_count, returned_count, capped)` into a sentence, used identically in
the ranked table, in each candidate's discovery provenance, and in the query
method section's worked examples. A capped query always reads "Sampled N of
M matches ... a partial sample, not an exhaustive result"; an uncapped one
reads "the full result set was below GitHub's pagination ceiling". A test
asserts the capped wording never contains the phrase "M repositories were
inspected" or "M inspected", which is the exact confusion the phase brief
warned against.

**Decisions:**

1. **Rejects are excluded by the join, not filtered after the fact.**
   `list_ranked_candidates` inner-joins `scores`, and a reject never has a row
   there (SCORING_MODEL.md section 1), so the exclusion is structural. The
   `qualification_status IN ('keep','investigate')` clause is kept anyway as
   a second, explicit guard, since the report is the last place a rejected
   candidate must never surface.
2. **One read pass, both outputs.** `gather_report_data` runs once;
   `render_csv` and `render_markdown` both consume the same `ReportData`
   object, which is what makes the CSV/Markdown consistency tests
   meaningful rather than a coincidence of two independent queries.
3. **The git commit hash is best-effort and never fatal.** `_commit_hash`
   wraps a `git rev-parse HEAD` subprocess call and returns `None` on any
   failure, so a report generated outside a git checkout, or before the
   first commit, still renders cleanly with "unavailable" in its place.
4. **Score is always rendered as `N/100`, never as a percentage.** A test
   asserts `"17%"` and the word "likelihood" never appear; the one
   permitted use of the word "probability" is the report's own explicit
   disclaimer ("a score, not a probability"), which a first draft of the
   test wrongly banned outright before being corrected.
5. **`industry_category` carries an inline caveat everywhere it is shown**
   in a candidate's detail section: "keyword-derived; treat as
   low-confidence supporting evidence, never a determining factor" - the
   same guidance approved at the phase 9 checkpoint, now visible to a human
   reader rather than only enforced in code.
6. **The CLI `report` command needs no `GITHUB_TOKEN`.** It calls
   `config_from_context(ctx, require_github_token=False)`, matching the
   `discover` and `runs` commands' precedent for stages that touch no
   network.
7. **A missing or schema-mismatched database exits non-zero with a clean
   message**, via `click.ClickException`, rather than a raw traceback:
   `ReportError`, `DatabaseNotInitialized` and `SchemaVersionMismatch` are
   all caught in the CLI command.

**Human review checkpoint**, generated from a representative sample (the five
real Phase 8/9/10 candidates, replayed with their actual stored evidence,
plus two runs and eight discovery-query records including the real measured
Gotenberg/docxtpl/docxtemplater/python-docx/Apache PDFBox totals and two
zero-result examples). Written to the scratchpad, not to `outputs/`, since no
real full run has happened yet - that is phase 13, and writing a sample into
the repository's actual deliverable path would misrepresent it as one.

| | |
|---|---|
| Ranked candidates | 3 (1 keep, 2 investigate) |
| Rejected, correctly absent from both outputs | 3 |
| Discovery queries | 8 (5 capped, 2 zero-result) |
| Top of ranking | PurpleOps 24, bigcapital 17, docbase 4 - internally consistent with the phase 10 scores, sensible given the evidence shown |
| Unknown dimensions | visible in the ranked table, per-candidate table, and as explicit "Unknown" lines; none silently smoothed into a bare number |
| Capped-query wording | "Sampled 10 of 16,832 matches ... a partial sample, not an exhaustive result" - never implies the total was inspected |
| Zero-result queries | both shown, including the historically real broken ReportLab `language:python` query, in its own table |

**One artifact of the review script worth naming, not a defect in
report.py:** the sample database's `discovery_queries.query` field was seeded
with the surfacing library's name (`"Gotenberg"`, `"docxtpl (python-docx-template)"`)
rather than a real GitHub search string, since the replayed Phase 8 JSON never
recorded the original query text. The report renders exactly what is stored,
correctly; the sample data itself is a simplification. A real run persists the
actual query string, and the report would show that instead.

**Known limitations:**

- Four of the seven scoring dimensions depend on prose the collector does not
  store in full (SCORING_MODEL.md's own observation, carried from phase 10),
  so most candidates will show several "Unknown" lines. The report states
  this honestly rather than hiding it, but it means the ranked table's early
  entries will look sparse until a larger corpus and, eventually, the phase
  14 maintenance-burden pass exist.
- The "candidates with enhanced evidence" executive-summary line is
  permanently 0 until phase 14 runs; it is not a placeholder metric, it is
  the honest current count.
- No real `data/dependency_map.db` exists yet. Phase 13 is the first real
  run; today's report is exercised only against synthetic and replayed
  sample data.

Not committed.

## Phase 12 - Full pipeline integration, resumability, and security

**Date:** 2026-08-21

**What changed:**

- `tests/test_integration.py` - 56 new tests, one file, organized under the
  17 numbered sections of the phase brief (full mocked pipeline, multi-run,
  interrupt/resume, cache, report consistency, schema integrity, security,
  CLI smoke, idempotency, pipeline failure, coverage/undercount, fresh-batch,
  output cleanliness). No new discovery strategy, scoring rule, qualification
  rule, or external service was added; every test drives the existing
  modules together against mocked or seeded data.
- `src/dependency_map/cli.py` - one bug fix, described below. No other
  production code changed.

**A real bug was found and fixed, not introduced by this phase's tests:**
`dependency-map run --stage qualification` and `run --stage scoring`
unconditionally required `GITHUB_TOKEN`, because `run_command` always called
`config_from_context(ctx)` with its default `require_github_token=True`.
Both `QualificationEngine` and `ScoringEngine` are proven to make zero
network calls (their own dedicated no-network tests already established
this), so requiring a token to run either stage alone contradicted a
guarantee the engines themselves already provide, and would block an
offline rerun over already-collected evidence - exactly the resumability
story phase 8-11 built. Fixed by computing `needs_token` from the requested
stage set (`True` only if `discovery` or `evidence` was requested) and
passing it through to `config_from_context`. Covered by two new regression
tests (`test_9_cli_run_qualification_stage_needs_no_token`,
`test_9_cli_run_scoring_stage_needs_no_token`), each running the CLI command
with `GITHUB_TOKEN` explicitly unset.

**Verification:**

| Check | Result |
|---|---|
| Full suite | **846 passed** (was 790; +56 from this phase) |
| Integration tests (this phase) | 56 passed |
| Sockets blocked, full suite | 846 passed, **0 connection attempts** |
| Interrupt/resume | uses real persisted SQLite state (a second on-disk database, not a mocked flag); completed candidates are provably never re-fetched after resuming; final state matches an uninterrupted run field-for-field |
| Fresh-batch guard | blocks a duplicated run-2 query plan via a transport that raises if ever called - proven to fire before any request is attempted, not just before any request succeeds |
| Report consistency | CSV and Markdown agree on candidate id, rank order, final score, confidence band, qualification status, and evidence coverage, both in the 3-candidate keep/investigate/reject mix and in a separate 5-candidate seeded set |
| Security | fake fixture-only secrets (a fake GitHub token, a fake Libraries.io key) confirmed absent from CSV, Markdown, logs, and every relevant database table after a full pipeline run with both set as real env vars; `.env`, `data/*.db`, `.venv/` confirmed still gitignored via `git check-ignore`; `PROGRESS.md`/`config.yaml`/`weights.yaml` confirmed to contain no secret-shaped pattern. The real `.env` value was never inspected or printed. |
| Coverage/undercount | a `total_count=75648, returned_count=10, capped=true` query renders as "Sampled 10 of 75,648" and the phrase "partial sample"; never renders as if 75,648 repositories were inspected |
| Idempotency | evidence/qualification/scoring/report each re-run against fully-complete state with `pending()` empty and record counts unchanged |
| Pipeline failure | one candidate's API failure (500) leaves the other candidate's evidence intact; a systemic failure (rate limit) propagates and stops the batch rather than silently continuing; a malformed search hit missing `repository` produces no candidate row rather than a corrupted one; `report` on a schema-less database raises `ReportError` cleanly; a schema-version mismatch raises `SchemaVersionMismatch` before any query runs |
| Output cleanliness | `git status` shows only this phase's own two changes (`cli.py`, new `test_integration.py`); no real `data/dependency_map.db`, no stray scratch secrets, no unintended `outputs/` content |

**Interrupt/resume was built against real state, per the brief's explicit
requirement.** The test constructs a second on-disk SQLite database, runs
discovery, collects evidence for the first two of four candidates, then
throws away the in-memory `EvidenceCollector` entirely and builds a fresh one
over the same connection. That fresh collector's own `pending()` is what
decides what still needs work - there is no resume flag or checkpoint
object anywhere in the code path. The two already-completed candidates are
asserted to never appear in any client call made after the "restart," and
the final per-candidate business-evidence rows are asserted equal, field by
field, to an uninterrupted run over the identical fixture data.

**Assumptions validated by this phase:**

- The "ask the database what's missing" resumability pattern (technical
  design doc section 16) genuinely produces identical output whether a run
  completes straight through or is interrupted and resumed - not just in
  principle, but checked against real row-level output.
- The fresh-batch guard genuinely runs before any API budget is spent, not
  merely before any API call succeeds - the exploding-transport test would
  fail if the guard were checked lazily inside the request path instead of
  up front against stored query records.
- Rejects are structurally excluded from both report formats via the SQL
  join in `list_ranked_candidates`, confirmed again here against a fresh
  keep/investigate/reject mix generated through the full pipeline rather
  than seeded directly.

**Known limitations:**

- The no-live-network guarantee is verified via a scratchpad-only pytest
  plugin (`no_network_plugin.py`, socket-patching), invoked manually with
  `PYTHONPATH=<scratchpad> pytest -p no_network_plugin` rather than wired
  permanently into `conftest.py`. This matches every prior phase's pattern
  and was a deliberate choice this phase, to avoid adding a new permanent
  test-suite feature during a phase explicitly scoped as validation, not
  feature-expansion. The check itself (846 passed, 0 connection attempts)
  was run and is real; only its wiring is manual.
- No new production behavior was validated end-to-end against a *real*
  GitHub API response shape beyond what `test_github_client.py` and
  `test_evidence.py` already cover - this phase's CLI smoke tests use a
  hand-built fake transport keyed by URL substring, not recorded real
  responses. Phase 13's live run remains the first true end-to-end check
  against the real API.
- One implementation bug was found and fixed (the qualification/scoring
  token requirement, above). No design contradiction in the planning
  documents was found; none were modified.

Not committed.

## Phase 13 - First real end-to-end run (Run 1)

**Date:** 2026-08-20, 18:46:13Z to 20:05:08Z (report generated 20:05Z).
The first live run against real public GitHub data. No code was changed
during the run.

**Pre-run state:** `.env` present with a real `GITHUB_TOKEN` (never printed,
confirmed gitignored at `.gitignore:2`); working tree clean at Phase 12's
commit `8ad4f17`; **no database existed at all**, so Run 1 could not be
contaminated by earlier data. `LIBRARIES_IO_API_KEY` is not set - the run
needed only GitHub. The database was created with `db.initialize_database`
directly, because there is no `init` CLI command (see limitations).

### Discovery - 18:46:13Z to 19:13:16Z (27 minutes)

| | |
|---|---|
| Run id | `run_1` |
| Queries executed | 236 of 237 planned |
| Queries failed | 1 (`"pdfbox" filename:pom.xml pushed:2025-11-22..2026-02-20`, three transport failures) |
| Total GitHub matches across queries | 57,374 |
| Raw results returned | 472 |
| Unique repositories | 412 |
| Previously seen | **0** (correct for Run 1) |
| Capped queries | 6 |
| Zero-result queries | 219 |

Tier distribution: tier 1 - 9 queries, 39,650 matches, 250 returned, 3
capped, 0 zero-result. Tier 2 - 8 queries, 17,724 matches, 222 returned, 3
capped, 0 zero-result. Tier 3 - 220 queries, **0 matches, 0 returned, 219
zero-result, 1 failed**.

### What broke: Tier 3 produced nothing, and the cause is `pushed:`

**Every single Tier 3 query returned zero results.** Tier 3 is 220 of the
237 planned queries - 93% of the query budget and roughly 24 of the 27
minutes of discovery - and it contributed **0 of the 412 candidates**. All
412 came from tiers 1 and 2.

The cause is not noise or an empty universe. It is that **GitHub's code
search API does not support the `pushed:` qualifier**. `pushed:` is a
*repository* search qualifier; code search accepts `filename:`, `path:`,
`extension:`, `language:`, `repo:`, `org:`, `user:`, `size:` and treats
anything else as literal text to match. So every sliced query was really
searching for the literal string `pushed:2026-05-23..2026-08-21` inside
files, which matches nothing.

Confirmed directly with one controlled pair of live calls on the same query:

| Query | Total matches |
|---|---|
| `"python-docx" filename:requirements.txt` | **75,648** |
| `"python-docx" filename:requirements.txt pushed:2026-05-23..2026-08-21` | **0** |

The correlation across the run is perfect: all 17 queries without a window
returned results, all 219 queries with a window returned zero.

This means the mandatory Tier 3 date-window slicing - the mechanism
SEARCH_STRATEGY.md relies on to work around GitHub's 1,000-result
pagination ceiling - silently nullifies the queries it is applied to. It
does not merely under-sample; it returns nothing at all.

**Not patched, deliberately.** Section 14 of the phase brief permits code
changes only for a catastrophic defect that prevents safe completion. This
one did not: the run completed end to end on the 412 tier-1/tier-2
candidates and produced real outputs. Fixing discovery mid-run would also
have made Run 1's numbers unreproducible. It is reported here for a decision
before Run 2, since it invalidates the rotation design as currently built:
`plan_rotation` shifts date windows between runs, so on the current code
Run 2's Tier 3 would also return zero.

Worth naming plainly: **every test in the suite passes and none of them
caught this**, because the fake clients answer whatever query they are
given. Query *validity against the real API* was never something the mocked
tests could check. Phase 6A measured tier 3 empirically before mandatory
slicing was introduced, so the sliced form had never been executed live
until today.

### Evidence - 19:18:42Z to 20:04:42Z (46 minutes)

Run in five resumable batches of 100 (`--evidence-limit 100`, same
`--run-id run_1`), so progress committed incrementally rather than as one
27-minute transaction.

| | |
|---|---|
| Candidates processed | 412 |
| Successful | **412** |
| Failed | **0** |
| Cached API entries after the run | 2,811 |
| Dependency records written | 835 (`code_import` 451, `manifest_declaration` 264, `infrastructure_reference` 120) |

Evidence signal across the 412: code usage confirmed 279, infrastructure
service present 114, website detected 152, template directory present 42,
application code detected 252, **multiple document types handled just 1**.

### Qualification and scoring - 20:05:05Z to 20:05:08Z (3 seconds, offline)

Qualification: **keep 43, investigate 217, reject 152.** Rejection reasons:
`tutorial_or_demo` 76, `single_incidental_use` 75,
`personal_project_no_customers` 1. Confidence: high 32, medium 295, low 85.

Scoring: **260 scored** (43 keep + 217 investigate), **0 rejects scored**,
**0 gate caps applied**. Confidence bands: high 25, medium 184, low 51.
Unknown dimensions: `maintenance_burden` 260 (all of them, as designed until
phase 14), `commercial_leverage` 191, `pipeline_complexity` 51,
`document_volume` 47, `build_vs_buy_signal` 39, `document_complexity` 39.

Score distribution: min 0, max 38, median 15, mean 14.6 - 12 candidates in
30-39, 67 in 20-29, 116 in 10-19, 65 in 0-9.

### Output

`outputs/ranked-candidates.csv` (182 KB, 260 rows) and
`outputs/dependency-map-report.md` (876 KB). Both scanned: no token or
secret pattern present. Capped queries render as "Sampled 30 of 17,216
matches ... a partial sample", never as if the total was inspected.

### Candidate-quality observations

**Qualification is doing real work on obvious noise.** The rejected set
includes DefinitelyTyped (51,380 stars), `mayfrost/guides`,
`captn3m0/google-sre-ebook`, `benman1/generative_ai_with_langchain` and
similar - all `tutorial_or_demo`. It also correctly rejected
`carboneio/carbone`, the vendor of one of the libraries in the universe,
as `single_incidental_use`.

**A noise cluster survives into `investigate` rather than `reject`:**
self-hosting app-store and docker-collection repositories
(`runtipi/runtipi-appstore`, `WisdomSky/CasaOS-Coolstore`,
`pooneyy/1Panel-Appstore`, `Websoft9/docker-library`,
`MVladislav/vm-docker-collection`, `yuhuyoyo/devcontainers`). They surface
on tier-1 Docker queries because such repos ship compose files for hundreds
of apps, LibreOffice and Gotenberg among them. All 24 score-0 candidates are
of this shape. Scoring ranks them last, which is the correct outcome, but
they are not filtered out.

**Scores are compressed into the bottom 40% of the scale.** The maximum
across 412 real repositories is 38/100. Two structural causes, both by
design rather than defect: `maintenance_burden` (weight 0.15) is unknown for
every candidate until phase 14, and unknown weights are not redistributed;
and `document_complexity` is near-zero almost everywhere because
`multiple_document_types_handled` fired for exactly 1 of 412 repositories.
Whether that last number reflects reality or a too-strict detector is worth
checking before it is treated as a finding.

**Top-of-ranking ties are dense and include likely false positives.** Six
candidates tie at 34 on the identical dimension vector (3,0,2,2,0,3,3), and
among them `jolie-z/Auto-JobHunter` (a personal job-application tool),
`shehanrathnayake/checkpoint-pos-system` (a student POS project) and
`EaseTech/easytest-core` (a test framework) do not look like the growth
team's intended prospect. The tie-break is deterministic, so the ordering is
reproducible, but the rubric is not currently separating these from
`intuitem/ciso-assistant-community` or `PipedreamHQ/pipedream`.

**`industry_category` misfires visibly**, exactly as its own caveat warns:
`bagofwords1/bagofwords`, a BI/analytics tool, is labelled
`healthcare_diagnostics`. 168 of 260 are `unknown`. The report already
carries the "keyword-derived, never a determining factor" caveat inline.

**`company_name` extraction produces artifacts** on some repositories -
"BootSimply Solutions  Licensed", "Universitätsbibliothek Mannheim
Authors" - evidently picking up trailing words from LICENSE or README
lines. Cosmetic, and traceable to stored evidence rather than invented, but
it will read as sloppy to a human reviewer.

**Query effectiveness, by keep-rate** (the diagnostic most likely to shape
Run 2). Strongest: `"carbone" filename:package.json` 10 keeps of 23 (43%),
`"subprocess pandoc"` 2 of 7 (29%), `"gotenberg" filename:Dockerfile` 6 of
29 (21%), `"docxtpl" filename:pyproject.toml` 4 of 29 (14%),
`"libreoffice" filename:Dockerfile` 4 of 30 (13%). Weakest:
`"docx-mailmerge" filename:requirements.txt` 0 keeps and 25 rejects of 29,
`"unoconv"` 0 keeps and 17 rejects of 27, `"docx-mailmerge"
filename:pyproject.toml` 0 of 12, `"libreoffice" filename:docker-compose.yml`
0 of 17, `"docxtpl" filename:requirements.txt` 1 keep of 30. The pattern:
Dockerfile and `pyproject.toml` slices are consistently cleaner than
`requirements.txt` and bare-term queries.

### Other findings, not patched

- **Discovery commits once, at the end of the whole stage.** `db.connect`
  (db.py:332) commits only when the `with` block exits, so all 236 queries
  ran inside a single transaction: an abort at minute 26 would have rolled
  back the entire run and wasted the API budget. Phase 12's interrupt/resume
  test did not catch this because it interrupted at the collector level with
  the connection still open. Evidence collection was deliberately run in
  batches to work around it.
- **There is no `dependency-map init` command.** The database can only be
  created by calling `db.initialize_database` from Python. Every CLI command
  fails with `DatabaseNotInitialized` until that is done by hand.
- Local network was intermittently unstable during discovery (DNS
  resolution failures, SSL EOF, connection resets). The reliability layer
  retried, backed off, recorded one permanent query failure and continued -
  which is the intended behaviour and the reason 236 of 237 queries
  completed.

**Known limitations of Run 1:** the corpus is tier-1 and tier-2 only, so it
is biased toward infrastructure (Docker/LibreOffice/Gotenberg) and
template-library users, and it is a 472-result sample of 57,374 matches -
never an exhaustive census. No maintenance-burden evidence exists yet
(phase 14). No outreach or contact capability exists, at any phase.

Not committed. Run 1 is not final; see the correction pass below.

## Phase 13 correction pass - live discovery defects

**Date:** 2026-08-21

Run 1 completed end to end but is **not** the final Run 1: the live experiment
exposed a defect that made 93 percent of its query budget useless. This pass
fixes the three findings from that run. It changes no scoring logic, no
qualification rule, and no report code.

**What changed:**

- `src/dependency_map/dedup.py` - `quarterly_windows` replaced by
  `size_windows`, backed by a new `SIZE_BUCKETS` pool of eight contiguous
  byte ranges. `plan_rotation` now walks that pool instead of walking dates
  backwards; `RotationPlan.description` reports size slices.
- `src/dependency_map/discovery.py` - new `REPOSITORY_ONLY_QUALIFIERS` set and
  a `validate_query` rule that refuses any query carrying one. Discovery now
  commits per query and skips queries this run already answered.
- `src/dependency_map/storage.py` - `completed_query_ids(conn, run_id)`, the
  resume primitive: which queries already have a `total_count`.
- `SEARCH_STRATEGY.md` - section 4.5 rewritten around file-size slicing, with
  the measured numbers and an explicit correction notice for the date-window
  advice it previously gave. Section 7 updated to match.
- `tests/conftest.py`, `tests/test_db.py` - the retired production-database
  invariant, replaced (below).
- `tests/test_integration.py` - 22 new tests in a section 14 block.
- `tests/test_dedup.py`, `test_discovery.py`, `test_run_manager.py`,
  `test_storage.py` - date-window fixtures updated to size slices.

### Finding 1 - `pushed:` is not a code-search qualifier

All 220 tier-3 queries in Run 1 returned zero. `pushed:` belongs to
*repository* search; code search matches it as literal text inside a file, so
a query carrying it returns zero rather than a narrowed set, and reports that
zero as if it were a real finding. Measured on one query, live:

| Query | Matches |
|---|---|
| `"python-docx" filename:requirements.txt` | 75,648 |
| the same query plus `pushed:2026-05-23..2026-08-21` | 0 |

**The replacement is file size.** Before proposing it, candidate axes were
measured live against the same base query rather than reasoned about, since
reasoning about the API is exactly what produced the defect:

| Slice | Matches |
|---|---|
| no slice | 75,648 |
| `size:0..500` | 46,848 |
| `size:500..2000` | 19,872 |
| `size:>2000` | 12,352 |
| `path:/` | 49,536 |
| keyword `contract` | 204 |
| keyword `invoice` | 33 |
| `fork:false` | HTTP 422, rejected |

The three size buckets sum to roughly the unsliced total, which is what
separates a partition from a filter, and every file has exactly one size, so
the buckets neither overlap nor leave a gap. `path:` works but has no clean
complement. Keyword narrowing drops 99.7 percent of matches and is a precision
probe, not a coverage mechanism; generating it as one would misrepresent what
a run reached. `fork:` is rejected outright.

**A deviation worth naming:** the correction brief listed manifest family,
path, language, and keyword as the axes to use. Measurement showed none of
them can break the 1,000-result ceiling with auditable coverage - manifest
family leaves 45,000-plus per slice, language is incompatible with manifest
filenames by the pre-existing guard, path does not partition, and keyword is
lossy by two orders of magnitude. `size:` was added instead. It is not
date-based, and it is a single constant list if it needs to be reverted.

**Known limit, recorded rather than smoothed over:** a date walk could march
backwards forever; eight buckets at four per run gives exactly two disjoint
runs. Run 3 reuses Run 1's slices and `verify_fresh_batch` will refuse it, at
which point a further axis has to be chosen deliberately. A test asserts the
wrap so it fails loudly if the pool is ever widened.

### Finding 2 - discovery committed once, at the end

`db.connect` commits only when its `with` block exits, so Run 1's 237 queries
shared one transaction and an abort at minute 26 would have discarded all 26
minutes of API budget. `run_manager.py` already carried the comment
"Discovery already persisted whatever it completed, so the run is resumable" -
which was aspirational, not true.

Now: one query, the candidates it surfaced and the evidence rows linking them
are one committed unit. A resumed run loads `completed_query_ids` and skips
what is already answered, before spending any budget. A *failed* query leaves
`total_count` null on purpose, which is what distinguishes it from a genuine
zero and gets it retried rather than skipped. The skip also has to happen
before `create_discovery_query`, because that function upserts and would
otherwise overwrite a real stored total with null; a test covers exactly that.

No new storage architecture was needed. `create_discovery_query`,
`insert_discovery_evidence` and `insert_candidate_if_new` already carried
`ON CONFLICT` clauses, so duplicate suppression was already correct and only
the commit boundary and the resume check were missing.

### Finding 3 - the stale production-database invariant

`test_default_db_path_is_not_touched_by_the_suite` asserted
`data/dependency_map.db` does not exist. That could only hold until the tool
was used for the thing it was built for, and Phase 13 created it.

Replaced with the invariant actually wanted: tests never *write* the
production path. A session-scoped autouse fixture in `conftest.py` snapshots
the production file's size and mtime before the suite and asserts they are
unchanged after it, and a unit test asserts the shared `db_path` fixture
resolves under `tmp_path` and is not the production path. Verified by running
the full suite with the real 67 MB Run 1 database present: byte-identical
before and after.

**Verification:**

| Check | Result |
|---|---|
| Full suite | **868 passed** (was 846; +22) |
| Sockets blocked, full suite | 868 passed, **0 connection attempts** |
| Production database after full suite | unchanged, 66,920,448 bytes, same mtime |
| Generated queries containing `pushed:` | 0 of 237 |
| Repository-only qualifiers refused | 9 of 9 (`pushed`, `created`, `stars`, `forks`, `fork`, `topic`, `license`, `archived`, `is`) |
| Tier-3 slices drawn from `SIZE_BUCKETS` | 220 of 220 |
| Run 1 vs Run 2 slice sets | disjoint |

### Live validation

Six corrected tier-3 queries, run against the real API into a throwaway
scratchpad database. The production database was not touched and the full
30-library discovery was **not** run.

| Query | Total | Returned |
|---|---|---|
| `"python-docx" filename:requirements.txt size:0..250` | 32,064 | 30 |
| `"python-docx" filename:requirements.txt size:251..500` | 16,128 | 30 |
| `"reportlab" filename:requirements.txt size:0..250` | 30,016 | 30 |
| `"reportlab" filename:requirements.txt size:251..500` | 15,040 | 30 |
| `"pdfbox" filename:pom.xml size:0..250` | 3 | 3 |
| `"pdfbox" filename:pom.xml size:251..500` | 2 | 2 |

Six of six non-zero, against 0 of 220 in Run 1. 117 unique candidates from six
queries, all query records persisted with correct totals and cap flags.

Two observations from the validation, neither a defect:

- **docxtpl has no tier-3 query.** It is a tier-2 library in the universe, so
  the tier-3 subset correctly excluded it. Probed separately at
  `"docxtpl" filename:requirements.txt size:0..250` - 784 matches.
- **The small buckets are nearly empty for `pom.xml`.** A Maven POM is rarely
  under 500 bytes, so PDFBox returned 3 and 2 there while
  `size:2001..4000` returned 6,704 and `size:>16000` returned 1,788. The
  buckets are a valid partition but they are not evenly filled per ecosystem,
  which means Run 1's low four buckets favour Python manifests and Run 2's
  high four will favour Java ones. Worth knowing when comparing the two runs;
  not worth special-casing per ecosystem yet.

**Still open:** Run 1's outputs remain on disk and are not final. Re-running
discovery with corrected slicing has not been done and was explicitly out of
scope for this pass.

Not committed. Run 2 not started. Phase 14 not started.

## Phase 14 - Evidence quality and maintenance burden

**Date:** 2026-08-21

**Why this phase was needed.** The phase 13 audit found 26 keep/investigate
candidates with no dependency row at all, 22 of them surfaced by a tier-1
infrastructure query. The cause was not a bad heuristic: `discovery_evidence`
never stored *which file* a search hit matched, so the collector fell back to
the repository root and could not open the compose file discovery had actually
found. Separately, `maintenance_burden` was unknown for all 233 scored
candidates, holding 15 percent of the weight and contributing nothing.

**A contradiction found and reported before any code was written.** The phase
brief proposed collecting commit-history metadata (commits in 30/90 days,
active contributors, churn, repository age) as the maintenance-burden
evidence. SCORING_MODEL.md section 7 does not grade that. Its rungs measure
how much custom code surrounds the document libraries; commit history appears
once, at rung 4, as a conditional corroboration. Activity and custom-code
volume are independent - a thin wrapper committed daily is a rung 1, an
elaborate hand-built system untouched for a year is a rung 5. The work stopped
and reported rather than inventing an activity-based rubric. The approved
revision keeps section 7 unchanged and builds a code-structure collector, with
commit data retained only for rung 4.

**Schema 2 to 3, migrated in place.** One explicit `migrate_v2_to_v3`
function, additive only, no migration framework. A verified backup was taken
first (`audit/phase14-run1-comparison/dependency_map.v2-backup.db`,
integrity ok). After migration every row count was identical, integrity was
ok, and every new column was null - a run-1 row genuinely does not know its
file path or its purpose, and a default would turn "never asked" into a
finding.

- `discovery_evidence` + `file_path`, `evidence_url`
- `pipeline_evidence` + `infrastructure_reference_present`, deliberately
  separate from `infrastructure_service_present`
- `business_evidence` + `is_catalogue_repository`,
  `readme_indicates_example_or_tutorial`, `has_examples_directory`
- new `maintenance_evidence` table, code-structure fields first, commit
  fields last

**Run 1's lost paths were recovered from cache, at zero API cost.** All 237
discovery queries were still in `api_cache` with their full response bodies,
so `file_path` and `evidence_url` were reconstructed for all 4,897
`discovery_evidence` rows by local read alone. **No live request was needed.**
39.4 percent of the recovered paths were not at the repository root, which is
the measurement that explains the run-1 gap directly.

**What changed, measured:**

| | Before | After |
|---|---:|---:|
| Zero-dependency keep/investigate candidates | 26 | **10** |
| `infrastructure_reference_present` recorded | 0 | 19 |
| Candidates with maintenance evidence | 0 | 64 |
| `maintenance_burden` unknown (scored set) | 233 | 170 |
| Total unknown dimensions | 549 | **423** |
| Qualification | 43 keep / 190 inv / 267 rej | 44 keep / 189 inv / 267 rej |

Maintenance rungs now distribute across the whole scale rather than sitting at
unknown: rung 1 = 15, rung 2 = 22, rung 3 = 3, rung 4 = 22, rung 5 = 1.

**The reference-versus-service split does real work.** `getumbrel/umbrel-apps`
now records a reference at `libreoffice/docker-compose.yml` with
`infrastructure_service_present = false` and `is_catalogue_repository = true`;
`pooneyy/1Panel-Appstore` matched at `apps/libreoffice/25.8.7/docker-compose.yml`,
five directories down. Neither path was reachable by a root listing. Run 1
had one flag for both meanings, so a catalogue listing hundreds of other
people's services looked identical to a company running one.

**One qualification change, from evidence rather than a rule change.**
`Swiss-Armed-Forces/Loom` moved investigate to keep once its nested compose
file produced real dependency evidence. No qualification rule was modified.
Weights, gate caps, confidence rules, SCORING_MODEL.md and weights.yaml are
all untouched.

**Limitations, stated rather than smoothed over:**

- **10 candidates remain zero-dependency.** Their discovery hit was a tier-3
  manifest match whose file the collector could not tie to a library entry.
  Not diagnosed further this phase.
- **`infrastructure_service_present` uses application-code presence as its
  discriminator**, which is a proxy, not proof that the application calls the
  service. `pooneyy/1Panel-Appstore` still reads as "service present" because
  it does contain application code alongside its catalogue.
- **The maintenance collector reads at most four files per candidate**, chosen
  from existing `code_import` evidence. A repository whose complexity lives in
  files no discovery query touched will read thinner than it is.
- **Repository-purpose signals are evidence only.** Nothing qualifies or
  scores on them yet, and a test asserts that flipping all three leaves the
  qualification outcome unchanged. Deciding whether a catalogue should be
  rejected is a later, explicit decision.
- **169 of 233 scored candidates still have `maintenance_burden` unknown**,
  because the pass was deliberately bounded to 64 high-value candidates.

**Verification:** 939 tests pass (was 893; +46), 0 network connection attempts
across the suite, production database untouched by the suite,
`integrity_check: ok` after migration and after every collection pass.

The committed Run 1 outputs were **not** regenerated. The before/after
comparison lives in `audit/phase14-run1-comparison/`.

Not committed. Run 2 not started.

### Phase 14 part A/B correction (same day)

**`infrastructure_service_present` was over-claiming.** It accepted "a compose
file exists and there is application code somewhere", which is co-presence,
not use. It now requires direct evidence: the service named in an actual
source file (a `code_import` row is only written for a real source file), or
its URL, host or configuration key referenced from source. A reference with
neither records `infrastructure_reference_present = true` and service = false.

| | Before | After |
|---|---:|---:|
| `infrastructure_service_present` | 62 | **22** |
| `infrastructure_reference_present` | 19 | **71** |
| Qualification | 44 / 189 / 267 | **44 keep / 176 investigate / 280 reject** |

Forty over-claims removed. Thirteen candidates moved investigate to reject on
the corrected evidence, with no qualification rule changed. Every catalogue
repository now reads reference = true, service = false, and the candidates
still claiming service use are recognisable document products
(`document-templating-service`, `simpledms`, `reubah`, `bigcapital`).

One regex bug was caught by its own test before it reached data: the word
`port` matches inside `import`, so `import gotenberg_helper` counted as
service wiring until a word boundary was added.

**The remaining 10 zero-dependency candidates are not one bug**, so they were
reported rather than patched:

| Class | Count | Detail |
|---|---:|---|
| Collector gap | 3 | the exact-path fetch covers only infrastructure filenames, so a matched nested manifest (`libs/langchain/pyproject.toml`) or source file (`src/parser/pandoc/cli.rs`) is never opened |
| Likely false positive | 4 | prose matches from over-broad bare tier-1 queries, in `.md`, `.texi` and README files. Recording nothing is correct |
| Valid non-package signal | 1 | matched `requirements.txt.old`, a backup file that is properly not treated as a manifest |
| Unclear | 2 | root `requirements.txt` matched by the co-occurrence query, which carries no single library to attribute |

The smallest correct fix for the first class is to extend the exact-path fetch
beyond infrastructure filenames to manifests and source files, since
`manifest_kind` and `is_source_file` already recognise all the paths involved.
That is one change, but it does not explain the other seven, so it was left
for an explicit decision.

**A defect this exposed, not fixed:** the 13 candidates that moved to reject
kept their existing `scores` rows, because the scoring engine skips rejected
candidates but never removes a score already written. Reports are unaffected
(rejects are excluded by SQL join, and the outputs are unchanged), but the
"no scores on rejected candidates" invariant is currently violated in the
database. The fix is a delete in the scoring engine when a candidate is
rejected; it was not made because it is outside the approved scope.

**Verification after the correction:** 952 tests pass, 0 network connection
attempts, `integrity_check: ok`, schema 3, and the committed Run 1 outputs are
byte-identical to commit 744654b.

**Stale scores on newly rejected candidates - fixed.** Re-qualification could
leave a score behind: a candidate scored under earlier evidence that later
becomes a reject kept the old row, because the scoring engine skips rejects
but never removed one already written. `upsert_qualification` now deletes the
score whenever it writes a reject, via a new `storage.delete_score`. That
chokepoint was chosen over the scoring engine because it is the single place a
qualification decision is written, so every path that rejects cleans up, and
repeating the call changes nothing. The scoring engine already refused to
score a reject, so nothing recreates the row afterwards.

Thirteen stale rows were removed from the Run 1 database: scores 233 to 220,
rejected-with-a-score 13 to 0, qualification counts unchanged at 44 keep /
176 investigate / 280 reject, integrity ok. Reports were never affected -
rejects are excluded by SQL join - and the committed Run 1 outputs remain
byte-identical.

959 tests pass, 0 network connection attempts.

## Phase 15 - Official Run 2 (second fresh-batch execution)

**Date:** 2026-08-24

Proved the machine can run again with no manual candidate selection and no
code change, and obtain a genuinely fresh discovery batch. `verify_fresh_batch`
ran before any request and reported 237 planned, 0 already used, 237 novel.

**Discovery:** 237 queries, 0 failed, 3,584 new candidates, 630 previously
seen, 4,214 unique repositories surfaced. Tier-3 (the only sliced tier)
overlapped run 1 by zero queries; the 17 repeated queries are exactly the
unsliced tier-1/tier-2 queries, which need no slice. Database grew 4,429 to
8,013 candidates.

**Evidence sample:** same deterministic rule as run 1 (tier = strongest
discovery tier, `candidate_id` ascending, 100/100/300), scoped to what run 2
surfaced. 500 selected, 281 collected, 219 already had evidence from being
seen before, zero failures.

**Qualification (rules unchanged):** 46 keep, 173 investigate, 281 reject.
**Scoring (weights unchanged):** 219 scored.

**Reports were database-wide and had to be fixed before they could be
trusted.** The first draft of the run 2 report showed 8,013 discovered and 782
enriched next to run 2's own results, which credits run 2 with everything run
1 had found. `storage.list_ranked_candidates` and
`list_all_discovery_queries` now accept an optional `run_id` and scope by it;
`gather_report_data` and `write_report` take the same parameter; the CLI's
`report --run-id` flag now actually does what its name says. A labelled
"Cumulative project state (all runs)" section still shows the project-wide
totals, explicitly marked as not the run's own numbers. Run 1's committed
outputs were never touched by this and remain byte-identical throughout.

**Maintenance-evidence asymmetry, found and partially closed.** Every
genuinely new run-2 candidate had `maintenance_burden` unknown, because
phase 14's pass was bounded to run 1's top candidates and no run-2 candidate
had ever been offered to it - not a level comparison, since the dimension
carries 15 percent of the weight. An approved bounded pass enriched the top 50
run-2 scored candidates (deterministic: `final_score DESC, candidate_id ASC`;
23 reused, 27 collected), taking unknown-in-top-50 from 27 to 1. 49 of the top
50 ranks moved as a result. The report states plainly that score movement from
filling a previously-unknown dimension is not evidence the model improved -
it removes a comparability problem, nothing more - and that 167 of 219 scored
candidates remain un-enriched.

**Example/tutorial signal audited, not changed.** Fired on 69 of 500 (13.8%).
Manual review of 10 flagged true found 1 correctly flagged, 4 likely
over-flagged, 5 unclear; 0 of 10 flagged false looked missed. The signal
matches a README that *contains* an examples/quick-start heading, which mature
products routinely carry, rather than a repository that *is* an example. It
remains evidence-only: nothing in qualification or scoring reads it.

**Final-model limitation, recorded rather than patched:** the enriched top of
run 2 concentrates AI/RAG document-processing platforms (`argus`, `dynamiq`,
`Upsonic`, `LARS`, `appl-docchat`, `camel_forward`) - several of them also
flagged by the example/tutorial signal. Their evidence is genuine: real
multi-library document code with visible custom glue, which is exactly what
the maintenance rubric is built to reward. The MVP identifies
engineering-intensive document workflows and, by that same measure, surfaces
AI/RAG document-processing platforms; it does not yet distinguish all such
systems from customer-facing document workflows with high commercial
leverage, which is the actual business target. This is a scope limitation of
the current dimensions, not a bug, and was not addressed this phase.

**Verification:** 984 tests pass (was 959; +25), 0 network connection
attempts, `integrity_check: ok`, 0 rejected candidates holding a score row, 0
secrets in outputs or database, run 1 outputs confirmed byte-identical to the
committed artifacts throughout every step of this phase.

Not committed until reviewed. Phase 16 not started.
