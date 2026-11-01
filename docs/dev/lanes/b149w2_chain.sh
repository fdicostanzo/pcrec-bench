#!/bin/bash
# [B149] W2 = the FIRST WINDOW at cb32eda28 (abi 93) -- the manager, 2026-11-01. W1 (Sat 10-31) did
# not run: no chain had been written. This window carries W1's first tier instead. Copied from
# b147win_chain.sh (proven 2026-10-28, 7.0 h): opening sentinel, capability@0.4 (incl. the I-172 cells
# t-qs-1m / t-qs-nearmiss-256k) x {pcrec-auto, pcrec-nocaps} at the canonical pin AND at @614d45eb3 (the
# same-window BEFORE for the cross-pin Delta), closing sentinel. Deferred to Mon 01:00+: the inline arm
# (part 2 not built), the unusual deep arms, noedge, syntax.
#
# HARD END (Frank holds the box Sun 18:00-Mon 01:00): no capability cell starts at or after STOP_MAIN
# (16:45); the closing sentinel starts no cell after STOP_END (17:25); every suite runs under a
# gnutimeout that ends it by HARD_END (17:50) whatever the queue cap says.
#
# Launch (executable wrapper; boxq_window refuses `env ...`):
#     setsid scripts/boxq_window --name b149w2 --prio 700 --cap S -- /var/tmp/pcrecbench/b149w2win/wrap.sh
# Rehearsal: DRYRUN=1 (one synthetic pass into a scratch store, no deadlines).
# Completion: /var/tmp/pcrecbench/b149w2/chain.log ends `CHAIN_DONE`; `CHAIN_ABORT` = nothing measured.
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b149w2; mkdir -p "$W"
L=$W/chain.log
export PIN=${PIN:-7}
DRY=${DRYRUN:-0}
STORE=store; DRYARG=
if [ "$DRY" = 1 ]; then STORE=$W/dry-store; DRYARG=--dry-run; mkdir -p "$STORE"; fi
STOP_MAIN=${STOP_MAIN:-"2026-11-01 16:45"}
STOP_END=${STOP_END:-"2026-11-01 17:25"}
HARD_END=${HARD_END:-"2026-11-01 17:50"}
echo "CHAIN_START $(date -Is) PIN=$PIN MACHINE_ID=${MACHINE_ID:-<unset>} DRYRUN=$DRY" >> "$L"
abort() { echo "CHAIN_ABORT $*" >> "$L"; exit 9; }
[ -n "${MACHINE_ID:-}" ] || abort "MACHINE_ID is not set; nothing measured"
left() { local s=$(( $(date -d "$HARD_END" +%s) - $(date +%s) )); [ "$s" -gt 0 ] && echo "$s" || echo 0; }

B=614d45eb3
R_SENT="pcrec-auto pcrec-auto@$B pcrec-nocaps pcre2-jit"
R_CAP="pcrec-auto pcrec-nocaps pcrec-auto@$B pcrec-nocaps@$B"

python3 -m pcrecbench testees 2>>"$L" | awk '{print $1}' > "$W/testees.names"
for t in $R_SENT $R_CAP; do
  grep -qx -- "${t%@*}" "$W/testees.names" || abort "testee '$t' does not resolve"
done
read -r HOSTN CPUSLUG NCORES < <(python3 -c "
import platform
from pcrecbench import env
print(platform.node() or 'unknown', env.canon_cpu_model(env.cpu_model_raw()), env.cores())")
python3 -m pcrecbench machines register --store "$STORE" --machine-id "$MACHINE_ID" \
    --hostname "$HOSTN" --cpu-model "$CPUSLUG" --cores "$NCORES" \
    --first-seen "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --note "[B149] b149w2_chain.sh" >> "$L" 2>&1 \
  || abort "machines register ($MACHINE_ID $HOSTN) refused"
for s in cb32eda28 $B; do
  sh testees/pcrec/pin.sh --path $s >> "$L" 2>&1 || abort "no build of $s"
done
for d in sentinel capability; do
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

export CELL_CAP_sentinel=3600 CELL_CAP_sentinel_end1=3600 CELL_CAP_capability=5400
if [ "$DRY" = 1 ]; then SM=; SE=; T=86400; else SM=$STOP_MAIN; SE=$STOP_END; T=$(left); fi
[ "$T" -gt 0 ] || abort "past HARD_END ($HARD_END) before the suite; nothing measured"
SENTINEL=1 SUITE="capability" SUITE_LOG="$W/suite.log" STOP_AT="$SM" \
  TESTEES_sentinel="$R_SENT" TESTEES_capability="$R_CAP" \
  NOTE="[B149] first window at cb32eda28: capability@0.4 + BEFORE @$B ($MACHINE_ID)" \
  STORE="$STORE" gnutimeout -k 30 "$T" scripts/run_suite.sh $DRYARG >> "$L" 2>&1
rc=$?
[ "$DRY" = 1 ] || T=$(left)
if [ "$T" -gt 60 ]; then
  SENTINEL=0 SUITE="sentinel:end1" SUITE_LOG="$W/suite_end.log" STOP_AT="$SE" \
    TESTEES_sentinel_end1="$R_SENT" \
    NOTE="[B149] closing sentinel ($MACHINE_ID)" \
    STORE="$STORE" gnutimeout -k 30 "$T" scripts/run_suite.sh $DRYARG >> "$L" 2>&1
  crc=$?
else
  crc=skipped; echo "closing sentinel SKIPPED: HARD_END near" >> "$L"
fi
echo "WINDOW_DONE suite_rc=$rc closing_rc=$crc $(date -Is)" >> "$L"
drvsum
echo "CHAIN_DONE $(date -Is)" >> "$L"
