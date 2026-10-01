# Lane `b120reseed` — delivery report (PARTIAL: Phases A+B done, C BLOCKED on the manager's slot)

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

## Phase C (TIMING) — BLOCKED, not started

Per `docs/dev/lanes/BOILERPLATE.md` and this brief: timing needs a quiet
box, and other lanes are compiling right now (confirmed live:
`capability@0.1`'s own `pcrec_fc719ca4_*_cf-o*` cells are mid-window as
of this report, 2026-10-01 ~09:41Z — [B117]'s olevel census). **I have
NOT launched anything in Phase C** and am sending the manager the slot
request (SendMessage, separate from this file) before doing so, per the
brief's own stop instruction.

**What Phase C will do once cleared** (restated so a fresh agent or the
manager can act on this file alone):

- **Items 1+2 (the b109-style standalone multi-launch probe, SCRATCH,
  never `store/`)**: a new `docs/dev/measurements/probe_b120_reseed_
  multilaunch.py`, following `probe_b109_reseed_twin.py`'s exact shape
  (compile both arms — default vs `-fno-hyb-reseed` — via the pinned
  fc719ca4 binary's own CLI, under BOTH gcc and clang, build a drv.c
  reusing I-114's own best-of-N + answer-hash shape, 15 FRESH launches
  per cell via `probe_b109_multilaunch.sh`'s own harness), over:
  - utf8@0.1's `asr-lb-varwidth`/`-fixed`/`-neg` × all seven throughput
    subjects (`bench/utf8/throughput/`, regenerated) + I-114's three
    synthetic subjects (its own embedded generator, seed 20260927,
    reproduced verbatim as `probe_b109_reseed_twin.py` already does);
  - syntax@0.1's `lka-pos`/`lka-verb` × a THIRD arm, forced `--engine=vm`
    (I-124 item 2's own three-way ask), over whichever subjects give
    both a sparse-candidate and a match-dense (find-all) reading — the
    syntax@0.1 search_short/throughput subjects, read from
    `bench/syntax/subjects/`+`manifest.tsv`, is the natural source; no
    new subject generation needed.
  - Answer identity (match count + span hash) checked on every cell
    BEFORE any ratio is trusted, exactly as I-124's own closing
    paragraph requires.
- **Item 3's real window**: the six-cell `run_suite.sh` invocation
  above, launched by the MANAGER per `BOILERPLATE.md`'s "long runs at
  the end of a lane" rule (~3.7 h, over the ~4-minute DO-THEN-FINISH
  threshold) — not by this lane.

## Charter-vs-committed checklist

| I-124 item | status |
|---|---|
| Phase A: compile-only census, every bench pattern × {auto, auto-utf8} | **DONE**, committed (`probe_b120_census.py`, the 2026-10-01 archive) |
| Phase B: `pcrec-auto-nohybreseed` + utf8 sibling + clang siblings pinned | **DONE**, committed (configs.toml, capability roster, all checks green) |
| Phase B: window cell list for item 3 | **DONE**, this file, above |
| Item 1 (utf8@0.1, both compilers, 15 launches, 10 subjects) | **OWED** — Phase C, blocked on the manager's slot clearance |
| Item 2 (syntax@0.1 lka-pos/lka-verb, 3-way) | **OWED** — Phase C, same block |
| Item 3 (roster-wide adaptive* window, >5% slower names) | **OWED** — the six-cell window above, to be LAUNCHED BY THE MANAGER once cleared (DO-THEN-FINISH: this lane's last act is this report + the slot request, not the run itself) |
| "A cell whose answer moves is reported before any timing" | Not yet applicable — no timing has run. Phase A is compile-only by construction and carries no answer check; the answer-identity check belongs to Phase C and will be reported there, before any ratio |

## OWED

- Items 1, 2 and 3's actual TIMING NUMBERS (Phase C), blocked on the
  manager's slot clearance — see the SendMessage sent alongside this
  report.
- `probe_b120_reseed_multilaunch.py` (items 1+2's reproducing script) —
  not yet written; Phase C's first act once cleared.
- The six-cell item-3 window's launch, log path and `.done` marker —
  OWED to the manager per BOILERPLATE.md (a run this long is launched
  by the manager, not this lane).
- A draft outbox item answering I-124 is NOT yet written (nothing to
  report to pcrec until Phase C has numbers) — `b120reseed_outbox_draft.md`
  beside this file states that explicitly rather than guessing ahead of
  the data.

## Files touched

- `testees/pcrec/configs.toml` (4 new `[testees.*]` blocks)
- `bench/capability/gen_patterns.py` (+1 `EXT_BENCH_ROSTER` row, +3
  `EXCLUDED_TESTEES` entries)
- `bench/capability/patterns.rxt` (regenerated)
- `docs/dev/measurements/probe_b120_census.py` (new)
- `docs/dev/measurements/2026-10-01-b120-reseed-census.txt` (new)
- `docs/dev/measurements/CLAUDE.md` (+1 entry)
- `docs/dev/lanes/b120reseed_report.md` (this file, new)
- `docs/dev/lanes/b120reseed_outbox_draft.md` (new, placeholder — see
  its own text)
