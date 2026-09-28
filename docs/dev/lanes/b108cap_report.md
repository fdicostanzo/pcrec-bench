# lane b108cap report — the capability twin re-measured with the roster fixed (O-64 (4))

**Branch**: `lane/b108cap`, worktree `worktrees/b108cap`, from master
`b4a131d` (which already carries the roster fix `fef55af` and the
re-measure `b4a131d` itself — this lane is a READ lane over those two
new records, not a measurement lane). `~/pcrec` was not touched.

## 1. Findings first

1. **All eight of I-113 item 2's FLAT cells are now scoreable
   same-window: 7/8 confirmed, 1 refuted.** The roster fix
   (`bench/capability/patterns.rxt` + `gen_patterns.py`, commit
   `fef55af`) and the re-measure (commit `b4a131d`) let
   `pcrec-auto-nolitrun` attempt all 64 capability patterns (was 37; 27
   were `unsupported-by-declaration`). `P2a-d,f-h` confirm (0.928-1.024,
   inside the 0.85-1.05 band); `P2e` (`logparse-atomic-removed`) refutes
   at 1.1174, the SAME verdict the first window already had for this one
   pre-existing scoreable cell.
2. **The first window's 6 already-scoreable cells reproduce almost
   exactly**, except one threshold-straddle: `github-pat` reads 1.001
   (refuted vs `lte 1.0`) in the first window and 0.9997 (confirmed) in
   this one — both are null-band readings ±0.03% apart, and the verdict
   flip is an artifact of the exact-1.0 boundary, not a real behavior
   change.
3. **One real finding: `logparse-atomic`'s cross-pin stand-in reading
   does not hold up against its own true same-window twin.** The first
   window used a weaker cross-pin (02902356→a32bc86e) reading for the 7
   then-unreadable P2 cells and called `logparse-atomic`'s +6.74%
   throughput "the same shape" as its `-removed` sibling's +11.7%. The
   true same-window twin instead reads `logparse-atomic` throughput at
   **−2.9%** (0.9708, confirmed inside the FLAT band) — the opposite
   sign from its sibling. The two patterns DO agree in sign on
   short-subject-search (+3.2% vs +8.3%). Six of the cross-pin's other
   seven stand-in readings (all effectively null) DO agree with this
   window's true numbers. This is the first-window ledger's own §5.4
   caveat ("the cross-pin AFTER's identical-program cells swing up to
   ±17%") landing on the wrong side of null for one real cell, not a
   hypothetical.
4. **The roster fix is clean.** `pcrec-auto-nolitrun` and `pcrec-auto`
   compile-refuse identically now: `negation-scope-lookbehind-var` is
   `unsupported-by-declaration` on both (a pre-existing, shared
   limitation — not a roster gap), and
   `wild-datetime-datefinder-alternation` behaves exactly as the first
   window's item 9 already found (plain form refused on both arms,
   whole-subject VM form compiles under `auto` only, refused under
   `auto-nolitrun`).

## 2. Deliverables

| item | file |
|---|---|
| twin report (6 files) | `reports/2026-09-28-capability-0.1-budu-ryzen1600-litrun2-a32bc86e.*` (`.tsv`/`.md`/`.matrix.tsv`/`.matrix.html`/`.subject-grain.tsv`/`.interpretation.md`), restricted to the new pair by the reporter's own newest-wins dedup on the SAME `--testee`×2 query as the `-litrun` group — no `--since`/`--until` needed |
| sidecar | determinism-checked (`DETERMINISM-OK`, a second `interpret --render` byte-compared against the committed file) |
| ledger addendum | `docs/dev/ledgers/2026-09-28-b108-a32bc86e.md`, new `## ADDENDUM` section, APPENDED — the pre-existing text is untouched |
| outbox addendum draft | `docs/dev/lanes/b108cap_outbox_draft.md`, numbered O-65. NOT written to `docs/dev/outbox_to_pcrec.md` |
| `reports/CLAUDE.md` | new paragraph under the `[B108]` reading entry, cross-referencing this group |

## 3. Validation

- `make check-interpret` (worktree, `gnutimeout 900`, detached with a
  `DONE`-equivalent marker grep, polled with a bounded foreground
  fallback loop): **232 passed, 0 FAILED** (was 231 before this lane;
  +1 is the new report group's sidecar-freshness check in section 3,
  58→59).
- The render (`.tsv`/`.md`/`.matrix.tsv`/`.matrix.html`/
  `.subject-grain.tsv`/`.interpretation.md`) ran detached under
  `setsid gnutimeout 1800`, log
  `/tmp/…/scratchpad/render_litrun2.log`, ending `ALL-DONE rc=0` with a
  `DETERMINISM-OK` line before it — polled with a bounded foreground
  `until`-loop, never a bare wait on the harness notification alone.
- Every ratio in this report and the ledger addendum was cross-checked
  directly against the two JSONL records with
  `pcrecbench.reduce.reduce_set_cell` (a standalone script, scratchpad
  only); it agrees with the sidecar's `R-PRED-1`/`R-PRED-4` verdicts
  clause for clause.
- `make check-report` / the full `make check` were NOT run — this lane
  touched no reporter, harness or interpreter code, only report
  outputs, a ledger and a doc.
- No `store/` file was written by this lane (the two new records
  predate it, written by the commit the manager's brief names). Nothing
  under `~/pcrec` was touched.

## 4. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 0 | read BOILERPLATE.md, follow it | DONE — worktree already existed from a prior attempt (verified `git rev-parse --show-toplevel`, clean tree, on `lane/b108cap`), `gnutimeout`/detached-with-marker/bounded-poll used for both the render and `make check-interpret` | — |
| 1 | render the litrun2 report group + sidecar, restricted to the new pair | DONE | §2 |
| 2 | score every clause of `capability-0.1-litrun-a32bc86e.tsv` against the new pair, all 8 P2 FLAT cells incl. WATCH, P1 cells, state reproduction vs first window (aws, logparse-atomic-removed, username-password-pair, github-pat/slack) | DONE | ledger ADDENDUM; this report §1 items 1-3. The WATCH (item 2's 2-byte-run regression) does not name a capability cell in either window — nothing new to score beyond what the first window already read on `litrun@0.1`'s own instrument |
| 3 | ledger ADDENDUM (append, don't rewrite) + O-65 outbox draft (not written to the real outbox) | DONE | `docs/dev/ledgers/2026-09-28-b108-a32bc86e.md` `## ADDENDUM`; `docs/dev/lanes/b108cap_outbox_draft.md` |
| 4 | `reports/CLAUDE.md` row + `make check-interpret` green (worktree, gnutimeout 900) | DONE, 232/0 | reports/CLAUDE.md; §3 |
| 5 | this report, findings first | DONE | — |

## 5. OWED

None from this lane's brief. The manager still owns writing O-65 to
`docs/dev/outbox_to_pcrec.md` (this lane only drafted it, per its brief
and BOILERPLATE's "the manager merges").
