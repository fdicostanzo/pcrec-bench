#!/usr/bin/env python3
"""gen_expectations.py -- `expectations.tsv` for the log-line sub-bench, from
the libpcre2 oracle (method `libpcre2-differential`, requirements 5).

The derivation itself is `pcrecbench/expectations.py` -- the sub-bench
contract's chain, shared, not copied (see that module's header). This script
is the entry point and the place the sub-bench's own directory is named.

    python3 bench/loglines/gen_expectations.py            # write
    python3 bench/loglines/gen_expectations.py --check     # re-derive + diff

1320 rows: 11 patterns x (112 search-band + 8 throughput) subjects. The
`match` regime is NOT declared by this sub-bench (NOTES.md, "Regimes"), so no
row carries it.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench.expectations import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main(HERE, doc=__doc__.splitlines()[0]))
