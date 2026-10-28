#!/bin/bash
# [B148] L9 -- the unusual@0.1 SCRATCH READOUT window (the manager, 2026-10-28;
# Frank's go, live; pcrec_main ordered it after the [B147] window). SCRATCH
# tier into build/scratch-store (never store/), five trials, quiet gate as for a
# window, pcrec at the canonical pin 614d45eb3. Two purposes: the first readout
# of the set (native vs deep vs assisted, unusual_set_v1.md 7.5 / NOTES.md R0-R5)
# and the PER-CELL WALL TIMES that size CELL_CAP_unusual (b148l4_report.md 4's
# table was lost). Order = what a cut-off loses least of: the five assisted
# arms, then the native arms, then the deep arms, then tre. Launched through
# the box queue:
#
#     setsid scripts/boxq_window --name b148l9 --prio 7NN --cap S -- \
#         env MACHINE_ID=ryzen7700x bash docs/dev/lanes/b148l9_chain.sh
#
# Completion: /var/tmp/pcrecbench/b148l9win/chain.log ends `CHAIN_DONE`;
# per-cell walls are the `attempt N rc=` lines of the set's window log.
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b148l9win; mkdir -p "$W"
L=$W/chain.log
export PIN=${PIN:-7}
STORE=build/scratch-store
echo "CHAIN_START $(date -Is) PIN=$PIN MACHINE_ID=${MACHINE_ID:-<unset>}" >> "$L"
abort() { echo "CHAIN_ABORT $*" >> "$L"; exit 9; }
[ -n "${MACHINE_ID:-}" ] || abort "MACHINE_ID is not set; nothing measured"

R_ASSIST="pcre2-jit-assist-v01 onig-default-assist-v01 re2-default-assist-v01 rust-default-assist-v01 vectorscan-block-som-assist-v01"
R_NATIVE="pcre2-jit pcre2-interp pcrec-auto pcrec-vm onig-default re2-default rust-default vectorscan-block-som"
R_DEEP="pcre2-jit-deep pcre2-interp-deep pcrec-auto-deep pcrec-vm-deep onig-default-deep"
R_LAST="tre-default"
ROSTER="$R_ASSIST $R_NATIVE $R_DEEP $R_LAST"

python3 -m pcrecbench testees 2>>"$L" | awk '{print $1}' > "$W/testees.names"
for t in $ROSTER; do
  grep -qx -- "$t" "$W/testees.names" || abort "testee '$t' does not resolve"
done
read -r HOSTN CPUSLUG NCORES < <(python3 -c "
import platform
from pcrecbench import env
print(platform.node() or 'unknown', env.canon_cpu_model(env.cpu_model_raw()), env.cores())")
python3 -m pcrecbench machines register --store "$STORE" --machine-id "$MACHINE_ID" \
    --hostname "$HOSTN" --cpu-model "$CPUSLUG" --cores "$NCORES" \
    --first-seen "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --note "[B148] b148l9_chain.sh" >> "$L" 2>&1 \
  || echo "machines register on the scratch store refused or already present (continuing)" >> "$L"
sh testees/pcrec/pin.sh --path 614d45eb3 >> "$L" 2>&1 || abort "no build of 614d45eb3"
for g in gen_subjects.py gen_throughput_subjects.py gen_streams.py; do
  gnutimeout 1800 python3 bench/unusual/$g >> "$L" 2>&1 || abort "bench/unusual/$g failed"
done
gnutimeout 1800 python3 -I bench/unusual/check_set.py >> "$L" 2>&1 || abort "bench/unusual/check_set.py failed"
python3 -m pcrecbench quiet --samples 5 --pin "$PIN" >> "$L" 2>&1; echo "quiet rc=$?" >> "$L"

SUBBENCH=unusual TESTEES="$ROSTER" CELL_CAP=5400 TRIALS=5 EXTRA="--tier scratch" \
  STORE="$STORE" LOG="$W/window_unusual.log" \
  NOTE="[B148] L9 unusual@0.1 scratch readout at 614d45eb3 ($MACHINE_ID)" \
  scripts/run_window.sh >> "$L" 2>&1
echo "WINDOW_DONE rc=$? $(date -Is)" >> "$L"
echo "CHAIN_DONE $(date -Is)" >> "$L"
