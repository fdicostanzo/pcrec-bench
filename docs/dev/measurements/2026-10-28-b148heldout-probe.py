#!/usr/bin/env python3
"""[B148] lane b148heldout -- held-out correctness probe for the L6 assists.

SCRATCH tier only. Builds a fixture copy of bench/unusual/assists under
$OUT/assists in which EVERY ledger row (incl. the NOT-CAPABLE ones) reads
ASSISTED (the assist files, token counts and sha256 are untouched), sets
tokcount.BUDGET very high IN THIS PROCESS ONLY so the adapter's budget gate
admits the over-budget rows, points $PCRECBENCH_ASSISTS_DIR at the copy
(which forces the scratch tier) and runs one `pcrecbench run` cell
(--trials 1 --iters 1). Nothing under bench/ is edited.

usage: probe.py OUT_DIR TESTEE [run args...]    e.g. ... --regimes search_short
"""
import os, shutil, sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
out, testee, extra = sys.argv[1], sys.argv[2], sys.argv[3:]
src = os.path.join(REPO, "bench", "unusual", "assists")
dst = os.path.join(out, "assists")
if not os.path.isdir(dst):
    shutil.copytree(src, dst)
    p = os.path.join(dst, "assists.tsv")
    lines = open(p).read().split("\n")
    head = lines[0].split("\t"); vi = head.index("verdict")
    for i, ln in enumerate(lines[1:], 1):
        f = ln.split("\t")
        if len(f) > vi:
            f[vi] = "ASSISTED"; lines[i] = "\t".join(f)
    open(p, "w").write("\n".join(lines))
os.environ["PCRECBENCH_ASSISTS_DIR"] = dst
os.environ["PCRECBENCH_SCRATCH_STORE"] = os.path.join(out, "store")
sys.path.insert(0, REPO); sys.path.insert(0, os.path.join(REPO, "tools"))
from pcrecbench import assists
assists.tokcount.BUDGET = 10 ** 6
from pcrecbench.__main__ import main
sys.exit(main(["run", "--subbench", "unusual", "--testee", testee, "--trials", "1",
               "--iters", "1", "--tier", "scratch", "--force-unquiet", "--synthetic"] + extra))
