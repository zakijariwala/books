# Style Guide

Prose mechanics for this book. Vale enforces what can be automated
(`.vale.ini` + `styles/`); this document holds the mechanical decisions a linter
needs told. **Register and voice do not live here — they live in
`voice/sample.md`**, which is the authoritative style source. When drafting,
match the sample; use this guide for spelling, punctuation, and banned words.

## Voice (pointer)

The voice is defined by `voice/sample.md` — the author's own transcript, not a
rules list. Extract it per `voice/BRIEF.md` before drafting. The rules below are
the mechanical floor that applies under any voice:

- Write to be understood on one read. Prefer the plain word to the impressive
  one.
- Cut hedging and throat-clearing: "it is worth noting that", "in order to",
  "very", "really", "basically". If the `stop-slop` skill is installed, apply
  it to every draft — it targets the predictable tells of machine-written prose.
- As you extract voice rules from the sample (e.g. "no em dashes", "no -ly
  adverbs", "no 'not X, it's Y'"), record them in `CLAUDE.md`'s voice section and
  turn the mechanical ones into Vale rules (see `prompts/stage3-standards.md`).

## Spelling and regional English

- TODO: Choose **en-US** or **en-GB** and commit to it everywhere. This must
  match `lang` in `metadata.yaml`.
- Record the specific choices that recur: e.g. Oxford comma yes/no; "-ise" vs
  "-ize"; how you set em dashes (spaced or closed up — Google's rule is disabled
  in `.vale.ini` so the choice is yours).

## Mechanics that the build depends on

These are not taste; the pipeline and tests require them.

- **Headings:** H1 for chapter, H2 for section, H3 for subsection. Stop at H3.
- **Tables:** three columns maximum.
- **Code blocks:** hard-wrap at 60 characters (monospace overflows the 6x9
  measure past that).
- **Callouts:** blockquotes only — `> **Note.** ...`. No HTML `<div>`, no
  fenced `:::` divs.
- **Figures:** referenced by relative PNG path, captioned `Figure N.M`, with a
  matching source in `diagrams/`.

## Terminology

- Keep a consistent name for each concept; do not elegantly vary it. Readers
  track terms, not synonyms.
- When Vale flags a correct technical term or proper noun, add it to
  `styles/config/vocabularies/Book/accept.txt` (entries are regexes — use
  `[Aa]` for sentence-initial capitals) rather than rewording.
- Words this book bans go in `.../Book/reject.txt` so Vale catches them.

## Numbers, dates, references

- TODO: State conventions (e.g. spell out one to nine, numerals for 10+;
  ISO or long-form dates; how citations are formatted).
- Any number that could be wrong or go stale is verified and logged — see
  `GOVERNANCE.md` and `sources/research/`.
