# Lane b63window — [B63] pcrec re-measure wave 1 at 25b1984f (loglines + altwide)

Charter (team-lead brief, 2026-09-21): re-measure `bench/loglines@0.1`
and `bench/altwide@0.2` on pcrec's canonical roster (`pcrec-auto`,
`pcrec-nocaps`, `pcrec-vm`, `pcrec-vm-in`) at pin 25b1984f, the [B61]
staleness burn-down's first wave (these two sets' matrix columns carried
the hottest stale-pin findings). Predictions committed before each
window, grounded honestly against `store/index.tsv`'s own facts (not a
blanket "unchanged" claim); sequential windows via
`scripts/run_window.sh`; sidecars regenerated at each close.

## 0. A process note on this lane's own conduct

The manager's mid-lane message is correct and is recorded here rather
than smoothed over: the first poll after launching the loglines window
was a single `gnutimeout 590` call that the harness auto-promoted to a
tracked background task. That task DID complete and DID notify — but
between launch and the notification landing, no foreground activity
occurred, which is exactly the "notification dependency" the
boilerplate's foreground-polling rule exists to remove (a lost or
delayed notification would have stalled the lane with no fallback). From
the manager's message onward, every wait on a running window used
REPEATED FOREGROUND `gnutimeout` calls (100-115 s each, looped by hand,
this transcript's own turns) against the window log's own
`WINDOW_RUN_COMPLETE` line — the altwide window (over an hour) was
carried entirely this way, roughly two dozen sequential foreground polls.

## 1. Predictions (committed BEFORE each window)

`docs/dev/predictions/loglines-0.1-pin-25b1984f-confirm.tsv` (9 parents)
and `docs/dev/predictions/altwide-0.2-pin-25b1984f-confirm.tsv` (13
parents), commit `f4adf4a`, both authored against `store/index.tsv`'s
ACTUAL per-testee stale-pin facts rather than a blanket claim:

| set | testee | prior pin | gap | grounding shape |
|---|---|---|---|---|
| loglines | auto | d34c9131 | single-variable | [EMIT-VERB]/[B60]/[B62] |
| loglines | nocaps/vm/vm-in | 1989c62 | 5 pins (crosses [OPT-5] STEP 2) | honest null, stated as possibly-real |
| altwide | auto/vm | d34c9131 | single-variable | [EMIT-VERB]/[B60]/[B62] |
| altwide | nocaps/vm-in | 334fd10e | 1 pin (short of [FORM-CHAR] cls-fold) | honest null |

Both files also carry SAME-PIN structural clauses (nocaps vs auto,
vm-in vs vm, `compile:emit_bytes` ratio at 25b1984f only) meant to
sidestep the stale-baseline gap entirely, and altwide additionally
carries eight refusal-boundary `section=did_not_compile` set-eq clauses
read from `docs/dev/measurements/2026-09-06-altwide-size-census-
d34c9131.txt`.

Full detail and the `docs/dev/predictions/CLAUDE.md` index entry:
commit `f4adf4a`.

## 2. Windows

Both launched detached (`setsid scripts/run_window.sh & disown`),
`TESTEES="pcrec-auto pcrec-nocaps pcrec-vm pcrec-vm-in"`, `TRIALS=5`,
`STORE=store`, `PIN=11`, `CELL_CAP=5400`. Quiet gate verdict `quiet`
immediately before each launch (loglines: load1 0.03-0.04, max_busy_pct
≤2.2%; altwide: load1 0.13-0.18, max_busy_pct ≤3.01%).

### loglines@0.1

- LOG: `build/windows/window_loglines_20260921T041451Z.log`
- Window: 2026-09-21 00:14:51 → 00:49:28 EDT (~34m37s)
- `WINDOW_RUN_COMPLETE cells=4/4`, all attempt 1, rc=0
- store 190 → 194
- Per-cell `agreement` line: `agree` on all four (0 groups disagreeing)
- Commits: `f4adf4a` (predictions), `dbe7bbb` (store + sidecars),
  `dbe7bbb`… report group + `reports/CLAUDE.md` entry in a separate
  commit — see §4 below for the exact list.

### altwide@0.2

- LOG: `build/windows/window_altwide_20260921T053218Z.log`
- Window: 2026-09-21 01:32:18 → 02:37:59 EDT (~1h5m41s — auto's compile
  phase alone (wide/refusing patterns taking 10-30s each to fail or
  succeed, ×5 trials) accounted for most of the early time; vm/vm-in
  compiled far faster, matching the census's own sub-0.1s VM compile
  times)
- `WINDOW_RUN_COMPLETE cells=4/4`, all attempt 1, rc=0
- store 194 → 198
- Per-cell `agreement`: `agree` on all four (auto/nocaps: 0 of
  89/53 groups disagreeing; vm/vm-in: 0 of 65 groups, 4 rows unjudged
  of 1844 — within normal k=1.5 trial-agreement noise, no
  `inconclusive-spread`)

## 3. Results and predictions scored

### loglines@0.1 — verdict table

| pred | testee | quantity | verdict | note |
|---|---|---|---|---|
| P1 | auto | delta_verdict | refuted | strict eq-token, ×1.00-1.06 both ways — ordinary jitter |
| P2 | vm | delta_verdict | refuted | **real mover**: ×1.32-1.56 FASTER, not jitter |
| P3 | nocaps | delta_verdict | refuted | mixed ×1.00-1.32, includes the flat `floor` move |
| P4 | vm-in | delta_verdict | refuted | **real mover**: ×1.31-1.57 FASTER |
| P5.a/.b | nocaps vs auto, same-pin emit_bytes | eq 1 | refuted | ipv4/whole ×0.825, level-context/plain ×2.425 |
| P6.a/.b | vm-in vs vm, same-pin emit_bytes | eq 1 | refuted | ×1.13-1.16, not 1.00 |
| P7 | vm-in vs vm, same-pin time | between 0.85-1.20 | refuted | **selector bug**: bare testee glob matched the OLDER 1989c62 vm-in record, not 25b1984f's |

**Headline finding (R-DELTA-1, not absorbed)**: `pcrec-vm`/`pcrec-vm-in`
(the five-pin-stale pair, crossing `[OPT-5]` STEP 2) read a real,
substantial **×1.29-1.57 FASTER** on nearly every large-subject-
throughput and short-subject-search cell; `pcrec-auto`/`pcrec-nocaps`
(at or within one pin of the single-variable comparator) hold to
×1.00-1.08 as [EMIT-VERB] predicts. `floor` (the trivial baseline
pattern) reads **slower ×1.03-1.32 on ALL FOUR routes** — flat and
route-independent, read as measurement/box-state noise on a
near-zero-cost pattern rather than a route-specific regression, stated
plainly rather than explained away.

**Genuine, unpredicted finding on P5/P6**: `pcrec --no-captures` is NOT
a size-neutral flag on this capture-free corpus the way this lane
predicted — it moves `level-context`'s emit_bytes by ×2.425 (larger)
while shrinking `ipv4`'s whole-subject form by ×0.825, a real
per-pattern engine-selection effect, not the flat "nothing to strip"
null. `pcrec-vm-in` also carries genuinely more bytes than `pcrec-vm`
(×1.13-1.16) — plausibly the caller-provided buffer's own static sizing
reaching the emitted source.

### altwide@0.2 — verdict table

| pred | testee | quantity | verdict | note |
|---|---|---|---|---|
| P1 | auto | delta_verdict | refuted | ×1.00-1.01 both ways — ordinary jitter |
| P2 | vm | delta_verdict | refuted | ×1.01-1.14 — ordinary jitter (same-pin `dfa_table` change did not move time) |
| P3 | nocaps | delta_verdict | refuted | ×1.00-1.13 |
| P4 | vm-in | delta_verdict | refuted | ×1.00-1.10 |
| P5.a/.b | nocaps vs auto, same-pin emit_bytes | eq 1 | refuted | ×1.426 on w-256/srt-256 — same direction/magnitude as loglines' P5 |
| P6.a/.b | vm-in vs vm, same-pin emit_bytes | eq 1 | refuted | ×1.247 (w-256), ×1.951 (ci-256) |
| P8-P13 | refusal-boundary set-eq | section | **not-evaluable** | selector bug: `form=plain/whole-subject` matches nothing — `report.py`'s `did_not_compile` rows carry a BLANK `form` column (this project's own `plain`/`whole-subject` split for did-not-compile is the size-census PROBE SCRIPT's own column, not `report.py`'s) |

**THE HEADLINE FINDING OF THE WHOLE LANE, confirmed by direct TSV and
record inspection since the predictions mechanism could not score it**:
the DFA/auto route's compiled-size refusal boundary on `bench/altwide`
SHRANK DRAMATICALLY between d34c9131 and 25b1984f.
`pcrec_25b1984f_auto-caps-simdna`/`auto-nocaps-simdna` refuse only
**4 patterns** (`s-2048`, `s-4096`, `w-1024`, `w-2048`) where the exact
same roster refused **18** at d34c9131 (`ci-256`, `ci-512`, `cnt-64`,
`nar4-512`, `pfx3-512`, `sfx-512`, `sh1-512`, `srt-256`, `srt-512`,
`w-256`, `w-384`, `w-512`, `wb-256`, `wb-512` all now compile). Read
directly from the fresh record's own `engine_metadata`:

- `w-256` whole-subject: `emit_bytes` 1,033,795 B (d34c9131, refused,
  over the 1,000,000 B cap) → **706,900 B** (25b1984f, compiles,
  **-31.6%**).
- `ci-512`: plain form `emit_bytes` 976,275 B with `dfa_table: "mixed"`
  (compiles); whole-subject `emit_bytes` 686,048 B with
  `dfa_table: "indexed"` (compiles) — at d34c9131 BOTH forms refused
  (1,590,488 / 1,668,864 B, over cap).

The `dfa_table` stamp moving from `premultiplied` (still seen on
`w-256` here) to `mixed`/`indexed` on the larger tables is the
mechanism this points to: cf0962e3's own `[OPT-DIAL]`/K59 "premul
drop-ladder rung" (landed between d34c9131 and 25b1984f), which this
lane's `pcrec-auto` single-variable TIME comparator never crosses (its
own baseline IS d34c9131) but which the record's own `dfa_table`
stamp clearly does cross for SIZE — a real, substantial, GOOD-NEWS
rescue, stated here as a finding for pcrec to confirm, not asserted as
proven mechanism (this lane did not read pcrec's own source for K59).
**The VM route's refusal boundary is, by contrast, EXACTLY UNCHANGED**:
`pcrec_25b1984f_vm-caps-simdna`/`vm-in-caps-simdna` refuse the
identical 11-pattern set d34c9131/334fd10e already refused, name for
name.

This directly UPDATES the [B61] staleness caveat: the "wb/ci
refusal-boundary cells" it flagged as hot are not merely
stale-but-probably-similar — they moved for real, in the DFA route's
favor, and any full-roster matrix or ledger still reading the
d34c9131-era 18-pattern refusal set for `pcrec-auto`/`pcrec-nocaps` on
this set is now WRONG, not merely old.

## 4. Charter-vs-committed checklist

- [x] loglines@0.1 then altwide@0.2, pcrec canonical roster (auto,
      nocaps, vm, vm-in) — DELIVERED, both windows 4/4 cells attempt 1.
- [x] Predictions committed BEFORE each window, grounded per-testee
      against the real stale-pin facts (not a blanket claim) — DONE,
      commit `f4adf4a`.
- [x] Sequential windows via `scripts/run_window.sh`, quiet gate as-is,
      generators run first — DONE (generators re-run in this worktree
      at lane start; quiet gate `quiet` immediately before each launch).
- [x] Index, report group (this is a re-measure — cross-pin Δ against
      each testee's own newest prior record, per KB-5/`reports/CLAUDE.md`
      conventions) — DONE both sets: `2026-09-21-loglines-0.1-budu-
      ryzen1600-after-25b1984f.*`, `2026-09-21-altwide-0.2-budu-
      ryzen1600-after-25b1984f.*`.
- [x] Interpretation sidecar with `--predictions` — DONE, WITH A NAMED
      GAP: neither sidecar carries `--predictions` directly (the F27
      re-anchor refuses it, same documented gap as
      `capability-0.1-pin-25b1984f-confirm.tsv`); predictions scored via
      a direct `interpret.evaluate_predictions` call (same KB-24
      `_measured_text` workaround as that precedent), verdicts tabled in
      §3 above and in `reports/CLAUDE.md`'s own entries, not embedded in
      either sidecar file.
- [x] Sidecars regenerate at each close — DONE automatically by
      `run_window.sh` (21 then 22 sidecars re-stamped for the index
      bump, content unchanged but for the `index_sha256` line).
- [x] Lane report with per-cell outcomes, sentinel lines quoted,
      predictions scored, surprises stated prominently — THIS FILE.
- [x] Commit incrementally — 6 commits on `lane/b63window`: `f4adf4a`
      (predictions), `0472984` (loglines store+sidecars), `dbe7bbb`
      (loglines report group + reports/CLAUDE.md), `c02d41d` (altwide
      store+sidecars), `1863cc1` (altwide report group +
      reports/CLAUDE.md), plus this closing commit.
- [ ] Hand back complete; do not merge — hand-back message follows this
      report's commit. Not merged (per the boilerplate; the manager
      merges).

## 5. Owed / follow-ups (none blocking)

- The `form=` selector bug in the altwide refusal-boundary predictions
  (P8-P13) is a documented lesson, not a re-run — the next
  refusal-boundary predictions file for this set should select
  `section=did_not_compile` WITHOUT a `form=` key (or should confirm by
  a fresh `report.py` header/column read what key, if any, distinguishes
  a did-not-compile row's compile variant before assuming the size
  census probe script's own `plain`/`whole-subject` column applies).
- The K59/premul-drop-ladder rescue finding is stated as a hypothesis
  about MECHANISM (the `dfa_table` stamp's own value change is directly
  observed and certain; the attribution to cf0962e3's K59 specifically
  is this lane's own inference from the pin's own changelog text, not
  independently confirmed against pcrec's source). Worth an outbox item
  confirming/correcting the attribution and noting the bench-measured
  magnitude (-31.6% on the w-256 witness, up to -59% on ci-512's
  whole-subject form) — not sent by this lane (scope: measure and
  report, not draft outbox items unless asked).
- `bench/email@0.2`, `bench/bounded@0.3`, `bench/syntax@0.1` remain
  stale at pcrec pins per [B61] and are explicitly OUT of this wave's
  scope ("remaining sets ride later nights" — [B63]'s own charter text).
