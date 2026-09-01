#!/usr/bin/env python3
"""gen_oracle_limits.py -- `oracle_limits.tsv`: where the ORACLE itself stops
on each of this sub-bench's count-ladder skeletons, probed BEYOND the rungs
the set carries.

WHY THIS FILE EXISTS. The count ladder's third number (plan [B11.4] (3)) is
"the count at which an engine first refuses". libpcre2 is the oracle every
expectation comes from, so a rung it refuses can carry no expectation and is
not in the set -- yet its refusal is exactly the kind of fact the ladder
exists to locate, and for two skeletons it is the reason the ladder stops
where it does. So the probe is committed as a table: per skeleton, the
rungs tried (doubling from the set's smallest), the LAST the oracle
accepted, the FIRST it refused, and its own diagnostic, verbatim. Compile
only -- nothing is matched -- and re-derived by `make check` (`--check`) so
a new libpcre2 on the box that moves a limit is a visible diff.

    python3 bench/bounded/gen_oracle_limits.py           # write
    python3 bench/bounded/gen_oracle_limits.py --check    # re-derive + diff

TWO KINDS OF CEILING appear, and the diagnostic tells them apart: "number
too big in {} quantifier" is PCRE2's count ceiling (65535 on any count),
which every skeleton hits eventually; "regular expression is too large" is
its COMPILED-SIZE ceiling, which only the skeletons PCRE2 expands per count
reach -- a repeated GROUP is replicated per count, a repeated single unit
is one opcode with a counter -- and it fires far below 65535 on those.

WHAT THIS TABLE IS NOT: evidence about any other engine. pcrec's and
every other testee's refusals are recorded by the harness, per pattern,
as `did-not-compile` rows with the engine's diagnostic (requirements 4.4);
this table is only the oracle's edge of the ladder.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench import oracle_pcre2 as oracle  # noqa: E402

HEADER = ("skeleton\ttemplate\tset_rungs\tprobed\tlast_accepted"
          "\tfirst_refused\tdiagnostic\toracle")
OUT = os.path.join(HERE, "oracle_limits.tsv")

# (skeleton, template with N, the rungs the SET carries, probe start, cap).
# The probe doubles N from `start` until the oracle refuses or `cap` is
# passed; `cap` = 65536 is one past PCRE2's count ceiling so the count
# ceiling itself is always reached and named.
SKELETONS = (
    ("cls-upto",      r"[a-z]{0,N}",                    "4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65535", 16, 65536),
    # 0.3's short-run digit family ([B27]): the same probe on the two
    # skeletons `year4` is the k = 4 rung of, so the oracle's own ceiling on
    # them is on the record beside the class ladder's rather than assumed
    # from it. Both are single-unit repeats, so the COUNT ceiling is the one
    # they should reach -- if either reports a compiled-SIZE refusal instead,
    # PCRE2 is replicating something the set assumes it does not.
    ("dig-exact",     r"\d{N}",                         "2,4,8,16,32",                   2, 65536),
    ("dig-upto",      r"\d{1,N}",                       "2,4,8,16,32",                   2, 65536),
        ("cls-atleast",   r"[a-z]{N,}",                     "4096",                          256, 65536),
    ("cls-lazy",      r"[a-z]{0,N}?",                   "16384",                         256, 65536),
    ("grp-upto",      r"(?:a|[b-z]){0,N}",              "1024",                          16, 65536),
    ("nest2",         r"(?:\d{1,N}){1,N}",              "4,64",                          4, 65536),
    ("nest3",         r"(?:(?:\d{1,N}){1,N}){1,N}",     "3,16",                          3, 65536),
    ("nest2-letters", r"(?:[a-z]{1,N}){1,N}",           "6",                             6, 65536),
    ("ctx-lazy",      r"\b(?:fail|abort|panic)\b.{0,N}?\b(?:disk|memory|socket|quota)\b",
                                                        "64,256,1024",                   64, 65536),
)


def probe(template, start, cap):
    n = start
    last_ok = None
    tried = []
    while True:
        tried.append(n)
        try:
            oracle.compile(template.replace("N", str(n)))
            last_ok = n
        except oracle.Pcre2Error as e:
            msg = str(e)
            # strip the offset: "pcre2_compile failed at offset 13: <text>"
            return tried, last_ok, n, msg.split(": ", 1)[1] if ": " in msg else msg
        if n >= cap:
            return tried, last_ok, None, "-"
        n = min(n * 2, cap) if n * 2 < cap or n == cap else cap
        if n == cap and tried[-1] == cap:
            return tried, last_ok, None, "-"


def derive():
    version = oracle.version()
    rows = []
    for name, template, set_rungs, start, cap in SKELETONS:
        tried, last_ok, refused, diag = probe(template, start, cap)
        rows.append((name, template, set_rungs, ",".join(str(t) for t in tried),
                     str(last_ok), str(refused) if refused else "none-to-%d" % cap,
                     diag, version))
    return rows, version


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--check", action="store_true",
                    help="re-derive and DIFF against the committed file "
                         "instead of writing it (the `make check` mode)")
    args = ap.parse_args(argv)
    rows, version = derive()
    text = HEADER + "\n" + "\n".join("\t".join(r) for r in rows) + "\n"
    if args.check:
        if not os.path.exists(args.out):
            print("gen_oracle_limits --check: %s does not exist" % args.out,
                  file=sys.stderr)
            return 1
        with open(args.out, "r", encoding="utf-8") as f:
            have = f.read()
        if have != text:
            print("gen_oracle_limits --check: %s does NOT re-derive from "
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
        print("gen_oracle_limits --check: %d skeleton row(s) re-derive from "
              "libpcre2 %s" % (len(rows), version))
        return 0
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("gen_oracle_limits: %d row(s) from libpcre2 %s -> %s"
          % (len(rows), version, args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
