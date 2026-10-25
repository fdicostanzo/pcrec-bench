# b140set report ([B140] build-order step 1: `bench/subst/`, lane b140set2, 2026-10-24/25)

Branch `lane/b140set` (worktree `worktrees/b140set`). No timing run, no `store/`/`reports/` write, no install, no download. Scratch: `/var/tmp/pcrecbench/b140set/` (subjects, tune logs, check logs).

## Charter-vs-committed checklist

| item | committed artifact / status |
|---|---|
| Tuning, at most two more runs | Run 7 had been killed; `best.json` held its best (verified identical to the knobs shown at 288). It was applied and calibrated (2 FAIL: p99 mid -12.8 %, status_304 -12.8/-11.5 %), then ONE more run (run 8, seed 8, 45 min, `tune8.log`, score 12.83 -> 10.86) was made: 2 FAIL remained (p99 mid -11.9 %, status_304 unchanged). Tuning stopped; knobs applied in `bench/subst/logsim.py` (`K`). |
| Stated deviations | `calibrate.STATED_DEVIATIONS` (verdict `DEVIATION` inside a stated bound, FAIL beyond), `bench/subst/NOTES.md` "Stated deviations" (value, tolerance, why), the archive's `calibration.tsv`. |
| 1. Calibration archive | `docs/dev/measurements/2026-10-24-b140-subject-calibration/` (`calibration.txt` = source header incl. reference sha256 f15c31e9...64ef, commit bc53b584, blob 94bf224f + verbatim stdout; `calibration.tsv`; `reproduce.sh`); `docs/dev/measurements/CLAUDE.md` row. `gen_subjects.py --check` re-runs the first window (`--full`: the middle one too) and prints `calibration SKIPPED -- reference ... absent` by name when the reference is missing (tools/check_subst.py reports it as an `ok SKIPPED BY NAME`). Verified: `--check --full` printed `calibration PASS (30 rows, 0 FAIL, window(s): first10k + mid10k)`. |
| 2. Subject regenerated, manifest committed, subject gitignored | `bench/subst/manifest.tsv`, `planted.tsv`; `bench/*/subjects/` already ignored (the 362 MB file lives at `/var/tmp/pcrecbench/b140set/subjects/` via `PCRECBENCH_SUBST_SUBJECTS`). `gen_subjects.py --check --full`: regenerated acc-small + acc-main match the manifest, the on-disk files match, acc-small is a byte prefix of acc-main. acc-small 3,929,818 B sha256 7f9724543efa7f2b..., acc-main 361,986,301 B sha256 a9b0a4cc17e65d3a... (not 320 MB: NOTES deviation 9). |
| 3. Expectations via the oracle | `bench/subst/expectations.tsv`, 16 rows (8 cases x 2 subjects): nsubst, out_bytes, out_sha256, plus an oracle-independent count per row (all equal); case 7 ONE pass only (brief change after I-158: 7a/7b/7c removed, composition control dropped); case 6 `unsupported` strictly for non-case-operator dialects in `divergences.tsv`. Table below. |
| 4. Densities in NOTES.md before timing; divergences complete | NOTES.md "Densities" (stated) + the measured planted counts paragraph; `divergences.tsv` (38 rows: cases 1-5b agree for everyone, case 6 split, case 7 per competitor; pcrec 7 `pending` row to be set `agrees` at the [M4-SUBST] re-pin). |
| 5. `make check-harness` slice | Full run: **857 checks passed, 0 FAILED** (rc 0, log `/var/tmp/pcrecbench/b140set/checkh2.log`, ~35 min wall, box otherwise idle; no inconclusive-load item, not a timing run). The subst slice (`tools/check_subst.py`) is 34 checks, 0 bad; it includes the calibration first-window PASS, the acc-small expectation re-derivation, and python/sed/perl against the divergence table. Two real bugs in the slice were found and fixed (see below). Not independently verified: the one-pass case 7 on pcrec (O-106). |
| 6. CLAUDE.md files | `bench/subst/CLAUDE.md` (status, subjects dir), `docs/dev/measurements/CLAUDE.md` (archive row). `tools/` and `docs/dev/lanes/` CLAUDE.mds were not changed by this lane beyond file edits to an existing, already-listed `check_subst.py`. |

### Slice bugs found by the first full run (fixed, committed)

1. `tools/check_subst.py` section 2 compiled `(a)(b)?` for a template that references group 3 -> libpcre2 -49 `unknown substring`, which crashed `make check-harness` with a traceback (rc 2) before it reached the later checks. Pattern is now `(a)(b)?(c)?` and the render passes `extended=True`.
2. Section 8 reported GNU sed on case 7 as `unsupported:no-conditional` (the template failed to render first) where `divergences.tsv` says `unsupported:pattern-syntax`. The pattern is read first, so the check now probes sed with the pattern alone and reports `pattern-syntax` when sed refuses it. The table was right, the check's order was wrong.

## Final calibration table (knobs after tuning run 8)

| metric | reference | gen_first10k | gen_mid10k | dev_gen_first10k | dev_gen_mid10k | tolerance | verdict |
|---|---|---|---|---|---|---|---|
| entropy_bits_per_byte | 5.49409 | 5.44646 | 5.44997 | -0.9% | -0.8% | +-5% | PASS |
| gzip6_ratio | 0.0999431 | 0.0972136 | 0.0964831 | -2.7% | -3.5% | +-5% | PASS |
| xz6_ratio | 0.0549572 | 0.0574497 | 0.0571217 | +4.5% | +3.9% | +-5% | PASS |
| zstd3_ratio | 0.0821828 | 0.0856649 | 0.085374 | +4.2% | +3.9% | +-5% | PASS |
| linelen_mean | 237.079 | 223.869 | 223.572 | -5.6% | -5.7% | +-10% | PASS |
| linelen_p10 | 159 | 163 | 165 | +2.5% | +3.8% | +-10% | PASS |
| linelen_p50 | 232 | 219 | 219 | -5.6% | -5.6% | +-10% | PASS |
| linelen_p90 | 315 | 295 | 295 | -6.3% | -6.3% | +-10% | PASS |
| linelen_p99 | 445 | 426 | 392 | -4.3% | -11.9% | +-10% | DEVIATION |
| unparsed_lines | 1 | 0 | 0 | -100.0% | -100.0% | info | INFO |
| unique_ips_per_10k | 1753 | 1650 | 1598 | -5.9% | -8.8% | +-10% | PASS |
| unique_paths_per_10k | 1498 | 1570 | 1541 | +4.8% | +2.9% | +-10% | PASS |
| unique_agents_per_10k | 558 | 569 | 546 | +2.0% | -2.2% | +-10% | PASS |
| unique_referrers_per_10k | 628 | 623 | 578 | -0.8% | -8.0% | +-10% | PASS |
| ip_run_mean | 2.31834 | 2.54907 | 2.53872 | +10.0% | +9.5% | +-10% | PASS |
| status_200_frac | 0.912591 | 0.9194 | 0.9117 | +0.7% | -0.1% | +-10% | PASS |
| status_304_frac | 0.0445045 | 0.0388 | 0.0394 | -12.8% | -11.5% | +-10% or +-0.3pp | DEVIATION |
| status_404_frac | 0.0213021 | 0.0202 | 0.0221 | -5.2% | +3.7% | +-10% or +-0.3pp | PASS |
| status_301_frac | 0.0164016 | 0.0141 | 0.0146 | -14.0% | -11.0% | +-10% or +-0.3pp | PASS |
| case_1-literal_per_line | 0.93 | 0.9152 | 0.8763 | -1.6% | -5.8% | +-10% | PASS |
| case_2-rare_per_line | 0 | 0.0001 | 0.0001 | n/a | n/a | by design | BY-DESIGN |
| case_3-dense_per_line | 25.1154 | 24.3476 | 24.2099 | -3.1% | -3.6% | +-10% | PASS |
| case_4-reorder_per_line | 1 | 1 | 1 | +0.0% | +0.0% | by design | BY-DESIGN |
| case_5-mask-ipv4_per_line | 1.0213 | 1.0203 | 1.0181 | -0.1% | -0.3% | +-10% | PASS |
| case_5b-mask-email_per_line | 0.0198 | 0.0462 | 0.0483 | +133.3% | +143.9% | by design | BY-DESIGN |
| case_6-upper_per_line | 0.5598 | 0.5768 | 0.5749 | +3.0% | +2.7% | +-10% | PASS |
| case_7-url-tld-fix_per_line | 0 | 0.0144 | 0.0155 | n/a | n/a | by design | BY-DESIGN |
| case_7a-url-tld-value_per_line | 0 | 0.0073 | 0.0066 | n/a | n/a | by design | BY-DESIGN |
| case_7b-url-tld-insert-qmark_per_line | 0 | 0.0028 | 0.0047 | n/a | n/a | by design | BY-DESIGN |
| case_7c-url-tld-insert-amp_per_line | 0 | 0.0043 | 0.0042 | n/a | n/a | by design | BY-DESIGN |

Deviations: `linelen_p99` (mid window -11.9 % vs +-10 %, bound 13 %) and `status_304_frac` (-12.8 % / -11.5 %, 0.57 / 0.51 pp vs +-10 % or +-0.3 pp, bound 14 %). Reasons are in NOTES.md. All other non-exempt rows PASS on both windows (closest: xz +4.7 % of 5 %, ip_run_mean +10.0 % of 10 % on the first window, listed PASS at its rounded value).

## Expectations per case

| case | subject | nsubst | out_bytes | out_sha256 | independent count (basis) |
|---|---|---|---|---|---|
| 1 | acc-small | 15505 | 3836788 | `adddea6b349655f1` | 15505 (bytes.count) |
| 2 | acc-small | 2 | 3929792 | `ea67968e30b288c9` | 2 (planted) |
| 3 | acc-small | 426622 | 3385182 | `82435fd1b25166b5` | 426622 (digit-run transitions) |
| 4 | acc-small | 17500 | 3929818 | `a4f053b6bd491ec2` | 17500 (newline count) |
| 5 | acc-small | 17785 | 3823488 | `ade539918f5507dc` | 17785 (python re) |
| 5b | acc-small | 830 | 3918120 | `b4910705dad7e380` | 830 (python re) |
| 6 | acc-small | 10236 | 3929818 | `9092731349312891` | 10236 (python re) |
| 7 | acc-small | 283 | 3930988 | `247378b400f06379` | 283 (planted) |
| 1 | acc-main | 1411976 | 353514445 | `461dc93c83463524` | 1411976 (bytes.count) |
| 2 | acc-main | 160 | 361984203 | `0b9c3be4cfc728e3` | 160 (planted) |
| 3 | acc-main | 39337500 | 311463435 | `8e72938fde1567f7` | 39337500 (digit-run transitions) |
| 4 | acc-main | 1600000 | 361986301 | `6e64a063d97525db` | 1600000 (newline count) |
| 5 | acc-main | 1635130 | 352097319 | `6ccc00dabdc1b9e1` | 1635130 (python re) |
| 5b | acc-main | 80123 | 360838508 | `4b66e137a1e58cae` | 80123 (python re) |
| 6 | acc-main | 928237 | 361986301 | `e328833e09d745bc` | 928237 (python re) |
| 7 | acc-main | 23986 | 362091138 | `80c1df04f414bfb7` | 23986 (planted) |

Planted densities (acc-main): case 2 160 (1 per 10,000 lines), case 5b 80,123 (5.01 % of lines), case 7 23,986 edits of 40,095 planted URLs (9,920 wrong + 6,048 missing-no-query + 8,018 missing-with-query; 16,109 already correct), case 4 one per line.

## Predictions check (NOTES P1-P4)

P1 (oracle == independent count): holds on all 22 rows. P2 (case 4 = lines, case 2 = planted, case 7 = the three planted edit populations): holds. P3 (size): cases 4 and 6 keep the length exactly (3,929,818 / 361,986,301 B), cases 1, 2, 3, 5, 5b shorten, case 7 lengthens by 1,170 B (small) / 104,837 B (main) = 4.4 B per edit on average. P4 (sed/perl/python agree where they can express): verified on acc-small by the slice.

## OWED

* Case 7 on pcrec: O-106 is answered (I-158; pcrec pin 9ae59f5d4 = [M4-SUBST], recorded in NOTES.md). The `divergences.tsv` row for pcrec case 7 is still `pending`; flip it to `agrees` after the later re-pin lane verifies it. OWED to the manager.
* The sidecar rename `subst.toml` -> `subbench.toml`, driver `--mode subst`, TOOLS runner, record schema regime use (steps 2-4 of section 10): not this lane.
* Reference file is not committed by design; anyone re-running the calibration needs `bench/subst/fetch_reference.sh` (not run here; the file was already at `build/subst-ref/apache_logs` in this worktree, sha256 verified by `calibrate.load_reference` on every run).

## Amendment (brief change, I-158)

Case 7 is one pass only. Removed: `cases/7a-*`, `7b-*`, `7c-*`, their rows in `cases.tsv`/`divergences.tsv`/`expectations.tsv`, the independent-count branches and the composition control in `gen_expectations.py`, the BY_DESIGN entries in `calibrate.py`, the NOTES text. Expectations for the remaining cases are unchanged (sha256 identical; the case-7 `control` column is now empty). After the change: `gen_expectations.py --check` 8/8, `tools/check_subst.py` slice 34 ok / 0 bad. The full `make check-harness` was NOT re-run after the amendment (857/0 above predates it; the change is confined to bench/subst).
