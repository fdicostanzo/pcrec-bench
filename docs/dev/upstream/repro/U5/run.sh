#!/bin/bash
# U5 repro -- libpcre2's INTERPRETER is quadratic (well past linear) on
# balanced-paren recursion (`(?R)`), against a match count that is
# itself linear in subject size.
#
# Pattern: bench/syntax/patterns/rec-r-uc.rx, `\((?:[^()]|(?R))*\)` --
# balanced parenthesised expressions, recursing into itself for nested
# ones. Subject: mixed prose/structured text (gen_subject.py, a
# standalone transcription of pcrec-bench's own censustext.py line
# grammar -- prose lines as background, balanced paren expressions as
# a SPARSE hit, 1 line in ~112 ending in an UNBALANCED trailing `(`
# with no closer) at two sizes, a 16x step (64 KiB, 1 MiB). A find-all
# scan ("global" mode) is timed at BOTH sizes and the cost is reduced
# to nanoseconds per subject byte; a linear-time mechanism gives the
# same ns/byte at both sizes (ratio ~1), this pattern instead costs
# ~10x more per byte at 1 MiB than at 64 KiB.
#
# Exit 0 = PRESENT (1 MiB : 64 KiB ns/byte ratio >= 3, comfortably
# below the ~10x this repro and pcrec-bench's own original observation
# both show and comfortably above the ~1x [0.7, 1.4] band a per-byte
# cost that really is per-byte would show -- bench/syntax/NOTES.md's
# own R7 outlier rule), exit 1 = ABSENT, exit 2 = CANNOT-RUN.
# $UPSTREAM_SCRATCH holds the generated subjects. $UPSTREAM_ENGINE_BUILD,
# if set, names an alternate pcre2test binary.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRATCH="${UPSTREAM_SCRATCH:-/tmp/upstream-U5-scratch}"
mkdir -p "$SCRATCH"

PCRE2TEST="${UPSTREAM_ENGINE_BUILD:-pcre2test}"
if ! command -v "$PCRE2TEST" >/dev/null 2>&1 && [ ! -x "$PCRE2TEST" ]; then
    echo "U5 CANNOT-RUN pcre2 - -"
    exit 2
fi
VERSION="$("$PCRE2TEST" --version 2>/dev/null | awk '{print $3}')"
if [ -z "$VERSION" ]; then
    echo "U5 CANNOT-RUN pcre2 unknown -"
    exit 2
fi
if ! command -v python3 >/dev/null 2>&1; then
    echo "U5 CANNOT-RUN pcre2 $VERSION no-python3"
    exit 2
fi

PAT="$(cat "$HERE/pattern_rec.txt")"
DELIM='~'

build_and_time() {
    # build_and_time <label> <seed> <nbytes> -- generates the subject,
    # builds a pcre2test input with the subject's embedded newlines
    # escaped as literal backslash-n (pcre2test's own convention for
    # multi-line subject data -- man pcre2test, "DATA LINES": "to do
    # multi-line matches, you have to use the \n escape"), runs
    # `global` (find-all) timed via -tm 1, and sums every reported
    # "Match time" line. Prints "<total_us> <n_matches>".
    local label="$1" seed="$2" nbytes="$3"
    local subj="$SCRATCH/subj_${label}.bin"
    local input="$SCRATCH/in_${label}.pcre2test"
    local out="$SCRATCH/out_${label}.txt"
    python3 "$HERE/gen_subject.py" "$seed" "$nbytes" "$subj"
    python3 -c "
pat = open('$HERE/pattern_rec.txt', 'rb').read().rstrip(b'\n')
subj = open('$subj', 'rb').read()
assert b'\\\\' not in subj  # the grammar never emits a literal backslash
with open('$input', 'wb') as f:
    f.write(b'$DELIM' + pat + b'$DELIM' + b'global\n')
    f.write(subj.replace(b'\n', b'\\\\n') + b'\n')
"
    timeout 60 "$PCRE2TEST" -q -tm 1 "$input" > "$out" 2>&1
    grep -a "Match time" "$out" | awk '
        { split($0,a," "); total += a[3]; n += 1 }
        END { if (n == 0) { print "-1 0" } else { printf "%.4f %d\n", total, n } }'
}

read -r TOTAL_64K N_64K <<< "$(build_and_time small 20260905 65536)"
read -r TOTAL_1M N_1M <<< "$(build_and_time large 20260907 1048576)"

echo "# U5 repro: pcre2test $VERSION, rec-r-uc.rx, find-all" >&2
echo "#   64 KiB: total ${TOTAL_64K} us over ${N_64K} matches" >&2
echo "#   1 MiB:  total ${TOTAL_1M} us over ${N_1M} matches" >&2

if [ "$TOTAL_64K" = "-1" ] || [ "$TOTAL_1M" = "-1" ]; then
    echo "U5 CANNOT-RUN pcre2 $VERSION -"
    exit 2
fi

NSPB_64K=$(awk -v t="$TOTAL_64K" 'BEGIN{printf "%.4f", t*1000.0/65536}')
NSPB_1M=$(awk -v t="$TOTAL_1M" 'BEGIN{printf "%.4f", t*1000.0/1048576}')
echo "#   64 KiB: ${NSPB_64K} ns/byte" >&2
echo "#   1 MiB:  ${NSPB_1M} ns/byte" >&2

RATIO=$(awk -v a="$NSPB_1M" -v b="$NSPB_64K" 'BEGIN{ if (b<=0) b=0.001; printf "%.2f", a/b }')
echo "#   ratio (1 MiB ns/byte : 64 KiB ns/byte): ${RATIO}x" >&2

RESULT=$(awk -v r="$RATIO" 'BEGIN{print (r+0 >= 3.0) ? "PRESENT" : "ABSENT"}')
echo "U5 $RESULT pcre2 $VERSION ${RATIO}x"
[ "$RESULT" = PRESENT ] && exit 0 || exit 1
