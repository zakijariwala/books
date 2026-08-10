#!/usr/bin/env bash
#
# Build the single-file reading copy for the shred.
#
#   build/draft.md    one markdown file, figures placed, markers surfaced
#   build/draft.html  self-contained, images embedded, opens anywhere
#
# build/ is ignored by .gitignore: this is output, the manuscript is the source.

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

command -v pandoc >/dev/null 2>&1 || { echo "pandoc not found. Run ./setup.sh" >&2; exit 1; }

python3 scripts/build-draft.py

pandoc build/draft.md \
  --from=markdown+raw_html \
  --to=html5 \
  --standalone \
  --embed-resources \
  --css=scripts/draft.css \
  --metadata title="The Clouds, for People Who Don't Do Servers" \
  --output=build/draft.html \
  --resource-path=.:build:figures

printf 'build/draft.html  %s\n' "$(du -h build/draft.html | cut -f1)"
