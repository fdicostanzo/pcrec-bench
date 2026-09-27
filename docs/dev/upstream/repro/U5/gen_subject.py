#!/usr/bin/env python3
"""Standalone re-implementation of pcrec-bench's bench/syntax/censustext.py
line grammar (xorshift RNG + line-kind mix), for the U5 upstream repro.
Not imported from the bench tree -- transcribed so the repro is
self-contained. Produces byte-identical text to the bench's own
t-64k/t-256k/t-1m subjects at the same (seed, nbytes) pair.
"""
import sys


class Rng:
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


WORDS = (
    "the cat sat on mat and dog did not care at all item done order shipped "
    "to for with from into over under again then when where which while "
    "colour red blue green small large quick slow warm cold near far open "
    "close ready busy idle late early plain simple clear dark light "
    "concatenate category dogma catalog items doneness keyed value other "
    "table chair house road river stone paper glass metal cloth wire rope "
    "pack track fact"
).split()

LATIN1 = (b"caf\xe9", b"na\xefve", b"r\xe9sum\xe9", b"\xe0", b"fa\xe7ade",
          b"\xfcber")

TAGS = ("b", "i", "u", "em", "code")
KEYS = ("key", "name", "colour", "size", "mode")
VALUES = ("value", "other", "red", "large", "fast", "off")
USERS = ("bob", "alice", "carol", "dave")


def _cap(rng, w):
    return (w[:1].upper() + w[1:]) if rng.chance(1, 12) else w


def prose_line(rng, doubled=None):
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
    parts = []
    for _ in range(2 + rng.below(3)):
        t = rng.choice(TAGS)
        close = rng.choice(TAGS) if rng.chance(1, 6) else t
        parts.append("<%s>%s</%s>" % (t, rng.choice(WORDS), close))
    return " and ".join(parts)


def paren_expr(rng, depth):
    if depth == 0 or rng.chance(1, 3):
        return rng.choice("abcdefghxyz")
    inner = ", ".join(paren_expr(rng, depth - 1) for _ in range(1 + rng.below(2)))
    return "%s(%s)" % (rng.choice("fgh"), inner)


def parens_line(rng, allow_unbalanced=True):
    e = " + ".join(paren_expr(rng, 3) for _ in range(1 + rng.below(3)))
    unbalanced = rng.chance(1, 8)  # draw consumed either way -- keeps the
    if unbalanced and allow_unbalanced:  # RNG stream position identical
        e += " - (" + rng.choice(WORDS)  # between allow_unbalanced=True/False
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


KINDS = ((prose_line, 8), (order_line, 2), (tags_line, 1), (parens_line, 1),
         (kv_line, 1), (quoted_line, 1))
_TOTAL = sum(w for _f, w in KINDS)


def line(rng, allow_unbalanced=True):
    r = rng.below(_TOTAL)
    for f, w in KINDS:
        if r < w:
            if f is parens_line:
                return f(rng, allow_unbalanced=allow_unbalanced)
            return f(rng)
        r -= w
    raise AssertionError


def text(seed, nbytes, allow_unbalanced=True):
    """allow_unbalanced=False produces a BALANCED-ONLY control -- every
    parens_line's own 1-in-8 draw is still consumed (so the RNG stream,
    and therefore every OTHER line in the text, is identical either
    way), but the unbalanced trailing `- (word` tail is never appended.
    Manager review 2026-09-27 (item 1): this isolates whether U5's
    super-linear cost comes from the RECURSION construct itself or
    from the deliberately-unbalanced lines the grammar plants."""
    rng = Rng(seed)
    out = bytearray()
    while len(out) < nbytes:
        s = line(rng, allow_unbalanced=allow_unbalanced)
        out += s.encode("latin-1") + b"\n"
    return bytes(out[:nbytes])


if __name__ == "__main__":
    seed = int(sys.argv[1])
    nbytes = int(sys.argv[2])
    outpath = sys.argv[3]
    allow_unbalanced = (sys.argv[4] != "0") if len(sys.argv) > 4 else True
    body = text(seed, nbytes, allow_unbalanced=allow_unbalanced)
    assert len(body) == nbytes
    with open(outpath, "wb") as f:
        f.write(body)
