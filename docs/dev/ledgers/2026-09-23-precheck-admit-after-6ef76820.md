# THE LEDGER — capability@0.1's [OPT-PRECHECK-ADMIT] acceptance grid at pcrec 6ef76820 (abi 31)

Read-only extraction, no diagnosis, per inbox_from_pcrec.md I-102 (the
[B84] (b) ask). Scores the AFTER window's per-cell numbers against
I-102's own acceptance/no-move/negative-control grid, against the D119
landing bar (**a TARGET cell must improve by more than its IQR; every
other cell must not regress by more than its IQR**), and against the
REQ_WHY census as the fourth independent derivation. Numbers only; the
manager's interpretation and any outbox item are not this lane's to
write.

**BEFORE** = the four `pcrec_b1885a83_*` records (2026-09-23T11:47-13:33Z
starts; abi 30) — the same records that were the AFTER of
`2026-09-23-optloop2-batch2-after-b1885a83.md`.
**AFTER** = the four `pcrec_6ef76820_*` records (2026-09-23T20:01-21:41Z
starts; abi 31; store 229, window 2026-09-23 16:00-18:22 EDT, all
attempt-1). The committed cross-pin report group
`reports/2026-09-23-capability-0.1-budu-ryzen1600-after-6ef76820.*`
(reporter v21) is a CROSS-CHECK only (§0.2); every verdict below is
computed independently from the eight records.

**Ratio/percentage convention: `(after − before) / before`, so a
positive `Δ%` is SLOWER (a regression) and a negative `Δ%` is FASTER (an
improvement), for every table in this ledger.**

---

## SUMMARY TABLE — per grid letter, met / missed / partial

| letter | population | n rows | met | missed | partial | note |
|---|---|---|---|---|---|---|
| (a) `wild-validator-email-owasp` thr | 4 testees | 4 | **4/4 MET** | 0 | — | AFTER 37.0-68.8 ns; 3/4 land BELOW the predicted 43.7-85.3 ns floor |
| (b) `winpath-near-miss`/`email-nested-plus` thr | 4 testees × 2 patterns | 8 | **8/8 MET** | 0 | — | `email-nested-plus` forced-VM recovers to only ~7,200-7,257 ns, not the predicted ~47 ns (still clears IQR) |
| (c) `wild-codegrammar-json-array-begin` thr | 4 testees | 4 | 3/4 | 1/4 | — | `vm-in-caps` REGRESSES +1.84% |
| (d) `uuid-near-miss`/`ipv4-near-miss` thr+srch, DFA route | 2 patterns × 2 regimes × 2 testees | 8 | **8/8 MET** | 0 | — | −18.3% to −51.6% |
| "the 4 G1 cells" — NAMED: `wild-codegrammar-json-array-begin` thr, all 4 testees (`cycle1_ledger_reading.md` §4.3's "duplicated pass (G1)" rows) | 4 | 3/4 | 1/4 | — | **identical population to letter (c) above** — re-scored, not re-measured; see §1.6 |
| (e) the G2 population, PRIMARY 12 cells named by `cycle1_ledger_reading.md` (§2.2/§4.2/§4.3's explicit "(G2)"/carve-out labels) | 12 | **12/12 MET** | 0 | — | all improve beyond IQR (8 of the 12 are letter (d)'s own cells) |
| (e) the G2 population, SECONDARY 72-cell superset (9 named patterns, both regimes, 4 testees; 17 of the 29 cells NOT individually locatable by name — see §1.5) | 72 | 49 | **21 regress + 2 NEW give-up** | — | **MISSED** on the superset: 21/72 regress beyond IQR; 2/72 (`email-nested-plus`/srch/forced-VM) newly give up (`PCREC_ERR_STEPS`) where BEFORE all 75 subjects passed — under pcrec's own +8.4605% null band (§9/O-48) the miss count is 17/72, still a miss |
| (f) `nested-comment-rec` thr no-move | 4 testees | 2 | 2 within-bar | — | **2/4 float above their own before-IQR at floor scale (+0.06%/+0.24%, 4-9 ns)** — trivial by any null-band reading, flagged not scored as a miss |
| (g) `wild-secrets-github-pat` thr forced-VM no-move | 2 testees | 2 | **2/2 clean** | 0 | — | −0.03%/+0.04%, both within-bar |
| (h) `router-prefix-order`/`keyword-prefix-order` thr negative control | 4 testees × 2 patterns | 8 | **8/8 consistent with "no change"** | — | — | every row ≤ ±0.18%, matching the report's own `unchanged (within spread)` reading on every row checked |

**The single most consequential finding is NOT a D119 timing miss**: on the
forced-VM route (`vm-caps`, `vm-in-caps`), `email-nested-plus` /
`short-subject-search` newly gives up (`giveup:-2:PCREC_ERR_STEPS`) on 5 of
75 subjects where BEFORE (`b1885a83`) all 75 passed cleanly. This sits
inside the (e)/G2 population's own patterns and regimes (§1.5).

---

## 0. SOURCES, SAMPLE SHAPE, HYGIENE — what was read, and how

### 0.1 The eight records

| side | testee | record file (`store/records/capability@0.1/...`) | trials | rows (compile/match) | subjects (thr/srch) |
|---|---|---|---|---|---|
| before | `pcrec_b1885a83_auto-caps-simdna` | `...20260923T114747Z.jsonl` | 5 | 623 / 24,180 | 3 / 75 |
| before | `pcrec_b1885a83_auto-nocaps-simdna` | `...20260923T122232Z.jsonl` | 5 | 627 / 24,570 | 3 / 75 |
| before | `pcrec_b1885a83_vm-caps-simdna` | `...20260923T125206Z.jsonl` | 5 | 623 / 24,180 | 3 / 75 |
| before | `pcrec_b1885a83_vm-in-caps-simdna` | `...20260923T133317Z.jsonl` | 5 | 623 / 24,180 | 3 / 75 |
| after | `pcrec_6ef76820_auto-caps-simdna` | `...20260923T200117Z.jsonl` | 5 | 623 / 24,180 | 3 / 75 |
| after | `pcrec_6ef76820_auto-nocaps-simdna` | `...20260923T203241Z.jsonl` | 5 | 627 / 24,570 | 3 / 75 |
| after | `pcrec_6ef76820_vm-caps-simdna` | `...20260923T210008Z.jsonl` | 5 | 623 / 24,180 | 3 / 75 |
| after | `pcrec_6ef76820_vm-in-caps-simdna` | `...20260923T214059Z.jsonl` | 5 | 623 / 24,180 | 3 / 75 |

Read in full (all eight `kind: setup`/`compile`/`match` rows) via a
standalone Python extraction (`sys.path`-imported `pcrecbench.reduce`
directly, no CLI, no report load) — these are the ONLY files this
ledger's numbers come from. **The whole-store `report` load was NOT
run**; the committed cross-pin report group's `.tsv`/`.md`/
`.matrix.*`/`.subject-grain.*` files were read only for the four spot
checks in §0.2, never loaded as a population. The `.interpretation.md`
sidecar for this report group was **not read** (per the standing rule
that sidecars are stamped against the live index and this ledger does
not need one).

### 0.2 Arithmetic used — the SAME module the reporter imports

Medians, IQRs and verdicts are computed by importing `pcrecbench.reduce`
directly (`read_record`, `cells_from_record`, `reduce_set_cell`), the
exact functions `report.py` calls for `--grain set`. **IQR method
(unchanged convention): Type-7 / Hyndman-Fan linear interpolation, Q1 =
25th percentile, Q3 = 75th percentile.** For exactly 5 sorted per-trial
sums, Q1 = x1, Q3 = x3 (0-indexed), so IQR = x3 − x1.

**Cross-check against the committed cross-pin TSV** (not the source of
the verdicts, a confirmation of them): every median this ledger computed
for `wild-validator-email-owasp`/thr (all four AFTER testees, both
before-pin rows) and `router-prefix-order`/thr (all eight rows, both
pins) matches the report's own `median_ns` column to the printed digit,
and the report's own `delta_verdict` column agrees in direction on every
row checked (e.g. `wild-validator-email-owasp`/`auto-caps`: report
`faster ×625.86`, this ledger's before/after 23158.8185/37.0030 ns,
23158.8185/37.0030 = 625.86 — the same arithmetic read twice;
`router-prefix-order`/`auto-caps`/AFTER: report `unchanged (within
spread)`, this ledger's Δ% = −0.068%, consistent). The report's own `n`
column reads 3 for `large-subject-throughput` cells — confirmed to be
`n_subjects` (3), not `n_trials` (5): this ledger's own `SetCell.n_trials`
is 5 wherever a cell's `n_trials` is asserted, matching the `subjects
(thr)` column of §0.1, not the report's `n`.

### 0.3 Window provenance (BEFORE and AFTER)

Both windows: 5 trials, **trial-agreement `verdict: agree` on ALL EIGHT
records, 0 `groups_disagreeing` on every one, `rule: v1.4-group`, `k=1.5
d_min=2 share_c=3`**, attempt 1 throughout (a single record file per
testee directory on both sides; no `inconclusive-spread` re-measure).

| side | testee | load1 (before→after) | occupancy target% (before→after) | occupancy max-other% (before→after) | rows_disagreeing / rows_judged | worst_group |
|---|---|---|---|---|---|---|
| before | auto-caps | 0.40 → 1.00 | 7.01 → 0.0 | 2.2 → 1.6 | 7 / 4834 | phone-palindrome-6 / srch |
| before | auto-nocaps | 0.73 → 1.01 | 0.0 → 0.0 | 0.4 → 1.8 | 4 / 4912 | phone-palindrome-6 / srch |
| before | vm-caps | 0.74 → 1.01 | 0.0 → 0.0 | 2.0 → 1.0 | 2 / 4834 | phone-palindrome-6 / srch |
| before | vm-in-caps | 0.73 → 1.07 | 0.4 → 0.0 | 1.8 → 0.8 | 7 / 4834 | phone-palindrome-6 / srch |
| after | auto-caps | 0.40 → 1.00 | 0.0 → 0.0 | 2.4 → 1.8 | 13 / 4834 | **floor-byte / srch** (d=10, n=75) |
| after | auto-nocaps | 0.73 → 1.00 | 0.2 → 0.0 | 1.0 → 0.6 | 5 / 4912 | phone-palindrome-6 / srch |
| after | vm-caps | 0.73 → 1.01 | 0.2 → 0.0 | 0.8 → 1.6 | 6 / 4829 | phone-palindrome-6 / srch |
| after | vm-in-caps | 0.73 → 1.09 | 0.6 → 0.0 | 1.2 → 2.4 | 7 / 4829 | phone-palindrome-6 / srch |

All eight records' `occupancy.*.verdict` and `load.verdict` read `pass` /
`quiet` on both before/after samples (load limit 2.0, occupancy limit
10.0%); the highest gate-scope reading either side is 7.01% (BEFORE
auto-caps' own BEFORE-sample target-core reading), well under the 10%
bar. **The AFTER auto-caps record's own worst trial-agreement group is
`floor-byte`/`short-subject-search` (d=10), not the usual
`phone-palindrome-6`** — consistent with §1.5's independent finding that
`floor-byte`/srch/`auto-caps` is this ledger's largest DFA-route
regression (+15.34%, §1.5).

Neither window shows a `did-not-compile`/`compile_outcome` change from
its predecessor beyond the pre-existing `wild-datetime-datefinder-
alternation` refusal (unchanged both sides, §2.4).

**KB-27 standing check** (`evil-alt-nested` × `{rd-evil-alt-near-miss,
sd-empty-alt-hit}` under `short-subject-search`, read at the per-subject
level on all four AFTER and all four BEFORE testees): **unchanged across
this pin boundary** — `auto-caps`/`vm-caps`/`vm-in-caps` read
`outcome_counts={'gave-up': 5}` on both subjects on both pins;
`auto-nocaps` reads `{'did-not-match-as-expected': 5}` with
`n_no_expectation=5` on both subjects on both pins.

---

## 1. THE D119 GRID — I-102's acceptance / no-move / negative-control cells

### 1.1 (a) `wild-validator-email-owasp` thr, all four testees

| testee | before (ns) | before IQR | after (ns) | after IQR | Δ% | verdict |
|---|---|---|---|---|---|---|
| auto-caps | 23,158.8185 | 27.5238 | 37.0030 | 2.1000 | −99.8402% | **improve** |
| auto-nocaps | 23,119.5113 | 23.6273 | 37.9869 | 0.5197 | −99.8357% | **improve** |
| vm-caps | 23,200.5299 | 30.9018 | 63.1253 | 0.9127 | −99.7279% | **improve** |
| vm-in-caps | 23,118.8386 | 45.8945 | 68.7533 | 1.1300 | −99.7026% | **improve** |

**4/4 MEET.** I-102 EXPECTed a return to 43.7-85.3 ns; measured AFTER
values are 37.0-68.8 ns — `auto-caps` and `auto-nocaps` land BELOW the
predicted floor, `vm-caps`/`vm-in-caps` land inside the predicted range.
The recovery is, on this population, MORE complete than predicted on
the DFA route.

### 1.2 (b) `winpath-near-miss` / `email-nested-plus` thr, all four testees

| pattern | testee | before (ns) | before IQR | after (ns) | after IQR | Δ% | verdict |
|---|---|---|---|---|---|---|---|
| winpath-near-miss | auto-caps | 23,143.3070 | 33.1787 | 18.7629 | 0.1162 | −99.9189% | **improve** |
| winpath-near-miss | auto-nocaps | 23,144.9759 | 27.1402 | 18.9072 | 0.1913 | −99.9183% | **improve** |
| winpath-near-miss | vm-caps | 23,143.2307 | 3.9213 | 27.6810 | 0.0731 | −99.8804% | **improve** |
| winpath-near-miss | vm-in-caps | 23,156.0005 | 10.6557 | 36.4342 | 0.0370 | −99.8427% | **improve** |
| email-nested-plus | auto-caps | 23,136.0637 | 22.0331 | 48.0600 | 1.4195 | −99.7923% | **improve** |
| email-nested-plus | auto-nocaps | 23,133.7826 | 22.0908 | 37.0674 | 1.0217 | −99.8398% | **improve** |
| email-nested-plus | vm-caps | 23,126.7316 | 30.5224 | 7,206.8781 | 14.8030 | −68.8375% | **improve** |
| email-nested-plus | vm-in-caps | 23,148.1124 | 35.0873 | 7,257.3766 | 18.0592 | −68.6481% | **improve** |

**8/8 MEET the D119 bar.** `winpath-near-miss` matches the ~20 ns
prediction closely on all four testees. `email-nested-plus`'s DFA route
matches the ~47 ns prediction (`auto-caps` 48.06 ns almost exact); its
**forced-VM route recovers only to ~7,200-7,257 ns, not the predicted
~47 ns** — a real, large improvement (−68.6% to −68.8%) that clears its
own before-IQR by two orders of magnitude, but two orders of magnitude
short of the literal prediction. See §1.5 for why: this same pattern's
`short-subject-search` regime on the SAME forced-VM testees newly gives
up on 5 of 75 subjects.

### 1.3 (c) `wild-codegrammar-json-array-begin` thr, all four testees

| testee | before (ns) | before IQR | after (ns) | after IQR | Δ% | verdict |
|---|---|---|---|---|---|---|
| auto-caps | 349,719.4624 | 35.0927 | 263,314.2062 | 93.9647 | −24.7070% | **improve** |
| auto-nocaps | 349,629.0908 | 690.8051 | 263,573.7081 | 83.1218 | −24.6133% | **improve** |
| vm-caps | 1,101,475.3525 | 2,248.3320 | 1,098,667.1130 | 639.3087 | −0.2550% | **improve** |
| vm-in-caps | 1,094,794.5451 | 3,007.6803 | 1,114,970.9750 | 4,883.3167 | **+1.8429%** | **regress** |

**3/4 MEET, 1/4 MISS.** The DFA route (`auto-caps`/`auto-nocaps`) shows
the predicted "duplicated `memchr` gone, one pass not two" recovery
cleanly (−24.6% to −24.7%). The forced-VM pair, where `REQ_WHY` reads
`dominated` under `auto` but `emitted` under forced `--engine=vm` (§3 —
G1's dominance test reads the DFA route's own candidate-start scan, so a
forced-VM artifact has nothing to be dominated by), shows only a
near-flat move on `vm-caps` (−0.26%, inside its own IQR by a wide margin
in absolute terms but still counted `improve` since |Δ| > IQR) and a
genuine small regression on `vm-in-caps` (+1.84%, 8.3× its before-IQR).

### 1.4 (d) `uuid-near-miss` / `ipv4-near-miss`, thr + srch, DFA route only

| pattern | regime | testee | before (ns) | before IQR | after (ns) | after IQR | Δ% | verdict |
|---|---|---|---|---|---|---|---|---|
| uuid-near-miss | thr | auto-caps | 27.5693 | 0.0281 | 13.4781 | 0.0308 | −51.1118% | **improve** |
| uuid-near-miss | thr | auto-nocaps | 27.5763 | 0.0308 | 13.3459 | 0.0334 | −51.6037% | **improve** |
| uuid-near-miss | srch | auto-caps | 671.5267 | 6.2408 | 547.9335 | 0.8455 | −18.4048% | **improve** |
| uuid-near-miss | srch | auto-nocaps | 671.4460 | 3.0971 | 548.5520 | 3.9204 | −18.3029% | **improve** |
| ipv4-near-miss | thr | auto-caps | 24.8825 | 0.0196 | 12.5508 | 0.0312 | −49.5597% | **improve** |
| ipv4-near-miss | thr | auto-nocaps | 24.8968 | 0.0251 | 12.6158 | 0.0854 | −49.3279% | **improve** |
| ipv4-near-miss | srch | auto-caps | 627.2089 | 0.3582 | 444.9051 | 0.6518 | −29.0659% | **improve** |
| ipv4-near-miss | srch | auto-nocaps | 627.4275 | 1.7070 | 444.8196 | 2.8811 | −29.1042% | **improve** |

**8/8 MEET**, EXPECTED range (batch-1's +18.7%..+38.5% recovered) — the
measured recovery here is even larger (−18.3% to −51.6%).

### 1.5 (e) The G2 population — the primary 12 named cells, and the 72-cell superset

I-102's own text: *"the batch-1 29 regressing cells `cycle1_ledger_
reading.md` §6 G2 named, plus the 4 G1 cells — EXPECT improvement or
flat, none regressing."* `cycle1_ledger_reading.md`'s own G2 section
(§6) states the population's COUNT and SOURCE-SECTION breakdown ("9
patterns, 27 artifact-configs, 29 regressing ledger cells — 8 carve-out
rows, 8 of §2.1, 13 of §2.2") but this ledger could not resolve all 29
into individual `(pattern, regime, testee)` triples from the document's
own prose: §2.1's own table shows ZERO attributable regressions (its
"four patterns... regressing 1.0-4.7%" correction names patterns
OUTSIDE the G2 9-pattern list), so the "8 of §2.1"/"13 of §2.2" phrase
could not be traced to specific rows beyond what is captured below.
**12 of the 29 cells ARE individually locatable by name**, cited to
their exact source:

| pattern | regime | testee(s) | source citation |
|---|---|---|---|
| uuid-near-miss | thr, srch | auto-caps, auto-nocaps | §2.2 "carve-outs charged to it: uuid-near-miss, ipv4-near-miss (16 rows) → 8 regress"; §4.2's own "8 regress 18.7-38.5%" — 4 cells |
| ipv4-near-miss | thr, srch | auto-caps, auto-nocaps | same citation — 4 cells |
| winpath-near-miss | srch | auto-caps, auto-nocaps | §4.3 table: "+17.07 / +17.00 ... winpath-near-miss srch auto-caps/auto-nocaps ... one-start (G2)" — 2 cells |
| wild-validator-ipv4-owasp | srch | auto-nocaps | §4.3 table: "+25.64 ... wild-validator-ipv4-owasp srch auto-nocaps ... one-start (G2)" — 1 cell |
| logparse-atomic-removed | srch | auto-nocaps | §4.3 table: "+34.06 ... logparse-atomic-removed srch auto-nocaps ... one-start (§6 G2)" — 1 cell |

**These 12 are this ledger's PRIMARY (e) population. Result: 12/12
MEET** (all improve beyond before-IQR under this pin pair — the
`uuid-near-miss`/`ipv4-near-miss` 8 are letter (d)'s own already-scored
cells, §1.4; the 4 more score below).

| pattern | regime | testee | before (ns) | after (ns) | Δ% | verdict |
|---|---|---|---|---|---|---|
| winpath-near-miss | srch | auto-caps | 644.9036 | 488.9509 | −24.1823% | **improve** |
| winpath-near-miss | srch | auto-nocaps | 644.8550 | 494.2175 | −23.3599% | **improve** |
| wild-validator-ipv4-owasp | srch | auto-nocaps | 626.7226 | 446.2860 | −28.7905% | **improve** |
| logparse-atomic-removed | srch | auto-nocaps | 649.8574 | 517.7485 | −20.3289% | **improve** |

**The remaining 17 of the 29 cells are the count gap** this ledger
could not resolve into named `(pattern, regime, testee)` triples from
`cycle1_ledger_reading.md`'s own text. They are contained somewhere
within the SECONDARY population below (the 9-pattern × both-regime × 4
testee superset), which this ledger scores in full as a second table,
per instruction, rather than omitted.

### 1.5b The SECONDARY 72-cell superset (9 named patterns × both regimes × 4 testees)

`email-nested-plus`, `ipv4-near-miss`, `logparse-atomic`,
`logparse-atomic-removed`, `uuid-near-miss`, `wild-datetime-moment-
iso8601`, `wild-validator-email-owasp`, `wild-validator-ipv4-owasp`,
`winpath-near-miss` — × both regimes × 4 testees (72 cells, a SUPERSET
of the named 29 that also contains letters (b)/(d)'s own already-clean
target cells; two cells are expectation-failing rather than a regime ×
testee this population otherwise has).

**Aggregate (before-IQR bar): 49 improve, 21 regress, 2 newly
expectation-failing (0 missing, 0 within-bar). Under pcrec's own
+8.4605% null band** (`cycle1_ledger_reading.md` §9(B) / O-48 Block B,
120 program-identical cells, min −5.7393%/max +8.4605%/median
−0.0806%; bar `|Δ| > max(IQR, 8.4605%)`, ONE-SIDED applied here per
instruction): **45 improve, 17 regress, 8 within-bar, 2 expectation-
failing.** Neither reading meets "improvement or flat, none
regressing."

Regressing cells under the before-IQR bar (21); the "beyond null band"
column marks whether the cell ALSO regresses under `|Δ| >
max(IQR, 8.4605%)` (pcrec's own cited band, §9(B)/O-48 Block B):

| pattern | regime | testee | Δ% | beyond null band too? |
|---|---|---|---|---|
| ipv4-near-miss | thr | vm-caps | +31.19% | yes |
| ipv4-near-miss | thr | vm-in-caps | +23.75% | yes |
| ipv4-near-miss | srch | vm-caps | +33.65% | yes |
| ipv4-near-miss | srch | vm-in-caps | +11.83% | yes |
| logparse-atomic | srch | auto-caps | +1.61% | **no — inside band** |
| logparse-atomic | srch | auto-nocaps | +3.06% | **no — inside band** |
| uuid-near-miss | srch | vm-caps | +23.92% | yes |
| uuid-near-miss | srch | vm-in-caps | +9.97% | yes |
| wild-datetime-moment-iso8601 | srch | auto-caps | +15.07% | yes |
| wild-datetime-moment-iso8601 | srch | vm-caps | +70.20% | yes |
| wild-datetime-moment-iso8601 | srch | vm-in-caps | +68.41% | yes |
| wild-validator-email-owasp | srch | auto-caps | +65.80% | yes |
| wild-validator-email-owasp | srch | auto-nocaps | +66.38% | yes |
| wild-validator-email-owasp | srch | vm-caps | +78.88% | yes |
| wild-validator-email-owasp | srch | vm-in-caps | +72.41% | yes |
| wild-validator-ipv4-owasp | thr | vm-caps | +3.38% | **no — inside band** |
| wild-validator-ipv4-owasp | thr | vm-in-caps | +1.71% | **no — inside band** |
| wild-validator-ipv4-owasp | srch | vm-caps | +28.57% | yes |
| wild-validator-ipv4-owasp | srch | vm-in-caps | +38.36% | yes |
| email-nested-plus | srch | auto-caps | +53.93% | yes |
| email-nested-plus | srch | auto-nocaps | +53.84% | yes |

**17 of the 21 stay outside the null band; 4 fall inside it**
(`logparse-atomic`/srch ×2, `wild-validator-ipv4-owasp`/thr ×2 — all
four are ≤3.38%, below the 8.4605% ceiling). Every one of the 21
regressions sits on a `short-subject-search` cell or the two
`ipv4-near-miss` forced-VM throughput cells — no `large-subject-
throughput` DFA-route cell in this population regresses. The
`wild-validator-email-owasp`/srch and `email-nested-plus`/srch
regressions are the largest in this table (+53.8% to +78.9%): I-102's
own grid names these patterns' THROUGHPUT regime as a target ((a)/(b))
but the SEARCH regime is not separately named — it is scored here only
because it is part of the G2 population's declared scope.

**The two expectation-failing cells** (`email-nested-plus` / `short-
subject-search` / `vm-caps` and `/vm-in-caps`) are a NEW give-up, not a
timing move. Record facts only, read at the per-subject level:

| subject | BEFORE (`b1885a83`) outcome | AFTER (`6ef76820`) outcome | trials each side |
|---|---|---|---|
| sd-empty-alt-hit | matched, 5/5 | `gave-up`, 5/5, `giveup:-2:PCREC_ERR_STEPS` | 5 |
| sd-empty-alt-miss | matched, 5/5 | `gave-up`, 5/5, `giveup:-2:PCREC_ERR_STEPS` | 5 |
| sec-github-pat | matched, 5/5 | `gave-up`, 5/5, `giveup:-2:PCREC_ERR_STEPS` | 5 |
| v-uuid-badnibble | matched, 5/5 | `gave-up`, 5/5, `giveup:-2:PCREC_ERR_STEPS` | 5 |
| v-uuid-valid | matched, 5/5 | `gave-up`, 5/5, `giveup:-2:PCREC_ERR_STEPS` | 5 |

Present on both `vm-caps` and `vm-in-caps` (25 gave-up rows per testee
= 5 subjects × 5 trials; 50 gave-up rows total). Confirmed by a full
population scan (all 63×2×4 `(pattern, regime, testee)` cells present
on both pins): this is the ONLY cell in the entire population — named
or sweep — where a subject that passed BEFORE fails AFTER, on either
testee. No cell shows the reverse (a BEFORE-failing subject resolved
AFTER).

`email-nested-plus`'s own compile-row stamps, BEFORE vs AFTER, on all
four testees:

| stamp | BEFORE (`b1885a83`, abi 30) | AFTER (`6ef76820`, abi 31) |
|---|---|---|
| `req_byte` | `64` | `64` (unchanged) |
| `req_run` | `none` | `none` (unchanged) |
| `req_why` | field absent (abi 30 predates the stamp) | `one-attempt`, all four testees |
| `end_window` | `none` | `none` (unchanged) |
| `engine` | `vm` (auto-caps/vm-caps/vm-in-caps), `dfa` (auto-nocaps) | unchanged |

No further mechanism is claimed here; what the pre-check DID with the
removed byte-64 check ahead of the forced-VM attempt is pcrec's own to
diagnose.

### 1.6 "The 4 G1 cells" — NAMED, and identical to letter (c)'s own population

`cycle1_ledger_reading.md` §4.3's own "14 non-named cells above the null
band" table itemizes the G1 ("duplicated pass") rows by name: "+32.60
/ +32.50 | `wild-codegrammar-json-array-begin` thr `auto-nocaps`/
`auto-caps` | duplicated pass (G1)" and "+15.45 / +14.39 |
`wild-codegrammar-json-array-begin` thr `vm-in-caps`/`vm-caps` |
duplicated pass (G1)" -- four rows, one pattern, one regime, all four
testees: `wild-codegrammar-json-array-begin` / `large-subject-
throughput` / {`auto-nocaps`, `auto-caps`, `vm-in-caps`, `vm-caps`}. Section
7's own recommendation table confirms the count independently ("29
regressing cells come from ONE declinable predicate and 4 more from a
duplicated pass").

**This is the IDENTICAL population already scored as letter (c), Section 1.3
above** -- no new measurement is needed; the result carries over
unchanged: **3/4 MEET, 1/4 MISS** (`vm-in-caps` regresses +1.8429%; the
other three testees improve, `auto-caps`/`auto-nocaps` by -24.6% to
-24.7%, `vm-caps` by -0.26%). See Section 1.3 for the full before/after table.
The `floor-byte` reading this ledger's prior draft used as an inference
is WITHDRAWN -- it is not what "the 4 G1 cells" names.

### 1.7 (f) `nested-comment-rec` thr — no-move control

| testee | before (ns) | before IQR | after (ns) | after IQR | Δ% | verdict |
|---|---|---|---|---|---|---|
| auto-caps | 23,118.4635 | 13.4516 | 23,172.8001 | 22.2915 | +0.2350% | **regress** |
| auto-nocaps | 23,134.7268 | 13.4391 | 23,148.6152 | 37.4097 | +0.0600% | **regress** |
| vm-caps | 23,152.5167 | 28.1843 | 23,138.6898 | 14.8258 | −0.0597% | within-bar |
| vm-in-caps | 23,149.2921 | 40.0769 | 23,133.3014 | 10.5157 | −0.0691% | within-bar |

`auto-caps`/`auto-nocaps` cross their own tight before-IQR by 4-9 ns on
a ~23,100 ns floor (+0.06% to +0.24%) — technically `regress` under the
strict before-IQR bar, but this ledger flags rather than scores it a
miss: every prior ledger's own context-only null band at this same
floor scale (I-97/O-48's cited −5.74%..+8.46%, and this ledger's own §2
sweep at floor scale, both far wider) would read both moves as noise.
`RX_REQ_WHY` reads `emitted` on all four testees (byte 42, run `2a2f@0`
→ `"*/"@0`, both KEPT) — the artifact's own mechanism is unchanged
per §3; no code-level cause is claimed for the 4-9 ns move.

### 1.8 (g) `wild-secrets-github-pat` thr, forced-VM pair — no-move control

| testee | before (ns) | before IQR | after (ns) | after IQR | Δ% | verdict |
|---|---|---|---|---|---|---|
| vm-caps | 129,145.4333 | 248.8786 | 129,109.7361 | 335.6131 | −0.0276% | within-bar |
| vm-in-caps | 125,586.1034 | 85.8417 | 125,631.8944 | 255.6597 | +0.0365% | within-bar |

**2/2 clean.** `RX_REQ_WHY` reads `emitted` on both, byte 95, run
`6875625f7061745f@3` (`"hub_pat_"@3`) — unchanged.

### 1.9 (h) `router-prefix-order` / `keyword-prefix-order` thr — negative controls

| pattern | testee | before (ns) | before IQR | after (ns) | after IQR | Δ% | verdict |
|---|---|---|---|---|---|---|---|
| router-prefix-order | auto-caps | 720,485.5877 | 170.0585 | 719,995.5630 | 1,016.7535 | −0.0680% | improve |
| router-prefix-order | auto-nocaps | 720,106.0812 | 780.1989 | 720,273.2765 | 895.4553 | +0.0232% | within-bar |
| router-prefix-order | vm-caps | 4,451,241.0000 | 6,312.4483 | 4,459,252.0847 | 1,322.5593 | +0.1800% | regress |
| router-prefix-order | vm-in-caps | 4,441,972.6102 | 6,396.4915 | 4,443,144.3051 | 5,810.0339 | +0.0264% | within-bar |
| keyword-prefix-order | auto-caps | 1,236,473.0350 | 1,050.1600 | 1,238,485.2350 | 1,167.4050 | +0.1627% | regress |
| keyword-prefix-order | auto-nocaps | 1,237,361.0625 | 385.3466 | 1,239,078.3125 | 687.5573 | +0.1388% | regress |
| keyword-prefix-order | vm-caps | 4,625,668.9821 | 5,613.8036 | 4,617,899.0714 | 1,188.0179 | −0.1680% | improve |
| keyword-prefix-order | vm-in-caps | 4,643,087.0357 | 8,679.1429 | 4,640,082.7368 | 8,554.0702 | −0.0647% | within-bar |

**Consistent with "NO CHANGE"**: every row is ≤ ±0.18%, sign mixed, no
row exceeding ~0.2%. The committed cross-pin report's own
`delta_verdict` reads `unchanged (within spread)` on every AFTER row of
this table this ledger cross-checked (§0.2). `RX_REQ_WHY` reads
`emitted` on both patterns, all four testees, unchanged — the fix does
not reach either pattern, exactly as I-102 predicted.

---

## 2. THE WHOLE-POPULATION REGRESSION SWEEP (non-named cells)

Every `(pattern, regime, testee)` cell present on both pins EXCLUDING
the named populations of §1.1-§1.9 (the G2 9-pattern population, `wild-
codegrammar-json-array-begin`/thr, `nested-comment-rec`/thr,
`router-prefix-order`/thr, `keyword-prefix-order`/thr,
`wild-secrets-github-pat`/thr forced-VM pair — §1.6's "4 G1 cells" are
`wild-codegrammar-json-array-begin`/thr, already excluded as part of
that set). `floor-byte` is left IN the sweep — it is not named by any
letter of I-102's grid.

**126 (pattern, regime) keys, plain form, present on both pins** (63
patterns × 2 regimes) → **504 cells over 4 testees; 90 named (§1), 414
swept.**

**No null band was applied in the primary sweep below — this is an
IQR-only bar, `|Δ| > before-IQR`, per this ledger's own §0.2 convention
(the same bar §1 uses for every named cell).** A secondary count under
`|Δ| > max(IQR, 8.4605%)` — pcrec's own null band, `cycle1_ledger_
reading.md` §9(B)/O-48 Block B, 120 program-identical cells, min
−5.7393%/max +8.4605%/median −0.0806%, cited here as PCREC's measured
band, not this ledger's own (the bench's own equivalent is under
construction, [B79]) — follows the primary count.

**Sweep aggregate (before-IQR, no null band): 88 improve, 133 regress,
183 within-bar, 6 missing, 4 expectation-failing.**

**Sweep aggregate under `|Δ| > max(IQR, 8.4605%)` (pcrec's cited null
band, one-sided +8.4605% applied to the regression side): 1 improve,
17 regress, 386 within-bar, 6 missing, 4 expectation-failing.** All 17
of the null-band-surviving regressions are also in the top 27 of the
before-IQR-only count above (every one exceeds 8.4605% outright); the
two counts (133 vs 17) diverge because most of the 133 before-IQR
regressions are small absolute moves against very tight IQRs (before-
IQRs well under 1% of the cell's own median at floor and microsecond
scale) that the wider null band absorbs as noise.

The 6 missing and 4 expectation-failing cells are BOTH SIDES' own
pre-existing populations, UNCHANGED by this pin (confirmed by a direct
per-subject scan, not assumed): `wild-datetime-datefinder-alternation`
(`did-not-compile` on `auto-caps`/`vm-caps`/`vm-in-caps`, both regimes,
both pins — 6 missing cells) and `evil-alt-nested`/`short-subject-
search` (expectation-failing on all four testees, both pins — the KB-27
population, §0.3).

**133 sweep regressions beyond before-IQR, by testee**: `auto-nocaps` 43,
`auto-caps` 40, `vm-in-caps` 27, `vm-caps` 23. **By regime**: `short-
subject-search` 73, `large-subject-throughput` 60. **All 27 regressions
exceeding 5% sit on the DFA route (`auto-caps`/`auto-nocaps`) — ZERO
forced-VM sweep regression exceeds 5%.**

Top 15 sweep regressions by |Δ%| (before-IQR reading):

| pattern | regime | testee | before (ns) | after (ns) | Δ% |
|---|---|---|---|---|---|
| codegrammar-flat | srch | auto-caps | 713.8574 | 909.9910 | +27.48% |
| codegrammar-xflag | srch | auto-caps | 712.6363 | 904.5481 | +26.93% |
| floor-byte | srch | auto-caps | 599.5766 | 691.5704 | +15.34% |
| floor-byte | srch | auto-nocaps | 598.8684 | 678.5362 | +13.30% |
| wild-codegrammar-json-object-begin | srch | auto-nocaps | 598.3363 | 677.6450 | +13.25% |
| mojibake-curly-quote | srch | auto-nocaps | 620.1483 | 695.3362 | +12.12% |
| mojibake-curly-quote | srch | auto-caps | 619.8551 | 694.1231 | +11.98% |
| wild-codegrammar-json-object-begin | srch | auto-caps | 598.3317 | 669.7269 | +11.93% |
| numeric-id-nested-plus | srch | auto-nocaps | 445.6431 | 498.4684 | +11.85% |
| phone-list-nested-plus | thr | auto-nocaps | 14.3254 | 16.0213 | +11.84% |
| wild-validator-us-zip-owasp | srch | auto-nocaps | 417.7670 | 465.9170 | +11.53% |
| wild-codegrammar-json-array-begin | srch | auto-nocaps | 624.5777 | 695.7530 | +11.40% |
| phone-list-nested-plus | srch | auto-nocaps | 454.7073 | 505.2373 | +11.11% |
| wild-codegrammar-json-array-begin | srch | auto-caps | 624.4521 | 692.4232 | +10.88% |
| wild-codegrammar-json-stringcontent-escape | srch | auto-nocaps | 675.0793 | 744.2945 | +10.25% |

Full 133-row and 414-row populations are in this lane's own extraction
scripts (`extract.py`/`sweep.py`, session scratchpad; not committed —
the numbers above and their aggregate counts are what carries forward).
27 of the 133 regressions exceed 5%; the remaining 106 are below 5%,
concentrated (as the aggregate table shows) on `short-subject-search`.

**No non-named cell shows a NEW expectation failure or a resolved one**
(§1.5's scan covered the full population, not only the named cells).

---

## 3. THE REQ_WHY CENSUS — the fourth independent derivation

Computed from the four AFTER records' own `plain`-form compile rows,
grouped by `pattern_id`, using the 3-artifact-config convention
`b84repin_report.md` item 7 establishes (`auto-caps`=`pcrec-auto`,
`auto-nocaps`=`pcrec-nocaps`, `vm-caps`=`pcrec-vm`; `vm-in-caps` is
compile-identical to `vm-caps` — confirmed here too, every `req_why`/
`req_byte`/`req_run` value identical between the two on every pattern
this ledger checked — so counting it separately would double-count).

| token | this ledger's own count (artifact-configs) | this ledger's own count (patterns) | cited figure (I-102/b84repin_report.md) |
|---|---|---|---|
| none | 79 | 27 | 79 / 27 |
| emitted | 67 | 27 | 67 / 27 |
| one-attempt | 27 | 9 | 27 / 9 |
| dominated | 14 | 7 | 14 / 7 |

**Total: 187 artifact-configs, 5 refusals** (`wild-datetime-datefinder-
alternation` on `auto-caps`/`vm-caps`; `negation-scope-lookbehind-var`
on all three census configs) — **digit-exact agreement with the cited
figure**, independently re-derived from the AFTER records themselves
(the fifth derivation counting b84repin_report.md's own, the reading's,
I-99's, I-102a's, and this one).

**7 patterns whose REQ_WHY token diverges by config** (all `dominated`
under `auto-caps`/`auto-nocaps`, `emitted` under `vm-caps` — the DFA-vs-
forced-VM dominance-test asymmetry noted in §1.3/§1.6): `codegrammar-flat`,
`codegrammar-xflag`, `floor-byte`, `mojibake-curly-quote`, `wild-
codegrammar-json-array-begin`, `wild-codegrammar-json-object-begin`,
`wild-codegrammar-json-stringcontent-escape`.

### 3.1 Each acceptance-cell pattern's REQ_WHY token, all four testees (AFTER)

| pattern | auto-caps | auto-nocaps | vm-caps | vm-in-caps |
|---|---|---|---|---|
| wild-validator-email-owasp | one-attempt (byte 64) | one-attempt | one-attempt | one-attempt |
| winpath-near-miss | one-attempt (byte 92, run `3a5c@1`) | one-attempt | one-attempt | one-attempt |
| email-nested-plus | one-attempt (byte 64) | one-attempt | one-attempt | one-attempt |
| wild-codegrammar-json-array-begin | dominated (byte 91) | dominated | emitted | emitted |
| uuid-near-miss | one-attempt (byte 45) | one-attempt | one-attempt | one-attempt |
| ipv4-near-miss | one-attempt (byte 46) | one-attempt | one-attempt | one-attempt |
| nested-comment-rec | emitted (byte 42, run `2a2f@0`) | emitted | emitted | emitted |
| wild-secrets-github-pat | emitted (byte 95, run `6875625f7061745f@3`) | emitted | emitted | emitted |
| router-prefix-order | emitted (byte 47, run `2f75736572@0`) | emitted | emitted | emitted |
| keyword-prefix-order | emitted (byte 110, run `696e@1`) | emitted | emitted | emitted |
| floor-byte | dominated (byte 126) | dominated | emitted | emitted |

Every one of I-102's ten own named predictions (§8/`b84repin_report.md`
item 6) is confirmed again here from the AFTER records directly.

---

## 4. PROVENANCE

Window: **BEFORE 2026-09-23T11:47:47Z → 13:33:17Z (record write
timestamps; the same records that were the AFTER of the prior batch-2
ledger); AFTER 2026-09-23T20:01:17Z → 21:40:59Z (16:01-17:41 EDT,
finishing ~18:22 EDT — matching the brief's stated 16:00-18:22 EDT), 4/4
cells attempt-1 on each side**, trial-agreement `verdict: agree` on all
8 records with 0 `groups_disagreeing` (§0.3). Worst gate-scope reading
either window: 7.01% target-core busy (BEFORE auto-caps' pre-sample),
well under the 10% pre-flight bar.

Queries: this ledger's own extraction scripts (`extract.py`, `grid.py`,
`census.py`, `sweep.py`; `pcrecbench.reduce` imported directly against
the 8 `.jsonl` files by path — no CLI, no report load); the cross-check
against `reports/2026-09-23-capability-0.1-budu-ryzen1600-after-
6ef76820.tsv` was a `grep '^rank\t<pattern>\t(set)\t<regime>'` on two
named patterns (§0.2); `docs/dev/lanes/b84repin_report.md` in full
(stamp census cross-check, §3); `~/pcrec` (READ-ONLY) commits
`99e529d6` (`docs/dev/optloop/cycle2_batch2_reading.md`, full text) and
`b14a6ae1` (`docs/dev/optloop/cycle1_ledger_reading.md`, full text) —
both read via `git show <commit>:<path>` from the main pcrec-bench
checkout, no pcrec worktree touched, no write; `docs/dev/inbox_from_
pcrec.md`'s I-102/I-102a/I-102b/I-103/I-103a/I-104 entries in full.

**What was NOT read**: the whole-store report load (never run — all
numbers come from the 8 record files directly, per the box hazard
warning in this lane's brief); the committed report's
`.subject-grain.tsv`/`.matrix.html` renders and its `.interpretation.md`
sidecar; `cycle1_ledger_reading.md`'s §3/§5 worked-example prose beyond
what §1.5/§1.6/§3 here needed (its cost-model arithmetic is not
re-derived here — this ledger is numbers-from-records only, not a
re-run of pcrec's own cost model); any per-cell itemized 29-row table
for the G2 population, if one exists elsewhere in `cycle1_ledger_
reading.md` beyond its own §2.1/§2.2/§4.2/§4.3/§6 text — 12 of the 29
cells were resolved by name from §2.2/§4.2/§4.3's own explicit labels
(§1.5), the remaining 17 were not found in the sections read, hence
§1.5b's stated superset substitution for them. The G1 population WAS
fully resolved (§4.3's own table, §1.6) — no gap there.

---

## 5. RANKED FINDINGS (facts only)

1. **The four literal target letters (a)/(b)/(d) MEET the D119 bar
   cleanly (4/4, 8/8, 8/8); letter (c) is a near-clean 3/4** (one
   forced-VM cell, `wild-codegrammar-json-array-begin`/`vm-in-caps`,
   regresses +1.84%). The two no-move controls that ARE literally named
   in I-102's own text ((f), (g)) are clean or trivially floor-level;
   the negative control (h) reads as predicted (no change, ≤0.2%
   moves).

2. **The G2 population's PRIMARY 12 named cells (§1.5) all MEET the bar
   (12/12)** — 8 of them are letter (d)'s own already-clean cells; the
   4 more (`winpath-near-miss`/srch, `wild-validator-ipv4-owasp`/srch/
   `auto-nocaps`, `logparse-atomic-removed`/srch/`auto-nocaps`) improve
   −20.3% to −28.8%. **The SECONDARY 72-cell superset (§1.5b), which
   contains the 17 cells this ledger could not resolve to a name in
   `cycle1_ledger_reading.md`'s own text, MISSES**: 21 of 72 regress
   beyond before-IQR (17 of those 21 also exceed pcrec's own +8.4605%
   null band), and every regression sits on `short-subject-search` or a
   forced-VM `ipv4-near-miss`/thr cell — no DFA-route throughput cell in
   this population regresses. The largest regressions
   (`wild-validator-email-owasp`/srch +65.8% to +78.9%,
   `wild-datetime-moment-iso8601`/srch/forced-VM +68.4%/+70.2%,
   `email-nested-plus`/srch/DFA +53.8%/+53.9%) sit on patterns whose
   THROUGHPUT regime is a literal, cleanly-meeting target — the search
   regime of the same patterns was not separately named by I-102 and is
   scored here only because the superset's own definition spans both
   regimes.

3. **The single most consequential finding is a NEW give-up, not a
   timing miss**: `email-nested-plus`/`short-subject-search` on the
   forced-VM route (`vm-caps`, `vm-in-caps`) newly fails on 5 of 75
   subjects (`sd-empty-alt-hit`, `sd-empty-alt-miss`, `sec-github-pat`,
   `v-uuid-badnibble`, `v-uuid-valid`) with `giveup:-2:PCREC_ERR_STEPS`
   (50 gave-up rows: 5 subjects × 5 trials × 2 testees), where BEFORE
   all 75 subjects passed on both testees. A full population scan (all
   63×2×4 cells present on both pins) confirms this is the ONLY newly
   broken cell anywhere, named or swept, and that no cell resolves in
   the other direction. The pattern's own compile-row stamps move from
   `req_byte=64`/`req_why` absent (abi 30) to `req_byte=64`/
   `req_why=one-attempt` (abi 31, all four testees) — `req_byte`,
   `req_run` and `end_window` are otherwise unchanged (§1.5). What the
   removed pre-check did for these five subjects on the forced-VM route
   is not established by these records and is not claimed here; it is
   pcrec's own to diagnose.

4. **"The 4 G1 cells" ARE named**, in `cycle1_ledger_reading.md` §4.3's
   own "duplicated pass (G1)" rows: `wild-codegrammar-json-array-begin`/
   `large-subject-throughput`, all four testees — the IDENTICAL
   population already scored as letter (c) (§1.3, §1.6). Result carries
   over unchanged: 3/4 MEET, `vm-in-caps` MISSES (+1.84%). (This
   ledger's earlier draft inferred `floor-byte` as this population;
   that reading is withdrawn — see §1.6.)

5. **The whole-population sweep (414 non-named cells) shows 133
   regressions beyond before-IQR, concentrated on the DFA route and on
   `short-subject-search`**: `auto-caps`+`auto-nocaps` carry 83 of 133
   (62%); `short-subject-search` carries 73 of 133 (55%); every
   regression exceeding 5% (27 of 133) sits on the DFA route, none on
   forced-VM. `codegrammar-flat`/`codegrammar-xflag`/srch/`auto-caps`
   are the largest (+27.5%/+26.9%). No new expectation failure appears
   outside the one cell finding 3 names.

6. **The REQ_WHY census reproduces the cited figures digit-exact,
   independently, a fifth time**: 79/27 `none`, 67/27 `emitted`, 27/9
   `one-attempt`, 14/7 `dominated` over 187 artifact-configs (5
   refusals), computed directly from the AFTER records' own compile
   rows. All ten of I-102's own named per-pattern predictions (§3.1)
   hold exactly.

7. **Measurement quality is clean on both sides**: all eight records
   attempt-1, trial-agreement `agree` with 0 disagreeing groups on
   every one, box quiet throughout (worst gate-scope reading 7.01%,
   well under the 10% pre-flight limit), no `inconclusive-spread`
   re-measure either side. The AFTER `auto-caps` record's own worst
   trial-agreement group shifts to `floor-byte`/`short-subject-search`
   (from the usual `phone-palindrome-6`) — consistent with, not
   independent evidence for, `floor-byte`/srch/`auto-caps`'s own
   +15.34% sweep regression (§2, not part of any named letter). KB-27's
   standing give-up population
   (`evil-alt-nested`) and the pre-existing `wild-datetime-datefinder-
   alternation` refusal are both unchanged across this pin boundary.
