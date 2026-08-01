---
name: verify
description: Check factual claims against vendor documentation
argument-hint: [chapter number]
allowed-tools: Read, Write, WebSearch, WebFetch
---

Read chapter $ARGUMENTS. Extract every factual claim about AWS, Azure, GCP, or
cloud history. List them all before checking any.

For each claim, search and fetch the vendor's own documentation or an official
post. Mark it VERIFIED with the URL and the page's publication or update date,
UNVERIFIED, or CONTRADICTED with the correct version. Flag any claim that ages
badly within two years even when true today.

Never mark anything verified from your own knowledge without a fetched source.
Do not rewrite the chapter. Write to reviews/NN-facts.md.
