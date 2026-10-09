#!/bin/bash
# [B132] third arm WIN = testees/pcrec/{shim.c,driver.c} exactly as of e46e326
# (the 2026-10-08 window-era adapter: [B126], BEFORE [B129]'s prime change), worktree
# b132shim-win (49409c3 + those two files + the same B132_OLDSHIM-free adapter: the
# stamps ARE present, so no adapter patch). Per cell WIN1 WIN2, quick, search, 5 trials, core 11.
# Compare against OLD/MID/NEW in build/b132b (same cells, same session).
W=/home/duxevents/pcrec-bench/worktrees
OUT=${OUT:-$W/b132shim/build/b132b}; LOG=$OUT/run-win.log
echo "== b132 win start $(date -Is) load=$(cat /proc/loadavg)" >> "$LOG"
CELLS="pcrec-auto:winpath-near-miss pcrec-auto:base10num-near-miss pcrec-auto:ipv4-near-miss pcrec-auto:uuid-near-miss pcrec-auto:wild-waf-crs-942360-concat-sqli pcrec-nocaps:trim-nested-star pcrec-nocaps:numeric-id-nested-plus pcrec-nocaps:wild-validator-us-zip-owasp pcrec-nocaps:keyword-prefix-order"
for c in $CELLS; do
  t=${c%%:*}; p=${c#*:}
  for step in WIN WIN2; do
    echo "-- $t $p $step $(date -Is)" >> "$LOG"
    ( cd $W/b132shim-win && gnutimeout 600 nice python3 -m pcrecbench quick --subbench capability --pattern "$p" \
        --regime search --testee $t --trials 5 --pin 11 --store "$OUT/store-$step" ) >> "$LOG" 2>&1
    echo "   rc=$?" >> "$LOG"
  done
done
echo "DONE rc=0 $(date -Is)" >> "$LOG"
