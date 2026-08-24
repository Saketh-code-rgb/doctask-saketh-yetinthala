# Dependency Map — one-page write-up

**Saketh Yetinthala · SuperDocs growth task, assigned build: *Dependency map***

## Problem and hypothesis

The card asks for OSS projects that depend on document manipulation libraries,
on the theory that heavy dependency means an expensive homegrown pipeline —
and a prime SuperDocs target. The hard part isn't finding mentions of
`python-docx`; 75,648 repositories do. It's separating casual use from a real
pipeline. One dependency means nothing; a DOCX library *plus* a PDF library
*plus* a template engine *plus* conversion code, wired together in production
code, means a team maintaining infrastructure that isn't their core business.

## Approach

Three discovery tiers ordered by *measured* precision, not popularity:
infrastructure (a deployed service in a compose file), template generation,
broad manifest. Evidence collection inspects a bounded set of files per
repository — never a crawl — and every stored field carries an `evidence_url`.
Qualification returns keep/investigate/reject; scoring applies seven 0–5
rubrics weighted to 0–100.

Two design choices carried the most weight. **Absence of evidence is never
confirmed absence**: every rejection needs a positive combination of evidence,
so a candidate with none is always `investigate`. And **an unknown dimension
scores 0 without redistributing its weight**, keeping missing evidence visible
instead of smoothing it away.

## What real runs changed

1. **`pushed:` is not a code-search qualifier.** The first real run generated
   220 date-sliced queries; all 220 returned zero — GitHub matches `pushed:` as
   literal text in code search (measured: 75,648 without it, 0 with it).
   Replacing date windows with `size:` byte ranges — verified as a genuine
   partition, summing to the whole — took unique repositories from 412 to
   **4,429**. That run was discarded and re-run.
2. **A compose file is not a service in use.** "A file exists and there is
   application code somewhere" made self-hosting catalogues look like document
   companies. Requiring direct evidence — the service called from source, or
   wired into configuration — removed **40 of 62** such claims.
3. **Discovery discarded the matched file**, so the collector fell back to the
   repository root and missed compose files elsewhere (39% of matches weren't
   at root). Recovering paths from the response cache cost zero API calls and
   cut zero-dependency candidates from 26 to 10.

## Numbers

| | Run 1 | Run 2 |
|---|---:|---:|
| Queries executed / failed | 237 / 0 | 237 / 0 |
| Repositories surfaced | 4,429 | 4,214 |
| New / previously seen | 4,429 / 0 | **3,584 / 630** |
| Evidence-enriched sample | 500 | 500 |
| keep / investigate / reject | 44 / 176 / 281 | 46 / 173 / 281 |

Run 2 used disjoint size slices, no code change, no manual selection; the
fresh-batch guard confirmed 237 planned / 0 already used before any request.
1,039 tests pass, zero network calls.

## What I cut, and limitations

No dashboard, LLM classification, or auto-tuned weights. **No outreach
capability at any phase** — the brief forbids contact, so the capability was
never built. A full 4,429-candidate evidence pass would cost ~8 hours of API
time; I used a deterministic 500-candidate sample per run and said so, rather
than implying full coverage. Evidence covers 500 of ~4,400 discovered per run —
the rest were stored but never examined. 86/75 queries matched more than
GitHub returns and are labelled partial samples. Run 1 and Run 2 cover
different file-size populations and must not be differenced as a trend.
Maintenance evidence is bounded to top-ranked candidates; `contributor_count`
is never collected; company identity is sparse (real companies may appear in
this repository, real people may not, so the extractor refuses anything
reading as an individual).

Most importantly: **the system finds engineering-intensive document
workflows, not commercial prospects.** AI/RAG platforms rank highly because
their evidence is genuine — multi-library code with custom glue is exactly
what the rubrics reward. A top row is a lead worth a human read, not a
qualified prospect.

## Next

Separate *who the work is for* from *how much of it there is* — the current
dimensions measure engineering intensity well and commercial leverage poorly,
the biggest gap between this ranking and a prospect list. Then widen the
sample (a run now costs ~26 minutes), and extend the exact-path fetch to
manifests and source, which explains 3 of the 10 remaining zero-dependency
candidates.
