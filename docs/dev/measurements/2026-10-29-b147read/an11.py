import sys,glob,statistics
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs2
S="/home/pcrec/projects/pcrec-bench/worktrees/b147read/store/records"
ex=("t-lka-dense-256k","t-lka-sparse-256k")
fs=sorted(glob.glob(S+"/syntax@0.[12]/pcrec_*/*ryzen7700x*.jsonl"))
pats={"esc-octal-0","cls-s-uc","cls-range","lit-cat"}
for f in fs:
    row=[]
    for p in sorted(pats):
        t,_=recs2.trial_sums(f,{p},"large-subject-throughput","plain",ex)
        row.append("%s %.0f"%(p,statistics.median(t[p])) if p in t else p+" -")
    print(f.split("/")[-2].replace("-simdna",""), f.split("__")[-1][:-6], " | ".join(row))
