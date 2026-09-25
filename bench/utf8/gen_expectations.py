#!/usr/bin/env python3
"""gen_expectations.py -- `expectations.tsv` for bench/utf8@0.1 -- **A U4
STUB, NOT THE REAL DERIVATION** ([B77] U4's own brief: "Expectations
(expectations.tsv) and NOTES.md are U5, not yours, unless the generic
gates require a stub. If they do, say so and make the smallest possible
stub."). They do: the moment `subbench.toml` exists, `bench/utf8` is
ENUMERATED by `tools/selfcheck.py`'s `subbench_dirs()` and TWO generic
`make check-harness` gates unconditionally call this file --
`check_expectations()` (`gen_expectations.py --check` must exit 0) and
`check_floor_pattern()` (a real `pcrecbench quick --testee pcre2-jit
--regime search --pattern floor` cell, which reads `sb.expectation(...)`
for the floor pattern against WHICHEVER 5 `search_short` subjects `quick`
picks -- `pcrecbench/subbench.py`'s `Subbench.expectation()` raises if no
row exists for the (pattern, subject, regime) triple it is asked about).

**What this stub derives, and what it does not.** It calls the SAME
shared oracle derivation every other set uses
(`pcrecbench.expectations.derive`), REAL and libpcre2-differential, never
faked -- but restricted to the ONE pattern `check_floor_pattern` actually
needs: the floor (`~`), over EVERY subject in EVERY regime this set
declares (so it covers whichever short subjects `quick --subjects N`
picks, not just a named few). The floor is byte-safe by design
(utf8_set_v1.md 4.4) and pure ASCII, so this is fast (well under a
second) regardless of the set's own ~30x-slower UTF-8 oracle cost
(docs/dev/lanes/b77u4_report.md's own timed estimate for the REAL,
76-pattern derivation U5 owes).

**The 75 non-floor patterns carry NO expectation rows here.** A `quick`/
`run` cell against any of them will raise (no expectation for that
pattern) until U5 lands the real derivation -- this is the honest
consequence of a stub, not a hidden gap: `bench/utf8/CLAUDE.md` and this
lane's report both say so in writing, and `check_expectations()`/
`check_floor_pattern()` are the only two generic gates that touch
`expectations.tsv` at all (confirmed by reading both in
`tools/selfcheck.py`; no other generic check queries a non-floor
pattern's expectation).

    python3 bench/utf8/gen_expectations.py            # write (floor only)
    python3 bench/utf8/gen_expectations.py --check     # re-derive + diff
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench.expectations import HEADER, derive  # noqa: E402
from pcrecbench.subbench import load as load_subbench  # noqa: E402

OUT = os.path.join(HERE, "expectations.tsv")


def _floor_only_derive():
    sb = load_subbench(HERE)
    floors = [p for p in sb.patterns if p.role == "floor"]
    assert len(floors) == 1, (
        "bench/utf8: expected exactly one floor-role pattern, found %d"
        % len(floors))
    sb.patterns = floors  # a plain list attribute (subbench.py); safe to
    # narrow here since this process derives nothing else from `sb`.
    rows, giveups, version = derive(sb, report=False)
    for p, s, r, msg in giveups:
        print("ORACLE GAVE UP, triple DROPPED: %s / %s / %s: %s"
              % (p, s, r, msg), file=sys.stderr)
    return HEADER + "\n" + "\n".join("\t".join(row) for row in rows) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    text = _floor_only_derive()

    if args.check:
        if not os.path.exists(OUT):
            print("gen_expectations --check: %s does not exist" % OUT,
                  file=sys.stderr)
            return 1
        with open(OUT, "r", encoding="utf-8") as f:
            have = f.read()
        if have != text:
            print("gen_expectations --check: %s does NOT re-derive "
                  "(STUB: floor pattern only -- see this file's own "
                  "docstring)" % OUT, file=sys.stderr)
            return 1
        print("gen_expectations --check: OK (STUB: floor pattern only, "
              "%d row(s))" % (text.count("\n") - 1))
        return 0

    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("gen_expectations: STUB wrote %d row(s) (floor pattern only) "
          "-> %s -- the other 75 patterns' real UTF-aware oracle "
          "derivation is U5's own scope" % (text.count("\n") - 1, OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
