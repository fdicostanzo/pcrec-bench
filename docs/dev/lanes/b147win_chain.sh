#!/bin/bash
# [B147] FIRST WINDOW at 614d45eb3 (abi 89) -- the manager, 2026-10-28; Frank's
# go (live, "3&4 ok, coord with main"); pcrec_main cleared the tier the same
# morning (I-154 + [B147]: capability x {pcrec-auto, pcrec-nocaps}, plus the
# callout rows; order A before the [B148] L9 readout). Copied from
# b142win_chain.sh: capability at the canonical pin AND at @9ae59f5d4 (the
# same-window BEFORE, so the cross-pin Delta has a same-window partner), then
# bench/syntax x {pcrec-auto, pcrec-nocaps} at the canonical pin only (the
# grp-callout rows compile at abi 89 and did not at 9ae59f5d4); opening +
# closing sentinel passes. Launched through the box queue:
#
#     setsid scripts/boxq_window --name b147win --prio 7NN --cap S -- \
#         env MACHINE_ID=ryzen7700x bash docs/dev/lanes/b147win_chain.sh
#
# Completion: /var/tmp/pcrecbench/b147win/chain.log ends `CHAIN_DONE`;
# `CHAIN_ABORT` = nothing measured (exit 9).
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b147win; mkdir -p "$W"
L=$W/chain.log
export PIN=${PIN:-7}
STORE=store
echo "CHAIN_START $(date -Is) PIN=$PIN MACHINE_ID=${MACHINE_ID:-<unset>}" >> "$L"
abort() { echo "CHAIN_ABORT $*" >> "$L"; exit 9; }
[ -n "${MACHINE_ID:-}" ] || abort "MACHINE_ID is not set; nothing measured"

B=9ae59f5d4
R_SENT="pcrec-auto pcrec-auto@$B pcrec-nocaps pcre2-jit"
R_CAP="pcrec-auto pcrec-nocaps pcrec-auto@$B pcrec-nocaps@$B"
R_SYN="pcrec-auto pcrec-nocaps"

python3 -m pcrecbench testees 2>>"$L" | awk '{print $1}' > "$W/testees.names"
for t in $R_SENT $R_CAP $R_SYN; do
  grep -qx -- "${t%@*}" "$W/testees.names" || abort "testee '$t' does not resolve"
done
read -r HOSTN CPUSLUG NCORES < <(python3 -c "
import platform
from pcrecbench import env
print(platform.node() or 'unknown', env.canon_cpu_model(env.cpu_model_raw()), env.cores())")
python3 -m pcrecbench machines register --store "$STORE" --machine-id "$MACHINE_ID" \
    --hostname "$HOSTN" --cpu-model "$CPUSLUG" --cores "$NCORES" \
    --first-seen "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --note "[B147] b147win_chain.sh" >> "$L" 2>&1 \
  || abort "machines register ($MACHINE_ID $HOSTN) refused"
for s in 614d45eb3 $B; do
  sh testees/pcrec/pin.sh --path $s >> "$L" 2>&1 || abort "no build of $s"
done
for d in sentinel capability syntax; do
  for g in gen_subjects.py gen_throughput_subjects.py; do
    [ -f bench/$d/$g ] || continue
    gnutimeout 900 python3 bench/$d/$g >> "$L" 2>&1 || abort "bench/$d/$g failed"
  done
  [ -d bench/$d/subjects ] || abort "bench/$d/subjects missing"
done
python3 -m pcrecbench quiet --samples 5 --pin "$PIN" >> "$L" 2>&1; echo "quiet rc=$?" >> "$L"
DRV="build/work/pcrec-auto/pcrec_driver build/work/pcrec-nocaps/pcrec_driver"
drvsum() { for f in $DRV; do [ -f "$f" ] && sha256sum "$f"; done >> "$L" 2>&1; }
drvsum

export CELL_CAP_sentinel=3600 CELL_CAP_sentinel_end1=3600
export CELL_CAP_capability=5400 CELL_CAP_syntax=5400
SENTINEL=1 SUITE="capability syntax" SUITE_LOG="$W/suite.log" \
  TESTEES_sentinel="$R_SENT" TESTEES_capability="$R_CAP" TESTEES_syntax="$R_SYN" \
  NOTE="[B147] first window at 614d45eb3: capability I-154 tier + BEFORE @$B, syntax callout rows ($MACHINE_ID)" \
  STORE="$STORE" scripts/run_suite.sh >> "$L" 2>&1
rc=$?
SENTINEL=0 SUITE="sentinel:end1" SUITE_LOG="$W/suite_end.log" \
  TESTEES_sentinel_end1="$R_SENT" \
  NOTE="[B147] closing sentinel ($MACHINE_ID)" \
  STORE="$STORE" scripts/run_suite.sh >> "$L" 2>&1
echo "WINDOW_DONE suite_rc=$rc closing_rc=$? $(date -Is)" >> "$L"
drvsum
echo "CHAIN_DONE $(date -Is)" >> "$L"
