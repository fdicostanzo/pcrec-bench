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
# retried thrice with a 20 s backoff, as before this script existed.
#
# ENV-OVERRIDABLE (defaults shown; every one may be set on the command line
# before this script, e.g. `SUBBENCH=loglines TRIALS=5 scripts/run_window.sh`):
#
#   SUBBENCH   email                 -- the sub-bench to measure
#   PIN        11                    -- the CPU core `pcrecbench run --pin` uses
#   TRIALS     5                     -- trials per cell
#   STORE      store                 -- the record store (real windows: `store`)
#   TESTEES    "pcre2-interp pcre2-jit pcrec-auto pcrec-nocaps pcrec-vm pcrec-vm-in"
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
# vars to remember -- sets EXTRA to include `--synthetic --force-unquiet`
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

gnutimeout 120 python3 -m pcrecbench quiet --samples 6 --pin "$PIN" 2>&1 | tail -4 | tee -a "$LOG"

first=1
for t in $TESTEES; do
  if [ "$first" -eq 0 ]; then
    sleep 15
  fi
  first=0
  echo "-- cell $SUBBENCH x $t $(date -Is) load=$(cut -d' ' -f1-3 /proc/loadavg)" | tee -a "$LOG"
  for attempt in 1 2 3; do
    gnutimeout 3000 python3 -m pcrecbench run --subbench "$SUBBENCH" --testee "$t" \
        --trials "$TRIALS" --pin "$PIN" --subject-timeout 60 --driver-timeout 900 \
        --store "$STORE" $EXTRA --note "$NOTE" >> "$LOG" 2>&1
    rc=$?
    echo "   attempt $attempt rc=$rc $(date -Is)" | tee -a "$LOG"
    [ "$rc" -eq 3 ] || break
    sleep 20
  done
done

gnutimeout 120 python3 -m pcrecbench index --store "$STORE" 2>&1 | tail -2 | tee -a "$LOG"
echo "== window run end $(date -Is) load=$(cat /proc/loadavg)" | tee -a "$LOG"
echo "WINDOW_RUN_COMPLETE" >> "$LOG"
