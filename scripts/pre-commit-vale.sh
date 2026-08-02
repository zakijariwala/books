#!/usr/bin/env bash
# Pre-commit gate: Vale on staged Markdown, then the fast test suite.
#
# Both block the commit on failure. The build tests are deliberately excluded:
# they need Pandoc and a built book, which is too slow to run per commit. Run
# those with `make test-build` before publishing.
set -uo pipefail

PY=venv/Scripts/python.exe
[ -x "$PY" ] || PY=python

# --- Vale -----------------------------------------------------------------

# --diff-filter=d keeps deletions out of the list; a deleted file cannot lint.
mapfile -t STAGED_MD < <(git diff --cached --name-only --diff-filter=d -- 'manuscript/*.md')

if [ ${#STAGED_MD[@]} -gt 0 ]; then
    if ! command -v vale >/dev/null 2>&1; then
        echo "pre-commit: vale not on PATH, cannot lint. Install it or fix PATH." >&2
        echo "pre-commit: refusing to pass silently." >&2
        exit 1
    fi

    # First pass is for the author: show everything, including warnings.
    vale --config=.vale.ini "${STAGED_MD[@]}"

    # Second pass is the gate. Vale exits non-zero when it finds an alert at or
    # above --minAlertLevel, so the exit code does the work. Do not try to
    # detect severity by grepping the output: the `line` output format carries
    # no severity word at all, which silently passed every commit.
    if ! vale --config=.vale.ini --minAlertLevel=error --output=line "${STAGED_MD[@]}" >/dev/null 2>&1; then
        echo
        echo "pre-commit: Vale found errors in staged Markdown. Commit blocked." >&2
        echo "pre-commit: fix them, or run 'git commit --no-verify' to override." >&2
        exit 1
    fi
fi

# --- Tests ----------------------------------------------------------------

# Run regardless of what is staged: a change to scripts/ or to a figure source
# can break the manuscript invariants without touching a Markdown file.
if ! "$PY" -m pytest -m "not build" -q; then
    echo
    echo "pre-commit: tests failed. Commit blocked." >&2
    echo "pre-commit: fix them, or run 'git commit --no-verify' to override." >&2
    exit 1
fi

exit 0
