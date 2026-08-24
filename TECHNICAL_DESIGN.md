# Dependency Map Technical Design

## 1. Architecture decision

Three shapes were on the table: a simple script/pipeline, a backend application, or a CLI paired with a local database and a reporting step.

A backend application is the wrong shape here, and it's worth saying plainly why rather than just picking something else. The task document is explicit that the assigned build can be completed without a backend, and that a small thing that genuinely runs beats a bigger one that doesn't. Nothing about this system needs to run continuously, serve concurrent users, or expose a live API. The one and only consumer of this system is the person running it, on demand, to produce a ranked table. Building a backend would mean adding authentication, request handling, and deployment concerns that exist to serve users this system doesn't have.

Between a plain script and a CLI-plus-database, the requirements already gathered in the earlier documents settle it. The fresh-batch requirement from search-strategy.md needs a persistent record of what earlier runs already found, so Run 2 can genuinely avoid replaying Run 1. The candidate schema has roughly forty fields per candidate, several of them repeated lists (dependencies found, evidence trail entries). Qualification and scoring need to be rerunnable on already-discovered candidates without re-spending GitHub's rate-limited API budget. All three of those needs are exactly what a small local database buys, versus reinventing persistence by hand with JSON files and hoping nothing gets corrupted mid-write.

**Decision: a Python CLI orchestrating a pipeline, backed by a local SQLite database, exporting to CSV and Markdown.** This is option C. It satisfies the brief's own preference (no backend, no server, something that runs on a laptop and produces files that go straight into the submission), and it gives the pipeline real resumability and a real query surface for building the report, for close to the implementation cost of a plain script.

```
Python
   -> CLI / pipeline
   -> GitHub / Libraries.io / deps.dev APIs
   -> SQLite (source of truth)
   -> CSV + Markdown report (generated from SQLite, not held separately)
```

## 2. System overview, data flow, and component map

```
library-universe.md (data/library-universe.yaml)
        |
        v
  Discovery engine  --calls-->  GitHub client / Libraries.io client / deps.dev client
        |
        v
  raw hits --> Deduplication (candidate_id) --> candidates table
        |
        v
  Evidence collector  --calls-->  GitHub client (files, README, metadata)
        |
        v
  Qualification engine  (no API calls, reads stored fields)
        |
        v
  Scoring engine  (no API calls, keep/investigate only)
        |
        v
  Report generator  -->  ranked-candidates.csv + dependency-map-report.md
```

Twelve components do the actual work, each with one job:

| Component | Responsibility |
|---|---|
| Config system | Loads settings, secrets from environment, scoring weights, gate thresholds |
| Library universe loader | Turns the library universe into query-generation input |
| GitHub / Libraries.io / deps.dev clients | One thin wrapper per external API, handles auth and defers to the reliability layer |
| Discovery engine | Runs the query set, records raw hits, doesn't judge anything |
| Deduplication | Maps every hit to a stable candidate_id, tracks what's already been seen |
| Evidence collector | Fills in candidate-schema.md's dependency, pipeline, and business evidence fields |
| Qualification engine | Applies keep / investigate / reject rules from stored evidence, no new API calls |
| Scoring engine | Applies scoring-model.md's rubrics, weights, and gate, no new API calls |
| Run manager | Orchestrates the stages, tracks runs, makes resumability automatic |
| Report generator | Produces the ranked CSV and the Markdown report |
| Tests | Cover all of the above; see section 18 |

Sections 4 through 13 below correspond one-to-one with this table, so each can turn directly into an implementation task without further design work.

## 3. Data storage design

SQLite, one file, no server. The schema mirrors candidate-schema.md closely enough that reading one explains the other:

- **runs**: `run_id` (PK), `started_at`, `finished_at`, `notes`. One row per discovery run, this is what makes the fresh-batch requirement enforceable.
- **candidates**: `candidate_id` (PK), `repo_url`, `repo_owner`, `repo_name`, `is_fork`, `is_archived`, `primary_language`, `company_name`, `company_name_source`, `product_name`, `website_url`, `industry_category`, `first_seen_run_id` (FK). One row per unique repository, ever, across all runs.
- **discovery_queries**: `query_id` (PK), `run_id` (FK), `discovery_source`, `library_name`, `discovery_tier`, `query`, `total_count`, `capped`, `search_window`, `returned_count`, `executed_at`. One row per query execution, whether or not it returned anything. This exists because a query is an entity in its own right: it has a total match count and a coverage limitation that belong to the query, not to any candidate it happened to surface, and a query that returns nothing still needs to be on the record. `query_id` is derived from `run_id`, `query` and `search_window`, so re-running a slice within a run updates rather than duplicates, which is what makes the stage resumable. `capped` means `total_count` exceeded GitHub's 1,000-result pagination ceiling, not that 1,000 results were retrieved.
- **discovery_evidence**: `id` (PK), `query_id` (FK), `candidate_id` (FK), `discovery_result_rank`. One row per candidate surfaced by a query. A candidate can have several rows here, once per query or run that surfaced it, which is itself the mechanism dedup and fresh-batch tracking read from. Deliberately narrow: everything about the query is reached through `query_id` rather than repeated on every hit, so there is one source of truth for what a query was and what it covered.
- **dependencies_found**: `id` (PK), `candidate_id` (FK), `library_name`, `library_category`, `direction`, `manifest_file`, `detection_method`, `evidence_url`.
- **pipeline_evidence**: `candidate_id` (PK/FK), plus the six pipeline fields from candidate-schema.md section 5. One row per candidate.
- **business_evidence**: `candidate_id` (PK/FK), plus the nine business fields from section 6. One row per candidate.
- **qualification**: `candidate_id` (PK/FK), `qualification_status`, `qualification_reason`, `rejection_reason`, `confidence`.
- **scores**: `candidate_id` (PK/FK), the seven dimension scores, `raw_weighted_score`, `final_score`, `confidence_band`, `gate_cap_applied`, `unknown_dimensions`. Only candidates that clear qualification ever get a row here at all, matching the "no misleading zero" rule from scoring-model.md. `gate_cap_applied` is nullable and constrained to 0 through 100 rather than to the specific caps scoring-model.md currently specifies: the caps live in `weights.yaml` precisely so a person can retune them, and a database that hardcoded today's values would reject tomorrow's. Which cap applies is the scoring engine's decision, not the schema's.
- **evidence_trail**: `id` (PK), `candidate_id` (FK), `evidence_url`, `evidence_type`, `evidence_excerpt`, `source`, `collected_at`. The full audit list.
- **api_cache**: `cache_key` (PK), `response_json`, `fetched_at`. See section 14.

This is close to a direct table-per-section mapping of candidate-schema.md, which is deliberate, anyone reading the schema doc should be able to guess the database schema without needing this section spelled out.

## 4. Config system

A `config.yaml` for non-secret settings (output paths, pacing parameters, cache TTL, library universe path) and a separate `weights.yaml` holding the scoring weights and gate thresholds from scoring-model.md as data, not hardcoded constants, so they can be tuned without touching code once real candidates come in and the open questions in scoring-model.md section 17 get revisited. Secrets (GitHub token, Libraries.io key) come from environment variables only, loaded via `.env` locally; see section 19. Every config value can be overridden by a CLI flag for one-off runs.

## 5. Library universe loader

Reads a structured `data/library-universe.yaml`, a machine-readable sibling to library-universe.md, into a list of `{library_name, ecosystem, category, direction, manifest_filenames}` entries that feed query generation. library-universe.md stays the human-readable source of truth for the reasoning behind each entry; the YAML is what code actually consumes. Keeping these in sync is a manual step for now, flagged in section 24.

## 6. External API clients

One class per source, each responsible only for authentication, shaping requests, and returning typed results, with all pacing, retry, and caching behavior delegated to the shared reliability layer in section 14 rather than duplicated per client:

- **GitHubClient**: code search, repository search, repository metadata, file contents, and (later, see section 22) dependents-page fetching.
- **LibrariesIOClient**: `dependent_repositories` and package info lookups.
- **DepsDevClient**: package metadata and dependency graph lookups, used to cross-check Libraries.io rather than originate discovery.

## 7. Discovery engine

For each entry from the library universe loader, generates the query set following the patterns in search-strategy.md section 4, calls the relevant client, writes a `discovery_queries` row for the execution and a `discovery_evidence` row per hit, creating a new `candidates` row only when the repo hasn't been seen before (see section 8). The discovery engine deliberately makes no judgment calls, it records hits, nothing more.

**Tiered generation.** Queries are generated in three tiers ordered by measured precision, not by library popularity. Tier 1 is infrastructure: tools like Gotenberg that appear in a Dockerfile or compose file rather than a manifest, because they are deployed services and so imply real engineering investment. Tier 2 is template generation: libraries whose purpose is filling a template from data, so their presence implies a pipeline. Tier 3 is broad manifest search, which is where most usage lives but also where nearly all the noise is. The tier for each entry is read from `discovery_tier` in `data/library-universe.yaml`, which keeps tier membership as reviewable data rather than a second library list embedded in code. It is independent of `library_category`, because how precise a query is and what kind of library it targets are different questions.

**Slicing.** GitHub returns at most 1,000 results per query however it is paginated, and the controlled experiment behind this design found six of eight trial queries over that ceiling. Every tier-3 query is therefore generated as a set of sliced queries, most often by date window, and the slice applied is stored in `search_window`. Tier 1 needs no slicing, having been measured comfortably under the ceiling. The same slicing machinery is what rotates run 2 away from run 1, so the fresh-batch requirement in section 8 is satisfied by a mechanism that already had to exist rather than by a second one built alongside it.

**Compose filenames.** Infrastructure queries must cover both `docker-compose.yml` and `docker-compose.yaml`. This is handled in query generation rather than by duplicating a library-universe entry per extension. GitHub's `filename:` qualifier also matches by prefix, so near-miss filenames come back and are recorded like any other hit; filtering them is qualification's job, not discovery's.

## 8. Deduplication and fresh-batch tracking

`candidate_id` is a deterministic hash of the normalized `repo_url` (lowercased, trailing slash stripped), so the same repository always resolves to the same row no matter which query or run found it. Before writing a candidate, the discovery engine checks whether that `candidate_id` already exists; if it does, it adds a new `discovery_evidence` row rather than a duplicate candidate.

Fresh-batch tracking builds on the same table: before a new run starts, it loads every `candidate_id` already present in `discovery_evidence` and passes that set to the query generator, which rotates at least one query parameter per search-strategy.md section 7 (date filters, page offsets, which library subset leads the search). A hit matching an already-seen `candidate_id` still gets logged (it's useful to know a query surfaced the same repo again), but it doesn't count toward that run's "new candidates found" total.

## 9. Evidence collector

For every candidate with a `discovery_evidence` row but no `pipeline_evidence` or `business_evidence` row yet, this component fetches the referenced manifest file, a sample of code around each dependency hit, the README, and repository metadata (stars, forks, last commit, contributor count, fork and archive status), then populates `dependencies_found`, `pipeline_evidence`, `business_evidence`, and `evidence_trail` exactly as defined in candidate-schema.md. This is the most API-call-heavy component in the system, and the one leaning hardest on the caching and pacing described in section 14.

## 10. Qualification engine

A pure function: no network calls, only reads what's already stored. Applies the keep / investigate / reject rules from search-strategy.md section 5, made concrete through the observable field checks candidate-schema.md section 6 defines (`readme_describes_product` AND `application_code_exists` AND NOT `is_fork`, and so on), and writes `qualification_status`, a `qualification_reason` built from the actual field values that justified it (not a general summary, per the schema's own requirement), `rejection_reason`, and `confidence`. Being a pure function over stored data means it can be rerun on its own whenever the rules themselves get refined, without touching the API budget at all.

## 11. Scoring engine

Also a pure function. For every candidate with `qualification_status` in keep or investigate, computes the seven dimension scores against the rubrics in scoring-model.md sections 3 through 9, reading the relevant stored fields for each; applies the weights loaded from `weights.yaml`; computes `raw_weighted_score` and `final_score`; applies the gate caps from scoring-model.md section 14; and computes the confidence band from section 13. Rejected candidates never get a row in `scores` at all, matching the architecture decision that a rejection should exclude a candidate from ranking entirely rather than produce a misleadingly low number.

## 12. Run manager

The orchestrator, exposed as the `run` CLI command. It creates a new row in `runs`, then calls discovery, evidence collection, qualification, and scoring in sequence, with each stage processing only the candidates that are actually missing that stage's output. That single design choice is what makes resumability automatic rather than a separate feature, see section 16. A `--stage` flag lets any one stage run in isolation, useful for debugging and for the human-in-the-loop checkpoints in section 17.

## 13. Report generator

Joins `candidates`, `qualification`, and `scores`, filters to keep/investigate rows with a non-null `final_score`, sorts descending, and produces two outputs: `ranked-candidates.csv` (one row per candidate, every schema field flattened, for spreadsheet use) and `dependency-map-report.md` (the ranked table plus, per candidate, its evidence trail and qualification reasoning inline). The Markdown report is the actual "query method" artifact the task brief asks for, not just a bare list of repository names, it should be readable on its own without needing the database open next to it.

## 14. API reliability: request pacing, retries, exponential backoff, caching

**Request pacing.** GitHub code search is capped at 10 requests per minute even when authenticated, confirmed while researching search-strategy.md. The GitHub client enforces a minimum spacing between code-search calls specifically (targeting roughly one call every 6 to 7 seconds, safely under the cap), with a separate, looser budget for the general REST API's higher hourly limit. Libraries.io and deps.dev get their own, more generous pacing, but still rate-limited defensively rather than assumed unlimited.

**Retries.** Transient failures (HTTP 5xx responses, connection resets, timeouts) get retried up to a small fixed number of attempts (three) before that specific call is marked failed and logged, never silently dropped.

**Exponential backoff.** Retry delay doubles from a base of about 2 seconds, with a small random jitter added so that if several calls fail at once they don't all retry in lockstep. GitHub's secondary rate limit errors, distinct from the primary 10/minute cap, specifically call for backing off rather than retrying immediately, and the client treats them accordingly.

**Caching.** Every raw API response is written into the `api_cache` table, keyed by a hash of the request URL and parameters, before it's parsed into anything else. Every client checks the cache first; a configurable TTL (a generous default of about 7 days, since repository metadata doesn't change hour to hour) decides whether a cached response is still usable. This means a crashed or rerun pipeline never re-spends rate-limit budget re-fetching something it already successfully retrieved, and it means local development and the test suite can run entirely against a seeded cache without touching real APIs at all.

## 15. Error handling and partial failure strategy

Two kinds of failure are handled differently. A single call failing after retries are exhausted marks just that piece of evidence as missing for that candidate, feeding directly into the "unknown scores as 0" rule from scoring-model.md, and the pipeline moves on to the next candidate rather than aborting. A systemic failure (an invalid token, a rate limit exhausted for the day) stops the run entirely instead of burning through the remaining candidates producing nothing but unknowns. The run manager tells these apart by error type and HTTP status, and every failure is logged with enough context (candidate_id, stage, which call, the error) that it can be retried on its own later rather than requiring a full rerun.

## 16. Checkpointing / resumability

**What gets saved:** everything, continuously, because the database is the working state, not an end-of-run export. Each candidate's progress through each stage is committed to SQLite as it completes, not held in memory and flushed at the end. If the process crashes partway through evidence collection for candidate 47 of 200, candidates 1 through 46 already have their evidence rows safely committed.

**How the next run resumes:** each stage queries for candidates missing that stage's output, rather than being handed an explicit "resume from here" pointer. The evidence collector processes candidates that have discovery evidence but no pipeline or business evidence; the qualification engine processes candidates with evidence but no qualification row; the scoring engine processes qualified-but-unscored candidates. Simply rerunning `run` (or `run --stage evidence`) picks up exactly where things left off. Resumability falls out of the "process what's missing" design rather than being a separate feature that has to be built and kept in sync.

**How expensive API calls are avoided on resume:** the `api_cache` from section 14 means that even a candidate whose evidence collection crashed halfway through won't force a full re-fetch. If its README fetch succeeded and was cached before the crash, resuming reuses that cached response; only the specific pieces that never completed get retried.

## 17. Human-in-the-loop

Some decisions should stay manual rather than pretend to be reliably automatable:

- Final keep-versus-reject calls on borderline "investigate" candidates, especially where confidence is low. The qualification engine should propose a status and a reason, not quietly decide and hide that it was a close call.
- Resolving a company name when it isn't stated cleanly anywhere in the repository. `company_name_source = external_search` should mean a person actually went and looked, not that the system guessed and moved on.
- Any actual outreach or contact. This is explicitly out of scope per the task brief's own rules (SuperDocs does all outreach itself), so this system has no send capability of any kind, not even a draft-and-hold one.
- Tuning the scoring weights and gate thresholds. The current numbers, from scoring-model.md, are reasoned first guesses, not calibrated against outcomes, since there aren't any yet. They should be adjusted by a person reviewing real output, not auto-tuned against some proxy metric.
- Reviewing the investigate bucket specifically. Qualification is deliberately conservative, and a healthy investigate pile is expected, not a failure. Someone should skim it rather than have the system silently promote or demote those candidates on its own.

## 18. Testing strategy

**Unit tests.** Qualification rules (given a candidate record with specific field values, does it return the expected status and reason). Scoring rubrics and the final formula (given dimension inputs, does `final_score` match a hand-calculated expected value, including gate caps and the unknown-as-zero rule). The library universe loader (parses the expected entries). Config loading. `candidate_id` hashing (the same `repo_url` always produces the same id, including under case and trailing-slash variation).

**Integration tests.** The discovery engine against a recorded/mocked GitHub API response, never live calls in CI. The evidence collector building a full candidate record end to end from mocked responses, checked field by field against candidate-schema.md. The report generator producing correct CSV and Markdown output from a small, seeded SQLite database.

**Scoring tests.** The three synthetic examples from scoring-model.md section 15 (MedReport Solutions, EstateProposal, docutils-sandbox) become literal test fixtures. Their `final_score` and confidence band are asserted against the hand-worked math in that document, and it's asserted that docutils-sandbox never produces a row in `scores` at all.

**Qualification tests.** A fixture for each `rejection_reason` enum value, confirming each correctly maps to reject. Fixtures for a clean keep and a genuinely ambiguous investigate case.

**Deduplication tests.** The same `repo_url` fed through discovery twice, in the same run and across two separate runs, asserting exactly one row in `candidates` and two rows in `discovery_evidence`.

**Fresh-batch tests.** Simulated Run 1 and Run 2 with deliberately overlapping query results, asserting Run 2's "new candidates found" count excludes anything already present in Run 1's `discovery_evidence`.

## 19. Security

- GitHub token and Libraries.io key are read from environment variables only, never written into `config.yaml` or any file that could end up committed. A `.env.example` documents the required variable names with no values; `.env` itself is gitignored.
- The GitHub token uses the minimum scope needed, public read access, no write scopes at all, since this system never modifies anything on GitHub.
- Logs never include full API response bodies at default verbosity, and any string matching a token-like pattern gets scrubbed before being written to a log line, as a defense-in-depth measure even though tokens shouldn't appear in response bodies to begin with.
- A simple pre-commit check scans for common secret patterns before any commit goes through.
- Raw environment variable values never get written into the SQLite database or into any exported CSV or Markdown report, only application data goes into outputs.
- The `api_cache` table stores raw API responses, which is a second place a secret could theoretically leak if a response ever echoed something sensitive back. The database file itself is treated the same way as `.env`, not committed, not shared outside the local machine.

## 20. Project structure

```
dependency-map/
|-- README.md
|-- .env.example
|-- .gitignore
|-- pyproject.toml
|-- config/
|   |-- config.yaml
|   `-- weights.yaml
|-- data/
|   |-- library-universe.yaml
|   `-- dependency_map.db          (gitignored, generated)
|-- src/
|   `-- dependency_map/
|       |-- __init__.py
|       |-- cli.py
|       |-- config.py
|       |-- models.py              (dataclasses mirroring candidate-schema.md)
|       |-- db.py                  (SQLite connection + schema setup)
|       |-- library_universe.py
|       |-- clients/
|       |   |-- github_client.py
|       |   |-- libraries_io_client.py
|       |   `-- deps_dev_client.py
|       |-- reliability.py         (pacing, retry, backoff, cache helpers)
|       |-- discovery.py
|       |-- dedup.py
|       |-- evidence.py
|       |-- qualification.py
|       |-- scoring.py
|       |-- run_manager.py
|       `-- report.py
|-- tests/
|   |-- fixtures/
|   |   `-- synthetic_candidates.py   (the 3 scoring-model.md examples)
|   |-- test_qualification.py
|   |-- test_scoring.py
|   |-- test_dedup.py
|   |-- test_fresh_batch.py
|   |-- test_library_universe.py
|   `-- test_report.py
`-- outputs/
    |-- ranked-candidates.csv
    `-- dependency-map-report.md
```

## 21. Technology choice

- **Language: Python.** Every API this system touches has mature Python tooling, and routing implementation through Claude Code specifically favors a widely used, well-documented stack, since that minimizes the gap between this design document and working code.
- **HTTP: `requests`.** No need for async given GitHub's 10/minute code-search cap makes parallelizing those specific calls pointless; `requests` is simpler and sufficient.
- **CLI: `click`.** Cleaner subcommand ergonomics than raw `argparse` for something with multiple stages (`dependency-map run`, `dependency-map run --stage evidence`, `dependency-map report`).
- **Storage: SQLite via the standard library `sqlite3` module.** One file, no server to run, ships with Python, directly inspectable with any SQLite browser while debugging, and matches the scale of this problem. An ORM isn't needed yet, plain SQL keeps the schema transparent and easy to reason about; this can be revisited if the schema grows a lot later.
- **Config: `pyyaml`** for `config.yaml` and `weights.yaml`, **`python-dotenv`** for loading `.env` locally.
- **Testing: `pytest`.** The standard choice, with fixture support that fits naturally with the synthetic candidate fixtures described in section 18.
- **Output: the standard library `csv` module**, plus plain string templating for the Markdown report (upgrading to `jinja2` only if the report's formatting needs grow past what plain templates handle comfortably).

## 22. MVP vs later improvements

### MVP

What has to exist for the first working run: the config system with environment-variable secret loading; a library universe loader (a manually transcribed structured list is fine to start, it doesn't need to auto-parse library-universe.md yet); a GitHub client covering code search, repository metadata, and file contents; a Libraries.io client for `dependent_repositories`; a discovery engine running the tiered, sliced query set from search-strategy.md section 4, excluding the bare code-import queries that section 4.4 records as tested and set aside; deduplication by `candidate_id`; an evidence collector populating identity, dependency evidence, and the parts of pipeline and business evidence that don't require commit history; the qualification engine; the scoring engine, with `maintenance_burden` defaulting to unknown for every candidate at first (commit-history pulling is deferred, matching the open question already flagged in scoring-model.md); a run manager with the query-what's-missing resumability pattern; a report generator producing both outputs; basic pacing and caching (even a simple sleep plus a cache check is enough to start); and unit tests for qualification and scoring.

### Later

deps.dev cross-checking, once the primary pipeline is proven. Sourcegraph as a secondary code-search source. Parsing the GitHub dependents page directly, rather than relying on Libraries.io to cover similar ground. Pulling commit history to make `maintenance_burden` a real, evidenced dimension instead of a structural unknown. Auto-generating `library-universe.yaml` from library-universe.md instead of maintaining both by hand. Revisiting the scoring weights and gate thresholds once real output exists to review. A `qualification_history` table for tracking re-evaluations over time. Parallelizing the calls that aren't as tightly rate-limited as GitHub code search (Libraries.io, deps.dev). Any kind of dashboard or interactive UI, deliberately last on the list, since the brief itself asks for a ranked table and a query method, not a polished interface.

## 23. Known limitations

- GitHub-only for code search in v1. GitLab and Bitbucket repositories are out of scope, a gap already noted in search-strategy.md.
- Commercial SDKs used without appearing on a public package registry (Aspose, Spire.Office) will likely be under-discovered, since neither Libraries.io nor deps.dev tracks that kind of usage the way they track open-source dependencies.
- `maintenance_burden` will be unknown for nearly every candidate at launch, since commit-history pulling is deferred to a later phase, which means that dimension's 15% weight is effectively dormant at first. This is a known, accepted gap, not an oversight.
- Company name identification is best-effort and often stays null. The system doesn't search external sources (LinkedIn, Crunchbase, or anything beyond what's linked in the repo itself) to resolve an identity; that's explicitly left to a human.
- GitHub's 1,000-result cap per search query means broad, single-term queries will under-count true usage until the query set is sliced further than what's specified in search-strategy.md section 4 today. V1 ships with that known undercount rather than blocking on a full query-slicing system first.
- The scoring weights and gate thresholds are reasoned first guesses, not calibrated against any real outcome data, because none exists yet.

## 24. Open questions

- Should the library universe loader eventually parse library-universe.md directly, avoiding duplication but adding fragility, or keep a separate structured YAML that's synced by hand, simpler but prone to drift? MVP leans toward the manual YAML; worth revisiting once the universe stabilizes and stops changing often.
- Should evidence collection and qualification stay as fully separate stages, as designed, or run as one combined pass per candidate? Separate stages make resumability and independent reruns cleaner, but leave a window where a candidate's evidence could go stale relative to the live repository between collection and qualification. Worth deciding whether that gap matters for something that runs occasionally rather than continuously.
- How should the system treat a repository that GitHub simply hasn't indexed for code search yet, since very new repositories can lag behind? There's no current strategy for distinguishing "not indexed yet, try again later" from "genuinely doesn't exist," and it's not obvious that distinction is even visible from the API responses.
- Is SQLite still the right choice if this ever needs to run on a schedule from an ephemeral environment like a GitHub Action, where the database file would need to persist across runs somehow (committed, stored as an artifact, or moved to something like Postgres)? Not a concern for a single local run, worth flagging before this becomes a recurring job.
- Should the cache support a way to force-refresh a single candidate without clearing the whole `api_cache`, useful when someone wants to double-check one specific candidate with genuinely current data during a closer review?
