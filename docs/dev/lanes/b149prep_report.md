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
