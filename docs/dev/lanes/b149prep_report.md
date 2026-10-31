# lane b149prep report -- RE-PIN THE WHOLE ROSTER to cb32eda28 (abi 93); also_pins 614d45eb3 (abi 89)

**Task**: plan row [B149] (the manager adds it), pcrec_main's W1 sha. Writer lane (Sonnet); no `store/` write, no timing.
**Branch**: `lane/b149prep` in `worktrees/b149prep` (the branch name pre-existed as a stale ancestor of master with no unique
commit; fast-forwarded to master before work). pcrec source: `~/projects/pcrec` (`~/pcrec` does not exist on this box).

## 0. PREDICTION (written by READING pcrec's tree at 614d45eb3..cb32eda28, 322 commits, BEFORE any build)

Sources read: `git log`, `docs/dev/history/abi_changelog.md` (entries 90-93), `docs/dev/known_issues.md` K134,
`docs/dev/lanes/{reqvm1m,trailgc2,trailgc3,l9look}_report.md`, `docs/dev/full_suite_ledger.md`, the `src/`, `cli/`, `lib/`
diffs. Four abi steps, every one real; no step is skipped this time (85 was the only skipped number and is long past).

### 0.1 The four abi steps

| abi | what (pcrec's own entry) | stamps / struct / axes | corpus rows I predict move |
|---|---|---|---|
| 90 [INLINE-C] stage 2 (ic2 + ic2fix) | module `code-c`, embedded C in `(?C`c: ...`)`, granted ONLY by `--allow-code` / `pcrec_options.allow_code`; every CALLOUT artifact's surface gains the span helpers (`rx_span`, `rx_eq`..`rx_u8next`, guard `PCREC_RX_SPAN_H`); a code-bearing artifact gains `RX_CODE_LANGS`; everything else moves in the abi digits only | NEW stamp `RX_CODE_LANGS` (code-bearing only; we never grant code, so never present); `lib/pcrec.h` `pcrec_options` gains `allow_code` (an options member, not `rx_info`); new CLI flags `--allow-code[=LANGS]`, `--code-header[=...]`, `--include-block`, `--list-callouts`; `struct rx_info` UNCHANGED | the `syntax` `grp-callout` rows (caps/nocaps x plain/whole = 4) gain the span-helper block (size up, program text moves); no other row |
| 91 [REQRUN-VM] (reqvm1/reqvm1m) | the required-run handoff and its re-entry reach both VM routes: a VM artifact with NO DFA scan, a pre-check and a finite K gets the first attempt's `attempt_position = handoff_position` and a re-entry block; a VM HYBRID whose prefilter re-enters gains the same and `RX_DFA_PREFILTER` reads `"handoff"`; plus a drop-handoff fit rung | `RX_REQ_HANDOFF` value `none` -> K on VM artifacts; `RX_DFA_PREFILTER` `handoff` (already in the adapter's closed set since 6b2dbd3e); no new stamp; no rx_info field | VM-routed rows with a required run: the forced-VM rows (`pcrec-vm`, `pcrec-vm-in`) and auto rows that route VM (loglines / capability / syntax / unusual); the census will count them. NOT a refusal mover (a fit rung that DROPS the handoff when over the cap); one `did-not-compile` -> compile is possible at the size cap edge, I predict 0 |
| 92 [MEMFN] D172 S3 (s3m) | the memfn kit's `cover` LOCATE row is ROUTED by default: a pattern whose every match is ONE fixed-width window the kit's REPORT site proves is searched by the window family and reported `[c, c+k)` with no machine run | `RX_DFA_SCAN` gains the value `cover`; `RX_MEMFN_LIBC` moves; `rx_info.scan` moves; axes: `cover` at `locate` 2 and `unanchored` 2 -> 3, the `#section memfn` block gains `window-search` / `window-skip` (renamed deny rows, `--memfn=no-window-search,no-window-skip`); `rx_info` UNCHANGED | fixed-width-window patterns (literals, small classes, `\bfoo\b`-like cores): predicted a few dozen rows across email/loglines/syntax/utf8/capability; every other artifact digits only. The SHIM'S closed set for `RX_DFA_SCAN` must learn `cover` (this is the ONE adapter-code change I expect) |
| 93 [K134] trail compaction (trailgc2/3) | VM artifacts whose program writes a capture/counter slot inside a loop or a called region gain `<PREFIX>_TRAIL_CHECK();` before each backward `goto` that closes a trail-writing cycle and each region return, three file-scope functions (`_trail_gc_floor`, `_trail_gc_start`, `_trail_compact`), a `size_t trail_gc_floor` member in `<prefix>_run_state`, a matcher-local `_trail_gc_at`; the fast tier never compacts and escalates. A DFA artifact and a cycle-free VM artifact: abi digits only | NO new stamp, NO rx_info field, NO axis, NO deny flag (pcrec offers none: the `--list-axes` count does not move for K134); the shim floor STAYS 16 | VM artifacts with a capture/counter write inside a loop or a subroutine call: +0.6-1.2 KB text each (+3-10 % on small ones) per pcrec's own measurement; I predict the `unusual` cscan / wild-json-validate / wild-sexp-balanced and every capability recursion / possessive-loop row, plus every VM row with a captured repeat |

### 0.2 No-abi changes that move generated code or the interface

- [EMIT-BIDI] aftermath / `stamp_kinds.c`: a new `internal` column and a new `ENGINE_WHY` / `DFA_PREFILTER_OFFSETS` row (stamp
  CLASSIFICATION for the code-segment block, `#undef`s of non-contract stamps) -- source-side bookkeeping, no emitted byte
  predicted to move for a pattern with no code segment.
- `--list-axes` description edit (the `RX_DFA_START` `attempt-start` row now also names "the cover window search"): one
  description string, which makes `list_axes.tsv` differ from 614d45eb3's by that row.
- `cli/main.c` +482 lines: option arity is now a table (`TAKES` / `DESCRIBE`): a `--list-*` / `--emit-facts` style query no
  longer takes a pattern; new `--list-callouts`. Predicted: no effect on the adapter's compile call (`--pattern` + `-o`).
- The census may find a [FLAG-SPELL]-style spelling move (b142 precedent: 12 rows); I found none in a grep of `-fno-*` spellings
  between the two `src/cli` trees (identical set).

### 0.3 Registries: predicted

| surface | prediction |
|---|---|
| `list_axes.tsv` | +rows: `cover` (locate 2), `unanchored` renumbered 2 -> 3, memfn-section `window-search` / `window-skip`; one description change; ~172 -> ~176 rows; main table axes +0 or +1 |
| `list_definitions.tsv` | 75 BYTE-IDENTICAL (ninth pin running) unless stage 2 adds a `.rxt` directive definition (`code-header` / `include` is a block directive: possible +rows) |
| `list_limits.tsv` | possibly +rows for the code module (`PCREC_MAX_CODE_*`); K134 adds none (`4n+17` is a documented bound, not a registry limit) |
| `list_schema.tsv` | +rows for `.rxt` schema (`rxt_schema.def` +5 lines: code/include directives): ~+3..5 |
| new surface `--list-callouts` | exists now; the bench does not read it; I will archive it only if a check needs it (decided at the build) |

### 0.4 Shim floor and adapter

`struct rx_info` is byte-identical across the whole span (`lib/pcrec.h`'s diff is `allow_code` in `pcrec_options` and a frame-size
comment) so the shim floor STAYS 16. Adapter work expected: (1) `RX_DFA_SCAN` closed set + `cover`; (2) `RX_CODE_LANGS` is
never present (asserted absent); (3) the CLI `--list-*` arity change does not touch the compile call. The `adapter.py`'s
callout binding (b147prep) still serves grp-callout; abi 90 does not change the callout surface's binding contract for a
`(?C1)`-style site (only tagged `(?C`c:` code needs `--allow-code`).

### 0.5 K134 and the `bench/unusual` give-ups (pcrec's default arm, 614d45eb3 baseline: 24 + 8 + 3 FRAMES give-ups)

At 614d45eb3 pcrec's default (stack-resident, 2,048-frame) arm gave up `PCREC_ERR_FRAMES` on cscan: 24 cells; on
wild-json-validate-onig / wild-sexp-balanced: 8 + 3 (ledger `2026-10-29-unusual-0.1-l9-scratch.md` 1(a), 1(h)); on streams:
100/256 (seg-s), 1,723/4,096 (seg-l), 163/311 (sqlite-bodies-s), 2,620/4,971 (sqlite-bodies) calls. pcrec's l9look diagnosis: on
FLAT input the give-up is TRAIL exhaustion, never resume frames (idents-1m: 4 resume frames, 9.1 M trail entries, 145 B/byte).
K134's own statement: "All five flat cscan subjects (idents, comment, splice, nest-paren 32k/100k) answer on the default
arm; `^(a(?1)?b)$` reaches n = 763 (was 342)".

- **Predicted to FLIP gave-up -> answered (default arm)**: cscan on `idents-1m`, `comment-5m`, `splice-1m`, `nest-paren-32k`,
  `nest-paren-100k` (the five flat subjects), and the subset of the segment-stream calls whose failure was trail growth on
  nearly-flat C bodies (seg-s, seg-l, sqlite-bodies): I expect the 100/256, 1,723/4,096, 163/311, 2,620/4,971 give-up counts to
  FALL substantially (to a small residue of genuinely deep bodies), the answers agreeing with the oracle.
- **Predicted NOT to flip**: `nest-brace-<d>` rungs whose give-up is LIVE nesting (the resume stack holds `d` x (items+sp)
  frames, compaction only shortens the trail); the boundary moves from ~342 to ~763 levels on the pcrec specimen, so the
  smallest cscan nest-brace rungs (128, maybe 256) may flip while >= 512 stay. `nest-brace-128` is the one pcrec itself lists
  among its five libpcre2-answered subjects; I predict it FLIPS. wild-json-validate / wild-sexp-balanced: their 8 + 3
  give-ups are nest-depth; predicted mostly UNCHANGED except where depth < ~700.
- **Cost, same cells that already answered**: pcrec's D183 states +0.7-2.1 % instructions on cscan and +1.6-4.3 % on a
  recursive-parens matcher; I predict the bench's `_in` arm and any answered cell shows a +1-4 % shift, not measured here
  (no timing in this lane).
- **Gave-up outcomes are a BENCH-LEVEL consequence**: a cell moving gave-up -> answered changes `bench/unusual`'s outcome table
  and its R3 depth-of-failure table. That is for the first window, not this lane (the census is compile-only; the K134 give-up
  flip is predicted from pcrec's own statements and is OWED to the window).

### 0.6 `--code-header` (task item 4), answer from reading

NO bench config, adapter call, harness path, tool, script, `.rxt` set or Makefile target passes `--code-header`, `--allow-code`
or an `.rxt` `code-header` directive to pcrec (`grep -rIn` over testees/ pcrecbench/ tools/ scripts/ bench/ Makefile
catalogue/ for `code-header`, `code_header`, `allow-code`, `allow_code`: 0 hits in non-.md files; 0 hits in any `.rxt`). The
adapter's pcrec flags are `--features all`, `--engine=`, `--pattern`, `-o`, `--warn-emit-bytes=`, `--no-captures`, `--utf8`,
`--encoding=`, `--tune`, `--max-emit-*`, `--vm-entry-shape`, `--mode`, `--list-*` (read from `adapter.py`). **The crash does not
reach this bench; nothing stops.** (Re-verified after the adapter change, section 3.)

## 1. Census verdict (predicted vs measured)

`docs/dev/measurements/2026-10-30-b149prep-census.{txt,tsv}` (probes `probe_b149prep_{emit,census,summary}.py`): 1,600 rows
(every pattern x form x config of the program-identity population), 614d45eb3 vs cb32eda28, program identity **v3**.

| result | rows |
|---|---|
| v3-identical (0 B) | 1,186 |
| changed | 325 |
| refused both | 89 |
| refusal movers (either direction) | **0** |
| UNATTRIBUTED | **0** |

Every changed row is attributed by a marker that is verified, not assumed (a pure-k134 row is verified by stripping the trail
functions/macro/checkpoint sites/trail lines and comparing SORTED lines; cover rows by the `--memfn=no-window-search` arm
restoring the old program; handoff rows by `-fno-req-handoff`):

| attribution | rows | emit-byte delta |
|---|---|---|
| abi90-span-helpers (callout surface) | 20 | +2,612 |
| abi90 + abi91 | 28 | +2,662..+3,038 |
| abi91-reqrun-vm (handoff) | 9 | -1,079..+530 |
| abi91 + abi92-pair + abi93 | 1 | |
| abi92-cover | 159 | -6,837..-2,158 |
| cover + pair look-ahead | 10 | |
| abi92-pair-lookahead (reqrun `wa=128, wb=128`) | 5 | +368..+377 |
| abi93-k134 (trail compaction) | 93 | +1,608..+2,015 |

K134 rows by set: bounded 4, capability 49+1, sentinel 8, syntax 12, unusual 20 (cscan, cscan-onig, wild-sexp-balanced,
wild-json-validate, wild-json-validate-onig; both forms x caps/nocaps).

Prediction accuracy:

| predicted (section 0) | measured | verdict |
|---|---|---|
| abi 90: only the 4 syntax `grp-callout` rows gain the span block | 20 + 28 rows (more than the 4 predicted; the 28 overlap abi 91) | UNDER-called: the callout-surface population is larger than the 4 grp-callout rows |
| abi 91: VM rows with a required run; 0 refusal movers | 9 + 28 + overlaps; 0 refusal movers | held |
| abi 92: "a few dozen" cover rows | 159 + 10 = 169 | WRONG by ~4x: cover takes most literal/small-class windows (router-prefix-order emit 20,935 -> 16,138) |
| abi 92: the shim's closed set learns `cover` (the ONE adapter change) | exactly that, nothing else | held |
| abi 93: VM artifacts with a capture/counter write in a loop; +0.6-1.2 KB | 93 rows, +1.6..2.0 KB each | rows right, size UNDER-called (the stamp-free emitted block is ~2 KB with the three functions) |
| no new stamp / rx_info field / axis for K134 | held | held |
| not predicted | abi 92 also adds a bounded two-stream look-ahead to the reqrun pre-check (5 rows, +368..377 B) that pcrec's abi 92 entry does not name | finding F2 |
| refusal movers 0 | 0 | held |

## 2. Registries (archived verbatim with chained headers; bodies equal live output)

| surface | 614d45eb3 | cb32eda28 | predicted |
|---|---|---|---|
| `list_axes.tsv` | 172 rows | 176 rows (+4: `cover`, `unanchored` renumbered, memfn-section rows, one description) | held (+4) |
| `list_definitions.tsv` | 75 | 75 BYTE-IDENTICAL (ninth pin running) | held |
| `list_limits.tsv` | 78 | 78 BYTE-IDENTICAL | WRONG-ish: predicted possible `PCREC_MAX_CODE_*` rows; none |
| `list_schema.tsv` | 81 | 82 (+1 `file code-header`) | predicted +3..5, measured +1 |
| `--list-callouts` | n/a | exists, needs an argument; not archived (no check reads it) | as predicted |

## 3. Adapter change and the shim

`testees/pcrec/adapter.py`: the closed `dfa_scan` set gains `cover` (source and description text updated). `struct rx_info` is
unchanged, so `PB_SHIM_MIN_ABI` STAYS 16 (both abi-sabotage arms pass unchanged). `configs.toml`: `pin = "cb32eda28"`,
`also_pins = ["614d45eb3"]`, 9ae59f5d4 retired from the allowlist. `catalogue/rules.toml` 3.22, `pin_order` appended.
`testees/pcrec/CLAUDE.md` "Re-pin at cb32eda28" (7 points); root CLAUDE.md status paragraph.

`--code-header` (task item 4): NOT passed anywhere. Now asserted by a check (`check_b149_stamps` greps the adapter and the harness
files for `--code-header` / `--allow-code`) -- nothing stops.

## 4. Re-aims (each red: stale aim vs real change; nothing loosened)

Chain 2 gave 28 FAIL in the selfcheck slice; all are the SAME three real abi 90-93 changes meeting aims written for an older pin.
Chain 3: 489 pass / 0 fail on the slice. Every re-aim is a new EXPECTED VALUE with its reason, never a relaxed predicate:

| red | class | reason / new aim |
|---|---|---|
| `check_b147_stamps`, `check_b135_two_pin_window` | stale aim | they named builds / pins by "the also_pin" or "the canonical pin"; now name `614d45eb3` / `9ae59f5d4` explicitly (the b135 check expects canonical cb32eda28, also_pin 614d45eb3, retired list + 9ae59f5d4) |
| b122 / b124 / b126 deny-identity arms (restore-the-old-program) | REAL abi 92 + 91 | the denial no longer restores the old program unless cover and the handoff are denied too. `B149_COVER_OFF = --memfn=no-window-search` is applied on the pinned binary only (the older pins do not know the flag: "unknown option"); `-fno-req-handoff` is appended (`B149_LATER_DENIES`) |
| `DENY_CONTROLS` rows `(?i)abc` req-run-fold, both `abc` prefilter rows, `\bfoo` req-use, `x` search-start | REAL abi 92 | these literals route to `cover`; the shared-flags slot now carries `--memfn=no-window-search` so the control still reaches the mechanism it controls |
| G1 witness `\[` | REAL abi 92 | now cover; witness changed to `\[[a-z]+` (dfa_scan_edge `range`, req_why dominated) |
| router-prefix-order ledger row | REAL abi 92 | now asserts cover: dfa_scan cover, prefilter none, offsets none, dominated, req_byte 47, req_run `2f75736572@0` |
| litrun `alt-foo-tails` under auto | REAL abi 92 | new row asserts S1 `run-pinned` `0*,1,2`, req_run `666f6f@0`, req_byte 102, scan at offset 0 |
| b135 `locate` registry expectation | REAL abi 92 | rev-end / cover / unanchored |
| b136 `-fno-req-handoff` registry expectation | REAL abi 91 | four rows (prefilter handoff; req-use handoff, handoff-attempts, handoff-attempts-entry; all bit 46) |
| size books (`check_mechanism_stamps`) | REAL abi 90-93 | new layer `_b149_moved` / `B149_RESID`, measured per witness: `(?i)abc` VM +794; `[ac]` +426; `` [@`] `` +794; entry-shape PLAIN program +22; altwide pfx3-256 +426; email-nested-plus / wild-validator-email-owasp / winpath-near-miss +1,815 emit, +22 program; dup-param-detect +1,815; nested-comment-rec +1,882 |
| check-unusual `calls: streams: pcrec-auto give-up naming` (chain 3, the one red) | REAL abi 93 (K134), as predicted | see section 5 |

New: `check_b149_stamps` (15/15): abi 93/89; struct identical; floor 16; the span helpers and no `RX_CODE_LANGS`; abi 91 on
`7-url-tld-fix` (new "0", old "none", denied "none"); abi 92 `\d{2}` unanchored -> cover, the `nowindow` arm restoring the old
program, `a+b` as the v3-identical control; abi 93 balanced-parens-rec forced-VM with >= 1 `TRAIL_CHECK` site and the strip
restoring the old program; emit delta +1,815 in [1000, 2600]; the DFA artifact without checkpoints; no `--code-header`.

## 5. K134 and the bench/unusual give-ups: predicted vs MEASURED

Predicted (section 0.5): the five flat cscan subjects and a substantial fraction of the stream give-ups flip to answers; deep
`nest-brace` rungs (>= 512) stay.

Measured here (check-unusual `calls`, compile + one smoke stream, not a window):

| cell | 614d45eb3 | cb32eda28 |
|---|---|---|
| `pcrec-auto` x cscan-onig x seg-s (256 calls) | 151 matched / 5 nomatch / **100 gave up PCREC_ERR_FRAMES** | 251 matched / 5 nomatch / **0 gave up**; results_sha256 == expectations_stream.tsv |
| `pcrec-auto` x cscan-onig, all four streams of the check | gave up, named FRAMES | `matched-as-expected` on all |
| `pcrec-vm-in`, caller buffer 4 frames / 4 trail, same stream | n/a | 256 of 256 gave up, `first_limit PCREC_ERR_FRAMES` (still gives up; the naming check moved here) |
| `pcrec-vm-in`, configured buffer | n/a | 0 gave up, sha == expectation (the control) |

So the predicted stream flip is CONFIRMED in full for seg-s (100/256 -> 0, predicted "fall substantially"; it fell to zero) and the
check's other three streams matched-as-expected. The deep `nest-brace` and wild-json/sexp subject-cell flips (24 + 8 + 3 cells) are
NOT measured here and remain OWED to a window.

Repair (no loosening): the old assertion "pcrec-auto gives up and names FRAMES" is replaced by (a) a give-up-naming check on a shape
that still gives up (tiny caller buffer) with its control, and (b) a by-value flip row: the default pcrec-auto answers seg-s at the
canonical pin and, run as a child under `PCRECBENCH_PCREC_PIN=614d45eb3`, gave up on 100 of 256 calls.

## 6. Findings for pcrec

- F1 (abi 92): `cover` takes 169 of 325 changed rows out of the candidate-start / handoff / start mechanisms (router-prefix-order
  emit 20,935 -> 16,138); every cross-window mechanism comparison on literal windows now needs the `--memfn=no-window-search`
  arm. The prediction "a few dozen rows" was 4x low.
- F2 (abi 92): a bounded two-stream look-ahead (`wa = 128, wb = 128`) landed in the required-run pre-check (`rx_reqrun__body`), +368..377 B on
  5 rows; it is not in the abi 92 stamp list or entry.
- F3 (abi 91): the handoff moves forced-VM `abc`'s `.text`; any earlier "the deny flag restores the old program" claim needs
  `-fno-req-handoff` as well. No `--list-axes` row says so.
- F4: `\[[a-z]+` reads req_why `dominated` with `dfa_scan_edge range`; `\[` alone is now `cover` (the old G1 witness lost its meaning).
- F5 (abi 93, K134): the sorted-line strip identity holds on all 93 pure rows; the +1.6..2.0 KB cost is above pcrec's stated
  +0.6..1.2 KB. The default arm answers the seg-s cscan-onig stream completely (100/256 gave up before).
- F6: `--list-axes` has no deny row for K134 (by design); a window's K134 cost needs a differently-pinned BEFORE (614d45eb3), which is
  why `also_pins` keeps it.

## 7. Check counts

- targeted selfcheck slice (chain 3): `b149prep_checks.py` 489 passed, 0 FAILED (34 functions incl. `check_b149_stamps` 15/15,
  `check_mechanism_stamps` 142/0, b122/b124/b126 42/0).
- `make check-unusual` chain 3: 130 passed, 1 FAILED (the K134 flip, section 5). Chain 4 (calls section alone, after the repair): 45 passed, 0 FAILED (CALLS rc=0), incl. the tiny-buffer give-up naming and the K134 flip row. Whole check-unusual is thus 130 + the repaired section, 0 red; it was not re-run whole (manager's full check at merge).
- chain 2 (before repairs): slice 460 / 28 FAIL; check-unusual 109 / 21 (missing generated subject trees in a fresh worktree --
  fixed by generating them in the chain); REGEN_SIDECARS rc 0; CHECK_INTERPRET rc 0.
- NOT run here: the full `make -k check` (the manager runs it at merge).

## 8. Charter vs committed

| charter item | committed |
|---|---|
| PREDICTION section committed before the build | yes (8b702800) |
| re-pin pin / also_pins, 9ae59f5d4 retired | yes |
| registries archived and diffed | yes (section 2) |
| census, every mover attributed | yes, 0 unattributed, 0 refusal movers |
| stamp rows / checks for abi 90-93 | `check_b149_stamps` 15/15 + the re-aims |
| catalogue `pin_order` | 3.22 |
| `testees/pcrec/CLAUDE.md` "Re-pin at cb32eda28" | yes |
| `--code-header` check | NO, asserted |
| K134 give-up effect predicted | yes; stream flip measured, subject-cell flips OWED |
| heavy steps through the box queue | chains 1-4 via `boxq_window`, prio 7NN |
| store/ untouched, no timing, ~/pcrec read-only | yes |

## 9. OWED

- The full `make -k check` (manager, at merge).
- The K134 give-up flips on the unusual SUBJECT cells (24 cscan + 8 + 3), and the depth boundary (~342 -> ~763), in a window.
- `docs/dev/lanes/b147win_chain.sh` names `@9ae59f5d4`; it needs re-aiming to `@614d45eb3` before reuse.
- plan.md / dev_journal.md rows (the manager's).
