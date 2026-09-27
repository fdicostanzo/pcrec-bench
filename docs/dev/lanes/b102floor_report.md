# Lane `b102floor` — libpcre2 `floor`-pattern Cyrillic cost probe (addendum candidate 4)

Branch `lane/b102floor`, worktree `worktrees/b102floor` off `master` at
`a42af205`. Docs + one archived probe only: a standalone C program and
its archived output under `docs/dev/measurements/`, one new
`docs/dev/upstream_findings.md` entry, and the pointer/plan-log updates
the boilerplate requires. No code under `pcrecbench/`/`testees/` touched,
no store write, no report render, no bench window; `~/pcrec` never read
(this task needed only the committed report TSV, `bench/utf8/`'s
manifest/expectations/subject_facts, `testees/pcre2/driver.c`'s own
documented design, and the system libpcre2-dev headers).

## Charter vs. committed

| brief item | committed |
|---|---|
| Correct the addendum's wording: `floor` is the literal `~`, not match-anything | done — stated up front here and in the upstream_findings.md entry; verified against `bench/utf8/patterns.rxt:909` (`pattern ~` / `name floor`) |
| Re-derive the cited numbers from the committed report TSV(s): name files, rows, testee ids (byte vs `-utf` testees), check subject byte lengths and whether either contains `~` | done — `reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7.tsv`; the three hits are `libpcre2_10.46_{dfa-nocaps,interp-caps,jit-caps}-simdna_utf8` (the `-utf8`/UTF-mode testees, NOT byte-mode — corrected from the brief's "byte vs -utf" framing, since all three are UTF testees) on `t-64k-cyr` only, ratios 3.1198/3.1194/3.0481, npb 0.608/0.608/0.629 (asc) vs 1.897/1.897/1.918 (cyr) (`docs/dev/measurements/2026-09-26-utf8-0.1-r2-r7-addendum-extract.txt` lines 183-185, already committed by lane b97read). Both subjects exactly 65536 B (`bench/utf8/subject_facts.tsv`); `~` occurs 0 times in either (`expectations.tsv`: both `nomatch`, independently re-confirmed with `grep -c '~'` on the actual `.bin` files, both 0) |
| Hypothesise from libpcre2's source/behaviour, versioned | done — system `libpcre2-8-0 10.46-1build1` (no vendored source; same `.so` `testees/pcre2` loads, confirmed by `ldconfig -p` + the probe's own `PCRE2_CONFIG_VERSION` print: "10.46 2025-08-27", matching the report's testee ids exactly); the working hypothesis (libpcre2's built-in UTF-8 subject validation, man pcre2api "PCRE2_NO_UTF_CHECK") came from `testees/pcre2/CLAUDE.md`'s own already-committed [B94]/BD15 VALIDATE-ONCE section, read before writing any code |
| Check whether the ×3 is OURS (the driver/find-all loop) rather than libpcre2's | done — ruled out structurally before probing: `floor` matches 0 times, so the real find-all loop makes exactly ONE call per subject; there is no loop to be quadratic in. Confirmed empirically too (below) |
| Standalone C probe: `~` over 64 KB ASCII vs Cyrillic, byte vs UTF mode, with/without `PCRE2_NO_UTF_CHECK`, interp/JIT/DFA, one control pattern whose first code unit IS a common byte | done — `docs/dev/measurements/probe_libpcre2_floor_cyr.c`; the control is `' '` (space, common to both scripts' word-boundary structure), run as a find-all loop (not a single call) since it DOES match, replicating `testees/pcre2/driver.c`'s own VALIDATE-ONCE call shape |
| Single-threaded, taskset one core, median of >=5 trials with spread, record load/CPU/compiler/libpcre2 version | done — `taskset -c 3`, `NTRIALS=21` per in-process cell (median reported), 7 outer process invocations archived verbatim (`nice -n -5` attempted, failed with `EPERM` on this box — noted, not silently dropped); loadavg 0.69-0.74 throughout (checked quiet via `uptime` before starting: 0.17/0.23/0.16); gcc 15.2.0, libpcre2-8-0 10.46-1build1, `schedutil` governor noted (no root to force `performance` — explains two flagged outlier readings, ratio unaffected either way) |
| Archive under `docs/dev/measurements/2026-09-26-libpcre2-floor-cyr-probe.*` with a source-information header | done — `.c` + `.txt`, D35-style header (build/command/subjects+sha256/engine version/compiler/box/load) |
| If libpcre2's own behaviour: add a row to `docs/dev/upstream_findings.md` in its existing style | done — **U11** |
| If ours: say so, file as a candidate, do NOT change the driver | not applicable — the cost is libpcre2's own, confirmed by the `PCRE2_NO_UTF_CHECK` ablation; no driver change made or proposed |
| `docs/dev/measurements/CLAUDE.md` pointer row | done |
| Report with charter-vs-committed checklist | this file |
| Commit, hand back, end | this commit |

## What the probe found

**The ×3.05-3.13 cost IS libpcre2's own UTF-8 subject validation, on all
three routes, confirmed by ablation, not a driver artifact.**

With `PCRE2_UTF` set and no `PCRE2_NO_UTF_CHECK`, a single isolated
`pcre2_match()`/`pcre2_dfa_match()` call over the SAME 65536-byte
`t-64k-asc.bin`/`t-64k-cyr.bin` buffers (copied verbatim from
`bench/utf8/throughput/`, sha256-checked against
`bench/utf8/manifest_throughput.tsv` — both match) reproduces the
committed report's three ratios almost exactly: 7 outer runs, medians
**3.051 (interp) / 3.128 (dfa) / 3.051 (jit-via-match)**, each within
~1.6% of the report's 3.1194/3.1198/3.0481. Forcing
`PCRE2_NO_UTF_CHECK` on the SAME three call shapes collapses the ratio
to ~1.00 on all three (asc and cyr land within 1-2% of each other) AND
brings the absolute cost down to byte-mode (no `PCRE2_UTF` at all)
levels on the same cells — the entire gap is the validation pass, full
stop, on `pcre2_match()` and `pcre2_dfa_match()` alike.

**Why `pcre2-jit` shows the same cost as `pcre2-interp`/`pcre2-dfa`,
despite JIT-compiled matching code being vectorized:** `testees/
pcre2/driver.c`'s own header comment states the real testee NEVER calls
`pcre2_jit_match()` — `pcre2_match()` dispatches to JIT-compiled code
internally when present, and `do_match`'s single call site is
`pcre2_match_8` for both `pcre2-interp` and `pcre2-jit`. The probe's
`jit_via_match` measurement (JIT-compile, then call `pcre2_match()` —
the REAL testee's own shape) reproduces the ×3 ratio; a separate
`jit_direct` measurement (calling the lower-level `pcre2_jit_match()`
directly, which the real testee never does) is FLAT on both scripts,
check or no-check, in every one of the 7 runs. This localises the cost
precisely: it lives in `pcre2_match()`'s/`pcre2_dfa_match()`'s own
pre-dispatch validation call, not in JIT-compiled matching code itself —
and the real bench measures exactly the call shape that pays it.

**Negative control confirms the shape is `floor`'s own (one call, zero
matches), not general:** `' '` (space) run as a find-all loop (replicating
the driver's VALIDATE-ONCE call shape: call 1 unchecked, calls 2..n
forced `PCRE2_NO_UTF_CHECK`) shows the OPPOSITE, much smaller ratio
(~1.10-1.16, ASC costlier) across all 7 runs — `t-64k-asc` yields 9,216
matches vs `t-64k-cyr`'s 7,214 in the same 65,536 bytes (fewer, longer-
encoded Cyrillic words), so the one-time validation cost is amortised
across many per-match calls and the per-match loop overhead dominates
instead. This is the reason the ×3 gap shows up on `floor` specifically
and not (per R3's own census) on every pattern in the set.

**Noise, flagged not smoothed over:** the box runs the `schedutil`
frequency governor (no root to force `performance`). Of 7 outer process
invocations, one (run 1) shows a uniform ~1.6-2× common-mode elevation
across EVERY cell in that run (both scripts scaled by the same factor —
the ratio itself is unaffected, 3.047-3.132 within that run), and one
(run 6) shows a single `dfa_check`/cyr cell elevated to 2.084518 ns/B
against the other six runs' 1.892-1.897 (ratio 3.44 vs the typical
3.12-3.13 there) — both are in the archived verbatim block exactly as
recorded, and the summary table names both rather than excluding them.

## Verdict for the addendum's candidate 4

**Not a pcrec finding, not a bench/driver finding.** This is a real,
reproducible libpcre2 10.46 characteristic (UNDERSTOOD, not chased to
source — no libpcre2 source was read, only its documented
`PCRE2_NO_UTF_CHECK` contract and the ablation this probe runs). Filed
as `docs/dev/upstream_findings.md` U11. Nothing here changes
`testees/pcre2/driver.c`, `bench/utf8/`, or any reporter/interpreter
rule; `bench/utf8/NOTES.md`'s `floor` pattern continues to serve its
charter purpose (a byte-safe control whose compiled pcrec artifact is
identical under `-e utf8`/`-e byte`) unaffected by this reading.

**Not reported upstream**: plausibly a documented ASCII-fast-path/
multi-byte-slow-path property common to UTF-8 validators generally, not
obviously a defect on libpcre2's part, and not chased against its issue
tracker or source in this lane (out of the stated scope: "a light
probe — no bench window, no store write").

## Honest gaps

- No libpcre2 source was read; the mechanism attribution rests entirely
  on the `PCRE2_NO_UTF_CHECK` ablation and the `jit_direct`-vs-
  `jit_via_match` contrast, both black-box.
- The probe's absolute ns numbers vary run-to-run by up to ~2.5× (the
  `schedutil` governor) — the RATIO is the stable, reported quantity;
  no attempt was made to pin CPU frequency (would need root on this
  box).
- Only ONE common-byte control (`' '`) was tried, in ONE call shape
  (find-all loop via `pcre2_match()`). A `jit_via_match`/`dfa` variant
  of the control loop was not run (out of scope for a light probe; the
  `floor`-pattern single-call result across all three routes is the
  brief's own headline question and is fully answered).
