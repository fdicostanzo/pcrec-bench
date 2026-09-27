#!/bin/bash
# U4 repro -- libpcre2 JIT is SLOWER than its own interpreter on a
# pattern that begins with a literal delimiter byte followed by an
# alternation, over ordinary failing log text.
#
# Pattern: bench/loglines/patterns/http-5xx.rx, an HTTP-access-line
# match (`"(?:GET|POST|...) ... HTTP/1\.[01]" 5[0-9]{2}\b`). Its
# compiled first code unit is the literal `"` (`pcre2test ...,info`
# reports "First code unit = '\"'"). Subject: 1 MB of ordinary prose
# with NO `"` byte anywhere -- the interpreter can dismiss the whole
# subject with a `memchr`-class scan for `"`; per this finding the
# JIT scans the whole subject regardless, at a much higher per-byte
# cost. (The ORIGINAL observation, pcrec-bench's own bench/loglines
# set, 2026-08-28, ALSO reports a ~1.8x ratio at SHORT-subject-search
# grain (112 subjects, 256-512 B band) -- that per-call cost is a few
# tens of nanoseconds and this repro found it too noisy at
# `pcre2test -tm`'s granularity to give a stable ratio run to run
# (observed 1.0x-2.5x across repeated runs on this box); the 1 MB
# throughput measurement below is the robust, reproducible expression
# of the SAME mechanism cited in the same finding.)
#
# Exit 0 = PRESENT (jit:interp ratio >= 10, comfortably below the
# ~30-45x this repro and the original observation both show and
# comfortably above 1.0), exit 1 = ABSENT, exit 2 = CANNOT-RUN.
# $UPSTREAM_SCRATCH holds the generated subject. $UPSTREAM_ENGINE_BUILD,
# if set, names an alternate pcre2test binary.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRATCH="${UPSTREAM_SCRATCH:-/tmp/upstream-U4-scratch}"
mkdir -p "$SCRATCH"

PCRE2TEST="${UPSTREAM_ENGINE_BUILD:-pcre2test}"
if ! command -v "$PCRE2TEST" >/dev/null 2>&1 && [ ! -x "$PCRE2TEST" ]; then
    echo "U4 CANNOT-RUN pcre2 - -"
    exit 2
fi
VERSION="$("$PCRE2TEST" --version 2>/dev/null | awk '{print $3}')"
if [ -z "$VERSION" ]; then
    echo "U4 CANNOT-RUN pcre2 unknown -"
    exit 2
fi

PAT="$(cat "$HERE/pattern_http5xx.txt")"
N=1048576
SUBJECT="$SCRATCH/subject_noquote.bin"
if [ ! -f "$SUBJECT" ] || [ "$(wc -c < "$SUBJECT")" != "$N" ]; then
    python3 -c "
unit = b'the quick brown fox jumps over lazy dog '
body = (unit * ($N // len(unit) + 1))[:$N]
assert b'\"' not in body
with open('$SUBJECT', 'wb') as f:
    f.write(body)
"
fi

DELIM='~'
REPS=20

JIT_INPUT="$SCRATCH/jit.pcre2test"
INTERP_INPUT="$SCRATCH/interp.pcre2test"
{ printf '%s%s%sjit\n' "$DELIM" "$PAT" "$DELIM"; cat "$SUBJECT"; echo; } > "$JIT_INPUT"
{ printf '%s%s%s\n' "$DELIM" "$PAT" "$DELIM"; cat "$SUBJECT"; echo; } > "$INTERP_INPUT"

median_match_time_us() {
    local input="$1" out taskset_prefix=""
    command -v taskset >/dev/null 2>&1 && taskset_prefix="taskset -c 0"
    out=$(timeout 30 $taskset_prefix "$PCRE2TEST" -q -tm "$REPS" "$input" 2>&1 | grep -a "Match time")
    if [ -z "$out" ]; then
        echo "-1"
        return
    fi
    printf '%s\n' "$out" | awk '{print $3}' | sort -n | awk '
        { a[NR]=$1 } END { if (NR%2==1) print a[(NR+1)/2]; else print (a[NR/2]+a[NR/2+1])/2 }'
}

JIT_US=$(median_match_time_us "$JIT_INPUT")
INTERP_US=$(median_match_time_us "$INTERP_INPUT")

echo "# U4 repro: pcre2test $VERSION, http-5xx.rx over ${N} B of quote-free prose, $REPS reps" >&2
echo "#   jit median match time:    ${JIT_US} us" >&2
echo "#   interp median match time: ${INTERP_US} us" >&2

if [ "$JIT_US" = "-1" ] || [ "$INTERP_US" = "-1" ]; then
    echo "U4 CANNOT-RUN pcre2 $VERSION -"
    exit 2
fi

RATIO=$(awk -v j="$JIT_US" -v i="$INTERP_US" 'BEGIN{ if (i<=0) i=0.001; printf "%.2f", j/i }')
echo "#   ratio (jit/interp): ${RATIO}x" >&2

RESULT=$(awk -v r="$RATIO" 'BEGIN{print (r+0 >= 10) ? "PRESENT" : "ABSENT"}')
echo "U4 $RESULT pcre2 $VERSION ${RATIO}x"
[ "$RESULT" = PRESENT ] && exit 0 || exit 1
