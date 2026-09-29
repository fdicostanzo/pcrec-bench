#!/usr/bin/env python3
"""gen_throughput_subjects.py -- the log-line sub-bench's SIZE SWEEP.

Twelve subjects: 16 KB, 64 KB, 256 KB and 1 MB, each in three flavours, from
the same grammar the 256 B - 4 KB search band is drawn from (`logtext.py`).

  `t-<size>-fail`  MIXED background, BACKGROUND ONLY. No member pattern
                   matches it anywhere -- the oracle says so in
                   `expectations.tsv`. This is the failing path with the
                   precheck UNAVAILABLE: every required code unit in this set
                   (`:` `.` `-` `"` `)` and a digit) occurs in mixed log text,
                   so no testee can dismiss these subjects without scanning
                   them, and what they measure is raw failing-scan cost.
  `t-<size>-hit`   The same background with every shape injected, spread
                   through the chunk: the matching-bearing counterpart, so a
                   per-byte cost on failing text has a matching-text number
                   from the same size and the same grammar to read against.
  `t-<size>-syslog` A SINGLE-SOURCE BSD-syslog stream, also failing, and the
                   one flavour that carries the memchr-dismissal case: it
                   contains no `"` and no `)`, which are exactly the required
                   code units of `kv-quoted` and `stack-frame`, so those two
                   patterns can be dismissed on it without a scan while the
                   other eight cannot. MEASURED and added after the first cut:
                   on MIXED log text every required byte in this set is
                   present (`:` `.` `-` and digits are structural), so the
                   `-fail` subjects alone could not be the analogue of
                   bench/email's `t-b-no-at` -- they are the case where BOTH
                   engines must scan. Both cases are wanted; the pair is what
                   separates "the precheck was unavailable" from "the precheck
                   was available and this is what it bought".

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
import argparse
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import logtext  # noqa: E402

SEED = 20260829
OUT = os.path.join(HERE, "throughput")
MANIFEST = os.path.join(HERE, "manifest_throughput.tsv")

#: [B115]: not used by the PROFILED split (the throughput/search bands are
#: both TIMED regimes and O-72 Q1 rules out training on one to test the
#: other) but given its own constant, distinct from both committed seeds and
#: from gen_subjects.py's TRAIN_SEED, for symmetry and so a future PROFILED
#: throughput arm has a value ready rather than an ad hoc one.
TRAIN_SEED = 20260931

SIZES = (("016k", 16 * 1024), ("064k", 64 * 1024),
         ("256k", 256 * 1024), ("1024k", 1024 * 1024))

# One instance of every shape per this many bytes, in the `hit` subjects.
# 4 KB keeps the shapes sparse enough that the text between them is still the
# failing text the sub-bench is about (a `hit` subject where every other line
# matched would measure the match path, which is the other sub-bench's job).
HIT_SPACING = 4096


def fill(rng, target, features_every=None, line=None):
    """`line()` lines to `target` bytes (default the mixed background); if
    `features_every` is set, one line of every shape spliced in after each
    block of that many bytes."""
    line = line or logtext.background
    out = []
    size = 0
    next_inject = features_every
    while size < target:
        line_text = line(rng)
        out.append(line_text)
        size += len(line_text) + 1
        if features_every and size >= next_inject:
            for feat in logtext.FEATURES:
                block = logtext.feature_line(rng, feat)
                out.extend(block)
                size += sum(len(x) + 1 for x in block)
            next_inject = size + features_every
    return ("\n".join(out) + "\n").encode("latin-1")


def build(seed=SEED):
    rng = logtext.Rng(seed)
    subjects = []
    for label, nbytes in SIZES:
        subjects.append(
            ("t-%s-fail" % label,
             "%d KB of background log text, NO member shape anywhere (the "
             "failing path; the analogue of bench/email's t-b-no-at)"
             % (nbytes // 1024),
             fill(rng, nbytes)))
        subjects.append(
            ("t-%s-syslog" % label,
             "%d KB of a single-source BSD-syslog stream, no member shape and "
             "NO `\"` or `)` anywhere -- the required code units of kv-quoted "
             "and stack-frame, which are therefore dismissible without a scan"
             % (nbytes // 1024),
             fill(rng, nbytes, line=logtext.syslog_only)))
        subjects.append(
            ("t-%s-hit" % label,
             "%d KB of the same log text with one instance of every member "
             "shape per %d B (the matching-bearing counterpart)"
             % (nbytes // 1024, HIT_SPACING),
             fill(rng, nbytes, features_every=HIT_SPACING)))
    return subjects


def main(argv=None):
    # [B115]: --seed/--out, same shape and same default-byte-identity
    # guarantee as gen_subjects.py's.
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--seed", type=int, default=SEED,
                    help="RNG seed (default: the committed seed, %d)" % SEED)
    ap.add_argument("--out", default=None,
                    help="write subjects + manifest_throughput.tsv under "
                         "DIR instead of the committed throughput/ + "
                         "manifest_throughput.tsv beside this script")
    args = ap.parse_args(argv)
    out_dir = args.out or OUT
    manifest_path = (os.path.join(args.out, "manifest_throughput.tsv")
                     if args.out else MANIFEST)

    subjects = build(args.seed)
    os.makedirs(out_dir, exist_ok=True)
    lines = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, desc, buf in subjects:
        with open(os.path.join(out_dir, sid + ".bin"), "wb") as f:
            f.write(buf)
        lines.append("%s\t%d\t%s\t%s\t%s"
                     % (sid, len(buf), hashlib.sha256(buf).hexdigest(), desc,
                        logtext.periodic_field(buf)))
    with open(manifest_path, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(lines) + "\n")
    print("gen_throughput_subjects: %d subjects (%s) -> %s, manifest -> %s"
          % (len(subjects), ", ".join("%d B" % len(b) for _s, _d, b in subjects),
             out_dir, manifest_path))


if __name__ == "__main__":
    main()
