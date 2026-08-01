# Datapoints

Research notes extracted from third-party sources. Input to drafting, never
output.

## Usage rules

**Nothing in this folder goes into the manuscript as prose.** These are other
people's notes, under their copyright, some of it redistributed Google material
that was already restricted. Extract the *fact* or the *decision*, verify it
against Google's current documentation, then write it fresh in your own voice.

Every point below carries a confidence tag:

- `VERIFIED` — checked against current Google documentation
- `UNVERIFIED` — plausible, taken from a source, not yet checked
- `STALE` — known outdated, listed so you recognise it if you meet it again

Everything sourced from the two repos starts `UNVERIFIED` by default. One repo
dates to 2022 and its terminology has drifted.

## Sources

| Source | What it is | Quality |
| --- | --- | --- |
| `GCP_Professional_Architect/` | Personal Obsidian notes, 2022, Qwiklabs lab transcripts | Low. Stale, command-level, little architecture judgment |
| `gcp-pca-prep/` | Terraform implementations of case-study solutions plus service notes, AWS-comparative | High for this book. Author came from AWS, which matches the target reader exactly |

Both are gitignored. Neither is tracked by this repo.

## Files

| File | Covers | Target chapters |
| --- | --- | --- |
| `case-studies.md` | Six observed case studies, requirements, service picks | ch10, ch13-ch17 |
| `networking-identity.md` | VPC, private access variants, IAM, Workload Identity | ch02, ch03 |
| `compute-data-ops.md` | GKE, serverless, storage, data, Terraform | ch04-ch07, ch12 |
| `flags-stale-and-legal.md` | Outdated terminology and copyright exposure | all |

Read `flags-stale-and-legal.md` before using anything else here.
