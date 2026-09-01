#!/usr/bin/env python3
"""gen_expectations.py -- `expectations.tsv` for the wide-alternation
sub-bench, from the libpcre2 oracle (method `libpcre2-differential`,
requirements 5).

The derivation itself is `pcrecbench/expectations.py` -- the sub-bench
contract's chain, shared, not copied (see that module's header). This script
is the entry point and the place the sub-bench's own directory is named.

20 patterns x (38 match + 38 search_short + 4 throughput) subject slots.

Run it under `gnutimeout`. Nothing here is a backtracking hazard in the
`bench/bounded` sense -- the branches are literals and the pools are
substring-free, so no subject decomposes many ways -- but the widest rungs
enter thousands of branches per candidate start, and the throughput
subjects are 128 KB and 512 KB, so the whole derivation is minutes rather
than the sub-second every other set here takes. That cost is the
measurement's own subject matter (NOTES.md, "Cell-time estimate"), not a
symptom.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench.expectations import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main(HERE, doc=__doc__.splitlines()[0]))
