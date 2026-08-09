#!/usr/bin/env bash
#
# Render figures/*.svg to 300 DPI grayscale PNG at roughly 1350px wide, which is
# the width TASKS.md specifies for a 6x9 trim.
#
# The SVGs are the source and are tracked. The PNGs are build output and are
# ignored by .gitignore. Run this after scripts/figures.py.

set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

if ! command -v rsvg-convert >/dev/null 2>&1; then
  echo "rsvg-convert not found. Install librsvg2-bin." >&2
  exit 1
fi

WIDTH="${WIDTH:-1350}"
n=0

for svg in figures/*.svg; do
  png="${svg%.svg}.png"
  rsvg-convert --width="$WIDTH" --keep-aspect-ratio --background-color=white \
    --output="$png" "$svg"
  n=$((n + 1))
  printf '  %s\n' "$(basename "$png")"
done

echo "rendered $n figures at ${WIDTH}px wide"
