# b89waf — I-107 the WAF attribution timing block (EXECUTOR role, [B89])

Ran pcrec inbox item I-107 (`docs/dev/inbox_from_pcrec.md` `## I-107`),
source `~/pcrec` `docs/dev/optloop/waf_attribution.md` §4 at commit
`f37e5c23`, setup from `cycle1_analysis.md` §0.1-0.5 (same commit) with the
two substitutions named in the brief: `OPT1=/tmp/optloop-waf` (not
`/tmp/optloop1`), and §0.2 built as a **detached** worktree at `f37e5c23`
(`lane/wafread` is merged into `origin/main` at that commit; the branch
itself no longer exists). EXECUTOR role per BD10: numbers reported
verbatim, no diagnosis, no causal commentary added beyond what each
finding's own stated criterion licenses.

All raw logs are under `$OPT1` = `/tmp/optloop-waf/` (paths listed in
§7 below).

---

## 1. pcrec commit and build facts

- Worktree: `git -C /home/duxevents/pcrec worktree add --detach
  /tmp/optloop-waf/pcrec f37e5c23` → `HEAD is now at f37e5c23 Merge branch
  'lane/s1design'`.
- `git -C /tmp/optloop-waf/pcrec log -1 --format="%H %ci %s"`:
  `f37e5c23a9b67bdeefcfbf14d75f08837aae2da4 2026-09-25 12:51:08 -0400 Merge
  branch 'lane/s1design'`.
- Confirmed `docs/dev/optloop/waf_attribution.md` (lane wafread's S3 read)
  and `docs/dev/optloop/waf/` (its instruments) are present at this commit,
  and that `cb274d33` (`Merge branch 'lane/wafread'`) is an ancestor of
  `f37e5c23` (`git merge-base --is-ancestor cb274d33 f37e5c23` → true).
- `cd /tmp/optloop-waf/pcrec && make -j4` — built clean, no errors
  (`build/pcrec` produced; `ar`/final link both succeeded).
- Compiler: `gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0`. Host:
  `Linux ubuntubudu 7.0.0-29-generic #29-Ubuntu SMP PREEMPT_DYNAMIC Fri Jul
  17 20:52:35 UTC 2026 x86_64 GNU/Linux`.
- One deviation from the literal §0 command line, disclosed: `mk_inputs.py`
  (`docs/dev/optloop/waf/mk_inputs.py`) defaults `BENCH_ROOT` to
  `/Users/fdicostanzo/pcrec-bench`, which does not exist on this box
  (`ls /Users` → no such file or directory). Ran it as
  `python3 "$W/mk_inputs.py" "$OPT1" /home/duxevents/pcrec-bench` (its
  own documented second positional argument), the same substitution
  class as the brief's `OPT1` swap. Output: `match.bin + split.rx: 5 -> 4
  arms, 1460 -> 291 bytes` — matches `waf/CLAUDE.md`'s stated 5→4/1460→291
  figures exactly.

## 2. Subject sha256 (cycle1_analysis.md §0.3)

```
t-64k  65536   d2e4f134473cc40a9a4e7df7a30e0efa11f566d96ee990c62cd663a2439c8524
t-256k 262144  3cf7b248873da164518b74e039cc2380f39e233b2899716c82c8eb4b7b49b5a7
t-1m   1048576 ccbdf7eb97f15776a68b8bbb9d6387870cd01d4796207fb20032958caf9754ee
```

All three **match** the EXPECT lines in `cycle1_analysis.md` §0.3 byte for
byte. No STOP triggered. Log: `/tmp/optloop-waf/step0_3_subjects_sha256.log`.

## 3. Clock calibration (§0.4, ×5)

```
0.2257 GHz (N=2000000000, 8.860 s)
0.2258 GHz (N=2000000000, 8.857 s)
0.2254 GHz (N=2000000000, 8.872 s)
0.2257 GHz (N=2000000000, 8.862 s)
0.2255 GHz (N=2000000000, 8.871 s)
```

Log: `/tmp/optloop-waf/step0_4_clock.log`.

## 4. Step 0: artifacts + stamps

Built (`pcrec --features all --no-captures -p rx`): the three named WAF
patterns, `split.c` (from `split.rx`), and `sleepnrb.c`
(`-fno-req-byte` on the sleep-benchmark pattern). All five compiled with no
errors. `grep -h -E '^#define RX_(DFA_SCAN|DFA_PREFILTER|REQ_BYTE) '`, per
file:

```
== wild-waf-crs-942140-dbnames.c ==
#define RX_REQ_BYTE "none"
#define RX_DFA_SCAN "unanchored"
#define RX_DFA_PREFILTER "byte-class-bounded"
== wild-waf-crs-942270-union-select.c ==
#define RX_REQ_BYTE "none"
#define RX_DFA_SCAN "unanchored"
#define RX_DFA_PREFILTER "byte-class"
== wild-waf-crs-942160-sleep-benchmark.c ==
#define RX_REQ_BYTE "41"
#define RX_DFA_SCAN "unanchored"
#define RX_DFA_PREFILTER "byte-class"
== split.c ==
#define RX_REQ_BYTE "none"
#define RX_DFA_SCAN "unanchored"
#define RX_DFA_PREFILTER "byte-class-bounded"
== sleepnrb.c ==
#define RX_REQ_BYTE "none"
#define RX_DFA_SCAN "unanchored"
#define RX_DFA_PREFILTER "byte-class"
```

Log: `/tmp/optloop-waf/step0_stamps.log`.

## 5. Step 1: twins, check.sh, match counts

Every `check.sh` invocation, in run order (SAME/DIFF on every line; no
DIFF occurred):

```
plainloop: removed 3 skip/stay loop(s)
== check.sh wild-waf-crs-942140-dbnames plainloop ==
SAME matches=0 subj/t-64k.bin
SAME matches=0 subj/t-1m.bin
SAME matches=7 match.bin
plainloop: removed 1 skip/stay loop(s)
== check.sh split plainloop ==
SAME matches=0 subj/t-64k.bin
SAME matches=0 subj/t-1m.bin
SAME matches=10 match.bin
plainloop: removed 3 skip/stay loop(s)
== check.sh wild-waf-crs-942270-union-select plainloop ==
SAME matches=0 subj/t-64k.bin
SAME matches=0 subj/t-1m.bin
SAME matches=9 match.bin
plainloop: removed 5 skip/stay loop(s)
== check.sh wild-waf-crs-942160-sleep-benchmark plainloop ==
SAME matches=0 subj/t-64k.bin
SAME matches=0 subj/t-1m.bin
SAME matches=6 match.bin
ciprecheck: run=union letter=u
== check.sh wild-waf-crs-942270-union-select ciprecheck union u ==
SAME matches=0 subj/t-64k.bin
SAME matches=0 subj/t-1m.bin
SAME matches=9 match.bin
ciprecheck: run=from letter=f
== check.sh wild-waf-crs-942270-union-select ciprecheck from f ==
SAME matches=0 subj/t-64k.bin
SAME matches=0 subj/t-1m.bin
SAME matches=9 match.bin
ciprecheck: run=from letter=m
== check.sh wild-waf-crs-942270-union-select ciprecheck from m ==
SAME matches=0 subj/t-64k.bin
SAME matches=0 subj/t-1m.bin
SAME matches=9 match.bin
ciprecheck: run=select letter=c
== check.sh wild-waf-crs-942270-union-select ciprecheck select c ==
SAME matches=0 subj/t-64k.bin
SAME matches=0 subj/t-1m.bin
SAME matches=9 match.bin
```

**Every line is SAME. No DIFF.** No STOP triggered.

**Match counts on `match.bin`** (EXPECT: dbnames 7, split 10, union 9,
sleep 6): dbnames 7, split 10, union-select 9 (all four ci-twins agree at
9), sleep-benchmark 6. **All match EXPECT exactly.**

Log: `/tmp/optloop-waf/step1_twins_check.log`.

## 6. Step 2: quiet-box gate and timing (verbatim)

**Quiet-box readings, in order** (rule: load1 < 0.5 before any timed
phase):

```
15:03:32 up 43 days, 16:10, 6 users, load average: 0.29, 0.40, 0.59   (before worktree/build)
15:06:09 up 43 days, 16:12, 6 users, load average: 0.58, 0.43, 0.56   (after clock ×5 -- ABOVE 0.5)
15:06:31 up 43 days, 16:13, 6 users, load average: 0.57, 0.43, 0.56   (recheck -- still above 0.5)
[background poll] QUIET load1=0.48   Fri Sep 25 03:06:43 PM EDT 2026
15:06:52 up 43 days, 16:13, 6 users, load average: 0.41, 0.40, 0.54   (confirmed quiet)
15:07:03 up 43 days, 16:13, 6 users, load average: 0.35, 0.39, 0.54   (=== uptime before === inside the timed block)
15:07:05 up 43 days, 16:13, 6 users, load average: 0.40, 0.40, 0.54   (=== uptime after ===)
```

load1 was above 0.5 twice (0.58, 0.57) after the clock calibration; the
timed group itself was not launched until load1 read 0.48, then 0.41, then
0.35 on three successive checks, and stayed at 0.40 at the end of the
timed block. Nothing else heavy ran on the box during the wait or the
timed block.

**Full `findall.c` timing output, in run order** (`bin_<name>` built with
`-I"$OPT1" gcc -O2`, 5 iterations/best-of, three sizes each):

```
=== uptime before ===
 15:07:03 up 43 days, 16:13,  6 users,  load average: 0.35, 0.39, 0.54

# t wild-waf-crs-942140-dbnames wild-waf-crs-942140-dbnames  (dbnames BASE)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000200881 s  3.0652 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000803413 s  3.0648 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.003236875 s  3.0869 ns/byte

# t wild-waf-crs-942140-dbnames_plain wild-waf-crs-942140-dbnames  (dbnames PLAIN)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000117920 s  1.7993 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000468602 s  1.7876 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.001902089 s  1.8140 ns/byte

# t split split  (split BASE)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000154951 s  2.3644 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000621853 s  2.3722 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.002516041 s  2.3995 ns/byte

# t split_plain split  (split PLAIN)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000118600 s  1.8097 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000474112 s  1.8086 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.001894999 s  1.8072 ns/byte

# t $U $U  (union-select BASE)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000047411 s  0.7234 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000187431 s  0.7150 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.000752624 s  0.7178 ns/byte

# t ${U}_plain $U  (union-select PLAIN)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000120160 s  1.8335 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000479442 s  1.8289 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.001932349 s  1.8428 ns/byte

# t ${U}_ci_unionu $U  (union-select ci_unionu)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000029000 s  0.4425 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000119030 s  0.4541 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.000492942 s  0.4701 ns/byte

# t ${U}_ci_fromf $U  (union-select ci_fromf)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000021110 s  0.3221 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000087640 s  0.3343 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.000360811 s  0.3441 ns/byte

# t ${U}_ci_fromm $U  (union-select ci_fromm)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000014020 s  0.2139 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000057780 s  0.2204 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.000246211 s  0.2348 ns/byte

# t ${U}_ci_selectc $U  (union-select ci_selectc)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000029240 s  0.4462 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000111370 s  0.4248 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.000460182 s  0.4389 ns/byte

# t wild-waf-crs-942160-sleep-benchmark wild-waf-crs-942160-sleep-benchmark  (sleep BASE)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000064320 s  0.9814 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000247111 s  0.9427 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.000976945 s  0.9317 ns/byte

# t wild-waf-crs-942160-sleep-benchmark_plain wild-waf-crs-942160-sleep-benchmark  (sleep PLAIN)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000116320 s  1.7749 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000463072 s  1.7665 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.001862919 s  1.7766 ns/byte

# t sleepnrb sleepnrb  (sleep, -fno-req-byte)
/tmp/optloop-waf/subj/t-64k.bin n=65536 matches=0 best=0.000061601 s  0.9400 ns/byte
/tmp/optloop-waf/subj/t-256k.bin n=262144 matches=0 best=0.000235751 s  0.8993 ns/byte
/tmp/optloop-waf/subj/t-1m.bin n=1048576 matches=0 best=0.000941724 s  0.8981 ns/byte

=== uptime after ===
 15:07:05 up 43 days, 16:13,  6 users,  load average: 0.40, 0.40, 0.54
```

(The `# ...` lines above are labels added for this report, matching the
`t()` invocation order in the brief's §2 block; the timing tool's own
output lines are byte-for-byte as printed. Full raw output, unlabeled:
`/tmp/optloop-waf/step2_timing_output.log`.)

All 39 subject rows report `matches=0`, consistent with §1's note that all
five cells are zero-match scans on the throughput subjects; `giveup` never
printed.

## 7. Log paths (all under `$OPT1` = `/tmp/optloop-waf/`)

- `/tmp/optloop-waf/step0_3_subjects_sha256.log` — §0.3 subject generation + sha256
- `/tmp/optloop-waf/step0_4_clock.log` — §0.4 clock calibration ×5
- `/tmp/optloop-waf/step0_stamps.log` — the five artifacts' `#define RX_(DFA_SCAN|DFA_PREFILTER|REQ_BYTE)` grep
- `/tmp/optloop-waf/step1_twins_check.log` — every `check.sh` SAME/DIFF line
- `/tmp/optloop-waf/step2_timing_output.log` — the full timing block, verbatim, unlabeled
- `/tmp/optloop-waf/*.c` / `*.h` — the eighteen compiled artifacts (5 base + 4 plainloop twins + 4 ciprecheck twins + sleepnrb; `bin_*` executables alongside)
- `/tmp/optloop-waf/subj/{t-64k,t-256k,t-1m}.bin`, `/tmp/optloop-waf/match.bin`, `/tmp/optloop-waf/split.rx`

---

## 8. I-107 expectations vs measured (all ns/B at `t-1m`)

Hit counts (lower+upper case) are `waf_attribution.md` §3.2's table, cited
for the per-hit-count order check only; nothing here re-derives them.

| id | expectation (as stated in I-107) | measured (t-1m) | verdict per I-107's own stated criterion |
|---|---|---|---|
| U1 `ci_fromm` | ≈ 0.12 | **0.2348** | see below |
| U1 `ci_fromf` | ≈ 0.17 | **0.3441** | see below |
| U1 `ci_selectc` | ≈ 0.19 | **0.4389** | see below |
| U1 `ci_unionu` | ≈ 0.27 | **0.4701** | see below |
| U1 — refuted if any ≥ base 0.72 | base (union-select) = 0.7178 | none of the four ≥ 0.7178 | **CONFIRMED** (not refuted by this stated test) |
| U1 — order must follow hits (18k<27k<30k<43k: fromm<fromf<selectc<unionu) | — | measured order fromm(0.2348) < fromf(0.3441) < selectc(0.4389) < unionu(0.4701) — same order as the hit counts | **CONFIRMED** ("a uniform upward shift with the order intact still confirms the mechanism" — I-107's own wording) |
| U1 — "all below re2's 0.319" (part of the opening claim, not one of the two bulleted refutation tests) | < 0.319 | fromm 0.2348 below; fromf 0.3441, selectc 0.4389, unionu 0.4701 all above 0.319 | **N/A** — not one of I-107's two named refutation criteria; reported as raw fact, no verdict assigned |
| U2 `union-select_plain` vs base, slower, ~1.8-3.2 ns/B | plain slower than base | base 0.7178, plain **1.8428** (plain > base; within the stated 1.8-3.2 range) | **CONFIRMED** |
| U3 `sleep_plain` vs base, slower | plain slower than base | base 0.9317, plain **1.7766** (plain > base) | **CONFIRMED** |
| L1 `dbnames_plain` | ≤~1.8 (near re2 1.63) = dispatch net cost; ≈base (2.9) = dispatch free; in-between reported as a fraction | base **3.0869**, plain **1.8140** | **N/A** — I-107 frames this as a fraction report, not confirm/refute. Fraction of the base→re2(1.63) gap closed: (3.0869−1.8140)/(3.0869−1.63) = **87.4%** |
| L1 `split_plain` | ≤~1.8 (near re2 1.63) = dispatch net cost; ≈base (2.4) = dispatch free; in-between reported as a fraction | base **2.3995**, plain **1.8072** | **N/A** — same framing. Fraction of the base→re2(1.63) gap closed: (2.3995−1.8072)/(2.3995−1.63) = **77.0%** |
| L2 FIRSTSET re-seed rerun, dbnames 14-byte twin, 5 trials, model predicts 2.09 | — | **not run** | **N/A — L2 not staged**: see §9 |
| L4 `sleepnrb` vs base — below 1% "clears" the REQ_BYTE pre-check as the drift's cause; item says "Record, don't chase" | — | base 0.9317, sleepnrb **0.8981**; diff = 0.0336 ns/B = **3.61%** (≥ 1%) | **N/A** — I-107 states no pass/fail for this row, only "record"; the measured 3.61% is ≥ the stated 1% line, recorded as instructed |

## 9. L2 — not staged

Per the brief: run L2 only if `firstset_design.md` §7's F1 block is
executable **verbatim with the files present** at `f37e5c23`. It is not.

F1 (`docs/dev/optloop/firstset_design.md` §7, at `f37e5c23`) runs
`"$OPT1/twin_wild-codegrammar-json-constant"` and
`"$OPT1/base_wild-codegrammar-json-constant"` — artifacts that are not
built by anything in §7 itself. They are `cycle1_analysis.md` §"M3"'s
outputs, specifically M3.b (`base_wild-codegrammar-json-constant`, a
plain compile — staged) and **M3.c**, the "HAND-TWIN": the block's own
text reads "in each artifact, overwrite `rx_can_begin_match[256]` with
the set PCRE2 records ... Rebuild" — a manual source edit performed by a
person/session at execution time, not a checked-in generator or twin
source file. `git ls-tree -r f37e5c23 --name-only | grep -i
"json-constant\|codegrammar"` returns nothing: no
`twin_wild-codegrammar-json-constant.c` or equivalent is tracked at this
commit. Building it would mean authoring the hand-edit myself, which the
brief explicitly rules out ("Don't build anything to make it work").

**L2 not staged: F1 depends on a hand-twin (`M3.c`) that has no committed
source at `f37e5c23` — it is manual-edit instructions, not a script — so
the block is not executable verbatim with the files present.**

## 10. Cleanup

`git -C /home/duxevents/pcrec worktree remove /tmp/optloop-waf/pcrec` run
at the end of this session. `$OPT1`'s other files (`subj/`, `*.c`, `*.h`,
`bin_*`, `match.bin`, `split.rx`, the `*.log` files listed in §7) are kept.
