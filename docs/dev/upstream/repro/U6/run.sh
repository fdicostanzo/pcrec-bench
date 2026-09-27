#!/bin/sh
# U6 run.sh -- docs/design/upstream_pipeline_v1.md §2.2 contract.
# Builds repro.c into $UPSTREAM_SCRATCH (or a mktemp fallback) and runs it.
# Exit 0 PRESENT, 1 ABSENT, 2 CANNOT-RUN. Always prints the final line
#   U6 PRESENT|ABSENT|CANNOT-RUN tre <version> <evidence-number>
set -eu

HERE="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
SCRATCH="${UPSTREAM_SCRATCH:-}"
if [ -z "$SCRATCH" ]; then
    SCRATCH="$(mktemp -d /var/tmp/u6-repro.XXXXXX)"
fi
mkdir -p "$SCRATCH"
BIN="$SCRATCH/u6_repro"

CC="${CC:-gcc}"

if ! pkg-config --exists tre 2>/dev/null && [ ! -f /usr/include/tre/tre.h ]; then
    echo "U6 CANNOT-RUN tre unknown 1: /usr/include/tre/tre.h not found (libtre-dev not installed)"
    exit 2
fi

if ! "$CC" -O2 -std=gnu11 "$HERE/repro.c" -ltre -o "$BIN" 2>"$SCRATCH/u6_build.log"; then
    echo "U6 CANNOT-RUN tre unknown 1: build failed, see $SCRATCH/u6_build.log"
    cat "$SCRATCH/u6_build.log" >&2
    exit 2
fi

# CONTROL (manager review, 2026-09-27): does glibc's own POSIX regcomp
# show the SAME parse? Informational only -- links no TRE symbol, never
# affects this script's exit code (that stays TRE's own PRESENT/ABSENT/
# CANNOT-RUN per the pipeline contract).
CONTROL_BIN="$SCRATCH/u6_control_glibc"
if "$CC" -O2 -std=gnu11 "$HERE/control_glibc.c" -o "$CONTROL_BIN" 2>"$SCRATCH/u6_control_build.log"; then
    "$CONTROL_BIN" || true
else
    echo "CONTROL: glibc build failed, see $SCRATCH/u6_control_build.log (informational only)"
fi
echo

VERSION="unknown"
if command -v pkg-config >/dev/null 2>&1 && pkg-config --exists tre 2>/dev/null; then
    VERSION="$(pkg-config --modversion tre 2>/dev/null || echo unknown)"
elif command -v dpkg-query >/dev/null 2>&1; then
    VERSION="$(dpkg-query -W -f='${Version}' libtre-dev 2>/dev/null || echo unknown)"
fi

set +e
OUT="$("$BIN")"
RC=$?
set -e
echo "$OUT"

if [ "$RC" -eq 0 ]; then
    echo "U6 PRESENT tre $VERSION 1"
    exit 0
elif [ "$RC" -eq 1 ]; then
    echo "U6 ABSENT tre $VERSION 1"
    exit 1
else
    echo "U6 CANNOT-RUN tre $VERSION 1: repro exited $RC (compile failure inside repro)"
    exit 2
fi
