# Lane `b13skill` — the interpreter, part 2 ([B13.4])

Branch `lane/b13skill`, from master at `1b88882`. Delivered 2026-09-09.
Charter: `docs/design/interpreter_v1.md` v1.2 §9 (the skill and the
sidecar's exact format) — the project skill
`.claude/skills/pcrec-bench-interpret/SKILL.md` and the committed
`.interpretation.md` sidecars for §11 Q5's three acceptance reports.

## 1. Charter-vs-committed checklist

| # | the brief asked for | committed | state |
|---|---|---|---|
| 1 | the skill, running the real CLI, writing `reports/<name>.interpretation.md`, phrasing nothing, stating the opinion firewall, naming the regeneration rule and section 3 as the freshness gate; its row in `.claude/skills/CLAUDE.md` | `.claude/skills/pcrec-bench-interpret/SKILL.md` + `CLAUDE.md`; `.claude/skills/CLAUDE.md` gains its row | DONE |
| 2 | the committed sidecars for §11 Q5's reports (A, B, C), generated from the skill's own command line against the LIVE `store/index.tsv`; the with-predictions decision stated | Three sidecars generated and committed (see §2 below); decision: Report C's sidecar carries `--predictions docs/dev/predictions/syntax-0.1-first.tsv` because §9.1 step 2 makes matching-predictions detection part of the skill's own deterministic procedure (not an optional "variant") — the file's `subbench=syntax, version=0.1` rows match the report header's `filters: subbench=syntax, version=0.1` exactly, so there is exactly one sidecar per report, not a with/without pair | DONE |
| 3 | `make check-interpret` reports the committed sidecars fresh (quote its line); all else unchanged (129 + N); `make check-schema` unchanged | Section 3: **"3 committed sidecar(s) checked (the sidecars themselves are [B13.4]'s deliverable)"**; total **132 passed, 0 FAILED** (129 + 3); `make check-schema`: **4 example(s) accepted, 72 sabotage(s) rejected for the intended rule, 0 sabotage(s) WRONG** (unchanged) | DONE |
| 4 | docs: `reports/CLAUDE.md` sidecar section; `catalogue/CLAUDE.md` Running block mentions the skill; `interpreter_v1.md` STATUS gains one sentence, nothing else in the note changes; this report; the Report A opinion audit | All four landed (see §3, §4 below) | DONE |

Nothing is OWED. No background run is outstanding.

**Validation as run, on this branch, in this worktree:**

```
make check-interpret     132 passed, 0 FAILED   (12/8/4/103/4/1 by section)
make check-schema        4 example(s) accepted, 72 sabotage(s) rejected, 0 WRONG   (unchanged)
```

`pcrecbench/tests/test_report.py` and `make check-harness` were not run:
nothing in this lane touches the harness, adapters or a bench set, and
neither loads a fixed dataset this lane's changes could move.

## 2. The three sidecars, exactly as generated

Command used, per the skill's own §9.1 procedure, from the repository
root:

```
python3 -m pcrecbench interpret reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv \
    --index store/index.tsv --render \
    --out reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.interpretation.md

python3 -m pcrecbench interpret reports/2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv \
    --index store/index.tsv --render \
    --out reports/2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.interpretation.md

python3 -m pcrecbench interpret reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv \
    --index store/index.tsv \
    --predictions docs/dev/predictions/syntax-0.1-first.tsv \
    --render \
    --out reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.interpretation.md
```

All three re-run to stdout and `cmp`'d byte-identical against the
committed file (the skill's own step 4, run by hand here). Sizes:
156 / 330 / 465 lines respectively. Firing counts (headings present):

- **Report A** (email-specimen@0.1): R-STATUS-2 (3), R-STATUS-3 (13),
  R-STATUS-5 (1), R-STATUS-6 (1), R-STATUS-12 (3), R-DELTA-1 (3),
  R-DELTA-2 (6), R-DELTA-3 (4), R-ARM-1 (14→8 bullets), R-FLOOR-1 (2→1),
  R-BUCKET-FORM (2), R-BUCKET-VSBEST (4→1) — twelve rules fire, matching
  `docs/dev/lanes/b13impl_report.md` §3's §9.2-specimen reproduction
  exactly.
- **Report B** (bounded@0.3): matches the §10 B.1-B.7 counts from
  `b13impl_report.md` (R-RANK-1 fires 7 times, not the "at least five"
  the note states — the same finding `b13impl_report.md` §6 already
  flags; unchanged by this lane).
- **Report C** (syntax@0.1, WITH predictions): matches §10 C.1-C.7;
  R-PRED-1/2/3/4 now fire (input present) and score
  `docs/dev/predictions/syntax-0.1-first.tsv`'s P1-P13 exactly as
  `docs/dev/predictions/CLAUDE.md` states (4 confirmed / 4 refuted /
  5 partial parent verdicts).

Index used: the **live** `store/index.tsv` (160 rows at commit time),
per the skill's default and per `make check-interpret` section 3's own
re-render rule, which reads the sidecar's own stamped `index:` path
(`store/index.tsv` here) and re-resolves it from the repository root —
confirmed by reading `catalogue/check_interpret.py`'s `section_3()`
before generating anything: it builds `report = ROOT/stamp["report"]`
and `index = ROOT/stamp["index"]` and re-runs `interpret` against
**whatever is at that path now**, never a frozen snapshot. This is the
brief's "if section 3 re-renders from the stamp's own index: path and
sha256, the live index is right" branch — followed, not the golden's
frozen-snapshot behavior (that split is `check-interpret` section 2's
own, for the goldens only, and is unaffected by this lane).

**Consequence worth flagging for the manager**: because section 3 reads
the live index at check time, a sidecar generated today can go stale
the moment a *new* record lands in `store/index.tsv` for one of these
three reports' (subbench, version, machine) — most directly on
R-STATUS-2, whose whole job is to look outside the report's own
population. This is stated in the skill's "Regeneration" section and in
`reports/CLAUDE.md`'s new sidecar section. It is not a defect of this
lane's work; it is the same tradeoff `interpret`'s human-run default
already makes (§2.2), now inherited by a sidecar that is committed
rather than run ad hoc.

## 3. The opinion audit (Report A's sidecar, read end to end)

Read `reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.interpretation.md`
in full (157 lines) as the first fresh reader, looking for any sentence
that is not traceable to a catalogue template, a static `no_fire`
sentence, the aggregation boilerplate (`Also:` / `All N in the facts
TSV.` / `Extremal by …` / `Minimum by …`), or a `links` entry.

**Finding: none.** Specifically checked and found template-traceable,
not opinion:

- The two `See: docs/design/record_schema.md#5. The fixed enums
  (OD-B4 (a))` lines (R-BUCKET-FORM) — the trailing clause is the
  TARGET document's own section-5 heading text, resolved mechanically
  by the link validator (§7.3), not authored prose about what §5 says.
- The `See: docs/dev/feedback_pcrecdev1_2026-08-25-repin-v2.md#(2)
  STILL INTERPRETED / WRONG / AMBIGUOUS` line (R-STATUS-12) — likewise
  a resolved section heading from the linked file, not a claim made
  here.
- Every extremal/minimum sentence states a ratio and a spread bound and
  stops (`×N.NN, beyond 2 × max(stddev) = M ns`) — no adjective, no
  causal clause.
- The did-not-fire table's eighteen reasons are the catalogue's static
  `no_fire` strings (§7.1's rule, confirmed in
  `docs/dev/lanes/b13impl_report.md` item 6) — none of them names a
  report-specific number, consistent with the design.
- No occurrence anywhere in the file of `because`, `due to`, `caused
  by`, `better`, `worse`, `should`, or any comparative adjective outside
  a `×N.NN` ratio — the same MUST-NOT check §10's acceptance test runs
  mechanically, re-confirmed here by eye.

## 4. Docs

- `reports/CLAUDE.md` gains a new section, "`.interpretation.md`
  sidecars ([B13.4])", right after the file's opening paragraph: what a
  sidecar is, its stamp, that it is generated and never hand-edited (a
  wrong finding routes through the catalogue, never a hand patch), the
  regeneration triggers, and which three are committed today.
- `catalogue/CLAUDE.md`'s "Running" block gains one paragraph pointing
  at `/pcrec-bench-interpret` as how a sidecar is actually produced,
  rather than the raw `interpret --render` invocation being read as the
  whole procedure.
- `docs/design/interpreter_v1.md`'s STATUS block gains one sentence:
  "[B13.4], **IMPLEMENTED (lane `b13skill`, 2026-09-09)**: the skill at
  `.claude/skills/pcrec-bench-interpret/SKILL.md` and the three §10
  acceptance-report sidecars committed under `reports/`." Nothing else
  in the note was touched — confirmed by `git diff
  docs/design/interpreter_v1.md` showing exactly this one insertion.
- `.claude/skills/CLAUDE.md` gains the new skill's row.

## 5. What this lane does NOT do

Does not touch `catalogue/rules.toml`, `pcrecbench/interpret.py`, or any
fixture/golden file — no rule's predicate, threshold or template
changed, so no `catalogue_version` bump was needed and none was made.
Does not regenerate any of the other 39 committed report groups' sidecars
(§11 Q5: on demand only). Does not run `make check-harness` (no harness
change; ~20 min box cost not spent).
