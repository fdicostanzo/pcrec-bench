#!/usr/bin/env python3
"""altwidetext.py -- the GRAMMAR of the wide-alternation sub-bench: the branch
word pools every pattern is built from, the background prose the subjects are
built from, and the one randomness primitive both draw on.

WHY A WORD POOL AND NOT A DICTIONARY. Requirements 5 wants subjects generated
deterministically by a committed script; a dictionary file would be a corpus
with a licence question and a box dependency, and the words' MEANING is worth
nothing here -- what the patterns measure is branch COUNT and branch
STRUCTURE. So every branch literal is drawn from `Rng`, and the pools below
are the only place a branch word is ever invented.

THE FOUR PROPERTIES EVERY POOL HAS, and each is a design decision this set
rests on:

  1. DISTINCT. No word appears twice in a pool, so a pattern's branch count
     is its width and not "its width minus the collisions".

  2. SUBSTRING-FREE, GLOBALLY. No word of any pool occurs anywhere inside
     any other word of any pool. Two things rest on this. (a) The ORDER arm
     is a clean control: leftmost-first alternation can only return a
     different span when two branches match at the same start position, and
     two literals matching at one position means the shorter is a PREFIX of
     the longer -- so `w-512` and `srt-512`, the same 512 branches in
     generation order and sorted by first byte, are ANSWER-IDENTICAL and
     everything the two rows differ by is cost. (b) "This subject carries
     exactly one branch" becomes something a generator can PLACE and ASSERT,
     because a placed branch can neither contain a second one nor sit inside
     a third. Prefix-freeness alone gives (a) but not (b), and (b) is what
     the whole hit-allocation design needs.

  3. NESTED. Pool word i is branch i of every rung wide enough to hold it:
     `w-8`'s branches are `w-64`'s first eight, and so on to `w-4096`. The
     width ladder therefore ADDS branches rather than redrawing them, which
     is what makes a rung-to-rung difference a width difference. It also
     gives the leftmost-first arm for free: word 7 is the LAST branch of
     `w-8` and the eighth of 4096 in `w-4096`, so one subject reads as a
     late hit on one rung and an early hit on another.

  4. FIRST BYTES DRAWN THE WAY THE ARM DECLARES. The `main` pool draws the
     first byte uniformly over the 26 lowercase letters (the SPREAD arm: at
     width W each letter heads about W/26 branches and, in generation order,
     the maximal run of branches sharing a first byte is 1 or 2). The other
     pools fix it (`sh1`: every branch starts `k`), fix three bytes
     (`pfx3`: every branch starts `qux`), fix the last three (`sfx`: every
     branch ends `ing`), or draw it from four letters (`nar4`). Those five
     shapes are what PCRE2's first-code-unit / required-code-unit analysis
     and an AOT compiler's prefilter derivation see differently; the
     `pattern_facts.tsv` columns state each pattern's realised structure
     rather than this header's intention.

THE BACKGROUND IS BRANCH-FREE BY CONSTRUCTION. `background_word()` redraws
until the word contains NO branch of ANY pool as a substring, and every
subject is built by joining such words (and digit/bracket tokens) with
spaces. A branch literal is pure lowercase letters, so it can never span a
space or a digit: the invariant is therefore that EVERY maximal lowercase
run in a subject is either a background word the guard passed or a branch
the generator deliberately placed. `gen_subjects.py` asserts that per
subject rather than trusting it. Without the guard the match rate would be
an accident of the seed -- at width 4096 about one branch in ten is three
bytes long, and a 256-byte prose line has ~250 three-byte windows, so
several accidental hits per line is the EXPECTED number, not a tail risk.
(bench/loglines' lesson, one step further: that set allocated its hits
exactly instead of flipping a coin; this set has to exclude them first.)

DETERMINISM. One primitive, `random.Random(seed).getrandbits(32)`, which
CPython documents as stable; `Rng` builds every draw on it. `choice`,
`sample`, `randrange`, `shuffle` are not used: their internals have moved
between CPython releases and a committed manifest cannot rest on that.
(The same posture, for the same reason, as bench/bounded/boundedtext.py and
bench/loglines/logtext.py.)
"""

import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))

from pcrecbench.periodic import (periodic_field,  # noqa: E402,F401
                                 smallest_period)

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# The shortest branch literal the set carries, and so the shortest substring
# the substring-free property is enforced over.
MIN_WORD = 3

# The two fixed affixes below are never allowed to become words in their own
# right: every `sfx` branch contains `ing` and every `pfx3` branch contains
# `qux`, so a pool that had accepted either as a standalone word would make
# its own arm undrawable (2.3 % of the time, measured on this seed's
# alphabet, `main` would otherwise have drawn one of them). Reserving them is
# one line here rather than a draw-order rule nobody can see.
RESERVED = frozenset(("qux", "ing"))

# The pool seed. ONE seed for every branch pool, so the pools are a single
# reproducible draw: gen_patterns.py, gen_subjects.py, gen_throughput_subjects
# .py and gen_oracle_limits.py all call `pools()` and all get the same words.
POOL_SEED = 20260901


class Rng:
    """The one randomness primitive (see the module header)."""

    def __init__(self, seed):
        self._r = random.Random(seed)

    def below(self, n):
        return self._r.getrandbits(32) % n

    def between(self, lo, hi):
        """Inclusive on both ends."""
        return lo + self.below(hi - lo + 1)

    def pick(self, seq):
        return seq[self.below(len(seq))]

    def letters(self, n):
        return "".join(self.pick(ALPHABET) for _ in range(n))

    def digits(self, n):
        return "".join(self.pick("0123456789") for _ in range(n))


# ------------------------------------------------------------- word pools

class SubstringFreeSet:
    """Accumulates DISTINCT, SUBSTRING-FREE words (property 2 above).

    No accepted word occurs anywhere inside another accepted word, and the
    set is GLOBAL across every pool -- which is stronger than prefix-freeness
    and is what the whole subject design rests on. Prefix-freeness alone
    makes leftmost-first order-independent; substring-freeness additionally
    makes "this text carries exactly one branch" a statement a generator can
    place and assert, because a placed branch cannot contain a second one and
    cannot sit inside a third. Without it, `main` word 0 turns out to carry
    two shorter branches of its own and every per-subject assertion in
    `gen_subjects.py` fails -- which is how this class came to replace the
    prefix-free one it began as.

    `accepted` is the words; `subs` is every substring of length >= MIN_WORD
    of every accepted word (the word itself included), which makes "is this
    candidate inside something already accepted?" one lookup."""

    def __init__(self):
        self.words = []
        self.accepted = set()
        self.subs = set()

    def offer(self, w):
        """-> True if `w` was accepted."""
        if w in RESERVED or w in self.subs:
            return False
        n = len(w)
        for i in range(n):
            for j in range(i + MIN_WORD, n + 1):
                if (i, j) != (0, n) and w[i:j] in self.accepted:
                    return False
        self.words.append(w)
        self.accepted.add(w)
        for i in range(n):
            for j in range(i + MIN_WORD, n + 1):
                self.subs.add(w[i:j])
        return True


def draw_pool(rng, shared, n, lo, hi, first=None, prefix="", suffix=""):
    """`n` distinct words of `lo`..`hi` bytes, accepted into the SHARED
    substring-free set and returned as this pool's own list.

    `first` fixes the first byte to one of the given letters (a string of
    candidates, drawn per word); `prefix` / `suffix` fix a whole literal
    affix. A word is `prefix` + body + `suffix` with the total length in
    [lo, hi], so `lo` must leave the body at least one byte."""
    out = []
    guard = 0
    while len(out) < n:
        guard += 1
        if guard > 400 * n + 10000:
            raise AssertionError("draw_pool did not converge: %d/%d"
                                 % (len(out), n))
        total = rng.between(lo, hi)
        body_len = total - len(prefix) - len(suffix)
        if body_len < 1:
            continue
        body = rng.letters(body_len)
        if first is not None and not prefix:
            body = rng.pick(first) + body[1:]
        w = prefix + body + suffix
        if shared.offer(w):
            out.append(w)
    return out


# The pools, and the arm each one exists to spell. Every entry is
# (name, count, lo, hi, first, prefix, suffix); `main` is the width ladder's
# and is the largest, so it is drawn first and its words are the ones the
# subjects are built around.
POOL_SPECS = (
    # the SPREAD arm and the width ladder: first byte uniform over 26
    ("main", 4096, 3, 12, None, "", ""),
    # every branch starts with the same byte (PCRE2 gets a first code unit;
    # an AOT prefilter gets one memchr; a prefix-factoring pass gets one
    # maximal run as wide as the whole alternation)
    ("sh1", 512, 3, 12, "k", "", ""),
    # every branch starts with the same THREE bytes: the same lever one
    # trie level deeper
    ("pfx3", 512, 6, 12, None, "qux", ""),
    # every branch ends with the same three bytes: PCRE2 gets a REQUIRED
    # code unit where the spread arm has none
    ("sfx", 512, 6, 12, None, "", "ing"),
    # first byte from four letters: a start bitmap with four bits set,
    # between the one-byte and the 26-byte arms
    ("nar4", 512, 3, 12, "bgmt", "", ""),
    # SHORT branch words, spread first bytes, and the reason they exist is
    # the oracle's own ceiling: libpcre2 refuses `main`'s 4096-way
    # alternation outright ("regular expression is too large" -- its
    # LINK_SIZE 2 compiled-size limit; `oracle_limits.tsv` carries the
    # probe), and an expectation the oracle cannot state is a cell the
    # harness cannot judge. 3-6 byte branches compile at 4096, so the
    # brief's 4096-way rung is reachable with branch LENGTH as the thing
    # that moved -- and `s-2048` beside `w-2048` is the control that says
    # by how much. APPENDED LAST so every pool above is byte-identical to
    # the draw before this arm existed.
    ("short", 4096, 3, 6, None, "", ""),
)

_POOLS = None


def pools():
    """-> {name: [word, ...]}, drawn once per process from `POOL_SEED`.

    One `Rng` walks the specs in order, so every pool's words are a function
    of the seed and the spec table alone -- adding a pool at the END leaves
    the earlier pools byte-identical, exactly as bench/bounded's throughput
    generator appends its 0.2 subject last."""
    global _POOLS
    if _POOLS is None:
        rng = Rng(POOL_SEED)
        shared = SubstringFreeSet()
        got = {}
        for name, n, lo, hi, first, prefix, suffix in POOL_SPECS:
            got[name] = draw_pool(rng, shared, n, lo, hi, first, prefix, suffix)
        _POOLS = got
    return _POOLS


def probe_pool(name, n):
    """The first `n` words of pool `name`, drawn BEYOND the count the set
    carries -- what `gen_oracle_limits.py` needs to find the width at which
    the oracle refuses a skeleton.

    Replays the same single-`Rng` walk `pools()` does and stops at `name`,
    so the first `POOL_SPECS[name]` words are byte-identical to `pools()
    [name]` (an accept in `draw_pool` depends only on the words already
    accepted, so a longer draw EXTENDS a shorter one) and the continuation
    is the natural one. Nothing after `name` in the spec table is drawn,
    which is why this is a probe helper and not a second definition of the
    pools."""
    rng = Rng(POOL_SEED)
    shared = SubstringFreeSet()
    for spec_name, count, lo, hi, first, prefix, suffix in POOL_SPECS:
        want = max(n, count) if spec_name == name else count
        words = draw_pool(rng, shared, want, lo, hi, first, prefix, suffix)
        if spec_name == name:
            return words[:n]
    raise KeyError(name)


def all_branch_words():
    """Every branch literal of every pattern in the set, as one set -- what
    the background guard excludes."""
    out = set()
    for words in pools().values():
        out.update(words)
    return out


# ------------------------------------------------------- the branch finder

class BranchIndex:
    """Substring search for ANY branch word, by length-bucketed set lookup.

    The set holds words of 3..12 bytes, so a text of n bytes has at most
    10*n windows to test and each test is one hash lookup. That is fast
    enough to run on every generated token AND as an assertion over every
    finished subject, which is the point: the branch-free claim is CHECKED,
    never assumed."""

    def __init__(self, words=None):
        words = all_branch_words() if words is None else set(words)
        self.by_len = {}
        for w in words:
            self.by_len.setdefault(len(w), set()).add(w)
        self.lengths = sorted(self.by_len)

    def occurrences(self, text):
        """Every (start, word) a branch occupies in `text`, in start order."""
        hits = []
        n = len(text)
        for i in range(n):
            for L in self.lengths:
                if i + L > n:
                    break
                w = text[i:i + L]
                if w in self.by_len[L]:
                    hits.append((i, w))
        return hits

    def clean(self, text):
        return not self.occurrences(text)


# ----------------------------------------------------------- the prose

# Background tokens that are NOT pure letter runs, so they break any letter
# run a branch could otherwise be found in.
def line_prefix(rng):
    """The first token of every LINE subject: `#` and four digits.

    `#` is the FLOOR pattern, and this is the only place it occurs -- so the
    floor is a hit at offset 0 on every line, a whole-subject miss on every
    field, and a full-length `memchr` miss over every throughput subject.
    Three different readings of the harness's own per-call overhead from one
    one-byte pattern (NOTES.md, "The floor pattern")."""
    return "#%04d" % rng.below(10000)


def _numeric(rng):
    return rng.digits(rng.between(1, 4))


def _kv(rng, index):
    return "%s=%s" % (background_word(rng, index, 3, 6), _numeric(rng))


def background_word(rng, index, lo=3, hi=12):
    """One lowercase word that contains NO branch of any pool as a substring.

    Redraws until the guard passes (the module header says why the guard is
    necessary rather than paranoid). The rejection rate is a few percent, so
    this converges in one or two draws in the overwhelming majority of
    cases; the bound is asserted rather than left implicit."""
    for _ in range(2000):
        w = rng.letters(rng.between(lo, hi))
        if index.clean(w):
            return w
    raise AssertionError("no branch-free background word in 2000 draws")


def background_token(rng, index):
    """One background token, weighted so a line reads as machine prose and
    so roughly a fifth of the tokens are not pure letter runs."""
    k = rng.below(100)
    if k < 76:
        return background_word(rng, index)
    if k < 88:
        return _kv(rng, index)
    return _numeric(rng)


def background_prose(rng, index, nbytes):
    """Background tokens, space-joined, to at least `nbytes` bytes."""
    out = []
    size = -1
    while size < nbytes:
        t = background_token(rng, index)
        out.append(t)
        size += len(t) + 1
    return " ".join(out)


def glue(rng, index, word, pad_lo=2, pad_hi=3):
    """`word` buried inside a LONGER letter run: letters on both sides, drawn
    until the whole run contains `word` and nothing else from any pool.

    This is the `\\b` arm's designed near-miss -- a substring hit for every
    plain rung, a MISS for `wb-512` -- and the `match` regime's "a longer
    word containing a branch"."""
    for _ in range(2000):
        left = rng.letters(rng.between(pad_lo, pad_hi))
        right = rng.letters(rng.between(pad_lo, pad_hi))
        run = left + word + right
        hits = index.occurrences(run)
        if hits == [(len(left), word)]:
            return run
    raise AssertionError("no clean glue for %r in 2000 draws" % word)
