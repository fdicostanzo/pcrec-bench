#!/bin/bash
# [B149] lane b149prep chain 3 (2026-10-30): the targeted checks again after the repairs.
# Chain 2's check-unusual and noedge reds were MISSING GENERATED SUBJECT TREES in a fresh worktree,
# so this chain generates them first (the harness's `make check` does the same).
# Submit: setsid scripts/boxq_window --name b149prep-chk3 --prio 700 --cap 7200 -- <this file>
# Completion: /var/tmp/pcrecbench/b149prep/chain3.log ends `CHAIN3_DONE`.
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd) || exit 9
cd "$HERE" || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b149prep; mkdir -p "$W"
L=$W/chain3.log
echo "CHAIN3_START $(date -Is)" >> "$L"
for g in bench/email/gen_subjects.py bench/email/gen_throughput_subjects.py \
         bench/loglines/gen_subjects.py bench/loglines/gen_throughput_subjects.py \
         bench/unusual/gen_subjects.py bench/unusual/gen_throughput_subjects.py bench/unusual/gen_streams.py; do
  [ -f "$g" ] || { echo "no generator $g" >> "$L"; continue; }
  gnutimeout 1800 python3 "$g" >> "$L" 2>&1; echo "GEN $g rc=$?" >> "$L"
done
gnutimeout 3300 python3 docs/dev/lanes/b149prep_checks.py > "$W/checks3.log" 2>&1
echo "SELFCHECK_SLICE rc=$?" >> "$L"
gnutimeout 2400 make check-unusual > "$W/check_unusual3.log" 2>&1
echo "CHECK_UNUSUAL rc=$?" >> "$L"
echo "CHAIN3_DONE $(date -Is)" >> "$L"
