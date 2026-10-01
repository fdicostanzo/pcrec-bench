# DRAFT — O-79 (for the manager to date/file into docs/dev/outbox_to_pcrec.md)

Findings only, numbers cited from the committed report and ledger; no ask
beyond what the data supports. Source: `docs/dev/ledgers/2026-10-01-b117-olevel-fc719ca4.md`,
`reports/2026-10-01-capability-0.1-budu-ryzen1600-olevel-fc719ca4.{tsv,interpretation.md}`.

## O-79 (2026-10-01, lane b117read) — [B117]: pcrec's two engine routes respond very differently to the compilee's own `-O` level, measured at fc719ca4 (abi 50)

Not a bug report — this is our own phase-2 `$CC -O` level (OUR flags,
never passed to pcrec), measured on `bench/capability@0.1`'s 62 compiling
patterns, both engine routes, at your fixed `-O2` default against
`-O0`/`-O1`/`-O3`/`-Os`. FYI for whichever of your own documentation
names a recommended build flag for an artifact consumer; no change asked.

**The DFA/table-loop route (`pcrec-auto`) is NOT insensitive to codegen
quality the way a premultiplied-table byte walk might suggest.** At
`-O0`, 50 of 62 patterns (81%) run >15% slower than the same pattern at
`-O2` (median ×2.25, worst `utf8-lead-no-cont` ×6.72) — every one of them
in the slower direction, none faster. At `-Os`, 34/62 (55%) are still
>15% slower (median across the band is ×1.25, worst `wild-validator-
email-owasp` ×3.41). At `-O3`, the route is close to flat: 58/62 (94%)
stay within ±15% of `-O2`, and the 4 that don't are all slightly FASTER
(down to ×0.66, `phone-palindrome-6`), never slower.

**The VM/goto-dispatch route (`pcrec-vm`) moves in the expected direction
for most, not all, of the corpus.** At `-O0`, 48/62 (77%) are genuinely
>15% slower (median ×3.10, worst `wild-codegrammar-json-array-begin`
×9.20), but 14/62 read within a few tenths of a percent of `-O2`
(`mojibake-curly-quote` ×1.004, `winpath-near-miss` ×1.003, `floor-byte`
×1.003 among them) — we have not traced what these 14 share mechanically
(a DFA-side prefilter pre-check dominating the cost, a near-miss subject
exiting early, or fixed per-call overhead swamping the dispatch loop are
candidates, not conclusions). At `-Os`, 38/62 are measurably slower but
13/62 are genuinely FASTER (down to ×0.668, a real 33% win on `utf8-lead-
no-cont`) and 11/62 sit in a narrow near-neutral band. At `-O3`, only
4/62 exceed a 5% slowdown (worst `wild-waf-crs-942140-dbnames` ×1.159).

**`utf8-lead-no-cont` is a recurring outlier**, the single most extreme
witness in five of sixteen (route × regime × level) distributions we
computed, in both directions: the DFA-route `-O0`/throughput max
(×6.72), the VM-route `-O1` min on both regimes (×0.47/×0.62), and the
VM-route `-Os` min on both regimes (×0.67/×0.79). We have not examined
this pattern's own shape to say why; flagging it as a candidate witness
if useful on your side.

**Compile-side (`.so` bytes): `-O0` is the one level with a real,
across-the-board size cost on both routes** (median ×1.13-1.14; worst
`wild-logparse-syslogbase-expanded` ×1.91 auto / ×2.51 vm — nearly
doubling/2.5×ing). `-O1`/`-O3`/`-Os` all read essentially flat at the
median on both routes.

**`-O1`, which we did not predict against, costs real time on both
routes**: median ×1.04 (auto, throughput) to ×1.16 (vm, search), with a
genuine slower-side tail (vm `router-prefix-order` ×2.14 throughput,
`logparse-atomic` ×1.85 search).

Full distribution tables (median/Q1/Q3/extremes, every route × regime ×
level) are in the ledger's §2-§3; nothing here depends on a v1.4 spread
flag (all ten records this window wrote read `agree`, 5 trials each).

No ask attached. If useful: this is the first direct, same-window
measurement of how much pcrec's OWN emitted-C choices (table-walk DFA
vs. goto-threaded VM dispatch) interact with the downstream compiler's
optimization level — a question your own artifact-consumer
documentation may want an answer to, independent of anything pcrec
itself changes.
