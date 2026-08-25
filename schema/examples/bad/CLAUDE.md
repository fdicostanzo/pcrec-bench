# schema/examples/bad/ — records that MUST be rejected

The positive controls. pcrec's own history is the argument for them:
every check this project's sibling has written and later found broken
was broken in the direction of PASSING, and a check with no failing case
proves nothing about the rule it claims to enforce.

Each file is the good pcrec example with exactly ONE thing wrong, and
its content hash restamped so the sabotage is the only defect — a
control that fails for two reasons is not a control. (`x6-tampered-hash`
is the deliberate exception: not restamping IS its sabotage.)

**The file name names the rule.** The leading token before the first `-`
is the rule id `make check-schema` requires to fire: `x11-...` must fire
X11, `schema-...` must fire a JSON Schema violation. A file that is
rejected for some OTHER reason fails the build. The rules are defined in
`../../../docs/design/record_schema.md` §9.

## Files

| file | rule | the sabotage |
|---|---|---|
| `schema-missing-required-field.jsonl` | SCHEMA | `environment.machine_id` deleted |
| `schema-wrong-enum.jsonl` | SCHEMA | `execution_model` spelled `compiled-AOT` — the un-normalized spelling, which is the mistake an author actually makes |
| `x1-mixed-schema-versions.jsonl` | X1 | two records concatenated into one file, the second at schema version 2.0 |
| `x2-reserved-row-kind.jsonl` | X2 | a `match-list` row — the name reserved for OD-B3's list-valued scan regime, which has no shape yet |
| `x2-unknown-row-kind.jsonl` | X2 | a row with `kind: "timing"` |
| `x3-record-id-mismatch.jsonl` | X3 | `record_id`'s stamp no longer matches `run.timestamp` |
| `x4-filename-mismatch.jsonl` | X4 | a perfectly valid record under a name that is not its record id |
| `x6-tampered-hash.jsonl` | X6 | one `elapsed_ns` edited after the fact, hash NOT restamped |
| `x9-duplicate-trial.jsonl` | X9 | trial 2 of one (pattern, subject, regime) recorded twice — silently doubling that trial's weight in any median |
| `x10-cost-class-mismatch.jsonl` | X10 | a compile row claiming `interpretive` cost on a `compiled-aot` testee |
| `x11-timing-on-uncompiled-cell.jsonl` | X11 | a timed match row for the pattern this testee reported `unsupported-by-declaration` |
| `x13-measured-but-loaded.jsonl` | X13 | `status: measured` on a record whose after-load exceeded the limit |
| `x13-occupancy-after-fail.jsonl` | X13 | `status: measured` on a record whose per-core occupancy check FAILED *after* the run — the neighbour that started up midway, which a before-only check cannot see |
| `x19-load-raw-mismatch.jsonl` | X19 | `load.after.load1` says 0.14 while the `loadavg_raw` line it claims to be parsed from says 9.90 |
| `x20-verdict-quiet-but-loaded.jsonl` | X20 | `load.verdict: quiet` beside a peak `load1` of 11.4 against a limit of 6.0. X13 alone is satisfied by this record, which is why X20 exists |
| `x21-calibration-below-target.jsonl` | X21 | a probe that predicts a 20 ms loop recorded as having chosen an iteration count for a 50 ms target, with no `calibration_note` — the short loop that reads as a fast engine |
| `schema-missing-calibration.jsonl` | SCHEMA | a timed match row with `iterations` in the hundreds of thousands and no `calibration` object saying who chose that number |
| `x14-missing-compile-row.jsonl` | X14 | `status: measured` with a pattern that has no compile row at all |
| `x15-metadata-wrong-scope.jsonl` | X15 | the `engine` pair — declared `scope: pattern` — stamped on a MATCH row. The scope half of X15 has no good-example coverage now that the v8 example's undescribed `tier` pair is gone (note §7), so this control is the only thing holding it |
| `x15-undeclared-engine-metadata.jsonl` | X15 | an `engine_metadata` pair the testee never declared |
| `x18-duplicate-seq.jsonl` | X18 | two result rows claiming the same `seq` — the record no longer says which was emitted first, which is the one thing `seq` exists to say |
| `x18-seq-gap.jsonl` | X18 | the last result row's `seq` bumped past N: a row was dropped somewhere and the file does not admit it |
| `x17-future-major-version.jsonl` | X17 | a record at schema version 2.0, which this validator does not implement and for which no migration is declared. It is also the standalone half of X17: the cross-FILE half (two majors in one invocation) needs two files and is exercised by hand |

## Adding one

Every new cross-line rule gets a file here, named for it. The generator
that produced these lived in the session scratchpad and is deliberately
not committed: a sabotage is easier to read as a finished file than as a
mutation function, and these files change only when a rule does.

## When a control fires more than one rule

`--expect-rule` requires the NAMED rule to be among those that fired; it
does not require it to be alone. Three controls legitimately fire more
than one, and all three are honest rather than sloppy:

- `x14-missing-compile-row` also fires X11 — a timed match row whose
  pattern has no compile row has no provenance either (note §9's first
  corollary).
- `x1-mixed-schema-versions` also fires X18 and X9 — the second record's
  rows bring their own `seq` 1..N and their own trial numbering, which
  collide with the first record's. A concatenation is detectable in
  several ways at once; that is a property of concatenation, not a
  defect in the control.
- `x6-tampered-hash` is the one control that is deliberately NOT
  restamped, so its edit and its hash disagree by construction.

Maintenance: update this file when files are added/removed or change role.
