#!/usr/bin/env python3
"""docs/dev/measurements/probe_vectorscan_capability_census.py -- the
reproducing script behind 2026-09-17-vectorscan-capability-witness-census-
5.4.11.txt.

Lane l6bvs ([B7]/L6b wave 2, capability_set_v1.md 11.1): the VECTORSCAN
ADAPTER'S own capability witness census, mandatory BEFORE the `ext bench`
capability matrix declares anything for `vectorscan-block-nosom` -- the
same discipline testees/onig/'s l6bonig lane and pcrec's own [B42] L5
census used (docs/dev/lanes/b42cap_report.md 2's "wrong first-cut" lesson:
never declare from documentation prose alone when a real compile is one
call away).

TWO PASSES, both through the REAL vectorscan-block-nosom adapter (never a
second parser, never pcrecbench.subbench's own text without going through
Adapter.compile()):

  1. ONE ISOLATED WITNESS PER REQUIRES TOKEN (17 tokens,
     pcrecbench.capability.REQUIRES_VOCAB) -- a minimal pattern
     exercising exactly one construct, so a refusal is attributable to
     ONE token. `span-reporting`, `non-utf8-subject` and `captures` are
     EXECUTION-MODEL facts (capability_set_v1.md 5.1's own note), not
     compile witnesses -- stated, not probed, in the printed table.
  2. EVERY ONE of bench/capability's 64 REAL corpus patterns, cross-
     referenced against each pattern's own `requires-*` tags.

Run: python3 docs/dev/measurements/probe_vectorscan_capability_census.py
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

# One or more witnesses per REQUIRES_VOCAB token that IS a compile-time
# construct. `span-reporting` (needs HS_FLAG_SOM_LEFTMOST, not carried by
# this config by construction), `non-utf8-subject` (an execution-model
# fact: no HS_FLAG_UTF8 is ever set, so any byte sequence is a valid
# subject) and `captures` (Hyperscan has NO capturing-group mechanism at
# all, structurally, regardless of pattern text) are stated separately
# below, never as a compile witness.
WITNESSES = {
    "backrefs": [rb"(a)\1"],
    "lookaround": [rb"(?=a)a", rb"(?<=a)b"],
    "lookbehind-variable": [rb"(?<=a|bc)x"],
    "possessive-quantifier": [rb"a*+"],
    "atomic-group": [rb"(?>a*)b"],
    "recursion": [rb"(a(?R)?b)", rb"(a(?1)?b)"],
    "conditionals": [rb"(?(1)a|b)(a)?"],
    "k-reset": [rb"a\Kb"],
    "control-verbs": [rb"a(*ACCEPT)b", rb"a(*FAIL)b", rb"a(*SKIP)b"],
    "unicode-properties": [rb"\p{L}", rb"\p{Alpha}"],
    "named-groups": [rb"(?<name>a)", rb"(?P<name>a)"],
    "free-spacing": [rb"(?x) a b c"],
    "callouts": [rb"a(?C1)b"],
    "true-end-anchor": [rb"a\z"],
}


def compile_one(a, tmp, name, pat):
    cp = a.compile("vectorscan-block-nosom", name, pat, {}, 1, tmp)
    r = cp.get(ad.FORM_PLAIN)
    return r.outcome, r.diagnostic


def main():
    a = ad.discover(root=os.path.join(ROOT, "testees"))["vectorscan"]
    tmp = tempfile.mkdtemp(prefix="vectorscan-census-")
    a.prepare("vectorscan-block-nosom", tmp)

    print("=== EXECUTION-MODEL facts (not compile witnesses) ===")
    print("span-reporting       NOT SATISFIED -- HS_FLAG_SOM_LEFTMOST is "
          "never set by this config (that is the `nosom` config's whole "
          "reason to exist; the som config, documented not built, would "
          "satisfy it)")
    print("non-utf8-subject     SATISFIED -- HS_FLAG_UTF8 is never set; "
          "this driver is byte-oriented (Vectorscan's documented default), "
          "same as every other testee's default 8-bit convention")
    print("captures             NOT SATISFIED -- Hyperscan has NO "
          "capturing-group mechanism at all, structurally (confirmed by "
          "pass 1's own `named-groups` witnesses below: they compile "
          "clean, because Hyperscan accepts the SYNTAX and silently "
          "treats every group as non-capturing -- see this file's own "
          "reading in testees/vectorscan/CLAUDE.md)")
    print()

    print("=== pass 1: one isolated witness per REQUIRES token (compile-"
          "time constructs only) ===")
    for token, pats in WITNESSES.items():
        for i, pat in enumerate(pats):
            name = "w-%s-%d" % (token.replace(" ", "_"), i)
            outcome, diag = compile_one(a, tmp, name, pat)
            print("%-24s %-30r %-16s %s"
                 % (token, pat, outcome, diag or ""))

    print()
    print("=== pass 2: every bench/capability corpus pattern (64) ===")
    sb = sbmod.Subbench(os.path.join(ROOT, "bench", "capability"))
    print("n patterns:", len(sb.patterns))
    n_ok = 0
    for p in sb.patterns:
        txt = p.text
        outcome, diag = compile_one(a, tmp, p.name, txt)
        tags = [t for t in (getattr(p, "tags", None) or [])
               if t.startswith("requires-")]
        if outcome == "compiled":
            n_ok += 1
        else:
            print("REFUSED  %-48s %-40s -> %s" % (p.name, tags, diag))
    print("compiled: %d / %d" % (n_ok, len(sb.patterns)))


if __name__ == "__main__":
    main()
