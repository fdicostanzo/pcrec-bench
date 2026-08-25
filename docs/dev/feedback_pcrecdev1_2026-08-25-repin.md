# Feedback on the re-pin report — from the pcrec manager session (pcrecdev1), 2026-08-25 ~15:3x EDT

Verbatim in substance (lightly re-wrapped). Asked as outbox O-5 for
Frank's [B13] interpreter charter. The report read ALONE, set grain:
reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.md;
the bench manager's summary deliberately ignored.

## (1) ACTIONABILITY — what the report alone turns into a row, and what is missing

- (a) ROW: `vm-in` beats `vm` on every regime at one pin (orig/short-
  search 12,546 vs 28,997; orig/compliance 62,732 vs 80,228; factored/
  short-search 54,118 vs 69,538). Filed as pcrec **[OPT-1]** (per-call
  cost of the default entries). MISSING to charter from the report:
  which ENTRY each testee calls (`rx_search` vs `rx_search_in`) and the
  buffer sizes used (nframes/ntrail) — the testee id hints, the record
  has it, the table does not; and a per-call FLOOR control (a
  one-literal pattern on the same subjects) so the fixed overhead in
  12.5 µs is separable.
- (b) ROW: orig/large-subject-throughput — pcrec-auto 13.39 ms vs JIT
  9.12 ms: pcrec LOSES 1.47× on 1 MB. Chartable as an [OPT-*] row only
  with the artifact's mechanism stamps beside the cell (engine=dfa,
  prefilter kind, table width) and WHICH of the 3 subjects carries the
  loss (set grain sums them; `t-c-long-atom-run` is named only in the
  exclusion table).
- (c) ROW, and the one NOT expected: orig/match-compliance — the DFA
  `whole-subject` form (234,114) is 3.7× SLOWER than the VM form
  (62,732) on 85 subjects of 10-1000 B. Far more than the last-byte skip
  cost [DD-13](b) names; per subject ~2.7 µs vs ~0.7 µs, which smells
  like the anchored DFA `\z` artifact scanning to the END of every
  non-matching subject instead of stopping at its dead state. Chartable
  as a measurement row now (does the anchored DFA match exit on the dead
  state?). Missing: the per-subject pass/fail split (how many of the 85
  are non-matches — the cost model differs).
- (d) ROW-adjacent: compile cost — a VM artifact costs 3-4× a DFA
  artifact through gcc (orig 407 ms vs 138; factored 536 vs 138;
  factored-VM 536 vs orig-VM 407 = the splice expansion's gcc cost).
  [OPT-C]-class. Missing: the pcrec/gcc/dlopen SPLIT (the record has
  phases; the table shows totals).
- (e) NOT actionable from the report: the STEPS give-ups on
  `t-c-long-atom-run` under vm/vm-in — the code (steps vs frames) and
  the subject size at first firing are not stated ("gave-up 5" with n
  subjects 3 reads as per-trial; ambiguous).

## (2) INTERPRETATION — numbers that had to be interpreted and should be FACTS beside them

- STATUS (measured / inconclusive-load) is absent from the ranking
  tables entirely; known only from the manager's message. A column,
  every row.
- FORM semantics: for pcrec `whole-subject` is a SEPARATE ARTIFACT
  (`(?:P)\z`), for pcre2 it is a flag on the same program, yet pcre2
  shows `plain` in the compliance regime. State "same program /
  separate artifact" as a column; the "regime artifact" bucket IS that
  fact, not a footnote.
- The RATIO's baseline (interp = 1.000×) is stated once in the header;
  the ratio everyone wants is vs the best or vs JIT. Two ratio columns,
  or the baseline named in each table's title.
- NEAR-FLOOR: short-search tables omit `n subjects`, so a set sum of
  6,125 ns cannot be turned into per-call ns; give the per-subject mean
  and the timer floor per row.
- GIVE-UP: code (STEPS/FRAMES) + the smallest subject that fires it,
  per cell.
- CROSS-PIN: the tables interleave pins; a Δ column per (config,
  regime) for 8da6120→692c2e8 stating "collapsed / unchanged within
  noise / regressed" as a fact — that single column, plus a per-cell
  "worst subject: id, ns, size" line, would have made the subject-grain
  file unnecessary.
- MECHANISM STAMPS per pcrec cell (engine, prefilter, CALL_SPLICED/
  LINKED, frame size) — absent; that is I-3 + [B9]; until they are
  there, (1b) and (1c) are not chartable from the report alone.

## (3) PREDICTIONS (written before reading) → verdict

| prediction | verdict |
|---|---|
| factored/short-search collapses to orig's after wave G | CONFIRMED (6,284 vs 6,125) |
| pcrec-auto ≈ JIT on orig/short-search | CONFIRMED (6,125 vs 6,124 — closer than expected) |
| pcrec-auto slower than JIT on 1 MB throughput by ~1.3× | CONFIRMED in direction, magnitude 1.47× |
| vm-in ≈ vm (the buffer is only a depth remedy) | REFUTED, 2.3× — the surprise that became [OPT-1] |
| DFA `\z` whole-subject form ≥ VM on compliance | REFUTED, 3.7× slower — the second surprise, (1c) |
| VM artifact compile cost ≈ 2× DFA's | CONFIRMED in direction, magnitude 3-4× |
| interp compile-cost variance | UNCOVERED by any prediction; 12..109 µs over 10 trials is timer jitter — the report should say so rather than print a stddev larger than the median |
| JIT absent on factored/throughput (from U1) | CONFIRMED (5/5) |

## Manager's disposition

Items (2) are REPORTER COLUMNS → [B9] (status; form semantics
same-program/separate-artifact; ratio vs best AND vs the named
baseline; per-subject mean + timer floor; give-up code + smallest
firing subject; cross-pin Δ verdict column + worst-subject line;
mechanism stamps incl. entry used + buffer sizes; compile phases split;
a "stddev > median = timer jitter" flag). Items (1a)-(1d) are pcrec-side
rows ([OPT-1] filed by pcrecdev1; (1c) the anchored-DFA dead-state
question is a MEASUREMENT row for pcrec — outbox O-6 confirms it was
seen). (3) is the first PREDICTION LIST the [B13] interpreter takes as
input: eight predictions, five confirmed, two refuted, one uncovered.
The per-call FLOOR control pattern (1a) and the pass/fail split (1c)
are sub-bench design items for bench/email and every later set ([B11]).
