# b140pcrec report ([B140] build-order step 3, the last library driver: pcrec `--mode subst`, lane b140pcrec, 2026-10-25)

Branch `lane/b140pcrec` (worktree `worktrees/b140pcrec`, base f1ea966b). pcrec pin 9ae59f5d4 (abi 84). No acc-main timing, no window, no `store/` or `reports/` write, no install or download, `~/pcrec` untouched, `report.py` untouched. Scratch: `/var/tmp/pcrecbench/b140pcrec/`. The contract is pcrec's `docs/spec/subst_api.md` at the pin; the charter is `docs/design/subst_bench_v1.md` 3.1, 3.1.1, 3.1.2 with 8a; the shared harness is b140drv's, reused (one 6-line addition, finding 4).

## Charter-vs-committed checklist

| # | item | artifact / status |
|---|---|---|
| 1 | the new artifact kind (pattern + template, two inputs) compiled in the adapter | `testees/pcrec/adapter.py` `_compile_one(subst=)`: rx artifact + `pcrec -p sub [--features subst-extended] --subst-file` + `pcrec --emit-support`, one `.so` of `shim.c` + `subst_shim.c`; support unit private (`PCREC_SUPPORT_STATIC`). |
| 2 | driver `--mode subst`, `out` line, iters 1, refusals by name | `testees/pcrec/driver.c` (`run_subst`), `subst_shim.c` (`pb_subst_all` = the contract's `sub_all()` 6.9). |
| 3 | both sizing modes as separate testee-labelled arms | `pcrec-auto-sizefirst`, `pcrec-vm-sizefirst` (`configs.toml`, `subst_only`, `config_extra` `sizefirst` composed last); bound = one call into `n + 8*count + 1`, size-first = `out == NULL, cap == 0` then the real call at the returned length. |
| 4 | cases 6 and 7 verified by sha256, basis flipped | both agree on all four arms; `bench/subst/divergences.tsv` pcrec rows 6 and 7 `predicted` -> `verified-small`, reasons updated. Case 7 is the VM route (`selected` under auto, `forced` under vm), as predicted. No mismatch, so no pcrec finding. |
| 5 | roster decision | `pcrec-auto`, `pcrec-vm` + their two sizefirst arms. All others refused by name with reason (`Adapter.subst_support`): nocaps, `-in`, utf8, clang, bigcap, deny arms, align/o-level, dfa, pcrec-local. |
| 6 | BD16 instrument | `testees/pcrec/timed_subst.{c,h}` a NEW unit; accounting below. |
| 7 | `tools/check_subst.py` pcrec section | section 12 (+44 checks, below). |
| 8 | one scratch dry run per supported arm, validator-accepted | below. |
| 9 | full `make check-harness` | below. |
| 10 | CLAUDE.mds | `testees/pcrec`, `pcrecbench`, `tools`, `bench/subst`, `docs/dev/measurements`, `docs/dev/lanes`; `bench/capability/gen_patterns.py` EXCLUDED_TESTEES gained the two arms (its `--check` output unchanged). |

## Per-(arm, case) agreement (acc-small, driver called directly, sha256 + count + length == expectations.tsv)

| case | engine (auto / vm) | pcrec-auto | pcrec-vm | pcrec-auto-sizefirst | pcrec-vm-sizefirst |
|---|---|---|---|---|---|
| 1 literal | dfa / vm | agrees | agrees | agrees | agrees |
| 2 rare | vm / vm | agrees | agrees | agrees | agrees |
| 3 dense | dfa / vm | agrees | agrees | agrees | agrees |
| 4 reorder | vm / vm | agrees | agrees | agrees | agrees |
| 5 mask-ipv4 | vm / vm | agrees | agrees | agrees | agrees |
| 5b mask-email | dfa / vm | agrees | agrees | agrees | agrees |
| 6 upper (`\U$1\E`, subst-extended) | vm / vm | agrees | agrees | agrees | agrees |
| 7 url-tld-fix (conditional, subst-extended) | vm / vm | agrees | agrees | agrees | agrees |

The size-first arms' bytes equal their bound siblings' on all 8 cases. Control: case 6 WITHOUT `subst-extended` does not refuse - a backslash is an ordinary byte (subst_api.md 2 para 7), so it compiles and renders `\U..\E` literally; the gate catches it as `wrong` by name.

## Scratch dry runs (`run --subbench subst --testee T --tier scratch --subjects 1 --trials 5`, store `/var/tmp/pcrecbench/b140pcrec/store`)

Each: 80 rows (40 compile, 40 match), all 8 cases `agrees`, `schema/validate.py --check-filename` `4 valid, 0 invalid`. Status: `pcrec-auto`, `pcrec-vm` `measured`; both `-sizefirst` `inconclusive-load` (scratch tier does not gate; the box was busy then - an honest status, not a defect). Agreement block `agree 0/0 groups` (b140drv finding 1, unchanged). Timings are not numbers.

## BD16 accounting

`timed.c` / `timed.h` NOT edited (diff-empty vs f1ea966b). `docs/dev/measurements/2026-10-25-b140pcrec-instrument-additivity.{py,txt}`: `timed_run` 261 insns, sha `4a2e2d849cf44ae9` OLD = NEW, address mod 64 = 0 in both; `main` differs (positive control, 2755 -> 2908 insns); `timed_subst` 89 insns, mod 64 = 0; 8 existing-mode invocations over shared DFA and VM `.so`s (search, match, find-all, `--prime`, `--utf8`, frame buffer) identical on every column but SECONDS. (1) `run.harness_commit` and the driver build line (`timed_subst.c`) record the change. (2) plan row = existing [B140]; no re-pin-control run required for the existing instrument. (3) OWED: the sentinel read of pcrec cells in the first window containing subst cells - owner manager, trigger that window. (4) unaffected (no re-pin). (5) the probe.

## Findings

1. No pcrec finding: every cell agreed, so there is no outbox paragraph to send.
2. The template is an input of the COMPILE for pcrec (baked into the artifact), where every other engine takes it per call. The harness handed `compile()` only the pattern, so `substrun.write_template` now also writes `<template>.flags` (`extended`|`none`) beside the template and the adapter reads both. This is the only change to shared harness code (6 lines; other adapters ignore it).
3. pcrec's `emit-c` compile phase in a substitution cell is the sum of three pcrec execs (rx, `--subst-file`, `--emit-support`); `gcc` covers both translation units; stated in the compile row's diagnostic. The compile cost is therefore not comparable to a non-substitution pcrec compile row.
4. `pb_subst_all` includes the contract's setup (iterator init, context check) in the clock, as a user's wrapper does; its scratch for case-forcing regions is a static 64 KiB (a larger region would be a named `PCREC_SUBST_NOSPACE`, not silent). Fine for this set; not generic.
5. `tools/selfcheck.py`'s abi-floor driver build needed `extra_sources=["timed_subst.c"]` (found by the first full run, fixed).
6. b140drv/b140drv2 findings 1 (trial-agreement rule blind at iters = 1), 2, 4, 5 apply unchanged.

## OWED

| item | owner | trigger |
|---|---|---|
| BD16 (3) sentinel read of pcrec in the first window with subst cells | manager | that window |
| acc-main gate + timing for the four pcrec arms (362 MB; `pb_subst_all`'s output buffer ~360 MB + the subject) | manager's window | grant via pcrecdev1 |
| the b140drv findings 1, 2, 4, 5 rulings | manager -> Frank | before the first pinned subst window |

## Check counts

`make check-harness` (= `LC_ALL=C python3 tools/selfcheck.py`; log `/var/tmp/pcrecbench/b140pcrec/checkh3.log`, ends `DONE rc=0`): **985 check(s) passed, 0 FAILED** on the branch tip (section 12 is +44, standalone driver slice 87 ok / 0 bad). History, because the first two full runs were not clean: run 1 aborted - `selfcheck.check_abi_floor_refusal` builds the pcrec driver without `timed_subst.c` (link error; fixed, finding 5); run 2: 984 passed, 1 FAILED - the frozen pre-U2 id-composition check did not know the `sizefirst` part (fixed in `check_encoding_axis`; the part is composed LAST, append-only). No inconclusive-load item occurred. Not run: `check-report`, `check-interpret`, `check-upstream`, `check-schema`.
