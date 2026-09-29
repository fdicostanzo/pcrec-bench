# [B115] FINDINGS-BENCH-TIERS: the first four-column read (pcrec f7f5a143, scratch tier)

Charter: inbox I-118 (answered in O-72). pcrecdev1 confirmed it; the plan
row is [B115]. Tier: SCRATCH, through the `pcrec-local` testee at pcrec
f7f5a143 (abi 44). Nothing here entered `store/` or a ranking.

The tables are archived verbatim with their source header in
`docs/dev/measurements/2026-09-29-b115-findings-tiers-{loglines,email}.tsv`.
Each value is a set-grain median in ns (`reduce.reduce_set_cell`). Every
ratio below is **arm ÷ DEFAULT**, and lower means faster.

## What ran

- **When and where.** 2026-09-28 21:01 to 2026-09-29 04:55 EDT, on ubuntubudu
  (Ryzen 5 1600, gcc 15.2.0, governor schedutil). The pre-flight quiet
  verdict was `quiet` on every cell, with load1 about 0.9-1.1 (that is the
  sweep's own load; the threshold is 2.0).
- **Records.** 51 arm-records, 5 trials each, all status `measured`.
  - loglines@0.1 has 34 arms: DEFAULT; auto/vm/dfa × tune {−2..2} ×
    caps/nocaps; DECLARED `weblog` and `log`; PROFILED `loglines-profiled`.
  - email-specimen@0.2 has 17 arms: DEFAULT; auto/vm/dfa × tune; PROFILED
    `email-prose-profiled`. There is no nocaps twin, because `orig` and
    `factored` capture, and there is no DECLARED arm (O-72 Q4).
- **The auto-arm re-run.** The first pass wrote 36 of 51. The 15
  `--engine=auto --tune=N` arms were refused by our adapter's ENGINE_SEL
  agreement check, which counted `--engine=auto` as a forced route.
  8baab6d fixed that, and the 15 arms were re-run 02:48-04:55 into the
  same scratch store.
- **The bundle each arm used.** Every DECLARED/PROFILED arm's FINDINGS
  stamp names the bundle it meant, and every digest equals the archived
  `pcrec --list-analysis` output
  (`testees/pcrec/findings/*/list_analysis_*.tsv`): weblog `6b85ed6b…`,
  log `13f25004…`, loglines-profiled `b3946370…`, email-prose-profiled
  `8f0dbb8b…`. The other 758 compile rows stamp `default:1822fb97…`. The
  20 rows with no stamp are level-context's DFA refusals.

## Findings

**1. DECLARED is data that can mislead. weblog makes two loglines patterns slower.**

| pattern | regime | DECLARED-weblog | the stamp that moved (auto, plain form) |
|---|---|---|---|
| iso-ts | throughput / search | **×1.469 / ×1.838** | `RX_REQ_BYTE` 45 `-` → 58 `:` |
| kv-quoted | throughput / search | ×1.037 / **×1.313** | `RX_REQ_BYTE` 34 `"` → 61 `=`; the run anchor `3d22@1` → `@0` |

weblog is Apache access-log text, and its `-` and `"` frequencies differ
from our mixed-format log text. The data picks a byte that is common in
our subjects, so the change costs time. Every other loglines pattern is
within ±1% under weblog.

DECLARED-log is mixed:
- iso-ts runs ×0.911 / ×0.966 (faster).
- http-5xx runs **×1.168 / ×1.100** (slower). Its `RX_REQ_BYTE` moves 80
  `P` → 84 `T`, and the run index moves `@4` → `@3`.

**2. PROFILED never makes a cell measurably slower, and wins on three patterns.**

| pattern | throughput / search | the mechanism the stamps show |
|---|---|---|
| stack-frame | **×0.721 / ×0.782** | `RX_REQ_BYTE` 97 → 116; `RX_REQ_WHY` emitted → dominated; the prefilter changes from `offset-set-bounded` to `run-pinned-bounded` |
| http-5xx | ×0.900 / ×0.908 | `RX_REQ_BYTE` 80 → 72 `H`; the run index moves to `@1` |
| iso-ts | ×0.911 / ×0.965 | NO stamp we read moved, but `program_sha256` DID. The program is identical to DECLARED-log's, whose time is also identical. Some data-driven decision outside the six stamps read here |

Every other loglines cell is within +0.4%. On email, PROFILED
(prose-trained) is 0.994-1.001 everywhere, which means no effect.

**3. ORACLE-BEST, the selector headroom, is about zero on loglines and real on email's whole-subject forms.**

- **loglines.** Every cell is ×0.989-1.001, except `floor` search at
  ×0.968 (winning arm `vm tune 0`). The winning arm varies at random
  across dfa/auto/tune, which is what a noise floor looks like.
- **email.** The `floor` compliance cell (whole-subject form) runs
  **×0.648** under `vm tune 0`. `orig` compliance runs **×0.856** under
  `vm tune 2`. `floor` search runs ×0.916 under `vm tune −2`. On these
  whole-subject cells the forced-VM route beats what `auto` selects: an
  input for [SEL-COST].
- **email `factored` compliance.** Its five forced-VM arms are EXCLUDED
  from the min, because they give up with `PCREC_ERR_FRAMES` on s-058,
  -059, -061, -063 and -064. That is a standing outcome, not a new one:
  every pinned `pcrec-vm` email record from 35e1ab1 to 751b9c6d carries
  the same 25 give-ups. Without those arms, its ORACLE-BEST is 1.000.
- **level-context.** Its ten `--engine=dfa` arms refuse, with ">32000
  states; try --engine=vm", a known limit. They are excluded and flagged.

**4. `--tune` changes the program at only two positions.** Each count
below is the number of (pattern, form, caps) groups where the tune
position's `program_sha256` differs from tune 0's.

| route | −2 | −1 | +1 | +2 |
|---|---|---|---|---|
| dfa (loglines / email) | 40/40 · 6/6 | 0 · 0 | 0 · 0 | 0 · 0 |
| auto | 44/44 · 6/6 | 0 · 0 | 0 · 0 | 0 · 0 |
| vm | 0 · 0 | 0 · 0 | 8/44 · 0/6 | 8/44 · 0/6 |

DEFAULT's program is identical to tune 0's on every group checked. So on
these two sets the five-notch dial yields at most two distinct programs
per route. The ORACLE-BEST winners that name tune ±1 or −1 on the dfa or
auto routes are therefore timing the SAME program as tune 0. This is
direct evidence for pcrec's D129 Q1 re-proposal. It also means a future
`--extended` sweep can run tune {−2, 0, 2} without losing a program.

## The noise floor, measured, and what it does not cover

- **Identical programs time alike.** Where a program is byte-identical to
  DEFAULT's, times agree within about 0.1-0.2%. Examples: stack-frame
  under weblog and log; level-context's oracle arm, which reads ×1.001,
  above DEFAULT.
- **One launch per arm.** Each arm's five trials share ONE driver
  process. [B112]/O-69 found per-launch bimodality, from the CPU
  frequency governor's state at process start. A ±1% difference between
  two arms is therefore NOT a finding in this sweep. Every effect named
  above is ≥ 3%, and each coincides with a program change.
- **Not read.** Match counts per arm beyond the correctness gate. The
  compile-time axis: all four columns change match-time decisions, and
  compile cost was not compared. The seven other stamp families beyond
  the six read in findings 1-2. Any `--extended` set (bounded, altwide,
  capability, syntax). The caveat pcrecdev1 accepted also applies:
  ORACLE-BEST holds findings at `default`, so "oracle ÷ declared" mixes
  knobs and data. That ratio is in the TSV and not used here.

## What goes to pcrec (O-74)

These are findings 1-4, as facts only. The run-rarity arm stays out while
[FINDINGS] B4 is held. Frank reads these before any ruling on published
configs.
