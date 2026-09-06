#!/usr/bin/env python3
"""gen_pattern_facts.py -- `pattern_facts.tsv`: one row per pattern with the
FACTS a reader of the census's first sample needs beside a number, derived
and re-derived rather than typed.

    python3 bench/syntax/gen_pattern_facts.py           # write
    python3 bench/syntax/gen_pattern_facts.py --check    # re-derive + diff

WHY. An outlier in the census is read per construct FAMILY and per
mechanism: "what does PCRE2 itself know about this pattern's start" (a
first code unit, a required code unit, a minimum length -- the three
things a start-of-match optimisation lives on), "does it capture, does it
refer back, can it match empty, how far does it look behind" (the four
things that decide whether a pattern is regular at all, and so which route
an AOT compiler can take), and "how many subjects does it hit under each
regime" (the m/n every per-call number is read against). All of it comes
from libpcre2's own `pcre2_pattern_info` and from `expectations.tsv`.

COLUMNS
  pattern            the sub-bench pattern name
  family             the mechanism family (gen_patterns.py's FAMILIES)
  constructs         the seed rows the pattern exercises, space-joined, or
                     `base-grammar`
  seed_module        the seed's `module` column for those rows (the seed's
                     OWN value at its pin, labelled as such; `-` for a base
                     row), so a reader can bucket refusals by module
  bytes              the pattern text's length
  captures           PCRE2_INFO_CAPTURECOUNT
  backref_max        PCRE2_INFO_BACKREFMAX (0 = no backreference)
  match_empty        PCRE2_INFO_MATCHEMPTY (1 = the pattern can match the
                     empty string)
  max_lookbehind     PCRE2_INFO_MAXLOOKBEHIND, in code units
  first_code_unit    PCRE2's first-code-unit analysis: the byte, or
                     `bitmap-or-none`
  required_code_unit the byte every match must contain, or `NONE`
  min_length         PCRE2's minimum match length
  match_m_n          how many of the match-regime subjects MATCH whole
  search_m_n         how many of the search-band subjects contain a match
  tput_m_n           how many of the throughput subjects contain a match
                     (the count of matches per subject is in
                     expectations.tsv)
  oracle             the libpcre2 version the facts were read from

THE FOUR EXTRA PCRE2_INFO_* CODES are [measured] the way `oracle_pcre2.py`
measured its five: the -dev header is not installed on this box, so each
code is verified ON EVERY RUN against a pattern whose answer is known by
construction (`_verify_info_codes`), and a wrong code cannot pass silently.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench import oracle_pcre2 as oracle          # noqa: E402
from pcrecbench.subbench import load as load_subbench  # noqa: E402
import gen_patterns as gp                              # noqa: E402

HEADER = ("pattern\tfamily\tconstructs\tseed_module\tbytes\tcaptures"
          "\tbackref_max\tmatch_empty\tmax_lookbehind\tfirst_code_unit"
          "\trequired_code_unit\tmin_length\tmatch_m_n\tsearch_m_n\ttput_m_n"
          "\toracle")
OUT = os.path.join(HERE, "pattern_facts.tsv")

# [measured] pcre2.h's PCRE2_INFO_* enum, in declaration order:
# ALLOPTIONS 0, ARGOPTIONS 1, BACKREFMAX 2, BSR 3, CAPTURECOUNT 4,
# FIRSTCODEUNIT 5 ... MATCHEMPTY 13, MATCHLIMIT 14, MAXLOOKBEHIND 15,
# MINLENGTH 16. The five the oracle module uses are its own [measured]
# constants; these four are verified below on every run.
PCRE2_INFO_BACKREFMAX = 2
PCRE2_INFO_CAPTURECOUNT = 4
PCRE2_INFO_MATCHEMPTY = 13
PCRE2_INFO_MAXLOOKBEHIND = 15


def _info(rx, code):
    return oracle._info_u32(rx, code)


def _verify_info_codes():
    """Each code against a pattern whose answer is known by construction --
    two patterns per code, so a code that happened to name another field
    with the same value on one pattern cannot pass on both."""
    checks = (
        (PCRE2_INFO_CAPTURECOUNT, r"(a)(b)", 2), (PCRE2_INFO_CAPTURECOUNT, r"ab", 0),
        (PCRE2_INFO_BACKREFMAX, r"(a)(b)\2", 2), (PCRE2_INFO_BACKREFMAX, r"(a)(b)", 0),
        (PCRE2_INFO_MATCHEMPTY, r"a*", 1), (PCRE2_INFO_MATCHEMPTY, r"a+", 0),
        (PCRE2_INFO_MAXLOOKBEHIND, r"(?<=abc)d", 3), (PCRE2_INFO_MAXLOOKBEHIND, r"abcd", 0),
    )
    for code, pat, want in checks:
        got = _info(oracle.compile(pat), code)
        if got != want:
            raise SystemExit("PCRE2_INFO code %d on %r: got %d, want %d -- the "
                             "[measured] enum values do not hold on this "
                             "libpcre2 %s" % (code, pat, got, want, oracle.version()))


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


def seed_modules(seed_path):
    _cols, rows = gp.read_seed(seed_path)
    return {r["syntax"]: (r.get("module") or "-") for r in rows}


def derive(sb, seed_path):
    _verify_info_codes()
    version = oracle.version()
    modules = seed_modules(seed_path)
    table = {p[0]: p for p in gp.PATTERNS}
    rows = []
    for pat in sb.patterns:
        pid, fam, cs, _text, _note = table[pat.name]
        text = sb.pattern_bytes(pat.name)
        rx = oracle.compile(text)
        info = rx.pattern_info()
        mods = sorted({modules.get(c, "?") for c in cs}) if cs else ["-"]
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
            pid, fam, " ".join(cs) if cs else "base-grammar", "+".join(mods),
            str(len(text)),
            str(_info(rx, PCRE2_INFO_CAPTURECOUNT)),
            str(_info(rx, PCRE2_INFO_BACKREFMAX)),
            str(_info(rx, PCRE2_INFO_MATCHEMPTY)),
            str(_info(rx, PCRE2_INFO_MAXLOOKBEHIND)),
            show_first(info), show_byte(info["required_code_unit"]),
            str(info["min_length"]),
            mn["match"], mn["search_short"], mn["throughput"], version))
    return rows, version


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--seed", default=gp.SEED)
    ap.add_argument("--check", action="store_true",
                    help="re-derive and DIFF against the committed file "
                         "instead of writing it (the `make check` mode)")
    args = ap.parse_args(argv)

    sb = load_subbench(HERE)
    rows, version = derive(sb, args.seed)
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
