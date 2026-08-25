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
| `x14-missing-compile-row.jsonl` | X14 | `status: measured` with a pattern that has no compile row at all |
| `x15-undeclared-engine-metadata.jsonl` | X15 | an `engine_metadata` pair the testee never declared |
| `x17-future-major-version.jsonl` | X17 | a record at schema version 2.0, which this validator does not implement and for which no migration is declared. It is also the standalone half of X17: the cross-FILE half (two majors in one invocation) needs two files and is exercised by hand |

## Adding one

Every new cross-line rule gets a file here, named for it. The generator
that produced these lived in the session scratchpad and is deliberately
not committed: a sabotage is easier to read as a finished file than as a
mutation function, and these files change only when a rule does.

Maintenance: update this file when files are added/removed or change role.
