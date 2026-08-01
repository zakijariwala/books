# Exam guide, verified

`VERIFIED` against Google's official exam guide PDF, version 6.1, read directly
rather than summarised. This file overrides any conflicting claim elsewhere in
this folder.

Source: <https://cloud.google.com/learn/certification/guides/professional-cloud-architect>
which redirects to
<https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf>

## Sections and weights

Six sections. Weights sum to 100.

| # | Section | Weight |
| --- | --- | --- |
| 1 | Designing and planning a cloud solution architecture | ~25% |
| 2 | Managing and provisioning a cloud solution infrastructure | ~17.5% |
| 3 | Designing for security and compliance | ~17.5% |
| 4 | Analyzing and optimizing technical and business processes | ~15% |
| 5 | Managing implementation | ~12.5% |
| 6 | Ensuring solution and operations excellence | ~12.5% |

Note section 6 is "operations **excellence**", not "reliability", and the guide
ties it to the operational excellence pillar of the Architecture Framework.

Design and planning at 25% is the single heaviest section, and it is exactly
the judgment layer this book sells. Sections 4 and 5 together are 27.5% and are
the least served by Google's own learning path.

## Case studies

Four, and **three of the classic set are retired**.

| Case study | Status |
| --- | --- |
| Altostrat Media | Current |
| Cymbal Retail | Current |
| EHR Healthcare | Current |
| KnightMotives Automotive | Current |
| Mountkirk Games | RETIRED |
| Helicopter Racing League | RETIRED |
| TerramEarth | RETIRED |
| Dress4Win | RETIRED |

Official texts, linked from the exam guide itself:

- <https://services.google.com/fh/files/misc/v6.1_pca_altostrat_media_case_study_english.pdf>
- <https://services.google.com/fh/files/misc/v6.1_pca_cymbal_retail_case_study_english.pdf>
- <https://services.google.com/fh/files/misc/v6.1_pca_ehr_healthcare_case_study_english.pdf>
- <https://services.google.com/fh/files/misc/v6.1_pca_knightmotives_automotive_case_study_english.pdf>

Read these. Do not reproduce them. See `flags-stale-and-legal.md`.

## Format

- Each exam includes **2 case studies**, shown on a split screen
- Case study questions are **20-30% of the exam**
- Guide version 6.1

Question count, duration, cost, and recertification period still need
confirming from the certification landing page rather than the guide.

## What this invalidates

Two things previously treated as current turned out to be stale, and both were
load-bearing.

**Three retired case studies.** `case-studies.md` analyses Mountkirk,
Helicopter Racing League, and TerramEarth as if live. Their *patterns* stay
useful, since global scale, media streaming, and fleet telemetry are all still
plausible exam material. Their *names and specifics* must not appear in the
book as current.

**Both new case studies are generative-AI scenarios**, confirming the earlier
inference from the reference repo. Altostrat Media and Cymbal Retail both
centre on GenAI adoption. Chapter 8 on AI/ML infrastructure is now clearly
justified rather than speculative, and the Part II case studies should weight
toward AI-era problems rather than classic lift-and-shift.

KnightMotives Automotive is new and unanalysed. Read it before finalising the
Part II case study set: an automotive scenario likely covers connected-vehicle
telemetry, which is the niche TerramEarth used to occupy.
