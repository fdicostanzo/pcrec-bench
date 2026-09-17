#!/usr/bin/env python3
"""probe_re2_capability_census.py -- ([B42] L6b, testees/re2/) THE RE2
CAPABILITY WITNESS CENSUS.

The L5 lesson (bench/capability/gen_patterns.py's own EXT_BENCH_ROSTER
comment, "RE-VERIFIED ... against a real compile census ... never
inferred from ... prose alone"): a capability declaration is derived from
WITNESSED compiles/refusals, never from documentation. This script:

  1. compiles ONE minimal witness pattern per REQUIRES_VOCAB token (the
     same "one construct, otherwise plain" idiom bench/syntax/bench/
     capability's own EXT_BENCH_ROSTER witnesses use) through the REAL
     `testees/re2/adapter.py` `compile()` path -- never a second
     hand-rolled RE2 invocation;
  2. compiles every one of `bench/capability@0.1`'s 64 canonical patterns
     (the set this census exists to declare capabilities FOR);
  3. compiles every one of `bench/syntax@0.1`'s 95 canonical patterns (a
     second corpus, "as available" -- the census's own cross-check that
     the witness-derived vocabulary reading holds on real, differently-
     authored patterns, not just the one-construct witnesses).

Reuses the adapter's own `compile()` (never a second copy of the g++/
pkg-config flags or the Latin1-encoding decision) -- pcrec D35's own
"reuses the adapters' own compile and driver paths" rule. Runs from the
repo root:

    python3 docs/dev/measurements/probe_re2_capability_census.py
"""
import os
import sys
import re as _re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, REPO_ROOT)

from pcrecbench import adapters as _ad          # noqa: E402
from pcrecbench import subbench as _sb          # noqa: E402
from testees.re2.adapter import classify_refusal  # noqa: E402

WORKDIR = os.path.join(REPO_ROOT, "build", "work", "re2-census")

# One minimal witness per REQUIRES_VOCAB token (docs/design/
# capability_set_v1.md 5.1's 17-token vocabulary), each "one construct in
# an otherwise plain body" -- bench/syntax's own idiom, so a refusal
# points at one mechanism. Every witness is ASCII, plain-body, and (where
# the token names a Perl/PCRE extension RE2 does not have at all) exactly
# the shape docs/dev/research/2026-09-12-b42-engine-landscape.md 3's own
# table cites for that engine/construct pair.
WITNESSES = [
    ("backrefs", rb"(a)\1"),
    ("lookaround", rb"a(?=b)"),
    ("lookbehind-variable", rb"(?<=a|bc)x"),
    ("possessive-quantifier", rb"a++"),
    ("atomic-group", rb"(?>a)"),
    ("recursion", rb"a(?R)?b"),
    ("conditionals", rb"(?(1)a|b)(a)?"),
    ("k-reset", rb"a\Kb"),
    ("control-verbs", rb"a(*FAIL)b"),
    ("unicode-properties", rb"\p{L}+"),
    ("named-groups", rb"(?P<x>a)"),
    ("free-spacing", rb"(?x) a b c"),
    ("callouts", rb"a(?C1)b"),
    ("span-reporting", rb"abc"),        # every engine that compiles reports a span; not a construct
    ("non-utf8-subject", rb"\x93[\x20-\x7e]*\x94"),  # a lone high byte, I-72's own witness shape
    ("captures", rb"(a)(b)"),
    ("true-end-anchor", rb"abc\z"),
]


def compile_one(adapter, testee_id, pattern_id, pattern):
    workdir = os.path.join(WORKDIR, testee_id)
    os.makedirs(workdir, exist_ok=True)
    cp = adapter.compile(testee_id, pattern_id, pattern, {}, 1, workdir)
    res = cp.get(_ad.FORM_PLAIN)
    return res


def census_witnesses(adapter, testee_id):
    print("== witness census: %s ==" % testee_id)
    caps = []
    for tag, pat in WITNESSES:
        res = compile_one(adapter, testee_id, "w-" + tag, pat)
        if res.outcome == "compiled":
            caps.append(tag)
            print("  %-24s COMPILED   %r" % (tag, pat))
        else:
            rclass, code = classify_refusal(res.diagnostic)
            print("  %-24s REFUSED    %r  [%s/%s] %s"
                 % (tag, pat, rclass, code, res.diagnostic))
    print("  -> capabilities satisfied: %s" % ", ".join(caps))
    print("  -> capabilities REFUSED:   %s"
         % ", ".join(t for t, _ in WITNESSES if t not in caps))
    return caps


def census_corpus(adapter, testee_id, subbench_root, label):
    sb = _sb.load(subbench_root)
    print("== corpus census: %s over %s (%d patterns) =="
         % (testee_id, label, len(sb.patterns)))
    n_ok, n_refused = 0, 0
    by_code = {}
    for p in sb.patterns:
        pat = sb.pattern_bytes(p.name)
        res = compile_one(adapter, testee_id, "c-" + p.name, pat)
        if res.outcome == "compiled":
            n_ok += 1
            print("  %-48s COMPILED" % p.name)
        else:
            n_refused += 1
            rclass, code = classify_refusal(res.diagnostic)
            by_code[code] = by_code.get(code, 0) + 1
            print("  %-48s REFUSED  [%s/%s] %s"
                 % (p.name, rclass, code, res.diagnostic))
    print("  -> %d/%d compiled, %d refused" % (n_ok, len(sb.patterns), n_refused))
    print("  -> refusal codes: %s"
         % (", ".join("%s x%d" % (k, v) for k, v in sorted(by_code.items()))
            or "none"))


def main():
    adapters = _ad.discover()
    adapter = adapters["re2"]
    for testee_id in ("re2-default", "re2-longest"):
        adapter.prepare(testee_id, WORKDIR)
        caps = census_witnesses(adapter, testee_id)
        print()
    for testee_id in ("re2-default",):  # longest_match cannot change WHAT compiles
        census_corpus(adapter, testee_id, os.path.join(REPO_ROOT, "bench",
                                                        "capability"),
                     "bench/capability@0.1")
        print()
        census_corpus(adapter, testee_id, os.path.join(REPO_ROOT, "bench",
                                                        "syntax"),
                     "bench/syntax@0.1")


if __name__ == "__main__":
    main()
