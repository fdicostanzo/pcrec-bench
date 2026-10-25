# b142fix report (2026-10-25) -- the compound stamp declarations

STATE: code done and committed; **checks OWED** (box rule: no suite, build or
compile was run by this lane). Ready for checks.

## The bug
The first window at 9ae59f5d4 refused the pinned `sentinel x pcrec-auto` record
(validate.py X15) on `wild-waf-crs-942360-concat-sqli`, whole-subject form: a
COMPOUND (`compound = split`), whose machine-level stamps read the token
`compound`. METADATA_DECL's closed enums never gained it; the b142prep census
was compile-only and never validated a record.

## What the pcrec source says (read-only, pin 9ae59f5d4)
`docs/spec/match_api.md` 6.3.12 table + `src/gen/stamp_kinds.c`: "machine
(string)" stamps -> `"compound"`: `_DFA_SCAN, _DFA_PREFILTER,
_DFA_PREFILTER_OFFSETS, _DFA_TABLE, _DFA_SCAN_EDGE, _DFA_START, _DFA_MATCH,
_END_WINDOW, _REQ_WHY, _REQ_HANDOFF, _VM_START_SCAN` and the VM's string
stamps; "machine (count)" -> -1: `_DFA_UNIFORM_FOLDS, _RUN_WORDS`, the VM's
counts/masks. The VM stamps never reach a compound shell (it is a DFA
artifact; stamp_kinds.c says so), so none is declared. `rx_info.scan/.prefilter/
.match_form/.search_form` mirror the same token (already cross-checked).

Correction to the brief: only 8 of the 11 listed fields have a closed value
list (`dfa_scan, dfa_prefilter, dfa_scan_edge, dfa_start, dfa_match,
dfa_table, req_why, vm_start_scan`). `dfa_prefilter_offsets`, `end_window`,
`req_handoff` are declared `string` (free), so the validator already accepts
`compound` there; the counts are `integer` and accept -1. No declaration
change for those five; the iff below covers all 13.

## Changes
- `testees/pcrec/adapter.py`: `COMPOUND_MACHINE_ENUMS/_STRINGS/_COUNTS`; the
  eight enums gain `compound`; `REGISTRY_OUTCOME_VALUES` gains it for the same
  eight (the registry drift check otherwise flags the extra declared value);
  `check_compound_iff(meta)` called from `_check_agreement` (claim 13): a
  route-family stamp reads `compound` (counts -1) IFF `compound` is not
  `none`/`forced-off`; refused BY NAME otherwise, on both sides.
- `tools/selfcheck.py` (check_b142_stamps, after the compound compile): the real
  compound's engine_metadata through `RecordValidator._check_metadata` (X15) must
  be clean with >= 8 fields reading `compound`; the iff accepts it; controls: a
  plain `abc` validates; the iff REFUSES a planted `dfa_scan=compound` and
  `dfa_uniform_folds=-1` on the plain artifact and a machine `dfa_scan` /
  `req_why` on the compound; no other enum declares `compound`.
  Note: declared sets are per FIELD, not per pattern, so X15 alone cannot reject
  a planted `compound` on a plain artifact -- the adapter iff is the control.
- `docs/dev/lanes/b142fix_rehearsal.sh` (NOT RUN): scratch-store `--dry-run`
  of sentinel, capability, email, loglines, altwide, bounded, litrun, syntax,
  utf8, subst (ONE=1 default: first config per set + capability's compound
  witness + a `bounded:vm` pass; ONE=0 full rosters), pass criterion by name.
  Estimate ~1.3 h (ONE=1), ~3.5-4 h (ONE=0). Heavy: the manager clears it.
- CLAUDE.md: testees/pcrec (finding paragraph under "Re-pin at 9ae59f5d4"),
  docs/dev/lanes.

## Charter-vs-committed checklist
1. Verify affected set against pcrec docs/source: DONE (above; differs from brief).
2. Adapter iff, refused by name: DONE (`check_compound_iff`).
3. Harness check with control: WRITTEN, NOT RUN.
4. Rehearsal script + runtime estimate: DONE, NOT RUN.
5. CLAUDE.md for touched dirs: DONE.
6. Check counts: OWED (to be filled after the manager's go).

## Check counts
OWED. Expected: `make check-harness` +6 checks over the 324-based count.
