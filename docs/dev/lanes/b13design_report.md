# Lane `b13design` — [B13] the interpreter, DESIGN NOTE

Branch `lane/b13design`, worktree `worktrees/b13design`, 2026-09-07.
Deliverable: **`docs/design/interpreter_v1.md`** (committed, afc9239),
plus one entry in `docs/design/CLAUDE.md`. No code. No catalogue file.
No skill directory. Nothing under `pcrecbench/` or `.claude/skills/`
was created or touched.

## What was delivered

A reviewable design note for `[B13]`, in twelve sections:

- **§1 scope**, with an explicit OUT list — per-set outlier bands
  (`bench/*/NOTES.md`'s R0-R7), causes, and importance rankings are
  named as *not* the catalogue's business, with the reason.
- **§2 inputs**, exactly: the report TSV's header keys and its
  18 columns (`report.py:4092-4094`), `store/index.tsv`'s 8 columns,
  and the single join key between them (a `record` row's `testee`
  column is the basename of an index `path`).
- **§3 the catalogue** — `catalogue/rules.toml` at the repo root beside
  `schema/`, TOML, `MAJOR.MINOR`, with the bump rule spelled out and the
  regeneration invariant that makes a stale sidecar a `make check`
  failure.
- **§4 the rules** — six classes, 30 rules, each with inputs, threshold,
  threshold source, template and a worked example from a committed
  report.
- **§5** `interpret`'s output (facts TSV + `--render`), including the
  never-silent non-firing row.
- **§6 predictions** as machine-readable input, designed from scratch
  (none exists — see below).
- **§7 the opinion firewall**, enforced three ways.
- **§8 `make check-interpret`**, five sections.
- **§9 the skill**, plus a full hand-rendered sidecar from a real report.
- **§10 the acceptance test** — the falsifiable promise.
- **§11 eight open questions**, **§12 what the note does not decide.**

## What I read to ground each threshold

Every threshold in the catalogue is either a value `report.py` /
`reduce.py` already computes and prints (read as a string), or a
comparison of two measured numbers from the same report. **No rule
introduces a constant of its own.** Read directly, cited by line:

| threshold | where it lives | who set it |
|---|---|---|
| cross-pin "beyond spread" = \|Δmedian\| > 2 × max(stddev_old, stddev_new) | `report.py:2234-2248` `_cross_pin_verdict` | [B9] R8 |
| compile "timer floor" = min_ns < 20 µs | `report.py:1927` `_TIMER_FLOOR_NS`, applied at `:2150-2165` `_jitter_flag` | [B14] R5 |
| the reference arm = `libpcre2_*` + `_interp-` | `report.py:3153` `_is_reference` | [B9] R5 |
| set-cell dominance = 90 % one subject | `report.py:2326` `_DOMINANCE_SHARE`, `:2329` `_dominant_subject` | [B16] R7 |
| the floor pattern's per-subject mean = `median_ns / n_subjects` | `report.py:2582-2595` `_floor_mean_for` | [B14] R9 / schema v1.3 `patterns[].role` |
| a selection change is not a ratio | `report.py:2447` `_cross_pin_info` | [B16] R4 |
| trial agreement k=1.5, d_min=2, share_c=3, N≥5 odd | `reduce.py:246-250`, rendered by `agreement_line` at `:351` | [B20] / schema v1.4, **measured over the store's 68 records** |
| the set-grain comparable itself | `reduce.py` module header + `reduce_set_cell` | [B10] R5 |

Also read for grounding, not thresholds: the two `[B13]` seed documents
(`docs/dev/feedback_pcrecdev1_2026-08-25-repin.md` and `-repin-v2.md`),
`docs/dev/dev_journal.md`'s second-session parts 5 and 7, the `[B13]`
plan row in full, `docs/dev/known_issues.md` KB-13/14/15,
`docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md` §6/§8/§9/§10,
`reports/CLAUDE.md`'s reader's caveats, `Makefile`'s check targets, and
`schema/examples/bad/`'s 73-fixture naming pattern (the model for §8's
fixture design).

## Predictions: there is no existing store — checked, not assumed

`grep -rn "prediction" docs/dev/ pcrecbench/ schema/` returns prose only
(the eight-row markdown table in `feedback_…-repin.md` §3,
`bench/syntax/NOTES.md`'s P1-P13, ledger convention text, free text in
plan rows). **Nothing machine-readable exists.** §6 designs the minimum:
`docs/dev/predictions/<slug>.tsv`, columns
`prediction_id source source_ref stated_utc subbench version selector
quantity reducer op lo hi unit note`, with `quantity` drawn from a
closed set the TSV can answer and `reducer` (`ratio_to`,
`ratio_to_median_over`, …) so that all three real prediction shapes —
a cell-to-cell ratio (pcrec I-38's `cls-upto-2048 ÷ 1024` in 0.90-1.10),
a band before/after (I-27's `letters 3.65-6.05 → 1.76-2.00`) and a bound
over a population (`bench/syntax/NOTES.md` P13's "no compile time beyond
×10 the median") — fit one row shape. `stated_utc` is a column so
`make check-interpret` can assert it precedes the earliest record
timestamp in the report's population, making post-hoc prediction
mechanically visible. **Parsing inbox prose is explicitly rejected** and
the reason is stated.

## Which real reports the worked examples cite

Every number in the note was pulled from a committed file and verified
against it. By rule:

- **R-STATUS-2** — `reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv`
  header (`14 candidate(s); records: 9; superseded: 5`) against
  `store/index.tsv`'s 14 rows for `email-specimen@0.1`, of which three
  are `inconclusive-load` (interp @ 17:34:02Z, auto @ 17:51:31Z,
  auto-nocaps @ 17:55:34Z) and appear in **no** report.
- **R-STATUS-3 / R-STATUS-12** — same report, its 13 `excluded` rows:
  `-2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B)` on
  `factored`, `-4:PCREC_ERR_WORK×1 (same subject)` on `orig`,
  `-3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B)` on
  `factored`/match-compliance.
- **R-STATUS-4** — `reports/2026-09-07-syntax-0.1-…-first-d34c9131.tsv`,
  172 `did_not_compile` rows with pcrec's diagnostics verbatim.
- **R-DELTA-1** — same email report, `factored`/short-search/`vm`
  `faster ×1.19` (median 69,537.5) and `orig`/compliance/`vm`
  `faster ×1.26` (median 80,227.6) — the two numbers
  `feedback_…-repin-v2.md` §2 demanded be flagged.
- **R-DELTA-2** — six firings in that report (`selection changed
  (vm → dfa)`), and `cls-upto-8192`/compliance/whole-subject
  `selection changed (dfa → vm)` in
  `reports/2026-09-06-bounded-0.3-…-after-d34c9131.tsv`.
- **R-RANK-1** — same bounded report, `cls-upto-8192`/compliance/
  whole-subject/`auto-caps-simdna`: `ratio_vs_baseline` **1.788**
  (334fd10e) → **0.269** (d34c9131). Second instance:
  `reports/2026-08-29-loglines-0.1-…-repin-36d5963.tsv`,
  `stack-frame`/short-search/`auto-caps-simdna`, **2.698 → 0.155**.
- **R-FLOOR-1** — syntax report: 190 compile rows read `timer-floor`
  against 26/23/23/23 carrying real ratios.
- **R-FLOOR-2** — syntax report, `anc-caret`/short-search/
  `pcrec_d34c9131_vm-caps-simdna`: 246.458 ns / 42 = **5.868
  ns/subject** against the `floor` pattern's 800.099 / 42 = **19.050** →
  0.308× the set's own control.
- **R-BUCKET-FORM** — email report, `orig`/match-compliance and
  `factored`/match-compliance, the only two groups mixing
  `separate artifact` (7 pcrec rows) with `same program` (2 libpcre2).
- **R-BUCKET-VSBEST** — bounded report, `cls-upto-1024`/short-search:
  334fd10e ranks **1** at 989.820 ns, d34c9131 ranks **2** at 998.441,
  Δ `slower ×1.01`, three pin slugs in the group.

**One census run for the note** (read-only, over the 42 committed TSVs):
R-RANK-1's predicate fires in **9 of 42** files on **69** (pattern,
regime, form, config) pairs — 40 in `2026-09-05-altwide-0.2-…-after-334fd10e.tsv`,
7 in bounded@0.2 after-a7e0bdf, 7 in bounded@0.3 after-d34c9131, 4 + 4
in the two loglines files, 2 + 2 + 2 elsewhere, 1 in bounded@0.3
step2-after-288d505. The rule is neither dead nor universal.

## The falsifiable acceptance-test claims (§10), in brief

Three reports; the full numbered lists are in the note.

- **A — `2026-08-25-email-specimen-0.1-…-repin-692c2e8`** (Frank's
  original blinded target, still committed): the three inconclusive
  records by id **from the index, not the report**; the collapse as six
  R-DELTA-2 firings; all 13 give-up exclusions by code and smallest
  subject; the STEPS-vs-WORK pairing on `t-c-long-atom-run`; the two
  unpredicted Δs (×1.19, ×1.26); the regime artifact on both compliance
  groups; the mixed 1.1/1.2 schema population. Item A.4 (the vm-in
  result) is flagged **in advance** as the claim most likely to fail —
  it is an adjacency, not a rule firing.
- **B — `2026-09-06-bounded-0.3-…-after-d34c9131`**: R-RANK-1 and
  R-DELTA-2 **co-firing** on `cls-upto-8192` (a v1 that fires only one
  is failing); R-BUCKET-SPAN on the `vm-in` rows (a Δ across three abi
  steps); R-RANK-1 on five `dig-*` rows.
- **C — `2026-09-07-syntax-0.1-…-first-d34c9131`**: the 172 refusals and
  23 exclusions; **R-BUCKET-KB recognising KB-13's and KB-14's
  signatures** from TSV columns alone — flagged as v1's strongest and
  riskiest claim, since those two findings cost an opus lane hours;
  R-FLOOR-2 on `anc-caret`; R-FLOOR-1 on the 190 rows; and **R-STATUS-9
  must NOT fire** (all six records read `agree`) — a false-positive trap
  written into the test on purpose.

Each report also carries a MUST-NOT list (no causes, no "better",
no NOTES.md band verdicts).

## The one charter deviation, flagged not assumed

The plan row says the **skill** phrases the fired rules into the
sidecar. §7.4 instead puts the phrasing in `interpret --render` and
leaves the skill to run, verify and commit. Reason: a model writing the
sentences makes the firewall a promise about behaviour again and breaks
byte-reproducibility, which §8's determinism check and §3.3's
regeneration rule both depend on. Recorded as **open question Q4**, with
the fallback stated (a fenced `## Reader's note` excluded from the
byte-equality check) if Frank rules the other way.

## Validation

`make check-schema` in the worktree: **4 examples accepted, 72
sabotages rejected for the intended rule, 0 wrong** — a no-op
confirmation, as briefed; nothing in this lane touches `schema/`.
`make check-harness` was not run (nothing here is exercised by it) and
no engine, driver or box resource was used beyond read-only greps and
one python pass over the committed report TSVs.

## Scope

Only `docs/design/interpreter_v1.md` (new), `docs/design/CLAUDE.md`
(one entry) and this report were written. `~/pcrec` untouched (BD2). No
report, store record or bench sidecar modified. `docs/dev/plan.md` and
the root `CLAUDE.md` deliberately NOT touched — the `[B13]` row still
reads `STATE:not-started`, which is correct until the panel runs and the
implementation lane opens; the manager owns that transition.

## What a follow-up round should do

1. Run the adversarial critic panel on `interpreter_v1.md` (the R1-R3
   pattern, `docs/dev/reviews/YYYY-MM-DD-r4-interpreter-v1.md`).
2. Get rulings on the eight §11 questions — **Q4 (the charter
   deviation) and Q3 (set-local bands) are Frank's**; Q1, Q2, Q7, Q8 are
   the manager's; Q5 and Q6 are recommendations the panel can contest.
3. Only then open the implementation lane, which builds
   `catalogue/rules.toml`, `pcrecbench/interpret.py`,
   `make check-interpret` and the skill — against §10's acceptance test,
   which is now on the record and cannot be quietly weakened.
