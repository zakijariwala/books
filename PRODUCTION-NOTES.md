# Production Notes

For whoever lays out the interior — you, or a freelance typesetter you hire.
The Pandoc pipeline in this repository produces a correct, print-ready DOCX;
these are the decisions the source cannot express and someone has to make in
Word before uploading to KDP.

## Trim and measure

6x9in, black-and-white interior. Inside margin 0.875in, outside 0.625in, top
and bottom 0.75in, giving a 4.5in measure. Mirrored margins so the gutter
alternates on facing pages — `scripts/patch_docx.py` sets this, because Pandoc
drops it.

Every figure is rendered to fit that measure exactly and is already grayscale
at 300 DPI. Do not rescale figures upward: type in them is set close to an 8pt
floor and several are already at it.

## High-yield pages: give these distinct treatment

Five spreads carry disproportionate value. Readers will bookmark, screenshot,
and photocopy them, and they should be findable by flicking through the block
rather than by consulting the index.

| Page | Where |
| --- | --- |
| The database selection matrix | ch06, "The database selection matrix" |
| Security control mapping | ch09, "Security control mapping" |
| Compute selection cheat sheet | ch04, "Compute selection cheat sheet" |
| Appendix A, decision cheat sheets | back matter |
| Appendix B, exam traps | back matter |

Suggested treatment, in order of preference:

1. **Shaded background panel** behind the whole table, bleeding to the measure,
   with the section heading reversed out or rules above and below. Distinct
   from body pages at a glance when the book is fanned.
2. **Full-page or full-spread placement**, table set to fill the page rather
   than sitting in the text flow. The database matrix and Appendix B in
   particular deserve to start on a fresh recto.
3. **Thumb tabs or edge marks** on the outside margin of these pages. Cheap on
   a mono interior and it makes the appendices usable under time pressure,
   which is precisely when they are read.

Whatever treatment is chosen, apply it consistently to all five so the reader
learns the visual signal.

## Tables generally

Three columns maximum throughout, which is a hard constraint of the measure and
is enforced by the test suite. Tables must not be rotated to landscape; several
run long and should break across pages with the header row repeating.

Appendix B's trap tables are the longest in the book. Breaking them across
pages is fine; splitting a single trap's row across a page boundary is not.

## Figures

- 33 figures, numbered per chapter as `Figure N.M`
- 11 are close to full-page height. Set them on their own page rather than
  forcing surrounding text into a sliver
- Captions must stay with their figure. An orphaned caption is the single most
  likely layout defect in this manuscript
- Sources live in `diagrams/`; regenerate rather than editing the PNGs

## Front matter

- Half title, title, copyright, contents, then "About this book"
- "How to read this book" is a section of the front matter and should not be
  demoted to a preface that readers skip. It sets up the drills, which are a
  third of the book's value
- The imprint line in `metadata.yaml` is unset. KDP requires a publisher name:
  either an invented imprint or "Independently published"

## Part structure

Part I is chapters 1-12, Part II is 13-17. Part II opens with its own front
page ("Why these are not Google's case studies") which should be set as a part
opener, not as a chapter heading.
