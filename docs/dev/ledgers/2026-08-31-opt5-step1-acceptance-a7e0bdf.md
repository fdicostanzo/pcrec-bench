# THE LEDGER — the [B25] [OPT-5] STEP 1 ACCEPTANCE window, pcrec pin `a7e0bdf` (bounded@0.2 AFTER vs the 263b013 BEFORE)

Read-only extraction by the ledger lane, 2026-08-31 (window ended
2026-09-01 UTC), against: the [OPT-4.1] ledger
(`docs/dev/ledgers/2026-08-31-opt41-after-263b013.md`, "the PRED" below —
its §12 checklist is this file's scorecard), inbox I-27's per-rung
predictions (the falsifiable frame, plan [B25]), and the re-pin's
compile-time facts (`testees/pcrec/CLAUDE.md`, "MEASURED at pin a7e0bdf").
Numbers only; the manager's interpretation goes to O-12.

**Ratio convention throughout: `A ÷ B`, so > 1 means A is SLOWER.**

---

## 0. SOURCES, SAMPLE SHAPE, HYGIENE

**This sample** (records committed at `c504ad9`; reports at `d750550`,
merged `8d9efa4`; reporter **v10 unchanged** — the [B25] lanes made no
reporter code change):

- `reports/2026-08-31-bounded-0.2-budu-ryzen1600-after-a7e0bdf.{md,subject-grain.md,tsv}`
  — cited `AFT:<line>` / `SG:<line>`. Query `--subbench bounded --version
  0.2 --until 2026-09-02`, **10 records included** (`AFT:9-19`): 2 pcre2 +
  4 `pcrec_263b013_*` + 4 fresh `pcrec_a7e0bdf_*`; 1 superseded
  (`AFT:20`, the [B22] window's vm-in first run). DELIBERATELY cross-pin
  (KB-5's dedup shape used on purpose): **the R8 `Δ vs previous version`
  column firing `a7e0bdf vs 263b013` IS the acceptance table** I-27 (2)
  asked for. Schema **1.4** on all ten, every ranked row `measured`,
  pass-rate 100 %, `n_wrong 0`.
- The 4 new records under `store/records/bounded@0.2/pcrec_a7e0bdf_*/`
  (cited REC) — every per-subject ratio in this file was RECOMPUTED from
  the records' timed rows (median of `elapsed_ns/iterations` over 5
  trials) and agrees with both committed renderings everywhere checked.

**Cells**: bounded@0.2 × `auto`/`nocaps`/`vm`/`vm-in` at a7e0bdf,
2026-08-31 21:46–23:15 EDT (record ids 20260901T014700Z–025303Z),
**4/4 measured on attempt 1** (one record per cell, no retry, no
superseded row from this window). Testee short names as the PRED's.

**Comparability**: same set version (bounded@0.2), same machine, same
reporter — the BEFORE/AFTER verdicts in this file are the reporter's own
R8 column wherever one exists, hand math (records) only at per-subject
grain. "Within spread" = the box's documented run-to-run band (the PRED
§0; pcre2 arms not re-measured here — their rows are the [B22] window's).

---

## 1. THE HEADLINE

**[OPT-5] STEP 1 is ACCEPTED on both axes of I-27 (2), and the flagged
`cls-upto-8192` inversion DOES NOT EXIST — it was a mis-reading, not a
measurement (§4).**

1. **Letters, per rung: `auto ÷ vm` fell from 3.65–6.05 to 1.76–2.00 at
   all nine counted rungs** — inside the predicted ~1.9–2.1 band at
   512–16384, BELOW it (better than predicted) at 64/128/256. No rung at
   or below 1.0 on a `selected` DFA: parity was not predicted and did not
   appear (the two-pass residual, I-27's own mechanism). pcrec's own
   find-all speedups reproduce on our driver: BEFORE÷AFTER on `auto` =
   **2.77–2.80× at {0,256}** (pcrec said 2.71×) and **3.01–3.04× at
   {0,16384}** (pcrec said 3.03×).
2. **Digits: direction and ceiling confirmed, "noise" refuted.** The
   ratio moved 0.565–0.596 → **0.596–0.604** because `auto` itself
   slowed ×1.04–1.06 on every digits cell (e.g. `t-digits-016k` at 1024:
   82,699 → 87,252 ns) while the `vm` control sat at ×0.998–0.999 —
   a systematic entry cost, inside I-27's stated 1.08× bound but visible
   above trial noise, not inside it.
3. **The size axis collapsed exactly as re-pinned**: the plain counted
   ladder's emitted source is FLAT 16,347–19,502 B at run time
   (was 21,045–724,699), `.so` flat 22,552–22,704 (was up to 219,120),
   three of the five warned forms silent. The whole-subject ladder did
   NOT collapse (its `byte-class-bounded` machines stamp
   `dfa_scan_edge=none`) — the two surviving warns are wholes (§6).
4. Off the ladder, the edge moved half the set: `auto` search sets
   ×1.50–2.24 faster down the ladder, `pw-8-64` ×1.85, `line-80` ×1.69,
   the nest hybrids' throughput ×1.57–1.59 — and a small regression
   family (year4 match ×1.07, dotted4 search ×1.11, lazy/digits ×1.04–
   1.06) that is the entry cost's honest face (§7).

---

## 2. THE STAMPS — routes unchanged, one new stamp everywhere it should be

**The `sel=` census is BYTE-IDENTICAL pin-to-pin** (auto-caps compile
rows, 60 pattern×form entries): `selected` 44, `collapsed-prefilter` 10
(ctx ×4 both forms + nest2-64/nest3-16 wholes, same exact-nfa whys
174/175/558×2/2094/2095, 8258, 8466), `declined-nullable` 4 (the I-21
DECLINE set exactly; legend `AFT:3825, 3831, 3836-3837`),
`did-not-compile` 2, `size-cap-retry` 0, every `vm`/`vm-in` artifact
`forced`. **[OPT-5] STEP 1 changed machines, not routes.**

**The new abi-13 `dfa_scan_edge` stamp, censused** (auto-caps, REC):
`range` 26 (all ten plain counted-class rungs incl. `cls-lazy-16384`
plain and `grp-upto-1024`; `cls-atleast-4096` BOTH forms — the only
whole that stamps range; `dotted4`/`nest2-4`/`nest2-64`/
`nest2-letters-6`/`nest3-16`/`nest3-3` both forms; `year4` plain),
`bitmap` 7 (`csv5`/`line-80`/`pw-8-64` both forms + `hex32` plain),
`none` 21 (ALL eight `cls-upto-*` wholes — the `byte-class-bounded`
prefilters take no run — the four ctx rungs both forms, `floor`,
`hex32`/`year4` wholes), **absent** 4 (the declined artifacts: no DFA
scan, the scope iff holds in the field). At 263b013 the key is absent on
all 58 compiled forms. The stamp is in every record but **rendered
nowhere** — KB-6, filed by the manager (`5740103`) before this ledger.

**K census unchanged**: `nest3-16` still the corpus's one K mover
(`K=1/size-model`, whole + both vm forms); everything else `K=8/default`,
caps 500,000/1,000,000. **VM artifacts byte-identical across pins**: all
58 compiled vm-caps forms have EQUAL `emit_bytes` at both pins (REC);
`.so` +40/+48 B uniformly on every artifact class — the abi-13 SHIM's own
scan-edge reader, bench-side (finding §9.4).

---

## 3. THE ACCEPTANCE FRAME (I-27 (2)), PER RUNG PER SUBJECT

`auto ÷ vm`, `large-subject-throughput`, plain form, recomputed from the
records (agrees with `SG:14260-14333`-style sub-tables everywhere):

| rung | l-004k | l-016k | l-064k | vs band ~1.9–2.1 | d-004k | d-016k | BEFORE letters (PRED §4) |
|---|---|---|---|---|---|---|---|
| 64 | 1.769 | 1.781 | 1.791 | **BELOW — overshoot** | 0.598 | 0.601 | 3.65–3.67 |
| 128 | 1.764 | 1.786 | 1.783 | **BELOW — overshoot** | 0.596 | 0.601 | 4.52–4.57 |
| 256 | 1.854 | 1.871 | 1.874 | below (marginal) | 0.601 | 0.601 | 5.13–5.21 |
| 512 | 1.921 | 1.930 | 1.939 | IN | 0.600 | 0.600 | 5.50–5.63 |
| 1024 | 1.952 | 1.966 | 1.967 | IN | 0.601 | 0.600 | 5.72–5.84 |
| 2048 | 1.979 | 1.975 | 1.982 | IN | 0.600 | 0.604 | 5.93–5.94 |
| 4096 | 1.975 | 1.989 | 1.993 | IN | 0.601 | 0.602 | 5.68–6.03 |
| 8192 | 1.967 | 1.993 | 2.000 | IN (**no inversion — §4**) | 0.601 | 0.602 | 5.57–6.05 |
| 16384 | 1.996 | 1.989 | 1.997 | IN | 0.601 | 0.604 | 5.13–6.04 |
| 32768 | 0.999 | 1.002 | 1.000 | parity-via-decline, expected | 1.000 | 0.995 | ~1.0 (declined) |

- **Nine of nine letters rungs confirm the prediction's direction and
  magnitude; three land BETTER than predicted** (1.76–1.87 at 64–256).
  **No rung ≤ 1.0 on a `selected` DFA** — nothing to lead with beyond
  the band; parity remains gated on the un-chartered two-pass fix.
- **The 32768 parity-via-decline is verified by stamps**: both forms
  `sel=declined-nullable`, `engine=vm`, no `dfa_scan_edge`, emit
  18,291/18,496 byte-identical to the BEFORE (§5.1) — `auto` IS a VM
  there; its ~1.00 is the decline, not STEP 1.
- **Mechanism, per byte** (REC): `auto` letters is NO LONGER FLAT —
  1.81–1.82 ns/B at 64 falling to 1.19 at 16384, i.e. the scan-edge DFA
  now shows the same 1/n match-count bend the VM always had (vm 1.01 →
  0.594 ns/B), so the RATIO is flat ~1.8–2.0 end to end. The BEFORE's
  signature (DFA flat 3.61–3.75 ns/B, ratio bending) is gone; the
  residual ×~2.0 is count-independent — consistent with I-27's "two-pass
  structure, a different mechanism".
- **Digits, absolutes** (rung 1024, REC): auto 20,666 → 21,815 (×1.056)
  and 82,699 → 87,252 (×1.055); vm 36,374 → 36,322 (×0.999) and
  145,748 → 145,528 (×0.998). Same ×1.04–1.06 at every rung, both auto
  arms, stddevs 30–430 ns on 21–87 µs cells — systematic, reproducible,
  ≤ the predicted 1.08×, and NOT what "within noise of the BEFORE"
  describes. Scored: **CONFIRMED in direction and ceiling; the noise
  wording refuted** (§7's regression family is the same term).
- **Adjacent, outside the nine-rung frame**: `cls-atleast-4096` letters
  fell 8.09–8.32 → **2.107–2.716** (set verdict `faster ×3.62`,
  `AFT:41-42`) — above the ladder band, descending with subject size; its
  digits ratio 0.072 at BOTH pins (the byte-class prefilter dismisses
  digit subjects; pin-invariant). It is the one shape whose WHOLE form
  also stamps `range` (+448 B emit, §6).

---

## 4. THE `cls-upto-8192` "ANOMALY" — RESOLVED: NO ANOMALY, A MIS-READING

The reports lane flagged (reports/CLAUDE.md entry; commit message
`8d9efa4`): letters `auto÷vm` ≈ 0.13, digits ≈ 1.77 at a7e0bdf, "the
store's own records disagree with the surrounding rungs".

**All three sources — the records, the set-grain per-subject table
(`AFT:1455-1508`), and the subject-grain tables (`SG:14260-14333`) —
agree with each other and with the neighboring rungs:**

| quantity | value at a7e0bdf | source |
|---|---|---|
| letters `auto ÷ vm` | 4,922.5/2,502.5 = **1.967**; 19,564.6/9,816.5 = **1.993**; 77,979.6/38,989.0 = **2.000** | `AFT:1479-1508`, REC |
| digits `auto ÷ vm` | 21,832.2/36,318.9 = **0.601**; 87,510.1/145,421.5 = **0.602** | `AFT:1459-1478`, REC |
| set-grain verdicts | auto `faster ×1.96-1.97`, vm `unchanged` | `AFT:1444-1449` |

The claimed numbers are not derivable as `auto ÷ vm` from any row of the
rung. They ARE derivable as reading slips on the committed tables:
**1.761×** is the `vs best` cell of the a7e0bdf `vm-caps` row in the
`t-digits-004k` sub-table, where "best" is the 263b013 AUTO row that
ranks first there (`SG:14268` — the digits sub-tables are the only ones
the OLD pin tops, which makes their `vs best` column look inverted); and
**0.1345** = a7e0bdf auto `t-letters-016k` 19,564.6 ÷ vm
`t-digits-016k` 145,421.5 — a cross-SUBJECT pairing.

**Stamps, for completeness** (§2, REC): the 8192 rung's route is
IDENTICAL in kind at both pins — plain `sel=selected`,
`dfa_match=search-filter` at BOTH pins (the PRED §6.1 already had 4096/
8192 plains at search-filter); whole `selected`/`search-filter` both
pins. The only pin-to-pin differences are `dfa_scan_edge=range` on the
plain and its emit 364,250 → 16,347 (`AFT:4255, 4263`). Nothing selected
differently; nothing to ask pcrec. **O-12 should carry this correction
explicitly so the flag does not propagate** (it is in a committed commit
message and reports/CLAUDE.md).

---

## 5. THE PRED §12 CHECKLIST, ITEM BY ITEM

| # | expectation (PRED §12) | measured at a7e0bdf | verdict |
|---|---|---|---|
| 1 | 8 declined cells `declined-nullable`, emit 18,291/18,496/18,615, `.so` 22,296–22,344, `auto = vm` within spread (search 834 / 4-subj thr 197,643 / match 742–748) | `declined-nullable` ×4 forms ×2 testees (`AFT:3825-3837`); emit **byte-identical**; `.so` 22,344–22,384 (**+40/+48 B = the abi-13 shim on every artifact**, §2 — not a pcrec move); search 845.9 vs vm 841.4 (**1.005**), 4-subj thr 196,509 vs 197,199 (**0.997**, 1.919 ns/B), match 742.9 vs 744.7 (**0.998**); 16384 whole 745.1, lazy whole 2,395.4 | **CONFIRMED** (shim note) |
| 2 | knee table 3.65–6.05 / DFA flat 3.61–3.75 ns/B; *"if the [OPT-5] fix lands, the letters targets are the `vm` column and these exact subjects"* | the fix LANDED: the conditional clause applies. Letters 1.76–2.00 vs the vm target line (0.594–1.03 ns/B) — gap ×~2.0, not parity; auto letters now 1.19–1.82 ns/B, no longer flat (§3). No selected-DFA rung < 1 | **SUPERSEDED BY THE PIN, scored under its own carve-out** |
| 3 | ctx search 8,125–8,352 / 8,828 / 8,831 / 6,335; `level-context`; nest wholes 876 / 1,688 flat, K=1 on nest3-16 | ctx search **8,109 / 8,818 / 8,821 / 6,357**, `auto ÷ vm` 0.325–0.401 (band 0.32–0.45 ✓); `level-context` NOT MEASURED (no loglines cells this window — next loglines sample inherits 263b013); nest wholes match **915.4 / 1,741.6** — `slower ×1.05 / ×1.04` by the reporter's own Δ; K=1/size-model kept | ctx **CONFIRMED**; nest **MOVED, flagged** — their hybrid prefilter DFAs now stamp `range` (§7.3), so this is a machine change, not pure spread |
| 4 | `grp-upto-1024` ≡ `cls-upto-1024` (+7 B emit, 0 ns) | emit 19,502/19,495 plain and 187,035/187,028 whole (**+7 B both forms**); `.so` identical 22,704 / 76,136; search 1,084.1 vs 1,083.3 (0.07 %); thr ratios ≤ 0.7 % | **CONFIRMED** — the equivalence survived a machine change |
| 5 | five warned forms at 364,250 / 372,262 / 471,172 / 724,699 / 937,216; no size-cap fire | **SUPERSEDED BY THE PIN**: the three PLAIN warns are GONE (364,250 → 16,347 `AFT:4263`; 372,262 → 18,138 `AFT:4087`; 724,699 → 16,352 `AFT:4135` — all silent); the two WHOLE warns remain at old+32 B: **471,204** (`AFT:4200`) and **937,248** (`AFT:4264` — still 93.7 % of the 1,000,000 cap, still the largest artifact, `.so` 284,832). No size-cap fire | **scored as superseded**; the cap's nearest customer is now a WHOLE-form problem (§6) |
| 6 | refusal bullets byte-identical; row untimed until KB-4 | `pattern too large (NFA exceeds 131072 states) (pattern offset 0)` on both forms both auto arms (`AFT:1395-1396, 1418-1419`); compile row carries no `cost`; `did-not-compile=1` | **CONFIRMED** — fourth pin, KB-4 still open |
| 7 | floors: auto 10.9 ns search / 0.0137–0.0169 ns/B memchr; vm 149.0 search / 2.665 miss | auto **10.9** / **0.0168** / thr floor 4-subj 1,612 (was 1,613); vm search **156.0–156.9** (+5 % — same drift as the ubiquitous vm `slower ×1.01` verdicts on 834→841 ns search sets), miss **2.661 ns/B** | **CONFIRMED** (vm search at the spread edge, direction noted) |
| 8 | match counts against the 1/n ladder | every match row `matched-as-expected` (9,425/9,425 on each auto arm, 9,750/9,750 on each vm arm, REC); pass-rate 100 %, `n_wrong 0` on every ranked row | **CONFIRMED** |

**Score: 6 CONFIRMED, 2 superseded by the pin exactly as the pin said
(items 2 and 5), 1 sub-item flagged (nest wholes' match, +3–5 %, a real
mechanism candidate — §7.3).**

---

## 6. THE SIZE HALF, FROM THE RECORDS (the acceptance's second axis)

Plain `auto` forms, `emit / code / .so` bytes, 263b013 → a7e0bdf (REC;
the compile table `AFT:3582-4536` renders the same numbers):

| rung | 263b013 emit/code/.so | a7e0bdf emit/code/.so |
|---|---|---|
| 64 | 21,045 / 12,399 / 26,760 | 19,481 / 14,468 / **22,704** |
| 128–512 | 24,886–47,971 / 12,400 / 26,760–34,952 | **19,488** / 14,475 / 22,704 |
| 1024, 2048 | 80,228 / 144,740 / 12,401 / 43,144–59,528 | **19,495** / 14,482 / 22,704 |
| 4096, 8192 | 185,828 / 364,250 / 11,588 / 71,664–120,816 | **16,347** / 13,007 / 22,552 |
| 16384 | 724,699 / 11,589 / 219,120 | **16,352** / 13,012 / 22,552 (silent, ×44) |
| lazy-16384 plain | 372,262 / 12,404 / 120,968 | **18,138** / 13,165 / 22,704 (silent) |
| atleast-4096 plain | 171,183 / 11,855 / 71,712 | **18,630** / 13,828 / 22,600 |
| grp-1024 plain | 80,235 / 12,408 / 43,144 | **19,502** / 14,489 / 22,704 |

- **The flat ~16.3–19.5 KB ladder is confirmed AT RUN TIME, byte-exact
  against the re-pin lane's compile-time table** (testees/pcrec/
  CLAUDE.md — all seven of its rows reproduce in the records).
- **Code bytes RISE +1.4–2.1 KB per rung** (12,399–12,408 → 14,468–
  14,489 unwrapped; 11,588 → 13,007 search-filter) — the edge's in-loop
  block is code where the deleted states were table, as re-pinned.
- **The WHOLE-subject ladder is untouched**: 31,074 / 40,996 / 61,312 /
  103,058 / 187,028 / 239,779 / 471,204 / 937,248 = the 263b013 values
  **+32 B each** (the stamp line; the two 16384-class wholes are
  declined). Their machines stamp `edge=none` — the run sits inside a
  `byte-class-bounded` prefilter the pass does not take. The [ART-SIZE]
  cap's 93.7 % near-miss therefore SURVIVES [OPT-5] STEP 1, on the whole
  form only. `cls-atleast-4096` whole is the exception: `range`, +448 B.
- **Compile TIME did not move** (I-27/re-pin, confirmed): 16384 plain
  7,074 ms median (emit-c 6,940 ms — **7 s of DFA construction for a
  16,352 B artifact**, `AFT:4135`); 8192 whole 8,822 ms (`AFT:4264`); the
  K7 declined wholes 1,945–2,041 ms vs the 32768 plain's ~194 ms
  state-cap bail — both overflow routes intact, [OPT-5] STEP 3's
  numerators unchanged.

---

## 7. BEYOND THE LADDER — where else the edge moved (the R8 census)

Every verdict below is the reporter's own Δ column on an a7e0bdf row.

### 7.1 The search axis — an unpredicted second win

`auto` short-subject-search sets: **faster ×2.23–2.25 at every rung
256–16384** (2,428 → 1,082–1,087 ns/set, e.g. `AFT:1547-1548`), ×1.92 at
128, ×1.50 at 64; `grp` ×2.24; `cls-atleast-4096` ×1.49–1.51. The auto
floor is unchanged (10.9 ns), so these are pattern-cell wins. I-27's
frame named only throughput; O-12 should report the search band as a
bonus confirmed axis.

### 7.2 Everyday-shape wins (auto, BEFORE→AFTER, records ×/reporter verdict)

`pw-8-64` search 4,354.7 → 2,351.1 (**×0.540**) and thr ×1.88–1.90
faster; `line-80` search 5,380.4 → 3,178.5 (×0.591); `hex32` search
×0.852, thr faster ×1.23; `csv5` search ×0.820; `nest2-64` thr faster
×1.59, search ×1.50; `nest3-16` thr ×1.57–1.58, search ×1.50;
`nest2-letters-6` thr ×1.59; `nest3-3` thr ×1.31; `nest2-4` thr ×1.19.
The bitmap witnesses (`pw-8-64`/`line-80`/`csv5`, §2) are among the
largest movers — the 256-byte membership edge pays off in the field.

### 7.3 The regression family — the entry cost's face

| cell | BEFORE → AFTER (auto) | reporter verdict | edge stamp |
|---|---|---|---|
| `year4` match whole | 322.9 → **346.4** (×1.073) | `slower ×1.08` | plain `range`, whole `none` |
| `year4` throughput | — | `slower ×1.09–1.11` (1.19 ns/B) | plain `range` |
| `dotted4` search | 2,405.5 → **2,672.2** (×1.111) | `slower ×1.11-1.12` | both forms `range` |
| `cls-lazy-16384` plain thr | — | `slower ×1.05-1.06` | plain `range` (the empty-match digit subjects: 4,097–65,537 scan-nothing calls) |
| digits ladder (§3) | ×1.04–1.06 every rung | (inside the ratio) | `range` |
| nest2-64 / nest3-16 whole MATCH | 874.2 → 915.4 / 1,683.3 → 1,741.6 | `slower ×1.05 / ×1.04` | hybrid prefilter now `range` — same artifacts' THR is ×1.59 faster |

One coherent family: cells whose calls scan little pay a fixed per-call
term, magnitude ×1.04–1.11 — I-27 predicted the term at ×1.08 on its
digits control. `year4` (×1.07–1.11 on a 4-count run) and `dotted4`
(×1.11) sit at or above the stated bound and are the asks' material
(§11 ii). The `vm` arms are flat everywhere (largest vm movement:
lazy search `slower ×1.09` on a 301.6 ns cell with emit byte-identical —
box spread, §9.6), so the family is DFA-side only.

---

## 8. THE v1.4 INSTRUMENT ROW

- **4/4 measured on attempt 1** — no exit-4, no retry, no superseded
  record from this window (c504ad9's store line: 71 measured / 9
  inconclusive-load / 1 inconclusive-spread, the 1 being [B22]'s).
  **Spread base rate updates to 1 per 13 window cells** (was 1/9, n now
  13 — the PRED §12 asked for the tracking).
- **Trial agreement**: `agree` on all four (`AFT:15-18`) — auto **3 of
  1,885 rows** disagreeing (0 of 87 groups; worst group `hex32`/search
  d=2 of 30), nocaps 2 rows, vm/vm-in 0. First window where disagreeing
  ROWS appear in a passing record's header line; the group rule absorbed
  them exactly as specified.
- **Pre-flight target-core busy** (REC `occupancy.before.target_busy_pct`):
  auto **5.21 %**, nocaps 2.01 %, vm 0.80 %, vm-in 0.80 %. **The 5.21 %
  is the first reading OUTSIDE the PRED's 0.4–2.6 % quiet band** (n was
  9) — the gate's limit is 10.0 % (gate_shape_v14 §1), the record stands
  `measured` and its trials agree, so per the PRED's rule the reading is
  the gate's business and the gate passed it. The box's observed quiet
  band is now **0.4–5.21 % (n=13)**. `/proc/stat` timeline present on
  all four; after-run `max_busy_pct` 2.4 % on the auto record.

---

## 9. ADAPTER / REPORTER / PROCESS FINDINGS

1. **KB-6 (already filed, `5740103`)**: the abi-13 `dfa_scan_edge` stamp
   is in every record's declaration block but no legend clause renders
   it — every `edge=` fact in this ledger came from the records, not the
   report. The mechanism legend (`AFT:3586+`) is otherwise complete.
2. **The 8192 flag was a reading error** (§4) and is embedded in
   committed prose (reports/CLAUDE.md entry, commit message `8d9efa4`).
   Process note for the manager: per-subject `vs best` columns invert
   visually wherever the OLD pin ranks first (all digits sub-tables);
   a ratio quoted from a cross-pin table needs its denominator's row
   named. O-12 carries the correction.
3. **The R8 Δ column as acceptance instrument WORKED**: KB-5's
   cross-pin dedup, used deliberately, produced the per-rung acceptance
   verdicts with zero new reporter code. The narrower testee-roster
   filter (KB-5's candidate fix) remains unbuilt and was not needed.
4. **`.so` +40/+48 B on EVERY artifact incl. byte-identical VM emits**
   (§2, REC) — the abi-13 shim's scan-edge reader, bench-side; keep it
   out of any pcrec-attributed size delta (same class of trap as the
   year4 ELF-page finding).
5. **The refused compile row still carries no `cost` object** — KB-4,
   fourth pin running.
6. **Largest vm-arm movement in the whole report**: `cls-lazy-16384`
   search `slower ×1.09` (301.6 ns set) on artifacts whose emit is
   byte-identical across pins — the ~300 ns set is below the box's
   resolution; recorded so the next sample reads it as spread, not
   movement.

---

## 10. RANKED OPTIMIZATION CANDIDATES (pcrec D86), UPDATED FROM PRED §10

**RETIRED — was 1. "The counted DFA loses the letters axis at every
rung."** SHIPPED as [OPT-5] STEP 1 and ACCEPTED here (§3): ×3.65–6.05 →
×1.76–2.00, three rungs better than predicted, size ×44 at the top rung.
The row does not close to zero — it RE-SCOPES:

**1. (new scope of the retired row) The two-pass residual.** `auto`
still trails its own VM ×1.76–2.00 on letters at every counted rung
(§3), count-independent, mechanism named by pcrec (the DFA's two-pass
structure) and explicitly un-chartered. The target line is measured: vm
0.594–1.03 ns/B on these exact subjects. Parity is this row.

**2. (was 2) The wasted DFA build under `auto`.** Now starker: 7.07 s
median compile (6.94 s emit-c) at `cls-upto-16384` plain **for a
16,352 B artifact** (§6); the K7 subset walks still 1.95–2.04 s on the
three declined wholes vs ~194 ms on the state-cap sibling; 8.82 s on the
8192 whole. All named as [OPT-5] STEP 3's territory by I-27 (3) —
unchartered, no ETA. Unchanged in total, waiting on STEP 3.

**3. (was 3) The end-anchored `search-filter` DFA** — untouched by STEP
1: whole match at 2048/4096/8192 still `auto ÷ vm` **6.93 / 6.97 / 6.95**
(REC; `AFT:1529-1532` for 8192). Three rungs, the [LIM-1]
`PCREC_ANCHORED_MAX_STATES`=4096 row, proposal status unchanged.

**4. (was 4) The 65535 refusal** — byte-identical at the fourth pin
(§5.6); I-27 (3) assigns it to STEP 3 (the caps fire during
construction, before the edge can act). Our row stays open as a
pcrec-side future; the day `check_mechanism_stamps`'s by-name assertion
fails with a compiled artifact is the day it lands.

**5. (was 5) `pcrec-vm` has no prefilter.** Unchanged: floor miss 2.661
ns/B vs auto's 0.0168 (§5.7); the ctx band's `auto ÷ vm` 0.325–0.401
persists — the forced VM is still not `auto`'s fallback.

**6. NEW. The scan-edge entry cost on scan-light cells** (§7.3):
×1.04–1.11 across digits/year4/dotted4/lazy, systematic, DFA-side only.
Small money, but `year4`/`dotted4` sit at or above I-27's stated ×1.08 —
a boundary question (ask ii) before it is an optimization row.

**7. (was 6) The nest/backtracking cliffs** — unchanged in kind; the
nest hybrids additionally gained thr ×1.57–1.59 and paid match ×1.04–1.05
from the edge on their prefilter DFAs (§7.3, ask v).

**Filed pcrec-side, tracked not ranked**: [OPT-4.2] (the O-10 cls-*
hybrid losers; population GROWN by [OPT-5]) — when it lands, our cls
hybrids re-measure at that pin. [M4-QUOTING] ships opt-in with no bench
surface until a set charters one.

---

## 11. ASKS (for O-12)

- **(i) The acceptance verdict + the correction.** Accepted per rung on
  both axes (§3/§6), with the 64/128 overshoot and the search-band bonus
  (§7.1); and the `cls-upto-8192` inversion flag is WITHDRAWN as a
  mis-reading (§4) — say so explicitly, it is in committed prose.
- **(ii) The entry-cost boundary.** `year4` (a 4-count run, `range`)
  pays ×1.07–1.11 and `dotted4` ×1.11 where the digits control was
  stated at ×1.08. Is the per-RUN edge selection (the boundary pcrec
  said it would explain — bounded `hex32` plain stamps `bitmap` while
  loglines `hex32-id` stays `none`) expected to take runs this short,
  and is the fixed term's size known? A skip-below-k-count knob may be
  cheaper than the term.
- **(iii) The whole-form ladder.** The `byte-class-bounded` wholes stamp
  `edge=none`, keep linear tables (§6), and now own both surviving
  warns incl. the 93.7 %-of-cap 937,248. Is a bounded-prefilter scan
  edge STEP 2's territory (period-k/string edge) or STEP 3's, and does
  [ART-SIZE]'s cap expect its first real customer there?
- **(iv) The two-pass charter.** §10 row 1: parity on letters needs the
  two-pass fix I-27 named as "not chartered". Does Frank charter it, and
  is this same 9-rung surface the acceptance instrument again? (We held
  the set stable; it discriminated exactly as designed.)
- **(v) The hybrid trade.** The nest wholes' prefilter DFAs gained the
  edge: thr ×1.57–1.59 faster, match ×1.04–1.05 slower (§7.3). Accepted
  trade or tunable? (Small; bundled with (ii) if one term explains both.)
- Carried unchanged: KB-4 (the refusal row's own cost — fourth pin);
  size-cap-retry stays witness-less by design (I-27 (5), closed).

---

## 12. WHAT THE NEXT SAMPLES ARE READ AGAINST

**The next bounded@0.2 sample (any future pin) must show:**

1. Letters `auto ÷ vm` **1.76–2.00** per rung with auto at 1.19–1.82
   ns/B (falling with rung — the 1/n bend now on BOTH engines) and vm at
   0.594–1.03. **A `selected`-DFA letters rung below 1.0 is the two-pass
   fix (or better) landing**; a return toward 3.6+ ns/B flat is the edge
   lost.
2. Digits **0.596–0.604** (auto 5.32–5.36 ns/B). A return to 0.565–0.570
   means the entry cost went away — credit it to whichever pin claims it.
3. The 4 declined forms: emit 18,291/18,496/18,615, search 834–846 /
   4-subj thr 196,509–197,643 (1.92–1.93 ns/B) / match 742–748 with
   `auto = vm` within spread; `.so` 22,344–22,384 under THIS shim.
4. ctx search 8,109–8,831 / 6,326–6,357 (ratios 0.32–0.41); nest wholes
   match **874–916 / 1,683–1,742** — the ×1.05 edge cost is now inside
   the band; a further step is movement. K=1/size-model on `nest3-16`.
5. `grp ≡ cls` at +7 B emit both forms / ≤ 0.7 % — through a machine
   change, twice now; a divergence is an emitter change.
6. The size ladder: plains flat 16,347–19,502 emit / 22,552–22,704 `.so`;
   wholes linear at old+32 B with exactly TWO warns (471,204 / 937,248);
   compile times ~flat (16384 plain ≈ 7.0 s, 8192 whole ≈ 8.8 s, K7
   wholes 1.95–2.04 s, 32768 plain ≈ 194 ms) until STEP 3 or [SEL-1.2].
7. Refusal diagnostic byte-identical; still untimed until KB-4; the
   by-name harness assertion is the STEP 3 tripwire.
8. Floors: auto 10.9 ns search / 1,612 thr / 0.0168 ns/B memchr; vm
   149–157 search / 2.66 ns/B miss.
9. Search sets: auto 691–692 at 64, 782–784 at 128, 1,082–1,087 at
   256–16384; `pw-8-64` 2,351 / `line-80` 3,178 / `hex32` 2,415–2,481 /
   `csv5` 803.
10. Pass-rate 100 % against the same 1/n oracle counts.

**Instrument expectations**: pre-flight target-core quiet band
**0.4–5.21 % (n=13, limit 10.0 %)**; disagreeing ROWS at 0–3 per record
with 0 groups is a passing shape; `inconclusive-spread` base rate 1 per
13 cells (n=1 — keep tracking). **The next loglines/email samples** still
score against their 263b013 / 96e44c2 baselines respectively (neither
set ran here); note loglines' `level-context` KEEP numbers were NOT
re-read at a7e0bdf and its hybrid carries a count-collapsed prefilter —
§7.3's edge-on-hybrid effect predicts its next sample may move a few
percent on match-shaped cells.
