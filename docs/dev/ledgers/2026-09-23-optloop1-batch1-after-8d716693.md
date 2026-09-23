# THE LEDGER — capability@0.1's [OPTLOOP] cycle 1 batch-1 AFTER at pcrec 8d716693 (abi 29)

Read-only extraction, no diagnosis, per inbox_from_pcrec.md I-87/I-88 (the
[B74] (b) ask). Scores the AFTER window's per-cell numbers against
I-87(b)'s named targets and carve-outs, per the D119 landing bar as I-87(a)
states it: **a TARGET cell must improve by more than its IQR; every OTHER
cell must not regress by more than its IQR.** Numbers only; the manager's
interpretation and the outbox item (O-45) are not this lane's to write.

**BEFORE** = `reports/2026-09-22-capability-0.1-budu-ryzen1600-wrapfix-25b1984f.tsv`
(the [B71]/wrapfix second sample, pcrec pin **25b1984f**, abi 27) and its
four `pcrec_25b1984f_*` records timestamped 2026-09-22T02:11-04:39Z.
**AFTER** = `reports/2026-09-23-capability-0.1-budu-ryzen1600-after-8d716693.tsv`
(pcrec pin **8d716693**, abi 29) and its four `pcrec_8d716693_*` records
timestamped 2026-09-23T03:19-05:52Z. Both reports are `--grain set`;
the AFTER report is a CROSS-PIN render carrying both pins' testees plus
`oniguruma`/`rust`/`vectorscan`, with the reporter's own `delta_verdict`
column — used here only as a cross-check (§0.3), never as the source of
the D119 verdicts, which this ledger computes independently from the
records (see §0.2).

**Ratio/percentage convention: `(after − before) / before`, so a
positive `Δ%` is SLOWER (a regression) and a negative `Δ%` is FASTER (an
improvement), for every table in this ledger.**

---

## 0. SOURCES, SAMPLE SHAPE, HYGIENE — what was read, and how

### 0.1 The eight records

| side | testee | record file (`store/records/capability@0.1/...`) | trials | subjects (thr / srch) |
|---|---|---|---|---|
| before | `pcrec_25b1984f_auto-caps-simdna` | `.../capability@0.1__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260922T021127Z.jsonl` | 5 | 3 / 75 |
| before | `pcrec_25b1984f_auto-nocaps-simdna` | `...20260922T024402Z.jsonl` | 5 | 3 / 75 |
| before | `pcrec_25b1984f_vm-caps-simdna` | `...20260922T031341Z.jsonl` | 5 | 3 / 75 |
| before | `pcrec_25b1984f_vm-in-caps-simdna` | `...20260922T035712Z.jsonl` | 5 | 3 / 75 |
| after | `pcrec_8d716693_auto-caps-simdna` | `.../capability@0.1__pcrec_8d716693_auto-caps-simdna__budu-ryzen1600__20260923T031941Z.jsonl` | 5 | 3 / 75 |
| after | `pcrec_8d716693_auto-nocaps-simdna` | `...20260923T035507Z.jsonl` | 5 | 3 / 75 |
| after | `pcrec_8d716693_vm-caps-simdna` | `...20260923T042632Z.jsonl` | 5 | 3 / 75 |
| after | `pcrec_8d716693_vm-in-caps-simdna` | `...20260923T050923Z.jsonl` | 5 | 3 / 75 |

Every record is `kind: setup` (×1) + `kind: compile` (×623 for the
`-caps`/`vm-*` testees, ×624 for `auto-nocaps` — one more pattern
compiles under `nocaps`) + `kind: match` (×24,180-24,184). Read in full;
these are the ONLY files this ledger's numbers come from (see §0.2). The
two `.subject-grain.tsv` files (33 MB BEFORE-side wrapfix report, 54 MB
AFTER report) were **not opened** — every subject-grain number this
ledger needed is reconstructable, and was reconstructed, from the
records themselves (below), which carry the identical raw rows the
subject-grain TSV is rendered from. The two `.md`/`.matrix.html` renders
and both `.interpretation.md` sidecars were **not read** — this ledger
does not depend on the interpreter's prior pass.

### 0.2 Arithmetic used — the SAME module the reporter imports

Medians, IQRs and verdicts below are computed by importing
`pcrecbench.reduce` directly (`cells_from_record`, `reduce_set_cell`,
`reduce_match_cell`, `judge_trial_agreement` — the exact functions
`report.py` calls for `--grain set`), not a re-implementation. Per
`reduce_set_cell`'s own doc: for one (pattern, regime, form, testee),
each of the 5 trials contributes ONE number — the sum, over every
subject in the regime (3 for throughput, 75 for search), of that
subject's `elapsed_ns / iterations` for that trial. `sums` is that
length-5 list; `median_ns` is `statistics.median(sums)` — the number
both reports print.

**IQR method (stated once, applied identically both sides): Type-7 /
Hyndman-Fan linear interpolation (NumPy's default, `statistics.quantiles
(..., method='inclusive')`, equivalently Excel's `QUARTILE.INC`), Q1 =
25th percentile, Q3 = 75th percentile.** For exactly 5 sorted values
`x0<=x1<=x2<=x3<=x4` this interpolates to an INTEGER index both ends (no
fractional step): Q1 = x1 (the 2nd-smallest), Q3 = x3 (the 2nd-largest),
so **IQR = x3 − x1** — the spread of the three central trials, dropping
one extreme on each side. A cell whose SET is expectation-failing (any
subject `gave-up`/wrong/timed-out on any trial) carries no median/IQR at
all (`reduce_set_cell`'s own exclusion rule) and is reported as MISSING,
never interpolated.

**Cross-check against the committed TSV (not the source of the
verdicts, a confirmation of them):** `bracket-array-define` /
`large-subject-throughput` — this ledger's before/after medians for all
four pcrec testees (4,881,399.574074 / 4,877,809.132075 / 4,879,347.870370
/ 4,879,964.200000 before; 73.684296 / 72.958925 / 72.369 / 89.535163
after) match the AFTER report's `rank` rows
(`reports/2026-09-23-...-after-8d716693.tsv`, `median_ns` column) to
every printed digit; `router-prefix-order` / `large-subject-throughput` /
`auto-caps` likewise (393,757.008621 before, 398,422.848062 after,
matching the report's own `slower ×1.01` row exactly). This ledger's
numbers and the committed report's numbers are the same arithmetic
read twice, not two arithmetics.

### 0.3 Window provenance (BEFORE and AFTER)

Both windows: 5 trials, **X13 (v1.4 pre-flight + trial agreement)
`agree` on ALL EIGHT records, 0 `groups_disagreeing` on every one**,
attempt 1 throughout (no `inconclusive-spread` re-measure on either
side).

| side | testee | pre-flight load (before → after, 1-min avg) | worst other-core busy% (limit 10%) | trial-agreement verdict | rows_disagreeing / rows_judged |
|---|---|---|---|---|---|
| before | auto-caps | 0.18 → 1.11 | 4.22% | agree | 6 / 4834 |
| before | auto-nocaps | 0.79 → 1.00 | 3.22% | agree | 3 / 4912 |
| before | vm-caps | 0.73 → 1.00 | 0.80% | agree | 5 / 4829 |
| before | vm-in-caps | 0.73 → 1.00 | 0.80% | agree | 6 / 4829 |
| after | auto-caps | 0.01 → 1.00 | 1.60% | agree | 6 / 4834 |
| after | auto-nocaps | 0.73 → 1.03 | 1.80% | agree | 6 / 4912 |
| after | vm-caps | 0.75 → 1.06 | 1.40% | agree | 4 / 4834 |
| after | vm-in-caps | 0.76 → 1.00 | 1.40% | agree | 7 / 4834 |

BEFORE window ran 2026-09-22T02:11:22Z → 04:39:12Z (≈2h28m wall across
the four cells, per-cell `load.after.sampled_at`); AFTER window ran
2026-09-23T03:19:36Z → 05:51:45Z (≈2h32m). All eight `occupancy.*.verdict`
read `pass`; the highest single reading anywhere is 6.06% (BEFORE,
auto-nocaps, `phone-palindrome-6`/`short-subject-search`'s
worst-disagreeing group's own core) — the report header's own
`worst_other_core_busy: 62.5%` line names an OLDER record
(`pcrec_25b1984f_auto-caps-simdna` / `wild-validator-ipv4-owasp` /
`large-subject-throughput` from the FIRST 25b1984f sample, 2026-09-20,
which the wrapfix filter's `since`/`until` window excludes from the
actual BEFORE cells read here — read, not carried forward as this
window's own hygiene number). Every note field on the AFTER side that
carries a compile-refusal explains itself by name (`wild-datetime-
datefinder-alternation` too large on both `-caps` forms on both pins,
unchanged by the pin) — no undocumented refusal.

**KB-27 check (I-88's standing item, brief's explicit ask):**
`evil-alt-nested` × `{rd-evil-alt-near-miss, sd-empty-alt-hit}` under
`short-subject-search` were read directly at the per-subject
`reduce_match_cell` level on all four AFTER testees and both BEFORE/AFTER
`auto-caps`: **both subjects' outcome is `gave-up` on all 5 trials on
every testee, on both pins** (`outcome_counts={'gave-up': 5}`,
`n_wrong=0`, `n_no_expectation=0`). This is a genuine engine give-up
(a resource limit), not the `did-not-match-as-expected`/no-expectation
confusion KB-27 fixed — it is what takes the WHOLE
`evil-alt-nested`/`short-subject-search` SET cell out on all four
testees on both pins (`reduce_set_cell`: any one failing subject voids
the set), independent of KB-27. No wrong-answer exclusion applies to
either named subject, confirming the brief's own note.

---

## 1. THE D119 TABLE — named targets and carve-outs, all four configs

Two IQR readings are shown per row (`verdict (before-IQR / after-IQR)`)
because I-87(a)'s wording ("more than their IQR") does not say which
cell's IQR "their" is. **Primary reading used for the pass/fail call
below is the BEFORE cell's IQR** (the baseline spread the change is
measured against); the AFTER-IQR reading is carried alongside per the
brief's ask. **Among the 41 target rows and 32 carve-out rows below,
exactly ONE flips between readings**: `floor-byte` /
`large-subject-throughput` / `auto-caps` reads `improve` under
before-IQR (Δ = −29.4 ns vs. before-IQR 17.86 ns) and `within-bar`
under after-IQR (after-IQR 37.10 ns > 29.4 ns) — both readings agree it
is NOT a regression, so the flip does not change any pass/fail call.

### 1.1 TARGET CELLS (I-87(b))

| pattern | regime | testee | before median (ns) | before IQR (ns) | after median (ns) | after IQR (ns) | Δ% | verdict (before-IQR / after-IQR) |
|---|---|---|---|---|---|---|---|---|
| tag-depth3-bound | large-subject-throughput | auto-caps | 4,497,628.2 | 6,586.5 | 23,141.0 | 11.221 | -99.4855% | improve / improve |
| tag-depth3-bound | large-subject-throughput | auto-nocaps | 4,685,352.5 | 3,295.7 | 23,159.7 | 27.846 | -99.5057% | improve / improve |
| tag-depth3-bound | large-subject-throughput | vm-caps | 4,507,247.6 | 26,068.5 | 23,177.1 | 5.647 | -99.4858% | improve / improve |
| tag-depth3-bound | large-subject-throughput | vm-in-caps | 4,488,622.5 | 2,866.6 | 23,113.9 | 31.768 | -99.4851% | improve / improve |
| dup-param-detect | large-subject-throughput | auto-caps | 13,480,044.6 | 37,765.2 | 23,130.5 | 16.458 | -99.8284% | improve / improve |
| dup-param-detect | large-subject-throughput | auto-nocaps | 13,402,325.9 | 35,440.2 | 23,144.6 | 17.582 | -99.8273% | improve / improve |
| dup-param-detect | large-subject-throughput | vm-caps | 13,471,556.7 | 46,178.8 | 23,146.9 | 47.877 | -99.8282% | improve / improve |
| dup-param-detect | large-subject-throughput | vm-in-caps | 13,442,181.4 | 17,265.1 | 23,179.2 | 30.308 | -99.8276% | improve / improve |
| tag-pair-match | large-subject-throughput | auto-caps | 4,651,655.4 | 130.345 | 23,128.1 | 23.374 | -99.5028% | improve / improve |
| tag-pair-match | large-subject-throughput | auto-nocaps | 4,638,824.0 | 3,781.1 | 23,159.6 | 9.003 | -99.5007% | improve / improve |
| tag-pair-match | large-subject-throughput | vm-caps | 4,647,427.0 | 22,213.0 | 23,116.5 | 29.330 | -99.5026% | improve / improve |
| tag-pair-match | large-subject-throughput | vm-in-caps | 4,651,273.7 | 600.364 | 23,144.1 | 19.676 | -99.5024% | improve / improve |
| wild-secrets-username-password-pair | large-subject-throughput | auto-caps | 1,284,785.7 | 4,936.1 | 23,101.6 | 12.935 | -98.2019% | improve / improve |
| wild-secrets-username-password-pair | large-subject-throughput | auto-nocaps | 1,281,220.0 | 2,844.3 | 23,143.6 | 28.495 | -98.1936% | improve / improve |
| wild-secrets-username-password-pair | large-subject-throughput | vm-caps | 5,880,549.9 | 14,896.5 | 23,162.8 | 41.514 | -99.6061% | improve / improve |
| wild-secrets-username-password-pair | large-subject-throughput | vm-in-caps | 5,879,102.3 | 856.222 | 23,184.0 | 18.697 | -99.6057% | improve / improve |
| wild-logparse-winpath-grok | large-subject-throughput | auto-caps | 3,473,038.3 | 5,961.9 | 23,160.4 | 28.315 | -99.3331% | improve / improve |
| wild-logparse-winpath-grok | large-subject-throughput | auto-nocaps | 3,475,924.2 | 22,264.1 | 23,127.1 | 32.498 | -99.3346% | improve / improve |
| wild-logparse-winpath-grok | large-subject-throughput | vm-caps | 19,585,971.2 | 73,769.8 | 23,145.9 | 16.455 | -99.8818% | improve / improve |
| wild-logparse-winpath-grok | large-subject-throughput | vm-in-caps | 20,147,936.1 | 225,396.7 | 23,177.0 | 446.324 | -99.8850% | improve / improve |
| bracket-array-define | large-subject-throughput | auto-caps | 4,881,399.6 | 5,290.2 | 73.684 | 0.055 | -99.9985% | improve / improve |
| bracket-array-define | large-subject-throughput | auto-nocaps | 4,877,809.1 | 1,922.8 | 72.959 | 1.129 | -99.9985% | improve / improve |
| bracket-array-define | large-subject-throughput | vm-caps | 4,879,347.9 | 543.722 | 72.369 | 0.058 | -99.9985% | improve / improve |
| bracket-array-define | large-subject-throughput | vm-in-caps | 4,879,964.2 | 1,841.2 | 89.535 | 0.968 | -99.9982% | improve / improve |
| bracket-array-define | short-subject-search | auto-caps | 6,832.2 | 51.606 | 1,884.9 | 2.055 | -72.4111% | improve / improve |
| bracket-array-define | short-subject-search | auto-nocaps | 6,880.6 | 7.155 | 1,898.2 | 7.830 | -72.4123% | improve / improve |
| bracket-array-define | short-subject-search | vm-caps | 6,825.8 | 12.789 | 1,885.4 | 1.346 | -72.3780% | improve / improve |
| bracket-array-define | short-subject-search | vm-in-caps | 7,083.0 | 20.153 | 2,062.8 | 16.161 | -70.8772% | improve / improve |
| evil-alt-nested | large-subject-throughput | auto-caps | 4,282,437.3 | 12,442.5 | 12,126.9 | 309.855 | -99.7168% | improve / improve |
| evil-alt-nested | large-subject-throughput | auto-nocaps | 26.944 | 0.690 | 24.423 | 0.596 | -9.3550% | improve / improve |
| evil-alt-nested | large-subject-throughput | vm-caps | 4,282,218.8 | 8,750.7 | 11,981.8 | 155.438 | -99.7202% | improve / improve |
| evil-alt-nested | large-subject-throughput | vm-in-caps | 4,280,622.2 | 3,710.5 | 12,009.9 | 14.686 | -99.7194% | improve / improve |
| trim-nested-star (target scoped to auto-caps only) | large-subject-throughput | auto-caps | 3,258,460.6 | 11,513.1 | 47.053 | 0.121 | -99.9986% | improve / improve |
| wild-semdiv-dollar-trailing-newline-pcre2 | large-subject-throughput | auto-caps | 109,563.9 | 266.394 | 34.035 | 0.464 | -99.9689% | improve / improve |
| wild-semdiv-dollar-trailing-newline-pcre2 | large-subject-throughput | auto-nocaps | 109,709.6 | 174.305 | 34.785 | 0.424 | -99.9683% | improve / improve |
| wild-semdiv-dollar-trailing-newline-pcre2 | large-subject-throughput | vm-caps | 1,671,960.2 | 5,504.8 | 31.940 | 1.598 | -99.9981% | improve / improve |
| wild-semdiv-dollar-trailing-newline-pcre2 | large-subject-throughput | vm-in-caps | 1,671,839.2 | 1,003.3 | 35.402 | 0.525 | -99.9979% | improve / improve |
| router-prefix-order (reclassified control→target, I-87(b)) | large-subject-throughput | auto-caps | 393,757.0 | 431.416 | 398,422.8 | 174.809 | +1.1850% | **regress / regress** |
| router-prefix-order | large-subject-throughput | auto-nocaps | 393,998.2 | 1,399.2 | 398,752.2 | 395.217 | +1.2066% | **regress / regress** |
| router-prefix-order | large-subject-throughput | vm-caps | 4,068,366.3 | 9,073.1 | 4,050,506.2 | 3,154.7 | -0.4390% | improve / improve |
| router-prefix-order | large-subject-throughput | vm-in-caps | 4,067,713.3 | 5,675.4 | 4,049,652.5 | 2,640.9 | -0.4440% | improve / improve |

**39 of 41 target rows MEET the bar under both IQR readings** (huge
margins throughout — every met row's `|Δ%|` is at minimum 9.36%, most
are 70-100%). **2 of 41 MISS**: `router-prefix-order` /
`large-subject-throughput` on the DFA route (`auto-caps`,
`auto-nocaps`) regresses +1.19%/+1.21%, exceeding its (tight) before-IQR
of 431/1,399 ns by roughly 10× — a small absolute cost (≈4.7 μs on a
~394-399 ms baseline) but a real, IQR-exceeding regression on the
target's OWN route family under the OWN regime I-87 named, on the same
pattern whose forced-VM route and search regime both improve.

### 1.2 CARVE-OUT CELLS ("read with eyes open... sound, expected within noise" — I-87(b))

| pattern | regime | testee | before median (ns) | before IQR (ns) | after median (ns) | after IQR (ns) | Δ% | verdict (before-IQR / after-IQR) |
|---|---|---|---|---|---|---|---|---|
| floor-byte | large-subject-throughput | auto-caps | 23,142.7 | 17.860 | 23,113.3 | 37.099 | -0.1271% | improve / within-bar |
| floor-byte | large-subject-throughput | auto-nocaps | 23,126.4 | 12.301 | 23,155.0 | 2.657 | +0.1233% | regress / regress |
| floor-byte | large-subject-throughput | vm-caps | 814,079.5 | 325.096 | 23,088.0 | 41.450 | -97.1639% | improve / improve |
| floor-byte | large-subject-throughput | vm-in-caps | 814,259.1 | 3,972.4 | 23,134.8 | 47.604 | -97.1588% | improve / improve |
| floor-byte | short-subject-search | auto-caps | 667.783 | 1.602 | 599.000 | 0.579 | -10.3003% | improve / improve |
| floor-byte | short-subject-search | auto-nocaps | 666.237 | 3.468 | 600.043 | 0.017 | -9.9355% | improve / improve |
| floor-byte | short-subject-search | vm-caps | 1,355.4 | 0.807 | 664.143 | 4.134 | -50.9988% | improve / improve |
| floor-byte | short-subject-search | vm-in-caps | 1,298.7 | 3.003 | 656.403 | 0.724 | -49.4571% | improve / improve |
| nested-comment-rec | large-subject-throughput | auto-caps | 7,798,115.1 | 1,926.8 | 9,327,080.3 | 597,173.7 | **+19.6069%** | **regress / regress** |
| nested-comment-rec | large-subject-throughput | auto-nocaps | 7,808,166.4 | 2,933.2 | 9,275,952.3 | 366,365.7 | **+18.7981%** | **regress / regress** |
| nested-comment-rec | large-subject-throughput | vm-caps | 7,799,381.6 | 13,009.5 | 9,350,863.1 | 116,823.1 | **+19.8924%** | **regress / regress** |
| nested-comment-rec | large-subject-throughput | vm-in-caps | 7,799,560.3 | 35,812.3 | 9,746,259.5 | 31,549.4 | **+24.9591%** | **regress / regress** |
| nested-comment-rec | short-subject-search | auto-caps | 9,289.8 | 13.143 | 2,664.7 | 67.981 | -71.3162% | improve / improve |
| nested-comment-rec | short-subject-search | auto-nocaps | 9,295.3 | 8.577 | 2,658.8 | 17.607 | -71.3964% | improve / improve |
| nested-comment-rec | short-subject-search | vm-caps | 9,282.1 | 27.900 | 2,704.0 | 79.979 | -70.8689% | improve / improve |
| nested-comment-rec | short-subject-search | vm-in-caps | 9,066.4 | 6.897 | 2,228.8 | 10.686 | -75.4170% | improve / improve |
| uuid-near-miss | large-subject-throughput | auto-caps | 19.930 | 0.075 | 27.576 | 0.020 | **+38.3651%** | **regress / regress** |
| uuid-near-miss | large-subject-throughput | auto-nocaps | 19.914 | 0.014 | 27.589 | 0.021 | **+38.5418%** | **regress / regress** |
| uuid-near-miss | large-subject-throughput | vm-caps | 2,444,993.8 | 220,102.7 | 33.759 | 0.041 | -99.9986% | improve / improve |
| uuid-near-miss | large-subject-throughput | vm-in-caps | 2,766,890.8 | 404,686.7 | 40.531 | 0.093 | -99.9985% | improve / improve |
| uuid-near-miss | short-subject-search | auto-caps | 561.962 | 0.302 | 667.283 | 0.666 | **+18.7416%** | **regress / regress** |
| uuid-near-miss | short-subject-search | auto-nocaps | 565.548 | 0.716 | 671.572 | 4.582 | **+18.7472%** | **regress / regress** |
| uuid-near-miss | short-subject-search | vm-caps | 4,452.8 | 552.839 | 769.157 | 1.808 | -82.7263% | improve / improve |
| uuid-near-miss | short-subject-search | vm-in-caps | 4,757.9 | 160.167 | 900.671 | 2.859 | -81.0700% | improve / improve |
| ipv4-near-miss | large-subject-throughput | auto-caps | 18.791 | 0.052 | 24.961 | 0.112 | **+32.8377%** | **regress / regress** |
| ipv4-near-miss | large-subject-throughput | auto-nocaps | 18.737 | 0.085 | 24.888 | 0.038 | **+32.8285%** | **regress / regress** |
| ipv4-near-miss | large-subject-throughput | vm-caps | 4,067,060.2 | 2,256.3 | 28.457 | 0.024 | -99.9993% | improve / improve |
| ipv4-near-miss | large-subject-throughput | vm-in-caps | 4,065,788.8 | 750.615 | 34.505 | 1.098 | -99.9992% | improve / improve |
| ipv4-near-miss | short-subject-search | auto-caps | 492.116 | 1.891 | 626.883 | 0.179 | **+27.3851%** | **regress / regress** |
| ipv4-near-miss | short-subject-search | auto-nocaps | 497.033 | 2.613 | 627.037 | 0.357 | **+26.1561%** | **regress / regress** |
| ipv4-near-miss | short-subject-search | vm-caps | 6,407.7 | 12.679 | 985.863 | 4.560 | -84.6145% | improve / improve |
| ipv4-near-miss | short-subject-search | vm-in-caps | 6,392.7 | 35.827 | 1,021.4 | 1.334 | -84.0220% | improve / improve |

**Carve-outs are not bar-gated (I-87(b) frames them as predicted-benign,
not as targets), but read against that framing: 19 of 32 carve-out rows
are flat/improving (mostly the forced-VM route, which collapses like the
targets), and 13 of 32 read OUTSIDE "expected within noise"** — one
negligible (`floor-byte`/`auto-nocaps`/thr, +0.12%, ~28.5 ns on a
23,126 ns baseline — plausibly the noise I-87 predicted) and **twelve
that are not**: `nested-comment-rec`'s throughput regime on ALL FOUR
testees (+18.8% to +25.0%, while its OWN search regime improves 71-75%
on the same four testees — a split outcome, not a flat one), and
`uuid-near-miss`/`ipv4-near-miss` on the DFA route (`auto-caps`,
`auto-nocaps`) at BOTH regimes (+18.7% to +38.5%) while the SAME two
patterns improve 81-100% on the forced-VM route. See §5 findings 4-5.

---

## 2. CELLS OUTSIDE THE BAR EITHER WAY (non-named patterns)

Population: 384 (pattern, regime, testee) cells present on both pins
outside the 14 named target/carve-out patterns (of 504 total rows
across 126 pattern-regime-form combos × 4 testees; 12 rows are MISSING
on one or both sides — §2.3). Under the before-IQR reading: 202 improve
beyond bar, 104 within-bar, 78 regress beyond bar. Under the after-IQR
reading: 211 improve, 86 within-bar, 87 regress. 189 of 384 improve
under BOTH readings; 69 of 384 regress under BOTH readings — the 63
before/after-IQR verdict flips (listed by row, over the WHOLE 492-row
present population, in the extraction script's output; none is among
the named target/carve-out set beyond the one already noted in §1) are
concentrated at small (<1.5%) Δ% on cells whose IQR is comparable in
size to the movement itself.

### 2.1 Non-named REGRESSIONS with before-median ≥ 100 ns (64 cells, before-IQR reading)

| pattern | regime | testee | before med (ns) | after med (ns) | Δ% | before IQR | after IQR | verdict (b/a) |
|---|---|---|---|---|---|---|---|---|
| logparse-atomic-removed | short-subject-search | auto-nocaps | 492.620 | 660.420 | +34.06% | 0.487 | 0.857 | regress/regress |
| wild-codegrammar-json-array-begin | large-subject-throughput | auto-nocaps | 263,616.4 | 349,566.6 | +32.60% | 589.413 | 116.626 | regress/regress |
| wild-codegrammar-json-array-begin | large-subject-throughput | auto-caps | 263,784.5 | 349,512.7 | +32.50% | 202.558 | 80.969 | regress/regress |
| wild-validator-ipv4-owasp | short-subject-search | auto-nocaps | 498.641 | 626.471 | +25.64% | 0.262 | 1.079 | regress/regress |
| wild-secrets-github-pat | large-subject-throughput | vm-in-caps | 4,776,127.5 | 5,857,018.1 | +22.63% | 13,824.7 | 6,899.4 | regress/regress |
| float-literal-bound | large-subject-throughput | vm-caps | 18,893,460.4 | 22,138,490.7 | +17.18% | 28,300.9 | 158,352.6 | regress/regress |
| winpath-near-miss | short-subject-search | auto-caps | 499.934 | 585.254 | +17.07% | 0.995 | 0.716 | regress/regress |
| winpath-near-miss | short-subject-search | auto-nocaps | 499.765 | 584.722 | +17.00% | 1.254 | 1.782 | regress/regress |
| float-literal-bound | large-subject-throughput | vm-in-caps | 19,041,147.9 | 22,079,935.4 | +15.96% | 53,319.6 | 147,023.2 | regress/regress |
| wild-codegrammar-json-array-begin | large-subject-throughput | vm-in-caps | 957,768.1 | 1,105,767.8 | +15.45% | 3,246.4 | 1,556.1 | regress/regress |
| wild-codegrammar-json-array-begin | large-subject-throughput | vm-caps | 955,686.2 | 1,093,165.0 | +14.39% | 1,526.2 | 3,634.6 | regress/regress |
| file-ext-order | large-subject-throughput | vm-caps | 3,854,116.9 | 4,270,753.1 | +10.81% | 17,415.5 | 7,277.0 | regress/regress |
| file-ext-order | large-subject-throughput | vm-in-caps | 3,856,267.9 | 4,267,973.9 | +10.68% | 1,356.0 | 2,646.6 | regress/regress |
| wild-validator-uuid-grok | short-subject-search | auto-nocaps | 716.448 | 788.628 | +10.07% | 1.697 | 12.783 | regress/regress |
| phone-palindrome-6 | large-subject-throughput | auto-caps | 6,585,253.9 | 7,142,399.5 | +8.46% | 15,787.5 | 175,376.3 | regress/regress |
| float-literal-bound | large-subject-throughput | auto-caps | 1,791,555.1 | 1,939,786.6 | +8.27% | 4,160.2 | 8,031.1 | regress/regress |
| float-literal-bound | large-subject-throughput | auto-nocaps | 1,790,225.4 | 1,932,614.8 | +7.95% | 7,088.4 | 3,511.8 | regress/regress |
| wild-validator-uuid-grok | short-subject-search | auto-caps | 723.309 | 780.614 | +7.92% | 6.749 | 4.856 | regress/regress |
| wild-waf-crs-942160-sleep-benchmark | large-subject-throughput | auto-nocaps | 1,266,849.9 | 1,360,803.0 | +7.42% | 1,990.6 | 10,198.1 | regress/regress |
| wild-datetime-moment-iso8601 | short-subject-search | auto-nocaps | 589.054 | 631.497 | +7.21% | 1.150 | 0.368 | regress/regress |
| wild-waf-crs-942160-sleep-benchmark | large-subject-throughput | auto-caps | 1,268,060.9 | 1,358,357.1 | +7.12% | 4,976.1 | 4,601.2 | regress/regress |
| logparse-atomic-removed | short-subject-search | auto-caps | 809.509 | 858.585 | +6.06% | 1.548 | 3.254 | regress/regress |
| keyword-prefix-order | large-subject-throughput | auto-nocaps | 731,389.9 | 775,044.9 | +5.97% | 1,883.8 | 1,599.1 | regress/regress |
| keyword-prefix-order | large-subject-throughput | auto-caps | 731,121.5 | 774,694.7 | +5.96% | 851.031 | 805.678 | regress/regress |
| date-nested-plus | short-subject-search | auto-nocaps | 489.137 | 512.006 | +4.68% | 2.197 | 0.473 | regress/regress |
| keyword-prefix-order | short-subject-search | auto-caps | 774.516 | 802.304 | +3.59% | 2.443 | 1.557 | regress/regress |
| wild-secrets-slack-webhook-url | short-subject-search | auto-nocaps | 928.048 | 959.821 | +3.42% | 0.477 | 0.803 | regress/regress |
| keyword-prefix-order | short-subject-search | auto-nocaps | 774.371 | 800.610 | +3.39% | 13.018 | 1.481 | regress/regress |
| wild-secrets-github-pat | large-subject-throughput | vm-caps | 5,228,975.3 | 5,387,513.3 | +3.03% | 18,080.7 | 12,000.5 | regress/regress |
| logparse-atomic | short-subject-search | auto-caps | 852.179 | 876.424 | +2.85% | 14.730 | 0.857 | regress/regress |
| logparse-atomic | short-subject-search | auto-nocaps | 838.730 | 859.859 | +2.52% | 3.137 | 2.028 | regress/regress |
| date-nested-plus | short-subject-search | auto-caps | 868.879 | 890.540 | +2.49% | 0.979 | 5.734 | regress/regress |
| keyword-prefix-order | large-subject-throughput | vm-caps | 4,181,697.9 | 4,283,134.0 | +2.43% | 2,714.0 | 132.667 | regress/regress |
| keyword-prefix-order | large-subject-throughput | vm-in-caps | 4,193,358.5 | 4,286,675.4 | +2.23% | 4,277.6 | 1,397.3 | regress/regress |
| wild-secrets-slack-webhook-url | large-subject-throughput | vm-in-caps | 4,776,737.9 | 4,870,501.0 | +1.96% | 14,522.8 | 16,936.1 | regress/regress |
| wild-secrets-slack-webhook-url | large-subject-throughput | vm-caps | 4,775,991.7 | 4,867,333.9 | +1.91% | 2,212.6 | 4,941.2 | regress/regress |
| phone-list-nested-plus | short-subject-search | auto-caps | 894.719 | 909.256 | +1.62% | 1.176 | 4.339 | regress/regress |
| codegrammar-xflag | large-subject-throughput | vm-caps | 2,010,864.6 | 2,042,645.3 | +1.58% | 4,686.6 | 11,700.1 | regress/regress |
| wild-codegrammar-json-constant | short-subject-search | vm-in-caps | 3,349.3 | 3,391.3 | +1.26% | 24.012 | 13.984 | regress/regress |
| numeric-id-nested-plus | short-subject-search | vm-caps | 9,235,076.7 | 9,348,039.8 | +1.22% | 5,584.9 | 17,903.5 | regress/regress |
| codegrammar-flat | large-subject-throughput | vm-caps | 2,021,147.5 | 2,044,975.0 | +1.18% | 16,832.1 | 5,459.6 | regress/regress |
| codegrammar-flat | large-subject-throughput | auto-caps | 608,738.6 | 615,877.6 | +1.17% | 3,301.0 | 15,337.0 | regress/within-bar |
| wild-semdiv-altorder-foo-foobar-rustregex | large-subject-throughput | auto-nocaps | 408,869.9 | 413,226.8 | +1.07% | 756.002 | 244.904 | regress/regress |
| numeric-id-nested-plus | short-subject-search | vm-in-caps | 9,239,556.0 | 9,336,678.2 | +1.05% | 4,052.4 | 18,306.1 | regress/regress |
| phone-list-nested-plus | short-subject-search | vm-in-caps | 9,972,479.2 | 10,075,899.5 | +1.04% | 6,973.0 | 15,698.7 | regress/regress |
| wild-semdiv-empty-alt-repeat-pcre2 | large-subject-throughput | auto-nocaps | 3,815,862.7 | 3,851,419.8 | +0.93% | 26,168.2 | 6,314.4 | regress/regress |
| wild-waf-crs-942360-concat-sqli | short-subject-search | vm-caps | 48,545.1 | 48,979.4 | +0.89% | 109.011 | 67.966 | regress/regress |
| phone-list-nested-plus | short-subject-search | vm-caps | 9,990,745.8 | 10,066,942.3 | +0.76% | 21,013.4 | 2,134.0 | regress/regress |
| wild-semdiv-altorder-foo-foobar-rustregex | large-subject-throughput | auto-caps | 410,146.0 | 413,068.6 | +0.71% | 2,311.6 | 454.170 | regress/regress |
| wild-logparse-quotedstring-noatomic | large-subject-throughput | vm-in-caps | 23,029,113.2 | 23,180,108.5 | +0.66% | 94,723.0 | 200,437.8 | regress/within-bar |
| wild-waf-crs-942140-dbnames | short-subject-search | vm-caps | 16,350.5 | 16,454.0 | +0.63% | 8.768 | 287.978 | regress/within-bar |
| quoted-delim-match | large-subject-throughput | auto-caps | 10,078,110.5 | 10,132,095.1 | +0.54% | 19,674.7 | 101,620.8 | regress/within-bar |
| wild-semdiv-empty-alt-repeat-pcre2 | short-subject-search | vm-in-caps | 101,862.0 | 102,391.6 | +0.52% | 180.567 | 58.936 | regress/regress |
| wild-waf-crs-942270-union-select | short-subject-search | vm-in-caps | 5,298.1 | 5,315.3 | +0.32% | 6.459 | 7.887 | regress/regress |
| wild-logparse-base10num-grok | large-subject-throughput | auto-caps | 4,033,368.0 | 4,044,116.8 | +0.27% | 10,264.6 | 2,633.2 | regress/regress |
| wild-logparse-quotedstring-grok | short-subject-search | vm-in-caps | 49,149.4 | 49,278.6 | +0.26% | 31.168 | 38.125 | regress/regress |
| wild-waf-crs-942500-comment-obfuscation | large-subject-throughput | auto-caps | 23,099.9 | 23,153.2 | +0.23% | 42.750 | 9.956 | regress/regress |
| wild-secrets-slack-webhook-url | large-subject-throughput | auto-caps | 341,069.2 | 341,850.0 | +0.23% | 290.134 | 612.566 | regress/regress |
| wild-codegrammar-json-object-begin | large-subject-throughput | auto-nocaps | 23,134.0 | 23,184.9 | +0.22% | 26.893 | 43.033 | regress/regress |
| wild-logparse-quotedstring-noatomic | short-subject-search | vm-caps | 114,108.8 | 114,302.9 | +0.17% | 149.282 | 207.790 | regress/within-bar |
| file-ext-order | large-subject-throughput | auto-nocaps | 292,413.5 | 292,762.7 | +0.12% | 253.330 | 618.868 | regress/within-bar |
| wild-waf-crs-942360-concat-sqli | short-subject-search | auto-nocaps | 7,404.7 | 7,412.0 | +0.10% | 4.212 | 59.192 | regress/within-bar |
| wild-logparse-base10num-noatomic | large-subject-throughput | auto-nocaps | 3,986,220.4 | 3,990,114.4 | +0.10% | 3,276.9 | 6,875.2 | regress/within-bar |
| wild-codegrammar-json-constant | large-subject-throughput | auto-caps | 4,197,409.4 | 4,199,268.9 | +0.04% | 1,806.3 | 3,410.3 | regress/within-bar |

### 2.2 Non-named REGRESSIONS with before-median < 100 ns — the floor-conversion cells (14 cells)

These are cells that were already near-instant rejects before the pin
(15-48 ns), formally "regress" by the IQR bar because their trial-to-
trial spread is a few tens of picoseconds, but land at either a genuine
new ~23,100-23,180 ns floor (the first two rows — see §5 finding 2) or
a still-tiny few-tens-of-ns value (the rest):

| pattern | regime | testee | before med (ns) | after med (ns) | verdict (b/a) |
|---|---|---|---|---|---|
| winpath-near-miss | large-subject-throughput | auto-caps | 20.088 | 23,123.6 | regress/regress |
| winpath-near-miss | large-subject-throughput | auto-nocaps | 20.382 | 23,119.7 | regress/regress |
| email-nested-plus | large-subject-throughput | auto-nocaps | 31.981 | 23,138.8 | regress/regress |
| email-nested-plus | large-subject-throughput | auto-caps | 47.279 | 23,106.9 | regress/regress |
| wild-datetime-moment-iso8601 | large-subject-throughput | auto-nocaps | 19.684 | 36.907 | regress/regress |
| logparse-atomic-removed | large-subject-throughput | auto-nocaps | 18.774 | 30.007 | regress/regress |
| wild-datetime-moment-iso8601 | large-subject-throughput | auto-caps | 32.909 | 48.674 | regress/regress |
| logparse-atomic | large-subject-throughput | auto-caps | 30.016 | 41.518 | regress/regress |
| wild-validator-ipv4-owasp | large-subject-throughput | auto-nocaps | 18.700 | 24.949 | regress/regress |
| logparse-atomic-removed | large-subject-throughput | auto-caps | 30.324 | 40.450 | regress/regress |
| logparse-atomic | large-subject-throughput | auto-nocaps | 32.307 | 40.344 | regress/regress |
| wild-validator-email-owasp | large-subject-throughput | auto-nocaps | 38.954 | 43.740 | regress/regress |
| wild-validator-email-owasp | large-subject-throughput | auto-caps | 40.444 | 43.870 | regress/regress |
| date-nested-plus | large-subject-throughput | auto-caps | 30.617 | 30.948 | regress/regress |

**All 14 are on the DFA-route testees (`auto-caps`/`auto-nocaps`) only**
— no `vm-caps`/`vm-in-caps` cell appears in this list (the forced-VM
route's already-slow baselines on these same patterns move the OTHER
way — see §2.3/§5).

### 2.3 Improvements beyond bar (non-named, aggregate)

202 of 384 non-named cells improve beyond their before-IQR (211 by
after-IQR). Two populations, both dominated by the forced-VM route:

- **30 `large-subject-throughput` cells on `vm-caps`/`vm-in-caps`
  collapse from before-medians of 2.0-48.4 MILLION ns to after-medians
  under 100 ns** (e.g. `wild-validator-ipv4-owasp` 4,269,920.7 → 28.9 ns
  on `vm-caps`; `email-local-nodup` 3,863,999.1 → 916.4 ns; the full
  list is the same shape as §1's named targets, just unnamed). 86 more
  `vm-caps`/`vm-in-caps` large-subject-throughput cells with
  before-medians over 1,000,000 ns do **not** collapse (stay in the
  0.005-45% Δ band either way — `high-byte-run`, `wild-secrets-aws-
  access-key-id`, `utf8-lead-no-cont`, `currency-lookbehind-fixed`, and
  30 others are flat to within a few percent; a handful are the §2.1
  regressions above).
- **14 `large-subject-throughput` cells on `auto-caps`/`auto-nocaps`
  with before-medians over 1,000,000 ns collapse to under 30,000 ns**
  (the DFA-route mirror of the same population); 38 more stay flat or
  move by single-digit percent either way (§2.1's regressing rows are
  drawn from this same population).
- The remaining improving cells are `short-subject-search` rows moving
  by tens of percent (e.g. `phone-palindrome-6` −1.7% to −5.6% across
  all four testees — the largest of the before/after-IQR flips in §1's
  header note lives here) — no `short-subject-search` cell collapses to
  a near-zero floor the way `large-subject-throughput` cells do.

### 2.4 MISSING cells (12 rows, both sides or one side)

| pattern | regime | testee | before | after |
|---|---|---|---|---|
| email-nested-plus | short-subject-search | vm-caps | expectation-failing | present |
| email-nested-plus | short-subject-search | vm-in-caps | expectation-failing | present |
| wild-datetime-datefinder-alternation | short-subject-search | auto-caps | did-not-compile | did-not-compile |
| wild-datetime-datefinder-alternation | short-subject-search | vm-caps | did-not-compile | did-not-compile |
| wild-datetime-datefinder-alternation | short-subject-search | vm-in-caps | did-not-compile | did-not-compile |
| wild-datetime-datefinder-alternation | large-subject-throughput | auto-caps | did-not-compile | did-not-compile |
| wild-datetime-datefinder-alternation | large-subject-throughput | vm-caps | did-not-compile | did-not-compile |
| wild-datetime-datefinder-alternation | large-subject-throughput | vm-in-caps | did-not-compile | did-not-compile |
| evil-alt-nested | short-subject-search | auto-caps | expectation-failing | expectation-failing |
| evil-alt-nested | short-subject-search | auto-nocaps | expectation-failing | expectation-failing |
| evil-alt-nested | short-subject-search | vm-caps | expectation-failing | expectation-failing |
| evil-alt-nested | short-subject-search | vm-in-caps | expectation-failing | expectation-failing |

`wild-datetime-datefinder-alternation` refuses on both `-caps` VM-route
configs and `auto-caps` on BOTH pins, unchanged (the compile-time code
cap, per its own `note` line — §0.3); `email-nested-plus`/`short-
subject-search` on the two `-caps` VM testees is expectation-failing
BEFORE only — not interpolated, not counted in §1 or §2's tables, no
Δ computed. No new refusal appears on the AFTER side that was not
already present on the BEFORE side.

---

## 3. THE STAMP CENSUS

`req_byte` / `end_window` (`RX_REQ_BYTE` / `RX_END_WINDOW`) are
PATTERN-level: identical across all four AFTER testees whenever the
pattern compiles on both routes (checked; no divergence found).
`vm_start` (`RX_VM_START`) is engine-scoped: present on every compiled
VM artifact, absent on every DFA artifact — confirmed on all 623-624
compile rows per record, both directions of the iff. Counts across the
four AFTER records (compiled rows only, `plain` form; 64 unique
patterns, 127 pattern×form compile rows, one pattern
`negation-scope-lookbehind-var` is `unsupported-by-declaration` on
every testee and carries no stamps):

| stamp | present (non-`none`) | absent |
|---|---|---|
| `req_byte` | 72 / 127 rows, identically on all 4 testees | 55 / 127 |
| `end_window` | 25 / 127 rows, identically on all 4 testees | 102 / 127 |
| `vm_start` | 124/127 (`vm-caps`), 124/127 (`vm-in-caps`), 76/127 (`auto-caps`), 42/127 (`auto-nocaps`) | the complement, all DFA-route |

BEFORE (25b1984f, abi 27) compile rows carry **none of the three keys
at all** — confirmed by direct key listing on two BEFORE compile rows;
the cross-pin comparison in §1/§2 is therefore unconfounded by any
change to an EXISTING field.

### 3.1 Named-expectation cross-check (I-87(c))

| pattern | expectation (I-87) | measured (AFTER, all 4 testees identical req_byte/end_window) | match? |
|---|---|---|---|
| router-prefix-order | `RX_REQ_BYTE "114"` | `req_byte="114"`, `end_window="none"` | **MATCH, exact** |
| floor-byte | gains a required-byte memchr | `req_byte="126"` (was absent BEFORE) | **MATCH** |
| nested-comment-rec | gains a required-byte memchr | `req_byte="47"` (was absent BEFORE) | **MATCH** |
| uuid-near-miss | gains an end window (37 bytes) | `end_window="37"`, `req_byte="45"` | **MATCH, exact byte count** |
| ipv4-near-miss | gains an end window (16 bytes) | `end_window="16"`, `req_byte="46"` | **MATCH, exact byte count** |

All five named expectations confirmed by value, on every one of the
four AFTER records.

### 3.2 Full per-pattern census (AFTER, 8d716693, `plain` form)

`route(auto-X)` reads the ENGINE `auto-X` actually selected (`dfa` or
`vm`); `vm_start` is read off the forced-VM (`vm-caps`) artifact, which
compiles every pattern to VM by construction.

| pattern | req_byte | end_window | route(auto-caps) | route(auto-nocaps) | vm_start (forced VM) |
|---|---|---|---|---|---|
| balanced-parens-rec | 41 | none | vm | vm | unanchored |
| base10num-near-miss | none | none | dfa | dfa | anchored |
| bracket-array-define | none | none | vm | vm | anchored |
| codegrammar-flat | 58 | none | vm | dfa | unanchored |
| codegrammar-xflag | 58 | none | vm | dfa | unanchored |
| currency-lookbehind-fixed | none | none | vm | vm | unanchored |
| date-nested-plus | none | none | vm | dfa | anchored |
| doubled-word | none | none | vm | vm | unanchored |
| dup-param-detect | 61 | none | vm | vm | unanchored |
| email-local-nodup | none | none | vm | vm | anchored |
| email-nested-plus | 64 | none | vm | dfa | anchored |
| evil-alt-nested | none | none | vm | dfa | anchored |
| file-ext-order | 114 | none | dfa | dfa | unanchored |
| float-literal-bound | 46 | none | vm | vm | unanchored |
| floor-byte | 126 | none | dfa | dfa | unanchored |
| high-byte-run | none | none | dfa | dfa | unanchored |
| ipv4-near-miss | 46 | 16 | dfa | dfa | anchored |
| keyword-prefix-order | 110 | none | dfa | dfa | unanchored |
| logparse-atomic | 32 | none | vm | vm | anchored |
| logparse-atomic-removed | 32 | none | vm | dfa | anchored |
| mojibake-curly-quote | 148 | none | dfa | dfa | unanchored |
| negation-scope-lookbehind-var | -- | -- | unsupported-by-declaration | unsupported-by-declaration | -- |
| nested-comment-rec | 47 | none | vm | vm | unanchored |
| numeric-id-nested-plus | none | none | vm | dfa | anchored |
| phone-list-nested-plus | none | none | vm | dfa | anchored |
| phone-palindrome-6 | none | none | vm | vm | unanchored |
| pwd-strength-chain | none | none | vm | vm | anchored |
| quoted-delim-match | none | none | vm | vm | unanchored |
| router-prefix-order | 114 | none | dfa | dfa | unanchored |
| tag-depth3-bound | 62 | none | vm | vm | unanchored |
| tag-pair-match | 62 | none | vm | vm | unanchored |
| trim-nested-star | none | none | vm | dfa | anchored |
| utf8-lead-no-cont | none | none | vm | vm | unanchored |
| uuid-near-miss | 45 | 37 | dfa | dfa | anchored |
| wild-codegrammar-json-array-begin | 91 | none | dfa | dfa | unanchored |
| wild-codegrammar-json-constant | none | none | dfa | dfa | unanchored |
| wild-codegrammar-json-number-extended | none | none | dfa | dfa | unanchored |
| wild-codegrammar-json-object-begin | 123 | none | dfa | dfa | unanchored |
| wild-codegrammar-json-stringcontent-escape | 92 | none | dfa | dfa | unanchored |
| wild-datetime-datefinder-alternation | none | none | did-not-compile | dfa | (n/a on this route) |
| wild-datetime-moment-iso8601 | 45 | none | vm | dfa | anchored |
| wild-logparse-base10num-grok | none | none | vm | vm | unanchored |
| wild-logparse-base10num-noatomic | none | none | vm | vm | unanchored |
| wild-logparse-quotedstring-grok | none | none | vm | vm | unanchored |
| wild-logparse-quotedstring-noatomic | none | none | vm | vm | unanchored |
| wild-logparse-syslogbase-expanded | 58 | none | vm | vm | unanchored |
| wild-logparse-winpath-grok | 92 | none | vm | vm | unanchored |
| wild-secrets-aws-access-key-id | 65 | none | vm | dfa | unanchored |
| wild-secrets-github-pat | 95 | none | vm | dfa | unanchored |
| wild-secrets-slack-webhook-url | 47 | none | vm | dfa | unanchored |
| wild-secrets-username-password-pair | 61 | none | vm | dfa | unanchored |
| wild-semdiv-altorder-foo-foobar-rustregex | 111 | none | dfa | dfa | unanchored |
| wild-semdiv-dollar-trailing-newline-pcre2 | 99 | 4 | dfa | dfa | unanchored |
| wild-semdiv-empty-alt-repeat-pcre2 | none | none | vm | dfa | unanchored |
| wild-validator-email-owasp | 46 | none | dfa | dfa | anchored |
| wild-validator-ipv4-owasp | 46 | 16 | vm | dfa | anchored |
| wild-validator-us-zip-owasp | none | 11 | vm | dfa | anchored |
| wild-validator-uuid-grok | 45 | none | dfa | dfa | unanchored |
| wild-waf-crs-942140-dbnames | none | none | dfa | dfa | unanchored |
| wild-waf-crs-942160-sleep-benchmark | 41 | none | dfa | dfa | unanchored |
| wild-waf-crs-942270-union-select | none | none | dfa | dfa | unanchored |
| wild-waf-crs-942360-concat-sqli | none | none | dfa | dfa | unanchored |
| wild-waf-crs-942500-comment-obfuscation | 47 | none | dfa | dfa | unanchored |
| winpath-near-miss | 92 | none | dfa | dfa | anchored |

Note: `wild-semdiv-dollar-trailing-newline-pcre2` (M4's named target)
is the only pattern in the census carrying BOTH a `req_byte` (99) and a
non-`none` `end_window` (4) — consistent with I-87's mechanism label
`[OPT-ENDWIN]`/`\z` for M4 while M1's five named targets carry
`req_byte` only, and M2's named targets (`bracket-array-define`,
`evil-alt-nested`, `trim-nested-star`) carry NEITHER stamp (`none`/
`none`) and move only via `vm_start` (all three are `anchored` on the
forced-VM route) — the census is internally consistent with I-87's own
mechanism-to-target mapping.

`nested-comment-rec` and `email-nested-plus` are the two patterns in
the census where `auto-caps` and `auto-nocaps` pick DIFFERENT routes
from each other for the SAME pattern class shape as their neighbors —
`nested-comment-rec` picks `vm` on BOTH auto configs (unlike most
req_byte-bearing DFA-eligible patterns, which stay `dfa` under `auto`),
and `email-nested-plus` picks `vm` under `auto-caps` but `dfa` under
`auto-nocaps` — stated as fact, not diagnosed.

---

## 4. RANKED FINDINGS (facts only)

1. **The named ReDoS/pathological throughput targets collapse
   ~98.2-99.9% on ALL FOUR pcrec configs**, not only on the mechanism's
   nominal route — `tag-depth3-bound`, `dup-param-detect`,
   `tag-pair-match`, `wild-secrets-username-password-pair`,
   `wild-logparse-winpath-grok`, `bracket-array-define`,
   `evil-alt-nested`, `wild-semdiv-dollar-trailing-newline-pcre2` each
   drop from 1.28-20.1 MILLION ns to 23,100-89,500 ns (or, for
   `bracket-array-define`, to 72-90 ns) on `auto-caps`, `auto-nocaps`,
   `vm-caps` AND `vm-in-caps` alike (§1.1). `trim-nested-star`'s target
   scope (`auto-caps` only, per I-87(b)) also meets the bar by a wide
   margin (-99.9986%).

2. **A large fraction of `large-subject-throughput` cells — named and
   unnamed, both routes — converge on a common ~23,088-23,190 ns floor
   after the pin**, arrived at from BOTH directions: eight of the nine
   §1.1 named-target rows land in exactly this band; so do `floor-byte`
   (already there before the pin, on the DFA route) and two unnamed
   patterns that were previously near-ZERO (`winpath-near-miss` 20.1/
   20.4 ns → 23,106.9/23,123.6 ns; `email-nested-plus` 31.98/47.28 ns →
   23,106.9/23,138.8 ns, both DFA-route only — §2.2). The same two
   patterns' forced-VM route moves the opposite way (millions of ns
   down to tens of ns), so the floor is not a route property common to
   both engines uniformly — it is reached from above by the named
   targets and from below by these two DFA-route-only cells.

3. **`router-prefix-order`, the pattern I-87(b) reclassified from
   "byte-identity control" to "target" because it now stamps
   `RX_REQ_BYTE "114"`, is confirmed to carry that exact stamp value
   (§3.1) but MISSES the D119 bar on its own named regime on the DFA
   route**: `auto-caps` +1.19% and `auto-nocaps` +1.21% on
   `large-subject-throughput`, both exceeding their (tight, ~175-1,400
   ns) before-IQR by roughly an order of magnitude, while the SAME
   pattern's `vm-caps`/`vm-in-caps` throughput and ALL FOUR testees'
   `short-subject-search` regime improve (-0.44% to -49.4%) — the only
   named target with a split (2-met/2-missed) outcome (§1.1).

4. **`nested-comment-rec`, one of I-87(b)'s two carve-outs described as
   "sound, expected within noise," regresses 18.8-25.0% on its
   `large-subject-throughput` regime on ALL FOUR testees** — nowhere
   near noise — while its `short-subject-search` regime improves
   70.9-75.4% on the same four testees (§1.2). Its stamp census
   (§3.2) shows `route(auto-caps)=vm` and `route(auto-nocaps)=vm`: this
   pattern already selects the VM engine under BOTH `auto` configs, so
   its four "testees" are not four independent measurements of a
   DFA-vs-VM split — all four run the VM engine.

5. **`uuid-near-miss`/`ipv4-near-miss`, I-87(b)'s other two carve-outs
   ("gain an end window... sound, expected within noise"), regress
   18.7-38.5% on the DFA route (`auto-caps`, `auto-nocaps`) at BOTH
   regimes while improving 81.1-100% on the forced-VM route** (§1.2);
   their `end_window` stamps match I-87's predicted byte counts exactly
   (37 and 16 — §3.1), so the mechanism landed as specified, but its
   DFA-route cost on these two patterns is a real double-digit-percent
   regression, not the "within noise" framing named them for.

6. **A 64-cell population of non-named, previously-fast "everyday"
   patterns picks up real (0.04-34.1%) throughput/search regressions**,
   concentrated on the DFA route and correlated with a newly-present
   `req_byte` or `vm_start=anchored` stamp (§2.1) — e.g.
   `wild-codegrammar-json-array-begin` +14.4% to +32.6% on all four
   testees (`req_byte=91`, DFA on `auto-*`), `float-literal-bound`
   +8.0% to +17.2% on all four (`req_byte=46`, VM on `auto-*`),
   `keyword-prefix-order` +2.2% to +6.0% on all four (`req_byte=110`,
   DFA route), `file-ext-order` +10.7% to +10.8% on the forced-VM route
   only (`req_byte=114`, DFA on `auto-*`), `winpath-near-miss`'s
   `short-subject-search` regime +17.0% on `auto-caps`/`auto-nocaps`
   only (`req_byte=92`), and `date-nested-plus`/`phone-list-nested-
   plus`/`numeric-id-nested-plus`/`base10num-near-miss` regressing
   1.0-4.7% with NEITHER `req_byte` nor `end_window` set — `vm_start=
   anchored` is the only new stamp on these last four (§3.2), so their
   movement correlates with the OTHER named mechanism ([OPT-ANCHOR-VM])
   rather than the required-byte one. None of these 64 cells is an
   I-87-named target or carve-out.

7. **`trim-nested-star`'s `short-subject-search` regime — not a named
   target (only its `large-subject-throughput` regime at `auto-caps`
   was named) — regresses 13.6-13.9% on THREE of four testees**
   (`auto-caps`, `vm-caps`, `vm-in-caps`) while `auto-nocaps` is flat
   (-0.88%) — visible only because §2's sweep covers every cell, not
   only the named ones.

8. **KB-27's fix is confirmed clean on both named subjects, on both
   pins, on all four AFTER testees**: `rd-evil-alt-near-miss` and
   `sd-empty-alt-hit` under `evil-alt-nested`/`short-subject-search`
   read `gave-up` on all 5 trials everywhere checked (`n_wrong=0`,
   `n_no_expectation=0`) — a genuine engine resource limit, not a
   wrong-answer or no-expectation misclassification; this is what
   excludes the whole `evil-alt-nested`/`short-subject-search` SET cell
   on both pins (§0.3), independent of anything I-87/I-88 asked about.

9. **Measurement quality is clean on both sides of the comparison**:
   all eight records attempt-1, X13 `agree` with 0 disagreeing groups
   on every one, box quiet throughout (max other-core busy 6.06%
   BEFORE, 1.80% AFTER, both well under the 10% pre-flight limit), no
   `inconclusive-spread` re-measure on either side (§0.3) — no
   measurement-quality caveat qualifies any number in §1 or §2.
