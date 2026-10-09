#!/bin/bash
# [B129] priming A/B: the measurement driver. Run from the repo root (the
# lane worktree), detached; DONE marker = last line of $LOG.
#   setsid bash docs/dev/measurements/2026-10-09-b129-prime-run.sh >/dev/null 2>&1 & disown
# Scratch tier, store build/scratch-store-b129, never store/. Per testee:
# UNPRIMED (A) then PRIMED (B) back to back; a rc-4 cell is re-run once.
# Pin/timeouts as scripts/run_window.sh: --pin 11 --subject-timeout 60
# --driver-timeout 900, CELL_CAP 5400 s.
cd "$(dirname "$0")/../../.." || exit 2
STORE=build/scratch-store-b129
LOG=${LOG:-build/b129-prime-run.log}
CELL_CAP=5400
PIN=11
mkdir -p build
echo "== b129 start $(date -Is) load=$(cat /proc/loadavg)" >> "$LOG"
for t in re2-default rust-default pcrec-auto; do
  for arm in A B; do
    extra=""; [ "$arm" = B ] && extra="--prime"
    echo "-- $t arm=$arm $(date -Is)" >> "$LOG"
    gnutimeout 120 python3 -m pcrecbench quiet --samples 5 --pin $PIN 2>&1 | tail -6 >> "$LOG"
    for attempt in 1 2; do
      gnutimeout $CELL_CAP python3 -m pcrecbench run --subbench capability \
        --testee "$t" --trials 5 --tier scratch --store $STORE --pin $PIN \
        --subject-timeout 60 --driver-timeout 900 $extra >> "$LOG" 2>&1
      rc=$?
      echo "   attempt $attempt rc=$rc $(date -Is)" >> "$LOG"
      [ "$rc" -eq 4 ] || break
    done
  done
done
python3 -m pcrecbench index --store $STORE >> "$LOG" 2>&1
echo "DONE rc=$? $(date -Is)" >> "$LOG"
