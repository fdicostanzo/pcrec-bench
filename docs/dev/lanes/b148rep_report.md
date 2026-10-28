# b148rep report -- `report --grain stream` ([B148] unusual_set_v1.md 7.5 "Readers")

Branch `lane/b148rep` (commit 7db42264 + this report). Reads the scratch tier only; no pinned store, no whole-store load.

## Checklist vs 7.5

| 7.5 item | status | where |
|---|---|---|
| `--grain stream` view on the [B143] model | DONE | `pcrecbench/report_stream.py`; `report.py` grain choice + dispatch; `select_latest` factored out of `report_subst.py` (dedup rule shared, subst output unchanged) |
| ns per stream, calls/s, segment MB/s | DONE | stream's own `calls` / `segment_bytes` denominators, median + min-max |
| refused and miss counts | DONE | refused from the row; miss = row `assist_compiles` (`measured`) else `values/streams.tsv` `distinct_resolved` (`declared`), assisted testees only (pcrec native vars compiles once) |
| callout cost split and shares (3.2) | DONE | `arm-*`/`twin_of-*` tags; pass-twin, real-pass only where `callout_fires` equal; share needs `--callee-calib FILE` (callout_calib.py stdout), else `-` |
| depth-of-failure table (6.5) | DONE | `nest-*` rungs (any regime) + non-matched stream rows; limit name via `reduce.giveup_code` |
| break-even line (3.3) | DONE | per vars stream, per assisted testee |
| environment/status on every number | DONE | record list + legend carry status, tier, agreement, load/occupancy verdicts; unmeasured/scratch not ranked unless flagged |
| set grain REFUSES `call-stream` BY NAME | ALREADY DONE by L1, verified + now tested at set AND subject grain | `report.py` ~4365; `test_set_and_subject_grains_refuse...` |
| P12 viewer / trend / frontpage skip table | ALREADY DONE by L1 (`reduce.SET_GRAIN_SKIP_REGIMES`, all three read via `set_grain_rows`: none treats an unknown regime as a hole); added three BEHAVIOURAL controls run over the v1.11 example record | `test_skip_tables_exporters_by_name_b148rep` |

Not done / judgement calls: REPORTER_VERSION left at v28 (an additive grain moves no existing report; bumping would force a full regeneration wave). The depth table is not restricted to the `default` arm: it lists whatever testees are in the selection (deep arms appear as their own testee ids). The callout split lives on throughput rows (that is where the co-* members run), so it reads any non-stream regime of the same records. A stream record deduped by (set, testee, machine) supersedes an older record of the same testee, so cross-regime data must come from one full cell.

## Sample rendering (scratch store `/var/tmp/pcrecbench/b148rep/store`)

Four 1-trial scratch cells (pcre2-jit, pcre2-jit-deep, re2-default-assist-v01, pcrec-auto; `--regimes call-stream,throughput`), box loaded so every record is `inconclusive-load` (shown, `--include-unmeasured`). Numbers are NOT measurements. Full output: `/var/tmp/pcrecbench/b148rep/sample.md`.

### stream `tenant-d4096` pattern `va-tenant` (declared: 16384 calls, 4096 distinct resolved, reuse round-robin)

| testee | state | ns/stream (min-max) | calls/s | segment MB/s | matched | nomatch | refused | gave_up | misses |
|---|---|---|---|---|---|---|---|---|---|
| `pcrec_614d45eb3_auto-caps-simdna` | measured | 326.3 us (326.3 us-326.3 us) | 50,213,770 | 1635 MB/s | 11,706 | 4,678 | 0 | 0 | - |
| `re2_11.0.0_default-caps-simdna_assist-v01` | measured | 66.189 ms (66.189 ms-66.189 ms) | 247,534 | 8.1 MB/s | 11,706 | 4,678 | 0 | 0 | 4,096 (declared) |

break-even (3.3), pcrec's compile paid back against each assisted engine:
- 54,272 calls: `pcrec_614d45eb3_auto-caps-simdna` compile 218.171 ms / (assisted `re2_11.0.0_default-caps-simdna_assist-v01` 4040 - pcrec 20 ns/call)

_an assisted engine's time measures THAT assist (keying, container, escaping), not the engine in the abstract._


Callout split (excerpt):

## Callout cost split (3.2)

| testee | member | subject (regime) | twin | pass | pass-nofn | real | pass - twin | fires pass/real | real - pass (per fire) | callee share |
|---|---|---|---|---|---|---|---|---|---|---|
| `libpcre2_10.46_jit-caps-simdna` | co-isbn | co-isbn-1m (large-subject-throughput) | 554.6 us | 649.0 us | 568.4 us | 587.3 us | 94.4 us | 8,429 / 8,429 | -61.6 us (-7.3 ns) | - |
| `libpcre2_10.46_jit-caps-simdna` | co-luhn | co-luhn-1m (large-subject-throughput) | 1.279 ms | 1.204 ms | 1.379 ms | 1.885 ms | -74.5 us | 11,308 / 11,308 | 680.8 us (60.2 ns) | - |
| `libpcre2_10.46_jit-caps-simdna` | co-member | co-member-1m (large-subject-throughput) | 699.1 us | 808.9 us | 730.6 us | 769.7 us | 109.8 us | 13,158 / 13,158 | -39.1 us (-3.0 ns) | - |
| `libpcre2_10.46_jit-caps-simdna` | co-netstr[assisted] | co-netstr-1m (large-subject-throughput) | 5.287 ms | - | - | - | - | - / 7,152 | - | - |
| `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | co-isbn | co-isbn-1m (large-subject-throughput) | 358.7 us | 395.5 us | 383.0 us | 422.6 us | 36.9 us | 8,429 / 8,429 | 27.1 us (3.2 ns) | - |

Depth of failure (excerpt):

### pattern `cscan-onig`

| rung | `libpcre2_10.46_jit-caps-simdna` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | `pcrec_614d45eb3_auto-caps-simdna` |
|---|---|---|---|
| `nest-brace-128` | match | match | -3:PCREC_ERR_FRAMES |
| `nest-brace-512` | -46:JIT | match | -3:PCREC_ERR_FRAMES |
| `nest-brace-1k` | -46:JIT | match | -3:PCREC_ERR_FRAMES |
| `nest-brace-2k` | -46:JIT | match | -3:PCREC_ERR_FRAMES |
| `nest-brace-8k` | -46:JIT | match | -3:PCREC_ERR_FRAMES |

## Tests

New `pcrecbench/tests/test_report_stream.py`, 9 passed / 0 failed (wired into `make check-report`): cell reduction by hand, break-even (+ control), callout split/share/flags, depth table, gave-up naming, status/tier/two-host gates + no-call-stream refusal, set and subject grain refusal (+ stream-view control), CLI flag refusals, three exporter skip controls (+ search-record controls).

## make check

OWED: launched detached after the last commit. Log `/var/tmp/pcrecbench/b148rep/make_check.log`, completion line `DONE rc=<n>` (cwd `worktrees/b148rep`, `make check`). If `make` stops at an unrelated early red, run the rest with `make -k check`.
