# [B148] L9 read (lane b148l9read, 2026-10-29): analysis helper over the SCRATCH store build/scratch-store/records/unusual@0.1; reads JSONL, no timing. Run: python3 -I is NOT used (imports its sibling).
import sys,json,collections,statistics as st; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from load import *
for d,rs in recs():
    h=rs[0]; tid=h['testee']['testee_id']
    g=collections.defaultdict(list)
    for r in rs[1:]:
        if r['kind']=='match' and r['match_outcome']!='matched-as-expected':
            g[(r['pattern_id'],r['regime'],r['subject_id'],r['match_outcome'],(r.get('diagnostic') or '')[:50])].append(r['trial'])
    if not g: continue
    print('=====',tid,h['status'])
    # compress by pattern/regime/outcome/diag: list of subjects
    c=collections.defaultdict(list)
    for (p,rg,s,o,dg),t in g.items(): c[(p,rg,o,dg)].append((s,len(t)))
    for k,v in sorted(c.items()):
        print('  ',k, 'n=%d'%len(v), [x[0] if x[1]==5 else '%s(%dt)'%x for x in v][:40])
