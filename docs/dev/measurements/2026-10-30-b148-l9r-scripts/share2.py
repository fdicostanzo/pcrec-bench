# [B148] L9 re-run read (lane b148l9rread): callee share = fires x calibrated ns/fire / measured real time on 1 MB. Three columns: L9's (old calibration x L9 record), NEW calibration x the LATEST record (rerun where one exists), and the calibration's own share column. Run: python3 share2.py
import sys,os,statistics as st; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.argv=['x','none']
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cmp.py')).read().split("mode=sys.argv")[0])
M2='/home/pcrec/projects/pcrec-bench/worktrees/b148l9rread/docs/dev/measurements/'
def load(p):
    c={}
    for l in open(p):
        if l.startswith('#') or l.startswith('testee'): continue
        x=l.rstrip('\n').split('\t'); c[(x[0],x[1])]=(float(x[4]),float(x[9]) if x[9]!='-' else None,x[12] if len(x)>12 else '')
    return c
old=load(M2+'2026-10-28-b148l5-callout-calibration.txt'); new=load(M2+'2026-10-29-b148-l9r-callout-calib.txt')
MAP=lambda t:('pcre2-interp' if 'interp' in t and 'lim' not in t else 'pcre2-interp-deep' if 'interp' in t else 'pcre2-jit-deep' if ('jit' in t and 'lim-ceil1g' in t) else 'pcre2-jit' if 'jit' in t else 'pcrec-vm' if 'pcrec' in t and '_vm' in t else 'pcrec-auto' if 'pcrec' in t else 'onig-default' if 'onig' in t and 'lim' not in t else None)
allrecs=collections.defaultdict(dict)
for tid,new_,rs in recs(): allrecs[tid]['new' if new_ else 'old']=rs
def real(rs,p,s):
    xs=[];f=None
    for r in rs[1:]:
        if r['kind']=='match' and r['pattern_id']==p and r['subject_id']==s and r['regime']=='large-subject-throughput' and r['match_outcome']=='matched-as-expected':
            t=r['timing']; xs.append(t['elapsed_ns']/t['iterations']); f=(r.get('engine_metadata') or {}).get('callout_fires',f)
    return (st.median(xs),f) if xs else (None,None)
print('| arm | member | fires | old ns/fire | new ns/fire | real old-rec us | real latest-rec us | share L9 (old calib x L9 rec) | share NEW calib x latest rec | calib own share | latest record status |')
print('|---|---|---|---|---|---|---|---|---|---|---|')
for tid,v in sorted(allrecs.items()):
    k=MAP(tid)
    if not k or 'assist-v01' in tid: continue
    for p,s in (('co-luhn','co-luhn-1m'),('co-isbn','co-isbn-1m'),('co-member','co-member-1m'),('co-netstr-assist','co-netstr-1m'),('co-netstr','co-netstr-1m')):
        if p=='co-netstr' and 'pcrec' not in tid: continue
        ro,f=real(v['old'],p,s); rn,fn=real(v.get('new',v['old']),p,s)
        if ro is None or (k,p) not in new: continue
        so=f*old[(k,p)][0]/ro if (k,p) in old else None
        sn=fn*new[(k,p)][0]/rn
        flag=lambda x,key:('%.1f%%%s'%(x*100,' **>40**' if x>.4 else ' *>20 jit*' if ('pcre2-jit' in key and x>.2) else '') if x is not None else '-')
        print('| %s (%s) | %s | %d | %s | %.2f | %.0f | %.0f | %s | %s | %s | %s |'%(k,sh(tid).split('_')[-1] if 'pcrec' in tid else 'rec',p,fn,'%.2f'%old[(k,p)][0] if (k,p) in old else '-',new[(k,p)][0],ro/1e3,rn/1e3,flag(so,k),flag(sn,k),'%.1f%%'%(new[(k,p)][1]*100) if new[(k,p)][1] else '-',(v.get('new',v['old']))[0]['status']+(' (RERUN)' if 'new' in v else ' (L9)')))
