#!/usr/bin/env python3
"""gen_pattern_facts.py -- `pattern_facts.tsv`: per pattern, what PCRE2's own
analysis says about it, the bounded-repeat facts a reader of the compile
axis wants (the largest count, the nesting depth, the count product through
the nest), and how the pattern lands on THESE subjects (m/n per regime).

WHY THIS FILE EXISTS. This sub-bench's compile axis is "artifact size and
compile time against the COUNT" (plan [B11.4] (1)), so a reader of a compile
row needs the count beside the number, and the nesting depth, and the product
of the maxima through the nest -- the quantity a body-replicating compiler's
size follows. Those are facts about the pattern TEXT; the match-side facts
(first/required code unit, minimum length) are PCRE2's; the m/n is the
oracle's. All three kinds are derived here, committed, and re-derived by
`make check` (`--check`), never typed into NOTES.md where they would go stale
the day a rung is edited.

    python3 bench/bounded/gen_pattern_facts.py           # write
    python3 bench/bounded/gen_pattern_facts.py --check    # re-derive + diff

COLUMNS
  pattern            the sub-bench pattern name
  bytes              the pattern text's length (what `size_class` bands)
  max_count          the largest finite count in any `{n}`/`{n,m}`/`{n,}` --
                     the ladder's rung; `open` is noted in `count_product`
  nest_depth         how many counted repeats enclose the innermost counted
                     repeat, plus one: `[a-z]{0,n}` is 1, `(?:\\d{1,k}){1,k}`
                     is 2, `(?:(?:\\d{1,k}){1,k}){1,k}` is 3
  count_product      the product of the maxima along the deepest counted
                     nest -- the most repetitions of the innermost body a
                     whole match can contain; `open` when a `{n,}` is on the
                     path (no maximum)
  lazy               `yes` if any counted repeat is lazy (`?`-suffixed)
  first_code_unit    PCRE2's first-code-unit analysis: the byte, `bitmap-or-
                     none`, or `type-N`
  required_code_unit the byte every match must contain, or `NONE`
  min_length         PCRE2's minimum match length, in bytes
  match_m_n          how many of the match-regime subjects MATCH whole
  search_m_n         how many of the search-band subjects contain a match
  oracle             the libpcre2 version the PCRE2 facts were read from

The text facts come from a small scanner over the pattern bytes that
understands `(?:`, `(`, `)`, escapes, classes and `{...}` quantifiers -- and
nothing else, because nothing else occurs in this set; it refuses anything
it does not understand rather than guessing.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench import oracle_pcre2 as oracle          # noqa: E402
from pcrecbench.subbench import load as load_subbench  # noqa: E402

HEADER = ("pattern\tbytes\tmax_count\tnest_depth\tcount_product\tlazy"
          "\tfirst_code_unit\trequired_code_unit\tmin_length"
          "\tmatch_m_n\tsearch_m_n\toracle")
OUT = os.path.join(HERE, "pattern_facts.tsv")

_QUANT = re.compile(rb"\{(\d+)(?:(,)(\d*))?\}(\?)?")


def count_facts(text):
    """(max_count, nest_depth, count_product, lazy) from the pattern bytes.

    Walks the text tracking group depth. A quantifier applies to the atom
    that precedes it; when that atom is a group `(...)` the quantifier
    encloses every counted repeat inside the group. `stack` holds, per open
    group, the deepest (depth, product) seen inside it so far, so a
    quantifier on the group's `)` can extend the nest by one level."""
    max_count = 0
    lazy = False
    # (depth, product) of the deepest counted nest closed so far at each
    # group level; level 0 is the top.
    best = [(0, 1)]
    i = 0
    n = len(text)
    last_group_best = None       # the (depth, product) inside the group just closed
    while i < n:
        c = text[i:i + 1]
        if c == b"\\":
            i += 2
            last_group_best = None
            continue
        if c == b"[":
            j = text.index(b"]", i + 2 if text[i + 1:i + 2] == b"^" else i + 1)
            i = j + 1
            last_group_best = None
            continue
        if c == b"(":
            best.append((0, 1))
            i += 3 if text[i:i + 3] == b"(?:" else 1
            last_group_best = None
            continue
        if c == b")":
            last_group_best = best.pop()
            i += 1
            continue
        m = _QUANT.match(text, i)
        if m:
            lo = int(m.group(1))
            hi = (lo if m.group(2) is None
                  else (int(m.group(3)) if m.group(3) else None))
            lazy = lazy or bool(m.group(4))
            for v in (lo, hi):
                if v is not None:
                    max_count = max(max_count, v)
            inner = last_group_best or (0, 1)
            depth = inner[0] + 1
            prod = (None if hi is None or inner[1] is None
                    else hi * inner[1])
            cur = best[-1]
            if depth > cur[0] or (depth == cur[0] and (prod is None or
                                                       (cur[1] is not None and prod > cur[1]))):
                best[-1] = (depth, prod)
            i = m.end()
            last_group_best = None
            continue
        if c in b"{}":
            raise ValueError("unexpected %r at %d in %r" % (c, i, text))
        i += 1
        last_group_best = None
    depth, prod = best[0]
    return max_count, depth, ("open" if prod is None else str(prod)), lazy


def show_byte(v):
    if v is None:
        return "NONE"
    c = chr(v)
    return c if 33 <= v <= 126 else "\\x%02x" % v


def show_first(info):
    if info["first_code_type"] == 1:
        return show_byte(info["first_code_unit"])
    if info["first_code_type"] == 0:
        return "bitmap-or-none"
    return "type-%d" % info["first_code_type"]


def derive(sb):
    version = oracle.version()
    rows = []
    for pat in sb.patterns:
        text = sb.pattern_bytes(pat.name)
        rx = oracle.compile(text)
        info = rx.pattern_info()
        max_count, depth, prod, lazy = count_facts(text)
        mn = {}
        for regime in ("match", "search_short"):
            matched = total = 0
            for subj in sb.subjects_for(regime):
                total += 1
                exp = sb.expectation(pat.name, subj.subject_id, regime)
                if exp is not None and exp.matched:
                    matched += 1
            mn[regime] = "%d/%d" % (matched, total)
        rows.append((pat.name, str(len(text)), str(max_count), str(depth), prod,
                     "yes" if lazy else "no", show_first(info),
                     show_byte(info["required_code_unit"]),
                     str(info["min_length"]), mn["match"], mn["search_short"],
                     version))
    return rows, version


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--check", action="store_true",
                    help="re-derive and DIFF against the committed file "
                         "instead of writing it (the `make check` mode)")
    args = ap.parse_args(argv)

    sb = load_subbench(HERE)
    rows, version = derive(sb)
    text = HEADER + "\n" + "\n".join("\t".join(r) for r in rows) + "\n"

    if args.check:
        if not os.path.exists(args.out):
            print("gen_pattern_facts --check: %s does not exist" % args.out,
                  file=sys.stderr)
            return 1
        with open(args.out, "r", encoding="utf-8") as f:
            have = f.read()
        if have != text:
            print("gen_pattern_facts --check: %s does NOT re-derive from "
                  "libpcre2 %s" % (args.out, version), file=sys.stderr)
            hl, tl = have.splitlines(), text.splitlines()
            for i in range(max(len(hl), len(tl))):
                a = hl[i] if i < len(hl) else "<absent>"
                b = tl[i] if i < len(tl) else "<absent>"
                if a != b:
                    print("  line %d committed: %s" % (i + 1, a), file=sys.stderr)
                    print("  line %d derived  : %s" % (i + 1, b), file=sys.stderr)
                    break
            return 1
        print("gen_pattern_facts --check: %d pattern fact row(s) re-derive "
              "from libpcre2 %s" % (len(rows), version))
        return 0

    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("gen_pattern_facts: %d row(s) from libpcre2 %s -> %s"
          % (len(rows), version, args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
