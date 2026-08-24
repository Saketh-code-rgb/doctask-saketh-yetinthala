# Dependency Map Scoring Model

## 1. Purpose and architecture

This model only ever runs on candidates that already survived qualification. Scoring never rescues a candidate, it only ranks the ones qualification already let through. The flow is:

```
Discovery
   -> Qualification (keep / investigate / reject)
   -> Only keep / investigate candidates proceed
   -> Score each of the 7 dimensions from candidate-schema.md, 0-5
   -> Apply weights
   -> Apply the qualification gate (section 14) as a cap, not a bonus
   -> Final score, 0-100
   -> Rank
```

A reject never gets a final_score at all. It doesn't get a score of zero either, it simply doesn't enter the ranked table, because a numeric zero next to a company name still invites comparison, and a rejected candidate shouldn't be comparable to anything.

## 2. Scoring scale

Every dimension below uses the same 0 to 5 scale, so the anchors mean the same thing everywhere:

- **0**: The dimension is unknown, no usable evidence was collected, or the evidence directly contradicts the dimension (a confirmed false on a relevant schema field). Unknown is deliberately scored at the bottom of the scale rather than at a neutral middle value; see section 12 for why.
- **1**: Minimal but *confirmed* evidence. Something was actually observed; there is just very little of it. This rung is never used for an unknown.
- **2**: Some evidence, but thin or limited to a single weak signal.
- **3**: Moderate, clearly-present evidence, more than one signal pointing the same direction.
- **4**: Strong evidence, multiple corroborating signals.
- **5**: Decisive evidence, the strongest form this dimension can take given what a public repository can actually show us.

Each dimension section below defines what specifically earns each rung, tied to fields from `candidate-schema.md` wherever possible so the score isn't a feeling, it's a readout of fields that are themselves evidence-backed.

## 3. Dimension: Document Volume

### 0
No volume language anywhere (README, docs, code comments) and no batch-processing code path in the pipeline evidence. `document_volume` in the schema is unknown with nothing to lean on.

### 1
A single document type generated once, or code that clearly produces one output per manual run, with no loop or batch behavior anywhere.

### 2
A batch or loop construct exists somewhere in the pipeline evidence (iterating over records to produce multiple documents), but no explicit numbers or scale language anywhere.

### 3
README or docs describe recurring, ongoing generation ("used by our team to generate weekly reports") without a specific volume figure, or the repository is framed as serving multiple tenants without stating how many.

### 4
Explicit volume language tied to the actual pipeline found (a number, a frequency, or an order-of-magnitude claim like "thousands of documents a month"), or a confirmed multi-tenant platform where document generation is a core, repeated action for each tenant.

### 5
Explicit, specific volume language directly describing the document pipeline that was found (not marketing copy elsewhere in the repo) combined with confirmed multi-tenant framing, so both the scale and the breadth of who's generating documents are evidenced together.

## 4. Dimension: Document Complexity

### 0
`category_count` = 1, `multiple_document_types_handled` = false, and no evidence of structure beyond plain text insertion.

### 1
`category_count` = 1, but tables, images, or multi-section structure are evidenced in the template or code.

### 2
`category_count` = 2, but only one of the two dependencies has `detection_method` = code_import or infrastructure_reference. The other is manifest-only, so the actual complexity is unconfirmed.

### 3
`category_count` = 2 with `multiple_document_types_handled` = true and both dependencies confirmed via code usage, not just declared.

### 4
`category_count` = 3, or a confirmed conversion chain where one template feeds more than one output format.

### 5
`category_count` >= 3 with confirmed code usage across all of them, or explicit evidence (from `pipeline_evidence_notes` or direct code) of multi-section, multi-format, templated documents actually running in production.

## 5. Dimension: Business Criticality

### 0
`document_functionality_in_production_code` = false, or the documents evidently serve an internal, non-customer-facing purpose (changelogs, internal dev reports).

### 1
Internal but customer-adjacent, for example internal reports that describe or summarize customer activity without being delivered to the customer.

### 2
`industry_category` is unclear or "other", but `application_code_exists` = true and `readme_describes_product` = true, so there's a real product, just not one that maps cleanly onto a known high-criticality vertical.

### 3
`industry_category` is a moderately critical vertical (education, events_weddings) with clear customer-facing framing in the README.

### 4
`industry_category` is a high-criticality vertical (real_estate, proposal_sales, software_technical_docs) with explicit language tying the document directly to revenue or delivery to a customer.

### 5
`industry_category` is legal_contracts, healthcare_diagnostics, or finance_investment, and there's explicit language tying the document to a contract, a compliance obligation, or a patient or financial deliverable, not just a general business description.

## 6. Dimension: Pipeline Complexity

### 0
`pipeline_stage_count` is 0 or 1, and `code_usage_confirmed` = false. Only manifest evidence exists.

### 1
`pipeline_stage_count` = 1 with `code_usage_confirmed` = true. A single confirmed step, nothing chained after it.

### 2
`pipeline_stage_count` = 2, both confirmed.

### 3
`pipeline_stage_count` = 3, all confirmed through a single `detection_method`.

### 4
`pipeline_stage_count` >= 3 with more than one `detection_method` represented (for example, some steps confirmed via direct code_import and others via infrastructure_reference).

### 5
`pipeline_stage_count` >= 3 AND `infrastructure_service_present` = true, meaning the pipeline spans actual application code and a deployed conversion service, the strongest evidence a real, running system exists rather than a script.

## 7. Dimension: Maintenance Burden

### 0
Unknown. Commit history wasn't pulled, or too little surrounding code was retrieved to judge either way. This is the default for most candidates in a first pass, and that's intentional, see section 12.

### 1
The library is used in a thin, direct way, one call, no custom logic wrapped around it.

### 2
Some custom logic evidenced, for example a small formatting helper function, but limited in scope.

### 3
Multiple libraries stitched together with visible custom glue code connecting them.

### 4
Substantial custom code sitting between the library import and its actual use, plus some evidence of repeated modification if commit history was pulled.

### 5
An extensive, clearly hand-built system: custom formatting, validation, and error handling layered around multiple document libraries, functionally a homegrown version of what SuperDocs already does.

## 8. Dimension: Build-vs-Buy Signal

### 0
The team already uses a high-level managed tool (Carbone, Aspose, Gotenberg, Spire.Office) that already solves the document problem, or the library is used so lightly that build-vs-buy doesn't meaningfully apply.

### 1
Mostly using higher-level, managed tools with a small amount of custom glue around them.

### 2
A genuine mix: some off-the-shelf tooling, some custom code doing real work.

### 3
Mostly custom, built directly on lower-level libraries (python-docx, PDFBox, pdf-lib) rather than a managed document engine.

### 4
Fully custom pipeline assembled from primitives, no managed document tool anywhere in the stack.

### 5
Fully custom, and the pipeline duplicates something SuperDocs already does today. This is the clearest possible version of "this team is building what we sell."

## 9. Dimension: Commercial Leverage

### 0
A single individual's personal project, no company identifiable at all.

### 1
A small internal tool built for one, non-platform organization.

### 2
A single organization, but a real, sizeable business, not a hobbyist or student project.

### 3
Some multi-tenant signal exists, but the scale or customer count is unclear.

### 4
A clear SaaS or platform product serving multiple named or clearly implied customers.

### 5
A clear SaaS or platform serving many customers, where a single SuperDocs integration would reach all of them at once, stated explicitly in the README or website.

## 10. Weights

| Dimension | Weight |
|---|---:|
| Document Volume | 15% |
| Document Complexity | 15% |
| Business Criticality | 20% |
| Pipeline Complexity | 20% |
| Maintenance Burden | 15% |
| Build-vs-Buy Signal | 10% |
| Commercial Leverage | 5% |

That's 100%.

**Why these weights and not equal weights across all seven.** The business hypothesis is explicit about what actually matters: high volume, complex formatting, business-critical documents, and significant custom processing code are the strongest signals, and a single dependency on its own is weak. Business Criticality and Pipeline Complexity get the top weight for that reason, together they're the difference between "this repo imports a document library" and "this is a company running an actual document workflow that costs them engineering time." Both are also the hardest dimensions to fake, since their top rungs require confirmed code usage and explicit business framing, not just a library being present.

Document Volume and Document Complexity sit just below that, since they matter but are secondary to whether the workflow is even real and whether it's tied to something the business depends on.

Maintenance Burden is weighted at 15% even though it defaults to 0 for most candidates in a first pass (see section 12). That's deliberate: it's arguably the single most direct proxy for "expensive to maintain," which is the actual thesis of the business hypothesis, but the evidence for it is expensive to gather (it needs commit history, not just a code search hit). Weighting it meaningfully, rather than dropping it to save the score from being dragged down, keeps the incentive to actually go collect that evidence for candidates worth the extra look, instead of quietly treating it as optional.

Build-vs-Buy Signal gets 10%, since it's partly a restatement of Pipeline Complexity and Maintenance Burden from a different angle (custom versus managed), so giving it full weight would double-count the same underlying evidence.

Commercial Leverage gets the smallest weight, 5%. It answers "how big would the win be if this is a real prospect," not "is this a real prospect at all." A single large hospital system with enormous volume and criticality shouldn't be buried by a small SaaS platform just because the platform serves more logos, so leverage is treated as a modest addition, not a gate.

## 11. Final score

For a candidate that has passed qualification (see section 14):

```
raw_weighted_score = sum(dimension_score_i * weight_i)
```

where each `dimension_score_i` is the 0-5 rubric score from sections 3 through 9, and each `weight_i` is the decimal form of the percentages in section 10 (0.15, 0.15, 0.20, 0.20, 0.15, 0.10, 0.05). Since the weights sum to 1.0 and each dimension score maxes at 5, `raw_weighted_score` ranges from 0 to 5.

```
final_score = round((raw_weighted_score / 5) * 100)
```

`round` here means conventional half-up rounding to the nearest integer: a
value ending in exactly .5 rounds away from zero, so 46.5 becomes 47. This is
worth stating because it is *not* what several languages do by default. Python's
built-in `round` uses banker's rounding, which breaks a tie toward the nearest
even integer and would turn 46.5 into 46 but 47.5 into 48. Leaving the mode
unstated would let two correct-looking implementations disagree by a point, and
a reader checking the arithmetic by hand will round half up.

This rescales to a 0-100 range purely for readability in the ranked table. The qualification gate in section 14 is applied after this calculation, as a cap, not folded into the formula itself, so the arithmetic here stays simple and auditable on its own.

## 12. Unknown evidence

An unknown dimension scores 0, not a middle value like 2 or 3, and it is not dropped from the weighted average either. Two alternatives were considered and rejected:

- **Treating unknown as a neutral middle score** would mean a candidate benefits from evidence nobody bothered to collect, which rewards an incomplete research pass over a thorough one.
- **Dropping unknown dimensions and redistributing the remaining weight** would let a candidate score well by only having evidence gathered for its most flattering dimensions, since the weight that would have gone to an unresearched dimension quietly flows to the ones that were checked.

Scoring unknown as 0 means missing evidence never helps a candidate's score, it can only hold it back, which matches the evidence-first principle the schema was built on: nothing counts unless it's backed by an `evidence_url`. The tradeoff is that a genuinely strong candidate can end up under-scored simply because nobody pulled its commit history yet. That's an acceptable cost, and it's exactly what section 13 exists to make visible rather than hide.

## 13. Confidence

Confidence is tracked separately from `final_score` and never adjusts it. It's computed from how many of the seven dimensions actually had direct evidence behind their score, as opposed to defaulting to 0 for being unknown:

- **High confidence**: 6 or 7 of the 7 dimensions have direct evidence, **and** the qualification `confidence` field from candidate-schema.md is also high.
- **Medium confidence**: 4 or 5 of the 7 dimensions have direct evidence, **or** 6 or 7 dimensions have direct evidence but the qualification `confidence` field is not high.
- **Low confidence**: 3 or fewer dimensions have direct evidence, **or** the qualification `confidence` field is low.

The second clause on the medium band matters more than it looks: a well-evidenced candidate whose *qualification* was itself a close call should not inherit high confidence from its dimension count alone. That is the EstateProposal case in section 15, where 6 of 7 dimensions are evidenced but the candidate only reached `investigate`, and the band is therefore medium rather than high.

The reason to keep this separate rather than folding it into the score: a candidate can legitimately score high on only 3 or 4 dimensions if those happen to be the highest-weighted ones (Business Criticality and Pipeline Complexity alone are 40% of the total), and that's a real, defensible score, but it's also a score built on less checking than one where all 7 dimensions were evidenced. The ranked table should show both columns side by side, so a reviewer can prioritize high-score, high-confidence candidates first, and treat high-score, low-confidence candidates as "worth a closer look before trusting the number," rather than treating every 80 the same way.

## 14. Qualification gate

Scoring only ever runs on candidates with `qualification_status` of keep or investigate. Reject candidates are excluded before this section applies at all, that's the hard rule, and no score can override it.

Within keep and investigate, three further conditions cap how high `final_score` can go, regardless of what the weighted math produces. These exist specifically to stop a repository from scoring well purely by listing a lot of document libraries:

- If `code_usage_confirmed` = false (every dependency hit was manifest-only, nothing was ever actually imported or invoked in code), `final_score` is capped at 20, no matter what the dimension scores say.
- If `document_functionality_in_production_code` = false (the document code only lives in /examples, /test, /scripts, or /demo), `final_score` is capped at 25.
- If `category_count` = 1 and `infrastructure_service_present` = false (a single library, used in isolation, nothing else in the pipeline), `final_score` is capped at 40. A single library can still be a real, valuable signal in a genuinely critical business, but it shouldn't be able to outrank a repository showing an actual multi-step, multi-library pipeline just because its one dimension scores happened to be higher.

These caps apply after the weighted calculation in section 11, they don't change the math, they just put a ceiling on what the number is allowed to say.

## 15. Synthetic examples

**SYNTHETIC EXAMPLE — NOT REAL DATA** (all three below)

### Example 1: High-potential candidate — "MedReport Solutions"

A fictional diagnostic-report SaaS. `qualification_status: keep`. Pipeline confirmed as: pull lab result data, populate a docxtpl template, convert through a deployed Gotenberg service, deliver to a patient portal. README states it processes results for multiple partner labs at meaningful volume.

| Dimension | Score | Weight | Weighted |
|---|---:|---:|---:|
| Document Volume | 4 | 0.15 | 0.60 |
| Document Complexity | 5 | 0.15 | 0.75 |
| Business Criticality | 5 | 0.20 | 1.00 |
| Pipeline Complexity | 5 | 0.20 | 1.00 |
| Maintenance Burden | 4 | 0.15 | 0.60 |
| Build-vs-Buy Signal | 4 | 0.10 | 0.40 |
| Commercial Leverage | 5 | 0.05 | 0.25 |

raw_weighted_score = 4.60 -> final_score = round((4.60 / 5) * 100) = **92**
Confidence: all 7 dimensions directly evidenced -> **high**
No gate caps apply (code_usage_confirmed = true, document_functionality_in_production_code = true, category_count = 3).

### Example 2: Medium-potential candidate — "EstateProposal"

A fictional single real-estate brokerage's internal proposal generator, built on docxtpl and WeasyPrint. `qualification_status: investigate`, since the business framing is clear but a couple of dimensions weren't fully evidenced.

| Dimension | Score | Weight | Weighted |
|---|---:|---:|---:|
| Document Volume | 2 | 0.15 | 0.30 |
| Document Complexity | 3 | 0.15 | 0.45 |
| Business Criticality | 3 | 0.20 | 0.60 |
| Pipeline Complexity | 3 | 0.20 | 0.60 |
| Maintenance Burden | 0 (unknown) | 0.15 | 0.00 |
| Build-vs-Buy Signal | 3 | 0.10 | 0.30 |
| Commercial Leverage | 1 | 0.05 | 0.05 |

raw_weighted_score = 2.30 -> final_score = round((2.30 / 5) * 100) = **46**
Confidence: 6 of 7 dimensions evidenced (maintenance_burden unknown) -> **medium**
No gate caps apply, but the 0 on Maintenance Burden is visibly costing this candidate 15 weighted points it could earn back if commit history were pulled.

### Example 3: Low-potential candidate — "docutils-sandbox"

A fictional personal repository containing short standalone example scripts for python-docx, pypdf, reportlab, and docxtpl, four library-universe entries in one requirements.txt. No application code, no README product description, everything lives under /examples.

Before scoring even applies: `readme_describes_product` = false, `application_code_exists` = false, `document_functionality_in_production_code` = false. Under the rules in candidate-schema.md section 7, this pattern matches `rejection_reason: tutorial_or_demo`.

`qualification_status: reject`.

This candidate never reaches section 15's scoring table at all. It has four document libraries in its manifest, more than either MedReport Solutions or EstateProposal individually declare, but qualification stops it before the weighted formula ever runs. If someone tried to score it anyway against the rubrics above, it would land near 0 on Business Criticality, Pipeline Complexity, and Commercial Leverage regardless, since none of those rubrics award points for dependency count alone. The rejection is the more honest outcome: it stops the comparison from happening rather than producing a low number that still tempts someone to compare it to a real candidate.

## 16. Anti-gaming / anti-noise rules

Nothing about this model lets a repository win on dependency count by itself. That's enforced in four separate places, not just one, so gaming the model would mean beating all four at once:

**The qualification gate runs first.** A repository that's a toolkit, a tutorial, or a fork never reaches scoring at all, regardless of how many libraries it imports. This is section 14's job, and it's a hard stop, not a score penalty.

**The two highest-weighted dimensions require confirmed code usage and real business framing, not presence.** Business Criticality (20%) and Pipeline Complexity (20%) both cap out low unless `code_usage_confirmed` = true and there's actual evidence of a business behind the repository. A pile of manifest-only dependencies can't move either of these past their bottom rungs.

**Document Complexity requires confirmation, not just count.** `category_count` alone only gets a candidate to a 2 on that dimension's rubric (section 4). Reaching a 3 or higher requires `multiple_document_types_handled` = true and confirmed code usage across the categories, so simply listing more libraries in a requirements file doesn't climb the rubric on its own.

**Unknown scores as 0, not neutral.** Section 12 already covers this, but it's an anti-gaming rule as much as an evidence rule: a candidate can't inflate its score by having evidence collected only for the dimensions that happen to look good and leaving the rest unresearched, since unresearched costs points rather than being invisible.

Put together, the "generic toolkit repository with four impressive-looking imports" scenario from the earlier discussion is handled twice over: first by the qualification gate, which should catch it as tutorial_or_demo before it's ever scored, and second, even if it somehow slipped through qualification, by Business Criticality and Pipeline Complexity both defaulting low without confirmed, in-production code usage. A smaller SaaS repository generating real contracts every day, even with fewer total libraries, wins on both of those dimensions specifically because the evidence behind it is stronger, not because of anything to do with how many packages its requirements.txt lists.

## 17. Open questions

- Should weights vary by industry vertical? A single large hospital system or law firm can represent a bigger opportunity than a mid-sized SaaS platform with more logos, and the current 5% weight on Commercial Leverage may undervalue that kind of single-organization deal. Worth revisiting once real candidates come in and this gets tested against actual judgment calls.
- Should there be a minimum evidence_trail size (from candidate-schema.md section 9) required before a candidate is eligible for keep, independent of the score, so a candidate can't reach a high final_score on the strength of very few evidence entries even if those entries happen to hit the high-weighted dimensions?
- The 0-5 scale per dimension is coarse. It's likely to produce a cluster of mid-tier candidates all landing in a similar final_score band, which would make the ranked table less useful exactly where it matters most, in the middle of the list rather than at the extremes. Half-point increments would help, at the cost of making each rubric rung harder to define crisply.
- Right now Maintenance Burden defaults to 0 for most candidates because commit history usually isn't pulled in a first pass. Once that becomes cheap enough to gather for every keep/investigate candidate, this dimension's typical score will shift, and the weights in section 10 may need a second look once that data actually exists instead of being mostly absent.
- The qualification gate's caps in section 14 (20, 25, 40) are round numbers chosen for legibility, not derived from anything. Worth treating them as a first guess to be adjusted once a real batch of candidates shows whether they're too strict or too lenient in practice.
