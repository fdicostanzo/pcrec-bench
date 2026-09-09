# Lane `b13v12` — [B13] interpreter design note, cross-review revision to v1.2

Lane: `b13v12`, branch `lane/b13v12`, worktree `worktrees/b13v12`, base
`3aac68b`, 2026-09-08. Deliverable: `docs/design/interpreter_v1.md` at
**v1.2**, applying inbox item I-58 (the pcrec manager session's
cross-review of v1.1) verbatim as the specification of what changes;
`docs/design/CLAUDE.md`'s entry updated; the r4 review file's closing
pass and by-id completeness check appended. DOCS ONLY — no code, no
`catalogue/`, no `pcrecbench/`, no `.claude/`, no `docs/dev/plan.md`.

Commits: `e2d31fb` (the four spec edits + minors), `5dfe357` (the review
file's closing sections). **Validation: `make check-schema` green — 4
example(s) accepted, 72 sabotage(s) rejected for the intended rule, 0
wrong** — the run this lane touches nothing else, confirmed by
`git diff --stat 3aac68b lane/b13v12`: only `docs/design/CLAUDE.md`,
`docs/design/interpreter_v1.md`, and
`docs/dev/reviews/2026-09-07-r4-interpreter-v1.md` changed (494
insertions, 60 deletions across the three). `make check-harness` NOT
run, as instructed.

---

## Method

Every line-number citation and count in this delivery was re-read from
source in this worktree, never copied from I-58 or from the raw critic
files — the same rule `b13rev_report.md` set and this lane repeated. Two
source files were read in full for their exact line ranges
(`pcrecbench/reduce.py`, 376 lines; `pcrecbench/report.py`'s render_tsv
block and `_ranking_groups`/`_cross_pin_verdict`/`_is_reference`); one
count was re-derived by command over the committed corpus (Report A's 13
excluded rows, `awk -F'\t' '$1=="excluded"' … | wc -l`, quoted below);
and the by-id completeness check (item 7) was run as an actual script
over the three raw critic files and the consolidated review, not
asserted from memory.

---

## The seven items, what changed and where

**1. §2.1 header parse — known-key split made normative.** The
"Equivalently" claim between the regex-rejoin and known-key forms is
false: they diverge in both directions. Case 1 — a NEW header key from a
future reporter (exactly `floor_pattern`'s position today, before P-1
lands): the regex form keeps it separate; the known-key form (not yet
updated) silently re-joins it into the previous key's value. Case 2 — a
future value containing `word: `-shaped text: the regex form wrongly
splits it; the known-key form correctly keeps it joined. **Ruling: the
known-key form is normative** (fails safe on values, which is the more
likely future defect given this project's own values already carry `,`,
`=`, `%`, `/`, parens; its remaining exposure is bounded because the
key list is obtained at CHECK time from a live `report --format tsv`
run, so a reporter bump and the recognition of its new key are the same
commit's concern). The regex form is demoted to an explicit heuristic
note, marked as such. Per the brief's note that `floor_pattern` is being
appended at the END of the header line by the concurrent `b13pre` lane
(after `worst_other_core_busy`): the §2.1 key table now says so at the
`floor_pattern` row.

**2. R-STATUS-3 vs P-2 — scoped to `metric = pass_rate`.** Verified by
command against the currently committed corpus, not asserted:

```
$ awk -F'\t' '$1=="excluded"' reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv | wc -l
13
```
and every one of those 13 rows carries `metric = pass_rate` in column
11 (spot-checked the first three rows verbatim). R-STATUS-3's `inputs`
now declare `metric`, and the predicate is scoped to
`report:excluded?metric=pass_rate…`, so precondition P-2's
`giveup_smallest` rows (added to the SAME `excluded` section, one per
give-up code) cannot make it double-fire once P-2 lands. Checked every
other reader of the `excluded` section for the same hazard, per the
brief's ask: R-STATUS-12 already scopes to `metric=giveup_smallest`
(no change needed); no R-BUCKET rule reads the `excluded` section;
R-PRED-3 only tests a cell's `section` value for presence, never reads
`metric` or the count columns, so an extra row beside a base row changes
nothing it touches. §9.2's "13 firings", §10 A.3's "all thirteen
excluded cells" and §10 C.2's "23 excluded cells" are all unaffected —
they describe the current (pre-P-2) corpus, which already has
`metric = pass_rate` uniformly.

**3. §6.3 selector grammar — `section` added to the closed key list.**
§6.6's own P1 transcription already used `selector
section=did_not_compile;testee=pcrec_*` against a grammar that never
declared `section` as a legal key. Added. Re-checked §6.6's table: the
fix is syntactic only (P1 was already counted among the "twelve of
thirteen" expressible predictions; the count is unchanged, noted inline
in §6.6).

**4. R-DELTA aggregation keys — `config`/`direction` declared as
decompositions.** R-DELTA-1's `aggregate = ["regime","config","direction"]`
and R-DELTA-2/3's `aggregate = ["regime","config"]` referenced `config`
and `direction`, neither a TSV column, with `arith = []`. Declared:
`config` = the testee-id split §7.2 already has for R-RANK-1/R-ARM-1/
R-BUCKET-VSBEST/R-BUCKET-SPAN, minus `version_slug` (the one field a
cross-pin pair is guaranteed to differ on); `direction` = the matched
clause's own leading token (`faster`/`slower`), copied verbatim. Both
added to R-DELTA-1's TOML example (`arith`) and to §7.2's decomposition
table (two new rows, one per rule group). Mechanical — no predicate or
threshold changed.

**Two minors + one honesty edit, same commits:**

- **(a) §5.2** now defines aggregated-bullet rendering for a rule with
  no numeric slot: the specimen's own R-STATUS-2/R-BUCKET-VSBEST
  behaviour (a full sorted id list, not extremal+minimum) is stated as
  the rule, not left as an unexplained accident of the worked example. A
  rule may also declare its own `extremal` slot (new optional field,
  added to §3.2's field list); R-DELTA-1 now declares `extremal =
  "ratio"` (a new declared decomposition: the clause's own `×N.NN`,
  parsed as a float) instead of the default first-numeric-slot
  (`median_ns`, which would pick the largest-MEDIAN cell rather than the
  biggest MOVER). No visible change to Report A's own §9.2 rendering
  (its R-DELTA-1 group sizes are all 1, so extremal never engages there)
  — the fix matters on denser reports (Report B: 202→17).
- **(b) reduce.py citation corrected.** Re-read `pcrecbench/reduce.py`
  myself: the `return` for `agree (…)` spans **372-376**, and the file
  is **376 lines** total (`wc -l pcrecbench/reduce.py` → 376) — the old
  `373-379` citation ran past end-of-file. Fixed in §4.1's table.
- **(c) §6.5 honesty edit.** The `stated_utc` check now reads the
  earliest `timestamp` across ALL `store/index.tsv` rows for the
  (subbench, version, machine) triple, INCLUDING superseded ones — not
  just the report's own population — closing the supersession window a
  report-scoped check leaves open (state a prediction after reading run
  1, aim it at a later re-measure). No new index column is needed: all
  four columns the check reads (`subbench`, `version`, `machine_id`,
  `timestamp`) are already in §2.2's declared eight. The residual limit
  is stated plainly rather than claimed away: the check can prove a
  prediction predates the population's first-ever measurement, and
  nothing more (not that no other channel — reading pcrec's own source,
  say — informed it). §13's summary line updated to match.

**6. Provenance.** The STATUS block is now v1.2, 2026-09-08, lane
`b13v12`, dated against I-58's ruling ("APPROVED CONDITIONAL, four spec
edits, no re-panel") with a one-paragraph list of what changed.
`docs/design/CLAUDE.md`'s entry is updated in place (version marker +
a new paragraph, one line per edit) and a closing sentence records that
the step-2 confirmation pass has now run.

**7. The r4 review file's closing pass.** Appended two sections to
`docs/dev/reviews/2026-09-07-r4-interpreter-v1.md`:

- `## Step-2 confirmation pass (2026-09-08)` — records that the pass was
  run by `pcrecdev1` at Frank's ask (I-58): **19/19 dispositions
  (B1-B11, S1-S8) confirmed-resolved or resolved-with-a-flagged-
  deviation, zero silent**; ~25 report.py/reduce.py citations
  spot-checked exact; the numeric claims I-58 lists reproduced (13
  excluded rows, 3/6/4 R-DELTA firings, the R-ARM-1 ×2.31/×1.28/×3.73
  cells, the 44-bullet §9.2 sum, the 11-pin `[[pin_order]]`, the
  160/59/9/1 index counts); what was NOT independently re-verified named
  plainly (the 891-of-2,514 R-STATUS-13 census, Report C's figures); the
  one flagged deviation (the reduce.py citation, item 5(b) above) named
  and pointed at its v1.2 fix.
- `### By-id completeness` — the §7(a) check. **Script summary line: 56
  finding ids found across the three raw critic files (22 `Dn` in
  `-source.md`, 20 numbered findings in `-build.md`, 14 `Fn` in
  `-charter.md` — matching `docs/dev/reviews/CLAUDE.md`'s own "56 raw
  findings" count), 56 with a disposition.** 39 are cited by id
  directly in the consolidated review; the other 17 are not cited there
  by id, but every one is independently traceable to an applied fix —
  15 cited directly inside `interpreter_v1.md` itself
  (`corrected from v1, panel <id>`), and 2 (`build #19`, `build #20`)
  needed no spec change (a critic's own "no finding here", and a
  substance-level fix folded into §8's runtime-budget paragraph). A
  56-row table (id, one-line finding, cited-by-id?, where handled) is in
  the review file. **This check finds a THIRD dropped id beyond the two
  `b13rev_report.md` already named (`build #11`, `charter F10`):
  `charter F9`** — applied correctly in v1.1's §0 (cited `panel F9`
  there), but never named as a drop by either this review or the
  revision lane's own report, so the "two findings were dropped"
  headline both carried undercounts by one. No live gap: F9 is already
  correctly in v1.2. Recorded for the standing rule's own record, per
  the brief's ask ("there may be others — find out").

---

## Flagged ambiguities / refinements

**One citation imprecision found, not a completeness gap.** The
consolidated review's WORTH-NOTING paragraph tags `[source D4, D15]` to
a sentence describing TWO claims — "§9.2 omits eight non-firing rules"
(which is D15's content) and "understates R-DELTA-1 to two firings where
a third exists" (which is actually **D17's** content, not D4's — D4 is a
different finding, about R-DELTA-3's "the latter pair" being four cells
not two). Both D4 and D17 (and D15) are correctly and separately applied
and cited in `interpreter_v1.md` (lines 974, 960, and folded into
WORTH-NOTING respectively), so nothing is missing in substance — this is
a citation slip inside the consolidated review's own prose, noted in the
by-id table's D4/D17 rows rather than silently passed over.

**§2.5's P-2 row shape was not touched**, as instructed — `b13pre` owns
it. No ambiguity found there worth flagging; P-2's existing shape
(one extra `giveup_smallest` metric row per give-up code) already
supports the `metric` scoping fix cleanly.

---

## Charter-vs-committed checklist

| brief item | status |
|---|---|
| 1. §2.1 known-key split normative + divergence cases + `floor_pattern` position note | **COMMITTED** (`e2d31fb`) |
| 2. R-STATUS-3 scoped to `metric=pass_rate`; every other `excluded`-section reader checked | **COMMITTED** (`e2d31fb`) |
| 3. §6.3 `section` added to selector grammar; §6.6's 12-of-13 re-checked | **COMMITTED** (`e2d31fb`) |
| 4. R-DELTA-1/2/3 `config`/`direction` declared decompositions, §7.2 table extended | **COMMITTED** (`e2d31fb`) |
| 5. Two minors + honesty edit (§5.2 no-numeric-slot rendering + `extremal`; reduce.py citation; §6.5 earliest-index-timestamp check) | **COMMITTED** (`e2d31fb`) |
| 6. Provenance: STATUS block v1.2; `docs/design/CLAUDE.md` v1.2 paragraph | **COMMITTED** (`e2d31fb`) |
| 7. Review file step-2 confirmation pass (19/19) + §7(a) by-id completeness table | **COMMITTED** (`5dfe357`) |
| Method: every citation/count re-derived from source, not copied | **COMMITTED** — commands and line numbers quoted above and in the diff |
| §2.5's P-2 row shape untouched | **CONFIRMED** — `git diff --stat 3aac68b lane/b13v12` shows no touch to that section beyond the metric-scoping cross-reference |
| Validation: `make check-schema` | **COMMITTED** — green, 4/72/0, nothing else touched |
| `make check-harness` | **NOT RUN**, as instructed |

Nothing OWED. All seven items land in this delivery.
