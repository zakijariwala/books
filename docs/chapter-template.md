# Chapter template

**This is a coverage requirement, not a running order.** Every chapter must do
the eight jobs below and must serve both readers. Nothing here says the jobs
appear in a fixed sequence, under fixed headings, in every chapter.

That distinction is not pedantry. It was written the other way first, as a
numbered running order, and twelve chapters were drafted against it. The result:
all twelve ended with the same five identically titled sections in the same
order, and a reader sees the machinery by chapter three. The layer rule in
docs/buyer.md asks that both readers be served. It never asked for identical
headings.

Read docs/toc.md, docs/concept-registry.md, and docs/terminology.md before
drafting any chapter.

Two failure tests from buyer.md, applied to every draft:
- **The layer test.** If a reader stops once the belief has been corrected, did
  they get something worth the evening? If no, the chapter is written only for
  Meera and the second layer quits.
- **The reverse test.** If only the opening and the correction are any good, the
  chapter has drifted to general interest and Meera stops paying.

---

## The arc

Every chapter runs from exposure to competence. It opens on something going
wrong and ends on the reader knowing what to do. The opening scene is a room
overheating, a question nobody could answer, a bill nobody could explain. The
Monday question hands her the move. Between those two points the feeling shifts
from "I would not have known that" to "I can ask that on Tuesday."

This is a structural requirement, not a mood. /review checks it:

- **A chapter that opens comfortable has no reason to be read.** If the opening
  scene contains no failure, no exposure, and nothing at stake, rewrite it.
- **A chapter that ends anxious has taken something and given nothing back.**
  If the last two sections leave the reader worried rather than equipped, the
  chapter fails, however accurate it is.

Two findings from Poels and Dewitte's 2006 review of emotion measurement in
advertising sit behind this, and they are about advertising rather than books,
so treat them as support and not proof:

- Material works better when the emotional reaction shifts from negative to
  positive across the experience, rather than sitting still. A static ad, or a
  chapter that stays at one emotional altitude, does less work.
- Arousal predicts recall better than pleasantness does. The passages a reader
  can still repeat next month are the ones with something at stake, which is
  the argument for spending the STORY-TODO beats well. The 2am call earns its
  place twice: once because it is true, and once because it is the part she
  will retell.

---

## The eight jobs

Every chapter does all eight. The order is the writer's, chosen for the material.
The rough sizes are there to stop one job eating the chapter, not to be totalled.

| Job | Serves | Rough size | What it has to accomplish |
|-----|--------|-----------|---------------------------|
| **Open on exposure** | Second layer | 400-500 | A person, a place, a thing going wrong. No term the English major must already know. Start on the concrete noun. |
| **Name the stake** | Both | 350-450 | Money and consequence, not architecture. What it costs, who pays, what happens when it breaks. |
| **Build the model** | Second layer first, Meera second | 900-1,100 | The mental model lands before the vocabulary. Analogy from the approved set. The photo-thread callback rides here, two or three sentences. |
| **Work it through** | Meera | 600-750 | Where the utility lives and the terms get used properly. This earns O1-O6. |
| **Show it happening** | Meera | 500-650 | A first-hand story or a borrowed case study. Missing first-hand beats are `<!-- STORY-TODO: ... -->`. |
| **Correct the belief** | Second layer | 350-450 | The wrong thing everyone holds. Needs no job to understand. |
| **Leave three things** | Both | 200-300 | What the reader keeps. No new material. |
| **Hand her the move** | Meera | 50-100 | One question to ask at work. These twelve become the discussion guide. |

## How to vary it

The jobs are fixed. Everything else is a choice, and the choice should follow
the material:

- **Order.** A chapter with a strong incident can open on the incident and reach
  the model late. A chapter built on a trade can open on the trade. Chapter 7
  should let the reader feel the contradiction before it explains replication.
- **Headings.** Name sections for their content, not their function. "The
  librarian" and "Who sees stale data" are headings. "The business problem" is a
  label from a template, and twelve of them in a row read as a curriculum.
- **Merging.** Two jobs can share a section where they belong together. Naming
  the stake and correcting the belief often want to be the same passage.
- **The tail.** Do not let the last three jobs become a fixed closing sequence.
  A chapter can end on the story, or on the misconception, or on the question.

**The repetition test, applied across chapters rather than inside one:** lay the
section headings of every drafted chapter side by side. If more than half share a
heading, the book has a formula and the reader will find it before you do.

---

## Rules that apply inside the template

- **The callback thread** (docs/toc-review.md section 5) rides at the top of
  section 3, two or three sentences, reusing the same photo, user, and moment
  introduced in chapter 2.
- **First-hand stories** are never invented and never attributed to the author
  from a model. Missing ones are `<!-- STORY-TODO: what this needs -->`.
- **Borrowed case studies** (Netflix, Spotify, Airbnb, Shopify, Capital One)
  fill at most half of any chapter's examples, and every borrowed claim carries
  a source and a fact-check date in docs/case-study-registry.md.
- **Cost is taught as shape, not price.** No dollars, no rate cards. See
  CLAUDE.md hard content rules.
- **Figures** are grayscale-safe, one idea each, at most six labels. Mark planned
  figures `<!-- FIGURE: what it shows -->`. Numbering and captions live in
  figures/manifest.json. See docs/figures.md.
- **Say it once.** Reach the insight, land it, move on. If an argument is made,
  then restated for Meera, then restated in the summary, the reader has been told
  three times that they were not trusted the first time.
- **Voice** follows CLAUDE.md: rhythm and argument from voice/reference-article.md,
  first-hand register from voice/sample.md.

## Omitting a job

Any job may be omitted when the chapter is genuinely better without it. Note the
omission at the top of the draft with a reason, so /review reads it as a decision
rather than a gap. The one job that cannot be dropped is opening on exposure.
