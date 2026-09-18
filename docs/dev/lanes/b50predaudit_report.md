# lane `b50predaudit` — THE PREDICATE AUDIT: delivery report

Branch `lane/b50predaudit`, off `master` at `4eb413a`. Opus lane,
2026-09-18. **DOCS ONLY: no code, no catalogue, no reporter, no record,
no report regenerated.** Nothing under `pcrecbench/`, `catalogue/`,
`schema/`, `reports/`, `store/`, `bench/`, `testees/` or `~/pcrec` is
touched. The note proposes; fixes land on a ruling, as the brief says.

## Charter-vs-committed checklist (session_discipline.md §7(c))

| the brief asked for | committed as | state |
|---|---|---|
| read `docs/dev/lanes/BOILERPLATE.md` first and follow it | worktree off master, branch `lane/b50predaudit`, `git rev-parse --show-toplevel` verified before the first edit, incremental commits, no heavy run, `make check-interpret` only | DONE |
| study the canonical P5 instance first | `predicate_audit_v1.md` intro + §0 fact 1 (the tautology re-derived at 103,488 `rank` rows, up from the v1.4 note's 92,892) | DONE |
| read `interpreter_v1.md` v1.4 (§6.7), `catalogue/rules.toml` in full, `interpret_subject_grain_v1.md`, the two newest sidecars, `pcrecbench/interpret.py` | all read in full; every rules.toml `threshold_src` citation followed into `report.py`/`reduce.py`/`interpret.py` (the §2 table's (a) column is the code path, not the prose) | DONE |
| a table answering (a)-(d) for EVERY rule | §2 — 28 rows covering all 31 rules (R-PRED-1..4 share one row and are expanded in §3) | DONE |
| a table answering (a)-(d) for every prediction quantity | §3.1 — all **17** `QUANTITIES` members in five classes; §3.2 adds the same audit per PIPELINE STAGE (`_sections_for` → `_select` → `_keyed_values` → `_reduce` → `_op_holds` → `_measured_text` → `_elsewhere` → the roll-up) | DONE |
| flag every template whose sentence states a verdict without its population | §5, the separate rendered-sentence audit: 8 surfaces flagged, 3 named as the models to copy | DONE |
| findings ranked, with fixes and their version implications | §4 (F1-F25, each with severity, witness, fix shape and MINOR/MAJOR label) + §6 (four cost groups + a recommended order) | DONE |
| name any rule whose verdict on a COMMITTED sidecar is structurally unsound | **F1 named prominently** in the status paragraph, the CLAUDE.md entry and §4: R-FLOOR-2 at `reports/2026-08-25-email-specimen-0.1-…-repin-692c2e8.interpretation.md:152`. F2, F3, F4 named beside it | DONE |
| `docs/design/predicate_audit_v1.md`, D6-panel-ready | committed, 833 lines: status block, §0 method, §1 the four questions, §2/§3 the audit tables, §4 the ranked findings, §5 the sentence audit, §6 the costed fixes, §7 seven questions for the panel, §8 what it does not decide, source header | DONE |
| the lane report (charter-vs-committed) | this file | DONE |
| NO code or catalogue changes | verified: `git diff --stat master` touches only `docs/` | DONE |

Not in the brief, added because the project's own convention requires it
(BOILERPLATE "update the owning directory's CLAUDE.md"; measurements/
CLAUDE.md's archived-probe rule):

- `docs/dev/measurements/2026-09-18-predicate-audit-probes.txt` +
  `…-probe1.py` … `…-probe5.py` — the five probes archived with a source
  header and verbatim output, reproducible with
  `PCRECBENCH_ROOT=<checkout> python3 <probe>`.
- `docs/design/CLAUDE.md` and `docs/dev/measurements/CLAUDE.md` entries.

## What the audit is, in one paragraph

Every rule and every prediction quantity was asked: what population does
the predicate ACTUALLY read (by code path); what counterevidence would
refute the verdict it renders — its `no_fire` sentence included, since a
negative is the one verdict nobody double-checks; can that counterevidence
appear there; and if not, what is the failure shape. Five read-only probes
supply the numbers, each importing `pcrecbench.interpret`'s own functions
rather than reimplementing a predicate it is auditing.

## Headline findings

**Ten LIVE** (a committed sidecar renders a structurally unsound verdict
or an uninterpretable number today):

1. **F1, R-FLOOR-2 renders a verdict it never evaluated.** `floor_pattern`
   absent / `none` / multi-valued returns `no-matching-rows` and the
   renderer pairs every token with the rule's `no_fire`, so the sidecar
   reads *"no-matching-rows (no ranked cell is at or below its set's own
   floor pattern on the same testee and regime)"* for a set with **no
   floor pattern at all**. Witness: the email repin-692c2e8 sidecar,
   line 152 (MEASURED: 2 of 45 committed reports read `floor_pattern:
   none`, and that is the one with a sidecar). **A build deviation, not a
   design gap** — `interpreter_v1.md` §4.5 specifies
   `no-matching-rows (floor_pattern: none)` verbatim, and the code has no
   channel for the parenthetical.
2. **F2**, the same mechanism on R-DELTA-4's `input-absent`: *"every
   finding … is covered by a prediction selector"* rendered because there
   was nothing to cover with.
3. **F3, R-DELTA-4 denies a prediction that names the cell.** `coverage`
   is built only from clauses whose `_select` returned rows, so a
   not-evaluable clause contributes nothing. The capability AFTER sidecar
   names *"codegrammar-flat / large-subject-throughput … and no
   prediction in …capability-0.1-first.tsv selects that cell"* while P3's
   selector in that file reads
   `pattern=codegrammar-flat;…;regime_or_na=large-subject-throughput`.
   6 of 10 capability predictions are not-evaluable; 777 R-DELTA-4
   firings.
4. **F4, R-BUCKET-DOMINATED's "this cell's total" is neither.** MEASURED:
   **8 of 33** firings on the capability AFTER report are about set cells
   the same report EXCLUDED from ranking, and the denominator omits the
   failing subjects — *"`lp-atomic-nonmatch` is 94.6% of this cell's
   total"* is a sum over 73 ranked subjects with 2 excluded ones unseen,
   eleven lines below the same sidecar's own *"…is EXCLUDED from ranking…
   10 give-up trial(s)"*.
5. **F5** R-BUCKET-KB's `no_fire` says "catalogue 1.0" at catalogue 2.0,
   on all six sidecars.
6. **F6** *"over N value(s)"* is a ROW count, so it is **6× the cells**
   for a rank quantity and **1×** for a compile quantity in the same
   sidecar (P1.a "18" = 3 cells; P5.a "321" = 66 cells; P13 "834" = 834
   cells).
7. **F7** (β) annotates a compile-cost claim with `excluded (23)` match
   rows — a different population entirely; **F7b** (β) is blind wherever
   the selector names a column the other sections leave empty, which
   **falsifies a committed catalogue `example`**: R-PRED-3's own text says
   syntax P2.d is not evaluable because the cell is in `did_not_compile`;
   the tool in fact prints the bare "no row … matches the selector",
   because P2.d names `form=` and `did_not_compile` rows carry no `form`.
8. **F8** A `partial` parent — the catalogue's own modal outcome —
   renders NO numbers: R-PRED-4's slots discard the `claim`, the
   `measured` value and the not-evaluable reason, all three computed.
   Four of the six sidecars carry `partial` predictions.
9. **F22** R-STATUS-8 prints "30.15%" with no statement that the
   project's quiet bar is 10% and that this number is provenance, not the
   gate.

**Twelve silent omissions or latent**, the two largest structural:

- **F9** R-ARM-1 cannot see an arm pair one of whose arms REFUSED to
  compile — the strongest possible arm difference, and exactly the shape
  the deny-flag testees exist to measure. MEASURED: **532** (cell, ranked
  arm, refused arm) triples satisfy R-ARM-1's own one-token rule; clean
  witness `bench/loglines` `level-context`, `…_vm-caps-simdna` ranks
  while `…_auto-caps-simdna` is in `did_not_compile`. A new rule
  (R-ARM-2) is a MINOR fix and the highest-value single addition found.
- **F10** The reporter has **no "was measured, now failing" verdict**, so
  the whole R-DELTA class is blind to a regression that removed a cell
  from the ranking (R-DELTA-3 covers only the improvement direction).
  MEASURED: 38 such pairs in the corpus, all 38 improvements — an
  asymmetry that has not yet cost a missed regression, which is luck.
  PRECONDITION-shaped, on §2.5's P-1/P-2 precedent.
- **F13** Ruling (α) made the counterevidence REACHABLE, not WEIGHTY:
  MEASURED at **0.6-4.7%** of the rows a clause reduces over (P5.a: 3 of
  321 rows carry it). Sound under `identity` (P5 still refutes) and
  outweighed 100-158:1 under `median`/`count`/`max`/`min`.
- **F11** R-BUCKET-SPAN's partner population is NOT the reporter's,
  though the catalogue asserts it is; 4 measured Δ rows have a partner in
  `excluded` that the rule cannot reach. **F12** R-STATUS-1 silently
  treats a record that joins to no index row as `measured`. **F14**
  `metric` is not a selector key, so an explicit `section=excluded`
  clause reduces TRIAL counts and SUBJECT counts together (25 + 9 rows
  MEASURED; a committed clause already uses the shape and escaped only
  because its cell had no give-ups). **F15** three quantity/op
  combinations are decided before any measurement, one of them exiting on
  a bare `ValueError` instead of the exit-2 named error. **F16** "worst"
  is the wrong extreme for a lower-bound op (P7.a computes 89.000 where
  the worst violator is 61.000) — hidden today by F8, visible the moment
  F8 is fixed. **F17-F21** boundary, narrowing and rendering items.

**Audited CLEAN, recorded so a later pass does not "fix" them:** F23
R-FLOOR-1/3's jitter population is exactly the compiled cells (all 1,266
omitted ones are refusals — a cell with no compile time has no jitter);
F24 R-BUCKET-FORM's rankable-only read is deliberate and stated in its own
predicate. **Inert rather than sound:** F25, `not_ranked` and `scratch`
have ZERO rows in all 45 committed reports, so R-STATUS-11 has never fired
and (α)'s omission of `not_ranked` is untested, not safe.

## Validation run

`make check-interpret` (the only run the brief allows — ~30 s, store-free):
**149 passed, 0 FAILED** — sections 1/2/3/4/5/6 = 12/8/7/117/4/1, and
`gen.py --check` 211 files in 65 fixtures ok. Section 6 (the
template-diff gate, which legitimately fails in a lane worktree when a
lane touches prose) **passes**, because this lane touched no `template`,
`no_fire`, `legend` or `links` field. Nothing else was run: no store load,
no report regeneration, no engine, no `make check-harness` (the peer
session may hold the box).

## Open items the lane hands back

- **Nothing is OWED to complete this deliverable.** The note is finished
  and self-contained.
- **Every fix is a RULING**, not an omission: §6 groups them by cost and
  §7 puts seven questions to the panel. The one that will recur beyond
  this note is **Q2**: when the code and the catalogue's own
  `predicate`/`threshold_src` prose disagree and the PROSE is right (F3,
  F11), is the code fix MINOR or MAJOR? The note recommends MAJOR.
- **A plan row.** The audit is chartered under `[B42]`'s tail charter (i)
  and has no row of its own; if the manager wants the fixes tracked
  separately they want a row, because they span code-only, MINOR, MAJOR
  and reporter-precondition tiers.
- **A suggestion, not a request:** §7 Q7 asks whether the audit's
  invariants should become a seventh `check-interpret` section — no prose
  names a catalogue version, every declining rule has a reason distinct
  from its `no_fire`, every quantity/op pair is legal. The note
  recommends yes **after** the fixes land, since a gate written now would
  encode today's shape.

## Commits

```
d94fa32  [B50] WIP: archive the predicate-audit probes (5 scripts + output)
84e9f60  [B42] tail (i): the PREDICATE AUDIT -- docs/design/predicate_audit_v1.md
         (31 rules + 17 prediction quantities, 8 live defects, 5 archived probes)
<this>   [B42] tail (i): count corrections + the lane report
```

(The second commit's subject says "8 live defects"; the count was
corrected to **ten** in the third commit after F7b and F22 were promoted
to LIVE and F14 demoted to latent-with-a-live-mechanism. The note, the
`docs/design/CLAUDE.md` entry and this report all read ten.)
