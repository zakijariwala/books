# Stage 6: deferred until three chapters exist

Do not run this now. It has no input yet.

```
Now that manuscript/ holds three approved chapters and docs/figures.md lists
their figures:

1. Draw the listed figures with Mermaid or the Python diagrams library.
   Grayscale, one idea per figure, at most six labels, readable in isolation.
2. Add a `make diagrams` target that converts output to 300 DPI grayscale PNG at
   roughly 1350px width for a 6x9 trim, using ImageMagick.
3. Add a `make build` target that assembles the manuscript with Pandoc.
4. Write scripts/wordcount.py: parse manuscript/, report words per chapter
   against budget, total against 56,000, and count remaining STORY-TODO and
   FIGURE markers. Add a `make status` target.
```
