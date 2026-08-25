# pcrecbench/ — the harness package

`python3 -m pcrecbench run --subbench email --testee pcre2-jit` measures one
CELL and writes one RECORD. The spec is `docs/design/harness_contract.md`;
the record's shape is `docs/design/record_schema.md`.

| file | role |
|---|---|
| `__main__.py` | the CLI: `run` (`--tier pinned\|scratch`), `quick` (the edit-test loop's one-cell surface, [B10]), `index`, `quiet`, `testees`, `report` |
| `harness.py` | contract §4's seven steps; `outcome_for()` is the ONE place an engine's answer becomes a `match_outcome`; `run_cell(tier=, patterns=, subject_limit=, budget=)` is what `quick` parameterises — no second code path |
| `subbench.py` | loads `bench/<name>/`; owns the regime→subject mapping and `subbench.content_hash` |
| `adapters.py` | the `Adapter` interface, discovery, and **the DRIVER PROTOCOL** (in full, at the top of the file) |
| `driverrun.py` | build/run/parse a driver; the resume-after-driver-death rule |
| `record.py` | builds the record dict; every derived id comes FROM `schema/validate.py`'s own functions |
| `reduce.py` | the SET-GRAIN reduction `quick` prints and the reporter ranks (R5, [B10]): `reduce_set_cell`, `reduce_match_cell`, `cells_from_record`, `giveup_code`; pinned by a hand-computed fixture in `tools/selfcheck.py` |
| `store.py` | the store path rule, never-clobber, validate-before-write, the index; the TIERS: `.canonical` marks the canonical store, which refuses a `tier: scratch` record on write and on index; `scratch_store()` is `$PCRECBENCH_SCRATCH_STORE` or `build/scratch-store/` |
| `quiet.py` | the quiet-box instrument and its two thresholds (`docs/design/quiet_baseline.md`) |
| `env.py` | the `environment` block; the machine registry |
| `oracle_pcre2.py` | the libpcre2 ctypes binding, copied from pcrec (see its header) and extended |

## Three rules that are not obvious from the code

**The harness judges; the adapter answers.** An adapter reports what its
engine said. `harness.outcome_for()` decides what that means against the
sub-bench's expectation. An adapter that graded its own correctness would be
marking its own homework, and the outcome enum would stop being comparable
across engines.

**A record that fails validation is never written.** `store.write()` writes
to a temporary name, runs `schema/validate.py --check-filename` there, and
only then moves it into place. A validation failure is a HARNESS BUG, not a
measurement result, and it is reported as one.

**The harness judges by RANGE, not by lists it keeps in step by hand.** A
give-up is a give-up because the code fell inside bounds the ENGINE
reported (pcrec exports `[PCREC_ERR_FLOOR, -2]` from the artifact; pcre2
supplies its measured limit-code set). A code an engine adds later
classifies correctly with nobody editing `harness.py`, and a reserved code
cannot be laundered into `gave-up` by an enumeration that fell behind.

**A pattern has FORMS, and they never share a row.** `Adapter.compile()`
returns a `CompiledPattern`: one `CompileResult` per form. Most engines
have one (`plain`) because they anchor with runtime options; pcrec has no
end-anchored mode, so it compiles `(?:pattern)\z` as a second artifact and
the match regime is measured on that one. Both are timed and both get
compile rows — rule X27 rejects a `whole-subject` match row whose record
does not witness its compile.

**The store claims a name with `O_EXCL`, never `exists()`-then-write.** An
exists-then-write pair is the race the `-<n>` disambiguator exists to
prevent, reintroduced by the way it was checked. Staging is one temp
directory per write, not one shared one — the race control caught that too.

**Two tiers, and the store decides — not the harness.** A `tier: scratch`
record (a `pcrec-local` binary, any `quick` cell; schema v1.2,
record_schema.md §6.8) is refused into the store carrying the
`.canonical` marker, on write and on index. `run_cell` asks the same
question FIRST — before the gate, the registry or a driver — so a
refused run touches nothing; an adapter that is scratch by construction
says so through `Adapter.tier()`. At the scratch tier the quiet GATE is
skipped, never the INSTRUMENT: the box is sampled at both ends and
`status` is what the samples say. A scratch record is a real record
kept out of the rankings by its tier, not a lesser measurement.

**The number `quick` prints is the number the reporter ranks.**
`reduce.py` is the one home of the set-grain arithmetic (median over
trials of the per-trial sum of per-subject ns/call, a set excluded if
any subject fails); `quick` applies it to the record it just wrote, and
`make check-harness` recomputes the printed median from the file.

**Derivations are imported, never reimplemented.** `record.py` loads
`schema/validate.py` as a module and calls its `derive_record_id`,
`derive_testee_id` and `compute_content_hash`. Two implementations of one
derivation is the check-design failure pcrec has paid for repeatedly: the
check and the thing it checks must not share an author's second guess.

## The reporter ([B5], merged 2026-08-25)

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
  `--since`/`--until`, `--where a.b=v`), reduces raw trials to
  comparables (median / min / max / stddev / n / iters, over
  `elapsed_ns / iterations` -- see the module docstring for why per-call
  time and not raw elapsed_ns) at TWO ranking grains
  (`--grain set|subject`, default `set` -- manager change request,
  2026-08-25): `set` sums per-subject ns/call across the whole subject
  set per trial, then reduces over trials, per (pattern, regime); `subject`
  gives the finer (pattern, subject, regime) drill-down tables this
  module started with. Either grain excludes expectation-failing cells
  from ranking (a `set` cell excludes if ANY subject in it fails, naming
  the failing subjects rather than averaging through them) and lists
  them separately. `form` (`plain`/`whole-subject`, schema v1.1) is part
  of every match- and compile-CELL key (so a testee that carries both
  forms in one regime still reduces to two distinguishable numbers), but
  is DELIBERATELY NOT a RANKING-GROUP key (manager fix request,
  2026-08-25, reversing this module's first cut, which split the
  ranking table by form and made the compliance regime -- the whole
  point of which is comparing engines -- compare nobody to anybody):
  `form` records HOW a testee reached a regime (pcrec's own
  `(?:pattern)\z` artifact vs. another testee's runtime
  ANCHORED|ENDANCHORED flags on its ordinary artifact), not WHICH
  question it answered, so testees with different forms for the same
  (pattern, regime) rank TOGETHER in one table, each row carrying its
  own form as a column (shown only when a report actually includes more
  than `plain`). `form` DOES remain a key for compile-cost cells -- a
  whole-subject artifact is a genuinely separate compile, with its own
  cost, size and trials, and pooling those would report one testee's
  compliance timing against a compile cost it did not pay.
  `match_outcome: gave-up` (schema v1.1: the engine's OWN resource
  limit, not a wrong answer) is counted and labelled separately from
  wrong-answer outcomes everywhere outcomes are shown. Reduces compile
  cost per execution-model class (never pooling classes; the `lazy-jit`
  class is DERIVED via `first-match-row-minus-steady-state`, schema
  v1.1's token -- the pattern's globally-first TIMED match row by
  `seq`, minus the median of every other timed row -- since its compile
  row carries no number by schema design; not exercised by an
  end-to-end fixture record here, so unit-tested directly instead, see
  `_lazy_jit_derivation`'s docstring), and renders a self-describing
  report in markdown (default) or TSV. It never runs an engine.
  Every non-obvious design call this module makes beyond what
  requirements.md/harness_contract.md/record_schema.md pin down
  explicitly (the ns/call comparable, the two ranking grains, the
  `--include-synthetic` addition, the mixed-version-refusal ordering
  relative to per-record invalidity, the `form` column's show/hide
  rule) is stated in `report.py`'s own module docstring -- read that
  before changing the reduction or filtering logic.
- `__init__.py` -- package docstring only; states the scope split with
  `b3harness`.
- `__main__.py` -- CLI dispatch. Only `report` exists here
  (`python3 -m pcrecbench report ...`); merges with b3harness's fuller
  dispatcher at integration time.
- `tests/` -- see its own CLAUDE.md.

## Running the reporter

    python3 -m pcrecbench report --store pcrecbench/tests/fixtures/store \
        --include-synthetic                          # --grain set (default)
    python3 -m pcrecbench report --store pcrecbench/tests/fixtures/store \
        --include-synthetic --grain subject           # per-subject drill-down
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
