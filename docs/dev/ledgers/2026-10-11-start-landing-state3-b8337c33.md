# [START-LANDING] state 3 ledger -- 7388f1c0 (abi 73, control) vs b8337c33 (abi 74)

Lane `b135read3`, plan row [B135] step (e) (the state-3 READ). Window: `/var/tmp/b135win3/chain.log`,
`CHAIN_START 2026-10-10T20:21:17 EDT` to `CHAIN_DONE suite_rc=0 2026-10-11T13:03:26 EDT` (master 4cad239f;
chain `docs/dev/lanes/b135s3_chain.sh`). 11 suite sets, every cell `measured`; two quiet-gate refusals (`rc=3`, five seconds into the cell: `sentinel` x `pcre2-jit` at 20:45:50 EDT and
`bounded` x `pcrec-nocaps` at 10:46:19 EDT), both measured on attempt 2 (finishing 20:55:34 and 11:36:41). ~/pcrec was not touched; nothing was timed by this lane. Sources, all archived under
`docs/dev/measurements/` with source headers (`2026-10-11-b135-state3-*.txt`, one per analysis mode; the script is
`2026-10-11-b135-state3-analysis.py`, read-only over the records, arithmetic = `pcrecbench.reduce`):

- reports `reports/2026-10-11-{capability-0.2,loglines-0.1,email-specimen-0.2,litrun-0.1,utf8-0.1,syntax-0.1,bounded-0.3}-budu-ryzen1600-landing-b8337c33.*`
  (reporter v25; query = the four pcrec testees 7388f1c0/b8337c33 x caps/nocaps, `since=2026-10-11T00:00:00Z`, so
  the 7388f1c0 side is THIS window's control record, never the states 1+2 window's; 35 files + 7 sidecars,
  `regen_reports.py` 7 groups 0 failures);
- the cross-window pair uses the records directly (the reporter dedups to the newest record per testee id).

Numbers are medians over 5 trials; "(min-max)" is the trial range; ratios are computed from medians. "ov" = the two
trial ranges overlap, "DISJ" = they do not. A "mover" is a cell whose `dfa_start` stamp flipped
`reverse-pass -> end-minus-width | landing` between the two pcrec testees; "identical" = every other cell (the null).

## 0. Cautions, stated once

1. **The reporter's D119 bar and this ledger's overlap test are different cuts.** The reporter calls a cross-pin cell
   moved iff |delta%| > max(IQR%, null band) with the null band the largest |delta%| any program-identical cell of the same
   (regime, scale) stratum reached. In capability's `short-subject-search` `>=1us` stratum that band is +-24.69%
   (set by one noisy program-identical cell, `phone-palindrome-6` nocaps 0.753, trial range 3,165-4,320), so the reporter
   reads capability's 16 mover cells (its caps-vs-caps view) as "1 improve, 15 within the bar" while the overlap test reads the same 16 caps cells
   as 8 better / 1 worse / 7 overlap. Both are printed; the verdicts below say which one is meant.
2. **START-LANDING touches the search regime only.** The whole-subject (`match-compliance`) form is the `(?:...)\z` rev-end
   artifact and moves nothing (278 whole-subject cells measured, all program-identical to 7388f1c0).
3. **Window 1 vs window 3 of 7388f1c0.** The trend report's 7388f1c0 snapshot is window 1's records (immutable);
   its b8337c33-vs-7388f1c0 deltas therefore cross windows. Section 2 prices that.
4. The utf8 mover count is 56 patterns here (29 end-minus-width + 27 landing) against the census's 57:
   `ci-ucp-invariance` is in the census (compiled) but unsupported-by-declaration on `pcrec-*-utf8`, so no record exists.
   The other predicted populations are exact (below).

## 1. Sentinels -- did the box and instrument hold?

`sentinel@0.1`, 15 patterns x 75 short subjects, set-grain sums. Window 3: open 00:22-00:46Z (20:22-20:46 EDT), end
07:01-07:27Z (03:01-03:27 EDT), end2 16:28-16:52Z (12:28-12:52 EDT); `2026-10-11-b135-state3-sentinel.txt`. Ratios over the 15 cells
(min / median / max; DISJ = disjoint trial ranges):

| testee | end/open | DISJ | end2/open | DISJ | end2/end | DISJ |
|---|---|---|---|---|---|---|
| pcrec 7388f1c0 caps | 0.990 / 1.000 / 1.008 | 1 | 0.989 / 1.000 / 1.010 | 1 | 0.992 / 1.000 / 1.013 | 1 |
| pcrec 7388f1c0 nocaps | 0.992 / 1.000 / 1.011 | 0 | 0.982 / 1.000 / 1.011 | 0 | 0.989 / 1.000 / 1.007 | 0 |
| pcrec b8337c33 caps | 0.994 / 1.000 / 1.005 | 1 | 0.995 / 1.000 / 1.007 | 0 | 0.995 / 1.001 / 1.005 | 0 |
| pcrec b8337c33 nocaps | 0.989 / 1.000 / 1.004 | 0 | 0.990 / 0.998 / 1.003 | 1 | 0.986 / 0.999 / 1.002 | 0 |
| pcre2-jit | 0.960 / 1.000 / 1.074 | 0 | 0.941 / 0.998 / 1.074 | 0 | 0.919 / 0.997 / 1.040 | 0 |

- pcrec is flat to <= 1.8% at both pins across 16 h (open -> end2; worst single cell 0.982), 5 disjoint-range exceptions among 180 cell-pairs, all < 1.3%
  (e.g. `file-ext-order` 7388f1c0 caps end/open 0.995). pcre2-jit, the flat control, sits inside its trial agreement
  (every pair overlapping; the loudest are cells of ~3 us set sum with one slow trial: `wild-semdiv-dollar-trailing-newline-pcre2` 1.074).
- Window 3 open vs window 1 (the states 1+2 window) for the SAME 7388f1c0 testee ids: caps 0.987 / 1.000 / 1.011, nocaps
  0.992 / 1.001 / 1.010 (0 disjoint); pcre2-jit 0.938 / 1.002 / 1.022.
- **Verdict: the window is clean by the sentinel's own reading** at open, end and end2, at both pins and across the two windows.
  Worst other-core busy in the seven report headers (provenance, not a gate): capability 13.57%, loglines 11.83%,
  email 23.68%, litrun 23.4%, bounded 25.45%, utf8 27.3%, syntax 50.0% (`anc-caret` large-subject, b8337c33 caps; a
  program-identical non-mover cell).

## 2. CROSS-WINDOW CONTROL -- 7388f1c0 here vs 7388f1c0 in the states 1+2 window

Same testee ids, same cells, two windows 8-26 h apart (2026-10-10 12:13-19:19 EDT vs 2026-10-10 20:21 -> 2026-10-11 13:03 EDT).
B = window 3, A = window 1; set-cell median ratio B/A; `2026-10-11-b135-state3-control.txt`.

| set | cfg | cells | min | p5 | p25 | median | p75 | p95 | max | DISJ | outside +-5% |
|---|---|---|---|---|---|---|---|---|---|---|---|
| capability | caps | 137 | 0.851 | 0.995 | 1.000 | 1.000 | 1.003 | 1.011 | 1.158 | 7 | 2 |
| capability | nocaps | 139 | 0.910 | 0.989 | 0.999 | 1.000 | 1.001 | 1.007 | 1.118 | 4 | 2 |
| loglines | caps | 22 | 0.995 | 0.995 | 0.999 | 1.000 | 1.001 | 1.006 | 1.006 | 0 | 0 |
| loglines | nocaps | 22 | 0.992 | 0.998 | 0.999 | 1.000 | 1.001 | 1.003 | 1.004 | 0 | 0 |
| email-specimen | caps | 9 | 0.999 | 0.999 | 1.000 | 1.000 | 1.000 | 1.001 | 1.001 | 0 | 0 |
| email-specimen | nocaps | 9 | 0.998 | 0.999 | 1.000 | 1.000 | 1.001 | 1.001 | 1.002 | 0 | 0 |
| litrun | caps | 42 | 0.994 | 0.998 | 0.999 | 1.000 | 1.001 | 1.005 | 1.006 | 1 | 0 |
| litrun | nocaps | 42 | 0.981 | 0.996 | 0.999 | 1.000 | 1.001 | 1.005 | 1.008 | 4 | 0 |
| ALL | | 422 | 0.851 | 0.995 | 0.999 | 1.000 | 1.001 | 1.007 | 1.158 | 16 | 4 |

By regime: `large-subject-throughput` p5-p95 0.997-1.010, `short-subject-search` 0.992-1.006, `match-compliance` whole-subject 0.997-1.006.
By baseline scale: `<100ns` 0.999-1.023 (14 cells), `100ns-1us` 0.992-1.006 (156), `>=1us` 0.995-1.007 (252).

**Reading.** The window-to-window drift of the same program is +-0.7% (p5-p95) across 422 cells; every effect smaller than
that in the three-state comparison is not an engine effect. The tails are four cells, all in capability (the fourth, `phone-palindrome-6` throughput 0.910, has overlapping trial ranges): `wild-logparse-quotedstring-grok`
caps short 0.851 (2,525.2 -> 2,149.0: window 1's slow reading did NOT repeat, section 5.2), `bracket-array-define` caps
throughput 1.158 (285.9 -> 331.0; window 3's trial range is 285.7-335.7, i.e. a mixed-state record whose median sits in the slow
state, ranges overlap) and `phone-palindrome-6` nocaps short 1.118 (trial ranges 3,170-4,320 and 3,165-3,888, the set's
loudest cell; it also sets the capability short-`>=1us` D119 band). Everything else is inside +-5%.

## 3. Cross-pin reports and the three-state view

### 3.1 The reports

`reports/2026-10-11-<set>-<ver>-budu-ryzen1600-landing-b8337c33.{tsv,md,matrix.tsv,subject-grain.tsv,subject-grain.md,interpretation.md}`
for capability@0.2, loglines@0.1, email-specimen@0.2, litrun@0.1, utf8@0.1, syntax@0.1, bounded@0.3 (altwide@0.3 and sentinel
were measured at b8337c33 only; the 4 records per group are all `measured`, 0 superseded). The reporter's own D119 populations
(caps + nocaps pooled, per group):

| set | cross-pin cells | improve | regress | within bar | null-control |
|---|---|---|---|---|---|
| capability | 137 | 1 | 0 | 15 | 121 |
| loglines | 22 | 4 | 0 | 2 | 16 |
| email-specimen | 9 | 2 | 0 | 0 | 7 |
| litrun | 42 | 22 | 2 | 0 | 18 |
| utf8 | 138 | 70 | 14 | 28 | 26 |
| syntax | 243 | 74 | 0 | 24 | 145 |
| bounded | 126 | 28 | 0 | 6 | 92 |

The two litrun "regress" are `floor` short (245.1 -> 247.0 ns, +0.77%, IQR-only bar 0.05%) and `wild-secrets-github-pat` throughput
(29,810.6 -> 29,849.2, +0.13%): both below the +-0.7% window drift of section 2. The reporter versions in force are unchanged (v25); R8 pairs by pin
order (KB-37), so the nocaps delta column is not inverted.

### 3.2 The three-state view, tier-1 sets (auto-caps)

a15fb77b (window 1) -> 7388f1c0 (window 1) -> 7388f1c0 (window 3, the control) -> b8337c33 (window 3). Rows shown: the cells where a program
moved at b8337c33 or any step moved > 3% (the unlisted remainder is flat to 3% at all three steps). `S` = short-subject-search,
`T` = large-subject-throughput, `M` = whole-subject match. Medians in ns; the last three columns are ratios of consecutive states.
The first ratio (REVEND, same window) is the states 1+2 result; the second is the cross-window control; the third is START-LANDING.
`2026-10-11-b135-state3-threestate.txt` carries nocaps and the two-decimal rows.

#### capability (auto-caps)
| pattern | reg | dfa_start@b8337c33 | a15fb77b w1 | 7388f1c0 w1 | 7388f1c0 w3 (control) | b8337c33 w3 | 7388w1/a15 | 7388w3/7388w1 | b8337/7388w3 |
|---|---|---|---|---|---|---|---|---|---|
| `bracket-array-define` | T | None | 286.9 | 285.9 | 331.0 | 294.8 | 0.996 | 1.158 | 0.890 |
| `floor-byte` | T | end-minus-width | 78,578 | 78,633 | 78,617 | 78,606 | 1.001 | 1.000 | 1.000 |
| `floor-byte` | S | end-minus-width | 682.0 | 682.2 | 683.0 | 681.8 | 1.000 | 1.001 | 0.998 |
| `hex8-bounded` | T | end-minus-width | 15,430,124 | 15,432,982 | 15,438,453 | 15,094,255 | 1.000 | 1.000 | 0.978 |
| `hex8-bounded` | S | end-minus-width | 2,184 | 2,173 | 2,182 | 2,094 | 0.995 | 1.004 | 0.960 |
| `letters-bounded-tail-z` | T | reverse-pass | 10,289 | 779.4 | 782.2 | 783.8 | 0.076 | 1.004 | 1.002 |
| `letters-bounded-tail-z` | S | reverse-pass | 2,346 | 951.5 | 953.1 | 951.0 | 0.406 | 1.002 | 0.998 |
| `nested-comment-rec` | S | None | 1,507 | 1,484 | 1,543 | 1,521 | 0.985 | 1.040 | 0.986 |
| `phone-palindrome-6` | T | None | 8,491,808 | 8,522,314 | 8,794,206 | 8,494,735 | 1.004 | 1.032 | 0.966 |
| `tail-digits-eol` | T | reverse-pass | 3,740,915 | 138.4 | 135.3 | 136.4 | 0.000 | 0.978 | 1.008 |
| `tail-digits-eol` | S | reverse-pass | 1,641 | 711.0 | 710.9 | 712.7 | 0.433 | 1.000 | 1.003 |
| `tail-dotstar-txt` | T | reverse-pass | 857,681 | 146.0 | 145.3 | 145.3 | 0.000 | 0.995 | 1.000 |
| `tail-dotstar-txt` | S | reverse-pass | 644.2 | 738.1 | 739.5 | 736.4 | 1.146 | 1.002 | 0.996 |
| `tail-ext-lower-txt` | T | reverse-pass | 8,906,621 | 124.7 | 125.5 | 125.1 | 0.000 | 1.007 | 0.997 |
| `tail-ext-lower-txt` | S | reverse-pass | 681.3 | 646.1 | 634.2 | 637.8 | 0.948 | 0.982 | 1.006 |
| `tail-space-eol` | T | reverse-pass | 7,864,626 | 21,977 | 21,974 | 21,984 | 0.003 | 1.000 | 1.000 |
| `tail-space-eol` | S | reverse-pass | 1,367 | 678.6 | 680.0 | 678.2 | 0.496 | 1.002 | 0.997 |
| `tail-word-eoz` | T | reverse-pass | 9,811,057 | 21,908 | 21,904 | 21,905 | 0.002 | 1.000 | 1.000 |
| `tail-word-eoz` | S | reverse-pass | 2,733 | 1,013 | 1,024 | 1,017 | 0.371 | 1.011 | 0.994 |
| `utf8-lead-no-cont` | T | end-minus-width | 1,660,331 | 1,660,129 | 1,660,262 | 1,660,680 | 1.000 | 1.000 | 1.000 |
| `utf8-lead-no-cont` | S | end-minus-width | 1,255 | 1,255 | 1,254 | 1,245 | 1.000 | 1.000 | 0.993 |
| `wild-codegrammar-json-array-begin` | T | end-minus-width | 273,262 | 273,467 | 273,362 | 267,956 | 1.001 | 1.000 | 0.980 |
| `wild-codegrammar-json-array-begin` | S | end-minus-width | 699.6 | 698.6 | 699.2 | 688.8 | 0.999 | 1.001 | 0.985 |
| `wild-codegrammar-json-object-begin` | T | end-minus-width | 78,612 | 78,588 | 78,637 | 78,650 | 1.000 | 1.001 | 1.000 |
| `wild-codegrammar-json-object-begin` | S | end-minus-width | 682.1 | 682.3 | 682.0 | 680.3 | 1.000 | 1.000 | 0.997 |
| `wild-logparse-quotedstring-grok` | S | reverse-pass | 2,123 | 2,525 | 2,149 | 2,147 | 1.190 | 0.851 | 0.999 |
| `wild-secrets-aws-access-key-id` | T | end-minus-width | 159,059 | 159,148 | 159,110 | 158,501 | 1.001 | 1.000 | 0.996 |
| `wild-secrets-aws-access-key-id` | S | end-minus-width | 1,411 | 1,409 | 1,414 | 1,362 | 0.998 | 1.004 | 0.963 |
| `wild-secrets-github-pat` | T | end-minus-width | 180,242 | 180,296 | 180,419 | 180,375 | 1.000 | 1.001 | 1.000 |
| `wild-secrets-github-pat` | S | end-minus-width | 1,002 | 1,004 | 1,007 | 845.9 | 1.002 | 1.003 | 0.840 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | T | reverse-pass | 139.3 | 103.6 | 105.0 | 104.4 | 0.744 | 1.013 | 0.995 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | S | reverse-pass | 956.3 | 646.4 | 644.9 | 648.6 | 0.676 | 0.998 | 1.006 |
| `wild-validator-uuid-grok` | T | end-minus-width | 138,058 | 138,367 | 138,395 | 139,339 | 1.002 | 1.000 | 1.007 |
| `wild-validator-uuid-grok` | S | end-minus-width | 710.5 | 708.4 | 710.6 | 647.3 | 0.997 | 1.003 | 0.911 |
| `wild-waf-crs-942360-concat-sqli` | T | attempt-start | 36,496,744 | 36,620,518 | 37,831,747 | 36,466,915 | 1.003 | 1.033 | 0.964 |
| `winpath-near-miss` | T | attempt-start | 65.9 | 63.8 | 65.7 | 64.4 | 0.968 | 1.029 | 0.981 |

#### loglines (auto-caps)
| pattern | reg | dfa_start@b8337c33 | a15fb77b w1 | 7388f1c0 w1 | 7388f1c0 w3 (control) | b8337c33 w3 | 7388w1/a15 | 7388w3/7388w1 | b8337/7388w3 |
|---|---|---|---|---|---|---|---|---|---|
| `floor` | T | end-minus-width | 2,961,175 | 2,963,806 | 2,958,636 | 2,842,707 | 1.001 | 0.998 | 0.961 |
| `floor` | S | end-minus-width | 2,040 | 2,039 | 2,051 | 1,512 | 0.999 | 1.006 | 0.737 |
| `hex32-id` | T | end-minus-width | 11,312,531 | 11,334,337 | 11,297,511 | 11,052,363 | 1.002 | 0.997 | 0.978 |
| `hex32-id` | S | end-minus-width | 307,731 | 307,038 | 307,925 | 297,969 | 0.998 | 1.003 | 0.968 |
| `uuid` | T | end-minus-width | 1,080,447 | 1,080,632 | 1,081,039 | 1,060,908 | 1.000 | 1.000 | 0.981 |
| `uuid` | S | end-minus-width | 21,009 | 21,006 | 21,028 | 20,372 | 1.000 | 1.001 | 0.969 |

#### email-specimen (auto-caps)
| pattern | reg | dfa_start@b8337c33 | a15fb77b w1 | 7388f1c0 w1 | 7388f1c0 w3 (control) | b8337c33 w3 | 7388w1/a15 | 7388w3/7388w1 | b8337/7388w3 |
|---|---|---|---|---|---|---|---|---|---|
| `floor` | T | end-minus-width | 698,801 | 698,916 | 698,908 | 659,860 | 1.000 | 1.000 | 0.944 |
| `floor` | S | end-minus-width | 1,327 | 1,326 | 1,326 | 986.1 | 0.999 | 1.000 | 0.744 |

#### litrun (auto-caps)
| pattern | reg | dfa_start@b8337c33 | a15fb77b w1 | 7388f1c0 w1 | 7388f1c0 w3 (control) | b8337c33 w3 | 7388w1/a15 | 7388w3/7388w1 | b8337/7388w3 |
|---|---|---|---|---|---|---|---|---|---|
| `alt-foo-tails` (whole) | M | reverse-pass | 280.9 | 302.7 | 303.3 | 303.1 | 1.077 | 1.002 | 0.999 |
| `ctrl-abc-dollar` | T | reverse-pass | 390.3 | 257.9 | 259.3 | 256.4 | 0.661 | 1.006 | 0.989 |
| `ctrl-abc-dollar` | S | reverse-pass | 401.1 | 253.4 | 253.0 | 254.2 | 0.632 | 0.998 | 1.005 |
| `floor` | T | end-minus-width | 3,138,078 | 3,139,032 | 3,138,657 | 2,945,623 | 1.000 | 1.000 | 0.938 |
| `floor` | S | end-minus-width | 245.0 | 245.2 | 245.1 | 247.0 | 1.001 | 1.000 | 1.008 |
| `lit-l10` | T | end-minus-width | 1,092,312 | 1,091,846 | 1,093,912 | 760,974 | 1.000 | 1.002 | 0.696 |
| `lit-l10` | S | end-minus-width | 449.8 | 450.6 | 450.8 | 317.4 | 1.002 | 1.001 | 0.704 |
| `lit-l16` | T | end-minus-width | 1,012,748 | 1,011,996 | 1,012,192 | 734,727 | 0.999 | 1.000 | 0.726 |
| `lit-l16` | S | end-minus-width | 562.6 | 562.1 | 562.9 | 368.9 | 0.999 | 1.001 | 0.655 |
| `lit-l2` | T | end-minus-width | 3,379,600 | 3,372,296 | 3,372,349 | 3,061,991 | 0.998 | 1.000 | 0.908 |
| `lit-l2` (whole) | M | reverse-pass | 256.0 | 264.3 | 263.7 | 264.3 | 1.032 | 0.998 | 1.002 |
| `lit-l2` | S | end-minus-width | 434.1 | 435.6 | 434.4 | 362.4 | 1.003 | 0.997 | 0.834 |
| `lit-l3` | T | end-minus-width | 3,417,423 | 3,416,660 | 3,415,951 | 3,161,079 | 1.000 | 1.000 | 0.925 |
| `lit-l3` | S | end-minus-width | 501.1 | 501.6 | 501.1 | 385.9 | 1.001 | 0.999 | 0.770 |
| `lit-l31` | T | end-minus-width | 788,457 | 786,755 | 788,067 | 523,008 | 0.998 | 1.002 | 0.664 |
| `lit-l31` | S | end-minus-width | 824.0 | 824.3 | 825.0 | 564.1 | 1.000 | 1.001 | 0.684 |
| `lit-l4` | T | end-minus-width | 3,152,427 | 3,149,566 | 3,152,461 | 2,757,349 | 0.999 | 1.001 | 0.875 |
| `lit-l4` (whole) | M | reverse-pass | 266.0 | 275.0 | 276.3 | 275.9 | 1.034 | 1.005 | 0.999 |
| `lit-l4` | S | end-minus-width | 442.6 | 442.0 | 442.6 | 353.6 | 0.998 | 1.001 | 0.799 |
| `lit-l40` | T | end-minus-width | 463,447 | 463,314 | 463,158 | 346,286 | 1.000 | 1.000 | 0.748 |
| `lit-l40` | S | end-minus-width | 983.1 | 978.2 | 977.3 | 624.0 | 0.995 | 0.999 | 0.638 |
| `lit-l7` | T | end-minus-width | 3,220,739 | 3,217,154 | 3,209,188 | 2,671,767 | 0.999 | 0.998 | 0.833 |
| `lit-l7` | S | end-minus-width | 484.1 | 484.6 | 484.5 | 349.7 | 1.001 | 1.000 | 0.722 |
| `lit-l8` | T | end-minus-width | 2,861,918 | 2,863,225 | 2,863,959 | 2,411,137 | 1.000 | 1.000 | 0.842 |
| `lit-l8` | S | end-minus-width | 477.3 | 478.2 | 477.9 | 347.5 | 1.002 | 0.999 | 0.727 |
| `wild-secrets-aws-access-key-id` | T | end-minus-width | 403,983 | 403,938 | 403,957 | 402,539 | 1.000 | 1.000 | 0.996 |
| `wild-secrets-aws-access-key-id` | S | end-minus-width | 1,010 | 1,010 | 1,009 | 936.1 | 1.001 | 0.999 | 0.927 |
| `wild-secrets-github-pat` | T | end-minus-width | 29,814 | 29,818 | 29,811 | 29,849 | 1.000 | 1.000 | 1.001 |
| `wild-secrets-github-pat` | S | end-minus-width | 1,272 | 1,273 | 1,272 | 951.8 | 1.000 | 0.999 | 0.749 |



Rows omitted from the table above are flat at all three steps.

**Reading the three states together.** (a) REVEND (first ratio) reproduces the states 1+2 read: the tail family
(large-subject cells x0.000-0.003, short cells x0.37-0.95) and `ctrl-abc-dollar` (x0.66 / x0.63) / `wild-semdiv-dollar-trailing-newline-pcre2` (x0.74 / x0.68) fall, `tail-dotstar-txt` short is the one slower tail row (x1.146). (b) The control
column is 1.000 (+-0.7%) on every row except the four named in section 2. (c) START-LANDING (last column) moves
only the rows whose `dfa_start` flipped, and moves them mostly in the SEARCH regime. The litrun whole-subject rows (`alt-foo-tails`
1.077, `lit-l2` 1.032, `lit-l4` 1.034 at the REVEND step, listed above as `M`/`(whole)`) read 0.999-1.004 across the control and START-LANDING steps: the REVEND
price stays put, START-LANDING neither adds to nor removes it (they are rev-end artifacts and cannot move, section 0).

## 4. The START-LANDING verdict

### 4.1 Population: I-145's prediction reproduced, then measured

I-145 predicted 298 of 734 plain-form compiles move, 210 `end-minus-width` + 88 `landing`. Window 3 stamps (the compile row of each
b8337c33 record, 7388f1c0's `reverse-pass` on the other side):

| set | end-minus-width patterns | landing patterns | cells (caps+nocaps, 2 regimes) |
|---|---|---|---|
| capability | 8 | 0 | 32 |
| loglines | 3 | 0 | 12 |
| email-specimen | 1 | 0 | 4 |
| litrun | 12 | 0 | 48 |
| syntax | 42 | 7 | 196 |
| utf8 | 29 | 27 | 224 |
| bounded | 7 | 10 | 68 |
| **measured here** | **102** | **44** | **584** (292 compile rows) |

The other six of the 298 rows are altwide (1 pattern, measured at b8337c33 only), sentinel (1 pattern, covered by section 1) and
`ci-ucp-invariance` (1 pattern, no record on the `-utf8` testees): 292 + 6 = 204 + 6 = 210 end-minus-width (the 6 = altwide 2, sentinel `floor-byte` 2, `ci-ucp-invariance` 2) and 88 landing, **exactly I-145's figures**. In all 584
cells the stamp reads `dfa_start reverse-pass > {end-minus-width | landing}` and nothing else on the row moves except `scan_edges` /
`dfa_uniform_folds` on the rows that lose the reverse machine (`wild-validator-uuid-grok` `scan_edges 8 > 4`, bounded `hex32` `dfa_uniform_folds 2 > 1`,
`scan_edges 2 > 1`) and the four FIT rows (4.4).

### 4.2 Movers vs the null (pooled caps + nocaps; trial-overlap cut; `2026-10-11-b135-state3-movers.txt`)

| class | cells | better (DISJ, B < A) | worse (DISJ, B > A) | overlap | median B/A | p5 | p95 | min | max |
|---|---|---|---|---|---|---|---|---|---|
| end-minus-width | 408 | 311 (76%) | 21 (5%) | 76 | 0.956 | 0.731 | 1.003 | 0.637 | 1.052 |
| landing | 176 | 137 (78%) | 14 (8%) | 25 | 0.839 | 0.671 | 1.027 | 0.517 | 1.060 |
| program-identical (the null) | 852 | 22 (2.6%) | 15 (1.8%) | 815 | 1.000 | 0.990 | 1.008 | 0.753 | 1.063 |

By regime: end-minus-width throughput 204 cells, 143 better / 9 worse, median 0.976; search 204 cells, 168 better / 12 worse,
median 0.925. Landing throughput 88: 76 / 2, median 0.788; search 88: 61 / 12, median 0.886. The null by regime: throughput 283
cells (6 / 5, p5-p95 0.984-1.009), search 291 (10 / 6, 0.989-1.007), whole-subject 278 (6 / 4, 0.996-1.008). Where a cell is "better" the
move is mostly large: the median better mover is x0.93 (end-minus-width) / x0.79 (landing), the median worse one x1.013 / x1.043, against the null's +-1%.

By set (cells, better / worse / overlap, median B/A, min-max):

| set | class | cells | better | worse | overlap | median | min-max |
|---|---|---|---|---|---|---|---|
| capability | end-minus-width | 32 | 15 | 4 | 13 | 0.995 | 0.791-1.007 |
| loglines | end-minus-width | 12 | 11 | 0 | 1 | 0.968 | 0.737-0.983 |
| email-specimen | end-minus-width | 4 | 4 | 0 | 0 | 0.846 | 0.744-0.944 |
| litrun | end-minus-width | 48 | 43 | 2 | 3 | 0.786 | 0.637-1.008 |
| syntax | end-minus-width | 168 | 149 | 4 | 15 | 0.951 | 0.850-1.012 |
| syntax | landing | 28 | 28 | 0 | 0 | 0.790 | 0.703-0.980 |
| utf8 | end-minus-width | 116 | 67 | 10 | 39 | 0.981 | 0.789-1.052 |
| utf8 | landing | 108 | 69 | 14 | 25 | 0.942 | 0.517-1.060 |
| bounded | end-minus-width | 28 | 22 | 1 | 5 | 0.934 | 0.691-1.015 |
| bounded | landing | 40 | 40 | 0 | 0 | 0.743 | 0.586-0.951 |

### 4.3 Every mover pattern, tier-1 sets (the four sets of the three-state view)

Caps medians in ns (7388f1c0 control / b8337c33), `B/A` = b8337c33 / 7388f1c0 (window 3 both). `(ov)` = trial ranges overlap, `(better)` / `(WORSE)` =
disjoint ranges in that direction. Throughput subjects are mostly non-matching text, so the start is rarely recovered there;
the effect lives in `search-short`.

#### capability
| pattern | class | regime | 7388f1c0 caps (ns) | b8337c33 caps (ns) | caps B/A | nocaps B/A |
|---|---|---|---|---|---|---|
| `floor-byte` | end-minus-width | throughput | 78617 | 78606 | 1.000 (ov) | 1.001 (WORSE) |
| `floor-byte` | end-minus-width | search-short | 683.0 | 681.8 | 0.998 (ov) | 0.999 (better) |
| `hex8-bounded` | end-minus-width | throughput | 15438453 | 15094255 | 0.978 (better) | 0.977 (better) |
| `hex8-bounded` | end-minus-width | search-short | 2182 | 2094 | 0.960 (better) | 0.959 (better) |
| `utf8-lead-no-cont` | end-minus-width | throughput | 1660262 | 1660680 | 1.000 (ov) | 1.000 (ov) |
| `utf8-lead-no-cont` | end-minus-width | search-short | 1254 | 1245 | 0.993 (better) | 0.996 (ov) |
| `wild-codegrammar-json-array-begin` | end-minus-width | throughput | 273362 | 267956 | 0.980 (better) | 0.977 (better) |
| `wild-codegrammar-json-array-begin` | end-minus-width | search-short | 699.2 | 688.8 | 0.985 (better) | 0.984 (ov) |
| `wild-codegrammar-json-object-begin` | end-minus-width | throughput | 78637 | 78650 | 1.000 (ov) | 0.999 (ov) |
| `wild-codegrammar-json-object-begin` | end-minus-width | search-short | 682.0 | 680.3 | 0.997 (ov) | 0.995 (better) |
| `wild-secrets-aws-access-key-id` | end-minus-width | throughput | 159110 | 158501 | 0.996 (ov) | 1.006 (WORSE) |
| `wild-secrets-aws-access-key-id` | end-minus-width | search-short | 1414 | 1362 | 0.963 (better) | 0.980 (better) |
| `wild-secrets-github-pat` | end-minus-width | throughput | 180419 | 180375 | 1.000 (ov) | 1.000 (ov) |
| `wild-secrets-github-pat` | end-minus-width | search-short | 1007 | 845.9 | 0.840 (better) | 0.791 (better) |
| `wild-validator-uuid-grok` | end-minus-width | throughput | 138395 | 139339 | 1.007 (WORSE) | 1.006 (WORSE) |
| `wild-validator-uuid-grok` | end-minus-width | search-short | 710.6 | 647.3 | 0.911 (better) | 0.916 (ov) |

#### loglines
| pattern | class | regime | 7388f1c0 caps (ns) | b8337c33 caps (ns) | caps B/A | nocaps B/A |
|---|---|---|---|---|---|---|
| `floor` | end-minus-width | throughput | 2958636 | 2842707 | 0.961 (better) | 0.958 (ov) |
| `floor` | end-minus-width | search-short | 2051 | 1512 | 0.737 (better) | 0.741 (better) |
| `hex32-id` | end-minus-width | throughput | 11297511 | 11052363 | 0.978 (better) | 0.975 (better) |
| `hex32-id` | end-minus-width | search-short | 307925 | 297969 | 0.968 (better) | 0.966 (better) |
| `uuid` | end-minus-width | throughput | 1081039 | 1060908 | 0.981 (better) | 0.983 (better) |
| `uuid` | end-minus-width | search-short | 21028 | 20372 | 0.969 (better) | 0.969 (better) |

#### email-specimen
| pattern | class | regime | 7388f1c0 caps (ns) | b8337c33 caps (ns) | caps B/A | nocaps B/A |
|---|---|---|---|---|---|---|
| `floor` | end-minus-width | throughput | 698908 | 659860 | 0.944 (better) | 0.944 (better) |
| `floor` | end-minus-width | search-short | 1326 | 986.1 | 0.744 (better) | 0.748 (better) |

#### litrun
| pattern | class | regime | 7388f1c0 caps (ns) | b8337c33 caps (ns) | caps B/A | nocaps B/A |
|---|---|---|---|---|---|---|
| `floor` | end-minus-width | throughput | 3138657 | 2945623 | 0.938 (better) | 0.938 (better) |
| `floor` | end-minus-width | search-short | 245.1 | 247.0 | 1.008 (WORSE) | 1.007 (ov) |
| `lit-l10` | end-minus-width | throughput | 1093912 | 760974 | 0.696 (better) | 0.695 (better) |
| `lit-l10` | end-minus-width | search-short | 450.8 | 317.4 | 0.704 (better) | 0.702 (better) |
| `lit-l16` | end-minus-width | throughput | 1012192 | 734727 | 0.726 (better) | 0.725 (better) |
| `lit-l16` | end-minus-width | search-short | 562.9 | 368.9 | 0.655 (better) | 0.656 (better) |
| `lit-l2` | end-minus-width | throughput | 3372349 | 3061991 | 0.908 (better) | 0.908 (better) |
| `lit-l2` | end-minus-width | search-short | 434.4 | 362.4 | 0.834 (better) | 0.855 (better) |
| `lit-l3` | end-minus-width | throughput | 3415951 | 3161079 | 0.925 (better) | 0.923 (better) |
| `lit-l3` | end-minus-width | search-short | 501.1 | 385.9 | 0.770 (better) | 0.772 (better) |
| `lit-l31` | end-minus-width | throughput | 788067 | 523008 | 0.664 (better) | 0.664 (better) |
| `lit-l31` | end-minus-width | search-short | 825.0 | 564.1 | 0.684 (better) | 0.684 (better) |
| `lit-l4` | end-minus-width | throughput | 3152461 | 2757349 | 0.875 (better) | 0.873 (better) |
| `lit-l4` | end-minus-width | search-short | 442.6 | 353.6 | 0.799 (better) | 0.802 (better) |
| `lit-l40` | end-minus-width | throughput | 463158 | 346286 | 0.748 (better) | 0.746 (better) |
| `lit-l40` | end-minus-width | search-short | 977.3 | 624.0 | 0.638 (better) | 0.637 (better) |
| `lit-l7` | end-minus-width | throughput | 3209188 | 2671767 | 0.833 (better) | 0.831 (better) |
| `lit-l7` | end-minus-width | search-short | 484.5 | 349.7 | 0.722 (better) | 0.721 (better) |
| `lit-l8` | end-minus-width | throughput | 2863959 | 2411137 | 0.842 (better) | 0.841 (better) |
| `lit-l8` | end-minus-width | search-short | 477.9 | 347.5 | 0.727 (better) | 0.724 (better) |
| `wild-secrets-aws-access-key-id` | end-minus-width | throughput | 403957 | 402539 | 0.996 (better) | 1.000 (ov) |
| `wild-secrets-aws-access-key-id` | end-minus-width | search-short | 1009 | 936.1 | 0.927 (better) | 0.923 (better) |
| `wild-secrets-github-pat` | end-minus-width | throughput | 29811 | 29849 | 1.001 (WORSE) | 1.000 (ov) |
| `wild-secrets-github-pat` | end-minus-width | search-short | 1272 | 951.8 | 0.749 (better) | 0.641 (better) |


Tier-2 sets (every cell is in the movers file; extremes here, caps):
- **syntax** (49 patterns, 98 caps cells): best `cls-w` throughput x0.703 (landing), `mod-a` x0.715, `cls-posix` x0.720, `unp-p-lc` x0.722,
  `cls-d` x0.730; worst `mod-s` throughput x1.012 (end-minus-width, DISJ), `esc-nl` x1.003 (DISJ), `cls-negset` x1.000, `esc-cr` x1.000. No syntax mover is WORSE by more than 1.2%.
- **utf8** (56 patterns, 112 caps cells): best `prp-l` throughput x0.517 and short x0.568 (FIT row, 4.4), `cls-neg-cjk` throughput x0.544, `prp-latin` x0.729,
  `cls-mixed` x0.732, `cls-boundary-range` x0.747, `prp-cyrillic` x0.757; **worst (short-subject-search, DISJ): `prp-lu` x1.060, `ci-neg-fold` x1.054, `asr-lb-neg`
  x1.052 (end-minus-width), `cls-dot` x1.051, `cls-neg-single` x1.049, `lit-offset-at-tail` x1.028, `lit-offset-at-head` x1.026, `prp-lu` throughput x1.026,
  `alt-mixed-width` x1.016, `lit-1ch-2b` x1.018, `floor` x1.020, `qnt-lazy-2b` x1.015, `prp-greek` x1.016** (nocaps agrees on 10 of the 12 patterns; `alt-mixed-width` and `prp-greek` are caps-only). 12 patterns,
  24 cells slower, +1.3% to +6.0% (+10 to +92 ns on 770-1,870 ns cells).
- **bounded** (17 patterns, 34 caps cells): best `nest2-letters-6` throughput x0.596 (landing), `nest2-64` x0.672, `nest3-16` x0.677, `dig-exact-32` x0.697;
  worst `hex32` nocaps short x1.015 (DISJ; `dfa_uniform_folds 2 > 1`, `scan_edges 2 > 1`), `floor` throughput x1.003 (ov). No bounded mover is worse than +1.5%.

### 4.4 The FIT movers (I-145: `prp-l`, `prp-notl`)

Confirmed by value on all four utf8 records (caps and nocaps): `ENGINE_SEL size-cap-retry > selected`, `dfa_start reverse-pass > landing`,
`emit_bytes` 471,796 > 894,613 (`prp-l`) and 490,248 > 874,155 (`prp-notl`) -- they GROW, as the pcrec note said. They also get FASTER, by more
than the other landing movers: `prp-l` throughput 11,763,642 > 6,077,654 ns (x0.517) and short 3,093.1 > 1,756.4 (x0.568); `prp-notl` throughput 5,813,574 > 5,073,691
(x0.873) and short 1,424.6 > 1,298.1 (x0.911) (nocaps within 0.3%). The size-rung change and START-LANDING arrive in the same step, so this ledger does not split the
two (the denial `-fno-start-landing` restores the retry; it is a scratch-tier arm, not run here). Any set-grain mean over utf8 mixes both.

### 4.5 Non-movers that moved

Of 852 program-identical cells only ONE is both beyond trial overlap and beyond 3%: `loglines` `http-5xx` short-subject-search, **nocaps only**,
4,949.0 > 5,153.8 ns (x1.041, ranges 4,944.8-4,953.9 vs 5,146.7-5,160.6; `dfa_start reverse-pass` on both sides, program identical). Its caps twin reads 4,947.0 > 4,944.6
(x1.000) and both throughput cells read x1.001: a one-config, one-regime step that did not repeat across the caps/nocaps pair. 36 further program-identical
cells are DISJ but within +-1.5% (e.g. syntax `rec-name` caps short x1.015, `rec-r-uc` nocaps short x0.983); 10 are outside +-5% and every one of
those has overlapping trial ranges (wide-spread cells: `phone-palindrome-6` x0.753 / x0.953, `bak-2` x0.899, `bounded` `cls-lazy-16384` / `cls-upto-*` throughput, `bracket-array-define` x0.890 --
the window-3 control record's own slow state, section 2). **Nothing outside the stamp-flipped set moved in a way the null does not already contain.**

## 5. The controls I-146 asked for

### 5.1 The tail family -- a mover would be news; none

Stamps (every tail pattern, both forms, both configs): `dfa_scan rev-end`, `dfa_start reverse-pass`, `dfa_prefilter none` at BOTH pins, `program_sha256` identical on all
12 (pattern, form) rows -- b8337c33 does not recompile the family, as pcrec stated. Timing (`2026-10-11-b135-state3-tail.txt`):

- set cells (5 tail patterns + `letters-bounded-tail-z`, 2 regimes, 2 configs = 24): b8337c33 / 7388f1c0 (window 3) 0.990-1.013, **all 24 overlap**; window 3 / window 1 of
  7388f1c0 0.978-1.011.
- per-subject large-subject cells (6 patterns x 11 subjects x 2 configs = 132): b8337c33 / 7388f1c0 median 1.000 (caps p5-p95 0.980-1.040, nocaps 0.952-1.019),
  **0 disjoint**. The two remaining long-matching-body cells: `tail-word-eoz` x `t-evil-match-60k` 21,775.3 (7388f1c0 w1) / 21,774.2 (w3) / 21,772.9 (b8337c33) ns caps,
  `tail-space-eol` x `t-trim-match-60k` 21,799.2 / 21,799.4 / 21,808.4: unmoved to 0.05%.
- Verdict: the tail family is a clean cross-window control at state 3 (I-146's expectation held), and the "0.354 ns/B walk over a body that matches back to byte 0" is exactly where it was.

### 5.2 `wild-logparse-quotedstring-grok` caps -- the +19% did NOT persist

Short-subject-search set cell, caps, one program (`program_sha256` ae9848c3aa54..., `emit_bytes` 64,131, `vm_program_bytes` 17,340, `artifact_bytes` 41,864 at all four records):

| state | median ns (min-max) |
|---|---|
| a15fb77b, window 1 | 2,122.7 (2,102.5-2,129.3) |
| 7388f1c0, window 1 | 2,525.2 (2,517.9-2,529.3) |
| 7388f1c0, window 3 (control) | 2,149.0 (2,110.7-2,189.4) |
| b8337c33, window 3 | 2,147.0 (2,139.9-2,175.6) |

Per subject, 7388f1c0 window 3 vs window 1: faster on 75 of 75 subjects, median -5.3 ns (-7.3 to -0.6); window 1 vs a15fb77b: slower on 75 of 75, median +5.4 ns. nocaps never moved (2,154.1 / 2,164.5 / 2,141.3 / 2,121.8). b8337c33 vs
7388f1c0 window 3: x0.999, ranges overlap. The SAME 7388f1c0 testee id reads 2,525 in window 1 and 2,149 in window 3, so the +19% belongs to that record (a layout, process-state or
window effect on a program-identical artifact), not to the abi 72 > 73 step. Emitted-C diff (the brief's conditional "if it persists" is not met; done anyway for the relay ask):
`pcrec -p rx -fcomments --features all --pattern <text>` at 7388f1c0 and b8337c33: both 47,473 bytes, **three differing lines** (the generator banner `abi 73` / `abi 74`, the
`#include` of the per-pin header name, `.abi = 73` / `74`) -- `docs/dev/measurements/2026-10-11-b135-state3-grok-emitted-c-diff.txt`. No alignment-offset control was run (nothing to control); the unreplicated
window-1 reading stays unexplained, and the control the manager can quote is simply "a second window of the same testee reads 2,149".

## 6. pcrecdev1's [ENG-TACTICS] ask -- every loglines/* and altwide@0.3 sfx-* median at b8337c33

Set-grain cells (sum over the cell's subjects), window 3, pinned records, 5 trials, "median (min-max)" in ns. `Form whole-subject` is the `(?:...)\z` artifact (`match-compliance`).
Stamps are b8337c33's compile row (caps; nocaps identical). `loglines` `floor` nocaps throughput carries one slow trial (max 5,443,347.4 against a 2,841,138.2 median; the median is the figure).
Per-subject medians: `2026-10-11-b135-state3-sfx.txt` / the reports' subject-grain slices.

| set | pattern | regime | form | caps median ns (min-max) | nocaps median ns (min-max) | engine / scan / start / prefilter | subjects |
|---|---|---|---|---|---|---|---|
| loglines | `bignum` | large-subject-throughput | plain | 7,289,045.9 (7,279,862.6-7,291,919.4) | 7,261,136.4 (7,224,156.0-7,281,046.4) | dfa / unanchored / reverse-pass / first-class-bounded | 12 |
| loglines | `bignum` | short-subject-search | plain | 237,285.8 (236,236.5-238,232.2) | 237,399.7 (237,253.8-238,018.9) | dfa / unanchored / reverse-pass / first-class-bounded | 112 |
| loglines | `floor` | large-subject-throughput | plain | 2,842,707.3 (2,841,508.4-2,842,983.2) | 2,841,138.2 (2,839,035.5-5,443,347.4) | dfa / unanchored / end-minus-width / memchr | 12 |
| loglines | `floor` | short-subject-search | plain | 1,512.2 (1,510.3-1,814.1) | 1,511.8 (1,498.2-1,517.2) | dfa / unanchored / end-minus-width / memchr | 112 |
| loglines | `hex32-id` | large-subject-throughput | plain | 11,052,363.4 (11,045,672.8-11,064,049.1) | 11,057,040.6 (11,051,702.3-11,058,304.5) | dfa / unanchored / end-minus-width / first-class-bounded | 12 |
| loglines | `hex32-id` | short-subject-search | plain | 297,968.6 (297,630.4-298,078.8) | 297,938.2 (297,491.0-298,011.6) | dfa / unanchored / end-minus-width / first-class-bounded | 112 |
| loglines | `http-5xx` | large-subject-throughput | plain | 280,071.5 (279,568.9-280,875.1) | 280,542.3 (279,790.3-281,690.0) | dfa / unanchored / reverse-pass / memchr-bounded | 12 |
| loglines | `http-5xx` | short-subject-search | plain | 4,944.6 (4,943.8-4,985.0) | 5,153.8 (5,146.7-5,160.6) | dfa / unanchored / reverse-pass / memchr-bounded | 112 |
| loglines | `ipv4` | large-subject-throughput | plain | 6,938,840.7 (6,933,711.4-6,946,778.8) | 6,946,944.0 (6,938,426.0-6,954,694.2) | dfa / unanchored / reverse-pass / byte-class | 12 |
| loglines | `ipv4` | short-subject-search | plain | 207,712.9 (206,464.7-208,241.9) | 207,664.9 (207,524.2-208,423.0) | dfa / unanchored / reverse-pass / byte-class | 112 |
| loglines | `ipv6` | large-subject-throughput | plain | 10,616,540.5 (10,491,370.0-10,625,997.2) | 10,622,994.8 (10,528,765.2-10,634,336.0) | dfa / unanchored / reverse-pass / byte-class | 12 |
| loglines | `ipv6` | short-subject-search | plain | 260,510.0 (258,163.6-262,078.5) | 259,378.0 (258,324.2-261,717.0) | dfa / unanchored / reverse-pass / byte-class | 112 |
| loglines | `iso-ts` | large-subject-throughput | plain | 1,152,508.5 (1,151,977.7-1,152,999.8) | 1,152,760.2 (1,150,821.1-1,153,275.5) | dfa / unanchored / reverse-pass / offset-set | 12 |
| loglines | `iso-ts` | short-subject-search | plain | 20,564.2 (20,553.5-21,038.9) | 20,552.4 (20,538.5-20,566.0) | dfa / unanchored / reverse-pass / offset-set | 112 |
| loglines | `kv-quoted` | large-subject-throughput | plain | 202,809.9 (202,573.4-203,468.8) | 202,819.1 (202,682.1-203,916.0) | dfa / unanchored / reverse-pass / first-class-bounded | 12 |
| loglines | `kv-quoted` | short-subject-search | plain | 5,700.0 (5,697.0-5,711.4) | 5,699.5 (5,696.5-5,702.1) | dfa / unanchored / reverse-pass / first-class-bounded | 112 |
| loglines | `level-context` | large-subject-throughput | plain | 2,290,791.2 (2,290,324.1-2,303,670.6) | 2,291,346.3 (2,288,357.2-2,291,856.8) | vm / unanchored / reverse-pass / first-class-bounded | 12 |
| loglines | `level-context` | short-subject-search | plain | 83,955.6 (83,888.1-83,978.5) | 83,889.7 (83,861.9-84,034.7) | vm / unanchored / reverse-pass / first-class-bounded | 112 |
| loglines | `stack-frame` | large-subject-throughput | plain | 1,307,579.0 (1,307,161.3-1,309,147.8) | 1,308,074.1 (1,307,392.4-1,309,128.8) | dfa / unanchored / reverse-pass / offset-set-bounded | 12 |
| loglines | `stack-frame` | short-subject-search | plain | 33,358.7 (33,346.4-33,383.9) | 33,323.2 (33,278.4-33,378.4) | dfa / unanchored / reverse-pass / offset-set-bounded | 112 |
| loglines | `uuid` | large-subject-throughput | plain | 1,060,907.6 (1,060,343.4-1,064,360.8) | 1,061,509.7 (1,059,426.0-1,061,650.8) | dfa / unanchored / end-minus-width / offset-set-bounded | 12 |
| loglines | `uuid` | short-subject-search | plain | 20,372.4 (20,355.3-20,401.6) | 20,331.1 (20,313.1-20,336.8) | dfa / unanchored / end-minus-width / offset-set-bounded | 112 |
| altwide | `sfx-256` | large-subject-throughput | plain | 2,618,112.9 (2,613,122.4-2,647,614.5) | 2,621,032.6 (2,615,962.9-2,623,659.5) | dfa / unanchored / reverse-pass / byte-class | 4 |
| altwide | `sfx-256` | match-compliance | whole-subject | 428.0 (422.9-435.5) | 429.4 (429.2-431.6) | dfa / rev-end / reverse-pass / none | 40 |
| altwide | `sfx-256` | short-subject-search | plain | 1,016.4 (1,014.9-1,017.9) | 1,019.2 (1,016.9-1,028.2) | dfa / unanchored / reverse-pass / byte-class | 40 |
| altwide | `sfx-512` | large-subject-throughput | plain | 1,865,818.8 (1,864,170.7-1,866,377.7) | 1,866,491.6 (1,864,681.1-1,867,235.6) | dfa / unanchored / reverse-pass / byte-class | 4 |
| altwide | `sfx-512` | match-compliance | whole-subject | 447.0 (446.4-448.5) | 447.2 (446.1-451.3) | dfa / rev-end / reverse-pass / none | 40 |
| altwide | `sfx-512` | short-subject-search | plain | 1,017.9 (1,016.7-1,020.1) | 1,018.2 (1,016.3-1,019.1) | dfa / unanchored / reverse-pass / byte-class | 40 |
| altwide | `sfx-64` | large-subject-throughput | plain | 2,803,525.6 (2,799,922.4-2,807,238.0) | 2,801,848.2 (2,799,650.4-2,810,518.1) | dfa / unanchored / reverse-pass / byte-class | 4 |
| altwide | `sfx-64` | match-compliance | whole-subject | 423.4 (421.8-432.4) | 424.9 (422.7-428.8) | dfa / rev-end / reverse-pass / none | 40 |
| altwide | `sfx-64` | short-subject-search | plain | 1,016.6 (1,013.8-1,030.1) | 1,021.2 (1,015.7-1,022.5) | dfa / unanchored / reverse-pass / byte-class | 40 |

## 7. I-146's relay asks

### 7.1 (1) The exact litrun pattern texts for O-96 (c)2's regressed whole forms

The whole form is `(?:P)\z` over the plain text P (bench/litrun/patterns/*.rx, no trailing newline). O-96 (c)2 named, with the REVEND-step ratio
(a15fb77b > 7388f1c0, window 1) and the state-3 ratios (7388f1c0 control > b8337c33):

| pattern id | P (exact bytes) | REVEND x, window 1 (caps / nocaps) | state 3 x (caps / nocaps) |
|---|---|---|---|
| `alt-foo-tails` | `foo.x\|foobar\|foo.` | 1.077 / 1.077 | 0.999 / 1.004 |
| `lit-l4` | `abcd` | 1.034 / 1.035 | 0.999 / 0.997 |
| `lit-l2` | `ab` | 1.032 / 1.032 | 1.002 / 1.006 |
| `lit-l8` | `abcdefgh` | 1.022 / 1.023 | 1.001 / 1.001 |
| `wild-secrets-aws-access-key-id` | `\b((?:A3T[A-Z0-9]\|AKIA\|AGPA\|AIDA\|AROA\|AIPA\|ANPA\|ANVA\|ASIA)[A-Z0-9]{16})\b` | 1.001 / 1.048 | 0.999 / 0.999 |
| `wild-secrets-github-pat` | `\b(github_pat_[0-9a-zA-Z_]{82})\b` | 1.023 / 1.002 | 1.000 / 1.001 |
| `lit-l31` | `abcdefghijklmnopqrstuvwxyzABCDE` | 0.977 / 0.975 (win) | 1.002 / 0.999 |
| `lit-l40` | `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN` | 0.982 / 0.980 (win) | 0.999 / 0.999 |

(the `\|` is a table-escaped `|`; `foo.` is `foo` then the any-character metacharacter.) The whole-subject rows are measured at
`match-compliance` (27 subjects per pattern). State 3 leaves them where REVEND put them (the per-call medians are 263.7-404.9 ns).

### 7.2 (2) The quotedstring-grok emitted-C diff -- section 5.2

### 7.3 (3) A Vectorscan SOM reading of the tail cells

Records: capability@0.2 `vectorscan_5.4.11_block-som-nocaps-simd` (2026-10-09T03:38Z) and `...block-nosom-nocaps-simd` (2026-10-09T03:09Z), against pcrec-**nocaps** (the same
capture class: neither reports captures) at 7388f1c0 (windows 1 and 3) and b8337c33 (window 3). **CROSS-WINDOW caveat: the Vectorscan records are 1.5-2 days older than the pcrec
records and carry no same-window control; the sentinel does not include Vectorscan. The ratios below are x6 to x164,000 -- vastly beyond the +-0.7% window drift of section 2.**
Set cells over capability's `large-subject-throughput` subjects (11 per pattern; every subject judged correct on all arms), median ns (min-max):

| pattern | Vectorscan SOM | Vectorscan no-SOM | pcrec 7388f1c0 w1 | pcrec 7388f1c0 w3 | pcrec b8337c33 w3 | b8337c33 vs SOM |
|---|---|---|---|---|---|---|
| `tail-digits-eol` | 5,308,973 (5,143,291-5,347,749) | 878.5 | 135.7 | 136.6 | 135.2 | x39,000 faster |
| `tail-word-eoz` | 22,253,652 (22,168,266-22,306,632) | 393.7 | 21,905.0 | 21,908.9 | 21,909.0 | **x1,016 faster** (vs no-SOM: x55.6 slower) |
| `tail-space-eol` | 18,044,599 (17,687,008-18,113,918) | 1,013.0 | 21,978.9 | 21,977.8 | 21,970.8 | **x821 faster** (vs no-SOM: x21.7 slower) |
| `tail-ext-lower-txt` | 20,495,296 (20,335,598-20,509,518) | 880.7 | 125.2 | 125.0 | 124.7 | x164,000 faster |
| `tail-dotstar-txt` | 4,653,247 (4,549,560-4,764,261) | 866.1 | 147.4 | 145.0 | 146.9 | x31,700 faster |

The two cells that lose to no-SOM are the two long-matching-body subjects: `tail-word-eoz` x `t-evil-match-60k` SOM 133,475.9 ns vs pcrec 21,776.3 (**x6.1 faster**; no-SOM 38.2);
`tail-space-eol` x `t-trim-match-60k` SOM 133,331.8 vs 21,797.7 (**x6.1 faster**; no-SOM 127.3). Everywhere else SOM scales with the body (t-1m: 1.8-5.3 ms) while pcrec stays at 6-33 ns.
**Read against SOM -- the like-for-like arm for an engine that reports a leftmost start -- pcrec wins every tail cell, including the two that read as losses against no-SOM.**
Like-for-like means: no-SOM reports only whether a match exists (a boolean grain, never a span), pcrec's rev-end walk is the price of the leftmost start (I-146).
Per-subject table: `2026-10-11-b135-state3-som.txt`.

## 8. What this window shows, ranked

1. **START-LANDING works as designed where it applies.** 292 compile rows flipped (the whole 298 minus 6 with no pair), the movers are 76-78% beyond-overlap faster against a 2.6% null, the best
   cells x0.52-0.70, and the whole-subject form and the tail family are untouched (278 whole-subject cells, 24 tail set cells and 132 tail per-subject cells, none moved).
2. **Two populations get slower, both small and both in search-short:** utf8 (12 patterns, +1.3..+6.0%, 24 cells, `prp-lu`, `ci-neg-fold`, `cls-dot`, `cls-neg-single`, `asr-lb-neg`, the `lit-*` heads) and a handful of
   sub-1% rows (uuid-grok throughput +0.7%, aws nocaps throughput +0.6%, litrun `floor` short +0.8%). The sub-1% rows are inside the +-0.7% window drift. The utf8 rows are not.
3. **The gain is mostly a search-regime gain**: ewm throughput median 0.976 (143/204 better) vs search 0.925 (168/204); capability's throughput rows are flat because its throughput subjects
   rarely match.
4. **One compile-time mover:** pcrec's own emit-c phase on `wild-datetime-datefinder-alternation` (nocaps, 891,859 B emit, program-identical) is x2.53 (173 -> 437 ms); the other 119 (set, config, pattern, form) emit-c cells over 10 ms move by at most x1.18 and the gcc phase is unchanged (`2026-10-11-b135-state3-emitc-phase.txt`; the trend page shows the same pattern's total compile time x1.53 nocaps / x1.83 caps, the caps side being a refusal at both pins). One pattern, not attributed.
5. Instrument/window facts: sentinels flat (pcrec <= 1.3% over 16 h), the 7388f1c0 control reproduces its window-1 numbers to +-0.7% (p5-p95), with the grok +19% not reproducing.

## 9. Checklist the NEXT sample is read against

- sentinel `end/open` <= 1.5% for pcrec and jit's trial agreement; the control column of any three-state table <= +-0.7% (p5-p95) except named cells.
- tail family: `rev-end / reverse-pass`, `program_sha256` unchanged across pins unless pcrec announces K103/`rev-end-width`; the two 21.8 us long-body cells.
- utf8 search-short movers listed in 4.3: do the 12 slower patterns recover at the next pin (cause unestablished here; a hypothesis is the per-call landing/ill-formed-step cost under `-e utf8`)?
- grok caps short: 2,147 +- 1% (second-window reading); a return to 2,525 would be the state, not the pin.
