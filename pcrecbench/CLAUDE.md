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

## The reporter, [B9] columns/rulings (2026-08-25)

`report.py` gained nine rulings on top of the [B5] MVP below (docs/dev/
plan.md row [B9]; requirements.md OD-B11, OD-B13, OD-B14, OD-B15; the
pcrec manager's repin-report feedback), stamped as `reporter: v2
(2026-08-25)` in every render:

- **R1/OD-B14 — status.** Every ranking row carries the record's
  `status`; a non-`measured` row is excluded from ranking by default
  (listed under its table as `not ranked: <testee> -- <status>
  (<excerpt>)`), `--include-unmeasured` ranks it with status shown.
- **R2/OD-B15 — duplicate testee_id, AMENDED (manager, 2026-08-25,
  before merge).** The NEWEST *MEASURED* record per (subbench@version,
  testee_id, machine) ranks by default — not merely the newest by
  `run.timestamp`, because a non-measured record is not evidence against
  a measured one of the same testee and version (pcre2 does not change
  between two runs of the identical pin). Older-than-kept records are
  SUPERSEDED (named in the header, never pooled); a NEWER-than-kept
  record that is not `measured` does NOT supersede it and is listed
  separately as "newer, not measured"; only when no record in the group
  is measured does the newest overall stand (itself unranked per R1
  unless `--include-unmeasured`). `--all-records` is unchanged by the
  amendment: every record still shows as its own row, testee id suffixed
  `@<compact-timestamp>`.
- **R3 — `tier` (ahead of schema v1.2).** Coded as "absent = pinned"
  before lane b10loop's optional `tier` setup field lands in the shared
  validator; a `scratch` row excludes from ranking by default (listed as
  `scratch: <testee>`), `--include-scratch` ranks it with a `tier`
  column. Untestable through a real fixture file until the schema knows
  the field (`additionalProperties: false` on `setup`) -- tested
  directly against `build_report`/`LoadedRecord`, bypassing the
  validator, same technique as the lazy-JIT unit test.
- **R4 — `fact`.** A column beside `form`: `whole-subject` restates as
  `separate artifact`, `plain` as `same program` (record_schema.md 5
  ADDITIONS 3 makes this a restatement, not a lookup -- rule X27
  guarantees the two coincide). A ranking table whose rankable rows mix
  both facts carries a note under its title (the "regime artifact"
  bucket is a stated fact, not a footnote).
- **R5 — two ratios.** `vs baseline` (the reference testee, ALSO named
  in the table title) and `vs best` (best measured row = 1.000x).
- **R6 — near-floor.** `short-subject-search` tables (SET grain) always
  carry `n subjects` and `per-subject mean ns`, plus a `floor: n/a (no
  floor pattern in this set yet)` note -- no field for a real number
  exists in the schema yet; the note says so rather than inventing one.
- **R7/OD-B11 — give-ups and hazard outcomes by name.** A set cell's
  give-up count is shown as `gave-up: <CODE>x<n subjects> (smallest:
  <id>, <bytes> B)`, grouped by the DOMINANT code
  (`_gave_up_cell_summary`), counted in SUBJECTS not trials; `crashed`/
  `timed-out` get their own name in the per-subject failure label
  (`_failure_label`), never folded into an unnamed "(other)". The CODE
  itself comes from `pcrecbench.reduce.giveup_code` (lane b10loop's
  SHARED extractor, imported by name once b10loop landed it) -- it
  keeps a pcrec diagnostic's numeric code alongside its name
  (`-3:PCREC_ERR_FRAMES`) and falls back to the raw diagnostic
  (truncated to 64 chars) for an engine whose diagnostic never carries
  the `giveup:` protocol token (pcre2 today); this reporter groups by
  whatever string that function returns rather than reformatting it, so
  `quick`'s inline printout and this table read the same code.
- **R8 — cross-pin Δ.** Two testee_ids sharing (engine, config) at
  different `version_slug`s (record_schema.md 6.4) get a `Δ vs previous
  version` column (SET grain only): `unchanged (within spread)` when the
  medians differ by no more than 2x the larger stddev, else `faster/
  slower xN.NN`; a per-row "worst subject" note; a cell excluded at the
  previous pin and ranked now reads `now measured (was: <reason>)`. Two
  records of the SAME version (e.g. `--all-records`'s two rows of one
  identical pin) are explicitly NOT a cross-pin pair.
- **R9 — mechanism stamps.** pcrec's own compile-row `engine_metadata`
  (never `diagnostic`) rendered as columns on the `compiled-aot` table:
  `engine`, `entry` (`_in` when a buffer-capacity pair is present, else
  `plain entry` -- DERIVED, no field is named `entry`), `prefilter` (a
  DFA row states `(no stamp -- pcrec I-3)`, never a blank), `vm_rungs`
  (bit names joined by `|`), `buffer_frames`/`buffer_trail`,
  `resume_frame_size`; the table also splits by phase (`emit-c ns`/`gcc
  ns`/`load ns`) and flags `stddev > median` rows `timer jitter`.
  OD-B13: `--subbench` now also accepts the sub-bench DIRECTORY name
  (`email`), resolved via `bench/<dir>/subbench.toml`'s own `id`.

Details, worked examples and the exact verdict rules are in
`report.py`'s module docstring (the authoritative version) and its
per-function docstrings (`_gave_up_cell_summary`, `_cross_pin_verdict`,
`_mechanism_stamp_columns`, `_form_fact`, `resolve_subbench_arg`, etc.).
`pcrecbench/tests/test_report.py` has one test per ruling (11 new tests,
31 total at [B9]). `reports/*` were regenerated against `reporter: v2`
at [B9] -- see `reports/CLAUDE.md`.

## The reporter, [B14] follow-ups (2026-08-25)

The pcrec manager's SECOND reading of the reporter-v2 re-pin rendering
(docs/dev/feedback_pcrecdev1_2026-08-25-repin-v2.md) landed ten more
rulings on top of [B9]'s, stamped as `reporter: v3 (2026-08-25)` (two
separate `R1`..`R10`/`R1`..`R9` sequences -- [B9]'s and [B14]'s share
numbers by coincidence, not by design; read each ruling by its dated
section in `report.py`'s module docstring):

- **R1 -- plain-entry capacities.** A compile row with no `buffer_frames`/
  `buffer_trail` pair is not bufferless: it runs on the STAMPED DEFAULT
  capacity (`engine_metadata`'s `resume_frames`/`trail_frames`), read and
  shown as `buffers=2048/3072 (stamped default)` -- [OPT-1]'s own cost is
  proportional to exactly this number.
- **R4 -- the buffer/frame legend.** `n/s` (neither pair stamped at this
  pin) vs `0 (DFA)` (stamped, and zero because a DFA artifact takes no
  buffers) -- `-`/bare `0` never again stand for two different facts
  (`_buffers_display`/`_frame_size_display`).
- **R8 -- legend, not repeated columns.** The compile-cost table's six
  per-testee CONSTANT columns (`engine`, `entry`, `prefilter`,
  `vm_rungs`, R1/R4's buffer/frame facts) moved to a one-line-per-testee
  LEGEND above each `has_pcrec` table (`_testee_legend_line`), leaving
  the table itself to phase numbers, R7's artifact bytes and R5's
  jitter; the Query header's superseded-record list collapsed to one
  summary line (`--all-records` still lists every id).
- **R5 -- jitter is computed.** `stddev/median` (three decimals), or
  `timer-floor` when `min_ns` sits under a 20-microsecond floor --
  replacing [B9]'s boolean; a jitter column empty on EVERY row of one
  table is omitted from that table, not rendered as a wall of blanks.
- **R7 -- artifact size.** A compile row's own `artifact_bytes` is now a
  column on every compile-cost table, pcrec and non-pcrec alike.
- **R2 -- tiny sets.** A SET-grain cell of <= 3 subjects (today, every
  `large-subject-throughput` cell) gets a per-subject sub-table under its
  ranking row (subject id, bytes, median ns/call, ns/byte, every ranked
  testee); every throughput ranking row also gains `ns/byte` beside
  `ns/call`.
- **R3 -- matching-subject count, CORRECTED same day (KB-2,
  docs/dev/known_issues.md; manager steer 2026-08-25).** This ruling's
  first cut read `bench/<dir>/expectations.tsv` live through
  `pcrecbench.subbench` -- superseded, because the reporter must work
  from RECORDS ALONE (a record measured elsewhere, or against a later
  sub-bench version, has no sidecar checkout beside it). The record
  itself carries no field to derive this from either:
  `pcrecbench.harness.outcome_for` sets `observed = None` on the common
  `matched-as-expected` row (checked against real store data), so
  `_matching_subject_count` now always returns `None` and the rendered
  line reads `matches: n/s` -- honest, not fabricated, not silent.
  `report.py` no longer imports `pcrecbench.subbench` at all. Fixing
  this for real needs a schema/harness change (a real expected-answer
  field on a match row), not a reporter-side inference from the
  disagreeing minority (`observed` IS populated there, but inferring `m`
  from only that subset would systematically undercount it -- see the
  function's docstring).
- **R6 -- worst now vs largest Delta.** A cross-pin `Δ detail` line now
  names `worst now` (the new record's own slowest subject, [B9]'s
  meaning) and, only when it differs, `largest Δ` (the subject whose
  ns/call moved the most, `_largest_delta_subject`) beside it.
- **R9 -- the floor pattern.** Schema v1.3's optional `patterns[].role`
  (`member` default | `floor`, lane b15floor): a `role: floor` pattern's
  own short-subject-search table is retitled a per-call overhead CONTROL
  rather than ranked, and every other (member) pattern's short-subject-
  search row gains a `floor ns` figure beside its per-subject mean
  (`_floor_mean_for`). Landed same-day as b15floor's schema v1.3, so
  exercised BOTH ways: the original hand-built `LoadedRecord`s (the [B9]
  `tier` tests' bypass technique) and, once v1.3 made `patterns[].role`
  schema-legal, a REAL fixture file (`fixtures/floor_pattern/`) accepted
  by `schema/validate.py` itself -- proving the wired path end to end,
  not just the reduction logic.
- **R10 -- `reporter: v3 (2026-08-25)`, then `v4` the same day** for the
  KB-2 correction above (this module's own rule: bump whenever rendering
  changes, so two reports are never mistaken for each other); every
  committed report under `reports/` regenerated against `v4` -- see
  `reports/CLAUDE.md`.

`pcrecbench/tests/test_report.py` gained eleven more tests (one per
ruling, plus the R9 fixture-validated proof; 42 total). `reports/*`
regenerated against `reporter: v4` -- see `reports/CLAUDE.md`.

## The reporter, [B16] rulings (2026-08-28) -- the abi-8 re-pin's half

The re-pin to pcrec `35e1ab1` (abi 8) absorbed five pcrec pins of new
observability, and its inbox items I-5, I-6, I-7 and I-11 asked the
reporter for four rules by name. A THIRD `R1`.. sequence, independent of
[B9]'s and [B14]'s (the three share numbers by coincidence of three
separate sequences; read each ruling by its dated section), stamped
`reporter: v5 (2026-08-28)`:

- **R1 -- the DFA scan's mechanism, and "(no stamp -- pcrec I-3)"
  retired.** I-3 is CLEARED: every artifact that CONTAINS a DFA scan --
  every DFA artifact AND every VM HYBRID -- stamps `RX_DFA_SCAN`,
  `RX_DFA_PREFILTER` and (abi 7) `RX_DFA_TABLE`. The legend carries all
  three (`_dfa_scan_display`) and keeps the VM's own `RX_VM_PREFILTER` as
  a SEPARATE clause: two selections, not two spellings, and a hybrid
  answers both independently. `_dfa_scan_display` keeps THREE absences
  apart that one blank would merge -- "no DFA scan" (abi >= 6, read from
  `rx_info.scan == NULL`, the spec's own iff), "hybrids did not stamp
  yet" (abi 4-5, which says NOTHING either way), and "before the stamps
  landed" (abi < 4) -- deciding which from the record's own `abi` pair.
  pcrec I-5's hazard, in the reporter: read the value, never the absence.
- **R2 -- the fast tier in the legend** (`_fast_tier_display`):
  [OPT-1]'s boundary, and pcrec's ONLY spelling of "one tier"
  (`fast == stamped default`). Above the boundary an un-suffixed call
  runs twice, so a `pcrec-vm` vs `pcrec-vm-in` gap is not interpretable
  without it.
- **R3 -- the legend is per (testee, PATTERN, form)**, collapsing to one
  line when a testee's cells genuinely agree (a CHECKED fact about the
  rows). This CORRECTS [B14] R8, which took the first
  `sample_engine_metadata` it saw for a testee and printed it as the
  whole testee's mechanism: MEASURED on this repo's own records, at pin
  8da6120 `pcrec-auto` compiled `orig` to a DFA artifact and `factored`
  to a VM one, and the legend said `engine=dfa` for both because `orig`
  sorted first. `_engine_reading` prints `inferred (unstamped pin)` where
  nothing was read, and `unknown` for an `auto` config -- `--engine=auto`
  chooses per PATTERN, so the config fixes the REQUEST, not the answer.
- **R4 -- a give-up code names an engine; a cross-pin Δ can be a
  SELECTION CHANGE.** `PCREC_ERR_STEPS`/`_FRAMES`/`_WORK`/`_RECURSE` all
  need a budget a DFA artifact stamps `-1` for. `_cross_pin_info` asks
  whether the two pins are the same ENGINE before computing any ratio,
  reading each side's engine from ITS OWN (pattern, form) compile cell
  and falling back to the give-up witness on an unstamped pin; when they
  differ it prints `selection changed (dfa -> vm)` in place of
  faster/slower ×N. A selection change EXPLAINS a `now measured` rather
  than replacing it -- only the RATIO is what two engines make
  meaningless.
- **R5 -- the gcc-ms band as an independent witness** (`_GCC_BAND_NS`,
  `_gcc_band_witness`): a DFA artifact's gcc phase measured 124-140 ms on
  this box against a VM artifact's 400-540 ms (I-7 §4). Consulted ONLY
  where nothing was stamped, printed AS a witness, never filling the
  engine field, and abstaining rather than guessing between the bands. It
  is box- and toolchain-specific by construction, which is the other
  reason it may not become a value.
- **R6 -- "max is trial 1" beside the jitter ratio**
  (`_max_is_first_trial`): the fact that separates a warm-up from noise,
  which a ratio alone cannot. A FACT, not a verdict, and `None` when
  unanswerable.
- **R7 -- a dominated set-grain ratio says so** (`_dominant_subject`,
  threshold 90 %): with a note pointing at the per-subject rows. The
  measured case: pcre2-interp's throughput set is 99.9 % one subject, so
  its "3.15× slower than JIT" was 7.7× slower on that subject and 144×
  FASTER on the other two.
- **R8 -- `reporter: v5 (2026-08-28)`**, and every committed report under
  `reports/` regenerated: R3/R4/R6/R7 change the rendering of records
  already in `store/`.

`pcrecbench/tests/test_report.py` gained seven tests, one per ruling,
each with its control (the three absences must render DIFFERENTLY; an
evenly-spread set must NOT be flagged; a stamped engine gets no witness
line); four [B9]/[B14] tests that pinned superseded WORDING now check
their own ruling's facts instead of a sentence another ruling owns.
49 total, all green.

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
