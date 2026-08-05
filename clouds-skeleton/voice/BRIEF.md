# Voice brief

## Why this file is not the sample

A model can specify your target register. It cannot write your voice, and if it
writes it, you will match it, and the book will sound like a language model doing
an impression of an author. Readers detect that in two pages. For a book whose
advantage is that a real person with real experience wrote it, handing the voice
to a model deletes the advantage.

So this file gives you the target, the extraction method, and a specimen to argue
with. It is not a style source. **`voice/sample.md` is the only style source.**

---

## The target register, stated so it can be tested

[Describe the voice in one or two sentences — who is speaking and how. Example:
"Someone who has done the work, explaining it to a smart friend over lunch.
Specific, a little amused, never impressed by its own knowledge."]

The register passes when a paragraph contains at least two of these:

- A time, a place, or a number that could only come from having been there.
- A person doing something, named by role.
- Something that went wrong, told without drama.
- A sentence you would say out loud to a colleague.

It fails when a paragraph could appear in generic documentation with the subject
swapped.

---

## Extraction: talk, do not write

Writing 500 words on demand produces your careful register, which is the wrong
one. Talk instead. Record voice notes answering prompts like these — adapt to
your subject. Do not prepare. Do not restart.

1. **The time something went wrong.** From the start to the fix, told the way you
   would tell a colleague, including the part where you were wrong at first.
2. **What you actually do**, explained to someone outside your field entirely.
3. **The thing people around you believe about your subject that is wrong**, and
   what that belief costs when nobody corrects it.

Transcribe (Whisper works well). Then delete the filler and nothing else. No
tidying, no restructuring, no better word choices. The transcript is
`voice/sample.md`. The tidying instinct is the enemy: your polished writing
sounds like everyone's polished writing; your talking does not.

---

## Specimen: argue with this, do not copy it

[Write, or have a model write, one short passage to the target register above,
and treat it as a straw man. The useful reaction is "that is close but I would
never say X" or "too many short sentences" or "a real practitioner would mention
Y". Every correction you make is a rule the spec could not produce — add it to
CLAUDE.md's voice list, quoting the sentence that prompted it.]

> [Specimen paragraph.]

---

## What happens after the transcript exists

Nothing downstream unblocks without it. `/article` reads it, `/draft` reads it,
the Vale rules are generated from it. The transcript is the highest-leverage work
in the project.
