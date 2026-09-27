#!/bin/sh
# U8 run.sh -- docs/design/upstream_pipeline_v1.md §2.2 contract.
# Builds repro.cc into $UPSTREAM_SCRATCH (or a mktemp fallback) and runs it.
# Exit 0 PRESENT, 1 ABSENT, 2 CANNOT-RUN. Always prints the final line
#   U8 PRESENT|ABSENT|CANNOT-RUN re2 <version> <evidence-number>
set -eu

HERE="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
SCRATCH="${UPSTREAM_SCRATCH:-}"
if [ -z "$SCRATCH" ]; then
    SCRATCH="$(mktemp -d /var/tmp/u8-repro.XXXXXX)"
fi
mkdir -p "$SCRATCH"
BIN="$SCRATCH/u8_repro"

CXX="${CXX:-g++}"

if ! command -v pkg-config >/dev/null 2>&1 || ! pkg-config --exists re2 2>/dev/null; then
    echo "U8 CANNOT-RUN re2 unknown 1: pkg-config re2 not found (libre2-dev not installed)"
    exit 2
fi

# shellcheck disable=SC2046
if ! "$CXX" -O2 -std=c++17 $(pkg-config --cflags re2) "$HERE/repro.cc" \
        $(pkg-config --libs re2) -o "$BIN" 2>"$SCRATCH/u8_build.log"; then
    echo "U8 CANNOT-RUN re2 unknown 1: build failed, see $SCRATCH/u8_build.log"
    cat "$SCRATCH/u8_build.log" >&2
    exit 2
fi

VERSION="$(pkg-config --modversion re2 2>/dev/null || echo unknown)"

set +e
OUT="$("$BIN")"
RC=$?
set -e
echo "$OUT"

if [ "$RC" -eq 0 ]; then
    echo "U8 PRESENT re2 $VERSION 1"
    exit 0
elif [ "$RC" -eq 1 ]; then
    echo "U8 ABSENT re2 $VERSION 1"
    exit 1
else
    echo "U8 CANNOT-RUN re2 $VERSION 1: repro exited $RC (compile failure inside repro)"
    exit 2
fi
