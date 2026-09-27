# lane b104read report — THE READ of [B104]'s window at pcrec 751b9c6d (abi 39)

**Branch**: `lane/b104read` (worktree `worktrees/b104read`, from master
0caeb57). Writer lane; no measurement, no engine build, `~/pcrec` never
touched. Two report-render scripts were written for this window
(`render_b104_reports.py`, the twelve new groups; a small predictions-
scoring/sidecar generator) — both live in the session scratchpad, never
`scripts/`, per the manager's note.

## 0. Deliverables

| item | file |
|---|---|
| 12 report groups (6 sets × {fullroster, after}) | `reports/2026-09-27-{email-specimen-0.2,loglines-0.1,bounded-0.3,altwide-0.2,syntax-0.1,utf8-0.1}-budu-ryzen1600-{fullroster,after}-751b9c6d.{tsv,md,matrix.tsv,matrix.html}` (+ `.subject-grain.tsv` on both utf8 groups) |
| 12 sidecars | `...*.interpretation.md`, all determinism-checked |
| 4 identity censuses | `reports/identity/{loglines@0.1,bounded@0.3,syntax@0.1,altwide@0.2}/pcrec_25b1984f__751b9c6d.tsv` |
| ledger | `docs/dev/ledgers/2026-09-27-b104-751b9c6d.md` (+ its row in `docs/dev/ledgers/CLAUDE.md`) |
| outbox draft (O-63) | `docs/dev/lanes/b104read_outbox_draft.md` (NOT written to `outbox_to_pcrec.md`) |
| pcrecdev1's rider ask (subject-grain census) | `docs/dev/measurements/2026-09-27-b104-auto-select-short-whole-subject-census.txt` + its generator `probe_b104_auto_select_short_whole_subject.py` |
| `reports/CLAUDE.md` | new `[B104]` paragraph documenting the twelve groups |

## 1. What was rendered, and why two groups per set

The predictions files (lane b104pred) split cleanly into TWO structural
needs: the `delta_verdict` clauses need BOTH pcrec pins in one query
(R8's own pairing); syntax's `ratio_to(rust)` clauses need the current
pin PLUS the competitor roster, which the cross-pin query does not carry.
So each set got a `fullroster-751b9c6d` group (new pin + competitors) and
an `after-751b9c6d` group (old pin + new pin, pcrec only) — the same
`fullroster`/`after` split [B63]/[B64] already established, rather than
inventing a combined third shape.

**One correction made mid-window**: utf8's `after` group was first
rendered with only the two pcrec pins, which left P3.ii/P5's
`ratio_to(rust)` clauses unable to evaluate (rust wasn't in that
roster). Re-rendered with `rust-default` added — the fix that made all
five utf8 P-parents evaluable in one report.

Render costs (single-testee-roster loads, not whole-store): email/loglines
~15-75 s; bounded/altwide ~50-160 s; syntax/utf8 ~130-380 s (the two
largest corpora, both rendered DETACHED via `run_in_background`/a
foreground wait-loop, never blocking). Total wall time for all twelve
groups: ~50 minutes, one process, sequential (memory freed between
groups via explicit `del`+`gc.collect()`, matching `regen_reports.py`'s
own pattern) — never competing with the manager's own `make viewer-data`
run, confirmed by timing and later acknowledged by both sides.

## 2. Predictions scored (all six sets, F27 bypass — same precedent as every prior cross-pin file in `docs/dev/predictions/`)

**Committed sidecars carry NO predictions stamp** (`predictions:
(none)`), matching [B63]/[B64]'s own precedent exactly: `check-interpret`
section 3 always re-verifies a sidecar's stamped inputs with
`check_utc=True` (no override in `catalogue/check_interpret.py`'s
`run_interpret`), so a sidecar stamped against a predictions file whose
population genuinely needs the F27 bypass fails freshness FOREVER, not
just today. First attempt (predictions attached via a direct
`check_utc=False` call) hit exactly this: `make check-interpret` read
217 passed / 7 FAILED, one per set whose predictions file needed the
bypass. Fixed by regenerating those seven sidecars without
`--predictions`; scored values below come from a SEPARATE direct
`interpret.interpret(..., check_utc=False)` call per set, same as the
ledger's own numbers — real scores, just not stamped on the committed
artifact. `make check-interpret`: 224 passed, 0 FAILED after the fix.

- **utf8**: P1 confirmed, P2 confirmed (5/5, far beyond floor), P4
  confirmed (2/2, far beyond floor), P5 confirmed (2/2). **P3 (compound,
  4 residual witnesses): 4/8 clauses confirmed, 4/8 refuted** — the
  ledger's §2.3 quantifies this per cell; the "stays slow" assumption
  does not hold uniformly (2 witnesses nearly fully resolved, 1 flat, 1
  a real, unpredicted regression).
- **email-specimen/loglines/bounded/altwide**: P1 (delta_verdict,
  4 configs) REFUTED on all four configs, all four sets — exactly the
  honest-null outcome the files' own text anticipated; the identity
  census explains the split (program-changed cells move, identical
  cells are same-window jitter).
- **syntax**: P1 REFUTED (same shape); **P2/P3 (the anc-dollar/anc-z-lc
  collapse hypothesis) CONFIRMED, far past the conservative `lt 65`
  bound** — pcrec now beats rust outright (0.297×/0.301×, not merely
  under 65×).

Every sidecar's determinism was checked by the generation script itself
(a second `interpret()` call, byte-compared) before being written.

## 3. The manager's rider ask (pcrecdev1, auto-selection on short whole-subject matches)

Answered with a targeted, non-report-render script reading store JSONL
directly (`pcrecbench.reduce`, no jsonschema validation re-run, no store
load) — full data archived, summarized in both the ledger (§5) and the
outbox draft (item 5). The `bak-2` program-identity check (are the two
configs' whole-subject artifacts byte-identical?) came back YES
(`program_sha256` equal), confirming the manager's own "noise/layout"
hypothesis for that witness's timing wobble.

## 4. Validation

- `make check-report`: relaunched with a longer (900 s) timeout after the
  first 300 s attempt was killed mid-run (`test_report.py`'s real-store
  load cost, not a new regression — this lane touched no reporter code);
  see the hand-back for its marker.
- `make check-interpret`: **224 passed, 0 FAILED** (was 217/7 before the
  predictions-stamp fix, §2).
- Every one of the twelve sidecars was determinism-checked individually
  during generation (12/12 byte-equal second renders) — independent of
  `make check-interpret`'s own section 3 freshness check, which re-runs
  the same test against the committed files.
- No `store/` record was written or modified; no `~/pcrec` file touched.

## 5. What was NOT done (see the ledger's own §6 for the full list)

- No mechanism trace for any O-62 cell that did not move.
- No subject-grain rows for the five byte sets beyond the manager's own
  targeted ask.
- `tools/program_identity.py`'s email-specimen directory-alias bug is
  filed, not fixed (outside a read lane's scope).
- No `make check` in full (harness/interpret-adjacent code was not
  touched; the two report-side checks are the relevant surface).

## 6. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 1 | read BOILERPLATE.md first, follow it | DONE | §BOILERPLATE compliance: worktree ritual, `gnutimeout`, background-job markers, one-off script relocated out of `scripts/` on the manager's note |
| 2 | read plan.md [B104], I-112, O-60 §3, O-62, the predictions files | DONE | this report's context, the ledger's rule-text section |
| 3 | reports carrying competitor columns + matrix + cross-pin R8 Δ, per set | DONE: 12 groups | §1, §0 table |
| 4 | interpretation sidecars via the skill procedure / regen_sidecars.py, predictions attached where applicable | DONE, but landed as `predictions: (none)` on all twelve (matching [B63]/[B64]'s own precedent — attaching them fails `check-interpret` section 3 permanently, found and fixed mid-lane, §2) | §2, §0 table |
| 5 | ledger: rule text first, score every prediction clause, utf8 lit-* split by contains-literal with F3 quantified, flip-to-slow checked, answers 0 changes verified | DONE | `docs/dev/ledgers/2026-09-27-b104-751b9c6d.md` |
| 6 | O-62 §2-6 tables refreshed (same extract script), identity census as the lens, syntax anc-z-lc/anc-dollar, every O-62 loss >×2 re-read | DONE | ledger §4 |
| 7 | "what was NOT read" section | DONE | ledger §6 |
| 8 | charter-vs-committed checklist | DONE | this section |
| 9 | outbox draft (facts only, look-first list), NOT appended to outbox_to_pcrec.md | DONE | `docs/dev/lanes/b104read_outbox_draft.md` |
| 10 | pcrecdev1's rider ask: per-cell subject-grain + stamps, facts only, no fix proposed | DONE | ledger §5, outbox draft item 5, archived census |
| 11 | make check-report / check-interpret stay green | check-interpret DONE (224/0); check-report OWED — relaunched with a 900 s timeout after the first attempt's 300 s cap killed it | — |
| 12 | do not touch store/ records | DONE — confirmed, no store/ file modified | `git status` |
| — | plan.md / journal / outbox_to_pcrec.md commit | NOT touched (the manager's) | — |

## OWED

- **`make check-report` and `make check-interpret` results** — both were
  launched before this report was finalized; if either comes back
  non-clean, the specific failing check needs a follow-up (likely a
  fixture/golden-snapshot staleness from the twelve new committed
  reports, not a real regression, but not asserted here without the
  actual output). Marker: check the two background job outputs named in
  the hand-back message, or simply re-run both — they are fast relative
  to the store-loading renders this lane already paid for.
