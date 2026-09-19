# lane `b54extwindow` — the ext-bench roster's SECOND SAMPLE (TRE high-byte-run reproducibility)

Branch `lane/b54extwindow`, worktree `worktrees/b54extwindow`. Charter:
`docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md` §8 item 2 —
re-measure `re2-default`, `tre-default`, `vectorscan-block-nosom` on
`bench/capability@0.1` to check whether TRE's `high-byte-run`
correctness gap (0% throughput / 48% search pass rate on the first
sample) is reproducible or was a one-off box artifact.

## What was produced

**Three new pinned records**, `store/index.tsv` 178 → 181 (180
record(s) by the index's own count, header excluded): `re2-default`,
`tre-default`, `vectorscan-block-nosom` on `bench/capability@0.1`, all
`measured` at attempt 1, rc=0, five trials each, all `agree`.

**One report group** (7 files, `reports/2026-09-19-capability-0.1-
budu-ryzen1600-ext-second-cf0962e3.*`): `.md`/`.tsv`/
`.subject-grain.md`/`.subject-grain.tsv` plus `.matrix.tsv`/
`.matrix.html` siblings, all CLI-generated against the same narrowed
three-testee query shape the ext-first group used (explicit
`--since`/`--until` + explicit `--testee` roster, no reference/baseline
arms) — 3 record(s) matching, 3 included, 0 superseded.

**Interpretation sidecar**, generated and determinism-checked (a second
`interpret` invocation to stdout diffs clean against the committed
file) against `docs/dev/predictions/capability-0.1-first.tsv` only.
`docs/dev/predictions/capability-0.1-ext-roster.tsv` (a file that did
not exist when this lane's brief was written — landed via a separate
lane, b51preds) was deliberately NOT passed: `docs/dev/wake.md`'s
standing fact says it cannot be CLI-scored until pcrec's F27 fix lands,
and this lane's brief explicitly said not to touch or score it.

**Six pre-existing sidecars also moved**, automatically, as a
consequence of `scripts/run_window.sh`'s own end-of-window step
(`scripts/regen_sidecars.py`, run against the canonical store since
this lane's records landed there): each changes by exactly its
`index_sha256` stamp line, nothing below the stamp (confirmed via
`git diff` on all six) — the expected, previously-documented delta
class, not a content change.

**Directory doc**: a `[B54]` entry in `reports/CLAUDE.md`.

## The headline finding

`high-byte-run`'s TRE correctness gap **reproduces byte-identical**:

| pattern / regime | first sample | this (second) sample |
|---|---|---|
| `high-byte-run` / throughput | `pass_rate 0.0000` (3/3 wrong) | `pass_rate 0.0000` (15/15 wrong — n=3 subjects × 5 trials) |
| `high-byte-run` / search | `pass_rate 0.4800` (195/375 wrong) | `pass_rate 0.4800` (195/375 wrong) |
| `tag-pair-match` / search | `pass_rate 0.9867` (5/75 wrong) | `pass_rate 0.9867` (5/75 wrong) |
| `wild-waf-crs-942360-concat-sqli` / search | `pass_rate 0.9867` (5/75 wrong) | `pass_rate 0.9867` (5/75 wrong) |
| `tre-default` did-not-compile set | `wild-datetime-datefinder-alternation`, `wild-secrets-username-password-pair`, `wild-waf-crs-942500-comment-obfuscation` | same three, unchanged |

`re2-default` and `vectorscan-block-nosom` both stay `pass_rate 1.0000`
clean on `high-byte-run` in both samples — the gap is TRE-specific and
not a box artifact. All numbers read directly from the committed report
TSV and interpretation sidecar (`R-STATUS-3` section); no reading or
ranking is asserted here beyond what those files state — the morning
read lane owns the ledger interpretation.

## Two incidents

1. **First launch attempt refused instantly, all three cells, rc=1**:
   the worktree had never had `bench/capability`'s gitignored subject
   trees generated (`bench/capability/gen_subjects.py` /
   `gen_throughput_subjects.py`). Not committed — fixed by running both
   generators (manifests reproduced byte-identical, `git diff` clean)
   before relaunching. **Worth a KB note** (not filed by this lane,
   scope): `run_window.sh` printed `WINDOW_RUN_COMPLETE` after all
   three cells failed setup with nothing measured — the sentinel means
   "the script's control flow reached the end," not "cells succeeded,"
   and a reader trusting the marker alone (as this lane initially did)
   would believe the window succeeded. The log body has to be read, not
   just the marker/sentinel.
2. **Two background-notification stalls** during this lane's own
   run: once waiting on the relaunched window's completion marker
   (the team lead caught it from outside), once waiting on the report
   CLI render (~30 min gap with no foreground activity). Both times the
   underlying command had actually finished; the stall was in this
   lane surfacing that fact rather than in the command itself. No
   store or report content was affected, but it cost real wall time
   this lane should not have spent idle.
3. **A worktree-path mistake, caught and fixed before commit**: the
   first edit to `reports/CLAUDE.md` was made with an absolute path
   that resolved to the MAIN checkout (`/home/duxevents/pcrec-bench/
   reports/CLAUDE.md`) instead of this worktree's copy — a mandate
   violation (BOILERPLATE: touch only this lane's own worktree). Caught
   immediately by checking `git status` on the main checkout, reverted
   there (`git checkout -- reports/CLAUDE.md`, confirmed the diff was
   exactly this lane's intended addition and nothing else before
   reverting), and re-applied correctly inside the worktree. Main
   checkout confirmed clean afterward.

## Validation

- **CLI equivalence**: the report group was produced by direct
  `python3 -m pcrecbench report ...` invocations (no in-process
  script) — the committed files ARE the CLI's own output.
- **Determinism**: the `.interpretation.md` sidecar was re-generated to
  stdout via a second, independent `interpret` invocation and diffed
  clean against the committed file (`DETERMINISM_OK`).
- Every number in this report and in the `[B54]` `reports/CLAUDE.md`
  entry is read directly from the committed `.tsv`/`.interpretation.md`
  files (grepped/awked, cited above), not re-derived or inferred.
- `git status` on both this worktree and the main checkout confirmed
  clean before and after every commit in this lane.

## Charter-vs-committed checklist

| brief item | status |
|---|---|
| 1. Three cells measured into `store/`, statuses/attempts/wall times stated | **COMMITTED** — all three `measured`, attempt 1, rc=0 (re2-default 23:22:04-23:35:52 EDT, tre-default 23:36:07-23:55:32 EDT, vectorscan-block-nosom 23:55:47-00:16:16 EDT) |
| 2. `pcrecbench index`, new store count stated | **COMMITTED** — 178 → 181 (180 records, header excluded) |
| 3. Report group, v18, four surfaces + matrix siblings | **COMMITTED** — `reports/2026-09-19-capability-0.1-budu-ryzen1600-ext-second-cf0962e3.*` (7 files) |
| 4. Interpretation sidecar, determinism-checked | **COMMITTED** — determinism verified |
| 5. Final summary to the team lead | sent alongside this report |
| Do NOT touch/score the predictions file | honored — `capability-0.1-ext-roster.tsv` was found (new since brief) but deliberately not passed to `interpret` |
| Do NOT write a ledger reading | honored — no `docs/dev/ledgers/` file written by this lane |
| Do NOT merge | honored — branch left for the manager |

**Nothing is OWED.** Every deliverable in the brief is committed on
`lane/b54extwindow`.
