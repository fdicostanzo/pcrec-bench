"""utf8text.py -- bench/utf8's shared randomness primitive, word pools and
text grammar, in `bench/syntax/censustext.py`'s / `bench/capability/
captext.py`'s shape (same xorshift64* primitive, same "re-export
`periodic_field`" convention -- copied, not imported, per `captext.py`'s
own precedent: this set's texts must never move when another set's
generator changes).

FIVE SCRIPT CORPORA (utf8_set_v1.md 4.2): `lat` (French/German/Spanish,
Latin-1-Supplement-heavy), `cyr` (Russian), `cjk` (Japanese/Chinese, with
a small ASCII admixture -- numbers and Latin proper nouns, a real feature
of CJK prose), `mix` (all four interleaved, plus 4-byte emoji/symbols --
the only corpus carrying 4-byte characters), `asc` (byte-clean ASCII, the
CONTROL). Each script's word vocabulary is a committed `pool_<script>.tsv`
(`lat`/`cyr`/`cjk`/`asc`) of roughly 100-200 common words; `mix`'s own
`pool_mix.tsv` is not a fifth PROSE vocabulary -- it is the emoji/symbol
tokens the `mix` corpus interleaves into sentences drawn from the other
four (utf8_set_v1.md 4.2's own description of `mix`).

THE SIZE-FITTING BOUNDARY RULE (utf8_set_v1.md 4.1, F-M1, a stated
requirement of the U3 lane, not an implementation detail left to it).
`captext.py:100-118`'s trim-to-fit loop (a raw byte-offset slice,
`line[:remaining]`) is safe only because its alphabet is ASCII. Sliced at
an arbitrary byte offset, a multi-byte corpus lands inside a character on
most (corpus, size) pairs and leaves an ill-formed UTF-8 tail. `text()`
below instead trims back to the LAST COMPLETE CHARACTER at or before the
byte budget (`_trim_to_char_boundary`, a decode-and-truncate walk-back),
then PADS with ASCII spaces (0x20, never a multi-byte filler) up to the
exact target byte size -- every subject `text()` writes is still exactly
its named size in bytes; the pad simply shows up in the byte histogram,
visibly (`subject_facts.tsv`'s own claim is unaffected by it).

THE DECODE GATE (utf8_set_v1.md 4.1). `decode_gate()` raises
`UnicodeDecodeError` on anything that is not well-formed UTF-8; every
subject this module's callers write is passed through it before its
manifest row is written -- belt-and-braces beyond `_trim_to_char_
boundary`'s own structural argument, in `gen_throughput_subjects.py`'s
(bench/capability) own `_redos_safety_check` precedent: verify the
structural argument, don't just assert it. `gen_subjects.py --check` and
`gen_throughput_subjects.py --check` each carry a NEGATIVE-ARM control
(`_check_decode_gate_has_teeth`): a byte string deliberately truncated
MID-CHARACTER (built by slicing a real multi-byte corpus at a raw byte
offset, bypassing `_trim_to_char_boundary` on purpose) must FAIL the gate
-- a check with no failing case proves nothing (pcrec's own check-design
lesson, restated throughout this repo).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench.periodic import periodic_field  # noqa: E402,F401  (re-export)

MASK64 = (1 << 64) - 1


class Rng:
    """xorshift64* -- `bench/syntax/censustext.py`'s / `bench/capability/
    captext.py`'s primitive, copied rather than imported (see module
    docstring). Deterministic: the same seed reproduces the same stream on
    any box."""

    def __init__(self, seed):
        self.state = seed & MASK64 or 0x2545F4914F6CDD1D

    def next64(self):
        x = self.state
        x ^= (x >> 12)
        x ^= (x << 25) & MASK64
        x ^= (x >> 27)
        self.state = x & MASK64
        return (x * 0x2545F4914F6CDD1D) & MASK64

    def randrange(self, n):
        return self.next64() % n

    def choice(self, seq):
        return seq[self.randrange(len(seq))]


# The five corpus labels utf8_set_v1.md 4.2 names. `mix` is not a fifth
# PROSE pool (see module docstring) -- its own pool file carries the
# emoji/symbol tokens the `mix` grammar interleaves.
SCRIPTS = ("lat", "cyr", "cjk", "mix", "asc")
PROSE_SCRIPTS = ("lat", "cyr", "cjk", "asc")

_POOL_CACHE = {}


def load_pool(script):
    """The committed `pool_<script>.tsv` as a tuple of words (cached).
    One word per line after the header; UTF-8, LF-terminated."""
    if script in _POOL_CACHE:
        return _POOL_CACHE[script]
    path = os.path.join(HERE, "pool_%s.tsv" % script)
    with open(path, encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    words = tuple(w for w in lines[1:] if w)
    assert words, "empty pool: %s" % path
    _POOL_CACHE[script] = words
    return words


# Punctuation/whitespace vocabulary, per script -- small and hand-authored
# (utf8_set_v1.md 4.1's "plus a punctuation/whitespace vocabulary"),
# language-appropriate rather than one shared ASCII set: a sentence's own
# punctuation participates in the byte histogram exactly as its words do.
_PUNCT = {
    "asc": (".", ",", ";", "!", "?"),
    "lat": (".", ",", ";", "!", "?", "«", "»", "¿", "¡"),
    "cyr": (".", ",", ";", "!", "?", "—", "«", "»"),
    "cjk": ("。", "、", "！", "？"),
}

# ASCII proper nouns / numbers interleaved into `cjk` prose -- a real
# feature of Japanese/Chinese text (utf8_set_v1.md 4.2: "with ASCII
# interleaved (numbers, latin proper nouns)"), kept as a small
# hand-authored vocabulary in code per the design note's own allowance
# rather than a sixth pool file for a dozen tokens.
_CJK_LATIN = ("Tokyo", "Osaka", "Sony", "Toyota", "Beijing", "Shanghai",
              "Honda", "Nikon", "2026", "24", "365", "5G")


def _cap(word):
    # ASCII-only capitalization; a non-ASCII word's own orthography (no
    # case in Cyrillic prose-initial position by this generator's rule,
    # no case at all in CJK) is left as authored.
    if word and word[0].isascii() and word[0].isalpha():
        return word[0].upper() + word[1:]
    return word


def sentence(rng, script):
    """One sentence in `script`: 6-14 words from that script's pool
    (`cjk` also draws a `_CJK_LATIN` token about 1 word in 12), joined
    with spaces -- except `cjk`, whose words are joined with NO
    inter-word space (real Japanese/Chinese orthography has none) -- and
    closed with one of the script's own punctuation marks."""
    pool = load_pool(script)
    n = 6 + rng.randrange(9)
    words = []
    for _ in range(n):
        if script == "cjk" and rng.randrange(12) == 0:
            words.append(rng.choice(_CJK_LATIN))
        else:
            words.append(rng.choice(pool))
    if script == "cjk":
        body = "".join(words)
    else:
        words[0] = _cap(words[0])
        body = " ".join(words)
    return body + rng.choice(_PUNCT[script])


def _mix_sentence(rng):
    """One `mix` sentence: a sentence from one of the four PROSE scripts,
    with roughly 1 chance in 6 of one emoji/symbol token (from
    `pool_mix.tsv`) appended -- the corpus that carries 4-byte
    characters (utf8_set_v1.md 4.2)."""
    src = rng.choice(PROSE_SCRIPTS)
    s = sentence(rng, src)
    if rng.randrange(6) == 0:
        s = s + " " + rng.choice(load_pool("mix"))
    return s


def _raw_sentence(rng, script):
    if script == "mix":
        return _mix_sentence(rng)
    return sentence(rng, script)


def _trim_to_char_boundary(data, nbytes):
    """THE SIZE-FITTING BOUNDARY RULE (see module docstring): the last
    complete UTF-8 character at or before byte offset `nbytes`, found by
    a decode-and-truncate walk-back. `data` itself is assumed well-formed
    UTF-8 (every caller here builds it from `str.encode("utf-8")`
    concatenations), so this never has to repair an ill-formed sequence
    -- it only has to avoid CUTTING a well-formed one in half."""
    k = min(nbytes, len(data))
    while k > 0:
        try:
            data[:k].decode("utf-8")
            return data[:k]
        except UnicodeDecodeError:
            k -= 1
    return b""


def decode_gate(data):
    """THE DECODE GATE (see module docstring): raises `UnicodeDecodeError`
    if `data` is not well-formed UTF-8. Every subject this module's
    callers write is passed through this before its manifest row is
    written."""
    data.decode("utf-8")


def text(nbytes, seed, script="mix"):
    """`nbytes` EXACTLY (never approximately -- see the boundary rule
    above) of prose in `script`, deterministic in `seed`. Composes
    sentences until at or past `nbytes`, trims back to the last complete
    character, then pads with ASCII spaces to the exact target size."""
    rng = Rng(seed)
    out = []
    total = 0
    while total < nbytes:
        s = _raw_sentence(rng, script)
        out.append(s)
        total += len(s.encode("utf-8")) + 1
    body = (" ".join(out) + " ").encode("utf-8")
    trimmed = _trim_to_char_boundary(body, nbytes)
    if len(trimmed) < nbytes:
        trimmed = trimmed + b" " * (nbytes - len(trimmed))
    assert len(trimmed) == nbytes, (len(trimmed), nbytes)
    decode_gate(trimmed)
    return trimmed
