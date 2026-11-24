#!/bin/bash
# [B152] lane b152prep (2026-11-23, inbox I-179): the SCRATCH correctness smoke at d6c5e71a5 (abi 112).
# One cell per (testee x set) the night window runs; --tier scratch --trials 1 --iters 1 --force-unquiet --synthetic,
# into a scratch store under /var/tmp. NOT timing (Frank's evening hold: light, nice'd prep only).
# Every pcrec/gcc process runs under `nice -n 19 taskset -c 0-5`, ONE cell at a time (one compile job).
# Completion: /var/tmp/pcrecbench/b152prep/smoke.log ends `SMOKE_DONE`.
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd) || exit 9
cd "$HERE" || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b152prep; ST=$W/store; mkdir -p "$ST"
L=$W/smoke.log
echo "SMOKE_START $(date -Is) in $HERE" >> "$L"
NR="nice -n 19 taskset -c 0-5"
for s in sentinel altwide capability syntax bounded utf8 loglines email litrun; do
  for g in bench/$s/gen_subjects.py bench/$s/gen_throughput_subjects.py; do
    [ -f "$g" ] || continue
    $NR gnutimeout 1800 python3 "$g" > "$W/gen_${s}_$(basename "$g" .py).log" 2>&1; echo "GEN $g rc=$?" >> "$L"
  done
done
CELLS="${CELLS:-sentinel:pcrec-auto altwide:pcrec-auto altwide:pcrec-vm capability:pcrec-auto syntax:pcrec-auto
bounded:pcrec-auto utf8:pcrec-auto-utf8 loglines:pcrec-auto email:pcrec-auto litrun:pcrec-auto sentinel:pcrec-auto@cb32eda28}"
MID=""; [ -f "$ST/machines.tsv" ] || MID="--machine-id ryzen7700x"
for c in $CELLS; do
  s=${c%%:*}; t=${c#*:}; pin=""
  case "$t" in *@*) pin=${t#*@}; t=${t%@*} ;; esac
  echo "CELL_START $s $t ${pin:-canonical} $(date -Is)" >> "$L"
  PCRECBENCH_PCREC_PIN=$pin $NR gnutimeout 5400 python3 -m pcrecbench run --subbench "$s" --testee "$t" \
     --tier scratch --store "$ST" --trials 1 --iters 1 --force-unquiet --synthetic $MID \
     --note "b152prep correctness smoke (not a measurement)" > "$W/cell_${s}_${t}${pin:+@$pin}.log" 2>&1
  echo "CELL_END $s $t ${pin:-canonical} rc=$? $(date -Is)" >> "$L"
  MID=""
done
python3 -m pcrecbench index --store "$ST" > "$W/index.log" 2>&1; echo "INDEX rc=$?" >> "$L"
echo "SMOKE_DONE $(date -Is)" >> "$L"
