# Lane b148l4 report -- [B148] L4: `--mode calls`, the `deep` arms, limits, high-water

Branch `lane/b148l4`, base master 36faad9e. Tier: code + checks + one SCRATCH dry run (never
`store/`, no pinned window). ~/pcrec read-only, no downloads (cargo `--offline`).
Design: docs/design/unusual_set_v1.md v0.2 §6.1-6.5, §7.1-7.3, §10's L4 row; review
docs/dev/reviews/2026-10-27-r9-unusual-set.md C4/C7/C8.

## 1. Charter vs committed

| item (source) | committed | where |
|---|---|---|
| `--mode calls` in every v1 roster driver (§7.1-7.3) | YES: pcre2 (interp/jit), pcrec (auto/vm/-in), onig, re2, rust, vectorscan `-som` ONLY | each driver; `timed_calls.*` TUs; `testees/common/calls_io.h` |
| preallocated result array, hashed after the clock, subject load outside timing (§7.2) | YES: `struct call_res[]` allocated before the clock; tokens written by `calls_report` after it; the HARNESS hashes the token file (no SHA-256 in any driver) | `calls_io.h`, `driverrun.py` |
| group 0 + group 1 tokens (E-2b) | YES (`m:s,e;g1s,g1e` where the pattern has a group 1; vectorscan group 0 only) | `calls_io.h`; `check_calls` synthetic stream vs oracle |
| vectorscan only `-som` (C4) | YES: `supports_calls` = `engine_mode == "block-som"`; the driver refuses `--mode calls` without `--som` by name | `testees/vectorscan/` |
| flip `CALL_STREAM_PENDING`, replace the pending arm (§10) | YES: False; `check_call_stream_readers` now asserts `NO_STREAMS_REFUSAL` (found: email + a named call-stream regime silently ran with no stream rows) | `harness.py`, `tools/selfcheck.py` |
| `unusual_only` gate, refusal by name (subst_only analogue) | YES: `UNUSUAL_ONLY_REFUSAL` before any compile | `harness.py`; check_calls |
| `deep` configs, 1 GiB CAP on matcher storage for EVERY engine (Q1) | YES where the engine has a dial: `pcre2-interp-deep` (heap 1 GiB, match/depth UINT32_MAX), `pcre2-jit-deep` (JIT stack 1 GiB, match UINT32_MAX), `pcrec-{auto,vm}-deep` (1 GiB caller buffer, budgets INT64_MAX), `onig-default-deep` (stack 2^30/32 elements, retries 0, nest 1,000,000, global setters outside the timed loop). re2/rust/vectorscan: no counter limit to raise, no deep arm (stated per adapter) | configs.toml x3, `config_extra` `lim-ceil1g` |
| every engine's effective limits READ BACK and recorded (§6.2) | YES, compile-row `engine_metadata` `lim_*` on every unusual-set cell, both arms (table §2) | each adapter `LIMITS_DECL`; check_calls (4) |
| give-up named by limit (§6.3, X49) | YES: `giveup_names` per adapter, `harness.name_limit`; pcrec-auto on cscan-onig -> `PCREC_ERR_FRAMES` | check_calls (3) |
| O(segment) pre-flight, else explicit anchoring (§7.1, C4) | DONE: every engine O(segment) -> all `stream_anchor = native`; `--anchor-explicit` built anyway (pcre2/pcrec/onig/re2; rust refuses by name, vectorscan refuses) and checked vs PCRE2_ANCHORED | §3; docs/dev/measurements/2026-10-27-b148l4-oseg-preflight.* |
| memory high-water per §6.4 / C8 | YES: untimed `mem_pass` (one fresh driver per subject after the trials) on every unusual-set match row: `deep_mem_bytes`, `deep_mem_method`, `deep_maxrss_kb`. Methods: pcre2-interp `counting-alloc`, pcre2-jit `mincore`, pcrec `canary` (buffer arms only), onig `rss-delta`, re2/rust/vectorscan none | `harness.mem_pass`, `DEEP_MEM_DECL`; check_calls (5) |
| C8 amendment: a LIBRARY testee records maxrss as engine_metadata (X38 scopes `process`) | YES, `deep_maxrss_kb`; applied to the note's §6.4 text | unusual_set_v1.md §6.4 |
| `--grain stream` reporter view (§7.5) | NOT BUILT: §10's table assigns it to no lane (§7.5 lists it as a reader); pcrecbench/CLAUDE.md now says "owed" rather than "L4/L5's". The set-grain refusal L1 built stands | -- |
| BD16: timed code untouched | YES, proven for all six drivers (timed source diff-empty, timed function instruction-identical at the same mod-64 address, `main` the positive control, 20 existing-mode invocations byte-identical but seconds) | docs/dev/measurements/2026-10-27-b148l4-instrument-additivity.* |
| checks in `make check-harness` (shape of check_subst.py) | YES: `tools/check_calls.py`, 43 checks, ~70 s, via `check_calls_set` | §5 |
| dry run + `CELL_CAP_unusual` | see §4 | |
| callouts (L5), vars (L7) | not touched; a vars binding row is REFUSED by name in every driver ("lane L7") | |

## 2. Limits read back (compile-row engine_metadata, measured on this box)

| engine | default arm | deep arm |
|---|---|---|
| pcre2-interp | match 10,000,000; depth 10,000,000; heap 20,000,000 KiB (`pcre2_config` = context) | match/depth 4,294,967,295; heap 1,048,576 KiB |
| pcre2-jit | match 10,000,000; JIT stack 32,768 B (the library's internal default) | match 4,294,967,295; JIT stack 1,073,741,824 B |
| pcrec (auto, vm) | `lim_storage_bytes` 131,072 (stack frames); step 500,000,000 / work 1,000,000,000 | storage 1,073,741,760 B (frames 10,324,440 + trail 41,297,760 on cscan-onig); step/work 9,223,372,036,854,775,807 |
| onig | match stack 0 (unlimited); retry-in-match 10,000,000; retry-in-search 0; subexp-call-in-search 0; nest 20; parse depth 4,096 | 33,554,432 elements x 32 B; 0; 0; 0; 1,000,000; 4,096 |
| re2 | max_mem 8,388,608 | -- (no deep arm) |
| rust | size_limit 10,485,760; dfa_size_limit 2,097,152 | -- |
| vectorscan | none exposed | -- |

Q-E answered (the note): Oniguruma's match-stack limit counts 32-byte ELEMENTS, 4 per nesting
level on the recursion member; 2^30 / 32 = 33,554,432.

## 3. The O(segment) pre-flight

One refused (no-match) call over a real local-refusal segment of seg-s (calls 54 / 14, 60 / 333 B)
followed by a `(`-dense filler tail of 64 KiB vs 640 KiB, through each engine's real `--mode
calls`, 2000 replays x 5 trials, `taskset -c 11`, NOT quiet-gated (load ~10; the ratio is the
reading, not the ns). 10/10 engine rows read 0.77-1.07 for a 10x tail -> O(segment). CONTROL:
cscan with `\G` deleted on pcre2-interp reads 8.2x / 14.0x, so the probe sees an O(tail) scan
when one exists. Every engine stays `native`; `--anchor-explicit` is available but not used.

## 4. Dry run (scratch, `bench/unusual`, 12 testees, patterns cscan, cscan-onig, wild-sexp-balanced, wild-json-validate, wild-json-validate-onig, floor; 5 trials, `taskset -c 11`, `--force-unquiet`, load 8-10)

RAN to `DONE rc=0` (22:53:55 -> ~01:41 EDT, ~2 h 47 min for 12 cells) but MOST OF ITS OUTPUT
WAS LOST: the whole `/var/tmp/pcrecbench/` tree was deleted and recreated at ~01:41 by something
outside this lane (no script in this repo removes it; the manager should find out what), during
the last cell. What survives:

| cell | wall | status | source |
|---|---|---|---|
| pcre2-jit | 498 s | `inconclusive-load` (expected: unquiet box, scratch) | monitor event, before the wipe |
| tre-default | 62 s | rc 0 (call-stream dropped with the note; recursion refused) | the recreated log + its record |
| the other 10 | ~9,500 s together (avg ~16 min) | UNKNOWN (log, err files and records deleted) | wall arithmetic only |

The arithmetic cannot exclude ONE of the ten having been killed at the 5,400 s cap. So the
per-cell duration table is OWED (re-run: `/var/tmp/.../dry/run.sh` is gone too; it is the loop
in this report's §4 header: `harness.run_cell("unusual", t, trials=5, force_unquiet=True,
tier=scratch, patterns=[the six], machine_id="ryzen7700x")` under `gnutimeout 5400 taskset -c
11`, one cell per testee).

**Proposed `CELL_CAP_unusual`: keep the default 5400 s** for the six-pattern recursion subset
(pcre2-jit 498 s = 11x headroom; the mean of the rest ~16 min = 5.6x). For the FULL set (22
patterns; the callout/vars members refuse in seconds today but will run once L5/L7 land, and
pcre2-interp is super-quadratic on deep nesting, NOTES.md 3) set it from the re-measured table,
not from this; a first guess is 3x the subset's worst cell. A lane under load ~9-10 on core 11
reads slower than a window would.

## 5. Checks

- `tools/check_calls.py`: 43/43 PASS (~70 s).
- `check_call_stream_readers`: pending arm replaced; PASS.
- additivity probe: 6/6 drivers, 20/20 invocations.
- full `make check`: OWED -- launched detached at hand-back (log `/home/pcrec/projects/pcrec-bench/worktrees/b148l4/build/b148l4_makecheck.log`, marker line `DONE rc=N`); the manager watches it. The email quick-cell check is load-sensitive.

## 6. Findings

1. pcre2's counting allocator on the match CONTEXT alone read 136 B on a 2,048-deep nest: the
   interpreter's frames are the MATCH DATA's allocation (`pcre2_match_data_create_from_pattern`'s
   gctx). Fixed (both get the counting gctx); the known-depth control now grows 983,344 ->
   3,932,464 B (512 -> 2k nesting).
2. re2 and rust read their ordinary 2-column `--list` BEFORE the calls branch, so a calls list
   crashed them (exit 2). Fixed by ordering; caught by the synthetic stream.
3. A set with no stream subject plus a named `call-stream` regime ran SILENTLY with no stream
   rows: now `NO_STREAMS_REFUSAL`.
4. E-1 reproduced: `onig-default` answers cs-nest-19/20/21/30/100 did-not-match (nest-level 20);
   the deep arm answers them.
5. pcrec-auto (stack frames) gives up `PCREC_ERR_FRAMES` on 100/256 seg-s and 1,723/4,096 seg-l
   calls; pcrec-vm-deep matches both stream hashes. pcrec's default arm has no high-water method
   (no buffer to canary; frame count not on the shim surface) -- OWED, stated in §6.4.
6. rust-regex has no anchored-at-offset search on `regex::bytes::Regex`: `--anchor-explicit`
   refused by name (moot at v0.1: no stream pattern compiles under rust).
7. vectorscan/re2/rust compile no stream pattern of unusual@0.1 (no `\G`/recursion); their calls
   mode is exercised only on the synthetic stream.
8. The `--grain stream` view is assigned to no lane in §10 -- the manager's to place.
