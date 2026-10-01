# Lane `b120reseed` — delivery report (items 1+2 COMPLETE; item 3's roster window is the manager's)

[B120] (`docs/dev/plan.md`; pcrec inbox I-124,
`docs/dev/inbox_from_pcrec.md` "## I-124"): the [OPT-HYB-RESEED]
adaptive-retry x86 re-measure at pin **fc719ca4** (abi 50; the retry
landed at abi 49, [OPT-HYB-RESEED-XCALL] is its named follow-on trigger
if item 2's prediction confirms). Worktree `worktrees/b120reseed`,
branch `lane/b120reseed` from `master` (base `bfa27e6`, "[B119]/[B120]/
[B121] started: three lanes").

## What I-124 asks, restated

1. **utf8@0.1, auto vs `-fno-hyb-reseed`, BOTH compilers, 15 fresh
   launches each**, all seven throughput subjects + I-114's three
   synthetic ones, on `asr-lb-varwidth`/`asr-lb-fixed`/`asr-lb-neg`.
   PREDICTION: varwidth/neg sparse ×2-×21 faster; fixed/synth-dense
   flat; `clamped` rows unmoved.
2. **syntax@0.1's `lka-pos`/`lka-verb`**, auto vs denied vs forced-VM.
   PREDICTION: auto no longer equals forced-VM; faster sparse, possibly
   SLOWER match-dense (find-all) — the `[OPT-HYB-RESEED-XCALL]` trigger.
3. **Any roster cell stamping `adaptive*`**, bucketed by row x
   `RX_VM_FRAMELESS`, naming any cell >5% slower than the deny.
4. Answers are identical by construction; a moved answer is reported
   before any timing.

## Order of work

### Phase A (no timing) — DONE, committed

`docs/dev/measurements/probe_b120_census.py`: every bench pattern (all
eight sub-benches, by enumeration — `tools.selfcheck.subbench_dirs()`)
compiled under `pcrec-auto` and `pcrec-auto-utf8` at fc719ca4,
collecting `RX_VM_RESEED`/`RX_VM_FRAMELESS`/`RX_ENGINE`/`RX_ENGINE_SEL`.
Compile-only, no gcc, no timing, no store write. Archived:
`docs/dev/measurements/2026-10-01-b120-reseed-census.txt`.

**678 rows (339 patterns × 2 configs): 487 DFA / 142 VM / 49 refused.**
Zero `fixed` reads under default compile anywhere (expected — it is
the deny's own landing row). 27 `adaptive*` cells across **15 distinct
patterns in exactly three sets**: capability, syntax, utf8. No
`email`/`altwide`/`bounded`/`litrun` pattern stamps `adaptive*` at all
(their hybrids land in `exact`/`clamped`).

| set | config | row | frameless | patterns |
|---|---|---|---|---|
| capability | auto | adaptive-dense | 1 | logparse-atomic |
| capability | auto-utf8 | adaptive | 0 | utf8-lead-no-cont |
| syntax | auto / auto-utf8 | adaptive | 0 | grp-atomic-alt, lka-neg, lkb-neg |
| syntax | auto / auto-utf8 | adaptive | 1 | lka-nonatomic, **lka-pos**, **lka-verb**, lkb-pos, qnt-poss-plus, qnt-poss-quest |
| utf8 | auto / auto-utf8 | adaptive | 0 | asr-lb-neg, asr-lb-varwidth |
| utf8 | auto | adaptive | 1 | asr-lb-fixed |
| utf8 | auto-utf8 | adaptive | 1 | asr-lb-class, asr-lb-fixed |

**I-124's own five named patterns are confirmed in the population by
value, before any timing**: item 1's `asr-lb-varwidth`/`asr-lb-fixed`/
`asr-lb-neg` all stamp `adaptive` under `pcrec-auto-utf8` (the ONLY
pcrec config bench/utf8 ever runs — confirmed against `store/
index.tsv`: every historical utf8@0.1 pcrec record is one of the four
`-utf8` siblings, never plain `pcrec-auto`); item 2's `lka-pos`/
`lka-verb` both stamp `adaptive`, `frameless=1`, under BOTH encoding
configs (the whole nine-pattern `lka-*`/`lkb-*`/`grp-atomic-alt`/
`qnt-poss-*` family is encoding-invariant — no multi-byte-sensitive
construct in any of the nine, so syntax@0.1's own window needs no
`-utf8` arm for item 2).

Two findings beyond the ask: `asr-lb-class` also stamps `adaptive`, but
ONLY under `auto-utf8` (not one of I-124's three named patterns, noted
not folded in); `capability/logparse-atomic` is the roster's **only**
`adaptive-dense` cell anywhere, byte-only (it reads `clamped` under
`-e utf8` — the MRL clamp wins once compiled against the utf8 byte-rate
prior). `utf8-lead-no-cont`'s own `adaptive` cell is a CENSUS ARTIFACT
only: `bench/capability` never compiles under `-e utf8` in a real
window (the set declares no utf8 encoding, [B77] U2's convention), so
this cell is not reachable by item 3's real window below — recorded for
completeness, not actioned.

### Phase B (no timing) — DONE, committed

**Four new pinned testees** (`testees/pcrec/configs.toml`,
`-fno-hyb-reseed` already in `adapter.py`'s `DENY_FLAGS` since [B118]):

| testee_id (CLI) | derived store id | what it is |
|---|---|---|
| `pcrec-auto-nohybreseed` | `pcrec_fc719ca4_auto-caps-simdna_nohybreseed` | item 3's byte BEFORE/AFTER twin |
| `pcrec-auto-nohybreseed-utf8` | `..._nohybreseed-utf8` | item 1/3's utf8 twin |
| `pcrec-auto-clang-utf8` | `..._cc-clang-utf8` | item 1's undenied clang+utf8 baseline (crosses [B24]'s cc axis with [B77] U2's encoding axis for the FIRST time on this roster — no prior `-utf8`+`-clang` combo existed) |
| `pcrec-auto-clang-nohybreseed-utf8` | `..._cc-clang-nohybreseed-utf8` | item 1's clang+denied arm |

Verified (not merely derived): all four distinct, collision-free
`testee_id`s; the deny flag reaches `adaptive -> fixed` on
`(?<=a|\xc3\xa9)x` under `-e utf8` on **both** gcc and clang
(`emit_bytes` 31714 -> 31183, matching the flat per-artifact shrink the
[B118] CLAUDE.md entry already predicted for this witness); capability
roster coverage (60 testee ids total, 4 PASS arms,
`check_capability_roster_coverage`), `check_deny_flag_controls` (18/18)
and `check_mechanism_stamps` (80/80) all green at the HEAD of this
branch.

`bench/capability/gen_patterns.py`: `pcrec-auto-nohybreseed` added to
`EXT_BENCH_ROSTER` (an emit-side denial, satisfies exactly
`pcrec-auto`'s own tokens — the [B101]/[B108] reasoning stated
verbatim); `pcrec-auto-nohybreseed-utf8` / `pcrec-auto-clang-utf8` /
`pcrec-auto-clang-nohybreseed-utf8` added to `EXCLUDED_TESTEES` (every
`-utf8` config is excluded for the one reason every other `-utf8`
config already states — `bench/capability` is byte-mode-only).
`patterns.rxt` regenerated and `--check`-clean.

### The window-cell list, item 3 ([B120]'s own deliverable)

Item 3's real window needs `{auto, nohybreseed}` on every (set, testee
family) whose population contains an `adaptive*` artifact, restricted
to configs each set actually runs (`utf8@0.1` never runs plain
`pcrec-auto`; `capability@0.1` never runs `-utf8`):

| cell | testee | population reached | est. duration | basis |
|---|---|---|---|---|
| syntax@0.1 | `pcrec-auto` | 9 adaptive patterns (incl. lka-pos/lka-verb) | ~46 min | `store/index.tsv` gap, `pcrec_751b9c6d` auto-caps -> auto-nocaps, same set, 2026-09-27 |
| syntax@0.1 | `pcrec-auto-nohybreseed` | same 9, denied | ~46 min | same population size; no reason to differ materially |
| capability@0.1 | `pcrec-auto` | 1 adaptive-dense pattern (logparse-atomic) | ~34 min | `store/index.tsv` gap, `pcrec_fc719ca4` auto-caps -> `_cf-o0`, THIS pin, 2026-10-01 (the currently-running [B117] olevel window) |
| capability@0.1 | `pcrec-auto-nohybreseed` | same 1, denied | ~34 min | same population size |
| utf8@0.1 | `pcrec-auto-utf8` | 4 adaptive patterns (asr-lb-varwidth/fixed/neg/class) | ~61 min | `store/index.tsv` gap, `pcrec_751b9c6d` auto-caps_utf8 -> auto-nocaps_utf8, 2026-09-27 |
| utf8@0.1 | `pcrec-auto-nohybreseed-utf8` | same 4, denied | ~61 min | same population size |

**Total ≈ 3.7 h for all six cells**, each individually well inside the
5,400 s (90 min) default `$CELL_CAP`. Exact command (the standard
`run_window.sh`/`run_suite.sh` shape, `scripts/CLAUDE.md`):

    SUITE="syntax capability utf8" \
    TESTEES_syntax="pcrec-auto pcrec-auto-nohybreseed" \
    TESTEES_capability="pcrec-auto pcrec-auto-nohybreseed" \
    TESTEES_utf8="pcrec-auto-utf8 pcrec-auto-nohybreseed-utf8" \
    setsid scripts/run_suite.sh > build/windows/b120_$(date +%Y%m%dT%H%M%S).log 2>&1 &

No `-clang` arm is in this list: I-124 item 3 does not ask for both
compilers, only item 1 does, and item 1's own measurement (Phase C) is
a standalone probe, not this harness window (see below) — the two
clang+utf8 testees exist for a later cross-check if the manager wants
one folded into a real window, but nothing above needs them.

**One thing this window does NOT answer that a reader might expect it
to**: `pcrec-auto`/`pcrec-auto-utf8` on these three sets ALREADY HAVE
committed records at older pins (`751b9c6d`, `fc719ca4`'s own
currently-running capability@0.1 cell). The NEW record this window adds
for `pcrec-auto`/`pcrec-auto-utf8` at fc719ca4 is itself a useful
same-pin control if one does not already exist — `check` the index
before running to avoid a redundant cell.

## Phase C (TIMING) — items 1+2 DONE; item 3's window handed to the manager

Cleared by the manager 2026-10-01 (box verdict `quiet`, load1
0.07-0.09, `b121asks` on a CPU hold — the capability@0.1 cells I had
seen were [B117]'s own committed window, last written 06:21, not a
live run). Pre-flight: `python3 -m pcrecbench quiet --samples 5` ->
**VERDICT: quiet** on all five samples (max_busy_pct 1.6-3.41,
threshold <=10.00). Per-core `mpstat -P ALL 1 1`: before, every core
<=1.00% user / 0% busy except one at 1.00%; after, every core <=2.00%
user, 11/12 cores fully idle — nothing else used the box during the run.

**Items 1+2 ran as the standalone multi-launch probe** (SCRATCH, never
`store/`): `docs/dev/measurements/probe_b120_reseed_multilaunch.py
--trials 21 --launches 15 --out /var/tmp/b120reseed-real`, launched in
the background with a `DONE rc=0` completion marker, ~2,070 process
launches across 138 cells, completed clean in well under a minute of
wall time (far under the 60-minute estimate threshold — no upfront
estimate message was needed). **Answer identity: 0 mismatches
anywhere.** The driver's own within-process check printed zero
`NONDETERMINISM` lines across all 138 cells; a SEPARATE cross-arm check
(re-running every (pattern, subject) once per arm and diffing the
`matches=.../hash=...` line byte for byte) found 0/120 mismatches in
GROUP U (default vs denied x gcc vs clang) and 0/18 in GROUP S
(default vs denied vs forced `--engine=vm`, gcc) — including the
forced-VM arm against `auto`'s own route, a stronger check than I-124
asked for. Archived: `docs/dev/measurements/2026-10-01-b120-reseed-
multilaunch.txt` (full ratio tables, environment, quiet-gate output).

**Each I-124 sub-claim, CONFIRMED / REFUTED / NOT TESTED, with numbers:**

| # | claim | verdict | numbers |
|---|---|---|---|
| 1a | varwidth/neg sparse-candidate x2-x21 faster | **CONFIRMED in direction, MAGNITUDE FAR EXCEEDED** | I-114's own synthetic subjects (synth-64k-asc/synth-1m) land near the predicted band (1.17-3.95x on varwidth); `bench/utf8`'s own real throughput prose reads **11x-99x** (varwidth: 29-99x on t-64k/t-64k-asc/t-64k-lat/t-1m/t-256k/t-64k, both compilers; neg: 12-41x on the same subjects) — an order of magnitude past the predicted ceiling, because ordinary prose has an uncontrolled, often higher failed-candidate density than I-114's density-tuned synthetic subjects, and the pre-abi-48 FIXED behaviour re-seeds (full prefilter re-scan) after every failed candidate |
| 1b | fixed/synth-dense flat (+-5%) | **CONFIRMED** | gcc: denied/default = 1.042 (4.2%); clang: 0.967 (3.3%) — both inside the band |
| 1c | clamped rows do not move | **NOT TESTED** | none of this probe's five patterns carries the `clamped` row (Phase A: it's on bounded/capability/loglines); item 3's own window is where this gets tested |
| 2a | auto no longer equals forced-VM | **CONFIRMED** | all six (pattern, subject) cells read auto/forced-vm away from 1.0, 0.33-1.90x, in both directions |
| 2b | faster sparse / slower (XCALL trigger) match-dense | **NOT CLEANLY TESTABLE with these subjects** | `bench/syntax`'s t-64k/t-256k/t-1m are the SAME grammar at three independently-drawn sizes, not a density-controlled sparse/dense pair; `lka-verb` reads auto FASTER than forced-vm at all three sizes (0.75/0.33/0.43) while `lka-pos` flips (1.47/1.90/0.47) — no clean size-monotonic trend either, consistent with "no controlled density axis here" rather than with either verdict |
| 3 (this probe's slice) | any adaptive* cell >5% slower than denied | **NONE FOUND**, with a caveat | every cell with real candidate traffic reads default FASTER than denied (the whole speedup/denied-over-auto columns exceed 1.05); the only "slower" readings are three asr-lb-neg cells at 1.1-3.0 us absolute (near this box's timer floor, where the pattern's candidate byte barely occurs in that subject) — flagged, not treated as a genuine `[OPT-HYB-RESEED-XCALL]` trigger per this project's own measurement discipline (no conclusion from a floor-level ratio) |

**Item 3's full roster window is NOT run by this lane.** Per the
manager's explicit instruction ("Do NOT launch the item-3 window: I'll
run it from master after I merge your branch"), the six-cell plan
above (syntax/capability/utf8 @0.1 x {auto, nohybreseed-variant}, ~3.7h
estimated) is handed back for the manager to run from `master` post-merge.

## Charter-vs-committed checklist

| I-124 item | status |
|---|---|
| Phase A: compile-only census, every bench pattern × {auto, auto-utf8} | **DONE**, committed (`probe_b120_census.py`, the 2026-10-01 archive) |
| Phase B: `pcrec-auto-nohybreseed` + utf8 sibling + clang siblings pinned | **DONE**, committed (configs.toml, capability roster, all checks green) |
| Phase B: window cell list for item 3 | **DONE**, this file, above |
| Item 1 (utf8@0.1, both compilers, 15 launches, 10 subjects) | **DONE** — confirmed in direction, magnitude far exceeded (11x-99x vs predicted x2-x21) |
| Item 2 (syntax@0.1 lka-pos/lka-verb, 3-way) | **DONE** — auto != forced-VM confirmed; the sparse/dense sub-claim not cleanly testable with the available subjects |
| Item 3 (roster-wide adaptive* window, >5% slower names) | **PARTIAL**: this probe's own five-pattern slice finds none (outside timer-floor noise); the full roster window is OWED to the manager, who runs it from `master` post-merge per their own instruction |
| "A cell whose answer moves is reported before any timing" | Satisfied: answer identity checked (0/138 driver-internal, 0/138 cross-arm) BEFORE any ratio in this report was read |

## OWED

- Item 3's full roster window (the six-cell plan above) — the manager
  runs this from `master` after merging this branch, per their own
  instruction ("Do NOT launch the item-3 window: I'll run it... after I
  merge your branch").
- A draft outbox item answering I-124, now that Phase C has real
  numbers — `docs/dev/lanes/b120reseed_outbox_draft.md` is UPDATED
  below with the real findings; the manager drafts the actual O-n from
  it per this project's usual division of labour (lane reports, manager
  drafts outbox).

## Files touched

- `testees/pcrec/configs.toml` (4 new `[testees.*]` blocks)
- `bench/capability/gen_patterns.py` (+1 `EXT_BENCH_ROSTER` row, +3
  `EXCLUDED_TESTEES` entries)
- `bench/capability/patterns.rxt` (regenerated)
- `docs/dev/measurements/probe_b120_census.py` (new)
- `docs/dev/measurements/2026-10-01-b120-reseed-census.txt` (new)
- `docs/dev/measurements/probe_b120_reseed_multilaunch.py` (new,
  Phase C's instrument, RUN for real — see its own archive)
- `docs/dev/measurements/2026-10-01-b120-reseed-multilaunch.txt` (new,
  the Phase C archive: full ratio tables, environment, quiet-gate output)
- `docs/dev/measurements/CLAUDE.md` (+2 entries)
- `docs/dev/lanes/b120reseed_report.md` (this file)
- `docs/dev/lanes/b120reseed_outbox_draft.md` (updated with real findings)
