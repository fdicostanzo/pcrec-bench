# lane b44boolgrain — boolean-grain scoring in the harness

Branch `lane/b44boolgrain`, worktree `worktrees/b44boolgrain`, branch
point `a0ab43f` (master). Executes Frank's Q3 boolean-grain ruling
(`docs/design/capability_set_v1.md` §5.6 option B) for the blocker lane
`l6bvs` found and proved: `harness.outcome_for`'s span check fired
unconditionally on `row.matched`, so a boolean-grain testee's every true
match scored `wrong-span-or-captures` with `observed.span = [None,
None]` — which then FAILS SCHEMA VALIDATION (`span`'s array items must
be integers; only the whole field may be `null`), so
`vectorscan-block-nosom` could not write a valid record for any cell
containing a real match.

This lane touches only `pcrecbench/harness.py`, `pcrecbench/record.py`,
`schema/record.schema.json`, `schema/validate.py`,
`docs/design/record_schema.md`, `schema/examples/`, `tools/
selfcheck.py`, and the CLAUDE.md files for the directories those files
live in. It does NOT touch `testees/vectorscan/` or `lane/l6bvs`'s
branch — that lane's `configs.toml`/`CLAUDE.md` are read-only inputs
(see "The declaration seam" below for the reconciliation).

## Session-start correction

This session's first message arrived with the cwd apparently pointed at
`worktrees/b42repdiag` — a different lane's worktree containing that
lane's uncommitted regen work. Nothing there was read or touched;
`worktrees/b44boolgrain` was created fresh off `master` per
BOILERPLATE.md's own ritual before any edit was made, and the
environment corrected itself on the next tool call.

## A mid-lane mistake, caught and fixed

Partway through, several `Edit` calls were made against
`/home/duxevents/pcrec-bench/<file>` — the MAIN CHECKOUT's absolute
path — rather than the worktree's. This was caught immediately by
running the schema checks and finding the edits had landed nowhere
useful (and, on inspection, in the wrong tree). Recovery: the main
checkout's diff was captured (`git diff > <scratchpad>/patch`), the main
checkout was restored to clean (`git checkout -- <the four files>`), and
the SAME diff was applied inside `worktrees/b44boolgrain` with `git
apply`. Verified both ways: `git status --short` in the main checkout is
clean, and the worktree's `git rev-parse --show-toplevel` /
`git branch --show-current` confirm every subsequent edit landed in
`worktrees/b44boolgrain` on `lane/b44boolgrain`. No file under the main
checkout carries any trace of this lane's work.

## 1. The grain mechanism (`pcrecbench/harness.py`)

`outcome_for(row, expectation, regime, subject, giveup_ok=True,
convention=None, grain="full")` — a new `grain` parameter in the exact
shape `convention` already has (R5 B1/CB1 precedent). Two changes:

- **A new private helper, `_observed_span(row)`**: returns `[row.start,
  row.end]` when both are not `None`, else the bare `None` the schema's
  `observed.span` field allows for the WHOLE field. Every one of
  `outcome_for`'s five hand-built `[row.start, row.end] if row.matched
  else None` expressions is replaced by a call to it. This is
  UNCONDITIONAL, not `grain`-gated — a `full`-grain testee's matching
  rows always carry real integers by construction, so the helper is a
  no-op there; the practical beneficiary is a `boolean`-grain testee's
  `did-not-match-as-expected`/`truncated-subject` rows, which is where
  `[None, None]` was ALSO schema-illegal before this lane (a false
  positive from `vectorscan-block-nosom`, not merely its true matches).
- **The span-mismatch branch is skipped at `grain="boolean"`**: `if
  (grain != "boolean" and row.matched and (row.start !=
  expectation.start or row.end != expectation.end))`. Nothing else
  changes — the `row.matched != expectation.matched` boolean check
  (which decides `did-not-match-as-expected`) was never span-shaped and
  needs no grain guard.

`run_cell` reads `testee_grain = testee_block.get("grain", "full")` —
the same `.get(..., default)` shape `testee_convention` already has —
and threads it into the one `outcome_for` call site. ABSENT means
`"full"`, so every existing testee (none of which declares `grain`) is
provably unchanged; verified live (see §4).

`consumed_length` is untouched by this lane: `l6bvs`'s CLAUDE.md states
Vectorscan's own convention (the whole subject length, unconditionally)
and nothing in `outcome_for` reads `grain` when building it.

## 2. The declaration seam

`grain` is one more key in the dict an `Adapter.describe()` returns —
the SAME shape `conventions` already has (a per-config Python literal
in every adapter today, not a dynamically-read `configs.toml` key on
ANY adapter, `conventions` included). `harness.run_cell` reads
`testee_block.get("grain", "full")`, and `record.build_setup` already
copies the whole `testee_block` dict into the record's `testee` object
verbatim (`dict(testee_block)`, `pcrecbench/record.py:257`) — so a
declaring adapter's grain is queryable on every record it writes with
NO second code path. Engine-neutral by construction (R-BENCH-4):
nothing in `pcrecbench/harness.py` or `pcrecbench/record.py` names
Vectorscan or any other engine.

**Reconciliation note for the manager, not a change to `lane/l6bvs`**:
that branch's `testees/vectorscan/configs.toml` does NOT declare a
machine-readable grain key today — it states the boolean-grain fact in
PROSE only (`configs.toml`'s header comment and `CLAUDE.md`'s "THE
GOVERNING RULING" section). There is therefore no key-NAME collision to
reconcile; wiring `vectorscan-block-nosom` to this mechanism is a
one-line addition to that lane's `adapter.py::describe()` —
`"grain": "boolean"` alongside its existing `"captures": "off"` literal
— which the manager can make at merge time (or hand back to a fresh
`l6bvs`-lineage lane). This lane does not make that edit itself, per the
brief's explicit instruction not to touch `lane/l6bvs`'s files.

## 3. Schema half — v1.6, additive, smallest possible

Chose the schema-field route over `engine_metadata` (the brief's
alternative): `engine_metadata` is a per-testee DECLARED, dynamically-
typed extension point for engine MECHANISM facts (`RX_VM_*` stamps and
the like), validated per-declaration; `grain` is a SCORING-SEMANTICS
control that changes which branch `outcome_for` takes, the same class
of fact `conventions` already is as a formal top-level field. Following
that precedent kept the change smallest and most consistent, and made
it directly parallel to a mechanism the schema and the design note
already document at length.

- `schema/record.schema.json`: `x-record-schema-version` 1.5 → 1.6; new
  `$defs/grain` enum (`full`/`boolean`); `testee.grain` added as
  OPTIONAL (not in `required`) — absent means `full`.
- `docs/design/record_schema.md`: version history row; §5 ADDITIONS
  item 8 (`grain` exists at all); the `testee.grain` FIELD TABLE row;
  a new §6.10 subsection (mirrors §6.8/§6.9's shape — the declaration
  seam, precisely what `grain` changes in `outcome_for`, and that
  `_observed_span` fixes the schema-illegal shape unconditionally); the
  §9 rule table's new X34 row.
- `schema/validate.py`: rule X34 — "when `testee.grain = boolean`, no
  match row's `observed.span` is a non-null value" — a CROSS-LINE check
  (a plain per-line JSON Schema cannot see `setup.testee.grain` and a
  match row's `observed.span` at once; this is exactly the shape a
  schema alone cannot express). Module docstring's rule-list references
  bumped `X1..X33` → `X1..X34` (two sites).
- `schema/examples/boolgrain-example@0.1__example-boolscan_...jsonl` —
  a NEW, hand-built, hand-restamped good example (`testee.grain:
  "boolean"` on a fictional `example-boolscan` engine, modeled on
  `testees/vectorscan/CLAUDE.md`'s real shape but named differently so
  it never collides with that lane's own testee_id namespace — same
  precedent as the existing `v8-regexp` example, which also corresponds
  to no real adapter under `testees/`). Two match rows: a genuine match
  (`matched-as-expected`, `observed` ABSENT), a false positive
  (`did-not-match-as-expected`, `observed.span: null`).
- `schema/examples/bad/x34-boolean-grain-nonnull-span.jsonl` — the
  one-field mutation of the good example above (the false-positive
  row's span set to a real `[0, 3]`), rejected for X34 and nothing else.
- `pcrecbench/record.py`: `SCHEMA_VERSION` "1.5" → "1.6" (found while
  verifying with a real `quick` smoke — every NEW record this harness
  writes must declare the version it is actually written against, per
  that constant's own comment; a latent oversight this lane's own
  verification caught and fixed).

CLAUDE.md updates: `schema/CLAUDE.md`, `schema/examples/CLAUDE.md`,
`schema/examples/bad/CLAUDE.md`, `pcrecbench/CLAUDE.md`, `tools/
CLAUDE.md` — each names the new files/mechanism in its own directory's
existing style (no root `CLAUDE.md` STATUS-blob edit, deliberately, to
avoid a merge collision with the several concurrently-running lanes
that touch it).

## 4. Checks — all run in isolation, none of them `make check-harness`

- **Syntax**: `python3 -c "import ast; ast.parse(...)"` on
  `harness.py` (a merge slip during editing left a docstring paragraph
  as bare code outside its own triple-quote; caught and fixed before
  any further work).
- **`make check-schema`** (explicitly permitted, ~3 s, python3 +
  jsonschema only): **5 example(s) accepted, 73 sabotage(s) rejected
  for the intended rule, 0 WRONG** (was 4/72/0 before this lane; +1
  example, +1 rule/control). `check_fields.py`: 157 setup fields agree
  (was 156). `check_rules.py`: 34 rules / 73 controls, every rule has
  at least one. `gen_example_14.py --check`: OK, byte-identical.
- **`tools/selfcheck.py::check_boolean_grain_scoring`**, run in
  isolation (`python3 -c "import selfcheck as sc;
  sc.check_boolean_grain_scoring()"`, not via `make check-harness`):
  **PASS=5 FAIL=0**. A true match and a true nomatch at
  `grain="boolean"` both score `matched-as-expected` with `observed`
  absent; a false positive's `observed.span` is `None`, never `[None,
  None]`; two `grain="full"` controls (a spanless match still
  `wrong-span-or-captures`; an ordinary real-span match unchanged)
  prove the relaxation is grain-gated. `check_convention_scoring` was
  re-run alongside it as a regression control: PASS=4 FAIL=0, unchanged.
- **A real record through `store.write()`**, end to end, not merely
  through the reduced `outcome_for` fixtures: built a `testee_block`
  with `"grain": "boolean"` via `pcrecbench.record.build_setup` (the
  same builder `harness.run_cell` uses), ran the REAL `bench/email`
  sub-bench's own `orig`/`s-*` expectation through the REAL
  `outcome_for(..., grain="boolean")`, and wrote the result into a
  fresh temp scratch store. **Validated clean** (`store.validate_file`
  → `True`); `outcome` was `matched-as-expected` on a subject the
  pattern genuinely matches — the exact cell shape `vectorscan-block-
  nosom` could not write before this lane.
- **`pcrecbench quick` smoke on an EXISTING testee** (`pcre2-jit`,
  full grain, declares no `grain` key at all): `python3 -m pcrecbench
  quick --subbench email --pattern orig --regime search_short --testee
  pcre2-jit --subjects 5` — 5/5 pass, a real record written. Inspected
  the written setup line: `"grain" in setup["testee"]` is `False`
  (absent, as it must be) and `schema_version` is now `"1.6"` (the
  `SCHEMA_VERSION` bump above, confirmed live). Proves the full-grain
  path is unaffected by this lane end to end through the real harness,
  not merely by inspection of the diff.
- Cleaned up after every run: the temp scratch stores and the
  gitignored `bench/email/subjects`/`manifest.tsv`-regeneration
  artifacts were removed; `git status --short` in the worktree shows
  only this lane's own committed changes (verified: an accidental `rm`
  of the tracked `bench/email/manifest.tsv` was caught immediately by
  `git status` and restored with `git checkout --` before it was ever
  staged).

## 5. Reporter visibility — EXPLICITLY OUT OF SCOPE, deferred

No committed record anywhere carries `testee.grain = "boolean"` today
(nothing under `testees/` declares it yet — see §2's reconciliation
note), so nothing in any rendered report is wrong. `pcrecbench/
report.py` and `pcrecbench/reduce.py` are UNTOUCHED. When a boolean-
grain testee's first record lands (after `l6bvs`'s adapter gains the
one-line `describe()` addition §2 names), the reporter will need — at
minimum — a `grain=` legend clause beside `conventions=`'s own future
rendering (KB-5/KB-6's queued reporter wave is the right place for
both), and a stated caveat that such a testee's `matched-as-expected`
count is a weaker claim than every other testee's in the same row (the
same shape `reports/CLAUDE.md`'s existing reader's-caveat precedent for
the "8192 inversion" mis-reading takes). Nothing about THIS lane's
mechanism blocks that wave; it is additive and grain-gated exactly as
designed.

## OWED

1. **`make check-harness`** (and `make check` generally) — explicitly
   forbidden this session (HARD RULE: pcrec's battery owns the box).
   Command: `make check-harness` from the repo root. Expected: the new
   `check_boolean_grain_scoring` PASS lines appear in the count
   (5 more than the last confirmed run), everything else unchanged by
   this lane (`pcrecbench/report.py`/`reduce.py` untouched,
   `bench/*` untouched, `testees/*` untouched).
2. **The one-line `testees/vectorscan/adapter.py::describe()` addition**
   (`"grain": "boolean"`) that actually wires `vectorscan-block-nosom`
   to this mechanism — §2's reconciliation note. Not built here (the
   brief's explicit instruction); belongs to a fresh lane in
   `lane/l6bvs`'s lineage, or the manager's own merge-time edit.
3. **The reporter's `grain=` rendering** — §5's deferral, queued for
   the next reporter wave (KB-5/KB-6) alongside `conventions='s own
   still-unbuilt rendering (R5 B2, `capability_set_v1.md` §5.7).

## Files touched

- `pcrecbench/harness.py` — `_observed_span`, `outcome_for`'s `grain`
  parameter, `run_cell`'s `testee_grain` read/thread
- `pcrecbench/record.py` — `SCHEMA_VERSION` 1.5 → 1.6
- `schema/record.schema.json` — v1.6, `$defs/grain`, `testee.grain`
- `schema/validate.py` — rule X34
- `docs/design/record_schema.md` — version history, §5 ADDITIONS 8,
  field table, §6.10, §9 rule table
- `schema/examples/boolgrain-example@0.1__example-boolscan_1.0.0_block-nosom-nocaps-simd__example-box__20260917T120000Z.jsonl` — new
- `schema/examples/bad/x34-boolean-grain-nonnull-span.jsonl` — new
- `tools/selfcheck.py` — `check_boolean_grain_scoring`, wired into the
  dispatch list
- `schema/CLAUDE.md`, `schema/examples/CLAUDE.md`,
  `schema/examples/bad/CLAUDE.md`, `pcrecbench/CLAUDE.md`,
  `tools/CLAUDE.md` — updated
- `docs/dev/lanes/b44boolgrain_report.md` — this file

Not merged (the manager merges); branch `lane/b44boolgrain` is ready
for review.
