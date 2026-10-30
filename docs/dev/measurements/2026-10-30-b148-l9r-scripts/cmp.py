# [B148] L9 re-run read (lane b148l9rread): L9 record vs RERUN record of the same testee. Outcomes per cell (trial 1), per-cell median-ns ratio distribution, the headline short/MB-s rows. Run: python3 cmp.py [dist|head|out]
import sys,os,collections,statistics as st; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from load import *
by=collections.defaultdict(dict)
for tid,new,rs in recs(): by[tid]['new' if new else 'old']=rs
pairs={t:v for t,v in by.items() if 'new' in v and 'old' in v}
sh=lambda t:t.replace('_caps-simdna','').replace('-simdna','')
def cells(rs):
    d=collections.defaultdict(list); oc=collections.defaultdict(collections.Counter)
    for r in rs[1:]:
        if r['kind']!='match': continue
        k=(r['pattern_id'],r['subject_id'],r['regime'])
        oc[k][r['match_outcome']]+=1
        if r['match_outcome']=='matched-as-expected' and r.get('timing'):
            t=r['timing']; d[k].append((t['elapsed_ns']/t['iterations'],t['bytes_processed']/t['iterations']))
    return {k:(st.median(x[0] for x in v),v[0][1]) for k,v in d.items()},oc
def q(xs,p): xs=sorted(xs); return xs[min(len(xs)-1,int(p*len(xs)))]
mode=sys.argv[1] if len(sys.argv)>1 else 'dist'
HEAD={'cscan-onig':'comment-5m','cscan':'comment-5m','wild-sexp-balanced':'sx-1m','wild-json-validate-onig':'js-1m','wild-json-validate':'js-1m','co-luhn':'co-luhn-1m','co-isbn':'co-isbn-1m','co-member':'co-member-1m','co-netstr':'co-netstr-1m','co-netstr-assist':'co-netstr-1m'}
for tid,v in pairs.items():
    (co,oo),(cn,on)=cells(v['old']),cells(v['new'])
    if mode=='out':
        diff=[(k,dict(oo[k]),dict(on[k])) for k in set(oo)|set(on) if set(oo[k])!=set(on[k])]
        print('###',sh(tid),'cells old',len(oo),'new',len(on),'outcome-set differences',len(diff))
        for d in sorted(diff)[:12]: print('   ',d)
    if mode=='dist':
        print('###',sh(tid))
        for reg in ('short-subject-search','large-subject-throughput','call-stream'):
            rat=[cn[k][0]/co[k][0] for k in co if k in cn and k[2]==reg and co[k][0]>0]
            if not rat: continue
            out=sum(1 for x in rat if abs(x-1)>0.05)
            print('  %-26s n=%4d median %.3f p5 %.3f p95 %.3f min %.3f max %.3f  beyond+-5%%: %d'%(reg,len(rat),st.median(rat),q(rat,.05),q(rat,.95),min(rat),max(rat),out))
    if mode=='head':
        print('###',sh(tid))
        for pat,s in HEAD.items():
            row=[]
            for lab,c in (('old',co),('new',cn)):
                shorts=[c[k][0] for k in c if k[0]==pat and k[2]=='short-subject-search']
                t=c.get((pat,s,'large-subject-throughput'))
                row.append((st.mean(shorts) if shorts else None,len(shorts),t[1]/t[0]*1000 if t else None))
            if row[0][0] is None and row[1][0] is None and row[0][2] is None and row[1][2] is None: continue
            f=lambda x,u:('%.1f%s'%(x,u) if x is not None else '-')
            rt=lambda a,b:('x%.3f'%(b/a) if a and b else '-')
            print('  %-24s short old %s new %s (%s) | %s MB/s old %s new %s (%s)'%(pat,f(row[0][0],'ns'),f(row[1][0],'ns'),rt(row[0][0],row[1][0]),s,f(row[0][2],''),f(row[1][2],''),rt(row[1][2] and 1/row[1][2],row[0][2] and 1/row[0][2]) if False else (('x%.3f'%(row[1][2]/row[0][2])) if row[0][2] and row[1][2] else '-')))
