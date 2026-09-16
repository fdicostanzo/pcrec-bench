#!/usr/bin/env bash
# docs/dev/measurements/accept41_cd371441/run.sh
#
# [B42] restart step (1): THE AUTHORITATIVE RUN of rxt_needs_v1.md §3's
# 41-check acceptance checklist against pcrec's delivered pin cd371441
# (abi 23, [DD-13b.W23] full first-delivery scope, inbox I-68/I-69).
# Superseded pcrecdev1's own dry run (25/41 runnable, w235_report.md §3) --
# this is the one of record, run from pcrec-bench's own repo.
#
# Reproduces docs/dev/measurements/2026-09-16-b42-acceptance-41-cd371441.txt
# byte-for-byte except the `# bench:` provenance line (this repo's own
# commit, which legitimately moves between a re-run and the archive --
# same convention as probe_rxt_format.py).
#
#   PCREC_BIN=/path/to/pcrec bash docs/dev/measurements/accept41_cd371441/run.sh
#
# Defaults to build/pcrec-cd371441/build/pcrec under the repo root. Every
# fixture is written under a FIXED scratch directory (never /tmp root,
# BD3) and reused by C8/C9's run.sh invocation and B7's custom driver.
# NOTHING HERE IS A MEASUREMENT: every command is compile/parse-scale
# (--list-source is ~ms; the two gcc compiles for B7 are a few hundred ms
# each), so the box's load does not gate this run and none of it enters
# the store.
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
# build/ lives in the MAIN checkout; a run from a worktree (as this lane
# is) falls back to the git common directory's parent, same rule as
# probe_rxt_format.py's default_bin().
if [ -n "${PCREC_BIN:-}" ]; then
    P="$PCREC_BIN"
elif [ -x "$ROOT/build/pcrec-cd371441/build/pcrec" ]; then
    P="$ROOT/build/pcrec-cd371441/build/pcrec"
else
    COMMON="$(git -C "$ROOT" rev-parse --git-common-dir 2>/dev/null)"
    case "$COMMON" in /*) ;; *) COMMON="$ROOT/$COMMON" ;; esac
    P="$(dirname "$COMMON")/build/pcrec-cd371441/build/pcrec"
fi
SCRATCH="${TMPDIR:-/var/tmp}/b42accept41"
FIX="$(dirname "${BASH_SOURCE[0]}")/fixtures"
rm -rf "$SCRATCH"
mkdir -p "$SCRATCH"

if [ ! -x "$P" ]; then
    echo "no pcrec binary at $P (set \$PCREC_BIN)" >&2
    exit 1
fi

BENCH_COMMIT="$(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo unknown)"

echo "# [B42] restart step (1) -- the 41-check acceptance run, cd371441"
echo "# binary:   $P"
echo "# pin:      pcrec-cd371441 (abi 23, tip cfcedb0f)"
echo "# bench:    $BENCH_COMMIT  (the one field a re-run may differ on)"
echo "# box:      compile/parse-scale only -- no measurement, no quiet gate needed"
echo "# script:   docs/dev/measurements/accept41_cd371441/run.sh"
echo "# fixtures: docs/dev/measurements/accept41_cd371441/fixtures/ (committed)"
echo "# for:      docs/design/rxt_needs_v1.md 3 ([B42] restart acceptance)"
echo

run() {
    # run <label> <cmd...>
    local label="$1"; shift
    echo "=== $label ==="
    echo "+ $*"
    "$@"
    echo "EXIT=$?"
    echo
}

runstdin() {
    # runstdin <label> <cmd...> < file   -- caller redirects
    local label="$1"; shift
    echo "=== $label ==="
    "$@"
    echo "EXIT=$?"
    echo
}

cp "$FIX"/*.rxt "$SCRATCH"/ 2>/dev/null
cp "$FIX"/*.bin "$SCRATCH"/ 2>/dev/null
cd "$SCRATCH"

# ---------------------------------------------------------------- group A
run "A1  include(head)+tag+mc+@file: all accepted" "$P" --list-source a1.rxt
run "A2  corrected fixture: oracle+use+variant land (config testee/option removed)" "$P" --list-source a2.rxt
run "A2-BEFORE  old-style config-testee/option fixture (control: still refused)" "$P" --list-source a2_old.rxt
run "A3  unknown head keyword names its scope" "$P" --list-source a3.rxt
run "A4  tag inside a config body refused, names the scope" "$P" --list-source a4.rxt
run "A5  tag accumulates: bare label + key=value on two lines" "$P" --list-source a5.rxt

# ---------------------------------------------------------------- group B
run "B1  high-byte pattern -- byte-exact round trip" "$P" --list-source b1.rxt
run "B2  tab/backslash/CR/trailing-space -- byte-exact round trip" "$P" --list-source b2.rxt
run "B3  NUL in a pattern line -- refused BY NAME" "$P" --list-source b3.rxt
run "B4  control: NUL-free file accepted" "$P" --list-source b4.rxt
run "B5a  pattern-esc \\n + trailing \\r (no NUL) -- round trips" "$P" --list-source b5a.rxt
run "B5b  pattern-esc with \\x00 -- refused naming K9" "$P" --list-source b5b.rxt
run "B6  pattern then pattern-esc -- TWO blocks, not a refusal" "$P" --list-source b6.rxt
echo "=== B7  @file: bytes (NUL + high byte) reach the matcher whole -- custom driver ==="
mkdir -p b7work && cd b7work
echo "+ $P -o out.c -p rx --emit-ir >/dev/null; $P -o out.c -p rx '.*'"
"$P" -o out.c -p rx '.*'
echo "+ gcc -O1 -std=gnu11 -Wall -Wextra -o driver ../b7_driver.c out.c"
gcc -O1 -std=gnu11 -Wall -Wextra -o driver ../b7_driver.c out.c
printf '\x00\xff\x41' > subj3.bin
echo "+ xxd subj3.bin"
xxd subj3.bin
echo "+ ./driver subj3.bin   (pattern is '.*', so a whole-subject match at (0,3) proves the 3 bytes -- NUL, 0xff, 'A' -- all reached the engine)"
./driver subj3.bin
echo "EXIT=$?"
cd ..
echo

# ---------------------------------------------------------------- group C
run "C1  tag value outside a declared vocabulary -- refused" "$P" --list-source c1.rxt
run "C2  control: same key, a listed value -- accepted" "$P" --list-source c2.rxt
run "C3  control: key with no vocabulary line -- free vocabulary" "$P" --list-source c3.rxt
run "C4  provenance missing required 'license' -- refused naming it" "$P" --list-source c4.rxt
run "C5  fidelity adapted, no adaptation -- refused" "$P" --list-source c5.rxt
run "C6  control: fidelity verbatim, no adaptation -- accepted" "$P" --list-source c6.rxt
run "C7  a second provenance block -- refused, not last-wins" "$P" --list-source c7.rxt
echo "=== C8  @file: sha256 MISMATCH -- refused by the READER (run.sh), naming both digests ==="
echo "+ TMPDIR=$SCRATCH/tmpwork PCREC=$P bash ~/pcrec/tests/harness/run.sh c8.rxt"
mkdir -p tmpwork
TMPDIR="$SCRATCH/tmpwork" PCREC="$P" bash ~/pcrec/tests/harness/run.sh c8.rxt 2>&1
echo "EXIT=$?"
echo
echo "=== C9  control: @file: sha256 MATCHING -- accepted by the reader ==="
echo "+ TMPDIR=$SCRATCH/tmpwork PCREC=$P bash ~/pcrec/tests/harness/run.sh c9.rxt"
TMPDIR="$SCRATCH/tmpwork" PCREC="$P" bash ~/pcrec/tests/harness/run.sh c9.rxt 2>&1
echo "EXIT=$?"
echo
run "C10  a second description -- STEP 0 resolved as REFUSAL (not last-wins)" "$P" --list-source c10.rxt

# ---------------------------------------------------------------- group D
run "D1  every descriptive production appears in the dump" "$P" --list-source d1.rxt
echo "=== D2  the bench loader has no second .rxt tokenizer (code review) ==="
echo "+ grep -rniE 'rxt.*token|def parse_rxt|rxt_source|class.*RxtParser' $ROOT/pcrecbench/"
grep -rniE 'rxt.*token|def parse_rxt|rxt_source|class.*RxtParser' "$ROOT/pcrecbench/"
echo "grep exit=$? (1 = no match = no second tokenizer)"
echo "+ grep -rl '\\.rxt' $ROOT/pcrecbench/"
grep -rl '\.rxt' "$ROOT/pcrecbench/"
echo "grep exit=$? (1 = pcrecbench/ has no .rxt-reading code AT ALL today -- the loader is UNBUILT, Tier 1 of the restart's next step)"
echo
run "D3  the dump's escaping documented and round-trips (regression: B1/B2 above)" "$P" --list-source b1.rxt
echo "=== D4  the VALIDATES-vs-RECOGNISES table, rendered from --list-schema ==="
"$P" --list-schema 2>&1 | grep -A6 "^#section surface"
echo
run "D5  a case-free file emits NO #section at all" "$P" --list-source d5b.rxt
run "D5b  (precision) a file with case lines but no W23 production STILL emits #section cases" "$P" --list-source d5.rxt

# ---------------------------------------------------------------- group E
echo "=== E1/E2/E3/E6/E7  NOT-RUNNABLE -- no bench/capability@0.1 set or .rxt loader exists yet ==="
echo "(confirmed above at D2: pcrecbench/ has zero .rxt-reading code; building the loader"
echo " and the set is Tier 1 of the restart's NEXT step, per rxt_needs_v1.md section 4 and"
echo " I-69's own work order -- \"run the checklist ... THEN build the set\")"
echo
run "E4  duplicate block name still refused (regression guard, = M7)" "$P" --list-source e4.rxt
echo "=== E5  format half: 'under' produces a #section cases row with the qualifying convention ==="
echo "(see D1's dump above: line 7's row carries under=posix-leftmost-longest)"
echo "(the HARNESS half -- scoring a second testee against it -- is the bench's own unbuilt"
echo " work, R5 finding B1; NOT-RUNNABLE here for that reason)"
echo

# ---------------------------------------------------------------- group F
run "F1  target-less, config-less file parses, exits 0" "$P" --list-source f1.rxt
echo "=== F1b  --source on the same file builds NOTHING, exits 0 (the permanence CONTRACT) ==="
mkdir -p f1out
echo "+ $P --source f1.rxt -o f1out/out"
"$P" --source f1.rxt -o f1out/out 2>&1
echo "EXIT=$?"
echo
echo "=== F2  explicit CLI --engine=dfa vs a target config's 'engine vm' -- CLI wins, diagnostic ==="
mkdir -p f2out
echo "+ $P --source f2.rxt -o f2out/out --engine=dfa"
"$P" --source f2.rxt -o f2out/out --engine=dfa 2>&1
echo "EXIT=$?"
echo
echo "=== F3/F4  NOT-RUNNABLE -- no .rxt-sourced capability set exists yet to gate ==="
echo "(the underlying build-directive guard already exists and was code-reviewed:"
echo " tools/export_rxt.py rule 5 -- 'NO config/flags/engine/budget/encoding lines'):"
grep -n "5\. NO \`config\`" -A2 "$ROOT/tools/export_rxt.py"
echo

# ---------------------------------------------------------------- group G
echo "=== G1  NOT-RUNNABLE -- mandate forbids building/testing in ~/pcrec's tree (BD2) ==="
echo "(pcrec's own I-68 report already states this battery green: strict/axes/san/lint"
echo " rc=0, mech 256/0 anomalies, taken as the delivering party's evidence per BD2)"
echo
echo "=== G2  the five committed exports round-trip against the DELIVERED pin ==="
cd "$ROOT"
for s in email loglines bounded altwide syntax; do
    echo "+ python3 tools/export_rxt.py bench/$s -o $SCRATCH/g2_$s.rxt --verify $P"
    python3 tools/export_rxt.py "bench/$s" -o "$SCRATCH/g2_$s.rxt" --verify "$P" 2>&1
done
cd "$SCRATCH"
echo
echo "=== G3  the thirteen MEASURED facts of rxt_needs_v1.md 1.9, re-run and diffed ==="
echo "+ PCREC_BIN=$P python3 $ROOT/docs/dev/measurements/probe_rxt_format.py"
PCREC_BIN="$P" python3 "$ROOT/docs/dev/measurements/probe_rxt_format.py" > g3_rerun.txt 2>&1
echo "+ diff $ROOT/docs/dev/measurements/2026-09-12-rxt-format-probes-d34c9131.txt g3_rerun.txt"
diff "$ROOT/docs/dev/measurements/2026-09-12-rxt-format-probes-d34c9131.txt" g3_rerun.txt
echo "diff EXIT=$? (non-zero is EXPECTED -- the point of G3 is to classify every hunk,"
echo " not to reproduce the old file; see the archive's own reading of this diff)"
echo

echo "# fixtures + scratch under $SCRATCH (emptied each run)"
