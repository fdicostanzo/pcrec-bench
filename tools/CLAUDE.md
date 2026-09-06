# tools/ — repo tooling that is not the harness

| file | role |
|---|---|
| `selfcheck.py` | `make check-harness`: the [B3] half of the self-check suite |

THE GENERIC GATES ENUMERATE (`subbench_dirs()`, [B11.1]). Harness contract 6
says "bench/*/ each", and the checks that belong to the sub-bench CONTRACT --
the generators reproduce their committed manifests, any other `gen_*.py` in
the directory re-derives under `--check`, `expectations.tsv` re-derives, both
drivers answer the set's floor pattern exactly as the oracle says -- discover
every `bench/<name>/` with a `subbench.toml` instead of naming one. They named
`email`, and the count this suite prints would not have moved on the day a
second sub-bench landed: a check that silently covers half of what it claims
is the shape of failure this file's organising principle exists to prevent.
The email-SPECIFIC arms (the wrong-answer fixture, the two-patterns control,
the frame-buffer block, the `whole-subject` form control) stay named, because
they are about that set's own fixtures and not about the contract.

The per-sub-bench floor smoke is also the per-sub-bench DRIVER smoke: a real
adapter compiles a real pattern of the set and answers real subjects of it,
and it picks its two subjects BY THE EXPECTATION rather than by looking for a
byte -- a set whose floor matches every subject (bench/loglines' is `:`) has
no missing one, and the check says so rather than failing.

The [B20] block (2026-08-30, schema v1.4 — the gate's shape) adds ten
checks, every one carrying the control gate_shape_v14.md §8 names and
none injecting a sleep into a production driver (ruling R-10):
`check_target_core_preflight` (three synthetic captures: a busy target,
an idle one, the target's ROW ABSENT — the tri-state field and `gate()`
refusing BY NAME; unpinned, the field is absent and the 60 % capture is
refused by the NON-target clause instead), `check_quiet_cli_agrees_with_gate`
(the CLI's printed reasons are `gate()`'s list verbatim, exit 3; a
passing sample exits 0), `check_after_sample_is_provenance` (a 40 %
after sample on an agreeing 5-trial record → `measured`, the provenance
sentence SECOND in `note`, X26 holding, validated through `store.write`;
the SAME record re-stamped 1.3 rejected by X13 AND X33 — one sabotage,
two versions, two verdicts), `check_trial_agreement_fixture` (the
hand-computed fixture: group A d=2 of n=4 disagrees under (2,3), a
tolerated single 3× trial, a fast row, unjudged rows under BOTH reason
tokens, the boundary rows at exactly k·m and m/k; `share_c=1` flips it;
3 trials → `n/a-trials`; `validate.py`'s OWN implementation — no shared
source — gives the same integers, directly and through `store.write`,
and a stamp of 3 beside rows that say 4 is rejected by X32),
`check_spread_status_stamped` (`derive_status` on every decision-table
row, then a disagreeing record stamped and written → `inconclusive-spread`
with the §3.4 line at offset 0 of `status_detail`; ONE slow trial per
row → `measured`, the rule tolerates one), `check_status_sentence_never_elided`
(72 real calibration sentences over the cap: the status sentence at
offset 0, the marker naming the dropped class; joined WITHOUT `first=`
it is elided), `check_smoke_block_na_trials` (the `--trials 1` smoke
record carries the block, `n/a-trials`, every key unjudged, scratch
status = the pre-flight's; re-tiered pinned through `derive_status` →
`inconclusive-spread`; the X33 missing-block control),
`check_scratch_carries_block` (`quick --trials 5` carries and prints the
block; the default 3 trials print `n/a (3 trials …)` — the verdict at 5
trials is reported, not asserted `agree`, because the box is not what
the check is about), `check_exit_code_4` (`cmd_run` in-process with the
pre-flight's SAMPLES simulated quiet: a pinned `--trials 1` run returns
4, written and indexed with the per-status line; the same at tier
scratch is `measured` and returns 0) and `check_timeline_provenance`
(a pinned calibrated run writes one `/proc/stat` timeline item per group
with the target reading our own driver; the module's path pointed at a
nonexistent file — in-process, no production hook — writes NO timeline,
and both validate).

`selfcheck.py`'s organising principle is pcrec's check-design lesson: every
gate is exercised against an input it must REJECT in the same run that
exercises it against one it must accept. A check with no failing case proves
nothing, and a control that passes because the judge dislikes everything
proves nothing either — which is why the wrong-answer control runs each
falsified expectation AND its committed counterpart.

Three of its controls have already failed a real implementation and changed
the code: the two-patterns control (both patterns shared one workdir), the
store race control (a shared staging directory lost 2 of 8 records), and the
per-subject timeout control (nothing in the corpus hangs, so the alarm path
had never run). A fourth, the v1.1-readiness control, exists to stop
`record.project()` becoming dead code before the schema version flips.

The frame-buffer block (`check_frame_buffer`, [B8]) follows the same rule:
its "buffer matters" arm was sabotaged once on purpose — the shim made to
pass a NULL descriptor — and the configured-capacities arm failed exactly as
it must (the deep subject gave up as under the default), so the control is
known to see a shim that ignores the buffer. Its other arms: the `_in`
entries agree with the plain ones on the smoke pattern; a tiny caller buffer
gives up `PCREC_ERR_FRAMES` BY NAME; every pcrec compile row at the pin reads
ONE abi with the four sizing pairs; a DFA artifact stamps a frame size of
0 and records no `buffer_*` pair; a VM artifact records the configured
capacities. Seven PASS lines, all needing the pin's `_in` surface (pcrec
17469b6 or later).

That abi arm used to read `abi == 3` as a literal, and was edited at every
re-pin ([B16] removed it): a check that has to be edited to keep passing is
a check of this file's edit history. It now READS the abi and holds what
actually matters — one abi across four artifacts of both engines (a mixed
set would mean two pcrecs got into one run), at or above the floor
IMPORTED from `shim.c`'s `PB_SHIM_MIN_ABI` rather than retyped here.

The [B10] blocks (schema v1.2, the tiers, `quick`, `pcrec-local`) add
sixteen PASS lines, every gate with its sabotage: the two tier controls
are rejected FOR X28 / X29 by name and the 1.1 examples with no `tier`
still validate; the canonical store refuses a scratch record on write
and refuses to INDEX one planted by hand (the control: a scratch store
takes the same record, validated); the shared reduction reproduces a
hand-computed median (3 trials × 2 subjects → 220) and EXCLUDES a set
with one give-up while naming its code; a `quick` cell completes under
`gnutimeout 300` and the median it printed is recomputed from the record
file with the same function; `pcrec-local` errors cleanly without
`$PCREC_BIN`, describes the pin's binary as `local:<sha12>` with no
`+describe`, describes a scratch-built repository as `+<sha>` with HEAD
when clean and `+…-dirty` with a null commit when dirty, runs a quick
cell, and is REFUSED into a canonical store (a temp one carrying the
marker, so a broken refusal cannot reach the real `store/`).

The [B16] blocks (2026-08-28, the abi-8 re-pin) add thirteen PASS lines
(75 in all after the merge with [B11.1]'s per-sub-bench enumeration)
across three checks, each built around the failure it would otherwise
miss:

- `check_mechanism_stamps` compiles a real artifact of each KIND at the
  pin — pure DFA, VM HYBRID, non-hybrid VM, provably-empty — and asserts
  each stamp's VALUE, not its presence. A presence-only check would pass
  a `dfa_prefilter` filled from the wrong macro (it would read `hybrid`,
  which is not in that pair's value set at all), and would pass an
  adapter that dropped a pair the driver prints — a real failure this
  bench shipped for five pins, since `engine_stamp` was printed from abi
  4 and never recorded. Both directions of match_api.md §6.3 (a)'s IFF
  are asserted (a hybrid carries all three `_DFA_*` pairs; a non-hybrid
  VM carries none), and so is the fast tier's own scope. Its witnesses
  are small hand-chosen patterns rather than `bench/email`'s, because a
  check whose witness is a corpus pattern stops being a check the day
  engine selection moves under it — which is exactly what happened to
  `factored` between 8da6120 and 692c2e8.
  [B18] extended it to the abi 9-11 pairs on every case, added the
  anchored `attempt` kind, the LEDGER rows (`LEDGER_STAMP_CASES`: the
  bench's own loglines/email patterns at the values pcrec's inbox
  I-15/I-16/I-17 predicted — `uuid` offsets `0,8*,13`, `iso-ts` `0,4*`,
  `stack-frame` `0,1*`, the declined rows `none`, every VM artifact
  `K=8`/`default`, and `level-context` under `auto` compiling as the
  [SEL-1] VM fallback with `RX_ENGINE_WHY: dfa overflowed` in its
  diagnostic — on those rows a corpus witness moving IS the finding), the
  scope rules for the new pairs in both directions, and one fact read
  off the DRIVER rather than the record: `rx_info.match_form`'s presence,
  so "NULL on a VM artifact" is a value the check saw.
- `check_deny_flag_controls` (`check_dfa_table_deny_flag` until [B18]) is
  the control that keeps a one-sided stamp from being indistinguishable
  from a constant. pcrec's own form census measured `indexed` and `mixed`
  at ZERO corpus population, so nothing this bench measures will ever
  move `dfa_table`; the same is true of `dfa_match` (every DFA artifact
  is `unwrapped`) and `unroll_k_why` (every VM artifact `default`).
  Table-driven (`DENY_CONTROLS`): `-fno-premul-table` → `indexed`,
  `-fno-offset-skip` → `byte-class-bounded` AND offsets `none` on `uuid`,
  `-fno-anchored-dfa` → `search-filter` on `floor`, `-fno-size-term` →
  `denied` on `orig`/vm — through `pcrec-local` at the pin's binary, the
  flag's SPELLING read from `testees/pcrec/list_axes.tsv` (the axis's
  order-1 row) and its `stamp_value` checked against the default arm
  where the registry carries one.
- `check_list_axes_registry` ([B18]): the committed `list_axes.tsv` is
  byte-identical below its source header to the pin's live
  `pcrec --list-axes`, and `adapter.registry_check()` finds every
  registry `stamp_value` for the five name-valued macros declared (and
  nothing declared that the registry's `list` axes lack, outcome values
  `dfa_table none`/`mixed` excepted).
- [B19] (2026-08-30, the abi-12 re-pin to 96e44c2) extended the three
  above and added two: `check_mechanism_stamps` asserts `engine_sel` on
  every case (the ledger's `level-context` row at I-18's PREDICTED values
  — `collapsed-prefilter` / `count-collapsed` / `dfa overflow retry, exact
  nfa 462` — all of which HELD), two new kinds (a hybrid with a counted
  repeat that stays `exact`; K41's witness 2, the SIZE-CAP rung's rescue,
  which stamps `sel=selected`), two bounded ledger rows (`cls-upto-32768`
  rescued as a collapsed-prefilter hybrid; `cls-upto-16384` the DFA that
  WARNS, `warned_emit_bytes 724699`, outcome `compiled`, the line in the
  diagnostic), the language pair's scope in both directions (5 hybrids
  with, 17 others without — the letter said "every VM artifact"; the spec
  and the artifacts say hybrids), Frank's ask (b) bucket DERIVED from the
  records and asserted to be exactly the two state-cap rescues (the
  size-cap one outside it), and `emit_bytes`/`emit_code_bytes` on every
  artifact. `check_deny_flag_controls` is table-driven with a sixth
  `deny`/`force` column (the `prefilter-lang` row's `cli_flag` carries
  both spellings): `-fno-prefilter-collapse` on `level-context` → the
  prefilter is DROPPED (`overflowed-dfa`, the language pair absent — three
  pairs move), on K41 witness 2 → REFUSED by name (`DID_NOT_COMPILE`);
  `-fprefilter-collapse` on `a(b|c){2,5}d` → `count-collapsed`/`forced`.
  `check_list_definitions_registry` diffs `testees/pcrec/list_definitions.tsv`
  (the fifth registry surface, [DD-11]) against the pin's live output.
  `check_emit_size_port` runs the pin at `--warn-emit-bytes=1` on four
  artifact kinds × two forms and compares the warning's two numbers with
  `adapter.emit_size()`'s over the same files (8/8 byte-exact) — the
  control that a PORT of someone else's size definition is that
  definition — plus a hand-classified probe with a hand-derived answer.
- [B22] (2026-08-31, the re-pin to 263b013 -- abi 12 unchanged; inbox
  I-21-correction/I-22/I-25) extended the same checks for a pin that adds
  VALUES, not stamps: `check_mechanism_stamps`' size-cap kind re-pointed
  at its OWN route token (`size-cap-retry`, [LIM-1] -- the `selected`
  mislabel closed), eleven ledger rows for the I-21-corrected
  DECLINE/KEEP sets with a sixth FORM element on the case tuples (the
  four nullable declines stamp `declined-nullable` with prefilter `none`
  and NO language pair -- cls-upto-32768 both forms with its emit bytes
  pinned 18,291/18,496 (= code: no tables at all), the two 16384 wholes;
  the six kept rescues stamp `collapsed-prefilter` with their exact-nfa
  whys -- ctx ×4, the nest wholes, nest3-16 still the one K mover), the
  plain-vs-`\z` overflow ROUTES asserted distinct in RX_ENGINE_WHY (the
  state cap vs the K7 subset-elements budget -- two list_limits.tsv rows
  by name), and the ask-(b) bucket re-asserted as the VALUE-only rule
  over all witnesses (the `_why`-prefix special case retired, the
  size-cap witness now INSIDE). `check_deny_flag_controls` finds the
  flag row by its `cli_flag` cell (the 263b013 registry moved
  `-fno-size-term` off order 1 onto the `denied` row) and takes an
  optional `reg_arm` column ("default"/"flagged"/"skip"); a new force
  row proves `-fprefilter-collapse` reaching the nullability POLICY on
  `(x){0,5}` (`_LANG "exact"` / `_LANG_WHY "nullable collapsed
  language"`, route `selected` both arms). `check_list_limits_registry`
  is the THIRD registry-archive diff (44 rows, pcrec D90/[LIM-1]).
  `check_emit_size_port` gains the fifth witness: the declined
  `{0,32768}` artifact, both forms -- I-22 (ii)'s same-pin re-comparison,
  the counting rule stated (comment-excluded, .c + .h summed).
- [B25] (2026-08-31, the re-pin to a7e0bdf — abi 12 → 13; inbox I-27,
  [OPT-5] STEP 1) extended the same checks for the pin that changed a
  MACHINE: `check_mechanism_stamps` asserts the new `dfa_scan_edge` pair
  BY VALUE on every case (`range` on contiguous-class runs down to the
  unbounded one-state `[0-9]+` form; `bitmap` on ipv6's non-contiguous
  hex class — the only bitmap witness in reach; `none` on
  `attempt`/`empty` scans and on runs the pass leaves alone; absent
  exactly where no DFA scan exists — the scope tuple grew to four
  `_DFA_*` pairs, both directions), re-derives the 16384 rung as the
  COLLAPSE I-27 (2) predicted (the DFA that warned: 724,699/11,589 with
  the advisory line → 16,352/13,012 silent; `warned_emit_bytes` asserted
  ABSENT — no bench artifact warns at the default any more), asserts the
  DECLINE/KEEP sets, the K7-vs-state-cap routes AND the 65535 NFA-cap
  refusal UNCHANGED by name (I-27 (3): the caps fire during
  construction, before the edge can act — the day the 65535 assertion
  fails with a compiled artifact is the day [OPT-5] STEP 3 lands).
  `check_deny_flag_controls` gains the `-fno-scan-edge` (bit 21) row on
  the same rung — `range` → `none`, 16,352 → 724,737 B, and the warning
  RETURNS (the warn-capture path's positive witness since the ledger row
  stopped warning); the flag's registry row carries no `stamp_value`
  (the stamp lives on the companion `scan-body` axis), the note path's
  first exercise. The three registry diffs re-point at the re-archived
  copies (axes 69 rows / 23 axes: + the `scan-edge`/`scan-body` pair;
  definitions byte-identical; limits 45: + `PCREC_MAX_SCAN_EDGES`), and
  `RX_DFA_SCAN_EDGE` joins `registry_check` both ways (the `scan-body`
  axis carries `stamp_value` on all four rows, `none`/`mixed` as
  `predicate` outcome rows).
- [B24] (2026-09-01, the COMPILEE TOOLCHAIN axis; pcrec [CC-CLANG])
  adds `check_cc_axis`, eighteen PASS lines in five arms. pcrec emits C
  and stops, so the compiler that builds the artifact is this bench's
  own phase 2 and the axis is a testee property (`cc` in
  `configs.toml`). The arms: (1) the six configs that predate the axis
  derive an UNCHANGED `testee_id` and `build_flags`, compared against a
  FROZEN copy of the pre-[B24] renderer kept in the check itself, so a
  later edit to `describe()` that re-words an existing testee's
  provenance is caught rather than shipped and the store's committed
  a7e0bdf records stay comparable; (2) all three precedence arms — `$CC`
  still decides for a config with no `cc`, an agreeing `$CC` is
  accepted, a CONTRADICTING one is refused BY NAME rather than silently
  winning, which is the only outcome that could put a compiler in a
  `testee_id` that never ran; (3) the token round-trips into
  `testee_id`, `config_extra` and `build_flags` (clang's `--version`
  first line included, beside the driver's own compiler); (4) each
  artifact KIND compiled by BOTH siblings and asked the same smoke
  subjects, agreeing on answer, span AND captures — captures included
  because a shim that dropped the vector would otherwise agree with one
  that did not — with a per-kind `min_matches` floor, since two `.so`
  that both answer "no" to everything agree perfectly and prove nothing
  (the provably-empty artifact carries 0 and is held to the opposite
  statement instead); (5) one whole cell per clang config into a scratch
  store, validated by the run, with the token read back off the WRITTEN
  record rather than off `describe()`.
  A clang REFUSAL is a first-class outcome here, never a skip. At pin
  a7e0bdf (abi 13) a VM artifact that never pushes a resume frame emits
  `goto *run->resume_stack[...].resume_label` into a function with no
  `&&label` expression, and clang refuses it — three of the eight kinds.
  Such a refusal passes ONLY when its diagnostic carries that cause
  verbatim; any OTHER refusal FAILS, as a finding nobody has read. The
  refusing set is PRINTED, never frozen, so the check is green both at
  this pin and after it crosses pcrec's abi 14, where [CC-CLANG] step 1
  makes the set empty and those rows become agreements. One case
  (`(a+)+b` under `--engine=vm`) exists solely so the agreement arm is
  not DFA-only at abi 13: it pushes a frame, so it carries `&&label`
  expressions and clang accepts it.
- `check_abi_floor_refusal` is the SABOTAGE, and the path is unreachable
  without one: the pin's abi is at or above the floor by construction
  (13 at a7e0bdf vs a floor of 10 since [B18]; neither abi 12, the [B22]
  values nor abi 13's macro added a field), so nothing in the corpus can
  be below it. A real artifact's `.abi = N` is edited to `5` in a copy,
  built with the ordinary shim and run by the ordinary driver, and must
  be refused BY NAME carrying both numbers (the floor read out of
  `shim.c`, never retyped) — with the unmodified artifact loading in the
  same run as the positive control (a refusal
  that fired on everything would pass a check written without it), and
  the token the adapter watches for checked against the diagnostic the
  driver actually produced, since that is two copies of one string in
  two languages with nothing else enforcing that they agree.
- [B37] (2026-09-05, pin 334fd10e, abi 22 -- SIX abi steps in one
  re-pin; pcrec inbox I-41/I-43/I-44) adds no check FUNCTION and grows
  three: `check_mechanism_stamps` asserts the four new pairs BY VALUE on
  every kind -- `dfa_uniform_folds` on the scan family's iff (0 on every
  reverse-pass corpus DFA and the no-table scans, 4 on a pinned
  `unwrapped` rung, 2 on the pinned `search-filter` 16384 rung, both
  values reached with a one-character control), `vm_alt_islands` on the
  VM scope with a witness at 0 / 1 / 2 (`foo|bar` islands, `fo|foo`
  declined by the registry's own prefix-bearing knee, level-context and
  ctx-greedy-256 islanding TWO alternations each on the [SEL-1] hybrid
  under `auto`), and the `vm_entry_shape` / `vm_program_bytes` PAIR with
  a witness at each of the four closed tokens (`forward` foo|bar,
  `inline` (abc)(def), `plain` (a+)+b, `shared` w-256 at 305,686 B) and
  the AUTO size rule asserted over every VM artifact against
  VM_INLINE_CHAIN_MAX_BYTES read from `list_limits.tsv`; six new
  STAMP_CASES kinds and eleven new ledger rows (the altwide ORDER PAIR on
  the VM route asserted IDENTICAL to each other -- 292,043 B, 305,686
  program bytes -- rather than each to a constant; I-43's island/chain
  code-byte ratios 0.856 / 0.812 / 0.764 re-derived to three decimals
  against the SAME pin's `-fno-alt-island` arm, pcrec-emitted and sized
  without gcc; the refusal boundary BY ROUTE -- the DFA wall at w-384
  UNMOVED at the total cap, the VM wall MOVED to 384<w<=512 with w-384
  compiled as an island, w-512 refused at the code cap and w-384 refused
  AGAIN under the denial; the [B33] (3) fold witnesses' `-O2` OBJECTS
  sized with `size -A`, a folds-4 artifact carrying NO `.rodata` section
  against the folds-0 control's; iso-ts 8/4 edges through the abi-19/21
  dispatch). `check_deny_flag_controls` gains the `-fno-alt-island` (bit
  23) row -- FOUR pairs move at once on `foo|bar` (islands 1->0, frameless
  1->0, shape forward->plain, program bytes 1,532->1,233) -- and its two
  DFA deny rows re-derived with the fold count riding along (the
  scan-edge row 2->1 and its denied arm 367,390 -> 252,587 B, STILL
  warning by 2,587 B; the start-pinned row 4->6, the count's ceiling,
  reached on a real artifact only by that flag). The three registry
  checks diff the re-archived copies (axes 74/25: + `alt-island`;
  definitions byte-identical; limits 55: + nine `VM_ISL_*` /
  `VM_INLINE_CHAIN_MAX_BYTES` rows + `PCREC_MIN_SCAN_CHAIN`, one desc
  reworded). `check_abi_floor_refusal` is UNCHANGED: no rx_info field
  across abi 17-22, the floor stays 16 and both sabotage arms stand.
- [B39] (2026-09-06, pin d34c9131, abi 23; pcrec inbox I-49/I-50) adds no
  check FUNCTION and grows two. The prep lane (b39prep, 2026-09-05)
  drafted both rows before any build existed using the DRAFT(v)/TBD
  placeholder protocol (`DRAFT(v)`, a predicted value asserted exactly so
  a wrong prediction fails by name; `TBD`, presence asserted and the
  value printed); the build (2026-09-06, inbox I-52) CONFIRMED every
  prediction and RETIRED both placeholders back to plain values:
  `check_mechanism_stamps` gains the `vm_cls_folds` pair by value -- 3 on
  `(?i)abc` forced-VM, 26 on altwide ci-256 forced-VM (26 distinct
  letters), 0 on five fold-free VM rows and on the two one-character
  DECLINE controls (`[ac]`, not a 0x20 pair; `` [@`] ``, a 0x20 pair of
  non-letters), ABSENT on ci-256 under auto (a DFA); the scope row (every
  VM artifact, no DFA one), not-a-constant, the STRUCTURAL row (as many
  distinct `(b | 0x20) == N` compare constants in the artifact's own text
  as the stamp says, every N a lowercase letter), and the deny row on
  pcrec's own emission (`-fno-cls-fold` moves the stamp to 0, restores a
  `class_bitmap[32]` table per folded class, puts the SIZE BACK UP on both
  witnesses, and leaves a fold-free artifact BYTE-IDENTICAL -- the
  strategy_denials mask). Every VM `emit_bytes` in the tables is adjusted
  by ONE constant, `B39_VM_STAMP_LINE` (26: the new stamp line), DFA
  sizes untouched. `check_deny_flag_controls` gains the `-fno-cls-fold`
  (bit 24) row on `(?i)abc` (folds 3->0; frameless and shape unmoved). The
  three registry checks diff the re-archived copies exactly as predicted:
  axes 74/25 -> 76/26 (`cls-fold`), definitions byte-identical, limits 55
  -> 56 (`PCREC_MAX_AUTO_DFA_ELEMS` + three rows re-worded via the new
  raise-only flags). The floor stays 16 (no rx_info field at abi 23):
  `check_abi_floor_refusal` UNCHANGED. The DRAFT(v)/TBD placeholder
  machinery itself stays in selfcheck.py, unused until the next re-pin
  is prepared ahead of its build.
