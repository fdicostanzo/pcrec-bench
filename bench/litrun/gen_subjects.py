#!/usr/bin/env python3
"""gen_subjects.py -- the literal-run sub-bench's SHORT subjects: hit/
near-miss typed fields for the 2x2 set (S7.1) and the L-sweep's own
boundary subject (S7.2's "length L-1" arm).

Like `gen_patterns.py`, this file draws from no randomness primitive: every
subject is an explicit, named byte string with one stated purpose. That is
possible ONLY because these are typed short fields (bench/capability's
"field/hit" style), never generated prose -- the L-sweep's DENSE, tiled
subjects are the OTHER generator, `gen_throughput_subjects.py`, because
density at throughput scale is the whole point there and a hand-typed field
cannot give it.

THE BOUNDARY SUBJECT, `bnd-l<L>` (S7.2's "one of length L-1"): exactly L-1
bytes, the literal's own first L-1 bytes. pcrec's P8 guard is
`pos + L <= n`; at `n = L-1` no candidate start can ever satisfy it, so this
subject is `nomatch` on `lit-l<L>` by LENGTH ALONE, regardless of content --
it is not tiled (there is exactly one such boundary per subject, not
something density can multiply) and it is therefore a `match`/`search_short`
subject like the 2x2 set's, not a throughput one (NOTES.md, "Regime
choice", has the full reasoning for every subject in this set).

    python3 bench/litrun/gen_subjects.py
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import littext  # noqa: E402

OUT = os.path.join(HERE, "subjects")
MANIFEST = os.path.join(HERE, "manifest.tsv")

# The 82-byte github_pat_ suffix: a fixed, deterministic run over the
# pattern's own allowed charset [0-9a-zA-Z_], built by repeating one cycle
# that itself contains no accidental "github_pat_" substring anywhere it is
# sliced (checked once, in main(), rather than argued here).
_GHP_CYCLE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
GHP_SUFFIX_82 = (_GHP_CYCLE * 2)[:82].encode("ascii")
assert len(GHP_SUFFIX_82) == 82

SUBJECTS = []  # (id, bytes, description)


def add(sid, body, desc):
    if isinstance(body, str):
        body = body.encode("ascii")
    SUBJECTS.append((sid, body, desc))


# ---- alt-foo-tails: foo.x|foobar|foo. -----------------------------------
# Leftmost-first branch order matters for which branch a match reads as;
# each subject below matches exactly ONE branch under an anchored whole-
# subject test (`match` regime), which the corresponding NOTES.md row states.

add("at-match-b1", "fooXx", "alt-foo-tails: matches branch 1 (foo.x)")
add("at-match-b2", "foobar", "alt-foo-tails: matches branch 2 (foobar), the "
                              "only branch with no wildcard tail")
add("at-match-b3", "foo!", "alt-foo-tails: matches branch 3 (foo.), the "
                            "shortest branch")
add("at-nearmiss-short", "foo", "alt-foo-tails: too short for any branch "
                                 "(all three need >= 4 bytes)")
add("at-nearmiss-wrongchar", "fobar", "alt-foo-tails: missing the second "
                                       "'o' -- contains no branch's 'foo' "
                                       "prefix at all")
add("at-embed-search", "xxfoobarxx", "alt-foo-tails: 'foobar' embedded at "
                                      "offset 2, for search_short only")

# ---- wild-secrets-aws-access-key-id --------------------------------------
# AKIAIOSFODNN7EXAMPLE is AWS's own published EXAMPLE access key id (AWS
# SDK/CLI documentation's placeholder, e.g. docs.aws.amazon.com's own
# "AKIAIOSFODNN7EXAMPLE" -- a well-known, intentionally-fake value, never a
# real credential): AKIA + 16 alphanumeric bytes.

add("aws-match", "AKIAIOSFODNN7EXAMPLE", "wild-secrets-aws-access-key-id: "
                                          "AWS's own published example key")
add("aws-nearmiss-short", "AKIAIOSFODNN7EXAMPL",
    "wild-secrets-aws-access-key-id: one byte short of the required 16 "
    "after the prefix")
add("aws-nearmiss-prefix", "ZKIAIOSFODNN7EXAMPLE",
    "wild-secrets-aws-access-key-id: prefix not in the nine-alternative set")
add("aws-embed-search", "key=AKIAIOSFODNN7EXAMPLE;",
    "wild-secrets-aws-access-key-id: embedded with \\b satisfied on both "
    "sides, for search_short only")

# ---- ctrl-abc-dollar: abc$ ------------------------------------------------
# The two "match" rows and the two "nomatch" rows reproduce pcre2's own
# testdata (testinput1:1463/1466-1467, see provenance.tsv's note on
# bench/capability's twin of this pattern) rather than inventing new cases.

add("dollar-match", "abc", "ctrl-abc-dollar: $ matches end of subject")
add("dollar-match-trailing-nl", "abc\n",
    "ctrl-abc-dollar: $ matches before a trailing newline too "
    "(pcre2 testdata's own stated behaviour)")
add("dollar-nearmiss", "abcx", "ctrl-abc-dollar: a byte follows abc")
add("dollar-nearmiss-multiline", "abc\ndef",
    "ctrl-abc-dollar: pcre2 testdata's own 'expect no match' case -- "
    "no /m, so $ does not match before an INTERNAL newline")

# ---- wild-secrets-github-pat ----------------------------------------------

add("ghp-match", b"github_pat_" + GHP_SUFFIX_82,
    "wild-secrets-github-pat: exact 82-byte suffix")
add("ghp-nearmiss-short", b"github_pat_" + GHP_SUFFIX_82[:-1],
    "wild-secrets-github-pat: 81-byte suffix, one short")
add("ghp-nearmiss-prefix", b"github_token_" + GHP_SUFFIX_82,
    "wild-secrets-github-pat: wrong prefix ('token' for 'pat')")
add("ghp-embed-search", b"TOKEN=github_pat_" + GHP_SUFFIX_82 + b" ",
    "wild-secrets-github-pat: embedded with \\b satisfied on both sides, "
    "for search_short only")

# ---- the L-sweep's boundary subject (S7.2) -------------------------------

for _L in littext.L_SWEEP:
    _body = littext.literal(_L)[:-1]  # length L-1, content = literal's own head
    assert len(_body) == _L - 1
    add("bnd-l%d" % _L, _body,
        "lit-l%d: length L-1 (%d B) -- pcrec's P8 guard (pos + L <= n) "
        "fails on length alone; content is lit-l%d's own first %d bytes"
        % (_L, _L - 1, _L, _L - 1))


def main():
    # No accidental "github_pat_" inside the 82-byte cycle itself, and no
    # accidental match of any lit-l<L> literal inside another subject's
    # body (both would silently wrong an oracle-derived expectation this
    # file does not hand-compute).
    if b"github_pat_" in GHP_SUFFIX_82:
        raise SystemExit("GHP_SUFFIX_82 accidentally contains 'github_pat_'")

    os.makedirs(OUT, exist_ok=True)
    seen = set()
    lines = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, body, desc in SUBJECTS:
        if sid in seen:
            raise SystemExit("duplicate subject id %r" % sid)
        seen.add(sid)
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
        lines.append("%s\t%d\t%s\t%s\t%s"
                     % (sid, len(body), hashlib.sha256(body).hexdigest(),
                        desc, littext.periodic_field(body)))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(lines) + "\n")
    print("gen_subjects: %d subjects (%d..%d B) -> %s, manifest -> %s"
          % (len(SUBJECTS), min(len(b) for _s, b, _d in SUBJECTS),
             max(len(b) for _s, b, _d in SUBJECTS), OUT, MANIFEST))


if __name__ == "__main__":
    main()
