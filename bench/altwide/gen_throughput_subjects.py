#!/usr/bin/env python3
"""gen_throughput_subjects.py -- the wide-alternation sub-bench's large
subjects: `throughput/` (gitignored) + `manifest_throughput.tsv` (committed).

FOUR SUBJECTS, and the two axes they cross are DENSITY and SIZE, each held
fixed while the other moves:

  t-128k-clean    131072 B,    0 branch occurrences   density 0
  t-128k-sparse   131072 B,   16 occurrences          1 per 8 KB
  t-128k-dense    131072 B, 1024 occurrences          1 per 128 B
  t-512k-sparse   524288 B,   64 occurrences          1 per 8 KB (the size arm)

WHY DENSITY IS AN AXIS AT ALL. Under find-all search the engine restarts
after every match, so a subject's cost is (bytes scanned while failing) +
(matches x cost of a match). Those two are the two halves of what a wide
alternation does, and they scale differently with WIDTH: a backtracker's
failing scan pays per byte per branch, while its cost at a hit pays the
branch's INDEX; an automaton pays neither. `clean` isolates the failing
scan, `dense` puts a match every 128 bytes, and `sparse` at two sizes shows
whether the per-byte cost is flat in the subject length -- which is the
claim a `throughput` regime exists to test.

WHY 128 KB AND 512 KB RATHER THAN 1 MB. Arithmetic, stated so it can be
re-checked rather than believed (NOTES.md, "Cell-time estimate"). A
backtracker enters every branch at every candidate start: at width 2048
that is a few thousand operations per byte, so ONE pass over 1 MB is tens
of seconds and the harness's 20 s per-trial cap would bind on the widest
rungs of every backtracking testee -- five trials each, on eight patterns.
At 128 KB the median pass is ~1.5 s, the predicted sweep over all four
subjects is ~10 s, and the cap does not bind anywhere. The subjects are
still an order of magnitude above the 256 B search band and comfortably
above bench/bounded's own largest (64 KB), so the regime is doing its job.

WHICH BRANCHES OCCUR. `HIT_WORDS` cycles over sixteen words chosen so every
pattern in the set has some: one from each rung's exclusive range of the
`main` and `short` pools (word 0, 7, 255, 511, 1023, 2047; short 0, 2047,
4095) and two from each structure pool (index 0, inside the 64-wide rung,
and index 400, inside the 512-wide one only). A subject's occurrence count
is therefore a function of the PATTERN's width, which is exactly the number
`expectations.tsv`'s `nmatches` column then carries per rung.

Deterministic: SEED below, `altwidetext.Rng`, no clock, no environment; a
different seed from `gen_subjects.py` so a large subject is not a short
one's prose stretched. Every subject is drawn from the same branch-free
background guard and re-asserted here: the occurrence list of each finished
subject must be EXACTLY the words this file placed, at the offsets it
placed them.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import altwidetext as at  # noqa: E402

SEED = 20260902
OUT = os.path.join(HERE, "throughput")
MANIFEST = os.path.join(HERE, "manifest_throughput.tsv")

# (id, exact byte length, branch occurrences, description tail)
RUNS = (
    ("t-128k-clean",  131072,    0,
     "the failing scan alone: no branch of any pool occurs"),
    ("t-128k-sparse", 131072,   16,
     "one occurrence per 8 KB, each of the sixteen HIT_WORDS once"),
    ("t-128k-dense",  131072, 1024,
     "one occurrence per 128 B, each of the sixteen HIT_WORDS 64 times"),
    ("t-512k-sparse", 524288,   64,
     "the SIZE arm: 4x t-128k-sparse's bytes at t-128k-sparse's density"),
)


def hit_words(P):
    """The sixteen words the generator plants, in the order it cycles them.

    Every pattern in the set carries at least one: the `main` indices sit in
    each width rung's own exclusive range, the `short` ones in s-2048's and
    s-4096's, and each structure pool contributes index 0 (inside its 64-wide
    rung) and index 400 (inside the 512-wide rung only)."""
    return [P["main"][0], P["main"][7], P["main"][255], P["main"][511],
            P["main"][1023], P["main"][2047],
            P["short"][0], P["short"][2047], P["short"][4095],
            P["sh1"][0], P["sh1"][400], P["pfx3"][0],
            P["sfx"][0], P["sfx"][400], P["nar4"][0], P["nar4"][400]]


def build_one(rng, index, words, nbytes, nhits):
    """One subject: background tokens with `nhits` branch words planted at
    evenly spaced token positions, cut to exactly `nbytes`.

    The plant positions are computed from the finished token list rather
    than drawn, so the density is exact rather than expected. The cut can
    only REMOVE occurrences (truncation never manufactures a substring), and
    the last plant sits at 96 % of the tokens, so it never straddles the
    cut -- both facts are asserted by the occurrence check in `build()`."""
    tokens = []
    size = -1
    while size < nbytes + 64:
        t = at.background_token(rng, index)
        tokens.append(t)
        size += len(t) + 1
    if nhits:
        span = int(len(tokens) * 0.96) - 1
        for k in range(nhits):
            tokens[1 + (k * span) // nhits] = words[k % len(words)]
    return " ".join(tokens)[:nbytes]


def build():
    rng = at.Rng(SEED)
    P = at.pools()
    index = at.BranchIndex()
    words = hit_words(P)
    out = []
    for sid, nbytes, nhits, tail in RUNS:
        text = build_one(rng, index, words, nbytes, nhits)
        assert len(text) == nbytes, (sid, len(text))
        got = index.occurrences(text)
        assert len(got) == nhits, (sid, len(got), nhits)
        planted = {}
        for _off, w in got:
            planted[w] = planted.get(w, 0) + 1
        if nhits:
            assert set(planted) == set(words), (sid, sorted(planted))
            assert set(planted.values()) == {nhits // len(words)}, \
                (sid, sorted(planted.values()))
        out.append((sid, "run/prose %d B, %d branch occurrence(s) -- %s"
                    % (nbytes, nhits, tail), text))
    return out


def main():
    subjects = build()
    os.makedirs(OUT, exist_ok=True)
    rows = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, desc, text in subjects:
        b = text.encode("latin-1")
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(b)
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(b), hashlib.sha256(b).hexdigest(), desc,
            at.periodic_field(b)))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(rows) + "\n")
    print("gen_throughput_subjects: %d subjects (%d B) -> %s, manifest -> %s"
          % (len(subjects), sum(len(t) for _s, _d, t in subjects), OUT,
             MANIFEST))


if __name__ == "__main__":
    main()
