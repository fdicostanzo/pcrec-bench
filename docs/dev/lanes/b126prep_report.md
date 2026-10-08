# lane b126prep report -- RE-PIN to 255bcdd8 (abi 65 -> 68)

**Task**: plan row [B126], inbox I-134/I-135 and the manager's brief. Re-pin pcrec from
`60366d747` (abi 65) to `255bcdd8` (abi 68; pcrecdev1: contains 02db3811 and R4h 33186bc0,
docs-only after, compiler-identical). Writer lane; no store/ or timed run. One reports/ write:
the 75 sidecars' catalogue-version lines (same as b124prep's be078fa; check-interpret goes
red without it).

**Branch**: `lane/b126prep` in `worktrees/b126prep`, not merged. Build: `build/pcrec-255bcdd8/`
(`pin.sh 255bcdd8`). Scratch builds for the census layering: `/var/tmp/b126scratch/pcrec-{c9672bd2,
c4c37af8,02db3811}` (abi 66 / 67 / 68, deletable, ~120 MB each).

## 1. The three abi steps and the registry change: predicted vs measured

| step | pcrec's claim | MEASURED |
|---|---|---|
| 65->66 [ART-POSS-ARMS] | new stamp `RX_VM_POSS_ARMS` on VM artifacts; `-fno-poss-ctx-follow` selects the engine; three corpus movers; answers unchanged | stamp is an unsigned mask literal on every VM artifact (hybrids too, `0x0u` where no arm needed), absent on DFA. Values by witness: A0 `a+(?=b)b` (forced VM) 0x1; A1 `(\b\w+\b)` 0x2 (auto, a hybrid), `\B(x\|ab){1,2}\b` 0x2; B `\b(\w+)\s+\1\b` 0x4. Arms independent. Denial of A: strats POSSESSIVE->BACKTRACKING, frameless 1->0; **engine-selecting confirmed**: `(?:a\.)++\B` auto is DFA, `-fno-poss-ctx-follow` makes it a VM hybrid. Compiled `.text` of the denied artifact == 60366d747's default on all 5 witnesses, default != 60366d747. **Bench movers: 6 patterns / 18 census rows, not 3** (see 4). No row's engine moves. |
| 66->67 [MEMFN] R4h | ~half of artifacts move bytes, object-identical in executed code; `RX_VM_PROGRAM_BYTES` moves on VM | 564 census rows change v2 text at this step alone (586 total incl. mixed). Compiled `.text` identical on a stratified 94-row sample: **94/94**. `vm_program_bytes` moves (VM +22..+3,202). |
| 67->68 [NULLABLE-ANCH] | `empty_admits` row in `--emit-facts`; exactly 5 patterns move declined-nullable-default->selected, prefilter none->hybrid; ours evil-alt-nested + trim-nested-star | Confirmed by value: both read `selected` / `hybrid` / lang `exact`; 4 census rows (2 patterns x plain,whole, auto). No other bench pattern moves. Controls still declined: `^(\s+)*`, `(\s+)*$`, `(?m)^(\s+)*$`, `(x){0,5}`, `(?=abc)x*` (existing STAMP_CASE, unchanged). `empty_admits` by value through `--emit-facts` on 8 patterns (`^(\s+)*$` nullable yes / empty_admits no; one-sided and multiline yes). **Nothing here reads `--emit-facts`** (grep: only an unrelated `_emit_facts` size port) so no reader changed. |
| cf3ffaac `--list-axes` (not abi) | start axes projected; 18 `kind` cells predicate->list; one `applies` corrected | Exactly that (3). The only reader of `kind` is `registry_check` (reverse check applies to `list` axes); it passes with RX_REQ_WHY / RX_VM_RESEED / RX_VM_START now `list`. |
| 02db3811 -> 255bcdd8 | compiler-identical | census step `final`: 0 of 1,380 rows move. |

`struct rx_info`: UNCHANGED (the emitted `.h` of `abc` differs from 60366d747's only on abi lines).
**Shim floor stays 16**; the abi-sabotage arms (floor-1 and abi-5) pass.

## 2. Code changes

- shim.c `pb_has_vm_poss_arms`/`pb_vm_poss_arms`; driver.c `info vm_poss_arms`; adapter.py
  `vm_poss_arms` mask (bits `POSS_ARM_A0/A1/B`, adapter-named: pcrec defines no constants),
  `MASK_BITS`, `STAMP_SCOPE` `("vm", 66)`; the runtime scope iff (rule 7) enforces both directions.
- `DENY_FLAGS`: `-fno-poss-ctx-follow` (`nopossctxfollow`), `-fno-poss-bref-first`
  (`nopossbreffirst`), appended LAST. `DENY_CONTROLS`: two rows (reg_arm `skip`: the registry
  stamp_value is a mask bit; `check_b126_stamps` compares it to `MASK_BITS`).
- `check_b126_stamps` (new, in `main`): 23 checks -- B126_CASES (poss A0/A1/B, engine-selecting,
  scope both ways, R4h inert, nullable-anch lifted + 5 controls), registry-vs-MASK_BITS,
  `empty_admits` x 8. Identity there is on the **compiled `.text`** (`_b126_text_hash`), because
  v2 text identity is blind across abi 67.
- LEDGER_STAMP_CASES: evil-alt-nested + trim-nested-star under auto by value.
- [B122]/[B124] identity arms: when v2 differs they now fall back to `.text` (`_b126_text_eq`)
  -- 3 rows (`hyb-reseed: anchored`, two `req-use`) were red only because R4h respelled the text.
- Pin swap (`configs.toml pin = "255bcdd8"`), four registries re-archived, catalogue **3.16**
  (`[[pin_order]]` appended, NOT replaced: 60366d747 is a real pin in the store timeline) + 75
  sidecars, testees/pcrec/CLAUDE.md, pcrec_references.md, measurements/CLAUDE.md,
  catalogue/CLAUDE.md. bench/capability untouched (b125cap's).
- **Testee pair decision**: NO `pcrec-{auto,vm}-nopossctxfollow`. [B124]'s `nostartset` pair
  existed because the hats were that window's AFTER subject (716 census rows moved); the other
  [B124] flags and all [B122] flags got DENY_FLAGS only. I-134 asks for no run and 18 rows
  move, none changing engine. A pair is two configs.toml entries plus capability roster rows;
  the DENY_FLAGS words are already in place. Manager's call if a window wants it.

## 3. Registry deltas (each archive diffed against 60366d747's)

| surface | 60366d747 | 255bcdd8 | delta |
|---|---|---|---|
| `--list-axes` main | 131 rows / 44 axes | **136 / 46** | +`poss-ctx-follow` (a0, a1, widen; bit 50), +`poss-bref-first` (group-text, widen; bit 51), all `predicate`, stamp_macro RX_VM_POSS_ARMS (stamp_value 0x1/0x2/0x4 on the flagged rows, empty on the two `widen`); 18 `kind` cells predicate->list (req-admit 5, req-use 2, hyb-reseed 6, vm-anchor-bound 3, end-window 2); prefilter `first-memchr-bounded` `applies` corrected. Every other row byte-identical; `#section memfn` still 0 rows; the pcrec comment block identical. |
| `--list-limits` | 72 | **73** | +`PCREC_MAX_POSS_REF_DEPTH` 64 levels (arm B's backreference depth), inserted after row 39 |
| `--list-definitions` | 75 | 75 | byte-identical (data rows) |
| `--list-schema` | 79 | 79 | byte-identical |
| `--list-syntax` | -- | -- | byte-identical (not archived) |

## 4. Census (docs/dev/measurements/2026-10-08-b126prep-census.txt)

Population: b124prep's, 1,380 rows. Scratch pins at the abi 66/67/68 commits attribute each
row to the step whose v2 hash moved.

| result | rows |
|---|---|
| identical | 691 |
| changed | 586 = **67 only 564**, 66+67 **18**, 67+68 **4** |
| refused-both | 103 |
| refusal movers | **0** |
| step `final` (02db3811 -> 255bcdd8) | 0 |

- step 66: 18 rows = 6 patterns x {auto,vm} x {plain,whole} where they exist: capability
  wild-logparse-syslogbase-expanded (mask 0x3), doubled-word (0x6), currency-lookbehind-fixed
  (0x2, vm only), email-local-nodup (0x1), float-literal-bound (0x1, vm only), loglines bignum
  (0x2, vm only). In all 18 the two denials AT the abi-66 build reproduce 60366d747's v2 identity.
  No engine route changes on any bench row (pcrec's "default-route flips" are not in our sets).
- step 68: the 4 rows are evil-alt-nested and trim-nested-star (plain+whole, auto).
- step 67: 564 rows change text; 94/94 of a stratified sample are `.text`-identical.
  (docs/dev/measurements/2026-10-08-b126prep-r4h-text-identity.txt.)

## 5. Size books (measured at all five builds, by witness)

- abi 66: **+29 B** `emit_bytes` and `emit_code_bytes` on EVERY VM artifact, 0 on DFA, 0 in
  `vm_program_bytes` (asserted on every one of 96+ VM rows: `B126_VM_POSS_ARMS_LINE`).
- abi 67: NOT flat. `B126_R4H` holds 96 per-row (emit, code, program) moves, DFA +30..+392 B,
  VM +22..+3,202 (the program bytes move with it). Checked: abi 68 and `final` contribute exactly
  0 on every asserted row (asserted in the generator).
- 3 DENY_CONTROLS rows re-measured individually: scan-edge default arm +30 / denied 0;
  start-pinned +60 / +98; alt-island +29 / +29.
- abi 68 on its movers: evil-alt-nested plain 30,143 -> 34,077, trim-nested-star 28,342 ->
  32,276 (the hybrid pair; ledger rows assert stamps only).

## 6. Validation

- `check-harness` minus `check_expectations` (first pass, `/var/tmp/b126_harness1.log`):
  617 pass / 51 red, all explained: 43 size rows (fixed above), 3 identity arms (fixed), 4
  ENVIRONMENTAL (pruned old-pin builds: `gen_patterns --check` cd371441, KB-35 x2 25b1984f, b108
  mover 751b9c6d -- the same four as b124prep), 1 load-induced (`a real quick cell` read
  inconclusive-load under the lane's own census/make jobs).
- After the fixes: `check_mechanism_stamps` 131/0, `check_deny_flag_controls` 26/0,
  `check_b122_round1_stamps` + `check_b124_stamps` 19/0, `check_b126_stamps` 23/0, registry
  checks 6/0.
- Full `make check`: see 7.

## 7. make check

RESULT_PLACEHOLDER

## 8. Findings pcrec did not predict (candidate outbox items)

1. **Six bench patterns move at abi 66, not three** (18 rows): syslogbase-expanded, doubled-word,
   currency-lookbehind-fixed, email-local-nodup, float-literal-bound, loglines bignum. Their
   mask values are 0x1/0x2/0x3/0x6 -- the five-arm bits are all exercised.
2. **R4h is not "about half" in size but a graded growth**: +30 B per DFA search-loop site up to +392
   B, and VM `vm_program_bytes` moves with it (+22..+3,202). Not flat -> per-row books. Executed
   code identical (94/94).
3. v2 program identity (tools/program_identity.py, "program-identical" as the bench defines it)
   is blind across abi 67 for exactly the reason R4h changes the spelling; we use `.text`
   identity for cross-abi-67 controls. Worth telling pcrec that `program_identity v2` and R4h
   disagree, if they keep a v2-style gate.
4. The docs say [NULLABLE-ANCH] landed "since abi 67" (tuning.md / match_api.md) while the
   inbox and `rx_info.abi` say 68 (02db3811 stamps abi 68, c4c37af8 is 67). Prose drift only.
5. `a+(?=b)b` routes to the DFA under auto ([UCP] U2 folds the one-character lookahead) but is
   a poss-arm A0 witness only under forced VM.
6. `--list-axes` `poss-*` `widen` rows carry stamp_macro RX_VM_POSS_ARMS with an EMPTY
   stamp_value (the fallback), unlike every other fallback row, which names its value.

## 9. Charter-vs-committed checklist

| brief item | status |
|---|---|
| read BOILERPLATE, worktree b126prep, no store/reports write | done; reports/: the 75 sidecars' catalogue lines only (named above) |
| build `pin.sh 255bcdd8` | done |
| 66: reader, scope iff both ways, DENY control, STAMP witness | shim/driver/adapter; `check_b126_stamps` + 2 DENY_CONTROLS |
| 67: re-derive every size by measurement | `B126_VM_POSS_ARMS_LINE`, `B126_R4H` (96 rows), 3 deny rows, individually |
| 68: both movers by value, declined control kept | LEDGER rows + check_b126_stamps; `(?=abc)x*` and 5 controls |
| `--emit-facts` reader? | none exists; asserted by value only |
| registries re-archived and diffed, `kind` readers | section 3; only registry_check reads kind |
| struct rx_info / shim floor | unchanged / 16 |
| testee pair decision | NO, with reason (section 2) |
| catalogue `[[pin_order]]` + bump | 3.16 + sidecars |
| census 2026-10-08-b126prep-census.txt | committed, every changed row attributed to a step |
| testees/pcrec/CLAUDE.md | committed |
| root CLAUDE.md paragraph | DRAFT below, NOT applied |
| full `make check` | section 7 |

## 10. DRAFT root CLAUDE.md pin paragraph (NOT applied)

> 2026-10-08: [B126] RE-PINNED to **255bcdd8 (abi 68)** (lane b126prep, inbox I-134/I-135; pcrec
> main with [NULLABLE-ANCH] 02db3811 + [MEMFN] R4h, compiler-identical to 02db3811). THREE abi
> steps in one adapter change: 65->66 [ART-POSS-ARMS] (`RX_VM_POSS_ARMS`, a mask literal on every
> VM artifact -- 0x1 A0 / 0x2 A1 / 0x4 B, adapter-named bits `POSS_ARM_*`; `-fno-poss-ctx-follow`
> (bit 50, ENGINE-SELECTING) and `-fno-poss-bref-first` (bit 51) as DENY_FLAGS + DENY_CONTROLS, NO
> pinned testee; scope `vm` in STAMP_SCOPE), 66->67 [MEMFN] R4h layout normalization (564 census rows
> change text, compiled `.text` identical 94/94 on a sample; sizes per-row, `B126_R4H`), 67->68
> [NULLABLE-ANCH] (`empty_admits`, a `--emit-facts` row nothing here reads; evil-alt-nested and
> trim-nested-star go `declined-nullable-default` -> `selected`, prefilter none -> hybrid). `struct
> rx_info` unchanged, the shim floor STAYS 16. Registries: `--list-axes` 131/44 -> 136/46 (the two
> poss axes; plus cf3ffaac's 18 `kind` cells predicate->list and one `applies` correction, not an abi
> event), `--list-limits` 72 -> 73 (`PCREC_MAX_POSS_REF_DEPTH`), definitions/schema/syntax
> byte-identical. Census (docs/dev/measurements/2026-10-08-b126prep-census.txt): 1,380 rows, 691
> identical / 586 changed (67 only 564, 66+67 18, 67+68 4) / 103 refused-both / 0 refusal movers; step
> 66 moves six bench patterns, not pcrec's three. v2 program identity is blind across abi 67; the
> [B122]/[B124] identity arms fall back to compiled `.text`. Catalogue 3.16. NOT YET MEASURED at
> 255bcdd8: any timed cell; the capability@0.2 window ([B125]) measures the fixed compiler.
