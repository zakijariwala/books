# Stage 3: standards, in one run

Run after `docs/toc.md` is frozen and `voice/sample.md` exists. Generates the
standards that keep every chapter consistent, so you are not re-deciding them mid
draft.

```
Read voice/sample.md, docs/buyer.md, docs/toc.md, and CLAUDE.md.

1. docs/chapter-template.md
   Confirm the section list fits this book. Set a word budget per section
   totalling the per-chapter target in CLAUDE.md. Mark optional sections. If the
   book has a second layer of reader, map each section to the reader it serves.

2. docs/terminology.md
   Every term the frozen TOC forces the book to use: chosen spelling,
   capitalisation, naming convention, and one approved short definition each, so
   no two chapters define a term differently.

3. docs/concept-registry.md
   Prefill from the TOC: concept, the chapter that introduces it, and its
   approved one-line definition.

4. docs/case-study-registry.md
   Prefill the borrowed-example candidates with sources and fact-check dates.
   Leave first-hand rows empty for the author.

5. .vale.ini and .vale/styles/Book/
   Translate CLAUDE.md's voice rules and prohibited language into Vale rules —
   at minimum: em dashes, -ly adverbs, the "not X, it's Y" pattern, and any
   jargon / evangelism / filler lists the book bans. Use existence and
   substitution rule types. Severity: warning, not error.

6. setup.sh
   Install and verify Vale and Pandoc. Leave the diagram tools (Graphviz, the
   Python diagrams library, mermaid-cli) commented out with a note that they are
   needed at Stage 6. Run it and report what failed.

Then update CLAUDE.md's voice section with three concrete rules extracted from
voice/sample.md that are not already listed, each quoting the sentence it came
from. Do not write chapter content.
```

Edit `docs/terminology.md` yourself after this runs.
