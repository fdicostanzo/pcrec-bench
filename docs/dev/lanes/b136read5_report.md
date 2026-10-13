# b136read5 -- [B136] tier 5 READ (lane report)

Branch `lane/b136read5` (worktree `worktrees/b136read5`), Sonnet, not pushed, not merged. Window read: tier 5 of `docs/dev/lanes/b136_chain.sh`, 2026-10-13 09:23-14:39 EDT, every set rc=0, records committed b464e67a. Nothing timed by this lane; ~/pcrec untouched (the pin's `lib/pcrec.h` was read from the bench's own `build/pcrec-6b2dbd3e`). The full derivation is the "Tier 5 addendum (2026-10-13)" at the end of `docs/dev/ledgers/2026-10-13-req-handoff-l1-6b2dbd3e.md`; this file is its summary.

## Verdicts

1. **utf8 `ci-strasse` (the cell that gates pcrec's T5).** Throughput BASE 943,099 > NEW 623,352 ns (**x0.661**, DISJ) > CANON 623,392 (x1.000); DENY 1,274,329 (**x2.044 over NEW, x1.351 over BASE**). Stamps: K 2 at BASE and NEW, none under DENY, prefilter `byte-class` > `handoff` > `byte-class`. The gain sits on the 64 KB-1 MB Latin/ASCII subjects (x0.56-0.69), none on CJK/Cyrillic. search_short flat (1,252 / 1,271 / 1,282; N/B 1.015 ov). The DENY slowdown is `-fno-req-handoff` removing K82's ENTRY handoff too (BASE already had K 2), so it is not an L1-only number. **`ci-ascii-control` (K 0) is flat in every pair** (tp N/B 0.997, D/N 0.992; ss 1.003 / 1.000): unlike `mod-i` / `mod-r`, a K-0 cell here costs nothing.
2. **Whole utf8 DENY arm vs NEW (smoke).** 138 set cells, 0 wrong / missing, 0 refused compile rows; D/N median 1.000 (p5-p95 0.955-1.273); 10 cells above +3% (`lit-nfc-pair` x2.958 ... `asr-b-ascii` short x1.030), **every one a program-changed cell with a K at NEW and none under DENY** (22 compile rows differ); no program-identical cell moved. Nothing unexpected.
3. **Capability nocaps, the 15th mover.** `wild-secrets-username-password-pair`: engine `dfa`, K 0, `dfa_prefilter` `byte-class` (b8337c33) > **`handoff`** (00c97769), program d5aff4d878be > 4535c1956061; the only nocaps `handoff` row; caps (VM) is unchanged. Timing nocaps BASE > NEW: throughput 79,035.5 > 79,114.3 (x1.001), short 797.6 > 796.4 (x0.999): flat. All 139 nocaps cells N/B median 1.000, 3 above +3% (`phone-palindrome-6` x1.144 / x1.073, both ov with 20% trial ranges, the same cell is x1.125 / x1.038 between two BASE records; `bracket-array-define` tp x1.031 DISJ, program-identical).
4. **Capability DENY vs NEW / BASE.** 137 cells: D/N median 1.000 (0.992-1.009 p5-p95), **0 cells above +3%** (max 1.019), tail family 0.983-1.019 all ov, grok 0.996 / 0.999; the only visible DENY effect on a mover is `wild-secrets-username-password-pair` short x1.016 (DISJ, +17 ns).
5. **bounded at 6b2dbd3e vs 00c97769.** All 126 cells program-identical; median 1.000, one cell above +3% (`cls-upto-128` tp x1.039 ov); `dotted4` C/N 0.998 / 1.000. **email at 6b2dbd3e vs b8337c33 (no 00c97769 email record exists):** 9 of 9 program-identical, median 0.999, 0 above +3%. Neither set moved.
6. **Sentinels.** close5/open5 median 0.997-1.000 for every pcrec testee (per-cell 0.989-1.014), jit 0.999 (0.936-1.062); open5/open1 (vs the tier 1-4 window) 0.998-1.001; pcre2-jit sum of cell medians 10,464,128 (open5) / 10,456,609 (close5) vs 10,457,807 (open1): +-0.2%. Tier 5 sits on the main window's instrument.
7. **Trend.** `make trend-check`: 121 files, 0 drifted (`/var/tmp/pcrecbench/b136read5/trend-check.log`, `DONE rc=0`). **The trend needs nothing to stay green, but the 6b2dbd3e snapshot (45 records, immutable) predates tier 5: it has no bounded@0.3 or email-specimen@0.2 cell and none of the tier-5 sentinel/capability/utf8 records.** Whether to add a later snapshot (a new id, not an overwrite) is the manager's decision; I did not snapshot.
8. **Front page: moved to 6b2dbd3e.** Every FRONT_OTHER set has a 6b2dbd3e pcrec record (email 10-13T15:25Z, bounded 14:36Z, loglines/altwide/syntax/utf8/litrun in the main window) and capability's caps record is 10-12T23:36Z. `Makefile` FRONT_PIN b8337c33 > 6b2dbd3e; `make frontpage`, `frontpage-check` ("clean"), `check-frontpage` PASS. Headline **before > after: faster 936 > 938 of 1,019, tied 2 > 1, slower 81 > 80, median x5.02 > x5.01, geo-mean x8.51 > x8.52**; per competitor: Rust 76/14/0 > 76/13/1, Vectorscan no-SOM 66/23/2 > 68/23/0, RE2 longest-match median x9.59 > x9.68; the README's "wild-waf" row 21 > 20. NOTE: `tools/frontpage.py` reads `PCREC_VERSION` by `git show <pin>:lib/pcrec.h` in `~/pcrec` (detached at c4c70f2c, which has no 6b2dbd3e); I ran it with `PCREC_REPO=/var/tmp/pcrecbench/b136read5/pcrec-hdr-repo`, a one-commit scratch repo holding the pin's `lib/pcrec.h` copied from `build/pcrec-6b2dbd3e` (version `0.2.0-beta`, unchanged from b8337c33), tagged `6b2dbd3e`. **A later `make frontpage-check` without that override will fail until ~/pcrec has the pin**, as the earlier lane's note anticipated. The README's hand-written prose (e.g. the "latest pin (b8337c33)" tail paragraph) still names b8337c33; I did not edit hand-written prose.

## O-102 DRAFT (for the manager; NOT written to the outbox)

> ## O-102 (2026-10-13, bench manager) -- follow-up to O-101: the tier-5 cells measured; the window is closed
>
> Tier 5 (2026-10-13 09:23-14:39 EDT, all sets rc=0, store 400 lines) measured the three owed items plus bounded/email canonical cells. With it the [B136] window (tiers 1-5, 2026-10-12 11:08 -> 2026-10-13 14:39 EDT) is **CLOSED**; the sentinels bracket it: tier-5 close/open median 0.997-1.000 per pcrec testee, pcre2-jit row +-0.2%, tier 5 vs the tier 1-4 open 0.998-1.001. Ledger addendum in `docs/dev/ledgers/2026-10-13-req-handoff-l1-6b2dbd3e.md`; reports `reports/2026-10-13-{capability-0.2,utf8-0.1}-budu-ryzen1600-handoff5-6b2dbd3e.*`.
>
> **utf8 `ci-strasse` (the T5 gate), BASE b8337c33 / NEW 00c97769 / DENY / CANON 6b2dbd3e.** Throughput 943,099 / 623,352 / 1,274,329 / 623,392 ns (NEW/BASE **x0.661 DISJ**, DENY/NEW x2.044, DENY/BASE x1.351); K 2 at BASE and NEW, none under DENY; `dfa_prefilter` `byte-class` > `handoff`. Per subject: 64 KB-1 MB Latin/ASCII x0.56-0.69, CJK/Cyrillic x0.99-1.00. search_short 1,252 / 1,271 / 1,282 (flat). The DENY number includes K82's entry handoff (the flag removes both), so it is "no handoff of any kind", not L1 alone. **`ci-ascii-control` (K 0) is flat:** throughput N/B 0.997, D/N 0.992; short 1.003 / 1.000. This bears on O-101 ask 1: of the three cells you named, only `mod-i` / `mod-r` read x1.03; `ci-ascii-control` reads 1.00.
>
> **Whole utf8 DENY arm (smoke).** 138 cells, answers correct, 0 refused; D/N median 1.000; 10 cells above +3% (lit-nfc-pair x2.96, lit-1ch-4b x1.88, lit-1ch-3b x1.63, asr-lb-neg x1.51, alt-shared-char x1.51, lit-sharp-s x1.47, qnt-bounded-4b x1.24 ...) -- all program-changed K-bearing cells, none program-identical.
>
> **Capability.** The 15th mover (nocaps, `wild-secrets-username-password-pair`): engine dfa, K 0, prefilter `byte-class` > `handoff`, program d5aff4d878be > 4535c1956061; timing flat (throughput 79,035.5 > 79,114.3, x1.001; short 797.6 > 796.4). All 139 nocaps cells N/B median 1.000. Capability DENY vs NEW: 137 cells, median 1.000, **none above +3%** (max 1.019); tail and grok inert (grok short 2,136 / 2,141 / 2,133).
>
> **bounded and email at 6b2dbd3e.** bounded: all 126 cells program-identical to 00c97769, median 1.000, one cell x1.039 (overlapping ranges); dotted4 unchanged (C/N 0.998 / 1.000). email: 9 of 9 program-identical to b8337c33, median 0.999. (No 00c97769 email cell exists.)
>
> **Open, bench side:** the front page now reads 6b2dbd3e (936 > 938 faster of 1,019); `tools/frontpage.py` needs the pin's `lib/pcrec.h` from a pcrec checkout that has the commit -- ~/pcrec is detached at c4c70f2c. **Ask:** none new; O-101's asks 1-4 stand as answered by I-151, with the `ci-ascii-control` fact above as the one new data point on ask 1.

## Charter-vs-committed checklist (session_discipline.md 7(c))

| promise in the brief | status |
|---|---|
| BOILERPLATE first; worktree `lane/b136read5`; no timing; store loads detached one at a time; no forks | done; top-level printed first; report regen `/var/tmp/pcrecbench/b136read5/gen.log` (`DONE rc=0`), sidecars `sidecars.log` (`DONE rc=0`, 97 sidecars, 0 failures), `trend-check.log`, `frontpage.log`, `fpcheck.log` (`DONE`); a foreground `make check-report` at 118 s hit the timeout once and was re-run detached |
| 1. utf8 `ci-strasse` / `ci-ascii-control` BASE/NEW/DENY + whole DENY arm smoke | ledger T5.1, T5.2; `docs/dev/measurements/2026-10-13-b136t5-{utf8,utf8all}.txt` |
| 2. capability nocaps 15th mover by value + timing; DENY vs NEW tail/grok/+3% | ledger T5.3, T5.4; `...b136t5-{cap,capall}.txt` |
| 3. bounded and email at 6b2dbd3e | ledger T5.5; `...b136t5-{bounded,email}.txt` |
| 4. sentinels | ledger T5.6; `...b136t5-sentinel.txt` |
| 5. addendum + cross-pin groups (capability nocaps, utf8 DENY) pinned `--until 2026-10-13T23:59:59Z` + stale sidecars | addendum appended; `reports/2026-10-13-{capability-0.2,utf8-0.1}-budu-ryzen1600-handoff5-6b2dbd3e.*` (2 x 6 files); `handoff-6b2dbd3e` groups untouched; all 97 sidecars regenerated ([B41]) |
| 6. trend | said above (item 7): `trend-check` 0 drifted; snapshot gap named; no snapshot taken |
| 7. front page | moved; before > after above; the 3 checks green |
| 8. O-102 draft, outbox untouched | this file; `docs/dev/outbox_to_pcrec.md` not edited |
| 9. `make check-report` / `check-interpret` green; report; END | `check-report: OK` (`checkreport.log`), `check-interpret: 271 passed, 0 FAILED`; full `make check` not run (no code changed) |
| OWED (manager) | merge; send O-102; decide on a post-tier-5 trend snapshot; make `~/pcrec` carry 6b2dbd3e (or accept the `PCREC_REPO` override) before the next `make frontpage-check`; refresh the README's hand-written b8337c33 prose |

## Files

- `docs/dev/ledgers/2026-10-13-req-handoff-l1-6b2dbd3e.md` (addendum), `docs/dev/lanes/b136read5_report.md`
- `docs/dev/measurements/2026-10-13-b136t5-analysis.py` + seven `2026-10-13-b136t5-*.txt`
- `reports/2026-10-13-{capability-0.2,utf8-0.1}-budu-ryzen1600-handoff5-6b2dbd3e.*`, 97 `reports/*.interpretation.md` re-stamped
- `Makefile` (FRONT_PIN), `README.md`, `docs/methodology.md`, `docs/frontpage_provenance.tsv`, `docs/img/*.svg` (generated), `reports/CLAUDE.md`, `docs/dev/measurements/CLAUDE.md`
