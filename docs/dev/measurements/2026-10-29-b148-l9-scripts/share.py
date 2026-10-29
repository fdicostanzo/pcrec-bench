# [B148] L9 read (lane b148l9read, 2026-10-29): analysis helper over the SCRATCH store build/scratch-store/records/unusual@0.1; reads JSONL, no timing. Run: python3 -I is NOT used (imports its sibling).
import sys,statistics as st; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tab import *
W='/home/pcrec/projects/pcrec-bench/worktrees/b148l9read'
cal={}
for l in open(W+'/docs/dev/measurements/2026-10-28-b148l5-callout-calibration.txt'):
    if l.startswith('#') or l.startswith('testee'): continue
    p=l.rstrip('\n').split('\t'); cal[(p[0],p[1])]=float(p[4])
MAP=lambda t:('pcre2-interp' if 'interp' in t else 'pcre2-jit-deep' if ('jit' in t and 'lim-ceil1g' in t) else 'pcre2-jit' if 'jit' in t else 'pcrec-vm' if 'pcrec' in t and '_vm' in t else 'pcrec-auto' if 'pcrec' in t else 'onig-default' if 'onig' in t else None)
print('| testee | member | fires | calib ns/fire | L9 real (us) | share |'); print('|---|---|---|---|---|---|')
mem=[('co-luhn','co-luhn','co-luhn-1m'),('co-isbn','co-isbn','co-isbn-1m'),('co-member','co-member','co-member-1m'),('co-netstr-assist','co-netstr-assist','co-netstr-1m'),('co-netstr (native consume)','co-netstr','co-netstr-1m')]
for tid,rs in data.items():
    k=MAP(tid)
    if not k or 'assist-v01' in tid: continue
    for lab,p,s in mem:
        ck=(k,'co-netstr-assist' if p=='co-netstr-assist' else p)
        if p=='co-netstr' and 'pcrec' not in tid: continue
        xs=[];f=None
        for r in rs[1:]:
            if r['kind']=='match' and r['pattern_id']==p and r['subject_id']==s and r['regime']=='large-subject-throughput' and r['match_outcome']=='matched-as-expected':
                t=r['timing']; xs.append(t['elapsed_ns']/t['iterations']); f=(r.get('engine_metadata') or {}).get('callout_fires',f)
        if not xs or ck not in cal or not f: 
            if xs and f and ck not in cal: print('| %s | %s | %d | n/a | %.0f | - |'%(short(tid),lab,f,st.median(xs)/1e3))
            continue
        m=st.median(xs); sh=f*cal[ck]/m
        print('| %s | %s | %d | %.2f | %.0f | %.1f%%%s |'%(short(tid),lab,f,cal[ck],m/1e3,sh*100,' **FLAG**' if sh>0.4 or ('jit' in tid and 'pcre' in tid and sh>0.2) else ''))
