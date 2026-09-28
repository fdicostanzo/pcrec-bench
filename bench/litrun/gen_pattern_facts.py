#!/usr/bin/env python3
"""gen_pattern_facts.py -- `pattern_facts.tsv`: what PCRE2's own start-of-
match analysis says about each pattern, and the m/n it realises on this
set's own subjects.

WHY THIS FILE EXISTS. `first_code_unit` and `required_code_unit` are the
FACTS a required-byte precheck (pcrec's [OPT-REQPOS]/[OPT-REQBYTE]) reads
before it ever sees a subject, and the L-sweep's whole point (S7.2) is
comparing the VM's own literal-run compare against exactly that precheck --
"the default-flags row measures the pre-check, not S2a" is the lane report's
own warning. A reader needs, per pattern: which single byte PCRE2 says every
match must contain (for an exact literal of length L, this is measured to be
the literal's OWN LAST byte, not its first -- an unannounced PCRE2 fact this
column exists to make checkable rather than assumed), and how many of this
set's own subjects contain it. Derived and re-derived by `make check`, never
typed into NOTES.md by hand.

    python3 bench/litrun/gen_pattern_facts.py           # write
    python3 bench/litrun/gen_pattern_facts.py --check    # re-derive + diff

COLUMNS
  pattern             the sub-bench pattern name
  first_code_unit     PCRE2's first-code-unit analysis: the byte (as `x` or
                      `\\xNN`), `bitmap-or-none`, or `type-N`
  required_code_unit  the byte every match must contain, or `NONE`
  min_length          PCRE2's minimum match length, in bytes
  match_mn            of the `match` (short) subjects, how many MATCH, as
                      `m/n`
  search_mn           the same for `search_short`
  tput_mn             the same for `throughput` (the L-sweep's 27 dense
                      subjects, plus the 2x2 set's own null reading there)
  oracle              the libpcre2 version the facts were read from
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench import oracle_pcre2 as oracle          # noqa: E402
from pcrecbench.subbench import load as load_subbench  # noqa: E402

HEADER = ("pattern\tfirst_code_unit\trequired_code_unit\tmin_length"
          "\tmatch_mn\tsearch_mn\ttput_mn\toracle")
OUT = os.path.join(HERE, "pattern_facts.tsv")


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


def mn(sb, pat, regime):
    matched = total = 0
    for subj in sb.subjects_for(regime):
        total += 1
        exp = sb.expectation(pat.name, subj.subject_id, regime)
        if exp is not None and exp.matched:
            matched += 1
    return "%d/%d" % (matched, total)


def derive(sb):
    version = oracle.version()
    rows = []
    for pat in sb.patterns:
        rx = oracle.compile(sb.pattern_bytes(pat.name))
        info = rx.pattern_info()
        req = info["required_code_unit"]
        rows.append((pat.name, show_first(info), show_byte(req),
                     str(info["min_length"]),
                     mn(sb, pat, "match"), mn(sb, pat, "search_short"),
                     mn(sb, pat, "throughput"), version))
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
