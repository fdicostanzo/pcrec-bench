#!/bin/bash
# [B133] the lane's OWED heavy runs, as ONE detached chain (BD3: one heavy job
# at a time): (1) wait for a quiet box (3 consecutive `pcrecbench quiet`
# passes, polled every 60 s, up to 3 h), (2) the instrument A/B/A/B
# (scripts/instrument_ab.sh, BEFORE = master ec62878 = the pre-[B133] driver),
# (3) `make check-harness`. Markers: OUT/chain.log ends `CHAIN_DONE ab_rc=.. check_rc=..`.
#   setsid scripts/b133_owed_run.sh OUTDIR > /dev/null 2>&1 &
set -u
export LC_ALL=C
REPO=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd); cd "$REPO" || exit 9
OUT=$(realpath -m "${1:?OUTDIR}"); mkdir -p "$OUT"; L=$OUT/chain.log
echo "chain start $(date -Is)" >> "$L"
ok=0; deadline=$(( $(date +%s) + 10800 ))
while [ "$(date +%s)" -lt "$deadline" ]; do
  if gnutimeout 60 python3 -m pcrecbench quiet --samples 3 >/dev/null 2>&1; then ok=$((ok+1)); else ok=0; fi
  [ $ok -ge 3 ] && break
  sleep 60
done
if [ $ok -lt 3 ]; then echo "CHAIN_DONE quiet-wait-timeout (nothing measured) $(date -Is)" >> "$L"; exit 3; fi
echo "quiet confirmed $(date -Is) load=$(cat /proc/loadavg)" >> "$L"
scripts/instrument_ab.sh ec62878 "$OUT/ab" >> "$L" 2>&1; ab=$?
echo "ab done rc=$ab $(date -Is)" >> "$L"
gnutimeout 7200 make check-harness > "$OUT/check-harness.log" 2>&1; ck=$?
echo "CHAIN_DONE ab_rc=$ab check_rc=$ck $(date -Is)" >> "$L"
