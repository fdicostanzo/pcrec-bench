# lane b117read report — [B117] step (d), the compilee -O-level window READ

**Branch**: `lane/b117read`, worktree `worktrees/b117read`, from master
`1b7b495` (the manager's own "[B117] window done" commit — this lane is a
READ lane over that window's ten new records, not a measurement lane).
`~/pcrec` was not touched. No `store/`/`pcrecbench` code changes; no new
measurements or timing.

## 1. Findings first

1. **All seven predictions REFUTED (R-PRED-2), but the populations behind
   each verdict tell three different stories**, not one uniform "the
   charter's hypotheses were wrong": P1/P3 (`pcrec-auto` predicted flat at
   `-O0`/`-Os`) are substantively wrong — 50/62 and 34/62 of 62 patterns
   exceed the ±15% band, all in the slower direction, median ×2.25/×1.25.
   P2 (`pcrec-auto` flat at `-O3`) nearly holds — 58/62 inside band, the 4
   exceptions all FASTER, never slower. P4-P6 (`pcrec-vm` direction claims)
   are directionally right for the majority (48-58 of 62 patterns) but
   fail the strict per-pattern universal quantifier on a real minority
   (14-24 patterns), several of which move the OPPOSITE direction from
   the claim. P7 (`.so` bytes at `-O0`) mostly holds (56/62).
2. **`pcrec-auto` is not "the DFA route"** (team lead's review, item 1):
   it routes PER PATTERN — 29/62 patterns compile to a pure DFA, 22/62 to
   a VM-hybrid (DFA-side prefilter + VM core), 11/62 to a pure VM program,
   identical across all five `-O` levels (pcrec decides its own route at
   phase 1, before gcc ever sees `-O`). Re-checking P1-P3 against the
   DFA-stamped subset alone does not change the verdict: the DFA-only
   ratio distributions move almost identically to the whole-testee ones
   (`-O0` DFA-only median ×2.2449 vs ×2.2496 unsplit; `-O3` DFA-only
   ×1.0001, tighter than the unsplit ×0.9984). `pcrec-vm` (forced
   `--engine=vm`), by contrast, genuinely IS one uniform route — 62/62 of
   its patterns stamp `engine: vm`, `prefilter: none` — so no re-split was
   needed for P4-P6. A genuinely new finding from the split: `pcrec-auto`'s
   VM-hybrid-stamped patterns are measurably faster at `-O3` than `-O2`
   (median ×0.9683 throughput), the one category that moves in that
   direction consistently.
3. **The 14 `pcrec-vm`/`-O0` "flat" patterns (team lead's review, item 2)
   share one MEASURED mechanism, verified against the records and the
   regenerated throughput subjects, not guessed**: every one of the 14 has
   an `RX_REQ_BYTE` necessary-byte guard whose scanned byte occurs ZERO
   times in all three throughput subjects (direct byte-count over the
   gitignored, deterministic, sha256-verified `bench/capability/
   throughput/*.bin` files). pcrec's own pre-check (a single linear,
   `memchr`-shaped scan) therefore runs to completion and declares
   no-match WITHOUT the VM's dispatch loop ever executing — and that scan
   is glibc's own already-compiled code, never pcrec's emitted C, so our
   phase-2 `-O` flag cannot move it. The split is 100% clean over the
   WHOLE 62-pattern population: all 22 patterns whose necessary byte DOES
   occur, and all 26 with no necessary byte at all, read a real `-O0`
   slowdown; only the 14 zero-occurrence patterns read flat. The `.so`
   artifact DOES differ in size for all 14 at `-O0` (+240 B to +8,512 B) —
   the compiled code genuinely changes, it is just never reached by these
   subjects. Absolute magnitudes confirm it: `floor-byte` (this set's own
   designated near-zero-cost floor pattern) and `mojibake-curly-quote`
   (also zero-occurrence) both read ~23.1 microseconds at EVERY `-O`
   level, while `wild-codegrammar-json-array-begin` (byte occurs up to
   5,985 times) reads 1.11 ms at `-O2` and 10.18 ms at `-O0` on the same
   testee/regime/subjects.
4. **A sidecar-reading quirk, not a tool bug**: `_measured_text`'s "worst"
   witness for a `between` op (`interpret.py:2790`) picks the violator
   with the largest ABSOLUTE ratio among those that fail, which for a
   population whose violations are all on the LOW side (P2, P6) names
   the *least* extreme violator, not the most. Found by computing the
   full violating population directly from the TSV and comparing against
   the sidecar's own named witness; documented in the ledger so a future
   reader does not mistake the sidecar's one witness for the true
   extreme.
5. **Two predictions (P4, P6) carried a column-swap authoring defect**
   (`op=gt` with the threshold in `lo`, `hi` empty — `_op_holds` reads
   only `hi` for every op but `between`) that crashed `interpret` outright
   before any score existed. Fixed in place, same precedent as
   `docs/dev/predictions/CLAUDE.md`'s documented `syntax-0.1-rust-first.tsv`
   P1 fix (every other field byte-identical; not "revising an
   already-scored file," since nothing had scored yet).
6. **`utf8-lead-no-cont` recurs as the single most extreme witness in 5 of
   16 testee × regime × level distributions**, in both directions — not
   traced to a mechanism here, named as a candidate for a future read.
7. **Compile-side**: `-O0` is the one level with a real, across-the-board
   `.so`-size cost on both testees (median ×1.13-1.14); `-O1`/`-O3`/`-Os`
   all read flat at the median. `-O1`, named by no prediction, costs real
   time on both testees (median ×1.04-×1.16) — an uncovered finding worth a
   clause in any future predictions file on this axis.

**Revision note (2026-10-01, same lane, after the team lead's review of
the first commit c24995e)**: findings 2 and 3 above are new, added in
response to two change requests — (1) "route ≠ testee," the `pcrec-auto`
per-pattern engine split; (2) the 14 flat `pcrec-vm`/`-O0` patterns'
mechanism, verified rather than guessed. Every other finding and every
number elsewhere in this report, the ledger, and the outbox draft was
re-checked against the split/mechanism and found UNCHANGED (no verdict,
ratio, or population count in §1's items 1, 5-7 moved) except where
explicitly updated: "DFA route"/"VM route" is relabeled "`pcrec-auto`"/
"`pcrec-vm`" (or "DFA/VM-hybrid/VM-pure-stamped" for a pattern-level
subset) everywhere in the ledger, this report, `reports/CLAUDE.md`'s
entry, and the outbox draft.

## 2. Deliverables

| item | file |
|---|---|
| report group (4 files; `.matrix.html` not generated, per [B114]'s retirement) | `reports/2026-10-01-capability-0.1-budu-ryzen1600-olevel-fc719ca4.{tsv,md,matrix.tsv,subject-grain.tsv}` |
| `.interpretation.md` sidecar | `reports/2026-10-01-capability-0.1-budu-ryzen1600-olevel-fc719ca4.interpretation.md`, via the `/pcrec-bench-interpret` skill's exact procedure, determinism-checked (a second `--render` to stdout diffs byte-identical) |
| predictions fix | `docs/dev/predictions/capability-0.1-b117-olevel-fc719ca4.tsv` — P4/P6's `lo`/`hi` column swap corrected (load-time defect, fixed before any score; documented in `docs/dev/predictions/CLAUDE.md`'s existing precedent, not amended there — a hygiene fix on an unscored file, not a revision) |
| ledger | `docs/dev/ledgers/2026-10-01-b117-olevel-fc719ca4.md` — per-prediction verdicts with the measured number/spread/n, the full distribution tables (median/Q1/Q3/extremes) by testee × regime × level (§2), compile-side tables (§3), populations read/not-read (§4), findings outside the predictions (§5), `pcrec-auto`'s per-pattern engine-category split + its own distribution tables (§6), and the 14 flat `pcrec-vm`/`-O0` patterns' measured mechanism (§7) |
| `docs/dev/ledgers/CLAUDE.md` row | appended |
| `reports/CLAUDE.md` entry | new paragraph after the `[B110]` placement-twin entry |
| outbox draft | `docs/dev/lanes/b117read_outbox_draft.md` (O-79, findings only, no ask beyond what the data supports) — NOT written to `docs/dev/outbox_to_pcrec.md` |
| this report | `docs/dev/lanes/b117read_report.md` |

## 3. How the numbers were produced

- The report group was rendered via the CLI directly (`pcrecbench report`,
  ten `--testee` values, no `--since`/`--until` needed — no other pcrec
  testee exists at this pin yet). The first foreground attempt (a 240 s
  `gnutimeout`) was cut off mid-`.md` render; the partial `.tsv`/`.md`
  were deleted and the render was repeated DETACHED per BOILERPLATE's
  rule (`setsid gnutimeout 1800 … & disown`, a durable `DONE`/`ALL-DONE`
  marker in the log), polled with two bounded foreground `until`-loops
  (540 s each) rather than left to a background notification (the job was
  disowned — no harness notification was ever coming). Total wall time
  for all four renders: ~10 minutes (`.subject-grain.tsv`'s
  `--grain subject --subject-grain-slice` render was the slow one).
- The sidecar was generated per `.claude/skills/pcrec-bench-interpret/
  SKILL.md` exactly, with the matching predictions file named explicitly
  (more than one `capability-0.1-*.tsv` predictions file exists, so the
  skill's "at most one is expected" default does not apply here — the
  correct one, `capability-0.1-b117-olevel-fc719ca4.tsv`, was passed by
  name) and `--subject-grain` supplied (the slice exists). Determinism
  check: a second `interpret --render` to stdout diffs byte-identical
  against the committed file (`diff` clean).
- Every ratio/table in the ledger was computed directly from the
  committed report `.tsv` by two standalone scripts in the session
  scratchpad (never `scripts/`): one computing the full timing-ratio
  distribution (median/Q1/Q3/min/max with pattern names) per
  (regime, engine, level) over every compiling, ranked `plain`-form
  pattern, and compile-side `.so`-byte / phase-2-wall ratios the same
  way; a second specifically reproducing each prediction's own
  `between`/`gt`/`lte` test over the full population to find every
  violator in both directions and compare against the sidecar's own
  named "worst" witness (which is where the "worst" quirk, finding 4
  above, was found and then traced to `interpret.py:2790`'s exact
  `max(bad, key=lambda lv: abs(lv[1]))` line). The engine-category split
  (finding 2) was read directly from each record's own `compile`-kind
  rows' `engine_metadata.engine`/`.prefilter` fields (never from the
  report TSV's `compile_stamp` legend rows, which print only ONE
  representative value per testee when a testee's own cells agree on a
  fact across the query — not the case here, since `pcrec-auto` routes
  per pattern; the legend's single "engine: vm" line for `pcrec-auto`
  would have been a MISLEADING read on its own, the exact trap the team
  lead's review caught). The necessary-byte mechanism (finding 3) needed
  the throughput subject BYTES, regenerated locally
  (`bench/capability/gen_throughput_subjects.py`, deterministic,
  sha256-verified against the committed `manifest_throughput.tsv` — a
  gitignored input re-derivation, not a new measurement) and counted
  directly against each pattern's `req_byte` value.
- Record provenance: `store/index.tsv`'s own ten `fc719ca4` rows (nine
  `measured` plus the one superseded `inconclusive-spread`), cross-checked
  against the report header's own `records: 10; superseded: 1` count and
  each record's own `agreement: agree (...)` line (read directly from the
  TSV's `record` rows), confirming no v1.4 spread flag anywhere in this
  population.

## 4. Validation

- `python3 catalogue/check_interpret.py`: **234 passed, 0 FAILED**
  (includes this lane's new committed sidecar's own freshness check,
  section 3; section 1's closed-set/column checks pass on the corrected
  predictions file).
- `make check-harness` / the full `make check` were NOT run — this lane
  touched no reporter, harness or interpreter code, only report outputs,
  one predictions-file hygiene fix, a ledger, docs and an outbox draft.
- No `store/` write, no new measurement, no timing of any kind.

## 5. Charter-vs-committed checklist (session_discipline.md §7(c))

| brief item | status |
|---|---|
| (1) the report group, filtered to the 10 testees, set grain, plus whatever grain/form the predictions need, named per `reports/CLAUDE.md` | COMMITTED — `reports/2026-10-01-capability-0.1-budu-ryzen1600-olevel-fc719ca4.{tsv,md,matrix.tsv,subject-grain.tsv}`; the vm-o1 inconclusive-spread record's exclusion explained (§header above, §3) |
| (2) its `.interpretation.md` sidecar via `pcrecbench interpret`, scored against the fc719ca4 predictions file | COMMITTED — determinism-checked, scored through the normal CLI path (no F27 bypass needed: a never-before-measured testee population) |
| (3) ledger `docs/dev/ledgers/2026-10-01-b117-olevel-fc719ca4.md`: per prediction verdicts + measured number/spread/n; per route/regime distribution (median/quartiles/extremes with pattern names); compile-side tables; anything outside predictions; what was read and not read, every number with its environment pointer | COMMITTED — §1-§5 of the ledger cover each named element; record ids are in the ledger's header, not repeated per-number (the report TSV itself is the per-number pointer, as every other ledger in this directory does) |
| (6) team lead's review item 1: split `pcrec-auto` by per-pattern engine stamp, recompute `-O`-level ratio distributions per engine, say whether the "DFA route is not flat" claim holds on the DFA-stamped subset alone, relabel "DFA route" as "the auto testee" everywhere | COMMITTED — ledger §6 (29 DFA / 22 VM-hybrid / 11 VM-pure, identical across all five `-O` levels; P1/P3's claim CONFIRMED on the DFA-stamped subset alone, P2's holds even more tightly there); relabeled in the ledger, this report, `reports/CLAUDE.md`'s entry and the outbox draft |
| (7) team lead's review item 2: for the 14 flat `pcrec-vm`/`-O0` patterns, show `.so` bytes O0-vs-O2, `RX_REQ_WHY`, the VM prefilter/scan stamp, and whether subjects mostly fail; a measured mechanism or NOT-DETERMINED, never a guess | COMMITTED — ledger §7: `.so` bytes genuinely differ (+240 B to +8,512 B) for all 14; `req_why`/`prefilter` are identical (`emitted`/`none`) across the 14 AND the biggest mover, so those stamps alone do NOT explain the split; the actual mechanism is `req_byte`'s own occurrence count in the throughput subjects — 0 for all 14, >0 for every other pattern with a `req_byte`, a 100% clean split, confirmed by direct byte-count, not asserted |
| (4) a DRAFT outbox item O-79 for pcrec, findings only, no invented asks | COMMITTED — `docs/dev/lanes/b117read_outbox_draft.md`; `docs/dev/outbox_to_pcrec.md`/plan.md/the journal deliberately NOT touched (the manager's own act) |
| (5) `docs/dev/lanes/b117read_report.md` with the charter-vs-committed checklist | THIS FILE |

Also done, not explicitly named in the brief but the project's standing
convention for a new report group: `reports/CLAUDE.md`'s own paragraph
describing the group (committed), `docs/dev/ledgers/CLAUDE.md`'s table
row (committed).

Nothing is OWED by this lane — every deliverable named in the brief is
committed above with its file path.
