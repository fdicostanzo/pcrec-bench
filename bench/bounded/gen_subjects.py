#!/usr/bin/env python3
"""gen_subjects.py -- the bounded-repeat sub-bench's subjects: `subjects/`
(gitignored) + `manifest.tsv` (committed).

Three families from one grammar (`boundedtext.py`, whose header says why
three): FIELDS (4-65 B whole-string candidates, each everyday shape as its
exact match, its last-repetition near-miss and its end-anchor over-run),
LINES (80-1000 B ops prose, near-miss background, the everyday shapes
injected into an exactly allocated minority, and the bounded-context lines
with a trigger word and a context word at a DESIGNED gap), and RUNS
(random letters / digits at the count ladder's rungs and one off them).

Every subject is ONE line with NO trailing newline: `.` does not match `\\n`,
so a trailing newline would make every `.{80,}`-class whole-subject match
fail for a reason that has nothing to do with bounded repeats.

The manifest carries the contract's four columns plus `periodic` (inbox
I-10, `pcrecbench.periodic`): every subject here reads `no`, the runs
included, because the runs are random within their class rather than a
repeated byte (boundedtext.py's header).

The `description` column names the FAMILY and the ARM in a fixed spelling
-- `field/match`, `field/near-miss`, `field/over-run`, `line/ctx-gap-32`,
`line/ctx-no-context`, `line/background`, `run/letters`, `run/digits` -- so
a reader of the record can group subjects by what they were built to do
without a sixth manifest column (the loader accepts four or five).

DETERMINISM: SEED below, `boundedtext.Rng` (getrandbits only), no clock, no
environment. Re-running reproduces the identical files and manifest.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import boundedtext as bt  # noqa: E402

SEED = 20260829
OUT = os.path.join(HERE, "subjects")
MANIFEST = os.path.join(HERE, "manifest.tsv")

# Lines are capped at MAX_LINE bytes and the sidecar's short_search_max_bytes
# is 1024, so every field and every line is in the search band; only the
# 4096- and 16384-byte runs are match-regime-only.
MAX_LINE = 1000

# ---------------------------------------------------------------- fields

def fields(rng):
    """(id, description, text) for the everyday shapes' whole-string
    candidates. The three arms per shape are the point: the exact match, the
    near-miss that fails AT THE LAST REPETITION (one unit short), and the
    over-run that matches the repeat but fails at the end anchor."""
    out = []
    y = nonperiodic(rng, bt.year4, lambda v: v[:3])
    out.append(("f-year-4", "field/match year4: 4 digits", y))
    out.append(("f-year-3", "field/near-miss year4: 3 digits, fails at the 4th repetition", y[:3]))
    out.append(("f-year-5", "field/over-run year4: 5 digits, the repeat is satisfied and \\z fails", nonperiodic(rng, lambda r: y + r.digits(1))))
    h = nonperiodic(rng, bt.hex32, lambda v: v[:31], lambda v: v[:31] + "g")
    out.append(("f-hex-32", "field/match hex32: 32 hex", h))
    out.append(("f-hex-31", "field/near-miss hex32: 31 hex, fails at the 32nd repetition", h[:31]))
    out.append(("f-hex-32g", "field/near-miss hex32: 31 hex then `g`, fails at the 32nd repetition on a wrong byte", h[:31] + "g"))
    out.append(("f-pw-8", "field/match pw-8-64: 8 bytes, the exact minimum", nonperiodic(rng, lambda r: bt.password(r, 8))))
    out.append(("f-pw-7", "field/near-miss pw-8-64: 7 bytes, fails at the 8th repetition", nonperiodic(rng, lambda r: bt.password(r, 7))))
    out.append(("f-pw-64", "field/match pw-8-64: 64 bytes, the exact maximum", nonperiodic(rng, lambda r: bt.password(r, 64))))
    out.append(("f-pw-65", "field/over-run pw-8-64: 65 bytes, the repeat is satisfied at 64 and \\z fails", nonperiodic(rng, lambda r: bt.password(r, 65))))
    q = nonperiodic(rng, bt.dotted4, lambda v: v.rsplit(".", 1)[0])
    out.append(("f-quad-4", "field/match dotted4: four octets", q))
    out.append(("f-quad-3", "field/near-miss dotted4: three octets, fails inside the 3rd group repetition", q.rsplit(".", 1)[0]))
    out.append(("f-quad-4x", "field/over-run dotted4: last octet has 4 digits, \\z fails", nonperiodic(rng, lambda r: q + r.digits(1))))
    m = nonperiodic(rng, bt.mac6, lambda v: v[:14])
    out.append(("f-mac-6", "field/match mac6: six groups", m))
    out.append(("f-mac-5", "field/near-miss mac6: five groups, fails at the 5th `{5}` repetition's separator", m[:14]))
    c = nonperiodic(rng, bt.csv5, lambda v: v.rsplit(",", 1)[0])
    out.append(("f-csv-5", "field/match csv5: five fields", c))
    out.append(("f-csv-4", "field/near-miss csv5: four fields, fails at the 4th `{4}` repetition's comma", c.rsplit(",", 1)[0]))
    return out


# ----------------------------------------------------------------- lines

# The bounded-context lines. `gap` is the designed distance in bytes between
# the trigger word and the context word (the prose between is drawn to at
# least that many bytes, so the realised gap is `gap` plus the tail of one
# token and two spaces; the manifest states the realised one); `whole` means
# the line STARTS with the trigger and ENDS with the context word, so it is
# a whole-subject match for every ctx rung whose count covers the gap.
# `kind = "no-context"` is the failing arm the hazard measures: a trigger
# with no context word after it, so a lazy gap walks its full count on every
# trigger occurrence and finds nothing.
CTX_LINES = (
    # id,     total, gap,  kind
    ("l-00", None, 32,   "whole"),
    ("l-01", None, 128,  "whole"),
    ("l-02", None, 512,  "gap"),
    ("l-03", None, 840,  "gap"),
    ("l-04", 500,  None, "no-context"),
    ("l-05", 1000, None, "no-context"),
    ("l-06", 300,  None, "wrong-order"),
    ("l-07", 150,  None, "near-miss"),
)
BACKGROUND_LINES = (("l-08", 120), ("l-09", 400), ("l-10", 250), ("l-11", 800))

# HOW MANY of the ten non-whole lines carry each everyday shape -- an exact
# allocation without replacement (bench/loglines' lesson: a per-line coin
# flip at n=10 would make the match rate an accident of the seed). The two
# `whole` ctx lines are not in the pool: an injected token would break
# "ends with the context word".
COUNTS = (("year4", 3), ("hex32", 2), ("dotted4", 3), ("mac6", 2), ("csv5", 2))
SHAPES = {"year4": bt.year4, "hex32": bt.hex32, "dotted4": bt.dotted4,
          "mac6": bt.mac6, "csv5": bt.csv5}


def _pad(rng, parts, total):
    """Space-join `parts`, pad with background prose to about `total` bytes,
    then cut at a word gap so the line never exceeds MAX_LINE."""
    text = " ".join(parts)
    if total is not None and len(text) < total:
        text = text + " " + bt.prose(rng, total - len(text) - 1)
    if len(text) > MAX_LINE:
        text = text[:MAX_LINE].rsplit(" ", 1)[0]
    return text


def _inject(rng, words, shapes, lo, hi):
    """Insert each drawn shape as its own token at a random word gap between
    word indices `lo` and `hi` (so a ctx line's structure is preserved)."""
    for name in shapes:
        at = rng.between(lo, hi)
        words.insert(at, SHAPES[name](rng))
        hi += 1
    return words


def lines(rng):
    pool = [row[0] for row in CTX_LINES if row[3] != "whole"] \
        + [row[0] for row in BACKGROUND_LINES]
    assigned = {i: [] for i in pool}
    for name, k in COUNTS:
        for i in rng.shuffled_indices(len(pool))[:k]:
            assigned[pool[i]].append(name)
    out = []
    for sid, total, gap, kind in CTX_LINES:
        trig, ctx = rng.pick(bt.TRIGGERS), rng.pick(bt.CONTEXTS)
        if kind == "whole":
            text = " ".join([trig, bt.prose(rng, gap), ctx])
            desc = ("line/ctx-gap-%d whole: starts with `%s`, ends with `%s`, %d B between -- a "
                    "whole-subject match for every ctx rung whose count covers the gap"
                    % (gap, trig, ctx, len(text) - len(trig) - len(ctx)))
            out.append((sid, desc, text))
            continue
        head = [bt.prefix(rng)] + bt.prose(rng, 20).split(" ")
        if kind == "gap":
            between = bt.prose(rng, gap).split(" ")
            words = head + [trig] + between + [ctx]
            realised = sum(len(w) + 1 for w in between) + 1
            desc = "line/ctx-gap-%d: `%s` then `%s` %d B later, mid-line" % (gap, trig, ctx, realised)
            lo, hi = 1, len(head)          # inject BEFORE the trigger only
        elif kind == "no-context":
            words = head + [trig]
            desc = ("line/ctx-no-context: trigger `%s` and no context word after it (the lazy gap "
                    "walks its full count and finds nothing)" % trig)
            lo, hi = 1, len(words)
        elif kind == "wrong-order":
            words = head + [ctx] + bt.prose(rng, 40).split(" ") + [trig]
            desc = "line/ctx-wrong-order: context word `%s` BEFORE trigger `%s`" % (ctx, trig)
            lo, hi = 1, len(words)
        else:
            body = [rng.pick(bt.NEAR_WORDS) if rng.below(2) else rng.pick(bt.WORDS)
                    for _ in range(6)]
            words = head + body
            desc = ("line/ctx-near-miss: `%s`/`%s`-class near-miss words only, no whole-word trigger "
                    "or context" % (trig, ctx))
            lo, hi = 1, len(words)
        if assigned[sid]:
            words = _inject(rng, words, assigned[sid], lo, hi)
            desc += "; shapes: " + "+".join(assigned[sid])
        text = _pad(rng, words, total)
        # A gap line is never padded or cut: its context word must be the
        # last token, and the designed gap is what keeps it under MAX_LINE.
        assert kind != "gap" or (len(text) <= MAX_LINE and text.endswith(ctx)), sid
        out.append((sid, desc, text))
    for sid, total in BACKGROUND_LINES:
        words = _pad(rng, [bt.prefix(rng)], total).split(" ")
        words = _inject(rng, words, assigned[sid], 1, len(words))
        desc = "line/background: ops prose of near-misses" + (
            "; shapes: " + "+".join(assigned[sid]) if assigned[sid] else " (no shape injected)")
        out.append((sid, desc, _pad(rng, words, None)))
    return out


# ------------------------------------------------------------------ runs

LETTER_RUNS = (16, 17, 36, 37, 255, 256, 257, 4096, 16384)
DIGIT_RUNS = (16, 17, 27, 28, 256)


def nonperiodic(rng, draw, *derived):
    """Draw with `draw(rng)` until the result AND every `d(result)` in
    `derived` read `no` in the `periodic` column. The column's definition
    (pcrecbench.periodic) calls a string whose last byte equals its first
    "periodic at n-1", and a 3-byte `202` periodic at 2; a subject built to
    be non-periodic is drawn until it is, rather than the manifest admitting
    a trivial period on one subject in ten."""
    for _ in range(1000):
        v = draw(rng)
        if all(bt.periodic_field(x.encode("latin-1")) == "no"
               for x in [v] + [d(v) for d in derived]):
            return v
    raise AssertionError("no non-periodic draw in 1000 attempts")


def runs(rng):
    out = []
    for n in LETTER_RUNS:
        out.append(("r-%05d" % n, "run/letters: %d random lowercase letters" % n,
                    nonperiodic(rng, lambda r: r.letters(n))))
    for n in DIGIT_RUNS:
        out.append(("d-%05d" % n, "run/digits: %d random digits" % n,
                    nonperiodic(rng, lambda r: r.digits(n))))
    return out


def build():
    rng = bt.Rng(SEED)
    return fields(rng) + lines(rng) + runs(rng)


def main():
    subjects = build()
    os.makedirs(OUT, exist_ok=True)
    rows = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, desc, text in subjects:
        b = text.encode("latin-1")
        assert b"\n" not in b and b"\t" not in b, sid
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(b)
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(b), hashlib.sha256(b).hexdigest(), desc, bt.periodic_field(b)))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(rows) + "\n")
    sizes = [len(t) for _s, _d, t in subjects]
    print("gen_subjects: %d subjects (%d B, %d..%d) -> %s, manifest -> %s"
          % (len(subjects), sum(sizes), min(sizes), max(sizes), OUT, MANIFEST))


if __name__ == "__main__":
    main()
