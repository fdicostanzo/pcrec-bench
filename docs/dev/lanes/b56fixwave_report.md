# lane b56fixwave — the predicate-audit fix wave — report

Branch `lane/b56fixwave`, HEAD `622ee6eecb61b184082b1198cad8ed1941dba794`.
Nine commits (items 1-8 and 10; item 9 is a verification run only --
the brief explicitly forbids editing the predictions file or the
ledger, so it produced no diff). Working tree clean. Charter:
`docs/design/predicate_audit_v1.md` v1.1, plan row `[B56]`.

## Charter-vs-committed checklist

1. **§3.3 amendment (Q2 ruling).** DONE, commit `1cdbe82`. Rewrote
   `interpreter_v1.md` §3.3, `catalogue/rules.toml`'s header comment and
   `catalogue/CLAUDE.md`'s Versioning section identically: MAJOR = a
   fact/verdict moves on unchanged inputs; MINOR = additive. Field-text
   motion is an instance of MINOR, not its definition.
2. **F3 + F11 shared-code population fixes.** DONE, commit `b8ceff4`.
   `r_delta_4`'s coverage now reads a prediction clause's own selector
   glob against the firing cell (`_selector_covers_cell`), scoped to
   non-`compile:` quantities (found while wiring this in -- a
   compile-quantity clause with an unconstrained `regime_or_na`, e.g.
   syntax P13's `testee=*`, would otherwise "cover" every match-regime
   cell by accident, since a compile row carries no regime dimension at
   all; restricting to quantities outside `_COMPILE_METRIC` restored the
   `R-DELTA-4__uncovered-finding` fixture's expected firing).
   `r_bucket_span`'s partner search widens to `excluded` rows (which
   carry `form`, unlike `did_not_compile`); the `did_not_compile` half
   is NOT implemented, per r7pop-3's own "TBD at implementation" —
   `did_not_compile`'s `form` is unconditionally empty so it cannot join
   on the same key, and its own re-keyed join was never specified.
   `R-BUCKET-SPAN`'s `inputs` gains one `excluded` entry; no
   predicate/threshold_src text moved (it already described the
   corrected population).
3. **Q4's collapse + F13's companion check, together.** DONE, commit
   `93405bd`. `_keyed_values` collapses the six duplicate `rank` metric
   rows to ONE value per cell for `n_wrong`/`n_gave_up`/`pass_rate`/
   `status` before any reducer runs. `load_predictions` refuses the
   `median` reducer on a failure quantity at load time.
4. **Q1's did-not-fire REASON channel (F1/F2).** DONE, commit `b85ee9f`.
   A rule may return `(token, reason)`; `reason` must be one of the
   rule's own declared `no_fire_reasons` (optional field, §8(6)-reviewed
   like `no_fire`, added to `check_interpret.py`'s template-diff gate).
   `R-FLOOR-2` now distinguishes its three early-return causes;
   `R-DELTA-4`'s `input-absent` says plainly that coverage could not be
   evaluated.
5. **R-ARM-2 (F9).** DONE, commit `d6dfca0`. New rule, own
   control/sabotage fixture pair (`report_d` = the pin 35e1ab1 loglines
   first sample, a REAL witness, not synthetic).
6. **F27 (Q7 ruling).** DONE, commit `b8cfa74`. `check_stated_utc` takes
   a `report` argument and anchors to the OD-B15 dedup key
   (`(subbench, version, testee_id, machine_id)`) of the report's own
   included population; `_anchor_identity_lines` renders the anchor used
   unconditionally on every predictions-scoring run;
   `interpreter_v1.md` §6.5 revised with both residual halves stated
   (r7ver-7 gameability, r7pop-4 cross-testee). Fixture pair
   (`predictions-utc-before.tsv` / `-after.tsv`), checked directly in
   `check_interpret.py` section 1 on the inexpressible-quantities
   precedent (a load-time raise is not a firing `expect`/`expect_not`
   can assert on).
7. **Versions.** DONE, commit `b2924f7`. `catalogue_version` 2.0 → 3.0
   (header-comment-documented, citing the rulings by name);
   `INTERPRET_VERSION` v1 → v2, its first bump ever.
8. **Regen + gates.** DONE, commit `c558205`. `catalogue/
   refresh_golden.py` (4 files) and `scripts/regen_sidecars.py` (7
   sidecars, 0 failures) both re-run; `catalogue/fixtures/gen.py --check`
   clean (217 files, 67 fixtures); `make check-interpret` 150/150 (0
   failed) at the wave's start (`87882ba`, confirmed) → 155/155 (0
   failed) here.
9. **The acceptance witness.** VERIFIED, no commit (the brief forbids
   editing the predictions file or the ledger). See below.
10. **Docs.** DONE, commit `622ee6e`. `catalogue/CLAUDE.md`,
    `pcrecbench/CLAUDE.md`'s interpret row, `docs/design/
    predicate_audit_v1.md`'s new top-of-file status line + §6.05 marker,
    `docs/design/CLAUDE.md`'s mirrored summary. `docs/dev/known_issues.md`
    unchanged -- no KB row names a predicate-audit finding, so none
    closes.

**Not touched, on purpose:** `docs/dev/plan.md`'s `[B56]` STATE tag --
left for the manager to move to `completed` at merge/review, per this
project's usual lane/manager split; nothing under `bench/`, `schema/`,
`store/`, or pcrec.

## R-ARM-2: does it fire on the acceptance goldens?

r7ver-4 flagged this UNMEASURED. Answer: **yes, on Report B (bounded)
only.** Regenerated golden facts:

| golden | R-ARM-2 firing rows |
|---|---|
| email-specimen (A) | 0 |
| bounded (B) | 108 (= 9 firings × 12 slots) |
| syntax (C) | 0 |
| syntax + predictions | 0 |

The 9 firings are all `cls-upto-65535` (bounded's own headline 65535
NFA-cap refusal, [B11.4]'s reason for building the count ladder) across
its three regimes, `auto-caps-simdna` refused against `vm-caps-simdna`/
`vm-in-caps-simdna` ranked one config token (`mode`) apart. This is
exactly the shape the rule was built to catch.

## Item 3's identity check, on the real committed data

Against `reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.tsv`,
P5.a (`n_wrong eq 0`): 321 `rank` rows collapse to **66** values (63
zero, 3 at 10.000) -- matches the audit's hand-derivation exactly
(`_reduce`'s `identity` still refutes, 3/66 bad). P1.a-c's "over 18
value(s)" (3 cells × 6 rows) now reads "over 3 value(s)"; no verdict
moved (P1 stays confirmed, P5 stays refuted).

## Item 9: the acceptance witness, scored lines

    python3 -m pcrecbench interpret \
        reports/2026-09-19-capability-0.1-budu-ryzen1600-ext-second-cf0962e3.tsv \
        --index store/index.tsv \
        --predictions docs/dev/predictions/capability-0.1-ext-roster.tsv \
        --format md

Exit 0 (the check that previously refused this exact file, per
`docs/dev/wake.md`'s standing fact and the ledger's §4, now passes).
The anchor line:

> **Predictions anchor (§6.5, r7code-1).** ...
> - `capability@0.1`: anchor 2026-09-18T03:33:45Z, over 3 (testee_id,
>   machine_id) tuple(s) this report includes.

The scored line, reproducing the ledger's §5.4/§8 item 2 hand-derivation
by machine:

> - P2 (docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md
>   §5.4;§8 item 2) — **confirmed**: predicted P2.a: n_wrong eq 15; P2.b:
>   n_wrong eq 195; P2.c: n_wrong eq 5; P2.d: n_wrong eq 5; P2.e:
>   n_wrong eq 5; measured P2.a: worst high-byte-run/(set)/large-subject-
>   throughput/plain/tre_0.9.0_default-caps-simdna = 15.000 over 1
>   value(s); P2.b: worst high-byte-run/(set)/short-subject-search/
>   plain/tre_0.9.0_default-caps-simdna = 195.000 over 1 value(s); ...

matching the ledger's cited `n_wrong=15`/`n_wrong=195` exactly. P5 and
P8 also score `confirmed`; P6/P7 `not evaluable` (no matching row); P1/
P3/P4/P9 `partial` (one clause evaluable, one not, against this
three-engine roster) -- none of this was previously reachable at all
under the retired global anchor. Neither the predictions file nor the
ledger was edited.

## Final check-interpret count

`make check-interpret`: **155 passed, 0 FAILED** (was 150/150 at the
wave's start, `87882ba`, independently confirmed clean before touching
anything). `catalogue/acceptance_10.py`: **25/25** (was 24/25 mid-wave
until `acceptance_10.py`'s own hard-coded rule count was updated
alongside `check_interpret.py`'s, item 5). Section 6 (the template-diff
gate) is green on the final commit (it touches no `rules.toml` prose)
but correctly FAILED on the items-4/5/6 WIP commits that did touch
`template`/`no_fire`/`no_fire_reasons` -- expected per its own
docstring; **the reviewer's approval line is owed on the manager's
merge commit**, naming `R-FLOOR-2`, `R-DELTA-4` (the `no_fire_reasons`
additions, item 4) and `R-ARM-2` (item 5, its `template`/`no_fire`).

**Not run in this lane** (box note: pcrec's I-75 battery held the box;
nothing heavier than check-interpret): `make check-harness`,
`make check-report`, `make check-schema`'s real-store paths. None of
this wave's changes touch `pcrecbench/harness.py`, `report.py` or
`schema/`, so none of the three should move -- stated, not verified,
and owed to whoever next runs the full `make check` off the box's quiet
window.

## Where the audit note's own reasoning turned out to need a correction

The v1.1 audit note's F3 fix shape ("a firing cell is covered when some
clause's selector glob-matches its cell, evaluable or not") was
slightly underspecified: it does not name which QUANTITY CLASS is
eligible to cover a match-timing (`rank`) cell. Implemented literally,
a `compile:` quantity's clause with no `regime_or_na` constraint (real
committed example: syntax P13, `testee=*`) would "cover" every
match-regime finding by accident, since a compile-section row carries
no regime dimension to fail the glob match on. Scoped coverage to
quantities outside `_COMPILE_METRIC`, restoring the fixture's intended
behavior; documented in `interpret.py`'s own comment at the call site
and in commit `b85ee9f`'s message. Nothing else in the note's fix
shapes needed correction beyond what was already specified.
