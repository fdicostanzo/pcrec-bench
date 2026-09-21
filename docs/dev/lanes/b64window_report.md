# Lane b64window — [B64] pcrec re-measure wave 2 + full-roster matrix refresh

Charter (team-lead brief, 2026-09-21): plan row [B64] — the [B61]
staleness burn-down's wave 2 (email-specimen@0.2, syntax@0.1, bounded@0.3
on the canonical pcrec roster at 25b1984f, predictions before each
window, per-testee grounding per [B63]'s two authoring lessons), then
re-render the full-roster matrix groups so every set reads current-pin
pcrec + rust.

## 0. Process notes

- The BOILERPLATE'S single-`gnutimeout` trap fired once, early
  (email-specimen's first poll: a bare `gnutimeout 590` auto-promoted to
  a tracked background task). Caught immediately and switched to REPEATED
  FOREGROUND `gnutimeout` calls (100-115 s each) against each window
  log's own `WINDOW_RUN_COMPLETE` line for the remainder of the lane —
  roughly 60 such polls across the three windows (syntax alone,
  ~2h45m, was ~45 polls). One spurious task-completion notification
  arrived mid-poll (from that first auto-promoted task); its claim was
  NOT trusted — the log itself was re-checked directly (`grep -c
  WINDOW_RUN_COMPLETE`, returned 0) before continuing to poll, per the
  boilerplate's own "check the marker, not the notification" rule.
- Two multi-command chained report-render invocations also exceeded 120 s
  and auto-promoted (the syntax `--format md` render and one loglines
  five-command chain) — both CONFIRMED complete by checking the actual
  output FILES directly (existence, `wc -l`, `.err` file contents) rather
  than trusting the notification, which is a stronger check than the
  window-log marker pattern since the artifact itself is the ground
  truth. From the syntax report render onward, every render step that
  could plausibly exceed ~90 s (syntax's and bounded's report/subject-
  grain/interpret calls, both ~95-pattern/43-pattern corpora) was run
  DETACHED with an explicit completion-marker file
  (`echo "... DONE rc=$?" >> build/windows/<name>.marker`), foreground-
  polled the same way a window is — never a plain foreground command
  guessed to fit under 120 s.

## 1. Predictions (committed BEFORE each window)

`docs/dev/predictions/email-specimen-0.2-pin-25b1984f-confirm.tsv` (8
clause rows), `syntax-0.1-pin-25b1984f-confirm.tsv` (10 clause rows),
`bounded-0.3-pin-25b1984f-confirm.tsv` (10 clause rows) — commit
`78d5aa6`, all authored against `store/index.tsv`'s own per-testee facts,
applying BOTH of [B63]'s own authoring lessons explicitly: every
same-pin structural clause names a PIN-SPECIFIC testee id
(`pcrec_25b1984f_<mode>-caps-simdna`) on both sides of a `ratio_to`, never
a bare `pcrec_*_<mode>` glob (b63's own P7 finding: a bare glob can match
an OLDER pin's record of the same testee_id by accident); every
`section=did_not_compile` clause carries NO `form=` key (b63's own
altwide P8-P13 finding: a did-not-compile row's `form` column is
structurally blank).

| set | testee | prior pin | gap | grounding shape |
|---|---|---|---|---|
| email-specimen | auto | d34c9131 | single-variable | [EMIT-VERB]/[B60]/[B62] |
| email-specimen | nocaps/vm/vm-in | 1989c62 | six pins back | honest null |
| syntax | ALL FOUR | d34c9131 | single-variable | pin-uniform — the ONE set where this was already true |
| bounded | auto/vm/vm-in | d34c9131 | single-variable | [EMIT-VERB]/[B60]/[B62] |
| bounded | auto-nocaps | 288d505 | seven pins back — the widest gap in either wave | honest null |

`bounded`'s P6.a/.b are the team lead's own requested DIRECTION-ONLY
size-cap clauses: given [B63]'s O-40 finding (altwide's DFA refusal
boundary shrank dramatically, `dfa_table` moving `premultiplied` →
`mixed`/`indexed`), P6 predicts `cls-upto-4096`/`cls-upto-2048`'s
whole-subject forms (bounded's own largest `premultiplied`-table DFA
artifacts, 471,547 B / 240,122 B at d34c9131) SHRINK at 25b1984f
(`op=lt`, `hi=` the literal d34c9131 byte count) — stated explicitly as a
hypothesis this set's own table shape was never independently probed
for, not a certainty. P7.a/.b separately test the STRUCTURAL refusal
boundary (`cls-upto-65535`, the NFA-state cap — mechanically distinct
from P6's emitted-bytes cap).

## 2. Windows (Part A)

All three launched detached (`setsid scripts/run_window.sh & disown`),
`TESTEES="pcrec-auto pcrec-nocaps pcrec-vm pcrec-vm-in"`, `TRIALS=5`,
`STORE=store`, `PIN=11`, `CELL_CAP=5400`. Quiet gate verdict `quiet`
immediately before each launch.

### email-specimen@0.2

- LOG: `build/windows/window_email_20260921T065851Z.log`
- Window: 2026-09-21 02:58:51 → 03:22:48 EDT (~24m)
- `WINDOW_RUN_COMPLETE cells=4/4`, all attempt 1, rc=0, all `agree`
- store 198 → 202

### syntax@0.1

- LOG: `build/windows/window_syntax_20260921T072836Z.log`
- Window: 2026-09-21 03:29:06 → 06:13:50 EDT (~2h45m — 95 patterns × 4
  testees; `pcrec-auto`/`pcrec-nocaps`/`pcrec-vm`/`pcrec-vm-in` each took
  ~39-44 minutes)
- `WINDOW_RUN_COMPLETE cells=4/4`, all attempt 1, rc=0, all `agree`
- store 202 → 206

### bounded@0.3

- LOG: `build/windows/window_bounded_20260921T104216Z.log`
- Window: 2026-09-21 06:42:47 → 09:39:39 EDT (~2h57m — run in DAYLIGHT
  rather than overnight, per the lifted windows-at-night restriction
  [2026-09-04]: box confirmed `quiet` immediately before launch, and
  stayed `quiet`/near-1.0-load throughout, never re-checked mid-run and
  never a problem)
- `WINDOW_RUN_COMPLETE cells=4/4`, all attempt 1, rc=0, all `agree`
- store 206 → 210

**Box never went non-quiet and the morning arrival did not force a
drop** — the brief's own "may be dropped" escape hatch was not needed.

## 3. Results and predictions scored (Part A)

All three sets' predictions were scored via a direct
`interpret.evaluate_predictions`/`interpret.interpret(..., check_utc=False)`
call (the F27 `check_stated_utc` re-anchor refuses the normal CLI
`--predictions` path for any cross-pin `delta_verdict` clause, same
precedent as [B60]/[B63]), with the KB-24 `_measured_text` string-value
monkeypatch (delta_verdict/section values are strings, and the
unpatched formatter crashes on `abs()`/`:.3f`).

### email-specimen@0.2

| pred | testee | verdict | note |
|---|---|---|---|
| P1 | auto | refuted (mechanical) | real values ×1.00-1.04, unchanged/flat — the blank-old-row artifact, not a real mover |
| P2-P4 | nocaps/vm/vm-in | refuted (mechanical) | real values ×1.00-1.09 (floor outlier ×1.36-1.81) — email does NOT reproduce loglines' ×1.29-1.57 vm/vm-in win |
| P5.a/.b | vm-in vs vm, same-pin | **CONFIRMED both** | byte-identical (47,591 B / 58,762 B) — opposite of the stated expected-refute caveat |
| P6.a/.b | nocaps vs auto, direction-only | mixed | orig exactly equal (82,236=82,236) despite real captures; factored barely smaller (×0.9978) |

### syntax@0.1

| pred | testee | verdict | note |
|---|---|---|---|
| P1-P4 | all four, pin-uniform | refuted (mechanical) | same blank-old-row artifact |
| P5.a/.b | nocaps vs auto, captureless witnesses | **REFUTED FOR REAL** | `lit-cat` ×0.916, `anc-caret` ×0.629 — nocaps up to -37.1% smaller with NOTHING captured to strip |
| P6.a/.b | vm-in vs vm, captureless witnesses | **REFUTED FOR REAL** | `lit-cat` ×0.961, `anc-caret` ×0.975 — vm-in SMALLER (opposite direction from loglines' P6 and from this wave's own email P5) |
| P7.a/.b | refusal-set stability | **REFUTED — THE HEADLINE FINDING** | `unp-p-lc`/`unp-p-uc` (`\p{L}+`/`\P{L}+`) now COMPILE on all four routes (13 refused, was 15); confirmed independently by a direct TSV read |

### bounded@0.3

| pred | testee | verdict | note |
|---|---|---|---|
| P1-P4 | auto/vm/vm-in/nocaps | refuted (mechanical) | same blank-old-row artifact |
| P5.a/.b | same-pin structural | tool: partial (P5.a refuted, P5.b confirmed); direct record read: **BOTH confirmed** | `cls-upto-1024` byte-identical both directions (16,760/187,559 nocaps=auto; 18,379/18,490 vm-in=vm) — a possible `interpret.py` residual, not chased down |
| P6.a/.b | direction-only K59 size hypothesis | **REFUTED, WRONG DIRECTION** | `cls-upto-4096` whole-subject GREW +188 B (471,547→471,735); `cls-upto-2048` whole-subject GREW +188 B (240,122→240,310); `dfa_table` stays `premultiplied` on both — the K59 mechanism does NOT reach bounded's class-ladder tables |
| P7.a | auto refusal-set stability | **CONFIRMED** | `{cls-upto-65535}` unchanged, the NFA-state cap |
| P7.b | vm refusal-set empty | tool: not-evaluable (the same empty-target-set residual gap `capability-0.1-ext-roster.tsv`'s entry documents); direct read: **CONFIRMED** | vm compiles `cls-upto-65535` cleanly, resolving [B61]'s own open question (the cap is auto-route-only, not "both engines" as the abi-11-era prediction text said) |

**Headline finding of Part A**: pcrec gained Unicode-property-class
(`\p{L}`/`\P{L}`) compile support somewhere in the cd371441 → a770139e →
cf0962e3 → 25b1984f span — a genuinely new capability this wave's own
re-pin history never named, found only because `syntax@0.1`'s refusal
CENSUS is exhaustive enough to notice a set SHRINKING. Stated as a
finding for pcrec to confirm (an outbox candidate), not filed by this
lane (measure-and-report scope, per [B63]'s own precedent — Frank/the
manager's call whether to send it).

**Second finding of comparable weight**: the direction-only K59 size-cap
hypothesis the team lead explicitly asked to be tested came back
NEGATIVE and CLEAN — a real, small, flat +188 B growth on bounded's own
largest premultiplied DFA witnesses, `dfa_table` unmoved. The mechanism
that rescued altwide's compiled size by double-digit percentages simply
does not reach this set's own table shape. This is exactly the kind of
answer a direction-only clause is FOR (a testable claim that came back
false, informatively).

## 4. Part B — full-roster matrix refresh

All five sets (`email-specimen@0.2`, `loglines@0.1`, `bounded@0.3`,
`altwide@0.2`, `syntax@0.1`) re-rendered as NEW `fullroster-25b1984f`
groups, same seven-testee canonical-identity roster rule as [B61]
(`libpcre2-interp`, `libpcre2-jit`, `pcrec-auto`, `pcrec-auto-nocaps`,
`pcrec-vm`, `pcrec-vm-in`, `rust-default`; ablation testees excluded).
The [B61] `d34c9131`/mixed-pin groups stand as history, unchanged, per
this lane's own charter text. Every set's roster is now pin-uniform at
25b1984f for the FIRST TIME on four of the five sets (only `syntax@0.1`
was ever pin-uniform before, at d34c9131). Every sidecar is a fresh
file, determinism-checked (second independent render, byte-identical, on
all five).

**The matrix surface independently confirms Part A's two headline
findings a second way** (F26-immune columns, no ranking-group gap): on
`altwide@0.2`, `pcrec-auto`/`pcrec-auto-nocaps` each refuse exactly 4
patterns (`s-2048`, `s-4096`, `w-1024`, `w-2048`, down from 18 at
d34c9131) against `pcrec-vm`/`pcrec-vm-in`'s 11 (`ci-512`, `nar4-512`,
`s-2048`, `s-4096`, `sfx-512`, `sh1-512`, `srt-512`, `w-1024`, `w-2048`,
`w-512`, `wb-512`), `rust-default` refuses NOTHING; on `bounded@0.3`,
`pcrec-auto`/`pcrec-auto-nocaps` refuse only `{cls-upto-65535}`,
`pcrec-vm`/`pcrec-vm-in` refuse NOTHING, `rust-default` refuses
`{nest2-64, nest3-16}` (matching [B59]'s own `CompiledTooBig` finding).

`make check-interpret`: 178/178 (section 3 — sidecar freshness — covers
all ten new sidecars from this lane, plus the ~24 pre-existing ones
`run_window.sh`'s own `regen_sidecars.py` re-stamped for the index bump
across the three windows).

## 5. Charter-vs-committed checklist

- [x] Predictions committed BEFORE each window, per-testee grounding,
      both [B63] authoring lessons applied — DONE, commit `78d5aa6`.
- [x] Three windows, canonical roster ×4, in the stated order
      (email-specimen shortest, syntax, bounded last/longest) — DONE, all
      12/12 cells attempt 1, all `agree`. Box never went non-quiet; the
      "may be dropped" clause was not invoked.
- [x] Index, `after-25b1984f` report group per set, sidecar with
      determinism check, commit per set — DONE, three commits
      (`8568633`, `5aeb32d`, `3621717`).
- [x] Predictions scored — DONE (F27 bypass + KB-24 workaround, same
      precedent as [B60]/[B63]); both mechanical verdicts AND direct
      record reads reported where they diverged (bounded P5, the
      P7.b empty-set residual gap).
- [x] Part B: loglines/altwide fullroster-25b1984f groups re-rendered —
      DONE.
- [x] Part B extension: email-specimen/syntax/bounded fullroster groups
      ALSO re-rendered (Part A completed in full, so this was in scope
      per the brief's own conditional) — DONE, single commit `3876d61`.
- [x] One render at a time, single-format commands, `gnutimeout` each —
      MOSTLY held; TWO renders (syntax's initial chained md/tsv/matrix
      attempt, loglines' initial five-command chain) exceeded 120 s and
      auto-promoted to tracked background tasks before this lane
      corrected course to per-command `gnutimeout` calls and, for the
      two largest corpora, detached-with-marker rendering — named here
      rather than smoothed over, per §0.
- [x] Lane report with per-cell outcomes, sentinels quoted, predictions
      scored, surprises prominent — THIS FILE.
- [x] `make check-interpret` green post-delivery — 178/178.
- [ ] Hand back complete; do not merge — hand-back message follows this
      report's commit. Not merged (the manager merges).

## 6. Owed / follow-ups (none blocking)

- **pcrec outbox candidate, not filed by this lane**: the Unicode-
  property-class (`\p{L}`/`\P{L}`) compile-capability gain between
  d34c9131 and 25b1984f (syntax@0.1's `unp-p-lc`/`unp-p-uc`) is a
  genuinely new, unpredicted finding worth confirming with pcrec and
  attributing to a specific pin — this lane's scope was measure and
  report, not diagnose or send outbox items.
- **A possible new `interpret.py` residual**, alongside KB-24: bounded's
  P5 mechanical verdict (`partial`, P5.a refuted) disagrees with a direct
  record read (both P5.a/.b confirmed, byte-identical values). Not
  traced into the interpreter's selector/reducer machinery here — flagged
  for a follow-up read, same posture KB-24 itself took when first found.
- The K59/[OPT-4.1] premul-drop-ladder mechanism's REACH is now bounded
  by this wave's own negative result on `bench/bounded`: it helps
  `bench/altwide`'s wide-alternation DFA tables and does not touch
  `bench/bounded`'s count-ladder ones. Worth a note in whatever ledger
  next reads O-40, if one is written.

---
ATTRIBUTION ADDENDUM (2026-09-21, the manager, from pcrecdev1's live
reply to the O-41 message): the syntax@0.1 refusal shrink 15→13
(\p{L}+/\P{L}+ now compiling on all four routes) IS a documented pcrec
landing — [M5.0] stage 5, the uprops module (Unicode property classes,
PC-3 1,053 names swept against the live oracle), merged inside the
d34c9131..25b1984f span; pcrec plan_completed.md's [M5.0] row, their
2026-09-12 journal, and docs/pcre2_compliance.md carry it. This
report's "not named by any documented re-pin" was written from OUR
re-pin notes, which track abi/adapter deltas, not pcrec's full
milestone landings. No O-item; closed by attribution.
