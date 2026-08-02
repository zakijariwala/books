# Project Handover: GCP PCA Exam-Prep Book

This document provides a comprehensive guide for developers or technical writers taking over the repository for the Google Cloud Professional Cloud Architect (GCP PCA) exam-prep book project.

---

## 1. Project Overview & Positioning

This book is a decision-mapping prep guide targeted at experienced enterprise architects (AWS, Azure, or on-prem) who need to pass the Google Cloud Professional Cloud Architect exam. 

*   **Core Principle:** It focuses on the architectural judgment and "deltas" between platforms (e.g., Global VPC vs. regional VPC, project-based resource boundaries, service account impersonation) rather than enumerating every service feature or quota table.
*   **Compression Ratio:** The official Google learning path requires ~180 hours of study. This book is designed as a ~2-hour read (~28,000 words), functioning as a high-density "read-alongside" study guide.
*   **Case-Study Focus:** Approximately 20-30% of the exam questions map to case studies. The book devotes its entire second half (Part II) to original case studies that mirror the format and complexity of Google's official scenarios.

For details on the project structure, see the [BOOK-SPEC.md](file:///D:/books/BOOK-SPEC.md).

### 1.1 Current State

Every chapter, both parts, the back matter, and all 32 figures are drafted. The
manuscript is **~22,300 words against a 28,000 target**, so it is under budget,
not over.

What has *not* happened: Pandoc has never been run, so no DOCX or EPUB exists
and nothing about page layout is verified. Vale has never been run against any
drafted chapter. Several facts are deliberately marked for verification rather
than printed from memory. See [TASKS.md](file:///D:/books/TASKS.md) for the full
list of what is outstanding and why.

---

## 2. Repository Directory Map

Here is the layout of the repository and the primary files you will interact with:

*   [`manuscript/`](file:///D:/books/manuscript/) — Contains all book content in Markdown format.
    *   [`front-matter.md`](file:///D:/books/manuscript/front-matter.md) — Title, introduction, and exam weight map.
    *   [`ch01.md`](file:///D:/books/manuscript/ch01.md) — Chapter 1: Exam anatomy, case study reading, and question structures.
    *   [`ch02.md`](file:///D:/books/manuscript/ch02.md) — Chapter 2: Organization, folder, and project resource hierarchies; IAM/identity.
    *   [`ch03.md`](file:///D:/books/manuscript/ch03.md) — Chapter 3: Global VPCs, Shared VPCs, Private Access, and Interconnect.
    *   [`ch04.md`](file:///D:/books/manuscript/ch04.md) to [`ch12.md`](file:///D:/books/manuscript/ch12.md) — Part I decision chapters: compute, containers, storage and databases, data pipelines, AI/ML, security, migration, reliability, operations and cost.
    *   [`ch13.md`](file:///D:/books/manuscript/ch13.md) to [`ch17.md`](file:///D:/books/manuscript/ch17.md) — Part II, five original case studies. All companies and scenarios are invented; see section 5.
    *   [`back-matter.md`](file:///D:/books/manuscript/back-matter.md) — Playbook, AWS and Azure mapping tables, glossary, and links.
*   [`diagrams/`](file:///D:/books/diagrams/) — Source for all 32 book figures. One source file per figure, named `figNN_M_slug` to match its `Figure N.M` caption in the manuscript.
    *   [`architecture/`](file:///D:/books/diagrams/architecture/) — 16 Python scripts using the `diagrams` library, one per `Figure N.1`. Each carries the on-prem-beside-GCP device and renders grayscale through `figstyle.py`.
    *   [`flowcharts/`](file:///D:/books/diagrams/flowcharts/) — 16 Mermaid sources (`.mmd`), one per `Figure N.2`. Node labels are deliberately terse; see the print constraint under section 3.2.
*   `assets/` — Rendered PNGs. **Gitignored on purpose**: regenerate from `diagrams/` rather than committing binaries. A publisher handoff needs these built first.
*   [`scripts/`](file:///D:/books/scripts/) — Utility scripts for the print and build pipeline.
    *   [`figstyle.py`](file:///D:/books/scripts/figstyle.py) — Enforces shared print constraints (grayscale, DPI, width) for diagram generators.
    *   [`wordcount.py`](file:///D:/books/scripts/wordcount.py) — Analyzes manuscript length against the target word budget.
    *   [`normalize_image.py`](file:///D:/books/scripts/normalize_image.py) — Fits every figure to the text block, converts to grayscale, and fails the build if type would print below 8pt. Run it on any figure you render.
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

*   **Run the tests:**
    ```powershell
    .\venv\Scripts\python.exe -m pytest -m "not build"   # fast, no Pandoc
    .\venv\Scripts\python.exe -m pytest -m build         # needs a built book
    ```
    The fast set runs in the pre-commit hook. It checks the print-pipeline
    scripts and the manuscript's structural invariants: heading depth, table
    column counts, figure references resolving to real sources, code-line
    width. The `build` set asserts against `build/book.docx` and
    `build/book.epub` and needs `make epub docx` to have run first.

    Dependencies live in `requirements-dev.txt`.

*   **Check Word Count:**
    ```powershell
    .\venv\Scripts\python.exe scripts/wordcount.py --budget 28000 manuscript
    ```
*   **Run Linter (Vale):**

    Vale is installed via winget but, like Graphviz, is **not on PATH**. It
    lives under `%LOCALAPPDATA%\Microsoft\WinGet\Packages\errata-ai.Vale_Microsoft.Winget.Source_8wekyb3d8bbwe`.
    The pre-commit hook refuses to commit without it, by design.
    ```powershell
    $env:PATH += ";$env:LOCALAPPDATA\Microsoft\WinGet\Packages\errata-ai.Vale_Microsoft.Winget.Source_8wekyb3d8bbwe"
    vale --config=.vale.ini manuscript
    ```
    The hook gates on **errors only**. The manuscript is clean at that level.
    Warnings and suggestions are numerous and mostly not worth actioning; see
    [TASKS.md](file:///D:/books/TASKS.md) section 2.

    When Vale reports an unknown technical term, add it to
    `styles/config/vocabularies/Book/accept.txt` rather than rewording. Entries
    are regular expressions: write `[Aa]utoscaling`, not `Autoscaling`, or
    `Vale.Terms` will start demanding the capitalised form mid-sentence.
*   **Compile Diagrams:**

    Graphviz is installed at `C:\Program Files\Graphviz` but is **not on PATH**,
    so the `diagrams` library fails with `ExecutableNotFound: dot`. Add it for
    the session before rendering architecture figures:
    ```powershell
    $env:PATH += ";C:\Program Files\Graphviz\bin"
    $env:PYTHONPATH = "scripts"
    ```
    ```powershell
    # Render Python architecture diagram scripts
    .\venv\Scripts\python.exe diagrams/architecture/fig07_1_pipeline_shift.py
    
    # Render flowcharts (requires Mermaid CLI 'mmdc' installed globally).
    # Do NOT pass -w: the mermaid config sets useMaxWidth false so the diagram
    # renders at its natural size, and normalize_image.py fits it to the page.
    mmdc -i diagrams/flowcharts/fig06_2_database.mmd -o assets/flowcharts/fig06_2_database.png -c scripts/mermaid-config.json -p scripts/mermaid-puppeteer-config.json -b white
    .\venv\Scripts\python.exe scripts/normalize_image.py assets/flowcharts/fig06_2_database.png
    ```

    `normalize_image.py` fits each figure to the 4.5x7in text block, converts it
    to grayscale, and **exits non-zero if the type would print below 8pt**. That
    check is the constraint that matters: a 4.5in-wide flowchart holds about two
    columns of short labels. If it fails, shorten the node labels or cut a rank
    rather than enlarging the image, which cannot work on a fixed trim size.
*   **Render Book Outputs:**

    Pandoc is installed but **not on PATH**; it lives in
    `%LOCALAPPDATA%\Pandoc`. That makes three tools in this project installed
    and invisible: Graphviz, Vale, and Pandoc. Check there before concluding
    anything is missing.
    ```powershell
    $env:PATH += ";$env:LOCALAPPDATA\Pandoc"
    ```
    On Windows `--resource-path` must be separated with `;`, not `:`. With the
    wrong separator Pandoc still exits 0 and produces a book containing no
    figures at all, warning `Could not fetch resource` for each one. The
    Makefile now switches on `$(OS)`; the commands below are the Windows form.
    ```powershell
    # Render EPUB
    pandoc metadata.yaml manuscript/front-matter.md manuscript/ch*.md manuscript/back-matter.md --resource-path=".;assets;assets/architecture;assets/flowcharts" --toc --top-level-division=chapter --css=styles/epub.css --epub-title-page=false -o build/book.epub
    
    # Render Word DOCX (with reference template and patcher)
    pandoc metadata.yaml manuscript/front-matter.md manuscript/ch*.md manuscript/back-matter.md --resource-path=".;assets;assets/architecture;assets/flowcharts" --toc --top-level-division=chapter --reference-doc=styles/reference.docx -o build/book.docx
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

All chapters, both case-study halves, the back matter, and all 32 figures are
drafted. The manuscript stands at roughly 22,300 words against a 28,000 target,
which is under budget rather than over. What remains:

1.  **Proof the built outputs.** Nothing has been through Pandoc yet. Build the
    DOCX and EPUB and check figure placement, table breaks at 6x9, and that no
    figure lands orphaned from its caption.
2.  **Run Vale.** The linter is configured but is not on PATH in this
    environment, so no drafted chapter has been linted.
3.  **Verify the volatile facts.** Chapters 7 and 8 move fastest. The exam
    metrics in the back matter (cost, duration, question count, renewal terms)
    and the current case-study list both need confirming against the
    certification page before publication.
4.  **Decide on the spare word budget.** About 5,600 words are unspent. Part I
    is dense and could take more worked examples; alternatively the book ships
    shorter, which still clears the 79-page KDP spine threshold comfortably.
5.  **Second pass on Part II scenarios.** The five case studies are original and
    internally consistent, but the numbers in them (fleet sizes, data volumes,
    dates) were chosen for plausibility and should be sanity-checked for
    arithmetic that a careful reader would test.
