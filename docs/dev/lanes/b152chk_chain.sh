#!/bin/bash
# [B152] the owed full `make -k check` at d6c5e71a5 (abi 112), NO taskset (env.cores() reads affinity).
# Non-timing; pcrec_main 2026-11-24: run beside Frank's daytime use, refuse after 19:30 (his 20:00 hold).
# Submit: setsid scripts/boxq_window --name b152chk --prio 700 --cap 36000 -- <this file>
# Completion: /var/tmp/pcrecbench/b152chk/chain.log ends `CHK_DONE rc=N` (or `CHK_REFUSED`).
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd) || exit 9
cd "$HERE" || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b152chk
mkdir -p "$W"
L=$W/chain.log
STOP=$(date -d 'today 19:30' +%s)
NOW=$(date +%s)
echo "CHK_START $(date -Is) head=$(git rev-parse --short HEAD)" >> "$L"
if [ "$NOW" -ge "$STOP" ]; then
  echo "CHK_REFUSED past 19:30 $(date -Is)" >> "$L"
  exit 0
fi
gnutimeout $((STOP - NOW)) make -k check > "$W/make_check.log" 2>&1
rc=$?
echo "CHK_DONE rc=$rc $(date -Is)" >> "$L"
exit $rc
