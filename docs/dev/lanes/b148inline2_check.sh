#!/bin/bash
# Lane b148inline2 CHECK CHAIN (written 2026-11-01, NOT RUN by the lane; the manager queues it
# when the box is free). In worktrees/b148inline2 (or the merged tree via CHAIN_TREE=...):
#   1. link build/pcrec-* from the main tree if the tree has none (pin.sh reuses a build),
#   2. the new build-dependent section: tools/check_unusual.py --only inline inline-pcrec
#      (the source-only inline section, then check_inline_pcrec),
#   3. `make -k check` (selfcheck's frozen-renderer arm, the b149 grant check, the capability
#      rosters, check-unusual in full).
# Logs under /var/tmp/pcrecbench/b148inline2win/; real rcs in *.rc files; always exits 0.
W=/var/tmp/pcrecbench/b148inline2win
T=${CHAIN_TREE:-/home/pcrec/projects/pcrec-bench/worktrees/b148inline2}
MAIN=/home/pcrec/projects/pcrec-bench
mkdir -p "$W"
cd "$T" || exit 9
export LC_ALL=C
echo "CHAIN_START $(date -Is) tree $T load $(cat /proc/loadavg)" >> "$W/chain.log"
mkdir -p build
for d in "$MAIN"/build/pcrec-*; do
  [ -e "$d" ] && [ ! -e "build/$(basename "$d")" ] && ln -s "$d" "build/$(basename "$d")"
done
echo "LINKED $(ls build | grep -c '^pcrec-') pcrec builds" >> "$W/chain.log"
/usr/bin/gnutimeout 3600 python3 -I tools/check_unusual.py --only inline inline-pcrec > "$W/inline.log" 2>&1
echo "$?" > "$W/inline.rc"
echo "INLINE_DONE rc=$(cat "$W/inline.rc") $(date -Is)" >> "$W/chain.log"
/usr/bin/gnutimeout 14400 make -k check > "$W/check.log" 2>&1
rc=$?
echo "$rc" > "$W/check.rc"
echo "CHECK_DONE rc=$rc $(date -Is)" >> "$W/chain.log"
echo "CHAIN_DONE $(date -Is)" >> "$W/chain.log"
exit 0
