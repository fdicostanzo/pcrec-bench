#!/bin/bash
# [B135] STATE 3 chain (lane b135s3, NOT RUN): pcrec b8337c33 (abi 74,
# [START-LANDING]) against 7388f1c0 (abi 73, state 2) REPEATED as the
# cross-window control. Same four sets as the states 1+2 chain
# (/var/tmp/b135win/chain.sh), sentinel first and last. Launch from the MAIN
# tree AFTER the b135s3 merge, detached:
#
#     setsid bash docs/dev/lanes/b135s3_chain.sh > /dev/null 2>&1 &
#
# Completion: /var/tmp/b135win3/chain.log ends `CHAIN_DONE suite_rc=0`; the
# suite log (build/windows/suite_*.log) ends SUITE_RUN_COMPLETE with, per set,
# `set <name> rc=0 <min> min`; each set's own window log ends
# `WINDOW_RUN_COMPLETE cells=N/N` (expect 5/5 4/4 4/4 4/4 4/4 5/5 = 26 cells).
# `rc=4` (inconclusive-spread) cells are re-measured once by run_window.sh.
#
# ABBA within a set: control(7388f1c0)  new(b8337c33) | new-nocaps
# control-nocaps. Do NOT set PIN (that is the CPU core) nor
# PCRECBENCH_PCREC_PIN (run_window.sh sets it per `testee@pin` cell).
# The bare `pcrec-auto` / `pcrec-nocaps` run at the canonical pin b8337c33;
# `@7388f1c0` is the repeated state-2 pin (testee ids
# pcrec_7388f1c0_auto-{caps,nocaps}-simdna: the SAME ids as the states 1+2
# window's records, so the store holds the state-2 cell twice, one per window).
cd /home/duxevents/pcrec-bench || exit 9
W=/var/tmp/b135win3; mkdir -p $W
L=$W/chain.log
echo "CHAIN_START $(date -Is)" >> $L
# --- preconditions (a failure here aborts: nothing has been measured) ---
for s in 7388f1c0 b8337c33; do
  sh testees/pcrec/pin.sh --path $s >> $L 2>&1 || { echo "CHAIN_ABORT no build of $s" >> $L; exit 9; }
done
python3 bench/sentinel/gen_subjects.py >> $L 2>&1; echo "gen_sentinel rc=$?" >> $L
python3 -m pcrecbench quiet --samples 5 >> $L 2>&1; echo "quiet rc=$?" >> $L
# --- OPTIONAL instrument A/B/A/B (RUN_AB=1; ~35 min, measured 12:13-12:48
# at the states 1+2 chain). OFF by default: driver.c/shim.c/timed.* at this
# merge are byte-identical to master's (git diff empty), so the A/B would
# time identical sources; the sentinel set below, first and last, is the
# instrument control. If run, BEFORE_REV is master's tip at launch.
if [ "${RUN_AB:-0}" = 1 ]; then
  /usr/bin/gnutimeout 7200 scripts/instrument_ab.sh "${AB_REV:?AB_REV=<master tip at launch>}" $W/ab scripts/instrument_cells.txt >> $L 2>&1
  echo "AB_DONE rc=$? $(date -Is)" >> $L
fi
# --- the window ---
# one driver build for all four testee entries (the workdir carries no pin):
#   sha256sum build/work/pcrec-auto/pcrec_driver build/work/pcrec-nocaps/pcrec_driver
# must be equal and unchanged between the first sentinel cell and the end.
SUITE="sentinel capability loglines altwide email litrun sentinel:end" \
TESTEES_sentinel="pcrec-auto@7388f1c0 pcrec-auto pcrec-nocaps pcrec-nocaps@7388f1c0 pcre2-jit" \
TESTEES_sentinel_end="pcrec-auto pcrec-auto@7388f1c0 pcrec-nocaps@7388f1c0 pcrec-nocaps pcre2-jit" \
TESTEES_capability="pcrec-auto@7388f1c0 pcrec-auto pcrec-nocaps pcrec-nocaps@7388f1c0" \
TESTEES_loglines="pcrec-auto@7388f1c0 pcrec-auto pcrec-nocaps pcrec-nocaps@7388f1c0" \
# altwide@0.3 (the set is at 0.3 now): pcrecdev1 [ENG-TACTICS] needs sfx-* at b8337c33. SAME-PIN read, so
# the control arm is OFF by default (add pcrec-auto@7388f1c0 pcrec-nocaps@7388f1c0 for +36 min). The harness
# has no per-pattern filter on `run`, so the whole set runs (sfx-64/256/512 are in it).
TESTEES_altwide="pcrec-auto pcrec-nocaps" \
TESTEES_email="pcrec-auto@7388f1c0 pcrec-auto pcrec-nocaps pcrec-nocaps@7388f1c0" \
TESTEES_litrun="pcrec-auto@7388f1c0 pcrec-auto pcrec-nocaps pcrec-nocaps@7388f1c0" \
NOTE="[B135] START-LANDING state 3: b8337c33 (abi 74) vs 7388f1c0 (abi 73) repeated as the cross-window control" \
scripts/run_suite.sh >> $L 2>&1
echo "CHAIN_DONE suite_rc=$? $(date -Is)" >> $L
