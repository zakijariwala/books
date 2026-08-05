---
name: review
description: Review a drafted chapter and decide ship or revise
argument-hint: [chapter number]
allowed-tools: Read, Write, Glob, Grep, Bash(vale:*)
---

Review chapter $ARGUMENTS. Read the chapter, docs/concept-registry.md,
docs/buyer.md, docs/chapter-template.md, and CLAUDE.md. Run vale on the file if
it is configured.

Write reviews/NN-review.md with these sections and nothing else:

1. REPETITION. Every passage that re-explains a concept the registry shows was
   introduced earlier. Quote both.
2. THE BUYER TEST. Per section, one sentence on what the person in buyer.md does
   differently after reading it. Where you cannot answer, write "cut or rewrite".
3. GENERIC PASSAGES. Every paragraph a chatbot would produce from a one-line
   prompt. These get replaced with the author's own material.
4. BORROWED WEIGHT. Count borrowed examples against first-hand material. Flag if
   borrowed exceeds half.
5. VOICE BREAKS. Vale output plus anything Vale cannot catch, measured against
   voice/sample.md. Quote and fix.
6. THE THREE WEAKEST SENTENCES, with rewrites.
7. VERDICT. Ship or revise. If revise, at most five named fixes in order.

Do not score anything from one to ten. Do not praise the chapter.
