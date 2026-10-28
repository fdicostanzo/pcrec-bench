#!/bin/bash
# one scratch cell per assisted config, all regimes, sequential; wall time per cell in $OUT/walls.tsv
W=/home/pcrec/projects/pcrec-bench/worktrees/b148heldout; O=/var/tmp/pcrecbench/b148heldout
for t in pcre2-jit onig-default re2-default rust-default vectorscan-block-som; do
  s=$(date +%s); mkdir -p $O/$t
  (cd $W && nice gnutimeout 3000 python3 docs/dev/measurements/2026-10-28-b148heldout-probe.py $O/$t $t-assist-v01 --subject-timeout 30 > $O/$t.log 2>&1); rc=$?
  printf "%s\t%s\t%s\n" $t $rc $(( $(date +%s)-s )) >> $O/walls.tsv
done
echo "DONE" > $O/chain.done
