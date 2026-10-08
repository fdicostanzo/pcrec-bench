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

# [B125] capability@0.2: the subjects APPENDED after the three 0.1 texts
# (manifest rows 4..; the 0.1 rows and files are untouched, asserted by
# main()). All are > short_search_max_bytes, so they enter the THROUGHPUT
# regime only -- and, because the throughput regime is "every pattern x every
# throughput subject", every pattern of the set is run on each of them.
#   (id, generator-call, description)
_PROSE_BYTES = 1024 * 1024 - 64
_TAILS = (
    ("t-tail-digits-1m", b"total 20250614",
     "throughput/[B125] ~1 MiB generated prose (seed 0xC0FFEE21), last line "
     "'total 20250614': the tail `\\d+$` and `\\w+\\z` MATCH, `\\s+$`, "
     "`[a-z]+\\.txt$` and `.*\\.txt$` do not"),
    ("t-tail-txt-1m", b"saved to report.txt",
     "throughput/[B125] the SAME prose, last line 'saved to report.txt': "
     "`[a-z]+\\.txt$`, `.*\\.txt$` and `\\w+\\z` ('txt') MATCH, `\\d+$` and "
     "`\\s+$` do not"),
    ("t-tail-space-1m", b"end of file   ",
     "throughput/[B125] the SAME prose, last line 'end of file' + three "
     "spaces: `\\s+$` MATCHES, `\\d+$`, `\\w+\\z`, `[a-z]+\\.txt$` and "
     "`.*\\.txt$` do not"),
)
_LONG = 60 * 1024


def extra_subjects():
    """-> [(id, bytes, description)] in manifest order. The two long
    ReDoS-family subjects pair a MATCHING run with its NEAR-MISS (the SAME
    run plus one terminating non-member byte), for `^(([a-z]+)*)+$` and
    `^(\\s+)*$`; the mixed-run subject is ~4 KB of interleaved short runs;
    the three tail subjects share one ~1 MiB prose body and differ only in
    their last line."""
    letters = ct.letter_run(_LONG, 0xC0FFEE11)
    spaces = ct.ws_run(_LONG, 0xC0FFEE12)
    out = [
        ("t-evil-match-60k", letters,
         "throughput/[B125] 60 KiB of random [a-z], nothing else: the "
         "long MATCHING subject of `^(([a-z]+)*)+$` (whole subject; the "
         "backtracker's first greedy path)"),
        ("t-evil-nearmiss-60k", letters + b"!",
         "throughput/[B125] t-evil-match-60k + one '!': the long NEAR-MISS "
         "(the same run plus one terminating non-member byte) -- exponential "
         "for a backtracker, the oracle's second method answers it"),
        ("t-trim-match-60k", spaces,
         "throughput/[B125] 60 KiB of mixed \\s bytes (space/tab/LF/CR/FF/VT), "
         "ending in a space: the long MATCHING subject of `^(\\s+)*$`"),
        ("t-trim-nearmiss-60k", spaces + b"x",
         "throughput/[B125] t-trim-match-60k + one 'x': the long NEAR-MISS"),
        ("t-mixed-runs-4k", ct.mixed_runs(4096, 0xC0FFEE13),
         "throughput/[B125] 4096 B of interleaved SHORT runs (letters, "
         "digits, hex, signed decimals, separators, standalone 8-hex ids), "
         "ending in a letter: the real-text shape no pure-run subject has"),
    ]
    for sid, tail, desc in _TAILS:
        out.append((sid, ct.prose(_PROSE_BYTES, 0xC0FFEE21, tail), desc))
    return out


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


# The 0.1 rows, byte for byte: capability@0.2 EXTENDS the manifest, it never
# re-draws it. A change to captext.text() that moved a 0.1 text would fail
# here before it reached a manifest.
_0_1_SHA256 = {
    "t-64k": "d2e4f134473cc40a9a4e7df7a30e0efa11f566d96ee990c62cd663a2439c8524",
    "t-256k": "3cf7b248873da164518b74e039cc2380f39e233b2899716c82c8eb4b7b49b5a7",
    "t-1m": "ccbdf7eb97f15776a68b8bbb9d6387870cd01d4796207fb20032958caf9754ee",
}


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = ["id\tlen\tsha256\tdescription\tperiodic"]
    texts = []
    for sid, nbytes, seed in SIZES:
        body = ct.text(nbytes, seed)
        texts.append((sid, body))
        assert hashlib.sha256(body).hexdigest() == _0_1_SHA256[sid], (
            "capability@0.2 moved a 0.1 throughput text: %s" % sid)
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(),
            "throughput/mixed log+http+source+prose grammar, seed 0x%x"
            % seed, ct.periodic_field(body)))
    for sid, body, desc in extra_subjects():
        assert len(body) > 512, sid       # throughput-only, by size
        texts.append((sid, body))
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(), desc,
            ct.periodic_field(body)))
    _redos_safety_check(texts)
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(rows) + "\n")
    print("gen_throughput_subjects: %d text(s) -> %s, manifest -> %s "
          "(redos safety check: OK)" % (len(texts), OUT, MANIFEST))
    return 0


if __name__ == "__main__":
    sys.exit(main())
