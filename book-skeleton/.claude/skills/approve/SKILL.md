---
name: approve
description: Record an approved chapter in the registries
argument-hint: [chapter number]
allowed-tools: Read, Write, Edit, Glob, Grep
---

Chapter $ARGUMENTS is approved. Refuse to run if the chapter still contains
STORY-TODO markers — an approved chapter with an unwritten story is not approved.

1. Add every concept the chapter introduced to docs/concept-registry.md with its
   approved one-line definition. Update the "revisited in" column for concepts it
   reused.
2. Add every example used to docs/case-study-registry.md, marked borrowed or
   first-hand, with its source and today's date.
3. Append the chapter's figure list to docs/figures.md, creating the file if
   needed. One line per FIGURE marker.
4. Report the running manuscript word count against the CLAUDE.md target.
