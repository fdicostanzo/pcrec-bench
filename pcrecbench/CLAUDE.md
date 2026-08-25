# pcrecbench/ -- the python package

STATUS (this worktree, lane/b5report): only `report.py` and its package
scaffolding exist here. `harness.py`, `quiet.py`, `subbench.py`,
`adapters.py`, `store.py` (docs/design/harness_contract.md 1) belong to
the parallel `b3harness` lane and land at merge time; `__main__.py` here
is a MINIMAL placeholder that dispatches only `report` -- see its own
docstring for the merge note.

## Files (this lane's scope)

- `report.py` -- the reporter ([B5]): loads the record store (via
  `store/index.tsv`, falling back to walking `store/records/` when the
  index is absent), validates every candidate record with the SHARED
  validator (`schema/validate.py` -- requirements.md 6: "a tiny
  validator the reporter shares"), applies filters over setup-layer
  fields (`--subbench`, `--version`, `--regime`, `--machine`,
  `--since`/`--until`, `--where a.b=v`), reduces raw trials per
  (pattern, subject, regime, testee) cell to comparables (median / min /
  max / stddev / n / iters, over `elapsed_ns / iterations` -- see the
  module docstring for why per-call time and not raw elapsed_ns), ranks
  testees per (pattern, subject, regime) excluding expectation-failing
  cells, reduces compile cost per execution-model class (never pooling
  classes; the `lazy-jit` class is DERIVED via
  trial-1-minus-steady-state from timed match rows, since its compile
  row carries no number by schema design), and renders a
  self-describing report in markdown (default) or TSV. It never runs an
  engine.
  Every non-obvious design call this module makes beyond what
  requirements.md/harness_contract.md pin down explicitly (the ns/call
  comparable, the ranking grain, the `--include-synthetic` addition, the
  mixed-version-refusal ordering relative to per-record invalidity) is
  stated in `report.py`'s own module docstring -- read that before
  changing the reduction or filtering logic.
- `__init__.py` -- package docstring only; states the scope split with
  `b3harness`.
- `__main__.py` -- CLI dispatch. Only `report` exists here
  (`python3 -m pcrecbench report ...`); merges with b3harness's fuller
  dispatcher at integration time.
- `tests/` -- see its own CLAUDE.md.

## Running the reporter

    python3 -m pcrecbench report --store pcrecbench/tests/fixtures/store \
        --include-synthetic
    python3 -m pcrecbench report --store store --subbench email-specimen \
        --regime match-compliance --format tsv

`--include-synthetic` is required against ANY store made only of
synthetic records (every fixture here, and schema/examples/) -- the
reporter excludes `synthetic: true` records by default
(schema/examples/CLAUDE.md's stated rule) since a real query must never
silently include invented data.

## Maintenance

Update this file when files are added/removed or change role. `make
check-report` (root Makefile) is this lane's self-check; see
`tests/CLAUDE.md` for what it runs.
