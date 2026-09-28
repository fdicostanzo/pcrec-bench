# lane b108repin report — RE-PIN to a32bc86e (abi 39 -> 41)

**Task**: plan row [B108] / inbox I-113. Re-pin the pcrec testees from
`751b9c6d` (abi 39) to pcrec main `a32bc86e` (abi 41) by the
[B84]/[B90]/[B101]/[B104] ritual: build, re-archive the four registries
and explain every delta, assert the abi 40/41 stamps BY VALUE, decide
and justify the shim-floor question, add the S2a program-change deny
control, confirm the acceptance mover, reproduce I-113's bench-mover
count with a compile-only census, re-derive the size books (measured,
not assumed), add eight new pinned testees for I-113 §7.1's 2x2 and
§7.2's L-sweep, append the catalogue pin, and run `make check` in full.
No `store/`/`reports/` write, no timing of any kind (per the brief: the
manager schedules the measurement window).

**Branch**: `lane/b108repin` (worktree `worktrees/b108repin`), commits
`84b79af` (pin build, configs bump, three new `DENY_FLAGS` entries,
eight new pinned testees, the b108 census script), `d89de31` (the four
registries re-archived and diffed), `ae89c9d` (the `vm_lit_runs` stamp
wired end to end, every broken size-book assertion re-derived — 129/129
`check_mechanism_stamps`, 18/18 `check_deny_flag_controls`), `2fd0f82`
(root CLAUDE.md, testees/pcrec/CLAUDE.md, pcrec_references.md,
measurements/CLAUDE.md, catalogue 3.12), and this report.

## 0. Findings the manager must read first

1. **Both abi steps are exactly what I-113 described**, confirmed
   against pcrec's real history (`git log 751b9c6d..a32bc86e`: one merge,
   `Merge branch 'lane/s2a'`). Abi 39 -> 40 is [FINDINGS] B1 (the
   byte-rate accessor + `default.rxt` data tier: `<PREFIX>_FINDINGS` +
   `rx_info.findings`, APPENDED at the struct's end, on every artifact);
   abi 40 -> 41 is [OPT-LITSCAN] S2a (a VM literal run of two-plus
   one-byte literals, and an island's single-child trie chain, becomes
   ONE P4 compare instead of a per-byte chain; new axis `lit-run` bit 33,
   `-fno-lit-run`).
2. **`struct rx_info` gains exactly the one appended `findings` member**
   (diffed field for field on a plain `abc` witness against 751b9c6d's
   `.h`: empty diff but for the one appended line, inside the SAME
   `#ifndef PCREC_RX_ABI_H` block as every other field). `RX_VM_LIT_RUNS`
   has NO `rx_info` mirror at all (D77's precedent, `vm_alt_islands`'/
   `vm_cls_folds`' own shape).
3. **THE SHIM FLOOR DECISION: STAYS 16, on the [B90] vars/nvars
   precedent exactly.** Neither new surface needs a floor move: abi 41's
   `RX_VM_LIT_RUNS` has no field to read (a macro through `#ifdef` never
   moves the floor); abi 40's `rx_info.findings` field IS new, but this
   shim's protocol has no consumer for it (no bench check, no
   `engine_metadata` pair reads pcrec's internal analysis-provenance
   string) — the SAME judgement [B90] made for `vars`/`nvars` (a
   name-table field this shim's protocol never needed). Documented in
   shim.c's own new paragraph, right after [B90]'s. Confirmed at the
   build: `check_abi_floor_refusal`'s two sabotage arms (`.abi = 5`,
   `.abi = 15`) still refuse by name, with the unmodified artifact
   loading in the same run.
4. **Registries: THREE of four byte-identical, one gains two axis rows
   and two limit rows, every delta diffed against the LIVE pin binary**
   (never asserted from either lane's own report). `list_axes.tsv`
   91/32 -> **93/32** (the `lit-run` axis: order-1 `run` predicate /
   order-2 `denied`, `RX_VM_LIT_RUNS`, `PCREC_NO_LIT_RUN` bit 33,
   `-fno-lit-run`). `list_limits.tsv` 62 -> **64**
   (`PCREC_MAX_FIND_COUNT` 2^40, `PCREC_FIND_FLOOR_PPM` 2 ppm, both
   [FINDINGS] B1's). `list_definitions.tsv` and `list_schema.tsv`
   BYTE-IDENTICAL (50 / 78 rows) — neither step touches `.rxt` grammar.
5. **`RX_VM_LIT_RUNS` wired end to end and asserted BY VALUE on two
   witnesses**: `pb_has_vm_lit_runs()`/`pb_vm_lit_runs()` in shim.c
   (`vm_cls_folds`'s own presence-question shape), `driver.c`'s
   `info vm_lit_runs`, adapter.py's `INT_PAIRS` +
   `STAMP_SCOPE["vm_lit_runs"] = ("vm", 41)` + a `METADATA_DECL` entry.
   Witnesses: a plain 3-byte literal forced VM (`abc`: runs 1 -> 0 under
   `-fno-lit-run`, `vm_program_bytes` 256 -> 550 — both
   `check_b108_litrun_stamp` and the new `DENY_CONTROLS` row) and
   `foo|bar` (an island: runs 2, `vm_program_bytes` 1532 -> 1227,
   MEASURED — the island's own chains collapse too). `[FINDINGS] B1`
   asserted BY VALUE too (`check_b108_findings_stamp`): `RX_FINDINGS` ==
   `rx_info.findings`, shape `"byte-rate=default:<16 hex>"`, IDENTICAL
   across unrelated patterns (the hash is of the shipped rate table, not
   the pattern).
6. **The acceptance mover confirmed against BOTH binaries directly**
   (`check_b108_acceptance_mover`, never assumed from I-113's own
   numbers): `wild-datetime-datefinder-alternation` under `--engine=vm`
   refuses at 751b9c6d (666,249 code bytes; this project's
   `--features all` protocol token makes the exact count differ
   slightly from I-113's quoted 666,632) and compiles at a32bc86e
   (482,765 code bytes, `vm_lit_runs 826`).
7. **The compile-only census reproduces I-113's own bench manifest
   EXACTLY, digit for digit**: `docs/dev/measurements/
   probe_b108_census.py`, over pcrec's own S2a-lane population
   (capability@0.1's 64 patterns x pcrec's own 4-config `bench` set —
   auto-caps/auto-nocaps/vm-caps/vm-nocaps): **186 identical / 63
   changed / 5 refused-both / 2 refusal-mover** — matches pcrec's
   s2a_report.md §2 table exactly (I-113's own "63 bench + 1,018 corpus"
   line; the corpus half is pcrec's own `tests/**/*.rxt` tree, out of
   scope here). v2 program identity (`tools/program_identity.py`) needed
   NO change for [FINDINGS] B1: its own rule 2 drops the whole
   `PCREC_RX_ABI_H` block (the appended `findings` member included) and
   rule 3 drops the unreferenced initializer — B1 is invisible to the
   identity by construction, so this census is a pure S2a read. Archived
   at `docs/dev/measurements/2026-09-27-b108-census.txt`.
8. **Size books are NOT a single flat term — measured per witness, as
   the brief demanded.** Two new constants:
   `B108_FINDINGS_STAMP_LINE` (385, both engines, flat — MEASURED on a
   pure-DFA witness, matching pcrec's own quoted number exactly) and
   `B108_VM_LIT_RUNS_STAMP_LINE` (25, VM only, flat at any run-free/
   denied count). Where a VM artifact stamps a literal run, P4's
   collapse SHRINKS the program by a witness-specific amount that
   overrides the flat terms; every such row across `STAMP_CASES` and
   `LEDGER_STAMP_CASES` was individually re-measured against the live
   a32bc86e binary rather than derived: `foo|bar` (+125 net, not +410),
   the altwide island witnesses w-256/srt-256/pfx3-256/s-256/w-384
   (vm_program_bytes falls 34-56%), `wild-secrets-github-pat` (a HYBRID
   whose own VM body is not exempt from lit-run: net -1,150 B),
   `tag-pair-match` (+270, not +410), `nested-comment-rec` (a net
   SHRINK, -154 B), `winpath-near-miss`'s K64 row (+271, not +410) and
   `level-context`'s [SEL-1] hybrid (12,026 -> 6,805 program bytes, two
   islanded level-word sets). 44 individual assertions moved in total;
   every one re-measured, none guessed from the size delta alone.
9. **Two derived FINDINGS re-measured rather than silently patched.**
   I-43's altwide island/chain code-byte ratio (against the SAME pin's
   `-fno-alt-island` arm) INVERTS at this pin: 0.856/0.812/0.764 (every
   prior pin through d34c9131) -> **1.3105/1.3206/1.3561** — the island
   is now LARGER than the chain, because the chain's per-branch literal
   runs collapse independently and in full where the island's shared
   trie dispatch cannot collapse branch by branch the same way. The
   altwide VM refusal wall MOVES A SECOND TIME: [B37] held it at
   384<w<=512; at this pin BOTH the forced-VM island route and the
   `-fno-alt-island` chain route now compile through `w-1024` (456,072 /
   318,862 code bytes) and refuse at `w-2048` (884,931 / 621,150 bytes)
   — the new wall is **1024<w<=2048** on both arms. The DFA route's own
   wall (512<w<=1024, [B42]'s [K53-SELRETRY] finding) is untouched,
   since S2a is a VM-only mechanism.
10. **Eight new pinned testees, three new `DENY_FLAGS` entries.**
    `-fno-req-run`/`noreqrun`, `-fno-altcls-factor`/`noaltclsfactor` and
    `-fno-lit-run`/`nolitrun` appended AFTER `-fno-req-byte` in
    adapter.py's `DENY_FLAGS` tuple, so no existing `testee_id`'s parts
    move. `pcrec-{auto,vm}-nolitrun`, `pcrec-{auto,vm}-noaltclsfactor`,
    `pcrec-{auto,vm}-noaltclsfactor-nolitrun` (I-113 §7.1's 2x2's three
    missing corners — the default x default corner is the pre-existing
    `pcrec-auto`/`pcrec-vm`) and `pcrec-vm-noreqbyte-noreqrun[-nolitrun]`
    (I-113 §7.2's L-sweep rows). Every config's derived `config_extra`
    verified by direct `describe()` call before committing (all eight
    matched the expected DENY_FLAGS-order slug on the first try).
    `-fno-altcls-factor` had NO pinned testee before this pin (the axis
    predates [B108] — [OPT-ALTCLS] — but nothing had asked for its
    BEFORE until this interaction); the brief's pointer to
    `docs/dev/lanes/b102altctl_report.md` was a MISATTRIBUTION (that
    report is an unrelated UTF-8/altwide read lane) — confirmed by
    reading it and by grepping `configs.toml` directly for any existing
    `-fno-altcls-factor` config, finding none.

## 1. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 1 | `pin.sh a32bc86e`, build | DONE (`build/pcrec-a32bc86e`, via the sanctioned `git archive` — nothing written inside `~/pcrec`) | — (build/ is gitignored) |
| 2 | re-archive the four registries, diff against the pin, explain every delta | DONE: axes 91/32 -> 93/32 (`lit-run`), limits 62 -> 64 (two [FINDINGS] rows), definitions/schema BYTE-IDENTICAL | `d89de31`, §0.4 |
| 3 | assert the abi 40/41 stamps BY VALUE on witnesses (`RX_FINDINGS`/`rx_info.findings`, `RX_VM_LIT_RUNS`) | DONE: `check_b108_findings_stamp`, `check_b108_litrun_stamp`, the new `DENY_CONTROLS` row, plus two `STAMP_CASES`/`LEDGER_STAMP_CASES` witnesses (`foo\|bar`, the acceptance mover) | `ae89c9d`, §0.5 |
| 4 | decide and measure whether the shim must read `rx_info.findings` / whether the floor moves; justify either way, sabotage arm if it moves | DONE: floor STAYS 16, justified in shim.c's own new paragraph (the [B90] precedent), confirmed via the existing two-arm `check_abi_floor_refusal` (no new arm needed since the floor did not move) | shim.c, §0.3 |
| 5 | the S2a program change on a VM literal-run witness vs `-fno-lit-run` as a deny control in `check_deny_flag_controls` | DONE: the new `vm_lit_runs` row (`abc` --engine=vm, runs 1->0, program 256->550) | `ae89c9d`, §0.5 |
| 6 | the acceptance mover confirmed | DONE: `check_b108_acceptance_mover`, both binaries, both vm-caps/vm-nocaps arms measured | §0.6 |
| 7 | compile-only census reproducing I-113's 63 bench movers | DONE: `probe_b108_census.py`, 186/63/5/2, archived `2026-09-27-b108-census.txt` | §0.7 |
| 8 | re-derive the size books, measured not assumed | DONE: two new flat constants + 44 individually re-measured assertions (11 with real S2a shrinkage), two derived findings (the ratio inversion, the wall's second move) re-measured rather than patched | `ae89c9d`, §0.8-9 |
| 9 | catalogue `[[pin_order]]` append, minor bump | DONE: 3.11 -> 3.12 | `2fd0f82` |
| 10 | update root CLAUDE.md's pin paragraph, testees/pcrec/CLAUDE.md, pcrec_references.md, other owning CLAUDE.mds | DONE: root CLAUDE.md, testees/pcrec/CLAUDE.md's new "Re-pin at a32bc86e" section + table rows, pcrec_references.md's new [B108] row, docs/dev/measurements/CLAUDE.md's new probe+archive rows | `2fd0f82` |
| 11 | eight new pinned testees for the 2x2 and the L-sweep, checking for an existing `-fno-altcls-factor` config first | DONE: none existed; all eight added with derived-id verification (§0.10) | `84b79af` |
| 12 | `make check` in full, DETACHED with a completion marker | LAUNCHED (setsid, `/var/tmp/b108scratch/b108_make_check.log`), numbers OWED (§5) — per BOILERPLATE's manager-launched default; this lane launched it itself because the report was still being written (the "further independent work" clause) | §5 |
| 13 | no measurement window, no `store/`/`reports/` write | HONOURED: every probe/check here is compile-only or answers-only; no `quick`/`run` cell was executed | — |

## 2. Validation (targeted; numbers)

- **New checks, first run**: `check_b108_findings_stamp` **1/0**,
  `check_b108_litrun_stamp` **1/0**, `check_b108_acceptance_mover`
  **1/0**.
- **`check_deny_flag_controls`**: **18/0** (17 pre-existing rows + the
  new `vm_lit_runs` row).
- **`check_mechanism_stamps`**: **129/0** (re-run three times across
  this lane as size-book fixes landed: 85/44 fail first pass -> 127/2
  -> 129/0 final).
- **`make check-schema`**: 6 accepted / 74 rejected for the intended
  rule / 0 wrong (unaffected by this re-pin).
- **`python3 catalogue/fixtures/gen.py --check`**: 251 files in 77
  fixtures, ok (unaffected).
- **`struct rx_info` diff** (the `abc` witness's `.h`, both binaries):
  empty but for the one appended `findings` member, confirmed inside the
  shared ABI block.
- NOT run standalone: `check_list_axes_registry` /
  `check_list_limits_registry` / `check_list_definitions_registry` /
  the schema one (no such check exists) — their claims (byte-identical
  below the header, or the exact two-row/two-limit-row delta) were
  verified directly by diffing the re-archived files against the live
  pin's own `--list-axes`/`--list-limits` output during §0.4's work;
  inside the OWED full `make check` regardless.
- **`make check-interpret`**: NOT run standalone this lane (inside the
  OWED full `make check`); EXPECTED to show the catalogue 3.11 -> 3.12
  bump as section-3 (sidecar freshness) failures only, the same shape
  every prior re-pin has shown — sidecar regeneration is the manager's
  merge step (b58/b74/b80/b84/b90/b101/b104 precedent).

## 3. `struct rx_info` / shim-floor confirmation (the exact commands)

    OLD=/home/duxevents/pcrec-bench/build/pcrec-751b9c6d/build/pcrec
    NEW=/home/duxevents/pcrec-bench/build/pcrec-a32bc86e/build/pcrec
    $OLD --features all --pattern 'abc' -o old
    $NEW --features all --pattern 'abc' -o new
    diff <(sed -n '/struct rx_info {/,/^};/p' old.h) \
         <(sed -n '/struct rx_info {/,/^};/p' new.h)
    # only the appended `findings` member and its doc comment differ

`grep -n PB_SHIM_MIN_ABI testees/pcrec/shim.c` still reads `#define
PB_SHIM_MIN_ABI 16` (unedited) — the floor stays 16 because nothing this
pin adds is a field this shim reads.

## 4. The size-book re-derivation, in outline

Every one of the 44 assertions this pin's build moved was checked
against a LIVE compile at a32bc86e (never against a formula alone).
Two clean populations account for most of them:

- **DFA-routed, no VM involvement**: `+ B108_FINDINGS_STAMP_LINE` (385)
  appended to the existing symbolic sum. Nine witnesses (start-PINNED
  DFA, both `cls-upto-16384`/`cls-upto-4` DFA rows, altwide w-256/
  srt-256 DFA, dig-upto-16 auto, `wild-validator-uuid-grok`,
  `router-prefix-order`).
- **VM-routed, no literal run of its own**: `+ B108_FINDINGS_STAMP_LINE
  + B108_VM_LIT_RUNS_STAMP_LINE` (410). Eleven witnesses (the ASCII-fold
  triple, `cls-upto-32768`'s two declined forms, altwide ci-256/floor,
  dig-upto-16 forced-VM, five of the six K64 capability rows, the two
  fix-A control rows, `dup-param-detect`).
- **VM-routed with a real literal run**: hardcoded to the freshly
  measured value with a comment naming the mechanism and the old
  number. Eleven witnesses, listed in §0.8.

## 5. OWED (owner, trigger)

- **Full `make check`** — LAUNCHED by this lane (detached):

      setsid /usr/bin/gnutimeout 5400 make check > /var/tmp/b108scratch/b108_make_check.log 2>&1 < /dev/null & disown

  This is a bare `setsid ... & disown`, per BOILERPLATE's own warning:
  **no completion notification will ever reach any agent for it.** The
  trigger is the log file's own tail matching a `check-*: N passed, N
  FAILED` line for each of the four targets, or `make`'s own final exit
  line. A fresh agent (or the manager) must check
  `/var/tmp/b108scratch/b108_make_check.log`'s tail before relying on
  any number in it.
  EXPECTED: `check-schema` 6/74/0 (unaffected); `check-harness` all
  green (the harness's own in-process count, which the full suite may
  render slightly differently owing to `check_manifests` regenerating
  subject trees, as every prior re-pin's report notes); `check-report`
  green (the reporter is untouched by either abi step); `check-interpret`
  showing the catalogue 3.11 -> 3.12 bump as section-3 (sidecar
  freshness) failures only — `make`'s own exit code nonzero from those
  named failures alone, exactly as at every prior re-pin, until the
  sidecars are regenerated at merge.
- **Sidecar regeneration** for catalogue 3.12 — manager, at merge
  (b58/b74/b80/b84/b90/b101/b104 precedent).
- **plan.md [B108] row, dev_journal, outbox note to pcrec (if any)** —
  the manager's. No ask for pcrec is filed by this lane: both abi steps
  behave exactly as I-113 described, and every finding here (the ratio
  inversion, the wall's second move) CONFIRMS I-113's own predictions
  rather than contradicting them.
- **The measurement window** (I-113's factoring x lit-run 2x2, the
  L-sweep, and the D77 bench pass I-113 §7 names) is explicitly NOT this
  lane's — the brief says the manager schedules it. The eight new
  testees and the census/stamp work above are what the window will run
  against.
- **[B109]** (I-114, OPT-HYB-RESEED x86 confirmation) is queued behind
  this lane per plan.md, untouched here.
