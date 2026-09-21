# lane b61matrix report — full-roster matrix reports with rust

**Task**: Frank's direct request (relayed by the manager): produce, for
each of `email-specimen@0.2`, `loglines@0.1`, `bounded@0.3`,
`altwide@0.2`, `syntax@0.1`, a full-roster report group whose matrix
includes every roster engine with records for that set, with
`rust_1.13.1_default-caps-simdna` ([B59]) among them for the first time
— every existing committed matrix for these five sets either predates
`rust-default` entirely or is scoped to `rust-default` alone (the
[B57]/[B59] solo-roster shape). `capability@0.1` was initially out of
charter, pending an in-flight merge. Worktree `worktrees/b61matrix`,
branch `lane/b61matrix`. Does not merge.

**CHARTER EXTENSION (manager message, after the five sets landed)**: the
[B60] merge (8dde570) landed four fresh `pcrec_25b1984f_*` records on
`capability@0.1`; add it as a SIXTH set under the same conventions, after
merging `master` into this lane's branch first (not rebasing). Done: see
"The sixth set" section below.

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

## The sixth set: `capability@0.1`

**Merge first**: `git merge master` in this worktree hit ONE conflict, in
`reports/CLAUDE.md` — both `master` (the [B60] pinconfirm entry) and this
lane's own uncommitted `[B61]` entry had been inserted at the identical
point (immediately before the `[B39]` section). Not a semantic conflict:
resolved by keeping BOTH blocks intact, `[B60]`'s entry first (it landed
on master first), this lane's `[B61]` entry second — nothing dropped,
nothing reworded. `git status` showed no other unmerged paths; the merge
commit is `dca2ee1`. Side effect: `store/index.tsv` grew (187 → 191
records, the four new `pcrec_25b1984f_*` capability rows), which made
`make check-interpret`'s section-3 freshness check FAIL on all five
already-committed sidecars (each one's stamped `index_sha256` no longer
matched the live index) — fixed by regenerating all five in place
(one-line diffs, `index_sha256` only, confirmed by hand before
recommitting) before adding the sixth.

Roster derivation for `capability@0.1` differs from the other five sets'
mechanical rule because the set itself carries more than one canonical
identity per engine family (`libpcre2-dfa` beside `-interp`/`-jit`,
`re2-default` beside `re2-longest`) — this lane's rule generalizes to
"newest record of every canonical identity `store/index.tsv` shows for
this set," giving **thirteen** testees, not seven: `libpcre2-{interp,
jit,dfa-nocaps}`, `pcrec_25b1984f_{auto,auto-nocaps,vm,vm-in}-caps-simdna`
(now PIN-UNIFORM — the four [B60] records are the newest sample of every
canonical pcrec mode on this set, the first time that has been true for
`capability@0.1`), `oniguruma-default`, `re2-{default,longest}`,
`rust-default`, `tre-default`, `vectorscan-block-nosom`. Query: `report
--subbench capability --version 0.1` plus the thirteen `--testee` values
— 13 records matching, 13 included, 4 superseded (each id's own retired
history). Render wall (md → matrix.html): ~9m40s (the three
`--grain subject` / matrix steps each took ~3 minutes on this set's
15,000-25,000-row records — still an explicit-roster, index-prefiltered
query, nowhere near KB-16's old whole-store cost). Interpretation sidecar
regenerated the same way as the other five, determinism-checked
byte-identical. `make check-interpret` after all six (five regenerated +
one new): **168/168**.

**Distinguished explicitly, in `reports/CLAUDE.md`'s own text, from
`2026-09-20-capability-0.1-budu-ryzen1600-pinconfirm-25b1984f.md`** (the
[B60] cross-pin acceptance AFTER already committed on master): that
report answers "did anything measuring time move across the re-pin"
(eleven testees, both `cf0962e3` and `25b1984f` pcrec arms side by side);
this one answers "how does every engine compare right now" (thirteen
testees, one pcrec pin). Per the manager's own instruction, the
reports/CLAUDE.md entry states which is which so a reader does not
conflate them.

**Genuine finding, stated not diagnosed**: `evil-alt-nested` /
`short-subject-search` / `plain` has NO winner in the whole matrix — all
thirteen roster testees read `wrong` (7: `libpcre2-dfa`,
`pcrec_25b1984f_auto-nocaps-simdna`, `re2-default`, `re2-longest`,
`rust-default`, `tre-default`, `vectorscan`) or `gave-up` (6: the rest)
on that one cell; `best_testee`/`best_ns` are both empty. The SAME
pattern's `large-subject-throughput` row ranks cleanly. No prior
committed report (all narrower-roster) could show this — it takes all
thirteen testees in one row to see that nobody wins.

## Charter vs. committed

- [x] Six full-roster report groups, one per named set (five originally
  chartered plus `capability@0.1` on extension), `rust-default` in every
  one of the first five, the [B60] `25b1984f` records in the sixth:
  **COMMITTED** (42 files: 6 × `.md`/`.tsv`/`.subject-grain.md`/
  `.subject-grain.tsv`/`.matrix.tsv`/`.matrix.html`/`.interpretation.md`).
- [x] `master` merged into `lane/b61matrix` before rendering the sixth
  set, not rebased, conflict resolved with both sides kept and reported
  (see "The sixth set" above): merge commit `dca2ee1`.
- [x] `capability@0.1` added as the sixth set per the charter extension,
  its own roster-derivation rule and its distinction from the [B60]
  pinconfirm group stated inline in `reports/CLAUDE.md`: done.
- [x] Roster and pin-per-testee stated in `reports/CLAUDE.md`, inline,
  before the numbers (context-around-numbers rule): done in the `[B61]`
  entry and in each group's own bullet.
- [x] `fullroster` naming slug, `<date>-<subbench>-<version>-<machine>-
  fullroster-<pin>` per the committed convention (matches the
  `-after-<pin>` / `-first-<pin>` precedent's own shape): done; pin
  suffix is `d34c9131` on the first five (the newest pcrec pin actually
  present in each roster, not today's checkpoint) and `25b1984f` on the
  sixth (genuinely pin-uniform there).
- [x] Renders foreground, one at a time, `gnutimeout`-bounded: done (see
  per-set table; the one auto-background incident was polled to
  completion in the foreground, never left unattended).
- [x] Interpretation sidecars, `--render --out`, determinism re-run
  diffed byte-identical: done, all six (the first five were regenerated
  once after the merge, since the growing live index moved their stamp —
  see "The sixth set" above; content unaffected, confirmed by hand).
- [x] `make check-interpret` run after: **168/168** (all six sidecars).
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
is your liveness signal" rule); then the `master` merge commit; then the
sixth set (`capability@0.1`) plus the five regenerated sidecars and this
report's update, in one closing commit.

Handback: six full-roster groups committed and named above; nothing OWED
except the optional `make check-report` gate (unchanged from before the
extension — not re-attempted). The manager merges.
