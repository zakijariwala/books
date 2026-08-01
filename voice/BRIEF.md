# Voice brief

## Why this file is not the sample

I can specify your target register. I cannot write your voice sample, and if I write it, you will match it, and the book will sound like a language model doing an impression of an infrastructure engineer. Readers detect that in two pages. The one asset this book has over every generated cloud explainer is that a person who runs bank infrastructure wrote it. Handing that part to me deletes the asset.

So this file gives you the target, the extraction method, and a specimen to argue with.

---

## The target register, stated so it can be tested

A tour guide who used to run the place. Comfortable, specific, mildly amused by how systems actually behave versus how vendors describe them. Never impressed by its own knowledge.

The register passes when a paragraph contains at least two of these:

- A time, a place, or a number that could only come from being there.
- A person doing something, named by role.
- Something that went wrong, told without drama.
- A sentence you would say out loud to a colleague at lunch.

It fails when a paragraph could appear in vendor documentation with the logo swapped.

---

## Extraction: 25 minutes, no writing

Writing 500 words on demand produces your careful register, which is the wrong one. Talk instead.

Record voice notes answering these three. Do not prepare. Do not restart.

1. **The night something broke.** From the phone ringing to the fix. Tell it the way you would tell a colleague over lunch, including the part where you were wrong for the first twenty minutes.
2. **What you actually do all day**, explained to a cousin who sells insurance and has never heard of RHEL.
3. **The thing non-technical people at your office believe about infrastructure that is wrong**, and what that belief costs when nobody corrects it.

Transcribe. You have Whisper on the dev server. Then delete the filler and nothing else. No tidying, no restructuring, no better word choices. The transcript is `voice/sample.md`.

The tidying instinct is the enemy here. Your polished writing sounds like everyone's polished writing. Your talking does not.

---

## Specimen: argue with this, do not copy it

Written to the spec above. Treat it as a straw man. The useful reaction is "that is close but I would never say *transacted*" or "too many short sentences" or "an actual engineer would mention the change ticket." Every correction you make tells the project something the spec cannot.

> The bank's core ran on hardware you could touch. Two floors of it, cooled to the point where you kept a jacket at your desk. When someone in Bengaluru checked a balance at 9pm, that request landed on a machine with a serial number, in a room with a door, and somebody's name was on the maintenance contract for that door.
>
> Then the load doubled in a year, and doubling the room took eighteen months and a capital approval. That gap, between how fast demand moves and how slowly concrete moves, is the whole reason the cloud exists. Everything else in this book follows from it.
>
> The vendors will tell you cloud is about innovation. It is about the eighteen months.

Three things that passage does on purpose: it opens on a physical detail rather than a definition, it makes the business point through a number, and it takes one flat swing at vendor framing without sneering. If your transcript does none of those, the book's voice is still findable, and we tune the rules to what your transcript actually does.

---

## What happens after the transcript exists

Nothing else in the repo unblocks without it. `/article` reads it. `/draft` reads it. The Vale rules get generated from it. Twenty-five minutes of talking is the highest-leverage work left in this project.
