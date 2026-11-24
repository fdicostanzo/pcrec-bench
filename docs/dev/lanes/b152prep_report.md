# lane b152prep report: RE-PIN THE WHOLE ROSTER to d6c5e71a5 (abi 112); also_pins cb32eda28 (abi 93)

Plan row [B152], inbox I-179. Branch `lane/b152prep`, worktree `worktrees/b152prep`. The task was to be MERGE-READY
by 00:45 on 2026-11-24, ahead of tonight's pinned window (01:50). All builds, the census, the smoke and the checks
ran under `nice -n 19 taskset -c 0-5` with at most two concurrent jobs. Nothing was timed. Scratch output went only
under `/var/tmp/pcrecbench/b152prep/`.

## 0. Verdict

**WINDOW: GO at d6c5e71a5** (with `@cb32eda28` as the cross-pin control). Every cell the brief named wrote a record
that the validator accepts. Every non-measured outcome is named in section 2, and each one is pre-existing:
identical at cb32eda28, or a size-cap or declaration refusal. No closed-set value that the window's sets produce is
rejected. That holds over every emit of the 1,600-row census, plus the `-fno-landmark-walk` arm, read against the
adapter's METADATA_DECL. The shim floor stays 16.

## 1. Adapter, configs and the shim (item 1)

- `configs.toml`: `pin = "d6c5e71a5"`, `also_pins = ["cb32eda28"]`. 614d45eb3 is retired and refused by name.
- Abi 94-112 add no `struct rx_info` field, so `PB_SHIM_MIN_ABI` stays 16 (`check_abi_floor_refusal`).
- Closed sets widened, each MEASURED on an artifact:
  - `dfa_scan` + `landmark-walk`: abi 95 [LANDWALK], 11 census rows, the `locate` axis order 3, bit 57
    `-fno-landmark-walk`.
  - `dfa_scan` + `char-step`: the character-stepped DFA for UCP `\b` under `-e utf8`. It is not an axis row, so it
    lives in `REGISTRY_OUTCOME_VALUES`.
  - `req_why` + `untestable`: abi 106, 36 rows.
- New text-read stamp `targets` (`RX_TARGETS`, abi 98 [XARCH]). It reads `none:generic` on every artifact.
- `RX_REQ_RUN` (abi 104 respelling) and `RX_REQ_HANDOFF` (abi 105 `unbounded`, abi 112 negative K) stay free text.
- **`char-step` was found by this lane's closed-set sweep, after the 19:52 status went out.** Only bench/utf8
  `asr-b-cyr-ucp` stamps it. That pattern is `unsupported-by-declaration` under every utf8 roster config, so no
  window cell would have written it. It is admitted now, so a later declaration cannot fail. Witness through the
  adapter: char-step / reverse-pass / search-filter / prefilter none / targets none:generic. The whole-subject form
  refuses `(*VERB) not recognized` at both pins, because the `(*UCP)` lands inside the wrapper; this is pre-existing.
- Pinned-record validation: all 11 scratch records validate (`schema/validate.py --check-filename`, 11/11). Each of
  the 10 d6c5e71a5 records was also re-stamped `tier: pinned`, with the binary dropped and the hash recomputed with
  `record.stamp_content_hash`, and validates 10/10.

## 2. Scratch smoke (item 2)

Run by `docs/dev/lanes/b152prep_smoke.sh` (`--tier scratch --trials 1 --iters 1`, store
`/var/tmp/pcrecbench/b152prep/store`) between 18:03 and 18:10. Every cell exited 0. Every record is indexed
`inconclusive-load`, which is the honest status on a box that is not quiet; nothing was measured.

| cell | compile | match | non-measured outcomes (all named) |
|---|---|---|---|
| sentinel@0.1 × pcrec-auto | 30 compiled | 1,125 as expected | none |
| sentinel@0.1 × pcrec-auto@cb32eda28 | 30 | 1,125 | none |
| altwide@0.3 × pcrec-auto | 73 / 5 did-not-compile | 3,056 | clsa-1024, clsd-1024, s-4096, w-1024, w-2048: emitted-size cap (pre-existing) |
| altwide@0.3 × pcrec-vm | 70 / 8 | 2,940 | ci-512, s-2048 (plus the larger rungs), both forms: code-size cap (pre-existing) |
| capability@0.4 × pcrec-auto | 140 / 1 unsupported-by-declaration | 6,575 | negation-scope-lookbehind-var (declaration); 3 FRAMES gave-up (date-nested-plus t-hyb-datepath-16k, dup-param-detect ×2); email-nested-plus t-evil-match-60k / t-evil-nearmiss-16k "no expectation exists" |
| syntax@0.2 × pcrec-auto | 167 / 23 | 7,423 | 23 compile refusals (unimplemented modules, (*SKIP), mod-x whole); asr-k-uc f-kv wrong-span; rec-r-uc f-parens did-not-match; 9 FRAMES gave-up (rec-1, rec-name, rec-r-uc × t-64k/256k/1m) |
| bounded@0.3 × pcrec-auto | 84 / 2 | 4,200 | cls-upto-65535 both forms: NFA 131072-state cap (pre-existing) |
| utf8@0.1 × pcrec-auto-utf8 | 138 / 5 unsupported / 4 | 6,762 | 5 unicode-class-scope declarations; prp-ingreek (unimplemented property); prp-l-anchored (emitted-size cap) |
| loglines@0.1 × pcrec-auto | 22 | 1,364 | none |
| email@0.2 × pcrec-auto | 6 | 501 | none |
| litrun@0.1 × pcrec-auto | 28 | 1,134 | none |

I compared these records outcome by outcome with the canonical store's ryzen7700x records at cb32eda28. That
comparison covers sentinel, syntax and capability; the other sets have no cb32eda28 record of this config. Every
non-good outcome is IDENTICAL at cb32eda28. That includes the syntax wrong-span and did-not-match rows, all FRAMES
give-ups and both capability no-expectation rows. **Zero regressions.** The one mover is capability
`wild-datetime-datefinder-alternation`, both forms: did-not-compile → compiled, every match row as expected. That
is an improvement; the census names it too. Capability also has 94 match rows new at this pin, all as expected.
They come from the newly compiling pattern.

## 3. Compile-only census (item 3)

`docs/dev/measurements/2026-11-23-b152prep-census.txt` (+ `.tsv`). It covers 11 sets × {plain, whole} ×
{auto-caps, auto-nocaps}, 1,600 rows, emitted with `-fcomments --features all` (`-e utf8` on utf8). v2 and v3
identity agree on every row.

- **936 identical / 575 changed / 78 refused-both / 11 refusal movers. 0 UNATTRIBUTED.**
- Attribution (a row can carry more than one marker):
  - abi 103 [FIND-MINW] min-width early-out: 483 rows. 188 of them change in nothing else, and those 188 were
    checked line by line: only the min-width lines differ.
  - abi 104-112 req-run / handoff: 258 rows.
  - abi 97 altnf stamps: 105 rows.
  - abi 97 utf8 DFA table changes: 88 rows. These come from the sibling merge of wide-class UTF-8 boxes, which
    pcrec's changelog says gives "smaller DFA tables". The largest is `prp-l` plain at −77,030 B.
  - abi 95 landmark walk: 11 rows.
  - abi 108 cover: 8 rows.
  - abi 110 span-vector: 6 rows.
- **Refusal movers.** All 11 were refused at cb32eda28 and compile at d6c5e71a5; none went the other way:
  - capability `wild-datetime-datefinder-alternation`: caps plain (`size-cap-retry`), caps whole, nocaps whole.
  - capability `negation-scope-lookbehind-var`: ×4 (abi 96, variable lookbehind).
  - utf8 `cls-w-ucp`: caps and nocaps plain.
  - utf8 `asr-b-cyr-ucp`: caps and nocaps plain.
- **Deny control.** The `-fno-landmark-walk` arm differs from the canonical emit on exactly the 11 abi95 rows and
  on no other row. On those rows it restores a program close to cb32eda28's size.
- Sizes: 101 changed rows shrink and 474 grow (median +176 B emit).

## 4. Deny controls, registries, docs, catalogue (item 4)

- DENY_CONTROLS row `-fno-landmark-walk` on `foo[0-9]+bar`: `dfa_scan` goes landmark-walk → unanchored and
  `req_why` goes dominated → emitted (commit 75d24bb7). New check `check_b152_stamps` asserts the four new values by
  value.
- Registries re-archived with chained headers:
  - axes MAIN 176 → 181 rows / 50 axes, no new axis
  - limits 78 → 82
  - definitions and schema BYTE-IDENTICAL
  - `registry_check()` returns [].
- Re-aims, each from a stale aim to the real change, with nothing loosened:
  - `check_b135_two_pin_window` now uses canonical d6c5e71a5 and also_pin cb32eda28, with 614d45eb3 added to the
    retired list.
  - `check_b149_stamps` names its own builds (cb32eda28 vs 614d45eb3).
  - `tools/check_calls.py`'s K134 arm runs at the also_pin cb32eda28.
- Catalogue 3.23 (`[[pin_order]]` + d6c5e71a5). 123 sidecars regenerated by `scripts/regen_sidecars.py`; the only
  change in each is the catalogue line.
- testees/pcrec/CLAUDE.md "Re-pin at d6c5e71a5"; docs/dev/lanes/CLAUDE.md and docs/dev/measurements/CLAUDE.md
  entries.

## 5. Findings for pcrec (for the outbox; none blocks the window)

1. **The landmark walk's size.** On `wild-secrets-username-password-pair` nocaps plain, the walk adds +44.3 KB of
   emit (564,961 → 609,262 B). On the other ten rows it adds +6.6..+8.9 KB. The size cap's `drop-landmark-walk`
   fallback rung exists but does not fire here.
2. **`char-step` has no axis row.** It is forced by the pattern's set rather than chosen, so it is a documented
   outcome value. pcrec may want to list it in the `locate` axis, or state the reason it is absent.

## 6. Checks run (the full `make check` was NOT run)

All niced and pinned to cores 0-5; logs are under /var/tmp/pcrecbench/b152prep/.

- **`docs/dev/lanes/b152prep_checks.py` (the targeted selfcheck slice, 34 functions): 496 passed, 0 FAILED**
  (checks3.log, 20:24). Its first run went 422 / 74 FAILED. Every one of the 74 was a by-value expectation
  written at cb32eda28. Each was resolved as follows (commit 3460775c):
  - **Size and value moves.** `B152_FLAT` = +56 B on every artifact: the `RX_TARGETS` line plus
    `match-start-reset,` in the module list, which is the mode over 596 v3-identical census rows.
    `B152_RESID`, `B152_VALUES` and `B152_DENY` hold the per-witness moves (25 sizes, 18 values, 7 deny rows),
    each MEASURED through the adapter and attributed to an abi step in the comment above its table.
  - **Historical checks.** The historical by-value checks (b108, b118 cls-kit/findtie, b122, b124, b126) run at
    cb32eda28's OWN build via `_b152_hist_bin`, the way b149prep re-aimed `check_b147_stamps`. Their claims
    concern abi <= 93; the d6c5e71a5 moves are stated by the census and by `check_b152_stamps`. The abi-92 cover
    denial is now applied at that build too, in `_b118_compile` and `_b126_text_eq`.
  - **altwide P1** (altcls_merges == 0) is asserted at cb32eda28, and it holds there. Abi 97 redefined
    `RX_ALTCLS_MERGES` as the alternation owner's merge, so at d6c5e71a5 every altwide witness reads 1, and the
    check reports that.
  - **I-43's island/chain ratios** were re-measured: 1.2068 / 1.2175 / 1.2304, previously 1.234 / 1.238 / 1.265.
    Both arms gain the abi 106 run pre-check.
  - **b104's seven utf8 runs.** `req_byte`, the claim that check exists for, is unmoved on all seven. Three runs
    widen to the whole literal.
  - **Registry rows.** `locate` gains `landmark-walk`; `req-use` gains `handoff-attempts-unbounded`.
  - **No failure was a fault in the adapter, the records or the answers.**
- **`tools/check_calls.py`: 37 ok, 8 FAIL.**
  - The re-aimed K134 arm PASSES: "pcrec-auto answers seg-s x cscan-onig at the canonical pin and at the
    also_pin cb32eda28, 0 of 256 calls gave up".
  - The 8 FAILs are ENVIRONMENTAL. Four `streams:` rows refused with "this box (... cores=6) is not in
    machines.tsv", and the four `limits:` rows read those missing records. `pcrecbench/env.py cores()` is
    `len(sched_getaffinity(0))`, so under this lane's mandatory `taskset -c 0-5` the box key reads 6 cores and
    matches no registered machine. The window does not run under taskset. The first run also lacked
    bench/unusual's generated subjects, so I generated them in the worktree (deterministic; the manifests
    reproduced byte for byte).
- **`make check-interpret`: 297 passed, 0 FAILED**, after the 123 sidecars were regenerated (catalogue 3.23).
- `registry_check()` returns []. `check_b152_stamps` passes 4/4. `schema/validate.py`: 11/11 smoke records and
  10/10 pinned re-stamps.
- NOT run: the full `make check`, `make check-harness` beyond this slice, `make check-unusual`, check-report,
  check-upstream, check-schema.

## 7. Charter vs committed

| brief item | committed? |
|---|---|
| adapter + driver build at d6c5e71a5, abi 94-112 stamps read | yes: 0c37f118, f3d028d3 |
| targeted selfcheck slice green at the new pin | yes: 496/0 after 3460775c |
| new enum values in closed sets | yes: landmark-walk, char-step, untestable, targets |
| rx_info + shim floor 16 checked | yes: check_abi_floor_refusal, in the 496/0 slice |
| a pinned record validates | yes: 10/10 re-stamped pinned (section 1) |
| no closed-set value the window produces rejected | yes: the census-wide sweep found 0 undeclared after f3d028d3 |
| scratch smoke on all 11 cells | yes: 11/11 rc 0, all outcomes named (section 2) |
| census, every change attributed, movers named | yes: section 3, archived |
| deny controls for new deny flags | yes: `-fno-landmark-walk` (the only new deny flag) |
| registries re-archived | yes |
| testees/pcrec/CLAUDE.md section | yes |
| catalogue | yes: 3.23, sidecars regenerated |
| this report with go/no-go | yes |

## 8. OWED

- The full `make check` (not run, per the brief). Run it in a slot after the window, WITHOUT `taskset`: the
  machine key counts affinity cores (see section 6), which is also a known-issue candidate (KB) for the manager.
- `tools/check_calls.py`'s eight machine-registry FAILs need that un-tasksetted run to clear; the K134 arm passed.
- The outbox note for pcrec (section 5) and the plan.md / dev_journal entries are the manager's.
