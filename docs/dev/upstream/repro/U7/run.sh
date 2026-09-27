#!/bin/sh
# U7 run.sh -- docs/design/upstream_pipeline_v1.md §2.2 contract.
# Builds repro.c into $UPSTREAM_SCRATCH (or a mktemp fallback) and runs it.
# Exit 0 PRESENT, 1 ABSENT, 2 CANNOT-RUN. Always prints the final line
#   U7 PRESENT|ABSENT|CANNOT-RUN vectorscan <version> <evidence-number>
#
# $UPSTREAM_ENGINE_BUILD, if set, names an alternate vectorscan INSTALL
# PREFIX (a directory with include/hs/hs.h and lib/libhs.so*) -- the
# latest-release check (tools/upstream.py repro U7 --engine-build PATH
# --record). Default is the system package (/usr/include/hs, -lhs via
# the default library search path). $VECTORSCAN_INCLUDE_DIR overrides
# just the include dir for a system-package-only override; it is
# ignored when $UPSTREAM_ENGINE_BUILD is set.
set -eu

HERE="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
SCRATCH="${UPSTREAM_SCRATCH:-}"
if [ -z "$SCRATCH" ]; then
    SCRATCH="$(mktemp -d /var/tmp/u7-repro.XXXXXX)"
fi
mkdir -p "$SCRATCH"
BIN="$SCRATCH/u7_repro"

CC="${CC:-gcc}"

ENGINE_BUILD="${UPSTREAM_ENGINE_BUILD:-}"
LIBDIR=""
if [ -n "$ENGINE_BUILD" ]; then
    HS_INC="$ENGINE_BUILD/include/hs"
    LIBDIR="$ENGINE_BUILD/lib"
    if [ ! -f "$HS_INC/hs.h" ]; then
        echo "U7 CANNOT-RUN vectorscan unknown 1: $HS_INC/hs.h not found under \$UPSTREAM_ENGINE_BUILD ($ENGINE_BUILD)"
        exit 2
    fi
    if [ ! -f "$LIBDIR/libhs.so" ]; then
        echo "U7 CANNOT-RUN vectorscan unknown 1: $LIBDIR/libhs.so not found under \$UPSTREAM_ENGINE_BUILD ($ENGINE_BUILD)"
        exit 2
    fi
else
    HS_INC="${VECTORSCAN_INCLUDE_DIR:-/usr/include/hs}"
    if [ ! -f "$HS_INC/hs.h" ]; then
        echo "U7 CANNOT-RUN vectorscan unknown 1: $HS_INC/hs.h not found (libvectorscan-dev not installed; set VECTORSCAN_INCLUDE_DIR)"
        exit 2
    fi
fi

if [ -n "$LIBDIR" ]; then
    BUILD_CMD="$CC -O2 -std=gnu11 -I$HS_INC $HERE/repro.c -L$LIBDIR -Wl,-rpath,$LIBDIR -lhs -o $BIN"
else
    BUILD_CMD="$CC -O2 -std=gnu11 -I$HS_INC $HERE/repro.c -lhs -o $BIN"
fi
if ! $BUILD_CMD 2>"$SCRATCH/u7_build.log"; then
    echo "U7 CANNOT-RUN vectorscan unknown 1: build failed, see $SCRATCH/u7_build.log"
    cat "$SCRATCH/u7_build.log" >&2
    exit 2
fi

VERSION="unknown"
if [ -n "$ENGINE_BUILD" ]; then
    # A from-source build has no dpkg/pkg-config record of its own;
    # hs_version() (baked into the binary at build time) is the truth.
    # Build a one-line separate probe rather than overload repro.c's argv.
    VERBIN="$SCRATCH/u7_hsversion"
    VERSRC="$SCRATCH/u7_hsversion.c"
    printf '%s\n' \
        '#include <stdio.h>' \
        '#include <hs/hs.h>' \
        'int main(void){ printf("%s", hs_version()); return 0; }' \
        > "$VERSRC"
    if "$CC" -O2 -std=gnu11 -I"$HS_INC" "$VERSRC" -L"$LIBDIR" -Wl,-rpath,"$LIBDIR" -lhs -o "$VERBIN" 2>"$SCRATCH/u7_ver_build.log"; then
        VERSION="$(LD_LIBRARY_PATH="$LIBDIR${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}" "$VERBIN" 2>/dev/null | awk '{print $1}')"
    fi
    if [ -z "$VERSION" ]; then
        VERSION="source-build"
    fi
elif command -v dpkg-query >/dev/null 2>&1; then
    VERSION="$(dpkg-query -W -f='${Version}' libvectorscan-dev 2>/dev/null || echo unknown)"
fi
if [ -z "$ENGINE_BUILD" ] && command -v pkg-config >/dev/null 2>&1 && pkg-config --exists libhs 2>/dev/null; then
    VERSION="$(pkg-config --modversion libhs 2>/dev/null || echo "$VERSION")"
fi

set +e
if [ -n "$LIBDIR" ]; then
    OUT="$(LD_LIBRARY_PATH="$LIBDIR${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}" "$BIN")"
else
    OUT="$("$BIN")"
fi
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
