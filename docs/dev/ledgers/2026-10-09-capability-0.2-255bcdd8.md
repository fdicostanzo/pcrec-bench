# capability@0.2 ledger — the first sample at pcrec 255bcdd8 (abi 68)

Lane `b125read`. Window: `build/windows/window_capability_0.2_20261008T160751Z.log`
(main tree), 2026-10-08 12:07 EDT to 2026-10-09 00:09 EDT, `WINDOW_RUN_COMPLETE
cells=14/14`; store commit `6c5088c`. ~/pcrec was not touched. Every figure below
is read from the committed report group, cited by line:

- `S`  = `reports/2026-10-08-capability-0.2-budu-ryzen1600-first-255bcdd8.tsv` (set grain)
- `SG` = the same name `.subject-grain.tsv` (slice; one row per pattern x subject x testee)
- `MD` = the same name `.md` (the route stamps live there, `Compile cost` section)
- `W`  = the window log; `O-87` / `I-136` = the outbox / inbox entries.

`SG L<n>` cites the row; where I computed a ratio or a per-byte figure from cited
rows it is marked "(computed)". Two numbers come from the records (the `jsonl`
match rows) rather than a report and are marked "(records)". One number is quoted
from O-87 and was NOT re-derived (the c4c70f2c pre-fix spread in §3).

## 0. Reading the numbers: three cautions stated once

1. **First sample.** capability@0.2 has records at one pin only. Prior pins hold
   0.1 records. A cross-pin form was not generated: with one pin there is no
   cross-pin report, and a 0.1 -> 0.2 delta is not like for like (NOTES.md R9).
   Where §2-§3 quote a pre-fix number it is O-87's, labelled.
2. **The 14 testees are not one class.** The `Ranking` sections of the report are
   per class (caps vs caps; nocaps vs nocaps). I compare across classes below only
   where a cell's point is a mechanism (a near-miss, a tail), and say so.
3. **Vectorscan `block-nosom` is boolean-grain** (stops at the first match), so its
   tens-of-nanoseconds on a 1 MiB subject are a first-match cost, not a
   find-all cost. It is quoted in §6 only as the report's own number.

## 1. Report group and population

Named `2026-10-08-capability-0.2-budu-ryzen1600-first-255bcdd8.{tsv,md,matrix.tsv,
subject-grain.tsv,subject-grain.md,interpretation.md}`. Reporter v25 (S L1).
Query: `subbench=capability, version=0.2, since=2026-10-08T16:00:00Z,
until=2026-10-09T04:00:00Z` (S L1). It drew 15 candidate records, ranked 14, 1
superseded (S L1 `records: 14 ... superseded: 1`; interpretation R-STATUS-5).
Generation was one detached load (185 s load, 337 s total), not
`scripts/regen_reports.py`: that script only re-renders groups whose `.tsv`
already exists. The query is stored in the header so a later regen reproduces it.

- All 14 testees carry `agree` trial agreement (S L3-L16); per-testee unjudged
  groups: dfa 67 (6 all-timed-out), tre 65, interp 39, onig 30, jit 6, pcrec
  auto/nocaps 2 each (S L3-L16).
- `worst_other_core_busy: 40.0%` (pcrec vm-caps / bracket-array-define /
  large-subject-throughput, S L1; interpretation R-STATUS-8).
- Match rows in the 14 measured records, by outcome (records): 70,601
  `matched-as-expected`, 88 `did-not-match-as-expected`, 50 `gave-up`, 32
  `wrong-span-or-captures`, 6 `timed-out`, 1 `crashed`. The 88 include 22 rows
  that are "no expectation exists" (§4), 58 on tre, and the semantics cases in §5.
- Excluded cells at set grain: 88 `excluded` rows in S (the md's `Excluded` sections
  open at MD L7999, L12312, L23930); did-not-compile: 30 (S section `did_not_compile`). pcrec's own:
  datefinder refused on `auto-caps`/`vm-caps`/`vm-in-caps` at 589,177 / 589,100 /
  589,100 B of emitted code against the 500,000 cap (S L15357-L15359, L15421-L15423);
  `auto-nocaps` compiles it. This is the 0.1-era refusal, unchanged.
- Sidecar: 14 rules fired; the new facts it states are R-STATUS-2 (the spread
  record, §7), R-STATUS-10 (vm-in's failed after-sample, §7), R-ARM-1/2, R-FLOOR-1/2/3,
  R-BUCKET-DOMINATED. Generated without `--predictions`: there is no
  `docs/dev/predictions/capability-0.2-*.tsv`; P11-P16 live in NOTES.md as prose.

## 2. (a) The [NULLABLE-ANCH] read — evil-alt-nested / trim-nested-star

**Route stamps (what changed in the artifact).**
- `auto-caps` evil-alt-nested: `engine=vm, sel=selected, vm_prefilter=hybrid,
  dfa: scan=attempt prefilter=none ... start=reverse-pass, shape=plain (prog:
  4,191 B)` (MD L24189). Same for trim-nested-star, prog 1,822 B (MD L24241).
  So the caps default is a VM HYBRID whose DFA scan is an "attempt".
- `auto-nocaps` evil-alt-nested: `engine=dfa, match=search-filter, dfa: scan=attempt`
  (MD L24327); trim-nested-star the same (MD L24379). The nocaps default is a pure DFA.
- `vm-caps` / `vm-in-caps`: `engine=vm, sel=forced, vm_prefilter=none, no DFA scan`
  (MD L24466, L24518; L24604, L24656). The forced VM has no relief.

**Short near-misses (expected ~22 ns for pcrec).**

| cell | auto-nocaps | auto-caps | pcre2-jit | pcrec vm | rust | vs-nosom |
|---|---|---|---|---|---|---|
| evil-alt-nested x rd-evil-alt-near-miss (18 B) | 24.1 ns (SG L11382) | 29.1 ns (SG L11383) | gave up x5 (SG L11391) | gave up x5 (SG L11393) | 50.8 (SG L11384) | 51.0 (SG L11385) |
| evil-alt-nested x sd-empty-alt-hit (61 B) | 70.0 (SG L11562) | 72.9 (SG L11563) | gave up x5 (SG L11571) | gave up x5 (SG L11573) | 126.1 (SG L11565) | 91.8 (SG L11564) |
| trim-nested-star x rd-evil-alt-near-miss | 5.3 (SG L40794) | 10.5 (SG L40795) | 44.1 | 16.4 (SG L40796) | 23.1 | 18.7 |

The 22 ns expectation holds to within +10% (nocaps) / +32% (caps) on the first
row. Both auto routes give up 0 times on the two formerly-unjudged subjects (§4);
forced VM, pcre2 interp/jit and Oniguruma give up 5/5 trials on both.

**The matching tax (K97): long MATCHING subjects, whole-subject match (0,61440).**

| cell | auto-nocaps | auto-caps | vm (forced) | pcre2-jit | auto-caps / vm | auto-caps / jit | auto-nocaps / jit |
|---|---|---|---|---|---|---|---|
| evil-alt-nested x t-evil-match-60k | 54,470 ns (SG L11746) | 81,023 (SG L11748) | 26,445 (SG L11743) | 24,415 (SG L11742) | 3.06x | 3.32x | 2.23x |
| trim-nested-star x t-trim-match-60k | 73,331 (SG L41249) | 100,217 (SG L41250) | 45,892 (SG L41247) | 27,623 (SG L41244) | 2.18x | 3.63x | 2.65x |

(ratios computed). Per byte, auto-nocaps 0.89 / 1.19 ns/B, auto-caps 1.32 / 1.63
ns/B, jit 0.40 / 0.45 ns/B (computed). Read plainly: the tax is real and sits
between 2.2x and 3.6x against jit, within K97's "2-3x" for the nocaps route and
over it for the caps route (the pcrec default). **On both cells the auto route is
slower than the forced VM it would otherwise fall back to** (3.06x and 2.18x,
auto-caps). That is a comparison of two pcrec routes on one pin, not a cross-engine
claim.

**Near-miss at length (16 KiB, one terminating byte).**
evil-alt-nested x t-evil-nearmiss-16k: auto-nocaps 14,532 ns, auto-caps 14,535
(SG L11758-L11759); pcre2 interp/jit, Oniguruma, forced vm and vm-in all `gave up`
5/5 (SG L11765-L11769); vectorscan 10,021 (SG L11757); RE2 1.36-1.50 ms (SG
L11762-L11763). trim-nested-star x t-trim-nearmiss-16k: auto-caps 14,532, auto-nocaps
20,736 (SG L41262-L41263); the same five give up (SG L41267-L41271); RE2 1,342 ns
(but see §5: RE2's `\s` lacks VT).

## 3. (b) The throughput spread vs first-word length (O-87 (c))

O-87 (c) tied the c4c70f2c spread (10.4 us / 45 ns / 1.2 us, quoted, not
re-derived) to the first-run length of letters: 5 / 0 / 3 for `t-64k` / `t-256k` /
`t-1m`. Now, evil-alt-nested (ns per call):

| testee | t-64k (5) | t-256k (0) | t-1m (3) | max/min |
|---|---|---|---|---|
| vm (forced) | 10,639 (SG L11736) | 45.2 (SG L11715) | 1,155.6 (SG L11705) | 235.6x |
| vm-in | 10,557 (SG L11735) | 47.8 | 1,187.0 | 220x |
| auto-caps | 16.8 (SG L11728) | 10.8 (SG L11713) | 15.3 (SG L11698) | 1.55x |
| auto-nocaps | 12.4 (SG L11727) | 4.8 (SG L11712) | 10.5 (SG L11697) | 2.61x |
| pcre2-jit | 1,678.6 (SG L11734) | 50.9 | 227.0 | 33.0x |
| pcre2-interp | 18,811 (SG L11738) | 135.7 | 2,196.7 | 138.6x |
| Oniguruma | 15,402 | 305.7 | 1,904.2 | 50x |
| pcre2-dfa | 958 | 111 | 510 | 8.6x |
| rust | 31.9 | 25.3 | 27.4 | 1.26x |

(ratios computed). **The forced VM reproduces O-87's c4c70f2c figures to three
digits (10.6 us / 45.2 ns / 1.16 us) — [NULLABLE-ANCH] did not touch it. The fix
lives on the auto routes: the spread falls from ~235x to 1.55x (caps) and 2.61x
(nocaps).** The residual 1.5-2.6x on auto is a first-word effect of 4-6 ns.
trim-nested-star is flat everywhere, as O-87 predicted: max/min 1.04 (auto-caps),
1.02 (auto-nocaps), 1.00 (vm, jit), 1.01 (interp) (SG L41110-L41150, computed).

## 4. (c) The 0.1-era line "give-ups gone, cell still unjudged: no expectation"

It was written for 0.1 records and it was exact there: two evil-alt-nested short
triples (rd-evil-alt-near-miss, sd-empty-alt-hit) had no expectation, so every
engine's set cell reduced to 73/75 = 0.9733 and was excluded (O-87 (b)).

**In 0.2 the cell IS judged, so the line no longer applies.** The two triples now
carry `structural-alphabet` expectations (O-89: 4 rows by that method). Reading the
set grain:
- pcrec `auto-caps` and `auto-nocaps` rank at 75/75 (S L940 auto-caps 1,383.7 ns;
  S L6847 auto-nocaps 849.1 ns), as do RE2, tre, rust, vectorscan, pcre2-dfa.
- pcre2 interp/jit, Oniguruma and forced vm/vm-in are excluded at 0.9733 with
  `n_gave_up = 10` (two subjects x 5 trials) (S L10683-L10691). The number 0.9733
  is the same as the 0.1 one, but the CAUSE is now each engine's own give-up, not
  a missing expectation. pcrec's give-ups on the cell: 0 on both auto routes
  (records: outcomes list), 10 on the two forced-VM routes.
- The quantity that WAS "no expectation" in 0.2 is the other pair, email-nested-plus
  x {t-evil-match-60k, t-evil-nearmiss-16k}: 22 rows of `did-not-match-as-expected`
  with the diagnostic "no expectation exists for this (pattern, subject, regime)"
  (records: 11 testees x 2). pcre2 interp and dfa show `gave-up` / `timed-out`
  on them instead (they never reach the judge). The email-nested-plus throughput
  cell is therefore absent from every ranking (the md has its short section only,
  MD L1101).

## 5. (d) NOTES.md P11-P16 and R9-R11

| id | verdict | evidence |
|---|---|---|
| **P11** matching tax | **PARTLY CONFIRMED** | Every backtracker matches the two 60 KiB cells on the first greedy path (jit 24.4 / 27.6 us, SG L11742, L41244; interp 55.9 / 37.2 us). "Within 3x of pcre2-jit": nocaps yes (2.23x, 2.65x), **caps no** (3.32x, 3.63x), §2. "No engine gives up": **refuted for one engine** — pcre2-dfa `timed-out` 5/5 on both target cells (the 60 s alarm; records, SG L11754, L41254), and it is the DFA's n^2.8 (NOTES: 14 s at n=4000). RE2 is `did-not-match` on trim-nested-star x t-trim-match-60k (SG L41255-L41256): the subject holds 610 VT bytes (records, bench/capability/throughput/t-trim-match-60k.bin), RE2's `\s` excludes VT. A semantics difference, not a pcrec concern. |
| **P12** near-miss split | **CONFIRMED except the DFA clause** | interp and jit give up on both near-misses (SG L11765-L11766, L41267-L41268); re2, vectorscan and pcrec answer `nomatch` (§2). **pcre2-dfa does NOT answer nomatch: it `timed-out` 5/5 (SG L11764, L41266; records)**. Both ReDoS triples are judged (a give-up is `gave up`, not wrong). Only email-nested-plus x the two evil subjects lacks an expectation (§4). |
| **P13** design-quadratic (`\s+$` x t-trim-nearmiss-16k) | **HALF CONFIRMED** | interp 1.752 s (SG L38691; the oracle's 1.83 s predicted), Oniguruma 1.252 s (SG L38690), pcre2-dfa 2.596 s (SG L38692). **pcre2-jit is 46.8 us (SG L38686), not seconds**: the "seconds, not microseconds" clause fails for jit. The ">= 100x any linear engine" clause holds for jit (RE2 95.1 ns SG L38680 = 492x; rust 24.3 ns = 1,925x; vs-nosom 107.4 ns = 436x; computed) and for interp (7 orders). pcrec auto 29.1 us (SG L38683-L38684); forced vm 99.6 ms (SG L38688). |
| **P14** end-anchored tails | **CONFIRMED (agreement); spread is §6** | All five tail patterns x three tails: pcrec, jit, interp, Oniguruma, rust, RE2 default and vectorscan all judged and passing on the 15 cells with ONE exception family, tre (`tail-dotstar-txt` x t-tail-txt-1m wrong-span; `tail-word-eoz` x t-tail-digits-1m / t-tail-txt-1m excluded as `did-not-match-as-expected`, SG L39922, L39952, L36082; records). The spread is the end-anchored story (§6). |
| **P15** hex8 | **CONFIRMED (counts)** | Expectations 131 on t-mixed-runs-4k, 264/263/263 on the three tails, 0 on the other seven (bench/capability/expectations.tsv). Every hex8 row is `matched-as-expected` on all 14 testees (records: no hex8 entry among the non-matched outcomes). The "costs nothing on pure letters" clause is not scored (not a falsifiable number): pcrec auto is 1.96 ns/B on t-evil-match-60k, 3.53 on t-mixed-runs-4k (SG L16392, L16417; computed). |
| **P16** bounded end-anchor | **CONFIRMED** | `letters-bounded-tail-z`: interp 1.349 s (SG L21469), jit 196 ms (SG L21467), dfa 1.279 s (SG L21468) on t-evil-match-60k; per-byte pure-letter vs the mixed 4 KiB subject: interp 199x, jit 348x, dfa 246x (computed; threshold >= 50x). **pcrec auto is 1.29 us flat (SG L21464)** and rust 5.7 us: pcrec's per-byte ratio is 0.1x (does not scale with the run). |
| **R9** | applied | one pin, 0.2 cells only; no cross-version delta in the report (S `delta_verdict` column empty but for the header). |
| **R10** | applied | the near-miss cells and `\s+$` x t-trim-nearmiss-16k are reported as cell findings (§2, P13), no engine called an outlier. |
| **R11** | **substance confirmed, "stated on the report" NOT met** | the dropped triples are 2 (email-nested-plus x two evil subjects), 22 rows over 11 testees (§4). The report prints no count of them: the figure is only in per-row diagnostics in the records. A reporter gap, candidate for a KB entry. |

**The predicted pcre2 cells over 1 s**, scored (SG line, per call):
- `\s+$` x t-trim-nearmiss-16k: interp 1.75 s (L38691) **yes**; jit 46.8 us **no**.
- datefinder x each `t-tail-*-1m` (predicted 6.8 s): interp 3.89 s on all three (SG L50425, L50453, L50439) **yes (>1 s, lower than 6.8 s)**; Oniguruma 1.66 s; jit 0.20 s **no**; RE2 default 0.53-0.55 s; pcre2-dfa, RE2 longest and vs-som excluded (wrong span counts, longest/leftmost semantics).
- tail-ext-lower-txt x t-evil-match-60k (1.7 s): interp 1.74 s (L37295) yes; jit 36 us.
- letters-bounded-tail-z x t-evil-match-60k (1.2 s): interp 1.35 s (L21469) yes; jit 0.196 s.
- waf-942360 x t-trim-match-60k (1.7 s): interp 1.73 s (L75582) yes; **jit 1.12 s (L75581) also over 1 s**; Oniguruma and forced vm/vm-in give up (L75583-L75585).
- **Not predicted, over 1 s**: pcre2-dfa 18.5 s and Oniguruma 9.8 s on tail-ext-lower-txt x t-evil-match-60k (L37297, L37296); pcre2-dfa 1.29-1.31 s on `tail-word-eoz` / `tail-ext-lower-txt` x t-evil-nearmiss-16k (L39890, L37312), Oniguruma 1.33 s (L39891). 23 rank rows exceed 1 s per call in total (computed over SG).

Two semantic differences that look like wrong answers and are not (for the reader of
the 88 `did-not-match` rows): RE2/rust on `\d+$` x `t-1m` (`did-not-match`, records):
`t-1m` ends `...[20\n`, PCRE2's `$` matches before a final newline, RE2/rust's does
not. RE2 on `\s+$`, `trim-nested-star`, datefinder x t-trim-*: VT bytes (above).
Neither is a pcrec matter; per the upstream pipeline's standing rule they are
design properties, not filings.

## 6. (e) The end-anchored tail family — pcrec vs the engines that anchor at the end

Every pcrec tail cell scales with the subject, not with the tail. pcrec `auto-caps`,
ns per call (SG) and ns/B (computed):

| pattern | t-tail-digits-1m | t-tail-txt-1m | t-tail-space-1m | ns/B | route stamp (MD) |
|---|---|---|---|---|---|
| tail-digits-eol `\d+$` | 737,204 (L34753) | 736,695 (L34784) | 734,780 (L34768) | 0.70 | dfa, scan=unanchored, prefilter=byte-class-bounded, edge=range, start=reverse-pass (L24231) |
| tail-word-eoz `\w+\z` | 2,252,451 (L39915) | 2,250,659 (L39944) | 2,210,646 (L39929) | 2.15 | same, edge=bitmap (L24239) |
| tail-space-eol `\s+$` | 1,776,397 (L38624) | 1,776,333 (L38654) | 1,776,192 (L38639) | 1.69 | same, edge=bitmap (L24237) |
| tail-ext-lower-txt | 2,851,861 (L37334) | 2,843,731 (L37364) | 2,851,656 (L37350) | 2.72 | dfa, prefilter=byte-class-bounded, edge=none (L24235) |
| tail-dotstar-txt `.*\.txt$` | 209,510 (L36043) | 210,015 (L36074) | 209,706 (L36058) | 0.20 | dfa, prefilter=memchr-bounded, edge=none (L24233) |

All five are `engine=dfa, sel=selected, match=unwrapped`, `start=reverse-pass`. The
only prefilter that restricts the scan to a SUBSET of the megabyte is
`tail-dotstar-txt`'s `memchr-bounded` (0.20 ns/B). No stamp in the set names an
end-anchored (suffix) start. Forced vm (`sel=forced`, `vm_prefilter=none`) is 1.2-7.0
ms for `tail-digits/word/space/ext` (e.g. SG L34757, L39918) and 173 ms for
`tail-dotstar-txt` (SG L36051).

Reference engines on the same 15 cells (SG, same rows as above): RE2 default 94-255
ns, rust 22-221 ns, vectorscan nosom 34-146 ns, i.e. engines whose cost does not
depend on the 1 MiB body. **Ratios pcrec auto-caps / reference (computed, 15 cells):**
vs RE2 default 824x-30,001x (min tail-dotstar-txt x txt; max tail-ext-lower-txt x
digits); vs rust 952x-127,710x; vs vectorscan nosom 1,855x-65,084x. The brief's
"7,000-25,000x" sits inside the four non-memchr patterns' RE2 range (3,146x-30,001x)
but is not the whole range; the full per-cell figures are in the table in the
report's `.subject-grain.tsv` and above.
RE2/Rust's number being tail-bound is consistent with an end-anchored reverse
search (RE2's `anchor_end`); that attribution is inference from the shape, not
a stamp. The same mechanism explains RE2 at 95 ns on `\s+$` x t-trim-nearmiss-16k
(SG L38680): the final `x` fails the reverse pass at once.

**Against the JIT the picture is parity, not deficit:** pcrec auto / pcre2-jit =
0.79-0.80 (`\d+$`), 1.05-1.07 (`\w+\z`), 0.91-0.95 (`\s+$`), 1.11-1.12
(ext-lower), 0.17-0.20 (`.*\.txt$`: pcrec 5-6x FASTER) (computed from SG L34753-L36082).
pcrec is within ~20% of the JIT on four of five (faster on `\d+$`, slower by
7-12% on `\w+\z` and ext-lower) and 5-6x ahead on the fifth. The gap is to
the engines that start at the end. Filed item: pcrec [OPT-REVEND] (I-136). Where the
bound exists, pcrec is already flat: `letters-bounded-tail-z` x t-evil-match-60k is 1.29 us
(SG L21464) against rust 5.7 us.

## 7. (f) pcrec-vm-in's attempt history and the spread record

From the window log (EDT):
1. **Attempt 1, rc=3.** `-- cell capability x pcrec-vm-in 2026-10-08T14:49:08`:
   "the box is not quiet: occupancy: busiest non-target core 79.60% busy (limit
   10.00%)" (W L1088-L1092). Pre-flight refused, nothing written. The log does not
   say what held that core (not determined here).
2. **Attempt 2, rc=4.** Pre-flight passed; the cell ran ~1 h and was written as
   `capability@0.2__pcrec_255bcdd8_vm-in-caps-simdna__budu-ryzen1600__20261008T184948Z`,
   status **inconclusive-spread**, "disagree (1 of 138 groups; worst trim-nested-star /
   short-subject-search / plain d=56 of n=75; 7 unjudged)" (W L1446-L1450). The window
   script re-measured once, as designed.
3. **Attempt 3, rc=0.** `..._20261008T195106Z`, **measured**, "agree (0 of 138 groups;
   7 of 5927 rows; 7 unjudged)" (W L1807; S L10 `record` row for vm-in). Its
   `after:` sample failed (load1 2.93), recorded as provenance (S, interpretation
   R-STATUS-10); under v1.4 only the pre-flight and trial agreement decide.

**The first record is kept in the store, excluded from the report.** It is
indexed as `inconclusive-spread` (store/index.tsv; at the window end the index read
measured 347, inconclusive-load 9, inconclusive-spread 6, W L4813) and is
surfaced by the interpretation sidecar (R-STATUS-2, "NOT in this report's
population"). The report's `superseded: 1` (S L1) is that record.

**What the spread was (records, not a report).** In the first record the sum over
trim-nested-star's 75 short subjects is steady (10.355-10.368 ms across the 5 trials,
dominated by `rd-trim-near-miss` at 10.35 ms), tighter than the kept record's
(10.329-10.495 ms). The disagreement is per row: on 66 of 75 subjects trial 3 and on 41
trial 4 ran >1.5x the row's median (e.g. `v-email` 33.0 vs 20.3 ns) — a mid-run
disturbance on those two trials of one pattern. So the rule worked on a real
event the summed cell would never show. The kept record has 7 disagreeing rows of 5927
but 0 disagreeing groups (S L10), which is what `measured` requires.

## 8. (g) Ranked candidate list for pcrec, and the asks

Ranked by size of measured gap x frequency of the real-world shape. All are
this pin's facts, not pcrec diagnoses.

1. **[OPT-REVEND] — the end-anchored tail family.** 15 cells, 0.20-2.72 ns/B flat,
   824x-127,710x behind RE2/rust, parity with the JIT (§6). Acceptance surface, as
   built: tail-digits-eol / tail-word-eoz / tail-space-eol / tail-ext-lower-txt /
   tail-dotstar-txt x the three `t-tail-*-1m` (15), plus `tail-space-eol` x
   t-trim-nearmiss-16k (29.1 us vs RE2 95 ns, 305x, computed) and
   `\d+$` x `t-1m`. The shape needs no new set.
2. **K97's matching tax on the DEFAULT route.** auto-caps is the VM hybrid with an
   `attempt` DFA scan; it is 3.06x / 2.18x slower than the forced VM and 3.32x /
   3.63x slower than the JIT on the two 60 KiB matching cells (§2). The nocaps
   DFA route is 2.23x / 2.65x vs jit. Not a correctness issue.
3. **Forced-VM quadratic cells** (no relief by construction): vm gives up 5/5 on both
   16 KiB near-misses and on waf-942360 x t-trim-match-60k; `rd-trim-near-miss` is
   10.2 ms vs auto 36.5 ns (SG L40878, L40869); `\s+$` x t-trim-nearmiss-16k 99.6 ms vs
   auto 29.1 us (SG L38688, L38684). Observation only; the auto route is the product.
4. **caps tax at the floor:** ~10.5 ns vs ~5.0 ns on flat cells (trim-nested-star
   t-1m, SG L41110 vs L41109): caps adds ~5.3 ns per call on every cell.
5. **Positives worth keeping** (so a later change can be read against them):
   `tail-dotstar-txt` 5-6x faster than the JIT (`memchr-bounded`);
   `letters-bounded-tail-z` flat at 1.1-1.3 us from 4 KiB to 1 MiB; both auto routes
   give up 0 times on every ReDoS cell in the set.
6. Refusal, unchanged from 0.1: datefinder on the caps routes at 589,177 B (> 500,000).

**Asks (also drafted as O-91 below):** (1) which denominator K97's "2-3x" uses;
(2) the predicted cell values for [OPT-REVEND] before its window; (3) whether the
caps default's VM-hybrid route on the evil/trim shapes is meant to be slower than
the forced VM on matching subjects; (4) which cell the ~22 ns figure was.

## 9. What was NOT read

- No cross-pin form (one pin at 0.2). No 0.1 -> 0.2 delta. O-87's c4c70f2c figures
  quoted, not re-derived.
- `Compile cost` sections (sizes, compile phases) not analysed beyond the route
  stamps; no compile-time read in this lane.
- The `.matrix.tsv`; the `Standing cross-class query` (154 R-STATUS-15 firings)
  beyond noting it.
- The other 8 patterns' cells beyond those cited; tre's 58 `did-not-match` rows
  (email-nested-plus, tail-digits-eol, tail-word-eoz) not diagnosed.
- Why core 79.6% busy at attempt 1 (log silent).
- RE2's `anchor_end` and the VT/`$` explanations are source-level inferences backed
  by the record bytes (VT count, the `t-1m` tail) but not by a probe of the engines.
