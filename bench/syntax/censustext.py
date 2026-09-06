"""censustext.py -- the ONE randomness primitive and the shared VOCABULARY the
syntax census's generators draw from (`gen_throughput_subjects.py` builds
its large texts from the grammar here; `gen_subjects.py` hand-types its short
subjects from the same vocabulary so the two families speak one language).

WHY A VOCABULARY AT ALL. Every pattern in this set exercises ONE construct in
an otherwise plain body (NOTES.md, "The patterns"), and the bodies are drawn
from a small fixed word list -- `cat`, `item`, `done`, `key=value`, a date,
a time, a tag pair, a balanced paren expression, a quoted string, a doubled
word, a Latin-1 word -- so that ONE subject family serves every pattern: a
subject built to be a construct's whole-string hit is, for every other
pattern, a realistic near-miss or miss. The throughput texts are lines of
those same shapes at 64 KB .. 1 MB, so a pattern's per-byte cost on failing
text is measured on the alphabet its hits live in, not on a foreign corpus.

Deterministic: `Rng` is a small LCG-fed xorshift over `getrandbits`-style
draws with no dependence on python's `random` module, the clock or the
environment, so the manifests reproduce byte for byte on any box.

`periodic_field` is re-exported from `pcrecbench.periodic` so both
manifests here spell the `periodic` column by the harness's one definition.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from pcrecbench.periodic import periodic_field  # noqa: E402,F401


class Rng:
    """xorshift64* seeded from an integer; `below(n)` and `choice(seq)` are
    the only draws the generators make. Not python's `random` (whose stream
    is stable but whose API surface invites accidental extra draws)."""

    def __init__(self, seed):
        self.s = (seed * 0x9E3779B97F4A7C15 + 1) & 0xFFFFFFFFFFFFFFFF or 1

    def _next(self):
        x = self.s
        x ^= (x >> 12) & 0xFFFFFFFFFFFFFFFF
        x ^= (x << 25) & 0xFFFFFFFFFFFFFFFF
        x ^= (x >> 27) & 0xFFFFFFFFFFFFFFFF
        self.s = x & 0xFFFFFFFFFFFFFFFF
        return (x * 0x2545F4914F6CDD1D) & 0xFFFFFFFFFFFFFFFF

    def below(self, n):
        return (self._next() >> 11) % n

    def choice(self, seq):
        return seq[self.below(len(seq))]

    def chance(self, num, den):
        return self.below(den) < num


# ---------------------------------------------------------------- vocabulary

# The plain words. Lower-case ASCII letters only, so `\w+`, `[[:alpha:]]+`,
# `\p{L}+` and `(?[[a-z]-[aeiou]])+` all see them and a doubled word is the
# ONLY way `(\w+) \1` fires on prose.
WORDS = (
    "the cat sat on mat and dog did not care at all item done order shipped "
    "to for with from into over under again then when where which while "
    "colour red blue green small large quick slow warm cold near far open "
    "close ready busy idle late early plain simple clear dark light "
    "concatenate category dogma catalog items doneness keyed value other "
    "table chair house road river stone paper glass metal cloth wire rope "
    "pack track fact"
).split()

# Latin-1 words: bytes 0xE0-0xFF are letters to `\p{L}` (Unicode Latin-1
# Supplement) and NOT to `\w` under PCRE2's default C-locale tables. They
# are the census's one non-ASCII probe and stay inside 8-bit byte mode.
LATIN1 = (b"caf\xe9", b"na\xefve", b"r\xe9sum\xe9", b"\xe0", b"fa\xe7ade",
          b"\xfcber")

TAGS = ("b", "i", "u", "em", "code")
KEYS = ("key", "name", "colour", "size", "mode")
VALUES = ("value", "other", "red", "large", "fast", "off")
USERS = ("bob", "alice", "carol", "dave")


def _cap(rng, w):
    """Capitalise one word in ~1 of 12 draws, so `(?i)` shapes and the
    `(?^)` / `(?-i)` reset shapes have mixed case to disagree on."""
    return (w[:1].upper() + w[1:]) if rng.chance(1, 12) else w


def prose_line(rng, doubled=None):
    """6-12 plain words; `doubled` forces or forbids one doubled word (the
    backreference hit), otherwise it is drawn at 1 in 8."""
    n = 6 + rng.below(7)
    ws = [_cap(rng, rng.choice(WORDS)) for _ in range(n)]
    if doubled is None:
        doubled = rng.chance(1, 8)
    if doubled:
        i = rng.below(n - 1)
        ws[i + 1] = ws[i]
    if rng.chance(1, 10):
        ws[rng.below(n)] = rng.choice(LATIN1).decode("latin-1")
    return " ".join(ws)


def order_line(rng):
    return ("order %d shipped %04d-%02d-%02d at %02d:%02d to %s@example.com "
            "for $%d.%02d hex 0x%X"
            % (rng.below(9000) + 100, 2000 + rng.below(30), 1 + rng.below(12),
               1 + rng.below(28), rng.below(24), rng.below(60),
               rng.choice(USERS), rng.below(200), rng.below(100),
               rng.below(1 << 16)))


def tags_line(rng):
    """Two to four tag pairs; 1 in 6 pairs closes with the WRONG tag, the
    named-backreference near-miss."""
    parts = []
    for _ in range(2 + rng.below(3)):
        t = rng.choice(TAGS)
        close = rng.choice(TAGS) if rng.chance(1, 6) else t
        parts.append("<%s>%s</%s>" % (t, rng.choice(WORDS), close))
    return " and ".join(parts)


def paren_expr(rng, depth):
    """A balanced expression of nesting depth <= `depth` over one-letter
    names, the recursion patterns' hit."""
    if depth == 0 or rng.chance(1, 3):
        return rng.choice("abcdefghxyz")
    inner = ", ".join(paren_expr(rng, depth - 1) for _ in range(1 + rng.below(2)))
    return "%s(%s)" % (rng.choice("fgh"), inner)


def parens_line(rng):
    """Balanced expressions; 1 in 8 lines ends with an unbalanced `(`."""
    e = " + ".join(paren_expr(rng, 3) for _ in range(1 + rng.below(3)))
    if rng.chance(1, 8):
        e += " - (" + rng.choice(WORDS)
    return e


def kv_line(rng):
    out = []
    for _ in range(2 + rng.below(3)):
        k, v = rng.choice(KEYS), rng.choice(VALUES)
        sep = rng.choice(("=", " = ", "\t=\t", "= ", "\t"))
        out.append(k + sep + v)
    return " ".join(out)


def quoted_line(rng):
    q = '"%s"' % " ".join(rng.choice(WORDS) for _ in range(1 + rng.below(3)))
    tail = "'%s'" % rng.choice(WORDS)
    line = "say %s and %s" % (q, tail)
    if rng.chance(1, 8):
        line += ' and "' + rng.choice(WORDS)
    return line


# One draw decides the line KIND; the weights make prose the background and
# the structured shapes the sparse hits. `#` never appears anywhere (the
# floor pattern's throughput reading is a full-length miss), and no line
# carries a tab except a kv line's `\t=\t` separator.
KINDS = ((prose_line, 8), (order_line, 2), (tags_line, 1), (parens_line, 1),
         (kv_line, 1), (quoted_line, 1))
_TOTAL = sum(w for _f, w in KINDS)


def line(rng):
    r = rng.below(_TOTAL)
    for f, w in KINDS:
        if r < w:
            return f(rng)
        r -= w
    raise AssertionError


def text(seed, nbytes):
    """Exactly `nbytes` bytes of newline-terminated lines (the last line is
    cut at the byte boundary; a cut token is harmless and expected)."""
    rng = Rng(seed)
    out = bytearray()
    while len(out) < nbytes:
        s = line(rng)
        out += s.encode("latin-1") + b"\n"
    return bytes(out[:nbytes])
