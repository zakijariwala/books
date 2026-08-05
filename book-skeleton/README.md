# Book Skeleton

A reusable scaffold for writing a book — mostly nonfiction and technical — with
Git for version control and AI assistance (Claude Code) as a collaborator. It
gives you a reproducible toolchain that builds a Markdown manuscript into a
print-ready 6x9 paperback (DOCX) and an ebook (EPUB), with figures generated
from source, prose linting, structural tests, and the governance and briefing
docs a book project needs.

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
STYLE-GUIDE.md          Voice, spelling, and prose mechanics (what Vale can't decide)
GOVERNANCE.md           Git workflow, definition of done, fact-checking, copyright
PRODUCTION-NOTES.md     Layout decisions for the interior, made after the build
AGENT-BRIEF.md          Positioning and go-to-market / launch brief
TASKS.md                The living backlog, ordered by risk
CHANGELOG.md            Edition and printing history
metadata.yaml           Pandoc metadata: title, author, imprint, identifier
Makefile                Build pipeline: diagrams, lint, test, epub, docx, pdf
.vale.ini               Prose linter config, tuned for a book (not docs)
manuscript/             The book, in Markdown. Chapter template in ch01.md
diagrams/               Figure SOURCES: Python (architecture) + Mermaid (flowcharts)
scripts/                Render/build helpers, bootstrap, pre-commit hook
styles/                 Vale vocab + EPUB CSS + the 6x9 Word reference template
tests/                  pytest: manuscript invariants + script behaviour
sources/research/       Fact logs and permissions — auditable, never copied into the book
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
4. **Fill in the specifics**, roughly in this order:
   - `metadata.yaml` — title, author, imprint, a fresh UUID, language.
   - `BOOK-SPEC.md` — positioning, reader, word budget, chapter list. Set
     `WORD_BUDGET` in the `Makefile` to match.
   - `STYLE-GUIDE.md` — voice, and en-US vs en-GB (match `lang` in metadata).
5. **Confirm it's green** on the empty skeleton:
   ```
   make test
   ```
6. **Write.** Copy `manuscript/ch01.md` per chapter; render figures as you go.

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
