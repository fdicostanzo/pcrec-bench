#!/usr/bin/env python3
"""gen_oracle_limits.py -- `oracle_limits.tsv`: the WIDTH at which the ORACLE
itself refuses each of this sub-bench's alternation skeletons, probed BEYOND
the rungs the set carries.

WHY THIS FILE EXISTS. Plan row [B11.2] calls a 4096-way alternation "a
compile-size question", and the third number a width ladder exists to locate
is the width at which an engine first refuses. libpcre2 is the oracle every
expectation comes from, so a rung IT refuses can carry no expectation and
cannot be in the set -- yet that refusal is exactly the kind of fact the
ladder is for, and for this set it is the reason the ladder has the shape it
has: the `main` skeleton stops at 2048 and the `s-*` rungs exist at all
because libpcre2 will not compile 4096 branches of 3-12 byte words. So the
probe is committed as a table: per skeleton, the widths tried (doubling from
the set's smallest rung), the LAST the oracle accepted, the FIRST it refused,
and its own diagnostic, verbatim. Compile only -- nothing is matched -- and
re-derived by `make check` (`--check`), so a new libpcre2 on the box that
moves a limit is a visible diff.

    python3 bench/altwide/gen_oracle_limits.py           # write
    python3 bench/altwide/gen_oracle_limits.py --check    # re-derive + diff

THE CEILING HERE IS A COMPILED-SIZE ONE, and it is worth naming because it
is not the ceiling `bench/bounded` found. That set hit PCRE2's COUNT ceiling
("number too big in {} quantifier", 65535) and, on replicated groups, its
compiled-size ceiling. A wide alternation has no counts at all: it reaches
"regular expression is too large" alone, which in a default 8-bit build is
the LINK_SIZE 2 bound on the compiled pattern -- roughly two code units per
literal byte plus three per branch. That is why branch LENGTH moves the
ceiling as much as branch COUNT does, and why `s-2048` sits beside `w-2048`
as the controlled pair that says by how much.

WHAT THIS TABLE IS NOT: evidence about any other engine. pcrec's and every
other testee's refusals are recorded by the harness, per pattern, as
`did-not-compile` rows with the engine's own diagnostic (requirements 4.4);
this table is only the oracle's edge of the ladder. In particular it says
NOTHING about the pcrec caps NOTES.md predicts against -- one of which
(the DFA state ceiling) this table is the reason the set cannot reach.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

import altwidetext as at                       # noqa: E402
from gen_patterns import wrap                  # noqa: E402
from pcrecbench import oracle_pcre2 as oracle  # noqa: E402

HEADER = ("skeleton\tpool\tbranch_bytes\tset_rungs\tprobed\tlast_accepted"
          "\tfirst_refused\tdiagnostic\toracle")
OUT = os.path.join(HERE, "oracle_limits.tsv")

# One past the widest width any skeleton here is probed at. The probe doubles
# from `start` and stops at the first refusal or when it passes this.
PROBE_CAP = 8192

# (skeleton, pool, wrapper, the rungs the SET carries, probe start).
# `wrapper` is `gen_patterns.py`'s own, applied by the same function, so a
# probe row is the identical construction the set's patterns get.
SKELETONS = (
    ("w",    "main",  None,        "8,64,96,128,192,256,384,512,1024,2048", 8),
    ("s",    "short", None,        "256,512,2048,4096",      8),
    ("sh1",  "sh1",   None,        "64,256,512",             8),
    ("pfx3", "pfx3",  None,        "256,512",                8),
    ("sfx",  "sfx",   None,        "64,256,512",             8),
    ("nar4", "nar4",  None,        "64,256,512",             8),
    ("srt",  "main",  "sorted",    "256,512",                8),
    ("ci",   "main",  "caseless",  "256,512",                8),
    ("cnt",  "main",  "count13",   "64",                     8),
    ("wb",   "main",  "wordbound", "256,512",                8),
)


def probe(pool_name, wrapper, start):
    words = at.probe_pool(pool_name, PROBE_CAP)
    n = start
    last_ok = None
    tried = []
    while True:
        tried.append(n)
        try:
            oracle.compile(wrap(words[:n], wrapper).encode("latin-1"))
            last_ok = n
        except oracle.Pcre2Error as e:
            msg = str(e)
            # strip the offset: "pcre2_compile failed at offset N: <text>"
            return (tried, last_ok, n,
                    msg.split(": ", 1)[1] if ": " in msg else msg)
        if n >= PROBE_CAP:
            return tried, last_ok, None, "-"
        n = min(n * 2, PROBE_CAP)


def derive():
    version = oracle.version()
    rows = []
    for name, pool, wrapper, set_rungs, start in SKELETONS:
        spec = [s for s in at.POOL_SPECS if s[0] == pool][0]
        tried, last_ok, refused, diag = probe(pool, wrapper, start)
        rows.append((name, pool, "%d-%d" % (spec[2], spec[3]), set_rungs,
                     ",".join(str(t) for t in tried), str(last_ok),
                     str(refused) if refused else "none-to-%d" % PROBE_CAP,
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
