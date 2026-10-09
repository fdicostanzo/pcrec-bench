#!/usr/bin/env python3
"""[B129] "unprimed behaviour unchanged" control -- analysis.

Source: two scratch stores written by 2026-10-09-b129-prime-unchanged-run.sh,
MASTER = worktrees/b129ctl/build/scratch-store-b129unch (pristine master
drivers), FIXED = worktrees/b129prime/build/scratch-store-b129unch (the
restructured --prime drivers), both run WITHOUT --prime, M,F,M,F back to back.
Run:  python3 docs/dev/measurements/2026-10-09-b129-prime-unchanged-analysis.py \
          <master-store> <fixed-store>
Per (testee, pattern, regime) and repetition: F/M median ratio and whether
the closed [min,max] trial ranges overlap (the front page's tie rule), then
the ranges pooled over the two repetitions. Arithmetic: tools/frontpage.Summary
(pcrecbench.reduce). No number is typed.
"""
import os, sys
from collections import defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "tools"))
import frontpage as fp                      # noqa: E402


def load(store):
    out = defaultdict(list)
    for r in sorted(fp.index_rows(store), key=lambda r: r["timestamp"]):
        s = fp.Summary(store, r)
        for (pid, reg), c in s.cells.items():
            out[(fp.engine_of(s.testee_id), pid, reg)].append((c, r["status"]))
    return out


def ov(a, b):
    return max(a["lo"], b["lo"]) <= min(a["hi"], b["hi"])


def main(mstore, fstore):
    M, F = load(mstore), load(fstore)
    print("%-7s %-18s %-24s %3s %12s %12s %8s %s" % (
        "testee", "pattern", "regime", "rep", "master med", "fixed med", "F/M", "ranges"))
    for k in sorted(set(M) | set(F)):
        ms, fs = M.get(k, []), F.get(k, [])
        if len(ms) != len(fs):
            print(k, "UNEQUAL reps", len(ms), len(fs))
        for i, ((m, sm), (f, sf)) in enumerate(zip(ms, fs), 1):
            print("%-7s %-18s %-24s %3d %12.6g %12.6g %8.4f %s  [%s,%s]" % (
                k[0], k[1], k[2], i, m["median"], f["median"],
                f["median"] / m["median"], "overlap" if ov(m, f) else "DISJOINT", sm, sf))
        if ms and fs:
            lo = lambda L: min(c["lo"] for c, _ in L)
            hi = lambda L: max(c["hi"] for c, _ in L)
            pm = dict(lo=lo(ms), hi=hi(ms)); pf = dict(lo=lo(fs), hi=hi(fs))
            print("%-7s %-18s %-24s pooled ranges: master [%.6g, %.6g] fixed [%.6g, %.6g] -> %s" % (
                k[0], k[1], k[2], pm["lo"], pm["hi"], pf["lo"], pf["hi"],
                "OVERLAP" if ov(pm, pf) else "DISJOINT"))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
