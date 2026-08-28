#!/usr/bin/env python3
"""gen_pattern_facts.py -- `pattern_facts.tsv`: what PCRE2's own start-of-match
analysis says about each pattern, and how that lands on THESE subjects.

WHY THIS FILE EXISTS. This sub-bench's whole purpose (inbox I-7 1, pcrec
[OPT-5]) is the cost of failing over text, and the axis that splits it is
whether the engine can dismiss a subject by looking for a byte that every
match must contain -- PCRE2's `req_cu`, the REQUIRED CODE UNIT. A reader of
the numbers needs, per pattern: is there such a byte, and if so, is it present
in the subject anyway (in which case the precheck buys nothing and the engine
scans)? Both halves are FACTS, derivable from the oracle and the committed
subjects; neither is a judgement. So they are derived, committed, and
re-derived by `make check` -- not written into NOTES.md by hand, where they
would quietly go stale the day a pattern is edited.

    python3 bench/loglines/gen_pattern_facts.py           # write
    python3 bench/loglines/gen_pattern_facts.py --check    # re-derive + diff

COLUMNS
  pattern            the sub-bench pattern name
  first_code_unit    PCRE2's first-code-unit analysis: the byte (as `x` or
                     `\\xNN`), `bitmap` when it has a start bitmap instead of
                     one byte, or `none`
  required_code_unit the byte every match must contain, or `NONE` -- the
                     control column: `NONE` means no required-byte precheck
                     can help this pattern at all
  min_length         PCRE2's minimum match length, in bytes
  search_req_present of the search-band subjects, how many CONTAIN that byte
                     (`-` when there is none): the subjects on which the
                     precheck cannot dismiss and the engine must scan
  search_matches     of the search-band subjects, how many MATCH (the m/n
                     NOTES.md reports), from the same oracle
  tput_req_present   the same presence count over the 12 throughput subjects
  tput_matches       how many of the 12 throughput subjects match
  tput_req_absent    the throughput subjects that do NOT contain the required
                     byte, by id, or `-` -- the rows where a required-byte
                     precheck dismisses a large subject without scanning it,
                     which is the comparison this sub-bench was built for
  oracle             the libpcre2 version the facts were read from

THE ORACLE IS THE SOURCE FOR ALL OF IT, which is deliberate but worth saying
out loud: `required_code_unit` is a claim about what PCRE2 does, so PCRE2 is
the right source. It is NOT evidence about what any other engine's analysis
finds -- pcrec's, in particular, is what the bench is measuring, and a testee
that disagreed with this column would be a finding, not an error here.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench import oracle_pcre2 as oracle          # noqa: E402
from pcrecbench.subbench import load as load_subbench  # noqa: E402

HEADER = ("pattern\tfirst_code_unit\trequired_code_unit\tmin_length"
          "\tsearch_req_present\tsearch_matches\ttput_req_present"
          "\ttput_matches\ttput_req_absent\toracle")
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


def derive(sb):
    version = oracle.version()
    rows = []
    for pat in sb.patterns:
        rx = oracle.compile(sb.pattern_bytes(pat.name))
        info = rx.pattern_info()
        req = info["required_code_unit"]
        counts = {}
        absent_ids = []
        for regime, key in (("search_short", "search"), ("throughput", "tput")):
            present = matched = total = 0
            for subj in sb.subjects_for(regime):
                total += 1
                body = sb.subject_bytes(subj.subject_id)
                if req is not None:
                    if bytes([req]) in body:
                        present += 1
                    elif regime == "throughput":
                        absent_ids.append(subj.subject_id)
                exp = sb.expectation(pat.name, subj.subject_id, regime)
                if exp is not None and exp.matched:
                    matched += 1
            counts[key] = ("%d/%d" % (present, total) if req is not None
                           else "-", "%d/%d" % (matched, total))
        rows.append((pat.name, show_first(info), show_byte(req),
                     str(info["min_length"]),
                     counts["search"][0], counts["search"][1],
                     counts["tput"][0], counts["tput"][1],
                     ",".join(absent_ids) if absent_ids else "-", version))
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
