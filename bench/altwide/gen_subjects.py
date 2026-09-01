#!/usr/bin/env python3
"""gen_subjects.py -- the wide-alternation sub-bench's short subjects:
`subjects/` (gitignored) + `manifest.tsv` (committed).

TWO FAMILIES from one grammar (`altwidetext.py`):

  FIELDS  3-20 B whole-string candidates for the `match` regime -- the thing
          a validator is handed whole. One branch from each rung and each
          structure pool (so every pattern has a whole-string hit), and four
          designed MISSES that fail for four different reasons: a branch
          with its last byte changed (fails on a byte), a proper PREFIX of a
          branch (fails because the pools are prefix-free, so no shorter
          branch rescues it), a branch buried in a longer letter run (the
          repeat succeeds, the end anchor fails -- and it is `wb-512`'s
          designed miss under search too), and a background word that is in
          no pool at all.

  LINES   <= 256 B of machine prose for the `search_short` regime. The
          background is BRANCH-FREE BY CONSTRUCTION (altwidetext.py's guard)
          and re-asserted here per subject, so every hit in this set is one
          this file placed. Thirteen lines carry exactly one branch at a
          DESIGNED position -- early (token 2), mid, or last -- and a
          designed IDENTITY: `main` word 0 is branch 1 of every rung, word
          7 is the LAST branch of `w-8` and the eighth of `w-2048`, word
          2047 is the last branch of `w-2048` alone. That is the
          leftmost-first arm: one subject reads as a late hit on a narrow
          rung and an early hit on a wide one, and the same word sits at a
          different branch index again in `srt-512`.

WHY THE POSITION AND THE IDENTITY ARE BOTH DESIGNED. A backtracker tries
branches in source order at every candidate start, so its cost on a hit is
(bytes scanned before the match) x (branches tried per byte) + (branch index
of the hit). An automaton pays neither. Separating the two terms needs the
same word early and late in one line (position) and different branch indices
at one position (identity), which is why both arms exist rather than one.

Every subject is ONE line with NO trailing newline, and no subject contains a
tab (the manifest is TSV).

The manifest carries the contract's four columns plus `periodic`
(`pcrecbench.periodic`, inbox I-10): every subject here reads `no`. The
`description` column names the FAMILY and the ARM in a fixed spelling --
`field/hit`, `field/near-miss`, `line/carry-early`, `line/background` -- so a
reader of a record can group subjects by what they were built to do without
a sixth manifest column (the loader takes four or five).

DETERMINISM: SEED below, `altwidetext.Rng` (getrandbits only), no clock, no
environment. Re-running reproduces the identical files and manifest.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import altwidetext as at  # noqa: E402

SEED = 20260901
OUT = os.path.join(HERE, "subjects")
MANIFEST = os.path.join(HERE, "manifest.tsv")

# requirements 3's "~256-byte subjects" for the short-search regime, and
# bench/email's band. The sidecar's `short_search_max_bytes` is 512, so
# every subject here is in BOTH short regimes.
MAX_LINE = 256


# ---------------------------------------------------------------- fields

def fields(rng, index, P):
    """(id, description, text). One hit per rung and per structure pool,
    plus the four designed misses."""
    main, short = P["main"], P["short"]
    out = []

    def hit(sid, word, note):
        out.append((sid, "field/hit %s" % note, word))

    hit("f-w0", main[0], "`main` word 0: branch 1 of every w-* rung, of "
        "ci-512, cnt-64 and wb-512, and branch %d of srt-512"
        % (sorted(main[:512]).index(main[0]) + 1))
    hit("f-w7", main[7], "`main` word 7: the LAST branch of w-8 and the "
        "eighth of every wider rung -- the leftmost-first identity arm")
    hit("f-w255", main[255], "`main` word 255: the last branch of w-256, "
        "absent from w-8 and w-64")
    hit("f-w511", main[511], "`main` word 511: the last branch of w-512, "
        "ci-512, srt-512 and wb-512")
    hit("f-w2047", main[2047], "`main` word 2047: the last branch of w-2048 "
        "and of no narrower rung")
    hit("f-s0", short[0], "`short` word 0: branch 1 of s-2048 and s-4096")
    hit("f-s4095", short[4095], "`short` word 4095: the last branch of "
        "s-4096 and of nothing else in the set")
    hit("f-sh1", P["sh1"][0], "`sh1` word 0: the shared-first-byte arm")
    hit("f-pfx3", P["pfx3"][0], "`pfx3` word 0: the shared-3-byte-prefix arm")
    hit("f-sfx", P["sfx"][0], "`sfx` word 0: the shared-suffix arm (the only "
        "patterns in the set with a PCRE2 required code unit)")
    hit("f-nar4", P["nar4"][0], "`nar4` word 0: the four-first-bytes arm")

    upper = main[0].upper()
    out.append(("f-upper", "field/hit `main` word 0 upper-cased: a whole-"
                "subject match for ci-512 and for nothing else", upper))

    i, j = cnt_pair(index, main)
    two = main[i] + main[j]
    out.append(("f-cnt2", "field/hit `main` words %d + %d concatenated: " % (i, j)
                + "two `main` branches concatenated: "
                "cnt-64 matches it WHOLE at two repetitions; every plain "
                "rung matches only its first half, so this is a match-regime "
                "miss for them and a search hit", two))

    a, near, pref = near_anchor(index, main)
    out.append(("f-near", "field/near-miss `main` word %d with its last byte "
                "changed: every branch is rejected on one byte" % a, near))
    out.append(("f-prefix", "field/near-miss a proper PREFIX of `main` word "
                "%d: no shorter branch rescues it because the pools are "
                "prefix-free" % a, pref))

    glued = at.glue(rng, index, main[0])
    out.append(("f-glued", "field/near-miss `main` word 0 buried in a longer "
                "letter run: a search hit for every plain rung, a MISS for "
                "wb-512, and a match-regime miss for all of them", glued))

    bg = at.background_word(rng, index, 8, 12)
    out.append(("f-bg", "field/miss a background word in no pool: the "
                "all-miss control", bg))
    return out


def cnt_pair(index, main):
    """The two `w-64` branch indices whose CONCATENATION carries exactly
    those two branches and no third.

    Chosen by search rather than by hand because a join can manufacture a
    branch that spans it -- `main[3] + main[9]` does, which is how this
    function came to exist. The first pair in index order wins, so the
    choice is a function of the pool and not of a seed."""
    for i in range(64):
        for j in range(64):
            if i == j:
                continue
            two = main[i] + main[j]
            if index.occurrences(two) == [(0, main[i]), (len(main[i]), main[j])]:
                return i, j
    raise AssertionError("no clean two-branch concatenation inside w-64")


def near_anchor(index, main):
    """-> (i, near, prefix): the lowest `w-8` branch index whose one-byte
    substitution AND whose proper prefix are both branch-free.

    Searched rather than fixed, for the same reason `cnt_pair` is: changing
    one byte of a word can MANUFACTURE a different branch inside it (word 0's
    own substitutions do), and a near-miss that accidentally contains a hit
    is not a near-miss. `near` takes the first substituting letter in
    alphabet order that leaves the string branch-free, so the pair is a
    function of the pool alone."""
    for i in range(8):
        w = main[i]
        if len(w) < 4 or not index.clean(w[:-1]):
            continue
        for c in at.ALPHABET:
            if c == w[-1]:
                continue
            cand = w[:-1] + c
            if index.clean(cand):
                return i, cand, w[:-1]
    raise AssertionError("no clean near-miss anchor inside w-8")


# ----------------------------------------------------------------- lines

# (id, pool, word index, placement, prose target). `placement` is where the
# branch token goes: `early` is token 2 (right after the `#NNNN` prefix),
# `last` is the final token, `mid` is the middle of the line.
CARRY = (
    ("l-w0-early",    "main", 0,    "early", 236),
    ("l-w0-last",     "main", 0,    "last",  236),
    ("l-w7-mid",      "main", 7,    "mid",   232),
    ("l-w255-mid",    "main", 255,  "mid",   228),
    ("l-w511-last",   "main", 511,  "last",  230),
    ("l-w1023-early", "main", 1023, "early", 234),
    ("l-w2047-early", "main", 2047, "early", 226),
    ("l-s4095-mid",   "short", 4095, "mid",  240),
    ("l-sh1-mid",     "sh1",  3,    "mid",   230),
    ("l-pfx3-mid",    "pfx3", 3,    "mid",   228),
    ("l-sfx-mid",     "sfx",  3,    "mid",   230),
    ("l-nar4-mid",    "nar4", 3,    "mid",   232),
)

# Lines whose carried token is a DERIVED form rather than a bare branch.
DERIVED = (
    ("l-upper", "mid", 230),
    ("l-glued", "mid", 228),
    ("l-cnt2",  "mid", 226),
)

BACKGROUND = (("l-bg-0", 240), ("l-bg-1", 232), ("l-bg-2", 248),
              ("l-bg-3", 220), ("l-bg-4", 244), ("l-bg-5", 236))


def _line(rng, index, token, place, target):
    """A `#NNNN`-prefixed prose line carrying `token` at `place`, <= MAX_LINE."""
    body = at.background_prose(
        rng, index, max(8, target - len(token) - 14)).split(" ")
    words = [at.line_prefix(rng)] + body
    if place == "early":
        at_i = 1
    elif place == "last":
        at_i = len(words)
    else:
        at_i = 1 + len(body) // 2
    words.insert(at_i, token)
    text = " ".join(words)
    assert len(text) <= MAX_LINE, (len(text), text[:60])
    return text, sum(len(w) + 1 for w in words[:at_i])


def lines(rng, index, P):
    out = []
    for sid, pool, i, place, target in CARRY:
        word = P[pool][i]
        text, off = _line(rng, index, word, place, target)
        assert index.occurrences(text) == [(off, word)], sid
        out.append((sid, "line/carry-%s `%s` word %d at byte %d of %d"
                    % (place, pool, i, off, len(text)), text))
    for sid, place, target in DERIVED:
        if sid == "l-upper":
            token = P["main"][0].upper()
            note = ("an upper-cased `main` word 0: a hit for ci-512 and for "
                    "nothing else in the set")
            expect = []
        elif sid == "l-glued":
            token = at.glue(rng, index, P["main"][0])
            note = ("`main` word 0 buried in a longer letter run: a hit for "
                    "every plain rung, a MISS for wb-512")
            expect = [(token.index(P["main"][0]), P["main"][0])]
        else:
            ci, cj = cnt_pair(index, P["main"])
            token = P["main"][ci] + P["main"][cj]
            note = ("`main` words %d + %d adjacent: cnt-64 takes both in one "
                    "match, every plain rung takes the first" % (ci, cj))
            expect = [(0, P["main"][ci]), (len(P["main"][ci]), P["main"][cj])]
        text, off = _line(rng, index, token, place, target)
        assert index.occurrences(text) == [(off + a, w) for a, w in expect], sid
        out.append((sid, "line/carry-derived %s" % note, text))
    for sid, target in BACKGROUND:
        words = [at.line_prefix(rng)] + at.background_prose(
            rng, index, target - 14).split(" ")
        text = " ".join(words)
        assert len(text) <= MAX_LINE, (sid, len(text))
        assert index.clean(text), sid
        out.append((sid, "line/background prose in no pool: the failing "
                    "majority the search band is built from", text))
    return out


def build():
    rng = at.Rng(SEED)
    P = at.pools()
    index = at.BranchIndex()
    return fields(rng, index, P) + lines(rng, index, P), index


def main():
    subjects, index = build()
    os.makedirs(OUT, exist_ok=True)
    rows = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, desc, text in subjects:
        b = text.encode("latin-1")
        assert b"\n" not in b and b"\t" not in b, sid
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(b)
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(b), hashlib.sha256(b).hexdigest(), desc,
            at.periodic_field(b)))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(rows) + "\n")
    sizes = [len(t) for _s, _d, t in subjects]
    print("gen_subjects: %d subjects (%d B, %d..%d) -> %s, manifest -> %s"
          % (len(subjects), sum(sizes), min(sizes), max(sizes), OUT, MANIFEST))


if __name__ == "__main__":
    main()
