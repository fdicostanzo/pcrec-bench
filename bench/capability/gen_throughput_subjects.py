#!/usr/bin/env python3
"""gen_throughput_subjects.py -- the capability set's three throughput
texts: `throughput/` (gitignored) + `manifest_throughput.tsv`
(committed), in `bench/syntax/gen_throughput_subjects.py`'s shape:
`captext.text()` at three sizes and three seeds, a SIZE SWEEP at fixed
"grammar", not a density cross (capability_set_v1.md 3.5).

SAFETY NOTE for family 10 (`redos-nested`): every pattern in that family
is anchored at `^` (checked in NOTES.md's authoring review), so a
`find_all` scan over these texts attempts a real match only at offset 0
-- every later scan position fails in O(1) because `^` (no MULTILINE
anywhere in this set) cannot match past the subject's start. The
generated grammar also never emits a long uniform run of one character
class (captext's four line kinds all interleave words/punctuation/
digits), so no accidental adversarial prefix can arise. `--check`'s own
run empirically re-times every redos pattern against all three texts
(the `_redos_safety_check` below) as a belt-and-braces control beyond
the structural argument.
"""
import hashlib
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

import captext as ct  # noqa: E402

OUT = os.path.join(HERE, "throughput")
MANIFEST = os.path.join(HERE, "manifest_throughput.tsv")

SIZES = (
    ("t-64k", 64 * 1024, 0xC0FFEE1),
    ("t-256k", 256 * 1024, 0xC0FFEE2),
    ("t-1m", 1024 * 1024, 0xC0FFEE3),
)

_REDOS_PATTERNS = (
    r"^([a-zA-Z0-9._%+-]+)+@",
    r"^(\s+)*$",
    r"^(([a-z]+)*)+$",
    r"^(\d+)+$",
    r"^(\d+\s*)+$",
    r"^(([0-9]+[-/])+)+$",
)


def _redos_safety_check(texts):
    sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
    from pcrecbench import oracle_pcre2 as oracle
    for name, body in texts:
        for pat in _REDOS_PATTERNS:
            rx = oracle.compile(pat)
            t0 = time.time()
            try:
                rx.find_all(body)
            except oracle.Pcre2Error:
                pass  # a bounded give-up is fine; a HANG is what we guard
            dt = time.time() - t0
            if dt > 2.0:
                raise AssertionError(
                    "redos safety check: %r over %s took %.2fs (> 2s "
                    "guard) -- family 10's ^-anchor argument may not "
                    "hold for this text" % (pat, name, dt))


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = ["id\tlen\tsha256\tdescription\tperiodic"]
    texts = []
    for sid, nbytes, seed in SIZES:
        body = ct.text(nbytes, seed)
        texts.append((sid, body))
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(),
            "throughput/mixed log+http+source+prose grammar, seed 0x%x"
            % seed, ct.periodic_field(body)))
    _redos_safety_check(texts)
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(rows) + "\n")
    print("gen_throughput_subjects: %d text(s) -> %s, manifest -> %s "
          "(redos safety check: OK)" % (len(SIZES), OUT, MANIFEST))
    return 0


if __name__ == "__main__":
    sys.exit(main())
