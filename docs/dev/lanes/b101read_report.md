# lane b101read report — THE READ of [B101]'s twin window (capability@0.1 at pcrec 02902356)

**Branch**: `lane/b101read` (worktree `worktrees/b101read`, from master 646dee3).
Writer lane; no measurement, no store write, no build.

## 0. Deliverables

| item | file |
|---|---|
| report group (a), SAME-PIN TWIN | `reports/2026-09-26-capability-0.1-budu-ryzen1600-twin-noreqbyte-02902356.{tsv,md,subject-grain.md,subject-grain.tsv,matrix.tsv,matrix.html,interpretation.md}` |
| report group (b), CROSS-PIN AFTER | `reports/2026-09-26-capability-0.1-budu-ryzen1600-after-02902356.{…same seven…}` |
| ledger | `docs/dev/ledgers/2026-09-26-noreqbyte-twin-02902356.md` (+ its row in `docs/dev/ledgers/CLAUDE.md`) |
| predictions scored | `docs/dev/predictions/capability-0.1-noreqbyte-twin-02902356.tsv`, 12/12 hold (entry updated in `docs/dev/predictions/CLAUDE.md`) |
| O-61 draft | §3 below (NOT written to outbox_to_pcrec.md) |

**How the reports were rendered.** Each group's `.tsv` was rendered with
the CLI first (26-27 s, 270 MB RSS: two records, so no KB-16 load). The
other five siblings were placeholders re-rendered by
`scripts/regen_reports.py --only <label>`, 26-33 s per file. A render
can be reproduced from its own header line. **Note**: `--only` is `nargs="*"`, so
`--only A --only B` keeps only the last label. The correct usage is
`--only A B`. This was my usage error, not a script defect, and I re-ran
the script for the second group.

Sidecars were generated with `/pcrec-bench-interpret`, with
`--subject-grain` passed for both. Each was rendered twice and the two
renders were byte-equal (deterministic).

## 1. Findings (numbers in the ledger; row citations there)

1. **Answers (I-111)**: CONFIRMED. 24,180 of 24,180 match rows are
   identical to ce658cb7 on both 02902356 records, with timing, seq and
   trial excluded from the comparison. 0 wrong. The 10 `gave-up` rows
   are identical on all three records (`evil-alt-nested` srch). There
   are 0 compile-outcome movers.
2. **Twin clauses: 12/12 hold.**
   - IMPROVE: all five are ×55.7-×580 on thr, and every default thr cell
     sits at the floor's own ~23.1 µs.
   - Pure twins: `floor-byte` 1.0002 / 1.0001 and `uuid-grok` 0.9994,
     all inside the same-window noise.
3. **Same-window noise from the twin's own 87 program-identical cells**
   (it was not borrowed): ±1.96% thr ≥1us, ±2.25% srch 100ns-1us,
   ±2.44% srch ≥1us, ±6.80% thr <100ns. The predictions' ±16.62% /
   ±12.72% were 8.5× / 5.7× too generous.
4. **P7 holds as written, but the pre-check costs +5.46% on
   `float-literal-bound` thr** (the trial ranges are disjoint). The same
   pattern appears unpredicted on `wild-waf-crs-942160-sleep-benchmark`
   thr (+7.02%) and `wild-secrets-slack-webhook-url` thr (+3.79%,
   S1-confounded).
5. **github-pat / router**, read as REQBYTE and the S1 prefilter
   together: github-pat thr 1.0023 (equal), srch 0.9313; router thr
   0.8754, srch 0.8953. The default's pre-check is elided (`dominated`),
   so router's −12.5% attributes to the run-pinned prefilter by the
   stamps. No isolating arm exists.
6. **The AFTER by cause.**
   - [B88]'s field-first identity fired for the first time, on 123/123
     cells, and agrees with the census on every cell (95 identical / 28
     changed).
   - S1BUILD: 4 improve, **5 regress**. I-111 predicted "never a
     regression".
     - `wild-secrets-github-pat` srch +39.60%.
     - `wild-semdiv-dollar-trailing-newline-pcre2` thr +45.87% and srch
       +41.30%.
     - `keyword-prefix-order` srch +6.70% and `slack-webhook` srch
       +6.47%.
   - The subject grain shows a per-call constant. A failing short
     subject took ~8 ns under ce658cb7's whole-window pre-check and
     takes ~12-16 ns under 02902356's run-pinned scan with that
     pre-check elided. On github-pat srch this holds on 75/75 subjects.
   - S1STEP6-only srch +7.36% / +8.74%, and K65K66(+S1STEP6) srch +2.44%
     to +8.27%. The thr cells are all within the bar.

## 2. Validation

- `make check-interpret`: **212 passed, 0 FAILED** (210 at master + the
  two new sidecars).
- The predictions were scored with the normal CLI (`pcrecbench interpret
  … --predictions`, `check_stated_utc` enabled). **The bypass that
  b101pred_report.md §3 named was NOT needed and NOT used.** The F27
  anchor did not fire because the report's population (two testee ids
  first measured 2026-09-27T00:34Z) postdates the file's `stated_utc`
  (2026-09-26T23:55Z). The 25b1984f-confirm files' populations included
  older-pin records. I confirmed this by first calling
  `interpret.interpret(..., check_utc=True)` directly, which accepted the
  file.
- Every clause value was re-read by hand from the TSV rows. The ledger
  §1 table cites each row's line number.
- Not run: `make check` in full, and check-harness / check-report. No
  harness or reporter code changed, only committed reports, a sidecar
  pair and docs.

## 3. DRAFT — O-61 (for the manager; not written to the outbox)

> ## O-61 (2026-09-26, pcrec-bench manager) — 02902356 on capability@0.1: [OPT-REQBYTE]'s owed twin (12/12), 0 answer changes, and S1BUILD's short-subject cost
>
> Window 2026-09-26 20:34-21:41 EDT, capability@0.1 × {pcrec-auto,
> pcrec-auto-noreqbyte (`-fno-req-byte`)} at 02902356, 2/2 measured at
> attempt 1. The cross-pin AFTER reads the same pcrec-auto record against
> ce658cb7's (the [B90] window). Ledger:
> docs/dev/ledgers/2026-09-26-noreqbyte-twin-02902356.md. Reports:
> reports/2026-09-26-capability-0.1-budu-ryzen1600-{twin-noreqbyte,after}-02902356.*.
>
> 1. **ANSWERS: none changed**, as you predicted. 24,180 / 24,180 match
>    rows are identical to ce658cb7 on both records. The same 10 known
>    `evil-alt-nested` give-ups appear, there are 0 wrong answers and 0
>    compile-outcome movers.
>
> 2. **THE OWED [OPT-REQBYTE] TIMING — every landing-bar cell as you
>    predicted.** The ratio is default / `-fno-req-byte` at set grain.
>    Same-window noise from the twin's 87 program-identical cells is
>    ±1.96% on thr ≥1us.
>    - IMPROVE, thr:
>      - username-password-pair 0.0180 (×55.7)
>      - winpath-grok 0.0067 (×150)
>      - tag-depth3-bound 0.0052 (×194)
>      - dup-param-detect 0.0017 (×580)
>      - tag-pair-match 0.0050 (×201)
>
>      Every default cell reads 23.10-23.14 µs, the floor pattern's
>      own 23.13 µs. The srch cells also improve, by −42% to −89%.
>    - DO-NOT-REGRESS:
>      - floor-byte thr 1.0002 and srch 1.0001; uuid-grok thr 0.9994.
>        These are program-identical, so "may read identical" is
>        confirmed.
>      - nested-comment-rec thr 0.0030 (×336). The ~400× win is intact.
>      - github-pat thr 1.0023.
>      - **float-literal-bound thr 1.0546**. The pre-check is +5.5%
>        overhead where the byte is present, and the trial ranges are
>        disjoint. It is inside our stated 16.6% ceiling but outside the
>        noise. The same shape appears unasked on
>        wild-waf-crs-942160-sleep-benchmark thr (+7.0%, program
>        unchanged since ce658cb7).
>    - router-prefix-order thr 0.8754, srch 0.8953. The default's
>      pre-check is `dominated` (elided), so the −12.5% is S1's
>      run-pinned prefilter vs the twin's memchr, by the stamps.
>
> 3. **S1BUILD is NOT "never a regression" on short subjects.** The
>    cross-pin D119 bar over pcrec-auto uses 95 program-identical cells
>    as the band: ±4.03% thr ≥1us, ±1.41% / ±2.35% srch. S1BUILD's 16
>    cells:
>    - Improve: router-prefix-order thr −52.2% and srch −3.1%;
>      keyword-prefix-order thr −40.8%; uuid-grok srch −12.0%.
>    - Regress:
>      - wild-secrets-github-pat srch +39.6% (1,085 → 1,515 ns/set)
>      - wild-semdiv-dollar-trailing-newline-pcre2 srch +41.3% and thr
>        +45.9% (26.9 → 39.2 ns)
>      - keyword-prefix-order srch +6.7%
>      - wild-secrets-slack-webhook-url srch +6.5%
>
>    At subject grain it is a per-call constant. On github-pat srch, 75
>    of 75 subjects are slower and a typical failing subject goes from
>    8.3 to 16.2 ns. On dollar-trailing srch, 69 of 75 are slower (8-12
>    → 12-16 ns). ce658cb7's whole-window memchr pre-check dismissed a
>    short non-matching subject faster than 02902356's run-pinned DFA
>    scan does with that pre-check elided. On 1 MB subjects the elision
>    is flat or a large win. Question: is `dominated` meant to be a
>    throughput-regime identity only, or should G1 keep the pre-check
>    where the subject is short?
>
> 4. **K65K66 and S1STEP6 on short subjects.** All thr cells are within
>    the bar.
>    - K65K66(+S1STEP6) srch: tag-depth3 +8.3%, tag-pair +6.9%,
>      balanced-parens +2.4%. This fits your "small regression".
>    - S1STEP6-only srch: nested-comment-rec +7.4% and
>      wild-waf-crs-942500 +8.7%. You predicted "flat, at most
>      call-overhead noise". It is outside our noise. At these cells'
>      scale (~640-1,580 ns over 75 subjects) it is about +1 ns per
>      call.
>
> 5. **Bench-side, FYI.** This is the first pin pair where both sides'
>    records carry `program_sha256`. The reporter's field-first identity
>    agrees with our census on 123 of 123 cells. Your two axis points
>    under review, (3) `-fno-req-byte` also dropping S1's run-pinned
>    prefilter on github-pat/router and (4) bit 30 in `rx_info.flags`,
>    are NOT re-derived here. Items 2's router/github-pat readings are
>    confounded exactly as (3) says.
>
> No action needed tonight. The asks are: item 3's question, and whether
> item 4's S1STEP6 short-subject cost is expected.

## 4. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 1a | render group (a), same-pin twin, + sidecar via the skill | DONE | `reports/…twin-noreqbyte-02902356.*` (c7d4c58, sidecar next commit) |
| 1b | render group (b), cross-pin AFTER, attribution by cause with the identical rows as null control | DONE | `reports/…after-02902356.*`; ledger §3 |
| 1c | narrow queries (capability + the needed testees only); detached if >4 min | DONE: every render took 26-33 s, so nothing needed detaching | §0 |
| 2 | score the 12 clauses with `pcrecbench interpret`; follow the stated-UTC bypass precedent | DONE, 12/12 hold. **The bypass was not needed** (§2), and the deviation from the brief is stated here and in the ledger §1.1 | ledger §1; predictions/CLAUDE.md |
| 2b | verify each clause by hand, citing file+row | DONE | ledger §1 table (TSV line numbers) |
| 2c | github-pat/router as REQBYTE + S1 prefilter together | DONE | ledger §1 |
| 2d | floor-byte ×2 + uuid-grok as same-window noise, vs ±16.62/±12.72 | DONE, extended to all 87 identical twin cells | ledger §2 |
| 2e | IMPROVE wins vs same-window noise, not just <1 | DONE | ledger §1 last column |
| 3 | I-111 answer-level: zero wrong / changed answers vs ce658cb7 | DONE, CONFIRMED | ledger SUMMARY A |
| 4 | ledger (facts; read and NOT read; numbers cited) | DONE | `docs/dev/ledgers/2026-09-26-noreqbyte-twin-02902356.md` §5 |
| 4b | O-61 DRAFT in this report; axis facts (3)/(4) as context only | DONE | §3 |
| 5 | make check-interpret green after sidecars | DONE, 212/0 | §2 |
| — | plan.md / journal / outbox | NOT touched (the manager's) | — |

OWED: nothing from this lane.
