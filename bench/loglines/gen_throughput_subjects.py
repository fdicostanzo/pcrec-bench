#!/usr/bin/env python3
"""gen_throughput_subjects.py -- the log-line sub-bench's SIZE SWEEP.

Eight subjects: 16 KB, 64 KB, 256 KB and 1 MB, each in two flavours, from the
same grammar the 256 B - 4 KB search band is drawn from (`logtext.py`).

  `t-<size>-fail`  BACKGROUND ONLY. No member pattern matches it anywhere --
                   the oracle says so in `expectations.tsv`, and that is the
                   subject this sub-bench exists for: it is the direct
                   analogue of bench/email's `t-b-no-at`, the row where
                   pcre2-interp dismissed a whole 1 MB subject at memchr speed
                   because its required code unit was absent while pcrec's DFA
                   scanned every byte (inbox I-7 1). Here the required units
                   DIFFER per pattern -- `.` and `:` are structural in log
                   text and present in every one of these subjects, `-`, `"`
                   and `)` are not -- so the same set of failing subjects
                   carries BOTH cases, and `pattern_facts.tsv` says which
                   pattern is in which.
  `t-<size>-hit`   The same background with every shape injected, spread
                   through the chunk: the matching-bearing counterpart, so a
                   per-byte cost on failing text has a matching-text number
                   from the same size and the same grammar to read against.

WHY A SWEEP AND NOT ONE SIZE (inbox I-2 1b). A give-up is a first-class
outcome, and the number owed is the SIZE AT WHICH IT FIRST FIRES for each
testee. One subject size can only say "gave up" or "did not"; four sizes an
octave apart bracket it. Nothing here is expected to give up -- the member
patterns are bounded shapes -- so an observed give-up is a finding, and the
sweep is what makes it a locatable one.

Deterministic: SEED below, `logtext.Rng`, no clock, no environment. The seed
differs from `gen_subjects.py`'s so the sweep is not a re-run of the search
band's first lines at four lengths.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import logtext  # noqa: E402

SEED = 20260829
OUT = os.path.join(HERE, "throughput")
MANIFEST = os.path.join(HERE, "manifest_throughput.tsv")

SIZES = (("016k", 16 * 1024), ("064k", 64 * 1024),
         ("256k", 256 * 1024), ("1024k", 1024 * 1024))

# One instance of every shape per this many bytes, in the `hit` subjects.
# 4 KB keeps the shapes sparse enough that the text between them is still the
# failing text the sub-bench is about (a `hit` subject where every other line
# matched would measure the match path, which is the other sub-bench's job).
HIT_SPACING = 4096


def fill(rng, target, features_every=None):
    """Background lines to `target` bytes; if `features_every` is set, one
    line of every shape spliced in after each block of that many bytes."""
    out = []
    size = 0
    next_inject = features_every
    while size < target:
        line = logtext.background(rng)
        out.append(line)
        size += len(line) + 1
        if features_every and size >= next_inject:
            for feat in logtext.FEATURES:
                block = logtext.feature_line(rng, feat)
                out.extend(block)
                size += sum(len(x) + 1 for x in block)
            next_inject = size + features_every
    return ("\n".join(out) + "\n").encode("latin-1")


def build():
    rng = logtext.Rng(SEED)
    subjects = []
    for label, nbytes in SIZES:
        subjects.append(
            ("t-%s-fail" % label,
             "%d KB of background log text, NO member shape anywhere (the "
             "failing path; the analogue of bench/email's t-b-no-at)"
             % (nbytes // 1024),
             fill(rng, nbytes)))
        subjects.append(
            ("t-%s-hit" % label,
             "%d KB of the same log text with one instance of every member "
             "shape per %d B (the matching-bearing counterpart)"
             % (nbytes // 1024, HIT_SPACING),
             fill(rng, nbytes, features_every=HIT_SPACING)))
    return subjects


def main():
    subjects = build()
    os.makedirs(OUT, exist_ok=True)
    lines = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, desc, buf in subjects:
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(buf)
        lines.append("%s\t%d\t%s\t%s\t%s"
                     % (sid, len(buf), hashlib.sha256(buf).hexdigest(), desc,
                        logtext.periodic_field(buf)))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(lines) + "\n")
    print("gen_throughput_subjects: %d subjects (%s) -> %s, manifest -> %s"
          % (len(subjects), ", ".join("%d B" % len(b) for _s, _d, b in subjects),
             OUT, MANIFEST))


if __name__ == "__main__":
    main()
