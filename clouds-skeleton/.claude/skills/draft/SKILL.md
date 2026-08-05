---
name: draft
description: Draft one chapter from the frozen TOC
argument-hint: [chapter number]
allowed-tools: Read, Write, Glob, Grep
---

Draft chapter $ARGUMENTS to manuscript/chNN.md.

Before writing, read and report back on:
1. docs/toc.md. Quote this chapter's one-line promise.
2. docs/chapter-template.md. Follow its sections and per-section budgets.
3. docs/concept-registry.md. List every concept already introduced that this
   chapter must reference rather than re-teach, and name the chapter it came
   from.
4. docs/case-study-registry.md. List which examples are already spent, and on
   what, so this chapter does not overuse one.
5. The published article in articles/ covering this material, if one exists. Its
   voice is the target.
6. voice/sample.md. Match it.

Constraints:
- Stay in budget. Report the word count.
- Open on a scene or a decision someone had to make. Never on a definition.
- Mark first-hand material with `<!-- STORY-TODO: ... -->`. Invent nothing.
- Mark figures with `<!-- FIGURE: one line describing what it must show -->`.
  Draw nothing.
- If the TOC and the template conflict, stop and ask.
