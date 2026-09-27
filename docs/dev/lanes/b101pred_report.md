# lane b101pred report — predictions for [B101]'s owed noreqbyte-twin window

**Task**: write `docs/dev/predictions/capability-0.1-noreqbyte-twin-02902356.tsv`
— the machine-readable predictions for the coming [B101] timing window
(inbox I-111's OWED [OPT-REQBYTE] twin), stated BEFORE it runs. Docs
only; no runs, no builds, no store loads.

**Branch**: `b101pred` (worktree `worktrees/b101pred`), from `lane/b101repin`
(the re-pin lane, not master — carries the new pin, the
`pcrec-auto-noreqbyte` testee and catalogue 3.10). Commit `3df1788`.

## 0. What the file says

12 clause rows over 11 parents, one per I-111's own twelve landing-bar
cells (`capability@0.1` x `{pcrec_02902356_auto-caps-simdna,
pcrec_02902356_auto-caps-simdna_noreqbyte}` at pin `02902356`):

- **P1-P5, IMPROVE** (`op=lt hi=1`): the five cells I-111 names as
  unmoved or only mechanically moved since ce658cb7
  (`wild-secrets-username-password-pair`, `wild-logparse-winpath-grok`,
  `tag-depth3-bound`, `dup-param-detect`, `tag-pair-match`, all
  `/large-subject-throughput`). Predicts default (pre-check present)
  measurably faster than the twin (pre-check denied).
- **P6.a/.b (`floor-byte`/thr and /srch) and P10
  (`wild-validator-uuid-grok`/thr), DO-NOT-REGRESS on PROGRAM-IDENTICAL
  twins** (`op=between`, a symmetric band): `b101repin_report.md` §5
  marks these three cells `program_sha256`-equal between default and
  twin, so any observed |Δ| is same-pin measurement noise by
  construction — read as the window's own null-control sample, per the
  brief's own instruction.
- **P7-P9, DO-NOT-REGRESS on DIFFERING programs** (`op=lte`, one-sided,
  no lower bound — a faster twin is not a regression):
  `float-literal-bound`, `nested-comment-rec`, `wild-secrets-github-pat`
  (all `/thr`). P9's note carries the required caveat: its twin also
  moves S1's DFA prefilter (offset-set-bounded → run-pinned-bounded), so
  any measured Δ there is the pre-check AND the prefilter change
  together, never the pre-check alone.
- **P11, RECORD-ONLY / NON-DIRECTIONAL** (`quantity=median_ns;
  reducer=identity; op=present` on the twin's own row):
  `router-prefix-order`/thr. I-111's own text calls this cell "timed,
  attributed" to S1's prefilter move, never gives a direction — no
  `ratio_to`/`lt`/`lte` clause is written for it, since inventing a
  direction I-111 does not give is exactly what the brief said this
  file must not do.

## 1. The DO-NOT-REGRESS band: cited, not invented

Both numeric bands used (P6/P7/P8/P9/P10) are read directly from the
project's own null-band tooling and its most recent measurement, per the
brief's explicit instruction:

- `docs/design/null_band_v1.md` ([B79]) / `pcrecbench/nullband.py` define
  the band: per-stratum (regime, baseline scale), symmetric, half-width =
  the largest `|Δ%|` any program-identical cell of that stratum reached
  across a cross-pin pair, usable only at `n >= 10` (§3/§4 of the design
  note; `nullband.py`'s `N_MIN = 10`, `Stratum`, `d119_verdict`).
- The MOST RECENT measurement of that band for `capability@0.1` is the
  immediately-prior cross-pin pair, `6ef76820 -> ce658cb7`, printed in
  `reports/2026-09-25-capability-0.1-budu-ryzen1600-after-ce658cb7.md`'s
  own "Null-control band" section:

  | regime | baseline scale | n | band (±) | status |
  |---|---|---|---|---|
  | `large-subject-throughput` | `>=1us` | 150 | ±16.62% | ok |
  | `short-subject-search` | `100ns-1us` | 101 | ±12.72% | ok |

  (the other three printed strata — `large-subject-throughput/100ns-1us`
  at n=6, `large-subject-throughput/<100ns` at ±42.16%, and
  `short-subject-search/<100ns` empty — are not used: none of the twelve
  landing-bar cells falls in them, checked per cell below).
- Each cell's own stratum was read from `pcrec_ce658cb7_auto-caps-simdna`'s
  rank-row median in that same report: every named cell except
  `floor-byte`/srch (667.3 ns) falls in `>=1us`; `floor-byte`/srch alone
  is `100ns-1us`. (`wild-secrets-github-pat`/thr at 129,253.0 ns,
  `wild-validator-uuid-grok`/thr at 81,991.4 ns, `router-prefix-order`/thr
  at 718,170.1 ns and `float-literal-bound`/thr at 1,892,212.5 ns are all
  comfortably `>=1us`; the five IMPROVE cells and `nested-comment-rec`/thr
  sit around 23,100-23,185 ns, also `>=1us`.)
- **Honestly generalised, not silently reused**: this band's native
  population is cross-pin, same-testee, program-identical cells — ours is
  same-pin, cross-testee (default vs. twin). No same-pin cross-testee
  band has ever been computed by this project's tooling, so the cross-pin
  figure is used as the widest CITED (non-invented) floor available; every
  affected clause's note says this explicitly, including that a true
  same-window noise floor should be tighter, so a within-band P6/P10
  reading is a weak confirm, not a strong one.

This is the same posture the project's own `loglines-0.1-pin-25b1984f-confirm.tsv`
P7 clause already took for a different same-pin cross-testee pair
(vm-in vs vm): "a generous band (not tight to 1.0)... given [B62]'s own
O-38 witness measured real trial-to-trial spread." Ours differs by citing
a project-computed number (the null-band table) rather than an
unquantified "generous" adjective.

## 2. Testee ids: independently re-derived, not guessed

Per the brief's instruction, both ids were verified against
`schema/validate.py`'s `derive_testee_id` (the WHOLE-CONFIG rule:
`{engine}_{version}_{mode}-{caps}-{simd}`, then `_` + `config_extra` if
present) and `testees/pcrec/configs.toml`/`adapter.py`'s `DENY_FLAGS`
entry for `noreqbyte` (`configs.toml:578`, `adapter.py:2476`), not merely
copied from the re-pin report:

- default: `pcrec_02902356_auto-caps-simdna` (no `config_extra`)
- twin: `pcrec_02902356_auto-caps-simdna_noreqbyte` (`config_extra =
  "noreqbyte"`, appended with the leading underscore
  `derive_testee_id` adds — confirmed this is an UNDERSCORE join, not
  the hyphen `compose_config_extra` uses to join axis tokens WITHIN
  `config_extra`, by reading `schema/validate.py:177-185` directly)

Both agree exactly with `docs/dev/lanes/b101repin_report.md`'s own
values.

## 3. Validation

- `interpret.load_predictions(path)` called directly: **12/12 clause
  rows load, zero closed-set errors** (all `quantity`/`reducer`/`op`
  tokens are in the closed sets; every `compile:`-scope restriction is
  N/A since every clause uses `median_ns`, never a `compile:` quantity).
- `make check-interpret`: **174 passed, 36 FAILED** — identical to
  `docs/dev/lanes/b101repin_report.md`'s own count. Confirmed by direct
  comparison: every one of the 36 failures is a `[3]` sidecar-freshness
  failure on an `.interpretation.md` file, the pre-existing catalogue
  3.9→3.10 gap already OWED to the manager at merge (36 sidecars need
  regeneration once the catalogue bump lands) — not moved by this file
  (which does not touch `catalogue/rules.toml`).
- **NOT scorable via the normal CLI path, honestly**: `pcrecbench
  interpret --predictions ... <report>` takes a required positional
  `report` argument, and no `capability@0.1` record exists yet at pin
  `02902356` — there is no report to pass. Separately, even once one
  exists, `check_stated_utc`'s F27 re-anchor will refuse this file the
  same structural way already documented in this directory's own
  `CLAUDE.md` for `capability-0.1-first.tsv` /
  `capability-0.1-pin-25b1984f-confirm.tsv`: `capability@0.1` has been
  measured many times before (first ever: 2026-09-17T00:50:53Z), so any
  honestly-dated new file fails the anchor. Scoring this file will need
  the same bypass those files used (a direct
  `interpret.evaluate_predictions` call skipping only `check_stated_utc`)
  — noted in the file's own `docs/dev/predictions/CLAUDE.md` entry so the
  next reader does not rediscover this.
- `check_testee_globs` (Q6 (ii)) was DELIBERATELY not run pre-window,
  same precedent as the 25b1984f-confirm files: `capability@0.1` already
  has measured records at older pins, so the check is not vacuous, and an
  exact not-yet-measured-pin testee id would read as a false-positive
  authoring defect until the window writes the first `02902356` records
  — at which point it passes for the ordinary reason.

## 4. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 1 | write `docs/dev/predictions/capability-0.1-noreqbyte-twin-02902356.tsv` per `docs/dev/predictions/CLAUDE.md` / `interpreter_v1.md` §6 | DONE: 12 clause rows / 11 parents | commit `3df1788` |
| 2 | one clause per landing-bar cell | DONE | §0 above |
| 3 | IMPROVE: `default/twin < 1` | DONE: P1-P5, `op=lt hi=1` | file |
| 4 | DO-NOT-REGRESS: numeric band, derived from the project's own null-band tooling/ledgers, not invented | DONE: cited from `null_band_v1.md`/`nullband.py`'s own most recent capability@0.1 measurement (§1); every affected note names the exact source and the generalisation it makes | file, §1 |
| 5 | floor-byte(thr+srch) and uuid-grok stated as same-pin noise readings (ratio within the null band) | DONE: P6.a/.b, P10, `op=between` | file |
| 6 | github-pat and router-prefix-order: caveat / non-directional per I-111 | DONE: P9's note states the prefilter confound explicitly; P11 is record-only (`op=present`), no direction invented | file |
| 7 | validate the file loads; use catalogue checks that don't load the store | DONE: `interpret.load_predictions` direct call (12/12) + `make check-interpret` (174/36, unmoved) | §3 |
| 8 | if the file can't be load-checked until records exist, say so | DONE: stated explicitly (no report exists to pass to the CLI; `check_stated_utc` would refuse it regardless, same as documented precedent) | §3 |
| 9 | add the file's row to `docs/dev/predictions/CLAUDE.md` | DONE | commit `3df1788` |
| 10 | end with the charter-vs-committed checklist | DONE | this table |

Nothing OWED beyond the window itself and its post-hoc scoring (which
needs the `check_stated_utc` bypass, same as every other cross-testee/
cross-pin predictions file in this directory).
