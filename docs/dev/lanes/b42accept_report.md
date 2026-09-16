# [B42] restart step (1) — the 41-check acceptance run (lane `b42accept`)

Branch `lane/b42accept`, from `master` tip `7bd3f7d`. Brief: run
`docs/design/rxt_needs_v1.md` §3's 41-check acceptance checklist against
pcrec's delivered pin **cd371441** (abi 23), as the authoritative pass of
record (pcrecdev1's own dry run, `~/pcrec/docs/dev/lanes/w235_report.md`
§3, was 25/41 runnable / 20 green / 3 documented reds).

**STATUS: DELIVERED, COMPLETE.**

## What this lane did

Read, in order: `docs/design/rxt_needs_v1.md` §3 in full (the 41-check
checklist, its notation and negative-arm rule); inbox items I-67, I-68,
I-69 (`docs/dev/inbox_from_pcrec.md`); the authoritative correction list
at `~/pcrec/docs/design/dd13_format/format_design.md` §9 at the pin
(read-only, `git -C ~/pcrec show cd371441:...`); pcrecdev1's own dry-run
verdict table (`~/pcrec/docs/dev/lanes/w235_report.md` §3); the spec of
record at the pin (`~/pcrec/docs/spec/rxt_format.md`, `cli.md`); and the
20-probe BEFORE (`docs/dev/measurements/probe_rxt_format.py` +
`2026-09-12-rxt-format-probes-d34c9131.txt`).

Then, for every one of the 41 checks, constructed a real `.rxt` fixture
(or reused the archived probe fixture where the check says "existing"),
ran it against the pinned binary
(`build/pcrec-cd371441/build/pcrec`, built and delivered by pcrecdev1
before this lane started), and recorded the verbatim command and output.
Three checks needed more than `--list-source`:

- **B7** (`@file:`'s bytes reach the matcher raw) needed an actual
  running matcher, not just a parse. pcrec's own harness
  (`~/pcrec/tests/harness/run.sh`) is the intended reader, but this
  project may only READ `~/pcrec`, never build inside it (BD2). Wrote a
  from-scratch 20-line C driver (`fixtures/b7_driver.c`) against the
  generated matcher's own `rx_search` C API, built entirely under this
  project's own scratch directory. Result: `.*` over a 3-byte
  `\x00\xff\x41` file reports `start=0 end=3` — the NUL and the high
  byte both reached the engine, argv could never have carried either.
- **C8/C9** (the `@file:` sha256 mismatch/match refusal) is checked by
  the READER, not by `--list-source` (confirmed in the spec: "pcrec
  checks neither the hash nor the 64-digit syntax"). Invoked
  `~/pcrec/tests/harness/run.sh` directly — READ-ONLY (the script
  itself, unmodified) — pointed at this lane's own fixture files, with
  `TMPDIR` redirected into this project's own scratch directory so its
  `mktemp -d` work directory never touches `~/pcrec`'s tree. Verified
  `git -C ~/pcrec status --porcelain` stayed clean after every
  invocation.
- **G2** (the five committed exports round-trip) was run directly
  against the delivered pin's binary via `tools/export_rxt.py --verify
  $P`, NOT through the currently-pinned testee (`testees/pcrec/
  configs.toml` still points at d34c9131 — re-pinning that is a
  separate, later restart step, out of this brief's scope). 185/185
  patterns (3+11+43+33+95 across email/loglines/bounded/altwide/syntax)
  round-tripped.

G3 (re-running the thirteen MEASURED facts and diffing against the
archive) surfaced five real diffs beyond the three the checklist
predicted (M1, M5, M10a/c): M7/M8's diagnostics gained a `[class]`
prefix (additive, the new §2.25.5 taxonomy), every row gained three
trailing empty columns (`tags`/`oracle`/`esc`, additive per D5's own
precision), case lines are now reported at all (`#section cases`,
additive per "THE W23 PRODUCTIONS ARE NOW REPORTED"), and two probes
(M10b's `variant`, M10d's `include`) now fail for a DIFFERENT reason
than "not in this build" — because the archived probe script's own
fixtures were written against an early one-line sketch of `variant`
and never created the fragment file `include` references, both stale
against the grammar the delivery actually finalized (a sub-block for
`variant`, real path resolution for `include`). Every hunk is
classified in the archive; **none is unexplained**, and none implicates
the delivered pin.

## Result

**33 PASS / 0 FAIL / 1 DISSOLVED-but-verified-true (B6) / 8
NOT-RUNNABLE**, out of 41. Full per-check verdicts, evidence citations
and corrections-applied are the verdict table atop
`docs/dev/measurements/2026-09-16-b42-acceptance-41-cd371441.txt`.

**The eight NOT-RUNNABLE checks, and why**, so the next restart step
knows exactly what unblocks them:

- **E1, E2, E3, E6, E7** — need a real `bench/capability@0.1` set and an
  `.rxt` loader in `pcrecbench/subbench.py`. Confirmed by grep (D2):
  `pcrecbench/` has ZERO `.rxt`-reading code today. This is Tier 1 of
  the restart's NEXT step (building the set), explicitly scheduled
  AFTER this checklist by `rxt_needs_v1.md` §4 and I-69's own work
  order ("run the checklist … THEN build the set"). Not a gap in this
  lane's work — the correct sequencing.
- **F3, F4** — same reason: no `.rxt`-sourced set file exists yet to
  plant a build directive into or review. The underlying guard
  (`tools/export_rxt.py` rule 5, "NO config/flags/engine/budget/
  encoding lines") was confirmed present by code read and will gate the
  set once it exists.
- **G1** — the repository mandate (BD2) forbids running pcrec's own
  `make test` or building anything in `~/pcrec`'s tree from here.
  pcrec's own I-68 report already states this battery green
  (strict/axes/san/lint rc=0, mech 256/0 anomalies); taken as the
  delivering party's evidence, not independently re-verified, per the
  mandate.

**Findings worth flagging up, not down (no diagnosis attempted, per the
brief's discipline):**

1. **F2's NEW finding from pcrecdev1's own dry run (a silent engine
   selection: CLI `--engine=dfa` silently overridden by a file's
   `engine vm`) is CONFIRMED FIXED at this pin.** Frank's 2026-09-15
   ruling (I-68 item 1: the CLI wins, with a non-fatal stderr
   diagnostic naming both sources) is live: `pcrec --source f2.rxt -o
   out --engine=dfa` against a file whose target config declares
   `engine vm` now prints `pcrec: f2.rxt:4: target 'wild1': CLI
   --engine=dfa and this file's \`engine vm\` disagree; using the
   CLI's explicit choice` and exits 0, with the DFA artifact actually
   built. This closes the one red the dry run found that wasn't already
   a documented, expected cause.
2. **B3 and C10 are both live exactly as this project asked
   (rxt_needs_v1.md P-Q7, P-Q9).** A NUL in a `pattern` line is now
   refused BY NAME (`[value-shape] embedded NUL byte in .rxt source
   file`) instead of silently truncating; a second `description` line
   is refused (`a pattern block has one 'description'`) instead of
   silently last-winning. Both were STEP 0, ahead of the whole W23
   wave, per I-68 item 2.

Nothing in this run implicates pcrec's delivery as broken; the two
staleness findings in G3 (M10b, M10d) are this project's own archived
probe script being written against an earlier design sketch, not a
pcrec defect, and are noted for a future probe-script refresh rather
than filed to the outbox.

## Deliverables — charter vs. committed

1. `docs/dev/measurements/2026-09-16-b42-acceptance-41-cd371441.txt` —
   **COMMITTED.** D35-style: source header, the 41-row verdict table,
   every check's verbatim command+output.
2. `docs/dev/measurements/accept41_cd371441/run.sh` +
   `fixtures/` — **COMMITTED.** The reproducing script and every `.rxt`
   fixture (plus `b7_driver.c` and the two subject binaries `c89_subj.bin`,
   `a1_subj.bin`).
3. The verdict table — **COMMITTED**, atop the archive file (deliverable
   1), not a separate file.
4. `docs/dev/measurements/CLAUDE.md` — **COMMITTED**, updated for the
   new directory and archive file.
5. This report — **COMMITTED.**

Nothing is OWED. The lane's task was the checklist run only; reviewing
the spec/design deltas more broadly and building the capability set are
the restart's next two steps (I-69's own work order), not this brief's
scope.

## For the manager

- Pin binary used throughout: `build/pcrec-cd371441/build/pcrec` (in the
  MAIN checkout — `build/` is not per-worktree; `run.sh` resolves it via
  the git common directory when re-run from a worktree).
- No write ever landed under `~/pcrec`; verified with `git -C ~/pcrec
  status --porcelain` after the C8/C9 `run.sh` invocations (the only
  ones that execute anything from that tree).
- Box was not gated and did not need to be: every command here is
  compile/parse-scale (`--list-source` at single-digit ms; two ~200ms
  gcc compiles for B7), never a measurement cell.
- Ready to merge. This branch is stopped (no background jobs, no
  running processes) and can be `TaskStop`'d freely before any
  measurement window.
