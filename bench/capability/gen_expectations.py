#!/usr/bin/env python3
"""gen_expectations.py -- `expectations.tsv` for the capability set, from
the libpcre2 oracle (method `libpcre2-differential`, requirements 5).

The derivation itself is `pcrecbench/expectations.py` -- the sub-bench
contract's chain, shared, not copied (see that module's header). This
set declares `search_short` + `throughput` only (capability_set_v1.md
3.5's `match`-regime exclusion, set-wide); the shared derivation reads
`sb.regimes` and skips `match` on its own.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench.expectations import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main(HERE, doc=__doc__.splitlines()[0]))
