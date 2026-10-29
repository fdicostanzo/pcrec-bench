import json,glob,statistics,collections
S="/home/pcrec/projects/pcrec-bench/worktrees/b147read/store/records"
def path(sb,tid,stamp_prefix):
    fs=sorted(glob.glob(f"{S}/{sb}/{tid}/*{stamp_prefix}*.jsonl"))
    assert len(fs)==1,(sb,tid,stamp_prefix,fs); return fs[0]
def load(p):
    """returns setup, compile{(pat,form)->row}, cells{(pat,subj,regime,form)->(median ns/call, n, outcomes)}"""
    setup=None; comp={}; tr=collections.defaultdict(list); oc=collections.defaultdict(collections.Counter)
    for l in open(p):
        d=json.loads(l); k=d.get("kind")
        if k=="setup": setup=d
        elif k=="compile": comp[(d.get("pattern_id"),d.get("form","plain"))]=d
        elif k=="match":
            key=(d["pattern_id"],d["subject_id"],d["regime"],d.get("form","plain"))
            oc[key][d["match_outcome"]]+=1
            t=d.get("timing")
            if t and t.get("iterations"): tr[key].append(t["elapsed_ns"]/t["iterations"])
    cells={k:(statistics.median(v) if v else None,len(v),oc[k]) for k,v in tr.items()}
    for k in oc:
        if k not in cells: cells[k]=(None,0,oc[k])
    return setup,comp,cells
