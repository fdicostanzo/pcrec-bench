# b149w2read -- [B149] the READ of window W2 `b149w2`, the first window at pcrec cb32eda28 (abi 93) (lane report)

Branch `lane/b149w2read` (worktree `worktrees/b149w2read`), Sonnet, not pushed, not merged. Window 2026-11-01 07:56-13:18 EST (chain log `/var/tmp/pcrecbench/b149w2/chain.log`, `CHAIN_DONE`;
12 cells / 13 records, store commit 69b9af2e). Nothing was timed by this lane; `store/` and ~/pcrec untouched. Ledger `docs/dev/ledgers/2026-11-02-first-window-cb32eda28.md` (the full derivation; everything
below is its summary). Scratch + logs: `/var/tmp/pcrecbench/b149w2read/` (`gen_cap.log`, `gen_sen.log`, `interp_*.log`, `ci.log`, each ending `DONE rc=0` except `ci.log`, section 4). Renders and interprets ran
`nice -n 19 taskset -c 0-5`, detached (`setsid nohup`), one at a time; no `make check-harness`, no full `make check`.

## Verdicts

1. **Window usable, not quiet at the edges.** 7 of 12 cells passed the pre-flight at attempt 1; 10 invocations were refused (rc=3, nothing written) and one exited 4 (the jit opening sentinel, `inconclusive-spread`, d = 43 of 75,
   re-measured once per contract; the first record stays in the store). All 12 final records `measured`, trial agreement `agree` (capability 0 of 138 / 140 groups failing). 4 of 4 capability records carry a failed AFTER sample
   (occupancy 10.1% / 25.4%, load1 2.09 / 2.17; provenance under v1.4). Sentinel closing / opening: pcrec medians 0.9945-1.0091, the jit row noisier (set-cells 0.735-1.152). The chain's driver sha256 is equal at start and end and equal to
   the 10-28 window's final one: one driver binary.
2. **The cross-window control at 614d45eb3 (W2 vs 2026-10-28) is CLEAN**: capability set-cell medians 1.0009 / 1.0000 large, 0.9994 / 0.9983 short (caps / nocaps), sentinel 1.0004 opening / 1.0038 closing (jit 1.0068 / 0.9968), artifacts
   byte-identical. The +4-5% short-cell offset b147read found between 10-26 and 10-28 is absent between 10-28 and 11-01.
3. **Census confirmed by value: 138 of 138 (caps) and 139 of 139 (nocaps) compiled-both rows agree** with `2026-10-30-b149prep-census.tsv` on program identity AND `emit_bytes` / `emit_code_bytes` deltas; 0 mismatches, 0 unattributed, 0 refusal
   movers (K134 +1,608..+1,882 B median +1,815; cover -6,837..-2,404 median -4,286; pair look-ahead +368). Answers unchanged: 0 of 6,486 / 6,580 match cells differ; the non-expected populations are identical at both pins.
4. **abi 92 `cover` has two signs.** Faster: `hex8-bounded` x0.423 large / x0.57 short, `\[` x0.74 / x0.90, `keyword-prefix-order` x0.87 / x0.94, `\{` short x0.89; flat on 3 large. **Slower: `utf8-lead-no-cont` x1.95 large (0.192 -> 0.375 ns/B
   on all 19 subjects) and x1.20 short** (both configs, disjoint trials, D119 `regress`). Short-regime cover gain is a near-constant -0.6..-0.9 ns/call on tiny subjects, reproduced by the sentinel's four cover patterns (N/B 0.895-0.976).
5. **K134 costs +1.6-1.9 KB (above the stated +0.6-1.2 KB) and no per-byte time.** Large regime indistinguishable from the null (K134 median x1.0025 caps / x0.9991 nocaps vs control x1.0046 / x0.9992); short regime a fixed
   +0.2..+1.2 ns per call: median +1.9% caps / +3.8% nocaps, 8 of 24 cells beyond +4.3% (`bracket-array-define` +11.4%, `tag-depth3-bound` +10.3%, `numeric-id-nested-plus` +9.8%, `phone-list-nested-plus` +9.4% caps). No capability give-up changed.
6. **The reqrun look-ahead (`wa = wb = 128`) is a performance change, not +368 B**: nocaps `wild-secrets-username-password-pair` x0.057 large (5.64 ms -> 0.32 ms; t-qs-1m x0.045), no stamp moved; `wild-waf-crs-942270-union-select`
   x1.159 / x1.152 SLOWER large, x1.113 / x1.087 short (stamps unchanged).
7. **The I-172 query-string cells have no timing: `dup-param-detect` x `t-qs-1m` and `t-qs-nearmiss-256k` GIVE UP (`PCREC_ERR_FRAMES`, 2,048 resume frames) on all trials, both pins, both configs.** K134 does not touch frames. The reverse-landmark stage is not at this
   pin (`req_handoff` none for the pattern). abi 91 is NOT separately timed: the forced-VM `abc` witness and the `-fno-req-handoff` / `--memfn=no-window-search` arms were not in the roster; the one capability abi-91 mover is inseparable from the look-ahead and K134.
8. **The reporter's band is +-36.64% (large >= 1 us), set by one nocaps cell** (`phone-list-nested-plus`, IQR 44%); it reads `within` for `union-select` (+15.9%), `trim-nested-star` (+30.9%) and the K134 short tail. Caps-only program-identical cells (n = 84) span -7.06 .. +3.44%, p5-p95 -1.65 / +1.93.
9. **Unpredicted:** (i) `utf8-lead-no-cont` x1.95 under cover; (ii) the look-ahead's timing effect, both signs; (iii) the band's widening 19.92% -> 36.64%; (iv) both I-172 cells give up; (v) the clean control.

## Deliverables / charter-vs-committed checklist (session_discipline.md 7(c))

| brief item | status |
|---|---|
| BOILERPLATE read first; worktree `lane/b149w2read`; toplevel printed; explicit-path commits; no push/merge; no timing; renders detached; one heavy command at a time; `nice -n 19 taskset -c 0-5` | done; worktree created from 8f7e2197, `git rev-parse --show-toplevel` printed the worktree path; commits 0087b1ac, 30a3d1c2 and the final one; capability render 35 s, sentinel render 8 s, two interprets ~15 s each, all `setsid nohup ... gnutimeout`, each ending `DONE rc=0`; the cap and sentinel renders loaded only their 4 and 9 records |
| 1. capability@0.4 cross-pin cb32eda28 vs 614d45eb3, both caps arms; subject-grain too | `reports/2026-11-02-capability-0.4-ryzen7700x-first-cb32eda28.{tsv,md,matrix.tsv,subject-grain.md,subject-grain.tsv}` |
| 1. the W2 sentinel group (`--all-records`) | `reports/2026-11-02-sentinel-0.1-ryzen7700x-first-cb32eda28.{tsv,md,matrix.tsv}` |
| 2. `.interpretation.md` sidecars via `pcrecbench interpret` | both, skill recipe (repo-relative paths, `--subject-grain` for capability, no predictions file matches 0.4 / 0.1-sentinel, determinism `cmp` CMP_OK on both) |
| 3. ledger | `docs/dev/ledgers/2026-11-02-first-window-cb32eda28.md` (sections 0-9, each verdict says what was read and what was not): window quality, drift, cross-window control, census by value, the O-116 movers' timing, the I-172 cells, the null |
| 3. the null distribution over program-identical cells | ledger section 4 head and section 6 (`out/null.txt`, `out/null_excl.txt`, `out/d119.txt`) |
| 4. this report + O-117 DRAFT | here; `docs/dev/outbox_to_pcrec.md` NOT edited |
| 5. CLAUDE.md rows | `reports/CLAUDE.md` (new section), `docs/dev/ledgers/CLAUDE.md` (row), `docs/dev/measurements/CLAUDE.md` (row + the archive dir `2026-11-02-b149w2read/`), `docs/dev/lanes/CLAUDE.md` (row) |
| `make check-interpret` green | **NOT green, and not because of this lane**: 176 passed, 117 FAILED, all 117 section 3 "re-renders byte-identical" on pre-existing sidecars (every report older than W2's own regeneration: the stamped index sha256 no longer matches the live `store/index.tsv` after the b149mon / W2 records). My two new sidecars pass (they are not in the FAIL list); sections 1, 2, 4, 5, 6 pass. Regenerating 117 sidecars is the manager's [B41] act at window close and would conflict with it on merge, so I did not do it; the command is `scripts/regen_reports.py`'s sidecar regeneration (the chain runs it, ~1 min) |
| OWED (manager) | merge; the O-117 draft below; the [B41] sidecar regeneration (117) at the b149mon close; whether `make trend` / `make frontpage` / the viewer take the cb32eda28 records (NOT run, per the brief); the K134 give-up flips on `bench/unusual` and the abi-91 / cover A/B arms (a window with `pcrec-auto-noedge`-style deny testees for `--memfn=no-window-search` and `-fno-req-handoff`, which are flags without a pinned testee); full `make check` NOT run |

## O-117 DRAFT (for the manager; NOT written to the outbox)

> ## O-117 (2026-11-02, bench manager) -- the first window at cb32eda28 (abi 93): cover has two signs, the look-ahead is a timing change, K134's cost is per call, the I-172 cells give up
>
> Window `b149w2`, Sun 2026-11-01 07:56-13:18 EST on `ryzen7700x` (core 7): capability@0.4 x {auto, nocaps} at cb32eda28 and at `@614d45eb3` (same-window BEFORE), opening and closing sentinels; 12 cells measured (7 at attempt 1; 10 invocations refused by the pre-flight, one `inconclusive-spread` jit sentinel re-measured once). Usable, not quiet at the edges (4 of 4 capability records carry a failed AFTER sample, provenance only). The 614d45eb3 cross-window control against 2026-10-28 is clean (capability 0.998-1.001, sentinel 1.000-1.004; one driver binary). Ledger `docs/dev/ledgers/2026-11-02-first-window-cb32eda28.md`; reports `reports/2026-11-02-{capability-0.4,sentinel-0.1}-ryzen7700x-first-cb32eda28.*` (reporter v28).
>
> **Your census holds on our corpus, row for row.** 138 (caps) + 139 (nocaps) compiled-both rows agree on program identity and on emit / code deltas; K134 +1.6-1.9 KB (your +0.6-1.2 KB is low for these), cover -2.4..-6.8 KB, the look-ahead +368 B. Answers unchanged at every cell; K134 changed no capability give-up (`date-nested-plus` x `t-hyb-datepath-16k` still FRAMES).
>
> **abi 92 `cover` is faster on 5 of 9 and slower on one.** `hex8-bounded` (`\b[0-9a-f]{8}\b`) large x0.423, short x0.57 (but x1.5 on the 60-B `sd-empty-alt-*` subjects, 64 -> 99 ns); `\[` large x0.74 (x0.60 on the two prose texts, flat on the six tail/query texts), short x0.90; `keyword-prefix-order` x0.87 / x0.94; `\{` short x0.89. **`utf8-lead-no-cont` (`[\xc2-\xdf](?![\x80-\xbf])`) is x1.95 slower on every large subject (0.192 -> 0.375 ns/B) and x1.20 on short**, on both configs with disjoint trials; its stamps went prefilter byte-class-bounded -> none, scan unanchored -> cover, start end-minus-width -> attempt-start. Ask (a): is cover meant to take a class + negative-lookahead window, and what is the break-even against the byte-class-bounded scan? We have no `--memfn=no-window-search` testee, so this is the 614d45eb3 -> cb32eda28 pair, not an A/B on the one mechanism; we can add one.
>
> **The reqrun look-ahead is not +368 B of nothing.** nocaps `wild-secrets-username-password-pair`: 5.64 ms -> 0.32 ms (x0.057; the two query-string texts 5.27 ms -> 0.23 ms and 0.31 ms -> 0.03 ms), no stamp moved; caps x0.576 (abi 91 handoff and K134 ride along). `wild-waf-crs-942270-union-select`: x1.159 / x1.152 large, x1.113 / x1.087 short, no stamp moved. Ask (b): is that the intended trade, and is the 128-byte window tunable?
>
> **K134 is a per-call term.** Large subjects: no cost distinguishable from the null (K134 cells x1.0025 caps / x0.9991 nocaps against program-identical controls x1.0046 / x0.9992; the recursion specimens x0.98-1.02). Short subjects: +0.2..+1.2 ns per call, median +1.9% caps / +3.8% nocaps, up to +11.4% on 6-12 ns calls (`bracket-array-define`, `tag-depth3-bound`, `numeric-id-nested-plus`, `phone-list-nested-plus`). Ask (d): can the checkpoint-state bind be skipped on cycle-free calls?
>
> **The I-172 query-string cells could not be timed.** `dup-param-detect` x `t-qs-1m` and x `t-qs-nearmiss-256k` give up `PCREC_ERR_FRAMES` (2,048 resume frames) on all five trials at both pins and both configs: compile stamps `engine vm`, `req_handoff none`, `req_why emitted`; K134 does not touch frames. Ask (c): does the reverse-landmark stage land in a later pin, and is the frame cap the intended outcome for the near-miss? The other 68-70 patterns on `t-qs-1m` answer and move only as above. abi 91 was not separately timed (no forced-VM `abc` arm, no `-fno-req-handoff` testee).
>
> **Our side.** The reporter's D119 band for large >= 1 us is +-36.64% this window (was +-19.92%): one nocaps cell (`phone-list-nested-plus`, trials 2,402-4,614 ns in one record) sets it, so the report's `within` hides `union-select` (+15.9%) and the K134 short tail; we read against the program-identical caps cells instead (n = 84, p5-p95 -1.65 / +1.93, range -7.06 .. +3.44).

## Not read / owed items

Per ledger section 9. In particular: instruction counts (no `perf`), emitted C, whole-subject forms, every set but capability and sentinel, the 114+ stale sidecars.
