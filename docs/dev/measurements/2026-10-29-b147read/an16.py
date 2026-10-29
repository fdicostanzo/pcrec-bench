import sys,glob,csv,collections
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
S=recs.S
cen={}
for r in csv.DictReader((l for l in open("/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-27-b147prep-census.tsv") if not l.startswith("#")),delimiter="\t"):
    def pb(s):
        try: e,c=s.split(":"); return int(e),int(c)
        except: return None
    cen[(r["set"],r["pattern_id"],r["config"],r["form"])]=(r["attribution"],r["v3"],pb(r["old_bytes:code"]),pb(r["new_bytes:code"]))
def run(sb_old,sb_new,old_t,new_t,setn,cfg):
    a=recs.load(glob.glob(S+f"/{sb_old}/{old_t}/*{'20261028T' if sb_old.endswith('0.3') else '20261026T03'}*.jsonl")[0])[1]
    b=recs.load(glob.glob(S+f"/{sb_new}/{new_t}/*20261028T*.jsonl")[0])[1]
    tot=agree=0; v3same=v3chg=0; mism=[]; refmove=[]
    for k in sorted(set(a)|set(b)):
        x,y=a.get(k),b.get(k)
        form="plain" if k[1]=="plain" else "whole"
        c=cen.get((setn,k[0],cfg,form))
        if not x or not y: continue
        if x["compile_outcome"]!="compiled" or y["compile_outcome"]!="compiled":
            if x["compile_outcome"]!=y["compile_outcome"]: refmove.append((k,x["compile_outcome"],y["compile_outcome"]))
            continue
        tot+=1
        mx,my=x["engine_metadata"],y["engine_metadata"]
        same=mx["program_sha256_v3"]==my["program_sha256_v3"]
        v3same+=same; v3chg+=(not same)
        if c is None: mism.append((k,"no census row")); continue
        census_same=(c[1]=="identical")
        de=my["emit_bytes"]-mx["emit_bytes"]; dc=my["emit_code_bytes"]-mx["emit_code_bytes"]
        cd=(c[3][0]-c[2][0],c[3][1]-c[2][1]) if c[2] and c[3] else None
        if same!=census_same: mism.append((k,"identity differs from census",c[0]))
        elif same and (de,dc)!=(0,0): mism.append((k,"identical but bytes moved",de,dc))
        elif not same and cd and (de,dc)!=cd: mism.append((k,"delta differs",(de,dc),cd,c[0]))
        else: agree+=1
    print(f"{sb_new} {new_t.split('_')[2]}: compiled-both rows {tot}; v3 identical {v3same}, changed {v3chg}; agree with census (identity+emit/code deltas) {agree}; mismatches {len(mism)}; refusal movers {refmove}")
    for m in mism[:12]: print("    ",m)
run("capability@0.3","capability@0.3","pcrec_9ae59f5d4_auto-caps-simdna","pcrec_614d45eb3_auto-caps-simdna","capability","caps")
run("capability@0.3","capability@0.3","pcrec_9ae59f5d4_auto-nocaps-simdna","pcrec_614d45eb3_auto-nocaps-simdna","capability","nocaps")
run("syntax@0.1","syntax@0.2","pcrec_9ae59f5d4_auto-caps-simdna","pcrec_614d45eb3_auto-caps-simdna","syntax","caps")
