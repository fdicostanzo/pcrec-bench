# DRAFT — answer to inbox I-127 (for the manager; not written to outbox_to_pcrec.md)

**STATUS: SKELETON — render pending.** This draft's window-facts,
population and census-attribution sections are final; the per-cell
numbers that score K81/K82/K83 and the wrong-answer headline are
PENDING the manager's "renders OK" (the box is held for pcrec's
daytime [MEMFN] timing probe). The manager fills the numbered
placeholders below from `docs/dev/ledgers/2026-10-05-b122-round1-
wide-c4c70f2c.md` §3/§4 once rendered, or sends this lane back to do
so.

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

**pcrec wrong-answer count: [PENDING — must read 0 across all 16
cells; this is the headline if it is not].**

**K81 ([OPT-VEDGE]) scored**: [PENDING — base10num-grok mix/hex Δ;
cls-upto-1024 Δ; the short-call cell Δ, against your own filed +4-6.5
µs / +0.2-0.5 µs / +1-9 ns bands].

**K82 ([OPT-LITSCAN] S4 C3) scored**: [PENDING — userpass
(`wild-secrets-username-password-pair`) Δ against your own ~57× band;
mod-i/mod-r/cls-fold-pair/cls-pair-ctl/ci-strasse Δ (direction as
measured); union-select short-subject-search Δ against +2.4-4.4 ns;
union-select large-subject-throughput Δ against −0.40..−0.52 ns/B].

**K83 ([OPT-HYB-RESEED-FORM] A1) is UNSCORED this window.** Your own
filed number (+~24 ns/pass) is for the clang cc-axis arm specifically;
tonight's 16-cell list carries gcc-built pcrec testees only (no
`-clang` sibling was in the accepted cell list) — this window cannot
confirm or refute it either way. If K83 matters for round 2's
ranking, say so and we will add the clang arm to a future window.

**Census attribution (your own `2026-10-04-b122-census.txt`, carried
here for completeness, not re-derived)**: 815/1,380 identical, 462
changed (383 restored by one round-1 deny flag alone — run-overlap
291, view-edge 62, req-run-fold 30 — 15 by all three, 64 by other
flagless abi steps in the same merge: [CLS-TREE] S2's range respelling
56, A1's `adaptive-dense`→`anchored` move on `logparse-atomic` 2, K78's
DFA dead-group relocation on `factored` 2, [CLS-TREE] S2's
interval-vs-table move on two utf8 wide-class patterns 4), 103
refused-both, **0 refusal movers**.

**What this window did NOT do**: no deny-flag twins for
`-fno-view-edge`/`-fno-run-overlap`/`-fno-req-run-fold` were built or
measured (per your own I-127 note that the Linux alphas already
attribute each round-1 change) — every K81/K82 Δ scored here is
against the FULL nine-abi-step default build, not an isolated flag; no
clang cc-axis arm (K83 unscorable); litrun's three deny-twin testees
were not rebuilt at c4c70f2c (its report carries only `auto`/`vm`,
cross-pin against **a32bc86e**, two re-pins back, not fc719ca4 — stated
so a Δ on litrun is read at the right abi distance).

[The manager adds here: ranked candidates for round 2, in the shape of
prior outbox items (O-81/O-82) — PENDING the render.]
