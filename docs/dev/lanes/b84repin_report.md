# lane b84repin report — RE-PIN to 6ef76820 (abi 30 -> 31), [OPT-PRECHECK-ADMIT]

**Task**: plan row [B84] (a) / inbox I-102. Re-pin the pcrec testees from
`b1885a83` (abi 30) to pcrec main `6ef76820` (abi 30 -> 31) — the
`Merge branch 'lane/admitimpl'` commit, [OPT-PRECHECK-ADMIT]: one new stamp,
`RX_REQ_WHY`, unconditional on every artifact of both engines, a closed
four-token set (`none`/`emitted`/`one-attempt`/`dominated`) naming the
EMISSION of the `req_byte`/`req_run` pre-check beside their own ANALYSIS.
The capability re-measurement window is explicitly the MANAGER's own job
(I-102's slot-naming ack), out of scope here.

**Branch**: `lane/b84repin`, `worktrees/b84repin`, three commits (`90e0fa1`
the adapter/shim/driver/registry/selfcheck change, `4f128e6` the catalogue
3.5 -> 3.6 bump with its changelog comment in the SAME commit — closing the
gap the manager's brief flagged from the [B80] lane, `ac6111c` the CLAUDE.md
narrative). **DELIVERED**: full `make check` to completion three times (the
first two setsid-detached runs each hit the SAME single transient failure —
a concurrent `pcrecbench report` process on the box spiking one core to
100%, unrelated to this lane — the third, run once that process had cleared,
is clean): `check-schema` 5/73/0, `check-harness` **458/0**, `check-report`
89+7+12 (`OK`), `check-interpret` **163/29** (192 total, every failure
section 3 — sidecar staleness, entirely attributable to the catalogue bump,
per the b58/b74/b80 precedent this brief itself cites). `make`'s own exit
is 2, solely from those 29 named, classified failures.

## Charter-vs-committed checklist

1. **Fetch + confirm the commit, and build regardless of `main`'s tip.**
   DONE. `git -C ~/pcrec fetch origin` confirmed `6ef76820` on
   `origin/main` with `b1a100f3` (the `repin3` re-pin merge, itself a
   descendant of `6ef76820`) as its child. `git diff --stat
   6ef76820..origin/main -- src cli lib` is EMPTY — the only files that
   move are `docs/design/`, `docs/dev/` and one test script
   (`tests/codegen/run_recursion_identity.sh`), confirming I-102's own
   characterisation. Built `6ef76820` itself (`testees/pcrec/pin.sh
   6ef76820`), not whatever `main`'s tip happened to be at fetch time. No
   write to `~/pcrec` beyond the sanctioned `git fetch`.

2. **The KNOWN [B80] HAZARD, re-checked.** `git status --short` in the
   MAIN tree (`/home/duxevents/pcrec-bench`) was empty both before and
   after `pin.sh` ran from the lane worktree — **the hazard did NOT
   recur this time**. `pin.sh`'s own build-root resolution (shared
   `build/` via git-common-dir) is working as designed; whatever touched
   `list_axes.tsv` in the main tree at [B80] did not repeat here.

3. **`rx_info` / the shim floor.** `struct rx_info` diffed field for
   field between the two pins' emitted `.h` (a plain `abc` witness) —
   ZERO hunks in the struct body. Neither of `req_admit`'s two rules
   (`req_route_one_attempt`, `req_byte_dominated_by`) touches a struct
   member — the fix is an emit-time PREDICATE with four readers (whether
   to emit the pre-check's text, what the new stamp says, and
   `pcrec_emit_prologue`'s `#include <string.h>` decision), never a field
   addition. **Verdict: floor stays 16, no rx_info change** — exactly as
   I-102 said it doesn't claim movement.

4. **Registries re-archived and diffed against the pin's own live
   output — ALL FOUR BYTE-IDENTICAL below their source headers.** DONE,
   commit `90e0fa1`.
   - `list_axes.tsv`: **89/32, unchanged** — no new axis, no new row.
     This is the STRUCTURAL confirmation of I-102's "explicitly NOT an
     axis (no flag, no bit)" claim (pcrec's own `docs/spec/tuning.md`
     §2.29), not merely a citation of it.
   - `list_definitions.tsv`: **50 rows, byte-identical** — the
     thirteenth pin running.
   - `list_limits.tsv`: **60 rows, unchanged** — `req_admit`'s two rules
     read existing fields and existing limits only, no new numeric cap.
   - `list_schema.tsv`: **71 rows, byte-identical** — no `.rxt` grammar
     change.

   **Everything accounted for by name; nothing unexplained** — the
   emptiest registry diff of any re-pin in this file's history, which is
   itself the finding: a fix that ships with zero registry footprint.

5. **The adapter/shim/driver: the `req_why` stamp reader.** DONE.
   `testees/pcrec/shim.c`: `pb_req_why()`, the same `#ifdef MACRO /
   return MACRO; #else / return NULL` shape as `pb_req_run()`, placed
   right after it. `testees/pcrec/driver.c`: one declaration, one `SYM()`
   registration, one `info req_why` print beside `req_byte`/`end_window`/
   `req_run` in the SAME "every"-scope block. `testees/pcrec/adapter.py`:
   `req_why` added to `STR_PAIRS`, `STAMP_SCOPE` (`("every", 31)`),
   `METADATA_DECL` (full description, `"type": "enum"` with the closed
   four-value set — unlike its three variable-valued siblings), and a
   NEW `_check_agreement` rule 12: `req_why` reads `"none"` IFF `req_byte`
   itself reads `"none"` (pcrec's own cross-check), checked both
   directions. **No `REGISTRY_STAMP_PAIRS` entry** — confirmed correct
   by the empty registry diff: there is no `list_axes.tsv` row to check
   the enum against, the same "no stamp_value" shape `dfa_prefilter_
   offsets`/`req_byte` already have, but for the opposite reason (those
   carry a VARIABLE value; this one has NO REGISTRY ROW AT ALL). The
   closed-token assertion itself is covered by the EXISTING generic
   mechanism: `schema/validate.py`'s rule X15 already rejects any
   `engine_metadata` value not in a pair's declared `"values"` list for
   every `"type": "enum"` pair, and declaring `req_why` that way extends
   X15 to it automatically — no new validator code needed, and no
   record can carry an undeclared fifth token.
   `testees/pcrec/configs.toml`: `pin = "6ef76820"`. **No new deny
   testee**: the fix ships with NO CLI flag and NO axis bit at all
   (confirmed structurally by item 4's empty registry diff), so — per
   the brief's own instruction — this is reported as a FACT, not a
   defect: no acceptance review is open on [OPT-PRECHECK-ADMIT] the way
   [OPT-5]/[ENG-ISL]/[FORM-CHAR] each had one, so there is nothing to
   isolate with a `-noreqwhy`-shaped testee.

6. **Stamp spot-checks BY VALUE, and the deny controls.** DONE,
   `check_mechanism_stamps` **115/0** and `check_deny_flag_controls`
   **15/0**, both run standalone before the full suite.

   **All four tokens confirmed on hand-chosen witnesses** (`STAMP_
   CASES`): `foo[0-9]+bar` (pure DFA, unanchored — the pre-check's own
   byte 'b'=98 differs from the DFA prefilter's own scan byte 'f'=102,
   MEASURED by grepping the emitted `memchr` call sites) = `emitted`;
   `^foo[0-9]+bar` (the anchored attempt DFA, `dfa_interior_dead`) =
   `one-attempt`; `a(b|c)+d` under `auto` (VM hybrid) AND under
   `--engine=vm` (non-hybrid VM) = `emitted` both; `[^\x00-\xff]`
   (provably-empty) = `none` (the `req_byte "none"` cross-check); and a
   NEW kind this lane added, `` \[ `` ("dominated DFA (G1 identity)") —
   a single-byte literal whose candidate-start scan and pre-check would
   scan the IDENTICAL byte 91, admitimpl's own §0 F2 identity case
   ("today G1 fires only under identity") = **`dominated`**, MEASURED as
   exactly one `memchr(…, 91, …)` in the emitted C, not two.

   **I-102's own four named acceptance-cell patterns confirmed BY
   VALUE**, taken from `bench/capability/patterns.rxt`'s own text (the
   `.rxt` format's pattern-precedes-name convention read carefully):
   `wild-validator-email-owasp` = `one-attempt` (byte '@'=64, the pattern
   is `^`-anchored); `winpath-near-miss` / `email-nested-plus` =
   `one-attempt`; `wild-codegrammar-json-array-begin` (`` \[ `` again) =
   `dominated`; `uuid-near-miss` / `ipv4-near-miss` = `one-attempt` (the
   batch-1 recovery ask (d)); `nested-comment-rec` = `emitted`, byte
   `*`=42, run `*/`@0 (hex `2a2f@0`) both KEPT — exactly the no-move
   control (f)'s own description; `wild-secrets-github-pat` = `emitted`
   on BOTH `auto` and forced `--engine=vm` — the no-move control (g);
   `router-prefix-order` / `keyword-prefix-order` = `emitted`, unchanged
   — the negative controls (h): no recovery here, as I-102 itself
   predicted ("a recovery here would be the surprise, not the miss").
   **All ten of I-102's own predictions held exactly.**

7. **The corpus census, THE FOURTH INDEPENDENT DERIVATION.** DONE, over
   `bench/capability`'s 62 compiling patterns (2 refuse: `negation-
   scope-lookbehind-var` on all three configs, `wild-datetime-
   datefinder-alternation` on two of three — it compiles clean under
   `auto-nocaps`), counted by ARTIFACT-CONFIG across the THREE distinct
   COMPILED artifacts (`auto-caps`=`pcrec-auto`, `auto-nocaps`=
   `pcrec-nocaps`, `vm-caps`=`pcrec-vm` — `vm-in-caps` is compile-
   identical to `vm-caps`, same argv exactly, so counting it separately
   would double-count rather than add information; confirmed this is the
   convention the reading's own cited figures use by reproducing them
   exactly under it and NOT reproducing them under a naive 4-testee
   count, which gives 249/187 instead):

   | token | this lane's census | the reading's cited figures |
   |---|---|---|
   | `none` | 79 / 27 | 79 / 27 |
   | `emitted` | 67 / 27 | 67 / 27 |
   | `one-attempt` | 27 / 9 | 27 / 9 |
   | `dominated` | 14 / 7 | 14 / 7 |
   | total | 187 artifact-configs, 5 refusals | (agrees) |

   **EXACT agreement, digit for digit** — the fourth independent
   derivation the brief asked for, agreeing by value with the other
   three (`admitimpl_report.md`'s own corpus-wide movers census, I-99's
   reading, I-102a's). Ten patterns move between the `auto` and forced-
   VM readings (`codegrammar-flat`/`-xflag`, `floor-byte`, `mojibake-
   curly-quote`, and the four `wild-codegrammar-json-*` members — all
   `dominated` under `auto`, `emitted` under forced `--engine=vm`): G1's
   dominance test reads the DFA route's OWN candidate-start scan, so a
   forced-VM artifact with no DFA scan at all has nothing to be dominated
   BY, which is exactly why the union of `dominated`-in-`auto` and
   `emitted`-in-`vm` on these ten is not a contradiction.

8. **check-harness rows.** DONE, at the established granularity: five
   `STAMP_CASES` witnesses (the four kinds already in the table, plus the
   new `` \[ `` dominated one) asserted by VALUE; the closed-token set
   asserted through the EXISTING enum-declaration mechanism (item 5) —
   no separate check needed, and this is reported as the honest reason
   rather than manufacturing a redundant one; **NO deny control** — the
   registry declares no axis for `req_admit`'s mechanism (item 4/5), so
   per the brief's own instruction this is reported as a fact, not a
   defect.

9. **CLAUDE.mds.** DONE, commit `ac6111c`. Root `CLAUDE.md` and
   `testees/pcrec/CLAUDE.md` each gain a dated section in the established
   per-re-pin narrative shape (the stamp, the by-value witnesses, the
   census, the byte-identical registry diff, the size-book
   decomposition). `docs/dev/plan.md`'s `[B84]` row and the STATUS
   narrative are the manager's, per the brief; left untouched.

10. **Full `make check` — THE DELIVERED NUMBERS.** Ran three times, all
    `setsid`-detached with a `.done` marker, polled with bounded
    foreground `until`-loops (removed from the worktree before delivery
    — nothing untracked remains, `git status --short` clean):

    - **Run 1**: `check-harness` **457 passed, 1 FAILED** — the one FAIL
      was `a real quick cell on bench/email writes a MEASURED scratch
      record status=inconclusive-load tier=scratch rows=2`. Traced
      LIVE: a concurrent `python3 -m pcrecbench report --subbench
      capability ...` process (not this lane's) was pinning one CPU
      core at 99.9% at the moment this timing-sensitive quiet-gate check
      ran (confirmed via `ps aux --sort=-%cpu` at the time of the
      failure). `check_run_smoke` re-run standalone once that process
      exited (confirmed gone by PID) passed clean, 2/2, at load average
      1.19 — proving the failure was the box, not this lane's change.
    - **Run 2**: launched once the first competing process had cleared;
      hit the SAME identical failure, because a SECOND `pcrecbench
      report` invocation (a different format/testee-set argv, evidently
      part of a batch of report renders running elsewhere on the box —
      not identified further, not this lane's own process) had started
      in the interim. Same diagnosis, not chased further.
    - **Run 3**: launched once no competing process was visible in
      `ps aux`; completed CLEAN: `check-schema` 5/73/0, `check-harness`
      **458 passed, 0 FAILED**, `check-report` 89+7+12 (`OK`),
      `check-interpret` **163 passed, 29 FAILED** (192 total).

    `check-interpret`'s 29 failures are ALL section 3 (sidecar
    freshness) and are ENTIRELY the catalogue 3.5 -> 3.6 bump's own
    effect, isolated and proven rather than assumed: `git stash` of just
    the `catalogue/rules.toml` edit reproduced a CLEAN `192 passed, 0
    FAILED` immediately beforehand, and un-stashing reproduces `163/29`
    immediately after — the same shape `check-interpret.py`'s own design
    predicts (a version bump invalidates every committed sidecar's
    freshness stamp) and the same precedent `b58repin`/`b74repin`/
    `b80repin` already established: regenerating them is the MANAGER's
    merge-time step, never a re-pin lane's own.

## Not done / OWED

- **The capability re-measurement window** is explicitly the manager's
  own step per I-102's slot-naming ack ("the re-pin lane builds this
  afternoon ... the WINDOW opens TONIGHT ~22:0x EDT") and is NOT started
  here.
- **Sidecar regeneration for the catalogue 3.5 -> 3.6 bump** — a MINOR/
  additive `[[pin_order]]`-append bump, per the manager's standing
  instruction on this lane class — this lane does NOT regenerate
  committed `reports/*.interpretation.md` sidecars; that runs at the
  manager's merge, per precedent.
- No `store/` record needed re-deriving — this lane touches no `store/`
  record; the re-pin itself never runs a measurement window.
- `docs/dev/plan.md`'s `[B84]` row and the STATUS narrative are
  explicitly the manager's job per the brief; left untouched.

## For the manager, on review

- **The registry diff is the emptiest of any re-pin in this project's
  history** — all four surfaces byte-identical, structurally proving
  I-102's "explicitly NOT an axis" claim rather than merely citing it.
- **The size-book decomposition is a NEW SHAPE**: unlike every prior
  re-pin's single flat per-token constant, this stamp's own byte cost
  depends on the TOKEN'S LENGTH (`none`=+26, `emitted`=+29,
  `dominated`=+31, `one-attempt`=+33 bytes — `tools/selfcheck.py`'s new
  `B84_STAMP_LINE_*` family), because `req_why`'s four values are not
  equal-length strings the way most prior stamps' fallback value was.
  Twenty individual `STAMP_CASES`/`LEDGER_STAMP_CASES`/`DENY_CONTROLS`
  emit-size assertions were re-measured against the pin's own binary
  (never guessed from the observed delta alone, though the two agreed
  everywhere cross-checked) — 18 land on `none` (+26), 2 (`altwide
  pfx3-256`, `altwide floor`) land on `emitted` (+29), both forced-VM
  witnesses whose own required byte is NOT scanned by any candidate-
  start scan ahead of it.
- **The box-load hazard, for the process record**: TWO consecutive
  `setsid`-detached `make check` runs hit the identical single
  `inconclusive-load` failure, each time traced live to a DIFFERENT
  concurrent `pcrecbench report` invocation elsewhere on the box (not
  this lane's, not identified further — possibly report/sidecar
  regeneration work ahead of tonight's window). Neither run's failure
  says anything about this lane's own changes: `check_run_smoke` passed
  standalone both times the box was confirmed quiet. Worth a line to
  whoever is running batch report renders concurrently with a re-pin
  lane's `make check` — BOILERPLATE's "ONE heavy suite on the box at a
  time" rule exists for exactly this class of interference, and a
  report render loop is exactly the kind of activity that rule is meant
  to catch even though it is not itself a measurement window.
- **This lane is COMPLETE** except the two explicitly-scoped OWED items
  above (the manager's own window, the manager's own sidecar
  regeneration at merge). No further work is planned unless review
  surfaces something new.
