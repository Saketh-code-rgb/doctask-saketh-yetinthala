**SUPERDOCS · DEPENDENCY MAP INITIATIVE**

**Business Hypothesis**

_Identifying and Qualifying Document-Heavy Prospects_

Prepared for internal strategy review

August 2026

# **1\. What Problem Might These Companies Have?**

My hypothesis is that the real problem starts when documents stop being simple files and become a core part of a company's workflow.

Many businesses create documents repeatedly for customers, employees, partners, regulators, or internal teams. The documents may look different across industries, but the underlying problem is similar: information needs to be pulled from different systems, placed into templates, formatted correctly, reviewed, updated, converted, and delivered.

**A. Legal and Contract Companies**

**_Includes:_** _Legal-tech companies, law firms, contract-management companies, rental agreement companies, lease-management companies, legal notice companies, RTI filing companies, bar associations._

Legal businesses depend heavily on documents because most of their work has to be recorded in formal written documents. The same basic document may need to be customized for every client, case, property, or transaction. As volume increases, maintaining templates, clauses, formatting, and document versions can become a significant operational and engineering problem.

**Representative documents:**

- Contracts
- Rental and lease agreements
- Legal notices, affidavits, petitions, applications
- Client agreements and case-related documents
- Terms and conditions

**B. Real Estate and Property Businesses**

**_Includes:_** _Real estate companies, property-management companies, PropTech companies, rental platforms, lease-management platforms._

Real estate involves a large amount of paperwork for every property and transaction. A platform managing thousands of properties may need to automatically generate thousands of customized documents. That makes document generation a repeatable software problem rather than an occasional administrative task.

**Representative documents:**

- Rental, lease, and sale agreements
- Property disclosures and broker agreements
- Tenant documents and property reports
- Quotations, invoices, legal notices

**C. Healthcare and Diagnostics**

**_Includes:_** _Hospitals, clinics, diagnostic centers, body-scan centers, medical laboratories, laboratory software companies, healthcare SaaS, LIS/RIS platforms._

Healthcare organizations generate documents because information collected during a patient's visit or test needs to be communicated to patients, doctors, insurance companies, and other organizations. A diagnostic center is a particularly interesting example because the workflow can be highly automated — patient and test data flow through a report template into a personalized report and out as a PDF or DOCX. At high volume, even small problems in formatting or template changes can affect thousands of documents.

**Representative documents:**

- Diagnostic, lab, and scan reports
- Patient summaries and referral letters
- Discharge documents and medical certificates
- Insurance and compliance documents

**D. Education and EdTech**

**_Includes:_** _EdTech companies, universities, schools, learning platforms, academic software companies._

Education organizations generate documents for students, teachers, parents, and regulators. The interesting opportunity is where these documents are automatically generated from student or course data.

**Representative documents:**

- Certificates, transcripts, mark sheets
- Admission letters and student reports
- Course completion and recommendation letters
- Assessment reports and academic notices

**E. Finance, Investment and VC**

**_Includes:_** _VC firms, investment companies, FinTech companies, accounting software, financial reporting platforms, investment-management platforms, insurance companies._

Financial companies need documents to record decisions, communicate information, complete transactions, and meet regulatory requirements. These documents often contain information from multiple sources and need to follow standard templates and formatting.

**Representative documents:**

- Investment memos and due-diligence reports
- Term sheets and investor reports
- Financial and portfolio reports
- Insurance policies, claims, and compliance documents

**F. Proposal, RFP and Sales Companies**

**_Includes:_** _Proposal software, RFP platforms, sales-enablement platforms, quotation software, B2B SaaS companies._

Companies responding to RFPs or preparing proposals need to create customized documents for individual customers, moving from customer requirements and pricing through a proposal template into a customized DOCX or PDF. The same company may need to create hundreds of proposals with different content. This is especially interesting because the document is directly connected to revenue — faster document generation can mean faster RFP response and a direct business benefit.

**G. Event and Wedding Companies**

**_Includes:_** _Event-management companies, wedding companies, event-management software, wedding-management platforms, vendor-management platforms._

These companies repeatedly create customer-specific documents. The opportunity becomes more interesting when a software platform is generating these documents for thousands of event businesses.

**Representative documents:**

- Event proposals and wedding packages
- Quotations, contracts, invoices
- Event schedules and itineraries
- Vendor agreements

**H. Software and Technical Documentation**

**_Includes:_** _SaaS companies, developer platforms, enterprise software, technical-documentation platforms, document-automation software._

Software companies may generate documents for customers, internal teams, compliance, implementation, or technical workflows. This category is particularly important for the Dependency Map because software companies may expose their document-processing implementation in public repositories, allowing us to identify the libraries and custom infrastructure they use.

**Representative documents:**

- Technical documentation and implementation guides
- Customer reports and proposals
- Security and compliance documentation
- Product documentation

**THE COMMON THREAD**

_The common problem across these categories is not simply that they have documents. It is that documents become an operational system that needs continuous engineering, maintenance, customization, and human review._

# **2\. Why Might Heavy Use of Document-Manipulation Libraries Indicate This Problem?**

A single dependency on a document library does not prove that a company has a document problem. For example, a developer might use python-docx to create one simple Word document — that is not a strong prospect signal.

The stronger signal is when multiple document-related dependencies are combined with custom processing logic.

**_DOCX library + PDF library + Template engine + Formatting logic + Conversion code + Validation + Storage / versioning_**

This combination can indicate that the company has built its own document-processing pipeline.

## **What Different Dependencies Can Tell Us**

| **Library type**                                                   | **What it can indicate**                                                                                                                                                                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DOCX libraries (python-docx, docx4j, Apache POI, Open XML SDK)** | Word document generation, template population, formatting, tables, images, reports, contracts, letters, automated document creation.                                                                                            |
| **PDF libraries (PDFBox, iText, PyMuPDF, ReportLab)**              | PDF generation and editing, report generation, document extraction, conversion, and combining documents.                                                                                                                        |
| **Conversion libraries**                                           | Movement of information between formats — for example, database → HTML/template → DOCX → PDF. The more steps involved, the more opportunities for formatting issues, compatibility problems, maintenance, and engineering work. |

## **The Signal I Actually Want to Find**

The Dependency Map should answer more than: "Does this project use a document library?"

_It should answer: what document workflow is this dependency supporting, how complex is that workflow, and how much engineering effort appears to be invested in maintaining it?_

Heavy dependency usage becomes valuable when it is connected to high document volume, complex formatting, frequent changes, and business-critical documents.

# **3\. Why Might Such a Company Care About SuperDocs?**

A company that has built a large document pipeline may be spending engineering time solving problems that are not its core business. Developers may have to maintain document templates, formatting logic, DOCX and PDF generation, file conversion, tables and images, document editing, validation, versioning, storage, and content generation. Every new document requirement can result in more custom code and more testing.

SuperDocs could potentially provide an AI-powered document layer that reduces some of this complexity. The value could come from several areas:

| **1** | **Reduce engineering effort**<br><br>**—** Instead of building every document-editing capability internally, a company could use SuperDocs as part of its document workflow. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| **2** | **Speed up document changes**<br><br>**—** If a legal template, proposal, report, or policy changes, the company may not want developers to modify document-processing code every time. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| **3** | **Handle complex document workflows**<br><br>**—** AI-assisted editing could help with documents containing structured content, templates, formatting, and multiple sections. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| **4** | **Improve business workflows**<br><br>**—** Business application → SuperDocs → AI-assisted document generation/editing → Final document. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------- |

For software companies, the integration and API story is especially interesting because SuperDocs could potentially become part of their existing product rather than being used only as a standalone editor.

**THE VALUE PROPOSITION**

_The strongest value proposition is not that SuperDocs can edit Word documents. It is that SuperDocs could potentially reduce the amount of custom engineering required to build and maintain document-heavy workflows._

# **4\. What Would Make a Company a Strong Prospect?**

I would not rank a company highly just because it belongs to a document-heavy industry. I would look for evidence across the following dimensions:

| **1** | **High document volume**<br><br>**—** Thousands of contracts per month<br><br>**—** Thousands of diagnostic reports<br><br>**—** Large numbers of certificates, proposals, or invoices<br><br>**—** High volume increases the potential ROI |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| **2** | **High document complexity**<br><br>**—** Multiple templates, tables, images, headers and footers<br><br>**—** Complex formatting and multiple sections<br><br>**—** Customer-specific content<br><br>**—** DOCX/PDF conversion across multiple document types |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| **3** | **Business-critical documents**<br><br>**—** Directly connected to revenue, legal obligations, or compliance<br><br>**—** Tied to customer delivery, financial decisions, or healthcare reporting |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| **4** | **Significant document-processing code**<br><br>**—** Multiple document libraries and custom generation classes<br><br>**—** Template engines and formatting utilities<br><br>**—** Conversion services, validation, and report-generation modules |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| **5** | **Frequent document changes**<br><br>**—** Contracts, policies, templates, and reports change often<br><br>**—** Frequent changes increase maintenance cost |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |

| **6** | **Clear build-vs-buy opportunity**<br><br>**—** The company appears to be spending engineering resources building functionality SuperDocs may already provide |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| **7** | **Strong commercial leverage**<br><br>**—** A SaaS platform serving thousands of customers can be more attractive than a single organization<br><br>**—** One integration could improve document workflows for many end users |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| **8** | **Clear ROI**<br><br>**—** A large volume of complex documents plus a significant custom pipeline suggests reducing even a portion of that effort could create meaningful savings |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The exact ROI would need evidence later; this is the type of hypothesis the Dependency Map should help validate.

# **5\. What Would Make a Company a Weak Prospect?**

A company is weak when document processing is incidental rather than important to its product or operations.

- Uses a document library for one small script.
- Generates very few documents, or only simple text documents.
- Has no document templates and no custom document-processing code.
- Shows no evidence of automated document generation.
- Documents are not important to revenue or operations.
- Rarely changes its documents; low volume overall.
- Has no obvious engineering maintenance burden.
- Would not gain meaningful value from AI-assisted document workflows.

| **WEAK SIGNAL**<br><br>GitHub repository → uses python-docx → creates one simple Word file. | **STRONG SIGNAL**<br><br>DOCX + PDF library + template engine + formatting utilities + conversion code + report generation → used by a product → large document volume → frequent changes. |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

I also think individual organizations should generally be treated differently from software platforms. A single school or small clinic may use many documents but may not have enough engineering complexity or budget to justify an integration. A software platform serving hundreds or thousands of those organizations could be a much stronger prospect.

# **6\. My Current Hypothesis**

_The best SuperDocs prospects are companies where document creation and modification have become a core software workflow rather than a simple administrative task. The strongest signals will be high document volume, complex templates and formatting, frequent document changes, business-critical documents, and significant custom code or dependency usage for document processing._

I believe the Dependency Map can use these technical signals to uncover companies that may be spending substantial engineering effort maintaining their own document infrastructure. The highest-value prospects should be companies where replacing or augmenting that infrastructure could produce measurable savings, faster product development, or better document workflows.

END OF DOCUMENT