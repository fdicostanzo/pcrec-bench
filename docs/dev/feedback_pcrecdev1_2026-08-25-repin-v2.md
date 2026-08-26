# Feedback on the FINAL re-pin report (reporter v2) — from the pcrec manager session (pcrecdev1), 2026-08-25 ~19:xx EDT

Verbatim in substance (lightly re-wrapped). Read from
reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.md at
master 7db0519 ALONE (all six 692c2e8 cells `measured`; reporter v2).
Second of two readings (the first: feedback_pcrecdev1_2026-08-25-repin.md).

## (1) CHARTABILITY NOW

- **[OPT-1] vm-in vs vm: CHARTABLE as printed** — the compile-cost
  table's `entry` (plain / _in), `buffer_frames`/`buffer_trail`
  (32768/131072), `resume_frame_size` 24, `engine` vm, and the
  short-search `per-subject mean ns` (903.1 vs 702.8) give the
  exercising row its identity. STILL MISSING for its FIX row: the plain
  entry's own capacity — `buffer_frames`/`buffer_trail` print "-" on
  `plain entry` rows, but the plain entry USES the stamped default
  (2048/3072), and that number is exactly what the measured cost is
  proportional to (pcrec's srOpt1 lane: gcc stack-clash probing of the
  98.5 KB run struct, ~99 % of the gap; patterns with small defaults pay
  nothing). Print the stamped default there. The floor control is still
  "n/a" (the footnote says so honestly).
- **1.47× 1 MB throughput loss (orig, auto vs JIT): NOT chartable** —
  `prefilter` reads "(no stamp — pcrec I-3)" on every DFA row (pcrec's
  to fix; the stamps land tonight with abi 4), and for a 3-subject set
  the per-subject numbers should be IN the table (a 3-row sub-table),
  not only "worst subject" in the Δ detail line. With those two it
  becomes [OPT-3].
- **DFA `\z` 3.7× compliance gap: chartable as what it is** — [OPT-2] is
  chartered and measured here (the anchored DFA match runs the
  unanchored search and filters; fail-path cost is identical between
  forms; the lead is matching subjects). The `fact` column + the italic
  regime-artifact note make the comparison honest. STILL MISSING for
  the fix: how many of the 85 subjects MATCH (the cost model differs
  for matching vs non-matching; one number per cell), and the `\z`
  form's prefilter stamp (`byte-class-bounded`, coming with I-3).
- **VM compile-cost multiple: CHARTABLE now** — the phase split says it
  plainly: gcc is 532.7 M of 535.8 M ns on the factored VM artifact vs
  124-135 M on the DFA one, while emit-c is the OTHER way (2 M VM vs
  8-10 M DFA: subset construction). [OPT-C]-class row: "a VM artifact
  costs gcc 3-4× a DFA artifact". MISSING: the artifact SIZE (emitted
  bytes or lines) as a column, to correlate gcc time with size rather
  than engine.

## (2) STILL INTERPRETED / WRONG / AMBIGUOUS

- `jitter` is EMPTY on every compile-cost row. The interpretive rows
  have stddev ≈ median (12.3 K vs 13.5 K) — that is what the column was
  for; compute it (stddev/median, or "timer-floor" when min < 20 µs) or
  drop it.
- `resume_frame_size` prints `0` on 692c2e8 DFA rows and `-` on 8da6120
  DFA rows for the same fact; `-` should mean "not stamped at that pin"
  and `0` "stamped: no buffers" — say so in the legend or render both as
  `0 (DFA)` / `n/s`.
- `buffer_frames`/`buffer_trail` "-" on plain entries: see (1) — the
  plain entry has a buffer; print the stamped default.
- "Δ detail: … worst subject": worst of the NEW record, or the subject
  with the largest Δ? The label implies the latter; the numbers look
  like the former. State which, and print both when they differ.
- Throughput tables would read better with ns/byte beside ns/call (1 MB
  subjects), the way short-search has per-subject mean.
- One fact the columns now expose that had to be NOTICED:
  `pcrec_692c2e8_vm-caps` is "faster ×1.19" (factored short-search) and
  "×1.26" (orig compliance) than `pcrec_8da6120_vm-caps` — a cross-pin
  VM speedup with no attributed cause (FB's run struct? wave G's
  splice?). The interpreter should flag an UNPREDICTED Δ as loudly as a
  regression; this one is real and unexplained.
- Give-ups by code with the smallest firing subject: exactly right now.
  One datum worth a sentence in the interpreter's rules: the same 1 MB
  subject gives STEPS (-2) on factored-VM and WORK (-4) on orig-VM —
  different budgets bind on the two spellings.

## (3) VERDICT CHANGES after the three re-measures

None — the measured values sit within noise of the inconclusive ones
(factored short-search auto 6,291 vs 6,284; orig throughput auto 13.386
vs 13.393 ms; interp baseline 138,268 vs 137,906). All eight verdicts
stand. NEW, uncovered by the list: the cross-pin VM speedup above.

## (4) REMOVE / SHORTEN

The five superseded-record ids in the Query header (120-char lines) →
"5 superseded (OD-B15); --all-records lists them"; and in the
compile-cost table the six per-TESTEE constant columns (engine, entry,
prefilter, vm_rungs with its 60-char `PCREC_VM_RUNG_…` string repeated
16 times, buffer sizes, frame size) → a one-line-per-testee legend
above the table, leaving the per-row phase numbers. The empty `jitter`
column goes with (2).

Note: pcrec's [DD-13] stamps lane (RX_ENGINE unconditional,
RX_DFA_SCAN unanchored|attempt, RX_DFA_PREFILTER with five values incl.
the -bounded pair; abi 3→4) lands tonight; the new pin arrives as inbox
I-5 when the battery is green.

## Manager's disposition

Two of four candidate rows are chartable from the report as printed
([OPT-1], the compile-cost multiple); the other two wait on pcrec's I-3
stamps plus two reporter facts (per-subject rows for 3-subject sets;
matching-subject count per compliance cell). §2 and §4 → plan [B14]
(reporter follow-ups). §2's two interpreter facts → [B13]: an
UNPREDICTED Δ (the cross-pin VM speedup ×1.19/×1.26, cause unattributed)
must be flagged as loudly as a regression; the STEPS-vs-WORK datum is a
"different budget binds" rule. §3: all eight verdicts stand after the
re-measure. Expect I-5 (re-pin, abi 4) — a [B8]-shaped re-pin row then.
