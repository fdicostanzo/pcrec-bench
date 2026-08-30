# Manager's rulings on the [B20] panel blockers (2026-08-30, before r3 is compiled)

These are decisions, not proposals. The r3 compile lane records them as the
dispositions of the findings they name and applies them to the spec.

R-1 (B3, MINOR vs MAJOR): **MINOR (1.4), with record_schema.md §4 AMENDED in
the same change.** New clause: "a cross-line RULE may be revised at a MINOR
bump provided (i) the revision is keyed on `schema_version` in the validator,
(ii) older records keep the verdict of their own version — never re-stamped,
(iii) the reporter renders the rule's version beside every status it ranks
(a `rule:` marker in the ranking rows / legend, not only in the agreement
column)". Why not 2.0: a MAJOR bump makes the reporter refuse 1.3 + 1.4 in one
query by default — the first v1.4 window's cross-pin reports would need
`--allow-mixed-versions` on every query, and the store would split for zero
ranking difference (§7: every record's rank is unchanged). B3's sub-finding
(the note says "a reader on an older minor MUST accept" while validate.py
REJECTS a newer minor under X17): the VALIDATOR's behaviour is the rule
("upgrade the validator"); amend record_schema.md:177 to say so. D1 gains §4.

R-2 (B2 + F2 + F1 + B12, the target core): **tri-state, then-branch only,
pre-flight refusal.** `target_busy_pct`: ABSENT when `pinning.cpu` is not an
integer; `null` when the target's row was not in the capture; a number
otherwise; `null` whenever the sample is `unavailable` (the schema's `then`
branch enforces that direction only, as B2's hunk). The field is keyed on
`pinning.cpu` (one source; F1) — `exclude_cpu` is passed FROM pinning.cpu,
never the reverse. A missing target row on a pinned run is a PRE-FLIGHT
REFUSAL in `gate()` (reason: "the target core cpuN does not appear in the
mpstat capture") — exit 3 / `inconclusive-load` under --force-unquiet — so
X13 clause 3 ("measured requires target_busy_pct a number ≤ limit when
pinning.cpu is an integer") is never the first thing that notices. Both
samples carry the field (§1's "written on both"); only `before` is judged.
Controls: the three-capture fixture (present-under, present-over, absent)
and `x13-measured-but-target-busy-null.jsonl`.

R-3 (B5 + F8, the arithmetic): **add §3.5 "the rule, as arithmetic"** — the
exact pseudocode both implementations follow: row key `(pattern_id, regime,
form or "plain", subject_id)`; a TRIAL is timed iff `match_outcome ==
matched-as-expected` and `timing.iterations > 1`; a ROW is judged iff it has
≥ 2 timed trials (mixed outcomes: judged on the timed ones); `xs` = the timed
trials' `elapsed_ns / iterations` as float64, sorted by `trial`; `m =
statistics.median(xs)` (even N: the mean of the two middle values, as
statistics.median); `slow = sum(1 for x in xs if x > k * m)`; `fast = 1 if
min(xs) < m / k else 0`; `worst_row` = the judged row with the largest
`max(xs)/m` ratio, ties broken by the LOWEST `seq` among the row's trials.
X32 compares INTEGER COUNTS (rows_judged, rows_disagreeing) and the
worst_row key — never floats. The validator's implementation (no pcrecbench
import) is the control; one hand-computed fixture pins both; the arithmetic
is stated once, in §3.5, and both cite it.

R-4 (F5 + B6, the status-deciding sentence): **the status-deciding sentence
is always FIRST.** `record.join_notes` gains `first=` (the harness passes the
status sentence(s) separately); the after-sample provenance sentences go
SECOND; calibration sentences last. R1's not-ranked bullet for an
`inconclusive-spread` record prints FROM THE BLOCK (`rows_disagreeing /
rows_judged`, `k`, `worst_row`), not from the free text; `_excerpt` stays 120
for other statuses. Check + control as F5 (3).

R-5 (F6, status_detail): **keep today's split.** `note` = the operator's
`--note` prefix + the run's notes; `status_detail` ONLY when status ≠
`measured` (as today). The after-sample provenance sentence goes into `note`
on a `measured` record (second, per R-4) and into `status_detail` otherwise.
§2's "status_detail on every status" is withdrawn; `--include-provenance`
renders the provenance sentence from wherever it sits.

R-6 (F7, the window script): **contract 4 gains exit code 4 =
`inconclusive-spread`** (the record IS written; the exit code tells the
script). `scripts/run_window.sh` retries an rc=4 cell ONCE (a spread is not
a gate transient; one re-measure, then move on), logs it, and `pcrecbench
index` prints a per-status breakdown. `quick` prints the verdict line.

R-7 (F3): **`cmd_quiet` judges through `quiet.gate()`** (load1, the per-core
average, the target core) so the warm-up, the CLI and the harness are one
instrument; the CLI prints the target's number and the sibling.

R-8 (Q2 / F14): **`harness-failure` stays as it is** — a documented schema
value the harness cannot reach today; the spec says so in §3.4 and §9; not
made real in v1.4.

R-9 (F16 / KB-4): **the SCHEMA half of KB-4 rides with v1.4** — compile_row's
allOf no longer forbids `cost` beside `compile_outcome != compiled` (a
refused compile may carry the bench's clock around the pcrec exec). The
adapter and reporter halves stay KB-4's own follow-up.

R-10 (F13 / B10, checks and examples): **no sleep injection in the production
drivers.** `check_spread_status_stamped` = a pure `harness.derive_status()`
over a hand-assembled record + the record written through `store.write`
(the status is stamped by the harness path, checked by the validator path).
The examples plan is rewritten against the ACTUAL examples store (three good
records at 1.1/1.1/1.2, no 1.3 good example — add one 1.4 good example that
exercises every new field, and bump nothing else); one bad example per new
rule, each constructed to fail ONLY its rule (B7: the X31 example must not
also trip X32 — its counts must be consistent and only the verdict wrong).

R-11 (F4, the post-cell decay on the target core — "needs one measurement"):
**not gated on a measurement before the implementation**; the implementation
lane's first window prints the target's number on every pre-flight and the
distribution is read then (Q1); the retry budget stays 12 × 30 s.

R-12 (Q4, small cells; Q6/Q7, trials ≠ 5; B11, quick's 3 trials): **pinned
records require trials ≥ 5 for the rule to judge** — X33 becomes: the block
is REQUIRED on a pinned record whose match rows carry ≥ 5 trials; a pinned
record with 2-4 trials carries the block with `verdict: n/a-trials` and is
NOT `measured` (it is `inconclusive-spread` with rows_judged = 0 — a
measurement that did not meet the rule's precondition is not a measurement);
`--trials 1` pinned runs likewise. Scratch-tier records (quick, 3 trials)
carry the block with `verdict: n/a-trials` and are never ranked anyway —
`quick` prints "agreement: n/a (3 trials)". A row-count floor for F: none —
the base rate argument stands for pinned cells (≥ 321 rows); scratch cells
are not ranked.

R-13 (Q8): **confirmed** — `load.verdict = loaded` may sit beside `status =
measured` on a v1.4 record; X20 unchanged; the reporter's `--include-
provenance` shows it.

R-14 (Q9, the timer floor): **no exemption clause**; one row in 62,923 is
not worth a rule; recorded as a known false-positive risk at the timer floor
in §9's residue.

R-15 (Q10): **confirmed** — `inconclusive-load` over `inconclusive-spread`;
both facts in status_detail.

Everything else in the three panels (should-fix / note): accepted as text
fixes unless the compile lane finds a contradiction with a ruling above, in
which case it lists it under "escalated" in r3 rather than resolving it.

# Amendments after panel A (measurement validity) — same standing

R-16 (A blocker, F on a group boundary): **the record-level fraction F is
DROPPED; the rule becomes GROUP-LEVEL with integer arithmetic.** A GROUP is
one (pattern_id, regime, form) with n judged rows; it DISAGREES iff its
disagreeing rows d satisfy d ≥ D_MIN and c·d ≥ n (integer constants; the
rule's unit is a pass of a group, so the threshold is a share of the group,
never of the record); a RECORD disagrees iff ≥ 1 group disagrees. The
constants (D_MIN, c) are CHOSEN BY RECOMPUTE over the store (extend
probe_trial_agreement.py with the group-level census; archive the new
output as a NEW D35 file, e.g. 2026-08-30-trial-agreement-census-groups.txt;
the old file stays) under two constraints: zero disagreeing groups on the
store's 68 records, and the smallest threshold that still flags a group
whose every row has two slow trials (a two-pass disturbance) AND a half-pass
overlap (half the rows) — state the margin in ROWS per group size (n = 4,
5, 30, 85, 112). The store's single fast row (floor/s-081, 1 of 30) must
remain a non-disagreement under the chosen constants (it is real — A's
finding — but one row is not a disturbed group). §3.2/§3.5 restated; the
block's fields become {rule: "v1.4-group", k, d_min, share_c, trials,
groups_judged, groups_disagreeing, rows_judged, rows_disagreeing,
worst_group (pattern/regime/form, d, n), verdict}; X31 = verdict iff
groups_disagreeing == 0; X32 = the integer counts and worst_group recomputed
from the rows.

R-17 (A must-fix, the blind band): **state it, do not hide it.** §3 gains
"what the rule cannot see": a slowdown ≤ k on 3-4 of the 5 passes moves the
row median by up to (k−1) and reads agree; a competitor spanning all five
passes of a group is invisible to trial agreement by construction (the
pre-flight and BD7 are the defence; the after-sample is provenance). A's
power table (P(flag) vs competitor duration, from the reconstructed
timelines) goes into §3 as the honest statement, with the measured PASS
durations (0.07-20.2 s, capped by TRIAL_BUDGET_SECONDS) replacing the
"1-2 s" vocabulary everywhere. The per-group occupancy TIMELINE A proposes
(/proc/stat deltas around each group's measurement, microseconds, no new
process) is ACCEPTED AS PROVENANCE ONLY, never a verdict (Frank's item 4):
the spec designs the field (a per-group provenance record in the setup
layer or on the group's first row — the lane proposes the cleanest fit under
additionalProperties: false) and marks it "v1.4 if the schema hunk is
clean, else v1.5"; the reporter renders it under --include-provenance.

R-12 amended (A must-fix, one constant / four rules): pinned records
require **N ≥ 5 AND odd** for the rule to judge; the block records `trials`;
verdict `n/a-trials` otherwise (the R-12 consequences stand). `quick`'s
default 3 trials print "agreement: n/a (3 trials)".

R-14 amended (A reverses Q9): the fast row is a REAL bimodality (12.2 vs
18.7 ms over 1.32 M iterations; the same pattern/subject flat in the other
artifact) — the rule's only demonstrated true positive at the row level; no
exemption, and §3.1's wording ("a timer-floor artifact") is corrected.

R-19 (A: timed-out trials): a row with a `timed-out` trial among its
trials is COUNTED AS DISAGREEING (a trial that hit the alarm is a
disturbance, not a measurement); a row with < 2 timed trials for any other
reason (iterations ≤ 1 rows: 190 in the store) is not judged and is
counted in `rows_unjudged`, rendered by the reporter.

R-20 (A: the slowest-trial histogram, 158 of 387 events from one record;
k's margin — the FP appears at k = 1.30; the store cannot distinguish k in
[1.55, 2.0]): **k stays 1.5**; §3.1 states the margin honestly ("the
contaminated record clears the rule at k ≥ 1.35; the store is
uninformative above 1.55"); the one record that dominates the histogram is
named and its phase reading recorded as a note.

Q4's base-rate arithmetic (A: wrong on independence and population) is
withdrawn from the spec; the group rule makes it moot.
