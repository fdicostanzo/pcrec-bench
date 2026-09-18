# R7 — the consolidated panel on `predicate_audit_v1.md`

Consolidation of the three read-only R7 critic passes over
`docs/design/predicate_audit_v1.md` (v1, `HEAD` = `4eb413a` at critique
time): population semantics / measurement validity
(`2026-09-18-r7-predicate-audit-popsem.md`, r7pop-1..5), catalogue/
interpreter versioning and contract consistency
(`2026-09-18-r7-predicate-audit-versioning.md`, r7ver-1..9), and code
reality — does every claimed code path exist exactly as cited, does every
proposed fix actually work in the code as written
(`2026-09-18-r7-predicate-audit-code.md`, r7code-1..3). Seventeen findings
total. This file applies the manager's triage dispositions; it does not
re-litigate them. Where a disposition proved impossible to apply exactly
as stated, it is marked ESCALATED with the reason, per the brief — none
were.

## Completeness check (run, not assumed)

```
$ grep -oE '\br7pop-[0-9]+\b' docs/dev/reviews/2026-09-18-r7-predicate-audit-popsem.md | sort -u
r7pop-1
r7pop-2
r7pop-3
r7pop-4
r7pop-5

$ grep -oE '\br7ver-[0-9]+\b' docs/dev/reviews/2026-09-18-r7-predicate-audit-versioning.md | sort -u
r7ver-1
r7ver-2
r7ver-3
r7ver-4
r7ver-5
r7ver-6
r7ver-7
r7ver-8
r7ver-9

$ grep -oE '\br7code-[0-9]+\b' docs/dev/reviews/2026-09-18-r7-predicate-audit-code.md | sort -u
r7code-1
r7code-2
r7code-3
```

5 + 9 + 3 = **17**, matching the brief's own count exactly. Every id named
in the brief (`r7pop-1..5`, `r7ver-1..9`, `r7code-1..3`) appears in its
source file and is disposed of in the table below — no id is silently
dropped, and none of the three critic files carries an id outside this
set.

## By-id disposition table

| id | lens | disposition | where applied |
|---|---|---|---|
| r7pop-1 | popsem | **applied** | §7 Q4 rewritten: struck the uncited "changes every … median … one" claim, replaced with the hand-derivation showing `median` is unchanged (0) either side of the collapse and the clean:dirty ratio moves 106:1 → 21:1 |
| r7pop-2 | popsem | **applied** | F13's finding text split by reducer: `median`/`min` at risk (different shapes), `max` least-vulnerable, `count` value-blind (a different problem, F6's) |
| r7pop-3 | popsem | **applied** | F11's fix shape corrected: the `did_not_compile` half of the widening cannot join on `form` (always empty); only the `excluded` half is reachable as stated; the `did_not_compile` half marked TBD-at-implementation |
| r7pop-4 | popsem | **applied** (folded into F27 per manager's r7code-1 instruction) | F27's §4 entry and §7 Q7 now state the cross-testee/cross-config look-ahead gap the re-anchor does not close, as a risk for the ruling |
| r7pop-5 | popsem | **applied** | F1's fix shape now specifies wording for all three of `r_floor_2`'s early-return causes (absent / `none` / multi-value), states the multi-value case has 0 corpus witnesses |
| r7ver-1 | versioning | **applied** | F7 moved out of "no sidecar regeneration" into a new Group 1B (code only, no catalogue bump, but regeneration required); §6's cost table names the syntax sidecar's committed P13 line as the moved file |
| r7ver-2 | versioning | **applied** | F7b split into F7b-code (Group 1, unchanged) and F7b-example (Group 2, MINOR + regen, no §8(6) named-reviewer line since `example` isn't a gated field) |
| r7ver-3 | versioning | **applied** | New §6.05 subsection on `INTERPRET_VERSION`: states the stamp, its bump rule by the `REPORTER_VERSION` analogy, and folds a required bump into F3/F7/F7b-code/F11/F15/F16/F19/F27's cost lines |
| r7ver-4 | versioning | **applied** | §6 rebuilt as a fix-by-fix cost table with columns for catalogue bump, `INTERPRET_VERSION`, sidecars, fixtures, goldens; F9's new fixture-pair need and F3/F4/F9's unmeasured golden exposure named; recommended order re-derived with those as open, not assumed-clear, caveats |
| r7ver-5 | versioning | **applied** (together with r7ver-6) | §7 Q2 rewritten: strikes the false MINOR-vs-MAJOR binary, states that zero individual-rule field characters move for F3/F11 |
| r7ver-6 | versioning | **applied** (together with r7ver-5) | §7 Q2 cites the 2.0 bump's own precedent (`rules.toml:39-49`, a shared-helper `inputs`-shape change classified MAJOR without editing every affected rule's fields) as grounding for the MAJOR recommendation |
| r7ver-7 | versioning | **applied** (folded into F27 per manager's r7code-1 instruction) | F27's §4 entry and §7 Q7 now state the gameability trade-off (global anchor un-pickable; report-scoped anchor is a function of a post-hoc scope choice) as a risk for the ruling |
| r7ver-8 | versioning | **applied** | F27's cost now names revising `interpreter_v1.md` §6.5 to state the newly-found "mechanically unscoreable" class, consistent with how v1.1-v1.4 each folded a built-vs-designed correction back into the design note |
| r7ver-9 | versioning | **clean** — no note change | recorded below; F1/F2's MINOR label already meets the precedent bar this panel asked other findings to meet |
| r7code-1 | code | **applied** | F27's fix shape rewritten in full: the anchor is the OD-B15 dedup key's minimum timestamp over `index.tsv` rows sharing an included record's `(subbench, version, testee_id, machine_id)` tuple, not the R-STATUS-1/R-BUCKET-SPAN join; `check_stated_utc` needs a `report` parameter; kept "code only, store-free" |
| r7code-2 | code | **applied** | §0's probe table gets a labeling note: M2/M3/M5/M6/M8 are literal archive headers (all inside probe2.py), M1/M4/M7 are this note's own bookkeeping labels with no literal grep target |
| r7code-3 | code | **clean** — no note change | recorded below; a positive finding (no blocking code-reality defect), stated for the record only |

**Escalated: none.** Every disposition in the manager's brief was
applicable to the note as written; none required improvising a ruling the
brief did not give.

## The two CLEAN dispositions, recorded

- **r7ver-9.** F1/F2's recommended "MINOR + §8(6) review + full sidecar
  regeneration" label is the one version label in the v1 note that was
  already fully precedent-grounded on its own terms — it tracks the
  catalogue's 1.0 → 1.1 bump (`rules.toml:66-68`; *"entirely the new
  `legend` field"*) exactly: a new, declared, slot-free prose field on a
  rule's own block, MINOR, §8(6)-reviewed, full regeneration. No edit
  needed; this finding exists so the manager does not "fix" F1/F2's
  treatment along with the others the panel found under-grounded (F3,
  F11's Q2 framing) — it already meets the bar those needed to be raised
  to.
- **r7code-3.** A clean bill of health, stated for the panel's record:
  the code-reality critic checked essentially every code citation and
  fix-mechanism in the note (F1, F3, F4, F8, F9, F10, F11, F12, F14, F16,
  F19, F26, F27, `SELECTOR_KEYS`, `DID_NOT_FIRE_TOKENS`, `_ranking_groups`,
  `set_cells`'s population, `_pred_rule`'s branch structure, and more)
  against the actual files at the reviewed commit and found every
  citation exact and every proposed fix's minimal implementation a real,
  findable seam in the existing functions. This does not change with the
  note's v1.1 revision, since none of the corrected fix designs (F7's
  regrouping, F11's join correction, F27's rewrite) contradict anything
  this finding verified — they refine fix shapes the code-reality pass
  already confirmed were mechanically sound in their unrefined form.

## Panel's overall verdict

**The underlying defects the audit found (F1-F27) are confirmed and
unchanged by this panel.** All three critics independently re-derived
the note's headline claims — the P5-class structural blindness in
R-FLOOR-2, R-DELTA-4, R-BUCKET-DOMINATED and R-STATUS-4; the 532
R-ARM-1-blind arm triples; the R-DELTA regression-direction blind spot;
the six-rows-per-cell/N-means-two-things bookkeeping defect; F27's live
blocker — against the actual committed code, not the note's prose, and
every one checked out. No finding disputes that these are real defects
in the shipped catalogue and interpreter.

**What this panel found, and what it fixed, is a second-order problem:
the audit's OWN remediation reasoning reproduced defects of the same
class it exists to catch.** Five separate instances, now corrected in
v1.1: an uncited "MEASURED" claim about a reducer collapse that hand
computation refutes for the one case checked (r7pop-1); a reducer-risk
generalization that lumped a genuinely-safe reducer (`max`) and a
value-blind one (`count`) in with the two actually-vulnerable ones
(r7pop-2); a fix shape for F11 that could not structurally reach half the
population it named, because the widened section's own join key excludes
it (r7pop-3); a fix shape for F1 that specified wording for one of three
conflated causes and silently assumed the same wording would do for the
other two (r7pop-5); and F27's fix shape naming a join that recovers the
wrong population entirely, which would have shipped a "fix" that does not
close the gap it claims to close on the FIRST finding this note asks the
panel to land first (r7code-1). Layered onto this: the note's own cost
accounting for its fixes was incomplete on two independent axes — it
mis-bucketed two fixes against their own cited evidence (F7/F7b, r7ver-1/
r7ver-2), and it never named a second version stamp
(`INTERPRET_VERSION`) or two of the four regeneration surfaces this
project's own tooling gates on (fixtures, goldens) that several of its
recommended fixes actually touch (r7ver-3, r7ver-4). Two trade-offs the
v1 note presented as strict improvements — F27's re-anchor and (implicitly)
Q2's MINOR-vs-MAJOR framing — needed a counterargument stated explicitly
before a panel should rule on them (r7ver-7/r7pop-4; r7ver-5/r7ver-6).

None of this weakens F1-F27 as findings against the shipped catalogue and
interpreter code — those stand, confirmed by independent re-derivation
across all three lenses. It means the fix designs and the §6/§7 cost
accounting in v1 were not yet safe to hand to an implementer or rule on
as written; v1.1 corrects thirteen of the seventeen findings' worth of
that gap in place, with two recorded clean and none escalated.

## What is owed next

Per the manager's brief, this lane does not merge. The corrected note
(`docs/design/predicate_audit_v1.md`, now v1.1) is ready for Frank's
ruling on §7's questions, now argued with their corrections applied:
Q1 (the reason channel, now three-cause-complete), Q2 (MINOR-vs-MAJOR,
now precedent-grounded), Q3 (F4's fix depth), Q4 (the row collapse, now
correctly scoped to what it fixes and what it does not), Q5 (`metric` as
a selector key), Q6 (F10, filed with a trigger), Q7 (F27's re-anchor,
now with its two risks stated), Q8 (F26), Q9 (a standing check-interpret
section). Two open measurements this panel flagged as unmeasured, not
resolved, and named as such in §6's cost table: whether F9's new
R-ARM-2 rule fires on any of the three acceptance reports (Reports A-D),
and whether F3/F4 move any golden fact — both should be checked at
implementation time before the recommended order's "cheap-then-expensive"
framing is trusted.
