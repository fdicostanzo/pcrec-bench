# Lane b95read — [B95] READ of `utf8@0.1`'s first sample at pcrec ce658cb7

Branch `lane/b95read`, worktree `worktrees/b95read`, from master 68f4455.
Lane type: WRITER, read-only against the store. No measurement was run and
nothing in `~/pcrec` was touched. Validation: `make check-interpret` **210
passed, 0 FAILED** (209 before this lane + section 3's freshness check on
the new sidecar). The sidecar determinism check passed: a re-run to stdout
is byte-identical to the file.

## The records read (every `utf8` row in `store/index.tsv`)

| testee | timestamp (UTC) | status |
|---|---|---|
| `rust_1.13.1_default-caps-simdna` | 2026-09-26T04:35:43Z | measured |
| `pcrec_ce658cb7_auto-caps-simdna_utf8` | 2026-09-26T05:06:57Z | measured |
| `pcrec_ce658cb7_auto-nocaps-simdna_utf8` | 2026-09-26T06:03:39Z | measured |
| `pcrec_ce658cb7_vm-caps-simdna_utf8` | 2026-09-26T07:07:03Z | measured |
| `pcrec_ce658cb7_vm-in-caps-simdna_utf8` | 2026-09-26T07:52:20Z | measured |
| `libpcre2_10.46_interp-caps-simdna_utf8` | 2026-09-26T09:44:37Z | measured |
| `libpcre2_10.46_jit-caps-simdna_utf8` | 2026-09-26T10:26:26Z | measured |
| `oniguruma_6.9.10_default-caps-simdna_utf8` | 2026-09-26T14:52:15Z | measured |
| `vectorscan_5.4.11_block-nosom-nocaps-simd_utf8` | 2026-09-26T15:31:03Z | measured |
| `libpcre2_10.46_dfa-nocaps-simdna_utf8` | 2026-09-26T16:10:00Z | measured |
| `re2_11.0.0_default-caps-simdna_utf8` | 2026-09-26T16:54:47Z (the KB-33 re-measure) | measured |

The query window 00:00Z-18:00Z covers all eleven and nothing else. The
report header reads `11 record(s) matching this query; records: 11;
excluded_invalid: 0; superseded: 0`. The brief's roster list names ten;
the eleventh, `pcre2-utf-interp`, is in the index and in the report.

## Deliverables

1. **Report group** (reporter v24), `reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7.*`:
   `.tsv` (3.6 MB), `.md` (2.3 MB), `.matrix.tsv`, `.matrix.html` (151 rows,
   11 testees), and the `.subject-grain.tsv` slice (16.3 MB). These are the
   five b91views lists: four renders + the matrix page. It was rendered in
   ONE store load with a scratch script that follows
   `scripts/regen_reports.py`'s per-group body: DETACHED, `gnutimeout
   3000`, DONE marker, 300 s wall, load 205 s. No `.subject-grain.md` was
   rendered because the brief's list does not include it. If wanted, it is
   one more render.
2. **Sidecar**: `…-first-ce658cb7.interpretation.md` (catalogue 3.9). **The
   predictions file LOADS** now that the re2/onig/vectorscan globs match
   measured testees; the finding from b91views is closed. Fired: R-STATUS-3
   18, R-STATUS-4 12, R-STATUS-8 1 (65.02% on pcre2-dfa `cls-neg-cjk`),
   R-STATUS-15 141, R-DELTA-4 365, R-ARM-1 324, R-ARM-2 8, R-FLOOR-1 435,
   R-FLOOR-2 212, R-FLOOR-3 82, R-PRED-1 5 (P2, P5, P6, P7, P11), R-PRED-2
   4 (P1, P3, P9, P10), R-PRED-4 1 (P4 partial),
   R-BUCKET-DOMINATED 1. Determinism byte-checked.
3. **Ledger**: `docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7.md`.
   Every P1-P11 clause is scored with its number and rows, and each verdict
   states what was read and what was not. P5.a, P9.b and R8 are scored from
   NOTES.md's pre-run prose over the `unsupported_by_pattern` section; they
   were not added to the first-sample file.
4. **Compile times** (pcrecdev1's ask):
   `docs/dev/measurements/2026-09-26-utf8-0.1-pcrec-compile-times.py` +
   `.txt`. The script has a source header; its verbatim output covers 589
   rows (config × pattern × form: median / min / max / spread, per-phase
   medians, engine / engine_sel / emit_bytes / warned). The ledger §6 sets
   it against O-58. The per-row numbers behind the other clauses are in
   `…-first-ledger-extract.py` + `.txt`.
5. **Outbox draft O-60**: below. The manager commits it.
6. **Second-sample predictions draft**:
   `docs/dev/predictions/utf8-0.1-second.tsv`. It has 7 clause rows: P5.a
   (20), P9.b (6), R8.a-e (onig 11 / re2 9 / rust 15 / vectorscan 4 / pcrec
   20). `stated_utc` is 2026-09-26T20:56:12Z, so this commit predates any
   second-sample run.
   - Load check: `interpret.load_predictions` 7/7 clean.
   - The CLI correctly REFUSES the file against the first-sample report
     (rc 2, §6.5 stated_utc).
   - Mechanics dry-run: a scratch copy re-dated to 00:00Z reads 3/3
     parents confirmed against the first sample.
   - Honesty note: every count is INFORMED by the first sample. The census
     is declaration-driven, so these clauses are drift checks, not
     independent predictions. `predictions/CLAUDE.md` says so.

Also: `docs/dev/upstream_findings.md` gains **U8** (RE2 `\B` between
the bytes of one UTF-8 character), **U9** (Oniguruma folds ß↔SS under
`(?i)`) and **U10** (Script vs Script_Extensions on four scripts × four
engines, with the separating code points verified: U+0301, U+3001/U+3002).
CLAUDE.md rows were added in `docs/dev/ledgers/`,
`docs/dev/measurements/`, `docs/dev/predictions/` and `reports/`.

## Findings for the manager (bench-side, not pcrec)

1. **The whole-subject wrap puts `(*UCP)` mid-pattern on vectorscan.**
   `(?:(*UCP)\w+)\z` is refused with "(*UCP) must be at start of
   expression, encountered at index 6". This happens on 5 whole-subject
   forms. No measured cell is affected, because utf8 has no `match`
   regime. A set that has a `match` regime and a leading verb would record
   spurious refusals. KB candidate: hoist leading `(*VERB)`s out of the
   wrap. pcre2 appears unaffected because it compiled no whole-subject rows
   here.
2. **Whole-subject artifacts are compiled for a set with no `match`
   regime.** They are never measured. On auto/nocaps this costs ~903 s
   (≈15 min) per cell (5 trials × 180.6 s of medians), 842 s of it
   `prp-l`/`prp-notl`'s whole forms. The rows are real compile data, so
   this is the manager's call and not a defect.
3. **The `ratio_to` reducer takes the UPPER median** of an even-sized
   denominator (`sorted(d)[len(d)//2]`). P7.b reads ×21.953 instead of the
   true-median ×22.29. There is no verdict effect. It is a documentation
   point for `predictions/CLAUDE.md` or interpreter_v1 §6.
4. **The sidecar's `min`/`max` over a multi-testee selector pools the
   testees into ONE value** ("worst min = 5.000 over 1 value(s)" for
   P11.a). "min over the four" as the note intends is not what it
   computes. The ledger checked each testee separately.
5. **P1 and P3 as transcribed could not see their own mechanism.** P1's
   effect is at throughput grain (×39.6 on `t-64k-lat`), where the set's
   short cells show ×1.13. P3's control is not a null, because the scanned
   byte of `lit-mixed-ascii` is `u`. A second-sample P1 at subject grain
   (`pattern=lit-offset-at-*;subject_or_na=t-64k-lat;grain=subject`) would
   read it. It is NOT added to the second-sample draft: the brief scoped
   that file to P5.a/P9.b/R8, and the number is already known.
6. **R2-R7 are not scored** (the brief scoped the ledger to P1-P11 + R8;
   R0/R1 were read because they carry the findings). A follow-up read of
   the same report group needs no measurement.

## DRAFT — O-60 (for `docs/dev/outbox_to_pcrec.md`; the manager commits it)

```
## O-60 (2026-09-26, pcrec-bench manager) — utf8@0.1's first sample at ce658cb7: per-pattern compile times (your ask), 0 wrong answers, and one scan-byte finding under `-e utf8`

The full 11-testee roster measured utf8@0.1 on 2026-09-26: 4 pcrec-*-utf8,
pcre2-utf-interp/-jit/-dfa, rust, re2-utf8, onig-utf8,
vectorscan-block-nosom-utf8. All 11 records are `measured`, at schema 1.7
and quiet. Ledger: docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7.md.
Report group: reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7.*.

1. CORRECTNESS: pcrec answers every row on all four configs (0 wrong of
   33,810 / 33,810 / 32,830 / 32,830 match rows). Bare \p{Greek} reads
   Script_Extensions exactly as libpcre2 does (P11.b, 12/12 cells). The
   engines that got answers wrong are other engines (upstream U8-U10).

2. COMPILE TIMES, per pattern, every pcrec utf8 config (your ask; table in
   docs/dev/measurements/2026-09-26-utf8-0.1-pcrec-compile-times.txt, 5
   trials, trial spread (max/min) <= 1.23 on every compiled row):
   - \p{L}+ on auto: 70.74 s plain / 106.41 s whole-subject. emit-c is
     70.44 / 106.10 s of that, on engine_sel size-cap-retry, emitting
     469,567 / 487,235 B (warned). \P{L}+: 41.32 / 62.27 s (emit-c 41.01 /
     61.96), 488,019 / 502,995 B. nocaps is identical to within 0.1%.
     O-58's one-trial rehearsal reproduces within 0.12%.
   - The forced VM REFUSES both patterns at the 500,000 B code cap in
     17-39 ms (1,115,105 / 1,118,091 B).
   - ^\p{L}{4}$ is refused on all four configs. auto refuses it in
     0.19-0.24 s (1,556,333 B of C > 1,000,000); the VM refuses it in
     0.03-0.04 s (2,224,587 B code). It never reaches a retry.
   - Everything else: median 0.161 s (auto) / 0.187 s (vm), p90 <= 0.38 s,
     98.7-99.0% of it gcc. The slowest non-L property is \p{Lu} forced-VM,
     2.90 / 3.56 s, all gcc (369,615 B, warned). \p{N}+ is 0.25 s on auto;
     the "0.07 s" in O-58 was emit-c only (0.058 s).
   - \p{L}+ and \P{L}+ are 112.1 of auto's 123.4 s of plain-form compile
     medians over 69 patterns.

3. THE SCAN BYTE UNDER -e utf8 (the set's largest pcrec speed finding,
   stamps + timings only, no cause asserted). On every artifact in this set
   that stamps RX_REQ_RUN, the run is scanned at index @0, and
   RX_REQ_BYTE is the run's FIRST byte. Where that byte is the dominant
   lead byte of the subject's own script, the memchr stops constantly:
   - é@ (lit-offset-at-tail): RX_REQ_BYTE 195 (0xC3), run c3a940@0.
     t-64k-lat: 43,690 ns vs @é's 1,103 ns (x39.6). rust-regex: 2,004 ns
     on the same cell, flat (x1.015 between the two orders). t-1m: x12.25
     (rust x1.013). On the cyr/cjk/asc 64 KB subjects the pair is x1.000.
   - Москва (lit-cyr-run): 208 (0xD0), run d09cd0bed181d0ba@0. The
     throughput set cell is x16.1 rust.
   - 日本語 (lit-run-3): 230 (0xE6). t-64k-cjk: 28,186 ns vs rust 2,391
     (x11.8).
   - user@例え.jp (lit-mixed-ascii): 117 ('u'), run 7573657240e4be8b@0 —
     the '@' four bytes in is not the one scanned. t-64k-asc: 19,241 ns vs
     rust 2,430 (x7.9). On the same subject lit-run-3 costs 1,105 ns.
   - Also: café (lit-nfc-pair) 99 'c', x7.21 rust; Straße (lit-sharp-s) 83
     'S', x4.38.
   Your I-95 text says [OPT-FREQPICK] is byte-encoding only; these stamps
   look like that restriction at work. Please confirm. THE ASK: a
   frequency-ranked scan-member pick under -e utf8. A UTF-8-aware prior
   would rank the dominant scripts' lead bytes (0xC3, 0xD0, 0xE3-0xE9) as
   COMMON; even the byte prior would pick '@' over 'u'. RE2 shows the same
   shape (é@ x23.7 on t-64k-lat); rust does not. 22 of the 138 pcrec-auto
   set cells lose to the best full-grain competitor by more than x2, and
   all 22 are throughput cells. The literal members listed above are 7 of them.
   Acceptance surface: bench/utf8's lit-* family at subject grain.

4. SMALLER READINGS (numbers only):
   - ci-moskva (?i)москва: RX_VM_CLS_FOLDS 0 on the VM, vs 3 on (?i)abc.
     The Cyrillic case pairs are not or-mask folded. Emitted code is still
     only x1.283 (vm) / x1.435 (auto) the ASCII control (our P4.a
     predicted >x1.5; refuted). Throughput is x2.70 rust.
   - The lookbehinds route vm-selected under auto and are the other
     non-literal losers: asr-lb-varwidth x8.15 and asr-lb-fixed x2.85
     pcre2-utf-jit; asr-lb-neg x3.38 onig.
   - prp-ingreek (\p{InGreek}) refuses with "module 'unicode-props' is
     enabled but \p{...}: this Unicode property is not implemented yet".
     libpcre2 refuses it too ("unknown property"), so the refusal is
     expected. Only the message's "yet" differs.
   - Our P7 (the property size cliff) is confirmed. prp-l's emit_bytes is
     x22.3 the lit-* median on auto/nocaps; vm/vm-in refuse it.
```

## Charter-vs-committed checklist

| # | brief promise | committed path / status |
|---|---|---|
| — | check the index, list every utf8 record included | this report, "The records read" (11) |
| 1 | the report group, five files + matrix page, `$Q` covering every utf8 record and nothing else | `reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7.{tsv,md,matrix.tsv,matrix.html,subject-grain.tsv}`, commit 03b7168 — DONE |
| 2 | the sidecar via the skill's procedure; it LOADS | `…-first-ce658cb7.interpretation.md`, commit after 03b7168; determinism byte-checked; `make check-interpret` 210/0 — DONE |
| 3 | the ledger, every P1-P11 clause + P5.a/P9.b/R8 from prose, read/not-read per verdict | `docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7.md` — DONE |
| 4 | per-pattern pcrec compile times, every pcrec utf8 config, against O-58; script + verbatim output with source header | `docs/dev/measurements/2026-09-26-utf8-0.1-pcrec-compile-times.{py,txt}`; ledger §6 — DONE |
| 5 | DRAFT outbox item O-60 in the lane report | this file, "DRAFT — O-60" — DONE (the MANAGER commits it to `outbox_to_pcrec.md`) |
| 6 | DRAFT `utf8-0.1-second.tsv` carrying P5.a/P9.b/R8, load-checked | `docs/dev/predictions/utf8-0.1-second.tsv` (7 rows, load 7/7, stated_utc 2026-09-26T20:56:12Z) — DONE |
| — | findings about other engines → upstream_findings.md rows | U8, U9, U10 — DONE |
| — | no new measurement runs | none run — the U10 code-point check was a libpcre2 compile/match over subject characters, not a timed run |
| OWED | R2-R7 of NOTES.md's outlier rule, not scored | owner: manager, who decides whether to charter a follow-up read of this same report group; trigger: before the second sample or with O-60, no measurement needed |
| OWED | plan.md `[B95]` STATE row + dev_journal entry | owner: manager (lanes do not edit plan.md/journal); trigger: the merge |
