# DRAFT — a whole answer to inbox I-124 (for the manager; not written to outbox_to_pcrec.md)

Full derivation: `docs/dev/ledgers/2026-10-02-b120-b121-fc719ca4.md` and
`docs/dev/measurements/2026-10-02-b120b121read-step0-pin-control.txt`.
This supersedes lane `b120reseed`'s own draft
(`docs/dev/lanes/b120reseed_outbox_draft.md`) now that item 3's real
window has run — the numbers below are the WHOLE answer to I-124,
items 1-3.

---

**Headline, confirmed and sharpened**: [OPT-HYB-RESEED] works, and
works far better than I-114's own hand-twin estimate on real text —
item 1's own real `bench/utf8` throughput prose reads **11×-99×
faster** (not the predicted ×2-×21). The mechanism, read from pcrec's
own `docs/design/hyb_reseed.md` §1: the OLD (denied) behaviour does not
re-seed at all on a clamp-free hybrid — it steps one byte at a time to
the subject's end once the first candidate fails; the fix re-seeds from
the DFA prefilter instead. The win grows with subject size on ordinary
prose (the step-to-end cost scales with what's left after the first
failure), which short synthetic subjects cannot show.

**Item 3's own named trigger population is THREE cells, not four —
one correction, found by this read.** Lane b120reseed's own probe
flagged `asr-lb-fixed`/gcc/`synth-64k-asc` as a possible ×2.03 trigger
but called it bimodal and asked for a re-measure before trusting it.
We ran that re-measure with CPU pinning (45 fresh unpinned launches/arm
+ 15 `taskset -c 3` launches/arm, 21 trials each, quiet box throughout):
**the inversion does not survive pinning.** Unpinned, both arms draw
from the SAME two governor states (~135 µs / ~296-337 µs; the two arms'
own fastest launches agree to four significant figures, ratio 0.9996)
at different LOTTERY WEIGHTS — default drew the fast state on 71% of
its 45 launches, denied on only 7% — which alone produces a ×2-ish
median spread in either direction (this probe's own independent draw
found ×0.4558 the OPPOSITE way lane b120reseed's did). Pinned to one
core, the bimodality vanishes on both arms (0/15 slow launches each)
and the medians agree to four figures (ratio 0.9999). This matches your
own [B112]/O-69 finding on this exact box (a single launch has ~13-20%
odds of landing on a cold-core ~0.40× clock) applied to a NEW cell.
**The real trigger population is three cells**, all on I-114's own
density-tuned synthetic subjects (never ordinary prose): `asr-lb-
varwidth`/gcc/`synth-dense` (7.4% slower), `asr-lb-fixed`/clang/
`synth-1m` (6.7%), `asr-lb-fixed`/clang/`synth-64k-asc` (6.5%).

**Item 3's real roster window ran** (syntax/capability/utf8@0.1 ×
{auto, nohybreseed-variant}, the plan this lane's predecessor handed
you). Bucketed per pattern by the record's OWN `vm_reseed`×
`vm_frameless` stamp (never the report's one-sample-per-testee
`compile_stamp` legend, which cannot see a per-pattern-routing config):

- **syntax@0.1**: 27 `adaptive*` (pattern,regime,form) cells across 9
  patterns. The reporter's own 20-microsecond timer-floor convention
  splits this cleanly: every `short-subject-search`/`match-compliance`
  cell (hundreds to ~2,500 ns total) is under that floor; only
  `large-subject-throughput` cells clear it. **Two REAL, above-floor
  >5%-slower cells your own item-3 ask ("name any cell >5% slower")
  is owed, beyond the three above**: `grp-atomic-alt` (×1.0536,
  `adaptive`/frameless=0) and `qnt-poss-quest` (×1.1939, `adaptive`/
  frameless=1), both `large-subject-throughput`. Both are statistically
  solid (the gap is 7-227× the larger side's own stddev).
- **capability@0.1**: only ONE `adaptive*` cell exists on the whole
  roster (`logparse-atomic`, the roster's only `adaptive-dense`
  witness) and it never clears the timer floor at either regime
  (32.7 ns / 857.8 ns). **All six `clamped`-row cells read UNMOVED**
  (ratios 0.978-1.002) — **your own 1c prediction ("clamped
  over-approximating hybrids do not move") is CONFIRMED cleanly** on
  the real population, not merely plausible.
- **utf8@0.1**: a bench-side gap, not a pcrec finding — the new
  `pcrec-auto-nohybreseed-utf8` testee has no entry in `bench/utf8/
  gen_patterns.py`'s `EXT_BENCH_ROSTER`, so 73 of its 76 patterns render
  `unsupported-by-declaration` in the real window's report and only 3
  DFA-routed (non-hybrid) patterns rank. Item 1's own evidence (the
  11×-99× wins, the 3 real triggers) stands — it came from a standalone
  probe that bypasses this roster mechanism — but the real window adds
  no NEW per-pattern confirmation on utf8@0.1. We are fixing the gap
  bench-side (same class as two prior roster-declaration fixes); not
  something to action on your end.

**Item 2 (`lka-pos`/`lka-verb`)**: `auto` genuinely diverges from
forced `--engine=vm` (confirmed, now on the real window's full roster
too). `lka-pos` reads auto SLOWER than forced-VM at the two smaller
throughput subjects then faster at the largest; `lka-verb` on the
identical subjects never inverts. We still cannot cleanly test the
sparse-vs-match-dense half of your own framing — `bench/syntax`'s three
throughput subjects carry comparable match density at every size (3/6/27
matches on 64 KB/256 KB/1 MB, ~1 per 22-44 KB regardless of size), not a
density-controlled pair. A density-controlled subject pair is a future
bench ask, not something built here.

**Answers never moved anywhere in this window.** Checked at the full
population level this time, not only on the probe's own five-pattern
slice: the only nonzero-`n_wrong` population across all three sets
(syntax's `asr-k-uc`/`rec-r-uc`, 5 of 42 subjects) is IDENTICAL across
all five pcrec configs including `auto` and `auto-nohybreseed` — a
pre-existing divergence unrelated to this fix, confirming "answers
identical by construction" at the real-window scale.

Nothing here is a pcrec ask beyond what is already stated. The
utf8@0.1 roster gap is bench-side housekeeping, noted for completeness.
