# scripts/tests/ — self-tests for the operational scripts

- `wtprune.test` — `scripts/wtprune`'s self-test (`make check-wtprune`, part of
  `make check`). It builds a sacrificial repo under mktemp, never the real
  tree. Copied from pcrec `scripts/tests/wtprune.test` at 5426f83bf; the 26
  upstream gate checks are unchanged, and 7 lane-scratch checks are appended
  for the pcrec-bench extension. 33 checks, seconds.

- `test_boxq_window.sh` -- `scripts/boxq_window`'s self-test (`make check-boxq-window`,
  part of `make check`): fake state dir / inbox / sleep chains in a mktemp dir,
  41 checks, ~25 s of sleeps, `KEEP=1` keeps the dir.

Maintenance: update this file when a test is added or removed.
