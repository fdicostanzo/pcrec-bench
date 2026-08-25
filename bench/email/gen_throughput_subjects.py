#!/usr/bin/env python3
"""gen_throughput_subjects.py -- the email sub-bench's three 1 MB subjects.

COPIED from pcrec docs/design/subroutines_measurements/email_specimen/
gen_throughput_subjects.py (read-only origin; see CLAUDE.md). The three
constructions below are that file's verbatim, so the subjects are
byte-identical to the ones pcrec's srEmail lane measured. What changed is the
output shape: schema-slug ids, and a committed `manifest_throughput.tsv` with
a sha256 column.

1 MB is a KNOWN-SMALLER departure from pcrec's own 8-64 MB convention and is
inherited deliberately, not chosen: requirements 3 defers the standard size to
OD-B10 (spread at 1 MB vs 8 MB, measured on this box, at [B4]).

Deterministic: no randomness, no clock, no environment.
"""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "throughput")
MANIFEST = os.path.join(HERE, "manifest_throughput.tsv")

TARGET = 1024 * 1024

SUBJECTS = []


def build():
    # (a) valid addresses separated by spaces
    addr = b"user.name@sub.example.com "
    SUBJECTS.append(("t-a-valid-addrs",
                     "1 MB of valid dot-atom addresses separated by spaces",
                     (addr * (TARGET // len(addr) + 1))[:TARGET]))

    # (b) no '@' at all
    line = b"the quick brown fox jumps over the lazy dog 1234567890 "
    SUBJECTS.append(("t-b-no-at",
                     "1 MB of prose with no '@' anywhere (the prefilter case)",
                     (line * (TARGET // len(line) + 1))[:TARGET]))

    # (c) one long atom run (no @, no dots, no spaces -- pure atom-class bytes)
    SUBJECTS.append(("t-c-long-atom-run",
                     "1 MB of 'a' -- one unbroken atom-class run, no '@'",
                     b"a" * TARGET))


def main():
    build()
    os.makedirs(OUT, exist_ok=True)
    lines = ["id\tlen\tsha256\tdescription"]
    for sid, desc, buf in SUBJECTS:
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(buf)
        lines.append("%s\t%d\t%s\t%s"
                     % (sid, len(buf), hashlib.sha256(buf).hexdigest(), desc))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(lines) + "\n")
    print("gen_throughput_subjects: %d subjects -> %s, manifest -> %s"
          % (len(SUBJECTS), OUT, MANIFEST))


if __name__ == "__main__":
    main()
