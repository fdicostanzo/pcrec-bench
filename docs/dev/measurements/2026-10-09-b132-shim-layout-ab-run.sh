#!/bin/bash
# [B132] A/B/A/B: SHIM-OLD (worktree b132shim-old: master 49409c3 with
# testees/pcrec/{shim.c,driver.c} from 26eebfa and ONE uncommitted line in
# adapter.py's STAMP_SCOPE check, gated on $B132_OLDSHIM) vs SHIM-NEW (lane
# worktree b132shim = master), both at pin 255bcdd8. quick, scratch, search
# regime (all 75 short subjects), 5 trials, core 11. Order per cell/testee:
# OLD1 NEW1 OLD2 NEW2. One store per (arm,rep).
W=/home/duxevents/pcrec-bench/worktrees
OUT=${OUT:-$W/b132shim/build/b132}
mkdir -p "$OUT"; LOG=$OUT/run.log
echo "== b132 start $(date -Is) load=$(cat /proc/loadavg)" >> "$LOG"
CELLS="pcrec-auto:winpath-near-miss pcrec-auto:base10num-near-miss pcrec-auto:ipv4-near-miss pcrec-auto:wild-semdiv-dollar-trailing-newline-pcre2 pcrec-auto:uuid-near-miss pcrec-auto:router-prefix-order pcrec-auto:wild-validator-email-owasp pcrec-auto:wild-codegrammar-json-stringcontent-escape pcrec-auto:wild-waf-crs-942360-concat-sqli pcrec-auto:keyword-prefix-order pcrec-auto:file-ext-order
pcrec-nocaps:winpath-near-miss pcrec-nocaps:trim-nested-star pcrec-nocaps:numeric-id-nested-plus pcrec-nocaps:phone-list-nested-plus pcrec-nocaps:wild-validator-us-zip-owasp pcrec-nocaps:base10num-near-miss pcrec-nocaps:ipv4-near-miss pcrec-nocaps:wild-semdiv-dollar-trailing-newline-pcre2 pcrec-nocaps:wild-waf-crs-942360-concat-sqli pcrec-nocaps:keyword-prefix-order pcrec-nocaps:bracket-array-define"
for c in $CELLS; do
  t=${c%%:*}; p=${c#*:}
  for step in OLD1 NEW1 OLD2 NEW2; do
    case $step in OLD*) tree=$W/b132shim-old; export B132_OLDSHIM=1;; *) tree=$W/b132shim; unset B132_OLDSHIM;; esac
    echo "-- $t $p $step load=$(cut -d' ' -f1-3 /proc/loadavg) $(date -Is)" >> "$LOG"
    ( cd "$tree" && gnutimeout 600 nice python3 -m pcrecbench quick --subbench capability --pattern "$p" \
        --regime search --testee $t --trials 5 --pin 11 --store "$OUT/store-$step" ) >> "$LOG" 2>&1
    echo "   rc=$?" >> "$LOG"
  done
done
echo "DONE rc=0 $(date -Is)" >> "$LOG"
