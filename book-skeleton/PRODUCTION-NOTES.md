# Production Notes

For whoever lays out the interior — you, or a freelance typesetter you hire.
The Pandoc pipeline produces a correct, print-ready DOCX; these are the
decisions the source cannot express and someone has to make in Word (or InDesign)
before uploading to a print-on-demand service.

Fill in the book-specific parts; the trim and mechanics are the skeleton
defaults.

## Trim and measure

6x9in, black-and-white interior. Inside margin 0.875in, outside 0.625in, top and
bottom 0.75in, giving a 4.5in measure. Mirrored margins so the gutter alternates
on facing pages — `scripts/patch_docx.py` sets this, because Pandoc drops it.

Every figure is rendered to fit that measure exactly and is already grayscale at
300 DPI. **Do not rescale figures upward:** type in them is set close to an 8pt
floor and several may already be at it.

Changing the trim means editing `scripts/make_reference_docx.py` and
`scripts/normalize_image.py` together, then re-rendering every figure.

## High-yield pages

TODO: List the two to five pages that carry disproportionate value — the tables
and cheat sheets readers will bookmark, screenshot, and photocopy. Give them
distinct layout treatment so they are findable by fanning the book:

1. **Shaded background panel** behind the whole table, so it stands out at a
   glance when the block is riffled.
2. **Full-page or full-spread placement** for the densest tables, set to fill
   the page rather than sitting in the text flow.
3. **Thumb tabs or edge marks** on the outside margin — cheap on a mono
   interior, and they make reference pages usable under time pressure.

Apply whatever treatment you choose consistently, so the reader learns the
signal.

## Tables

Three columns maximum throughout (enforced by the test suite). Do not rotate
tables to landscape; long ones should break across pages with the header row
repeating, but a single logical row should not split across a page boundary.

## Figures

- Numbered per chapter as `Figure N.M`; sources live in `diagrams/`.
- Figures near full-page height should sit on their own page rather than forcing
  surrounding text into a sliver.
- **Captions must stay with their figure.** An orphaned caption is the single
  most likely layout defect. Check every one in the built DOCX.
- Regenerate from source rather than editing the PNGs.

## Front matter

- Half title, title, copyright, contents, then the "About this book" material.
- "How to read this book" belongs in the front matter, not demoted to a preface
  readers skip — it sets up any devices (drills, appendices) the book relies on.
- The imprint line in `metadata.yaml` must be set before upload: an invented
  imprint or "Independently published".

## Before uploading

- [ ] Imprint name set in `metadata.yaml`.
- [ ] Cover made (ebook: portrait RGB, ~1600x2560; paperback: wraparound built
      to the service's spine calculator once the final page count is known).
- [ ] Layout pass done in Word, high-yield pages given their treatment.
- [ ] Built EPUB checked in an actual reader for reflow, especially wide tables.
- [ ] Pre-publication facts verified (`BOOK-SPEC.md`).
- [ ] Marketing description drafted (`AGENT-BRIEF.md`).
