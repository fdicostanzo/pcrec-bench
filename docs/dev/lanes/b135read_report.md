# b135read -- [B135] step (c): the READ of the states 1+2 window (lane report)

Branch `lane/b135read` (worktree `worktrees/b135read`), not pushed, not merged. Window 2026-10-10 12:13-19:19 EDT, 26/26
cells measured at attempt 1. Nothing was timed by this lane; ~/pcrec untouched. Ledger:
`docs/dev/ledgers/2026-10-10-opt-revend-states12-7388f1c0.md`.

## Verdicts

1. **Instrument A/B**: NOT a same-pin test -- BEFORE (2eb8938) ran pcrec at 255bcdd8, AFTER (17cb77d) at 7388f1c0 (the script reads each tree's own `configs.toml` pin;
   the brief's "both at 7388f1c0" is not what the stores hold). pcre2-jit (the only pcrec-free rows): AFTER/BEFORE median 0.998 (0.982-1.014): the driver did not change pcre2 timing.
   pcrec cells are driver x pin; timed.c/.h are byte-identical, and the window itself used one driver build for both states. A fixed-pin re-run is OWED if wanted.
2. **Sentinels**: held. pcrec end/open 0.989-1.006 at both pins (60 cells, 2 disjoint ranges, both < 1%); pcre2-jit 0.943-1.060, all overlapping. First window with a sentinel, so the cross-window half waits for state 3.
3. **Acceptance**: 32/32 (16 cells x caps/nocaps) INSIDE the predicted ns and ratio ranges; ratios x2,898-x337,939. Neither failure signature fired (max 1 MiB cell 40.74 ns; no body-size dependence).
4. **Window clean?** Yes by the sentinel's own reading; the trend report's 7388f1c0-vs-a15fb77b pair carries no `instrument_changed`/`wide_gap`/`drift_suspect` flag.
5. **Regressions**: `.*\.txt$` short regime +14.6% (66/75 short subjects +5.5 ns); litrun whole-subject family +1.5..+7.7% (sub-ns to +2.5 ns on ~10 ns calls); one PROGRAM-IDENTICAL +19% (`wild-logparse-quotedstring-grok` short, caps only, +6.5 ns on 74/75 subjects).
6. **Reporter defect found**: R8's "previous version" is timestamp-ordered, so ABBA inverts the nocaps Δ column, D119 bar, null band and the nocaps R-DELTA sidecar rows in all four new reports (medians right).

## O-92 DRAFT (for the manager; not written to the outbox)

> ## O-92 (2026-10-10, bench manager) -- [OPT-REVEND] states 1+2: acceptance 32/32, three regressions, and what REVEND left
>
> Window 2026-10-10 12:13-19:19 EDT, one window, one driver build, ABBA: pcrec-auto / pcrec-nocaps at a15fb77b (abi 72) and 7388f1c0 (abi 73), capability@0.2, loglines@0.1, email-specimen@0.2, litrun@0.1; 26/26 cells measured at attempt 1; sentinel@0.1 open and end flat (pcrec <= 0.6%, pcre2-jit 0.94-1.06). Ledger `docs/dev/ledgers/2026-10-10-opt-revend-states12-7388f1c0.md`; reports `reports/2026-10-10-*-revend-7388f1c0.*`.
>
> **(a) I-142 s1 acceptance: all 32 cells (16 x caps, nocaps) inside the predicted ns range and ratio range.** Measured ns per call (caps): no-match cells 7.97-9.54; `\w+\z` x txt 21.55 and `\s+$` x space 28.36 (13-42); `\d+$` x digits 28.36 and `\w+\z` x digits 23.48 (19-60); `[a-z]+\.txt$` x txt 32.92 (22-66); `.*\.txt$` x txt 39.73 (33-98); `\s+$` x t-trim-nearmiss-16k 10.02 (7-24). Ratios vs a15fb77b (whose medians reproduce O-91 (c)): x2,898 (trim) to x337,939 (`[a-z]+\.txt$` x digits). The ">150 ns or varying with body size" signature did not fire (largest 1 MiB cell 40.74 ns; `\w+\z` 6.6/6.7/6.6 ns on t-64k/t-256k/t-1m); the "40-60 ns with flat sentinels" signature does not apply (the one cell there is a matching cell with predicted 33-98). Stamps to the letter, caps == nocaps but the flags word; `req_why` is `dominated` on the two `.txt` patterns (I-142 s1 omitted it). emit_bytes -17.5%..-27%.
>
> **(b) What REVEND left on the tail family.** `tail-word-eoz` and `tail-space-eol` still lose their large-subject cell to Vectorscan no-SOM (x55.6, x21.7), and each cell is one subject: 21,775 ns on `t-evil-match-60k` (`\w+\z`) and 21,799 ns on `t-trim-match-60k` (`\s+$`), the two 61,440-byte bodies that match from byte 0 to the end (0.354 ns/B), against 42,820 / 130,730 ns at a15fb77b. Every other subject of those cells is 6.6-32.0 ns. The long matching body is the family's remaining cost, not the megabyte of non-matching text. Is the walk's per-byte cost on a body that matches back to byte 0 expected, and is there a cheaper start recovery for it ([START-LANDING] state 3 will show)?
>
> **(c) Regressions (all beyond trial overlap, caps and nocaps unless stated).**
> 1. `.*\.txt$` x short-subject-search: 644 -> 738 ns set sum (x1.146 / x1.149); 66 of 75 short subjects +5.5 ns each (3.8 -> 9.3 ns). The old `memchr-bounded` prefilter dismissed subjects with no `.` in 3.8 ns; rev-end's floor is 9.3 ns. The other four tail patterns' short rows still win (x0.37-0.95).
> 2. litrun whole-subject forms (rev-end, `end_window 2..16 -> none`): `alt-foo-tails` x1.077 (+0.84 ns/call mean over 27 subjects), `lit-l4` x1.034, `lit-l2` x1.032, `wild-secrets-aws-access-key-id` nocaps x1.048, `lit-l8` / `wild-secrets-github-pat` x1.022; longer literals (`lit-l31`, `lit-l40`) win 2%. email's whole-subject cells (`orig`, `factored`, `floor`) read x1.000 (73,130 ns -> 73,126 ns): REVEND moves nothing there.
> 3. `wild-logparse-quotedstring-grok` x short-subject-search, caps only: 2,122.7 -> 2,525.2 ns (x1.190) on a PROGRAM-IDENTICAL VM artifact (`program_sha256`, `emit_bytes` 64,131 and `vm_program_bytes` 17,340 equal); +1.5..+7.3 ns on 74 of 75 subjects; nocaps +0..2.7 ns on 9. Cause unknown (layout is a hypothesis). Of 356 program-identical set cells the ratio is p5 0.995 / p95 1.006; this is the only one beyond 5%.
>
> **(d) Unpredicted, from b135prep and confirmed here.** 13 census rows go `engine_sel size-cap-retry -> selected` and grow (+36 KB..+460 KB; the capability row here is `wild-logparse-syslogbase-expanded` whole form, +35,755 B), so a speed read of altwide/utf8 whole forms mixes REVEND with the restored prefilter; 285 of 297 rev-end census rows are the whole-subject form, and only the search regime of the tail family shows the large effect in this suite; abi 72 stamps `RX_DFA_START reverse-pass` on attempt/empty bodies (74 census rows, 38 in capability) and abi 73 corrects it to `attempt-start` with no timing change; `req_why` `dominated` on 81 census rows (emitted -> dominated).
>
> **(e) Two things on our side.** The instrument A/B was not same-pin (BEFORE ran 255bcdd8); the pcre2-jit control is flat (0.998), the window used one driver build and the sentinels were flat, so the verdict stands, but we cannot say what the 2eb8938 -> 17cb77d driver change did to pcrec cells. Our reporter paired the nocaps records backwards (timestamp order under ABBA); medians are right, its Δ column is inverted for nocaps; being fixed before state 3.
>
> **Asks.** (1) (b)'s question. (2) Is (c)1 the expected price of REVEND on patterns whose old route was a `memchr` dismissal, and is a cheap last-byte or required-byte dismissal in front of the reverse walk planned? (3) State 3 (b8337c33) is queued over the same cells with a15fb77b or 7388f1c0 repeated as the cross-window control; (c)3 is the cell we will watch.

## Charter-vs-committed checklist (session_discipline.md 7(c))

| promise in the brief | status |
|---|---|
| read BOILERPLATE first; worktree `lane/b135read`; commit only, no push/merge | done; commits on `lane/b135read`; not pushed |
| detached store loads, one at a time, markers | report generation (`DONE rc=0`), snapshots (`DONE rc=0`), `make trend` x2 + trend-check (`DONE rc=0`), frontpage x2 + check (`DONE rc=0`); no two ran together |
| 1. A/B read with the b133 analysis script, archived with source header, "did the driver change timing" | `docs/dev/measurements/2026-10-10-b135-instrument-ab.txt`; answered in ledger section 1 and above (confounded by pin; pcre2 flat) |
| 2. sentinels open vs end per pin | `2026-10-10-b135-sentinel-open-end.{py,txt}`; ledger section 2 |
| 3. cross-pin reports (4 sets, auto + nocaps), existing naming, sidecars | `reports/2026-10-10-{capability-0.2,loglines-0.1,email-specimen-0.2,litrun-0.1}-budu-ryzen1600-revend-7388f1c0.{tsv,md,matrix.tsv,subject-grain.tsv,subject-grain.md,interpretation.md}`; sidecars deterministic (byte-equal re-render), `make check-interpret` 254/0 |
| 4. acceptance table + both failure signatures + movers both directions + stamps + regressions flagged | ledger sections 3, 4, 4.1; `2026-10-10-b135-acceptance.txt`, `-movers.txt` |
| 5. ledger + DRAFT outbox item (not in outbox_to_pcrec.md) incl. b135prep's four unpredicted findings | ledger `docs/dev/ledgers/2026-10-10-opt-revend-states12-7388f1c0.md` (+ row in ledgers/CLAUDE.md); draft above; `docs/dev/outbox_to_pcrec.md` NOT touched |
| 6. trend: snapshot both pins, links, `make trend`/`trend-check`, FIRST interpretation + say if clean, `make check-trend` | snapshots `a15fb77b.tsv.gz`, `7388f1c0.tsv.gz` (`verify_snapshot` `[]`); links: 0 proposed, 5 already listed; `make trend` + `trend-check` 111 files 0 drifted; `reports/trend/interpretation/{7388f1c0,a15fb77b}.md` (cite-check 0 problems); `make check-trend` ALL PASS; clean per sentinel (7388f1c0 pair unflagged; a15fb77b's own pair is `instrument_changed` against 255bcdd8) |
| 7. front page at 7388f1c0, `make frontpage-check`, state headline + "Where pcrec loses" changes, mixed windows noted | done below; README/methodology/svg/provenance regenerated, `frontpage --check: clean`, `check-frontpage` pass |
| `make check` (full) | NOT run (long; manager launches): command `make check > build/check.log 2>&1; echo "DONE rc=$?" >> build/check.log` from the worktree. Ran: `check-interpret` 254/0, `check-trend` pass, `check-frontpage` pass, `frontpage-check` clean, `trend-check` 0 drifted |
| OWED | (a) manager: merge, send O-92, KB entry + fix for the R8 timestamp pairing before state 3 (regenerate these four groups and sidecars after); (b) optional fixed-pin A/B re-run; (c) Frank's OK before the front page is pushed |

## Front page (item 7)

Regenerated with `make frontpage FRONT_PIN=7388f1c0` (the Makefile default is now 7388f1c0 so `frontpage-check` passes: `frontpage --check: clean`). The page now MIXES
windows: capability's competitors are the 2026-10-08/09 records, pcrec's is 2026-10-10. The headline footnote says so with dates ("Competitor records were measured 2026-10-08 to 2026-10-09, pcrec's on 2026-10-10, all on one machine"); the methodology engines table and the other-sets table carry per-row dates; I added the same statement to the hand-written losses prose.

- **Headline**: faster in 936 of 1,019 comparisons (was 919), median speedup 5.00x (was 4.59x); wins 936 / losses 81 / ties 2 (was 919 / 99 / 1). Per competitor, PCRE2 JIT median x2.84 -> x3.18 (losses 17 -> 16, ties 1 -> 0), RE2 x8.71 -> x9.83 (losses 11 -> 8), Rust x2.00 -> x2.29, Vectorscan no-SOM x1.57 -> x1.98 (29 -> 24 losses). Pattern-support table unchanged (69 compiled, 0 wrong). pcrec compile median 224 ms -> 228 ms.
- **Where pcrec loses**: the tail-cause group fell from 17 cases to 2 (`tail-word-eoz` and `tail-space-eol`, large-subject, vs Vectorscan no-SOM, x55.6 / x21.7); total losses 99 -> 81; the `wild-logparse` family leaves the top (25 -> 8 losses, 10.6% -> 3.4%). Two corrections the generator cannot make: the hand-written paragraph said reverse search "is a filed, not yet implemented pcrec work item" (now false) and `docs/frontpage_why.tsv` cited bench/capability/NOTES.md's "engines that scan forward pay the megabyte" for the five tail patterns (no longer the cause for the two left). I rewrote the paragraph and re-sourced the two remaining rows to the ledger (4.1), quote "the tail family's remaining cost is the long MATCHING body, not the megabyte of non-matching text"; the other three rows are removed. The generated "Work item" link still names OPT-REVEND, relabelled "(implemented, pcrec 7388f1c0)".
- The `othersets` table moves email/loglines pcrec-auto from c4c70f2c (2026-10-05) to 7388f1c0 (2026-10-10); other sets (bounded, altwide, syntax, utf8) keep their own latest pcrec record; litrun has no competitor.
- NOT pushed; needs Frank's OK.

## Files

- `/home/duxevents/pcrec-bench/worktrees/b135read/docs/dev/ledgers/2026-10-10-opt-revend-states12-7388f1c0.md`
- `/home/duxevents/pcrec-bench/worktrees/b135read/docs/dev/lanes/b135read_report.md` (this file)
- `/home/duxevents/pcrec-bench/worktrees/b135read/reports/2026-10-10-*-revend-7388f1c0.*`, `reports/trend/` (snapshots, interpretation/{7388f1c0,a15fb77b}.md)
- `/home/duxevents/pcrec-bench/worktrees/b135read/docs/dev/measurements/2026-10-10-b135-*`
- `/home/duxevents/pcrec-bench/worktrees/b135read/README.md`, `docs/methodology.md`, `docs/frontpage_why.tsv`, `Makefile`
