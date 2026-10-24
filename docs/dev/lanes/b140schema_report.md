# b140schema report -- record schema v1.9 (the substitution regime)

Branch lane/b140schema. Design: docs/design/subst_bench_v1.md 5 (S1-S8) as amended by 8a item 7 (TOOLS tier timed through `| wc -c`).

## What landed
- schema/record.schema.json 1.9: regime `substitution`; `testee.invocation`; `match_row.subst`, `.unsupported_reason`, `.process` (with `sink` const `wc-c`, `sink_bytes`, `core`, `sink_core`, rusage, `page_cache_resident`). Case ids are an opaque string (`^[a-z0-9][a-z0-9-]*$`), none enumerated.
- schema/validate.py: X36-X43 (`_subst_rules`), X11/X14 relaxed for a `process` testee.
- docs/design/record_schema.md: version row, enums, 6.12, field tables, rules table; check_fields/check_rules unchanged (they read the note).
- schema/examples: 2 valid (library, process); examples/bad: 11 controls for X36-X43.
- pcrecbench/record.py SCHEMA_VERSION 1.9 (the house rule: the writer stamps the latest, as [B137]); CLAUDE.md, schema/CLAUDE.md, examples CLAUDE.mds.

## Rules
X36 subst iff regime substitution; X37 gate<->match_outcome and unsupported_reason coherence; X38 process iff timed process row; X39 sink_bytes == out_bytes; X40 wc core != tool core; X41 process => interpretive; X42 v1.9 members only on >= 1.9 record; X43 trials of a cell agree on case/gate/nsubst/out_bytes/out_sha256.

## Decisions to flag
- Non-agreeing gates (wrong, divergent-declared, unsupported) map to `match_outcome` `did-not-match-as-expected` (with the existing `observed`); no new match_outcome value was added.
- `process` is required only on TIMED process rows (a gate-failed cell is never launched under the timed protocol).
- Compile rows are optional (not forbidden) for a process testee.
- The generator for the example records was a throwaway in the lane scratch, not committed.

## Validation
make check-schema: 7 -> 9 accepted, 76 -> 87 rejected for the intended rule, 0 wrong; check_rules 35 -> 43 rules; 40 sampled store records (v1.x) validate under the 1.9 validator. Full make check-harness NOT run (OWED to the manager; nothing in tools/selfcheck.py hardcodes 1.8, it reads record.SCHEMA_VERSION).
