#!/bin/sh
# testees/pcrec/pin.sh -- materialise and build ONE pinned pcrec commit.
#
#   pin.sh <commit>                    -> prints the path of the built binary
#   pin.sh --path <commit>             -> prints the path without building
#   pin.sh --build-root DIR <commit>   -> build somewhere else (a throwaway
#                                         root, for exercising this script)
#
# THE TWO RULES THIS SCRIPT EXISTS TO ENFORCE:
#
# 1. IT NEVER WRITES INSIDE pcrec. The source tree at $PCREC_SRC is READ-ONLY
#    to this project. `git archive <commit>` extracts a detached snapshot into
#    the build root; `make` runs THERE. pcrec's own working tree, its build/
#    and its worktrees/ are never touched, so a pcrec session running its test
#    batteries in that tree cannot be disturbed by a bench run, and a bench
#    number can never come from a dirty tree.
#
# 2. IT REUSES AN EXISTING BUILD. Two sessions may want the same pin; the
#    first one to arrive builds it, the rest use it. A build is "present" iff
#    the binary exists, which is the only test that cannot be satisfied by a
#    half-finished extraction.
#
# BUILD ROOT: $PCRECBENCH_BUILD_ROOT, defaulting to the repo's MAIN tree's
# `build/` -- NOT a worktree's. A pin is a heavy, shared artifact; one copy
# per box, not one per worktree. Resolved from git's COMMON dir so a worktree
# resolves to the same place its main tree does.
#
# LC_ALL=C throughout (requirements 9(f)); gnutimeout on the build.

set -eu
export LC_ALL=C LANG=C

PCREC_SRC="${PCREC_SRC:-/home/duxevents/pcrec}"
JOBS="${PCRECBENCH_PIN_JOBS:-4}"
BUILD_TIMEOUT="${PCRECBENCH_PIN_TIMEOUT:-900}"

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

default_build_root() {
    # `git rev-parse --git-common-dir` in a worktree points at the MAIN
    # tree's .git, so this resolves to the main tree's build/ from anywhere.
    common=$(git -C "$here" rev-parse --git-common-dir 2>/dev/null || echo "")
    if [ -n "$common" ]; then
        case "$common" in
            /*) ;;
            *) common=$(CDPATH= cd -- "$here" && CDPATH= cd -- "$common" && pwd) ;;
        esac
        printf '%s\n' "$(dirname -- "$common")/build"
    else
        printf '%s\n' "$(dirname -- "$(dirname -- "$here")")/build"
    fi
}

BUILD_ROOT="${PCRECBENCH_BUILD_ROOT:-$(default_build_root)}"

path_only=0
while [ $# -gt 0 ]; do
    case "${1:-}" in
        --path)       path_only=1; shift ;;
        --build-root) BUILD_ROOT="${2:?--build-root needs a directory}"; shift 2 ;;
        --)           shift; break ;;
        -*)           echo "pin.sh: unknown option $1" >&2; exit 2 ;;
        *)            break ;;
    esac
done
commit="${1:-}"
[ -n "$commit" ] || { echo "usage: pin.sh [--path] <commit>" >&2; exit 2; }

dest="$BUILD_ROOT/pcrec-$commit"
binary="$dest/build/pcrec"

if [ "$path_only" = 1 ]; then printf '%s\n' "$binary"; exit 0; fi

if [ -x "$binary" ]; then
    printf '%s\n' "$binary"
    exit 0
fi

[ -d "$PCREC_SRC/.git" ] || {
    echo "pin.sh: $PCREC_SRC is not a git repository" >&2; exit 2; }
git -C "$PCREC_SRC" cat-file -e "$commit^{commit}" 2>/dev/null || {
    echo "pin.sh: $PCREC_SRC has no commit $commit" >&2; exit 2; }

full=$(git -C "$PCREC_SRC" rev-parse "$commit^{commit}")
describe=$(git -C "$PCREC_SRC" describe --always --dirty=+dirty "$full" 2>/dev/null || echo "$commit")

echo "pin.sh: archiving pcrec $commit ($describe) -> $dest" >&2
rm -rf "$dest.partial"
mkdir -p "$dest.partial"
git -C "$PCREC_SRC" archive --format=tar "$full" | tar -x -C "$dest.partial"

# Provenance beside the tree: the pin is a detached snapshot with no .git, so
# without this file nothing in it says which commit it is.
{
    printf 'commit\t%s\n' "$full"
    printf 'short\t%s\n' "$commit"
    printf 'describe\t%s\n' "$describe"
    printf 'archived_from\t%s\n' "$PCREC_SRC"
    printf 'archived_at\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
} > "$dest.partial/PIN.tsv"

echo "pin.sh: building (make -j$JOBS, gnutimeout $BUILD_TIMEOUT)" >&2
( cd "$dest.partial" && gnutimeout "$BUILD_TIMEOUT" make -j"$JOBS" ) >"$dest.partial/build.log" 2>&1 || {
    echo "pin.sh: BUILD FAILED; log tail:" >&2
    tail -30 "$dest.partial/build.log" >&2
    exit 1
}
[ -x "$dest.partial/build/pcrec" ] || {
    echo "pin.sh: make succeeded but build/pcrec is absent" >&2; exit 1; }

rm -rf "$dest"
mv "$dest.partial" "$dest"
printf '%s\n' "$binary"
