#!/usr/bin/env python3
"""gen_expectations.py -- derive `expectations.tsv` from the libpcre2 oracle.

Method `libpcre2-differential` (requirements 5): the CANONICAL answers, for
every testee, taken from the installed libpcre2-8 runtime through
`pcrecbench/oracle_pcre2.py`. The oracle VERSION is read live off the loaded
library and written into every row -- an expectation whose oracle is not named
is not an expectation.

One row per (pattern x subject x regime), for both patterns:

  * `match`        -- all 85 short subjects, PCRE2_ANCHORED|PCRE2_ENDANCHORED
                      at offset 0 (harness contract 2: whole-subject match).
  * `search_short` -- the short subjects of <= 256 bytes, unanchored at
                      offset 0 (contract 2: SEARCH semantics).
  * `throughput`   -- the three 1 MB subjects, unanchored: the FIRST match's
                      span AND the count of NON-OVERLAPPING matches, both
                      recorded, found by the same `pos = max(end, pos+1)`
                      advance rule both drivers use.

WHAT IS NOT RECORDED, and why: capture-level expectations. `orig.rx` has NO
capturing group at all, and `factored.rx`'s four named groups are `{0}`
DEFINITION groups reached only through `(?&name)` calls, whose slots the call
return restores -- so on both patterns the span IS the whole observable
answer. This script CHECKS that rather than asserting it (see `--report`), and
the general capture-correspondence contract stays where requirements 12 put
it: OD-B9, with the first non-PCRE2 adapter.

An oracle GIVE-UP (a match-limit or depth-limit error, never NOMATCH) is not
folded into "no match": the triple is dropped from the file and listed on
stderr, because an expectation derived from a give-up is a wrong answer
recorded as ground truth.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench import oracle_pcre2 as oracle  # noqa: E402
from pcrecbench.subbench import load as load_subbench  # noqa: E402

HEADER = ("pattern\tsubject\tregime\texpected\tstart\tend\tnmatches"
          "\tmethod\toracle")
METHOD = "libpcre2-differential"
SHORT_SEARCH_MAX = 256


def derive(sb, report=False):
    version = oracle.version()
    rows = []
    giveups = []
    ncaps_seen = {}

    for pat in sb.patterns:
        text = sb.pattern_bytes(pat.name)
        rx = oracle.compile(text)
        for regime in ("match", "search_short", "throughput"):
            if regime not in sb.regimes:
                continue
            for subj in sb.subjects_for(regime):
                body = sb.subject_bytes(subj.subject_id)
                try:
                    if regime == "match":
                        got = rx.match(body, 0)
                        span, groups = (got if got else (None, ()))
                        n = "-"
                    elif regime == "search_short":
                        got = rx.search(body, 0)
                        span, groups = (got if got else (None, ()))
                        n = "-"
                    else:
                        span, count = rx.find_all(body)
                        groups = ()
                        n = str(count)
                except oracle.Pcre2Error as e:
                    giveups.append((pat.name, subj.subject_id, regime, str(e)))
                    continue
                if groups:
                    ncaps_seen.setdefault(pat.name, set()).update(
                        i for i, g in enumerate(groups, 1) if g is not None)
                if span is None:
                    rows.append((pat.name, subj.subject_id, regime,
                                 "nomatch", "-", "-", n, METHOD, version))
                else:
                    rows.append((pat.name, subj.subject_id, regime,
                                 "match", str(span[0]), str(span[1]), n,
                                 METHOD, version))
    if report:
        for name in sorted(ncaps_seen):
            print("NOTE: pattern %r had participating capture groups %s in at "
                  "least one subject -- the 'span is the whole answer' claim "
                  "in this script's header needs revisiting."
                  % (name, sorted(ncaps_seen[name])), file=sys.stderr)
        if not ncaps_seen:
            print("checked: no capturing group participated in any match, on "
                  "either pattern, over every subject and regime -- the span "
                  "is the whole observable answer for this sub-bench.",
                  file=sys.stderr)
    return rows, giveups, version


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=os.path.join(HERE, "expectations.tsv"))
    ap.add_argument("--check", action="store_true",
                    help="re-derive and DIFF against the committed file "
                         "instead of writing it (the `make check` mode)")
    ap.add_argument("--report", action="store_true", default=True)
    args = ap.parse_args(argv)

    sb = load_subbench(HERE)
    rows, giveups, version = derive(sb, report=args.report)

    for p, s, r, msg in giveups:
        print("ORACLE GAVE UP, triple DROPPED: %s / %s / %s: %s"
              % (p, s, r, msg), file=sys.stderr)

    text = HEADER + "\n" + "\n".join("\t".join(r) for r in rows) + "\n"

    if args.check:
        if not os.path.exists(args.out):
            print("gen_expectations --check: %s does not exist" % args.out,
                  file=sys.stderr)
            return 1
        with open(args.out, "r", encoding="utf-8") as f:
            have = f.read()
        if have != text:
            print("gen_expectations --check: %s does NOT re-derive from the "
                  "oracle (libpcre2 %s)" % (args.out, version), file=sys.stderr)
            hl, tl = have.splitlines(), text.splitlines()
            for i in range(max(len(hl), len(tl))):
                a = hl[i] if i < len(hl) else "<absent>"
                b = tl[i] if i < len(tl) else "<absent>"
                if a != b:
                    print("  line %d committed: %s" % (i + 1, a), file=sys.stderr)
                    print("  line %d derived  : %s" % (i + 1, b), file=sys.stderr)
                    break
            return 1
        print("gen_expectations --check: %d expectation(s) re-derive from "
              "libpcre2 %s" % (len(rows), version))
        return 0

    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("gen_expectations: %d expectation(s) from libpcre2 %s -> %s"
          % (len(rows), version, args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
