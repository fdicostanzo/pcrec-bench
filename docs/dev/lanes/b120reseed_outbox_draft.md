# DRAFT — toward an answer to inbox I-124 (for the manager; not written to outbox_to_pcrec.md)

Phases A-C are done for items 1+2 (item 3's roster window is the
manager's, post-merge). Full numbers, tables, spreads and environment
are in `docs/dev/lanes/b120reseed_report.md` and
`docs/dev/measurements/2026-10-01-b120-reseed-multilaunch.txt`. This is
a draft of what an eventual O-n to pcrec could say, not the O-n itself.

**Headline for pcrec**: [OPT-HYB-RESEED] works, and works MUCH better
than I-114's own hand-twin estimate on real text — 11x-99x, not the
predicted x2-x21. The mechanism, read from pcrec's own
`docs/design/hyb_reseed.md` (section 1): on a clamp-free hybrid the OLD
behaviour does not re-seed at all — it STEPS one byte at a time to the
subject's end once the first candidate fails, running a VM attempt at
each. That cost scales with how much subject remains after the first
failure, which is why the win GROWS with subject size on ordinary
`bench/utf8` throughput prose (t-64k -> t-256k -> t-1m) while landing
in the predicted band on I-114's own short, density-tuned synthetic
subjects. Worth a line to pcrec: their own fix is a much bigger win on
real text than their own test subjects could show.

**The [OPT-HYB-RESEED-XCALL] trigger population pcrec asked us to
name**: four real cells read the fix >5% SLOWER than denied, all on
I-114's OWN density-tuned synthetic subjects (never on ordinary prose,
which is faster everywhere) — `asr-lb-varwidth`/`synth-dense` (7.4%
slower), `asr-lb-fixed`/`synth-1m` clang (6.7%), `asr-lb-fixed`/
`synth-64k-asc` clang (6.5%), and `asr-lb-fixed`/`synth-64k-asc` gcc
(103% slower, but this one cell's 15-launch spread looks bimodal —
default's own min undercuts denied's own min — so we'd re-measure it
with more launches before calling it a clean x2 before reporting the
number as settled). All four match pcrec's own `hyb_reseed.md` §3
caveat on the `clamped` row's calibration ("the measured gain was
mixed... a fourth [witness] whose step the class calibration
misprices") — the same shape here, on the `adaptive` row.

**syntax@0.1's lka-pos/lka-verb (item 2)**: `auto` genuinely diverges
from forced `--engine=vm` now (confirmed). A named finding beyond that:
`lka-pos` reads AUTO SLOWER than forced-VM at the two smaller subjects
(x1.47, x1.90) then faster at the largest (x0.47) — real and
pattern-specific, since `lka-verb` on the IDENTICAL three subjects
never inverts. We could not test the sparse-vs-match-dense half of
item 2 as I-124 states it: `bench/syntax`'s three throughput subjects
are one grammar at three independently-drawn sizes with comparable
match density throughout (3/6/27 matches on 64 KB/256 KB/1 MB — ~1 per
22-44 KB regardless of size), not a density-controlled pair. **An ask
for a future bench lane** (not pcrec): build a density-controlled
subject pair for syntax@0.1 if the sparse/dense half of
`[OPT-HYB-RESEED-XCALL]`'s question is to be settled here.

**Item 3's roster slice (the five patterns this probe measured)**: the
>5%-slower population is exactly the four synthetic-subject cells
above plus the `lka-pos` inversion — nothing else, and nothing on
ordinary prose. The FULL roster (bounded's ctx-*/nest* family,
capability's logparse-* family, loglines' level-context — all
`clamped`, not `adaptive*`, outside this probe's two groups by
construction) is still owed from the manager's real window; a complete
answer to I-124 should wait for that.

**No answer ever moved.** Checked twice: the driver's own within-process
hash (0/138) and a separate cross-arm re-check including the forced-VM
arm (0/138) — nothing here is a correctness finding.
