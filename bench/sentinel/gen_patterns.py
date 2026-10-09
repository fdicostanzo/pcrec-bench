#!/usr/bin/env python3
"""gen_patterns.py -- the SENTINEL set's patterns: byte-for-byte copies of
`bench/capability/patterns/*.rx` members (the program-identical short-call
movers and controls of [B132]/O-92) plus capability's floor. Nothing is
authored here; a copy that drifts from its source fails `--check`.

    python3 bench/sentinel/gen_patterns.py            # write patterns/*.rx
    python3 bench/sentinel/gen_patterns.py --check    # re-derive + diff
    python3 bench/sentinel/gen_patterns.py --sidecar  # print the [[patterns]] blocks

`--check` also compares subbench.toml's [[patterns]] blocks against the
blocks derived from capability's own sidecar entries.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CAP = os.path.join(os.path.dirname(HERE), "capability")

# The [B132] movers (pcrec-auto / pcrec-nocaps, O-92) first, then its controls.
MEMBERS = (
    "winpath-near-miss", "trim-nested-star", "numeric-id-nested-plus",
    "phone-list-nested-plus", "wild-validator-us-zip-owasp",
    "base10num-near-miss", "ipv4-near-miss", "uuid-near-miss",
    "wild-semdiv-dollar-trailing-newline-pcre2", "router-prefix-order",
    "wild-validator-email-owasp",
    # controls: flat in every [B132] arm (bracket-array-define, the fourth, holds a
    # newline and has no .rxt `pattern` line spelling -- dropped, [B133])
    "wild-waf-crs-942360-concat-sqli", "keyword-prefix-order",
    "file-ext-order",
)
FLOOR = "floor-byte"


def cap_blocks():
    """name -> its [[patterns]] block text in capability's sidecar."""
    text = open(os.path.join(CAP, "subbench.toml"), encoding="utf-8").read()
    out = {}
    for blk in re.split(r"(?m)^(?=\[\[patterns\]\]\n)", text):
        m = re.search(r'(?m)^name = "([^"]+)"', blk) if blk.startswith("[[patterns]]") else None
        if m:
            out[m.group(1)] = blk.rstrip("\n") + "\n"
    return out


def derived_blocks():
    blocks = cap_blocks()
    out = []
    for n in MEMBERS + (FLOOR,):
        b = blocks[n]
        b = re.sub(r'tags = \[', 'tags = ["sentinel", ', b, count=1)
        out.append(b)
    return "\n".join(out)


def main():
    check = "--check" in sys.argv
    if "--sidecar" in sys.argv:
        sys.stdout.write(derived_blocks())
        return 0
    bad = 0
    for n in MEMBERS + (FLOOR,):
        src = open(os.path.join(CAP, "patterns", n + ".rx"), "rb").read()
        dst = os.path.join(HERE, "patterns", n + ".rx")
        if check:
            if not os.path.exists(dst) or open(dst, "rb").read() != src:
                print("DRIFT %s" % n); bad += 1
        else:
            with open(dst, "wb") as f:
                f.write(src)
    if check:
        have = set(os.listdir(os.path.join(HERE, "patterns")))
        extra = have - {n + ".rx" for n in MEMBERS + (FLOOR,)}
        if extra:
            print("EXTRA pattern files: %s" % sorted(extra)); bad += 1
        side = open(os.path.join(HERE, "subbench.toml"), encoding="utf-8").read()
        if derived_blocks() not in side:
            print("DRIFT subbench.toml [[patterns]] blocks vs capability's"); bad += 1
        print("gen_patterns --check: %s" % ("OK" if not bad else "%d problem(s)" % bad))
        return 1 if bad else 0
    print("gen_patterns: %d patterns copied" % (len(MEMBERS) + 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
