# Dependency Map - run_2

## Executive summary

- Discovery runs recorded: **2**
- Discovery queries executed: **237**
  - Capped (exceeded GitHub's 1,000-result ceiling): **75**
  - Zero-result: **27**
  - Failed (no total recorded): **0**
- Raw discovery hits (API results, before dedup): **5587**
- Unique repositories discovered: **4214**
- Qualification: keep **46**, investigate **173**, reject **281**
- Scored candidates (keep or investigate with a score): **219**
- Candidates with enhanced maintenance-burden evidence: **0** (the phase 14 targeted commit-history pass has not run yet; `maintenance_burden` defaults to unknown for every candidate)

Raw hits and unique repositories are different numbers on purpose: several queries, or several file matches within one query, can all point at the same repository. The gap between them is deduplication working, not an error.

## Coverage and sampling (run_2)

Every number in this section describes **run_2 only**. Totals across all runs are in the cumulative section at the end.

- Repositories **surfaced by run_2**: **4,214**
  - Found for the first time by this run: **3,584**
  - Already seen by an earlier run: **630**
- Repositories **selected for evidence enrichment**: **500**
- Repositories with evidence collected but outside the official sample: **15**

**Where this run's evidence came from.** 630 of the repositories above were first found by an earlier run, so any evidence held for them may have been collected then rather than during this run. The database records which run first saw a candidate (`candidates.first_seen_run_id`); it does not timestamp each evidence row, so that first-sighting is the whole provenance available and nothing finer is claimed here.

**Every qualification, scoring and ranking number in this report describes the 500-repository evidence sample, not the 4,214 repositories surfaced by run_2.** The remaining 3,714 were surfaced by a discovery query and stored, but no evidence was collected for them and they were never qualified, scored or ranked. They are absent from the results because they were not examined, which is not the same as having been examined and found wanting.

### How the sample was selected

The sample is deterministic and stratified by discovery tier, so it can be reproduced exactly from stored discovery data. A candidate's tier is the strongest (lowest) tier of any query that surfaced it; within a tier, candidates are ordered by `candidate_id` ascending and taken from the front.

| Tier | Selected |
|---|---:|
| 1 | 100 |
| 2 | 100 |
| 3 | 300 |
| **Total** | **500** |

`candidate_id` is a hash of the normalised repository URL, so the ordering depends only on repository identity, never on the order results happened to arrive in.

Because the sample is stratified rather than proportional, the tier mix here is not the tier mix of the discovery universe. Tier 1 and tier 2 are deliberately over-represented relative to their share of discovered repositories, so keep and reject rates quoted per tier should not be read as rates across all of GitHub.

> **Maintenance-burden evidence was enriched for a bounded, highest-ranked candidate set; candidates outside that set may still have unknown `maintenance_burden`.** 52 of the 219 ranked candidates below rest on collected source evidence for that dimension; the remaining 167 score 0 on it because it was never inspected, which is not a finding that their document code is thin. `maintenance_burden` carries 15 percent of the weight, so an un-enriched candidate is ranked below where its evidence might otherwise place it. Comparing a candidate inside the enriched set against one outside it compares different amounts of collection.

## Ranked table

Sorted by score, highest first. Ties break on confidence (high, then medium, then low), then on candidate id, so the order is reproducible from the same data.

| Rank | Repository | Company | Qualification | Score | Confidence | Evidence coverage | Unknown dimensions |
|---:|---|---|---|---:|---|---|---|
| 1 | [quarqlabs/argus](https://github.com/quarqlabs/argus) | — | keep | 61/100 | high | 7/7 | none |
| 2 | [LinuxPlumbersConf/indico](https://github.com/linuxplumbersconf/indico) | — | investigate | 51/100 | medium | 6/7 | Commercial leverage |
| 3 | [B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making](https://github.com/b253500/llm-agents-to-automate-vc-intelligence-and-deal-making) | — | keep | 50/100 | medium | 7/7 | none |
| 4 | [dynamiq-ai/dynamiq](https://github.com/dynamiq-ai/dynamiq) | — | investigate | 48/100 | medium | 7/7 | none |
| 5 | [Upsonic/Upsonic](https://github.com/upsonic/upsonic) | — | investigate | 47/100 | medium | 6/7 | Commercial leverage |
| 6 | [LegalQuants/lq-ai](https://github.com/legalquants/lq-ai) | — | keep | 44/100 | high | 6/7 | Commercial leverage |
| 7 | [sbrunner/scan-to-paperless](https://github.com/sbrunner/scan-to-paperless) | — | investigate | 44/100 | medium | 6/7 | Commercial leverage |
| 8 | [llv22/camel_forward](https://github.com/llv22/camel_forward) | — | investigate | 43/100 | medium | 6/7 | Commercial leverage |
| 9 | [PapiHack/document-templating-service](https://github.com/papihack/document-templating-service) | — | investigate | 43/100 | medium | 6/7 | Commercial leverage |
| 10 | [UKGovernmentBEIS/inspect_evals](https://github.com/ukgovernmentbeis/inspect_evals) | — | keep | 41/100 | high | 7/7 | none |
| 11 | [pbl-nl/appl-docchat](https://github.com/pbl-nl/appl-docchat) | — | investigate | 41/100 | medium | 6/7 | Commercial leverage |
| 12 | [abgulati/LARS](https://github.com/abgulati/lars) | — | investigate | 41/100 | medium | 7/7 | none |
| 13 | [ilee165/network-infrastructure-ai-platform](https://github.com/ilee165/network-infrastructure-ai-platform) | — | keep | 40/100 | high | 7/7 | none |
| 14 | [FERAL-AI/FERAL-AI](https://github.com/feral-ai/feral-ai) | — | keep | 40/100 | high | 7/7 | none |
| 15 | [AmrasElessar/adminpdftoolkit](https://github.com/amraselessar/adminpdftoolkit) | — | keep | 40/100 | high | 7/7 | none |
| 16 | [AnujaK/restfiddle](https://github.com/anujak/restfiddle) | BootSimply Solutions  Licensed | keep | 40/100 | high | 7/7 | none |
| 17 | [shehanrathnayake/checkpoint-pos-system](https://github.com/shehanrathnayake/checkpoint-pos-system) | — | keep | 40/100 | high | 7/7 | none |
| 18 | [jolie-z/Auto-JobHunter](https://github.com/jolie-z/auto-jobhunter) | — | keep | 40/100 | high | 7/7 | none |
| 19 | [anki291103/Event4U](https://github.com/anki291103/event4u) | — | keep | 40/100 | medium | 7/7 | none |
| 20 | [TuiQiao/CBoard](https://github.com/tuiqiao/cboard) | — | keep | 40/100 | medium | 7/7 | none |
| 21 | [pandora-analysis/pandora](https://github.com/pandora-analysis/pandora) | — | investigate | 40/100 | medium | 6/7 | Commercial leverage |
| 22 | [nhiney/database-security](https://github.com/nhiney/database-security) | — | keep | 40/100 | medium | 7/7 | none |
| 23 | [vectara/vectara-ingest](https://github.com/vectara/vectara-ingest) | — | keep | 40/100 | medium | 6/7 | Document volume |
| 24 | [Ubada-Hussain/FormFixer](https://github.com/ubada-hussain/formfixer) | — | keep | 38/100 | high | 7/7 | none |
| 25 | [OpsinTech/opsintech-platform](https://github.com/opsintech/opsintech-platform) | — | investigate | 38/100 | medium | 7/7 | none |
| 26 | [hereugo-ak/Hyperion](https://github.com/hereugo-ak/hyperion) | HYPERION Consulting | investigate | 38/100 | medium | 7/7 | none |
| 27 | [openai/GABRIEL](https://github.com/openai/gabriel) | — | investigate | 37/100 | medium | 6/7 | Commercial leverage |
| 28 | [seepick/gadsu](https://github.com/seepick/gadsu) | — | keep | 36/100 | medium | 7/7 | none |
| 29 | [Cyberwatch/Pentest-Collaboration-Framework](https://github.com/cyberwatch/pentest-collaboration-framework) | — | investigate | 36/100 | medium | 6/7 | Commercial leverage |
| 30 | [ghk/sideka-electron](https://github.com/ghk/sideka-electron) | — | keep | 35/100 | medium | 7/7 | none |
| 31 | [keystrokehq/keystroke](https://github.com/keystrokehq/keystroke) | — | keep | 34/100 | high | 7/7 | none |
| 32 | [302ai/302_resume](https://github.com/302ai/302_resume) | — | keep | 34/100 | medium | 7/7 | none |
| 33 | [aws-amplify/docs](https://github.com/aws-amplify/docs) | — | keep | 33/100 | high | 7/7 | none |
| 34 | [webxos/phalanx](https://github.com/webxos/phalanx) | — | keep | 33/100 | high | 7/7 | none |
| 35 | [activepieces/activepieces](https://github.com/activepieces/activepieces) | — | keep | 33/100 | high | 7/7 | none |
| 36 | [buzzqw/NotePadPQ](https://github.com/buzzqw/notepadpq) | — | keep | 33/100 | medium | 6/7 | Commercial leverage |
| 37 | [kartoza/docker-mezzanine](https://github.com/kartoza/docker-mezzanine) | — | investigate | 33/100 | medium | 6/7 | Commercial leverage |
| 38 | [metorial/metorial](https://github.com/metorial/metorial) | — | keep | 32/100 | high | 7/7 | none |
| 39 | [watat83/document-chat-system](https://github.com/watat83/document-chat-system) | — | investigate | 32/100 | medium | 7/7 | none |
| 40 | [kamkahou/ragflow-0.17.2](https://github.com/kamkahou/ragflow-0.17.2) | — | investigate | 32/100 | medium | 7/7 | none |
| 41 | [shivama205/DocBrain](https://github.com/shivama205/docbrain) | — | investigate | 32/100 | medium | 7/7 | none |
| 42 | [stella/stella](https://github.com/stella/stella) | — | keep | 30/100 | high | 7/7 | none |
| 43 | [ceskaexpedice/kramerius](https://github.com/ceskaexpedice/kramerius) | — | investigate | 30/100 | medium | 6/7 | Commercial leverage |
| 44 | [CyberCX-STA/PurpleOps](https://github.com/cybercx-sta/purpleops) | — | investigate | 30/100 | medium | 6/7 | Commercial leverage |
| 45 | [Aleks-Ya/yaal_examples](https://github.com/aleks-ya/yaal_examples) | — | investigate | 30/100 | medium | 6/7 | Commercial leverage |
| 46 | [FikrahFathoniSiregar/Auto-Report](https://github.com/fikrahfathonisiregar/auto-report) | — | investigate | 30/100 | medium | 6/7 | Commercial leverage |
| 47 | [ngs-doo/TemplaterExamples](https://github.com/ngs-doo/templaterexamples) | — | keep | 29/100 | medium | 7/7 | none |
| 48 | [PipedreamHQ/pipedream](https://github.com/pipedreamhq/pipedream) | — | keep | 28/100 | high | 6/7 | Maintenance burden |
| 49 | [simpledms/simpledms](https://github.com/simpledms/simpledms) | — | keep | 27/100 | high | 7/7 | none |
| 50 | [iondv/registry](https://github.com/iondv/registry) | — | keep | 27/100 | medium | 6/7 | Commercial leverage |
| 51 | [bashly-framework/bashly](https://github.com/bashly-framework/bashly) | — | keep | 26/100 | high | 7/7 | none |
| 52 | [ShirleyBailey/ragflow](https://github.com/shirleybailey/ragflow) | — | investigate | 26/100 | medium | 6/7 | Maintenance burden |
| 53 | [liferay/liferay-portal](https://github.com/liferay/liferay-portal) | Liferay | keep | 26/100 | medium | 7/7 | none |
| 54 | [paunchygent/skriptoteket](https://github.com/paunchygent/skriptoteket) | — | keep | 25/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 55 | [microsoft/powerplatform-vscode](https://github.com/microsoft/powerplatform-vscode) | — | keep | 25/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 56 | [jreyesr/n8n-nodes-carbonejs](https://github.com/jreyesr/n8n-nodes-carbonejs) | — | keep | 24/100 | high | 7/7 | none |
| 57 | [yashiroots-school/School](https://github.com/yashiroots-school/school) | — | investigate | 24/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 58 | [PaNGalaxy/galaxy](https://github.com/pangalaxy/galaxy) | — | investigate | 24/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 59 | [34j/decryptpdf](https://github.com/34j/decryptpdf) | — | investigate | 24/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 60 | [vasilistotskas/grooveshop-django-api](https://github.com/vasilistotskas/grooveshop-django-api) | — | investigate | 24/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 61 | [fossasia/eventyay](https://github.com/fossasia/eventyay) | — | keep | 23/100 | medium | 6/7 | Maintenance burden |
| 62 | [DSPaul/COMPASS](https://github.com/dspaul/compass) | — | keep | 23/100 | medium | 6/7 | Maintenance burden |
| 63 | [WNormanTPN/HotelManagement](https://github.com/wnormantpn/hotelmanagement) | — | investigate | 23/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 64 | [symfony/webpack-encore](https://github.com/symfony/webpack-encore) | Symfony | investigate | 23/100 | medium | 6/7 | Maintenance burden |
| 65 | [robusta-dev/robusta](https://github.com/robusta-dev/robusta) | — | keep | 23/100 | medium | 6/7 | Maintenance burden |
| 66 | [cuba-platform/yarg](https://github.com/cuba-platform/yarg) | Haulmont | investigate | 23/100 | medium | 6/7 | Maintenance burden |
| 67 | [Kavithma-Thushal/Computershop-Management-System-1st-Sem-Final](https://github.com/kavithma-thushal/computershop-management-system-1st-sem-final) | — | investigate | 23/100 | medium | 6/7 | Maintenance burden |
| 68 | [QuivrHQ/MegaParse](https://github.com/quivrhq/megaparse) | — | investigate | 22/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 69 | [City-of-Helsinki/kaavapino](https://github.com/city-of-helsinki/kaavapino) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 70 | [xkevio/Creasy](https://github.com/xkevio/creasy) | — | keep | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 71 | [beenuar/AiSOC](https://github.com/beenuar/aisoc) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 72 | [Friday-Labs-Inc/friday](https://github.com/friday-labs-inc/friday) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 73 | [pinussilvestrus/postit-js](https://github.com/pinussilvestrus/postit-js) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 74 | [jerry609/PaperBot](https://github.com/jerry609/paperbot) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 75 | [dfir-iris/docx-generator](https://github.com/dfir-iris/docx-generator) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 76 | [zhangzhen1979/JIMU-ConvertPreview](https://github.com/zhangzhen1979/jimu-convertpreview) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 77 | [auchenberg/vscode-browser-preview](https://github.com/auchenberg/vscode-browser-preview) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 78 | [athola/simple-resume](https://github.com/athola/simple-resume) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 79 | [tghfly/grafana-chinese](https://github.com/tghfly/grafana-chinese) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 80 | [jpmorganchase/modular](https://github.com/jpmorganchase/modular) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 81 | [Verivox/lighthouse-monitor](https://github.com/verivox/lighthouse-monitor) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 82 | [UST-QuAntiL/latex-renderer](https://github.com/ust-quantil/latex-renderer) | — | keep | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 83 | [javadev/jasper-xml-to-pdf-generator](https://github.com/javadev/jasper-xml-to-pdf-generator) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 84 | [xcmt/ABC_report](https://github.com/xcmt/abc_report) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 85 | [qwc-services/jasper-reporting-service](https://github.com/qwc-services/jasper-reporting-service) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 86 | [wso2/carbon-commons](https://github.com/wso2/carbon-commons) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 87 | [Azure-Samples/healthcare-agent-orchestrator](https://github.com/azure-samples/healthcare-agent-orchestrator) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 88 | [AIGeniusInstitue/restfeel](https://github.com/aigeniusinstitue/restfeel) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 89 | [zorazrw/odex](https://github.com/zorazrw/odex) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 90 | [lincolnluiz/SpringBoot-JasperReports](https://github.com/lincolnluiz/springboot-jasperreports) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 91 | [gooderp-study/GoodERP](https://github.com/gooderp-study/gooderp) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 92 | [davidkey/DynamicJasperExample](https://github.com/davidkey/dynamicjasperexample) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 93 | [zkoss/zk](https://github.com/zkoss/zk) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 94 | [Lawyer-ray/FachuanHybridSystem](https://github.com/lawyer-ray/fachuanhybridsystem) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 95 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/skill_seekers) | — | investigate | 20/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 96 | [bigbeartechworld/big-bear-casaos](https://github.com/bigbeartechworld/big-bear-casaos) | BigBearTechWorld | investigate | 20/100 | medium | 6/7 | Maintenance burden |
| 97 | [rsrdesarrollo/sarna](https://github.com/rsrdesarrollo/sarna) | — | investigate | 20/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 98 | [lr101/homelab](https://github.com/lr101/homelab) | — | investigate | 20/100 | medium | 6/7 | Maintenance burden |
| 99 | [RCGAI/SimplyRetrieve](https://github.com/rcgai/simplyretrieve) | — | investigate | 20/100 | low | 5/7 | Pipeline complexity, Maintenance burden |
| 100 | [convertigo/convertigo](https://github.com/convertigo/convertigo) | — | investigate | 19/100 | medium | 6/7 | Maintenance burden |
| 101 | [iiitdwd-exams/certificates](https://github.com/iiitdwd-exams/certificates) | — | investigate | 19/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 102 | [Mihir-Rabari/inboxfm-connect](https://github.com/mihir-rabari/inboxfm-connect) | — | keep | 19/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 103 | [datawizz/Openpieces](https://github.com/datawizz/openpieces) | — | keep | 19/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 104 | [zgsm-ai/costrict](https://github.com/zgsm-ai/costrict) | Sangfor | investigate | 18/100 | medium | 5/7 | Document volume, Maintenance burden |
| 105 | [Websoft9/docker-library](https://github.com/websoft9/docker-library) | — | investigate | 18/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 106 | [runtipi/runtipi-appstore](https://github.com/runtipi/runtipi-appstore) | — | investigate | 18/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 107 | [dendianugerah/reubah](https://github.com/dendianugerah/reubah) | — | investigate | 18/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 108 | [bigcapitalhq/bigcapital](https://github.com/bigcapitalhq/bigcapital) | — | keep | 17/100 | high | 6/7 | Maintenance burden |
| 109 | [infonl/dimpact-zaakafhandelcomponent](https://github.com/infonl/dimpact-zaakafhandelcomponent) | Atos | keep | 17/100 | high | 6/7 | Maintenance burden |
| 110 | [airens/interactive_brokers_tax](https://github.com/airens/interactive_brokers_tax) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 111 | [Cinnamon/kotaemon](https://github.com/cinnamon/kotaemon) | — | investigate | 17/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 112 | [bbossgroups/bboss](https://github.com/bbossgroups/bboss) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 113 | [miyabayt/spring-boot-doma2-sample](https://github.com/miyabayt/spring-boot-doma2-sample) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 114 | [dahatake/HypervelocityEngineering](https://github.com/dahatake/hypervelocityengineering) | — | investigate | 17/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 115 | [FerGusMosca/Quant_ML_Research_Platform](https://github.com/fergusmosca/quant_ml_research_platform) | — | investigate | 17/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 116 | [healthonrails/annolid](https://github.com/healthonrails/annolid) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 117 | [codion-is/codion](https://github.com/codion-is/codion) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 118 | [wocommunity/wonder](https://github.com/wocommunity/wonder) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 119 | [BearMelon/thomaslo](https://github.com/bearmelon/thomaslo) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 120 | [basxsoftwareassociation/bread](https://github.com/basxsoftwareassociation/bread) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 121 | [elapouya/python-docx-template](https://github.com/elapouya/python-docx-template) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 122 | [SuffolkLITLab/docassemble-ALWeaver](https://github.com/suffolklitlab/docassemble-alweaver) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 123 | [OParl/spec](https://github.com/oparl/spec) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 124 | [GUMGA/frameworkbackend](https://github.com/gumga/frameworkbackend) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 125 | [Swiss-Armed-Forces/Loom](https://github.com/swiss-armed-forces/loom) | — | keep | 17/100 | medium | 6/7 | Maintenance burden |
| 126 | [GUMGA/framework-backend](https://github.com/gumga/framework-backend) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 127 | [adfinis/document-merge-service](https://github.com/adfinis/document-merge-service) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 128 | [dkratzert/FinalCif](https://github.com/dkratzert/finalcif) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 129 | [fitercanary/fineract-template](https://github.com/fitercanary/fineract-template) | — | investigate | 17/100 | low | 5/7 | Pipeline complexity, Maintenance burden |
| 130 | [psi-oss/get-physics-done](https://github.com/psi-oss/get-physics-done) | Physical Superintelligence PBC | investigate | 16/100 | medium | 5/7 | Document volume, Maintenance burden |
| 131 | [project-ryoma/ryoma](https://github.com/project-ryoma/ryoma) | — | investigate | 16/100 | medium | 5/7 | Document volume, Maintenance burden |
| 132 | [adcontextprotocol/adcp](https://github.com/adcontextprotocol/adcp) | — | investigate | 16/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 133 | [rte-france/wattelse](https://github.com/rte-france/wattelse) | — | investigate | 16/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 134 | [open-octo/octo-agent](https://github.com/open-octo/octo-agent) | — | investigate | 16/100 | medium | 5/7 | Document volume, Maintenance burden |
| 135 | [espoon-voltti/evaka](https://github.com/espoon-voltti/evaka) | — | investigate | 16/100 | medium | 5/7 | Document volume, Maintenance burden |
| 136 | [Pissaia92/chatbot-rag-autosservico](https://github.com/pissaia92/chatbot-rag-autosservico) | — | investigate | 16/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 137 | [stardustai/dataset-viewer](https://github.com/stardustai/dataset-viewer) | — | investigate | 16/100 | medium | 5/7 | Document volume, Maintenance burden |
| 138 | [readest/readest](https://github.com/readest/readest) | — | investigate | 16/100 | medium | 5/7 | Document volume, Maintenance burden |
| 139 | [open-mercato/open-mercato](https://github.com/open-mercato/open-mercato) | — | investigate | 16/100 | medium | 5/7 | Document volume, Maintenance burden |
| 140 | [huridocs/pdf-document-layout-analysis](https://github.com/huridocs/pdf-document-layout-analysis) | Alibaba Research Group | investigate | 15/100 | medium | 6/7 | Maintenance burden |
| 141 | [imarthe75/ades-nevadi](https://github.com/imarthe75/ades-nevadi) | — | investigate | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 142 | [azavea/raster-vision](https://github.com/azavea/raster-vision) | — | investigate | 15/100 | medium | 6/7 | Maintenance burden |
| 143 | [dalibo/pandocker](https://github.com/dalibo/pandocker) | — | investigate | 15/100 | medium | 6/7 | Maintenance burden |
| 144 | [carbon-design-system/carbon](https://github.com/carbon-design-system/carbon) | — | investigate | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 145 | [globalis-ms/carbone](https://github.com/globalis-ms/carbone) | — | investigate | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 146 | [gyselroth/balloon](https://github.com/gyselroth/balloon) | — | keep | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 147 | [dante-ev/docker-texlive](https://github.com/dante-ev/docker-texlive) | — | investigate | 15/100 | medium | 6/7 | Maintenance burden |
| 148 | [ad-on-is/rachoon](https://github.com/ad-on-is/rachoon) | — | keep | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 149 | [riclolsen/json-scada](https://github.com/riclolsen/json-scada) | — | investigate | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 150 | [DefinitelyTyped/DefinitelyTyped](https://github.com/definitelytyped/definitelytyped) | — | investigate | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 151 | [ZUGFeRD/mustangapi](https://github.com/zugferd/mustangapi) | — | investigate | 15/100 | low | 5/7 | Pipeline complexity, Maintenance burden |
| 152 | [jimmymnt/pim-e-shop](https://github.com/jimmymnt/pim-e-shop) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 153 | [CoJoA13/EasySynQ](https://github.com/cojoa13/easysynq) | — | investigate | 14/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 154 | [Simon-Drohsen/pimcore-certificate](https://github.com/simon-drohsen/pimcore-certificate) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 155 | [WPI-LNL/lnldb](https://github.com/wpi-lnl/lnldb) | — | investigate | 14/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 156 | [JanBancerewicz/pimcoretask](https://github.com/janbancerewicz/pimcoretask) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 157 | [datnv41001/pimcore](https://github.com/datnv41001/pimcore) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 158 | [LevDmitriev/dc-pimcore-demo](https://github.com/levdmitriev/dc-pimcore-demo) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 159 | [vivliostyle/vivliostyle-cli](https://github.com/vivliostyle/vivliostyle-cli) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 160 | [l4houx/recipe](https://github.com/l4houx/recipe) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 161 | [engine-public/engine-partner-api](https://github.com/engine-public/engine-partner-api) | — | investigate | 14/100 | low | 5/7 | Pipeline complexity, Maintenance burden |
| 162 | [PrimaverabssDeveloper/ERP10Extensibility](https://github.com/primaverabssdeveloper/erp10extensibility) | — | investigate | 13/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 163 | [networktocode/yangify](https://github.com/networktocode/yangify) | — | investigate | 13/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 164 | [gitrgoliveira/bracket-creator](https://github.com/gitrgoliveira/bracket-creator) | — | investigate | 13/100 | medium | 6/7 | Maintenance burden |
| 165 | [getumbrel/umbrel-apps](https://github.com/getumbrel/umbrel-apps) | — | investigate | 13/100 | medium | 6/7 | Maintenance burden |
| 166 | [Paparusi/legal-ai-agent](https://github.com/paparusi/legal-ai-agent) | — | investigate | 13/100 | medium | 6/7 | Maintenance burden |
| 167 | [LazyAGI/LazyLLM](https://github.com/lazyagi/lazyllm) | — | investigate | 12/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 168 | [sifter-ai/sifter](https://github.com/sifter-ai/sifter) | — | investigate | 12/100 | medium | 5/7 | Document volume, Maintenance burden |
| 169 | [Ganesh-403/semantic-plagiarism-detector](https://github.com/ganesh-403/semantic-plagiarism-detector) | — | investigate | 12/100 | low | 3/7 | Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal |
| 170 | [sitepoint-editors/awesome-symfony](https://github.com/sitepoint-editors/awesome-symfony) | — | investigate | 12/100 | low | 3/7 | Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal |
| 171 | [dragonfore4/deka-download](https://github.com/dragonfore4/deka-download) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 172 | [modrinth/code](https://github.com/modrinth/code) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 173 | [Probesys/lotemplate](https://github.com/probesys/lotemplate) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 174 | [MVladislav/vm-docker-collection](https://github.com/mvladislav/vm-docker-collection) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 175 | [ministryofjustice/send-legal-mail-to-prisons](https://github.com/ministryofjustice/send-legal-mail-to-prisons) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 176 | [notadev-iamaura/OneRAG](https://github.com/notadev-iamaura/onerag) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 177 | [solidtime-io/solidtime](https://github.com/solidtime-io/solidtime) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 178 | [unitedworldwrestling/arena-public](https://github.com/unitedworldwrestling/arena-public) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 179 | [YYC-Cube/YYC3-Knowledge-Base](https://github.com/yyc-cube/yyc3-knowledge-base) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 180 | [georgemarian98/home-server](https://github.com/georgemarian98/home-server) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 181 | [tjmlabs/ColiVara](https://github.com/tjmlabs/colivara) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 182 | [samvera/hydra-derivatives](https://github.com/samvera/hydra-derivatives) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 183 | [AppCivico/smae](https://github.com/appcivico/smae) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 184 | [mperreir/Hyblab2023](https://github.com/mperreir/hyblab2023) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 185 | [OPPO-PersonalAI/Agent-KB](https://github.com/oppo-personalai/agent-kb) | — | investigate | 10/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 186 | [khulnasoft/deepstack](https://github.com/khulnasoft/deepstack) | — | investigate | 10/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 187 | [paulgessinger/swift-paperless](https://github.com/paulgessinger/swift-paperless) | — | investigate | 9/100 | medium | 6/7 | Maintenance burden |
| 188 | [selkies-project/docker-selkies-glx-desktop](https://github.com/selkies-project/docker-selkies-glx-desktop) | — | investigate | 9/100 | medium | 6/7 | Maintenance burden |
| 189 | [mementoweb/SiteStory](https://github.com/mementoweb/sitestory) | — | investigate | 8/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 190 | [JoachimSchaeffer/AttackSelection](https://github.com/joachimschaeffer/attackselection) | — | investigate | 8/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 191 | [makinacorpus/convertit](https://github.com/makinacorpus/convertit) | — | investigate | 7/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 192 | [octos-org/octos](https://github.com/octos-org/octos) | — | investigate | 7/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 193 | [CitizenLabDotCo/citizenlab](https://github.com/citizenlabdotco/citizenlab) | — | investigate | 7/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 194 | [AtlasOfLivingAustralia/fieldcapture](https://github.com/atlasoflivingaustralia/fieldcapture) | — | investigate | 5/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 195 | [isle-project/isle-editor](https://github.com/isle-project/isle-editor) | — | investigate | 5/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 196 | [archerysec/archerysec](https://github.com/archerysec/archerysec) | — | investigate | 5/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 197 | [Scouterna/skojjt](https://github.com/scouterna/skojjt) | — | investigate | 5/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 198 | [philips-software/amp-devcontainer](https://github.com/philips-software/amp-devcontainer) | — | investigate | 5/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 199 | [RedPlanetHQ/core](https://github.com/redplanethq/core) | — | investigate | 4/100 | low | 4/7 | Document volume, Pipeline complexity, Maintenance burden |
| 200 | [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) | — | investigate | 4/100 | low | 4/7 | Document volume, Pipeline complexity, Maintenance burden |
| 201 | [DirectumCompany/rx-util-importdata](https://github.com/directumcompany/rx-util-importdata) | — | investigate | 3/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 202 | [Kentico/xperience-by-kentico-kentico-migration-tool](https://github.com/kentico/xperience-by-kentico-kentico-migration-tool) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 203 | [Hitendra-Cyber/Data-Guard](https://github.com/hitendra-cyber/data-guard) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 204 | [AIE-enginehub/personERP-SERVER](https://github.com/aie-enginehub/personerp-server) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 205 | [kvcache-ai/TrEnv-X](https://github.com/kvcache-ai/trenv-x) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 206 | [coderfolks/Rccs](https://github.com/coderfolks/rccs) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 207 | [hisachin/chathive](https://github.com/hisachin/chathive) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 208 | [janderswag/docuchat.app](https://github.com/janderswag/docuchat.app) | — | investigate | 2/100 | low | 2/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal |
| 209 | [dundalek/closh](https://github.com/dundalek/closh) | — | investigate | 2/100 | low | 2/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal |
| 210 | [iltoga/BusinessSuite](https://github.com/iltoga/businesssuite) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 211 | [remacs/remacs](https://github.com/remacs/remacs) | Free Software Foundation | investigate | 2/100 | low | 2/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal |
| 212 | [rapid7/nexpose-warehouse-jasper-templates](https://github.com/rapid7/nexpose-warehouse-jasper-templates) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 213 | [fiyo/DBCheck](https://github.com/fiyo/dbcheck) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 214 | [koskasmail/whatAmess](https://github.com/koskasmail/whatamess) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 215 | [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 216 | [ryumada/docker-odoo](https://github.com/ryumada/docker-odoo) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 217 | [ebongard/renfield](https://github.com/ebongard/renfield) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 218 | [receipt-print-hq/escpos-tools](https://github.com/receipt-print-hq/escpos-tools) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 219 | [TurtleTech-ehf/snapper](https://github.com/turtletech-ehf/snapper) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |

## Candidate details

### 1. quarqlabs/argus

**Repository / product**

- Repository: [https://github.com/quarqlabs/argus](https://github.com/quarqlabs/argus)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=2, pipeline_stage_count=3 \| supporting: category_count=2; multiple_document_types_handled=true; pipeline_stage_count=3; template_directory_present=true; confirmed generation/conversion code

**Score**

- Score: 61/100 (a score, not a probability)
- Raw weighted score: 3.05 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 3 |
| Business criticality | 2 |
| Pipeline complexity | 3 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 4 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:2001..4000`, rank 8
  - Query: `"PyMuPDF" filename:requirements.txt size:2001..4000`
  - Sampled 30 of 5,296 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 5,296 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_2`, window `size:2001..4000`, rank 7
  - Query: `"python-docx" filename:requirements.txt size:2001..4000`
  - Sampled 30 of 6,224 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 6,224 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [requirements.txt](https://github.com/quarqlabs/argus/blob/main/requirements.txt)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/quarqlabs/argus/blob/b56a9bc73ef3676a343dcc90a8103c024c9449a3/local_channel_store.py)
- `python-docx` (docx, generation) — manifest_declaration — [requirements.txt](https://github.com/quarqlabs/argus/blob/main/requirements.txt)
- `python-docx` (docx, generation) — code_import — [code](https://github.com/quarqlabs/argus/blob/b56a9bc73ef3676a343dcc90a8103c024c9449a3/local_channel_store.py)

**Evidence trail**

- [api_response](https://github.com/quarqlabs/argus) (source: github_api): stars=273, fork=False, archived=False
- [manifest_line](https://github.com/quarqlabs/argus/blob/main/requirements.txt) (source: github_api): PyMuPDF>=1.24.0,<2.0.0
- [code_permalink](https://github.com/quarqlabs/argus/blob/b56a9bc73ef3676a343dcc90a8103c024c9449a3/local_channel_store.py) (source: github_api): import fitz     except Exception as exc:         raise RuntimeError(             "PDF vision fallback requires PyMuPDF. Run `pip install -r requirements.txt` "             f"in this environmen
- [manifest_line](https://github.com/quarqlabs/argus/blob/main/requirements.txt) (source: github_api): python-docx>=1.1.2,<2.0.0
- [code_permalink](https://github.com/quarqlabs/argus/blob/b56a9bc73ef3676a343dcc90a8103c024c9449a3/local_channel_store.py) (source: github_api): try:         from docx import Document     except Exception as exc:         return {"extract_type": "docx", "text": "", "error": f"python-docx unavailable: {exc}"}     try:         document = Doc
- [other](https://github.com/quarqlabs/argus/tree/main/reports) (source: github_api): directory reports/ present
- [readme_excerpt](https://github.com/quarqlabs/argus/blob/main/README.md) (source: readme): **Cloud-tool expansion:** external SaaS actions are routed through a single cloud-tool skill with configurable toolkits, user-facing `/tools`, `/which-tool`, `/cloud-tools`, `/add-tool`, and `/remove-

### 2. LinuxPlumbersConf/indico

**Repository / product**

- Repository: [https://github.com/linuxplumbersconf/indico](https://github.com/linuxplumbersconf/indico)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: events_weddings (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=3, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; pipeline_stage_count=3; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 51/100 (a score, not a probability)
- Raw weighted score: 2.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 1 |
| Pipeline complexity | 3 |
| Maintenance burden | 5 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `ReportLab`, run `run_2`, window `size:8001..16000`, rank 24
  - Query: `"reportlab" filename:requirements.txt size:8001..16000`
  - Sampled 30 of 1,636 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,636 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `WeasyPrint`, run `run_2`, window `size:8001..16000`, rank 22
  - Query: `"weasyprint" filename:requirements.txt size:8001..16000`
  - Retrieved 30 of 474 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [requirements.txt](https://github.com/LinuxPlumbersConf/indico/blob/lpc/v3.3.12/requirements.txt)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/LinuxPlumbersConf/indico/blob/70f19d26a3cdbd52f7c7a644bbf7d260a526fd13/indico/modules/designer/pdf.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/LinuxPlumbersConf/indico/blob/70f19d26a3cdbd52f7c7a644bbf7d260a526fd13/indico/modules/events/posters.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/LinuxPlumbersConf/indico/blob/70f19d26a3cdbd52f7c7a644bbf7d260a526fd13/indico/legacy/pdfinterface/base.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/LinuxPlumbersConf/indico/blob/70f19d26a3cdbd52f7c7a644bbf7d260a526fd13/indico/modules/designer/__init__.py)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements.txt](https://github.com/LinuxPlumbersConf/indico/blob/lpc/v3.3.12/requirements.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/LinuxPlumbersConf/indico/blob/70f19d26a3cdbd52f7c7a644bbf7d260a526fd13/indico/modules/receipts/util.py)

**Evidence trail**

- [api_response](https://github.com/LinuxPlumbersConf/indico) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/LinuxPlumbersConf/indico/blob/lpc/v3.3.12/requirements.txt) (source: github_api): #   reportlab
- [code_permalink](https://github.com/LinuxPlumbersConf/indico/blob/70f19d26a3cdbd52f7c7a644bbf7d260a526fd13/indico/modules/designer/pdf.py) (source: github_api): from io import BytesIO from PIL import Image from reportlab.lib import pagesizes from reportlab.lib.colors import getAllNamedColors from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_
- [code_permalink](https://github.com/LinuxPlumbersConf/indico/blob/70f19d26a3cdbd52f7c7a644bbf7d260a526fd13/indico/modules/events/posters.py) (source: github_api): from collections import namedtuple from reportlab.lib.units import cm from reportlab.lib.utils import ImageReader from indico.modules.designer import PageOrientation from indico.modules.designer.pdf
- [code_permalink](https://github.com/LinuxPlumbersConf/indico/blob/70f19d26a3cdbd52f7c7a644bbf7d260a526fd13/indico/legacy/pdfinterface/base.py) (source: github_api): from xml.sax import saxutils  # noqa: S406 from PIL import Image as PILImage from reportlab import platypus from reportlab.lib.enums import TA_CENTER from reportlab.lib.fonts import addMapping from r
- [code_permalink](https://github.com/LinuxPlumbersConf/indico/blob/70f19d26a3cdbd52f7c7a644bbf7d260a526fd13/indico/modules/designer/__init__.py) (source: github_api): from flask import session from reportlab.lib import pagesizes from reportlab.lib.units import mm from indico.core import signals from indico.util.enum import RichIntEnum
- [manifest_line](https://github.com/LinuxPlumbersConf/indico/blob/lpc/v3.3.12/requirements.txt) (source: github_api): #   weasyprint
- [code_permalink](https://github.com/LinuxPlumbersConf/indico/blob/70f19d26a3cdbd52f7c7a644bbf7d260a526fd13/indico/modules/receipts/util.py) (source: github_api): from sqlalchemy.sql import or_ from weasyprint import CSS, HTML, default_url_fetcher from webargs.flaskparser import abort

### 3. B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making

**Repository / product**

- Repository: [https://github.com/b253500/llm-agents-to-automate-vc-intelligence-and-deal-making](https://github.com/b253500/llm-agents-to-automate-vc-intelligence-and-deal-making)
- Company: Unknown — not stated in the repository
- Product: VC Agents - AI-Powered Investment Memo Generation
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=3, pipeline_stage_count=0 \| supporting: category_count=3

**Score**

- Score: 50/100 (a score, not a probability)
- Raw weighted score: 2.50 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 4 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:8001..16000`, rank 8
  - Query: `"mammoth" filename:requirements.txt size:8001..16000`
  - Retrieved 30 of 105 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `ReportLab`, run `run_2`, window `size:8001..16000`, rank 29
  - Query: `"reportlab" filename:requirements.txt size:8001..16000`
  - Sampled 30 of 1,636 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,636 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `pikepdf`, run `run_2`, window `size:8001..16000`, rank 14
  - Query: `"pikepdf" filename:requirements.txt size:8001..16000`
  - Retrieved 30 of 253 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Unstructured`, run `run_2`, window `size:8001..16000`, rank 19
  - Query: `"unstructured" filename:requirements.txt size:8001..16000`
  - Sampled 30 of 54,144 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 54,144 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `(co-occurrence query, spans multiple libraries)`, run `run_2`, window `size:8001..16000`, rank 6
  - Query: `"python-docx" "reportlab" filename:requirements.txt size:8001..16000`
  - Retrieved 30 of 236 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [exact_requirements.txt](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/exact_requirements.txt)
- `ReportLab` (pdf, generation) — manifest_declaration — [requirements.txt](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/requirements.txt)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [exact_requirements.txt](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/exact_requirements.txt)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/requirements.txt)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [web_scraping/minimal_requirements.txt](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/620fc93a7b6a8bc4f1ea97635a0cda014cc8d310/web_scraping/minimal_requirements.txt)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/620fc93a7b6a8bc4f1ea97635a0cda014cc8d310/agents/founder_profiling_agent.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/620fc93a7b6a8bc4f1ea97635a0cda014cc8d310/build_report_cache.py)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [exact_requirements.txt](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/exact_requirements.txt)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [requirements.txt](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/requirements.txt)
- `pikepdf` (pdf, generation) — manifest_declaration — [exact_requirements.txt](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/exact_requirements.txt)

**Evidence trail**

- [api_response](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/exact_requirements.txt) (source: github_api): reportlab==4.4.1
- [manifest_line](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/requirements.txt) (source: github_api): reportlab
- [manifest_line](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/exact_requirements.txt) (source: github_api): unstructured==0.18.9
- [manifest_line](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/requirements.txt) (source: github_api): unstructured[pdf]>=0.10.30
- [manifest_line](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/620fc93a7b6a8bc4f1ea97635a0cda014cc8d310/web_scraping/minimal_requirements.txt) (source: github_api): pypdf>=3.17.0 pymupdf>=1.23.0 pdfminer.six unstructured[pdf]>=0.10.30 # Document Processing (Required) python-docx
- [code_permalink](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/620fc93a7b6a8bc4f1ea97635a0cda014cc8d310/agents/founder_profiling_agent.py) (source: github_api): seen_names.add(name_lower)                 break          # Second pass: look for LinkedIn URLs in unstructured text     if len(execs) < 3:         linkedin_pattern = r"htt
- [code_permalink](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/620fc93a7b6a8bc4f1ea97635a0cda014cc8d310/build_report_cache.py) (source: github_api): import logging from langchain_community.document_loaders import UnstructuredPDFLoader from langchain_community.vectorstores import Chroma
- [manifest_line](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/exact_requirements.txt) (source: github_api): mammoth==1.9.1
- [manifest_line](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/requirements.txt) (source: github_api): mammoth
- [manifest_line](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/exact_requirements.txt) (source: github_api): pikepdf==9.10.2
- [readme_excerpt](https://github.com/B253500/LLM-Agents-to-Automate-VC-Intelligence-and-Deal-Making/blob/main/README.md) (source: readme): This is the recommended way to run the platform for continuous operation.

### 4. dynamiq-ai/dynamiq

**Repository / product**

- Repository: [https://github.com/dynamiq-ai/dynamiq](https://github.com/dynamiq-ai/dynamiq)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://getdynamiq.ai

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=3, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=3; multiple_document_types_handled=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 48/100 (a score, not a probability)
- Raw weighted score: 2.40 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 4 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden | 5 |
| Build-vs-buy signal | 4 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `ReportLab`, run `run_2`, window `size:4001..8000`, rank 23
  - Query: `"reportlab" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 769 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `WeasyPrint`, run `run_2`, window `size:4001..8000`, rank 7
  - Query: `"weasyprint" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 419 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Unstructured`, run `run_2`, window `size:4001..8000`, rank 24
  - Query: `"unstructured" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 574 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/dynamiq-ai/dynamiq/blob/main/pyproject.toml)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/dynamiq/nodes/transformers/markdown.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/tests/integration_with_creds/agents/test_agent_llms.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/tests/integration_with_creds/nodes/knowledgebases/test_vertex_rag_e2e.py)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [pyproject.toml](https://github.com/dynamiq-ai/dynamiq/blob/main/pyproject.toml)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/dynamiq/connections/connections.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/dynamiq/nodes/converters/unstructured.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/dynamiq/components/converters/unstructured.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/dynamiq/nodes/converters/__init__.py)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/dynamiq-ai/dynamiq/blob/main/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/dynamiq-ai/dynamiq) (source: github_api): stars=1066, fork=False, archived=False
- [manifest_line](https://github.com/dynamiq-ai/dynamiq/blob/main/pyproject.toml) (source: github_api): "reportlab>=4.3.0,<4.4.0",
- [code_permalink](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/dynamiq/nodes/transformers/markdown.py) (source: github_api): from inscriptis import ParserConfig, get_text from pydantic import BaseModel, ConfigDict, Field from reportlab.lib.pagesizes import letter from reportlab.pdfgen import canvas from dynamiq.nodes impor
- [code_permalink](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/tests/integration_with_creds/agents/test_agent_llms.py) (source: github_api): from io import BytesIO import pytest from reportlab.pdfgen import canvas from dynamiq.connections import Anthropic as AnthropicConnection from dynamiq.connections import Gemini as GeminiConnection
- [code_permalink](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/tests/integration_with_creds/nodes/knowledgebases/test_vertex_rag_e2e.py) (source: github_api): def _build_pdf() -> bytes:     from reportlab.lib.pagesizes import LETTER     from reportlab.pdfgen import canvas     buffer = io.BytesIO()     pdf = canvas.Canvas(buffer, pagesize=LETTER)
- [manifest_line](https://github.com/dynamiq-ai/dynamiq/blob/main/pyproject.toml) (source: github_api): "unstructured-client>=0.42.3,<0.43.0",
- [code_permalink](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/dynamiq/connections/connections.py) (source: github_api): return chroma_client class Unstructured(HttpApiKey):     """     Represents a connection to the Unstructured API.
- [code_permalink](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/dynamiq/nodes/converters/unstructured.py) (source: github_api): from dynamiq.components.converters.unstructured import ConvertStrategy, DocumentCreationMode, UnstructuredElementTypes from dynamiq.components.converters.unstructured import UnstructuredFileConverter
- [code_permalink](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/dynamiq/components/converters/unstructured.py) (source: github_api): from unstructured_client import UnstructuredClient from unstructured_client.models import operations, shared
- [code_permalink](https://github.com/dynamiq-ai/dynamiq/blob/9fcec5f14f96e311212f240ca14fd0f1f2ccc771/dynamiq/nodes/converters/__init__.py) (source: github_api): from .llm_text_extractor import LLMImageConverter, LLMPDFConverter from .multi_file_type_converter import MultiFileTypeConverter from .pptx import PPTXFileConverter from .pypdf import PyPDFConverter f
- [manifest_line](https://github.com/dynamiq-ai/dynamiq/blob/main/pyproject.toml) (source: github_api): "weasyprint>=68.0,<69.0",
- [readme_excerpt](https://github.com/dynamiq-ai/dynamiq/blob/main/README.md) (source: readme): 🤖 Dynamiq is your all-in-one Gen AI framework, designed to streamline the development of AI-powered applications.

### 5. Upsonic/Upsonic

**Repository / product**

- Repository: [https://github.com/upsonic/upsonic](https://github.com/upsonic/upsonic)
- Company: Unknown — not stated in the repository
- Product: Upsonic
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://docs.upsonic.ai

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=3, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=3; multiple_document_types_handled=true; pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 47/100 (a score, not a probability)
- Raw weighted score: 2.35 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 4 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `ReportLab`, run `run_2`, window `size:4001..8000`, rank 11
  - Query: `"reportlab" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 769 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:4001..8000`, rank 5
  - Query: `"PyMuPDF" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 892 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Docling`, run `run_2`, window `size:4001..8000`, rank 6
  - Query: `"docling" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 323 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `python-docx`, run `run_2`, window `size:4001..8000`, rank 12
  - Query: `"python-docx" filename:pyproject.toml size:4001..8000`
  - Sampled 30 of 1,288 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,288 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Docling` (other_processing, extraction) — manifest_declaration — [pyproject.toml](https://github.com/Upsonic/Upsonic/blob/master/pyproject.toml)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/docling.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/__init__.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/factory.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/config.py)
- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [pyproject.toml](https://github.com/Upsonic/Upsonic/blob/master/pyproject.toml)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/pymupdf.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/__init__.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/ocr/layer_0/document_converter.py)
- `ReportLab` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/Upsonic/Upsonic/blob/master/pyproject.toml)
- `python-docx` (docx, generation) — manifest_declaration — [pyproject.toml](https://github.com/Upsonic/Upsonic/blob/master/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/Upsonic/Upsonic) (source: github_api): stars=7944, fork=False, archived=False
- [manifest_line](https://github.com/Upsonic/Upsonic/blob/master/pyproject.toml) (source: github_api): docling-loader = [
- [code_permalink](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/docling.py) (source: github_api): from docling.datamodel.base_models import InputFormat     from docling.datamodel.document import DoclingDocument     from docling.datamodel.pipeline_options import (
- [code_permalink](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/__init__.py) (source: github_api): from .html import HTMLLoader     from .docling import DoclingLoader     from .factory import (
- [code_permalink](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/factory.py) (source: github_api): # DoclingLoader - optional advanced loader         try:             from .docling import DoclingLoader             # Docling supports a wide range of formats, register with high prior
- [code_permalink](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/config.py) (source: github_api): class DoclingLoaderConfig(LoaderConfig):     """     Advanced configuration for Docling-based document loading.          Docling provides enterprise-grade document processing with support for     PDF
- [manifest_line](https://github.com/Upsonic/Upsonic/blob/master/pyproject.toml) (source: github_api): pymupdf-loader = [
- [code_permalink](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/pymupdf.py) (source: github_api): except ImportError:     pymupdf = None     _PYMUPDF_AVAILABLE = False
- [code_permalink](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/loaders/__init__.py) (source: github_api): from .pdf import PdfLoader     from .pymupdf import PyMuPDFLoader     from .pdfplumber import PdfPlumberLoader
- [code_permalink](https://github.com/Upsonic/Upsonic/blob/101f0313b0ddb96cd4078354879b2ff57005db29/src/upsonic/ocr/layer_0/document_converter.py) (source: github_api): # --------------------------------------------------------------------------- # PDF → images  (PyMuPDF, no poppler needed) # ---------------------------------------------------------------------------
- [manifest_line](https://github.com/Upsonic/Upsonic/blob/master/pyproject.toml) (source: github_api): "reportlab>=4.1.0",
- [manifest_line](https://github.com/Upsonic/Upsonic/blob/master/pyproject.toml) (source: github_api): "python-docx>=1.2.0",
- [other](https://github.com/Upsonic/Upsonic/tree/master/documents) (source: github_api): directory documents/ present

### 6. LegalQuants/lq-ai

**Repository / product**

- Repository: [https://github.com/legalquants/lq-ai](https://github.com/legalquants/lq-ai)
- Company: Unknown — not stated in the repository
- Product: LQ.AI
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=2, pipeline_stage_count=1 \| supporting: category_count=2; multiple_document_types_handled=true; confirmed generation/conversion code

**Score**

- Score: 44/100 (a score, not a probability)
- Raw weighted score: 2.20 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:8001..16000`, rank 19
  - Query: `"PyMuPDF" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 334 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Docling`, run `run_2`, window `size:8001..16000`, rank 20
  - Query: `"docling" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 150 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/config.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/pipeline/ingest.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/pipeline/parsers.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/pipeline/__init__.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/models/document.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/pipeline/parsers.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/pipeline/__init__.py)

**Evidence trail**

- [api_response](https://github.com/LegalQuants/lq-ai) (source: github_api): stars=125, fork=False, archived=False
- [code_permalink](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/config.py) (source: github_api): # Concurrency: how many ingest jobs the arq worker runs in parallel.     # 2 is the conservative default for M1 — both Docling and PyMuPDF are     # CPU-bound and we don't want to starve the host.
- [code_permalink](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/pipeline/ingest.py) (source: github_api): 3. Runs :func:`app.pipeline.parsers.parse_pdf` (PyMuPDF mandatory,    Docling best-effort) on the byte stream — wrapped in    :func:`asyncio.to_thread` because the parsers are sync.
- [code_permalink](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/pipeline/parsers.py) (source: github_api): paragraphs, tables) that is stashed for M2 consumption. M1's   chunker does not consume Docling's offsets — they are not   character-precise against the original PDF.
- [code_permalink](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/pipeline/__init__.py) (source: github_api): This package contains the pieces of the document-pipeline service: * :mod:`app.pipeline.parsers` — Docling and PyMuPDF adapter functions   that translate PDF bytes into a canonical character stream
- [code_permalink](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/models/document.py) (source: github_api): Citation Engine. ``char_offset_start`` and ``char_offset_end`` are   byte-precise against the canonical PyMuPDF character stream — the   fidelity contract the M2 Citation Engine's deterministic subs
- [code_permalink](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/pipeline/parsers.py) (source: github_api): * **PyMuPDF** is the source of truth for the canonical character   stream. Every chunk's ``content`` slices the PyMuPDF output by   ``[char_offset_start:char_offset_end]`` byte-for-byte.
- [code_permalink](https://github.com/LegalQuants/lq-ai/blob/9f6f51c30e96ff12b181d16edec6897f608810f4/api/app/pipeline/__init__.py) (source: github_api): This package contains the pieces of the document-pipeline service: * :mod:`app.pipeline.parsers` — Docling and PyMuPDF adapter functions   that translate PDF bytes into a canonical character stream
- [readme_excerpt](https://github.com/LegalQuants/lq-ai/blob/main/README.md) (source: readme): LQ.AI is a self-hosted AI platform purpose-built for legal teams.

### 7. sbrunner/scan-to-paperless

**Repository / product**

- Repository: [https://github.com/sbrunner/scan-to-paperless](https://github.com/sbrunner/scan-to-paperless)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=3, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; pipeline_stage_count=3; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 44/100 (a score, not a probability)
- Raw weighted score: 2.20 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 0 |
| Pipeline complexity | 3 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `ReportLab`, run `run_2`, window `size:4001..8000`, rank 25
  - Query: `"reportlab" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 769 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `pikepdf`, run `run_2`, window `size:4001..8000`, rank 7
  - Query: `"pikepdf" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 89 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `WeasyPrint`, run `run_2`, window `size:4001..8000`, rank 10
  - Query: `"weasyprint" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 419 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/sbrunner/scan-to-paperless/blob/test/pyproject.toml)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/sbrunner/scan-to-paperless/blob/03f910666a19f1bf5337ab8ff2e3ad425ef71b9f/scan_to_paperless/add_code.py)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/sbrunner/scan-to-paperless/blob/test/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/sbrunner/scan-to-paperless/blob/03f910666a19f1bf5337ab8ff2e3ad425ef71b9f/scan_to_paperless/add_code.py)
- `pikepdf` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/sbrunner/scan-to-paperless/blob/test/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/sbrunner/scan-to-paperless) (source: github_api): stars=265, fork=False, archived=False
- [manifest_line](https://github.com/sbrunner/scan-to-paperless/blob/test/pyproject.toml) (source: github_api): reportlab = { version = "5.0.0", optional = true }
- [code_permalink](https://github.com/sbrunner/scan-to-paperless/blob/03f910666a19f1bf5337ab8ff2e3ad425ef71b9f/scan_to_paperless/add_code.py) (source: github_api): from PIL import Image from pypdf import PdfReader, PdfWriter from pyzbar import pyzbar from reportlab.lib.colors import Color from reportlab.pdfgen import canvas from weasyprint import CSS, HTML
- [manifest_line](https://github.com/sbrunner/scan-to-paperless/blob/test/pyproject.toml) (source: github_api): weasyprint = { version = "69.0", optional = true }
- [code_permalink](https://github.com/sbrunner/scan-to-paperless/blob/03f910666a19f1bf5337ab8ff2e3ad425ef71b9f/scan_to_paperless/add_code.py) (source: github_api): from pyzbar import pyzbar from reportlab.lib.colors import Color from reportlab.pdfgen import canvas from weasyprint import CSS, HTML _LOG = logging.getLogger(__name__) Image.MAX_IMAGE_PIXELS = 50000
- [manifest_line](https://github.com/sbrunner/scan-to-paperless/blob/test/pyproject.toml) (source: github_api): pikepdf = { version = "10.11.0", optional = true }

### 8. llv22/camel_forward

**Repository / product**

- Repository: [https://github.com/llv22/camel_forward](https://github.com/llv22/camel_forward)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 43/100 (a score, not a probability)
- Raw weighted score: 2.15 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden | 5 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `ReportLab`, run `run_2`, window `size:>16000`, rank 22
  - Query: `"reportlab" filename:pyproject.toml size:>16000`
  - Retrieved 30 of 96 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Unstructured`, run `run_2`, window `size:>16000`, rank 22
  - Query: `"unstructured" filename:pyproject.toml size:>16000`
  - Retrieved 30 of 640 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/llv22/camel_forward/blob/master/pyproject.toml)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/llv22/camel_forward/blob/858de49e7a759759b14dac7cc4448a9b447f2d9e/camel/toolkits/file_toolkit.py)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [pyproject.toml](https://github.com/llv22/camel_forward/blob/master/pyproject.toml)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/llv22/camel_forward/blob/858de49e7a759759b14dac7cc4448a9b447f2d9e/camel/loaders/unstructured_io.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/llv22/camel_forward/blob/858de49e7a759759b14dac7cc4448a9b447f2d9e/examples/loaders/unstructured_io_example.py)

**Evidence trail**

- [api_response](https://github.com/llv22/camel_forward) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/llv22/camel_forward/blob/master/pyproject.toml) (source: github_api): "reportlab>=4.4.2",
- [code_permalink](https://github.com/llv22/camel_forward/blob/858de49e7a759759b14dac7cc4448a9b447f2d9e/camel/toolkits/file_toolkit.py) (source: github_api): try:                 from reportlab.lib import colors                 from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
- [manifest_line](https://github.com/llv22/camel_forward/blob/master/pyproject.toml) (source: github_api): "unstructured==0.16.20; python_version < '3.13'",
- [code_permalink](https://github.com/llv22/camel_forward/blob/858de49e7a759759b14dac7cc4448a9b447f2d9e/camel/loaders/unstructured_io.py) (source: github_api): r"""A class to handle various functionalities provided by the     Unstructured library, including version checking, parsing, cleaning,     extracting, staging, chunking data, and integrating with
- [code_permalink](https://github.com/llv22/camel_forward/blob/858de49e7a759759b14dac7cc4448a9b447f2d9e/examples/loaders/unstructured_io_example.py) (source: github_api): from camel.loaders.unstructured_io import UnstructuredIO

### 9. PapiHack/document-templating-service

**Repository / product**

- Repository: [https://github.com/papihack/document-templating-service](https://github.com/papihack/document-templating-service)
- Company: Unknown — not stated in the repository
- Product: 🚀 Document Template Processing Service 🚀
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=3, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; pipeline_stage_count=3; infrastructure_service_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 43/100 (a score, not a probability)
- Raw weighted score: 2.15 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 0 |
| Pipeline complexity | 5 |
| Maintenance burden | 3 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 4
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 29
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 14
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 4
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 29
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 14
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/PapiHack/document-templating-service/blob/master/Dockerfile)
- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/PapiHack/document-templating-service/blob/master/docker-compose.yaml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/PapiHack/document-templating-service/blob/adb593da4b9395db113b7d52a3189e526227fe4b/main.py)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/PapiHack/document-templating-service/blob/adb593da4b9395db113b7d52a3189e526227fe4b/utils.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [requirements.txt](https://github.com/PapiHack/document-templating-service/blob/master/requirements.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/PapiHack/document-templating-service/blob/adb593da4b9395db113b7d52a3189e526227fe4b/main.py)

**Evidence trail**

- [api_response](https://github.com/PapiHack/document-templating-service) (source: github_api): stars=63, fork=False, archived=False
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/master/Dockerfile) (source: github_api): ENV GOTENBERG_API_URL=http://host.docker.internal:3000
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/master/docker-compose.yaml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/adb593da4b9395db113b7d52a3189e526227fe4b/main.py) (source: github_api): return JSONResponse({'status': 'error', 'message': 'file is required'}, status_code=400)     if data is None or len(data) == 0:         return JSONResponse({'status': 'error', 'message': 'data
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/adb593da4b9395db113b7d52a3189e526227fe4b/utils.py) (source: github_api): def get_env(var_name: str) -> str:     if 'GOTENBERG_API_URL' in os.environ:         return os.environ['GOTENBERG_API_URL']     return env[var_name] def remove_file(filename: str):
- [manifest_line](https://github.com/PapiHack/document-templating-service/blob/master/requirements.txt) (source: github_api): docxtpl==0.15.2
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/adb593da4b9395db113b7d52a3189e526227fe4b/main.py) (source: github_api): from fastapi import Body, FastAPI, File, UploadFile from fastapi.responses import FileResponse, JSONResponse from pydantic import Json from docxtpl import DocxTemplate import aiofiles from utils impor
- [api_response](https://github.com/PapiHack/document-templating-service) (source: github_api): stars=63, fork=False, archived=False
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/master/Dockerfile) (source: github_api): FROM python:3.8.13-slim-buster WORKDIR /code RUN python -m venv venv ENV PATH="venv/bin:$PATH" ENV GOTENBERG_API_URL=http://host.docker.internal:3000 COPY ./requirements.txt /code/requirements.txt
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/master/docker-compose.yaml) (source: github_api): version: '3' services:   gotenberg:     container_name: gotenberg-service     # replace image with gotenberg/gotenberg:7-cloudrun or thecodingmachine/gotenberg:7-cloudrun     # if you plan to run it o
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/master/Dockerfile) (source: github_api): ENV GOTENBERG_API_URL=http://host.docker.internal:3000
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/master/docker-compose.yaml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/master/Dockerfile) (source: github_api): ENV GOTENBERG_API_URL=http://host.docker.internal:3000
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/master/docker-compose.yaml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/adb593da4b9395db113b7d52a3189e526227fe4b/main.py) (source: github_api): return JSONResponse({'status': 'error', 'message': 'file is required'}, status_code=400)     if data is None or len(data) == 0:         return JSONResponse({'status': 'error', 'message': 'data
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/adb593da4b9395db113b7d52a3189e526227fe4b/utils.py) (source: github_api): def get_env(var_name: str) -> str:     if 'GOTENBERG_API_URL' in os.environ:         return os.environ['GOTENBERG_API_URL']     return env[var_name] def remove_file(filename: str):
- [manifest_line](https://github.com/PapiHack/document-templating-service/blob/master/requirements.txt) (source: github_api): docxtpl==0.15.2
- [code_permalink](https://github.com/PapiHack/document-templating-service/blob/adb593da4b9395db113b7d52a3189e526227fe4b/main.py) (source: github_api): from fastapi import Body, FastAPI, File, UploadFile from fastapi.responses import FileResponse, JSONResponse from pydantic import Json from docxtpl import DocxTemplate import aiofiles from utils impor

### 10. UKGovernmentBEIS/inspect_evals

**Repository / product**

- Repository: [https://github.com/ukgovernmentbeis/inspect_evals](https://github.com/ukgovernmentbeis/inspect_evals)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: healthcare_diagnostics (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://ukgovernmentbeis.github.io/inspect_evals/

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=2, pipeline_stage_count=1 \| supporting: category_count=2; confirmed generation/conversion code

**Score**

- Score: 41/100 (a score, not a probability)
- Raw weighted score: 2.05 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 2 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 2
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_1`, window `size:1001..2000`, rank 3
  - Query: `"python-docx" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 8,336 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 8,336 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 2
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `pypdf / PyPDF2`, run `run_2`, window `size:>16000`, rank 11
  - Query: `"pypdf" filename:pyproject.toml size:>16000`
  - Retrieved 30 of 205 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `WeasyPrint`, run `run_2`, window `size:2001..4000`, rank 5
  - Query: `"weasyprint" filename:requirements.txt size:2001..4000`
  - Sampled 30 of 1,336 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,336 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `(co-occurrence query, spans multiple libraries)`, run `run_2`, window `size:2001..4000`, rank 2
  - Query: `"python-docx" "reportlab" filename:requirements.txt size:2001..4000`
  - Retrieved 30 of 932 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [src/inspect_evals/bigcodebench/docker-requirements.txt](https://github.com/UKGovernmentBEIS/inspect_evals/blob/32b79a244f17ecf54fa1186d30f33dc10143c10f/src/inspect_evals/bigcodebench/docker-requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [src/inspect_evals/class_eval/docker-requirements.txt](https://github.com/UKGovernmentBEIS/inspect_evals/blob/32b79a244f17ecf54fa1186d30f33dc10143c10f/src/inspect_evals/class_eval/docker-requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [src/inspect_evals/bigcodebench/docker-requirements.txt](https://github.com/UKGovernmentBEIS/inspect_evals/blob/32b79a244f17ecf54fa1186d30f33dc10143c10f/src/inspect_evals/bigcodebench/docker-requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [src/inspect_evals/gdpval/docker-requirements.txt](https://github.com/UKGovernmentBEIS/inspect_evals/blob/32b79a244f17ecf54fa1186d30f33dc10143c10f/src/inspect_evals/gdpval/docker-requirements.txt)
- `python-docx` (docx, generation) — code_import — [code](https://github.com/UKGovernmentBEIS/inspect_evals/blob/32b79a244f17ecf54fa1186d30f33dc10143c10f/src/inspect_evals/theagentcompany/common_evaluators.py)

**Evidence trail**

- [api_response](https://github.com/UKGovernmentBEIS/inspect_evals) (source: github_api): stars=637, fork=False, archived=False
- [manifest_line](https://github.com/UKGovernmentBEIS/inspect_evals/blob/32b79a244f17ecf54fa1186d30f33dc10143c10f/src/inspect_evals/bigcodebench/docker-requirements.txt) (source: github_api): sympy==1.12 pyfakefs==5.4.1 textblob==0.18.0 docxtpl==0.11.5 statsmodels==0.14.0 pyquery==1.4.3 holidays==0.29
- [manifest_line](https://github.com/UKGovernmentBEIS/inspect_evals/blob/32b79a244f17ecf54fa1186d30f33dc10143c10f/src/inspect_evals/class_eval/docker-requirements.txt) (source: github_api): numpy scipy pandas python-docx openpyxl bs4 pillow
- [manifest_line](https://github.com/UKGovernmentBEIS/inspect_evals/blob/32b79a244f17ecf54fa1186d30f33dc10143c10f/src/inspect_evals/bigcodebench/docker-requirements.txt) (source: github_api): Pillow==10.3.0 beautifulsoup4==4.8.2 datetime==5.5 python-docx==1.1.0 openpyxl==3.1.2 Levenshtein==0.25.0 PyYAML==6.0.1
- [manifest_line](https://github.com/UKGovernmentBEIS/inspect_evals/blob/32b79a244f17ecf54fa1186d30f33dc10143c10f/src/inspect_evals/gdpval/docker-requirements.txt) (source: github_api): pytest-cov~=5.0.0 pytest-json-report~=1.5.0 pyth3==0.7 python-docx==0.8.11 python-pptx==0.6.21 pyttsx3==2.90 pyxlsb==1.0.8
- [code_permalink](https://github.com/UKGovernmentBEIS/inspect_evals/blob/32b79a244f17ecf54fa1186d30f33dc10143c10f/src/inspect_evals/theagentcompany/common_evaluators.py) (source: github_api): def _paragraph_text_from_p(p_elem: ET.Element) -> str:     """Text of a ``w:p`` (same idea as ``paragraph.text`` in python-docx)."""     parts: list[str] = []
- [readme_excerpt](https://github.com/UKGovernmentBEIS/inspect_evals/blob/main/README.md) (source: readme): The major one used by some Inspect Evals is `torch`.

### 11. pbl-nl/appl-docchat

**Repository / product**

- Repository: [https://github.com/pbl-nl/appl-docchat](https://github.com/pbl-nl/appl-docchat)
- Company: Unknown — not stated in the repository
- Product: Chat with your docs!
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://github.com/pbl-nl

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 41/100 (a score, not a probability)
- Raw weighted score: 2.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden | 3 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:2001..4000`, rank 5
  - Query: `"PyMuPDF" filename:requirements.txt size:2001..4000`
  - Sampled 30 of 5,296 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 5,296 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_2`, window `size:2001..4000`, rank 14
  - Query: `"python-docx" filename:requirements.txt size:2001..4000`
  - Sampled 30 of 6,224 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 6,224 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [requirements.txt](https://github.com/pbl-nl/appl-docchat/blob/main/requirements.txt)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/pbl-nl/appl-docchat/blob/c9e9b6b707bbd2969f083e2a1dca990ee48afebc/setup.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/pbl-nl/appl-docchat/blob/c9e9b6b707bbd2969f083e2a1dca990ee48afebc/ingest/file_parser.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/pbl-nl/appl-docchat/blob/c9e9b6b707bbd2969f083e2a1dca990ee48afebc/summarize/summarizer.py)
- `python-docx` (docx, generation) — manifest_declaration — [requirements.txt](https://github.com/pbl-nl/appl-docchat/blob/main/requirements.txt)
- `python-docx` (docx, generation) — code_import — [code](https://github.com/pbl-nl/appl-docchat/blob/c9e9b6b707bbd2969f083e2a1dca990ee48afebc/setup.py)

**Evidence trail**

- [api_response](https://github.com/pbl-nl/appl-docchat) (source: github_api): stars=22, fork=False, archived=False
- [manifest_line](https://github.com/pbl-nl/appl-docchat/blob/main/requirements.txt) (source: github_api): PyMuPDF==1.25.1
- [code_permalink](https://github.com/pbl-nl/appl-docchat/blob/c9e9b6b707bbd2969f083e2a1dca990ee48afebc/setup.py) (source: github_api): "pydantic_core==2.18.4",     "pydeck==0.9.1",     "Pygments==2.18.0",     "PyMuPDF==1.24.5",     "PyMuPDFb==1.24.3",     "pypdf==4.2.0",     "PyPika==0.48.9",
- [code_permalink](https://github.com/pbl-nl/appl-docchat/blob/c9e9b6b707bbd2969f083e2a1dca990ee48afebc/ingest/file_parser.py) (source: github_api): Raw text is extracted from the documents and metadata added. PDF files are parsed with pymupdf, Word files are first converted to pdf files and then parsed. This is to be able to show the sources in t
- [code_permalink](https://github.com/pbl-nl/appl-docchat/blob/c9e9b6b707bbd2969f083e2a1dca990ee48afebc/summarize/summarizer.py) (source: github_api): from langchain.chains.summarize import load_summarize_chain from langchain_community.document_loaders import PyMuPDFLoader from dotenv import load_dotenv
- [manifest_line](https://github.com/pbl-nl/appl-docchat/blob/main/requirements.txt) (source: github_api): python-docx==1.1.2
- [code_permalink](https://github.com/pbl-nl/appl-docchat/blob/c9e9b6b707bbd2969f083e2a1dca990ee48afebc/setup.py) (source: github_api): "pyreadline3==3.4.1",     "pysbd==0.3.4",     "python-dateutil==2.9.0.post0",     "python-docx==1.1.2",     "python-dotenv==1.0.1",     "python-iso639==2024.4.27",     "python-magic==0.4.27",

### 12. abgulati/LARS

**Repository / product**

- Repository: [https://github.com/abgulati/lars](https://github.com/abgulati/lars)
- Company: Unknown — not stated in the repository
- Product: LARS - The LLM & Advanced Referencing Solution
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.youtube.com/watch?v=Mam1i86n8sU&ab_channel=AbheekGulati

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2; pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 41/100 (a score, not a probability)
- Raw weighted score: 2.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 2 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `pypdf / PyPDF2`, run `run_2`, window `size:4001..8000`, rank 3
  - Query: `"pypdf" filename:requirements.txt size:4001..8000`
  - Sampled 30 of 8,208 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 8,208 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:4001..8000`, rank 3
  - Query: `"PyMuPDF" filename:requirements.txt size:4001..8000`
  - Sampled 30 of 3,352 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,352 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Unstructured`, run `run_2`, window `size:4001..8000`, rank 4
  - Query: `"unstructured" filename:requirements.txt size:4001..8000`
  - Sampled 30 of 1,700 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,700 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [requirements.txt](https://github.com/abgulati/LARS/blob/main/requirements.txt)
- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [requirements_linux.txt](https://github.com/abgulati/LARS/blob/main/requirements_linux.txt)
- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [requirements_mac.txt](https://github.com/abgulati/LARS/blob/main/requirements_mac.txt)
- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [dockerized/requirements_linux.txt](https://github.com/abgulati/LARS/blob/710489fc67b8a315d7429af0869425ebbef73148/dockerized/requirements_linux.txt)
- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [dockerized_nvidia_cuda_gpu/requirements_linux.txt](https://github.com/abgulati/LARS/blob/710489fc67b8a315d7429af0869425ebbef73148/dockerized_nvidia_cuda_gpu/requirements_linux.txt)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/abgulati/LARS/blob/710489fc67b8a315d7429af0869425ebbef73148/web_app/app.py)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/abgulati/LARS/blob/main/requirements.txt)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements_linux.txt](https://github.com/abgulati/LARS/blob/main/requirements_linux.txt)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements_mac.txt](https://github.com/abgulati/LARS/blob/main/requirements_mac.txt)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [dockerized/requirements_linux.txt](https://github.com/abgulati/LARS/blob/710489fc67b8a315d7429af0869425ebbef73148/dockerized/requirements_linux.txt)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [dockerized_nvidia_cuda_gpu/requirements_linux.txt](https://github.com/abgulati/LARS/blob/710489fc67b8a315d7429af0869425ebbef73148/dockerized_nvidia_cuda_gpu/requirements_linux.txt)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [requirements.txt](https://github.com/abgulati/LARS/blob/main/requirements.txt)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [requirements_linux.txt](https://github.com/abgulati/LARS/blob/main/requirements_linux.txt)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [requirements_mac.txt](https://github.com/abgulati/LARS/blob/main/requirements_mac.txt)

**Evidence trail**

- [api_response](https://github.com/abgulati/LARS) (source: github_api): stars=637, fork=False, archived=False
- [manifest_line](https://github.com/abgulati/LARS/blob/main/requirements.txt) (source: github_api): PyMuPDF==1.23.1
- [manifest_line](https://github.com/abgulati/LARS/blob/main/requirements_linux.txt) (source: github_api): PyMuPDF==1.23.1
- [manifest_line](https://github.com/abgulati/LARS/blob/main/requirements_mac.txt) (source: github_api): PyMuPDF==1.23.1
- [manifest_line](https://github.com/abgulati/LARS/blob/710489fc67b8a315d7429af0869425ebbef73148/dockerized/requirements_linux.txt) (source: github_api): pydantic==1.10.12 pydantic_core==2.6.3 Pygments==2.16.1 PyMuPDF==1.23.1 PyMuPDFb==1.23.0 pypandoc==1.11 pyparsing==2.4.7
- [manifest_line](https://github.com/abgulati/LARS/blob/710489fc67b8a315d7429af0869425ebbef73148/dockerized_nvidia_cuda_gpu/requirements_linux.txt) (source: github_api): pydantic==1.10.12 pydantic_core==2.6.3 Pygments==2.16.1 PyMuPDF==1.23.1 PyMuPDFb==1.23.0 pypandoc==1.11 pyparsing==2.4.7
- [code_permalink](https://github.com/abgulati/LARS/blob/710489fc67b8a315d7429af0869425ebbef73148/web_app/app.py) (source: github_api): from pdf2image import convert_from_path from PIL import Image import fitz # PyMuPDF from rapidfuzz import process, fuzz from urllib.parse import unquote
- [manifest_line](https://github.com/abgulati/LARS/blob/main/requirements.txt) (source: github_api): unstructured==0.10.8
- [manifest_line](https://github.com/abgulati/LARS/blob/main/requirements_linux.txt) (source: github_api): unstructured==0.10.8
- [manifest_line](https://github.com/abgulati/LARS/blob/main/requirements_mac.txt) (source: github_api): unstructured==0.10.8
- [manifest_line](https://github.com/abgulati/LARS/blob/710489fc67b8a315d7429af0869425ebbef73148/dockerized/requirements_linux.txt) (source: github_api): typing_extensions==4.7.1 tzdata==2023.3 tzlocal==5.0.1 unstructured==0.10.8 urllib3 uvicorn wasabi==1.1.2
- [manifest_line](https://github.com/abgulati/LARS/blob/710489fc67b8a315d7429af0869425ebbef73148/dockerized_nvidia_cuda_gpu/requirements_linux.txt) (source: github_api): typing_extensions==4.7.1 tzdata==2023.3 tzlocal==5.0.1 unstructured==0.10.8 urllib3 uvicorn wasabi==1.1.2
- [manifest_line](https://github.com/abgulati/LARS/blob/main/requirements.txt) (source: github_api): pypdf==4.2.0
- [manifest_line](https://github.com/abgulati/LARS/blob/main/requirements_linux.txt) (source: github_api): pypdf==4.2.0
- [manifest_line](https://github.com/abgulati/LARS/blob/main/requirements_mac.txt) (source: github_api): pypdf==4.2.0
- [other](https://github.com/abgulati/LARS/tree/main/documents) (source: github_api): directory documents/ present
- [readme_excerpt](https://github.com/abgulati/LARS/blob/main/README.md) (source: readme): <p align="center"> <img src="https://github.com/abgulati/LARS/blob/main/web_app/static/images/LARS_Logo_3.png"  align="center"> </p> LARS is an application that enables you to run LLM's (Large Languag

### 13. ilee165/network-infrastructure-ai-platform

**Repository / product**

- Repository: [https://github.com/ilee165/network-infrastructure-ai-platform](https://github.com/ilee165/network-infrastructure-ai-platform)
- Company: Unknown — not stated in the repository
- Product: AI Network Operations Platform
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.30 / 5
- Confidence: high
- Gate cap applied: **40** — the weighted calculation produced a higher number, but a qualification-gate condition capped it (SCORING_MODEL.md section 14)

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_2`, window `size:>16000`, rank 21
  - Query: `"weasyprint" filename:pyproject.toml size:>16000`
  - Retrieved 30 of 38 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [backend/pyproject.toml](https://github.com/ilee165/network-infrastructure-ai-platform/blob/main/backend/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [backend/requirements.lock.txt](https://github.com/ilee165/network-infrastructure-ai-platform/blob/main/backend/requirements.lock.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/ilee165/network-infrastructure-ai-platform/blob/40d73bbd3a9c9d29a7b20ab38fd0a9af0e1fe413/backend/app/engines/reports/render.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/ilee165/network-infrastructure-ai-platform/blob/40d73bbd3a9c9d29a7b20ab38fd0a9af0e1fe413/backend/app/engines/reports/__init__.py)

**Evidence trail**

- [api_response](https://github.com/ilee165/network-infrastructure-ai-platform) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/ilee165/network-infrastructure-ai-platform/blob/main/backend/pyproject.toml) (source: github_api): # GHSA-cpwx-vrp4-4pq7 sandbox escapes; re-review 2026-09-23). WeasyPrint
- [manifest_line](https://github.com/ilee165/network-infrastructure-ai-platform/blob/main/backend/requirements.lock.txt) (source: github_api): #   weasyprint
- [code_permalink](https://github.com/ilee165/network-infrastructure-ai-platform/blob/40d73bbd3a9c9d29a7b20ab38fd0a9af0e1fe413/backend/app/engines/reports/render.py) (source: github_api): PDF: WeasyPrint behind :func:`_deny_all_url_fetcher` — every URL hard-fails except ``data:`` URIs and ``file:`` paths INSIDE the packaged template
- [code_permalink](https://github.com/ilee165/network-infrastructure-ai-platform/blob/40d73bbd3a9c9d29a7b20ab38fd0a9af0e1fe413/backend/app/engines/reports/__init__.py) (source: github_api): ``extra="forbid"``), enforces the fail-closed redaction contract at ONE choke point (:func:`app.engines.reports.redaction.enforce_redaction` inside the single :func:`app.engines.reports.render.render_
- [readme_excerpt](https://github.com/ilee165/network-infrastructure-ai-platform/blob/main/README.md) (source: readme): A self-hosted, AI-powered Network Operations Platform for enterprise infrastructure teams.

### 14. FERAL-AI/FERAL-AI

**Repository / product**

- Repository: [https://github.com/feral-ai/feral-ai](https://github.com/feral-ai/feral-ai)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://docs.feral.sh

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.15 / 5
- Confidence: high
- Gate cap applied: **40** — the weighted calculation produced a higher number, but a qualification-gate condition capped it (SCORING_MODEL.md section 14)

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 1 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:>16000`, rank 13
  - Query: `"PyMuPDF" filename:pyproject.toml size:>16000`
  - Retrieved 30 of 126 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/FERAL-AI/FERAL-AI/blob/bdd9c17bd6a1910cc5f79d3c37206fbf59414347/feral-core/memory/ingest.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/FERAL-AI/FERAL-AI/blob/bdd9c17bd6a1910cc5f79d3c37206fbf59414347/feral-core/skills/impl/pdf_reader.py)

**Evidence trail**

- [api_response](https://github.com/FERAL-AI/FERAL-AI) (source: github_api): stars=123, fork=False, archived=False
- [code_permalink](https://github.com/FERAL-AI/FERAL-AI/blob/bdd9c17bd6a1910cc5f79d3c37206fbf59414347/feral-core/memory/ingest.py) (source: github_api): raise ValueError("path must point to a .pdf file")         try:             import fitz  # PyMuPDF         except ImportError as e:             raise ValueError("PyMuPDF is required for P
- [code_permalink](https://github.com/FERAL-AI/FERAL-AI/blob/bdd9c17bd6a1910cc5f79d3c37206fbf59414347/feral-core/skills/impl/pdf_reader.py) (source: github_api): try:         import fitz  # PyMuPDF         return fitz
- [other](https://github.com/FERAL-AI/FERAL-AI/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/FERAL-AI/FERAL-AI/blob/main/README.md) (source: readme): **Server-driven UI (Gen-UI)** — the brain emits structured UI payloads; clients render them.

### 15. AmrasElessar/adminpdftoolkit

**Repository / product**

- Repository: [https://github.com/amraselessar/adminpdftoolkit](https://github.com/amraselessar/adminpdftoolkit)
- Company: Unknown — not stated in the repository
- Product: Admin PDF Toolkit
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://github.com/AmrasElessar/adminpdftoolkit/releases

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.10 / 5
- Confidence: high
- Gate cap applied: **40** — the weighted calculation produced a higher number, but a qualification-gate condition capped it (SCORING_MODEL.md section 14)

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `pdf2docx`, run `run_2`, window `size:4001..8000`, rank 7
  - Query: `"pdf2docx" filename:pyproject.toml size:4001..8000`
  - Retrieved 10 of 10 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pdf2docx` (other_processing, mixed) — manifest_declaration — [pyproject.toml](https://github.com/AmrasElessar/adminpdftoolkit/blob/main/pyproject.toml)
- `pdf2docx` (other_processing, mixed) — manifest_declaration — [requirements.txt](https://github.com/AmrasElessar/adminpdftoolkit/blob/main/requirements.txt)
- `pdf2docx` (other_processing, mixed) — code_import — [code](https://github.com/AmrasElessar/adminpdftoolkit/blob/88755e06dd053ed9cbb36ae09995fdc9e5d06565/pdf_converter.py)
- `pdf2docx` (other_processing, mixed) — code_import — [code](https://github.com/AmrasElessar/adminpdftoolkit/blob/88755e06dd053ed9cbb36ae09995fdc9e5d06565/pipelines/convert.py)

**Evidence trail**

- [api_response](https://github.com/AmrasElessar/adminpdftoolkit) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/AmrasElessar/adminpdftoolkit/blob/main/pyproject.toml) (source: github_api): "pdf2docx>=0.5.12,<1.0",
- [manifest_line](https://github.com/AmrasElessar/adminpdftoolkit/blob/main/requirements.txt) (source: github_api): pdf2docx>=0.5.12,<1.0
- [code_permalink](https://github.com/AmrasElessar/adminpdftoolkit/blob/88755e06dd053ed9cbb36ae09995fdc9e5d06565/pdf_converter.py) (source: github_api): Heavy imports (``openpyxl``, ``pdf2docx``) are deferred into the functions that use them so the spawn-mode batch worker (see ``core.batch
- [code_permalink](https://github.com/AmrasElessar/adminpdftoolkit/blob/88755e06dd053ed9cbb36ae09995fdc9e5d06565/pipelines/convert.py) (source: github_api): * :func:`batch_files_worker` — N PDFs → one ZIP of .docx or per-PDF JPG dirs. * :class:`Pdf2DocxProgressHandler` — logging shim that turns pdf2docx's   ``(i/N)`` progress lines into per-page progress
- [other](https://github.com/AmrasElessar/adminpdftoolkit/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/AmrasElessar/adminpdftoolkit/blob/main/README.md) (source: readme): <details> <summary>🇬🇧 At a glance (English)</summary> **Admin PDF Toolkit** is a **LAN-first, offline, open-source PDF processing pipeline** built for KVKK-compliant in-house deployments.

### 16. AnujaK/restfiddle

**Repository / product**

- Repository: [https://github.com/anujak/restfiddle](https://github.com/anujak/restfiddle)
- Company: BootSimply Solutions  Licensed
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://www.restfiddle.com/

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.00 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 8
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 8
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [build.gradle](https://github.com/AnujaK/restfiddle/blob/master/build.gradle)
- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/AnujaK/restfiddle/blob/master/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/AnujaK/restfiddle/blob/5851bb30cc87d185dd1f57863b88ba9230ff52b5/src/main/java/com/restfiddle/controller/rest/ReportController.java)

**Evidence trail**

- [api_response](https://github.com/AnujaK/restfiddle) (source: github_api): stars=138, fork=False, archived=False
- [readme_excerpt](https://github.com/AnujaK/restfiddle/blob/master/README.md) (source: readme): company stated as 'BootSimply Solutions\n\nLicensed'
- [manifest_line](https://github.com/AnujaK/restfiddle/blob/master/build.gradle) (source: github_api): compile(group: 'net.sf.jasperreports', name: 'jasperreports', version:'6.0.0') {
- [manifest_line](https://github.com/AnujaK/restfiddle/blob/master/pom.xml) (source: github_api): <groupId>net.sf.jasperreports</groupId>
- [code_permalink](https://github.com/AnujaK/restfiddle/blob/5851bb30cc87d185dd1f57863b88ba9230ff52b5/src/main/java/com/restfiddle/controller/rest/ReportController.java) (source: github_api): import javax.servlet.http.HttpServletResponse; import net.sf.jasperreports.engine.JRException; import net.sf.jasperreports.engine.JasperExportManager; import net.sf.jasperreports.engine.JasperFillMa
- [readme_excerpt](https://github.com/AnujaK/restfiddle/blob/master/README.md) (source: readme): [RESTFiddle](http://www.restfiddle.com/) An Enterprise-grade API Management Platform for Teams.

### 17. shehanrathnayake/checkpoint-pos-system

**Repository / product**

- Repository: [https://github.com/shehanrathnayake/checkpoint-pos-system](https://github.com/shehanrathnayake/checkpoint-pos-system)
- Company: Unknown — not stated in the repository
- Product: CheckPoint POS System
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://medium.com/@shehan_rathnayake/my-experience-in-point-of-sale-system-project-af15e4cada95

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.00 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 28
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 28
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/shehanrathnayake/checkpoint-pos-system/blob/main/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/shehanrathnayake/checkpoint-pos-system/blob/a31c4b8ef42fff56002861941757db6e62cf8c7d/src/main/java/lk/ijse/dep11/app/controller/OrderSceneController.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/shehanrathnayake/checkpoint-pos-system/blob/a31c4b8ef42fff56002861941757db6e62cf8c7d/src/main/java/lk/ijse/dep11/app/controller/PlaceOrderSceneController.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/shehanrathnayake/checkpoint-pos-system/blob/a31c4b8ef42fff56002861941757db6e62cf8c7d/src/main/java/lk/ijse/dep11/app/controller/UserProfileSceneController.java)

**Evidence trail**

- [api_response](https://github.com/shehanrathnayake/checkpoint-pos-system) (source: github_api): stars=13, fork=False, archived=False
- [manifest_line](https://github.com/shehanrathnayake/checkpoint-pos-system/blob/main/pom.xml) (source: github_api): <!-- https://mvnrepository.com/artifact/net.sf.jasperreports/jasperreports -->
- [code_permalink](https://github.com/shehanrathnayake/checkpoint-pos-system/blob/a31c4b8ef42fff56002861941757db6e62cf8c7d/src/main/java/lk/ijse/dep11/app/controller/OrderSceneController.java) (source: github_api): import lk.ijse.dep11.app.common.WindowNavigation; import lk.ijse.dep11.app.db.OrderDataAccess; import lk.ijse.dep11.app.tm.Order; import net.sf.jasperreports.engine.*; import net.sf.jasperreports.engi
- [code_permalink](https://github.com/shehanrathnayake/checkpoint-pos-system/blob/a31c4b8ef42fff56002861941757db6e62cf8c7d/src/main/java/lk/ijse/dep11/app/controller/PlaceOrderSceneController.java) (source: github_api): import lk.ijse.dep11.app.tm.Customer; import lk.ijse.dep11.app.tm.Item; import lk.ijse.dep11.app.tm.OrderItem; import net.sf.jasperreports.engine.*; import net.sf.jasperreports.engine.data.JRBeanColle
- [code_permalink](https://github.com/shehanrathnayake/checkpoint-pos-system/blob/a31c4b8ef42fff56002861941757db6e62cf8c7d/src/main/java/lk/ijse/dep11/app/controller/UserProfileSceneController.java) (source: github_api): import lk.ijse.dep11.app.db.UserDataAccess; import lk.ijse.dep11.app.tm.User; import lk.ijse.dep11.app.tm.UserRole; import net.sf.jasperreports.components.items.ItemProperty; import org.apache.commons
- [readme_excerpt](https://github.com/shehanrathnayake/checkpoint-pos-system/blob/main/README.md) (source: readme): [SRS Document](SRS-Document.pdf) <img src="ref-images/dashboard-mock.png" width="600px" height="auto"> In this project, I have designed a Java based POS system to streamline transactions for retail cu

### 18. jolie-z/Auto-JobHunter

**Repository / product**

- Repository: [https://github.com/jolie-z/auto-jobhunter](https://github.com/jolie-z/auto-jobhunter)
- Company: Unknown — not stated in the repository
- Product: 🚀 Auto-Job-Hunter \| 全自动 AI 求职
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.30 / 5
- Confidence: high
- Gate cap applied: **40** — the weighted calculation produced a higher number, but a qualification-gate condition capped it (SCORING_MODEL.md section 14)

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 24
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 24
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [requirements.txt](https://github.com/jolie-z/Auto-JobHunter/blob/main/requirements.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/jolie-z/Auto-JobHunter/blob/4f9dec38978035a87d34cab5b15914dc8688e6f0/jobhunter-backend/main.py)

**Evidence trail**

- [api_response](https://github.com/jolie-z/Auto-JobHunter) (source: github_api): stars=70, fork=False, archived=False
- [manifest_line](https://github.com/jolie-z/Auto-JobHunter/blob/main/requirements.txt) (source: github_api): docxtpl>=0.16.7             # Word 模板变量渲染 (from docxtpl import DocxTemplate, RichText)
- [code_permalink](https://github.com/jolie-z/Auto-JobHunter/blob/4f9dec38978035a87d34cab5b15914dc8688e6f0/jobhunter-backend/main.py) (source: github_api): from openai import OpenAI from pdf2image import convert_from_path from pydantic import BaseModel from docxtpl import DocxTemplate, RichText # 🌟 修改 1：去掉了废弃的表 ID 导入 from common.config import (     FEISH
- [readme_excerpt](https://github.com/jolie-z/Auto-JobHunter/blob/main/readme.md) (source: readme): 本项目源代码及相关文档仅供**个人学习、技术研究及非商业性质的交流使用**。 未经作者（[name redacted]）明确书面许可，严禁将本项目用于任何形式的商业用途（包括但不限于：作为 SaaS 服务提供、二次打包售卖、嵌入商业产品中牟利等）。商用授权请联系作者沟通。

### 19. anki291103/Event4U

**Repository / product**

- Repository: [https://github.com/anki291103/event4u](https://github.com/anki291103/event4u)
- Company: Unknown — not stated in the repository
- Product: Event4U – Event Management System
- Industry: events_weddings (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://gourmaze-food-delivery-app-a59z.vercel.app

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.00 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 3 |
| Pipeline complexity | 1 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `iText`, run `run_2`, window `size:2001..4000`, rank 29
  - Query: `"itext" filename:packages.config size:2001..4000`
  - Sampled 30 of 1,368 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,368 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `iText` (pdf, generation) — manifest_declaration — [Event4U.csproj](https://github.com/anki291103/Event4U/blob/master/Event4U.csproj)
- `iText` (pdf, generation) — manifest_declaration — [packages.config](https://github.com/anki291103/Event4U/blob/master/packages.config)
- `iText` (pdf, generation) — code_import — [code](https://github.com/anki291103/Event4U/blob/63ef7af1ccf71043d2e29f71193a8f07aa528b7a/Controllers/AdminController.cs)

**Evidence trail**

- [api_response](https://github.com/anki291103/Event4U) (source: github_api): stars=1, fork=False, archived=False
- [manifest_line](https://github.com/anki291103/Event4U/blob/master/Event4U.csproj) (source: github_api): <Reference Include="itext.barcodes, Version=9.1.0.0, Culture=neutral, PublicKeyToken=8354ae6d2174ddca, processorArchitecture=MSIL">
- [manifest_line](https://github.com/anki291103/Event4U/blob/master/packages.config) (source: github_api): <package id="itext" version="9.1.0" targetFramework="net472" />
- [code_permalink](https://github.com/anki291103/Event4U/blob/63ef7af1ccf71043d2e29f71193a8f07aa528b7a/Controllers/AdminController.cs) (source: github_api): using System.Web.Mvc; using Event4U.Models; // Ensure this includes your context and view model namespaces using Event4U.Models.ViewModel; using iText.Kernel.Pdf; using iText.Layout.Element; using iTe
- [readme_excerpt](https://github.com/anki291103/Event4U/blob/master/README.md) (source: readme): It allows users to manage events, bookings, and provides functionalities for both customers and event organizers.

### 20. TuiQiao/CBoard

**Repository / product**

- Repository: [https://github.com/tuiqiao/cboard](https://github.com/tuiqiao/cboard)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://tuiqiao.github.io/CBoardDoc/#/

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.10 / 5
- Confidence: medium
- Gate cap applied: **40** — the weighted calculation produced a higher number, but a qualification-gate condition capped it (SCORING_MODEL.md section 14)

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `Apache POI (XWPF/HWPF)`, run `run_2`, window `size:>16000`, rank 1
  - Query: `"poi" filename:pom.xml size:>16000`
  - Sampled 30 of 15,200 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 15,200 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Apache POI (XWPF/HWPF)` (docx, generation) — manifest_declaration — [pom.xml](https://github.com/TuiQiao/CBoard/blob/branch-0.4.2/pom.xml)
- `Apache POI (XWPF/HWPF)` (docx, generation) — code_import — [code](https://github.com/TuiQiao/CBoard/blob/67a2e9165bb71c94392f8ba4eab6d8eb7b58b3f3/src/main/java/org/cboard/services/persist/excel/XlsProcesser.java)
- `Apache POI (XWPF/HWPF)` (docx, generation) — code_import — [code](https://github.com/TuiQiao/CBoard/blob/67a2e9165bb71c94392f8ba4eab6d8eb7b58b3f3/src/main/java/org/cboard/services/MailService.java)
- `Apache POI (XWPF/HWPF)` (docx, generation) — code_import — [code](https://github.com/TuiQiao/CBoard/blob/67a2e9165bb71c94392f8ba4eab6d8eb7b58b3f3/src/main/java/org/cboard/services/persist/excel/JpgXlsProcesser.java)
- `Apache POI (XWPF/HWPF)` (docx, generation) — code_import — [code](https://github.com/TuiQiao/CBoard/blob/67a2e9165bb71c94392f8ba4eab6d8eb7b58b3f3/src/main/java/org/cboard/services/persist/excel/XlsProcesserContext.java)
- `Apache POI (XWPF/HWPF)` (docx, generation) — code_import — [code](https://github.com/TuiQiao/CBoard/blob/67a2e9165bb71c94392f8ba4eab6d8eb7b58b3f3/src/main/java/org/cboard/services/persist/excel/TableXlsProcesser.java)

**Evidence trail**

- [api_response](https://github.com/TuiQiao/CBoard) (source: github_api): stars=3098, fork=False, archived=False
- [manifest_line](https://github.com/TuiQiao/CBoard/blob/branch-0.4.2/pom.xml) (source: github_api): <groupId>org.apache.poi</groupId>
- [code_permalink](https://github.com/TuiQiao/CBoard/blob/67a2e9165bb71c94392f8ba4eab6d8eb7b58b3f3/src/main/java/org/cboard/services/persist/excel/XlsProcesser.java) (source: github_api): package org.cboard.services.persist.excel; import com.alibaba.fastjson.JSONObject; import org.apache.poi.ss.usermodel.Cell; import org.apache.poi.ss.usermodel.ClientAnchor; import org.apache.poi.ss.u
- [code_permalink](https://github.com/TuiQiao/CBoard/blob/67a2e9165bb71c94392f8ba4eab6d8eb7b58b3f3/src/main/java/org/cboard/services/MailService.java) (source: github_api): import org.apache.commons.mail.EmailException; import org.apache.commons.mail.HtmlEmail; import org.apache.poi.hssf.record.crypto.Biff8EncryptionKey; import org.apache.poi.hssf.usermodel.HSSFWorkbook;
- [code_permalink](https://github.com/TuiQiao/CBoard/blob/67a2e9165bb71c94392f8ba4eab6d8eb7b58b3f3/src/main/java/org/cboard/services/persist/excel/JpgXlsProcesser.java) (source: github_api): package org.cboard.services.persist.excel; import org.apache.poi.ss.usermodel.*; import java.util.Base64; /**
- [code_permalink](https://github.com/TuiQiao/CBoard/blob/67a2e9165bb71c94392f8ba4eab6d8eb7b58b3f3/src/main/java/org/cboard/services/persist/excel/XlsProcesserContext.java) (source: github_api): package org.cboard.services.persist.excel; import com.alibaba.fastjson.JSONObject; import org.apache.poi.ss.usermodel.CellStyle; import org.apache.poi.ss.usermodel.Sheet; import org.apache.poi.ss.use
- [code_permalink](https://github.com/TuiQiao/CBoard/blob/67a2e9165bb71c94392f8ba4eab6d8eb7b58b3f3/src/main/java/org/cboard/services/persist/excel/TableXlsProcesser.java) (source: github_api): import com.alibaba.fastjson.JSONArray; import com.alibaba.fastjson.JSONObject; import org.apache.poi.hssf.usermodel.HSSFClientAnchor; import org.apache.poi.ss.usermodel.*; import org.apache.poi.ss.ut
- [readme_excerpt](https://github.com/TuiQiao/CBoard/blob/branch-0.4.2/README.md) (source: readme): CBoard is not only a analysis platform that supports interactive multi-dimensional report design and data analysis for user, but also a BI product development platform for developer.

### 21. pandora-analysis/pandora

**Repository / product**

- Repository: [https://github.com/pandora-analysis/pandora](https://github.com/pandora-analysis/pandora)
- Company: Unknown — not stated in the repository
- Product: Pandora
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://pandora.circl.lu/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.00 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:>16000`, rank 9
  - Query: `"PyMuPDF" filename:pyproject.toml size:>16000`
  - Retrieved 30 of 126 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `pikepdf`, run `run_2`, window `size:>16000`, rank 1
  - Query: `"pikepdf" filename:pyproject.toml size:>16000`
  - Retrieved 6 of 6 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `WeasyPrint`, run `run_2`, window `size:>16000`, rank 4
  - Query: `"weasyprint" filename:pyproject.toml size:>16000`
  - Retrieved 30 of 38 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [pyproject.toml](https://github.com/pandora-analysis/pandora/blob/main/pyproject.toml)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/pandora-analysis/pandora/blob/4f096fb704755b1d47e6eef55505fb8944fa7efb/pandora/workers/pdf.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/pandora-analysis/pandora/blob/4f096fb704755b1d47e6eef55505fb8944fa7efb/pandora/file.py)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/pandora-analysis/pandora/blob/main/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/pandora-analysis/pandora/blob/4f096fb704755b1d47e6eef55505fb8944fa7efb/pandora/file.py)
- `pikepdf` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/pandora-analysis/pandora/blob/main/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/pandora-analysis/pandora) (source: github_api): stars=282, fork=False, archived=False
- [manifest_line](https://github.com/pandora-analysis/pandora/blob/main/pyproject.toml) (source: github_api): PyMuPDF = "^1.28.2"
- [code_permalink](https://github.com/pandora-analysis/pandora/blob/4f096fb704755b1d47e6eef55505fb8944fa7efb/pandora/workers/pdf.py) (source: github_api): import re from typing import Any import pymupdf from pymupdf import Document from ..helpers import Status
- [code_permalink](https://github.com/pandora-analysis/pandora/blob/4f096fb704755b1d47e6eef55505fb8944fa7efb/pandora/file.py) (source: github_api): import exiftool  # type: ignore[import-untyped] import pymupdf import pikepdf
- [manifest_line](https://github.com/pandora-analysis/pandora/blob/main/pyproject.toml) (source: github_api): weasyprint = "^69.0"
- [code_permalink](https://github.com/pandora-analysis/pandora/blob/4f096fb704755b1d47e6eef55505fb8944fa7efb/pandora/file.py) (source: github_api): import textract  # type: ignore[import-untyped] from weasyprint import HTML, default_url_fetcher  # type: ignore[import-untyped]
- [manifest_line](https://github.com/pandora-analysis/pandora/blob/main/pyproject.toml) (source: github_api): pikepdf = "^10.11.0"

### 22. nhiney/database-security

**Repository / product**

- Repository: [https://github.com/nhiney/database-security](https://github.com/nhiney/database-security)
- Company: Unknown — not stated in the repository
- Product: Secure E-Commerce Shoe Shop System
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.30 / 5
- Confidence: medium
- Gate cap applied: **40** — the weighted calculation produced a higher number, but a qualification-gate condition capped it (SCORING_MODEL.md section 14)

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 3 |
| Pipeline complexity | 1 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `iText`, run `run_2`, window `size:2001..4000`, rank 26
  - Query: `"itext" filename:packages.config size:2001..4000`
  - Sampled 30 of 1,368 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,368 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `iText` (pdf, generation) — manifest_declaration — [DA_N6.csproj](https://github.com/nhiney/database-security/blob/main/DA_N6.csproj)
- `iText` (pdf, generation) — manifest_declaration — [packages.config](https://github.com/nhiney/database-security/blob/main/packages.config)
- `iText` (pdf, generation) — code_import — [code](https://github.com/nhiney/database-security/blob/3a0d44c0836b6bb3f6affb27fa9f5335156105ed/Views/Orders/OrderDetailsForm.cs)
- `iText` (pdf, generation) — code_import — [code](https://github.com/nhiney/database-security/blob/3a0d44c0836b6bb3f6affb27fa9f5335156105ed/Views/Cart/CartForm.cs)

**Evidence trail**

- [api_response](https://github.com/nhiney/database-security) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/nhiney/database-security/blob/main/DA_N6.csproj) (source: github_api): <Reference Include="itext.barcodes, Version=9.4.0.0, Culture=neutral, PublicKeyToken=8354ae6d2174ddca, processorArchitecture=MSIL">
- [manifest_line](https://github.com/nhiney/database-security/blob/main/packages.config) (source: github_api): <package id="itext" version="9.4.0" targetFramework="net48" />
- [code_permalink](https://github.com/nhiney/database-security/blob/3a0d44c0836b6bb3f6affb27fa9f5335156105ed/Views/Orders/OrderDetailsForm.cs) (source: github_api): var fCompany = new iTextSharp.text.Font(bf, 14, iTextSharp.text.Font.BOLD, BaseColor.BLACK);                 var fInfo = new iTextSharp.text.Font(bf, 10, iTextSharp.text.Font.NORMAL,
- [code_permalink](https://github.com/nhiney/database-security/blob/3a0d44c0836b6bb3f6affb27fa9f5335156105ed/Views/Cart/CartForm.cs) (source: github_api): using System.IO; using System.Diagnostics; using iTextSharp.text; using iTextSharp.text.pdf;
- [readme_excerpt](https://github.com/nhiney/database-security/blob/main/README.md) (source: readme): [Conclusion](#conclusion) This project simulates a real-world e-commerce shoe shop where customers can browse products, place orders (Cash on Delivery), and manage their accounts — while administrator

### 23. vectara/vectara-ingest

**Repository / product**

- Repository: [https://github.com/vectara/vectara-ingest](https://github.com/vectara/vectara-ingest)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://vectara.com

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=3, pipeline_stage_count=0 \| supporting: category_count=3

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.00 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 4 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Document volume: Unknown

**Discovery provenance**

- Tier 3, `pypdf / PyPDF2`, run `run_2`, window `size:>16000`, rank 6
  - Query: `"pypdf" filename:requirements.txt size:>16000`
  - Sampled 30 of 1,476 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,476 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `pikepdf`, run `run_2`, window `size:>16000`, rank 1
  - Query: `"pikepdf" filename:requirements.txt size:>16000`
  - Retrieved 30 of 98 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Unstructured`, run `run_2`, window `size:>16000`, rank 2
  - Query: `"unstructured" filename:requirements.txt size:>16000`
  - Retrieved 30 of 227 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Docling`, run `run_2`, window `size:>16000`, rank 1
  - Query: `"docling" filename:requirements.txt size:>16000`
  - Retrieved 30 of 69 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `python-docx`, run `run_2`, window `size:>16000`, rank 4
  - Query: `"python-docx" filename:requirements.txt size:>16000`
  - Retrieved 30 of 571 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Docling` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/vectara/vectara-ingest/blob/main/requirements.txt)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/vectara/vectara-ingest/blob/aa82b4e480c233742b2abdcc259e8fdcd233efbe/docker/bin/download-docling-models.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/vectara/vectara-ingest/blob/aa82b4e480c233742b2abdcc259e8fdcd233efbe/core/file_processor.py)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements-extra.txt](https://github.com/vectara/vectara-ingest/blob/main/requirements-extra.txt)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/vectara/vectara-ingest/blob/main/requirements.txt)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/vectara/vectara-ingest/blob/aa82b4e480c233742b2abdcc259e8fdcd233efbe/core/file_processor.py)
- `pikepdf` (pdf, generation) — manifest_declaration — [requirements-extra.txt](https://github.com/vectara/vectara-ingest/blob/main/requirements-extra.txt)
- `pikepdf` (pdf, generation) — manifest_declaration — [requirements.txt](https://github.com/vectara/vectara-ingest/blob/main/requirements.txt)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [requirements-extra.txt](https://github.com/vectara/vectara-ingest/blob/main/requirements-extra.txt)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [requirements.txt](https://github.com/vectara/vectara-ingest/blob/main/requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [requirements-extra.txt](https://github.com/vectara/vectara-ingest/blob/main/requirements-extra.txt)
- `python-docx` (docx, generation) — manifest_declaration — [requirements.txt](https://github.com/vectara/vectara-ingest/blob/main/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/vectara/vectara-ingest) (source: github_api): stars=195, fork=False, archived=False
- [manifest_line](https://github.com/vectara/vectara-ingest/blob/main/requirements.txt) (source: github_api): #   docling-ibm-models
- [code_permalink](https://github.com/vectara/vectara-ingest/blob/aa82b4e480c233742b2abdcc259e8fdcd233efbe/docker/bin/download-docling-models.py) (source: github_api): from docling.datamodel.layout_model_specs import DOCLING_LAYOUT_HERON_101, DOCLING_LAYOUT_V2 from docling.models.stages.layout.layout_model import LayoutModel
- [code_permalink](https://github.com/vectara/vectara-ingest/blob/aa82b4e480c233742b2abdcc259e8fdcd233efbe/core/file_processor.py) (source: github_api): self.summarize_images = cfg.doc_processing.get("summarize_images", False)         self.doc_parser = cfg.doc_processing.get("doc_parser", "docling")         self.contextual_chunking = cfg.doc_p
- [manifest_line](https://github.com/vectara/vectara-ingest/blob/main/requirements-extra.txt) (source: github_api): #   unstructured-inference
- [manifest_line](https://github.com/vectara/vectara-ingest/blob/main/requirements.txt) (source: github_api): #   unstructured-inference
- [code_permalink](https://github.com/vectara/vectara-ingest/blob/aa82b4e480c233742b2abdcc259e8fdcd233efbe/core/file_processor.py) (source: github_api): self.image_context = cfg.doc_processing.get("image_context", {'num_previous_chunks': 1, 'num_next_chunks': 1})                  # Parser configurations         self.unstructured_config = cfg.d
- [manifest_line](https://github.com/vectara/vectara-ingest/blob/main/requirements-extra.txt) (source: github_api): #   pikepdf
- [manifest_line](https://github.com/vectara/vectara-ingest/blob/main/requirements.txt) (source: github_api): #   pikepdf
- [manifest_line](https://github.com/vectara/vectara-ingest/blob/main/requirements-extra.txt) (source: github_api): pypdf==6.14.2
- [manifest_line](https://github.com/vectara/vectara-ingest/blob/main/requirements.txt) (source: github_api): pypdf==6.14.2
- [manifest_line](https://github.com/vectara/vectara-ingest/blob/main/requirements-extra.txt) (source: github_api): #   python-docx
- [manifest_line](https://github.com/vectara/vectara-ingest/blob/main/requirements.txt) (source: github_api): #   python-docx
- [readme_excerpt](https://github.com/vectara/vectara-ingest/blob/main/README.md) (source: readme): **`extract.py`:** Utilities for text extraction from HTML **`utils.py`:** Some utility functions used by the other code.

### 24. Ubada-Hussain/FormFixer

**Repository / product**

- Repository: [https://github.com/ubada-hussain/formfixer](https://github.com/ubada-hussain/formfixer)
- Company: Unknown — not stated in the repository
- Product: FormFixer
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: formfixer.online

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=2, pipeline_stage_count=1 \| supporting: category_count=2; multiple_document_types_handled=true; confirmed generation/conversion code

**Score**

- Score: 38/100 (a score, not a probability)
- Raw weighted score: 1.90 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 3 |
| Pipeline complexity | 1 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 1 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 11
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `pdf2docx`, run `run_1`, window `size:251..500`, rank 4
  - Query: `"pdf2docx" filename:requirements.txt size:251..500`
  - Retrieved 30 of 247 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 11
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/Ubada-Hussain/FormFixer/blob/b527fe94296418f59f0fcc9e7748bfdc839a2d01/app/api/convert/route.ts)
- `pdf2docx` (other_processing, mixed) — code_import — [code](https://github.com/Ubada-Hussain/FormFixer/blob/b527fe94296418f59f0fcc9e7748bfdc839a2d01/services/pdf2docx-service/main.py)
- `pdf2docx` (other_processing, mixed) — manifest_declaration — [services/pdf2docx-service/requirements.txt](https://github.com/Ubada-Hussain/FormFixer/blob/b527fe94296418f59f0fcc9e7748bfdc839a2d01/services/pdf2docx-service/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/Ubada-Hussain/FormFixer) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/Ubada-Hussain/FormFixer/blob/b527fe94296418f59f0fcc9e7748bfdc839a2d01/app/api/convert/route.ts) (source: github_api): contentType = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document';     }   } else {     // Office → PDF via Gotenberg     const gotenbergUrl = resolveServiceUrl(process.env
- [code_permalink](https://github.com/Ubada-Hussain/FormFixer/blob/b527fe94296418f59f0fcc9e7748bfdc839a2d01/services/pdf2docx-service/main.py) (source: github_api): app = FastAPI(title="pdf2docx-service", version="1.0.0")
- [manifest_line](https://github.com/Ubada-Hussain/FormFixer/blob/b527fe94296418f59f0fcc9e7748bfdc839a2d01/services/pdf2docx-service/requirements.txt) (source: github_api): uvicorn[standard]==0.30.1 # pdf2docx-headless uses opencv-python-headless (no GUI/libGL deps — required on Railway) # Latest available version on PyPI is 0.5.8 pdf2docx-headless==0.5.8 python-multipar
- [readme_excerpt](https://github.com/Ubada-Hussain/FormFixer/blob/main/README.md) (source: readme): FormFixer is an all-in-one toolkit for preparing documents and photos for online applications.

### 25. OpsinTech/opsintech-platform

**Repository / product**

- Repository: [https://github.com/opsintech/opsintech-platform](https://github.com/opsintech/opsintech-platform)
- Company: Unknown — not stated in the repository
- Product: OpsinTech Platform
- Industry: real_estate (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://www.opsintech.net

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 38/100 (a score, not a probability)
- Raw weighted score: 1.90 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:4001..8000`, rank 12
  - Query: `"mammoth" filename:requirements.txt size:4001..8000`
  - Retrieved 30 of 175 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/OpsinTech/opsintech-platform/blob/5474b29d40bcf68962564f1d8f7b3f16e0f3660a/skills/public/ppt-master/scripts/source_to_md/doc_to_md.py)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [skills/public/ppt-master/requirements.txt](https://github.com/OpsinTech/opsintech-platform/blob/5474b29d40bcf68962564f1d8f7b3f16e0f3660a/skills/public/ppt-master/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/OpsinTech/opsintech-platform) (source: github_api): stars=91, fork=False, archived=False
- [code_permalink](https://github.com/OpsinTech/opsintech-platform/blob/5474b29d40bcf68962564f1d8f7b3f16e0f3660a/skills/public/ppt-master/scripts/source_to_md/doc_to_md.py) (source: github_api): Primary formats (pure Python, no external tools required):     .docx   → mammoth     .html   → markdownify + BeautifulSoup
- [manifest_line](https://github.com/OpsinTech/opsintech-platform/blob/5474b29d40bcf68962564f1d8f7b3f16e0f3660a/skills/public/ppt-master/requirements.txt) (source: github_api): # 原生路径（纯 Python，无需外部程序）： #   .docx   → mammoth #   .html   → markdownify (+ beautifulsoup4, listed below)
- [readme_excerpt](https://github.com/OpsinTech/opsintech-platform/blob/main/README.md) (source: readme): [中文](./README_zh.md) \| English OpsinTech is an **AI-Native Operations Platform for production environments**.

### 26. hereugo-ak/Hyperion

**Repository / product**

- Repository: [https://github.com/hereugo-ak/hyperion](https://github.com/hereugo-ak/hyperion)
- Company: HYPERION Consulting
- Product: Unknown
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: contributor_count not collected

**Score**

- Score: 38/100 (a score, not a probability)
- Raw weighted score: 1.90 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `pikepdf`, run `run_2`, window `size:8001..16000`, rank 13
  - Query: `"pikepdf" filename:pyproject.toml size:8001..16000`
  - Retrieved 19 of 19 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pikepdf` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/hereugo-ak/Hyperion/blob/main/pyproject.toml)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/hereugo-ak/Hyperion/blob/2b06e20217515743f1245c4670a5c7f5c4b44012/hyperion/output/pdf_postprocess.py)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/hereugo-ak/Hyperion/blob/2b06e20217515743f1245c4670a5c7f5c4b44012/hyperion/output/render.py)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/hereugo-ak/Hyperion/blob/2b06e20217515743f1245c4670a5c7f5c4b44012/scripts/verify_playwright_cover.py)

**Evidence trail**

- [api_response](https://github.com/hereugo-ak/Hyperion) (source: github_api): stars=0, fork=False, archived=False
- [readme_excerpt](https://github.com/hereugo-ak/Hyperion/blob/main/README.md) (source: readme): company stated as 'HYPERION Consulting'
- [manifest_line](https://github.com/hereugo-ak/Hyperion/blob/main/pyproject.toml) (source: github_api): "pikepdf>=9.0.0",
- [code_permalink](https://github.com/hereugo-ak/Hyperion/blob/2b06e20217515743f1245c4670a5c7f5c4b44012/hyperion/output/pdf_postprocess.py) (source: github_api): This is NOT a generic "tidy the PDF" wrapper. It: - Runs pikepdf lazily — the module is importable without pikepdf installed   (985MB sandbox); the caller degrades to the un-post-processed PDF with a
- [code_permalink](https://github.com/hereugo-ak/Hyperion/blob/2b06e20217515743f1245c4670a5c7f5c4b44012/hyperion/output/render.py) (source: github_api): # zero-margin, furniture-free page and merged ahead of the body with     # pikepdf. Any failure in the split/merge legs degrades to the previous     # single-pass behaviour (cover inset) — never a
- [code_permalink](https://github.com/hereugo-ak/Hyperion/blob/2b06e20217515743f1245c4670a5c7f5c4b44012/scripts/verify_playwright_cover.py) (source: github_api): uses, where WeasyPrint GTK natives are unavailable) and checks:   - the cover is rendered as its OWN zero-margin, furniture-free page,   - body pages keep the margins + running header/footer,   - pike
- [other](https://github.com/hereugo-ak/Hyperion/tree/main/reports) (source: github_api): directory reports/ present
- [readme_excerpt](https://github.com/hereugo-ak/Hyperion/blob/main/README.md) (source: readme): It runs entirely on free-tier LLM capacity and is designed to finish an engagement in minutes, not hours.[5] Hyperion is built for the work that sits between an executive question and a defensible rec

### 27. openai/GABRIEL

**Repository / product**

- Repository: [https://github.com/openai/gabriel](https://github.com/openai/gabriel)
- Company: Unknown — not stated in the repository
- Product: GABRIEL
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 37/100 (a score, not a probability)
- Raw weighted score: 1.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden | 3 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `pypdf / PyPDF2`, run `run_2`, window `size:2001..4000`, rank 15
  - Query: `"pypdf" filename:pyproject.toml size:2001..4000`
  - Sampled 30 of 4,000 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 4,000 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_2`, window `size:2001..4000`, rank 16
  - Query: `"python-docx" filename:pyproject.toml size:2001..4000`
  - Sampled 30 of 2,732 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,732 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [pyproject.toml](https://github.com/openai/GABRIEL/blob/main/pyproject.toml)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/openai/GABRIEL/blob/9caced978453d4ae857118eed01ed6abe9e72723/src/gabriel/utils/file_utils.py)
- `python-docx` (docx, generation) — manifest_declaration — [pyproject.toml](https://github.com/openai/GABRIEL/blob/main/pyproject.toml)
- `python-docx` (docx, generation) — code_import — [code](https://github.com/openai/GABRIEL/blob/9caced978453d4ae857118eed01ed6abe9e72723/src/gabriel/utils/file_utils.py)

**Evidence trail**

- [api_response](https://github.com/openai/GABRIEL) (source: github_api): stars=423, fork=False, archived=False
- [manifest_line](https://github.com/openai/GABRIEL/blob/main/pyproject.toml) (source: github_api): "pypdf>=4.0.0",
- [code_permalink](https://github.com/openai/GABRIEL/blob/9caced978453d4ae857118eed01ed6abe9e72723/src/gabriel/utils/file_utils.py) (source: github_api): with open(file_path, "r", encoding="utf-8", errors="ignore") as fh:             return fh.read()     if ext == ".pdf":         pypdf = _optional_import("pypdf", "pypdf")         reader = pypdf
- [manifest_line](https://github.com/openai/GABRIEL/blob/main/pyproject.toml) (source: github_api): "python-docx>=1.1.0",
- [code_permalink](https://github.com/openai/GABRIEL/blob/9caced978453d4ae857118eed01ed6abe9e72723/src/gabriel/utils/file_utils.py) (source: github_api): reader = pypdf.PdfReader(file_path)         return "\n".join(page.extract_text() or "" for page in reader.pages).strip()     if ext == ".docx":         docx = _optional_import("docx", "python-

### 28. seepick/gadsu

**Repository / product**

- Repository: [https://github.com/seepick/gadsu](https://github.com/seepick/gadsu)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 36/100 (a score, not a probability)
- Raw weighted score: 1.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 4 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `iText`, run `run_2`, window `size:8001..16000`, rank 22
  - Query: `"itext" filename:build.gradle size:8001..16000`
  - Retrieved 30 of 318 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `iText` (pdf, generation) — manifest_declaration — [build.gradle](https://github.com/seepick/gadsu/blob/master/build.gradle)
- `iText` (pdf, generation) — code_import — [code](https://github.com/seepick/gadsu/blob/f6a84c42e1985bc53d566730ed0552b3ae71d94b/src/main/kotlin/at/cpickl/gadsu/report/multiprotocol/multiprotocol.kt)
- `iText` (pdf, generation) — code_import — [code](https://github.com/seepick/gadsu/blob/f6a84c42e1985bc53d566730ed0552b3ae71d94b/src/test/kotlin/at/cpickl/gadsu/report/playground.kt)

**Evidence trail**

- [api_response](https://github.com/seepick/gadsu) (source: github_api): stars=3, fork=False, archived=False
- [manifest_line](https://github.com/seepick/gadsu/blob/master/build.gradle) (source: github_api): compile 'com.lowagie:itext:2.1.7'
- [code_permalink](https://github.com/seepick/gadsu/blob/f6a84c42e1985bc53d566730ed0552b3ae71d94b/src/main/kotlin/at/cpickl/gadsu/report/multiprotocol/multiprotocol.kt) (source: github_api): import at.cpickl.gadsu.service.toDateTime import com.google.common.eventbus.EventBus import com.google.inject.AbstractModule import com.itextpdf.text.Document import com.itextpdf.text.Element import c
- [code_permalink](https://github.com/seepick/gadsu/blob/f6a84c42e1985bc53d566730ed0552b3ae71d94b/src/test/kotlin/at/cpickl/gadsu/report/playground.kt) (source: github_api): import com.itextpdf.text.Document import com.itextpdf.text.Element
- [readme_excerpt](https://github.com/seepick/gadsu/blob/master/README.md) (source: readme): Gadsu is a Shiatsu tool which helps you in your daily life as a practitioner, mainly keeping track of clients and their (medical) data, appointments and treatments.

### 29. Cyberwatch/Pentest-Collaboration-Framework

**Repository / product**

- Repository: [https://github.com/cyberwatch/pentest-collaboration-framework](https://github.com/cyberwatch/pentest-collaboration-framework)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 36/100 (a score, not a probability)
- Raw weighted score: 1.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 16
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 16
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [requirements.txt](https://github.com/Cyberwatch/Pentest-Collaboration-Framework/blob/master/requirements.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [requirements_unix.txt](https://github.com/Cyberwatch/Pentest-Collaboration-Framework/blob/master/requirements_unix.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [requirements_windows.txt](https://github.com/Cyberwatch/Pentest-Collaboration-Framework/blob/master/requirements_windows.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/Cyberwatch/Pentest-Collaboration-Framework/blob/6748527734e259a30c945d14d580ac62b13f7f5c/routes/ui/project.py)

**Evidence trail**

- [api_response](https://github.com/Cyberwatch/Pentest-Collaboration-Framework) (source: github_api): stars=37, fork=False, archived=False
- [manifest_line](https://github.com/Cyberwatch/Pentest-Collaboration-Framework/blob/master/requirements.txt) (source: github_api): docxtpl==0.20.2 # template generation
- [manifest_line](https://github.com/Cyberwatch/Pentest-Collaboration-Framework/blob/master/requirements_unix.txt) (source: github_api): docxtpl==0.20.2 # template generation
- [manifest_line](https://github.com/Cyberwatch/Pentest-Collaboration-Framework/blob/master/requirements_windows.txt) (source: github_api): docxtpl==0.20.2 # template generation
- [code_permalink](https://github.com/Cyberwatch/Pentest-Collaboration-Framework/blob/6748527734e259a30c945d14d580ac62b13f7f5c/routes/ui/project.py) (source: github_api): from routes.ui import routes from functools import wraps from docxtpl import DocxTemplate, InlineImage, RichText from docx.shared import Mm from io import BytesIO from system.forms import *
- [other](https://github.com/Cyberwatch/Pentest-Collaboration-Framework/tree/master/templates) (source: github_api): directory templates/ present

### 30. ghk/sideka-electron

**Repository / product**

- Repository: [https://github.com/ghk/sideka-electron](https://github.com/ghk/sideka-electron)
- Company: Unknown — not stated in the repository
- Product: Sideka - Platform Tata Kelola Desa
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://sideka.id

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 35/100 (a score, not a probability)
- Raw weighted score: 1.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 2, `docxtemplater`, run `run_1`, window `unsliced`, rank 26
  - Query: `"docxtemplater" filename:package.json`
  - Sampled 30 of 3,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,256 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtemplater`, run `run_2`, window `unsliced`, rank 26
  - Query: `"docxtemplater" filename:package.json`
  - Sampled 30 of 3,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,256 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtemplater` (docx, generation) — manifest_declaration — [package.json](https://github.com/ghk/sideka-electron/blob/master/package.json)
- `docxtemplater` (docx, generation) — code_import — [code](https://github.com/ghk/sideka-electron/blob/a025d0f949adbd173905b00164e30676d0689866/src/app/components/surat.ts)
- `docxtemplater` (docx, generation) — code_import — [code](https://github.com/ghk/sideka-electron/blob/a025d0f949adbd173905b00164e30676d0689866/src/app/pages/penerimaan.ts)

**Evidence trail**

- [api_response](https://github.com/ghk/sideka-electron) (source: github_api): stars=16, fork=False, archived=False
- [manifest_line](https://github.com/ghk/sideka-electron/blob/master/package.json) (source: github_api): "docxtemplater": "^3.0.11",
- [code_permalink](https://github.com/ghk/sideka-electron/blob/a025d0f949adbd173905b00164e30676d0689866/src/app/components/surat.ts) (source: github_api): import * as path from 'path'; import * as jetpack from 'fs-jetpack'; import * as expressions from 'angular-expressions'; import * as ImageModule from 'docxtemplater-image-module'; import * as JSZip fr
- [code_permalink](https://github.com/ghk/sideka-electron/blob/a025d0f949adbd173905b00164e30676d0689866/src/app/pages/penerimaan.ts) (source: github_api): import * as jetpack from 'fs-jetpack'; import { DiffTracker } from '../helpers/diffs'; var Docxtemplater = require('docxtemplater'); var Handsontable = require('../lib/handsontablep/dist/handsontable
- [readme_excerpt](https://github.com/ghk/sideka-electron/blob/master/README.md) (source: readme): npm run package npm run package:linux npm run package:mac npm run package:windows npm run test npm run watch:test npm run e2e npm run ci This allows you to debug e2e tests and explore your app while i

### 31. keystrokehq/keystroke

**Repository / product**

- Repository: [https://github.com/keystrokehq/keystroke](https://github.com/keystrokehq/keystroke)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code

**Score**

- Score: 34/100 (a score, not a probability)
- Raw weighted score: 1.70 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 1 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 7
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 7
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/keystrokehq/keystroke/blob/785bed9e330db1d6e8c275d74c20807d12942296/packages/integrations/carbone/src/app.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/keystrokehq/keystroke/blob/785bed9e330db1d6e8c275d74c20807d12942296/packages/integrations/carbone/src/index.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/keystrokehq/keystroke/blob/785bed9e330db1d6e8c275d74c20807d12942296/packages/integrations/carbone/src/action.ts)

**Evidence trail**

- [api_response](https://github.com/keystrokehq/keystroke) (source: github_api): stars=64, fork=False, archived=False
- [code_permalink](https://github.com/keystrokehq/keystroke/blob/785bed9e330db1d6e8c275d74c20807d12942296/packages/integrations/carbone/src/app.ts) (source: github_api): generic_api_key: z.string(), }; export const carbone: KeystrokeApp<"carbone", typeof credential> = defineApp({   slug: "carbone",   auth: "keystroke",   credential,
- [code_permalink](https://github.com/keystrokehq/keystroke/blob/785bed9e330db1d6e8c275d74c20807d12942296/packages/integrations/carbone/src/index.ts) (source: github_api): export { carbone } from "./app"; export { carboneCatalog } from "./catalog"; export * from "./actions/index";
- [code_permalink](https://github.com/keystrokehq/keystroke/blob/785bed9e330db1d6e8c275d74c20807d12942296/packages/integrations/carbone/src/action.ts) (source: github_api): import { carbone } from "./app"; import { executeCarboneTool } from "./execute";
- [other](https://github.com/keystrokehq/keystroke/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/keystrokehq/keystroke/blob/main/README.md) (source: readme): </p> <p align="center"> <a href="https://keystroke.ai/signup"><strong>Get started</strong></a> · <a href="https://keystroke.ai/docs">Documentation</a> · <a href="https://keystroke.ai/docs/use-cases">U

### 32. 302ai/302_resume

**Repository / product**

- Repository: [https://github.com/302ai/302_resume](https://github.com/302ai/302_resume)
- Company: Unknown — not stated in the repository
- Product: <p align="center">📝 AI Resume Creation 🚀✨</p>
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://302.ai/tools/resume/

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 34/100 (a score, not a probability)
- Raw weighted score: 1.70 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 4 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `pdf-lib`, run `run_2`, window `size:2001..4000`, rank 29
  - Query: `"pdf-lib" filename:package.json size:2001..4000`
  - Sampled 30 of 7,488 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,488 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `pdf-lib` (pdf, generation) — manifest_declaration — [package.json](https://github.com/302ai/302_resume/blob/main/package.json)
- `pdf-lib` (pdf, generation) — code_import — [code](https://github.com/302ai/302_resume/blob/e4942fa31523752738f537ec7cfc5964d69974f2/src/app/api/pdf-download/route.ts)

**Evidence trail**

- [api_response](https://github.com/302ai/302_resume) (source: github_api): stars=8, fork=False, archived=False
- [manifest_line](https://github.com/302ai/302_resume/blob/main/package.json) (source: github_api): "@pdf-lib/fontkit": "^1.1.1",
- [code_permalink](https://github.com/302ai/302_resume/blob/e4942fa31523752738f537ec7cfc5964d69974f2/src/app/api/pdf-download/route.ts) (source: github_api): import { logger } from "@/utils"; import { NextRequest, NextResponse } from "next/server"; import { PDFDocument } from "pdf-lib"; import fontkit from "@pdf-lib/fontkit"; import { getFontUrls } from "
- [readme_excerpt](https://github.com/302ai/302_resume/blob/main/README.md) (source: readme): && docker run -p 3000:3000 resume` [302.AI](https://302.ai) is an AI application platform for enterprises, with pay-as-you-go pricing, ready to use out of the box, and an open-source ecosystem.

### 33. aws-amplify/docs

**Repository / product**

- Repository: [https://github.com/aws-amplify/docs](https://github.com/aws-amplify/docs)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://docs.amplify.aws

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 33/100 (a score, not a probability)
- Raw weighted score: 1.65 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_2`, window `size:4001..8000`, rank 11
  - Query: `"puppeteer" filename:package.json size:4001..8000`
  - Sampled 30 of 9,184 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 9,184 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/aws-amplify/docs/blob/main/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/aws-amplify/docs/blob/804d139a33f84018136a3603f9ecf555eea9936d/tasks/link-checker.js)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/aws-amplify/docs/blob/804d139a33f84018136a3603f9ecf555eea9936d/e2e/jest.e2e.config.js)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/aws-amplify/docs/blob/804d139a33f84018136a3603f9ecf555eea9936d/tasks/console-errors.js)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/aws-amplify/docs/blob/804d139a33f84018136a3603f9ecf555eea9936d/tasks/get-sitemap-links.js)

**Evidence trail**

- [api_response](https://github.com/aws-amplify/docs) (source: github_api): stars=506, fork=False, archived=False
- [manifest_line](https://github.com/aws-amplify/docs/blob/main/package.json) (source: github_api): "@axe-core/puppeteer": "^4.9.1",
- [code_permalink](https://github.com/aws-amplify/docs/blob/804d139a33f84018136a3603f9ecf555eea9936d/tasks/link-checker.js) (source: github_api): const puppeteer = require('puppeteer'); // eslint-disable-line const axios = require('axios'); // eslint-disable-line const SITEMAP_URL = 'https://docs.amplify.aws/sitemap.xml'; const DOMAIN = 'https
- [code_permalink](https://github.com/aws-amplify/docs/blob/804d139a33f84018136a3603f9ecf555eea9936d/e2e/jest.e2e.config.js) (source: github_api): module.exports = {   rootDir: './',   preset: 'jest-puppeteer',   testMatch: ['<rootDir>/*.test.js'] };
- [code_permalink](https://github.com/aws-amplify/docs/blob/804d139a33f84018136a3603f9ecf555eea9936d/tasks/console-errors.js) (source: github_api): const puppeteer = require('puppeteer'); // eslint-disable-line const { getSitemapUrls } = require('./get-sitemap-links'); // eslint-disable-line // Here we are excluding shortbread errors because the
- [code_permalink](https://github.com/aws-amplify/docs/blob/804d139a33f84018136a3603f9ecf555eea9936d/tasks/get-sitemap-links.js) (source: github_api): const puppeteer = require('puppeteer'); // eslint-disable-line const DOMAIN = 'https://docs.amplify.aws'; const SITEMAP_URL = 'https://docs.amplify.aws/sitemap.xml'; const getSitemapUrls = async (lo
- [readme_excerpt](https://github.com/aws-amplify/docs/blob/main/Readme.md) (source: readme): This helps you keep your pages focused on the need-to-know information upfront, while also providing readers an option to dive deeper when they choose.

### 34. webxos/phalanx

**Repository / product**

- Repository: [https://github.com/webxos/phalanx](https://github.com/webxos/phalanx)
- Company: Unknown — not stated in the repository
- Product: PHALANX v3.6 – Autonomous Pentesting Framework (UNDER DEVELOPMENT)
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 33/100 (a score, not a probability)
- Raw weighted score: 1.65 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_2`, window `size:2001..4000`, rank 25
  - Query: `"weasyprint" filename:requirements.txt size:2001..4000`
  - Sampled 30 of 1,336 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,336 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements.txt](https://github.com/webxos/phalanx/blob/main/requirements.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/webxos/phalanx/blob/9b24f0a54c4b858c9a73e11dd2c2d2dcb0b53ec7/threepointtwo/phalanx_reporting.py)

**Evidence trail**

- [api_response](https://github.com/webxos/phalanx) (source: github_api): stars=127, fork=False, archived=False
- [readme_excerpt](https://github.com/webxos/phalanx/blob/main/README.md) (source: readme): company stated as 'MIT Open Sourced'
- [manifest_line](https://github.com/webxos/phalanx/blob/main/requirements.txt) (source: github_api): # weasyprint>=60.0
- [code_permalink](https://github.com/webxos/phalanx/blob/9b24f0a54c4b858c9a73e11dd2c2d2dcb0b53ec7/threepointtwo/phalanx_reporting.py) (source: github_api): report_path.write_text(html)     # Optionally convert to PDF using weasyprint     if config.get("reporting", {}).get("pdf_enabled", False):
- [readme_excerpt](https://github.com/webxos/phalanx/blob/main/README.md) (source: readme): It is designed for red teams, bug bounty hunters, and security researchers who need scalable, adaptive, and intelligent offensive security tooling.

### 35. activepieces/activepieces

**Repository / product**

- Repository: [https://github.com/activepieces/activepieces](https://github.com/activepieces/activepieces)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.activepieces.com

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 33/100 (a score, not a probability)
- Raw weighted score: 1.65 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 2
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 2
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/activepieces/activepieces/blob/d4cc3eaff77209b773f31e947b3b71306b02059d/packages/pieces/community/carbone/src/index.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/activepieces/activepieces/blob/d4cc3eaff77209b773f31e947b3b71306b02059d/packages/pieces/community/carbone/src/lib/auth.ts)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [packages/pieces/community/carbone/package.json](https://github.com/activepieces/activepieces/blob/d4cc3eaff77209b773f31e947b3b71306b02059d/packages/pieces/community/carbone/package.json)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/activepieces/activepieces/blob/d4cc3eaff77209b773f31e947b3b71306b02059d/packages/pieces/community/carbone/src/lib/common/props.ts)

**Evidence trail**

- [api_response](https://github.com/activepieces/activepieces) (source: github_api): stars=23948, fork=False, archived=False
- [code_permalink](https://github.com/activepieces/activepieces/blob/d4cc3eaff77209b773f31e947b3b71306b02059d/packages/pieces/community/carbone/src/index.ts) (source: github_api): import { carboneAuth } from './lib/auth'; import { CARBONE_API_URL } from './lib/common/constants';
- [code_permalink](https://github.com/activepieces/activepieces/blob/d4cc3eaff77209b773f31e947b3b71306b02059d/packages/pieces/community/carbone/src/lib/auth.ts) (source: github_api): import { PieceAuth } from '@activepieces/pieces-framework'; import { HttpMethod, httpClient } from '@activepieces/pieces-common'; import { CARBONE_API_URL, CARBONE_VERSION } from './common/constants';
- [manifest_line](https://github.com/activepieces/activepieces/blob/d4cc3eaff77209b773f31e947b3b71306b02059d/packages/pieces/community/carbone/package.json) (source: github_api): {   "name": "@activepieces/piece-carbone",   "version": "0.0.5",   "type": "commonjs",   "main": "./dist/src/index.js",   "types": "./dist/src/index.d.ts",   "dependencies": {
- [code_permalink](https://github.com/activepieces/activepieces/blob/d4cc3eaff77209b773f31e947b3b71306b02059d/packages/pieces/community/carbone/src/lib/common/props.ts) (source: github_api): import { Property } from '@activepieces/pieces-framework'; import { HttpMethod, httpClient } from '@activepieces/pieces-common'; import { carboneAuth } from '../auth'; import { CARBONE_API_URL, CARBON
- [readme_excerpt](https://github.com/activepieces/activepieces/blob/main/README.md) (source: readme): **🔒 Secure by Design**: Self-hosted and network-gapped for maximum security and control over your data.

### 36. buzzqw/NotePadPQ

**Repository / product**

- Repository: [https://github.com/buzzqw/notepadpq](https://github.com/buzzqw/notepadpq)
- Company: Unknown — not stated in the repository
- Product: NotePadPQ
- Industry: healthcare_diagnostics (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 33/100 (a score, not a probability)
- Raw weighted score: 1.65 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Pandoc`, run `run_1`, window `unsliced`, rank 6
  - Query: `"subprocess pandoc"`
  - Retrieved 10 of 10 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Pandoc`, run `run_2`, window `unsliced`, rank 6
  - Query: `"subprocess pandoc"`
  - Retrieved 10 of 10 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Pandoc` (conversion, conversion) — manifest_declaration — [pyproject.toml](https://github.com/buzzqw/NotePadPQ/blob/main/pyproject.toml)
- `Pandoc` (conversion, conversion) — code_import — [code](https://github.com/buzzqw/NotePadPQ/blob/3482cfc110cb74de150dfb0251b8d95bc6c364f4/ui/richtext_widget.py)

**Evidence trail**

- [api_response](https://github.com/buzzqw/NotePadPQ) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/buzzqw/NotePadPQ/blob/main/pyproject.toml) (source: github_api): richtext = ["mammoth>=0.11", "htmldocx>=0.0.6", "pypandoc>=1.8"]
- [code_permalink](https://github.com/buzzqw/NotePadPQ/blob/3482cfc110cb74de150dfb0251b8d95bc6c364f4/ui/richtext_widget.py) (source: github_api): Formati supportati:   Lettura : .docx (mammoth), .odt/.rtf (pandoc), .html/.htm (nativo)   Scrittura: .html (nativo), .docx (htmldocx/python-docx), .pdf (Qt print),
- [readme_excerpt](https://github.com/buzzqw/NotePadPQ/blob/main/README.md) (source: readme): [English](#english) \| [Italiano](#italiano) \| [Manuale EN](MANUAL_EN.md) \| [Manuale IT](MANUAL_IT.md) </div> NotePadPQ is designed for people who do not want to switch between a text editor, a LaTeX I

### 37. kartoza/docker-mezzanine

**Repository / product**

- Repository: [https://github.com/kartoza/docker-mezzanine](https://github.com/kartoza/docker-mezzanine)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=3, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=3; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 33/100 (a score, not a probability)
- Raw weighted score: 1.65 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity | 3 |
| Maintenance burden | 3 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 8
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_1`, window `size:501..1000`, rank 7
  - Query: `"python-docx" filename:requirements.txt size:501..1000`
  - Sampled 30 of 11,984 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 11,984 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `WeasyPrint`, run `run_1`, window `size:501..1000`, rank 7
  - Query: `"weasyprint" filename:requirements.txt size:501..1000`
  - Sampled 30 of 3,560 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,560 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 8
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [deployment/docker/REQUIREMENTS.txt](https://github.com/kartoza/docker-mezzanine/blob/f97e8342bd6d2b3cea240f8ce59ba6d0616fb10e/deployment/docker/REQUIREMENTS.txt)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [deployment/docker/REQUIREMENTS-dev.txt](https://github.com/kartoza/docker-mezzanine/blob/f97e8342bd6d2b3cea240f8ce59ba6d0616fb10e/deployment/docker/REQUIREMENTS-dev.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/kartoza/docker-mezzanine/blob/f97e8342bd6d2b3cea240f8ce59ba6d0616fb10e/django_project/kartoza_project/export_utils.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [deployment/docker/REQUIREMENTS.txt](https://github.com/kartoza/docker-mezzanine/blob/f97e8342bd6d2b3cea240f8ce59ba6d0616fb10e/deployment/docker/REQUIREMENTS.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/kartoza/docker-mezzanine/blob/f97e8342bd6d2b3cea240f8ce59ba6d0616fb10e/django_project/kartoza_project/export_utils.py)

**Evidence trail**

- [api_response](https://github.com/kartoza/docker-mezzanine) (source: github_api): stars=9, fork=False, archived=False
- [manifest_line](https://github.com/kartoza/docker-mezzanine/blob/f97e8342bd6d2b3cea240f8ce59ba6d0616fb10e/deployment/docker/REQUIREMENTS.txt) (source: github_api): git+https://github.com/kartoza/plugin-host.git@apps requests==2.1.0 weasyprint==0.42.3 python-docx==0.8.10 docxtpl==0.6.3 pytidylib
- [manifest_line](https://github.com/kartoza/docker-mezzanine/blob/f97e8342bd6d2b3cea240f8ce59ba6d0616fb10e/deployment/docker/REQUIREMENTS-dev.txt) (source: github_api): pypandoc==1.4 weasyprint==0.42.3 django-nose coverage pep8>=1.5.7,<1.6 pylint flake8==2.5.4
- [code_permalink](https://github.com/kartoza/docker-mezzanine/blob/f97e8342bd6d2b3cea240f8ce59ba6d0616fb10e/django_project/kartoza_project/export_utils.py) (source: github_api): from django.conf import settings from django.contrib.staticfiles.finders import find from django.forms.models import model_to_dict from weasyprint import HTML, CSS def add_css(output_text, css_file_
- [manifest_line](https://github.com/kartoza/docker-mezzanine/blob/f97e8342bd6d2b3cea240f8ce59ba6d0616fb10e/deployment/docker/REQUIREMENTS.txt) (source: github_api): git+https://github.com/kartoza/plugin-host.git@apps requests==2.1.0 weasyprint==0.42.3 python-docx==0.8.10 docxtpl==0.6.3 pytidylib
- [code_permalink](https://github.com/kartoza/docker-mezzanine/blob/f97e8342bd6d2b3cea240f8ce59ba6d0616fb10e/django_project/kartoza_project/export_utils.py) (source: github_api): import tempfile import base64 import re from docxtpl import DocxTemplate, RichText from django.conf import settings from django.contrib.staticfiles.finders import find from django.forms.models import
- [other](https://github.com/kartoza/docker-mezzanine/tree/develop/templates) (source: github_api): directory templates/ present

### 38. metorial/metorial

**Repository / product**

- Repository: [https://github.com/metorial/metorial](https://github.com/metorial/metorial)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://metorial.com

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 32/100 (a score, not a probability)
- Raw weighted score: 1.60 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 4 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 4
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 4
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/metorial/metorial/blob/c0d90ad98d7f810d895b6fee9bb29c20dbc07b73/integrations/carbone/src/auth.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/metorial/metorial/blob/c0d90ad98d7f810d895b6fee9bb29c20dbc07b73/integrations/carbone/src/spec.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/metorial/metorial/blob/c0d90ad98d7f810d895b6fee9bb29c20dbc07b73/integrations/carbone/src/config.ts)

**Evidence trail**

- [api_response](https://github.com/metorial/metorial) (source: github_api): stars=3346, fork=False, archived=False
- [code_permalink](https://github.com/metorial/metorial/blob/c0d90ad98d7f810d895b6fee9bb29c20dbc07b73/integrations/carbone/src/auth.ts) (source: github_api): token: z         .string()         .describe(           'Carbone API key. Obtain from https://account.carbone.io/. Can be a Production or Test key.'         )     }),     getOutput: async ctx =>
- [code_permalink](https://github.com/metorial/metorial/blob/c0d90ad98d7f810d895b6fee9bb29c20dbc07b73/integrations/carbone/src/spec.ts) (source: github_api): export let spec = SlateSpecification.create({   key: 'carbone',   name: 'Carbone',   description:     'Document generation engine that merges JSON data into templates (DOCX, XLSX, PPTX, ODT, ODS, HTM
- [code_permalink](https://github.com/metorial/metorial/blob/c0d90ad98d7f810d895b6fee9bb29c20dbc07b73/integrations/carbone/src/config.ts) (source: github_api): .number()       .int()       .default(5)       .describe('Carbone API version to use (e.g. 5). Sent as the carbone-version header.'),     baseUrl: z       .string()       .default('https://api.c
- [readme_excerpt](https://github.com/metorial/metorial/blob/main/README.md) (source: readme): **1200+ integrations** across SaaS tools, enterprise systems, data sources, and custom MCP servers.

### 39. watat83/document-chat-system

**Repository / product**

- Repository: [https://github.com/watat83/document-chat-system](https://github.com/watat83/document-chat-system)
- Company: Unknown — not stated in the repository
- Product: Chat With Your PDFs Using AI - RAG Document Intelligence Platform
- Industry: healthcare_diagnostics (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://document-chat-system.vercel.app

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 32/100 (a score, not a probability)
- Raw weighted score: 1.60 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `Docling`, run `run_1`, window `size:251..500`, rank 4
  - Query: `"docling" filename:requirements.txt size:251..500`
  - Sampled 30 of 1,026 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,026 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:4001..8000`, rank 30
  - Query: `"mammoth" filename:package.json size:4001..8000`
  - Sampled 30 of 2,208 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,208 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `pdf-lib`, run `run_2`, window `size:4001..8000`, rank 26
  - Query: `"pdf-lib" filename:package.json size:4001..8000`
  - Sampled 30 of 2,028 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,028 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Docling` (other_processing, extraction) — manifest_declaration — [package.json](https://github.com/watat83/document-chat-system/blob/main/package.json)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/watat83/document-chat-system/blob/a39060505f9439d31a9062faf2b1bdcaf87da04d/src/lib/file-processing/processors/docling-processor.ts)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/watat83/document-chat-system/blob/a39060505f9439d31a9062faf2b1bdcaf87da04d/services/docling-api/main.py)

**Evidence trail**

- [api_response](https://github.com/watat83/document-chat-system) (source: github_api): stars=147, fork=False, archived=False
- [manifest_line](https://github.com/watat83/document-chat-system/blob/main/package.json) (source: github_api): "dev": "concurrently \"npm run dev:next\" \"npm run dev:inngest\" \"npm run dev:docling\" --names \"NEXT,INNGEST,DOCLING\" --prefix-colors \"cyan,magenta,yellow\"",
- [code_permalink](https://github.com/watat83/document-chat-system/blob/a39060505f9439d31a9062faf2b1bdcaf87da04d/src/lib/file-processing/processors/docling-processor.ts) (source: github_api): } from '../types' /**  * Docling Processor - Advanced document processing using IBM Docling  *  * This processor calls an external Python microservice running Docling for  * superior document underst
- [code_permalink](https://github.com/watat83/document-chat-system/blob/a39060505f9439d31a9062faf2b1bdcaf87da04d/services/docling-api/main.py) (source: github_api): from docling.document_converter import DocumentConverter, PdfFormatOption from docling.datamodel.base_models import InputFormat
- [readme_excerpt](https://github.com/watat83/document-chat-system/blob/main/README.md) (source: readme): Deploy your own instance, modify as needed, or monetize as a SaaS.

### 40. kamkahou/ragflow-0.17.2

**Repository / product**

- Repository: [https://github.com/kamkahou/ragflow-0.17.2](https://github.com/kamkahou/ragflow-0.17.2)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 32/100 (a score, not a probability)
- Raw weighted score: 1.60 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `Apache Tika`, run `run_2`, window `size:4001..8000`, rank 30
  - Query: `"tika" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 111 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache Tika` (other_processing, extraction) — manifest_declaration — [pyproject.toml](https://github.com/kamkahou/ragflow-0.17.2/blob/main/pyproject.toml)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/kamkahou/ragflow-0.17.2/blob/44de58fe2d2b0b634ea4c94bed2c69abb5a96931/download_deps.py)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/kamkahou/ragflow-0.17.2/blob/44de58fe2d2b0b634ea4c94bed2c69abb5a96931/rag/app/naive.py)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/kamkahou/ragflow-0.17.2/blob/44de58fe2d2b0b634ea4c94bed2c69abb5a96931/rag/app/one.py)

**Evidence trail**

- [api_response](https://github.com/kamkahou/ragflow-0.17.2) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/kamkahou/ragflow-0.17.2/blob/main/pyproject.toml) (source: github_api): "tika==2.6.0",
- [code_permalink](https://github.com/kamkahou/ragflow-0.17.2/blob/44de58fe2d2b0b634ea4c94bed2c69abb5a96931/download_deps.py) (source: github_api): urls = [     "http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb",     "http://ports.ubuntu.com/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_arm64.deb",     "htt
- [code_permalink](https://github.com/kamkahou/ragflow-0.17.2/blob/44de58fe2d2b0b634ea4c94bed2c69abb5a96931/rag/app/naive.py) (source: github_api): import logging from tika import parser from io import BytesIO
- [code_permalink](https://github.com/kamkahou/ragflow-0.17.2/blob/44de58fe2d2b0b634ea4c94bed2c69abb5a96931/rag/app/one.py) (source: github_api): # import logging from tika import parser from io import BytesIO import re
- [readme_excerpt](https://github.com/kamkahou/ragflow-0.17.2/blob/main/README.md) (source: readme): It offers a streamlined RAG workflow for businesses of any scale, combining LLM (Large Language Models) to provide truthful question-answering capabilities, backed by well-founded citations from vario

### 41. shivama205/DocBrain

**Repository / product**

- Repository: [https://github.com/shivama205/docbrain](https://github.com/shivama205/docbrain)
- Company: Unknown — not stated in the repository
- Product: DocBrain
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 32/100 (a score, not a probability)
- Raw weighted score: 1.60 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `Docling`, run `run_2`, window `size:2001..4000`, rank 29
  - Query: `"docling" filename:requirements.txt size:2001..4000`
  - Retrieved 30 of 494 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Docling` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/shivama205/DocBrain/blob/main/requirements.txt)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/shivama205/DocBrain/blob/00f02786497c2dc99172d833162361c68444514f/app/services/rag/ingestor/ingestor.py)

**Evidence trail**

- [api_response](https://github.com/shivama205/DocBrain) (source: github_api): stars=13, fork=False, archived=False
- [manifest_line](https://github.com/shivama205/DocBrain/blob/main/requirements.txt) (source: github_api): docling>=2.0.0,<3.0.0
- [code_permalink](https://github.com/shivama205/DocBrain/blob/00f02786497c2dc99172d833162361c68444514f/app/services/rag/ingestor/ingestor.py) (source: github_api): from docling.datamodel.pipeline_options import PdfPipelineOptions from docling.document_converter import (     DocumentConverter,
- [readme_excerpt](https://github.com/shivama205/DocBrain/blob/main/README.md) (source: readme): ![DocBrain-Banner-3](https://github.com/user-attachments/assets/6c882743-a60e-4efd-b1b7-13f83167e38e) Self-hosted RAG for teams that can't send data to third-party APIs.

### 42. stella/stella

**Repository / product**

- Repository: [https://github.com/stella/stella](https://github.com/stella/stella)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://stll.app

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: infrastructure_service_present=true; confirmed generation/conversion code

**Score**

- Score: 30/100 (a score, not a probability)
- Raw weighted score: 1.50 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 13
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 13
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/stella/stella/blob/main/docker-compose.yml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/stella/stella/blob/e0451ee6086649fb0776e4c0e41b21202dba1395/apps/api/src/lib/files/gotenberg.ts)

**Evidence trail**

- [api_response](https://github.com/stella/stella) (source: github_api): stars=180, fork=False, archived=False
- [code_permalink](https://github.com/stella/stella/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/stella/stella/blob/e0451ee6086649fb0776e4c0e41b21202dba1395/apps/api/src/lib/files/gotenberg.ts) (source: github_api): const gotenbergAuth = (): string =>   basicAuthorizationHeader(env.GOTENBERG_USERNAME, env.GOTENBERG_PASSWORD);
- [readme_excerpt](https://github.com/stella/stella/blob/main/README.md) (source: readme): **Business registries.** [Business Registries](packages/business-registries) provides typed clients for national company and commercial registries, including ARES, Companies House, SEC EDGAR, KRS, PRH
- [api_response](https://github.com/stella/stella) (source: github_api): stars=180, fork=False, archived=False
- [code_permalink](https://github.com/stella/stella/blob/main/docker-compose.yml) (source: github_api): services:   postgres:     profiles: [dev]     # Keep dev aligned with infra. Postgres 18 expects the volume     # mounted at /var/lib/postgresql, not /var/lib/postgresql/data.     # After switching fr
- [code_permalink](https://github.com/stella/stella/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/stella/stella/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/stella/stella/blob/e0451ee6086649fb0776e4c0e41b21202dba1395/apps/api/src/lib/files/gotenberg.ts) (source: github_api): const gotenbergAuth = (): string =>   basicAuthorizationHeader(env.GOTENBERG_USERNAME, env.GOTENBERG_PASSWORD);
- [readme_excerpt](https://github.com/stella/stella/blob/main/README.md) (source: readme): **Business registries.** [Business Registries](packages/business-registries) provides typed clients for national company and commercial registries, including ARES, Companies House, SEC EDGAR, KRS, PRH

### 43. ceskaexpedice/kramerius

**Repository / product**

- Repository: [https://github.com/ceskaexpedice/kramerius](https://github.com/ceskaexpedice/kramerius)
- Company: Unknown — not stated in the repository
- Product: Kramerius system
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 30/100 (a score, not a probability)
- Raw weighted score: 1.50 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Apache PDFBox`, run `run_1`, window `size:501..1000`, rank 10
  - Query: `"pdfbox" filename:build.gradle size:501..1000`
  - Retrieved 30 of 412 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Apache PDFBox`, run `run_1`, window `size:1001..2000`, rank 21
  - Query: `"pdfbox" filename:build.gradle size:1001..2000`
  - Sampled 30 of 1,100 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,100 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Apache Tika`, run `run_1`, window `size:251..500`, rank 24
  - Query: `"tika" filename:build.gradle size:251..500`
  - Retrieved 30 of 100 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Apache PDFBox`, run `run_2`, window `size:4001..8000`, rank 18
  - Query: `"pdfbox" filename:build.gradle size:4001..8000`
  - Retrieved 30 of 764 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `iText`, run `run_2`, window `size:4001..8000`, rank 9
  - Query: `"itext" filename:build.gradle size:4001..8000`
  - Sampled 30 of 1,060 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,060 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Apache Tika`, run `run_2`, window `size:2001..4000`, rank 13
  - Query: `"tika" filename:build.gradle size:2001..4000`
  - Sampled 30 of 1,076 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,076 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Apache PDFBox` (pdf, generation) — manifest_declaration — [shared/common/build.gradle](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/shared/common/build.gradle)
- `Apache PDFBox` (pdf, generation) — manifest_declaration — [processes/cdk/cdkreharvest/build.gradle](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/cdk/cdkreharvest/build.gradle)
- `Apache PDFBox` (pdf, generation) — manifest_declaration — [processes/cdk/cdkprocesses/build.gradle](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/cdk/cdkprocesses/build.gradle)
- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/search-index/src/main/java/cz/kramerius/searchIndex/indexer/execution/PdfExtractor.java)
- `Apache PDFBox` (pdf, generation) — manifest_declaration — [processes/platform/cdk/cdk-delete-library/build.gradle](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/platform/cdk/cdk-delete-library/build.gradle)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/search-index/src/main/java/cz/kramerius/utils/EncodingAwareReader.java)
- `Apache Tika` (other_processing, extraction) — manifest_declaration — [processes/search-index/build.gradle](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/search-index/build.gradle)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/shared/common/src/main/java/cz/inovatika/dochub/DocumentType.java)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/shared/common/src/main/java/cz/inovatika/dochub/UsageCounter.java)

**Evidence trail**

- [api_response](https://github.com/ceskaexpedice/kramerius) (source: github_api): stars=53, fork=False, archived=False
- [manifest_line](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/shared/common/build.gradle) (source: github_api): api 'javax.servlet:servlet-api:2.5'     api 'org.json:json:20140107'     api 'commons-codec:commons-codec:1.5'     //api 'org.apache.pdfbox:pdfbox:2.0.26'     api 'org.apache.pdfbox:pdfbox:2.0.32'
- [manifest_line](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/cdk/cdkreharvest/build.gradle) (source: github_api): configurations.api {     exclude group: 'org.bouncycastle'     exclude group: 'com.lowagie'     exclude group: 'org.apache.pdfbox'     exclude group: 'com.levigo.jbig2'     exclude group: 'org.apache.
- [manifest_line](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/cdk/cdkprocesses/build.gradle) (source: github_api): configurations.api {     exclude group: 'org.bouncycastle'     exclude group: 'com.lowagie'     exclude group: 'org.apache.pdfbox'     exclude group: 'com.levigo.jbig2'     exclude group: 'org.apache.
- [code_permalink](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/search-index/src/main/java/cz/kramerius/searchIndex/indexer/execution/PdfExtractor.java) (source: github_api): import org.apache.commons.io.IOUtils; import org.apache.commons.lang3.StringEscapeUtils; import org.apache.pdfbox.pdmodel.PDDocument; import org.apache.pdfbox.text.PDFTextStripper; import java.io.Fil
- [manifest_line](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/platform/cdk/cdk-delete-library/build.gradle) (source: github_api): configurations.api {     exclude group: 'org.bouncycastle'     exclude group: 'com.lowagie'     exclude group: 'org.apache.pdfbox'     exclude group: 'com.levigo.jbig2'     exclude group: 'org.apache.
- [code_permalink](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/search-index/src/main/java/cz/kramerius/utils/EncodingAwareReader.java) (source: github_api): package cz.kramerius.utils; import org.apache.commons.io.IOUtils; import org.apache.tika.detect.EncodingDetector; import org.apache.tika.parser.txt.UniversalEncodingDetector; import org.apache.tika.m
- [manifest_line](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/processes/search-index/build.gradle) (source: github_api): //api project(':security:security-core')     api project(':shared:common')     // tika     implementation'org.apache.tika:tika-parser-text-module:3.1.0'     implementation ('org.apache.tika:tika-
- [code_permalink](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/shared/common/src/main/java/cz/inovatika/dochub/DocumentType.java) (source: github_api): package cz.inovatika.dochub; public enum DocumentType {     PDF,     EPUB,     TEXT
- [code_permalink](https://github.com/ceskaexpedice/kramerius/blob/a51ae6e9cf3c1544e23222ae6ffbb1da78b0adda/shared/common/src/main/java/cz/inovatika/dochub/UsageCounter.java) (source: github_api): package cz.inovatika.dochub; import cz.incad.kramerius.security.licenses.limits.LimitInterval; public interface UsageCounter {     void logUsage(String pid, String user);

### 44. CyberCX-STA/PurpleOps

**Repository / product**

- Repository: [https://github.com/cybercx-sta/purpleops](https://github.com/cybercx-sta/purpleops)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://purpleops.app

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2; pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 30/100 (a score, not a probability)
- Raw weighted score: 1.50 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 2 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 5
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_1`, window `size:1001..2000`, rank 5
  - Query: `"python-docx" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 8,336 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 8,336 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 5
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [requirements.txt](https://github.com/CyberCX-STA/PurpleOps/blob/main/requirements.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/CyberCX-STA/PurpleOps/blob/0072abf6428d15aee4ff76f54fc82b211a47fcd6/blueprints/assessment_export.py)
- `python-docx` (docx, generation) — manifest_declaration — [requirements.txt](https://github.com/CyberCX-STA/PurpleOps/blob/main/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/CyberCX-STA/PurpleOps) (source: github_api): stars=313, fork=False, archived=False
- [manifest_line](https://github.com/CyberCX-STA/PurpleOps/blob/main/requirements.txt) (source: github_api): docxtpl==0.16.7
- [code_permalink](https://github.com/CyberCX-STA/PurpleOps/blob/0072abf6428d15aee4ff76f54fc82b211a47fcd6/blueprints/assessment_export.py) (source: github_api): import json import shutil from model import * from docxtpl import DocxTemplate from utils import user_assigned_assessment from werkzeug.utils import secure_filename from flask_security import auth_req
- [manifest_line](https://github.com/CyberCX-STA/PurpleOps/blob/main/requirements.txt) (source: github_api): python-docx==0.8.11
- [other](https://github.com/CyberCX-STA/PurpleOps/tree/main/templates) (source: github_api): directory templates/ present

### 45. Aleks-Ya/yaal_examples

**Repository / product**

- Repository: [https://github.com/aleks-ya/yaal_examples](https://github.com/aleks-ya/yaal_examples)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 30/100 (a score, not a probability)
- Raw weighted score: 1.50 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 27
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Apache POI (XWPF/HWPF)`, run `run_1`, window `size:0..250`, rank 30
  - Query: `"poi" filename:build.gradle size:0..250`
  - Retrieved 30 of 395 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Apache PDFBox`, run `run_1`, window `size:0..250`, rank 7
  - Query: `"pdfbox" filename:build.gradle size:0..250`
  - Retrieved 30 of 44 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `iText`, run `run_1`, window `size:0..250`, rank 4
  - Query: `"itext" filename:build.gradle size:0..250`
  - Retrieved 30 of 40 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `iText`, run `run_1`, window `size:251..500`, rank 26
  - Query: `"itext" filename:build.gradle size:251..500`
  - Retrieved 30 of 103 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 27
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache PDFBox` (pdf, generation) — manifest_declaration — [Java+/UnitTest+/PdfBox/build.gradle](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/UnitTest+/PdfBox/build.gradle)
- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/UnitTest+/PdfBox/test/pdf/Helper.java)
- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/UnitTest+/PdfBox/test/pdf/ReadPdfFileTest.java)
- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/UnitTest+/PdfBox/test/pdf/ExtractTextTest.java)
- `Apache POI (XWPF/HWPF)` (docx, generation) — manifest_declaration — [Java+/Libs+/Apache+/ApachePOI/build.gradle](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/Libs+/Apache+/ApachePOI/build.gradle)
- `Apache POI (XWPF/HWPF)` (docx, generation) — code_import — [code](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/Spring+/Spring5+/AOP+/AspectJ/src/pointcut/execution/Converter.java)

**Evidence trail**

- [api_response](https://github.com/Aleks-Ya/yaal_examples) (source: github_api): stars=3, fork=False, archived=False
- [manifest_line](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/UnitTest+/PdfBox/build.gradle) (source: github_api): dependencies {     implementation 'org.apache.pdfbox:pdfbox:2.0.29', 'org.apache.pdfbox:pdfbox-lucene:1.8.17' }
- [code_permalink](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/UnitTest+/PdfBox/test/pdf/Helper.java) (source: github_api): package pdf; import org.apache.pdfbox.pdmodel.PDDocument; import org.apache.pdfbox.pdmodel.PDPage; import org.apache.pdfbox.pdmodel.PDPageContentStream; import org.apache.pdfbox.pdmodel.font.PDType1F
- [code_permalink](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/UnitTest+/PdfBox/test/pdf/ReadPdfFileTest.java) (source: github_api): package pdf; import org.apache.pdfbox.io.RandomAccessFile; import org.apache.pdfbox.pdfparser.PDFParser; import org.junit.jupiter.api.Test; import java.io.IOException;
- [code_permalink](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/UnitTest+/PdfBox/test/pdf/ExtractTextTest.java) (source: github_api): import org.apache.pdfbox.lucene.LucenePDFDocument; import org.junit.jupiter.api.Disabled;
- [manifest_line](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/Libs+/Apache+/ApachePOI/build.gradle) (source: github_api): dependencies {     implementation 'org.apache.poi:poi-ooxml:5.4.0' }
- [code_permalink](https://github.com/Aleks-Ya/yaal_examples/blob/3926d71af9ec20c5434f357fdcbca6de6eb67ed7/Java+/Spring+/Spring5+/AOP+/AspectJ/src/pointcut/execution/Converter.java) (source: github_api): package pointcut.execution; public class Converter {     public String toUpperCase(String s) {         return s.toUpperCase();     } }

### 46. FikrahFathoniSiregar/Auto-Report

**Repository / product**

- Repository: [https://github.com/fikrahfathonisiregar/auto-report](https://github.com/fikrahfathonisiregar/auto-report)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 30/100 (a score, not a probability)
- Raw weighted score: 1.50 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtemplater`, run `run_1`, window `unsliced`, rank 30
  - Query: `"docxtemplater" filename:package.json`
  - Sampled 30 of 3,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,256 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtemplater`, run `run_2`, window `unsliced`, rank 30
  - Query: `"docxtemplater" filename:package.json`
  - Sampled 30 of 3,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,256 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtemplater` (docx, generation) — manifest_declaration — [package-lock.json](https://github.com/FikrahFathoniSiregar/Auto-Report/blob/main/package-lock.json)
- `docxtemplater` (docx, generation) — manifest_declaration — [package.json](https://github.com/FikrahFathoniSiregar/Auto-Report/blob/main/package.json)
- `docxtemplater` (docx, generation) — code_import — [code](https://github.com/FikrahFathoniSiregar/Auto-Report/blob/93f60e25a731c3f6ff261cd31eecb260c4a5dce8/api/server.js)

**Evidence trail**

- [api_response](https://github.com/FikrahFathoniSiregar/Auto-Report) (source: github_api): stars=8, fork=False, archived=False
- [manifest_line](https://github.com/FikrahFathoniSiregar/Auto-Report/blob/main/package-lock.json) (source: github_api): "docxtemplater": "^3.65.2",
- [manifest_line](https://github.com/FikrahFathoniSiregar/Auto-Report/blob/main/package.json) (source: github_api): "docxtemplater": "^3.65.2",
- [code_permalink](https://github.com/FikrahFathoniSiregar/Auto-Report/blob/93f60e25a731c3f6ff261cd31eecb260c4a5dce8/api/server.js) (source: github_api): const cors = require("cors"); const fs = require("fs"); const path = require("path"); const Docxtemplater = require("docxtemplater"); const PizZip = require("pizzip"); const ImageModule = require("doc
- [other](https://github.com/FikrahFathoniSiregar/Auto-Report/tree/main/reports) (source: github_api): directory reports/ present

### 47. ngs-doo/TemplaterExamples

**Repository / product**

- Repository: [https://github.com/ngs-doo/templaterexamples](https://github.com/ngs-doo/templaterexamples)
- Company: Unknown — not stated in the repository
- Product: Document generation from templates
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://templater.info

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 29/100 (a score, not a probability)
- Raw weighted score: 1.45 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 1 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `docx4j`, run `run_1`, window `size:1001..2000`, rank 17
  - Query: `"docx4j" filename:pom.xml size:1001..2000`
  - Retrieved 30 of 76 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Open XML SDK`, run `run_1`, window `size:251..500`, rank 8
  - Query: `"DocumentFormat.OpenXml" filename:packages.config size:251..500`
  - Retrieved 30 of 508 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Aspose.Words`, run `run_1`, window `size:1001..2000`, rank 9
  - Query: `"Aspose.Words" extension:csproj size:1001..2000`
  - Retrieved 30 of 187 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Open XML SDK`, run `run_2`, window `size:2001..4000`, rank 16
  - Query: `"DocumentFormat.OpenXml" extension:csproj size:2001..4000`
  - Sampled 30 of 1,580 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,580 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Open XML SDK`, run `run_2`, window `size:4001..8000`, rank 14
  - Query: `"DocumentFormat.OpenXml" extension:csproj size:4001..8000`
  - Sampled 30 of 1,092 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,092 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Aspose.Words` (docx, generation) — code_import — [code](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Advanced/TemplaterServer/src/Aspose.cs)
- `Aspose.Words` (docx, generation) — code_import — [code](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Advanced/TemplaterServer/src/main/java/hr/ngs/templater/server/Aspose.java)
- `Aspose.Words` (docx, generation) — manifest_declaration — [Advanced/TemplaterServer/TemplaterServer.csproj](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Advanced/TemplaterServer/TemplaterServer.csproj)
- `Open XML SDK` (docx, generation) — code_import — [code](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Intermediate/HtmlToExcel/src/Program.cs)
- `Open XML SDK` (docx, generation) — code_import — [code](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Intermediate/HtmlToWord/src/Program.cs)
- `Open XML SDK` (docx, generation) — manifest_declaration — [Intermediate/HtmlToWord/packages.config](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Intermediate/HtmlToWord/packages.config)
- `Open XML SDK` (docx, generation) — manifest_declaration — [Intermediate/HtmlToExcel/packages.config](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Intermediate/HtmlToExcel/packages.config)
- `Open XML SDK` (docx, generation) — manifest_declaration — [Intermediate/HtmlToWord/HtmlToWord.csproj](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Intermediate/HtmlToWord/HtmlToWord.csproj)

**Evidence trail**

- [api_response](https://github.com/ngs-doo/TemplaterExamples) (source: github_api): stars=48, fork=False, archived=False
- [code_permalink](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Advanced/TemplaterServer/src/Aspose.cs) (source: github_api): ﻿using Aspose.Words; using System.IO; namespace TemplaterServer.src { public class Aspose : PdfConverter {
- [code_permalink](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Advanced/TemplaterServer/src/main/java/hr/ngs/templater/server/Aspose.java) (source: github_api): package hr.ngs.templater.server; import com.aspose.words.Document; import com.aspose.words.SaveFormat; import java.io.ByteArrayInputStream; import java.io.ByteArrayOutputStream;
- [manifest_line](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Advanced/TemplaterServer/TemplaterServer.csproj) (source: github_api): </ItemGroup>   <ItemGroup>     <PackageReference Include="Aspose.Words" Version="19.12.0" />     <PackageReference Include="FreeSpire.Doc" Version="7.11.0" />     <PackageReference Include="Ne
- [code_permalink](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Intermediate/HtmlToExcel/src/Program.cs) (source: github_api): using System.Linq; using System.Xml.Linq; using DocumentFormat.OpenXml; using DocumentFormat.OpenXml.Packaging; using HtmlToOpenXml; using NGS.Templater;
- [code_permalink](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Intermediate/HtmlToWord/src/Program.cs) (source: github_api): using System.Linq; using System.Xml.Linq; using DocumentFormat.OpenXml; using DocumentFormat.OpenXml.Packaging; using HtmlToOpenXml; using NGS.Templater;
- [manifest_line](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Intermediate/HtmlToWord/packages.config) (source: github_api): ﻿<?xml version="1.0" encoding="utf-8"?> <packages>   <package id="DocumentFormat.OpenXml" version="2.7.2" targetFramework="net40-Client" />   <package id="HtmlToOpenXml.dll" version="2.0.1" targetF
- [manifest_line](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Intermediate/HtmlToExcel/packages.config) (source: github_api): ﻿<?xml version="1.0" encoding="utf-8"?> <packages>   <package id="DocumentFormat.OpenXml" version="2.7.2" targetFramework="net40-Client" />   <package id="HtmlToOpenXml.dll" version="2.0.1" targetF
- [manifest_line](https://github.com/ngs-doo/TemplaterExamples/blob/d1fa6cf6284dc94b33a370f628f3783468cc858d/Intermediate/HtmlToWord/HtmlToWord.csproj) (source: github_api): <WarningLevel>4</WarningLevel>   </PropertyGroup>   <ItemGroup>     <Reference Include="DocumentFormat.OpenXml">       <HintPath>..\..\packages\DocumentFormat.OpenXml.2.7.2\lib\net40\DocumentF
- [readme_excerpt](https://github.com/ngs-doo/TemplaterExamples/blob/master/README.md) (source: readme): Main goal is to provide customization options outside of development, so that reports/invoices/quotes and various other type of documents can be made to look as customers needs them.

### 48. PipedreamHQ/pipedream

**Repository / product**

- Repository: [https://github.com/pipedreamhq/pipedream](https://github.com/pipedreamhq/pipedream)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://pipedream.com

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 28/100 (a score, not a probability)
- Raw weighted score: 1.40 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 3
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 3
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/PipedreamHQ/pipedream/blob/b441a8cb86e2195900aca15ce9b47d7ef7a7752f/components/carbone/carbone.app.mjs)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [components/carbone/package.json](https://github.com/PipedreamHQ/pipedream/blob/b441a8cb86e2195900aca15ce9b47d7ef7a7752f/components/carbone/package.json)

**Evidence trail**

- [api_response](https://github.com/PipedreamHQ/pipedream) (source: github_api): stars=11636, fork=False, archived=False
- [code_permalink](https://github.com/PipedreamHQ/pipedream/blob/b441a8cb86e2195900aca15ce9b47d7ef7a7752f/components/carbone/carbone.app.mjs) (source: github_api): export default {   type: "app",   app: "carbone",   propDefinitions: {},   methods: {     // this.$auth contains connected account data     authKeys() {
- [manifest_line](https://github.com/PipedreamHQ/pipedream/blob/b441a8cb86e2195900aca15ce9b47d7ef7a7752f/components/carbone/package.json) (source: github_api): {   "name": "@pipedream/carbone",   "version": "0.0.1",   "description": "Pipedream Carbone Components",   "main": "carbone.app.mjs",   "keywords": [     "pipedream",
- [readme_excerpt](https://github.com/PipedreamHQ/pipedream/blob/master/README.md) (source: readme): Pipedream provides a free, hosted platform for connecting apps and developing event-driven automations.

### 49. simpledms/simpledms

**Repository / product**

- Repository: [https://github.com/simpledms/simpledms](https://github.com/simpledms/simpledms)
- Company: Unknown — not stated in the repository
- Product: SimpleDMS – Document Management for Small Businesses
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://simpledms.eu

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: infrastructure_service_present=true; confirmed generation/conversion code

**Score**

- Score: 27/100 (a score, not a probability)
- Raw weighted score: 1.35 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 17
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 17
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/simpledms/simpledms/blob/main/docker-compose.yml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/simpledms/simpledms/blob/a3cfb0331869af24ab611fb7bf84f50a80b6cd8b/internal/gotenberg/gotenberg_client.go)

**Evidence trail**

- [api_response](https://github.com/simpledms/simpledms) (source: github_api): stars=162, fork=False, archived=False
- [code_permalink](https://github.com/simpledms/simpledms/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/simpledms/simpledms/blob/a3cfb0331869af24ab611fb7bf84f50a80b6cd8b/internal/gotenberg/gotenberg_client.go) (source: github_api): package gotenberg import (
- [readme_excerpt](https://github.com/simpledms/simpledms/blob/main/README.md) (source: readme): The app is also available as a SaaS offering at [simpledms.eu](https://simpledms.eu) and [simpledms.ch](https://simpledms.ch).
- [api_response](https://github.com/simpledms/simpledms) (source: github_api): stars=162, fork=False, archived=False
- [code_permalink](https://github.com/simpledms/simpledms/blob/main/docker-compose.yml) (source: github_api): volumes:     mailpit_data:     versitygw_data:     #garage_meta:     #garage_data: name: simpledms-dev services:     #docling:         #image: ghcr.io/docling-project/docling-serve-cpu         #cont
- [code_permalink](https://github.com/simpledms/simpledms/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/simpledms/simpledms/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/simpledms/simpledms/blob/a3cfb0331869af24ab611fb7bf84f50a80b6cd8b/internal/gotenberg/gotenberg_client.go) (source: github_api): package gotenberg import (
- [readme_excerpt](https://github.com/simpledms/simpledms/blob/main/README.md) (source: readme): The app is also available as a SaaS offering at [simpledms.eu](https://simpledms.eu) and [simpledms.ch](https://simpledms.ch).

### 50. iondv/registry

**Repository / product**

- Repository: [https://github.com/iondv/registry](https://github.com/iondv/registry)
- Company: Unknown — not stated in the repository
- Product: IONDV. Registry
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 27/100 (a score, not a probability)
- Raw weighted score: 1.35 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtemplater`, run `run_1`, window `unsliced`, rank 25
  - Query: `"docxtemplater" filename:package.json`
  - Sampled 30 of 3,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,256 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtemplater`, run `run_2`, window `unsliced`, rank 25
  - Query: `"docxtemplater" filename:package.json`
  - Sampled 30 of 3,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,256 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtemplater` (docx, generation) — manifest_declaration — [package.json](https://github.com/iondv/registry/blob/main/package.json)
- `docxtemplater` (docx, generation) — code_import — [code](https://github.com/iondv/registry/blob/d1b431ea992d1d4ae10a0435f183b7d343c603f4/export/listToDocx.js)
- `docxtemplater` (docx, generation) — code_import — [code](https://github.com/iondv/registry/blob/d1b431ea992d1d4ae10a0435f183b7d343c603f4/export/itemToDocx.js)

**Evidence trail**

- [api_response](https://github.com/iondv/registry) (source: github_api): stars=4, fork=False, archived=False
- [manifest_line](https://github.com/iondv/registry/blob/main/package.json) (source: github_api): "docxtemplater": "^3.8.3",
- [code_permalink](https://github.com/iondv/registry/blob/d1b431ea992d1d4ae10a0435f183b7d343c603f4/export/listToDocx.js) (source: github_api): const resolvePath = require('core/resolvePath'); const normalize = require('core/util/normalize'); const prepareDate = require('../backend/items').prepareDate; const Docxtemplater = require('docxtempl
- [code_permalink](https://github.com/iondv/registry/blob/d1b431ea992d1d4ae10a0435f183b7d343c603f4/export/itemToDocx.js) (source: github_api): const resolvePath = require('core/resolvePath'); const normalize = require('core/util/normalize'); const prepareDate = require('../backend/items').prepareDate; const Docxtemplater = require('docxtempl
- [readme_excerpt](https://github.com/iondv/registry/blob/main/README.md) (source: readme): **[pm-gov-ru.iondv.com](https://pm-gov-ru.iondv.com/geomap) project** - is a registry type software solution for organizing public sector project activities.

### 51. bashly-framework/bashly

**Repository / product**

- Repository: [https://github.com/bashly-framework/bashly](https://github.com/bashly-framework/bashly)
- Company: Unknown — not stated in the repository
- Product: Bashly - Bash CLI Framework and Generator
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://bashly.dev

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: infrastructure_service_present=true; confirmed generation/conversion code

**Score**

- Score: 26/100 (a score, not a probability)
- Raw weighted score: 1.30 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 1, `Pandoc`, run `run_1`, window `unsliced`, rank 4
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `Pandoc`, run `run_2`, window `unsliced`, rank 4
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Pandoc` (conversion, conversion) — infrastructure_reference — [code](https://github.com/bashly-framework/bashly/blob/master/Dockerfile)
- `Pandoc` (conversion, conversion) — infrastructure_reference — [code](https://github.com/bashly-framework/bashly/blob/master/docker-compose.yml)
- `Pandoc` (conversion, conversion) — code_import — [code](https://github.com/bashly-framework/bashly/blob/2817b75f786ffca4a083872c8ccb8fc2198b25b4/lib/bashly/libraries/render/mandoc/render.rb)

**Evidence trail**

- [api_response](https://github.com/bashly-framework/bashly) (source: github_api): stars=2435, fork=False, archived=False
- [code_permalink](https://github.com/bashly-framework/bashly/blob/master/Dockerfile) (source: github_api): # Install pandoc to support manpage generation (`bashly render :mandoc docs`)
- [code_permalink](https://github.com/bashly-framework/bashly/blob/master/docker-compose.yml) (source: github_api): pandoc-test:
- [code_permalink](https://github.com/bashly-framework/bashly/blob/2817b75f786ffca4a083872c8ccb8fc2198b25b4/lib/bashly/libraries/render/mandoc/render.rb) (source: github_api): manfile = "#{target}/#{command.full_name.tr(' ', '-')}.1"   save mdfile, gtx.parse(command)   # The pandoc command that creates a manpage from markdown   cmd = %[pandoc -f markdown-smart -s --to ma
- [readme_excerpt](https://github.com/bashly-framework/bashly/blob/master/README.md) (source: readme): <div align='center'> <img src='support/img/bashly-logo.svg' width=280> Create feature-rich bash scripts using simple YAML configuration ![demo](support/demo/cast.gif) </div> ![repocard](https://repoca
- [api_response](https://github.com/bashly-framework/bashly) (source: github_api): stars=2435, fork=False, archived=False
- [code_permalink](https://github.com/bashly-framework/bashly/blob/master/Dockerfile) (source: github_api): FROM dannyben/alpine-ruby:4.0 LABEL io.whalebrew.name=bashly ENV PS1="\n\n>> bashly \W \$ " ENV BASHLY_VERSION=1.4.0 WORKDIR /app # Install pandoc to support manpage generation (`bashly render :ma
- [code_permalink](https://github.com/bashly-framework/bashly/blob/master/Dockerfile) (source: github_api): # Install pandoc to support manpage generation (`bashly render :mandoc docs`)
- [code_permalink](https://github.com/bashly-framework/bashly/blob/master/docker-compose.yml) (source: github_api): pandoc-test:
- [code_permalink](https://github.com/bashly-framework/bashly/blob/master/Dockerfile) (source: github_api): # Install pandoc to support manpage generation (`bashly render :mandoc docs`)
- [code_permalink](https://github.com/bashly-framework/bashly/blob/2817b75f786ffca4a083872c8ccb8fc2198b25b4/lib/bashly/libraries/render/mandoc/render.rb) (source: github_api): manfile = "#{target}/#{command.full_name.tr(' ', '-')}.1"   save mdfile, gtx.parse(command)   # The pandoc command that creates a manpage from markdown   cmd = %[pandoc -f markdown-smart -s --to ma
- [readme_excerpt](https://github.com/bashly-framework/bashly/blob/master/README.md) (source: readme): <div align='center'> <img src='support/img/bashly-logo.svg' width=280> Create feature-rich bash scripts using simple YAML configuration ![demo](support/demo/cast.gif) </div> ![repocard](https://repoca

### 52. ShirleyBailey/ragflow

**Repository / product**

- Repository: [https://github.com/shirleybailey/ragflow](https://github.com/shirleybailey/ragflow)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 26/100 (a score, not a probability)
- Raw weighted score: 1.30 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `Apache Tika`, run `run_2`, window `size:4001..8000`, rank 29
  - Query: `"tika" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 111 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache Tika` (other_processing, extraction) — manifest_declaration — [pyproject.toml](https://github.com/ShirleyBailey/ragflow/blob/master/pyproject.toml)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/ShirleyBailey/ragflow/blob/3ea340de7601778c8d05665a8bbc6b9364251cc7/download_deps.py)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/ShirleyBailey/ragflow/blob/3ea340de7601778c8d05665a8bbc6b9364251cc7/rag/app/naive.py)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/ShirleyBailey/ragflow/blob/3ea340de7601778c8d05665a8bbc6b9364251cc7/rag/app/one.py)

**Evidence trail**

- [api_response](https://github.com/ShirleyBailey/ragflow) (source: github_api): stars=1, fork=False, archived=False
- [manifest_line](https://github.com/ShirleyBailey/ragflow/blob/master/pyproject.toml) (source: github_api): "tika==2.6.0",
- [code_permalink](https://github.com/ShirleyBailey/ragflow/blob/3ea340de7601778c8d05665a8bbc6b9364251cc7/download_deps.py) (source: github_api): urls = [     "http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb",     "http://ports.ubuntu.com/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_arm64.deb",     "htt
- [code_permalink](https://github.com/ShirleyBailey/ragflow/blob/3ea340de7601778c8d05665a8bbc6b9364251cc7/rag/app/naive.py) (source: github_api): import logging from tika import parser from io import BytesIO
- [code_permalink](https://github.com/ShirleyBailey/ragflow/blob/3ea340de7601778c8d05665a8bbc6b9364251cc7/rag/app/one.py) (source: github_api): # import logging from tika import parser from io import BytesIO import re
- [readme_excerpt](https://github.com/ShirleyBailey/ragflow/blob/master/README.md) (source: readme): It offers a streamlined RAG workflow for businesses of any scale, combining LLM (Large Language Models) to provide truthful question-answering capabilities, backed by well-founded citations from vario

### 53. liferay/liferay-portal

**Repository / product**

- Repository: [https://github.com/liferay/liferay-portal](https://github.com/liferay/liferay-portal)
- Company: Liferay
- Product: Liferay DXP
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://liferay.com

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 26/100 (a score, not a probability)
- Raw weighted score: 1.30 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 3
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Apache PDFBox`, run `run_1`, window `size:501..1000`, rank 1
  - Query: `"pdfbox" filename:build.gradle size:501..1000`
  - Retrieved 30 of 412 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 3
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache PDFBox` (pdf, generation) — manifest_declaration — [modules/apps/shared-dependencies/shared-dependencies-pdfbox/build.gradle](https://github.com/liferay/liferay-portal/blob/e991fedb012463b125a8a3c6daa85c008e789679/modules/apps/shared-dependencies/shared-dependencies-pdfbox/build.gradle)
- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/liferay/liferay-portal/blob/e991fedb012463b125a8a3c6daa85c008e789679/modules/apps/shared-dependencies/shared-dependencies-pdfbox/src/main/java/com/liferay/shared/dependencies/pdfbox/internal/activator/SharedDependenciesPDFBoxBundleActivator.java)

**Evidence trail**

- [api_response](https://github.com/liferay/liferay-portal) (source: github_api): stars=2262, fork=False, archived=False
- [readme_excerpt](https://github.com/liferay/liferay-portal/blob/master/README.md) (source: readme): company stated as 'Liferay'
- [manifest_line](https://github.com/liferay/liferay-portal/blob/e991fedb012463b125a8a3c6daa85c008e789679/modules/apps/shared-dependencies/shared-dependencies-pdfbox/build.gradle) (source: github_api): dependencies { compileInclude group: "com.github.jai-imageio", name: "jai-imageio-core", version: "1.4.0" compileInclude group: "com.github.jai-imageio", name: "jai-imageio-jpeg2000", version: "1.3.
- [code_permalink](https://github.com/liferay/liferay-portal/blob/e991fedb012463b125a8a3c6daa85c008e789679/modules/apps/shared-dependencies/shared-dependencies-pdfbox/src/main/java/com/liferay/shared/dependencies/pdfbox/internal/activator/SharedDependenciesPDFBoxBundleActivator.java) (source: github_api): package com.liferay.shared.dependencies.pdfbox.internal.activator;
- [readme_excerpt](https://github.com/liferay/liferay-portal/blob/master/README.md) (source: readme): The build system, marker files, and Gradle conventions used by these modules are documented in [`modules/README.md`](modules/README.md).

### 54. paunchygent/skriptoteket

**Repository / product**

- Repository: [https://github.com/paunchygent/skriptoteket](https://github.com/paunchygent/skriptoteket)
- Company: Unknown — not stated in the repository
- Product: Skriptoteket
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 25/100 (a score, not a probability)
- Raw weighted score: 1.25 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_2`, window `size:>16000`, rank 22
  - Query: `"weasyprint" filename:pyproject.toml size:>16000`
  - Retrieved 30 of 38 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/paunchygent/skriptoteket/blob/main/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/paunchygent/skriptoteket/blob/faef46a807a7982ae48abee35c666ef8069866ea/runner/pdf_helper.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/paunchygent/skriptoteket/blob/faef46a807a7982ae48abee35c666ef8069866ea/scripts/run_pytest_with_native_libs.py)

**Evidence trail**

- [api_response](https://github.com/paunchygent/skriptoteket) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/paunchygent/skriptoteket/blob/main/pyproject.toml) (source: github_api): "weasyprint>=69.0",
- [code_permalink](https://github.com/paunchygent/skriptoteket/blob/faef46a807a7982ae48abee35c666ef8069866ea/runner/pdf_helper.py) (source: github_api): raise ToolUserError("Kunde inte skapa undermappar för PDF-utdata.") from exc     try:         from weasyprint import HTML  # imported lazily; tool scripts may not need PDF support         HT
- [code_permalink](https://github.com/paunchygent/skriptoteket/blob/faef46a807a7982ae48abee35c666ef8069866ea/scripts/run_pytest_with_native_libs.py) (source: github_api): Purpose:     Provide the repo-owned pytest command surface for local validation where     WeasyPrint-backed PDF renderers need macOS package-manager libraries. Relationships:     - Used by PDM `test`
- [readme_excerpt](https://github.com/paunchygent/skriptoteket/blob/main/README.md) (source: readme): It’s designed to be **self-hosted** and adapted to local IT constraints (on‑prem, private cloud, intranet/VPN-only, central logging, approved SMTP relays, strict data retention).

### 55. microsoft/powerplatform-vscode

**Repository / product**

- Repository: [https://github.com/microsoft/powerplatform-vscode](https://github.com/microsoft/powerplatform-vscode)
- Company: Unknown — not stated in the repository
- Product: Power Platform Tools for VS Code
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 25/100 (a score, not a probability)
- Raw weighted score: 1.25 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_2`, window `size:>16000`, rank 29
  - Query: `"puppeteer" filename:package.json size:>16000`
  - Retrieved 30 of 856 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package-lock.json](https://github.com/microsoft/powerplatform-vscode/blob/main/package-lock.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/microsoft/powerplatform-vscode/blob/main/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/microsoft/powerplatform-vscode/blob/7c5ba5ac4c8b75dd9ac78b9a6ccb84d3c25aa5cc/src/debugger/RequestInterceptor.ts)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/microsoft/powerplatform-vscode/blob/7c5ba5ac4c8b75dd9ac78b9a6ccb84d3c25aa5cc/src/debugger/browser/BrowserManager.ts)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/microsoft/powerplatform-vscode/blob/7c5ba5ac4c8b75dd9ac78b9a6ccb84d3c25aa5cc/src/debugger/controlLocation/ControlLocator.ts)

**Evidence trail**

- [api_response](https://github.com/microsoft/powerplatform-vscode) (source: github_api): stars=272, fork=False, archived=False
- [manifest_line](https://github.com/microsoft/powerplatform-vscode/blob/main/package-lock.json) (source: github_api): "puppeteer-core": "^22.13.1",
- [manifest_line](https://github.com/microsoft/powerplatform-vscode/blob/main/package.json) (source: github_api): "test-e2e": "npx playwright test --config=src/e2e/playwright.config.ts",
- [code_permalink](https://github.com/microsoft/powerplatform-vscode/blob/7c5ba5ac4c8b75dd9ac78b9a6ccb84d3c25aa5cc/src/debugger/RequestInterceptor.ts) (source: github_api): import { EventEmitter, HTTPRequest, Page } from "puppeteer-core"; import { Disposable } from "vscode";
- [code_permalink](https://github.com/microsoft/powerplatform-vscode/blob/7c5ba5ac4c8b75dd9ac78b9a6ccb84d3c25aa5cc/src/debugger/browser/BrowserManager.ts) (source: github_api): /**  * Class that controls a {@link puppeteer.Browser puppeteer browser instance} and manages all logic that interacts with puppeteer including:  * - {@link BrowserLocator} to locate the browser.
- [code_permalink](https://github.com/microsoft/powerplatform-vscode/blob/7c5ba5ac4c8b75dd9ac78b9a6ccb84d3c25aa5cc/src/debugger/controlLocation/ControlLocator.ts) (source: github_api): import { Page } from "puppeteer-core"; import { Disposable } from "vscode";
- [readme_excerpt](https://github.com/microsoft/powerplatform-vscode/blob/main/README.md) (source: readme): An integrated VS Code chat participant (`@powerpages`) that helps you write code by describing your expected behavior in natural language.

### 56. jreyesr/n8n-nodes-carbonejs

**Repository / product**

- Repository: [https://github.com/jreyesr/n8n-nodes-carbonejs](https://github.com/jreyesr/n8n-nodes-carbonejs)
- Company: Unknown — not stated in the repository
- Product: n8n-nodes-carbonejs
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://blog.jreyesr.com/posts/n8n-node-carbone-1/

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 24/100 (a score, not a probability)
- Raw weighted score: 1.20 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 27
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 27
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — manifest_declaration — [package-lock.json](https://github.com/jreyesr/n8n-nodes-carbonejs/blob/master/package-lock.json)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [package.json](https://github.com/jreyesr/n8n-nodes-carbonejs/blob/master/package.json)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/jreyesr/n8n-nodes-carbonejs/blob/a5ef92931ff0759a2546e59bc351a14e05a607f5/carbone.d.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/jreyesr/n8n-nodes-carbonejs/blob/a5ef92931ff0759a2546e59bc351a14e05a607f5/nodes/CarboneNode/CarboneUtils.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/jreyesr/n8n-nodes-carbonejs/blob/a5ef92931ff0759a2546e59bc351a14e05a607f5/nodes/CarboneNode/CarboneNode.node.ts)

**Evidence trail**

- [api_response](https://github.com/jreyesr/n8n-nodes-carbonejs) (source: github_api): stars=56, fork=False, archived=False
- [manifest_line](https://github.com/jreyesr/n8n-nodes-carbonejs/blob/master/package-lock.json) (source: github_api): "name": "n8n-nodes-carbonejs",
- [manifest_line](https://github.com/jreyesr/n8n-nodes-carbonejs/blob/master/package.json) (source: github_api): "name": "n8n-nodes-carbonejs",
- [code_permalink](https://github.com/jreyesr/n8n-nodes-carbonejs/blob/a5ef92931ff0759a2546e59bc351a14e05a607f5/carbone.d.ts) (source: github_api): // Overwrite an old @types/carbone declaration: // carbone.convert() no longer is convert(data, convertTo, options?, callback) // but convert(data, options?, callback), similar to the render() functio
- [code_permalink](https://github.com/jreyesr/n8n-nodes-carbonejs/blob/a5ef92931ff0759a2546e59bc351a14e05a607f5/nodes/CarboneNode/CarboneUtils.ts) (source: github_api): import os from 'os'; import path from 'path'; import carbone from 'carbone'; import type {Readable} from 'stream'; import {IBinaryData, IExecuteFunctions} from 'n8n-workflow';
- [code_permalink](https://github.com/jreyesr/n8n-nodes-carbonejs/blob/a5ef92931ff0759a2546e59bc351a14e05a607f5/nodes/CarboneNode/CarboneNode.node.ts) (source: github_api): description: 'Locale of the generated document, it will used for translation `{t()}`, formatting numbers with `:formatN`, and currencies `:formatC`. See https://github.com/carboneio/carbone/b
- [readme_excerpt](https://github.com/jreyesr/n8n-nodes-carbonejs/blob/master/README.md) (source: readme): It lets you use [the Carbone JS library](https://carbone.io/) in your n8n workflows.

### 57. yashiroots-school/School

**Repository / product**

- Repository: [https://github.com/yashiroots-school/school](https://github.com/yashiroots-school/school)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 24/100 (a score, not a probability)
- Raw weighted score: 1.20 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Open XML SDK`, run `run_2`, window `size:>16000`, rank 27
  - Query: `"DocumentFormat.OpenXml" filename:packages.config size:>16000`
  - Retrieved 30 of 31 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `iText`, run `run_2`, window `size:>16000`, rank 6
  - Query: `"itext" filename:packages.config size:>16000`
  - Retrieved 9 of 9 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Open XML SDK` (docx, generation) — code_import — [code](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/ViewModels/SiblingVM.cs)
- `Open XML SDK` (docx, generation) — code_import — [code](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/Controllers/FeeController.cs)
- `Open XML SDK` (docx, generation) — code_import — [code](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/Controllers/AccountController.cs)
- `Open XML SDK` (docx, generation) — code_import — [code](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/Controllers/TimeTableNewController.cs)
- `Open XML SDK` (docx, generation) — code_import — [code](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/Controllers/SMSandEmailController.cs)
- `iText` (pdf, generation) — manifest_declaration — [SchoolManagement.Data/packages.config](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Data/packages.config)
- `iText` (pdf, generation) — code_import — [code](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/Controllers/AdmissionFeeController.cs)
- `iText` (pdf, generation) — manifest_declaration — [SchoolManagement.Data/SchoolManagement.Data.csproj](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Data/SchoolManagement.Data.csproj)
- `iText` (pdf, generation) — manifest_declaration — [SchoolManagement.Website/packages.config](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/packages.config)
- `iText` (pdf, generation) — manifest_declaration — [SchoolManagement.Website/SchoolManagement.Website.csproj](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/SchoolManagement.Website.csproj)

**Evidence trail**

- [api_response](https://github.com/yashiroots-school/School) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/ViewModels/SiblingVM.cs) (source: github_api): ﻿using DocumentFormat.OpenXml.Office.CoverPageProps; using System; using System.Collections.Generic; using System.ComponentModel.DataAnnotations; using System.Linq; using System.Web;
- [code_permalink](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/Controllers/FeeController.cs) (source: github_api): ﻿using DocumentFormat.OpenXml.Bibliography; using EmployeeManagement.Repository; using Microsoft.Extensions.Primitives; using Rotativa; using SchoolManagement.Data.Constants; using SchoolManagement.Da
- [code_permalink](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/Controllers/AccountController.cs) (source: github_api): using System.Web.Mvc; using ClosedXML.Excel; using DataAccess.ViewModels; using DocumentFormat.OpenXml.VariantTypes; using Microsoft.AspNet.Identity; using Microsoft.AspNet.Identity.EntityFramework; u
- [code_permalink](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/Controllers/TimeTableNewController.cs) (source: github_api): using System.Web.Mvc; using System.Data.SqlClient; using SchoolManagement.Website.ViewModels; using DocumentFormat.OpenXml.VariantTypes; using System.Configuration; using System.Data;
- [code_permalink](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/Controllers/SMSandEmailController.cs) (source: github_api): using System.Globalization; using System.Collections.Specialized; using DocumentFormat.OpenXml.Bibliography; using DocumentFormat.OpenXml.Spreadsheet; namespace SchoolManagement.Website.Controllers {
- [manifest_line](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Data/packages.config) (source: github_api): <package id="ExcelNumberFormat" version="1.0.10" targetFramework="net461" />   <package id="GoogleApi" version="4.0.7" targetFramework="net461" />   <package id="iTextSharp" version="5.5.13.3" targe
- [code_permalink](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/Controllers/AdmissionFeeController.cs) (source: github_api): ﻿using EmployeeManagement.Repository; using iTextSharp.text; using iTextSharp.text.pdf; using iTextSharp.tool.xml; using Microsoft.Ajax.Utilities; using Rotativa; using SchoolManagement.Data.Constants
- [manifest_line](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Data/SchoolManagement.Data.csproj) (source: github_api): <Reference Include="GoogleApi, Version=4.0.7.0, Culture=neutral, PublicKeyToken=781851e053b06e74, processorArchitecture=MSIL">       <HintPath>..\packages\GoogleApi.4.0.7\lib\net45\GoogleApi.dll</
- [manifest_line](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/packages.config) (source: github_api): <package id="HtmlRenderer.Core" version="1.5.1-beta1" targetFramework="net48" />   <package id="HtmlRenderer.PdfSharp" version="1.5.1-beta1" targetFramework="net48" />   <package id="iTextSharp" ver
- [manifest_line](https://github.com/yashiroots-school/School/blob/7dec2440751cd286b2a655da6dc3dea873ccf61c/SchoolManagement.Website/SchoolManagement.Website.csproj) (source: github_api): <Reference Include="HtmlRenderer.PdfSharp, Version=1.5.1.0, Culture=neutral, processorArchitecture=MSIL">       <HintPath>..\packages\HtmlRenderer.PdfSharp.1.5.1-beta1\lib\net45\HtmlRenderer.PdfSh

### 58. PaNGalaxy/galaxy

**Repository / product**

- Repository: [https://github.com/pangalaxy/galaxy](https://github.com/pangalaxy/galaxy)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 24/100 (a score, not a probability)
- Raw weighted score: 1.20 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_2`, window `size:2001..4000`, rank 29
  - Query: `"weasyprint" filename:requirements.txt size:2001..4000`
  - Sampled 30 of 1,336 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,336 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [lib/galaxy/dependencies/conditional-requirements.txt](https://github.com/PaNGalaxy/galaxy/blob/301b0ce54e9ca3c3a0425c66878d68b2332a5d00/lib/galaxy/dependencies/conditional-requirements.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/PaNGalaxy/galaxy/blob/301b0ce54e9ca3c3a0425c66878d68b2332a5d00/lib/galaxy/dependencies/__init__.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/PaNGalaxy/galaxy/blob/301b0ce54e9ca3c3a0425c66878d68b2332a5d00/lib/galaxy/managers/configuration.py)

**Evidence trail**

- [api_response](https://github.com/PaNGalaxy/galaxy) (source: github_api): stars=3, fork=False, archived=False
- [manifest_line](https://github.com/PaNGalaxy/galaxy/blob/301b0ce54e9ca3c3a0425c66878d68b2332a5d00/lib/galaxy/dependencies/conditional-requirements.txt) (source: github_api): # Deep learning packages for tool recommendation tensorflow==2.15.1 # weasyprint has problematic requirements (cairo, Pango, see: # https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#li
- [code_permalink](https://github.com/PaNGalaxy/galaxy/blob/301b0ce54e9ca3c3a0425c66878d68b2332a5d00/lib/galaxy/dependencies/__init__.py) (source: github_api): def check_fastmcp(self):         return asbool(self.config.get("enable_mcp_server", False))     def check_weasyprint(self):         # See notes in ./conditional-requirements.txt for more informat
- [code_permalink](https://github.com/PaNGalaxy/galaxy/blob/301b0ce54e9ca3c3a0425c66878d68b2332a5d00/lib/galaxy/managers/configuration.py) (source: github_api): from galaxy.managers.context import ProvidesUserContext from galaxy.managers.markdown_util import weasyprint_available from galaxy.schema import SerializationParams
- [other](https://github.com/PaNGalaxy/galaxy/tree/main/templates) (source: github_api): directory templates/ present

### 59. 34j/decryptpdf

**Repository / product**

- Repository: [https://github.com/34j/decryptpdf](https://github.com/34j/decryptpdf)
- Company: Unknown — not stated in the repository
- Product: decryptpdf
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 24/100 (a score, not a probability)
- Raw weighted score: 1.20 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `pikepdf`, run `run_2`, window `size:2001..4000`, rank 22
  - Query: `"pikepdf" filename:pyproject.toml size:2001..4000`
  - Retrieved 30 of 125 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pikepdf` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/34j/decryptpdf/blob/main/pyproject.toml)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/34j/decryptpdf/blob/af979d681471f53ab3e1eb03a6423ba07b96779a/src/decryptpdf/_main.py)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/34j/decryptpdf/blob/af979d681471f53ab3e1eb03a6423ba07b96779a/tests/test_main.py)

**Evidence trail**

- [api_response](https://github.com/34j/decryptpdf) (source: github_api): stars=34, fork=False, archived=False
- [manifest_line](https://github.com/34j/decryptpdf/blob/main/pyproject.toml) (source: github_api): "pikepdf>=9.8.1",
- [code_permalink](https://github.com/34j/decryptpdf/blob/af979d681471f53ab3e1eb03a6423ba07b96779a/src/decryptpdf/_main.py) (source: github_api): import pikepdf
- [code_permalink](https://github.com/34j/decryptpdf/blob/af979d681471f53ab3e1eb03a6423ba07b96779a/tests/test_main.py) (source: github_api): import pikepdf import pytest
- [other](https://github.com/34j/decryptpdf/tree/main/templates) (source: github_api): directory templates/ present

### 60. vasilistotskas/grooveshop-django-api

**Repository / product**

- Repository: [https://github.com/vasilistotskas/grooveshop-django-api](https://github.com/vasilistotskas/grooveshop-django-api)
- Company: Unknown — not stated in the repository
- Product: Grooveshop Django API
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 24/100 (a score, not a probability)
- Raw weighted score: 1.20 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_2`, window `size:8001..16000`, rank 30
  - Query: `"weasyprint" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 92 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/vasilistotskas/grooveshop-django-api/blob/main/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/vasilistotskas/grooveshop-django-api/blob/0c73374afc8e5c86ea5a99a309d05e8ab191f2bd/order/invoicing.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/vasilistotskas/grooveshop-django-api/blob/0c73374afc8e5c86ea5a99a309d05e8ab191f2bd/tests/unit/order/test_invoicing.py)

**Evidence trail**

- [api_response](https://github.com/vasilistotskas/grooveshop-django-api) (source: github_api): stars=8, fork=False, archived=False
- [manifest_line](https://github.com/vasilistotskas/grooveshop-django-api/blob/main/pyproject.toml) (source: github_api): "weasyprint>=69.0",
- [code_permalink](https://github.com/vasilistotskas/grooveshop-django-api/blob/0c73374afc8e5c86ea5a99a309d05e8ab191f2bd/order/invoicing.py) (source: github_api): pin ``_compute_vat_breakdown`` and ``_build_context`` without spinning up WeasyPrint's native stack:
- [code_permalink](https://github.com/vasilistotskas/grooveshop-django-api/blob/0c73374afc8e5c86ea5a99a309d05e8ab191f2bd/tests/unit/order/test_invoicing.py) (source: github_api): Covers the parts that don't need WeasyPrint's GTK stack: the atomic counter, the VAT breakdown computation, the totals derivation, and
- [other](https://github.com/vasilistotskas/grooveshop-django-api/tree/main/templates) (source: github_api): directory templates/ present

### 61. fossasia/eventyay

**Repository / product**

- Repository: [https://github.com/fossasia/eventyay](https://github.com/fossasia/eventyay)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://eventyay.com

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 23/100 (a score, not a probability)
- Raw weighted score: 1.15 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `pypdf / PyPDF2`, run `run_2`, window `size:8001..16000`, rank 29
  - Query: `"pypdf" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 594 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `ReportLab`, run `run_2`, window `size:8001..16000`, rank 12
  - Query: `"reportlab" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 233 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [app/pyproject.toml](https://github.com/fossasia/eventyay/blob/dev/app/pyproject.toml)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/helpers/reportlab.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/orga/views/cards.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/plugins/reports/apps.py)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [app/pyproject.toml](https://github.com/fossasia/eventyay/blob/dev/app/pyproject.toml)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/base/pdf.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/plugins/badges/models.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/control/views/pdf.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/plugins/ticketoutputpdf/exporters.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/plugins/badges/exporters.py)

**Evidence trail**

- [api_response](https://github.com/fossasia/eventyay) (source: github_api): stars=1650, fork=False, archived=False
- [manifest_line](https://github.com/fossasia/eventyay/blob/dev/app/pyproject.toml) (source: github_api): "reportlab>=5.0.0",
- [code_permalink](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/helpers/reportlab.py) (source: github_api): from PIL.Image import Resampling from reportlab.lib.utils import ImageReader
- [code_permalink](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/orga/views/cards.py) (source: github_api): import reportlab.rl_config from django.contrib import messages
- [code_permalink](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/plugins/reports/apps.py) (source: github_api): try:             import reportlab  # NOQA         except ImportError:             errs.append("Python package 'reportlab' is not installed.")         return errs
- [manifest_line](https://github.com/fossasia/eventyay/blob/dev/app/pyproject.toml) (source: github_api): "pypdf>=6.16.1",
- [code_permalink](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/base/pdf.py) (source: github_api): from django.utils.translation import gettext_lazy as _ from pypdf import PdfReader from zoneinfo import ZoneInfo
- [code_permalink](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/plugins/badges/models.py) (source: github_api): from django.db import models from django.utils.crypto import get_random_string from django.utils.translation import gettext_lazy as _ from pypdf import PdfReader from eventyay.base.models import Logg
- [code_permalink](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/control/views/pdf.py) (source: github_api): from django.utils.translation import gettext as _ from django.views.generic import TemplateView from pypdf import PdfReader, PdfWriter from pypdf.errors import PdfReadError from reportlab.lib.units im
- [code_permalink](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/plugins/ticketoutputpdf/exporters.py) (source: github_api): from django.db.models.functions import Coalesce from django.utils.translation import gettext as _ from django.utils.translation import gettext_lazy from pypdf import PdfWriter from eventyay.base.expo
- [code_permalink](https://github.com/fossasia/eventyay/blob/59f797ad5f567a9b0242804865eae6d6e0b9db65/app/eventyay/plugins/badges/exporters.py) (source: github_api): from django.db.models.functions import Coalesce from django.utils.translation import gettext as _ from django.utils.translation import gettext_lazy from pypdf import PdfReader, PdfWriter, Transformati
- [readme_excerpt](https://github.com/fossasia/eventyay/blob/dev/README.rst) (source: readme): For production or self-hosted server deployment, see the `Deployment`_ section below and ``DEPLOYMENT.md``.

### 62. DSPaul/COMPASS

**Repository / product**

- Repository: [https://github.com/dspaul/compass](https://github.com/dspaul/compass)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.compassapp.info

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 23/100 (a score, not a probability)
- Raw weighted score: 1.15 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `iText`, run `run_2`, window `size:2001..4000`, rank 3
  - Query: `"itext" extension:csproj size:2001..4000`
  - Sampled 30 of 3,464 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,464 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `iText` (pdf, generation) — manifest_declaration — [src/COMPASS.csproj](https://github.com/DSPaul/COMPASS/blob/master/src/COMPASS.csproj)
- `iText` (pdf, generation) — code_import — [code](https://github.com/DSPaul/COMPASS/blob/f44ee6027cc5ec981f9c4d63ed8ee035d582ee5e/src/ViewModels/Sources/PdfSourceViewModel.cs)

**Evidence trail**

- [api_response](https://github.com/DSPaul/COMPASS) (source: github_api): stars=155, fork=False, archived=False
- [manifest_line](https://github.com/DSPaul/COMPASS/blob/master/src/COMPASS.csproj) (source: github_api): <PackageReference Include="itext" Version="9.4.0" />
- [code_permalink](https://github.com/DSPaul/COMPASS/blob/f44ee6027cc5ec981f9c4d63ed8ee035d582ee5e/src/ViewModels/Sources/PdfSourceViewModel.cs) (source: github_api): using COMPASS.Tools; using ImageMagick; using ImageMagick.Formats; using iText.Kernel.Pdf; using iText.Kernel.Pdf.Canvas.Parser; using iText.Kernel.Pdf.Canvas.Parser.Listener; using System;
- [readme_excerpt](https://github.com/DSPaul/COMPASS/blob/master/README.md) (source: readme): and helps you keep an overview by reducing the amount of books that are on your screen at once.

### 63. WNormanTPN/HotelManagement

**Repository / product**

- Repository: [https://github.com/wnormantpn/hotelmanagement](https://github.com/wnormantpn/hotelmanagement)
- Company: Unknown — not stated in the repository
- Product: 🏨 Hotel Management System
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 23/100 (a score, not a probability)
- Raw weighted score: 1.15 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `iText`, run `run_2`, window `size:4001..8000`, rank 4
  - Query: `"itext" filename:packages.config size:4001..8000`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `iText` (pdf, generation) — manifest_declaration — [GUI/packages.config](https://github.com/WNormanTPN/HotelManagement/blob/8239bb9d18e293b2c17b8ad909ae2a16cd0e02ff/GUI/packages.config)
- `iText` (pdf, generation) — manifest_declaration — [GUI/GUI.csproj](https://github.com/WNormanTPN/HotelManagement/blob/8239bb9d18e293b2c17b8ad909ae2a16cd0e02ff/GUI/GUI.csproj)
- `iText` (pdf, generation) — code_import — [code](https://github.com/WNormanTPN/HotelManagement/blob/8239bb9d18e293b2c17b8ad909ae2a16cd0e02ff/GUI/GUI_BILL/BillForm.cs)
- `iText` (pdf, generation) — code_import — [code](https://github.com/WNormanTPN/HotelManagement/blob/8239bb9d18e293b2c17b8ad909ae2a16cd0e02ff/GUI/GUI_BOOKING/ThanhToan.cs)
- `iText` (pdf, generation) — code_import — [code](https://github.com/WNormanTPN/HotelManagement/blob/8239bb9d18e293b2c17b8ad909ae2a16cd0e02ff/GUI/GUI_BOOKING/frmBookingNew.cs)

**Evidence trail**

- [api_response](https://github.com/WNormanTPN/HotelManagement) (source: github_api): stars=1, fork=False, archived=False
- [manifest_line](https://github.com/WNormanTPN/HotelManagement/blob/8239bb9d18e293b2c17b8ad909ae2a16cd0e02ff/GUI/packages.config) (source: github_api): <package id="Google.Apis.Auth" version="1.68.0" targetFramework="net472" />   <package id="Google.Apis.Core" version="1.68.0" targetFramework="net472" />   <package id="Google.Apis.Gmail.v1" version
- [manifest_line](https://github.com/WNormanTPN/HotelManagement/blob/8239bb9d18e293b2c17b8ad909ae2a16cd0e02ff/GUI/GUI.csproj) (source: github_api): <Reference Include="itext.barcodes, Version=9.0.0.0, Culture=neutral, PublicKeyToken=8354ae6d2174ddca, processorArchitecture=MSIL">       <HintPath>..\packages\itext.9.0.0\lib\net461\itext.barcode
- [code_permalink](https://github.com/WNormanTPN/HotelManagement/blob/8239bb9d18e293b2c17b8ad909ae2a16cd0e02ff/GUI/GUI_BILL/BillForm.cs) (source: github_api): ﻿using BUS; using GUI.GUI_COMPONENT; using iTextSharp.text.pdf; using iTextSharp.text; using Org.BouncyCastle.Asn1.X500; using System; using System.Collections.Generic;
- [code_permalink](https://github.com/WNormanTPN/HotelManagement/blob/8239bb9d18e293b2c17b8ad909ae2a16cd0e02ff/GUI/GUI_BOOKING/ThanhToan.cs) (source: github_api): ﻿using BUS; using DTO; using GUI.GUI_COMPONENT; using iTextSharp.text.pdf; using iTextSharp.text; using System; using System.Collections.Generic;
- [code_permalink](https://github.com/WNormanTPN/HotelManagement/blob/8239bb9d18e293b2c17b8ad909ae2a16cd0e02ff/GUI/GUI_BOOKING/frmBookingNew.cs) (source: github_api): using System.IO; using System.Linq; using System.Windows.Forms; using iTextSharp.text; using iTextSharp.text.pdf; using System.Text;
- [readme_excerpt](https://github.com/WNormanTPN/HotelManagement/blob/master/README.md) (source: readme): Service charges** **Time ranges** (daily, monthly, yearly, etc.) ![Statistics](./Resources/statistics.png) <br> <br> **Clone the repository**: git clone https://github.com/WNormanTPN/hotel-management-

### 64. symfony/webpack-encore

**Repository / product**

- Repository: [https://github.com/symfony/webpack-encore](https://github.com/symfony/webpack-encore)
- Company: Symfony
- Product: Webpack Encore: A Simple & Powerful Webpack API
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://symfony.com/doc/current/frontend.html

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; contributor_count not collected

**Score**

- Score: 23/100 (a score, not a probability)
- Raw weighted score: 1.15 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_2`, window `size:8001..16000`, rank 18
  - Query: `"puppeteer" filename:package.json size:8001..16000`
  - Sampled 30 of 1,644 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,644 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/symfony/webpack-encore/blob/main/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/symfony/webpack-encore/blob/cf7da2b9a47627aab305a4e378b2691ac8c6bdaf/eslint.config.js)

**Evidence trail**

- [api_response](https://github.com/symfony/webpack-encore) (source: github_api): stars=2221, fork=False, archived=False
- [readme_excerpt](https://github.com/symfony/webpack-encore/blob/main/README.md) (source: readme): company stated as 'Symfony'
- [manifest_line](https://github.com/symfony/webpack-encore/blob/main/package.json) (source: github_api): "puppeteer": "^25.0.2",
- [code_permalink](https://github.com/symfony/webpack-encore/blob/cf7da2b9a47627aab305a4e378b2691ac8c6bdaf/eslint.config.js) (source: github_api): languageOptions: {             ecmaVersion: 2025,             globals: {                 // For Puppeteer when calling "page.evaluate()"                 document: 'readonly',             },

### 65. robusta-dev/robusta

**Repository / product**

- Repository: [https://github.com/robusta-dev/robusta](https://github.com/robusta-dev/robusta)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://home.robusta.dev/

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 23/100 (a score, not a probability)
- Raw weighted score: 1.15 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `ReportLab`, run `run_2`, window `size:4001..8000`, rank 13
  - Query: `"reportlab" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 769 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/robusta-dev/robusta/blob/master/pyproject.toml)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/robusta-dev/robusta/blob/b392d6396baf11cc256da52f5996bfa1af7db8c3/src/robusta/core/sinks/transformer.py)

**Evidence trail**

- [api_response](https://github.com/robusta-dev/robusta) (source: github_api): stars=3076, fork=False, archived=False
- [manifest_line](https://github.com/robusta-dev/robusta/blob/master/pyproject.toml) (source: github_api): reportlab = "^5.0.0"
- [code_permalink](https://github.com/robusta-dev/robusta/blob/b392d6396baf11cc256da52f5996bfa1af7db8c3/src/robusta/core/sinks/transformer.py) (source: github_api): # reportlab is imported lazily so the PDF toolchain is only required on the         # scan-report path, not for merely importing the sink layer
- [readme_excerpt](https://github.com/robusta-dev/robusta/blob/master/README.md) (source: readme): You can use Robusta without Prometheus, or install our all-in-one Kubernetes observability stack with Robusta and Prometheus included.

### 66. cuba-platform/yarg

**Repository / product**

- Repository: [https://github.com/cuba-platform/yarg](https://github.com/cuba-platform/yarg)
- Company: Haulmont
- Product: Unknown
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.cuba-platform.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: contributor_count not collected

**Score**

- Score: 23/100 (a score, not a probability)
- Raw weighted score: 1.15 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 12
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 12
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `docx4j`, run `run_2`, window `size:8001..16000`, rank 1
  - Query: `"docx4j" filename:build.gradle size:8001..16000`
  - Retrieved 8 of 8 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Apache PDFBox`, run `run_2`, window `size:8001..16000`, rank 18
  - Query: `"pdfbox" filename:build.gradle size:8001..16000`
  - Retrieved 30 of 321 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `iText`, run `run_2`, window `size:8001..16000`, rank 5
  - Query: `"itext" filename:build.gradle size:8001..16000`
  - Retrieved 30 of 318 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/cuba-platform/yarg/blob/3b3f2aa009de69748bd82c86520911c84c3d04cf/core/modules/core/src/com/haulmont/yarg/formatters/impl/JasperFormatter.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/cuba-platform/yarg/blob/3b3f2aa009de69748bd82c86520911c84c3d04cf/core/modules/core/src/com/haulmont/yarg/formatters/impl/jasper/CubaJRFunction.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/cuba-platform/yarg/blob/3b3f2aa009de69748bd82c86520911c84c3d04cf/core/modules/core/src/com/haulmont/yarg/formatters/impl/jasper/JRBandDataDataSource.java)
- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [core/build.gradle](https://github.com/cuba-platform/yarg/blob/3b3f2aa009de69748bd82c86520911c84c3d04cf/core/build.gradle)

**Evidence trail**

- [api_response](https://github.com/cuba-platform/yarg) (source: github_api): stars=256, fork=False, archived=False
- [readme_excerpt](https://github.com/cuba-platform/yarg/blob/master/README.md) (source: readme): company stated as 'Haulmont'
- [code_permalink](https://github.com/cuba-platform/yarg/blob/3b3f2aa009de69748bd82c86520911c84c3d04cf/core/modules/core/src/com/haulmont/yarg/formatters/impl/JasperFormatter.java) (source: github_api): import com.haulmont.yarg.formatters.impl.jasper.JRBandDataDataSource; import com.haulmont.yarg.structure.ReportOutputType; import com.haulmont.yarg.structure.ReportTemplate; import net.sf.jasperreport
- [code_permalink](https://github.com/cuba-platform/yarg/blob/3b3f2aa009de69748bd82c86520911c84c3d04cf/core/modules/core/src/com/haulmont/yarg/formatters/impl/jasper/CubaJRFunction.java) (source: github_api): package com.haulmont.yarg.formatters.impl.jasper; import net.sf.jasperreports.engine.JRDataSource; import net.sf.jasperreports.functions.annotations.FunctionCategory; import java.io.ByteArrayInputSt
- [code_permalink](https://github.com/cuba-platform/yarg/blob/3b3f2aa009de69748bd82c86520911c84c3d04cf/core/modules/core/src/com/haulmont/yarg/formatters/impl/jasper/JRBandDataDataSource.java) (source: github_api): package com.haulmont.yarg.formatters.impl.jasper; import com.haulmont.yarg.structure.BandData; import net.sf.jasperreports.engine.JRDataSource; import net.sf.jasperreports.engine.JRException; import
- [manifest_line](https://github.com/cuba-platform/yarg/blob/3b3f2aa009de69748bd82c86520911c84c3d04cf/core/build.gradle) (source: github_api): }         compile(group: "com.opencsv", name: "opencsv", version: "5.7.1")         compile group: 'org.olap4j', name: 'olap4j', version: '1.2.0'         compile(group: "net.sf.jasperreports",

### 67. Kavithma-Thushal/Computershop-Management-System-1st-Sem-Final

**Repository / product**

- Repository: [https://github.com/kavithma-thushal/computershop-management-system-1st-sem-final](https://github.com/kavithma-thushal/computershop-management-system-1st-sem-final)
- Company: Unknown — not stated in the repository
- Product: ✌️Bashicomputershop-1st-Sem-Final
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; contributor_count not collected

**Score**

- Score: 23/100 (a score, not a probability)
- Raw weighted score: 1.15 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 24
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 24
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/Kavithma-Thushal/Computershop-Management-System-1st-Sem-Final/blob/master/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/Kavithma-Thushal/Computershop-Management-System-1st-Sem-Final/blob/2be53e55ca069e74190af06fbdd51d23c70f70e0/src/main/java/lk/ijse/computershop/controller/ManagereportsFormController.java)

**Evidence trail**

- [api_response](https://github.com/Kavithma-Thushal/Computershop-Management-System-1st-Sem-Final) (source: github_api): stars=17, fork=False, archived=False
- [readme_excerpt](https://github.com/Kavithma-Thushal/Computershop-Management-System-1st-Sem-Final/blob/master/README.md) (source: readme): company stated as 'All Right Reserved Designed'
- [manifest_line](https://github.com/Kavithma-Thushal/Computershop-Management-System-1st-Sem-Final/blob/master/pom.xml) (source: github_api): <groupId>net.sf.jasperreports</groupId>
- [code_permalink](https://github.com/Kavithma-Thushal/Computershop-Management-System-1st-Sem-Final/blob/2be53e55ca069e74190af06fbdd51d23c70f70e0/src/main/java/lk/ijse/computershop/controller/ManagereportsFormController.java) (source: github_api): import javafx.scene.input.MouseEvent; import lk.ijse.computershop.db.DBConnection; import net.sf.jasperreports.engine.*; import net.sf.jasperreports.view.JasperViewer; import java.io.InputStream; imp

### 68. QuivrHQ/MegaParse

**Repository / product**

- Repository: [https://github.com/quivrhq/megaparse](https://github.com/quivrhq/megaparse)
- Company: Unknown — not stated in the repository
- Product: MegaParse - Your Parser for every type of documents
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://megaparse.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 22/100 (a score, not a probability)
- Raw weighted score: 1.10 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 3 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 2
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Unstructured`, run `run_1`, window `size:1001..2000`, rank 6
  - Query: `"unstructured" filename:pyproject.toml size:1001..2000`
  - Sampled 30 of 1,070 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,070 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 2
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Apache Tika`, run `run_2`, window `size:2001..4000`, rank 1
  - Query: `"tika" filename:pyproject.toml size:2001..4000`
  - Retrieved 30 of 115 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Unstructured`, run `run_2`, window `size:2001..4000`, rank 8
  - Query: `"unstructured" filename:pyproject.toml size:2001..4000`
  - Retrieved 30 of 728 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [code](https://github.com/QuivrHQ/MegaParse/blob/main/Dockerfile)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [pyproject.toml](https://github.com/QuivrHQ/MegaParse/blob/main/pyproject.toml)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/QuivrHQ/MegaParse/blob/ba9a24aec950d6cf14834b8e2e11f5725778f12e/libs/megaparse/examples/parse_file_unstructured.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/QuivrHQ/MegaParse/blob/ba9a24aec950d6cf14834b8e2e11f5725778f12e/libs/megaparse/src/megaparse/parser/unstructured_parser.py)

**Evidence trail**

- [api_response](https://github.com/QuivrHQ/MegaParse) (source: github_api): stars=7412, fork=False, archived=False
- [code_permalink](https://github.com/QuivrHQ/MegaParse/blob/main/Dockerfile) (source: github_api): libreoffice \
- [manifest_line](https://github.com/QuivrHQ/MegaParse/blob/main/pyproject.toml) (source: github_api): "unstructured: these tests require `unstructured` dependency",
- [code_permalink](https://github.com/QuivrHQ/MegaParse/blob/ba9a24aec950d6cf14834b8e2e11f5725778f12e/libs/megaparse/examples/parse_file_unstructured.py) (source: github_api): from dataclasses import dataclass from time import perf_counter from unstructured.partition.auto import partition @dataclass
- [code_permalink](https://github.com/QuivrHQ/MegaParse/blob/ba9a24aec950d6cf14834b8e2e11f5725778f12e/libs/megaparse/src/megaparse/parser/unstructured_parser.py) (source: github_api): ) from megaparse_sdk.schema.extensions import FileExtension from megaparse_sdk.schema.parser_config import StrategyEnum from unstructured.documents.elements import Element from unstructured.partition.
- [api_response](https://github.com/QuivrHQ/MegaParse) (source: github_api): stars=7412, fork=False, archived=False
- [code_permalink](https://github.com/QuivrHQ/MegaParse/blob/main/Dockerfile) (source: github_api): FROM python:3.11.10-slim-bullseye WORKDIR /app # Install runtime dependencies RUN apt-get update && apt-get upgrade && apt-get install -y \     libgeos-dev \     libcurl4-openssl-dev \     libssl-de
- [code_permalink](https://github.com/QuivrHQ/MegaParse/blob/main/Dockerfile) (source: github_api): libreoffice \
- [code_permalink](https://github.com/QuivrHQ/MegaParse/blob/main/Dockerfile) (source: github_api): libreoffice \
- [manifest_line](https://github.com/QuivrHQ/MegaParse/blob/main/pyproject.toml) (source: github_api): "unstructured: these tests require `unstructured` dependency",
- [code_permalink](https://github.com/QuivrHQ/MegaParse/blob/ba9a24aec950d6cf14834b8e2e11f5725778f12e/libs/megaparse/examples/parse_file_unstructured.py) (source: github_api): from dataclasses import dataclass from time import perf_counter from unstructured.partition.auto import partition @dataclass
- [code_permalink](https://github.com/QuivrHQ/MegaParse/blob/ba9a24aec950d6cf14834b8e2e11f5725778f12e/libs/megaparse/src/megaparse/parser/unstructured_parser.py) (source: github_api): ) from megaparse_sdk.schema.extensions import FileExtension from megaparse_sdk.schema.parser_config import StrategyEnum from unstructured.documents.elements import Element from unstructured.partition.

### 69. City-of-Helsinki/kaavapino

**Repository / product**

- Repository: [https://github.com/city-of-helsinki/kaavapino](https://github.com/city-of-helsinki/kaavapino)
- Company: Unknown — not stated in the repository
- Product: kaavapino
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 29
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 29
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [pyproject.toml](https://github.com/City-of-Helsinki/kaavapino/blob/development/pyproject.toml)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/City-of-Helsinki/kaavapino/blob/117c42407c7124840b1e4c62bfae0ae5d440b27d/projects/exporting/document.py)

**Evidence trail**

- [api_response](https://github.com/City-of-Helsinki/kaavapino) (source: github_api): stars=3, fork=False, archived=False
- [manifest_line](https://github.com/City-of-Helsinki/kaavapino/blob/development/pyproject.toml) (source: github_api): docxtpl = "0.16.7"
- [code_permalink](https://github.com/City-of-Helsinki/kaavapino/blob/117c42407c7124840b1e4c62bfae0ae5d440b27d/projects/exporting/document.py) (source: github_api): from django.utils import timezone from django.core.cache import cache from docx.shared import Mm from docxtpl import DocxTemplate, InlineImage, Listing, RichText from xltpl.writerx import BookWriter f

### 70. xkevio/Creasy

**Repository / product**

- Repository: [https://github.com/xkevio/creasy](https://github.com/xkevio/creasy)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Apache PDFBox`, run `run_2`, window `size:2001..4000`, rank 19
  - Query: `"pdfbox" filename:pom.xml size:2001..4000`
  - Sampled 30 of 6,672 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 6,672 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Apache PDFBox` (pdf, generation) — manifest_declaration — [pom.xml](https://github.com/xkevio/Creasy/blob/main/pom.xml)
- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/xkevio/Creasy/blob/c704af049eb924b66ad0158e9f76a7cf7bf61d2c/src/main/java/ovgu/creasy/util/exporter/history/PDFHistoryExporter.java)
- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/xkevio/Creasy/blob/c704af049eb924b66ad0158e9f76a7cf7bf61d2c/src/main/java/ovgu/creasy/util/exporter/cp/PDFCreasePatternExporter.java)

**Evidence trail**

- [api_response](https://github.com/xkevio/Creasy) (source: github_api): stars=15, fork=False, archived=False
- [manifest_line](https://github.com/xkevio/Creasy/blob/main/pom.xml) (source: github_api): <groupId>org.apache.pdfbox</groupId>
- [code_permalink](https://github.com/xkevio/Creasy/blob/c704af049eb924b66ad0158e9f76a7cf7bf61d2c/src/main/java/ovgu/creasy/util/exporter/history/PDFHistoryExporter.java) (source: github_api): import de.rototor.pdfbox.graphics2d.PdfBoxGraphics2D; import javafx.scene.Parent;
- [code_permalink](https://github.com/xkevio/Creasy/blob/c704af049eb924b66ad0158e9f76a7cf7bf61d2c/src/main/java/ovgu/creasy/util/exporter/cp/PDFCreasePatternExporter.java) (source: github_api): package ovgu.creasy.util.exporter.cp; import de.rototor.pdfbox.graphics2d.PdfBoxGraphics2D; import org.apache.pdfbox.pdmodel.PDDocument; import org.apache.pdfbox.pdmodel.PDPage; import org.apache.pdf
- [readme_excerpt](https://github.com/xkevio/Creasy/blob/main/README.md) (source: readme): This allows you to put together the generated folding sequences as you like and export them as needed.

### 71. beenuar/AiSOC

**Repository / product**

- Repository: [https://github.com/beenuar/aisoc](https://github.com/beenuar/aisoc)
- Company: Unknown — not stated in the repository
- Product: AiSOC
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://tryaisoc.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_2`, window `size:2001..4000`, rank 10
  - Query: `"weasyprint" filename:pyproject.toml size:2001..4000`
  - Retrieved 30 of 872 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/beenuar/AiSOC/blob/98e8dfc809bf89f9962c3025775ea6dd7d3402eb/scripts/render_white_paper.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/beenuar/AiSOC/blob/98e8dfc809bf89f9962c3025775ea6dd7d3402eb/services/agents/app/api/investigate.py)

**Evidence trail**

- [api_response](https://github.com/beenuar/AiSOC) (source: github_api): stars=2488, fork=False, archived=False
- [code_permalink](https://github.com/beenuar/AiSOC/blob/98e8dfc809bf89f9962c3025775ea6dd7d3402eb/scripts/render_white_paper.py) (source: github_api): It uses the WeasyPrint stack already required by the executive-digest PDF in ``services/api/app/services/digest_pdf.py`` plus a ``markdown``
- [code_permalink](https://github.com/beenuar/AiSOC/blob/98e8dfc809bf89f9962c3025775ea6dd7d3402eb/services/agents/app/api/investigate.py) (source: github_api): GET  /api/v1/investigations/{run_id}/report.html   GET  /api/v1/investigations/{run_id}/report.pdf  → weasyprint PDF   WS   /api/v1/investigations/{run_id}/stream  → SSE-style step stream

### 72. Friday-Labs-Inc/friday

**Repository / product**

- Repository: [https://github.com/friday-labs-inc/friday](https://github.com/friday-labs-inc/friday)
- Company: Unknown — not stated in the repository
- Product: Friday
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_2`, window `size:8001..16000`, rank 28
  - Query: `"weasyprint" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 92 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/Friday-Labs-Inc/friday/blob/main/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/Friday-Labs-Inc/friday/blob/bb2829e56c3495e0c633e6cc625c422692b3f68c/frappe/utils/weasyprint.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/Friday-Labs-Inc/friday/blob/bb2829e56c3495e0c633e6cc625c422692b3f68c/frappe/utils/print_utils.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/Friday-Labs-Inc/friday/blob/bb2829e56c3495e0c633e6cc625c422692b3f68c/frappe/www/printview.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/Friday-Labs-Inc/friday/blob/bb2829e56c3495e0c633e6cc625c422692b3f68c/frappe/public/js/print_format_builder/Preview.vue)

**Evidence trail**

- [api_response](https://github.com/Friday-Labs-Inc/friday) (source: github_api): stars=3, fork=False, archived=False
- [manifest_line](https://github.com/Friday-Labs-Inc/friday/blob/main/pyproject.toml) (source: github_api): "WeasyPrint==68.0",
- [code_permalink](https://github.com/Friday-Labs-Inc/friday/blob/bb2829e56c3495e0c633e6cc625c422692b3f68c/frappe/utils/weasyprint.py) (source: github_api): This generator draws its inspiration and, also a bit of its implementation, from this discussion in the library github issues: https://github.com/Kozea/WeasyPrint/issues/92 """
- [code_permalink](https://github.com/Friday-Labs-Inc/friday/blob/bb2829e56c3495e0c633e6cc625c422692b3f68c/frappe/utils/print_utils.py) (source: github_api): is_weasyprint_print_format = False if print_format and print_format != "Standard":
- [code_permalink](https://github.com/Friday-Labs-Inc/friday/blob/bb2829e56c3495e0c633e6cc625c422692b3f68c/frappe/www/printview.py) (source: github_api): print_format = get_print_format_doc(None, meta=meta) if print_format and print_format.get("print_format_builder_beta"): from frappe.utils.weasyprint import get_html body = get_html( doctype
- [code_permalink](https://github.com/Friday-Labs-Inc/friday/blob/bb2829e56c3495e0c633e6cc625c422692b3f68c/frappe/public/js/print_format_builder/Preview.vue) (source: github_api): params.append("letterhead", store.value.letterhead.name); } let _url = type.value == "PDF" ? `/api/method/frappe.utils.weasyprint.download_pdf` : "/printpreview"; return `${_url}?${params.toStr

### 73. pinussilvestrus/postit-js

**Repository / product**

- Repository: [https://github.com/pinussilvestrus/postit-js](https://github.com/pinussilvestrus/postit-js)
- Company: Unknown — not stated in the repository
- Product: postit-js
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://postit-js-demo.netlify.app/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_2`, window `size:2001..4000`, rank 25
  - Query: `"puppeteer" filename:package.json size:2001..4000`
  - Sampled 30 of 25,792 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 25,792 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package-lock.json](https://github.com/pinussilvestrus/postit-js/blob/main/package-lock.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/pinussilvestrus/postit-js/blob/main/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/pinussilvestrus/postit-js/blob/64b3a02e97719872b82628317b97b46533703489/karma.conf.js)

**Evidence trail**

- [api_response](https://github.com/pinussilvestrus/postit-js) (source: github_api): stars=96, fork=False, archived=False
- [manifest_line](https://github.com/pinussilvestrus/postit-js/blob/main/package-lock.json) (source: github_api): "puppeteer": "^21.0.0",
- [manifest_line](https://github.com/pinussilvestrus/postit-js/blob/main/package.json) (source: github_api): "puppeteer": "^21.0.0",
- [code_permalink](https://github.com/pinussilvestrus/postit-js/blob/64b3a02e97719872b82628317b97b46533703489/karma.conf.js) (source: github_api): var browsers = (process.env.TEST_BROWSERS \|\| 'ChromeHeadless').split(','); // use puppeteer provided Chrome for testing process.env.CHROME_BIN = require('puppeteer').executablePath(); var basePath =

### 74. jerry609/PaperBot

**Repository / product**

- Repository: [https://github.com/jerry609/paperbot](https://github.com/jerry609/paperbot)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://paper-bot-git-test-milestone-v12-jerrys-projects-bfbe8245.vercel.app/studio

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_2`, window `size:2001..4000`, rank 26
  - Query: `"weasyprint" filename:requirements.txt size:2001..4000`
  - Sampled 30 of 1,336 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,336 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/jerry609/PaperBot/blob/dev/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements-ci.txt](https://github.com/jerry609/PaperBot/blob/dev/requirements-ci.txt)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements.txt](https://github.com/jerry609/PaperBot/blob/dev/requirements.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/jerry609/PaperBot/blob/9030c5e2e327f0205f5fa0a8a62b6529b760104e/src/paperbot/core/report_engine/renderers/__init__.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/jerry609/PaperBot/blob/9030c5e2e327f0205f5fa0a8a62b6529b760104e/src/paperbot/core/report_engine/renderers/pdf_renderer.py)

**Evidence trail**

- [api_response](https://github.com/jerry609/PaperBot) (source: github_api): stars=108, fork=False, archived=False
- [manifest_line](https://github.com/jerry609/PaperBot/blob/dev/pyproject.toml) (source: github_api): "weasyprint>=62.3",
- [manifest_line](https://github.com/jerry609/PaperBot/blob/dev/requirements-ci.txt) (source: github_api): # Keep this smaller than requirements.txt to avoid heavy system deps (e.g. weasyprint).
- [manifest_line](https://github.com/jerry609/PaperBot/blob/dev/requirements.txt) (source: github_api): weasyprint>=62.3
- [code_permalink](https://github.com/jerry609/PaperBot/blob/9030c5e2e327f0205f5fa0a8a62b6529b760104e/src/paperbot/core/report_engine/renderers/__init__.py) (source: github_api): 提供多种输出格式的渲染能力： - HTMLRenderer: HTML 渲染 - PDFRenderer: PDF 渲染（依赖 weasyprint） """ from .base import RenderContext, Renderer
- [code_permalink](https://github.com/jerry609/PaperBot/blob/9030c5e2e327f0205f5fa0a8a62b6529b760104e/src/paperbot/core/report_engine/renderers/pdf_renderer.py) (source: github_api): """ HTML -> PDF 渲染（依赖 weasyprint，可选）。 """

### 75. dfir-iris/docx-generator

**Repository / product**

- Repository: [https://github.com/dfir-iris/docx-generator](https://github.com/dfir-iris/docx-generator)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 22
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 22
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [pyproject.toml](https://github.com/dfir-iris/docx-generator/blob/master/pyproject.toml)
- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [requirements.txt](https://github.com/dfir-iris/docx-generator/blob/master/requirements.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/dfir-iris/docx-generator/blob/41cf2b33f12fc333a0ef62d96ebf16d3d2c74f44/src/docx_generator/globals/globals.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/dfir-iris/docx-generator/blob/41cf2b33f12fc333a0ef62d96ebf16d3d2c74f44/src/docx_generator/globals/document_globals.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/dfir-iris/docx-generator/blob/41cf2b33f12fc333a0ef62d96ebf16d3d2c74f44/src/docx_generator/globals/picture_globals.py)

**Evidence trail**

- [api_response](https://github.com/dfir-iris/docx-generator) (source: github_api): stars=5, fork=False, archived=False
- [manifest_line](https://github.com/dfir-iris/docx-generator/blob/master/pyproject.toml) (source: github_api): "docxtpl==0.19.0",
- [manifest_line](https://github.com/dfir-iris/docx-generator/blob/master/requirements.txt) (source: github_api): docxtpl==0.19.0
- [code_permalink](https://github.com/dfir-iris/docx-generator/blob/41cf2b33f12fc333a0ef62d96ebf16d3d2c74f44/src/docx_generator/globals/globals.py) (source: github_api): import logging from docxtpl import DocxTemplate from docxtpl import RichText from jinja2 import Environment from docx_generator.globals.document_globals import DocumentGlobals
- [code_permalink](https://github.com/dfir-iris/docx-generator/blob/41cf2b33f12fc333a0ef62d96ebf16d3d2c74f44/src/docx_generator/globals/document_globals.py) (source: github_api): from docxcompose.composer import Composer from docxtpl import DocxTemplate, Subdoc
- [code_permalink](https://github.com/dfir-iris/docx-generator/blob/41cf2b33f12fc333a0ef62d96ebf16d3d2c74f44/src/docx_generator/globals/picture_globals.py) (source: github_api): from docx.enum.text import WD_PARAGRAPH_ALIGNMENT from docxtpl import DocxTemplate, Subdoc

### 76. zhangzhen1979/JIMU-ConvertPreview

**Repository / product**

- Repository: [https://github.com/zhangzhen1979/jimu-convertpreview](https://github.com/zhangzhen1979/jimu-convertpreview)
- Company: Unknown — not stated in the repository
- Product: Convert-Preview 文件格式转换及预览服务
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 23
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 23
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Apache POI (XWPF/HWPF)`, run `run_2`, window `size:>16000`, rank 18
  - Query: `"poi" filename:pom.xml size:>16000`
  - Sampled 30 of 15,200 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 15,200 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/zhangzhen1979/JIMU-ConvertPreview/blob/master/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/zhangzhen1979/JIMU-ConvertPreview/blob/46902555e72b8ed83178fd03c17dd75f38f8e319/src/main/java/com/thinkdifferent/convertpreview/service/impl/x2x/ConvertXml2PdfServiceImpl.java)

**Evidence trail**

- [api_response](https://github.com/zhangzhen1979/JIMU-ConvertPreview) (source: github_api): stars=54, fork=False, archived=False
- [manifest_line](https://github.com/zhangzhen1979/JIMU-ConvertPreview/blob/master/pom.xml) (source: github_api): <groupId>net.sf.jasperreports</groupId>
- [code_permalink](https://github.com/zhangzhen1979/JIMU-ConvertPreview/blob/46902555e72b8ed83178fd03c17dd75f38f8e319/src/main/java/com/thinkdifferent/convertpreview/service/impl/x2x/ConvertXml2PdfServiceImpl.java) (source: github_api): import com.thinkdifferent.convertpreview.utils.XmlUtil; import lombok.SneakyThrows; import lombok.extern.log4j.Log4j2; import net.sf.jasperreports.engine.*; import net.sf.jasperreports.engine.fill.JRF

### 77. auchenberg/vscode-browser-preview

**Repository / product**

- Repository: [https://github.com/auchenberg/vscode-browser-preview](https://github.com/auchenberg/vscode-browser-preview)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_2`, window `size:8001..16000`, rank 15
  - Query: `"puppeteer" filename:package.json size:8001..16000`
  - Sampled 30 of 1,644 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,644 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/auchenberg/vscode-browser-preview/blob/master/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/auchenberg/vscode-browser-preview/blob/9904ed468c17062c0fd87c50c6b5dc7051666ffc/ext-src/browser.ts)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/auchenberg/vscode-browser-preview/blob/9904ed468c17062c0fd87c50c6b5dc7051666ffc/tests/puppeteer.js)

**Evidence trail**

- [api_response](https://github.com/auchenberg/vscode-browser-preview) (source: github_api): stars=4380, fork=False, archived=False
- [manifest_line](https://github.com/auchenberg/vscode-browser-preview/blob/master/package.json) (source: github_api): "puppeteer-core": "^1.11.0",
- [code_permalink](https://github.com/auchenberg/vscode-browser-preview/blob/9904ed468c17062c0fd87c50c6b5dc7051666ffc/ext-src/browser.ts) (source: github_api): import * as edge from '@chiragrupani/karma-chromium-edge-launcher'; import * as chrome from 'karma-chrome-launcher'; const puppeteer = require('puppeteer-core'); const getPort = require('get-port');
- [code_permalink](https://github.com/auchenberg/vscode-browser-preview/blob/9904ed468c17062c0fd87c50c6b5dc7051666ffc/tests/puppeteer.js) (source: github_api): const puppeteer = require('puppeteer'); (async () => {   const browser = await puppeteer.launch();   const page = await browser.newPage();   await page.goto('http://localhost:3000');

### 78. athola/simple-resume

**Repository / product**

- Repository: [https://github.com/athola/simple-resume](https://github.com/athola/simple-resume)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_2`, window `size:4001..8000`, rank 25
  - Query: `"weasyprint" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 419 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/athola/simple-resume/blob/main/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/athola/simple-resume/blob/aa2839c8bb960856b609a99da48c086c5417a2d0/src/simple_resume/shell/services.py)

**Evidence trail**

- [api_response](https://github.com/athola/simple-resume) (source: github_api): stars=58, fork=False, archived=False
- [manifest_line](https://github.com/athola/simple-resume/blob/main/pyproject.toml) (source: github_api): "weasyprint>=62.1,<63.0",
- [code_permalink](https://github.com/athola/simple-resume/blob/aa2839c8bb960856b609a99da48c086c5417a2d0/src/simple_resume/shell/services.py) (source: github_api): def __init__(self, mode: str = "weasyprint") -> None:         """Initialize the PDF generation strategy.

### 79. tghfly/grafana-chinese

**Repository / product**

- Repository: [https://github.com/tghfly/grafana-chinese](https://github.com/tghfly/grafana-chinese)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_2`, window `size:8001..16000`, rank 30
  - Query: `"puppeteer" filename:package.json size:8001..16000`
  - Sampled 30 of 1,644 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,644 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/tghfly/grafana-chinese/blob/master/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/tghfly/grafana-chinese/blob/5c16b85a63ca274134438fc6f3301918855b2dd8/jest.config.e2e.js)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/tghfly/grafana-chinese/blob/5c16b85a63ca274134438fc6f3301918855b2dd8/packages/grafana-toolkit/src/e2e/login.ts)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/tghfly/grafana-chinese/blob/5c16b85a63ca274134438fc6f3301918855b2dd8/packages/grafana-toolkit/src/e2e/install.ts)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/tghfly/grafana-chinese/blob/5c16b85a63ca274134438fc6f3301918855b2dd8/packages/grafana-toolkit/src/e2e/launcher.ts)

**Evidence trail**

- [api_response](https://github.com/tghfly/grafana-chinese) (source: github_api): stars=58, fork=False, archived=False
- [manifest_line](https://github.com/tghfly/grafana-chinese/blob/master/package.json) (source: github_api): "@types/expect-puppeteer": "4.4.0",
- [code_permalink](https://github.com/tghfly/grafana-chinese/blob/5c16b85a63ca274134438fc6f3301918855b2dd8/jest.config.e2e.js) (source: github_api): roots: ['<rootDir>/public/e2e-test'],   testRegex: '(\\.\|/)(test)\\.(jsx?\|tsx?)$',   moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json'],   setupFiles: [],   globals: { 'ts-jest': { isolatedMod
- [code_permalink](https://github.com/tghfly/grafana-chinese/blob/5c16b85a63ca274134438fc6f3301918855b2dd8/packages/grafana-toolkit/src/e2e/login.ts) (source: github_api): import { Page } from 'puppeteer-core'; import { constants } from './constants'; import { loginPage } from './pages/loginPage'; export const login = async (page: Page) => {   await loginPage.init(pag
- [code_permalink](https://github.com/tghfly/grafana-chinese/blob/5c16b85a63ca274134438fc6f3301918855b2dd8/packages/grafana-toolkit/src/e2e/install.ts) (source: github_api): import puppeteer from 'puppeteer-core'; import { constants } from './constants'; export const downloadBrowserIfNeeded = async (): Promise<void> => {   const browserFetcher = puppeteer.createBrowserFe
- [code_permalink](https://github.com/tghfly/grafana-chinese/blob/5c16b85a63ca274134438fc6f3301918855b2dd8/packages/grafana-toolkit/src/e2e/launcher.ts) (source: github_api): import puppeteer, { Browser } from 'puppeteer-core'; export const launchBrowser = async (): Promise<Browser> => {   const browserFetcher = puppeteer.createBrowserFetcher();   const localRevisions = a

### 80. jpmorganchase/modular

**Repository / product**

- Repository: [https://github.com/jpmorganchase/modular](https://github.com/jpmorganchase/modular)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://modular.js.org/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_2`, window `size:2001..4000`, rank 6
  - Query: `"puppeteer" filename:package.json size:2001..4000`
  - Sampled 30 of 25,792 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 25,792 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/jpmorganchase/modular/blob/main/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/jpmorganchase/modular/blob/e9615527cebabc41a1a921e9d94e714f20afcc4f/packages/modular-scripts/src/__tests__/start.test.ts)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/jpmorganchase/modular/blob/e9615527cebabc41a1a921e9d94e714f20afcc4f/packages/remote-view/src/__tests__/integration.test.tsx)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/jpmorganchase/modular/blob/e9615527cebabc41a1a921e9d94e714f20afcc4f/packages/modular-scripts/src/__tests__/index.test.ts)

**Evidence trail**

- [api_response](https://github.com/jpmorganchase/modular) (source: github_api): stars=640, fork=False, archived=False
- [manifest_line](https://github.com/jpmorganchase/modular/blob/main/package.json) (source: github_api): "@types/puppeteer": "^5.4.6",
- [code_permalink](https://github.com/jpmorganchase/modular/blob/e9615527cebabc41a1a921e9d94e714f20afcc4f/packages/modular-scripts/src/__tests__/start.test.ts) (source: github_api): import { exec } from 'child_process'; import fs from 'fs-extra'; import { getDocument, queries, waitFor } from 'pptr-testing-library'; import puppeteer from 'puppeteer'; import { DevServer, startApp }
- [code_permalink](https://github.com/jpmorganchase/modular/blob/e9615527cebabc41a1a921e9d94e714f20afcc4f/packages/remote-view/src/__tests__/integration.test.tsx) (source: github_api): import path from 'path'; import { spawn } from 'child_process'; import puppeteer from 'puppeteer'; import { getDocument, queries, waitFor } from 'pptr-testing-library'; const controller = new AbortC
- [code_permalink](https://github.com/jpmorganchase/modular/blob/e9615527cebabc41a1a921e9d94e714f20afcc4f/packages/modular-scripts/src/__tests__/index.test.ts) (source: github_api): getQueriesForElement,   queries, } from 'pptr-testing-library'; import puppeteer from 'puppeteer'; import getModularRoot from '../utils/getModularRoot'; import { DevServer, startApp } from './start-

### 81. Verivox/lighthouse-monitor

**Repository / product**

- Repository: [https://github.com/verivox/lighthouse-monitor](https://github.com/verivox/lighthouse-monitor)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_2`, window `size:2001..4000`, rank 23
  - Query: `"puppeteer" filename:package.json size:2001..4000`
  - Sampled 30 of 25,792 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 25,792 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package-lock.json](https://github.com/Verivox/lighthouse-monitor/blob/master/package-lock.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/Verivox/lighthouse-monitor/blob/master/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/Verivox/lighthouse-monitor/blob/4155437668f282d6b64615aaa412c19b0b25d09a/config/sample.js)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/Verivox/lighthouse-monitor/blob/4155437668f282d6b64615aaa412c19b0b25d09a/src/lighthouse.js)

**Evidence trail**

- [api_response](https://github.com/Verivox/lighthouse-monitor) (source: github_api): stars=183, fork=False, archived=False
- [manifest_line](https://github.com/Verivox/lighthouse-monitor/blob/master/package-lock.json) (source: github_api): "puppeteer": {
- [manifest_line](https://github.com/Verivox/lighthouse-monitor/blob/master/package.json) (source: github_api): "puppeteer": "^10.4.0",
- [code_permalink](https://github.com/Verivox/lighthouse-monitor/blob/4155437668f282d6b64615aaa412c19b0b25d09a/config/sample.js) (source: github_api): const presets = {     'mobile-snail': {         preset: 'mobile-snail',         // browserOptions - is an options object that is accepted by launch command of puppeteer         // https://github.com/p
- [code_permalink](https://github.com/Verivox/lighthouse-monitor/blob/4155437668f282d6b64615aaa412c19b0b25d09a/src/lighthouse.js) (source: github_api): * Licensed under MIT from the Verivox GmbH  */ const lighthouseLib = require('lighthouse') const puppeteer = require('puppeteer'); const DefaultOptions = {     browserOptions: {

### 82. UST-QuAntiL/latex-renderer

**Repository / product**

- Repository: [https://github.com/ust-quantil/latex-renderer](https://github.com/ust-quantil/latex-renderer)
- Company: Unknown — not stated in the repository
- Product: LaTex-Renderer
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Apache PDFBox`, run `run_2`, window `size:4001..8000`, rank 13
  - Query: `"pdfbox" filename:pom.xml size:4001..8000`
  - Sampled 30 of 7,824 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,824 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Apache PDFBox` (pdf, generation) — manifest_declaration — [pom.xml](https://github.com/UST-QuAntiL/latex-renderer/blob/master/pom.xml)
- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/UST-QuAntiL/latex-renderer/blob/ef8f2a7ccf86b210d87caf234a05aac58ca87409/src/main/java/com/renderLatex/service/RenderService.java)

**Evidence trail**

- [api_response](https://github.com/UST-QuAntiL/latex-renderer) (source: github_api): stars=9, fork=False, archived=False
- [manifest_line](https://github.com/UST-QuAntiL/latex-renderer/blob/master/pom.xml) (source: github_api): <!--Dependencies for PDFBox and Batik for pdf conversion-->
- [code_permalink](https://github.com/UST-QuAntiL/latex-renderer/blob/ef8f2a7ccf86b210d87caf234a05aac58ca87409/src/main/java/com/renderLatex/service/RenderService.java) (source: github_api): import org.apache.batik.svggen.SVGGraphics2D; import org.apache.batik.util.XMLResourceDescriptor; import org.apache.commons.io.FileUtils; import org.apache.pdfbox.Loader; import org.apache.pdfbox.pdmo
- [readme_excerpt](https://github.com/UST-QuAntiL/latex-renderer/blob/master/README.md) (source: readme): Service for rendering latex content such as algorithms, diagrams, pictures etc.

### 83. javadev/jasper-xml-to-pdf-generator

**Repository / product**

- Repository: [https://github.com/javadev/jasper-xml-to-pdf-generator](https://github.com/javadev/jasper-xml-to-pdf-generator)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 26
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 26
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/javadev/jasper-xml-to-pdf-generator/blob/main/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/javadev/jasper-xml-to-pdf-generator/blob/7c1a3cb83a5207c8ac40f7392b497d9902a75a32/src/main/java/com/github/xmltopdf/JasperPdfGenerator.java)

**Evidence trail**

- [api_response](https://github.com/javadev/jasper-xml-to-pdf-generator) (source: github_api): stars=16, fork=False, archived=False
- [manifest_line](https://github.com/javadev/jasper-xml-to-pdf-generator/blob/main/pom.xml) (source: github_api): <id>jasperreports</id>
- [code_permalink](https://github.com/javadev/jasper-xml-to-pdf-generator/blob/7c1a3cb83a5207c8ac40f7392b497d9902a75a32/src/main/java/com/github/xmltopdf/JasperPdfGenerator.java) (source: github_api): import net.sf.jasperreports.engine.JasperPrint; import net.sf.jasperreports.engine.JasperCompileManager; import net.sf.jasperreports.engine.JasperFillManager;

### 84. xcmt/ABC_report

**Repository / product**

- Repository: [https://github.com/xcmt/abc_report](https://github.com/xcmt/abc_report)
- Company: Unknown — not stated in the repository
- Product: 自动化安全测试报告生成器（练手）
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 26
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 26
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [requirements.txt](https://github.com/xcmt/ABC_report/blob/main/requirements.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/xcmt/ABC_report/blob/de20aef3263471178d6520f99d649a78d81b7b65/services/docx_render_service.py)

**Evidence trail**

- [api_response](https://github.com/xcmt/ABC_report) (source: github_api): stars=56, fork=False, archived=False
- [manifest_line](https://github.com/xcmt/ABC_report/blob/main/requirements.txt) (source: github_api): docxtpl>=0.16.0
- [code_permalink](https://github.com/xcmt/ABC_report/blob/de20aef3263471178d6520f99d649a78d81b7b65/services/docx_render_service.py) (source: github_api): import io import jinja2 from bs4 import BeautifulSoup from docxtpl import DocxTemplate, RichText, InlineImage from docx.shared import Inches from models import report as report_model, template as temp

### 85. qwc-services/jasper-reporting-service

**Repository / product**

- Repository: [https://github.com/qwc-services/jasper-reporting-service](https://github.com/qwc-services/jasper-reporting-service)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 14
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 14
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `iText`, run `run_2`, window `size:4001..8000`, rank 9
  - Query: `"itext" filename:pom.xml size:4001..8000`
  - Sampled 30 of 8,720 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 8,720 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/qwc-services/jasper-reporting-service/blob/master/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/qwc-services/jasper-reporting-service/blob/fb6e15ff16bd994a7c268fe1205fa7c321ec4bf8/src/main/java/jasperapp/Config.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/qwc-services/jasper-reporting-service/blob/fb6e15ff16bd994a7c268fe1205fa7c321ec4bf8/src/main/java/jasperapp/JasperEndpointController.java)

**Evidence trail**

- [api_response](https://github.com/qwc-services/jasper-reporting-service) (source: github_api): stars=11, fork=False, archived=False
- [manifest_line](https://github.com/qwc-services/jasper-reporting-service/blob/master/pom.xml) (source: github_api): <groupId>net.sf.jasperreports</groupId>
- [code_permalink](https://github.com/qwc-services/jasper-reporting-service/blob/fb6e15ff16bd994a7c268fe1205fa7c321ec4bf8/src/main/java/jasperapp/Config.java) (source: github_api): import org.springframework.web.servlet.config.annotation.DefaultServletHandlerConfigurer; import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter; import org.springframework.w
- [code_permalink](https://github.com/qwc-services/jasper-reporting-service/blob/fb6e15ff16bd994a7c268fe1205fa7c321ec4bf8/src/main/java/jasperapp/JasperEndpointController.java) (source: github_api): }         });         // This can be used in JasperReports to have absolute Image Paths         modelMap.put("ROOT_DIR", System.getProperty("user.dir") + "/" + reportsDirectory + (reportf

### 86. wso2/carbon-commons

**Repository / product**

- Repository: [https://github.com/wso2/carbon-commons](https://github.com/wso2/carbon-commons)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: real_estate (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 4
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 4
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Apache POI (XWPF/HWPF)`, run `run_2`, window `size:>16000`, rank 6
  - Query: `"poi" filename:pom.xml size:>16000`
  - Sampled 30 of 15,200 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 15,200 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `iText`, run `run_2`, window `size:>16000`, rank 9
  - Query: `"itext" filename:pom.xml size:>16000`
  - Sampled 30 of 2,044 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,044 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/wso2/carbon-commons/blob/master/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/wso2/carbon-commons/blob/15c762f7485dacc05b03b25f834cfb648f4c4b71/components/reporting/org.wso2.carbon.reporting.api/src/main/java/org/wso2/carbon/reporting/api/ReportData.java)
- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [components/reporting/org.wso2.carbon.reporting.core/pom.xml](https://github.com/wso2/carbon-commons/blob/15c762f7485dacc05b03b25f834cfb648f4c4b71/components/reporting/org.wso2.carbon.reporting.core/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [components/reporting/org.wso2.carbon.reporting.util/pom.xml](https://github.com/wso2/carbon-commons/blob/15c762f7485dacc05b03b25f834cfb648f4c4b71/components/reporting/org.wso2.carbon.reporting.util/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/wso2/carbon-commons/blob/15c762f7485dacc05b03b25f834cfb648f4c4b71/components/reporting/org.wso2.carbon.reporting.util/src/main/java/org/wso2/carbon/reporting/util/ReportStream.java)

**Evidence trail**

- [api_response](https://github.com/wso2/carbon-commons) (source: github_api): stars=59, fork=False, archived=False
- [manifest_line](https://github.com/wso2/carbon-commons/blob/master/pom.xml) (source: github_api): <groupId>org.wso2.orbit.net.sf.jasperreports</groupId>
- [code_permalink](https://github.com/wso2/carbon-commons/blob/15c762f7485dacc05b03b25f834cfb648f4c4b71/components/reporting/org.wso2.carbon.reporting.api/src/main/java/org/wso2/carbon/reporting/api/ReportData.java) (source: github_api): package org.wso2.carbon.reporting.api; import net.sf.jasperreports.engine.JRDataSource; /**  * should be implement to create a data source for the report
- [manifest_line](https://github.com/wso2/carbon-commons/blob/15c762f7485dacc05b03b25f834cfb648f4c4b71/components/reporting/org.wso2.carbon.reporting.core/pom.xml) (source: github_api): <artifactId>pax-logging-api</artifactId>         </dependency>         <dependency>             <groupId>org.wso2.orbit.net.sf.jasperreports</groupId>             <artifactId>jasperreports
- [manifest_line](https://github.com/wso2/carbon-commons/blob/15c762f7485dacc05b03b25f834cfb648f4c4b71/components/reporting/org.wso2.carbon.reporting.util/pom.xml) (source: github_api): <artifactId>pax-logging-api</artifactId>         </dependency>         <dependency>             <groupId>org.wso2.orbit.net.sf.jasperreports</groupId>             <artifactId>jasperreports
- [code_permalink](https://github.com/wso2/carbon-commons/blob/15c762f7485dacc05b03b25f834cfb648f4c4b71/components/reporting/org.wso2.carbon.reporting.util/src/main/java/org/wso2/carbon/reporting/util/ReportStream.java) (source: github_api): package org.wso2.carbon.reporting.util; import net.sf.jasperreports.engine.JRException; import net.sf.jasperreports.engine.JasperPrint; import org.wso2.carbon.reporting.api.ReportingException; import

### 87. Azure-Samples/healthcare-agent-orchestrator

**Repository / product**

- Repository: [https://github.com/azure-samples/healthcare-agent-orchestrator](https://github.com/azure-samples/healthcare-agent-orchestrator)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: healthcare_diagnostics (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 10
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 10
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [src/requirements.txt](https://github.com/Azure-Samples/healthcare-agent-orchestrator/blob/main/src/requirements.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [src/scenarios/default/requirements.txt](https://github.com/Azure-Samples/healthcare-agent-orchestrator/blob/f9abf14177c0c7c6817a990f45ffa19b3a4cd51b/src/scenarios/default/requirements.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/Azure-Samples/healthcare-agent-orchestrator/blob/f9abf14177c0c7c6817a990f45ffa19b3a4cd51b/src/scenarios/default/tools/content_export/content_export.py)

**Evidence trail**

- [api_response](https://github.com/Azure-Samples/healthcare-agent-orchestrator) (source: github_api): stars=206, fork=False, archived=False
- [manifest_line](https://github.com/Azure-Samples/healthcare-agent-orchestrator/blob/main/src/requirements.txt) (source: github_api): docxtpl==0.19.1
- [manifest_line](https://github.com/Azure-Samples/healthcare-agent-orchestrator/blob/f9abf14177c0c7c6817a990f45ffa19b3a4cd51b/src/scenarios/default/requirements.txt) (source: github_api): docxtpl==0.19.1 websockets==15.0.1
- [code_permalink](https://github.com/Azure-Samples/healthcare-agent-orchestrator/blob/f9abf14177c0c7c6817a990f45ffa19b3a4cd51b/src/scenarios/default/tools/content_export/content_export.py) (source: github_api): from azure.core.exceptions import ResourceNotFoundError from docx.shared import Inches from docxtpl import DocxTemplate, InlineImage, RichText from semantic_kernel.connectors.ai.open_ai.prompt_execut

### 88. AIGeniusInstitue/restfeel

**Repository / product**

- Repository: [https://github.com/aigeniusinstitue/restfeel](https://github.com/aigeniusinstitue/restfeel)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 20
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 20
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [build.gradle](https://github.com/AIGeniusInstitue/restfeel/blob/master/build.gradle)
- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/AIGeniusInstitue/restfeel/blob/master/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/AIGeniusInstitue/restfeel/blob/41a5066917d9a94b92be69e67f32fc08c46a9f52/src/main/java/com/restfeel/controller/rest/ReportController.java)

**Evidence trail**

- [api_response](https://github.com/AIGeniusInstitue/restfeel) (source: github_api): stars=74, fork=False, archived=False
- [manifest_line](https://github.com/AIGeniusInstitue/restfeel/blob/master/build.gradle) (source: github_api): compile('net.sf.jasperreports:jasperreports:6.0.0') {
- [manifest_line](https://github.com/AIGeniusInstitue/restfeel/blob/master/pom.xml) (source: github_api): <groupId>net.sf.jasperreports</groupId>
- [code_permalink](https://github.com/AIGeniusInstitue/restfeel/blob/41a5066917d9a94b92be69e67f32fc08c46a9f52/src/main/java/com/restfeel/controller/rest/ReportController.java) (source: github_api): import javax.servlet.http.HttpServletResponse; import net.sf.jasperreports.engine.JRException; import net.sf.jasperreports.engine.JasperExportManager; import net.sf.jasperreports.engine.JasperFillMa

### 89. zorazrw/odex

**Repository / product**

- Repository: [https://github.com/zorazrw/odex](https://github.com/zorazrw/odex)
- Company: Unknown — not stated in the repository
- Product: Execution-based Evaluation for Open Domain Code Generation
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://code-eval.github.io

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 18
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 18
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/zorazrw/odex/blob/21308ea6d474a078d5a85c61c2b5ca228d1fd167/library/imports.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [library/requirements.txt](https://github.com/zorazrw/odex/blob/21308ea6d474a078d5a85c61c2b5ca228d1fd167/library/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/zorazrw/odex) (source: github_api): stars=49, fork=False, archived=False
- [code_permalink](https://github.com/zorazrw/odex/blob/21308ea6d474a078d5a85c61c2b5ca228d1fd167/library/imports.py) (source: github_api): from django.conf import settings from django.db import models from django.http import HttpResponse from docxtpl import DocxTemplate from flask import Flask from functools import reduce from io import
- [manifest_line](https://github.com/zorazrw/odex/blob/21308ea6d474a078d5a85c61c2b5ca228d1fd167/library/requirements.txt) (source: github_api): configparser datetime django docxtpl flask lxml matplotlib

### 90. lincolnluiz/SpringBoot-JasperReports

**Repository / product**

- Repository: [https://github.com/lincolnluiz/springboot-jasperreports](https://github.com/lincolnluiz/springboot-jasperreports)
- Company: Unknown — not stated in the repository
- Product: SpringBoot + JasperReports
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 15
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 15
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/lincolnluiz/SpringBoot-JasperReports/blob/master/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/lincolnluiz/SpringBoot-JasperReports/blob/ca1f3efe9b6faa2b998258907e12de9b91e51ae9/src/main/java/com/github/lincolnluiz/SpringJasper/controller/RelatorioController.java)

**Evidence trail**

- [api_response](https://github.com/lincolnluiz/SpringBoot-JasperReports) (source: github_api): stars=33, fork=False, archived=False
- [manifest_line](https://github.com/lincolnluiz/SpringBoot-JasperReports/blob/master/pom.xml) (source: github_api): <groupId>net.sf.jasperreports</groupId>
- [code_permalink](https://github.com/lincolnluiz/SpringBoot-JasperReports/blob/ca1f3efe9b6faa2b998258907e12de9b91e51ae9/src/main/java/com/github/lincolnluiz/SpringJasper/controller/RelatorioController.java) (source: github_api): import org.springframework.web.bind.annotation.RequestMapping; import org.springframework.web.bind.annotation.RequestParam; import net.sf.jasperreports.engine.JRException; import net.sf.jasperrep

### 91. gooderp-study/GoodERP

**Repository / product**

- Repository: [https://github.com/gooderp-study/gooderp](https://github.com/gooderp-study/gooderp)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 20
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 20
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [requirements.txt](https://github.com/gooderp-study/GoodERP/blob/master/requirements.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/gooderp-study/GoodERP/blob/a3f460280fa02c48163d97182a590400243cf0a1/report_docx/__manifest__.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/gooderp-study/GoodERP/blob/a3f460280fa02c48163d97182a590400243cf0a1/report_docx/report/report_helper.py)

**Evidence trail**

- [api_response](https://github.com/gooderp-study/GoodERP) (source: github_api): stars=25, fork=False, archived=False
- [manifest_line](https://github.com/gooderp-study/GoodERP/blob/master/requirements.txt) (source: github_api): docxtpl>=0.6.3
- [code_permalink](https://github.com/gooderp-study/GoodERP/blob/a3f460280fa02c48163d97182a590400243cf0a1/report_docx/__manifest__.py) (source: github_api): ],     'external_dependencies': {         'python': [             'docxtpl', #            'python-ooxml', #            'pdfkit',         ],
- [code_permalink](https://github.com/gooderp-study/GoodERP/blob/a3f460280fa02c48163d97182a590400243cf0a1/report_docx/report/report_helper.py) (source: github_api): # © 2016 cole # License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html). from docxtpl import DocxTemplate import docx

### 92. davidkey/DynamicJasperExample

**Repository / product**

- Repository: [https://github.com/davidkey/dynamicjasperexample](https://github.com/davidkey/dynamicjasperexample)
- Company: Unknown — not stated in the repository
- Product: DynamicJasperExample
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 13
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 13
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/davidkey/DynamicJasperExample/blob/master/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/davidkey/DynamicJasperExample/blob/c2e181f0ef2d1ce7081452cb94f4749a9f6e2977/src/main/java/com/dak/jasperpoc/reports/Report.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/davidkey/DynamicJasperExample/blob/c2e181f0ef2d1ce7081452cb94f4749a9f6e2977/src/main/java/com/dak/jasperpoc/service/ReportService.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/davidkey/DynamicJasperExample/blob/c2e181f0ef2d1ce7081452cb94f4749a9f6e2977/src/main/java/com/dak/jasperpoc/reports/EmployeeReport.java)

**Evidence trail**

- [api_response](https://github.com/davidkey/DynamicJasperExample) (source: github_api): stars=30, fork=False, archived=False
- [manifest_line](https://github.com/davidkey/DynamicJasperExample/blob/master/pom.xml) (source: github_api): <jasperreports.version>7.0.4</jasperreports.version>
- [code_permalink](https://github.com/davidkey/DynamicJasperExample/blob/c2e181f0ef2d1ce7081452cb94f4749a9f6e2977/src/main/java/com/dak/jasperpoc/reports/Report.java) (source: github_api): import com.dak.jasperpoc.exception.ReportException; import net.sf.jasperreports.engine.JasperPrint; public interface Report { public JasperPrint getReport() throws ReportException;
- [code_permalink](https://github.com/davidkey/DynamicJasperExample/blob/c2e181f0ef2d1ce7081452cb94f4749a9f6e2977/src/main/java/com/dak/jasperpoc/service/ReportService.java) (source: github_api): import com.dak.jasperpoc.exception.ReportException; import net.sf.jasperreports.engine.JRException; import net.sf.jasperreports.engine.JasperExportManager; import net.sf.jasperreports.engine.JasperP
- [code_permalink](https://github.com/davidkey/DynamicJasperExample/blob/c2e181f0ef2d1ce7081452cb94f4749a9f6e2977/src/main/java/com/dak/jasperpoc/reports/EmployeeReport.java) (source: github_api): import ar.com.fdvs.dj.domain.constants.Transparency; import ar.com.fdvs.dj.domain.constants.VerticalAlign; import ar.com.fdvs.dj.domain.entities.columns.AbstractColumn; import net.sf.jasperreports.eng

### 93. zkoss/zk

**Repository / product**

- Repository: [https://github.com/zkoss/zk](https://github.com/zkoss/zk)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://www.zkoss.org

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 7
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 7
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [package-lock.json](https://github.com/zkoss/zk/blob/master/package-lock.json)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/zkoss/zk/blob/b83deca66da904525296170beff19a6baf9c53c2/zksandbox/src/main/java/org/zkoss/zksandbox/CustomDataSource.java)
- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [zksandbox/build.gradle](https://github.com/zkoss/zk/blob/b83deca66da904525296170beff19a6baf9c53c2/zksandbox/build.gradle)
- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [zktest/build.gradle](https://github.com/zkoss/zk/blob/b83deca66da904525296170beff19a6baf9c53c2/zktest/build.gradle)

**Evidence trail**

- [api_response](https://github.com/zkoss/zk) (source: github_api): stars=475, fork=False, archived=False
- [manifest_line](https://github.com/zkoss/zk/blob/master/package-lock.json) (source: github_api): "integrity": "sha512-oahGvuMGQlPw/ivIYBjVSrWAfWLBeku5tpPE2fOPLi+WHffIWbuh2tCjhyQhTBPMf5E9jDEH4FOmTYgYwbKwtQ==",
- [code_permalink](https://github.com/zkoss/zk/blob/b83deca66da904525296170beff19a6baf9c53c2/zksandbox/src/main/java/org/zkoss/zksandbox/CustomDataSource.java) (source: github_api): package org.zkoss.zksandbox; import net.sf.jasperreports.engine.JRDataSource; import net.sf.jasperreports.engine.JRException; import net.sf.jasperreports.engine.JRField;
- [manifest_line](https://github.com/zkoss/zk/blob/b83deca66da904525296170beff19a6baf9c53c2/zksandbox/build.gradle) (source: github_api): implementation 'org.zkoss.zk:zuljsp:1.4.1' implementation 'org.zkoss.zkforge.el:zcommons-el:1.1.0' implementation 'org.apache.commons:commons-lang3:3.20.0' implementation 'net.sf.jasperreports:
- [manifest_line](https://github.com/zkoss/zk/blob/b83deca66da904525296170beff19a6baf9c53c2/zktest/build.gradle) (source: github_api): implementation 'org.apache.commons:commons-lang3:3.20.0' implementation 'commons-beanutils:commons-beanutils:1.9.4' implementation 'com.google.javascript:closure-compiler-unshaded:v20230802' imple

### 94. Lawyer-ray/FachuanHybridSystem

**Repository / product**

- Repository: [https://github.com/lawyer-ray/fachuanhybridsystem](https://github.com/lawyer-ray/fachuanhybridsystem)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 21/100 (a score, not a probability)
- Raw weighted score: 1.05 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 10
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 10
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:4001..8000`, rank 5
  - Query: `"mammoth" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 92 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `pikepdf`, run `run_2`, window `size:4001..8000`, rank 10
  - Query: `"pikepdf" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 89 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `WeasyPrint`, run `run_2`, window `size:4001..8000`, rank 26
  - Query: `"weasyprint" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 419 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [backend/pyproject.toml](https://github.com/Lawyer-ray/FachuanHybridSystem/blob/main/backend/pyproject.toml)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/Lawyer-ray/FachuanHybridSystem/blob/faa86d83bac45f6b122a81edc59d82b5d6b1201d/backend/apps/cases/services/template/unified/renderer.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/Lawyer-ray/FachuanHybridSystem/blob/faa86d83bac45f6b122a81edc59d82b5d6b1201d/backend/apps/documents/services/generation/base_generator.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/Lawyer-ray/FachuanHybridSystem/blob/faa86d83bac45f6b122a81edc59d82b5d6b1201d/backend/apps/documents/services/generation/pipeline/preview.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/Lawyer-ray/FachuanHybridSystem/blob/faa86d83bac45f6b122a81edc59d82b5d6b1201d/backend/apps/documents/services/generation/pipeline/renderer.py)

**Evidence trail**

- [api_response](https://github.com/Lawyer-ray/FachuanHybridSystem) (source: github_api): stars=208, fork=False, archived=False
- [manifest_line](https://github.com/Lawyer-ray/FachuanHybridSystem/blob/main/backend/pyproject.toml) (source: github_api): "docxtpl==0.20.2",
- [code_permalink](https://github.com/Lawyer-ray/FachuanHybridSystem/blob/faa86d83bac45f6b122a81edc59d82b5d6b1201d/backend/apps/cases/services/template/unified/renderer.py) (source: github_api): import logging from typing import Any from docxtpl import DocxTemplate from apps.core.exceptions import ValidationException from apps.core.utils.path import Path
- [code_permalink](https://github.com/Lawyer-ray/FachuanHybridSystem/blob/faa86d83bac45f6b122a81edc59d82b5d6b1201d/backend/apps/documents/services/generation/base_generator.py) (source: github_api): """         使用 docxtpl 渲染模板
- [code_permalink](https://github.com/Lawyer-ray/FachuanHybridSystem/blob/faa86d83bac45f6b122a81edc59d82b5d6b1201d/backend/apps/documents/services/generation/pipeline/preview.py) (source: github_api): if simple_var is not None:                 stripped = simple_var.strip()                 # {{r xxx}} → docxtpl 的 RichText 内联标签，提取 xxx                 # {{p xxx}} → docxtpl 的 RichTextParagr
- [code_permalink](https://github.com/Lawyer-ray/FachuanHybridSystem/blob/faa86d83bac45f6b122a81edc59d82b5d6b1201d/backend/apps/documents/services/generation/pipeline/renderer.py) (source: github_api): class DocxRenderer:     def render(self, template_path: str, context: dict[str, Any]) -> bytes:  # pragma: no cover         from docxtpl import DocxTemplate         from apps.documents.services.plac

### 95. yusufkaraaslan/Skill_Seekers

**Repository / product**

- Repository: [https://github.com/yusufkaraaslan/skill_seekers](https://github.com/yusufkaraaslan/skill_seekers)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://skillseekersweb.com/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2; template_directory_present=true \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 20/100 (a score, not a probability)
- Raw weighted score: 1.00 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 2 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:8001..16000`, rank 3
  - Query: `"mammoth" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 59 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:8001..16000`, rank 3
  - Query: `"PyMuPDF" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 334 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `python-docx`, run `run_2`, window `size:8001..16000`, rank 11
  - Query: `"python-docx" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 486 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [pyproject.toml](https://github.com/yusufkaraaslan/Skill_Seekers/blob/development/pyproject.toml)
- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [requirements.txt](https://github.com/yusufkaraaslan/Skill_Seekers/blob/development/requirements.txt)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [pyproject.toml](https://github.com/yusufkaraaslan/Skill_Seekers/blob/development/pyproject.toml)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/yusufkaraaslan/Skill_Seekers/blob/f3972efa33fa79634b96936acf1fac321cdcf7c1/src/skill_seekers/cli/word_scraper.py)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/yusufkaraaslan/Skill_Seekers/blob/f3972efa33fa79634b96936acf1fac321cdcf7c1/src/skill_seekers/cli/doctor.py)
- `python-docx` (docx, generation) — manifest_declaration — [pyproject.toml](https://github.com/yusufkaraaslan/Skill_Seekers/blob/development/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/yusufkaraaslan/Skill_Seekers) (source: github_api): stars=14807, fork=False, archived=False
- [manifest_line](https://github.com/yusufkaraaslan/Skill_Seekers/blob/development/pyproject.toml) (source: github_api): "PyMuPDF>=1.24.14",
- [manifest_line](https://github.com/yusufkaraaslan/Skill_Seekers/blob/development/requirements.txt) (source: github_api): PyMuPDF==1.24.14
- [manifest_line](https://github.com/yusufkaraaslan/Skill_Seekers/blob/development/pyproject.toml) (source: github_api): "mammoth>=1.6.0",
- [code_permalink](https://github.com/yusufkaraaslan/Skill_Seekers/blob/f3972efa33fa79634b96936acf1fac321cdcf7c1/src/skill_seekers/cli/word_scraper.py) (source: github_api): Converts Word documents into AI skills. Uses mammoth for HTML conversion and python-docx for metadata/tables.
- [code_permalink](https://github.com/yusufkaraaslan/Skill_Seekers/blob/f3972efa33fa79634b96936acf1fac321cdcf7c1/src/skill_seekers/cli/doctor.py) (source: github_api): # ── Optional dependency import names ───────────────────────────────────────── OPTIONAL_DEPS = {     "mammoth": "mammoth",     "ebooklib": "ebooklib",     "yt-dlp": "yt_dlp",     "mcp": "mcp",
- [manifest_line](https://github.com/yusufkaraaslan/Skill_Seekers/blob/development/pyproject.toml) (source: github_api): "python-docx>=1.1.0",
- [other](https://github.com/yusufkaraaslan/Skill_Seekers/tree/development/templates) (source: github_api): directory templates/ present

### 96. bigbeartechworld/big-bear-casaos

**Repository / product**

- Repository: [https://github.com/bigbeartechworld/big-bear-casaos](https://github.com/bigbeartechworld/big-bear-casaos)
- Company: BigBearTechWorld
- Product: Big Bear CasaOS App Store
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://community.bigbeartechworld.com/c/bigbearyoutube/bigbearcasaos/10

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: contributor_count not collected

**Score**

- Score: 20/100 (a score, not a probability)
- Raw weighted score: 1.00 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 24
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 24
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [Apps/paperless-ngx/docker-compose.yml](https://github.com/bigbeartechworld/big-bear-casaos/blob/master/Apps/paperless-ngx/docker-compose.yml)

**Evidence trail**

- [api_response](https://github.com/bigbeartechworld/big-bear-casaos) (source: github_api): stars=617, fork=False, archived=False
- [readme_excerpt](https://github.com/bigbeartechworld/big-bear-casaos/blob/master/README.md) (source: readme): company stated as 'BigBearTechWorld'
- [other](https://github.com/bigbeartechworld/big-bear-casaos/tree/master/templates) (source: github_api): directory templates/ present
- [api_response](https://github.com/bigbeartechworld/big-bear-casaos) (source: github_api): stars=617, fork=False, archived=False
- [code_permalink](https://github.com/bigbeartechworld/big-bear-casaos/blob/master/Apps/paperless-ngx/docker-compose.yml) (source: github_api): # Configuration for paperless-ngx setup # Name of the big-bear-paperless-ngx application name: big-bear-paperless-ngx # Service definitions for the big-bear-paperless-ngx application services:   # Se
- [readme_excerpt](https://github.com/bigbeartechworld/big-bear-casaos/blob/master/README.md) (source: readme): company stated as 'BigBearTechWorld'
- [other](https://github.com/bigbeartechworld/big-bear-casaos/tree/master/templates) (source: github_api): directory templates/ present
- [api_response](https://github.com/bigbeartechworld/big-bear-casaos) (source: github_api): stars=617, fork=False, archived=False
- [code_permalink](https://github.com/bigbeartechworld/big-bear-casaos/blob/master/Apps/paperless-ngx/docker-compose.yml) (source: github_api): # Configuration for paperless-ngx setup # Name of the big-bear-paperless-ngx application name: big-bear-paperless-ngx # Service definitions for the big-bear-paperless-ngx application services:   # Se
- [readme_excerpt](https://github.com/bigbeartechworld/big-bear-casaos/blob/master/README.md) (source: readme): company stated as 'BigBearTechWorld'
- [manifest_line](https://github.com/bigbeartechworld/big-bear-casaos/blob/master/Apps/paperless-ngx/docker-compose.yml) (source: github_api): PAPERLESS_TIKA_GOTENBERG_ENDPOINT: http://big-bear-paperless-ngx-gotenberg:3000
- [other](https://github.com/bigbeartechworld/big-bear-casaos/tree/master/templates) (source: github_api): directory templates/ present
- [api_response](https://github.com/bigbeartechworld/big-bear-casaos) (source: github_api): stars=617, fork=False, archived=False
- [code_permalink](https://github.com/bigbeartechworld/big-bear-casaos/blob/master/Apps/paperless-ngx/docker-compose.yml) (source: github_api): # Configuration for paperless-ngx setup # Name of the big-bear-paperless-ngx application name: big-bear-paperless-ngx # Service definitions for the big-bear-paperless-ngx application services:   # Se
- [readme_excerpt](https://github.com/bigbeartechworld/big-bear-casaos/blob/master/README.md) (source: readme): company stated as 'BigBearTechWorld'
- [manifest_line](https://github.com/bigbeartechworld/big-bear-casaos/blob/master/Apps/paperless-ngx/docker-compose.yml) (source: github_api): PAPERLESS_TIKA_GOTENBERG_ENDPOINT: http://big-bear-paperless-ngx-gotenberg:3000
- [other](https://github.com/bigbeartechworld/big-bear-casaos/tree/master/templates) (source: github_api): directory templates/ present

### 97. rsrdesarrollo/sarna

**Repository / product**

- Repository: [https://github.com/rsrdesarrollo/sarna](https://github.com/rsrdesarrollo/sarna)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 20/100 (a score, not a probability)
- Raw weighted score: 1.00 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 15
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 15
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [requirements.txt](https://github.com/rsrdesarrollo/sarna/blob/master/requirements.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/rsrdesarrollo/sarna/blob/6a858459fe77437af9321bbdb9c42297592b931c/sarna/report_generator/engine.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/rsrdesarrollo/sarna/blob/6a858459fe77437af9321bbdb9c42297592b931c/sarna/report_generator/markdown.py)

**Evidence trail**

- [api_response](https://github.com/rsrdesarrollo/sarna) (source: github_api): stars=43, fork=False, archived=False
- [manifest_line](https://github.com/rsrdesarrollo/sarna/blob/master/requirements.txt) (source: github_api): docxtpl==0.8.0
- [code_permalink](https://github.com/rsrdesarrollo/sarna/blob/6a858459fe77437af9321bbdb9c42297592b931c/sarna/report_generator/engine.py) (source: github_api): from typing import * import jinja2 from docxtpl import DocxTemplate from markupsafe import Markup from werkzeug.utils import secure_filename
- [code_permalink](https://github.com/rsrdesarrollo/sarna/blob/6a858459fe77437af9321bbdb9c42297592b931c/sarna/report_generator/markdown.py) (source: github_api): import mistletoe from PIL import Image from docx.section import Section from docxtpl import DocxTemplate from mistletoe.base_renderer import BaseRenderer from sarna.report_generator import *
- [other](https://github.com/rsrdesarrollo/sarna/tree/master/templates) (source: github_api): directory templates/ present

### 98. lr101/homelab

**Repository / product**

- Repository: [https://github.com/lr101/homelab](https://github.com/lr101/homelab)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 20/100 (a score, not a probability)
- Raw weighted score: 1.00 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 26
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 26
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [medion/nextcloud/docker-compose.yaml](https://github.com/lr101/homelab/blob/main/medion/nextcloud/docker-compose.yaml)

**Evidence trail**

- [api_response](https://github.com/lr101/homelab) (source: github_api): stars=1, fork=False, archived=False
- [readme_excerpt](https://github.com/lr101/homelab/blob/main/README.md) (source: readme): **Internet Access:** External clients connect via HTTPS to the public IP, where a Traefik reverse proxy routes requests to services running on the internal devices over the encrypted VPN tunnel.
- [api_response](https://github.com/lr101/homelab) (source: github_api): stars=1, fork=False, archived=False
- [code_permalink](https://github.com/lr101/homelab/blob/main/medion/nextcloud/docker-compose.yaml) (source: github_api): services:   nextcloud:     image: nextcloud:34     restart: always     annotations:     - de.lr-projects.description=File sharing and collaboration     - de.lr-projects.sso=true     volumes:     - ./n
- [readme_excerpt](https://github.com/lr101/homelab/blob/main/README.md) (source: readme): **Internet Access:** External clients connect via HTTPS to the public IP, where a Traefik reverse proxy routes requests to services running on the internal devices over the encrypted VPN tunnel.
- [api_response](https://github.com/lr101/homelab) (source: github_api): stars=1, fork=False, archived=False
- [code_permalink](https://github.com/lr101/homelab/blob/main/medion/nextcloud/docker-compose.yaml) (source: github_api): services:   nextcloud:     image: nextcloud:34     restart: always     annotations:     - de.lr-projects.description=File sharing and collaboration     - de.lr-projects.sso=true     volumes:     - ./n
- [manifest_line](https://github.com/lr101/homelab/blob/main/medion/nextcloud/docker-compose.yaml) (source: github_api): - de.lr-projects.description=LibreOffice Online
- [readme_excerpt](https://github.com/lr101/homelab/blob/main/README.md) (source: readme): **Internet Access:** External clients connect via HTTPS to the public IP, where a Traefik reverse proxy routes requests to services running on the internal devices over the encrypted VPN tunnel.
- [api_response](https://github.com/lr101/homelab) (source: github_api): stars=1, fork=False, archived=False
- [code_permalink](https://github.com/lr101/homelab/blob/main/medion/nextcloud/docker-compose.yaml) (source: github_api): services:   nextcloud:     image: nextcloud:34     restart: always     annotations:     - de.lr-projects.description=File sharing and collaboration     - de.lr-projects.sso=true     volumes:     - ./n
- [manifest_line](https://github.com/lr101/homelab/blob/main/medion/nextcloud/docker-compose.yaml) (source: github_api): - de.lr-projects.description=LibreOffice Online
- [readme_excerpt](https://github.com/lr101/homelab/blob/main/README.md) (source: readme): **Internet Access:** External clients connect via HTTPS to the public IP, where a Traefik reverse proxy routes requests to services running on the internal devices over the encrypted VPN tunnel.

### 99. RCGAI/SimplyRetrieve

**Repository / product**

- Repository: [https://github.com/rcgai/simplyretrieve](https://github.com/rcgai/simplyretrieve)
- Company: Unknown — not stated in the repository
- Product: SimplyRetrieve: A Private and Lightweight Retrieval-Centric Generative AI Tool
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=2, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| supporting: category_count=2 \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 20/100 (a score, not a probability)
- Raw weighted score: 1.00 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 2 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Pipeline complexity: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `Unstructured`, run `run_2`, window `size:2001..4000`, rank 8
  - Query: `"unstructured" filename:requirements.txt size:2001..4000`
  - Sampled 30 of 1,912 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,912 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_2`, window `size:2001..4000`, rank 6
  - Query: `"python-docx" filename:requirements.txt size:2001..4000`
  - Sampled 30 of 6,224 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 6,224 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/RCGAI/SimplyRetrieve/blob/main/requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [requirements.txt](https://github.com/RCGAI/SimplyRetrieve/blob/main/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/RCGAI/SimplyRetrieve) (source: github_api): stars=218, fork=False, archived=False
- [manifest_line](https://github.com/RCGAI/SimplyRetrieve/blob/main/requirements.txt) (source: github_api): unstructured==0.9.0
- [manifest_line](https://github.com/RCGAI/SimplyRetrieve/blob/main/requirements.txt) (source: github_api): python-docx==0.8.11
- [readme_excerpt](https://github.com/RCGAI/SimplyRetrieve/blob/main/README.md) (source: readme): *SimplyRetrieve* is an open-source tool with the goal of providing a fully localized, lightweight and user-friendly GUI and API platform for *Retrieval-Centric Generation* (RCG) approach to the machin

### 100. convertigo/convertigo

**Repository / product**

- Repository: [https://github.com/convertigo/convertigo](https://github.com/convertigo/convertigo)
- Company: Unknown — not stated in the repository
- Product: Convertigo AI Driven Low Code & No Code business apps
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.convertigo.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 19/100 (a score, not a probability)
- Raw weighted score: 0.95 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `Apache PDFBox`, run `run_2`, window `size:>16000`, rank 18
  - Query: `"pdfbox" filename:build.gradle size:>16000`
  - Retrieved 30 of 228 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/convertigo/convertigo/blob/c092481118811554575d2d8f2a59650a3c3ca226/engine/src/com/twinsoft/convertigo/beans/steps/PdfFormStep.java)
- `Apache PDFBox` (pdf, generation) — manifest_declaration — [engine/build.gradle](https://github.com/convertigo/convertigo/blob/c092481118811554575d2d8f2a59650a3c3ca226/engine/build.gradle)

**Evidence trail**

- [api_response](https://github.com/convertigo/convertigo) (source: github_api): stars=383, fork=False, archived=False
- [code_permalink](https://github.com/convertigo/convertigo/blob/c092481118811554575d2d8f2a59650a3c3ca226/engine/src/com/twinsoft/convertigo/beans/steps/PdfFormStep.java) (source: github_api): import org.apache.pdfbox.Loader; import org.apache.pdfbox.cos.COSArray; import org.apache.pdfbox.cos.COSDictionary;
- [manifest_line](https://github.com/convertigo/convertigo/blob/c092481118811554575d2d8f2a59650a3c3ca226/engine/build.gradle) (source: github_api): compileFlat    'org.apache.commons:commons-lang3:' + commonsLang3 compileFlat    'org.apache.httpcomponents:httpclient:4.5.14' compileFlat    'org.apache.james:apache-mime4j-core:0.8.14' compileFl
- [readme_excerpt](https://github.com/convertigo/convertigo/blob/develop/README.md) (source: readme): The platform is currently used by more than 150K developers worldwide, building enterprise class web and mobile apps.

### 101. iiitdwd-exams/certificates

**Repository / product**

- Repository: [https://github.com/iiitdwd-exams/certificates](https://github.com/iiitdwd-exams/certificates)
- Company: Unknown — not stated in the repository
- Product: `certificates`
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 19/100 (a score, not a probability)
- Raw weighted score: 0.95 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 2 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docx-mailmerge / docxedit`, run `run_1`, window `unsliced`, rank 10
  - Query: `"docx-mailmerge" filename:pyproject.toml`
  - Retrieved 12 of 12 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `pikepdf`, run `run_1`, window `size:251..500`, rank 30
  - Query: `"pikepdf" filename:pyproject.toml size:251..500`
  - Retrieved 30 of 66 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docx-mailmerge / docxedit`, run `run_2`, window `unsliced`, rank 10
  - Query: `"docx-mailmerge" filename:pyproject.toml`
  - Retrieved 12 of 12 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docx-mailmerge / docxedit` (other_processing, generation) — manifest_declaration — [pyproject.toml](https://github.com/iiitdwd-exams/certificates/blob/main/pyproject.toml)
- `pikepdf` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/iiitdwd-exams/certificates/blob/main/pyproject.toml)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/iiitdwd-exams/certificates/blob/bd27043eb1edcaa686e0cde90cba4bc4acb0722a/qr_gen.py)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/iiitdwd-exams/certificates/blob/bd27043eb1edcaa686e0cde90cba4bc4acb0722a/gencert.py)

**Evidence trail**

- [api_response](https://github.com/iiitdwd-exams/certificates) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/iiitdwd-exams/certificates/blob/main/pyproject.toml) (source: github_api): "docx-mailmerge2>=0.8.3",
- [manifest_line](https://github.com/iiitdwd-exams/certificates/blob/main/pyproject.toml) (source: github_api): "pikepdf>=9.3.0",
- [code_permalink](https://github.com/iiitdwd-exams/certificates/blob/bd27043eb1edcaa686e0cde90cba4bc4acb0722a/qr_gen.py) (source: github_api): import segno from PIL import Image from pathlib import Path from pikepdf import Pdf, Page, Rectangle # from certutils import str2path, qr_string
- [code_permalink](https://github.com/iiitdwd-exams/certificates/blob/bd27043eb1edcaa686e0cde90cba4bc4acb0722a/gencert.py) (source: github_api): from mailmerge import MailMerge import qr_gen from pikepdf import Pdf, Encryption, Permissions if sys.platform == "win32":     libre_office_path = "c:/Program Files/LibreOffice/program/soffice.exe"

### 102. Mihir-Rabari/inboxfm-connect

**Repository / product**

- Repository: [https://github.com/mihir-rabari/inboxfm-connect](https://github.com/mihir-rabari/inboxfm-connect)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 19/100 (a score, not a probability)
- Raw weighted score: 0.95 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 23
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 23
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/Mihir-Rabari/inboxfm-connect/blob/ff0599cf95d3853f98475a79e0940076e1305f66/packages/integrations/community/carbone/src/index.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/Mihir-Rabari/inboxfm-connect/blob/ff0599cf95d3853f98475a79e0940076e1305f66/packages/integrations/community/carbone/src/lib/auth.ts)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [packages/integrations/community/carbone/package.json](https://github.com/Mihir-Rabari/inboxfm-connect/blob/ff0599cf95d3853f98475a79e0940076e1305f66/packages/integrations/community/carbone/package.json)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/Mihir-Rabari/inboxfm-connect/blob/ff0599cf95d3853f98475a79e0940076e1305f66/packages/integrations/community/carbone/src/lib/common/props.ts)

**Evidence trail**

- [api_response](https://github.com/Mihir-Rabari/inboxfm-connect) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/Mihir-Rabari/inboxfm-connect/blob/ff0599cf95d3853f98475a79e0940076e1305f66/packages/integrations/community/carbone/src/index.ts) (source: github_api): import { carboneAuth } from './lib/auth'; import { CARBONE_API_URL } from './lib/common/constants';
- [code_permalink](https://github.com/Mihir-Rabari/inboxfm-connect/blob/ff0599cf95d3853f98475a79e0940076e1305f66/packages/integrations/community/carbone/src/lib/auth.ts) (source: github_api): import { PieceAuth } from '@inboxfm-connect/pieces-framework'; import { HttpMethod, httpClient } from '@inboxfm-connect/pieces-common'; import { CARBONE_API_URL, CARBONE_VERSION } from './common/const
- [manifest_line](https://github.com/Mihir-Rabari/inboxfm-connect/blob/ff0599cf95d3853f98475a79e0940076e1305f66/packages/integrations/community/carbone/package.json) (source: github_api): {   "name": "@inboxfm-connect/piece-carbone",   "version": "0.0.4",   "type": "commonjs",   "main": "./dist/src/index.js",   "types": "./dist/src/index.d.ts",   "dependencies": {
- [code_permalink](https://github.com/Mihir-Rabari/inboxfm-connect/blob/ff0599cf95d3853f98475a79e0940076e1305f66/packages/integrations/community/carbone/src/lib/common/props.ts) (source: github_api): import { Property } from '@inboxfm-connect/pieces-framework'; import { HttpMethod, httpClient } from '@inboxfm-connect/pieces-common'; import { carboneAuth } from '../auth'; import { CARBONE_API_URL,
- [readme_excerpt](https://github.com/Mihir-Rabari/inboxfm-connect/blob/main/README.md) (source: readme): Whether self-hosted or deployed in the cloud, Inboxfm Connect connects LLM models (via Claude Desktop, Cursor, Windsurf, or custom AI agents) to over **400+ integrations** safely and deterministically

### 103. datawizz/Openpieces

**Repository / product**

- Repository: [https://github.com/datawizz/openpieces](https://github.com/datawizz/openpieces)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; confirmed generation/conversion code

**Score**

- Score: 19/100 (a score, not a probability)
- Raw weighted score: 0.95 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 18
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 18
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/datawizz/Openpieces/blob/1d7f1e696159e725a1fed0c914abb444eddec14d/packages/pieces/community/carbone/src/index.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/datawizz/Openpieces/blob/1d7f1e696159e725a1fed0c914abb444eddec14d/packages/pieces/community/carbone/src/lib/auth.ts)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [packages/pieces/community/carbone/package.json](https://github.com/datawizz/Openpieces/blob/1d7f1e696159e725a1fed0c914abb444eddec14d/packages/pieces/community/carbone/package.json)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/datawizz/Openpieces/blob/1d7f1e696159e725a1fed0c914abb444eddec14d/packages/pieces/community/carbone/src/lib/common/props.ts)

**Evidence trail**

- [api_response](https://github.com/datawizz/Openpieces) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/datawizz/Openpieces/blob/1d7f1e696159e725a1fed0c914abb444eddec14d/packages/pieces/community/carbone/src/index.ts) (source: github_api): import { carboneAuth } from './lib/auth'; import { CARBONE_API_URL } from './lib/common/constants';
- [code_permalink](https://github.com/datawizz/Openpieces/blob/1d7f1e696159e725a1fed0c914abb444eddec14d/packages/pieces/community/carbone/src/lib/auth.ts) (source: github_api): import { PieceAuth } from '@openpieces/pieces-framework'; import { HttpMethod, httpClient } from '@openpieces/pieces-common'; import { CARBONE_API_URL, CARBONE_VERSION } from './common/constants'; ex
- [manifest_line](https://github.com/datawizz/Openpieces/blob/1d7f1e696159e725a1fed0c914abb444eddec14d/packages/pieces/community/carbone/package.json) (source: github_api): {   "name": "@openpieces/piece-carbone",   "version": "0.0.2",   "main": "./dist/src/index.js",   "types": "./dist/src/index.d.ts",   "dependencies": {     "form-data": "catalog:",
- [code_permalink](https://github.com/datawizz/Openpieces/blob/1d7f1e696159e725a1fed0c914abb444eddec14d/packages/pieces/community/carbone/src/lib/common/props.ts) (source: github_api): import { Property } from '@openpieces/pieces-framework'; import { HttpMethod, httpClient } from '@openpieces/pieces-common'; import { carboneAuth } from '../auth'; import { CARBONE_API_URL, CARBONE_VE
- [readme_excerpt](https://github.com/datawizz/Openpieces/blob/main/README.md) (source: readme): Self-hosted and network-gapped for maximum security and control over your data.

### 104. zgsm-ai/costrict

**Repository / product**

- Repository: [https://github.com/zgsm-ai/costrict](https://github.com/zgsm-ai/costrict)
- Company: Sangfor
- Product: Unknown
- Industry: proposal_sales (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://costrict.ai

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2 \| unknown: contributor_count not collected

**Score**

- Score: 18/100 (a score, not a probability)
- Raw weighted score: 0.90 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 2 |
| Business criticality | 1 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:>16000`, rank 6
  - Query: `"mammoth" filename:package.json size:>16000`
  - Retrieved 30 of 283 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_2`, window `size:>16000`, rank 10
  - Query: `"puppeteer" filename:package.json size:>16000`
  - Retrieved 30 of 856 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [src/package.json](https://github.com/zgsm-ai/costrict/blob/main/src/package.json)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [src/package.json](https://github.com/zgsm-ai/costrict/blob/main/src/package.json)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/zgsm-ai/costrict/blob/9fc86b5c62fa4021b87541bc522ade865eeeea0f/src/integrations/misc/extract-text.ts)

**Evidence trail**

- [api_response](https://github.com/zgsm-ai/costrict) (source: github_api): stars=4384, fork=False, archived=False
- [readme_excerpt](https://github.com/zgsm-ai/costrict/blob/main/README.md) (source: readme): company stated as 'Sangfor'
- [manifest_line](https://github.com/zgsm-ai/costrict/blob/main/src/package.json) (source: github_api): "puppeteer-chromium-resolver": "^24.0.0",
- [manifest_line](https://github.com/zgsm-ai/costrict/blob/main/src/package.json) (source: github_api): "mammoth": "^1.9.1",
- [code_permalink](https://github.com/zgsm-ai/costrict/blob/9fc86b5c62fa4021b87541bc522ade865eeeea0f/src/integrations/misc/extract-text.ts) (source: github_api): import * as path from "path" // @ts-ignore-next-line import pdf from "pdf-parse/lib/pdf-parse" import mammoth from "mammoth" import fs from "fs/promises" import { readFileWithEncodingDetection, isBina

### 105. Websoft9/docker-library

**Repository / product**

- Repository: [https://github.com/websoft9/docker-library](https://github.com/websoft9/docker-library)
- Company: Unknown — not stated in the repository
- Product: Awesome Docker Compose Examples
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.websoft9.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 18/100 (a score, not a probability)
- Raw weighted score: 0.90 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 30
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 30
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [apps/paperlessngx/docker-compose.yml](https://github.com/Websoft9/docker-library/blob/main/apps/paperlessngx/docker-compose.yml)

**Evidence trail**

- [api_response](https://github.com/Websoft9/docker-library) (source: github_api): stars=67, fork=False, archived=False
- [other](https://github.com/Websoft9/docker-library/tree/main/template) (source: github_api): directory template/ present
- [api_response](https://github.com/Websoft9/docker-library) (source: github_api): stars=67, fork=False, archived=False
- [code_permalink](https://github.com/Websoft9/docker-library/blob/main/apps/paperlessngx/docker-compose.yml) (source: github_api): services:   broker:     image: redis:7     container_name: $W9_ID-redis     restart: unless-stopped     volumes:       - redisdata:/data   db:     image: postgres:16     container_name: $W9_ID-postgr
- [other](https://github.com/Websoft9/docker-library/tree/main/template) (source: github_api): directory template/ present
- [api_response](https://github.com/Websoft9/docker-library) (source: github_api): stars=67, fork=False, archived=False
- [code_permalink](https://github.com/Websoft9/docker-library/blob/main/apps/paperlessngx/docker-compose.yml) (source: github_api): services:   broker:     image: redis:7     container_name: $W9_ID-redis     restart: unless-stopped     volumes:       - redisdata:/data   db:     image: postgres:16     container_name: $W9_ID-postgr
- [manifest_line](https://github.com/Websoft9/docker-library/blob/main/apps/paperlessngx/docker-compose.yml) (source: github_api): - gotenberg
- [other](https://github.com/Websoft9/docker-library/tree/main/template) (source: github_api): directory template/ present
- [api_response](https://github.com/Websoft9/docker-library) (source: github_api): stars=67, fork=False, archived=False
- [code_permalink](https://github.com/Websoft9/docker-library/blob/main/apps/paperlessngx/docker-compose.yml) (source: github_api): services:   broker:     image: redis:7     container_name: $W9_ID-redis     restart: unless-stopped     volumes:       - redisdata:/data   db:     image: postgres:16     container_name: $W9_ID-postgr
- [manifest_line](https://github.com/Websoft9/docker-library/blob/main/apps/paperlessngx/docker-compose.yml) (source: github_api): - gotenberg
- [other](https://github.com/Websoft9/docker-library/tree/main/template) (source: github_api): directory template/ present

### 106. runtipi/runtipi-appstore

**Repository / product**

- Repository: [https://github.com/runtipi/runtipi-appstore](https://github.com/runtipi/runtipi-appstore)
- Company: Unknown — not stated in the repository
- Product: Runtipi App Store ⛺
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://runtipi.io/docs/apps-available

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 18/100 (a score, not a probability)
- Raw weighted score: 0.90 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 20
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 20
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [apps/paperless-ngx/docker-compose.yml](https://github.com/runtipi/runtipi-appstore/blob/master/apps/paperless-ngx/docker-compose.yml)

**Evidence trail**

- [api_response](https://github.com/runtipi/runtipi-appstore) (source: github_api): stars=489, fork=False, archived=False
- [other](https://github.com/runtipi/runtipi-appstore/tree/master/templates) (source: github_api): directory templates/ present
- [api_response](https://github.com/runtipi/runtipi-appstore) (source: github_api): stars=489, fork=False, archived=False
- [code_permalink](https://github.com/runtipi/runtipi-appstore/blob/master/apps/paperless-ngx/docker-compose.yml) (source: github_api): version: '3.7' services:   paperless-ngx:     container_name: paperless-ngx     image: ghcr.io/paperless-ngx/paperless-ngx:3.0.5     restart: unless-stopped     depends_on:       - db       - broker
- [other](https://github.com/runtipi/runtipi-appstore/tree/master/templates) (source: github_api): directory templates/ present
- [api_response](https://github.com/runtipi/runtipi-appstore) (source: github_api): stars=489, fork=False, archived=False
- [code_permalink](https://github.com/runtipi/runtipi-appstore/blob/master/apps/paperless-ngx/docker-compose.yml) (source: github_api): version: '3.7' services:   paperless-ngx:     container_name: paperless-ngx     image: ghcr.io/paperless-ngx/paperless-ngx:3.0.5     restart: unless-stopped     depends_on:       - db       - broker
- [manifest_line](https://github.com/runtipi/runtipi-appstore/blob/master/apps/paperless-ngx/docker-compose.yml) (source: github_api): PAPERLESS_TIKA_GOTENBERG_ENDPOINT: http://gotenberg:3000
- [other](https://github.com/runtipi/runtipi-appstore/tree/master/templates) (source: github_api): directory templates/ present
- [api_response](https://github.com/runtipi/runtipi-appstore) (source: github_api): stars=489, fork=False, archived=False
- [code_permalink](https://github.com/runtipi/runtipi-appstore/blob/master/apps/paperless-ngx/docker-compose.yml) (source: github_api): version: '3.7' services:   paperless-ngx:     container_name: paperless-ngx     image: ghcr.io/paperless-ngx/paperless-ngx:3.0.5     restart: unless-stopped     depends_on:       - db       - broker
- [manifest_line](https://github.com/runtipi/runtipi-appstore/blob/master/apps/paperless-ngx/docker-compose.yml) (source: github_api): PAPERLESS_TIKA_GOTENBERG_ENDPOINT: http://gotenberg:3000
- [other](https://github.com/runtipi/runtipi-appstore/tree/master/templates) (source: github_api): directory templates/ present

### 107. dendianugerah/reubah

**Repository / product**

- Repository: [https://github.com/dendianugerah/reubah](https://github.com/dendianugerah/reubah)
- Company: Unknown — not stated in the repository
- Product: Reubah - Universal File Converter & Image Processor
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; infrastructure_service_present=true; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 18/100 (a score, not a probability)
- Raw weighted score: 0.90 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 10
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 10
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [code](https://github.com/dendianugerah/reubah/blob/main/Dockerfile)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/dendianugerah/reubah/blob/47aae9d339a6060b271ad205c8e5d6f1599e0eac/internal/processor/document/converter.go)

**Evidence trail**

- [api_response](https://github.com/dendianugerah/reubah) (source: github_api): stars=704, fork=False, archived=False
- [code_permalink](https://github.com/dendianugerah/reubah/blob/main/Dockerfile) (source: github_api): libreoffice \
- [code_permalink](https://github.com/dendianugerah/reubah/blob/47aae9d339a6060b271ad205c8e5d6f1599e0eac/internal/processor/document/converter.go) (source: github_api): // ConvertDocument converts a document from one format to another using LibreOffice func ConvertDocument(input io.Reader, inputFormat, outputFormat string) ([]byte, error) {
- [other](https://github.com/dendianugerah/reubah/tree/main/templates) (source: github_api): directory templates/ present
- [api_response](https://github.com/dendianugerah/reubah) (source: github_api): stars=704, fork=False, archived=False
- [code_permalink](https://github.com/dendianugerah/reubah/blob/main/Dockerfile) (source: github_api): # Build stage FROM golang:1.22-alpine AS builder WORKDIR /app # Install build dependencies RUN apk add --no-cache \     gcc \     g++ \     pkgconfig \     libwebp-dev \     musl-dev \     nodejs \
- [code_permalink](https://github.com/dendianugerah/reubah/blob/main/Dockerfile) (source: github_api): libreoffice \
- [code_permalink](https://github.com/dendianugerah/reubah/blob/main/Dockerfile) (source: github_api): libreoffice \
- [code_permalink](https://github.com/dendianugerah/reubah/blob/47aae9d339a6060b271ad205c8e5d6f1599e0eac/internal/processor/document/converter.go) (source: github_api): // ConvertDocument converts a document from one format to another using LibreOffice func ConvertDocument(input io.Reader, inputFormat, outputFormat string) ([]byte, error) {
- [other](https://github.com/dendianugerah/reubah/tree/main/templates) (source: github_api): directory templates/ present

### 108. bigcapitalhq/bigcapital

**Repository / product**

- Repository: [https://github.com/bigcapitalhq/bigcapital](https://github.com/bigcapitalhq/bigcapital)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://bigcapital.app

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: infrastructure_service_present=true; confirmed generation/conversion code

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 2
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 2
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/bigcapitalhq/bigcapital/blob/develop/docker-compose.yml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/common/config/gotenberg.ts)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/common/config/index.ts)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/libs/chromiumly/Converter.ts)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/libs/chromiumly/Chromiumly.ts)

**Evidence trail**

- [api_response](https://github.com/bigcapitalhq/bigcapital) (source: github_api): stars=3846, fork=False, archived=False
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/develop/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/common/config/gotenberg.ts) (source: github_api): import { registerAs } from '@nestjs/config'; export default registerAs('gotenberg', () => ({   url: process.env.GOTENBERG_URL,   docsUrl: process.env.GOTENBERG_DOCS_URL, }));
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/common/config/index.ts) (source: github_api): import systemDatabase from './system-database'; import tenantDatabase from './tenant-database'; import signup from './signup'; import gotenberg from './gotenberg'; import plaid from './plaid'; import
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/libs/chromiumly/Converter.ts) (source: github_api): export abstract class Converter {   readonly endpoint: string;   constructor(route: ChromiumRoute) {     this.endpoint = `${Chromiumly.GOTENBERG_ENDPOINT}/${Chromiumly.CHROMIUM_PATH}/${Chromiumly.CHR
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/libs/chromiumly/Chromiumly.ts) (source: github_api): import { ChromiumRoute, LibreOfficeRoute, PdfEngineRoute } from './_types'; export class Chromiumly {   public static readonly GOTENBERG_ENDPOINT = process.env.GOTENBERG_URL \|\| '';   public static r
- [readme_excerpt](https://github.com/bigcapitalhq/bigcapital/blob/develop/README.md) (source: readme): To get started with self-hosted with Docker and Docker Compose, take a look at the [Docker guide](https://docs.bigcapital.app/deployment/docker).
- [api_response](https://github.com/bigcapitalhq/bigcapital) (source: github_api): stars=3846, fork=False, archived=False
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/develop/docker-compose.yml) (source: github_api): # WARNING! # This is a development version of THE Bigcapital docker-compose.yml file. # Avoid using this file in your production environment. # We're exposing here sensitive ports and mounting code vo
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/develop/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/develop/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/common/config/gotenberg.ts) (source: github_api): import { registerAs } from '@nestjs/config'; export default registerAs('gotenberg', () => ({   url: process.env.GOTENBERG_URL,   docsUrl: process.env.GOTENBERG_DOCS_URL, }));
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/common/config/index.ts) (source: github_api): import systemDatabase from './system-database'; import tenantDatabase from './tenant-database'; import signup from './signup'; import gotenberg from './gotenberg'; import plaid from './plaid'; import
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/libs/chromiumly/Converter.ts) (source: github_api): export abstract class Converter {   readonly endpoint: string;   constructor(route: ChromiumRoute) {     this.endpoint = `${Chromiumly.GOTENBERG_ENDPOINT}/${Chromiumly.CHROMIUM_PATH}/${Chromiumly.CHR
- [code_permalink](https://github.com/bigcapitalhq/bigcapital/blob/4b5130d1513de613c94d555a234c332e080c1136/packages/server/src/libs/chromiumly/Chromiumly.ts) (source: github_api): import { ChromiumRoute, LibreOfficeRoute, PdfEngineRoute } from './_types'; export class Chromiumly {   public static readonly GOTENBERG_ENDPOINT = process.env.GOTENBERG_URL \|\| '';   public static r
- [readme_excerpt](https://github.com/bigcapitalhq/bigcapital/blob/develop/README.md) (source: readme): To get started with self-hosted with Docker and Docker Compose, take a look at the [Docker guide](https://docs.bigcapital.app/deployment/docker).

### 109. infonl/dimpact-zaakafhandelcomponent

**Repository / product**

- Repository: [https://github.com/infonl/dimpact-zaakafhandelcomponent](https://github.com/infonl/dimpact-zaakafhandelcomponent)
- Company: Atos
- Product: ICATT Zaakafhandelcomponent (ZAC)
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: infrastructure_service_present=true; confirmed generation/conversion code

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 18
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 18
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [code](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/main/docker-compose.yaml)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/73c86a461817154f0b2ba4fe95d1a2c5ce1b7509/src/main/kotlin/nl/info/client/officeconverter/OfficeConverterClient.kt)

**Evidence trail**

- [api_response](https://github.com/infonl/dimpact-zaakafhandelcomponent) (source: github_api): stars=7, fork=False, archived=False
- [readme_excerpt](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/main/README.md) (source: readme): company stated as 'Atos'
- [code_permalink](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/main/docker-compose.yaml) (source: github_api): # Disable Chromium routes since we only use LibreOffice for document conversion.
- [code_permalink](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/73c86a461817154f0b2ba4fe95d1a2c5ce1b7509/src/main/kotlin/nl/info/client/officeconverter/OfficeConverterClient.kt) (source: github_api): import org.eclipse.microprofile.rest.client.inject.RegisterRestClient import org.jboss.resteasy.plugins.providers.multipart.MultipartFormDataOutput @Path("forms/libreoffice/convert") @RegisterRestCli
- [readme_excerpt](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/main/README.md) (source: readme): ZAC was created as an extensible, future-proof solution for managing zaken.
- [api_response](https://github.com/infonl/dimpact-zaakafhandelcomponent) (source: github_api): stars=7, fork=False, archived=False
- [code_permalink](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/main/docker-compose.yaml) (source: github_api): # # SPDX-FileCopyrightText: 2024 INFO.nl # SPDX-License-Identifier: EUPL-1.2+ # services:   keycloak-database:     image: postgres:17.11@sha256:e38411452a464af89e5adadb8d223bf53b898d47d6ef918b2d58c087
- [readme_excerpt](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/main/README.md) (source: readme): company stated as 'Atos'
- [code_permalink](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/main/docker-compose.yaml) (source: github_api): # Disable Chromium routes since we only use LibreOffice for document conversion.
- [code_permalink](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/main/docker-compose.yaml) (source: github_api): # Disable Chromium routes since we only use LibreOffice for document conversion.
- [code_permalink](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/73c86a461817154f0b2ba4fe95d1a2c5ce1b7509/src/main/kotlin/nl/info/client/officeconverter/OfficeConverterClient.kt) (source: github_api): import org.eclipse.microprofile.rest.client.inject.RegisterRestClient import org.jboss.resteasy.plugins.providers.multipart.MultipartFormDataOutput @Path("forms/libreoffice/convert") @RegisterRestCli
- [readme_excerpt](https://github.com/infonl/dimpact-zaakafhandelcomponent/blob/main/README.md) (source: readme): ZAC was created as an extensible, future-proof solution for managing zaken.

### 110. airens/interactive_brokers_tax

**Repository / product**

- Repository: [https://github.com/airens/interactive_brokers_tax](https://github.com/airens/interactive_brokers_tax)
- Company: Unknown — not stated in the repository
- Product: 3-НДФЛ Interactive Brokers
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 9
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 9
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [requirements.txt](https://github.com/airens/interactive_brokers_tax/blob/master/requirements.txt)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/airens/interactive_brokers_tax/blob/cb40816ce3eb80bea39d8ceb8c4875a140cd89ca/ib.py)

**Evidence trail**

- [api_response](https://github.com/airens/interactive_brokers_tax) (source: github_api): stars=101, fork=False, archived=False
- [manifest_line](https://github.com/airens/interactive_brokers_tax/blob/master/requirements.txt) (source: github_api): docxtpl==0.17.0
- [code_permalink](https://github.com/airens/interactive_brokers_tax/blob/cb40816ce3eb80bea39d8ceb8c4875a140cd89ca/ib.py) (source: github_api): from datetime import datetime import requests import yfinance as yf from docxtpl import DocxTemplate from collections import namedtuple from io import BytesIO

### 111. Cinnamon/kotaemon

**Repository / product**

- Repository: [https://github.com/cinnamon/kotaemon](https://github.com/cinnamon/kotaemon)
- Company: Unknown — not stated in the repository
- Product: kotaemon
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://cinnamon.github.io/kotaemon/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: template_directory_present=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Unstructured`, run `run_2`, window `size:2001..4000`, rank 4
  - Query: `"unstructured" filename:pyproject.toml size:2001..4000`
  - Retrieved 30 of 728 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Docling`, run `run_2`, window `size:2001..4000`, rank 4
  - Query: `"docling" filename:pyproject.toml size:2001..4000`
  - Retrieved 30 of 746 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/loaders/docling_loader.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/loaders/__init__.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/loaders/unstructured_loader.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/loaders/__init__.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/indices/ingests/files.py)

**Evidence trail**

- [api_response](https://github.com/Cinnamon/kotaemon) (source: github_api): stars=25713, fork=False, archived=False
- [code_permalink](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/loaders/docling_loader.py) (source: github_api): class DoclingReader(BaseReader):     """Using Docling to extract document structure and content"""
- [code_permalink](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/loaders/__init__.py) (source: github_api): from .azureai_document_intelligence_loader import AzureAIDocumentIntelligenceLoader from .base import AutoReader, BaseReader from .composite_loader import DirectoryReader from .docling_loader import D
- [code_permalink](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/loaders/unstructured_loader.py) (source: github_api): """Unstructured file reader. A parser for unstructured text files using Unstructured.io. Supports .txt, .docx, .pptx, .jpg, .png, .eml, .html, and .pdf documents. To use .doc and .xls parser, instal
- [code_permalink](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/loaders/__init__.py) (source: github_api): from .paddleocr_loader import PaddleOCRVLReader, PPStructureV3Reader from .pdf_loader import PDFThumbnailReader from .txt_loader import TxtReader from .unstructured_loader import UnstructuredReader fr
- [code_permalink](https://github.com/Cinnamon/kotaemon/blob/9ad3e4e49aa35b8acddd235918a5d9753c1cfdf9/libs/kotaemon/kotaemon/indices/ingests/files.py) (source: github_api): web_reader = WebReader() unstructured = UnstructuredReader() adobe_reader = AdobeReader()
- [other](https://github.com/Cinnamon/kotaemon/tree/main/templates) (source: github_api): directory templates/ present

### 112. bbossgroups/bboss

**Repository / product**

- Repository: [https://github.com/bbossgroups/bboss](https://github.com/bbossgroups/bboss)
- Company: Unknown — not stated in the repository
- Product: bboss website:
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://www.bbossgroups.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 5
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 5
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `iText`, run `run_2`, window `size:4001..8000`, rank 8
  - Query: `"itext" filename:build.gradle size:4001..8000`
  - Sampled 30 of 1,060 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,060 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/bbossgroups/bboss/blob/70cdef15354d841d265653f2996f75b1a67e7fff/bboss-mvc/src/org/frameworkset/ui/jasperreports/JasperReportsUtils.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/bbossgroups/bboss/blob/70cdef15354d841d265653f2996f75b1a67e7fff/bboss-mvc/src/org/frameworkset/web/servlet/view/jasperreports/JasperReportsXlsView.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/bbossgroups/bboss/blob/70cdef15354d841d265653f2996f75b1a67e7fff/bboss-mvc/src/org/frameworkset/web/servlet/view/jasperreports/JasperReportsCsvView.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/bbossgroups/bboss/blob/70cdef15354d841d265653f2996f75b1a67e7fff/bboss-mvc/src/org/frameworkset/web/servlet/view/jasperreports/JasperReportsPdfView.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/bbossgroups/bboss/blob/70cdef15354d841d265653f2996f75b1a67e7fff/bboss-mvc/src/org/frameworkset/web/servlet/view/jasperreports/JasperReportsHtmlView.java)

**Evidence trail**

- [api_response](https://github.com/bbossgroups/bboss) (source: github_api): stars=319, fork=False, archived=False
- [code_permalink](https://github.com/bbossgroups/bboss/blob/70cdef15354d841d265653f2996f75b1a67e7fff/bboss-mvc/src/org/frameworkset/ui/jasperreports/JasperReportsUtils.java) (source: github_api): import net.sf.jasperreports.engine.JRDataSource; import net.sf.jasperreports.engine.JRException; import net.sf.jasperreports.engine.JRExporter;
- [code_permalink](https://github.com/bbossgroups/bboss/blob/70cdef15354d841d265653f2996f75b1a67e7fff/bboss-mvc/src/org/frameworkset/web/servlet/view/jasperreports/JasperReportsXlsView.java) (source: github_api): *  limitations under the License.  */ package org.frameworkset.web.servlet.view.jasperreports; import net.sf.jasperreports.engine.JRExporter; import net.sf.jasperreports.engine.export.JRXlsEx
- [code_permalink](https://github.com/bbossgroups/bboss/blob/70cdef15354d841d265653f2996f75b1a67e7fff/bboss-mvc/src/org/frameworkset/web/servlet/view/jasperreports/JasperReportsCsvView.java) (source: github_api): *  limitations under the License.  */ package org.frameworkset.web.servlet.view.jasperreports; import net.sf.jasperreports.engine.JRExporter; import net.sf.jasperreports.engine.export.JRCsvEx
- [code_permalink](https://github.com/bbossgroups/bboss/blob/70cdef15354d841d265653f2996f75b1a67e7fff/bboss-mvc/src/org/frameworkset/web/servlet/view/jasperreports/JasperReportsPdfView.java) (source: github_api): *  limitations under the License.  */ package org.frameworkset.web.servlet.view.jasperreports; import net.sf.jasperreports.engine.JRExporter; import net.sf.jasperreports.engine.export.JRPdfEx
- [code_permalink](https://github.com/bbossgroups/bboss/blob/70cdef15354d841d265653f2996f75b1a67e7fff/bboss-mvc/src/org/frameworkset/web/servlet/view/jasperreports/JasperReportsHtmlView.java) (source: github_api): *  limitations under the License.  */ package org.frameworkset.web.servlet.view.jasperreports; import net.sf.jasperreports.engine.JRExporter; import net.sf.jasperreports.engine.export.JRHtmlE

### 113. miyabayt/spring-boot-doma2-sample

**Repository / product**

- Repository: [https://github.com/miyabayt/spring-boot-doma2-sample](https://github.com/miyabayt/spring-boot-doma2-sample)
- Company: Unknown — not stated in the repository
- Product: Spring Boot Sample Application
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 15
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 15
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/miyabayt/spring-boot-doma2-sample/blob/db0c8315cc493ef8eed5a31e783f8c17ae109353/sample-web-base/src/main/java/com/bigtreetc/sample/web/base/view/PdfView.java)
- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [sample-web-base/build.gradle](https://github.com/miyabayt/spring-boot-doma2-sample/blob/db0c8315cc493ef8eed5a31e783f8c17ae109353/sample-web-base/build.gradle)

**Evidence trail**

- [api_response](https://github.com/miyabayt/spring-boot-doma2-sample) (source: github_api): stars=115, fork=False, archived=False
- [code_permalink](https://github.com/miyabayt/spring-boot-doma2-sample/blob/db0c8315cc493ef8eed5a31e783f8c17ae109353/sample-web-base/src/main/java/com/bigtreetc/sample/web/base/view/PdfView.java) (source: github_api): import java.util.Collection; import java.util.Map; import lombok.val; import net.sf.jasperreports.engine.JRException; import net.sf.jasperreports.engine.JasperCompileManager; import net.sf.jasperrepor
- [manifest_line](https://github.com/miyabayt/spring-boot-doma2-sample/blob/db0c8315cc493ef8eed5a31e783f8c17ae109353/sample-web-base/build.gradle) (source: github_api): api "nz.net.ultraq.thymeleaf:thymeleaf-layout-dialect"     api "com.fasterxml.jackson.dataformat:jackson-dataformat-csv"     api "org.modelmapper:modelmapper:3.2.6"     api "net.sf.jasperreports:j

### 114. dahatake/HypervelocityEngineering

**Repository / product**

- Repository: [https://github.com/dahatake/hypervelocityengineering](https://github.com/dahatake/hypervelocityengineering)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: template_directory_present=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:8001..16000`, rank 21
  - Query: `"mammoth" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 59 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [pyproject.toml](https://github.com/dahatake/HypervelocityEngineering/blob/main/pyproject.toml)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/dahatake/HypervelocityEngineering/blob/71ec5904c28d5bf43b4bc844619c748c34bb77ac/hve/gui/doc_convert.py)

**Evidence trail**

- [api_response](https://github.com/dahatake/HypervelocityEngineering) (source: github_api): stars=3, fork=False, archived=False
- [manifest_line](https://github.com/dahatake/HypervelocityEngineering/blob/main/pyproject.toml) (source: github_api): # 変換エンジンは microsoft/markitdown 単一に統合済み（旧 pypdf/mammoth/markdownify/openpyxl は廃止）。
- [code_permalink](https://github.com/dahatake/HypervelocityEngineering/blob/71ec5904c28d5bf43b4bc844619c748c34bb77ac/hve/gui/doc_convert.py) (source: github_api): 変換エンジン:   - 任意依存対象は microsoft/markitdown (`MarkItDown.convert_local()`) に一本化。   - 旧 pypdf / mammoth / markdownify / openpyxl 経路は撤去済み。 セキュリティ:   - MarkItDown はローカルファイル限定の `convert_local()` のみを呼び出す
- [other](https://github.com/dahatake/HypervelocityEngineering/tree/main/template) (source: github_api): directory template/ present

### 115. FerGusMosca/Quant_ML_Research_Platform

**Repository / product**

- Repository: [https://github.com/fergusmosca/quant_ml_research_platform](https://github.com/fergusmosca/quant_ml_research_platform)
- Company: Unknown — not stated in the repository
- Product: AlgoTrading_Neural_Networks
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: template_directory_present=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Docling`, run `run_2`, window `size:2001..4000`, rank 14
  - Query: `"docling" filename:requirements.txt size:2001..4000`
  - Retrieved 30 of 494 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Docling` (other_processing, extraction) — manifest_declaration — [temp_requirements.txt](https://github.com/FerGusMosca/Quant_ML_Research_Platform/blob/master/temp_requirements.txt)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/FerGusMosca/Quant_ML_Research_Platform/blob/278a9146297b05548389ba7e0907a739d7be7023/logic_layer/rag_corpus_metadata/corpus_metadata_pipeline.py)

**Evidence trail**

- [api_response](https://github.com/FerGusMosca/Quant_ML_Research_Platform) (source: github_api): stars=1, fork=False, archived=False
- [manifest_line](https://github.com/FerGusMosca/Quant_ML_Research_Platform/blob/master/temp_requirements.txt) (source: github_api): docling==2.66.0
- [code_permalink](https://github.com/FerGusMosca/Quant_ML_Research_Platform/blob/278a9146297b05548389ba7e0907a739d7be7023/logic_layer/rag_corpus_metadata/corpus_metadata_pipeline.py) (source: github_api): import os #from docling.document_converter import DocumentConverter from tqdm import tqdm from data_access_layer.qdrant.qdrant_manager import QdrantManager from framework.common.logger.message_type
- [other](https://github.com/FerGusMosca/Quant_ML_Research_Platform/tree/master/templates) (source: github_api): directory templates/ present

### 116. healthonrails/annolid

**Repository / product**

- Repository: [https://github.com/healthonrails/annolid](https://github.com/healthonrails/annolid)
- Company: Unknown — not stated in the repository
- Product: Annolid
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:8001..16000`, rank 24
  - Query: `"PyMuPDF" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 334 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [pyproject.toml](https://github.com/healthonrails/annolid/blob/main/pyproject.toml)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/healthonrails/annolid/blob/9c3e04efbe8268b326aa66a09c12c82df5569d14/annolid/gui/widgets/pdf_import_widget.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/healthonrails/annolid/blob/9c3e04efbe8268b326aa66a09c12c82df5569d14/annolid/io/vector/document_import.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/healthonrails/annolid/blob/9c3e04efbe8268b326aa66a09c12c82df5569d14/annolid/core/agent/tools/pdf.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/healthonrails/annolid/blob/9c3e04efbe8268b326aa66a09c12c82df5569d14/annolid/gui/widgets/pdf_manager.py)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/healthonrails/annolid/blob/9c3e04efbe8268b326aa66a09c12c82df5569d14/annolid/gui/widgets/pdf_viewer_impl.py)

**Evidence trail**

- [api_response](https://github.com/healthonrails/annolid) (source: github_api): stars=58, fork=False, archived=False
- [manifest_line](https://github.com/healthonrails/annolid/blob/main/pyproject.toml) (source: github_api): "pymupdf",
- [code_permalink](https://github.com/healthonrails/annolid/blob/9c3e04efbe8268b326aa66a09c12c82df5569d14/annolid/gui/widgets/pdf_import_widget.py) (source: github_api): except ImportError:             QtWidgets.QMessageBox.critical(                 window,                 window.tr("PyMuPDF Required"),                 window.tr(                     "PyMuPDF (
- [code_permalink](https://github.com/healthonrails/annolid/blob/9c3e04efbe8268b326aa66a09c12c82df5569d14/annolid/io/vector/document_import.py) (source: github_api): def _pdf_like_to_svg_and_labels_with_pymupdf(     path: Path,
- [code_permalink](https://github.com/healthonrails/annolid/blob/9c3e04efbe8268b326aa66a09c12c82df5569d14/annolid/core/agent/tools/pdf.py) (source: github_api): if start_index >= total_pages:                     return "", 0, total_pages, "pymupdf"                 end_index = min(total_pages, start_index + pages_limit)
- [code_permalink](https://github.com/healthonrails/annolid/blob/9c3e04efbe8268b326aa66a09c12c82df5569d14/annolid/gui/widgets/pdf_manager.py) (source: github_api): try:             import fitz  # type: ignore         except Exception:             return {"ok": False, "error": "PyMuPDF (pymupdf) is required."}         path = Path(path_text)         if not
- [code_permalink](https://github.com/healthonrails/annolid/blob/9c3e04efbe8268b326aa66a09c12c82df5569d14/annolid/gui/widgets/pdf_viewer_impl.py) (source: github_api): self._clear_bookmarks()                     self._open_with_pymupdf(path, source_path=source_path)                     self._web_loading_path = None
- [readme_excerpt](https://github.com/healthonrails/annolid/blob/main/README.md) (source: readme): Annolid is designed for real lab data, including overlap, occlusion, variable lighting, long videos, and projects where saved annotations need to remain readable and reproducible.

### 117. codion-is/codion

**Repository / product**

- Repository: [https://github.com/codion-is/codion](https://github.com/codion-is/codion)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://codion.is

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 14
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 14
  - Query: `"jasperreports" filename:build.gradle`
  - Retrieved 30 of 641 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [build.gradle.kts](https://github.com/codion-is/codion/blob/main/build.gradle.kts)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/codion-is/codion/blob/c461bd4c7e6a6bb225ee32fbfdc4df77cef51a3f/plugins/jasperreports/src/main/java/is/codion/plugin/jasperreports/JasperReports.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/codion-is/codion/blob/c461bd4c7e6a6bb225ee32fbfdc4df77cef51a3f/demos/manual/src/main/java/is/codion/manual/plugin/jasperreports/JasperReportsDemo.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/codion-is/codion/blob/c461bd4c7e6a6bb225ee32fbfdc4df77cef51a3f/plugins/jasperreports/src/main/java/is/codion/plugin/jasperreports/JRExport.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/codion-is/codion/blob/c461bd4c7e6a6bb225ee32fbfdc4df77cef51a3f/plugins/jasperreports/src/main/java/is/codion/plugin/jasperreports/JRReport.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/codion-is/codion/blob/c461bd4c7e6a6bb225ee32fbfdc4df77cef51a3f/demos/manual/src/main/java/is/codion/manual/plugin/jasperreports/package-info.java)

**Evidence trail**

- [api_response](https://github.com/codion-is/codion) (source: github_api): stars=4, fork=False, archived=False
- [manifest_line](https://github.com/codion-is/codion/blob/main/build.gradle.kts) (source: github_api): id("io.github.f-cramer.jasperreports") version "0.0.4"
- [code_permalink](https://github.com/codion-is/codion/blob/c461bd4c7e6a6bb225ee32fbfdc4df77cef51a3f/plugins/jasperreports/src/main/java/is/codion/plugin/jasperreports/JasperReports.java) (source: github_api): */ public final class JasperReports {
- [code_permalink](https://github.com/codion-is/codion/blob/c461bd4c7e6a6bb225ee32fbfdc4df77cef51a3f/demos/manual/src/main/java/is/codion/manual/plugin/jasperreports/JasperReportsDemo.java) (source: github_api): public final class JasperReportsDemo { static void jasperReports() { EntityConnection connection = EntityConnection.builder() .domain(Store.DOMAIN)
- [code_permalink](https://github.com/codion-is/codion/blob/c461bd4c7e6a6bb225ee32fbfdc4df77cef51a3f/plugins/jasperreports/src/main/java/is/codion/plugin/jasperreports/JRExport.java) (source: github_api): import net.sf.jasperreports.engine.JRException; import net.sf.jasperreports.engine.JasperExportManager;
- [code_permalink](https://github.com/codion-is/codion/blob/c461bd4c7e6a6bb225ee32fbfdc4df77cef51a3f/plugins/jasperreports/src/main/java/is/codion/plugin/jasperreports/JRReport.java) (source: github_api): */ package is.codion.plugin.jasperreports;
- [code_permalink](https://github.com/codion-is/codion/blob/c461bd4c7e6a6bb225ee32fbfdc4df77cef51a3f/demos/manual/src/main/java/is/codion/manual/plugin/jasperreports/package-info.java) (source: github_api): *  * Copyright (c) 2026, Björn Darri Sigurðsson.  */ /**  * Snippets for {@link is.codion.plugin.jasperreports}, included by manual/framework-reports.adoc.  */ package is.codion.manual.plugin.jasperr

### 118. wocommunity/wonder

**Repository / product**

- Repository: [https://github.com/wocommunity/wonder](https://github.com/wocommunity/wonder)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://wiki.wocommunity.org/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 6
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 6
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Apache POI (XWPF/HWPF)`, run `run_2`, window `size:>16000`, rank 11
  - Query: `"poi" filename:pom.xml size:>16000`
  - Sampled 30 of 15,200 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 15,200 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/wocommunity/wonder/blob/master/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/wocommunity/wonder/blob/0795aab7163528923ea41453c22ac68845f94175/Frameworks/Reporting/ERJasperReports/Sources/er/jasperreports/ERJRUtilities.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/wocommunity/wonder/blob/0795aab7163528923ea41453c22ac68845f94175/Frameworks/Reporting/ERJasperReports/Sources/er/jasperreports/ERJRFoundationDataSource.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/wocommunity/wonder/blob/0795aab7163528923ea41453c22ac68845f94175/Frameworks/Reporting/ERJasperReports/Sources/er/jasperreports/ERJRReportTaskFromEO.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/wocommunity/wonder/blob/0795aab7163528923ea41453c22ac68845f94175/Frameworks/Reporting/ERJasperReports/Sources/er/jasperreports/ERJRFetchSpecificationReportTask.java)

**Evidence trail**

- [api_response](https://github.com/wocommunity/wonder) (source: github_api): stars=255, fork=False, archived=False
- [manifest_line](https://github.com/wocommunity/wonder/blob/master/pom.xml) (source: github_api): <groupId>org.apache.xmlgraphics</groupId>
- [code_permalink](https://github.com/wocommunity/wonder/blob/0795aab7163528923ea41453c22ac68845f94175/Frameworks/Reporting/ERJasperReports/Sources/er/jasperreports/ERJRUtilities.java) (source: github_api): package er.jasperreports; import java.io.File;
- [code_permalink](https://github.com/wocommunity/wonder/blob/0795aab7163528923ea41453c22ac68845f94175/Frameworks/Reporting/ERJasperReports/Sources/er/jasperreports/ERJRFoundationDataSource.java) (source: github_api): package er.jasperreports; import java.util.Enumeration;
- [code_permalink](https://github.com/wocommunity/wonder/blob/0795aab7163528923ea41453c22ac68845f94175/Frameworks/Reporting/ERJasperReports/Sources/er/jasperreports/ERJRReportTaskFromEO.java) (source: github_api): package er.jasperreports; import java.io.File; import java.util.HashMap; import java.util.Map; import java.util.concurrent.Callable;
- [code_permalink](https://github.com/wocommunity/wonder/blob/0795aab7163528923ea41453c22ac68845f94175/Frameworks/Reporting/ERJasperReports/Sources/er/jasperreports/ERJRFetchSpecificationReportTask.java) (source: github_api): package er.jasperreports; import java.io.File;

### 119. BearMelon/thomaslo

**Repository / product**

- Repository: [https://github.com/bearmelon/thomaslo](https://github.com/bearmelon/thomaslo)
- Company: Unknown — not stated in the repository
- Product: ALDashboard: a docassemble Admin and Configuration Tool
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 4
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 4
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [pyproject.toml](https://github.com/BearMelon/thomaslo/blob/main/pyproject.toml)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/BearMelon/thomaslo/blob/a8e52b3434f554a9dc96ce9f13047d154f7bda75/docassemble/ALDashboard/validate_docx.py)

**Evidence trail**

- [api_response](https://github.com/BearMelon/thomaslo) (source: github_api): stars=223, fork=False, archived=False
- [manifest_line](https://github.com/BearMelon/thomaslo/blob/main/pyproject.toml) (source: github_api): module ="docxtpl.*"
- [code_permalink](https://github.com/BearMelon/thomaslo/blob/a8e52b3434f554a9dc96ce9f13047d154f7bda75/docassemble/ALDashboard/validate_docx.py) (source: github_api): from typing import Callable, Optional from jinja2 import Undefined, DebugUndefined, ChainableUndefined from jinja2.utils import missing from docxtpl import DocxTemplate from jinja2 import Environment,

### 120. basxsoftwareassociation/bread

**Repository / product**

- Repository: [https://github.com/basxsoftwareassociation/bread](https://github.com/basxsoftwareassociation/bread)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 11
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 11
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [pyproject.toml](https://github.com/basxsoftwareassociation/bread/blob/main/pyproject.toml)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/basxsoftwareassociation/bread/blob/53f58e20062cd5e40998cf32e9c9e6790063aba2/basxbread/contrib/document_templates/models.py)

**Evidence trail**

- [api_response](https://github.com/basxsoftwareassociation/bread) (source: github_api): stars=19, fork=False, archived=False
- [manifest_line](https://github.com/basxsoftwareassociation/bread/blob/main/pyproject.toml) (source: github_api): all = ["docxtpl", "pymupdf", "hypothesis[django]", "django_dynamic_fixture", "defusedxml"]
- [code_permalink](https://github.com/basxsoftwareassociation/bread/blob/53f58e20062cd5e40998cf32e9c9e6790063aba2/basxbread/contrib/document_templates/models.py) (source: github_api): from django.utils.translation import gettext_lazy as _ from docxtpl import DocxTemplate from jinja2.sandbox import SandboxedEnvironment

### 121. elapouya/python-docx-template

**Repository / product**

- Repository: [https://github.com/elapouya/python-docx-template](https://github.com/elapouya/python-docx-template)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 1
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 1
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [pyproject.toml](https://github.com/elapouya/python-docx-template/blob/master/pyproject.toml)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/elapouya/python-docx-template/blob/1f143fbe86c19ecb28c3205d5f4b1547c7e2d7ad/docxtpl/__main__.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/elapouya/python-docx-template/blob/1f143fbe86c19ecb28c3205d5f4b1547c7e2d7ad/docxtpl/template.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/elapouya/python-docx-template/blob/1f143fbe86c19ecb28c3205d5f4b1547c7e2d7ad/setup.py)

**Evidence trail**

- [api_response](https://github.com/elapouya/python-docx-template) (source: github_api): stars=2695, fork=False, archived=False
- [manifest_line](https://github.com/elapouya/python-docx-template/blob/master/pyproject.toml) (source: github_api): name = "docxtpl"
- [code_permalink](https://github.com/elapouya/python-docx-template/blob/1f143fbe86c19ecb28c3205d5f4b1547c7e2d7ad/docxtpl/__main__.py) (source: github_api): def make_arg_parser():     parser = argparse.ArgumentParser(         usage="python -m docxtpl [-h] [-o] [-q] {} {} {}".format(             TEMPLATE_ARG, JSON_ARG, OUTPUT_ARG         ),         descri
- [code_permalink](https://github.com/elapouya/python-docx-template/blob/1f143fbe86c19ecb28c3205d5f4b1547c7e2d7ad/docxtpl/template.py) (source: github_api): docx_file.seek(0)             else:                 tmp_file = "%s_docxtpl_before_replace_medias" % docx_file                 os.rename(docx_file, tmp_file)             with zipfile.
- [code_permalink](https://github.com/elapouya/python-docx-template/blob/1f143fbe86c19ecb28c3205d5f4b1547c7e2d7ad/setup.py) (source: github_api): setup(     name="docxtpl",     version=get_version("docxtpl"),     description="Python docx template engine",     long_description=long_description,

### 122. SuffolkLITLab/docassemble-ALWeaver

**Repository / product**

- Repository: [https://github.com/suffolklitlab/docassemble-alweaver](https://github.com/suffolklitlab/docassemble-alweaver)
- Company: Unknown — not stated in the repository
- Product: Assembly Line Weaver: Suffolk LIT Lab Document Assembly Line
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://apps-dev.suffolklitlab.org/start/ALWeaver/assembly_line/#/1

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 16
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 16
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `pikepdf`, run `run_2`, window `size:2001..4000`, rank 9
  - Query: `"pikepdf" filename:pyproject.toml size:2001..4000`
  - Retrieved 30 of 125 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [pyproject.toml](https://github.com/SuffolkLITLab/docassemble-ALWeaver/blob/main/pyproject.toml)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/SuffolkLITLab/docassemble-ALWeaver/blob/2dfa51df6cd02c3b7149768145c032fb8a42d4c8/docassemble/ALWeaver/validate_template_files.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/SuffolkLITLab/docassemble-ALWeaver/blob/2dfa51df6cd02c3b7149768145c032fb8a42d4c8/docassemble/ALWeaver/interview_generator.py)

**Evidence trail**

- [api_response](https://github.com/SuffolkLITLab/docassemble-ALWeaver) (source: github_api): stars=25, fork=False, archived=False
- [manifest_line](https://github.com/SuffolkLITLab/docassemble-ALWeaver/blob/main/pyproject.toml) (source: github_api): module = "docxtpl"
- [code_permalink](https://github.com/SuffolkLITLab/docassemble-ALWeaver/blob/2dfa51df6cd02c3b7149768145c032fb8a42d4c8/docassemble/ALWeaver/validate_template_files.py) (source: github_api): from pathlib import Path from jinja2 import DebugUndefined from docxtpl import DocxTemplate from docx2python import docx2python import jinja2.exceptions from docassemble.base.util import DAFile
- [code_permalink](https://github.com/SuffolkLITLab/docassemble-ALWeaver/blob/2dfa51df6cd02c3b7149768145c032fb8a42d4c8/docassemble/ALWeaver/interview_generator.py) (source: github_api): return list(dict.fromkeys(fields)) # A Jinja statement tag, with the whole inside captured. docxtpl adds `p`, `r`, # `tr` and `tc` prefixes, and Jinja itself allows `-`/`+` whitespace control on

### 123. OParl/spec

**Repository / product**

- Repository: [https://github.com/oparl/spec](https://github.com/oparl/spec)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://oparl.org

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Pandoc`, run `run_1`, window `unsliced`, rank 17
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `Pandoc`, run `run_2`, window `unsliced`, rank 17
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Pandoc` (conversion, conversion) — infrastructure_reference — [code](https://github.com/OParl/spec/blob/master/Dockerfile)
- `Pandoc` (conversion, conversion) — code_import — [code](https://github.com/OParl/spec/blob/0ca34358433b781faf1e006abdeb3653e4401d95/build.py)

**Evidence trail**

- [api_response](https://github.com/OParl/spec) (source: github_api): stars=64, fork=False, archived=False
- [code_permalink](https://github.com/OParl/spec/blob/master/Dockerfile) (source: github_api): # recommended packages for pandoc + basic pdf export
- [code_permalink](https://github.com/OParl/spec/blob/0ca34358433b781faf1e006abdeb3653e4401d95/build.py) (source: github_api): def get_pandoc_version(pandoc_bin):     version_tuple = subprocess.getoutput('{} --version'.format(pandoc_bin)).split('\n')[0].split(' ')[1].split('.')
- [api_response](https://github.com/OParl/spec) (source: github_api): stars=64, fork=False, archived=False
- [code_permalink](https://github.com/OParl/spec/blob/master/Dockerfile) (source: github_api): # Dockerfile to create a container able to build the OParl Specification # # MIT License # # Copyright (c) 2016, Stefan Graupner # # Permission is hereby granted, free of charge, to any person obtaini
- [code_permalink](https://github.com/OParl/spec/blob/master/Dockerfile) (source: github_api): # recommended packages for pandoc + basic pdf export
- [code_permalink](https://github.com/OParl/spec/blob/master/Dockerfile) (source: github_api): # recommended packages for pandoc + basic pdf export
- [code_permalink](https://github.com/OParl/spec/blob/0ca34358433b781faf1e006abdeb3653e4401d95/build.py) (source: github_api): def get_pandoc_version(pandoc_bin):     version_tuple = subprocess.getoutput('{} --version'.format(pandoc_bin)).split('\n')[0].split(' ')[1].split('.')

### 124. GUMGA/frameworkbackend

**Repository / product**

- Repository: [https://github.com/gumga/frameworkbackend](https://github.com/gumga/frameworkbackend)
- Company: Unknown — not stated in the repository
- Product: GUMGA FRAMEWORK BACKEND
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 12
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 12
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/GUMGA/frameworkbackend/blob/master/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/GUMGA/frameworkbackend/blob/57708606a8b2592ae1c3b8dec7b52445661cf1b9/gumga-application/src/main/java/io/gumga/application/service/JasperReportService.java)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/GUMGA/frameworkbackend/blob/57708606a8b2592ae1c3b8dec7b52445661cf1b9/gumga-presentation/src/main/java/io/gumga/presentation/api/AbstractReportAPI.java)

**Evidence trail**

- [api_response](https://github.com/GUMGA/frameworkbackend) (source: github_api): stars=5, fork=False, archived=False
- [manifest_line](https://github.com/GUMGA/frameworkbackend/blob/master/pom.xml) (source: github_api): <groupId>net.sf.jasperreports</groupId>
- [code_permalink](https://github.com/GUMGA/frameworkbackend/blob/57708606a8b2592ae1c3b8dec7b52445661cf1b9/gumga-application/src/main/java/io/gumga/application/service/JasperReportService.java) (source: github_api): */ package io.gumga.application.service; import net.sf.jasperreports.engine.*; import net.sf.jasperreports.engine.data.JRBeanCollectionDataSource; import net.sf.jasperreports.engine.util.JRLoader; i
- [code_permalink](https://github.com/GUMGA/frameworkbackend/blob/57708606a8b2592ae1c3b8dec7b52445661cf1b9/gumga-presentation/src/main/java/io/gumga/presentation/api/AbstractReportAPI.java) (source: github_api): import io.gumga.application.service.JasperReportService; import io.gumga.application.service.ReportType; import net.sf.jasperreports.engine.JRException; import org.springframework.beans.factory.annot

### 125. Swiss-Armed-Forces/Loom

**Repository / product**

- Repository: [https://github.com/swiss-armed-forces/loom](https://github.com/swiss-armed-forces/loom)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://gitlab.com/swiss-armed-forces/cyber-command/cea/loom

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 16
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 16
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [gotenberg/Dockerfile](https://github.com/Swiss-Armed-Forces/Loom/blob/main/gotenberg/Dockerfile)

**Evidence trail**

- [api_response](https://github.com/Swiss-Armed-Forces/Loom) (source: github_api): stars=18, fork=False, archived=False
- [readme_excerpt](https://github.com/Swiss-Armed-Forces/Loom/blob/main/README.md) (source: readme): **Loom** is an open-source document analysis platform that lets you import documents, search, analyze, and export them from a single deployment.
- [api_response](https://github.com/Swiss-Armed-Forces/Loom) (source: github_api): stars=18, fork=False, archived=False
- [code_permalink](https://github.com/Swiss-Armed-Forces/Loom/blob/main/gotenberg/Dockerfile) (source: github_api): # Image version ARG GOTENBERG_IMAGE_VERSION="8.32.0" ARG DOCKER_REGISTRY="docker.io" FROM ${DOCKER_REGISTRY}/gotenberg/gotenberg:${GOTENBERG_IMAGE_VERSION} USER root # Install Fonts # see: https://
- [readme_excerpt](https://github.com/Swiss-Armed-Forces/Loom/blob/main/README.md) (source: readme): **Loom** is an open-source document analysis platform that lets you import documents, search, analyze, and export them from a single deployment.
- [api_response](https://github.com/Swiss-Armed-Forces/Loom) (source: github_api): stars=18, fork=False, archived=False
- [code_permalink](https://github.com/Swiss-Armed-Forces/Loom/blob/main/gotenberg/Dockerfile) (source: github_api): # Image version ARG GOTENBERG_IMAGE_VERSION="8.32.0" ARG DOCKER_REGISTRY="docker.io" FROM ${DOCKER_REGISTRY}/gotenberg/gotenberg:${GOTENBERG_IMAGE_VERSION} USER root # Install Fonts # see: https://
- [manifest_line](https://github.com/Swiss-Armed-Forces/Loom/blob/main/gotenberg/Dockerfile) (source: github_api): ARG GOTENBERG_IMAGE_VERSION="8.32.0"
- [readme_excerpt](https://github.com/Swiss-Armed-Forces/Loom/blob/main/README.md) (source: readme): **Loom** is an open-source document analysis platform that lets you import documents, search, analyze, and export them from a single deployment.
- [api_response](https://github.com/Swiss-Armed-Forces/Loom) (source: github_api): stars=18, fork=False, archived=False
- [code_permalink](https://github.com/Swiss-Armed-Forces/Loom/blob/main/gotenberg/Dockerfile) (source: github_api): # Image version ARG GOTENBERG_IMAGE_VERSION="8.32.0" ARG DOCKER_REGISTRY="docker.io" FROM ${DOCKER_REGISTRY}/gotenberg/gotenberg:${GOTENBERG_IMAGE_VERSION} USER root # Install Fonts # see: https://
- [manifest_line](https://github.com/Swiss-Armed-Forces/Loom/blob/main/gotenberg/Dockerfile) (source: github_api): ARG GOTENBERG_IMAGE_VERSION="8.32.0"
- [readme_excerpt](https://github.com/Swiss-Armed-Forces/Loom/blob/main/README.md) (source: readme): **Loom** is an open-source document analysis platform that lets you import documents, search, analyze, and export them from a single deployment.

### 126. GUMGA/framework-backend

**Repository / product**

- Repository: [https://github.com/gumga/framework-backend](https://github.com/gumga/framework-backend)
- Company: Unknown — not stated in the repository
- Product: GUMGA FRAMEWORK BACKEND
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 11
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 11
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/GUMGA/framework-backend/blob/master/pom.xml)
- `JasperReports / Apache FOP` (template_generation, generation) — code_import — [code](https://github.com/GUMGA/framework-backend/blob/5fd08b1498e184e65e616211eed58c9a054036ae/gumga-application/src/main/java/gumga/framework/application/service/JasperReportService.java)
- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [gumga-application/pom.xml](https://github.com/GUMGA/framework-backend/blob/5fd08b1498e184e65e616211eed58c9a054036ae/gumga-application/pom.xml)

**Evidence trail**

- [api_response](https://github.com/GUMGA/framework-backend) (source: github_api): stars=5, fork=False, archived=False
- [manifest_line](https://github.com/GUMGA/framework-backend/blob/master/pom.xml) (source: github_api): <groupId>net.sf.jasperreports</groupId>
- [code_permalink](https://github.com/GUMGA/framework-backend/blob/5fd08b1498e184e65e616211eed58c9a054036ae/gumga-application/src/main/java/gumga/framework/application/service/JasperReportService.java) (source: github_api): import java.util.HashMap; import java.util.List; import java.util.Map; import net.sf.jasperreports.engine.JRException; import net.sf.jasperreports.engine.JasperExportManager; import net.sf.jasperrepor
- [manifest_line](https://github.com/GUMGA/framework-backend/blob/5fd08b1498e184e65e616211eed58c9a054036ae/gumga-application/pom.xml) (source: github_api): <artifactId>jackson-databind</artifactId>         </dependency>         <dependency>             <groupId>net.sf.jasperreports</groupId>             <artifactId>jasperreports</artifactId>

### 127. adfinis/document-merge-service

**Repository / product**

- Repository: [https://github.com/adfinis/document-merge-service](https://github.com/adfinis/document-merge-service)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 9
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 9
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [pyproject.toml](https://github.com/adfinis/document-merge-service/blob/main/pyproject.toml)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/adfinis/document-merge-service/blob/d7ed12121f4e92fd81b539e5a2990c3cf57a53dc/document_merge_service/api/apps.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/adfinis/document-merge-service/blob/d7ed12121f4e92fd81b539e5a2990c3cf57a53dc/document_merge_service/api/jinja.py)

**Evidence trail**

- [api_response](https://github.com/adfinis/document-merge-service) (source: github_api): stars=16, fork=False, archived=False
- [manifest_line](https://github.com/adfinis/document-merge-service/blob/main/pyproject.toml) (source: github_api): docxtpl = ">=0.17,<0.21"
- [code_permalink](https://github.com/adfinis/document-merge-service/blob/d7ed12121f4e92fd81b539e5a2990c3cf57a53dc/document_merge_service/api/apps.py) (source: github_api): TextField.register_lookup(IContains, lookup_name="search")         mitigate_docxtpl_corruption_bug()
- [code_permalink](https://github.com/adfinis/document-merge-service/blob/d7ed12121f4e92fd81b539e5a2990c3cf57a53dc/document_merge_service/api/jinja.py) (source: github_api): from docx.shared import Mm from docxtpl import Listing from jinja2 import pass_context

### 128. dkratzert/FinalCif

**Repository / product**

- Repository: [https://github.com/dkratzert/finalcif](https://github.com/dkratzert/finalcif)
- Company: Unknown — not stated in the repository
- Product: FinalCif
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://dkratzert.de/finalcif.html

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 20
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 20
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [pyproject.toml](https://github.com/dkratzert/FinalCif/blob/master/pyproject.toml)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/dkratzert/FinalCif/blob/f43029f35cde23412cba989cb6b696f27733f66c/finalcif/template/xsl/convert.py)
- `docxtpl (python-docx-template)` (template_generation, generation) — code_import — [code](https://github.com/dkratzert/FinalCif/blob/f43029f35cde23412cba989cb6b696f27733f66c/finalcif/report/references.py)

**Evidence trail**

- [api_response](https://github.com/dkratzert/FinalCif) (source: github_api): stars=20, fork=False, archived=False
- [manifest_line](https://github.com/dkratzert/FinalCif/blob/master/pyproject.toml) (source: github_api): "docxtpl[subdoc]>=0.20.2",
- [code_permalink](https://github.com/dkratzert/FinalCif/blob/f43029f35cde23412cba989cb6b696f27733f66c/finalcif/template/xsl/convert.py) (source: github_api): from docxtpl import RichText from lxml import etree from finalcif.app_path import application_path def xml_to_html(xml_string: str \| RichText) -> str:
- [code_permalink](https://github.com/dkratzert/FinalCif/blob/f43029f35cde23412cba989cb6b696f27733f66c/finalcif/report/references.py) (source: github_api): from typing import Union from docx.text.paragraph import Paragraph from docxtpl import RichText from finalcif import VERSION

### 129. fitercanary/fineract-template

**Repository / product**

- Repository: [https://github.com/fitercanary/fineract-template](https://github.com/fitercanary/fineract-template)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| supporting: template_directory_present=true \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 17/100 (a score, not a probability)
- Raw weighted score: 0.85 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Pipeline complexity: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `iText`, run `run_2`, window `size:>16000`, rank 26
  - Query: `"itext" filename:build.gradle size:>16000`
  - Retrieved 30 of 174 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `iText` (pdf, generation) — manifest_declaration — [fineract-provider/build.gradle](https://github.com/fitercanary/fineract-template/blob/a3f5fefb37fdd24b61229f279564a4887c699fbd/fineract-provider/build.gradle)

**Evidence trail**

- [api_response](https://github.com/fitercanary/fineract-template) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/fitercanary/fineract-template/blob/a3f5fefb37fdd24b61229f279564a4887c699fbd/fineract-provider/build.gradle) (source: github_api): exclude module: 'jaxb-api' exclude module: 'jaxb-impl' exclude module: 'jboss-logging' exclude module: 'itext-rtf' exclude module: 'classworlds' exclude module: 'jcl-over-slf4j' exclude
- [other](https://github.com/fitercanary/fineract-template/tree/canary-dev/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/fitercanary/fineract-template/blob/canary-dev/README.md) (source: readme): Apache Fineract: A Platform for Microfinance The next evolution of Apache Fineract focuses on being faster, lighter and cheaper to change (than the existing Mifos) so that it is more responsive to the

### 130. psi-oss/get-physics-done

**Repository / product**

- Repository: [https://github.com/psi-oss/get-physics-done](https://github.com/psi-oss/get-physics-done)
- Company: Physical Superintelligence PBC
- Product: Get Physics Done (GPD)
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.psi.inc

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: industry_category=unknown; contributor_count not collected

**Score**

- Score: 16/100 (a score, not a probability)
- Raw weighted score: 0.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `pypdf / PyPDF2`, run `run_2`, window `size:4001..8000`, rank 4
  - Query: `"pypdf" filename:pyproject.toml size:4001..8000`
  - Sampled 30 of 2,588 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,588 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [pyproject.toml](https://github.com/psi-oss/get-physics-done/blob/main/pyproject.toml)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/psi-oss/get-physics-done/blob/0f417695ccf1f987af44bb4f4b3cbbdeb5f2c48b/src/gpd/core/artifact_text.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/psi-oss/get-physics-done/blob/0f417695ccf1f987af44bb4f4b3cbbdeb5f2c48b/src/gpd/core/workflow_presets.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/psi-oss/get-physics-done/blob/0f417695ccf1f987af44bb4f4b3cbbdeb5f2c48b/src/gpd/core/health.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/psi-oss/get-physics-done/blob/0f417695ccf1f987af44bb4f4b3cbbdeb5f2c48b/src/gpd/mcp/paper/models.py)

**Evidence trail**

- [api_response](https://github.com/psi-oss/get-physics-done) (source: github_api): stars=905, fork=False, archived=False
- [readme_excerpt](https://github.com/psi-oss/get-physics-done/blob/main/README.md) (source: readme): company stated as 'Physical Superintelligence PBC'
- [manifest_line](https://github.com/psi-oss/get-physics-done/blob/main/pyproject.toml) (source: github_api): "pypdf>=5.0",
- [code_permalink](https://github.com/psi-oss/get-physics-done/blob/0f417695ccf1f987af44bb4f4b3cbbdeb5f2c48b/src/gpd/core/artifact_text.py) (source: github_api): return companion if companion.exists() and companion.is_file() else None def _pypdf_available() -> bool:     """Return True when pypdf can be imported."""     try:         import pypdf  # noqa:
- [code_permalink](https://github.com/psi-oss/get-physics-done/blob/0f417695ccf1f987af44bb4f4b3cbbdeb5f2c48b/src/gpd/core/workflow_presets.py) (source: github_api): pdftotext_value = _capability_value(latex_capability, "pdftotext_available", "pdftotext")     # pdf_review_ready may be set explicitly (pypdf-based); otherwise use the     # text-extraction capabi
- [code_permalink](https://github.com/psi-oss/get-physics-done/blob/0f417695ccf1f987af44bb4f4b3cbbdeb5f2c48b/src/gpd/core/health.py) (source: github_api): warnings.append(             "Publication / manuscript and full research presets are degraded without pypdf: "             "`write-paper`, `paper-build`, and `arxiv-submission` remain usable,
- [code_permalink](https://github.com/psi-oss/get-physics-done/blob/0f417695ccf1f987af44bb4f4b3cbbdeb5f2c48b/src/gpd/mcp/paper/models.py) (source: github_api): # Keep pdftotext_available as the toolchain-status field; PDF         # extraction now uses pypdf instead of the pdftotext binary.         # pdf_review_ready is set by the caller (e.g. detect_
- [readme_excerpt](https://github.com/psi-oss/get-physics-done/blob/main/README.md) (source: readme): It is designed for long-horizon projects that require rigorous verification, structured research memory, multi-step analytical work, complex numerical studies, and manuscript writing or review.

### 131. project-ryoma/ryoma

**Repository / product**

- Repository: [https://github.com/project-ryoma/ryoma](https://github.com/project-ryoma/ryoma)
- Company: Unknown — not stated in the repository
- Product: Ryoma
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://project-ryoma.github.io/ryoma/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 16/100 (a score, not a probability)
- Raw weighted score: 0.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `pypdf / PyPDF2`, run `run_2`, window `size:>16000`, rank 4
  - Query: `"pypdf" filename:requirements.txt size:>16000`
  - Sampled 30 of 1,476 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,476 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [requirements.txt](https://github.com/project-ryoma/ryoma/blob/main/requirements.txt)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [packages/ryoma_lab/pyproject.toml](https://github.com/project-ryoma/ryoma/blob/90edcd95c8cd954180f910cda3a09b7ffcfc99ae/packages/ryoma_lab/pyproject.toml)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/project-ryoma/ryoma/blob/90edcd95c8cd954180f910cda3a09b7ffcfc99ae/packages/ryoma_ai/ryoma_ai/vector_store/document_processor.py)

**Evidence trail**

- [api_response](https://github.com/project-ryoma/ryoma) (source: github_api): stars=405, fork=False, archived=False
- [manifest_line](https://github.com/project-ryoma/ryoma/blob/main/requirements.txt) (source: github_api): pypdf==4.3.1
- [manifest_line](https://github.com/project-ryoma/ryoma/blob/90edcd95c8cd954180f910cda3a09b7ffcfc99ae/packages/ryoma_lab/pyproject.toml) (source: github_api): "amundsen-databuilder>=7.5.0",     "ibis-framework>=10.0.0",     "fastapi-users[sqlalchemy,oauth]>=13.0.0",     "pypdf>=4.3.1",     "sql-formatter>=0.6.2",     "torch>=2.4.0",     "gpt4all>=2.8.2"
- [code_permalink](https://github.com/project-ryoma/ryoma/blob/90edcd95c8cd954180f910cda3a09b7ffcfc99ae/packages/ryoma_ai/ryoma_ai/vector_store/document_processor.py) (source: github_api): import pandas as pd from langchain_community.document_loaders import PyPDFLoader from langchain_core.documents import Document
- [readme_excerpt](https://github.com/project-ryoma/ryoma/blob/main/README.md) (source: readme): AI Powered Data Agent framework, a comprehensive solution for data analysis, engineering, and visualization.

### 132. adcontextprotocol/adcp

**Repository / product**

- Repository: [https://github.com/adcontextprotocol/adcp](https://github.com/adcontextprotocol/adcp)
- Company: Unknown — not stated in the repository
- Product: AdCP - Advertising Context Protocol
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2 \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 16/100 (a score, not a probability)
- Raw weighted score: 0.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 2 |
| Business criticality | 1 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:>16000`, rank 12
  - Query: `"mammoth" filename:package.json size:>16000`
  - Retrieved 30 of 283 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_2`, window `size:>16000`, rank 28
  - Query: `"puppeteer" filename:package.json size:>16000`
  - Retrieved 30 of 856 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package-lock.json](https://github.com/adcontextprotocol/adcp/blob/main/package-lock.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/adcontextprotocol/adcp/blob/main/package.json)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [package-lock.json](https://github.com/adcontextprotocol/adcp/blob/main/package-lock.json)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [package.json](https://github.com/adcontextprotocol/adcp/blob/main/package.json)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/adcontextprotocol/adcp/blob/3d38505d3b7d070294e4654140b5af40c54a7d54/server/src/addie/mcp/url-tools.ts)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/adcontextprotocol/adcp/blob/3d38505d3b7d070294e4654140b5af40c54a7d54/server/src/addie/jobs/committee-document-indexer.ts)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/adcontextprotocol/adcp/blob/3d38505d3b7d070294e4654140b5af40c54a7d54/server/tests/unit/document-parsers.test.ts)

**Evidence trail**

- [api_response](https://github.com/adcontextprotocol/adcp) (source: github_api): stars=241, fork=False, archived=False
- [manifest_line](https://github.com/adcontextprotocol/adcp/blob/main/package-lock.json) (source: github_api): "puppeteer": "^25.7.0",
- [manifest_line](https://github.com/adcontextprotocol/adcp/blob/main/package.json) (source: github_api): "puppeteer": "^25.7.0",
- [manifest_line](https://github.com/adcontextprotocol/adcp/blob/main/package-lock.json) (source: github_api): "mammoth": "^1.12.1",
- [manifest_line](https://github.com/adcontextprotocol/adcp/blob/main/package.json) (source: github_api): "mammoth": "^1.12.1",
- [code_permalink](https://github.com/adcontextprotocol/adcp/blob/3d38505d3b7d070294e4654140b5af40c54a7d54/server/src/addie/mcp/url-tools.ts) (source: github_api): // Handle Word documents - extract text using mammoth (if available) or return error     if (
- [code_permalink](https://github.com/adcontextprotocol/adcp/blob/3d38505d3b7d070294e4654140b5af40c54a7d54/server/src/addie/jobs/committee-document-indexer.ts) (source: github_api): } from '../mcp/google-docs.js'; import { isLLMConfigured, complete } from '../../utils/llm.js'; import { PDFParse } from 'pdf-parse'; import mammoth from 'mammoth'; import yauzl from 'yauzl'; import {
- [code_permalink](https://github.com/adcontextprotocol/adcp/blob/3d38505d3b7d070294e4654140b5af40c54a7d54/server/tests/unit/document-parsers.test.ts) (source: github_api): describe('parseDocxContent', () => {   it('extracts text from a minimal DOCX', async () => {     // mammoth expects a valid DOCX structure with [Content_Types].xml,     // word/document.xml, and _rel

### 133. rte-france/wattelse

**Repository / product**

- Repository: [https://github.com/rte-france/wattelse](https://github.com/rte-france/wattelse)
- Company: Unknown — not stated in the repository
- Product: WattElse project
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2 \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 16/100 (a score, not a probability)
- Raw weighted score: 0.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 2 |
| Business criticality | 1 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 17
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `mammoth / python-mammoth`, run `run_1`, window `size:1001..2000`, rank 15
  - Query: `"mammoth" filename:pyproject.toml size:1001..2000`
  - Retrieved 30 of 158 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 17
  - Query: `"docxtpl" filename:pyproject.toml`
  - Retrieved 30 of 427 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [pyproject.toml](https://github.com/rte-france/wattelse/blob/main/pyproject.toml)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [pyproject.toml](https://github.com/rte-france/wattelse/blob/main/pyproject.toml)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/rte-france/wattelse/blob/1a7ab033ef74b2884077c57b9d491de44df84e5c/wattelse/web_app/doc/views.py)

**Evidence trail**

- [api_response](https://github.com/rte-france/wattelse) (source: github_api): stars=10, fork=False, archived=False
- [manifest_line](https://github.com/rte-france/wattelse/blob/main/pyproject.toml) (source: github_api): docxtpl = "^0.18.0"
- [manifest_line](https://github.com/rte-france/wattelse/blob/main/pyproject.toml) (source: github_api): mammoth = "^1.9.0"
- [code_permalink](https://github.com/rte-france/wattelse/blob/1a7ab033ef74b2884077c57b9d491de44df84e5c/wattelse/web_app/doc/views.py) (source: github_api): import tempfile import mammoth from loguru import logger
- [readme_excerpt](https://github.com/rte-france/wattelse/blob/main/README.md) (source: readme): It is composed of two main modules: a simple chatbot interface to interact with any LLM -> **WattElse GPT** a Retrieval Augmented Generation (RAG) application -> **WattElse DOC** Some services are use

### 134. open-octo/octo-agent

**Repository / product**

- Repository: [https://github.com/open-octo/octo-agent](https://github.com/open-octo/octo-agent)
- Company: Unknown — not stated in the repository
- Product: octo-agent
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://octo-agent.dev/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 16/100 (a score, not a probability)
- Raw weighted score: 0.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:4001..8000`, rank 25
  - Query: `"mammoth" filename:requirements.txt size:4001..8000`
  - Retrieved 30 of 175 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/open-octo/octo-agent/blob/409561b28511385e5ba3d23331647fe6126cf5b4/internal/skills/defaults/ppt-master/scripts/svg_to_pptx.py)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/open-octo/octo-agent/blob/409561b28511385e5ba3d23331647fe6126cf5b4/internal/skills/defaults/ppt-master/scripts/template_fill_pptx.py)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/open-octo/octo-agent/blob/409561b28511385e5ba3d23331647fe6126cf5b4/internal/skills/defaults/ppt-master/scripts/native_enhance_pptx.py)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/open-octo/octo-agent/blob/409561b28511385e5ba3d23331647fe6126cf5b4/internal/skills/defaults/ppt-master/scripts/icon_sync.py)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/open-octo/octo-agent/blob/409561b28511385e5ba3d23331647fe6126cf5b4/internal/skills/defaults/ppt-master/scripts/pptx_to_svg.py)

**Evidence trail**

- [api_response](https://github.com/open-octo/octo-agent) (source: github_api): stars=94, fork=False, archived=False
- [code_permalink](https://github.com/open-octo/octo-agent/blob/409561b28511385e5ba3d23331647fe6126cf5b4/internal/skills/defaults/ppt-master/scripts/svg_to_pptx.py) (source: github_api): # requires-python = ">=3.11" # dependencies = [ #     "python-pptx>=0.6.21", "XlsxWriter>=3.0.0", "edge-tts>=7.2.8", #     "PyMuPDF>=1.23.0", "mammoth>=1.6.0", "markdownify>=0.11.6", #     "ebooklib>=
- [code_permalink](https://github.com/open-octo/octo-agent/blob/409561b28511385e5ba3d23331647fe6126cf5b4/internal/skills/defaults/ppt-master/scripts/template_fill_pptx.py) (source: github_api): # requires-python = ">=3.11" # dependencies = [ #     "python-pptx>=0.6.21", "XlsxWriter>=3.0.0", "edge-tts>=7.2.8", #     "PyMuPDF>=1.23.0", "mammoth>=1.6.0", "markdownify>=0.11.6", #     "ebooklib>=
- [code_permalink](https://github.com/open-octo/octo-agent/blob/409561b28511385e5ba3d23331647fe6126cf5b4/internal/skills/defaults/ppt-master/scripts/native_enhance_pptx.py) (source: github_api): # requires-python = ">=3.11" # dependencies = [ #     "python-pptx>=0.6.21", "XlsxWriter>=3.0.0", "edge-tts>=7.2.8", #     "PyMuPDF>=1.23.0", "mammoth>=1.6.0", "markdownify>=0.11.6", #     "ebooklib>=
- [code_permalink](https://github.com/open-octo/octo-agent/blob/409561b28511385e5ba3d23331647fe6126cf5b4/internal/skills/defaults/ppt-master/scripts/icon_sync.py) (source: github_api): # requires-python = ">=3.11" # dependencies = [ #     "python-pptx>=0.6.21", "XlsxWriter>=3.0.0", "edge-tts>=7.2.8", #     "PyMuPDF>=1.23.0", "mammoth>=1.6.0", "markdownify>=0.11.6", #     "ebooklib>=
- [code_permalink](https://github.com/open-octo/octo-agent/blob/409561b28511385e5ba3d23331647fe6126cf5b4/internal/skills/defaults/ppt-master/scripts/pptx_to_svg.py) (source: github_api): # requires-python = ">=3.11" # dependencies = [ #     "python-pptx>=0.6.21", "XlsxWriter>=3.0.0", "edge-tts>=7.2.8", #     "PyMuPDF>=1.23.0", "mammoth>=1.6.0", "markdownify>=0.11.6", #     "ebooklib>=
- [readme_excerpt](https://github.com/open-octo/octo-agent/blob/main/README.md) (source: readme): **Data stays on your machine**: self-hosted, zero telemetry — except for the model API calls you configure, octo sends no outbound traffic on its own.

### 135. espoon-voltti/evaka

**Repository / product**

- Repository: [https://github.com/espoon-voltti/evaka](https://github.com/espoon-voltti/evaka)
- Company: Unknown — not stated in the repository
- Product: eVaka® – ERP for early childhood education
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: industry_category=unknown; contributor_count not collected

**Score**

- Score: 16/100 (a score, not a probability)
- Raw weighted score: 0.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `Apache Tika`, run `run_2`, window `size:8001..16000`, rank 20
  - Query: `"tika" filename:build.gradle size:8001..16000`
  - Retrieved 30 of 210 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/espoon-voltti/evaka/blob/a92d9b6341b555f0f59dee7da632d93c686ef092/service/src/main/kotlin/evaka/core/s3/ContentTypeUtils.kt)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/espoon-voltti/evaka/blob/a92d9b6341b555f0f59dee7da632d93c686ef092/service/src/main/kotlin/evaka/trevaka/archival/tweb/RegionalArchivalFeeDecision.kt)
- `Apache Tika` (other_processing, extraction) — manifest_declaration — [service/evaka-bom/build.gradle.kts](https://github.com/espoon-voltti/evaka/blob/a92d9b6341b555f0f59dee7da632d93c686ef092/service/evaka-bom/build.gradle.kts)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/espoon-voltti/evaka/blob/a92d9b6341b555f0f59dee7da632d93c686ef092/service/src/main/kotlin/evaka/trevaka/archival/tweb/RegionalArchivalChildDocument.kt)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/espoon-voltti/evaka/blob/a92d9b6341b555f0f59dee7da632d93c686ef092/service/src/integrationTest/kotlin/evaka/core/attachments/AttachmentsIntegrationTest.kt)

**Evidence trail**

- [api_response](https://github.com/espoon-voltti/evaka) (source: github_api): stars=58, fork=False, archived=False
- [readme_excerpt](https://github.com/espoon-voltti/evaka/blob/master/README.md) (source: readme): company stated as 'Text'
- [code_permalink](https://github.com/espoon-voltti/evaka/blob/a92d9b6341b555f0f59dee7da632d93c686ef092/service/src/main/kotlin/evaka/core/s3/ContentTypeUtils.kt) (source: github_api): import evaka.core.shared.domain.BadRequest import java.io.InputStream val tika: org.apache.tika.Tika = org.apache.tika.Tika() enum class ContentTypePattern(     private val type: String,
- [code_permalink](https://github.com/espoon-voltti/evaka/blob/a92d9b6341b555f0f59dee7da632d93c686ef092/service/src/main/kotlin/evaka/trevaka/archival/tweb/RegionalArchivalFeeDecision.kt) (source: github_api): import evaka.core.s3.Document import evaka.trevaka.archival.status import evaka.trevaka.jaxb.localDateToXMLGregorianCalendar import org.apache.tika.mime.MimeTypes internal fun transformFeeDecision(
- [manifest_line](https://github.com/espoon-voltti/evaka/blob/a92d9b6341b555f0f59dee7da632d93c686ef092/service/evaka-bom/build.gradle.kts) (source: github_api): api("org.apache.commons:commons-text:1.15.0")         api("org.apache.commons:commons-imaging:1.0.0-alpha6")         api("org.apache.httpcomponents:httpclient:4.5.14")         api("org.apache.
- [code_permalink](https://github.com/espoon-voltti/evaka/blob/a92d9b6341b555f0f59dee7da632d93c686ef092/service/src/main/kotlin/evaka/trevaka/archival/tweb/RegionalArchivalChildDocument.kt) (source: github_api): import evaka.core.s3.Document import evaka.trevaka.archival.status import evaka.trevaka.jaxb.localDateToXMLGregorianCalendar import org.apache.tika.mime.MimeTypes internal fun transformChildDocument(
- [code_permalink](https://github.com/espoon-voltti/evaka/blob/a92d9b6341b555f0f59dee7da632d93c686ef092/service/src/integrationTest/kotlin/evaka/core/attachments/AttachmentsIntegrationTest.kt) (source: github_api): ContentTypePattern.MSWORD,                         ContentTypePattern.MSWORD_DOCX,                         ContentTypePattern.OPEN_DOCUMENT_TEXT,                         Conten
- [readme_excerpt](https://github.com/espoon-voltti/evaka/blob/master/README.md) (source: readme): [Docker](https://www.docker.com) [`service/service-lib`](service/service-lib/) – Old common library for service projects, but today only used by `service`.

### 136. Pissaia92/chatbot-rag-autosservico

**Repository / product**

- Repository: [https://github.com/pissaia92/chatbot-rag-autosservico](https://github.com/pissaia92/chatbot-rag-autosservico)
- Company: Unknown — not stated in the repository
- Product: In progress [......]
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2 \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 16/100 (a score, not a probability)
- Raw weighted score: 0.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 2 |
| Business criticality | 1 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Unstructured`, run `run_2`, window `size:8001..16000`, rank 18
  - Query: `"unstructured" filename:requirements.txt size:8001..16000`
  - Sampled 30 of 54,144 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 54,144 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_2`, window `size:8001..16000`, rank 27
  - Query: `"python-docx" filename:requirements.txt size:8001..16000`
  - Sampled 30 of 1,280 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,280 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Unstructured` (other_processing, extraction) — manifest_declaration — [deprec-requirements.txt](https://github.com/Pissaia92/chatbot-rag-autosservico/blob/main/deprec-requirements.txt)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/Pissaia92/chatbot-rag-autosservico/blob/main/requirements.txt)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/Pissaia92/chatbot-rag-autosservico/blob/5227479d3fbabcb2457359c28275323a3d94e6e7/ingest.py)
- `python-docx` (docx, generation) — manifest_declaration — [deprec-requirements.txt](https://github.com/Pissaia92/chatbot-rag-autosservico/blob/main/deprec-requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [requirements.txt](https://github.com/Pissaia92/chatbot-rag-autosservico/blob/main/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/Pissaia92/chatbot-rag-autosservico) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/Pissaia92/chatbot-rag-autosservico/blob/main/deprec-requirements.txt) (source: github_api): #   unstructured-client
- [manifest_line](https://github.com/Pissaia92/chatbot-rag-autosservico/blob/main/requirements.txt) (source: github_api): # UNSTRUCTURED
- [code_permalink](https://github.com/Pissaia92/chatbot-rag-autosservico/blob/5227479d3fbabcb2457359c28275323a3d94e6e7/ingest.py) (source: github_api): import os import re from typing import List from unstructured.partition.auto import partition from sentence_transformers import SentenceTransformer embedding_model = SentenceTransformer("all-MiniLM-L
- [manifest_line](https://github.com/Pissaia92/chatbot-rag-autosservico/blob/main/deprec-requirements.txt) (source: github_api): #   python-docx
- [manifest_line](https://github.com/Pissaia92/chatbot-rag-autosservico/blob/main/requirements.txt) (source: github_api): python-docx==1.2.0

### 137. stardustai/dataset-viewer

**Repository / product**

- Repository: [https://github.com/stardustai/dataset-viewer](https://github.com/stardustai/dataset-viewer)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://stardustai.github.io/dataset-viewer

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 16/100 (a score, not a probability)
- Raw weighted score: 0.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:2001..4000`, rank 5
  - Query: `"mammoth" filename:package.json size:2001..4000`
  - Sampled 30 of 7,920 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,920 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [package.json](https://github.com/stardustai/dataset-viewer/blob/main/package.json)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/stardustai/dataset-viewer/blob/47acb50658414581336580a57083ddc758ee4827/src/components/FileViewer/viewers/WordViewer.tsx)

**Evidence trail**

- [api_response](https://github.com/stardustai/dataset-viewer) (source: github_api): stars=1003, fork=False, archived=False
- [manifest_line](https://github.com/stardustai/dataset-viewer/blob/main/package.json) (source: github_api): "mammoth": "^1.11.0",
- [code_permalink](https://github.com/stardustai/dataset-viewer/blob/47acb50658414581336580a57083ddc758ee4827/src/components/FileViewer/viewers/WordViewer.tsx) (source: github_api): import DOMPurify from 'dompurify'; import mammoth from 'mammoth'; import type { FC } from 'react'; import { useEffect, useMemo, useState } from 'react'; import { useTranslation } from 'react-i18next';
- [readme_excerpt](https://github.com/stardustai/dataset-viewer/blob/main/README.md) (source: readme): Our plugin system allows you to add support for new file formats and viewers.

### 138. readest/readest

**Repository / product**

- Repository: [https://github.com/readest/readest](https://github.com/readest/readest)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://readest.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 16/100 (a score, not a probability)
- Raw weighted score: 0.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:>16000`, rank 5
  - Query: `"mammoth" filename:package.json size:>16000`
  - Retrieved 30 of 283 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/readest/readest/blob/558ed2afb488efe4b88ed3da9130130f9389bff5/apps/readest-app/src/workers/send-conversion.worker.ts)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/readest/readest/blob/558ed2afb488efe4b88ed3da9130130f9389bff5/apps/readest-app/src/services/send/conversion/convertToEpub.ts)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [apps/readest-app/package.json](https://github.com/readest/readest/blob/558ed2afb488efe4b88ed3da9130130f9389bff5/apps/readest-app/package.json)

**Evidence trail**

- [api_response](https://github.com/readest/readest) (source: github_api): stars=23670, fork=False, archived=False
- [code_permalink](https://github.com/readest/readest/blob/558ed2afb488efe4b88ed3da9130130f9389bff5/apps/readest-app/src/workers/send-conversion.worker.ts) (source: github_api): ConversionWorkerResponse, } from '../services/send/conversion/conversion-worker-protocol'; // Document conversion (mammoth DOCX parsing, Readability, EPUB zip assembly) is // CPU-heavy; running it
- [code_permalink](https://github.com/readest/readest/blob/558ed2afb488efe4b88ed3da9130130f9389bff5/apps/readest-app/src/services/send/conversion/convertToEpub.ts) (source: github_api): import { detectLanguage } from '@/utils/lang'; // `mammoth` (DOCX → HTML) and `TxtToEpubConverter` are dynamically imported // inside their respective `case` bodies in `convertToEpub`. They're heavy
- [manifest_line](https://github.com/readest/readest/blob/558ed2afb488efe4b88ed3da9130130f9389bff5/apps/readest-app/package.json) (source: github_api): "katex": "^0.16.45",     "lucide-react": "^0.562.0",     "lunr": "^2.3.9",     "mammoth": "^1.12.0",     "marked": "^15.0.12",     "marked-footnote": "^1.4.0",     "marked-katex-extension": "^5.1.
- [readme_excerpt](https://github.com/readest/readest/blob/main/README.md) (source: readme): This behavior is usually caused by compatibility issues between the bundled AppImage libraries and the system’s EGL / Wayland environment.

### 139. open-mercato/open-mercato

**Repository / product**

- Repository: [https://github.com/open-mercato/open-mercato](https://github.com/open-mercato/open-mercato)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.openmercato.com/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 16/100 (a score, not a probability)
- Raw weighted score: 0.80 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:8001..16000`, rank 25
  - Query: `"mammoth" filename:package.json size:8001..16000`
  - Retrieved 30 of 737 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/open-mercato/open-mercato/blob/12049a2a958d1de4e78548e0318d235de71be2e8/packages/core/src/modules/attachments/lib/textExtraction.ts)

**Evidence trail**

- [api_response](https://github.com/open-mercato/open-mercato) (source: github_api): stars=1671, fork=False, archived=False
- [code_permalink](https://github.com/open-mercato/open-mercato/blob/12049a2a958d1de4e78548e0318d235de71be2e8/packages/core/src/modules/attachments/lib/textExtraction.ts) (source: github_api): function isDocx(mimeType: string, ext: string): boolean {   // mammoth supports only Open XML .docx, not legacy binary .doc files.   return (
- [readme_excerpt](https://github.com/open-mercato/open-mercato/blob/main/README.md) (source: readme): Built for CTOs who have already deployed Cursor/Copilot and noticed it isn't enough.

### 140. huridocs/pdf-document-layout-analysis

**Repository / product**

- Repository: [https://github.com/huridocs/pdf-document-layout-analysis](https://github.com/huridocs/pdf-document-layout-analysis)
- Company: Alibaba Research Group
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| supporting: confirmed generation/conversion code \| unknown: industry_category=unknown; contributor_count not collected

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `Pandoc`, run `run_1`, window `unsliced`, rank 11
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `Pandoc`, run `run_2`, window `unsliced`, rank 11
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Pandoc` (conversion, conversion) — manifest_declaration — [pyproject.toml](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/pyproject.toml)
- `Pandoc` (conversion, conversion) — manifest_declaration — [requirements.txt](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/requirements.txt)
- `Pandoc` (conversion, conversion) — infrastructure_reference — [code](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/Dockerfile)

**Evidence trail**

- [api_response](https://github.com/huridocs/pdf-document-layout-analysis) (source: github_api): stars=1344, fork=False, archived=False
- [readme_excerpt](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/README.md) (source: readme): company stated as 'Alibaba Research Group'
- [manifest_line](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/pyproject.toml) (source: github_api): "pypandoc==1.17",
- [manifest_line](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/requirements.txt) (source: github_api): pypandoc==1.17
- [code_permalink](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/Dockerfile) (source: github_api): pandoc \
- [readme_excerpt](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/README.md) (source: readme): Sharing your use case helps us improve the service for everyone.
- [api_response](https://github.com/huridocs/pdf-document-layout-analysis) (source: github_api): stars=1344, fork=False, archived=False
- [code_permalink](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/Dockerfile) (source: github_api): ARG BUILDER_IMAGE=nvidia/cuda:12.6.0-cudnn-devel-ubuntu24.04 ARG TORCH_INDEX_URL=https://download.pytorch.org/whl/cu126 ARG FORCE_CUDA=1 ARG TORCH_CUDA_ARCH_LIST="6.1;7.0;7.5;8.0;8.6;8.9;9.0" FROM ${
- [readme_excerpt](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/README.md) (source: readme): company stated as 'Alibaba Research Group'
- [manifest_line](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/pyproject.toml) (source: github_api): "pypandoc==1.17",
- [manifest_line](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/requirements.txt) (source: github_api): pypandoc==1.17
- [code_permalink](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/Dockerfile) (source: github_api): pandoc \
- [code_permalink](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/Dockerfile) (source: github_api): pandoc \
- [readme_excerpt](https://github.com/huridocs/pdf-document-layout-analysis/blob/main/README.md) (source: readme): Sharing your use case helps us improve the service for everyone.

### 141. imarthe75/ades-nevadi

**Repository / product**

- Repository: [https://github.com/imarthe75/ades-nevadi](https://github.com/imarthe75/ades-nevadi)
- Company: Unknown — not stated in the repository
- Product: ADES — Sistema Integral de Administración Escolar
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://portalnvd.setag.mx

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 28
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 28
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/imarthe75/ades-nevadi/blob/b2160deac0d29756e36130ad5703c4ed8b508842/backend/app/api/v1/carbone.py)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/imarthe75/ades-nevadi/blob/b2160deac0d29756e36130ad5703c4ed8b508842/integrations/carbone/server.js)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [integrations/carbone/package.json](https://github.com/imarthe75/ades-nevadi/blob/b2160deac0d29756e36130ad5703c4ed8b508842/integrations/carbone/package.json)

**Evidence trail**

- [api_response](https://github.com/imarthe75/ades-nevadi) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/imarthe75/ades-nevadi/blob/b2160deac0d29756e36130ad5703c4ed8b508842/backend/app/api/v1/carbone.py) (source: github_api): GET  /carbone/templates                 — lista plantillas disponibles   POST /carbone/templates                 — sube una plantilla (admin)   DELETE /carbone/templates/{id}          — elimina plan
- [code_permalink](https://github.com/imarthe75/ades-nevadi/blob/b2160deac0d29756e36130ad5703c4ed8b508842/integrations/carbone/server.js) (source: github_api): /**  * Carbone Server ADES — microservicio de generación de reportes.  *
- [manifest_line](https://github.com/imarthe75/ades-nevadi/blob/b2160deac0d29756e36130ad5703c4ed8b508842/integrations/carbone/package.json) (source: github_api): {   "name": "carbone-server-ades",   "version": "1.0.0",   "description": "Microservicio Carbone para generación de reportes ADES Instituto Nevadi",   "main": "server.js",   "dependencies": {     "car

### 142. azavea/raster-vision

**Repository / product**

- Repository: [https://github.com/azavea/raster-vision](https://github.com/azavea/raster-vision)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://docs.rastervision.io

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| supporting: confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `Pandoc`, run `run_1`, window `unsliced`, rank 1
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `Pandoc`, run `run_2`, window `unsliced`, rank 1
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Pandoc` (conversion, conversion) — manifest_declaration — [requirements.txt](https://github.com/azavea/raster-vision/blob/master/requirements.txt)
- `Pandoc` (conversion, conversion) — infrastructure_reference — [code](https://github.com/azavea/raster-vision/blob/master/Dockerfile)

**Evidence trail**

- [api_response](https://github.com/azavea/raster-vision) (source: github_api): stars=2240, fork=False, archived=False
- [manifest_line](https://github.com/azavea/raster-vision/blob/master/requirements.txt) (source: github_api): pandocfilters==1.5.1
- [code_permalink](https://github.com/azavea/raster-vision/blob/master/Dockerfile) (source: github_api): # Install pandoc, needed for rendering notebooks
- [readme_excerpt](https://github.com/azavea/raster-vision/blob/master/README.md) (source: readme): 3rd party licenses for all dependecies used by Raster Vision can be found [here](./THIRD_PARTY_LICENSES.txt).
- [api_response](https://github.com/azavea/raster-vision) (source: github_api): stars=2240, fork=False, archived=False
- [code_permalink](https://github.com/azavea/raster-vision/blob/master/Dockerfile) (source: github_api): ARG BUILD_TYPE ARG CUDA_VERSION ARG UBUNTU_VERSION ######################################################################## FROM nvidia/cuda:${CUDA_VERSION}-cudnn8-runtime-ubuntu${UBUNTU_VERSION} AS
- [manifest_line](https://github.com/azavea/raster-vision/blob/master/requirements.txt) (source: github_api): pandocfilters==1.5.1
- [code_permalink](https://github.com/azavea/raster-vision/blob/master/Dockerfile) (source: github_api): # Install pandoc, needed for rendering notebooks
- [code_permalink](https://github.com/azavea/raster-vision/blob/master/Dockerfile) (source: github_api): # Install pandoc, needed for rendering notebooks
- [readme_excerpt](https://github.com/azavea/raster-vision/blob/master/README.md) (source: readme): 3rd party licenses for all dependecies used by Raster Vision can be found [here](./THIRD_PARTY_LICENSES.txt).

### 143. dalibo/pandocker

**Repository / product**

- Repository: [https://github.com/dalibo/pandocker](https://github.com/dalibo/pandocker)
- Company: Unknown — not stated in the repository
- Product: pandocker
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://hub.docker.com/r/dalibo/pandocker/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| supporting: confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `Pandoc`, run `run_1`, window `unsliced`, rank 16
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `Pandoc`, run `run_2`, window `unsliced`, rank 16
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Pandoc` (conversion, conversion) — manifest_declaration — [requirements.txt](https://github.com/dalibo/pandocker/blob/latest/requirements.txt)
- `Pandoc` (conversion, conversion) — infrastructure_reference — [code](https://github.com/dalibo/pandocker/blob/latest/Dockerfile)

**Evidence trail**

- [api_response](https://github.com/dalibo/pandocker) (source: github_api): stars=168, fork=False, archived=False
- [manifest_line](https://github.com/dalibo/pandocker/blob/latest/requirements.txt) (source: github_api): # https://github.com/daamien/pandoc-cover/releases/latest
- [code_permalink](https://github.com/dalibo/pandocker/blob/latest/Dockerfile) (source: github_api): FROM pandoc/extra:3.7-ubuntu AS extra
- [readme_excerpt](https://github.com/dalibo/pandocker/blob/latest/README.md) (source: readme): So far, we provide the 3 templates below: [eisvogel] is designed for lecture notes and exercises with a focus on computer science.
- [api_response](https://github.com/dalibo/pandocker) (source: github_api): stars=168, fork=False, archived=False
- [code_permalink](https://github.com/dalibo/pandocker/blob/latest/Dockerfile) (source: github_api): # # STAGE 1: extra variant # FROM pandoc/extra:3.7-ubuntu AS extra # Set the env variables to non-interactive ENV DEBIAN_FRONTEND noninteractive ENV DEBIAN_PRIORITY critical ENV DEBCONF_NOWARNINGS ye
- [manifest_line](https://github.com/dalibo/pandocker/blob/latest/requirements.txt) (source: github_api): # https://github.com/daamien/pandoc-cover/releases/latest
- [code_permalink](https://github.com/dalibo/pandocker/blob/latest/Dockerfile) (source: github_api): FROM pandoc/extra:3.7-ubuntu AS extra
- [code_permalink](https://github.com/dalibo/pandocker/blob/latest/Dockerfile) (source: github_api): FROM pandoc/extra:3.7-ubuntu AS extra
- [readme_excerpt](https://github.com/dalibo/pandocker/blob/latest/README.md) (source: readme): So far, we provide the 3 templates below: [eisvogel] is designed for lecture notes and exercises with a focus on computer science.

### 144. carbon-design-system/carbon

**Repository / product**

- Repository: [https://github.com/carbon-design-system/carbon](https://github.com/carbon-design-system/carbon)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.carbondesignsystem.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 22
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 22
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/carbon-design-system/carbon/blob/94437ffbc2ce5894425cd579dcb75648bba49d1f/packages/web-components/src/components/icon/icon.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/carbon-design-system/carbon/blob/94437ffbc2ce5894425cd579dcb75648bba49d1f/packages/web-components/src/components/form/form.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/carbon-design-system/carbon/blob/94437ffbc2ce5894425cd579dcb75648bba49d1f/packages/web-components/src/components/grid/column.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/carbon-design-system/carbon/blob/94437ffbc2ce5894425cd579dcb75648bba49d1f/packages/web-components/src/components/layer/layer.ts)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/carbon-design-system/carbon/blob/94437ffbc2ce5894425cd579dcb75648bba49d1f/packages/web-components/src/components/form/form-item.ts)

**Evidence trail**

- [api_response](https://github.com/carbon-design-system/carbon) (source: github_api): stars=9373, fork=False, archived=False
- [code_permalink](https://github.com/carbon-design-system/carbon/blob/94437ffbc2ce5894425cd579dcb75648bba49d1f/packages/web-components/src/components/icon/icon.ts) (source: github_api): import { LitElement, html } from 'lit'; import { property } from 'lit/decorators.js'; import { prefix } from '../../globals/settings'; import { carbonElement as customElement } from '../../globals/dec
- [code_permalink](https://github.com/carbon-design-system/carbon/blob/94437ffbc2ce5894425cd579dcb75648bba49d1f/packages/web-components/src/components/form/form.ts) (source: github_api): import { LitElement, html } from 'lit'; import { prefix } from '../../globals/settings'; import styles from './form.scss?lit'; import { carbonElement as customElement } from '../../globals/decorators/
- [code_permalink](https://github.com/carbon-design-system/carbon/blob/94437ffbc2ce5894425cd579dcb75648bba49d1f/packages/web-components/src/components/grid/column.ts) (source: github_api): import { LitElement } from 'lit'; import { property } from 'lit/decorators.js'; import { carbonElement as customElement } from '../../globals/decorators/carbon-element'; import { prefix } from '../..
- [code_permalink](https://github.com/carbon-design-system/carbon/blob/94437ffbc2ce5894425cd579dcb75648bba49d1f/packages/web-components/src/components/layer/layer.ts) (source: github_api): import { LitElement, html } from 'lit'; import { property } from 'lit/decorators.js'; import { carbonElement as customElement } from '../../globals/decorators/carbon-element'; import { prefix } from
- [code_permalink](https://github.com/carbon-design-system/carbon/blob/94437ffbc2ce5894425cd579dcb75648bba49d1f/packages/web-components/src/components/form/form-item.ts) (source: github_api): import { LitElement, html } from 'lit'; import { prefix } from '../../globals/settings'; import styles from './form-item.scss?lit'; import { carbonElement as customElement } from '../../globals/decora

### 145. globalis-ms/carbone

**Repository / product**

- Repository: [https://github.com/globalis-ms/carbone](https://github.com/globalis-ms/carbone)
- Company: Unknown — not stated in the repository
- Product: CARBONE
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 8
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 8
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/globalis-ms/carbone/blob/7e70680b3773a26fc124bea8a5f7ae365093ea13/include/lib/lib_carbone.php)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/globalis-ms/carbone/blob/7e70680b3773a26fc124bea8a5f7ae365093ea13/web/theme/carbone/start_html.php)

**Evidence trail**

- [api_response](https://github.com/globalis-ms/carbone) (source: github_api): stars=8, fork=False, archived=False
- [code_permalink](https://github.com/globalis-ms/carbone/blob/7e70680b3773a26fc124bea8a5f7ae365093ea13/include/lib/lib_carbone.php) (source: github_api): if(is_array($data) \|\| is_object($data))         echo("<script>console.log('Carbone: ".json_encode($data)."');</script>");     else         echo("<script>console.log('Carbone: ".$data."');</scri
- [code_permalink](https://github.com/globalis-ms/carbone/blob/7e70680b3773a26fc124bea8a5f7ae365093ea13/web/theme/carbone/start_html.php) (source: github_api): <meta http-equiv="Cache-Control" content="no-cache">         <meta http-equiv="Cache-Control" content="no-store">         <meta http-equiv="Cache-Control" content="must-revalidate">         <m

### 146. gyselroth/balloon

**Repository / product**

- Repository: [https://github.com/gyselroth/balloon](https://github.com/gyselroth/balloon)
- Company: Unknown — not stated in the repository
- Product: balloon
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 11
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 11
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/gyselroth/balloon/blob/991e097e1b3d2531d5344c77d828fe15d6357409/src/app/Balloon.App.Wopi/.container.config.php)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/gyselroth/balloon/blob/991e097e1b3d2531d5344c77d828fe15d6357409/src/app/Balloon.App.Office/.container.config.php)

**Evidence trail**

- [api_response](https://github.com/gyselroth/balloon) (source: github_api): stars=21, fork=False, archived=False
- [code_permalink](https://github.com/gyselroth/balloon/blob/991e097e1b3d2531d5344c77d828fe15d6357409/src/app/Balloon.App.Wopi/.container.config.php) (source: github_api): 'config' => [                 'hosts' => [                     [                         'name' => 'LibreOffice Online',                         'url' => '{ENV(BALLOON_LIBREOFFICE_COLLAB_U
- [code_permalink](https://github.com/gyselroth/balloon/blob/991e097e1b3d2531d5344c77d828fe15d6357409/src/app/Balloon.App.Office/.container.config.php) (source: github_api): ClientInterface::class => [                 'arguments' => [                     'config' => [                         'base_uri' => '{ENV(BALLOON_LIBREOFFICE_CONVERT_URL,https://libreoffi
- [readme_excerpt](https://github.com/gyselroth/balloon/blob/master/README.md) (source: readme): Of course there is also a complete desktop solution for balloon.

### 147. dante-ev/docker-texlive

**Repository / product**

- Repository: [https://github.com/dante-ev/docker-texlive](https://github.com/dante-ev/docker-texlive)
- Company: Unknown — not stated in the repository
- Product: Docker image for TeX Live
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://hub.docker.com/r/danteev/texlive/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| supporting: confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `Pandoc`, run `run_1`, window `unsliced`, rank 29
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `Pandoc`, run `run_2`, window `unsliced`, rank 29
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Pandoc` (conversion, conversion) — infrastructure_reference — [code](https://github.com/dante-ev/docker-texlive/blob/main/Dockerfile)

**Evidence trail**

- [api_response](https://github.com/dante-ev/docker-texlive) (source: github_api): stars=117, fork=False, archived=False
- [code_permalink](https://github.com/dante-ev/docker-texlive/blob/main/Dockerfile) (source: github_api): # pandoc in the repositories is older - we just overwrite it with a more recent version
- [readme_excerpt](https://github.com/dante-ev/docker-texlive/blob/main/README.md) (source: readme): In case this all-in-one image is too large for you, you might be interested in following images: [VS.Code DevContainer](https://github.com/a-nau/latex-devcontainer) - contains a ready-to-start VS Code
- [api_response](https://github.com/dante-ev/docker-texlive) (source: github_api): stars=117, fork=False, archived=False
- [code_permalink](https://github.com/dante-ev/docker-texlive/blob/main/Dockerfile) (source: github_api): FROM registry.gitlab.com/islandoftex/images/texlive:latest # FROM registry.gitlab.com/islandoftex/images/texlive:TL2026-2026-06-26-full ARG TARGETARCH LABEL \   org.opencontainers.image.title="Full
- [code_permalink](https://github.com/dante-ev/docker-texlive/blob/main/Dockerfile) (source: github_api): # pandoc in the repositories is older - we just overwrite it with a more recent version
- [code_permalink](https://github.com/dante-ev/docker-texlive/blob/main/Dockerfile) (source: github_api): # pandoc in the repositories is older - we just overwrite it with a more recent version
- [readme_excerpt](https://github.com/dante-ev/docker-texlive/blob/main/README.md) (source: readme): In case this all-in-one image is too large for you, you might be interested in following images: [VS.Code DevContainer](https://github.com/a-nau/latex-devcontainer) - contains a ready-to-start VS Code

### 148. ad-on-is/rachoon

**Repository / product**

- Repository: [https://github.com/ad-on-is/rachoon](https://github.com/ad-on-is/rachoon)
- Company: Unknown — not stated in the repository
- Product: Rachoon — The Clever Way to Handle Invoices
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: infrastructure_service_present=true; confirmed generation/conversion code

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 1
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 1
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/ad-on-is/rachoon/blob/main/docker-compose.yaml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/ad-on-is/rachoon/blob/c532aa2fc969c6ef3b12bae3df33fb8fb02b64c0/apps/backend/app/Services/Renderer.ts)

**Evidence trail**

- [api_response](https://github.com/ad-on-is/rachoon) (source: github_api): stars=978, fork=False, archived=False
- [code_permalink](https://github.com/ad-on-is/rachoon/blob/main/docker-compose.yaml) (source: github_api): - "GOTENBERG_URL=http://gotenberg:3000"
- [code_permalink](https://github.com/ad-on-is/rachoon/blob/c532aa2fc969c6ef3b12bae3df33fb8fb02b64c0/apps/backend/app/Services/Renderer.ts) (source: github_api): f.append('preferCssPageSize', 'true')     f.append('generateDocumentOutline', 'true')     const res = await fetch(       `${process.env.GOTENBERG_URL \|\| 'http://gotenberg'}/forms/chromium/convert/
- [readme_excerpt](https://github.com/ad-on-is/rachoon/blob/main/README.md) (source: readme): <div align="center"> <img src="https://raw.githubusercontent.com/ad-on-is/rachoon/main/apps/frontend/assets/logo.png" height="100" /> </div> **Rachoon** (from _račun_, meaning _invoice_ in Bosnian) is
- [api_response](https://github.com/ad-on-is/rachoon) (source: github_api): stars=978, fork=False, archived=False
- [code_permalink](https://github.com/ad-on-is/rachoon/blob/main/docker-compose.yaml) (source: github_api): services:   rachoon:     image: ghcr.io/ad-on-is/rachoon     container_name: rachoon     environment:       - APP_KEY=e494d218125cd56396f2a12421d3a03a       - DB_CONNECTION=pg       - "GOTENBERG_URL=h
- [code_permalink](https://github.com/ad-on-is/rachoon/blob/main/docker-compose.yaml) (source: github_api): - "GOTENBERG_URL=http://gotenberg:3000"
- [code_permalink](https://github.com/ad-on-is/rachoon/blob/main/docker-compose.yaml) (source: github_api): - "GOTENBERG_URL=http://gotenberg:3000"
- [code_permalink](https://github.com/ad-on-is/rachoon/blob/c532aa2fc969c6ef3b12bae3df33fb8fb02b64c0/apps/backend/app/Services/Renderer.ts) (source: github_api): f.append('preferCssPageSize', 'true')     f.append('generateDocumentOutline', 'true')     const res = await fetch(       `${process.env.GOTENBERG_URL \|\| 'http://gotenberg'}/forms/chromium/convert/
- [readme_excerpt](https://github.com/ad-on-is/rachoon/blob/main/README.md) (source: readme): <div align="center"> <img src="https://raw.githubusercontent.com/ad-on-is/rachoon/main/apps/frontend/assets/logo.png" height="100" /> </div> **Rachoon** (from _račun_, meaning _invoice_ in Bosnian) is

### 149. riclolsen/json-scada

**Repository / product**

- Repository: [https://github.com/riclolsen/json-scada](https://github.com/riclolsen/json-scada)
- Company: Unknown — not stated in the repository
- Product: {json:scada}
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://riclolsen.github.io/json-scada/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 5
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 5
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/riclolsen/json-scada/blob/06a2b03961a992c3557d91a2805cc09cd5fb0a14/src/carbone-reports/index.js)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/riclolsen/json-scada/blob/06a2b03961a992c3557d91a2805cc09cd5fb0a14/src/carbone-reports/app-defs.js)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [src/carbone-reports/package.json](https://github.com/riclolsen/json-scada/blob/06a2b03961a992c3557d91a2805cc09cd5fb0a14/src/carbone-reports/package.json)

**Evidence trail**

- [api_response](https://github.com/riclolsen/json-scada) (source: github_api): stars=418, fork=False, archived=False
- [code_permalink](https://github.com/riclolsen/json-scada/blob/06a2b03961a992c3557d91a2805cc09cd5fb0a14/src/carbone-reports/index.js) (source: github_api): /*  * Carbone Reports Example  *
- [code_permalink](https://github.com/riclolsen/json-scada/blob/06a2b03961a992c3557d91a2805cc09cd5fb0a14/src/carbone-reports/app-defs.js) (source: github_api): 'use strict' module.exports = {   NAME: 'CARBONE_REPORTS',   ENV_PREFIX: 'JS_CARBONE_',   MSG: '{json:scada} - Carbone Reports',   VERSION: '0.1.1',
- [manifest_line](https://github.com/riclolsen/json-scada/blob/06a2b03961a992c3557d91a2805cc09cd5fb0a14/src/carbone-reports/package.json) (source: github_api): {   "dependencies": {     "carbone": "^3.2.3",     "mongodb": "^6.7.0",     "pg": "^8.7.1"   } }

### 150. DefinitelyTyped/DefinitelyTyped

**Repository / product**

- Repository: [https://github.com/definitelytyped/definitelytyped](https://github.com/definitelytyped/definitelytyped)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: healthcare_diagnostics (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 2 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 1
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `docx (dolanmiu/docx)`, run `run_1`, window `size:251..500`, rank 1
  - Query: `"docx" filename:package.json size:251..500`
  - Sampled 30 of 2,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,256 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 1
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — manifest_declaration — [types/carbone/package.json](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/carbone/package.json)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [types/json2xml/package.json](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/json2xml/package.json)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [types/aws-lambda/package.json](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/aws-lambda/package.json)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [types/node-canvas-text/package.json](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/node-canvas-text/package.json)
- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/html-docx-js/index.d.ts)
- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/jsreport-docx/index.d.ts)
- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/jsreport-html-embedded-in-docx/index.d.ts)
- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/pdf2docx/index.d.ts)
- `docx (dolanmiu/docx)` (docx, generation) — manifest_declaration — [types/html-to-docx/package.json](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/html-to-docx/package.json)

**Evidence trail**

- [api_response](https://github.com/DefinitelyTyped/DefinitelyTyped) (source: github_api): stars=51381, fork=False, archived=False
- [manifest_line](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/carbone/package.json) (source: github_api): "private": true,     "name": "@types/carbone",     "version": "3.2.9999",
- [manifest_line](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/json2xml/package.json) (source: github_api): "owners": [         {             "name": "Gabriel Fournier",             "githubUsername": "carboneater"         }     ] }
- [manifest_line](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/aws-lambda/package.json) (source: github_api): "githubUsername": "redlickigrzegorz"         },         {             "name": "Juan Carbonel",             "githubUsername": "juancarbonel"         },         {
- [manifest_line](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/node-canvas-text/package.json) (source: github_api): "owners": [         {             "name": "Gabriel Fournier",             "githubUsername": "carboneater"         }     ] }
- [code_permalink](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/html-docx-js/index.d.ts) (source: github_api): /// <reference types="node" /> /**  * To generate DOCX, simply pass a HTML document (as string) to this method  * to receive `Blob` (or `Buffer`) containing the output file.  */ export function asBlo
- [code_permalink](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/jsreport-docx/index.d.ts) (source: github_api): declare namespace JsReportDocx {     interface DocxTemplateModifier extends TemplateBase {         docx?: DocxTemplate \| undefined;     }     interface Configuration {
- [code_permalink](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/jsreport-html-embedded-in-docx/index.d.ts) (source: github_api): declare namespace JsReportHtmlEmbeddedInDocx {     interface HtmlEmbeddedInDocxTemplate extends Template {         recipe: "html-embedded-in-docx" \| string;     } }
- [code_permalink](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/pdf2docx/index.d.ts) (source: github_api): constructor(pdf_file: string \| Buffer, password?: string);     /**      * Parse and convert PDF to DOCX      * @param docx_file Output DOCX file path      * @param options Conversion options
- [manifest_line](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/df17ec34853e80dac955a0c2649cec989d90b2b5/types/html-to-docx/package.json) (source: github_api): "private": true,     "name": "@types/html-to-docx",     "version": "1.8.9999",

### 151. ZUGFeRD/mustangapi

**Repository / product**

- Repository: [https://github.com/zugferd/mustangapi](https://github.com/zugferd/mustangapi)
- Company: Unknown — not stated in the repository
- Product: mustangAPI
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 15/100 (a score, not a probability)
- Raw weighted score: 0.75 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage | 4 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Pipeline complexity: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `Apache PDFBox`, run `run_2`, window `size:2001..4000`, rank 15
  - Query: `"pdfbox" filename:pom.xml size:2001..4000`
  - Sampled 30 of 6,672 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 6,672 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Apache PDFBox` (pdf, generation) — manifest_declaration — [pom.xml](https://github.com/ZUGFeRD/mustangapi/blob/master/pom.xml)

**Evidence trail**

- [api_response](https://github.com/ZUGFeRD/mustangapi) (source: github_api): stars=9, fork=False, archived=False
- [manifest_line](https://github.com/ZUGFeRD/mustangapi/blob/master/pom.xml) (source: github_api): <groupId>org.apache.pdfbox</groupId>
- [readme_excerpt](https://github.com/ZUGFeRD/mustangapi/blob/master/README.md) (source: readme): Access http://localhost:8080/swagger.yaml to build your clients.

### 152. jimmymnt/pim-e-shop

**Repository / product**

- Repository: [https://github.com/jimmymnt/pim-e-shop](https://github.com/jimmymnt/pim-e-shop)
- Company: Unknown — not stated in the repository
- Product: Demo and Blue Print Application for Pimcore
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 14/100 (a score, not a probability)
- Raw weighted score: 0.70 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 26
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 26
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/jimmymnt/pim-e-shop/blob/main/docker-compose.yaml)

**Evidence trail**

- [api_response](https://github.com/jimmymnt/pim-e-shop) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/jimmymnt/pim-e-shop/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/jimmymnt/pim-e-shop/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/jimmymnt/pim-e-shop/blob/main/README.md) (source: readme): This demo package is intended to be used by Pimcore newcomers who want to learn Pimcore and see it in action.
- [api_response](https://github.com/jimmymnt/pim-e-shop) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/jimmymnt/pim-e-shop/blob/main/docker-compose.yaml) (source: github_api): services:     redis:         image: redis:alpine         command: [ redis-server, --maxmemory, 128mb, --maxmemory-policy, volatile-lru, --save, '""' ]     db:         image: mariadb:10.11         wor
- [code_permalink](https://github.com/jimmymnt/pim-e-shop/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/jimmymnt/pim-e-shop/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/jimmymnt/pim-e-shop/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/jimmymnt/pim-e-shop/blob/main/README.md) (source: readme): This demo package is intended to be used by Pimcore newcomers who want to learn Pimcore and see it in action.

### 153. CoJoA13/EasySynQ

**Repository / product**

- Repository: [https://github.com/cojoa13/easysynq](https://github.com/cojoa13/easysynq)
- Company: Unknown — not stated in the repository
- Product: EasySynQ
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 14/100 (a score, not a probability)
- Raw weighted score: 0.70 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Apache Tika`, run `run_2`, window `size:2001..4000`, rank 28
  - Query: `"tika" filename:pyproject.toml size:2001..4000`
  - Retrieved 30 of 115 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/CoJoA13/EasySynQ/blob/17378211da31626c39d437d77ea813b9cdc45570/apps/api/src/easysynq_api/services/ingestion/extractor_tika.py)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/CoJoA13/EasySynQ/blob/17378211da31626c39d437d77ea813b9cdc45570/apps/api/src/easysynq_api/domain/diff/__init__.py)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/CoJoA13/EasySynQ/blob/17378211da31626c39d437d77ea813b9cdc45570/apps/api/src/easysynq_api/services/diff/extractor.py)

**Evidence trail**

- [api_response](https://github.com/CoJoA13/EasySynQ) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/CoJoA13/EasySynQ/blob/17378211da31626c39d437d77ea813b9cdc45570/apps/api/src/easysynq_api/services/ingestion/extractor_tika.py) (source: github_api): """The v1 ``ExtractorProvider`` — an Apache Tika ``-full`` HTTP sidecar (slice S-ing-2, doc 09 §5). ``TikaExtractorProvider`` is the §3.4 ExtractorProvider implementation: it PUTs the staged bytes to
- [code_permalink](https://github.com/CoJoA13/EasySynQ/blob/17378211da31626c39d437d77ea813b9cdc45570/apps/api/src/easysynq_api/domain/diff/__init__.py) (source: github_api): ``diff_metadata`` compares two versions' frozen ``metadata_snapshot`` field-by-field; ``redline`` produces an inline text redline (line-level LCS via stdlib ``difflib``) of two extracted texts. The s
- [code_permalink](https://github.com/CoJoA13/EasySynQ/blob/17378211da31626c39d437d77ea813b9cdc45570/apps/api/src/easysynq_api/services/diff/extractor.py) (source: github_api): Diff text is extracted **on-demand** from each version's WORM-immutable source blob (no per-version text is persisted; a cache is a v1.x optimization). The default extractor reuses the S-ing-2 Tika `
- [readme_excerpt](https://github.com/CoJoA13/EasySynQ/blob/main/README.md) (source: readme): **A self-hosted ISO 9001:2015 Quality Management System where document drift is engineered out, not policed.** EasySynQ runs your quality system on your own server, in the browser — and answers the on

### 154. Simon-Drohsen/pimcore-certificate

**Repository / product**

- Repository: [https://github.com/simon-drohsen/pimcore-certificate](https://github.com/simon-drohsen/pimcore-certificate)
- Company: Unknown — not stated in the repository
- Product: Demo and Blue Print Application for Pimcore
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 14/100 (a score, not a probability)
- Raw weighted score: 0.70 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 23
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 23
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/Simon-Drohsen/pimcore-certificate/blob/main/docker-compose.yaml)

**Evidence trail**

- [api_response](https://github.com/Simon-Drohsen/pimcore-certificate) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/Simon-Drohsen/pimcore-certificate/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/Simon-Drohsen/pimcore-certificate/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/Simon-Drohsen/pimcore-certificate/blob/main/README.md) (source: readme): This demo package is intended to be used by Pimcore newcomers who want to learn Pimcore and see it in action.
- [api_response](https://github.com/Simon-Drohsen/pimcore-certificate) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/Simon-Drohsen/pimcore-certificate/blob/main/docker-compose.yaml) (source: github_api): services:     redis:         image: redis:alpine         command: [ redis-server, --maxmemory, 128mb, --maxmemory-policy, volatile-lru, --save, '""' ]     db:         image: mariadb:10.11         wor
- [code_permalink](https://github.com/Simon-Drohsen/pimcore-certificate/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/Simon-Drohsen/pimcore-certificate/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/Simon-Drohsen/pimcore-certificate/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/Simon-Drohsen/pimcore-certificate/blob/main/README.md) (source: readme): This demo package is intended to be used by Pimcore newcomers who want to learn Pimcore and see it in action.

### 155. WPI-LNL/lnldb

**Repository / product**

- Repository: [https://github.com/wpi-lnl/lnldb](https://github.com/wpi-lnl/lnldb)
- Company: Unknown — not stated in the repository
- Product: LNLDB
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 14/100 (a score, not a probability)
- Raw weighted score: 0.70 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `pypdf / PyPDF2`, run `run_2`, window `size:2001..4000`, rank 17
  - Query: `"pypdf" filename:requirements.txt size:2001..4000`
  - Sampled 30 of 15,616 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 15,616 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [requirements.txt](https://github.com/WPI-LNL/lnldb/blob/master/requirements.txt)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/WPI-LNL/lnldb/blob/d642e1698a2834a3ff299e028003840a01d070d8/pdfs/views.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/WPI-LNL/lnldb/blob/d642e1698a2834a3ff299e028003840a01d070d8/pdfs/utils.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/WPI-LNL/lnldb/blob/d642e1698a2834a3ff299e028003840a01d070d8/pdfs/overlay.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/WPI-LNL/lnldb/blob/d642e1698a2834a3ff299e028003840a01d070d8/pdfs/tests/test_views.py)

**Evidence trail**

- [api_response](https://github.com/WPI-LNL/lnldb) (source: github_api): stars=16, fork=False, archived=False
- [manifest_line](https://github.com/WPI-LNL/lnldb/blob/master/requirements.txt) (source: github_api): pypdf==5.1.0
- [code_permalink](https://github.com/WPI-LNL/lnldb/blob/d642e1698a2834a3ff299e028003840a01d070d8/pdfs/views.py) (source: github_api): from weasyprint.text.fonts import FontConfiguration except ModuleNotFoundError:     from weasyprint.fonts import FontConfiguration from pypdf import PdfWriter from events.models import Category,
- [code_permalink](https://github.com/WPI-LNL/lnldb/blob/d642e1698a2834a3ff299e028003840a01d070d8/pdfs/utils.py) (source: github_api): from io import BytesIO from PyPDF2 import PdfFileMerger def concat_pdf(*infiles, **kwargs):     if 'outfile' in kwargs:
- [code_permalink](https://github.com/WPI-LNL/lnldb/blob/d642e1698a2834a3ff299e028003840a01d070d8/pdfs/overlay.py) (source: github_api): import os.path from io import BytesIO from PyPDF2 import PdfFileReader, PdfFileWriter def get_base(name):
- [code_permalink](https://github.com/WPI-LNL/lnldb/blob/d642e1698a2834a3ff299e028003840a01d070d8/pdfs/tests/test_views.py) (source: github_api): from django.test import TestCase from django.utils import timezone from pypdf import PdfReader from io import BytesIO from events.tests.generators import EventFactory, Event2019Factory, UserFactory,
- [readme_excerpt](https://github.com/WPI-LNL/lnldb/blob/master/README.md) (source: readme): The most important are Python3 and virtualenv (which allows you to install python libs without root).

### 156. JanBancerewicz/pimcoretask

**Repository / product**

- Repository: [https://github.com/janbancerewicz/pimcoretask](https://github.com/janbancerewicz/pimcoretask)
- Company: Unknown — not stated in the repository
- Product: Pimcore Product Management Demo
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 14/100 (a score, not a probability)
- Raw weighted score: 0.70 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 29
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 29
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/JanBancerewicz/pimcoretask/blob/main/docker-compose.yaml)

**Evidence trail**

- [api_response](https://github.com/JanBancerewicz/pimcoretask) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/JanBancerewicz/pimcoretask/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/JanBancerewicz/pimcoretask/tree/main/templates) (source: github_api): directory templates/ present
- [api_response](https://github.com/JanBancerewicz/pimcoretask) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/JanBancerewicz/pimcoretask/blob/main/docker-compose.yaml) (source: github_api): services:     redis:         image: redis:alpine         command: [ redis-server, --maxmemory, 128mb, --maxmemory-policy, volatile-lru, --save, '""' ]         volumes:             - pimcore-demo-redis
- [code_permalink](https://github.com/JanBancerewicz/pimcoretask/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/JanBancerewicz/pimcoretask/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/JanBancerewicz/pimcoretask/tree/main/templates) (source: github_api): directory templates/ present

### 157. datnv41001/pimcore

**Repository / product**

- Repository: [https://github.com/datnv41001/pimcore](https://github.com/datnv41001/pimcore)
- Company: Unknown — not stated in the repository
- Product: Demo and Blue Print Application for Pimcore
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 14/100 (a score, not a probability)
- Raw weighted score: 0.70 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 30
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 30
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/datnv41001/pimcore/blob/main/docker-compose.yaml)

**Evidence trail**

- [api_response](https://github.com/datnv41001/pimcore) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/datnv41001/pimcore/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/datnv41001/pimcore/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/datnv41001/pimcore/blob/main/README.md) (source: readme): This demo package is intended to be used by Pimcore newcomers who want to learn Pimcore and see it in action.
- [api_response](https://github.com/datnv41001/pimcore) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/datnv41001/pimcore/blob/main/docker-compose.yaml) (source: github_api): services:     redis:         image: redis:alpine         command: [ redis-server, --maxmemory, 128mb, --maxmemory-policy, volatile-lru, --save, '""' ]         volumes:             - pimcore-demo-redis
- [code_permalink](https://github.com/datnv41001/pimcore/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/datnv41001/pimcore/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/datnv41001/pimcore/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/datnv41001/pimcore/blob/main/README.md) (source: readme): This demo package is intended to be used by Pimcore newcomers who want to learn Pimcore and see it in action.

### 158. LevDmitriev/dc-pimcore-demo

**Repository / product**

- Repository: [https://github.com/levdmitriev/dc-pimcore-demo](https://github.com/levdmitriev/dc-pimcore-demo)
- Company: Unknown — not stated in the repository
- Product: Demo and Blue Print Application for Pimcore
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 14/100 (a score, not a probability)
- Raw weighted score: 0.70 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 28
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 28
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/LevDmitriev/dc-pimcore-demo/blob/master/docker-compose.yaml)

**Evidence trail**

- [api_response](https://github.com/LevDmitriev/dc-pimcore-demo) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/LevDmitriev/dc-pimcore-demo/blob/master/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/LevDmitriev/dc-pimcore-demo/tree/master/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/LevDmitriev/dc-pimcore-demo/blob/master/README.md) (source: readme): This demo package is intended to be used by Pimcore newcomers who want to learn Pimcore and see it in action.
- [api_response](https://github.com/LevDmitriev/dc-pimcore-demo) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/LevDmitriev/dc-pimcore-demo/blob/master/docker-compose.yaml) (source: github_api): services:     redis:         image: redis:alpine         command: [ redis-server, --maxmemory, 128mb, --maxmemory-policy, volatile-lru, --save, '""' ]         volumes:             - pimcore-demo-redis
- [code_permalink](https://github.com/LevDmitriev/dc-pimcore-demo/blob/master/docker-compose.yaml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/LevDmitriev/dc-pimcore-demo/blob/master/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/LevDmitriev/dc-pimcore-demo/tree/master/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/LevDmitriev/dc-pimcore-demo/blob/master/README.md) (source: readme): This demo package is intended to be used by Pimcore newcomers who want to learn Pimcore and see it in action.

### 159. vivliostyle/vivliostyle-cli

**Repository / product**

- Repository: [https://github.com/vivliostyle/vivliostyle-cli](https://github.com/vivliostyle/vivliostyle-cli)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://docs.vivliostyle.org/cli/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 14/100 (a score, not a probability)
- Raw weighted score: 0.70 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 19
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 19
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/vivliostyle/vivliostyle-cli/blob/main/Dockerfile)

**Evidence trail**

- [api_response](https://github.com/vivliostyle/vivliostyle-cli) (source: github_api): stars=230, fork=False, archived=False
- [code_permalink](https://github.com/vivliostyle/vivliostyle-cli/blob/main/Dockerfile) (source: github_api): # - https://github.com/gotenberg/gotenberg/blob/main/build/Dockerfile
- [other](https://github.com/vivliostyle/vivliostyle-cli/tree/main/templates) (source: github_api): directory templates/ present
- [api_response](https://github.com/vivliostyle/vivliostyle-cli) (source: github_api): stars=230, fork=False, archived=False
- [code_permalink](https://github.com/vivliostyle/vivliostyle-cli/blob/main/Dockerfile) (source: github_api): # References: # - https://github.com/gotenberg/gotenberg/blob/main/build/Dockerfile # - https://github.com/microsoft/playwright/blob/main/utils/docker/Dockerfile.noble FROM debian:13-slim AS base AR
- [code_permalink](https://github.com/vivliostyle/vivliostyle-cli/blob/main/Dockerfile) (source: github_api): # - https://github.com/gotenberg/gotenberg/blob/main/build/Dockerfile
- [code_permalink](https://github.com/vivliostyle/vivliostyle-cli/blob/main/Dockerfile) (source: github_api): # - https://github.com/gotenberg/gotenberg/blob/main/build/Dockerfile
- [other](https://github.com/vivliostyle/vivliostyle-cli/tree/main/templates) (source: github_api): directory templates/ present

### 160. l4houx/recipe

**Repository / product**

- Repository: [https://github.com/l4houx/recipe](https://github.com/l4houx/recipe)
- Company: Unknown — not stated in the repository
- Product: En cours
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 14/100 (a score, not a probability)
- Raw weighted score: 0.70 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 16
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 16
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/l4houx/recipe/blob/main/docker-compose.yaml)

**Evidence trail**

- [api_response](https://github.com/l4houx/recipe) (source: github_api): stars=3, fork=False, archived=False
- [code_permalink](https://github.com/l4houx/recipe/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/l4houx/recipe/tree/main/templates) (source: github_api): directory templates/ present
- [api_response](https://github.com/l4houx/recipe) (source: github_api): stars=3, fork=False, archived=False
- [code_permalink](https://github.com/l4houx/recipe/blob/main/docker-compose.yaml) (source: github_api): version: '3.8' services:     nginx:         image: nginx:1.22-alpine         ports:             - 89:80         volumes:             - ./:/code             - ./nginx.conf:/etc/nginx/nginx.conf
- [code_permalink](https://github.com/l4houx/recipe/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/l4houx/recipe/blob/main/docker-compose.yaml) (source: github_api): gotenberg:
- [other](https://github.com/l4houx/recipe/tree/main/templates) (source: github_api): directory templates/ present

### 161. engine-public/engine-partner-api

**Repository / product**

- Repository: [https://github.com/engine-public/engine-partner-api](https://github.com/engine-public/engine-partner-api)
- Company: Unknown — not stated in the repository
- Product: Omni, Powered by Engine
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://omni.engine.com

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 14/100 (a score, not a probability)
- Raw weighted score: 0.70 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Pipeline complexity: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `Apache Tika`, run `run_2`, window `size:>16000`, rank 26
  - Query: `"tika" filename:build.gradle size:>16000`
  - Retrieved 30 of 148 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache Tika` (other_processing, extraction) — manifest_declaration — [build.gradle.kts](https://github.com/engine-public/engine-partner-api/blob/main/build.gradle.kts)

**Evidence trail**

- [api_response](https://github.com/engine-public/engine-partner-api) (source: github_api): stars=4, fork=False, archived=False
- [manifest_line](https://github.com/engine-public/engine-partner-api/blob/main/build.gradle.kts) (source: github_api): classpath("org.apache.tika:tika-core:3.2.2") {
- [readme_excerpt](https://github.com/engine-public/engine-partner-api/blob/main/README.md) (source: readme): The Omni API is ideal for businesses looking to: **Provide travel to their users as a first-time offering** **Integrate Omni as a new lodging partner** into their existing travel booking platform.

### 162. PrimaverabssDeveloper/ERP10Extensibility

**Repository / product**

- Repository: [https://github.com/primaverabssdeveloper/erp10extensibility](https://github.com/primaverabssdeveloper/erp10extensibility)
- Company: Unknown — not stated in the repository
- Product: Extensibility
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| supporting: confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 13/100 (a score, not a probability)
- Raw weighted score: 0.65 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `iText`, run `run_2`, window `size:>16000`, rank 7
  - Query: `"itext" filename:packages.config size:>16000`
  - Retrieved 9 of 9 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `iText` (pdf, generation) — code_import — [code](https://github.com/PrimaverabssDeveloper/ERP10Extensibility/blob/7975fb8d27f0863e9a76cb90cfbf7dfc1538d867/samples/OMNIA Procurement/Primavera.TemplateProcurement.Extensibility/Primavera.TemplateProcurement.Extensibility/UI/frmParametrosOMNIA.cs)
- `iText` (pdf, generation) — manifest_declaration — [Implementation/GeolocationExtension/packages.config](https://github.com/PrimaverabssDeveloper/ERP10Extensibility/blob/7975fb8d27f0863e9a76cb90cfbf7dfc1538d867/Implementation/GeolocationExtension/packages.config)
- `iText` (pdf, generation) — manifest_declaration — [Implementation/GeolocationExtension/Primavera.Platform.Geolocation.csproj](https://github.com/PrimaverabssDeveloper/ERP10Extensibility/blob/7975fb8d27f0863e9a76cb90cfbf7dfc1538d867/Implementation/GeolocationExtension/Primavera.Platform.Geolocation.csproj)
- `iText` (pdf, generation) — code_import — [code](https://github.com/PrimaverabssDeveloper/ERP10Extensibility/blob/7975fb8d27f0863e9a76cb90cfbf7dfc1538d867/samples/Custom Tabs/Primavera.Base.CustomTabs/Customer/CustomerFields.Designer.cs)
- `iText` (pdf, generation) — code_import — [code](https://github.com/PrimaverabssDeveloper/ERP10Extensibility/blob/7975fb8d27f0863e9a76cb90cfbf7dfc1538d867/samples/OMNIA Procurement/Primavera.TemplateProcurement.Extensibility/Primavera.TemplateProcurement.Extensibility/UI/frmParametrosOMNIA.Designer.cs)

**Evidence trail**

- [api_response](https://github.com/PrimaverabssDeveloper/ERP10Extensibility) (source: github_api): stars=23, fork=False, archived=False
- [code_permalink](https://github.com/PrimaverabssDeveloper/ERP10Extensibility/blob/7975fb8d27f0863e9a76cb90cfbf7dfc1538d867/samples/OMNIA Procurement/Primavera.TemplateProcurement.Extensibility/Primavera.TemplateProcurement.Extensibility/UI/frmParametrosOMNIA.cs) (source: github_api): endpointApiTextBox.Text = parametros.EndpointApi;                 endpointIdentityTextBox.Text = parametros.EndpointIdentity;
- [manifest_line](https://github.com/PrimaverabssDeveloper/ERP10Extensibility/blob/7975fb8d27f0863e9a76cb90cfbf7dfc1538d867/Implementation/GeolocationExtension/packages.config) (source: github_api): <package id="Primavera.Platform.UserControls100" version="10.10.0.2525" targetFramework="net471" />   <package id="PrimaveraSupportNetSupport" version="10.0010.0000.2502" targetFramework="net471" />
- [manifest_line](https://github.com/PrimaverabssDeveloper/ERP10Extensibility/blob/7975fb8d27f0863e9a76cb90cfbf7dfc1538d867/Implementation/GeolocationExtension/Primavera.Platform.Geolocation.csproj) (source: github_api): <Reference Include="PrimaveraSupportNetSupport, Version=10.0.0.0, Culture=neutral, PublicKeyToken=11cd844aca152173, processorArchitecture=MSIL">       <HintPath>..\..\..\packages\PrimaveraSupportN
- [code_permalink](https://github.com/PrimaverabssDeveloper/ERP10Extensibility/blob/7975fb8d27f0863e9a76cb90cfbf7dfc1538d867/samples/Custom Tabs/Primavera.Base.CustomTabs/Customer/CustomerFields.Designer.cs) (source: github_api): this.label5 = new System.Windows.Forms.Label();             this.CDU_GLNFornecedor = new Primavera.Platform.Extensibility.Controls.PriTextEdit();             this.ManualCDU.SuspendLayout()
- [code_permalink](https://github.com/PrimaverabssDeveloper/ERP10Extensibility/blob/7975fb8d27f0863e9a76cb90cfbf7dfc1538d867/samples/OMNIA Procurement/Primavera.TemplateProcurement.Extensibility/Primavera.TemplateProcurement.Extensibility/UI/frmParametrosOMNIA.Designer.cs) (source: github_api): this.endpointIdentityTextBox = new System.Windows.Forms.TextBox();             this.endpointApiTextBox = new System.Windows.Forms.TextBox();             this.label1 = new System.Windows.Fo
- [readme_excerpt](https://github.com/PrimaverabssDeveloper/ERP10Extensibility/blob/master/README.md) (source: readme): In this repository you will find information and code samples that allows you to understand how to use PRIMAVERA extensibility technology.

### 163. networktocode/yangify

**Repository / product**

- Repository: [https://github.com/networktocode/yangify](https://github.com/networktocode/yangify)
- Company: Unknown — not stated in the repository
- Product: Yangify
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| supporting: confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 13/100 (a score, not a probability)
- Raw weighted score: 0.65 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Pandoc`, run `run_1`, window `unsliced`, rank 10
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `Pandoc`, run `run_2`, window `unsliced`, rank 10
  - Query: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Pandoc` (conversion, conversion) — infrastructure_reference — [code](https://github.com/networktocode/yangify/blob/develop/Dockerfile)

**Evidence trail**

- [api_response](https://github.com/networktocode/yangify) (source: github_api): stars=117, fork=False, archived=False
- [code_permalink](https://github.com/networktocode/yangify/blob/develop/Dockerfile) (source: github_api): RUN apt-get update && apt-get install -y pandoc
- [readme_excerpt](https://github.com/networktocode/yangify/blob/develop/README.md) (source: readme): Yangify is a framework that allows you to easily write code that can map structured and unstructured data into data modelled using YANG models.
- [api_response](https://github.com/networktocode/yangify) (source: github_api): stars=117, fork=False, archived=False
- [code_permalink](https://github.com/networktocode/yangify/blob/develop/Dockerfile) (source: github_api): ARG PYTHON FROM python:${PYTHON}-stretch RUN apt-get update && apt-get install -y pandoc RUN pip install poetry==1.0.0 && poetry config virtualenvs.create false && pip install -U pip ADD poetry.lo
- [code_permalink](https://github.com/networktocode/yangify/blob/develop/Dockerfile) (source: github_api): RUN apt-get update && apt-get install -y pandoc
- [code_permalink](https://github.com/networktocode/yangify/blob/develop/Dockerfile) (source: github_api): RUN apt-get update && apt-get install -y pandoc
- [readme_excerpt](https://github.com/networktocode/yangify/blob/develop/README.md) (source: readme): Yangify is a framework that allows you to easily write code that can map structured and unstructured data into data modelled using YANG models.

### 164. gitrgoliveira/bracket-creator

**Repository / product**

- Repository: [https://github.com/gitrgoliveira/bracket-creator](https://github.com/gitrgoliveira/bracket-creator)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: events_weddings (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://gitrgoliveira.github.io/bracket-creator/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: contributor_count not collected

**Score**

- Score: 13/100 (a score, not a probability)
- Raw weighted score: 0.65 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 15
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 15
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [code](https://github.com/gitrgoliveira/bracket-creator/blob/main/docker-compose.yaml)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/gitrgoliveira/bracket-creator/blob/d466bc5245f10d53d545a38bc4e96787b4e0e853/cmd/print.go)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/gitrgoliveira/bracket-creator/blob/d466bc5245f10d53d545a38bc4e96787b4e0e853/internal/pdf/soffice.go)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/gitrgoliveira/bracket-creator/blob/d466bc5245f10d53d545a38bc4e96787b4e0e853/internal/mobileapp/handlers_print.go)

**Evidence trail**

- [api_response](https://github.com/gitrgoliveira/bracket-creator) (source: github_api): stars=3, fork=False, archived=False
- [code_permalink](https://github.com/gitrgoliveira/bracket-creator/blob/main/docker-compose.yaml) (source: github_api): # WARNING: pulls in LibreOffice headless (~500 MB+), do NOT enable unless
- [code_permalink](https://github.com/gitrgoliveira/bracket-creator/blob/d466bc5245f10d53d545a38bc4e96787b4e0e853/cmd/print.go) (source: github_api): Long: `Render the sheets of one or more bracket XLSX workbooks into grouped, print-ready PDFs using LibreOffice.
- [code_permalink](https://github.com/gitrgoliveira/bracket-creator/blob/d466bc5245f10d53d545a38bc4e96787b4e0e853/internal/pdf/soffice.go) (source: github_api): // // LibreOffice (soffice) is a runtime dependency. It is NOT bundled. Callers // detect availability with LocateSoffice and surface an actionable error when
- [code_permalink](https://github.com/gitrgoliveira/bracket-creator/blob/d466bc5245f10d53d545a38bc4e96787b4e0e853/internal/mobileapp/handlers_print.go) (source: github_api): // // The handler is synchronous, PDF generation via LibreOffice takes 30–60 s // for a typical tournament. That is acceptable for an admin-initiated,
- [api_response](https://github.com/gitrgoliveira/bracket-creator) (source: github_api): stars=3, fork=False, archived=False
- [code_permalink](https://github.com/gitrgoliveira/bracket-creator/blob/main/docker-compose.yaml) (source: github_api): version: '3.8' services:   # Stateless bracket creator generator web GUI   bracket-creator:     build: .     image: ghcr.io/gitrgoliveira/bracket-creator:${VERSION:-latest}     environment:       - B
- [code_permalink](https://github.com/gitrgoliveira/bracket-creator/blob/main/docker-compose.yaml) (source: github_api): # WARNING: pulls in LibreOffice headless (~500 MB+), do NOT enable unless
- [code_permalink](https://github.com/gitrgoliveira/bracket-creator/blob/main/docker-compose.yaml) (source: github_api): # WARNING: pulls in LibreOffice headless (~500 MB+), do NOT enable unless
- [code_permalink](https://github.com/gitrgoliveira/bracket-creator/blob/d466bc5245f10d53d545a38bc4e96787b4e0e853/cmd/print.go) (source: github_api): Long: `Render the sheets of one or more bracket XLSX workbooks into grouped, print-ready PDFs using LibreOffice.
- [code_permalink](https://github.com/gitrgoliveira/bracket-creator/blob/d466bc5245f10d53d545a38bc4e96787b4e0e853/internal/pdf/soffice.go) (source: github_api): // // LibreOffice (soffice) is a runtime dependency. It is NOT bundled. Callers // detect availability with LocateSoffice and surface an actionable error when
- [code_permalink](https://github.com/gitrgoliveira/bracket-creator/blob/d466bc5245f10d53d545a38bc4e96787b4e0e853/internal/mobileapp/handlers_print.go) (source: github_api): // // The handler is synchronous, PDF generation via LibreOffice takes 30–60 s // for a typical tournament. That is acceptable for an admin-initiated,

### 165. getumbrel/umbrel-apps

**Repository / product**

- Repository: [https://github.com/getumbrel/umbrel-apps](https://github.com/getumbrel/umbrel-apps)
- Company: Unknown — not stated in the repository
- Product: Umbrel App Store Packages
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://apps.umbrel.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 13/100 (a score, not a probability)
- Raw weighted score: 0.65 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 2
  - Query: `"libreoffice" filename:docker-compose.yml`
  - Retrieved 30 of 466 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 7
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 2
  - Query: `"libreoffice" filename:docker-compose.yml`
  - Retrieved 30 of 466 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 7
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [paperless/docker-compose.yml](https://github.com/getumbrel/umbrel-apps/blob/master/paperless/docker-compose.yml)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [libreoffice/docker-compose.yml](https://github.com/getumbrel/umbrel-apps/blob/master/libreoffice/docker-compose.yml)

**Evidence trail**

- [api_response](https://github.com/getumbrel/umbrel-apps) (source: github_api): stars=766, fork=False, archived=False
- [readme_excerpt](https://github.com/getumbrel/umbrel-apps/blob/master/README.md) (source: readme): That file helps the agent choose the right repo-local skill for the work: packaging an existing app, updating an App Store package, testing a package, or building a self-hosted app that can be package
- [api_response](https://github.com/getumbrel/umbrel-apps) (source: github_api): stars=766, fork=False, archived=False
- [code_permalink](https://github.com/getumbrel/umbrel-apps/blob/master/libreoffice/docker-compose.yml) (source: github_api): version: "3.7" services:   app_proxy:     environment:       APP_HOST: libreoffice_server_1       APP_PORT: 3000   server:     image: linuxserver/libreoffice:7.6.7@sha256:a62c7f094f2a7ed8145983d04f5
- [code_permalink](https://github.com/getumbrel/umbrel-apps/blob/master/paperless/docker-compose.yml) (source: github_api): version: "3.7" services:   app_proxy:     environment:       APP_HOST: paperless_webserver_1       APP_PORT: 8000       PROXY_AUTH_ADD: 'false'   broker:     image: docker.io/library/redis:7@sha256:
- [readme_excerpt](https://github.com/getumbrel/umbrel-apps/blob/master/README.md) (source: readme): That file helps the agent choose the right repo-local skill for the work: packaging an existing app, updating an App Store package, testing a package, or building a self-hosted app that can be package
- [api_response](https://github.com/getumbrel/umbrel-apps) (source: github_api): stars=766, fork=False, archived=False
- [code_permalink](https://github.com/getumbrel/umbrel-apps/blob/master/libreoffice/docker-compose.yml) (source: github_api): version: "3.7" services:   app_proxy:     environment:       APP_HOST: libreoffice_server_1       APP_PORT: 3000   server:     image: linuxserver/libreoffice:7.6.7@sha256:a62c7f094f2a7ed8145983d04f5
- [code_permalink](https://github.com/getumbrel/umbrel-apps/blob/master/paperless/docker-compose.yml) (source: github_api): version: "3.7" services:   app_proxy:     environment:       APP_HOST: paperless_webserver_1       APP_PORT: 8000       PROXY_AUTH_ADD: 'false'   broker:     image: docker.io/library/redis:7@sha256:
- [manifest_line](https://github.com/getumbrel/umbrel-apps/blob/master/paperless/docker-compose.yml) (source: github_api): - gotenberg
- [manifest_line](https://github.com/getumbrel/umbrel-apps/blob/master/libreoffice/docker-compose.yml) (source: github_api): APP_HOST: libreoffice_server_1
- [readme_excerpt](https://github.com/getumbrel/umbrel-apps/blob/master/README.md) (source: readme): That file helps the agent choose the right repo-local skill for the work: packaging an existing app, updating an App Store package, testing a package, or building a self-hosted app that can be package
- [api_response](https://github.com/getumbrel/umbrel-apps) (source: github_api): stars=766, fork=False, archived=False
- [code_permalink](https://github.com/getumbrel/umbrel-apps/blob/master/libreoffice/docker-compose.yml) (source: github_api): version: "3.7" services:   app_proxy:     environment:       APP_HOST: libreoffice_server_1       APP_PORT: 3000   server:     image: linuxserver/libreoffice:7.6.7@sha256:a62c7f094f2a7ed8145983d04f5
- [code_permalink](https://github.com/getumbrel/umbrel-apps/blob/master/paperless/docker-compose.yml) (source: github_api): version: "3.7" services:   app_proxy:     environment:       APP_HOST: paperless_webserver_1       APP_PORT: 8000       PROXY_AUTH_ADD: 'false'   broker:     image: docker.io/library/redis:7@sha256:
- [manifest_line](https://github.com/getumbrel/umbrel-apps/blob/master/paperless/docker-compose.yml) (source: github_api): - gotenberg
- [manifest_line](https://github.com/getumbrel/umbrel-apps/blob/master/libreoffice/docker-compose.yml) (source: github_api): APP_HOST: libreoffice_server_1
- [readme_excerpt](https://github.com/getumbrel/umbrel-apps/blob/master/README.md) (source: readme): That file helps the agent choose the right repo-local skill for the work: packaging an existing app, updating an App Store package, testing a package, or building a self-hosted app that can be package

### 166. Paparusi/legal-ai-agent

**Repository / product**

- Repository: [https://github.com/paparusi/legal-ai-agent](https://github.com/paparusi/legal-ai-agent)
- Company: Unknown — not stated in the repository
- Product: ⚖️ AI Legal Agent
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: contributor_count not collected

**Score**

- Score: 13/100 (a score, not a probability)
- Raw weighted score: 0.65 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 21
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 21
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [code](https://github.com/Paparusi/legal-ai-agent/blob/main/Dockerfile)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/Paparusi/legal-ai-agent/blob/7d6de9580ccb1e4ac27bea4315ba6f77fdd349ed/src/services/libreoffice_editor.py)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/Paparusi/legal-ai-agent/blob/7d6de9580ccb1e4ac27bea4315ba6f77fdd349ed/src/api/main.py)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/Paparusi/legal-ai-agent/blob/7d6de9580ccb1e4ac27bea4315ba6f77fdd349ed/test_libreoffice.py)

**Evidence trail**

- [api_response](https://github.com/Paparusi/legal-ai-agent) (source: github_api): stars=200, fork=False, archived=False
- [code_permalink](https://github.com/Paparusi/legal-ai-agent/blob/main/Dockerfile) (source: github_api): # Install system dependencies (including LibreOffice for DOCX editing)
- [code_permalink](https://github.com/Paparusi/legal-ai-agent/blob/7d6de9580ccb1e4ac27bea4315ba6f77fdd349ed/src/services/libreoffice_editor.py) (source: github_api): Uses LibreOffice CLI in headless mode for find/replace operations. Falls back to python-docx if LibreOffice is not available. """
- [code_permalink](https://github.com/Paparusi/legal-ai-agent/blob/7d6de9580ccb1e4ac27bea4315ba6f77fdd349ed/src/api/main.py) (source: github_api): async def preview_document(doc_id: str, company: dict = Depends(verify_api_key)):     """Convert DOCX to PDF for web preview using LibreOffice"""     from pathlib import Path
- [code_permalink](https://github.com/Paparusi/legal-ai-agent/blob/7d6de9580ccb1e4ac27bea4315ba6f77fdd349ed/test_libreoffice.py) (source: github_api): """Test LibreOffice editor integration""" from src.services.libreoffice_editor import find_libreoffice, edit_docx, convert_to_pdf import os print("Testing LibreOffice integration...\n") print("1. Ch
- [api_response](https://github.com/Paparusi/legal-ai-agent) (source: github_api): stars=200, fork=False, archived=False
- [code_permalink](https://github.com/Paparusi/legal-ai-agent/blob/main/Dockerfile) (source: github_api): FROM python:3.11-slim WORKDIR /app # Install system dependencies (including LibreOffice for DOCX editing) RUN apt-get update && apt-get install -y --no-install-recommends \     libpq-dev gcc curl li
- [code_permalink](https://github.com/Paparusi/legal-ai-agent/blob/main/Dockerfile) (source: github_api): # Install system dependencies (including LibreOffice for DOCX editing)
- [code_permalink](https://github.com/Paparusi/legal-ai-agent/blob/main/Dockerfile) (source: github_api): # Install system dependencies (including LibreOffice for DOCX editing)
- [code_permalink](https://github.com/Paparusi/legal-ai-agent/blob/7d6de9580ccb1e4ac27bea4315ba6f77fdd349ed/src/services/libreoffice_editor.py) (source: github_api): Uses LibreOffice CLI in headless mode for find/replace operations. Falls back to python-docx if LibreOffice is not available. """
- [code_permalink](https://github.com/Paparusi/legal-ai-agent/blob/7d6de9580ccb1e4ac27bea4315ba6f77fdd349ed/src/api/main.py) (source: github_api): async def preview_document(doc_id: str, company: dict = Depends(verify_api_key)):     """Convert DOCX to PDF for web preview using LibreOffice"""     from pathlib import Path
- [code_permalink](https://github.com/Paparusi/legal-ai-agent/blob/7d6de9580ccb1e4ac27bea4315ba6f77fdd349ed/test_libreoffice.py) (source: github_api): """Test LibreOffice editor integration""" from src.services.libreoffice_editor import find_libreoffice, edit_docx, convert_to_pdf import os print("Testing LibreOffice integration...\n") print("1. Ch

### 167. LazyAGI/LazyLLM

**Repository / product**

- Repository: [https://github.com/lazyagi/lazyllm](https://github.com/lazyagi/lazyllm)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://docs.lazyllm.ai/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2 \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 12/100 (a score, not a probability)
- Raw weighted score: 0.60 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 2 |
| Business criticality | 0 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `pypdf / PyPDF2`, run `run_2`, window `size:8001..16000`, rank 14
  - Query: `"pypdf" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 594 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `python-docx`, run `run_2`, window `size:8001..16000`, rank 12
  - Query: `"python-docx" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 486 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [pyproject.toml](https://github.com/LazyAGI/LazyLLM/blob/main/pyproject.toml)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [requirements.txt](https://github.com/LazyAGI/LazyLLM/blob/main/requirements.txt)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/LazyAGI/LazyLLM/blob/9d28284bac867f7429f77ed7107024b15bf5093f/lazyllm/tools/rag/readers/pdfReader.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/LazyAGI/LazyLLM/blob/9d28284bac867f7429f77ed7107024b15bf5093f/lazyllm/tools/rag/readers/ocrReader/ocr_reader_base.py)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [tests/requirements.txt](https://github.com/LazyAGI/LazyLLM/blob/9d28284bac867f7429f77ed7107024b15bf5093f/tests/requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [pyproject.toml](https://github.com/LazyAGI/LazyLLM/blob/main/pyproject.toml)
- `python-docx` (docx, generation) — manifest_declaration — [requirements.txt](https://github.com/LazyAGI/LazyLLM/blob/main/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/LazyAGI/LazyLLM) (source: github_api): stars=3871, fork=False, archived=False
- [manifest_line](https://github.com/LazyAGI/LazyLLM/blob/main/pyproject.toml) (source: github_api): pypdf = {version = "^5.0.0", optional = true}
- [manifest_line](https://github.com/LazyAGI/LazyLLM/blob/main/requirements.txt) (source: github_api): pypdf<=6.5.0
- [code_permalink](https://github.com/LazyAGI/LazyLLM/blob/9d28284bac867f7429f77ed7107024b15bf5093f/lazyllm/tools/rag/readers/pdfReader.py) (source: github_api): from lazyllm.common import retry from lazyllm.thirdparty import fsspec, pypdf from lazyllm import LOG
- [code_permalink](https://github.com/LazyAGI/LazyLLM/blob/9d28284bac867f7429f77ed7107024b15bf5093f/lazyllm/tools/rag/readers/ocrReader/ocr_reader_base.py) (source: github_api): from lazyllm import locals as lazyllm_locals from lazyllm.thirdparty import bs4, pypdf from lazyllm.common import AuthStrategy, BearerTokenStrategy, CredentialMixin
- [manifest_line](https://github.com/LazyAGI/LazyLLM/blob/9d28284bac867f7429f77ed7107024b15bf5093f/tests/requirements.txt) (source: github_api): pytest-cov rapidfuzz volcengine-python-sdk[ark]>=4.0.6 dashscope>=1.23.6 zhipuai>=2.1.5.20250708 huggingface-hub==0.35.3 pypdf<=6.5.0
- [manifest_line](https://github.com/LazyAGI/LazyLLM/blob/main/pyproject.toml) (source: github_api): python-docx = { version = ">=1.2.0,<2.0.0", optional = true }
- [manifest_line](https://github.com/LazyAGI/LazyLLM/blob/main/requirements.txt) (source: github_api): python-docx

### 168. sifter-ai/sifter

**Repository / product**

- Repository: [https://github.com/sifter-ai/sifter](https://github.com/sifter-ai/sifter)
- Company: Unknown — not stated in the repository
- Product: Sifter
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| unknown: contributor_count not collected

**Score**

- Score: 12/100 (a score, not a probability)
- Raw weighted score: 0.60 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:2001..4000`, rank 29
  - Query: `"mammoth" filename:pyproject.toml size:2001..4000`
  - Retrieved 30 of 163 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/sifter-ai/sifter/blob/162347f29c49a304901c25b2c6b1f4ce94635ff4/code/server/sifter/services/file_processor.py)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [code/server/pyproject.toml](https://github.com/sifter-ai/sifter/blob/162347f29c49a304901c25b2c6b1f4ce94635ff4/code/server/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/sifter-ai/sifter) (source: github_api): stars=55, fork=False, archived=False
- [code_permalink](https://github.com/sifter-ai/sifter/blob/162347f29c49a304901c25b2c6b1f4ce94635ff4/code/server/sifter/services/file_processor.py) (source: github_api): def _process_docx(self, data: bytes, filename: str) -> ProcessedFile:         import mammoth         result = mammoth.convert_to_markdown(io.BytesIO(data))         return ProcessedFile(
- [manifest_line](https://github.com/sifter-ai/sifter/blob/162347f29c49a304901c25b2c6b1f4ce94635ff4/code/server/pyproject.toml) (source: github_api): "slowapi>=0.1.9",     "email-validator>=2.1.0",     "google-auth>=2.29.0",     "mammoth>=1.8.0",     "beautifulsoup4>=4.12.0",     "markitdown[all]>=0.1.0",     "markitdown-ocr>=0.1.0",
- [readme_excerpt](https://github.com/sifter-ai/sifter/blob/main/README.md) (source: readme): ![Sifter demo](docs/images/sifter-demo.gif) RAG is built for retrieval — *find me chunks similar to this query*.

### 169. Ganesh-403/semantic-plagiarism-detector

**Repository / product**

- Repository: [https://github.com/ganesh-403/semantic-plagiarism-detector](https://github.com/ganesh-403/semantic-plagiarism-detector)
- Company: Unknown — not stated in the repository
- Product: 🔍 Semantic Plagiarism Detection System
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://semantic-plagiarism-detector.streamlit.app/

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: no dependency evidence located; company_name=null; contributor_count not collected

**Score**

- Score: 12/100 (a score, not a probability)
- Raw weighted score: 0.60 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown

**Discovery provenance**

- Tier 3, `(co-occurrence query, spans multiple libraries)`, run `run_2`, window `size:4001..8000`, rank 26
  - Query: `"python-docx" "reportlab" filename:requirements.txt size:4001..8000`
  - Retrieved 30 of 515 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/Ganesh-403/semantic-plagiarism-detector) (source: github_api): stars=15, fork=False, archived=False
- [readme_excerpt](https://github.com/Ganesh-403/semantic-plagiarism-detector/blob/main/README.md) (source: readme): **Generate or obtain TLS certificates** for your Redis server (CA certificate, and optionally a client certificate/key pair if you're using `tls-auth-clients yes` as described in `SECURITY.md`).

### 170. sitepoint-editors/awesome-symfony

**Repository / product**

- Repository: [https://github.com/sitepoint-editors/awesome-symfony](https://github.com/sitepoint-editors/awesome-symfony)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| unknown: no dependency evidence located; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 12/100 (a score, not a probability)
- Raw weighted score: 0.60 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 11
  - Query: `"unoconv"`
  - Sampled 30 of 17,216 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 17,216 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 11
  - Query: `"unoconv"`
  - Sampled 30 of 17,216 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 17,216 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/sitepoint-editors/awesome-symfony) (source: github_api): stars=1573, fork=False, archived=False
- [readme_excerpt](https://github.com/sitepoint-editors/awesome-symfony/blob/master/README.md) (source: readme): [Slack](https://symfony.com/slack-invite) - Symfony on Slack, platform for team communication.
- [api_response](https://github.com/sitepoint-editors/awesome-symfony) (source: github_api): stars=1573, fork=False, archived=False
- [readme_excerpt](https://github.com/sitepoint-editors/awesome-symfony/blob/master/README.md) (source: readme): [Slack](https://symfony.com/slack-invite) - Symfony on Slack, platform for team communication.
- [api_response](https://github.com/sitepoint-editors/awesome-symfony) (source: github_api): stars=1573, fork=False, archived=False
- [readme_excerpt](https://github.com/sitepoint-editors/awesome-symfony/blob/master/README.md) (source: readme): [Slack](https://symfony.com/slack-invite) - Symfony on Slack, platform for team communication.

### 171. dragonfore4/deka-download

**Repository / product**

- Repository: [https://github.com/dragonfore4/deka-download](https://github.com/dragonfore4/deka-download)
- Company: Unknown — not stated in the repository
- Product: DEKA Ptoey (ฎีกา ผู้ต่อ)
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 10
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 10
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/dragonfore4/deka-download/blob/main/docker-compose.yml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/dragonfore4/deka-download/blob/5fdb0344ee23fcf8253f923944a69453731aee32/config.ts)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/dragonfore4/deka-download/blob/5fdb0344ee23fcf8253f923944a69453731aee32/downloadDeka.ts)

**Evidence trail**

- [api_response](https://github.com/dragonfore4/deka-download) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/dragonfore4/deka-download/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/dragonfore4/deka-download/blob/5fdb0344ee23fcf8253f923944a69453731aee32/config.ts) (source: github_api): readonly DEKA_BASE_URL: string;   readonly DEKA_SEARCH_URL: string;   readonly DEKA_PRINT_URL: string;   readonly GOTENBERG_BASE_URL: string;   readonly GOTENBERG_HTML_URL: string;   // Concurrency
- [code_permalink](https://github.com/dragonfore4/deka-download/blob/5fdb0344ee23fcf8253f923944a69453731aee32/downloadDeka.ts) (source: github_api): } async function renderWithGotenberg(htmlContent: string, filePath: string) {   if (!config.ENABLE_GOTENBERG) {     throw new Error("Gotenberg is disabled in configuration");   }
- [api_response](https://github.com/dragonfore4/deka-download) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/dragonfore4/deka-download/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/dragonfore4/deka-download/blob/5fdb0344ee23fcf8253f923944a69453731aee32/config.ts) (source: github_api): readonly DEKA_BASE_URL: string;   readonly DEKA_SEARCH_URL: string;   readonly DEKA_PRINT_URL: string;   readonly GOTENBERG_BASE_URL: string;   readonly GOTENBERG_HTML_URL: string;   // Concurrency
- [code_permalink](https://github.com/dragonfore4/deka-download/blob/5fdb0344ee23fcf8253f923944a69453731aee32/downloadDeka.ts) (source: github_api): } async function renderWithGotenberg(htmlContent: string, filePath: string) {   if (!config.ENABLE_GOTENBERG) {     throw new Error("Gotenberg is disabled in configuration");   }

### 172. modrinth/code

**Repository / product**

- Repository: [https://github.com/modrinth/code](https://github.com/modrinth/code)
- Company: Unknown — not stated in the repository
- Product: ![Modrinth Monorepo Cover](/.github/assets/monorepo_cover.png)
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://modrinth.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 9
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 9
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/modrinth/code/blob/main/docker-compose.yml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/util/gotenberg.rs)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/routes/internal/gotenberg.rs)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/lib.rs)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/util/mod.rs)

**Evidence trail**

- [api_response](https://github.com/modrinth/code) (source: github_api): stars=2322, fork=False, archived=False
- [code_permalink](https://github.com/modrinth/code/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/util/gotenberg.rs) (source: github_api): ))             .header("Gotenberg-Webhook-Url", success_webhook)             .header("Gotenberg-Webhook-Error-Url", error_webhook)
- [code_permalink](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/routes/internal/gotenberg.rs) (source: github_api): /// Document generated by Gotenberg and returned to us. #[derive(Debug, Serialize, Deserialize)]
- [code_permalink](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/lib.rs) (source: github_api): use util::cors::default_cors; use util::gotenberg::GotenbergClient;
- [code_permalink](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/util/mod.rs) (source: github_api): pub mod date; pub mod error; pub mod ext; pub mod gotenberg; pub mod guards; pub mod http; pub mod img;
- [api_response](https://github.com/modrinth/code) (source: github_api): stars=2322, fork=False, archived=False
- [code_permalink](https://github.com/modrinth/code/blob/main/docker-compose.yml) (source: github_api): name: labrinth services:   postgres_db:     # staging/prod Labrinth are currently using this version of Postgres     image: postgres:15-alpine     container_name: labrinth-postgres     volumes:
- [code_permalink](https://github.com/modrinth/code/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/modrinth/code/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/util/gotenberg.rs) (source: github_api): ))             .header("Gotenberg-Webhook-Url", success_webhook)             .header("Gotenberg-Webhook-Error-Url", error_webhook)
- [code_permalink](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/routes/internal/gotenberg.rs) (source: github_api): /// Document generated by Gotenberg and returned to us. #[derive(Debug, Serialize, Deserialize)]
- [code_permalink](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/lib.rs) (source: github_api): use util::cors::default_cors; use util::gotenberg::GotenbergClient;
- [code_permalink](https://github.com/modrinth/code/blob/237963bb3532d0f612737af80b0284969d994412/apps/labrinth/src/util/mod.rs) (source: github_api): pub mod date; pub mod error; pub mod ext; pub mod gotenberg; pub mod guards; pub mod http; pub mod img;

### 173. Probesys/lotemplate

**Repository / product**

- Repository: [https://github.com/probesys/lotemplate](https://github.com/probesys/lotemplate)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 30
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 30
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [code](https://github.com/Probesys/lotemplate/blob/master/Dockerfile)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/Probesys/lotemplate/blob/4a9d0c4f04df602c97efe746058f2bdf2491565f/lotemplate_cli.py)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/Probesys/lotemplate/blob/4a9d0c4f04df602c97efe746058f2bdf2491565f/lotemplate/__init__.py)

**Evidence trail**

- [api_response](https://github.com/Probesys/lotemplate) (source: github_api): stars=49, fork=False, archived=False
- [code_permalink](https://github.com/Probesys/lotemplate/blob/master/Dockerfile) (source: github_api): libreoffice-nogui \
- [code_permalink](https://github.com/Probesys/lotemplate/blob/4a9d0c4f04df602c97efe746058f2bdf2491565f/lotemplate_cli.py) (source: github_api): help="Names of the filled files, if the template should be filled. supported formats: "                         "pdf, html, docx, png, odt")     p.add_argument('--config', '-c', is_
- [code_permalink](https://github.com/Probesys/lotemplate/blob/4a9d0c4f04df602c97efe746058f2bdf2491565f/lotemplate/__init__.py) (source: github_api): LOTemplate Filler ~~~~~~~~~~~~~~~~~ A module for manipulate and fill libreoffice writer-like documents with given variables Contains the two used classes, errors raised and some utils fonctions """
- [api_response](https://github.com/Probesys/lotemplate) (source: github_api): stars=49, fork=False, archived=False
- [code_permalink](https://github.com/Probesys/lotemplate/blob/master/Dockerfile) (source: github_api): FROM debian:trixie-slim AS prod RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache RUN --mount=type=cache,id=apt-c
- [code_permalink](https://github.com/Probesys/lotemplate/blob/master/Dockerfile) (source: github_api): libreoffice-nogui \
- [code_permalink](https://github.com/Probesys/lotemplate/blob/master/Dockerfile) (source: github_api): libreoffice-nogui \
- [code_permalink](https://github.com/Probesys/lotemplate/blob/4a9d0c4f04df602c97efe746058f2bdf2491565f/lotemplate_cli.py) (source: github_api): help="Names of the filled files, if the template should be filled. supported formats: "                         "pdf, html, docx, png, odt")     p.add_argument('--config', '-c', is_
- [code_permalink](https://github.com/Probesys/lotemplate/blob/4a9d0c4f04df602c97efe746058f2bdf2491565f/lotemplate/__init__.py) (source: github_api): LOTemplate Filler ~~~~~~~~~~~~~~~~~ A module for manipulate and fill libreoffice writer-like documents with given variables Contains the two used classes, errors raised and some utils fonctions """

### 174. MVladislav/vm-docker-collection

**Repository / product**

- Repository: [https://github.com/mvladislav/vm-docker-collection](https://github.com/mvladislav/vm-docker-collection)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 17
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 19
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 17
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 19
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [composer/sys-finance/InvoiceShelf/docker-compose.yaml](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-finance/InvoiceShelf/docker-compose.yaml)
- `Gotenberg` (conversion, conversion) — infrastructure_reference — [composer/sys-tools/rxresu/docker-compose.yaml](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-tools/rxresu/docker-compose.yaml)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [composer/sys-tools/rxresu/docker-compose.yaml](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-tools/rxresu/docker-compose.yaml)

**Evidence trail**

- [api_response](https://github.com/MVladislav/vm-docker-collection) (source: github_api): stars=10, fork=False, archived=False
- [readme_excerpt](https://github.com/MVladislav/vm-docker-collection/blob/main/README.md) (source: readme): A curated collection of ready-to-use Docker Compose stacks for a fast and easy start-up, designed for Docker Swarm with Traefik.
- [api_response](https://github.com/MVladislav/vm-docker-collection) (source: github_api): stars=10, fork=False, archived=False
- [code_permalink](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-finance/InvoiceShelf/docker-compose.yaml) (source: github_api): --- x-basic-deploy-labels: &basic-deploy-labels   labels:     - traefik.enable=true     - traefik.swarm.lbswarm=${LB_SWARM:-true}     - traefik.swarm.network=proxy     - traefik.http.routers.invoicesh
- [code_permalink](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-tools/rxresu/docker-compose.yaml) (source: github_api): --- x-basic-deploy-labels: &basic-deploy-labels   labels:     - traefik.enable=true     - traefik.swarm.lbswarm=${LB_SWARM:-true}     - traefik.swarm.network=proxy     - traefik.http.routers.reactive-
- [readme_excerpt](https://github.com/MVladislav/vm-docker-collection/blob/main/README.md) (source: readme): A curated collection of ready-to-use Docker Compose stacks for a fast and easy start-up, designed for Docker Swarm with Traefik.
- [api_response](https://github.com/MVladislav/vm-docker-collection) (source: github_api): stars=10, fork=False, archived=False
- [code_permalink](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-finance/InvoiceShelf/docker-compose.yaml) (source: github_api): --- x-basic-deploy-labels: &basic-deploy-labels   labels:     - traefik.enable=true     - traefik.swarm.lbswarm=${LB_SWARM:-true}     - traefik.swarm.network=proxy     - traefik.http.routers.invoicesh
- [code_permalink](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-tools/rxresu/docker-compose.yaml) (source: github_api): --- x-basic-deploy-labels: &basic-deploy-labels   labels:     - traefik.enable=true     - traefik.swarm.lbswarm=${LB_SWARM:-true}     - traefik.swarm.network=proxy     - traefik.http.routers.reactive-
- [manifest_line](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-finance/InvoiceShelf/docker-compose.yaml) (source: github_api): gotenberg:
- [manifest_line](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-tools/rxresu/docker-compose.yaml) (source: github_api): GOTENBERG_ENDPOINT: http://gotenberg:3000
- [manifest_line](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-tools/rxresu/docker-compose.yaml) (source: github_api): LIBREOFFICE_DISABLE_ROUTES: ${LIBREOFFICE_DISABLE_ROUTES:-true}
- [readme_excerpt](https://github.com/MVladislav/vm-docker-collection/blob/main/README.md) (source: readme): A curated collection of ready-to-use Docker Compose stacks for a fast and easy start-up, designed for Docker Swarm with Traefik.
- [api_response](https://github.com/MVladislav/vm-docker-collection) (source: github_api): stars=10, fork=False, archived=False
- [code_permalink](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-finance/InvoiceShelf/docker-compose.yaml) (source: github_api): --- x-basic-deploy-labels: &basic-deploy-labels   labels:     - traefik.enable=true     - traefik.swarm.lbswarm=${LB_SWARM:-true}     - traefik.swarm.network=proxy     - traefik.http.routers.invoicesh
- [code_permalink](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-tools/rxresu/docker-compose.yaml) (source: github_api): --- x-basic-deploy-labels: &basic-deploy-labels   labels:     - traefik.enable=true     - traefik.swarm.lbswarm=${LB_SWARM:-true}     - traefik.swarm.network=proxy     - traefik.http.routers.reactive-
- [manifest_line](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-finance/InvoiceShelf/docker-compose.yaml) (source: github_api): gotenberg:
- [manifest_line](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-tools/rxresu/docker-compose.yaml) (source: github_api): GOTENBERG_ENDPOINT: http://gotenberg:3000
- [manifest_line](https://github.com/MVladislav/vm-docker-collection/blob/main/composer/sys-tools/rxresu/docker-compose.yaml) (source: github_api): LIBREOFFICE_DISABLE_ROUTES: ${LIBREOFFICE_DISABLE_ROUTES:-true}
- [readme_excerpt](https://github.com/MVladislav/vm-docker-collection/blob/main/README.md) (source: readme): A curated collection of ready-to-use Docker Compose stacks for a fast and easy start-up, designed for Docker Swarm with Traefik.

### 175. ministryofjustice/send-legal-mail-to-prisons

**Repository / product**

- Repository: [https://github.com/ministryofjustice/send-legal-mail-to-prisons](https://github.com/ministryofjustice/send-legal-mail-to-prisons)
- Company: Unknown — not stated in the repository
- Product: Send legal mail to prisons
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://send-legal-mail.prison.service.justice.gov.uk/start

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 27
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 27
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/main/docker-compose.yml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/6e321faeac07c7086971dc1bc07d7787a8f06002/server/data/gotenbergClient.ts)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/6e321faeac07c7086971dc1bc07d7787a8f06002/server/config.ts)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/6e321faeac07c7086971dc1bc07d7787a8f06002/server/middleware/setupPdfRenderer.ts)

**Evidence trail**

- [api_response](https://github.com/ministryofjustice/send-legal-mail-to-prisons) (source: github_api): stars=2, fork=False, archived=False
- [code_permalink](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/main/docker-compose.yml) (source: github_api): - GOTENBERG_API_URL=http://gotenberg:3000
- [code_permalink](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/6e321faeac07c7086971dc1bc07d7787a8f06002/server/data/gotenbergClient.ts) (source: github_api): const request = superagent       .post(`${config.gotenberg.url}/forms/chromium/convert/html`)       .set('Content-Type', 'multi-part/form-data')
- [code_permalink](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/6e321faeac07c7086971dc1bc07d7787a8f06002/server/config.ts) (source: github_api): },   },   gotenberg: {     url: get('GOTENBERG_API_URL', 'http://localhost:3001', requiredInProduction),   },   domain: get('INGRESS_URL', 'http://localhost:3000', requiredInProduction),   slmCont
- [code_permalink](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/6e321faeac07c7086971dc1bc07d7787a8f06002/server/middleware/setupPdfRenderer.ts) (source: github_api): /*  * This function accepts a Gotenberg client as its only argument.  * It returns a handler function to render a normal HTML view template to
- [api_response](https://github.com/ministryofjustice/send-legal-mail-to-prisons) (source: github_api): stars=2, fork=False, archived=False
- [code_permalink](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/main/docker-compose.yml) (source: github_api): version: '3.1' services:   app:     image: quay.io/hmpps/send-legal-mail-to-prisons     networks:       - hmpps     container_name: send-legal-mail-to-prisons     depends_on: [redis]     ports:
- [code_permalink](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/main/docker-compose.yml) (source: github_api): - GOTENBERG_API_URL=http://gotenberg:3000
- [code_permalink](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/main/docker-compose.yml) (source: github_api): - GOTENBERG_API_URL=http://gotenberg:3000
- [code_permalink](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/6e321faeac07c7086971dc1bc07d7787a8f06002/server/data/gotenbergClient.ts) (source: github_api): const request = superagent       .post(`${config.gotenberg.url}/forms/chromium/convert/html`)       .set('Content-Type', 'multi-part/form-data')
- [code_permalink](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/6e321faeac07c7086971dc1bc07d7787a8f06002/server/config.ts) (source: github_api): },   },   gotenberg: {     url: get('GOTENBERG_API_URL', 'http://localhost:3001', requiredInProduction),   },   domain: get('INGRESS_URL', 'http://localhost:3000', requiredInProduction),   slmCont
- [code_permalink](https://github.com/ministryofjustice/send-legal-mail-to-prisons/blob/6e321faeac07c7086971dc1bc07d7787a8f06002/server/middleware/setupPdfRenderer.ts) (source: github_api): /*  * This function accepts a Gotenberg client as its only argument.  * It returns a handler function to render a normal HTML view template to

### 176. notadev-iamaura/OneRAG

**Repository / product**

- Repository: [https://github.com/notadev-iamaura/onerag](https://github.com/notadev-iamaura/onerag)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://github.com/notadev-iamaura/OneRAG

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 27
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 27
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:8001..16000`, rank 27
  - Query: `"PyMuPDF" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 334 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [code](https://github.com/notadev-iamaura/OneRAG/blob/main/Dockerfile)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/notadev-iamaura/OneRAG/blob/d91d74a09faaebc5c4d80aa14b931d61224cf059/app/modules/core/documents/loaders/docx_loader.py)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/notadev-iamaura/OneRAG/blob/d91d74a09faaebc5c4d80aa14b931d61224cf059/app/modules/core/documents/loaders/factory.py)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/notadev-iamaura/OneRAG/blob/d91d74a09faaebc5c4d80aa14b931d61224cf059/scripts/reindex_documents.py)

**Evidence trail**

- [api_response](https://github.com/notadev-iamaura/OneRAG) (source: github_api): stars=125, fork=False, archived=False
- [code_permalink](https://github.com/notadev-iamaura/OneRAG/blob/main/Dockerfile) (source: github_api): # docx_loader가 soffice/libreoffice 바이너리로 .doc를 변환하므로, 이 의존성이
- [code_permalink](https://github.com/notadev-iamaura/OneRAG/blob/d91d74a09faaebc5c4d80aa14b931d61224cf059/app/modules/core/documents/loaders/docx_loader.py) (source: github_api): Word 문서 파일 로딩 전략 구현 차용/개선 사항(백포트, #26): - 레거시 .doc 지원: LibreOffice headless 변환(soffice --convert-to docx) 후 기존   DOCX 경로를 재사용한다. - graceful-optional: soffice/libreoffice 바이너리 부재 시 명확한 ValueError로 안내하
- [code_permalink](https://github.com/notadev-iamaura/OneRAG/blob/d91d74a09faaebc5c4d80aa14b931d61224cf059/app/modules/core/documents/loaders/factory.py) (source: github_api): ".txt": TextLoader(),         ".text": TextLoader(),         ".docx": DOCXLoader(),         ".doc": DOCXLoader(),  # #26: 레거시 .doc는 LibreOffice 변환 후 DOCX 경로 재사용         ".pptx": PPTXLoader(),
- [code_permalink](https://github.com/notadev-iamaura/OneRAG/blob/d91d74a09faaebc5c4d80aa14b931d61224cf059/scripts/reindex_documents.py) (source: github_api): 원본 대비 일반화:     - chunked 업로드 경로 전부 제거(OneRAG에 /api/upload/chunked/* 부재).     - LibreOffice(soffice) .doc/.pptx 변환 제거(LoaderFactory가 직접 지원 여부 판단).     - Cloud Run 하드코딩 backend-url / 한국어 기본 소스 디렉토리 제거
- [api_response](https://github.com/notadev-iamaura/OneRAG) (source: github_api): stars=125, fork=False, archived=False
- [code_permalink](https://github.com/notadev-iamaura/OneRAG/blob/main/Dockerfile) (source: github_api): # Python FastAPI build FROM python:3.11-slim # Install system dependencies (including Playwright requirements) RUN apt-get update && apt-get install -y --no-install-recommends \     curl \     build-
- [code_permalink](https://github.com/notadev-iamaura/OneRAG/blob/main/Dockerfile) (source: github_api): # docx_loader가 soffice/libreoffice 바이너리로 .doc를 변환하므로, 이 의존성이
- [code_permalink](https://github.com/notadev-iamaura/OneRAG/blob/main/Dockerfile) (source: github_api): # docx_loader가 soffice/libreoffice 바이너리로 .doc를 변환하므로, 이 의존성이
- [code_permalink](https://github.com/notadev-iamaura/OneRAG/blob/d91d74a09faaebc5c4d80aa14b931d61224cf059/app/modules/core/documents/loaders/docx_loader.py) (source: github_api): Word 문서 파일 로딩 전략 구현 차용/개선 사항(백포트, #26): - 레거시 .doc 지원: LibreOffice headless 변환(soffice --convert-to docx) 후 기존   DOCX 경로를 재사용한다. - graceful-optional: soffice/libreoffice 바이너리 부재 시 명확한 ValueError로 안내하
- [code_permalink](https://github.com/notadev-iamaura/OneRAG/blob/d91d74a09faaebc5c4d80aa14b931d61224cf059/app/modules/core/documents/loaders/factory.py) (source: github_api): ".txt": TextLoader(),         ".text": TextLoader(),         ".docx": DOCXLoader(),         ".doc": DOCXLoader(),  # #26: 레거시 .doc는 LibreOffice 변환 후 DOCX 경로 재사용         ".pptx": PPTXLoader(),
- [code_permalink](https://github.com/notadev-iamaura/OneRAG/blob/d91d74a09faaebc5c4d80aa14b931d61224cf059/scripts/reindex_documents.py) (source: github_api): 원본 대비 일반화:     - chunked 업로드 경로 전부 제거(OneRAG에 /api/upload/chunked/* 부재).     - LibreOffice(soffice) .doc/.pptx 변환 제거(LoaderFactory가 직접 지원 여부 판단).     - Cloud Run 하드코딩 backend-url / 한국어 기본 소스 디렉토리 제거

### 177. solidtime-io/solidtime

**Repository / product**

- Repository: [https://github.com/solidtime-io/solidtime](https://github.com/solidtime-io/solidtime)
- Company: Unknown — not stated in the repository
- Product: solidtime - The modern Open-Source TimeTracker
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.solidtime.io

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 3
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 3
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/solidtime-io/solidtime/blob/main/docker-compose.yml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/solidtime-io/solidtime/blob/3af69830ee08bb69df890887349bb550b00e9923/config/services.php)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/solidtime-io/solidtime/blob/3af69830ee08bb69df890887349bb550b00e9923/app/Http/Controllers/Api/V1/TimeEntryController.php)

**Evidence trail**

- [api_response](https://github.com/solidtime-io/solidtime) (source: github_api): stars=8865, fork=False, archived=False
- [code_permalink](https://github.com/solidtime-io/solidtime/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/solidtime-io/solidtime/blob/3af69830ee08bb69df890887349bb550b00e9923/config/services.php) (source: github_api): declare(strict_types=1); return [     'gotenberg' => [         'url' => env('GOTENBERG_URL'),         'basic_auth_username' => env('GOTENBERG_BASIC_AUTH_USERNAME'),         'basic_auth_password' => e
- [code_permalink](https://github.com/solidtime-io/solidtime/blob/3af69830ee08bb69df890887349bb550b00e9923/app/Http/Controllers/Api/V1/TimeEntryController.php) (source: github_api): use App\Service\TimeEntryFilter; use App\Service\TimeEntryService; use App\Service\TimezoneService; use Gotenberg\Exceptions\GotenbergApiErrored; use Gotenberg\Exceptions\NoOutputFileInResponse; use G
- [api_response](https://github.com/solidtime-io/solidtime) (source: github_api): stars=8865, fork=False, archived=False
- [code_permalink](https://github.com/solidtime-io/solidtime/blob/main/docker-compose.yml) (source: github_api): services:     laravel.test:         build:             context: ./docker/local/8.3             dockerfile: Dockerfile             args:                 WWWGROUP: '${WWWGROUP}'         image: sail-8.3/
- [code_permalink](https://github.com/solidtime-io/solidtime/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/solidtime-io/solidtime/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/solidtime-io/solidtime/blob/3af69830ee08bb69df890887349bb550b00e9923/config/services.php) (source: github_api): declare(strict_types=1); return [     'gotenberg' => [         'url' => env('GOTENBERG_URL'),         'basic_auth_username' => env('GOTENBERG_BASIC_AUTH_USERNAME'),         'basic_auth_password' => e
- [code_permalink](https://github.com/solidtime-io/solidtime/blob/3af69830ee08bb69df890887349bb550b00e9923/app/Http/Controllers/Api/V1/TimeEntryController.php) (source: github_api): use App\Service\TimeEntryFilter; use App\Service\TimeEntryService; use App\Service\TimezoneService; use Gotenberg\Exceptions\GotenbergApiErrored; use Gotenberg\Exceptions\NoOutputFileInResponse; use G

### 178. unitedworldwrestling/arena-public

**Repository / product**

- Repository: [https://github.com/unitedworldwrestling/arena-public](https://github.com/unitedworldwrestling/arena-public)
- Company: Unknown — not stated in the repository
- Product: Arena
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 6
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 6
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yaml`
  - Retrieved 30 of 102 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [Resources/docker-compose.yaml](https://github.com/unitedworldwrestling/arena-public/blob/master/Resources/docker-compose.yaml)

**Evidence trail**

- [api_response](https://github.com/unitedworldwrestling/arena-public) (source: github_api): stars=20, fork=False, archived=False
- [readme_excerpt](https://github.com/unitedworldwrestling/arena-public/blob/master/README.md) (source: readme): [Download](https://we.tl/t-KQDJvizNRH) (If this link does not work, check [the current one](https://github.com/unitedworldwrestling/arena-public/blob/releases/lgtv/download.link) [Documentation](https
- [api_response](https://github.com/unitedworldwrestling/arena-public) (source: github_api): stars=20, fork=False, archived=False
- [code_permalink](https://github.com/unitedworldwrestling/arena-public/blob/master/Resources/docker-compose.yaml) (source: github_api): services:     php-fpm:         image: public.ecr.aws/uww/app/arena:latest         environment:             PHP_MEMORY_LIMIT: ${PHP_MEMORY_LIMIT:--1}             DOCKER_COMPOSE_FILE_VERSION: "1.2"
- [readme_excerpt](https://github.com/unitedworldwrestling/arena-public/blob/master/README.md) (source: readme): [Download](https://we.tl/t-KQDJvizNRH) (If this link does not work, check [the current one](https://github.com/unitedworldwrestling/arena-public/blob/releases/lgtv/download.link) [Documentation](https
- [api_response](https://github.com/unitedworldwrestling/arena-public) (source: github_api): stars=20, fork=False, archived=False
- [code_permalink](https://github.com/unitedworldwrestling/arena-public/blob/master/Resources/docker-compose.yaml) (source: github_api): services:     php-fpm:         image: public.ecr.aws/uww/app/arena:latest         environment:             PHP_MEMORY_LIMIT: ${PHP_MEMORY_LIMIT:--1}             DOCKER_COMPOSE_FILE_VERSION: "1.2"
- [manifest_line](https://github.com/unitedworldwrestling/arena-public/blob/master/Resources/docker-compose.yaml) (source: github_api): gotenberg:
- [readme_excerpt](https://github.com/unitedworldwrestling/arena-public/blob/master/README.md) (source: readme): [Download](https://we.tl/t-KQDJvizNRH) (If this link does not work, check [the current one](https://github.com/unitedworldwrestling/arena-public/blob/releases/lgtv/download.link) [Documentation](https
- [api_response](https://github.com/unitedworldwrestling/arena-public) (source: github_api): stars=20, fork=False, archived=False
- [code_permalink](https://github.com/unitedworldwrestling/arena-public/blob/master/Resources/docker-compose.yaml) (source: github_api): services:     php-fpm:         image: public.ecr.aws/uww/app/arena:latest         environment:             PHP_MEMORY_LIMIT: ${PHP_MEMORY_LIMIT:--1}             DOCKER_COMPOSE_FILE_VERSION: "1.2"
- [manifest_line](https://github.com/unitedworldwrestling/arena-public/blob/master/Resources/docker-compose.yaml) (source: github_api): gotenberg:
- [readme_excerpt](https://github.com/unitedworldwrestling/arena-public/blob/master/README.md) (source: readme): [Download](https://we.tl/t-KQDJvizNRH) (If this link does not work, check [the current one](https://github.com/unitedworldwrestling/arena-public/blob/releases/lgtv/download.link) [Documentation](https

### 179. YYC-Cube/YYC3-Knowledge-Base

**Repository / product**

- Repository: [https://github.com/yyc-cube/yyc3-knowledge-base](https://github.com/yyc-cube/yyc3-knowledge-base)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 25
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 25
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — manifest_declaration — [YYC3-A/DefinitelyTyped/types/carbone/package.json](https://github.com/YYC-Cube/YYC3-Knowledge-Base/blob/7dddb5770f5c35c186a0eb92fee5e1cd4279fed6/YYC3-A/DefinitelyTyped/types/carbone/package.json)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [YYC3-E/types/definitely-typed/types/carbone/package.json](https://github.com/YYC-Cube/YYC3-Knowledge-Base/blob/7dddb5770f5c35c186a0eb92fee5e1cd4279fed6/YYC3-E/types/definitely-typed/types/carbone/package.json)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/YYC-Cube/YYC3-Knowledge-Base/blob/7dddb5770f5c35c186a0eb92fee5e1cd4279fed6/YYC3-H/mui-x/docs/data/charts/dataset/carbonEmissions2024Every6Hours.ts)

**Evidence trail**

- [api_response](https://github.com/YYC-Cube/YYC3-Knowledge-Base) (source: github_api): stars=1, fork=False, archived=False
- [manifest_line](https://github.com/YYC-Cube/YYC3-Knowledge-Base/blob/7dddb5770f5c35c186a0eb92fee5e1cd4279fed6/YYC3-A/DefinitelyTyped/types/carbone/package.json) (source: github_api): "private": true,     "name": "@types/carbone",     "version": "3.2.9999",
- [manifest_line](https://github.com/YYC-Cube/YYC3-Knowledge-Base/blob/7dddb5770f5c35c186a0eb92fee5e1cd4279fed6/YYC3-E/types/definitely-typed/types/carbone/package.json) (source: github_api): "private": true,     "name": "@types/carbone",     "version": "3.2.9999",
- [code_permalink](https://github.com/YYC-Cube/YYC3-Knowledge-Base/blob/7dddb5770f5c35c186a0eb92fee5e1cd4279fed6/YYC3-H/mui-x/docs/data/charts/dataset/carbonEmissions2024Every6Hours.ts) (source: github_api): export const carbonEmissions2024Every6Hours = {   BEL: [     579.78, 607.24, 569.72, 498.73, 484.13, 507.21000000000004, 527.61, 569.8199999999999, 564.37,     588.1999999999999, 561.53, 539.23, 556.7

### 180. georgemarian98/home-server

**Repository / product**

- Repository: [https://github.com/georgemarian98/home-server](https://github.com/georgemarian98/home-server)
- Company: Unknown — not stated in the repository
- Product: Home server
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 24
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 24
  - Query: `"libreoffice" filename:docker-compose.yaml`
  - Retrieved 30 of 45 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [paperless/docker-compose.yaml](https://github.com/georgemarian98/home-server/blob/master/paperless/docker-compose.yaml)

**Evidence trail**

- [api_response](https://github.com/georgemarian98/home-server) (source: github_api): stars=0, fork=False, archived=False
- [readme_excerpt](https://github.com/georgemarian98/home-server/blob/master/README.md) (source: readme): This structure is used by Jellyfin, QBittorrent, prowlarr, radarr, etc.
- [api_response](https://github.com/georgemarian98/home-server) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/georgemarian98/home-server/blob/master/paperless/docker-compose.yaml) (source: github_api): --- # Docker Compose file for running paperless from the docker container registry. # This file contains everything paperless needs to run. # Paperless supports amd64, arm and arm64 hardware. # # All
- [readme_excerpt](https://github.com/georgemarian98/home-server/blob/master/README.md) (source: readme): This structure is used by Jellyfin, QBittorrent, prowlarr, radarr, etc.
- [api_response](https://github.com/georgemarian98/home-server) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/georgemarian98/home-server/blob/master/paperless/docker-compose.yaml) (source: github_api): --- # Docker Compose file for running paperless from the docker container registry. # This file contains everything paperless needs to run. # Paperless supports amd64, arm and arm64 hardware. # # All
- [manifest_line](https://github.com/georgemarian98/home-server/blob/master/paperless/docker-compose.yaml) (source: github_api): #   Office documents (Word, Excel, PowerPoint and their LibreOffice counter-
- [readme_excerpt](https://github.com/georgemarian98/home-server/blob/master/README.md) (source: readme): This structure is used by Jellyfin, QBittorrent, prowlarr, radarr, etc.
- [api_response](https://github.com/georgemarian98/home-server) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/georgemarian98/home-server/blob/master/paperless/docker-compose.yaml) (source: github_api): --- # Docker Compose file for running paperless from the docker container registry. # This file contains everything paperless needs to run. # Paperless supports amd64, arm and arm64 hardware. # # All
- [manifest_line](https://github.com/georgemarian98/home-server/blob/master/paperless/docker-compose.yaml) (source: github_api): #   Office documents (Word, Excel, PowerPoint and their LibreOffice counter-
- [readme_excerpt](https://github.com/georgemarian98/home-server/blob/master/README.md) (source: readme): This structure is used by Jellyfin, QBittorrent, prowlarr, radarr, etc.

### 181. tjmlabs/ColiVara

**Repository / product**

- Repository: [https://github.com/tjmlabs/colivara](https://github.com/tjmlabs/colivara)
- Company: Unknown — not stated in the repository
- Product: ColiVara
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://colivara.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 4
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 4
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/tjmlabs/ColiVara/blob/main/docker-compose.yml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/tjmlabs/ColiVara/blob/20a8bcd5c1ac70937565577b2ee2759d11a83d3c/web/config/settings.py)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/tjmlabs/ColiVara/blob/20a8bcd5c1ac70937565577b2ee2759d11a83d3c/web/api/models.py)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/tjmlabs/ColiVara/blob/20a8bcd5c1ac70937565577b2ee2759d11a83d3c/web/api/tests/tests.py)

**Evidence trail**

- [api_response](https://github.com/tjmlabs/ColiVara) (source: github_api): stars=1486, fork=False, archived=False
- [code_permalink](https://github.com/tjmlabs/ColiVara/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/tjmlabs/ColiVara/blob/20a8bcd5c1ac70937565577b2ee2759d11a83d3c/web/config/settings.py) (source: github_api): ALWAYS_ON_EMBEDDINGS_URL = env("ALWAYS_ON_EMBEDDINGS_URL", default=EMBEDDINGS_URL) EMBEDDINGS_URL_TOKEN = env("EMBEDDINGS_URL_TOKEN") # Gotenberg GOTENBERG_URL = env("GOTENBERG_URL", default="http://
- [code_permalink](https://github.com/tjmlabs/ColiVara/blob/20a8bcd5c1ac70937565577b2ee2759d11a83d3c/web/api/models.py) (source: github_api): """         Helper method to convert documents to PDF using Gotenberg.         """
- [code_permalink](https://github.com/tjmlabs/ColiVara/blob/20a8bcd5c1ac70937565577b2ee2759d11a83d3c/web/api/tests/tests.py) (source: github_api): async def test_create_document_webpage_await(async_client, user, collection):     url = "https://gotenberg.dev/docs/getting-started/introduction"     response = await async_client.post(
- [api_response](https://github.com/tjmlabs/ColiVara) (source: github_api): stars=1486, fork=False, archived=False
- [code_permalink](https://github.com/tjmlabs/ColiVara/blob/main/docker-compose.yml) (source: github_api): services:   web:     build: ./web     ports:       - "8001:8000"     command: uvicorn config.asgi:application --reload --host 0.0.0.0 --port 8000     volumes:       - ./web:/code     depends_on:
- [code_permalink](https://github.com/tjmlabs/ColiVara/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/tjmlabs/ColiVara/blob/main/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/tjmlabs/ColiVara/blob/20a8bcd5c1ac70937565577b2ee2759d11a83d3c/web/config/settings.py) (source: github_api): ALWAYS_ON_EMBEDDINGS_URL = env("ALWAYS_ON_EMBEDDINGS_URL", default=EMBEDDINGS_URL) EMBEDDINGS_URL_TOKEN = env("EMBEDDINGS_URL_TOKEN") # Gotenberg GOTENBERG_URL = env("GOTENBERG_URL", default="http://
- [code_permalink](https://github.com/tjmlabs/ColiVara/blob/20a8bcd5c1ac70937565577b2ee2759d11a83d3c/web/api/models.py) (source: github_api): """         Helper method to convert documents to PDF using Gotenberg.         """
- [code_permalink](https://github.com/tjmlabs/ColiVara/blob/20a8bcd5c1ac70937565577b2ee2759d11a83d3c/web/api/tests/tests.py) (source: github_api): async def test_create_document_webpage_await(async_client, user, collection):     url = "https://gotenberg.dev/docs/getting-started/introduction"     response = await async_client.post(

### 182. samvera/hydra-derivatives

**Repository / product**

- Repository: [https://github.com/samvera/hydra-derivatives](https://github.com/samvera/hydra-derivatives)
- Company: Unknown — not stated in the repository
- Product: hydra-derivatives
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 16
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 16
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [code](https://github.com/samvera/hydra-derivatives/blob/main/Dockerfile)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/samvera/hydra-derivatives/blob/bf8e076ca30d90d5f3d1f8cd99e20a97fafd3c4e/lib/hydra/derivatives.rb)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/samvera/hydra-derivatives/blob/bf8e076ca30d90d5f3d1f8cd99e20a97fafd3c4e/spec/units/config_spec.rb)

**Evidence trail**

- [api_response](https://github.com/samvera/hydra-derivatives) (source: github_api): stars=17, fork=False, archived=False
- [code_permalink](https://github.com/samvera/hydra-derivatives/blob/main/Dockerfile) (source: github_api): libreoffice \
- [code_permalink](https://github.com/samvera/hydra-derivatives/blob/bf8e076ca30d90d5f3d1f8cd99e20a97fafd3c4e/lib/hydra/derivatives.rb) (source: github_api): @config = Config.new     end     CONFIG_METHODS = %i[ffmpeg_path libreoffice_path temp_file_base fits_path kdu_compress_path                         kdu_compress_recipes enable_ffmpeg source_fi
- [code_permalink](https://github.com/samvera/hydra-derivatives/blob/bf8e076ca30d90d5f3d1f8cd99e20a97fafd3c4e/spec/units/config_spec.rb) (source: github_api): it "has some configuration defaults" do     expect(subject.ffmpeg_path).to eq('ffmpeg')     expect(subject.enable_ffmpeg).to be true     expect(subject.libreoffice_path).to eq('soffice')     expect(
- [api_response](https://github.com/samvera/hydra-derivatives) (source: github_api): stars=17, fork=False, archived=False
- [code_permalink](https://github.com/samvera/hydra-derivatives/blob/main/Dockerfile) (source: github_api): ARG RUBY_VERSION=3.2.2 FROM rubylang/ruby:$RUBY_VERSION-dev-jammy RUN apt update && apt -y install \   imagemagick \   zip \   ghostscript \   libpng-dev \   libvips \   libvips-dev \   libvips-tool
- [code_permalink](https://github.com/samvera/hydra-derivatives/blob/main/Dockerfile) (source: github_api): libreoffice \
- [code_permalink](https://github.com/samvera/hydra-derivatives/blob/main/Dockerfile) (source: github_api): libreoffice \
- [code_permalink](https://github.com/samvera/hydra-derivatives/blob/bf8e076ca30d90d5f3d1f8cd99e20a97fafd3c4e/lib/hydra/derivatives.rb) (source: github_api): @config = Config.new     end     CONFIG_METHODS = %i[ffmpeg_path libreoffice_path temp_file_base fits_path kdu_compress_path                         kdu_compress_recipes enable_ffmpeg source_fi
- [code_permalink](https://github.com/samvera/hydra-derivatives/blob/bf8e076ca30d90d5f3d1f8cd99e20a97fafd3c4e/spec/units/config_spec.rb) (source: github_api): it "has some configuration defaults" do     expect(subject.ffmpeg_path).to eq('ffmpeg')     expect(subject.enable_ffmpeg).to be true     expect(subject.libreoffice_path).to eq('soffice')     expect(

### 183. AppCivico/smae

**Repository / product**

- Repository: [https://github.com/appcivico/smae](https://github.com/appcivico/smae)
- Company: Unknown — not stated in the repository
- Product: SMAE
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 14
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 14
  - Query: `"gotenberg" filename:Dockerfile`
  - Retrieved 30 of 169 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/AppCivico/smae/blob/homol/docker-compose.yml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/AppCivico/smae/blob/f8490ffecad70997f4ef636e09ad58f89f44f2aa/backend/src/upload/gotenberg.service.ts)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/AppCivico/smae/blob/f8490ffecad70997f4ef636e09ad58f89f44f2aa/backend/src/upload/upload.module.ts)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/AppCivico/smae/blob/f8490ffecad70997f4ef636e09ad58f89f44f2aa/backend/src/upload/preview.service.ts)
- `Gotenberg` (conversion, conversion) — infrastructure_reference — [gotenberg/Dockerfile](https://github.com/AppCivico/smae/blob/homol/gotenberg/Dockerfile)

**Evidence trail**

- [api_response](https://github.com/AppCivico/smae) (source: github_api): stars=6, fork=False, archived=False
- [code_permalink](https://github.com/AppCivico/smae/blob/homol/docker-compose.yml) (source: github_api): GOTENBERG_URL: "http://gotenberg:3000"
- [code_permalink](https://github.com/AppCivico/smae/blob/f8490ffecad70997f4ef636e09ad58f89f44f2aa/backend/src/upload/gotenberg.service.ts) (source: github_api): this.logger.error(                     `Gotenberg did not return a valid PDF for "${filename}". Response length: ${pdfBuffer.length}`                 );
- [code_permalink](https://github.com/AppCivico/smae/blob/f8490ffecad70997f4ef636e09ad58f89f44f2aa/backend/src/upload/upload.module.ts) (source: github_api): import { JwtModule } from '@nestjs/jwt'; import { SmaeConfigModule } from '../common/services/smae-config.module'; import { PrismaModule } from '../prisma/prisma.module'; import { GotenbergService } f
- [code_permalink](https://github.com/AppCivico/smae/blob/f8490ffecad70997f4ef636e09ad58f89f44f2aa/backend/src/upload/preview.service.ts) (source: github_api): import { PreviewConfig } from './arquivo-preview.helper'; import { GotenbergService } from './gotenberg.service'; import { StorageService } from './storage-service';
- [api_response](https://github.com/AppCivico/smae) (source: github_api): stars=6, fork=False, archived=False
- [code_permalink](https://github.com/AppCivico/smae/blob/homol/gotenberg/Dockerfile) (source: github_api): FROM gotenberg/gotenberg:8 # Default configuration is handled via docker-compose environment variables and command
- [code_permalink](https://github.com/AppCivico/smae/blob/homol/docker-compose.yml) (source: github_api): GOTENBERG_URL: "http://gotenberg:3000"
- [manifest_line](https://github.com/AppCivico/smae/blob/homol/gotenberg/Dockerfile) (source: github_api): FROM gotenberg/gotenberg:8
- [code_permalink](https://github.com/AppCivico/smae/blob/f8490ffecad70997f4ef636e09ad58f89f44f2aa/backend/src/upload/gotenberg.service.ts) (source: github_api): this.logger.error(                     `Gotenberg did not return a valid PDF for "${filename}". Response length: ${pdfBuffer.length}`                 );
- [code_permalink](https://github.com/AppCivico/smae/blob/f8490ffecad70997f4ef636e09ad58f89f44f2aa/backend/src/upload/upload.module.ts) (source: github_api): import { JwtModule } from '@nestjs/jwt'; import { SmaeConfigModule } from '../common/services/smae-config.module'; import { PrismaModule } from '../prisma/prisma.module'; import { GotenbergService } f
- [code_permalink](https://github.com/AppCivico/smae/blob/f8490ffecad70997f4ef636e09ad58f89f44f2aa/backend/src/upload/preview.service.ts) (source: github_api): import { PreviewConfig } from './arquivo-preview.helper'; import { GotenbergService } from './gotenberg.service'; import { StorageService } from './storage-service';

### 184. mperreir/Hyblab2023

**Repository / product**

- Repository: [https://github.com/mperreir/hyblab2023](https://github.com/mperreir/hyblab2023)
- Company: Unknown — not stated in the repository
- Product: Hyblab2023
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 11/100 (a score, not a probability)
- Raw weighted score: 0.55 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `Carbone.io`, run `run_1`, window `unsliced`, rank 16
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `Carbone.io`, run `run_2`, window `unsliced`, rank 16
  - Query: `"carbone" filename:package.json`
  - Retrieved 30 of 444 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/mperreir/Hyblab2023/blob/79afcbdee3b7e8f338a20ba078071751598af926/carbone/vue.config.js)
- `Carbone.io` (template_generation, generation) — manifest_declaration — [carbone/package.json](https://github.com/mperreir/Hyblab2023/blob/79afcbdee3b7e8f338a20ba078071751598af926/carbone/package.json)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/mperreir/Hyblab2023/blob/79afcbdee3b7e8f338a20ba078071751598af926/server.js)
- `Carbone.io` (template_generation, generation) — code_import — [code](https://github.com/mperreir/Hyblab2023/blob/79afcbdee3b7e8f338a20ba078071751598af926/carbone/src/pages/Home/App.vue)

**Evidence trail**

- [api_response](https://github.com/mperreir/Hyblab2023) (source: github_api): stars=2, fork=False, archived=False
- [code_permalink](https://github.com/mperreir/Hyblab2023/blob/79afcbdee3b7e8f338a20ba078071751598af926/carbone/vue.config.js) (source: github_api): ]     }   },   publicPath: process.env.NODE_ENV === 'production'    ? '/nantes2023/carbone/'    : '/' }
- [manifest_line](https://github.com/mperreir/Hyblab2023/blob/79afcbdee3b7e8f338a20ba078071751598af926/carbone/package.json) (source: github_api): {   "name": "carbone",   "version": "0.1.0",   "private": true,   "scripts": {     "serve": "vue-cli-service serve",     "build": "vue-cli-service build",
- [code_permalink](https://github.com/mperreir/Hyblab2023/blob/79afcbdee3b7e8f338a20ba078071751598af926/server.js) (source: github_api): // declare the list of sub apps var app_names = []; var hyblab2023_names = ['alerte', 'carbone', 'communes', 'herisson', 'pionniers', 'raisin', 'resilience', 'soleil', 'tips', 'verdure']; app_names.
- [code_permalink](https://github.com/mperreir/Hyblab2023/blob/79afcbdee3b7e8f338a20ba078071751598af926/carbone/src/pages/Home/App.vue) (source: github_api): <span style="color: #4D51F4;">en Bretagne</span> en limitant<br>       votre <span style="color: #4D51F4;">impact carbone</span>     </div>

### 185. OPPO-PersonalAI/Agent-KB

**Repository / product**

- Repository: [https://github.com/oppo-personalai/agent-kb](https://github.com/oppo-personalai/agent-kb)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 10/100 (a score, not a probability)
- Raw weighted score: 0.50 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:2001..4000`, rank 9
  - Query: `"mammoth" filename:requirements.txt size:2001..4000`
  - Retrieved 30 of 227 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/OPPO-PersonalAI/Agent-KB/blob/588d6694e743a981179f2e11b47ca3a668e2f1ac/Agent-KB-GAIA/examples/open_deep_research/scripts/mdconvert.py)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [Agent-KB-GAIA/examples/open_deep_research/requirements.txt](https://github.com/OPPO-PersonalAI/Agent-KB/blob/588d6694e743a981179f2e11b47ca3a668e2f1ac/Agent-KB-GAIA/examples/open_deep_research/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/OPPO-PersonalAI/Agent-KB) (source: github_api): stars=449, fork=False, archived=False
- [code_permalink](https://github.com/OPPO-PersonalAI/Agent-KB/blob/588d6694e743a981179f2e11b47ca3a668e2f1ac/Agent-KB-GAIA/examples/open_deep_research/scripts/mdconvert.py) (source: github_api): import mammoth import markdownify
- [manifest_line](https://github.com/OPPO-PersonalAI/Agent-KB/blob/588d6694e743a981179f2e11b47ca3a668e2f1ac/Agent-KB-GAIA/examples/open_deep_research/requirements.txt) (source: github_api): litellm==1.63.12 lxml==5.3.1 Mako==1.3.9 mammoth==1.9.0 markdown-it-py==3.0.0 markdownify==1.1.0 MarkupSafe==3.0.2
- [readme_excerpt](https://github.com/OPPO-PersonalAI/Agent-KB/blob/master/README.md) (source: readme): Cross-Domain Adaptability: Designed for generalization across different task domains (e.g., QA, coding, planning).

### 186. khulnasoft/deepstack

**Repository / product**

- Repository: [https://github.com/khulnasoft/deepstack](https://github.com/khulnasoft/deepstack)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 10/100 (a score, not a probability)
- Raw weighted score: 0.50 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Apache Tika`, run `run_2`, window `size:8001..16000`, rank 7
  - Query: `"tika" filename:pyproject.toml size:8001..16000`
  - Retrieved 30 of 81 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache Tika` (other_processing, extraction) — manifest_declaration — [pyproject.toml](https://github.com/khulnasoft/deepstack/blob/main/pyproject.toml)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/khulnasoft/deepstack/blob/1da02c91e4e3f51b4f6664d72886ef3cd7fc2b29/deepstack/components/converters/tika.py)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/khulnasoft/deepstack/blob/1da02c91e4e3f51b4f6664d72886ef3cd7fc2b29/deepstack/components/converters/__init__.py)

**Evidence trail**

- [api_response](https://github.com/khulnasoft/deepstack) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/khulnasoft/deepstack/blob/main/pyproject.toml) (source: github_api): "tika",  # TikaDocumentConverter
- [code_permalink](https://github.com/khulnasoft/deepstack/blob/1da02c91e4e3f51b4f6664d72886ef3cd7fc2b29/deepstack/components/converters/tika.py) (source: github_api): with LazyImport("Run 'pip install tika'") as tika_import:     from tika import parser as tika_parser
- [code_permalink](https://github.com/khulnasoft/deepstack/blob/1da02c91e4e3f51b4f6664d72886ef3cd7fc2b29/deepstack/components/converters/__init__.py) (source: github_api): from deepstack.components.converters.output_adapter import OutputAdapter from deepstack.components.converters.pdfminer import PDFMinerToDocument from deepstack.components.converters.pypdf import PyPDF
- [readme_excerpt](https://github.com/khulnasoft/deepstack/blob/main/README.md) (source: readme): <div align="center"> </div> [Deepstack](https://deepstack.khulnasoft.com/) is an end-to-end LLM framework that allows you to build applications powered by LLMs, Transformer models, vector search and m

### 187. paulgessinger/swift-paperless

**Repository / product**

- Repository: [https://github.com/paulgessinger/swift-paperless](https://github.com/paulgessinger/swift-paperless)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://swift-paperless.gessinger.dev/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| supporting: confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 9/100 (a score, not a probability)
- Raw weighted score: 0.45 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 22
  - Query: `"libreoffice" filename:docker-compose.yml`
  - Retrieved 30 of 466 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 10
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 22
  - Query: `"libreoffice" filename:docker-compose.yml`
  - Retrieved 30 of 466 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 10
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [demo/docker-compose.yml](https://github.com/paulgessinger/swift-paperless/blob/main/demo/docker-compose.yml)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [demo/docker-compose.yml](https://github.com/paulgessinger/swift-paperless/blob/main/demo/docker-compose.yml)

**Evidence trail**

- [api_response](https://github.com/paulgessinger/swift-paperless) (source: github_api): stars=990, fork=False, archived=False
- [readme_excerpt](https://github.com/paulgessinger/swift-paperless/blob/main/README.md) (source: readme): Paperless-ngx is a self-hosted document management system that helps you organize your documents digitally.
- [api_response](https://github.com/paulgessinger/swift-paperless) (source: github_api): stars=990, fork=False, archived=False
- [code_permalink](https://github.com/paulgessinger/swift-paperless/blob/main/demo/docker-compose.yml) (source: github_api): # docker-compose file for running paperless from the docker container registry. # This file contains everything paperless needs to run. # Paperless supports amd64, arm and arm64 hardware. # All compos
- [readme_excerpt](https://github.com/paulgessinger/swift-paperless/blob/main/README.md) (source: readme): Paperless-ngx is a self-hosted document management system that helps you organize your documents digitally.
- [api_response](https://github.com/paulgessinger/swift-paperless) (source: github_api): stars=990, fork=False, archived=False
- [code_permalink](https://github.com/paulgessinger/swift-paperless/blob/main/demo/docker-compose.yml) (source: github_api): # docker-compose file for running paperless from the docker container registry. # This file contains everything paperless needs to run. # Paperless supports amd64, arm and arm64 hardware. # All compos
- [manifest_line](https://github.com/paulgessinger/swift-paperless/blob/main/demo/docker-compose.yml) (source: github_api): # - Apache Tika and Gotenberg servers are started with paperless and paperless
- [manifest_line](https://github.com/paulgessinger/swift-paperless/blob/main/demo/docker-compose.yml) (source: github_api): #   Office documents (Word, Excel, Power Point and their LibreOffice counter-
- [readme_excerpt](https://github.com/paulgessinger/swift-paperless/blob/main/README.md) (source: readme): Paperless-ngx is a self-hosted document management system that helps you organize your documents digitally.
- [api_response](https://github.com/paulgessinger/swift-paperless) (source: github_api): stars=990, fork=False, archived=False
- [code_permalink](https://github.com/paulgessinger/swift-paperless/blob/main/demo/docker-compose.yml) (source: github_api): # docker-compose file for running paperless from the docker container registry. # This file contains everything paperless needs to run. # Paperless supports amd64, arm and arm64 hardware. # All compos
- [manifest_line](https://github.com/paulgessinger/swift-paperless/blob/main/demo/docker-compose.yml) (source: github_api): # - Apache Tika and Gotenberg servers are started with paperless and paperless
- [manifest_line](https://github.com/paulgessinger/swift-paperless/blob/main/demo/docker-compose.yml) (source: github_api): #   Office documents (Word, Excel, Power Point and their LibreOffice counter-
- [readme_excerpt](https://github.com/paulgessinger/swift-paperless/blob/main/README.md) (source: readme): Paperless-ngx is a self-hosted document management system that helps you organize your documents digitally.

### 188. selkies-project/docker-selkies-glx-desktop

**Repository / product**

- Repository: [https://github.com/selkies-project/docker-selkies-glx-desktop](https://github.com/selkies-project/docker-selkies-glx-desktop)
- Company: Unknown — not stated in the repository
- Product: docker-selkies-glx-desktop
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://github.com/selkies-project/docker-selkies-glx-desktop/pkgs/container/nvidia-glx-desktop

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| supporting: confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 9/100 (a score, not a probability)
- Raw weighted score: 0.45 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 23
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 23
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [code](https://github.com/selkies-project/docker-selkies-glx-desktop/blob/main/Dockerfile)

**Evidence trail**

- [api_response](https://github.com/selkies-project/docker-selkies-glx-desktop) (source: github_api): stars=451, fork=False, archived=False
- [code_permalink](https://github.com/selkies-project/docker-selkies-glx-desktop/blob/main/Dockerfile) (source: github_api): libreoffice \
- [readme_excerpt](https://github.com/selkies-project/docker-selkies-glx-desktop/blob/main/README.md) (source: readme): KDE Plasma Desktop container designed for Kubernetes, supporting OpenGL EGL and GLX, Vulkan, and Wine/Proton for NVIDIA GPUs through WebRTC and HTML5, providing an open-source remote cloud/HPC graphic
- [api_response](https://github.com/selkies-project/docker-selkies-glx-desktop) (source: github_api): stars=451, fork=False, archived=False
- [code_permalink](https://github.com/selkies-project/docker-selkies-glx-desktop/blob/main/Dockerfile) (source: github_api): # This Source Code Form is subject to the terms of the Mozilla Public # License, v. 2.0. If a copy of the MPL was not distributed with this # file, You can obtain one at https://mozilla.org/MPL/2.0/.
- [code_permalink](https://github.com/selkies-project/docker-selkies-glx-desktop/blob/main/Dockerfile) (source: github_api): libreoffice \
- [code_permalink](https://github.com/selkies-project/docker-selkies-glx-desktop/blob/main/Dockerfile) (source: github_api): libreoffice \
- [readme_excerpt](https://github.com/selkies-project/docker-selkies-glx-desktop/blob/main/README.md) (source: readme): KDE Plasma Desktop container designed for Kubernetes, supporting OpenGL EGL and GLX, Vulkan, and Wine/Proton for NVIDIA GPUs through WebRTC and HTML5, providing an open-source remote cloud/HPC graphic

### 189. mementoweb/SiteStory

**Repository / product**

- Repository: [https://github.com/mementoweb/sitestory](https://github.com/mementoweb/sitestory)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=2, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| supporting: category_count=2 \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 8/100 (a score, not a probability)
- Raw weighted score: 0.40 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 2 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Apache POI (XWPF/HWPF)`, run `run_2`, window `size:8001..16000`, rank 26
  - Query: `"poi" filename:pom.xml size:8001..16000`
  - Sampled 30 of 20,352 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 20,352 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `iText`, run `run_2`, window `size:8001..16000`, rank 22
  - Query: `"itext" filename:pom.xml size:8001..16000`
  - Sampled 30 of 3,464 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,464 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Apache POI (XWPF/HWPF)` (docx, generation) — manifest_declaration — [sitestory-core/pom.xml](https://github.com/mementoweb/SiteStory/blob/4e3a70e1c8315efc5d1e2677a26633a9ab2f1af0/sitestory-core/pom.xml)
- `iText` (pdf, generation) — manifest_declaration — [sitestory-core/pom.xml](https://github.com/mementoweb/SiteStory/blob/4e3a70e1c8315efc5d1e2677a26633a9ab2f1af0/sitestory-core/pom.xml)

**Evidence trail**

- [api_response](https://github.com/mementoweb/SiteStory) (source: github_api): stars=14, fork=False, archived=False
- [manifest_line](https://github.com/mementoweb/SiteStory/blob/4e3a70e1c8315efc5d1e2677a26633a9ab2f1af0/sitestory-core/pom.xml) (source: github_api): <artifactId>spring-expression</artifactId>           </exclusion>          <exclusion>          <groupId>poi</groupId>               <artifactId>poi</artifactId>          </exclusion>
- [manifest_line](https://github.com/mementoweb/SiteStory/blob/4e3a70e1c8315efc5d1e2677a26633a9ab2f1af0/sitestory-core/pom.xml) (source: github_api): </exclusion>            <exclusion>            <groupId>itext</groupId>             <artifactId>itext</artifactId>           </exclusion>           <exclusion>           <groupId>org.dnsjava

### 190. JoachimSchaeffer/AttackSelection

**Repository / product**

- Repository: [https://github.com/joachimschaeffer/attackselection](https://github.com/joachimschaeffer/attackselection)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=2, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| supporting: category_count=2 \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 8/100 (a score, not a probability)
- Raw weighted score: 0.40 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 2 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 22
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_1`, window `size:1001..2000`, rank 23
  - Query: `"python-docx" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 8,336 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 8,336 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 22
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [BCB/docker/docker-requirements.txt](https://github.com/JoachimSchaeffer/AttackSelection/blob/1a0b4c6bf5a125a55b7512fb5ff910da437ad041/BCB/docker/docker-requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [BCB/docker/docker-requirements.txt](https://github.com/JoachimSchaeffer/AttackSelection/blob/1a0b4c6bf5a125a55b7512fb5ff910da437ad041/BCB/docker/docker-requirements.txt)

**Evidence trail**

- [api_response](https://github.com/JoachimSchaeffer/AttackSelection) (source: github_api): stars=4, fork=False, archived=False
- [manifest_line](https://github.com/JoachimSchaeffer/AttackSelection/blob/1a0b4c6bf5a125a55b7512fb5ff910da437ad041/BCB/docker/docker-requirements.txt) (source: github_api): sympy==1.12 pyfakefs==5.4.1 textblob==0.18.0 docxtpl==0.11.5 statsmodels==0.14.0 pyquery==1.4.3 holidays==0.29
- [manifest_line](https://github.com/JoachimSchaeffer/AttackSelection/blob/1a0b4c6bf5a125a55b7512fb5ff910da437ad041/BCB/docker/docker-requirements.txt) (source: github_api): Pillow==10.3.0 beautifulsoup4==4.8.2 datetime==5.5 python-docx==1.1.0 openpyxl==3.1.2 Levenshtein==0.25.0 PyYAML==6.0.1

### 191. makinacorpus/convertit

**Repository / product**

- Repository: [https://github.com/makinacorpus/convertit](https://github.com/makinacorpus/convertit)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 7/100 (a score, not a probability)
- Raw weighted score: 0.35 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 19
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 19
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [code](https://github.com/makinacorpus/convertit/blob/master/Dockerfile)
- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — code_import — [code](https://github.com/makinacorpus/convertit/blob/4768f910d9cbf64af75a70e598f6ff350ca18238/convertit/converters/unoconv.py)

**Evidence trail**

- [api_response](https://github.com/makinacorpus/convertit) (source: github_api): stars=26, fork=False, archived=False
- [code_permalink](https://github.com/makinacorpus/convertit/blob/master/Dockerfile) (source: github_api): RUN apt-get update && apt-get install -y -qq python3 libreoffice default-jre libreoffice-java-common inkscape python3-magic && \
- [code_permalink](https://github.com/makinacorpus/convertit/blob/4768f910d9cbf64af75a70e598f6ff350ca18238/convertit/converters/unoconv.py) (source: github_api): def unoconv(output_path, output_format, source):     command = [         'libreoffice', '--headless',         '--convert-to', output_format,         '--outdir', output_path, source     ]
- [api_response](https://github.com/makinacorpus/convertit) (source: github_api): stars=26, fork=False, archived=False
- [code_permalink](https://github.com/makinacorpus/convertit/blob/master/Dockerfile) (source: github_api): ARG DISTRO=noble FROM ubuntu:${DISTRO} AS base LABEL org.opencontainers.image.authors="Makina Corpus <contact@makina-corpus.com>" RUN apt-get update && apt-get install -y -qq python3 libreoffice def
- [code_permalink](https://github.com/makinacorpus/convertit/blob/master/Dockerfile) (source: github_api): RUN apt-get update && apt-get install -y -qq python3 libreoffice default-jre libreoffice-java-common inkscape python3-magic && \
- [code_permalink](https://github.com/makinacorpus/convertit/blob/master/Dockerfile) (source: github_api): RUN apt-get update && apt-get install -y -qq python3 libreoffice default-jre libreoffice-java-common inkscape python3-magic && \
- [code_permalink](https://github.com/makinacorpus/convertit/blob/4768f910d9cbf64af75a70e598f6ff350ca18238/convertit/converters/unoconv.py) (source: github_api): def unoconv(output_path, output_format, source):     command = [         'libreoffice', '--headless',         '--convert-to', output_format,         '--outdir', output_path, source     ]

### 192. octos-org/octos

**Repository / product**

- Repository: [https://github.com/octos-org/octos](https://github.com/octos-org/octos)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| supporting: confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 7/100 (a score, not a probability)
- Raw weighted score: 0.35 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 7
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 7
  - Query: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `LibreOffice headless / unoconv / JODConverter` (conversion, conversion) — infrastructure_reference — [code](https://github.com/octos-org/octos/blob/main/Dockerfile)

**Evidence trail**

- [api_response](https://github.com/octos-org/octos) (source: github_api): stars=1031, fork=False, archived=False
- [code_permalink](https://github.com/octos-org/octos/blob/main/Dockerfile) (source: github_api): # LibreOffice + Poppler for office document conversion and visual QA
- [readme_excerpt](https://github.com/octos-org/octos/blob/main/README.md) (source: readme): Use the installer script instead — see [self-hosted install options](https://github.com/octos-org/octos-web#self-hosting--deployment): curl -fsSL https://github.com/octos-org/octos/releases/latest/dow
- [api_response](https://github.com/octos-org/octos) (source: github_api): stars=1031, fork=False, archived=False
- [code_permalink](https://github.com/octos-org/octos/blob/main/Dockerfile) (source: github_api): # ============================================================ # Stage 1: Build the octos binary # ============================================================ FROM rust:1.88-alpine AS builder RUN ap
- [code_permalink](https://github.com/octos-org/octos/blob/main/Dockerfile) (source: github_api): # LibreOffice + Poppler for office document conversion and visual QA
- [code_permalink](https://github.com/octos-org/octos/blob/main/Dockerfile) (source: github_api): # LibreOffice + Poppler for office document conversion and visual QA
- [readme_excerpt](https://github.com/octos-org/octos/blob/main/README.md) (source: readme): Use the installer script instead — see [self-hosted install options](https://github.com/octos-org/octos-web#self-hosting--deployment): curl -fsSL https://github.com/octos-org/octos/releases/latest/dow

### 193. CitizenLabDotCo/citizenlab

**Repository / product**

- Repository: [https://github.com/citizenlabdotco/citizenlab](https://github.com/citizenlabdotco/citizenlab)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.govocal.com

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: infrastructure_service_present=true; confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 7/100 (a score, not a probability)
- Raw weighted score: 0.35 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 1 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Gotenberg`, run `run_1`, window `unsliced`, rank 14
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Gotenberg`, run `run_2`, window `unsliced`, rank 14
  - Query: `"gotenberg/gotenberg" filename:docker-compose.yml`
  - Retrieved 30 of 648 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `docx (dolanmiu/docx)`, run `run_2`, window `size:8001..16000`, rank 27
  - Query: `"docx" filename:package.json size:8001..16000`
  - Retrieved 30 of 482 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Gotenberg` (conversion, conversion) — infrastructure_reference — [code](https://github.com/CitizenLabDotCo/citizenlab/blob/master/docker-compose.yml)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/app/services/gotenberg_client.rb)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/spec/services/gotenberg_client_spec.rb)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/app/services/files/preview_service.rb)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/app/jobs/export/pdf/input_responses_job.rb)
- `Gotenberg` (conversion, conversion) — code_import — [code](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/spec/jobs/export/pdf/input_responses_job_spec.rb)

**Evidence trail**

- [api_response](https://github.com/CitizenLabDotCo/citizenlab) (source: github_api): stars=236, fork=False, archived=False
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/master/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/app/services/gotenberg_client.rb) (source: github_api): class GotenbergClient   # Web-request callers must fail fast (not pin Puma workers); only background   # jobs pass JOB_TIMEOUT_SECONDS. It sits slightly above Gotenberg's   # --api-timeout of 600s (s
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/spec/services/gotenberg_client_spec.rb) (source: github_api): describe '#render_html_to_pdf' do     it 'raises HttpError on non-2xx response' do       url = "#{ENV.fetch('GOTENBERG_PDF_URL', 'http://gotenberg:3000')}/forms/chromium/convert/html"       stub_re
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/app/services/files/preview_service.rb) (source: github_api): def initialize       @gotenberg = GotenbergClient.new     end
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/app/jobs/export/pdf/input_responses_job.rb) (source: github_api): # Renders the input responses PDF of a phase in the background (the     # Gotenberg render takes minutes for large phases) and stores the result as     # a transient +Export::ResultFile+ for the r
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/spec/jobs/export/pdf/input_responses_job_spec.rb) (source: github_api): owner_id: owner.id,         total: 3, # 2 inputs + 1 reserved for the Gotenberg render         progress: 0
- [api_response](https://github.com/CitizenLabDotCo/citizenlab) (source: github_api): stars=236, fork=False, archived=False
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/master/docker-compose.yml) (source: github_api): services:   postgres:     # When you update PostgreSQL, make sure to upgrade the `postgresql-client` version     # in `Dockerfile` and `Dockerfile.development`. This ensures that `pg_dump` and     # `
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/master/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/master/docker-compose.yml) (source: github_api): gotenberg:
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/app/services/gotenberg_client.rb) (source: github_api): class GotenbergClient   # Web-request callers must fail fast (not pin Puma workers); only background   # jobs pass JOB_TIMEOUT_SECONDS. It sits slightly above Gotenberg's   # --api-timeout of 600s (s
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/spec/services/gotenberg_client_spec.rb) (source: github_api): describe '#render_html_to_pdf' do     it 'raises HttpError on non-2xx response' do       url = "#{ENV.fetch('GOTENBERG_PDF_URL', 'http://gotenberg:3000')}/forms/chromium/convert/html"       stub_re
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/app/services/files/preview_service.rb) (source: github_api): def initialize       @gotenberg = GotenbergClient.new     end
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/app/jobs/export/pdf/input_responses_job.rb) (source: github_api): # Renders the input responses PDF of a phase in the background (the     # Gotenberg render takes minutes for large phases) and stores the result as     # a transient +Export::ResultFile+ for the r
- [code_permalink](https://github.com/CitizenLabDotCo/citizenlab/blob/8d8d76e04777c61bcfa3829d586fe5e854e1b365/back/spec/jobs/export/pdf/input_responses_job_spec.rb) (source: github_api): owner_id: owner.id,         total: 3, # 2 inputs + 1 reserved for the Gotenberg render         progress: 0

### 194. AtlasOfLivingAustralia/fieldcapture

**Repository / product**

- Repository: [https://github.com/atlasoflivingaustralia/fieldcapture](https://github.com/atlasoflivingaustralia/fieldcapture)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://fieldcapture.ala.org.au

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| supporting: template_directory_present=true \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 5/100 (a score, not a probability)
- Raw weighted score: 0.25 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Apache POI (XWPF/HWPF)`, run `run_2`, window `size:8001..16000`, rank 16
  - Query: `"poi" filename:build.gradle size:8001..16000`
  - Sampled 30 of 6,296 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 6,296 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Apache POI (XWPF/HWPF)` (docx, generation) — manifest_declaration — [build.gradle](https://github.com/AtlasOfLivingAustralia/fieldcapture/blob/dev/build.gradle)
- `Apache POI (XWPF/HWPF)` (docx, generation) — manifest_declaration — [package-lock.json](https://github.com/AtlasOfLivingAustralia/fieldcapture/blob/dev/package-lock.json)

**Evidence trail**

- [api_response](https://github.com/AtlasOfLivingAustralia/fieldcapture) (source: github_api): stars=5, fork=False, archived=False
- [manifest_line](https://github.com/AtlasOfLivingAustralia/fieldcapture/blob/dev/build.gradle) (source: github_api): implementation 'org.apache.poi:ooxml-schemas:1.4'
- [manifest_line](https://github.com/AtlasOfLivingAustralia/fieldcapture/blob/dev/package-lock.json) (source: github_api): "node_modules/is-fullwidth-code-point": {
- [other](https://github.com/AtlasOfLivingAustralia/fieldcapture/tree/dev/forms) (source: github_api): directory forms/ present

### 195. isle-project/isle-editor

**Repository / product**

- Repository: [https://github.com/isle-project/isle-editor](https://github.com/isle-project/isle-editor)
- Company: Unknown — not stated in the repository
- Product: *ISLE Editor* [![LICENSE][license-image]][license-url]
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://isledocs.com

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| supporting: template_directory_present=true \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 5/100 (a score, not a probability)
- Raw weighted score: 0.25 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `PDFKit`, run `run_2`, window `size:>16000`, rank 11
  - Query: `"pdfkit" filename:package.json size:>16000`
  - Retrieved 30 of 376 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `PDFKit` (pdf, generation) — manifest_declaration — [package.json](https://github.com/isle-project/isle-editor/blob/master/package.json)

**Evidence trail**

- [api_response](https://github.com/isle-project/isle-editor) (source: github_api): stars=19, fork=False, archived=False
- [manifest_line](https://github.com/isle-project/isle-editor/blob/master/package.json) (source: github_api): "!node_modules/@foliojs-fork/pdfkit/**/*",
- [other](https://github.com/isle-project/isle-editor/tree/master/templates) (source: github_api): directory templates/ present

### 196. archerysec/archerysec

**Repository / product**

- Repository: [https://github.com/archerysec/archerysec](https://github.com/archerysec/archerysec)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.archerysec.com/

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| supporting: template_directory_present=true \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 5/100 (a score, not a probability)
- Raw weighted score: 0.25 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `pypdf / PyPDF2`, run `run_2`, window `size:4001..8000`, rank 23
  - Query: `"pypdf" filename:pyproject.toml size:4001..8000`
  - Sampled 30 of 2,588 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,588 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `ReportLab`, run `run_2`, window `size:4001..8000`, rank 10
  - Query: `"reportlab" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 769 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/archerysec/archerysec/blob/master/pyproject.toml)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [pyproject.toml](https://github.com/archerysec/archerysec/blob/master/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/archerysec/archerysec) (source: github_api): stars=2470, fork=False, archived=False
- [manifest_line](https://github.com/archerysec/archerysec/blob/master/pyproject.toml) (source: github_api): reportlab = ">=3.6.11"
- [manifest_line](https://github.com/archerysec/archerysec/blob/master/pyproject.toml) (source: github_api): PyPDF2 = ">=2.10.2"
- [other](https://github.com/archerysec/archerysec/tree/master/templates) (source: github_api): directory templates/ present

### 197. Scouterna/skojjt

**Repository / product**

- Repository: [https://github.com/scouterna/skojjt](https://github.com/scouterna/skojjt)
- Company: Unknown — not stated in the repository
- Product: Skojjt
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| supporting: template_directory_present=true \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 5/100 (a score, not a probability)
- Raw weighted score: 0.25 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docx-mailmerge / docxedit`, run `run_1`, window `unsliced`, rank 7
  - Query: `"docx-mailmerge" filename:requirements.txt`
  - Retrieved 30 of 113 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docx-mailmerge / docxedit`, run `run_2`, window `unsliced`, rank 7
  - Query: `"docx-mailmerge" filename:requirements.txt`
  - Retrieved 30 of 113 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docx-mailmerge / docxedit` (other_processing, generation) — manifest_declaration — [requirements.txt](https://github.com/Scouterna/skojjt/blob/GAE/master/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/Scouterna/skojjt) (source: github_api): stars=14, fork=False, archived=False
- [manifest_line](https://github.com/Scouterna/skojjt/blob/GAE/master/requirements.txt) (source: github_api): docx-mailmerge==0.5.0
- [other](https://github.com/Scouterna/skojjt/tree/GAE/master/templates) (source: github_api): directory templates/ present

### 198. philips-software/amp-devcontainer

**Repository / product**

- Repository: [https://github.com/philips-software/amp-devcontainer](https://github.com/philips-software/amp-devcontainer)
- Company: Unknown — not stated in the repository
- Product: amp-devcontainer
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| supporting: template_directory_present=true \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 5/100 (a score, not a probability)
- Raw weighted score: 0.25 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docxtpl (python-docx-template)`, run `run_1`, window `unsliced`, rank 28
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `docxtpl (python-docx-template)`, run `run_2`, window `unsliced`, rank 28
  - Query: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_2`, window `size:>16000`, rank 8
  - Query: `"python-docx" filename:requirements.txt size:>16000`
  - Retrieved 30 of 571 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docxtpl (python-docx-template)` (template_generation, generation) — manifest_declaration — [.devcontainer/docs/requirements.txt](https://github.com/philips-software/amp-devcontainer/blob/e53bbb90ea32459a29ebb42278c55615cecfcbba/.devcontainer/docs/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/philips-software/amp-devcontainer) (source: github_api): stars=134, fork=False, archived=False
- [manifest_line](https://github.com/philips-software/amp-devcontainer/blob/e53bbb90ea32459a29ebb42278c55615cecfcbba/.devcontainer/docs/requirements.txt) (source: github_api): # via sbdl docxtpl==0.20.2 \     --hash=sha256:626d5c570a46a62b2ca73b4d08f1c240fa031a5bc45371e1466a4fe184923d10 \
- [other](https://github.com/philips-software/amp-devcontainer/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/philips-software/amp-devcontainer/blob/main/README.md) (source: readme): The amp-devcontainer-base image is a shared foundation used by the other flavors.

### 199. RedPlanetHQ/core

**Repository / product**

- Repository: [https://github.com/redplanethq/core](https://github.com/redplanethq/core)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://getcore.me

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 4/100 (a score, not a probability)
- Raw weighted score: 0.20 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:8001..16000`, rank 27
  - Query: `"mammoth" filename:package.json size:8001..16000`
  - Retrieved 30 of 737 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [apps/webapp/package.json](https://github.com/RedPlanetHQ/core/blob/549301e79f1def9e7ee3fed9930e273787dc3171/apps/webapp/package.json)

**Evidence trail**

- [api_response](https://github.com/RedPlanetHQ/core) (source: github_api): stars=1948, fork=False, archived=False
- [manifest_line](https://github.com/RedPlanetHQ/core/blob/549301e79f1def9e7ee3fed9930e273787dc3171/apps/webapp/package.json) (source: github_api): "lowlight": "^3.3.0",     "lucide-react": "^0.563.0",     "luxon": "^3.7.2",     "mammoth": "^1.12.0",     "marked": "^17.0.4",     "mastra": "^1.19.0",     "morgan": "^1.10.0",
- [readme_excerpt](https://github.com/RedPlanetHQ/core/blob/main/README.md) (source: readme): Open source, self-hosted, yours forever.

### 200. ag-ui-protocol/ag-ui

**Repository / product**

- Repository: [https://github.com/ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://ag-ui.com

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 4/100 (a score, not a probability)
- Raw weighted score: 0.20 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 4/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:4001..8000`, rank 20
  - Query: `"PyMuPDF" filename:pyproject.toml size:4001..8000`
  - Retrieved 30 of 892 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [integrations/crew-ai/python/pyproject.toml](https://github.com/ag-ui-protocol/ag-ui/blob/821b8c227c6fe7b78de2c8259173dd7cbbdf181b/integrations/crew-ai/python/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/ag-ui-protocol/ag-ui) (source: github_api): stars=15499, fork=False, archived=False
- [manifest_line](https://github.com/ag-ui-protocol/ag-ui/blob/821b8c227c6fe7b78de2c8259173dd7cbbdf181b/integrations/crew-ai/python/pyproject.toml) (source: github_api): # # ``crewai-tools`` is NOT a runtime dependency (CPK-7721 review #6): the bridge # imports nothing from it (``grep -rn crewai_tools ag_ui_crewai/ tests/`` is # empty), yet as a hard dep it drags in ~
- [readme_excerpt](https://github.com/ag-ui-protocol/ag-ui/blob/main/README.md) (source: readme): Built for simplicity and flexibility, it enables seamless integration between AI agents, real time user context, and user interfaces.

### 201. DirectumCompany/rx-util-importdata

**Repository / product**

- Repository: [https://github.com/directumcompany/rx-util-importdata](https://github.com/directumcompany/rx-util-importdata)
- Company: Unknown — not stated in the repository
- Product: rx-util-importdata
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| supporting: template_directory_present=true \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 3/100 (a score, not a probability)
- Raw weighted score: 0.15 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Aspose.Words`, run `run_2`, window `size:>16000`, rank 16
  - Query: `"Aspose.Words" extension:csproj size:>16000`
  - Retrieved 30 of 219 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Aspose.Words` (docx, generation) — manifest_declaration — [src/ImportData/ImportData.csproj](https://github.com/DirectumCompany/rx-util-importdata/blob/e6f505cdef9f48b90b09f2ae5955741610cbefdd/src/ImportData/ImportData.csproj)

**Evidence trail**

- [api_response](https://github.com/DirectumCompany/rx-util-importdata) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/DirectumCompany/rx-util-importdata/blob/e6f505cdef9f48b90b09f2ae5955741610cbefdd/src/ImportData/ImportData.csproj) (source: github_api): <HintPath>\\orpihost\Sungero\DirectumX\3.6.29.0\DrxUtil\Aspose.HTML.dll</HintPath>     </Reference>     <Reference Include="Aspose.Words">       <HintPath>\\orpihost\Sungero\DirectumX\3.6.29.
- [other](https://github.com/DirectumCompany/rx-util-importdata/tree/master/Template) (source: github_api): directory Template/ present

### 202. Kentico/xperience-by-kentico-kentico-migration-tool

**Repository / product**

- Repository: [https://github.com/kentico/xperience-by-kentico-kentico-migration-tool](https://github.com/kentico/xperience-by-kentico-kentico-migration-tool)
- Company: Unknown — not stated in the repository
- Product: Xperience by Kentico: Kentico Migration Tool
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 2/100 (a score, not a probability)
- Raw weighted score: 0.10 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Open XML SDK`, run `run_2`, window `size:8001..16000`, rank 5
  - Query: `"DocumentFormat.OpenXml" filename:packages.config size:8001..16000`
  - Retrieved 30 of 324 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Open XML SDK` (docx, generation) — manifest_declaration — [KX13.NET48.Extensions/packages.config](https://github.com/Kentico/xperience-by-kentico-kentico-migration-tool/blob/6086a7fdf12b4b02d9acbe06a02f0eced72d1de8/KX13.NET48.Extensions/packages.config)

**Evidence trail**

- [api_response](https://github.com/Kentico/xperience-by-kentico-kentico-migration-tool) (source: github_api): stars=29, fork=False, archived=False
- [manifest_line](https://github.com/Kentico/xperience-by-kentico-kentico-migration-tool/blob/6086a7fdf12b4b02d9acbe06a02f0eced72d1de8/KX13.NET48.Extensions/packages.config) (source: github_api): <package id="AWSSDK.S3" version="3.3.104.36" targetFramework="net48" />   <package id="AngleSharp" version="0.14.0" targetFramework="net48" />   <package id="Antlr" version="3.5.0.2" targetFramework
- [readme_excerpt](https://github.com/Kentico/xperience-by-kentico-kentico-migration-tool/blob/master/README.md) (source: readme): This project has **Full support by 7-day bug-fix policy**: Bug fixes are applied to the latest version only (no backporting to previous releases) The Migration Tool is a temporary utility designed for

### 203. Hitendra-Cyber/Data-Guard

**Repository / product**

- Repository: [https://github.com/hitendra-cyber/data-guard](https://github.com/hitendra-cyber/data-guard)
- Company: Unknown — not stated in the repository
- Product: 🛡️ Data Quality Guard
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 2/100 (a score, not a probability)
- Raw weighted score: 0.10 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `pdf2docx`, run `run_2`, window `size:4001..8000`, rank 24
  - Query: `"pdf2docx" filename:requirements.txt size:4001..8000`
  - Retrieved 30 of 117 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pdf2docx` (other_processing, mixed) — manifest_declaration — [requirements.txt](https://github.com/Hitendra-Cyber/Data-Guard/blob/main/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/Hitendra-Cyber/Data-Guard) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/Hitendra-Cyber/Data-Guard/blob/main/requirements.txt) (source: github_api): pdf2docx==0.5.8
- [readme_excerpt](https://github.com/Hitendra-Cyber/Data-Guard/blob/main/README.md) (source: readme): Designed for analysts, students, and businesses, the tool ensures datasets are reliable and ready for reporting, analytics, or machine learning workflows.

### 204. AIE-enginehub/personERP-SERVER

**Repository / product**

- Repository: [https://github.com/aie-enginehub/personerp-server](https://github.com/aie-enginehub/personerp-server)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 2/100 (a score, not a probability)
- Raw weighted score: 0.10 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `iText`, run `run_2`, window `size:>16000`, rank 22
  - Query: `"itext" filename:build.gradle size:>16000`
  - Retrieved 30 of 174 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `iText` (pdf, generation) — manifest_declaration — [build.gradle](https://github.com/AIE-enginehub/personERP-SERVER/blob/master/build.gradle)

**Evidence trail**

- [api_response](https://github.com/AIE-enginehub/personERP-SERVER) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/AIE-enginehub/personERP-SERVER/blob/master/build.gradle) (source: github_api): compile 'com.lowagie:itext:2.1.7'
- [readme_excerpt](https://github.com/AIE-enginehub/personERP-SERVER/blob/master/README.md) (source: readme): For example: `gradlew "ofbiz --help"` Shortcuts to task names can be used by writing the first letter of every word in a task name.

### 205. kvcache-ai/TrEnv-X

**Repository / product**

- Repository: [https://github.com/kvcache-ai/trenv-x](https://github.com/kvcache-ai/trenv-x)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 2/100 (a score, not a probability)
- Raw weighted score: 0.10 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `python-docx`, run `run_1`, window `size:251..500`, rank 9
  - Query: `"python-docx" filename:requirements.txt size:251..500`
  - Sampled 30 of 16,192 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 16,192 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_1`, window `size:501..1000`, rank 9
  - Query: `"python-docx" filename:requirements.txt size:501..1000`
  - Sampled 30 of 11,984 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 11,984 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `pypdf / PyPDF2`, run `run_2`, window `size:4001..8000`, rank 8
  - Query: `"pypdf" filename:requirements.txt size:4001..8000`
  - Sampled 30 of 8,208 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 8,208 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `PyMuPDF (fitz)`, run `run_2`, window `size:4001..8000`, rank 6
  - Query: `"PyMuPDF" filename:requirements.txt size:4001..8000`
  - Sampled 30 of 3,352 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,352 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Unstructured`, run `run_2`, window `size:4001..8000`, rank 9
  - Query: `"unstructured" filename:requirements.txt size:4001..8000`
  - Sampled 30 of 1,700 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,700 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `python-docx`, run `run_2`, window `size:4001..8000`, rank 6
  - Query: `"python-docx" filename:requirements.txt size:4001..8000`
  - Sampled 30 of 4,552 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 4,552 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `python-docx` (docx, generation) — manifest_declaration — [packages/fc-rootfs/ci-requirements.txt](https://github.com/kvcache-ai/TrEnv-X/blob/8bb02dc99df909f065322b576812401657680311/packages/fc-rootfs/ci-requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [packages/fc-rootfs/metagpt-requirements.txt](https://github.com/kvcache-ai/TrEnv-X/blob/8bb02dc99df909f065322b576812401657680311/packages/fc-rootfs/metagpt-requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [packages/fc-rootfs/default-requirements.txt](https://github.com/kvcache-ai/TrEnv-X/blob/8bb02dc99df909f065322b576812401657680311/packages/fc-rootfs/default-requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [packages/fc-rootfs/owl-requirements.txt](https://github.com/kvcache-ai/TrEnv-X/blob/8bb02dc99df909f065322b576812401657680311/packages/fc-rootfs/owl-requirements.txt)

**Evidence trail**

- [api_response](https://github.com/kvcache-ai/TrEnv-X) (source: github_api): stars=98, fork=False, archived=False
- [manifest_line](https://github.com/kvcache-ai/TrEnv-X/blob/8bb02dc99df909f065322b576812401657680311/packages/fc-rootfs/ci-requirements.txt) (source: github_api): pandas==1.5.3 plotly==5.19.0 pytest==8.1.0 python-docx==1.1.0 pytz==2024.1 requests==2.26.0 scikit-image==0.22.0
- [manifest_line](https://github.com/kvcache-ai/TrEnv-X/blob/8bb02dc99df909f065322b576812401657680311/packages/fc-rootfs/metagpt-requirements.txt) (source: github_api): pandas==2.2.2 plotly==5.22.0 pytest==8.2.2 python-docx==1.1.2 pytz==2024.1 requests==2.32.3 scikit-image==0.24.0
- [manifest_line](https://github.com/kvcache-ai/TrEnv-X/blob/8bb02dc99df909f065322b576812401657680311/packages/fc-rootfs/default-requirements.txt) (source: github_api): pandas==1.5.3 plotly==5.19.0 pytest==8.1.0 python-docx==1.1.0 pytz==2024.1 requests==2.26.0 scikit-image==0.22.0
- [manifest_line](https://github.com/kvcache-ai/TrEnv-X/blob/8bb02dc99df909f065322b576812401657680311/packages/fc-rootfs/owl-requirements.txt) (source: github_api): pytest-asyncio==0.23.8 pytest-cov==4.1.0 python-dateutil==2.8.2 python-docx==1.1.2 python-dotenv==1.0.1 python-iso639==2025.2.18 python-magic==0.4.27
- [readme_excerpt](https://github.com/kvcache-ai/TrEnv-X/blob/main/README.md) (source: readme): </h3> TrENV-X is an open-source runtime platform designed for AI Agent applications.

### 206. coderfolks/Rccs

**Repository / product**

- Repository: [https://github.com/coderfolks/rccs](https://github.com/coderfolks/rccs)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 2/100 (a score, not a probability)
- Raw weighted score: 0.10 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `iText`, run `run_2`, window `size:>16000`, rank 30
  - Query: `"itext" filename:build.gradle size:>16000`
  - Retrieved 30 of 174 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `iText` (pdf, generation) — manifest_declaration — [build.gradle](https://github.com/coderfolks/Rccs/blob/master/build.gradle)

**Evidence trail**

- [api_response](https://github.com/coderfolks/Rccs) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/coderfolks/Rccs/blob/master/build.gradle) (source: github_api): compile 'com.lowagie:itext:2.1.7'
- [readme_excerpt](https://github.com/coderfolks/Rccs/blob/master/README.md) (source: readme): For example: `gradlew "ofbiz --help"` Shortcuts to task names can be used by writing the first letter of every word in a task name.

### 207. hisachin/chathive

**Repository / product**

- Repository: [https://github.com/hisachin/chathive](https://github.com/hisachin/chathive)
- Company: Unknown — not stated in the repository
- Product: **ChatHive: Conversational AI with GPT-4, Pinecone, LangChain, and MongoDB**
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 2/100 (a score, not a probability)
- Raw weighted score: 0.10 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `mammoth / python-mammoth`, run `run_2`, window `size:2001..4000`, rank 25
  - Query: `"mammoth" filename:package.json size:2001..4000`
  - Sampled 30 of 7,920 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,920 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [package-lock.json](https://github.com/hisachin/chathive/blob/master/package-lock.json)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [package.json](https://github.com/hisachin/chathive/blob/master/package.json)

**Evidence trail**

- [api_response](https://github.com/hisachin/chathive) (source: github_api): stars=37, fork=False, archived=False
- [manifest_line](https://github.com/hisachin/chathive/blob/master/package-lock.json) (source: github_api): "mammoth": "^1.5.1",
- [manifest_line](https://github.com/hisachin/chathive/blob/master/package.json) (source: github_api): "mammoth": "^1.5.1",
- [readme_excerpt](https://github.com/hisachin/chathive/blob/master/README.md) (source: readme): ChatHive is a powerful AI-driven chatbot application designed for interactive document-based conversations.

### 208. janderswag/docuchat.app

**Repository / product**

- Repository: [https://github.com/janderswag/docuchat.app](https://github.com/janderswag/docuchat.app)
- Company: Unknown — not stated in the repository
- Product: Legal Document Chat for Attorneys: Private, Self-Hosted, Cited
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://docuchat.app/

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| unknown: no dependency evidence located; company_name=null; contributor_count not collected

**Score**

- Score: 2/100 (a score, not a probability)
- Raw weighted score: 0.10 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 2/7 dimensions

- Document volume: Unknown
- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown

**Discovery provenance**

- Tier 3, `Docling`, run `run_2`, window `size:2001..4000`, rank 10
  - Query: `"docling" filename:requirements.txt size:2001..4000`
  - Retrieved 30 of 494 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/janderswag/docuchat.app) (source: github_api): stars=31, fork=False, archived=False
- [readme_excerpt](https://github.com/janderswag/docuchat.app/blob/main/README.md) (source: readme): This project is a **self-hosted, privacy-first** document-intelligence stack that runs **100% locally**: **Your documents never leave your machine.** Inference, embeddings, OCR, and storage are all lo

### 209. dundalek/closh

**Repository / product**

- Repository: [https://github.com/dundalek/closh](https://github.com/dundalek/closh)
- Company: Unknown — not stated in the repository
- Product: closh - Bash-like shell based on Clojure
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| unknown: no dependency evidence located; contributor_count not collected

**Score**

- Score: 2/100 (a score, not a probability)
- Raw weighted score: 0.10 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 2/7 dimensions

- Document volume: Unknown
- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 6
  - Query: `"unoconv"`
  - Sampled 30 of 17,216 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 17,216 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 6
  - Query: `"unoconv"`
  - Sampled 30 of 17,216 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 17,216 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/dundalek/closh) (source: github_api): stars=1627, fork=False, archived=False
- [api_response](https://github.com/dundalek/closh) (source: github_api): stars=1627, fork=False, archived=False
- [api_response](https://github.com/dundalek/closh) (source: github_api): stars=1627, fork=False, archived=False
- [api_response](https://github.com/dundalek/closh) (source: github_api): stars=1627, fork=False, archived=False

### 210. iltoga/BusinessSuite

**Repository / product**

- Repository: [https://github.com/iltoga/businesssuite](https://github.com/iltoga/businesssuite)
- Company: Unknown — not stated in the repository
- Product: BusinessSuite (RevisBali CRM/ERP)
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 2/100 (a score, not a probability)
- Raw weighted score: 0.10 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `docx-mailmerge / docxedit`, run `run_1`, window `unsliced`, rank 8
  - Query: `"docx-mailmerge" filename:pyproject.toml`
  - Retrieved 12 of 12 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 2, `docx-mailmerge / docxedit`, run `run_2`, window `unsliced`, rank 8
  - Query: `"docx-mailmerge" filename:pyproject.toml`
  - Retrieved 12 of 12 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docx-mailmerge / docxedit` (other_processing, generation) — manifest_declaration — [backend/pyproject.toml](https://github.com/iltoga/BusinessSuite/blob/main/backend/pyproject.toml)
- `docx-mailmerge / docxedit` (other_processing, generation) — manifest_declaration — [backend/requirements.txt](https://github.com/iltoga/BusinessSuite/blob/main/backend/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/iltoga/BusinessSuite) (source: github_api): stars=2, fork=False, archived=False
- [manifest_line](https://github.com/iltoga/BusinessSuite/blob/main/backend/pyproject.toml) (source: github_api): "docx-mailmerge>=0.5.0",
- [manifest_line](https://github.com/iltoga/BusinessSuite/blob/main/backend/requirements.txt) (source: github_api): docx-mailmerge==0.5.0
- [readme_excerpt](https://github.com/iltoga/BusinessSuite/blob/main/README.md) (source: readme): Python 3.12+ (backend deps are managed via `uv`) Bun 1.3+ (frontend) Docker (for local Postgres/Redis and optional all-in-one stack) This runs DB + Redis + backend + workers + scheduler + frontend con

### 211. remacs/remacs

**Repository / product**

- Repository: [https://github.com/remacs/remacs](https://github.com/remacs/remacs)
- Company: Free Software Foundation
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: no dependency evidence located; industry_category=unknown; contributor_count not collected

**Score**

- Score: 2/100 (a score, not a probability)
- Raw weighted score: 0.10 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 2/7 dimensions

- Document volume: Unknown
- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 9
  - Query: `"unoconv"`
  - Sampled 30 of 17,216 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 17,216 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 9
  - Query: `"unoconv"`
  - Sampled 30 of 17,216 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 17,216 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/remacs/remacs) (source: github_api): stars=4611, fork=False, archived=False
- [readme_excerpt](https://github.com/remacs/remacs/blob/master/README) (source: readme): company stated as 'Free Software Foundation'
- [readme_excerpt](https://github.com/remacs/remacs/blob/master/README) (source: readme): The file 'configure.ac' is the input used by the autoconf program to construct the 'configure' script.
- [api_response](https://github.com/remacs/remacs) (source: github_api): stars=4611, fork=False, archived=False
- [readme_excerpt](https://github.com/remacs/remacs/blob/master/README) (source: readme): company stated as 'Free Software Foundation'
- [readme_excerpt](https://github.com/remacs/remacs/blob/master/README) (source: readme): The file 'configure.ac' is the input used by the autoconf program to construct the 'configure' script.
- [api_response](https://github.com/remacs/remacs) (source: github_api): stars=4611, fork=False, archived=False
- [readme_excerpt](https://github.com/remacs/remacs/blob/master/README) (source: readme): company stated as 'Free Software Foundation'
- [readme_excerpt](https://github.com/remacs/remacs/blob/master/README) (source: readme): The file 'configure.ac' is the input used by the autoconf program to construct the 'configure' script.
- [api_response](https://github.com/remacs/remacs) (source: github_api): stars=4611, fork=False, archived=False
- [readme_excerpt](https://github.com/remacs/remacs/blob/master/README) (source: readme): company stated as 'Free Software Foundation'
- [readme_excerpt](https://github.com/remacs/remacs/blob/master/README) (source: readme): The file 'configure.ac' is the input used by the autoconf program to construct the 'configure' script.

### 212. rapid7/nexpose-warehouse-jasper-templates

**Repository / product**

- Repository: [https://github.com/rapid7/nexpose-warehouse-jasper-templates](https://github.com/rapid7/nexpose-warehouse-jasper-templates)
- Company: Unknown — not stated in the repository
- Product: Nexpose Warehouse Jasper Templates
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; company_name=null; contributor_count not collected

**Score**

- Score: 2/100 (a score, not a probability)
- Raw weighted score: 0.10 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 1 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 3/7 dimensions

- Document volume: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 2, `JasperReports / Apache FOP`, run `run_1`, window `unsliced`, rank 5
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 2, `JasperReports / Apache FOP`, run `run_2`, window `unsliced`, rank 5
  - Query: `"jasperreports" filename:pom.xml`
  - Sampled 30 of 10,944 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,944 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `iText`, run `run_2`, window `size:4001..8000`, rank 5
  - Query: `"itext" filename:pom.xml size:4001..8000`
  - Sampled 30 of 8,720 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 8,720 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `JasperReports / Apache FOP` (template_generation, generation) — manifest_declaration — [pom.xml](https://github.com/rapid7/nexpose-warehouse-jasper-templates/blob/master/pom.xml)

**Evidence trail**

- [api_response](https://github.com/rapid7/nexpose-warehouse-jasper-templates) (source: github_api): stars=5, fork=False, archived=False
- [manifest_line](https://github.com/rapid7/nexpose-warehouse-jasper-templates/blob/master/pom.xml) (source: github_api): <artifactId>jasperreports-plugin</artifactId>
- [readme_excerpt](https://github.com/rapid7/nexpose-warehouse-jasper-templates/blob/master/README.md) (source: readme): Nexpose Warehouse Jasper Templates is a set of report templates designed for use against a dimensional data warehouse populated by the Nexpose Data Warehouse feature.

### 213. fiyo/DBCheck

**Repository / product**

- Repository: [https://github.com/fiyo/dbcheck](https://github.com/fiyo/dbcheck)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://dbcheck.top

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| supporting: template_directory_present=true \| unknown: no dependency evidence located; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 0/100 (a score, not a probability)
- Raw weighted score: 0.00 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 1/7 dimensions

- Document volume: Unknown
- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `(co-occurrence query, spans multiple libraries)`, run `run_2`, window `size:4001..8000`, rank 15
  - Query: `"python-docx" "reportlab" filename:requirements.txt size:4001..8000`
  - Retrieved 30 of 515 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/fiyo/DBCheck) (source: github_api): stars=148, fork=False, archived=False
- [other](https://github.com/fiyo/DBCheck/tree/main/templates) (source: github_api): directory templates/ present

### 214. koskasmail/whatAmess

**Repository / product**

- Repository: [https://github.com/koskasmail/whatamess](https://github.com/koskasmail/whatamess)
- Company: Unknown — not stated in the repository
- Product: whatAmess
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| unknown: no dependency evidence located; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 0/100 (a score, not a probability)
- Raw weighted score: 0.00 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 1/7 dimensions

- Document volume: Unknown
- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Apache POI (XWPF/HWPF)`, run `run_2`, window `size:2001..4000`, rank 10
  - Query: `"poi" filename:pom.xml size:2001..4000`
  - Sampled 30 of 45,184 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 45,184 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Apache PDFBox`, run `run_2`, window `size:2001..4000`, rank 22
  - Query: `"pdfbox" filename:pom.xml size:2001..4000`
  - Sampled 30 of 6,672 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 6,672 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/koskasmail/whatAmess) (source: github_api): stars=0, fork=False, archived=False

### 215. elastic/elasticsearch

**Repository / product**

- Repository: [https://github.com/elastic/elasticsearch](https://github.com/elastic/elasticsearch)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.elastic.co/products/elasticsearch

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| unknown: no dependency evidence located; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 0/100 (a score, not a probability)
- Raw weighted score: 0.00 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 1/7 dimensions

- Document volume: Unknown
- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Apache PDFBox`, run `run_2`, window `size:4001..8000`, rank 1
  - Query: `"pdfbox" filename:build.gradle size:4001..8000`
  - Retrieved 30 of 764 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `Apache Tika`, run `run_2`, window `size:4001..8000`, rank 1
  - Query: `"tika" filename:build.gradle size:4001..8000`
  - Retrieved 30 of 798 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/elastic/elasticsearch) (source: github_api): stars=77855, fork=False, archived=False

### 216. ryumada/docker-odoo

**Repository / product**

- Repository: [https://github.com/ryumada/docker-odoo](https://github.com/ryumada/docker-odoo)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| unknown: no dependency evidence located; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 0/100 (a score, not a probability)
- Raw weighted score: 0.00 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 1/7 dimensions

- Document volume: Unknown
- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `ReportLab`, run `run_2`, window `size:4001..8000`, rank 11
  - Query: `"reportlab" filename:requirements.txt size:4001..8000`
  - Sampled 30 of 5,392 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 5,392 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/ryumada/docker-odoo) (source: github_api): stars=3, fork=False, archived=False
- [readme_excerpt](https://github.com/ryumada/docker-odoo/blob/main/README.md) (source: readme): These directories will be used by Odoo for static data storage and logging.

### 217. ebongard/renfield

**Repository / product**

- Repository: [https://github.com/ebongard/renfield](https://github.com/ebongard/renfield)
- Company: Unknown — not stated in the repository
- Product: Renfield
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: no dependency evidence located; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 0/100 (a score, not a probability)
- Raw weighted score: 0.00 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 1/7 dimensions

- Document volume: Unknown
- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Docling`, run `run_2`, window `size:4001..8000`, rank 17
  - Query: `"docling" filename:requirements.txt size:4001..8000`
  - Retrieved 30 of 252 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/ebongard/renfield) (source: github_api): stars=34, fork=False, archived=False
- [readme_excerpt](https://github.com/ebongard/renfield/blob/main/README.md) (source: readme): **English** \| [Deutsch](README.de.md) <div align="center"> **Self-hosted AI assistant with voice satellites, 100+ tool integrations, and full offline capability.** </div> **Voice-first with physical s

### 218. receipt-print-hq/escpos-tools

**Repository / product**

- Repository: [https://github.com/receipt-print-hq/escpos-tools](https://github.com/receipt-print-hq/escpos-tools)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| unknown: no dependency evidence located; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 0/100 (a score, not a probability)
- Raw weighted score: 0.00 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 1/7 dimensions

- Document volume: Unknown
- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_1`, window `unsliced`, rank 24
  - Query: `"unoconv"`
  - Sampled 30 of 17,216 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 17,216 figure describes how many repositories matched, not how many were inspected.
- Tier 1, `LibreOffice headless / unoconv / JODConverter`, run `run_2`, window `unsliced`, rank 24
  - Query: `"unoconv"`
  - Sampled 30 of 17,216 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 17,216 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/receipt-print-hq/escpos-tools) (source: github_api): stars=239, fork=False, archived=False
- [api_response](https://github.com/receipt-print-hq/escpos-tools) (source: github_api): stars=239, fork=False, archived=False
- [api_response](https://github.com/receipt-print-hq/escpos-tools) (source: github_api): stars=239, fork=False, archived=False

### 219. TurtleTech-ehf/snapper

**Repository / product**

- Repository: [https://github.com/turtletech-ehf/snapper](https://github.com/turtletech-ehf/snapper)
- Company: Unknown — not stated in the repository
- Product: Table of Contents
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://snapper.turtletech.us

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| unknown: no dependency evidence located; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 0/100 (a score, not a probability)
- Raw weighted score: 0.00 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity *(unknown)* | 0 |
| Business criticality | 0 |
| Pipeline complexity *(unknown)* | 0 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal *(unknown)* | 0 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 1/7 dimensions

- Document volume: Unknown
- Document complexity: Unknown
- Pipeline complexity: Unknown
- Maintenance burden: Unknown
- Build-vs-buy signal: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 1, `Pandoc`, run `run_1`, window `unsliced`, rank 4
  - Query: `"subprocess pandoc"`
  - Retrieved 10 of 10 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 1, `Pandoc`, run `run_2`, window `unsliced`, rank 4
  - Query: `"subprocess pandoc"`
  - Retrieved 10 of 10 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/TurtleTech-ehf/snapper) (source: github_api): stars=6, fork=False, archived=False
- [api_response](https://github.com/TurtleTech-ehf/snapper) (source: github_api): stars=6, fork=False, archived=False
- [api_response](https://github.com/TurtleTech-ehf/snapper) (source: github_api): stars=6, fork=False, archived=False

## Query method

This section documents how candidates were found, so the result can be checked and rerun (the task brief's "query method" requirement).

**Discovery is tiered by measured precision, not library popularity.** Queries run in three tiers, read from `discovery_tier` in the library universe:

1. **Infrastructure** — a deployed conversion service (for example Gotenberg), found by a Dockerfile or compose-file reference rather than a manifest line. The highest-precision tier measured.
2. **Template generation** — libraries whose purpose is populating a template from data, so their presence implies a real pipeline.
3. **Broad manifest** — a library declared in a dependency manifest. The most common signal, and also the noisiest.

**Slicing.** GitHub returns at most 1,000 results for any single query, however it is paginated. Every tier-3 query is therefore run as a set of sliced queries, most often by date window (`search_window` in the record below), so a broad query's true coverage — and its gap — is visible rather than silently truncated. Tier 1 needs no slicing: the measured tier-1 query stayed under the ceiling on its own.

**`total_count`** is what the source reported as the total number of matches for a query, independent of how many were actually retrieved. **`capped`** means that total exceeded GitHub's 1,000-result pagination ceiling — it does **not** mean 1,000 results were retrieved, and in practice far fewer are. A capped query is always a partial sample; see the coverage note on each query below.

**Deduplication.** The same repository found by different queries, in the same run or a later one, resolves to one candidate via a deterministic id derived from its normalized URL. Every query that found it still gets its own evidence record, so overlap between queries stays visible instead of being collapsed away.

**Fresh-batch rotation (Run 2 and beyond).** A later run's date windows are shifted a full block further back than the run before it, so the two runs partition time rather than overlapping, and a run is refused outright if its planned queries were already executed by an earlier run. The exact rotation for each run is in the run information section below.

**Example queries actually executed, one per tier:**

- Tier 1: `"libreoffice" filename:Dockerfile`
  - Sampled 30 of 7,024 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 7,024 figure describes how many repositories matched, not how many were inspected.
- Tier 2: `"docxtpl" filename:requirements.txt`
  - Sampled 30 of 1,848 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,848 figure describes how many repositories matched, not how many were inspected.
- Tier 3: `"docx4j" filename:pom.xml size:2001..4000`
  - Retrieved 30 of 174 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**This is not an exhaustive map of every document-processing repository on GitHub.** It is a reproducible sample built from a documented, versioned query set. Coverage is partial wherever a query is marked capped, and the size of that gap is stated rather than hidden.

## Zero-result queries

27 of 237 recorded queries returned no results. An empty result can mean the library genuinely was not found this way, or it can mean the query itself is malformed — which is exactly what one earlier query in this project's history turned out to be, until it was corrected. Zero-result queries are therefore worth reviewing, not treated as uninteresting.

| Query | Library | Tier | Run |
|---|---|---:|---|
| `"Aspose.Words" filename:packages.config size:>16000` | Aspose.Words | 3 | run_2 |
| `"Aspose.Words" filename:requirements.txt size:2001..4000` | Aspose.Words | 3 | run_2 |
| `"Aspose.Words" filename:requirements.txt size:4001..8000` | Aspose.Words | 3 | run_2 |
| `"Aspose.Words" filename:requirements.txt size:8001..16000` | Aspose.Words | 3 | run_2 |
| `"Aspose.Words" filename:requirements.txt size:>16000` | Aspose.Words | 3 | run_2 |
| `"Aspose.Words" filename:pyproject.toml size:2001..4000` | Aspose.Words | 3 | run_2 |
| `"Aspose.Words" filename:pyproject.toml size:8001..16000` | Aspose.Words | 3 | run_2 |
| `"Aspose.Words" filename:pyproject.toml size:>16000` | Aspose.Words | 3 | run_2 |
| `"Aspose.Total" filename:packages.config size:>16000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:pom.xml size:2001..4000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:pom.xml size:>16000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:build.gradle size:2001..4000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:build.gradle size:4001..8000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:build.gradle size:8001..16000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:build.gradle size:>16000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:requirements.txt size:2001..4000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:requirements.txt size:4001..8000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:requirements.txt size:8001..16000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:requirements.txt size:>16000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:pyproject.toml size:2001..4000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:pyproject.toml size:4001..8000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:pyproject.toml size:8001..16000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:pyproject.toml size:>16000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:package.json size:2001..4000` | Aspose / Spire.Office suites | 3 | run_2 |
| `"Aspose.Total" filename:package.json size:8001..16000` | Aspose / Spire.Office suites | 3 | run_2 |

...and 2 more.

## Cumulative project state (all runs)

These totals cover **all 2 runs together**, not run_2. They are here for context and are not this run's results.

| Measure | All runs |
|---|---:|
| Discovery runs | 2 |
| Discovery queries executed | 474 |
| Unique repositories discovered | 8,013 |
| Repositories evidence-enriched and qualified | 782 |
| Repositories scored | 316 |

Unique repositories is a deduplicated count: a repository found by more than one run is one row, not two.

## Run information

### run_1

- Started: 2026-08-21T07:32:24.165484+00:00
- Finished: 2026-08-21T09:16:28.353080+00:00
- Rotation: run #1: size slices 0..250 through 1001..2000, library order rotated by 0
- Queries executed: 237 (failed: 0)
- Raw results: 5300
- Unique repositories surfaced: 4429
- Previously seen (found by an earlier run): 0
- New candidates: 4429

### run_2

- Started: 2026-08-23T19:59:31.881689+00:00
- Finished: 2026-08-23T20:23:23.038723+00:00
- Rotation: run #2: size slices 2001..4000 through >16000, library order rotated by 1
- Queries executed: 237 (failed: 0)
- Raw results: 5587
- Unique repositories surfaced: 4214
- Previously seen (found by an earlier run): 630
- New candidates: 3584

## Reproducibility

- Generated: 2026-08-23T21:56:24.632795+00:00
- Database schema version: 3
- Repository commit: 610c7860d474f6abcb24605f98346b851631d456
