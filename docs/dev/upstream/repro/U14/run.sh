#!/bin/bash
# U14 repro -- libpcre2's auto-possessification pass wrongly
# possessifies a GREEDY ITERATOR AT THE END OF THE WHOLE PATTERN when
# the pattern contains a (?R) WHOLE-PATTERN recursive call that
# re-enters that same end-of-pattern position -- and doing so CHANGES
# THE ANSWER, not merely the backtracking the optimization is
# documented to skip.
#
# Pattern: /(?:b(?R)a|a+)/ (no capturing groups, no subroutine-called
# NAMED/NUMBERED groups -- just a top-level non-capturing group whose
# second branch is a bare a+, and a (?R) call in the first branch that
# re-enters the WHOLE PATTERN).
#
# Subject "baa": a non-recursing match (first alternative never taken)
# would just see "a+" greedily eat "aa" from offset 1. But with the
# (?R) call site live, the SOUND (full-backtracking) answer is
# (0,3) == "baa": 'b' matches at 0, (?R) re-enters the pattern at
# offset 1, where "a+" greedily grabs "aa" (offsets 1-3) -- but then
# the OUTER branch's trailing literal 'a' has nothing left to match,
# so the only way the overall match can succeed is for the recursive
# call's "a+" to give back one 'a', so the recursive call matches just
# "a" (offset 1-2) and the outer "a" then matches at offset 2,
# producing "baa" end to end. This is exactly the backtracking
# PCRE2_NO_AUTO_POSSESS disables the optimization in order to permit
# (see man pcre2api, NO_AUTO_POSSESS: "disables ... an optimization
# that ... avoid[s] backtracks ... that can never be successful" --
# implying the optimization is ONLY ever supposed to skip paths that
# were always going to fail anyway).
#
# libpcre2 10.46/10.49's DEFAULT answer disagrees: it possessifies the
# top-level a+ (reached, after skipping the enclosing non-capturing
# group's closing paren, at the pattern's own OP_END) WITHOUT checking
# whether the pattern contains any recursions -- so the (?R)-entered
# copy of a+ can no longer give back the 'a' the outer branch needs,
# the first alternative's match attempt from offset 0 fails outright,
# and PCRE2's unanchored search instead reports the SECOND start
# position's match of plain "a+": offset 1-3, "aa".
#
# Three subjects show the same shape: "baa" (1,3)/(0,3), "bbaaa"
# (2,5)/(0,5), "baaa" (1,4)/(0,4) -- default vs PCRE2_NO_AUTO_POSSESS.
# A fourth input uses a NUMBERED recursive call into a real capturing
# group, ^(b(?1)a|a+)$ on "baa": this gives (0,3) under BOTH options
# -- libpcre2 ChangeLog 10.31 item 31 (Bugzilla #2232, "Auto-
# possessification at the end of a capturing group ... caused
# incorrect behaviour when the group was called recursively ...
# Iterators at the ends of CAPTURING groups are no longer considered
# for auto-possessification if the pattern contains any recursions")
# fixed EXACTLY this shape back in 2018 -- but only for iterators at
# the end of a CAPTURING group (pcre2_auto_possess.c's OP_KET/
# OP_KETRPOS case checks cb->had_recurse only for OP_CBRA/OP_SCBRA/
# OP_CBRAPOS/OP_SCBRAPOS brackets). The OP_END case (reached when the
# iterator's "what follows" is the true end of the compiled pattern,
# which is where a non-capturing group at the top level lands, and
# where a bare (?R) call -- which recurses into the WHOLE PATTERN, not
# into any numbered/named group -- re-enters) has NO such check at
# all, identically in 10.46 and 10.49 (diffed byte-for-byte modulo
# comments/fallthrough-annotations). The capturing-group fix did not
# cover the no-group-at-all / whole-pattern-recursion case.
#
# Exit 0 = PRESENT (the default and no_auto_possess answers disagree
# on at least one of the three (?R) subjects, AND the numbered-group
# control agrees under both options -- showing the divergence is
# specific to (?R)'s whole-pattern-reentry shape, not recursion in
# general), exit 1 = ABSENT, exit 2 = CANNOT-RUN.
#
# No $UPSTREAM_SCRATCH subject generation needed -- every input here
# is a few bytes, written as pcre2test script fragments below.
# $UPSTREAM_ENGINE_BUILD, if set, names an alternate pcre2test binary
# (the latest-release check).
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRATCH="${UPSTREAM_SCRATCH:-/tmp/upstream-U14-scratch}"
mkdir -p "$SCRATCH"

PCRE2TEST="${UPSTREAM_ENGINE_BUILD:-pcre2test}"
if ! command -v "$PCRE2TEST" >/dev/null 2>&1 && [ ! -x "$PCRE2TEST" ]; then
    echo "U14 CANNOT-RUN pcre2 - -"
    exit 2
fi
VERSION="$("$PCRE2TEST" --version 2>/dev/null | awk '{print $3}')"
if [ -z "$VERSION" ]; then
    echo "U14 CANNOT-RUN pcre2 unknown -"
    exit 2
fi

run_one() {
    # run_one <pattern> <modifiers> <subject...> -- writes a pcre2test
    # script, runs it with -q (quiet: pattern/subject echo suppressed
    # would hide too much, so we keep the default verbose echo off via
    # -q and instead print our own labels), returns pcre2test's own
    # match-report lines.
    local pat="$1" mods="$2"; shift 2
    local f="$SCRATCH/case.pcre2test"
    {
        printf '/%s/%s\n' "$pat" "$mods"
        for s in "$@"; do printf '%s\n' "$s"; done
    } > "$f"
    "$PCRE2TEST" -q "$f" 2>&1
}

echo "# U14 repro: pcre2test $VERSION" >&2
echo "# --- (?:b(?R)a|a+) on baa / bbaaa / baaa, default ---" >&2
DEFAULT_OUT="$(run_one '(?:b(?R)a|a+)' '' baa bbaaa baaa)"
echo "$DEFAULT_OUT" | sed 's/^/#   /' >&2
echo "# --- (?:b(?R)a|a+) on baa / bbaaa / baaa, no_auto_possess ---" >&2
NAP_OUT="$(run_one '(?:b(?R)a|a+)' ',no_auto_possess' baa bbaaa baaa)"
echo "$NAP_OUT" | sed 's/^/#   /' >&2
echo "# --- control: ^(b(?1)a|a+)\$ on baa, default ---" >&2
CTRL_DEFAULT="$(run_one '^(b(?1)a|a+)$' '' baa)"
echo "$CTRL_DEFAULT" | sed 's/^/#   /' >&2
echo "# --- control: ^(b(?1)a|a+)\$ on baa, no_auto_possess ---" >&2
CTRL_NAP="$(run_one '^(b(?1)a|a+)$' ',no_auto_possess' baa)"
echo "$CTRL_NAP" | sed 's/^/#   /' >&2

# Extract just the " 0: ..." match lines (one per subject, in order),
# dropping the echoed pattern/subject lines pcre2test prints even
# under -q.
extract_matches() { grep -E '^ 0: ' <<<"$1"; }

DEFAULT_MATCHES="$(extract_matches "$DEFAULT_OUT")"
NAP_MATCHES="$(extract_matches "$NAP_OUT")"
CTRL_DEFAULT_MATCH="$(extract_matches "$CTRL_DEFAULT")"
CTRL_NAP_MATCH="$(extract_matches "$CTRL_NAP")"

echo "# default   : $(echo "$DEFAULT_MATCHES" | tr '\n' '|')" >&2
echo "# no_auto_possess: $(echo "$NAP_MATCHES" | tr '\n' '|')" >&2
echo "# control default: $(echo "$CTRL_DEFAULT_MATCH" | tr '\n' '|')" >&2
echo "# control no_auto_possess: $(echo "$CTRL_NAP_MATCH" | tr '\n' '|')" >&2

DIVERGES=0
if [ "$DEFAULT_MATCHES" != "$NAP_MATCHES" ]; then DIVERGES=1; fi
CONTROL_AGREES=0
if [ "$CTRL_DEFAULT_MATCH" = "$CTRL_NAP_MATCH" ]; then CONTROL_AGREES=1; fi

if [ "$DIVERGES" = 1 ] && [ "$CONTROL_AGREES" = 1 ]; then
    RESULT=PRESENT
else
    RESULT=ABSENT
fi

EVIDENCE="baa:$(echo "$DEFAULT_MATCHES" | sed -n 1p | tr -d ' ')-vs-$(echo "$NAP_MATCHES" | sed -n 1p | tr -d ' ')"
echo "U14 $RESULT pcre2 $VERSION $EVIDENCE"
[ "$RESULT" = PRESENT ] && exit 0 || exit 1
