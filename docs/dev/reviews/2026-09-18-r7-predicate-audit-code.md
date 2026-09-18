# R7 — CODE REALITY review of `docs/design/predicate_audit_v1.md`

Read-only critic pass, D6 panel, lens: does every claimed code path exist
exactly as cited, and would every proposed fix actually work in the code
as written. No file touched except this one. No build, no store load, no
heavy run: `git diff`, direct reads of `pcrecbench/interpret.py`,
`pcrecbench/report.py`, `catalogue/rules.toml`, three probe re-runs (the
task asked for two), two from-scratch independent one-liners, and one
`make check-interpret` (~15 s, store-free).

**Verdict up front: the audit is code-accurate.** Every citation I
checked — and I checked essentially all of them, not a sample — resolves
to the exact lines claimed, with the exact behavior claimed. I found no
false code citation and no fix whose mechanism is actually broken. I did
find one real precision gap in the highest-priority recommended fix
(r7code-1) and one cosmetic labeling mismatch (r7code-2). Both are
WORTH-NOTING/SHOULD-FIX, not blockers.

## 0. The "mid-lane master move" hazard — checked, and it did not fire

The note's source header claims `HEAD = 4eb413a`. Current master is
`8a0ec37` (four commits ahead, all `[B42]` tail-charter merges).
`git diff 4eb413a HEAD --stat` touches only `docs/`
(the note itself, two lane reports, the eight probe files, two CLAUDE.md
files, `docs/dev/predictions/CLAUDE.md`, and
`capability-0.1-ext-roster.tsv`) — **zero changes** to
`pcrecbench/interpret.py`, `pcrecbench/report.py`, `catalogue/rules.toml`
or `catalogue/check_interpret.py`. So every line-number citation in the
note is checked against the byte-identical file the note was written
against; the "stale line numbers from a pre-move reading" failure mode
this review was asked to hunt for does not exist in this note's final
form. Confirmed by re-running `make check-interpret` (149/149 passed,
including the freshness section that re-renders every committed sidecar
from its recorded inputs and requires byte equality) — every sidecar the
note quotes is a current, non-stale rendering under today's catalogue.

## 1. Line-citation spot audit (all confirmed exact)

I pulled the actual source at every cited range for the four headline
fixes plus F27 and R-ARM-2, and a representative sample of the rest.
Every one matched exactly:

- `interpret.py:558-571` (R-STATUS-1 / F12): the `hit is None or hit[1]
  == "measured": continue` line is exactly line 566, confirming F12's
  "the `no_fire` asserts both halves ... and the predicate checks only
  the second."
- `interpret.py:945-948` (R-FLOOR-2 / F1): `floor_pattern = ...strip()`
  / the `not floor_pattern or == "none" or "," in` guard / `return
  "no-matching-rows"` are exactly lines 946-948.
- `interpret.py:1580-1581` (`render_markdown`'s no_fire pairing): exactly
  `for rule, token in not_fired: out.append(f"| {rule['id']} | {token}
  ({rule['no_fire']}) |")` — confirms F1's "the renderer always
  substitutes `no_fire`" for every token.
- `DID_NOT_FIRE_TOKENS` (line 88): exactly six bare strings
  (`no-matching-rows`, `input-absent`, `grain`, `reporter-version`,
  `no-registered-signatures`, `retired`) — confirms F1's "a closed set of
  six bare strings."
- `interpret.py:2035-2038` (R-DELTA-4 / F3): `rows = _select(view, p)` /
  `for r in rows: coverage.add(...)` is exactly there; `ctx.prediction_
  coverage` is set once at init (line 1298) and once after scoring (line
  2095) — matches F3's "built ONLY from clauses whose `_select` returned
  rows."
- `interpret.py:880-928` (R-ARM-1 / F9, F19): confirmed it reads `view.
  rows("rank", metric="median_ns")` and `("rank", metric="stddev_ns")`
  only — no `did_not_compile` read anywhere in the function. `float(r
  ["value"])` at lines 886 and 890 exactly, unguarded, as F19 claims.
- `interpret.py:1040-1089` / `:1062-1073` (R-BUCKET-SPAN / F11): `cell_
  rows` is built at lines 1047-1050 from `view.rows("rank",
  metric="median_ns")` only, and the `older` search over `cell_rows` at
  1062-1073 matches character for character.
- `report.py:2729-2752` (F11's reporter-side claim): `rd.record_ts_by_
  testee` and `rd.set_cells.get((sb, prev_tid, pattern_id, regime,
  form))` are exactly there. I traced `set_cells` to its single writer
  (`report.py:3328`, populated from `set_rows_by_key` before any
  rank/exclude split) — confirms "every reduction cell, rankable or
  not," independently of the note's own assertion.
- `report.py:4517-4520` (F10): `delta_verdict = ""` /
  `info = _cross_pin_info(...)` / `delta_verdict = info["verdict"] if
  info else ""` sit inside the `rankable` loop only, exactly as cited —
  the `others` loop (excluded/did_not_compile rows) never touches this
  variable.
- `report.py:4555-4564` (F26): the `did_not_compile` emission block is
  exactly there, and I traced `groups = _ranking_groups(rd, grain)`
  (line 4484) to `_ranking_groups`' single body (line 3462), which
  builds keys ONLY from `rd.set_cells`/`rd.match_cells` — structures fed
  by `set_rows_by_key`/`match_rows_by_key`, which in turn are populated
  only from rows the sub-bench actually reduced to a match result. A
  pattern with zero compiled testees never enters either dict, so it
  never has a `gkey`, so the did_not_compile emission — nested inside
  `for gkey in sorted(groups)` — never runs for it. This is F26's central
  structural claim and it is exactly right, verified independently of
  the note's own wording.
- `interpret.py:1787-1789` (F14's `explicit_section` gate) and
  `SELECTOR_KEYS` (line 1605-1606, exactly the seven keys named, no
  `metric`): both exact.
- `interpret.py:1700-1725` (`check_stated_utc` / F27): confirmed it
  iterates the **entire** `index.rows`, keyed only by `(subbench,
  version)`, taking the global minimum timestamp with no report-scoping
  and no supersession awareness — exactly the claim.
- `_measured_text` (F16, lines 2108-2118): `max(bad, key=lambda lv:
  abs(lv[1]))` and `max(reduced, key=lambda lv: lv[1])`, both direction-
  blind — exact.
- R-PRED-4's `slots` (`catalogue/rules.toml:1065-1110`, F8): exactly
  `["prediction_id", "source", "source_ref", "n_confirmed", "n_refuted",
  "n_not_evaluable", "clause_verdicts"]` — no `claim`/`measured`/
  `reason`. I additionally traced `evaluate_predictions` (lines 2071-2085)
  and `_pred_rule` (lines 1135-1163): `entry["claim"]`, `entry
  ["measured"]` and `entry["reason"]` **are already computed for every
  parent**, including `partial` ones, and are sitting unused one branch
  away from where `_pred_rule`'s `want == "partial"` arm builds its
  `fire()` dict. F8's claim that this is "the cheapest large win" is
  code-verified: the fix is three extra dict keys plus three slots plus
  a template edit, not a new computation.

## 2. Corpus/count claims — independently re-derived, all exact

- 31 `[[rule]]` blocks (`grep -c` on `rules.toml`) and 17
  `QUANTITIES` (imported `pcrecbench.interpret.QUANTITIES` directly) —
  both match the note's "31 catalogue rules... 17 prediction-scoring
  quantities" exactly.
- 45 set-grain report TSVs, 3 `.subject-grain.tsv` slices, 3 predictions
  files with 19+15+35 = 69 clause rows, 6 `.interpretation.md` sidecars —
  all match §0's corpus census exactly, counted by my own `ls`/`wc`, not
  by re-running a probe.
- **Foundational P5-class claim, re-derived with a bare `awk` one-liner
  that imports nothing from `pcrecbench`:** 103,488 `rank` rows
  corpus-wide, **0** with `n_wrong>0` or `n_gave_up>0` (columns 15/16 of
  the fixed `REPORT_COLUMNS` order, read directly off the TSV). Matches
  §0 fact 1 exactly, via a path that shares no code with `_select`/
  `_keyed_values`/`RuleView` at all — a genuine second implementation,
  not a re-run of the note's own probe.
- **The two "inert population" claims (`not_ranked`/`scratch` = 0 rows
  in all 45 committed reports), re-derived the same way** — a raw
  `split('\t', 1)[0]` first-column check across every report file,
  again sharing no code with `interpret.py`: **0** rows. Confirms F25
  and the `not_ranked`/`scratch` premise every R-ARM-2/F9/F10 argument
  depends on.

## 3. Probe re-runs (three, not two)

- **Probe 7** (`2026-09-18-predicate-audit-probe7.py`, the F26/M7 basis):
  re-run output byte-identical to the archive, including the final line
  `total (report, pattern) pairs invisible to R-STATUS-4: 29` and every
  per-report breakdown (the ext sidecar's 2 patterns, the bounded-0.3
  `cls-upto-65535` case, the 11/14-pattern altwide walls).
- **Probe 2** (M2/M3/M5/M6/M8): re-run output byte-identical to the
  archive after accounting for the section-boundary line my extraction
  script introduced. Confirms the **532** R-ARM-1 blind triples (F9), the
  **38** R-DELTA-1-blind cross-pin pairs (F10), P5.a's 321
  rows/66 cells/3-counterevidence-row breakdown (F13's basis), the two
  `floor_pattern: none` reports (F1's witness count), and `not_ranked`/
  `scratch` = 0 (M8).
- **Probe 1** (M1, the §0 structural facts): re-run output byte-identical
  to the archive line for line — the per-section always-empty column
  lists, the "6 rows/cell: 17,248 cells" line, and the floor_pattern
  header-value histogram.

## 4. Committed-sidecar witness quotes — checked byte-exact

Every quoted sidecar sentence I checked reproduces exactly at the cited
location:
- F1's `R-FLOOR-2 | no-matching-rows (no ranked cell is at or below its
  set's own floor pattern...)` at
  `.../2026-08-25-...-repin-692c2e8.interpretation.md:152`, with the
  report's own header confirming `floor_pattern: none`.
- F3's R-DELTA-4 quote (found under the aggregated bullet header
  `## R-DELTA-4 — a finding no prediction covers`, sub-bulleted by
  `rule_id × regime` — "R-DELTA-1 × large-subject-throughput" is
  correctly an R-DELTA-4 firing about an R-DELTA-1 finding, not a
  mislabel; I confirmed this via the aggregate-key convention before
  concluding the citation was right).
- F6/F7's P1.a "over 18 value(s)", P5.a "over 321 value(s)", and P13
  "over 834 value(s)... also present in: did_not_compile (172),
  excluded (23)" — all four numbers exact, in two different sidecars
  (capability and syntax).
- R-ARM-1's `legend` field (`catalogue/rules.toml:788`) and R-STATUS-3's
  inline trials-vs-subjects clarification (`rules.toml:191`) — both
  "model to copy" claims in §5 confirmed as the literal template text.

## Findings

### r7code-1 — SHOULD-FIX. F27's fix shape names the wrong join for "closing the supersession window"

F27 (and Q7, "recommend YES, and first" — the single highest-priority
item in the whole note) proposes: anchor `check_stated_utc` to the
earliest index timestamp of *the records this report includes*, "with
the supersession window closed by including any index row superseded by
one of them," citing "the join R-STATUS-1 and R-BUCKET-SPAN already
use."

That join (`record_id_of(index_row)` against a report's `record` rows,
used identically by both cited rules) recovers exactly the *included*
records' own index rows — it does **not** recover which OTHER index rows
those records superseded. I checked where the superseded-record mapping
actually lives: `report.py` computes it transiently inside `dup_groups`
processing (`report.py:3166-3206`, `superseded.append((kept_r.setup
["record_id"], [older record_ids]))`), and the **only** place it survives
into the committed TSV is a scalar count in the header (`report.py:4446`,
`f"superseded: {sum(len(v) for _k, v in rd.superseded)}"`). The
kept→superseded id mapping itself is discarded after rendering. So a
reader implementing F27 literally — "the join those two rules use" — gets
the report-scoped earliest timestamp with **no** supersession extension
at all, which is not what F27 promises to fix.

The good news: the fix is still achievable without a reporter change,
just not via the record_id join. OD-B15's own dedup key is `(subbench@
version, testee_id, machine_id)` (`report.py:3166-3168`), and `index.
tsv` carries `testee_id` and `machine_id` directly (`INDEX_COLUMNS`,
`interpret.py:67`). So the correct construction is: for each of the
report's included records, take its `(subbench, version, testee_id,
machine_id)` tuple (via the record_id→index-row join `check_stated_utc`
would gain from `report`), then take the minimum index timestamp over
**every** index row sharing that tuple — which recovers the superseded
population by the OD-B15 grouping key, with no need to read the
reporter's discarded mapping and no store load. This is a different
(second) join from the one F27 cites, one line longer, and entirely
within KB-16's "the interpreter never loads the store" constraint — but
the note doesn't name it, and a panel or implementer taking the note's
"the join those two rules already use" at face value will ship a fix
that silently doesn't close the window it claims to close, on the
**first** fix this note asks to land. Also worth a one-line note in the
fix shape: `check_stated_utc(predictions, index, where=...)` has no
`report` parameter today (`interpret.py:1700`), so the fix needs a
signature change at the one call site (`interpret.py:2159`) as well as
the new join — trivial, but the note's "Code only" framing doesn't
mention it.

**Evidence**: `report.py:3166-3206`, `report.py:4446`, `interpret.py:67`
(`INDEX_COLUMNS`), `interpret.py:1700-1725`, `interpret.py:2149-2159`.

### r7code-2 — WORTH-NOTING. §0's M1/M4/M7 probe labels are the note's own bookkeeping, not literal probe output

§0's table (lines 71-79) labels seven measurements M1-M7 (skipping
nothing) as "what was measured." The archived
`2026-09-18-predicate-audit-probes.txt` only prints literal `M2`, `M3`,
`M5`, `M6`, `M8` section headers (all inside `probe2.py`'s output); `M1`
(probe1.py's structural census), `M4` (split across probe3.py's and
probe4.py's several `====` sections with no numeric label), and `M7`
(probe7.py, headed only by `########## probe7.py ##########`) never
appear as that literal string in the archive. A reader `grep`-ing the
archive for "M4" to find its evidence will find nothing under that name
— they have to know M4 means "probe3.py + probe4.py." This does not
affect any number's traceability (I confirmed every M-labeled claim
independently above, including M1/M4-equivalent/M7 content), and it is
purely a labeling mismatch between the design note's own summary table
and the archive it points to. Not worth blocking on; worth a one-word
fix (drop the M-numbers from §0's table, or add them as comments in the
scripts) the next time the file is touched.

### r7code-3 — WORTH-NOTING (positive finding, stated for the record). No blocking code-reality defect found

I checked every code citation behind F1, F3, F4, F8, F9, F10, F11, F12,
F14, F16, F19, F26, F27, R-ARM-1's legend, R-STATUS-3's template, R-
FLOOR-2's template, `SELECTOR_KEYS`, `DID_NOT_FIRE_TOKENS`,
`_ranking_groups`, `set_cells`'s population, and `_pred_rule`'s branch
structure, against the actual file at the current commit — not a sample,
essentially the full set the brief asked for plus more. Every citation
resolved to the exact line range with the exact behavior claimed; every
proposed fix's minimal implementation is a real, findable seam in the
existing functions (R-ARM-2's multi-section `inputs` pattern already
exists verbatim in R-PRED-4's eight-section declaration; F8's three
missing slots are sitting one branch away from where they're needed;
F26's fix slots into the reporter's existing `did_not_compile_by_
pattern` structure with one new pass). The §6 cost-grouping (code-only /
MINOR+regen / MAJOR / reporter-wave / the one gate) matches
`interpreter_v1.md` §3.3's stated versioning bar in every case I checked,
including the genuinely open Q2 (MINOR vs MAJOR when catalogue prose is
right and code is wrong) — that ambiguity is real in the discipline as
written, not a note error.

## Summary

**3 findings**: 0 BLOCKING, 1 SHOULD-FIX (r7code-1: F27's cited join
does not by itself close the supersession window it claims to; a correct
code-only construction exists but is a different join, unstated), 2
WORTH-NOTING (r7code-2: cosmetic M-label mismatch between §0's table and
the probe archive; r7code-3: a clean bill of health recorded for the
panel's benefit — every other code citation and fix-mechanism I checked,
which is nearly all of them, holds exactly as claimed). Three probes
re-run byte-identical to the archive (probes 1, 2, 7); two structural
claims re-derived with from-scratch one-liners sharing no code with
`interpret.py` (the 103,488/0 `rank` census, the 0-row `not_ranked`/
`scratch` census); `make check-interpret` green (149/149) confirming
every quoted sidecar is a current, non-stale rendering.
