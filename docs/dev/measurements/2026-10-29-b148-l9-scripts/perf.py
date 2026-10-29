# [B148] L9 read (lane b148l9read, 2026-10-29): analysis helper over the SCRATCH store build/scratch-store/records/unusual@0.1; reads JSONL, no timing. Run: python3 -I is NOT used (imports its sibling).
import sys,json,collections,statistics as st; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tab import *
HEAD={'cscan-onig':'comment-5m','cscan':'comment-5m','wild-sexp-balanced':'sx-1m','wild-json-validate-onig':'js-1m','wild-json-validate':'js-1m','co-luhn':'co-luhn-1m','co-isbn':'co-isbn-1m','co-member':'co-member-1m','co-netstr':'co-netstr-1m','co-netstr-assist':'co-netstr-1m'}
def run(rs,pat):
    per=collections.defaultdict(lambda:collections.defaultdict(list)); bad=collections.Counter()
    for r in rs[1:]:
        if r['kind']=='match' and r['pattern_id']==pat and r['regime'] in('short-subject-search','large-subject-throughput'):
            if r['match_outcome']=='matched-as-expected' and r.get('timing'):
                t=r['timing']; per[r['regime']][r['subject_id']].append((t['elapsed_ns']/t['iterations'],t['bytes_processed']/t['iterations']))
            else: bad[r['regime']]+=1
    sh=[st.median(x[0] for x in v) for v in per['short-subject-search'].values()]
    thr=per['large-subject-throughput'].get(HEAD[pat])
    mbs=None
    if thr: m=st.median(x[0] for x in thr); mbs=thr[0][1]/m*1000
    return (st.mean(sh) if sh else None, len(sh), mbs)
for pat in HEAD:
    print('###',pat,'(short: mean ns/call over n subjects; headline',HEAD[pat],'MB/s)')
    for tid,rs in data.items():
        if not any(r['kind']=='compile' and r['pattern_id']==pat and r['compile_outcome']=='compiled' for r in rs[1:]): continue
        m,n,mb=run(rs,pat)
        print('  %-52s short %s (n=%d)  head %s'%(short(tid),'%.0f ns'%m if m else '-',n,'%.1f MB/s'%mb if mb else '-'))
