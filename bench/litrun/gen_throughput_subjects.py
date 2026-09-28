#!/usr/bin/env python3
"""gen_throughput_subjects.py -- the L-sweep's THROUGHPUT-SCALE, dense
subjects (S7.2), the instrument P8 asked for.

WHY THROUGHPUT SCALE, NOT S2a's OWN L-BYTE MICRO-SUBJECTS ("Regime choice",
NOTES.md's fuller version). pcrec's own `memcmp_lowering_study.md` times its
three candidate forms with a tight C loop calling one comparison directly --
an instrument this project does not have. A pcrecbench cell times ONE driver
invocation over ONE subject; a single L-byte subject (2-40 B) would compile,
run and answer in far less than a microsecond, well under this harness's own
per-call floor (see the floor pattern), and the reported median would be
noise, not signal. The fix used everywhere else this project needs a
per-call number against a busy background (bench/loglines' size sweep,
bench/altwide's throughput arm) is the same one here: tile the SAME small
unit back-to-back until the candidate-start scan or the VM's own loop has
thousands of independent attempts to make, and read the per-attempt cost off
the total. So each of the L-sweep's nine lengths gets three ~64 KiB dense
subjects instead of tiny ones -- `mat-l<L>` (every window a full match),
`fbf-l<L>` (every window fails at the first compared byte) and `lbf-l<L>`
(every window fails only after L-1 matching bytes) -- built by tiling one
`littext.unit_*` helper, which is where the per-length byte content lives.

WHY THE TILING IS SAFE (no accidental match/mismatch at an unintended
offset). `littext.literal(L)` is drawn from a 52-DISTINCT-character
alphabet (`gen_patterns.py`'s own `check_no_internal_repeat`), so:

  * `mat-l<L>` = literal * N. The only way an L-byte window of a repeated,
    non-self-overlapping string can equal the string itself is at an
    ALIGNED offset (a multiple of L) -- a periodic string with no smaller
    period (which `literal`'s all-distinct-byte construction guarantees)
    has no other self-alignment. Every aligned window matches; the oracle
    confirms the exact count (`total_bytes // L`) rather than this file
    asserting it.
  * `fbf-l<L>` / `lbf-l<L>` = `unit * N`, where `unit` is `literal` with ONE
    byte replaced by the floor byte `#` -- a byte that appears NOWHERE in
    `literal` (`#` is not a letter; `gen_patterns.py` asserts this at
    generation time for every pattern). A full-length (L-byte) window over
    a stream built by repeating a period-L unit ALWAYS contains exactly one
    complete copy of that unit's bytes, in some rotation -- so it ALWAYS
    contains the `#` guard byte at exactly one position, and `literal`
    (which contains no `#` anywhere) can therefore never equal ANY window
    of this stream, aligned or not. `check_no_accidental_match()` below
    confirms this by brute force (every offset in one period) at
    generation time, rather than resting on the argument alone.

Sizes: TARGET_BYTES (64 KiB) rounded down to a whole number of periods, so
the manifest's `periodic` column reads the true period (`L` for `mat`, the
unit length for `fbf`/`lbf`, which is also `L`) rather than "no" from a
partial trailing copy.

    python3 bench/litrun/gen_throughput_subjects.py
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import littext  # noqa: E402

OUT = os.path.join(HERE, "throughput")
MANIFEST = os.path.join(HERE, "manifest_throughput.tsv")

TARGET_BYTES = 65536

KINDS = (
    ("mat", littext.unit_match,
     "every {L}-byte aligned window is a full match"),
    ("fbf", littext.unit_first_byte_flip,
     "every window fails at the first compared byte (byte 0 replaced "
     "by the floor byte, which occurs in no literal)"),
    ("lbf", littext.unit_last_byte_flip,
     "every window matches L-1 bytes then fails on the last (last byte "
     "replaced by the floor byte)"),
)


def check_no_accidental_match(lit, unit):
    """Brute-force confirmation of the tiling argument in this file's own
    docstring: over TWO full periods of `unit` (so every possible window
    offset within one period is covered, including ones that straddle a
    period boundary), no window of len(lit) bytes equals `lit`, UNLESS
    `unit == lit` itself (the `mat` case, where every aligned window is
    meant to match and this check is skipped by the caller)."""
    stream = unit * 3
    L = len(lit)
    for off in range(L):
        if stream[off:off + L] == lit:
            raise SystemExit(
                "accidental match at offset %d for unit %r (literal %r)"
                % (off, unit, lit))


def build_one(L, kind, unit_fn):
    unit = unit_fn(L)
    lit = littext.literal(L)
    if unit != lit:
        check_no_accidental_match(lit, unit)
    reps = TARGET_BYTES // L
    body = unit * reps
    return body


def main():
    os.makedirs(OUT, exist_ok=True)
    lines = ["id\tlen\tsha256\tdescription\tperiodic"]
    rows = []
    for L in littext.L_SWEEP:
        for kind, unit_fn, note in KINDS:
            body = build_one(L, kind, unit_fn)
            sid = "%s-l%d" % (kind, L)
            with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
                f.write(body)
            desc = "lit-l%d %s density, %d reps of a %d-byte unit: %s" % (
                L, kind, len(body) // L, L, note.replace("{L}", str(L)))
            rows.append((sid, len(body), hashlib.sha256(body).hexdigest(),
                         desc, littext.periodic_field(body)))
    for sid, ln, sha, desc, per in rows:
        lines.append("%s\t%d\t%s\t%s\t%s" % (sid, ln, sha, desc, per))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(lines) + "\n")
    total = sum(r[1] for r in rows)
    print("gen_throughput_subjects: %d subjects (%d B total, %d..%d each) "
          "-> %s, manifest -> %s"
          % (len(rows), total, min(r[1] for r in rows),
             max(r[1] for r in rows), OUT, MANIFEST))


if __name__ == "__main__":
    main()
