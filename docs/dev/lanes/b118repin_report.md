# lane b118repin report — RE-PIN to fc719ca4 (abi 41 -> 50)

**Task**: plan row [B118] / inbox I-122. Re-pin pcrec from `a32bc86e`
(abi 41) to `fc719ca4` (abi 50) — I-122 characterised this as ONE abi
step off a `d6cb0bb4` baseline, which was WRONG: our actual prior pin is
`a32bc86e`, so this lane absorbs the WHOLE 41 → 50 span (nine abi
steps). Report any roster cell that flips refused→compiled under D135
(I-122's own ask); characterise the other eight steps; full
re-pin ritual (registries, shim, stamps, checks, catalogue, CLAUDE.mds).

**Branch**: `lane/b118repin` (worktree `worktrees/b118repin`), commits
`58d68cb`/`cb17726`/`2e4b2be` (the two research forks, see §0), `a343712`
(re-derived all 39 STAMP_CASES/LEDGER_STAMP_CASES numbers by MEASURING,
two of them real findings not stale numbers — the ctx-node engine flip
and the FIND-TIE mover — documented in place), `fb7fad3` (CLAUDE.md
updates: root, testees/pcrec, pcrec_references.md, measurements/CLAUDE.md;
[B117] predictions re-pointed), `4c5a174` (the 3 real check-harness
failures the full run found, fixed — see §5), `bb3b6b4` (outbox O-78),
`75032f9` (plan.md row + dev_journal.md entry), plus this report's own
updates.

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

## 4. `check_mechanism_stamps`: every one of the 39 fails MEASURED, not
assumed flat — two are real findings

Ran standalone, then inside the full `make check-harness`: 129/129
after the fixes below. **37 of the 39 original fails were genuine
stamp-line-or-real-code SIZE moves**, individually re-measured against
the real `fc719ca4` binary and re-derived in the source (never patched
by blindly adding a flat constant): most are the three new flat terms
(`B118_UTF_VALID_DFA_TERM` 381 / `_VM_TERM` 431 / `_VM_HYBRID_TERM`
460), added as NAMED terms into the existing formulas (this file's own
per-re-pin convention); four (`K41` witness 2, the declined-island
chain, `winpath-near-miss`, `tag-pair-match`) carry REAL
[OPT-HYB-RESEED] program-byte growth (+139-140 B each) beyond the flat
term — the adaptive retry emitting genuine VM bytecode on these
specific backtracking programs; `nested-comment-rec` nets a real
SHRINK (-1032 B) not traced to one single abi step, documented as
measured with named candidates.

**Two were real findings, not drift, confirmed live and fixed in
place:**

1. **"alternation ISLAND on a VM hybrid under auto"** (witness
   `(?=x)(?:foo|bar|baz)`) now compiles as a plain DFA under `auto`:
   [UCP] U2's ctx-node fold (abi 45→46) folds this single-character
   lookahead into the DFA's own context machinery. Confirmed both
   directions against the real binary (`-fno-ctx-node` restores the
   exact a32bc86e reading, `vm_program_bytes` 2424 included) and it
   matches the dedicated `check_b118_ctxnode_engine_flip` control
   exactly. The row's own job (VM alternation islands under auto) needs
   a ctx-node-IMMUNE witness to keep testing it, so the pattern widens
   to `(?=foo)(?:foo|bar|baz)` (a three-byte literal lookahead body —
   ctx-node's predicate needs a set of SINGLE characters, and `{"foo"}`
   is one three-byte string, so the fold does not apply).
2. **`wild-secrets-github-pat`'s `dfa_prefilter`/`req_run`/`req_why`**
   all move under `auto`: [FIND-TIE] (abi 43→44) moves the necessary
   run's tied-byte scan pick from leftmost to rightmost
   (`pcrec_find_set_pick`'s own rule) — the scan index moves 3→7
   ("hub_pat_"'s own rightmost byte, `_`), shortening the DFA's bounded
   offset-set rung below the whole run and un-dominating it
   (`run-pinned-bounded`→`offset-set-bounded`, `req_why`
   `dominated`→`emitted`). No axis or deny flag exists for this rule;
   confirmed live against the real binary.

Also fixed [B39]'s cls-fold deny control: altwide `ci-256`'s denied arm
(26 classes, over [OPT-CLSPACK]'s packing threshold) now packs into
ONE shared atom table (`vm_cls_atoms 27`) instead of 26 per-class
`class_bitmap` declarations — "the classes came back" is now read as
bitmaps-OR-atoms, confirmed against both the small control (`(?i)abc`,
3 classes, under the threshold: unaffected) and the corpus witness.
Re-derived the I-43 island/chain ratio pair that moved outside
tolerance (w-256/pfx3-256: 1.3105/1.3206 → 1.3032/1.3035, a real
asymmetric effect on the `-fno-alt-island` chain arm; s-256 unchanged).

## 5. The full `make check-harness` run: 622/3, all three REAL findings,
fixed (never loosened)

The full run (20 min under `gnutimeout 2400`, quiet box) found three
failures beyond the 39 above — genuine findings the standalone
`check_mechanism_stamps` pass does not reach:

1. **`check_program_sha256`**'s "email `orig`: v1 changed / v2
   identical" pair verdict broke: v2 ALSO started reading "changed".
   Root cause, confirmed with a direct `normalize_one` diff against
   both binaries: [UTF-VALID] (abi 49→50) adds a real, unconditional
   FUNCTION, `<prefix>_valid_upto`, to every artifact — not a macro
   rule 5 already drops. Fixed by adding **rule 6** to
   `tools/program_identity.py`'s v2 normalization: the function's
   definition + header declaration are dropped together IFF the
   identifier appears nowhere else (the SAME "nothing reads it" test
   rule 3 already uses for the `rx_info` initializer) — confirmed true
   on every one of this project's pinned configs (none pass
   `-futf-check`). Re-verified: `na == nb` again on the email `orig`
   pair.
2. **`check_noreqbyte_testee`**'s `wild-secrets-github-pat` case had
   the PRE-[FIND-TIE] values hardcoded (a second, independent copy of
   the same fact §4 item 2 fixed on the LEDGER row) — updated to match.
3. **`check_b108_acceptance_mover`**: a REAL regression. I-113's own
   celebrated acceptance mover, `wild-datetime-datefinder-alternation`
   (forced `--engine=vm`), RE-REFUSES under the default 500,000-byte
   cap at fc719ca4 (compiled at a32bc86e, 482,765 B, `vm_lit_runs
   826`). Mechanism, confirmed by direct compile at three binaries
   (751b9c6d/a32bc86e/fc719ca4) plus a raised-cap arm: [OPT-LITSCAN] F5
   (abi 42→43) raises the VM literal-run floor 2→3, and this witness is
   dense with 2-byte literal runs (month/weekday abbreviations,
   timezone codes) that S2a used to collapse — `vm_lit_runs` falls
   826→155, `vm_program_bytes` grows +96,670 B (+19%, 508,413→605,083),
   pushing code bytes from 482,765 to 579,863. The check now asserts
   the re-refusal AND that a raised cap still compiles with
   `vm_lit_runs` measurably lower than at a32bc86e (the F5 signature),
   rather than being loosened. Filed as outbox O-78 (FYI only — F5's
   own ruling states the tradeoff is intentional).

All three fixed and individually re-verified green before the
re-derivation went into `STAMP_CASES`/etc.; the fixes are commit
`4c5a174`.

## 6. The [B118] roster-wide flip census (I-122's own ask)

`docs/dev/measurements/probe_b118_census.py` (committed by the earlier
forks, run by this lane): **Part A** (capability@0.1, 4 configs: 256
rows) — 170 identical / 79 changed / **5 refused-both** / **2
refusal-mover**; **Part B** (all six non-utf8 sets, `pcrec-auto`'s real
argv, plain form: 249 rows) — **0 flips**. The two refusal-movers are
BOTH `wild-datetime-datefinder-alternation` (vm-caps/vm-nocaps) — §5
item 3's own finding, confirmed independently by the census. D135's own
named witness, `(\p{Xwd})` under `-e utf8`, is not itself a bench
pattern (confirmed separately, testees/pcrec/CLAUDE.md §2). Archived:
`docs/dev/measurements/2026-09-30-b118-census.txt`.

## 7. Charter-vs-committed checklist

| charter item | status |
|---|---|
| Re-pin configs.toml, build fc719ca4 | **DONE** |
| Re-archive list_axes/definitions/limits/schema.tsv with deltas explained | **DONE** (§3 of the earlier draft; testees/pcrec/CLAUDE.md's new section has the full table) |
| Shim floor decision | **DONE**: stays 16 |
| New stamps asserted by value on witnesses with deny-flag controls | **DONE**: five dedicated `check_b118_*` functions (utf_check_stamp, ctxnode_engine_flip, clstree_stamps, hybreseed_stamp, findtie_k69_noop_on_bench), all green |
| Size books re-derived (measured, never assumed flat) | **DONE**: all 39 STAMP_CASES/LEDGER numbers re-measured (§4), two real findings documented in place, not patched over |
| `check_mechanism_stamps`/`check_deny_flag_controls` green | **DONE**: 129/129, 18/18 |
| Catalogue `[[pin_order]]` append | **DONE**: `fc719ca4` appended, version 3.13 |
| Compile-only census vs old pin (I-122's flip ask) | **DONE**: §6, archived |
| Report any roster cell that flips refused→compiled (D135, I-122's ask) | **DONE**: none in the bench roster under `pcrec-auto` (Part B, 0 flips); the two VM-forced flips are the acceptance-mover RE-refusal (§5.3/§6), the opposite direction from what I-122 asked about, reported anyway as the honest answer |
| Confirm default-config artifacts differ only as predicted for [UTF-VALID] | **DONE**: confirmed via `check_b118_utf_check_stamp` and the program_sha256 fix (§5.1) |
| Characterise the other abi steps (42-49) | **DONE**: §1's table, testees/pcrec/CLAUDE.md's new section |
| 3 real check-harness failures the full run found | **DONE**: all fixed, never loosened (§5) |
| `make check-harness` full re-run | **DONE**, 622/3→ (owed: the confirming re-run inside the chain below) |
| `make cc-gate-census` | **RUNNING** in the detached chain below |
| [B117] olevel census re-run at fc719ca4; predictions re-point | predictions file **DONE** (`docs/dev/predictions/capability-0.1-b117-olevel-fc719ca4.tsv`, the `-a32bc86e` original kept per convention); PIN label in the script updated; the actual re-run is **RUNNING** in the chain below |
| Full `make check` | **RUNNING** in the chain below (the final confirmation) |
| CLAUDE.md updates (root, testees/pcrec, pcrec_references.md, measurements/CLAUDE.md) | **DONE** |
| docs/dev/plan.md [B118] row / dev_journal.md entry | **DONE** |
| outbox O-78 (the F5/S2a tug-of-war FYI) | **DONE** |
| [B119]/[B120]/[B121] | **NOT STARTED** — explicitly queued AFTER [B117] per plan.md, out of this lane's scope |

## 8. OWED — the detached chain (DO-THEN-FINISH)

One detached chain, launched `setsid`'d and disowned (no harness
notification will arrive for it — the manager or a fresh agent must
poll the marker), covers the three remaining heavy steps in sequence
so they never contend with each other for CPU:

    /var/tmp/b118/chain.sh   (committed nowhere -- see its text below)
    log:    /var/tmp/b118/chain.log
    steps, in order:
      1. wait for the already-running `make cc-gate-census`
         (docs/dev/measurements/2026-09-30-cc-gate-census-fc719ca4.txt,
         2,034 cells -- bench x 3 pcrec engine modes x 2 forms x
         {gcc,clang}; ~79/2034 done when this chain was launched, so
         budget well over an hour)
      2. the [B117] olevel census re-run:
         `python3 docs/dev/measurements/probe_b117_olevel_census.py
         docs/dev/measurements/2026-09-30-b117-olevel-census-fc719ca4.txt`
         (gnutimeout 1200; the 2026-09-29 file at a32bc86e is KEPT,
         per this project's "a re-measurement is a new file" rule)
      3. the full `make check` (gnutimeout 5400)
    completion marker: the literal line "CHAIN DONE" at the end of
    /var/tmp/b118/chain.log; each step also prints its own
    "<NAME>_RC=<code>" line immediately before the next step starts,
    so a partial read of the log shows exactly how far it got.

Poll with `tail -f /var/tmp/b118/chain.log` or
`grep -E "_RC=|CHAIN (START|DONE)" /var/tmp/b118/chain.log`. If `make
check` is not 0, or either census script exits non-zero, the next
session should read the log's own tail before assuming anything about
what changed — cc-gate-census and the b117 census are both compile-only
and cannot themselves turn `make check` red, but a real, previously-
unseen finding on a 2,034-cell sweep this wide is plausible and should
be triaged the same way §5's three were: measure first, never loosen a
check to make it pass.

## 9. What's NOT owed

Nothing in [B119]/[B120]/[B121] was started (correctly queued AFTER
[B117] in plan.md); no store/reports write or timing happened in this
lane (the manager's window, Thursday 2026-10-01, as chartered).
