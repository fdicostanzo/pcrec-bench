# schema/examples/bad/ — records that MUST be rejected

The positive controls. pcrec's own history is the argument for them:
every check this project's sibling has written and later found broken
was broken in the direction of PASSING, and a check with no failing case
proves nothing about the rule it claims to enforce.

Each file is a good example with exactly ONE thing wrong, and its
content hash restamped so the sabotage is the only defect — a control
that fails for two reasons is not a control. (`x6-tampered-hash` is the
deliberate exception: not restamping IS its sabotage.) All but one are
built from the pcrec example; `x16-lazy-jit-no-warmup` is built from the
v8 one, because the rule it controls only exists for a `lazy-jit`
testee and the pcrec example is `compiled-aot`. Where a rule could be
sabotaged on several rows, the row is chosen to keep OTHER rules out of
it — `x7` sabotages the untimed `wrong-span-or-captures` row precisely
so X11 does not fire alongside.

**The file name names the rule.** The leading token before the first `-`
is the rule id `make check-schema` requires to fire: `x11-...` must fire
X11, `schema-...` must fire a JSON Schema violation. A file that is
rejected for some OTHER reason fails the build. The rules are defined in
`../../../docs/design/record_schema.md` §9.

## Files

| file | rule | the sabotage |
|---|---|---|
| `schema-gave-up-without-diagnostic.jsonl` | SCHEMA | a `gave-up` row with no `diagnostic` — a refusal that does not say which budget was exhausted, which is indistinguishable from a wrong answer |
| `schema-index-map-missing.jsonl` | SCHEMA | `capture_correspondence.mode: by-index-map` with no `index_map` — the mode NAMES a map |
| `schema-iterations-zero.jsonl` | SCHEMA | `timing.iterations: 0` — the reporter's per-call cost is `elapsed_ns / iterations` |
| `schema-missing-calibration.jsonl` | SCHEMA | a timed match row with `iterations` in the hundreds of thousands and no `calibration` object saying who chose that number |
| `schema-missing-clock-source.jsonl` | SCHEMA | `run.clock_source` deleted — nanoseconds from an unnamed clock |
| `schema-missing-compile-cost.jsonl` | SCHEMA | an AOT compile row reporting `compiled` and carrying no `cost` — the compile axis silently empty for that pattern |
| `schema-missing-driver-build-flags.jsonl` | SCHEMA | `run.driver_build_flags` deleted — the engine's build is pinned and the timing driver's is not |
| `schema-missing-required-field.jsonl` | SCHEMA | `environment.machine_id` deleted |
| `schema-missing-subject-sha256.jsonl` | SCHEMA | a subject roster entry with no `sha256`: the bytes that produced the numbers are unidentified |
| `schema-missing-truncation-check.jsonl` | SCHEMA | a `large-subject-throughput` row with no `truncation_check`, so requirements §4.4's "marked `unverified-for-truncation`" marks nothing |
| `schema-negative-elapsed-ns.jsonl` | SCHEMA | a negative `elapsed_ns` — a clock that ran backwards, or a subtraction done in the wrong order |
| `schema-occupancy-verdict-without-number.jsonl` | SCHEMA | `occupancy.before.verdict: pass` beside `max_busy_pct: null` — a judgement with nothing behind it |
| `schema-quiet-attestation-present.jsonl` | SCHEMA | the DROPPED `quiet_attestation` field, still present. `additionalProperties: false` is what makes a removal stick, and this is the control that proves it does |
| `schema-single-role-many-subjects.jsonl` | SCHEMA | a `role: single` subject claiming `n_subjects: 4`, which makes the reporter's per-subject arithmetic wrong by 4× |
| `schema-wrong-enum.jsonl` | SCHEMA | `execution_model` spelled `compiled-AOT` — the un-normalized spelling, which is the mistake an author actually makes |
| `x1-mixed-schema-versions.jsonl` | X1 | two records concatenated into one file, the second at schema version 2.0 |
| `x2-reserved-row-kind.jsonl` | X2 | a `match-list` row — the name reserved for OD-B3's list-valued scan regime, which has no shape yet |
| `x2-unknown-row-kind.jsonl` | X2 | a row with `kind: "timing"` |
| `x3-record-id-mismatch.jsonl` | X3 | `record_id`'s stamp no longer matches `run.timestamp` |
| `x4-filename-mismatch.jsonl` | X4 | a perfectly valid record under a name that is not its record id |
| `x5-testee-id-mismatch.jsonl` | X5 | `engine_mode` changed to `dfa` while the id still says `vm-caps-simdna` — the id claiming a configuration the record does not carry, which is the exact thing deriving the id was for |
| `x6-tampered-hash.jsonl` | X6 | one `elapsed_ns` edited after the fact, hash NOT restamped |
| `x7-unknown-pattern-id.jsonl` | X7 | a match row keyed on `p-nonexistent`. The `wrong-span-or-captures` row is the one sabotaged because it carries no `timing`, which keeps X11 out of it |
| `x7-unknown-subject-id.jsonl` | X7 | the subject half of the same rule, on the throughput row — the only trial of its cell, so re-keying it leaves no gap in anyone's trial numbering and X9 stays out of it |
| `x8-regime-not-declared.jsonl` | X8 | `large-subject-throughput` removed from `subbench.regimes` while a match row still claims it — a result in a regime the sub-bench says it does not exercise |
| `x9-duplicate-trial.jsonl` | X9 | trial 2 of one (pattern, subject, regime) recorded twice — silently doubling that trial's weight in any median |
| `x10-cost-class-mismatch.jsonl` | X10 | a compile row claiming `interpretive` cost on a `compiled-aot` testee. This is also the file stamped `schema_version: 1.0` while carrying 1.1's fields — deliberately, so validate.py's accept-an-older-MINOR branch has a live example and nobody quietly makes the minor comparison strict (note §4.1) |
| `x11-timing-on-uncompiled-cell.jsonl` | X11 | a timed match row for the pattern this testee reported `unsupported-by-declaration` |
| `x12-phase-names-mismatch.jsonl` | X12 | a compile row whose second phase is `cc` where the testee declared `gcc`: phase-by-phase numbers added up across rows that do not mean the same thing |
| `x12-phase-order-swapped.jsonl` | X12 | the `gcc` and `load` phases exchanged, values and all: the same three names in the wrong ORDER, which attributes 214 ms of compiler time to a dynamic load. The subtler half of the rule, and the reason X12 checks order and not just membership |
| `x13-measured-but-loaded.jsonl` | X13 | `status: measured` on a record whose after-load exceeded the limit |
| `x13-occupancy-after-fail.jsonl` | X13 | `status: measured` on a record whose per-core occupancy check FAILED *after* the run — the neighbour that started up midway, which a before-only check cannot see |
| `x13-occupancy-unavailable.jsonl` | X13 | `status: measured` on a record whose post-run occupancy check is `unavailable` — no mpstat, so nothing is known about the other cores. Under the v1.1 ruling that is `inconclusive-load`, not `measured` |
| `x14-missing-compile-row.jsonl` | X14 | `status: measured` with a pattern that has no compile row at all |
| `x15-mask-as-integer.jsonl` | X15 | `vm_rungs: 3` instead of the array of set bit names — the raw bitmask an adapter reaches for first, which no reporter can filter without pcrec's bit table (note §7 rule 3) |
| `x15-metadata-wrong-scope.jsonl` | X15 | the `engine` pair — declared `scope: pattern` — stamped on a MATCH row. The scope half of X15 has no good-example coverage now that the v8 example's undescribed `tier` pair is gone (note §7), so this control is the only thing holding it |
| `x15-undeclared-engine-metadata.jsonl` | X15 | an `engine_metadata` pair the testee never declared |
| `x16-lazy-jit-no-warmup.jsonl` | X16 | *(built from the **v8** example)* a `lazy-jit` testee declaring `warmup_trials: 0` — the class whose compile cost IS the first trial, claiming no trial needs excluding |
| `x17-future-major-version.jsonl` | X17 | a record at schema version 2.0, which this validator does not implement and for which no migration is declared. It is also the standalone half of X17: the cross-FILE half (two majors in one invocation) needs two files and is exercised by hand |
| `x18-duplicate-seq.jsonl` | X18 | two result rows claiming the same `seq` — the record no longer says which was emitted first, which is the one thing `seq` exists to say |
| `x18-seq-gap.jsonl` | X18 | the last result row's `seq` bumped past N: a row was dropped somewhere and the file does not admit it |
| `x19-load-raw-mismatch.jsonl` | X19 | `load.after.load1` says 0.14 while the `loadavg_raw` line it claims to be parsed from says 9.90 |
| `x20-verdict-quiet-but-loaded.jsonl` | X20 | `load.verdict: quiet` beside a peak `load1` of 11.4 against a limit of 6.0. X13 alone is satisfied by this record, which is why X20 exists |
| `x21-calibration-below-target.jsonl` | X21 | a probe that predicts a 20 ms loop recorded as having chosen an iteration count for a 50 ms target, with no `calibration_note` — the short loop that reads as a fast engine |
| `x22-unpinned-engine-version.jsonl` | X22 | `engine_version: 0.9.0-g1a2b3c4` — a `git describe` string, not a release — with `engine_commit: null`. §6.2 has always said the version must be reproducible from the commit; this is the first time anything checks it |
| `x23-compiler-not-derived.jsonl` | X23 | `compiler` naming a gcc version `compiler_raw` does not |
| `x23-cpu-model-not-derived.jsonl` | X23 | `cpu_model: example-cpu` beside a `cpu_model_raw` that normalizes to `example-cpu-12-core` — the FILTERABLE half and the reproducible half disagreeing, which is the whole failure mode §6 exists to prevent |
| `x23-kernel-not-derived.jsonl` | X23 | `kernel` naming a release `kernel_raw` does not |
| `x24-bytes-processed-exceeds-offered.jsonl` | X24 | `bytes_processed` ten times what 44 offered bytes × 200000 iterations can be — a cell's MB/s multiplied by ten, in a record that validated |
| `x25-consumed-exceeds-offered.jsonl` | X25 | `consumed_length: 4400` on a 44-byte subject |
| `x25-truncation-without-loss.jsonl` | X25 | a `truncated-subject` row whose `consumed_length` equals the full 1 MB offered — a truncation that truncated nothing |
| `x26-occupancy-verdict-contradicts-number.jsonl` | X26 | `occupancy.before.verdict: pass` beside a busiest-core reading of 91.5% against a 10% limit |
| `x27-whole-subject-without-compile-row.jsonl` | X27 | `p-quoted-local`'s whole-subject compile rows removed, leaving its whole-subject match row matching against an artifact the record never witnessed compiling |

## Adding one

Every new cross-line rule gets a file here, named for it — and since
v1.1 `schema/check_rules.py` fails the build if one does not, so this is
now a rule rather than a habit. The generator
that produced these lived in the session scratchpad and is deliberately
not committed: a sabotage is easier to read as a finished file than as a
mutation function, and these files change only when a rule does.

## When a control fires more than one rule

`--expect-rule` requires the NAMED rule to be among those that fired; it
does not require it to be alone. Three controls legitimately fire more
than one, and all three are honest rather than sloppy:

- `x14-missing-compile-row` also fires X11 and X27 — it deletes BOTH
  forms' compile rows for one pattern, so that pattern's timed plain
  rows lose their provenance (X11) and its whole-subject row loses its
  artifact (X27). Three rules for one deletion is what deleting a
  pattern's whole compile history actually looks like.
- `x1-mixed-schema-versions` also fires X18 and X9 — the second record's
  rows bring their own `seq` 1..N and their own trial numbering, which
  collide with the first record's. A concatenation is detectable in
  several ways at once; that is a property of concatenation, not a
  defect in the control.
- `x6-tampered-hash` is the one control that is deliberately NOT
  restamped, so its edit and its hash disagree by construction.

Maintenance: update this file when files are added/removed or change role.
