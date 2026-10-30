#!/bin/bash
# [B148] L9 RE-RUN -- the manager, 2026-10-29; Frank's go ("you might be able to
# slip in the rerun"), slot 19:30-00:00 from pcrec_main, before their suite
# 300-main-fullsuite (not-before 2026-10-30T00:00). Re-measures the 7 unusual@0.1
# cells L9 read `inconclusive-load` (ledger 2026-10-29-unusual-0.1-l9-scratch.md
# 1(b)), plus the owed quiet-box callee-share calibration (tools/callout_calib.py).
# SCRATCH tier into build/scratch-store, five trials, pcrec 614d45eb3, as L9.
# Walls at L9 sum to 11,043 s (3.07 h); per-cell cap 7200 (the L9 read's proposal).
# Order: the calibration (minutes), then the short cells, then the long ones, so
# a cut-off loses the least. Launched through the box queue, submitted at 19:30
# (the .window format has no not-before key, so the submission itself waits):
#
#     setsid scripts/boxq_window --name b148l9r --prio 720 --cap 15600 -- \
#         /var/tmp/pcrecbench/b148l9rwin/chain_wrap.sh
#
# (CORRECTED 2026-10-30: the line first written here, `-- env MACHINE_ID=... bash
# <chain>`, FAILS -- boxq_window requires CHAIN to be an executable path ("chain not
# executable: env"). The run used a wrapper that cd's to the repo, exports
# MACHINE_ID=ryzen7700x and execs this file.)
#
# Completion: /var/tmp/pcrecbench/b148l9rwin/chain.log ends `CHAIN_DONE`.
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b148l9rwin; mkdir -p "$W"
L=$W/chain.log
export PIN=${PIN:-7}
STORE=build/scratch-store
echo "CHAIN_START $(date -Is) PIN=$PIN MACHINE_ID=${MACHINE_ID:-<unset>}" >> "$L"
abort() { echo "CHAIN_ABORT $*" >> "$L"; exit 9; }
[ -n "${MACHINE_ID:-}" ] || abort "MACHINE_ID is not set; nothing measured"

ROSTER="rust-default onig-default-assist-v01 rust-default-assist-v01 pcrec-auto onig-default-deep pcre2-interp-deep pcre2-interp"

python3 -m pcrecbench testees 2>>"$L" | awk '{print $1}' > "$W/testees.names"
for t in $ROSTER; do
  grep -qx -- "$t" "$W/testees.names" || abort "testee '$t' does not resolve"
done
sh testees/pcrec/pin.sh --path 614d45eb3 >> "$L" 2>&1 || abort "no build of 614d45eb3"
for g in gen_subjects.py gen_throughput_subjects.py gen_streams.py; do
  gnutimeout 1800 python3 bench/unusual/$g >> "$L" 2>&1 || abort "bench/unusual/$g failed"
done
gnutimeout 1800 python3 -I bench/unusual/check_set.py >> "$L" 2>&1 || abort "bench/unusual/check_set.py failed"
python3 -m pcrecbench quiet --samples 5 --pin "$PIN" >> "$L" 2>&1; echo "quiet rc=$?" >> "$L"

echo "CALIB_START $(date -Is) load $(cat /proc/loadavg)" >> "$L"
gnutimeout 1200 python3 tools/callout_calib.py --cpu "$PIN" > "$W/callout_calib.txt" 2>> "$L"
echo "CALIB_DONE rc=$? $(date -Is)" >> "$L"

SUBBENCH=unusual TESTEES="$ROSTER" CELL_CAP=7200 TRIALS=5 EXTRA="--tier scratch" \
  STORE="$STORE" LOG="$W/window_unusual.log" \
  NOTE="[B148] L9 re-run of the 7 inconclusive-load cells at 614d45eb3 ($MACHINE_ID)" \
  scripts/run_window.sh >> "$L" 2>&1
echo "WINDOW_DONE rc=$? $(date -Is)" >> "$L"
echo "CHAIN_DONE $(date -Is)" >> "$L"
