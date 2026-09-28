# lane b108read report — THE READ of [B108]'s window at pcrec a32bc86e (abi 41)

**Branch**: `lane/b108read`, worktree `worktrees/b108read`, from master
bcd93fa. This is a writer lane: no measurement, no engine build, and
`~/pcrec` only read (`git -C ~/pcrec show a32bc86e:…`). The render,
extraction and re-score scripts live in the session scratchpad, never in
`scripts/`.

## 1. Findings first

1. **Answers: 0 wrong on all 17 records.** The one excluded cell is
   capability `evil-alt-nested`/short-search: a `PCREC_ERR_STEPS`×2
   give-up, identical on both twin arms.
2. **I-113 item 3 (DFA NULL) is CONFIRMED on program and time.**
   - 153/153 DFA artifact pairs (auto vs auto-nolitrun, four sets) are
     `program_sha256`-identical.
   - The twin null band on identical cells is p5-p95 0.991-1.011.
   - All three P3 clauses hold: 1.045, 1.000, 1.000.
   - Cross-pin, abi 40 moved no normalized program: 20/22, 114/126 and
     99/123 cells null, 0 disagreements.
3. **I-113 item 1 (the named FASTER population) is NOT faster on x86.**
   Ratios are auto ÷ auto-nolitrun.
   - bounded `ctx-*` throughput reads 0.9996-1.0010. The no-context-word
     worst case (l-03/l-04) reads 0.999-1.005.
   - **ctx-lazy-256/1024 whole-subject match is ×1.034 / ×1.042 SLOWER**,
     a uniform +0.3-0.6 ns per ~10 ns call on every subject.
   - loglines `level-context` reads 0.998 / 1.002, inside the band.
   - **capability `aws-access-key-id` throughput is ×1.037 SLOWER**, on all
     three subjects, with non-overlapping spreads.
   - The cross-pin AFTERs agree in sign and size (aws +3.64%, ctx-lazy-1024
     match +3.3%), inside their wider 7-17% bands.
4. **A window-plan gap: capability's `ext bench` roster omits
   `pcrec-auto-nolitrun`.**
   - Fail-closed, 27 of 64 patterns are `unsupported-by-declaration` on
     the deny arm (14,429 vs 24,807 rows).
   - So **7 of I-113 item 2's 8 FLAT cells cannot be read same-window.**
   - The one that can, `logparse-atomic-removed`, is **×1.107 slower** on
     throughput and ×1.082 on search: +0.7 ns on every short call.
   - The cross-pin 02902356→a32bc86e reads the other seven: all inside
     that pair's band, with `logparse-atomic` at +6.7% / +3.4%.
   - Fix: a roster line in `bench/capability/patterns.rxt` (+
     `gen_patterns.py`) and one re-measured cell. OWED to the manager; not
     done here.
5. **§7.1: lit-run does NOT flip the sign of factoring on
   `wild-secrets-aws-access-key-id`, on either route.**
   - All 16 stamp cells match pcrec's table exactly.
   - VM route, `fac ÷ nofac` with lit-run on vs off: throughput 0.742 vs
     0.753, search 0.800 vs 0.759, match 0.354 vs 0.349.
   - The smaller unfactored program is the SLOW one, by ×1.25-×2.9.
   - Auto (hybrid): throughput and search are null; match is 0.355 vs
     0.343.
   - `foo.x|foobar|foo.`: both of §7.1's directional sentences are
     refuted by 1-3 points on the VM. The cell is DFA under auto.
   - Controls: factoring is null by program sha and by time.
6. **§7.2, the L-sweep in cycles per byte.** The PRIMARY row has the
   pre-checks denied.
   - **Match** gets faster with L: 0.929 → 0.253.
   - **First-byte flip moves in ONE-CYCLE PLATEAUS**: 2/3/4 cycles per
     position with lit-run, against 3.01 flat without it up to L=16, then
     6.02/6.52 at L=31/40. That is why L=10 reads ×1.333 and L=3/7 read
     ×0.667.
   - **No L=2 first-byte constant**: ×1.007.
   - The one per-call constant is the L-1 subject at L=2 on short-search:
     **+1.54 ns/call**.
   - **L-1 is not null for the chain**: 6.5 → 19.8 ns, while lit-run stays
     flat at ~6.2 ns.
7. **L=31 on x86: no cliff, as restated before the window.**
   - PRIMARY at L=31: mat 0.284, lbf 0.567, fbf 0.523. These sit between
     L=16 and L=40.
   - The x86 memcmp column for pcrec's `memcmp_lowering_study.md`: gcc-15
     at -O2/-O3 inlines at every L = 1..64; at -O1/-Os it calls memcmp
     out of line at every L ≥ 2. On x86 the cliff is a flag property,
     not an L property.
8. **Unasked:**
   - The pre-check costs ×2.0-×9.35 on dense-matching tiles (`vm` vs
     `vm_noreqbyte-noreqrun`, `mat-l<L>`). At L=40 that is 49.8 vs 5.3 ns
     per match.
   - The acceptance mover `wild-datetime-datefinder-alternation` is
     confirmed on the AUTO route's whole-subject form: 482,896 code B
     compiles, while the denied arm is refused at 666,790.
9. **A predictions-file defect.** `litrun-0.1-first.tsv`'s P5 selectors
   name `subject_or_na` without `grain=subject`.
   - The committed sidecar honestly reads P5 "not evaluable" on all 37
     clauses.
   - A scratch re-score (grain key added, `check_utc=False`, never
     committed) reads **32 confirmed / 5 refuted**. It agrees clause for
     clause with direct `pcrecbench.reduce` extraction.
   - Four of the five refutations are favourable: lit-run is faster than
     the band allowed.
   - The committed predictions file is not edited after the window.

## 2. Deliverables

| item | file |
|---|---|
| 7 report groups | `reports/2026-09-28-litrun-0.1-budu-ryzen1600-first-a32bc86e.*`, `reports/2026-09-28-{loglines-0.1,capability-0.1,bounded-0.3}-budu-ryzen1600-{litrun,after}-a32bc86e.*` (`.tsv`/`.md`/`.matrix.tsv`/`.matrix.html`/`.subject-grain.tsv`) |
| 7 sidecars | `….interpretation.md`, each determinism-checked (a second render, byte-compared). The four `first`/`litrun` sidecars carry their predictions STAMPED (`check_utc=True` passed); the three `after` sidecars carry none |
| identity | field-first on all three cross-pin pairs (every pin postdates [B88]), so no census file was needed. Twin identity was read from `program_sha256` directly |
| ledger | `docs/dev/ledgers/2026-09-28-b108-a32bc86e.md` (+ its row in `docs/dev/ledgers/CLAUDE.md`) |
| outbox draft (O-64) | `docs/dev/lanes/b108read_outbox_draft.md`. NOT written to `outbox_to_pcrec.md` |
| `reports/CLAUDE.md` | the new `[B108] reading` paragraph |

## 3. Validation

- `make check-interpret` (worktree, `gnutimeout 900`): **231 passed, 0
  FAILED**. That is 224 + the seven new sidecars.
- The render run was detached with a `DONE rc=0` marker, 03:42 → 03:52
  EDT, with no `FAIL` line.
- The set-grain numbers in the ledger were recomputed from the 17 JSONL
  records with `pcrecbench.reduce`, and they agree with the committed TSVs.
- No `store/` file was modified, and no `~/pcrec` write.
- Not run: `make check-report` / the full `make check`. This lane touched
  no reporter, harness or interpreter code.

## 4. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 0 | read BOILERPLATE.md, follow it | DONE: worktree, gnutimeout, detached render with a marker, kill-by-PID (one relaunch to fix a filename slug) | — |
| 1a | report groups for the four sets at a32bc86e | DONE: 7 groups | §2 |
| 1b | sidecars via the skill | DONE: 7, determinism-checked, with predictions stamped where applicable | §2 |
| 1c | cross-pin AFTER vs 751b9c6d where needed | DONE for loglines/bounded (751b9c6d) and capability (02902356, its last pin). No prediction needed them; they serve as an independent second reading | ledger §0.2, §3.4 |
| 1d | program-identity censuses where the D119 band needs one | NOT NEEDED: field-first identity on all pairs, 0 census fallback | ledger §0.2 |
| 2 | ledger scoring EVERY clause of the four predictions files, with number, spread and not-read | DONE: P1-P3 × 3 sets, P4/P5/P6. P5 was scored via the re-score, and the defect is stated | ledger §3 |
| 2a | the named FASTER population | DONE | ledger §4.1 |
| 2b | the WATCH 2-byte regression | DONE | ledger §4.2 |
| 2c | DFA cells NULL + program identity | DONE | ledger §2.3, §4.3 |
| 2d | the §7.1 2×2 sign question, both routes | DONE | ledger §4.4 |
| 2e | the §7.2 L-sweep per subject kind, both pairs, the L=2/3 constant, L=31 on x86 | DONE | ledger §4.5 |
| 2f | every arm's configuration stated | DONE | ledger, "THE ARMS" |
| 3 | outbox draft (next O-number, O-64), incl. the x86 memcmp column | DONE | `docs/dev/lanes/b108read_outbox_draft.md` item 7 |
| 4 | reports/CLAUDE.md + ledgers/CLAUDE.md rows; `make check-interpret` green | DONE (231/0) | §3 |
| 5 | this report, findings first | DONE | — |

## 5. OWED, to the manager (none from this lane's brief)

- **capability × `pcrec-auto-nolitrun` re-measure.** Add `capabilities
  pcrec-auto-nolitrun` to `bench/capability/patterns.rxt`'s `ext bench`
  block, mirroring `pcrec-auto`'s tokens, and to `gen_patterns.py`. Then
  re-run the one cell (~35 min, a window), so the seven P2 cells get a
  same-window reading. Trigger: the manager's next window.
- **Optional**: amend `litrun-0.1-first.tsv`'s P5 selectors with
  `grain=subject` for the NEXT litrun sample only, as a new file or a
  dated amendment, never a post-hoc edit of this one.
