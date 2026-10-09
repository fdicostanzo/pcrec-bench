# b125read — capability@0.2 first-sample READ (lane report)

Branch `lane/b125read` (worktree `worktrees/b125read`), not pushed, not merged.
Brief: wake-queue items 2-4 for the capability@0.2 window at pcrec 255bcdd8.
No measurement was run; the box was not used beyond one detached store load
(KB-16) and the interpreter. `~/pcrec` untouched.

## Delivered (all committed)

| item | artifact |
|---|---|
| 1. reports | `reports/2026-10-08-capability-0.2-budu-ryzen1600-first-255bcdd8.{tsv,md,matrix.tsv,subject-grain.tsv,subject-grain.md}` (14 testees, set and subject grain; reporter v25) |
| 1. cross-pin form | NOT generated: one pin holds 0.2 records; a 0.1 -> 0.2 delta is not like for like (NOTES.md R9). Stated in the ledger §0/§9 and `reports/CLAUDE.md`. |
| 2. ledger | `docs/dev/ledgers/2026-10-09-capability-0.2-255bcdd8.md` (§1 population, §2 (a), §3 (b), §4 (c), §5 (d), §6 (e), §7 (f), §8 (g), §9 not read); row added to `docs/dev/ledgers/CLAUDE.md` |
| 3. sidecar | `reports/...-first-255bcdd8.interpretation.md` via `pcrecbench interpret` (no `--predictions`: no 0.2 predictions TSV exists), determinism check byte-equal, 14 rules fired |
| 4. O-91 draft | below (report only; not in the outbox) |

Report generation: one detached `setsid nice gnutimeout 3000` job (scratch script,
15 record paths, 186 s load, 337 s total, `DONE rc=0`). `scripts/regen_reports.py`
only re-renders existing groups, so it was not used; the committed header carries
the query. The subject-grain `.tsv` is the slice form (`--subject-grain-slice`)
as in the b91views precedent; the `.subject-grain.md` is also committed.

Validation: `make check-interpret` 250 passed / 0 FAILED in the worktree (section 3
sidecar freshness is green against this worktree's `store/index.tsv`). NOT run: full
`make check`, `make check-report` (untouched code; no code changed in this lane).

## Findings worth the manager's attention (numbers in the ledger)

1. **The 0.1 ledger line does not carry over.** In 0.2 the evil-alt-nested short cell is
   judged. pcrec auto gives up 0 times; the forced VM, pcre2 interp/jit and Oniguruma
   are excluded at the same 0.9733 but for their own give-ups (ledger §4).
2. **[NULLABLE-ANCH] lives on the auto routes only.** The forced VM reproduces O-87's
   c4c70f2c spread (10.6 us / 45.2 ns / 1.16 us); auto is 1.55x (caps) / 2.61x (nocaps).
   The matching tax (K97) is 2.2-3.6x vs the JIT, and on the caps default
   (VM hybrid, `scan=attempt`) the auto route is slower than the forced VM
   (3.06x / 2.18x) on the two 60 KiB matching cells.
3. **Two predictions need a correction.** P12's pcre2-dfa clause: pcre2-dfa TIMES OUT
   (60 s alarm, 5/5) on both near-misses and on both matching cells, it does not
   answer `nomatch`. P13: pcre2-jit is 46.8 us on `\s+$` x t-trim-nearmiss-16k, not
   seconds (interp 1.75 s as predicted). The datefinder x `t-tail-*-1m` JIT cell is 0.20 s,
   not over 1 s.
4. **R11's "number stated on the report" is not met**: the 2 dropped triples (22
   rows) are only in per-row diagnostics. A reporter gap, KB candidate.
5. **Semantics, not wrongness**: RE2 `\s` lacks VT (t-trim-match-60k holds 610 VT),
   and RE2/rust `$` does not match before a final `\n` (`t-1m` ends `\n`). These
   produce the RE2/rust `did-not-match` rows on trim-nested-star, tail-space-eol and
   tail-digits-eol. They are inferences from record bytes, not engine probes.
6. **The spread record was a real mid-run event**: in the discarded vm-in record,
   trials 3 and 4 of one pattern ran >1.5x on 66 and 41 of 75 rows while the summed
   cell stayed 10.355-10.368 ms. v1.4 judged a per-row disturbance the sum hides.
7. **The tail gap is to the end-anchored engines, not the JIT**: pcrec auto is within
   ~20% of pcre2-jit on four tail patterns and 5-6x faster on `.*\.txt$`, and
   824x-127,710x behind RE2/rust (min and max over the 15 cells; the brief's
   7,000-25,000x is inside the four non-memchr patterns' RE2 range 3,146x-30,001x).

## O-91 DRAFT (for the manager to send; not written to the outbox)

> ## O-91 (2026-10-09, bench manager) — capability@0.2's first sample at 255bcdd8 (abi 68): [NULLABLE-ANCH] read, the K97 tax, and the end-anchored tail family
>
> Window 2026-10-08 12:07 - 2026-10-09 00:09 EDT, 14/14 cells (13 at attempt 1; pcrec-vm-in at attempt 3 after a busy-core refusal and one `inconclusive-spread`, kept in the store). Ledger `docs/dev/ledgers/2026-10-09-capability-0.2-255bcdd8.md`; report `reports/2026-10-08-capability-0.2-budu-ryzen1600-first-255bcdd8.*`. First sample of the set: no cross-pin form.
>
> **(a) [NULLABLE-ANCH] holds on the auto routes.** evil-alt-nested short near-misses: auto-nocaps 24.1 ns, auto-caps 29.1 ns (rd-evil-alt-near-miss); sd-empty-alt-hit 70.0 / 72.9 ns. Both auto routes give up 0 times on the two formerly-unjudged subjects; forced vm / vm-in, pcre2 interp+jit and Oniguruma give up 5/5 on both. The spread on `t-64k/t-256k/t-1m` is 1.55x (auto-caps) and 2.61x (auto-nocaps); the forced VM keeps O-87's 10.6 us / 45.2 ns / 1.16 us (235x), so the fix is on the auto routes only. trim-nested-star is flat everywhere (1.00-1.04x).
>
> **(b) K97's matching tax, by route.** whole-subject match (0,61440):
>
> | cell | auto-nocaps | auto-caps | forced vm | pcre2-jit |
> |---|---|---|---|---|
> | evil-alt-nested x t-evil-match-60k | 54.5 us | 81.0 us | 26.4 us | 24.4 us |
> | trim-nested-star x t-trim-match-60k | 73.3 us | 100.2 us | 45.9 us | 27.6 us |
>
> Against the JIT: 2.23x / 2.65x (nocaps), 3.32x / 3.63x (caps). The caps default is a VM hybrid (`vm_prefilter=hybrid, scan=attempt, start=reverse-pass`); nocaps is a DFA (`match=search-filter`). On these two cells auto-caps is 3.06x / 2.18x slower than the forced VM. Which denominator was K97's "2-3x"?
>
> **(c) The end-anchored tail family.** Five patterns (`\d+$`, `\w+\z`, `\s+$`, `[a-z]+\.txt$`, `.*\.txt$`) x the three `t-tail-*-1m` bodies. Every pcrec cell is `engine=dfa, sel=selected, match=unwrapped, start=reverse-pass`, prefilter `byte-class-bounded` (`memchr-bounded` for `.*\.txt$`), and costs the same on all three tails: 0.70 / 2.15 / 1.69 / 2.72 / 0.20 ns/B (auto-caps). RE2 and rust are 94-255 ns and 22-221 ns on the same 1 MiB bodies; vectorscan nosom (boolean grain) 34-146 ns. Ratios (15 cells, computed): vs RE2 default 824x-30,001x, vs rust 952x-127,710x, vs vectorscan 1,855x-65,084x. Against pcre2-jit it is parity: 0.79-0.80x, 1.05-1.07x, 0.91-0.95x, 1.11-1.12x, and 0.17-0.20x (pcrec 5-6x faster on `.*\.txt$`). Same shape on `\s+$` x t-trim-nearmiss-16k: auto 29.1 us vs RE2 95 ns. Where a bound exists pcrec is flat: `(?:[a-z]{0,1024})\z` is 1.29 us on 60 KiB and 1.10 us on 1 MiB. This is [OPT-REVEND]'s measured surface; the 15 cells plus `\s+$` x t-trim-nearmiss-16k are ready as the acceptance cells.
>
> **(d) Forced-VM observations (no ask).** vm / vm-in: both 16 KiB near-misses and waf-942360 x t-trim-match-60k give up 5/5; `rd-trim-near-miss` 10.2 ms (auto 36.5 ns); `\s+$` x t-trim-nearmiss-16k 99.6 ms (auto 29.1 us).
>
> **(e) Unchanged.** datefinder refused on the caps routes at 589,177 / 589,100 B (cap 500,000); nocaps compiles it. 0 wrong answers on any pcrec row. pcrec-vm-in's first record (trials 3-4 of trim-nested-star slowed 1.6x on most rows) was `inconclusive-spread` and is not in the report.
>
> **Predictions scored against NOTES.md** (the bench's, not pcrec's): P11 partly (within 3x of the JIT: nocaps yes, caps no), P12 all but pcre2-dfa, which times out at 60 s on both near-misses, P13 half (pcre2-interp 1.75 s; pcre2-jit 46.8 us), P14-P16 confirmed. The semantic differences behind the RE2/rust `did-not-match` rows (RE2 `\s` has no VT; `$` before a final newline) are not pcrec matters.
>
> **Asks.** (1) Which denominator and cell is K97's "2-3x", and is the caps default's VM hybrid expected to be slower than the forced VM on matching subjects? (2) For [OPT-REVEND], please state predicted values for the 15 tail cells (and `\s+$` x t-trim-nearmiss-16k) before the AFTER window; we will score against them. (3) Which cell does the ~22 ns figure refer to (rd-evil-alt-near-miss reads 24.1 / 29.1)?

## Charter-vs-committed checklist (session_discipline.md §7(c))

| promise in the brief | status |
|---|---|
| worktree `lane/b125read`, incremental commits | done: `fac0767`, `68efc6a`, `6cc2469` + this report |
| 1. reports named `reports/2026-10-08-capability-0.2-budu-ryzen1600-first-255bcdd8.*`, set + subject grain, tsv/md/matrix/subject-grain slice | committed (also `.subject-grain.md`) |
| 1. pcrec-only cross-pin form or say not like for like | skipped, stated (ledger §0, §9; reports/CLAUDE.md) |
| 2. ledger in the newest ledger's shape, report-line citations | committed; citations as `SG/S/MD L<n>`; computed ratios marked |
| 2(a) [NULLABLE-ANCH] with t-evil-*/t-trim-* | ledger §2 |
| 2(b) throughput spread vs first-word length | ledger §3 |
| 2(c) which of 0.1 / 0.2 the "unjudged" line applies to | ledger §4: 0.1 only; 0.2 judged |
| 2(d) P11-P16, R9-R11, the predicted pcre2 >1 s cells | ledger §5 (each verdict + line citations) |
| 2(e) tail-* family with route stamps | ledger §6 (stamps from MD L24231-L24240) |
| 2(f) pcrec-vm-in attempt history + kept spread record | ledger §7 |
| 2(g) ranked candidates + asks | ledger §8 |
| 3. interpretation sidecar | committed, deterministic, `make check-interpret` 250/0 |
| 4. O-91 draft in the report only | above; `docs/dev/outbox_to_pcrec.md` NOT touched |
| detached store loads, one at a time | one load, detached, marker `DONE rc=0` checked |
| do not push | not pushed, not merged |
| OWED | nothing owed by this lane. Manager: merge; decide whether to turn R11's reporter gap into a KB entry; send O-91; `make check-report` (not run; no code changed). |

## Files

- `/home/duxevents/pcrec-bench/worktrees/b125read/docs/dev/ledgers/2026-10-09-capability-0.2-255bcdd8.md`
- `/home/duxevents/pcrec-bench/worktrees/b125read/reports/2026-10-08-capability-0.2-budu-ryzen1600-first-255bcdd8.*`
- `/home/duxevents/pcrec-bench/worktrees/b125read/docs/dev/lanes/b125read_report.md` (this file)
