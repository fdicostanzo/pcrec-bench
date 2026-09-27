#!/usr/bin/env python3
"""gen_patterns.py -- `patterns/*.rx` for the literal-run sub-bench.

WHY THIS SET DOES NOT DRAW FROM AN `Rng`. Every other generator sub-bench
under `bench/` seeds a randomness primitive because its patterns or subjects
are typed from a VOCABULARY (log lines, word pools, prose). This set's whole
point is the opposite: each pattern is an EXPLICIT, NAMED construction with
one purpose (an alternation with literal tails, a wild-provenance secret
pattern, a bounded-length exact literal), so there is nothing here a draw
would help with, and inventing one would only make the pattern table harder
to read against pcrec's own I-113 ask. Determinism is total: this file
contains the whole answer, no seed, no clock, no environment.

    python3 bench/litrun/gen_patterns.py           # write
    python3 bench/litrun/gen_patterns.py --check    # re-derive + diff

FOURTEEN MEMBERS, in two groups plus the floor (NOTES.md has the full
rationale and the pcrec citations):

  * THE 2x2 SET (pcrec `docs/dev/lanes/s2a_report.md` S7.1): `alt-foo-tails`
    (a), `wild-secrets-aws-access-key-id` (a'), `ctrl-abc-dollar` (b),
    `wild-secrets-github-pat` (b') -- crossed, by the WINDOW plan (not this
    set), against {default, -fno-altcls-factor} x {default, -fno-lit-run}.
  * THE L-SWEEP (S7.2): `lit-l2` .. `lit-l40`, nine exact literals of length
    L = 2, 3, 4, 7, 8, 10, 16, 31, 40, each the first L bytes of the
    52-character alphabet `ascii_lowercase + ascii_uppercase` -- EVERY
    character in this alphabet is used at most once for L <= 40, so no
    literal here contains a repeated byte and no literal is a rotation of
    another (`check_no_internal_repeat` below asserts this at generation
    time, not by eye).
  * `floor` -- one literal byte, `#`, which occurs in NO other pattern's
    text and is the ONE byte `gen_throughput_subjects.py` uses to build the
    L-sweep's near-miss units (see that file's header): the floor pattern
    therefore reads as a real per-attempt cost on those subjects, not just
    a full-length miss.

`wild-secrets-aws-access-key-id` and `wild-secrets-github-pat` are copied
VERBATIM, byte for byte, from `bench/capability/patterns/` (I-113's own
naming) -- see `provenance.tsv` in this directory for the full chain back
to their ultimate source (rebar-wild's `noseyparker.txt`, Unlicense).
`ctrl-abc-dollar` (`abc$`) is the same pcre2-testdata pattern
`bench/capability`'s `wild-semdiv-dollar-trailing-newline-pcre2` already
carries verbatim (testinput1:1463); reused here as S7.1's control (b)
because ITS pattern text -- not a paraphrase -- is what the lane report
names.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import littext  # noqa: E402

OUT = os.path.join(HERE, "patterns")

# ALPHABET, L_SWEEP and FLOOR_BYTE live in littext.py -- the one place, also
# read by gen_subjects.py/gen_throughput_subjects.py/gen_pattern_facts.py,
# so this file and the subject generators can never disagree about what a
# literal's text is.
ALPHABET = littext.ALPHABET
L_SWEEP = littext.L_SWEEP
FLOOR_BYTE = littext.FLOOR_BYTE


def check_no_internal_repeat(name, lit):
    """Every L-sweep literal is drawn from a 52-DISTINCT-character alphabet,
    so no byte repeats within it and no rotation of it can equal itself --
    both properties `gen_throughput_subjects.py`'s tiling relies on for a
    provably exact match/mismatch count. Asserted here, at the source, so a
    future edit to ALPHABET that broke it would fail loudly at generation
    time rather than silently wrong an oracle-derived expectation."""
    if len(set(lit)) != len(lit):
        raise SystemExit("%s: literal %r repeats a byte" % (name, lit))


PATTERNS = {}

# ---- the 2x2 set (S7.1) ----------------------------------------------

# (a): the tails are not all literal ('.'), so no VM island can take the
# whole alternation -- S7.1's own reading is that lit-run's runs are
# `foo` (island-less alternation, `vm_alt`'s per-branch chain) plus
# whatever a factoring pass pulls out or leaves in place.
PATTERNS["alt-foo-tails"] = b"foo.x|foobar|foo."

# (a'): copied verbatim from bench/capability/patterns/
# wild-secrets-aws-access-key-id.rx -- see provenance.tsv.
PATTERNS["wild-secrets-aws-access-key-id"] = (
    b"\\b((?:A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)"
    b"[A-Z0-9]{16})\\b")

# (b), the control: no alternation, so `-fno-altcls-factor` must read null
# and only the lit-run column may move (S7.1's own reading). This is
# pcre2's own testdata pattern (testinput1:1463), same text
# bench/capability's wild-semdiv-dollar-trailing-newline-pcre2 carries.
PATTERNS["ctrl-abc-dollar"] = b"abc$"

# (b'): copied verbatim from bench/capability/patterns/
# wild-secrets-github-pat.rx -- see provenance.tsv.
PATTERNS["wild-secrets-github-pat"] = b"\\b(github_pat_[0-9a-zA-Z_]{82})\\b"

# ---- the L-sweep (S7.2) ------------------------------------------------

for _L in L_SWEEP:
    _lit = littext.literal(_L)
    check_no_internal_repeat("lit-l%d" % _L, _lit)
    PATTERNS["lit-l%d" % _L] = _lit

# ---- the floor ----------------------------------------------------------

PATTERNS["floor"] = FLOOR_BYTE

# Sanity: the floor byte appears in no other pattern's text (requirements
# 5's floor-pattern rule -- a floor hit on another member's text would be
# an accident of these bytes, not the design NOTES.md states).
for _name, _text in PATTERNS.items():
    if _name != "floor" and FLOOR_BYTE in _text:
        raise SystemExit("%s: contains the floor byte %r" % (_name, FLOOR_BYTE))

FLOOR_NAME = "floor"

# name -> (hazard_class, size_class, tags, role)
META = {
    "alt-foo-tails": ("wide-alternation", "tiny",
                       ["litrun", "2x2", "alt-tails", "cell-a"], "member"),
    "wild-secrets-aws-access-key-id": ("none", "small",
                       ["litrun", "2x2", "wild-secret", "cell-a-prime"],
                       "member"),
    "ctrl-abc-dollar": ("none", "tiny",
                       ["litrun", "2x2", "control", "cell-b"], "member"),
    "wild-secrets-github-pat": ("none", "small",
                       ["litrun", "2x2", "wild-secret", "control",
                        "cell-b-prime"], "member"),
    "floor": ("none", "tiny", ["floor", "control", "one-literal"], "floor"),
}
for _L in L_SWEEP:
    META["lit-l%d" % _L] = (
        "none", "tiny",
        ["litrun", "l-sweep", "exact-literal", "l-%d" % _L], "member")


def build():
    return {name: PATTERNS[name] for name in PATTERNS}


def write(patterns, out):
    os.makedirs(out, exist_ok=True)
    for name, text in patterns.items():
        with open(os.path.join(out, name + ".rx"), "wb") as f:
            f.write(text)


def check(patterns, out):
    bad = []
    for name, text in patterns.items():
        path = os.path.join(out, name + ".rx")
        if not os.path.exists(path):
            bad.append("%s: missing" % path)
            continue
        with open(path, "rb") as f:
            have = f.read()
        if have != text:
            bad.append("%s: committed %r != derived %r" % (path, have, text))
    have_names = {os.path.splitext(f)[0] for f in os.listdir(out)
                  if f.endswith(".rx")} if os.path.isdir(out) else set()
    extra = have_names - set(patterns)
    for name in sorted(extra):
        bad.append("%s.rx: committed but no longer derived" % name)
    return bad


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)

    patterns = build()

    if args.check:
        bad = check(patterns, args.out)
        if bad:
            print("gen_patterns --check: %d problem(s):" % len(bad),
                  file=sys.stderr)
            for b in bad:
                print("  " + b, file=sys.stderr)
            return 1
        print("gen_patterns --check: %d pattern(s) re-derive byte for byte"
              % len(patterns))
        return 0

    write(patterns, args.out)
    print("gen_patterns: %d pattern(s) -> %s" % (len(patterns), args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
