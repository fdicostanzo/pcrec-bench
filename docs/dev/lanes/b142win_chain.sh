#!/bin/bash
# [B142] FIRST WINDOW at 9ae59f5d4 (abi 84), PART 1 (the manager, 2026-10-25;
# Frank's go, live; cleared by pcrec_main the same morning). b142prep_report.md
# section 8 tier 1: I-154's owed capability re-run x {pcrec-auto, pcrec-nocaps}
# at the canonical pin AND at @6b2dbd3e (the same-window BEFORE, so the
# cross-pin Delta has a same-window partner), plus loglines x {auto,
# auto@6b2dbd3e}; opening + closing sentinel passes. Launch from the MAIN tree,
# detached:
#
#     MACHINE_ID=ryzen7700x setsid bash docs/dev/lanes/b142win_chain.sh > /dev/null 2>&1 &
#
# Completion: /var/tmp/pcrecbench/b142win/chain.log ends `CHAIN_DONE`;
# `CHAIN_ABORT` = nothing measured. Part 2 (the bench/subst cells + the BD16
# sentinel reads + the JIT-stack check) is a separate chain after the spread
# rule revision ([B144]) lands.
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b142win; mkdir -p "$W"
L=$W/chain.log
export PIN=${PIN:-7}
STORE=store
echo "CHAIN_START $(date -Is) PIN=$PIN MACHINE_ID=${MACHINE_ID:-<unset>}" >> "$L"
abort() { echo "CHAIN_ABORT $*" >> "$L"; exit 9; }
[ -n "${MACHINE_ID:-}" ] || abort "MACHINE_ID is not set; nothing measured"

B=6b2dbd3e
R_SENT="pcrec-auto pcrec-auto@$B pcrec-nocaps pcre2-jit"
R_CAP="pcrec-auto pcrec-nocaps pcrec-auto@$B pcrec-nocaps@$B"
R_LOG="pcrec-auto pcrec-auto@$B"

python3 -m pcrecbench testees 2>>"$L" | awk '{print $1}' > "$W/testees.names"
for t in $R_SENT $R_CAP $R_LOG; do
  grep -qx -- "${t%@*}" "$W/testees.names" || abort "testee '$t' does not resolve"
done
read -r HOSTN CPUSLUG NCORES < <(python3 -c "
import platform
from pcrecbench import env
print(platform.node() or 'unknown', env.canon_cpu_model(env.cpu_model_raw()), env.cores())")
python3 -m pcrecbench machines register --store "$STORE" --machine-id "$MACHINE_ID" \
    --hostname "$HOSTN" --cpu-model "$CPUSLUG" --cores "$NCORES" \
    --first-seen "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --note "[B142] b142win_chain.sh" >> "$L" 2>&1 \
  || abort "machines register ($MACHINE_ID $HOSTN) refused"
for s in 9ae59f5d4 $B; do
  sh testees/pcrec/pin.sh --path $s >> "$L" 2>&1 || abort "no build of $s"
done
for d in sentinel loglines capability; do
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
export CELL_CAP_loglines=3600 CELL_CAP_capability=5400
# pcrec-main 2026-10-25: part 1 must END by 20:00. No cell STARTS at or after
# STOP_AT (default 18:30 today): the longest cell (capability, ~55 min) plus
# the closing sentinel (~26 min) then ends by ~19:51.
STOP_AT_T1=${STOP_AT_T1:-"$(date +%F) 18:30"}
echo "STOP_AT=$STOP_AT_T1" >> "$L"
STOP_AT="$STOP_AT_T1" SENTINEL=1 SUITE="capability loglines" SUITE_LOG="$W/suite_t1.log" \
  TESTEES_sentinel="$R_SENT" TESTEES_capability="$R_CAP" TESTEES_loglines="$R_LOG" \
  NOTE="[B142] first window at 9ae59f5d4 part 1: capability I-154 re-run + loglines, BEFORE @$B ($MACHINE_ID)" \
  STORE="$STORE" scripts/run_suite.sh >> "$L" 2>&1
rc=$?
STOP_AT="" SENTINEL=0 SUITE="sentinel:end1" SUITE_LOG="$W/suite_t1_end.log" \
  TESTEES_sentinel_end1="$R_SENT" \
  NOTE="[B142] part 1 closing sentinel ($MACHINE_ID)" \
  STORE="$STORE" scripts/run_suite.sh >> "$L" 2>&1
echo "TIER1_DONE suite_rc=$rc closing_rc=$? $(date -Is)" >> "$L"
drvsum
echo "CHAIN_DONE $(date -Is)" >> "$L"
