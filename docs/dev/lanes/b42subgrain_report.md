# lane b42subgrain — interpret at subject grain (design note)

**Branch** `lane/b42subgrain`, worktree `worktrees/b42subgrain`, one
commit `9a03263`. **DESIGN ONLY**, as chartered: no code, no catalogue
change, no reporter change, no record touched. Diff is exactly two files.

## Deliverable

| file | state |
|---|---|
| `docs/design/interpret_subject_grain_v1.md` | NEW, 640 lines, PROPOSED (not adopted), D6-panel-ready |
| `docs/design/CLAUDE.md` | entry added after `interpreter_v1.md` |
| this report | committed |

## Charter items, one by one

All six brief items are covered; nothing is OWED.

1. **Why 6 of 10 were machine-unevaluable — derived, not asserted.** §1.
   Done by re-resolving all fifteen clause rows of
   `docs/dev/predictions/capability-0.1-first.tsv` through `interpret`'s
   OWN `parse_selector` / `_glob_match` / `_select`, against the committed
   set-grain TSV. Result contradicts the ledger's single-cause reading.
2. **The options, with costs.** §2, five of them — (a) second input,
   (b) selector extension, (c) per-grain runs, plus two the analysis
   surfaced: (d) subject rows inside the set-grain TSV, (e) a subject-grain
   row SLICE. Each with determinism, fixture/golden strategy and catalogue
   versioning; summary table at §2.6.
3. **KB-16.** §3. Every option preserves the no-store-load invariant;
   the cost is priced and located on the reporter, not the interpreter.
4. **P2/P3/P4/P6/P7/P10 as acceptance cases.** §4, one subsection each
   plus a scoreboard at §4.1.
5. **P5 rank-blindness — mandate `section=`?** §5, both sides argued,
   settled by a corpus measurement, recommendation at §5.4.
6. **Numbered questions for Frank.** §6, eleven, each with a
   recommendation.

## The findings that matter (numbers inline)

**1. The ledger's diagnosis is right for four of the six and wrong for
two.** The eleven zero-matching clauses have THREE causes:

| cause | clauses | fixed by a subject-grain input? |
|---|---|---|
| A — grain gap: a real subject id against the literal `(set)` (`report.py:4413`) | 7 (P3, P4.b, P6.a, P6.b, P7, P10.a, P10.b) | **yes** |
| B — `regime_or_na=n/a` against the `compile` section's EMPTY string (`report.py:4493`) | 2 (P2.a, P2.b) | **no, at any grain** |
| C — `testee=pcrec_*-auto-*` matches no testee (`pcrec_a770139e_auto-caps-simdna` has `_auto-`, not `-auto-`) | 2 (P4.a, and jointly P4.b) | **no** |

MEASURED against a real subject-grain TSV of the identical query: P3
matches 6 rows, P6.a/P6.b 18 each, P7 24, P10.a/P10.b 18 each — while
P2.a/P2.b and P4.a/P4.b still match **zero**. So "give interpret a
subject-grain input" is necessary and **not sufficient**; without the two
authoring fixes the next sample reports 2 of 10 not-evaluable and a reader
would reasonably read those as genuine measurement gaps.

**2. `interpret --subject-grain` already exists, and its firing path has
never run.** The flag ships (`interpret.py:2101`), is threaded to
`InterpretCtx.subject_grain`, and one rule consumes it
(`r_bucket_dominated`, `interpret.py:1084-1087`). What is missing is the
committed file (0 of 43 report groups have a `.subject-grain.tsv`; all 43
have a `.subject-grain.md`), the prediction evaluator's route to it
(`_select` reads the primary report only), and —

**3. A live latent defect, independent of every ruling.** `build_stamp`
(`interpret.py:2067-2086`) does not record the subject-grain input, and
`check_interpret.py`'s section-3 freshness re-render calls
`run_interpret(report, index, pred, "md")` with no subject-grain argument
(`check_interpret.py:254-267`). A sidecar rendered today WITH the flag
re-renders WITHOUT it, its facts differ, and `make check-interpret`
section 3 fails on an unmodified file. Unexposed only because no sidecar
uses the flag; every option in §2 exposes it. Recommended fixed
unconditionally (§6 Q10).

**4. Option (c) — per-grain interpret runs — is refuted by the
catalogue.** All four R-PRED rules declare `grain = ["set"]`, so on a
subject-grain report no prediction is scored at all. And flipping them is
not a wording change: MEASURED on the real subject-grain file, `n` is 5
(trials) where the set-grain rows carry 75 (subjects), and **0 of 202,794**
subject-grain `rank` rows carry a non-empty `delta_verdict`.

**5. Sizes, measured, which is what decides the recommendation.**

| artifact | lines | bytes |
|---|---|---|
| set-grain TSV (committed) | 8,217 | 1,230,812 (1.17 MiB) |
| full subject-grain TSV | 206,331 | 35,126,390 (33.5 MiB) — **×28.5** |
| proposed row SLICE | 34,251 | 5,895,262 (**5.62 MiB**, ×4.8) |

The slice keeps `record` rows plus ranking-family rows whose `metric` is
`median_ns` / `pass_rate` / `giveup_smallest`, and is a strict superset of
everything §4's acceptance cases and R-BUCKET-DOMINATED's own declared
`inputs` need. Same 18 columns, same header — `ReportTsv` reads it with no
code change.

**6. KB-16 is preserved by all five options**, because each hands
`interpret` a committed TSV. The cost lands on the reporter: the
subject-grain render MEASURED at **100.75 s wall / 678,016 KB peak RSS**
(same order as KB-16's own committed AFTER row, 116.78 s / 762,940 KB), a
**fourth** store load per report group on top of the three already paid
(`.md`, `.tsv`, `.subject-grain.md`) — ~33 % more, not a new class of cost.
Recommended UNCOUPLED from a one-load-many-renderings reporter change
(§6 Q5); that change's ~3× saving is flagged UNMEASURED.

**7. P5's rank-blindness, settled by measurement.** Scanned all 43
committed `reports/*.tsv`:

> **92,892 `rank` rows. ZERO carry `n_wrong > 0` or `n_gave_up > 0`.**
> 111 `excluded` base rows, of which **33 carry `n_wrong > 0`.**

So `n_wrong eq 0` over `_select`'s default `rank` section is a corpus-wide
TAUTOLOGY — R-PRED-1's "confirmed" on P5 could not have failed, and the
population the prediction exists to check is exactly the 33 rows it is
structurally forbidden from seeing. **Recommendation: do NOT mandate
`section=`.** Instead (α) make the default read `rank` **and** `excluded`
for the four failure-population quantities, and (β) have a confirmed
prediction ANNOUNCE the elsewhere-population it did not read (`_elsewhere`
already computes it, `interpret.py:1737-1742`, and is consulted only when
the primary selection is empty). Full both-sides argument at §5.3; the
case against the mandate is that it buys ritual compliance — `section=rank`
written explicitly is exactly as blind — at the price of a corpus-wide
migration of every `n_wrong` row in two committed prediction files.

**8. Two store-free load-time checks** proposed (§4, §6 Q6) that turn
causes B and C into named LOAD ERRORS at authoring time, on the discipline
`docs/dev/predictions/CLAUDE.md` already states: a `compile:` quantity's
selector may not name `subject_or_na`/`regime_or_na`; a `testee=` glob must
match ≥1 index testee for its own measured `(subbench, version)`, vacuous
when unmeasured (the shape `check_stated_utc` already uses).

**9. Two prediction notes describe claims inexpressible at ANY grain.**
P6.b ("the grok import still HITS the same subject — the pair diverges")
and P7's "IDENTICAL answers" half are ANSWER claims, and §6.4 says the TSV
carries no answer, span or capture at either grain. Subject grain rescues
the clause that was written, not the claim the note describes. Worth
saying in the file rather than rediscovering next sample.

## Validation

**COMPLETE.** Four read-only probes (§0 of the note), plus:

- `make check-interpret` — **133 passed, 0 FAILED** (sections 12/8/5/103/4/1)
  on this branch, confirming the note changed nothing it describes.
- `git diff --name-only HEAD~1` — exactly
  `docs/design/CLAUDE.md` and `docs/design/interpret_subject_grain_v1.md`.
- Every line-number citation in the note was re-grepped against `HEAD`
  after drafting; three were corrected in place (`interpreter_v1.md:2190`
  for §8(4)'s heading, `:483` for the `expectation_detail` follow-up, and
  the report-corpus counts re-derived as 43/43/43/0/4 rather than quoted
  from `reports/CLAUDE.md:38`'s 42-group vintage).

`make check-harness`/`check-report` were NOT run: this lane changed no
code, no schema, no bench file and no report, and both are heavy
store-touching suites the boilerplate keeps off a docs lane.

## Scope and box discipline

Worktree-only, `git rev-parse --show-toplevel` verified before the first
edit. `~/pcrec` never read or written. The one background job (the
subject-grain render, M3) ran DETACHED with a durable marker per the
boilerplate's store-loading rule, and its marker was checked before this
report was written: `sg.done` present, log tail `DONE rc=0`, 100.75 s,
678,016 KB. Its output TSV lives in the session scratchpad and is **not
committed** — it is reproducible byte-for-byte from the report's own
committed query with `--grain subject --format tsv`. No outstanding
background job.

## For the manager

- Merge, then the note wants a **D6 critic panel** before adoption — it is
  written for one (contested cells marked MEASURED/UNMEASURED, every claim
  cited to a `file:line` or a probe).
- §6 Q10 (the `--subject-grain` stamp gap) is the one item that should be
  fixed **regardless of the panel's outcome or Frank's rulings** — it is
  broken at `HEAD` today.
- Ledger checklist item 1 for the next capability sample should be
  re-worded: a subject-grain input alone leaves P2 and P4 exactly where
  they are, and item 2's P5 re-transcription is superseded by §5.4's
  recommendation (fix the default, not the 9 rows).
