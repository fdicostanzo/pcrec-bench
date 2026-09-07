# pcrecbench/ — the harness package

`python3 -m pcrecbench run --subbench email --testee pcre2-jit` measures one
CELL and writes one RECORD. The spec is `docs/design/harness_contract.md`;
the record's shape is `docs/design/record_schema.md`.

| file | role |
|---|---|
| `__main__.py` | the CLI: `run` (`--tier pinned\|scratch`), `quick` (the edit-test loop's one-cell surface, [B10]), `index`, `quiet`, `testees`, `report` |
| `harness.py` | contract §4's seven steps; `outcome_for()` is the ONE place an engine's answer becomes a `match_outcome`; `run_cell(tier=, patterns=, subject_limit=, budget=)` is what `quick` parameterises — no second code path |
| `subbench.py` | loads `bench/<name>/`; owns the regime→subject mapping and `subbench.content_hash`; `_load_manifest` is GENERIC on a subject manifest's column count (4, the original shape, or 5 with `periodic` appended, [B17]) — no column position is hard-coded beyond "periodic, if present, is last". `bench/loglines`' manifests use the same column, in the same place ([B11.1]). Since KB-12 ([B36]'s incident): `Subbench.__init__` checks EVERY pattern and subject id (short and throughput) against the record schema's own `$defs/slug` rule (`check_id`, `_slug_pattern` — the regex is READ from `schema/record.schema.json`, never retyped) and raises `SubbenchError` naming the offending id, the set and the rule, so `run`/`quick` refuse in under a second instead of after every trial of a cell has already run (bench/syntax@0.1's incident: six cells, 259 minutes, 0 records written, all refused at `store.write()`'s validator) |
| `adapters.py` | the `Adapter` interface, discovery, and **the DRIVER PROTOCOL** (in full, at the top of the file) |
| `driverrun.py` | build/run/parse a driver; the resume-after-driver-death rule |
| `record.py` | builds the record dict; every derived id comes FROM `schema/validate.py`'s own functions |
| `reduce.py` | the SET-GRAIN reduction `quick` prints and the reporter ranks (R5, [B10]): `reduce_set_cell`, `reduce_match_cell`, `cells_from_record`, `giveup_code`; pinned by a hand-computed fixture in `tools/selfcheck.py`. Since [B20] also THE ONE derivation of the v1.4 `trial_agreement` block (`judge_trial_agreement`, gate_shape_v14.md §3.5) and its shared rendering (`agreement_line`) — the harness stamps with it, `quick` prints it, the reporter renders it, and `schema/validate.py` carries a deliberate SECOND implementation X32 compares it against |
| `store.py` | the store path rule, never-clobber, validate-before-write, the index; the TIERS: `.canonical` marks the canonical store, which refuses a `tier: scratch` record on write and on index; `scratch_store()` is `$PCRECBENCH_SCRATCH_STORE` or `build/scratch-store/` |
| `quiet.py` | the quiet-box instrument and its two thresholds (`docs/design/quiet_baseline.md`) — since BD7 (2026-08-30) the occupancy sample is `mpstat -P ALL 1 5` judged on its `Average:` block (`judge_mpstat`, pure; `split_mpstat`); `OCCUPANCY_SECONDS`. Since [B20] (schema v1.4) `judge_mpstat` also writes the TARGET core's tri-state `target_busy_pct`, `gate()` is the whole PRE-FLIGHT (load1, the non-target average, the target's own reading, the missing-row refusal — the `quiet` CLI judges through it too), `preflight_ok`/`after_notes` replace `occupancy_ok` (the after samples are PROVENANCE), and `cpu_times`/`timeline_item` read the per-group `/proc/stat` timeline |
| `env.py` | the `environment` block; the machine registry |
| `oracle_pcre2.py` | the libpcre2 ctypes binding, copied from pcrec (see its header) and extended: anchoring bits, `find_all`, an explicit give-up surface, and `pattern_info()` ([B11.1] — PCRE2's own first/REQUIRED code unit and min length, the analysis `bench/loglines` is built around) |
| `periodic.py` | the `periodic` manifest column's DEFINITION (inbox I-10, [B17]): `smallest_period` / `periodic_field`, the smallest exact repeat period in [1, 4096] bytes or `no`. Moved here from `bench/email/` when `bench/loglines` became its second caller ([B11.1]) — the column means the same thing in every manifest because one function computes it |
| `expectations.py` | the GENERIC expectation chain every `bench/<name>/gen_expectations.py` runs: one row per (pattern × subject × declared regime) from the libpcre2 oracle, `--check` mode, the no-capture-participated assertion, and the rule that an oracle give-up is DROPPED and listed rather than recorded as `nomatch`. Lifted out of `bench/email/gen_expectations.py` when the second sub-bench arrived; two copies would be two chances for two sets' expectations to be derived by different rules |

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
50 total, all green (corrected here from a stale "49" -- the [B16] count
text had drifted from the actual `TESTS` list by one; found while
counting for [B12] R10's own addition below).

- **R9 -- the per-subject sub-table is keyed on the REGIME.** [B14] R2's
  `<= 3 subjects` rule was "every throughput cell" only while the
  throughput sets had three subjects; at email-specimen@0.2 (five) and
  bench/loglines (twelve) it dropped the table. A
  `large-subject-throughput` cell, a `dominated` cell, and a <= 3 set all
  get it (`test_per_subject_subtable_b16_r9`). `reporter: v6 (2026-08-28)`;
  every committed report re-rendered.

## The reporter, [B18] (2026-08-29) -- the abi-11 re-pin's half

The re-pin to pcrec `36d5963` (abi 11; inbox I-15/I-16/I-17) added six
`engine_metadata` pairs to every pcrec compile row (`dfa_prefilter_offsets`,
`dfa_match`, `unroll_k`, `unroll_k_why`, `max_emit_code_bytes`,
`max_emit_bytes`; `dfa_prefilter` gains `offset-set` / `offset-set-bounded`).
The reporter change is deliberately SMALL and additive -- no version bump,
no re-render, every committed report byte-identical:

- `_mechanism_stamp_columns` carries `dfa_prefilter_offsets` and `dfa_match`
  (`-` when absent, as every other absent pair).
- `_dfa_scan_display` appends ` offsets=0,8*,13` to the `dfa:` clause when
  the record carries the pair; `_match_form_display` gives the legend a
  `match=unwrapped` / `match=search-filter` clause when the record carries
  `dfa_match` -- and NOTHING when it does not, because that absence has two
  causes (a VM artifact at any abi, a DFA artifact before abi 10) that the
  reader tells apart from the `engine` and `abi` on the same line, and
  rendering a guess is pcrec I-5's hazard again. The TSV gets a
  `compile_stamp` row for each of the two only when carried.
  `test_b18_offsets_and_match_form_in_legend` pins both directions (50
  tests).
- RECORDED BUT NOT RENDERED, for the manager to rule: `unroll_k` /
  `unroll_k_why` / `max_emit_code_bytes` / `max_emit_bytes`. On both
  sub-benches every VM artifact reads `8` / `default` under the default
  caps (I-17: 0 K movements, 54/54 accept), so a column would be constant
  today; the pairs are in every record for the day a K moves or a cap is
  raised, and [B11.4] bounded-repeat is where that is expected first.
- THE [SEL-1] FALLBACK AND HOW IT IS BUCKETED. `level-context` under
  `pcrec-auto` is now a VM artifact (`engine=vm`, `vm_prefilter=none`, no
  DFA scan, `K=8/default`) whose compile row's `diagnostic` is
  `RX_ENGINE_WHY: dfa overflowed: >32000 states at pattern offset 0`. The
  reporter shows the mechanism stamps as for any VM artifact, and its
  ranking compares the cell against the JIT as a measured row (Frank's ask
  (b)); what it does NOT show is WHY `auto` chose the VM -- that fact
  exists only as prose (record_schema.md 7 keeps `RX_ENGINE_WHY` out of the
  pairs), and the [B9] R9 rule is that a mechanism column never reads
  `diagnostic`. Separating "auto picked the VM" from "auto fell back to the
  VM" as a STRUCTURED fact needs pcrec to stamp the selection reason as an
  enum (an O-8 ask), or a bench-side rule that a `diagnostic` prefix may
  feed one declared pair -- a ruling, not a lane's call. Until then the
  distinction is readable in the compile-cost table's diagnostic column.

## The reporter, [B19] (2026-08-30) -- the abi-12 re-pin's half

The re-pin to pcrec `96e44c2` (abi 12; inbox I-18, [OPT-4] ruling B +
[DD-11]) added six `engine_metadata` pairs to every pcrec compile row:
three stamps (`engine_sel` on every artifact; `vm_prefilter_lang` +
`vm_prefilter_lang_why` on every VM HYBRID and no other artifact) and
three adapter-side facts (`emit_bytes` / `emit_code_bytes` on every
compiled artifact -- pcrec's own size definition, ported and controlled;
`warned_emit_bytes` only where pcrec's advisory `--warn-emit-bytes` line
fired). The reporter change is again SMALL, additive and CONDITIONAL --
no version bump (still `v7`), every committed report byte-identical,
`test_b19_engine_sel_lang_and_emit_bytes` pins both directions (54 tests with the scope addition below):

- THE LEGEND LINE gains `sel=<engine_sel>` right after `engine=`, and
  `lang=<vm_prefilter_lang> (<why>)` right after `vm_prefilter=` -- each
  only where the record carries the pair (`_engine_sel_display`,
  `_prefilter_lang_display`; None -> no clause, as [B18]'s `match=`).
- FRANK'S ASK (b), DERIVED FROM THE RECORD BY ONE RULE: a `sel` that is
  neither `selected` nor `forced` renders as
  `sel=collapsed-prefilter (DFA fallback tripped)`. The rule is the
  ruling's own (`_ENGINE_SEL not in (selected, forced)`), not an
  enumerated copy of pcrec's token set, and a legend NOTE under the lines
  (printed only when a `sel=` appears) states it so a reader need not
  know the tokens. What the [B18] note above called "a ruling, not a
  lane's call" is answered: pcrec stamped the reason as a closed set,
  and the mechanism column never reads `diagnostic`.
- THE ONE RESCUE THE BUCKET MISSES, stated in that note: the SIZE-CAP
  retry rung (an emitted-size cap refused the exact artifact; the retry
  ships a count-collapsed hybrid) stamps `sel=selected` -- measured at
  the pin on K41's witness 2 -- so its only trace is
  `lang=count-collapsed (size cap retry, exact N > cap)`. A finding for
  the outbox; the legend shows both facts side by side.
- THE COMPILE-COST TABLE gains `emit bytes` and `code bytes` beside
  `artifact bytes` (the `.so`) when any row of the table carries them
  (R5's rule for an empty column -- an older pin's table renders as
  before): comment-excluded C source (what pcrec's total cap measures)
  and that minus table initializers (what the code cap measures; the
  quantity that tracks gcc time -- a table-dominated DFA artifact is
  large in the first and small in the second). The emit cell reads
  `724,699 (warned)` where `warned_emit_bytes` is present
  (`_emit_bytes_display`); the warning is never an outcome.
- THE TSV gets `compile_stamp` rows for the three abi-12 pairs and
  `compile` rows for the three size facts at `artifact_bytes`'s grain,
  each only when carried.
- SCOPE ADDITION (manager, 2026-08-30, same branch): the abi-11
  [ART-SIZE] stamps recorded since [B18] and never rendered -- bounded's
  first sample's only K movement (`nest3-16` = K=1 / size-model on every
  VM form) had to be read out of the JSONL -- now sit on the same legend
  line for VM artifacts: `K=<unroll_k>/<unroll_k_why>` and
  `caps=<max_emit_code_bytes>/<max_emit_bytes>` (`_size_term_display`,
  `_caps_display`, after `rungs=`), with a legend note naming them. A
  DFA artifact shows neither (no counter rung; the code cap is absent from
  its metadata by design). `test_b19_size_term_and_caps_in_legend` (54
  tests): the firing case, the default K, a DFA control, an abi-8 control,
  the note's presence and absence.

**v8 (2026-08-30).** The `sel=`/`lang=`/emit-bytes half above landed
`REPORTER_VERSION` unchanged at `v7` -- no record in the store at the
time carried the abi-12 pairs, so every committed report was
byte-identical. The SCOPE ADDITION just above (the abi-11 `K=`/`caps=`
legend clauses and their note) does not have that luxury: bench/bounded's
first sample and both 36d5963 re-pin reports already carry
`unroll_k`/`max_emit_bytes` pairs on their VM rows, so rendering those
EXISTING records changes under this addition -- the same case R8/R10
bump the version for. `REPORTER_VERSION` bumps to `v8 (2026-08-30)`
(precedent: [B12] R10 below); every committed report under `reports/`
regenerated with its own named query -- see `reports/CLAUDE.md`.

I-19 (3) follow-up (2026-08-30, manager): until pcrec's [LIM-1] gives the
SIZE-CAP rescue its own `RX_ENGINE_SEL` value, `_engine_sel_display`
also buckets a `selected` artifact whose `vm_prefilter_lang_why` starts
`size cap retry`, rendered `sel=selected (DFA fallback tripped: size-cap
rescue)`; the legend note says so; a `selected` hybrid with any other
why stays outside the bucket (the test's control). No committed report
changes: no record in the store carries a size-cap rescue (census over
the 96e44c2 records: 760 forced / 580 selected / 160 collapsed-prefilter,
every why a `dfa overflow retry`) -- this covers the [B19] AFTER sample
too (the only 96e44c2 records in the store), so the AFTER reports
rendered after this merge show no size-cap-rescue bucket either.

## The reporter, [B22] (2026-08-31) -- the fallback bucket reads the VALUE (v10)

The re-pin to pcrec `263b013` (abi 12 UNCHANGED; inbox I-25, pcrec
[OPT-4.1] + [LIM-1]) adds no pair -- it adds two `engine_sel` VALUES
(`declined-nullable`, `size-cap-retry`) and one `vm_prefilter_lang_why`
value (`nullable collapsed language`). The reporter change is ONE rule
and its note:

- `_engine_sel_display`'s bucket is `sel not in (selected, forced)` and
  NOTHING else. The I-19 (3) interim rule -- also bucketing a `selected`
  artifact whose `vm_prefilter_lang_why` starts `size cap retry`,
  rendered `size-cap rescue` -- is RETIRED (inbox I-25: pcrec's [LIM-1]
  gave that rescue its own token, and "your bucket reads the value now,
  not the _LANG_WHY prefix"). An OLD (96e44c2) record with that shape
  renders `sel=selected` unbucketed, its why still readable in the
  `lang=` clause; no stored record carries the shape (the [B19] census),
  so no committed NUMBER moved.
- The legend note's wording changes accordingly on every report that
  prints a `sel=` clause -- twelve committed files -- which is the
  regenerate-everything case: `REPORTER_VERSION` bumps to
  `v10 (2026-08-31)` and every committed report under `reports/` was
  regenerated from its own header query (see `reports/CLAUDE.md`).
- `test_b19_engine_sel_lang_and_emit_bytes` now pins the retirement both
  ways (the old shape unbucketed -- the control; `size-cap-retry` and
  `declined-nullable` bucketed by value, the decline with no `lang=`
  clause), and `_classify_v9_diff` skips the CURRENT version line
  instead of a hard-coded `v9`. 59 tests, count unchanged.

## The reporter, [B28] (2026-09-01) -- KB-5's `--testee` roster filter, KB-6's `edge=` clause (v11)

Two independent reporter-only fixes, one wave (docs/dev/known_issues.md
KB-5, KB-6):

- **KB-5 -- `--testee TESTEE_ID`.** Repeatable, exact match on the
  literal `testee.testee_id` (same spelling as `run --testee`), OR'd
  within its own occurrences and AND'd with every other filter -- same
  shape as `--where`. Lets a committed query name its roster explicitly
  (`--testee pcrec_a7e0bdf_auto-caps-simdna --testee
  libpcre2_10.46_jit-caps-simdna`) instead of relying on a
  `--since`/`--until` range that cannot express "this pin OR that
  unpinned baseline" -- the gap the loglines@0.1 AFTER-at-263b013 report
  hit (KB-5's own history). Deliberately UNLIKE every other filter here:
  an id matching NO record anywhere in the loaded store (checked before
  any other filter narrows the selection) is a REFUSAL naming the
  unknown id(s) and the known ones, not a silently empty report --
  `--subbench nope` still narrows to nothing. Printed in the Query
  header as one `testee=<id>` line per occurrence.
- **KB-6 -- `edge=<range|bitmap|mixed|none>`.** pcrec abi 13's
  `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, pin a7e0bdf) on the legend line,
  right after the `dfa: scan=... prefilter=... table=... [offsets=...]`
  composite clause -- the SAME scope (`dfa-scan`: every artifact whose
  DFA scan is stamped, VM hybrids included) rather than `dfa_match`'s
  narrower dfa-only scope, so it sits beside `offsets=` rather than
  among the VM-only `K=`/`caps=` pair. Conditional (no clause on a
  forced-VM artifact, a non-hybrid VM artifact, or a pre-abi-13 record).
  A legend note names the four values, printed once under the lines that
  carry the clause. KB-6's own closing question -- whether the value
  belongs in the `sel=` fallback bucket or the [B16] R1-R8 ranking-group
  bucketing -- is answered as a RECOMMENDATION only (report.py's module
  docstring, "[B28]" section): scan-edge is a mechanism FACT independent
  of whether selection fell back, and the wave takes no bucketing
  action; a future finding that wants rows grouped by scan-edge shape is
  a new ruling, not a rendering change.
- `REPORTER_VERSION` bumps to `v11 (2026-09-01)`; every committed report
  under `reports/` regenerated -- see `reports/CLAUDE.md`. KB-5 is
  additive (no committed query used `--testee`, so no report's rendering
  moves from it alone); KB-6 changes the twelve `pcrec_a7e0bdf` reports'
  mechanism legends and adds the new note.
- Two new tests (`test_testee_filter_kb5`, `test_dfa_scan_edge_legend_kb6`),
  each with the shape's controls: KB-5's narrow/OR/AND/unknown-id-refusal/
  known+unknown-mix cases; KB-6's DFA-artifact firing case, the VM-hybrid
  case (edge present, no `match=`), the forced-VM control (no scope, no
  clause), the abi-12 control (no pair), and the note's presence/absence.
  61 total (`pcrecbench/tests/CLAUDE.md`).

## The reporter, KB-4's adapter half (2026-09-01) -- a refusal's emit-c time renders

`docs/dev/known_issues.md` KB-4 (schema half DONE at v1.4, [B20]):
`testees/pcrec/adapter.py`'s `_compile_one` now times the pcrec exec
(the `emit-c` phase) regardless of exit code and carries that number
forward on a `did-not-compile` result (I-20's ruling: pcrec prints no
timing on any path, so this is the bench's own clock); `record.py`'s
`compile_row` turns it into `cost = {"total_ns": ...}` on the row --
NEVER a `cost.phases` array (rule X12 requires `phases[].name` to equal
`compile_phases` EXACTLY whenever the key is present at all, and a
refusal never ran every declared phase). `_phase_medians` reads that
`total_ns` as the row's `emit-c` contribution precisely because a
refusal's `cost` never carries a `phases` array -- the same absence
that keeps X12 satisfied is the signal that tells a refusal's clock
apart from a compiled row's phase breakdown. Purely conditional and
additive: a compile cell that is entirely `did-not-compile` now shows a
real `emit-c ns` figure in the compile-cost table instead of `-`
(`gcc ns`/`load ns` stay `-` -- those phases never ran); a cell with any
`compiled` row is unaffected. `REPORTER_VERSION` UNCHANGED: no record in
`store/` yet carries a `cost` on a `did-not-compile` row, so every
committed report renders byte-identical -- the rendering fires the next
time a refusing cell is measured under the fixed adapter.
`test_kb4_refusal_cost_in_phase_medians` (`pcrecbench/tests/
test_report.py`) covers the firing case and three controls (a compiled
row's shape unchanged; a did-not-compile row whose cost DOES carry a
`phases` array is not read for emit-c; a did-not-compile row with no
`cost` at all renders exactly as before). 62 total
(`pcrecbench/tests/CLAUDE.md`).

## The reporter, [B12] R10 (2026-08-29) -- a did-not-compile cell is not-ranked, not invisible

M1 close item (docs/dev/plan.md row [B12], "[ADDED 2026-08-28]"; lane
b12close), kept the plan row's own label rather than opening a fourth
`R1..` sequence. Found on bench/loglines' first sample: `level-context`
under `pcrec-auto` did not compile at pcrec 35e1ab1 ("pattern too complex
for the DFA engine (>32000 states; try --engine=vm)") and vanished from
the RANKING entirely -- it still showed in the compile-cost table (every
compile row does), which is not where a reader scanning a ranking looks.
The cause: a testee whose compile fails contributes zero match rows, so
it never reaches `_ranking_groups` -- [B9] R1's `status` gate only
excludes a row that EXISTS.

Fixed at `build_report`: every compile cell whose `compile_outcome` is
`did-not-compile` (never `unsupported-by-declaration`, a testee's own
advance declaration and a different fact) is indexed by `(sb, pattern_id)
-> {testee_id: diagnostic}` (`ReportData.did_not_compile_by_pattern`)
independently of match rows, and every ranking group for that pattern --
either grain, every regime some OTHER testee actually ranked in --
prints a bullet under its table:

    not ranked: <testee> -- did-not-compile (<diagnostic>)

`<diagnostic>` is the record's own string verbatim, truncated to one
line with a stated note when it is multi-line (`_diagnostic_first_line`).
A THIRD source of "why is this testee missing", alongside [B9] R1's
status gate and R3's tier gate, not a replacement for either -- tracked
independently since a testee can fail one pattern and measure the next
cleanly in the same record. The TSV render gets the same fact as a
`did_not_compile` section row (`gave_up_summary` carries the diagnostic,
the only free-text column that fits). `pcrecbench/tests/test_report.py`
gained `test_did_not_compile_ranking_line_r10` (the firing case, two
hand-built testees sharing one pattern/regime group so the group exists,
plus a control pattern both compile cleanly on) and the version-pinning
test moved out from under [B14]'s name to `test_reporter_version_pin`
(it was never really that ruling's own -- every rendering-changing
ruling re-bumps `REPORTER_VERSION` and re-points it). 51 total. Also
fixed at [B12]: `test_report`'s runtime (`REAL_STORE` -- `store/` itself,
not a fixture -- grew to three sub-benches' worth of records, and
`schema/validate.py`'s jsonschema validation cost ~39 s per
`_load_store(REAL_STORE)` call; seven call sites in this suite each paid
it independently, which is where the suite's > 2 minute runtime went).
Fixed with a module-level cache (`_load_real_store()`,
`pcrecbench/tests/test_report.py`) shared by all seven call sites rather
than a marker that would have split the suite `make check` still needs
to run whole -- nothing in this suite or in `report.build_report`/
`render_markdown`/`render_tsv` mutates a `LoadedRecord` after
`report.load_all` returns it, so sharing one load across tests changes
nothing about what is asserted. Suite runtime: 274.6s -> 47.6s (measured
2026-08-29, same box, same 51 tests, all green both times).
`reporter: v7 (2026-08-29)`; every committed report under `reports/`
regenerated -- see `reports/CLAUDE.md`.

## The harness, [B12] the free_text note guard (2026-08-29, bounded's first window)

A record's `note` and `status_detail` are schema `free_text` (maxLength
8192, `schema/record.schema.json` $defs), and `harness.run_cell` filled
them from a per-cell LIST of sentences whose length grew with the set:
one "iters for (pattern, form, regime) = N: median per-iteration ..."
per calibration, 72 of them on bench/bounded@0.1 (24 patterns x 3
regimes, ~12 KB). The first bounded cell (pcre2-interp, 21 min on a
quiet box) was measured and then REJECTED at validation -- contract 4
step 5, a harness bug, nothing written -- and every following cell
would have been. Two changes: (1) the ROUTINE calibration sentence is
no longer a note at all -- every match row's `calibration` block
(`probe_iterations`, `probe_elapsed_ns`, `target_ns`) and its
`timing.iterations` already carry it; only a calibration that did NOT
meet its target (`calibration_note` set: capped by the per-trial
budget, no usable probe timing, a fixed count) is still a sentence,
"calibration for (...) = N iters: <why>"; (2) `record.join_notes(notes,
prefix)` is the ONLY path from the list to either field: it joins under
`record.FREE_TEXT_MAX`, dropping sentences from the END and ending with
"[+N note(s) elided ...]" so a truncation is visible, never silent.
`tools/selfcheck.py check_note_length_guard` (five checks) reads the cap
FROM THE SCHEMA JSON, replays the rejected record's own 72-sentence
shape, and validates the joined strings against the schema's own
`free_text` -- a control sharing no source with the constant it checks.
The rejected record itself was moved out of `store/` (never indexed);
the cell was re-measured.

## The harness, [B12] the occupancy AVERAGE (BD7, 2026-08-30, the same window)

Three of the six bounded cells came back `inconclusive-load` on the
1-s occupancy AFTER-sample alone (10.10 %, 20.2 % on one non-target
core; load quiet; before-sample clean) -- the fifth such record in two
windows. `pidstat -u 1` named the bursts: the VS Code remote server
(~40 % of a core for a second when the store or the window log
changes), the streaming manager's own ~9 %, a per-refresh `gh pr list`
from the status line. `quiet.occupancy()` now runs `mpstat -P ALL 1 5`
and `judge_mpstat()` (pure -- `split_mpstat` separates the per-second
blocks from mpstat's own `Average:` block) judges the five-second
per-core AVERAGE against the unchanged 10 % bar; `raw` keeps the
Average block and the per-second peaks; `occupancy.tool` names the
command, so pre-BD7 records (`... 1 1`) stay distinguishable; schema and
X26 untouched. `tools/selfcheck.py check_occupancy_average`: seven
controls on a synthetic capture (a 1-s 30 % burst passes on the average
and fails judged alone; a sustained 100 % core fails; the target core is
excluded iff asked; a single-interval capture is judged as itself).
Ruling and evidence: docs/dev/decisions.md BD7,
docs/design/quiet_baseline.md (2026-08-30 section).

## The harness and reporter, [B20] THE GATE'S SHAPE — schema v1.4 (2026-08-30)

`docs/design/gate_shape_v14.md` (SPEC; Frank's ruling I-19: BD7 ratified
as the gate, the after samples provenance, trial agreement decides),
implemented here as one wave. What a reader of this package must know:

- **The PRE-FLIGHT is the gate.** `run_cell` computes `pinning` FIRST and
  passes `pinning["cpu"]` into `quiet.check` (one source for "the target
  core", ruling R-2); `quiet.gate()` refuses (exit 3) on load1 before,
  the busiest non-target 5-s average, the TARGET core's own reading, a
  target row missing from the capture, or an unavailable sample. On a
  quiet box `--force-unquiet` changes nothing (the flag is not a status).
- **The AFTER samples are provenance.** Recorded exactly as before, X19/
  X26 still enforced, never a verdict on the status; `quiet.after_notes`
  renders each failure as one sentence ("after-sample (provenance, not a
  verdict): ..."), into `note` on a measured record and `status_detail`
  otherwise. The old "occupancy differed across the run" sentence is
  retired.
- **Trial agreement decides `measured` vs `inconclusive-spread`.**
  `reduce.judge_trial_agreement(rows)` (rule `v1.4-group`: k=1.5,
  d_min=2, share_c=3, N ≥ 5 and odd; the arithmetic is gate_shape_v14.md
  §3.5, spelled a second time in `schema/validate.py` for X32) stamps
  `setup.trial_agreement` on EVERY record (X33); the pure
  `harness.derive_status(reasons, agreement, tier)` implements the §5
  decision table — `inconclusive-load` takes precedence (both facts in
  `status_detail`); a PINNED record without five odd trials is
  `inconclusive-spread`; a SCRATCH one keeps the pre-flight's status
  (E-2: `quick`'s 3 trials and the `--trials 1` smoke never write
  `inconclusive-spread`).
- **The sentences are ORDERED and the status one never elided.**
  `record.join_notes(notes, prefix=, first=)`: `first` (the gate's
  reasons or the §3.4 trial-agreement line) sits at offset 0 and cannot
  be dropped; elision only ever removes calibration/adapter notes and
  the marker names that class (ruling R-4). Today's `note`/
  `status_detail` split is kept (R-5).
- **Exit code 4** (contract 4): the written record is
  `inconclusive-spread`; `scripts/run_window.sh` re-measures such a cell
  ONCE (the first record stays); `pcrecbench index` prints a per-status
  breakdown (`store.status_breakdown`).
- **The per-group timeline** (§3.6, provenance only): on a pinned run
  with a readable `/proc/stat`, one `occupancy.timeline[]` item per
  (pattern, regime, form) group — the target core (our own driver), its
  SMT sibling, the busiest other core over the group's passes. No rule
  reads it; the reporter shows it under `--include-provenance`.

The reporter's half is v9 — R1 (an `inconclusive-spread` bullet printed
FROM THE BLOCK), R3 (the trial-agreement legend), R4 (`agreement:` per
record line; `n/a (v1.x)` for a pre-1.4 record, never re-judged), R4′
(the X13 rule marker: the `status rule:` legend line, and
`measured@1.3`/`measured@1.4` status cells when one query mixes X13
versions), R5 (`--include-provenance`), R5′ (the unconditional `after:
load1 … / occ …%` clause on a record whose after sample failed) — see
the module docstring's "[B20] SCHEMA v1.4 WAVE" section and
`tests/CLAUDE.md`.

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

## The reporter, [B26] (2026-09-01) -- pcrec abi 14's EIGHTH route token (v11, unchanged)

The re-pin to pcrec `1989c62` (abi 15) adds no pair. It adds ONE
`engine_sel` value -- `declined-nullable-default` ([OPT-4.2]: the
nullability decline with NO rung; nothing overflowed, and the ORDINARY
hybrid's own EXACT prefilter language is nullable, so the prefilter is
declined). The reporter change is one rendering rule and one conditional
sentence:

- THE BUCKET IS UNCHANGED. Frank's ask (b) is `sel not in (selected,
  forced)` and the eighth value is outside that pair, so it IS bucketed
  (`adapter.ENGINE_SEL_FALLBACK`, six values now). An artifact whose own
  prefilter a policy declined did not get auto's ordinary answer, and a
  reader comparing it with its `selected` siblings needs to see that.
- THE SUFFIX IS NOT. ` (DFA fallback tripped)` would be a FALSE sentence
  on this token -- no cap was hit and no fallback ran. `ENGINE_SEL_NO_CAP`
  maps it to ` (prefilter declined, no cap hit)` instead, so the bucket
  stays one predicate while the report's own sentence stays true. pcrec
  draws the same line (match_api.md 6.3: the value is "deliberately NOT
  among the five" fallback values); the adapter's
  `ENGINE_SEL_OVERFLOW_FALLBACK` names pcrec's five so the two readings
  are checked against each other rather than drifting.
- `REPORTER_VERSION` STAYS `v11 (2026-09-01)` and NO committed report is
  regenerated. Both the suffix and the legend sentence that explains it
  are CONDITIONAL on a record carrying the token, on the same terms as
  every clause since [B18]; no record in `store/` carries it (the value
  did not exist before this pin, and the re-pin census found NO corpus
  pattern that stamps it at all), so every committed report renders byte
  for byte as it stands. The first reports to print either are the ones
  the [B26] window writes.

## The reporter, [B32] (b) (2026-09-02) -- four small rulings, v12

Plan row [B32] (the reporter half; docs/dev/known_issues.md KB-8/KB-9/
KB-10, ledger docs/dev/ledgers/2026-09-02-full-suite-1989c62.md §12 (d),
and one new column for lane b32adp's `scan_edges`/`scan_edges_match`
pair):

- **KB-8's reporter half -- the header's record count is
  QUERY-FILTERED.** `- record source: store/index.tsv (N candidate
  file(s))` used to print `len(paths)` -- the WHOLE store's candidate
  count, computed in `main()` before any filter ran, and the ONLY line
  that moved on 42/48 of the [B26] (c) re-render invariant's reports. It
  now prints `len(selected)` -- every record THIS QUERY's own filters
  admit (`matches_filters`), computed inside `build_report` -- worded
  `(N record(s) matching this query)`. `args._source_desc` now carries
  the bare store LABEL only; `build_report` appends the count.
- **KB-9 -- the compile phase named `gcc` on a `-clang` testee.** The
  RECORD is unchanged (the phase name stays `gcc` on purpose, [B24] --
  it is what makes a clang testee's column comparable to its gcc
  sibling's). `_cc_from_testee_id` reads `config_extra`'s `cc-<name>`
  token (always the FIRST axis when present, testees/pcrec/CLAUDE.md's
  chartering-order rule); the compile-cost table appends `(clang cc)` to
  the `gcc ns` cell of any row whose OWN testee declares a non-gcc `cc`,
  plus one legend note per table that fires.
- **Ledger §12 (d) -- the worst other-core occupancy, unconditionally in
  the header.** A new `ReportData.worst_other_core` field
  (`(pct, testee_id, pattern_id, regime) | None`), computed once over
  every included record's `environment.occupancy.timeline` items while
  `build_report` walks `valid` records -- NOT gated behind
  `--include-provenance` (the ledger's own 91.63% spike sat inside one
  record and in no report). Renders as `- worst other-core busy: N%
  (testee / pattern / regime)` or `n/a` on both markdown and the TSV
  header comment.
- **A `scan_edges`/`scan_edges_match` column.** `_scan_edges_display`
  renders `edges=N` (search-side count) or `edges=N (match: M)` beside
  the existing `edge=` shape clause (KB-6) in `_testee_legend_line`,
  gated on the PAIR's own presence -- independent of `edge=`'s dfa-scan
  scope, since a forced-VM artifact can carry `scan_edges=0` with no DFA
  scan at all. `0` is a real, recorded value (presence gates the clause,
  not truthiness). `_mechanism_stamp_columns` and the TSV's
  `compile_stamp` rows carry the pair too, same shape as every other
  conditional pair since [B18].
- **KB-10 -- `quick --vs` on a refused arm prints `refused`, not an
  error.** `pcrecbench/__main__.py`'s cell-lookup loop is now
  `_split_quick_cells` (module-level, unit-tested in the new
  `pcrecbench/tests/test_quick.py`): a `--vs`-only arm (never the
  primary `--testee` arm) whose only row is a `did-not-compile` compile
  row becomes a `refused (<diagnostic, first line>)` entry instead of
  the old "expected one cell ... found 0" error, `quick` exiting 0 with
  the record's path still printed. An empty cell for any other reason
  still errors, on either arm.
- `REPORTER_VERSION` bumps to `v12 (2026-09-02)`; every committed report
  under `reports/` regenerated from its own recorded query -- see
  `reports/CLAUDE.md` for the diff classification (the count and version
  line move on every file; KB-9's note only on the `cc-1989c62` reports;
  the worst-other-core line is new everywhere; `scan_edges` prints on
  none of them yet -- no committed record carries the pair).
  `pcrecbench/tests/test_report.py` gained 4 tests (KB-8, KB-9, ledger
  12(d), `scan_edges`); `pcrecbench/tests/test_quick.py` is a new file
  (7 tests, KB-10). 73 reporter-side tests total
  (`pcrecbench/tests/CLAUDE.md`).

## The reporter, [B37] (2026-09-05) -- the abi-22 re-pin's half, v14

Plan row [B37], the re-pin to pcrec 334fd10e (abi 22: SIX abi steps in
one pin). Four new stamps in two scopes; the reporter takes THREE legend
clauses, all additive and CONDITIONAL on a record carrying the pair (no
record in `store/` does yet -- nothing under `reports/` is regenerated):

- **`folds=<0..6>`** (`RX_DFA_UNIFORM_FOLDS`, abi 17) on `edge=`/`start=`'s
  `dfa-scan` scope, right after `start=`: how many DFA tables had
  all-equal cells and were NOT EMITTED. `table=premultiplied` beside
  `folds=4` is an artifact with no transition table -- the SIZE fact the
  [B33] (3) witnesses are about. `0` is a real value; presence gates it.
- **`islands=<N>`** (`RX_VM_ALT_ISLANDS`, abi 18) on `frameless=`'s VM
  scope, right after it: how many flat alternations were lowered as an
  alternation island (a trie) instead of vm_alt's resume chain -- the
  mechanism that removes the 2026-09-03 ledger's x8.87/x20.1 branch-ORDER
  effect at the source. A row's `islands=1` beside its
  `pcrec-auto-noisland` sibling's `islands=0` is the pair the AFTER is
  read on. `0` is a real value.
- **`shape=<plain|shared|forward|inline> (prog: N B)`** (`RX_VM_ENTRY_SHAPE`
  + `RX_VM_PROGRAM_BYTES`, abi 22), after `islands=`: the entry-chain rung
  the emitter took, with the program size AUTO compared against
  VM_INLINE_CHAIN_MAX_BYTES (4,096) to choose it -- ONE clause for two
  stamps on `edges=`'s `(match: M)` precedent, because the number is what
  makes the token checkable (four artifacts can read `plain` for four
  reasons). Answer-identical across every value: a cost/size fact.
- Three notes under the legend, each named once under the lines that
  carry the clause; `REPORTER_VERSION` bumps to `v14 (2026-09-05)`;
  `pcrecbench/tests/test_report.py` gained 2 tests (70 + test_quick's 7 =
  77 reporter-side tests). The regeneration belongs with the window that
  first writes an abi-22 record.

## The reporter, [B39] (2026-09-06) -- the abi-23 re-pin's half, v15

Plan row [B39], the re-pin to pcrec d34c9131 (abi 23, [FORM-CHAR] STEP 1),
drafted by lane b39prep from pcrec's source before the build and BUILT
2026-09-06 (inbox I-52; pin.sh d34c9131). One clause, one wording fix,
both conditional; committed reports are regenerated with the AFTER window:

- **`clsfolds=<N>`** (`RX_VM_CLS_FOLDS`, abi 23) on `islands=`/`shape=`'s
  VM scope, right after `shape=`: how many VM class-pool entries take the
  ASCII-FOLD test (`(byte | 0x20) == lower`, no 32-byte bitmap) -- the
  SIZE fact the abi-23 AFTER is about, read on altwide `ci-256`'s
  forced-VM pair (`clsfolds=26` MEASURED beside `pcrec-vm-noclsfold`'s
  `0`). VM route only: an `auto` row that selected the DFA prints no
  clause even on a `(?i)` pattern. `0` is a real value.
- **The `prog: N B` note** carries pcrec I-50 1's reconcile: the VM
  PROGRAM REGION with COMMENTS INCLUDED, against the `code bytes`
  columns' whole-file comment-EXCLUDED count (w-256: 305,686 vs 292,043,
  neither wrong). Prints under any table whose rows carry `shape=`.
- `REPORTER_VERSION` bumps to `v15 (2026-09-06)`;
  `pcrecbench/tests/test_report.py` gained 1 test (71 + test_quick's 7).
