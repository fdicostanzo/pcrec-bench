#!/bin/bash
# [B149] lane b149prep chain 4 (2026-10-30): check-unusual's `calls` section alone, after the
# K134 repair (pcrec-auto now ANSWERS the cscan-onig streams; the give-up naming moved to a
# 4-frame caller buffer; a flip row runs the also_pin 614d45eb3 as a child).
# Submit: setsid scripts/boxq_window --name b149prep-chk4 --prio 700 --cap 3600 -- <this file>
# Completion: /var/tmp/pcrecbench/b149prep/chain4.log ends `CHAIN4_DONE`.
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd) || exit 9
cd "$HERE" || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b149prep; mkdir -p "$W"
L=$W/chain4.log
echo "CHAIN4_START $(date -Is)" >> "$L"
gnutimeout 1800 python3 tools/check_unusual.py --only calls > "$W/check_unusual4.log" 2>&1
echo "CALLS rc=$?" >> "$L"
echo "CHAIN4_DONE $(date -Is)" >> "$L"
