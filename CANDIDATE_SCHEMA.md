# Dependency Map Candidate Schema

## 1. Schema overview

This schema defines one record per candidate repository. It exists to close the gap the search strategy left open: phrases like "looks like a real product" or "plausible commit history" are judgment calls, and two different passes over the same repo could land on different answers. Every field below is either something pulled directly from an API (a star count, a boolean from GitHub's metadata) or something that has to be backed by a specific `evidence_url` before it can be set. Nothing gets recorded as true or false just because it "seems" that way.

The sections follow the flow from the earlier notes:

```
Candidate
   -> Identity
   -> Discovery evidence
   -> Dependency evidence
   -> Pipeline evidence
   -> Business evidence
   -> Qualification decision
   -> Ranking fields
```

Field names are written in snake_case, since they're meant to map directly onto whatever gets built later, whether that's JSON output, a spreadsheet, or a database table.

## 2. Identity

| Field | Type | Description / allowed values |
|---|---|---|
| candidate_id | string | Stable identifier, generated from repo_url (a hash is fine), so the same repository always resolves to the same record across runs |
| repo_url | string (URL) | Canonical GitHub URL |
| repo_owner | string | Org or username |
| repo_name | string | |
| is_fork | boolean | Pulled directly from the GitHub API's `fork` field |
| is_archived | boolean | Pulled directly from the GitHub API |
| primary_language | string | Pulled directly from the GitHub API |
| company_name | string or null | Only filled when identifiable, null otherwise, never guessed |
| company_name_source | enum: readme / website_link / org_profile / external_search / null | Records how company_name was derived; null if company_name is null |
| product_name | string or null | |
| website_url | string (URL) or null | Pulled from repo description, README, or org profile |
| industry_category | enum | One of the categories from the business hypothesis: legal_contracts, real_estate, healthcare_diagnostics, education, finance_investment, proposal_sales, events_weddings, software_technical_docs, other, unknown |

## 3. Discovery evidence

Discovery evidence splits across two records, because a query execution and a
candidate hit are different things with different lifetimes. A query is
executed once and may return many candidates, one candidate, or none at all.
Keeping query facts on the candidate record would both duplicate them across
every hit and, worse, lose them entirely when a query returns nothing.

That last case is not hypothetical. The Phase 6A experiment found a query in
this document that returned zero results because of an invalid qualifier
combination. Under a candidate-only model that finding would have left no trace
in the database at all.

### 3a. Query record

*Stored as `discovery_queries`.* One record per query execution, whether or not
it found anything.

| Field | Type | Description / allowed values |
|---|---|---|
| query_id | string | Stable identifier for this query execution, derived from run_id, query and search_window, so re-running the same slice within a run resolves to the same record instead of duplicating it |
| run_id | string | Which run executed it (run_1, run_2, ...), needed to satisfy the fresh-batch requirement from the search strategy |
| discovery_source | enum | github_code_search / github_dependents / github_repo_search / libraries_io / deps_dev / sourcegraph / manual |
| library_name | string or null | The library-universe entry this query was generated for. Null for co-occurrence queries, which deliberately span more than one library |
| discovery_tier | integer or null | 1 infrastructure / 2 template generation / 3 broad manifest, per search-strategy.md section 4. Null where a tier doesn't apply, such as a manual query |
| query | string | The exact query string or API call, copied verbatim |
| total_count | integer or null | Total matches the source reported for this query, independent of how many were retrieved. Null when the source reports no total, as Libraries.io and manual entry do |
| capped | boolean or null | True when `total_count` > 1000, meaning the query exceeded GitHub's pagination ceiling. This says the query had more matches than can ever be retrieved; it does **not** mean 1,000 results were retrieved, and in practice far fewer are. Null when `total_count` is null |
| search_window | string or null | The slicing qualifier actually applied, verbatim, for example `pushed:2026-01-01..2026-03-31`. Null means the query was run unsliced, not that the slice is unknown |
| returned_count | integer | How many raw results the API handed back for this execution. Intentionally allowed to differ from the number of candidate records below, since several hits can collapse onto one repository |
| executed_at | timestamp (ISO 8601) | |

### 3b. Candidate hit record

*Stored as `discovery_evidence`.* One record per candidate surfaced by a query. A candidate accumulates many of
these, one per query or run that found it, which is the mechanism deduplication
and fresh-batch tracking read from.

| Field | Type | Description / allowed values |
|---|---|---|
| query_id | string | Which query execution surfaced this candidate. Everything about the query itself is reached through here rather than repeated per hit |
| candidate_id | string | Which candidate was surfaced |
| discovery_result_rank | integer or null | Position in the result list when found, useful for checking whether a later rerun of the same query returns comparable results |

`discovery_source`, `discovery_query`, `discovery_run_id` and `discovered_at`
were previously fields on this record. They are all properties of the query
rather than of the hit, and now live in 3a, reached through `query_id`. The
timestamp of a hit is the `executed_at` of the query that found it.

## 4. Dependency evidence

`dependencies_found` is a list, one entry per library actually located, each with:

| Field | Type | Description / allowed values |
|---|---|---|
| library_name | string | Matched against an entry in library-universe.md |
| library_category | enum | docx / pdf / template_generation / conversion / other_processing |
| direction | enum | generation / extraction / conversion / mixed, per the tags used in library-universe.md |
| manifest_file | string or null | e.g. requirements.txt, package.json; null if this library was found through infrastructure evidence instead (a Dockerfile, a docker-compose service) rather than a manifest |
| detection_method | enum | manifest_declaration / code_import / infrastructure_reference |
| evidence_url | string (URL) | Permalink to the specific file and line |

Computed at the candidate level, from the list above:

| Field | Type | Description |
|---|---|---|
| category_count | integer | Number of distinct library_category values present |
| generation_signal_count | integer | Count of entries where direction = generation |
| extraction_signal_count | integer | Count of entries where direction = extraction |
| conversion_signal_count | integer | Count of entries where direction = conversion or mixed |

## 5. Pipeline evidence

This section turns "is this actually a pipeline, not just an import" into fields that have to be justified individually rather than eyeballed as a whole.

| Field | Type | Description / allowed values |
|---|---|---|
| code_usage_confirmed | boolean | True only if at least one entry in dependencies_found has detection_method = code_import or infrastructure_reference. A repository where every hit is manifest_declaration only gets false here |
| template_directory_present | boolean | True if a templates/, reports/, or similarly named directory exists in the repo |
| multiple_document_types_handled | boolean | True if code evidence shows more than one output format (for example both DOCX and PDF), not just one library used in one place |
| pipeline_stage_count | integer | Count of distinct stages evidenced in code (for example: fetch data, populate template, convert format, deliver output). Each counted stage needs its own evidence_url; stages that are assumed rather than seen don't count |
| infrastructure_service_present | boolean | True only if a document-conversion service (Gotenberg, LibreOffice headless, and so on) is actually deployed, evidenced by a docker-compose entry, Dockerfile, or deployment manifest, not just mentioned in passing |
| pipeline_evidence_notes | string | Short free text for anything the fields above don't capture cleanly |

## 6. Business evidence

This is the section that replaces "real product" with discrete, checkable claims.

| Field | Type | Description / allowed values |
|---|---|---|
| readme_describes_product | boolean | True only if the README states what the software does for a customer or user, not just what a script does internally. Requires a quoted excerpt to be set true |
| readme_excerpt | string | The specific sentence(s) used to justify readme_describes_product |
| website_exists | boolean | Mirrors whether website_url is non-null |
| application_code_exists | boolean | True if the repository contains a real application (routes, models, a UI, a service) beyond the document-library usage itself, distinguishing it from a demo script that only shows off the library |
| document_functionality_in_production_code | boolean | True if the document-related code lives in the application's main path, not in /examples, /test, /scripts, or /demo |
| stars | integer | From the GitHub API |
| last_commit_date | date | From the GitHub API |
| contributor_count | integer or null | From the GitHub API, where available |
| business_evidence_notes | string | Short free text |

A repository only counts as "real product" evidence when readme_describes_product, application_code_exists, and is_fork = false all hold together, with document_functionality_in_production_code as the strongest single field for whether the document handling itself is central or incidental. No single field decides this alone.

## 7. Qualification decision

| Field | Type | Description / allowed values |
|---|---|---|
| qualification_status | enum | keep / investigate / reject |
| qualification_reason | string | References the specific field values that justified the decision, for example "category_count=2, code_usage_confirmed=true, readme_describes_product=true", not a general summary |
| rejection_reason | enum or null | Only set when qualification_status = reject. One of: single_incidental_use, tutorial_or_demo, fork_of_library, archived_no_signal, personal_project_no_customers, other (with detail in qualification_reason) |
| confidence | enum | high / medium / low, reflecting how much of the decision rests on directly observed fields versus inference where evidence was thin |

## 8. Ranking fields

These are the dimensions the eventual score will draw on, carried over from the business hypothesis. No formula yet, just what each dimension means and what would move it up, down, or to unknown.

**document_volume**
- High score supported by: language in the README or docs pointing to volume ("thousands of contracts a month"), the repository being a multi-tenant SaaS platform (industry_category plus business_evidence suggesting many customers), or code that loops over a dataset generating many outputs rather than producing one document.
- Low score supported by: a single document type generated once, an internal or personal tool, no batch-processing code path anywhere in the pipeline evidence.
- Unknown when: no volume language anywhere in the README or docs, and the code structure doesn't reveal batch behavior either way.

**document_complexity**
- High score supported by: category_count of 2 or more, multiple_document_types_handled = true, evidence of multi-section documents, tables, images, or headers and footers in the templates found.
- Low score supported by: one flat template, one library, no formatting logic beyond basic text insertion.
- Unknown when: template contents aren't inspectable (stored as binary files we can't read into) and the README says nothing about formatting.

**business_criticality**
- High score supported by: industry_category of legal_contracts, healthcare_diagnostics, or finance_investment, combined with README or product framing that ties the documents directly to a contract, a compliance requirement, or a customer-facing deliverable.
- Low score supported by: document generation clearly serving an internal purpose (auto-generated changelogs, developer-facing scripts, internal reports with no external recipient).
- Unknown when: industry_category is unclear or no framing was found either way.

**pipeline_complexity**
- High score supported by: pipeline_stage_count of 3 or more, infrastructure_service_present = true, more than one detection_method represented (declared, actually called, and deployed as a service).
- Low score supported by: a single call to a single library in one file, nothing else.
- Unknown when: code_usage_confirmed = false, meaning only the manifest was seen and the actual code path was never inspected.

**maintenance_burden**
- High score supported by: substantial custom code sitting between the library import and its use (hand-rolled formatting or glue logic), several document libraries combined and stitched together manually, frequent commits touching document-related files.
- Low score supported by: the library used in a thin, direct way, one call, no custom logic wrapped around it.
- Unknown when: commit history wasn't pulled (this is the most expensive field to fill, since it needs its own API calls beyond code search) or too little surrounding code was retrieved to judge either way.

**build_vs_buy_signal**
- High score supported by: evidence the team is reinventing something SuperDocs already does, for example their own template engine layered on raw DOCX manipulation, or their own HTML-to-PDF pipeline built from primitives rather than an existing high-level tool.
- Low score supported by: the team already using a high-level managed tool (Carbone, Aspose, Gotenberg) that already solves the problem, or using a document library so lightly that build-vs-buy doesn't meaningfully apply.
- Unknown when: there isn't enough visibility into how much of the logic is custom versus off-the-shelf.

**commercial_leverage**
- High score supported by: industry_category and business_evidence indicating a platform or SaaS product serving many downstream customers, where one integration would reach all of them.
- Low score supported by: a single organization's internal tool, a small team, no multi-tenant signal anywhere.
- Unknown when: it isn't clear from what's visible whether this is a platform or a single company's own tooling.

## 9. Evidence trail

Every candidate keeps a list of evidence entries, not just one. Each entry has:

| Field | Type | Description |
|---|---|---|
| evidence_url | string (URL) | Permalink to the exact source: a code line, a manifest entry, a README section, a website page, an API response, or a dependents page |
| evidence_type | enum | code_permalink / manifest_line / readme_excerpt / website_page / api_response / dependents_page / other |
| evidence_excerpt | string | The specific text or data point being cited, kept short |
| source | string | Which discovery_source or tool produced this piece of evidence |
| collected_at | timestamp | May differ from discovered_at, since qualification and business evidence are often gathered in a later pass than the initial discovery hit |

This matters for three reasons. First, defensibility: every field in sections 2 through 8 that isn't raw API metadata should be traceable back to something in this list, so a claim like readme_describes_product = true can be checked against the actual sentence rather than taken on faith. Second, reproducibility: GitHub content changes and disappears, so a permalink with a collected_at timestamp lets someone verify what was seen at the time, even if the repository has since changed. Third, it's what makes the fresh-batch requirement enforceable: without a collected_at timestamp, and a run traceable through the query record in section 3a, there's no clean way to tell Run 2's evidence apart from Run 1's.

## 10. Example candidate

**SYNTHETIC EXAMPLE — NOT REAL DATA**

```
candidate_id: c_8f2a1d
repo_url: https://github.com/clauseforge-io/lease-engine
repo_owner: clauseforge-io
repo_name: lease-engine
is_fork: false
is_archived: false
primary_language: Python
company_name: ClauseForge
company_name_source: website_link
product_name: ClauseForge Lease Engine
website_url: https://clauseforge.example.com
industry_category: real_estate

discovery (query record, shared with every other candidate this query found):
  query_id: q_4b91c7
  run_id: run_1
  discovery_source: github_code_search
  library_name: docxtpl (python-docx-template)
  discovery_tier: 2
  query: "docxtpl" filename:requirements.txt
  total_count: 1852
  capped: true
  search_window: null
  returned_count: 30
  executed_at: 2026-08-21T09:14:00Z

discovery (candidate hit record):
  query_id: q_4b91c7
  discovery_result_rank: 12

dependencies_found:
  - library_name: docxtpl
    library_category: template_generation
    direction: generation
    manifest_file: requirements.txt
    detection_method: code_import
    evidence_url: https://github.com/clauseforge-io/lease-engine/blob/main/app/documents/lease_builder.py#L18
  - library_name: pypdf
    library_category: pdf
    direction: extraction
    manifest_file: requirements.txt
    detection_method: manifest_declaration
    evidence_url: https://github.com/clauseforge-io/lease-engine/blob/main/requirements.txt#L7
  - library_name: WeasyPrint
    library_category: template_generation
    direction: conversion
    manifest_file: requirements.txt
    detection_method: code_import
    evidence_url: https://github.com/clauseforge-io/lease-engine/blob/main/app/documents/render.py#L41
category_count: 2
generation_signal_count: 1
extraction_signal_count: 1
conversion_signal_count: 1

code_usage_confirmed: true
template_directory_present: true
multiple_document_types_handled: true
pipeline_stage_count: 3
infrastructure_service_present: false
pipeline_evidence_notes: "Pipeline is data -> docxtpl template -> WeasyPrint PDF render. pypdf appears only in requirements.txt, no confirmed call site found."

readme_describes_product: true
readme_excerpt: "ClauseForge auto-generates state-specific lease agreements for property managers from a single intake form."
website_exists: true
application_code_exists: true
document_functionality_in_production_code: true
stars: 41
last_commit_date: 2026-07-30
contributor_count: 4
business_evidence_notes: "README frames this as a customer-facing product for property management companies, not an internal tool."

qualification_status: investigate
qualification_reason: "category_count=2, code_usage_confirmed=true, readme_describes_product=true, but pypdf has no confirmed call site (detection_method=manifest_declaration only), so the actual scope of the PDF-handling side of the pipeline is unclear."
rejection_reason: null
confidence: medium

document_volume: unknown
document_complexity: high
business_criticality: high
pipeline_complexity: medium
maintenance_burden: unknown
build_vs_buy_signal: high
commercial_leverage: unknown

evidence_trail:
  - evidence_url: https://github.com/clauseforge-io/lease-engine/blob/main/app/documents/lease_builder.py#L18
    evidence_type: code_permalink
    evidence_excerpt: "from docxtpl import DocxTemplate"
    source: github_code_search
    collected_at: 2026-08-21T09:16:00Z
  - evidence_url: https://github.com/clauseforge-io/lease-engine/blob/main/README.md
    evidence_type: readme_excerpt
    evidence_excerpt: "auto-generates state-specific lease agreements for property managers"
    source: manual
    collected_at: 2026-08-21T09:20:00Z
```

## 11. Open questions

- maintenance_burden is the field most likely to stay unknown at scale, since judging "how much custom logic sits around the library" really needs a human or a deeper code read, not just a code search hit. Worth deciding whether it's acceptable to leave this unknown for most candidates in v1, or whether a cheap proxy (lines of code in the file that imports the document library, as a rough stand-in) is worth building.
- The evidence_trail list could get long for a well-qualified candidate. Worth deciding a cap, or whether it's fine to let it grow and just rely on evidence_type to filter later.
- industry_category currently depends on reading the README and matching it to one of nine categories, which is itself a judgment call, not a hard rule. It may need its own short set of matching examples per category before it's consistent across candidates.
- commit history (needed for parts of maintenance_burden) requires separate GitHub API calls beyond code search, which eats further into the 10 requests/minute code search budget and the broader per-hour REST limit. Worth deciding whether it's pulled for every kept/investigate candidate or only for a final shortlist.
- Libraries.io and deps.dev both lag real-time by some amount, so discovered_at and the actual current state of a repository's dependencies could drift apart for older candidates. Not clear yet how much that matters for ranking versus just discovery.
