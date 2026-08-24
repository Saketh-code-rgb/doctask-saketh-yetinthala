# Dependency Map Implementation Plan

## Phase 1 — Repository bootstrap

Tasks:
1. Initialize the git repository and directory structure from technical-design.md section 20
2. Create `pyproject.toml` with the dependencies from technical-design.md section 21 (requests, click, pyyaml, python-dotenv, pytest)
3. Create `.gitignore` (covers `.env`, `data/dependency_map.db`, `__pycache__`, standard Python ignores)
4. Create `.env.example` documenting `GITHUB_TOKEN` and `LIBRARIES_IO_API_KEY` with no values
5. Create `README.md` stub describing what the project does and how to run it
6. Create `TASK.md` describing how to work with this repository (per the SuperDocs task's own suggested working method)
7. Create `PROGRESS.md` with an empty log structure ready for entries
8. Confirm `python -m dependency_map --help` (or equivalent) runs and exits cleanly, even with no real commands yet

Definition of done: the repository exists, installs cleanly (`pip install -e .`), and a placeholder CLI command runs without error.

## Phase 2 — Storage layer

Tasks:
1. Create a SQLite connection helper (context-managed, path read from config, one shared connection pattern)
2. Create schema initialization covering all ten tables from technical-design.md section 3 (`runs`, `candidates`, `discovery_evidence`, `dependencies_found`, `pipeline_evidence`, `business_evidence`, `qualification`, `scores`, `evidence_trail`, `api_cache`)
3. Create a schema-version table and a startup check that fails loudly if the database's schema version doesn't match what the code expects, rather than full migration tooling
4. Add candidate CRUD: insert-if-new (keyed on `candidate_id`), get-by-id, get-by-repo-url
5. Add `runs` and `discovery_evidence` persistence: create a run, insert a discovery hit, list every `candidate_id` associated with a given run
6. Add `dependencies_found` persistence (insert, list-by-candidate)
7. Add `pipeline_evidence` and `business_evidence` persistence (one row per candidate, upsert)
8. Add `qualification` persistence
9. Add `scores` persistence, including a field for `unknown_dimensions` (a list of which of the seven dimensions defaulted to 0 for this candidate), a small addition to the schema in technical-design.md made specifically so the report generator in Phase 11 can show unknown dimensions honestly instead of a bare number
10. Add `evidence_trail` and `api_cache` persistence
11. Unit tests for every operation above, run against an in-memory or temp-file SQLite database, never the real one

Definition of done: every table from the schema has working CRUD covered by a passing test, and the schema-version check correctly refuses to run against a mismatched database file.

**Human checkpoint.** Stop here and confirm the schema itself, especially the `unknown_dimensions` addition, matches intent before anything gets built on top of it.

## Phase 3 — Config system

Tasks:
1. Create `config.yaml` and `weights.yaml` per technical-design.md sections 4 and 20, with the exact weights from scoring-model.md section 10 and the gate thresholds from section 14
2. Create a config-loading module that reads both YAML files plus `.env`, with environment variables taking priority for secrets specifically
3. Add CLI flag overrides for the settings most likely to change per run (output paths, cache TTL)
4. Add validation: refuse to start if `GITHUB_TOKEN` is missing, and if `weights.yaml`'s dimension weights don't sum to 1.0 (a direct, automatic check against the requirement in scoring-model.md section 10)
5. Unit tests for config loading, override precedence, and the weight-sum validation

Definition of done: config loads correctly from files and environment, secrets never come from the YAML files, and a deliberately broken `weights.yaml` (weights not summing to 1.0) fails loudly at startup rather than silently producing wrong scores later.

## Phase 4 — Library universe loader

Tasks:
1. Transcribe library-universe.md's five tables into a structured `data/library-universe.yaml`, one entry per library with `library_name`, `ecosystem`, `category`, `direction`, and `manifest_filenames`
2. Build the loader module that reads this YAML into the in-memory structure the discovery engine will consume
3. Add a helper that, for a given library entry, returns the manifest filenames and any infrastructure-reference patterns relevant to it (the Pandoc/Gotenberg/LibreOffice special case from search-strategy.md section 2, where the signal lives in a Dockerfile rather than a manifest)
4. Unit tests confirming every entry from library-universe.md is present and correctly categorized in the loaded structure

Definition of done: loading the library universe returns the expected number of entries with correct categories and directions, verified against library-universe.md by a test that checks specific known entries (python-docx, docxtemplater, Gotenberg) by name.

## Phase 5 — Reliability layer and API clients

Tasks:
1. Build the reliability layer first, since every client depends on it: request pacing (a simple rate limiter targeting GitHub's 10/minute code-search cap), retry-with-exponential-backoff-and-jitter, and the cache-check-before-call wrapper against the `api_cache` table
2. Build `GitHubClient` with methods for code search, repository search, repository metadata, and file contents, each routed through the reliability layer
3. Build `LibrariesIOClient` with a method for `dependent_repositories` and basic package info lookup
4. Wire both clients to write every raw response into `api_cache` before parsing, keyed by a hash of the request
5. Unit tests for the reliability layer using a fake, controllable HTTP client (forcing timeouts, 5xx responses, and secondary-rate-limit responses to confirm backoff behaves correctly)
6. Unit tests for both API clients against recorded/mocked responses, never live calls

Definition of done: the reliability layer's retry and backoff behavior is verified with deliberately-failing fake responses, both clients return correctly typed results from mocked data, and every client call writes to `api_cache` before returning.

## Phase 6 — Discovery engine

This phase was redesigned after a controlled real-API experiment (Phase 6A, run 2026-08-20) measured what the query set in search-strategy.md section 4 actually returns. The tiering, the slicing requirement and the query-level persistence below all come from that measurement rather than from reasoning. The full results are in PROGRESS.md.

### Schema version 2, before anything else

The schema changes first, because the discovery engine writes into tables that don't exist yet at version 1 and there is no point building on a schema that's about to move.

1. Add the `discovery_queries` table from technical-design.md section 3: `query_id` (PK, derived from `run_id`, `query` and `search_window` so a re-run slice resolves to the same row), `run_id` (FK), `discovery_source`, `library_name` (nullable, since co-occurrence queries span several), `discovery_tier`, `query`, `total_count`, `capped`, `search_window` (nullable, where null means unsliced rather than unknown), `returned_count`, `executed_at`
2. Rewrite `discovery_evidence` down to `id`, `query_id` (FK), `candidate_id` (FK), `discovery_result_rank`. Drop `run_id`, `discovery_source`, `discovery_query` and `discovered_at`: all four are properties of the query, now reachable through `query_id`, and keeping copies on every hit would recreate exactly the duplicate-source-of-truth problem this change removes
3. Replace the `scores.gate_cap_applied` constraint, which hardcodes today's caps as `IN (20, 25, 40)`, with a nullable 0-to-100 range. The caps live in `weights.yaml` so a person can retune them; a database that only accepts the current three would reject a retuned cap and make the configurability a fiction. Which cap applies stays the scoring engine's decision in Phase 10, not the schema's
4. Bump `SCHEMA_VERSION` from 1 to 2. No migration is needed or written: no database file exists yet, and the version check is there to refuse a mismatch loudly rather than to repair one
5. Update `db.py` and `storage.py` for the new and changed tables, including CRUD for `discovery_queries`
6. Update the Phase 2 tests to match. Several `discovery_evidence` tests reference columns that no longer exist, and one gate-cap test asserts that a cap of 33 is rejected, which version 2 deliberately allows. Leaving Phase 2's tests inconsistent with the approved schema is not acceptable; they are part of this task, not follow-up work

### Discovery engine

7. Add `discovery_tier` to every entry in `data/library-universe.yaml` and extend the library universe loader to accept and expose it. Tier membership is data, never a library list hardcoded in Python
8. Build the tiered query generator per search-strategy.md section 4: tier 1 infrastructure patterns, tier 2 template-generation manifests, tier 3 broad manifests. Generate both `docker-compose.yml` and `docker-compose.yaml` for compose-based infrastructure signals, in the generator rather than by duplicating library-universe entries
9. Implement slicing as part of generation, not as an afterthought. Every tier-3 query must carry a slice (date window, ecosystem narrowing where valid, or keyword narrowing), and the applied slice is recorded in `search_window`. Never generate a query combining `filename:requirements.txt` with `language:python`: search-strategy.md section 4.3 records that this returns zero results because GitHub does not classify a requirements file as Python
10. Do not generate bare code-import queries. Search-strategy.md section 4.4 records `import docx language:python` as tested and set aside at 690,176 measured results, unusable as a discovery primitive. The narrower goal it served is met by adding `filename:pyproject.toml` to tier-3 manifest queries
11. Build the discovery loop: for each generated query, call the appropriate client, write one `discovery_queries` row for the execution including `total_count`, `capped` and `returned_count`, and one `discovery_evidence` row per hit. A query that returns zero results still gets its row: the experiment found an invalid query precisely because a zero-result execution is itself a finding
12. Wire candidate creation into the discovery loop (new `candidates` row only if the repo hasn't been seen, see Phase 7 for the dedup logic itself)
13. Keep the co-occurrence query as a supplementary tier-3 probe. Search-strategy.md section 4.3 records it measuring 11,552 results with substantial noise, which does not support its earlier billing as the closest single-query proxy for the combined-libraries signal
14. Discovery makes no judgment calls. The four noise classes in search-strategy.md section 5 (library-adjacent tools, incidental AI and LLM usage, personal scripts, nested manifests) are inputs to qualification and must not become discovery filters
15. Integration test: run discovery against a small, fixed set of mocked API responses, and confirm the expected `discovery_queries` and `discovery_evidence` rows land in the database, including a query that returns zero candidates and still records its row

Definition of done: the database is at schema version 2 with all Phase 2 tests updated and passing; running discovery against mocked responses for a handful of library-universe entries produces the expected candidates, `discovery_queries` rows and `discovery_evidence` rows; every tier-3 query carries a recorded `search_window`; a zero-result query is persisted; and no live API calls are made during the test.

## Phase 7 — Deduplication and fresh-batch tracking

Tasks:
1. Implement `candidate_id` generation: a deterministic hash of the normalized `repo_url` (lowercased, trailing slash stripped)
2. Implement the seen-check: before inserting a candidate, look up whether its `candidate_id` already exists, and if so, add a `discovery_evidence` row instead of a duplicate candidate
3. Implement fresh-batch query rotation: before a new run starts, load every `candidate_id` already in `discovery_evidence`, and rotate at least one query parameter (date filter, page offset, or which library subset leads) per search-strategy.md section 7
4. Implement the "new candidates found" count for a run, explicitly excluding anything already present in a prior run's `discovery_evidence`
5. Deduplication unit tests: the same `repo_url` fed through discovery twice, in the same run and across two separate runs, asserting exactly one `candidates` row and two `discovery_evidence` rows
6. Fresh-batch unit tests: simulated Run 1 and Run 2 with deliberately overlapping results, asserting Run 2's new-candidate count excludes anything already in Run 1's `discovery_evidence`

Definition of done: the dedup and fresh-batch tests from technical-design.md section 18 pass, using synthetic overlapping fixtures, not live data yet.

## Phase 8 — Evidence collector and run manager

Tasks:
1. Build the evidence collector: for each candidate with a `discovery_evidence` row but no `pipeline_evidence`/`business_evidence` row, fetch the manifest file, a sample of code around each dependency hit, the README, and repository metadata
2. Populate `dependencies_found`, `pipeline_evidence`, `business_evidence`, and `evidence_trail` exactly per the field definitions in candidate-schema.md sections 4 through 6 and 9
3. Build the run manager: creates a `runs` row, calls discovery then evidence collection in sequence, with each stage processing only candidates missing that stage's output
4. Add the `--stage` CLI flag so discovery and evidence collection can each run in isolation
5. Wire the CLI's `run` command end to end for these two stages (qualification and scoring get wired in Phases 9 and 10)
6. Integration test: full discovery-then-evidence-collection pass against mocked responses, checking every candidate-schema.md field lands correctly on a known fixture repo

Definition of done: running `dependency-map run --stage evidence` against mocked data produces fully populated evidence records matching candidate-schema.md, and rerunning it a second time makes no new API calls for candidates already completed (verified against the mock's call count, not just assumed).

**Human checkpoint.** Stop here and review actual evidence records pulled for a handful of real repositories (a small manual run against live APIs, not just mocks) before qualification and scoring get built on top of this data.

## Phase 9 — Qualification engine

Tasks:
1. Implement one predicate function per `rejection_reason` value from candidate-schema.md section 7 (`single_incidental_use`, `tutorial_or_demo`, `fork_of_library`, `archived_no_signal`, `personal_project_no_customers`), each reading only stored fields, no network calls
2. Implement the keep criteria check, requiring `readme_describes_product`, `application_code_exists`, and `is_fork = false` to hold together, per the rule established in candidate-schema.md section 6
3. Implement the investigate fallback for candidates that don't cleanly match keep or any reject predicate
4. Build the `qualification_reason` generator, which must cite the specific field values that drove the decision (for example "category_count=2, code_usage_confirmed=true"), not a general summary
5. Implement the qualification `confidence` field (high/medium/low, based on how much of the decision rests on directly observed fields)
6. Wire the qualification engine into the run manager as `--stage qualification`, processing candidates with evidence but no qualification row yet
7. Persist qualification results using Phase 2's CRUD
8. Unit tests: one fixture per `rejection_reason` value, one clean keep fixture, one genuinely ambiguous investigate fixture

Definition of done: qualification runs as a pure function with zero network calls; every candidate with evidence receives a status; every fixture in the test suite resolves to its expected status; rerunning qualification twice on identical evidence produces identical results.

## Phase 10 — Scoring engine

Tasks:
1. Load `weights.yaml` and the gate thresholds into the scoring engine
2. Implement each of the seven dimension rubric functions (document_volume, document_complexity, business_criticality, pipeline_complexity, maintenance_burden, build_vs_buy_signal, commercial_leverage) exactly per scoring-model.md sections 3 through 9, each returning an integer 0 through 5
3. Implement the unknown-as-0 rule, and track which dimensions were unknown into the `unknown_dimensions` field added in Phase 2, so nothing about the missing evidence gets hidden later
4. Implement `raw_weighted_score` and `final_score` per the formula in scoring-model.md section 11
5. Implement the three qualification gate caps from scoring-model.md section 14 (unconfirmed code usage, document code outside production paths, single-category with no infrastructure signal)
6. Implement `confidence_band` (high/medium/low) from scoring-model.md section 13, based on how many of the seven dimensions had real evidence rather than defaulting to unknown
7. Wire the scoring engine into the run manager as `--stage scoring`, processing keep/investigate candidates with no score row yet, and confirm reject candidates are never touched
8. Persist scores, including `unknown_dimensions` and `confidence_band`
9. Unit tests: the three synthetic candidates from scoring-model.md section 15 (MedReport Solutions, EstateProposal, docutils-sandbox) as literal fixtures, asserting `final_score` and `confidence_band` match the hand-worked math exactly, and asserting docutils-sandbox produces no row in `scores` at all

Definition of done: scoring runs as a pure function with zero network calls; the three synthetic fixtures reproduce scoring-model.md's math exactly, including the gate caps; every reject candidate has zero rows in `scores`; rerunning scoring twice on identical evidence is deterministic.

**Human checkpoint.** Stop here and manually verify `weights.yaml` and the gate thresholds match scoring-model.md precisely before this runs against real candidates. This is the most consequential logic in the system, and a typo here silently distorts every ranking that follows.

## Phase 11 — Report generator

Tasks:
- CSV: build `ranked-candidates.csv`, one row per keep/investigate candidate with a non-null `final_score`, every schema field flattened, sorted by `final_score` descending
- Markdown: build `dependency-map-report.md` with the ranked table at the top, then a per-candidate section including its evidence trail links and qualification reasoning
- For every candidate entry, explicitly render `Score: X/100`, `Confidence: [band]`, `Evidence coverage: N/7 dimensions`, and a plain line for each dimension listed in `unknown_dimensions` (for example `Maintenance burden: Unknown`), so the missing 15 percent from an unscored dimension is always visible and never silently folded into the number, per the explicit instruction not to normalize it away
- Add a short section documenting the exact discovery queries used, pulled from `discovery_evidence`, so the report itself satisfies the task brief's "query method" requirement rather than needing a separate document
- Wire `dependency-map report` as its own CLI command, runnable independently of `run`
- Unit tests: report generation against a small seeded database, checking CSV columns, Markdown structure, and specifically confirming that a candidate with an unknown dimension shows the explicit "Unknown" label rather than a bare `0`

Definition of done: running `dependency-map report` against a populated database produces both files; every candidate's entry visibly shows score, confidence, evidence coverage, and explicit unknown-dimension labels; reject candidates appear in neither output; the report includes the actual queries used.

## Phase 12 — Testing

Tasks:
1. Integration test: the full pipeline, discovery through report generation, against a small fixed library-universe subset and mocked API responses
2. Deduplication tests (if not already fully covered in Phase 7, extend to a multi-stage scenario spanning discovery through evidence collection)
3. Fresh-batch tests against a more realistic simulated Run 1/Run 2 overlap, not just the minimal fixture from Phase 7
4. Checkpointing/resumability test: interrupt a simulated run partway through (kill the process after N candidates complete a stage), rerun, and assert it resumes from where it stopped rather than reprocessing already-committed candidates, and that cached API responses aren't re-fetched
5. Security test: assert no environment variable value or token-like string ever appears in a generated CSV, Markdown report, or committed config file
6. Run the full test suite and confirm coverage across qualification, scoring, dedup, fresh-batch, checkpointing, and report generation

Definition of done: the full test suite passes; resumability is verified by an actual interrupt-and-resume test, not just asserted by design; the security test passes against deliberately-planted fake secrets in test fixtures to confirm the check actually catches something.

## Phase 13 — First real run

Tasks:
1. Confirm `.env` is populated with a real `GITHUB_TOKEN` and `LIBRARIES_IO_API_KEY` (human-provided, never committed)
2. Run `dependency-map run` for real, against the actual library universe and search-strategy.md query set, as `run_1`
3. Watch for rate-limit handling working correctly against real GitHub responses, not the mocked behavior from earlier phases
4. Run `dependency-map report` and read the actual output
5. Manually spot-check a handful of keep/investigate candidates against their real GitHub repositories, to sanity-check that qualification and scoring aren't producing something obviously wrong
6. Log any real-world surprises, bugs, or rough edges into `PROGRESS.md`, in the same blunt spirit the SuperDocs task brief itself asks for

Definition of done: a real `ranked-candidates.csv` and `dependency-map-report.md` exist, generated from live API data; several candidates have been manually checked against their actual GitHub source; `PROGRESS.md` documents what happened, including anything that broke.

**Human checkpoint.** Stop here. Do not proceed to Phase 14 without a human actually reading the real output first, since Phase 14's work depends on a person deciding which candidates are worth the deeper pass.

## Phase 14 — Review and improve

Tasks:
1. Human review of the full keep/investigate list from Phase 13, including the investigate bucket specifically, not just the top of the ranking
2. Select the top 10 to 15 candidates by `final_score` for a targeted maintenance-burden evidence pass
3. Build a narrow commit-history collection method using the GitHub commits API, filtered to paths touching the document-related files identified in each candidate's `dependencies_found`, scoped only to this selected set, not the full pipeline
4. Update `maintenance_burden` for just those candidates using real commit-history evidence in place of the unknown default
5. Recompute `raw_weighted_score`, `final_score`, `confidence_band`, and `unknown_dimensions` for just that subset
6. Regenerate the report so it clearly distinguishes which candidates received this enhanced pass from which are still running on the MVP default, rather than presenting all scores as equally evidenced
7. Review whether qualification rules or scoring weights need adjusting based on what real candidates actually looked like, and if so, document the change and the reasoning behind it in `PROGRESS.md`, since weight and threshold changes are a human decision, not something the pipeline adjusts on its own

Definition of done: the top 10 to 15 candidates have real, evidenced maintenance_burden scores instead of the default; the report visibly distinguishes enhanced-pass candidates from MVP-default candidates; any rule or weight changes made during this review are documented with reasoning, not applied silently.

## Phase 15 — Run 2 / fresh batch

Tasks:
1. Confirm Phase 14's review is finished and any resulting rule changes are intentional and already documented, before spending further API budget
2. Rotate at least one query parameter per search-strategy.md section 7 (date filter, page offset, or leading library subset) for `run_2`
3. Run discovery for `run_2`, and confirm the "new candidates found" count genuinely excludes anything already present in `run_1`'s `discovery_evidence`
4. Run evidence collection, qualification, and scoring for `run_2`'s genuinely new candidates
5. Regenerate the report covering both runs combined and ranked together
6. Confirm the fresh-batch behavior holds against this real second run, not just the simulated fixtures from Phase 12

Definition of done: `run_2` produces genuinely new candidates not present in `run_1`; the combined ranked table includes both runs correctly; `PROGRESS.md` documents exactly what was rotated between the two runs, so the fresh-batch requirement from search-strategy.md is demonstrably satisfied, not just designed for.

## Phase 16 — Final submission artifacts

Tasks:
1. Finalize `dependency-map-report.md` and `ranked-candidates.csv` as the primary deliverables for Task 1 of the growth round
2. Write the one-page write-up the SuperDocs task brief asks for: what was built, the calls made, what was cut and why, and honest numbers rather than invented ones
3. Assemble the private GitHub submission repository per the task brief's own naming and collaborator instructions (`doctask-yourname`, `o-kadam` added as collaborator)
4. Include library-universe.md, search-strategy.md, candidate-schema.md, scoring-model.md, technical-design.md, this implementation-plan.md, `TASK.md`, and `PROGRESS.md` in the repository alongside the code, since the working documents are themselves part of what demonstrates the reasoning
5. Fold the known limitations from technical-design.md section 23 and the "what broke" log from `PROGRESS.md` into the write-up honestly, rather than only presenting what worked
6. Final check that no real person or company was ever contacted at any point, and that no secrets, tokens, or the SQLite database file are committed anywhere in the repository

Definition of done: everything the SuperDocs Growth Task document asks for exists in the submission repository; the write-up is honest about limitations rather than overselling; a final scan confirms no secrets are committed and no real outreach occurred anywhere in the project's history.

## Implementation order

Phases execute strictly in order, 1 through 16, with no skipping and no reordering, even where two phases look independent enough to parallelize (Phase 3's config and Phase 4's library universe loader, for instance, don't strictly depend on each other, but they still run in sequence). The reason is the human-checkpoint model in the next section needs a single linear thread to review against, not several partially-finished branches to reconcile later. The one place this matters most: Phase 14's targeted maintenance-burden work only makes sense once Phase 13 has produced real candidates to choose from, and Phase 15 only makes sense once Phase 14's review, and any resulting rule changes, are actually settled. Nothing here should be started early just because the code for it could technically be written sooner.

## What Claude must NOT do

- Build any dashboard or interactive UI. The brief asks for a ranked table and a query method, not a polished interface, and technical-design.md section 22 puts this explicitly last.
- Implement commit-history pulling as part of the Phase 8 evidence collector. It's deferred entirely to the targeted, top-10-to-15-only pass in Phase 14.
- Implement GitHub dependents-page scraping in the MVP. It's listed under "Later" in technical-design.md section 22.
- Implement Sourcegraph integration in the MVP.
- Implement a deps.dev client in the MVP. Only Libraries.io is required for the first working pipeline; deps.dev cross-checking is explicitly deferred.
- Build any outreach, messaging, or contact capability, in any form, at any point. This is a hard rule from the SuperDocs task brief itself, not just a technical scoping choice.
- Auto-tune or silently adjust the scoring weights or gate thresholds. They live in `weights.yaml` as data specifically so a human changes them deliberately; the pipeline never adjusts its own scoring logic.
- Normalize away or hide a missing dimension's weight in the final score. The unknown-as-0 rule from scoring-model.md stays exactly as specified, and the report must show the gap explicitly, per Phase 11's tasks, not smooth it over.
- Let a high raw score override a reject. The qualification gate always runs first, and reject candidates never receive a score at all.
- Commit `.env`, the SQLite database file, or any token to version control, at any phase.
- Make live API calls from inside the test suite. Tests run against mocked or cached responses only.
- Implement async or parallel request handling for GitHub code search calls specifically. It adds complexity for no real benefit given the 10-per-minute cap, per the reasoning in technical-design.md section 21.

## Human checkpoints

- **End of Phase 2.** Confirm the database schema, including the `unknown_dimensions` addition, before anything is built on top of it.
- **End of Phase 8.** Review real evidence records pulled from a handful of live repositories before qualification and scoring are built on top of that data.
- **End of Phase 10.** Manually verify `weights.yaml` and the gate thresholds match scoring-model.md exactly before scoring runs against real candidates.
- **End of Phase 13.** Read the actual first-run output before Phase 14 begins; Phase 14 depends on a human deciding which candidates deserve the deeper pass.
- **Before Phase 15.** Confirm Phase 14's review, and any rule changes it produced, are finished and documented before more API budget is spent on a second run.
- **Before Phase 16.** Final human sign-off on everything going into the actual submission.

## Definition of MVP

Phases 1 through 13 are complete. Running `dependency-map run` end to end against real GitHub and Libraries.io APIs produces at least one qualified (keep or investigate) candidate with a non-null `final_score`. `dependency-map report` produces both `ranked-candidates.csv` and `dependency-map-report.md`. Every candidate entry in the report visibly shows its score, confidence band, evidence coverage as a fraction (for example "6/7"), and an explicit "Unknown" label for any dimension that defaulted, rather than a bare number that hides the gap. All tests from Phases 1 through 12 pass. Interrupting a run partway through and rerunning it resumes correctly, verified by an actual test, not just asserted by design. Reject candidates never appear in the ranked output. This is the point where the system genuinely runs, even though `maintenance_burden` is still unknown for most candidates and no second run has happened yet.

## Definition of final submission

Phases 1 through 16 are complete. Two full discovery runs exist (`run_1` and `run_2`), genuinely fresh per the fresh-batch requirement, not a replay. The top 10 to 15 candidates by score have a real, evidenced `maintenance_burden` from the targeted Phase 14 pass, and the report distinguishes them from the rest. `dependency-map-report.md` is the primary deliverable, the actual "ranked table plus the query method" the SuperDocs task brief asks for, alongside `ranked-candidates.csv`. The private GitHub repository is set up exactly per the brief's naming and collaborator instructions, containing every working document produced across all eight planning steps plus the code itself. The one-page write-up is honest about what broke and what was cut, using the real numbers from the actual runs rather than invented ones. No real person or company was ever contacted at any point in the project's history, and no secrets are committed anywhere in the repository.

## Claude operating rule

Claude must work phase-by-phase.

Before implementing a phase:
1. Inspect the existing repository.
2. Read the relevant design documents.
3. State the files it intends to create or modify.
4. Identify any ambiguity.
5. Wait for approval when a human checkpoint is defined.

After implementation:
1. Run relevant tests.
2. Run lint/type checks where applicable.
3. Run the CLI/help command where applicable.
4. Summarize exactly what changed.
5. Record progress in PROGRESS.md.
6. Do not silently move to the next phase.
