# lane b101repin report — RE-PIN to 02902356 (abi 33 -> 37) + the `-fno-req-byte` twin prepared

**Task**: plan row [B101] / inbox I-111. Re-pin the pcrec testees from
`ce658cb7` (abi 33) to pcrec main `02902356` (abi 37) by the
[B84]/[B90] ritual; reproduce I-111's census on our side; prepare (not
run) the [OPT-REQBYTE] twin. No `store/`/`reports/` write, no timing of
any kind.

**Branch**: `lane/b101repin` (worktree `worktrees/b101repin`), commits
`10ff1bc` (pin, four registries, `dfa_prefilter` run-pinned values),
`2c02dbc` (size books, run-pinned deny controls, the twin config +
`check_noreqbyte_testee`, census archive, catalogue 3.10), `a87af99`
(capability roster row, docs), and this report.

## 0. Findings the manager must read first

1. **I-111's bench census REPRODUCES DIGIT FOR DIGIT**, under BOTH
   identities (pcrec's raw-`.c` rule and our v2 `program_sha256`, which
   agree on every one of 1,034 rows): 650 = 403 identical / 59
   refused-both / 10 K65K66 / 6 K65K66+S1STEP6 / 110 S1BUILD / 62
   S1STEP6, zero refusal movers, no S1BUILD combined with another cause,
   and 42ee828f -> 02902356 moves nothing. **The population is NOT
   capability@0.1**: pcrec's `reqpos_census.py` `bench_pop()` is ALL 325
   `bench/*/patterns/*.rx` of this repo (altwide 33, bounded 43,
   capability 64, email 3, loglines 11, syntax 95, utf8 76) x
   {caps, nocaps}, plain form. The brief's "capability@0.1's pcrec
   configs" framing would not have reproduced it; I ran I-111's actual
   population AND capability separately (§3). No need to ask pcrec for
   their TSV.
2. **S1 (abi 36) added two new `RX_DFA_PREFILTER` VALUES and an axis
   bit that I-111 does not spell out**: `run-pinned` /
   `run-pinned-bounded` (ranked ahead of the seven old values; `rx_info.
   prefilter` mirrors them) and bit 32 `-fno-run-prefilter`. The adapter
   would have REFUSED every run-pinned artifact (closed value set + the
   `_OFFSETS` iff) -- 94 of I-111's 110 bench S1BUILD movers and 24 of
   capability's 32 are run-pinned. Fixed: `dfa_prefilter` values +2,
   `OFFSET_SET_VALUES` spans four values (a run-pinned `_OFFSETS` lists
   the run's own offsets and may scan at `0*`). I-111's "memchr-only
   prefilter -> run-pinned + an rx_ofsskip helper" for router is this.
3. **The registry's first `|`-joined deny broke a harness control.** The
   run-pinned rows carry `PCREC_NO_OFFSET_SKIP|PCREC_NO_RUN_PREFILTER` /
   `16|32` / `-fno-offset-skip|-fno-run-prefilter` (pcrec registry.md's new
   column rule); `check_deny_flag_controls` passed the whole cell as one
   flag to pcrec (refused as an unknown option). Fixed: the cells are split
   on `|`, an optional eighth row element names the spelling, and the
   registry agreement reads the carrying row whose `stamp_value` the arm
   reads. Two new controls on `abc`: `-fno-run-prefilter` -> `offset-set`
   `0,1*`; `-fno-offset-skip` -> `memchr` (both: `req_why` dominated ->
   emitted).
4. **The `-fno-req-byte` twin is NOT a pure pre-check twin on every
   cell** (measured, §4): where the default artifact's prefilter is S1's
   `run-pinned[-bounded]` (built on the run), the denial also drops the
   prefilter to the pre-S1 form -- **github-pat** run-pinned-bounded
   `0,3..10` -> offset-set-bounded `0,6*`, **router-prefix-order**
   run-pinned -> memchr. So I-111's "github-pat/uuid-grok may read
   identical" holds for **uuid-grok** (program-identical) and **fails for
   github-pat** (a different program with a different prefilter).
   **floor-byte** is also program-identical across the twin (its byte is
   `dominated`, nothing emitted). And bit 30 is NOT in pcrec's
   strategy_denials mask: every denied artifact carries `rx_info.flags =
   1073741824` (bit 31, `-fno-req-run`, IS masked: 0) -- a one-constant
   `.so` difference even on program-identical cells.
5. **A non-abi registry move**: `list_schema.tsv` 73 -> 78 from pcrec's
   [FINDINGS] B0 `.rxt` rows (merge 54bb1159, `rxt_schema.def` /
   `rxt_source.c`, landed between 0bb87eda and 42ee828f; +6 / -1 / 5
   re-worded). Not in I-111's text; no emitter change; nothing here reads
   the file.
6. **The shim floor STAYS 16**: `struct rx_info` byte-identical (diffed
   on `abc`); no new stamp at any of the four steps.

## 1. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 1 | `pin.sh 02902356`, build | DONE (`build/pcrec-02902356`, via `git fetch origin` in ~/pcrec -- the sanctioned fetch, nothing else written there); scratch builds 27a63314 / 0bb87eda / 42ee828f under `/var/tmp/b101scratch` (never pinned) | `10ff1bc` |
| 2 | read pcrec's changes for EVERY abi step 34-37 | DONE: 135 commits; `PCREC_ARTIFACT_ABI` moves only in the three merges (33->35 in 27a63314, K65+K66 together; 35->36 0bb87eda; 36->37 42ee828f); read each merge's `src/` diff + match_api.md's abi change-log entries 34-37, §6.3's nine-value table, registry.md's `|` rule; the other in-range `src/` edits are a `definitions.c` comment and [FINDINGS] B0's `.rxt` parser rows | §0, testees/pcrec/CLAUDE.md "Re-pin at 02902356" |
| 3 | four registry surfaces archived and diffed | DONE: axes 89->91/32 (two run-pinned rows), definitions 50 and limits 62 byte-identical, schema 73->78 ([FINDINGS] B0, §0.5); `--list-syntax` byte-identical to ce658cb7 | `10ff1bc`, the four headers |
| 4 | shim floor: does any step add an rx_info field? measure | DONE: none; struct byte-identical; floor STAYS 16; `check_abi_floor_refusal` 5/5 | §0.6 |
| 5 | every stamp by value incl. `dominated` on the S1BUILD movers | DONE: six new LEDGER rows (github-pat `run-pinned-bounded`/`0,3,4,5,6*,7,8,9,10`/dominated; uuid-grok `offset-set`/dominated; router `run-pinned`/`0*,1,2,3,4`/dominated; tag-pair-match K65+step6, dup-param-detect K65, nested-comment-rec step6 -- all `emitted`) + the two run-pinned deny controls | `2c02dbc` |
| 6 | size books MEASURED per witness | DONE at all FIVE builds with the adapter's own argv and port (`probe_b101_sizes.py`); no flat term this pin; `B101_K65_SET_REST_121`=245, `_46`=244, `B101_STEP6_RUN_AT0`=-18, `_AT1`=-41; five pre-existing expectations moved (x[ac]y, x[@`]y +245; pfx3-256 -18; email-owasp +244; winpath -41), every other asserted witness 0 | `2c02dbc`, docs/dev/measurements/2026-09-26-b101-sizes.txt |
| 7 | catalogue `[[pin_order]]` append | DONE: 3.9 -> 3.10 (MINOR), `02902356` after `ce658cb7` | `2c02dbc` |
| 8 | testees/pcrec config pin bump | DONE `pin = "02902356"` | `10ff1bc` |
| 9 | every CLAUDE.md that states the pin | DONE: root CLAUDE.md, testees/CLAUDE.md, testees/pcrec/CLAUDE.md (table + re-pin section), tools/CLAUDE.md, docs/dev/measurements/CLAUDE.md, bench/capability/CLAUDE.md, scripts/CLAUDE.md (cell-length estimate), docs/dev/pcrec_references.md ([B101] row, now the CURRENT pin) | `a87af99` |
| 10 | reproduce I-111's census with program_sha256; digit-for-digit or the exact disagreement | DONE -- AGREES digit for digit (§0.1, §3) | docs/dev/measurements/2026-09-26-b101-census.txt + probe_b101_census.py |
| 11 | decide the twin's shape; if a pinned deny testee, ADD it with frozen-id controls | DONE: `pcrec-auto-noreqbyte` (§4) -- DENY_FLAGS word `noreqbyte` after `noclsfold`; id `pcrec_02902356_auto-caps-simdna_noreqbyte`; `check_noreqbyte_testee` (6) incl. pcrec-auto's frozen shape; `check_encoding_axis` (frozen four-part renderer over every pcrec config) 7/7; added to capability's `ext bench` roster with pcrec-auto's tokens (refusal sets measured identical) | `2c02dbc`, `a87af99` |
| 12 | the twelve landing-bar cells' REQ stamps under both arms, by value | DONE, §5 | docs/dev/measurements/2026-09-26-b101-twin-stamps.txt |
| 13 | targeted selfcheck functions (each <4 min) | DONE, §2 | — |
| 14 | full `make check` | OWED, manager-launched (§6) | — |
| 15 | no timing measurement | honoured: every probe is emit-only; no `quick`/`run` cell was executed | — |

## 2. Validation (targeted; numbers)

- `check_manifests` + the three diffed registries: **32/0** (after the
  re-archive).
- First pass after the pin bump (before fixes): `check_abi_floor_refusal`
  5/0, `check_mechanism_stamps` 118/**5** (the five size moves of §1.6),
  `check_program_sha256` 9/0, `check_vars_surface` 3/0,
  `check_deny_flag_controls` 15/**1** (§0.3), `check_opt42_...` 2/0,
  `check_emit_size_port` 11/0, `check_cc_axis` 18/0, `check_cap_axis`
  13/0, `check_noedge_axis` 10/0, `check_cflags_axis` 7/0,
  `check_encoding_axis` 7/0 -- 217/6.
- After the fixes: `check_mechanism_stamps` **129/0** (+6 ledger rows),
  `check_deny_flag_controls` **17/0** (+2), `check_noreqbyte_testee`
  **6/0** (new), `check_encoding_axis` **7/0**,
  `check_list_axes_registry` **2/0** -- 161/0.
- After the roster row: `check_capability_policy` +
  `check_capability_policy_noop_elsewhere` + `check_rxt_source_load` +
  `check_rxt_export` + `check_describe_schema_shape` **35/0**;
  `bench/capability/gen_patterns.py --check` rc 0.
- `make check-schema`: 6 accepted / 74 rejected for the intended rule / 0
  wrong. `catalogue/fixtures/gen.py --check`: 251 files in 77 fixtures, ok.
- `make check-interpret`: **174 passed, 36 FAILED -- all 36 section 3
  (sidecar freshness)**; with `catalogue/rules.toml` restored to the
  branch base the same tree reads **210/0** -- entirely the 3.9 -> 3.10
  bump (the b58/b74/b80/b84/b90 precedent; regenerating the 36 sidecars
  is the manager's merge step).
- NOT run here: `make check-report` (the reporter is untouched; it renders
  `dfa_prefilter` values generically) -- inside the owed full check.

## 3. The census (compile-only; docs/dev/measurements/2026-09-26-b101-census.txt)

Five builds, emits without `-fcomments`, 5 workers, 5,170 emits.

**I-111's population** (§0.1): identical 403, refused-both 59, K65K66 10,
K65K66+S1STEP6 6, S1BUILD 110, S1STEP6 62 -- = I-111's bench column
exactly. S1BUILD transitions: 56 memchr->run-pinned, 32 offset-set->
run-pinned, 14 offset-set kept, 4 offset-set-bounded->run-pinned-bounded,
2 offset-set-bounded kept, 2 memchr-bounded->run-pinned-bounded; every one
`req_why` emitted -> dominated. `req_why` over the 591 compiled: base
none 257 / emitted 238 / dominated 68 / one-attempt 28 -> tip 257 / 128 /
178 / 28.

**capability@0.1** (our three distinct compiled configs x 64 x 2 forms,
384): identical 277, refused 11, K65K66 24, K65K66+S1STEP6 14, S1BUILD 32,
S1STEP6 26; zero refusal movers; S1BUILD never on vm-caps. Per config:
auto-caps 96 / 4 / 4 / 16 / 4 / refused 4; auto-nocaps 97 / 4 / 4 / 16 / 4
/ 3; vm-caps 84 / 16 / 6 / 0 / 18 / 4. **This is the predicted null band
for the window's ce658cb7 -> 02902356 capability pair** (vm-in-caps =
vm-caps). Movers by pattern: the S1BUILD set under auto is file-ext-order,
keyword-prefix-order, router-prefix-order, wild-secrets-github-pat,
wild-secrets-slack-webhook-url, wild-semdiv-altorder-foo-foobar-rustregex,
wild-semdiv-dollar-trailing-newline-pcre2, wild-validator-uuid-grok (each
S1STEP6 or K65K66+S1STEP6 under vm); K65 hits balanced-parens-rec,
dup-param-detect, tag-*, and under vm codegrammar-flat/-xflag,
mojibake-curly-quote, wild-logparse-syslogbase-expanded,
wild-validator-email-owasp (the archive lists every row).

## 4. The twin: decision and shape

**A pinned deny testee is the right shape**, the [B37]/[B39]
noisland/noclsfold precedent: [OPT-REQBYTE] is in every pin since
8d716693, so only a same-pin twin isolates it; the window's records must
land in `store/` beside `pcrec-auto`'s and be read by the reporter as a
pair (a scratch `pcrec-local` twin never enters the store or a ranking).
Added: `[testees.pcrec-auto-noreqbyte]` (`--features all -fno-req-byte`),
DENY_FLAGS `("-fno-req-byte", "noreqbyte", ...)` after `noclsfold`, id
`pcrec_02902356_auto-caps-simdna_noreqbyte`, capability roster row
(without it every requires-tagged pattern would be fail-closed
`unsupported-by-declaration` for the twin). MEASURED over capability's 64
x 2: the twin's refusal set equals pcrec-auto's (4 refused both, 0
movers); 88/124 compiled artifacts program-identical, 36 changed.

Caveats for the window (§0.4): the pair is not a pure pre-check twin on
github-pat and router-prefix-order (the prefilter moves too), and the
`.so` differs by the `rx_info.flags` constant everywhere.

## 5. Pre-window facts: the twelve landing-bar cells (capability@0.1, `pcrec-auto` flags, plain form -- both regimes compile the plain form)

`req_why / req_byte / req_run / dfa_prefilter (offsets)`; engine in
brackets; "id" = the two 02902356 arms program-identical (v2).

| cell (I-111 class) | ce658cb7 default | 02902356 default | 02902356 `-fno-req-byte` | since ce658cb7 | twin |
|---|---|---|---|---|---|
| wild-secrets-username-password-pair/thr (IMPROVE) [vm] | emitted/61/none/byte-class | emitted/61/none/byte-class | none/none/none/byte-class | unmoved | differ |
| wild-logparse-winpath-grok/thr (IMPROVE) [vm] | emitted/92/none/byte-class | emitted/92/none/byte-class | none/none/none/byte-class | unmoved | differ |
| tag-depth3-bound/thr (IMPROVE) [vm, no DFA scan] | emitted/60/3c2f@0/- | emitted/60/3c2f@0/- | none/none/none/- | K65K66+S1STEP6 (+244, -18) | differ |
| dup-param-detect/thr (IMPROVE) [vm, no DFA scan] | emitted/38/none/- | emitted/38/none/- | none/none/none/- | K65K66 (+244) | differ |
| tag-pair-match/thr (IMPROVE) [vm, no DFA scan] | emitted/60/3c2f@0/- | emitted/60/3c2f@0/- | none/none/none/- | K65K66+S1STEP6 (+244, -18) | differ |
| floor-byte/thr and /srch (DO-NOT-REGRESS) [dfa] | dominated/126/none/memchr | dominated/126/none/memchr | none/none/none/memchr | unmoved | **id** |
| float-literal-bound/thr (DNR) [vm] | emitted/46/none/byte-class | emitted/46/none/byte-class | none/none/none/byte-class | unmoved | differ |
| nested-comment-rec/thr (DNR) [vm, no DFA scan] | emitted/42/2a2f@0/- | emitted/42/2a2f@0/- | none/none/none/- | S1STEP6 (-18) | differ |
| wild-secrets-github-pat/thr (DNR) [vm hybrid] | emitted/95/6875625f7061745f@3/offset-set-bounded (0,6*) | **dominated**/95/same/**run-pinned-bounded (0,3,4,5,6*,7,8,9,10)** | none/none/none/**offset-set-bounded (0,6*)** | S1BUILD (-489) | differ (prefilter too) |
| wild-validator-uuid-grok/thr (DNR) [dfa] | emitted/45/none/offset-set (0,8*,13) | **dominated**/45/none/offset-set (0,8*,13) | none/none/none/offset-set (0,8*,13) | S1BUILD (-131) | **id** |
| router-prefix-order/thr (timed) [dfa] | emitted/47/2f75736572@0/memchr | **dominated**/47/same/**run-pinned (0*,1,2,3,4)** | none/none/none/memchr | S1BUILD (-184) | differ (prefilter too) |

Every I-111 per-cell "what moved since ce658cb7" claim is confirmed by
the attribution builds. Twin predictions to file before the window (the
manager's): floor-byte and uuid-grok are program-identical twins -> a
same-pin noise reading; github-pat's and router's twin Δ includes S1's
prefilter change, not the pre-check alone.

## 6. OWED (owner, trigger)

- **Full `make check`** -- manager-launched (2026-09-25 rule). From
  `/home/duxevents/pcrec-bench/worktrees/b101repin`:

      setsid /usr/bin/gnutimeout 5400 make check > /var/tmp/b101scratch/b101_make_check.log 2>&1; echo "DONE rc=$?" >> /var/tmp/b101scratch/b101_make_check.log

  Completion line `DONE rc=<n>`. EXPECTED: check-schema 6/74/0;
  check-harness all green (the prior total + 6 mechanism ledger rows + 2
  deny rows + 6 `check_noreqbyte_testee`); check-report green (untouched
  reporter); check-interpret **174/36**, all 36 section 3 until the
  sidecars are regenerated at catalogue 3.10 (so `make`'s exit is 2 from
  those named failures alone).
- **Sidecar regeneration** for catalogue 3.10 (36 sidecars) -- manager, at
  merge.
- **The window** (not tonight's lane): capability@0.1 x {pcrec-auto,
  pcrec-auto-noreqbyte} at 02902356 on I-111's twelve cells, predictions
  filed first (§5 gives the stamp facts), plus the cross-pin
  `program_identity.py --old ce658cb7 --new 02902356` file once records
  exist (predicted counts in §3). An answers-only smoke of the twin was
  NOT run (brief: no timing of any kind); the twin's answer identity is
  the window's first check.
- **plan.md [B101] row, dev_journal, outbox note to pcrec** (census
  reproduced; the twin is not pure on run-pinned cells; bit 30 unmasked in
  `rx_info.flags`) -- the manager's.
- Scratch builds `/var/tmp/b101scratch/pcrec-{27a63314,0bb87eda,42ee828f}`
  (~3 x build trees) can be deleted once the census is accepted.
