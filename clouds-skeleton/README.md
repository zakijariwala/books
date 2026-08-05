# Editorial-First Book Skeleton

A lean scaffold for writing a nonfiction book with Git and AI assistance, built
around **deciding and drafting** rather than tooling. It defers the build
pipeline until you have chapters worth building, on the principle that the hard
part of a book is not converting Markdown to a PDF — it is knowing what to write,
for whom, in whose voice.

Use this variant when you want to start writing immediately and add production
tooling later. If you want the full batteries-included toolchain (Pandoc build,
figure generation, print-spec tests) from day one, use `../book-skeleton/`
instead — the consolidated seed contains everything here plus that. See
`../COMPARISON.md`.

## The idea

Most book failures are editorial, not technical: no clear reader, a table of
contents that is a topic list rather than a promise, a voice that sounds like
everyone else, invented facts and stories. This skeleton front-loads the
decisions that prevent those, and encodes them as rules an AI collaborator must
follow.

## What's here

```
CLAUDE.md          Thesis, reader, budget, voice rules, hard content rules — loads every session
HANDOVER.md        Living state doc: where things are, decisions taken, what blocks drafting
TASKS.md           The staged plan, ordered so each block unblocks the next
docs/
  buyer.md         The reader. Outcomes, layers, purchase moment. Wins scope arguments
  toc.md           Seeded chapter list, frozen only after the kill test
  chapter-template.md   The fixed shape every chapter takes, with per-section budgets
  terminology.md   One approved definition per term, so chapters do not disagree
  concept-registry.md    Where each concept is introduced and revisited
  case-study-registry.md Which example illustrates what, dated and sourced
voice/
  BRIEF.md         How to extract your voice. NOT a voice source
  sample.md        Your transcript. The only style input. Blocks everything until real
prompts/
  stage2-kill-test.md   Freeze the structure
  stage3-standards.md   Generate the standards in one run
  stage6-deferred.md    Build the pipeline, after three chapters exist
.claude/skills/    /article /draft /review /approve /verify
setup.sh           Lean install: Vale + Pandoc. Diagram tools deferred
manuscript/ articles/ reviews/ scripts/   Fill as you go
```

## How to start

1. Copy this directory to a new repo, `git init`.
2. Write the **thesis** into `CLAUDE.md` and the **reader** into `docs/buyer.md`.
   These two decisions govern everything else.
3. **Extract your voice:** follow `voice/BRIEF.md`, record, transcribe, paste the
   raw transcript into `voice/sample.md`. Do not tidy it. This blocks drafting.
4. **Freeze the TOC:** run `prompts/stage2-kill-test.md`, fold the cuts into
   `docs/toc.md`, commit.
5. **Generate the standards:** run `prompts/stage3-standards.md`.
6. **Pilot before you commit to chapters:** `/article` two or three chapters,
   publish, see who responds. Then draft with `/draft → /review → /verify →
   /approve`.
7. Once three chapters are approved, run `prompts/stage6-deferred.md` to add the
   diagram and build pipeline.

## First stop for an AI collaborator

Read `CLAUDE.md`, then `docs/buyer.md`. Do not draft a chapter before reading the
four files `CLAUDE.md` names under "What this repo is".
