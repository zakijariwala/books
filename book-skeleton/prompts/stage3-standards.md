# Stage 3: standards, in one run

Run after `docs/toc.md` is frozen and `voice/sample.md` exists. Generates the
standards that keep every chapter consistent, so they are not re-decided mid
draft.

Unlike the lean variant, this seed already ships `.vale.ini`, the vocabulary
files under `styles/`, and `scripts/bootstrap.sh`. So this stage fills the
standards docs and adds voice-specific lint rules, rather than creating the
toolchain from scratch.

```
Read voice/sample.md, docs/buyer.md, docs/toc.md, BOOK-SPEC.md, and CLAUDE.md.

1. docs/chapter-template.md
   Confirm the section list fits this book. Set a word budget per section
   totalling the per-chapter target in BOOK-SPEC.md. Mark optional sections. If
   the book has a second layer of reader, map each section to the reader it
   serves. Keep it consistent with manuscript/ch01.md (the fill-in template).

2. docs/terminology.md
   Every term the frozen TOC forces the book to use: chosen spelling,
   capitalisation, naming convention, and one approved short definition each.

3. docs/concept-registry.md
   Prefill from the TOC: concept, the chapter that introduces it, and its
   approved one-line definition.

4. docs/case-study-registry.md
   Prefill the borrowed-example candidates with sources and fact-check dates.
   Leave first-hand rows empty for the author.

5. Voice lint rules
   Extract this book's voice rules from voice/sample.md and CLAUDE.md and add
   them to enforcement: banned words to styles/config/vocabularies/Book/reject.txt,
   and any pattern rules (em dashes, "not X, it's Y", -ly adverbs, jargon lists)
   as a custom Vale style under styles/Book/ referenced from .vale.ini. Severity
   warning, not error.

Then update CLAUDE.md's voice section with three concrete rules extracted from
voice/sample.md that are not already listed, each quoting the sentence it came
from. Do not write chapter content.
```

Edit `docs/terminology.md` yourself after this runs — it does not survive being
left entirely to a model.
