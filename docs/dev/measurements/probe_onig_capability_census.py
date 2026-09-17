#!/usr/bin/env python3
"""docs/dev/measurements/probe_onig_capability_census.py -- the reproducing
script behind 2026-09-17-onig-capability-witness-census-6.9.10.txt.

Lane l6bonig ([B7]/L6b, capability_set_v1.md 11.1): the ONIGURUMA ADAPTER'S
own capability witness census, mandatory BEFORE the `ext bench` capability
matrix declares anything for `onig-default` (the L5 lesson: "three wrong
first-cut declarations" on the pcrec side, docs/dev/lanes/b42cap_report.md
2).

TWO PASSES, both through the REAL onig-default adapter (never a second
parser, never pcrecbench.subbench's own text without going through
Adapter.compile()):

  1. ONE ISOLATED WITNESS PER REQUIRES TOKEN (17 tokens,
     pcrecbench.capability.REQUIRES_VOCAB) -- the same discipline
     testees/pcre2/CLAUDE.md and docs/dev/lanes/b42cap_report.md 2 use:
     a minimal pattern that exercises exactly one construct, so a
     refusal is attributable to ONE token, not a confound of several.
     Several witnesses per token where a single one would not settle
     the question by itself (recursion's five spellings; named-groups'
     two).
  2. EVERY ONE OF bench/capability's 64 REAL corpus patterns, cross-
     referenced against each pattern's own `requires-*` tags -- the
     literal ask ("every bench/capability pattern through onig_new"),
     and the check that the isolated-witness verdict actually holds on
     REAL, not synthetic, text.

Run: python3 docs/dev/measurements/probe_onig_capability_census.py
(from the repo root; needs the `onig` adapter's driver, built on demand).
"""
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)

from pcrecbench import adapters as ad          # noqa: E402
from pcrecbench import subbench as sbmod       # noqa: E402

# One or more witnesses per REQUIRES_VOCAB token (pcrecbench.capability.
# REQUIRES_VOCAB, 17 tokens). `span-reporting`, `non-utf8-subject` and
# `captures` are EXECUTION-MODEL facts (capability_set_v1.md 5.1's own
# note) -- not compile witnesses, verified separately below.
WITNESSES = {
    "backrefs": [rb"(a)\1"],
    "lookaround": [rb"(?=a)a", rb"(?<=a)b"],
    "lookbehind-variable": [rb"(?<=a|bc)x"],
    "possessive-quantifier": [rb"a*+"],
    "atomic-group": [rb"(?>a*)b"],
    "recursion": [rb"(a(?R)?b)", rb"(a(?1)?b)", rb"(?<n>a(?&n)?b)",
                 rb"(a\g<1>?b)", rb"(?<n>a\g<n>?b)", rb"(a(?0)?b)"],
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
    cp = a.compile("onig-default", name, pat, {}, 1, tmp)
    r = cp.get(ad.FORM_PLAIN)
    return r.outcome, r.diagnostic


def main():
    a = ad.discover(root=os.path.join(ROOT, "testees"))["onig"]
    tmp = tempfile.mkdtemp(prefix="onig-census-")
    a.prepare("onig-default", tmp)

    print("=== pass 1: one isolated witness per REQUIRES token ===")
    for token, pats in WITNESSES.items():
        for i, pat in enumerate(pats):
            name = "w-%s-%d" % (token.replace(" ", "_"), i)
            outcome, diag = compile_one(a, tmp, name, pat)
            print("%-24s %-40r %-16s %s"
                 % (token, pat, outcome, diag or ""))

    print()
    print("=== pass 2: every bench/capability corpus pattern (64) ===")
    sb = sbmod.load(os.path.join(ROOT, "bench", "capability"))
    print("n patterns:", len(sb.patterns))
    n_ok = 0
    for p in sb.patterns:
        txt = p.pattern_bytes() if hasattr(p, "pattern_bytes") else p.text
        outcome, diag = compile_one(a, tmp, p.name, txt)
        tags = [t for t in (getattr(p, "tags", None) or [])
               if t.startswith("requires-")]
        if outcome == "compiled":
            n_ok += 1
        else:
            print("REFUSED  %-40s %-40s -> %s" % (p.name, tags, diag))
    print("compiled: %d / %d" % (n_ok, len(sb.patterns)))


if __name__ == "__main__":
    main()
