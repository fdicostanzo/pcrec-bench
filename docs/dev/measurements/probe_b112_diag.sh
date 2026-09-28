#!/bin/bash
# [B112] I-116 diagnostic: which property does a process fix at startup?
# Cell: row11_fixed (asr-lb-fixed), gcc, orig+twin, synth-dense + synth-64k-asc
# (the widest split). Six experiments (0-3f), run in order; each prints a
# labelled block. WORKDIR default /var/tmp/b112bimodal-scratch; it must
# already hold bin/row11_fixed_{orig,twin}_gcc_{ctl,align,probe,probe2,
# align64code}, built from the SAME row11_fixed*.c sources [B109]'s
# probe_b109_reseed_twin.py workdir produced (bench d0220be, pcrec pin
# a32bc86e), each with a different driver/CFLAGS:
#   gcc -O2 -Wall -Wextra -o bin/row11_fixed_${v}_gcc_ctl      $src drv.c            -lm
#   gcc -O2 -Wall -Wextra -o bin/row11_fixed_${v}_gcc_align    $src probe_b112_drv_align.c  -lm
#   gcc -O2 -Wall -Wextra -o bin/row11_fixed_${v}_gcc_probe    $src probe_b112_drv_probe.c  -lm
#   gcc -O2 -Wall -Wextra -o bin/row11_fixed_${v}_gcc_probe2   $src probe_b112_drv_probe2.c -lm
#   gcc -O2 -falign-functions=64 -falign-loops=64 -Wall -Wextra \
#       -o bin/row11_fixed_${v}_gcc_align64code $src probe_b112_drv_probe.c -lm
# ($src = row11_fixed.c for orig, row11_fixed_twin.c for twin; drv.c is
# [B109]'s own driver, copied unmodified into WORKDIR.) After this script
# runs, derive the summary table with:
#   python3 probe_b112_summarize.py OUT_probe.txt OUT_probe2.txt
#   python3 probe_b112_summarize_pipe.py OUT_sections012.txt OUT_3e3f.txt
set -u
W=${1:-/var/tmp/b112bimodal-scratch}
SUBJDIR=/var/tmp/b109twin-htuo1bxs/subjects
N=${N:-15}
NOFF=${NOFF:-5}

echo "=== [B112] diagnostic run $(date -Iseconds) ==="
echo "=== host load/context ==="
uptime
echo

# ---------- Sanity: reproduce the known bimodal split with our _ctl build ----------
echo "=== 0. SANITY: _ctl build (plain drv.c, same as archived bin/) reproduces bimodality ==="
for v in orig twin; do
  for s in synth-dense synth-64k-asc; do
    vals=$(for i in $(seq $N); do /usr/bin/gnutimeout 30 $W/bin/row11_fixed_${v}_gcc_ctl $SUBJDIR/$s.bin 21 | grep -o "best_us=[0-9.]*" | cut -d= -f2; done)
    st=$(echo "$vals" | sort -g | awk '{a[NR]=$1} END{printf "min=%.3f med=%.3f max=%.3f", a[1], a[int((NR+1)/2)], a[NR]}')
    printf "%-6s %-14s %s | %s\n" $v $s "$st" "$(echo $vals)"
  done
done
echo

# ---------- 1. ASLR off vs on ----------
echo "=== 1. ASLR OFF (setarch -R) vs ON, $N launches each, gcc orig+twin, both subjects ==="
for mode in on off; do
  for v in orig twin; do
    for s in synth-dense synth-64k-asc; do
      if [ "$mode" = off ]; then
        vals=$(for i in $(seq $N); do /usr/bin/gnutimeout 30 setarch $(uname -m) -R $W/bin/row11_fixed_${v}_gcc_ctl $SUBJDIR/$s.bin 21 | grep -o "best_us=[0-9.]*" | cut -d= -f2; done)
      else
        vals=$(for i in $(seq $N); do /usr/bin/gnutimeout 30 $W/bin/row11_fixed_${v}_gcc_ctl $SUBJDIR/$s.bin 21 | grep -o "best_us=[0-9.]*" | cut -d= -f2; done)
      fi
      st=$(echo "$vals" | sort -g | awk '{a[NR]=$1} END{printf "min=%.3f med=%.3f max=%.3f", a[1], a[int((NR+1)/2)], a[NR]}')
      printf "aslr=%-3s %-6s %-14s %s | %s\n" $mode $v $s "$st" "$(echo $vals)"
    done
  done
done
echo

# ---------- 2. Subject-buffer alignment sweep ----------
echo "=== 2. ALIGNMENT SWEEP: posix_memalign(4096)+OFFSET, $NOFF launches/offset, gcc orig+twin, both subjects ==="
for v in orig twin; do
  for s in synth-dense synth-64k-asc; do
    for off in 0 8 16 32 48 63; do
      vals=$(for i in $(seq $NOFF); do /usr/bin/gnutimeout 30 $W/bin/row11_fixed_${v}_gcc_align $SUBJDIR/$s.bin 21 $off | grep -o "best_us=[0-9.]*" | cut -d= -f2; done)
      st=$(echo "$vals" | sort -g | awk '{a[NR]=$1} END{printf "min=%.3f med=%.3f max=%.3f", a[1], a[int((NR+1)/2)], a[NR]}')
      printf "off=%-3s %-6s %-14s %s | %s\n" $off $v $s "$st" "$(echo $vals)"
    done
  done
done
echo

# ---------- 3. Counters substituted: placement telemetry, fast vs slow ----------
echo "=== 3a. PLACEMENT TELEMETRY (normal ASLR): gcc orig+twin, synth-64k-asc (widest split), $N launches, full line ==="
for v in orig twin; do
  for i in $(seq $N); do
    /usr/bin/gnutimeout 30 $W/bin/row11_fixed_${v}_gcc_probe $SUBJDIR/synth-64k-asc.bin 21
  done | sed "s/^/probe v=$v /"
done
echo

echo "=== 3b. PLACEMENT TELEMETRY, ASLR OFF: gcc orig+twin, synth-64k-asc, $N launches ==="
for v in orig twin; do
  for i in $(seq $N); do
    /usr/bin/gnutimeout 30 setarch $(uname -m) -R $W/bin/row11_fixed_${v}_gcc_probe $SUBJDIR/synth-64k-asc.bin 21
  done | sed "s/^/probe-noaslr v=$v /"
done
echo

echo "=== 3c. CODE-PLACEMENT ARM: -falign-functions=64 -falign-loops=64, gcc orig+twin, synth-64k-asc, $N launches ==="
for v in orig twin; do
  for i in $(seq $N); do
    /usr/bin/gnutimeout 30 $W/bin/row11_fixed_${v}_gcc_align64code $SUBJDIR/synth-64k-asc.bin 21
  done | sed "s/^/probe-align64 v=$v /"
done
echo

# ---------- 3d. CPU id + scaling_cur_freq per launch ----------
echo "=== 3d. CPU id + scaling_cur_freq per launch (normal ASLR): gcc orig+twin, synth-64k-asc, 30 launches ==="
for v in orig twin; do
  for i in $(seq 30); do
    /usr/bin/gnutimeout 30 $W/bin/row11_fixed_${v}_gcc_probe2 $SUBJDIR/synth-64k-asc.bin 21
  done | sed "s/^/probe2 v=$v /"
done
echo

# ---------- 3e. taskset pin vs unpinned ----------
echo "=== 3e. taskset -c 3 pinned (single core kept warm across the loop) vs unpinned, gcc orig+twin, synth-64k-asc, 20 launches ==="
for v in orig twin; do
  for mode in pinned unpinned; do
    if [ "$mode" = pinned ]; then
      vals=$(for i in $(seq 20); do /usr/bin/gnutimeout 30 taskset -c 3 $W/bin/row11_fixed_${v}_gcc_probe2 $SUBJDIR/synth-64k-asc.bin 21 | grep -o "best_us=[0-9.]*" | cut -d= -f2; done)
    else
      vals=$(for i in $(seq 20); do /usr/bin/gnutimeout 30 $W/bin/row11_fixed_${v}_gcc_probe2 $SUBJDIR/synth-64k-asc.bin 21 | grep -o "best_us=[0-9.]*" | cut -d= -f2; done)
    fi
    st=$(echo "$vals" | sort -g | awk '{a[NR]=$1} END{printf "min=%.3f med=%.3f max=%.3f", a[1], a[int((NR+1)/2)], a[NR]}')
    printf "%-9s %-6s %s | %s\n" $mode $v "$st" "$(echo $vals)"
  done
done
echo

# ---------- 3f. deliberate idle gap vs back-to-back ----------
echo "=== 3f. deliberate idle gap (sleep 0.3 between launches, lets the core decay to a deeper C-state) vs back-to-back, gcc orig+twin, synth-64k-asc, 15 launches ==="
for v in orig twin; do
  for mode in gap noback; do
    if [ "$mode" = gap ]; then
      vals=$(for i in $(seq 15); do sleep 0.3; /usr/bin/gnutimeout 30 $W/bin/row11_fixed_${v}_gcc_probe2 $SUBJDIR/synth-64k-asc.bin 21 | grep -o "best_us=[0-9.]*" | cut -d= -f2; done)
    else
      vals=$(for i in $(seq 15); do /usr/bin/gnutimeout 30 $W/bin/row11_fixed_${v}_gcc_probe2 $SUBJDIR/synth-64k-asc.bin 21 | grep -o "best_us=[0-9.]*" | cut -d= -f2; done)
    fi
    st=$(echo "$vals" | sort -g | awk '{a[NR]=$1} END{printf "min=%.3f med=%.3f max=%.3f", a[1], a[int((NR+1)/2)], a[NR]}')
    printf "%-8s %-6s %s | %s\n" $mode $v "$st" "$(echo $vals)"
  done
done
echo

echo "=== host load/context (end) ==="
uptime
echo "DONE rc=0"
