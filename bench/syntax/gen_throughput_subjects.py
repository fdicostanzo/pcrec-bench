#!/usr/bin/env python3
"""gen_throughput_subjects.py -- the syntax census's large subjects:
`throughput/` (gitignored) + `manifest_throughput.tsv` (committed).

THREE TEXTS, ONE GRAMMAR, A SIZE SWEEP: 64 KB, 256 KB and 1 MB of
newline-terminated lines drawn from censustext.py's line grammar -- eight
parts plain prose (one line in eight carries a doubled word, one in ten a
Latin-1 word, one word in twelve capitalised) to two parts order lines
(integer, date, time, address, price, hex) and one part each of tag lines
(one pair in six mis-closed), balanced paren expressions (one line in eight
left open), key=value lines in four spellings and quoted strings (one in
eight unterminated). Every construct in the set therefore has SPARSE hits
in every text -- the backreference's doubled words, the recursion's balanced
parens, the lookarounds' `item done`, the named backreference's tag pairs --
on a background where most candidate starts fail, which is the regime a
per-byte cost is read in.

WHY A SIZE SWEEP AND NOT A DENSITY CROSS. This is a census, not a
depth set: what it needs from the throughput regime is one per-byte number
per construct that can be read against `pcre2-jit`'s and against the floor,
and a second and third size to say whether that number is flat in the
subject length (a non-flat one is itself an outlier, NOTES.md "The outlier
rule"). Density is fixed by the grammar; a construct whose cost turns out to
hinge on hit density gets a depth probe of its own.

WHY 1 MB IS THE TOP. Nothing in this set is a backtracking hazard -- the
bodies are literal words, bounded repeats and single-class runs -- so an
interpreter's pass over 1 MB is tens of milliseconds for most patterns and
under a second for the backreference and recursion shapes, far inside the
harness's 20 s per-trial budget even at the calibrated iteration count. The
one shape held OUT of this set on purpose is an unbounded `.` repeat under
`(?s)`, which is quadratic on a 1 MB subject with no newline barrier.

Seeds differ per subject so the 256 KB text is not the 64 KB one's prefix
(a prefix would make the sweep read the same bytes three times). The
`periodic` column is computed, never assumed: the grammar has no fixed-
length repeating unit, and the manifest says so per subject.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import censustext as ct  # noqa: E402

OUT = os.path.join(HERE, "throughput")
MANIFEST = os.path.join(HERE, "manifest_throughput.tsv")

# (id, exact byte length, seed, description tail)
RUNS = (
    ("t-64k", 65536, 20260905, "the small run"),
    ("t-256k", 262144, 20260906, "4x the small run's bytes, its own draw"),
    ("t-1m", 1048576, 20260907, "16x the small run's bytes, its own draw"),
)


# [B123] syntax@0.2: the lka DENSITY PAIR, appended after the three 0.1 texts
# (the 0.1 rows and files are untouched, asserted below). Same size, same
# seed, same background, same `item`->` done` conditional (4 in 5); only the
# density of `item` differs: one word slot in three (match-dense: a call per
# match dominates) against one in 4096 (match-sparse: the per-byte scan
# dominates). pcrec I-124 item 2b / inbox I-127 [BENCH-ASKS-PENDING] (1).
LKA_BYTES = 262144
LKA_SEED = 20261025
LKA_PAIR = (
    ("t-lka-dense-256k", 1, 3, "match-dense"),
    ("t-lka-sparse-256k", 1, 4096, "match-sparse"),
)

# The 0.1 rows, byte for byte: 0.2 EXTENDS the manifest, it never re-draws it.
_0_1_SHA256 = {
    "t-64k": "2611159e8419e266c57b9b21714d1b34ec1cbcbd678aba320e0476ce1af2e658",
    "t-256k": "8b7ca5c5e32209bed1ee5ccce8b1f74141e25d0c092cd62a48b281f5be20be2d",
    "t-1m": "8b41f4bc9494eb4160d51a5ba030904e933b5c0798102c2d8a0c918111f09b63",
}


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, nbytes, seed, tail in RUNS:
        body = ct.text(seed, nbytes)
        assert len(body) == nbytes
        assert b"#" not in body, "the floor byte must not occur"
        assert hashlib.sha256(body).hexdigest() == _0_1_SHA256[sid], (
            "syntax@0.2 moved a 0.1 throughput text: %s" % sid)
        nlines = body.count(b"\n")
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
        desc = ("run/mixed %d B, %d lines of censustext.py's grammar -- %s"
                % (nbytes, nlines, tail))
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, nbytes, hashlib.sha256(body).hexdigest(), desc,
            ct.periodic_field(body)))
    counts = {}
    for sid, num, den, label in LKA_PAIR:
        body = ct.lka_text(LKA_SEED, LKA_BYTES, num, den)
        assert len(body) == LKA_BYTES
        assert b"#" not in body, "the floor byte must not occur"
        n_item, n_done = ct.lka_counts(body)
        counts[sid] = (n_item, n_done)
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
        desc = ("lka/%s %d B, seed %d, `item` planted at 1 word slot in %d, "
                "followed by ` done` 4 times in 5: %d `item`, %d `item done` "
                "(lka-pos matches %d, lka-neg %d) -- [B123] the density pair"
                % (label, LKA_BYTES, LKA_SEED, den, n_item, n_done, n_done,
                   n_item - n_done))
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(), desc,
            ct.periodic_field(body)))
    # the pair's contract, asserted: dense is >= 100x sparse in `item` AND in
    # matches; sparse still has at least one lka-pos and one lka-neg match
    # (a count of zero would make a per-match cost unreadable).
    (di, dd), (si, sd) = counts["t-lka-dense-256k"], counts["t-lka-sparse-256k"]
    assert di >= 100 * si and dd >= 100 * sd, counts
    assert sd >= 1 and si - sd >= 1, counts
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(rows) + "\n")
    print("gen_throughput_subjects: %d subjects (%d B) -> %s, manifest -> %s"
          % (len(RUNS) + len(LKA_PAIR),
             sum(r[1] for r in RUNS) + LKA_BYTES * len(LKA_PAIR), OUT,
             MANIFEST))
    return 0


if __name__ == "__main__":
    sys.exit(main())
