# lane b90repin report — RE-PIN to ce658cb7 (abi 31 -> 33) + [B88] program_sha256 (schema v1.7)

**Task**: plan rows [B90] and [B88] / inbox I-108. Re-pin the pcrec testees
from `6ef76820` (abi 31) to pcrec main `ce658cb7` (`Merge branch
'lane/k64fix': K64 fix A + abi 33`), the [B74]/[B80]/[B84] ritual; [B88]
rides it: `engine_metadata.program_sha256` on every pcrec compile row,
record schema minor bump, the null band reads the field first. No
`store/`/`reports/` write, no timed window (the manager's, tonight).

**Branch**: `lane/b90repin` (harness worktree `.claude/worktrees/agent-a69c6359fb21a4aeb`),
six commits: `a41362d` (pin, registries, shim, +1001 size books),
`d445150` ([B88] field + schema + census v2 + null band field-first, K64
ledger rows, vars check), `39626ee` (catalogue 3.7 -> 3.8), `c8051f1`
(CLAUDE.md / design note / references), `304ca28` (the archived census),
and this report.

## 0. Findings the manager must read first

1. **Abi 32 is pcrec's [VAR] module, NOT in I-108's text** (commit
   68422ba1, D121): `${name}` caller variables. On EVERY artifact of both
   engines: an `rx_var` typedef, two appended `rx_ctx` members (`vars`,
   `nvars`), `#define PCREC_ERR_UNSET_VAR (-8)`, two appended
   `struct rx_info` members (`vars`, `nvars`) and their initializer lines.
   `--features all` (every config here) now INCLUDES `vars`: the byte pair
   `${` in a pattern is a variable reference (VM-only; a var-bearing
   artifact's `<prefix>_search` gains a trailing `vars, nvars` pair the
   shim does not pass -- it would fail to BUILD, loudly). MEASURED: no
   bench pattern contains `${` (249 patterns across six sets).
2. **I-108 prediction 3 ("auto configs program-identical to 6ef76820 on
   the bench patterns") is FALSE for six BACKREFERENCE patterns.** The
   [VAR] step generalised the backreference compare
   (`rx_bref_match(s, n, ref_start, ref_end, at)` ->
   `rx_span_match(s, n, ref_ptr, reflen, at)`, the shared seam entry of
   D121's addendum), so every backreference artifact's program text
   changed on EVERY config: `doubled-word`, `dup-param-detect`,
   `phone-palindrome-6`, `quoted-delim-match`, `tag-pair-match`,
   `tag-depth3-bound` (36 artifact rows: 6 x 3 configs x 2 forms). pcrec's
   own census counted fix A's movers against its abi-32 baseline, where
   the seam change had already landed; against OUR BEFORE (6ef76820) the
   two steps compound. It DOES hold for every non-backreference auto
   artifact (112/124 auto-caps, 113/125 auto-nocaps compiled rows
   identical; `RX_REQ_WHY` moves on NO auto artifact). Tonight's window
   must read those six patterns' auto cells as CHANGED programs, not as
   null controls -- which the v2 census does automatically.
3. **The [B79] census normalization (v1) would have read EVERY artifact
   `changed` at this pair** (abi 32 grew the shared ABI block and the
   `rx_info` initializer everywhere): 373/373 compiled rows -- an EMPTY
   null band tonight. [B88]'s one-artifact normalization (v2, below) was
   needed anyway for a record field (v1's one-sided-define rule is
   pair-relative and cannot be stamped on one row) and fixes this: v2
   reads 325 identical / 48 changed / 11 refused.
4. **v2 is a faithful generalisation of v1, measured**: over the three
   committed capability@0.1 pairs (3 configs x 64 x 2 forms, 1,152 rows)
   my v1 re-run reproduces the committed files' verdicts 1,152/1,152, and
   v2 agrees with v1 on 1,144. The 8 others are ONE pattern
   (`wild-logparse-syslogbase-expanded`, both auto configs, both forms,
   8d716693->b1885a83 and b1885a83->6ef76820) where v1 read `changed` only
   because a PROSE stamp, `RX_VM_PREFILTER_LANG_WHY "size cap retry, exact
   1463264 > 1000000"`, echoed the pin's own new stamp line in its byte
   count (+29 = `RX_REQ_WHY "emitted"`); the program is identical and v2
   says so. So v1's documented premise "a moved stamp value is always a
   changed program" was false for that one prose stamp -- the committed
   v1 files under-count the null population by those 4 rows per pair (not
   re-derived here: `reports/` is out of scope; they stay v1 and
   `--check`-clean).
5. **Schema version: v1.7, not v1.6.** v1.6 was already taken (lane
   b44boolgrain, `testee.grain`, 2026-09-17; the root CLAUDE.md still said
   v1.5 -- corrected). BD13/[B88] say "v1.6"; the rule-conforming number
   is 1.7.
6. **`struct rx_info` grew, but the shim floor STAYS 16**: two members
   APPENDED, no offset moved, the shim reads neither (no bench artifact
   has a variable). One real shim fix: both `rx_ctx` builders
   (`pb_match_caps`, `pb_match_caps_in`) now zero `ctx.vars`/`ctx.nvars`
   under `#ifdef PCREC_ERR_UNSET_VAR` -- the stack struct would otherwise
   carry an indeterminate pointer (harmless today: a var-free artifact
   never reads `ctx->vars`, MEASURED).
7. **The K64 prediction "0 VM steps on the nomatch ones" is not
   observable in a record** (no step counter in the driver protocol); the
   window can test "answers as pcre2 does / no give-up" and read the
   timing as a proxy (a ~floor-scale cell vs a 500M-step give-up).

## 1. Charter-vs-committed checklist

| # | charter item | status | where |
|---|---|---|---|
| 1 | `pin.sh ce658cb7`, build | DONE (build/pcrec-ce658cb7, sha256 f84d06e0...); main tree `testees/pcrec/list_axes.tsv` mtime unchanged (the [B80] hazard did not recur) | `a41362d` |
| 2 | read EVERY abi step 31->32->33 in `git log 6ef76820..ce658cb7` + docs; say what abi 32 is | DONE: 122 commits, two bump `PCREC_ARTIFACT_ABI` (68422ba1 [VAR] 31->32; 1e6a90b0 K64 32->33, fix in 7172f7f4); read match_api.md §6's two change-log entries, docs/spec/vars.md, known_issues K64, cycle2_admitfix_reading.md §1.8 | §0 items 1-2; testees/pcrec/CLAUDE.md "Re-pin at ce658cb7" |
| 3 | struct rx_info: does the floor stay 16? | DONE: grew by two APPENDED members; floor STAYS 16 (both sabotage arms of `check_abi_floor_refusal` pass unchanged) | §0 item 6 |
| 4 | new stamps/macros absorbed with a by-value check | DONE: no new stamp at either step; the new macros `PCREC_ERR_UNSET_VAR` (every artifact) / `RX_NVARS` (var-bearing only) asserted by value in `check_vars_surface` (4 checks); shim `rx_ctx` zeroing | `d445150` |
| 5 | re-archive the four registries, explain every delta | DONE: axes 89/32 byte-identical; definitions 50 byte-identical; limits 60 -> 62 (`PCREC_MAX_VAR_NAME_LEN` 64, `PCREC_MAX_VAR_NEST_DEPTH` 8 -- [VAR], limits.md §3.6); schema 71 -> 73 (`block var` qualified-line, `block var-unset` token -- [VAR]'s `.rxt` production; `# schema-rows:` 67 -> 69) | `a41362d`, the four headers |
| 6 | fix A's stamp move BY VALUE on the K64 forced-VM artifacts | DONE: six LEDGER rows (`email-nested-plus`, `ipv4-near-miss`, `wild-datetime-moment-iso8601`, `wild-validator-email-owasp`, `wild-validator-ipv4-owasp`, `winpath-near-miss` under `pcrec-vm`): `req_why "emitted"` (was `one-attempt`), `vm_frameless 0`, `prefilter none`, `vm_program_bytes` unmoved; plus fix A's two arms as controls keeping `one-attempt` (`email-nested-plus` under auto = EXACT hybrid; `uuid-near-miss` forced-VM = frameless) | `d445150`, `LEDGER_STAMP_CASES` |
| 7 | size books per witness, not a flat constant | DONE, measured both pins: every artifact +1001 (`B90_VAR_ABI_BLOCK`: .c +39 = 34 initializer + 5 `,vars`; .h +962), independent of `-fcomments`; the 30 existing expectations each gained that term; K64 movers +1150 (5 byte checks: 1001 + `B90_K64_BYTE_CHECK` 153 - 4) and +1578 (winpath's run check: 1001 + `B90_K64_RUN_CHECK` 581 - 4) | `a41362d`, `d445150` |
| 8 | verify "auto program-identical" with a compile-only census using program_identity.py's normalization | DONE, and it does NOT hold for six backreference patterns (§0 item 2); v1's normalization is unusable at this pair (§0 item 3) -- measured under BOTH | `304ca28`: docs/dev/measurements/2026-09-25-b90-identity-census.txt + probe |
| 9 | catalogue `[[pin_order]]` append | DONE: 3.7 -> 3.8 (MINOR), `ce658cb7` after `6ef76820` | `39626ee` |
| 10 | testees/pcrec CLAUDE.md, root CLAUDE.md pin paragraph, pcrec_references.md | DONE (references had no pin row since [B39]: added a [B90] row naming the pcrec docs this pin's absorption rests on) | `c8051f1` |
| 11 | [B88] `program_sha256` on every pcrec compile row, SAME normalization as the census, code reused | DONE -- with one necessary change: the census gained normalization **v2** (`normalize_one`, one artifact at a time) because v1 is pair-relative; the adapter IMPORTS `program_identity.program_sha256_of_files` (no re-implementation); the census uses the same function (`--normalization v2`, the default for a new file; v1 files stay `--check`-clean, version read off their first line -- re-derived `pcrec_b1885a83__6ef76820.tsv` byte-identical) | `d445150` |
| 12 | record schema minor bump; field tables; check-schema examples; bad example for a new rule | DONE as **v1.7** (§0 item 5): declaration TYPE `sha256` (X15 enforces 64 lowercase hex); record_schema.md (enum table, 4.1 history row, X15 text, §7 worked-example row); a v1.7 good example + `bad/x15-sha256-malformed.jsonl`; `make check-schema` 6 accepted / 74 rejected for the intended rule / 0 wrong | `d445150`, `c8051f1` |
| 13 | nullband reads the field FIRST, census fallback | DONE: `nullband.field_identity`/`cell_identity`; `report.py` `_build_null_band_model` asks the field first per cell, falls back to the census, NAMES a disagreement (field wins); a pair with no census but the field on both sides now gets a band; every existing report renders byte-identical (no stored record carries the field) so `REPORTER_VERSION` stays v23 | `d445150`, test `test_b88_null_band_reads_program_sha256_first` |
| 14 | a check that the field and the census agree on >=1 artifact at this pin | DONE: `check_program_sha256` -- three artifact kinds (a DFA, K64's forced-VM witness, a backreference VM): field present + 64 hex, field == the census's own v2 hash of a WITHOUT-`-fcomments` emission while the raw texts differ, three programs three hashes, and across the pair v1 `changed`/v2 `identical` on the DFA and v2 `changed` on the backreference with the seam named (10 checks) | `d445150` |
| 15 | acceptance-window draft cell list | DONE, §3 | this file |
| 16 | validation: check-schema, gen.py --check, check-interpret, check-report, targeted harness | DONE except check-report -- see §2 | §2 |
| 17 | full `make check` | OWED, manager-launched (§4) | — |

## 2. Validation (targeted; numbers)

- `make check-schema`: **6 examples accepted, 74 sabotages rejected for the
  intended rule, 0 wrong** (`x15-sha256-malformed` -> X15; check_fields
  157/25/17 agree).
- `python3 catalogue/fixtures/gen.py --check`: **243 files in 75 fixtures, ok**.
- `make check-interpret`: **169 passed, 30 FAILED -- every failure section
  3 (sidecar freshness), entirely the catalogue 3.7 -> 3.8 bump**: with
  `catalogue/rules.toml` restored to HEAD~ the same tree reads **199
  passed, 0 FAILED** (the b58/b74/b80/b84 precedent; regenerating the 30
  sidecars is the manager's merge step).
- targeted `tools/selfcheck.py` sections (in-process runner, the pin at
  ce658cb7): `check_list_axes_registry` + `_definitions_` + `_limits_` +
  `check_mechanism_stamps` + `check_deny_flag_controls` +
  `check_opt42_preempts_collapse_policy` + `check_cc_axis` +
  `check_cap_axis` + `check_noedge_axis` + `check_cflags_axis` +
  `check_emit_size_port` + `check_abi_floor_refusal` +
  `check_encoding_axis`: **202 passed, 5 failed** -- the 5 were all
  "subject files missing" (a fresh worktree; `check_manifests` generates
  them) and re-ran **59/0** after `check_manifests`; then
  `check_program_sha256` + `check_vars_surface` + `check_mechanism_stamps`
  (with the 8 new K64 ledger rows): **135 passed, 0 failed**.
- the four null-band tests (`test_b79_*` x3 + `test_b88_*`): **4/4 pass**.
- `make check-report`: RESULT BELOW (§2a).
- `python3 tools/program_identity.py --subbench capability --version 0.1
  --old b1885a83 --new 6ef76820 --check`: **re-derives byte-identical**
  (v1 read off the file header).

### 2a. check-report and the record-writing harness sections

(filled in below before handback)

## 3. DRAFT acceptance-window cell list (I-108's four predictions)

All cells are `capability@0.1` (regimes `short-subject-search` +
`large-subject-throughput`, 75 short / 3 throughput subjects), AFTER =
ce658cb7, BEFORE = the 6ef76820 records in `store/index.tsv`:

| config (testee) | AFTER testee_id | BEFORE record (store/records/capability@0.1/...) |
|---|---|---|
| `pcrec-vm` | `pcrec_ce658cb7_vm-caps-simdna` | `pcrec_6ef76820_vm-caps-simdna/capability@0.1__pcrec_6ef76820_vm-caps-simdna__budu-ryzen1600__20260923T210008Z.jsonl` |
| `pcrec-vm-in` | `pcrec_ce658cb7_vm-in-caps-simdna` | `pcrec_6ef76820_vm-in-caps-simdna/capability@0.1__pcrec_6ef76820_vm-in-caps-simdna__budu-ryzen1600__20260923T214059Z.jsonl` |
| `pcrec-auto` | `pcrec_ce658cb7_auto-caps-simdna` | `pcrec_6ef76820_auto-caps-simdna/capability@0.1__pcrec_6ef76820_auto-caps-simdna__budu-ryzen1600__20260923T200117Z.jsonl` |
| `pcrec-nocaps` | `pcrec_ce658cb7_auto-nocaps-simdna` | `pcrec_6ef76820_auto-nocaps-simdna/capability@0.1__pcrec_6ef76820_auto-nocaps-simdna__budu-ryzen1600__20260923T203241Z.jsonl` |

(The b1885a83 records -- `..._b1885a83_{auto-caps,auto-nocaps,vm-caps,vm-in-caps}-simdna__...20260923T{114747,122232,125206,133317}Z.jsonl`
-- are the "~23.1 µs" reference for prediction 2.)

Which cells test which prediction:

- **P1 -- the 5 K64 subjects answer as pcre2 on vm-caps/vm-in-caps**:
  pattern `email-nested-plus`, regime `short-subject-search`, testees
  `pcrec-vm` + `pcrec-vm-in`; subjects `sd-empty-alt-hit`,
  `sd-empty-alt-miss`, `sec-github-pat`, `v-uuid-badnibble`,
  `v-uuid-valid`. BEFORE: 5 `gave-up` (PCREC_ERR_STEPS) per testee
  (O-52). AFTER: `matched-as-expected` on all 75, the set cell RANKABLE
  (it was excluded). "0 VM steps" is not in the record (§0 item 7).
- **P2 -- the 6 forced-VM thr cells return to ~23.1 µs**: regime
  `large-subject-throughput`, testees `pcrec-vm` + `pcrec-vm-in`, patterns
  `wild-validator-email-owasp`, `winpath-near-miss`, `email-nested-plus`
  (pcrec cycle2_admitfix_reading.md §1.8's own list). BEFORE (6ef76820):
  63.1 / 68.8, 27.7 / 36.4, 7,206.9 / 7,257.4 ns (ledger
  2026-09-23-precheck-admit-after-6ef76820.md §1.1-1.2); reference
  (b1885a83): 23,200.5 / 23,118.8, 23,143.2 / 23,156.0, 23,126.7 /
  23,148.1 ns. Expected verdict: `regress` beyond the band -- the stated,
  accepted cost. By the same fix the forced-VM SEARCH cells [B84] saw
  regress should return toward b1885a83: `ipv4-near-miss` thr+srch,
  `wild-datetime-moment-iso8601` srch, `wild-validator-email-owasp` srch,
  `wild-validator-ipv4-owasp` thr+srch, on vm-caps/vm-in-caps (the §1.5
  list of that ledger).
- **P3 -- auto program-identical**: testees `pcrec-auto` + `pcrec-nocaps`,
  every pattern, both regimes. MEASURED already (compile-only): true for
  every non-backreference pattern; FALSE for the six backreference
  patterns (§0 item 2) on every config. The window's reading is the null
  band over the auto cells: `python3 tools/program_identity.py --subbench
  capability --version 0.1 --old 6ef76820 --new ce658cb7` (v2 by default;
  needs the window's ce658cb7 records) writes
  `reports/identity/capability@0.1/pcrec_6ef76820__ce658cb7.tsv`;
  PREDICTED from this lane's census: 512 rows -- identical 425 (auto-caps
  112, auto-nocaps 113, vm-caps 100, vm-in-caps 100), changed 72 (12 /
  12 / 24 / 24), refused-both 15 (4 / 3 / 4 / 4). A mismatch against
  those counts is a finding, not noise.
- **P4 -- nothing else moves**: all four testees; every cell whose v2
  identity is `identical` is a null control, and every CHANGED cell other
  than the 12 K64 rows x 2 testees and the 36 backreference rows should
  not exist (the census says none do); the D119 verdicts on the 6
  backreference patterns are the only un-predicted movers to read.

Suggested roster for the report group: the four pcrec testees at BOTH
pins (+ pcre2-jit as the answer reference for P1). This lane ran none of it.

## 4. OWED (owner, trigger)

- **Full `make check`** -- manager-launched (2026-09-25 rule). From the
  lane worktree root
  `/home/duxevents/pcrec-bench/.claude/worktrees/agent-a69c6359fb21a4aeb`:

      setsid /usr/bin/gnutimeout 5400 make check > /tmp/claude-1001/-home-duxevents-pcrec-bench/98054373-1218-4048-b7b7-c2ddd4f16eb8/scratchpad/b90_make_check.log 2>&1; echo "DONE rc=$?" >> /tmp/claude-1001/-home-duxevents-pcrec-bench/98054373-1218-4048-b7b7-c2ddd4f16eb8/scratchpad/b90_make_check.log

  (or the same with the log under `/var/tmp`). EXPECTED: check-schema
  6/74/0; check-harness all green (the prior total + 10
  `check_program_sha256` + 4 `check_vars_surface` + 8 new ledger rows);
  check-report green (98 test_report tests); check-interpret **169/30**
  with all 30 in section 3 until the sidecars are regenerated at
  catalogue 3.8. Completion line: `DONE rc=<n>`.
- **Sidecar regeneration** for catalogue 3.8 (30 sidecars) -- manager,
  at merge (precedent).
- **The pair census file** `reports/identity/capability@0.1/pcrec_6ef76820__ce658cb7.tsv`
  -- manager, after the window writes the ce658cb7 records (command in
  §3 P3).
- **plan.md rows [B90]/[B88], dev_journal, BD13's "v1.6" wording** --
  the manager's.
- **Reporter version**: kept at v23 (output byte-identical on every
  existing record). The first render that carries the new `identity from
  the records` line is the NEXT pin pair's; a bump then is the manager's
  call.
- **A note for pcrec** (outbox candidate): I-108's prediction 3 needs
  "against the abi-32 baseline" -- against 6ef76820 the [VAR] seam moves
  every backreference program.
