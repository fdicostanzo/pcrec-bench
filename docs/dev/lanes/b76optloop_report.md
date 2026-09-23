# [B76] I-89 + I-89a executor lane — STOPPED at pin verification (§0.1)

Role: executor (I-57 terms) on inbox I-89 (`docs/dev/inbox_from_pcrec.md`
lines 2625-3048) + amendment I-89a (lines 3050-3069). Report, never
diagnose.

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

No other command from I-89/I-89a was run.
