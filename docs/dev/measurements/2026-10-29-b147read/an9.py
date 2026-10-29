import sys,glob
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs2
S="/home/pcrec/projects/pcrec-bench/worktrees/b147read/store/records"
a=glob.glob(S+"/syntax@0.1/pcrec_9ae59f5d4_auto-caps-simdna/*.jsonl")[0]
b=glob.glob(S+"/syntax@0.2/pcrec_614d45eb3_auto-caps-simdna/*.jsonl")[0]
pats={"cls-range","cls-s-uc","asr-k-uc","esc-octal-0","esc-tab"}
ex=("t-lka-dense-256k","t-lka-sparse-256k")
for reg,form in (("large-subject-throughput","plain"),("short-subject-search","plain"),("match-compliance","whole-subject")):
    ta,na=recs2.trial_sums(a,pats,reg,form,ex); tb,nb=recs2.trial_sums(b,pats,reg,form,ex)
    print("==",reg)
    for p in sorted(pats):
        if p in ta and p in tb:
            f=lambda v:"[%s]"%" ".join("%.0f"%x for x in sorted(v))
            print(" ",p,"9ae",f(ta[p]),"614",f(tb[p]),"n/trial",na[p],nb[p])
