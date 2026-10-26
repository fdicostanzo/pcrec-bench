# b138rep -- report wave, [B138] re-baseline at pcrec 6b2dbd3e (abi 76), ryzen7700x

Branch lane/b138rep. Reporter v28. No timing, no store write; renders only (nice 10, detached, sequential, one at a time).

## Commands

Driver (scratch, not committed): /var/tmp/pcrecbench/b138rep/gen.py -- b142rep's gen.py with the group table, window and name suffix changed; chain /var/tmp/pcrecbench/b138rep/chain.sh, log `log`, ended `DONE all`, every group rc=0, no warning/refusal/traceback in the log. Per group, CLI-equivalent:

    pcrecbench report --subbench <set> --version <ver> --machine ryzen7700x \
      --since 2026-10-19T03:50:00Z --until 2026-10-20T11:00:00Z [--grain set|subject]

No `--testee` filter: the window holds only the intended roster (checked against store/index.tsv before rendering), all at 6b2dbd3e. Sidecars (/var/tmp/pcrecbench/b138rep/side.sh), from the worktree root, no `--predictions`, `--subject-grain` where the slice exists, then re-rendered to stdout and `cmp`'d:

    python3 -m pcrecbench interpret reports/<name>.tsv --index store/index.tsv [--subject-grain reports/<name>.subject-grain.tsv] --render --out reports/<name>.interpretation.md

Determinism: identical for all 9 groups (side.log `DET <set> identical`, `DONE side`).

## Files

52 files in reports/, base `2026-10-26-<set>-ryzen7700x-rebaseline-6b2dbd3e`: for email-specimen-0.2, loglines-0.1, altwide-0.3, bounded-0.3, litrun-0.1, capability-0.2, syntax-0.1, utf8-0.1: `.tsv .md .matrix.tsv .subject-grain.md .subject-grain.tsv .interpretation.md`; sentinel-0.1: `.tsv .md .matrix.tsv .interpretation.md`. Plus reports/CLAUDE.md entry.

## Record counts (from each .tsv header)

| group | index rows matched | records used | superseded | roster |
|---|---|---|---|---|
| email-specimen-0.2 | 6 | 6 | 0 | jit, interp, rust, P6 auto-caps/auto-nocaps/vm-caps |
| loglines-0.1 | 6 | 6 | 0 | same |
| altwide-0.3 | 6 | 6 | 0 | same |
| bounded-0.3 | 6 | 6 | 0 | same |
| litrun-0.1 | 5 | 5 | 0 | same minus rust |
| syntax-0.1 | 6 | 6 | 0 | same as email |
| utf8-0.1 | 9 | 9 | 0 | jit/interp/onig/re2/vectorscan nosom (all _utf8), rust, P6 auto-caps/auto-nocaps/vm-caps (_utf8) |
| capability-0.2 | 12 | 10 | 2 | jit, interp, onig, re2, rust, tre, vectorscan nosom, P6 auto-caps/auto-nocaps/vm-caps |
| sentinel-0.1 | 14 | 3 | 11 | jit, P6 auto-caps, P6 auto-nocaps (sentinel ran repeatedly; newest per testee kept, all `measured`; the older jit records included two `inconclusive-spread`; not checked per regime) |

Header facts: `excluded_invalid: 0`, `newer_not_measured: 0` everywhere; no `null_band` line (one pin, as expected), no identity census written.

capability-0.2 superseded 2: P6 auto-caps and auto-nocaps each had two `inconclusive-spread` records (4 total); newest-wins kept one of each, and THE KEPT ONES ARE STILL `inconclusive-spread` (137 / 139 `not_ranked` rows). So in capability-0.2 pcrec auto-caps/auto-nocaps are not ranked and not in the matrix as numbers (cells `excluded`): no slower-than-best table is possible for them. vm-caps is measured there. Reason for the spread and whether the re-measure fired as designed: not read.

Refusals/warnings by name: none from the reporter or interpret.

## Where pcrec_6b2dbd3e auto is slower than the best non-pcrec testee

Source: each `.matrix.tsv`; value = cell ratio x the row's `best_ns_pooled` (absolute median_ns), compared with the lowest non-pcrec, non-vectorscan cell that is a measured number in that row (cells `excluded`/`unsup`/`refused`/`gave-up` skipped). Ratio = pcrec median / that best. Vectorscan block-nosom is EXCLUDED everywhere (I did not determine which rows have all-no-match subjects, so no row re-admits it; in capability/utf8 it might be faster on some rows). Only ratios >= 1.10 are listed; both auto columns on one line (caps / nocaps). Regime abbreviated: large = large-subject-throughput, short = short-subject-search, mc = match-compliance. Columns: pattern | regime | form | ratio | pcrec ns vs best ns | best testee. Cells compared: email 16, loglines 44, litrun 56, bounded 248, altwide 214, syntax 412, utf8 276, sentinel 30, capability 0.

### email-specimen-0.2
(email-specimen-0.2 comparable pcrec-cells 16 slower>1.10 cells 0 rows 0)

### loglines-0.1
(loglines-0.1 comparable pcrec-cells 44 slower>1.10 cells 12 rows 6)
| level-context | large-throughput | plain | caps x3.78 / nocaps x3.81 | 1189600 vs 314496 | rust_default |
| level-context | short-search | plain | caps x3.12 / nocaps x3.10 | 40778 vs 13091 | rust_default |
| stack-frame | large-throughput | plain | caps x3.08 / nocaps x3.08 | 608811 vs 197808 | libpcre2_jit |
| stack-frame | short-search | plain | caps x3.06 / nocaps x3.06 | 18760 vs 6123 | rust_default |
| iso-ts | large-throughput | plain | caps x1.21 / nocaps x1.22 | 326438 vs 269147 | libpcre2_jit |
| iso-ts | short-search | plain | caps x1.17 / nocaps x1.17 | 12021 vs 10295 | libpcre2_jit |

### litrun-0.1
(litrun-0.1 comparable pcrec-cells 56 slower>1.10 cells 14 rows 7)
| alt-foo-tails | large-throughput | plain | caps x7.86 / nocaps x7.86 | 334520 vs 42567 | libpcre2_jit |
| wild-secrets-aws-access-key-id | large-throughput | plain | caps x2.63 / nocaps x2.63 | 229770 vs 87242 | libpcre2_jit |
| lit-l40 | large-throughput | plain | caps x2.27 / nocaps x2.27 | 175119 vs 77092 | libpcre2_jit |
| lit-l31 | large-throughput | plain | caps x1.81 / nocaps x1.81 | 275979 vs 152470 | libpcre2_jit |
| lit-l8 | large-throughput | plain | caps x1.77 / nocaps x1.77 | 1420769 vs 803236 | libpcre2_jit |
| lit-l16 | large-throughput | plain | caps x1.49 / nocaps x1.49 | 420576 vs 282686 | libpcre2_jit |
| lit-l7 | large-throughput | plain | caps x1.36 / nocaps x1.37 | 1611145 vs 1182201 | libpcre2_jit |

### bounded-0.3
(bounded-0.3 comparable pcrec-cells 248 slower>1.10 cells 32 rows 16)
| ctx-lazy-64 | large-throughput | plain | caps x19.74 / nocaps x19.70 | 102802 vs 5208 | rust_default |
| ctx-lazy-256 | large-throughput | plain | caps x19.61 / nocaps x19.52 | 102638 vs 5235 | rust_default |
| ctx-lazy-1024 | large-throughput | plain | caps x19.41 / nocaps x19.26 | 102818 vs 5298 | rust_default |
| ctx-greedy-256 | large-throughput | plain | caps x19.00 / nocaps x19.07 | 99320 vs 5227 | rust_default |
| cls-atleast-4096 | short-search | plain | caps x7.55 / nocaps x7.55 | 1248 vs 165 | rust_default |
| cls-atleast-4096 | mc | whole-subject | caps x6.79 / nocaps x6.79 | 1195 vs 176 | rust_default |
| line-80 | large-throughput | plain | caps x2.01 / nocaps x2.01 | 40431 vs 20079 | libpcre2_jit |
| ctx-lazy-64 | short-search | plain | caps x1.96 / nocaps x1.96 | 3263 vs 1667 | rust_default |
| pw-8-64 | large-throughput | plain | caps x1.57 / nocaps x1.58 | 87060 vs 55293 | libpcre2_jit |
| line-80 | short-search | plain | caps x1.21 / nocaps x1.21 | 1632 vs 1346 | libpcre2_jit |
| floor | mc | whole-subject | caps x1.16 / nocaps x1.16 | 215 vs 185 | rust_default |
| ctx-lazy-256 | short-search | plain | caps x1.14 / nocaps x1.14 | 3522 vs 3095 | libpcre2_jit |
| cls-atleast-4096 | large-throughput | plain | caps x1.13 / nocaps x1.13 | 40606 vs 36049 | libpcre2_jit |
| ctx-lazy-1024 | short-search | plain | caps x1.12 / nocaps x1.12 | 3522 vs 3138 | libpcre2_jit |
| ctx-greedy-256 | short-search | plain | caps x1.10 / nocaps x1.10 | 2850 vs 2585 | libpcre2_jit |
| pw-8-64 | short-search | plain | caps x1.10 / nocaps x1.10 | 1384 vs 1258 | libpcre2_jit |

### altwide-0.3
(altwide-0.3 comparable pcrec-cells 214 slower>1.10 cells 44 rows 22)
| w-8 | large-throughput | plain | caps x25.02 / nocaps x25.30 | 1188276 vs 47499 | rust_default |
| nar4-64 | large-throughput | plain | caps x4.67 / nocaps x4.75 | 983081 vs 210504 | rust_default |
| w-64 | large-throughput | plain | caps x2.12 / nocaps x2.12 | 2019754 vs 954908 | rust_default |
| cnt-64 | large-throughput | plain | caps x2.07 / nocaps x2.07 | 1966790 vs 951040 | rust_default |
| clsa-64 | large-throughput | plain | caps x2.05 / nocaps x2.05 | 1939620 vs 945656 | rust_default |
| w-8 | short-search | plain | caps x2.00 / nocaps x2.04 | 2102 vs 1052 | rust_default |
| clsd-64 | large-throughput | plain | caps x1.87 / nocaps x1.87 | 1941359 vs 1036492 | rust_default |
| wb-512 | large-throughput | plain | caps x1.83 / nocaps x1.83 | 2216580 vs 1210543 | rust_default |
| w-96 | large-throughput | plain | caps x1.69 / nocaps x1.69 | 1844506 vs 1092003 | rust_default |
| w-128 | large-throughput | plain | caps x1.62 / nocaps x1.62 | 1834830 vs 1129142 | rust_default |
| wb-256 | large-throughput | plain | caps x1.56 / nocaps x1.55 | 1725454 vs 1109497 | rust_default |
| w-192 | large-throughput | plain | caps x1.50 / nocaps x1.49 | 1832914 vs 1223163 | rust_default |
| s-256 | large-throughput | plain | caps x1.43 / nocaps x1.43 | 1694830 vs 1183182 | rust_default |
| srt-256 | large-throughput | plain | caps x1.40 / nocaps x1.40 | 1700893 vs 1211142 | rust_default |
| w-256 | large-throughput | plain | caps x1.40 / nocaps x1.40 | 1697912 vs 1210813 | rust_default |
| w-512 | large-throughput | plain | caps x1.35 / nocaps x1.34 | 2135859 vs 1587769 | rust_default |
| srt-512 | large-throughput | plain | caps x1.33 / nocaps x1.33 | 2135127 vs 1607784 | rust_default |
| w-384 | large-throughput | plain | caps x1.26 / nocaps x1.26 | 1756317 vs 1391243 | rust_default |
| floor | mc | whole-subject | caps x1.24 / nocaps x1.24 | 180 vs 145 | rust_default |
| s-2048 | short-search | plain | caps x1.17 / nocaps x1.17 | 7191 vs 6141 | rust_default |
| s-512 | large-throughput | plain | caps x1.15 / nocaps x1.15 | 1839603 vs 1592941 | rust_default |
| clsa-64 | short-search | plain | caps x1.14 / nocaps x1.14 | 4675 vs 4091 | rust_default |

### sentinel-0.1
(sentinel-0.1 comparable pcrec-cells 30 slower>1.10 cells 0 rows 0)

### syntax-0.1
(syntax-0.1 comparable pcrec-cells 412 slower>1.10 cells 87 rows 44)
| esc-nl | large-throughput | plain | caps x5.35 / nocaps x5.35 | 110857 vs 20734 | rust_default |
| cls-s-lc | large-throughput | plain | caps x4.60 / nocaps x4.60 | 352747 vs 76666 | rust_default |
| lkb-pos | large-throughput | plain | caps x4.14 / nocaps x4.14 | 262316 vs 63400 | libpcre2_jit |
| anc-m-dollar | large-throughput | plain | caps x4.09 / nocaps x4.04 | 235680 vs 57597 | rust_default |
| asr-wb | large-throughput | plain | caps x4.02 / nocaps x4.03 | 472183 vs 117325 | libpcre2_jit |
| asr-nwb | large-throughput | plain | caps x3.94 / nocaps x3.94 | 467231 vs 118672 | libpcre2_jit |
| lka-verb | large-throughput | plain | caps x3.69 / nocaps x3.69 | 204627 vs 55473 | libpcre2_jit |
| lka-pos | large-throughput | plain | caps x3.68 / nocaps x3.68 | 203925 vs 55352 | libpcre2_jit |
| grp-atomic-alt | large-throughput | plain | caps x3.41 / nocaps x3.40 | 534943 vs 157098 | libpcre2_jit |
| mod-x | large-throughput | plain | caps x3.25 / nocaps x3.23 | 322859 vs 99403 | rust_default |
| esc-hex | large-throughput | plain | caps x3.23 / nocaps x3.24 | 322518 vs 99887 | rust_default |
| lit-cat | large-throughput | plain | caps x3.21 / nocaps x3.21 | 321090 vs 100127 | rust_default |
| mod-s | large-throughput | plain | caps x3.01 / nocaps x3.14 | 160359 vs 53268 | rust_default |
| esc-octal-0 | large-throughput | plain | caps x2.70 / nocaps x2.92 | 148747 vs 55028 | libpcre2_jit |
| lkb-neg | large-throughput | plain | caps x2.91 / nocaps x2.91 | 332788 vs 114221 | libpcre2_jit |
| cls-v | large-throughput | plain | caps x2.88 / nocaps x2.78 | 164826 vs 57312 | libpcre2_jit |
| alt-nested | large-throughput | plain | caps x2.52 / nocaps x2.54 | 1032084 vs 408873 | rust_default |
| cls-n-uc | large-throughput | plain | caps x2.52 / nocaps x2.52 | 270316 vs 107225 | libpcre2_jit |
| alt-two | large-throughput | plain | caps x2.38 / nocaps x2.40 | 962398 vs 405033 | rust_default |
| qnt-quest | large-throughput | plain | caps x2.34 / nocaps x2.33 | 298462 vs 127787 | libpcre2_jit |
| anc-m-caret | large-throughput | plain | caps x2.16 / nocaps x2.17 | 127127 vs 58987 | libpcre2_jit |
| bak-k-named | large-throughput | plain | caps x2.12 / nocaps x2.12 | 419349 vs 197865 | libpcre2_jit |
| mod-r | large-throughput | plain | caps x2.11 / nocaps x2.11 | 506303 vs 239529 | libpcre2_jit |
| mod-i | large-throughput | plain | caps x2.08 / nocaps x2.08 | 506156 vs 243707 | libpcre2_jit |
| lka-neg | large-throughput | plain | caps x2.05 / nocaps x2.05 | 223961 vs 109193 | libpcre2_jit |
| lka-nonatomic | large-throughput | plain | caps x1.89 / nocaps x1.88 | 205654 vs 109012 | libpcre2_jit |
| cls-dot | large-throughput | plain | caps x1.83 / nocaps x1.84 | 355848 vs 194020 | libpcre2_jit |
| mod-unset | large-throughput | plain | caps x1.83 / nocaps x1.82 | 494791 vs 270908 | rust_default |
| qnt-poss-quest | large-throughput | plain | caps x1.72 / nocaps x1.74 | 916596 vs 532011 | libpcre2_jit |
| cls-fold-pair | large-throughput | plain | caps x1.67 / nocaps x1.67 | 328683 vs 197125 | libpcre2_jit |
| cls-i-class | large-throughput | plain | caps x1.65 / nocaps x1.64 | 695102 vs 421170 | rust_default |
| mod-reset | large-throughput | plain | caps x1.50 / nocaps x1.49 | 494440 vs 330618 | libpcre2_jit |
| mod-j-uc | large-throughput | plain | caps x1.49 / nocaps x1.49 | 10294181 vs 6910001 | libpcre2_jit |
| cls-pair-ctl | large-throughput | plain | caps x1.48 / nocaps x1.47 | 328411 vs 222307 | rust_default |
| mod-n | large-throughput | plain | caps x1.44 / nocaps x1.44 | 321762 vs 223967 | libpcre2_jit |
| grp-named-quote | large-throughput | plain | caps x1.44 / nocaps x1.39 | 332471 vs 231567 | libpcre2_jit |
| grp-cap | large-throughput | plain | caps x1.43 / nocaps x1.38 | 331735 vs 232027 | libpcre2_jit |
| grp-named | large-throughput | plain | caps x1.43 / nocaps x1.38 | 332447 vs 233243 | libpcre2_jit |
| mod-j-uc | short-search | plain | caps x1.39 / nocaps x1.39 | 3852 vs 2764 | libpcre2_jit |
| floor | mc | whole-subject | caps x1.23 / nocaps x1.28 | 186 vs 152 | rust_default |
| esc-quote | large-throughput | plain | caps x1.22 / nocaps x1.22 | 55362 vs 45555 | libpcre2_jit |
| cls-h | large-throughput | plain | caps x1.19 / nocaps x1.19 | 62262 vs 52371 | libpcre2_jit |
| qnt-quest | mc | whole-subject | caps x1.16 / nocaps x1.16 | 193 vs 167 | rust_default |
| bak-2 | large-throughput | plain | caps x1.11 | 5602203 vs 5053914 | libpcre2_jit |

### utf8-0.1
(utf8-0.1 comparable pcrec-cells 276 slower>1.10 cells 36 rows 18)
| alt-distinct-lead | large-throughput | plain | caps x14.11 / nocaps x14.09 | 1340026 vs 94990 | rust_default |
| lit-sharp-s | large-throughput | plain | caps x13.88 / nocaps x13.86 | 316253 vs 22790 | re2_utf8 |
| ci-sigma | large-throughput | plain | caps x7.96 / nocaps x7.96 | 314637 vs 39524 | rust_default |
| lit-offset-at-head | large-throughput | plain | caps x6.35 / nocaps x6.34 | 72982 vs 11493 | re2_utf8 |
| asr-b-ascii | large-throughput | plain | caps x5.95 / nocaps x5.94 | 171133 vs 28773 | rust_default |
| ci-moskva | large-throughput | plain | caps x5.25 / nocaps x5.24 | 691796 vs 131879 | rust_default |
| ci-kelvin | large-throughput | plain | caps x2.81 / nocaps x2.88 | 380609 vs 135425 | rust_default |
| lit-nfc-pair | large-throughput | plain | caps x2.75 / nocaps x2.75 | 76416 vs 27769 | rust_default |
| lit-1ch-4b | large-throughput | plain | caps x2.73 / nocaps x2.72 | 66482 vs 24388 | re2_utf8 |
| qnt-bounded-4b | large-throughput | plain | caps x2.37 / nocaps x2.36 | 58506 vs 24705 | rust_default |
| cls-dot-rep | large-throughput | plain | caps x2.30 / nocaps x2.31 | 61 vs 27 | rust_default |
| ci-strasse | large-throughput | plain | caps x2.27 / nocaps x2.27 | 240536 vs 105942 | rust_default |
| ci-ascii-control | large-throughput | plain | caps x2.24 / nocaps x2.24 | 130146 vs 58175 | rust_default |
| qnt-counted-3b | large-throughput | plain | caps x1.43 / nocaps x1.42 | 36782 vs 25683 | rust_default |
| lit-cyr-run | large-throughput | plain | caps x1.38 / nocaps x1.37 | 32526 vs 23530 | rust_default |
| ci-turkish-i | large-throughput | plain | caps x1.26 / nocaps x1.30 | 672748 vs 533402 | rust_default |
| alt-nearmiss | large-throughput | plain | caps x1.25 / nocaps x1.25 | 36603 vs 29286 | rust_default |
| lit-1ch-3b | large-throughput | plain | caps x1.23 / nocaps x1.22 | 52171 vs 42510 | rust_default |

### capability-0.2
(capability-0.2 comparable pcrec-cells 0 slower>1.10 cells 0 rows 0)

email-specimen-0.2: none >= 1.10 (the only slower cells are `floor` whole-subject, x1.01 caps / x1.04 nocaps vs rust). sentinel-0.1: none >= 1.10 (roster has only jit as non-pcrec). Smaller (1.00-1.10) slower cells are in the .matrix.tsv, not listed.

## What I did NOT read

The .md renderings, subject-grain files and interpretation sidecars' content (only rc and the determinism result); the `compile`, `compile_stamp`, `d119` rows and any compile-size/time data; status of non-pcrec records beyond the index; why capability's pcrec auto records are inconclusive-spread; why sentinel was run repeatedly; slower cells < x1.10; any class-pure column (best_ns_yes/no) -- I compared against non-pcrec caps-class testees only (all of them are `-caps`; auto-nocaps is therefore compared across classes); the vm-caps column (not asked); no cause is interpreted.

## Charter vs committed

1. Nine groups `2026-10-26-<set>-<ver>-ryzen7700x-rebaseline-6b2dbd3e.*`, filters as briefed: committed.
2. Files per group as b142rep's (tsv/md/matrix, subject-grain md+tsv for the eight set groups, sentinel without): committed.
3. Sidecars + determinism re-run, 9 of 9: committed.
4. reports/CLAUDE.md entry: committed.
5. This report with counts, tables, did-not-read: committed.
6. Identity census: not written (no pin pair), as briefed. Not run: make check-report / regen_reports.py equivalence (not asked).
