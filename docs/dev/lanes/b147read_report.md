# b147read -- [B147] the first-window READ at pcrec 614d45eb3 (abi 89) (lane report)

Branch `lane/b147read` (worktree `worktrees/b147read`), Sonnet, not pushed, not merged. Window 2026-10-28 12:10 -> 19:09 EDT (chain log `/var/tmp/pcrecbench/b147win/chain.log`,
`CHAIN_DONE`; 14 cells, all `measured`, records committed e5ea76f8). Nothing was timed by this lane; `store/` and ~/pcrec untouched. Ledger:
`docs/dev/ledgers/2026-10-29-first-window-614d45eb3.md` (the full derivation; everything below is its summary). Scratch + logs: `/var/tmp/pcrecbench/b147read/` (`gen_*.log`, each ending `DONE rc=0`).

## Verdicts

1. **Window usable, not quiet.** 11 of 14 cells passed the pre-flight at attempt 1; 3 were refused (rc=3, nothing written) and measured at attempt 2 (sentinel nocaps open, syntax auto, sentinel jit close).
   No `inconclusive-*`. All 14 records `measured`, trial agreement `agree`. 6 of 14 carry a failed AFTER occupancy sample and 3 an AFTER load1 above 2.00 (provenance under v1.4). Sentinels closing/opening: medians
   0.996-1.005, single short set-cells up to +-11% (pcrec) / +-22% (jit). The chain's driver-sha start/end lines differ (`aa38260d` vs `0e877032`) **because the first cell of each config rebuilt the driver at 12:11/12:23**
   (file mtimes), not drift: the start hash is the previous window's leftover; one build measured all 14 cells.
2. **The cross-window control (9ae59f5d4 now vs 10-25) is NOT clean.** Large-subject cells 0.9989 / 0.9997; **short cells +4.0% / +4.4%** (caps / nocaps, 69-70 set-cells each); pcrec sentinel +5.4% while the jit row is
   +-1%. Harness commit `ef83d130` -> `e0e68c3e` (driver now links `timed_calls.c`, `timed_calls_vars.c`; every sentinel artifact +160 B median). Cause not isolated. The in-window N vs B pair is unaffected.
3. **Census confirmed by value: 442 of 442 compiled-both rows** (capability caps 138, nocaps 139, syntax caps 165) agree with the prep census on program identity AND `emit_bytes`/`emit_code_bytes` deltas; 0 mismatches;
   refusal movers = the two syntax grp-callout rows. Answers unchanged anywhere (same non-expected outcomes at both pins, both configs).
4. **[SCANEDGE-SET] timing, same-window N vs B (capability):** `\s+$` (`tail-space-eol`) **x0.164** (72,999.9 -> 11,990.9 ns; `t-trim-match-60k` 1.186 -> **0.194 ns/B**, pcrec's 1.17 -> 0.19 reproduced), nocaps x0.165;
   `.*\.txt$` x0.929 / x0.908 large; `[a-z]+\.txt$` flat. **The same mechanism is slower elsewhere**: `base10num-noatomic` x1.200 large / x1.176 short, `-grok` x1.102 / x1.071, syntax `cls-s-uc` x1.116 large /
   x1.119 short (cross-window; the trials are disjoint), all with a scan edge gained or widened (range -> mixed). `username-password-pair` (range -> mixed) flat; `cls-range` x0.816 large. 6b2dbd3e read 0.192-0.194 ns/B on
   `\s+$`: abi 87 undoes the 9ae59f5d4 rev-end regression (x6.1), it does not beat 6b2dbd3e.
5. **Null distribution:** 241 of 275 capability cells program-identical, median +0.12%, p5-p95 -1.88 / +2.40%; the report's band is **+-19.92%** (large >=1us) / +-16.78% (short 100ns-1us), set by one bimodal family
   (`evil-alt-nested`: 41.8k-55.7k inside one record; `numeric-id-nested-plus`, `phone-list-nested-plus`). Sentinel N/B over 30 identical patterns: median 0.9991. syntax `esc-octal-0` (identical) is bimodal 126k / 160k across pins.
6. **grp-callout `ca(?C1)t`:** compiles under auto-caps/nocaps, plain + whole (VM, selected, no prefilter, 24,921 / 25,145 B emit, 145 ms); `callout_binding = separate-tu-pass`, `callout_bindings = rx_callout_1` on
   every compile row; **445/445 match rows per config `matched-as-expected`** against the libpcre2 oracle; set cells large 1,159,917 ns (x2.78 `lit-cat`), short 240.8 ns (x1.18), whole 180.0 ns. Per-fire cost is NOT derivable
   (fires per call unread). Prediction P1 of `syntax-0.1-first.tsv` ("did-not-compile") is now false at this pin (not scored: the file is for 0.1).
7. **Unpredicted:** (i) the +4-5% pcrec-side harness shift (2); (ii) the scan edge's two signs (4); (iii) the D119 band is one bimodal cell (5); (iv) the chain's sha check cannot see a rebuild.

## Deliverables / charter-vs-committed checklist (session_discipline.md 7(c))

| brief item | status |
|---|---|
| BOILERPLATE read first; worktree `lane/b147read`; toplevel printed first; explicit-path commits; no push/merge; no timing; store loads detached | done; `git rev-parse --show-toplevel` printed the worktree; reports rendered detached `setsid nohup ... gnutimeout 2400` (`gen_*.log`, `DONE rc=0`, `gen.done`) -- each group loaded only its 2-4 records and took 12-34 s, never the whole store |
| 1. capability@0.3 cross-pin 614d45eb3 vs 9ae59f5d4, both caps arms | `reports/2026-10-29-capability-0.3-ryzen7700x-first-614d45eb3.{tsv,md,matrix.tsv,subject-grain.md,subject-grain.tsv}` |
| 1. syntax at 614d45eb3 incl. grp-callout, cross-pin against the latest prior syntax record | `reports/2026-10-29-syntax-0.2-ryzen7700x-first-614d45eb3.{tsv,md,matrix.tsv,subject-grain.md,subject-grain.tsv}`; the reporter cannot join versions (prior record is syntax@0.1), so the cross-pin is from the records in ledger section 5 with the cross-window offset named |
| 1. the cross-pin census a committed cross-pin report needs (`reports/identity/`) | NOT needed: the reporter's null band read the records' own `program_sha256_v3` (275 cells, no census fallback); the header says so. No identity file written |
| 1. (extra) sentinel pair | `reports/2026-10-29-sentinel-0.1-ryzen7700x-first-614d45eb3.{tsv,md,matrix.tsv}` (`--all-records`) |
| 2. interpretation sidecars via `pcrecbench interpret` | three `.interpretation.md` (skill recipe: repo-relative paths, `--subject-grain` where it exists, determinism `cmp` clean on all three; no predictions file matches 0.3 / 0.2) |
| 3. ledger | `docs/dev/ledgers/2026-10-29-first-window-614d45eb3.md` (sections 0-11, each verdict says what was read and what was not) |
| 4. this report + O-n draft | here; `docs/dev/outbox_to_pcrec.md` NOT edited |
| 5. CLAUDE.md rows | `reports/CLAUDE.md` (new section), `docs/dev/ledgers/CLAUDE.md` (row), `docs/dev/measurements/CLAUDE.md` (row + the archive dir `2026-10-29-b147read/`) |
| `make check-interpret` green | **291 passed, 0 FAILED** (`make -C worktrees/b147read check-interpret`, ~30 s) |
| OWED (manager) | merge; send the O-111 draft below; regenerate the 114 older sidecars at the window close if `check-interpret` section 3 goes stale after the merge ([B41]); the chain's driver-sha check (hash after the first cell); a decision on an old-shim A/B for the +4-5% harness shift and on an `-fno-scan-edge` arm (`pcrec-auto-noedge`) for the three slower movers; whether the viewer / trend / front page take the 614d45eb3 records (`make trend`, `make frontpage` NOT run, per the brief); full `make check` NOT run |

## O-111 DRAFT (for the manager; NOT written to the outbox)

> ## O-111 (2026-10-29, bench manager) -- the first window at 614d45eb3 (abi 89): [SCANEDGE-SET] has two signs; the callout row measured; I-163's `\s+$` reproduced
>
> Window 2026-10-28 12:10 -> 19:09 EDT on `ryzen7700x` (core 7): capability@0.3 x {auto, nocaps} at 614d45eb3 and at 9ae59f5d4 (same-window BEFORE), syntax@0.2 x {auto, nocaps} at 614d45eb3, opening and closing sentinels; 14 cells measured, 3 of them after one pre-flight refusal. The box is Frank's desktop in daytime: usable, not quiet (6 of 14 records carry a failed AFTER occupancy sample; sentinel medians flat to 0.7%). Ledger `docs/dev/ledgers/2026-10-29-first-window-614d45eb3.md`; reports `reports/2026-10-29-{capability-0.3,syntax-0.2,sentinel-0.1}-ryzen7700x-first-614d45eb3.*` (reporter v28).
>
> **Your census holds on our corpus, row for row.** 442 compiled-both rows (capability caps/nocaps, syntax caps) agree with the b147prep census on program identity and on `emit_bytes` / `emit_code_bytes` deltas (0 mismatches); answers are unchanged at every cell (the same non-expected outcomes at both pins in each config).
>
> **I-163 `\s+$` reproduced.** capability `tail-space-eol` large: 72,999.9 -> 11,990.9 ns caps (x0.164), 72,996.1 -> 12,008.5 nocaps (x0.165); on the 61,440 B `t-trim-match-60k` **1.186 ns/B at 9ae59f5d4 -> 0.194 ns/B at 614d45eb3** (your 1.17 -> 0.19). The 6b2dbd3e records read 0.192-0.194 ns/B on the same cell, so abi 87 restores the 6b2dbd3e speed; the x6.1 slowdown at 9ae59f5d4 was the rev-end scan edge-less path. `.*\.txt$` large x0.929 / x0.908 (a 64-ns three-subject cell), `[a-z]+\.txt$` flat (x1.004 / x1.000).
>
> **The same mechanism is slower on four other cells.** With a scan edge gained or widened (`range` -> `mixed`, edges 1 -> 2): capability `wild-logparse-base10num-noatomic` large x1.200 (3.629 -> 4.354 ms caps, x1.199 nocaps), short x1.176 / x1.168; `wild-logparse-base10num-grok` (VM) large x1.102 / x1.104, short x1.071 / x1.078; syntax `cls-s-uc` (`\S+@\S+`, edge gained) large x1.116 (trial ranges 1.499-1.506 ms vs 1.662-1.698 ms, disjoint) and short x1.119 (cross-window, caps; nocaps agrees at 1.672 ms). `wild-secrets-username-password-pair` (range -> mixed) is flat; `cls-range` large is x0.816 faster. We have no `-fno-scan-edge` arm in this window, so this is the 9ae59f5d4 -> 614d45eb3 pair, not an A/B on the one mechanism. Ask (a): is a `mixed` edge on a short class run a mis-selection, and what is the break-even run length? We can run `pcrec-auto-noedge` on these five cells if you want it.
>
> **grp-callout measured.** `ca(?C1)t` compiles under auto (VM, selected, no prefilter, 24,921 B emit plain / 25,145 whole, 145 ms compile), binding `separate-tu-pass` with `callout_bindings = rx_callout_1` recorded on every compile row (one indirect call per fire). 445 of 445 match rows per config agree with the libpcre2 oracle (no callout function set = the pass-through). Set cells: large 1,159,917 ns (x2.78 the literal `cat` in the same window), short 240.8 ns (x1.18), whole 180.0 ns. We cannot give ns/fire: fires per call are not in the record. Ask (b): a fires-per-call count (stamp or `--emit-ir`) so the cell can be split.
>
> **Two things on our side you will otherwise trip on.** (1) Cross-window comparison of short cells against the 10-25/26 records carries a +4.0-4.4% pcrec-side offset at the SAME pin (large cells 0.999-1.000; the sentinel pcrec +5.4%, the jit row +-1%): our driver between the windows gained the callout/vars call modes and every artifact grew a median 160 B (shim). Cause not isolated; every number above is same-window except the syntax rows, which carry it. (2) The capability D119 null band is +-19.92% on large cells and +-16.78% on short: one bimodal cell family (`evil-alt-nested` trials 41.8k-55.7k in a single record) sets it, so nothing under 20% on a large capability cell is resolved by the report; syntax `esc-octal-0` (program-identical) alternates 126k / 160k across pins and windows. We read short cells against the sentinel null (30 identical patterns, median 0.9991) instead.
>
> **Asks (c).** `RX_VM_PROGRAM_BYTES` moves on EMIT-BIDI respells with no program change (b147prep finding 2, 330 -> 326 on `key\tvalue`); please state the intended definition. The syntax P1 prediction ("grp-callout did-not-compile on every pcrec testee", dated 334fd10e) is now false and is not scored.
