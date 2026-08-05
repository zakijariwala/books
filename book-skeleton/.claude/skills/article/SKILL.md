---
name: article
description: Draft a standalone article that pilots a book chapter
argument-hint: [chapter number or topic]
allowed-tools: Read, Write, Glob, Grep
---

Draft a standalone article on $ARGUMENTS for publication (blog, LinkedIn,
newsletter). It pilots a chapter: cheap to publish, and it tests demand before
the chapter is written. Read CLAUDE.md, voice/sample.md, docs/buyer.md, and
docs/toc.md first.

Rules:
- 1,100 to 1,400 words. It stands alone. Never reference the book.
- Open on a concrete scene. No definitions in the first 200 words.
- One idea. One analogy. One takeaway the reader can use at work or in life.
- Mark where the author's own story goes with `<!-- STORY-TODO: ... -->`.
  Invent nothing.
- End with a question that invites the reader to answer from their own
  experience.
- Propose three headline options at the top of the file.

Write to articles/NN-slug.md.
