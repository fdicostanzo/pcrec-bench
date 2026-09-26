#!/usr/bin/env python3
"""docs/dev/measurements/probe_vectorscan_som_witness_census.py -- the
reproducing script behind 2026-09-26-vectorscan-som-vs-nosom-census.txt.

[B92] (docs/dev/plan.md; Frank's ruling on docs/dev/lanes/
b72smalls_report.md 4 / capability_set_v1.md 5.6 -- option (b) of the two
live candidates named there): `vectorscan-block-som` (HS_FLAG_SOM_LEFTMOST
always set) was wired to answer the driver protocol's EXISTING
non-overlapping find-all count (NMATCHES) and first-match span, at FULL
scoring grain. HS_FLAG_SOM_LEFTMOST documents a real, ADDITIONAL compile-
time restriction beyond `nosom`'s own refusal set (Hyperscan's own
documented history-tracking limit: some expressions would need to track
an unbounded amount of match history to report a leftmost start offset,
and SOM tracking refuses those outright rather than accept and misreport).
This is a COMPILE-ONLY census (no timing, no match run, no quiet-box gate
needed -- mirrors `probe_vectorscan_capability_census.py`'s own stated
exemption): every one of `bench/capability`'s 64 real corpus patterns,
compiled through the REAL adapter under BOTH configs (`plain` form only --
SOM's own restriction is about the pattern's history-tracking shape, not
about the `^...\\z` wrapper), and the ONE-CHARACTER-CONTROLLED isolated
witness this lane's own selfcheck arm already uses (`.*a.{40,}`, refused
under `som`, compiled under `nosom`).

Run: python3 docs/dev/measurements/probe_vectorscan_som_witness_census.py
(from the repo root; needs the `vectorscan` adapter's driver, built on
demand -- libvectorscan-dev must be installed).
"""
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)

from pcrecbench import adapters as ad          # noqa: E402
from pcrecbench import subbench as sbmod       # noqa: E402

# The isolated witness this lane's own tools/selfcheck.py:check_vectorscan_som
# arm 5 uses -- a SOM-only refusal (Hyperscan's own documented
# history-tracking restriction), reproduced here beside the corpus census
# rather than only inside the check suite.
ISOLATED_WITNESSES = {
    "som-only-refusal (unbounded lookahead-shaped repeat)": rb".*a.{40,}",
}


def compile_one(a, tmp, tid, name, pat):
    cp = a.compile(tid, name, pat, {}, 1, tmp)
    r = cp.get(ad.FORM_PLAIN)
    return r.outcome, r.diagnostic


def main():
    a = ad.discover(root=os.path.join(ROOT, "testees"))["vectorscan"]
    tmp = tempfile.mkdtemp(prefix="vectorscan-som-census-")
    a.prepare("vectorscan-block-nosom", tmp)
    a.prepare("vectorscan-block-som", tmp)

    print("=== isolated witness(es): a SOM-only compile restriction ===")
    for label, pat in ISOLATED_WITNESSES.items():
        outcome_nosom, diag_nosom = compile_one(
            a, tmp, "vectorscan-block-nosom", "w-nosom", pat)
        outcome_som, diag_som = compile_one(
            a, tmp, "vectorscan-block-som", "w-som", pat)
        print("%-55s nosom=%-16s som=%-16s"
             % (label, outcome_nosom, outcome_som))
        if outcome_nosom != outcome_som:
            print("    nosom diag: %s" % (diag_nosom or ""))
            print("    som   diag: %s" % (diag_som or ""))

    print()
    print("=== bench/capability's 64 corpus patterns, plain form, "
          "nosom vs som ===")
    sb = sbmod.Subbench(os.path.join(ROOT, "bench", "capability"))
    print("n patterns:", len(sb.patterns))
    n_both = n_nosom_only = n_som_only = n_neither = 0
    divergences = []
    for p in sb.patterns:
        txt = p.text
        outcome_nosom, diag_nosom = compile_one(
            a, tmp, "vectorscan-block-nosom", "c-nosom-" + p.name, txt)
        outcome_som, diag_som = compile_one(
            a, tmp, "vectorscan-block-som", "c-som-" + p.name, txt)
        ok_nosom = outcome_nosom == "compiled"
        ok_som = outcome_som == "compiled"
        if ok_nosom and ok_som:
            n_both += 1
        elif ok_nosom and not ok_som:
            n_nosom_only += 1
            divergences.append((p.name, diag_som))
        elif ok_som and not ok_nosom:
            n_som_only += 1
            divergences.append((p.name, "compiles under som but NOT nosom "
                               "-- unexpected, investigate: %r" % diag_nosom))
        else:
            n_neither += 1
    print("compiled under BOTH:       %d" % n_both)
    print("compiled under nosom ONLY (SOM's own restriction costs this "
          "pattern): %d" % n_nosom_only)
    print("compiled under som ONLY (unexpected):  %d" % n_som_only)
    print("compiled under NEITHER:    %d" % n_neither)
    if divergences:
        print()
        print("=== the SOM-only restriction's cost, by pattern ===")
        for name, diag in divergences:
            print("  %-48s -> %s" % (name, diag))


if __name__ == "__main__":
    main()
