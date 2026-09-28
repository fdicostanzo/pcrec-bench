# lane b108fix report — check-harness 576/2 -> full `make check` green

**Task**: fix the two `check-harness` failures the a32bc86e re-pin's full
`make check` found (`/var/tmp/b108scratch/b108_make_check.log`), resolve
the `check_testee_globs` question on the three new litrun-a32bc86e
predictions files, regenerate the catalogue 3.11 -> 3.12 sidecars, run
the full `make check` and report.

**Branch**: `lane/b108set` (worktree `worktrees/b108set`), commits
`34c76ea` (re-archive `list_limits.tsv`, re-aim the cap-axis control past
S2a), `080ba82` (regenerate all 50 report sidecars for the catalogue
3.11 -> 3.12 bump).

## 0. Findings the manager must read first

1. **`list_limits.tsv`'s failure was an archiving slip, not a live drift.**
   Lane b108repin's re-archive accidentally pasted pcrec's own registry
   preamble comment block (`# pcrec numeric-limits registry ...` through
   `# override: "flag" ...`) in TWICE (lines 17-31 duplicated verbatim as
   32-46 of the committed file), so `check_list_limits_registry`'s
   find-first-live-line anchor landed on the WRONG occurrence and diffed
   the header against itself. Re-derived directly from the pin binary
   (`build/pcrec-a32bc86e/build/pcrec --list-limits`) and reassembled as
   bench-header (lines 1-16, unchanged, already correct) + exactly one
   copy of the live output — 64 data rows, matching the header's own
   stated count. No limit VALUE was ever wrong; only the archive's own
   bytes were.
2. **The cap-axis control's `w-512` rung was retired by S2a, not by this
   lane's own change.** [OPT-LITSCAN] S2a (abi 40 -> 41) shrinks
   forced-VM alternation-island/chain code by collapsing per-branch
   literal runs to one memcmp, and moved the altwide VM refusal wall a
   SECOND time: [B37] held it at 384<w<=512; at a32bc86e it is
   1024<w<=2048 on both the island and the `-fno-alt-island` chain
   routes (the pre-existing `check_mechanism_stamps` altwide-refusal-
   boundary block already knew and asserted this — it passed unchanged
   in the original run). `check_cap_axis`'s OLDER [B31] six-arm control
   (`_CAP_PAIRS`) still pointed the VM arm at `w-512`, which now compiles
   under `pcrec-vm` at the default cap (456,072 code bytes < 500,000) and
   so proves nothing — exactly the premise check's own designed catch
   ("it compiled — pick a wider rung"). Re-aimed at `w-2048`: measured
   directly against the pin binary, `w-2048` refuses at 884,927 code
   bytes under the default cap (0.05 s) and compiles at 894,611 file
   bytes / 884,928 measured code bytes under the 8 MiB raise (0.06 s) —
   both of the control's premises. The auto arm's rung (`w-1024`) is
   untouched, since S2a is VM-only. History of the move documented in
   `tools/selfcheck.py`'s own comment above `_CAP_PAIRS`, the same
   convention every earlier move of this control used (`pfx3-512` ->
   `wb-512` -> `w-1024` -> `w-512`, now `w-2048`).
3. **`check_testee_globs` is NOT reachable by `docs/dev/predictions/
   {bounded-0.3,capability-0.1,loglines-0.1}-litrun-a32bc86e.tsv` inside
   `make check` today, and needs no fix.** It is called ONLY from
   `pcrecbench.interpret.interpret()` (the CLI's `interpret` /
   `--render` path), never from `check_interpret.py`'s section-1 sweep
   over every committed predictions file (that sweep calls
   `load_predictions(path)` alone — confirmed by reading both call
   sites, `pcrecbench/interpret.py:2836` vs
   `catalogue/check_interpret.py`'s `pred_dir` loop, and by directly
   loading all three files with `load_predictions`: 5/13/3 rows, all
   clean). `scripts/regen_sidecars.py` (this lane's own sidecar-refresh
   step) only re-renders EXISTING `reports/*.interpretation.md` sidecars
   against the predictions path recorded in each one's OWN stamp — no
   existing sidecar is stamped against a `litrun-a32bc86e.tsv` file
   (there is no report yet for the unmeasured a32bc86e window), so the
   regen never touches them either. This is exactly how the three prior
   `*-b104-751b9c6d.tsv` fresh-pin files avoided it too (they name the
   fresh pin's testee id as an exact literal, not a glob, and are first
   interpreted only after their window measures that pin — at which
   point the testee is no longer unmeasured). **No code change**;
   `bench/litrun`'s own `litrun-0.1-first.tsv` already documents the
   identical, correctly-vacuous case in `docs/dev/lanes/
   b108set_report.md`'s charter-vs-committed section.

## 1. Charter-vs-committed checklist

- **Fix `list_limits.tsv`** — DONE. Re-derived from the pin binary,
  committed at `34c76ea`; `check_list_limits_registry` verified
  standalone before the full run (64 rows, byte-identical below the
  source header).
- **Fix the cap-axis control (`check_cap_axis`)** — DONE. `_CAP_PAIRS`'s
  VM arm moved `w-512` -> `w-2048`, with the move's own history
  documented in the same comment block every prior move used; verified
  standalone (all six `check_cap_axis` arms PASS) before the full run.
- **Update comment/CLAUDE.md text naming the old rung** — CHECKED, none
  needed updating: every other mention of `w-512` in the tree is either
  the bench pattern's own name (`bench/altwide/`'s generator, NOTES.md,
  gen_subjects.py — unrelated to this check), or a DATED, historical
  narrative entry (root `CLAUDE.md`'s append-only `make check-harness`
  changelog at the [B31]/[B37] entries, `testees/pcrec/CLAUDE.md`'s
  own re-pin history) describing what the check verified AT THAT PIN —
  this project's convention is to never retroactively edit those
  (confirmed against a dozen precedents in the same files, e.g. the
  a7e0bdf/263b013/96e44c2 sections' own untouched "MEASURED at pin ..."
  language). Nothing currently claims, in the present tense, that the
  live check targets `w-512`.
- **Run the full `make check`, detached, wait on the marker** — DONE.
  `setsid /usr/bin/gnutimeout 5400 make check >
  /var/tmp/b108scratch/b108fix_make_check.log 2>&1 < /dev/null &
  disown`, polled via a bounded `until`-loop inside one `gnutimeout`'d
  bash call (auto-backgrounded by the harness past 120 s, notified on
  completion) — see §2 for the exact final numbers.
- **check-schema green, check-harness green, check-report green** —
  DONE, all three (§2).
- **Regenerate sidecars for the catalogue 3.11 -> 3.12 bump** — DONE.
  `scripts/regen_sidecars.py`, detached under `setsid` (a store-loading
  step, per the box's own rule): 50/50 regenerated cleanly, 0 failures;
  every diff a pure `catalogue: 3.11 -> 3.12` line pair (the stamp line
  and its matching prose sentence) — no rule moved in this bump, so no
  fact or verdict changed on any sidecar. Committed at `080ba82`.
- **Determine whether `check_testee_globs` is in `make check`'s path for
  the three new cross-set predictions files; if so, it must not leave
  master red** — DONE, see §0 item 3. It is NOT in the path; no fix was
  needed or made.
- **Commit incrementally** — DONE, two commits (§ header), each with its
  own targeted verification run before landing.
- **Deliver `docs/dev/lanes/b108fix_report.md`, then END** — this file.

## 2. Validation (the full `make check`, final numbers)

Log: `/var/tmp/b108scratch/b108fix_make_check.log`. `grep -n
"^check-.*:\|FAIL" `finds no `FAIL` anywhere in the log:

    check-schema: 6 example(s) accepted, 74 sabotage(s) rejected for the intended rule, 0 sabotage(s) WRONG
    check-harness: 592 check(s) passed, 0 FAILED
    check-report: OK
    check-interpret: 224 passed, 0 FAILED
    check-upstream: OK -- 13 finding(s), 2 thread(s), 0 issues

(`make`'s own exit code for the whole chain: 0 — not printed as a
separate line by this Makefile, confirmed by the log ending cleanly at
`check-upstream: OK` with no trailing `make: ***` error line, and by the
detached job's own process having exited by the time the poll loop's
`pgrep` test returned false.)

check-harness rose from 576 checks (2 failing) in the original
b108repin/b108set run to 592 (0 failing) here — the check-schema/
check-harness boundary and the harness's own smoke-fixture regeneration
(`gen.py: checked ... file(s)` lines) can shift the printed count run to
run by a handful of checks (every prior re-pin's report notes the same);
the two named failures are gone and nothing else moved.

Targeted pre-checks, run standalone before committing each fix (numbers
quoted in §0):

    python3 -c "import sys; sys.path.insert(0,'tools'); import selfcheck; selfcheck.check_list_limits_registry()"
    python3 -c "import sys; sys.path.insert(0,'tools'); import selfcheck; selfcheck.check_cap_axis()"
    make check-interpret        # 224 passed, 0 FAILED (after the sidecar regen)
    make check-schema           # 6/74/0
    make check-report           # OK (detached: ~2m30s wall, ~700 MB peak RSS -- test_kb16_query_never_opens_other_subbench_files loads the smallest real subbench through report.main())
    make check-upstream         # OK -- 13 finding(s), 2 thread(s), 0 issues

## 3. The `list_limits.tsv` fix, exactly

Before (committed, broken): lines 1-16 the bench's own source header
(correct, untouched), lines 17-31 pcrec's own registry preamble
(`# pcrec numeric-limits registry ...` through the truncated
`# override: "flag" ...` line), lines 32-56 the SAME preamble AGAIN
verbatim, line 56 `#name value unit kind override anchor desc`, then 64
data rows — 120 lines total, with the accidental duplicate meaning
`check_list_limits_registry`'s `committed.find(first_live)` search
matched the header's OWN first occurrence rather than the true start of
the live-comparable body.

After (this lane): bench header (16 lines, unchanged) + exactly one copy
of `build/pcrec-a32bc86e/build/pcrec --list-limits`'s live stdout (89
lines: 24 comment lines + the column header + 64 data rows) — 105 lines
total. Verified two ways: `check_list_limits_registry()` standalone
(PASS, byte-identical below the source header) and a direct python
re-derivation of the check's own `committed.find(first_live)` /
`body == live` logic before writing the file.

## 4. The cap-axis control move, exactly

    _CAP_PAIRS = (("pcrec-vm-bigcap", "pcrec-vm", "w-2048"),      # was "w-512"
                  ("pcrec-auto-bigcap", "pcrec-auto", "w-1024"))  # unchanged

Measured directly against `build/pcrec-a32bc86e/build/pcrec` (not
inferred from the check's own PASS/FAIL, to have an independent number):

| rung | route | default cap | 8 MiB raise |
|---|---|---|---|
| `w-512` (retired) | `pcrec-vm` | **compiles**, 456,072 code bytes (no longer separates the two configs) | n/a |
| `w-2048` (new) | `pcrec-vm` | refuses: "pattern too large: 884927 bytes of emitted code (limit 500000)", 0.048 s | compiles: 894,611 file bytes / 884,928 measured code bytes, 0.058 s |

All six `check_cap_axis` arms PASS with the new rung (the nine pre-[B31]
configs untouched, every committed record's testee re-derives, the
below-default refusal, the cc x caps composition, `pcrecbench testees`
lists both bigcap configs, and the refuse/compile/oracle-agreement pair
itself).

## 5. OWED

None. Every item in the brief is either DONE (§1) or resolved as
requiring no change (§0 item 3, `check_testee_globs`). The measurement
window for I-113 §7.1/§7.2 (the factoring x lit-run 2x2, the L-sweep)
remains the manager's, per [B108]'s own OWED list — untouched by this
lane, which is a pure `make check` repair.

## Files

- `testees/pcrec/list_limits.tsv` — re-archived (duplicate preamble
  removed, 120 -> 105 lines, 64 data rows unchanged in content).
- `tools/selfcheck.py` — `_CAP_PAIRS`'s VM arm `w-512` -> `w-2048`, with
  the move's history appended to the existing comment block.
- `reports/*.interpretation.md` (50 files) — regenerated for catalogue
  3.11 -> 3.12 (pure version-line diffs, no fact or verdict moved).
