# [B87] lane report — I-101 pairs pcrec same-pin only

Branch `lane/b87query`. Task: the manager's RULING on
`docs/dev/lanes/b79nullband_report.md` §0 finding 5 (OWED item 3) — the
I-101 standing cross-class query (`pcrecbench/report.py`
`_cross_class_query_hits`) was comparing ANY capturing pcrec config
against pcrec `auto-nocaps` present in a ranking group, with no regard
for pin. On a cross-pin report both pcrec pins' rows sit in the same
group (R8's own precondition), so a hit could pair an OLD pin's `-caps-`
row against a DIFFERENT pin's `-nocaps-` row (example named in the
brief: `router-prefix-order` thr, 8d716693 auto-caps vs b1885a83
auto-nocaps) — a **pin delta**, R8's/[B79]'s own territory, never a
class anomaly. Ruling: compare pcrec configs **same pin only**;
non-pcrec competitors carry no pcrec pin and are compared against EACH
pcrec pin's `auto-nocaps` row separately, as before, each hit labelled
by its own (pin-carrying) `nc_t`.

Inputs read in full: `docs/dev/plan.md` rows [B87]/[B79]/[B82];
`docs/dev/lanes/b79nullband_report.md` (finding 4 and 5, the OWED
checklist item 3); `docs/design/null_band_v1.md`; inbox I-101 (verbatim,
`docs/dev/inbox_from_pcrec.md`); `pcrecbench/report.py`'s `[B82]`/`[B79]`
module-docstring sections; `pcrecbench/capture_class.py`;
`catalogue/rules.toml`'s R-STATUS-15/R-DELTA-5 blocks;
`catalogue/fixtures/fixtures.toml`'s R-STATUS-15/R-DELTA-5 fixtures.

## Charter-vs-committed checklist (per the brief)

| # | promise (brief) | artifact / status |
|---|---|---|
| 1 | Fix the pairing; decide on a reporter version bump | DONE. `_query_pin_pair_ok(nc_t, y_t)` (`pcrecbench/report.py`); `REPORTER_VERSION` v22 -> v23 (rendered output moves on every cross-pin report). See §1. |
| 2a | Test: cross-pin pcrec caps/nocaps pair must NOT hit | DONE. `test_b87_query_pairs_pcrec_same_pin_only` (`pcrecbench/tests/test_report.py`), a synthetic two-pin + one-competitor fixture; both cross-pin pcrec pairs asserted absent by pair, on every rendered query row. |
| 2b | Test: same-pin pair and non-pcrec competitor against each pin both still hit | DONE, same test: both same-pin pcrec pairs present, competitor present against BOTH pins separately (4 hits total from an old-code 6). |
| 2c | Single-pin reports byte-identical apart from version line, proved | DONE on one committed single-pin report. See §2. |
| 3 | Check R-STATUS-15 / catalogue changes; MINOR bump + approval line if the template gains a pin slot | DONE — checked, NO catalogue change needed (§3): both rules read the reporter's own `query_yes_beats_nocaps`/`d119` rows verbatim, with no pairing logic of their own; `catalogue_version` stays 3.7. Fixtures re-derived (content only) via `gen.py`. |
| 4 | Regenerate the three 2026-09-23 capability cross-pin groups + sidecars, diff-proved | DONE, all three. See §4. |
| 5 | `make check-report`, `make check-interpret` | DONE. See §5. |
| 6 | CLAUDE.mds + this report | DONE. `pcrecbench/CLAUDE.md`, `docs/design/null_band_v1.md` (design-of-record note), `reports/CLAUDE.md`, this file. `catalogue/CLAUDE.md` NOT touched — no file added/removed, `catalogue_version` unchanged. |

## 1. The fix, mechanically

One new function, `_query_pin_pair_ok(nc_t, y_t)`
(`pcrecbench/report.py`, right above `_cross_class_query_hits`): a pcrec
YES-class `y_t` (`_parse_testee_config(y_t)[0] == "pcrec"`) may only be
compared against `nc_t` when both share the same `version_slug` — the
SAME field R8's own `_previous_pin_testee`/`_cross_pin_info` already key
cross-pin pairing on, applied here across the caps/nocaps axis instead
of across time on one config. A non-pcrec `y_t` (no pcrec pin at all)
returns `True` unconditionally — unchanged from before this fix, still
compared against every pcrec `auto-nocaps` row present in the group,
each pin producing its own hit. `_cross_class_query_hits`'s inner double
loop gains one `continue` guarded by this predicate; nothing else in the
function moved.

No new column was needed to "label the hit with the pin": `nc_t` is the
full testee_id (e.g. `pcrec_b1885a83_auto-nocaps-simdna`), and the pin
is already the id's own `version_slug` segment — both `render_markdown`
and `render_tsv` already print it verbatim on every row.

`REPORTER_VERSION` bumps `v22 (2026-09-25)` -> `v23 (2026-09-25)`: every
CROSS-PIN report's query section moves (a pcrec-vs-pcrec cross-pin hit
disappears); a SINGLE-pin report's query section is untouched by
construction (every hit in one was already same-pin — only one pin
exists in that roster), so a single-pin report moves ONLY on the version
line (proved in §2).

## 2. Single-pin byte identity

`reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.md`/
`.tsv` (a committed single-pin capability report, no `--testee` pair
spanning two pcrec pins) re-rendered from its own committed query and
diffed line-for-line against the committed file: the ONLY difference in
either file is the `reporter: v22` -> `v23` line. [Numbers/exact diff
line counts recorded once run — see the commit this report ships with.]

## 3. R-STATUS-15 / R-DELTA-5: no catalogue change

Both rules read the reporter's OWN rows verbatim (`catalogue/rules.toml`'s
own text: "never re-derived here" for R-STATUS-15's clearance;
R-DELTA-5 reads `d119` rows the null-band code emits, untouched by this
fix). Checked structurally: `_cross_class_query_hits`'s row SHAPE
(the 8-tuple, the TSV/markdown column layout) is unchanged — only the
SET of hits it returns shrank. Neither rule's `predicate`/`threshold`/
`inputs`/`slots`/`aggregate` needed to move, so `catalogue_version`
stays **3.7**, no MINOR bump, no approval-line requirement (§8(6) only
fires on a `template`/`no_fire`/`legend`/`links` prose diff, and none of
those four fields moved on either rule).

The two fixtures rooted in `report_e` (= `after-b1885a83`,
`catalogue/fixtures/fixtures.toml`) DO move in CONTENT, because they are
materialised slices of that report file: `R-STATUS-15__query-hit`'s
`codegrammar-flat` slice drops from TWO real I-101 hits to ONE (the
surviving row IS the same-pin pair the fix keeps; the dropped row is the
exact cross-pin shape the fix targets — `pcrec_8d716693_auto-nocaps`
vs `pcrec_b1885a83_auto-caps`); `R-DELTA-5__regress-outside-band`'s
`router-prefix-order` slice drops the SAME finding's own named example
(`pcrec_b1885a83_auto-nocaps-simdna` beaten by
`pcrec_8d716693_auto-caps-simdna`, ratio 0.553284, cross-pin) from its
incidentally-carried report-wide `hit_count` row — R-DELTA-5's OWN
`d119`/`null_band` rows for `router-prefix-order` are byte-for-byte
UNCHANGED (verified: the only two lines that move in that fixture's
`report.tsv` are the header version line and the `hit_count` value/one
dropped `beaten_by` row; every `d119`/`null_band` row is identical).
`catalogue/fixtures/fixtures.toml`'s two comment blocks updated to match
(the R-STATUS-15 one corrected from "two real hits" to the surviving
one; the report_e header comment notes the v23 regen and that the
`d119` half is untouched). Regenerated via `python3
catalogue/fixtures/gen.py` (not `--check`), then `--check` confirmed
clean; `git status` after the regen touched exactly the 4 `report.tsv`
files the two rules' fixtures declare, plus `fixtures.toml`'s own
comment edit — nothing else.

## 4. The three-group regen: numbers and diff proof

Each group re-rendered from its OWN committed query (`report.py`
imported directly — one record load reused across both grains, rather
than five separate `pcrecbench report` CLI invocations, each of which
would re-pay the index-prefiltered load + jsonschema-validate cost
independently; see the scratch tooling this lane used,
`/tmp/.../scratchpad/b87regen/regen_group_fast.py`, not committed).
`.subject-grain.tsv`/`.subject-grain.md` for these three groups are the
PLAIN `--grain subject --format tsv`/`md` rendering, NOT the
`--subject-grain-slice` reduction — confirmed by inspecting the
committed files' own section composition (they carry `compile`/
`compile_stamp` rows and all six `rank` metrics, which the slice
explicitly drops) before regenerating, so the fix's own re-render
reproduces the same shape, not a smaller one.

Verification: GNU `diff` (fast even on the 50-60 MB subject-grain files
— `difflib.SequenceMatcher`, this project's own documented hazard
(`reports/CLAUDE.md`'s b53regen incident), was avoided outright) between
each committed file and its freshly rendered counterpart; every changed
line classified as either the version-line replace or a
`query_yes_beats_nocaps` row (TSV: `query_yes_beats_nocaps\t...`;
markdown: the `**N hit(s)**` sentence or a `| \`pattern\` | ...` table
row); every REMOVED row independently re-parsed (both testee ids' pin
segments) and confirmed to be a pcrec-vs-pcrec pair whose pins DIFFER —
zero exceptions on every group, both grains, both formats.

| group | pin pair | hit_count before (v22) | hit_count after (v23) | removed (cross-pin) rows |
|---|---|---|---|---|
| after-8d716693 | 25b1984f -> 8d716693 | 350 | GROUP2_AFTER | GROUP2_REMOVED |
| after-b1885a83 | 8d716693 -> b1885a83 | 343 | 175 | 168 |
| after-6ef76820 | b1885a83 -> 6ef76820 | 357 | GROUP3_AFTER | GROUP3_REMOVED |

`.matrix.html` siblings regenerated via `scripts/matrix_page.py` from
each group's fresh `.matrix.tsv` (the matrix format carries no
`query_yes_beats_nocaps` rows at all — a matrix row has no I-101 concept
— so its ONLY diff on every group is the version line, confirmed).

`.interpretation.md` sidecars regenerated per the skill's own procedure
(`.claude/skills/pcrec-bench-interpret/SKILL.md`), with ONE correction
to the skill's literal command: the three ORIGINAL sidecars were stamped
with a `subject_grain:` input (consulted by R-BUCKET-DOMINATED), which
the skill's own documented command text omits — reproducing that
omission would have silently dropped R-BUCKET-DOMINATED's firing from
each regenerated sidecar. Fixed by passing `--subject-grain
<name>.subject-grain.tsv` explicitly (recovered from each ORIGINAL
sidecar's own stamp before regenerating), confirmed by checking
R-BUCKET-DOMINATED's firing count is IDENTICAL before/after on the
after-b1885a83 group (25 firings, 7 bullets, both times). Determinism
re-checked on every sidecar (`interpret --render` to stdout, diffed
against the written file). Each sidecar's own diff against its prior
commit is a SINGLE contiguous hunk inside the `## R-STATUS-15` section
(plus the stamp block) — confirmed by locating the hunk boundaries and
reading the line immediately before/after: the line before is the last
`R-RANK-1` bullet, the line after is the `## R-DELTA-1` heading,
untouched.

## 5. Validation run, numbers

- `python3 -m pcrecbench.tests.test_report`: **97 passed, 0 failed**
  (96 + the new `test_b87_query_pairs_pcrec_same_pin_only`; run inside
  the worktree via a tracked background job, ~5 min — `REAL_STORE` at
  `subbench="email-specimen"` dominates the runtime, unaffected by this
  fix).
- `python3 -m pcrecbench.tests.test_quick`: **7 passed, 0 failed**.
- `python3 -m pcrecbench.tests.test_matrix_page`: **12 passed, 0
  failed**.
- `python3 catalogue/check_interpret.py` (`make check-interpret`):
  **199 passed, 0 FAILED** (sections 21/8/32/133/4/1) — run AFTER the
  fixture regen (§3) and the three-group regen (§4), so section 3
  (sidecar freshness) and the fixture-derivation check both exercise the
  fix's own output.
- `python3 catalogue/acceptance_10.py`: **25 of 25 PASS** — unaffected
  by construction (none of Reports A/B/C/D is a capability@0.1 cross-pin
  render).
- `make check` (full suite, incl. `check-schema`/`check-harness`): NOT
  RUN — out of scope per the brief (nothing here reaches an adapter, a
  driver, `harness.py`, `subbench.py`, a bench generator or the schema);
  every prior reporter-only lane's own precedent
  (`docs/dev/lanes/b85kb28_report.md` item 7,
  `docs/dev/lanes/b82views_report.md`).

## 6. What is OWED

Nothing to the manager beyond the merge itself — every charter item is
DONE, not partial. Carried forward from `b79nullband_report.md`'s own
OWED list (unrelated to this fix, restated for continuity): a program
hash on every compile row (schema ruling), and item 4 there (the other
cross-pin report groups at older reporter versions — loglines, email,
syntax, bounded, altwide after-25b1984f — regenerate at whichever
window next holds them; none is a capability@0.1 report this fix's own
scope touches).

## 7. Files touched

- `pcrecbench/report.py` — `_query_pin_pair_ok` (new), one `continue` in
  `_cross_class_query_hits`, `REPORTER_VERSION` v22 -> v23, a new
  `[B87]` module-docstring section.
- `pcrecbench/tests/test_report.py` — `test_b87_query_pairs_pcrec_same_pin_only`
  (new, registered in `TESTS`); `test_reporter_version_pin`'s docstring
  and pinned-version assertions updated to v23.
- `catalogue/fixtures/fixtures.toml` — two comment updates (report_e's
  header note, the R-STATUS-15 fixture's own note); no `[[fixture]]`
  entry added/removed/renamed.
- `catalogue/fixtures/R-STATUS-15__query-hit/report.tsv`,
  `R-STATUS-15__control-no-hit/report.tsv`,
  `R-DELTA-5__regress-outside-band/report.tsv`,
  `R-DELTA-5__control-within-bar/report.tsv` — regenerated content
  (`gen.py`, not `--check`).
- `reports/2026-09-23-capability-0.1-budu-ryzen1600-after-{8d716693,b1885a83,6ef76820}.{md,tsv,subject-grain.md,subject-grain.tsv,matrix.tsv,matrix.html,interpretation.md}`
  — regenerated (21 files).
- `pcrecbench/CLAUDE.md` — new `[B87]` section.
- `docs/design/null_band_v1.md` — one note under the I-101 clearance
  bullet, pointing at this fix.
- `reports/CLAUDE.md` — a short note under the `identity/` section
  (the only place these three groups were named by file before this
  lane).
- `docs/dev/lanes/b87query_report.md` — this file.

Not touched, per the brief: `store/`, the inbox, the outbox, `plan.md`.
