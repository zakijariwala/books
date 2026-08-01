#!/usr/bin/env bash
# Runs Vale on staged Markdown in manuscript/. Errors block commit, warnings pass.
set -euo pipefail

STAGED_MD=$(git diff --cached --name-only --diff-filter=ACM -- 'manuscript/*.md' || true)

if [ -z "$STAGED_MD" ]; then
    exit 0
fi

OUTPUT=$(vale --config=.vale.ini --output=line $STAGED_MD 2>&1) || true
echo "$OUTPUT"

if echo "$OUTPUT" | grep -qE '\berror\b'; then
    echo "Vale found errors in staged Markdown. Fix them or amend the offending lines before committing."
    exit 1
fi

exit 0
