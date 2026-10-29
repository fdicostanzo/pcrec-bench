# b148l9read report -- the READ of [B148] L9 (unusual@0.1 scratch readout, pcrec 614d45eb3)

Lane b148l9read (Sonnet), branch `lane/b148l9read`, 2026-10-29. Read-only over the scratch store; no timing, no
`pcrecbench run/quick`, no `callout_calib`, `store/` untouched, no script cap changed, nothing under `bench/unusual/` touched
(so `make check-unusual` was not run). The derivation is the ledger
`docs/dev/ledgers/2026-10-29-unusual-0.1-l9-scratch.md` (section numbers below are its); the reports are
`docs/dev/measurements/2026-10-29-b148-l9-{stream,set-throughput,set-short}.md` (reports/CLAUDE.md admits no scratch-tier
report group, so they live under measurements/ with source headers); helpers: `.../2026-10-29-b148-l9-scripts/`.

## Charter-vs-committed checklist

| brief item | where |
|---|---|
| 1 reports (stream grain; set grain for the rest; scratch admitted? no -> measurements/ with header, said so) | `docs/dev/measurements/2026-10-29-b148-l9-*`; large loads run detached (setsid, gnutimeout, marker `DONE rc=0`, outputs under `/var/tmp/pcrecbench/b148l9read/`) |
| 2(a) verdict table x outcome x MB/s or ns/call, deep-arm high-water | ledger 1(a), 1(a'), 1(g) deep-storage table |
| 2(b) why 7 cells inconclusive-load | ledger 1(b) |
| 2(c) the 2 all-timed-out groups | ledger 1(c) |
| 2(d) wall times, CELL_CAP_unusual proposal, `scripts/CLAUDE.md` cell-length table | ledger 1(d); `scripts/CLAUDE.md` (a row added; NO cap value changed) |
| 2(e) callout fires, callee share, >40 % flags, e0e68c3e order | ledger 1(e) |
| 2(f) latent risks | ledger 1(f) |
| 2(g) cscan headline | ledger 1(g), 1(g') |
| 3 report with outbox DRAFT (pcrec only) + upstream CANDIDATES (other engines, separate) | below; the outbox and `upstream_findings.md` NOT written |

## Verdicts (each: what was read, what was not)

1. **7 of 19 cells are `inconclusive-load` because of a roaming 10-16 % competitor on non-target cores plus a standing 5-6 %
   background, not because of the pin and not load1.** Pinned to cpu7 on all 19; load1 `quiet` on all 19; the target core was over
   the limit in 1 of 7 (pcre2-interp, 10.64 %); in the other 6 a *different* core each time read 10.9-15.9 % in the 5 s `mpstat`
   average; the per-group timeline shows median other-core max 5.3-6.3 % in every record; the 12 `measured` ones sit at 5.2-9.96 %.
   The opening `quiet` in `chain.log` was NOT QUIET (3 of 5). Trial agreement found 0 disagreeing groups on all 19. NOT read: which
   process the load was (no per-process accounting exists).
2. **The cap proposal: `CELL_CAP_unusual=7200` (x2.4 the worst, 3,009 s pcre2-interp); ~9000 is also safe.** Window 6.15 h; deep arms
   x1.0 libpcre2, x1.95 pcrec, x1.97 Onig. Not applied.
3. **The two all-timed-out groups = `cscan` and `cscan-onig` on `nest-brace-100k`** on pcre2-interp, pcre2-interp-deep, onig-deep: a
   quadratic pathology (interp 8k 1.64 s -> 32k 31.0 s, exponent ~2.1, 100k ~320 s; onig-deep 32k 9.2 s, 100k ~86 s) cut by the 60 s
   per-subject cap; pcre2-jit-deep (2.4 ms) and pcrec `_in` (11.6 ms) answer it linearly.
4. **Predictions (NOTES.md section 4, pre-run):** D-1 (Onig silent nest level 20) CONFIRMED to the letter; D-2 pcre2-jit "first give-up
   at 512" CONFIRMED; D-2 pcre2-interp "answers every rung" confirmed to 32k (100k = the cap); **D-2 pcrec default "FRAMES from 512"
   REFUTED** (gives up at 128, and on non-nesting 1-5 MB inputs); D-5 (tenant ladder flat for pcrec, assists grow) CONFIRMED.
5. **Callouts:** every native and assisted engine fires the same counts (11,308 / 8,429 / 13,158 on the three filter members;
   935,341 on the *fixed* co-netstr-1m: the window ran 8 h after e0e68c3e and the record's sha256 matches the manifest). pcrec's native
   `consume` fires 34,127 (x27.4 fewer). Calibrated shares: filter members 3-24 %; co-netstr-assist 18.4-79 %, **flags (>40 %)** on
   pcre2-jit 41.0, jit-deep 76.7, pcrec-auto 78/79, pcrec-vm 49/51 -- on a calibration taken at load 8.6-10.7 and BEFORE the payload
   fix, so indicative only. NOT read: a fresh quiet-box calibration (OWED).
6. **Latent risks:** R10B-5/6 not seen; R10B-10/11 cannot surface (those vars assists are NOT-CAPABLE); R10A-7 not seen on this subject
   (0.94 fires/byte, no timeout), the held-out worst-case junk is not in the set.
7. **cscan headline:** pcre2-jit 1,421 MB/s on comment-5m vs pcrec `_in` 602 (x2.4 behind) vs interp 147 vs Onig 92 vs RE2-assist 484;
   on the cscan call stream pcrec `_in` is x3.1-3.3 behind the JIT (46.7 vs 14.3 ms on seg-l); the default pcrec arm gives up on 39-53 %
   of stream calls.

## Findings the brief did not ask for

- pcrec runs only the `-onig` variants (`cscan`, `wild-json-validate` unsupported: `conditionals` undeclared).
- The vectorscan co-netstr ASSIST costs 7.01 s per 1 MB call (0.14 MB/s) vs RE2 3.9 ms / Rust 2.2 ms: an assist-shape cost (R4
  ASSISTED), worth a look by the assist lane, no engine claim.
- pcre2-interp uses 960 MiB of its 1 GiB default heap on a 1 MB JSON (js-1m): 6 % from giving up.

## OUTBOX DRAFT for pcrec (findings about pcrec only; the manager writes O-n)

> **O-? DRAFT -- unusual@0.1 first (scratch) readout at 614d45eb3, abi 89.** Scratch tier, ryzen7700x, 19 cells, 12 measured / 7
> inconclusive-load (pcrec-auto is one of the 7; pcrec-vm, auto-in, vm-in are measured and agree with it to 1.5 %). All pcrec rows are
> correct answers (0 wrong on 4 pcrec testees); the findings are limits and rates. Ledger
> docs/dev/ledgers/2026-10-29-unusual-0.1-l9-scratch.md.
>
> 1. **Default-arm frame exhaustion on NON-nesting input.** On `cscan-onig` the stack-resident arm (131,072 B, 2,048 resume / 3,072
>    trail frames) returns `PCREC_ERR_FRAMES` at `nest-brace-128` and on `comment-5m`, `idents-1m`, `splice-1m`, `nest-paren-512...100k`
>    (cscan reads parens as plain bytes), 19 of 23 throughput subjects and `cs-nest-100`; on the compiler's own call stream it gives
>    up on 100/256, 1,723/4,096, 163/311 and 2,620/4,971 calls (39-53 %). Working storage on the 1 GiB `_in` arm scales with the SUBJECT
>    LENGTH on flat input (idents-1m 138.8 MiB, ~139 B/byte; comment-5m 7.6 MiB; wild-json js-1m 323.6 MiB), so frames accumulate per loop
>    iteration of `(?:...)*+` containing `(?&sp)` calls rather than per nesting level. Our D-2 prediction ("frames from the 512 rung",
>    from limits.md 4's ~342 levels) is refuted. Ask: is the retention across a possessive loop's iterations intended, and is
>    releasing at iteration end (or a larger default for recursive patterns) on the table? The stream is the pattern's real customer.
> 2. **`conditionals` / verbatim cscan.** `cscan` is pcrec's own tests/recursion/cscan.rxt (uses `(?(DEFINE)`); the bench measures
>    pcrec on the `(?<n>...){0}` variant only because the testees do not declare `conditionals`. Please confirm pcrec supports the
>    DEFINE spelling (then we declare it) or state the gap.
> 3. **Rates behind the JIT on the recursive members (R1, > 3x):** cscan-onig short search x3.6 (296 vs 81 ns/call), nest-paren-32k
>    (no recursion) x5.4 (35 vs 190 MB/s), idents-1m x3.0, nest-brace-100k x4.8 (11.6 vs 2.43 ms), wild-json-validate short x4.8 and
>    **js-1m x21.9 (7.7 vs 168 MB/s; Onig 13.4)**. comment-5m (x2.4) and splice-1m (x2.5) inside the band. Stamps: engine `vm`
>    `selected`, prefilter `none`, `RX_REQ_RUN` `(?{`@1, compile 395 ms. We have not isolated a mechanism.
> 4. **Wins, for the record:** native `consume` co-netstr 1.51 ms per 1 MB (x5.4 faster than the check-at-end spelling on pcre2-jit, x12.9
>    than the pcre2 host-loop assist); co-luhn 1,073 vs 888 MB/s (x1.21 over pcre2-jit; co-isbn / co-member x0.68); caller-variable
>    streams flat in distinct values (194 -> 219 us over 4 -> 4,096 bindings) vs RE2 x14.8 / Rust x19.9, break-even 97k calls at d4096;
>    `unterminated-5m` 145 GB/s (consistent with the `RX_REQ_RUN` dismissal -- please confirm this is the intended mechanism for a
>    subject without the run). 100k-deep nesting answered at 11.6 ms where libpcre2's interpreter needs > 60 s.
> 5. Context only (not an ask): pcre2-jit gives up `-46` from nest-brace-512 with its default 32 KiB JIT stack; Onig's default nest
>    level 20 is silent (wrong, not a give-up).

## Upstream-finding CANDIDATES (other engines; unambiguous bugs only -- the rule filters most of these out)

No clean candidate. Listed so the manager can close them NOT-A-BUG on the record:
- **libpcre2 10.46 interpreter, super-quadratic time on deep subroutine recursion** (31 s at nest-brace-32k; already flagged in NOTES.md
  section 3 and the syntax census). A design property of heap-frame recursion, not a wrong answer -> NOT-A-BUG under the rule.
- **libpcre2 JIT `-46` at 512 nesting levels** with the default 32 KiB JIT stack: a documented, configurable limit, reported as an error.
- **Oniguruma silent no-match beyond subexp-call nest level 20** (`onig_set_subexp_call_max_nest_level`, default 20): confirmed by D-1
  and the whole depth table -- a WRONG ANSWER with no error, which is the one borderline item (documented knob, undocumented silence);
  NOTES.md leaves it to the manager (Q-D). Evidence is in the ledger's 1(a').
- libpcre2 interpreter heap 960 MiB on a 1 MB JSON at the default 1 GiB heap limit: a limit, not a bug.

## Reader / harness findings (bench-side, for KB)

stream grain: `state` column prints the cell outcome, so numbers from `inconclusive-load` records read `measured`; `--callee-calib`
joins on the full testee id while `callout_calib.py` writes the config id (SHARE is `-` on every row); the callout split lists
10,626 zero-valued short-subject rows; the break-even lines call native engines "assisted"; set-grain ranks assisted and native
testees in one column with the label only in the id suffix (R4). `b148l9_chain.sh`'s opening `quiet rc=3` was advisory.

## OWED (owner / trigger)

- a quiet-box `callout_calib` re-run (manager; the co-netstr shares and the >40 % flags depend on it);
- a re-run of the 7 IL cells inside a genuinely exclusive pinned window (manager);
- pcrec's answer to ask 2 (declare `conditionals` or not) before any pinned unusual@0.1 sample;
- `make check` was not run: no code, bench, or schema file changed (docs and measurements only).
