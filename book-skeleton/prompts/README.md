# prompts/

Staged prompt text for the drafting workflow. Each stage produces an artifact the
next stage depends on. Run them in order; do not skip ahead.

| Stage | File | When | Produces |
|-------|------|------|----------|
| 2 | `stage2-kill-test.md` | After the thesis and `docs/buyer.md` exist | `docs/toc-review.md`, then a frozen `docs/toc.md` |
| 3 | `stage3-standards.md` | After the TOC freezes and `voice/sample.md` exists | chapter template, terminology, registries, voice lint rules |
| 6 | `stage6-figures.md` | After three chapters are approved | rendered figures |

Stages 1, 4, and 5 are author-driven and live in `TASKS.md`: write the thesis and
buyer (1), pilot articles and test demand (4), draft/review/verify/approve the
chapters (5). The agent skills (`/article`, `/draft`, `/review`, `/verify`,
`/approve`) carry stages 4 and 5.
