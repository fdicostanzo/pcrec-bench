"""docs/dev/measurements/probe_b104_o62_identity_sanity.py -- [B104], lane
b104pred, 2026-09-27: THE SANITY CHECK the manager asked for on
`probe_b104_o62_identity.py`'s own census: does `tools/program_identity.py`'s
v2 normalization (`normalize_one`) exclude the STAMP #define lines the
abi 29-37 pin range added (`RX_REQ_BYTE`/`_RUN`/`_WHY`, `RX_END_WINDOW`,
`RX_VM_START`, ...), or does a "changed" verdict just mean "the pin added a
stamp line", which would make the census WEAK (every artifact would read
"changed" regardless of any real code difference)?

TWO checks, both direct (no re-implementation of normalize_one's own rule):

1. For one witness (email/factored, auto-caps, plain), print the RAW
   emitted `#define RX_*` stamp lines on both pins, then confirm NONE of
   those stamp NAMES survive `program_identity.normalize_one` on EITHER
   side -- proving rule 3 (a macro #define'd on ONE side only is dropped
   whole) actually fires on this project's real emitted text, not merely
   as documented in the module's own docstring.
2. For three independently-chosen "changed" rows from the census (one
   per set: email/factored, syntax/alt-nested, bounded/cls-lazy-16384),
   unified-diff the two pins' own NORMALIZED text and print every hunk --
   proving what a "changed" verdict is actually made of on real data.

Compile-only (no gcc, no timing); both pins must already be built
(`build/pcrec-25b1984f/build/pcrec`, `build/pcrec-751b9c6d/build/pcrec`).

Run from the repo root:
    python3 docs/dev/measurements/probe_b104_o62_identity_sanity.py
"""
import difflib
import os
import sys
import tempfile

sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI              # noqa: E402
from pcrecbench import record as _rec      # noqa: E402

BINS = {"25b1984f": "/home/duxevents/pcrec-bench/build/pcrec-25b1984f/build/pcrec",
        "751b9c6d": "/home/duxevents/pcrec-bench/build/pcrec-751b9c6d/build/pcrec"}
CAPS = ["--features", "all"]
STAMP_NAMES = ("RX_REQ_BYTE", "RX_REQ_RUN", "RX_REQ_WHY", "RX_END_WINDOW",
               "RX_VM_START")


def emit_both(text, shapes, tmp):
    return {pin: PI.emit(BINS[pin], shapes[pin], CAPS, text,
                          os.path.join(tmp, pin)) for pin in BINS}


def check1(shapes, tmp):
    print("=== check 1: are the new stamp #define lines excluded by "
          "normalize_one? (bench/email/patterns/factored.rx, auto-caps, "
          "plain) ===")
    b = open("bench/email/patterns/factored.rx", "rb").read()
    while b.endswith(b"\n"):
        b = b[:-1]
    got = emit_both(b, shapes, tmp)
    for pin, t in got.items():
        stamps = [ln for ln in t.splitlines()
                  if any(ln.startswith("#define %s " % n) for n in STAMP_NAMES)]
        print("%s raw stamp lines: %r" % (pin, stamps))
    for pin, t in got.items():
        n = PI.normalize_one(t)
        present = [s for s in STAMP_NAMES if s in n]
        print("%s stamp names surviving normalize_one: %r" % (pin, present))
    print()


def check2(shapes, tmp):
    witnesses = [
        ("bench/email/patterns/factored.rx", "plain"),
        ("bench/syntax/patterns/alt-nested.rx", "whole-subject"),
        ("bench/bounded/patterns/cls-lazy-16384.rx", "whole-subject"),
    ]
    print("=== check 2: diff the normalized programs of three independent "
          "'changed' rows (one per set) ===")
    for path, form in witnesses:
        b = open(path, "rb").read()
        while b.endswith(b"\n"):
            b = b[:-1]
        text = b if form == "plain" else _rec.whole_subject_text(b, False)
        got = emit_both(text, shapes, tmp)
        norm = {pin: PI.normalize_one(t) for pin, t in got.items()}
        d = list(difflib.unified_diff(
            norm["25b1984f"].splitlines(), norm["751b9c6d"].splitlines(),
            fromfile="25b1984f.norm", tofile="751b9c6d.norm", lineterm=""))
        print("---- %s (%s) ----" % (path, form))
        print("\n".join(d))
        print("(%d diff line(s) total, header included)" % len(d))
        print()


def main():
    with tempfile.TemporaryDirectory() as tmp:
        shapes = {p: PI._cli_shape(b, tmp) for p, b in BINS.items()}
        print("CLI shapes: %s" % shapes)
        print()
        check1(shapes, tmp)
        check2(shapes, tmp)


if __name__ == "__main__":
    main()
