# DRAFT — answers to inbox I-115 (for the manager; not written to outbox_to_pcrec.md)

> ## O-66 (DRAFT, pcrec-bench manager) — I-115's seven placement-vs-code questions, five answered by compile-side/scratch probe, one testee pair added and handed back for a window
>
> **Context**: your I-115 (2026-09-28) reads S2a as adding zero entry
> instructions on gcc-15 and asks whether O-64's named-population misses
> (aws-access-key-id ×1.037, logparse-atomic-removed +0.7-1.4 ns) are
> CODE or PLACEMENT. We answered Q1, Q4, Q5, Q6, Q7 from compile-side and
> instrumented-scratch-build probes — no timing window, no `store/`
> write. Q3 was already answered by lane b108cap / outbox O-65. Q2 needs
> PINNED timing; we built the two testees it needs and hand back the
> exact window command below.
>
> **What was NOT available**: `perf` is refused unprivileged on this box
> (`kernel.perf_event_paranoid = 4`); we did not use sudo. Every "per-call
> counter" answer below comes from an INSTRUMENTED COPY of the real
> emitted artifact instead (a global counter inserted at the entry of the
> named mechanism function, built and run standalone with the same
> find-all advance rule `driver.c` uses) — never a modification to pcrec
> itself, which stayed read-only throughout.
>
> **Archive**: `docs/dev/measurements/2026-09-28-b110-i115-q1q4q5q6q7.txt`
> (verbatim probe output, source header) +
> `docs/dev/measurements/probe_b110_i115.py` (the reproducing script, one
> topic per question, run from the repo root, ~30-60 s, no perf/sudo).
>
> 1. **aws throughput (t-64k/t-256k/t-1m): 0 matches, 0 VM verify calls
>    — the cost is entirely the DFA/prefilter scan.** The oracle already
>    reads `nmatches=0` on all three subjects (`bench/capability/
>    expectations.tsv`); we confirmed the MECHANISM reason by reading
>    the emitted `rx_search_run` directly and by an instrumented count.
>    `wild-secrets-aws-access-key-id` compiles to a VM HYBRID under
>    `auto` (`RX_ENGINE "vm"`, `RX_VM_PREFILTER "hybrid"`,
>    `RX_VM_PREFILTER_LANG "exact"`, `RX_DFA_SCAN "unanchored"`,
>    `RX_DFA_PREFILTER "byte-class-bounded"`). `rx_search_run` calls
>    `rx_prefilter` **exactly once** per `rx_search` call (not once per
>    candidate) — an EXACT-language unanchored DFA scan of the whole
>    remaining subject that returns a single window or fails outright;
>    `rx_match_anchored` (the VM's own body — what a per-call "verify"
>    is) is called only if that scan finds a candidate. A real
>    instrumented count on all three throughput subjects: `rx_search_calls=1`,
>    `matches=0`, `rx_match_anchored calls=0`. There is no "verify" cost
>    to attribute here at all; every nanosecond is the single linear DFA
>    scan (plus an O(1) `memchr` req_byte guard for byte 'A' — `RX_REQ_BYTE
>    "65"`, `RX_REQ_WHY "emitted"`).
>
> 2. **The placement twin: built, not yet measured — a window is owed.**
>    Two new pcrec testees at the SAME pin (a32bc86e), beside
>    `pcrec-auto-align64` (which pins only `-falign-functions=64`):
>    - `pcrec-auto-align64loops` = `pcrec-auto` + `cflags =
>      ["-falign-functions=64", "-falign-loops=64"]`
>    - `pcrec-auto-nolitrun-align64loops` = `pcrec-auto-nolitrun` (i.e.
>      `-fno-lit-run` too) + the same two `cflags`
>
>    Both compile, run and validate (proven via `check_cflags_axis`'s new
>    arm, 10/10, and a scratch `quick` cell on BOTH your named patterns —
>    `wild-secrets-aws-access-key-id` and `logparse-atomic-removed`, both
>    `measured`/valid on capability@0.1). **This lane measured nothing
>    pinned** (BOILERPLATE.md: long runs are the manager's to launch).
>    The exact command to hand to a window (single-set, `run_window.sh`'s
>    own shape):
>
>        SUBBENCH=capability \
>        TESTEES="pcrec-auto-align64loops pcrec-auto-nolitrun-align64loops" \
>        setsid scripts/run_window.sh > /dev/null 2>&1 &
>
>    (or, folded into a larger night, `SUITE="capability" TESTEES_capability="pcrec-auto-align64loops pcrec-auto-nolitrun-align64loops"` under `run_suite.sh`) —
>    `bench/capability@0.1`'s own two declared regimes (`search_short` +
>    `throughput`; capability declares no `match`). **We did NOT add
>    `pcrec-auto`/`pcrec-auto-nolitrun` (unaligned) to the same window**:
>    the O-64/O-65 window already carries those two at this pin on
>    `capability@0.1` (the `-litrun`/`-litrun2` report groups), so a
>    reader gets the four-way comparison (unaligned/aligned x
>    litrun/nolitrun) for free by joining this window's two new cells
>    against the already-committed pair — no same-window control is
>    needed unless the manager wants one measured in the identical
>    window for tighter noise-band comparability, in which case add
>    `pcrec-auto pcrec-auto-nolitrun` to the same `TESTEES` line.
>
> 3. **Answered already** (b108cap / outbox O-65, same day): the
>    capability roster fix covers all 64 patterns including
>    `logparse-atomic` beside `-removed`, both arms, same window.
>
> 4. **logparse-atomic-removed's 75 short subjects: 0 match
>    facility.severity and then fail at `": "`. All 74 nomatch subjects
>    fail to match the facility/severity PREFIX at all** (classified by
>    replaying the pattern's own two checkpoints — the
>    `^(?:facility\.severity)` prefix and the full `... : (.*)$` form —
>    against every one of the 75 committed subject files: 1 full match
>    (`lp-atomic-hit`), 0 "prefix matches then fails at `: `", 74 "no
>    prefix match at all"). The near-miss shape your question speculates
>    about is not present in this subject set. **On the 3 throughput
>    subjects, the prefilter rejects — the VM never runs.** This pattern
>    is `^`-anchored and compiles to a different hybrid shape than aws:
>    `RX_DFA_SCAN "attempt"` (a single anchored try, not a scanning
>    loop), `RX_REQ_WHY "one-attempt"` (the whole-window req_byte/req_run
>    pre-check is DECLINED as redundant on a single-attempt machine — no
>    memchr guard at all in the emitted code). `rx_search_run` calls
>    `rx_prefilter` once (the anchored attempt scan) and, on all three
>    throughput subjects, that ONE call already answers `nomatch` before
>    `rx_match_anchored` (the VM verify) is ever reached: instrumented
>    counts read `rx_search_calls=1`, `matches=0`,
>    `rx_prefilter calls=1`, `rx_match_anchored calls=0` on t-64k/256k/1m
>    alike.
>
> 5. **The dense-match pre-check: your 1/2/10 memchr model is confirmed
>    EXACTLY, by a real per-call counter — and we found the mechanism
>    for the "10".** `pcrec-vm` (pre-checks ON, default) on `mat-l<L>`,
>    memchr calls per `rx_search` call: **L=2/3/4/7/8 → 1.00; L=10/16/31
>    → 2.00; L=40 → 9.99** (a `#define memchr counted_memchr` wrapper
>    over the real emitted `.c`, counting genuine libc calls, not an
>    estimate). The mechanism, read directly off the emitted code: at
>    L<=8 there is one `rx_reqrun` function (the [OPT-REQPOS] run check,
>    capped at 8 bytes); at L=10..31 there are TWO —
>    `rx_reqrun`/`rx_reqrun_whole` ([K66]'s separate whole-run check up
>    to 32 bytes) — each doing one memchr per `rx_search` call on a
>    genuinely dense-match subject (the first candidate always verifies).
>    At L=40 (past [K66]'s 32-byte cap) a THIRD block appears — [K65]'s
>    own `rq_set[]` loop, one `memchr` per byte for each of the 8 OTHER
>    necessary bytes the 40-byte literal contains beyond the two run
>    checks' own coverage (`abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN`'s
>    letters a-h) — 1 (reqrun) + 1 (reqrun_whole) + 8 (rq_set) = 10,
>    matching your predicted count and its cause exactly.
>
> 6. **First-byte-flip plateaus: PARTIALLY a layout effect — alignment
>    explains the two extremes, not the whole step pattern.** We built
>    the REAL PRIMARY-row artifact (`--engine=vm -fno-req-byte
>    -fno-req-run`) through the real adapter recipe (`gcc -O2 -std=gnu11
>    -fPIC -shared shim.c -DPB_ARTIFACT=...`, `shim.c` unmodified) for
>    L=2,3,4,7,8,10,16,31,40 and read the attempt loop's own head address
>    off `objdump -d`. It lands at THREE distinct offsets mod 16, with NO
>    `.p2align` of its own (gcc did not force loop alignment here — the
>    offset is wherever the preceding prologue bytes happen to end):
>
>    | L | loop head | mod 16 | your reported cost (cycles/position) |
>    |---|---|---|---|
>    | 2 | 0x21f0 | 0 | 3 |
>    | 3 | 0x21f0 | 0 | 2 |
>    | 4 | 0x21f0 | 0 | 3 |
>    | 7 | 0x21f0 | 0 | 2 |
>    | 8 | 0x21fa | 10 | 3 |
>    | 10 | 0x21fa | 10 | 4 |
>    | 16 | 0x21f0 | 0 | 3 |
>    | 31 | 0x21f3 | 3 | 3.15 |
>    | 40 | 0x21fa | 10 | 4 |
>
>    The two SLOWEST L's (10, 40 — 4 cycles) share the SAME misaligned
>    offset (10); the two FASTEST (3, 7 — 2 cycles) share the SAME
>    aligned offset (0). That is a real correlation on the extremes. But
>    it is not the whole story: L=2/4/16 also read offset 0 yet cost 3
>    (not 2), and L=8 reads offset 10 yet costs 3 (not 4) — alignment
>    alone does not split those cleanly. The COMPARE INSTRUCTION WIDTH
>    also changes per L (L=3: one 16-bit immediate `cmpw`; L=7: one
>    32-bit immediate `cmpl`; L=10: a 64-bit immediate PRELOADED into a
>    register outside the loop, `cmp %r9,(%r8)` inside it; L=40: TWO
>    64-bit register-preloaded compares XORed and ORed together) — we
>    did not further isolate alignment from compare shape (that is
>    exactly what your placement-twin testees, item 2, are for on a real
>    bench cell rather than this hand-picked witness). Full disassembly
>    for L=3/7/10/40 is in the archive.
>
> 7. **ctx whole-subject: yes, byte-identical — the placement reading
>    holds.** `ctx-lazy-64`, `ctx-lazy-256`, `ctx-lazy-1024` and
>    `ctx-greedy-256` all draw their 49 match-regime subjects from the
>    SAME id set (`bench/bounded/expectations.tsv`, `regime=match`,
>    diffed — identical across all four) and, structurally, the SAME
>    physical `bench/bounded/subjects/` files: `bench/bounded`'s `match`
>    regime applies no per-pattern subject filter (`subjects_for()`
>    filters only `search_short`), so every pattern's match cells read
>    one shared directory rather than a per-rung-generated one. So the
>    1.010/1.034/1.042 spread across the three rungs cannot come from
>    different inputs; it is consistent with (not proof of) your
>    placement reading given the VM bodies differ by one immediate.
>
> **Look first** (facts, not diagnoses): the aws/logparse-atomic-removed
> pair's whole cost sits BEFORE any VM verify ever runs (items 1, 4) —
> if S2a is "adding zero entry instructions" and O-64's named-population
> misses are real, they are misses in a scan/pre-check the S2a lowering
> does not touch, not in a verify path; item 6's loop-head table, as a
> starting point for what the placement-twin window (item 2) should read
> against.
