# schema/examples/bad/ — records that MUST be rejected

The positive controls. pcrec's own history is the argument for them:
every check this project's sibling has written and later found broken
was broken in the direction of PASSING, and a check with no failing case
proves nothing about the rule it claims to enforce.

Each file is a good example with exactly ONE thing wrong, and its
content hash restamped so the sabotage is the only defect — a control
that fails for two reasons is not a control. (`x6-tampered-hash` is the
deliberate exception: not restamping IS its sabotage.) The pre-1.4
controls are built from the pcrec 1.1 example (`x16-lazy-jit-no-warmup`
and `x30-two-floor-patterns` from the v8 one, because the rules they
control only exist for a `lazy-jit` testee / a second pattern); the
sixteen v1.4 controls ([B20]) are built from the GENERATED 1.4 example
(`../gen_example_14.py`'s output), each a one-field mutation of it
constructed to fire ONLY its rule. Where a rule could be
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
| `x28-local-binary-not-scratch.jsonl` | X28 | `engine_version: local:0123456789ab` — a binary nobody pinned by commit — on a record with no `tier`, which is `pinned`. `testee.binary` is present (so X29 stays out), the ids are re-derived (so X3/X5 stay out) and X22 exempts the shape: the one defect is a local binary claiming the pinned tier, which is exactly what "a bench number never comes from a dirty tree" forbids |
| `x29-scratch-without-binary.jsonl` | X29 | `tier: scratch` with no `testee.binary` — a scratch record that does not say what the binary was, which is the one thing a scratch record's engine identity consists of |
| `x30-two-floor-patterns.jsonl` | X30 | *(built from the **v8** example, like `x16`)* both patterns carry `role: "floor"` — a record may declare at most one: the floor pattern's whole point is a SINGLE per-call baseline the rest of the set reads against, and two of them leave that baseline ambiguous |
| `x13-measured-but-target-core-busy.jsonl` | X13 (v1.4) | *(built from the **1.4** example, like every row below)* `occupancy.before.target_busy_pct: 55.0` beside `status: measured` and `pinning.cpu: 2` — the TARGET core was busy before the run: a competitor pinned where the cell was measured sits under every trial uniformly, which trial agreement cannot see (clause 3) |
| `x13-measured-but-target-busy-null.jsonl` | X13 (v1.4) | `occupancy.before.target_busy_pct: null` beside `verdict: pass`, `pinning.cpu: 2`, `status: measured` — the target's row was missing from the capture, the same unknown as `unavailable` (the missing-row control, ruling R-2; the pre-flight refuses it before the run, X13 clause 3 refuses `measured` for it after) |
| `x13-measured-but-trials-disagree.jsonl` | X13 (v1.4) | both judged rows of (`p-addrspec`, match-compliance, whole-subject) given two 2× trials, the block RECOMPUTED to `disagree` (d = 2 of n = 2), status left `measured` — X31/X32 quiet, X13 clause 4 alone |
| `x13-measured-but-load-before-high.jsonl` | X13 (v1.4) | `load.before.load1: 9.8` (its `loadavg_raw` edited to match, so X19 stays out), `load.verdict` already `loaded` (X20 quiet), `status: measured` — the control that shows the v1.4 X13 reads the BEFORE sample and not the verdict (clause 1) |
| `x13-measured-but-na-trials-pinned.jsonl` | X13 (v1.4) | the example truncated to 3 trials (`seq` renumbered, the block recomputed to `n/a-trials` with every count 0 and every row key unjudged under `na_trials`), `tier: pinned`, `status: measured` — a pinned record without the five odd trials the rule needs is `inconclusive-spread` (ruling R-12; clause 4) |
| `x31-verdict-contradicts-groups.jsonl` | X31 | the same two-slow-trial sabotage, every count stamped CORRECTLY (`groups_disagreeing: 1`), only `verdict: agree` wrong — X32 quiet (the counts recompute), X13 quiet (`agree` satisfies clause 4), X31 alone |
| `x32-groups-disagreeing-not-recomputable.jsonl` | X32 | the same rows, the block left as the CLEAN record's (`groups_disagreeing: 0`, `rows_disagreeing: 0`, `verdict: agree`, `worst_group` d = 0) — self-consistent, so X31 is quiet: the "stamp 0 beside the rows" sabotage, which is the whole reason X32 exists |
| `x32-trials-not-recomputable.jsonl` | X32 | `trial_agreement.trials: 7` on a 5-trial record (7 is odd and ≥ 5, so X31 stays quiet) |
| `x32-rows-unjudged-not-recomputable.jsonl` | X32 | `rows_unjudged: 4` where the rows say 3 (the reasons object left correct, so it is the count alone) |
| `x32-worst-group-unknown-pattern.jsonl` | X32 | `worst_group.pattern_id: p-nonexistent` — the key neither recomputes nor exists in `setup.patterns[]` |
| `x33-trial-agreement-missing.jsonl` | X33 | a 1.4 record with NO `trial_agreement` block (X13 clause 4 deliberately does not read an absent block, so X33 is the only finding) |
| `x33-trial-agreement-on-a-v13-record.jsonl` | X33 | the block on a record re-stamped `1.3` (its status set `inconclusive-load` so the v1.1 X13 stays out of it) — the OTHER direction: a block on a record stamped before the version that defined it is a mis-stamped record, not a forward-compatible one |
| `schema-status-inconclusive-spread-misspelt.jsonl` | SCHEMA | `status: inconclusive_spread` — the token-spelling rule (record_schema.md §5) |
| `schema-target-busy-beside-unavailable.jsonl` | SCHEMA | `occupancy.after.verdict: unavailable`, `max_busy_pct: null` and `target_busy_pct: 3.0` — a target number beside a sample that measured nothing, which S2's `then` branch forbids (on the AFTER sample so the v1.4 X13 stays out) |
| `schema-trial-agreement-unknown-member.jsonl` | SCHEMA | the block carrying the earlier draft's dropped `worst_row` array — `additionalProperties: false` is what makes a removal stick |
| `schema-timeline-item-missing-member.jsonl` | SCHEMA | a `timeline[]` item with no `elapsed_ms` — the denominator of its percentages, required |

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
than one, and all three are honest rather than sloppy (every v1.4
control fires exactly one rule — `x32-groups-disagreeing-not-recomputable`
and `x32-worst-group-unknown-pattern` report several X32 problems, all
X32):

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
