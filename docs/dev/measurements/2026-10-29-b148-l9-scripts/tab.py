# [B148] L9 read (lane b148l9read, 2026-10-29): analysis helper over the SCRATCH store build/scratch-store/records/unusual@0.1; reads JSONL, no timing. Run: python3 -I is NOT used (imports its sibling).
import sys,json,collections,statistics as st; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from load import *
import re
SHORT={'cscan':'cscan'}
T={}  # tid-> (short name, hdr)
data={}
for d,rs in recs():
    h=rs[0]; tid=h['testee']['testee_id']; data[tid]=rs
def short(t):
    t=t.replace('_caps-simdna','').replace('_nocaps-simd','').replace('-simdna','')
    return t
def med(rs,pat,subj,reg):
    xs=[]; bp=None; out=collections.Counter(); fires=None
    for r in rs[1:]:
        if r['kind']=='match' and r['pattern_id']==pat and r['subject_id']==subj and r['regime']==reg:
            out[r['match_outcome']]+=1
            if r['match_outcome']=='matched-as-expected' and r.get('timing'):
                tm=r['timing']; xs.append(tm['elapsed_ns']/tm['iterations']); bp=tm['bytes_processed']/tm['iterations']
    return (st.median(xs) if xs else None, bp, dict(out))
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='thr':
        pat=sys.argv[2]; subs=sys.argv[3:]
        print('| testee | '+' | '.join(subs)+' |'); print('|---'*(len(subs)+1)+'|')
        for tid,rs in data.items():
            row=[]
            for s in subs:
                m,bp,o=med(rs,pat,s,'large-subject-throughput')
                if m is None:
                    k=[x for x in o if x!='matched-as-expected']
                    row.append(('-' if not o else '/'.join(k)) if o else 'n/a')
                else:
                    row.append('%.1f'%(bp/m*1000) )  # MB/s
            if any(x!='n/a' for x in row): print('| %s | '%short(tid)+' | '.join(row)+' |')
