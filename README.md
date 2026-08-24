# Dependency Map

Finds public GitHub repositories that show real evidence of a **homegrown
document generation, editing, or conversion pipeline**, then qualifies and
ranks them as potential SuperDocs prospects.

Built by Saketh Yetinthala for the SuperDocs growth task (assigned build:
*Dependency map*).

The premise, from [BUSINESS_HYPOTHESIS.md](BUSINESS_HYPOTHESIS.md): a single
dependency on `python-docx` means very little. What matters is a DOCX library
*plus* a PDF library *plus* a template engine *plus* conversion code, actually
wired together in production application code. That combination suggests a
company spending engineering time maintaining document infrastructure that
isn't their core business.

```
library universe -> discovery -> deduplication -> evidence collection
    -> qualification (keep / investigate / reject)
    -> scoring (7 dimensions, weighted, 0-100)
    -> ranked CSV + Markdown report
```

Discovery and evidence collection call the GitHub API. Qualification and
scoring are pure functions over stored data with no network access, so the
rules can be revised and rerun without spending API budget.

## What it produced

Two complete runs against live GitHub data.

| | Run 1 | Run 2 |
|---|---:|---:|
| Discovery queries | 237 | 237 |
| Repositories surfaced | 4,429 | 4,214 |
| New (never seen before) | 4,429 | **3,584** |
| Previously seen | 0 | 630 |
| Evidence-enriched sample | 500 | 500 |
| Scored and ranked | 220 | 219 |

Run 2 used a disjoint set of file-size slices and needed no code change or
manual candidate selection: `verify_fresh_batch` reported 237 planned, 0
already used, before a single request was sent.

Outputs:

- `outputs/ranked-candidates.csv` and `outputs/dependency-map-report.md` (Run 1)
- `outputs/run2/` (Run 2)

## How discovery works

Queries are generated in three tiers, ordered by *measured* precision rather
than library popularity ([SEARCH_STRATEGY.md](SEARCH_STRATEGY.md) section 4):

- **Tier 1, infrastructure.** A deployed conversion service in a Dockerfile or
  compose file (`"gotenberg/gotenberg" filename:docker-compose.yml`). The
  strongest signal: someone chose to run a service, not just import a library.
- **Tier 2, template generation.** Libraries whose purpose is filling a
  template from data (`"docxtpl" filename:requirements.txt`).
- **Tier 3, broad manifest.** A library named in a dependency manifest. Where
  most usage lives, and the noisiest.

**GitHub returns at most 1,000 results for any query**, however it is
paginated. Tier-3 queries match tens of thousands, so every one carries a
`size:` byte-range slice, and eight contiguous buckets give two fully disjoint
runs. A query whose total exceeds the ceiling is recorded as `capped`, and the
report always describes it as a partial sample — "Sampled 30 of 9,392" — never
as if the total had been inspected.

## Evidence and qualification

Nothing is inferred. Every stored field traces to an `evidence_url`, and the
collector inspects a bounded set of files per repository rather than crawling
it. The distinctions that do the work:

- **Manifest declaration vs code import.** A `requirements.txt` line proves a
  dependency; a matched source file proves use.
- **Infrastructure reference vs service use.** A compose file naming a service
  is a *reference*; application code calling that service is *use*. Collapsing
  the two made self-hosting catalogues look like document companies.
- **Repository purpose.** Catalogue, example/tutorial and examples-directory
  signals are recorded as evidence only; no rule reads them yet.
- **Maintenance burden.** How much custom code surrounds the libraries, graded
  from targeted source inspection, not from commit activity.

Qualification returns **keep / investigate / reject**. Every rejection reason
requires a *positive* combination of evidence — never a bare absence. A
candidate with no evidence is always `investigate`, never `reject`: absence of
evidence is not confirmed absence.

## Scoring

Seven dimensions scored 0-5 against the rubrics in
[SCORING_MODEL.md](SCORING_MODEL.md), weighted to 0-100, with `Decimal`
arithmetic and half-up rounding. Weights and gate caps live in
`config/weights.yaml`, never in code.

**An unknown dimension scores 0 and its weight is not redistributed.** That is
deliberate: it keeps the cost of missing evidence visible instead of smoothing
it away, and every report shows evidence coverage as a fraction plus an
explicit "Unknown" line per candidate.

## Setup

Requires Python 3.11 or newer.

```bash
python -m venv .venv && .venv/Scripts/activate   # Windows
pip install -e ".[dev]"
cp .env.example .env        # then paste a GitHub token into .env
```

`GITHUB_TOKEN` needs public read scope only. Secrets are read from the
environment; they never appear in a tracked file.

## Running

```bash
dependency-map --help
dependency-map runs                              # runs recorded, new vs seen
dependency-map run --run-id run_3 --stage discovery
dependency-map run --run-id run_3 --stage evidence --evidence-limit 50
dependency-map run --run-id run_3 --stage qualification
dependency-map run --run-id run_3 --stage scoring
dependency-map report --run-id run_3
```

`--run-id` is required for every stage except discovery, which is the only one
allowed to create a run. Qualification, scoring and reporting make no network
calls and need no token.

See [DEMO.md](DEMO.md) for a three-minute walkthrough against the stored data.

## Tests

```bash
pytest
```

984 tests. **No test makes a live API call**; a socket-blocking run confirms
zero connection attempts. Tests never write the production database.

## Limitations

Stated plainly, because a named limitation is worth more than a hidden one:

- **Evidence covers a deterministic 500-candidate sample per run, not all
  4,429/4,214 discovered.** Everything outside the sample was stored but never
  examined — absent from the results because it was not looked at, which is
  not the same as having been looked at and dismissed.
- **Capped queries are partial samples.** 86 of Run 1's and 75 of Run 2's
  queries matched more than GitHub will return.
- **Run 1 and Run 2 cover different file-size populations** by design. Their
  counts add together as coverage; they are not two samples of one population
  and must not be differenced as a trend.
- **Maintenance evidence is bounded** to the top-ranked candidates per run, so
  most scored candidates still carry `maintenance_burden` unknown.
- **`contributor_count` is never populated.**
- **Company identity is sparse** — 14 of 220 Run 1 rows. The extractor stores
  an organisation only where a repository states one outright, and refuses
  anything that reads as an individual, so genuine small-company names are
  sometimes lost too.
- **Industry classification is keyword-derived** and low confidence.
- **AI/RAG document-processing platforms can rank highly.** Their evidence is
  real: multi-library document code with custom glue is exactly what the
  rubrics reward.
- **The example/tutorial signal is imprecise** — it fires on READMEs that
  contain an examples heading, which mature products routinely have. Evidence
  only; nothing scores on it.
- **The system identifies engineering-intensive document workflows.** It does
  not fully distinguish document-processing infrastructure from
  customer-facing document workflows with commercial leverage. A top-ranked
  repository is a lead worth a human read, not a qualified prospect.

## Repository layout

```
config/     config.yaml and weights.yaml
data/       library-universe.yaml, SQLite database (db gitignored)
src/        the dependency_map package
tests/      pytest suite
outputs/    Run 1 artifacts; outputs/run2/ holds Run 2
audit/      run archives and comparisons (gitignored, kept locally)
```

`outputs/` is deliberately tracked — those files are the deliverable.

## Planning documents

Produced before any code, and still the source of truth. Where code and a
document disagree, that is a bug in one of them, resolved deliberately rather
than by quietly changing the code.

| Document | What it settles |
|---|---|
| [BUSINESS_HYPOTHESIS.md](BUSINESS_HYPOTHESIS.md) | Which industries have document problems, and what separates a strong prospect from a weak one |
| [LIBRARY_UNIVERSE.md](LIBRARY_UNIVERSE.md) | The ~30 libraries to search for, tagged generation / extraction / conversion |
| [SEARCH_STRATEGY.md](SEARCH_STRATEGY.md) | Discovery sources, the concrete queries, slicing, and the fresh-batch rule |
| [CANDIDATE_SCHEMA.md](CANDIDATE_SCHEMA.md) | Every field per candidate, each backed by an `evidence_url` |
| [SCORING_MODEL.md](SCORING_MODEL.md) | The seven rubrics, the weights, the gate caps, and why unknown scores 0 |
| [TECHNICAL_DESIGN.md](TECHNICAL_DESIGN.md) | Architecture, schema, reliability and caching |
| [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) | The 16 phases and the explicit do-not-build list |
| [OBSERVATIONS.md](OBSERVATIONS.md) | Field notes from actually using SuperDocs |
| [PROGRESS.md](PROGRESS.md) | What was actually done, phase by phase, including every defect found |
| [WRITEUP.md](WRITEUP.md) | The one-page summary |

[TASK.md](TASK.md) describes how to work in this repository.

## Scope boundaries

This project builds **no outreach, messaging, or contact capability of any
kind, in any phase**. No real person or company is contacted by this system at
any point. SuperDocs handles all outreach itself.

Per the task brief, real companies may appear in this repository and real
people may not: `company_name` stores an organisation or nothing, and no
personal names are recorded in any output.

It also does not build a dashboard or UI, does not auto-tune its own scoring
weights, and does not make live API calls from its test suite.
