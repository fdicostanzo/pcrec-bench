# DRAFT — toward an answer to inbox I-124 (for the manager; not written to outbox_to_pcrec.md)

Phases A-C are done for items 1+2 (item 3's roster window is the
manager's, post-merge). Full numbers, tables and environment are in
`docs/dev/lanes/b120reseed_report.md` and
`docs/dev/measurements/2026-10-01-b120-reseed-multilaunch.txt`. This is
a draft of what an eventual O-n to pcrec could say, not the O-n itself.

**Headline for pcrec**: [OPT-HYB-RESEED] works, and works BETTER than
I-114's own hand-twin estimate on real text. On `bench/utf8`'s own
throughput prose (ordinary mixed-script corpus, not density-tuned),
`asr-lb-varwidth`/`asr-lb-fixed`/`asr-lb-neg` read **11x-99x faster**
with the real adaptive retry than with it denied (`-fno-hyb-reseed`),
against I-114's predicted x2-x21 band — which DOES hold on I-114's own
density-tuned synthetic subjects. The gap is explained structurally,
not just measured: ordinary prose has an uncontrolled failed-candidate
density that is often higher than what the synthetic subjects were
tuned to, and the pre-fix FIXED behaviour re-seeds (re-scans the whole
remaining subject from the prefilter) after every failed candidate —
a cost that compounds with candidate count far past what a
density-tuned synthetic subject can show. Worth a line to pcrec: their
own fix is a bigger win on real text than their own test subjects
demonstrated.

**syntax@0.1's lka-pos/lka-verb (item 2)**: `auto` genuinely diverges
from forced `--engine=vm` now (confirmed, both directions depending on
subject size) — the three-way ask's first half holds. The
sparse-vs-match-dense half (item 2's own `[OPT-HYB-RESEED-XCALL]`
trigger question) could NOT be answered from `bench/syntax`'s existing
subjects: its three throughput subjects are the same grammar at three
independently-drawn sizes, not a density-controlled pair, and the
measured ratios do not even trend monotonically with size. **An ask
for a future bench lane** (not pcrec): build a density-controlled
subject pair for syntax@0.1 (or reuse bounded's own near-miss
machinery) if the `[OPT-HYB-RESEED-XCALL]` question is to be settled
here rather than guessed at.

**Item 3's roster slice (the five patterns this probe measured)**: NO
cell with real candidate traffic reads the fix more than 5% slower
than denied — the opposite of the `[OPT-HYB-RESEED-XCALL]` trigger's
whole premise, on this slice. A few near-timer-floor cells (1-3us
absolute, near-zero real candidates) read "slower" by ratio but are
not evidence of anything. **This slice alone does not justify
[OPT-HYB-RESEED-XCALL]** — pcrec's own per-call re-learning-cost
worry does not show up where this probe could look. The FULL roster
(bounded's ctx-*/nest* family, capability's logparse-* family,
loglines' level-context — all `clamped`, not `adaptive*`, so outside
this probe's own two groups by construction) is still owed from the
manager's real window; a complete answer to I-124 should wait for that.

**No answer ever moved.** Checked twice: the driver's own within-process
hash (0/138) and a separate cross-arm re-check including the forced-VM
arm (0/138) — nothing here is a correctness finding.
