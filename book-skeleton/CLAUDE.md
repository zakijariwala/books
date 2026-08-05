# CLAUDE.md — Operating Manual for AI Assistance

This file is read automatically by Claude Code (and is the source for
`AGENTS.md`). It tells an AI collaborator how this book is built and what rules
are non-negotiable. Keep it accurate: it is the single most load-bearing
document for machine-assisted writing here. When a convention changes, change it
here first.

## What this repository is

A single book, written in Markdown, built to print (DOCX for a 6x9 paperback)
and ebook (EPUB) with Pandoc. Figures are generated from source — never
hand-drawn, never pasted — so the whole book rebuilds from text with one
command. This is a **book toolchain, not an application**: optimise for
reproducibility and for prose quality, not for runtime performance.

Read `BOOK-SPEC.md` for this book's specific positioning, audience, word budget,
and structure before writing any content.

## The rules that do not bend

These are enforced by the test suite (`tests/test_manuscript.py`) and the render
scripts. Breaking one either fails a commit or ships a defective book.

1. **No placeholders in committed content.** If a figure is needed, write the
   diagram source and render it. Never commit `[FIGURE X: ...]`, `TODO`, or
   `lorem ipsum` in a manuscript file. The template TODOs in `manuscript/` are
   the one exception, and only until real content replaces them.
2. **Figures are generated, one source per figure.** Architecture figures are
   Python in `diagrams/architecture/` using the `diagrams` library via
   `scripts/figstyle.py`. Flowcharts are Mermaid `.mmd` in
   `diagrams/flowcharts/`. Name each `figNN_M_slug` to match its `Figure N.M`
   caption (chapter N, figure M). Rendered PNGs go to `assets/`, which is
   gitignored — regenerate, do not commit binaries.
3. **Grayscale only.** The print interior is black and white. No colour, no
   colour-coded legends. `normalize_image.py` converts every figure to
   grayscale and **fails the build if type would print below 8pt** — that is the
   signal to simplify the figure, not to enlarge it. The trim size does not
   move.
4. **Print constraints in the Markdown:** headings stop at H3; tables have at
   most three columns; code blocks hard-wrap at 60 characters; callouts are
   blockquotes, never HTML `<div>` or fenced `:::` divs.
5. **Facts are verified, not remembered.** Anything that could be wrong or could
   go stale — prices, dates, version numbers, statistics, quotations — is
   checked against a primary source and logged in `sources/research/`. If it
   cannot be verified, write around it or mark it explicitly for verification
   rather than printing a confident guess. See `GOVERNANCE.md`.
6. **Respect copyright.** Do not reproduce third-party text, tables, or figures.
   Research clones are for reference only and stay out of the repo (`.gitignore`
   excludes `reference-clones/`). Log what you consulted; write original prose.

## Writing standards

- Follow `STYLE-GUIDE.md` for voice, spelling, and mechanics. It is the house
  style; when in doubt, match the surrounding prose.
- Write like the reader is an intelligent adult. Prefer plain words. Cut
  hedging, throat-clearing, and filler. The `stop-slop` skill (if installed
  under `.claude/skills/`) exists to catch AI writing tells — apply its
  guidance to any prose you draft.
- Every chapter should make the reader *decide* or *do* something, not only
  read. See the chapter template in `manuscript/ch01.md`.
- Density over length. Respect the word budget in `BOOK-SPEC.md`; check with
  `make wordcount`. Being under budget is fine; padding is not.

## How to build and check

```
bash scripts/bootstrap.sh   # first time: venv, deps, tool check, vale sync
make diagrams               # render every figure to assets/
make lint                   # Vale over the manuscript (errors block)
make test                   # fast: script + manuscript invariants
make wordcount              # prose count against the budget
make epub docx              # build both outputs into build/
make test-build             # slow: assertions against the built book
```

External tools required on PATH: `pandoc`, `vale`, `dot` (Graphviz), `mmdc`
(mermaid-cli). If a tool seems missing, check whether it is installed but off
PATH before concluding it is absent — that is a recurring trap. `bash
scripts/bootstrap.sh` reports what is present.

## Git workflow

- Never commit to `main`/`master` directly. Branch per unit of work; see
  `GOVERNANCE.md` for branch naming and commit conventions.
- Run `make hooks` once to install the pre-commit gate (Vale + fast tests). It
  blocks a commit that would break the invariants above.
- `assets/` and `build/` are gitignored. A fresh clone must render figures
  before a build produces a book with images.
- Do not open a pull request unless explicitly asked.

## What NOT to do

- Do not invent facts, statistics, citations, or quotations.
- Do not paste external copyrighted material into the manuscript or the repo.
- Do not commit rendered PNGs, build outputs, or the venv.
- Do not add colour to figures or nest headings past H3 to "fit more in".
- Do not pad to hit a page count. Solve length in positioning, not filler
  (see `AGENT-BRIEF.md`).
