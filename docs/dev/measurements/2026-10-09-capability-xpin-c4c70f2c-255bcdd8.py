import sys, statistics
sys.path.insert(0, '/home/duxevents/pcrec-bench')
from pcrecbench import reduce as R
S='/home/duxevents/pcrec-bench/store/'
pairs={
 'pcrec-auto (caps)':('records/capability@0.1/pcrec_c4c70f2c_auto-caps-simdna/capability@0.1__pcrec_c4c70f2c_auto-caps-simdna__budu-ryzen1600__20261005T042902Z.jsonl','records/capability@0.2/pcrec_255bcdd8_auto-caps-simdna/capability@0.2__pcrec_255bcdd8_auto-caps-simdna__budu-ryzen1600__20261008T160826Z.jsonl'),
 'pcrec-auto-nocaps':('records/capability@0.1/pcrec_c4c70f2c_auto-nocaps-simdna/capability@0.1__pcrec_c4c70f2c_auto-nocaps-simdna__budu-ryzen1600__20261005T053908Z.jsonl','records/capability@0.2/pcrec_255bcdd8_auto-nocaps-simdna/capability@0.2__pcrec_255bcdd8_auto-nocaps-simdna__budu-ryzen1600__20261008T170014Z.jsonl'),
 'CONTROL pcre2-jit':('records/capability@0.1/libpcre2_10.46_jit-caps-simdna/capability@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260917T013333Z.jsonl','records/capability@0.2/libpcre2_10.46_jit-caps-simdna/capability@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20261008T220359Z.jsonl'),
}
def cells(path):
    setup, rows = R.read_record(S+path)
    return R.cells_from_record(rows)
for name,(a,b) in pairs.items():
    A=cells(a); B=cells(b)
    res=[]
    for key in A:
        if key[2]!='plain' or key not in B: continue
        subs=[s for s in A[key] if s in B[key]]
        if not subs: continue
        ca=R.reduce_set_cell({s:A[key][s] for s in subs}); cb=R.reduce_set_cell({s:B[key][s] for s in subs})
        if ca.median_ns is None or cb.median_ns is None:
            res.append((key, None, None, ca.median_ns is None, cb.median_ns is None)); continue
        r=cb.median_ns/ca.median_ns
        overlap = not (cb.max_ns < ca.min_ns or cb.min_ns > ca.max_ns)
        res.append((key, r, overlap, ca.median_ns, cb.median_ns))
    num=[x for x in res if x[1] is not None]
    print(f"== {name}: {len(num)} comparable cells (common subjects only), {len(res)-len(num)} without a number on one side")
    for rg in ('short-subject-search','large-subject-throughput'):
        sel=[x for x in num if x[0][1]==rg]
        if not sel: continue
        rs=[x[1] for x in sel]
        faster=[x for x in sel if not x[2] and x[1]<1]; slower=[x for x in sel if not x[2] and x[1]>1]
        gm=statistics.geometric_mean(rs)
        print(f"  {rg}: n={len(sel)} median new/old={statistics.median(rs):.3f} geomean={gm:.3f} | moved faster (ranges disjoint)={len(faster)} slower={len(slower)} within-noise={len(sel)-len(faster)-len(slower)}")
        for x in sorted(faster,key=lambda x:x[1])[:6]: print(f"     faster {x[0][0]:45s} x{x[1]:.3f}  {x[3]:.0f} -> {x[4]:.0f} ns")
        for x in sorted(slower,key=lambda x:-x[1])[:6]: print(f"     slower {x[0][0]:45s} x{x[1]:.3f}  {x[3]:.0f} -> {x[4]:.0f} ns")
    for x in res:
        if x[1] is None: print(f"  no-number: {x[0][0]} {x[0][1]} old_missing={x[3]} new_missing={x[4]}")
