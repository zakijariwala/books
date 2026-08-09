# Chapter template

Every chapter follows this shape. The per-section budgets total 3,800 to 4,200
words. The "Serves" column comes straight from docs/buyer.md's layer rule and is
checked during /review. Read docs/toc.md, docs/concept-registry.md, and
docs/terminology.md before drafting any chapter.

Two failure tests from buyer.md, applied to every draft:
- **The layer test.** If a reader stops after The Misconception, did they get
  something worth the evening? If no, the chapter is written only for Meera and
  the second layer quits.
- **The reverse test.** If only the opening scene and the misconception are any
  good, the chapter has drifted to general interest and Meera stops paying.

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

## Sections, in order

| # | Section | Serves | Budget | What it does |
|---|---------|--------|--------|--------------|
| 1 | Opening scene | Second layer | 400-500 | A person, a place, a thing going wrong. No term the English major must already know. Start on the concrete noun. |
| 2 | The business problem | Both | 350-450 | State it as money and consequence, not architecture. What does this cost, who pays, what happens when it breaks. |
| 3 | Core explanation | Second layer first, Meera second | 900-1,100 | The mental model lands before the vocabulary. Analogy from the approved set. The photo-thread callback opens this section in 2-3 sentences. |
| 4 | Worked example | Meera | 600-750 | Where the utility lives and where the terms get used properly. This is the section that earns O1-O6. |
| 5 | Inside a real organization | Meera | 500-650 | A first-hand story or a borrowed case study. First-hand carries at least half. Mark missing first-hand beats `<!-- STORY-TODO: ... -->`. |
| 6 | The misconception | Second layer | 350-450 | The wrong belief everyone holds, corrected. Needs no job to understand. For ch10 this section carries the chapter. |
| 7 | Summary | Both | 200-300 | The three things a reader keeps. No new material. |
| 8 | Monday question | Meera | 50-100 | One question she should ask at work. Second layer reads it and moves on. These twelve become the discussion guide. |

Midpoint total: ~3,975 words.

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
- **Figures** are grayscale-safe, one idea each, at most six labels. Do not draw
  them until three chapters are approved. Mark planned figures `<!-- FIGURE:
  what it shows -->`.
- **Voice** follows CLAUDE.md: rhythm and argument from voice/reference-article.md,
  first-hand register from voice/sample.md.

## Optional sections

- **Inside a real organization** may be omitted only when a chapter has two
  strong first-hand stories elsewhere and the word budget is tight. Note the
  omission at the top of the draft so /review does not flag it as missing.
