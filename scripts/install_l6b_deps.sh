#!/bin/sh
# scripts/install_l6b_deps.sh -- the [B7]/L6b engine-adapter dependencies
# ([B42] capability_set_v1.md 11.2; Frank's install line, scripted and
# VALIDATED 2026-09-16 against this box's apt).
#
#   install_l6b_deps.sh              check only: every package name
#                                    resolved against apt, installed
#                                    state printed, conflicts detected;
#                                    exit 0 iff every needed package is
#                                    already installed, else 1. NEVER
#                                    installs anything.
#   install_l6b_deps.sh --install    the same checks, then
#                                    `sudo apt-get install` of the
#                                    missing ones (sudo prompts; run it
#                                    at a terminal).
#   install_l6b_deps.sh --with-rust  include cargo + rustc (ONLY if the
#                                    Rust `regex` testee is actually
#                                    being built -- 11.2's own caveat).
#                                    Combines with --install.
#
# PACKAGE SET (each name validated by `apt-cache policy` on this box,
# 2026-09-16 -- candidates existed for all; versions in the git log of
# this file's introducing commit):
#   libonig-dev        Oniguruma      (L6b)
#   libtre-dev         TRE            (L6b)
#   libvectorscan-dev  Vectorscan     (L6b; Frank's Q3 ruling 2026-09-16:
#                                      boolean match grain)
#   libabsl-dev        Abseil, RE2's runtime dependency (L6b)
#   libre2-dev         RE2            (L6b. NOTE: the 2026-09-12 research
#                                      note N2 claimed this was already
#                                      installed on this box; measured
#                                      2026-09-16: it is NOT -- the claim
#                                      is stale, so it is in the set)
#
# HARD RULE (11.2, Ubuntu's own Replaces/Provides/Conflicts): NEVER
# install libhyperscan-dev beside libvectorscan-dev. This script REFUSES
# to proceed if libhyperscan-dev is installed, and never installs it.
# cmake is NOT needed for anything on this roster (11.2), and RE2's
# route is a direct C++ driver, not cre2 (N2 follow-up: cre2 needs an
# autotools bootstrap this box lacks and has zero release tags).

set -eu
export LC_ALL=C LANG=C

PKGS="libonig-dev libtre-dev libvectorscan-dev libabsl-dev libre2-dev"
RUST_PKGS="cargo rustc"
FORBIDDEN="libhyperscan-dev"

do_install=0
with_rust=0
for arg in "$@"; do
    case "$arg" in
        --install)   do_install=1 ;;
        --with-rust) with_rust=1 ;;
        *) echo "usage: $0 [--install] [--with-rust]" >&2; exit 2 ;;
    esac
done
[ "$with_rust" -eq 1 ] && PKGS="$PKGS $RUST_PKGS"

# -- the forbidden-package gate, first and unconditionally ------------
if dpkg-query -W -f '${Status}\n' "$FORBIDDEN" 2>/dev/null \
        | grep -q "install ok installed"; then
    echo "REFUSED: $FORBIDDEN is installed. It Conflicts/Replaces" >&2
    echo "libvectorscan-dev (capability_set_v1.md 11.2); remove it" >&2
    echo "deliberately before running this script. Nothing was done." >&2
    exit 1
fi
echo "ok: $FORBIDDEN not installed (the Vectorscan conflict gate)"

# -- validate every name against apt, report state --------------------
missing=""
bad=""
for p in $PKGS; do
    cand=$(apt-cache policy "$p" 2>/dev/null \
           | sed -n 's/^  Candidate: //p')
    if [ -z "$cand" ] || [ "$cand" = "(none)" ]; then
        echo "BAD NAME: $p has no apt candidate on this box" >&2
        bad="$bad $p"
        continue
    fi
    if dpkg-query -W -f '${Status}\n' "$p" 2>/dev/null \
            | grep -q "install ok installed"; then
        echo "ok: $p installed ($(dpkg-query -W -f '${Version}' "$p"))"
    else
        echo "missing: $p (candidate $cand)"
        missing="$missing $p"
    fi
done
[ -n "$bad" ] && { echo "FAILED: unresolvable package name(s):$bad" >&2; exit 1; }

if [ -z "$missing" ]; then
    echo "all L6b dependencies present."
    exit 0
fi

if [ "$do_install" -eq 0 ]; then
    echo ""
    echo "check-only mode; to install the missing set:"
    echo "  sudo apt-get install$missing"
    echo "or re-run: $0 --install"
    exit 1
fi

echo ""
echo "installing:$missing"
# shellcheck disable=SC2086
sudo apt-get install $missing
