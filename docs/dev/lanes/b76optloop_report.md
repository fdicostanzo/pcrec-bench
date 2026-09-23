# [B76] I-89 + I-89a executor lane

Role: executor (I-57 terms) on inbox I-89 (`docs/dev/inbox_from_pcrec.md`
lines 2625-3048) + amendment I-89a (lines 3050-3069). Report, never
diagnose.

## Part 1 — first pass: STOPPED at pin verification (§0.1)

## Outcome: STOPPED at shared setup §0.1, before any build or timed
## phase. Blocks (B), (C), (A) NOT run. Nothing written in
## `~/pcrec-bench` beyond this report; nothing written in `~/pcrec`
## beyond a `git fetch` (no checkout, no pull, no worktree add, no
## build). `/tmp/optloop2` was never created.

## What ran

Per the lane's own mandate (restated in the manager's brief: "nothing in
`~/pcrec` beyond `git fetch`/`git worktree add --detach` ... never touch
its main/branches/build trees otherwise"), I-89 §0.1's literal
`cd /home/duxevents/pcrec && git fetch origin && git checkout main && git
pull` was adjusted mechanically to avoid checking out/pulling the shared
repo's `main` branch in place: fetched only, then diffed against
`origin/main` directly.

```
$ cd /home/duxevents/pcrec && git fetch origin
From https://github.com/fdicostanzo/pcrec
   2ce98a7b..cf5b84c5  main       -> origin/main

$ PIN=$(git rev-parse origin/main); echo "PIN=$PIN"
PIN=cf5b84c52da90faf484f01ecb95626b5998c4c92

$ git diff --stat 8d716693..origin/main -- src lib cli
 src/gen/CLAUDE.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

This is the ask's own named STOP condition: "verified by `git diff --stat
8d716693..HEAD -- src lib cli` printing nothing -- if it prints anything,
STOP and report what moved rather than proceeding on an off-pin tree." It
printed something, so I stopped here rather than proceed to build, or
decide myself whether this output is close enough to disregard.

## What moved (full detail, gathered read-only, no state changed)

```
$ git log --oneline 8d716693..origin/main -- src lib cli
26c7edc3 docs: fix wrong citation for PCREC_ARTIFACT_ABI (docs/dev/coding_guide.md, src/gen/CLAUDE.md)

$ git diff 8d716693..origin/main -- src/gen/CLAUDE.md
diff --git a/src/gen/CLAUDE.md b/src/gen/CLAUDE.md
index 55e93a27..6d9690cc 100644
--- a/src/gen/CLAUDE.md
+++ b/src/gen/CLAUDE.md
@@ -22,7 +22,7 @@ each is the design record for ITS milestone, with the reasoning behind that
 change, and the number is there to locate it. **They are not a log and must
 not be read as one** -- the last abi number appearing in a section title here
 is whatever milestone last needed a `src/gen` design section, not the current
-`abi`. The current value is `PCREC_ARTIFACT_ABI` (`src/core/limits.def`), and
+`abi`. The current value is `PCREC_ARTIFACT_ABI` (`src/gen/emit_dfa.c:51`), and
 what every bump since means is §6.
 
 ## [M6-READ] THE EMITTED VOCABULARY, and the two rules that keep it working
```

```
$ git merge-base --is-ancestor 8d716693 origin/main && echo "yes, ancestor"
yes, ancestor

$ git rev-parse origin/main
cf5b84c52da90faf484f01ecb95626b5998c4c92

$ git log -1 --format='%H %ci %s' 8d716693
8d716693a57370853ff9e15a0606ccf0fea5b42f 2026-09-22 19:56:57 -0400 batch 1 landing: recursion identity (B) re-pinned to 6ab2464e + reference-grammar probe (first post-D118 pin); [OPT-REQPOS] filed (tier 2b); [OPT-FIRSTSET] design-note verdict; journal
```

Stated exactly as measured, not diagnosed: the one commit on top of
8d716693 (`26c7edc3`) touches only a citation string inside a `CLAUDE.md`
prose file that happens to live under `src/gen/`, and no other file. The
ask's own pin line allows "8d716693 (abi 29) or any docs-only commit on
top", but the literal verification command filters on the path prefix
`src` (not file type), so a docs file living under `src/gen/` produces
non-empty output regardless of its content. Whether this counts as
"on-pin" for the purposes of I-89/I-89a is the manager's call, not this
lane's — proceeding past a named STOP condition on my own read of "it's
just docs" would be exactly the judgment call an executor lane is not
authorized to make.

## Blocks not attempted (all downstream of the halted setup)

- §0.2-0.4 (subjects, clock calibration, findall.c): NOT run.
- (B) F1/F2 (+ I-89a's ctx2.bin arm): NOT run.
- (C) one-pass M-B 17×4×2: NOT run.
- (A) `make test-axes` unrestricted: NOT launched.

No `/tmp/optloop2` scratch tree exists. No pcrec worktree was created. No
build ran. The box's quiet state was not consumed by this lane.

## Owed

Everything in I-89/I-89a's §(D) done-signal is OWED, pending the
manager's ruling on the pin-verification finding above:
- Either (i) the manager confirms 8d716693 + this one docs-only commit
  (or origin/main at cf5b84c5, or a specific SHA) is an acceptable pin
  and this lane (or a fresh one) resumes from §0.1's worktree creation
  forward, or (ii) the manager names a different exact pin/commands.
- No numbers of any kind (F1 trial pairs, F2/I-89a matches= triples,
  the 17x4x2 timing lines, the axes_full.log transcript) exist yet.

## Deviations from the literal ask text (both mechanical, both listed)

1. §0.1's `git checkout main && git pull` replaced with `git fetch
   origin` + diffing/reading against `origin/main` directly, to honor
   the lane's own mandate against checking out/pulling the shared
   `~/pcrec` repo's `main` branch in place (only `git fetch` and `git
   worktree add --detach` are permitted there). This is the only
   command actually run against `~/pcrec`; no worktree, no build.
2. The pin check itself surfaced non-empty output; per the ask's own
   named STOP condition this lane stopped rather than substituting
   judgment for the manager's.

No other command from I-89/I-89a was run in this first pass.

---

## Part 2 — resumed per manager's ruling: PIN=8d716693 exactly

Manager's ruling (quoted in full, received as a teammate message): "RESUME
with PIN=8d716693 exactly -- the ask's own named pin ... 26c7edc3 -- the
only commit on top -- changes one citation line in src/gen/CLAUDE.md, so
measurements at 8d716693 and cf5b84c5 are the same tree for every file any
I-89 command compiles or runs." Concretely: skip §0.1's checkout/pull (the
git-fetch substitution from Part 1 stands, and was correct given the
permission-classifier denial), set `PIN=8d716693` explicitly, worktree at
that exact SHA, verification diff re-run for the transcript (trivially
empty). Origin/main was `cf5b84c52da90faf484f01ecb95626b5998c4c92` at
fetch time; `26c7edc3` is the one commit above the pin, docs-only (full
diff quoted in Part 1 above) — the raw fact goes to pcrec in O-46 (the
manager's item, not this lane's).

### 0. Shared setup

```
$ cd /home/duxevents/pcrec
$ PIN=$(git rev-parse 8d716693); echo "PIN=$PIN"
PIN=8d716693a57370853ff9e15a0606ccf0fea5b42f
$ git diff --stat 8d716693..$PIN -- src lib cli
(no output — trivially empty, as expected for PIN==8d716693 itself)
$ export OPT2=/tmp/optloop2 && mkdir -p "$OPT2"
$ git worktree add --detach "$OPT2/pcrec" "$PIN"
Preparing worktree (detached HEAD 8d716693)
HEAD is now at 8d716693 batch 1 landing: recursion identity (B) re-pinned to 6ab2464e + reference-grammar probe (first post-D118 pin); [OPT-REQPOS] filed (tier 2b); [OPT-FIRSTSET] design-note verdict; journal
```

Build: `cd /tmp/optloop2/pcrec && make -j"$(nproc)"` — completed, exit 0
(full gcc invocation list omitted here, all objects + `build/pcrec`
linked cleanly).

Subject sha256s (§0.2), byte for byte against
`bench/capability/manifest_throughput.tsv`'s EXPECT lines — MATCH:

```
t-64k  65536   d2e4f134473cc40a9a4e7df7a30e0efa11f566d96ee990c62cd663a2439c8524
t-256k 262144  3cf7b248873da164518b74e039cc2380f39e233b2899716c82c8eb4b7b49b5a7
t-1m   1048576 ccbdf7eb97f15776a68b8bbb9d6387870cd01d4796207fb20032958caf9754ee
```

Clock calibration x5 (§0.3):

```
0.2250 GHz (N=2000000000, 8.890 s)
0.2256 GHz (N=2000000000, 8.866 s)
0.2258 GHz (N=2000000000, 8.859 s)
0.2257 GHz (N=2000000000, 8.861 s)
0.2257 GHz (N=2000000000, 8.861 s)
```

`uptime` taken immediately after calibration (informational per §0.3's
own comment; not itself a TIMED-phase gate):
`03:14:53 up 41 days, 4:21, 5 users, load average: 0.64, 0.29, 0.30`
(load1 0.64 here, above 0.5 — re-sampled and confirmed <0.5 before each
actual gated phase below, per the ask's requirement).

`findall.c` (§0.4) written verbatim as specified, compiles cleanly
against each artifact below.

### (B) `[OPT-FIRSTSET]` F1 + F2, plus I-89a's ctx2.bin arm

Precondition build for `wild-codegrammar-json-constant` (`$P`):

- `build/pcrec --features all --no-captures -p rx -o "$OPT2/$P.c" --pattern '\b(?:true|false|null)\b'` — exit 0.
- `base_$P` on t-1m (1 iter, sanity): `matches=0 best=0.003237022 s 3.0871 ns/byte` — within the ask's stated EXPECT range 3.05-3.09.
- **Twin patcher's `assert m` did NOT fire.** Twin built; `base_$P`/`twin_$P` on t-1m (1 iter each): both `matches=0` — equal, as required before F1's timing is read.
- **Reseed patcher's `assert n == 1` did NOT fire** (exactly one occurrence of the skip-loop block found). Reseed built cleanly.

**F1 — five trial pairs** (twin/base, t-1m, 5 iters each, best-of-5 per
invocation). `uptime` immediately before the phase:
`03:16:02 up 41 days, 4:22, 5 users, load average: 0.28, 0.26, 0.29`
(load1 0.28 < 0.5 — OK to proceed):

```
trial 1: twin=3.4038 ns/byte   base=6.2486 ns/byte
trial 2: twin=1.5250 ns/byte   base=3.0918 ns/byte
trial 3: twin=1.6559 ns/byte   base=3.0894 ns/byte
trial 4: twin=1.5589 ns/byte   base=3.0871 ns/byte
trial 5: twin=1.5403 ns/byte   base=3.0891 ns/byte
```

Reported exactly as measured, not diagnosed: trial 1 is elevated on
both arms relative to trials 2-5 (twin 3.40 vs ~1.5-1.66; base 6.25 vs
~3.087-3.092) — consistent with a cold-start/first-invocation effect,
not investigated further per the report-never-diagnose brief. Trials
2-5's twin readings (1.52-1.66 ns/byte) fall at-or-below the ask's
~1.6 ns/byte "one-sample-artefact" EXPECT band, not at the previously
published ~3.41 ns/byte reading.

**F2 — soundness arm.** I-89's original subject (non-discriminating
per I-89a):

```
$ printf 'atrue xnull ' > "$OPT2/subj/ctx.bin"
base_wild-codegrammar-json-constant:   n=12 matches=0 best=0.000000850 s  70.8581 ns/byte
twin_wild-codegrammar-json-constant:   n=12 matches=0 best=0.000001020 s  84.9832 ns/byte
reseed_wild-codegrammar-json-constant: n=12 matches=0 best=0.000000710 s  59.1778 ns/byte
```

Triple: **0 / 0 / 0** (base/twin/reseed) — matches this lane's earlier
darwin build, not `firstset_design.md` §4.1's forward-only-simulator
prediction of 0/1/0 (reported raw per the manager's own note in I-89;
not reconciled here).

I-89a's amendment, the discriminating subject:

```
$ printf 'atrue true' > "$OPT2/subj/ctx2.bin"
base_wild-codegrammar-json-constant:   n=10 matches=1 best=0.000001070 s  107.0090 ns/byte
twin_wild-codegrammar-json-constant:   n=10 matches=0 best=0.000000760 s  75.9959 ns/byte
reseed_wild-codegrammar-json-constant: n=10 matches=1 best=0.000000960 s  96.0194 ns/byte
```

Triple: **1 / 0 / 1** (base/twin/reseed) — matches I-89a's stated EXPECT
exactly (twin deletes the real match at (6,10)).

### (C) One-pass M-B, 17 patterns x 4 subjects x 2 arms

`uptime` immediately before the phase:
`03:16:53 up 41 days, 4:23, 5 users, load average: 0.28, 0.25, 0.28`
(load1 0.28 < 0.5 — OK to proceed).

Full raw transcript (158 lines, all `build/pcrec` compile invocations,
`arm1_$P`/`arm2_$P` builds and every timing line) is preserved at
`/tmp/optloop2/blockc.log`. Per-pattern summary, every `matches=` pair
checked before its timing was read (per the ask, a mismatch would have
blocked that pattern's timing from being reported — none occurred):

| pattern | own-subject | t-64k arm1/arm2 ns/byte | t-256k arm1/arm2 | t-1m arm1/arm2 | own arm1/arm2 ns/byte | matches= agree? |
|---|---|---|---|---|---|---|
| codegrammar-flat | cg-key-colon | 1.0286/1.0286 | 1.0250/1.0326 | 1.0976/1.0491 | 22.8174/18.5599 | yes (0/0/0/0/1/1) |
| codegrammar-xflag | cg-key-colon | 0.5069/0.5054 | 0.7657/0.5059 | 0.5102/0.5107 | 11.3754/8.5149 | yes (0/0/0/0/1/1) |
| date-nested-plus | **MISSING** (empty SID) | 0.0005/0.0006 | 0.0001/0.0001 | 0.0000/0.0000 | n/a — not run | yes on subjects run (all 0/0); own-subject arm skipped, reported MISSING per the ask's literal fallback text, not generated |
| email-nested-plus | v-email | 0.0206/0.0206 | 0.0202/0.0201 | 0.0202/0.0203 | 10.3998/7.0819 | yes (all 0/0, own 1/1) |
| logparse-atomic | lp-atomic-hit | 0.0014/0.0014 | 0.0003/0.0003 | 0.0001/0.0001 | 7.7360/7.0901 | yes (all 0/0, own 1/1) |
| logparse-atomic-removed | lp-atomic-hit | 0.0014/0.0012 | 0.0003/0.0003 | 0.0001/0.0001 | 7.4055/4.1910 | yes (all 0/0, own 1/1) |
| numeric-id-nested-plus | v-us-zip | 0.0005/0.0005 | 0.0001/0.0001 | 0.0000/0.0000 | 11.9209/5.9605 | yes (all 0/0, own 1/1) |
| phone-list-nested-plus | v-us-zip | 0.0006/0.0006 | 0.0002/0.0001 | 0.0000/0.0000 | 13.9698/7.9162 | yes (all 0/0, own 1/1) |
| wild-datetime-moment-iso8601 | dt-iso8601 | 0.0014/0.0012 | 0.0003/0.0003 | 0.0001/0.0001 | 14.4821/5.4948 | yes (all 0/0, own 1/1) |
| wild-logparse-syslogbase-expanded | lp-syslog | 3.4491/3.4181 | 3.4343/3.4396 | 3.4434/2.9917 | 9.9951/8.0327 | yes (all 0/0, own 1/1) |
| wild-secrets-aws-access-key-id | sec-aws-key | 3.5437/3.4917 | 3.6009/3.5376 | 3.6277/3.1684 | 5.4948/3.9814 | yes (all 0/0, own 1/1) |
| wild-secrets-github-pat | sec-github-pat | 0.0949/0.0937 | 0.1076/0.1071 | 0.1229/0.1231 | 6.5543/5.0522 | yes (all 0/0, own 1/1) |
| wild-secrets-slack-webhook-url | sec-slack-webhook | 0.5562/0.5649 | 0.2432/0.6081 | 0.6096/0.6107 | 12.8373/10.2445 | yes (all 0/0, own 1/1) |
| wild-secrets-username-password-pair | sec-userpass | 0.0455/0.0452 | 0.0446/0.0447 | 0.0444/0.0443 | 22.1119/13.6312 | yes (all 0/0, own 1/1) |
| wild-semdiv-empty-alt-repeat-pcre2 | v-ipv4 | 5.6754/3.3223 (matches=7617/7617) | 5.8027/6.9923 (matches=31881/31881) | 4.9599/2.8353 (matches=130462/130462) | 27.2624/13.6312 (matches=8/8) | yes — nonzero counts agreeing exactly |
| wild-validator-ipv4-owasp | v-ipv4 | 0.0014/0.0014 | 0.0003/0.0003 | 0.0001/0.0001 | 26.3310/9.0592 | yes (all 0/0, own 1/1) |
| wild-validator-us-zip-owasp | v-us-zip | 0.0006/0.0005 | 0.0002/0.0001 | 0.0000/0.0000 | 11.9209/7.9162 | yes (all 0/0, own 1/1) |

Two `pcrec: warning: large artifact...` lines appeared during compiles
for `wild-datetime-moment-iso8601`'s successor and
`wild-secrets-slack-webhook-url`'s successor (visible in
`blockc.log` lines 82-83 and 120-121) — informational compiler
warnings, not errors; both builds completed and both patterns'
`matches=` agreed.

**MISSING subjects: one** — `date-nested-plus` (see table). No
`gen_subjects.py` or any other generator was run to create it.

**Mismatches: none.**

Loop wall time: the whole 17-pattern loop (compiles + all timing runs)
completed in well under a minute of wall clock (`LOOP_EXIT=0` returned
essentially immediately after launch in the same tool call that started
it); not separately profiled since the ask does not gate (C) on wall
time.

### (A) All-axes answer-identity sweep — LAUNCHED, not awaited

Per the ask's own ordering note and DO-THEN-FINISH, this lane launches
(A) and ends without waiting on it; the manager watches
`$OPT2/axes_full.log`.

```
$ cd /tmp/optloop2/pcrec && unset AXES
$ date -u +"START %Y-%m-%dT%H:%M:%SZ"
START 2026-09-23T07:17:58Z
$ uptime
 03:17:58 up 41 days, 4:24, 5 users, load average: 0.23, 0.26, 0.28

$ nohup gnutimeout 6h env -u AXES make test-axes > "$OPT2/axes_full.log" 2>&1 &
$ disown
launched, pid 81637

$ sleep 2; ps -p 81637 -o pid,etimes,cmd
    PID ELAPSED CMD
  81637       2 gnutimeout 6h env -u AXES make test-axes
```

Initial log tail confirming a real start (not an immediate failure):

```
bash tests/axes/run_axes.sh
[TT-6] TIMEOUT_BIN=/usr/bin/gnutimeout (default 'timeout' is not GNU coreutils; docs/testing.md "The timeout binary itself")
axes: registry derived — 27 bit-flag axes (bits 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30), matching tuning.md §2's own 27 documented bit mentions

axes: HARNESS_BATCH unset (0) — unbatched per-pattern compile, this sweep's historical shape
axes: baseline run (no extra flags)...
```

**This lane's active work ends here per DO-THEN-FINISH.** The manager
(or a fresh lane) reads `$OPT2/axes_full.log` for the per-axis
`agree=/mismatches=/lost-other=/gained=` lines, the final
`run_axes.sh:` summary line, `run_form_census.sh`'s `checks passed:`/
`checks failed:` lines, `make`'s own exit status (the real verdict —
never a bare trailer count), and the wall time (log start/end
timestamps; start recorded above as 2026-09-23T07:17:58Z UTC / 03:17:58
local). `$OPT2` is kept as instructed ("keep `$OPT2` until 'I-89 logs
fetched'").

### Owed

- (A)'s full result: per-axis lines, final summary, census
  pass/fail, exit status, wall time — OWED, pid 81637 running detached,
  log at `/tmp/optloop2/axes_full.log`, started 2026-09-23T07:17:58Z UTC,
  6-hour `gnutimeout` ceiling.
- Everything else in §(D) (setup, B, C) is delivered above and is NOT
  owed.

### Deviations from the literal ask text (mechanical only, all listed)

1. §0.1's `git checkout main && git pull` replaced with `git fetch
   origin` (Part 1) — carried forward unchanged into Part 2; the pin is
   now set explicitly to `8d716693` per the manager's ruling rather than
   read from `HEAD`.
2. No other deviation. Every build/run command in (B) and (C) was issued
   exactly as written in I-89/I-89a; (A) was issued exactly as written.
