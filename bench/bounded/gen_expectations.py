#!/usr/bin/env python3
"""gen_expectations.py -- `expectations.tsv` for the bounded-repeat sub-bench,
from the libpcre2 oracle (method `libpcre2-differential`, requirements 5).

The derivation itself is `pcrecbench/expectations.py` -- the sub-bench
contract's chain, shared, not copied (see that module's header). This script
is the entry point and the place the sub-bench's own directory is named.

    python3 bench/bounded/gen_expectations.py            # write
    python3 bench/bounded/gen_expectations.py --check     # re-derive + diff

29 patterns x (38 match + 38 search_short + 4 throughput) subject slots.
The `throughput` rows are the ladder's large rungs under find-all search,
not a size sweep (NOTES.md, "Regimes").

Run it under `gnutimeout`: the nested rungs are backtracking hazards by
design, and the subjects are sized so the oracle FINISHES every cell
(NOTES.md, "The runs and the oracle"); a give-up printed here is a design
regression, not a number to wait longer for.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench.expectations import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main(HERE, doc=__doc__.splitlines()[0]))
