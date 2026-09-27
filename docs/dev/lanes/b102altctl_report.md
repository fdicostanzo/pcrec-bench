# lane b102altctl — report

Task: `docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7-addendum-r2r7.md`
§8 candidate 1 — decide how far the ALREADY-COMMITTED `bench/altwide@0.2`
records separate "64 branches" from "Cyrillic/2-byte-per-char" as the
cause of `bench/utf8`'s `alt-cyr-64` tripping R4 (script band) and R5
(compile-time cliff). Read-only; no measurement, no window, no store-wide
reporter load; the deliverable is a ledger, not a build.

## Operational note: the box was at 920 MB free (disk-full)

`git worktree add worktrees/b102altctl -b lane/b102altctl` FAILED partway
through a full checkout (`error: unable to write file
store/records/…jsonl`, `df -h /` showed 921 MB avail on a 98 GB root, 100%
used — `worktrees/` alone holds 24 GB across eleven stale lane
worktrees from prior sessions, `build/` 3.9 GB, `reports/` 931 MB). The
partial branch (`lane/b102altctl`, created but pointing at master, no
divergence) was left over from the failed attempt; no worktree directory
survived (`git worktree prune` found nothing to prune — the failed
checkout rolled back its own directory).

Recovery used to STAY inside the mandate (touch only my own worktree; no
cleanup of other lanes' worktrees, which is the manager's call, not a
read lane's): `git worktree add --no-checkout worktrees/b102altctl
lane/b102altctl`, then `git sparse-checkout init --cone` +
`git sparse-checkout set docs` before the first `git checkout` — the
worktree materializes ONLY `docs/` (~10 MB) plus the repo-root files cone
mode always includes, never `store/`/`build/`/`bench/`/`reports/`/
`testees/`. Every read this lane needed from those directories (report
TSVs, `bench/utf8`/`bench/altwide` sources, two individual
`store/records/*.jsonl` files) was done against the MAIN TREE
(`/home/duxevents/pcrec-bench`, read-only, never written), which already
has them checked out; only my own deliverables (the ledger, its
extract script/archive, this report, the `docs/dev/ledgers/CLAUDE.md`
pointer) are written inside the sparse worktree. The extract script
documents this in its own header and reads `PCRECBENCH_ROOT` (default
the main tree) so it is reproducible from either location.

**Flag for the manager:** `df -h /` is at 100% used, 920 MB free, as of
this lane's start. `worktrees/b101pred`, `b101read`, `b101repin`,
`b74repin`, `b75kb27`, `b95read`, `b97r6`, `b97read`, `b98kb29`,
`b98rider`, `b99som` are still present at 1.5-2.3 GB each (24 GB total);
several of their branches (`b74repin`, `b75kb27`, `b95read`, `b97r6`,
`b101read`, `b101repin`) already show `+` (merged into master per
`git branch -a --merged master`), which usually means the lane's work is
done and the worktree could be removed (`git worktree remove`) to free
space — a call for the manager, not this read lane, since it touches
other lanes' directories.

## Deliverables (all committed on `lane/b102altctl`)

- `docs/dev/ledgers/2026-09-26-utf8-0.1-alt-cyr-64-control-read.md` — the
  ledger: method stated first, §2/§3 the compile axis (altwide already
  brackets it; no Cyrillic compile penalty found), §4/§5 the match axis
  (altwide cannot answer it, structurally — no non-ASCII byte anywhere in
  its corpus, and its engineered hit densities are 5.8× sparser than
  alt-cyr-64's own natural density), §6 the recommendation (no new
  pattern for the compile axis; an `alt-asc-64` match-axis control, if
  chartered, belongs in `bench/utf8@0.2` and needs a new natural-density
  subject, not a drop-in pattern), §7 what was NOT read, §8 the
  charter-vs-committed checklist.
- `docs/dev/ledgers/CLAUDE.md` — one pointer row appended for the new
  ledger (never edited any existing row).
- `docs/dev/measurements/2026-09-26-alt-cyr-64-vs-altwide-w64-extract.py`
  + `…-extract.txt` — the reproducing script (source header, committed-
  file sources named) and its verbatim archived output; every number in
  the ledger cites one of this file's six sections.
- This report.

## Validation

**COMPLETE.** Every number in the ledger was produced by the committed
extract script and cross-checked by hand while writing it (the abi
numbers against `CLAUDE.md`'s own pin history — caught and corrected an
initial abi-29 mislabel for `25b1984f`, which is actually abi 27; the
script's printed table was re-verified against the corrected labels
before archiving). No OWED items: the brief's three numbered asks
(compile axis, match axis, recommendation) are each a ledger section
with cited numbers, and "what was considered and not done" (trie-node
derivation for `alt-cyr-64`, an abi-27-vs-33 A/B rebuild for the
`dfa_scan_edge` difference, re2/onig/vectorscan compile comparisons) is
named in the ledger's own §5.

No re-pin, no bench change, no code change — this is a read.
