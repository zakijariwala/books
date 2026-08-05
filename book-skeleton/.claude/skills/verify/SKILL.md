---
name: verify
description: Check factual claims against primary sources
argument-hint: [chapter number]
allowed-tools: Read, Write, WebSearch, WebFetch
---

Read chapter $ARGUMENTS. Extract every factual claim — numbers, dates, named
entities, technical assertions, history. List them all before checking any.

For each claim, search and fetch a primary source: the original document, the
vendor's or organisation's own page, an official record. Mark it VERIFIED with
the URL and the page's publication or update date, UNVERIFIED, or CONTRADICTED
with the correct version. Flag any claim that ages badly within two years even
when true today, so it can be dated in the text or written around.

Never mark anything verified from your own knowledge without a fetched source.
Do not rewrite the chapter. Write the results into a fact log under
sources/research/ (one file per topic, see sources/research/_TEMPLATE.md) so the
verification record lives with the rest of the book's sources, and update the
"Facts to verify" table in BOOK-SPEC.md.
