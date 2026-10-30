# [B148] L9 re-run read (lane b148l9rread): old-vs-new detail for the 7 re-run testees: nest-brace ladder, call streams, timed-out/gave-up groups, callout fires. Run: python3 detail.py
import sys,os,collections,statistics as st; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.argv=['x','none']
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cmp.py')).read().split("mode=sys.argv")[0])
def fmt(ns): return '%.1f us'%(ns/1e3) if ns<1e6 else '%.2f ms'%(ns/1e6) if ns<1e9 else '%.2f s'%(ns/1e9)
for tid,v in pairs.items():
    print('###',sh(tid))
    for lab in ('old','new'):
        rs=v[lab]; c,oc=cells(rs)
        # nest-brace ladder on cscan-onig throughput
        lad=[(k[1],c.get(k)) for k in sorted(c) if k[0]=='cscan-onig' and k[2]=='large-subject-throughput' and k[1].startswith('nest-brace')]
        to=collections.Counter(); gu=collections.Counter(); fires={}; stream={}
        for r in rs[1:]:
            if r['kind']!='match' or r['trial']!=1: continue
            o=r['match_outcome']
            if o=='timed-out': to[(r['pattern_id'],r['subject_id'])]+=1
            if o=='gave-up': gu[r['pattern_id']]+=1
            m=r.get('engine_metadata') or {}
            if 'callout_fires' in m and r['regime']=='large-subject-throughput': fires[(r['pattern_id'],r['subject_id'])]=m['callout_fires']
            if r['regime']=='call-stream' and r.get('timing') and r['trial']==1: stream[(r['pattern_id'],r['subject_id'])]=r['timing']['elapsed_ns']/r['timing']['iterations']
        print(' ',lab,'ladder',[(s,fmt(x[0])) for s,x in lad if x][:12])
        print(' ',lab,'timed-out(trial1)',dict(to),'gave-up',dict(gu))
        print(' ',lab,'fires',{k:f for k,f in sorted(fires.items()) if k[1].endswith('-1m')})
        print(' ',lab,'stream(trial1 one row)',{k:fmt(x) for k,x in sorted(stream.items())})
