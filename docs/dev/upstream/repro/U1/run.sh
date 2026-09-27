#!/bin/bash
# U1 repro -- libpcre2 JIT catastrophic-backtracking cliff on the
# subroutine-factored RFC 5322 email pattern, over a long run of a
# single non-matching byte ('a', no '@' anywhere in the subject).
#
# Mechanism (confirmed by ablation, see README.md): pcre2_compile()'s
# static analysis determines "Last code unit = '@'" for this pattern
# (checkable with `pcre2test ... info`) REGARDLESS of JIT -- the
# interpreter (pcre2_match without JIT) uses that fact to dismiss a
# subject with no '@' in a single linear scan; the JIT-compiled
# matcher does NOT get the same benefit once the pattern's
# `@(?&label)`-style bodies are reached through SUBROUTINE CALLS
# ((?&atom) etc., pcrec-bench's bench/email/patterns/factored.rx), and
# instead performs real per-start-position backtracking, whose cost
# grows very steeply with this subject's length near a sharp cliff
# around 500,000 bytes. The HAND-INLINED control pattern (no
# subroutines, bench/email/patterns/orig.rx) does NOT show this: JIT
# is instant on the identical subject.
#
# STACK-LIMIT ABLATION (manager review 2026-09-27, item 2 -- "check
# whether this is a resource threshold, not a smooth cost; check the
# JIT stack; report what flips"): this script also runs the JIT case
# at a SMALLER, fixed subject size (N=501,000 B, already inside the
# catastrophic band, ~4s by default) at TWO very different `jitstack`
# sizes (1 KiB and 65536 KiB). If the cliff were a JIT-stack
# exhaustion (as it genuinely IS for a different finding, U5's
# recursion case -- PCRE2_ERROR_JIT_STACKLIMIT, error -46), a tiny
# stack would either error quickly or behave very differently from a
# huge one. Measured on this box: both sizes return the SAME clean
# "No match" (rc 0, no error code of any kind) in statistically the
# same ~4 seconds -- ruling out a JIT-stack cause. This is NOT a
# resource-limit artifact; see README.md for the fuller discussion of
# what was and was not established about the underlying mechanism.
#
# Exit 0 = PRESENT (the JIT run does not finish quickly / times out),
# exit 1 = ABSENT, exit 2 = CANNOT-RUN. $UPSTREAM_SCRATCH holds the
# generated subject (never committed). $UPSTREAM_ENGINE_BUILD, if set,
# names an alternate pcre2test binary (the latest-release check).
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRATCH="${UPSTREAM_SCRATCH:-/tmp/upstream-U1-scratch}"
mkdir -p "$SCRATCH"

PCRE2TEST="${UPSTREAM_ENGINE_BUILD:-pcre2test}"
if ! command -v "$PCRE2TEST" >/dev/null 2>&1 && [ ! -x "$PCRE2TEST" ]; then
    echo "U1 CANNOT-RUN pcre2 - -"
    exit 2
fi
VERSION="$("$PCRE2TEST" --version 2>/dev/null | awk '{print $3}')"
if [ -z "$VERSION" ]; then
    echo "U1 CANNOT-RUN pcre2 unknown -"
    exit 2
fi

# The subject size: 524288 B (512 KiB) of the byte 'a'. This is inside
# the catastrophic band (confirmed on this box between ~502,000 B, ~4s,
# and >=520,000 B, >15s) -- well short of the original observation's
# full 1,048,576-byte subject (which hangs 60s+; not used here to keep
# a maintainer's re-run under a minute).
N=524288
SUBJECT="$SCRATCH/subject_a.bin"
if [ ! -f "$SUBJECT" ] || [ "$(wc -c < "$SUBJECT")" != "$N" ]; then
    python3 -c "
import sys
with open('$SUBJECT', 'wb') as f:
    f.write(b'a' * $N)
"
fi

PAT_FACTORED="$(cat "$HERE/pattern_factored.txt")"
PAT_ORIG="$(cat "$HERE/pattern_orig.txt")"
# Neither pattern contains ',' or ';' -- verified when this repro was
# authored (both use '/' inside a character class, ruling out the
# usual '/' delimiter).
DELIM=','

mk_input() {
    # mk_input <outfile> <pattern> <modifiers>
    { printf '%s%s%s,%s\n' "$DELIM" "$2" "$DELIM" "$3"; cat "$SUBJECT"; echo; } > "$1"
}

JIT_FACTORED="$SCRATCH/jit_factored.pcre2test"
INTERP_FACTORED="$SCRATCH/interp_factored.pcre2test"
JIT_ORIG="$SCRATCH/jit_orig.pcre2test"
mk_input "$JIT_FACTORED" "$PAT_FACTORED" "jit"
mk_input "$INTERP_FACTORED" "$PAT_FACTORED" ""
mk_input "$JIT_ORIG" "$PAT_ORIG" "jit"

timed_run() {
    # timed_run <input> <budget_s> -- prints elapsed seconds (or
    # "TIMEOUT" on the budget firing) to stdout.
    local input="$1" budget="$2" t0 t1 rc
    t0=$(date +%s.%N)
    timeout "$budget" "$PCRE2TEST" -q "$input" >/dev/null 2>&1
    rc=$?
    t1=$(date +%s.%N)
    if [ "$rc" -eq 124 ]; then
        echo "TIMEOUT"
    else
        python3 -c "print(f'{$t1 - $t0:.3f}')"
    fi
}

echo "# U1 repro: pcre2test $VERSION, subject ${N} B of 'a' (no '@')" >&2
echo "# control (orig.rx, no subroutines), jit:" >&2
CTRL_ORIG_JIT=$(timed_run "$JIT_ORIG" 20)
echo "#   elapsed: ${CTRL_ORIG_JIT}s" >&2
echo "# factored.rx, interpreter (no jit):" >&2
FACTORED_INTERP=$(timed_run "$INTERP_FACTORED" 20)
echo "#   elapsed: ${FACTORED_INTERP}s" >&2
echo "# factored.rx, jit (the finding):" >&2
FACTORED_JIT=$(timed_run "$JIT_FACTORED" 45)
if [ "$FACTORED_JIT" = "TIMEOUT" ]; then
    echo "#   elapsed: >45s (timed out)" >&2
else
    echo "#   elapsed: ${FACTORED_JIT}s" >&2
fi

# --- STACK-LIMIT ABLATION (manager review item 2) ---
# Fixed N=501,000 B (inside the cliff, ~4s by default), jitstack=1 KiB
# vs jitstack=65536 KiB. If the outcome or the timing differed sharply
# between the two, that would point at a JIT-stack cause; a check_rc
# of anything but "clean, no error" would also be reported here.
N_STACK=501000
SUBJECT_STACK="$SCRATCH/subject_a_stack.bin"
if [ ! -f "$SUBJECT_STACK" ] || [ "$(wc -c < "$SUBJECT_STACK")" != "$N_STACK" ]; then
    python3 -c "
with open('$SUBJECT_STACK', 'wb') as f:
    f.write(b'a' * $N_STACK)
"
fi
mk_stack_input() {
    # mk_stack_input <outfile> <jitstack-KiB>
    { printf '%s%s%s,jit\n' "$DELIM" "$PAT_FACTORED" "$DELIM"; cat "$SUBJECT_STACK"; printf '\\=jitstack=%s\n' "$2"; } > "$1"
}
echo "# stack-limit ablation: factored.rx, jit, fixed N=${N_STACK} B, two jitstack sizes:" >&2
for STACK in 1 65536; do
    STACK_INPUT="$SCRATCH/jit_stack_${STACK}.pcre2test"
    mk_stack_input "$STACK_INPUT" "$STACK"
    T0=$(date +%s.%N)
    timeout 30 "$PCRE2TEST" -q "$STACK_INPUT" > "$SCRATCH/stack_${STACK}.out" 2>&1
    RC=$?
    T1=$(date +%s.%N)
    ELAPSED=$(python3 -c "print(f'{$T1 - $T0:.3f}')")
    OUTCOME="no-match"
    if [ "$RC" -eq 124 ]; then OUTCOME="timeout"; fi
    if grep -qa "^Failed:" "$SCRATCH/stack_${STACK}.out"; then
        OUTCOME="$(grep -a '^Failed:' "$SCRATCH/stack_${STACK}.out" | head -1)"
    fi
    echo "#   jitstack=${STACK} KiB: elapsed ${ELAPSED}s, rc=${RC}, outcome: ${OUTCOME}" >&2
done

# PRESENT iff the factored+jit run either timed out or took long enough
# to be unmistakably catastrophic (>2s), where the two controls above
# are expected to finish in well under 0.1s regardless.
if [ "$FACTORED_JIT" = "TIMEOUT" ]; then
    EVIDENCE="timeout45s"
    RESULT=PRESENT
else
    EVIDENCE="${FACTORED_JIT}s"
    AWK_SLOW=$(awk -v v="$FACTORED_JIT" 'BEGIN{print (v+0 > 2.0) ? 1 : 0}')
    if [ "$AWK_SLOW" = "1" ]; then
        RESULT=PRESENT
    else
        RESULT=ABSENT
    fi
fi

echo "U1 $RESULT pcre2 $VERSION $EVIDENCE"
[ "$RESULT" = PRESENT ] && exit 0 || exit 1
