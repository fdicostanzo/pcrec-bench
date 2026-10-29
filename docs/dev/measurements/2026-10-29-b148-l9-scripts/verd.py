# [B148] L9 read (lane b148l9read, 2026-10-29): analysis helper over the SCRATCH store build/scratch-store/records/unusual@0.1; reads JSONL, no timing. Run: python3 -I is NOT used (imports its sibling).
import sys,json,collections,re,csv; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tab import *
MEM={'cscan':['cscan','cscan-onig'],'wild-sexp':['wild-sexp-balanced'],'wild-json':['wild-json-validate','wild-json-validate-onig'],
 'co-luhn':['co-luhn'],'co-isbn':['co-isbn'],'co-member':['co-member'],'co-netstr':['co-netstr','co-netstr-assist'],
 'va-tenant':['va-tenant'],'va-route':['va-route'],'va-term':['va-term'],'va-term-bang':['va-term-bang']}
def cell(rs,pats):
    comp={}
    for r in rs[1:]:
        if r['kind']=='compile' and r['pattern_id'] in pats: comp[r['pattern_id']]=r['compile_outcome']
    ran=[p for p in pats if comp.get(p)=='compiled']
    if not ran: return 'unsupported'
    ok=wr=to=0; gu=collections.Counter(); n=0
    for r in rs[1:]:
        if r['kind']!='match' or r['trial']!=1 or r['pattern_id'] not in ran: continue
        o=r['match_outcome']; n+=1
        if o=='matched-as-expected': ok+=1
        elif o in('did-not-match-as-expected','wrong-span-or-captures'): wr+=1
        elif o=='timed-out': to+=1
        elif o=='gave-up':
            m=re.search(r'giveup:(-?\d+:?\w*)',r.get('diagnostic','')); gu[m.group(1) if m else 'stream-partial']+=1
    s='%d ok'%ok
    if wr: s+=', %d WRONG'%wr
    if gu: s+=', %d gave-up (%s)'%(sum(gu.values()),'/'.join('%s×%d'%kv for kv in gu.items()))
    if to: s+=', %d timed-out'%to
    return s
print('| testee | '+' | '.join(MEM)+' |'); print('|---'*(len(MEM)+1)+'|')
for tid,rs in data.items():
    print('| `%s` | '%short(tid)+' | '.join(cell(rs,MEM[m]) for m in MEM)+' |')
