#!/usr/bin/env python3
r"""probe_rust_capability_census.py -- ([B7]/L6b, testees/rust/, lane
l6brust) THE RUST-REGEX CAPABILITY WITNESS CENSUS.

NOT YET RUN (BOILERPLATE.md's HARD RULE: authored while pcrec's I-75
battery holds the box, cargo/rustup install and every real compile
deferred until the trailer shows DONE -- see this lane's report). Written
now, ready to run unmodified once the box frees, so the capability
declaration this script exists to produce is never typed ahead of a real
witness (the L5 lesson, `bench/capability/gen_patterns.py`'s own
`EXT_BENCH_ROSTER` comment: "witnessed compiles/refusals, never
documentation").

Same shape as `probe_re2_capability_census.py` / `probe_onig_capability_
census.py` / `probe_vectorscan_capability_census.py`:

  1. one (or, where one spelling would not settle the question, several)
     minimal witness per `REQUIRES_VOCAB` token, through the REAL
     `testees/rust/adapter.py` `compile()` path;
  2. every one of `bench/capability@0.1`'s 64 canonical patterns;
  3. every one of `bench/syntax@0.1`'s 95 canonical patterns, "as
     available" (the second-corpus cross-check other L6b lanes ran).

A DELIBERATE OPEN QUESTION this script is built to resolve, not assume
(see testees/rust/CLAUDE.md's "non-utf8-subject: TWO WITNESSES, ONE
UNRESOLVED" section for the full reasoning): the `regex` crate's
`unicode(bool)` toggle (default true, ON for `rust-default`, needed for
`unicode-properties`) may make `\xHH` and a `[\x80-\xff]`-style class
match the UTF-8 ENCODING of that codepoint (e.g. `\x93` -> the two-byte
sequence C2 93) rather than the single raw byte -- which would mean this
engine's byte-level `non-utf8-subject` claim and its `unicode-properties`
claim are NOT simultaneously free the way RE2's `EncodingLatin1` or
Oniguruma's `ONIG_ENCODING_ASCII` make them. `WITNESS_NONUTF8_CLASS_RAW`
and `WITNESS_NONUTF8_CLASS_INLINE_BYTE` below are two DIFFERENT
candidate patterns for the SAME subject, matched against the SAME raw
high-byte subject, specifically to settle this by a real match run (not
merely a compile) before the token is declared either way.
"""
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, REPO_ROOT)

from pcrecbench import adapters as _ad          # noqa: E402
from pcrecbench import subbench as _sb          # noqa: E402
from testees.rust.adapter import classify_refusal  # noqa: E402

WORKDIR = os.path.join(REPO_ROOT, "build", "work", "rust-census")
TESTEE = "rust-default"

# One minimal witness per REQUIRES_VOCAB token (docs/design/
# capability_set_v1.md 5.1's 17-token vocabulary). PCRE-spelling witnesses
# reused verbatim from testees/re2/probe_re2_capability_census.py where
# the construct is a PCRE/Perl extension neither engine has, for direct
# cross-engine comparability (the same discipline testees/re2's own
# script states).
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
    ("span-reporting", rb"abc"),   # every engine that compiles reports a span
    # non-utf8-subject: the ASCII-escape witness other L6b censuses use.
    # See this file's header -- under `unicode(true)` this MAY compile to
    # match the UTF-8 ENCODING of U+0093, not the raw byte. Read the
    # actual MATCH result against a raw-byte subject below, not just
    # whether this compiles.
    ("non-utf8-subject", rb"\x93[\x20-\x7e]*\x94"),
    ("captures", rb"(a)(b)"),
    ("true-end-anchor", rb"abc\z"),
]

# The non-utf8-subject DISCRIMINATION PAIR (this file's header): both
# patterns are run against BOTH a raw-single-high-byte subject and a
# UTF-8-encoded-codepoint subject, so the census reads which byte shape
# each spelling actually matches, rather than assuming from the crate's
# documented semantics alone.
SUBJ_RAW_HIGH_BYTE = b"\x93hello\x94"                # 0x93 ... 0x94, literal bytes
SUBJ_UTF8_ENCODED = "hello".encode("utf-8")  # C2 93 ... C2 94
WITNESS_NONUTF8_CLASS = rb"[\x80-\xff]{1,4}"          # bench/capability's own high-byte-run shape
WITNESS_NONUTF8_INLINE_BYTE = rb"(?-u:[\x80-\xff]){1,4}"  # per-expression unicode OFF, if supported


def compile_one(adapter, testee_id, pattern_id, pattern, form=_ad.FORM_PLAIN):
    workdir = os.path.join(WORKDIR, testee_id)
    os.makedirs(workdir, exist_ok=True)
    cp = adapter.compile(testee_id, pattern_id, pattern, {}, 1, workdir)
    return cp.get(form)


def census_witnesses(adapter, testee_id):
    print("== witness census: %s ==" % testee_id)
    caps = []
    for tag, pat in WITNESSES:
        res = compile_one(adapter, testee_id, "w-" + tag, pat)
        if res.outcome == "compiled":
            caps.append(tag)
            print("  %-24s COMPILED   %r" % (tag, pat))
        else:
            rclass, name = classify_refusal(res.diagnostic)
            print("  %-24s REFUSED    %r  [%s/%s] %s"
                 % (tag, pat, rclass, name, res.diagnostic))
    print("  -> capabilities satisfied (compile-only pass): %s"
         % ", ".join(caps))
    print("  -> capabilities REFUSED:   %s"
         % ", ".join(t for t, _ in WITNESSES if t not in caps))
    return caps


def match_one(adapter, testee_id, pattern_id, pattern, subject_bytes):
    """Compile-and-match a single pattern against a single subject
    through the REAL driver (never the compile-only path alone) --
    needed for the non-utf8-subject discrimination, which is a MATCH
    question, not a compile one."""
    import tempfile
    workdir = os.path.join(WORKDIR, testee_id)
    os.makedirs(workdir, exist_ok=True)
    cp = adapter.compile(testee_id, pattern_id, pattern, {}, 1, workdir)
    res = cp.get(_ad.FORM_PLAIN)
    if res.outcome != "compiled":
        return None, res
    tmp = tempfile.mkdtemp(prefix="rust-census-subj-")
    subj_path = os.path.join(tmp, "s.bin")
    with open(subj_path, "wb") as f:
        f.write(subject_bytes)

    class S:
        subject_id, path, length = "s", subj_path, len(subject_bytes)

    rows, _i, _n = adapter.measure(dict(res.handle), "search_short", [S()],
                                   1, 1, timeout=60)
    return rows[0][0], res


def census_nonutf8_discrimination(adapter, testee_id):
    print("== non-utf8-subject discrimination: %s ==" % testee_id)
    for label, pat in (("class \\x80-\\xff", WITNESS_NONUTF8_CLASS),
                       ("(?-u:...) class", WITNESS_NONUTF8_INLINE_BYTE)):
        for subj_label, subj in (("raw high byte (0x93...0x94)",
                                  SUBJ_RAW_HIGH_BYTE),
                                 ("UTF-8-encoded codepoint (C2 93...C2 94)",
                                  SUBJ_UTF8_ENCODED)):
            row, res = match_one(adapter, testee_id,
                                 "nu-%s-%s" % (label, subj_label), pat, subj)
            if row is None:
                print("  %-20s vs %-40s REFUSED TO COMPILE  %s"
                     % (label, subj_label, res.diagnostic))
            else:
                print("  %-20s vs %-40s %s  start=%s end=%s"
                     % (label, subj_label, row.answer, row.start, row.end))


def census_corpus(adapter, testee_id, subbench_root, label):
    sb = _sb.load(subbench_root)
    print("== corpus census: %s over %s (%d patterns) =="
         % (testee_id, label, len(sb.patterns)))
    n_ok, n_refused = 0, 0
    by_name = {}
    for p in sb.patterns:
        pat = sb.pattern_bytes(p.name)
        res = compile_one(adapter, testee_id, "c-" + p.name, pat)
        if res.outcome == "compiled":
            n_ok += 1
            print("  %-48s COMPILED" % p.name)
        else:
            n_refused += 1
            rclass, name = classify_refusal(res.diagnostic)
            by_name[name] = by_name.get(name, 0) + 1
            print("  %-48s REFUSED  [%s/%s] %s"
                 % (p.name, rclass, name, res.diagnostic))
    print("  -> %d/%d compiled, %d refused" % (n_ok, len(sb.patterns), n_refused))
    print("  -> refusal variants: %s"
         % (", ".join("%s x%d" % (k, v) for k, v in sorted(by_name.items()))
            or "none"))


def main():
    adapter = _ad.discover()["rust"]
    adapter.prepare(TESTEE, WORKDIR)
    census_witnesses(adapter, TESTEE)
    print()
    census_nonutf8_discrimination(adapter, TESTEE)
    print()
    census_corpus(adapter, TESTEE, os.path.join(REPO_ROOT, "bench",
                                                "capability"),
                 "bench/capability@0.1")
    print()
    census_corpus(adapter, TESTEE, os.path.join(REPO_ROOT, "bench",
                                                "syntax"),
                 "bench/syntax@0.1")


if __name__ == "__main__":
    main()
