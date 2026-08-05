#!/usr/bin/env bash
# Lean setup: install and verify only what the editorial stage needs.
#
#   bash setup.sh
#
# Vale (prose linting) and Pandoc (later assembly) are enough to write and check
# chapters. The diagram tools — Graphviz, the Python `diagrams` library, and
# mermaid-cli — are deferred until Stage 6, when three chapters exist and figures
# are drawn. They are listed commented-out below; uncomment when you get there.
set -uo pipefail

echo "== Required now =="
check() {
    if command -v "$1" >/dev/null 2>&1; then
        printf "  ok    %-8s %s\n" "$1" "$(command -v "$1")"
    else
        printf "  MISS  %-8s %s\n" "$1" "$2"
    fi
}
check vale   "brew install vale   | https://vale.sh/docs/install"
check pandoc "brew install pandoc | apt install pandoc"

if command -v vale >/dev/null 2>&1 && [ -f .vale.ini ]; then
    vale sync && echo "  vale sync complete"
fi

echo
echo "== Deferred until Stage 6 (figures) — install when you get there =="
echo "  graphviz    brew install graphviz | apt install graphviz   (provides 'dot')"
echo "  diagrams    python -m pip install diagrams pillow"
echo "  mermaid-cli npm install -g @mermaid-js/mermaid-cli"
# check dot  "graphviz"
# check mmdc "mermaid-cli"
