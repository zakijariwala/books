# Project Handover: GCP PCA Exam-Prep Book

This document provides a comprehensive guide for developers or technical writers taking over the repository for the Google Cloud Professional Cloud Architect (GCP PCA) exam-prep book project.

---

## 1. Project Overview & Positioning

This book is a decision-mapping prep guide targeted at experienced enterprise architects (AWS, Azure, or on-prem) who need to pass the Google Cloud Professional Cloud Architect exam. 

*   **Core Principle:** It focuses on the architectural judgment and "deltas" between platforms (e.g., Global VPC vs. regional VPC, project-based resource boundaries, service account impersonation) rather than enumerating every service feature or quota table.
*   **Compression Ratio:** The official Google learning path requires ~180 hours of study. This book is designed as a ~2-hour read (~28,000 words), functioning as a high-density "read-alongside" study guide.
*   **Case-Study Focus:** Approximately 20-30% of the exam questions map to case studies. The book devotes its entire second half (Part II) to original case studies that mirror the format and complexity of Google's official scenarios.

For details on the project structure, see the [BOOK-SPEC.md](file:///D:/books/BOOK-SPEC.md).

---

## 2. Repository Directory Map

Here is the layout of the repository and the primary files you will interact with:

*   [`manuscript/`](file:///D:/books/manuscript/) — Contains all book content in Markdown format.
    *   [`front-matter.md`](file:///D:/books/manuscript/front-matter.md) — Title, introduction, and exam weight map.
    *   [`ch01.md`](file:///D:/books/manuscript/ch01.md) — Chapter 1: Exam anatomy, case study reading, and question structures.
    *   [`ch02.md`](file:///D:/books/manuscript/ch02.md) — Chapter 2: Organization, folder, and project resource hierarchies; IAM/identity.
    *   [`ch03.md`](file:///D:/books/manuscript/ch03.md) — Chapter 3: Global VPCs, Shared VPCs, Private Access, and Interconnect.
    *   [`ch04.md`](file:///D:/books/manuscript/ch04.md) to [`ch17.md`](file:///D:/books/manuscript/ch17.md) — Skeletons for chapters on compute, GKE, databases, data pipelines, AI/ML, operations, and the 5 original case studies.
    *   [`back-matter.md`](file:///D:/books/manuscript/back-matter.md) — Playbook, AWS/Azure mapping table, glossary, and links.
*   [`diagrams/`](file:///D:/books/diagrams/) — Source code for all book illustrations.
    *   [`architecture/`](file:///D:/books/diagrams/architecture/) — Python scripts using the `diagrams` library. Every figure must render to grayscale and follow the on-prem/GCP side-by-side design device. See [`sample_hybrid.py`](file:///D:/books/diagrams/architecture/sample_hybrid.py).
    *   [`flowcharts/`](file:///D:/books/diagrams/flowcharts/) — Mermaid flowchart sources (`.mmd`). See [`sample_flow.mmd`](file:///D:/books/diagrams/flowcharts/sample_flow.mmd).
*   [`scripts/`](file:///D:/books/scripts/) — Utility scripts for the print and build pipeline.
    *   [`figstyle.py`](file:///D:/books/scripts/figstyle.py) — Enforces shared print constraints (grayscale, DPI, width) for diagram generators.
    *   [`wordcount.py`](file:///D:/books/scripts/wordcount.py) — Analyzes manuscript length against the target word budget.
    *   [`normalize_image.py`](file:///D:/books/scripts/normalize_image.py) — Resizes and prepares flowchart PNG exports.
    *   [`make_reference_docx.py`](file:///D:/books/scripts/make_reference_docx.py) — Generates reference templates for Pandoc.
    *   [`patch_docx.py`](file:///D:/books/scripts/patch_docx.py) — Custom XML patches for word processor outputs.
*   [`styles/`](file:///D:/books/styles/) — Formatting templates.
    *   [`epub.css`](file:///D:/books/styles/epub.css) — Custom stylesheet for the EPUB layout.
    *   [`reference.docx`](file:///D:/books/styles/reference.docx) — Pandoc Word template (6x9 trim, print margins).
*   [`sources/datapoints/`](file:///D:/books/sources/datapoints/) — Curated research notes. **Read these for technical facts, but do not copy their prose.**
    *   [`flags-stale-and-legal.md`](file:///D:/books/sources/datapoints/flags-stale-and-legal.md) — **CRITICAL:** Review this before writing to avoid copyright exposure or stale term usage.
    *   [`exam-guide-verified.md`](file:///D:/books/sources/datapoints/exam-guide-verified.md) — Verified facts on exam sections and case studies.
    *   [`case-studies.md`](file:///D:/books/sources/datapoints/case-studies.md) — Deep dives into classic case study patterns.
    *   [`networking-identity.md`](file:///D:/books/sources/datapoints/networking-identity.md) — VPC and IAM details.
    *   [`compute-data-ops.md`](file:///D:/books/sources/datapoints/compute-data-ops.md) — GKE, serverless, databases, and deployment pipelines.
*   [`Makefile`](file:///D:/books/Makefile) — Central build script defining tasks for EPUB, DOCX, diagrams, and linting.
*   [`.vale.ini`](file:///D:/books/.vale.ini) — Configuration for Vale linter, tailoring rules (disabling sentence-case checks on headings, first-person constraints, etc.) for a book context.

---

## 3. Toolchain & Environment Setup

This project runs on Windows with Python 3 and a local virtual environment.

### 3.1 Initial Setup
To set up dependencies, activate the virtual environment and install requirements:
```powershell
# Activate venv
.\venv\Scripts\Activate.ps1

# Install requirements (if modifying scripts/diagrams dependencies)
# pip install diagrams pillow
```

### 3.2 Running Commands (When `make` is Missing)
Since standard `make` is not natively installed on some Windows environments, run the backing python/utility commands directly:

*   **Check Word Count:**
    ```powershell
    .\venv\Scripts\python.exe scripts/wordcount.py --budget 28000 manuscript
    ```
*   **Run Linter (Vale):**
    ```powershell
    vale --config=.vale.ini manuscript
    ```
*   **Compile Diagrams:**
    ```powershell
    # Render Python architecture diagram scripts
    .\venv\Scripts\python.exe diagrams/architecture/sample_hybrid.py
    
    # Render flowcharts (requires Mermaid CLI 'mmdc' installed globally)
    mmdc -i diagrams/flowcharts/sample_flow.mmd -o assets/flowcharts/sample_flow.png -c scripts/mermaid-config.json -p scripts/mermaid-puppeteer-config.json -w 1350 -b white
    .\venv\Scripts\python.exe scripts/normalize_image.py assets/flowcharts/sample_flow.png
    ```
*   **Render Book Outputs (Requires Pandoc installed):**
    ```powershell
    # Render EPUB
    pandoc metadata.yaml manuscript/front-matter.md manuscript/ch*.md manuscript/back-matter.md --resource-path=.:assets:assets/architecture:assets/flowcharts --toc --top-level-division=chapter --css=styles/epub.css --epub-title-page=false -o build/book.epub
    
    # Render Word DOCX (with reference template and patcher)
    pandoc metadata.yaml manuscript/front-matter.md manuscript/ch*.md manuscript/back-matter.md --resource-path=.:assets:assets/architecture:assets/flowcharts --toc --top-level-division=chapter --reference-doc=styles/reference.docx -o build/book.docx
    .\venv\Scripts\python.exe scripts/patch_docx.py build/book.docx
    ```

---

## 4. Writing & Formatting Constraints

All draft chapters must strictly respect these guidelines to ensure consistency and compile smoothly into KDP print templates:

*   **Chapter Word Budgets:** Each chapter has an allocated budget (between 1,200 and 1,800 words) detailed in [BOOK-SPEC.md](file:///D:/books/BOOK-SPEC.md). Keep your writing dense.
*   **No Placeholders:** Never use placeholders. If an image is needed, write a Python/Mermaid script to generate the actual figure.
*   **Grayscale-Only Interior:** The book prints in black-and-white. Figures must be rendered in grayscale; do not include color legends.
*   **Table Width Limit:** Standard print trim is 6x9. Tables must not exceed three columns.
*   **Code Block Wrap:** Hard-wrap all code blocks (specifically `gcloud` and `terraform`) at **60 characters** to prevent overflow on the printed page.
*   **Callouts:** Use standard blockquotes (`> **Note** ...`), not HTML divs or fenced divs, to guarantee compatibility across EPUB and Word outputs.
*   **Structure Depth:** Do not nest headings deeper than H3 (`###`).

---

## 5. Technical Fact Verification (PCA Exam v6.1)

The following core exam metrics have been verified against the current exam requirements and should be integrated into [manuscript/back-matter.md](file:///D:/books/manuscript/back-matter.md):

*   **Exam Cost:** $200 USD.
*   **Exam Duration:** 2 hours (120 minutes).
*   **Question Count:** 50–60 multiple-choice and multiple-select questions.
*   **Validity / Recertification:** Valid for 2 years. The renewal exam is shorter (1 hour, ~25 questions, ~$100 USD) and highlights updated content (like GenAI).
*   **Current Case Studies:** *Altostrat Media*, *Cymbal Retail*, *EHR Healthcare*, *KnightMotives Automotive*. (All others like Mountkirk, HRL, TerramEarth, Dress4Win are retired).

---

## 6. Immediate Next Steps

1.  **Draft Chapter 4 (Compute) and Chapter 5 (Containers):** Transition these files from draft skeletons to fully written prose following the exact word counts.
2.  **Analyze KnightMotives Automotive:** Read the case study from the official Google guide. Determine its technology map and write the case study chapter in [`manuscript/ch17.md`](file:///D:/books/manuscript/ch17.md).
3.  **Implement Diagrams:** Write diagram generator scripts under [`diagrams/architecture/`](file:///D:/books/diagrams/architecture/) and flowchart models under [`diagrams/flowcharts/`](file:///D:/books/diagrams/flowcharts/) to replace placeholders listed in the manuscript skeletons.
4.  **Populate AWS/Azure Concept Table:** Complete the translation matrix in [`manuscript/back-matter.md`](file:///D:/books/manuscript/back-matter.md).
