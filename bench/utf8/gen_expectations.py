#!/usr/bin/env python3
"""gen_expectations.py -- `expectations.tsv` for bench/utf8@0.1, from the
libpcre2 oracle (method `libpcre2-differential`, requirements 5) -- [B77] U5,
the REAL 76-pattern derivation (U4's floor-only stub is retired).

The derivation itself is `pcrecbench/expectations.py` -- the sub-bench
contract's chain, shared, not copied. This set declares `search_short` +
`throughput` (utf8_set_v1.md 10.1: no `match`) and `[expectations] encoding
= "utf8"`, so every pattern is oracled under PCRE2_UTF, plus PCRE2_UCP on
exactly the patterns declaring `requires-unicode-class-scope`
(`expectations.oracle_option_word`, [B77] U1), with U1's CHARACTER-BOUNDARY
find-all advance on the throughput regime.

THE METHOD, recorded (NOTES.md "The oracle"): libpcre2 10.46 through
`pcrecbench/oracle_pcre2.py`, find-all under utf8_set_v1.md 8.2 AS AMENDED
by the manager's VALIDATE-ONCE ruling (2026-09-25): call 1 of each find-all
loop (offset 0, no PCRE2_NO_UTF_CHECK) lets libpcre2 validate the whole
subject; calls 2..n over that same buffer pass PCRE2_NO_UTF_CHECK at
asserted character boundaries. Without it libpcre2 re-checks from the start
offset to the END on every call, and the derivation is quadratic (~55-60
min; docs/dev/measurements/2026-09-25-b77u5-validate-once-probe.txt). The
always-check path is kept (`find_all(validate_once=False)`) as the control
`tools/selfcheck.py check_utf8_validate_once` compares against.

ONE DECLARED ORACLE REFUSAL: `prp-ingreek` (`\\p{InGreek}`) -- libpcre2
refuses block names at compile time (utf8_set_v1.md 5(f): THE REFUSAL
WITNESS). It carries NO expectation rows, by design; an undeclared refusal,
or this pattern compiling, fails the derivation BY NAME.

    python3 bench/utf8/gen_expectations.py            # write
    python3 bench/utf8/gen_expectations.py --check     # re-derive + diff
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench.expectations import main  # noqa: E402

# utf8_set_v1.md 5(f): the one pattern libpcre2 is DESIGNED to refuse.
EXPECTED_ORACLE_REFUSALS = frozenset({"prp-ingreek"})

if __name__ == "__main__":
    sys.exit(main(HERE, doc=__doc__.splitlines()[0],
                  expected_refusals=EXPECTED_ORACLE_REFUSALS))
