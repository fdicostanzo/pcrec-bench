# lane b36ids — report

Branch `lane/b36ids` off master `6a0a764`. Task: fix bench/syntax@0.1's
twelve schema-violating ids (bench/syntax@0.1's first-sample window ran
six cells over 259 minutes and wrote zero records, refused at
`store.write()`'s validator for uppercase ids the harness never
checked) and add the missing pre-flight so the harness refuses a bad id
before any cell runs. Full brief from the manager (team-lead), mirrored
in commit `3ff1ebc`'s message.

## (1) The rename

Ten pattern ids and two subject ids, all uppercase, renamed lowercase
following bench/syntax's own `-uc`/`-lc` convention (already used once
today for the case-COLLISION renames):

| old | new |
|---|---|
| `anc-A` | `anc-a-uc` |
| `anc-G` | `anc-g-uc` |
| `asr-K` | `asr-k-uc` |
| `cls-N` | `cls-n-uc` |
| `mod-J` | `mod-j-uc` |
| `mod-U` | `mod-u-uc` |
| `msc-C` | `msc-c-uc` |
| `msc-R` | `msc-r-uc` |
| `msc-X` | `msc-x-uc` |
| `rec-R` | `rec-r-uc` |
| `f-CAT` (subject) | `f-cat-uc` |
| `f-Cat` (subject) | `f-cat-mixed` |

None collided with an existing lowercase id (checked before renaming).
No record anywhere carries the old ids (the six refused cells wrote
nothing), so this is not a version bump — `subbench.toml`'s `version`
stays `0.1`.

What moved, and how it was verified:

- `bench/syntax/patterns/*.rx` — ten files renamed via `git mv` (pure
  renames, confirmed with `git diff --stat -M`: zero content diff, only
  the path changed).
- `bench/syntax/gen_patterns.py` — the `PATTERNS` table's ten ids
  renamed, plus three prose cross-references (`` `rec-R` ``,
  `` `msc-R` ``) inside pattern notes.
- `bench/syntax/gen_subjects.py` — the `FIELDS` table's two subject ids
  renamed.
- `bench/syntax/coverage.tsv`, `subbench.toml`'s `[[patterns]]` block,
  `pattern_facts.tsv` — regenerated via `gen_patterns.py` /
  `gen_patterns.py --sidecar` / `gen_pattern_facts.py`; diffed against
  the pre-rename committed versions to confirm ONLY the id columns
  moved (shown by inspection of each diff).
- `bench/syntax/manifest.tsv` — regenerated via `gen_subjects.py`;
  diffed to confirm the sha256 column is unchanged (bytes identical)
  and only the `id` column moved for the two subjects; re-ran
  `gen_subjects.py` a second time and diffed the two outputs
  byte-identical (idempotence).
- `bench/syntax/expectations.tsv` — NOT regenerated (per the brief).
  Edited by a script that rewrote only the `pattern`/`subject` columns
  by the rename maps, verified row-for-row against a pre-edit copy:
  exactly 870 rows changed their pattern column (87 rows × 10 renamed
  patterns) and exactly 380 rows changed their subject column (190
  rows × 2 renamed subjects), and every other column of every row
  (including rows that changed one of the two id columns) is byte
  identical to the pre-edit file. `gen_expectations.py --check`
  afterwards re-derives all 8,265 rows from the libpcre2 10.46 oracle
  clean (no diff), confirming the edited file agrees with a fresh
  derivation under the new ids.
- `bench/syntax/NOTES.md` — eight prose cross-references to the ten
  renamed pattern ids updated (word-bounded sed); no subject-id
  mentions were present.
- `bench/syntax/CLAUDE.md` — convention item 4 grown with the new
  incident, the twelve renames, and the pointer to the new pre-flight
  (KB-12).
- Repo-wide word-bounded grep for all twelve old ids, after all edits:
  zero hits outside `bench/syntax/`'s own history text (my new KB-12
  entry) and the pre-existing `.rejected` staging debris under
  `store/records/syntax@0.1/` (left over from the incident run; already
  removed from master's tip by a separate commit not yet in this lane's
  base — out of this lane's scope, not touched here).

## (2) The pre-flight, in the harness

`pcrecbench/subbench.py`: `Subbench.__init__` now validates every
pattern id and every subject id (short and throughput) against the
record schema's own `$defs/slug` rule
(`^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`) before construction finishes. The
regex is read from `schema/record.schema.json` at call time
(`_slug_pattern()`, cached) — never retyped — so it can never drift
from what `schema/validate.py` enforces; an unreadable schema file
raises loudly (`SubbenchError`) rather than skipping the check. A
violation raises `SubbenchError` naming the id, the set, and the rule,
e.g.:

    id 'anc-A' violates the record schema's id rule
    ^[a-z0-9]([a-z0-9-]*[a-z0-9])?$ (schema/record.schema.json
    $defs/slug): lowercase letters, digits, single hyphens
    (set syntax@0.1, pattern id)

`pcrecbench run` and `quick` both construct a `Subbench` early in their
path (`subbench.find`/`subbench.load`), so this refuses in well under a
second instead of after a full multi-hour cell.

## (3) tools/selfcheck.py

Two additions, +13 checks (324 → 337):

- **`check_id_preflight`** (new function, 9 PASS lines): (a) a GENERIC
  gate — every `bench/*/` (via `subbench_dirs()`, [B11.1]'s
  enumeration rule) loads through `Subbench()` without raising (5
  lines, one per current set); (b) the negative control, both
  directions, for both id kinds — `_write_synthetic_subbench` builds a
  minimal never-committed `bench/<name>/`-shaped directory under
  `build/` (one pattern, one subject, nothing else): an uppercase
  PATTERN id is refused BY NAME with the rule quoted (checked: the id,
  `$defs/slug`, and the word "lowercase" all appear in the message),
  and the same sidecar with the id lowercased loads; then the same
  pair for a SUBJECT id, holding the pattern id clean so construction
  reaches the subject loader (4 lines).
- **`check_floor_pattern`** widened (+4 lines): its one-cell validator
  smoke — a real scratch-tier `quick` cell, schema-validated through
  `store.write()` — used to run on bench/email's floor pattern only.
  It now enumerates `bench/*/` and runs on every set's own floor
  pattern (altwide, bounded, email, loglines, syntax — one line each
  instead of one line total), closing the gap KB-12 names: `make
  check`'s one-cell validator smoke had never covered any set but the
  first one built. This was cheap to add generically: every set's
  floor pattern is a one-byte-or-so literal by charter (requirements
  §5), so the widened check still runs 5 tiny `quick` cells at 5
  subjects / 1 trial each, not a real measurement.

Residual honestly stated: I did NOT add a separate `--trials 1 --iters
1 --synthetic` cell via `pcrecbench run` (rather than `quick`) on every
set, because `run` has no per-pattern filter — it measures the WHOLE
declared pattern set of a sub-bench, and bench/altwide's widest rungs
(4096-way alternations) and bench/bounded's 65535-count rung would make
that expensive even at `--iters 1` (real pcre2/pcrec compiles of every
pattern in the set, not just the floor). The widened `quick`-based
floor smoke above already exercises `store.write()`'s validator gate
(pcrecbench/CLAUDE.md: "a record that fails validation is never
written") on every set's sidecar and manifest shape, which is what
KB-12's incident actually needed caught early — a full `run` smoke per
set would be a much larger, differently-scoped addition.

## Documentation

- `pcrecbench/CLAUDE.md` — `subbench.py`'s row grown with the KB-12
  pre-flight.
- `tools/CLAUDE.md` — the `selfcheck.py` table row, the floor-smoke
  paragraph, and a new KB-12 paragraph in its own house style.
- `bench/syntax/CLAUDE.md` — convention item 4 grown (see above).
- `docs/dev/known_issues.md` — **KB-12** filed in the house style
  (OBSERVED / WHY IT MATTERS / FIXED), naming the incident numbers from
  the brief (6 cells, 259 min, 0 records written, 31,747 validator
  lines on the first refused cell) and the fix.

## Validation

- `make check-schema`: 4/72/0 (unchanged; nothing here touches
  `schema/`).
- `make check-harness`: **337/337, 0 FAILED** (up from 324; log:
  `check-harness: 337 check(s) passed, 0 FAILED`). The two new KB-12
  lines and the four widened floor-smoke lines all print `PASS`.
- `bench/syntax/gen_patterns.py --check`: green (`95 pattern file(s)
  re-derive, coverage.tsv re-derives ..., the sidecar agrees with the
  table`).
- `bench/syntax/gen_pattern_facts.py --check`: green (`95 pattern fact
  row(s) re-derive from libpcre2 10.46 2025-08-27`).
- `bench/syntax/gen_subjects.py`: idempotent (re-run produces a
  byte-identical `manifest.tsv`).
- `bench/syntax/gen_expectations.py --check`: green (`8265
  expectation(s) re-derive from libpcre2 10.46 2025-08-27`) — this is
  the ~3.3 min step; ran to completion with no diff.
- `git diff --stat -M` on `bench/syntax/patterns/`: ten pure renames,
  zero content lines changed.
- `make check-report`: STARTED, running in the background at hand-off
  (KB-11: this target alone takes ~7-10 min on this box); if this
  section still says "STARTED" when you read it, the run had not
  finished when this report was committed — check
  `pcrecbench/tests/test_report.py`'s result directly. Nothing in this
  lane touches `report.py` or its tests, and `report.py` does not
  import `pcrecbench.subbench` at all ([B14] R3), so no interaction is
  expected.

## Delivery

Branch `lane/b36ids`, one commit (`3ff1ebc`) carrying the full change
plus this report. `git diff --stat -M` confirms pure renames for the
ten `.rx` files. Row counts: `expectations.tsv` verified row-for-row
(870 + 380 id-column changes, zero other-column changes). KB-12 filed.
`make check-harness` green at the new count.

STOPPING HERE per the boilerplate's lifecycle rule: work is committed
and documented. The one open item is `make check-report`'s own
completion, which is independent of this lane's changes (see above) —
worth a final glance in a resumed session if a definitive PASS is
wanted before merge, but nothing in this diff is expected to move it.
