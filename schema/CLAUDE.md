# schema/ — the record format, its validator, its examples

The RECORD is pcrec-bench's unit of measured data: one file for one CELL
(one sub-bench version × one testee) measured in one RUN, JSONL,
schema-versioned, written once and never edited (requirements.md §2, §6;
APPROACH.md §3's "standardized per-testee output artifacts, compared
statically"). This directory owns that format.

The DESIGN lives in `../docs/design/record_schema.md` — every field, why
it exists, the enums, the normalization rules, the cross-line rules
X1..X33, the record tiers (§6.8), the floor-pattern role (§5 ADDITIONS
7), trial agreement (§6.9, designed in `gate_shape_v14.md`), and the
open questions. Read it before changing anything here;
the files below are its implementation and `make check-schema` fails if
they and the note disagree.

## Files

- `record.schema.json` — JSON Schema draft 2020-12. One `$defs` entry
  per line kind (`setup`, `match_row`, `compile_row`); the root is their
  `oneOf`, so a generic tool can validate a line without knowing which
  it is. `x-record-schema-version` at the root is the version this
  schema IMPLEMENTS (1.4), which is what `validate.py` compares a file's
  `schema_version` against. v1.2 added the two optional TIER fields
  (`tier`, `testee.binary`) and the `local:` shape of `engine_version`
  ([B10]); v1.3 added optional `patterns[].role` (`member`/`floor`,
  absent = `member`, [B15]); v1.4 ([B20], `docs/design/gate_shape_v14.md`)
  added `inconclusive-spread` to `record_status`, the tri-state
  `occupancy_sample.target_busy_pct`, the `trial_agreement` setup block
  (`$defs.trial_agreement`, not in `setup.required` — the schema is
  version-blind; X33 owns the requirement), the per-group occupancy
  `timeline` (provenance), and dropped the compile row's "no cost beside
  a refusal" branch (KB-4); every 1.1, 1.2 and 1.3 record still
  validates, and the older examples are left stamped at their own
  versions to prove it.
- `validate.py` — the validator the harness and the reporter share
  (requirements §6). Per-line schema validation PLUS the cross-line
  rules a schema cannot express, PLUS the three normalization rules of
  the note's §6.6-§6.7 as functions (`normalize_cpu_model`,
  `normalize_kernel`, `normalize_compiler`) — a rule stated only in
  prose is a rule nobody runs, and X23 is what runs these. `python3` + `jsonschema` only, so it
  runs anywhere a record is read. Modes: plain, `--expect-reject`
  (positive controls), `--expect-rule` (which rule must fire),
  `--check-filename` (rule X4), `--allow-mixed-versions` (rule X17),
  `--print-hash` (restamp an edited example). Rules X28/X29 (v1.2) are
  the tier rules: a `local:` binary is never `pinned`, and a `scratch`
  record says what its binary was. Rule X30 (v1.3) is the floor-pattern
  rule: at most one `patterns[]` entry may carry `role: floor`. Rules
  X31-X33 (v1.4) are the trial-agreement rules: the block's verdict
  follows from its counts (X31); its counts are RECOMPUTED from the
  match rows by `validate.py`'s OWN `judge_trial_agreement` — a
  deliberate second implementation of gate_shape_v14.md §3.5, no
  `pcrecbench` import, comparing integer counts and the worst group's
  key only (X32); the block is present iff the record is stamped ≥ 1.4
  (X33, both directions). X13 is VERSIONED at 1.4: a record's own
  `schema_version` selects the text that judges it (record_schema.md
  §4's rule-revision clause), so older records keep the verdict of
  their day.
- `check_fields.py` — diffs the design note's field tables against the
  JSON Schema, field for field, in both directions. The note and the
  schema are two independent hand-written statements of one contract;
  this is what keeps them from drifting apart silently.
- `check_rules.py` — the same idea for the note's §9 RULE table against
  `examples/bad/`'s directory listing: every rule must have a control
  named for it, every control must name a rule that exists. Added at
  v1.1 because five rules had reached that version with no control at
  all while the note claimed in prose that none could.
- `examples/` — records that MUST validate, and `examples/gen_example_14.py`,
  the committed deterministic generator of the 1.4 example (`--check` is
  part of `make check-schema`). See its CLAUDE.md.
- `examples/bad/` — records that MUST NOT. See its CLAUDE.md.

## How to run it

    make check-schema          # from the repo root; it is also the default target

Five checks: the note's field tables against the schema; the note's rule
table against `examples/bad/`; the generated 1.4 example reproducing
byte for byte; every good example accepted; every sabotage rejected FOR
THE RULE ITS FILE NAME NAMES. The last is what makes the others mean
anything, and the second is what makes the last one complete.

## Rules for changing the format

- Adding an OPTIONAL field or an ENUM VALUE is a MINOR bump
  (`x-record-schema-version`, the note §4) and needs a line in the note
  saying why. Revising a cross-line RULE is MINOR only under §4's
  rule-revision clause (v1.4, X13): keyed on `schema_version` in the
  validator, older records never re-judged, the rule's version rendered
  by the reporter beside every ranked status. Anything else is a MAJOR
  bump and needs a declared migration. 1.0 → 1.1 was a documented
  ONE-TIME exception to that rule (note §4.1) and it expires the moment
  the first record is stored; read §4.1 before assuming the next change
  of that shape can do the same.
- A new field needs a row in the note's `### FIELD TABLE:` block for its
  kind, or `check_fields.py` fails. That is deliberate: a field with no
  stated reason is a field nobody can filter on with confidence.
- A new cross-line rule needs a sabotaged record in `examples/bad/`
  named for it. A check with no failing case proves nothing — and since
  v1.1 `check_rules.py` enforces that rather than trusting it.
- Nothing pcrec-specific becomes a top-level field. pcrec's mechanism
  stamps go in `engine_metadata` under the per-testee declaration, like
  every other engine's (requirements §4.2; R1 finding B1).
- No statistics. Records carry raw trials; medians, spreads and
  MB/s belong to the reporter (requirements §6, OD-B1). The one argued
  exception (v1.4): `trial_agreement` carries COUNTS the rows determine,
  under a recomputation rule (X32) — never a time.

Maintenance: update this file when files are added/removed or change role.
