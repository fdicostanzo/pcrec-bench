# [B83] lane report -- I-103/I-103a's run-form discriminator, one timed block

Executor lane, I-57 terms. Report, never diagnose. Every command run, every
raw number, stated as MEASURED.

## 0. Deviations from I-103/I-103a's literal text (all listed up front)

1. **Instrument form delivered: the O-50/[B81] fallback shape, exactly as
   `docs/dev/lanes/b81blockd_report.md` documents it.** The REAL
   `testees.pcrec.adapter.Adapter` instance (via `pcrecbench.adapters.
   discover()["pcrec"]`), used ONLY for its `.measure()` method (which calls
   `pcrecbench.driverrun.per_trial`, the real driver-invocation loop)
   against hand-built `handle` dicts pointing at each variant's `.so`; the
   real `pcrecbench.subbench.find("capability")` / `.subjects_for(
   "throughput")` / `.expectation(...)` / `.subject(...)`; the real
   `pcrecbench.harness.calibrate` / `outcome_for` / `classify_giveup` /
   `truncation_for`; the real `pcrecbench.record.match_row`; and the real
   `pcrecbench.reduce.reduce_set_cell` / `judge_trial_agreement` /
   `agreement_line`. No line of `pcrecbench/` or `testees/` was edited. No
   record was written to any store. Runner script:
   `/tmp/optloop5/b83/run_instrument.py` (scratch, not committed).
2. **The throughput subject trees were regenerated in this worktree.**
   `bench/capability/throughput/*.bin` are GENERATED and gitignored
   (harness_contract's own rule); a fresh `git worktree add` does not carry
   them. Ran `python3 bench/capability/gen_throughput_subjects.py` once;
   sha256 confirmed byte-identical to the main tree's already-generated
   copies (`d2e4f134…/t-64k`, `3cf7b248…/t-256k`, `ccbdf7eb…/t-1m` --
   matching `docs/dev/lanes/b81blockd_report.md`'s own recorded hashes).
3. **CONFIG RECONCILIATION (I-103 vs I-103a), per the brief's own
   instruction to follow I-103a's wider list.** I-103's literal text names
   ONE config per pattern, `(auto, --no-captures)` -- `pcrec-nocaps`'s flag
   shape (`--features all --no-captures`). I-103a widens this to "the two
   DFA-route auto configs where the +80.8%/+59.7% live, plus the
   forced-VM pair for router" -- read here as `auto-caps` (`pcrec-auto`'s
   shape, `--features all`, captures ON) and `auto-nocaps` (I-103's own
   config) for BOTH patterns, plus `vm-caps` (`pcrec-vm`'s shape,
   `--features all --engine=vm`) and `vm-in-caps` (`pcrec-vm-in`'s shape,
   same flags + `buffer_frames=32768`/`buffer_trail=131072`) for ROUTER
   ONLY -- exactly the four-testee naming I-102 uses elsewhere in the same
   inbox batch (`auto-caps, auto-nocaps, vm-caps, vm-in-caps`). This is the
   full grid measured below: router x 4 configs, keyword x 2 configs.
4. **STOP on arm (d) for BOTH keyword configs -- judgment-shaped, not
   mechanical, reported rather than decided.** I-103a's literal inline-loop
   template is `subject[rp_c] == <byte> && !memcmp(subject + rp_c, "<run>",
   <runlen>)`, which assumes the scanned byte sits at OFFSET 0 of the run.
   Router's own default artifact confirms offset 0 ("the scan is on byte 47
   at offset 0 of the run"; run "/user", byte 47 = '/', the run's own first
   character) -- the template applies literally, no interpretation needed.
   Keyword's default artifact states plainly: **"the scan is on byte 110 at
   offset 1 of the run"** (run "in", byte 110 = 'n' = the run's SECOND
   character; verbatim region below). Applying I-103a's template literally
   to keyword (`subject[rp_c] == 110`) checks whether the byte at the
   RUN-START candidate position is 'n' -- but the run starts with 'i' at
   every true occurrence, so a literal application would build a guard that
   never fires on a real match, silently changing the guard from
   "not-found early-out" to "always not found" -- a correctness bug wearing
   a timing instrument's clothes, not a faithful hand-twin. Adapting the
   template to the byte's own offset (`subject[rp_c + 1] == 110`) is a
   mechanical-looking one-token edit, but it is a JUDGMENT CALL beyond what
   I-103a's literal text authorizes (the addendum's template text does not
   itself carry an offset parameter), so per the lane brief's own
   contingency ("if the emitted region does not match what the entry
   describes closely enough to edit unambiguously, STOP on (d) and report
   the region verbatim") this is STOPPED for `keyword-prefix-order` on BOTH
   its configs and reported, verbatim, in section 3 below. Router's arm (d)
   is built and measured on all four of its configs (the template applies
   there with zero interpretation).

## 1. Box facts, pin, subjects

`gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0`. pcrec pin `b1885a83`
(`/home/duxevents/pcrec-bench/build/pcrec-b1885a83`, `PIN.tsv`: commit
`b1885a83dea907d9f942bb0fc19760af3d463b2c`) -- ALREADY BUILT, reused
unmodified, no new pcrec build (I-103's own note). Worktree
`worktrees/b83runform` (branch `lane/b83runform`). Scratch:
`/tmp/optloop5/b83/` (`run_instrument.py`, `work/`, `*.json`,
`run_instrument.log`). `uptime` immediately before the run: `load average:
0.11, 0.43, 0.74` (quiet: load1 < 0.5, per the brief's own bar). Subjects:
`bench/capability/throughput/{t-64k,t-256k,t-1m}.bin` (65,536 / 262,144 /
1,048,576 B), the capability set's own three committed throughput
subjects. Regime: `throughput` (`--find-all`, the driver protocol's
non-overlapping-match count operation).

## 2. Building the variants

Phase-1 argv, mirroring `testees/pcrec/adapter.py::_compile_one` exactly
(`-fcomments` as the fixed protocol token, never in `cfg["flags"]`; the
pattern element as raw bytes, the I-72 convention):

    build/pcrec-b1885a83/build/pcrec -p rx -fcomments <cfg flags> \
        [-fno-req-run | -fno-req-byte] -o artifact.c --pattern <PATTERN>

Phase-2 argv, mirroring the adapter's phase 2 exactly (no `cflags`
axis on any of these configs):

    gcc -O2 -std=gnu11 -fPIC -shared -o artifact.so \
        testees/pcrec/shim.c -DPB_ARTIFACT="<dir>/artifact.c" -I <dir>

Configs (pcrec flags, from `testees/pcrec/configs.toml`):

| config | flags |
|---|---|
| `auto-caps` | `--features all` |
| `auto-nocaps` | `--features all --no-captures` |
| `vm-caps` | `--features all --engine=vm` |
| `vm-in-caps` | `--features all --engine=vm` + driver `--buffer-frames 32768 --buffer-trail 131072` |

Arms: (a) default: config flags only. (b) `+ -fno-req-run`. (c)
`+ -fno-req-byte`. (d) the inline-run hand-twin -- see section 3.

**sha256 of every built `artifact.c`** (arm a/b/c on all six
pattern-config pairs, arm d on router's four):

    d43feb8f87ad53d6...  router-prefix-order/auto-caps/a
    51dbd5fd378aa170...  router-prefix-order/auto-nocaps/a
    5bca8f4114037205...  router-prefix-order/vm-caps/a
    5bca8f4114037205...  router-prefix-order/vm-in-caps/a        <- IDENTICAL to vm-caps/a
    40edf48a559e7ff7...  router-prefix-order/auto-caps/b
    5eda371652181ebc...  router-prefix-order/auto-nocaps/b
    af9d62b4d39cadea...  router-prefix-order/vm-caps/b
    af9d62b4d39cadea...  router-prefix-order/vm-in-caps/b         <- IDENTICAL to vm-caps/b
    bfd7e29eaaaf146f...  router-prefix-order/auto-caps/c
    9b7e7143902962e3...  router-prefix-order/auto-nocaps/c
    892fea2568e2fda5...  router-prefix-order/vm-caps/c
    892fea2568e2fda5...  router-prefix-order/vm-in-caps/c         <- IDENTICAL to vm-caps/c
    0857eb11514f7231...  router-prefix-order/auto-caps/d
    9aa54ce420718e48...  router-prefix-order/auto-nocaps/d
    e73504317b9f1af4...  router-prefix-order/vm-caps/d
    e73504317b9f1af4...  router-prefix-order/vm-in-caps/d         <- IDENTICAL to vm-caps/d
    aedbb97641aa9c55...  keyword-prefix-order/auto-caps/a
    078d176193b3a51a...  keyword-prefix-order/auto-nocaps/a
    fe6ab38969bd35d4...  keyword-prefix-order/auto-caps/b
    6092e9397a8ec170...  keyword-prefix-order/auto-nocaps/b
    41207c93dd3d1d07...  keyword-prefix-order/auto-caps/c
    15ac5afab757e4c8...  keyword-prefix-order/auto-nocaps/c

The `vm-caps`/`vm-in-caps` sha256 identity per arm is a CONTROL, not
decoration: it confirms the `--buffer-*` driver flags never touch the
emitted artifact, only the runtime call (`rx_search_in` forwards to
`rx_search` on a DFA artifact and, per `rx_search_run`'s own body on the
VM route, the buffer descriptor only rebinds `rx_run_state`'s storage --
the guard block sits in `rx_search_run`, shared by both entries, exactly
as `testees/pcrec/CLAUDE.md`'s cf0962e3-era note ("the guard lives in the
shared search prologue") predicts).

## 3. The guard region, and the STOP on keyword's arm (d)

**Router's default guard** (`rx_search`, DFA route; `rx_search_run`,
VM route -- identical text either way), byte 47 offset 0:

    /* [OPT-REQPOS] every match of this pattern contains the 5 bytes
     * "/user", so a window without them holds no match at all;
     * the scan is on byte 47 at offset 0 of the run. */
    if (subject_length <= search_from) return 0;
    {
        size_t rp_pos = search_from;
        for (;;) {
            const void *rp_q = memchr(subject + rp_pos, 47, subject_length - rp_pos);
            size_t rp_c;
            if (!rp_q) return 0;
            rp_c = (size_t)((const unsigned char *)rp_q - subject);
            if (rp_c + 5 <= subject_length
                && !memcmp(subject + rp_c, "/user", 5)) break;
            rp_pos = rp_c + 1;
            if (rp_pos >= subject_length) return 0;
        }
    }

**Router's arm (d)** (the ONLY edit; the two-line comment above it is left
in place, byte-identical text, describing a guard that is no longer
literally a memchr call -- the comment is inert prose, not re-derived):

    if (subject_length <= search_from) return 0;
    {
        size_t rp_pos = search_from;
        size_t rp_c;
        for (rp_c = rp_pos; rp_c + 5 <= subject_length; rp_c++)
            if (subject[rp_c + 0] == 47 && !memcmp(subject + rp_c, "\x2f\x75\x73\x65\x72", 5))
                break;
        if (rp_c + 5 > subject_length) return 0;
    }

Same found/not-found wiring as the original: the block falls through
(into the forward-table scan) exactly when a run occurrence exists at or
after `search_from`, and `return 0`s exactly when none does. I-103a's
own template applied with zero interpretation (byte offset 0 = the run's
own first character).

**Keyword's default guard**, VERBATIM, byte 110 offset 1 -- the region
this lane STOPS on:

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

I-103a's literal template (`subject[rp_c] == <byte> && !memcmp(subject +
rp_c, "<run>", <runlen>)`) reads the byte at the SAME position the memcmp
starts from -- correct only when the scanned byte IS the run's first
byte. Here it is not (`rp_c - 1` is where the run's memcmp starts; the
byte is checked one position later, at `rp_c`). Substituting the template
literally builds `if (subject[rp_c] == 110 && !memcmp(subject + rp_c,
"in", 2))`, which checks whether the SECOND character of a candidate
2-byte window is 'n' while comparing the window starting AT that same
position against "in" -- neither the position an "in" occurrence's start
would satisfy nor a faithful re-expression of the original's semantics.
STOPPED per the brief's own contingency; `keyword-prefix-order` measures
arms (a), (b), (c) only, on both its configs.

## 4. Answer-check, before any timing

One `iters=1 --find-all` call per variant, all three subjects, via the
real `adapter.measure()` (`work/answer_check.json` carries the full
per-variant per-subject `nmatches`):

| pattern | subject | expected nmatches (expectations.tsv) | measured (every arm, every config) |
|---|---|---:|---:|
| router-prefix-order | t-64k | 9 | 9 |
| router-prefix-order | t-256k | 58 | 58 |
| router-prefix-order | t-1m | 245 | 245 |
| keyword-prefix-order | t-64k | 433 | 433 |
| keyword-prefix-order | t-256k | 1791 | 1791 |
| keyword-prefix-order | t-1m | 7243 | 7243 |

**EQUAL across all four (router) / three (keyword) arms, on every config,
on every subject** -- the counts above are the SAME set of numbers for
(a), (b), (c) and, where built, (d); no variant answered `nomatch` or a
different count anywhere. Confirmed BEFORE any timed round (per-variant
answer dump in `work/answer_check.json`; the equality table itself in
`run_instrument.log`, section "matches= equality across arms").

## 5. Calibration (`harness.calibrate`, real function, one probe per variant)

    router-prefix-order  auto-caps    a  iters=295  (169.601 us/iter, t-256k)
    router-prefix-order  auto-caps    b  iters=544  (92.060 us/iter, t-256k)
    router-prefix-order  auto-caps    c  iters=544  (91.981 us/iter, t-256k)
    router-prefix-order  auto-caps    d  iters=188  (266.682 us/iter, t-256k)
    router-prefix-order  auto-nocaps  a  iters=280  (179.051 us/iter, t-256k)
    router-prefix-order  auto-nocaps  b  iters=543  (92.121 us/iter, t-256k)
    router-prefix-order  auto-nocaps  c  iters=546  (91.670 us/iter, t-256k)
    router-prefix-order  auto-nocaps  d  iters=195  (256.771 us/iter, t-256k)
    router-prefix-order  vm-caps      a  iters=49   (1030.796 us/iter, t-256k)
    router-prefix-order  vm-caps      b  iters=54   (940.366 us/iter, t-256k)
    router-prefix-order  vm-caps      c  iters=54   (933.795 us/iter, t-256k)
    router-prefix-order  vm-caps      d  iters=45   (1111.737 us/iter, t-256k)
    router-prefix-order  vm-in-caps   a  iters=49   (1027.866 us/iter, t-256k)
    router-prefix-order  vm-in-caps   b  iters=54   (937.886 us/iter, t-256k)
    router-prefix-order  vm-in-caps   c  iters=54   (942.236 us/iter, t-256k)
    router-prefix-order  vm-in-caps   d  iters=45   (1114.426 us/iter, t-256k)
    keyword-prefix-order auto-caps    a  iters=161  (310.732 us/iter, t-256k)
    keyword-prefix-order auto-caps    b  iters=267  (187.551 us/iter, t-256k)
    keyword-prefix-order auto-caps    c  iters=284  (176.521 us/iter, t-256k)
    keyword-prefix-order auto-nocaps  a  iters=165  (304.661 us/iter, t-256k)
    keyword-prefix-order auto-nocaps  b  iters=268  (186.662 us/iter, t-256k)
    keyword-prefix-order auto-nocaps  c  iters=285  (175.631 us/iter, t-256k)

`n_iters` is calibrated PER VARIANT (own probe, own `SetCell`), the same
shape `docs/dev/lanes/b81blockd_report.md` used -- `reduce.reduce_set_cell`'s
numbers are ns/call, already iteration-normalized, so the grid below
compares apples to apples regardless.

## 6. Timed rounds -- interleaved a,b,c[,d] x 5, `uptime` before each round

    round 1 uptime: load average 0.24, 0.15, 0.45
    round 2 uptime: load average 0.38, 0.18, 0.46
    round 3 uptime: load average 0.43, 0.20, 0.46
    round 4 uptime: load average 0.48, 0.21, 0.46
    round 5 uptime: load average 0.52, 0.22, 0.46

load1 rose from 0.24 to 0.52 over the run's own five rounds (this
process's own gcc/driver children) -- consistent with the box's
pre-run 0.11 baseline and the brief's own "load1 < 0.5" bar at launch;
the whole run (build + answer-check + calibration + 5 rounds x 22
variants) completed in under 25 seconds wall time.

**Per-variant `SetCell` (median / min / max / IQR over 5 trials, ns,
sum over the 3 throughput subjects per trial):**

| pattern | config | arm | median ns | min ns | max ns | IQR (Q3-Q1) |
|---|---|---|---:|---:|---:|---:|
| router-prefix-order | auto-caps | a | 754,122.4 | 723,274.9 | 807,410.2 | 47,860.0 |
| router-prefix-order | auto-caps | b | 410,943.0 | 403,535.7 | 425,506.0 | 12,637.6 |
| router-prefix-order | auto-caps | c | 396,885.1 | 393,755.6 | 411,530.4 | 16,135.8 |
| router-prefix-order | auto-caps | d | 1,148,801.6 | 1,100,880.9 | 1,155,500.4 | 50,677.1 |
| router-prefix-order | auto-nocaps | a | 746,341.9 | 720,393.7 | 754,578.5 | 32,473.4 |
| router-prefix-order | auto-nocaps | b | 411,046.1 | 402,976.9 | 416,555.6 | 7,276.9 |
| router-prefix-order | auto-nocaps | c | 411,087.3 | 393,630.9 | 412,381.7 | 18,519.4 |
| router-prefix-order | auto-nocaps | d | 1,146,928.4 | 1,101,938.6 | 1,160,918.6 | 31,251.3 |
| router-prefix-order | vm-caps | a | 4,644,138.2 | 4,441,783.0 | 4,654,639.7 | 143,740.6 |
| router-prefix-order | vm-caps | b | 4,236,402.6 | 4,059,764.7 | 4,298,936.3 | 143,090.5 |
| router-prefix-order | vm-caps | c | 4,203,401.6 | 4,059,362.7 | 4,233,785.1 | 123,904.4 |
| router-prefix-order | vm-caps | d | 5,024,701.2 | 4,827,343.4 | 5,034,640.8 | 202,466.7 |
| router-prefix-order | vm-in-caps | a | 4,596,408.2 | 4,449,317.7 | 4,600,629.4 | 76,142.3 |
| router-prefix-order | vm-in-caps | b | 4,139,167.9 | 4,060,108.6 | 4,196,586.2 | 130,810.2 |
| router-prefix-order | vm-in-caps | c | 4,192,858.6 | 4,063,275.5 | 4,200,966.5 | 125,631.2 |
| router-prefix-order | vm-in-caps | d | 4,983,249.4 | 4,822,152.3 | 4,992,817.7 | 89,253.3 |
| keyword-prefix-order | auto-caps | a | 1,262,073.6 | 1,236,234.1 | 1,298,224.7 | 60,024.4 |
| keyword-prefix-order | auto-caps | b | 809,646.6 | 776,182.8 | 812,724.7 | 18,550.2 |
| keyword-prefix-order | auto-caps | c | 761,466.6 | 733,586.1 | 764,443.1 | 28,825.7 |
| keyword-prefix-order | auto-nocaps | a | 1,291,424.4 | 1,258,581.5 | 1,297,547.9 | 19,741.6 |
| keyword-prefix-order | auto-nocaps | b | 811,216.9 | 809,435.3 | 811,981.0 | 1,583.1 |
| keyword-prefix-order | auto-nocaps | c | 762,870.7 | 732,616.0 | 763,582.7 | 15,839.6 |

All 22 cells: `failing_subjects=[]`, `n_wrong=0`, `n_gave_up=0`, trial
agreement **`agree`** (`reduce.judge_trial_agreement`, rule `v1.4-group`,
k=1.5, d_min=2, share_c=3, 5 trials -- a record built from any of these
would stamp `measured`, none `inconclusive-spread`; raw per-round sums
and full agreement lines in `results.json`).

## 7. The EXPECT call counts (I-103/I-103a, quoted) beside the measured deltas

| pattern | config | (a)-(c) ns | (b)-(c) ns | (d)-(a) ns | (d)-(c) ns |
|---|---|---:|---:|---:|---:|
| router | auto-caps | +357,237.3 | +14,057.9 | +394,679.2 | +751,916.5 |
| router | auto-nocaps | +335,254.6 | **-41.2** | +400,586.5 | +735,841.1 |
| router | vm-caps | +440,736.6 | +33,001.0 | +380,563.0 | +821,299.6 |
| router | vm-in-caps | +403,549.6 | **-53,690.7** | +386,841.2 | +790,390.8 |
| keyword | auto-caps | +500,607.0 | +48,180.0 | (STOPPED) | (STOPPED) |
| keyword | auto-nocaps | +528,553.7 | +48,346.2 | (STOPPED) | (STOPPED) |

I-103's own EXPECT, quoted: "router: (a) 39,098 memchr calls, (b) 315, (c)
0 -- so (a) - (c) ~ +322,000 ns and (b) - (c) ~ 0"; "keyword: (a) 44,135,
(b) 9,470, (c) 9,467 in the prefilter alone". I-103a's own hit-rate facts,
quoted: "router '/' 39,095 hits in 1,375,008 B = 2.8%; keyword 'n' 44,132
in 1,376,256 B = 3.2%".

## 8. The (b)-vs-(c) decision line (I-103's own bar: |Δ| vs max(IQR_b, IQR_c))

| pattern / config | \|(b)-(c)\| ns | max(IQR_b, IQR_c) | verdict |
|---|---:|---:|---|
| router / auto-caps | 14,057.9 | 16,135.8 | **within IQR** |
| router / auto-nocaps | 41.2 | 18,519.4 | **within IQR** |
| router / vm-caps | 33,001.0 | 143,090.5 | **within IQR** |
| router / vm-in-caps | 53,690.7 | 130,810.2 | **within IQR** |
| keyword / auto-caps | 48,180.0 | 28,825.7 | **outside IQR -- (b) materially worse** |
| keyword / auto-nocaps | 48,346.2 | 15,839.6 | **outside IQR -- (b) materially worse** |

**ROUTER reads exactly as I-103 predicted, on all four configs**: the
byte-only guard (b) is statistically indistinguishable from no guard at
all (c) -- the run form (memcmp-on-top-of-memchr) is the WHOLE cost of
router's pre-check. **KEYWORD does NOT**: (b) reads a measurable ~48,200 ns
slower than (c) on BOTH configs, well outside even the wider of the two
IQRs, despite I-103's own call-count estimate putting (b) and (c) at
nearly the SAME count (9,470 vs 9,467) -- a finding, stated as measured,
not diagnosed: keyword's match density is far higher than router's
(nmatches 433/1,791/7,243 vs 9/58/245 on the same three subjects), so
`rx_search` (and therefore the byte-only guard's single `memchr` call) is
invoked roughly 30x more often on keyword than on router for the SAME
three subjects -- a per-CALL cost multiplied by a much larger call count,
which the quoted "calls in the prefilter alone" figures do not appear to
capture on their own terms. Per I-103's own reading rule: "if (b) is
materially worse than (c), the one-byte form costs something too and
G1's existing dominance rule is under-measured rather than the run form
over-admitted" -- that is keyword's reading.

## 9. Inline-vs-memchr (router only, arm (d) built)

| config | (d) vs (a) | max(IQR_a, IQR_d) | verdict |
|---|---:|---:|---|
| auto-caps | +394,679.2 (+52.3%) | 50,677.1 | **outside IQR -- memchr-run clearly beats inline** |
| auto-nocaps | +400,586.5 (+53.7%) | 32,473.4 | **outside IQR -- memchr-run clearly beats inline** |
| vm-caps | +380,563.0 (+8.2%) | 202,466.7 | **outside IQR -- memchr-run clearly beats inline** |
| vm-in-caps | +386,841.2 (+8.4%) | 89,253.3 | **outside IQR -- memchr-run clearly beats inline** |

**Confirms I-103a's own EXPECT** ("at 2.8-3.2% memchr-run should still
beat the inline scalar loop") on every one of the four configs measured;
the inline hand-twin is NOT a refuted expectation here -- router's own
2.8% byte frequency sits below whatever crossover exists (section 10).
Keyword's arm (d) is STOPPED (section 3); this project cannot report an
inline-vs-memchr verdict for keyword's 3.2% point from this window.

## 10. Derived constants and the crossover arithmetic (shown in full)

**The naive two-equation solve is ill-conditioned and is reported as
such, not silently discarded.** Setting up I-103a's own linear model
(`ΔT = c_byte x BYTES + c_hit x HITS`) at the `auto-nocaps` cell (I-103's
own originally-asked config) for both patterns:

    router:  1,375,008 * c_byte +  39,095 * c_hit =   335,254.6
    keyword: 1,376,256 * c_byte +  44,132 * c_hit =   528,553.7

BYTES differs by only 0.09% between the two rows (1,375,008 vs
1,376,256) while HITS differs by 12.9% (39,095 vs 44,132) -- the system
is NEARLY COLLINEAR in `c_byte`'s column, so solving it exactly (scale
the first equation by 1,376,256/1,375,008 = 1.0009076 and subtract)
gives:

    5,001.5 * c_hit = 192,994.7   =>   c_hit = 38.58 ns/hit
    c_byte = (335,254.6 - 39,095 * 38.58) / 1,375,008 = -0.853 ns/B

A NEGATIVE per-byte cost is not physical -- the two-point solve is too
sensitive to the rows' near-identical BYTES totals to trust its split.
**Reported instead, as single-term bounding estimates** (assuming the
OTHER term negligible, one at a time -- the same simplification I-103a's
own model implies is reasonable, since 0.017 ns/B x 1,375,008 B ~ 23,375
ns is a minority of 7.7 ns/hit x 39,095 ~ 301,032 ns under I-103a's own
assumed constants):

    memchr, per-hit only (assume c_byte ~ 0):
      router:  335,254.6 /  39,095 hits = 8.58 ns/hit
      keyword: 528,553.7 /  44,132 hits = 11.98 ns/hit
    (I-103a's own assumed memchr constant: 7.7 ns/hit -- router's own
    estimate, 8.58 ns/hit, is within 11.4% of it; keyword's, 11.98
    ns/hit, is higher, consistent with 8's finding that keyword's guard
    costs more than a pure per-hit model predicts)

    inline, per-byte only (router auto-nocaps, assume c_hit ~ 0):
      (d)-(c) = 1,146,928.4 - 411,087.3 = 735,841.1 ns
      735,841.1 / 1,375,008 B = 0.535 ns/B
    (I-103a's own assumed inline constant: 0.5 ns/B -- 7.0% above it)

    inline, per-hit residual (using I-103a's OWN 0.5 ns/B for the byte
    term, solving the remainder against router's own hit count):
      735,841.1 - 0.5 * 1,375,008 = 48,337.1 ns
      48,337.1 / 39,095 hits = 1.24 ns/hit
    (I-103a's own assumed inline constant: ~2 ns/hit -- same order of
    magnitude, on the low side)

**Crossover, using I-103a's OWN stated model constants** (0.017 ns/B +
7.7 ns/hit memchr; 0.5 ns/B + 2 ns/hit inline; treating "frequency" as
hits per byte scanned, f):

    0.017 + 7.7f = 0.5 + 2f
    5.7f = 0.483
    f = 0.0847  (8.47%)

matching I-103a's own "near 8%" statement. **This lane's own single
per-pattern measurements corroborate the ORDER OF MAGNITUDE of both
model constants (memchr per-hit: 8.58 ns measured vs 7.7 ns assumed on
router; inline per-byte: 0.535 ns measured vs 0.5 ns assumed on router)
but cannot independently re-derive the crossover frequency**: doing so
needs the byte/hit split solved cleanly, which this data set's
near-collinear BYTES totals do not support (above), and only ONE
pattern (router, at 2.8%) has a measured inline point at all -- a
second, well-separated frequency point (ideally with the byte-count
axis varied independently of hit density, unlike this window's three
fixed-size subjects) is what a genuinely independent crossover estimate
would need.

## Summary of what changed vs I-103/I-103a's literal asks

- Config set: I-103a's wider four/two-config grid, reconciled explicitly
  (deviation 3) -- I-103's own single `(auto, --no-captures)` cell is the
  `auto-nocaps` row throughout.
- Arm (d): built and measured on router's four configs (offset 0, the
  template applies literally); STOPPED on keyword's two configs (offset
  1, the literal template would build a guard that never fires --
  deviation 4, section 3's verbatim region).
- Everything else -- 5 interleaved trials, load gate, answer-check
  before any timing, the O-50/[B81] fallback instrument shape -- follows
  I-98's protocol and I-103/I-103a's text verbatim.

Scratch artifacts (not committed, per the mandate): `/tmp/optloop5/b83/`
(`run_instrument.py`, `run_instrument.log`, `work/`, `answer_check.json`,
`rows_by_variant.json`, `results.json`, `deviations.json`) -- held per the
brief's own instruction until "I-103 logs fetched".
