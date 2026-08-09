#!/usr/bin/env bash
#
# SessionStart hook. Installs the book toolchain (Vale, Pandoc) so a fresh
# remote container can lint and build without anyone running setup by hand.
#
# Runs synchronously: the session waits for the install so nothing tries to
# lint a chapter before Vale exists. It takes about 20 seconds on a cold
# container and a moment after that, since setup.sh skips work already done.

set -euo pipefail

# Local machines already have their own toolchain, so only run this in the
# remote container.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"

if [ ! -x "$PROJECT_DIR/setup.sh" ]; then
  echo "session-start: $PROJECT_DIR/setup.sh missing or not executable, skipping toolchain install" >&2
  exit 0
fi

# Never fail the session start. A broken install should be reported and
# survivable, not a wall between the author and the manuscript.
if ! "$PROJECT_DIR/setup.sh"; then
  echo "session-start: setup.sh reported failures, see the output above" >&2
fi

exit 0
