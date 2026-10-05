# DRAFT — answer to inbox I-127 (for the manager; not written to outbox_to_pcrec.md)

Full derivation: `docs/dev/ledgers/2026-10-05-b122-round1-wide-
c4c70f2c.md`.

---

**[OPTLOOP] round 1's WIDE BENCH ran clean.** 16/16 cells `measured`
at attempt 1, 2026-10-05 00:28-08:42 EDT (`STOP_AT` 12:00 not reached,
nothing carried). The cell count your own gate note and our launch
message both said was 19 is corrected here to **16** — the real list
is capability/syntax/utf8@0.1 × {auto, vm, nocaps} (9 cells),
loglines@0.1/bounded@0.3/email-specimen@0.2 × auto (3), altwide@0.3/
litrun@0.1 × {auto, vm} (4). Per-set wall time: capability 98 min,
syntax 136, utf8 120, loglines 12, altwide 38, bounded 49, email 7,
litrun 29 (≈8h09m of the ~8h14m window).

**pcrec wrong-answer count: 0 NEW anywhere.** The one nonzero reading
(`syntax`'s `asr-k-uc`/`rec-r-uc`, `match-compliance`/`whole-subject`,
`n_wrong=5` of 42, all three pcrec testees) is BYTE-IDENTICAL to the
same two patterns' fc719ca4 reading and is the already-documented
2026-09-07 whole-subject anchored-branch limitation (`first_s`
hardcoded to 0) — not a round-1 regression. Every other set/testee
combination (13 of 16 cells) reads 0.

**K81 ([OPT-VEDGE]) scored — NOT CONFIRMED as a real mover on either
named pattern.** `base10num-grok`/large-subject-throughput moved
+73,447 ns (your own band was +4-6.5 µs; we measured +73.4 µs, in the
predicted direction but 11-18× larger) — and it reads `unchanged
(within spread)` by our own R8 criterion (only 3 trials on this
regime; stddev 40,725/26,625 ns swamps the move). `cls-upto-1024`
moved +5,703 ns on large-subject-throughput (your band +0.2-0.5 µs;
measured +5.7 µs, 11-28× larger) — also `unchanged (within spread)`.
Both patterns' SMALLER-magnitude cells (short-subject-search on both;
match-compliance on cls-upto-1024) moved the OPPOSITE direction and
ARE real by our own criterion (`faster ×1.02`/`×1.03`; `slower ×1.00`
at +18.2 ns on match-compliance, an order of magnitude smaller than
your 0.2-0.5 µs band). **We could not locate the "short-call +1-9 ns"
cell** — no pattern in our eight sets spells "short-call", and no
short-subject-search cell on either named pattern moved in that
direction/magnitude. Please name the exact (pattern, regime) for this
one.

**K82 ([OPT-LITSCAN] S4 C3) scored — two clean confirmations, one
larger-than-stated population, two unresolved citations.**
`wild-secrets-username-password-pair` ("userpass") large-subject-
throughput: 23,180 → 1,290,153 ns = **slower ×55.66** (your ~57×, 2.4%
off) — its short-subject-search cell ALSO regresses, unnamed by you,
`slower ×1.46`. `wild-waf-crs-942270-union-select` ("customers
union-select") large-subject-throughput: 997,001 → 465,669 ns over
1,376,256 B = **−0.3861 ns/B** (your −0.40..−0.52 ns/B band, 3.6%
outside its near edge, same sign/order of magnitude) — the forced-VM
sibling moves even more, `faster ×9.08`. **Its own short-subject-search
cell moved the OPPOSITE direction from your "+2.4-4.4 ns" line**: both
`auto` (`faster ×1.16`, −2.12 ns/subject) and `vm` (`faster ×3.54`) are
REAL IMPROVEMENTS — please confirm whether "short union-srch calls"
names union-select itself or a different population; as measured here
it does not match. **The five named fold-family patterns
(mod-i/mod-r/cls-fold-pair/cls-pair-ctl/ci-strasse) all read a real,
consistent REGIME SPLIT, far larger than any magnitude in your own
text**: on large-subject-throughput, SLOWER on every config — `mod-i`
×1.69/×1.70/×2.28 (auto/auto-nocaps/forced-vm), `mod-r`
×1.70/×1.69/×2.29, `cls-fold-pair` ×1.69/×1.68/×1.48, `cls-pair-ctl`
×1.67/×1.68/×2.08, `ci-strasse` ×1.10/×1.24 (auto/auto-nocaps only, no
forced-vm cross-pin on utf8's roster this window); on short-subject-
search, the four syntax ones FASTER on the forced-VM route specifically
— `mod-i` ×1.67, `mod-r` ×1.68, `cls-fold-pair` ×1.55, `cls-pair-ctl`
×1.36 (ci-strasse's forced-vm sibling the same shape, ×1.56). Worth
knowing if this two-sided shape (slower sustained matching, faster
short dispatch, biggest swings on the forced-VM route) is what the fix
intends, or a side effect.

**K83 ([OPT-HYB-RESEED-FORM] A1) is UNSCORED this window.** Your own
filed number (+~24 ns/pass) is for the clang cc-axis arm specifically;
tonight's 16-cell list carries gcc-built pcrec testees only (no
`-clang` sibling was in the accepted cell list) — this window cannot
confirm or refute it either way. If K83 matters for round 2's
ranking, say so and we will add the clang arm to a future window.

**Two real movers beyond anything your text named, found on a spot
check (not a full census — say if a systematic sweep is wanted)**:
utf8's `ci-ascii-control` IMPROVES hugely on large-subject-throughput
— `×2.77` (auto/auto-nocaps), `×8.38` (forced vm) — the largest win in
any report this window; utf8's `alt-shared-char` REGRESSES on the same
regime — `×2.06` (both DFA configs), `×1.21` (forced vm).

**Census attribution (your own `2026-10-04-b122-census.txt`, carried
here for completeness, not re-derived)**: 815/1,380 identical, 462
changed (383 restored by one round-1 deny flag alone — run-overlap
291, view-edge 62, req-run-fold 30 — 15 by all three, 64 by other
flagless abi steps in the same merge: [CLS-TREE] S2's range respelling
56, A1's `adaptive-dense`→`anchored` move on `logparse-atomic` 2, K78's
DFA dead-group relocation on `factored` 2, [CLS-TREE] S2's
interval-vs-table move on two utf8 wide-class patterns 4), 103
refused-both, **0 refusal movers**. Confirming on real timing: email's
`factored` (a K78 flagless program mover) reads genuinely FLAT
(`slower ×1.00`/`unchanged (within spread)`/`faster ×1.04` across its
three regimes) — a program change need not move a number.
Confirming altwide's own run-overlap attribution in TIMING too: the
class-tail family (`clsa-64`/`clsd-64`) is `×1.16-×1.37 faster` on the
forced-VM route across all three regimes, consistent with 291 of 462
changed rows being altwide's own VM forms restored-by run-overlap
alone — a real, not merely compile-byte, win on this set's forced-VM
arm. litrun shows no cross-pin mover beyond ±1.17× on any of its 15
patterns — round 1's four changes do not touch this set's own
literal-run mechanism family in any measurable way at this sample
(expected: none of litrun's own mechanism, S2a, is one of round 1's
four changes).

**What this window did NOT do**: no deny-flag twins for
`-fno-view-edge`/`-fno-run-overlap`/`-fno-req-run-fold` were built or
measured (per your own I-127 note that the Linux alphas already
attribute each round-1 change) — every K81/K82 Δ scored here is
against the FULL nine-abi-step default build, not an isolated flag; no
clang cc-axis arm (K83 unscorable); litrun's three deny-twin testees
were not rebuilt at c4c70f2c (its report carries only `auto`/`vm`,
cross-pin against **a32bc86e**, two re-pins back, not fc719ca4 — stated
so a Δ on litrun is read at the right abi distance); the two
beyond-ask findings (ci-ascii-control, alt-shared-char) came from a
spot check of utf8's largest-magnitude rows, not an exhaustive sweep
of all eight reports.
