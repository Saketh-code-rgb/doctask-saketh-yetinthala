# Dependency Map Search Strategy

## 1. Objective

Find public repositories (and, where possible, the real companies behind them) that show genuine signs of a homegrown document generation, editing, or conversion pipeline, using the library universe as the starting vocabulary. The output should be reproducible: someone else should be able to read this document, run the same queries, and land on a comparable set of candidates.

The strategy is split into two stages on purpose, because a single dependency doesn't mean much on its own:

- **Discovery**: cast a wide net using library names and manifest files to find repositories that plausibly touch document processing at all.
- **Qualification**: narrow that list down to repositories where the usage actually looks like a real pipeline (multiple libraries, real code paths, an actual product behind it), not a single script or a tutorial.

## 2. Starting signals

Everything in `library-universe.md` is fair game, but three kinds of signal matter differently:

- **Package names**, searched against the manifest file for each ecosystem: `requirements.txt` / `pyproject.toml` for Python, `package.json` for JS/Node, `pom.xml` / `build.gradle` for Java, `*.csproj` / `packages.config` for .NET.
- **Import or invocation patterns** in actual source code (`import docx`, `require('docxtemplater')`, `org.apache.pdfbox`), since a library can sit unused in a manifest.
- **Infrastructure signals** for the tools that aren't code dependencies at all, like Pandoc, LibreOffice headless, and Gotenberg. These show up in Dockerfiles, docker-compose files, CI scripts, or shell calls rather than import statements, so they need a different query shape than the DOCX/PDF libraries.

## 3. Discovery sources

**GitHub Code Search**
- What we can search: literal text inside files across public repositories, filterable by filename, path, extension, and language. Reaches import statements, manifest entries, and Dockerfile lines directly.
- What evidence it gives: the most direct evidence there is, an actual line of code or manifest entry showing the library in use, with a permalink.
- Advantages: free, covers essentially all public GitHub repositories, supports combining terms (`"python-docx" "reportlab"`) to look for co-occurrence in one query.
- Limitations: requires authentication and is capped at 10 requests per minute even when authenticated. Any single query is capped at 1,000 results, so a generic query like `python-docx` needs to be sliced (by file size; see section 4.5, and note that date slicing is not available here) to get full coverage. Only searches the default branch of indexed repositories, and doesn't rank by anything other than best-match relevance.
- Measured, 2026-08-20: six of eight trial queries exceeded the 1,000-result ceiling, so slicing is a precondition rather than a refinement. The tightest query (a Gotenberg compose-file search) returned 662 results and was fully enumerable; the broadest (a bare `import docx` search) returned 690,176, of which 0.14 percent is reachable. Note also that `language:` cannot be combined with a `filename:` qualifier naming a manifest GitHub does not classify as that language: the combination returns zero rather than narrowing. See section 4.

**GitHub Dependency Graph ("Used by" / Dependents)**
- What we can search: for a package that's published to a supported registry and links back to a public source repository, GitHub maintains a page listing other public repositories that declare it as a dependency (`github.com/{owner}/{repo}/network/dependents`).
- What evidence it gives: a pre-computed reverse-dependency list, no need to reconstruct it ourselves.
- Advantages: free, and it's the closest thing to an authoritative "who uses this" list for a given package.
- Limitations: only works for public repositories, only appears when GitHub has successfully linked the package to its source repo, and there's no official REST endpoint for it, it's a web page, so pulling it programmatically means fetching and parsing HTML rather than calling a clean API. GitHub's own docs also note dependents aren't always populated correctly, especially for packages with unconventional manifest setups.

**GitHub Repository Search**
- What we can search: repository name, description, README, and topics.
- What evidence it gives: candidates whose document handling wouldn't show up as a named dependency at all, for example a company using a paid, non-public SDK, or one that built everything in-house. Also useful for the Task 3 side of this work, finding companies by what they say about themselves.
- Advantages: catches product framing ("contract automation platform", "diagnostic report generator") that a pure code search would miss.
- Limitations: noisy. Description and README text is unstructured, so this needs to run as a secondary, lower-precision source, not the main discovery engine.

**Libraries.io API**
- What we can search: for a given package name and ecosystem, its `dependents()` (other packages that depend on it) and `dependent_repositories()` (actual repositories that depend on it), across more than 30 package managers including PyPI, npm, Maven, and NuGet, from one consistent API.
- What evidence it gives: a structured, scriptable reverse-dependency list per library, without needing to build our own GitHub query for every ecosystem separately.
- Advantages: free (an API key is required, but there's no cost), and it's the only source on this list that gives a single, consistent way to ask "who depends on this" across every ecosystem in the library universe at once.
- Limitations: Libraries.io syncs its data periodically rather than in real time, so very recent adoption of a library may not show up yet. Coverage also depends on the underlying package registries' own data being clean, and it inherits any gaps there.

**deps.dev (Google Open Source Insights)**
- What we can search: package metadata, resolved dependency graphs, license data, and linked project data (stars, forks, issue activity) pulled from PyPI, npm, Maven Central, NuGet, RubyGems, Cargo, and Go modules, via a free JSON or gRPC API.
- What evidence it gives: a second, independently maintained source to cross-check what Libraries.io reports, plus license and advisory data that's useful once we get to qualification.
- Advantages: actively maintained by Google, generally fresher than Libraries.io, and gives clean version-level dependency graphs.
- Limitations: its dependents view is less complete than Libraries.io's for some ecosystems, and it isn't really built as a repository-discovery tool, more as a package-metadata and dependency-resolution tool. Best used to confirm findings, not to originate them.

**Sourcegraph public code search (secondary)**
- What we can search: full-text and regex search across roughly 2 million public repositories on GitHub, GitLab, and Bitbucket at sourcegraph.com/search, with query syntax that makes co-occurrence searches (multiple libraries in the same file or manifest) easier to express than GitHub's own search.
- What evidence it gives: a second code-search index that can catch results GitHub's own search misses, plus non-GitHub public repositories.
- Advantages: free, decent syntax for "does this file contain both X and Y".
- Limitations: Sourcegraph has shifted its product focus toward its AI assistant in the last couple of years and isn't investing in the search product the way it used to, so treat it as a backup and cross-check, not the primary source.

**Package registries themselves (PyPI, npm, Maven Central, NuGet), investigated and mostly set aside**
- PyPI has no built-in reverse-dependency search; its public API is per-package metadata only, so "who depends on requests" isn't answerable from PyPI directly.
- npm shows a "Dependents" tab on a package's own page, but only lists other published npm packages, not arbitrary application repositories, and there's no clean bulk API for it.
- Maven Central has no first-party reverse-dependency feature; the closest thing is the "Used By" tab on the third-party site mvnrepository.com, which is not an official API and would need scraping.
- NuGet has a similar "Used By" tab, again limited to other published NuGet packages.

None of the four is strong enough or consistent enough to be a primary discovery source on its own, and Libraries.io and deps.dev already aggregate the useful parts of what they know. They're worth a manual spot check when a specific package's dependents list looks thin elsewhere, but they don't need their own place in the pipeline.

**The smallest workable set**: GitHub Code Search and the GitHub Dependency Graph for direct, high-confidence evidence; Libraries.io as the one scriptable cross-ecosystem reverse-dependency source; deps.dev to cross-check it; GitHub Repository Search as a secondary channel for candidates that don't show up as a named dependency at all. Sourcegraph stays in reserve for co-occurrence queries GitHub can't express well.

## 4. Discovery queries

Queries are organised into three tiers, ordered by how precise they proved to
be when actually run. The ordering is not a guess: it comes from the controlled
experiment recorded in section 4.4, and it replaces an earlier flat list that
treated every library's query as equally worth running.

The principle behind the tiers is that **how specific a query is matters more
than how popular the library is.** A query that can only match a deployed
conversion service returns a few hundred results, nearly all of them real
products. A query that matches any manifest mentioning a common library returns
tens of thousands, most of them irrelevant.

`discovery_tier` is recorded per entry in `data/library-universe.yaml`, so tier
membership is data rather than a second library list hidden in code. It is
deliberately independent of `library_category`: docxtemplater is a DOCX library
but a tier-2 signal, while Puppeteer sits in the template category but is a
tier-3 signal because the package is mostly used for browser testing.

### 4.1 Tier 1 — Infrastructure

The strongest signal available. These tools are not package dependencies at
all: they are services a team chose to deploy, which means someone made a
deliberate engineering investment in document conversion rather than importing
a library and moving on.

Library: **Gotenberg**
Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
Finds repositories running Gotenberg as a service. Measured on 2026-08-20 at
662 results, the only query in the experiment that stayed under GitHub's
1,000-result ceiling, with no library-adjacent or tutorial noise on the first
page. The results were recognisable products: accounting platforms, CRM
applications, time-tracking SaaS, document-management deployments.

Library: **Pandoc**
Query: `"pandoc" filename:Dockerfile`
Pandoc is a CLI tool, so it never appears in a manifest. Installation in a
Docker image is the way to find it.

Library: **LibreOffice headless / unoconv / JODConverter**
Query: `"libreoffice" filename:Dockerfile`, `"unoconv" filename:Dockerfile`
Same shape as Pandoc: a subprocess or service rather than an import.

**Filename handling.** Compose files appear as both `docker-compose.yml` and
`docker-compose.yaml`, and the query generator must cover both rather than the
library universe carrying duplicate entries for the extension. GitHub's
`filename:` qualifier also matches by prefix, which the experiment demonstrated
by returning a file named `docker-compose.yml-noai`. Near-miss filenames are
expected and are not filtered out at discovery; see section 5.

### 4.2 Tier 2 — Template generation

Libraries whose primary purpose is populating a template from data. Their
presence implies a generation pipeline rather than an incidental read of a
document, which is exactly the pattern the business hypothesis flags as
stronger than plain document creation.

Library: **docxtpl (python-docx-template)**
Query: `"docxtpl" filename:requirements.txt`
Measured on 2026-08-20 at 1,852 results. First-page results included several
real reporting products (security-reporting platforms, financial research
tooling), a materially better hit rate than any tier-3 query.

Library: **docxtemplater**
Query: `"docxtemplater" filename:package.json`
Measured on 2026-08-20 at 3,256 results. Good precision, with one recurring
caveat: roughly a third of the first page were plugins and integrations *for*
docxtemplater rather than products using it. See section 5.

Library: **Carbone.io**
Query: `"carbone" filename:package.json`
Node repositories using a document engine rather than hand-rolling generation.
**Not measured**; placed in tier 2 by reasoning from its description in
library-universe.md ("fills native DOCX/XLSX/PPTX/ODT templates from JSON"),
not from experimental evidence.

Library: **JasperReports / Apache FOP**
Query: `jasperreports filename:pom.xml`
Declarative, template-driven enterprise reporting. **Not measured**; tier
assigned by reasoning.

Library: **docx-mailmerge / docxedit**
Query: `"docx-mailmerge" filename:requirements.txt`
Mail-merge field replacement, a narrower and older template pattern. **Not
measured**; tier assigned by reasoning.

### 4.3 Tier 3 — Broad manifest

A library named in a dependency manifest. Still useful, since this is where
most document-processing usage actually lives, but every query in this tier
returns far more matches than can be retrieved, and most of what it returns is
noise. **Slicing is mandatory here** (section 4.5).

Library: **python-docx**
Query: `"python-docx" filename:requirements.txt`
Measured on 2026-08-20 at 75,648 results, capped. The first page was dominated
by AI and LLM tooling that lists python-docx so an agent can read a Word file.

Library: **ReportLab**
Query: `"reportlab" filename:requirements.txt`
Measured on 2026-08-20 at 90,240 results, capped.

> **Correction.** This query previously read
> `"reportlab" filename:requirements.txt language:python`. That query returns
> **zero results**, because GitHub classifies `requirements.txt` as a text or
> pip-requirements file rather than Python, making the two qualifiers mutually
> exclusive. The `language:` qualifier is not narrowing such a query, it is
> annihilating it. Any query combining `filename:requirements.txt` with
> `language:python` is invalid and must not be generated.

Library: **Apache PDFBox**
Query: `org.apache.pdfbox filename:pom.xml`
Measured on 2026-08-20 at 16,832 results, capped, with heavy library-adjacent
noise: most of the first page were PDF tools and utilities rather than
companies using PDFs in a product.

Library: **Apache Tika**
Query: `org.apache.tika filename:pom.xml`
Tagged as an extraction signal rather than generation, since Tika reads
documents rather than producing them.

Supplementary probe: **DOCX + PDF co-occurrence**
Query: `"python-docx" "reportlab" filename:requirements.txt`
Intended to find repositories declaring both a DOCX and a PDF library in one
manifest. This was previously described as the closest single-query proxy for
the "multiple document libraries combined" signal. **The experiment does not
support that.** Measured on 2026-08-20 at 11,552 results, capped, with a first
page of AI projects and student work. Two document libraries co-occurring in a
requirements file turns out to be weak evidence, because a single LLM framework
pulls both in incidentally. It is retained as a supplementary tier-3 probe, not
as a high-confidence discovery primitive.

### 4.4 Tested and set aside: bare code-import search

Library: **python-docx**
Query: `import docx language:python`
Measured on 2026-08-20 at **690,176 results**, capped.

The original intent was sound: a library can be pinned somewhere other than
`requirements.txt`, and an import statement proves actual use where a manifest
line does not. In practice the query is unusable as a discovery primitive. It
returns nine times the volume of the manifest query for the same library, of
which 0.14 percent is reachable, and the entire first page was personal scripts
with filenames like `1.py`, `02.py` and `voz.py`.

It is excluded from MVP query generation. The narrower goal it was meant to
serve, catching non-`requirements.txt` pinning, is met far more cheaply by
adding `filename:pyproject.toml` to the tier-3 manifest queries.

This is recorded rather than deleted because the measurement is the reason, and
a future reader deciding whether to reintroduce code-import search should see
the number rather than rediscover it.

### 4.5 Slicing

GitHub returns at most 1,000 results for any single query however it is
paginated. Six of the eight queries in the experiment exceeded that ceiling, so
slicing is not a refinement to add later, it is a precondition for claiming any
coverage at all.

Every tier-3 query must therefore be generated as a set of sliced queries
rather than one broad query.

> **Correction, 2026-08-20 (Run 1).** This section previously named a **date
> window** (`pushed:2026-01-01..2026-03-31`) as the primary slicing axis. That
> axis does not exist in GitHub Code Search. `pushed:` is a *repository* search
> qualifier; code search matches it as literal text inside a file, so a query
> carrying it returns zero rather than a narrowed set. Run 1 generated 220
> tier-3 queries this way and every one returned zero, 93 percent of the query
> budget spent for no results. Measured on one query, with and without:
>
> | Query | Matches |
> |---|---|
> | `"python-docx" filename:requirements.txt` | 75,648 |
> | `"python-docx" filename:requirements.txt pushed:2026-05-23..2026-08-21` | 0 |
>
> Date slicing must not be used against code search, and `validate_query`
> now refuses any repository-only qualifier outright.

**The slicing axis is file size.** `size:` is supported by code search, and it
has the properties the date walk was chosen for: it partitions results without
assuming anything about their content, every file has exactly one size, and the
buckets are contiguous with nothing falling outside them. Measured 2026-08-20
on `"python-docx" filename:requirements.txt`, against 75,648 unsliced:

| Slice | Matches |
|---|---|
| `size:0..500` | 46,848 |
| `size:500..2000` | 19,872 |
| `size:>2000` | 12,352 |

The parts sum to roughly the whole, which is what distinguishes a partition
from a filter. The bucket pool is eight contiguous ranges from `size:0..250`
to `size:>16000`, and a run takes four of them.

Two further axes are available but are **not** used for coverage:

- **Ecosystem or language narrowing**, where valid. Note the constraint above:
  `language:` cannot be combined with a `filename:` qualifier naming a manifest
  that GitHub does not classify as that language, which rules it out for
  essentially every tier-3 manifest query.
- **Keyword narrowing.** Adding a second term drawn from the business
  hypothesis vocabulary trades recall for precision. Measured on the same
  query: `invoice` returned 33 matches and `contract` 204, against 75,648. That
  is a precision probe, not a coverage mechanism, and generating it as one
  would misrepresent what a run actually reached.

`path:` was also measured and works (`path:/` returned 49,536), but it has no
clean complement, so it filters rather than partitions and is not generated.
`fork:` is rejected by code search outright with HTTP 422.

**Size is a partition, never a signal.** `size:` exists here for one purpose:
to divide a result set too large to paginate into pieces that can be reached.
The size of a manifest file says nothing about whether the repository behind it
is a good prospect, and it must never be read as if it did. It is not a scoring
dimension, it is not an input to qualification, and it does not affect rank. A
250-byte `requirements.txt` and a 20 KB one are equally interesting until the
evidence collector says otherwise. Nothing in `scoring.py`, `qualification.py`
or `report.py` reads it, and nothing should be added that does.

**Runs are not interchangeable samples.** Because each run takes a different
block of buckets, Run 1 and Run 2 deliberately search *different populations of
files*, not two random samples of the same one. The buckets are also unevenly
filled per ecosystem: a `requirements.txt` is usually small, a Maven `pom.xml`
usually is not, so the low buckets skew Python and the high buckets skew Java.
Measured 2026-08-21: `"pdfbox" filename:pom.xml size:0..250` returned 3
matches, while the same query at `size:2001..4000` returned 6,704.

The consequence is that comparing Run 1's results against Run 2's is comparing
two different slices of the world, and any difference between them may be an
artefact of which file sizes each covered rather than a real change in what is
out there. Counts from the two runs should be added together as coverage, never
differenced as a trend, and the per-query `search_window` record is what lets a
reader check which population a given candidate came from.

**Known limit of the size pool.** A date walk could march backwards
indefinitely; eight size buckets at four per run gives two fully disjoint runs
before the pool wraps. Runs 1 and 2 are guaranteed fresh. Run 3 reuses run 1's
slices and `verify_fresh_batch` will refuse it, at which point a further axis
(a finer bucket split, or keyword partitioning accepting its recall cost) has
to be chosen deliberately. This is recorded as an open constraint rather than
presented as solved.

The slice actually applied is recorded per query in `discovery_queries.search_window`,
so the report can state what was and was not covered rather than implying a
query set was exhaustive.

Tier 1 needs no slicing; the Gotenberg query returned 662 results and is fully
enumerable. Tier 2 is optional and should be applied only when a query is
measured over the ceiling.

### 4.6 Libraries.io

For cross-checking any of the above: a call to
`GET https://libraries.io/api/pypi/docxtpl/dependent_repositories?api_key=KEY`
returns the actual list of repositories declaring docxtpl as a dependency,
which can be diffed against what GitHub Code Search turns up for the same
library. Its `page` parameter is also the natural rotation axis for the
fresh-batch requirement in section 7.

## 5. Candidate filtering

**Keep** when a repository shows more than one library-universe entry actually used in code (not just listed and unreferenced), spans more than one category (for example a DOCX library plus a template engine, or a PDF library plus a conversion tool), and reads like a real product: a README describing what it does for customers, a plausible commit history, and no sign it's a fork or a direct copy of the library it's using.

**Reject** when the only hit is a single library used once, in what's clearly a tutorial, a course assignment, a personal playground, or a fork of the library's own repository or its examples folder. Also reject anything archived with no other product signal, or anything where the "company" appears to just be an individual's side project with no customers implied anywhere in the repo.

**Investigate further** when a repository has multiple library-universe hits but the context isn't clear from the search result alone, for example the manifest lists several document libraries but it isn't obvious from a snippet whether they're actually wired together into a pipeline or just accumulated over time. Also investigate when the repository looks like a real product but it isn't clear who's behind it (no company name, no website in the README), since that's needed for the eventual Task 3 use-case mapping.

### Observed noise classes

The Phase 6A experiment (2026-08-20) surfaced four recurring kinds of
unhelpful result. They are recorded here as **inputs to qualification, not as
discovery filters.** Discovery records what a query returned and makes no
judgment; that separation is deliberate and is what keeps the evidence trail
honest about what was actually seen.

**Library-adjacent tools.** Repositories that are themselves PDF or DOCX
tooling rather than companies using it. The Apache PDFBox query returned six of
these on its first page (PDF comparison, watermark removal, table extraction,
conversion utilities); the docxtemplater query returned three plugins and
integrations built for the library. These are not forks, so the existing
`fork_of_library` rejection reason does not cover them; qualification needs to
recognise a repository whose own product *is* document tooling.

**Incidental AI and LLM usage.** The single largest noise class observed, and
one the earlier drafts of this document did not anticipate. Agent frameworks,
evaluation harnesses and RAG starter kits routinely list `python-docx` so a
model can read a Word file. That is precisely the weak signal the business
hypothesis describes: a document library present without a document workflow
behind it.

**Personal scripts.** Concentrated almost entirely in the bare code-import
query, which is one of the reasons that query was set aside. Single-letter and
numeric filenames at repository root are a reliable tell.

**Nested and auxiliary manifests.** Twenty-one percent of all results came from
a manifest that was not at repository root, such as
`src/inspect_evals/bigcodebench/docker-requirements.txt` or
`deployment/docker/REQUIREMENTS.txt`. A dependency declared in a per-component
or vendored requirements file is weaker evidence of a central document workflow
than the same dependency in a root manifest, and qualification should weigh it
accordingly rather than treating every manifest hit as equivalent.

## 6. Evidence to collect

For every candidate that clears discovery, save: the repository URL and owner/org, the company or product name if it can be identified from the README or an associated site, which library-universe entries were found and in which manifest file or source file, a permalink to the actual code snippet showing usage (not just the manifest line), whether each hit is a generation, extraction, or conversion signal per the tags in `library-universe.md`, how many distinct categories are represented, whether there's a templates/ or reports/ style directory suggesting real document volume, star count and last commit date as a rough proxy for whether the project is alive, primary language, a short excerpt from the README describing what the product actually does, the exact query and source that surfaced it, and the date the query was run.

## 7. Fresh-batch requirement

Run 2 needs to surface candidates Run 1 didn't already return, not a replay of the same top results. GitHub's best-match sort will return the same top hits for an identical query every time, so a fresh batch means changing something about the query itself, not just re-running it.

Concretely: keep a running list of every repository URL or ID already collected, and exclude anything on that list even if it resurfaces. For the query itself, rotate at least one of: the file-size bucket (`size:0..250` for one run, a higher range for the next; the date filter this document originally named is unavailable in code search, see section 4.5), the sort order (best match versus most recently indexed, where the API allows it), the page offset within the same query, or which subset of the library universe leads the search (Run 1 could lead with DOCX and PDF libraries, Run 2 with template and conversion tools). For Libraries.io, request the next page of `dependent_repositories` results rather than the first page again. It's also worth rotating which industry vertical from the business hypothesis the repository-search queries target, so Run 2 doesn't just return more of the same kind of company Run 1 already found.

**Fresh batch and slicing are the same mechanism.** Section 4.5 requires every
tier-3 query to carry a slice because no single query can reach past 1,000
results. Rotating that slice between runs is exactly what the fresh-batch
requirement asks for. Run 1 covering `size:0..250` through `size:1001..2000`
and Run 2 covering `size:2001..4000` through `size:>16000` satisfies both at
once, and because the slice is recorded in `discovery_queries.search_window`,
the difference between the two runs is auditable rather than asserted. Building
a separate rotation system on top of slicing would duplicate machinery that
already has to exist.

The date-filter rotation suggested in the paragraph above is not available
against code search, for the reason given in section 4.5. Page offset and sort
order remain available in principle; the size-bucket walk is what the
implementation actually uses.

Note the practical consequence of the experiment's low measured overlap: only
two repositories appeared in more than one query, so the runs are not currently
at risk of replaying each other. The harder problem is the opposite one,
coverage, since each query reaches a small and largely disjoint slice of what
actually matches.

## 8. Initial pipeline

`library-universe.md` supplies the vocabulary. For each entry, generate a discovery query per source (a GitHub code search string, and where applicable a Libraries.io `dependent_repositories` call). Run discovery and collect raw hits, deduplicating by repository URL as they come in. For each surviving repository, run qualification: pull the actual manifest file and a sample of the source hits, tag each library found as generation, extraction, or conversion, and count how many categories are represented. Apply the keep/reject/investigate rule from section 5. For everything kept or flagged for investigation, record the evidence fields from section 6. Ranking happens after this point, using the dimensions the business hypothesis already lays out (document volume, complexity, business criticality, breadth of the pipeline, build-vs-buy opportunity), but the actual scoring formula is a separate step and isn't designed here. The final output is a ranked table with a link back to the query and evidence that produced each row, so the result can be checked and rerun.

## 9. Current assumptions / open questions

- Assuming a GitHub personal access token is available for code search; without one, code search isn't accessible at all, and even with one the 10 requests/minute cap means the query list needs to run with deliberate pacing, not in a tight loop.
- Assuming a free Libraries.io API key can be obtained; the exact current sign-up requirements weren't fully clear from what's publicly documented, so this needs a quick confirmation before relying on it.
- Open question: for commercial SDKs like Aspose or Spire.Office, a company might license and use them without ever appearing in a public package registry the way an open-source dependency would, so Libraries.io and deps.dev won't catch that usage at all. GitHub code search for license file references or import statements may be the only way in, and it's worth testing whether that actually turns up anything.
- Open question: how to reliably turn a GitHub org or repo owner into an actual company name for the Task 3 side of this work, since a meaningful share of repositories are personal accounts, forks, or don't state a company anywhere in the README.
- Open question: this strategy is GitHub-centric. GitLab and Bitbucket aren't covered directly except through Sourcegraph's index, which may be incomplete for them. Worth deciding whether that gap matters enough to address in v1 or is an acceptable known limitation.
- ~~Open question~~ **Measured, 2026-08-20.** GitHub's 1,000-result cap per query does under-count true usage, and by more than expected: `python-docx` alone matched 75,648 manifests and `reportlab` 90,240, against a ceiling of 1,000. Six of eight trial queries were capped. Section 4.5 now makes slicing a required part of query generation rather than a later refinement, and `discovery_queries.total_count` and `capped` record the shortfall per query so the final report can say "10 of 75,648 inspected" instead of implying coverage it never had. This remains a known undercount, not a solved problem: slicing improves coverage but does not prove completeness.
- Measured, 2026-08-20: the tier ordering in section 4 came out of a controlled eight-query experiment rather than reasoning. The full result set is recorded in PROGRESS.md. These counts are a dated observation of a moving target, not permanent truth; a library's popularity and GitHub's index both change, and any future rerun should expect different numbers.
