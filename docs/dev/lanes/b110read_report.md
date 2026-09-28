# lane b110read report — I-115 Q2's placement twin, read

**Branch**: `lane/b110read`, worktree `worktrees/b110read`, from master
`3b3b0b4` (which already carries `[B110]`'s window commit — this lane is
a READ lane over that one new pair of records, not a measurement lane).
`~/pcrec` was not touched.

## 1. Findings first

1. **The twin's own precondition holds: `program_sha256` is IDENTICAL,
   aligned vs unaligned, on every checked cell.** Both I-115 Q2 witness
   patterns (`wild-secrets-aws-access-key-id`, `logparse-atomic-removed`),
   both forms (4/4), plus every one of 73/72 shared DFA-null
   (program-identical between `auto` and `auto-nolitrun`) compile keys
   still available on the aligned pair, 0 diffs either arm. pcrec's own
   emitted C source is provably unmoved by our phase-2 `cflags`; the
   `.so` binaries themselves genuinely differ (distinct file sha256 on
   both witnesses; `objdump -d` shows `rx_search_run`/`rx_match_anchored`
   and every function after them shift 0x30-0x80 bytes between the
   unaligned and aligned build of the SAME arm). Placement, not code —
   the twin measures what Q2 asks.
2. **Neither headline miss survives intact; both shrink substantially
   toward null.** aws throughput 1.0361 → 1.0144 (~60% of the 3.61%
   excess gone); logparse-atomic-removed throughput 1.1174 → 1.0286
   (~83% gone, now arguably inside this window's own ±3.9% DFA-null
   noise band) and search 1.0833 → 1.0341 (~59% gone, stays outside the
   ±2.4% band). aws search flips sign (0.9813 → 1.0089) but both
   readings are inside the search noise band either way. Read plainly:
   placement/alignment accounts for MOST but not clearly ALL of either
   miss — a partial-placement finding, not a clean either/or.
3. **An UNPLANNED finding: the O-64/O-65 roster-declaration gap recurs,
   unfixed, on the two new testees.** `bench/capability/patterns.rxt`'s
   `ext bench` roster declares no capability tokens for
   `pcrec-auto-align64loops`/`pcrec-auto-nolitrun-align64loops` — the
   same gap class O-64/O-65 found and fixed for `pcrec-auto-nolitrun`
   itself (`fef55af`), not ported when [B110] added these two testees.
   27/64 patterns refuse `unsupported-by-declaration` identically on
   both aligned arms, including `logparse-atomic` (I-115 Q3's own
   pattern — unreadable on this twin at all) and three of O-65's own P2
   FLAT cells (`tag-pair-match`, `nested-comment-rec`,
   `email-local-nodup`). Neither headline witness nor the
   `router-prefix-order` DFA-null control is affected. Not fixed here
   (a read lane); a fix + re-measure is OWED, same shape as O-64→O-65.
4. **The aligned/unaligned-per-arm table is stated with an explicit
   cross-window caveat** (§5 of the ledger): the two windows are ~2 h
   apart under different box load (worst-other-core-busy 25.0% vs
   38.1%), and the DFA-null control itself reads 1-2.5% off unity in
   BOTH directions across the pair, so per-pattern cells in that table
   are not reliably separable from cross-window noise at this grain —
   stated, not claimed as a directional finding.

## 2. Deliverables

| item | file |
|---|---|
| report group (6 files) | `reports/2026-09-28-capability-0.1-budu-ryzen1600-align64loops-a32bc86e.{tsv,md,matrix.tsv,matrix.html,subject-grain.tsv,interpretation.md}` |
| ledger | `docs/dev/ledgers/2026-09-28-capability-0.1-i115q2-align64loops-a32bc86e.md` (NEW file — the b108 ledger's own O-65 addendum is already sent, never edited again per its CLAUDE.md) |
| ledger CLAUDE.md row | `docs/dev/ledgers/CLAUDE.md`, appended |
| O-67 outbox draft | `docs/dev/lanes/b110read_outbox_draft.md` — NOT written to `docs/dev/outbox_to_pcrec.md` |
| `reports/CLAUDE.md` row | new paragraph after the `[B108]` cap re-measure entry |
| measurement archive | `docs/dev/measurements/probe_b110_align64loops_placement.py` + `2026-09-28-b110-align64loops-placement.txt` (program_sha256 identity, the roster-gap census, `objdump` placement facts, source header) |
| this report | `docs/dev/lanes/b110read_report.md` |

## 3. How the numbers were produced

- The report group was rendered with the CLI directly (2 records — no
  KB-16 whole-store load hazard, but detached anyway per BOILERPLATE's
  "a run that loads the store... goes DETACHED" rule since the store
  has grown to 292 records): `setsid gnutimeout 1800 bash
  render_align64loops.sh` from the scratchpad, `.tsv`/`.md` ~16 s each,
  the rest similar; log ended `ALL-DONE rc=0`, polled with a bounded
  foreground `until`-loop.
- The sidecar was generated per `.claude/skills/pcrec-bench-interpret/SKILL.md`
  exactly: `pcrecbench interpret … --render --out …`, then the same
  command without `--out` to stdout, byte-diffed against the file —
  `DETERMINISM-OK`.
- Every ratio in the ledger and the outbox draft was extracted directly
  from the report TSV's `rank`/`ratio_vs_baseline` rows (a standalone
  script in the scratchpad, not `scripts/`) and cross-checked against
  the store records' own `engine_metadata.program_sha256` for program
  identity. The predictions file could not score anything here (its
  selectors name the unaligned testee ids), so this direct extraction
  is the only route to the numbers — stated as such in both the ledger
  and the report's own `reports/CLAUDE.md` entry.
- `program_sha256`, the roster-gap census and the `objdump` placement
  facts came from `docs/dev/measurements/probe_b110_align64loops_placement.py`,
  reading the four store records plus the `build/work/pcrec-auto{,-align64loops}/`
  directories the two windows left on disk (mtimes confirmed to match
  each window's own timestamps before trusting them).

## 4. Validation

- `make check-interpret` (worktree, detached under `setsid gnutimeout
  900`, polled with a bounded foreground fallback loop, never a bare
  wait): **233 passed, 0 FAILED** (was 232 before this lane per
  `docs/dev/lanes/b108cap_report.md`; +1 is this report group's new
  sidecar-freshness check in section 3).
- `make check-report` / the full `make check` were NOT run — this lane
  touched no reporter, harness or interpreter code, only report
  outputs, a ledger, a measurement archive and docs.
- No `store/` file was written by this lane — the two `[B110]` records
  were already committed on master before this worktree was created;
  the render was read-only over the store.
- Nothing under `~/pcrec` was touched.

## 5. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 0 | read BOILERPLATE.md, follow it | DONE — worktree already existed from a prior attempt (verified `git rev-parse --show-toplevel`, clean tree, on `lane/b110read` at master `3b3b0b4`); `gnutimeout`/detached-with-marker/bounded-poll used for the render and `check-interpret` | — |
| 1 | render the align64loops report group + sidecar via the skill, store-loading render detached with a polled marker | DONE | §2, §3 |
| 2 | the four-way table on every capability pattern × regime (unaligned auto÷nolitrun, aligned auto÷nolitrun, aligned÷unaligned per arm), headline cells (aws thr/srch, lp-removed thr/srch, lp-atomic, DFA null controls as the noise band); state spreads; state the cross-window caveat; verify program_sha256 identity + `.so` difference | DONE | ledger §1-§5; `lp-atomic` is NOT a four-way cell — it is unreadable on the aligned twin at all (finding 3 above), stated explicitly rather than silently omitted |
| 3 | draft O-67 at `docs/dev/lanes/b110read_outbox_draft.md`, facts not diagnoses, what was NOT measured | DONE | file above |
| 4 | a measurement archive under `docs/dev/measurements/` for the objdump/placement facts, source header | DONE | `probe_b110_align64loops_placement.py` + the `.txt` |
| 5 | `reports/CLAUDE.md` row; `make check-interpret` green | DONE, 233/0 | `reports/CLAUDE.md`; §4 |
| 6 | this report, findings first, charter-vs-committed checklist | DONE | — |

## 6. OWED

- The roster-declaration gap on `pcrec-auto-align64loops`/
  `pcrec-auto-nolitrun-align64loops` is NOT fixed here (a read lane's
  brief does not include a fix+re-measure cycle). A future lane should
  mirror O-64→O-65's own fix (`bench/capability/patterns.rxt`'s roster
  line + `gen_patterns.py`) and re-measure the cell if a full aligned
  four-way reading (including `logparse-atomic` and the three affected
  P2 cells) is wanted.
- The manager still owns writing O-67 to `docs/dev/outbox_to_pcrec.md`
  (this lane only drafted it, per BOILERPLATE's "the manager merges").
