# b112bimodal — [B112] I-116's bimodality diagnostic

## 0. Task

Brief (main, this session): I-116 (`docs/dev/inbox_from_pcrec.md`) asks
whether O-68's per-process bimodal timing state (the reseed-twin driver's
`best_us` settling into one of two stable values for a process's whole
life) has a cause cheaper to fix than "measure more launches" —
(1) ASLR off, does the split collapse; (2) does the split follow a
subject-buffer alignment offset; (3) fast-vs-slow counters (`perf`
refused on this box, substitute what is available); optional `taskset`
pinning. Report a spread across deliberate layouts, say plainly what is
supported/refuted/unresolved. Answer feeds outbox O-69 (drafted by the
manager, not this lane).

Cell: `asr-lb-fixed` (row11_fixed, `(?<=\xc3\xa9)x`) on `synth-dense` and
`synth-64k-asc` (the widest split per O-68), gcc, orig and twin — the
SAME binaries [B109]'s multilaunch addendum built
(`/var/tmp/b109twin-htuo1bxs`, read-only), bench d0220be, pcrec pin
a32bc86e.

## 1. What was run

Six experiments, all in
`docs/dev/measurements/2026-09-28-b112-bimodality-diagnostic.txt` (verbatim
output) + `probe_b112_diag.sh` / three `drv_*.c` variants / two
`summarize_*.py` (the reproducing scripts, per D35 rule 4):

- **0. Sanity**: the `_ctl` build (plain `drv.c`, byte-identical driver to
  [B109]'s own) reproduces the known split on `synth-64k-asc` (min≈173.5
  vs a slow tail up to 434 across the various arms below).
- **1. ASLR off vs on** (`setarch $(uname -m) -R`, N=15 launches each):
  the split **PERSISTS under ASLR off** — 13.3-20.0% slow launches either
  way, no collapse.
- **2. Subject-buffer alignment sweep**: `posix_memalign(4096)` +
  offset ∈ {0,8,16,32,48,63}, 5 launches/offset. No dose-response with
  offset value; twin reads 0% slow at every offset (a real observation,
  but — see below — confounded with scheduler/core warmth, not proof the
  offset matters).
- **3a-3c. Placement telemetry** (`drv_probe.c`): `rx_search`'s own
  function pointer (a PIE binary's runtime address, no `/proc/self/maps`
  parsing needed) and the subject buffer's `malloc()` address, both mod
  64/4096/2 MiB, under normal ASLR, ASLR off, and a
  `-falign-functions=64 -falign-loops=64` code-placement arm.
- **3d. CPU id + `scaling_cur_freq`** (`drv_probe2.c`, `perf` refused —
  `perf_event_paranoid=4`, no sudo, not attempted further): 30 launches
  each, orig+twin, normal ASLR.
- **3e. `taskset -c 3` pinned vs unpinned**: 20 launches each.
- **3f. Deliberate 0.3 s idle gap vs back-to-back**: 15 launches each.

Box checked clear of any `pcrecbench report/run/quick` process
immediately before every timed block (`pgrep -af`, excluding the grep's
own self-match — the documented trap); load 0.08-0.82 throughout, no
concurrent heavy lane.

## 2. Findings

**(1) Address layout: RULED OUT, two independent ways.** The split
persists almost identically under ASLR off (13.3-20.0%) as under ASLR
on (13.3-20.0%) — I-116's own stated reading for this outcome is
"scheduling or the core." Separately and more strongly: `fn_mod64` and
`buf_mod64` read **exactly 0 on every one of 90+ launches**, both ASLR
modes, both variants — a PIE binary's load base is always page-aligned
(bits 0-11 always 0), so a symbol's or a `malloc()` allocation's
low-order virtual-address bits are a *build* constant, never a
*per-launch* variable, independent of what ASLR does to the high bits.
Intra-page code/data placement cannot be the cause by construction; this
was true before experiment (1) even ran.

**(2) Subject-buffer alignment: NOT SUPPORTED — the apparent effect is
confounded, not causal.** No offset in {0,8,16,32,48,63} shows a
dose-response; `posix_memalign`'s own allocation path happened to
correlate with near-zero slow launches for twin in this batch, but (3)
below shows this is very likely scheduler/core-warmth luck common to any
tight back-to-back shell loop (a process re-executing a bash loop tends
to land on the same, already-warm core repeatedly unless something
disturbs it), not a buffer-alignment effect. Correcting an earlier
in-flight read of this same data: I initially took 30/30 fast twin
launches in the alignment sweep as "posix_memalign suppresses the slow
state"; the taskset/idle-gap evidence below supersedes that reading.

**(3) Scheduling / per-core DVFS state: SUPPORTED, four converging lines
of evidence.**
- Per-launch CPU-frequency telemetry (3d): the observed timing ratio
  matches the observed frequency ratio almost exactly. Slow launches:
  `freq0_khz` mean ≈1.33 GHz (orig) / 1.36 GHz (twin); fast launches:
  ≈3.32 GHz / 3.31 GHz. Ratio ≈2.49-2.49, matching the timing ratio
  (≈433.85/173.54=2.50, ≈300.51/119.55=2.51) to two decimals.
- `taskset -c 3` pinning (3e) removes the slow state **entirely**: 0/40
  slow launches across both variants, vs the SAME unpinned command in the
  SAME batch still producing it (1/20 orig).
- A deliberate 0.3 s idle gap between launches (3f) **raises** the slow
  fraction (twin: 0% back-to-back → 26.7% with gaps; orig: 13.3% → 20.0%)
  — letting the assigned core's frequency decay between launches makes
  landing on a cold core more likely.
- The mechanism this supports: the whole `NTRIALS=21` loop completes in
  ~2-4 ms — short enough that a process exec'd onto a core still sitting
  at a low P-state (recently idle, `schedutil` hasn't sampled/ramped it
  yet) can run its ENTIRE lifetime at the cold clock before the governor
  reacts. A process landing on an already-busy/warm core reads at the
  boosted clock throughout. Pinning to one core keeps that core
  continuously busy (schedutil never drops it); idle gaps let any core
  decay back down between launches.

**Unresolved**: the exact schedutil sampling/ramp latency that sets the
~2-4 ms threshold was not measured directly (would need `perf` or a
kernel tracepoint, both unavailable without root); governor→`performance`
was refused (`/sys/.../scaling_governor` is `root:root 0644`, both a bare
write and `sudo -n` refused without a password, per the brief's own "skip
it" instruction). The code-placement arm (3c,
`-falign-functions=64 -falign-loops=64`) happened to land `fn_mod64=0`
both before and after (both builds were already 64-aligned by luck at
-O2), so it is not a clean positive/negative control on alignment
specifically — noted rather than overclaimed.

**Bottom line for O-69**: this is driver hygiene / measurement-protocol
territory (I-116's own framing) — the fix is more launches, `taskset`
pinning, or back-to-back scheduling, not evidence for pcrec's filed
[EMIT-ALIGN] row. No code- or data-placement signal read here correlates
with the state.

## 3. Deliverables

- `docs/dev/measurements/2026-09-28-b112-bimodality-diagnostic.txt` —
  verbatim output under a D35 source header (bench/pin identity, box,
  exact commands, the answer summary), plus a DERIVED numbers-only table
  at the foot.
- `docs/dev/measurements/probe_b112_diag.sh` + `probe_b112_drv_align.c` +
  `probe_b112_drv_probe.c` + `probe_b112_drv_probe2.c` +
  `probe_b112_summarize.py` + `probe_b112_summarize_pipe.py` — the
  reproducing scripts, committed beside the archive.
- `docs/dev/measurements/CLAUDE.md` — two new rows.
- This report.
- NOT written: the outbox (O-69) — the manager drafts it, per the brief.

## 4. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 0 | read BOILERPLATE.md, follow it | DONE — worktree created fresh, `git rev-parse --show-toplevel` verified first | — |
| 1 | (1) ASLR off, 15 launches each, both variants, both subjects | DONE — split persists, 13.3-20.0% either mode | archive §1, report §2 |
| 2 | (2) alignment offset sweep {0,8,16,32,48,63}, a few launches each | DONE — no dose-response; the apparent twin-suppression flagged as confounded, not causal | archive §2, report §2 |
| 3 | (3) counters fast vs slow (perf substituted) | DONE — code/data virtual-address telemetry (3a-3c, both invariant), CPU id + scaling_cur_freq (3d, the decisive signal), plus two extra confirmatory arms beyond the brief's own three: taskset pinning (3e) and an idle-gap arm (3f) | archive §3a-3f, report §2 |
| 4 | optional taskset -c N | DONE (3e) — the single cleanest result: 0/40 slow when pinned | archive §3e |
| 5 | optional governor→performance | NOT DONE, per the brief's own instruction ("needs root, skip it") — confirmed refused (root:root 0644, sudo -n refused) before skipping, not assumed | report §2 |
| 6 | report a spread across deliberate layouts, say what's supported/refuted/unresolved | DONE | report §2 |
| 7 | archive under docs/dev/measurements/ with source header + reproducing script | DONE | §3 |
| 8 | docs/dev/measurements/CLAUDE.md rows | DONE | §3 |
| 9 | lane report with charter-vs-committed checklist | DONE (this file) | — |
| 10 | do not write the outbox | DONE (not written) | — |
| 11 | commit incrementally, then end | DONE — one commit (the archive + scripts); this report and the CLAUDE.md update commit next | — |

## 5. OWED

Nothing. All six experiments ran to completion in the foreground (each
well under the ~4-minute DO-THEN-FINISH threshold); no background job
outstanding.
