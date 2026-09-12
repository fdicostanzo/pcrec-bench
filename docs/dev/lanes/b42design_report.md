# Lane `b42design` — [B42] phase (b), the capability-set design note

Branch `lane/b42design`, off master at `ed8bc0f`. Opus tier, design lane:
no builds, no measurements, no package installs, nothing under `bench/`,
`schema/`, `pcrecbench/` or `testees/` touched. Scratch: none needed.

## Delivered

| file | what |
|---|---|
| `docs/design/capability_set_v1.md` | the design note, v0.1 "draft for panel", 13 numbered sections + Appendix A |
| `docs/design/CLAUDE.md` | its row (the only lane touching this file) |
| `docs/dev/lanes/b42design_report.md` | this file |

Two commits. Not merged.

## Charter-vs-committed checklist

### The thirteen sections the brief named

| § | required content | where | state |
|---|---|---|---|
| 1 | charter restated + traceability table | §1, §1.1 (a row per requirement) | **done** |
| 2 | new set vs extend `bench/syntax`; directory name, version, relationship to the five existing sets | §2 (four reasons against extending; §2.4's cite-don't-duplicate table, one row per existing set) | **done** |
| 3 | family taxonomy with mechanism / wild source + licence + retrieval status / designed members / expected `unsupported` / target count; totals; subjects; regimes; floor; cell-time arithmetic vs `CELL_CAP` | §3.1 (12 families), §3.2-3.5 | **done** |
| 4 | provenance record; licensing-floor OPTIONS + recommendation; wild-vs-designed ratio options; subject-data provenance options; Davis specifically incl. the MIT/"Other (Open)" mismatch | §4.1-4.5 | **done** |
| 5 | REQUIRES vocabulary; per-engine declarations; pre-compile policy; outcome-enum reuse (adopt or refute N2 §7); `refusal_class`; the three conventions + Hyperscan all-ends options; variant visibility on the scoreboard | §5.1-5.7 | **done** (N2 §7 ADOPTED, reasoning re-derived; a 16th REQUIRES tag `true-end-anchor` ADDED on N2 §5's TRE evidence) |
| 6 | where a variant lives; the adopted rewrite table; the hazard-class rule; the equivalence check and its gate | §6.1-6.4 | **done** |
| 7 | compile time per class + phases; the `cost_class` question; artifact size + non-comparability; peak memory; the recorded/scored/caveated table | §7.1-7.5 | **done** |
| 8 | named configs per engine; the `testee_id` composition rule; v1 vs later; python/perl scope | §8, §8.1 | **done** (python/perl ADOPTED; **new finding**: it needs no schema change and no "partial regime" concept — a record with compile rows and no match rows is already legal and its `trial_agreement` already defined) |
| 9 | adopt Option B or argue otherwise; file layout; the loader change; the `make check` gates incl. [B38]'s round-trip; `source_ref`; the four asks; the newline/free-spacing limit | §9.1-9.7 | **done** (Option B ADOPTED; [B38]'s round-trip gets an explicit fate; the newline limit is upgraded from N3's "forward risk" to a handled current one, because family 6's `(?x)` member hits it) |
| 10 | the data shapes a later UI consumes; what is sufficient, what is missing; build nothing | §10 (three shapes sufficient, four gaps named (a)-(d)) | **done** |
| 11 | lanes + order; sizing; Frank's install line; predictions and outlier rule before the run; the first night's shape | §11.1-11.4 | **done** |
| 12 | ONE consolidated deduplicated question list, each with recommendation + consequence per answer + BLOCK/DEFAULT | §12, fourteen rows | **done** |
| 13 | risks and what would refute this design | §13 (nine risks + three refuters) | **done** |

### The eight charter requirements

Each maps to a section in the note's own §1.1 table: (1) §4, (2) §3,
(3) §7, (4) §9, (5) §8, (6) this note + phase (c), (7) §10, (8) §12.
Plus the two standing clauses — capability first-class → §5, syntactic
adjustment → §6.

### Reading done, in the brief's order

`plan.md`'s `[B42]` and `[B7]` rows; the three research notes IN FULL
including both follow-up sections; `APPROACH.md`;
`docs/design/requirements.md` in full; `record_schema.md` §§5, 6.4, 6.8,
7, 8 (setup / patterns / match / compile field tables) and §9's opening;
`subbench_directory_model.md` §0-1.3; `bench/syntax/NOTES.md` and
`CLAUDE.md` in full, plus `bench/CLAUDE.md`; `docs/dev/predictions/
CLAUDE.md`; `docs/design/CLAUDE.md`; `docs/dev/reviews/2026-09-07-r4-
interpreter-v1.md` (opening + finding shape); the [B36] syntax-first
ledger's §9 Tier A; `scripts/CLAUDE.md`'s measured cell-time table and
`CELL_CAP` paragraph; `store/index.tsv`'s header and a committed report
TSV's header + column row (for §10).

`docs/design/interpreter_v1.md` §6 was read at second hand through
`docs/dev/predictions/CLAUDE.md`, which states the fifteen-column format,
the closed sets, the `stated_utc` rule and the inexpressibility rule in
full. That is what §11.3 needed; the note cites the CLAUDE.md, not §6.

## OWED — nothing

No background job was launched, no number is outstanding, no section is
partial. Three OWED items are recorded IN the note as inputs the BUILD
lane owes (Appendix A: rebar's `noseyparker.txt` literal text, CRS
942360's untruncated text, the CVE index for family 10) — those are
[B42] phase (e)'s, not this lane's.

## What the panel should aim at first

Named in the note's own §13, repeated here so the panel brief can quote
it:

1. **Q10 / §9.** If "BUILT ON the .rxt format" means `pcrec --source`-
   buildable, Option B is wrong and D93 plus [B29] §4.1's compile-cost
   objection both re-open.
2. **§5 / R2.** The capability contrast may already be answered by N2
   §3's fetched documentation table. If measurement only confirms it, the
   family taxonomy should be rebuilt around cost, not capability.
3. **§4.3 / §3.1.** 30 wild members assumes N1's fetch status holds. Two
   of the twelve families rest on text that is still OWED or was never
   obtainable.
4. **§13 R8.** `fidelity: inspired` is a named laundering surface, not a
   formality.
5. **§3.5.** The decision to drop the `match` regime is the largest
   single scope cut in the note and rests on one ledger's Tier A.
