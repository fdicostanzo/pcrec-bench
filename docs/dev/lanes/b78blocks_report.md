# [B78] lane report — I-93's five blocks, executed (I-57 terms: report, never diagnose)

Executor lane, I-57 terms. Every command run, every raw number, stated as
MEASURED. Deviations from I-93's literal text are listed in §0. Nothing
here is a conclusion the manager or Frank needs to re-derive from a
number this file omits.

## 0. Deviations from I-93's literal text (all mechanical, listed up front)

1. **BEFORE-pin CLI shape.** I-93/I-89 both give the pcrec invocation as
   `... -o OUT --pattern 'PATTERN'` (the D118 CLI). The BEFORE pin
   (`build/pcrec-25b1984f/build/pcrec`, abi 27) predates D118's reshape
   and only accepts the OLD shape: `pcrec [options] -o OUT.c [--]
   'PATTERN'` (confirmed via `--help`; `--pattern` is REFUSED as an
   unknown option). Block C's BEFORE-pin builds used `-o art.c --
   'PATTERN'` instead; the AFTER-pin builds (both Block A and Block C)
   used `--pattern 'PATTERN'` unchanged. This is the same fact
   `testees/pcrec/CLAUDE.md`'s "Re-pin at 8d716693" section already
   documents about this exact commit range.
2. **Block A did not pass `--features all`.** The bench's own `pcrec-auto`
   config always adds it; none of Block A's four patterns
   (`/user|/users`, the two near-miss classes, `\[`) uses a
   non-`std1` construct, so this is inert for these four patterns
   specifically — noted, not defended as generally safe.
3. **Block A/D use a hand-rolled instrument (I-89 §0.4's `findall.c`),
   never the bench's own `shim.c`/`driver.c`.** This instrument's
   absolute numbers read SYSTEMATICALLY DIFFERENT from the store's own
   committed numbers for the same patterns (§1.4, §4.4) — reported as a
   measured fact, not reconciled or explained.
4. Everything else (subjects, patterns, deny-flag spellings, the
   AFTER-pin build shape, the disassembly targets) follows I-93's text
   verbatim.

**Box facts for the whole lane:** `gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0`
(I-93 said gcc-15.2 — matches to the point release; no separate
`gcc-15.2` binary exists on this box, only the default `gcc`).
`GNU objdump/nm (GNU Binutils for Ubuntu) 2.46`. Box: quiet throughout
(`load average` sampled immediately before every timed phase, all
readings below 0.5 — see each block). BEFORE pin binary:
`/home/duxevents/pcrec-bench/build/pcrec-25b1984f/build/pcrec` (abi 27,
the bench's own committed build). AFTER pin binary:
`/tmp/optloop2/pcrec/build/pcrec`, confirmed
`git rev-parse HEAD` = `8d716693a57370853ff9e15a0606ccf0fea5b42f` (the
already-built worktree named in the brief, reused read-only). Subjects:
`bench/capability/throughput/t-{64k,256k,1m}.bin` exist at the exact
path I-93 names — **no substitution needed**; sha256 re-verified against
`bench/capability/manifest_throughput.tsv`, 3/3 match (§0.2 below).
Patterns: `bench/capability/patterns/<name>.rx`, read-only, verbatim.

---

## BLOCK E — perf availability check (done first; determined scope)

    $ cat /proc/sys/kernel/perf_event_paranoid
    4

Matches I-93's own expectation ("expected: it is 4"). **SKIPPED per the
brief's instruction** — no attempt made to change it.

---

## BLOCK B — the null-control band, both directions (no new runs; read from store)

### Method and identity criterion (stated in full, since I-93 asks for it)

Read ONLY from the eight committed records
`store/records/capability@0.1/pcrec_{25b1984f,8d716693}_{auto-caps,auto-nocaps,vm-caps,vm-in-caps}-simdna/*.jsonl`
(read-only), via `pcrecbench.reduce.cells_from_record` /
`reduce_set_cell` / `read_record` imported directly — the same functions
`docs/dev/ledgers/2026-09-23-optloop1-batch1-after-8d716693.md` §0.2
used, not a re-implementation. Script:
`/tmp/optloop3/blockb.py` (scratch, not committed).

**Program-identity criterion used** (stated once, applied uniformly): a
pattern is counted PROGRAM-IDENTICAL on one of the three distinct
emitted artifacts (`auto-caps`, `auto-nocaps`, `vm-caps` — `vm-in-caps`
reuses the `vm-caps` artifact, confirmed: 0 `emit_bytes` mismatches
between the two AFTER records over the whole corpus) iff, comparing its
BEFORE (abi 27) and AFTER (abi 29) `compile` rows' PLAIN form:

  (a) both sides show `compile_outcome == "compiled"` (a refusal on
      either side excludes the pattern, never counted identical);
  (b) every `engine_metadata` key present on EITHER side, other than
      `abi`, `emit_bytes`, `emit_code_bytes` and the three abi-29
      additions (`req_byte`, `end_window`, `vm_start`), is EQUAL — a
      STAMP-EQUALITY test (engine, engine_sel, vm_program_bytes,
      vm_entry_shape, vm_frameless, resume_frames, dfa_*, altcls_*,
      scan_edges, ...), not a byte-level source diff, because the record
      does not carry the emitted `.c`/`.h` text or a hash of it;
  (c) where present on the AFTER side, `req_byte`/`end_window`/
      `vm_start` read the NEUTRAL/INERT value (`"none"` / `"none"` /
      `"unanchored"`) — i.e. none of the three abi-29 mechanisms fired.

`emit_bytes`/`emit_code_bytes` (the WHOLE emitted `.c`+`.h` byte counts)
are DELIBERATELY EXCLUDED from the equality test: MEASURED here that
they grow by a small, PATTERN-DEPENDENT boilerplate amount on every
abi-29 artifact regardless of whether any mechanism fired — +89 B on
most VM artifacts, +168/+201 B on others (the new `#define` lines' own
text length, which varies with the printed values) — confirmed
concretely on `phone-palindrome-6`, one of the pcrec ledger's own
byte-identical-`.text` witnesses (`docs/dev/optloop/cycle1_ledger_reading.md`
§1): its `emit_bytes` still moves +89 B despite the compiled object
being unchanged. Using `emit_bytes` as the gate would have produced ZERO
identical patterns.

### Result: 15 program-identical patterns (not 16)

    currency-lookbehind-fixed, doubled-word, high-byte-run,
    phone-palindrome-6, quoted-delim-match, utf8-lead-no-cont,
    wild-codegrammar-json-constant, wild-codegrammar-json-number-extended,
    wild-logparse-base10num-grok, wild-logparse-base10num-noatomic,
    wild-logparse-quotedstring-grok, wild-logparse-quotedstring-noatomic,
    wild-semdiv-empty-alt-repeat-pcre2, wild-waf-crs-942140-dbnames,
    wild-waf-crs-942270-union-select

MEASURED, not diagnosed: this is 15, where I-93/the pcrec reading cite
16. All FOUR of the pcrec ledger's own named byte-identical `.text`
witnesses (`phone-palindrome-6`, `quoted-delim-match`,
`wild-codegrammar-json-constant`, `wild-logparse-quotedstring-noatomic`)
ARE in this list, and the single worst cell my criterion finds
(`phone-palindrome-6`/`large-subject-throughput`/`auto-caps`, +8.4605%)
matches the pcrec reading's own cited worst case (+8.46%) to the fourth
significant figure — cross-validating the method despite the population
count differing by one. The count difference is attributable to a
different identity method (stamp-equality over the record's own metadata
here vs. an actual compiled-object byte diff on the pcrec side) — stated
as fact, not chased further per I-57 terms.

### Two-sided band, all 120 cells (15 patterns × 2 regimes × 4 testees)

Full per-cell table: `/tmp/optloop3/blockb_output2.txt` (scratch). Summary:

    n cells = 120
    min = -5.7393%   max = +8.4605%
    median = -0.0806%   mean = -0.4488%
    regressing (>0): 41   worst = +8.4605%
    improving (<0): 79    best  = -5.7393%

The band is now explicitly TWO-SIDED (I-93's ask): 79 of 120
program-identical cells read as "improving" and 41 as "regressing" by
the same arithmetic that, applied one-sidedly, produced the ledger's
16-cell regression-only reading. The single largest movement either
direction is `phone-palindrome-6` on `large-subject-throughput`
(auto-caps +8.46%, vm-in-caps −5.74%, vm-caps −5.42%,
short-subject-search auto-caps −5.56%) — one pattern accounts for both
tails of the band. `wild-semdiv-empty-alt-repeat-pcre2`'s
`short-subject-search`/`auto-nocaps` cell reads −3.69%, the second
largest movement. No further significance asserted; the numbers are
the deliverable.

---

## BLOCK A — axis isolation, timing (AFTER pin only)

Patterns/configs, AFTER pin (`/tmp/optloop2/pcrec/build/pcrec`, abi 29):
`router-prefix-order` (`auto`, `--no-captures`), `uuid-near-miss` (auto),
`ipv4-near-miss` (auto), `wild-codegrammar-json-array-begin` (auto).
Four builds each: default, `-fno-req-byte`, `-fno-end-window`, both
together. Build shape: `pcrec -p rx [--no-captures] [deny-flags] -o
art.c --pattern '<text>'` then `gcc -O2 -I<dir> -o <bin> findall.c
art.c` (I-89 §0.4's driver, verbatim; the naming/build line from
`cycle1_analysis.md` 0.5 as quoted in inbox I-89). Scratch:
`/tmp/optloop3/blockA/`.

**Stamp control (before trusting any timing): the deny flags land
exactly where the earlier O-45 census said they would** —

    router-prefix-order  default: REQ_BYTE "114" END_WINDOW "none"
    uuid-near-miss        default: REQ_BYTE "45"  END_WINDOW "37"
    ipv4-near-miss         default: REQ_BYTE "46"  END_WINDOW "16"
    wild-codegrammar-json-array-begin default: REQ_BYTE "91" END_WINDOW "none"

(all four `-fno-req-byte` builds read `REQ_BYTE "none"`; all four
`-fno-end-window` builds on uuid/ipv4 read `END_WINDOW "none"`) — an
exact match to the record's own `req_byte`/`end_window` values
(`docs/dev/ledgers/2026-09-23-optloop1-batch1-after-8d716693.md` §3.2).

**Timing: uptime before = `load average: 0.23, 0.17, 0.38`** (load1 <
0.5, quiet). 5 trials, interleaved across all four variants each round
(order: default, noreqbyte, noendwin, noboth, repeated 5×). One "trial"
= one process launch per subject (3 launches), summing each launch's
internal best-of-5 (`argv[2]=5`) `best` time in ns; sums over the 3
throughput subjects. Full raw output: `/tmp/optloop3/blockA/time_output.txt`.
`matches=` identical across all four variants of every pattern on every
trial (answer identity holds under both deny flags — `[9,58,245]` for
router, `[0,0,0]` for uuid/ipv4, `[382,1449,5985]` for the json pattern).

| pattern | variant | median (ns) | IQR (ns) | Δ vs default |
|---|---|---:|---:|---:|
| router-prefix-order | default | 867,510.0 | 295,590.0 | +0.00% |
| router-prefix-order | noreqbyte | 793,050.0 | 270,420.0 | −8.58% |
| router-prefix-order | noendwin | 870,150.0 | 1,490.0 | +0.30% |
| router-prefix-order | noboth | 858,821.0 | 119,410.0 | −1.00% |
| uuid-near-miss | default | 210.0 | 20.0 | +0.00% |
| uuid-near-miss | noreqbyte | 190.0 | 60.0 | −9.52% |
| uuid-near-miss | noendwin | 240.0 | 20.0 | **+14.29%** |
| uuid-near-miss | noboth | 210.0 | 10.0 | +0.00% |
| ipv4-near-miss | default | 210.0 | 10.0 | +0.00% |
| ipv4-near-miss | noreqbyte | 190.0 | 10.0 | −9.52% |
| ipv4-near-miss | noendwin | 220.0 | 10.0 | **+4.76%** |
| ipv4-near-miss | noboth | 200.0 | 20.0 | −4.76% |
| wild-codegrammar-json-array-begin | default | 772,630.0 | 132,319.0 | +0.00% |
| wild-codegrammar-json-array-begin | noreqbyte | 577,220.0 | 11,500.0 | −25.29% |
| wild-codegrammar-json-array-begin | noendwin | 773,320.0 | 130,949.0 | +0.09% |
| wild-codegrammar-json-array-begin | noboth | 578,230.0 | 10,550.0 | −25.16% |

### EXPECT vs measured (stated, never reconciled)

1. **"-fno-req-byte recovers the BEFORE number on all four"**: DIRECTION
   confirmed on all four (noreqbyte < default in every case: −8.58%,
   −9.52%, −9.52%, −25.29%). ABSOLUTE recovery to the store's own cited
   BEFORE numbers (router 393,757–393,998 ns; uuid 19.9–20.4 ns; ipv4
   18.7–18.8 ns; json-array-begin 263,616–263,784 ns) does NOT hold under
   this instrument — every one of my noreqbyte medians is 2×–10× the
   cited BEFORE value (793,050 vs ~393,900; 190 vs ~20; 190 vs ~18.8;
   577,220 vs ~263,700). This scale gap is present on EVERY cell,
   including the trivial near-instant ones, so it reads as a property of
   the `findall.c` instrument relative to the bench's own `shim.c`/
   `driver.c` harness (§0 deviation 3), not a per-pattern anomaly —
   measured, not diagnosed.
2. **"-fno-end-window leaves uuid/ipv4 WORSE than default"**: CONFIRMED
   in direction on both (uuid +14.29%, ipv4 +4.76%), consistent with the
   memchr window (37/16 bytes) being a genuine narrowing that a scan
   without it does not get.
3. **"router's -fno-req-byte number is within its IQR of 393,757 ns"**:
   NOT MET under this instrument's absolute scale — noreqbyte reads
   793,050 ns (IQR 270,420), nowhere near 393,757 ± that IQR. Same scale
   gap as point 1.

---

## BLOCK C — VM placement mechanism, disassembly only, both pins

Patterns: `nested-comment-rec` (auto, `--features all`),
`float-literal-bound`/`file-ext-order`/`wild-secrets-github-pat`
(`--engine=vm`, `--features all`). Built as standalone `.o` files
(`gcc -O2 -std=gnu11 -fPIC -c art.c -o art.o`, matching the bench's real
`-fPIC` compile flag; re-verified identical results without `-fPIC` too)
at BOTH pins. Scratch: `/tmp/optloop3/blockC/`.

### (i) `nm | grep rx_search_run` — `.part.0` presence

    nested-comment-rec / before:  rx_search_run present, NO .part.0
    nested-comment-rec / after:   rx_search_run present, NO .part.0
    float-literal-bound / before: rx_search_run present, NO .part.0
    float-literal-bound / after:  rx_search_run present, NO .part.0
    file-ext-order / before:      rx_search_run present, NO .part.0
    file-ext-order / after:       rx_search_run present, NO .part.0
    wild-secrets-github-pat / before: NO rx_search_run symbol at all
    wild-secrets-github-pat / after:  NO rx_search_run symbol at all

**EXPECT ("`.part.0` present at 25b1984f and ABSENT at 8d716693 on the
first three") REFUTED on gcc-15.2/x86_64: no `.part.0` symbol appears on
EITHER pin, on any of the three.** I-93 itself flagged this as an
arm64/gcc-16 reading needing replication; it does not reproduce here.

`wild-secrets-github-pat` has no `rx_search_run` at all, on either pin —
its full symbol table (`rx_search`, `rx_search_in`, `rx_match`,
`rx_match_in`, `rx_match_caps`, `rx_match_caps_in`, `rx_next_pos`,
`rx_class_bitmap0`, `rx_info`) never includes it. Not investigated
further (out of scope for "report, never diagnose").

### (ii) `objdump -d rx_search_run` — call vs inline, instruction count

All three (nested-comment-rec, float-literal-bound, file-ext-order), BOTH
pins: `rx_search_run` CALLS `rx_match_anchored` (an out-of-line call —
`call ... <rx_match_anchored>`, `R_X86_64_PLT32 rx_match_anchored`),
never inlined, on both pins.

**AFTER-pin-only finding, all three patterns, from `objdump -dr`'s own
relocation records:** `rx_search_run` gains ONE new `call` at its very
top, before the bounds check's loop entry, resolved by relocation to
`memchr` (`R_X86_64_PLT32 memchr-0x4`) — the compiled req_byte pre-check
call, with the exact byte constant matching the record's stamped
`req_byte` value: nested-comment-rec `mov $0x2f,%esi` (47, `'/'`),
float-literal-bound `mov $0x2e,%esi` (46, `'.'`), file-ext-order
`mov $0x72,%esi` (114, `'r'`). This is the placement I-93's whole
hypothesis is about, confirmed directly on this box's compiler.

Instruction line counts (`objdump -dr --disassemble=rx_search_run`,
counting disassembled instruction lines):

| pattern | before | after |
|---|---:|---:|
| nested-comment-rec | 97 | 107 |
| float-literal-bound | 87 | 96 |
| file-ext-order | 79 | 96 |

`__stack_chk_fail` is called exactly once in `rx_search_run` on BOTH
pins, all three patterns (canary present at both pins — NOT an
AFTER-only addition).

### (iii) frame size and `__stack_chk`

| pattern | pin | callee-saved pushes | `sub $N,%rsp` | total stack footprint |
|---|---|---|---:|---:|
| nested-comment-rec | before | r13,r12,rbp,rbx (4) | 0x48 (72) | 104 B |
| nested-comment-rec | after | r14,r13,r12,rbp,rbx (5) | 0x40 (64) | 104 B |
| float-literal-bound | before | r14,r13,r12,rbp,rbx (5) | 0x40 (64) | 104 B |
| float-literal-bound | after | r14,r13,r12,rbp,rbx (5) | 0x40 (64) | 104 B |
| file-ext-order | before | r14,r12,rbp,rbx (4) | 0x48 (72) | 104 B |
| file-ext-order | after | r14,r13,r12,rbp,rbx (5) | 0x40 (64) | 104 B |

**Total stack footprint (pushes×8 + sub) is a FLAT 104 bytes in all six
cases.** Where the AFTER pin adds the memchr pre-check, `nested-comment-rec`
and `file-ext-order` each gain exactly one more callee-saved push (r13 in
both cases) and shed 8 bytes of `sub`-allocated locals in exchange — a
wash on the total, consistent with the compiler keeping one more
pointer live across the new call rather than growing the frame.
`float-literal-bound` already pushed 5 registers at BEFORE and its
`sub`/push split is unchanged by the AFTER pin's new call. `__stack_chk`
canary present on both pins throughout (see ii).

### (iv) hot-loop top: byte offset, 64-byte alignment

Offsets are the `.o` FILE's own section-relative offsets (as `objdump`
reports on the unlinked relocatable object) — a mechanical caveat, not a
finding: this is not necessarily the function's true RUNTIME load
address once linked into the `.so` the driver `dlopen`s, since the
linker/loader may relocate the section start. Reported as measured, not
as proof of true cache-line alignment.

| pattern | pin | loop-top offset | mod 64 | aligned? |
|---|---|---:|---:|---|
| nested-comment-rec | before | 0xc80 (3200) | 0 | yes |
| nested-comment-rec | after | 0xcc0 (3264) | 0 | yes |
| float-literal-bound | before | 0x4b0 (1200) | 48 | no |
| float-literal-bound | after | 0x4f0 (1264) | 48 | no |
| file-ext-order | before | 0x210 (528) | 16 | no |
| file-ext-order | after | 0x250 (592) | 16 | no |

Each pattern's own before/after loop-top offset shifts by exactly the
new call's own encoded size (nested-comment-rec +0x40, float-literal-bound
+0x40, file-ext-order +0x40 — all three shift by 64 bytes exactly, which
is why the mod-64 residue is IDENTICAL before/after on each pattern: the
inserted pre-check block happens to occupy exactly one 64-byte multiple
of code on all three witnesses here).

---

## BLOCK D — placement hand-twin, timing + acceptance test (AFTER pin, nested-comment-rec)

The AFTER-pin emitted C for `nested-comment-rec` carries the pre-check as
lines 418–420 of `rx_search_run` (quoted verbatim; line 417's bounds
check is UNCHANGED from the BEFORE pin and is not part of the pre-check):

```c
    if (search_from > subject_length) return 0;        /* line 417, unchanged at both pins */
    if (subject_length <= search_from ||                /* lines 418-420, NEW at abi 29 */
        !memchr(subject + search_from, 47, subject_length - search_from))
        return 0;
```

Four builds, all from this one emitted `art.c` (scratch:
`/tmp/optloop3/blockD/`):

- **(a) as-is** — `bin_a_asis`.
- **(b) the three pre-check lines (418-420) deleted by hand** from
  `rx_search_run`, line 417 left in place — `bin_b_deleted`.
- **(c) the same three lines MOVED** out of `rx_search_run` (line 417
  stays) and reinserted verbatim at the top of `rx_search`,
  `rx_search_in`, and `rx_search_deep` (each guards before doing
  anything else, including before `rx_search`'s fallback call into
  `rx_search_deep` on a frame give-up — so the fallback path re-runs the
  memchr check a second time by construction of this literal move) —
  `bin_c_moved`.
- **(d) as-is, compiled with `-fno-partial-inlining`** — `bin_d_nopartial`.

All four answer-checked before timing: `matches=[0,0,0]` on all three
throughput subjects, all four binaries (identical). No wrong answers.

**Timing: uptime before = `load average: 0.08, 0.09, 0.25`** (quiet). 5
trials, interleaved (a,b,c,d order, repeated 5×), each trial = sum of
3-subject best-of-5 (`argv[2]=5`) internal loop, same `findall.c`
protocol as Block A. Raw output: `/tmp/optloop3/blockD/time_output.txt`
(internal iters=5) and `time_output_i25.txt` (a repeat at iters=25, run
to check whether more internal repeats reduced trial-to-trial spread —
it did not materially).

| variant | median (ns), iters=5 | IQR | Δ vs (a) | median (ns), iters=25 | IQR | Δ vs (a) |
|---|---:|---:|---:|---:|---:|---:|
| (a) as-is | 8,751,088.0 | 597,890.0 | +0.00% | 9,314,519.0 | 953,113.0 | +0.00% |
| (b) deleted | 9,614,141.0 | 1,538,205.0 | +9.86% | 8,899,829.0 | 835,132.0 | −4.45% |
| (c) moved | 8,353,787.0 | 397,001.0 | −4.54% | 8,759,608.0 | 296,511.0 | −5.96% |
| (d) `-fno-partial-inlining` | 9,348,030.0 | 1,267,783.0 | +6.82% | 9,894,452.0 | 1,401,535.0 | +6.22% |

### EXPECT vs measured (stated, never reconciled)

**MEASURED, not resolved: the per-variant IQRs (300K–1.5M ns on medians
of 8.4M–9.9M ns, i.e. roughly 3–17% of the median) are comparable to or
larger than every reported Δ, and the sign of (b)'s delta FLIPS between
the two internal-iters settings (+9.86% at iters=5, −4.45% at
iters=25).** Under this instrument, at this trial count, none of the
four EXPECT clauses resolves cleanly:

- "(b) reproduces the BEFORE median 7,798,115 ns within its IQR" — NOT
  MET at either iters setting (8.90M–9.61M ns vs 7.80M ns store-cited;
  same absolute-scale gap as Block A, §0 deviation 3), and the relative
  direction (b faster or slower than a) is not stable across the two
  runs above.
- "(c) is the fix: within IQR of (b)" — (c) reads BELOW (a) in both
  runs (−4.54%, −5.96%) while (b) straddles both directions; not
  cleanly resolved either way given the overlapping IQRs.
- "(d) separates the partial-inlining route from plain layout" — (d)
  reads modestly slower than (a) in both runs (+6.82%, +6.22%,
  the most internally CONSISTENT of the three deltas across the two
  iters settings) but the effect size sits inside (a)'s and (d)'s own
  IQRs.

**Consistent with Block C's own finding (i): no `.part.0` split exists
on this compiler/architecture for this artifact at all**, so a probe
built to separate "the partial-inlining split" from "plain layout" is
asking a question this box's gcc-15.2/x86_64 build does not structurally
raise — matching the pcrec ledger's own §4.1 "perturbation" framing
(nested-comment-rec's own pre-check work is measured there at ≈25 ns
against a claimed ~1.5M ns delta, a 60,674× ratio) rather than a case
where the pre-check's own cost dominates. The three-throughput-subject
sum here (0 matches throughout) is dominated by the O(n) attempt-loop
scan itself (order 9M ns / 1,376,256 B ≈ 6.5-6.8 ns/B), against which a
layout-only perturbation of a few hundred K ns is the same order as this
instrument's own trial-to-trial noise floor — stated as the arithmetic
that explains why nothing resolves here, not as a diagnosis of pcrec's
compiler behavior.

---

## Summary of what changed vs I-93's literal asks

- Block E: skipped (paranoid=4, as expected).
- Block B: derived independently from records; 15 not 16
  program-identical patterns (worst cell matches the cited +8.46% to
  4 sig figs); two-sided band reported (min −5.74%, max +8.46%).
- Block A: built and timed; deny-flag stamps confirmed exact; direction
  of every EXPECT confirmed; ABSOLUTE recovery to the store's cited
  numbers NOT achieved under this hand-rolled instrument (systematic
  2×-10× scale gap vs. the bench's own driver, present on every cell).
- Block C: built and disassembled at both pins, all four named
  artifacts; the `.part.0` EXPECT is REFUTED on this box (none found on
  either pin); the memchr pre-check call IS compiled directly into
  `rx_search_run` at the AFTER pin on all three DFA-scan-bearing
  witnesses, confirmed by relocation records and the exact stamped
  byte constant; total stack frame footprint is an unchanged flat
  104 B; `wild-secrets-github-pat` has no `rx_search_run` symbol on
  either pin.
- Block D: all four variants built, answer-checked identical, timed;
  none of the three EXPECT clauses resolves cleanly against this
  instrument's own trial-to-trial noise, which is the same order of
  magnitude as the claimed effect.

Scratch artifacts (not committed, per the mandate): `/tmp/optloop3/`
(blockA/, blockC/, blockD/, blockb.py + its outputs, and the detached
worktree `pcrec-ead8bf62` used to read
`docs/dev/optloop/cycle1_ledger_reading.md`, fetched read-only from
pcrec origin).
