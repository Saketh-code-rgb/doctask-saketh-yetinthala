# Document Manipulation Library Universe

This is the starting vocabulary for the Dependency Map. Every entry below was checked against current docs, GitHub, or PyPI/npm listings in August 2026, not pulled from memory alone. The goal isn't to be exhaustive, it's to give the search step a real list of things to grep for in `requirements.txt`, `package.json`, `pom.xml`, `.csproj`, and lockfiles.

One thing that shaped the list: a library that *creates or edits* a document tells us something different than one that *reads or extracts* from one. I've flagged that direction in each "why it matters" cell, and there's a short note on it at the end.

## 1. DOCX / Word

| Library | Language | What it does | Why it matters |
|---|---|---|---|
| python-docx | Python | Creates, reads, and updates .docx files: paragraphs, tables, styles, images, headers/footers | The most common baseline signal. On its own it's weak (could be one script generating one file), but it's the thing to look for combined with other dependencies |
| docx4j | Java | Full OOXML manipulation for Word (and Excel/PowerPoint) on the JVM | Signals a JVM backend actually generating or editing real Word docs, not just displaying them |
| Apache POI (XWPF/HWPF) | Java | Creates and reads Word documents via OOXML and legacy binary formats, alongside its Excel/PPT modules | Extremely common in enterprise Java stacks; often the backbone of a homegrown reporting pipeline |
| Open XML SDK | .NET / C# | Microsoft's own low level SDK for reading and writing OOXML (docx/xlsx/pptx) without Office installed | Common in .NET shops building document automation server-side, since it needs no Office license |
| docx (dolanmiu/docx) | JavaScript / TypeScript | Generates and manages Word files (sections, tables, headers, footers) purely in JS, works in Node and the browser | A signal that document generation is happening inside a JS/Node product, not farmed out to a backend service |
| docxtemplater | JavaScript | Fills a .docx template from data with loops, conditionals, and placeholders | Strong signal on its own: this is template-driven document generation, exactly the pattern the business hypothesis flags as valuable |
| mammoth / python-mammoth | JS and Python | Converts .docx into clean HTML | Different direction: this is about *displaying* Word content on the web, not generating documents |
| Aspose.Words | .NET, Java, Python, C++ (commercial) | Full-featured proprietary Word processing SDK, no MS Office needed | A company paying for this is a strong signal, since it means they've already decided document handling is important enough to buy rather than build from scratch |

## 2. PDF

| Library | Language | What it does | Why it matters |
|---|---|---|---|
| pypdf / PyPDF2 | Python | Basic PDF reading, merging, splitting, page extraction | Common but shallow. Usually a support utility rather than the core of a pipeline |
| ReportLab | Python | Low-level, canvas-based PDF generation from scratch | The industry default for invoices, certificates, and generated reports in Python |
| PyMuPDF (fitz) | Python | Fast PDF rendering, text and image extraction, low-level manipulation | Mixed direction: used for both extraction and, less often, generation. Worth checking which |
| pikepdf | Python (wraps QPDF) | Creates, repairs, and manipulates PDFs, handles encrypted files and linearization | Lower-level and more structural than ReportLab, usually paired with something else for content |
| Apache PDFBox | Java | Creates, edits, and extracts content from PDFs, includes form filling and signing | Common in Java backends, frequently shows up alongside Apache POI in the same repo |
| iText | Java and .NET (AGPL / commercial) | Mature, full-featured PDF SDK: creation, editing, forms, digital signatures, HTML-to-PDF add-on | The AGPL-vs-commercial licensing split is itself a signal, since a paid iText license means real budget behind document infrastructure |
| pdf-lib | JavaScript (Node and browser) | Creates and modifies PDFs with no native dependencies, including form filling | The go-to when a team wants PDF generation to run client-side or in a lightweight Node service |
| PDFKit | Node.js | Programmatic, streams-based PDF generation | Common in Node backends generating invoices/reports on the fly |

## 3. HTML / Template → Document

| Library | Language | What it does | Why it matters |
|---|---|---|---|
| docxtpl (python-docx-template) | Python | Jinja2-style templating layered on python-docx: placeholders, loops, inline images | This is close to the ideal signal from the hypothesis: DOCX library + template engine in one place |
| Carbone.io | Node.js (engine, also has a cloud API) | Fills native DOCX/XLSX/PPTX/ODT templates from JSON and can render straight to PDF, driving LibreOffice/Chromium under the hood | A strong "report generation as a product feature" signal, since it's usually adopted specifically to avoid building this in-house |
| JasperReports / Apache FOP | Java | Declarative, XML-template-driven report generation that outputs PDF, DOCX, XLSX | The classic enterprise reporting engine; almost always means recurring, formal reports are core to the product |
| WeasyPrint | Python | Renders styled HTML/CSS directly to PDF | Common when a team already has an HTML template and just wants a print-quality PDF out of it |
| Puppeteer / Playwright (used for PDF) | Node.js | Drives headless Chromium to print an HTML page to PDF | Signals a homegrown "HTML template → PDF" pipeline rather than a purpose-built document library, often paired with Handlebars or EJS |

## 4. Document Conversion

| Library | Language | What it does | Why it matters |
|---|---|---|---|
| Pandoc | CLI, invoked from almost any language | Converts between Markdown, DOCX, HTML, LaTeX, PDF, and dozens of other formats | A strong signal of a format-crossing content pipeline, common in docs tooling and publishing workflows |
| LibreOffice headless / unoconv / JODConverter | Runs as a subprocess or service, called from any language | Uses LibreOffice itself, without the GUI, to convert between virtually all Office formats | Often exactly the "expensive to maintain" homegrown pipeline the hypothesis calls out. It works, but running LibreOffice as a subprocess at scale is a known operational headache |
| Gotenberg | Dockerized Go service (wraps Chromium + LibreOffice) | An HTTP microservice for converting HTML, Markdown, and Office documents to PDF | A dedicated document-conversion microservice is a strong signal of real engineering investment, not a one-off script |
| Aspose / Spire.Office suites | .NET, Java, Python, JS (commercial) | Multi-format commercial SDKs covering Word, Excel, PowerPoint, and PDF conversion without needing MS Office installed | Different flavor of signal: the company chose to buy rather than build, which still means documents matter enough to spend on |

## 5. Other Document Processing

| Library | Language | What it does | Why it matters |
|---|---|---|---|
| Apache Tika | Java, with REST/Python bindings | Detects and extracts text and metadata from over a thousand file types | Almost always an extraction/ingestion signal (search, compliance, indexing), not generation |
| Unstructured | Python | Partitions and chunks documents across many formats, built for RAG pipelines, wraps poppler/tesseract/LibreOffice/Pandoc internally | A 2026-era signal: this shows up when a team is feeding documents into an LLM pipeline, not producing documents for people |
| Docling | Python (IBM Research) | AI layout-aware parser that converts PDFs, DOCX, and PPTX into structured Markdown or JSON, self-hostable | Same direction as Unstructured, extraction for AI use rather than document creation, but newer and increasingly common |
| pdf2docx | Python (built on PyMuPDF + python-docx) | Converts a PDF's layout into an editable DOCX, preserving tables and images | A genuinely bidirectional signal: this only gets used where PDF and DOCX both matter to the same workflow |
| docx-mailmerge / docxedit | Python | Mail-merge-style field replacement, or global find-and-replace that preserves formatting | A narrower, older pattern than docxtpl but still shows up in form-letter and template-heavy repos |

## Initial inclusion rule

A library goes on this list if its primary purpose is creating, editing, populating, or converting document files (DOCX, PDF, and the formats that regularly move between them), not simply displaying, storing, or attaching them. And its presence in a dependency manifest has to plausibly tell us something about how that company handles documents, not just that they once needed to read a file. That's why general-purpose text libraries, plain file-storage SDKs, and pure PDF viewers didn't make the cut.

## A note on direction: generation vs. extraction

Not every hit means the same thing. A DOCX or PDF *generation* library (python-docx, ReportLab, docxtpl, Carbone) tells us a company is producing documents, which is the closer match to what SuperDocs replaces. An *extraction* library (Apache Tika, Unstructured, Docling, PyMuPDF used for reading) tells us they're consuming or parsing documents, which is a related but different problem, closer to ingestion than to editing. Some libraries genuinely do both (PyMuPDF, pdf2docx), and a few conversion tools (Pandoc, Gotenberg, LibreOffice headless) sit in between, moving content from one format to another without really "authoring" it.

The Dependency Map should keep this distinction visible in its output rather than collapsing everything into one score. A repo full of extraction libraries and no generation libraries is a different kind of prospect than one running a template-to-PDF pipeline in production.
