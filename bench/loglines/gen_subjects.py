#!/usr/bin/env python3
"""gen_subjects.py -- the log-line sub-bench's 112 search-band subjects.

Each subject is a CHUNK OF WHOLE LINES of mixed-format log text, 256 B - 4 KB
(the band this sub-bench declares as `short_search_max_bytes`; requirements 3
names "~256-byte subjects, log lines, fields" and this sub-bench is the log
lines, at the sizes a log-shipper actually hands a matcher).

THE CONSTRUCTION, and what it is a construction OF. The background grammar
(`logtext.py`) emits lines that no member pattern matches, full of near-misses
(12-hex ids where the pattern wants 32, three-part versions where it wants a
dotted quad, BSD/klog timestamps where it wants ISO-8601). Each subject then
draws a small set of FEATURES, and each drawn feature injects one real line
(or, for `stack-frame`, a real block) carrying that shape. The draw
probabilities are what set the match rate, and they are set LOW on purpose:
this sub-bench exists to measure the FAILING path (inbox I-7 1, pcrec
[OPT-5]), so ~90 % of the (pattern, subject) cells are `nomatch` and the
number it produces is the cost of establishing that.

That is a deliberate construction of the failing regime, not a claim about
how often ISO timestamps occur in the field. It IS a claim that the failing
text is realistic and stays interesting to the engine all the way to the end
of the subject -- which the near-misses are what buy.

DETERMINISM: seed SEED below, `logtext.Rng` (getrandbits only), no clock, no
environment. Re-running reproduces the identical files and manifest.

THE MANIFEST carries the harness contract's four columns plus `periodic`
(inbox I-10): the smallest period in 1..4096 bytes, or `no`. Every subject
here is `no` by construction and the column proves it per subject rather than
this docstring claiming it for all of them.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import logtext  # noqa: E402

SEED = 20260828
OUT = os.path.join(HERE, "subjects")
MANIFEST = os.path.join(HERE, "manifest.tsv")

# Four size bands x 28 subjects. The band is drawn as a TARGET; lines are
# appended until the target is reached, so the realised size is the target
# plus the tail of one line, and never exceeds 4096 (the top band's target
# leaves room for the longest line the grammar can emit).
BANDS = ((256, 512), (512, 1024), (1024, 2048), (2048, 3800))
PER_BAND = 28
MAX_BYTES = 4096

# HOW MANY of the 112 subjects carry each shape -- a COUNT, drawn without
# replacement, not a per-subject coin flip.
#
# The first cut used independent Bernoulli draws and the realised rates moved
# by a factor of four between retunes (`kv-quoted` came out 3/112 on one
# setting and 12/112 on the next, from draws of 45 and 55 per mille): at
# n = 112 the sampling noise is wider than the band the set is meant to sit
# in, so the match rate would have been an accident of the seed rather than a
# property of the set. Exact allocation makes m/n a DESIGNED number that
# NOTES.md states and the oracle then confirms.
#
# The one CORRELATION, deliberate and stated in NOTES.md: `http-5xx` injects
# an access line and an access line carries an IPv4 client, so `ipv4`'s
# realised count is the UNION of its own subjects and `http-5xx`'s -- which is
# why its own count is the smallest here. `stack-frame`'s block opens with an
# ERROR line, but with no context word, so it does not feed `level-context`.
COUNTS = (
    ("iso-ts", 8),
    ("ipv4", 3),
    ("ipv6", 7),
    ("kv-quoted", 8),
    ("level-context", 8),
    ("http-5xx", 7),
    ("uuid", 8),
    ("hex32-id", 8),
    ("bignum", 8),
    ("stack-frame", 7),
)


def choose(rng, n, k):
    """k distinct indices out of n, by a Fisher-Yates shuffle over
    `Rng.below` -- the module's one primitive; `random.sample`'s internals
    are not stable across CPython versions and a committed manifest is."""
    idx = list(range(n))
    for i in range(n - 1, 0, -1):
        j = rng.below(i + 1)
        idx[i], idx[j] = idx[j], idx[i]
    return sorted(idx[:k])


def build_chunk(rng, target, max_bytes=MAX_BYTES, features=()):
    """One subject of `target` bytes (plus the tail of one line), features
    INCLUDED in the budget.

    The feature blocks are drawn FIRST and their bytes counted against the
    target, so a subject that carries a five-line stack trace is not a
    different size class from one that carries nothing: the band is a
    property of the subject, and a size sweep whose sizes move with the
    match rate would confound the two."""
    blocks = [logtext.feature_line(rng, f) for f in features]
    size = sum(len(x) + 1 for blk in blocks for x in blk)
    lines = []
    while size < target:
        line = logtext.background(rng)
        if size + len(line) + 1 > max_bytes:
            break
        lines.append(line)
        size += len(line) + 1
    for blk in blocks:
        at = rng.below(len(lines) + 1)
        lines[at:at] = blk
    return ("\n".join(lines) + "\n").encode("latin-1")


def build():
    rng = logtext.Rng(SEED)
    n = len(BANDS) * PER_BAND
    assigned = [[] for _ in range(n)]
    for name, k in COUNTS:
        for i in choose(rng, n, k):
            assigned[i].append(name)
    subjects = []
    for band, (lo, hi) in enumerate(BANDS):
        for j in range(PER_BAND):
            target = rng.between(lo, hi)
            feats = assigned[band * PER_BAND + j]
            body = build_chunk(rng, target, features=feats)
            desc = ("%d-%d B band, %d lines, %s"
                    % (lo, hi, body.count(b"\n"),
                       ("shapes: " + "+".join(feats)) if feats
                       else "background only (no shape injected)"))
            subjects.append((desc, body))
    return subjects


def main():
    subjects = build()
    os.makedirs(OUT, exist_ok=True)
    lines = ["id\tlen\tsha256\tdescription\tperiodic"]
    for i, (desc, b) in enumerate(subjects):
        sid = "s-%03d" % i
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(b)
        lines.append("%s\t%d\t%s\t%s\t%s"
                     % (sid, len(b), hashlib.sha256(b).hexdigest(), desc,
                        logtext.periodic_field(b)))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(lines) + "\n")
    total = sum(len(b) for _d, b in subjects)
    print("gen_subjects: %d subjects (%d B, %d..%d) -> %s, manifest -> %s"
          % (len(subjects), total, min(len(b) for _d, b in subjects),
             max(len(b) for _d, b in subjects), OUT, MANIFEST))


if __name__ == "__main__":
    main()
