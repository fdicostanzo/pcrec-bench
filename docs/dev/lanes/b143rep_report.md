# b143rep report -- the reporter: Part A (check-report reds), Part B (abi 77+ items), Part C (the substitution view)

Lane b143rep, branch `lane/b143rep` from master f1ea966b, 2026-10-25. No `store/` write, no timing, no `reports/` write
(no committed report changes by a byte: none carries an abi >= 77 or a substitution record), so no sidecar regeneration was needed.

## Part A -- the eight check-report reds

**Diagnosis VERIFIED** (not assumed): on master the suite reads `96 passed, 8 failed`; every failure message is
`the selected records span 2 machines (budu-ryzen1600, ryzen7700x); a report is PER HOST ... add --machine <id> (O-90, [B137])`
(`store/index.tsv` now holds both hosts for email-specimen, loglines, bounded, altwide, litrun, syntax, utf8, capability, sentinel).
Fix is in the TESTS only (`REAL_MACHINE = "budu-ryzen1600"`, the host every committed fixture/report was built from, passed in
every `_args(store=REAL_STORE, ...)` and in the `report.main` call of the KB-16 test); the refusal is untouched. Result:
`108 passed, 0 failed` after Parts A-C (104 after A alone).

**Committed reports' query lines vs `--machine` (REPORTED, nothing regenerated):** 40 of the 136 committed report TSVs carry
`machine=` in their `filters:` header; **96 do not**. `scripts/regen_reports.py` rebuilds the argv from `filters:` alone, so
regenerating one of those 96 would now REFUSE wherever the subbench@version has records from the second host. The regeneration must
add `--machine <id>` from the file's own `machines:` header key; the regenerated `filters:` line then GAINS `machine=<id>`, so
those files change by that line (plus the version line): an expected, classifiable diff, not a content change. OWED: amend
`scripts/regen_reports.py` (owner: manager; trigger: the next regen wave, i.e. the first v27 report group). Recorded in `reports/CLAUDE.md`.

## Part B -- [B142]'s owed reporter items, reporter v27

* `compound=<name>` legend clause (after `clsfolds=`) + its legend line, from `RX_COMPOUND` (abi 77+). The stamp is on EVERY artifact
  at its abi and `none` is the plain case, so the clause prints only for a non-`none` value (presence cannot gate it); reports over
  pre-77 pins and plain artifacts are unchanged.
* Emit-bytes definition note under the `emit bytes`/`code bytes` columns, printed iff a row in the table has abi >= 77: the flat
  ~+106 B of counted stamp/initializer lines, the find-all iterator scaffold excluded from both counts from abi 83 with no marker in
  the text, and the DFA retry machine (`RX_ITER_RETRY=retry`) NOT being scaffold (b142prep section 6).
* `REPORTER_VERSION` `v26 (2026-10-13)` -> `v27 (2026-10-25)`; the version pin test and the module docstring moved with it.
* Catalogue/sidecar knock-on: **none required, by measurement.** The version string is stamped only into reports as they are
  rendered; no committed report is regenerated, so no sidecar's stamped inputs move, and the catalogue reads no `REPORTER_VERSION`
  (`grep` of `interpret.py`/`catalogue/*.py`: no reference except `refresh_golden.py`'s docstring). `make check-interpret` is
  271 passed / 0 FAILED. The first v27 report (the abi-84 window's) will be the one whose sidecar is stamped against it.

## Part C -- the substitution view ([B140] step 5)

* `python3 -m pcrecbench report --grain subst [--format md|tsv]` -> `pcrecbench/report_subst.py` (lazy import from `report.main`).
  Matrix and subject-grain-slice are refused with it BY NAME. Rulings applied: two tiers reported separately (`testee.invocation`),
  no cross-tier ratio (the sentence is in both renderings; the TSV header says `cross_tier_ratio: none`); LIBRARY ratio vs
  `pcre2-jit`, TOOLS ratio vs `sed`; `unsupported` a first-class cell with its declared token (also in the TSV as `state`); `wrong`
  shown with the first differing byte and excluded from every derived number; `divergent-declared` shown with its citation; per-case
  `n_subst` under the case name; pcrec's (and every library testee's) compile time a SEPARATE table; a TOOLS tier says it has no
  compile (S7); one summary row per case, pcrec LIBRARY / best-other-library, wrong/unsupported excluded, not computed for TOOLS.
  Tier/status/dedup/one-host rules are the standard reporter's (scratch and non-measured listed under "Not ranked" unless
  `--include-scratch` / `--include-unmeasured`).
* The standard grains now leave substitution records alone: a selection of ONLY substitution records is refused BY NAME
  (`use --grain subst`); a mixed selection drops them. No committed query selects any.
* **Sidecar rename** `bench/subst/subst.toml` -> `subbench.toml` (git mv); `subbench.py`'s `SIDECAR_NAMES` is now `("subbench.toml",)`.
* **Generic gates, decided BY NAME** (`tools/selfcheck.py` `SUBST_GATE_SKIPS`, a skip prints an `ok` line with its reason, and
  `check_subst_gate_skips` proves each name drops exactly that set, is passed by a real call site, and that an unnamed gate keeps it):

| gate (`subbench_dirs(...)`) | substitution set | reason |
|---|---|---|
| `manifests` (`check_manifests`) | SKIPPED | `gen_subjects.py` without `--check` WRITES the 320 MB acc-main; `check_subst` re-derives acc-small and the manifest with `--check` |
| `floor-quick-cell` | SKIPPED | no `role: floor` pattern, no match/search regime |
| `floor-oracle-smoke` | SKIPPED | no floor pattern, no matcher driver mode (driver answers `--mode subst`; check_subst section 9) |
| `rxt-export` | SKIPPED | its patterns are (pattern, template) cases, not match blocks |
| `expectations` (`gen_expectations.py --check`, 0.3 s) | APPLIES | |
| KB-12 id slug rule | APPLIES | |
| `${` scan (`check_vars_surface`), free_text cap (`check_pattern_text_cap`), UTF option word (byte, 0), capability no-op | APPLY | run against the set: all PASS |
| `importer._committed_sets` | APPLIES | `subst` now reads `('0.1', 7da96abe...)`, so `pcrecbench import` checks substitution records' set version and hash |
| report `resolve_subbench_arg` | no-op | id == directory (`subst`) |

Tested on the scratch records the earlier lanes left, copied into `/var/tmp/pcrecbench/b143rep/store` (b140drv pcre2-jit,
b140drv2 rust + re2, b140tools/store2 sed/perl/python/sd/rg: 8 records, one host, all `tier: scratch`; the pcre2-jit one
`inconclusive-load` at 3 trials, hence `--include-scratch --include-unmeasured`; `build/scratch-store` does not exist in the main tree).
**There is no pcrec substitution record yet** (b140pcrec's lane), so the pcrec summary row renders its `n/a` form here; it is
exercised with a hand-built pcrec record in `test_subst_tiers_ratios_and_summary_b143` (pcrec 0.5 ms vs jit 1.0 ms = x2.00 faster).

Findings (not fixed, for the manager):
1. The three library records are not comparable in trial count (pcre2-jit 3 trials, the others 5) and the agreement lines read
   `agree 0/0 groups -- nothing judged` (b140drv's known limit, iters = 1): the reporter prints it verbatim; a pinned substitution
   record is `measured` whatever its spread until gate_shape_v14.md 3.5 is amended.
2. The TSV's `record` rows reuse `state` for the record status and `gate` for the record tier (the column set is cell-shaped);
   an interpreter rule that wants substitution cells needs its own section names (design 6: "catalogue minor bump is a follow-up").
3. `sd` reports `reported_version: sd 1.0.0` (stale flag set) for the 1.1.0 binary: shown only in the record, not the report.

## Sample rendered subst report (verbatim; `report --grain subst --machine ryzen7700x --subbench subst --include-scratch --include-unmeasured`)

```markdown
# pcrec-bench report

reporter: v27 (2026-10-25)

## Query

- filters: subbench=subst, machine=ryzen7700x
- record source: walked store/records/ (no index.tsv) (8 record(s) matching this query)
- records included: 8
    - `subst@0.1__libpcre2_10.46_jit-caps-simdna__ryzen7700x__20261025T045034Z` (store/records/subst@0.1/libpcre2_10.46_jit-caps-simdna/subst@0.1__libpcre2_10.46_jit-caps-simdna__ryzen7700x__20261025T045034Z.jsonl) — agreement: n/a (3 trials)
    - `subst@0.1__perl_5.40.1_default-caps-simdna__ryzen7700x__20261025T061859Z` (store/records/subst@0.1/perl_5.40.1_default-caps-simdna/subst@0.1__perl_5.40.1_default-caps-simdna__ryzen7700x__20261025T061859Z.jsonl) — agreement: agree 0/0 groups -- nothing judged (7 rows unjudged)
    - `subst@0.1__python_3.14.4_default-caps-simdna__ryzen7700x__20261025T061910Z` (store/records/subst@0.1/python_3.14.4_default-caps-simdna/subst@0.1__python_3.14.4_default-caps-simdna__ryzen7700x__20261025T061910Z.jsonl) — agreement: agree 0/0 groups -- nothing judged (6 rows unjudged)
    - `subst@0.1__re2_11.0.0_default-caps-simdna__ryzen7700x__20261025T054039Z` (store/records/subst@0.1/re2_11.0.0_default-caps-simdna/subst@0.1__re2_11.0.0_default-caps-simdna__ryzen7700x__20261025T054039Z.jsonl) — agreement: agree 0/0 groups -- nothing judged (6 rows unjudged)
    - `subst@0.1__ripgrep_15.2.0_default-caps-simdna__ryzen7700x__20261025T061934Z` (store/records/subst@0.1/ripgrep_15.2.0_default-caps-simdna/subst@0.1__ripgrep_15.2.0_default-caps-simdna__ryzen7700x__20261025T061934Z.jsonl) — agreement: agree 0/0 groups -- nothing judged (6 rows unjudged)
    - `subst@0.1__rust_1.13.1_default-caps-simdna__ryzen7700x__20261025T054025Z` (store/records/subst@0.1/rust_1.13.1_default-caps-simdna/subst@0.1__rust_1.13.1_default-caps-simdna__ryzen7700x__20261025T054025Z.jsonl) — agreement: agree 0/0 groups -- nothing judged (6 rows unjudged)
    - `subst@0.1__sd_1.1.0_default-caps-simdna__ryzen7700x__20261025T061922Z` (store/records/subst@0.1/sd_1.1.0_default-caps-simdna/subst@0.1__sd_1.1.0_default-caps-simdna__ryzen7700x__20261025T061922Z.jsonl) — agreement: agree 0/0 groups -- nothing judged (6 rows unjudged)
    - `subst@0.1__sed_4.9_default-caps-simdna__ryzen7700x__20261025T061848Z` (store/records/subst@0.1/sed_4.9_default-caps-simdna/subst@0.1__sed_4.9_default-caps-simdna__ryzen7700x__20261025T061848Z.jsonl) — agreement: agree 0/0 groups -- nothing judged (7 rows unjudged)
- sub-bench version(s): subst@0.1
- machine(s): ryzen7700x
- schema version(s): 1.9
- grain: subst (per case x subject; median over trials of `elapsed_ns / iterations`; MB/s = subject bytes / 10^6 / seconds; ratio = baseline median / cell median)
- the tiers are not comparable: the LIBRARY tier times only the transform in-process; the TOOLS tier times a whole `tool ... | wc -c` launch (process start, pattern parse, I/O). No cross-tier ratio is computed.
- Oniguruma, TRE and Vectorscan are not in this set (no usable substitute API, subst_bench_v1.md 3.1); that is a roster fact, not an `unsupported` cell.
- LIBRARY baseline: `libpcre2_10.46_jit-caps-simdna`
- TOOLS baseline: `sed_4.9_default-caps-simdna`

## LIBRARY tier

### LIBRARY subject `acc-small` (3,929,818 B)

| case | `libpcre2_10.46_jit-caps-simdna` | `re2_11.0.0_default-caps-simdna` | `rust_1.13.1_default-caps-simdna` |
|---|---|---|---|
| **1** `1-literal` (n_subst 15,505) | 705.0 us (5574 MB/s) baseline | 5.459 ms (720 MB/s) x7.74 slower | 1.769 ms (2222 MB/s) x2.51 slower |
| **2** `2-rare` (n_subst 2) | 542.2 us (7248 MB/s) baseline | 4.874 ms (806 MB/s) x8.99 slower | 1.720 ms (2285 MB/s) x3.17 slower |
| **3** `3-dense` (n_subst 426,622) | 12.349 ms (318 MB/s) baseline | 44.206 ms (88.9 MB/s) x3.58 slower | 22.457 ms (175 MB/s) x1.82 slower |
| **4** `4-reorder` (n_subst 17,500) | 2.339 ms (1680 MB/s) baseline | 9.566 ms (411 MB/s) x4.09 slower | 5.951 ms (660 MB/s) x2.54 slower |
| **5** `5-mask-ipv4` (n_subst 17,785) | 4.479 ms (877 MB/s) baseline | 8.740 ms (450 MB/s) x1.95 slower | 9.545 ms (412 MB/s) x2.13 slower |
| **5b** `5b-mask-email` (n_subst 830) | 3.173 ms (1239 MB/s) baseline | 7.448 ms (528 MB/s) x2.35 slower | 1.743 ms (2255 MB/s) x1.82 faster |
| **6** `6-upper` (n_subst 10,236) | 2.547 ms (1543 MB/s) baseline | **unsupported** (no-case-operators) | **unsupported** (no-case-operators) |
| **7** `7-url-tld-fix` (n_subst 283) | 468.9 us (8381 MB/s) baseline | **unsupported** (pattern-syntax) | **unsupported** (pattern-syntax) |

pcrec LIBRARY / best-other-library: n/a (no ranked pcrec library testee in this report)

### LIBRARY compile (a SEPARATE column, never added into a run time)

| case | `libpcre2_10.46_jit-caps-simdna` | `re2_11.0.0_default-caps-simdna` | `rust_1.13.1_default-caps-simdna` |
|---|---|---|---|
| **1** `1-literal` (n_subst 15,505) | 6.2 us (compile 0.7 us, jit-compile 5.5 us) | 1.7 us | 3.3 us |
| **2** `2-rare` (n_subst 2) | 11.7 us (compile 1.9 us, jit-compile 9.8 us) | 5.2 us | 31.0 us |
| **3** `3-dense` (n_subst 426,622) | 4.7 us (compile 0.9 us, jit-compile 3.8 us) | 1.5 us | 26.4 us |
| **4** `4-reorder` (n_subst 17,500) | 9.9 us (compile 1.7 us, jit-compile 8.2 us) | 4.8 us | 89.3 us |
| **5** `5-mask-ipv4` (n_subst 17,785) | 10.2 us (compile 1.8 us, jit-compile 8.5 us) | 6.9 us | 61.6 us |
| **5b** `5b-mask-email` (n_subst 830) | 9.7 us (compile 1.8 us, jit-compile 7.9 us) | 6.8 us | 16.3 us |
| **6** `6-upper` (n_subst 10,236) | 10.6 us (compile 1.6 us, jit-compile 9.1 us) | unsupported | unsupported |
| **7** `7-url-tld-fix` (n_subst 283) | 32.1 us (compile 6.1 us, jit-compile 26.0 us) | unsupported | unsupported |

## TOOLS tier

### TOOLS subject `acc-small` (3,929,818 B)

| case | `perl_5.40.1_default-caps-simdna` | `python_3.14.4_default-caps-simdna` | `ripgrep_15.2.0_default-caps-simdna` | `sd_1.1.0_default-caps-simdna` | `sed_4.9_default-caps-simdna` |
|---|---|---|---|---|---|
| **1** `1-literal` (n_subst 15,505) | 8.694 ms (452 MB/s) x1.26 slower<br>maxrss 5.7 MB | 18.889 ms (208 MB/s) x2.73 slower<br>maxrss 25.1 MB | 4.797 ms (819 MB/s) x1.44 faster<br>maxrss 8.8 MB | 19.173 ms (205 MB/s) x2.78 slower<br>maxrss 2.1 MB | 6.907 ms (569 MB/s) baseline<br>maxrss 2.4 MB |
| **2** `2-rare` (n_subst 2) | 5.184 ms (758 MB/s) x1.07 faster<br>maxrss 5.2 MB | 18.213 ms (216 MB/s) x3.29 slower<br>maxrss 22.2 MB | 3.748 ms (1049 MB/s) x1.48 faster<br>maxrss 8.9 MB | 17.270 ms (228 MB/s) x3.12 slower<br>maxrss 2.3 MB | 5.530 ms (711 MB/s) baseline<br>maxrss 2.4 MB |
| **3** `3-dense` (n_subst 426,622) | 34.427 ms (114 MB/s) x1.39 slower<br>maxrss 5.9 MB | 89.999 ms (43.7 MB/s) x3.65 slower<br>maxrss 100.6 MB | 58.082 ms (67.7 MB/s) x2.35 slower<br>maxrss 8.9 MB | 120.756 ms (32.5 MB/s) x4.89 slower<br>maxrss 2.2 MB | 24.679 ms (159 MB/s) baseline<br>maxrss 2.3 MB |
| **4** `4-reorder` (n_subst 17,500) | 19.022 ms (207 MB/s) x1.22 faster<br>maxrss 5.9 MB | 48.388 ms (81.2 MB/s) x2.09 slower<br>maxrss 26.8 MB | 12.989 ms (303 MB/s) x1.79 faster<br>maxrss 8.7 MB | 26.631 ms (148 MB/s) x1.15 slower<br>maxrss 2.2 MB | 23.202 ms (169 MB/s) baseline<br>maxrss 2.4 MB |
| **5** `5-mask-ipv4` (n_subst 17,785) | 35.319 ms (111 MB/s) x1.19 slower<br>maxrss 5.9 MB | 52.194 ms (75.3 MB/s) x1.76 slower<br>maxrss 25.6 MB | 22.609 ms (174 MB/s) x1.31 faster<br>maxrss 8.8 MB | 29.053 ms (135 MB/s) x1.02 faster<br>maxrss 2.3 MB | 29.583 ms (133 MB/s) baseline<br>maxrss 2.4 MB |
| **5b** `5b-mask-email` (n_subst 830) | 5.708 ms (689 MB/s) x1.60 faster<br>maxrss 5.5 MB | 59.613 ms (65.9 MB/s) x6.51 slower<br>maxrss 22.4 MB | 3.848 ms (1021 MB/s) x2.38 faster<br>maxrss 7.8 MB | 16.802 ms (234 MB/s) x1.84 slower<br>maxrss 2.1 MB | 9.152 ms (429 MB/s) baseline<br>maxrss 2.4 MB |
| **6** `6-upper` (n_subst 10,236) | 12.603 ms (312 MB/s) x1.06 slower<br>maxrss 5.6 MB | **unsupported** (no-case-operators) | **unsupported** (no-case-operators) | **unsupported** (no-case-operators) | 11.839 ms (332 MB/s) baseline<br>maxrss 2.4 MB |
| **7** `7-url-tld-fix` (n_subst 283) | **unsupported** (no-conditional) | **unsupported** (no-conditional) | **unsupported** (pattern-syntax) | **unsupported** (pattern-syntax) | **unsupported** (pattern-syntax) |

### TOOLS compile (a SEPARATE column, never added into a run time)

_none: a command-line tool re-parses its pattern on every launch, so there is no separable compile (schema v1.9 S7); the parse is inside the timed process wall time and no compile row is recorded._

## Legend

- **cell** = median wall time over trials (MB/s of subject) and the ratio against the tier's baseline; `x2.00 faster` means half the baseline's time. TOOLS cells add the median maxrss under the time.
- **unsupported** = the (testee, case) cannot express the case; a result, never a wrong answer, and never dropped (its token is the declared reason). **WRONG** = the output sha256 differs from the oracle's and the divergence is not declared; shown with the first differing byte, excluded from every number built from the others. **divergent-declared** = differs by a declared, cited divergence.
- **n_subst** under a case name = the oracle's substitution count for that subject (from the agreeing cells).
- the tiers are not comparable: the LIBRARY tier times only the transform in-process; the TOOLS tier times a whole `tool ... | wc -c` launch (process start, pattern parse, I/O). No cross-tier ratio is computed.
- `libpcre2_10.46_jit-caps-simdna` (libpcre2, library tier): status inconclusive-load, record tier scratch, agreement n/a (3 trials)
- `re2_11.0.0_default-caps-simdna` (re2, library tier): status measured, record tier scratch, agreement agree 0/0 groups -- nothing judged (6 rows unjudged)
- `rust_1.13.1_default-caps-simdna` (rust, library tier): status measured, record tier scratch, agreement agree 0/0 groups -- nothing judged (6 rows unjudged)
- `perl_5.40.1_default-caps-simdna` (perl, tools tier): status measured, record tier scratch, agreement agree 0/0 groups -- nothing judged (7 rows unjudged)
- `python_3.14.4_default-caps-simdna` (python, tools tier): status measured, record tier scratch, agreement agree 0/0 groups -- nothing judged (6 rows unjudged)
- `ripgrep_15.2.0_default-caps-simdna` (ripgrep, tools tier): status measured, record tier scratch, agreement agree 0/0 groups -- nothing judged (6 rows unjudged)
- `sd_1.1.0_default-caps-simdna` (sd, tools tier): status measured, record tier scratch, agreement agree 0/0 groups -- nothing judged (6 rows unjudged)
- `sed_4.9_default-caps-simdna` (sed, tools tier): status measured, record tier scratch, agreement agree 0/0 groups -- nothing judged (7 rows unjudged)
```

TSV (first rows of 82; header comment + column header + record and cell rows):

```
# reporter: v27 (2026-10-25); filters: subbench=subst, machine=ryzen7700x; source: walked store/records/ (no index.tsv) (8 record(s) matching this query); records: 8; excluded_invalid: 0; superseded: 0; newer_not_measured: 0; subbench_versions: subst@0.1; machines: ryzen7700x; schema_versions: 1.9; grain: subst; include_unmeasur
section	tier	subject	case	pattern_id	testee	state	gate	n_trials	median_ns	min_ns	max_ns	mb_per_s	ratio_vs_baseline	n_subst	out_bytes	maxrss_kb	user_s	sys_s	compile_median_ns	note
record	library				libpcre2_10.46_jit-caps-simdna	inconclusive-load	scratch													n/a (3 trials)
record	tools				perl_5.40.1_default-caps-simdna	measured	scratch													agree 0/0 groups -- nothing judged (7 rows unjudged)
record	tools				python_3.14.4_default-caps-simdna	measured	scratch													agree 0/0 groups -- nothing judged (6 rows unjudged)
record	library				re2_11.0.0_default-caps-simdna	measured	scratch													agree 0/0 groups -- nothing judged (6 rows unjudged)
record	tools				ripgrep_15.2.0_default-caps-simdna	measured	scratch													agree 0/0 groups -- nothing judged (6 rows unjudged)
record	library				rust_1.13.1_default-caps-simdna	measured	scratch													agree 0/0 groups -- nothing judged (6 rows unjudged)
record	tools				sd_1.1.0_default-caps-simdna	measured	scratch													agree 0/0 groups -- nothing judged (6 rows unjudged)
record	tools				sed_4.9_default-caps-simdna	measured	scratch													agree 0/0 groups -- nothing judged (7 rows unjudged)
cell	library	acc-small	1	1-literal	libpcre2_10.46_jit-caps-simdna	measured	agrees	3	704988	695089	714316	5574.3		15505	3836788				6171	
cell	library	acc-small	1	1-literal	re2_11.0.0_default-caps-simdna	measured	agrees	5	5.45866e+06	5.33801e+06	5.73293e+06	719.924	0.12915	15505	3836788				1684	
cell	library	acc-small	1	1-literal	rust_1.13.1_default-caps-simdna	measured	agrees	5	1.76899e+06	1.58529e+06	1.93393e+06	2221.5	0.398525	15505	3836788				3276	
summary	library	acc-small	1	1-literal		n/a														no ranked pcrec library cell
```

## make check counts

| target | result |
|---|---|
| `make check-schema` | 9 examples accepted, 89 sabotages rejected for the intended rule, 0 WRONG |
| `make check-report` | `108 passed, 0 failed` (test_report) + `7 passed` (test_quick) + `15 passed` (matrix_page); `check-report: OK` |
| `make check-interpret` | 271 passed, 0 FAILED |
| `make check-upstream` | OK -- 14 findings, 3 threads, 0 issues; 23/23 self-test cases |
| `make check-frontpage` / `check-trend` / `check-wtprune` | pass (trend 0 problems in all three cites; wtprune 33 checks, 0 failed) |
| `make check-harness` | **OWED** (boilerplate: a run > 4 min at the end of a lane is the manager's). Targeted slices run here and PASS: the 5 generic gates that now see the substitution set (KB-12 ids, `${` scan, UTF option word, capability no-op, `check_pattern_text_cap`), `check_subst_gate_skips` (11 checks), `gen_expectations.py --check` on bench/subst (8/8). Command: `cd /home/pcrec/projects/pcrec-bench/worktrees/b143rep && LC_ALL=C python3 tools/selfcheck.py > /var/tmp/pcrecbench/b143rep/harness.log 2>&1; echo "DONE rc=$?" >> /var/tmp/pcrecbench/b143rep/harness.log`. Expect a small merge conflict in `tools/selfcheck.py` with lane b140pcrec (the `subbench_dirs` block and the call list near `check_subst_set()`). |

## Charter-vs-committed checklist

| brief item | status |
|---|---|
| BOILERPLATE read; worktree `worktrees/b143rep` on `lane/b143rep` from f1ea966b; scratch under `/var/tmp/pcrecbench/b143rep`; no store/timing/reports writes | done |
| A: verify the diagnosis | done (96 passed / 8 failed on master, every message the two-machine refusal) |
| A: fix the tests, not the refusal | done (`REAL_MACHINE`; commit "Part A") |
| A: report whether committed query lines need `--machine`; regenerate nothing | done (96 of 136 lack it; reports/CLAUDE.md; `regen_reports.py` amendment OWED, owner manager, trigger next regen wave) |
| B: `compound` legend/clause (abi-77) | done (`_compound_display`, legend block, test) |
| B: emit_bytes cross-pin reading note | done (`_emit_definition_note`, test) |
| B: version bump + catalogue/sidecar knock-on, `make check-interpret` green | bump done (v27); knock-on measured to be NONE (no committed report changes); check-interpret 271/0 |
| C: `--grain subst` per design 6 + 8a (two tiers, no cross-tier ratio, pcrec compile separate, unsupported first-class, n_subst under case name, process records) | done (`report_subst.py`, 3 tests) |
| C: rename `subst.toml` -> `subbench.toml`; subbench_dirs / report set-id / importer decided by name | done (table above; `check_subst_gate_skips`) |
| C: test on the earlier lanes' scratch records | done (sample above) |
| `make check` in full, every target's counts | all targets run and reported except `check-harness`: OWED to the manager (command above) |
| report + sample + counts; message the manager; END | this file |
