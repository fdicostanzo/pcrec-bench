# U8 — RE2's `\B` (and `\b`) evaluate at BYTE offsets, ASCII-only, under UTF-8 encoding

**Engine:** RE2 (`RE2::Options::EncodingUTF8`). **Version:** 11.0.0
(both the distribution `libre2-dev` package this project pins and the
pristine upstream tag `2025-11-05` — identical result from both
builds, see `expected.txt`). **Kind:** semantics (see Status below —
this repro's own reading is that it is NOT A BUG).

## What it shows

Given the subject `"a" + U+00E9` ("é") UTF-8-encoded as bytes
`61 C3 A9`, RE2's `\B` (in `EncodingUTF8` mode) reports an empty-width
match at byte offset `[2,2)` — a position that sits **between the two
bytes of the single character U+00E9** — as well as the arguably more
defensible `[3,3)` (end of text, after a non-word byte). No decoded
Unicode reader would ever consider byte offset 2 a character boundary
at all: it is inside one multi-byte encoding unit. `repro.cc` finds
both positions by walking `RE2::Match()` with an advancing `startpos`
(the same "advance by the match end, or by one byte past an empty
match" find-all rule this project's own `testees/re2/driver.cc` and
`testees/pcre2/driver.c` implement — KB-17).

Traced against `bench/utf8`'s own corpus (`utf8@0.1`,
`docs/dev/upstream_findings.md` U8): the same shape reproduces on real
`cls-mixed-hit` and `cls-space-pair`/`prp-zs-hit` subjects, with
find-all counts inflated 3.0-3.3% over the oracle on 64 KB/1 MB
subjects — every extra match is one of these mid-character or
mid-multi-byte-space positions.

## Why this is (most likely) NOT A BUG

RE2's own syntax documentation states both assertions in exactly these
terms (`doc/syntax.txt`, upstream `main` branch, as of 2026-09-27):

    \b   at ASCII word boundary («\w» on one side and «\W», «\A», or «\z» on the other)
    \B   not at ASCII word boundary

and, a few lines later, that RE2's Perl character classes (`\w` among
them) are **"all ASCII-only"**. There is no UTF-8-aware `\b`/`\B` in
RE2 at all, by design, at any encoding setting — this is not a
UTF-8-specific gap, it is the documented ASCII-only definition applied
uniformly. Its predictable corollary under `EncodingUTF8` (where the
compiled automaton necessarily operates over UTF-8 *bytes*, since RE2
has no separate "decode to runes first" pass) is that **every
continuation byte of a multi-byte character is "not a word character"
by the ASCII-only rule**, so a `\B` test lands true between any two
non-ASCII bytes — including the interior bytes of one character. The
RE2 maintainer (`junyer`, a listed contributor) states the same
restriction directly in response to an near-identical complaint,
google/re2#344 ("`\b` not working with Unicode characters", 2024,
still open): *"Sorry, RE2 supports `\b`, `\d`, `\s`, `\w` and their
counterparts for ASCII only."* That issue is about word-CHARACTER
classification (should `ä` count as `\w`?) rather than this repro's
byte-vs-character POSITION framing, so it is not a byte-identical
duplicate of U8 — but it is the same underlying, documented root cause,
and reading it made this repro possible without independently
guessing at RE2's internals.

## Build and run

Needs `libre2-dev` (`pkg-config re2` discoverable) — the same
`pkg-config --cflags --libs re2` line `testees/re2/adapter.py` uses to
build its own driver. `run.sh` builds with `g++ -O2 -std=c++17` and
runs the single binary; no pcrec-bench code, no store, no stdin.

    UPSTREAM_SCRATCH=/var/tmp/some-dir ./run.sh

Exit 0 = PRESENT (a `\B` match lands inside U+00E9's 2-byte encoding),
1 = ABSENT (no such match — i.e. RE2 gained rune-aware `\B`, which
would be a real behavior/API change), 2 = CANNOT-RUN (libre2 not
found / build failed).

## What ABSENT would look like

    \B match at byte [3,3)
    ABSENT: no \B match landed inside a multi-byte character
    U8 ABSENT re2 <version> 1

## Status

REPRODUCED (this repro; also `docs/dev/upstream_findings.md` U8's
original bench record). **Likely NOT-A-BUG**: the ASCII-only `\b`/`\B`
definition is documented upstream (`doc/syntax.txt`, cited above) and
confirmed by the maintainer's own words on a closely related issue
(google/re2#344, searched 2026-09-27, still open — not a byte-identical
duplicate, so not cited as `tracker: KNOWN-UPSTREAM`, but strong
supporting context). Whoever finalizes U8's status should weigh: is
"lands between two bytes of one character" different enough from
"treats `ä` as non-word" to be worth a documentation request (e.g. RE2
could document that under `EncodingUTF8`, `\b`/`\B` positions are byte
offsets that may fall inside a multi-byte character, which `doc/
syntax.txt` does not currently say explicitly) — that would be a
documentation-clarity ask, not a behavior-change bug report. Not
REPORTED.
