#!/usr/bin/env bash
# One-shot environment check + Python setup for the book toolchain.
#
#   bash scripts/bootstrap.sh
#
# It does two things it can do safely and portably:
#   1. Creates a Python venv and installs requirements-dev.txt into it.
#   2. Reports which external tools are present and how to get the missing ones.
#
# It deliberately does NOT install the external binaries (Pandoc, Vale,
# Graphviz, Node/mermaid-cli): those come from your OS package manager and the
# right command differs per platform. The report below tells you what to run.
set -uo pipefail

echo "== Python venv =="
if [ ! -d venv ]; then
    python3 -m venv venv && echo "created venv/"
fi
# venv layout differs: bin on Unix, Scripts on Windows.
if [ -x venv/bin/python ]; then PY=venv/bin/python; else PY=venv/Scripts/python.exe; fi
"$PY" -m pip install --quiet --upgrade pip
"$PY" -m pip install --quiet -r requirements-dev.txt
echo "installed requirements-dev.txt"
echo

echo "== External tools =="
check() {
    if command -v "$1" >/dev/null 2>&1; then
        printf "  ok    %-10s %s\n" "$1" "$(command -v "$1")"
    else
        printf "  MISS  %-10s %s\n" "$1" "$2"
    fi
}
check pandoc "brew install pandoc | apt install pandoc | winget install JohnMacFarlane.Pandoc"
check vale   "brew install vale   | https://vale.sh/docs/install"
check dot    "brew install graphviz | apt install graphviz   (Graphviz: provides 'dot')"
check mmdc   "npm install -g @mermaid-js/mermaid-cli"
check magick "brew install imagemagick   (only needed for 'make grayscale' proofs)"
echo

echo "== Vale styles =="
if command -v vale >/dev/null 2>&1; then
    vale sync && echo "vale sync complete"
else
    echo "  skipped: install Vale first, then run 'vale sync' to fetch style packages"
fi
echo

echo "== Git hooks =="
echo "  run 'make hooks' to install the pre-commit gate (Vale + fast tests)"
echo
echo "Bootstrap done. Try: make diagrams && make test"
