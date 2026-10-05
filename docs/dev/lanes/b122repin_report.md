# lane b122repin report — RE-PIN to c4c70f2c (abi 50 -> 59)

**Task**: plan row [B122] / inbox I-127. Re-pin pcrec from `fc719ca4`
(abi 50) to `c4c70f2c` (abi 59), pcrec's [OPTLOOP] round 1, the [B118]
ritual. No store/ or reports/ write beyond the catalogue's sidecar
version lines, no timing.

**Branch**: `lane/b122repin`. The harness isolated this agent in
`.claude/worktrees/agent-a353755085f3282ad` (not `worktrees/b122repin`;
every git op outside it was refused), so the branch lives there. WIP
commits db83880 .. (this report's commit). Build: `build/pcrec-c4c70f2c/`
(main tree, via `pin.sh c4c70f2c`, started 23:36 EDT right after
`r1gate.log` printed `ALL_DONE Sun Oct 4 11:36:03 PM EDT 2026`).

## 1. The nine abi steps (read in pcrec's source and match_api.md §6, not
assumed from I-127's four)

| abi | step | surface here |
|---|---|---|
| 50→51→52→53 | [CLS-TREE] S2, three events (1c12395f) | VM byte classes chosen by the kit's ROWS (default-position mover: a wide class that is one interval ≤ U+00FF, utf8 `cls-boundary-range`/`cls-neg-allhigh` forced-VM); `RX_DFA_SCAN_EDGE` gains `kit`/`fold` (only at `--tune=-2/-1`, never at our default); the scan-edge RANGE test respelled `(unsigned)(b - lo) <= span u` (−4 B per site) |
| 53→54 | K79 + K80 | K79: selection at a canonical 2-byte prefix — a NO-OP here (every exec is `-p rx`, grep-checked); K80: `#define PCREC_RX_ABI_H 59` behind a mixed-abi `#error` (the shim compiles one artifact per TU, never trips it) |
| 54→55 | K78 | DFA dead-group fill moved to the success paths (census mover: email `factored` auto) |
| 55→56 | [OPT-HYB-RESEED-FORM] A1 | `RX_VM_RESEED "anchored"` on a start-anchored hybrid; artifact == its `-fno-hyb-reseed` one (whose stamp ALSO reads `anchored`) |
| 56→57 | [OPT-VEDGE] `-fno-view-edge` (bit 42) | moves the existing `RX_DFA_SCAN_EDGE` (`(?:[a-z]{0,64})\z`: none → range) |
| 57→58 | [OPT-LITSCAN] S4 C1 `-fno-run-overlap` (bit 43) | NEW stamp `RX_RUN_WORDS` (every artifact, a count) |
| 58→59 | S4 C3 `-fno-req-run-fold` (bit 44) | `RX_REQ_RUN` gains `/mask`; `RX_REQ_BYTE` may read `none` beside `RX_REQ_WHY "emitted"` |

`struct rx_info` gains NO member (MEASURED: `abc`'s struct block
byte-identical to fc719ca4's; match_api.md says so at each step) — **shim
floor STAYS 16**.

## 2. Code changes

- `testees/pcrec/shim.c` / `driver.c`: `pb_has_run_words`/`pb_run_words`,
  `info run_words`.
- `testees/pcrec/adapter.py`: `run_words` METADATA_DECL + INT_PAIRS +
  STAMP_SCOPE ("every", 58); `vm_reseed` values + `anchored`;
  `dfa_scan_edge` values + `fold`/`kit`; **rule 12 (req_why iff) widened at
  abi ≥ 59** to "none iff req_byte AND req_run none" — a real finding:
  without it every caseless pattern (`(?i)abc`: req_byte none, req_why
  emitted) raises an AdapterError at compile; three DENY_FLAGS
  (`noviewedge`, `norunoverlap`, `noreqrunfold`). No new testee.
- `tools/program_identity.py`: v2 rule 2 also drops K80's three-line
  guard (it carries the abi literal; otherwise every v2 hash reads
  `changed` across any abi step; pre-54 artifacts unaffected).
- `configs.toml` pin; four registry archives; catalogue 3.14
  (`[[pin_order]]` + `c4c70f2c`) and the 67 sidecars' two version lines
  (`make check-interpret` 241/0 confirms freshness).

## 3. Registries

`--list-axes` 108/38 → **119/41** (+`run-overlap` 4 rows, +`req-run-fold`
2, +`view-edge` 2; `scan-body` 4→6 with `fold`/`kit`; `hyb-reseed` 5→6
with `anchored`; `lit-run`/`req-run` order-1 text re-worded).
`--list-limits` 70 → **72** (`PCREC_MIN_REQ_RUN_BITS` 16,
`PCREC_MAX_REQ_RUN_POS_SET` 2; `PCREC_MAX_REQ_RUN_EMIT` unit
bytes→positions). `--list-definitions` 75 and `--list-schema` 79
**byte-identical**. All diffed line for line; `check_list_*_registry`
green.

## 4. Stamps by value and the deny controls

`check_b122_round1_stamps` (new, 7/7): `abc` run_words 1 (DFA run term),
`abcde --engine=vm` run_words 2 / program 258→316, `(?i)abc` both engines
`414243@1/dfdfdf` + req_why emitted, `^(?>ab*)c` anchored, the `\z` view
edge `range` — and for each, the **deny arm's v2 program identity equals
the fc719ca4 artifact** while the default's differs (A1: default ==
fc719ca4's `-fno-hyb-reseed`), plus the K80 guard emitted and dropped by
v2. Three new DENY_CONTROLS rows (registry-read spellings).
`check_mechanism_stamps` + `check_deny_flag_controls`: **150/0**.

## 5. Size books — measured, not assumed

`B122_FLAT_TERM = 224` on every artifact (K80 guard 201 + `RX_RUN_WORDS 0`
line 23; MEASURED exactly on DFA/VM/hybrid witnesses); `B122_RANGE_SITE =
4` subtracted per scan-edge range site (`[a-z]+@[a-z]+`: 224 − 6×4 = 200);
per-witness residuals where C1/C3 write real code: `(?i)abc` forced-VM
+1106 (C3 masked pre-check), `x[ac]y` +321 / `` x[@`]y `` +704 (C3
one-bit hulls), router-prefix-order +138, github-pat +148, the altwide
VM islands +4,626..+12,186 (program +4,536..+11,919), VM program bytes
+56/+112/+287 on 3-byte-run witnesses. I-43's island/chain ratios
re-derived 1.3032/1.3035/1.3561 → **1.2344/1.2375/1.2649** (C1 grows both
arms, the chain more). `check_b108_litrun_stamp` default 256 → 312.

## 6. Compile-only census (`docs/dev/measurements/2026-10-04-b122-census.txt`)

Every set (8, by enumeration; utf8 under `-e utf8`) × {plain, whole} ×
{auto, vm}, both pins, v2 identity: **1,380 rows — 815 identical / 462
changed / 103 refused-both / 0 refusal movers.** Of the 462: 383 restored
to fc719ca4's program by ONE round-1 denial (run-overlap 291, view-edge
62, req-run-fold 30), 15 by all three; the remaining 64 attributed to the
flagless steps ([CLS-TREE] S2 range spelling 56, A1 2 — capability
`logparse-atomic`, K78 2 — email `factored`, S2 wide-class interval 4).
Answers: identical rows are answer-identical by construction; changed
rows rest on pcrec's per-step "no answer moves" and the window's oracle.

## 7. Roster/requires gates

Keyed by config NAME (`capability.missing_capabilities`), so the re-pin
moves nothing — verified over all 46 pinned pcrec configs: capability
blocks 1/64 for the 37 byte configs (as before), 20/21 for
`pcrec-dfa`/`-nocaps` (their [B121] declarations), 27/64 for the seven
`-utf8` configs (deliberately off that roster); utf8 blocks 5/76 for the
`-utf8` configs; every other set carries no `requires-*` tag.

## 8. Validation run by this lane

- `make check-schema`: 6 accepted / 74 rejected / 0 wrong.
- `make check-interpret`: 241/0. `make check-upstream`: OK.
- check-harness subsets (standalone, after `check_manifests` generated the
  subject trees): mechanism+deny 150/0; b122 7/7; 23 pcrec-facing
  functions (program_sha256, noreqbyte, opt42, b104/b108/b118 checks,
  the four registry diffs, emit-size port, abi floor, vars, kb33,
  roster coverage, encoding axis, b115) 73/0 after the litrun fix; and
  check_manifests + frame_buffer + pcrec_local + cc/noedge/cflags axes +
  wrong-answer control 86/0. (An earlier subset run without generated
  subject trees failed 18 rows on "subject file(s) are missing" — an
  ordering artifact of running functions standalone, gone once
  `check_manifests` ran.)

## 9. Charter-vs-committed checklist

| charter item | status |
|---|---|
| pin.sh c4c70f2c build (after ALL_DONE) | DONE (23:36) |
| every abi step 51→59 read in source | DONE (§1; three S2 events + K79/K80 + K78 beyond I-127's four) |
| shim reads new stamp/field; floor decision | DONE: `RX_RUN_WORDS`; floor stays 16 |
| STAMP_CASES/LEDGER re-derived by measuring | DONE (§5) |
| three deny flags as DENY_FLAGS controls moving their own stamp/program | DONE (§4, identity-proved) |
| registries re-archived, deltas explained | DONE (§3) |
| size books measured | DONE (§5) |
| catalogue pin_order + sidecars | DONE (3.14, 67 sidecars) |
| roster/requires gates admit pinned testees | DONE (§7) |
| CLAUDE.md files (root, testees/pcrec, pcrec_references, measurements, catalogue, tools) | DONE |
| compile-only census vs fc719ca4, refusal movers named | DONE (§6: none) |
| full `make check` GREEN | **OWED — manager launches** (DO-THEN-FINISH, >4 min) |

## 10. OWED: the full `make check` (manager to launch)

    cd /home/duxevents/pcrec-bench/.claude/worktrees/agent-a353755085f3282ad
    setsid /usr/bin/gnutimeout 5400 sh -c 'make check > /var/tmp/b122_makecheck.log 2>&1; echo "MAKECHECK_RC=$?" >> /var/tmp/b122_makecheck.log' < /dev/null > /dev/null 2>&1 &

Completion line: `MAKECHECK_RC=<n>` at the end of
`/var/tmp/b122_makecheck.log` (0 = green). Expected: check-harness grows
by the 7 b122 checks + 3 deny rows (B118's 625 → ~635), interpret 241,
upstream OK. Not yet run by this lane: `check_expectations` (the ~20-min
oracle re-derivation; untouched by a pcrec re-pin), `check-report`, and
`make cc-gate-census` (optional re-pin sweep, ~28 min).
