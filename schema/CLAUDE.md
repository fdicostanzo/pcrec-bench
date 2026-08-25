# schema/ — the record format, its validator, its examples

The RECORD is pcrec-bench's unit of measured data: one file for one CELL
(one sub-bench version × one testee) measured in one RUN, JSONL,
schema-versioned, written once and never edited (requirements.md §2, §6;
APPROACH.md §3's "standardized per-testee output artifacts, compared
statically"). This directory owns that format.

The DESIGN lives in `../docs/design/record_schema.md` — every field, why
it exists, the enums, the normalization rules, the cross-line rules
X1..X17, and the open questions. Read it before changing anything here;
the files below are its implementation and `make check-schema` fails if
they and the note disagree.

## Files

- `record.schema.json` — JSON Schema draft 2020-12. One `$defs` entry
  per line kind (`setup`, `match_row`, `compile_row`); the root is their
  `oneOf`, so a generic tool can validate a line without knowing which
  it is. `x-record-schema-version` at the root is the version this
  schema IMPLEMENTS (1.0), which is what `validate.py` compares a file's
  `schema_version` against.
- `validate.py` — the validator the harness and the reporter share
  (requirements §6). Per-line schema validation PLUS the cross-line
  rules a schema cannot express. `python3` + `jsonschema` only, so it
  runs anywhere a record is read. Modes: plain, `--expect-reject`
  (positive controls), `--expect-rule` (which rule must fire),
  `--check-filename` (rule X4), `--allow-mixed-versions` (rule X17),
  `--print-hash` (restamp an edited example).
- `check_fields.py` — diffs the design note's field tables against the
  JSON Schema, field for field, in both directions. The note and the
  schema are two independent hand-written statements of one contract;
  this is what keeps them from drifting apart silently.
- `examples/` — records that MUST validate. See its CLAUDE.md.
- `examples/bad/` — records that MUST NOT. See its CLAUDE.md.

## How to run it

    make check-schema          # from the repo root; it is also the default target

Three checks: the note against the schema; every good example accepted;
every sabotage rejected FOR THE RULE ITS FILE NAME NAMES. The third is
what makes the first two mean anything.

## Rules for changing the format

- Adding an OPTIONAL field or an ENUM VALUE is a MINOR bump
  (`x-record-schema-version`, the note §4) and needs a line in the note
  saying why. Anything else is a MAJOR bump and needs a declared
  migration.
- A new field needs a row in the note's `### FIELD TABLE:` block for its
  kind, or `check_fields.py` fails. That is deliberate: a field with no
  stated reason is a field nobody can filter on with confidence.
- A new cross-line rule needs a sabotaged record in `examples/bad/`
  named for it. A check with no failing case proves nothing.
- Nothing pcrec-specific becomes a top-level field. pcrec's mechanism
  stamps go in `engine_metadata` under the per-testee declaration, like
  every other engine's (requirements §4.2; R1 finding B1).
- No statistics. Records carry raw trials; medians, spreads and
  MB/s belong to the reporter (requirements §6, OD-B1).

Maintenance: update this file when files are added/removed or change role.
