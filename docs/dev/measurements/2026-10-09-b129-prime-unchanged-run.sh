#!/bin/bash
# [B129] "unprimed behaviour unchanged" control for the restructured --prime
# drivers: master's driver (worktree worktrees/b129ctl, lane/b129ctl at
# 957edd2, a pristine master checkout) vs the fixed driver (this lane),
# BOTH WITHOUT --prime, back to back M,F,M,F; pcrec-auto and re2-default;
# one search cell (tail-ext-lower-txt, --subjects 20) and one throughput cell
# (tail-dotstar-txt); quick, scratch tier, 5 trials, core 11. Separate
# scratch stores per tree. Run from the lane worktree root.
W=$(cd "$(dirname "$0")/../../.." && pwd)
C=$(dirname "$W")/b129ctl
LOG=${LOG:-$W/build/b129-prime-unchanged.log}
echo "== start $(date -Is) load=$(cat /proc/loadavg)" >> "$LOG"
run() {  # tree label pattern regime testee extra
  ( cd "$1" && gnutimeout 600 python3 -m pcrecbench quick --subbench capability \
      --pattern "$3" --regime "$4" --testee "$5" --trials 5 --pin 11 $6 \
      --store build/scratch-store-b129unch ) >> "$LOG" 2>&1
  echo "   rc=$?" >> "$LOG"
}
for cell in "tail-ext-lower-txt search --subjects 20" "tail-dotstar-txt throughput"; do
  set -- $cell; p=$1; r=$2; x="${3:-} ${4:-}"
  for t in pcrec-auto re2-default; do
    for rep in 1 2; do
      for tree in master fixed; do
        d=$C; [ $tree = fixed ] && d=$W
        echo "-- $tree rep$rep $p $r $t load=$(cut -d' ' -f1-3 /proc/loadavg) $(date -Is)" >> "$LOG"
        run "$d" $tree $p $r $t "$x"
      done
    done
  done
done
echo "DONE $(date -Is)" >> "$LOG"
