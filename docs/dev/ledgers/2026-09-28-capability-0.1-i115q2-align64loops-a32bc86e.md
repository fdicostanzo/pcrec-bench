# the [B110] I-115 Q2 READ: the placement twin at pcrec a32bc86e (abi 41), auto vs auto-nolitrun at `-falign-functions=64 -falign-loops=64`

Lane b110read. This is a NEW ledger file, not an addendum to
`2026-09-28-b108-a32bc86e.md` — that file's own O-65 addendum has
already been sent (outbox_to_pcrec.md), and `docs/dev/ledgers/CLAUDE.md`
says a ledger is never edited after its outbox item is sent.

**Context.** Inbox I-115 Q2 (docs/dev/inbox_from_pcrec.md) asks whether
O-64's two named-population misses — `wild-secrets-aws-access-key-id`
throughput ×1.037 slower and `logparse-atomic-removed` +0.7-1.4 ns/call
(auto ÷ auto-nolitrun, `-fno-lit-run`, at pin a32bc86e) — survive when
both arms are built at `-O2 -falign-functions=64 -falign-loops=64`. O-66
built the two testees (`pcrec-auto-align64loops`,
`pcrec-auto-nolitrun-align64loops`) and handed back the window command;
[B110] ran it 2026-09-28 06:15-06:58 EDT (`build/windows/
suite_b110_20260928T101534Z.log`), 2/2 measured at attempt 1. Records:
`capability@0.1__pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64__budu-ryzen1600__20260928T101609Z`
and the `_nolitrun-cf-…` sibling at `…T103722Z`. Worst other-core busy
this window: 38.1% (`…align64loops` / `wild-datetime-moment-iso8601` /
large-subject-throughput).

**What was rendered.** `reports/2026-09-28-capability-0.1-budu-ryzen1600-align64loops-a32bc86e.*`
(`.tsv`/`.md`/`.matrix.tsv`/`.matrix.html`/`.subject-grain.tsv`), a plain
`pcrecbench report --testee … --testee …` query on the two new testee
ids, no `--since`/`--until` needed. Sidecar via `/pcrec-bench-interpret`
against `docs/dev/predictions/capability-0.1-litrun-a32bc86e.tsv` (the
same predictions file O-65's twin used, for the same pin/set family) —
**every P1/P2/P3 clause in it reads `not evaluable`, R-PRED-3**, because
every clause's selector names the UNALIGNED testee ids by exact string
and none matches this report's population; this is correct behavior
(the predictions genuinely do not apply to a different testee id), not
a defect, and every number below is instead cross-checked directly
against the report TSV's own `ratio_vs_baseline` column. Determinism
checked (`DETERMINISM-OK`, a second `interpret --render` byte-compared
against the committed file).

## 1. A FINDING BEFORE THE HEADLINE: the O-64/O-65 roster gap recurs, unfixed, on both new testees

O-64/O-65 found and fixed `bench/capability/patterns.rxt`'s `ext bench`
roster omitting `pcrec-auto-nolitrun` (27/64 patterns
`unsupported-by-declaration`, fixed by commit `fef55af`). **The SAME gap
exists on the two testees [B110] added and was NOT ported**: both
`pcrec-auto-align64loops` and `pcrec-auto-nolitrun-align64loops` refuse
the IDENTICAL 27 patterns with `unsupported-by-declaration`
(`docs/dev/measurements/2026-09-28-b110-align64loops-placement.txt`
PART 3) — including `logparse-atomic` (one of I-115 Q3's own answered
patterns), and three of O-65's own P2 FLAT cells
(`tag-pair-match`, `nested-comment-rec`, `email-local-nodup`). Compile
row counts: 393/389 (aligned) vs 627/623 (unaligned) — the same 64
patterns attempted on both, just 27 refused identically on the aligned
pair. **Neither headline witness is affected** (`wild-secrets-aws-
access-key-id`, `logparse-atomic-removed` both compile clean on all
four arms), nor is the DFA null control `router-prefix-order` used
below. This means the aligned twin CANNOT answer Q3's `logparse-atomic`
control at all, and narrows the DFA-null noise-band population from
100 shared unaligned keys to 62 available on the aligned pair (see §3).
Not fixed by this lane (a read lane; the fix + re-measure is OWED, same
shape as O-64→O-65).

## 2. Placement, not code: `program_sha256` is IDENTICAL, aligned vs unaligned, on every checked cell

`docs/dev/measurements/probe_b110_align64loops_placement.py` / the
`.txt` archive, PARTS 1-2 and 4. Compared via the store records'
`engine_metadata.program_sha256` (pcrec's own emitted-C identity, [B88]
schema v1.7):

- Both witnesses, both forms (plain/whole-subject), all four arms (auto,
  nolitrun, auto-aligned, nolitrun-aligned): **`program_sha256` IDENTICAL
  between an arm and its aligned twin, and DIFFERENT between auto and
  nolitrun (as expected — `-fno-lit-run` is a real code change)**. 4/4.
- Every one of the 100 unaligned DFA-null (program-identical between
  auto and nolitrun) compile keys that also compiled on the aligned
  pair (73/73 for auto vs auto-aligned, 72/72 for nolitrun vs
  nolitrun-aligned; the remaining 27-28 keys are the §1 roster gap):
  **0 diffs**. So pcrec's own emitted C source is provably UNMOVED by
  this project's own phase-2 `cflags` — exactly the property the
  placement twin needs to hold for its comparison to mean anything.
- The `.so` BINARIES differ (`objdump -d` + `sha256sum`, real adapter
  builds under `build/work/pcrec-auto{,-align64loops}/p-<pattern>/plain/t1/`):
  distinct file sha256 on both witnesses, and every `rx_*` function
  after `rx_match_anchored` shifts by 0x30-0x80 bytes between the
  unaligned and aligned build of the SAME arm (e.g. aws's
  `rx_search_run` 0x2890 → 0x28c0; lp-removed's `rx_match_anchored`
  0xac50 → 0xac80). **Placement moved; code did not.** This is the
  proof the twin measures what Q2 asks.

## 3. The headline ratios: BOTH shrink toward null, neither reaches it

Read directly from the two report TSVs' `ratio_vs_baseline` column
(set grain, plain form; `router-prefix-order` as the DFA null control —
program-identical on both windows, unaffected by the roster gap).

| pattern | regime | unaligned (O-65 same-window) | aligned (this window) | excess shrinks by |
|---|---|---|---|---|
| aws-access-key-id | throughput | **1.0361** | **1.0144** | ~60% (3.61%→1.44% excess) |
| aws-access-key-id | search | 0.9813 | 1.0089 | direction flips, both inside noise band (§4) |
| logparse-atomic-removed | throughput | **1.1174** | **1.0286** | ~83% (11.74%→2.86% excess) |
| logparse-atomic-removed | search | **1.0833** | **1.0341** | ~59% (8.33%→3.41% excess) |
| router-prefix-order (control) | throughput | 1.0003 | 1.0004 | — |
| router-prefix-order (control) | search | 1.0003 | 0.9977 | — |

**Neither ×1.037 nor +0.7-1.4 ns SURVIVES INTACT: both shrink
substantially toward 1.0 under alignment, but neither reaches the noise
band (§4) or flips sign cleanly.** lp-removed throughput is the
cleanest case — the biggest excess (11.7%) shrinks the most (to 2.9%,
inside a band whose own DFA-null spread on THIS window reaches ±3.9%,
so this ONE cell is now arguably within noise) while lp-removed search
(8.3%→3.4%) stays outside the search band's own tighter ±2.4% spread.
aws throughput (3.6%→1.4%) also stays outside its own DFA-null
population's spread on this window. Read plainly: alignment/placement
accounts for MOST but not clearly all of O-64's two headline misses —
a partial-placement finding, not a clean placement-only or code-only
one.

## 4. The noise band, computed the same way on both windows

Set-grain `ratio_vs_baseline` (auto÷nolitrun, plain form) over every
DFA-null (program-identical, per §2's method) compile key available in
each report — 61/99 keys on the aligned window (narrowed by §1's roster
gap), 99/123 on the unaligned:

| window | regime | n | min | max | mean | stdev |
|---|---|---|---|---|---|---|
| aligned | throughput | 31 | 0.9733 | 1.0387 | 0.9988 | 0.0108 |
| aligned | search | 30 | 0.9870 | 1.0235 | 0.9999 | 0.0057 |
| unaligned | throughput | 50 | 0.9488 | 1.0131 | 0.9974 | 0.0096 |
| unaligned | search | 49 | 0.9898 | 1.0266 | 1.0010 | 0.0058 |

The two windows' own noise bands are comparable in magnitude (stdev
~1%, both regimes) despite being measured ~2-5 hours apart on different
box states — a same-order-of-magnitude cross-window agreement, not a
proof the two windows are directly poolable (they are NOT the same
window; see §5's caveat).

## 5. Aligned ÷ unaligned per arm (the within-arm effect of adding the flags) — CROSS-WINDOW, read with caution

Not asked for directly by I-115 Q2, but sitting in the same numbers:
does adding `-falign-functions=64 -falign-loops=64` alone move EITHER
arm's own absolute time, aligned vs its own unaligned build?

| pattern | regime | auto: aligned/unaligned | nolitrun: aligned/unaligned |
|---|---|---|---|
| aws-access-key-id | throughput | 0.9781 | 0.9990 |
| aws-access-key-id | search | 0.9745 | 0.9479 |
| logparse-atomic-removed | throughput | 0.9554 | 1.0379 |
| logparse-atomic-removed | search | 0.9530 | 0.9983 |
| router-prefix-order (control) | throughput | 0.9916 | 0.9915 |
| router-prefix-order (control) | search | 1.0226 | 1.0254 |

**CAVEAT STATED PLAINLY: this row is a CROSS-WINDOW comparison** — the
unaligned pair ran 2026-09-28 04:10-05:21 EDT, the aligned pair
06:15-06:58 EDT, on the same box but not the same measurement session,
so a cell here conflates the alignment flags' own effect with whatever
moved on the box between windows (frequency scaling, cache state,
other-core load — §0's worst-busy readings differ, 25.0% vs 38.1%).
`router-prefix-order`'s own control reads ~1-2.5% off unity in BOTH
directions (throughput down, search up) — a same-order-of-magnitude
cross-window swing to the §4 within-window noise bands, which is the
right read of this table's precision: real per-pattern shifts of a few
percent are not reliably separable from cross-window noise at this
grain. No same-window unaligned-vs-aligned control exists (O-66 item 2
explicitly did not add the unaligned pair to this window).

## 6. What was NOT measured / read

- The `logparse-atomic` control (I-115 Q3's own pattern) has NO reading
  on the aligned twin at all (§1's roster gap — refused identically on
  both aligned arms, not a placement question).
- No `perf`/hardware counter reading (same constraint as O-66: this box
  refuses unprivileged `perf`, no sudo used).
- No fix was made to the roster gap; no re-measurement was launched.
- `make check-report` / a full `make check` were not run (this lane
  touched no reporter/harness/interpreter code, only report outputs, a
  measurement archive, and docs).

## Checks

- `make check-interpret`: see the lane report for the exact count (run
  worktree, `gnutimeout 900`).
- No `store/` file was written by this lane; the render is read-only
  over the store the `[B110]` window commit already wrote.
- Nothing under `~/pcrec` was touched.
