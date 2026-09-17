#!/usr/bin/env python3
"""docs/dev/measurements/probe_tre_capability_census.py -- the reproducing
script behind 2026-09-17-tre-capability-witness-census.txt.

Lane l6btre ([B7]/L6b, capability_set_v1.md 11.1): the TRE ADAPTER'S own
capability witness census, mandatory BEFORE the `ext bench` capability
matrix declares anything for `tre-default` -- the same L5 lesson
testees/onig/'s own census states ("three wrong first-cut declarations" on
the pcrec side, docs/dev/lanes/b42cap_report.md 2), and CS5 (this design
note's own open item: TRE's `named-groups`/`free-spacing` support must be
CITED or marked UNCONFIRMED, never assumed either way).

THREE PASSES, all through the REAL tre-default adapter (never a second
parser, never pcrecbench.subbench's own text without going through
Adapter.compile()/measure()):

  1. ONE ISOLATED WITNESS PER REQUIRES TOKEN (17 tokens,
     pcrecbench.capability.REQUIRES_VOCAB) -- a minimal pattern
     exercising exactly one construct, so a refusal is attributable to
     ONE token, not a confound of several. Several witnesses per token
     where a single one would not settle the question (lookaround's two
     directions; named-groups' two spellings).
  2. EVERY ONE OF bench/capability's 64 REAL corpus patterns -- the
     literal ask ("every one of the 64 bench/capability patterns"), and
     the check that the isolated-witness verdict actually holds on REAL,
     not synthetic, text.
  3. BEHAVIORAL CONFIRMATIONS, at MATCH grain (not just compile), for
     findings a bare compile/refuse verdict cannot show: TRE's real
     POSIX leftmost-longest convention (`a|ab` vs "ab"), the two SILENT
     MISPARSE hazards this lane found (`\\K` compiles as literal "K",
     `(*NAME)` compiles as a capturing group around literal "NAME" with
     the leading `*` silently dropped -- NEITHER refuses, both change
     the pattern's meaning without a diagnostic), non-greedy `+?`/`*?`
     genuinely taking effect (a real deviation from pure POSIX
     leftmost-longest once that syntax appears), the whole-subject
     `^(?:...)$` wrap's own anchoring correctness (matches exactly the
     right subjects, both directions), and the I-72 high-byte witness.

Run: python3 docs/dev/measurements/probe_tre_capability_census.py
(from the repo root; needs the `tre` adapter's driver, built on demand).
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
# note), verified in pass 3 rather than by a compile witness here.
WITNESSES = {
    "backrefs": [rb"(a)\1"],
    "lookaround": [rb"(?=a)a", rb"(?<=a)b"],
    "lookbehind-variable": [rb"(?<=a|bc)x"],
    "possessive-quantifier": [rb"a*+"],
    "atomic-group": [rb"(?>a*)b"],
    "recursion": [rb"(a(?R)?b)", rb"(a(?1)?b)", rb"(?<n>a(?&n)?b)",
                 rb"(a\g<1>?b)"],
    "conditionals": [rb"(?(1)a|b)(a)?"],
    "k-reset": [rb"a\Kb"],
    "control-verbs": [rb"a(*ACCEPT)b", rb"a(*FAIL)b", rb"a(*SKIP)b"],
    "unicode-properties": [rb"\p{L}", rb"\p{Alpha}"],
    "named-groups": [rb"(?<name>a)", rb"(?P<name>a)"],
    "free-spacing": [rb"(?x) a b c"],
    "callouts": [rb"a(?C1)b"],
    "true-end-anchor": [rb"a\z"],  # NOT this spelling for tre-default --
                                   # see pass 3's own `$`-based witness.
}


def compile_one(a, tmp, name, pat, form=ad.FORM_PLAIN):
    cp = a.compile("tre-default", name, pat, {}, 1, tmp)
    r = cp.get(form)
    return r.outcome, r.diagnostic


class _Subj:
    def __init__(self, sid, path, length):
        self.subject_id, self.path, self.length = sid, path, length


def match_one(a, tmp, name, pat, subj_bytes, form=ad.FORM_PLAIN):
    cp = a.compile("tre-default", name, pat, {}, 1, tmp)
    r = cp.get(form)
    if r.outcome != "compiled":
        return None, r.outcome, r.diagnostic
    spath = os.path.join(tmp, name + "-" + form + ".subj")
    with open(spath, "wb") as f:
        f.write(subj_bytes)
    # `whole-subject` is measured under `match` -- the ONLY regime the
    # driver's own cross-check accepts alongside that form (this file's
    # driver.c: "--mode and --form disagree"); `plain` uses `search_short`.
    regime = "match" if form == ad.FORM_WHOLE_SUBJECT else "search_short"
    rows, _info, _notes = a.measure(dict(r.handle), regime,
                                    [_Subj(name, spath, len(subj_bytes))],
                                    1, 1, timeout=30)
    return rows[0][0], r.outcome, None


def main():
    a = ad.discover(root=os.path.join(ROOT, "testees"))["tre"]
    tmp = tempfile.mkdtemp(prefix="tre-census-")
    a.prepare("tre-default", tmp)

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

    print()
    print("=== pass 3: behavioral confirmations (match grain) ===")

    def show(label, name, pat, subj, form=ad.FORM_PLAIN):
        row, outcome, diag = match_one(a, tmp, name, pat, subj, form)
        if row is None:
            print("%-46s %-14s %s" % (label, outcome, diag))
        else:
            print("%-46s answer=%-10s span=[%s,%s) caps=%s"
                 % (label, row.answer, row.start, row.end, row.caps))

    show("POSIX leftmost-longest: a|ab vs 'ab'",
        "conv1", rb"a|ab", b"ab")
    show("perl-first would answer [0,1) here",
        "conv1b", rb"a|ab", b"xab")
    show("K-RESET HAZARD: a\\Kb vs 'aKb' (expect literal K match)",
        "khaz1", rb"a\Kb", b"aKb")
    show("K-RESET HAZARD: a\\Kb vs 'ab' (expect NOMATCH -- proves no keep)",
        "khaz2", rb"a\Kb", b"ab")
    show("CONTROL-VERB HAZARD: a(*FAIL) vs 'aFAIL' (silent literal group)",
        "fhaz1", rb"a(*FAIL)", b"aFAIL")
    show("CONTROL-VERB HAZARD: a(*FAIL) vs 'a*FAIL' (NOT literal '*FAIL')",
        "fhaz2", rb"a(*FAIL)", b"a*FAIL")
    show("non-greedy a+? vs 'aaa' (expect [0,1), a REAL deviation)",
        "ng1", rb"a+?", b"aaa")
    show("greedy a+ vs 'aaa' (expect [0,3), the control)",
        "ng2", rb"a+", b"aaa")
    show("whole-subject wrap ^(?:ab)$ vs 'ab' (expect match)",
        "ws1", rb"ab", b"ab", form=ad.FORM_WHOLE_SUBJECT)
    show("whole-subject wrap ^(?:ab)$ vs 'xaby' (expect NOMATCH)",
        "ws2", rb"ab", b"xaby", form=ad.FORM_WHOLE_SUBJECT)
    show("whole-subject wrap vs trailing newline 'ab\\n' (expect NOMATCH, "
        "true end anchor)",
        "ws3", rb"ab", b"ab\n", form=ad.FORM_WHOLE_SUBJECT)
    # NOTE: the SHARED cross-engine I-72 witness
    # (`\x93[\x20-\x7e]*\x94`, tools/selfcheck.py's own PAT) is PCRE-style
    # regex SOURCE TEXT that relies on the ENGINE interpreting `\xHH` hex
    # escapes -- TRE has NO such escape at all (confirmed this lane,
    # docs/dev/research/2026-09-12-b42-engine-landscape.md (5) and this
    # census's own pass-1 evidence: a bare `\x93` compiles as literal
    # "x93", never byte 0x93). Feeding TRE that exact witness would test
    # TRE's escape-syntax GAP, not I-72's actual transport property (do
    # raw high pattern BYTES survive the adapter's file-based delivery
    # unmangled). This adapter's own I-72 witness is therefore the RAW
    # BYTES as a LITERAL pattern (no class, no escape) -- the same
    # property, without the confound.
    show("I-72 high-byte witness, LITERAL bytes (expect [0,7))",
        "hib", b"\x93hello\x94", b"\x93hello\x94")


if __name__ == "__main__":
    main()
