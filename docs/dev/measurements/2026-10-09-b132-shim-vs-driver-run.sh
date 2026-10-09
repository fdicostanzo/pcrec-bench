#!/bin/bash
# [B132] follow-up factor split: master's driver.c differs from 26eebfa's too ([B129]'s
# --prime restructure of the timed loop, + new dlsyms), so the A/B above moves BOTH files.
# Arms (all at pin 255bcdd8, quick, search, 5 trials, core 11):
#   OLD = shim.c+driver.c @26eebfa   (worktree b132shim-old)
#   MID = shim.c @master + driver.c @26eebfa   (worktree b132shim-mid)  -> the shim alone
#   NEW = shim.c+driver.c @master    (worktree b132shim)               -> + the driver
# Per cell: OLD MID NEW MID2. MID/OLD = shim effect; NEW/MID = driver effect.
W=/home/duxevents/pcrec-bench/worktrees
OUT=${OUT:-$W/b132shim/build/b132b}; mkdir -p "$OUT"; LOG=$OUT/run.log
echo "== b132b start $(date -Is) load=$(cat /proc/loadavg)" >> "$LOG"
CELLS="pcrec-auto:winpath-near-miss pcrec-auto:base10num-near-miss pcrec-auto:ipv4-near-miss pcrec-auto:uuid-near-miss pcrec-auto:wild-waf-crs-942360-concat-sqli pcrec-nocaps:trim-nested-star pcrec-nocaps:numeric-id-nested-plus pcrec-nocaps:wild-validator-us-zip-owasp pcrec-nocaps:keyword-prefix-order"
for c in $CELLS; do
  t=${c%%:*}; p=${c#*:}
  for step in OLD MID NEW MID2; do
    case $step in OLD) tree=$W/b132shim-old; export B132_OLDSHIM=1;; MID|MID2) tree=$W/b132shim-mid; export B132_OLDSHIM=1;; NEW) tree=$W/b132shim; unset B132_OLDSHIM;; esac
    echo "-- $t $p $step $(date -Is)" >> "$LOG"
    ( cd "$tree" && gnutimeout 600 nice python3 -m pcrecbench quick --subbench capability --pattern "$p" \
        --regime search --testee $t --trials 5 --pin 11 --store "$OUT/store-$step" ) >> "$LOG" 2>&1
    echo "   rc=$?" >> "$LOG"
  done
done
echo "DONE rc=0 $(date -Is)" >> "$LOG"
