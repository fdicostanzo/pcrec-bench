# pcrecbench/ — the harness package

`python3 -m pcrecbench run --subbench email --testee pcre2-jit` measures one
CELL and writes one RECORD. The spec is `docs/design/harness_contract.md`;
the record's shape is `docs/design/record_schema.md`.

| file | role |
|---|---|
| `__main__.py` | the CLI: `run` (`--tier pinned\|scratch`), `quick` (the edit-test loop's one-cell surface, [B10]), `index`, `quiet`, `testees`, `report`, `interpret` |
| `interpret.py` | THE INTERPRETER ([B13], `docs/design/interpreter_v1.md` v1.4, `INTERPRET_VERSION` **v2**): a deterministic fact-finder over a committed report **TSV** and `store/index.tsv` — never the markdown, never a record, never an engine. Emits the FIRED catalogue rules with their rows, numbers and record ids, and the rules that did NOT fire with the reason each did not. The rules live in `catalogue/rules.toml` (**3.0**, [B56] the predicate-audit fix wave), which this module is checked against by `make check-interpret`; this file holds the header's known-key split (§2.1, normative), the raising VIEW every rule function is handed (§3.2.2), the 32 rule functions (R-ARM-2, [B56]/F9: an arm pair one config token apart, one of which refused to compile — the strongest possible arm difference R-ARM-1 cannot see), §5.2's counted collapse, the predictions reader and evaluator (§6, since [B47] §6.7: a SEVENTH selector key `grain=subject` routes a clause to `--subject-grain PATH`'s `ReportTsv` instead of the primary report; `_select`'s default section for `n_wrong`/`n_gave_up`/`pass_rate`/`status` widens to `rank` UNION `excluded` — ruling (α) — and `_elsewhere` also annotates an EVALUATED clause with what it finds outside that default read — ruling (β); since [B56]: `_keyed_values` collapses the six duplicate `rank` metric rows to ONE per cell for those four quantities before any reducer runs, Q4, and `load_predictions` refuses the `median` reducer on one of them, F13; `r_delta_4`'s coverage reads a prediction's own selector glob against a firing cell, F3; `check_stated_utc` takes a `report` argument and anchors to the OD-B15 dedup key of the report's own included population rather than the whole store's history, F27 — `_anchor_identity_lines` renders the anchor used, unconditionally, on every predictions-scoring run), a rule function's did-not-fire return may be `(token, reason)` where `reason` is one of the rule's own declared `no_fire_reasons` ([B56]/F1-F2, `_normalize_not_fired`), `build_stamp`'s now-unconditional `subject_grain`/`subject_grain_sha256` stamp lines, and the renderer whose only sentence-production surface is one `str.format` per rule template (§7.1) |
| `harness.py` | contract §4's seven steps; `outcome_for()` is the ONE place an engine's answer becomes a `match_outcome` (since [B42] L5: an optional `convention` parameter, R5 B1/CB1 — a no-op on every real corpus row, see `capability.py`'s docstring; since lane `b44boolgrain`, schema v1.6: an optional `grain` parameter, default `"full"` — `run_cell` reads `testee_block.get("grain", "full")`, the same declaration seam `conventions` already has — at `grain="boolean"` a matching row is never scored against a span it cannot know, and the private `_observed_span()` helper never builds a schema-illegal `[None, None]` array); `run_cell(tier=, patterns=, subject_limit=, budget=)` is what `quick` parameterises — no second code path; since [B42] L5 also runs `capability.missing_capabilities()` before `adapter.compile()` for every pattern, producing an `unsupported-by-declaration` compile row (with `declaration_ref`) in place of a real compile attempt where it fires; [B77] U1: `run_cell` sets a measured pattern's `handle["utf8_advance"]` iff `expectations.utf8_advance(sb, p)` (only when true — a byte set's handle and every adapter argv are unchanged); every adapter turns it into the driver protocol's `--utf8` |
| `capability.py` | [B42] L5 (lane b42cap, 2026-09-16): THE PRE-COMPILE CAPABILITY POLICY (`docs/design/capability_set_v1.md` 5.3) — `REQUIRES(pattern) ⊄ capabilities(testee) ⇒ unsupported-by-declaration`, decided in `harness.run_cell` before `adapter.compile()` is called. `REQUIRES_VOCAB` (17 tokens, 5.1 + 6.2's `true-end-anchor`) is the closed vocabulary; `pattern_requires()` reads `Pattern.tags`' `requires-*` entries against it; `capabilities_for()`/`missing_capabilities()` read a set's `.rxt` `ext bench` aux block via TWO paths — `sb.rxt.aux_rows` when the loader already has it, or `rxt_source.load_aux_rows()` (the sidecar/shim path — was `bench/capability`'s real path until the O-29 fix pin a770139e + the [B42] sidecar switch made that set whole-file loadable, `sb.rxt.aux_rows`; still the path for any future non-`.rxt` set carrying an `ext bench` block) otherwise — cached per `sb.root`. Fail-closed throughout: a testee/token absent from the matrix satisfies nothing; [B77] U1: `REQUIRES_VOCAB` is 20 tokens — `utf8-encoding`, `ascii-class-scope`, `unicode-class-scope` added (`utf8_set_v1.md` 7.5, Q3 ruled GLOBAL by I-94); `unicode-class-scope` is also the token the oracle word reads |
| `subbench.py` | loads `bench/<name>/`; owns the regime→subject mapping and `subbench.content_hash`; `_load_manifest` is GENERIC on a subject manifest's column count (4, the original shape, or 5 with `periodic` appended, [B17]) — no column position is hard-coded beyond "periodic, if present, is last". `bench/loglines`' manifests use the same column, in the same place ([B11.1]). Since KB-12 ([B36]'s incident): `Subbench.__init__` checks EVERY pattern and subject id (short and throughput) against the record schema's own `$defs/slug` rule (`check_id`, `_slug_pattern` — the regex is READ from `schema/record.schema.json`, never retyped) and raises `SubbenchError` naming the offending id, the set and the rule, so `run`/`quick` refuse in under a second instead of after every trial of a cell has already run (bench/syntax@0.1's incident: six cells, 259 minutes, 0 records written, all refused at `store.write()`'s validator). Since [B42] L4 (lane b42load): a sidecar's `rxt_source = "<relative path>"` is the ONE-LINE switch that loads `[[patterns]]` from an `.rxt` file (`rxt_source.py`) instead of the TOML array — present, `[[patterns]]` is ignored outright, so a set does not need its stale array deleted to switch. `Pattern.file` is now OPTIONAL: a pattern carries EITHER `file` (the original per-pattern-`.rx`-file shape) OR inline `text` (an `.rxt` block's own decoded bytes), never neither — `pattern_bytes()` reads whichever is present, opening nothing for an `.rxt`-sourced pattern. Since [B42] L5: `Expectation` gains a `.convention` slot (R5 B1/CB1), always `None` from the real 9-column `expectations.tsv` loader — set only by a future `under <convention>`-qualified row's own loader, which does not exist yet; [B77] U1: `sb.encoding` from the sidecar's `[expectations] encoding` (`byte` default, or `utf8`; anything else refused BY NAME — `SET_ENCODINGS`) |
| `rxt_source.py` | [B42] L4 (lane b42load): THE `.rxt` PATTERN-SOURCE LOADER — the ONE sanctioned reader of pcrec's `.rxt` format on this side (`pcrec --list-source`, docs/spec/rxt_format.md at pin a770139e/abi 25 (cd371441 + the O-29 close-frame fix); no second `.rxt` parser — D2 of `docs/design/rxt_needs_v1.md` 3's acceptance checklist). `resolve_pcrec_bin()` delegates to the SAME pin resolution `export_rxt.py --verify`'s default already uses (`adapters.discover()["pcrec"].pin_binary(build=False)`) — never builds; a missing pin is `RxtSourceError` BY NAME. `parse_list_source()` reads the dump's own `#kind`/`#line`/`#section` structure column-NAME-driven (never a hard-coded column index); `_decode_dump_field` is its OWN escape decoder (NOT `export_rxt.decode_rxt_escape` — that one's plain `.encode("utf-8")` fallback corrupts a RAW, unescaped high byte a plain `pattern` block's column carries verbatim, MEASURED this lane; `errors="surrogateescape"` on both the subprocess decode and the re-encode is the lossless fix). `load_rxt_source()` is the entry point: it runs two gates before returning anything — `check_no_build_directives` (a pattern-SOURCE `.rxt` file declares no `target`/`config` row, ever; an `ext` block's rows live only in `#section aux` and never trip it) and `check_block_sidecar_agreement` (every pattern block appears exactly once in what the loader hands the harness, ids matched by the block's own `name`). `RxtSource` exposes `patterns` (in file order), `provenance`/`variants`/`cases` indexed by `block_line`, `aux_rows` (the `ext` tree, verbatim — interpreted by nothing here, a future L5's own reading), and `head` (file-level description/oracle/vocabulary/tag). **KNOWN GAP (outbox O-29), found by this lane and FIXED UPSTREAM at pin a770139e (2026-09-16, inbox I-71 — see the lane report `docs/dev/lanes/b42load_report.md` and docs/dev/measurements/2026-09-16-o29-verify-a770139e.txt):** at pin cd371441, `--list-source` silently dropped the `#section provenance`/`variants` rows for every pattern block whose sub-block was closed by a blank/comment line (no diagnostic, exit 0; the flat `m`/`n`/`mc` case rows unaffected) — reproduced on a 3-pattern synthetic fixture and on the real 64-pattern `bench/capability` corpus. This module reads the dump FAITHFULLY either way; at the fix pin the corpus dumps 64/64 and `bench/capability` loads whole-file (the sidecar switch). Since [B42] L5: `load_aux_rows()` is a NARROWER entry point — the `#section aux` tree and head facts only, skipping the two per-pattern-content gates (`check_block_sidecar_agreement`, `check_provenance_agreement`) that make `bench/capability` un-loadable AS A WHOLE at this pin — for a caller (`capability.py`) that wants only the `ext` tree |
| `adapters.py` | the `Adapter` interface, discovery, and **the DRIVER PROTOCOL** (in full, at the top of the file) |
| `driverrun.py` | build/run/parse a driver; the resume-after-driver-death rule |
| `record.py` | builds the record dict; every derived id comes FROM `schema/validate.py`'s own functions |
| `capture_class.py` | [B82] (2026-09-23, inbox I-99/I-100/I-101): THE CAPTURE-CLASS DECLARATION TABLE `report.py` reads to render the two class-pure ranking views and the standing cross-class query -- `classify_testee(testee_id)` returns `yes`/`no`/`undeclared` from a table keyed on the pin-independent `(engine_name, engine_mode, caps_token)` identity every testee_id already encodes, never the id verbatim (a re-pin never goes stale) and never a schema/harness/adapter change. FROZEN by I-100: every real config's own `-caps-`/`-nocaps-` token is trusted as the run fact EXCEPT `rust-default` (`is_override` true), whose config declares `captures=on` but whose timed loop makes exactly one verification `captures_at` call -- declared here as a fixed per-call cost, citing `src/main.rs:255-266`. An id this table has no row for is `undeclared`, NEVER guessed (I-99's fail-loud rule) |
| `nullband.py` | [B79] THE NULL-CONTROL BAND's arithmetic (`docs/design/null_band_v1.md`): `scale_bin` (`>=1us`/`100ns-1us`/`<100ns`), `type7_quantile`/`iqr`, `delta_pct`, `Stratum` (the symmetric worst-null-cell half-width, `ok`/`insufficient`/`empty` against `N_MIN = 10`), `build_strata`, `d119_verdict` (|Δ%| > max(IQR%, band), `(IQR only: band n=K < 10)` when the stratum is unusable). Pure; `report.py` gathers the cells and renders |
| `reduce.py` | the SET-GRAIN reduction `quick` prints and the reporter ranks (R5, [B10]): `reduce_set_cell`, `reduce_match_cell`, `cells_from_record`, `giveup_code`; pinned by a hand-computed fixture in `tools/selfcheck.py`. Since [B20] also THE ONE derivation of the v1.4 `trial_agreement` block (`judge_trial_agreement`, gate_shape_v14.md §3.5) and its shared rendering (`agreement_line`) — the harness stamps with it, `quick` prints it, the reporter renders it, and `schema/validate.py` carries a deliberate SECOND implementation X32 compares it against. Since KB-27 (2026-09-22, docs/dev/known_issues.md): `MatchCell`/`SetCell` also carry `n_no_expectation`, subtracted back out of `n_wrong` — a `did-not-match-as-expected` row caused by NO expectation existing at all (`harness.outcome_for()`'s `expectation is None` branch; an oracle give-up dropped at derivation, or nobody has authored one yet) is identified by that branch's OWN fixed diagnostic text (`NO_EXPECTATION_DIAGNOSTIC_PREFIX`, `_is_no_expectation_row`) rather than counted as a wrong answer |
| `store.py` | the store path rule, never-clobber, validate-before-write, the index; the TIERS: `.canonical` marks the canonical store, which refuses a `tier: scratch` record on write and on index; `scratch_store()` is `$PCRECBENCH_SCRATCH_STORE` or `build/scratch-store/` |
| `quiet.py` | the quiet-box instrument and its two thresholds (`docs/design/quiet_baseline.md`) — since BD7 (2026-08-30) the occupancy sample is `mpstat -P ALL 1 5` judged on its `Average:` block (`judge_mpstat`, pure; `split_mpstat`); `OCCUPANCY_SECONDS`. Since [B20] (schema v1.4) `judge_mpstat` also writes the TARGET core's tri-state `target_busy_pct`, `gate()` is the whole PRE-FLIGHT (load1, the non-target average, the target's own reading, the missing-row refusal — the `quiet` CLI judges through it too), `preflight_ok`/`after_notes` replace `occupancy_ok` (the after samples are PROVENANCE), and `cpu_times`/`timeline_item` read the per-group `/proc/stat` timeline |
| `env.py` | the `environment` block; the machine registry |
| `oracle_pcre2.py` | the libpcre2 ctypes binding, copied from pcrec (see its header) and extended: anchoring bits, `find_all`, an explicit give-up surface, and `pattern_info()` ([B11.1] — PCRE2's own first/REQUIRED code unit and min length, the analysis `bench/loglines` is built around); [B77] U1 (`docs/design/utf8_set_v1.md` 8, 14 Q9): the per-pattern ORACLE OPTION WORD as a parameter of this one shared module (`option_word(utf=, ucp=)`, `PCRE2_UTF`/`PCRE2_UCP`, a `Compiled` keeps `.options`) and the CHARACTER-BOUNDARY find-all advance `next_start()` (pcrec match_api.md S3.1.1's normative utf8 rule), active ONLY when the word carries `PCRE2_UTF`; `PCRE2_NO_UTF_CHECK` is never passed. With the word 0 every set re-derives byte-identically (`docs/dev/measurements/2026-09-25-b77u1-byte-identical-rederivation.txt`) |
| `periodic.py` | the `periodic` manifest column's DEFINITION (inbox I-10, [B17]): `smallest_period` / `periodic_field`, the smallest exact repeat period in [1, 4096] bytes or `no`. Moved here from `bench/email/` when `bench/loglines` became its second caller ([B11.1]) — the column means the same thing in every manifest because one function computes it |
| `expectations.py` | the GENERIC expectation chain every `bench/<name>/gen_expectations.py` runs: one row per (pattern × subject × declared regime) from the libpcre2 oracle, `--check` mode, the no-capture-participated assertion, and the rule that an oracle give-up is DROPPED and listed rather than recorded as `nomatch`. Lifted out of `bench/email/gen_expectations.py` when the second sub-bench arrived; two copies would be two chances for two sets' expectations to be derived by different rules; [B77] U1: `oracle_option_word(sb, pattern)` — `PCRE2_UTF` iff the set declares `[expectations] encoding = "utf8"`, `PCRE2_UCP` iff the pattern declares `requires-unicode-class-scope` — and `utf8_advance()`, the ONE fact the harness forwards to every driver (`handle["utf8_advance"]` → `--utf8`), so the oracle and the drivers step alike |

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

## The reporter, [B13.2] (2026-09-08) -- the two interpreter preconditions, v16

Lane `b13pre`. `docs/design/interpreter_v1.md` 2.5's two PRECONDITIONS
the [B13] interpreter design depends on -- neither rule the interpreter
carries (R-FLOOR-2, R-STATUS-12) is implementable without them. TSV-only:
neither touches `render_markdown` at all.

- **P-1 -- `floor_pattern: <pattern_id|none>`**, the LAST key of
  `render_tsv`'s header comment (after `worst_other_core_busy`, so no
  existing key's position moves). Derived from `ReportData.
  floor_pattern_by_sb` ([B14] R9) -- the DISTINCT set of its values:
  zero -> `none`; one -> that id; more than one (no committed report
  hits this) -> the sorted ids joined with `,`. `_floor_pattern_header_
  value(rd)` is the one function both `render_tsv` and its test call.
- **P-2 -- the give-up smallest subject as its own metric rows.** Beside
  each `excluded` row with at least one give-up, one extra `excluded`
  row per DISTINCT give-up code, immediately after the base row, same
  sorted-code order `_gave_up_cell_summary` already renders (both now
  read a shared pure helper, `_gave_up_cell_detail`, so the human string
  and the TSV rows can never disagree about which subject is smallest).
  18 columns: `subject_or_na` = that code's smallest subject id,
  `metric=giveup_smallest`, `value`=the code, `n`=its byte count (`""`
  when unknown), `n_gave_up`=the SUBJECT count for that code (not
  `r.n_gave_up`'s trial count -- a deliberately different number under
  the same column name, read per emitted row), every other column
  empty. `excluded` section only (R-STATUS-12's own input); set grain
  only, via the SAME `hasattr(r, "failing_detail")` gate the base row's
  `gave_up_summary` already uses (a `MatchCellReduction`, subject
  grain's row type, carries no such field) -- no separate branch needed.
- **CWD-independent provenance paths.** `render_markdown`'s two
  per-record-listing `os.path.relpath(path)` sites now read
  `os.path.relpath(path, rd.store_parent)` (a new `ReportData.
  store_parent = os.path.dirname(os.path.abspath(args.store))`, the
  STORE directory's own PARENT, never `os.getcwd()`) -- found
  regenerating `reports/`: ten 2026-09-05 files rendered `../../store/
  records/...` where every other file reads `store/records/...` for the
  identical query, purely from a different CLI cwd. Ten committed files'
  provenance lines normalize to `store/records/...` on regeneration;
  `fixtures/golden/store_v8.md`'s three lines are corrected in place.
- `REPORTER_VERSION` bumps to `v16 (2026-09-08)`; every committed report
  under `reports/` regenerated -- see `reports/CLAUDE.md`.
  `pcrecbench/tests/test_report.py` gained 4 tests (75 + test_quick's
  7 = 82).


## The interpreter, [B13.3] (2026-09-09) — `interpret.py`, catalogue 1.0

Lane `b13impl`. Part 1 of `docs/design/interpreter_v1.md` v1.2: the
deterministic fact-finder, the versioned rule catalogue, the facts TSV
and the rendered sidecar, the predictions input, the opinion firewall as
code, and `make check-interpret`. Four things a reader of this package
must know:

- **It reads the TSV and the index, and nothing else.** No markdown, no
  `bench/*/subbench.toml` (that read was v1's KB-2 mistake; the floor
  pattern now comes from reporter v16's own `floor_pattern:` header
  key), no record JSONL, no engine. The reporter already made the
  reduction; a second one here would be a second implementation of
  arithmetic this project keeps in exactly one place.
- **It can never disagree with the report about whether something
  moved.** Every R-DELTA rule reads `_cross_pin_verdict`'s own verdict
  STRING rather than re-deriving the comparison. `delta_verdict` is a
  `; `-separated CLAUSE LIST, so R-DELTA-2 and R-DELTA-3 co-fire on the
  compound `selection changed (vm → dfa); now measured (was: gave-up)`
  and R-DELTA-1 and R-DELTA-2 never co-fire on one cell.
- **A rule function cannot touch a column it did not declare.**
  `RuleView` raises `UndeclaredColumn`, which is a check over the paths
  the fixtures and goldens exercise — a good check, not a proof, and the
  design note says so.
- **The sidecar is a function of the facts TSV.** The render reads
  numbers back out of the rendered slot STRINGS (`slot_number`), so
  §8(5)'s no-prose check can re-render the whole document from the facts
  alone and require byte equality — every line is a template, a link, a
  heading, a did-not-fire row or the stamp.

`REPORTER_VERSION` is untouched: the interpreter reads the reporter, it
does not change it. The `interpret` subcommand is dispatched before
argparse in `__main__.py`, the same way `report` is, so it owns its own
flags.

## The reporter, KB-18 (2026-09-17) -- a did-not-compile diagnostic is FULL, never truncated, v17

Lanes `b42repdiag` (the fix) and `b42repfin` (the regen wave and this
entry). `docs/dev/known_issues.md` KB-18, found on bench/capability@0.1's
first sample: `wild-waf-crs-942500-comment-obfuscation`'s did-not-compile
diagnostic (a genuine pcrec DFA-emitter bug -- an unescaped `*/` in a
generated comment desynchronizes the rest of the C compile, cascading
into two more errors) had to be read out of the raw JSONL record because
`_diagnostic_first_line` (since [B12] R10) kept only the first line and
printed `[truncated, diagnostic continues]` in its place
(docs/dev/ledgers/2026-09-17-capability-0.1-first-a770139e.md, Finding F).

- **`_diagnostic_full` replaces `_diagnostic_first_line`.** A
  did-not-compile row's `diagnostic` is carried VERBATIM and IN FULL,
  bounded only by `record.FREE_TEXT_MAX` (1,048,576 chars, schema v1.5's
  hygiene bound, [B30]) as a defensive ceiling -- the schema itself caps
  a compile row's `diagnostic` at 8192 chars today, well under it. Both
  call sites (the markdown `not ranked: ... did-not-compile (<diagnostic>)`
  bullet, the TSV `did_not_compile` row) are ONE-PHYSICAL-LINE contexts,
  so an embedded newline/tab/backslash is rendered VISIBLY (backslash
  escaped FIRST, then `\n`/`\t`) rather than executed -- nothing is
  dropped, and the mapping is losslessly reversible: a diagnostic that
  happens to already contain the literal two characters `\n` renders
  distinguishably from one with a real embedded newline. This means
  EVERY literal backslash in a diagnostic is doubled, not only ones
  adjacent to a real control character -- a deliberate, necessary part
  of the reversibility guarantee, not an oversight; see the finding
  below for where it fires on ordinary single-line text.
  `pcrecbench/__main__.py`'s OWN, SEPARATE `_diagnostic_first_line`
  (KB-10's `quick --vs` refused-arm one-liner, genuinely one-line-by-
  design) is UNCHANGED.
- `REPORTER_VERSION` bumps to `v17 (2026-09-17)`;
  `pcrecbench/tests/test_report.py` gained `test_diagnostic_full_kb18`
  (a multi-line diagnostic escapes visibly and survives whole; a
  single-line one is unchanged when it carries no backslash; `None`/empty
  render `(no diagnostic)`; a literal two-character `\n` in the SOURCE
  renders distinguishably from a real embedded newline). Standalone run
  (`python3 -m pcrecbench.tests.test_report`, pre-regen): 78 passed, 0
  failed.
- **The regen wave (lane b42repfin) touched TWO groups beyond the
  version-line stamp, both EXPLAINED, neither a bug.** All 43 committed
  report groups (129 files) were re-rendered from each file's OWN
  committed query and diffed against the last commit; 41 groups are
  byte-identical but for the `reporter: v16` -> `v17` line.
  `2026-09-17-capability-0.1-*-first-a770139e.*` moves exactly as KB-18
  intended (5/5/157 changed lines in tsv/md/subject-grain: the four
  `wild-waf-crs-942500-comment-obfuscation` did-not-compile rows now
  carry the full gcc transcript). `2026-09-07-syntax-0.1-*-first-
  d34c9131.*` ALSO moves (85/85/2437 changed lines) -- diagnosed and
  CONFIRMED NOT store drift (the query already carries an explicit
  `--since`/`--until` pair; both renders match the same 6 records, 0
  superseded, 0 excluded) but the SAME escaping rule firing on seven
  bench/syntax patterns whose pcrec diagnostics quote a literal
  backslash-letter escape sequence with no embedded control character at
  all -- `esc-ctrl` (`\c`), `esc-octal-o` (`\o`), `msc-c-uc` (`\C`),
  `msc-r-uc` (`\R`), `msc-x-uc` (`\x`), `unp-p-lc`/`unp-p-uc` (`\p{...}`)
  -- each rendering e.g. `\c` as `\\c` for the same lossless-reversibility
  reason stated above. Neither the lane's own one-record manual proof nor
  the disposable `regen_reports.py` scratch script's diff classifier
  (which only recognised the OLD truncation marker as an expected class)
  anticipated this population; `git diff` against the last commit is
  what confirms both groups' deltas are fully accounted for by these two
  causes and nothing else. The four committed `reports/*.interpretation.md`
  sidecars were also regenerated (`scripts/regen_sidecars.py`, 0
  failures, all determinism-checked) -- the capability sidecar's own
  finding line now shows the full gcc transcript in place of the old
  truncation marker, proving the fix reaches the interpreter path too.

## The reporter, [B47] (2026-09-17) -- the subject-grain SLICE

Lane `b47subgrain`, implementing `docs/design/interpret_subject_grain_v1.md`
§6's eleven ratified rulings (folded into `docs/design/interpreter_v1.md`
v1.4 §6.7 as the design of record). `REPORTER_VERSION` UNCHANGED (`v17`):
this is a NEW, additive rendering path, never a change to what `--grain
set` or `--grain subject` already emit -- every existing committed report
renders byte-identical.

- **`render_tsv_subject_grain_slice(rd)`** is a pure ROW FILTER over
  `render_tsv`'s own `--grain subject` output: keeps every `record` row
  and every `rank` row's `median_ns` metric (dropping the five others --
  `min_ns`/`max_ns`/`stddev_ns`/`ratio_vs_baseline`/`ratio_vs_best`),
  keeps `excluded`/`not_ranked`/`scratch`/`did_not_compile` WHOLE, and
  drops `compile`/`compile_stamp` outright (grain-independent, already in
  the set-grain file). Same header, same 18 columns -- `pcrecbench.
  interpret.ReportTsv` reads it unchanged.
- **`--subject-grain-slice`** (requires `--grain subject --format tsv`,
  refused BY NAME otherwise): the CLI surface. MEASURED on its first real
  use (email-specimen@0.1's repin-692c2e8 query): 17,836 full
  subject-grain lines -> a 2,981-line slice (16.7%), matching the design
  note's corpus-scale ×4.8-vs-set-grain estimate.
- The committed artifact this produces is `<name>.subject-grain.tsv`
  (`reports/CLAUDE.md`'s own section): `interpret`'s SECOND input,
  `--subject-grain`, consulted by R-BUCKET-DOMINATED and by a prediction
  clause naming `grain=subject` (catalogue 2.0, `interpret.py`'s
  `_select`/`evaluate_predictions`). Exactly one group carries one today
  (§6 Q9: no back-fill) -- see `reports/CLAUDE.md`.

## The reporter, [B52] (2026-09-18) -- THE MATRIX REPORT SURFACE, v18

Lane `b52matrix`. Frank's ruling, live at the twenty-fifth session close
(docs/dev/dev_journal.md): the tests-x-engines ratio matrix a manager
session had been building ad hoc (from two committed report TSVs plus
the raw compile outcomes) becomes a STANDARD committed reporter surface,
Claude-readable TSV canonical, HTML derived. Four charter items:

1. **`--format matrix`** (requires `--grain set`, refused BY NAME at
   `--grain subject` -- same shape `--subject-grain-slice` already uses
   for the opposite grain), `render_matrix_tsv(rd)`: one row per timing
   cell `(subbench, pattern, regime_or_na, form)`, one column per testee
   in the query's own roster, every data cell EITHER `median_ns /
   this row's best measured median_ns` (six decimals) or one of five
   CLOSED status tokens (`unsup`/`refused`/`wrong`/`gave-up`/`excluded`)
   -- NEVER blank (the NO-EMPTY-CELLS invariant, mechanically checked by
   `test_matrix_no_empty_cells`). `best_testee`/`best_ns` columns recover
   the absolute scale a bare ratio loses. **F26 IMMUNITY, BY
   CONSTRUCTION** (`docs/design/predicate_audit_v1.md` F26): the row
   population (`_matrix_row_keys`) is the UNION of every pattern with a
   real `set_cells` entry and every pattern with a
   `did_not_compile_by_pattern`/`unsupported_by_pattern` entry -- a
   pattern refused or declared unsupported by EVERY testee in the
   roster (no ranking group, and therefore no row, in `render_tsv`'s own
   loop) gets exactly one full row, `regime_or_na=""`/`form=""`, every
   column a status token. `unsupported_by_pattern` is a NEW
   `ReportData` field (built the same way `did_not_compile_by_pattern`
   already is, keyed on `compile_outcome ==
   "unsupported-by-declaration"` instead) -- the fact that dict
   deliberately excludes and that nothing before this lane rendered
   anywhere. Full design and worked examples: `report.py`'s own module
   docstring, `[B52]` section.
2. **The `.matrix.tsv` sibling itself** is produced by running the SAME
   committed query through `--format matrix` -- charter item 1 is the
   CAPABILITY; regenerating the sibling for every existing report group
   is the whole-store regen this lane does NOT do (out of scope by the
   lane's own brief; owed to the window/manager that next holds the
   store, same footing as every prior `REPORTER_VERSION` bump's
   regeneration wave -- see `reports/CLAUDE.md`).
3. **THE BASELINE-IDENTITY FACT** (the O-33 addendum: `ratio_vs_baseline`
   silently fell back to the group's own row-best whenever no testee in
   it is the interp reference, with nothing stating which applied --
   found investigating O-32's ×102-vs-×2.24 mislabel). `_resolve_baseline`
   (shared by `render_markdown` and `render_tsv`, so the two renderings
   can never name two different baselines for one group) returns
   `(baseline_ns, baseline_testee, is_interp)`: the interp row's own
   reading when one is rankable in the group, else the row's own best
   with `is_interp=False`. Rendered as an UNCONDITIONAL bullet on every
   rankable group in `render_markdown` (`- baseline: <testee> (interp,
   present in this group)` / `(row-best fallback -- interp absent from
   this group)`, right under the group's title -- which still states the
   QUERY's own PREDICTED baseline unconditionally; the bullet states what
   this GROUP actually used) and a `baseline` section row in `render_tsv`
   (`metric=baseline_identity`, `value=interp` or `row-best-fallback`,
   the same sentence in `gave_up_summary`'s free-text slot). This is the
   matrix's own baseline column TOO -- `best_ns`/`best_testee` are
   ALREADY always row-best by construction and ALREADY documented as
   such in the matrix header, so the matrix surface was immune to the
   ambiguity by design; only `render_markdown`/`render_tsv`'s
   `ratio_vs_baseline` needed the fix. Tests, BOTH ARMS
   (`test_baseline_identity_interp_present`,
   `test_baseline_identity_row_best_fallback`): the fallback case asserts
   the FASTEST non-interp testee is named, not a slower one and not the
   query's static prediction string.
4. **`scripts/matrix_page.py`** (new, committed, stdlib-only -- see
   `scripts/CLAUDE.md`): renders any `.matrix.tsv` into a self-contained
   interactive HTML page (a sticky table, a log-scale colour ramp 1x-10^7x,
   one fixed chip per status token, a hover tooltip recovering the
   absolute median from `best_ns x ratio`, the provenance comment
   verbatim, light + dark themes). The ad hoc page Frank read at the
   session reset is this script's visual reference, not its input --
   this script takes only a `.matrix.tsv` and writes only HTML, so the
   TSV stays canonical (item 1) and the HTML stays DERIVED, regenerable
   on demand.

`REPORTER_VERSION` bumps to `v18 (2026-09-18)`; every committed report
regenerates on its own version-line stamp alone (item 3's baseline
bullet/row is now UNCONDITIONAL on every rankable group of every
existing report too -- `_V9_ALLOWED_ADDED` gained the `"- baseline: "`
prefix so `test_v13_record_still_renders`'s classifier keeps passing);
the actual regeneration wave is OWED to the window/manager holding the
store, same as every prior version bump (`reports/CLAUDE.md`).
`pcrecbench/tests/test_report.py` gains 6 tests (4 matrix-format, 2
baseline-identity; 84 total, ALL now registered in `TESTS` -- a
predecessor lane's WIP had left the 4 matrix tests defined but not
wired into the plain-runner's list, silently never run; this lane
wired them in and confirmed all pass), plus the new
`pcrecbench/tests/test_matrix_page.py` (8 tests, `scripts/
matrix_page.py`'s parser and renderer, no engine/store). 99
reporter-side tests total across the three files
(`pcrecbench/tests/CLAUDE.md`).

**The regeneration wave RAN 2026-09-18 (lane b53regen)** -- all 45
report groups, the `.matrix.tsv`/`.matrix.html` back-fill, the six
sidecars and the fixture corpus; full detail in `reports/CLAUDE.md`'s
own `[B52]` back-fill paragraph. Two things worth a reader of THIS file
knowing, since neither is about the reporter's rendering rules
themselves: the wave's own classifier (a scratch tool, never part of
this package) hung for ~4 h under `difflib.SequenceMatcher`'s worst case
on one group's multi-million-line diff before being replaced with a
linear one -- a lesson about regen TOOLING, not about `report.py`; and
`scripts/regen_sidecars.py` (KB-22, `docs/dev/known_issues.md`) had been
silently dropping a sidecar's `--subject-grain` input on every
regeneration since [B47] shipped it, invisible until this wave was the
first to run the script against one of the two subject-grain-stamped
sidecars -- fixed in the same lane, `scripts/CLAUDE.md` updated.

(Reporter waves between this entry and the one below -- [B13.2]'s
interpreter preconditions, KB-18's full diagnostic, [B47]'s
subject-grain slice, [B52]'s matrix report surface, KB-27's
no-expectation label and [B82]'s capture-class views -- are documented
in `report.py`'s own module docstring, `reports/CLAUDE.md` and
`pcrecbench/tests/CLAUDE.md`, not backfilled here; this file's own
"## The reporter, [Bn]" sections resume below with the most recent one.)

## The reporter, [B85] (2026-09-23) -- KB-28: subject grain never duplicates (v21)

`docs/dev/known_issues.md` KB-28: [B82]'s three-pass dispatch
(`rank_yes`/`rank_no`/the demoted mixed `rank`), fine at SET grain, drove
two capability AFTER groups' `.subject-grain.tsv` files to 107 MB at
SUBJECT grain -- over the remote's 100 MB push limit, the push rejected,
those two groups held at v19. Fix: at subject grain a mixed roster gets
ONE ranking pass (never three), with a `capture class` column
(`pcrecbench.capture_class.classify_testee(t).bucket`) on the single
table instead of a filtered roster; SET grain is completely untouched
(proven byte-identical, modulo the version line, against a real
committed render -- `reports/2026-09-22-capability-0.1-budu-ryzen1600-
wrapfix-25b1984f.md`/`.tsv`, regenerated from its own committed query
and diffed). `render_tsv`'s header carries the new `capture_class`
column ONLY when a mixed roster is rendered at subject grain (every
other case's header is the unchanged 18 columns); every row in the
function goes through one `_emit_row(cols, class_val="")` helper so the
column count always matches. The standing cross-class query (I-101) is
UNCHANGED -- it was never one of the tripled sections. A new
`_warn_if_large` prints a stderr WARNING (never a failure) when a
rendered report exceeds 50 MB, called on every format `main()` renders.
`REPORTER_VERSION` bumps to `v21 (2026-09-23)`; regeneration of the two
held capability AFTER groups (and the wrapfix group's own
`.subject-grain.*` siblings) is OWED to the manager at merge. Full
detail, including the exact `diff` proof and every call site touched,
is in `report.py`'s own `[B85]` module-docstring section and
`docs/dev/lanes/b85kb28_report.md`.
## The reporter, [B79] (2026-09-25) -- THE NULL-CONTROL BAND (v22)

Lane `b79nullband`; inbox I-93 block B, I-104 (the banded spec), [B82]
(ii); the design of record is `docs/design/null_band_v1.md`. On every
CROSS-PIN report (R8's own pairs, `_previous_pin_testee`, extracted from
`_cross_pin_info` so the band and the `Δ vs previous version` column pair
the same testees), at SET grain:

- a `## Null-control band` section after the Query section: per pair,
  the identity census (`reports/identity/...`, written by
  `tools/program_identity.py` -- the records carry no program hash) and
  the strata table (regime x baseline scale of the BEFORE median; n,
  min/median/max Δ%, the symmetric band = the worst null cell, and
  `ok` / `insufficient (n=K < 10)` / `empty (n=0)` by name);
- a `D119 bar` column beside `Δ vs previous version`
  (`+80.83% vs bar 8.77% (band) → regress`; `(null control: program
  identical)` on the band's own population; `(IQR only: band n=K < 10)`
  where the stratum is unusable) and a per-view restatement line with
  each class-pure view's OWN counts;
- TSV: a conditional last header key `null_band:`, `null_band` /
  `d119` / `d119_view` rows;
- the I-101 query's clearance column COMPUTED (`_query_clearance`) --
  on every report, cross-pin or not ([B82]'s "not held" claim was wrong
  for set cells: `SetCell.sums` carries the per-trial sums).

A report with no cross-pin pair renders nothing else new; a pair with no
census says `NO NULL BAND` naming the path (never a silent IQR-only
fallback). `pcrecbench/tests/test_report.py` gained three tests (a
hand-computed fixture with ok/insufficient/empty strata and all five
verdict shapes; the no-census and single-pin controls): 96 total.

## The reporter, [B87] (2026-09-25) -- I-101 pairs pcrec same-pin only (v23)

Lane `b87query`; the manager's ruling on the OWED item [B79] left open
(`docs/dev/lanes/b79nullband_report.md` 0 finding 5): `_cross_class_
query_hits` was pairing ANY YES-class row with ANY pcrec `auto-nocaps`
row present in a ranking group, with no regard for pin -- on a cross-pin
report most of the reported "hits" were an OLD pin's caps config beaten
by (or beating) a DIFFERENT pin's nocaps config, a PIN DELTA (R8's/
[B79]'s own territory), never a class anomaly. Fix, `_query_pin_pair_
ok(nc_t, y_t)`: a pcrec YES-class `y_t` is paired against `nc_t` ONLY
when both share the same `version_slug`; a NON-pcrec competitor carries
no pcrec pin and is unchanged -- still compared against EVERY pcrec
`auto-nocaps` row present in the group, each pin producing its own hit
labelled by that hit's own `nc_t` (whose id already names the pin, so no
new column was needed). `REPORTER_VERSION` bumps to `v23 (2026-09-25)`;
regenerated in the same lane: the three 2026-09-23 capability AFTER
groups (`after-8d716693`, `after-b1885a83`, `after-6ef76820` -- the only
cross-pin reports in `reports/` at the time), their sidecars, and the
`R-STATUS-15__*` fixture pair (`catalogue/fixtures/fixtures.toml`,
derived from `report_e` = `after-b1885a83`, whose own `codegrammar-flat`
hit count drops from two to one -- the surviving row is the same-pin
one). `R-STATUS-15` and `R-DELTA-5` need NO catalogue change: both read
the reporter's own rows verbatim, with no pairing logic of their own to
fix (catalogue stays at 3.7). See `docs/dev/lanes/b87query_report.md`
for the full checklist and the before/after hit counts per group.
