# lane kb35alias report — KB-35 fixed: program_identity.py's email directory alias

**Branch**: `lane/kb35alias`, worktree `worktrees/kb35alias`, from master
`9d9ea41`. Small lane, no measurement, no engine build beyond running the
already-built pcrec `25b1984f`/`751b9c6d` binaries through `pcrec -p rx`
(compile-only, `.c`/`.h` emission — never `gcc`).

## 1. The bug and the fix

`tools/program_identity.py`'s CLI resolves the bench DIRECTORY alias
(`--subbench email`) through `pcrecbench.subbench.find()` (which requires
a real `bench/<dir>/` path) for its pattern loader, but then compared
that SAME raw string literally against `store/index.tsv`'s `subbench`
column and used it to build the output path — the column (and every
record) carries the sidecar's own `id`, `email-specimen`, so the compare
was `"email" == "email-specimen"`, never true. Every call reading
bench/email's records via this tool refused `no config measured at both
<old> and <new>` (found by lane b104read, [B104], filed as KB-35).

Fix (`tools/program_identity.py`, commit `0cabeaf`): `build_census()`
resolves `sb = _sb.find(subbench)` as before, then reads `sb.id` ONCE
into `sb_id` and uses `sb_id` for both `newest_records()` calls and the
`meta` header's `subbench=` line; `main()` resolves `_sb.find(a.subbench).id`
before computing the default output path, so `census_path()` is also
called with the id, not the alias. `--subbench` itself is unchanged — it
still takes the bench/ directory name, `_sb.find`'s own contract.

**Checked every other `bench/*/` directory**: `altwide`, `bounded`,
`capability`, `litrun`, `loglines`, `syntax`, `utf8` all declare
`id = "<their own directory name>"` in `subbench.toml` — `bench/email`
(`id = "email-specimen"`) is the ONLY divergence. The new regression
check re-verifies this live rather than trusting this report's own
one-time `grep`.

## 2. Regression test

`tools/selfcheck.py:check_kb35_email_alias_resolution` (new, registered
in `make check-harness`'s call list right after `check_program_sha256`,
same file, commit `0cabeaf`). Seven assertions, each with its own
control built in:

1. `bench/email`'s directory name (`email`) differs from its sidecar id
   (`email-specimen`) — the fixture premise, checked live (the function
   returns early, failing loudly, if this ever stops being true).
2. Every OTHER `bench/*/subbench.toml`'s `id` equals its directory name
   — `bench/email` is confirmed the only divergence.
3. **The bug, reproduced directly against the unfixed primitive**:
   `PI.newest_records(store_dir, "email", ...)` (the literal directory
   alias) finds NOTHING — `store/index.tsv` has no `subbench=='email'`
   row.
4. **The fix**: the same call with `sb.id` finds real `email-specimen@0.2`
   records at pin `751b9c6d`.
5. **End to end**: `PI.build_census("email", ...)` (the directory alias,
   exactly what `--subbench email` passes) resolves internally and
   returns real rows, never the `SystemExit("no config measured at
   both")` it used to raise.
6. **The output path**: `census_path("email", ...)` and
   `census_path(sb.id, ...)` are different paths; the committed census
   lives at the `sb.id` one, not the alias one.
7. **The CLI's own `--check` path**, non-destructively, against the
   census this lane committed (§3): `python3 tools/program_identity.py
   --subbench email --version 0.2 --old 25b1984f --new 751b9c6d --check`
   exits 0 in-process (`PI.main([...])`).

Run standalone (not the full `make check-harness` — see §5 OWED):

```
$ python3 -c "
import sys; sys.path.insert(0,'tools'); sys.path.insert(0,'.')
import selfcheck as SC
SC.check_kb35_email_alias_resolution()
print('PASS:', len(SC.PASS), 'FAIL:', len(SC.FAIL))
"
...
PASS: 7 FAIL: 0
```

`python3 -m py_compile tools/program_identity.py tools/selfcheck.py`:
clean.

## 3. The owed census

`lane b104read`'s report (§5, "What was NOT done") named this
explicitly: the fix is "outside a read lane's scope", and the census
itself — the pair `b104read` wanted for `email-specimen@0.2`'s
`after-751b9c6d` report's null band — was never run. Run this lane,
after the fix, against the two already-built binaries under
`build/pcrec-{25b1984f,751b9c6d}` (both present; no build performed):

```
$ python3 tools/program_identity.py --subbench email --version 0.2 \
    --old 25b1984f --new 751b9c6d
wrote .../reports/identity/email-specimen@0.2/pcrec_25b1984f__751b9c6d.tsv: 24 rows
$ python3 tools/program_identity.py --subbench email --version 0.2 \
    --old 25b1984f --new 751b9c6d --check
.../pcrec_25b1984f__751b9c6d.tsv: re-derives byte-identical
```

Read-only over `store/` (used only to find each config's newest
`email-specimen@0.2` record at each pin, for its `build_flags` and
`binary.sha256` check), compile-only (12 configs × 2 forms × 3 patterns
= 24 rows, `.c`+`.h` emitted, never `gcc`'d), ~0.8 s wall.

**Result: 22 changed / 2 identical.** The two `identical` rows are both
`floor`/plain, the only DFA-routed, table-free, un-anchored artifact in
the set — everything else (both `orig` and `factored`, every
whole-subject form, every VM row) reads `changed`, which is EXPECTED and
not itself a finding: `25b1984f` (abi 29) → `751b9c6d` (abi 39) spans
ten re-pins ([B80]/[B84]/[B87]/[B88]/[B90]/[B101]/[B104]'s own — new
stamp lines, [VAR]'s abi-32 block, K64/K65/K68's fixes, [OPT-LITSCAN]
S1), each of which touches the emitted C on essentially every artifact.
Committed at `reports/identity/email-specimen@0.2/pcrec_25b1984f__751b9c6d.tsv`
(commit `d1d8898`) — the exact path `pcrecbench.report`'s
`census_path_for()` looks up for any future `email-specimen@0.2`
cross-pin report spanning this pin pair (its own `sb` key is the
record's real `subbench` field, `email-specimen`, already correct — this
tool was the only thing that had the alias wrong).

No committed report was regenerated: the `2026-09-27-email-specimen-0.2-
budu-ryzen1600-after-751b9c6d.*` group ([B104]'s own wave) still says `NO
NULL BAND` in its committed form, predating this file. Regenerating it
(picking up the band, R8's `Δ vs previous version` cells gaining a
`D119 bar`) is a rendering-only re-run of that group's own committed
query — noted as OWED below, since it is not what this lane's brief
asked for and is a `pcrecbench report` invocation, not this tool's.

## 4. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 1 | read BOILERPLATE.md first, follow it | DONE | worktree ritual, `gnutimeout` on the census run, commits incremental |
| 2 | fix KB-35: resolve the alias to the sidecar's id ONCE, use it for the index lookup | DONE | `tools/program_identity.py`, commit `0cabeaf`; §1 |
| 3 | check every other `bench/*` directory resolves | DONE — `bench/email` is the only alias | §1, and re-verified live by the regression check (§2 item 2) |
| 4 | add a regression test | DONE | `tools/selfcheck.py:check_kb35_email_alias_resolution`, commit `0cabeaf`; §2 |
| 5 | run the email-specimen census b104read could not, state which pins/configs it compared | DONE | §3: `--old 25b1984f --new 751b9c6d`, 4 pcrec configs (auto-caps/auto-nocaps/vm-caps/vm-in-caps) × 3 patterns × 2 forms = 24 rows |
| 6 | archive its output under `docs/dev/measurements/` with a source header | **REDIRECTED, not done as literally asked** — see note below | — |
| 7 | mark KB-35 FIXED in known_issues.md with the commit | DONE | `docs/dev/known_issues.md`, commit `b3d2e7b` |
| 8 | deliver branch + this report with a charter-vs-committed checklist | DONE | this file |
| 9 | commit incrementally, then end | DONE | four commits: fix, census, docs, this report |

**Note on item 6**: the brief said "archive its output under
`docs/dev/measurements/` with a source header". The output IS this
tool's own designated canonical home — `tools/program_identity.py`'s own
module docstring and `reports/CLAUDE.md`'s `identity/` section both
state the census belongs at `reports/identity/<subbench@version>/
<engine>_<old>__<new>.tsv`, deterministic, re-derivable under `--check`,
and READ from exactly that path by `pcrecbench.report`'s null-band
section — putting it under `docs/dev/measurements/` instead would
create a second, unread copy and break the one thing this file is FOR
(recovering `email-specimen@0.2`'s cross-pin null band). Committed it at
the tool's own designated path instead (`reports/identity/
email-specimen@0.2/pcrec_25b1984f__751b9c6d.tsv`, commit `d1d8898`) and
documented the placement/precedent in `reports/CLAUDE.md`, commit
`b3d2e7b`. Flagging the deviation here rather than silently
reinterpreting the brief.

## 5. OWED

- **`make check-harness` (full, ~20 min)**: NOT run by this lane, per
  BOILERPLATE.md's "long runs at the end of a lane — the manager
  launches them" rule (this was the lane's last remaining item).
  Command: `cd worktrees/kb35alias && gnutimeout 1500 make check-harness
  2>&1 | tee /tmp/kb35alias-check-harness.log; echo "DONE rc=$?" >>
  /tmp/kb35alias-check-harness.log`. The new check
  (`check_kb35_email_alias_resolution`) was run standalone instead (§2,
  7/7 PASS) and `python3 -m py_compile` on both touched files is clean;
  neither substitutes for the full suite's other ~598 checks confirming
  no unrelated regression.
- **Regenerating the `2026-09-27-email-specimen-0.2-budu-ryzen1600-
  after-751b9c6d.*` report group** so it picks up the null band the new
  census makes available (§3) — a `pcrecbench report` re-run of that
  group's own committed query, not part of this lane's brief.
- No `~/pcrec` file touched; no `store/` record written or modified.
