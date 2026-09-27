#!/bin/bash
# U2 repro -- libpcre2 JIT does NOT get the interpreter's whole-subject
# required-code-unit dismissal on a 1 MB failing subject.
#
# Pattern: bench/email/patterns/orig.rx (the hand-inlined RFC 5322
# address-spec regex, no subroutine calls -- see U1's repro for the
# subroutine-calling sibling, whose gap is catastrophic rather than a
# fixed multiplier). Subject: 1,048,576 bytes of 'a' -- the pattern's
# required code unit is '@' (`pcre2test ...,info` reports
# "Last code unit = '@'"), which never occurs, so both routes give a
# clean nomatch; the finding is PURELY about how much CHEAPER that
# nomatch is on the interpreter than on the JIT.
#
# Exit 0 = PRESENT (jit:interp ratio >= 20, comfortably below the
# ~150x originally observed and the ~35x this box reproduces, and
# comfortably above the ~1x a fixed engine would show), exit 1 =
# ABSENT, exit 2 = CANNOT-RUN. $UPSTREAM_SCRATCH holds the generated
# subject. $UPSTREAM_ENGINE_BUILD, if set, names an alternate
# pcre2test binary (the latest-release check).
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRATCH="${UPSTREAM_SCRATCH:-/tmp/upstream-U2-scratch}"
mkdir -p "$SCRATCH"

PCRE2TEST="${UPSTREAM_ENGINE_BUILD:-pcre2test}"
if ! command -v "$PCRE2TEST" >/dev/null 2>&1 && [ ! -x "$PCRE2TEST" ]; then
    echo "U2 CANNOT-RUN pcre2 - -"
    exit 2
fi
VERSION="$("$PCRE2TEST" --version 2>/dev/null | awk '{print $3}')"
if [ -z "$VERSION" ]; then
    echo "U2 CANNOT-RUN pcre2 unknown -"
    exit 2
fi

N=1048576
SUBJECT="$SCRATCH/subject_a.bin"
if [ ! -f "$SUBJECT" ] || [ "$(wc -c < "$SUBJECT")" != "$N" ]; then
    python3 -c "
with open('$SUBJECT', 'wb') as f:
    f.write(b'a' * $N)
"
fi

PAT_ORIG="$(cat "$HERE/pattern_orig.txt")"
DELIM=','
REPS=50

JIT_INPUT="$SCRATCH/jit.pcre2test"
INTERP_INPUT="$SCRATCH/interp.pcre2test"
{ printf '%s%s%s,jit\n' "$DELIM" "$PAT_ORIG" "$DELIM"; cat "$SUBJECT"; echo; } > "$JIT_INPUT"
{ printf '%s%s%s\n' "$DELIM" "$PAT_ORIG" "$DELIM"; cat "$SUBJECT"; echo; } > "$INTERP_INPUT"

median_match_time_us() {
    # median_match_time_us <input> -- runs -tm REPS, prints the median
    # of the reported "Match time" values in microseconds.
    local input="$1" out
    out=$(timeout 30 "$PCRE2TEST" -q -tm "$REPS" "$input" 2>&1 | grep -a "Match time")
    if [ -z "$out" ]; then
        echo "-1"
        return
    fi
    printf '%s\n' "$out" | awk '{print $3}' | sort -n | awk '
        { a[NR]=$1 } END { if (NR%2==1) print a[(NR+1)/2]; else print (a[NR/2]+a[NR/2+1])/2 }'
}

JIT_US=$(median_match_time_us "$JIT_INPUT")
INTERP_US=$(median_match_time_us "$INTERP_INPUT")

echo "# U2 repro: pcre2test $VERSION, orig.rx over ${N} B of 'a' (no '@'), $REPS reps" >&2
echo "#   jit median match time:    ${JIT_US} us" >&2
echo "#   interp median match time: ${INTERP_US} us" >&2

if [ "$JIT_US" = "-1" ] || [ "$INTERP_US" = "-1" ]; then
    echo "U2 CANNOT-RUN pcre2 $VERSION -"
    exit 2
fi

RATIO=$(awk -v j="$JIT_US" -v i="$INTERP_US" 'BEGIN{ if (i<=0) i=0.001; printf "%.2f", j/i }')
echo "#   ratio (jit/interp): ${RATIO}x" >&2

RESULT=$(awk -v r="$RATIO" 'BEGIN{print (r+0 >= 20) ? "PRESENT" : "ABSENT"}')
echo "U2 $RESULT pcre2 $VERSION ${RATIO}x"
[ "$RESULT" = PRESENT ] && exit 0 || exit 1
