# [BOOK TITLE]

The operating manual for AI assistance on this book. Loads every session. Keep
it accurate; it is the single source of truth for how this book gets written.

## Thesis

[One paragraph. Every chapter, analogy, case study, and figure serves this
sentence. Cut anything that does not. Write this before drafting anything —
until it exists, the kill test in `prompts/stage2-kill-test.md` has nothing to
score chapters against.]

## What this repo is

A nonfiction book. Chapters live in `/manuscript` as Markdown. **Never write
chapter content without first reading** `docs/toc.md`,
`docs/chapter-template.md`, `docs/concept-registry.md`, and
`docs/terminology.md`.

## Reader

`docs/buyer.md` wins any argument about scope. When a section could serve the
reader or could serve the topic, it serves the reader.

## Budget

[TOTAL] words total. [N] chapters. [PER-CHAPTER] words per chapter. Report the
word count after every draft.

## Principles

[The ordering rules that keep the book coherent. Examples from a business-reader
book, replace with your own:]

- Story before concept. Concept before terminology.
- Business consequence before implementation detail.
- Vendor and tool neutrality unless the book's subject is one tool.
- Every chapter answers a fixed set of questions. State them here so every
  chapter is the same shape.

## Voice

**`voice/sample.md` is the only style source.** Match it. Do not read
`voice/BRIEF.md` as a voice input — the specimen inside it is model prose, and
matching it deletes the book's one advantage.

These rules override any default style. [Seed with the ones below; add three
more extracted from `voice/sample.md`, each quoting the sentence it came from.]

- No em dashes.
- Active voice with human subjects. People do things; systems do not happen.
- No adverbs where a stronger verb will do.
- No "not X, it's Y" constructions.
- No throat-clearing openers. Start on the concrete noun.
- Specific nouns over vague declaratives.
- Vary sentence length. Short sentences carry weight.
- [Narrator persona: who is telling this, and what they never do.]

## Hard content rules

[The non-negotiables for this book's factual and ethical integrity. Seeded from
a technical-nonfiction book; adapt.]

- Never invent a first-hand story or attribute one to the author. When it is not
  written yet, insert `<!-- STORY-TODO: what this needs -->` and move on.
- Never state a fact that can go stale (prices, versions, tiers, quotas) without
  the year it was true, or write around it. See `/verify`.
- Borrowed case studies fill at most half of any chapter's examples. The reader
  can get those free in thirty seconds. The other half is the author's own work.
- Analogies stay in one register. [Name it — e.g. everyday physical systems. No
  fantasy, no sci-fi.]
- Grayscale-safe figures only. No colour-dependent meaning.

## Registries

- `docs/concept-registry.md` records where each concept is introduced and
  revisited. Read it before drafting so you reference rather than re-teach.
- `docs/case-study-registry.md` records which example illustrates what, and
  where, so no company is overused and every borrowed one is dated and sourced.
- `/approve` updates both. Never edit a chapter's status by hand.

## Workflow

The book is written in stages, not all at once. See `TASKS.md` for the ordered
plan and `prompts/` for the staged prompt text. The agent skills drive drafting:

- `/article N` — draft a standalone pilot article for chapter N.
- `/draft N` — draft chapter N from the frozen TOC.
- `/review N` — review a draft; decide ship or revise.
- `/verify N` — fact-check a draft against primary sources.
- `/approve N` — record an approved chapter in the registries.

Governing rule: **build only what the next 5,000 words need.** The diagram
pipeline and the word-count script are deferred until three chapters exist
(`prompts/stage6-deferred.md`).
