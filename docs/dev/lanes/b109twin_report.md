# Lane `b109twin` — delivery report

[B109] (`docs/dev/plan.md`; pcrec inbox I-114,
`git -C ~/pcrec show origin/main:docs/dev/utf8_attrib_twin/I-114.md`):
the x86 CONFIRM of the [OPT-HYB-RESEED] hand-twin. I-114 hand-wrote a
twin of pcrec's proposed fix (the VM hybrid's unanchored retry loop
re-seeding `attempt_position` from the DFA prefilter after EVERY failed
attempt, not only under an MRL clamp) on three lookaround patterns at
pin a32bc86e, measured it on an Apple M1 (scratch tier, box not quiet),
and asked this project to confirm on x86: answers identical, timing
reproduced or not, and specifically whether x86 shows the Mac run's
dense-candidate slowdown on `asr-lb-fixed` (`(?<=é)x`, ×0.81-0.90 twin
SLOWER on its two densest subjects).

Worktree `worktrees/b109twin`, branch `lane/b109twin` from `master`
(base `9d9ea41`, "plan: [B109] + [B105] started"). Scratch tier
throughout — no `store/` or `reports/` write, nothing measured here
enters a ranking.

## Order of work

1. Located the pinned a32bc86e binary already built
   (`testees/pcrec/pin.sh --path a32bc86e`) and the `bench/utf8`
   throughput-subject generator (deterministic, regenerated in this
   worktree since the generated subjects are gitignored per-worktree).
2. Compiled the three patterns, verified the retry-loop needle I-114's
   diffs target matches this pin's emitted C BYTE FOR BYTE (line
   numbers included) before applying anything.
3. Applied I-114's 8-line hand twin verbatim to all three, confirmed
   each diff against I-114's own three diffs (identical).
4. Built orig+twin under BOTH gcc and clang, `-O2 -Wall -Wextra`
   (I-114 asked for both compilers; the Mac numbers are gcc-16 only) —
   zero warnings, 12/12 builds.
5. Regenerated I-114's three synthetic subjects from its embedded,
   seeded (20260927) generator — sizes match I-114's stated
   1,000,000 / 65,536 / 200,000 B exactly.
6. Copied and sha256-verified the bench's own seven `bench/utf8`
   throughput subjects against `manifest_throughput.tsv` — all seven
   match.
7. Ran I-114's own find-all driver (best-of-N, full match count + a
   32-byte-span FNV-1a hash) across all 3 patterns x 10 subjects x
   2 compilers x 2 variants = 120 driver invocations, 21 trials each.
8. Added ONE instrument I-114 did not ship, to answer its own ask (4):
   a compile-only candidate-density probe (`rx_prefilter` called
   repeatedly across a whole subject, counted against the real
   find-all match count) — this is what explains the sparse/dense
   split rather than merely restating it.
9. Consolidated everything into one reproducible script,
   `docs/dev/measurements/probe_b109_reseed_twin.py`, and ran it for
   real from the repo root to produce the archive (not hand-assembled
   from ad hoc runs — see the caveat below on why that distinction
   mattered).

Box: quiet throughout (`mpstat -P ALL 1 5` >= 98.7% idle on every core
immediately before the archived run; `/proc/loadavg` 0.18/0.25/0.18
before, 0.38/0.29/0.19 after) — not gated by another session.

## Charter-vs-committed checklist

### 1. Bench's own utf8@0.1 subjects for the three cells — DONE

All seven `bench/utf8/throughput/*.bin` subjects run against all three
patterns, both compilers, both variants (42 cells).

### 2. The lane's three synth-* subjects too — DONE

Regenerated from I-114's own embedded generator, seed 20260927; sizes
confirmed exact (1,000,000 / 65,536 / 200,000 B). Run against all three
patterns, both compilers, both variants (18 cells).

### 3. Answer-identity confirmed independently — DONE, CLEAN

**60/60 (pattern, subject, cc) cells: `matches` and the full-span
FNV-1a hash agree orig vs twin, no exceptions.** As a bonus
cross-check not asked for, gcc vs clang also agree on **60/60** cells
(same variant) — the twin changes no answer on x86 either compiler.
No `NONDETERMINISM` line was ever printed by the driver across any of
the 120 x 21 = 2,520 trials.

### 4. Does x86 show the same subject-composition sensitivity? — YES, WITH A NEW SPLIT

The candidate-density probe makes the mechanism legible: for a given
pattern, the win shrinks monotonically as **candidates per subject
byte** rises (density independent of whether those candidates end up
matching):

| pattern | subject | candidates | bytes | density | matches | ratio (gcc) | ratio (clang) |
|---|---|---:|---:|---:|---:|---:|---:|
| asr-lb-fixed | t-64k-lat | 59 | 65,536 | 0.0009 | 0 | 181.4 | 115.7 |
| asr-lb-fixed | t-64k-asc | 240 | 65,536 | 0.0037 | 0 | 20.8 | 44.9 |
| asr-lb-fixed | synth-1m | 85,292 | 1,000,000 | 0.0853 | 0 | 1.78 | 3.32 |
| asr-lb-fixed | synth-64k-asc | 5,167 | 65,536 | 0.0789 | 0 | **0.57** | 1.26 |
| asr-lb-fixed | synth-dense | 31,459 | 200,000 | 0.1573 | 10,523 | **0.99** | 1.19 |
| asr-lb-varwidth | synth-dense | (same byte 'x') | 200,000 | 0.1573 | 22,505 | 1.04 | 1.30 |
| asr-lb-neg | synth-dense | 21,063\* | 200,000 | 0.1053 | 9,093 | 1.41 | 1.54 |

(\*asr-lb-neg's candidate byte is 本's UTF-8 lead byte, a different scan
from the other two patterns' `memchr('x')`, so its counts are not
directly comparable across the pattern column — only within a pattern's
own row.)

At the sparse end (density < 0.005), x86 shows the SAME direction and a
comparable OR LARGER magnitude to Mac's own ×25-124 (x86 asr-lb-fixed
sparse cells run ×20-270 faster; asr-lb-varwidth/asr-lb-neg sparse
cells ×28-285). At the dense end, the win shrinks toward parity on
every pattern and every compiler — matching Mac's own qualitative
story exactly.

**The headline, beyond a yes/no**: on `asr-lb-fixed` specifically — the
one pattern Mac found genuinely INVERTED (twin slower, ×0.81-0.90) on
its two densest, all-candidates-rejected subjects — **x86 gcc
reproduces a comparable-direction result on the identical two subjects**
(`synth-64k-asc` ×0.57, `synth-dense` ×0.99) **while x86 clang does
not** (×1.26, ×1.19 — twin still faster on the same binaries' own
subjects, same box, same run). `asr-lb-varwidth` and `asr-lb-neg` never
invert on either compiler at any density measured here — the inversion
is specific to `asr-lb-fixed`'s own regime, where (per I-114's own
observation) the pattern's only real matches live in `synth-dense` and
its other high-density subjects are 100% false candidates, so the
twin's extra `rx_prefilter` call is pure overhead with nothing to
amortize it against on gcc's code shape specifically. This is a NEW
finding beyond I-114's own text: the inversion's presence is
compiler-dependent on x86, not just density-dependent, which the
Mac-only, gcc-16-only run could not see.

## MEASUREMENT CAVEAT (found while building this, not predicted by I-114)

This box's `scaling_governor` is `schedutil`. Several cells' trial 0
(and, on `row11_fixed/synth-64k-asc/gcc/orig` specifically, trials 1-7
too) ran at what reads as a throttled/ramping frequency state — that
one cell's raw trials were `2355,2348,2340,2352,2332,1971,1100,929,173,
173,...`, an order of magnitude down before settling. An ad hoc 11-trial
rerun of that exact cell (not archived, done while building the probe
script) found its UNFILTERED median 2.4x a 21-trial rerun's median for
the IDENTICAL binaries and subject, purely from where in the ramp the
median trial landed. The archived numbers use 21 trials, drop trial 0,
and report full max-min spread alongside every median so a
still-contaminated cell is visible in its own spread column rather than
silently averaged away — this is a real residual: `asr-lb-fixed/
synth-64k-asc/gcc/orig`'s own archived spread is 2,178.5 µs against a
median of 173.6 µs. The orig-vs-twin RATIO within one cell (both
variants compiled and measured within the same script invocation,
seconds apart) is the reliable comparison this file supports — cross-run
or cross-machine absolute-µs comparisons are not.

## Deliverables

- `docs/dev/measurements/probe_b109_reseed_twin.py` — the reproducing
  script (self-contained: I-114's three patterns, its exact 8-line
  twin diff, its drv.c, its subject generator, all reproduced verbatim
  inline; plus the density probe, ours). Runs from the repo root:
  `python3 docs/dev/measurements/probe_b109_reseed_twin.py --trials 21`.
  Requires the a32bc86e pin built and `bench/utf8/gen_throughput_
  subjects.py` run first (both already true in this worktree/box).
- `docs/dev/measurements/2026-09-28-b109-reseed-twin-x86.txt` — its
  archive: D35-style source header (bench commit, pin + binary sha256,
  both compiler versions, box/governor, load before/after, the exact
  command), then the script's full verbatim stdout (every build, every
  subject's sha256 check, the candidate-density census, all 120 raw
  driver lines with their 21 comma-separated trial times, both
  answer-identity summaries, and the derived summary table).
- `docs/dev/measurements/CLAUDE.md` — updated with both entries above
  the pre-existing chronological list (newest-first, matching this
  file's own convention).

## Validation run

The probe script's own two identity-check sections ARE the validation:
60/60 orig-vs-twin and 60/60 gcc-vs-clang, both printed `ALL IDENTICAL`
with zero mismatches, in the archived run. No `pcrecbench` harness
change was made by this lane (compile-only + a standalone driver, no
adapter/schema/reporter touched), so no `make check` regression surface
was opened; `make check` was not run and nothing here required it.

## OWED

- Nothing. Every charter item (I-114's four numbered asks, the "what to
  measure on x86" section) is answered and archived; no follow-on run
  is pending from this lane.
- The manager drafts outbox O-68 from this report per the brief's own
  instruction — not written here.

## Files touched

- `docs/dev/measurements/probe_b109_reseed_twin.py` (new)
- `docs/dev/measurements/2026-09-28-b109-reseed-twin-x86.txt` (new)
- `docs/dev/measurements/CLAUDE.md`
- `docs/dev/lanes/b109twin_report.md` (this file, new)
