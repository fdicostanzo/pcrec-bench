# [B138] re-baseline wall-clock hours on the OLD box (budu-ryzen1600, Ryzen 5 1600)

Lane b138hours, read-only. No timing, no store load: store/index.tsv plus the
first JSONL line of each of the 507 records (small script, one record at a
time; scratch at /var/tmp/b138dur.py, b138an.py, b138core.py).

## Headline

| roster | cells | cell minutes | + overhead | WALL HOURS |
|---|---|---|---|---|
| (A) FULL: every config measured at the set's current version, one cell each, pins collapsed | 100 | 2,838 | 2,910 min | **48.5 h** |
| (B) CORE: pcrec-auto/-nocaps/-vm, pcre2-jit/-interp, one config per other engine, sentinel | 56 | 1,589 | 1,640 min (+45 imputed) | **27.3 h as measured, 28.1 h with the one imputed cell** |

Overhead = 0.5 min per cell (the ~25-40 s sleep + quiet-gate gap between cells)
+ 2.5 min per set (the ~150 s extra gap before the first cell of each set).
Not included: the sentinel pass the chain brackets each tier with (5 cells,
~33 min per pass; the b136 night ran six of them, ~3.3 h).

## Method

Per-cell duration = `environment.load.after.sampled_at` minus
`environment.load.before.sampled_at` inside each record (the harness samples
load immediately before the first and after the last trial; `run.timestamp`
and the index timestamp are the START, within ~5 s of `before`). That is the
cell's measured span: compile, all subjects, all trials. Records do NOT carry
a separate end timestamp or per-trial wall time (`trial_agreement.trials` is a
count).

Cross-check 1, gap method: consecutive cells of the 2026-10-12/13 b136 night,
start(next) minus end(prev) = 24-44 s between cells of one set and 150-170 s
at a set boundary, 5,426 s once (a manual stop between tiers). So the cell
durations sum to the night's wall time within the gaps; no cell hides time.

Cross-check 2, b136_chain.sh tier totals (predicted ~1236 min = 20.6 h).
Actual span from the first cell start (10-12 15:09 UTC, sentinel pass) to the
last cell end of tier 4 (10-13 ~11:54 UTC, email interp): **20 h 45 min =
1,245 min**, within 1% of the prediction in total. Per tier the prediction
was off both ways: tier 1 actual ~312 vs 356 min, tier 2 ~246 vs 240,
tier 3 ~310 vs 361, tier 4 ~372 vs 279 (tier 4 includes a sentinel pass the
estimate probably left out). Later cells on 10-13 (13:24 onward: sentinel
passes, the utf8 noreqhandoff re-run, bounded canonical, email canonical,
the capability nocaps/deny cells) are repairs/extra tiers beyond those 1,245
min. Sum of the b136-window cell durations by set (all cells after 10-12
15:00): sentinel 192, loglines 50, altwide 94, bounded 266, litrun 81,
capability 298, syntax 252, utf8 217, email 26 = 1,475 min including those
late cells.

Confidence: HIGH (about +-5%) for the per-cell minutes of cells measured in
the quiet b136 night (10-12/13); MEDIUM for cells last measured at older pins
or on other nights (cost depends on the pin, e.g. bounded vm 54-57 min at
751b9c6d vs 47 min at 288d505b; a pin whose engine got faster or slower
moves the number); the totals' dominant uncertainty is the roster
definition, not the timing.

Roster rules used. Config key = testee_id with the pcrec pin removed, so
`pcrec_6b2dbd3e_auto-caps-simdna` and `pcrec_b8337c33_auto-caps-simdna` are one
config; the most recent cell at the set's current version supplies the
minutes. Current versions from bench/*/subbench.toml agree with the highest
version in the index for every set.


## altwide@0.3

| min | testee config | last pin | status | measured |
|---:|---|---|---|---|
| 65.0 | libpcre2_10.46_jit-caps-simdna | (pinned engine) | measured | 2026-10-02 |
| 23.7 | pcrec:auto-caps-simdna | 6b2dbd3e | measured | 2026-10-12 |
| 23.6 | pcrec:auto-caps-simdna_noreqhandoff | 00c97769 | measured | 2026-10-12 |
| 23.5 | pcrec:auto-nocaps-simdna | b8337c33 | measured | 2026-10-11 |
| 21.8 | rust_1.13.1_default-caps-simdna | (pinned engine) | measured | 2026-10-02 |
| 18.5 | pcrec:vm-caps-simdna | c4c70f2c | measured | 2026-10-05 |
| 17.3 | pcrec:auto-caps-simdna_noisland | fc719ca4 | measured | 2026-10-02 |

sum 193 min over 7 configs.

## bounded@0.3

| min | testee config | last pin | status | measured |
|---:|---|---|---|---|
| 56.6 | pcrec:vm-in-caps-simdna | 751b9c6d | measured | 2026-09-27 |
| 54.4 | pcrec:vm-caps-simdna | 751b9c6d | measured | 2026-09-27 |
| 53.0 | pcrec:vm-caps-simdna_cc-clang | 1989c623 | measured | 2026-09-02 |
| 49.1 | pcrec:auto-caps-simdna_noreqhandoff | 00c97769 | measured | 2026-10-12 |
| 48.6 | pcrec:auto-nocaps-simdna | 7388f1c0 | measured | 2026-10-11 |
| 48.5 | pcrec:auto-nocaps-simdna_cc-clang | 1989c623 | measured | 2026-09-02 |
| 47.9 | pcrec:auto-caps-simdna_cc-clang | 334fd10e | measured | 2026-09-05 |
| 46.8 | pcrec:auto-caps-simdna_nolitrun | a32bc86e | measured | 2026-09-28 |
| 45.8 | libpcre2_10.46_interp-caps-simdna | (pinned engine) | measured | 2026-10-13 |
| 45.5 | pcrec:auto-caps-simdna | 6b2dbd3e | measured | 2026-10-13 |
| 43.5 | pcrec:auto-caps-simdna_cf-align-functions-64 | 288d505b | measured | 2026-09-05 |
| 35.6 | libpcre2_10.46_jit-caps-simdna | (pinned engine) | measured | 2026-10-13 |
| 27.0 | rust_1.13.1_default-caps-simdna | (pinned engine) | measured | 2026-09-20 |

sum 602 min over 13 configs.

## capability@0.2

| min | testee config | last pin | status | measured |
|---:|---|---|---|---|
| 106.5 | libpcre2_10.46_dfa-nocaps-simdna | (pinned engine) | measured | 2026-10-08 |
| 71.9 | libpcre2_10.46_interp-caps-simdna | (pinned engine) | measured | 2026-10-08 |
| 61.3 | pcrec:vm-caps-simdna | 255bcdd8 | measured | 2026-10-08 |
| 59.7 | pcrec:vm-in-caps-simdna | 255bcdd8 | measured | 2026-10-08 |
| 57.6 | oniguruma_6.9.10_default-caps-simdna | (pinned engine) | measured | 2026-10-09 |
| 50.5 | pcrec:auto-caps-simdna | 6b2dbd3e | measured | 2026-10-12 |
| 50.0 | pcrec:auto-nocaps-simdna | 00c97769 | measured | 2026-10-13 |
| 46.4 | libpcre2_10.46_jit-caps-simdna | (pinned engine) | measured | 2026-10-08 |
| 46.2 | pcrec:auto-caps-simdna_noreqhandoff | 00c97769 | measured | 2026-10-13 |
| 29.2 | vectorscan_5.4.11_block-som-nocaps-simd | (pinned engine) | measured | 2026-10-09 |
| 28.6 | tre_0.9.0_default-caps-simdna | (pinned engine) | measured | 2026-10-09 |
| 28.2 | vectorscan_5.4.11_block-nosom-nocaps-simd | (pinned engine) | measured | 2026-10-09 |
| 21.6 | re2_11.0.0_longest-caps-simdna | (pinned engine) | measured | 2026-10-09 |
| 21.2 | re2_11.0.0_default-caps-simdna | (pinned engine) | measured | 2026-10-09 |
| 19.8 | rust_1.13.1_default-caps-simdna | (pinned engine) | measured | 2026-10-09 |

sum 699 min over 15 configs.

## email-specimen@0.2

| min | testee config | last pin | status | measured |
|---:|---|---|---|---|
| 11.9 | libpcre2_10.46_jit-caps-simdna | (pinned engine) | measured | 2026-10-13 |
| 8.5 | pcrec:vm-caps-simdna | 751b9c6d | measured | 2026-09-27 |
| 8.4 | libpcre2_10.46_interp-caps-simdna | (pinned engine) | measured | 2026-10-13 |
| 8.2 | pcrec:vm-in-caps-simdna | 751b9c6d | measured | 2026-09-27 |
| 5.6 | pcrec:auto-caps-simdna | 6b2dbd3e | measured | 2026-10-13 |
| 5.3 | pcrec:auto-nocaps-simdna | 7388f1c0 | measured | 2026-10-11 |
| 4.7 | pcrec:auto-caps-simdna_noclsfold | d34c9131 | measured | 2026-09-06 |
| 2.7 | rust_1.13.1_default-caps-simdna | (pinned engine) | measured | 2026-09-20 |

sum 55 min over 8 configs.

## litrun@0.1

| min | testee config | last pin | status | measured |
|---:|---|---|---|---|
| 18.5 | libpcre2_10.46_interp-caps-simdna | (pinned engine) | measured | 2026-10-13 |
| 16.1 | pcrec:auto-caps-simdna_noaltclsfactor | a32bc86e | measured | 2026-09-28 |
| 16.0 | pcrec:auto-caps-simdna_noaltclsfactor-nolitrun | a32bc86e | measured | 2026-09-28 |
| 14.7 | pcrec:auto-caps-simdna_nolitrun | a32bc86e | measured | 2026-09-28 |
| 12.9 | pcrec:auto-caps-simdna | 6b2dbd3e | measured | 2026-10-12 |
| 12.9 | pcrec:auto-caps-simdna_norevend | 6b2dbd3e | measured | 2026-10-12 |
| 12.9 | pcrec:vm-caps-simdna_noaltclsfactor-nolitrun | a32bc86e | measured | 2026-09-28 |
| 12.8 | pcrec:vm-caps-simdna_nolitrun | a32bc86e | measured | 2026-09-28 |
| 12.7 | pcrec:auto-nocaps-simdna_norevend | 6b2dbd3e | measured | 2026-10-12 |
| 12.2 | libpcre2_10.46_jit-caps-simdna | (pinned engine) | measured | 2026-10-13 |
| 11.5 | pcrec:vm-caps-simdna_noaltclsfactor | a32bc86e | measured | 2026-09-28 |
| 11.3 | pcrec:auto-nocaps-simdna | 6b2dbd3e | measured | 2026-10-12 |
| 9.7 | pcrec:vm-caps-simdna | c4c70f2c | measured | 2026-10-05 |
| 6.3 | pcrec:vm-caps-simdna_noreqbyte-noreqrun | a32bc86e | measured | 2026-09-28 |
| 6.1 | pcrec:vm-caps-simdna_noreqbyte-noreqrun-nolitrun | a32bc86e | measured | 2026-09-28 |

sum 187 min over 15 configs.

## loglines@0.1

| min | testee config | last pin | status | measured |
|---:|---|---|---|---|
| 12.6 | pcrec:vm-in-caps-simdna | 751b9c6d | measured | 2026-09-27 |
| 12.5 | pcrec:vm-caps-simdna | 751b9c6d | measured | 2026-09-27 |
| 9.8 | pcrec:auto-caps-simdna_noedge | fc719ca4 | measured | 2026-10-02 |
| 9.2 | pcrec:auto-caps-simdna_nolitrun | a32bc86e | measured | 2026-09-28 |
| 9.1 | pcrec:auto-caps-simdna_noreqhandoff | 00c97769 | measured | 2026-10-12 |
| 8.6 | libpcre2_10.46_interp-caps-simdna | (pinned engine) | measured | 2026-10-13 |
| 8.2 | pcrec:auto-nocaps-simdna | 7388f1c0 | measured | 2026-10-11 |
| 8.1 | libpcre2_10.46_jit-caps-simdna | (pinned engine) | measured | 2026-10-13 |
| 8.1 | pcrec:auto-caps-simdna_cc-clang | 1989c623 | measured | 2026-09-02 |
| 8.1 | pcrec:auto-nocaps-simdna_cc-clang | 1989c623 | measured | 2026-09-02 |
| 8.1 | pcrec:auto-caps-simdna_noclsfold | d34c9131 | measured | 2026-09-06 |
| 7.8 | pcrec:vm-caps-simdna_cc-clang | 1989c623 | measured | 2026-09-02 |
| 7.7 | pcrec:auto-caps-simdna | 6b2dbd3e | measured | 2026-10-12 |
| 6.7 | rust_1.13.1_default-caps-simdna | (pinned engine) | measured | 2026-09-20 |

sum 125 min over 14 configs.

## sentinel@0.1

| min | testee config | last pin | status | measured |
|---:|---|---|---|---|
| 9.1 | libpcre2_10.46_jit-caps-simdna | (pinned engine) | measured | 2026-10-13 |
| 6.1 | pcrec:auto-caps-simdna | b8337c33 | measured | 2026-10-13 |
| 6.1 | pcrec:auto-nocaps-simdna | 6b2dbd3e | measured | 2026-10-13 |

sum 21 min over 3 configs.

## syntax@0.1

| min | testee config | last pin | status | measured |
|---:|---|---|---|---|
| 54.2 | libpcre2_10.46_interp-caps-simdna | (pinned engine) | measured | 2026-10-13 |
| 49.5 | pcrec:vm-caps-simdna | c4c70f2c | measured | 2026-10-05 |
| 49.3 | pcrec:vm-in-caps-simdna | 751b9c6d | measured | 2026-09-27 |
| 45.9 | pcrec:vm-nocaps-simdna | fc719ca4 | inconclusive-spread | 2026-10-02 |
| 45.1 | pcrec:auto-caps-simdna_nohybreseed | fc719ca4 | measured | 2026-10-01 |
| 44.5 | pcrec:auto-nocaps-simdna | 7388f1c0 | measured | 2026-10-11 |
| 43.1 | pcrec:auto-caps-simdna_noreqhandoff | 00c97769 | measured | 2026-10-13 |
| 37.7 | pcrec:auto-caps-simdna | 6b2dbd3e | measured | 2026-10-13 |
| 36.1 | libpcre2_10.46_jit-caps-simdna | (pinned engine) | measured | 2026-10-13 |
| 29.3 | pcrec:dfa-nocaps-simdna | fc719ca4 | measured | 2026-10-02 |
| 26.2 | pcrec:dfa-caps-simdna | fc719ca4 | measured | 2026-10-02 |
| 19.2 | rust_1.13.1_default-caps-simdna | (pinned engine) | measured | 2026-09-20 |

sum 480 min over 12 configs.

## utf8@0.1

| min | testee config | last pin | status | measured |
|---:|---|---|---|---|
| 41.7 | libpcre2_10.46_dfa-nocaps-simdna_utf8 | (pinned engine) | measured | 2026-09-26 |
| 41.2 | libpcre2_10.46_interp-caps-simdna_utf8 | (pinned engine) | measured | 2026-10-13 |
| 40.3 | pcrec:vm-caps-simdna_utf8 | c4c70f2c | measured | 2026-10-05 |
| 38.3 | pcrec:vm-in-caps-simdna_utf8 | 751b9c6d | measured | 2026-09-27 |
| 38.3 | vectorscan_5.4.11_block-nosom-nocaps-simd_utf8 | (pinned engine) | measured | 2026-09-26 |
| 38.2 | oniguruma_6.9.10_default-caps-simdna_utf8 | (pinned engine) | measured | 2026-09-26 |
| 38.1 | pcrec:auto-caps-simdna_nohybreseed-utf8 | fc719ca4 | measured | 2026-10-02 |
| 36.8 | libpcre2_10.46_jit-caps-simdna_utf8 | (pinned engine) | measured | 2026-10-13 |
| 34.8 | pcrec:auto-caps-simdna_noreqhandoff-utf8 | 00c97769 | measured | 2026-10-13 |
| 34.5 | pcrec:auto-caps-simdna_utf8 | 6b2dbd3e | measured | 2026-10-13 |
| 34.4 | pcrec:auto-nocaps-simdna_utf8 | 7388f1c0 | measured | 2026-10-11 |
| 30.6 | rust_1.13.1_default-caps-simdna | (pinned engine) | measured | 2026-09-26 |
| 28.5 | re2_11.0.0_default-caps-simdna_utf8 | (pinned engine) | measured | 2026-09-26 |

sum 476 min over 13 configs.
## Roster (B) CORE, per set (minutes of wall, cell + 0.5 min/cell + 2.5 min/set)

| set | cells | min | note |
|---|---:|---:|---|
| altwide@0.3 | 5 | 158 | pcre2-interp has NO cell at 0.3 (see below): +~45 min imputed |
| bounded@0.3 | 6 | 262 | |
| capability@0.2 | 10 | 443 | incl. onig 57.6, vectorscan-nosom 28.2, tre 28.6, re2-default 21.2, rust 19.8 |
| email-specimen@0.2 | 6 | 48 | |
| litrun@0.1 | 5 | 70 | no non-pcrec engine beyond pcre2 |
| loglines@0.1 | 6 | 57 | incl. rust 6.7 |
| sentinel@0.1 | 3 | 25 | one pin: pcrec auto, nocaps, pcre2-jit (the chain's 5-cell pass is ~33 min) |
| syntax@0.1 | 6 | 247 | incl. rust 19.2 |
| utf8@0.1 | 9 | 330 | pcrec auto/nocaps/vm-utf8, jit/interp-utf8, onig, re2, vectorscan-nosom-utf8, rust |
| **total** | **56** | **1,640** | **27.3 h; 28.1 h with altwide interp imputed** |

CORE excludes pcre2-dfa (capability 106.5, syntax-less, utf8 41.7 min), the
second re2 config (longest, 21.6), vectorscan som (29.2) and every deny/clang/
align/bigcap pcrec sibling.

## Cells over 60 minutes (these dominate the night)

| min | cell |
|---:|---|
| 106.5 | capability@0.2 libpcre2 dfa-nocaps (2026-10-08) -- longer than the 5400 s (90 min) default CELL_CAP; it must have run under a raised CELL_CAP_capability or before the cap existed (not determined) |
| 71.9 | capability@0.2 libpcre2 interp (2026-10-08) |
| 65.0 | altwide@0.3 libpcre2 jit (2026-10-02) |
| 61.3 | capability@0.2 pcrec vm-caps (255bcdd8) |
| 59.7, 57.6, 56.6, 54.4, 54.2 | just under: capability pcrec vm-in-caps, capability oniguruma, bounded vm-in-caps (751b9c6d), bounded vm-caps (751b9c6d), syntax pcre2-interp |

Five longest overall: 106.5, 71.9, 65.0, 61.3, 59.7 min. Cells in the 40-57
min range (capability 46-58 x 8, bounded 36-57 x 18, syntax 26-54 x 12,
utf8 28-42 x 13) make the sets, not any one cell, the night: capability,
bounded, syntax and utf8 are 39 of the 48.5 FULL hours.

## What could not be determined

- Whether the 106.5-min capability dfa cell ran under a raised cell cap: the
  record does not carry CELL_CAP; the window log is not in the repo.
- Per-trial wall time and compile-vs-match split of a cell's minutes: not in
  records (only counts and per-row timing ns inside the rows, which I did not
  read; summing them was out of scope and would miss harness/driver overhead).
- altwide@0.3 pcre2-interp: no cell exists. Its altwide@0.1 cell took 41.9
  min; +~45 min is a guess.
- Cells last measured on other nights/pins (bounded vm 54-57 min at
  751b9c6d, bounded clang siblings, altwide jit at 2026-10-02): minutes may
  differ at a current pin; the FULL roster also includes stale one-off
  configs (cc-clang, cf-align-functions-64, noisland, nolitrun, nohybreseed,
  noclsfold, dfa pcrec) which a re-baseline would likely drop; dropping
  them lowers FULL below 48.5 h (not quantified).
- The wall cost of sentinel passes, builds, quiet-gate waits and the rc=4
  re-measure (one set-wide re-run; the 1.5-min utf8 noreqhandoff cell of
  10-13 05:03 was an aborted attempt later redone at 34.8 min): only the
  sentinel pass is estimated (~33 min each), not a general factor.
- Load: all durations were on a quiet box (verdict `quiet`); a new box with
  more cores will not scale linearly (single-core pinned cells), so the
  scaling factor should come from a one-cell probe, not core ratio.
- The `utf8` rust entry is `rust_1.13.1_default-caps-simdna` (no `_utf8`
  id suffix); counted as the utf8 rust arm.
