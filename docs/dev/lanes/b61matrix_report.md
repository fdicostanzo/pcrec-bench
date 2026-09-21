# lane b61matrix report — full-roster matrix reports with rust

**Task**: Frank's direct request (relayed by the manager): produce, for
each of `email-specimen@0.2`, `loglines@0.1`, `bounded@0.3`,
`altwide@0.2`, `syntax@0.1`, a full-roster report group whose matrix
includes every roster engine with records for that set, with
`rust_1.13.1_default-caps-simdna` ([B59]) among them for the first time
— every existing committed matrix for these five sets either predates
`rust-default` entirely or is scoped to `rust-default` alone (the
[B57]/[B59] solo-roster shape). `capability@0.1` is out of charter (the
manager's own read, pending an in-flight merge). Worktree
`worktrees/b61matrix`, branch `lane/b61matrix`. Does not merge.

## Roster-selection rule (stated once, applied mechanically five times)

"Full roster" = the newest record of each CANONICAL engine identity —
`libpcre2-interp`, `libpcre2-jit`, `pcrec-auto`, `pcrec-auto-nocaps`,
`pcrec-vm`, `pcrec-vm-in`, `rust-default` — never every distinct
`testee_id` the store has ever recorded. Ablation testees (`-noedge`,
`-noisland`, `-noclsfold`, `-cc-clang`, `-bigcap`, `-align64`) are
excluded, matching every prior `-after-<pin>` cross-pin group already
committed in `reports/`. Derived mechanically from `store/index.tsv`:
for each of the six canonical `testee_id` suffixes, take the newest
record ACROSS ALL PCREC PINS; add `rust_1.13.1_default-caps-simdna`'s
own newest record. Full derivation and per-testee newest-record table:
`reports/CLAUDE.md`'s new `[B61]` entry (inserted before the `[B39]`
section, immediately after `[B59]`'s).

**The one finding common to all five groups**: pcrec's canonical roster
has not been re-measured on any of these sets since pin **d34c9131**
(abi 23, 2026-09-06/07) — four re-pins behind today's checkpoint
(`cd371441` → `a770139e` → `cf0962e3` → `25b1984f`, abi 27). Every
filename below is suffixed `d34c9131` because that is what the newest
pcrec data on each set actually is. Three of five groups mix pcrec pins
WITHIN their own roster (not every canonical mode was re-measured at
every pin); only `syntax@0.1` is pin-uniform (its own single census
window).

## Per-set table

| set | roster (7 testees) | pcrec pins in roster | records in query | render wall (md→matrix.html) | interpret wall |
|---|---|---|---|---|---|
| email-specimen@0.2 | interp, jit, auto(d34c9131), auto-nocaps/vm/vm-in(1989c62), rust | d34c9131 + 1989c62 | 7 (0 superseded in-query; 7 retired-history records superseded) | ~1m27s | ~18s (2 runs) |
| loglines@0.1 | interp, jit, auto(d34c9131), auto-nocaps/vm/vm-in(1989c62), rust | d34c9131 + 1989c62 | 7 (6 retired-history superseded) | ~2m58s | fast |
| bounded@0.3 | interp, jit, auto/vm/vm-in(d34c9131), auto-nocaps(288d505), rust | d34c9131 + 288d505 | 7 (2 retired-history superseded) | ~7m06s | ~26s |
| altwide@0.2 | interp, jit, auto/vm(d34c9131), auto-nocaps/vm-in(334fd10e), rust | d34c9131 + 334fd10e | 7 (0 superseded) | ~2m56s | ~1m01s |
| syntax@0.1 | interp, jit, auto/auto-nocaps/vm/vm-in(d34c9131, all one census window), rust | d34c9131 only | 7 (0 superseded) | ~10m13s | ~23s |

Render wall times are elapsed between the first (`--format md`) and last
(`matrix.html` via `scripts/matrix_page.py`) file's mtime per set,
foreground, one render at a time (KB-16 is closed — an explicit `--testee`
roster query loads only the matching records via the index prefilter, so
no render here approached the old whole-store cost; the longest single
step was `syntax@0.1`'s `--grain subject --format md`, 3 m 21 s, the
set's own biggest records at 35,859-41,800 rows each). One Bash-tool
timeout hiccup on the first loglines render chain (five chained commands
exceeded the tool's own foreground window and auto-backgrounded as a
tracked task; polled to completion rather than left unattended, matching
BOILERPLATE's foreground-fallback rule) — all renders after that one were
issued as single per-format commands with an explicit generous `timeout`
to avoid repeating it.

Every `.interpretation.md` sidecar is NEW (no `docs/dev/predictions/*.tsv`
applies — these are roster snapshots, not first samples), rendered via
`pcrecbench interpret <tsv> --subject-grain <tsv> --render --out <path>`,
and determinism-checked: a second, independent `interpret --render`
invocation to stdout `cmp`s byte-identical against all five committed
sidecars. `make check-interpret`: **166/166** (section 3, sidecar
freshness, covers all five new files; unchanged section/check counts
otherwise).

## Findings a reader should see before the numbers (full detail in
`reports/CLAUDE.md`'s `[B61]` entry)

1. `rust-default` is `best_testee` (fastest of the seven) on five of ten
   `loglines@0.1` patterns (`hex32-id`, `ipv6`, `kv-quoted`,
   `level-context` on both regimes, `stack-frame` on search) — it beats
   `pcre2-jit` and every pcrec arm outright, not merely competes.
2. `altwide@0.2`: on `ci-256`'s whole-subject match-compliance row,
   `rust-default` is fastest (1,066.2 ns) against pcrec's forced-VM arm
   at ×103.3 slower, with BOTH pcrec AUTO roster arms refusing that exact
   (pattern, form) cell outright. Separately, `wb-512` (512 branches each
   individually `\b`-wrapped) refuses on all four pcrec roster arms on
   every regime/form while pcre2 compiles but runs 40-318× slower than
   `rust-default`; `wb-256` also refuses on all four pcrec arms, a
   smaller branch count than the plain `w`-family's own known DFA/VM
   refusal wall. None of this is diagnosed here (no source was traced);
   stated as matrix-surfaced observations only.
3. `syntax@0.1`'s matrix surfaces six `rust-default` wrong-answer
   patterns beyond the two ([B59]'s P4/P6.a: `qnt-poss-brace`,
   `unp-p-lc`) already named by the prior solo-roster report:
   `anc-dollar`, `cls-v`, `esc-hex-braced`, `qnt-poss-plus`,
   `qnt-poss-quest`, `rec-r-uc` — visible now because this roster ranks
   `rust-default` against pcre2/pcrec on all 95 patterns, not the seven
   witnesses the predictions file selected. Not diagnosed here.
4. `bounded@0.3`/`cls-upto-65535` (pcrec NFA-cap, O-9's history) and
   `bounded@0.3`/`nest2-64`+`nest3-16` (rust's own `CompiledTooBig`,
   [B59]'s own finding) both reproduce on the matrix surface — confirmed
   consistent with prior narrower reports, not new discoveries.

## Charter vs. committed

- [x] Five full-roster report groups, one per named set, `rust-default`
  in every roster: **COMMITTED** (35 files: 5 × `.md`/`.tsv`/
  `.subject-grain.md`/`.subject-grain.tsv`/`.matrix.tsv`/`.matrix.html`/
  `.interpretation.md`).
- [x] `capability@0.1` excluded per charter: not touched.
- [x] Roster and pin-per-testee stated in `reports/CLAUDE.md`, inline,
  before the numbers (context-around-numbers rule): done in the `[B61]`
  entry and in each group's own bullet.
- [x] `fullroster` naming slug, `<date>-<subbench>-<version>-<machine>-
  fullroster-<pin>` per the committed convention (matches the
  `-after-<pin>` / `-first-<pin>` precedent's own shape): done; pin
  suffix is `d34c9131` on all five (the newest pcrec pin actually present
  in each roster, not today's checkpoint — see the finding above).
- [x] Renders foreground, one at a time, `gnutimeout`-bounded: done (see
  per-set table; the one auto-background incident was polled to
  completion in the foreground, never left unattended).
- [x] Interpretation sidecars, `--render --out`, determinism re-run
  diffed byte-identical: done, all five.
- [x] `make check-interpret` run after: **166/166**.
- [ ] `make check-report` was STARTED and KILLED mid-run in this lane,
  not completed: `pcrecbench.tests.test_report` ran 10+ minutes and grew
  to ~3.2 GB RSS (killed by PID with cwd verified, box quiet at the time,
  `/proc/loadavg` 0.85/12 cores — not contention from another lane) before
  finishing, which does not match `Makefile`'s own description of this
  suite as fixture-only and fast. `pcrecbench/tests/test_report.py:56`
  defines a `REAL_STORE = os.path.join(report.REPO_ROOT, "store")`
  constant used by at least one test, so this is plausibly an intentional
  real-store-validating check (in the KB-16 spirit — "before/after on ONE
  committed query" against the live store) that has simply grown slower
  as the store has grown (187 records / ~800 MB today), not a regression
  this lane caused; NOT independently confirmed, and NOT re-run to
  completion — judged out of scope for a report-addition lane that
  touches no reporter/interpreter source. OWED to the manager: either
  let it run to completion off-lane (budget 15+ min, several GB RSS) or
  confirm the `REAL_STORE` hypothesis explains the wall time before
  trusting it as green.
- [x] Lane report committed (this file).

## Commits on `lane/b61matrix`

One commit per set (five) plus the `reports/CLAUDE.md` entry and this
report, incremental as each set finished (per BOILERPLATE's "commit age
is your liveness signal" rule).

Handback: five full-roster groups committed and named above; nothing
OWED except the optional `make check-report` gate. The manager merges.
