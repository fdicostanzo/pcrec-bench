#!/bin/bash
# [B149] lane b149prep chain 2 (2026-10-30): the targeted checks at cb32eda28 (no timing).
#   1. the named selfcheck slice (docs/dev/lanes/b149prep_checks.py)
#   2. make check-unusual   3. sidecar regeneration + make check-interpret
# Submit: setsid scripts/boxq_window --name b149prep-chk --prio 740 --cap 7200 -- <this file>
# Completion: /var/tmp/pcrecbench/b149prep/chain2.log ends `CHAIN2_DONE`.
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd) || exit 9
cd "$HERE" || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b149prep; mkdir -p "$W"
L=$W/chain2.log
echo "CHAIN2_START $(date -Is)" >> "$L"
gnutimeout 900 python3 bench/email/gen_subjects.py >> "$L" 2>&1
gnutimeout 900 python3 bench/email/gen_throughput_subjects.py >> "$L" 2>&1
gnutimeout 3000 python3 docs/dev/lanes/b149prep_checks.py > "$W/checks.log" 2>&1
echo "SELFCHECK_SLICE rc=$?" >> "$L"
gnutimeout 2400 make check-unusual > "$W/check_unusual.log" 2>&1
echo "CHECK_UNUSUAL rc=$?" >> "$L"
gnutimeout 1200 python3 scripts/regen_sidecars.py > "$W/regen_sidecars.log" 2>&1
echo "REGEN_SIDECARS rc=$?" >> "$L"
gnutimeout 900 make check-interpret > "$W/check_interpret.log" 2>&1
echo "CHECK_INTERPRET rc=$?" >> "$L"
echo "CHAIN2_DONE $(date -Is)" >> "$L"
