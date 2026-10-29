import json,collections,statistics
def trial_sums(path,patterns,regime,form,exclude_subj=()):
    """per-trial set sums of ns/call over subjects for given patterns; returns {pattern:[sum per trial]}"""
    t=collections.defaultdict(lambda: collections.defaultdict(float)); n=collections.defaultdict(lambda: collections.defaultdict(int))
    for l in open(path):
        d=json.loads(l)
        if d["kind"]!="match" or d["pattern_id"] not in patterns or d["regime"]!=regime or d.get("form","plain")!=form: continue
        if d["subject_id"] in exclude_subj: continue
        tm=d.get("timing")
        if not tm or d["match_outcome"]!="matched-as-expected": continue
        t[d["pattern_id"]][d["trial"]]+=tm["elapsed_ns"]/tm["iterations"]; n[d["pattern_id"]][d["trial"]]+=1
    return {p:[t[p][k] for k in sorted(t[p])] for p in t}, {p:set(n[p].values()) for p in n}
