#!/bin/bash
# [B149] MONDAY 11-02 window: the tiers deferred from W1/W2 -- the manager, 2026-11-01. Runs after pcrec's pilot
# (790-797, ~01:00-05:30) and must be off the box before Frank's 20:00 hold. PINNED tier into store/.
#   0. the inline lane's CHECK CHAIN (b148inline2, make -k check + the inline checks) if its worktree carries one:
#      correctness only, before any timed cell; its rc is logged and never stops the window. (The inline arm
#      itself is NOT timed here: it is unmerged until that check is read.)
#   1. opening sentinel
#   2. unusual@0.1 -- the FIRST PINNED unusual records: pcrec-auto/vm at cb32eda28 and @614d45eb3 (the K134
#      give-up flips: 24 cscan + 8 + 3 FRAMES predicted to answer), then the five deep arms (BD17 --prime in
#      throughput) incl. pcre2-jit-deep on js-1m. CELL_CAP_unusual=7200 (L9: worst cell 3,009 s).
#   3. capability@0.4 x pcrec-auto-noedge (the noedge rows: base10num-noatomic/-grok, secrets-username-
#      password-pair) and syntax x {pcrec-auto, pcrec-nocaps, pcrec-auto-noedge} (cls-s-uc, cls-range).
#   4. closing sentinel
# Order = what a cut-off loses least of. DEADLINES: no main-suite SET or cell starts at or after STOP_MAIN
# (18:30), no closing-sentinel cell after STOP_END (19:15), every suite under a gnutimeout ending by
# HARD_END (19:40).
# Launch: a DELAYED SUBMISSION (no not_before route yet, O-115) of
#     scripts/boxq_window --name b149mon --prio 700 --cap S -- /var/tmp/pcrecbench/b149monwin/wrap.sh
# Completion: /var/tmp/pcrecbench/b149mon/chain.log ends `CHAIN_DONE`; `CHAIN_ABORT` = nothing measured.
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b149mon; mkdir -p "$W"
L=$W/chain.log
export PIN=${PIN:-7}
STORE=store
STOP_MAIN=${STOP_MAIN:-"2026-11-02 18:30"}
STOP_END=${STOP_END:-"2026-11-02 19:15"}
HARD_END=${HARD_END:-"2026-11-02 19:40"}
echo "CHAIN_START $(date -Is) PIN=$PIN MACHINE_ID=${MACHINE_ID:-<unset>}" >> "$L"
abort() { echo "CHAIN_ABORT $*" >> "$L"; exit 9; }
[ -n "${MACHINE_ID:-}" ] || abort "MACHINE_ID is not set; nothing measured"
left() { local s=$(( $(date -d "$HARD_END" +%s) - $(date +%s) )); [ "$s" -gt 0 ] && echo "$s" || echo 0; }

# 0. the inline lane's check chain (correctness; never fatal)
IC=worktrees/b148inline2/docs/dev/lanes/b148inline2_check.sh
if [ -x "$IC" ]; then
  echo "INLINE_CHECK_START $(date -Is)" >> "$L"
  gnutimeout -k 30 7200 "$IC" >> "$W/inline_check.out" 2>&1
  echo "INLINE_CHECK_DONE rc=$? $(date -Is) (the real rc is in /var/tmp/pcrecbench/b148inline2win/)" >> "$L"
else
  echo "INLINE_CHECK_SKIPPED: no executable $IC" >> "$L"
fi

B=614d45eb3
R_SENT="pcrec-auto pcrec-auto@$B pcrec-nocaps pcre2-jit"
R_UNU="pcrec-auto pcrec-vm pcrec-auto@$B pcrec-vm@$B pcre2-jit-deep pcrec-auto-deep pcrec-vm-deep pcre2-interp-deep onig-default-deep"
R_CAP="pcrec-auto-noedge"
R_SYN="pcrec-auto pcrec-nocaps pcrec-auto-noedge"

python3 -m pcrecbench testees 2>>"$L" | awk '{print $1}' > "$W/testees.names"
for t in $R_SENT $R_UNU $R_CAP $R_SYN; do
  grep -qx -- "${t%@*}" "$W/testees.names" || abort "testee '$t' does not resolve"
done
read -r HOSTN CPUSLUG NCORES < <(python3 -c "
import platform
from pcrecbench import env
print(platform.node() or 'unknown', env.canon_cpu_model(env.cpu_model_raw()), env.cores())")
python3 -m pcrecbench machines register --store "$STORE" --machine-id "$MACHINE_ID" \
    --hostname "$HOSTN" --cpu-model "$CPUSLUG" --cores "$NCORES" \
    --first-seen "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --note "[B149] b149mon_chain.sh" >> "$L" 2>&1 \
  || abort "machines register ($MACHINE_ID $HOSTN) refused"
for s in cb32eda28 $B; do
  sh testees/pcrec/pin.sh --path $s >> "$L" 2>&1 || abort "no build of $s"
done
for d in sentinel capability syntax unusual; do
  for g in gen_subjects.py gen_throughput_subjects.py gen_streams.py; do
    [ -f bench/$d/$g ] || continue
    gnutimeout 1800 python3 bench/$d/$g >> "$L" 2>&1 || abort "bench/$d/$g failed"
  done
  [ -d bench/$d/subjects ] || abort "bench/$d/subjects missing"
done
gnutimeout 1800 python3 -I bench/unusual/check_set.py >> "$L" 2>&1 || abort "bench/unusual/check_set.py failed"
python3 -m pcrecbench quiet --samples 5 --pin "$PIN" >> "$L" 2>&1; echo "quiet rc=$?" >> "$L"
DRV="build/work/pcrec-auto/pcrec_driver build/work/pcrec-nocaps/pcrec_driver"
drvsum() { for f in $DRV; do [ -f "$f" ] && sha256sum "$f"; done >> "$L" 2>&1; }
drvsum

export CELL_CAP_sentinel=3600 CELL_CAP_sentinel_end1=3600 CELL_CAP_unusual=7200
export CELL_CAP_capability=5400 CELL_CAP_syntax=5400
T=$(left); [ "$T" -gt 0 ] || abort "past HARD_END ($HARD_END) before the suite; nothing measured"
SENTINEL=1 SUITE="unusual capability syntax" SUITE_LOG="$W/suite.log" STOP_AT="$STOP_MAIN" \
  TESTEES_sentinel="$R_SENT" TESTEES_unusual="$R_UNU" TESTEES_capability="$R_CAP" TESTEES_syntax="$R_SYN" \
  NOTE="[B149] Monday deferred tiers at cb32eda28: unusual (K134 flips + deep arms), noedge ($MACHINE_ID)" \
  STORE="$STORE" gnutimeout -k 30 "$T" scripts/run_suite.sh >> "$L" 2>&1
rc=$?
T=$(left)
if [ "$T" -gt 60 ]; then
  SENTINEL=0 SUITE="sentinel:end1" SUITE_LOG="$W/suite_end.log" STOP_AT="$STOP_END" \
    TESTEES_sentinel_end1="$R_SENT" \
    NOTE="[B149] Monday closing sentinel ($MACHINE_ID)" \
    STORE="$STORE" gnutimeout -k 30 "$T" scripts/run_suite.sh >> "$L" 2>&1
  crc=$?
else
  crc=skipped; echo "closing sentinel SKIPPED: HARD_END near" >> "$L"
fi
echo "WINDOW_DONE suite_rc=$rc closing_rc=$crc $(date -Is)" >> "$L"
drvsum
echo "CHAIN_DONE $(date -Is)" >> "$L"
