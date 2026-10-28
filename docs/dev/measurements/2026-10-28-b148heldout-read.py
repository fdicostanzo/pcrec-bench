#!/usr/bin/env python3
"""Read the b148heldout scratch records: per (testee, member, regime) outcome
counts, mismatch rows, callout_fires.  usage: read.py OUT_DIR"""
import glob, json, sys, collections
out = sys.argv[1]
for f in sorted(glob.glob(out + "/*/store/records/unusual@0.1/*/*.jsonl")):
    L = [json.loads(l) for l in open(f)]
    hdr = L[0]
    print("=" * 8, f.split("/")[-2], hdr["status"])
    print("  assist:", json.dumps(hdr["testee"].get("assist"))[:600])
    comp = {}
    for x in L:
        if x.get("kind") == "compile":
            comp[x["pattern_id"]] = {k: v for k, v in x.items()
                                     if k in ("outcome", "compile_outcome", "assist_tokens", "declaration_ref", "reason")}
    c = collections.defaultdict(collections.Counter)
    bad = []
    fires = {}
    for x in L:
        if x.get("kind") != "match":
            continue
        c[(x["pattern_id"], x["regime"])][x["match_outcome"]] += 1
        if x["match_outcome"] != "matched-as-expected":
            bad.append(x)
        for src in (x, x.get("timing", {}), x.get("engine_metadata", {})):
            if "callout_fires" in src:
                fires[(x["pattern_id"], x["subject_id"])] = src["callout_fires"]
    for k, v in sorted(c.items()):
        print("  %-26s %-22s %s" % (k[0], k[1], dict(v)))
    for k, v in sorted(comp.items()):
        print("  compile", k, v)
    for x in bad[:80]:
        print("  BAD", json.dumps({k: v for k, v in x.items() if k != "timing"})[:320])
    if len(bad) > 80:
        print("  ... %d bad rows total" % len(bad))
    print("  fires(throughput 1m rows):", {"%s/%s" % k: v for k, v in fires.items() if k[1].endswith("-1m") and v})
