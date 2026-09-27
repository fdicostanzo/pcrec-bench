# Source: pcrec-bench manager, 2026-09-27 (O-62). Reads committed reports/*.matrix.tsv only (argv).
# Per row: pcrec best-of-configs vs best FULL-GRAIN non-pcrec testee (vectorscan block-nosom EXCLUDED: boolean grain).
# Prints per-regime win / lose<=x2 / lose>x2 tallies, every loss >x2, and up to 8 wins >x10.
import csv,sys,re
from collections import Counter
def num(s):
    try: return float(s)
    except: return None
for M in sys.argv[1:]:
    lines=open(M).read().splitlines()
    hdr=[l for l in lines if l.startswith('#')][:1]
    r=list(csv.reader([l for l in lines if not l.startswith('#')],delimiter='\t'));h=r[0]
    t=[c for c in h[10:]]
    print('=====',M.split('/')[-1]); print('  testees:',', '.join(sorted(set(re.sub(r'_[0-9a-f]{7,8}_','_',c) for c in t))))
    tallies={};loss=[];wins=[]
    for x in r[1:]:
        if len(x)<len(h): continue
        d=dict(zip(h,x));b=num(d['best_ns_pooled'])
        if b is None: continue
        g=lambda cs:[(num(d[k])*b,k) for k in cs if num(d[k]) is not None]
        p=g([k for k in t if k.startswith('pcrec')]);o=g([k for k in t if not k.startswith('pcrec') and 'nosom' not in k])
        reg=x[2]+('/'+x[3] if x[3]!='plain' else '')
        c=tallies.setdefault(reg,Counter())
        if not p or not o: c['n/a']+=1;continue
        bp=min(p);bo=min(o);q=bp[0]/bo[0]
        c['win' if q<1 else ('lose>2' if q>2 else 'lose<=2')]+=1
        short=lambda k:k.split('_')[0]+'/'+k.split('_')[2].split('-')[0] if len(k.split('_'))>2 else k
        if q>2: loss.append((q,x[1],reg,bp[0],short(bp[1]),bo[0],short(bo[1])))
        if q<0.1: wins.append((q,x[1],reg,bp[0],short(bp[1]),bo[0],short(bo[1])))
    for k,v in tallies.items(): print('  ',k,dict(v))
    for q,p,reg,a,ac,bb,bc in sorted(loss,reverse=True): print(f'   LOSE x{q:7.2f} {p:28s} {reg:32s} pcrec {a/1e3:10.1f}us ({ac}) vs {bb/1e3:10.1f}us ({bc})')
    for q,p,reg,a,ac,bb,bc in sorted(wins)[:8]: print(f'   WIN  x{1/q:7.1f} {p:28s} {reg:32s} pcrec {a/1e3:10.1f}us ({ac}) vs {bb/1e3:10.1f}us ({bc})')
    if len(wins)>8: print(f'   ... {len(wins)} rows pcrec >x10 faster')
