#!/usr/bin/env python3
"""gen_pattern_facts.py -- `pattern_facts.tsv`: the STRUCTURE of each
alternation, read off its committed text, beside what PCRE2's own
start-of-match analysis makes of it and how it lands on THESE subjects.

WHY THIS FILE EXISTS. This sub-bench's whole subject is what a start-of-match
optimization and a compile-size term can SEE in an alternation, so a reader
of any row needs the four structural facts beside the number: how many
branches, how their first bytes are distributed, how long a run of adjacent
branches shares one first byte (the quantity a prefix-factoring pass works
on, and the ONLY thing `srt-512` changes about `w-512`), and how many
distinct prefixes the branch set has (the node count of its forward trie --
the natural size proxy for any engine that builds one). Those are facts about
the pattern TEXT. The match-side facts -- first code unit, required code
unit, minimum length -- are PCRE2's. The m/n is the oracle's. All three kinds
are derived here, committed, and re-derived by `make check` (`--check`),
never typed into NOTES.md where they would go stale the day a rung is edited.

    python3 bench/altwide/gen_pattern_facts.py           # write
    python3 bench/altwide/gen_pattern_facts.py --check    # re-derive + diff

COLUMNS
  pattern            the sub-bench pattern name
  bytes              the pattern text's length (what `size_class` bands)
  branches           how many alternation branches the text carries
  branch_bytes       shortest-longest branch, in bytes
  distinct_first     how many DISTINCT bytes begin a branch (1 for the
                     shared-first-byte arm, 4 for `nar4-*`, 26 for the
                     spread ladder) -- the population of a start bitmap
  max_first_run      the longest run of ADJACENT branches sharing a first
                     byte: 512 when every branch shares one, about 30 in
                     `srt-512`, 2-3 in the ladder's generation order. The
                     order arm's whole content is this column
  shared_prefix      how many leading bytes EVERY branch shares
  shared_suffix      how many trailing bytes every branch shares
  trie_nodes         distinct non-empty prefixes over the branch set -- the
                     forward trie's node count, a text-derived size proxy
                     and NOT a claim about any engine's state count
  first_code_unit    PCRE2's first-code-unit analysis: the byte, or
                     `bitmap-or-none`
  required_code_unit the byte every match must contain, or `NONE` -- the
                     control column: `NONE` means no required-byte precheck
                     can help this pattern at all
  min_length         PCRE2's minimum match length, in bytes
  match_m_n          how many of the match-regime subjects MATCH whole
  search_m_n         how many of the search-band subjects contain a match
  tput_m_n           how many of the throughput subjects contain a match
                     (the count of matches per subject is in expectations.tsv)
  oracle             the libpcre2 version the PCRE2 facts were read from

THE BRANCH LIST IS PARSED FROM THE COMMITTED `.rx` BYTES, not taken from
`gen_patterns.py`'s table. The two are checked against each other already
(`gen_patterns.py --check`), and reading the text here means a drift between
the table and the files shows up twice rather than being invisible to the
half that trusts the other. The parser understands exactly what this set
spells -- an optional `(?i)`, an optional `\\b` pair, a `(?:...)` group, an
optional `{1,3}`, and `|`-separated pure-letter branches -- and REFUSES
anything else rather than guessing.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench import oracle_pcre2 as oracle          # noqa: E402
from pcrecbench.subbench import load as load_subbench  # noqa: E402

HEADER = ("pattern\tbytes\tbranches\tbranch_bytes\tdistinct_first"
          "\tmax_first_run\tshared_prefix\tshared_suffix\ttrie_nodes"
          "\tfirst_code_unit\trequired_code_unit\tmin_length"
          "\tmatch_m_n\tsearch_m_n\ttput_m_n\toracle")
OUT = os.path.join(HERE, "pattern_facts.tsv")


def branches_of(text):
    """The branch literals of one pattern, from its raw bytes.

    Refuses anything outside this set's own vocabulary, so a pattern that
    grew a construct nobody updated this parser for fails loudly instead of
    being described wrongly."""
    s = text.decode("latin-1")
    if s.startswith("(?i)"):
        s = s[4:]
    if s.endswith("{1,3}"):
        s = s[:-5]
    if s.startswith("\\b") and s.endswith("\\b"):
        s = s[2:-2]
    if not s.startswith("(?:") or not s.endswith(")"):
        # the floor pattern: a single literal byte, one "branch"
        if len(s) == 1 and s.isprintable():
            return [s]
        raise ValueError("unparsed pattern: %r" % s[:40])
    body = s[3:-1]
    parts = body.split("|")
    for p in parts:
        if not p or not all(c in "abcdefghijklmnopqrstuvwxyz" for c in p):
            raise ValueError("unparsed branch %r" % p[:40])
    return parts


def common_affix(words, reverse=False):
    seq = [w[::-1] for w in words] if reverse else list(words)
    n = min(len(w) for w in seq)
    for i in range(n):
        c = seq[0][i]
        if any(w[i] != c for w in seq):
            return i
    return n


def max_first_run(words):
    best = cur = 1
    for i in range(1, len(words)):
        cur = cur + 1 if words[i][0] == words[i - 1][0] else 1
        best = max(best, cur)
    return best


def trie_nodes(words):
    """Distinct non-empty prefixes over the branch set."""
    seen = set()
    for w in words:
        for k in range(1, len(w) + 1):
            seen.add(w[:k])
    return len(seen)


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
        info = oracle.compile(text).pattern_info()
        br = branches_of(text)
        mn = {}
        for regime in ("match", "search_short", "throughput"):
            matched = total = 0
            for subj in sb.subjects_for(regime):
                total += 1
                exp = sb.expectation(pat.name, subj.subject_id, regime)
                if exp is not None and exp.matched:
                    matched += 1
            mn[regime] = "%d/%d" % (matched, total)
        rows.append((
            pat.name, str(len(text)), str(len(br)),
            "%d-%d" % (min(map(len, br)), max(map(len, br))),
            str(len(set(w[0] for w in br))), str(max_first_run(br)),
            str(common_affix(br)), str(common_affix(br, reverse=True)),
            str(trie_nodes(br)), show_first(info),
            show_byte(info["required_code_unit"]), str(info["min_length"]),
            mn["match"], mn["search_short"], mn["throughput"], version))
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
