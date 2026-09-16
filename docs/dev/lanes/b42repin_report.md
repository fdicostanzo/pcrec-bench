# b42repin — [B42] restart step (4): re-pin testees to cd371441 + KB-17

Lane on `lane/b42repin`, worktree `worktrees/b42repin`. Two independent
halves, delivered as separate commits each.

## HALF 1 — re-pin the pcrec testees, d34c9131 (abi 23) → cd371441

### Registry delta enumeration

Archived at cd371441 (`testees/pcrec/pin.sh cd371441`; the binary was
already built at `build/pcrec-cd371441/build/pcrec`), diffed body-for-body
against the committed d34c9131 copies:

| registry | d34c9131 | cd371441 | delta |
|---|---|---|---|
| `--list-axes` | 76 rows / 26 axes | 78 rows / 27 axes | +1 axis, `startpos-guard` (2 candidate rows: `guarded`/`permissive`) |
| `--list-definitions` | 50 rows | 50 rows | byte-identical |
| `--list-limits` | 56 rows | 57 rows | +1 row, `PCREC_STARTPOS_GUARD_TEXT_MAX` (1024 B, identifier cap) |
| `--list-schema` | (did not exist) | 70 rows, 2 sections | archived for the FIRST TIME (the seventh registry surface; the manager's decision per the brief) |

`--list-syntax` against the bench/syntax seed (`list_syntax_9a1583ba.tsv`):
138 rows both sides, delta confined to **two rows' `built` column**
(`\p{L}`/`\P{L}`, unicode-props: `unbuilt` → `built`). Per the brief, NOT
re-seeded — `kind`/`syntax`/`status`/`family` (the only machine-read
columns) are unmoved, so `make check` stays green on the un-re-seeded
file. **Reported here for a ruling**, not acted on further.

### STOP-AND-REPORT: the abi did NOT stay at 23

Inbox I-68 stated this re-pin's abi as "23 UNCHANGED." **Measured at the
build, it is not**: a plain witness (`abc`, byte encoding) stamps
`.abi = 25` at cd371441 against `.abi = 23` at d34c9131 — two real steps,
not zero. Read verbatim, read-only, from pcrec's own git history (BD2 —
no diagnosis attempted):

- abi 23→24: `5ce02f81 WIP k50bnd: abi 23 -> 24 + the spec hunks (D80) +
  the RX_STARTPOS_GUARD stamp` — [K50-NULLGATE], the caller-startpos
  boundary guard (`RX_STARTPOS_GUARD` + the new error code
  `PCREC_ERR_STARTPOS` = -7). This is the one axis/limit delta the two
  registries above show.
- abi 24→25: `e1bf0025 [PORTFIX] abi 24 -> 25 (D76): the
  clang-compatibility label fix's abi ritual` (`05c27b43 [PORTFIX] fix:
  gcc-16-vs-clang21 label-then-declaration in the DFA scan-edge
  emission`) — a portability fix, no new stamp, no new field.

**Why this does not block the re-pin.** `struct rx_info` is
byte-identical between the two pins (diffed the generated `.h` files
field for field — no member added, order unchanged), so this project's
own floor rule ("the shim floor rises iff a FIELD is added to what it
reads") holds regardless of the abi NUMBER's movement:
`PB_SHIM_MIN_ABI` stays 16. `make check` (below) is the empirical proof
that nothing the shim reads actually broke.

**Flagged for the manager's outbox**: I-68's "23 UNCHANGED" claim should
be corrected against this evidence.

### Pin update and testee_id verification

`testees/pcrec/configs.toml`'s `pin = "cd371441"`. Verified directly
(not assumed) by calling the adapter's `describe()` + `schema/validate.
derive_testee_id` for three representative configs:

    pcrec-auto          -> pcrec_cd371441_auto-caps-simdna
    pcrec-vm-noclsfold  -> pcrec_cd371441_vm-caps-simdna_noclsfold
    pcrec-auto-bigcap   -> pcrec_cd371441_auto-caps-simdna_emitcap-8388608-codecap-8388608

`engine_commit` reads the full `cd3714410cab2c0cce74dfa815fba630e0564db5`
on every config. All sixteen pinned configs derive by the same rule;
these three exercise the plain, deny-flag and cap-axis composition
branches.

`catalogue/rules.toml`'s `[[pin_order]]` gains `cd371441`;
`catalogue_version` 1.1 → 1.2 (MINOR, per its own versioning rule — a
`[[pin_order]]` append). This bump changes the rendered
`catalogue: N.N` stamp line in every committed sidecar, so the three
existing `reports/*.interpretation.md` files were regenerated
(`python3 -m pcrecbench interpret ... --render --out ...`, the
`/pcrec-bench-interpret` skill's exact command) and each verified
DETERMINISTIC (re-rendered to stdout, byte-diffed against the committed
file) before commit. Only the version-stamp line moved in any of the
three; no fact changed.

### Documentation

`testees/pcrec/CLAUDE.md`: added the `list_schema.tsv` table row,
extended the RE-PIN CHECKLIST to name it and the `--list-syntax`-vs-seed
step (with this re-pin's own outcome as the worked example). Root
`CLAUDE.md`'s testees bullet: pin marker updated to
`cd371441, abi 25`, `list_schema.tsv` added to the archived-file list,
the `[B39]` historical parenthetical about the d34c9131 re-pin kept
verbatim (not rewritten) with the new material appended ahead of it.

## HALF 2 — KB-17 fix: the find-all advance rule

Adopted pcrec `docs/spec/match_api.md` §3.1's find-all loop **by
reference** in the three places that carried the old rule
(`pos = max(end, pos+1)`, which advances off the previous SCAN position
and double-counts an empty match found ahead of it):

- `testees/pcre2/driver.c` (was line 338)
- `testees/pcrec/driver.c` (was line 728)
- `pcrecbench/oracle_pcre2.py`'s `_find_all_impl`

New rule: advance to the match END when non-empty, else one past the
match's own reported **START** (§3.1.1's `next_pos` residual, which is
`start + 1` under the byte encoding — this bench compiles no `utf8`
artifact anywhere, confirmed by grep). Also corrected the three prose
restatements of the old rule that were not code (`pcrecbench/
adapters.py`'s driver-protocol docstring, `pcrecbench/expectations.py`,
`bench/email/gen_expectations.py`) to cite §3.1 instead.

### Expectation re-derivation — ZERO movers

Every set's subject trees were regenerated (gitignored;
`gen_subjects.py` + `gen_throughput_subjects.py`, all five sets
byte-identical to their committed manifests) and every set's
`expectations.tsv` re-derived under its own `gen_expectations.py
--check`:

| set | rows re-derived | result |
|---|---|---|
| email | 501 | byte-identical |
| loglines | 1,364 | byte-identical |
| bounded | 4,300 | byte-identical |
| altwide | 2,772 | byte-identical |
| syntax | 8,265 | byte-identical |

**ZERO committed expectation counts moved anywhere.** The control KB-17
named — bounded's 17 `{0,N}` min-length-0 patterns, whose empty matches
are always AT the scan position so old and new rules agree there by
construction — held exactly as predicted; nothing else moved either
(the KB-17 census's claim that no committed number was affected is
confirmed by re-measurement, not merely by the a-priori argument).

### The pinned harness check

`tools/selfcheck.py`'s new `check_kb17_find_all_advance` (wired into
`main()`, runs in `make check-harness`) pins the two corrected oracle
witnesses by value:

    (?=a)  over b"xax"  -> first (1, 1), count 1   (was 2)
    (?=a)  over b"aXa"  -> first (0, 0), count 2   (was 3)
    a*     over b"xax"  -> first (0, 0), count 4   (unchanged; the control)

plus a negative control that reproduces the RETIRED rule inline — a
second, independent implementation read off KB-17's own mechanism
paragraph, never by calling production code — and asserts it still
produces the OLD wrong counts (2, 3) on the two lookaround witnesses,
proving the fix changed a real number rather than being a no-op.
Verified standalone before the full gate: 4/4 PASS.

`docs/dev/known_issues.md` KB-17 updated to FIXED, with the commit's
evidence (the delta enumeration and the byte-identical re-derivation
counts) folded into the entry.

## Gate: `make check`

Launched in the background (`gnutimeout 3600 make check`, box quiet:
load average 0.27/0.62/0.43, 11 GiB free before the run) — **OWED**: the
run was in progress when this report was written. It will be reported,
with counts, in a follow-up message once the background task's
completion notification lands; the log is at
`/tmp/claude-1001/-home-duxevents-pcrec-bench/932894fa-f62e-4029-8fb0-f23809c3696f/scratchpad/repin/make_check.log`
(session scratchpad, not committed) and ends with a `DONE rc=<n>` line.

## Charter-vs-committed checklist

| brief item | status |
|---|---|
| HALF 1 (1) registry re-archive + diff, by name | DONE — table above |
| HALF 1 (1) `--list-schema` archived as new | DONE |
| HALF 1 (2) `--list-syntax` vs seed, report not re-seed | DONE — 2-row `built`-column delta reported |
| HALF 1 (3) pin update, testee_id derivation verified | DONE — three configs directly verified |
| HALF 1 (3) abi/floor assertions verified, not assumed | DONE — struct rx_info diffed field-for-field; abi surprise STOPPED AND REPORTED above, not worked around |
| HALF 1 (4) `[[pin_order]]` append | DONE — catalogue 1.1 → 1.2, three sidecars regenerated and determinism-checked |
| HALF 1 (5) CLAUDE.md pin references updated, historical narrative untouched | DONE |
| HALF 2 advance rule adopted in both drivers + `_find_all_impl` | DONE |
| HALF 2 §3.1 cited in the driver-protocol comment | DONE (`pcrecbench/adapters.py`) |
| HALF 2 every set's expectations re-derived under `--check` | DONE — 0 movers, table above |
| HALF 2 control: 17 bounded patterns unmoved | DONE — confirmed by re-measurement |
| HALF 2 oracle witnesses pinned by value + negative control | DONE — `check_kb17_find_all_advance`, 4/4 PASS standalone |
| HALF 2 KB-17 → FIXED | DONE |
| GATE: `make check` full, every count green | **OWED** — running in background at time of writing |
| Any red implicating pcrec: verbatim repro, no diagnosis | N/A this lane found none that blocked delivery; the abi surprise above is reported verbatim per BD2 |

## Commits (chronological)

1. `5f1dc55` — HALF 1 (1/2): re-pin registries, catalogue pin_order/version bump, sidecar regeneration
2. `7b49289` — HALF 2: KB-17 fix
3. `9bc966a` — HALF 1 (2/2): root CLAUDE.md pin reference
4. `93559b0` — HALF 1 (2/2b): testees/pcrec/CLAUDE.md list_schema.tsv + checklist
