# Lane `b13rev` — [B13] interpreter design note, r4 revision to v1.1

Lane: `b13rev`, branch `lane/b13rev`, worktree `worktrees/b13rev`,
2026-09-07. Deliverable: `docs/design/interpreter_v1.md` at **v1.1**,
revised in place under every disposition of
`docs/dev/reviews/2026-09-07-r4-interpreter-v1.md`. DESIGN ONLY — no
code, no `catalogue/`, no `pcrecbench/interpret.py`, no skill directory,
no touch to `docs/dev/plan.md`.

Commit: `0d9f62c`. Validation: **`make check-schema` green — 4 examples
accepted, 72 sabotages rejected for the intended rule, 0 wrong.** (The
run also confirms the note's own corrected count of 72 sabotage files.)
No `make check-harness` run; nothing under `schema/`, `pcrecbench/`,
`bench/`, `testees/` or `tools/` was touched.

Files changed: `docs/design/interpreter_v1.md` (1,228 → **2,391 lines**),
`docs/design/CLAUDE.md` (its entry rewritten for v1.1), this report.

---

## Method

Every disposition was applied against **source I read myself**, not
against the critics' citations: `pcrecbench/report.py`
(`_ranking_groups`, `_cross_pin_info`, `_cross_pin_verdict`,
`_is_reference`, `_jitter_flag`, `_floor_mean_for`,
`_gave_up_cell_summary`, `_set_cell_failure_reason`, `_n_and_pass_rate`,
`render_tsv`'s row emitters and header block, the `floor_pattern_by_sb`
derivation), `pcrecbench/reduce.py` (`agreement_line` and the v1.4
constants), `schema/examples/gen_example_14.py`,
`docs/design/record_schema.md` §6.4, `bench/syntax/NOTES.md` P1-P13, and
`docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md` §6. Every
number written into the revised note was re-derived by a script over the
committed corpus in the session scratchpad (nothing written outside the
worktree).

---

## Disposition by disposition

### BLOCKING

**B1 — the record row's agreement string.** §2.1's row description now
says the agreement string is in `value` paired with `metric = agreement`,
and that `gave_up_summary` is EMPTY on every `record` row, with a
bracketed "corrected from v1" note explaining that v1 copied report.py's
own stale comment at 4097-4099. §8(4)'s fixture plan requires
R-STATUS-9's fixture to be a projection of a REAL `record` row, so the
column position is pinned by data. *Verified myself against
report.py:4104-4107 and against all nine `record` rows of Report A.*

**B2 — R-STATUS-9.** §4.1's table now fires on `disagree` only. A
five-row table in §4.1 enumerates every reachable string with its
source, its meaning and who reports it: `agree (…)` (reduce.py:373-379),
`agree 0/0 groups -- nothing judged` (reduce.py:371), `disagree (…)`
(reduce.py:365-369), `n/a (N trials)` (reduce.py:359), and
`n/a (v<schema>)` (`_agreement_display`, report.py:2788-2792). The last
is folded into R-STATUS-6, whose template now carries `{n_pre_14} of
{n_records} record(s) predate the v1.4 block`. §9.2 re-rendered
accordingly, and §10 A.8 makes "R-STATUS-9 must NOT fire on Report A" an
explicit MUST-NOT. *One note on the disposition's wording: it says "all
four output shapes"; `agreement_line` has four returns and
`_agreement_display` adds a fifth (`n/a (v<schema>)`). I enumerated all
five and named which function produces each, since the fifth is the one
the whole finding is about.*

**B3 — the verdict column's grammar.** §2.1 now states it explicitly:
`delta_verdict` is a `; `-separated list of independent clauses, each
R-DELTA rule matches its anchor against each CLAUSE, and the five
reachable clause shapes are enumerated with their sources
(`_cross_pin_verdict`, the selection-change block, and
`_set_cell_failure_reason`'s five reason tokens). The corpus value-space
census is quoted. §4.2 states the two consequences — R-DELTA-1/2 never
co-fire, R-DELTA-2/3 DO — and §8(4) requires the co-firing fixture
alongside the mutual-exclusion one. *Re-derived: the compound occurs on
**four cells** (24 rows at six metric rows each), all four in Report A;
the review's "24" is a row count and I said so, because a lane reading
"24" as cells would build the wrong fixture.*

**B4 — R-BUCKET-KB.** I took the **known-gap branch** and did NOT design
the `expectation_detail` precondition, and §4.7 states why in full: the
observed-vs-expected string is derived per SUBJECT inside the record's
`observed` field and the reporter computes nothing like it today
(`_set_cell_failure_reason` gives a one-word class that does not
discriminate KB-13 from KB-14 either), so it is not a one-line change.
The class ships with its registration bar stated (a signature must name a
column-level discriminator no other registered signature matches, checked
against every golden), with **no signature registered**, always reporting
`did-not-fire: no-registered-signatures`. Registration is a MAJOR bump
(§3.3). §10 C.3 is now a numbered item that says v1 does NOT find those
defects, plainly.

**B5 — the ranking-group key.** §4 opens with a "Note on 'group'" that
states `_ranking_groups`'s real key `(subbench, pattern, regime)` at set
grain, quotes the docstring's reason that `form` is deliberately excluded,
and distinguishes it from the cross-pin pair's key (which IS keyed on
form, report.py:2481) and the arm pair's. Every rule that says "group"
was re-derived. Re-verified against Report A: 6 ranking groups, of which
**2** carry both `same program` and `separate artifact` (R-BUCKET-FORM's
worked example, 7+2 and 3+2 rows) and **4** carry two pin slugs
(R-BUCKET-VSBEST). R-STATUS-13's population re-derived over all 42
reports by my own script: **891 of 2,514** — exactly the charter critic's
number, and I state it as the corrected figure against v1's implied
1,323/2,946.

**B6 — R-RANK-1's guard.** R-RANK-1 now fires only where R-STATUS-13 does
not. **I refined the disposition here and flag it:** the review offered
`baseline_is: reference|best` as a "better" reporter column. I did NOT
make it a precondition, because the guard is derivable EXACTLY from the
TSV — report.py:4133-4136 falls back iff no *rankable* reference row
exists, and a rankable row is precisely a `rank` row, so "this group has
no `rank` row whose testee satisfies `_is_reference`" is the fallback's
own condition, not an approximation. `baseline_is` is recorded in §2.5 as
an optional follow-up that would remove one derivation. This keeps the
precondition set at two, which matters because each precondition is a
`REPORTER_VERSION` bump plus a full regeneration.

**B7 — R-ARM.** New §4.4, one rule (R-ARM-1). Threshold copied from
`_cross_pin_verdict` and applied within-report, so §4's no-tuned-constant
property survives. The config decomposition is stated precisely and was
**verified against all 59 testee ids in `store/index.tsv`**: parse
`<engine>_<version>_<config_slug>[_<config_extra>]`, then parse the
config slug FROM THE RIGHT (`simd`, `caps`, then `mode` = everything
before, because `vm-in` contains a hyphen), giving four tokens
`(mode, caps, simd, extra)`. This detail is load-bearing: a naive
"differ in one hyphen field, same field count" rule does **not** pair
`vm-caps-simdna` with `vm-in-caps-simdna` (3 fields vs 4) — i.e. it would
miss precisely the pair §10 A.4 exists for. I found that by running both
rules over Report A. Two definitional exclusions: same `form` (else two
artifacts are compared), and neither arm is the reference arm (else the
rule is a census of the `ratio_vs_baseline` column).

Measured, on Report A: R-ARM-1 fires **14** times and surfaces A.4
exactly — `orig` / short-subject-search / plain, `vm-in` 12,546.2 vs `vm`
28,996.9 = **×2.31** (spread 862.2); `orig` / match-compliance /
whole-subject, `vm-in` 62,732.3 vs `vm` 80,227.6 = **×1.28** (spread
318.8). It also finds the grounding feedback's row (c) by rule:
`vm-in` 62,732.3 vs `auto` 234,082.1 = **×3.73**, the feedback's "3.7×".
On Reports B and C it fires **432** and **635** times, which is what
made S1's aggregation mandatory rather than optional.

**B8 — the golden and freshness checks.** §8(2) now runs against
`catalogue/golden/index@<date>.tsv`, a frozen snapshot committed beside
the goldens; the live index stays the default for a human run. A table
states, for four commit kinds, whether `check-interpret` may fail and who
regenerates: records-only **NO** (that is what the snapshot buys, and it
is KB-8's failure mode one layer up); catalogue bump **YES**, the
catalogue lane; **reporter bump YES**, the reporter lane, in the same
commit as the report regeneration `reports/CLAUDE.md` already requires;
snapshot refresh YES, the refreshing lane. §3.3 now names all three
things that move a sidecar, not just a catalogue bump.

**B9 — `firing_seq`.** §5.1's facts TSV gains `firing_seq` (integer, per
rule, emit order) and `prediction_id` as its own column, with the four
rule shapes that break key-column identification enumerated.

**B10 — `[[pin_order]]`.** §3.2 shows the table; §4.7 states that a pin
absent from it is a load error (exit 2), never a silent non-firing, and
that appending at a re-pin is MINOR. v1.0's `pcrec` row is written out —
the eleven pins in `store/index.tsv`, `8da6120 … d34c9131` — and §8(1)
checks that every pcrec pin slug in a golden report is in the table.
Q10 (§11) asks where the append belongs in the re-pin checklist.

**B11 — template prose audited.** §7.1 states the rule: every clause in
a template that is not a slot and not definitional must be a `links`
entry the renderer appends, or be removed. R-STATUS-12's template now
renders the two codes and stops, with "a different budget binds" demoted
to a `links` entry to `feedback_pcrecdev1_2026-08-25-repin-v2.md` §2.
§8(6) is the new sixth section: a template-diff gate that flags any diff
touching `template`, `no_fire`, `links` or a `[[signature]]` and requires
a reviewer approval line in the commit message naming the rule ids.
§7.4 is rewritten: the renderer phrases, templates are human-reviewed
prose authored once before any run, no charter deviation exists, and the
`## Reader's note` fallback is **deleted and explicitly rejected** with
the reason (it would make §8(3) and §8(5) both partial; a human reading
belongs in a ledger).

### SHOULD-FIX

**S1 — `aggregate`.** §5.2 defines it: a rule declares
`aggregate = [<slot>, …]`; at RENDER time (never in the facts TSV)
firings group by those slots and each group renders as one bullet with a
count, its extremal firing and, above two members, its minimum. Groups
render in sorted key order with ties broken by the sorted key columns, so
there is no free choice in the rendering. Every rule in §4 declares one.
Measured collapse, from my own scripts:

| rule | Report A | Report B | Report C |
|---|---|---|---|
| R-DELTA-1 | 3 → 3 | 202 → **17** | 0 |
| R-ARM-1 | 14 → **8** | 432 → **9** | 635 → **12** |
| R-FLOOR-1 | 2 → 1 | 81 → **2** | 190 → **2** |
| R-STATUS-4 | 0 | 6 → 2 | 172 rows / 60 pairs → **4** |
| R-BUCKET-VSBEST | 4 → 1 | 129 → **1** | 0 |

Report A's rendered sidecar is **44 bullets**, enumerated rule by rule in
§9.2. One judgment I made inside the mechanism, flagged: **R-STATUS-3
keeps `aggregate = []`** (13 and 23 bullets) because each of its bullets
carries its own give-up summary and §10 A.3 requires all three distinct
summaries to appear — an extremal-only rendering would drop the
`-3:PCREC_ERR_FRAMES` one. §5.2 states that reason as the rule for when
a rule stays un-aggregated. R-DELTA-4's `input-absent` with no
predictions file is fixed in §4.2's table (the mock-up was already
right, and was left alone as instructed).

**S2 — the predictions format, and the transcription exercise.** Reported
separately below; §6 rewritten around it.

**S3 — §10 falsifiable.** A.4 is now an ordinary MUST that passes by rule
(with the two numbers and spreads). C.3 states plainly that v1 does not
find KB-13/KB-14 and why. A **Report D** was added: the synthetic clean
fixture — every record measured, nothing excluded, nothing refused, no Δ
and no arm pair outside spread, one pin, one schema version — on which
all 31 rules must report `fired=0`. §10's closing sentence now names both
conditions and excludes C.3 from the promise.

**S4 — the fourth slot kind.** §7.2 now permits "a declared
decomposition, its regex or split rule written out in full in the
catalogue's `arith` field", with a table of the five decompositions v1.0
uses (the testee-id split, the `source:` candidate count, `_is_reference`
copied verbatim, the `delta_verdict` clause split, the header parse).
Q8's option (b) is precondition **P-2** (§2.5) — and I refined its
shape, flagged below.

**S5 — the `inputs` grammar and view contract.** §3.2.2 states the
grammar `<file>:<section>[?<col>=<val>…][.<column>|.{<col>,…}]` with four
worked entries, and the view contract `rows(section, **eq)`,
`header(key)`, `index_rows(**eq)` — each raising `UndeclaredColumn`. It
also states, per build #9(a), that the guarantee is "checked on the paths
the fixtures exercise", not a property. `rows()` returns a table because
at least eight rules are group-scoped or cross-row.

**S6 — the fixture plan.** §8(4) rewritten around `catalogue/fixtures/gen.py`
run with `--check`, mirroring `gen_example_14.py --check` (which I read:
generated base, one-field mutations, `--check` pinning the output). Each
fixture directory carries a `source.toml` naming a committed report, a
row selector, the index snapshot, `expect`, and — for the sabotage — one
declared field mutation; the generator projects a real reporter-produced
slice. "Minimum number of bytes" becomes "exactly one declared field
differs". The mis-described precedent, the ~190-hand-typed-files cost and
the shapes-`render_tsv`-cannot-emit problem are all stated as the reasons.

**S7 — `grain` mandatory.** §3.2.1 makes it required and checked at load,
with the two silent hazards named (`_n_and_pass_rate` returning
`n_subjects` vs `n_trials` into one column; `delta_verdict` populated at
set grain only). Every rule in §4 declares it; R-FLOOR-2 and R-RANK-* are
`["set"]`.

**S8 — `floor_pattern:`.** Precondition **P-1** (§2.5). §2.4's
"one place `interpret` reads outside its two inputs" is deleted; the note
now really does have two inputs. **A finding that strengthens the
disposition:** the reporter already computes `floor_pattern_by_sb` at
report.py:2927/2989 **from the records' own `patterns[].role`**, so the
header key carries the floor pattern *of the records in this report* —
which is not merely a convenience over reading `bench/`, it is the only
correct answer, and it is genuinely one line. On Report A the value is
`none` (its records are schema 1.1/1.2, pre-`role`), so R-FLOOR-2 reports
`no-matching-rows (floor_pattern: none)` — and that also corrects v1's
§9.2, which gave a reason (D6) that is false about the tree as it stands.

### The documentation batch

All swept: the header `; ` parse rule stated with the re-join algorithm
and the `x13_rules` collision quoted (§2.1); §9.2 re-rendered by hand
against every fix, all 31 rules present (12 firing, 19 not);
R-PRED-4/R-DELTA-4's scope conflict resolved by defining the
uncovered-finding rule ONCE as R-DELTA-4 with the wide scope and giving
R-PRED-4 to the `partial` verdict; R-RANK-2 **dropped** (argued in §4.3:
`rank_or_na` is a position among all testees and `delta_verdict` compares
one testee to its own older pin, so disagreement is an ordinary
consequence of a third row moving, not a contradiction — and a rule that
needs a *reason* to fire is a rule with an opinion; since it never
shipped, this is an absence, not a retirement, and the id is free);
R-RANK-3 → R-STATUS-13; the real-ratio count corrected to **644 rows,
161 per pcrec testee** (re-derived myself: 190 timer-floor = 95 on each
libpcre2 arm, 644 real = 161 × 4); `schema/examples/bad/` = 72 sabotages
+ one CLAUDE.md; `pyproject.toml` dropped from the TOML list (two
runtime readers, not three); `subject_or_na`'s two absent spellings
(`(set)` vs empty, by section); `encoding="utf-8"` on every planned
`open()`/`write()`, stated in §12 as a determinism property with the
`LC_ALL=C` reason; the "eighth row" corrected to the seventh; `§10 Q2` →
`§11 Q2`; the abbreviated testee ids in the bounded worked example
spelled out in full.

---

## S2 in detail — the P1-P13 transcription exercise

I read `bench/syntax/NOTES.md`'s P1-P13 and the [B36] ledger's §6
scorecard myself and transcribed all thirteen into the proposed format.
Result, written into §6.6:

- **12 of 13 expressible** in the clause the ledger actually scored;
- **8 of 13 expressible in every clause** (P1, P3, P4, P5, P6, P7, P8,
  P11, P13 — nine, of which P5 needs precondition P-1 for its second
  clause);
- **2 clauses inexpressible and now failing loudly at load**: P9's span
  claim (`asr-k-uc` reports [4,9]) and P12's answer-EQUALITY claim
  (`mod-j-uc` agrees with `bak-1`);
- **1 clause correctly lands as `not-evaluable`** (P2's `vrb-accept`
  clause — the pattern is a refusal at this pin), which is R-PRED-3
  working.

**Four things changed in the format because of the exercise**, none of
which v1's three-prediction survey would have surfaced:

1. `set_of(<key>)` reducer + `set-eq` / `set-subset` ops, for P1's
   set-membership claim.
2. `rank_over(<key>)` reducer for a cross-PATTERN ordering (P5, P7), and
   the TSV column renamed `rank` → **`rank_in_group`** so the trap the
   panel identified is closed by name: v1's `rank` would have handed a
   prediction author the rank of a TESTEE in a group when they meant the
   rank of a PATTERN in a set. §2.4 argues that `rank_over` is legitimate
   — it orders numbers the reporter already reduced, not records.
3. Clause-suffixed prediction ids (`P5.a`, `P5.b`) as a `clause` column,
   plus the **`partial`** verdict as R-PRED-4. Ten of thirteen real
   predictions were scored per-clause.
4. §6.4, a new subsection stating plainly what a prediction CANNOT say:
   an answer/span claim that AGREES with the oracle is expressible as
   `n_wrong eq 0` (that is exactly how P10's semantics and P12's
   agreement clauses were scored), one that DISAGREES is expressible only
   as `n_wrong gt 0` plus clean controls (that is how P2 was scored), and
   the specific answer or span is out of reach and must be a LOAD ERROR,
   never a silent `not-evaluable`.

**On reproducing the ledger's 3/5/5 tally — it does not, and I argue in
§6.6 that this is the right outcome.** Every CLAUSE verdict reproduces.
The parent roll-up (all-confirmed → confirmed, all-refuted → refuted,
mixed → partial) differs on **four of thirteen**, always by being
stricter than the human tally:

- **P6**: the ledger tallied CONFIRMED calling interp "marginal"; a
  measured ratio of **1.722** exceeds the stated ×1.5 band, so the clause
  is refuted and the roll-up is `partial`. "Marginal" is charity a rule
  does not have.
- **P1**: ledger PARTIAL ("13/15 as stated"); both clauses fail as
  stated, so the roll-up is `refuted`.
- **P4** and **P12**: the ledger listed them under REFUTED while naming
  only the refuted clause; mechanically both are `partial`.

The note takes the ruling that **per-clause verdicts are `interpret`'s
authoritative output, the parent verdict is the stated arithmetic, and a
ledger's tally is a human reading the tool must not try to reproduce** —
and calls the four disagreements the no-opinions property working. The
panel asked for ≥ 9 of 13 and the tally reproduced; I deliver 12 of 13
and argue explicitly why the tally should not be a target. **This is the
one place I did not do what the disposition literally asked, and it is
flagged here rather than done quietly.**

---

## Flagged: refinements, disagreements, and gaps in the dispositions

Nothing was silently re-litigated. Five items.

**1. S4/Q8's shape — refined, not rejected.** The disposition says "the
reporter emits `smallest_giveup_subject`/`_bytes` columns". I specified
**extra metric rows** instead (`metric = giveup_smallest`, the subject id
in `subject_or_na`, the code in `value`, the byte count in `n`), for two
stated reasons: two new columns would take the layout from 18 to 20 and
move every consumer's column index, and — decisively — "smallest" is
**per give-up code**, so two columns cannot carry a two-code cell without
re-introducing a `; `-joined value, which is the exact defect being
closed. The extra-row form is `render_tsv`'s own extension idiom (`rank`
already emits six rows per cell). Reversible: if the manager prefers
columns, only §2.5 and R-STATUS-12's `inputs` change.

**2. B6's `baseline_is` column — not made a precondition.** Argued
above: the guard is exactly derivable from the TSV, so the column would
buy nothing a rule needs. Recorded in §2.5 as an optional follow-up.

**3. Two panel findings were dropped in consolidation and I applied them
anyway, under B11's authority.** Neither appears in the consolidated
review's BLOCKING, SHOULD-FIX or worth-noting lists:

- **build #11** — R-STATUS-3's template renders "0 wrong answer(s), 0
  give-up trial(s)" on Report A's `libpcre2_10.46_jit-caps-simdna`
  throughput row (I verified: pass-rate 0.6667, `n_wrong` 0,
  `n_gave_up` 0, `gave_up_summary` `0`), i.e. a sentence naming no cause
  on a row whose cause the TSV does not carry. Since B11 requires every
  template clause to be a slot, definitional, or a link, the template is
  fixed to say only what the columns support, and the exclusion-cause
  column (`_set_cell_failure_reason` already computes it and throws it
  away) is recorded as Q9. That row is inside §10 A.3's MUST, so leaving
  it would have shipped a known-unsound sentence into the acceptance set.
- **charter F10** — the did-not-fire reason is specified as a closed
  token and rendered in §9.2 as free text, a second unchecked prose
  channel. Rules now carry a `no_fire` field (one sentence, no slots)
  reviewed under §8(6) exactly like `template`, and the render is
  `<token> (<no_fire>)`.

Also folded in: **charter F9**'s reframing of §0 (opinions concentrated
in one reviewed file, not made impossible), because B11's disposition
adopts F12's synthesis wholesale and F9 is the claim that makes the
template gate coherent rather than defensive.

**4. One number in the review's own framing is a row/cell conflation.**
"24 rows in the corpus" for the R-DELTA-2+3 compound is four CELLS at six
metric rows each. The note says both, because a fixture built for 24
cells would be wrong.

**5. Length.** The note went 1,228 → 2,391 lines. Every added section is
required by a disposition (a new rule class, an aggregation mechanism, a
predictions redesign with the transcription result, an `inputs` grammar
and view contract, a preconditions section, a six-section check, and a
fully re-rendered 44-bullet specimen with all 31 rules), but an
implementation lane now has ~2,400 lines to hold. If the manager wants it
shorter, the compressible parts are §6.6's transcription table (could
move to this report), §9.2's specimen (could drop to the non-firing table
plus three sections), and §13.

**Nothing in the r4 dispositions struck me as wrong.** The two I refined
(1 and 2 above) were both cases where the disposition named an outcome
and left the mechanism open, and the mechanism I chose serves the same
outcome at lower cost. B5 in particular is as important as the review
says: I found and fixed a second-order consequence of it while building
R-ARM (the config-token rule), which is exactly the "written from the
TSV's columns rather than from the reducer's semantics" failure the
review warned the revision to guard against.

---

## What is NOT done, and what the next step is

- No code, no `catalogue/`, no `pcrecbench/interpret.py`, no
  `docs/dev/predictions/`, no skill directory, no
  `reports/*.interpretation.md`. Verified absent.
- `docs/dev/plan.md` untouched — `[B13]`'s STATE transition is the
  manager's, and per the review's own "what happens next", the row stays
  `not-started` until an implementation lane opens.
- The two reporter **preconditions** (§2.5, P-1 and P-2) are stated but
  not built. They are one reporter change, one `REPORTER_VERSION` bump
  and one regeneration of the committed reports, and they must land
  before the implementation lane, because R-FLOOR-2 and R-STATUS-12 are
  both acceptance-test items that depend on them. That is the one piece
  of sequencing the manager needs to schedule.
- The r4 review's step 2 — a lighter confirmation pass that the revised
  note actually resolves B1-B11/S1-S8, re-verified against source —
  has not been run; that is the manager's call and is what should
  precede opening the implementation lane.

## Summary

`docs/design/interpreter_v1.md` is now v1.1: 2,391 lines, all 11 blocking
and 8 should-fix dispositions applied plus the ~14 documentation
corrections, every corrected number re-derived from source or from the
committed corpus by this lane rather than copied from the critics. The
substantive additions are a seventh rule class (R-ARM), which turns
Frank's `vm-in` acceptance item from a conceded gap into a rule that
fires with the right two numbers; an `aggregate` counted collapse that
takes a modern report's sidecar from ~420 bullets to ~44 without any
ranking by interest; a predictions format that was tested against the
project's only scored prediction set and expresses 12 of its 13; a
template-prose audit with a human review gate, which closes the one hole
in the "no opinions" firewall; and two named reporter preconditions that
let the note's claim of exactly two inputs finally be true. Two rules
were subtracted rather than fixed — R-RANK-2 as incoherent and
R-BUCKET-KB's signature registry as unreachable from the TSV — and both
subtractions are argued in the note rather than quietly dropped.
`make check-schema` is green (4/72/0). The design is ready for the
review's step-2 confirmation; it is not ready to build until the two
reporter preconditions land.
