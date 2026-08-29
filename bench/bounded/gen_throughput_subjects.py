#!/usr/bin/env python3
"""gen_throughput_subjects.py -- the bounded-repeat sub-bench's LARGE runs:
`throughput/` (gitignored) + `manifest_throughput.tsv` (committed).

Four subjects, and why they are here rather than in `subjects/`:

  t-letters-004k   4096 random lowercase letters   `[a-z]{0,4096}` at its full count
  t-letters-016k  16384 random lowercase letters   `[a-z]{0,16384}` / `{16384}` / `{0,16384}?` / `{4096,}` at theirs
  t-letters-064k  65536 random lowercase letters   `[a-z]{0,65535}` at PCRE2's own count ceiling, with one byte over
  t-digits-016k   16384 random digits              the nested rungs (`(?:\\d{1,64}){1,64}` = 4096, `nest3-16` = 4096) at theirs, repeatedly

They exercise the count ladder's LARGE rungs at match time -- the row
[ENG-COUNT] (inbox I-17 (c): "large DFA-side counts like `[a-z]{0,30000}`
would find their measured need here if one exists") wants -- and they do it
under find-all SEARCH rather than whole-subject MATCH for two reasons:

  1. The harness calibrates a regime's loop on its MEDIAN subject and caps a
     trial's predicted sweep at 20 s (`harness.py`). A 16 KB run in the
     `match` set, whose median subject is ~40 B, is 400x the median, so
     every length-proportional pattern's match trial would hit the cap: 13
     patterns x 5 trials x 20 s before anything else. In their own regime
     the median IS a 16 KB run and the four subjects cost ~0.3 s a trial.
  2. A near-miss beyond a NESTED rung's maximum is catastrophic for a
     backtracker (boundedtext.py's header; NOTES.md "The runs and the
     oracle"), and whole-subject match on a 16 KB digit run is exactly that
     for `nest2-16` (max 256). Under find-all search there is no end anchor:
     each match takes the greedy maximum and succeeds at once, so a 16 KB
     digit run is 64 matches of `nest2-16` and 4 of `nest2-64`, every one of
     them the counter run to its top -- which is the number wanted.

What is NOT here: a size sweep. This set's give-up axis is the COUNT in the
pattern (NOTES.md, "Regimes"), and the sizes are chosen to sit on the
ladder's rungs, not an octave apart for their own sake.

Deterministic: SEED below, `boundedtext.Rng`, no clock, no environment; a
different seed from `gen_subjects.py` so the 4 KB run is not the 256 B
run's prefix stretched. Every subject is drawn non-periodic (gen_subjects
.nonperiodic) and the manifest's `periodic` column proves it per subject.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import boundedtext as bt          # noqa: E402
from gen_subjects import nonperiodic  # noqa: E402

SEED = 20260830
OUT = os.path.join(HERE, "throughput")
MANIFEST = os.path.join(HERE, "manifest_throughput.tsv")

RUNS = (
    ("t-letters-004k", "letters", 4096,
     "run/letters: 4096 random lowercase letters -- `[a-z]{0,4096}` at its full count"),
    ("t-letters-016k", "letters", 16384,
     "run/letters: 16384 random lowercase letters -- the 16384 rungs (`{0,n}`, `{n}`, `{0,n}?`) at their full count, `{4096,}` past its minimum"),
    ("t-letters-064k", "letters", 65536,
     "run/letters: 65536 random lowercase letters -- `[a-z]{0,65535}` at PCRE2's count ceiling with one byte left over"),
    ("t-digits-016k", "digits", 16384,
     "run/digits: 16384 random digits -- the nested rungs at their full count, 64x / 4x / 4x over the run"),
)


def build():
    rng = bt.Rng(SEED)
    out = []
    for sid, kind, n, desc in RUNS:
        draw = (lambda r, n=n: r.letters(n)) if kind == "letters" else (lambda r, n=n: r.digits(n))
        out.append((sid, desc, nonperiodic(rng, draw)))
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
            sid, len(b), hashlib.sha256(b).hexdigest(), desc, bt.periodic_field(b)))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(rows) + "\n")
    print("gen_throughput_subjects: %d subjects (%d B) -> %s, manifest -> %s"
          % (len(subjects), sum(len(t) for _s, _d, t in subjects), OUT, MANIFEST))


if __name__ == "__main__":
    main()
