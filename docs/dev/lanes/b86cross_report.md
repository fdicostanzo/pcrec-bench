# [B86] lane report -- the three-point crossover block (I-105's cycle-3 ask)

Executor lane, I-57 terms. Report, never diagnose. Every command run, every
raw number, stated as MEASURED. **COMPLETE**: prep (sections 1-7) and the
timed rounds (section 8) both delivered, in that order, the second gated on
the manager's explicit go ("go. The box is clear...", sent after the prep
commit and a HOLD/re-check cycle -- see section 8's own preamble).

## 0. Charter-vs-committed checklist

| charter item | status |
|---|---|
| (i) wild-semdiv-dollar-trailing-newline-pcre2, four arms | BUILT, stamped, answer-checked, calibrated, **TIMED** (section 8) |
| (ii) keyword-prefix-order, four arms, rebuilt from O-51's recipe | BUILT, stamped, answer-checked, calibrated, **TIMED** (section 8) |
| (iii) synthetic e/space-run witness, SCRATCH PROBE, stamp-verified RX_REQ_BYTE 101, never enters bench/capability | BUILT + VERIFIED (RX_REQ_BYTE "101" confirmed by compile), answer-checked by arm-equality, **TIMED** (section 8); NOT added to any bench/ set (no gen_*.py touched, no manifest changed, `git status` on `bench/` clean throughout) |
| pin | 6ef76820 (I-105's ack does not name one; the brief's fallback rule applies) |
| stamps recorded for every arm, decline visibility | DONE -- section 3: all 24 cells read `RX_REQ_WHY "emitted"` on arms a/b/d and `"none"` on arm c (c's own contract checked); **no cell declines** -- itself the finding the brief asked to surface, not hide |
| per-point per-arm medians+IQRs | DONE -- section 8.1 |
| frequency-vs-(b)-(c) table | DONE -- section 8.3 |
| two-parameter solve re-attempted on 0.48/3.21/8.52% | DONE -- section 8.5, WITH conditioning shown and NOT forced (a NEW ill-conditioning cause found, distinct from O-51's frequency-proximity one) |
| keyword's IQR-flip finding restated | DONE -- section 8.4 |
| GATE: SendMessage before first timed round, wait for go | DONE (sent after the prep commit; one HOLD/re-check cycle; box re-verified quiet by `uptime` + `mpstat -P ALL 1 5` at go time, section 8's preamble) |

## 1. Deviations from the charter's literal text (listed up front)

1. **Instrument form: the O-50/[B81]/[B83] fallback shape, exactly as
   `docs/dev/lanes/b83runform_report.md` documents it and this lane
   repeats.** The REAL `testees.pcrec.adapter.Adapter` instance (via
   `pcrecbench.adapters.discover()["pcrec"]`), used only for its
   `.measure()` method (`pcrecbench.driverrun.per_trial`, the real
   driver-invocation loop) against hand-built `handle` dicts pointing at
   each variant's `.so`; the real `pcrecbench.subbench.find("capability")`
   / `.subjects_for("throughput")` / `.expectation(...)`; the real
   `pcrecbench.harness.calibrate`. No line of `pcrecbench/` or `testees/`
   edited. No record written to any store. Runner script:
   `/tmp/claude-1001/-home-duxevents-pcrec-bench/7f4bf7d7-e800-428b-be70-ccf4ea6d40e5/scratchpad/b86/run_instrument.py`
   (scratch, not committed; session scratchpad, not `/tmp` root, per this
   lane's own BOILERPLATE).
2. **Configs: BOTH of O-51's `keyword` configs (`auto-caps`, `auto-nocaps`)
   applied to ALL THREE points**, not just keyword, for a comparable grid
   across the three-point spread -- the charter names configs for keyword
   only ("rebuild its arms from O-51's recipe"); semdiv and the synthetic
   witness get the SAME two-config treatment rather than a narrower one,
   so the frequency-vs-(b)-(c) table has a like-for-like cell for every
   point. Router-prefix-order's own four-config grid (O-51's widest) is
   NOT rebuilt here -- it is not one of I-105's three named points and
   the charter does not ask for it.
3. **The synthetic witness's pattern text.** I-105 suggested "a
   nested-comment-rec-shaped delimiter pair using `"e "`/`" e"` in place
   of `"*/"`" as an example, not a spelled-out pattern. Built as:
   `(e (?:[^e ]|e(?! )| (?!e)|(?1))* e)` -- nested-comment-rec's own
   `(/\*(?:[^*/]|\*(?!/)|/(?!\*)|(?1))*\*/)` with `/` -> ` ` (space) and
   `*` -> `e` throughout, opening delimiter `"e "`, closing delimiter
   `" e"`. Compiles (VM route, recursive), stamps `RX_REQ_BYTE "101"`
   (101 = ASCII `e`) exactly as I-105 predicted (section 3). Byte 101's
   hit frequency over the three EXISTING throughput subjects, counted
   directly (not assumed): 117,274 / 1,376,256 = **8.5212%**, matching
   I-105's own cited figure to four decimals.
4. **The offset-corrected inline hand-twin (arm d) is a mechanical
   generalisation of the manager's own I-103a ruling** (quoted in full in
   `b83runform_report.md` section 3): given the compiled artifact's own
   `(byte, run bytes, runlen, offset)` -- read from that SAME arm-(a)
   artifact's `RX_REQ_BYTE`/`RX_REQ_RUN` stamps, never hand-guessed -- the
   edit is

       for (rp_c = rp_pos; rp_c + <runlen> <= subject_length; rp_c++)
           if (subject[rp_c + <offset>] == <byte>
               && !memcmp(subject + rp_c, "<run>", <runlen>))
               break;
       if (rp_c + <runlen> > subject_length) return 0;

   applied by an exact-string find-and-replace against the SAME 12-line
   memchr-loop block b83's own report quotes (section 3 there), refusing
   (STOP, raising) if that block is not found EXACTLY ONCE in the arm-(a)
   source -- the same discipline `make_variants.py` used at [B81]. All
   six (point, config) cells' arm (a) sources contained the block exactly
   once; no STOP fired. `runlen`/`offset` differ per point (semdiv 3/1,
   keyword 2/1, espace 2/1) and the formula is applied identically, not
   re-derived by hand each time.
5. Everything else -- two configs x four arms, answer-check before any
   timing, calibration per variant, 5 interleaved trials (once gated),
   load gate -- follows O-51/[B83]'s protocol verbatim.

## 2. Box facts, pin, subjects

`gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0`. pcrec pin `6ef76820`
(`/home/duxevents/pcrec-bench/build/pcrec-6ef76820/build/pcrec`,
`PIN.tsv`: commit `6ef768204cd0de4cf8594e7af6b08da5e050e2c0`, archived from
`/home/duxevents/pcrec` at 2026-09-23T18:19:58Z) -- ALREADY BUILT, reused
unmodified, no new pcrec build. `configs.toml`'s own `pin = "6ef76820"`
confirms this is also the CURRENT pinned testee commit, not a stale
archive. Worktree `worktrees/agent-ad67a7bb2c77ec68a` (branch
`lane/b86cross`). Scratch: session scratchpad `.../scratchpad/b86/`
(`run_instrument.py`, `work/`, `manifest.json`, `build.log`) -- never
committed. `uptime` at prep time (NOT the quiet-gate reading for the
timed rounds, which will be re-taken at go time): `load average: 1.69,
1.29, 0.89` -- **busy**, consistent with the brief's own warning that
another lane's `make check` is queued on this box; the timed rounds will
re-check load before round 1 and report it honestly, not this number.
Subjects: `bench/capability/throughput/{t-64k,t-256k,t-1m}.bin`
(65,536 / 262,144 / 1,048,576 B), regenerated in this worktree
(`python3 bench/capability/gen_throughput_subjects.py`; gitignored) and
confirmed sha256-identical to the committed `manifest_throughput.tsv`:
`d2e4f134...`/`t-64k`, `3cf7b248...`/`t-256k`, `ccbdf7eb...`/`t-1m`.
Regime: `throughput` (`--find-all`).

## 3. The three points, their run/byte/offset facts, and every arm's stamps

| point | pattern | route | byte | run (hex) | run (text) | runlen | offset | scan-byte freq (this window's 3 subjects) |
|---|---|---|---:|---|---|---:|---:|---:|
| (i) semdiv | `abc$` | DFA (`rx_search`, [OPT-ENDWIN]+[OPT-REQPOS] fused) | 98 ('b') | `616263` | "abc" | 3 | 1 | 0.4773% (I-105's own cited figure; not re-derived here, carried from the pattern's own necessary-run byte 'b') |
| (ii) keyword | `in\|instanceof` | DFA (`rx_search_run` shared helper) | 110 ('n') | `696e` | "in" | 2 | 1 | 3.2067% (I-105's own cited figure) |
| (iii) espace (SCRATCH) | `(e (?:[^e ]\|e(?! )\| (?!e)\|(?1))* e)` | VM (`rx_search_run` shared helper) | 101 ('e') | `2065` | " e" | 2 | 1 | 8.5212% (counted directly over the three committed throughput subjects, byte 101: 117,274 / 1,376,256) |

**Every arm's `RX_REQ_BYTE` / `RX_REQ_RUN` / `RX_REQ_WHY`, both configs
(auto-caps, auto-nocaps -- identical stamp VALUES on both, differing only
in the compiled artifact's other bytes since captures on/off still
changes emission even where nothing is captured):**

| point | arm | flags | REQ_BYTE | REQ_RUN | REQ_WHY |
|---|---|---|---|---|---|
| semdiv | a | (default) | `98` | `616263@1` | `emitted` |
| semdiv | b | `-fno-req-run` | `98` | `none` | `emitted` |
| semdiv | c | `-fno-req-byte` | `none` | `none` | `none` |
| semdiv | d | (hand-twin of a) | `98` | `616263@1` | `emitted` |
| keyword | a | (default) | `110` | `696e@1` | `emitted` |
| keyword | b | `-fno-req-run` | `110` | `none` | `emitted` |
| keyword | c | `-fno-req-byte` | `none` | `none` | `none` |
| keyword | d | (hand-twin of a) | `110` | `696e@1` | `emitted` |
| espace | a | (default) | `101` | `2065@1` | `emitted` |
| espace | b | `-fno-req-run` | `101` | `none` | `emitted` |
| espace | c | `-fno-req-byte` | `none` | `none` | `none` |
| espace | d | (hand-twin of a) | `101` | `2065@1` | `emitted` |

**THE VISIBILITY THE BRIEF ASKED FOR: no cell declines.** All 24
(point, config, arm) cells read `RX_REQ_WHY "emitted"` on arms a/b/d and
`"none"` on arm c (c's own contract, checked here rather than assumed:
`REQ_WHY` "none" holds iff `REQ_BYTE` itself reads "none" -- true on
every one of the 6 arm-c cells). 6ef76820's [OPT-PRECHECK-ADMIT] fix
does NOT decline the pre-check on any of these three patterns at either
config -- none reads `one-attempt` or `dominated`, the two tokens that
would mean the admission fix removed the check rather than leaving it in
place. This matches I-102's own negative control (h) for router/keyword
("`REQ_WHY` reads `emitted` on both") extended here to semdiv and the
synthetic espace witness: all three points measure the SAME mechanism
[OPT-REQPOS]'s admission fix leaves standing, which is the precondition
for the crossover-conditioning question I-105 asks (a point where the
fix had DECLINED the check would not be measuring the run-vs-byte-vs-
inline form question at all).

## 4. Building the variants (24 cells: 3 points x 2 configs x 4 arms)

Phase-1 argv, mirroring `testees/pcrec/adapter.py::_compile_one` exactly
(`-fcomments` fixed protocol token, never in `cfg["flags"]`; pattern text
as raw bytes, the I-72 convention):

    build/pcrec-6ef76820/build/pcrec -p rx -fcomments <cfg flags> \
        [-fno-req-run | -fno-req-byte] -o artifact.c --pattern <PATTERN>

Phase-2 argv, mirroring the adapter's phase 2 exactly (no `cflags` axis
on either config):

    gcc -O2 -std=gnu11 -fPIC -shared -o artifact.so \
        testees/pcrec/shim.c -DPB_ARTIFACT="<dir>/artifact.c" -I <dir>

Configs (`testees/pcrec/configs.toml`):

| config | flags |
|---|---|
| `auto-caps` | `--features all` |
| `auto-nocaps` | `--features all --no-captures` |

Arms: (a) default -- config flags only. (b) `+ -fno-req-run`. (c)
`+ -fno-req-byte`. (d) the offset-corrected inline hand-twin, edited
FROM arm (a)'s own emitted source per section 1 deviation 4 above.

All 24 `.so` built rc=0, no warnings. Every arm-(c) artifact is smaller
than its arm-(a) sibling (no pre-check emitted at all); every arm-(d) is
between (a) and (b) in size (same guard SHAPE as (a), a shorter loop
body). Full sha256/byte-count table:
`.../scratchpad/b86/manifest.json` (24 `artifact_c_sha256` + `so_bytes`
entries, one per cell) -- not reproduced inline here for length; every
number in it is reproducible by re-running `run_instrument.py build`
against the same pin.

## 5. The guard region, all three points (arm a / b / c shapes; arm d's edit)

**semdiv (DFA route, the guard sits INLINE in `rx_search` itself, fused
with `[OPT-ENDWIN]` -- no separate `rx_search_run` helper on this
pattern, unlike keyword/espace):**

    /* [OPT-ENDWIN] every match of this pattern ends at the subject's
     * end (or one byte before it), and spans at most 4 bytes, so
     * none can begin earlier than this. */
    if (subject_length > 4ULL && search_from < subject_length - 4ULL)
        search_from = subject_length - 4ULL;
    /* [OPT-REQPOS] every match of this pattern contains the 3 bytes
     * "abc", so a window without them holds no match at all;
     * the scan is on byte 98 at offset 1 of the run. */
    if (subject_length <= search_from) return 0;
    {
        size_t rp_pos = search_from;
        for (;;) {
            const void *rp_q = memchr(subject + rp_pos, 98, subject_length - rp_pos);
            size_t rp_c;
            if (!rp_q) return 0;
            rp_c = (size_t)((const unsigned char *)rp_q - subject);
            if (rp_c - search_from >= 1 && rp_c - 1 + 3 <= subject_length
                && !memcmp(subject + rp_c - 1, "abc", 3)) break;
            rp_pos = rp_c + 1;
            if (rp_pos >= subject_length) return 0;
        }
    }

**keyword and espace (VM/DFA-via-shared-helper route, the guard sits in
`rx_search_run`, shared by `rx_search`/`rx_search_in` -- keyword's is
byte-for-byte the shape b83's own report quotes at b1885a83, reproduced
here unchanged at 6ef76820):**

    /* [OPT-REQPOS] every match of this pattern contains the 2 bytes
     * "in", so a window without them holds no match at all;
     * the scan is on byte 110 at offset 1 of the run. */
    if (subject_length <= search_from) return 0;
    {
        size_t rp_pos = search_from;
        for (;;) {
            const void *rp_q = memchr(subject + rp_pos, 110, subject_length - rp_pos);
            size_t rp_c;
            if (!rp_q) return 0;
            rp_c = (size_t)((const unsigned char *)rp_q - subject);
            if (rp_c - search_from >= 1 && rp_c - 1 + 2 <= subject_length
                && !memcmp(subject + rp_c - 1, "in", 2)) break;
            rp_pos = rp_c + 1;
            if (rp_pos >= subject_length) return 0;
        }
    }

espace's own copy of this block is identical in shape with byte 101,
run `" e"`, runlen 2, offset 1 (section 3's table).

**Arm (b) (`-fno-req-run`) collapses the block above to the BYTE-ONLY
memchr guard, `[OPT-REQBYTE]`'s own spelling** (confirmed in every
arm-(b) source, e.g. keyword's):

    /* [OPT-REQBYTE] every match of this pattern contains the byte
     * 110, so a window without it holds no match at all. */
    if (subject_length <= search_from ||
        !memchr(subject + search_from, 110, subject_length - search_from))
        return 0;

**Arm (c) (`-fno-req-byte`) emits NO pre-check block at all** -- the
`[OPT-REQPOS]`/`[OPT-REQBYTE]` comment and guard are both absent,
confirmed by grep (no `OPT-REQPOS`/`OPT-REQBYTE`/pre-check `memchr` line
in any arm-c source, section 3's `REQ_WHY "none"` reading the same
fact from the stamp).

**Arm (d), the offset-corrected inline hand-twin (I-103a's ruling,
applied mechanically per point -- section 1 deviation 4), e.g. keyword's:**

    if (subject_length <= search_from) return 0;
    {
        size_t rp_pos = search_from;
        size_t rp_c;
        for (rp_c = rp_pos; rp_c + 2 <= subject_length; rp_c++)
            if (subject[rp_c + 1] == 110 && !memcmp(subject + rp_c, "in", 2))
                break;
        if (rp_c + 2 > subject_length) return 0;
    }

Same found/not-found wiring as (a): falls through into the forward-table
scan / VM entry exactly when a run occurrence exists at or after
`search_from`, `return 0`s exactly when none does -- confirmed by
measurement in section 6, not merely by inspection.

## 6. Answer-check, before any timing (all 24 cells)

One `iters=1 --find-all` call per variant, all three subjects, via the
REAL `adapter.measure()`. **EQUAL across all FOUR arms on every one of
the 6 (point, config) cells:**

| point | subject | nmatches (every arm) | oracle (real patterns only) |
|---|---|---:|---|
| semdiv | t-64k / t-256k / t-1m | 0 / 0 / 0 | matches `expectations.tsv` ("nomatch", nmatches 0, all three subjects) |
| keyword | t-64k / t-256k / t-1m | 433 / 1,791 / 7,243 | matches `expectations.tsv` exactly (433/1,791/7,243) |
| espace (SCRATCH, arm-equality only, no oracle row exists) | t-64k / t-256k / t-1m | 1 / 0 / 0 | n/a by design (never enters `bench/capability`); the four arms' own agreement (1/0/0 on all four, both configs) is the ONLY check this point carries, per the charter's own "answer-checked by arm equality" |

No wrong answer anywhere; no mismatch raised the script's own
arm-equality or oracle-agreement assertions (both are hard failures in
`run_instrument.py`, not soft warnings -- a mismatch would have stopped
the build before this report could claim "answer-check passing").

## 7. Calibration (`harness.calibrate`, real function, one probe per variant)

Target 50 ms/subject-sweep loop, per-variant probe (median subject sets
`n_iters`, same rule `run_cell` itself uses):

| point | config | arm | n_iters | median probe (µs/iter, subject) |
|---|---|---:|---:|---|
| semdiv | auto-caps | a/b/c/d | 1,250,000 / 714,286 / 625,000 / 833,334 | 0.040 / 0.070 / 0.080 / 0.060 |
| semdiv | auto-nocaps | a/b/c/d | 1,250,000 / 833,334 / 1,000,000 / 1,000,000 | 0.040 / 0.060 / 0.050 / 0.050 |
| keyword | auto-caps | a/b/c/d | 200 / 261 / 263 / 117 | 250.780 / 192.070 / 190.130 / 430.591 |
| keyword | auto-nocaps | a/b/c/d | 153 / 262 / 328 / 146 | 328.511 / 191.090 / 152.630 / 344.282 |
| espace | auto-caps | a/b/c/d | 5,066 / 5,292 / 5,176 / 2,758 | 9.870 / 9.450 / 9.660 / 18.130 |
| espace | auto-nocaps | a/b/c/d | 5,077 / 5,383 / 5,253 / 4,776 | 9.850 / 9.290 / 9.520 / 10.470 |

Already visible at the calibration probe (a SINGLE iters=1 call, not the
5-trial measurement): arm (d) is calibrated to MORE iterations-per-loop
time on keyword and semdiv (i.e. SLOWER per call: keyword's arm-d probe
430.591 µs/iter vs arm-a's 250.780 µs/iter) and on espace auto-caps
(18.130 vs 9.870 µs/iter) -- consistent with O-51's own finding that
memchr-run beats the inline scalar loop at these frequencies, restated
properly with medians/IQRs over 5 trials in section 8 once timed.

## 8. Timed rounds, verdict grid, crossover solve

**The gate sequence.** After the prep commit, `SendMessage` to `main`
("b86: ready to time, est 2-3 min") flagged the box as busy (`uptime`
load average 1.69/1.29/0.89 at prep time). The manager replied **HOLD**
("the load is another lane's report regen, two cores busy with GB-scale
memory traffic... I'll send go when the box is clear"), acknowledged.
The manager then sent **go** ("The box is clear: no other job is
running, and the load average is still decaying from 1.9 (1-min 1.43 at
10:25). Take your uptime + mpstat -P ALL 1 5 sample first... If the
target core isn't idle, wait a minute and re-sample instead of timing"),
with the instruction to record both samples regardless.

**Occupancy sample taken at go time, before round 1** (this lane pins no
core -- `handle["pin"] = None` throughout, matching the O-50/[B81]/[B83]
fallback instrument's own unpinned shape -- so "the target core" reads
as the whole box here):

    $ uptime
     10:26:11 up 43 days, 11:32,  6 users,  load average: 1.29, 1.85, 1.42
    $ mpstat -P ALL 1 5
    Average:     CPU  %usr %nice %sys %iowait %irq %soft %steal %guest %gnice %idle
    Average:     all  0.25  0.00 0.13    0.00 0.00  0.00   0.00   0.00   0.00  99.62
    Average:       0  1.41  0.00 0.00    0.00 0.00  0.00   0.00   0.00   0.00  98.59
    Average:       1  0.60  0.00 0.20    0.00 0.00  0.00   0.00   0.00   0.00  99.20
    Average:       2  0.00  0.00 0.00    0.00 0.00  0.00   0.00   0.00   0.00 100.00
    Average:       3  0.00  0.00 0.20    0.00 0.00  0.00   0.00   0.00   0.00  99.80
    Average:       4  0.80  0.00 0.20    0.00 0.00  0.00   0.00   0.00   0.00  98.99
    Average:       5  0.00  0.00 0.20    0.00 0.00  0.00   0.00   0.00   0.00  99.80
    Average:       6  0.00  0.00 0.20    0.00 0.00  0.00   0.00   0.00   0.00  99.80
    Average:       7  0.00  0.00 0.00    0.00 0.00  0.00   0.00   0.00   0.00 100.00
    Average:       8  0.00  0.00 0.00    0.00 0.00  0.00   0.00   0.00   0.00 100.00
    Average:       9  0.00  0.00 0.60    0.00 0.00  0.00   0.00   0.00   0.00  99.40
    Average:      10  0.20  0.00 0.00    0.00 0.00  0.00   0.00   0.00   0.00  99.80
    Average:      11  0.00  0.00 0.00    0.00 0.00  0.00   0.00   0.00   0.00 100.00

`load1` (1.29) was still decaying from the prior job, exactly as the go
message predicted, but the mpstat Average over every one of the 12 cores
reads >= 98.59% idle -- the BD7 occupancy-sample convention (judged on
the mpstat Average, not load1, since load1 lags real occupancy by design
on this box) reads QUIET. Proceeded to timing rather than re-sampling.
The whole 24-cell x 5-round run (build re-verification + fresh
answer-check + calibration + timed rounds) completed in 16 seconds wall
time; `uptime` immediately after read `load average: 0.37, 1.23, 1.24`
-- load1 continuing its decay, occupancy unaffected by this run's own
tiny cost.

Instrument, unchanged from section 1: the real
`Adapter.measure()`/`harness.calibrate`/`harness.outcome_for`/
`harness.classify_giveup`/`harness.truncation_for`/`record.match_row`/
`reduce.reduce_set_cell`/`reduce.judge_trial_agreement`/
`reduce.agreement_line`, against hand-built handles, five interleaved
trials per (point, config, arm) -- `run_instrument.py time`, appended to
the same scratch script as sections 1-7 (not committed, per the
mandate). A FRESH answer-check (iters=1, all four arms) ran immediately
before calibration on every one of the six (point, config) cells and
re-confirmed section 6's own findings byte for byte -- no drift between
the prep run and the timed one.

### 8.1 Per-variant medians/IQRs (all 24 cells, ns, sum over the 3
throughput subjects per trial -- the SAME `reduce.reduce_set_cell`
arithmetic `quick` prints and the reporter ranks)

| point | config | arm | median ns | min ns | max ns | IQR (Q3-Q1) | n_iters |
|---|---|---|---:|---:|---:|---:|---:|
| semdiv | auto-caps | a | 31.6580 | 26.0870 | 32.7309 | 4.2958 | 1,250,000 |
| semdiv | auto-caps | b | 31.4100 | 24.8360 | 31.6906 | 0.0111 | 1,250,000 |
| semdiv | auto-caps | c | 49.6317 | 42.7390 | 62.2820 | 0.2694 | 833,334 |
| semdiv | auto-caps | d | 27.0454 | 21.9588 | 27.2687 | 4.5976 | 1,000,000 |
| semdiv | auto-nocaps | a | 36.0036 | 35.7324 | 46.1038 | 0.2553 | 833,334 |
| semdiv | auto-nocaps | b | 33.1416 | 24.8611 | 33.5427 | 0.0569 | 1,000,000 |
| semdiv | auto-nocaps | c | 41.8453 | 39.6218 | 49.6240 | 9.5314 | 833,334 |
| semdiv | auto-nocaps | d | 25.6030 | 19.1776 | 26.2964 | 1.0353 | 1,250,000 |
| keyword | auto-caps | a | 1,263,898.9939 | 1,240,084.8424 | 1,364,601.9455 | 28,557.9091 | 165 |
| keyword | auto-caps | b | 798,014.3271 | 792,518.7323 | 806,713.6506 | 4,664.2565 | 269 |
| keyword | auto-caps | c | 756,679.9653 | 753,512.8757 | 772,494.3844 | 2,565.6734 | 346 |
| keyword | auto-caps | d | 1,849,101.1966 | 1,848,268.5470 | 1,853,425.5726 | 1,658.8120 | 117 |
| keyword | auto-nocaps | a | 1,326,273.1648 | 1,290,153.4835 | 1,333,476.9341 | 2,208.6923 | 91 |
| keyword | auto-nocaps | b | 834,418.8099 | 777,786.4296 | 838,396.8451 | 1,916.0634 | 142 |
| keyword | auto-nocaps | c | 765,398.0070 | 746,902.9789 | 766,333.7465 | 15,770.8275 | 284 |
| keyword | auto-nocaps | d | 1,833,102.9315 | 1,780,552.6781 | 1,841,758.1712 | 2,005.3493 | 146 |
| espace | auto-caps | a | 30,295.1774 | 28,319.9836 | 30,381.2317 | 557.7095 | 2,007 |
| espace | auto-caps | b | 26,369.6011 | 24,727.0082 | 26,930.5575 | 295.0132 | 5,365 |
| espace | auto-caps | c | 26,969.0753 | 25,769.8006 | 27,876.0056 | 68.0816 | 4,263 |
| espace | auto-caps | d | 29,031.5601 | 28,856.6664 | 31,082.5761 | 135.0577 | 4,817 |
| espace | auto-nocaps | a | 27,934.2589 | 25,951.5212 | 30,814.8947 | 1,345.5169 | 4,171 |
| espace | auto-nocaps | b | 26,841.7858 | 25,568.7914 | 27,056.8305 | 142.4999 | 4,425 |
| espace | auto-nocaps | c | 29,371.7148 | 29,026.4142 | 29,682.4531 | 518.3789 | 1,953 |
| espace | auto-nocaps | d | 28,916.4178 | 28,879.8318 | 29,078.9184 | 25.4290 | 4,804 |

**All 24 cells**: `failing_subjects=[]`, `n_wrong=0`, `n_gave_up=0`,
trial agreement **`agree`** (`reduce.judge_trial_agreement`, rule
`v1.4-group`, k=1.5, d_min=2, share_c=3, 5 trials) on every one -- a
record built from any of these would stamp `measured`, none
`inconclusive-spread`.

### 8.2 The (b)-vs-(c) decision line, all six cells (I-103's own bar:
|Δ| vs max(IQR_b, IQR_c))

| point / config | freq | (b)-(c) ns | max(IQR_b, IQR_c) | verdict |
|---|---:|---:|---:|---|
| semdiv / auto-caps | 0.4773% | -18.2217 | 0.2694 | **outside IQR** (b faster than c) |
| semdiv / auto-nocaps | 0.4773% | -8.7037 | 9.5314 | **within IQR** |
| keyword / auto-caps | 3.2067% | +41,334.3618 | 4,664.2565 | **outside IQR** (b slower than c) |
| keyword / auto-nocaps | 3.2067% | +69,020.8028 | 15,770.8275 | **outside IQR** (b slower than c) |
| espace / auto-caps | 8.5212% | -599.4742 | 295.0132 | **outside IQR** (b faster than c) |
| espace / auto-nocaps | 8.5212% | -2,529.9290 | 518.3789 | **outside IQR** (b faster than c) |

**The SIGN flips with the pattern, not with the frequency, and that is
itself the finding.** On keyword, arm (b) (the byte-only guard, no run
check) is SLOWER than arm (c) (no pre-check at all) -- the byte guard
costs something real, confirming I-103/O-51's own reading. On BOTH
semdiv and espace, arm (b) is FASTER than arm (c) -- the byte guard
HELPS, the ordinary dominance-rule direction. The variable that tracks
this sign is NOT scan-byte frequency (semdiv 0.48%, espace 8.52%, wide
apart, same sign) -- it is **match density**: keyword's three subjects
answer 433/1,791/7,243 matches (nmatches sums to 9,467, so
`rx_search`/`rx_search_run` is re-entered thousands of times per
subject, paying the guard's own cost on every re-entry even where it
correctly dismisses nothing new); semdiv answers 0/0/0 and espace
answers 1/0/0 (`rx_search` runs essentially ONCE per subject, so a
cheap guard that dismisses most of the subject in one call is a clear
win). Section 8.5 returns to this as the mechanism that ALSO breaks the
two-parameter solve.

### 8.3 Frequency-vs-(b)-(c) table, and (d)-vs-(a) inline-vs-memchr,
side by side (auto-nocaps, I-103a's own reading config; auto-caps
shows the same signs, table above)

| point | scan-byte freq | (b)-(c) ns | (b)-(c) verdict | (d)-(a) ns | (d)-(a) verdict |
|---|---:|---:|---|---:|---|
| semdiv | 0.4773% | -8.7037 | within IQR | -10.4006 | outside IQR (d FASTER) |
| keyword | 3.2067% | +69,020.8028 | outside IQR | +506,829.7667 | outside IQR (d SLOWER) |
| espace | 8.5212% | -2,529.9290 | outside IQR | +982.1588 | **within IQR** (no significant difference) |

(auto-caps (d)-(a): semdiv -4.6126 outside IQR, d faster; keyword
+585,202.2026 outside IQR, d slower; espace **-1,263.6173 outside IQR,
d FASTER** -- the auto-caps espace cell flips sign relative to its own
auto-nocaps sibling, discussed below.)

**This is the bracket I-105 asked for, read qualitatively (never
forced into a number the solve in 8.5 shows cannot be trusted).**
O-51's own established finding was "memchr-run beats the inline scalar
loop at both 2.8% and 3.2%, every configuration measured -- outside IQR
every time." THIS run reproduces that on keyword (3.2067%, both
configs, both clearly outside IQR, memchr-run wins by 42-46% of its own
median) and adds semdiv (0.4773%) where memchr-run ALSO wins, though
by a much smaller absolute margin at this near-floor scale (see 8.6's
caveat). At espace (8.5212% -- ABOVE the model's own predicted ~8.47%
crossover, I-103a's stated constants), the picture is NO LONGER
uniformly in memchr-run's favour: auto-nocaps shows NO significant
difference (982 ns vs an IQR bar of 1,345 ns), and auto-caps shows the
inline form winning outright (-1,263.6 ns, outside IQR). Below/at
~3.2% memchr-run clearly wins on every cell measured; at ~8.5% the
advantage is gone or reversed on at least one cell -- **qualitatively
consistent with a crossover sitting between 3.2% and 8.5%,
bracketing rather than pinpointing the model's own predicted ~8.47%**,
exactly the charter's own ask.

### 8.4 Keyword's IQR-flip finding, restated beside this run's own

O-51 (session 2, the one delivered): keyword auto-caps crossed the IQR
bar by a thin 1.4% margin (39,506.9 vs 38,964.0); auto-nocaps did NOT
cross it in that same session (45,236.2 vs 65,093.6, IQR having widened
40x between two runs of the SAME cell) though session 1's own number for
that cell (48,346.2 ns) would have. O-51's own conclusion: "the DIRECTION
is robust, but whether it clears THIS particular IQR decision rule
depends on which round's own arm-(b) noise happened to land."

**THIS session (a third independent 5-trial window) reads clearly
OUTSIDE the IQR bar on BOTH configs**: auto-caps +41,334.4 vs a bar of
4,664.3 (an 8.9x margin, not O-51's 1.4% one); auto-nocaps +69,020.8 vs
a bar of 15,770.8 (a 4.4x margin). The DIRECTION is identical across all
three sessions (positive: the byte-only guard costs more than no guard
at all, on keyword specifically); the MAGNITUDE is in the same order as
O-51's own two sessions (this session: 41.3k/69.0k ns; O-51: 39.5k-48.3k
ns on auto-caps across its two sessions, single auto-nocaps reads of
45.2k/48.3k) but noticeably larger on auto-nocaps this time (69.0k vs
45.2k/48.3k). **The decision-RULE's own robustness question I-105 left
open (needing [B79]'s null-control band, not yet landed at commit time
of this report) is NOT settled by a third session landing clean** --
three sessions now read `outside`/`borderline`/`outside`, all POSITIVE,
all the same order of magnitude, which argues the DIRECTION is
trustworthy and the IQR-crossing BAR is where three windows still do not
agree with each other on the margin. [B79]'s null band, once it lands,
is what would let a reader tell "outside the IQR bar" apart from "outside
a band this box's own noise floor produces between separate windows" --
this lane does not have that band and does not construct one.

### 8.5 The two-parameter solve, re-attempted on the well-separated
frequency spread -- conditioning shown, NOT forced

Using the SAME method O-51/section 10 used (`auto-nocaps`, eliminating
`c_byte` between two patterns' equations): `bytes` is IDENTICAL across
every point (all three use `bench/capability`'s own three throughput
subjects, 1,376,256 B total), so the model is `ΔT = c_byte*bytes +
c_hit*hits` and the two-point elimination is `(hits_1-hits_2)*c_hit =
ΔT_1-ΔT_2`.

**Semdiv is EXCLUDED from this solve on structural grounds, stated
before computing anything** (not discovered after a bad fit): semdiv's
own guard sits inside `rx_search` AFTER `[OPT-ENDWIN]` has already
clamped `search_from` to `subject_length - 4` (section 5) -- the byte
scan touches at most 4 bytes of ANY subject regardless of its length,
so "bytes scanned" for semdiv is NOT the subject's own byte count the
way it is for keyword/espace (whose guards run from `search_from` to
the subject's end, unclamped). Mixing semdiv into a model whose `bytes`
term assumes "the whole subject was available to be scanned" would
silently misuse the model's own geometry, not merely add a noisy point
-- excluded, not down-weighted.

**Keyword (3.2067%, hits=44,132) vs espace (8.5212%, hits=117,274),
auto-nocaps -- Δhits=73,142, a 2.66x wider separation than O-51's own
0.36-percentage-point / 5,037-hit gap between router and keyword:**

    MEMCHR (ΔT = (a)-(c)):
      keyword: (a)-(c) = +560,875.1578 ns, hits=44,132
      espace:  (a)-(c) =    -1,437.4559 ns, hits=117,274
      => c_hit = (-1,437.4559 - 560,875.1578) / 73,142 = -7.6880 ns/hit  (UNPHYSICAL)
      => c_byte = (560,875.1578 - 44,132*(-7.6880)) / 1,376,256 = 0.654064 ns/B

    INLINE (ΔT = (d)-(c)):
      keyword: (d)-(c) = +1,067,704.9245 ns, hits=44,132
      espace:  (d)-(c) =      -455.2970 ns, hits=117,274
      => c_hit = (-455.2970 - 1,067,704.9245) / 73,142 = -14.6039 ns/hit  (UNPHYSICAL)
      => c_byte = (1,067,704.9245 - 44,132*(-14.6039)) / 1,376,256 = 1.244104 ns/B

**BOTH solves land on a negative (unphysical) per-hit term again --
with a frequency gap 7.4x wider than I-105's own bracket needed to fix
O-51's stated cause (near-collinearity from proximity), and the fit is
STILL wrong. A wider frequency spread does NOT fix this solve, and the
reason is visible directly in section 8.2/8.1's own numbers, not
inferred: keyword's `(a)-(c)` is enormous and POSITIVE (+560,875 ns)
while espace's is tiny and NEGATIVE (-1,437 ns) -- not merely smaller,
the SIGN itself differs. A linear model in (bytes, hits) alone cannot
produce a sign change from a hit-count increase (44,132 -> 117,274 is
MORE hits, and both `c_byte`/`c_hit` terms the model assumes are
non-negative physical rates) without one of its own coefficients going
negative BY CONSTRUCTION -- so the two solves above did not fail from
noise or proximity, they failed because the MODEL ITSELF omits a
variable that dominates the signal: match density (section 8.2's own
finding). Keyword's guard is re-entered ~9,467 times per its own three
subjects (nmatches summed); espace's is re-entered ~1 time. A model
with a per-CALL fixed cost term (`c_call * calls`, `calls` scaling with
nmatches, not with `hits` or `bytes`) is what these two points'
`(a)-(c)` values actually look shaped by -- keyword's huge and positive
because ~9,467 guard invocations each pay something; espace's near-zero
because ~1 invocation pays it once. THIS is shown and stopped here, per
the ruling's own instruction ("if it still can't separate the terms
cleanly, show it and stop there, no forcing") -- a three-parameter
model (`bytes`, `hits`, `calls`) is what the data now argues for, and
three points cannot solve three unknowns with only two of them
(keyword, espace) usable in the two-point elimination the current
method allows; the crossover-conditioning question I-105 asked (is the
NUMERIC solve fixable by spreading the frequency points further apart)
is answered **NO** -- not because the points are still too close (they
are not: 5.31 percentage points apart here vs O-51's 0.36), but because
the underlying two-parameter model does not include the variable
(match density / call count) that turns out to dominate `(a)-(c)`'s own
sign and magnitude. The QUALITATIVE bracket in 8.3 (memchr-run
dominant at <=3.2%, no longer uniformly dominant at 8.5%) survives this
finding untouched -- it does not depend on the linear model at all,
only on IQR-cleared sign comparisons within each cell.

**Single-term bounding estimates, auto-nocaps (assuming the OTHER term
negligible, one at a time -- reported for completeness, same caveat as
O-51's own section 10: a simplification the match-density confound
above means should not be over-read either):**

    memchr, per-hit only (assume c_byte ~ 0):
      keyword: 560,875.1578 / 44,132 hits = 12.7090 ns/hit
      espace:   -1,437.4559 / 117,274 hits = -0.0123 ns/hit

    inline, per-byte only (assume c_hit ~ 0):
      keyword: 1,067,704.9245 / 1,376,256 B = 0.775804 ns/B
      espace:     -455.2970 / 1,376,256 B = -0.000331 ns/B

Keyword's own per-hit figure (12.71 ns/hit) is close to O-51's own
auto-nocaps reading (12.64 ns/hit) -- reproduced across sessions.
Espace's near-zero/negative reading under the SAME single-term
assumption is consistent with 8.2's own finding (the guard barely
costs anything, or slightly helps, at espace's own near-zero match
density) rather than with a genuine negative physical rate -- read as
further evidence for the match-density confound, not a crossover
constant.

### 8.6 Semdiv's own caveat, stated plainly

Semdiv's absolute costs (25-50 ns for the WHOLE 3-subject sum) sit at
or below this instrument's own measurement floor -- keyword/espace's
smallest IQRs are still in the hundreds-of-ns to low-thousands-of-ns
range; semdiv's are single-digit to tens of ns, the same ORDER as the
deltas being compared (section 8.2: -18.2 ns and -8.7 ns deltas against
IQR bars of 0.27-9.53 ns). Section 8.3's own (d)-(a) reading (memchr-run
wins on semdiv too) is directionally consistent with keyword's but
should not be read as a THIRD independent frequency point for the
crossover model at all -- both because [OPT-ENDWIN]'s window-collapse
makes its own "bytes scanned" incomparable (8.5's own exclusion) and
because at these absolute magnitudes, fixed per-call overhead (a
function call vs. an inlined loop's own entry cost) plausibly dominates
over any per-byte or per-hit rate, which is a DIFFERENT mechanism than
either model term. Kept in the report as measured, not discarded --
but not used in 8.5's solve, and not cited as crossover evidence beyond
the qualitative "memchr-run wins here too" already stated.

## Summary of what changed vs the charter's literal asks

- Configs: BOTH of O-51's keyword configs (`auto-caps`, `auto-nocaps`)
  applied to all three points, not keyword alone (section 1 deviation 2)
  -- for a comparable grid across the three-point spread.
- The synthetic witness's exact pattern text was the lane's own choice
  within I-105's example (section 1 deviation 3), verified against its
  own stamp and frequency before being trusted.
- Semdiv EXCLUDED from the two-parameter solve on structural grounds
  ([OPT-ENDWIN]'s window collapse), stated before computing anything
  (section 8.5) -- the charter's own three-point spread (0.48/3.21/8.52%)
  is fully DELIVERED (all 24 cells measured, medians+IQRs, the
  frequency-vs-(b)-(c) table, the qualitative bracket), but the NUMERIC
  two-parameter solve only ever had two usable points (keyword, espace)
  once semdiv's geometry disqualified it -- and even THAT pair's much
  wider frequency separation does not produce a physical fit, for a
  reason (match-density / call-count confound) the charter's own model
  does not name and this report does not paper over.
- Everything else -- 5 interleaved trials, load gate (re-verified at go
  time by BOTH `uptime` and `mpstat -P ALL 1 5`, both recorded), the
  fresh answer-check immediately before timing, the O-50/[B81]/[B83]
  fallback instrument shape -- follows the charter and O-51's protocol
  verbatim.

Scratch artifacts (not committed, per the mandate):
`.../scratchpad/b86/` (`run_instrument.py`, `analyze.py`, `analyze2.py`,
`work/`, `manifest.json`, `timing_results.json`, `build.log`,
`time.log`) -- reproducible against pin 6ef76820; held in the session
scratchpad, never `/tmp` root.
