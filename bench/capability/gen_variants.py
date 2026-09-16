#!/usr/bin/env python3
"""gen_variants.py -- `variants.tsv` for the capability set.

capability_set_v1.md 6.4: "Every declared variant is oracled on EVERY
subject the canonical pattern is measured on. A rewrite that changes one
answer fails the build" -- via a committed `variants.tsv` a
`gen_*.py --check` hook re-derives, exactly as `gen_expectations.py`
does for the canonical expectation grid.

**v1's table is EMPTY, and that is the correct, checked answer, not an
omission.** The set's first-sample roster is the six pinned pcre2-*/
pcrec-* configs (docs/design/capability_set_v1.md 11.4); every one of
them runs the CANONICAL PCRE2-compatible spelling of every pattern here
(pcrec is D26's Compatibility Standard to libpcre2) -- no engine in v1
needs a per-testee rewrite (`\\d` -> `[0-9]`, a possessive suffix
dropped, `(?>...)` -> `(?:...)`) at all. The rewrite table
(capability_set_v1.md 6.2) and the hazard rule (6.3) exist for RE2,
Rust `regex`, Vectorscan and TRE, none of which is in v1's roster (see
NOTES.md, "Not built here"). This is CHECKED rather than merely stated:
`--check` re-derives the table from `subbench.toml`'s `[testees.*]`
sections (none declared) and confirms it is still empty, so the day a
future lane adds a variant-needing testee, this generator's own
`--check` starts failing on a real row rather than staying silently
vacuous.
"""
import argparse
import os
import sys
import tomllib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "variants.tsv")
SUBBENCH_TOML = os.path.join(HERE, "subbench.toml")
HEADER = ("pattern\ttestee\tsubject\tregime\tcanonical_expected"
          "\tvariant_expected\tmatch")


def derive():
    """-> list of TSV rows (empty in v1; see module docstring)."""
    with open(SUBBENCH_TOML, "rb") as f:
        cfg = tomllib.load(f)
    testees = cfg.get("testees", {})
    rows = []
    for tid, spec in testees.items():
        if "variant" in spec:
            raise NotImplementedError(
                "testee %r declares a variant -- gen_variants.py's v1 "
                "empty-table assumption no longer holds; build the real "
                "oracle-equivalence derivation (capability_set_v1.md "
                "6.4) before committing" % tid)
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    rows = derive()
    text = HEADER + "\n" + "\n".join(rows) + ("\n" if rows else "")

    if args.check:
        if not os.path.exists(OUT):
            print("gen_variants --check: %s does not exist" % OUT,
                  file=sys.stderr)
            return 1
        with open(OUT, "r", encoding="utf-8") as f:
            have = f.read()
        if have != text:
            print("gen_variants --check: %s does not re-derive (has "
                  "%d row(s), derived %d)"
                  % (OUT, max(0, have.count("\n") - 1), len(rows)),
                  file=sys.stderr)
            return 1
        print("gen_variants --check: %d variant row(s) re-derive "
              "(v1: no testee declares a variant -- see module "
              "docstring)" % len(rows))
        return 0

    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("gen_variants: %d row(s) -> %s" % (len(rows), OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
