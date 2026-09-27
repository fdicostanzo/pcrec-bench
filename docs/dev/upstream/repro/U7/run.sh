#!/bin/sh
# U7 run.sh -- docs/design/upstream_pipeline_v1.md §2.2 contract.
# Builds repro.c into $UPSTREAM_SCRATCH (or a mktemp fallback) and runs it.
# Exit 0 PRESENT, 1 ABSENT, 2 CANNOT-RUN. Always prints the final line
#   U7 PRESENT|ABSENT|CANNOT-RUN vectorscan <version> <evidence-number>
set -eu

HERE="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
SCRATCH="${UPSTREAM_SCRATCH:-}"
if [ -z "$SCRATCH" ]; then
    SCRATCH="$(mktemp -d /var/tmp/u7-repro.XXXXXX)"
fi
mkdir -p "$SCRATCH"
BIN="$SCRATCH/u7_repro"

CC="${CC:-gcc}"
HS_INC="${VECTORSCAN_INCLUDE_DIR:-/usr/include/hs}"

if [ ! -f "$HS_INC/hs.h" ]; then
    echo "U7 CANNOT-RUN vectorscan unknown 1: $HS_INC/hs.h not found (libvectorscan-dev not installed; set VECTORSCAN_INCLUDE_DIR)"
    exit 2
fi

if ! "$CC" -O2 -std=gnu11 -I"$HS_INC" "$HERE/repro.c" -lhs -o "$BIN" 2>"$SCRATCH/u7_build.log"; then
    echo "U7 CANNOT-RUN vectorscan unknown 1: build failed, see $SCRATCH/u7_build.log"
    cat "$SCRATCH/u7_build.log" >&2
    exit 2
fi

VERSION="unknown"
if command -v dpkg-query >/dev/null 2>&1; then
    VERSION="$(dpkg-query -W -f='${Version}' libvectorscan-dev 2>/dev/null || echo unknown)"
fi
if command -v pkg-config >/dev/null 2>&1 && pkg-config --exists libhs 2>/dev/null; then
    VERSION="$(pkg-config --modversion libhs 2>/dev/null || echo "$VERSION")"
fi

set +e
OUT="$("$BIN")"
RC=$?
set -e
echo "$OUT"

if [ "$RC" -eq 0 ]; then
    echo "U7 PRESENT vectorscan $VERSION 1"
    exit 0
elif [ "$RC" -eq 1 ]; then
    echo "U7 ABSENT vectorscan $VERSION 1"
    exit 1
else
    echo "U7 CANNOT-RUN vectorscan $VERSION 1: repro exited $RC (see output above)"
    exit 2
fi
