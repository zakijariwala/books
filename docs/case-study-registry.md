# Case study registry

Which company illustrates what, and where. Two rules from CLAUDE.md:

- Borrowed case studies (Netflix, Spotify, Airbnb, Shopify, Capital One) fill at
  **most half** of any chapter's examples. The other half is first-hand.
- Every borrowed claim carries a **source** and a **fact-check date**. Nothing
  goes into a draft from this table until its Verified column is a date, set by
  /verify. Rows below are seeded mappings, not verified facts. Do not cite them
  until checked.

Status legend: `SEED` = candidate mapping, unverified. `OK <date>` = checked via
/verify. `STORY-TODO` = first-hand slot the author fills.

---

## Borrowed rows (verify before use)

| Chapter | Company | Illustrates | Source | Verified |
|---------|---------|-------------|--------|----------|
| 2 | (choose one) | A single user action fanning out across services | TODO | SEED |
| 8 | (candidate) | Traffic spike survived by elasticity | TODO | SEED |
| 9 | (candidate) | A public outage and what it did not cover | TODO | SEED |
| 11 | Capital One | Cloud economics / a large regulated migration | TODO | SEED |
| 12 | (hyperscalers, named generically) | AI-era capacity scramble and capex | TODO | SEED |

Borrowed examples are deliberately thin here. The reader can get Netflix and
Spotify free in thirty seconds (buyer.md). Prefer first-hand. When a borrowed
case is used, /verify fills Source and Verified before it enters a draft.

## First-hand rows (author fills)

One per chapter minimum, per CLAUDE.md. Left empty on purpose. Fill from the
voice transcript and the author's own work. Never invented.

| Chapter | The story it needs | Status |
|---------|--------------------|--------|
| 1 | The night the room filled past what it could cool; wrong for the first twenty minutes | STORY-TODO |
| 2 | A real upload followed end to end in a system the author ran | STORY-TODO |
| 3 | A data residency question answered live, on a real call | STORY-TODO |
| 4 | An "we need bigger instances" moment and what it actually cost | STORY-TODO |
| 5 | Data that was cheap to keep and expensive to move | STORY-TODO |
| 6 | The distant customer who saw a slower product | STORY-TODO |
| 7 | The stale-read incident; someone saw data that was not there yet | STORY-TODO |
| 8 | The traffic event that was planned for, or was not | STORY-TODO |
| 9 | The half-succeeded write; the thing nobody could find, still being paid for | STORY-TODO |
| 10 | The compromise whose blast radius was larger than expected | STORY-TODO |
| 11 | The bill line that grew, and the product decision behind it | STORY-TODO |
| 12 | Being inside the capacity scramble; a region that could not give you what you asked for | STORY-TODO |
