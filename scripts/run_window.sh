#!/bin/bash
# scripts/run_window.sh -- a QUIET-WINDOW cell run: one sub-bench, one
# testee list, one pcrec pin, measured PINNED-TIER into a real store
# ([B12] close item: committed here rather than kept as a scratchpad copy
# a manager session re-typed by hand each window; the copy this generalises
# is `docs/dev/dev_journal.md`'s third-session part 7, 2026-08-28).
#
# MUST BE LAUNCHED UNDER `setsid` -- a harness background task has a
# 10-minute cap, and a real window (SUBBENCH=loglines, six testees, 5
# trials each) runs far longer than that:
#
#     setsid scripts/run_window.sh > /dev/null 2>&1 &
#
# One cell at a time, pinned to one core, records into the REAL store; rc 3
# == the harness's own quiet gate refused a cell on a transient (OD-B12) --
# retried up to twelve times with a 30 s backoff (THE GATE BUDGET below);
# rc 4 (schema v1.4, [B20], contract 4) == the cell was WRITTEN and indexed
# as `inconclusive-spread` (the box was quiet, the trials did not agree) --
# re-measured ONCE, logged, then on to the next cell: a spread is not a
# gate transient, and the first record is never deleted (ruling R-6).
#
# ENV-OVERRIDABLE (defaults shown; every one may be set on the command line
# before this script, e.g. `SUBBENCH=loglines TRIALS=5 scripts/run_window.sh`):
#
#   SUBBENCH   email                 -- the sub-bench to measure
#   PIN        11                    -- the CPU core `pcrecbench run --pin` uses
#   TRIALS     5                     -- trials per cell
#   STORE      store                 -- the record store (real windows: `store`)
#   TESTEES    "pcre2-interp pcre2-jit pcrec-auto pcrec-nocaps pcrec-vm pcrec-vm-in"
#              ([B24]) the compilee-toolchain axis adds pcrec-auto-clang /
#              pcrec-nocaps-clang / pcrec-vm-clang -- run them as their OWN
#              TESTEES list, beside the gcc six, so the pair is one variable
#              apart. Do not export $CC for such a window: a $CC that
#              contradicts a config's declared `cc` is refused by name.
#              ([B31]) the emitted-size cap axis adds pcrec-auto-bigcap /
#              pcrec-vm-bigcap, and they belong to bench/altwide's window
#              ALONE -- every other set compiles inside pcrec's default
#              caps, where a bigcap testee would measure the same artifact
#              as its plain sibling. Run them as their own TESTEES list
#              (or, under run_suite.sh, as $TESTEES_altwide / a labelled
#              second pass `altwide:bigcap` with $TESTEES_altwide_bigcap).
#   NOTE       "quiet window run, $(date -Is)"
#   LOG        build/windows/window_${SUBBENCH}_$(date +%Y%m%dT%H%M%SZ).log
#              (gitignored -- `build/` is in .gitignore already)
#   EXTRA      ""                    -- extra flags appended to every `run`
#              (the REHEARSAL knob: EXTRA="--synthetic --force-unquiet"
#              STORE=<a scratch dir> TRIALS=1 makes every cell synthetic,
#              skips the quiet gate, and runs one trial -- provably light.
#              `--dry-run` below sets exactly this combination for you.)
#
# --dry-run: the rehearsal mode spelled as a flag instead of three env
# vars to remember -- sets EXTRA to include `--synthetic --force-unquiet
# --tier scratch` (the tier: a one-trial PINNED record is inconclusive-spread
# by rule R-12 and would be re-measured; see below)
# (appended to whatever EXTRA already had), TRIALS=1 unless already set,
# and STORE to a scratch dir under build/ unless STORE was already
# pointed somewhere under build/ or $PCRECBENCH_SCRATCH_STORE. Refuses to
# run if STORE still resolves to the canonical `store` (the same refusal
# `pcrecbench run --tier scratch --store store` gives, checked here too
# so a rehearsal typo cannot land synthetic records in the real store).
#
# THE SLEEP-15 FIX (OD-B12, 2026-08-28): every cell after the FIRST needed
# a retry on the quiet gate's post-cell transient that day -- the box
# reads as busy for a second or two right after one `run` process exits,
# so the very next cell's OWN first quiet-gate sample (inside
# `pcrecbench run`, not this script's own `quiet` warm-up below) came back
# not-quiet and burned a whole 20 s retry cycle on every cell but the
# first. A flat `sleep 15` before a NON-FIRST cell's first attempt (never
# before the retries, which already sleep 20) is cheap insurance against
# that specific transient and is provably harmless: a truly quiet box
# stays quiet across 15 idle seconds.
#
# THE PER-CELL CAP (2026-09-02, the [B26] full-suite night): `gnutimeout 5400`
# around each `run`, up from 3000. bounded@0.3's clang cells ran 49-50 min
# (auto-clang 49:22 measured; nocaps-clang and vm-clang KILLED at 50:00 with
# rc 124, both re-run by hand after the suite) against the old 3000 s cap --
# a cap sized for 0.1/0.2's ~20-min cells. A cap firing is a lost cell with
# no record, indistinguishable in the suite summary from a clean set (the
# set's rc is the index's), so the budget now sits ~2x above the longest
# measured cell (bounded@0.3 x pcrec-vm-clang, ~50 min). rc 124 is logged
# per attempt; grep the window logs for it after every window.
#
# THE GATE BUDGET (2026-08-29, the 36d5963 window): 3 x 20 s LOST cells
# that day -- a peer lane's breach and, after it, the two managers' own
# claude processes (~9 % + ~6 % CPU while streaming) left an 11 % residue
# on one core against the gate's 10 % limit, and a refused cell's next
# cell meets the same box. 12 x 30 s (six minutes per cell) carried every
# one of the 12 + 3 cells that day on attempt 1-3. The `sleep 15` did NOT
# cover the post-cell transient (every cell after the first still refused
# once); the budget is what covers it.
set -u
export LC_ALL=C

# Capture "was this already set by the caller" BEFORE applying defaults --
# --dry-run needs to know whether to override TRIALS/STORE or leave an
# explicit caller choice alone.
_trials_was_set=${TRIALS+x}
_store_was_set=${STORE+x}

SUBBENCH=${SUBBENCH:-email}
PIN=${PIN:-11}
TRIALS=${TRIALS:-5}
STORE=${STORE:-store}
EXTRA=${EXTRA:-}
TESTEES=${TESTEES:-"pcre2-interp pcre2-jit pcrec-auto pcrec-nocaps pcrec-vm pcrec-vm-in"}
NOTE=${NOTE:-"quiet window run, $(date -Is)"}
DRY_RUN=0

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    *) echo "run_window.sh: unrecognized argument: $arg" >&2; exit 2 ;;
  esac
done

REPO=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd) || exit 9
cd "$REPO" || exit 9

if [ "$DRY_RUN" -eq 1 ]; then
  case " $EXTRA " in
    *" --synthetic "*) : ;;
    *) EXTRA="$EXTRA --synthetic" ;;
  esac
  case " $EXTRA " in
    *" --force-unquiet "*) : ;;
    *) EXTRA="$EXTRA --force-unquiet" ;;
  esac
  # SCRATCH TIER, too (2026-09-01, [B26]'s rehearsal of the full suite): a
  # PINNED record with fewer than five trials is `inconclusive-spread` by
  # the status table's own rule (harness.py: "R empty, V n/a, pinned" --
  # ruling R-12), so a one-trial rehearsal on a QUIET box exited 4 and was
  # re-measured once per cell -- twice the rehearsal time to prove the same
  # thing. At the scratch tier the same n/a verdict reads `measured` (E-2),
  # which is what a rehearsal is: never a ranking input either way.
  case " $EXTRA " in
    *" --tier scratch "*) : ;;
    *) EXTRA="$EXTRA --tier scratch" ;;
  esac
  EXTRA="${EXTRA# }"
  [ -n "$_trials_was_set" ] || TRIALS=1
  [ -n "$_store_was_set" ] || STORE="${PCRECBENCH_SCRATCH_STORE:-build/scratch-store}"
fi

# Refuse a rehearsal (or a plain mistake) that still points at the
# canonical store -- `pcrecbench run` refuses a synthetic/scratch record
# into `store` on its own (store.py's `.canonical` marker), but failing
# here, before spawning anything, is a clearer message for this script's
# own purpose.
if [ "$DRY_RUN" -eq 1 ] && [ "$STORE" = "store" ]; then
  echo "run_window.sh --dry-run: refusing to rehearse into the canonical store/ -- set STORE to a scratch dir" >&2
  exit 9
fi

LOG=${LOG:-build/windows/window_${SUBBENCH}_$(date -u +%Y%m%dT%H%M%SZ).log}
mkdir -p "$(dirname "$LOG")" || exit 9

echo "== window run start $(date -Is) subbench=$SUBBENCH store=$STORE dry_run=$DRY_RUN load=$(cat /proc/loadavg)" | tee -a "$LOG"

# The warm-up is ADVISORY: `quiet` now judges every sample through the same
# `gate()` a run's pre-flight uses (v1.4, ruling R-7), but its exit code is
# discarded by this pipe on purpose -- the per-cell `run` below makes the
# binding decision, with the retry budget, and a window that refused to
# start on one warm-up sample would lose the cells that budget carries.
gnutimeout 120 python3 -m pcrecbench quiet --samples 6 --pin "$PIN" 2>&1 | tail -6 | tee -a "$LOG"

first=1
for t in $TESTEES; do
  if [ "$first" -eq 0 ]; then
    sleep 15
  fi
  first=0
  echo "-- cell $SUBBENCH x $t $(date -Is) load=$(cut -d' ' -f1-3 /proc/loadavg)" | tee -a "$LOG"
  spread_retried=0
  for attempt in 1 2 3 4 5 6 7 8 9 10 11 12; do
    gnutimeout 5400 python3 -m pcrecbench run --subbench "$SUBBENCH" --testee "$t" \
        --trials "$TRIALS" --pin "$PIN" --subject-timeout 60 --driver-timeout 900 \
        --store "$STORE" $EXTRA --note "$NOTE" >> "$LOG" 2>&1
    rc=$?
    echo "   attempt $attempt rc=$rc $(date -Is)" | tee -a "$LOG"
    if [ "$rc" -eq 4 ]; then
      # inconclusive-spread: the record is written; re-measure ONCE (R-6).
      if [ "$spread_retried" -eq 0 ]; then
        spread_retried=1
        echo "   inconclusive-spread: re-measuring this cell once (the first record stays)" | tee -a "$LOG"
        sleep 15
        continue
      fi
      echo "   inconclusive-spread twice: moving on" | tee -a "$LOG"
      break
    fi
    [ "$rc" -eq 3 ] || break
    sleep 30
  done
done

gnutimeout 120 python3 -m pcrecbench index --store "$STORE" 2>&1 | tail -3 | tee -a "$LOG"
echo "== window run end $(date -Is) load=$(cat /proc/loadavg)" | tee -a "$LOG"
echo "WINDOW_RUN_COMPLETE" >> "$LOG"
