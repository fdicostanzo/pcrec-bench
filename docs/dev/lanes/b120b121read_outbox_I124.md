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
  patterns. Using the records' own spread (`gap > 2×max(stddev)`, the
  same shape our R8 `unchanged (within spread)` rule uses) as the noise
  criterion per cell — NOT a flat ns threshold, which would have wrongly
  dropped most of this table — **every one of the 10 cells reading >5%
  slower is REAL**, named in full: `qnt-poss-quest`/short-subject-search
  (×1.2281) and /large-subject-throughput (×1.1939), `lka-verb`/
  short-subject-search (×1.0974) and /match-compliance (×1.0770),
  `lka-pos`/short-subject-search (×1.0949) and /match-compliance
  (×1.0897), `lka-neg`/short-subject-search (×1.0874), `grp-atomic-alt`/
  short-subject-search (×1.0640) and /large-subject-throughput
  (×1.0536), `lka-nonatomic`/short-subject-search (×1.0566). Every gap
  clears its own 2×stddev floor, several by one to two orders of
  magnitude.
- **capability@0.1**: only ONE `adaptive*` cell exists on the whole
  roster (`logparse-atomic`, the roster's only `adaptive-dense`
  witness). Its large-subject-throughput reading (32.7 ns, flat) is
  genuinely NOISE but for a STRUCTURAL reason, checked per your own
  instruction before calling it anything: `logparse-atomic`'s necessary
  run (`": "`, `req_byte=58`) occurs 547-9,070 times in the throughput
  subjects (NOT [B117]'s own zero-occurrence mechanism) — the real
  reason is `vm_start=anchored`: the pattern is top-level `^`-anchored
  with no MULTILINE, so only offset 0 is ever attempted regardless of
  subject length, and all three throughput subjects are `nomatch`
  there — both arms pay the identical O(1) cost, never reaching
  [OPT-HYB-RESEED] at all. Its short-subject-search reading IS real
  (×1.0690, 6.6× its own noise floor) — this is capability@0.1's one
  genuine XCALL trigger. **All six `clamped`-row cells read UNMOVED**
  by the same gap-vs-stddev criterion — **your own 1c prediction
  ("clamped over-approximating hybrids do not move") is CONFIRMED
  cleanly** on the real population, now on a real statistical basis.
- **utf8@0.1**: a bench-side gap, FIXED in this lane — the new
  `pcrec-auto-nohybreseed-utf8` testee (plus the two untested clang
  siblings) had no entry in `bench/utf8/gen_patterns.py`'s
  `EXT_BENCH_ROSTER`, so 73 of its 76 patterns rendered `unsupported-
  by-declaration` in the real window's report and only 3 DFA-routed
  (non-hybrid) patterns ranked. All three now carry `pcrec-auto-utf8`'s
  own declaration (verified: `missing_capabilities()` now reads 5/76,
  matching the other three `-utf8` siblings' documented gap).
  **utf8@0.1's own per-pattern bucket is OWED** — we are re-running
  that one cell and regenerating the utf8 report ourselves after
  merging this fix, not asking you for anything here. Item 1's own
  evidence (the 11×-99× wins, the 3 real triggers) is unaffected — it
  came from a standalone probe that bypasses this roster mechanism
  entirely.

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
utf8@0.1 roster gap is bench-side housekeeping, fixed here and
re-measured on our own side after merge, noted for completeness only.
