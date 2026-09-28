#!/bin/bash
# [B109] addendum: per-PROCESS bimodality of the I-114 reseed-twin driver.
# Each cell is launched N times as a fresh process (21 trials each, best_us
# kept); prints every launch's best_us, then min / median across launches.
# Usage: probe_b109_multilaunch.sh WORKDIR [N]   (WORKDIR = the probe_b109_
# reseed_twin.py workdir holding bin/ and subjects/; N default 15)
W=${1:?workdir}; N=${2:-15}
for p in row1_varwidth row10_neg row11_fixed; do
 for s in synth-64k-asc synth-dense synth-1m t-64k-cyr t-64k-asc; do
  for v in orig_gcc twin_gcc orig_clang twin_clang; do
   vals=$(for i in $(seq $N); do /usr/bin/gnutimeout 30 $W/bin/${p}_$v $W/subjects/$s.bin 21 | grep -o "best_us=[0-9.]*" | cut -d= -f2; done)
   st=$(echo "$vals" | sort -g | awk '{a[NR]=$1} END{printf "min=%.3f med=%.3f max=%.3f", a[1], a[int((NR+1)/2)], a[NR]}')
   printf "%-14s %-14s %-11s %s | %s\n" $p $s $v "$st" "$(echo $vals)"
  done
 done
done
