# Demo — about three minutes

Runs against the stored database from Runs 1 and 2, so nothing here needs a
long live GitHub pass. Only step 8 is optional and touches the network.

Nothing in this sequence contacts any person or company. The system has no
outreach capability.

## 0. Setup (~20s)

```bash
pip install -e ".[dev]"
cp .env.example .env          # paste a GitHub token; public read scope only
pytest -q                     # 984 passed
```

The suite makes no live API calls. To prove it rather than assert it, the
socket-blocking plugin used throughout development reports zero connection
attempts across all 984 tests.

## 1. What the tool is (~15s)

```bash
dependency-map --help
```

Four commands: `discover`, `run`, `runs`, `report`. `--run-id` is required for
every stage except discovery — the one stage allowed to create a run.

## 2. The two runs (~20s)

```bash
dependency-map runs
```

Shows both runs with their rotation and new-versus-seen counts. Run 1 covers
size slices `0..250` through `1001..2000`; Run 2 covers `2001..4000` through
`>16000`. **Run 2: 3,584 new candidates, 630 previously seen.**

## 3. Discovery method (~25s)

```bash
sqlite3 data/dependency_map.db \
  "SELECT discovery_tier, query, total_count, returned_count, capped
     FROM discovery_queries WHERE run_id='run_2'
     ORDER BY discovery_tier LIMIT 6;"
```

Tier 1 is a deployed service in a compose file; tier 3 is a manifest query with
a `size:` slice. Note a `capped` row: GitHub returns at most 1,000 results for
any query, so the report describes such a query as *"Sampled 30 of 9,392 …
a partial sample, not an exhaustive result"* — never as if the total had been
inspected.

## 4. Evidence for one candidate (~30s)

```bash
sqlite3 data/dependency_map.db \
  "SELECT library_name, detection_method, evidence_url
     FROM dependencies_found
    WHERE candidate_id=(SELECT candidate_id FROM scores
                        ORDER BY final_score DESC LIMIT 1);"
```

Every row carries a permalink. The distinction that does the work:
`manifest_declaration` proves a dependency exists, `code_import` proves it is
used in a source file, and `infrastructure_reference` proves a service is
declared — which is separate from that service actually being called.

## 5. Qualification (~20s)

```bash
sqlite3 data/dependency_map.db \
  "SELECT qualification_status, COUNT(*) FROM qualification GROUP BY 1;"
sqlite3 data/dependency_map.db \
  "SELECT rejection_reason, COUNT(*) FROM qualification
    WHERE qualification_status='reject' GROUP BY 1 ORDER BY 2 DESC;"
```

Every rejection reason requires a positive combination of evidence. A candidate
with no evidence is always `investigate`, never `reject` — absence of evidence
is not confirmed absence.

## 6. Scoring (~20s)

```bash
sqlite3 data/dependency_map.db \
  "SELECT final_score, confidence_band, maintenance_burden, unknown_dimensions
     FROM scores ORDER BY final_score DESC LIMIT 5;"
```

Seven dimensions, weighted to 0–100. An unknown dimension scores 0 and its
weight is **not** redistributed, so the cost of missing evidence stays visible.
`unknown_dimensions` names exactly which ones defaulted.

## 7. The reports (~30s)

```bash
dependency-map report --run-id run_1
dependency-map --output-csv outputs/run2/ranked-candidates.csv \
               --output-markdown outputs/run2/dependency-map-report.md \
               report --run-id run_2
```

Each report is scoped to its run. Open `outputs/run2/dependency-map-report.md`
and show three things:

- **Coverage and sampling (run_2)** — 4,214 surfaced, 3,584 new, 630 seen, 500
  enriched, and the sentence saying the remaining 3,714 were *not examined*,
  which is not the same as examined and dismissed.
- **The ranked table** — score, confidence, evidence coverage as a fraction,
  and an explicit Unknown column.
- **Cumulative project state (all runs)** — labelled as covering both runs, so
  no cumulative number is mistaken for this run's result.

## 8. Optional: the fresh-batch guard, live (~20s)

```bash
dependency-map run --run-id run_3 --stage discovery --tier 1 --query-limit 2
```

Plans run 3's rotation and checks it against every earlier run *before* any
request is sent. A fully-overlapping plan is refused rather than replayed.

## Closing line

From an empty database to a ranked prospect list, then again on a fresh batch:
3,584 repositories Run 1 had never seen, with zero tier-3 query overlap and no
code changed between the runs.
