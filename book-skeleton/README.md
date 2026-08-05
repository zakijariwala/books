# Book Skeleton — the consolidated seed

A reusable scaffold for writing a book — mostly nonfiction and technical — with
Git for version control and AI assistance (Claude Code) as a collaborator. It
merges two proven approaches (see `../COMPARISON.md`): the **editorial workflow**
that decides what to write, for whom, and in whose voice; and the **production
pipeline** that builds a Markdown manuscript into a print-ready 6x9 paperback
(DOCX) and an ebook (EPUB), with figures generated from source, prose linting,
structural tests, and the governance and launch docs a book needs.

It covers the whole arc: reader → thesis → voice → structure → draft → review →
verify → build → launch. The tooling ships ready but stays dormant until the
stage that needs it, so you can start writing immediately and still have a build
that runs the day you want one.

Copy this directory to a new repository, then work through the setup checklist
below. Nothing here is book-specific until you fill it in.

## Why this exists

Books written with an AI collaborator need the same things software does:
a single source of truth, reproducible builds, automated checks, and written
rules so every session (human or machine) behaves consistently. This skeleton
supplies all of that, distilled from a finished, published book so the
conventions are proven rather than guessed.

## What's in the box

```
CLAUDE.md / AGENTS.md   Operating manual for AI assistance — the rules that don't bend
BOOK-SPEC.md            This book's positioning, reader, word budget, structure
STYLE-GUIDE.md          Spelling and prose mechanics (voice lives in voice/sample.md)
GOVERNANCE.md           Git workflow, definition of done, fact-checking, copyright
PRODUCTION-NOTES.md     Layout decisions for the interior, made after the build
AGENT-BRIEF.md          Positioning and go-to-market / launch brief
HANDOVER.md             Living state doc: where things are, decisions taken, blockers
TASKS.md                The staged plan, ordered so each block unblocks the next
CHANGELOG.md            Edition and printing history
metadata.yaml           Pandoc metadata: title, author, imprint, identifier

docs/                   Editorial standards
  buyer.md              The reader. Outcomes, layers, purchase moment. Wins scope
  toc.md                Chapter list, frozen only after the kill test
  chapter-template.md   The fixed shape every chapter takes, with section budgets
  terminology.md        One approved definition per term
  concept-registry.md   Where each concept is introduced and revisited
  case-study-registry.md  Which example illustrates what, dated and sourced
  figures.md            Figure list, collected by /approve
voice/
  BRIEF.md              How to extract your voice. NOT a voice source
  sample.md             Your transcript. The only style input
prompts/                Staged prompt text: kill test, standards, figures
.claude/skills/         /article /draft /review /approve /verify

manuscript/             The book, in Markdown. Fill-in template in ch01.md
diagrams/               Figure SOURCES: Python (architecture) + Mermaid (flowcharts)
scripts/                Render/build helpers, bootstrap, pre-commit hook
styles/                 Vale vocab + EPUB CSS + the 6x9 Word reference template
tests/                  pytest: manuscript invariants + script behaviour
sources/research/       Fact logs and permissions — auditable, never copied into the book
articles/ reviews/      Pilot articles and chapter reviews, produced by the skills
Makefile                Build pipeline: diagrams, lint, test, epub, docx, pdf
.vale.ini               Prose linter config, tuned for a book (not docs)
.github/                CI workflow + PR template
```

## Setup for a new book

1. **Copy** this directory into a fresh repo and `git init`.
2. **Bootstrap** the environment:
   ```
   bash scripts/bootstrap.sh
   ```
   This creates a Python venv, installs `requirements-dev.txt`, reports which
   external tools are present, and runs `vale sync`. Install any tool it flags
   as missing (`pandoc`, `vale`, `graphviz`/`dot`, `mermaid-cli`/`mmdc`).
3. **Install the commit gate:**
   ```
   make hooks
   ```
4. **Decide, in this order** (the editorial stages — see `TASKS.md` and
   `prompts/`):
   - `metadata.yaml` — title, author, imprint, a fresh UUID, language.
   - `BOOK-SPEC.md` — thesis, positioning, word budget, chapter list. Set
     `WORD_BUDGET` in the `Makefile` to match.
   - `docs/buyer.md` — the one reader. This wins any scope argument.
   - `voice/sample.md` — extract your voice per `voice/BRIEF.md`. This is the
     authoritative style source and it blocks drafting until it is real.
   - Freeze the TOC with `prompts/stage2-kill-test.md`, then generate the
     standards with `prompts/stage3-standards.md`.
5. **Confirm it's green** on the empty skeleton:
   ```
   make test
   ```
6. **Pilot, then write.** `/article` a couple of chapters to test demand, then
   per chapter: `/draft → /review → /verify → /approve`. Mark figures and
   first-hand stories with `<!-- FIGURE: ... -->` / `<!-- STORY-TODO: ... -->`;
   draw and write them later. Render figures once three chapters exist
   (`prompts/stage6-figures.md`).

## Daily commands

```
make diagrams     Render every figure source to assets/ (gitignored)
make lint         Vale over the manuscript (errors block commits)
make test         Fast checks: structure + script behaviour
make wordcount    Prose count against the budget
make epub docx    Build both book outputs into build/
make test-build   Slow checks against the built book
make grayscale    Grayscale proofs of every figure
make clean        Remove build/ and assets/
```

## Toolchain

| Tool | Role | Install |
| --- | --- | --- |
| Pandoc | Markdown → EPUB / DOCX | OS package manager |
| Vale | prose linter | `vale.sh` / package manager |
| Graphviz (`dot`) | architecture figures | OS package manager |
| mermaid-cli (`mmdc`) | flowchart figures | `npm i -g @mermaid-js/mermaid-cli` |
| Python 3 + `diagrams`, `pillow`, `pytest` | figures + tests | `requirements-dev.txt` |

## First stop for an AI collaborator

Read `CLAUDE.md`. It states the non-negotiable rules, the build commands, the
git workflow, and what not to do — before touching a single chapter.
