# b140tools report ([B140] build-order step 4: the TOOLS tier, lane b140tools, 2026-10-25)

Branch `lane/b140tools` (worktree `worktrees/b140tools`, base 58f6af36). No acc-main timing, no window, no `store/` or `reports/` write, no install or download, `~/pcrec` untouched, `testees/pcrec/` and `catalogue/` untouched. Scratch: `/var/tmp/pcrecbench/b140tools/` (acc-small copy, output files, scratch stores, probes, logs). The charter is `docs/design/subst_bench_v1.md` 3.2, 4, 8a (ruling 7 binding); the shared harness is b140drv's/b140drv2's (`substrun.py`'s gate, `plan_case`'s `PATTERN_LEVEL_TOKENS`, the X44/X45 unsupported rows) and was REUSED. The binaries are `build/tools/sd-1.1.0/sd` and `build/tools/ripgrep-15.2.0/rg` of the MAIN checkout (found from the worktree through the git common dir), both sha256-verified at describe/prepare/run time.

## Charter-vs-committed checklist

| # | item | committed artifact / status |
|---|---|---|
| 1 | `pcrecbench/toolrun.py`: untimed correctness pass writing a real output file, then every timed run `tool ... \| wc -c` with wc on a different core, byte count == validated size or the run fails BY NAME | `pcrecbench/toolrun.py` (`untimed_pass`, `timed_pipeline`, `pick_cores`, `SinkMismatch`); no shell: `os.posix_spawn` + file actions, tool and wc under `taskset -c`, env `LC_ALL=C` only, clock = tool spawn to the second `wait4`. The gate is `substrun`'s, unchanged: trial 1's untimed output is hashed against `expectations.tsv`. |
| 2 | five testees: GNU sed -E, perl -pe, python3 whole-file `re.sub` on bytes (committed script), sd 1.1.0, `rg --passthru -r` | `testees/tools/tools.toml` (`sed-ere`, `perl-p`, `python-resub`, `sd-stdin`, `rg-passthru`), `testees/tools/adapter.py`, `testees/tools/subst_py.py`. Command shapes in `toolrun.build_argv`, shown in `testees/tools/CLAUDE.md`. |
| 3 | pin sd and rg BY BINARY SHA256, verified at describe time; sd's `--version` is stale; sed/perl/python: version string AND binary sha256 recorded; absolute paths, never PATH | `tools.toml` `binary_sha256` for sd (`302e7368...29e`) and rg (`e62198eb...849`); `Adapter.binary_path` refuses a mismatch BY NAME (check: a doctored pin). sd's `--version` ("sd 1.0.0") is recorded in `runtime_options.reported_version` + `reported_version_stale`, never compared. System tools: the version string they report must equal `tools.toml`'s (refused by name otherwise, checked), the live binary sha256 is in `testee.binary` and `build_flags` of every record. |
| 4 | records at schema v1.9, `testee.invocation` = process, `match.process` incl. the `wc -c` sink (X39: sink_bytes == out_bytes) | `harness.run_cell` stamps what the adapter's `describe()` says (`invocation: process`, `execution_model: interpretive`); `record.match_row(process=)`; `substrun._judge` attaches the row's `process` object on every timed row. Validator-accepted (X38-X41, X44, X45) in the five dry-run records and in `check_subst` section 11. |
| 5 | the compile row per section 5 S7 (interpretive) | OMITTED for a compiled case (S7/X41): `harness.run_cell` skips the compiled compile row of a `process` testee; `compile_phases` is `[]`, `compile_cost_definition` says why. The compile row that DOES exist is the `unsupported-by-declaration` one (X44/X45). |
| 6 | REUSE `substrun.py`; keep it engine-neutral; templates from the neutral per-dialect render | `substrun.py` edits are engine-neutral: `support["count"] == "oracle"` (below). `subst_template.render` already had sed/perl/python/sd/rg dialects and the hostile-template control (`check_subst` sections 2-3); NOT extended - nothing was missing (the claim is checked by the 32 sha256 agreements). |
| 7 | `divergences.tsv`'s declared unsupported cases become `unsupported-by-declaration` rows | sed 7; perl 7; python 6, 7; sd 6, 7; rg 6, 7 - through `plan_case`, record rows asserted in section 11. sd and rg were also run against case 7's pattern: both refuse the lookahead ("look-around ... is not supported"); sed/perl/python are covered by section 8. |
| 8 | sed is leftmost-longest: every case where sed's output differs from PCRE2's is a FINDING | NO such case on acc-small: sed agrees on all 7 cases it can run. The table below. Not a claim about acc-main (OWED). |
| 9 | `tools/check_subst.py` section for the tools tier on acc-small | section 11, `_tools_tier`: 24 checks (list below). |
| 10 | one scratch dry run per tool on acc-small (`--tier scratch`), validator-accepted | five records, below. |
| 11 | full `make check-harness`, counts honest | see "Check counts". |
| 12 | CLAUDE.md for every directory touched (incl. new `testees/tools/CLAUDE.md`) and the `adapters.py` protocol doc | `testees/tools/CLAUDE.md` (new), `testees/`, `pcrecbench/`, `tools/`, `docs/dev/lanes/`, `bench/capability/` CLAUDE.mds; `pcrecbench/adapters.py` header "THE PROCESS INVOCATION" + the `subst_support` `count` key. |

## The per-(tool, case) agreement table (acc-small, 3,929,818 B; output sha256 + length == `expectations.tsv`, judged by hashlib after the untimed pass)

| case | sed-ere | perl-p | python-resub | sd-stdin | rg-passthru |
|---|---|---|---|---|---|
| 1 literal | agrees | agrees | agrees | agrees | agrees |
| 2 rare | agrees | agrees | agrees | agrees | agrees |
| 3 dense | agrees | agrees | agrees | agrees | agrees |
| 4 reorder | agrees | agrees | agrees | agrees | agrees |
| 5 mask-ipv4 | agrees | agrees | agrees | agrees | agrees |
| 5b mask-email | agrees | agrees | agrees | agrees | agrees |
| 6 upper | agrees | agrees | unsupported:no-case-operators | unsupported:no-case-operators | unsupported:no-case-operators |
| 7 url-tld-fix | unsupported:pattern-syntax | unsupported:no-conditional | unsupported:no-conditional | unsupported:pattern-syntax | unsupported:pattern-syntax |

32 runnable pairs, 32 agree, 0 wrong, 0 divergent-declared. Every `unsupported` cell is the table's own declaration, not an observation, except that sd and rg were also seen refusing case 7's pattern.

## The section-11 checks (24, `tools/check_subst.py`)

Per tool x5: (a) the untimed pass over every case the table does not declare unsupported (7+7+6+6+6 = 32 pairs) - sha256 and length equal the expectation; (b) one timed `tool | wc -c` on case 1 - clean exit, wc's count == `out_bytes` (3,836,788), the input 100 % resident by `fincore`, wc on another core. Once: (c) the unsabotaged two-trial sed cell as the control (every timed row has `process`, sink_bytes == out_bytes, the cores differ, `nsubst` is the expectation's), then the SABOTAGED sink (`echo 7`) raising `SINK MISMATCH ... counted 7 bytes` with nothing written; (d) the rusage floor (below); (e) a doctored sd sha256 and a doctored sed version each refused by name, the real pins describing. Per tool x5 through `run_cell`: a schema-1.9 `process` record accepted by `store.write` with one row per runnable (case, trial), every one `matched-as-expected` / gate `agrees` / the oracle's `out_sha256` / `process.sink_bytes == out_bytes` / the cores differ (sed with 2 trials, the rest 1), and the compile rows are exactly the declared-unsupported cases, no compile row for a compiled case, no match row for an unsupported one.

## Scratch dry runs (acc-small, `run --subbench subst --testee T --tier scratch --subjects 1 --trials 5 --pin 14`)

All five `schema/validate.py --check-filename`: `1 valid, 0 invalid`. Status `measured` (the scratch tier does not gate; the box was quiet). Tool on core 14, wc on core 15 (14's SMT sibling is 6). Records (gitignored, not committed):

* `/var/tmp/pcrecbench/b140tools/store2/records/subst@0.1/sed_4.9_default-caps-simdna/subst@0.1__sed_4.9_default-caps-simdna__ryzen7700x__20261025T061848Z.jsonl`
* `.../perl_5.40.1_default-caps-simdna/subst@0.1__perl_5.40.1_default-caps-simdna__ryzen7700x__20261025T061859Z.jsonl`
* `.../python_3.14.4_default-caps-simdna/subst@0.1__python_3.14.4_default-caps-simdna__ryzen7700x__20261025T061910Z.jsonl`
* `.../sd_1.1.0_default-caps-simdna/subst@0.1__sd_1.1.0_default-caps-simdna__ryzen7700x__20261025T061922Z.jsonl`
* `.../ripgrep_15.2.0_default-caps-simdna/subst@0.1__ripgrep_15.2.0_default-caps-simdna__ryzen7700x__20261025T061934Z.jsonl`

Rows: sed/perl 36 (1 compile = the case-7 declaration, 35 match = 7 cases x 5 trials); python/sd/rg 32 (2 compile, 30 match). Each carries the trial-agreement block `agree 0/0 groups -- nothing judged` (the b140drv F1 blindness at iters = 1, below). These are scratch numbers, not measurements; per-call walls on 3.9 MB were 4-120 ms.

## Findings the manager should rule on

1. **`wait4`'s `ru_maxrss` is useless for a small tool, and the charter's "store maxrss from `wait4`" would have been wrong.** A `posix_spawn` child shares the harness's mm until exec and the kernel folds that mm's high-water mark into the child's signal struct at exec, so EVERY tool read the harness's own RSS (measured: 38,964 KB for `sed`, whose real peak is 2,328 KB; the first dry run read 35,816-36,160 KB for sed, perl, sd and rg alike). `maxrss_kb` is therefore taken from the UNTIMED pass: the tool's own `/proc/PID/status` `VmHWM`, polled every 1 ms once `/proc/PID/exe` is the tool's binary (after taskset's exec, so the shared pre-exec mm is never read). The timed run falls back to `wait4`'s value only if the poll never saw the tool. A check asserts the floor and the fix. Residual: a 1 ms poll can under-read a sub-millisecond peak; provenance only, never ranked.
2. **A command-line tool prints no substitution count and no consumed length.** `subst_support` declares `count = "oracle"`: `substrun._judge` takes `nsubst` from `expectations.tsv` iff the output sha256 equals the oracle's (a wrong output records `nsubst` 0, a placeholder its diagnostic names), and `truncation_check` is `not-applicable` (the whole-output hash is the evidence). So for the TOOLS tier `subst.nsubst` is DERIVED, not observed; the `independent_nsubst` column is what keeps the oracle's count honest.
3. **`run.driver_build_flags` / `run.driver_compiler` are required strings and a tool has no driver.** The harness now writes "none: the testee is a command-line tool launched directly ..." / `none` for a `process` testee. No schema change; if the reporter wants to filter on it, `testee.invocation` is the field.
4. **wc is uutils coreutils 0.10.0** (`/usr/bin/wc` -> the cargo coreutils multicall), not GNU wc; recorded in every `build_flags`. Ruling 7's measurement (2 GiB through `| wc -c` at ~5-6 GB/s) was on this box, so presumably this wc; the sink is the same for every tool.
5. **Trial 1's TIMED run still happens when the untimed output fails the gate** (the adapter cannot see the expectation). Cost: one wasted launch per wrong (tool, case), never a recorded timing (substrun writes none for a wrong cell). A tool that disagrees on acc-main costs one extra 320 MB run.
6. **The v1.4 trial-agreement blindness (b140drv F1) applies identically**: iters = 1, so every group is "unjudged", a PINNED tools record is `measured` whatever its trial spread. Still the manager -> Frank ruling before the first pinned subst window. For the tools tier it bites harder: the whole-process walls are exactly the numbers the spread rule exists to judge.
7. **`rg` exits 1 when nothing matched; with `--passthru` the output is still the whole file**, so `ok_exit = [0, 1]` for rg. Every acc-small case has matches, so the exit-1 path was NOT exercised; the sha256 gate judges the bytes either way.
8. **sed agreed everywhere it could run.** The leftmost-longest hazard I-157 names is real in general but none of the 7 patterns sed runs has a prefix-ambiguous alternation; this is a result on acc-small (17,500 lines), and `acc-main`'s gate is the stronger statement.
9. **The input is read warm and `fincore`-asserted before EVERY timed launch** (stronger than the charter's "before each tool's block"); a partly cold input raises `NotResident` by name rather than timing it. On acc-main that is one 362 MB read per launch (~0.1 s, untimed).
10. **Pins are checked at describe, prepare and run time** (`binary_path`), each re-hashing sd (and rg): one extra 4-5 MB hash per call to `measure_subst` per subject per trial. Negligible on acc-main, noted.
11. **The generic per-adapter sweeps assumed every adapter has a matcher driver.** The first full `make check-harness` died in `check_driver_smokes` (`Adapter.measure` -> `NotImplementedError` for the tools adapter, after 69 log lines). `Adapter.has_driver` (default True; the tools adapter says False) now makes four sweeps skip it by name: `check_driver_smokes`, `check_kb33_refusal_metadata_declared`, `check_prime_flag`, `check_utf8_find_all_advance`. The sweeps that need no driver include it deliberately: KB-21's `describe()` vs schema (`tools/perl-p` is in its 8 adapters and passes) and the capability-roster coverage (77 testee ids). This is the lane's ONE edit to `tools/selfcheck.py` (four 2-line guards) - the file b142prep may also touch; expect a trivial merge conflict at most.
12. `quick` still does not know the `substitution` regime and `report`/`viewer`/`frontpage`/`trend` were not exercised on a `process` record (b140drv finding 5, unchanged).

## BD16 accounting

No existing instrument is touched: `timed.c`/`timed.h`, the pcre2/rust/RE2 `timed_subst` units, every driver and `driverrun.py` are diff-empty against 58f6af36. The new instrument is `toolrun.timed_pipeline` (a Python function, new file); it has no previous version to A/B against and no disassembly to prove (its clock reads and the spawn path are Python, in one function, `perf_counter_ns` at the same two points for every tool). Edits to shared Python: `substrun._judge` (a new `count_oracle` branch inert for every library testee, whose `support` lacks the key - sections 9 and 10 of `check_subst` pass unchanged in the full run), `MatchRow.process`, `record.match_row(process=)`, the harness's compile-row skip and run-block fallback (both gated on `testee.invocation == "process"`). The re-pin-control run does not apply. OWED: the sentinel read in the first window containing subst cells (owner manager) covers the library instruments; the tools tier has no sentinel analogue (a `taskset ... true | wc -c` null launch would price the fixed launch overhead - a candidate, not asked).

## OWED

| item | owner | trigger |
|---|---|---|
| acc-main gate + timing for the five tools (362 MB; python holds ~1 GB; sed/perl/sd/rg low MB) and the stronger sed agreement statement | manager's window | window grant via pcrecdev1 |
| Finding 6 (spread-rule blindness at iters = 1), b140drv findings 1, 2, 4, 5 | manager -> Frank | before the first pinned subst window / plan [B140] step 5 |
| reporter `--grain subst` over `process` records (ruling 8: no cross-tier ratio column; tiers never mixed in one ordering), `quick`, viewer/frontpage/trend | later lane (step 5) | the charter order |
| the `rg` exit-1 path (an acc-main case with no match does not exist; needs a synthetic subject if it is to be exercised) | manager | optional |
| a null-launch overhead cell (`true \| wc -c`) to price process start + pipe | manager | optional |
| the pcrec-as-a-tool testee (ruling 9) | after [M4-SUBST] | later |

## Check counts

`make check-harness` (= `LC_ALL=C python3 tools/selfcheck.py`, log `/var/tmp/pcrecbench/b140tools/checkh.log`, ends `DONE rc=0`): **924 check(s) passed, 0 FAILED** (the base was 900/0 after b140drv2; the +24 are section 11). History, stated because the first full run was not clean: run 1 died at the driver smoke with an uncaught `NotImplementedError` (finding 11; 69 log lines, no count), fixed by `Adapter.has_driver`; the four generic sweeps and the two that include the tools adapter were re-run standalone (32 checks, 0 failed) before the clean second full run. Section 11 alone: 24 ok / 0 bad in 54 s. Not run (nothing they read changed): `make check-report`, `check-interpret`, `check-upstream`, `check-schema`.
