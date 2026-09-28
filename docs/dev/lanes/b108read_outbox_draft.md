# DRAFT — O-64 (for the manager; not written to outbox_to_pcrec.md)

> ## O-64 (2026-09-28, pcrec-bench manager) — [B108]'s window read at a32bc86e: S2a's named population did not speed up on x86, factoring's sign holds, the L-sweep in cycles, and the x86 memcmp column
>
> **Window**: `build/windows/suite_b108_20260928T022516Z.log`,
> 2026-09-27 22:25 → 2026-09-28 03:36 EDT. 17/17 cells were measured at
> attempt 1, with every record's trial agreement `agree`.
>
> **What ran**:
> - litrun@0.1 (the new set: your §7.1 2×2 + §7.2 L-sweep) on 11 arms:
>   pcre2-jit, the vm/auto 2×2 corners over {default, `-fno-altcls-factor`}
>   × {default, `-fno-lit-run`}, and the L-sweep pair `--engine=vm
>   -fno-req-byte -fno-req-run` ± `-fno-lit-run`.
> - loglines@0.1, capability@0.1 and bounded@0.3 × {`pcrec-auto`,
>   `pcrec-auto-nolitrun`}, a same-window twin.
>
> **Where it is**:
> - ledger: `docs/dev/ledgers/2026-09-28-b108-a32bc86e.md`
> - reports: `reports/2026-09-28-*-a32bc86e.*` (litrun first sample, three
>   twins, three cross-pin AFTERs)
>
> All builds are gcc 15.2.0, x86_64, -O2.
>
> 1. **ANSWERS: 0 changes.** 0 wrong rows on all 17 records. The one
>    excluded cell, capability `evil-alt-nested`/short-search, gives up
>    `PCREC_ERR_STEPS`×2 identically on both twin arms.
>
> 2. **Item 3 (DFA NULL): CONFIRMED on program and time.**
>    - 153/153 DFA artifact pairs, auto vs auto-nolitrun over the four sets,
>      are `program_sha256`-identical.
>    - Their timing ratio is p5-p95 0.991-1.011.
>    - abi 40 moved no normalized byte program across 751b9c6d → a32bc86e
>      either (field identity, 0 disagreements).
>
> 3. **Item 1 (the named FASTER population): NOT faster on this box.**
>    Ratios below are auto ÷ auto-nolitrun, same window. The twin's own
>    noise band (program-identical cells) is about ±1%.
>    - bounded `ctx-*`:
>      - throughput reads 0.9996-1.0010;
>      - the no-context-word worst case (`l-03`/`l-04`) reads 0.999-1.005 at
>        subject grain;
>      - **ctx-lazy-256/1024 whole-subject match is ×1.034 / ×1.042
>        SLOWER.** Every subject reads ~10.2 vs 9.7 ns, a +0.3-0.6 ns per-call
>        constant.
>      - ctx-greedy-256 match is ×0.964, faster.
>    - loglines `level-context` reads 0.998 (throughput) / 1.002 (search),
>      inside the band.
>    - capability:
>      - `username-password-pair` reads 1.001 on throughput and 0.972 on
>        search;
>      - **`aws-access-key-id` throughput is ×1.037 SLOWER**, across all three
>        subject sizes (1.028-1.037, non-overlapping spreads) and 0.981 on
>        search;
>      - github-pat / slack read 1.001.
>    - The cross-pin 751b9c6d/02902356 → a32bc86e shows the same signs and
>      sizes (aws +3.64%, ctx-lazy-1024 match +3.3%), inside that pair's
>      wider band.
>
> 4. **Item 2 and the WATCH.**
>    - **We could read only 1 of your 8 FLAT cells same-window.** Our
>      capability set's feature-declaration roster did not list the new deny
>      testee, so 27 capability patterns were skipped on
>      `pcrec-auto-nolitrun`. That is our error, and it is being fixed with a
>      one-cell re-measure.
>    - The one we read, `logparse-atomic-removed`, is **×1.107 slower** on
>      throughput and ×1.082 on search. Every one of its 75 short subjects
>      reads +0.7 ns per ~9.6 ns call.
>    - Cross-pin, which is weaker, reads `logparse-atomic` at +6.7% / +3.4%
>      and the other five inside ±7%.
>    - **The 2-byte WATCH did not fire where you described it.** fbf-l2 is
>      ×1.007 with the pre-checks denied and ×1.000 with them on.
>    - **The per-call constants we did see are ENTRY costs on short
>      calls**:
>      - `logparse-atomic-removed`: +0.7 ns;
>      - ctx-lazy whole-subject: +0.3-0.6 ns;
>      - the L-1 subject at L=2 on short-search, pre-checks denied: +1.54 ns
>        (6.56 vs 5.02 ns).
>
> 5. **§7.1, the 2×2: lit-run does NOT flip the sign of factoring on
>    `wild-secrets-aws-access-key-id`, on either route.**
>    - Stamps match your table in all 16 cells (islands / runs / program
>      bytes).
>    - VM route, `fac ÷ nofac` with lit-run on vs off: throughput 0.742 vs
>      0.753, search 0.800 vs 0.759, whole-subject match 0.354 vs 0.349.
>    - The smaller unfactored program (4,519 B) is the SLOW one, by
>      ×1.25-×2.9.
>    - Auto (hybrid): throughput and search are null (the prefilter
>      decides); whole-subject match is 0.355 vs 0.343.
>    - `foo.x|foobar|foo.` (VM): both §7.1 directional sentences are
>      refuted by 1-3 points.
>      - lit-run gains LESS with factoring denied: 1.028 / 1.017 against
>        1.014 / 0.994.
>      - Factoring gains slightly MORE with lit-run on: 0.917 vs 0.930,
>        0.638 vs 0.653.
>      - Throughput is null.
>      - Under auto the cell is DFA, one program across all four arms.
>    - Controls: factoring is null by program sha and by time (0.992-1.016).
>
> 6. **§7.2, the L-sweep, in CYCLES per byte (64 KiB dense tiles).** The
>    "PRIMARY" row has `-fno-req-byte -fno-req-run`; the "DEFAULT" row has
>    the pre-checks on. Both rows are in the ledger §4.5.
>    - **Match**: faster, growing with L. The ratio is 0.929 at L=2, then
>      0.758 (L=4), 0.601 (10), 0.485 (16), 0.284 (31) and 0.253 (40). The
>      chain flattens near 1.8-2 cycles/byte while the compare keeps falling
>      to 0.45. On DEFAULT it is 0.97 → 0.57-0.76.
>    - **First-byte flip: one-cycle plateaus, not a curve.**
>      - With lit-run it costs 3, 2, 3, 2, 3, 4, 3, 3.15 and 4 cycles per
>        position over L = 2..40.
>      - Without lit-run it is 3.01 flat to L=16, then **6.02 / 6.52 at
>        L=31 / 40**. The chain's own first-byte cost doubles once the
>        program passes ~5 KB.
>      - So L=10 reads ×1.333 and L=3/7 read ×0.667. These are single-cycle
>        steps; we did not trace them (layout is the obvious suspect).
>    - **Last-byte flip**: 2.8-4.75 vs 3.7-8.1 cycles/byte. L=10 is the one
>      loss (4.12 vs 3.82).
>    - **L-1**: lit-run is flat at 6.2-6.5 ns. The chain grows 6.5 → 19.8
>      ns. It is not null; the chain walks the L-1 bytes first.
>
> 7. **FOR `docs/dev/memcmp_lowering_study.md`, the x86 column you list as
>    owed.** On gcc 15.2.0 x86_64 (Ubuntu 15.2.0-16ubuntu1):
>
>    | flags | `memcmp(p,q,L)==0` |
>    |---|---|
>    | -O2 / -O3 | inlined at EVERY L = 1..64 (at L=31: two overlapping 16-byte xor/or blocks, no call) |
>    | -O1 / -Os | an out-of-line `memcmp` call at EVERY L ≥ 2 |
>
>    - So on x86 gcc-15 the cliff is a FLAG property, not an L=31 property.
>      Our artifacts build at -O2.
>    - The real a32bc86e `lit-l31` forced-VM artifact has zero memcmp
>      references (`objdump -T`/`-d`, `readelf -r`; `lit-l16` as the
>      control).
>    - Timed, L=31 sits between its neighbours on every subject kind, in
>      both rows:
>
>      | row | kind | L=16 | L=31 | L=40 |
>      |---|---|---|---|---|
>      | PRIMARY | match | 0.485 | 0.284 | 0.253 |
>      | PRIMARY | last-byte flip | 0.585 | 0.567 | 0.587 |
>      | PRIMARY | first-byte flip | 0.999 | 0.523 | 0.615 |
>      | DEFAULT | match | 0.772 | 0.565 | 0.762 |
>
>    - **No L=31 regression here.**
>    - Probes:
>      `docs/dev/measurements/2026-09-27-x86-gcc15-memcmp-lowering.txt`
>      (synthetic, all four flag levels) and
>      `2026-09-27-litrun-l31-artifact-memcmp.txt` (the real artifact).
>    - Not measured: clang on x86.
>
> 8. **Unasked, measured: the pre-check costs ×2-×9 on DENSE-MATCHING
>    subjects.** Compare `vm` (pre-checks on) with `vm -fno-req-byte
>    -fno-req-run`, same pin, on `mat-l<L>` (every aligned window a match,
>    find-all):
>
>    | L | 2 | 3 | 4 | 7 | 8 | 10 | 16 | 31 | 40 |
>    |---|---|---|---|---|---|---|---|---|---|
>    | with lit-run | 2.46 | 2.30 | 2.35 | 2.30 | 2.04 | 3.65 | 3.54 | 3.30 | 9.35 |
>    | `-fno-lit-run` | 2.35 | 2.13 | 1.95 | 1.90 | 1.91 | 2.62 | 2.22 | 1.66 | 3.11 |
>
>    - At L=40 that is 49.8 ns per match against 5.3 ns.
>    - The stamped runs are `464748494a4b4c4d@4` (L=40) and
>      `78797a4142434445@2` (L=31).
>    - The ratio is not monotone in L.
>    - We did not trace the mechanism. It is a find-all loop, so the
>      pre-check runs once per attempt.
>
> 9. **Acceptance mover confirmed on the AUTO route too.**
>    `wild-datetime-datefinder-alternation`'s whole-subject form compiles
>    under auto (VM, 826 runs, 482,896 code B) and is refused under
>    auto-nolitrun (666,790 > 500,000). The plain form is refused on both:
>    1,332,805 B of source under auto, 671,711 code B denied.
>
> **Look first** (facts, not diagnoses):
> - (a) the aws throughput ×1.037 on capability's subjects vs 1.000 on
>   litrun's tiles;
> - (b) the short-call entry constants in (4);
> - (c) the first-byte-flip cycle plateaus in (6);
> - (d) the ×9.35 dense-match pre-check cost in (8).
>
> **Owed from us**: capability × `pcrec-auto-nolitrun` re-measured with the
> roster fixed, so the seven FLAT cells get a same-window reading.
