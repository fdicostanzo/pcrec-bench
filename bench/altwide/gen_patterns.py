#!/usr/bin/env python3
"""gen_patterns.py -- `patterns/*.rx`, the thirty-three canonical patterns of
the wide-alternation sub-bench (twenty at 0.1, thirteen added at 0.2).

WHY THE PATTERNS ARE GENERATED HERE AND NOT TYPED. Every other sub-bench in
this repo commits hand-written `.rx` files, because every other sub-bench's
patterns are short enough to read. This one's are not: `w-2048` is 17 KB of
alternation and `s-4096` is 22 KB. What a reader needs is not the bytes but
the RULE that produced them -- which pool, which slice, which wrapper -- and
a rule in a header beside 17 KB of committed text is a rule that can drift
from the text without anyone noticing. So the `.rx` files are DERIVED, they
are committed (the loader reads them, `content_hash` hashes them, and a
window must be able to see exactly what was measured), and `make check`
re-derives them with `--check` the way it re-derives every other table here.

    python3 bench/altwide/gen_patterns.py           # write
    python3 bench/altwide/gen_patterns.py --check    # re-derive + diff

THE TABLE BELOW IS THE SET. Each row is (name, pool, width, wrapper), and
the four columns are the set's four design axes:

  WIDTH   `w-8` .. `w-2048` over the `main` pool, and `s-256`/`s-512`/
          `s-2048`/`s-4096` over the short-word pool. Nested slices of one
          pool, so a rung-to-rung difference is a WIDTH difference and
          nothing else. The rungs are geometric and DENSE where a knee is
          predicted (NOTES.md, "What the ladder brackets"): 256/512 bracket
          the point at which a forward DFA's `states x classes` is predicted
          to cross an emitter's 16-bit table-encoding bound, 1024/2048 the
          point at which a branch-per-node VM lowering is predicted to cross
          an emitted-size cap. 0.2 densified 64..512 to 64/96/128/192/256/
          384/512 because the band BELOW the width at which pcrec refuses is
          where a flat line has to be shown to be flat, and 0.1 had three
          points there.

  STRUCTURE  the pool decides what PCRE2's start-of-match analysis and an
          AOT compiler's prefilter derivation can see: `main` spreads first
          bytes over all 26 letters (a start bitmap), `sh1` shares one first
          byte (a first code unit; one `memchr`), `pfx3` shares three,
          `nar4` uses four first bytes (a four-bit bitmap), `sfx` shares a
          three-byte SUFFIX (a REQUIRED code unit where the others have
          none). Since 0.2 every one of them appears at 256 as well, so
          structure is crossed with width at a width every engine in the
          bench is known to COMPILE, not only at 64 and at 512.

  ORDER   `srt-256` / `srt-512` are `w-256` / `w-512`'s branches SORTED by
          first byte. Same words, same language (the pools are
          substring-free, so leftmost-first cannot return a different span
          -- altwidetext.py, property 2), and the maximal run of adjacent
          branches sharing a first byte goes from 2 to about 15 (256) or 30
          (512). Everything a pair's two rows differ by is cost.

  WRAPPER `ci-256`/`ci-512` are `w-256`/`w-512` under `(?i)`, `cnt-64` is
          `w-64` under a bounded count (the bridge to bench/bounded),
          `wb-256`/`wb-512` are `w-256`/`w-512` inside `\\b...\\b` (the
          `assertions` module).

Plus the floor: one literal byte (`#`), requirements 5's per-call control.

Every group is `(?:...)`: no capture participates anywhere in this set, which
`gen_expectations.py` re-checks on every run.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import altwidetext as at  # noqa: E402

OUT = os.path.join(HERE, "patterns")

# (name, pool, width, wrapper). `wrapper` is applied to the bare
# `(?:b1|b2|...)` alternation; `sorted` reorders the slice first.
SPECS = (
    # ---- the width ladder, spread first bytes, generation order ----
    # 0.2 DENSIFIED it between 64 and 512 (`w-96`/`-128`/`-192`/`-384`):
    # 0.1's rungs under the width at which pcrec refuses were 8, 64 and 256
    # -- three points -- and a flat line needs more than three points before
    # it is a line rather than three numbers. Every rung is still a NESTED
    # slice of the same pool, so `w-8` C `w-64` C `w-96` C ... C `w-2048`
    # and every 0.1 rung's bytes are unchanged.
    ("w-8",       "main",  8,    None),
    ("w-64",      "main",  64,   None),
    ("w-96",      "main",  96,   None),
    ("w-128",     "main",  128,  None),
    ("w-192",     "main",  192,  None),
    ("w-256",     "main",  256,  None),
    ("w-384",     "main",  384,  None),
    ("w-512",     "main",  512,  None),
    ("w-1024",    "main",  1024, None),
    ("w-2048",    "main",  2048, None),
    # ---- the short-word ladder: the oracle's ceiling is why it exists,
    # ---- and 0.2's two low rungs are the branch-LENGTH pair at a width
    # ---- that is not at anyone's ceiling (`s-256` against `w-256`) plus
    # ---- the byte-versus-count probe at the width where the `main` pool
    # ---- is refused (`s-512` against `w-512`, 3023 B of pattern against
    # ---- 4264 at the identical branch COUNT).
    ("s-256",     "short", 256,  None),
    ("s-512",     "short", 512,  None),
    ("s-2048",    "short", 2048, None),
    ("s-4096",    "short", 4096, None),
    # ---- structure, at three widths since 0.2: 64, the 256 ANCHOR (the
    # ---- widest rung every engine in the bench is known to compile), and
    # ---- 512 ----
    ("sh1-64",    "sh1",   64,   None),
    ("sh1-256",   "sh1",   256,  None),
    ("sh1-512",   "sh1",   512,  None),
    ("pfx3-256",  "pfx3",  256,  None),
    ("pfx3-512",  "pfx3",  512,  None),
    ("sfx-64",    "sfx",   64,   None),
    ("sfx-256",   "sfx",   256,  None),
    ("sfx-512",   "sfx",   512,  None),
    ("nar4-64",   "nar4",  64,   None),
    ("nar4-256",  "nar4",  256,  None),
    ("nar4-512",  "nar4",  512,  None),
    # ---- order ----
    ("srt-256",   "main",  256,  "sorted"),
    ("srt-512",   "main",  512,  "sorted"),
    # ---- wrappers ----
    ("ci-256",    "main",  256,  "caseless"),
    ("ci-512",    "main",  512,  "caseless"),
    ("cnt-64",    "main",  64,   "count13"),
    ("wb-256",    "main",  256,  "wordbound"),
    ("wb-512",    "main",  512,  "wordbound"),
)

FLOOR_NAME = "floor"
FLOOR_TEXT = "#"


def wrap(words, wrapper):
    """The pattern text for a branch list. THE one definition of what each
    wrapper spells -- `gen_oracle_limits.py` imports this rather than
    restating it, so a probe row can never describe a shape the set does not
    actually build."""
    if wrapper == "sorted":
        words = sorted(words)
    alt = "(?:" + "|".join(words) + ")"
    if wrapper == "caseless":
        return "(?i)" + alt
    if wrapper == "count13":
        return alt + "{1,3}"
    if wrapper == "wordbound":
        return "\\b" + alt + "\\b"
    if wrapper is not None and wrapper != "sorted":
        raise ValueError("unknown wrapper %r" % wrapper)
    return alt


def pattern_text(pool, width, wrapper):
    return wrap(at.pools()[pool][:width], wrapper)


def derive():
    """-> [(filename, bytes)], in the order `SPECS` lists them."""
    out = [("%s.rx" % name, pattern_text(pool, w, wrapper).encode("latin-1"))
           for name, pool, w, wrapper in SPECS]
    out.append(("%s.rx" % FLOOR_NAME, FLOOR_TEXT.encode("latin-1")))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--check", action="store_true",
                    help="re-derive and DIFF against the committed files "
                         "instead of writing them (the `make check` mode)")
    args = ap.parse_args(argv)
    files = derive()

    if args.check:
        have = sorted(f for f in os.listdir(args.out) if f.endswith(".rx"))
        want = sorted(fn for fn, _b in files)
        if have != want:
            print("gen_patterns --check: %s holds %s, the table derives %s"
                  % (args.out, have, want), file=sys.stderr)
            return 1
        for fn, body in files:
            with open(os.path.join(args.out, fn), "rb") as f:
                got = f.read()
            if got != body:
                print("gen_patterns --check: %s does NOT re-derive (committed "
                      "%d B, derived %d B)" % (fn, len(got), len(body)),
                      file=sys.stderr)
                return 1
        print("gen_patterns --check: %d pattern file(s) re-derive, %d B total"
              % (len(files), sum(len(b) for _f, b in files)))
        return 0

    os.makedirs(args.out, exist_ok=True)
    for fn, body in files:
        with open(os.path.join(args.out, fn), "wb") as f:
            f.write(body)
    print("gen_patterns: %d pattern(s), %d B total -> %s"
          % (len(files), sum(len(b) for _f, b in files), args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
