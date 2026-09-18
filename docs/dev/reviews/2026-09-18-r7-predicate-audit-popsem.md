# R7 — population semantics / measurement validity critique of `predicate_audit_v1.md`

Read-only D6 panel lens, run against `docs/design/predicate_audit_v1.md` as
merged (`HEAD` = `8a0ec37`, catalogue 2.0, reporter v17, `interpreter_v1.md`
v1.4). Method: independently re-derived the code paths behind F1, F3, F4,
F26, F27 and the two "audited CLEAN" narrowings directly against
`pcrecbench/interpret.py` and `pcrecbench/report.py` as committed (not the
note's prose); re-ran all seven archived probes
(`docs/dev/measurements/2026-09-18-predicate-audit-probe{1..7}.py`) fresh
and diffed their output against the committed
`2026-09-18-predicate-audit-probes.txt` (byte-for-byte match on every
number quoted below); re-ran the F27 witness command live against the
current store; and hand-verified two of the note's own proposed FIXES
(Q4's row-collapse, Group 3's R-BUCKET-SPAN widening) against the actual
reducer/join code to check whether the remediation itself introduces a new
population gap of the same class the note is auditing for.

**Bottom line.** F1, F3, F4, F26 and F27 all check out: every code
citation, every quoted rendered sentence, and every corpus count I
re-derived (45 reports / 3 subject-grain slices / 3 predictions files / 69
clause rows / 6 sidecars; the 532 arm triples; the 38 cross-pin pairs; the
33/8/25 R-BUCKET-DOMINATED split; the 29 R-STATUS-4-blind pairs; F27's live
`PredictionError`) reproduced exactly, and the two "audited CLEAN"
narrowings (F23, F24) hold up mechanistically, not just by corpus
coincidence — I traced `_jitter_flag`/`_pstdev_safe` far enough to confirm
F23 is clean by construction (a single-trial *compiled* cell gets
`stddev_ns = 0.0`, not `None`, so it never falls into the "no jitter row"
bucket the omitted-population claim is about). The five findings below are
about places where the AUDIT'S OWN reasoning — mostly in its proposed
fixes — either overstates a population risk, understates one it just
fixed, or quietly reproduces the P5 class it exists to catch.

---

### r7pop-1 — BLOCKING. §7 Q4's "MEASURED" justification cites no probe and is contradicted by hand computation for the reducer it names

Q4 recommends collapsing the six identical rank metric rows to one per
cell for the four failure quantities, and backs it with: *"MEASURED: P5.a
still refutes, P1.a-c still confirm... and changes every
count/median/max/min one — which is the point"* (`predicate_audit_v1.md`
§7 Q4). This is the single most consequential fix the note proposes (a
MAJOR bump touching all 17,248 rank cells' reduction), and it is the one
number in the note I could not verify.

- **No probe backs it.** `grep -n "still refut\|still confirm\|collapse"
  docs/dev/measurements/2026-09-18-predicate-audit-probes.txt` returns
  nothing. None of the seven probe scripts implements the row collapse or
  re-evaluates P1/P5 under it. The note's own closing discipline states
  *"Every contested number is marked MEASURED and traceable to a named
  probe"* (source header, last paragraph) — this number is marked MEASURED
  and is not traceable to any of the seven.
- **Hand re-derivation contradicts the "changes every ... median ... one"
  half.** From probe2's own already-verified output (re-run live, matches
  the archive): P5.a selects 321 `n_wrong` values, 318 zero and 3 at
  10.000 (`by_section={'rank': 306, 'excluded': 15}`, "rows with
  n_wrong>0: 3"). `_reduce`'s `median` branch is `nums[len(nums) // 2]`
  after `sorted(...)` (`pcrecbench/interpret.py:1880-1886`). Sorted
  ascending, the 3 tens sit at the top; index `321//2=160` lands inside the
  318 zeros → **median = 0**. Collapsing the six duplicate rank rows to one
  per cell (Q4's own proposal) turns this into 51 rank + 15 excluded = 66
  values, 63 zero + 3 at 10.000; index `66//2=33` still lands inside the 63
  zeros → **median = 0, unchanged**. The collapse moves the ratio of clean
  to dirty rows from 318:3 (106:1) to 63:3 (21:1) — still an overwhelming
  majority, and the `median` reducer's picked *value* does not move at
  all, let alone flip a verdict. The collapse fixes F6's row-count
  inflation (the point of "over N value(s)"); on this evidence it does
  **not** fix the median-invisibility hazard F13 uses to justify adopting
  it — that needs the load-time check F13's own fix-shape paragraph
  separately proposes ("a load check refusing an averaging reducer on a
  failure quantity"), not the collapse alone. Recommend: either produce
  the missing probe (an eighth, re-running `evaluate_predictions` under a
  collapsed view) or drop the "changes every ... median ... one" clause
  from Q4's justification, since as stated it is unverified and, for the
  one case I could check by hand, false.

### r7pop-2 — SHOULD-FIX. F13's "median, count, max or min" grouping overstates which reducers actually hide a violation

F13 states: *"With `median`, `count`, `max` or `min` the clean rank rows
outweigh the counterevidence 100-158:1 and a real failure can be
arithmetically invisible."* Read against `_reduce`'s own code
(`pcrecbench/interpret.py:1873-1874,1880-1886`) with the op actually used
on this quantity in the corpus (`eq 0`, P5.a's own clause,
`docs/dev/predictions/capability-0.1-first.tsv:10`):

- **`max`** picks `nums[-1]`, i.e. the single WORST value in the
  population. For an `n_wrong eq 0` hypothesis, if even one row is
  nonzero, `max` returns it and the clause correctly reads *refuted*
  regardless of how many thousands of clean rows dilute the population.
  `max` is the reducer **least** susceptible to the class F13 names, not
  one of the four vulnerable ones — for a "no failures anywhere" claim it
  is the closest thing this catalogue has to `identity`'s own per-row
  guarantee.
- **`count`** (`len(values)`, line 1874) never reads the quantity's VALUE
  at all — it counts selected rows. Whatever hazard exists in "some
  clauses' row counts are inflated 6× or diluted by the (α) widening" is
  F6's row-inflation finding, not a value-dilution finding; folding it
  into the same sentence as `median`/`min` conflates two different
  problems under one severity number ("100-158:1").
- Only `median` (verified above, r7pop-1) and, for an `eq`-style
  hypothesis, `min`'s weaker existential semantics (`min eq 0` proves "at
  least one row is clean," a near-vacuous claim when most rows are clean
  by construction, not "the failure is invisible" in the same sense) are
  actually vulnerable the way F13 describes.

Lumping all four together risks the panel either widening Q4's scope
further than the evidence supports, or discounting the real `median`
hazard by association with two reducers that are not actually at risk.

### r7pop-3 — SHOULD-FIX. Group 3's fix for F11 (widen R-BUCKET-SPAN) reproduces the P5 class inside its own remedy

Group 3 proposes, for F11: *"Widen the partner search to `excluded` and
`did_not_compile`."* `r_bucket_span` groups candidate partners by
`by_cell[(r["pattern"], r["regime_or_na"], r["form"])]`
(`pcrecbench/interpret.py:1050`) — the JOIN KEY includes `form`. The
note's own §0 fact 3 (re-verified via probe1, re-run live: `did_not_compile
rows= 1,416 ALWAYS-EMPTY: form,fact,tier,...`) establishes that a
`did_not_compile` row's `form` column is unconditionally empty. Under the
literal fix as scoped, a `did_not_compile` row can therefore never satisfy
the same `(pattern, regime, form)` key a ranked row groups under — the
join silently never fires for that half of the widened population, no
matter how the search itself is widened, because the KEY excludes it
before the search runs. Only the `excluded` half of Group 3's proposal
(whose rows do carry `form`, per the same fact 3) would actually become
reachable; the `did_not_compile` half needs its own join re-keyed to drop
`form` (or to fall back to `(pattern, regime)` when the candidate section
is `did_not_compile`), which neither §6 Group 3 nor Q2's discussion
mentions. This is exactly the audit's own P5 shape — a population widened
in name that cannot structurally contain the counterevidence it claims to
add — occurring inside the fix meant to close F11.

### r7pop-4 — SHOULD-FIX. Q7's re-anchoring fix for F27 narrows the population and reopens a cross-testee look-ahead gap it doesn't name

F27 itself is confirmed live and exactly as quoted: re-running
`python3 -m pcrecbench interpret --predictions
docs/dev/predictions/capability-0.1-ext-roster.tsv
reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.tsv --index
store/index.tsv` raises the identical `PredictionError` the note quotes,
byte for byte. Q7 recommends anchoring `check_stated_utc` to *"the
earliest index timestamp of the records THIS REPORT actually includes...
with the supersession window closed."* This is a real fix for the bug as
demonstrated, but it trades the check's current (unusable) over-caution
for a narrower population without saying what that narrowing gives up.

`check_stated_utc` only ever compares `stated_utc` against the EARLIEST
timestamp of its anchor population (`pcrecbench/interpret.py:1707-1712`,
`if key not in earliest or ts < earliest[key]`); scoping that population
down to "records this report includes" makes the anchor exactly as recent
as whatever the report's own `--testee`/`--since`/`--until` filters happen
to admit — a fact about the QUERY, not about the (subbench, version)'s
real measurement history. Verified live on the AFTER report itself: its 11
included records span **2026-09-17T00:50:53Z** (the FIRST-sample baseline
testees, `libpcre2_10.46_interp-caps-simdna` etc.) to
**2026-09-18T02:51:49Z** (the fresh `cf0962e3` pin's own samples) — in this
particular report the two anchors happen to coincide because the report
includes the corpus-earliest record too, but a report scoped (by filter,
not by the store's own state) to exclude that older baseline would move
the anchor forward to the newest pin's own earliest record, and would then
accept a `stated_utc` authored after the analyst had already seen results
from OTHER, differently-configured testees of the SAME (subbench, version)
that the report's filters simply chose not to include. This is the same
"residual limit" `interpreter_v1.md` v1.1 named once already for a related
supersession gap (cited approvingly by F27 itself). The proposed fix
closes the SAME-testee supersession half of that residual (explicitly, via
"the supersession window closed") but not the cross-testee/cross-config
half, and Q7 does not say so — it should, since Frank's directive is
specifically that a result should "carry the context around its numbers."

### r7pop-5 — WORTH-NOTING. F1's "one mechanism" fix-shape is worked out for one of `r_floor_2`'s three collapsed causes, not all three

`r_floor_2`'s single early return
(`pcrecbench/interpret.py:946-948`: `if not floor_pattern or floor_pattern
== "none" or "," in floor_pattern: return "no-matching-rows"`) conflates
THREE distinct causes into one token: the header key absent, the literal
string `"none"`, and a comma-joined multi-value. `interpreter_v1.md`
§4.5's own worked precedent — the one F1 cites as proof the fix is "the
code's own intended rendering" — only demonstrates the wording for the
`none` case (`no-matching-rows (floor_pattern: none)`,
`docs/design/interpreter_v1.md:474`). `report.py:4418-4432`'s own
docstring confirms the multi-value case is a materially different
population (multiple sub-benches, each declaring a genuine but DIFFERENT
floor pattern — an ambiguity about WHICH comparison to make, not an
absence of one to make), and probe1's floor_pattern census (re-run live:
`'floor': 40, 'floor-byte': 3, 'none': 2`) shows zero committed reports
have hit it yet, so it is untested by any witness. Before calling F1
"closed... in one mechanism" (§6 Group 2), the panel should confirm the
reason channel's closed vocabulary gets a distinct third member for the
multi-value case, since the design precedent it is copying never worked
that member's wording out.

---

## What I re-verified and found sound (not findings, stated for the record)

- **F1, F3, F4, F26, F27**: every code citation, every quoted rendered
  sentence and every corpus number reproduced exactly against a fresh
  re-run of the corresponding probe and/or a direct read of
  `interpret.py`/`report.py` at the cited lines. F26 in particular: I
  traced `render_tsv`'s `did_not_compile` emission
  (`report.py:4555-4564`) back to `_ranking_groups` (`report.py:3462-3486`,
  keyed only from `rd.match_cells`/`rd.set_cells`) and confirmed
  `did_not_compile_by_pattern` is built independently from raw compile
  rows (`report.py:3347-3358`) — a pattern with zero compiling testees
  genuinely has no group key for the emission loop to ever visit, in both
  `render_tsv` and `render_markdown`.
- **F23 (R-FLOOR-1/3, audited CLEAN)**: confirmed clean by construction,
  not just by corpus coincidence. `_jitter_flag` returns `""` only when
  `median_ns` is falsy or `stddev_ns is None`
  (`report.py:2419-2431`); `_pstdev_safe` returns `0.0`, not `None`, for a
  single-trial population (`report.py:1379`), so a genuinely *compiled*
  single-trial cell still gets a real jitter row. The omitted population
  is mechanistically exactly the refusals, matching probe4's corpus count
  (1,266 missing jitter rows = 1,266 empty-median compile rows).
- **F24 (R-BUCKET-FORM, audited CLEAN)**: confirmed — the narrowing is
  explicitly stated in the catalogue's own `predicate` prose, and the
  rule's `rank`-only read matches that stated scope exactly
  (`interpret.py:1006-1019`).
- Corpus bookkeeping in §0/§4's opening paragraph (45 reports, 3
  subject-grain slices, 3 predictions files, 69 clause rows, 6 sidecars;
  "eleven LIVE" = the eleven §4 entries actually headed "LIVE") all
  cross-checked against `ls`/`grep` counts and the §4 headers themselves.

---

## Summary

Five findings: **1 BLOCKING** (r7pop-1), **3 SHOULD-FIX** (r7pop-2,
r7pop-3, r7pop-4), **1 WORTH-NOTING** (r7pop-5). All five are about the
note's own reasoning or proposed fixes, not about the underlying rule
code, which I independently re-derived and found the note's account of
(F1, F3, F4, F26, F27, plus the F23/F24 CLEAN narrowings) to be accurate
in every particular I could check. The recurring shape across all five:
the audit is very good at finding a population that cannot contain its own
counterevidence in the CATALOGUE; it is less careful about the same
failure mode in its OWN remediation proposals (r7pop-1's uncited "MEASURED",
r7pop-2's reducer overgeneralization, r7pop-3's fix that cannot reach the
population it names, r7pop-4's fix that narrows the population it anchors
to without saying what that costs). None of this weakens F1/F3/F4/F26/F27
as findings against the shipped code — those stand, confirmed. It bears on
whether the panel should adopt Q4, F11's Group-3 fix and F27's Q7 fix
exactly as worded.
