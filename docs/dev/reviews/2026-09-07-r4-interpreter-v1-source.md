# r4 critic panel — `docs/design/interpreter_v1.md`, SOURCE-VERIFICATION lens

Critic: read-only lane, 2026-09-07, main tree at `2bc471e` (+ the
uncommitted-at-read `afc9239` design note). Scope: **factual and citation
accuracy only.** No judgement about whether the design is good — that is
another lens.

Method: every cited `report.py` / `reduce.py` line range was opened and
counted line-by-line; every cited report row was re-extracted from the
committed `.tsv` with `awk` on the 18-column layout; the §10 census
claims were re-derived with an independent script over all 42 committed
report TSVs; the §6.1 grep was re-run and widened.

**93 distinct claims checked · 22 discrepancies · 0 could-not-verify.**
None of the 22 is a fabricated number: the arithmetic and the cited
report rows are, with the exceptions listed, correct to the digit. The
discrepancies cluster in three places — the record-row column mapping
(D1/D2), the two rules whose predicate cannot match the data they are
promised to match (D5/D7), and the §9.2 output specification's internal
consistency with §5/§7.1/§8(5) (D14/D15).

---

## Findings

### Source citations — `report.py` / `reduce.py` / `store/index.tsv`

| # | Location in note | Claim | What I found | Verdict |
|---|---|---|---|---|
| 1 | §1 | `REPORTER_VERSION`, report.py:896 | line 896 is exactly `REPORTER_VERSION = "v15 (2026-09-05)"` | CONFIRMED |
| 2 | §2.1 | `render_tsv` at report.py:4065 | line 4065 is `def render_tsv(rd: ReportData):` | CONFIRMED |
| 3 | §2.1 | header comment line, report.py:4068-4091 | the single `lines.append("# " + "; ".join([...]))` spans exactly 4068-4091 | CONFIRMED |
| 4 | §2.1 | 18-column table, report.py:4092-4094 | the `header = [...]` literal spans exactly 4092-4094 and holds 18 names in the note's order | CONFIRMED |
| 5 | §2.1 | all 14 header keys the note names exist | `reporter, filters, source, records, excluded_invalid, superseded, newer_not_measured, subbench_versions, machines, schema_versions, grain, x13_rules, mixed_x13, worst_other_core_busy` all emitted at 4069-4091 | CONFIRMED |
| 6 | §2.1 | `records` = the included count | `f"records: {len(rd.included)}"` (4072) | CONFIRMED |
| 7 | §2.1 | `source` carries the candidate count (KB-8) | header of the email report reads `source: store/index.tsv (14 record(s) matching this query)` | CONFIRMED |
| 8 | §2.1 | `section` ∈ the eight named values | all eight emitted: `record` 4104, `rank` 4149, `excluded`/`not_ranked`/`scratch` 4124/4127/4130 via `others`, `did_not_compile` 4172, `compile` 4179, `compile_stamp` 4225 | CONFIRMED |
| 9 | §2.1 | a `record` row carries the record id in `testee`, **the agreement string in `gave_up_summary`'s slot**, the after-sample in `delta_verdict`'s (report.py:4100-4107) | the row is `["record","","","","","",rid,"","","","agreement",_agreement_display(...),"","","","","",after]`. The agreement string lands in **`value`** (col 12, with `metric` = `agreement`); `gave_up_summary` (col 17) is **empty**. Verified against data: every `record` row of the email report has `$11=agreement`, `$12=n/a (v1.x)`, `$17=""`. The note has copied report.py's own stale comment at 4097-4099. §4.1's own Inputs line (`report:record.{testee,value,delta_verdict}`) is CORRECT and contradicts §2.1. | **DISCREPANCY (D1)** |
| 10 | §2.1 | a `rank` row emitted six times per (group, testee, form), metrics `median_ns\|min_ns\|max_ns\|stddev_ns\|ratio_vs_baseline\|ratio_vs_best`, report.py:4146-4153 | the metric tuple and the emit loop occupy exactly 4146-4153, in that order | CONFIRMED |
| 11 | §2.2 | `store/index.tsv` line 1 is the 8 columns `path subbench version testee_id machine_id timestamp status rows` | byte-identical | CONFIRMED |
| 12 | §2.2 | the join key: a `record` row's `testee` is the basename of `path` minus `.jsonl` | checked on all 9 email `record` rows against their index paths | CONFIRMED |
| 13 | §2.2 | no committed report contains a `not_ranked` row | `grep -c '^not_ranked' reports/*.tsv` → 0 in all 42 | CONFIRMED |
| 14 | §2.2 | nine `inconclusive-load` + one `inconclusive-spread` in the index, appearing in no report | index statuses: 150 measured / 9 inconclusive-load / 1 inconclusive-spread (160 records, 161 lines). All ten record ids grepped against all 42 TSVs: zero hits. | CONFIRMED |
| 15 | §2.4 | `reduce.py`'s own header states the one-place-arithmetic rule | reduce.py:1-8 states it verbatim ("the arithmetic lives here, once, and both import it") | CONFIRMED |
| 16 | §3.2 / §4.2 | `_cross_pin_verdict` at report.py:2234; unchanged iff \|Δmedian\| ≤ 2·max(σ_old, σ_new); range 2234-2248 | line 2234 is the `def`; body is `spread = max(...) * 2` / `if abs(diff) <= spread: return "unchanged (within spread)"`; the function ends at 2248 | CONFIRMED |
| 17 | §4.2 | R-DELTA-2's source is [B16] R4, `_cross_pin_info`, report.py:2447 | line 2447 is the `def`; its docstring says [B9] R8 but the selection-change block is explicitly commented `# [B16] R4 (pcrec I-7 §3 (a))` at 2486 and produces `selection changed (X → Y)` at 2531/2534. Attribution correct. | CONFIRMED |
| 18 | §4.2 | `delta_verdict` computed for `grain == "set"` alone, report.py:4143-4145 | `if grain == "set": info = _cross_pin_info(...)` occupies exactly 4143-4145; `_cross_pin_info` also self-guards on `rd.grain != "set"` | CONFIRMED |
| 19 | §4.3 | `_is_reference` at report.py:3153: id begins `libpcre2_` and contains `_interp-` | line 3153 is the `def`; body is `base.startswith("libpcre2_") and "_interp-" in base` | CONFIRMED |
| 20 | §4.3 | `_is_reference` is the denominator of `ratio_vs_baseline` | 4134-4138: `ref = next(... _is_reference ...)`; `ratio_b = r.median_ns / ref_ns`. Confirmed in data: `libpcre2_10.46_interp-caps-simdna` reads `ratio_vs_baseline = 1.000000` in the loglines report. | CONFIRMED |
| 21 | §4.3 | R-RANK-3: the reporter falls back to the best row when the reference is absent, report.py:4134-4135 | 4135 is `ref_ns = ref.median_ns if ref else (rankable[0][2].median_ns if rankable else None)`, and `rankable` is sorted by `median_ns` at 4133 | CONFIRMED |
| 22 | §4.4 | `_TIMER_FLOOR_NS = 20_000` at report.py:1927 | line 1927, exactly | CONFIRMED |
| 23 | §4.4 | applied by `_jitter_flag`, report.py:2150-2165; "20 microseconds, the clock's practical floor"; "a ratio that is mostly measuring the clock, not the compile" | `def _jitter_flag` is line 2150, `return f"{stddev_ns / median_ns:.3f}"` is 2165. Both quoted phrases appear verbatim in the docstring (2156, 2157-2158). | CONFIRMED |
| 24 | §4.4 | `_floor_mean_for` at report.py:2582-2595, arithmetic `median_ns / n` | 2582 is the `def`, 2595 the closing `return None`; body computes `red.median_ns / red.n_subjects` | CONFIRMED |
| 25 | §4.6 | `_DOMINANCE_SHARE = 0.90` at report.py:2326, `_dominant_subject`'s docstring ([B16] R7) | line 2326 exactly; the docstring's "a ratio between two such sums is a real number about a real total, and it is also a statement about ONE subject wearing the set's name" is the note's sentence verbatim | CONFIRMED |
| 26 | §4.1 | R-STATUS-4's diagnostic lives in `gave_up_summary`, report.py:4172 | the `did_not_compile` row at 4172-4173 puts `diag` in position 17 = `gave_up_summary` | CONFIRMED |
| 27 | §4.1 | "[B12] R10 emits one row per group" | code comment at 4164-4167 says exactly that | CONFIRMED |
| 28 | §4.1 | R-STATUS-9 reads `reduce.agreement_line` at reduce.py:351 | line 351 is `def agreement_line(block):` | CONFIRMED |
| 29 | §4.1 | constants `k=1.5, d_min=2, share_c=3, N ≥ 5 and odd` at reduce.py:246-250, measured over the store's 68 records at [B20] | 247-250 are the four constants; 246 is `TRIAL_AGREEMENT_RULE`. The "and odd" requirement is prose in the comment at 241-242, not a constant. "MEASURED over the store's 68 records" is stated at 243-244. Citation is one line wide and the "odd" half is not in the cited range. | **DISCREPANCY (D22, cosmetic)** |
| 30 | §4.1 | R-STATUS-9 fires on an agreement string starting `disagree` or `n/a` | `agreement_line` emits `n/a (%d trials)`, `disagree (...)`, `agree (...)`; `_agreement_display` (report.py:2788) additionally emits `n/a (v<schema>)` for pre-v1.4 records | CONFIRMED (definition matches the code's output space) |
| 31 | §4.1 | `_gave_up_cell_summary` renders `(smallest: <id>, <n> B)` ([B9] R7) | docstring at the `def` states `'gave-up: <CODE>x<n subjects> (smallest: <id>, <bytes> B)'`; data confirms `-2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B)` | CONFIRMED |
| 32 | §4.1 | R-STATUS-3 fires on "an `excluded` section row (a cell with `pass_rate` < 1)" | the `excluded` section is selected at report.py:4123-4124 by `r.expectation_failing or not n_timed`, **not** by `pass_rate`. In practice every committed excluded row has pass_rate < 1, but the parenthetical mis-states the reporter's own predicate. | **DISCREPANCY (D19, minor)** |
| 33 | §4.3 | the cross-pin pair is formed "within a (pattern, regime, form) group" | `_ranking_groups` (report.py:3161+) DELIBERATELY excludes `form` from the group key (its docstring says so in capitals, and R-BUCKET-FORM/-VSBEST depend on that). `_cross_pin_info` DOES key its previous-cell lookup on `form` (2481). The note uses "ranking group" for both meanings without distinguishing them. | **DISCREPANCY (D11, minor)** |
| 34 | §4.3 | the split regex `^pcrec_(?P<pin>[0-9a-f]+)_(?P<config>.*)$`, per record_schema.md §6.4 | record_schema.md §6.4 exists and is the composition rule. The reporter's own `_parse_testee_config` additionally strips an `@<compact-timestamp>` suffix (`--all-records`) before splitting; the note's regex does not. Latent only — no committed report carries an `@` in a testee id (checked all 42). The 14 four-segment `config_extra` ids parse identically under both. | **DISCREPANCY (D12, latent)** |
| 35 | §8 | a new target "beside `check-schema` / `check-harness` / `check-report`" | all three exist in the Makefile (35, 83, 128) and `check` = `check-schema check-harness check-report` (80). `check-interpret` absent, as the note says. | CONFIRMED |
| 36 | §8(4) | mirrors `schema/examples/bad/`'s pattern (**73 files**, each rejected for its named rule) | `schema/examples/bad/` holds 73 entries, of which **72** are `.jsonl` sabotage records; the 73rd is `CLAUDE.md`. | **DISCREPANCY (D9, minor)** |
| 37 | §3.1 | "the project already reads TOML in three places (`subbench.toml`, `testees/*/configs.toml`, `pyproject.toml`)" | `tomllib` is imported by `pcrecbench/subbench.py` (subbench.toml), `pcrecbench/adapters.py` (configs.toml), `pcrecbench/report.py:1091` (subbench.toml again), `bench/syntax/gen_patterns.py`. **Nothing in the repo reads `pyproject.toml` at runtime** — it is consumed by build tooling only. | **DISCREPANCY (D18, minor)** |
| 38 | §3.1 | BD4 fixes python ≥ 3.11, `tomllib` stdlib | decisions.md BD4 (2026-08-25) is the python-is-the-project-language decision; `pyproject.toml` pins ≥ 3.11 | CONFIRMED |
| 39 | §3.3 | pcrecbench/CLAUDE.md, [B14] R10: "bump whenever rendering changes, so two reports are never mistaken for each other" | verbatim at pcrecbench/CLAUDE.md:233-234, under the heading "## The reporter, [B14] follow-ups (2026-08-25)" (line 164) | CONFIRMED |

### Worked examples — Report A, `2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv`

| # | Location | Claim | What I found | Verdict |
|---|---|---|---|---|
| 40 | §4.1, §10 A.1 | header `source: … (14 record(s) matching this query); records: 9; superseded: 5` | byte-identical in the committed header | CONFIRMED |
| 41 | §4.1, §10 A.1 | 14 index rows for `email-specimen@0.1` on `budu-ryzen1600`, three `inconclusive-load`: interp @ 17:34:02Z, `pcrec_692c2e8_auto-caps-simdna` @ 17:51:31Z, `pcrec_692c2e8_auto-nocaps-simdna` @ 17:55:34Z | 14 rows exactly; the three ids, statuses and timestamps match to the second | CONFIRMED |
| 42 | §4.1 | each superseded by a `measured` record of the same testee "at 22:1x-22:2x" | interp @ 22:16:51Z, auto-caps @ 22:24:22Z, auto-nocaps @ 22:28:40Z | CONFIRMED |
| 43 | §9.2 | the three record ids rendered in full (e.g. `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T173402Z`) | byte-identical to the index basename | CONFIRMED |
| 44 | §9.2 | stamp `reporter: v12 (2026-09-02)` | the committed TSV header reads `reporter: v12 (2026-09-02)` | CONFIRMED |
| 45 | §9.2 | R-STATUS-5 renders 14 candidates / 9 included / 5 superseded / 0 newer / 0 invalid | header: `records: 9; excluded_invalid: 0; superseded: 5; newer_not_measured: 0` | CONFIRMED |
| 46 | §9.2, §10 A.7 | R-STATUS-6: schema versions `1.1, 1.2` | header `schema_versions: 1.1,1.2` | CONFIRMED |
| 47 | §9.2 | R-STATUS-7 did-not-fire, "mixed_x13: False" | header `mixed_x13: False`. (3 of the 42 reports DO carry `True`, so the rule is not dead.) | CONFIRMED |
| 48 | §9.2 | R-STATUS-9 did-not-fire, "every record reads `agree` or `n/a (v1.x)`" | all 9 records read `n/a (v1.1)` or `n/a (v1.2)` — which **starts with `n/a`**, and §4.1 defines R-STATUS-9 as firing on `disagree` **or `n/a`**. Under the note's own rule definition R-STATUS-9 fires **9 times** on this report, not zero. §10 C.6's use of the same rule (all six syntax records read `agree (…)` → must not fire) is consistent with the definition; only this row is not. | **DISCREPANCY (D2)** |
| 49 | §9.2, §10 A.3 | 13 excluded cells, with the three give-up summaries quoted | exactly 13 `excluded` rows; `-2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B)`, `-3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B)`, `-4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B)` all byte-identical | CONFIRMED |
| 50 | §9.2 | the three quoted excluded rows: pass-rate 0.6667 / 0 wrong / 5 give-ups; 0.9412 / 25 give-ups; 0.6667 / 5 give-ups | all three match column-for-column | CONFIRMED |
| 51 | §9.2 | R-STATUS-3 rendered as "5 give-up(s)" | the §4.1 template declares `{n_gave_up} give-up trial(s)`; the §9.2 render says `give-up(s)`, and the trailing note claims "the template prints both, in those words" | **DISCREPANCY (D21, cosmetic)** |
| 52 | §9.2, §10 A.3b | R-STATUS-12: `t-c-long-atom-run` (1,048,576 B) STEPS on `factored`, WORK on `orig`, `pcrec_692c2e8_vm-caps-simdna`, large-subject-throughput | both rows present and exactly as described | CONFIRMED |
| 53 | §3.2, §4.2, §10 A.5 | R-DELTA-1: factored/short-search/plain/vm rank 5 median 69,537.5 ns `faster ×1.19`; orig/compliance/whole-subject/vm rank 2 median 80,227.6 ns `faster ×1.26` | 69537.547361 and 80227.619276, ranks 5 and 2, verdicts exact | CONFIRMED |
| 54 | §10 A.5 / §9.2 | those are "the two" R-DELTA-1 firings | the rule's own predicate `^(faster\|slower) ×` also matches a **third** row: `orig` / match-compliance / whole-subject / `pcrec_692c2e8_auto-nocaps-simdna`, rank 4, `faster ×1.00`. Neither §9.2 nor §10 A.5 accounts for it. | **DISCREPANCY (D17)** |
| 55 | §4.2, §9.2, §10 A.2 | R-DELTA-2 fires six times; `factored` under `auto`, three regimes × two configs, ranks 1 and 2 in each | exactly 6 cells carry `selection changed (vm → dfa)`, at ranks 1 and 2 in each of the three regimes, on `auto-caps-simdna` and `auto-nocaps-simdna` | CONFIRMED |
| 56 | §4.2 | R-DELTA-2's worked example: factored/short-search/plain/`auto-nocaps`, rank 1 | exact | CONFIRMED |
| 57 | §10 A.2 | "large-subject-throughput ranks 1 and 2, **the latter pair** also carrying `now measured (was: gave-up)`" | **four** cells carry it, not two: large-subject-throughput ranks 1 and 2 AND match-compliance whole-subject ranks 1 and 2 | **DISCREPANCY (D4)** |
| 58 | §4.2 table, §10 A.2 | R-DELTA-3 fires on `^now measured \(was: ` | across all 42 reports the delta_verdict value space is exactly: `unchanged (within spread)` (9,900 rows), `faster ×N` (5,928), `slower ×N` (2,280), `selection changed (vm → dfa); now measured (was: gave-up)` (24), `selection changed (vm → dfa)` (12), `selection changed (dfa → vm)` (6). **`now measured` never appears at the start of a string.** report.py:2530-2532 prefixes it whenever a selection change coincides. The start-anchored predicate therefore fires on nothing in the corpus, while §10 A.2 requires it to fire on those cells. (A bare `now measured (was: …)` IS reachable — report.py:2523 with no selection change — just not in any committed report.) | **DISCREPANCY (D5)** |
| 59 | §4.2 | R-DELTA-1 and R-DELTA-2 never co-fire | holds, because R-DELTA-1's regex is start-anchored and every selection-change string begins `selection changed` | CONFIRMED |
| 60 | §4.6, §10 A.6 | R-BUCKET-FORM: `orig` / match-compliance ranks nine rows, seven `whole-subject`/`separate artifact` (all pcrec), two `plain`/`same program` (both libpcre2) | 9 rows, 7 and 2, exactly as described; `factored` / match-compliance is 3 + 2 → both facts present | CONFIRMED |
| 61 | §9.2 | R-BUCKET-VSBEST: `orig` / short-subject-search / plain carries 2 pin slugs (8da6120, 692c2e8) | both pins present in that group | CONFIRMED |
| 62 | §10 A.4 | vm-in: orig/short-search ranks vm-in 6 (12,546.19) and vm 7 (28,996.91); orig/compliance ranks vm-in 1 (62,732.30) and vm 2 (80,227.62) | 12546.190865 / 28996.905722 / 62732.301756 / 80227.619276, at ranks 6, 7, 1, 2 | CONFIRMED |
| 63 | §9.2 | R-FLOOR-1: orig / plain / `libpcre2_10.46_interp-caps-simdna` reads `timer-floor` | present; 2 timer-floor rows in this report (factored and orig, both interp) | CONFIRMED |
| 64 | §9.2 | R-FLOOR-2 did-not-fire, "no `role: floor` pattern in email-specimen@0.1" | `bench/email/subbench.toml` **does** declare `role = "floor"` (pattern `floor`, [B15]) — and the directory's only sidecar is at `version = "0.2"`. Under v1's own Q1 mechanism (read `bench/<dir>/subbench.toml`), a floor pattern IS found; the real reason the rule cannot fire is that the 2026-08-25 records predate it, so the report has no `floor` rows (its only patterns are `factored` and `orig`). The stated reason is false about the tree as it stands. | **DISCREPANCY (D6)** |

### Worked examples — Report B, `2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv`

| # | Location | Claim | What I found | Verdict |
|---|---|---|---|---|
| 65 | §4.3, §10 B.1 | R-RANK-1: `cls-upto-8192`/match-compliance/whole-subject/`auto-caps-simdna`: 334fd10e 1.788 → d34c9131 0.269 | `ratio_vs_baseline` 1.788241 and 0.269358 | CONFIRMED |
| 66 | §4.2, §10 B.2 | R-DELTA-2 on that same cell: `selection changed (dfa → vm)`, rank 3 | exact, on `pcrec_d34c9131_auto-caps-simdna` rank 3 | CONFIRMED |
| 67 | §10 B.3 | R-BUCKET-SPAN: `cls-upto-1024`/large-subject-throughput/plain `vm-in` `faster ×1.53`; short-subject-search `faster ×1.25` | both exact | CONFIRMED |
| 68 | §4.6, §10 B.4 | R-BUCKET-VSBEST: `cls-upto-1024`/short-search: 334fd10e_auto rank 1 @ 989.820, d34c9131_auto rank 2 @ 998.441, Δ `slower ×1.01`; three pin slugs in the group | 989.819865 / 998.441155, ranks 1 / 2, verdict exact; slugs 288d505, 334fd10e, d34c9131 all present | CONFIRMED |
| 69 | §4.6 | those testees named `pcrec_334fd10e_auto` / `pcrec_d34c9131_auto` | the actual ids are `…_auto-caps-simdna` | **DISCREPANCY (D20, cosmetic)** |
| 70 | §10 B.5 | R-RANK-1 on `dig-exact-8`, `dig-upto-8`, `dig-exact-16`, `dig-upto-16`, `dig-exact-32`, config `vm-in-caps-simdna`, each crossing 1.0 between 288d505 and d34c9131 | all five: 288d505 reads 1.081 / 1.058 / 1.591 / 1.603 / 1.770 and d34c9131 reads 0.643 / 0.620 / 0.946 / 0.951 / 0.926 | CONFIRMED |
| 71 | §4.3 | second R-RANK-1 instance: loglines repin-36d5963, `stack-frame`/short-search/plain, `auto-caps-simdna`: 2.698 → 0.155 | 2.697803 and 0.155111 | CONFIRMED |

### Worked examples — Report C, `2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv`

| # | Location | Claim | What I found | Verdict |
|---|---|---|---|---|
| 72 | §4.1, §10 C.1 | 172 `did_not_compile` rows | exactly 172 (reducing to 60 distinct (pattern, testee) pairs) | CONFIRMED |
| 73 | §4.1 | the quoted diagnostic `pcrec: module 'conditionals' is enabled but (?(...) is not implemented yet (pattern offset 8)` on `pcrec_d34c9131_auto-caps-simdna` | byte-identical, on pattern `cnd-group` | CONFIRMED |
| 74 | §10 C.2 | 23 excluded cells; `rec-1`/large-subject-throughput at pass_rate 0.0000 with 15 wrong on **five** testees; `asr-k-uc`/match-compliance/whole-subject at 0.9762 with 5 wrong on **four** pcrec arms | exactly 23; `rec-1` on 5 testees (jit + 4 pcrec) at 0.0000/15 wrong; `asr-k-uc` on 4 pcrec arms at 0.9762/5 wrong | CONFIRMED |
| 75 | §4.6, §10 C.3 | R-BUCKET-KB's KB-13 signature: "a `large-subject-throughput` cell whose exclusion reads `expected N non-overlapping match(es); observed M`" | the string `non-overlapping` occurs **0 times** in the report `.tsv` and **0 times** in the `.md`. It lives in `docs/dev/known_issues.md:489` ("expected 116 non-overlapping match(es); observed 5") and in the record JSONL — which §2.4 explicitly excludes from `interpret`'s inputs. The `gave_up_summary` column on those rows reads `0`. The half of the signature that IS expressible from the TSV is `n_gave_up == 0 && n_wrong > 0` in the throughput regime. | **DISCREPANCY (D7)** — the note flags this risk in prose ("if R-BUCKET-KB cannot express those two signatures from TSV columns alone…"), but the signature as written is stated as fact about the report and is not. |
| 76 | §10 C.3 | KB-14's signature "a whole-subject span mismatch on pcrec only" | expressible: the `asr-k-uc` / `rec-r-uc` whole-subject exclusions are on the four pcrec arms and no libpcre2 arm. KB-13/KB-14/KB-15 all exist in known_issues.md (484/541/578). | CONFIRMED |
| 77 | §4.4, §10 C.5 | 190 compile rows read `timer-floor` | exactly 190 (95 patterns × the two libpcre2 testees) | CONFIRMED |
| 78 | §4.4 | "against **26/23/23/23** carrying real ratios" | **644** compile rows carry a real ratio, split 161 / 161 / 161 / 161 across the four pcrec testees. `26/23/23/23` are the frequencies of the four most common ratio VALUES (0.025, 0.032, 0.029, 0.018) — not a count of rows carrying ratios, and not a per-testee split. | **DISCREPANCY (D3)** |
| 79 | §4.4, §10 C.4 | R-FLOOR-2: `anc-caret`/short-search/`vm-caps-simdna` rank 1, median 246.458 over n=42 → 5.868 ns/subject; `floor` on the same testee/regime 800.099 over 42 → 19.050; ratio 0.308× | 246.457657 / 42 = 5.8680; 800.098671 / 42 = 19.0500; 5.868/19.050 = 0.3080. Every digit checks out, including the rank and n. | CONFIRMED |
| 80 | §10 C.6 | all six records read `agree (0 of N groups …)` | all six do (`0 of 282`, `0 of 282`, `0 of 239` ×4) | CONFIRMED |
| 81 | §0 | the syntax ledger is 1,085 lines | `wc -l` = 1085 | CONFIRMED |

### §10's census and corpus claims

| # | Location | Claim | What I found | Verdict |
|---|---|---|---|---|
| 82 | §10 | "the corpus is now 42" report TSVs | 42 `.tsv`, 85 `.md` (42 + 42 subject-grain + CLAUDE.md) | CONFIRMED |
| 83 | §4.3 | R-RANK-1 census: **9 of 42** files, **69** (pattern, regime, form, config) pairs; altwide-after-334fd10e 40; bounded@0.2 after-a7e0bdf 7; bounded@0.3 after-d34c9131 7; loglines 4 + 4; email@0.2 2; loglines after-1989c62 2; bounded@0.1 repin-96e44c2 2; bounded@0.3 step2-after-288d505 1 | Re-derived independently over all 42 files by the note's own predicate: **9 files, 69 pairs**, and every per-file figure matches exactly (40 / 7 / 7 / 4 / 4 / 2 / 2 / 2 / 1, same files). This is the note's most falsifiable claim and it reproduces to the pair. | CONFIRMED |
| 84 | §11 Q2 | no committed report group has a subject-grain TSV | 42 `*.subject-grain.md`, 0 `*.subject-grain.tsv` | CONFIRMED |

### §6 — the predictions claim

| # | Location | Claim | What I found | Verdict |
|---|---|---|---|---|
| 85 | §6.1 | "**No machine-readable prediction exists anywhere in this repository.**" | Re-run and widened: `docs/dev/predictions/` does not exist; no `.tsv`/`.toml`/`.json` in the repo holds predictions (the `predict*` hits in `list_axes.tsv`, `list_limits.tsv`, `list_definitions.tsv`, `configs.toml` and three `subbench.toml`s are all the word "predicate" or prose comments). Headline claim CONFIRMED. | CONFIRMED |
| 86 | §6.1 | the cited grep `grep -rn "prediction" docs/dev/ pcrecbench/ schema/` returns the enumerated four things | the cited paths do **not** include `bench/`, so `bench/syntax/NOTES.md`'s P1-P13 is not among that grep's results though the note lists it. The grep also returns one hit the note does not list: `pcrecbench/harness.py:353` (prose, "the prediction is made here in exactly the terms…"). `schema/` returns nothing. | **DISCREPANCY (D13, cosmetic)** |
| 87 | §6.2 (1) | "cls-upto-2048 ÷ 1024 stays in 0.90-1.10" (pcrec I-38), scored 1.986 → 1.987 | ledger `2026-09-05-opt5-step2-after-288d505.md:659` reads "`cls-upto-2048 ÷ cls-upto-1024` at r-01024 **1.986 → 1.987** (target 0.90–1.10) — REFUTED" | CONFIRMED |
| 88 | §6.2 (2) | "letters 3.65-6.05 → 1.76-2.00" (pcrec I-27, [OPT-5] STEP 1) | ledger `2026-08-31-opt5-step1-acceptance-a7e0bdf.md:54` reads "`auto ÷ vm` fell from 3.65–6.05 to 1.76–2.00" | CONFIRMED |
| 89 | §6.2 (3) | "no compile time beyond ×10 the median on any compiled testee" (NOTES P13), scored CONFIRMED at worst ×2.08 | NOTES.md:340-343 states P13 with the ×10 band; the syntax ledger's scorecard row 652 is that sentence verbatim with "**CONFIRMED** \| worst ×2.08" | CONFIRMED |
| 90 | §4.5 | "`feedback_…-repin.md` §3's **eighth** row is literally 'UNCOVERED by any prediction'" | it is the **seventh** row (`interp compile-cost variance`); the eighth is `JIT absent on factored/throughput (from U1) \| CONFIRMED (5/5)`. The table does have eight data rows, as §6.1/§6.5 say. | **DISCREPANCY (D8, minor)** |

### Quoted feedback and pointer files

| # | Location | Claim | What I found | Verdict |
|---|---|---|---|---|
| 91 | §4.1, §4.2, §4.4, §4.6, §10 | five verbatim quotations from the two feedback files | all five byte-identical: "the same 1 MB subject gives STEPS (-2) on factored-VM and WORK (-4) on orig-VM — different budgets bind on the two spellings" (repin-v2:69-70); "a cross-pin VM speedup with no attributed cause" (:64); "flagged as loudly as a regression" (:102); "the interpretive rows have stddev ≈ median (12.3 K vs 13.5 K)" (:47); "State 'same program / separate artifact' as a column; the 'regime artifact' bucket IS that fact, not a footnote" (repin.md §2); and R-FLOOR-3's "12..109 µs over 10 trials is timer jitter — the report should say so rather than print a stddev larger than the median" (repin.md:81) | CONFIRMED |
| 92 | §4.6 | R-BUCKET-SPAN / R-BUCKET-VSBEST sources in `reports/CLAUDE.md` | "The bounded `vm-in` row's Δ partner is 288d505, not 334fd10e" (:167) and "spans THREE abi steps (16 → 22 → 23)" (:169) verbatim; the `vs best` reader's caveat at :170-173 and :466-471; the "8192 inversion … was REFUTED" passage at :1444-1455, attributing it to the a7e0bdf ledger — all as cited | CONFIRMED |
| 93 | §1.1, §7.3 | `bench/syntax/NOTES.md` R2 (×2 / ×20 vs the JIT), R4 (family median ×3), R7 ([0.7, 1.4]); `outbox_to_pcrec.md`, `known_issues.md`, `upstream_findings.md` (`Un`), `docs/dev/ledgers/` all exist | NOTES.md:220-224 (R2), :242-246 (R4), :258-260 (R7) match the note's paraphrases exactly; all four pointer targets exist (`upstream_findings.md` U5 present, `outbox_to_pcrec.md` O-22 present) | CONFIRMED |

### Internal consistency of §5 / §7.1 / §8(5) against §9.2's output specification

These are not source-citation errors, but they are *falsifiable claims the
note makes about itself*, so they belong in this lens.

| # | Location | Claim | What I found | Verdict |
|---|---|---|---|---|
| 94 | §5 vs §9.2 | "**A rule is never silently absent** … plus the rules that did NOT fire" | §9.2's "Rules that did not fire" table omits **eight** rules that do not fire on that report: R-STATUS-1, R-STATUS-8 (header reads `worst_other_core_busy: n/a`), R-STATUS-10, R-DELTA-3 (see D5), R-RANK-2, R-RANK-3, R-FLOOR-3 (max jitter in that report is 0.645), R-BUCKET-SPAN. The `…` abridgement markers appear only inside firing lists, and §9.2 declares itself "a specification of output, not an example of style". | **DISCREPANCY (D15)** |
| 95 | §7.1 / §8(5) vs §9.2 | "no code path by which `interpret` can emit a string that is not `stamp \| heading \| template output \| link \| did-not-fire row`", enforced by §8(5)'s no-prose check | §9.2's specified output contains at least six sentences that are not any template shown in §4: R-DELTA-1's "Source: report.py `_cross_pin_verdict` ([B9] R8) — unchanged iff…", R-DELTA-2's "A ratio between two different engines is not computed ([B16] R4).", R-FLOOR-1's "(min under 20 µs, report.py `_TIMER_FLOOR_NS`); the ratio measures the clock, not the compile", the whole R-BUCKET-FORM and R-BUCKET-VSBEST bodies (§4.6 declares no templates at all), and the free-standing parenthetical after R-STATUS-3 ("`n_gave_up` counts TRIALS; the `×N` … counts SUBJECTS"). §8(5) as specified would fail the very document §9.2 says the tool must produce. | **DISCREPANCY (D14)** |
| 96 | §4.2 vs §4.5 | R-PRED-4 "(= R-DELTA-4)" | the two definitions differ in scope: §4.2's R-DELTA-4 is "a **R-DELTA-1** firing with NO prediction covering the cell"; §4.5's R-PRED-4 is "a **R-DELTA-1 / R-RANK-1 / R-FLOOR-2** firing that no prediction's selector covers". They are declared the same rule but are not the same rule, and §3.2's one-function-per-id contract cannot hold for two ids. | **DISCREPANCY (D16)** |
| 97 | §4.6 | R-BUCKET-DOMINATED "**Needs a subject-grain TSV** (§10 Q2)" | Q2 is in **§11**, not §10 | **DISCREPANCY (D10, cosmetic)** |

### `docs/design/CLAUDE.md`'s new entry (brief item 6)

Read against the note it describes. Every substantive statement checks
out: DESIGN ONLY / no code / no catalogue file / no skill (verified —
`catalogue/`, `pcrecbench/interpret.py`, `.claude/skills/pcrec-bench-interpret/`,
`docs/dev/predictions/` and `reports/*.interpretation.md` all absent, and
`check-interpret` appears zero times in the Makefile); the two inputs and
"never the markdown"; the sidecar path; `catalogue/rules.toml` MAJOR.MINOR
and the regeneration rule; the six classes; the three threshold-source
examples (`_cross_pin_verdict`, `_jitter_flag`'s `timer-floor`,
`agreement_line`); the three firewall properties; the predictions path and
"none exists today, checked"; `make check-interpret`'s five sections and
the `schema/examples/bad/` mirror; §10's three named reports; and "Eight
open questions … incl. Q4, a flagged charter deviation" — §11 does carry
exactly Q1-Q8 and Q4 is the §7.4 deviation. **No discrepancy.** One
inherited inaccuracy only: the entry repeats the note's "mirroring
`schema/examples/bad/`" framing, and it repeats "one sabotage fixture +
one minimal-diff control per rule", both of which are the note's own words
and accurate as descriptions of the note.

---

## Summary

I re-derived every numeric and citation claim in `interpreter_v1.md`
against the source rather than trusting its own footnotes: all sixteen
cited `report.py` / `reduce.py` line ranges were opened and counted (every
one lands on the exact construct named — `_cross_pin_verdict` at 2234-2248,
`_jitter_flag` at 2150-2165, `_floor_mean_for` at 2582-2595, `_is_reference`
at 3153, `_TIMER_FLOOR_NS` at 1927, `_DOMINANCE_SHARE` at 2326,
`agreement_line` at 351, `render_tsv`'s four cited spans at 4065/4068-4091/
4092-4094/4100-4107/4143-4153/4172, and `REPORTER_VERSION` at 896); every
worked-example row was re-extracted from the committed TSVs; and the §4.3
census was re-derived by an independent script over all 42 report files,
where it reproduces to the pair (9 of 42 files, 69 pairs, and every one of
the eight per-file counts). The note's arithmetic is, with one exception,
exact to the last printed digit — 246.457657/42 = 5.868, 800.098671/42 =
19.050, 0.308×; 1.788241 → 0.269358; 989.819865 / 998.441155; 14 candidates
/ 9 included / 5 superseded; 13 and 23 excluded cells; 172 did-not-compile
rows; 190 timer-floor rows; 1,085 ledger lines. Of the 22 discrepancies,
five are substantive and should be dispositioned before implementation:
**D1** (the record row's agreement string is in `value`, not
`gave_up_summary` — the note has inherited report.py's own stale comment,
and contradicts its own §4.1 inputs); **D2** (§9.2 says R-STATUS-9 does not
fire on a report where all nine agreement strings begin `n/a`, which
§4.1's definition says fires); **D3** (the 26/23/23/23 real-ratio figure is
wrong by an order of magnitude — 644 rows, 161 per pcrec testee); **D5**
(R-DELTA-3's start-anchored predicate matches nothing in the corpus,
because every `now measured (was: gave-up)` is a suffix of a compound
selection-change string, yet §10 A.2 requires it to fire); and **D7**
(R-BUCKET-KB's KB-13 signature quotes a string that occurs zero times in
the report TSV and MD — it lives in the record JSONL, which §2.4 excludes).
D4, D14, D15, D16 and D17 are internal-consistency defects in the §9.2
output specification and the rule table; the remaining twelve are cosmetic
(a wrong section cross-reference, a row ordinal, a fixture count off by the
directory's CLAUDE.md, abbreviated testee ids, a grep path that does not
cover a file it lists). Nothing in the note is invented: every report row,
timestamp, record id and ledger quotation I checked exists and reads as
claimed.
