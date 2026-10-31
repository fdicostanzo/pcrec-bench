#!/bin/bash
# [B149] lane b149prep chain 1 (2026-10-30): build the cb32eda28 pin, dump its registry surfaces
# raw, run the compile-only census (614d45eb3 vs cb32eda28 + two deny arms), classify it.
# No timing; heavy (a ~1 min build + ~1,500 rows x 4 compiles). Submitted through the box queue:
#
#     setsid scripts/boxq_window --name b149prep --prio 740 --cap 7200 -- \
#         /home/pcrec/projects/pcrec-bench/worktrees/b149prep/docs/dev/lanes/b149prep_chain.sh
#
# Completion: /var/tmp/pcrecbench/b149prep/chain.log ends `CHAIN_DONE rc=<n>`.
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd) || exit 9
cd "$HERE" || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b149prep; mkdir -p "$W/reg"
L=$W/chain.log
echo "CHAIN_START $(date -Is) in $HERE" >> "$L"
NEW=cb32eda28; OLD=614d45eb3
BR=/home/pcrec/projects/pcrec-bench/build
sh testees/pcrec/pin.sh "$NEW" >> "$L" 2>&1 || { echo "CHAIN_DONE rc=11 build" >> "$L"; exit 11; }
[ -x "$BR/pcrec-$OLD/build/pcrec" ] || { echo "CHAIN_DONE rc=12 no $OLD build" >> "$L"; exit 12; }
B=$BR/pcrec-$NEW/build/pcrec
for q in axes definitions limits schema callouts syntax; do
  gnutimeout 300 "$B" --list-$q > "$W/reg/list_$q.raw" 2> "$W/reg/list_$q.err"; echo "list-$q rc=$?" >> "$L"
done
gnutimeout 60 "$B" --version > "$W/reg/version.txt" 2>&1
gnutimeout 120 "$B" -p rx --features all -o "$W/abc.c" --pattern abc >> "$L" 2>&1; echo "abc-witness rc=$?" >> "$L"
grep -m3 -E "RX_ABI|PCREC_RX_ABI_H" "$W/abc.h" >> "$L" 2>&1
B149_JOBS=6 gnutimeout 6000 python3 docs/dev/measurements/probe_b149prep_emit.py "$W/emit" >> "$L" 2>&1
echo "EMIT rc=$?" >> "$L"
gnutimeout 1800 python3 docs/dev/measurements/probe_b149prep_census.py "$W/emit" "$W/census.tsv" >> "$L" 2>&1
echo "CENSUS rc=$?" >> "$L"
gnutimeout 600 python3 docs/dev/measurements/probe_b149prep_summary.py "$W/emit" "$W/census.tsv" > "$W/census_summary.txt" 2>> "$L"
echo "SUMMARY rc=$?" >> "$L"
echo "CHAIN_DONE rc=0 $(date -Is)" >> "$L"
