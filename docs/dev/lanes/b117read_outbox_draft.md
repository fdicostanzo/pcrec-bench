# DRAFT — O-79 (for the manager to date/file into docs/dev/outbox_to_pcrec.md)

Findings only, numbers cited from the committed report and ledger; no ask
beyond what the data supports. Source: `docs/dev/ledgers/2026-10-01-b117-olevel-fc719ca4.md`,
`reports/2026-10-01-capability-0.1-budu-ryzen1600-olevel-fc719ca4.{tsv,interpretation.md}`.

## O-79 (2026-10-01, lane b117read) — [B117]: pcrec's compiled artifact responds very differently to the compilee's own `-O` level depending on engine selection and on a pattern's own necessary-byte guard, measured at fc719ca4 (abi 50)

Not a bug report — this is our own phase-2 `$CC -O` level (OUR flags,
never passed to pcrec), measured on `bench/capability@0.1`'s 62 compiling
patterns, two testees (`pcrec-auto`, `pcrec-vm`), at your fixed `-O2`
default against `-O0`/`-O1`/`-O3`/`-Os`. FYI for whichever of your own
documentation names a recommended build flag for an artifact consumer; no
change asked.

**`pcrec-auto` is NOT one engine route — it is NOT insensitive to codegen
quality the way a premultiplied-table byte walk alone might suggest.** Of
its 62 compiling patterns, 29 compile to a pure DFA, 22 to a VM core with
a DFA-side prefilter ("VM hybrid"), 11 to a VM core with no prefilter
("VM pure") — identical across all five `-O` levels (your own routing
decision happens before our `-O` flag is ever applied). Checked against
the DFA-stamped subset alone: at `-O0`, those 29 patterns run >15% slower
than at `-O2` in 24 of 29 cases (median ×2.24, worst `utf8-lead-no-cont`
×6.72, itself DFA-routed) — every one of them in the slower direction,
none faster. At `-Os`, the DFA-stamped subset is STILL >15% slower in the
majority of cases (median ×1.25, worst `wild-validator-email-owasp`
×3.41). At `-O3`, all three engine categories read close to flat, but the
VM-hybrid category is measurably the odd one out: median ×0.9683
throughput / ×0.9429 search — consistently slightly FASTER at `-O3` than
`-O2`, the one category that moves that direction across the board. Over
the WHOLE `pcrec-auto` population (all three categories combined): `-O0`
50/62 patterns (81%) exceed ±15%, `-Os` 34/62 (55%), `-O3` only 4/62 (all
faster, never slower).

**`pcrec-vm` (forced `--engine=vm`, a genuinely uniform route — 62/62
patterns stamp `engine: vm`, `prefilter: none`) moves in the expected
direction for most, not all, of the corpus, and we found a MEASURED
reason for the exceptions.** At `-O0`, 48/62 (77%) are genuinely >15%
slower (median ×3.10, worst `wild-codegrammar-json-array-begin` ×9.20),
but 14/62 read within a few tenths of a percent of `-O2`. **All 14 share
one trait, confirmed by direct byte-count over the throughput subjects,
not guessed**: each has an `RX_REQ_BYTE` necessary-byte guard whose
scanned byte occurs ZERO times in the three throughput texts (64 KB/256
KB/1 MB). Your own necessary-byte pre-check therefore runs a single
linear scan to completion and declares no-match WITHOUT the VM dispatch
loop ever executing once — and that scan's own machine code is presumably
`memchr`/equivalent, outside what our phase-2 `-O` flag recompiles, which
is why these 14 read flat. The split is 100% clean over the whole
62-pattern population: every pattern whose necessary byte DOES occur in
the subjects (22/62, counts 2,289-44,132) reads a real `-O0` slowdown
(×1.61-×9.20); every pattern with no necessary byte emitted at all (26/62)
also reads a real slowdown (×2.41-×7.87); only the 14 zero-occurrence
patterns read flat. Their `.so` artifact DOES still differ in size at
`-O0` (+240 B to +8,512 B, the usual no-dead-code-elimination cost) — the
differing code is simply never reached by these particular subjects.
Absolute magnitudes: `floor-byte` and `mojibake-curly-quote` (both
zero-occurrence) read ~23.1 microseconds summed over all three throughput
subjects at EVERY `-O` level; `wild-codegrammar-json-array-begin` (byte
occurs up to 5,985 times) reads 1.11 ms at `-O2` and 10.18 ms at `-O0` on
the same testee/regime/subjects — a ×9.20 move on the SAME necessary-byte
mechanism, present vs. absent. At `-Os`, 38/62 are measurably slower but
13/62 are genuinely FASTER (down to ×0.668, a real 33% win on `utf8-lead-
no-cont`) and 11/62 sit in a narrow near-neutral band. At `-O3`, only
4/62 exceed a 5% slowdown (worst `wild-waf-crs-942140-dbnames` ×1.159).

**`utf8-lead-no-cont` is a recurring outlier**, the single most extreme
witness in five of sixteen (testee × regime × level) distributions we
computed, in both directions: `pcrec-auto`'s `-O0`/throughput max (×6.72,
itself DFA-routed), `pcrec-vm`'s `-O1` min on both regimes (×0.47/×0.62),
and `pcrec-vm`'s `-Os` min on both regimes (×0.67/×0.79). We have not
examined this pattern's own shape to say why; flagging it as a candidate
witness if useful on your side.

**Compile-side (`.so` bytes): `-O0` is the one level with a real,
across-the-board size cost on both testees** (median ×1.13-1.14; worst
`wild-logparse-syslogbase-expanded` ×1.91 `pcrec-auto` / ×2.51 `pcrec-vm`
— nearly doubling/2.5×ing). `-O1`/`-O3`/`-Os` all read essentially flat
at the median on both testees.

**`-O1`, which we did not predict against, costs real time on both
testees**: median ×1.04 (`pcrec-auto`, throughput) to ×1.16 (`pcrec-vm`,
search), with a genuine slower-side tail (`pcrec-vm` `router-prefix-order`
×2.14 throughput, `logparse-atomic` ×1.85 search).

Full distribution tables (median/Q1/Q3/extremes, every testee × regime ×
level, plus `pcrec-auto`'s own per-engine-category breakdown) are in the
ledger's §2, §3 and §6; the necessary-byte mechanism's full per-pattern
table is in §7. Nothing here depends on a v1.4 spread flag (all ten
records this window wrote read `agree`, 5 trials each).

No ask attached. If useful: this is the first direct, same-window
measurement of how much pcrec's OWN emitted-C choices (which engine, and
whether a necessary-byte guard's own scanned byte is present in the
subject) interact with the downstream compiler's optimization level — a
question your own artifact-consumer documentation may want an answer to,
independent of anything pcrec itself changes.
