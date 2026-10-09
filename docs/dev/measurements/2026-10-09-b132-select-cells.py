#!/usr/bin/env python3
"""[B132] cell selection: capability short-search cells, plain form, whose pcrec
program is IDENTICAL across c4c70f2c (capability@0.1 record) and 255bcdd8
(capability@0.2 record) by engine_metadata.program_sha256 (v2 normalization,
the record field), with the O-92 new/old ratio (common subjects, set-grain
reduction). Source records are the O-92 script's (2026-10-09-capability-xpin-
c4c70f2c-255bcdd8.py). Prints TSV: config pattern ratio overlap old_ns new_ns identical.
Run: python3 2026-10-09-b132-select-cells.py > cells.tsv
"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
MAIN = "/home/duxevents/pcrec-bench"
sys.path.insert(0, MAIN)
from pcrecbench import reduce as R
S = MAIN + "/store/"
pairs = {
 'pcrec-auto': ('records/capability@0.1/pcrec_c4c70f2c_auto-caps-simdna/capability@0.1__pcrec_c4c70f2c_auto-caps-simdna__budu-ryzen1600__20261005T042902Z.jsonl','records/capability@0.2/pcrec_255bcdd8_auto-caps-simdna/capability@0.2__pcrec_255bcdd8_auto-caps-simdna__budu-ryzen1600__20261008T160826Z.jsonl'),
 'pcrec-nocaps': ('records/capability@0.1/pcrec_c4c70f2c_auto-nocaps-simdna/capability@0.1__pcrec_c4c70f2c_auto-nocaps-simdna__budu-ryzen1600__20261005T053908Z.jsonl','records/capability@0.2/pcrec_255bcdd8_auto-nocaps-simdna/capability@0.2__pcrec_255bcdd8_auto-nocaps-simdna__budu-ryzen1600__20261008T170014Z.jsonl'),
}
def shas(path):
    out = {}
    for l in open(S + path):
        d = json.loads(l)
        if d.get('kind') == 'compile':
            out.setdefault(d['pattern_id'], set()).add(d.get('engine_metadata', {}).get('program_sha256'))
    return out
print("config\tpattern\tratio\toverlap\told_ns\tnew_ns\tidentical\tnshas")
for name, (a, b) in pairs.items():
    sa, sb = shas(a), shas(b)
    A = R.cells_from_record(R.read_record(S + a)[1]); B = R.cells_from_record(R.read_record(S + b)[1])
    for key in A:
        if key[1] != 'short-subject-search' or key[2] != 'plain' or key not in B: continue
        subs = [s for s in A[key] if s in B[key]]
        ca = R.reduce_set_cell({s: A[key][s] for s in subs}); cb = R.reduce_set_cell({s: B[key][s] for s in subs})
        if ca.median_ns is None or cb.median_ns is None: continue
        ident = sa.get(key[0]) == sb.get(key[0]) and None not in sa.get(key[0], {None})
        ov = not (cb.max_ns < ca.min_ns or cb.min_ns > ca.max_ns)
        print("%s\t%s\t%.4f\t%s\t%.1f\t%.1f\t%s\t%d" % (name, key[0], cb.median_ns/ca.median_ns, "overlap" if ov else "DISJOINT", ca.median_ns, cb.median_ns, ident, len(sb.get(key[0], ()))))
