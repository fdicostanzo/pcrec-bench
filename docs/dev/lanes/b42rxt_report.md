# Lane b42rxt report — [B42] research note 3: `.rxt` as a bench set source

**Branch**: `lane/b42rxt`, off master `0d6e919`. **Commit**: `0966047`.
**Not merged** (per boilerplate: the manager merges).

## What the brief asked for, vs what is committed

The brief's six numbered questions, each with its section in
`docs/dev/research/2026-09-12-b42-rxt-as-source.md`:

1. **What `.rxt` carries/does not carry, and extension points** — §1.
   COMPLETE. Table of BUILT (W1) vs DESIGNED-not-built (W2/W3)
   productions, cited against the current pin's spec text
   (`~/pcrec/docs/spec/rxt_format.md:57-62`'s explicit by-name refusal
   list). Finding: no comment-convention extension point exists for
   anything missing — the only sanctioned path is a future wave's
   production.
2. **Source-of-truth options A/B/C with consequences** — §2. COMPLETE.
   Each option's effect on `subbench.py`, `make check` gates, the record
   schema (no change needed under any option — `canonical_sha256`/
   `canonical_text`/`source_ref` are already format-agnostic), and the
   per-engine variant question (stays in the sidecar under B until W3).
   Engine-neutrality analysed directly against R-BENCH-4/AR-6: the
   grammar's CASE vocabulary is not pcrec-shaped; `target`/`config` IS,
   and D93 makes that concrete (a `config` block in an authored source
   file would silently pin the testee matrix).
3. **What pcrec's own harnesses do that's reusable** — §3. COMPLETE.
   `--list-source` is the reusable HEAD seam (already used in the
   opposite direction by [B38]'s round-trip check); the BODY parser
   (`run.sh`/`driver.c`) is bash tied to pcrec's own build ABI, not
   reusable; `bench/syntax`'s own `--list-syntax` import is flagged as a
   closer, already-shipped precedent for "take structure from pcrec
   without becoming pcrec-shaped."
4. **Format asks pcrec would need to grant** — §4. COMPLETE, four
   candidate outbox items, none blocking (two are pre-named triggers in
   pcrec's own `format_design.md` Q5, i.e. pre-approved in principle).
5. **Risk list** — §5. COMPLETE: format churn, the free_text cap
   (not new), multi-line patterns (a genuine, previously-unstated gap —
   `.rxt`'s `pattern` line cannot express an embedded literal newline
   under ANY option, since the line is both unescaped and
   single-line), non-ASCII/binary (mostly fine, NUL-byte behavior in
   pcrec's own line reader NOT independently verified — flagged as an
   open item, not asserted either way), name/target collisions (handled
   precedent from [B38], flagged as more likely at capability-survey
   scale).
6. **Questions for Frank + recommendation** — §6. COMPLETE.
   Recommendation: **Option B** (hybrid), with the one-paragraph
   rationale the brief asked for, plus three sharper questions for
   Frank's ruling (does Option B satisfy charter item 4 as written; ask
   pcrec now or after the design note settles; does the survey set need
   to be `--source`-buildable from day one, re-opening [B29]'s
   compile-cost objection).

**Also delivered, not explicitly asked but load-bearing**: a direct
re-verification that [B29]'s own §3.3 finding (63 of 77 pattern names
illegal as a `.rxt` block name) is now STALE — the name grammar widened
between [B29]'s pin (abi 15) and the current one (abi 23), and a fresh
count against all five live sub-benches (185 patterns) found zero
illegal names, matching [B38]'s own already-committed number. This
matters because [B29] is still the only design note in this repo stating
the old count, and whoever writes [B42]'s design note needs the
correction, not a rediscovery.

## What was NOT done, and why

- **No independent verification of the NUL-byte behavior in pcrec's own
  `.rxt` line reader** (§5's risk list item). Out of the lane's time
  budget and out of scope for a bench-side research note (would require
  reading/testing pcrec's C parser, `src/parse/rxt_source.c`, which is
  legitimate to READ under the mandate but testing it would mean
  building pcrec — not authorized for a research lane). Named as an open
  item for whoever designs Option A/B in earnest, not silently dropped.
- **R-BENCH-8's import direction (pcrec `.rxt` → a bench sub-bench) was
  not independently checked** beyond citing [B29]'s own open Q4 on it.
  Out of this note's stated scope (source-of-truth for OUR sets, not
  import FROM pcrec's corpus).
- **No design proposal was written.** Per the brief and per [B42]'s
  charter phase ordering, this is research only; §6's recommendation is
  a recommendation, not a spec.

## Process note (self-reported, per the boilerplate's honesty rule)

The `Write` tool call for the research note landed the file in the MAIN
tree (`/home/duxevents/pcrec-bench/docs/dev/research/...`) instead of the
worktree, despite the worktree being the verified cwd for all prior Bash
calls. Caught immediately by `git status` in both trees before any
commit; fixed by moving the file into the worktree and re-checking both
trees clean before proceeding. No commit was ever made in the main tree,
and the main tree's `git status --short` is confirmed clean as of this
report. Recorded here because the boilerplate's scope mandate is exactly
about this failure mode, even though this instance was self-caught and
had no lasting effect.

## Validation

`docs/dev/research/2026-09-12-b42-rxt-as-source.md` committed at `0966047`
on `lane/b42rxt`. This lane made no code changes, so `make check` was not
run (nothing it gates changed) — COMPLETE for a research-only lane per
the delivery bar's "targeted validation" clause (there is no code to
validate; the validation IS the citation check performed inline while
writing, e.g. the `git log`/`merge-base` format-movement check in §0 and
the live re-run of the name-legality count in §1.2, both reproduced
above with their actual output).

Handback: complete, no OWED items. Ending per lifecycle rules.
