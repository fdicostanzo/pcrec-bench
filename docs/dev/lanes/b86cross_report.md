# [B86] lane report -- the three-point crossover block (I-105's cycle-3 ask)

Executor lane, I-57 terms. Report, never diagnose. Every command run, every
raw number, stated as MEASURED. This is the PREP delivery: arms built,
stamps checked, answer-check passing, calibration done -- the timed rounds
themselves are GATED on the manager's explicit go (the brief's own GATE),
sent as a `SendMessage` to `main` after this commit.

## 0. Charter-vs-committed checklist

| charter item | status |
|---|---|
| (i) wild-semdiv-dollar-trailing-newline-pcre2, four arms | ARMS BUILT, stamped, answer-checked, calibrated. TIMING OWED (gated) |
| (ii) keyword-prefix-order, four arms, rebuilt from O-51's recipe | ARMS BUILT, stamped, answer-checked, calibrated. TIMING OWED (gated) |
| (iii) synthetic e/space-run witness, SCRATCH PROBE, stamp-verified RX_REQ_BYTE 101, never enters bench/capability | BUILT + VERIFIED (RX_REQ_BYTE "101" confirmed by compile), answer-checked by arm-equality, NOT added to any bench/ set (no gen_*.py touched, no manifest changed, `git status` on `bench/` is clean below) |
| pin | 6ef76820 (I-105's ack does not name one; the brief's fallback rule applies) |
| stamps recorded for every arm, decline visibility | DONE -- section 3 below: all 24 cells read `RX_REQ_WHY "emitted"` on arms a/b/d and `"none"` on arm c (c's own contract: "none" iff REQ_BYTE is "none"); **no cell declines** -- itself the finding the brief asked to surface, not hide |
| per-point per-arm medians+IQRs | OWED (gated on timed rounds) |
| frequency-vs-(b)-(c) table | OWED (gated) |
| two-parameter solve re-attempted on 0.48/3.21/8.52% | OWED (gated) |
| keyword's IQR-flip finding restated | OWED (gated; will read O-51's finding beside this run's own) |
| GATE: SendMessage before first timed round | DONE (sent after this commit) |

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

## 8. Timed rounds, verdict grid, crossover solve -- OWED, gated

**NOT YET RUN.** Per the brief's own GATE: preparation (arms, stamps,
answer-check) is complete; the 5 interleaved-trial timed rounds are held
for the manager's explicit go, sent by `SendMessage` to `main`
immediately after this commit. This section, the frequency-vs-(b)-(c)
table, the two-parameter crossover solve on the 0.48/3.21/8.52% spread,
and keyword's IQR-flip finding restated beside this run's own, are ALL
OWED and will be appended (a follow-up commit on this same branch, this
same report file) once the go arrives and the timed rounds complete.

## Summary of what is committed here vs owed

- Committed: sections 0-7 above (deviations, box/pin/subjects, the three
  points' facts and stamps -- the no-decline finding -- building,
  guard regions, answer-check, calibration). `run_instrument.py`
  (scratch, session scratchpad, not committed) reproduces all of it
  against the same pin.
- Owed: section 8 (timed rounds, medians+IQRs, the frequency table, the
  crossover solve, keyword's IQR-flip restated) -- gated on the
  manager's go, per the brief.
