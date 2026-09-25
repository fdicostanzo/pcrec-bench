# [B79] lane report: the null-control band + the class-aware interpreter rules ([B82] (ii))

Branch `lane/b79nullband`. Inputs, read in full before any code: plan rows
[B79]/[B82]; inbox I-93 block B, I-99, I-100, I-101 and I-104 (the
authority); `docs/dev/lanes/b82views_report.md` and `b85kb28_report.md`;
`pcrecbench/report.py`, `reduce.py`, `capture_class.py`, `interpret.py`;
`catalogue/CLAUDE.md`. I also read pcrec's cycle-2 reading §1 and
`b2ledger/nullctl.{py,json}` READ-ONLY, via `git show 4fe938ad:...`
against `~/pcrec` (nothing written there). The design of record is
**`docs/design/null_band_v1.md`**.

## 0. Findings a reader needs first

1. **The records carry NO program hash.** The brief said to take identity
   "from OUR OWN compile-row artifact/emit hashes — find where the records
   carry them". They don't carry them anywhere. `engine_metadata` has
   `emit_bytes`, `emit_code_bytes`, `artifact_bytes` and the stamps. None
   of these establishes identity:
   - every re-pin adds stamp lines, so every artifact's size moves by a
     pin-specific constant;
   - two different programs can share a size.

   I computed identity with our own tool instead. **`tools/program_identity.py`**
   re-emits every pattern × form at both pins using the SAME pinned binaries
   the records' `emit-c` phase ran (`build/pcrec-<pin>/build/pcrec`). Each
   config's flags are read FROM THE RECORD (`testee.build_flags`, refused
   if they differ across the pin). Pattern bytes are checked against the
   record's `canonical_sha256`. It then compares `.c` + `.h` after dropping
   only the generated-by line, the `.abi` integer and one-sided `#define`
   stamps.

   **PROPOSED FIX (OWED, a ruling; not built here, per the manager):** the
   pcrec adapter stamps a normalized `program_sha256` into each compile
   row's `engine_metadata`. That is a schema v1.6 minor plus a
   field-declaration row. The census would then become a cross-check and
   no re-emission would be needed.
2. **Our census agrees with pcrec's exactly: 192/192.** This is for
   8d716693 → b1885a83, three configs, plain form, against their darwin
   `nullctl.json`. The agreement is recorded in the census file's own
   header line.
3. **The band reproduces pcrec's published numbers to the digit.**
   - 8d716693 → b1885a83: throughput ≥1 µs **±8.77%**
     (`phone-palindrome-6`), throughput <100 ns **±41.09%**
     (`date-nested-plus`), search ≥1 µs **±11.16%** (`ipv4-near-miss`
     vm-in). These are the cycle2 reading §1's three numbers.
   - 25b1984f → 8d716693: throughput ≥1 µs **−5.74%..+8.46%**, which is
     O-48's two-sided cycle-1 band exactly.
4. **[B82]'s claim that IQR was "not computable" was wrong for set
   cells.** `reduce.SetCell.sums` has always carried the per-trial sums.
   The I-101 clearance column is now computed at set grain. At subject
   grain it says `IQR n/a`, and nothing is fabricated.
5. **A standing-query shape to rule on (not changed here).**
   `_cross_class_query_hits` ([B82]) compares any YES-class row against
   any `auto-nocaps` row in the same ranking group, ACROSS PINS. So on a
   cross-pin report, some hits are "old-pin caps beats new-pin nocaps":
   a pcrec regression, not a class anomaly. For example, on
   `router-prefix-order`/thr at after-b1885a83, 8d716693 auto-caps beats
   b1885a83 auto-nocaps by a 44.67% gap, and that hit CLEARS max(IQR,
   band). The v21 hit counts (350/343/357) mostly count
   pcrec-caps-vs-pcrec-nocaps near-ties. Most now read `within max(IQR,
   band)`, which is exactly what the clearance column exists to show.
   Whether the query should pair same-pin only is a ruling for
   Frank/the manager.

## 1. Charter-vs-committed checklist

| # | promise (brief) | artifact / status |
|---|---|---|
| 1a | per-window band from the PROGRAM-IDENTICAL population, our own identity | `tools/program_identity.py`; `reports/identity/capability@0.1/pcrec_{25b1984f__8d716693,8d716693__b1885a83,b1885a83__6ef76820}.tsv`; `report.py` `_build_null_band_model` (pairs = R8's own `_previous_pin_testee`, extracted) |
| 1b | nullctl.json only as a cross-check | 192/192 agree, in the census header |
| 1c | symmetric, banded by REGIME × BASELINE SCALE (≥1 µs / 100 ns–1 µs / <100 ns) | `pcrecbench/nullband.py` (`scale_bin`, `Stratum`: half-width = worst null cell, both signs) |
| 1d | band in the report header and per cell | md `## Null-control band` section + `D119 bar` column; TSV `null_band:` header key + `null_band`/`d119` rows |
| 1e | bar restated as \|Δ\| > max(IQR, null band) in each class-pure view | per-view line with its own counts (md); `d119_view` rows yes/no/mixed (TSV) |
| 1f | …and in the I-101 query's clearance column | `_query_clearance` (gap vs max(IQR, band), the band from the nocaps cell's own stratum) |
| 1g | an insufficient stratum stated, never a silent fallback; threshold chosen + justified | `N_MIN = 10`: P(one more null cell exceeds the max of n) = 1/(n+1) ≤ 9.1%. Rendered `insufficient (n=K < 10)` / `empty (n=0)`; verdicts `(IQR only: band n=K < 10)`. A pair with NO census renders `NO NULL BAND … <path>` and no verdicts |
| 2a | reporter v21 → v22 | `REPORTER_VERSION = "v22 (2026-09-25)"`, module-docstring `[B79]` section |
| 2b | tests, hand-computed fixture incl. an empty stratum | `test_b79_null_band_hand_computed` (ok/insufficient/empty, five verdict shapes incl. IQR > band, TSV rows) + two controls; `test_report` **96/96** |
| 2c | single-pin reports byte-identical except the version line, proved | §3 below: identical except the version line **and the I-101 clearance cells** (the brief's own item 1f moves them; nothing else moves) |
| 3a | class-aware D119 verdict rule + I-101 query-firing rule | `R-DELTA-5`, `R-STATUS-15` (`catalogue/rules.toml`, `pcrecbench/interpret.py`) |
| 3b | MINOR bump from 3.6 | catalogue **3.7** |
| 3c | fixtures (sabotage + control, one declared field apart) | `R-DELTA-5__regress-outside-band` / `__control-within-bar` (one `mutate`: every `d119` verdict → `within`); `R-STATUS-15__query-hit` / `__control-no-hit` (same slice, one `mutate`: the hit rows' recorded ratio → 1.000000, the query's own non-hit; the rule's predicate restates the strict `ratio < 1`); base = the v22 after-b1885a83 TSV (`report_e`); 75 fixtures |
| 3d | goldens | `catalogue/refresh_golden.py`: four files, +2 rows each (`R-STATUS-15`/`R-DELTA-5` `input-absent`), no existing fact moved; `acceptance_10.py` **25/25** |
| 3e | `make check-interpret` green | **199 passed, 0 failed** in the lane worktree (section 6 passed on the lane's last commit; the merge commit needs its approval line naming R-DELTA-5 and R-STATUS-15, since `template`/`no_fire`/`links` were added) |
| 4 | regenerate ONLY the three 2026-09-23 capability groups + sidecars, diff-proved | §2. The sidecar wave was necessarily WIDER than the three groups: a catalogue bump re-stamps EVERY committed sidecar (catalogue/CLAUDE.md, "every bump regenerates every committed sidecar"). `scripts/regen_sidecars.py`: 34 sidecars, 30 regenerated, and the 4 standing `capability-first` sidecars refused as before (blocked on the predictions ruling, `_SIDECARS_BLOCKED_ON_CAPABILITY_FIRST_RULING`, unchanged). Non-capability sidecars change only by the catalogue stamp and two did-not-fire rows each. No other report file was touched |
| 5 | `make check` once, after an OK from the manager | see §5 |
| 6 | CLAUDE.mds, design note, this report | `pcrecbench/CLAUDE.md`, `pcrecbench/tests/CLAUDE.md`, `catalogue/CLAUDE.md`, `tools/CLAUDE.md`, `reports/CLAUDE.md` (the `identity/` section), `docs/design/CLAUDE.md`; `docs/design/null_band_v1.md` |

## 2. The three regenerated groups: diff proof

Each group was re-rendered from its OWN committed query (the `- filters:`
line). Records were loaded once per group, and every format went through
`report.main()` exactly as the CLI would. The v22 files were then
NORMALIZED by removing only the [B79] additions:

- the band section;
- the per-view restatement lines;
- the `D119 bar` column;
- the TSV `null_band:` key and the `null_band`/`d119`/`d119_view` rows;
- the query clearance text, reset to v21's wording.

The result was compared line for line with the committed v21 file. Every
file came out **IDENTICAL**:

| group | .md | .tsv | .subject-grain.md | .subject-grain.tsv | .matrix.tsv |
|---|---|---|---|---|---|
| after-8d716693 (25b1984f→8d716693) | identical (21 band lines, 3 view lines, 3,280 D119 cells, 350 clearance) | identical (1 key, 7 band + 492 d119 + 3 view rows, 350 clearance) | identical (4 band lines, 13,803 clearance) | identical (13,803 clearance) | version line only |
| after-b1885a83 (8d716693→b1885a83) | identical (3,284 D119 cells, 343 clearance) | identical (494 d119 rows) | identical (12,717 clearance) | identical (12,717 clearance) | version line only |
| after-6ef76820 (b1885a83→6ef76820) | identical (2,718 D119 cells, 357 clearance) | identical (492 d119 rows) | identical | identical (13,416 clearance) | version line only |

The `.matrix.html` siblings were re-rendered with `scripts/matrix_page.py`.

## 3. Single-pin byte identity

The same query was rendered by master's v21 reporter (a `git archive`
copy) and by v22, then diffed line by line:

| report | md | tsv |
|---|---|---|
| 2026-09-21-loglines-0.1 fullroster-25b1984f | version 1 + query-clearance 23 | version 1 + query-clearance 23 |
| 2026-09-21-email-specimen-0.2 fullroster-25b1984f | version 1 + query-clearance 10 | version 1 + query-clearance 10 |
| 2026-09-22-capability-0.1 wrapfix-25b1984f (committed at v21) | version 1 + query-clearance 80 | version 1 + query-clearance 80 |

On every one of these reports, the only lines that move are the version
line and the I-101 clearance cells. There is no band section, no column
and no header key.

## 4. First reading (numbers only, no diagnosis)

Per pair: the null population and the per-view verdict counts over all
cross-pin cells (TSV `d119_view` rows).

| pair | null cells / cells | yes: improve/regress/within/null | no: improve/regress/within/null | IQR-only verdicts |
|---|---|---|---|---|
| 25b1984f→8d716693 | 143 / 492 | 187 / 32 / 50 / 98 | 36 / 21 / 23 / 45 | 74 |
| 8d716693→b1885a83 | 346 / 494 | 47 / 9 / 54 / 259 | 9 / 4 / 25 / 87 | 0 |
| b1885a83→6ef76820 | 390 / 492 | 26 / 18 / 24 / 299 | 15 / 5 / 14 / 91 | 0 |

Bands per stratum (thr = large-subject-throughput, srch =
short-subject-search):

| pair | thr ≥1µs | thr 100ns–1µs | thr <100ns | srch ≥1µs | srch 100ns–1µs | srch <100ns |
|---|---|---|---|---|---|---|
| 25b1984f→8d716693 | ±8.46% (n=65) | empty | insufficient n=7 | ±5.56% (n=65) | insufficient n=6 | empty |
| 8d716693→b1885a83 | ±8.77% (n=124) | insufficient n=6 | ±41.09% (n=45) | ±11.16% (n=108) | ±9.37% (n=63) | empty |
| b1885a83→6ef76820 | ±8.18% (n=158) | insufficient n=6 | ±29.68% (n=33) | ±7.07% (n=128) | ±11.85% (n=65) | empty |

`router-prefix-order`/thr at 8d716693→b1885a83 reads **+80.83% vs bar
8.77% (band) → regress** on the DFA route. On the VM route it reads
+9.89% / +9.69% → regress, the narrowest margin in the table. pcrec's
reading made the same two calls ("OUTSIDE, 9.2×" and "borderline,
1.13×").

## 5. Validation and what is OWED

**`make check`, run once in full after the manager's go (10:42–11:05
EDT, rc=0):**

| check | result |
|---|---|
| check-schema | 5 accepted / 73 rejected / 0 wrong |
| check-harness | 458 passed / 0 failed |
| check-report | test_report 96/0, test_quick 7/0, test_matrix_page 12/0 |
| check-interpret | 199 passed / 0 failed (sections 21/8/32/133/4/1) |

`catalogue/acceptance_10.py` (not part of `make check`): 25/25.
`tools/program_identity.py --check` re-derives each census deterministically
(no timestamps). The files were generated by the same code path.

OWED, each with an owner and a trigger:

1. **The merge commit's §8(6) approval line.** Owner: the manager, at
   merge. It must name R-DELTA-5 and R-STATUS-15; both rules add
   `template`/`no_fire`/`links` prose.
2. **A program hash on every compile row** (§0.1). Owner: Frank or the
   manager, as a ruling. Trigger: the next pcrec re-pin. Until then,
   every new cross-pin pair needs `tools/program_identity.py` run and its
   census committed BEFORE its report is rendered, or the report says
   `NO NULL BAND`.
3. **The standing query pairs across pins** (§0.5). Owner: Frank or the
   manager, as a ruling on [B82]'s query semantics: same-pin only, or
   keep it and mark the cross-pin hits.
4. **Other cross-pin report groups at v18–v21** (loglines, email,
   syntax, bounded, altwide after-25b1984f, capability pinconfirm).
   These are NOT regenerated, per the brief's scope. Owner: the window
   close that next regenerates them (KB-16). Trigger: their census files
   first. Those pairs have none, so a v22 render today would say `NO NULL
   BAND` for them.
5. **[B86]'s keyword IQR-flip re-read against the band** (plan row
   [B86]). Owner: that lane. The after-b1885a83 band for thr ≥1µs is
   ±8.77%. `keyword-prefix-order` thr regresses +59.6% on the DFA route
   (R-DELTA-5 fires; the sidecar lists it).
6. plan.md, the inbox/outbox and the journal were NOT touched, per the
   brief. Owner: the manager.

## 6. Symbols changed

- New: `pcrecbench/nullband.py`, `tools/program_identity.py`,
  `reports/identity/…` (3 files), `docs/design/null_band_v1.md`, 4
  fixture directories.
- `pcrecbench/report.py`: `_previous_pin_testee` (extracted from
  `_cross_pin_info`, behaviour-preserving); `_CensusFile`,
  `census_path_for`, `_PairBand`, `_CellD119`, `_NullBandModel`,
  `_null_band_model`/`_build_null_band_model`, `_d119_*`,
  `_null_band_header_lines`, `_null_band_tsv_header_value`,
  `_query_clearance`. `_cross_class_query_hits` gains an 8th tuple
  element (the clearance). `_NULL_BAND_NOT_COMPUTABLE` is retired.
- `pcrecbench/interpret.py`: `SECTIONS` + `null_band`/`d119`/`d119_view`;
  `HEADER_KEYS` + `null_band`; the new `CONDITIONAL_HEADER_KEYS`;
  `_kv_fields`, `r_status_15`, `r_delta_5`.
- `catalogue/check_interpret.py` and `acceptance_10.py`: the rule count
  is now 35, and the conditional header key is allowed to be absent.
