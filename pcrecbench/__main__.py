"""pcrecbench CLI entry point.

MINIMAL BY DESIGN, per the [B5] lane brief: this worktree does not have the
[B3] harness lane's `run` / `index` / `quiet` subcommands
(docs/design/harness_contract.md 4), so this dispatcher exposes only
`report` (docs/design/harness_contract.md 5). When this lane merges
alongside b3harness, whichever tree already has a fuller
`pcrecbench/__main__.py` should keep its other subcommands and add the
`report` dispatch below to it -- the manager resolves that merge.
"""

from __future__ import annotations

import sys


def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    if not argv or argv[0] != "report":
        print("usage: python3 -m pcrecbench report [options]", file=sys.stderr)
        print("  (this tree only implements the `report` subcommand; "
              "run/index/quiet land with the [B3] harness lane)",
              file=sys.stderr)
        return 2
    from pcrecbench import report
    return report.main(argv[1:])


if __name__ == "__main__":
    sys.exit(main())
