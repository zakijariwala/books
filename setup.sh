#!/usr/bin/env bash
#
# Toolchain setup for "The Clouds, for People Who Don't Do Servers".
#
# Installs the two tools the manuscript workflow needs:
#   Vale    prose linter, enforces the CLAUDE.md voice rules
#   Pandoc  assembles the manuscript
#
# Idempotent and non-interactive. Safe to run on every container start.
# Run directly with:  ./setup.sh
#
# Note on install channels: this container's egress policy blocks github.com,
# where Vale publishes its release binaries. The npm registry is reachable, and
# @vvago/vale ships the same upstream binaries, so Vale comes from npm. If you
# run this somewhere with GitHub access, the official tarball works too.

set -euo pipefail

VALE_PKG="${VALE_PKG:-@vvago/vale}"
BIN_DIR="${BIN_DIR:-/usr/local/bin}"

FAILED=()

log()  { printf '  %s\n' "$*"; }
step() { printf '\n[%s]\n' "$*"; }

# Use sudo only when we are not already root and sudo exists.
SUDO=""
if [ "$(id -u)" -ne 0 ]; then
  if command -v sudo >/dev/null 2>&1; then
    SUDO="sudo"
  fi
fi

have() { command -v "$1" >/dev/null 2>&1; }

# ---------------------------------------------------------------------------
# Vale
# ---------------------------------------------------------------------------
install_vale() {
  step "Vale"

  if have vale; then
    log "already installed: $(vale --version)"
    return 0
  fi

  if ! have npm; then
    log "npm not found, cannot install Vale"
    FAILED+=("vale (no npm)")
    return 0
  fi

  log "installing $VALE_PKG from npm"
  if ! $SUDO npm install -g "$VALE_PKG" >/tmp/setup-vale.log 2>&1; then
    log "npm install failed, see /tmp/setup-vale.log"
    FAILED+=("vale (npm install)")
    return 0
  fi

  # The npm package drops the binary in the package tree but does not link it
  # onto PATH, so link it here.
  local prefix binary
  prefix="$(npm config get prefix 2>/dev/null || echo /usr/local)"
  binary="$prefix/lib/node_modules/$VALE_PKG/bin/vale"

  if [ ! -f "$binary" ]; then
    binary="$(find "$prefix/lib/node_modules" -maxdepth 4 -type f -name vale 2>/dev/null | head -1 || true)"
  fi

  if [ -z "$binary" ] || [ ! -f "$binary" ]; then
    log "installed the package but could not find the vale binary"
    FAILED+=("vale (binary not found)")
    return 0
  fi

  $SUDO chmod +x "$binary"
  $SUDO ln -sf "$binary" "$BIN_DIR/vale"
  log "linked $binary -> $BIN_DIR/vale"
}

# ---------------------------------------------------------------------------
# Pandoc
# ---------------------------------------------------------------------------
install_pandoc() {
  step "Pandoc"

  if have pandoc; then
    log "already installed: $(pandoc --version | head -1)"
    return 0
  fi

  if ! have apt-get; then
    log "apt-get not found, cannot install Pandoc"
    FAILED+=("pandoc (no apt-get)")
    return 0
  fi

  # A refresh is nice to have but not required: the cached package lists are
  # usually enough, and the refresh can fail behind a restrictive egress policy.
  log "refreshing package lists"
  $SUDO apt-get update -qq >/dev/null 2>&1 || log "apt-get update failed, continuing with cached lists"

  log "installing pandoc"
  if ! $SUDO env DEBIAN_FRONTEND=noninteractive apt-get install -y pandoc >/tmp/setup-pandoc.log 2>&1; then
    log "apt-get install failed, see /tmp/setup-pandoc.log"
    FAILED+=("pandoc (apt-get install)")
    return 0
  fi
}

# ---------------------------------------------------------------------------
# Diagram tooling, deliberately not installed yet.
#
# HANDOVER.md holds these back until three chapters are approved, so nothing
# below runs. Uncomment when the figures in docs/figures.md get drawn.
#
# install_diagram_tools() {
#   step "Diagram tooling"
#   $SUDO env DEBIAN_FRONTEND=noninteractive apt-get install -y graphviz
#   pip3 install --break-system-packages diagrams
#   $SUDO npm install -g @mermaid-js/mermaid-cli
# }
# ---------------------------------------------------------------------------

verify() {
  step "Verify"

  local ok=0

  if have vale; then
    log "vale    $(vale --version 2>&1 | head -1)"
  else
    log "vale    MISSING"
    ok=1
  fi

  if have pandoc; then
    log "pandoc  $(pandoc --version 2>&1 | head -1)"
  else
    log "pandoc  MISSING"
    ok=1
  fi

  if [ ${#FAILED[@]} -gt 0 ]; then
    printf '\nFailed steps:\n'
    printf '  %s\n' "${FAILED[@]}"
  fi

  if [ "$ok" -ne 0 ]; then
    printf '\nSetup incomplete.\n'
    return 1
  fi

  printf '\nSetup complete.\n'
  return 0
}

main() {
  install_vale
  install_pandoc
  # install_diagram_tools   # see the note above
  verify
}

main "$@"
