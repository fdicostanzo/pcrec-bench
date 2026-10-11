# b135read3 -- [B135] the STATE-3 READ (lane report)

Branch `lane/b135read3` (worktree `worktrees/b135read3`), not pushed, not merged. Window 2026-10-10 20:21:17 EDT ->
2026-10-11 13:03:26 EDT (master 4cad239f, `CHAIN_DONE suite_rc=0`), 11 sets, every cell measured, two quiet-gate refusals both
measured on attempt 2 (`sentinel` x `pcre2-jit`, `bounded` x `pcrec-nocaps`). Nothing was timed by this lane; ~/pcrec untouched
(one read-only `git show` against the b135s3 lane's scratch clone `/var/tmp/b135s3/pcrec`, see the front-page note). Ledger:
`docs/dev/ledgers/2026-10-11-start-landing-state3-b8337c33.md` (the full derivation; everything below is its summary).

## Verdicts

1. **Sentinels / window clean?** Yes. open / end / end2, window 3: pcrec end/open, end2/open and end2/end 0.982-1.013 at both pins (5 disjoint-range
   pairs among 180, all < 1.3%), pcre2-jit 0.941-1.074 with every pair overlapping; 7388f1c0 window 3 open vs window 1 0.987-1.011.
2. **Cross-window control** (7388f1c0 here vs in the states 1+2 window, 422 set cells, four tier-1 sets): B/A p5-p95 **0.995-1.007**, median 1.000
   (loglines 0.992-1.006, email 0.998-1.002, litrun 0.981-1.008, capability 0.851-1.158 with four named cells: `wild-logparse-quotedstring-grok` caps
   short 0.851, `bracket-array-define` caps throughput 1.158, `phone-palindrome-6` nocaps short 1.118 and throughput 0.910). That is the drift the three-state comparison is read against: +-0.7%.
3. **Reports:** seven cross-pin groups `reports/2026-10-11-<set>-<ver>-budu-ryzen1600-landing-b8337c33.*` (capability, loglines, email-specimen, litrun,
   utf8, syntax, bounded; 35 files + 7 sidecars, all deterministic) and the three-state table per tier-1 set (ledger section 3.2).
4. **START-LANDING verdict:** I-145's 298 reproduced to the unit (292 measured here + 6 with no pair: altwide 2, sentinel 2, `ci-ucp-invariance` 2, which has no `-utf8` record);
   every one flipped `dfa_start reverse-pass > end-minus-width | landing` (584 cells). Beyond trial overlap: end-minus-width 311 of 408 cells faster (76%), 21 slower (5%),
   median 0.956; landing 137 of 176 faster (78%), 14 slower, median 0.839; the program-identical null (852 cells) 22 faster / 15 slower (2.6% / 1.8%), p5-p95 0.990-1.008. The gain is mostly search-regime
   (end-minus-width median 0.925 short-search vs 0.976 throughput). Best cells: utf8 `prp-l` x0.52, litrun `lit-l31` throughput x0.66 and `lit-l40` short x0.64; tier-1: capability `wild-secrets-github-pat` short x0.84 / x0.79,
   loglines/email `floor` short x0.74, litrun `lit-l40` x0.64. The whole-subject form moved nothing (278 cells).
   - **FIT movers** (`prp-l`, `prp-notl`): confirmed by value (`size-cap-retry > selected`, `reverse-pass > landing`, emit 471,796 > 894,613 and 490,248 > 874,155) and they got FASTER (x0.517 / x0.568, x0.873 / x0.911).
   - **Non-movers that moved:** one -- `loglines` `http-5xx` nocaps short x1.041 (program-identical, caps twin x1.000). 37 of 852 null cells are DISJ, 10 are outside +-5% (all with overlapping ranges).
   - **Unpredicted:** utf8 `search-short` gets SLOWER on 12 patterns (24 cells, +1.3..+6.0%: `prp-lu` x1.060, `ci-neg-fold` x1.054, `asr-lb-neg` x1.052, `cls-dot` x1.051, `cls-neg-single` x1.049, the `lit-offset-*` heads x1.026-1.028 ...).
5. **I-146 controls:** the tail family is flat (24 set cells all overlap, 0.990-1.013; 132 per-subject cells 0 disjoint; stamps and `program_sha256` unchanged). `wild-logparse-quotedstring-grok` caps: the +19% did **not** persist --
   7388f1c0 window 3 reads 2,149.0 ns (window 1: 2,525.2; a15fb77b 2,122.7), b8337c33 2,147.0; the same testee id, 75 of 75 subjects faster by a median 5.3 ns; the emitted C differs in 3 lines
   (banner abi, `#include` name, `.abi`); no alignment-offset control was run (nothing to control).
6. **[ENG-TACTICS] table:** ledger section 6 (loglines 11 patterns x 2 regimes, altwide `sfx-64/256/512` x 3 regimes, caps and nocaps, median and min-max).
7. **Relay asks:** (1) litrun texts: ledger 7.1 (`alt-foo-tails` = `foo.x|foobar|foo.`, `lit-l2` = `ab`, `lit-l4` = `abcd`, `lit-l8` = `abcdefgh`, aws `\b((?:A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16})\b`,
   github-pat `\b(github_pat_[0-9a-zA-Z_]{82})\b`, whole form `(?:P)\z`); (2) grok diff: ledger 5.2; (3) Vectorscan SOM: ledger 7.3 -- pcrec wins every tail cell against SOM (set sums x1,016 / x821 on the two cells that lose to no-SOM,
   x6.1 on the two 61,440-byte matching bodies, x39,000-x164,000 elsewhere), CROSS-WINDOW (SOM records 2026-10-09 03:38Z, no same-window control).
8. **Finding the brief did not ask for:** `wild-datetime-datefinder-alternation` (nocaps, 891,859 B emit, program-identical) emit-c phase **x2.53** (173 > 437 ms; of the other 119 (set, config, pattern, form) emit-c cells over 10 ms the largest ratio is x1.18; gcc phase unchanged) --
   `docs/dev/measurements/2026-10-11-b135-state3-emitc-phase.txt`. Reported as an observation; not attributed.

## O-97 DRAFT (for the manager; NOT written to the outbox)

> ## O-97 (2026-10-11, bench manager) -- [START-LANDING] state 3: 298/298 flipped, 76-78% faster beyond overlap, the tail family flat, the grok +19% not repeated, the SOM reading
>
> Window 2026-10-10 20:21 -> 2026-10-11 13:03 EDT, one driver build, ABBA: pcrec-auto / pcrec-nocaps at b8337c33 (abi 74) and 7388f1c0 (abi 73, repeated as the cross-window control) over capability@0.2, loglines@0.1, email-specimen@0.2, litrun@0.1, utf8@0.1, syntax@0.1, bounded@0.3 (+ altwide@0.3 at b8337c33 only, sentinel@0.1 open/end/end2); every cell measured (two quiet-gate refusals measured on attempt 2). Sentinels flat (pcrec 0.982-1.013 across 16 h, jit 0.94-1.07). Ledger `docs/dev/ledgers/2026-10-11-start-landing-state3-b8337c33.md`; reports `reports/2026-10-11-*-landing-b8337c33.*`.
>
> **(a) I-145's 298 movers: reproduced to the unit, then measured.** 210 end-minus-width / 88 landing flipped `reverse-pass` on 292 compile rows we timed (the other 6: altwide 2, sentinel 2, `ci-ucp-invariance` 2 -- no pair). Beyond trial overlap (caps+nocaps pooled): end-minus-width 311 of 408 cells faster (76%, median x0.956, search-short median x0.925), 21 slower (5%); landing 137 of 176 faster (78%, median x0.839), 14 slower; the 852 program-identical cells: 22 faster / 15 slower (2.6% / 1.8%), p5-p95 x0.990-1.008. Best: utf8 `prp-l` x0.517/x0.568, litrun `lit-l40` short x0.638, `wild-secrets-github-pat` short x0.84 (caps) / x0.79 (nocaps), loglines `floor` short x0.74, email `floor` short x0.74. The whole-subject form moved nothing (278 cells), as pcrec said.
>
> **(b) FIT movers confirmed by value and faster:** `prp-l` / `prp-notl` `size-cap-retry > selected`, `landing`, emit 471,796 > 894,613 / 490,248 > 874,155; x0.517/x0.568 and x0.873/x0.911.
>
> **(c) The tail family did not move** (I-146's control): 24 set cells x0.990-1.013 all overlapping, 132 per-subject cells 0 disjoint, `rev-end / reverse-pass` and `program_sha256` identical at both pins. The two long-matching-body cells: 21,774 / 21,772 ns and 21,799 / 21,808 ns.
>
> **(d) The grok +19% did not persist:** `wild-logparse-quotedstring-grok` caps short -- 7388f1c0 window 1 2,525.2 ns, window 3 2,149.0, b8337c33 2,147.0 (a15fb77b 2,122.7); program-identical (`program_sha256`, `emit_bytes` 64,131, `.so` 41,864 B at all four records), 75 of 75 subjects faster by a median 5.3 ns window 3 vs window 1. The emitted C of the two pins differs in 3 lines (banner abi, header `#include` name, `.abi`). So the +19% was that record's, not the abi 72 > 73 step's; no pcrec issue is filed from our side.
>
> **(e) Vectorscan SOM reading of the tail cells** (your relay ask 3; capability@0.2 records 2026-10-09, no same-window control, so only the order of magnitude is claimed): pcrec-nocaps b8337c33 against `vectorscan-block-som` on the large-subject set cells -- `tail-word-eoz` 21,909 ns vs 22,253,652 (x1,016 faster; no-SOM 393.7), `tail-space-eol` 21,971 vs 18,044,599 (x821; no-SOM 1,013.0), `tail-digits-eol` x39,000, `tail-ext-lower-txt` x164,000, `tail-dotstar-txt` x31,700. On the two 61,440-byte matching bodies: 21,776 vs 133,476 ns and 21,798 vs 133,332 (x6.1 faster). Read against SOM pcrec wins every tail cell; the two x55.6 / x21.7 losses exist only against the boolean-grain no-SOM arm. The public front page now says so, citing I-146.
>
> **(f) Unpredicted -- utf8 search-short slower on 12 patterns:** 24 cells, +1.3% to +6.0% (+10..+92 ns on 770-1,870 ns cells), DISJ in both configs: `prp-lu` x1.060, `ci-neg-fold` x1.054, `asr-lb-neg` x1.052 (end-minus-width), `cls-dot` x1.051, `cls-neg-single` x1.049, `lit-offset-at-tail` x1.028, `lit-offset-at-head` x1.026, `floor` x1.020, `lit-1ch-2b` x1.018, `prp-greek` x1.016, `alt-mixed-width` x1.016, `qnt-lazy-2b` x1.015. 56 utf8 patterns flipped; 48 have at least one cell faster beyond overlap (41 only faster). Hypothesis only: a per-call cost in the landing / ill-formed-step path under `-e utf8`. Is that expected?
>
> **(g) Compile time:** pcrec's own emit-c on `wild-datetime-datefinder-alternation` (nocaps, 891,859 B, program-identical) went 173 > 437 ms (x2.53); gcc phase unchanged; the other 119 emit-c cells over 10 ms move at most x1.18. One pattern; not attributed.
>
> **(h) Relay asks answered:** O-96 (c)2 litrun texts (ledger 7.1; whole form `(?:P)\z`; the whole-subject rows read 0.997-1.006 across state 3 -- START-LANDING neither adds to nor removes the REVEND price); [ENG-TACTICS] table (ledger 6).
>
> **Asks.** (1) Is (f) expected -- is there a per-call cost in the utf8 landing / end-minus-width path that a later pin removes? (2) Is (g) the new start-recovery analysis on a very wide DFA? (3) Does K103's trigger count the litrun whole rows (unchanged at state 3)?

## Charter-vs-committed checklist (session_discipline.md 7(c))

| promise in the brief | status |
|---|---|
| read BOILERPLATE first; worktree `lane/b135read3`; commit explicit paths, no push/merge | done; commits on `lane/b135read3` (reports+sidecars 05998b6d, ledger, trend a65b2032, front page / docs below); not pushed |
| detached store loads, one at a time, markers | regen `/var/tmp/b135read3_regen.log` (`DONE rc=0`), `build/trend-snapshot.log`, `trend*.log`, `trend-check*.log`, `frontpage.log`, `frontpage-check.log` (all `DONE rc=0`), no two together |
| 1. sentinels open / end / end2 per pin | ledger section 1; `docs/dev/measurements/2026-10-11-b135-state3-sentinel.txt` |
| 2. cross-window control per set (capability, loglines, email, litrun) | ledger section 2; `...-state3-control.txt` |
| 3. cross-pin reports, 7 sets, naming, sidecars; three-state table per tier-1 set | `reports/2026-10-11-*-landing-b8337c33.*` (35 files + 7 sidecars); ledger 3.2; `...-state3-threestate.txt` |
| 4. START-LANDING verdict: every mover (both medians, overlap, direction, by set), the null, FIT movers, non-mover that moved | ledger sections 4.1-4.5; `...-state3-movers.txt` (every cell), `...-state3-fit.txt` |
| 5. I-146 controls: tail family; grok (+ emitted-C diff, alignment control if it persists) | ledger 5.1, 5.2; `...-state3-tail.txt`, `...-state3-grok.txt`, `...-grok-emitted-c-diff.txt`; the +19% did not persist so no alignment control was run |
| 6. [ENG-TACTICS] table | ledger section 6; `...-state3-sfx.txt` |
| 7. relay asks (1)-(3) | ledger 7.1 / 5.2 / 7.3; `...-state3-som.txt` |
| 8. ledger + O-97 draft (text in the report only) | `docs/dev/ledgers/2026-10-11-start-landing-state3-b8337c33.md` (+ row in `ledgers/CLAUDE.md`); the draft above; `outbox_to_pcrec.md` NOT touched |
| 9. window close per the report-trend skill: snapshot b8337c33, links, make trend / trend-check, interpretation, make check-trend | snapshot `reports/trend/snapshots/b8337c33.tsv.gz` (`verify_snapshot` `[]`, 51 records, 19 inline); links 0 proposed, 5 listed; `make trend` + `trend-check` 112 files 0 drifted; `reports/trend/interpretation/b8337c33.md` (cite-check 0 problems); `make check-trend` ALL PASS. The interpretation reads the pair CLEAN by the sentinel's own cell set and says what it cannot see (no control for the other sets; tier-2 sets pair with older pins and are flagged `wide_gap`/`instrument_changed`) |
| 10. front page at b8337c33 (Makefile FRONT_PIN, make frontpage detached, frontpage-check), like-for-like line citing I-146, state the headline change | `Makefile` FRONT_PIN b8337c33; README/methodology/svg/provenance regenerated; `frontpage --check: clean`; hand-written loss prose rewritten (Where pcrec loses, citing I-146 and ledger 7.3); headline below |
| check-report, check-interpret, check-trend, check-frontpage | see Validation |
| OWED (manager) | merge; send O-97; full `make check` (long; command below); Frank's OK before the front page is pushed; decide whether to pin the `revend-7388f1c0` groups with `--until` (reports/CLAUDE.md) before any `regen_reports.py --only revend`; ~/pcrec's checkout lacks b8337c33 (`PCREC_REPO=/var/tmp/b135s3/pcrec make frontpage-check` needed until the pcrec manager fetches) |

## Front page (item 10)

`make frontpage` (with `PCREC_REPO=/var/tmp/b135s3/pcrec`: ~/pcrec's detached HEAD still lacks b8337c33, so the version-string read fails without the override; the b135s3 lane's scratch clone has it)
and `make frontpage-check` -> `frontpage --check: clean`. **Headline change: faster in 937 of 1,019 comparisons (was 936), slower 80 (was 81), ties 2, median speedup 5.01x (was 5.00x), geo-mean 8.52x (was 8.49x).** Per
competitor: PCRE2 JIT 118 / 16 / 0, median x3.18 -> x3.21; RE2 76 / 8, x9.83 -> x9.84; Rust 76 / 13 / 1, x2.29; Vectorscan no-SOM 67 / 24 / 0 -> 67 / 23 / 1 (one loss became a tie); PCRE2 interpreter 132 / 1 / 1 -> 133 / 1 / 0;
TRE median x56.4 -> x65.7 (a median cell moved; probably the `wild-secrets-github-pat` search pair, x0.84 -- not verified). pcrec compile median 228 ms -> 221 ms. The "wild-secrets" loss family 5 -> 4 cases. The tail group is unchanged at 2
(`tail-word-eoz` x55.6, `tail-space-eol` x21.7 against no-SOM). The 20-worst list reorders (binary-nonutf8 above wild-logparse); `high-byte-run` and `hex8-bounded` ratios move a few percent. The other-sets table now pairs
b8337c33 for email, loglines, bounded, syntax, utf8, litrun (it was c4c70f2c / 7388f1c0); altwide@0.2 (in `FRONT_OTHER`) has no b8337c33 record -- altwide@0.3 was measured here but is not in the front page's set list (left as is; a manager call).
The hand-written paragraph states, with the I-146 citation, that the two tail losses are against a boolean-grain engine and that against Vectorscan SOM pcrec wins them (x1,016 / x821 set sums, x6.1 on the two bodies; cross-window caveat).

## Validation

- `make trend-check` 112 files, 0 drifted (after the final `make trend`); `make check-trend` ALL PASS (cite-check 0 problems on all three sidecars).
- `make check-frontpage` PASS; `frontpage --check: clean`.
- `make check-report`: OK (test_report 103 passed / 0 failed, test_quick 7/0, 15/0 matrix/fixtures, CLI smoke). `make check-interpret`: **261 passed, 0 FAILED** (254 + the 7 new sidecars' freshness/determinism checks). Detached runs, logs `build/check-report.log`, `build/check-interpret.log`, `DONE rc=0` each.
- Full `make check` NOT run (long): `cd /home/duxevents/pcrec-bench/worktrees/b135read3 && make check > build/check.log 2>&1; echo "DONE rc=$?" >> build/check.log` -- OWED, manager.

## Files

- `docs/dev/ledgers/2026-10-11-start-landing-state3-b8337c33.md`, `docs/dev/lanes/b135read3_report.md`
- `docs/dev/measurements/2026-10-11-b135-state3-*` (analysis script, nine mode outputs, grok C diff, emit-c phase probe)
- `reports/2026-10-11-*-landing-b8337c33.*`, `reports/trend/` (snapshot, regenerated TSVs/HTML, `interpretation/b8337c33.md`)
- `README.md`, `docs/methodology.md`, `docs/frontpage_provenance.tsv`, `docs/img/*.svg`, `Makefile`
- `reports/CLAUDE.md`, `docs/dev/ledgers/CLAUDE.md`, `docs/dev/measurements/CLAUDE.md`
