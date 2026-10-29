import sys,statistics,collections
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
def get(sb,pin,cfg,stamp=""):
    return recs.load(recs.path(sb,f"pcrec_{pin}_{cfg}-simdna",stamp))
def setsums(cells,keys):
    out=collections.defaultdict(float)
    for k in keys:
        out[(k[0],k[2])]+=cells[k][0]
    return out
def pct(v,q):
    v=sorted(v); return v[min(len(v)-1,int(q*len(v)))]
for cfg in ("auto-caps","auto-nocaps"):
    a=get("capability@0.2","9ae59f5d4",cfg)[2]      # prior window
    b=get("capability@0.3","9ae59f5d4",cfg)[2]      # this window
    keys=[k for k in a if k in b and a[k][0] and b[k][0] and set(a[k][2])=={"matched-as-expected"}|set(a[k][2]) and set(b[k][2])<= {"matched-as-expected"} and set(a[k][2])<={"matched-as-expected"}]
    r=[b[k][0]/a[k][0] for k in keys]
    print(f"== cross-window control {cfg}: 9ae59f5d4 @0.3 (10-28) / @0.2 (10-25); common clean subject-cells n={len(keys)} of a={len(a)} b={len(b)}")
    print(" subject-cell ratio median %.4f p5 %.4f p95 %.4f min %.3f max %.3f; |dev|>5%%: %d, >10%%: %d"%(statistics.median(r),pct(r,.05),pct(r,.95),min(r),max(r),sum(abs(x-1)>.05 for x in r),sum(abs(x-1)>.1 for x in r)))
    sa,sb=setsums(a,keys),setsums(b,keys)
    sr={k:sb[k]/sa[k] for k in sa}
    v=list(sr.values())
    print(" set-cell (pattern,regime; common subjects) ratio n=%d median %.4f p5 %.4f p95 %.4f; >+-5%%: %d, >+-10%%: %d"%(len(v),statistics.median(v),pct(v,.05),pct(v,.95),sum(abs(x-1)>.05 for x in v),sum(abs(x-1)>.1 for x in v)))
    worst=sorted(sr.items(),key=lambda kv:-abs(kv[1]-1))[:8]
    for k,x in worst: print("   ",k,"x%.3f"%x, "%.1f -> %.1f"%(sa[k],sb[k]))
    # new-in-0.3 subjects
    new=sorted({(k[1]) for k in b if k not in a})
    print(" subjects only in @0.3:",new)
print("---- by regime (set-cells) ----")
for cfg in ("auto-caps","auto-nocaps"):
    a=get("capability@0.2","9ae59f5d4",cfg)[2]; b=get("capability@0.3","9ae59f5d4",cfg)[2]
    keys=[k for k in a if k in b and a[k][0] and b[k][0] and set(a[k][2])<={"matched-as-expected"} and set(b[k][2])<={"matched-as-expected"}]
    sa,sb=setsums(a,keys),setsums(b,keys)
    byr=collections.defaultdict(list)
    for k in sa: byr[k[1]].append(sb[k]/sa[k])
    for r,v in byr.items(): print(cfg,r,"n=%d median %.4f p5 %.3f p95 %.3f"%(len(v),statistics.median(v),pct(v,.05),pct(v,.95)))
