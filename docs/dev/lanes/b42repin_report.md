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

## `make check`: three rounds to green, both triage classes closed

**Round 1** (log `make_check.log`): rc=2. `check-harness` CRASHED inside
`check_mechanism_stamps` before printing any summary — an uncaught
`AdapterError` on pcrec's `size-cap-retry` witness ("engine 'dfa', no VM
prefilter... match_api.md 6.3's table says vm/hybrid/count-collapsed").
Fixed (HALF 1's own commits `5f1dc55`.."3c98a22"): §6.3's table CHANGED
at cd371441 ([K53-SELRETRY], 2026-09-10, read at the pin, read-only) —
a SECOND rung now reaches `size-cap-retry`, on a DFA artifact whose
optional anchored machine was dropped to fit an emitted-size cap
(`RX_DFA_MATCH "search-filter"`, no VM prefilter), mutually exclusive by
engine with the pre-existing VM-hybrid rung. `_check_agreement` fixed as
a two-armed OR, citing the updated table verbatim. Also fixed CLASS 1
(the emit_bytes deltas, see below) on the 8 rows this round surfaced.

**Round 2** (log `make_check2.log`): rc=2, 328 PASS / 17 FAIL — the same
two failure classes, on rows the first pass's fix didn't reach:

- **CLASS 1, extended (commit `19927bc`)**: 15 more emit_bytes
  assertions (9 altwide ledger rows, 3 bounded ledger rows, 3
  `check_deny_flag_controls` entries that duplicate numbers the ledger
  rows already carry, independently). Every row decomposes exactly into
  the SAME two named constants added in round 1
  (`B42_STARTPOS_GUARD_LINES` = 161, `B42_PORTFIX_SEMI_PER_MACHINE` = 2)
  — verified by compiling the real witness pattern at both pins with a
  MATCHING output basename and diffing comment-excluded `emit_size()`
  directly, never assumed: flat 161 on every non-hybrid VM artifact;
  +163/+165/+167 on DFA artifacts with 1/2/3 scan-edge-bearing machines
  (2 bytes each, one trailing `;` per machine's two labels); ONE
  exception measured directly rather than forced into the 2-per-machine
  shape — bounded `dig-upto-16`'s reverse-pass form has THREE machines
  but its scan carries no `scan_edge` label at all, only `scan_views`,
  so its delta is 161+3=164, not 161+6. All 18 affected values verified
  against `tools/selfcheck.py`'s own arithmetic before commit; zero
  residue.
- **CLASS 2 / GROUP B (commit `9922bbf`)**: real pin-behavior movement,
  not a book-keeping delta, and it points the WRONG WAY for CLASS 1's
  growth — `altwide w-384` under `pcrec-auto` now COMPILES (969,454 B)
  where d34c9131 refused it (1,432,392 B > the 1,000,000 total cap), and
  `pfx3-512` compiles at the DEFAULT cap where it used to be the [B31]
  cap-axis control's cheapest refusal. MEASURED the why before touching
  either check: two-pin recompile of `w-384`, matching basename, diffed.
  d34c9131's artifact carries BOTH `rx_forward_next_state[52056]` and
  `rx_anchored_next_state[41742]`; cd371441's carries ONLY the forward
  table, stamps `RX_ENGINE_SEL "size-cap-retry"` /
  `RX_DFA_MATCH "search-filter"`, and is 462,938 B smaller. This is
  pcrec **[K53-SELRETRY]** (charter `8e3a5485`, landed `6effd93a`
  "merge lane/utf8k53", 2026-09-10 — between d34c9131 and cd371441): the
  emitted-size-cap retry rung, previously VM/forced-island-only (the
  [B37] wall), now ALSO drops the DFA route's optional anchored
  match-here machine on a cap refusal. **pcrec's own commit message
  names this bench directly**: "the corpus population was the bench's
  altwide witnesses, not \p". Re-derived the DFA wall by a direct sweep
  of the width ladder (no rung between 512 and 1024 in the corpus):
  w-512 now compiles too (970,229 B, `size-cap-retry`); w-1024 still
  refuses (1,243,231 B — the drop is not always enough). **DFA wall:
  256<w≤384 → 512<w≤1024.** The VM wall (384<w≤512, [B37]'s island
  finding) is UNCHANGED — a different mechanism; both its arms (w-512
  forced-VM, the denied w-384 chain) still refuse exactly as before.
  `check_mechanism_stamps`' refusal-boundary arm re-derived to the new
  wall (asserting the POSITIVE evidence — w-512 auto compiles via
  `size-cap-retry` — alongside the negative one, w-1024 still refuses).
  The [B31] cap-axis control's auto arm moved from `pfx3-512` to
  `wb-512` (swept the ladder at cd371441 for the cheapest STILL-refusing
  pattern: 1,514,697 B, refuses even after the drop rung, ~1.6 s). Both
  re-derivations verified standalone before commit
  (`check_mechanism_stamps` 111/111, `check_deny_flag_controls` 11/11,
  `check_cap_axis` 13/13). **This finding belongs in the outbox** (O-28
  per the manager) as a positive [K53-SELRETRY] acceptance data point on
  this bench's own corpus, not a bug report.

**Round 3** (log `make_check3.log`, box quiet — load 0.69/0.54/0.40 at
launch): launched after both fixes; **OWED** at report-commit time — see
the follow-up message for the counts. All fixes for both classes are
committed; every standalone check that could be run without the ~20-min
full suite (`check_mechanism_stamps`, `check_deny_flag_controls`,
`check_cap_axis`, `check_kb17_find_all_advance`) is green.

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
| GATE: `make check` full, every count green | Round 3 **OWED** (running); rounds 1-2's failures both fixed and verified standalone — see the "three rounds to green" section above |
| Any red implicating pcrec: verbatim repro, no diagnosis | The abi surprise (HALF 1) is reported verbatim per BD2. The [K53-SELRETRY] wall movement is NOT a bug — it is a real, positive, pcrec-acknowledged improvement this bench's own corpus triggered; reported as a finding for the outbox (O-28), not a red |

## Commits (chronological)

1. `5f1dc55` — HALF 1 (1/2): re-pin registries, catalogue pin_order/version bump, sidecar regeneration
2. `7b49289` — HALF 2: KB-17 fix
3. `9bc966a` — HALF 1 (2/2): root CLAUDE.md pin reference
4. `93559b0` — HALF 1 (2/2b): testees/pcrec/CLAUDE.md list_schema.tsv + checklist
5. `e03f94d` — lane report (round 1's gate marked OWED)
6. `3c98a22` — round 1 fix: CLASS 1 (8 rows) + CLASS 2 (size-cap-retry two-armed check)
7. `19927bc` — round 2 fix: CLASS 1 extended (15 more rows)
8. `9922bbf` — round 2 fix: GROUP B ([K53-SELRETRY] wall movement, named and re-derived)
4. `93559b0` — HALF 1 (2/2b): testees/pcrec/CLAUDE.md list_schema.tsv + checklist
