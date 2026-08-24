# Dependency Map - run_1

## Executive summary

- Discovery runs recorded: **2**
- Discovery queries executed: **237**
  - Capped (exceeded GitHub's 1,000-result ceiling): **86**
  - Zero-result: **34**
  - Failed (no total recorded): **0**
- Raw discovery hits (API results, before dedup): **5300**
- Unique repositories discovered: **4429**
- Qualification: keep **44**, investigate **176**, reject **281**
- Scored candidates (keep or investigate with a score): **220**
- Candidates with enhanced maintenance-burden evidence: **0** (the phase 14 targeted commit-history pass has not run yet; `maintenance_burden` defaults to unknown for every candidate)

Raw hits and unique repositories are different numbers on purpose: several queries, or several file matches within one query, can all point at the same repository. The gap between them is deduplication working, not an error.

## Coverage and sampling (run_1)

Every number in this section describes **run_1 only**. Totals across all runs are in the cumulative section at the end.

- Repositories **surfaced by run_1**: **4,429**
  - Found for the first time by this run: **4,429**
  - Already seen by an earlier run: **0**
- Repositories **selected for evidence enrichment**: **501**
- Repositories with evidence collected but outside the official sample: **266**

**Every qualification, scoring and ranking number in this report describes the 501-repository evidence sample, not the 4,429 repositories surfaced by run_1.** The remaining 3,928 were surfaced by a discovery query and stored, but no evidence was collected for them and they were never qualified, scored or ranked. They are absent from the results because they were not examined, which is not the same as having been examined and found wanting.

### How the sample was selected

The sample is deterministic and stratified by discovery tier, so it can be reproduced exactly from stored discovery data. A candidate's tier is the strongest (lowest) tier of any query that surfaced it; within a tier, candidates are ordered by `candidate_id` ascending and taken from the front.

| Tier | Selected |
|---|---:|
| 1 | 100 |
| 2 | 100 |
| 3 | 301 |
| **Total** | **501** |

`candidate_id` is a hash of the normalised repository URL, so the ordering depends only on repository identity, never on the order results happened to arrive in.

Because the sample is stratified rather than proportional, the tier mix here is not the tier mix of the discovery universe. Tier 1 and tier 2 are deliberately over-represented relative to their share of discovered repositories, so keep and reject rates quoted per tier should not be read as rates across all of GitHub.

> **Maintenance-burden evidence was enriched for a bounded, highest-ranked candidate set; candidates outside that set may still have unknown `maintenance_burden`.** 63 of the 220 ranked candidates below rest on collected source evidence for that dimension; the remaining 157 score 0 on it because it was never inspected, which is not a finding that their document code is thin. `maintenance_burden` carries 15 percent of the weight, so an un-enriched candidate is ranked below where its evidence might otherwise place it. Comparing a candidate inside the enriched set against one outside it compares different amounts of collection.

## Ranked table

Sorted by score, highest first. Ties break on confidence (high, then medium, then low), then on candidate id, so the order is reproducible from the same data.

| Rank | Repository | Company | Qualification | Score | Confidence | Evidence coverage | Unknown dimensions |
|---:|---|---|---|---:|---|---|---|
| 1 | [kartoza/prj.app](https://github.com/kartoza/prj.app) | Kartoza.com | investigate | 60/100 | medium | 7/7 | none |
| 2 | [PapiHack/document-templating-service](https://github.com/papihack/document-templating-service) | — | investigate | 43/100 | medium | 6/7 | Commercial leverage |
| 3 | [inclusionAI/AWorld](https://github.com/inclusionai/aworld) | — | keep | 41/100 | high | 7/7 | none |
| 4 | [UKGovernmentBEIS/inspect_evals](https://github.com/ukgovernmentbeis/inspect_evals) | — | keep | 41/100 | high | 7/7 | none |
| 5 | [saipraveen-k/pharmarep_master](https://github.com/saipraveen-k/pharmarep_master) | — | keep | 40/100 | high | 6/7 | Commercial leverage |
| 6 | [lacework/extensible-reporting](https://github.com/lacework/extensible-reporting) | — | keep | 40/100 | high | 7/7 | none |
| 7 | [provena/provena](https://github.com/provena/provena) | — | keep | 40/100 | high | 7/7 | none |
| 8 | [AnujaK/restfiddle](https://github.com/anujak/restfiddle) | BootSimply Solutions  Licensed | keep | 40/100 | high | 7/7 | none |
| 9 | [shehanrathnayake/checkpoint-pos-system](https://github.com/shehanrathnayake/checkpoint-pos-system) | — | keep | 40/100 | high | 7/7 | none |
| 10 | [jolie-z/Auto-JobHunter](https://github.com/jolie-z/auto-jobhunter) | — | keep | 40/100 | high | 7/7 | none |
| 11 | [MuhdArshadd/4Tire](https://github.com/muhdarshadd/4tire) | — | keep | 40/100 | medium | 7/7 | none |
| 12 | [sourangshupal/multidata-rag-project](https://github.com/sourangshupal/multidata-rag-project) | — | investigate | 40/100 | medium | 7/7 | none |
| 13 | [runtsang/RebuttalStudio](https://github.com/runtsang/rebuttalstudio) | — | keep | 38/100 | high | 6/7 | Commercial leverage |
| 14 | [Ubada-Hussain/FormFixer](https://github.com/ubada-hussain/formfixer) | — | keep | 38/100 | high | 7/7 | none |
| 15 | [aurcode/ankineitor](https://github.com/aurcode/ankineitor) | — | keep | 37/100 | medium | 5/7 | Document volume, Commercial leverage |
| 16 | [MarvekG/BestAITrader](https://github.com/marvekg/bestaitrader) | — | investigate | 37/100 | medium | 6/7 | Commercial leverage |
| 17 | [Entity069/wtpdf-playground](https://github.com/entity069/wtpdf-playground) | — | investigate | 36/100 | medium | 6/7 | Commercial leverage |
| 18 | [proto-at-block/bitkey](https://github.com/proto-at-block/bitkey) | — | keep | 36/100 | medium | 7/7 | none |
| 19 | [Mufath/SerbaBisa](https://github.com/mufath/serbabisa) | — | investigate | 36/100 | medium | 6/7 | Commercial leverage |
| 20 | [luckylykkk/nnscholar-search](https://github.com/luckylykkk/nnscholar-search) | — | investigate | 36/100 | medium | 6/7 | Commercial leverage |
| 21 | [SudoXploit7/DefenSight-AI](https://github.com/sudoxploit7/defensight-ai) | — | investigate | 36/100 | medium | 6/7 | Commercial leverage |
| 22 | [nbazaes/django-bazpos](https://github.com/nbazaes/django-bazpos) | — | investigate | 36/100 | medium | 6/7 | Commercial leverage |
| 23 | [Cyberwatch/Pentest-Collaboration-Framework](https://github.com/cyberwatch/pentest-collaboration-framework) | — | investigate | 36/100 | medium | 6/7 | Commercial leverage |
| 24 | [varadlad/varadlad-portfolio](https://github.com/varadlad/varadlad-portfolio) | — | keep | 35/100 | medium | 7/7 | none |
| 25 | [peerdavid/remapy](https://github.com/peerdavid/remapy) | Freepik | keep | 35/100 | medium | 7/7 | none |
| 26 | [guangxiangdebizi/TradingAgents-MCPmode](https://github.com/guangxiangdebizi/tradingagents-mcpmode) | — | investigate | 35/100 | medium | 6/7 | Commercial leverage |
| 27 | [ghk/sideka-electron](https://github.com/ghk/sideka-electron) | — | keep | 35/100 | medium | 7/7 | none |
| 28 | [keystrokehq/keystroke](https://github.com/keystrokehq/keystroke) | — | keep | 34/100 | high | 7/7 | none |
| 29 | [activepieces/activepieces](https://github.com/activepieces/activepieces) | — | keep | 33/100 | high | 7/7 | none |
| 30 | [mleoca/ucn](https://github.com/mleoca/ucn) | — | keep | 33/100 | medium | 6/7 | Commercial leverage |
| 31 | [rhshah/iAnnotateSV](https://github.com/rhshah/iannotatesv) | — | investigate | 33/100 | medium | 7/7 | none |
| 32 | [LeDat98/NexusRAG](https://github.com/ledat98/nexusrag) | — | investigate | 33/100 | medium | 7/7 | none |
| 33 | [buzzqw/NotePadPQ](https://github.com/buzzqw/notepadpq) | — | keep | 33/100 | medium | 6/7 | Commercial leverage |
| 34 | [kartoza/docker-mezzanine](https://github.com/kartoza/docker-mezzanine) | — | investigate | 33/100 | medium | 6/7 | Commercial leverage |
| 35 | [metorial/metorial](https://github.com/metorial/metorial) | — | keep | 32/100 | high | 7/7 | none |
| 36 | [watat83/document-chat-system](https://github.com/watat83/document-chat-system) | — | investigate | 32/100 | medium | 7/7 | none |
| 37 | [ASUCICREPO/PDF_Accessibility](https://github.com/asucicrepo/pdf_accessibility) | Arizona State University | investigate | 32/100 | medium | 7/7 | none |
| 38 | [giovanniuchoa/DocumentinAPI](https://github.com/giovanniuchoa/documentinapi) | — | keep | 30/100 | high | 7/7 | none |
| 39 | [stella/stella](https://github.com/stella/stella) | — | keep | 30/100 | high | 7/7 | none |
| 40 | [mahasv/xdocreport](https://github.com/mahasv/xdocreport) | — | investigate | 30/100 | medium | 6/7 | Commercial leverage |
| 41 | [ceskaexpedice/kramerius](https://github.com/ceskaexpedice/kramerius) | — | investigate | 30/100 | medium | 6/7 | Commercial leverage |
| 42 | [MagaluCloud/s3-specs](https://github.com/magalucloud/s3-specs) | — | investigate | 30/100 | medium | 6/7 | Commercial leverage |
| 43 | [864381832/xJavaFxTool](https://github.com/864381832/xjavafxtool) | — | investigate | 30/100 | medium | 6/7 | Commercial leverage |
| 44 | [CyberCX-STA/PurpleOps](https://github.com/cybercx-sta/purpleops) | — | investigate | 30/100 | medium | 6/7 | Commercial leverage |
| 45 | [Aleks-Ya/yaal_examples](https://github.com/aleks-ya/yaal_examples) | — | investigate | 30/100 | medium | 6/7 | Commercial leverage |
| 46 | [FikrahFathoniSiregar/Auto-Report](https://github.com/fikrahfathonisiregar/auto-report) | — | investigate | 30/100 | medium | 6/7 | Commercial leverage |
| 47 | [SK-CERT/Taranis-NG](https://github.com/sk-cert/taranis-ng) | NCSC-NL | investigate | 29/100 | medium | 7/7 | none |
| 48 | [ngs-doo/TemplaterExamples](https://github.com/ngs-doo/templaterexamples) | — | keep | 29/100 | medium | 7/7 | none |
| 49 | [cool-dev-guy/rabbitthunder](https://github.com/cool-dev-guy/rabbitthunder) | — | keep | 28/100 | high | 6/7 | Commercial leverage |
| 50 | [PipedreamHQ/pipedream](https://github.com/pipedreamhq/pipedream) | — | keep | 28/100 | high | 6/7 | Maintenance burden |
| 51 | [simpledms/simpledms](https://github.com/simpledms/simpledms) | — | keep | 27/100 | high | 7/7 | none |
| 52 | [tringert/PdfSignabilityCheckerTool](https://github.com/tringert/pdfsignabilitycheckertool) | — | keep | 27/100 | medium | 6/7 | Commercial leverage |
| 53 | [nayetdet/softworker](https://github.com/nayetdet/softworker) | — | investigate | 27/100 | medium | 6/7 | Commercial leverage |
| 54 | [Oxylo/btreport](https://github.com/oxylo/btreport) | — | investigate | 27/100 | medium | 6/7 | Commercial leverage |
| 55 | [Azure/gpt-rag-ingestion](https://github.com/azure/gpt-rag-ingestion) | — | keep | 27/100 | medium | 6/7 | Commercial leverage |
| 56 | [iondv/registry](https://github.com/iondv/registry) | — | keep | 27/100 | medium | 6/7 | Commercial leverage |
| 57 | [bashly-framework/bashly](https://github.com/bashly-framework/bashly) | — | keep | 26/100 | high | 7/7 | none |
| 58 | [liferay/liferay-portal](https://github.com/liferay/liferay-portal) | Liferay | keep | 26/100 | medium | 7/7 | none |
| 59 | [kaiser6989/Team-6989-Rebuilt-Technical-Binder](https://github.com/kaiser6989/team-6989-rebuilt-technical-binder) | — | investigate | 25/100 | medium | 7/7 | none |
| 60 | [jreyesr/n8n-nodes-carbonejs](https://github.com/jreyesr/n8n-nodes-carbonejs) | — | keep | 24/100 | high | 7/7 | none |
| 61 | [sschuberth/stan](https://github.com/sschuberth/stan) | — | keep | 24/100 | medium | 6/7 | Commercial leverage |
| 62 | [GRAVITAD-SL/pizquito-backend-strapi](https://github.com/gravitad-sl/pizquito-backend-strapi) | — | keep | 24/100 | medium | 6/7 | Commercial leverage |
| 63 | [I-CAN-hack/pdf-mcp](https://github.com/i-can-hack/pdf-mcp) | — | keep | 24/100 | medium | 6/7 | Commercial leverage |
| 64 | [radic82/docx4jUtil](https://github.com/radic82/docx4jutil) | — | keep | 24/100 | medium | 6/7 | Commercial leverage |
| 65 | [freelawproject/recap-chrome](https://github.com/freelawproject/recap-chrome) | — | investigate | 23/100 | medium | 6/7 | Maintenance burden |
| 66 | [cuba-platform/yarg](https://github.com/cuba-platform/yarg) | Haulmont | investigate | 23/100 | medium | 6/7 | Maintenance burden |
| 67 | [Kavithma-Thushal/Computershop-Management-System-1st-Sem-Final](https://github.com/kavithma-thushal/computershop-management-system-1st-sem-final) | — | investigate | 23/100 | medium | 6/7 | Maintenance burden |
| 68 | [QuivrHQ/MegaParse](https://github.com/quivrhq/megaparse) | — | investigate | 22/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 69 | [City-of-Helsinki/kaavapino](https://github.com/city-of-helsinki/kaavapino) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 70 | [JaocHatter/ReportGenerator-Landmarks](https://github.com/jaochatter/reportgenerator-landmarks) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 71 | [dfir-iris/docx-generator](https://github.com/dfir-iris/docx-generator) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 72 | [TheOnlyWayUp/WattpadDownloader](https://github.com/theonlywayup/wattpaddownloader) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 73 | [zhangzhen1979/JIMU-ConvertPreview](https://github.com/zhangzhen1979/jimu-convertpreview) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 74 | [mila-iqia/COVI-AgentSim](https://github.com/mila-iqia/covi-agentsim) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 75 | [g3w-suite/g3w-admin](https://github.com/g3w-suite/g3w-admin) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 76 | [javadev/jasper-xml-to-pdf-generator](https://github.com/javadev/jasper-xml-to-pdf-generator) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 77 | [xcmt/ABC_report](https://github.com/xcmt/abc_report) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 78 | [qwc-services/jasper-reporting-service](https://github.com/qwc-services/jasper-reporting-service) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 79 | [wso2/carbon-commons](https://github.com/wso2/carbon-commons) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 80 | [Azure-Samples/healthcare-agent-orchestrator](https://github.com/azure-samples/healthcare-agent-orchestrator) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 81 | [AIGeniusInstitue/restfeel](https://github.com/aigeniusinstitue/restfeel) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 82 | [zorazrw/odex](https://github.com/zorazrw/odex) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 83 | [lincolnluiz/SpringBoot-JasperReports](https://github.com/lincolnluiz/springboot-jasperreports) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 84 | [gooderp-study/GoodERP](https://github.com/gooderp-study/gooderp) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 85 | [davidkey/DynamicJasperExample](https://github.com/davidkey/dynamicjasperexample) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 86 | [zkoss/zk](https://github.com/zkoss/zk) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 87 | [Lawyer-ray/FachuanHybridSystem](https://github.com/lawyer-ray/fachuanhybridsystem) | — | investigate | 21/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 88 | [DFE-Digital/funding-service-myesf-docex-ui](https://github.com/dfe-digital/funding-service-myesf-docex-ui) | — | investigate | 20/100 | medium | 6/7 | Maintenance burden |
| 89 | [kedowen/KedoExecutorNet](https://github.com/kedowen/kedoexecutornet) | — | investigate | 20/100 | medium | 6/7 | Maintenance burden |
| 90 | [sublee/subl.ee](https://github.com/sublee/subl.ee) | — | investigate | 20/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 91 | [AWS-Student-Builder-Group-IIT-SL/CertSys](https://github.com/aws-student-builder-group-iit-sl/certsys) | — | investigate | 20/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 92 | [GaiZhenbiao/ChuanhuChatGPT](https://github.com/gaizhenbiao/chuanhuchatgpt) | — | investigate | 20/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 93 | [spk3077/pdf-library-assessment](https://github.com/spk3077/pdf-library-assessment) | — | investigate | 20/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 94 | [bigbeartechworld/big-bear-casaos](https://github.com/bigbeartechworld/big-bear-casaos) | BigBearTechWorld | investigate | 20/100 | medium | 6/7 | Maintenance burden |
| 95 | [rsrdesarrollo/sarna](https://github.com/rsrdesarrollo/sarna) | — | investigate | 20/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 96 | [lr101/homelab](https://github.com/lr101/homelab) | — | investigate | 20/100 | medium | 6/7 | Maintenance burden |
| 97 | [qgis/QGIS-Certification-Website](https://github.com/qgis/qgis-certification-website) | Kartoza.com | investigate | 19/100 | medium | 6/7 | Maintenance burden |
| 98 | [kw677/Fileo](https://github.com/kw677/fileo) | — | investigate | 19/100 | medium | 6/7 | Maintenance burden |
| 99 | [iiitdwd-exams/certificates](https://github.com/iiitdwd-exams/certificates) | — | investigate | 19/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 100 | [Mihir-Rabari/inboxfm-connect](https://github.com/mihir-rabari/inboxfm-connect) | — | keep | 19/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 101 | [datawizz/Openpieces](https://github.com/datawizz/openpieces) | — | keep | 19/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 102 | [DenizAltunkapan/ilias-mcp](https://github.com/denizaltunkapan/ilias-mcp) | — | investigate | 18/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 103 | [Websoft9/docker-library](https://github.com/websoft9/docker-library) | — | investigate | 18/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 104 | [runtipi/runtipi-appstore](https://github.com/runtipi/runtipi-appstore) | — | investigate | 18/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 105 | [dendianugerah/reubah](https://github.com/dendianugerah/reubah) | — | investigate | 18/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 106 | [bigcapitalhq/bigcapital](https://github.com/bigcapitalhq/bigcapital) | — | keep | 17/100 | high | 6/7 | Maintenance burden |
| 107 | [infonl/dimpact-zaakafhandelcomponent](https://github.com/infonl/dimpact-zaakafhandelcomponent) | Atos | keep | 17/100 | high | 6/7 | Maintenance burden |
| 108 | [scienceai/open-docx](https://github.com/scienceai/open-docx) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 109 | [airens/interactive_brokers_tax](https://github.com/airens/interactive_brokers_tax) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 110 | [virgiliojr94/localpdf.io](https://github.com/virgiliojr94/localpdf.io) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 111 | [capitoledulibre/cdl_paper_generator](https://github.com/capitoledulibre/cdl_paper_generator) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 112 | [yogeshhk/Sarvadnya](https://github.com/yogeshhk/sarvadnya) | — | investigate | 17/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 113 | [bbossgroups/bboss](https://github.com/bbossgroups/bboss) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 114 | [runZeroInc/runzero-api](https://github.com/runzeroinc/runzero-api) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 115 | [ethicalhackingplayground/shodan-grabber](https://github.com/ethicalhackingplayground/shodan-grabber) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 116 | [rava-dosa/epub2pdf](https://github.com/rava-dosa/epub2pdf) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 117 | [miyabayt/spring-boot-doma2-sample](https://github.com/miyabayt/spring-boot-doma2-sample) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 118 | [UniversitaDellaCalabria/uniTicket](https://github.com/universitadellacalabria/uniticket) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 119 | [cdump/investments](https://github.com/cdump/investments) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 120 | [simbianai/taskgen](https://github.com/simbianai/taskgen) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 121 | [JasonObeid/Chart2Text](https://github.com/jasonobeid/chart2text) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 122 | [zhihuiyuze/PDF-Prompt-Injection-Toolkit](https://github.com/zhihuiyuze/pdf-prompt-injection-toolkit) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 123 | [inbn/screenshot-urls](https://github.com/inbn/screenshot-urls) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 124 | [MK2112/any_to_any.py](https://github.com/mk2112/any_to_any.py) | — | investigate | 17/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 125 | [lmorgadodacosta/iTELL](https://github.com/lmorgadodacosta/itell) | — | investigate | 17/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 126 | [codion-is/codion](https://github.com/codion-is/codion) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 127 | [wocommunity/wonder](https://github.com/wocommunity/wonder) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 128 | [BearMelon/thomaslo](https://github.com/bearmelon/thomaslo) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 129 | [basxsoftwareassociation/bread](https://github.com/basxsoftwareassociation/bread) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 130 | [elapouya/python-docx-template](https://github.com/elapouya/python-docx-template) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 131 | [SuffolkLITLab/docassemble-ALWeaver](https://github.com/suffolklitlab/docassemble-alweaver) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 132 | [OParl/spec](https://github.com/oparl/spec) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 133 | [GUMGA/frameworkbackend](https://github.com/gumga/frameworkbackend) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 134 | [Swiss-Armed-Forces/Loom](https://github.com/swiss-armed-forces/loom) | — | keep | 17/100 | medium | 6/7 | Maintenance burden |
| 135 | [GUMGA/framework-backend](https://github.com/gumga/framework-backend) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 136 | [adfinis/document-merge-service](https://github.com/adfinis/document-merge-service) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 137 | [dkratzert/FinalCif](https://github.com/dkratzert/finalcif) | — | investigate | 17/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 138 | [rte-france/wattelse](https://github.com/rte-france/wattelse) | — | investigate | 16/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 139 | [AndersonBY/vector-vein](https://github.com/andersonby/vector-vein) | — | investigate | 16/100 | medium | 5/7 | Document volume, Maintenance burden |
| 140 | [vitorcastro78/KYC](https://github.com/vitorcastro78/kyc) | — | investigate | 15/100 | medium | 6/7 | Maintenance burden |
| 141 | [huridocs/pdf-document-layout-analysis](https://github.com/huridocs/pdf-document-layout-analysis) | Alibaba Research Group | investigate | 15/100 | medium | 6/7 | Maintenance burden |
| 142 | [imarthe75/ades-nevadi](https://github.com/imarthe75/ades-nevadi) | — | investigate | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 143 | [conscia/node-tika](https://github.com/conscia/node-tika) | — | investigate | 15/100 | medium | 6/7 | Maintenance burden |
| 144 | [azavea/raster-vision](https://github.com/azavea/raster-vision) | — | investigate | 15/100 | medium | 6/7 | Maintenance burden |
| 145 | [dalibo/pandocker](https://github.com/dalibo/pandocker) | — | investigate | 15/100 | medium | 6/7 | Maintenance burden |
| 146 | [carbon-design-system/carbon](https://github.com/carbon-design-system/carbon) | — | investigate | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 147 | [globalis-ms/carbone](https://github.com/globalis-ms/carbone) | — | investigate | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 148 | [gyselroth/balloon](https://github.com/gyselroth/balloon) | — | keep | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 149 | [dante-ev/docker-texlive](https://github.com/dante-ev/docker-texlive) | — | investigate | 15/100 | medium | 6/7 | Maintenance burden |
| 150 | [ad-on-is/rachoon](https://github.com/ad-on-is/rachoon) | — | keep | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 151 | [riclolsen/json-scada](https://github.com/riclolsen/json-scada) | — | investigate | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 152 | [DefinitelyTyped/DefinitelyTyped](https://github.com/definitelytyped/definitelytyped) | — | investigate | 15/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 153 | [HarnessFix/HarnessFix](https://github.com/harnessfix/harnessfix) | — | investigate | 14/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 154 | [MarkEdmondson1234/langchain-github](https://github.com/markedmondson1234/langchain-github) | — | investigate | 14/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 155 | [The-Liberal-Labs/Data-Crawler](https://github.com/the-liberal-labs/data-crawler) | — | investigate | 14/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 156 | [jimmymnt/pim-e-shop](https://github.com/jimmymnt/pim-e-shop) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 157 | [Simon-Drohsen/pimcore-certificate](https://github.com/simon-drohsen/pimcore-certificate) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 158 | [JanBancerewicz/pimcoretask](https://github.com/janbancerewicz/pimcoretask) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 159 | [datnv41001/pimcore](https://github.com/datnv41001/pimcore) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 160 | [LevDmitriev/dc-pimcore-demo](https://github.com/levdmitriev/dc-pimcore-demo) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 161 | [vivliostyle/vivliostyle-cli](https://github.com/vivliostyle/vivliostyle-cli) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 162 | [l4houx/recipe](https://github.com/l4houx/recipe) | — | investigate | 14/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 163 | [flopach/create-your-own-api-assistant-cisco-catalyst-center](https://github.com/flopach/create-your-own-api-assistant-cisco-catalyst-center) | Cisco | investigate | 14/100 | low | 5/7 | Pipeline complexity, Maintenance burden |
| 164 | [marlian/claude-qdrant-mcp](https://github.com/marlian/claude-qdrant-mcp) | — | investigate | 14/100 | low | 5/7 | Pipeline complexity, Maintenance burden |
| 165 | [abgulati/Privion](https://github.com/abgulati/privion) | — | investigate | 13/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 166 | [networktocode/yangify](https://github.com/networktocode/yangify) | — | investigate | 13/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 167 | [gitrgoliveira/bracket-creator](https://github.com/gitrgoliveira/bracket-creator) | — | investigate | 13/100 | medium | 6/7 | Maintenance burden |
| 168 | [getumbrel/umbrel-apps](https://github.com/getumbrel/umbrel-apps) | — | investigate | 13/100 | medium | 6/7 | Maintenance burden |
| 169 | [Paparusi/legal-ai-agent](https://github.com/paparusi/legal-ai-agent) | — | investigate | 13/100 | medium | 6/7 | Maintenance burden |
| 170 | [netease-youdao/QAnything](https://github.com/netease-youdao/qanything) | — | investigate | 12/100 | medium | 5/7 | Document volume, Maintenance burden |
| 171 | [Hellvisback365/datapizza-ai-main](https://github.com/hellvisback365/datapizza-ai-main) | — | investigate | 12/100 | medium | 5/7 | Document volume, Maintenance burden |
| 172 | [VIDA-NYU/ache](https://github.com/vida-nyu/ache) | — | investigate | 12/100 | medium | 5/7 | Document volume, Maintenance burden |
| 173 | [sitepoint-editors/awesome-symfony](https://github.com/sitepoint-editors/awesome-symfony) | — | investigate | 12/100 | low | 3/7 | Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal |
| 174 | [dragonfore4/deka-download](https://github.com/dragonfore4/deka-download) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 175 | [modrinth/code](https://github.com/modrinth/code) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 176 | [Probesys/lotemplate](https://github.com/probesys/lotemplate) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 177 | [MVladislav/vm-docker-collection](https://github.com/mvladislav/vm-docker-collection) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 178 | [ministryofjustice/send-legal-mail-to-prisons](https://github.com/ministryofjustice/send-legal-mail-to-prisons) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 179 | [notadev-iamaura/OneRAG](https://github.com/notadev-iamaura/onerag) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 180 | [solidtime-io/solidtime](https://github.com/solidtime-io/solidtime) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 181 | [unitedworldwrestling/arena-public](https://github.com/unitedworldwrestling/arena-public) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 182 | [YYC-Cube/YYC3-Knowledge-Base](https://github.com/yyc-cube/yyc3-knowledge-base) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 183 | [georgemarian98/home-server](https://github.com/georgemarian98/home-server) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 184 | [tjmlabs/ColiVara](https://github.com/tjmlabs/colivara) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 185 | [samvera/hydra-derivatives](https://github.com/samvera/hydra-derivatives) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 186 | [AppCivico/smae](https://github.com/appcivico/smae) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 187 | [mperreir/Hyblab2023](https://github.com/mperreir/hyblab2023) | — | investigate | 11/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 188 | [open-edge-platform/edge-ai-suites](https://github.com/open-edge-platform/edge-ai-suites) | — | investigate | 10/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 189 | [NVIDIA/workbench-example-agentic-rag](https://github.com/nvidia/workbench-example-agentic-rag) | — | investigate | 10/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 190 | [AidenFaulconer/AI.DEN](https://github.com/aidenfaulconer/ai.den) | — | investigate | 10/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 191 | [paulgessinger/swift-paperless](https://github.com/paulgessinger/swift-paperless) | — | investigate | 9/100 | medium | 6/7 | Maintenance burden |
| 192 | [selkies-project/docker-selkies-glx-desktop](https://github.com/selkies-project/docker-selkies-glx-desktop) | — | investigate | 9/100 | medium | 6/7 | Maintenance burden |
| 193 | [JoachimSchaeffer/AttackSelection](https://github.com/joachimschaeffer/attackselection) | — | investigate | 8/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 194 | [makinacorpus/convertit](https://github.com/makinacorpus/convertit) | — | investigate | 7/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 195 | [octos-org/octos](https://github.com/octos-org/octos) | — | investigate | 7/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 196 | [CitizenLabDotCo/citizenlab](https://github.com/citizenlabdotco/citizenlab) | — | investigate | 7/100 | medium | 5/7 | Maintenance burden, Commercial leverage |
| 197 | [CivilHub/CivilHub](https://github.com/civilhub/civilhub) | — | investigate | 7/100 | low | 4/7 | Document volume, Pipeline complexity, Maintenance burden |
| 198 | [ppc64le/pyeco](https://github.com/ppc64le/pyeco) | — | investigate | 6/100 | medium | 4/7 | Document volume, Maintenance burden, Commercial leverage |
| 199 | [Scouterna/skojjt](https://github.com/scouterna/skojjt) | — | investigate | 5/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 200 | [philips-software/amp-devcontainer](https://github.com/philips-software/amp-devcontainer) | — | investigate | 5/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 201 | [JetBrains/compose-multiplatform](https://github.com/jetbrains/compose-multiplatform) | JetBrains | investigate | 4/100 | low | 4/7 | Document volume, Pipeline complexity, Maintenance burden |
| 202 | [buildbyadnan/zero-day-codebase](https://github.com/buildbyadnan/zero-day-codebase) | — | investigate | 4/100 | low | 4/7 | Document volume, Pipeline complexity, Maintenance burden |
| 203 | [FlagAI-Open/Aquila2](https://github.com/flagai-open/aquila2) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 204 | [Sshyamsundar6887/Clausewise](https://github.com/sshyamsundar6887/clausewise) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 205 | [simbo1905/agt](https://github.com/simbo1905/agt) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 206 | [aws-samples/bedrock-qnachatbot](https://github.com/aws-samples/bedrock-qnachatbot) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 207 | [doczrz/literaturereport](https://github.com/doczrz/literaturereport) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 208 | [kvcache-ai/TrEnv-X](https://github.com/kvcache-ai/trenv-x) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 209 | [misbahsy/RAGTune](https://github.com/misbahsy/ragtune) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 210 | [dundalek/closh](https://github.com/dundalek/closh) | — | investigate | 2/100 | low | 2/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal |
| 211 | [iltoga/BusinessSuite](https://github.com/iltoga/businesssuite) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 212 | [remacs/remacs](https://github.com/remacs/remacs) | Free Software Foundation | investigate | 2/100 | low | 2/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal |
| 213 | [rapid7/nexpose-warehouse-jasper-templates](https://github.com/rapid7/nexpose-warehouse-jasper-templates) | — | investigate | 2/100 | low | 3/7 | Document volume, Pipeline complexity, Maintenance burden, Commercial leverage |
| 214 | [karthikeya3342/careerOS](https://github.com/karthikeya3342/careeros) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 215 | [archanags001/AI-Report-Generator](https://github.com/archanags001/ai-report-generator) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 216 | [datastax/ragstack-ai](https://github.com/datastax/ragstack-ai) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 217 | [Representable/representable](https://github.com/representable/representable) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 218 | [CesarPetrescu/deeper-research](https://github.com/cesarpetrescu/deeper-research) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 219 | [receipt-print-hq/escpos-tools](https://github.com/receipt-print-hq/escpos-tools) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |
| 220 | [TurtleTech-ehf/snapper](https://github.com/turtletech-ehf/snapper) | — | investigate | 0/100 | low | 1/7 | Document volume, Document complexity, Pipeline complexity, Maintenance burden, Build-vs-buy signal, Commercial leverage |

## Candidate details

### 1. kartoza/prj.app

**Repository / product**

- Repository: [https://github.com/kartoza/prj.app](https://github.com/kartoza/prj.app)
- Company: Kartoza.com
- Product: Projecta
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=3, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: category_count=2; multiple_document_types_handled=true; pipeline_stage_count=3; confirmed generation/conversion code \| unknown: contributor_count not collected

**Score**

- Score: 60/100 (a score, not a probability)
- Raw weighted score: 3.00 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 3 |
| Business criticality | 1 |
| Pipeline complexity | 3 |
| Maintenance burden | 5 |
| Build-vs-buy signal | 4 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `ReportLab`, run `run_1`, window `size:1001..2000`, rank 8
  - Query: `"reportlab" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 9,392 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 9,392 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `WeasyPrint`, run `run_1`, window `size:1001..2000`, rank 2
  - Query: `"weasyprint" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 2,532 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,532 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [deployment/docker/REQUIREMENTS.txt](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/deployment/docker/REQUIREMENTS.txt)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/django_project/base/views/certificate_preview.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/django_project/certification/views/certificate_organisation.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/django_project/certification/views/certificate.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/django_project/certification/tests/views/test_certificate_views.py)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [deployment/docker/REQUIREMENTS.txt](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/deployment/docker/REQUIREMENTS.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/django_project/lesson/views/worksheet.py)

**Evidence trail**

- [api_response](https://github.com/kartoza/prj.app) (source: github_api): stars=29, fork=False, archived=False
- [readme_excerpt](https://github.com/kartoza/prj.app/blob/develop/README.md) (source: readme): company stated as 'Kartoza.com'
- [manifest_line](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/deployment/docker/REQUIREMENTS.txt) (source: github_api): # support special characters Unidecode==0.4.20 Pillow==9.1.0 reportlab==3.6.9 xhtml2pdf==0.2.7 django-modeltranslation==0.16.1 django-colorfield==0.3.2
- [code_permalink](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/django_project/base/views/certificate_preview.py) (source: github_api): from django.http import HttpResponse from django.utils.text import slugify from reportlab.lib.pagesizes import A4, landscape from reportlab.pdfgen import canvas from core.settings.contrib import STOP_
- [code_permalink](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/django_project/certification/views/certificate_organisation.py) (source: github_api): from django.urls import reverse from django.http import Http404, FileResponse from django.views.generic import CreateView, DetailView from reportlab.lib.utils import ImageReader from reportlab.lib.pag
- [code_permalink](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/django_project/certification/views/certificate.py) (source: github_api): from djstripe.enums import PaymentIntentStatus from djstripe.models import Customer, PaymentIntent from djstripe import settings as djstripe_settings from reportlab.pdfgen import canvas from reportlab
- [code_permalink](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/django_project/certification/tests/views/test_certificate_views.py) (source: github_api): @patch('os.path.exists')     @patch('os.makedirs')     @patch('builtins.open', create=True)     @patch('reportlab.lib.utils.ImageReader')     def test_generate_certificate_with_signature(
- [manifest_line](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/deployment/docker/REQUIREMENTS.txt) (source: github_api): xhtml2pdf==0.2.7 django-modeltranslation==0.16.1 django-colorfield==0.3.2 WeasyPrint==0.42.3 djangorestframework==3.11.2 django-simple-history==3.0.0 dj-stripe==2.1.1
- [code_permalink](https://github.com/kartoza/prj.app/blob/d964ffe78fbf2b703ccc3d06fc27319beee01f96/django_project/lesson/views/worksheet.py) (source: github_api): from django.utils.translation import ugettext_lazy as _ from braces.views import LoginRequiredMixin from weasyprint import HTML from lesson.forms.worksheet import WorksheetForm, WorksheetUpdateForm
- [readme_excerpt](https://github.com/kartoza/prj.app/blob/develop/README.md) (source: readme): **Backups** If you wish to sync backups, you need to establish a read / write btsync key on your production server and run one or more btsync clients with a read only key.

### 2. PapiHack/document-templating-service

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

### 3. inclusionAI/AWorld

**Repository / product**

- Repository: [https://github.com/inclusionai/aworld](https://github.com/inclusionai/aworld)
- Company: Unknown — not stated in the repository
- Product: AWorld: The Agent Harness for Your World
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.aworldagents.com

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

- Tier 3, `python-docx`, run `run_1`, window `size:251..500`, rank 6
  - Query: `"python-docx" filename:pyproject.toml size:251..500`
  - Sampled 30 of 1,454 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,454 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `WeasyPrint`, run `run_1`, window `size:1001..2000`, rank 13
  - Query: `"weasyprint" filename:pyproject.toml size:1001..2000`
  - Sampled 30 of 1,190 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,190 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [aworld-tools/filex/pyproject.toml](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/aworld-tools/filex/pyproject.toml)
- `python-docx` (docx, generation) — code_import — [code](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/examples/gaia/mcp_collections/documents/msdocx.py)
- `python-docx` (docx, generation) — manifest_declaration — [aworld-tools/filex/pyproject.toml](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/aworld-tools/filex/pyproject.toml)
- `python-docx` (docx, generation) — code_import — [code](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/aworld-tools/filex/src/document_parse_service/word_document_service.py)
- `python-docx` (docx, generation) — manifest_declaration — [aworld/sandbox/tool_servers/filesystem/pyproject.toml](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/aworld/sandbox/tool_servers/filesystem/pyproject.toml)
- `python-docx` (docx, generation) — manifest_declaration — [aworld/sandbox/tool_servers/filesystem/requirements.txt](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/aworld/sandbox/tool_servers/filesystem/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/inclusionAI/AWorld) (source: github_api): stars=1223, fork=False, archived=False
- [manifest_line](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/aworld-tools/filex/pyproject.toml) (source: github_api): "socksio>=1.0.0",     "reportlab~=4.4.3",     "markdown~=3.7",     "weasyprint~=65.0",     "faster-whisper~=1.2.1", ]
- [code_permalink](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/examples/gaia/mcp_collections/documents/msdocx.py) (source: github_api): class DOCXExtractionCollection(ActionCollection):     """MCP service for DOCX/DOC document content extraction using python-docx.
- [manifest_line](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/aworld-tools/filex/pyproject.toml) (source: github_api): "pandas~=2.2.3",     "duckdb>=1.1.0",     "xlrd~=2.0.1",     "python-docx~=1.2.0",     "python-pptx~=1.0.2",     "pillow~=12.1.0",     "pdf2image~=1.17.0",
- [code_permalink](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/aworld-tools/filex/src/document_parse_service/word_document_service.py) (source: github_api): stage_logger: DocumentParseLogger,     ) -> MarkdownArtifact:         if Document is None:             raise RuntimeError("未安装python-docx。请安装: pip install python-docx")         output_dir = D
- [manifest_line](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/aworld/sandbox/tool_servers/filesystem/pyproject.toml) (source: github_api): "openpyxl~=3.1.5",     "pandas~=2.2.3",     "tabulate>=0.9.0",     "python-docx~=1.2.0",     "python-pptx~=1.0.2",     "pillow~=12.1.0",     "pdf2image~=1.17.0",
- [manifest_line](https://github.com/inclusionAI/AWorld/blob/3f2ff921005f65aab2d03ecb39e33cba39e73d0c/aworld/sandbox/tool_servers/filesystem/requirements.txt) (source: github_api): openpyxl~=3.1.5 pandas~=2.2.3 tabulate>=0.9.0 python-docx~=1.2.0 python-pptx~=1.0.2 pillow~=12.1.0 pdf2image~=1.17.0
- [readme_excerpt](https://github.com/inclusionAI/AWorld/blob/main/README.md) (source: readme): AWorld is the platform designed for this singular purpose.

### 4. UKGovernmentBEIS/inspect_evals

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

### 5. saipraveen-k/pharmarep_master

**Repository / product**

- Repository: [https://github.com/saipraveen-k/pharmarep_master](https://github.com/saipraveen-k/pharmarep_master)
- Company: Unknown — not stated in the repository
- Product: PharmaRep Master 💊 — Agentic AI for Rapid Drug Repurposing
- Industry: healthcare_diagnostics (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.00 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `ReportLab`, run `run_1`, window `size:0..250`, rank 25
  - Query: `"reportlab" filename:requirements.txt size:0..250`
  - Sampled 30 of 30,016 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 30,016 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [Requirements.txt](https://github.com/saipraveen-k/pharmarep_master/blob/main/Requirements.txt)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/saipraveen-k/pharmarep_master/blob/6fe4841f67f3265458118fca9250678d1a05b227/venv/Lib/site-packages/reportlab/__init__.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/saipraveen-k/pharmarep_master/blob/6fe4841f67f3265458118fca9250678d1a05b227/venv/Lib/site-packages/reportlab/rl_config.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/saipraveen-k/pharmarep_master/blob/6fe4841f67f3265458118fca9250678d1a05b227/venv/Lib/site-packages/reportlab/rl_settings.py)

**Evidence trail**

- [api_response](https://github.com/saipraveen-k/pharmarep_master) (source: github_api): stars=3, fork=False, archived=False
- [manifest_line](https://github.com/saipraveen-k/pharmarep_master/blob/main/Requirements.txt) (source: github_api): reportlab
- [code_permalink](https://github.com/saipraveen-k/pharmarep_master/blob/6fe4841f67f3265458118fca9250678d1a05b227/venv/Lib/site-packages/reportlab/__init__.py) (source: github_api): #Copyright ReportLab Europe Ltd. 2000-2023 #see license.txt for license details __doc__="""The Reportlab PDF generation library.""" Version = "4.4.5" __version__=Version __date__='20251117'
- [code_permalink](https://github.com/saipraveen-k/pharmarep_master/blob/6fe4841f67f3265458118fca9250678d1a05b227/venv/Lib/site-packages/reportlab/rl_config.py) (source: github_api): def _defaults_init():     '''     create & return defaults for all reportlab settings from     reportlab.rl_settings.py     reportlab.local_rl_settings.py     reportlab_settings.py or ~/.reportlab_se
- [code_permalink](https://github.com/saipraveen-k/pharmarep_master/blob/6fe4841f67f3265458118fca9250678d1a05b227/venv/Lib/site-packages/reportlab/rl_settings.py) (source: github_api): #Copyright ReportLab Europe Ltd. 2000-2017 #see license.txt for license details '''default settings for reportlab to override these drop a module rl_local_settings.py parallel to this file or anywher
- [other](https://github.com/saipraveen-k/pharmarep_master/tree/main/reports) (source: github_api): directory reports/ present
- [readme_excerpt](https://github.com/saipraveen-k/pharmarep_master/blob/main/README.md) (source: readme): Areas: [ ] New data source integrations [ ] Scoring formula improvements [ ] UI/UX enhancements [ ] Performance optimization [ ] Testing & validation MIT License - See LICENSE file Built for **EY Tech

### 6. lacework/extensible-reporting

**Repository / product**

- Repository: [https://github.com/lacework/extensible-reporting](https://github.com/lacework/extensible-reporting)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:0..250`, rank 9
  - Query: `"weasyprint" filename:requirements.txt size:0..250`
  - Sampled 30 of 3,832 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,832 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `WeasyPrint`, run `run_1`, window `size:501..1000`, rank 26
  - Query: `"weasyprint" filename:pyproject.toml size:501..1000`
  - Retrieved 30 of 976 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [lambda_requirements.txt](https://github.com/lacework/extensible-reporting/blob/main/lambda_requirements.txt)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/lacework/extensible-reporting/blob/main/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements.txt](https://github.com/lacework/extensible-reporting/blob/main/requirements.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/lacework/extensible-reporting/blob/158f8af21414fcdbd416dcf11dfd411e6af5f7a1/lw_report_gen.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/lacework/extensible-reporting/blob/158f8af21414fcdbd416dcf11dfd411e6af5f7a1/lambda_function.py)

**Evidence trail**

- [api_response](https://github.com/lacework/extensible-reporting) (source: github_api): stars=17, fork=False, archived=False
- [readme_excerpt](https://github.com/lacework/extensible-reporting/blob/main/README.md) (source: readme): company stated as 'Copyright'
- [manifest_line](https://github.com/lacework/extensible-reporting/blob/main/lambda_requirements.txt) (source: github_api): weasyprint
- [manifest_line](https://github.com/lacework/extensible-reporting/blob/main/pyproject.toml) (source: github_api): "weasyprint (>=62.1)",
- [manifest_line](https://github.com/lacework/extensible-reporting/blob/main/requirements.txt) (source: github_api): weasyprint==62.3 ; python_version >= "3.10" and python_version < "3.13"
- [code_permalink](https://github.com/lacework/extensible-reporting/blob/158f8af21414fcdbd416dcf11dfd411e6af5f7a1/lw_report_gen.py) (source: github_api): report_file_name += ".pdf"             logger.info(f'Writing report to {report_file_name}')             try:                 from weasyprint import HTML, CSS                 from weasyprin
- [code_permalink](https://github.com/lacework/extensible-reporting/blob/158f8af21414fcdbd416dcf11dfd411e6af5f7a1/lambda_function.py) (source: github_api): import boto3 import boto3.session from weasyprint import HTML, CSS from weasyprint.text.fonts import FontConfiguration #import pdfkit import json from botocore.exceptions import ClientError
- [other](https://github.com/lacework/extensible-reporting/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/lacework/extensible-reporting/blob/main/README.md) (source: readme): If you wish to configure the Lacework FortiCNAPP Client instance using environment variables, this tool honors the same variables used by the Lacework FortiCNAPP CLI.

### 7. provena/provena

**Repository / product**

- Repository: [https://github.com/provena/provena](https://github.com/provena/provena)
- Company: Unknown — not stated in the repository
- Product: Provena
- Industry: proposal_sales (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://provena.io

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

- Tier 3, `python-docx`, run `run_1`, window `size:501..1000`, rank 13
  - Query: `"python-docx" filename:requirements.txt size:501..1000`
  - Sampled 30 of 11,984 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 11,984 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `python-docx` (docx, generation) — manifest_declaration — [prov-api/docker-requirements.txt](https://github.com/provena/provena/blob/a4142d4f1a05431c5c6ae17ab901c93784afc94a/prov-api/docker-requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [prov-api/requirements.txt](https://github.com/provena/provena/blob/a4142d4f1a05431c5c6ae17ab901c93784afc94a/prov-api/requirements.txt)
- `python-docx` (docx, generation) — code_import — [code](https://github.com/provena/provena/blob/a4142d4f1a05431c5c6ae17ab901c93784afc94a/prov-api/helpers/generate_report_helpers.py)

**Evidence trail**

- [api_response](https://github.com/provena/provena) (source: github_api): stars=8, fork=False, archived=False
- [manifest_line](https://github.com/provena/provena/blob/a4142d4f1a05431c5c6ae17ab901c93784afc94a/prov-api/docker-requirements.txt) (source: github_api): python-dotenv sentry-sdk[fastapi] mypy-boto3-kms python-docx==1.1.2 # requires GITHUB_TOKEN as environment variable
- [manifest_line](https://github.com/provena/provena/blob/a4142d4f1a05431c5c6ae17ab901c93784afc94a/prov-api/requirements.txt) (source: github_api): python-dotenv sentry-sdk[fastapi] mypy-boto3-kms python-docx==1.1.2 # this links to the utilities package deployed as part of  # this provena repo - ensure this is correct in your
- [code_permalink](https://github.com/provena/provena/blob/a4142d4f1a05431c5c6ae17ab901c93784afc94a/prov-api/helpers/generate_report_helpers.py) (source: github_api): def add_hyperlink(paragraph: Paragraph, text: str, url: str, color: Optional[RGBColor] = None) -> Optional[docx.oxml.CT_Hyperlink]:     # Python-docx does not have a native .add_hyperlink() functiona
- [other](https://github.com/provena/provena/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/provena/provena/blob/main/README.md) (source: readme): Provena additionally implements a robust data storage solution for seamless interaction with and inspection of the data referenced in provenance records.

### 8. AnujaK/restfiddle

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

### 9. shehanrathnayake/checkpoint-pos-system

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

### 10. jolie-z/Auto-JobHunter

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

### 11. MuhdArshadd/4Tire

**Repository / product**

- Repository: [https://github.com/muhdarshadd/4tire](https://github.com/muhdarshadd/4tire)
- Company: Unknown — not stated in the repository
- Product: 🚗 Car Service and Maintenance System 🛠️
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.70 / 5
- Confidence: medium
- Gate cap applied: **40** — the weighted calculation produced a higher number, but a qualification-gate condition capped it (SCORING_MODEL.md section 14)

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 5 |
| Pipeline complexity | 1 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `iText`, run `run_1`, window `size:0..250`, rank 1
  - Query: `"itext" filename:pom.xml size:0..250`
  - Retrieved 5 of 5 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `iText` (pdf, generation) — manifest_declaration — [pom.xml](https://github.com/MuhdArshadd/4Tire/blob/main/pom.xml)
- `iText` (pdf, generation) — code_import — [code](https://github.com/MuhdArshadd/4Tire/blob/f44e76a8714a37d2ed48ec8c643af157fcd4bb5f/src/view/PaymentMenu.java)

**Evidence trail**

- [api_response](https://github.com/MuhdArshadd/4Tire) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/MuhdArshadd/4Tire/blob/main/pom.xml) (source: github_api): <groupId>com.itextpdf</groupId>
- [code_permalink](https://github.com/MuhdArshadd/4Tire/blob/f44e76a8714a37d2ed48ec8c643af157fcd4bb5f/src/view/PaymentMenu.java) (source: github_api): import java.awt.event.ActionEvent; import javax.swing.JTextArea; import com.itextpdf.text.Chunk; import com.itextpdf.text.Document; import com.itextpdf.text.DocumentException; import com.itextpdf.tex
- [readme_excerpt](https://github.com/MuhdArshadd/4Tire/blob/main/README.md) (source: readme): It helps customers request car services and make payments, while staff can manage bookings and invoices efficiently.

### 12. sourangshupal/multidata-rag-project

**Repository / product**

- Repository: [https://github.com/sourangshupal/multidata-rag-project](https://github.com/sourangshupal/multidata-rag-project)
- Company: Unknown — not stated in the repository
- Product: Multi-Source RAG + Text-to-SQL System
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 40/100 (a score, not a probability)
- Raw weighted score: 2.30 / 5
- Confidence: medium
- Gate cap applied: **40** — the weighted calculation produced a higher number, but a qualification-gate condition capped it (SCORING_MODEL.md section 14)

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 4 |
| Pipeline complexity | 0 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `Docling`, run `run_1`, window `size:1001..2000`, rank 22
  - Query: `"docling" filename:requirements.txt size:1001..2000`
  - Retrieved 30 of 371 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Docling` (other_processing, extraction) — manifest_declaration — [pyproject.toml](https://github.com/sourangshupal/multidata-rag-project/blob/main/pyproject.toml)
- `Docling` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/sourangshupal/multidata-rag-project/blob/main/requirements.txt)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/sourangshupal/multidata-rag-project/blob/3d4169d0a4dd412319e73af439088386e12bca3a/app/services/docling_service.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/sourangshupal/multidata-rag-project/blob/3d4169d0a4dd412319e73af439088386e12bca3a/app/services/document_service.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/sourangshupal/multidata-rag-project/blob/3d4169d0a4dd412319e73af439088386e12bca3a/app/main.py)

**Evidence trail**

- [api_response](https://github.com/sourangshupal/multidata-rag-project) (source: github_api): stars=15, fork=False, archived=False
- [manifest_line](https://github.com/sourangshupal/multidata-rag-project/blob/main/pyproject.toml) (source: github_api): "docling",              # Advanced PDF parsing with layout analysis
- [manifest_line](https://github.com/sourangshupal/multidata-rag-project/blob/main/requirements.txt) (source: github_api): docling                # Advanced PDF parsing with layout analysis
- [code_permalink](https://github.com/sourangshupal/multidata-rag-project/blob/3d4169d0a4dd412319e73af439088386e12bca3a/app/services/docling_service.py) (source: github_api): """ Docling Service Provides context-aware document parsing and chunking using Docling's HybridChunker.
- [code_permalink](https://github.com/sourangshupal/multidata-rag-project/blob/3d4169d0a4dd412319e73af439088386e12bca3a/app/services/document_service.py) (source: github_api): Now supports context-aware chunking with Docling for improved RAG quality. """
- [code_permalink](https://github.com/sourangshupal/multidata-rag-project/blob/3d4169d0a4dd412319e73af439088386e12bca3a/app/main.py) (source: github_api): # If cache miss or cache unavailable, process document         if chunks is None or embeddings is None:             # Parse and chunk with context-aware approach (Docling with smart merging)
- [readme_excerpt](https://github.com/sourangshupal/multidata-rag-project/blob/main/README.md) (source: readme): **Examples:** "How many customers do we have?" "What is the total revenue from delivered orders?" "Show me the top 10 customers by spending" Routed to RAG service for information retrieval: **Keywords

### 13. runtsang/RebuttalStudio

**Repository / product**

- Repository: [https://github.com/runtsang/rebuttalstudio](https://github.com/runtsang/rebuttalstudio)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: events_weddings (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code

**Score**

- Score: 38/100 (a score, not a probability)
- Raw weighted score: 1.90 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 3 |
| Pipeline complexity | 2 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `docx (dolanmiu/docx)`, run `run_1`, window `size:251..500`, rank 18
  - Query: `"docx" filename:package.json size:251..500`
  - Sampled 30 of 2,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,256 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docx (dolanmiu/docx)` (docx, generation) — manifest_declaration — [package-lock.json](https://github.com/runtsang/RebuttalStudio/blob/master/package-lock.json)
- `docx (dolanmiu/docx)` (docx, generation) — manifest_declaration — [package.json](https://github.com/runtsang/RebuttalStudio/blob/master/package.json)
- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/runtsang/RebuttalStudio/blob/1f81e2f0aeccd582df2f5f84dfb3c17da5189599/src/main/main.js)
- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/runtsang/RebuttalStudio/blob/1f81e2f0aeccd582df2f5f84dfb3c17da5189599/src/renderer/i18n/locales.js)

**Evidence trail**

- [api_response](https://github.com/runtsang/RebuttalStudio) (source: github_api): stars=215, fork=False, archived=False
- [manifest_line](https://github.com/runtsang/RebuttalStudio/blob/master/package-lock.json) (source: github_api): "html-to-docx": "^1.8.0",
- [manifest_line](https://github.com/runtsang/RebuttalStudio/blob/master/package.json) (source: github_api): "html-to-docx": "^1.8.0",
- [code_permalink](https://github.com/runtsang/RebuttalStudio/blob/1f81e2f0aeccd582df2f5f84dfb3c17da5189599/src/main/main.js) (source: github_api): const { app, BrowserWindow, ipcMain, shell, dialog } = require('electron'); const HTMLtoDOCX = require('html-to-docx'); const {
- [code_permalink](https://github.com/runtsang/RebuttalStudio/blob/1f81e2f0aeccd582df2f5f84dfb3c17da5189599/src/renderer/i18n/locales.js) (source: github_api): "export.markdown": "Markdown Document (.md)",   "export.word": "Word Document (.docx) (Not supported yet)",
- [other](https://github.com/runtsang/RebuttalStudio/tree/master/documents) (source: github_api): directory documents/ present
- [readme_excerpt](https://github.com/runtsang/RebuttalStudio/blob/master/README.md) (source: readme): By offloading the tedious mechanical work — format conversion, issue segmentation, template management — Rebuttal Studio lets you **focus on the substance of your rebuttal**, which is the part that ac

### 14. Ubada-Hussain/FormFixer

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

### 15. aurcode/ankineitor

**Repository / product**

- Repository: [https://github.com/aurcode/ankineitor](https://github.com/aurcode/ankineitor)
- Company: Unknown — not stated in the repository
- Product: Ankineitor 🤖
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=2, pipeline_stage_count=0 \| supporting: category_count=2; multiple_document_types_handled=true

**Score**

- Score: 37/100 (a score, not a probability)
- Raw weighted score: 1.85 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 3 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 4 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 5/7 dimensions

- Document volume: Unknown
- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `pypdf / PyPDF2`, run `run_1`, window `size:251..500`, rank 7
  - Query: `"pypdf" filename:requirements.txt size:251..500`
  - Sampled 30 of 33,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 33,728 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Unstructured`, run `run_1`, window `size:251..500`, rank 13
  - Query: `"unstructured" filename:requirements.txt size:251..500`
  - Sampled 30 of 4,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 4,256 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Unstructured`, run `run_1`, window `size:501..1000`, rank 8
  - Query: `"unstructured" filename:pyproject.toml size:501..1000`
  - Sampled 30 of 1,512 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,512 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Unstructured` (other_processing, extraction) — manifest_declaration — [pyproject.toml](https://github.com/aurcode/ankineitor/blob/master/pyproject.toml)
- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/aurcode/ankineitor/blob/master/requirements.txt)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/aurcode/ankineitor/blob/5b6f4fc1ca0ce523132b43cd1782ced831bf0d28/src/ankineitor/pipeline/text_extractor.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/aurcode/ankineitor/blob/5b6f4fc1ca0ce523132b43cd1782ced831bf0d28/tests/test_text_extractor.py)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [pyproject.toml](https://github.com/aurcode/ankineitor/blob/master/pyproject.toml)
- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [requirements.txt](https://github.com/aurcode/ankineitor/blob/master/requirements.txt)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/aurcode/ankineitor/blob/5b6f4fc1ca0ce523132b43cd1782ced831bf0d28/src/ankineitor/pipeline/text_extractor.py)

**Evidence trail**

- [api_response](https://github.com/aurcode/ankineitor) (source: github_api): stars=83, fork=False, archived=False
- [manifest_line](https://github.com/aurcode/ankineitor/blob/master/pyproject.toml) (source: github_api): "unstructured",
- [manifest_line](https://github.com/aurcode/ankineitor/blob/master/requirements.txt) (source: github_api): unstructured
- [code_permalink](https://github.com/aurcode/ankineitor/blob/5b6f4fc1ca0ce523132b43cd1782ced831bf0d28/src/ankineitor/pipeline/text_extractor.py) (source: github_api): PYTESSERACT_AVAILABLE = False     pytesseract = None # --- Unstructured Imports (optional at runtime) --- UNSTRUCTURED_AVAILABLE = True try:     from unstructured.partition.auto import partition
- [code_permalink](https://github.com/aurcode/ankineitor/blob/5b6f4fc1ca0ce523132b43cd1782ced831bf0d28/tests/test_text_extractor.py) (source: github_api): class FakeElement:     """Minimal stand-in for unstructured elements."""
- [manifest_line](https://github.com/aurcode/ankineitor/blob/master/pyproject.toml) (source: github_api): "pypdf",
- [manifest_line](https://github.com/aurcode/ankineitor/blob/master/requirements.txt) (source: github_api): pypdf
- [code_permalink](https://github.com/aurcode/ankineitor/blob/5b6f4fc1ca0ce523132b43cd1782ced831bf0d28/src/ankineitor/pipeline/text_extractor.py) (source: github_api): JIEBA_AVAILABLE = False     pseg = None PYPDF_AVAILABLE = True try:     from pypdf import PdfReader except ModuleNotFoundError:
- [readme_excerpt](https://github.com/aurcode/ankineitor/blob/master/README.md) (source: readme): This file allows you to define: The Anki card model (fields, templates).

### 16. MarvekG/BestAITrader

**Repository / product**

- Repository: [https://github.com/marvekg/bestaitrader](https://github.com/marvekg/bestaitrader)
- Company: Unknown — not stated in the repository
- Product: 天枢智投 (Best-AI-Trader)
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
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

- Tier 3, `mammoth / python-mammoth`, run `run_1`, window `size:501..1000`, rank 19
  - Query: `"mammoth" filename:requirements.txt size:501..1000`
  - Retrieved 30 of 309 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `pdf2docx`, run `run_1`, window `size:501..1000`, rank 4
  - Query: `"pdf2docx" filename:requirements.txt size:501..1000`
  - Retrieved 30 of 171 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [backend/requirements.txt](https://github.com/MarvekG/BestAITrader/blob/main/backend/requirements.txt)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/app/data/pdf_parser.py)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [backend/app/ai/agentic/tooling/news_plugins/requirements.txt](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/app/ai/agentic/tooling/news_plugins/requirements.txt)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/tests/test_pdf_parser_service.py)
- `pdf2docx` (other_processing, mixed) — manifest_declaration — [backend/requirements.txt](https://github.com/MarvekG/BestAITrader/blob/main/backend/requirements.txt)
- `pdf2docx` (other_processing, mixed) — code_import — [code](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/app/data/pdf_parser.py)
- `pdf2docx` (other_processing, mixed) — manifest_declaration — [backend/app/ai/agentic/tooling/news_plugins/requirements.txt](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/app/ai/agentic/tooling/news_plugins/requirements.txt)
- `pdf2docx` (other_processing, mixed) — code_import — [code](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/tests/test_pdf_parser_service.py)
- `pdf2docx` (other_processing, mixed) — code_import — [code](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/tests/test_pdf_tool.py)

**Evidence trail**

- [api_response](https://github.com/MarvekG/BestAITrader) (source: github_api): stars=35, fork=False, archived=False
- [manifest_line](https://github.com/MarvekG/BestAITrader/blob/main/backend/requirements.txt) (source: github_api): mammoth>=1.8.0
- [code_permalink](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/app/data/pdf_parser.py) (source: github_api): logger.info("Converting Word to Markdown: %s", docx_path)             import mammoth             from markdownify import markdownify as md
- [manifest_line](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/app/ai/agentic/tooling/news_plugins/requirements.txt) (source: github_api): feedparser trafilatura markdownify>=0.13.1 pycryptodome>=3.23.0 pymupdf4llm>=0.0.17 pdf2docx>=0.5.8 mammoth>=1.8.0
- [code_permalink](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/tests/test_pdf_parser_service.py) (source: github_api): fake_pdf2docx = types.SimpleNamespace(Converter=FakeConverter)     fake_mammoth = types.SimpleNamespace(         convert_to_html=lambda _file: types.SimpleNamespace(value="<p>converted</p>")
- [manifest_line](https://github.com/MarvekG/BestAITrader/blob/main/backend/requirements.txt) (source: github_api): pdf2docx>=0.5.8
- [code_permalink](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/app/data/pdf_parser.py) (source: github_api): PDF2DOCX_PAGE_STATE_PATTERN = "pages-*.json"
- [manifest_line](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/app/ai/agentic/tooling/news_plugins/requirements.txt) (source: github_api): feedparser trafilatura markdownify>=0.13.1 pycryptodome>=3.23.0 pymupdf4llm>=0.0.17 pdf2docx>=0.5.8 mammoth>=1.8.0
- [code_permalink](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/tests/test_pdf_parser_service.py) (source: github_api): fake_pdf2docx = types.SimpleNamespace(Converter=FakeConverter)     fake_mammoth = types.SimpleNamespace(
- [code_permalink](https://github.com/MarvekG/BestAITrader/blob/15d5b1a9a955545874d021aa4c2c6358ea4fd247/backend/tests/test_pdf_tool.py) (source: github_api): def test_pdf_parser_cleans_pdf2docx_page_state_files(tmp_path, monkeypatch):     keep_path = tmp_path / "not-pages-0.json"

### 17. Entity069/wtpdf-playground

**Repository / product**

- Repository: [https://github.com/entity069/wtpdf-playground](https://github.com/entity069/wtpdf-playground)
- Company: Unknown — not stated in the repository
- Product: wtpdf-playground
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

- Tier 3, `pikepdf`, run `run_1`, window `size:0..250`, rank 6
  - Query: `"pikepdf" filename:pyproject.toml size:0..250`
  - Retrieved 15 of 15 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pikepdf` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/Entity069/wtpdf-playground/blob/main/pyproject.toml)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/Entity069/wtpdf-playground/blob/21462c17f37eaa8c79fc7a2d4c7ecc017834422c/parser.py)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/Entity069/wtpdf-playground/blob/21462c17f37eaa8c79fc7a2d4c7ecc017834422c/builder.py)

**Evidence trail**

- [api_response](https://github.com/Entity069/wtpdf-playground) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/Entity069/wtpdf-playground/blob/main/pyproject.toml) (source: github_api): "pikepdf",
- [code_permalink](https://github.com/Entity069/wtpdf-playground/blob/21462c17f37eaa8c79fc7a2d4c7ecc017834422c/parser.py) (source: github_api): import pikepdf from pikepdf import Dictionary, Array TYPE_COLOURS = {     "Document": "#7c3aed", "Part": "#6d28d9", "Art": "#6d28d9",     "Sect": "#5b21b6", "Div": "#4c1d95", "NonStruct": "#374151",
- [code_permalink](https://github.com/Entity069/wtpdf-playground/blob/21462c17f37eaa8c79fc7a2d4c7ecc017834422c/builder.py) (source: github_api): import pikepdf from pikepdf import Dictionary, Array, Name, String import io import textwrap ALLOWED_TYPES = {     "Document", "Part", "Art", "Sect", "Div", "BlockQuote", "Caption",
- [other](https://github.com/Entity069/wtpdf-playground/tree/main/templates) (source: github_api): directory templates/ present

### 18. proto-at-block/bitkey

**Repository / product**

- Repository: [https://github.com/proto-at-block/bitkey](https://github.com/proto-at-block/bitkey)
- Company: Unknown — not stated in the repository
- Product: Bitkey
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://bitkey.world

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
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `Apache PDFBox`, run `run_1`, window `size:1001..2000`, rank 20
  - Query: `"pdfbox" filename:build.gradle size:1001..2000`
  - Sampled 30 of 1,100 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,100 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Apache PDFBox` (pdf, generation) — manifest_declaration — [app/libs/platform/impl/build.gradle.kts](https://github.com/proto-at-block/bitkey/blob/4ba8c4c87dfe16b7514b328f523233bb7501c246/app/libs/platform/impl/build.gradle.kts)
- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/proto-at-block/bitkey/blob/4ba8c4c87dfe16b7514b328f523233bb7501c246/app/libs/platform/impl/src/androidMain/kotlin/build/wallet/platform/pdf/PdfAnnotatorImpl.android.kt)
- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/proto-at-block/bitkey/blob/4ba8c4c87dfe16b7514b328f523233bb7501c246/app/libs/platform/impl/src/androidMain/kotlin/build/wallet/platform/pdf/PdfAnnotatorFactoryImpl.android.kt)

**Evidence trail**

- [api_response](https://github.com/proto-at-block/bitkey) (source: github_api): stars=221, fork=False, archived=False
- [manifest_line](https://github.com/proto-at-block/bitkey/blob/4ba8c4c87dfe16b7514b328f523233bb7501c246/app/libs/platform/impl/build.gradle.kts) (source: github_api): dependencies {         implementation(libs.android.browser)         implementation(libs.android.core.ktx)         implementation(libs.android.pdfbox)         implementation(libs.android.biometri
- [code_permalink](https://github.com/proto-at-block/bitkey/blob/4ba8c4c87dfe16b7514b328f523233bb7501c246/app/libs/platform/impl/src/androidMain/kotlin/build/wallet/platform/pdf/PdfAnnotatorImpl.android.kt) (source: github_api): import com.github.michaelbull.result.binding import com.github.michaelbull.result.mapError import com.github.michaelbull.result.toResultOr import com.tom_roush.pdfbox.pdmodel.PDDocument import com.tom
- [code_permalink](https://github.com/proto-at-block/bitkey/blob/4ba8c4c87dfe16b7514b328f523233bb7501c246/app/libs/platform/impl/src/androidMain/kotlin/build/wallet/platform/pdf/PdfAnnotatorFactoryImpl.android.kt) (source: github_api): import build.wallet.di.AppScope import build.wallet.di.BitkeyInject import com.github.michaelbull.result.mapError import com.tom_roush.pdfbox.android.PDFBoxResourceLoader import com.tom_roush.pdfbox.p
- [readme_excerpt](https://github.com/proto-at-block/bitkey/blob/main/README.md) (source: readme): To protect our customers, we ask that you report vulnerabilities to us as soon as you can, and that you coordinate disclosure with us first, so that we can understand and mitigate reported vulnerabili

### 19. Mufath/SerbaBisa

**Repository / product**

- Repository: [https://github.com/mufath/serbabisa](https://github.com/mufath/serbabisa)
- Company: Unknown — not stated in the repository
- Product: 🛠️ SerbaBisa
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

- Tier 3, `pdf2docx`, run `run_1`, window `size:251..500`, rank 23
  - Query: `"pdf2docx" filename:requirements.txt size:251..500`
  - Retrieved 30 of 247 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pdf2docx` (other_processing, mixed) — manifest_declaration — [requirements.txt](https://github.com/Mufath/SerbaBisa/blob/main/requirements.txt)
- `pdf2docx` (other_processing, mixed) — code_import — [code](https://github.com/Mufath/SerbaBisa/blob/7cace5f8747c2be3e46ad72d6384a815e6858151/routes/convert_tools.py)

**Evidence trail**

- [api_response](https://github.com/Mufath/SerbaBisa) (source: github_api): stars=3, fork=False, archived=False
- [manifest_line](https://github.com/Mufath/SerbaBisa/blob/main/requirements.txt) (source: github_api): pdf2docx
- [code_permalink](https://github.com/Mufath/SerbaBisa/blob/7cace5f8747c2be3e46ad72d6384a815e6858151/routes/convert_tools.py) (source: github_api): from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT try:     from pdf2docx import Converter as Pdf2DocxConverter     HAS_PDF2DOCX = True except ImportError:     HAS_PDF2DOCX = False
- [other](https://github.com/Mufath/SerbaBisa/tree/main/templates) (source: github_api): directory templates/ present

### 20. luckylykkk/nnscholar-search

**Repository / product**

- Repository: [https://github.com/luckylykkk/nnscholar-search](https://github.com/luckylykkk/nnscholar-search)
- Company: Unknown — not stated in the repository
- Product: 🧬 NNScholar - 智能学术文献检索与分析平台
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

- Tier 3, `python-docx`, run `run_1`, window `size:251..500`, rank 16
  - Query: `"python-docx" filename:requirements.txt size:251..500`
  - Sampled 30 of 16,192 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 16,192 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `python-docx` (docx, generation) — manifest_declaration — [requirements.txt](https://github.com/luckylykkk/nnscholar-search/blob/7.17/requirements.txt)
- `python-docx` (docx, generation) — code_import — [code](https://github.com/luckylykkk/nnscholar-search/blob/a8fa6a95d78ac5fc099e39d05c85a15e691e80a8/services/word_export_service.py)
- `python-docx` (docx, generation) — code_import — [code](https://github.com/luckylykkk/nnscholar-search/blob/a8fa6a95d78ac5fc099e39d05c85a15e691e80a8/routes/export_routes.py)

**Evidence trail**

- [api_response](https://github.com/luckylykkk/nnscholar-search) (source: github_api): stars=100, fork=False, archived=False
- [manifest_line](https://github.com/luckylykkk/nnscholar-search/blob/7.17/requirements.txt) (source: github_api): python-docx==1.1.0
- [code_permalink](https://github.com/luckylykkk/nnscholar-search/blob/a8fa6a95d78ac5fc099e39d05c85a15e691e80a8/services/word_export_service.py) (source: github_api): if not DOCX_AVAILABLE:             logger.warning("python-docx not available, Word export will be disabled")
- [code_permalink](https://github.com/luckylykkk/nnscholar-search/blob/a8fa6a95d78ac5fc099e39d05c85a15e691e80a8/routes/export_routes.py) (source: github_api): return buffer.getvalue()     except ImportError:         logger.error("python-docx库未安装，无法生成Word文档")         return None     except Exception as e:         logger.error(f"生成综述Word文档失败: {e}")
- [other](https://github.com/luckylykkk/nnscholar-search/tree/7.17/templates) (source: github_api): directory templates/ present

### 21. SudoXploit7/DefenSight-AI

**Repository / product**

- Repository: [https://github.com/sudoxploit7/defensight-ai](https://github.com/sudoxploit7/defensight-ai)
- Company: Unknown — not stated in the repository
- Product: DefenSight AI - Autonomous Network Defense Copilot
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

- Tier 3, `ReportLab`, run `run_1`, window `size:0..250`, rank 13
  - Query: `"reportlab" filename:requirements.txt size:0..250`
  - Sampled 30 of 30,016 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 30,016 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [requirements.txt.txt](https://github.com/SudoXploit7/DefenSight-AI/blob/main/requirements.txt.txt)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/SudoXploit7/DefenSight-AI/blob/b0fe7aaee7395ce4fee3d772001659991cc32688/gui_app.py)

**Evidence trail**

- [api_response](https://github.com/SudoXploit7/DefenSight-AI) (source: github_api): stars=5, fork=False, archived=False
- [manifest_line](https://github.com/SudoXploit7/DefenSight-AI/blob/main/requirements.txt.txt) (source: github_api): reportlab
- [code_permalink](https://github.com/SudoXploit7/DefenSight-AI/blob/b0fe7aaee7395ce4fee3d772001659991cc32688/gui_app.py) (source: github_api): from flask_login import LoginManager, login_user, logout_user, login_required, current_user from auth import db, bcrypt, User from reportlab.lib.pagesizes import A4 from reportlab.platypus import (
- [other](https://github.com/SudoXploit7/DefenSight-AI/tree/main/templates) (source: github_api): directory templates/ present

### 22. nbazaes/django-bazpos

**Repository / product**

- Repository: [https://github.com/nbazaes/django-bazpos](https://github.com/nbazaes/django-bazpos)
- Company: Unknown — not stated in the repository
- Product: BazPOS — Sistema de Punto de Venta
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

- Tier 3, `docx (dolanmiu/docx)`, run `run_1`, window `size:0..250`, rank 15
  - Query: `"docx" filename:package.json size:0..250`
  - Retrieved 30 of 721 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/nbazaes/django-bazpos/blob/fbf8d4bf70a62dbbb41e59ed4b6d1dabaa03e067/.agents/skills/docx/scripts/comment.py)
- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/nbazaes/django-bazpos/blob/fbf8d4bf70a62dbbb41e59ed4b6d1dabaa03e067/.agents/skills/docx/scripts/merge_runs.py)
- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/nbazaes/django-bazpos/blob/fbf8d4bf70a62dbbb41e59ed4b6d1dabaa03e067/.agents/skills/docx/scripts/accept_changes.py)
- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/nbazaes/django-bazpos/blob/fbf8d4bf70a62dbbb41e59ed4b6d1dabaa03e067/.agents/skills/docx/scripts/office/validate.py)

**Evidence trail**

- [api_response](https://github.com/nbazaes/django-bazpos) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/nbazaes/django-bazpos/blob/fbf8d4bf70a62dbbb41e59ed4b6d1dabaa03e067/.agents/skills/docx/scripts/comment.py) (source: github_api): """Add comments to a DOCX document. Accepts either an unpacked directory OR a .docx/.dotx file directly. Usage:     # Against an unpacked directory (writes satellite files in place)     python comme
- [code_permalink](https://github.com/nbazaes/django-bazpos/blob/fbf8d4bf70a62dbbb41e59ed4b6d1dabaa03e067/.agents/skills/docx/scripts/merge_runs.py) (source: github_api): """Merge adjacent identically-formatted runs in a DOCX. Word fragments paragraph text across many <w:r> elements (revision ids,
- [code_permalink](https://github.com/nbazaes/django-bazpos/blob/fbf8d4bf70a62dbbb41e59ed4b6d1dabaa03e067/.agents/skills/docx/scripts/accept_changes.py) (source: github_api): """Accept all tracked changes in a DOCX file using LibreOffice. Requires LibreOffice (soffice) to be installed.
- [code_permalink](https://github.com/nbazaes/django-bazpos/blob/fbf8d4bf70a62dbbb41e59ed4b6d1dabaa03e067/.agents/skills/docx/scripts/office/validate.py) (source: github_api): - An unpacked directory containing the Office document XML files - A packed Office file (.docx/.pptx/.xlsx or .dotx/.potx/.xltx template) which will be unpacked to a temp directory
- [other](https://github.com/nbazaes/django-bazpos/tree/main/templates) (source: github_api): directory templates/ present

### 23. Cyberwatch/Pentest-Collaboration-Framework

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

### 24. varadlad/varadlad-portfolio

**Repository / product**

- Repository: [https://github.com/varadlad/varadlad-portfolio](https://github.com/varadlad/varadlad-portfolio)
- Company: Unknown — not stated in the repository
- Product: [Varad Lad Portfolio Website](https://varadlad.github.io/varadlad-portfolio/)
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://varadlad.github.io/varadlad-portfolio/

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

- Tier 3, `ReportLab`, run `run_1`, window `size:0..250`, rank 24
  - Query: `"reportlab" filename:requirements.txt size:0..250`
  - Sampled 30 of 30,016 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 30,016 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [pdf_requirements.txt](https://github.com/varadlad/varadlad-portfolio/blob/main/pdf_requirements.txt)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/varadlad/varadlad-portfolio/blob/f21316ec7a792d5f1153673fbff0a10c3306eae9/generate_portfolio_pdf.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/varadlad/varadlad-portfolio/blob/f21316ec7a792d5f1153673fbff0a10c3306eae9/improved_portfolio_pdf.py)

**Evidence trail**

- [api_response](https://github.com/varadlad/varadlad-portfolio) (source: github_api): stars=2, fork=False, archived=False
- [manifest_line](https://github.com/varadlad/varadlad-portfolio/blob/main/pdf_requirements.txt) (source: github_api): reportlab>=3.6.0
- [code_permalink](https://github.com/varadlad/varadlad-portfolio/blob/f21316ec7a792d5f1153673fbff0a10c3306eae9/generate_portfolio_pdf.py) (source: github_api): """ import os from reportlab.lib.pagesizes import letter, A4 from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle from reportlab.lib.units import inch from reportlab.lib.colors import
- [code_permalink](https://github.com/varadlad/varadlad-portfolio/blob/f21316ec7a792d5f1153673fbff0a10c3306eae9/improved_portfolio_pdf.py) (source: github_api): """ import os from reportlab.lib.pagesizes import letter, A4 from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle from reportlab.lib.units import inch from reportlab.lib.colors import
- [readme_excerpt](https://github.com/varadlad/varadlad-portfolio/blob/main/README.md) (source: readme): Built with HTML, CSS, and JavaScript, it is fully responsive and designed for clarity and impact.

### 25. peerdavid/remapy

**Repository / product**

- Repository: [https://github.com/peerdavid/remapy](https://github.com/peerdavid/remapy)
- Company: Freepik
- Product: RemaPy Explorer
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

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

- Tier 3, `ReportLab`, run `run_1`, window `size:0..250`, rank 7
  - Query: `"reportlab" filename:requirements.txt size:0..250`
  - Sampled 30 of 30,016 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 30,016 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [requirements.txt](https://github.com/peerdavid/remapy/blob/master/requirements.txt)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/peerdavid/remapy/blob/a5f811ad93831e14220be5947226882e43b9033e/setup.py)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/peerdavid/remapy/blob/a5f811ad93831e14220be5947226882e43b9033e/model/render.py)

**Evidence trail**

- [api_response](https://github.com/peerdavid/remapy) (source: github_api): stars=182, fork=False, archived=False
- [readme_excerpt](https://github.com/peerdavid/remapy/blob/master/README.md) (source: readme): company stated as 'Freepik'
- [manifest_line](https://github.com/peerdavid/remapy/blob/master/requirements.txt) (source: github_api): reportlab
- [code_permalink](https://github.com/peerdavid/remapy/blob/a5f811ad93831e14220be5947226882e43b9033e/setup.py) (source: github_api): "Pillow",         "pdfrw",         "pyyaml",         "reportlab",         "requests",     ],     package_data={
- [code_permalink](https://github.com/peerdavid/remapy/blob/a5f811ad93831e14220be5947226882e43b9033e/model/render.py) (source: github_api): from pdfrw import PdfReader, PdfWriter, PageMerge from reportlab.lib import colors from reportlab.pdfgen import canvas # Size DEFAULT_IMAGE_WIDTH = 1404
- [readme_excerpt](https://github.com/peerdavid/remapy/blob/master/README.md) (source: readme): The rendering is implemented accordingly to [4]:<br /> <img src="doc/goofy.png" width="500sp" /> Custom colors for individual layers are used by RemaPy for rendering if the layer name contains a '#' f

### 26. guangxiangdebizi/TradingAgents-MCPmode

**Repository / product**

- Repository: [https://github.com/guangxiangdebizi/tradingagents-mcpmode](https://github.com/guangxiangdebizi/tradingagents-mcpmode)
- Company: Unknown — not stated in the repository
- Product: TradingAgents-MCPmode
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://47.79.147.241:8501/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 35/100 (a score, not a probability)
- Raw weighted score: 1.75 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 2 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden | 4 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `python-docx`, run `run_1`, window `size:1001..2000`, rank 9
  - Query: `"python-docx" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 8,336 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 8,336 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `WeasyPrint`, run `run_1`, window `size:1001..2000`, rank 8
  - Query: `"weasyprint" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 2,532 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,532 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `(co-occurrence query, spans multiple libraries)`, run `run_1`, window `size:1001..2000`, rank 9
  - Query: `"python-docx" "reportlab" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 1,362 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,362 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements.txt](https://github.com/guangxiangdebizi/TradingAgents-MCPmode/blob/main/requirements.txt)
- `python-docx` (docx, generation) — manifest_declaration — [requirements.txt](https://github.com/guangxiangdebizi/TradingAgents-MCPmode/blob/main/requirements.txt)
- `python-docx` (docx, generation) — code_import — [code](https://github.com/guangxiangdebizi/TradingAgents-MCPmode/blob/8806e3b5327b035b32e6d864b9afe6009f8103d4/src/dumptools/md2docx.py)

**Evidence trail**

- [api_response](https://github.com/guangxiangdebizi/TradingAgents-MCPmode) (source: github_api): stars=335, fork=False, archived=False
- [manifest_line](https://github.com/guangxiangdebizi/TradingAgents-MCPmode/blob/main/requirements.txt) (source: github_api): weasyprint>=61.0     # PDF生成首选方案，支持CSS样式
- [manifest_line](https://github.com/guangxiangdebizi/TradingAgents-MCPmode/blob/main/requirements.txt) (source: github_api): python-docx>=0.8.11  # DOCX文档生成
- [code_permalink](https://github.com/guangxiangdebizi/TradingAgents-MCPmode/blob/8806e3b5327b035b32e6d864b9afe6009f8103d4/src/dumptools/md2docx.py) (source: github_api): from docx.enum.style import WD_STYLE_TYPE     from docx.oxml.shared import OxmlElement, qn except ImportError:     print("❌ 缺少依赖包，请安装：pip install python-docx")     sys.exit(1)

### 27. ghk/sideka-electron

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

### 28. keystrokehq/keystroke

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

### 29. activepieces/activepieces

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

### 30. mleoca/ucn

**Repository / product**

- Repository: [https://github.com/mleoca/ucn](https://github.com/mleoca/ucn)
- Company: Unknown — not stated in the repository
- Product: UCN - Universal Code Navigator
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
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

- Tier 3, `Apache POI (XWPF/HWPF)`, run `run_1`, window `size:0..250`, rank 28
  - Query: `"poi" filename:pom.xml size:0..250`
  - Retrieved 28 of 28 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache POI (XWPF/HWPF)` (docx, generation) — manifest_declaration — [package-lock.json](https://github.com/mleoca/ucn/blob/main/package-lock.json)
- `Apache POI (XWPF/HWPF)` (docx, generation) — manifest_declaration — [package.json](https://github.com/mleoca/ucn/blob/main/package.json)
- `Apache POI (XWPF/HWPF)` (docx, generation) — code_import — [code](https://github.com/mleoca/ucn/blob/514dbd8a06f9018b52f30e04f4b7dc209ecd2544/ucn.js)
- `Apache POI (XWPF/HWPF)` (docx, generation) — code_import — [code](https://github.com/mleoca/ucn/blob/514dbd8a06f9018b52f30e04f4b7dc209ecd2544/core/check.js)
- `Apache POI (XWPF/HWPF)` (docx, generation) — code_import — [code](https://github.com/mleoca/ucn/blob/514dbd8a06f9018b52f30e04f4b7dc209ecd2544/languages/html.js)

**Evidence trail**

- [api_response](https://github.com/mleoca/ucn) (source: github_api): stars=1, fork=False, archived=False
- [manifest_line](https://github.com/mleoca/ucn/blob/main/package-lock.json) (source: github_api): "integrity": "sha512-hvpoI6korhJMnej285dSg6nu1+e6uxs7zG3BYAm5byqDsgJNWwxzM6z6iZiAgQR4TJ30JmBTOwqZUw3WlyH3AQ==",
- [manifest_line](https://github.com/mleoca/ucn/blob/main/package.json) (source: github_api): "endpoints",
- [code_permalink](https://github.com/mleoca/ucn/blob/514dbd8a06f9018b52f30e04f4b7dc209ecd2544/ucn.js) (source: github_api): #!/usr/bin/env node /**  * UCN entry point wrapper  * Redirects to the actual CLI implementation  */
- [code_permalink](https://github.com/mleoca/ucn/blob/514dbd8a06f9018b52f30e04f4b7dc209ecd2544/core/check.js) (source: github_api): };         // Orphan = newly added with zero caller CANDIDATES IN EITHER TIER and         // not detected as an entry point. Zero confirmed + N unverified is NOT         // orphan (the #223 r
- [code_permalink](https://github.com/mleoca/ucn/blob/514dbd8a06f9018b52f30e04f4b7dc209ecd2544/languages/html.js) (source: github_api): } /**  * Classify an HTML symbol as a runtime entry point.  * HTML has no entry points of its own — JS extracted from <script> blocks  * is classified by the JS predicate.  */
- [readme_excerpt](https://github.com/mleoca/ucn/blob/main/README.md) (source: readme): And it's built for auditable trust.

### 31. rhshah/iAnnotateSV

**Repository / product**

- Repository: [https://github.com/rhshah/iannotatesv](https://github.com/rhshah/iannotatesv)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://iannotatesv.readthedocs.org/en/latest/index.html

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 33/100 (a score, not a probability)
- Raw weighted score: 1.65 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 3 |
| Pipeline complexity | 1 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `ReportLab`, run `run_1`, window `size:501..1000`, rank 21
  - Query: `"reportlab" filename:pyproject.toml size:501..1000`
  - Sampled 30 of 3,440 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,440 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [pyproject.toml](https://github.com/rhshah/iAnnotateSV/blob/master/pyproject.toml)
- `ReportLab` (pdf, generation) — manifest_declaration — [requirements-dev.txt](https://github.com/rhshah/iAnnotateSV/blob/master/requirements-dev.txt)
- `ReportLab` (pdf, generation) — manifest_declaration — [requirements.txt](https://github.com/rhshah/iAnnotateSV/blob/master/requirements.txt)
- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/rhshah/iAnnotateSV/blob/bb8fcda690aa02368fa9a97bd77484da753cb211/setup.py)

**Evidence trail**

- [api_response](https://github.com/rhshah/iAnnotateSV) (source: github_api): stars=16, fork=False, archived=False
- [manifest_line](https://github.com/rhshah/iAnnotateSV/blob/master/pyproject.toml) (source: github_api): reportlab = "3.6.13"
- [manifest_line](https://github.com/rhshah/iAnnotateSV/blob/master/requirements-dev.txt) (source: github_api): reportlab==3.6.13
- [manifest_line](https://github.com/rhshah/iAnnotateSV/blob/master/requirements.txt) (source: github_api): reportlab==3.6.13
- [code_permalink](https://github.com/rhshah/iAnnotateSV/blob/bb8fcda690aa02368fa9a97bd77484da753cb211/setup.py) (source: github_api): 'pandas==2.2.2',           'pillow==10.4.0',           'biopython==1.84',           'reportlab==3.6.13',           'coloredlogs==15.0.1',       ],       zip_safe=False,
- [readme_excerpt](https://github.com/rhshah/iAnnotateSV/blob/master/README.rst) (source: readme): It is designed for use with hybrid capture, including both whole-exome and custom target panels, and short-read sequencing platforms such as Illumina.

### 32. LeDat98/NexusRAG

**Repository / product**

- Repository: [https://github.com/ledat98/nexusrag](https://github.com/ledat98/nexusrag)
- Company: Unknown — not stated in the repository
- Product: NexusRAG
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 33/100 (a score, not a probability)
- Raw weighted score: 1.65 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 0 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 4 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `Docling`, run `run_1`, window `size:501..1000`, rank 13
  - Query: `"docling" filename:requirements.txt size:501..1000`
  - Retrieved 30 of 740 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Docling` (other_processing, extraction) — manifest_declaration — [backend/requirements.txt](https://github.com/LeDat98/NexusRAG/blob/main/backend/requirements.txt)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/LeDat98/NexusRAG/blob/1d4791c6b352091f773f276ccbc86a605f55e5b2/backend/app/services/document_parser/docling_parser.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/LeDat98/NexusRAG/blob/1d4791c6b352091f773f276ccbc86a605f55e5b2/backend/app/main.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/LeDat98/NexusRAG/blob/1d4791c6b352091f773f276ccbc86a605f55e5b2/backend/app/core/config.py)

**Evidence trail**

- [api_response](https://github.com/LeDat98/NexusRAG) (source: github_api): stars=487, fork=False, archived=False
- [manifest_line](https://github.com/LeDat98/NexusRAG/blob/main/backend/requirements.txt) (source: github_api): # Document parsing (Docling — default)
- [code_permalink](https://github.com/LeDat98/NexusRAG/blob/1d4791c6b352091f773f276ccbc86a605f55e5b2/backend/app/services/document_parser/docling_parser.py) (source: github_api): # File extensions handled by Docling vs legacy _DOCLING_EXTENSIONS = {".pdf", ".docx", ".pptx", ".html"}
- [code_permalink](https://github.com/LeDat98/NexusRAG/blob/1d4791c6b352091f773f276ccbc86a605f55e5b2/backend/app/main.py) (source: github_api): app.include_router(api_router, prefix="/api/v1") # Static files — document images extracted by NexusRAG (Docling) _docling_data = Path(__file__).resolve().parent.parent / "data" / "docling" _docling
- [code_permalink](https://github.com/LeDat98/NexusRAG/blob/1d4791c6b352091f773f276ccbc86a605f55e5b2/backend/app/core/config.py) (source: github_api): NEXUSRAG_DEFAULT_QUERY_MODE: str = "hybrid"     NEXUSRAG_DOCLING_IMAGES_SCALE: float = 2.0     NEXUSRAG_MAX_IMAGES_PER_DOC: int = 50
- [readme_excerpt](https://github.com/LeDat98/NexusRAG/blob/main/README.md) (source: readme): You can directly add the NexusRAG MCP server to Cursor or Claude as an SSE connection using the URL: `http://localhost:8000/mcp` *(Note: some clients still label this as an SSE connection, but use the

### 33. buzzqw/NotePadPQ

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

### 34. kartoza/docker-mezzanine

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

### 35. metorial/metorial

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

### 36. watat83/document-chat-system

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

### 37. ASUCICREPO/PDF_Accessibility

**Repository / product**

- Repository: [https://github.com/asucicrepo/pdf_accessibility](https://github.com/asucicrepo/pdf_accessibility)
- Company: Arizona State University
- Product: PDF Accessibility Solutions
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.remediate-pdf.com/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: contributor_count not collected

**Score**

- Score: 32/100 (a score, not a probability)
- Raw weighted score: 1.60 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 1 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 3 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `pdf-lib`, run `run_1`, window `size:0..250`, rank 5
  - Query: `"pdf-lib" filename:package.json size:0..250`
  - Retrieved 30 of 549 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pdf-lib` (pdf, generation) — manifest_declaration — [alt-text-generator-container/package.json](https://github.com/ASUCICREPO/PDF_Accessibility/blob/50ee27545912c871789bcb41965679d2d24c95b9/alt-text-generator-container/package.json)
- `pdf-lib` (pdf, generation) — code_import — [code](https://github.com/ASUCICREPO/PDF_Accessibility/blob/50ee27545912c871789bcb41965679d2d24c95b9/alt-text-generator-container/alt_text_generator.js)

**Evidence trail**

- [api_response](https://github.com/ASUCICREPO/PDF_Accessibility) (source: github_api): stars=128, fork=False, archived=False
- [readme_excerpt](https://github.com/ASUCICREPO/PDF_Accessibility/blob/main/README.md) (source: readme): company stated as 'Arizona State University'
- [manifest_line](https://github.com/ASUCICREPO/PDF_Accessibility/blob/50ee27545912c871789bcb41965679d2d24c95b9/alt-text-generator-container/package.json) (source: github_api): "@aws-sdk/client-bedrock-runtime": "^3.632.0",     "@aws-sdk/client-s3": "^3.633.0",     "better-sqlite3": "^11.8.1",     "pdf-lib": "^1.17.1",     "winston": "^3.14.2"   } }
- [code_permalink](https://github.com/ASUCICREPO/PDF_Accessibility/blob/50ee27545912c871789bcb41965679d2d24c95b9/alt-text-generator-container/alt_text_generator.js) (source: github_api): const winston = require('winston'); const pdfLib = require('pdf-lib'); const stream = require('stream');
- [readme_excerpt](https://github.com/ASUCICREPO/PDF_Accessibility/blob/main/README.md) (source: readme): Customers are responsible for making their own independent assessment of the information in this document.

### 38. giovanniuchoa/DocumentinAPI

**Repository / product**

- Repository: [https://github.com/giovanniuchoa/documentinapi](https://github.com/giovanniuchoa/documentinapi)
- Company: Unknown — not stated in the repository
- Product: DocumentinAPI
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://documentinapi.onrender.com/swagger

**Qualification**

- Status: **keep**
- Confidence: high
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=2 \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code

**Score**

- Score: 30/100 (a score, not a probability)
- Raw weighted score: 1.50 / 5
- Confidence: high

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 0 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `Aspose.Words`, run `run_1`, window `size:1001..2000`, rank 27
  - Query: `"Aspose.Words" extension:csproj size:1001..2000`
  - Retrieved 30 of 187 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Aspose.Words` (docx, generation) — manifest_declaration — [DocumentinAPI.csproj](https://github.com/giovanniuchoa/DocumentinAPI/blob/master/DocumentinAPI.csproj)
- `Aspose.Words` (docx, generation) — code_import — [code](https://github.com/giovanniuchoa/DocumentinAPI/blob/caa8b4ed785a8ce5cc2539c8343561d38d6f26fd/Domain/Utils/Helpers.cs)
- `Aspose.Words` (docx, generation) — code_import — [code](https://github.com/giovanniuchoa/DocumentinAPI/blob/caa8b4ed785a8ce5cc2539c8343561d38d6f26fd/Services/ImportService.cs)
- `Aspose.Words` (docx, generation) — code_import — [code](https://github.com/giovanniuchoa/DocumentinAPI/blob/caa8b4ed785a8ce5cc2539c8343561d38d6f26fd/Services/AsposeService.cs)

**Evidence trail**

- [api_response](https://github.com/giovanniuchoa/DocumentinAPI) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/giovanniuchoa/DocumentinAPI/blob/master/DocumentinAPI.csproj) (source: github_api): <PackageReference Include="Aspose.Words" Version="25.5.0" />
- [code_permalink](https://github.com/giovanniuchoa/DocumentinAPI/blob/caa8b4ed785a8ce5cc2539c8343561d38d6f26fd/Domain/Utils/Helpers.cs) (source: github_api): }             markdown = markdown.Replace($"**Evaluation Only. Created with Aspose.Words. Copyright 2003-2025 Aspose Pty Ltd.**", $"");             markdown = markdown.Replace($"**Created
- [code_permalink](https://github.com/giovanniuchoa/DocumentinAPI/blob/caa8b4ed785a8ce5cc2539c8343561d38d6f26fd/Services/ImportService.cs) (source: github_api): using var pdfStream = dto.File.OpenReadStream();                 var loadOptions = new Aspose.Words.Loading.LoadOptions { LoadFormat = Aspose.Words.LoadFormat.Pdf };
- [code_permalink](https://github.com/giovanniuchoa/DocumentinAPI/blob/caa8b4ed785a8ce5cc2539c8343561d38d6f26fd/Services/AsposeService.cs) (source: github_api): ﻿using Aspose.Words.Saving; using DocumentinAPI.Domain.DTOs.Supabase; using DocumentinAPI.Interfaces.IServices; using Microsoft.AspNetCore.Http; namespace DocumentinAPI.Services {
- [other](https://github.com/giovanniuchoa/DocumentinAPI/tree/master/Templates) (source: github_api): directory Templates/ present
- [readme_excerpt](https://github.com/giovanniuchoa/DocumentinAPI/blob/master/README.md) (source: readme): DocumentinAPI is a RESTful API developed in .NET 8.0 designed for comprehensive document management and workflow in business environments.

### 39. stella/stella

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

### 40. mahasv/xdocreport

**Repository / product**

- Repository: [https://github.com/mahasv/xdocreport](https://github.com/mahasv/xdocreport)
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

- Tier 3, `docx4j`, run `run_1`, window `size:501..1000`, rank 20
  - Query: `"docx4j" filename:pom.xml size:501..1000`
  - Retrieved 30 of 41 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docx4j` (docx, generation) — manifest_declaration — [converter/fr.opensagres.xdocreport.converter.docx.docx4j/pom.xml](https://github.com/mahasv/xdocreport/blob/2524e65c4eb26d205bd8f6f5c7525071de343023/converter/fr.opensagres.xdocreport.converter.docx.docx4j/pom.xml)
- `docx4j` (docx, generation) — code_import — [code](https://github.com/mahasv/xdocreport/blob/2524e65c4eb26d205bd8f6f5c7525071de343023/converter/fr.opensagres.xdocreport.converter.docx.docx4j/src/main/java/fr/opensagres/xdocreport/converter/docx/docx4j/pdf/Docx2PDFViaDocx4jConverter.java)
- `docx4j` (docx, generation) — code_import — [code](https://github.com/mahasv/xdocreport/blob/2524e65c4eb26d205bd8f6f5c7525071de343023/converter/fr.opensagres.xdocreport.converter.docx.docx4j/src/main/java/fr/opensagres/xdocreport/converter/docx/docx4j/xhtml/Docx2XHTMLViaDocx4jConverter.java)
- `docx4j` (docx, generation) — code_import — [code](https://github.com/mahasv/xdocreport/blob/2524e65c4eb26d205bd8f6f5c7525071de343023/converter/fr.opensagres.xdocreport.converter.docx.docx4j/src/main/java/fr/opensagres/xdocreport/converter/docx/docx4j/pdf/discovery/Docx2PDFViaDocx4jConverterDiscovery.java)

**Evidence trail**

- [api_response](https://github.com/mahasv/xdocreport) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/mahasv/xdocreport/blob/2524e65c4eb26d205bd8f6f5c7525071de343023/converter/fr.opensagres.xdocreport.converter.docx.docx4j/pom.xml) (source: github_api): </parent> <artifactId>fr.opensagres.xdocreport.converter.docx.docx4j</artifactId> <dependencies>
- [code_permalink](https://github.com/mahasv/xdocreport/blob/2524e65c4eb26d205bd8f6f5c7525071de343023/converter/fr.opensagres.xdocreport.converter.docx.docx4j/src/main/java/fr/opensagres/xdocreport/converter/docx/docx4j/pdf/Docx2PDFViaDocx4jConverter.java) (source: github_api): */ package fr.opensagres.xdocreport.converter.docx.docx4j.pdf;
- [code_permalink](https://github.com/mahasv/xdocreport/blob/2524e65c4eb26d205bd8f6f5c7525071de343023/converter/fr.opensagres.xdocreport.converter.docx.docx4j/src/main/java/fr/opensagres/xdocreport/converter/docx/docx4j/xhtml/Docx2XHTMLViaDocx4jConverter.java) (source: github_api): */ package fr.opensagres.xdocreport.converter.docx.docx4j.xhtml;
- [code_permalink](https://github.com/mahasv/xdocreport/blob/2524e65c4eb26d205bd8f6f5c7525071de343023/converter/fr.opensagres.xdocreport.converter.docx.docx4j/src/main/java/fr/opensagres/xdocreport/converter/docx/docx4j/pdf/discovery/Docx2PDFViaDocx4jConverterDiscovery.java) (source: github_api): */ package fr.opensagres.xdocreport.converter.docx.docx4j.pdf.discovery;
- [other](https://github.com/mahasv/xdocreport/tree/master/template) (source: github_api): directory template/ present

### 41. ceskaexpedice/kramerius

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

### 42. MagaluCloud/s3-specs

**Repository / product**

- Repository: [https://github.com/magalucloud/s3-specs](https://github.com/magalucloud/s3-specs)
- Company: Unknown — not stated in the repository
- Product: S3 Specs
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://magalucloud.github.io/s3-specs/

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

- Tier 3, `ReportLab`, run `run_1`, window `size:251..500`, rank 20
  - Query: `"reportlab" filename:pyproject.toml size:251..500`
  - Sampled 30 of 1,130 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,130 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `ReportLab` (pdf, generation) — code_import — [code](https://github.com/MagaluCloud/s3-specs/blob/2b22bd0cd4d9bb7aa212d3a9a8543a8f23c10622/reports/src/report.py)
- `ReportLab` (pdf, generation) — manifest_declaration — [reports/pyproject.toml](https://github.com/MagaluCloud/s3-specs/blob/2b22bd0cd4d9bb7aa212d3a9a8543a8f23c10622/reports/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/MagaluCloud/s3-specs) (source: github_api): stars=4, fork=False, archived=False
- [code_permalink](https://github.com/MagaluCloud/s3-specs/blob/2b22bd0cd4d9bb7aa212d3a9a8543a8f23c10622/reports/src/report.py) (source: github_api): from reportlab.lib.pagesizes import A4 from reportlab.lib import colors from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle from reportlab.platypus import SimpleDocTemplate, Paragraph
- [manifest_line](https://github.com/MagaluCloud/s3-specs/blob/2b22bd0cd4d9bb7aa212d3a9a8543a8f23c10622/reports/pyproject.toml) (source: github_api): "fastparquet>=2024.11.0",     "kaleido==0.2.0",     "matplotlib>=3.10.1",     "pandas>=2.2.3",     "plotly>=6.0.0",     "reportlab>=4.3.1", ]
- [other](https://github.com/MagaluCloud/s3-specs/tree/main/reports) (source: github_api): directory reports/ present

### 43. 864381832/xJavaFxTool

**Repository / product**

- Repository: [https://github.com/864381832/xjavafxtool](https://github.com/864381832/xjavafxtool)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://github.com/864381832/xJavaFxTool

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

- Tier 3, `Apache POI (XWPF/HWPF)`, run `run_1`, window `size:251..500`, rank 1
  - Query: `"poi" filename:build.gradle size:251..500`
  - Sampled 30 of 1,242 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,242 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Apache PDFBox`, run `run_1`, window `size:251..500`, rank 1
  - Query: `"pdfbox" filename:build.gradle size:251..500`
  - Retrieved 30 of 107 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache PDFBox` (pdf, generation) — manifest_declaration — [littleTools/x-PdfConvertTool/build.gradle](https://github.com/864381832/xJavaFxTool/blob/6625bd93ad60c6866bc0b583692f95f5df9320d8/littleTools/x-PdfConvertTool/build.gradle)
- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/864381832/xJavaFxTool/blob/6625bd93ad60c6866bc0b583692f95f5df9320d8/littleTools/x-PdfConvertTool/src/main/java/com/xwintop/xJavaFxTool/services/littleTools/PdfConvertToolService.java)
- `Apache POI (XWPF/HWPF)` (docx, generation) — code_import — [code](https://github.com/864381832/xJavaFxTool/blob/6625bd93ad60c6866bc0b583692f95f5df9320d8/games/x-SnakeJavaFx/src/main/java/com/xwintop/xJavaFxTool/controller/games/SnakeBody.java)
- `Apache POI (XWPF/HWPF)` (docx, generation) — manifest_declaration — [littleTools/x-FileMergeTool/build.gradle](https://github.com/864381832/xJavaFxTool/blob/6625bd93ad60c6866bc0b583692f95f5df9320d8/littleTools/x-FileMergeTool/build.gradle)

**Evidence trail**

- [api_response](https://github.com/864381832/xJavaFxTool) (source: github_api): stars=2236, fork=False, archived=False
- [manifest_line](https://github.com/864381832/xJavaFxTool/blob/6625bd93ad60c6866bc0b583692f95f5df9320d8/littleTools/x-PdfConvertTool/build.gradle) (source: github_api): dependencies {     api project(':xcore')     implementation 'org.apache.pdfbox:pdfbox:2.0.30' } group = 'com.xwintop' version = '0.0.4'
- [code_permalink](https://github.com/864381832/xJavaFxTool/blob/6625bd93ad60c6866bc0b583692f95f5df9320d8/littleTools/x-PdfConvertTool/src/main/java/com/xwintop/xJavaFxTool/services/littleTools/PdfConvertToolService.java) (source: github_api): import lombok.extern.slf4j.Slf4j; import org.apache.commons.io.FilenameUtils; import org.apache.commons.lang3.StringUtils; import org.apache.pdfbox.pdmodel.PDDocument; import org.apache.pdfbox.renderi
- [code_permalink](https://github.com/864381832/xJavaFxTool/blob/6625bd93ad60c6866bc0b583692f95f5df9320d8/games/x-SnakeJavaFx/src/main/java/com/xwintop/xJavaFxTool/controller/games/SnakeBody.java) (source: github_api): \|\| firstPoi.getY() + getHeight() <= getY() \|\| firstPoi.getY() - getHeight() >= getY()) { Point poi = new Point(); poi.setX(getX());
- [manifest_line](https://github.com/864381832/xJavaFxTool/blob/6625bd93ad60c6866bc0b583692f95f5df9320d8/littleTools/x-FileMergeTool/build.gradle) (source: github_api): dependencies {     api project(':xcore')     implementation 'org.apache.poi:poi-ooxml:5.2.5'     implementation 'org.apache.commons:commons-csv:1.10.0' } group = 'com.xwintop'

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

### 47. SK-CERT/Taranis-NG

**Repository / product**

- Repository: [https://github.com/sk-cert/taranis-ng](https://github.com/sk-cert/taranis-ng)
- Company: NCSC-NL
- Product: Taranis NG
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: industry_category=unknown; contributor_count not collected

**Score**

- Score: 29/100 (a score, not a probability)
- Raw weighted score: 1.45 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_1`, window `size:501..1000`, rank 10
  - Query: `"weasyprint" filename:pyproject.toml size:501..1000`
  - Retrieved 30 of 976 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [src/presenters/pyproject.toml](https://github.com/SK-CERT/Taranis-NG/blob/6d1070af490c556d0f4be70e39d4e79a4ac99072/src/presenters/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/SK-CERT/Taranis-NG/blob/6d1070af490c556d0f4be70e39d4e79a4ac99072/src/presenters/presenters/base_presenter.py)

**Evidence trail**

- [api_response](https://github.com/SK-CERT/Taranis-NG) (source: github_api): stars=127, fork=False, archived=False
- [readme_excerpt](https://github.com/SK-CERT/Taranis-NG/blob/main/README.md) (source: readme): company stated as 'NCSC-NL. Currently'
- [manifest_line](https://github.com/SK-CERT/Taranis-NG/blob/6d1070af490c556d0f4be70e39d4e79a4ac99072/src/presenters/pyproject.toml) (source: github_api): "Jinja2==3.1.6",     "marshmallow==4.3.1",     "python-dotenv==1.2.2",     "weasyprint==69.0",     "taranis-ng-shared==26.05.1", ]
- [code_permalink](https://github.com/SK-CERT/Taranis-NG/blob/6d1070af490c556d0f4be70e39d4e79a4ac99072/src/presenters/presenters/base_presenter.py) (source: github_api): from shared.common import TZ from shared.log_manager import logger from shared.schema.presenter import PresenterSchema from weasyprint import HTML from . import jinja_filters

### 48. ngs-doo/TemplaterExamples

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

### 49. cool-dev-guy/rabbitthunder

**Repository / product**

- Repository: [https://github.com/cool-dev-guy/rabbitthunder](https://github.com/cool-dev-guy/rabbitthunder)
- Company: Unknown — not stated in the repository
- Product: rabbitthunder
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

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
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 2 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_1`, window `size:501..1000`, rank 20
  - Query: `"puppeteer" filename:package.json size:501..1000`
  - Sampled 30 of 40,704 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 40,704 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/cool-dev-guy/rabbitthunder/blob/main/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/cool-dev-guy/rabbitthunder/blob/50dc7abe09842dca2e03064ba686363d54b14e28/api/upcloud.ts)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/cool-dev-guy/rabbitthunder/blob/50dc7abe09842dca2e03064ba686363d54b14e28/api/vidcloud.ts)

**Evidence trail**

- [api_response](https://github.com/cool-dev-guy/rabbitthunder) (source: github_api): stars=19, fork=False, archived=False
- [manifest_line](https://github.com/cool-dev-guy/rabbitthunder/blob/main/package.json) (source: github_api): "description": "A rabbit stream extractor based on puppeteer by cool-dev-guy.",
- [code_permalink](https://github.com/cool-dev-guy/rabbitthunder/blob/50dc7abe09842dca2e03064ba686363d54b14e28/api/upcloud.ts) (source: github_api): // Stealth plugin issue - There is a good fix but currently this works. require('puppeteer-extra-plugin-user-data-dir') require('puppeteer-extra-plugin-user-preferences')
- [code_permalink](https://github.com/cool-dev-guy/rabbitthunder/blob/50dc7abe09842dca2e03064ba686363d54b14e28/api/vidcloud.ts) (source: github_api): // Stealth plugin issue - There is a good fix but currently this works. require('puppeteer-extra-plugin-user-data-dir') require('puppeteer-extra-plugin-user-preferences')
- [readme_excerpt](https://github.com/cool-dev-guy/rabbitthunder/blob/main/README.md) (source: readme): `Note 2` : The devoloper of the project (cool-dev-guy) is never responsible for anything caused by this project.So use this at your own risk.

### 50. PipedreamHQ/pipedream

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

### 51. simpledms/simpledms

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

### 52. tringert/PdfSignabilityCheckerTool

**Repository / product**

- Repository: [https://github.com/tringert/pdfsignabilitycheckertool](https://github.com/tringert/pdfsignabilitycheckertool)
- Company: Unknown — not stated in the repository
- Product: PdfSignabilityCheckerTool
- Industry: healthcare_diagnostics (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
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

- Tier 3, `iText`, run `run_1`, window `size:251..500`, rank 22
  - Query: `"itext" extension:csproj size:251..500`
  - Retrieved 30 of 732 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `iText` (pdf, generation) — manifest_declaration — [PdfSignabilityCheckerTool.csproj](https://github.com/tringert/PdfSignabilityCheckerTool/blob/main/PdfSignabilityCheckerTool.csproj)
- `iText` (pdf, generation) — code_import — [code](https://github.com/tringert/PdfSignabilityCheckerTool/blob/0ab88065c9f4db0503d6aee6862d58d72d9e7161/Program.cs)
- `iText` (pdf, generation) — code_import — [code](https://github.com/tringert/PdfSignabilityCheckerTool/blob/0ab88065c9f4db0503d6aee6862d58d72d9e7161/PdfReaderWrapper.cs)
- `iText` (pdf, generation) — code_import — [code](https://github.com/tringert/PdfSignabilityCheckerTool/blob/0ab88065c9f4db0503d6aee6862d58d72d9e7161/PdfSignatureField.cs)
- `iText` (pdf, generation) — code_import — [code](https://github.com/tringert/PdfSignabilityCheckerTool/blob/0ab88065c9f4db0503d6aee6862d58d72d9e7161/SignatureExtractor.cs)

**Evidence trail**

- [api_response](https://github.com/tringert/PdfSignabilityCheckerTool) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/tringert/PdfSignabilityCheckerTool/blob/main/PdfSignabilityCheckerTool.csproj) (source: github_api): <PackageReference Include="itext" Version="9.4.0" />
- [code_permalink](https://github.com/tringert/PdfSignabilityCheckerTool/blob/0ab88065c9f4db0503d6aee6862d58d72d9e7161/Program.cs) (source: github_api): ﻿using System.Diagnostics; using iText.Kernel.Exceptions; namespace PdfSignabilityCheckerTool; internal static class Program {
- [code_permalink](https://github.com/tringert/PdfSignabilityCheckerTool/blob/0ab88065c9f4db0503d6aee6862d58d72d9e7161/PdfReaderWrapper.cs) (source: github_api): ﻿using iText.Kernel.Pdf; namespace PdfSignabilityCheckerTool; internal class PdfReaderWrapper {     private readonly MemoryStream _ms;
- [code_permalink](https://github.com/tringert/PdfSignabilityCheckerTool/blob/0ab88065c9f4db0503d6aee6862d58d72d9e7161/PdfSignatureField.cs) (source: github_api): ﻿using iText.Kernel.Pdf; using PdfSignabilityCheckerTool.Enums; namespace PdfSignabilityCheckerTool; internal class PdfSignatureField(PdfDictionary dict) {
- [code_permalink](https://github.com/tringert/PdfSignabilityCheckerTool/blob/0ab88065c9f4db0503d6aee6862d58d72d9e7161/SignatureExtractor.cs) (source: github_api): ﻿using iText.Forms; using iText.Forms.Fields; using iText.Kernel.Pdf; using iText.Kernel.Pdf.Annot; using iText.Signatures; namespace PdfSignabilityCheckerTool;
- [readme_excerpt](https://github.com/tringert/PdfSignabilityCheckerTool/blob/main/README.md) (source: readme): It performs the same signability checks used by DSS (Digital Signature Service), including permission checks and handling of encrypted PDFs when possible.

### 53. nayetdet/softworker

**Repository / product**

- Repository: [https://github.com/nayetdet/softworker](https://github.com/nayetdet/softworker)
- Company: Unknown — not stated in the repository
- Product: SoftWorker
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://softworker.vercel.app

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 27/100 (a score, not a probability)
- Raw weighted score: 1.35 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_1`, window `size:501..1000`, rank 30
  - Query: `"weasyprint" filename:pyproject.toml size:501..1000`
  - Retrieved 30 of 976 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/nayetdet/softworker/blob/main/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/nayetdet/softworker/blob/92659831ecff3e30110af6a85a4ebe081cec4ce2/src/softworker/core/render.py)

**Evidence trail**

- [api_response](https://github.com/nayetdet/softworker) (source: github_api): stars=19, fork=False, archived=False
- [manifest_line](https://github.com/nayetdet/softworker/blob/main/pyproject.toml) (source: github_api): "weasyprint>=68.1",
- [code_permalink](https://github.com/nayetdet/softworker/blob/92659831ecff3e30110af6a85a4ebe081cec4ce2/src/softworker/core/render.py) (source: github_api): from typing import Dict, Any from weasyprint import HTML, CSS from softworker.enums import ResumeLanguage from softworker.core.template import render_template from softworker.core.template_context imp
- [other](https://github.com/nayetdet/softworker/tree/main/template) (source: github_api): directory template/ present

### 54. Oxylo/btreport

**Repository / product**

- Repository: [https://github.com/oxylo/btreport](https://github.com/oxylo/btreport)
- Company: Unknown — not stated in the repository
- Product: Objective
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 27/100 (a score, not a probability)
- Raw weighted score: 1.35 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 1 |
| Business criticality | 1 |
| Pipeline complexity | 2 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_1`, window `size:0..250`, rank 13
  - Query: `"weasyprint" filename:requirements.txt size:0..250`
  - Sampled 30 of 3,832 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,832 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements.txt](https://github.com/Oxylo/btreport/blob/master/requirements.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/Oxylo/btreport/blob/133d632856dd93d6012147f5481420e91956296c/report.py)

**Evidence trail**

- [api_response](https://github.com/Oxylo/btreport) (source: github_api): stars=71, fork=False, archived=False
- [manifest_line](https://github.com/Oxylo/btreport/blob/master/requirements.txt) (source: github_api): weasyprint==0.42.3
- [code_permalink](https://github.com/Oxylo/btreport/blob/133d632856dd93d6012147f5481420e91956296c/report.py) (source: github_api): import os import pandas as pd from jinja2 import Environment, FileSystemLoader from weasyprint import HTML from utils import timestamp2str, get_now, dir_exists
- [other](https://github.com/Oxylo/btreport/tree/master/templates) (source: github_api): directory templates/ present

### 55. Azure/gpt-rag-ingestion

**Repository / product**

- Repository: [https://github.com/azure/gpt-rag-ingestion](https://github.com/azure/gpt-rag-ingestion)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
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

- Tier 3, `PyMuPDF (fitz)`, run `run_1`, window `size:1001..2000`, rank 14
  - Query: `"PyMuPDF" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 6,128 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 6,128 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [requirements.txt](https://github.com/Azure/gpt-rag-ingestion/blob/main/requirements.txt)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/Azure/gpt-rag-ingestion/blob/84b927769ef0839110f2d68e3ca471e2260567cf/tools/figure_extraction.py)

**Evidence trail**

- [api_response](https://github.com/Azure/gpt-rag-ingestion) (source: github_api): stars=187, fork=False, archived=False
- [manifest_line](https://github.com/Azure/gpt-rag-ingestion/blob/main/requirements.txt) (source: github_api): PyMuPDF==1.27.2.3
- [code_permalink](https://github.com/Azure/gpt-rag-ingestion/blob/84b927769ef0839110f2d68e3ca471e2260567cf/tools/figure_extraction.py) (source: github_api): """Extract a figure region from a PDF page."""     import fitz  # PyMuPDF     from PIL import Image
- [readme_excerpt](https://github.com/Azure/gpt-rag-ingestion/blob/main/README.md) (source: readme): Grant the ingestion service managed identity **Search Index Data Reader** on the configured Search service for query access.

### 56. iondv/registry

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

### 57. bashly-framework/bashly

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

### 58. liferay/liferay-portal

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

### 59. kaiser6989/Team-6989-Rebuilt-Technical-Binder

**Repository / product**

- Repository: [https://github.com/kaiser6989/team-6989-rebuilt-technical-binder](https://github.com/kaiser6989/team-6989-rebuilt-technical-binder)
- Company: Unknown — not stated in the repository
- Product: Team 6989 Rebuilt Technical Binder
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://team-6989-rebuilt-technical-binder.vercel.app/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| supporting: pipeline_stage_count=2; template_directory_present=true; confirmed generation/conversion code \| unknown: contributor_count not collected

**Score**

- Score: 25/100 (a score, not a probability)
- Raw weighted score: 1.80 / 5
- Confidence: medium
- Gate cap applied: **25** — the weighted calculation produced a higher number, but a qualification-gate condition capped it (SCORING_MODEL.md section 14)

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 3 |
| Document complexity | 1 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden | 2 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 4 |

**Evidence coverage**

Evidence coverage: 7/7 dimensions

- No unknown dimensions; all seven were directly evidenced.

**Discovery provenance**

- Tier 3, `pdf-lib`, run `run_1`, window `size:501..1000`, rank 27
  - Query: `"pdf-lib" filename:package.json size:501..1000`
  - Sampled 30 of 9,312 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 9,312 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `pdf-lib` (pdf, generation) — manifest_declaration — [package-lock.json](https://github.com/kaiser6989/Team-6989-Rebuilt-Technical-Binder/blob/main/package-lock.json)
- `pdf-lib` (pdf, generation) — manifest_declaration — [package.json](https://github.com/kaiser6989/Team-6989-Rebuilt-Technical-Binder/blob/main/package.json)
- `pdf-lib` (pdf, generation) — code_import — [code](https://github.com/kaiser6989/Team-6989-Rebuilt-Technical-Binder/blob/f9fecc95e8f63f9cc3ba815e85df17e1fe6bec9b/scripts/book.js)

**Evidence trail**

- [api_response](https://github.com/kaiser6989/Team-6989-Rebuilt-Technical-Binder) (source: github_api): stars=2, fork=False, archived=False
- [readme_excerpt](https://github.com/kaiser6989/Team-6989-Rebuilt-Technical-Binder/blob/main/README.md) (source: readme): company stated as 'Team'
- [manifest_line](https://github.com/kaiser6989/Team-6989-Rebuilt-Technical-Binder/blob/main/package-lock.json) (source: github_api): "pdf-lib": "^1.17.1",
- [manifest_line](https://github.com/kaiser6989/Team-6989-Rebuilt-Technical-Binder/blob/main/package.json) (source: github_api): "pdf-lib": "^1.17.1",
- [code_permalink](https://github.com/kaiser6989/Team-6989-Rebuilt-Technical-Binder/blob/f9fecc95e8f63f9cc3ba815e85df17e1fe6bec9b/scripts/book.js) (source: github_api): import { readFile } from "fs/promises"; import { lookup } from "mime-types"; import puppeteer from "puppeteer"; import { PDFDocument } from "pdf-lib"; const __dirname = dirname(fileURLToPath(import.m
- [other](https://github.com/kaiser6989/Team-6989-Rebuilt-Technical-Binder/tree/main/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/kaiser6989/Team-6989-Rebuilt-Technical-Binder/blob/main/README.md) (source: readme): We extend our gratitude to the original developer and the community members on ChiefDelphi who made this open-source tool available for teams to share their technical documentation effectively.

### 60. jreyesr/n8n-nodes-carbonejs

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

### 61. sschuberth/stan

**Repository / product**

- Repository: [https://github.com/sschuberth/stan](https://github.com/sschuberth/stan)
- Company: Unknown — not stated in the repository
- Product: Stan - The *St*atement *An*alyzer
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 24/100 (a score, not a probability)
- Raw weighted score: 1.20 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `Apache PDFBox`, run `run_1`, window `size:0..250`, rank 11
  - Query: `"pdfbox" filename:build.gradle size:0..250`
  - Retrieved 30 of 44 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.
- Tier 3, `iText`, run `run_1`, window `size:0..250`, rank 10
  - Query: `"itext" filename:build.gradle size:0..250`
  - Retrieved 30 of 40 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Apache PDFBox` (pdf, generation) — code_import — [code](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/postbank-db-pdf/src/main/kotlin/PostbankDbPdfParser.kt)
- `Apache PDFBox` (pdf, generation) — manifest_declaration — [plugins/parsers/postbank-db-pdf/build.gradle.kts](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/postbank-db-pdf/build.gradle.kts)
- `iText` (pdf, generation) — code_import — [code](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/psd-bank-pdf/src/main/kotlin/PsdBankPdfParser.kt)
- `iText` (pdf, generation) — code_import — [code](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/postbank-pdf/src/main/kotlin/PostbankPdfParser.kt)
- `iText` (pdf, generation) — code_import — [code](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/ing-pdf/src/main/kotlin/IngPdfParser.kt)
- `iText` (pdf, generation) — manifest_declaration — [plugins/parsers/ing-pdf/build.gradle.kts](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/ing-pdf/build.gradle.kts)

**Evidence trail**

- [api_response](https://github.com/sschuberth/stan) (source: github_api): stars=22, fork=False, archived=False
- [code_permalink](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/postbank-db-pdf/src/main/kotlin/PostbankDbPdfParser.kt) (source: github_api): import java.time.format.DateTimeFormatter import java.util.Locale import org.apache.pdfbox.Loader import org.apache.pdfbox.cos.COSDictionary import org.apache.pdfbox.cos.COSName import org.apache.pdf
- [manifest_line](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/postbank-db-pdf/build.gradle.kts) (source: github_api): } dependencies {     api(projects.lib)     implementation(libs.pdfbox) }
- [code_permalink](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/psd-bank-pdf/src/main/kotlin/PsdBankPdfParser.kt) (source: github_api): private val applicableProducers = setOf(         "Compart MFFPDF I/O Filter",         "iText 2.1.5 (by lowagie.com)",         "iText 2.1.7 by 1T3XT"     )
- [code_permalink](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/postbank-pdf/src/main/kotlin/PostbankPdfParser.kt) (source: github_api): "StreamServe Communication Server 5.6.2 GA Build 1210 (64 bit)",         "StreamServe Communication Server 5.6.2 INTERNAL Build 0 (64 bit)",         "XEP 4.19 build 20110414",         "iText 1
- [code_permalink](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/ing-pdf/src/main/kotlin/IngPdfParser.kt) (source: github_api): package dev.schuberth.stan.plugins.parsers.ing import com.itextpdf.text.pdf.PdfReader import com.itextpdf.text.pdf.parser.PdfTextExtractor import dev.schuberth.stan.Parser import dev.schuberth.stan.
- [manifest_line](https://github.com/sschuberth/stan/blob/0dd8be4078592c787f26767f2e257cce6a715eb3/plugins/parsers/ing-pdf/build.gradle.kts) (source: github_api): dependencies {     api(projects.lib)     implementation(libs.itextpdf)     funTestImplementation(testFixtures(projects.lib)) }
- [readme_excerpt](https://github.com/sschuberth/stan/blob/main/README.md) (source: readme): [SUPA](https://www.subsembly.com/download/SUPA.pdf) Subsembly's SUPA format is used by the [Banking4](https://banking4.de/) application.

### 62. GRAVITAD-SL/pizquito-backend-strapi

**Repository / product**

- Repository: [https://github.com/gravitad-sl/pizquito-backend-strapi](https://github.com/gravitad-sl/pizquito-backend-strapi)
- Company: Unknown — not stated in the repository
- Product: 🚀 Getting started with Strapi
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 24/100 (a score, not a probability)
- Raw weighted score: 1.20 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `PDFKit`, run `run_1`, window `size:1001..2000`, rank 26
  - Query: `"pdfkit" filename:package.json size:1001..2000`
  - Sampled 30 of 14,912 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 14,912 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `PDFKit` (pdf, generation) — manifest_declaration — [package-lock.json](https://github.com/GRAVITAD-SL/pizquito-backend-strapi/blob/main/package-lock.json)
- `PDFKit` (pdf, generation) — manifest_declaration — [package.json](https://github.com/GRAVITAD-SL/pizquito-backend-strapi/blob/main/package.json)
- `PDFKit` (pdf, generation) — code_import — [code](https://github.com/GRAVITAD-SL/pizquito-backend-strapi/blob/3d39b0e128aa10a68ef49e366a9cb8998fada50c/src/api/reports/services/pdf/pdf-generator.ts)

**Evidence trail**

- [api_response](https://github.com/GRAVITAD-SL/pizquito-backend-strapi) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/GRAVITAD-SL/pizquito-backend-strapi/blob/main/package-lock.json) (source: github_api): "pdfkit": "^0.17.2",
- [manifest_line](https://github.com/GRAVITAD-SL/pizquito-backend-strapi/blob/main/package.json) (source: github_api): "pdfkit": "^0.17.2",
- [code_permalink](https://github.com/GRAVITAD-SL/pizquito-backend-strapi/blob/3d39b0e128aa10a68ef49e366a9cb8998fada50c/src/api/reports/services/pdf/pdf-generator.ts) (source: github_api): * PDF Generator for Invoices (matrículas) and Payrolls (nóminas)  */ import PDFDocument from "pdfkit"; import * as fs from "fs"; import * as path from "path"; import * as os from "os";
- [readme_excerpt](https://github.com/GRAVITAD-SL/pizquito-backend-strapi/blob/main/README.md) (source: readme): Strapi comes with a full featured [Command Line Interface](https://docs.strapi.io/dev-docs/cli) (CLI) which lets you scaffold and manage your project in seconds.

### 63. I-CAN-hack/pdf-mcp

**Repository / product**

- Repository: [https://github.com/i-can-hack/pdf-mcp](https://github.com/i-can-hack/pdf-mcp)
- Company: Unknown — not stated in the repository
- Product: pdf-mcp
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 24/100 (a score, not a probability)
- Raw weighted score: 1.20 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `PyMuPDF (fitz)`, run `run_1`, window `size:251..500`, rank 8
  - Query: `"PyMuPDF" filename:pyproject.toml size:251..500`
  - Sampled 30 of 2,508 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,508 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [pyproject.toml](https://github.com/I-CAN-hack/pdf-mcp/blob/main/pyproject.toml)
- `PyMuPDF (fitz)` (pdf, mixed) — code_import — [code](https://github.com/I-CAN-hack/pdf-mcp/blob/c430ba664d82b06140f24358310dbf7016b532a1/src/pdf_mcp/server.py)

**Evidence trail**

- [api_response](https://github.com/I-CAN-hack/pdf-mcp) (source: github_api): stars=75, fork=False, archived=False
- [manifest_line](https://github.com/I-CAN-hack/pdf-mcp/blob/main/pyproject.toml) (source: github_api): "pymupdf>=1.27.2,<2",
- [code_permalink](https://github.com/I-CAN-hack/pdf-mcp/blob/c430ba664d82b06140f24358310dbf7016b532a1/src/pdf_mcp/server.py) (source: github_api): import tempfile from typing import Literal import fitz  # PyMuPDF import pymupdf4llm from mcp.server.fastmcp import FastMCP, Image
- [readme_excerpt](https://github.com/I-CAN-hack/pdf-mcp/blob/main/README.md) (source: readme): Designed for use with LLMs that need to read datasheets and other PDFs containing diagrams, tables, and technical content.

### 64. radic82/docx4jUtil

**Repository / product**

- Repository: [https://github.com/radic82/docx4jutil](https://github.com/radic82/docx4jutil)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **keep**
- Confidence: medium
- Reason: readme_describes_product=true, application_code_exists=true, is_fork=false, document_functionality_in_production_code=true, code_usage_confirmed=true, category_count=1, pipeline_stage_count=1 \| supporting: confirmed generation/conversion code

**Score**

- Score: 24/100 (a score, not a probability)
- Raw weighted score: 1.20 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 2 |
| Pipeline complexity | 1 |
| Maintenance burden | 1 |
| Build-vs-buy signal | 3 |
| Commercial leverage *(unknown)* | 0 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Commercial leverage: Unknown

**Discovery provenance**

- Tier 3, `docx4j`, run `run_1`, window `size:501..1000`, rank 21
  - Query: `"docx4j" filename:pom.xml size:501..1000`
  - Retrieved 30 of 41 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docx4j` (docx, generation) — manifest_declaration — [pom.xml](https://github.com/radic82/docx4jUtil/blob/master/pom.xml)
- `docx4j` (docx, generation) — code_import — [code](https://github.com/radic82/docx4jUtil/blob/56b6633333f986acfb7b8da284e3910c67270105/src/main/java/it/docx4j/item/DocImg.java)
- `docx4j` (docx, generation) — code_import — [code](https://github.com/radic82/docx4jUtil/blob/56b6633333f986acfb7b8da284e3910c67270105/src/main/java/it/docx4j/item/DocRow.java)
- `docx4j` (docx, generation) — code_import — [code](https://github.com/radic82/docx4jUtil/blob/56b6633333f986acfb7b8da284e3910c67270105/src/main/java/it/docx4j/item/DocLink.java)
- `docx4j` (docx, generation) — code_import — [code](https://github.com/radic82/docx4jUtil/blob/56b6633333f986acfb7b8da284e3910c67270105/src/main/java/it/docx4j/item/DocText.java)
- `docx4j` (docx, generation) — code_import — [code](https://github.com/radic82/docx4jUtil/blob/56b6633333f986acfb7b8da284e3910c67270105/src/main/java/it/docx4j/item/DocItem.java)

**Evidence trail**

- [api_response](https://github.com/radic82/docx4jUtil) (source: github_api): stars=5, fork=False, archived=False
- [manifest_line](https://github.com/radic82/docx4jUtil/blob/master/pom.xml) (source: github_api): <artifactId>docx4jUtil</artifactId>
- [code_permalink](https://github.com/radic82/docx4jUtil/blob/56b6633333f986acfb7b8da284e3910c67270105/src/main/java/it/docx4j/item/DocImg.java) (source: github_api): package it.docx4j.item; import it.docx4j.style.IDocxObjectStyle; /**  * Class to manage image  */
- [code_permalink](https://github.com/radic82/docx4jUtil/blob/56b6633333f986acfb7b8da284e3910c67270105/src/main/java/it/docx4j/item/DocRow.java) (source: github_api): package it.docx4j.item;
- [code_permalink](https://github.com/radic82/docx4jUtil/blob/56b6633333f986acfb7b8da284e3910c67270105/src/main/java/it/docx4j/item/DocLink.java) (source: github_api): package it.docx4j.item; import it.docx4j.style.custom.DocxStyleEnum; /**  * Class to manage link  */
- [code_permalink](https://github.com/radic82/docx4jUtil/blob/56b6633333f986acfb7b8da284e3910c67270105/src/main/java/it/docx4j/item/DocText.java) (source: github_api): package it.docx4j.item;
- [code_permalink](https://github.com/radic82/docx4jUtil/blob/56b6633333f986acfb7b8da284e3910c67270105/src/main/java/it/docx4j/item/DocItem.java) (source: github_api): package it.docx4j.item; import it.docx4j.style.IDocxObjectStyle; import java.io.Serializable; /**
- [readme_excerpt](https://github.com/radic82/docx4jUtil/blob/master/readme.md) (source: readme): [Here you can find Class Diagram](ClassDiagram.png) This Lib (classes) helps you to create docx document.

### 65. freelawproject/recap-chrome

**Repository / product**

- Repository: [https://github.com/freelawproject/recap-chrome](https://github.com/freelawproject/recap-chrome)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://free.law/recap/

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

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_1`, window `size:1001..2000`, rank 14
  - Query: `"puppeteer" filename:package.json size:1001..2000`
  - Sampled 30 of 38,336 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 38,336 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package-lock.json](https://github.com/freelawproject/recap-chrome/blob/main/package-lock.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/freelawproject/recap-chrome/blob/main/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/freelawproject/recap-chrome/blob/ec6dde75b4f43cb4c9d4c86328b0f5069866f7b4/karma.conf.js)

**Evidence trail**

- [api_response](https://github.com/freelawproject/recap-chrome) (source: github_api): stars=79, fork=False, archived=False
- [manifest_line](https://github.com/freelawproject/recap-chrome/blob/main/package-lock.json) (source: github_api): "puppeteer": "^19.6.2",
- [manifest_line](https://github.com/freelawproject/recap-chrome/blob/main/package.json) (source: github_api): "puppeteer": "^19.6.2",
- [code_permalink](https://github.com/freelawproject/recap-chrome/blob/ec6dde75b4f43cb4c9d4c86328b0f5069866f7b4/karma.conf.js) (source: github_api): // Karma configuration // Generated on Wed Jan 03 2018 21:51:16 GMT-0800 (PST) process.env.CHROME_BIN = require("puppeteer").executablePath(); module.exports = function(config) {   config.set({

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

### 70. JaocHatter/ReportGenerator-Landmarks

**Repository / product**

- Repository: [https://github.com/jaochatter/reportgenerator-landmarks](https://github.com/jaochatter/reportgenerator-landmarks)
- Company: Unknown — not stated in the repository
- Product: ReportGenerator-Landmarks (Beta)
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:0..250`, rank 26
  - Query: `"weasyprint" filename:requirements.txt size:0..250`
  - Sampled 30 of 3,832 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,832 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/JaocHatter/ReportGenerator-Landmarks/blob/39515831d73c8ca3f817e3af0170adcda91d9a3b/src/agents/report_generator.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/JaocHatter/ReportGenerator-Landmarks/blob/39515831d73c8ca3f817e3af0170adcda91d9a3b/manual_report/app/report_generator.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/JaocHatter/ReportGenerator-Landmarks/blob/39515831d73c8ca3f817e3af0170adcda91d9a3b/src/utils/test_report_generator.py)

**Evidence trail**

- [api_response](https://github.com/JaocHatter/ReportGenerator-Landmarks) (source: github_api): stars=2, fork=False, archived=False
- [code_permalink](https://github.com/JaocHatter/ReportGenerator-Landmarks/blob/39515831d73c8ca3f817e3af0170adcda91d9a3b/src/agents/report_generator.py) (source: github_api): from typing import List, Optional, Dict import markdown2 from weasyprint import HTML, CSS from states import (     IdentifiedLandmarksBatchState, ConfirmedLandmarkState, RobotPose
- [code_permalink](https://github.com/JaocHatter/ReportGenerator-Landmarks/blob/39515831d73c8ca3f817e3af0170adcda91d9a3b/manual_report/app/report_generator.py) (source: github_api): import os from typing import List, Dict, Any import markdown2 from weasyprint import HTML, CSS import base64 import mimetypes import json
- [code_permalink](https://github.com/JaocHatter/ReportGenerator-Landmarks/blob/39515831d73c8ca3f817e3af0170adcda91d9a3b/src/utils/test_report_generator.py) (source: github_api): # --- Library Imports --- import markdown2 from weasyprint import HTML, CSS import matplotlib matplotlib.use('Agg')  # To prevent GUI issues on servers import matplotlib.pyplot as plt

### 71. dfir-iris/docx-generator

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

### 72. TheOnlyWayUp/WattpadDownloader

**Repository / product**

- Repository: [https://github.com/theonlywayup/wattpaddownloader](https://github.com/theonlywayup/wattpaddownloader)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://wpd.my

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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:501..1000`, rank 8
  - Query: `"weasyprint" filename:pyproject.toml size:501..1000`
  - Retrieved 30 of 976 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/TheOnlyWayUp/WattpadDownloader/blob/697590c1ce675d851686fc085663cd156050ca23/src/api/src/create_book/generators/pdf.py)
- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [src/api/pyproject.toml](https://github.com/TheOnlyWayUp/WattpadDownloader/blob/697590c1ce675d851686fc085663cd156050ca23/src/api/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/TheOnlyWayUp/WattpadDownloader) (source: github_api): stars=314, fork=False, archived=False
- [code_permalink](https://github.com/TheOnlyWayUp/WattpadDownloader/blob/697590c1ce675d851686fc085663cd156050ca23/src/api/src/create_book/generators/pdf.py) (source: github_api): from bs4 import BeautifulSoup from jinja2 import Template from weasyprint import CSS, HTML, Document from weasyprint.text.fonts import FontConfiguration from ..models import Story from .types import
- [manifest_line](https://github.com/TheOnlyWayUp/WattpadDownloader/blob/697590c1ce675d851686fc085663cd156050ca23/src/api/pyproject.toml) (source: github_api): "aiohttp-client-cache[all]",     "bs4>=0.0.2",     "uvicorn>=0.32.1",     "weasyprint>=63.0",     "jinja2>=3.1.6", ]

### 73. zhangzhen1979/JIMU-ConvertPreview

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

### 74. mila-iqia/COVI-AgentSim

**Repository / product**

- Repository: [https://github.com/mila-iqia/covi-agentsim](https://github.com/mila-iqia/covi-agentsim)
- Company: Unknown — not stated in the repository
- Product: COVI-AgentSim: A testbed for comparing contact tracing apps
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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:251..500`, rank 14
  - Query: `"weasyprint" filename:requirements.txt size:251..500`
  - Sampled 30 of 2,632 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,632 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements.txt](https://github.com/mila-iqia/COVI-AgentSim/blob/master/requirements.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/mila-iqia/COVI-AgentSim/blob/7e4dea42ad9c5dd251aa8d7546c647ad4f173d28/src/covid19sim/plotting/plot_infection_chains.py)

**Evidence trail**

- [api_response](https://github.com/mila-iqia/COVI-AgentSim) (source: github_api): stars=19, fork=False, archived=False
- [manifest_line](https://github.com/mila-iqia/COVI-AgentSim/blob/master/requirements.txt) (source: github_api): weasyprint
- [code_permalink](https://github.com/mila-iqia/COVI-AgentSim/blob/7e4dea42ad9c5dd251aa8d7546c647ad4f173d28/src/covid19sim/plotting/plot_infection_chains.py) (source: github_api): import random import weasyprint from PIL import Image

### 75. g3w-suite/g3w-admin

**Repository / product**

- Repository: [https://github.com/g3w-suite/g3w-admin](https://github.com/g3w-suite/g3w-admin)
- Company: Unknown — not stated in the repository
- Product: G3W-ADMIN
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://g3w-suite.readthedocs.io/en/latest/g3wsuite_administration.html

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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:1001..2000`, rank 10
  - Query: `"weasyprint" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 2,532 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,532 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements.txt](https://github.com/g3w-suite/g3w-admin/blob/dev/requirements.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/g3w-suite/g3w-admin/blob/ca821a1fa4dc8d98442bf66d06938299f7d92dc4/g3w-admin/core/api/views.py)

**Evidence trail**

- [api_response](https://github.com/g3w-suite/g3w-admin) (source: github_api): stars=47, fork=False, archived=False
- [manifest_line](https://github.com/g3w-suite/g3w-admin/blob/dev/requirements.txt) (source: github_api): weasyprint==68.0
- [code_permalink](https://github.com/g3w-suite/g3w-admin/blob/ca821a1fa4dc8d98442bf66d06938299f7d92dc4/g3w-admin/core/api/views.py) (source: github_api): from rest_framework import status from rest_framework.response import Response from owslib.wms import WebMapService from weasyprint import HTML as WeasyHTML from qgis.core import NULL, Qgis, QgsCoordi

### 76. javadev/jasper-xml-to-pdf-generator

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

### 77. xcmt/ABC_report

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

### 78. qwc-services/jasper-reporting-service

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

### 79. wso2/carbon-commons

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

### 80. Azure-Samples/healthcare-agent-orchestrator

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

### 81. AIGeniusInstitue/restfeel

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

### 82. zorazrw/odex

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

### 83. lincolnluiz/SpringBoot-JasperReports

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

### 84. gooderp-study/GoodERP

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

### 85. davidkey/DynamicJasperExample

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

### 86. zkoss/zk

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

### 87. Lawyer-ray/FachuanHybridSystem

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

### 88. DFE-Digital/funding-service-myesf-docex-ui

**Repository / product**

- Repository: [https://github.com/dfe-digital/funding-service-myesf-docex-ui](https://github.com/dfe-digital/funding-service-myesf-docex-ui)
- Company: Unknown — not stated in the repository
- Product: Manage Your Education and Skills Funding Document Exchange
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

- Tier 3, `Aspose / Spire.Office suites`, run `run_1`, window `size:1001..2000`, rank 7
  - Query: `"Aspose.Total" extension:csproj size:1001..2000`
  - Retrieved 14 of 14 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Aspose / Spire.Office suites` (conversion, conversion) — code_import — [code](https://github.com/DFE-Digital/funding-service-myesf-docex-ui/blob/6c21367730f8b19f475cce9a991b15838dd36a4f/Pds.DocumentExchange.Services/DependencyInjection/FeatureServiceCollectionExtensions.cs)
- `Aspose / Spire.Office suites` (conversion, conversion) — manifest_declaration — [Pds.DocumentExchange.Services/Pds.DocumentExchange.Services.csproj](https://github.com/DFE-Digital/funding-service-myesf-docex-ui/blob/6c21367730f8b19f475cce9a991b15838dd36a4f/Pds.DocumentExchange.Services/Pds.DocumentExchange.Services.csproj)

**Evidence trail**

- [api_response](https://github.com/DFE-Digital/funding-service-myesf-docex-ui) (source: github_api): stars=2, fork=False, archived=False
- [code_permalink](https://github.com/DFE-Digital/funding-service-myesf-docex-ui/blob/6c21367730f8b19f475cce9a991b15838dd36a4f/Pds.DocumentExchange.Services/DependencyInjection/FeatureServiceCollectionExtensions.cs) (source: github_api): services.AddAsposeSpreadsheetBuilder(options =>             {                 var licenseStream = Assembly.GetExecutingAssembly()                     .GetManifestResourceStream("Pds.Docume
- [manifest_line](https://github.com/DFE-Digital/funding-service-myesf-docex-ui/blob/6c21367730f8b19f475cce9a991b15838dd36a4f/Pds.DocumentExchange.Services/Pds.DocumentExchange.Services.csproj) (source: github_api): </ItemGroup>      <ItemGroup>     <EmbeddedResource Include="Resources\Aspose.Total.lic">       <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>     </EmbeddedResource>   </ItemGroup>
- [readme_excerpt](https://github.com/DFE-Digital/funding-service-myesf-docex-ui/blob/main/README.md) (source: readme): External users having the ability to view, download and send documents back to DfE [The Department for Education](https://www.gov.uk/government/organisations/department-for-education) This project is

### 89. kedowen/KedoExecutorNet

**Repository / product**

- Repository: [https://github.com/kedowen/kedoexecutornet](https://github.com/kedowen/kedoexecutornet)
- Company: Unknown — not stated in the repository
- Product: KedoExecutor - Workflow Execution Engine (.NET Core)
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: contributor_count not collected

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

- Tier 3, `Aspose.Words`, run `run_1`, window `size:1001..2000`, rank 12
  - Query: `"Aspose.Words" extension:csproj size:1001..2000`
  - Retrieved 30 of 187 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Aspose.Words` (docx, generation) — code_import — [code](https://github.com/kedowen/KedoExecutorNet/blob/24538433a79af5919b260463373a9f95a3a07a30/Kedo.Web.Core/Startup.cs)
- `Aspose.Words` (docx, generation) — code_import — [code](https://github.com/kedowen/KedoExecutorNet/blob/24538433a79af5919b260463373a9f95a3a07a30/Kedo.Comm/WordHelper/WordHelper.cs)
- `Aspose.Words` (docx, generation) — code_import — [code](https://github.com/kedowen/KedoExecutorNet/blob/24538433a79af5919b260463373a9f95a3a07a30/Kedo.rqbbitMQ.CourseSelection/Utils/FileReaderUtil.cs)
- `Aspose.Words` (docx, generation) — manifest_declaration — [Kedo.Comm/Kedo.Comm.csproj](https://github.com/kedowen/KedoExecutorNet/blob/24538433a79af5919b260463373a9f95a3a07a30/Kedo.Comm/Kedo.Comm.csproj)
- `Aspose.Words` (docx, generation) — manifest_declaration — [Kedo.Web.Core/Kedo.Web.Core.csproj](https://github.com/kedowen/KedoExecutorNet/blob/24538433a79af5919b260463373a9f95a3a07a30/Kedo.Web.Core/Kedo.Web.Core.csproj)

**Evidence trail**

- [api_response](https://github.com/kedowen/KedoExecutorNet) (source: github_api): stars=3, fork=False, archived=False
- [readme_excerpt](https://github.com/kedowen/KedoExecutorNet/blob/main/README.md) (source: readme): company stated as 'Notice  \r\n\r\nKedo'
- [code_permalink](https://github.com/kedowen/KedoExecutorNet/blob/24538433a79af5919b260463373a9f95a3a07a30/Kedo.Web.Core/Startup.cs) (source: github_api): using Microsoft.Extensions.Hosting; using System.IO; using System; using Aspose.Words; using Microsoft.AspNetCore.Server.Kestrel.Core; using Microsoft.AspNetCore.Http.Features; using Kedo.Comm.C
- [code_permalink](https://github.com/kedowen/KedoExecutorNet/blob/24538433a79af5919b260463373a9f95a3a07a30/Kedo.Comm/WordHelper/WordHelper.cs) (source: github_api): ﻿using Aspose.Words; using Microsoft.AspNetCore.Mvc; using Microsoft.Extensions.Configuration;
- [code_permalink](https://github.com/kedowen/KedoExecutorNet/blob/24538433a79af5919b260463373a9f95a3a07a30/Kedo.rqbbitMQ.CourseSelection/Utils/FileReaderUtil.cs) (source: github_api): using System.IO; using Aspose.Words; using System.Text;
- [manifest_line](https://github.com/kedowen/KedoExecutorNet/blob/24538433a79af5919b260463373a9f95a3a07a30/Kedo.Comm/Kedo.Comm.csproj) (source: github_api): <ItemGroup>     <PackageReference Include="AlibabaCloud.SDK.Dysmsapi20170525" Version="2.0.22" />     <PackageReference Include="Aspose.Words" Version="24.6.0" />     <PackageReference Include=
- [manifest_line](https://github.com/kedowen/KedoExecutorNet/blob/24538433a79af5919b260463373a9f95a3a07a30/Kedo.Web.Core/Kedo.Web.Core.csproj) (source: github_api): </ItemGroup>   <ItemGroup>     <PackageReference Include="Aspose.Words" Version="24.6.0" />     <PackageReference Include="FluentEmail.Core" Version="3.0.2" />     <PackageReference Include="F
- [readme_excerpt](https://github.com/kedowen/KedoExecutorNet/blob/main/README.md) (source: readme): Kedo is an open-source workflow management platform for developers, deeply integrated with Large Language Model (LLM) capabilities.

### 90. sublee/subl.ee

**Repository / product**

- Repository: [https://github.com/sublee/subl.ee](https://github.com/sublee/subl.ee)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://subl.ee/

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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:251..500`, rank 14
  - Query: `"weasyprint" filename:pyproject.toml size:251..500`
  - Retrieved 30 of 309 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/sublee/subl.ee/blob/main/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/sublee/subl.ee/blob/e4c949cc6e19eb3f3cd717c5f6f687fbd92fda3f/stubs/weasyprint/__init__.pyi)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/sublee/subl.ee/blob/e4c949cc6e19eb3f3cd717c5f6f687fbd92fda3f/sublee.py)

**Evidence trail**

- [api_response](https://github.com/sublee/subl.ee) (source: github_api): stars=7, fork=False, archived=False
- [manifest_line](https://github.com/sublee/subl.ee/blob/main/pyproject.toml) (source: github_api): "weasyprint>=65.1",
- [code_permalink](https://github.com/sublee/subl.ee/blob/e4c949cc6e19eb3f3cd717c5f6f687fbd92fda3f/stubs/weasyprint/__init__.pyi) (source: github_api): from typing import BinaryIO, List from weasyprint.text.fonts import FontConfiguration class HTML:     def __init__(self, string: str) -> None: ...     def render(self, stylesheets: List[CSS], font_c
- [code_permalink](https://github.com/sublee/subl.ee/blob/e4c949cc6e19eb3f3cd717c5f6f687fbd92fda3f/sublee.py) (source: github_api): import fitz  # Its package name is PyMuPDF. import weasyprint from flask import (Flask, Response, abort, make_response, redirect,
- [other](https://github.com/sublee/subl.ee/tree/main/templates) (source: github_api): directory templates/ present

### 91. AWS-Student-Builder-Group-IIT-SL/CertSys

**Repository / product**

- Repository: [https://github.com/aws-student-builder-group-iit-sl/certsys](https://github.com/aws-student-builder-group-iit-sl/certsys)
- Company: Unknown — not stated in the repository
- Product: 🎓 CertSys – Certificate Generation & Emailing System
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

- Tier 3, `iText`, run `run_1`, window `size:501..1000`, rank 25
  - Query: `"itext" extension:csproj size:501..1000`
  - Sampled 30 of 2,760 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,760 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `iText` (pdf, generation) — code_import — [code](https://github.com/AWS-Student-Builder-Group-IIT-SL/CertSys/blob/2c0331ebb0b50592e43129b388d3e7e74fa0f981/CertSys/Services/CertGenerateService.cs)
- `iText` (pdf, generation) — manifest_declaration — [CertSys/CertSys.csproj](https://github.com/AWS-Student-Builder-Group-IIT-SL/CertSys/blob/2c0331ebb0b50592e43129b388d3e7e74fa0f981/CertSys/CertSys.csproj)

**Evidence trail**

- [api_response](https://github.com/AWS-Student-Builder-Group-IIT-SL/CertSys) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/AWS-Student-Builder-Group-IIT-SL/CertSys/blob/2c0331ebb0b50592e43129b388d3e7e74fa0f981/CertSys/Services/CertGenerateService.cs) (source: github_api): ﻿using CertSys.Modals; using ClosedXML.Excel; using iText.IO.Font.Constants; using iText.Kernel.Colors; using iText.Kernel.Font; using iText.Kernel.Pdf; using iText.Kernel.Pdf.Canvas;
- [manifest_line](https://github.com/AWS-Student-Builder-Group-IIT-SL/CertSys/blob/2c0331ebb0b50592e43129b388d3e7e74fa0f981/CertSys/CertSys.csproj) (source: github_api): <ItemGroup>     <PackageReference Include="ClosedXML" Version="0.105.0" />     <PackageReference Include="itext" Version="9.6.0" />     <PackageReference Include="itext.bouncy-castle-adapter" Versio
- [other](https://github.com/AWS-Student-Builder-Group-IIT-SL/CertSys/tree/main/Templates) (source: github_api): directory Templates/ present

### 92. GaiZhenbiao/ChuanhuChatGPT

**Repository / product**

- Repository: [https://github.com/gaizhenbiao/chuanhuchatgpt](https://github.com/gaizhenbiao/chuanhuchatgpt)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://huggingface.co/spaces/JohnSmith9982/ChuanhuChatGPT

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=2, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: category_count=2; template_directory_present=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

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

- Tier 3, `python-docx`, run `run_1`, window `size:501..1000`, rank 1
  - Query: `"python-docx" filename:requirements.txt size:501..1000`
  - Sampled 30 of 11,984 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 11,984 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Unstructured`, run `run_1`, window `size:501..1000`, rank 1
  - Query: `"unstructured" filename:requirements.txt size:501..1000`
  - Sampled 30 of 2,464 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,464 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/main/requirements.txt)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/c020b2ddc0fc230ef4f2398152a89d8a2d907f0a/modules/index_func.py)
- `python-docx` (docx, generation) — manifest_declaration — [requirements.txt](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/main/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/GaiZhenbiao/ChuanhuChatGPT) (source: github_api): stars=15281, fork=False, archived=False
- [manifest_line](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/main/requirements.txt) (source: github_api): unstructured
- [code_permalink](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/c020b2ddc0fc230ef4f2398152a89d8a2d907f0a/modules/index_func.py) (source: github_api): from langchain.document_loaders import \                     UnstructuredWordDocumentLoader
- [manifest_line](https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/main/requirements.txt) (source: github_api): python-docx
- [other](https://github.com/GaiZhenbiao/ChuanhuChatGPT/tree/main/templates) (source: github_api): directory templates/ present

### 93. spk3077/pdf-library-assessment

**Repository / product**

- Repository: [https://github.com/spk3077/pdf-library-assessment](https://github.com/spk3077/pdf-library-assessment)
- Company: Unknown — not stated in the repository
- Product: pdf-library-assessment
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

- Tier 3, `pikepdf`, run `run_1`, window `size:0..250`, rank 22
  - Query: `"pikepdf" filename:requirements.txt size:0..250`
  - Retrieved 30 of 790 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pikepdf` (pdf, generation) — manifest_declaration — [environments/pikepdf/requirements.txt](https://github.com/spk3077/pdf-library-assessment/blob/f1f0ad2a1f5599263724b986a7220ec21a87b85c/environments/pikepdf/requirements.txt)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/spk3077/pdf-library-assessment/blob/f1f0ad2a1f5599263724b986a7220ec21a87b85c/exploit-checking/injection-check.py)
- `pikepdf` (pdf, generation) — manifest_declaration — [exploit-checking/requirements.txt](https://github.com/spk3077/pdf-library-assessment/blob/f1f0ad2a1f5599263724b986a7220ec21a87b85c/exploit-checking/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/spk3077/pdf-library-assessment) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/spk3077/pdf-library-assessment/blob/f1f0ad2a1f5599263724b986a7220ec21a87b85c/environments/pikepdf/requirements.txt) (source: github_api): Django pikepdf reportlab
- [code_permalink](https://github.com/spk3077/pdf-library-assessment/blob/f1f0ad2a1f5599263724b986a7220ec21a87b85c/exploit-checking/injection-check.py) (source: github_api): import pikepdf from PyPDF2 import PdfReader
- [manifest_line](https://github.com/spk3077/pdf-library-assessment/blob/f1f0ad2a1f5599263724b986a7220ec21a87b85c/exploit-checking/requirements.txt) (source: github_api): # pip install -r requirements.txts PyPDF2 pikePDF
- [other](https://github.com/spk3077/pdf-library-assessment/tree/main/documents) (source: github_api): directory documents/ present

### 94. bigbeartechworld/big-bear-casaos

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

### 95. rsrdesarrollo/sarna

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

### 96. lr101/homelab

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

### 97. qgis/QGIS-Certification-Website

**Repository / product**

- Repository: [https://github.com/qgis/qgis-certification-website](https://github.com/qgis/qgis-certification-website)
- Company: Kartoza.com
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=2, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: pipeline_stage_count=2; confirmed generation/conversion code \| unknown: contributor_count not collected

**Score**

- Score: 19/100 (a score, not a probability)
- Raw weighted score: 0.95 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume | 1 |
| Document complexity | 0 |
| Business criticality | 0 |
| Pipeline complexity | 2 |
| Maintenance burden *(unknown)* | 0 |
| Build-vs-buy signal | 3 |
| Commercial leverage | 2 |

**Evidence coverage**

Evidence coverage: 6/7 dimensions

- Maintenance burden: Unknown

**Discovery provenance**

- Tier 3, `WeasyPrint`, run `run_1`, window `size:1001..2000`, rank 22
  - Query: `"weasyprint" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 2,532 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,532 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [deployment/docker/REQUIREMENTS.txt](https://github.com/qgis/QGIS-Certification-Website/blob/06774bf5ca8ca868e01e48e500a99cc03e8a8c32/deployment/docker/REQUIREMENTS.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/qgis/QGIS-Certification-Website/blob/06774bf5ca8ca868e01e48e500a99cc03e8a8c32/django_project/certification/invoice_utils.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/qgis/QGIS-Certification-Website/blob/06774bf5ca8ca868e01e48e500a99cc03e8a8c32/django_project/core/settings/base.py)

**Evidence trail**

- [api_response](https://github.com/qgis/QGIS-Certification-Website) (source: github_api): stars=0, fork=False, archived=False
- [readme_excerpt](https://github.com/qgis/QGIS-Certification-Website/blob/master/README.md) (source: readme): company stated as 'Kartoza.com'
- [manifest_line](https://github.com/qgis/QGIS-Certification-Website/blob/06774bf5ca8ca868e01e48e500a99cc03e8a8c32/deployment/docker/REQUIREMENTS.txt) (source: github_api): requests~=2.32 # support special characters Unidecode~=0.4 WeasyPrint==62.1 pydyf==0.11.0 xhtml2pdf~=0.2 sentry-sdk~=2.2
- [code_permalink](https://github.com/qgis/QGIS-Certification-Website/blob/06774bf5ca8ca868e01e48e500a99cc03e8a8c32/django_project/certification/invoice_utils.py) (source: github_api): def render_invoice_pdf(invoice) -> bytes:     """Render the invoice as a PDF using WeasyPrint."""     from weasyprint import HTML  # imported lazily — weasyprint loads native libs     project = inv
- [code_permalink](https://github.com/qgis/QGIS-Certification-Website/blob/06774bf5ca8ca868e01e48e500a99cc03e8a8c32/django_project/core/settings/base.py) (source: github_api): WEASYPRINT_OPTIONS = {     "zoom": 1.0,

### 98. kw677/Fileo

**Repository / product**

- Repository: [https://github.com/kw677/fileo](https://github.com/kw677/fileo)
- Company: Unknown — not stated in the repository
- Product: Fileo
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://fileo.even-simpler.com/

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| supporting: confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

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

- Tier 3, `Open XML SDK`, run `run_1`, window `size:251..500`, rank 21
  - Query: `"DocumentFormat.OpenXml" filename:packages.config size:251..500`
  - Retrieved 30 of 508 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Open XML SDK` (docx, generation) — code_import — [code](https://github.com/kw677/Fileo/blob/d31ffcdc5a2e98dbcc2b3f120ce37cc5a2830f69/Fileo/Import/ImporterDefinition/ImportFromXlsx.cs)
- `Open XML SDK` (docx, generation) — manifest_declaration — [Fileo/Fileo.csproj](https://github.com/kw677/Fileo/blob/d31ffcdc5a2e98dbcc2b3f120ce37cc5a2830f69/Fileo/Fileo.csproj)
- `Open XML SDK` (docx, generation) — manifest_declaration — [Fileo/packages.config](https://github.com/kw677/Fileo/blob/d31ffcdc5a2e98dbcc2b3f120ce37cc5a2830f69/Fileo/packages.config)

**Evidence trail**

- [api_response](https://github.com/kw677/Fileo) (source: github_api): stars=10, fork=False, archived=False
- [code_permalink](https://github.com/kw677/Fileo/blob/d31ffcdc5a2e98dbcc2b3f120ce37cc5a2830f69/Fileo/Import/ImporterDefinition/ImportFromXlsx.cs) (source: github_api): ﻿using DocumentFormat.OpenXml.Packaging; using DocumentFormat.OpenXml.Spreadsheet; using Fileo.Common; using Fileo.Import.Base; using Fileo.Import.DataStructure.FileStructure; using System; using Syst
- [manifest_line](https://github.com/kw677/Fileo/blob/d31ffcdc5a2e98dbcc2b3f120ce37cc5a2830f69/Fileo/Fileo.csproj) (source: github_api): <WarningLevel>4</WarningLevel>   </PropertyGroup>   <ItemGroup>     <Reference Include="DocumentFormat.OpenXml, Version=2.5.5631.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, processorArchi
- [manifest_line](https://github.com/kw677/Fileo/blob/d31ffcdc5a2e98dbcc2b3f120ce37cc5a2830f69/Fileo/packages.config) (source: github_api): ﻿<?xml version="1.0" encoding="utf-8"?> <packages>   <package id="DocumentFormat.OpenXml" version="2.5" targetFramework="net452" />   <package id="NLog" version="4.4.7" targetFramework="net452" />   <
- [readme_excerpt](https://github.com/kw677/Fileo/blob/master/README.md) (source: readme): Fileo is a nice solution for load data from files with extensions: .csv, .xls, .xlsx.

### 99. iiitdwd-exams/certificates

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

### 100. Mihir-Rabari/inboxfm-connect

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

### 101. datawizz/Openpieces

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

### 102. DenizAltunkapan/ilias-mcp

**Repository / product**

- Repository: [https://github.com/denizaltunkapan/ilias-mcp](https://github.com/denizaltunkapan/ilias-mcp)
- Company: Unknown — not stated in the repository
- Product: ILIAS MCP
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria met but no evidence the document workflow is more than an isolated utility \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

**Score**

- Score: 18/100 (a score, not a probability)
- Raw weighted score: 0.90 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
| Business criticality | 3 |
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

- Tier 3, `pypdf / PyPDF2`, run `run_1`, window `size:501..1000`, rank 29
  - Query: `"pypdf" filename:pyproject.toml size:501..1000`
  - Sampled 30 of 10,336 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,336 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `pypdf / PyPDF2` (pdf, extraction) — manifest_declaration — [pyproject.toml](https://github.com/DenizAltunkapan/ilias-mcp/blob/main/pyproject.toml)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/DenizAltunkapan/ilias-mcp/blob/0e1666cc998693f7d1b649bda8dfdab663db190a/src/mcp_app/server.py)
- `pypdf / PyPDF2` (pdf, extraction) — code_import — [code](https://github.com/DenizAltunkapan/ilias-mcp/blob/0e1666cc998693f7d1b649bda8dfdab663db190a/src/services/repository_service.py)

**Evidence trail**

- [api_response](https://github.com/DenizAltunkapan/ilias-mcp) (source: github_api): stars=11, fork=False, archived=False
- [manifest_line](https://github.com/DenizAltunkapan/ilias-mcp/blob/main/pyproject.toml) (source: github_api): "pypdf>=5.0.0",
- [code_permalink](https://github.com/DenizAltunkapan/ilias-mcp/blob/0e1666cc998693f7d1b649bda8dfdab663db190a/src/mcp_app/server.py) (source: github_api): max_chars: int = 20000,     max_pdf_pages: int = 20, ) -> dict[str, object]:     """Download file content by ref_id. PDFs are parsed to text via pypdf."""     app = _app(ctx)     try:         cont
- [code_permalink](https://github.com/DenizAltunkapan/ilias-mcp/blob/0e1666cc998693f7d1b649bda8dfdab663db190a/src/services/repository_service.py) (source: github_api): from bs4 import BeautifulSoup, Tag from pypdf import PdfReader
- [readme_excerpt](https://github.com/DenizAltunkapan/ilias-mcp/blob/main/README.md) (source: readme): Downloads use the official ILIAS file routes used by the Stuttgart fork, including ilObjFileGUI sendfile and goto.php file download routes.

### 103. Websoft9/docker-library

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

### 104. runtipi/runtipi-appstore

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

### 105. dendianugerah/reubah

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

### 106. bigcapitalhq/bigcapital

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

### 107. infonl/dimpact-zaakafhandelcomponent

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

### 108. scienceai/open-docx

**Repository / product**

- Repository: [https://github.com/scienceai/open-docx](https://github.com/scienceai/open-docx)
- Company: Unknown — not stated in the repository
- Product: open-docx
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

- Tier 3, `docx (dolanmiu/docx)`, run `run_1`, window `size:501..1000`, rank 28
  - Query: `"docx" filename:package.json size:501..1000`
  - Sampled 30 of 6,624 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 6,624 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docx (dolanmiu/docx)` (docx, generation) — manifest_declaration — [package.json](https://github.com/scienceai/open-docx/blob/master/package.json)
- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/scienceai/open-docx/blob/f63b34dc677e18decb4d710c84626e0e5533693c/open-docx.js)

**Evidence trail**

- [api_response](https://github.com/scienceai/open-docx) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/scienceai/open-docx/blob/master/package.json) (source: github_api): "name": "open-docx",
- [code_permalink](https://github.com/scienceai/open-docx/blob/f63b34dc677e18decb4d710c84626e0e5533693c/open-docx.js) (source: github_api): if (ret) console.log(ret); } if (process.argv.length !== 4) die('Usage: open-docx path/to/document.docx path/to/directory'); var doc = path.resolve(process.argv[2])   , dir = path.resolve(process.a
- [readme_excerpt](https://github.com/scienceai/open-docx/blob/master/README.md) (source: readme): This tool allows you to quickly split open a docx file.

### 109. airens/interactive_brokers_tax

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

### 110. virgiliojr94/localpdf.io

**Repository / product**

- Repository: [https://github.com/virgiliojr94/localpdf.io](https://github.com/virgiliojr94/localpdf.io)
- Company: Unknown — not stated in the repository
- Product: 🌟 LocalPDF.io
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

- Tier 3, `pdf2docx`, run `run_1`, window `size:0..250`, rank 7
  - Query: `"pdf2docx" filename:requirements.txt size:0..250`
  - Retrieved 30 of 842 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pdf2docx` (other_processing, mixed) — manifest_declaration — [requirements.txt](https://github.com/virgiliojr94/localpdf.io/blob/main/requirements.txt)
- `pdf2docx` (other_processing, mixed) — code_import — [code](https://github.com/virgiliojr94/localpdf.io/blob/6fed6e8493c35efd788faac8e386d2f637112f46/app.py)

**Evidence trail**

- [api_response](https://github.com/virgiliojr94/localpdf.io) (source: github_api): stars=257, fork=False, archived=False
- [manifest_line](https://github.com/virgiliojr94/localpdf.io/blob/main/requirements.txt) (source: github_api): pdf2docx==0.5.8
- [code_permalink](https://github.com/virgiliojr94/localpdf.io/blob/6fed6e8493c35efd788faac8e386d2f637112f46/app.py) (source: github_api): send_file, ) from pdf2docx import Converter from pdf2docx.converter import ConversionException import pytesseract from PIL import Image from reportlab.lib.pagesizes import letter
- [readme_excerpt](https://github.com/virgiliojr94/localpdf.io/blob/main/README.md) (source: readme): <div align="right"> 🌐 **Language** \| **English** · [Português 🇧🇷](README.pt-br.md) </div> <div align="center"> **🌐 [Visit the Official Website](https://virgiliojr94.github.io/localpdf.io/)** [Features

### 111. capitoledulibre/cdl_paper_generator

**Repository / product**

- Repository: [https://github.com/capitoledulibre/cdl_paper_generator](https://github.com/capitoledulibre/cdl_paper_generator)
- Company: Unknown — not stated in the repository
- Product: cdl_paper_generator
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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:251..500`, rank 11
  - Query: `"weasyprint" filename:pyproject.toml size:251..500`
  - Retrieved 30 of 309 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/capitoledulibre/cdl_paper_generator/blob/main/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/capitoledulibre/cdl_paper_generator/blob/014ec4bdaa7f36b342d624cea0061521ce334cf7/gen.py)

**Evidence trail**

- [api_response](https://github.com/capitoledulibre/cdl_paper_generator) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/capitoledulibre/cdl_paper_generator/blob/main/pyproject.toml) (source: github_api): weasyprint = "*"
- [code_permalink](https://github.com/capitoledulibre/cdl_paper_generator/blob/014ec4bdaa7f36b342d624cea0061521ce334cf7/gen.py) (source: github_api): from urllib.request import urlopen from xml.etree import ElementTree from weasyprint import CSS, HTML class UniqueByConference(object):

### 112. yogeshhk/Sarvadnya

**Repository / product**

- Repository: [https://github.com/yogeshhk/sarvadnya](https://github.com/yogeshhk/sarvadnya)
- Company: Unknown — not stated in the repository
- Product: Sarvadnya (सर्वज्ञ), an All-Knowing Chatbot!!
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=true \| supporting: template_directory_present=true \| unknown: company_name=null; contributor_count not collected

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

- Tier 3, `Docling`, run `run_1`, window `size:501..1000`, rank 19
  - Query: `"docling" filename:requirements.txt size:501..1000`
  - Retrieved 30 of 740 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/yogeshhk/Sarvadnya/blob/bccd21901e85ad862e04f7ffaf7bfc1f8d7ed301/src/ask_finance/document_parser.py)
- `Docling` (other_processing, extraction) — manifest_declaration — [src/ask_finance/requirements.txt](https://github.com/yogeshhk/Sarvadnya/blob/bccd21901e85ad862e04f7ffaf7bfc1f8d7ed301/src/ask_finance/requirements.txt)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/yogeshhk/Sarvadnya/blob/bccd21901e85ad862e04f7ffaf7bfc1f8d7ed301/src/ask_finance/test_document_parser.py)

**Evidence trail**

- [api_response](https://github.com/yogeshhk/Sarvadnya) (source: github_api): stars=65, fork=False, archived=False
- [code_permalink](https://github.com/yogeshhk/Sarvadnya/blob/bccd21901e85ad862e04f7ffaf7bfc1f8d7ed301/src/ask_finance/document_parser.py) (source: github_api): from typing import Dict, List, Optional, Tuple, Union import uuid from docling.document_converter import DocumentConverter from docling.document_converter import ConversionResult import pandas as pd
- [manifest_line](https://github.com/yogeshhk/Sarvadnya/blob/bccd21901e85ad862e04f7ffaf7bfc1f8d7ed301/src/ask_finance/requirements.txt) (source: github_api): # Core document processing docling>=1.0.0 pandas>=1.5.0 numpy>=1.24.0 Pillow>=9.0.0 # Vector embeddings and search
- [code_permalink](https://github.com/yogeshhk/Sarvadnya/blob/bccd21901e85ad862e04f7ffaf7bfc1f8d7ed301/src/ask_finance/test_document_parser.py) (source: github_api): Tests focus on the pure-Python logic that does not require docling or a real PDF. Run with: python -m pytest test_document_parser.py -v
- [other](https://github.com/yogeshhk/Sarvadnya/tree/master/reports) (source: github_api): directory reports/ present

### 113. bbossgroups/bboss

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

### 114. runZeroInc/runzero-api

**Repository / product**

- Repository: [https://github.com/runzeroinc/runzero-api](https://github.com/runzeroinc/runzero-api)
- Company: Unknown — not stated in the repository
- Product: runZero API
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

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_1`, window `size:0..250`, rank 16
  - Query: `"puppeteer" filename:package.json size:0..250`
  - Sampled 30 of 5,600 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 5,600 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package-lock.json](https://github.com/runZeroInc/runzero-api/blob/main/package-lock.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/runZeroInc/runzero-api/blob/main/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/runZeroInc/runzero-api/blob/78a8afc316f53871670975a8c8f551a91697049b/pdfgen/makepdf.js)

**Evidence trail**

- [api_response](https://github.com/runZeroInc/runzero-api) (source: github_api): stars=11, fork=False, archived=False
- [manifest_line](https://github.com/runZeroInc/runzero-api/blob/main/package-lock.json) (source: github_api): "puppeteer": "^25.1.0",
- [manifest_line](https://github.com/runZeroInc/runzero-api/blob/main/package.json) (source: github_api): "puppeteer": "^25.1.0",
- [code_permalink](https://github.com/runZeroInc/runzero-api/blob/78a8afc316f53871670975a8c8f551a91697049b/pdfgen/makepdf.js) (source: github_api): const puppeteer = require('puppeteer'); (async () => {     const browser = await puppeteer.launch({headless: true, args: ["--no-sandbox", "--disable-setuid-sandbox"]});     const page = await browser

### 115. ethicalhackingplayground/shodan-grabber

**Repository / product**

- Repository: [https://github.com/ethicalhackingplayground/shodan-grabber](https://github.com/ethicalhackingplayground/shodan-grabber)
- Company: Unknown — not stated in the repository
- Product: Shodan-Grabber
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

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_1`, window `size:251..500`, rank 15
  - Query: `"puppeteer" filename:package.json size:251..500`
  - Sampled 30 of 23,552 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 23,552 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package-lock.json](https://github.com/ethicalhackingplayground/shodan-grabber/blob/main/package-lock.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/ethicalhackingplayground/shodan-grabber/blob/main/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/ethicalhackingplayground/shodan-grabber/blob/4a36e6426d712cee6ed2d1dd1e618d2e1cc0d938/index.js)

**Evidence trail**

- [api_response](https://github.com/ethicalhackingplayground/shodan-grabber) (source: github_api): stars=18, fork=False, archived=False
- [manifest_line](https://github.com/ethicalhackingplayground/shodan-grabber/blob/main/package-lock.json) (source: github_api): "puppeteer": "^23.7.1"
- [manifest_line](https://github.com/ethicalhackingplayground/shodan-grabber/blob/main/package.json) (source: github_api): "puppeteer": "^23.7.1"
- [code_permalink](https://github.com/ethicalhackingplayground/shodan-grabber/blob/4a36e6426d712cee6ed2d1dd1e618d2e1cc0d938/index.js) (source: github_api): const puppeteer = require("puppeteer"); const fs = require("fs"); const path = require("path"); const minimist = require("minimist"); const helpText = () => {   (async () => {

### 116. rava-dosa/epub2pdf

**Repository / product**

- Repository: [https://github.com/rava-dosa/epub2pdf](https://github.com/rava-dosa/epub2pdf)
- Company: Unknown — not stated in the repository
- Product: Instruction to Setup
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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:251..500`, rank 21
  - Query: `"weasyprint" filename:requirements.txt size:251..500`
  - Sampled 30 of 2,632 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,632 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements.txt](https://github.com/rava-dosa/epub2pdf/blob/master/requirements.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/rava-dosa/epub2pdf/blob/ab00a23abc50109e61c7442dfa604cec80c0024b/mobi2pdf.py)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/rava-dosa/epub2pdf/blob/ab00a23abc50109e61c7442dfa604cec80c0024b/epub2pdf.py)

**Evidence trail**

- [api_response](https://github.com/rava-dosa/epub2pdf) (source: github_api): stars=107, fork=False, archived=False
- [manifest_line](https://github.com/rava-dosa/epub2pdf/blob/master/requirements.txt) (source: github_api): WeasyPrint==51
- [code_permalink](https://github.com/rava-dosa/epub2pdf/blob/ab00a23abc50109e61c7442dfa604cec80c0024b/mobi2pdf.py) (source: github_api): from bs4 import BeautifulSoup from weasyprint import HTML, CSS, default_url_fetcher import mobi import shutil import sys if __name__ == "__main__":
- [code_permalink](https://github.com/rava-dosa/epub2pdf/blob/ab00a23abc50109e61c7442dfa604cec80c0024b/epub2pdf.py) (source: github_api): from bs4 import BeautifulSoup from weasyprint import HTML, CSS, default_url_fetcher from weasyprint.fonts import FontConfiguration from os import listdir import sys import shutil import zipfile

### 117. miyabayt/spring-boot-doma2-sample

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

### 118. UniversitaDellaCalabria/uniTicket

**Repository / product**

- Repository: [https://github.com/universitadellacalabria/uniticket](https://github.com/universitadellacalabria/uniticket)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: real_estate (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:1001..2000`, rank 17
  - Query: `"weasyprint" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 2,532 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,532 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements.txt](https://github.com/UniversitaDellaCalabria/uniTicket/blob/master/requirements.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/UniversitaDellaCalabria/uniTicket/blob/5a31ce4812bbce1d1ab6bb61fb2969f48b4e3dd6/uniticket/uni_ticket/pdf_utils.py)

**Evidence trail**

- [api_response](https://github.com/UniversitaDellaCalabria/uniTicket) (source: github_api): stars=27, fork=False, archived=False
- [manifest_line](https://github.com/UniversitaDellaCalabria/uniTicket/blob/master/requirements.txt) (source: github_api): WeasyPrint
- [code_permalink](https://github.com/UniversitaDellaCalabria/uniTicket/blob/5a31ce4812bbce1d1ab6bb61fb2969f48b4e3dd6/uniticket/uni_ticket/pdf_utils.py) (source: github_api): try:     from weasyprint import HTML except ModuleNotFoundError:

### 119. cdump/investments

**Repository / product**

- Repository: [https://github.com/cdump/investments](https://github.com/cdump/investments)
- Company: Unknown — not stated in the repository
- Product: Investments
- Industry: finance_investment (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:1001..2000`, rank 19
  - Query: `"weasyprint" filename:pyproject.toml size:1001..2000`
  - Sampled 30 of 1,190 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,190 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [pyproject.toml](https://github.com/cdump/investments/blob/master/pyproject.toml)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/cdump/investments/blob/3a56f9dc3fbbd9a36e6813a158077dff090c490f/investments/ibtax/report_presenter.py)

**Evidence trail**

- [api_response](https://github.com/cdump/investments) (source: github_api): stars=115, fork=False, archived=False
- [manifest_line](https://github.com/cdump/investments/blob/master/pyproject.toml) (source: github_api): "WeasyPrint>=60.2",
- [code_permalink](https://github.com/cdump/investments/blob/3a56f9dc3fbbd9a36e6813a158077dff090c490f/investments/ibtax/report_presenter.py) (source: github_api): import pandas  # type: ignore from tabulate import tabulate from weasyprint import CSS, HTML  # type: ignore from investments.money import Money from investments.trades_fifo import PortfolioElement

### 120. simbianai/taskgen

**Repository / product**

- Repository: [https://github.com/simbianai/taskgen](https://github.com/simbianai/taskgen)
- Company: Unknown — not stated in the repository
- Product: TaskGen (Simbian) v3.3.4
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

- Tier 3, `python-docx`, run `run_1`, window `size:501..1000`, rank 3
  - Query: `"python-docx" filename:pyproject.toml size:501..1000`
  - Sampled 30 of 4,072 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 4,072 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `python-docx` (docx, generation) — manifest_declaration — [pyproject.toml](https://github.com/simbianai/taskgen/blob/main/pyproject.toml)
- `python-docx` (docx, generation) — manifest_declaration — [requirements.txt](https://github.com/simbianai/taskgen/blob/main/requirements.txt)
- `python-docx` (docx, generation) — code_import — [code](https://github.com/simbianai/taskgen/blob/e20048068cb0659862c2bec459f9b0c5e93c88a3/setup.py)

**Evidence trail**

- [api_response](https://github.com/simbianai/taskgen) (source: github_api): stars=462, fork=False, archived=False
- [manifest_line](https://github.com/simbianai/taskgen/blob/main/pyproject.toml) (source: github_api): "python-docx", "pandas", "xlrd",
- [manifest_line](https://github.com/simbianai/taskgen/blob/main/requirements.txt) (source: github_api): python-docx
- [code_permalink](https://github.com/simbianai/taskgen/blob/e20048068cb0659862c2bec459f9b0c5e93c88a3/setup.py) (source: github_api): "dill>=0.3.9",         "termcolor>=3.1.0",         "requests",         "python-docx",         "pandas",         "xlrd",         "asyncio",
- [readme_excerpt](https://github.com/simbianai/taskgen/blob/main/README.md) (source: readme): The LLM to be used by the Agent <br/><br/> **Agent Internal Parameters**: **Task**: String.

### 121. JasonObeid/Chart2Text

**Repository / product**

- Repository: [https://github.com/jasonobeid/chart2text](https://github.com/jasonobeid/chart2text)
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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:251..500`, rank 18
  - Query: `"weasyprint" filename:requirements.txt size:251..500`
  - Sampled 30 of 2,632 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,632 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [requirements.txt](https://github.com/JasonObeid/Chart2Text/blob/master/requirements.txt)
- `WeasyPrint` (template_generation, conversion) — code_import — [code](https://github.com/JasonObeid/Chart2Text/blob/b400d6ddddb5454ac81e4a3d6ceeca3c08b0b98a/utils/getSamples.py)

**Evidence trail**

- [api_response](https://github.com/JasonObeid/Chart2Text) (source: github_api): stars=160, fork=False, archived=False
- [manifest_line](https://github.com/JasonObeid/Chart2Text/blob/master/requirements.txt) (source: github_api): WeasyPrint==51
- [code_permalink](https://github.com/JasonObeid/Chart2Text/blob/b400d6ddddb5454ac81e4a3d6ceeca3c08b0b98a/utils/getSamples.py) (source: github_api): import os from sklearn import utils import csv import weasyprint as wsp import PIL as pil import matplotlib.pyplot as plt

### 122. zhihuiyuze/PDF-Prompt-Injection-Toolkit

**Repository / product**

- Repository: [https://github.com/zhihuiyuze/pdf-prompt-injection-toolkit](https://github.com/zhihuiyuze/pdf-prompt-injection-toolkit)
- Company: Unknown — not stated in the repository
- Product: 🛡️ PDF Prompt Injection Toolkit
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

- Tier 3, `pikepdf`, run `run_1`, window `size:0..250`, rank 30
  - Query: `"pikepdf" filename:requirements.txt size:0..250`
  - Retrieved 30 of 790 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pikepdf` (pdf, generation) — manifest_declaration — [requirements.txt](https://github.com/zhihuiyuze/PDF-Prompt-Injection-Toolkit/blob/master/requirements.txt)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/zhihuiyuze/PDF-Prompt-Injection-Toolkit/blob/02f9ec412bff82114ae825bcaaeda88a96d606e2/pdf_injector.py)
- `pikepdf` (pdf, generation) — code_import — [code](https://github.com/zhihuiyuze/PDF-Prompt-Injection-Toolkit/blob/02f9ec412bff82114ae825bcaaeda88a96d606e2/pdf_injection_detector.py)

**Evidence trail**

- [api_response](https://github.com/zhihuiyuze/PDF-Prompt-Injection-Toolkit) (source: github_api): stars=62, fork=False, archived=False
- [manifest_line](https://github.com/zhihuiyuze/PDF-Prompt-Injection-Toolkit/blob/master/requirements.txt) (source: github_api): pikepdf
- [code_permalink](https://github.com/zhihuiyuze/PDF-Prompt-Injection-Toolkit/blob/02f9ec412bff82114ae825bcaaeda88a96d606e2/pdf_injector.py) (source: github_api): def inject_micro_font(pdf: pikepdf.Pdf, payload: str) -> str:     """
- [code_permalink](https://github.com/zhihuiyuze/PDF-Prompt-Injection-Toolkit/blob/02f9ec412bff82114ae825bcaaeda88a96d606e2/pdf_injection_detector.py) (source: github_api): from pypdf import PdfReader import pikepdf
- [readme_excerpt](https://github.com/zhihuiyuze/PDF-Prompt-Injection-Toolkit/blob/master/README.md) (source: readme): This toolkit lets you **test whether your systems are vulnerable** — and **detect whether documents you've received have been weaponized**.

### 123. inbn/screenshot-urls

**Repository / product**

- Repository: [https://github.com/inbn/screenshot-urls](https://github.com/inbn/screenshot-urls)
- Company: Unknown — not stated in the repository
- Product: Screenshot URLs script
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

- Tier 3, `Puppeteer / Playwright (used for PDF)`, run `run_1`, window `size:251..500`, rank 28
  - Query: `"puppeteer" filename:package.json size:251..500`
  - Sampled 30 of 23,552 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 23,552 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package-lock.json](https://github.com/inbn/screenshot-urls/blob/master/package-lock.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — manifest_declaration — [package.json](https://github.com/inbn/screenshot-urls/blob/master/package.json)
- `Puppeteer / Playwright (used for PDF)` (template_generation, conversion) — code_import — [code](https://github.com/inbn/screenshot-urls/blob/0c5e58688d1f4f876655315693c6f744ce161479/index.js)

**Evidence trail**

- [api_response](https://github.com/inbn/screenshot-urls) (source: github_api): stars=34, fork=False, archived=False
- [manifest_line](https://github.com/inbn/screenshot-urls/blob/master/package-lock.json) (source: github_api): "puppeteer": "^18.0.5",
- [manifest_line](https://github.com/inbn/screenshot-urls/blob/master/package.json) (source: github_api): "puppeteer": "^18.0.5",
- [code_permalink](https://github.com/inbn/screenshot-urls/blob/0c5e58688d1f4f876655315693c6f744ce161479/index.js) (source: github_api): const formatDate = require("date-fns/format"); const puppeteer = require("puppeteer"); const sanitize = require("sanitize-filename"); const fs = require("fs"); let program = require("commander"); //

### 124. MK2112/any_to_any.py

**Repository / product**

- Repository: [https://github.com/mk2112/any_to_any.py](https://github.com/mk2112/any_to_any.py)
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

- Tier 3, `mammoth / python-mammoth`, run `run_1`, window `size:251..500`, rank 7
  - Query: `"mammoth" filename:requirements.txt size:251..500`
  - Retrieved 30 of 227 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [requirements.txt](https://github.com/MK2112/any_to_any.py/blob/main/requirements.txt)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [requirements_build.txt](https://github.com/MK2112/any_to_any.py/blob/main/requirements_build.txt)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/MK2112/any_to_any.py/blob/7d3859cbe624f5c045b20cfb59590135e8f638ea/gui/build.py)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/MK2112/any_to_any.py/blob/7d3859cbe624f5c045b20cfb59590135e8f638ea/core/converter/doc_converter.py)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/MK2112/any_to_any.py/blob/7d3859cbe624f5c045b20cfb59590135e8f638ea/tests/test_doc_converter.py)

**Evidence trail**

- [api_response](https://github.com/MK2112/any_to_any.py) (source: github_api): stars=32, fork=False, archived=False
- [manifest_line](https://github.com/MK2112/any_to_any.py/blob/main/requirements.txt) (source: github_api): mammoth>=1.9.0
- [manifest_line](https://github.com/MK2112/any_to_any.py/blob/main/requirements_build.txt) (source: github_api): mammoth>=1.9.0
- [code_permalink](https://github.com/MK2112/any_to_any.py/blob/7d3859cbe624f5c045b20cfb59590135e8f638ea/gui/build.py) (source: github_api): "--hidden-import=imageio_ffmpeg",         "--hidden-import=docx",         "--hidden-import=pptx",         "--hidden-import=mammoth",         "--collect-all=reportlab",         "--hidden-import
- [code_permalink](https://github.com/MK2112/any_to_any.py/blob/7d3859cbe624f5c045b20cfb59590135e8f638ea/core/converter/doc_converter.py) (source: github_api): import shutil import mammoth import subprocess
- [code_permalink](https://github.com/MK2112/any_to_any.py/blob/7d3859cbe624f5c045b20cfb59590135e8f638ea/tests/test_doc_converter.py) (source: github_api): @patch("mammoth.convert_to_html")     @patch("os.makedirs")
- [other](https://github.com/MK2112/any_to_any.py/tree/main/templates) (source: github_api): directory templates/ present

### 125. lmorgadodacosta/iTELL

**Repository / product**

- Repository: [https://github.com/lmorgadodacosta/itell](https://github.com/lmorgadodacosta/itell)
- Company: Unknown — not stated in the repository
- Product: iTELL: Intelligent Technologically Enhanced Language Learning
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

- Tier 3, `mammoth / python-mammoth`, run `run_1`, window `size:0..250`, rank 27
  - Query: `"mammoth" filename:requirements.txt size:0..250`
  - Retrieved 30 of 467 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [requirements.txt](https://github.com/lmorgadodacosta/iTELL/blob/master/requirements.txt)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/lmorgadodacosta/iTELL/blob/3c027d19b352c3167dffb24052def82631c0e947/lcc.py)

**Evidence trail**

- [api_response](https://github.com/lmorgadodacosta/iTELL) (source: github_api): stars=4, fork=False, archived=False
- [manifest_line](https://github.com/lmorgadodacosta/iTELL/blob/master/requirements.txt) (source: github_api): mammoth
- [code_permalink](https://github.com/lmorgadodacosta/iTELL/blob/3c027d19b352c3167dffb24052def82631c0e947/lcc.py) (source: github_api): import mammoth  # to parse the docx into html import lxml.html  # to manipulate the html
- [other](https://github.com/lmorgadodacosta/iTELL/tree/master/templates) (source: github_api): directory templates/ present

### 126. codion-is/codion

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

### 127. wocommunity/wonder

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

### 128. BearMelon/thomaslo

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

### 129. basxsoftwareassociation/bread

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

### 130. elapouya/python-docx-template

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

### 131. SuffolkLITLab/docassemble-ALWeaver

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

### 132. OParl/spec

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

### 133. GUMGA/frameworkbackend

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

### 134. Swiss-Armed-Forces/Loom

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

### 135. GUMGA/framework-backend

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

### 136. adfinis/document-merge-service

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

### 137. dkratzert/FinalCif

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

### 138. rte-france/wattelse

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

### 139. AndersonBY/vector-vein

**Repository / product**

- Repository: [https://github.com/andersonby/vector-vein](https://github.com/andersonby/vector-vein)
- Company: Unknown — not stated in the repository
- Product: 🔀 VectorVein
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://vectorvein.ai

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

- Tier 3, `mammoth / python-mammoth`, run `run_1`, window `size:1001..2000`, rank 3
  - Query: `"mammoth" filename:pyproject.toml size:1001..2000`
  - Retrieved 30 of 158 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [backend/pyproject.toml](https://github.com/AndersonBY/vector-vein/blob/main/backend/pyproject.toml)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/AndersonBY/vector-vein/blob/8177b3a45342afd6085f35e9b20fc6914371e138/backend/utilities/file_processing/files.py)

**Evidence trail**

- [api_response](https://github.com/AndersonBY/vector-vein) (source: github_api): stars=939, fork=False, archived=False
- [manifest_line](https://github.com/AndersonBY/vector-vein/blob/main/backend/pyproject.toml) (source: github_api): "mammoth>=1.5.1",
- [code_permalink](https://github.com/AndersonBY/vector-vein/blob/8177b3a45342afd6085f35e9b20fc6914371e138/backend/utilities/file_processing/files.py) (source: github_api): import pypdf import mammoth import openpyxl
- [readme_excerpt](https://github.com/AndersonBY/vector-vein/blob/main/README.md) (source: readme): ![Shortcut Settings](resources/images/shortcut-settings1-en.jpg) To use your own local Stable Diffusion API, you need to add the parameter --api to the startup item of webui-user.bat, that is set COMM

### 140. vitorcastro78/KYC

**Repository / product**

- Repository: [https://github.com/vitorcastro78/kyc](https://github.com/vitorcastro78/kyc)
- Company: Unknown — not stated in the repository
- Product: KYC AI Platform
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://kortexio.io

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| supporting: confirmed generation/conversion code \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

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

- Tier 3, `docx (dolanmiu/docx)`, run `run_1`, window `size:0..250`, rank 30
  - Query: `"docx" filename:package.json size:0..250`
  - Retrieved 30 of 721 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/vitorcastro78/KYC/blob/215d08a084872830ffe136e44a4ce81e6177e842/scripts/generate-docx-docs/md-to-docx.mjs)

**Evidence trail**

- [api_response](https://github.com/vitorcastro78/KYC) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/vitorcastro78/KYC/blob/215d08a084872830ffe136e44a4ce81e6177e842/scripts/generate-docx-docs/md-to-docx.mjs) (source: github_api): NumberFormat, } from "docx";
- [readme_excerpt](https://github.com/vitorcastro78/KYC/blob/main/README.md) (source: readme): GitHub topics (apply after `gh auth login`): pwsh ./scripts/set-github-topics.ps1 Topics for this repo: `kyc`, `aml`, `know-your-customer`, `blazor`, `csharp`, `dotnet`, `postgresql`, `contextmemory`,

### 141. huridocs/pdf-document-layout-analysis

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

### 142. imarthe75/ades-nevadi

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

### 143. conscia/node-tika

**Repository / product**

- Repository: [https://github.com/conscia/node-tika](https://github.com/conscia/node-tika)
- Company: Unknown — not stated in the repository
- Product: node-tika #
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

- Tier 3, `docx (dolanmiu/docx)`, run `run_1`, window `size:501..1000`, rank 26
  - Query: `"docx" filename:package.json size:501..1000`
  - Sampled 30 of 6,624 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 6,624 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `docx (dolanmiu/docx)` (docx, generation) — manifest_declaration — [package.json](https://github.com/conscia/node-tika/blob/master/package.json)
- `docx (dolanmiu/docx)` (docx, generation) — code_import — [code](https://github.com/conscia/node-tika/blob/04be2c5478adf1d923bad351ba96be74a45eda34/test/tika.js)

**Evidence trail**

- [api_response](https://github.com/conscia/node-tika) (source: github_api): stars=2, fork=False, archived=False
- [manifest_line](https://github.com/conscia/node-tika/blob/master/package.json) (source: github_api): "docx",
- [code_permalink](https://github.com/conscia/node-tika/blob/04be2c5478adf1d923bad351ba96be74a45eda34/test/tika.js) (source: github_api): });   });   test('extract from docx', done => {     tika.text('test/data/file.docx', (err, text) => {       assert.ifError(err);       assert.equal(text, 'Just some text.\n');
- [readme_excerpt](https://github.com/conscia/node-tika/blob/master/README.md) (source: readme): `ocrLanguage` to set the language used by Tesseract.

### 144. azavea/raster-vision

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

### 145. dalibo/pandocker

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

### 146. carbon-design-system/carbon

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

### 147. globalis-ms/carbone

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

### 148. gyselroth/balloon

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

### 149. dante-ev/docker-texlive

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

### 150. ad-on-is/rachoon

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

### 151. riclolsen/json-scada

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

### 152. DefinitelyTyped/DefinitelyTyped

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

### 153. HarnessFix/HarnessFix

**Repository / product**

- Repository: [https://github.com/harnessfix/harnessfix](https://github.com/harnessfix/harnessfix)
- Company: Unknown — not stated in the repository
- Product: HarnessFix
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

- Tier 3, `mammoth / python-mammoth`, run `run_1`, window `size:501..1000`, rank 16
  - Query: `"mammoth" filename:pyproject.toml size:501..1000`
  - Retrieved 30 of 107 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [task_agent/final/gaia/pyproject.toml](https://github.com/HarnessFix/HarnessFix/blob/9167a0b9a58748c73b56c3ee04fdc3437ba0c56e/task_agent/final/gaia/pyproject.toml)
- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [task_agent/open_deep_research/pyproject.toml](https://github.com/HarnessFix/HarnessFix/blob/9167a0b9a58748c73b56c3ee04fdc3437ba0c56e/task_agent/open_deep_research/pyproject.toml)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/HarnessFix/HarnessFix/blob/9167a0b9a58748c73b56c3ee04fdc3437ba0c56e/task_agent/final/gaia/src/open_deep_research/scripts/mdconvert.py)
- `mammoth / python-mammoth` (docx, extraction) — code_import — [code](https://github.com/HarnessFix/HarnessFix/blob/9167a0b9a58748c73b56c3ee04fdc3437ba0c56e/task_agent/open_deep_research/src/open_deep_research/scripts/mdconvert.py)

**Evidence trail**

- [api_response](https://github.com/HarnessFix/HarnessFix) (source: github_api): stars=17, fork=False, archived=False
- [manifest_line](https://github.com/HarnessFix/HarnessFix/blob/9167a0b9a58748c73b56c3ee04fdc3437ba0c56e/task_agent/final/gaia/pyproject.toml) (source: github_api): "pathvalidate>=3.2.1",     "puremagic>=1.28",     "pypdf>=5.1.0",     "mammoth>=1.8.0",     "openpyxl",     "xlrd>=2.0.1",     "imageio-ffmpeg>=0.5.1",
- [manifest_line](https://github.com/HarnessFix/HarnessFix/blob/9167a0b9a58748c73b56c3ee04fdc3437ba0c56e/task_agent/open_deep_research/pyproject.toml) (source: github_api): "pathvalidate>=3.2.1",     "puremagic>=1.28",     "pypdf>=5.1.0",     "mammoth>=1.8.0",     "openpyxl",     "python-pptx>=1.0.2",     "tqdm>=4.66.4",
- [code_permalink](https://github.com/HarnessFix/HarnessFix/blob/9167a0b9a58748c73b56c3ee04fdc3437ba0c56e/task_agent/final/gaia/src/open_deep_research/scripts/mdconvert.py) (source: github_api): import mammoth import markdownify
- [code_permalink](https://github.com/HarnessFix/HarnessFix/blob/9167a0b9a58748c73b56c3ee04fdc3437ba0c56e/task_agent/open_deep_research/src/open_deep_research/scripts/mdconvert.py) (source: github_api): import mammoth import markdownify
- [readme_excerpt](https://github.com/HarnessFix/HarnessFix/blob/main/README.md) (source: readme): The public artifact keeps the source code, repair pipeline, analysis utilities, and the initial/final harness snapshots used by the paper.

### 154. MarkEdmondson1234/langchain-github

**Repository / product**

- Repository: [https://github.com/markedmondson1234/langchain-github](https://github.com/markedmondson1234/langchain-github)
- Company: Unknown — not stated in the repository
- Product: Adventures in LLMs
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

- Tier 3, `Unstructured`, run `run_1`, window `size:251..500`, rank 28
  - Query: `"unstructured" filename:requirements.txt size:251..500`
  - Sampled 30 of 4,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 4,256 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/MarkEdmondson1234/langchain-github/blob/main/requirements.txt)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/MarkEdmondson1234/langchain-github/blob/2e471e92dc44c0c7e2935d03bec0756e16bfcc29/debugger.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/MarkEdmondson1234/langchain-github/blob/2e471e92dc44c0c7e2935d03bec0756e16bfcc29/qna/read_repo.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/MarkEdmondson1234/langchain-github/blob/2e471e92dc44c0c7e2935d03bec0756e16bfcc29/encoder_service/publish_to_pubsub_embed.py)

**Evidence trail**

- [api_response](https://github.com/MarkEdmondson1234/langchain-github) (source: github_api): stars=64, fork=False, archived=False
- [manifest_line](https://github.com/MarkEdmondson1234/langchain-github/blob/main/requirements.txt) (source: github_api): unstructured[local-inference]
- [code_permalink](https://github.com/MarkEdmondson1234/langchain-github/blob/2e471e92dc44c0c7e2935d03bec0756e16bfcc29/debugger.py) (source: github_api): # imports import os, shutil import pathlib from langchain.document_loaders.unstructured import UnstructuredFileLoader from langchain.embeddings import OpenAIEmbeddings from langchain.docstore.document
- [code_permalink](https://github.com/MarkEdmondson1234/langchain-github/blob/2e471e92dc44c0c7e2935d03bec0756e16bfcc29/qna/read_repo.py) (source: github_api): from my_llm import standards as my_llm from my_llm.langchain_class import PubSubChatMessageHistory from langchain import PromptTemplate from langchain.document_loaders.unstructured import Unstructured
- [code_permalink](https://github.com/MarkEdmondson1234/langchain-github/blob/2e471e92dc44c0c7e2935d03bec0756e16bfcc29/encoder_service/publish_to_pubsub_embed.py) (source: github_api): # imports import os, shutil, json, re import pathlib from langchain.document_loaders.unstructured import UnstructuredFileLoader from langchain.document_loaders.unstructured import UnstructuredAPIFileL
- [readme_excerpt](https://github.com/MarkEdmondson1234/langchain-github/blob/main/README.md) (source: readme): It also allows you to write the message history to disk in a JSON newline format suitable for BigQuery import, and saves the message history as you go to a [Chroma vectorstore](https://blog.langchain.

### 155. The-Liberal-Labs/Data-Crawler

**Repository / product**

- Repository: [https://github.com/the-liberal-labs/data-crawler](https://github.com/the-liberal-labs/data-crawler)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
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

- Tier 3, `Docling`, run `run_1`, window `size:251..500`, rank 17
  - Query: `"docling" filename:requirements.txt size:251..500`
  - Sampled 30 of 1,026 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,026 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/The-Liberal-Labs/Data-Crawler/blob/5f851a257fc192940bfd261e58a79df47adddcd4/gpu_services/docling_service/main.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/The-Liberal-Labs/Data-Crawler/blob/5f851a257fc192940bfd261e58a79df47adddcd4/gpu_services/docling_service/config.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/The-Liberal-Labs/Data-Crawler/blob/5f851a257fc192940bfd261e58a79df47adddcd4/gpu_services/docling_service/processing.py)
- `Docling` (other_processing, extraction) — manifest_declaration — [gpu_services/docling_service/requirements.txt](https://github.com/The-Liberal-Labs/Data-Crawler/blob/5f851a257fc192940bfd261e58a79df47adddcd4/gpu_services/docling_service/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/The-Liberal-Labs/Data-Crawler) (source: github_api): stars=0, fork=False, archived=False
- [code_permalink](https://github.com/The-Liberal-Labs/Data-Crawler/blob/5f851a257fc192940bfd261e58a79df47adddcd4/gpu_services/docling_service/main.py) (source: github_api): # gpu_services/docling_service/main.py """ Document Processing Service using Docling. Simplified for Docling 2.x API. """
- [code_permalink](https://github.com/The-Liberal-Labs/Data-Crawler/blob/5f851a257fc192940bfd261e58a79df47adddcd4/gpu_services/docling_service/config.py) (source: github_api): # gpu_services/docling_service/config.py from pydantic_settings import BaseSettings, SettingsConfigDict
- [code_permalink](https://github.com/The-Liberal-Labs/Data-Crawler/blob/5f851a257fc192940bfd261e58a79df47adddcd4/gpu_services/docling_service/processing.py) (source: github_api): # gpu_services/docling_service/processing.py """ Document processing service using Docling. Updated for Docling 2.x API. """
- [manifest_line](https://github.com/The-Liberal-Labs/Data-Crawler/blob/5f851a257fc192940bfd261e58a79df47adddcd4/gpu_services/docling_service/requirements.txt) (source: github_api): # Docling Service Requirements # For Linux with NVIDIA GPU (8GB VRAM)
- [readme_excerpt](https://github.com/The-Liberal-Labs/Data-Crawler/blob/main/README.md) (source: readme): **Document Processing (Docling)**: Local service for secure, robust document extraction (text, tables, images).

### 156. jimmymnt/pim-e-shop

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

### 157. Simon-Drohsen/pimcore-certificate

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

### 158. JanBancerewicz/pimcoretask

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

### 159. datnv41001/pimcore

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

### 160. LevDmitriev/dc-pimcore-demo

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

### 161. vivliostyle/vivliostyle-cli

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

### 162. l4houx/recipe

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

### 163. flopach/create-your-own-api-assistant-cisco-catalyst-center

**Repository / product**

- Repository: [https://github.com/flopach/create-your-own-api-assistant-cisco-catalyst-center](https://github.com/flopach/create-your-own-api-assistant-cisco-catalyst-center)
- Company: Cisco
- Product: Create your own API Assistant with Cisco Catalyst Center
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; contributor_count not collected

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

- Tier 3, `PyMuPDF (fitz)`, run `run_1`, window `size:251..500`, rank 11
  - Query: `"PyMuPDF" filename:pyproject.toml size:251..500`
  - Sampled 30 of 2,508 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,508 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [pyproject.toml](https://github.com/flopach/create-your-own-api-assistant-cisco-catalyst-center/blob/main/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/flopach/create-your-own-api-assistant-cisco-catalyst-center) (source: github_api): stars=18, fork=False, archived=False
- [readme_excerpt](https://github.com/flopach/create-your-own-api-assistant-cisco-catalyst-center/blob/main/README.md) (source: readme): company stated as 'Cisco'
- [manifest_line](https://github.com/flopach/create-your-own-api-assistant-cisco-catalyst-center/blob/main/pyproject.toml) (source: github_api): pymupdf = "^1.24.2"
- [readme_excerpt](https://github.com/flopach/create-your-own-api-assistant-cisco-catalyst-center/blob/main/README.md) (source: readme): include authentication"** ![](images/example_eos.png) **User query: "export a summary of all clients"** ![](images/example_clients_summary.png) **User query: "get me a list of all devices and export t

### 164. marlian/claude-qdrant-mcp

**Repository / product**

- Repository: [https://github.com/marlian/claude-qdrant-mcp](https://github.com/marlian/claude-qdrant-mcp)
- Company: Unknown — not stated in the repository
- Product: 🚀 Qdrant MCP Hybrid - Ultimate RAG System
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

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

- Tier 3, `mammoth / python-mammoth`, run `run_1`, window `size:1001..2000`, rank 18
  - Query: `"mammoth" filename:package.json size:1001..2000`
  - Sampled 30 of 10,464 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 10,464 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [package.json](https://github.com/marlian/claude-qdrant-mcp/blob/main/package.json)

**Evidence trail**

- [api_response](https://github.com/marlian/claude-qdrant-mcp) (source: github_api): stars=13, fork=False, archived=False
- [manifest_line](https://github.com/marlian/claude-qdrant-mcp/blob/main/package.json) (source: github_api): "mammoth": "^1.9.1",
- [readme_excerpt](https://github.com/marlian/claude-qdrant-mcp/blob/main/README.md) (source: readme): { "query": "machine learning implementation", "client": "research", "source": "/path/to/specific/document.md",  // optional "limit": 5 } Search across all clients and collections.

### 165. abgulati/Privion

**Repository / product**

- Repository: [https://github.com/abgulati/privion](https://github.com/abgulati/privion)
- Company: Unknown — not stated in the repository
- Product: Privion
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.youtube.com/watch?v=2CpgqA_YjWU&list=PLGhCeHSq43a4H7N-t_49SDfwP9LpZXED-

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: readme_describes_product, application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=1, readme_describes_product=false, application_code_exists=false, document_functionality_in_production_code=true \| supporting: template_directory_present=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 13/100 (a score, not a probability)
- Raw weighted score: 0.65 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 1 |
| Business criticality | 0 |
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

- Tier 3, `Docling`, run `run_1`, window `size:1001..2000`, rank 30
  - Query: `"docling" filename:requirements.txt size:1001..2000`
  - Retrieved 30 of 371 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Docling` (other_processing, extraction) — manifest_declaration — [installer/requirements_mac.txt](https://github.com/abgulati/Privion/blob/4292b5a756c1db2ad1026f95e33e57a752be34ea/installer/requirements_mac.txt)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/abgulati/Privion/blob/4292b5a756c1db2ad1026f95e33e57a752be34ea/web_app/privion_config_concierge.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/abgulati/Privion/blob/4292b5a756c1db2ad1026f95e33e57a752be34ea/web_app/static/js/save-config.js)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/abgulati/Privion/blob/4292b5a756c1db2ad1026f95e33e57a752be34ea/web_app/static/js/dom-loader.js)

**Evidence trail**

- [api_response](https://github.com/abgulati/Privion) (source: github_api): stars=3, fork=False, archived=False
- [manifest_line](https://github.com/abgulati/Privion/blob/4292b5a756c1db2ad1026f95e33e57a752be34ea/installer/requirements_mac.txt) (source: github_api): blobfile>=3.0.0 chromadb>=1.0.12 diffusers>=0.33.1 docling>=2.36.1 falkordb>=1.1.2 Flask>=3.1.1 Flask-Cors>=6.0.0
- [code_permalink](https://github.com/abgulati/Privion/blob/4292b5a756c1db2ad1026f95e33e57a752be34ea/web_app/privion_config_concierge.py) (source: github_api): 'ocr_service_choice':'Docling',                 'backup_ocr_service_choice':'Backup-Docling',                 'docling_pipeline':'standard',
- [code_permalink](https://github.com/abgulati/Privion/blob/4292b5a756c1db2ad1026f95e33e57a752be34ea/web_app/static/js/save-config.js) (source: github_api): const update_kosmos_url_config = document.getElementById('update_kosmos_url_config').checked;     const update_docling_config = document.getElementById('update_docling_config').checked;
- [code_permalink](https://github.com/abgulati/Privion/blob/4292b5a756c1db2ad1026f95e33e57a752be34ea/web_app/static/js/dom-loader.js) (source: github_api): 'docling_vlm_model',         'docling_do_ocr',         'docling_force_full_page_ocr',
- [other](https://github.com/abgulati/Privion/tree/main/documents) (source: github_api): directory documents/ present

### 166. networktocode/yangify

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

### 167. gitrgoliveira/bracket-creator

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

### 168. getumbrel/umbrel-apps

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

### 169. Paparusi/legal-ai-agent

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

### 170. netease-youdao/QAnything

**Repository / product**

- Repository: [https://github.com/netease-youdao/qanything](https://github.com/netease-youdao/qanything)
- Company: Unknown — not stated in the repository
- Product: **Q**uestion and **A**nswer based on **Anything**
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://qanything.ai

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

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

- Tier 3, `Unstructured`, run `run_1`, window `size:1001..2000`, rank 2
  - Query: `"unstructured" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 1,308 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,308 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/netease-youdao/QAnything/blob/qanything-v2/requirements.txt)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/netease-youdao/QAnything/blob/65de10426b99d5945b8c616a4814afa5a92826cb/qanything_kernel/utils/loader/pdf_loader.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/netease-youdao/QAnything/blob/65de10426b99d5945b8c616a4814afa5a92826cb/qanything_kernel/utils/loader/image_loader.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/netease-youdao/QAnything/blob/65de10426b99d5945b8c616a4814afa5a92826cb/qanything_kernel/utils/loader/audio_loader.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/netease-youdao/QAnything/blob/65de10426b99d5945b8c616a4814afa5a92826cb/qanything_kernel/utils/loader/__init__.py)

**Evidence trail**

- [api_response](https://github.com/netease-youdao/QAnything) (source: github_api): stars=14074, fork=False, archived=False
- [manifest_line](https://github.com/netease-youdao/QAnything/blob/qanything-v2/requirements.txt) (source: github_api): unstructured==0.12.4
- [code_permalink](https://github.com/netease-youdao/QAnything/blob/65de10426b99d5945b8c616a4814afa5a92826cb/qanything_kernel/utils/loader/pdf_loader.py) (source: github_api): """Loader that loads image files.""" from typing import List, Callable from langchain.document_loaders.unstructured import UnstructuredFileLoader from unstructured.partition.text import partition
- [code_permalink](https://github.com/netease-youdao/QAnything/blob/65de10426b99d5945b8c616a4814afa5a92826cb/qanything_kernel/utils/loader/image_loader.py) (source: github_api): """Loader that loads image files.""" from typing import List, Callable from langchain.document_loaders.unstructured import UnstructuredFileLoader from unstructured.partition.text import partition
- [code_permalink](https://github.com/netease-youdao/QAnything/blob/65de10426b99d5945b8c616a4814afa5a92826cb/qanything_kernel/utils/loader/audio_loader.py) (source: github_api): import torch from langchain.document_loaders.unstructured import UnstructuredFileLoader import os
- [code_permalink](https://github.com/netease-youdao/QAnything/blob/65de10426b99d5945b8c616a4814afa5a92826cb/qanything_kernel/utils/loader/__init__.py) (source: github_api): from .image_loader import UnstructuredPaddleImageLoader from .pdf_loader import UnstructuredPaddlePDFLoader __all__ = [     "UnstructuredPaddleImageLoader",     "UnstructuredPaddlePDFLoader", ]
- [readme_excerpt](https://github.com/netease-youdao/QAnything/blob/qanything-v2/README.md) (source: readme): This improvement prevents interruptions in meaning caused by logical segmentation when parsing long tables.

### 171. Hellvisback365/datapizza-ai-main

**Repository / product**

- Repository: [https://github.com/hellvisback365/datapizza-ai-main](https://github.com/hellvisback365/datapizza-ai-main)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| unknown: industry_category=unknown; contributor_count not collected

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

- Tier 3, `Docling`, run `run_1`, window `size:1001..2000`, rank 26
  - Query: `"docling" filename:pyproject.toml size:1001..2000`
  - Sampled 30 of 1,008 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,008 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Docling` (other_processing, extraction) — manifest_declaration — [pyproject.toml](https://github.com/Hellvisback365/datapizza-ai-main/blob/main/pyproject.toml)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/Hellvisback365/datapizza-ai-main/blob/0168326c3a0d979a8eb94468084b49567de3e3fd/datapizza-ai-modules/parsers/docling/datapizza/modules/parsers/docling/utils.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/Hellvisback365/datapizza-ai-main/blob/0168326c3a0d979a8eb94468084b49567de3e3fd/datapizza-ai-modules/parsers/docling/datapizza/modules/parsers/docling/__init__.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/Hellvisback365/datapizza-ai-main/blob/0168326c3a0d979a8eb94468084b49567de3e3fd/datapizza-ai-modules/parsers/docling/datapizza/modules/parsers/docling/ocr_options.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/Hellvisback365/datapizza-ai-main/blob/0168326c3a0d979a8eb94468084b49567de3e3fd/datapizza-ai-modules/parsers/docling/datapizza/modules/parsers/docling/docling_parser.py)

**Evidence trail**

- [api_response](https://github.com/Hellvisback365/datapizza-ai-main) (source: github_api): stars=0, fork=False, archived=False
- [readme_excerpt](https://github.com/Hellvisback365/datapizza-ai-main/blob/main/README.md) (source: readme): company stated as 'Engineers'
- [manifest_line](https://github.com/Hellvisback365/datapizza-ai-main/blob/main/pyproject.toml) (source: github_api): #"datapizza-ai-modules/parsers/docling",
- [code_permalink](https://github.com/Hellvisback365/datapizza-ai-main/blob/0168326c3a0d979a8eb94468084b49567de3e3fd/datapizza-ai-modules/parsers/docling/datapizza/modules/parsers/docling/utils.py) (source: github_api): def extract_media_from_docling_bbox(     bbox: dict,     file_path: str,
- [code_permalink](https://github.com/Hellvisback365/datapizza-ai-main/blob/0168326c3a0d979a8eb94468084b49567de3e3fd/datapizza-ai-modules/parsers/docling/datapizza/modules/parsers/docling/__init__.py) (source: github_api): from .docling_parser import DoclingParser from .ocr_options import OCREngine, OCROptions __all__ = ["DoclingParser", "OCREngine", "OCROptions"]
- [code_permalink](https://github.com/Hellvisback365/datapizza-ai-main/blob/0168326c3a0d979a8eb94468084b49567de3e3fd/datapizza-ai-modules/parsers/docling/datapizza/modules/parsers/docling/ocr_options.py) (source: github_api): """ OCR (Optical Character Recognition) configuration for Docling parser.
- [code_permalink](https://github.com/Hellvisback365/datapizza-ai-main/blob/0168326c3a0d979a8eb94468084b49567de3e3fd/datapizza-ai-modules/parsers/docling/datapizza/modules/parsers/docling/docling_parser.py) (source: github_api): from docling.datamodel.pipeline_options import PdfPipelineOptions from docling.document_converter import (     DocumentConverter,
- [readme_excerpt](https://github.com/Hellvisback365/datapizza-ai-main/blob/main/README.md) (source: readme): Built by Engineers, trusted by Engineers.

### 172. VIDA-NYU/ache

**Repository / product**

- Repository: [https://github.com/vida-nyu/ache](https://github.com/vida-nyu/ache)
- Company: Unknown — not stated in the repository
- Product: ACHE Focused Crawler
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: http://ache.readthedocs.io

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

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

- Tier 3, `Apache Tika`, run `run_1`, window `size:1001..2000`, rank 10
  - Query: `"tika" filename:build.gradle size:1001..2000`
  - Sampled 30 of 1,282 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,282 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/VIDA-NYU/ache/blob/81b29c09bd6cde03e97cad174959a660620bff3c/ache-tools/src/main/java/achecrawler/memex/cdr/TikaExtractor.java)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/VIDA-NYU/ache/blob/81b29c09bd6cde03e97cad174959a660620bff3c/ache-tools/src/main/java/achecrawler/memex/cdr/CDR2Document.java)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/VIDA-NYU/ache/blob/81b29c09bd6cde03e97cad174959a660620bff3c/ache-tools/src/main/java/achecrawler/memex/cdr/CDR3Document.java)
- `Apache Tika` (other_processing, extraction) — code_import — [code](https://github.com/VIDA-NYU/ache/blob/81b29c09bd6cde03e97cad174959a660620bff3c/ache-tools/src/main/java/achecrawler/memex/cdr/CDRDocumentBuilder.java)

**Evidence trail**

- [api_response](https://github.com/VIDA-NYU/ache) (source: github_api): stars=486, fork=False, archived=False
- [code_permalink](https://github.com/VIDA-NYU/ache/blob/81b29c09bd6cde03e97cad174959a660620bff3c/ache-tools/src/main/java/achecrawler/memex/cdr/TikaExtractor.java) (source: github_api): import java.util.HashMap; import java.util.Map; import org.apache.tika.config.TikaConfig; import org.apache.tika.detect.Detector; import org.apache.tika.exception.TikaException; import org.apache.tik
- [code_permalink](https://github.com/VIDA-NYU/ache/blob/81b29c09bd6cde03e97cad174959a660620bff3c/ache-tools/src/main/java/achecrawler/memex/cdr/CDR2Document.java) (source: github_api): import org.apache.commons.codec.digest.DigestUtils; import org.apache.tika.mime.MediaType;
- [code_permalink](https://github.com/VIDA-NYU/ache/blob/81b29c09bd6cde03e97cad174959a660620bff3c/ache-tools/src/main/java/achecrawler/memex/cdr/CDR3Document.java) (source: github_api): import org.apache.commons.codec.digest.DigestUtils; import org.apache.tika.mime.MediaType;
- [code_permalink](https://github.com/VIDA-NYU/ache/blob/81b29c09bd6cde03e97cad174959a660620bff3c/ache-tools/src/main/java/achecrawler/memex/cdr/CDRDocumentBuilder.java) (source: github_api): //import org.apache.commons.codec.digest.DigestUtils; //import org.apache.tika.mime.MediaType; //
- [readme_excerpt](https://github.com/VIDA-NYU/ache/blob/master/README.md) (source: readme): WARC - stores data using the standard format used by the Web Archive and Common Crawl.

### 173. sitepoint-editors/awesome-symfony

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

### 174. dragonfore4/deka-download

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

### 175. modrinth/code

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

### 176. Probesys/lotemplate

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

### 177. MVladislav/vm-docker-collection

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

### 178. ministryofjustice/send-legal-mail-to-prisons

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

### 179. notadev-iamaura/OneRAG

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

### 180. solidtime-io/solidtime

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

### 181. unitedworldwrestling/arena-public

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

### 182. YYC-Cube/YYC3-Knowledge-Base

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

### 183. georgemarian98/home-server

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

### 184. tjmlabs/ColiVara

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

### 185. samvera/hydra-derivatives

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

### 186. AppCivico/smae

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

### 187. mperreir/Hyblab2023

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

### 188. open-edge-platform/edge-ai-suites

**Repository / product**

- Repository: [https://github.com/open-edge-platform/edge-ai-suites](https://github.com/open-edge-platform/edge-ai-suites)
- Company: Unknown — not stated in the repository
- Product: Edge-AI-Suites
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

- Tier 3, `Unstructured`, run `run_1`, window `size:1001..2000`, rank 20
  - Query: `"unstructured" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 1,308 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,308 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Unstructured` (other_processing, extraction) — manifest_declaration — [education-ai-suite/smart-classroom/requirements.txt](https://github.com/open-edge-platform/edge-ai-suites/blob/72d68075c7171d887ba9b163e415d72ada03f18d/education-ai-suite/smart-classroom/requirements.txt)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/open-edge-platform/edge-ai-suites/blob/72d68075c7171d887ba9b163e415d72ada03f18d/education-ai-suite/smart-classroom/content_search/providers/file_ingest_and_retrieve/utils.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/open-edge-platform/edge-ai-suites/blob/72d68075c7171d887ba9b163e415d72ada03f18d/education-ai-suite/smart-classroom/content_search/providers/file_ingest_and_retrieve/document_parser.py)

**Evidence trail**

- [api_response](https://github.com/open-edge-platform/edge-ai-suites) (source: github_api): stars=128, fork=False, archived=False
- [manifest_line](https://github.com/open-edge-platform/edge-ai-suites/blob/72d68075c7171d887ba9b163e415d72ada03f18d/education-ai-suite/smart-classroom/requirements.txt) (source: github_api): python-docx==1.2.0 docx2txt==0.9 python-magic==0.4.27 unstructured[all-docs]==0.18.32 lmdb==1.7.3 attrdict==2.0.1 lxml>=6.1.0
- [code_permalink](https://github.com/open-edge-platform/edge-ai-suites/blob/72d68075c7171d887ba9b163e415d72ada03f18d/education-ai-suite/smart-classroom/content_search/providers/file_ingest_and_retrieve/utils.py) (source: github_api): from PIL import Image as PILImage from unstructured.documents.elements import ElementMetadata, Image from unstructured.partition.docx import DocxPartitionerOptions from docx.text.paragraph import Par
- [code_permalink](https://github.com/open-edge-platform/edge-ai-suites/blob/72d68075c7171d887ba9b163e415d72ada03f18d/education-ai-suite/smart-classroom/content_search/providers/file_ingest_and_retrieve/document_parser.py) (source: github_api): from llama_index.core.node_parser import SentenceSplitter, SemanticSplitterNodeParser from llama_index.core.schema import BaseNode, TextNode from llama_index.readers.file import UnstructuredReader fro
- [readme_excerpt](https://github.com/open-edge-platform/edge-ai-suites/blob/main/README.md) (source: readme): [The Health And Life Sciences AI Suite](health-and-life-sciences-ai-suite) is a solution for supporting the healthcare field with AI software tools covering a wide range of monitoring and analysis fea

### 189. NVIDIA/workbench-example-agentic-rag

**Repository / product**

- Repository: [https://github.com/nvidia/workbench-example-agentic-rag](https://github.com/nvidia/workbench-example-agentic-rag)
- Company: Unknown — not stated in the repository
- Product: Agentic RAG - Web Search with Accuracy and Hallucination Controls
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

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

- Tier 3, `Unstructured`, run `run_1`, window `size:251..500`, rank 10
  - Query: `"unstructured" filename:requirements.txt size:251..500`
  - Sampled 30 of 4,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 4,256 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/NVIDIA/workbench-example-agentic-rag/blob/main/requirements.txt)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/NVIDIA/workbench-example-agentic-rag/blob/1f05c9c255a3d1c3ea120deb3a3853147f098de4/code/chatui/utils/database.py)

**Evidence trail**

- [api_response](https://github.com/NVIDIA/workbench-example-agentic-rag) (source: github_api): stars=166, fork=False, archived=False
- [manifest_line](https://github.com/NVIDIA/workbench-example-agentic-rag/blob/main/requirements.txt) (source: github_api): unstructured[pdf]==0.16.17
- [code_permalink](https://github.com/NVIDIA/workbench-example-agentic-rag/blob/1f05c9c255a3d1c3ea120deb3a3853147f098de4/code/chatui/utils/database.py) (source: github_api): WebBaseLoader,     UnstructuredPDFLoader,     TextLoader,
- [readme_excerpt](https://github.com/NVIDIA/workbench-example-agentic-rag/blob/main/README.md) (source: readme): Configure the chat app to use the self-hosted endpoint.

### 190. AidenFaulconer/AI.DEN

**Repository / product**

- Repository: [https://github.com/aidenfaulconer/ai.den](https://github.com/aidenfaulconer/ai.den)
- Company: Unknown — not stated in the repository
- Product: AI.DEN — Local AI Cluster
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=true \| unknown: company_name=null; contributor_count not collected

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

- Tier 3, `Unstructured`, run `run_1`, window `size:501..1000`, rank 24
  - Query: `"unstructured" filename:pyproject.toml size:501..1000`
  - Sampled 30 of 1,512 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,512 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/AidenFaulconer/AI.DEN/blob/6b1597bc263ab1d262d82d4f881a318b0268f263/unsloth/studio/backend/plugins/data-designer-unstructured-seed/src/data_designer_unstructured_seed/impl.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/AidenFaulconer/AI.DEN/blob/6b1597bc263ab1d262d82d4f881a318b0268f263/unsloth/studio/backend/plugins/data-designer-unstructured-seed/src/data_designer_unstructured_seed/config.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/AidenFaulconer/AI.DEN/blob/6b1597bc263ab1d262d82d4f881a318b0268f263/unsloth/studio/backend/plugins/data-designer-unstructured-seed/src/data_designer_unstructured_seed/plugin.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/AidenFaulconer/AI.DEN/blob/6b1597bc263ab1d262d82d4f881a318b0268f263/unsloth/studio/backend/plugins/data-designer-unstructured-seed/src/data_designer_unstructured_seed/__init__.py)
- `Unstructured` (other_processing, extraction) — code_import — [code](https://github.com/AidenFaulconer/AI.DEN/blob/6b1597bc263ab1d262d82d4f881a318b0268f263/unsloth/studio/backend/plugins/data-designer-unstructured-seed/src/data_designer_unstructured_seed/chunking.py)

**Evidence trail**

- [api_response](https://github.com/AidenFaulconer/AI.DEN) (source: github_api): stars=2, fork=False, archived=False
- [code_permalink](https://github.com/AidenFaulconer/AI.DEN/blob/6b1597bc263ab1d262d82d4f881a318b0268f263/unsloth/studio/backend/plugins/data-designer-unstructured-seed/src/data_designer_unstructured_seed/impl.py) (source: github_api): def get_dataset_uri(self) -> str:         from .chunking import materialize_multi_file_unstructured_seed         import json as json_mod
- [code_permalink](https://github.com/AidenFaulconer/AI.DEN/blob/6b1597bc263ab1d262d82d4f881a318b0268f263/unsloth/studio/backend/plugins/data-designer-unstructured-seed/src/data_designer_unstructured_seed/config.py) (source: github_api): class UnstructuredSeedSource(SeedSource):     seed_type: Literal["unstructured"] = "unstructured"     paths: list[str] = Field(min_length = 1)     @model_validator(mode = "before")
- [code_permalink](https://github.com/AidenFaulconer/AI.DEN/blob/6b1597bc263ab1d262d82d4f881a318b0268f263/unsloth/studio/backend/plugins/data-designer-unstructured-seed/src/data_designer_unstructured_seed/plugin.py) (source: github_api): from data_designer.plugins.plugin import Plugin, PluginType unstructured_seed_plugin = Plugin(     impl_qualified_name = "data_designer_unstructured_seed.impl.UnstructuredSeedReader",     config_qua
- [code_permalink](https://github.com/AidenFaulconer/AI.DEN/blob/6b1597bc263ab1d262d82d4f881a318b0268f263/unsloth/studio/backend/plugins/data-designer-unstructured-seed/src/data_designer_unstructured_seed/__init__.py) (source: github_api): from .chunking import (     DEFAULT_CHUNK_OVERLAP,     DEFAULT_CHUNK_SIZE,     build_unstructured_preview_rows,     materialize_unstructured_seed_dataset,     resolve_chunking, )
- [code_permalink](https://github.com/AidenFaulconer/AI.DEN/blob/6b1597bc263ab1d262d82d4f881a318b0268f263/unsloth/studio/backend/plugins/data-designer-unstructured-seed/src/data_designer_unstructured_seed/chunking.py) (source: github_api): _MIN_BREAK_RATIO = 0.6 _CACHE_DIR = unstructured_seed_cache_root()
- [readme_excerpt](https://github.com/AidenFaulconer/AI.DEN/blob/main/README.md) (source: readme): A self-hosted private AI cluster on your laptop via Docker, with a **`model-router`** that injects a configurable **`prompt-pipeline`** (optional **claw-stage** prose + **[Caveman](https://github.com/

### 191. paulgessinger/swift-paperless

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

### 192. selkies-project/docker-selkies-glx-desktop

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

### 193. JoachimSchaeffer/AttackSelection

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

### 194. makinacorpus/convertit

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

### 195. octos-org/octos

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

### 196. CitizenLabDotCo/citizenlab

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

### 197. CivilHub/CivilHub

**Repository / product**

- Repository: [https://github.com/civilhub/civilhub](https://github.com/civilhub/civilhub)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://civilhub.org

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| supporting: template_directory_present=true \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 7/100 (a score, not a probability)
- Raw weighted score: 0.35 / 5
- Confidence: low

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 1 |
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

- Tier 3, `ReportLab`, run `run_1`, window `size:501..1000`, rank 7
  - Query: `"reportlab" filename:requirements.txt size:501..1000`
  - Sampled 30 of 11,552 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 11,552 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `ReportLab` (pdf, generation) — manifest_declaration — [requirements.txt](https://github.com/CivilHub/CivilHub/blob/master/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/CivilHub/CivilHub) (source: github_api): stars=109, fork=False, archived=False
- [manifest_line](https://github.com/CivilHub/CivilHub/blob/master/requirements.txt) (source: github_api): reportlab>=2.7,<3
- [other](https://github.com/CivilHub/CivilHub/tree/master/templates) (source: github_api): directory templates/ present
- [readme_excerpt](https://github.com/CivilHub/CivilHub/blob/master/README.md) (source: readme): Due to limitations in Google Maps (not a good solution for Clustering and displaying more than 100 thousand points on a map).

### 198. ppc64le/pyeco

**Repository / product**

- Repository: [https://github.com/ppc64le/pyeco](https://github.com/ppc64le/pyeco)
- Company: Unknown — not stated in the repository
- Product: Welcome to IBM Power - Optimized Python Wheels 🚀
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: medium
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=true, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| unknown: industry_category=unknown; company_name=null; contributor_count not collected

**Score**

- Score: 6/100 (a score, not a probability)
- Raw weighted score: 0.30 / 5
- Confidence: medium

| Dimension | Score (0-5) |
|---|---:|
| Document volume *(unknown)* | 0 |
| Document complexity | 0 |
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

- Tier 3, `Docling`, run `run_1`, window `size:0..250`, rank 6
  - Query: `"docling" filename:requirements.txt size:0..250`
  - Sampled 30 of 1,524 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,524 figure describes how many repositories matched, not how many were inspected.
- Tier 3, `Docling`, run `run_1`, window `size:501..1000`, rank 3
  - Query: `"docling" filename:requirements.txt size:501..1000`
  - Retrieved 30 of 740 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/ppc64le/pyeco/blob/023f1f4b50017c2e73857b9ebd21ddf6b19e864b/examples/Python3.12/Docling-example/docling_example.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/ppc64le/pyeco/blob/023f1f4b50017c2e73857b9ebd21ddf6b19e864b/examples/Python3.11/Docling-example/docling_example.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/ppc64le/pyeco/blob/023f1f4b50017c2e73857b9ebd21ddf6b19e864b/examples/Python3.11/docling-parse-example/docling_parse_example.py)
- `Docling` (other_processing, extraction) — code_import — [code](https://github.com/ppc64le/pyeco/blob/023f1f4b50017c2e73857b9ebd21ddf6b19e864b/examples/Python3.12/docling-parse-example/docling_parse_example.py)

**Evidence trail**

- [api_response](https://github.com/ppc64le/pyeco) (source: github_api): stars=33, fork=False, archived=False
- [code_permalink](https://github.com/ppc64le/pyeco/blob/023f1f4b50017c2e73857b9ebd21ddf6b19e864b/examples/Python3.12/Docling-example/docling_example.py) (source: github_api): """ Docling Package Example - PDF Document Conversion with Granite Docling (local, inline) This file mirrors the pattern used in the Granite-with-pytorch example: the model is loaded **locally** usin
- [code_permalink](https://github.com/ppc64le/pyeco/blob/023f1f4b50017c2e73857b9ebd21ddf6b19e864b/examples/Python3.11/Docling-example/docling_example.py) (source: github_api): """ Docling Package Example - PDF Document Conversion with Granite Docling (local, inline) This file mirrors the pattern used in the Granite-with-pytorch example: the model is loaded **locally** usin
- [code_permalink](https://github.com/ppc64le/pyeco/blob/023f1f4b50017c2e73857b9ebd21ddf6b19e864b/examples/Python3.11/docling-parse-example/docling_parse_example.py) (source: github_api): from typing import List, Dict from docling_parse.pdf_parser import DoclingPdfParser
- [code_permalink](https://github.com/ppc64le/pyeco/blob/023f1f4b50017c2e73857b9ebd21ddf6b19e864b/examples/Python3.12/docling-parse-example/docling_parse_example.py) (source: github_api): from typing import List, Dict from docling_parse.pdf_parser import DoclingPdfParser
- [readme_excerpt](https://github.com/ppc64le/pyeco/blob/main/README.md) (source: readme): 📝 **Note: Wheel Versions and Suffixes** IBM Power wheels are published in two forms: The **suffix** (`ppc64le1`, `ppc64le2`, …) is incremented each time a wheel is rebuilt for the same upstream versio

### 199. Scouterna/skojjt

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

### 200. philips-software/amp-devcontainer

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

### 201. JetBrains/compose-multiplatform

**Repository / product**

- Repository: [https://github.com/jetbrains/compose-multiplatform](https://github.com/jetbrains/compose-multiplatform)
- Company: JetBrains
- Product: Unknown
- Industry: software_technical_docs (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://jetbrains.com/lp/compose-multiplatform

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; contributor_count not collected

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

- Tier 3, `Apache Tika`, run `run_1`, window `size:1001..2000`, rank 2
  - Query: `"tika" filename:build.gradle size:1001..2000`
  - Sampled 30 of 1,282 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,282 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Apache Tika` (other_processing, extraction) — manifest_declaration — [ci/build-helpers/publishing/build.gradle.kts](https://github.com/JetBrains/compose-multiplatform/blob/a933da08f5d5fd24098b0e0370983a1104b7bc9b/ci/build-helpers/publishing/build.gradle.kts)

**Evidence trail**

- [api_response](https://github.com/JetBrains/compose-multiplatform) (source: github_api): stars=19308, fork=False, archived=False
- [readme_excerpt](https://github.com/JetBrains/compose-multiplatform/blob/master/README.md) (source: readme): company stated as 'JetBrains'
- [manifest_line](https://github.com/JetBrains/compose-multiplatform/blob/a933da08f5d5fd24098b0e0370983a1104b7bc9b/ci/build-helpers/publishing/build.gradle.kts) (source: github_api): implementation("io.ktor:ktor-client-core:3.1.3")     implementation("io.ktor:ktor-client-cio:3.1.3")     implementation("io.ktor:ktor-client-okhttp:3.1.3")     implementation("org.apache.tika:tika
- [readme_excerpt](https://github.com/JetBrains/compose-multiplatform/blob/master/README.md) (source: readme): Compose Multiplatform for web is based on [Kotlin/Wasm](https://kotl.in/wasm), the newest target for Kotlin Multiplatform projects.

### 202. buildbyadnan/zero-day-codebase

**Repository / product**

- Repository: [https://github.com/buildbyadnan/zero-day-codebase](https://github.com/buildbyadnan/zero-day-codebase)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://zero-day-web.ghost-server.workers.dev/

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=true, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

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

- Tier 3, `mammoth / python-mammoth`, run `run_1`, window `size:501..1000`, rank 24
  - Query: `"mammoth" filename:package.json size:501..1000`
  - Sampled 30 of 9,056 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 9,056 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `mammoth / python-mammoth` (docx, extraction) — manifest_declaration — [package.json](https://github.com/buildbyadnan/zero-day-codebase/blob/main/package.json)

**Evidence trail**

- [api_response](https://github.com/buildbyadnan/zero-day-codebase) (source: github_api): stars=4, fork=False, archived=False
- [manifest_line](https://github.com/buildbyadnan/zero-day-codebase/blob/main/package.json) (source: github_api): "mammoth": "^1.10.0",
- [readme_excerpt](https://github.com/buildbyadnan/zero-day-codebase/blob/main/README.md) (source: readme): nx run-many --target=build --projects=web,other-app This command allows you to run the `build` target for both the `web` project and another app in the workspace.

### 203. FlagAI-Open/Aquila2

**Repository / product**

- Repository: [https://github.com/flagai-open/aquila2](https://github.com/flagai-open/aquila2)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

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

- Tier 3, `Unstructured`, run `run_1`, window `size:1001..2000`, rank 21
  - Query: `"unstructured" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 1,308 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,308 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Unstructured` (other_processing, extraction) — manifest_declaration — [examples/rag_pipe/requirements.txt](https://github.com/FlagAI-Open/Aquila2/blob/4b8250a703cc8330d0e2c66ddfb09363fd446cf8/examples/rag_pipe/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/FlagAI-Open/Aquila2) (source: github_api): stars=447, fork=False, archived=False
- [manifest_line](https://github.com/FlagAI-Open/Aquila2/blob/4b8250a703cc8330d0e2c66ddfb09363fd446cf8/examples/rag_pipe/requirements.txt) (source: github_api): paddleocr~=2.6.1.3 langchain==0.0.174 transformers==4.29.1 unstructured[local-inference] layoutparser[layoutmodels,tesseract] nltk~=3.8.1 sentence-transformers
- [readme_excerpt](https://github.com/FlagAI-Open/Aquila2/blob/main/README.md) (source: readme): 2023.11.10 🔥 Based on the open-source large language model (Aquila2) and embedding model (BGE) released by BAAI, [rag_pipe](./examples/rag_pipe) a solution for a question-answering application based o

### 204. Sshyamsundar6887/Clausewise

**Repository / product**

- Repository: [https://github.com/sshyamsundar6887/clausewise](https://github.com/sshyamsundar6887/clausewise)
- Company: Unknown — not stated in the repository
- Product: ClauseWise - AI-Powered Legal Document Analyzer
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
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

- Tier 3, `pdf2docx`, run `run_1`, window `size:1001..2000`, rank 26
  - Query: `"pdf2docx" filename:requirements.txt size:1001..2000`
  - Retrieved 30 of 218 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pdf2docx` (other_processing, mixed) — manifest_declaration — [requirements.txt](https://github.com/Sshyamsundar6887/Clausewise/blob/main/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/Sshyamsundar6887/Clausewise) (source: github_api): stars=2, fork=False, archived=False
- [manifest_line](https://github.com/Sshyamsundar6887/Clausewise/blob/main/requirements.txt) (source: github_api): pdf2docx>=0.5.6  # PDF to DOCX conversion
- [readme_excerpt](https://github.com/Sshyamsundar6887/Clausewise/blob/main/README.md) (source: readme): Built for lawyers, businesses, and laypersons alike, it uses cutting-edge generative AI to make legal documents more accessible and understandable.

### 205. simbo1905/agt

**Repository / product**

- Repository: [https://github.com/simbo1905/agt](https://github.com/simbo1905/agt)
- Company: Unknown — not stated in the repository
- Product: AGT Monorepo
- Industry: legal_contracts (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
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

- Tier 3, `WeasyPrint`, run `run_1`, window `size:0..250`, rank 11
  - Query: `"weasyprint" filename:pyproject.toml size:0..250`
  - Retrieved 30 of 61 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `WeasyPrint` (template_generation, conversion) — manifest_declaration — [bin/pyproject.toml](https://github.com/simbo1905/agt/blob/6e9fa4ca600e55d0040b06f40828ece48edb52b0/bin/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/simbo1905/agt) (source: github_api): stars=0, fork=False, archived=False
- [manifest_line](https://github.com/simbo1905/agt/blob/6e9fa4ca600e55d0040b06f40828ece48edb52b0/bin/pyproject.toml) (source: github_api): requires-python = ">=3.11" dependencies = [     "markdown>=3.5",     "weasyprint>=62",     "pygments>=2.17", ]
- [readme_excerpt](https://github.com/simbo1905/agt/blob/main/README.md) (source: readme): Standalone snapshots are designed for answering "what changed?" across generated output and ignored files without interfering with normal Git history or AGT session flows.

### 206. aws-samples/bedrock-qnachatbot

**Repository / product**

- Repository: [https://github.com/aws-samples/bedrock-qnachatbot](https://github.com/aws-samples/bedrock-qnachatbot)
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

- Tier 3, `pikepdf`, run `run_1`, window `size:501..1000`, rank 27
  - Query: `"pikepdf" filename:requirements.txt size:501..1000`
  - Retrieved 30 of 324 matches; the full result set was below GitHub's 1,000-result pagination ceiling at collection time.

**Dependency evidence**

- `pikepdf` (pdf, generation) — manifest_declaration — [requirements.txt](https://github.com/aws-samples/bedrock-qnachatbot/blob/main/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/aws-samples/bedrock-qnachatbot) (source: github_api): stars=8, fork=False, archived=False
- [manifest_line](https://github.com/aws-samples/bedrock-qnachatbot/blob/main/requirements.txt) (source: github_api): pikepdf
- [readme_excerpt](https://github.com/aws-samples/bedrock-qnachatbot/blob/main/README.md) (source: readme): This is a solution for building a single interface conversational chatbot that allows end users to choose between different large language models (LLMs), inference parameters for varied input data for

### 207. doczrz/literaturereport

**Repository / product**

- Repository: [https://github.com/doczrz/literaturereport](https://github.com/doczrz/literaturereport)
- Company: Unknown — not stated in the repository
- Product: literaturereport
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

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

- Tier 3, `PyMuPDF (fitz)`, run `run_1`, window `size:251..500`, rank 21
  - Query: `"PyMuPDF" filename:pyproject.toml size:251..500`
  - Sampled 30 of 2,508 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 2,508 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `PyMuPDF (fitz)` (pdf, mixed) — manifest_declaration — [pyproject.toml](https://github.com/doczrz/literaturereport/blob/main/pyproject.toml)

**Evidence trail**

- [api_response](https://github.com/doczrz/literaturereport) (source: github_api): stars=17, fork=False, archived=False
- [manifest_line](https://github.com/doczrz/literaturereport/blob/main/pyproject.toml) (source: github_api): "PyMuPDF>=1.26,<2",
- [readme_excerpt](https://github.com/doczrz/literaturereport/blob/main/README.md) (source: readme): `literaturereport` is a Codex / ChatGPT skill built for exactly that situation.

### 208. kvcache-ai/TrEnv-X

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

### 209. misbahsy/RAGTune

**Repository / product**

- Repository: [https://github.com/misbahsy/ragtune](https://github.com/misbahsy/ragtune)
- Company: Unknown — not stated in the repository
- Product: RAGTune
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: application_code_exists, document_functionality_in_production_code \| category_count=1, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=true, application_code_exists=false, document_functionality_in_production_code=false \| unknown: all dependency evidence is manifest-only; industry_category=unknown; company_name=null; contributor_count not collected

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

- Tier 3, `Unstructured`, run `run_1`, window `size:251..500`, rank 9
  - Query: `"unstructured" filename:requirements.txt size:251..500`
  - Sampled 30 of 4,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 4,256 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

- `Unstructured` (other_processing, extraction) — manifest_declaration — [requirements.txt](https://github.com/misbahsy/RAGTune/blob/main/requirements.txt)

**Evidence trail**

- [api_response](https://github.com/misbahsy/RAGTune) (source: github_api): stars=263, fork=False, archived=False
- [manifest_line](https://github.com/misbahsy/RAGTune/blob/main/requirements.txt) (source: github_api): unstructured[docx,pptx,csv,pdf]
- [readme_excerpt](https://github.com/misbahsy/RAGTune/blob/main/README.md) (source: readme): This tool allows you to evaluate different LLMs (Large Language Models), embedding models, query transformations, and rerankers.

### 210. dundalek/closh

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

### 211. iltoga/BusinessSuite

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

### 212. remacs/remacs

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

### 213. rapid7/nexpose-warehouse-jasper-templates

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

### 214. karthikeya3342/careerOS

**Repository / product**

- Repository: [https://github.com/karthikeya3342/careeros](https://github.com/karthikeya3342/careeros)
- Company: Unknown — not stated in the repository
- Product: CareerOS — Autonomous Multi-Agent Career Optimization Engine
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: Unknown

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| unknown: no dependency evidence located; company_name=null; contributor_count not collected

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

- Tier 3, `(co-occurrence query, spans multiple libraries)`, run `run_1`, window `size:501..1000`, rank 15
  - Query: `"python-docx" "reportlab" filename:requirements.txt size:501..1000`
  - Sampled 30 of 1,784 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,784 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/karthikeya3342/careerOS) (source: github_api): stars=4, fork=False, archived=False
- [api_response](https://github.com/karthikeya3342/careerOS) (source: github_api): stars=4, fork=False, archived=False
- [api_response](https://github.com/karthikeya3342/careerOS) (source: github_api): stars=4, fork=False, archived=False

### 215. archanags001/AI-Report-Generator

**Repository / product**

- Repository: [https://github.com/archanags001/ai-report-generator](https://github.com/archanags001/ai-report-generator)
- Company: Unknown — not stated in the repository
- Product: 🧠 AI Data Analyst & Report Generator
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

- Tier 3, `(co-occurrence query, spans multiple libraries)`, run `run_1`, window `size:251..500`, rank 2
  - Query: `"python-docx" "reportlab" filename:requirements.txt size:251..500`
  - Sampled 30 of 1,964 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,964 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/archanags001/AI-Report-Generator) (source: github_api): stars=11, fork=False, archived=False
- [readme_excerpt](https://github.com/archanags001/AI-Report-Generator/blob/main/README.md) (source: readme): Welcome to **AI Data Analyst & Report Generator** — an intelligent system that helps you analyze data and create reports easily.
- [api_response](https://github.com/archanags001/AI-Report-Generator) (source: github_api): stars=11, fork=False, archived=False
- [readme_excerpt](https://github.com/archanags001/AI-Report-Generator/blob/main/README.md) (source: readme): Welcome to **AI Data Analyst & Report Generator** — an intelligent system that helps you analyze data and create reports easily.
- [api_response](https://github.com/archanags001/AI-Report-Generator) (source: github_api): stars=11, fork=False, archived=False
- [readme_excerpt](https://github.com/archanags001/AI-Report-Generator/blob/main/README.md) (source: readme): Welcome to **AI Data Analyst & Report Generator** — an intelligent system that helps you analyze data and create reports easily.

### 216. datastax/ragstack-ai

**Repository / product**

- Repository: [https://github.com/datastax/ragstack-ai](https://github.com/datastax/ragstack-ai)
- Company: Unknown — not stated in the repository
- Product: Unknown
- Industry: unknown (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://www.datastax.com/products/ragstack

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

- Tier 3, `Unstructured`, run `run_1`, window `size:1001..2000`, rank 30
  - Query: `"unstructured" filename:pyproject.toml size:1001..2000`
  - Sampled 30 of 1,070 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,070 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/datastax/ragstack-ai) (source: github_api): stars=193, fork=False, archived=False
- [api_response](https://github.com/datastax/ragstack-ai) (source: github_api): stars=193, fork=False, archived=False
- [api_response](https://github.com/datastax/ragstack-ai) (source: github_api): stars=193, fork=False, archived=False

### 217. Representable/representable

**Repository / product**

- Repository: [https://github.com/representable/representable](https://github.com/representable/representable)
- Company: Unknown — not stated in the repository
- Product: Representable PA +
- Industry: education (keyword-derived; treat as low-confidence supporting evidence, never a determining factor)
- Website: https://representable.org

**Qualification**

- Status: **investigate**
- Confidence: low
- Reason: keep criteria not met: readme_describes_product, document_functionality_in_production_code \| category_count=0, code_usage_confirmed=false, pipeline_stage_count=0, readme_describes_product=false, application_code_exists=true, document_functionality_in_production_code=false \| unknown: no dependency evidence located; company_name=null; contributor_count not collected

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

- Tier 3, `ReportLab`, run `run_1`, window `size:1001..2000`, rank 14
  - Query: `"reportlab" filename:requirements.txt size:1001..2000`
  - Sampled 30 of 9,392 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 9,392 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/Representable/representable) (source: github_api): stars=18, fork=False, archived=False
- [api_response](https://github.com/Representable/representable) (source: github_api): stars=18, fork=False, archived=False
- [api_response](https://github.com/Representable/representable) (source: github_api): stars=18, fork=False, archived=False
- [api_response](https://github.com/Representable/representable) (source: github_api): stars=18, fork=False, archived=False

### 218. CesarPetrescu/deeper-research

**Repository / product**

- Repository: [https://github.com/cesarpetrescu/deeper-research](https://github.com/cesarpetrescu/deeper-research)
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

- Tier 3, `(co-occurrence query, spans multiple libraries)`, run `run_1`, window `size:251..500`, rank 28
  - Query: `"python-docx" "reportlab" filename:requirements.txt size:251..500`
  - Sampled 30 of 1,964 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 1,964 figure describes how many repositories matched, not how many were inspected.

**Dependency evidence**

No dependency evidence recorded.

**Evidence trail**

- [api_response](https://github.com/CesarPetrescu/deeper-research) (source: github_api): stars=0, fork=False, archived=False
- [api_response](https://github.com/CesarPetrescu/deeper-research) (source: github_api): stars=0, fork=False, archived=False
- [api_response](https://github.com/CesarPetrescu/deeper-research) (source: github_api): stars=0, fork=False, archived=False

### 219. receipt-print-hq/escpos-tools

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

### 220. TurtleTech-ehf/snapper

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

- Tier 1: `"pandoc" filename:Dockerfile`
  - Sampled 30 of 13,728 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 13,728 figure describes how many repositories matched, not how many were inspected.
- Tier 2: `"docxtemplater" filename:package.json`
  - Sampled 30 of 3,256 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 3,256 figure describes how many repositories matched, not how many were inspected.
- Tier 3: `"python-docx" filename:requirements.txt size:0..250`
  - Sampled 30 of 32,576 matches; the query exceeded GitHub's 1,000-result pagination ceiling. This is a partial sample, not an exhaustive result — the 32,576 figure describes how many repositories matched, not how many were inspected.

**This is not an exhaustive map of every document-processing repository on GitHub.** It is a reproducible sample built from a documented, versioned query set. Coverage is partial wherever a query is marked capped, and the size of that gap is stated rather than hidden.

## Zero-result queries

34 of 237 recorded queries returned no results. An empty result can mean the library genuinely was not found this way, or it can mean the query itself is malformed — which is exactly what one earlier query in this project's history turned out to be, until it was corrected. Zero-result queries are therefore worth reviewing, not treated as uninteresting.

| Query | Library | Tier | Run |
|---|---|---:|---|
| `"docx4j" filename:pom.xml size:0..250` | docx4j | 3 | run_1 |
| `"docx4j" filename:pom.xml size:251..500` | docx4j | 3 | run_1 |
| `"Aspose.Words" filename:pom.xml size:0..250` | Aspose.Words | 3 | run_1 |
| `"Aspose.Words" filename:pom.xml size:251..500` | Aspose.Words | 3 | run_1 |
| `"Aspose.Words" filename:build.gradle size:0..250` | Aspose.Words | 3 | run_1 |
| `"Aspose.Words" filename:build.gradle size:251..500` | Aspose.Words | 3 | run_1 |
| `"Aspose.Words" filename:requirements.txt size:501..1000` | Aspose.Words | 3 | run_1 |
| `"Aspose.Words" filename:pyproject.toml size:0..250` | Aspose.Words | 3 | run_1 |
| `"Aspose.Words" filename:pyproject.toml size:251..500` | Aspose.Words | 3 | run_1 |
| `"Aspose.Total" extension:csproj size:0..250` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:packages.config size:0..250` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:packages.config size:251..500` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:packages.config size:501..1000` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:packages.config size:1001..2000` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:pom.xml size:0..250` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:pom.xml size:251..500` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:pom.xml size:501..1000` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:pom.xml size:1001..2000` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:build.gradle size:0..250` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:build.gradle size:251..500` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:build.gradle size:501..1000` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:requirements.txt size:0..250` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:requirements.txt size:251..500` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:requirements.txt size:501..1000` | Aspose / Spire.Office suites | 3 | run_1 |
| `"Aspose.Total" filename:requirements.txt size:1001..2000` | Aspose / Spire.Office suites | 3 | run_1 |

...and 9 more.

## Cumulative project state (all runs)

These totals cover **all 2 runs together**, not run_1. They are here for context and are not this run's results.

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

- Generated: 2026-08-23T21:56:23.428339+00:00
- Database schema version: 3
- Repository commit: 610c7860d474f6abcb24605f98346b851631d456
