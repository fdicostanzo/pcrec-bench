import sys,glob,statistics
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs2
S="/home/pcrec/projects/pcrec-bench/worktrees/b147read/store/records"
fs=sorted(glob.glob(S+"/capability@0.[23]/pcrec_*auto-*/*ryzen7700x*.jsonl"))
pats=["evil-alt-nested","numeric-id-nested-plus","phone-list-nested-plus","date-nested-plus"]
for reg in ("large-subject-throughput","short-subject-search"):
    print("==",reg)
    for f in fs:
        t,_=recs2.trial_sums(f,set(pats),reg,"plain",("t-hyb-datepath-16k","t-hyb-digits-4k","t-hyb-embed-1k","t-hyb-embed-64k","t-hyb-embed-8k","t-hyb-logline-16k"))
        print(" %-26s %s"%(f.split("/")[-2].replace("-simdna","").replace("pcrec_",""),f.split("__")[-1][4:15]),"  ".join("%s %.0f [%.0f-%.0f]"%(p[:12],statistics.median(t[p]),min(t[p]),max(t[p])) for p in pats if p in t))
