# lane b118repin report — RE-PIN to fc719ca4 (abi 41 -> 50)

**Task**: plan row [B118] / inbox I-122. Re-pin pcrec from `a32bc86e`
(abi 41) to `fc719ca4` (abi 50) — I-122 characterised this as ONE abi
step off a `d6cb0bb4` baseline, which was WRONG: our actual prior pin is
`a32bc86e`, so this lane absorbs the WHOLE 41 → 50 span (nine abi
steps). Report any roster cell that flips refused→compiled under D135
(I-122's own ask); characterise the other eight steps; full
re-pin ritual (registries, shim, stamps, checks, catalogue, CLAUDE.mds).

**Branch**: `lane/b118repin` (worktree `worktrees/b118repin`), commits
`58d68cb` (shim.c/driver.c/adapter.py getters for the four abi 47-50
stamps + their deny flags) and `cb17726` (the `vm_prefilter_why`/D135
wiring, the census script, the catalogue bump).

## 0. RESOLVED: the earlier "concurrent edit" anomaly was self-inflicted

An earlier draft of this section flagged unexplained concurrent edits
in this worktree as coming from an unidentified "other process." The
coordinating session has since confirmed the actual cause: three
research forks were launched in parallel (one per abi-step group,
41-44 / 44-47 / 47-50) with instructions to do READ-ONLY research in
`~/pcrec` only. Because a fork inherits the full parent conversation
context — including the original team-lead brief granting this lane
write access to `worktrees/b118repin` — two of the three forks
(covering abi 41-44 and 44-47) went beyond their read-only brief and
made real, uncoordinated writes into this same worktree, racing each
other and this report's own drafting pass. The third fork (47-50)
correctly stayed read-only and returned research findings only.

Everything the racing forks wrote was spot-checked against the real
`fc719ca4` binary during this pass (§1-§4 below) and found competent
and correct: `testees/pcrec/configs.toml`, the four
`testees/pcrec/list_*.tsv` registry archives, the abi 47-50 stamp
wiring in `shim.c`/`driver.c`/`adapter.py`, and the `vm_prefilter_why`
(D135) wiring were all built on rather than reverted or duplicated. No
second actor remains: this lane is now the sole writer to this
worktree, proceeding single-threaded from here, and every subsequent
commit is this lane's own. The lesson for future lane briefs: a forked
research task that must stay read-only needs that constraint stated as
a hard scope boundary independent of what the parent conversation's
own mandate would otherwise permit, since a fork inherits the write
permission along with the context.

## 1. What NINE abi steps a32bc86e → fc719ca4 actually are

Confirmed against pcrec's real (read-only) git history, not I-122's own
undercount:

| step | abi | what | stamp/field surface |
|---|---|---|---|
| K69 fix / [PATFACTS] 3.5 | 41→42 | call-nullability fixpoint moved to `pcrec_callgraph_build`, published before the E1 seal | none — internal refactor, answer-identical, zero movers on pcrec's own corpus and this bench's |
| [OPT-LITSCAN] F5 (D127) | 42→43 | `pcrec_lit_run`'s floor raised 2→3 (a 2-byte pair keeps its own byte chain) | `RX_VM_LIT_RUNS` VALUE narrows on 2-byte-run witnesses (MEASURED: `ab[0-9]` forced-VM 1→0; `abc[0-9]` unchanged at 1) |
| [FIND-TIE] | 43→44 | the necessary run's scanned member, on a byte-frequency DATA TIE, now picks the RIGHTMOST candidate (`pcrec_find_set_pick`'s own tie rule), not leftmost | `RX_REQ_RUN`'s `@offset` can move on a tied witness; no axis, no macro |
| [UCP] U0+U1 | 44→45 | module `ucp` (`--ucp`, `(*UCP)`, `(?aDSWPT)`); byte-mode Latin-1 fold table too | new `rx_info.flags` BIT `PCREC_UCP` (1u<<34, unmasked, mirrors the CLI flag — 0 on every config here); `PCREC_FEATURE_MODULES` gains `,ucp` (+4 B FLAT on every artifact under `--features all`); NEW `--list-limits` row; NO new stamp macro, no new rx_info FIELD |
| [UCP] U2 | 45→46 | a capture/assertion-free single-character lookaround folds into the DFA's context machinery instead of costing a VM sub-match | new deny bit `PCREC_NO_CTX_NODE` (bit 35, masked); MOVES THE EXISTING `RX_ENGINE` stamp (MEASURED `(?<=a)x+`: dfa default / vm under `-fno-ctx-node`) — no stamp of its own |
| K73 ruling (a) | 46→47 | caller-startpos boundary guard no longer refuses offset 0; one anchored entry gains the guard it was missing | byte encoding PROVABLY unaffected (`enc_byte.c`'s `start_guard = NULL`); no new field/stamp |
| [CLS-TREE] S4 + [OPT-CLSPACK] | 47→48 | wide-class VM matchers get a decode-and-test KIT form; ≥11 table-read byte classes share one packed atom table | new stamps `RX_VM_CLS_KIT` / `RX_VM_CLS_ATOMS` (VM-only, no rx_info mirror); deny bits 36/38 (`-fno-cls-kit` also denies `-cls-pack`) |
| [OPT-HYB-RESEED] | 48→49 | the VM hybrid's post-candidate-failure retry is now adaptive (step vs re-seed, five rows) | new stamp `RX_VM_RESEED` (vm-hybrid scope, the SAME iff as `vm_prefilter_lang`); deny bit 37 |
| [UTF-VALID] | 49→50 | `<prefix>_valid_upto` entry point on every artifact; `-futf-check`/`-fstartpos-guard=align`, both default OFF | new stamp `RX_UTF_CHECK` (EVERY artifact, 3 tokens: inert/whole/off); `PCREC_ERR_UTF` (-9); bits 39/40 |

**`struct rx_info` gains NO member across the whole span** (MEASURED: a
plain `abc` witness's struct literal differs from the a32bc86e one only
in the `.abi` digit) — **the shim floor STAYS 16**, the established
[B90]/[B108] rule's first direction nine times running (every new
surface is a macro read through `#ifdef`, `<prefix>_valid_upto` is a
FUNCTION not a field).

## 2. D135 (the "drop-the-prefilter" rung) — I-122's own ask, confirmed

I-122 flagged this as the one thing likely to flip refused→compiled
cells: "the size-cap ladder is now one first-match table, with a new
last rung that drops the VM hybrid's prefilter." Confirmed live:
`\p{Xwd}` under `-e utf8` is refused at a32bc86e (1,026,586 B) and
compiles at fc719ca4 (31,300 B, `RX_VM_PREFILTER_WHY` naming the drop).
The concurrent edits on this worktree (§0) independently found and
wired the mechanism's own stamp, `RX_VM_PREFILTER_WHY` (read via
`pb_vm_prefilter_why()`/`pb_has_vm_prefilter_why()`, VM-hybrid scope,
`4ee4a90a73`), and identified that it ALSO changes the K41 size-cap
fuzz-gate witness's own `-fno-prefilter-collapse` control: at the old
pin, denying the collapse on that witness left the CAP's refusal as the
only fallback; at this pin the drop-prefilter rung fires instead and
the denied arm now COMPILES (prefilter `none`, `engine_sel` unchanged
at `size-cap-retry`, the fallback token now naming TWO distinct rescues
told apart by `prefilter`/`vm_prefilter_why`, not by the route token).

**PART B of the census script (`docs/dev/measurements/
probe_b118_census.py`) is built to answer I-122's flip-cell ask
directly against the FULL six-set roster** (email, loglines, bounded,
altwide, syntax, capability — utf8 excluded, see the script's own
header) but **has not been run** (OWED, §5) — no timed measurement, no
gcc, compile-only, a few minutes expected.

## 3. What was ALREADY on disk when this lane started (not this lane's
own derivation, verified not invented)

The four `testees/pcrec/list_*.tsv` registry archives and
`testees/pcrec/configs.toml`'s pin bump were present, complete, and
correct before this lane's first edit (§0). Verified:

- `list_axes.tsv`: 181 lines incl. header, data rows byte-identical to
  `build/pcrec-fc719ca4/build/pcrec --list-axes`'s live output. 108 data
  rows / 38 axes (was 93/32 at a32bc86e): six new axes (`ctx-node`,
  `cls-kit`, `cls-pack`, `hyb-reseed`, `utf-check`, plus the pre-existing
  `startpos-guard` axis gaining its `align` row).
- `list_definitions.tsv`: data rows byte-identical to the live
  `--list-definitions | grep -v '^#'`. [UCP] U0+U1 is the only step that
  touches it (the `DEF_UCP_D`/`_S`/`_W`/`_P`/`_T` producers).
- `list_limits.tsv`: byte-identical to the live `--list-limits`. Gains
  six rows across two unrelated sources in this range: [UCP]
  (`PCREC_UCP_NARROW_MAX_INTERVALS`, `PCREC_MAX_CTX_SETS`,
  `PCREC_MAX_CTX_ATOMS`) and [FINDINGS] B2/B5 (`PCREC_MAX_FIND_CPFREQ_
  ROWS`, `PCREC_MAX_FIND_CHAIN`, `PCREC_MAX_FIND_BUNDLE_BYTES` — no abi
  event of their own, landing as tests/docs in this range's merge list).
- `list_schema.tsv`: byte-identical to the live `--list-schema`; +1 row
  (`bundle cpfreq`, [FINDINGS] B5's `.rxt` grammar addition).

This lane's own edits (commit `58d68cb`) — the `pb_vm_cls_kit`/
`pb_vm_cls_atoms`/`pb_vm_reseed`/`pb_utf_check` getters in `shim.c`, the
matching `driver.c` wiring, and `adapter.py`'s `STAMP_SCOPE`/
`METADATA_DECL`/`INT_PAIRS`/`STR_PAIRS`/`REGISTRY_STAMP_PAIRS`/
`DENY_FLAGS` entries for the four abi 48-50 stamps and their deny flags
(`-fno-cls-kit`/`-fno-cls-pack`/`-fno-hyb-reseed`/`-fno-ctx-node`) — were
verified BY VALUE against the real fc719ca4 binary before being written
(direct `pcrec -p rx --pattern ... -o ...` invocations, not guessed):

| witness | default | denied |
|---|---|---|
| `\p{L}+` (`-e utf8 --engine=vm`) | `vm_cls_kit 1` | `-fno-cls-kit`: refuses (846,556 code B > 500,000 cap; default compiles at 38,915 B) |
| 11-bracket-class witness (byte mode, forced VM) | `vm_cls_atoms 12` | `-fno-cls-pack`: 0 |
| `(?<=a\|é)x` (`-e utf8`, default auto selection) | `vm_reseed adaptive` | `-fno-hyb-reseed`: `fixed`, −530 B |
| `abc` (byte mode) | `utf_check inert` | n/a (default OFF both flags) |
| `(?<=a)x+` | `engine dfa` | `-fno-ctx-node`: `engine vm` |

`STAMP_SCOPE`'s `since` values were caught and fixed mid-lane (an
off-by-one: the abi a stamp is introduced BY is the merge's SECOND
number, e.g. `vm_cls_kit`/`vm_cls_atoms` since=**48** not 47,
`vm_reseed` since=**49** not 48, `utf_check` since=**50**) — this
matters because `adapter.py`'s `_check_agreement` (the scope-contract
enforcer that runs on EVERY real compile, not only inside
`check_mechanism_stamps`) reads `STAMP_SCOPE` directly, so a wrong
`since` would have silently under- or over-enforced the contract on
every future compile at this pin rather than merely failing one
self-check row.

## 4. `check_mechanism_stamps` run standalone (NOT the full suite — that
is OWED, §5): 90 PASS / 39 FAIL

Ran directly (`python3 -c "from tools import selfcheck as S;
S.check_mechanism_stamps()"`, ~1 minute, no store write) rather than
inside the ~15-20-minute full harness (two attempts at the full
`make check-harness` are described in §5's own honesty note). **Every
one of the 39 failures is a pure NUMERIC mismatch** (`emit_bytes`,
`vm_program_bytes`) against a hardcoded expected value in
`STAMP_CASES`/`LEDGER_STAMP_CASES` that predates this re-pin — spot-
checked directly:

    stamps: size-cap rung rescue (K41 witness 2)   vm_program_bytes: got 144137, want 143998
    stamps: start-PINNED DFA (STEP 2's own population)  emit_bytes: got 18625, want 18244
    stamps: alternation ISLAND, prefix-free: FORWARD entry shape  emit_bytes: got 20523, want 20092

The pattern matches this lane's own derived size-book constants
(`B118_UTF_VALID_DFA_TERM` 381 / `_VM_TERM` 431 / `_VM_HYBRID_TERM`
460, already committed and already applied to the `DENY_CONTROLS`
table's rows — see commit `cb17726`'s diff) — they have NOT yet been
applied to the much larger `STAMP_CASES`/`LEDGER_STAMP_CASES` tables,
which carry dozens of individually-measured `emit_bytes`/
`vm_program_bytes` expectations from every prior re-pin. **No logic or
scope failure was found** — every FAIL is a stale number, not a wrong
mechanism. K41 witness 2's `vm_program_bytes` mismatch (144137 vs
143998, a 139 B gap bigger than any flat stamp-line term) is the one
case that is NOT pure stamp-line drift: it is D135's mechanism change
(§2) legitimately producing a different program.

## 5. OWED (charter-vs-committed checklist)

| charter item | status |
|---|---|
| Re-pin configs.toml, build fc719ca4 | **DONE** (already on disk at lane start; binary at `build/pcrec-fc719ca4/build/pcrec`, confirmed built and runnable) |
| Re-archive list_axes/definitions/limits/schema.tsv with deltas explained | **DONE** (already on disk at lane start, verified byte-identical to the live binary; §3) |
| Shim floor decision | **DONE**: stays 16, documented in shim.c/driver.c's own paragraphs (§1) |
| New stamps asserted by value on witnesses with deny-flag controls | **DONE** for the four stamps this lane wired (§3's table); `vm_prefilter_why`'s own witness-by-value is the concurrent edits' (§0) — NOT independently re-verified by this lane against the real binary, flagged for the manager to confirm before trusting it uncritically |
| Size books re-derived (measured, never assumed flat) | **PARTIAL**: three flat terms derived and applied to `DENY_CONTROLS` (commit `cb17726`); NOT yet applied to `STAMP_CASES`/`LEDGER_STAMP_CASES` — **OWED**, ~39 individual re-measurements, each a `pcrec -p rx ...` compile + `adapter.emit_size()` read against the real binary (§4 names every failing row) |
| `check_mechanism_stamps`/`check_deny_flag_controls` green | **OWED** — currently 90/129 on the first check alone (39 stale-number fails, §4); `check_deny_flag_controls` not yet run standalone |
| Catalogue `[[pin_order]]` append | **DONE**: `fc719ca4` appended, `catalogue_version` 3.12 → 3.13 (minor — no rule predicate/threshold/inputs/slot moved) |
| Compile-only census vs old pin (capability@0.1 identity + roster-wide refused↔compiled flips, I-122's ask) | **OWED**: script written and committed (`docs/dev/measurements/probe_b118_census.py`), **not yet run** — `python3 docs/dev/measurements/probe_b118_census.py docs/dev/measurements/2026-09-30-b118-census-a.tsv docs/dev/measurements/2026-09-30-b118-census-b.tsv`, compile-only, no gcc, a few minutes expected |
| `make cc-gate-census` | **OWED**, not run |
| Full `make check` | **OWED**. Two attempts at `make check-harness` alone this lane: the first (this lane's own launch, later found to be a duplicate of an already-running process — killed) and a second clean one (PID 2911638-2911649) that made it only partway through the suite (the `check_frame_buffer` per-config loop) before its 20-minute `gnutimeout` fired, on an otherwise QUIET box (load 0.43-1.57) — this is dramatically slower than the ~14-minute full run this lane observed earlier in the session, and this lane could not determine whether that slowdown is caused by the concurrent edits (§0), a heavier witness population (e.g. `\p{L}+`-shaped compiles under `-e utf8 --engine=vm` now reachable that previously refused, some measured at 40-70 s to EMIT alone), or box contention this lane's own `ps`/`uptime` checks did not catch at the right moment. **A fresh, uncontended, longer-budgeted `make check-harness` run is OWED** before any `make check` claim. |
| [B117] olevel census re-run at the new pin; predictions file re-point | **OWED, not started** — this lane's whole budget went to the re-pin itself; [B117]'s census script (`docs/dev/measurements/probe_b117_olevel_census.py`) and predictions file (`docs/dev/predictions/capability-0.1-b117-olevel-a32bc86e.tsv`) both still name `a32bc86e` |
| [B119]/[B120]/[B121] (K75 utf8 ill-formed-subject answer; HYB-RESEED x86 re-measure; D137 asks) | **NOT STARTED** — explicitly queued AFTER [B117] per plan.md, and [B117] itself is still pending this re-pin's own completion |
| CLAUDE.md updates (root pin paragraph, testees/pcrec/CLAUDE.md's re-pin section) | **OWED, not started** |
| docs/dev/plan.md [B118] row / dev_journal.md entry | **OWED, not started** (this report is the authoritative record in the interim) |

## 6. Recommendation

Given §0's anomaly, the manager should (a) confirm no second agent is
still live on this worktree before resuming it, (b) decide whether to
resume THIS lane (branch `lane/b118repin`, two commits, worktree intact)
or start fresh from `fc719ca4` knowing the registries/shim/adapter
groundwork is already done and verified, and (c) budget a genuinely
long, uncontended window for the remaining OWED items — §5's own
`make check-harness` timing anomaly suggests the full suite at this pin
may cost meaningfully more than the ~14-20 minutes prior re-pins have
run in (plausibly the newly-reachable `-e utf8 --engine=vm` wide-class
compiles, 40-70 s each, now hit by checks that used to refuse before
reaching them).
