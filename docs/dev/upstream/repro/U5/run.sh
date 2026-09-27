#!/bin/bash
# U5 repro -- a super-linear (well past linear) per-byte cost on
# `\((?:[^()]|(?R))*\)` (balanced-paren recursion) over mixed text,
# AND the ablation that classifies it (manager review 2026-09-27:
# "rule out intended/inherent behaviour before we tell a maintainer
# something is wrong").
#
# Pattern: bench/syntax/patterns/rec-r-uc.rx. Subject: mixed
# prose/structured text (gen_subject.py, a standalone transcription of
# pcrec-bench's own censustext.py line grammar) at two sizes, a 16x
# step (64 KiB, 1 MiB) -- the ORIGINAL grammar plants ~1 line in ~112
# with a DELIBERATELY UNBALANCED trailing `(word` (no closer).
#
# THE ABLATION this run.sh performs, in order:
#   1. interpreter, ORIGINAL subject (with unbalanced lines) -- this is
#      the finding as first observed: per-byte cost far higher at 1 MiB
#      than at 64 KiB.
#   2. interpreter, CONTROL subject (same seed, unbalanced lines
#      suppressed -- gen_subject.py's allow_unbalanced=0, same RNG
#      stream otherwise) -- isolates whether RECURSION ITSELF is
#      super-linear, or only the unbalanced lines are.
#   3. JIT, ORIGINAL subject, with a LARGE jitstack (65536 KiB) --
#      DEFAULT jitstack (32 KiB) makes the JIT abort partway through
#      with "error -46: JIT stack limit reached" on the unbalanced
#      lines (verified: this is a genuine resource cap firing, not a
#      hang) rather than complete the same work the interpreter does;
#      raising jitstack removes that cap so JIT can be compared on the
#      SAME completed work.
#   4. JIT, CONTROL subject -- JIT's own linear-cost baseline.
#
# CONCLUSION baked into run.sh's own PRESENT/ABSENT logic: if the
# CONTROL (balanced-only) subject's ratio is inside the [0.7, 1.4]
# "still linear" band on BOTH interpreter and JIT, while the ORIGINAL
# subject's ratio is not, the super-linear cost is caused by the
# UNBALANCED lines specifically (a naive backtracking engine, of ANY
# kind, must scan an unclosed `(` forward through the remainder of the
# subject before failing -- inherent to backtracking on this input
# shape, not a libpcre2-specific defect). See README.md for the
# classification this repro's own numbers support (NOT-A-BUG) and the
# independent Oniguruma cross-check (not run by this script -- see
# onig_probe.c).
#
# Exit 0 = PRESENT (the raw super-linear ratio reproduces on the
# ORIGINAL subject; run.sh does not itself decide NOT-A-BUG vs a real
# defect -- that determination, and the evidence for it, is in
# README.md), exit 1 = ABSENT, exit 2 = CANNOT-RUN.
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
    # build_and_time <label> <seed> <nbytes> <allow_unbalanced 0|1> <jit 0|1> <jitstack-KiB-or-empty>
    local label="$1" seed="$2" nbytes="$3" allow_unb="$4" jit="$5" jstack="$6"
    local subj="$SCRATCH/subj_${label}.bin"
    local input="$SCRATCH/in_${label}.pcre2test"
    local out="$SCRATCH/out_${label}.txt"
    python3 "$HERE/gen_subject.py" "$seed" "$nbytes" "$subj" "$allow_unb"
    python3 -c "
pat = open('$HERE/pattern_rec.txt', 'rb').read().rstrip(b'\n')
subj = open('$subj', 'rb').read()
assert b'\\\\' not in subj  # the grammar never emits a literal backslash
mods = b'global' + (b',jit' if $jit else b'')
with open('$input', 'wb') as f:
    f.write(b'$DELIM' + pat + b'$DELIM' + mods + b'\n')
    tail = subj.replace(b'\n', b'\\\\n')
    if '$jstack':
        tail += b'\\\\=jitstack=$jstack'
    f.write(tail + b'\n')
"
    timeout 90 "$PCRE2TEST" -q -tm 1 "$input" > "$out" 2>&1
    grep -a "Match time" "$out" | awk -v nb="$nbytes" '
        { split($0,a," "); total += a[3]; n += 1 }
        END { if (n == 0) { print "-1 0 -1" } else { printf "%.4f %d %.4f\n", total, n, total*1000.0/nb } }'
}

# 1: interpreter, ORIGINAL (unbalanced lines present)
read -r I_ORIG_64K_US I_ORIG_64K_N I_ORIG_64K_NSPB <<< "$(build_and_time interp_orig_64k 20260905 65536 1 0 '')"
read -r I_ORIG_1M_US I_ORIG_1M_N I_ORIG_1M_NSPB <<< "$(build_and_time interp_orig_1m 20260907 1048576 1 0 '')"
# 2: interpreter, CONTROL (unbalanced lines suppressed, same seed/stream)
read -r I_CTL_64K_US I_CTL_64K_N I_CTL_64K_NSPB <<< "$(build_and_time interp_ctl_64k 20260905 65536 0 0 '')"
read -r I_CTL_1M_US I_CTL_1M_N I_CTL_1M_NSPB <<< "$(build_and_time interp_ctl_1m 20260907 1048576 0 0 '')"
# 3: JIT, ORIGINAL, large jitstack (65536 KiB = 64 MiB)
read -r J_ORIG_64K_US J_ORIG_64K_N J_ORIG_64K_NSPB <<< "$(build_and_time jit_orig_64k 20260905 65536 1 1 65536)"
read -r J_ORIG_1M_US J_ORIG_1M_N J_ORIG_1M_NSPB <<< "$(build_and_time jit_orig_1m 20260907 1048576 1 1 65536)"
# 4: JIT, CONTROL, default jitstack (irrelevant when balanced, but stated)
read -r J_CTL_64K_US J_CTL_64K_N J_CTL_64K_NSPB <<< "$(build_and_time jit_ctl_64k 20260905 65536 0 1 '')"
read -r J_CTL_1M_US J_CTL_1M_N J_CTL_1M_NSPB <<< "$(build_and_time jit_ctl_1m 20260907 1048576 0 1 '')"

echo "# U5 repro: pcre2test $VERSION, rec-r-uc.rx, find-all, 64 KiB vs 1 MiB (16x)" >&2
echo "#   interp ORIGINAL (unbalanced lines present): ${I_ORIG_64K_NSPB} -> ${I_ORIG_1M_NSPB} ns/byte (n=${I_ORIG_64K_N},${I_ORIG_1M_N})" >&2
echo "#   interp CONTROL  (balanced only):            ${I_CTL_64K_NSPB} -> ${I_CTL_1M_NSPB} ns/byte (n=${I_CTL_64K_N},${I_CTL_1M_N})" >&2
echo "#   jit    ORIGINAL (jitstack=65536 KiB):        ${J_ORIG_64K_NSPB} -> ${J_ORIG_1M_NSPB} ns/byte (n=${J_ORIG_64K_N},${J_ORIG_1M_N})" >&2
echo "#   jit    CONTROL  (balanced only):             ${J_CTL_64K_NSPB} -> ${J_CTL_1M_NSPB} ns/byte (n=${J_CTL_64K_N},${J_CTL_1M_N})" >&2

for v in "$I_ORIG_64K_NSPB" "$I_ORIG_1M_NSPB" "$I_CTL_64K_NSPB" "$I_CTL_1M_NSPB" \
         "$J_ORIG_64K_NSPB" "$J_ORIG_1M_NSPB" "$J_CTL_64K_NSPB" "$J_CTL_1M_NSPB"; do
    if [ "$v" = "-1" ]; then
        echo "U5 CANNOT-RUN pcre2 $VERSION -"
        exit 2
    fi
done

RATIO_I_ORIG=$(awk -v a="$I_ORIG_1M_NSPB" -v b="$I_ORIG_64K_NSPB" 'BEGIN{ if (b<=0) b=0.001; printf "%.2f", a/b }')
RATIO_I_CTL=$(awk -v a="$I_CTL_1M_NSPB" -v b="$I_CTL_64K_NSPB" 'BEGIN{ if (b<=0) b=0.001; printf "%.2f", a/b }')
RATIO_J_ORIG=$(awk -v a="$J_ORIG_1M_NSPB" -v b="$J_ORIG_64K_NSPB" 'BEGIN{ if (b<=0) b=0.001; printf "%.2f", a/b }')
RATIO_J_CTL=$(awk -v a="$J_CTL_1M_NSPB" -v b="$J_CTL_64K_NSPB" 'BEGIN{ if (b<=0) b=0.001; printf "%.2f", a/b }')
echo "#   ratio 1MiB:64KiB  interp-orig=${RATIO_I_ORIG}x  interp-ctl=${RATIO_I_CTL}x  jit-orig=${RATIO_J_ORIG}x  jit-ctl=${RATIO_J_CTL}x" >&2

CTL_LINEAR=$(awk -v ic="$RATIO_I_CTL" -v jc="$RATIO_J_CTL" 'BEGIN{ print (ic+0>=0.7 && ic+0<=1.4 && jc+0>=0.7 && jc+0<=1.4) ? 1 : 0 }')
BOTH_ORIG_SUPERLINEAR=$(awk -v io="$RATIO_I_ORIG" -v jo="$RATIO_J_ORIG" 'BEGIN{ print (io+0>=3.0 && jo+0>=3.0) ? 1 : 0 }')

if [ "$CTL_LINEAR" = "1" ] && [ "$BOTH_ORIG_SUPERLINEAR" = "1" ]; then
    echo "#   CLASSIFICATION: both engines flat on the balanced-only control, both super-linear on the original -- the unbalanced lines are the cause on BOTH engines (pattern-inherent backtracking cost, see README.md: NOT-A-BUG)" >&2
elif [ "$BOTH_ORIG_SUPERLINEAR" = "1" ]; then
    echo "#   CLASSIFICATION: super-linear on the original but the control did not come back flat -- inconclusive, see README.md" >&2
else
    echo "#   CLASSIFICATION: JIT (once not truncated by its own stack limit) is NOT super-linear where the interpreter is -- would point at the interpreter specifically" >&2
fi

# PRESENT reports the RAW interpreter ORIGINAL-subject ratio (the
# finding as originally observed); run.sh does not decide NOT-A-BUG.
RESULT=$(awk -v r="$RATIO_I_ORIG" 'BEGIN{print (r+0 >= 3.0) ? "PRESENT" : "ABSENT"}')
echo "U5 $RESULT pcre2 $VERSION ${RATIO_I_ORIG}x"
[ "$RESULT" = PRESENT ] && exit 0 || exit 1
