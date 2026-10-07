# lane b124prep report — RE-PIN PREP to 5ff21faca (abi 59 -> 65)

**Task**: plan row [B124] readiness items (1)-(4), inbox I-128..I-132. Re-pin
pcrec from `c4c70f2c` (abi 59) to `5ff21faca` (lane/k93tri's tip: pcrec main
445f2ffc1 + the K93/K95 fixes). A PREP: inbox I-133 names the final pin. No
store/ write, no timing; the one reports/ write is the 75 sidecars'
catalogue-version lines (see §8).

**Branch**: `lane/b124prep` in `worktrees/b124prep` (the boilerplate's
`lane/<lane>` convention; the brief said `b124prep`, and every earlier lane
branch is `lane/...`). Not merged, not pushed. Build:
`build/pcrec-5ff21faca/` (main tree, `pin.sh 5ff21faca`, 2026-10-07 02:57).
Scratch build for the census layer: `/var/tmp/b124scratch/pcrec-445f2ffc1`
(`pin.sh --build-root`, 142 MB, deletable).

## 1. The six abi steps (read in pcrec's match_api.md §6, not only the inbox)

| abi | step | surface here |
|---|---|---|
| 59→60 | [K82] (A)+(C) | `req-admit` first-match table on `--list-axes` (RX_REQ_WHY's four tokens in the registry for the first time); `set-leads` row, bit 45 `-fno-req-set-lead`, moves NO stamp. (C): NONE-pick prices size, moves `RX_REQ_RUN @idx` under `-e utf8`, no flag. **Not in any inbox note** |
| 60→61 | [K82] (B) | NEW stamp `RX_REQ_HANDOFF` (every artifact; decimal K or `none`); axis `req-use`, bit 46 `-fno-req-handoff`. **Not in any inbox note** |
| 61→62 | [START-SET] stage 2 | NEW stamp `RX_VM_START_SCAN`; `prefilter` row `first-class` (stamp_macro RX_VM_START_SCAN); bit 47 `-fno-start-set` |
| 62→63 | [MEMFN] R4a′ | NEW stamps `RX_MEMFN_FORMS` / `RX_MEMFN_LIBC` |
| 63→64 | [START-SET] stage 3 | `RX_DFA_PREFILTER` + `first-memchr-bounded` / `first-class-bounded` (two `prefilter` rows) |
| 64→65 | K92 | derived `.flags` mask; no stamp |

Also at abi 65: [MEMFN] R4c (`memfn-simd` axis, bits 48/49) and K93/K95 (no
abi event). `struct rx_info` gains NO member (match_api.md at every step;
MEASURED: the `.c`/`.h` diff of `abc` is stamp lines + abi digits only) —
**shim floor STAYS 16**.

## 2. Readiness items -> commits

| item | status | commit |
|---|---|---|
| (1) I-128/I-129: every `--list-axes` reader selects the MAIN table | DONE: `adapter.registry_main_lines()` / `registry_sections()`; `registry_rows()` stops at the first `#section`; `check_list_axes_registry` counts main-table rows only and parses every section; a SYNTHETIC 0-row section and a 1-row section (different column count) parse, the main table not growing. Audited readers: `registry_rows` (3 selfcheck callers + `registry_check`), the archive diff, the counts. The archived `probe_o38_*` measurement scripts read `--list-axes` for a flag name only — left as archived probes | 4b054e3, 0e2ecdc |
| (2) I-130 abi 62: `RX_VM_START_SCAN` read; `-fno-start-set` a DENY_FLAGS control; ordinal audit | DONE: shim/driver/adapter read it (STAMP_SCOPE `every`, closed enum `none`/`first-class`, `REGISTRY_STAMP_PAIRS` with `none` as an outcome value). Ordinal audit: NO reader keys on the `order` column; ONE reader keyed on "the first `-f` row of an axis" (`check_deny_flag_controls`), which would have mis-read `-fno-start-set` (rows 5-7, below `-fno-offset-skip|-fno-run-prefilter`) — now spelling-keyed. DENY_FLAGS `nostartset` + two DENY_CONTROLS rows (VM + DFA hat) | 4b054e3, 0e2ecdc |
| (2) I-130 abi 63: `_MEMFN_FORMS`/`_LIBC`; size books | DONE (§5) | 4b054e3, 0e2ecdc |
| (3) I-131 abi 64: the closed enum learns `first-memchr-bounded`/`first-class-bounded` | DONE (`dfa_prefilter` values + description); `registry_check` both ways green | 4b054e3 |
| (4) I-132 abi 65 K92 | DONE: confirmed by value (§4); no adapter reader depends on `.flags` under those flags | 0e2ecdc |
| full re-pin ritual: build, registries x4, catalogue append, CLAUDE.md, census | DONE (§3, §6, §8) | 4b054e3, be078fa, the census/docs commit |
| `pcrec-auto-nostartset` / `pcrec-vm-nostartset` | DONE by the [B108]/[B120] precedent (flag in `flags`, `nostartset` appended LAST in DENY_FLAGS, capability roster rows + `patterns.rxt` regenerated). Derived ids `pcrec_5ff21faca_{auto,vm}-caps-simdna_nostartset` | 4b054e3 |
| the other two new flags | `-fno-req-set-lead` (`noreqsetlead`) and `-fno-req-handoff` (`noreqhandoff`) as DENY_FLAGS entries ([B122] precedent: every new flag gets one); NO testees for them | 4b054e3 |
| `make check` GREEN | see §7: everything except `check_expectations` run by this lane, 638/4 + check-interpret 249/0 + schema/upstream OK; the 4 reds are three ENVIRONMENTAL (pruned pin builds, red on master too) and one load-induced (re-run green alone); the full `make check` is OWED to the manager | — |

## 3. Registries

`--list-axes` MAIN table 119/41 → **131/44**: `prefilter` 9 → 12 rows (the
three [START-SET] rows at orders 5-7, old 5..9 now 8..12), `req-admit` 5,
`req-use` 2, `memfn-simd` 2; every other row byte-identical. Then
`#section memfn` with **0 rows** (I-129's first carrier 5328a87d is an
ancestor). `--list-definitions` 75, `--list-limits` 72, `--list-schema` 79:
**BYTE-IDENTICAL** to the c4c70f2c archives. `--list-syntax` byte-identical
to c4c70f2c's, so it carries the same two pre-existing seed deltas
(`\p{L}`/`\P{L}` built, `(*UCP)a`); no re-seed was done.

## 4. Predictions confirmed or refuted, by value

- I-130 (1) "every VM artifact gains `RX_VM_START_SCAN`": **narrower than
  measured**. It is on EVERY artifact, `none` on every DFA artifact and
  hybrid (match_api.md §6.3 says the same: "on EVERY artifact pcrec emits").
  Declared scope `every`.
- I-130 (1) the `first-class` row at ordinal 5, old 5..9 → 6..10: true at
  abi 62. At this pin (abi 64, two more hat rows) `first-class` is order 7
  and the old rows are 8..12, as I-131 said.
- I-130 (2) MEMFN: `RX_MEMFN_FORMS "none"` on all 1,277 compiling census
  rows. `-fno-memfn-simd` program-identical to default (two witnesses). Size
  = the two lines: `RX_MEMFN_FORMS "none"` 30 B, `RX_MEMFN_LIBC "<x>"` 29 B +
  the token's extra length.
- I-131: the two values and two rows CONFIRMED. `-fno-start-set` denies the
  DFA hat too. Witnesses `\bq\w*z` (first-memchr-bounded) and `\b\d+x`
  (first-class-bounded) go back to byte-class-bounded, and the denied
  program equals c4c70f2c's.
- I-132 K92: CONFIRMED. On `abc`, `-fno-size-term` `.flags` 262144 → 0 and
  `-fno-scan-edge` 2097152 → 0. On the bench, the scan-edge deny row's
  denied arm is −6 B.
- pcrec k93fix_report §5 "Bench: 0 movers": CONFIRMED on the whole
  1,380-row population. No changed row differs between the tip and main
  445f2ffc1. That includes both (?R) witnesses, balanced-parens-rec and
  rec-r-uc, whose only movement is the VM hat.
- pcrec's K82 (A) mover list (7 bench patterns, 28 artifact-configs):
  CONFIRMED exactly. K82 (C) "alt-shared-char (4)": CONFIRMED exactly.

## 5. Size books (`tools/selfcheck.py`), measured not assumed

- `B124_STAMP_LINES = 121`: the four new lines at `none` (30 + 32 + 30 + 29).
- `RX_MEMFN_LIBC`'s token adds more: `B124_LIBC_ONE_CALL` = 2 for
  `memchr`/`memcmp`, `B124_LIBC_TWO_CALLS` = 9.
- `B124_VM_START_SET = 7 + 1804` on every `first-class` VM artifact. The
  1,804 B splits into a 256-entry table (1,468 B, excluded from code bytes)
  and two seek loops (336 B). The same on every witness, one start byte or
  many. `B124_VM_START_SET_CODE = 7 + 336`.
- `vm_program_bytes` does NOT move: the seek sits in the search prologue.
- `B124_K92_FLAGS_SCAN_EDGE = -6`.
- github-pat +178 = the handoff, measured exactly against its own
  `-fno-req-handoff` compile.
- 36 STAMP/LEDGER/DENY rows re-measured. The ledger movers are loglines
  kv-quoted and bignum (byte-class-bounded → first-class-bounded; kv-quoted
  `req_handoff "32"`) and uuid's `-fno-offset-skip` deny arm, which now
  lands on the DFA hat.

## 6. Compile-only census (`docs/dev/measurements/2026-10-07-b124prep-census.txt`)

Same population as [B122]: 1,380 rows.

**Result: 561 identical / 716 changed / 103 refused-both / 0 refusal movers
/ 0 K93-layer movers.**

How the 716 changed rows split:
- 712 are restored to c4c70f2c's v2 program by the new denials: start-set
  alone 596, req-handoff 86, req-set-lead 6, all three together 24.
- 4 are [K82] (C): utf8 alt-shared-char.

Facts for tonight's window:
- The VM hat fires on 544 of 640 compiling forced-VM rows, and on 34 auto
  rows that select a non-hybrid VM.
- The DFA hat fires on 36 auto rows.
- `wild-secrets-aws-access-key-id` (capability and litrun, both forms) also
  flips `req_why` emitted → dominated under the DFA hat.
- The handoff is non-none on 98 auto rows and 0 forced-VM rows.
- **Give-up caveat for the window**: on a VM artifact, `-fno-start-set` can
  turn the default's answer into a give-up. The direction is never the
  reverse (match_api.md §3.1; pcrec's own `(?=(?:a|b|x)*c)x` under
  `budget frames=8`). A `gave-up` row on a nostartset arm that is `matched`
  on its sibling is this mechanism, not a regression.

## 7. Validation run by this lane (load 1-5, all compile-only or smoke)

- `check_list_axes/definitions/limits_registry`: 7/0 (incl. the two
  `#section` checks).
- `check_mechanism_stamps` + `check_deny_flag_controls`: **153/0**.
  `check_b124_stamps`: **12/0**. `check_b122_round1_stamps`: 7/0.
- `make check-schema`: 6 accepted / 74 rejected / 0 wrong.
- `make check-interpret`: **249/0**. `make check-upstream`: OK.
- The rest of `check-harness` minus `check_expectations`:
  `/var/tmp/b124_harness.log` (completion line `DONE rc=<n>`); results in
  §7a.
- Three REDS, all ENVIRONMENTAL and red on master too: the pin builds they
  need were pruned from `build/` (the 44th session's disk prune; the disk
  is at 87% again) -- see §7a.
- A quoting slip in four new METADATA_DECL lines was caught by KB-21's
  describe sweep and the pcrec-local quick cell. It is fixed (commit after
  0e2ecdc) and both checks re-ran green.

### 7a. check-harness minus check_expectations

Every `main()` function but `check_expectations`, one process, 03:33-03:47
EDT (`/var/tmp/b124_harness.log`, `DONE rc=0`): **638 PASS / 4 FAIL**. None
of the four is this re-pin's:
- `capability: gen_patterns.py --check`, `KB-35 build_census` and
  `b108 acceptance mover` are the ENVIRONMENTAL reds: they need the pruned
  builds `pcrec-cd371441`, `pcrec-25b1984f` and `pcrec-751b9c6d`. Fix:
  `pin.sh` each (~120 MB each, disk at 87%), or accept them.
- `a real quick cell on bench/email writes a MEASURED scratch record` read
  `inconclusive-load` while this lane's own census and check jobs had the
  load at ~5. RE-RUN alone at load 0.75 (`check_pcre2_dfa`): PASS,
  `status=measured`; that function 12/0.

## 8. The catalogue and the one reports/ write

Catalogue **3.15** (`[[pin_order]]` + `5ff21faca`, MINOR). §3.3 requires
every committed sidecar to carry the catalogue version, so the 75
`reports/*.interpretation.md` sidecars' two version lines moved 3.14 → 3.15.
Nothing else moved; `check-interpret` 249/0 confirms freshness. This is
committed separately as be078fa. Dropping it would turn check-interpret red.

## 9. When the final pin differs from 5ff21faca: what to re-do

`lane/axtri` (the likely addition) touches NO `src/`, `lib/`, `cli/` or
`memfn/` file (`git diff --stat` empty). So a main of 5ff21faca + axtri
should be program-identical, and the delta is mechanical:

1. `pin.sh <final>`, then `configs.toml` `pin = "<final>"` (testee ids
   change with it).
2. Re-archive the four registries and diff them. Expected byte-identical
   below the header; update the four headers' pin/commit lines.
3. `catalogue/rules.toml`: REPLACE `"5ff21faca"` with the final pin in
   `[[pin_order]]` and in the 3.15 changelog line. No version bump needed if
   it lands in the same merge; otherwise 3.16 + sidecars.
4. Check `rx_info.abi` is still 65. If it moved, read the new §6 entries.
5. Re-run the census with `NEW = "<final>"` (or diff the tip's v2 hashes:
   expect 0 changed vs 5ff21faca), `check_mechanism_stamps`,
   `check_deny_flag_controls`, `check_b124_stamps` and the registry checks.
6. Update the pin mentions: root CLAUDE.md, testees/pcrec/CLAUDE.md,
   pcrec_references.md, catalogue/CLAUDE.md, the census archive name/header,
   and the `[B124]` comments in configs.toml and gen_patterns.py.
7. If K93's final form differs from k93tri, re-check bench movers: 0 at
   this tip.

## 10. OWED

- **Full `make check` — the manager launches it.** It runs longer than
  4 minutes (`check_expectations` alone is ~20 min).

      cd /home/duxevents/pcrec-bench/worktrees/b124prep
      setsid /usr/bin/gnutimeout 5400 sh -c 'make check > /var/tmp/b124_makecheck.log 2>&1; echo "MAKECHECK_RC=$?" >> /var/tmp/b124_makecheck.log' < /dev/null > /dev/null 2>&1 &

  Completion line: `MAKECHECK_RC=<n>`. Expected: red only on the three
  environmental checks of §7a unless their pins are rebuilt
  (`pin.sh cd371441 25b1984f 751b9c6d`, one at a time).
- plan.md / dev_journal.md / wake.md: the manager's.
- Reporter clauses for the new stamps (`start=`-style for vm_start_scan /
  handoff): not asked for, not done.
