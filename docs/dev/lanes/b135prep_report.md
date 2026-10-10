# lane b135prep report -- RE-PIN to 7388f1c0 (abi 73) + a15fb77b (abi 72) as a second pin

**Task**: plan row [B135] step (a), inbox I-140/I-142 and the manager's brief. Re-pin pcrec
from `255bcdd8` (abi 68) so ONE window can measure two pcrec revisions: `a15fb77b` (abi 72, the
BEFORE of [OPT-REVEND]) and `7388f1c0` (abi 73, the AFTER; the canonical pin). Writer lane; no
`store/` write, no pinned-tier run. One `reports/` write: the 76 sidecars' catalogue-version lines
(check-interpret goes red without it, as at b124prep/b126prep).

**Branch**: `lane/b135prep` in `worktrees/b135prep`, not merged. Builds (main tree's `build/`, shared):
`build/pcrec-a15fb77b/`, `build/pcrec-7388f1c0/`. Scratch builds for the census layering:
`/var/tmp/b135scratch/pcrec-{32a1c91f0,82ff94323,631771b7f}` (abi 69 / 70 / 71, deletable, ~100 MB each).

## 1. The five abi steps: pcrec's claim vs what I measured

pcrec's own change log is `docs/dev/history/abi_changelog.md` (moved out of `match_api.md` §6 by its
[SPEC-CLEAN]); the movers tables are `docs/dev/lanes/revbuild_report.md` §2. Main-line commits:
69 = 32a1c91f0, 70 = 82ff94323, 71 = 631771b7f, 72 = a15fb77b, 73 = 7388f1c0.

| step | pcrec's claim | MEASURED |
|---|---|---|
| 68->69 [DEC-VAR-ATTRIB] + [DEC-COLLAPSE-WASTE] | two stamp VALUES move, none added: nullable `${v}` reads `ENGINE_SEL selected`; a size-cap retry quotes the exact artifact's size (`-e utf8 (\p{Xwd})` 1028613 -> 1028607) | **Reproduced to the byte** at the abi-69 build (1028613 -> 1028607) and `${v}`: `declined-nullable-default` at 255bcdd8, `selected` at 32a1c91f0 and every later build. **0 of 1,365 census rows move**: no bench pattern contains `${`, and the collapse-waste rung is not offered on any bench pattern whose figure we assert. |
| 69->70 [MEMFN] R4e'.0b | every offset-skip/pre-check function keeps its loop under `<fn>__body`; text only; "+139..+184 B per FUNC; 326 asm movers" | **+139 (229 rows), +141 (87), +280 (78), +290 (34), +184 (12), +323 (2)**; 0 on 923. +323 is two functions (139+184). **326 census rows move at this step alone** (442 counting 70+72, 70+73) -- the same number as pcrec's asm movers by coincidence of two populations, not by construction. No stamp, no `rx_info` member. |
| 70->71 [MEMFN] RQ-3 | ONE stamp line on every artifact, `RX_SIMD_GUARDED_BYTES 0x...ULL`, always 0; "zero movers outside the new line" | **+52 B on 1,365 of 1,365 rows**, exactly; 0 in `vm_program_bytes`; stamp value 0 on every kind (plain DFA, forced VM, VM hybrid, rev-end DFA). |
| 71->72 [MEMFN] R-12 VMLAZY | the lazy rmin prefix respelled; only VM programs with a lazy quantifier of rmin > 0 on the cursor rung move; `vm_program_bytes` moves with the text | **4 census rows, +58 B each** (syntax `mod-u-uc` vm plain+whole; utf8 `qnt-lazy-2b` vm plain+whole), 1,361 rows 0. STAMP_CASE K41 witness 2: `vm_program_bytes` +1,800. |
| 72->73 [OPT-REVEND] L1 + L2 + stage 2 | end-pinned DFA body searches by the reverse-from-end walk (`RX_DFA_SCAN rev-end`, no forward machine); the generated absence rule moves `RX_DFA_START` -> `attempt-start` on attempt/empty bodies, empty `_match` -> `nomatch`; hybrids' inlined prefilter walks too; `-fno-rev-end`, `locate` axis. I-142 s1: the 15 tail cells stamp `engine=dfa, rev-end, reverse-pass, prefilter none, unwrapped`, caps == nocaps but the flags word | **All of it, to the letter** (section 3). 291 compiled census rows move `unanchored > rev-end`; **for all 291 `-fno-rev-end` at the pin reproduces a15fb77b's v2 program identity**; on every rev-end witness the denial reproduces a15fb77b's compiled `.text` AND its `emit_bytes`/`emit_code_bytes`/`vm_program_bytes` byte for byte. One stamp I-142 did not list: `req_why` is `dominated` on the two `.txt` patterns (`none` on `\d+$`, `\w+\z`, `\s+$`). |

`struct rx_info`: UNCHANGED across the whole span (28 members, compared field by field after stripping
comments at 255bcdd8, a15fb77b, 7388f1c0; only a comment on `search_form` gains the `attempt-start` word).
**Shim floor stays 16**; the abi-sabotage arms (`abi == floor-1` and the abi-5 one) pass in
`check_abi_floor_refusal`.

## 2. Code changes

- **Pin**: `configs.toml` `pin = "7388f1c0"`, `also_pins = ["a15fb77b"]`.
- **adapter.py**: `Adapter.pin()` honours `$PCRECBENCH_PCREC_PIN` (`PIN_OVERRIDE_ENV`) iff the value is in
  `also_pins` (anything else: `AdapterError ... is not a declared pin`, by name); declared values
  `dfa_scan += rev-end`, `dfa_start += attempt-start`, `dfa_match += nomatch`; new pair `simd_guarded_bytes`
  (`integer`, `INT_PAIRS`, `STAMP_SCOPE ("every", 71)`); `RX_DFA_SCAN` joins `REGISTRY_STAMP_PAIRS`
  (the `locate` axis lists `rev-end`/`unanchored` as `list` candidates; `attempt`/`empty` are
  `REGISTRY_OUTCOME_VALUES["dfa_scan"]`); `DENY_FLAGS += ("-fno-rev-end", "norevend", ...)` appended LAST.
- **shim.c / driver.c**: `pb_has_simd_guarded_bytes`/`pb_simd_guarded_bytes` (`unsigned long long`),
  `info simd_guarded_bytes`. `timed.c`/`timed.h` UNTOUCHED (`git diff master` empty).
- **scripts/run_window.sh**: a `$TESTEES` entry may be `testee@PIN`; the cell runs under
  `env PCRECBENCH_PCREC_PIN=PIN`, a bare entry under `env -u PCRECBENCH_PCREC_PIN`; the log, retry and
  sentinel logic are unchanged.
- **tools/selfcheck.py**: `B135_SIMD_GUARDED_LINE` (52), `B135_RESID` (12 per-row residuals for abi 70/72,
  `_b135_moved` layered after `_b126_moved`), three STAMP_CASES values (`dfa_start attempt-start` on the
  `attempt`, empty and K41-witness-2 rows; `dfa_match nomatch` on the empty row), the "dfa_start is not a
  constant" check now asserts THREE values, 10 LEDGER_STAMP_CASES rows (the five capability tail patterns x
  `pcrec-auto` / `pcrec-nocaps`, I-142 s1 by value), the size rows of three DENY_CONTROLS (+52), one new
  DENY_CONTROLS row (`-fno-rev-end`: `dfa_scan rev-end > unanchored`, `dfa_prefilter none > byte-class-bounded`),
  `B124_LATER_DENIES += -fno-rev-end` (the [B122] END-view chain `(?:[a-z]{0,64})\z` is end-pinned, so the
  view-edge denial alone no longer reproduced c4c70f2c's program -- inert on every non-end-pinned row),
  `check_b135_stamps` (20 checks), `check_b135_two_pin_window` (5 checks), `B135_CASES`, `B135_SIZES`.
- **Registries re-archived** (testees/pcrec/list_{axes,definitions,limits,schema}.tsv; the bench header
  chain keeps the 255bcdd8 header under a "PREVIOUS archiving" line; the verbatim body ends the file and is
  asserted byte-equal to the pin's live output by the existing `check_list_*_registry`).
- **Catalogue 3.17** (`[[pin_order]]` appended with BOTH pins, `a15fb77b` then `7388f1c0`, adjacent) +
  76 sidecars' catalogue lines, `catalogue/CLAUDE.md`.
- Docs: `testees/pcrec/CLAUDE.md` ("Re-pin at 7388f1c0 ... and the TWO-PIN window"), root `CLAUDE.md`
  (status sentence + the testees pin paragraph, APPLIED), `docs/dev/pcrec_references.md`,
  `docs/dev/measurements/CLAUDE.md`, `scripts/CLAUDE.md`.
- **No new pinned testee** (said explicitly, as asked): the AFTER's deny twin is not needed -- the window's
  before/after IS the two pins, and `-fno-rev-end` at the pin reproduces the BEFORE byte for byte
  (section 3), so a `pcrec-auto-norevend` pair would measure the BEFORE a second time at a worse
  discipline (a denial inside the AFTER's own compiler instead of the BEFORE's actual pin). `DENY_FLAGS`
  is in place, so adding the pair later is two `configs.toml` entries. The flag is reachable today as
  `PCREC_LOCAL_FLAGS="-fno-rev-end"` at the scratch tier.
- **Not changed, on purpose**: the pinned-testee count stays at forty-eight (+ `pcrec-local`).

## 3. The rev-end stamps BY VALUE (I-142 section 1)

`LEDGER_STAMP_CASES` (10 rows, mechanism check 141/0) and `B135_CASES` (the literal patterns at BOTH pins
through the adapter, plus `.text` identity):

| pattern (capability@0.2) | abi 72 (a15fb77b) | abi 73 (7388f1c0) | 73 + `-fno-rev-end` | emit_bytes 72 -> 73 |
|---|---|---|---|---|
| tail-digits-eol `\d+$` | unanchored / byte-class-bounded / reverse-pass / unwrapped / req_why none | **rev-end / none / reverse-pass / unwrapped / none** | == 72 | 25,328 -> 20,619 |
| tail-word-eoz `\w+\z` | same | same as above | == 72 | 32,145 -> 23,624 |
| tail-space-eol `\s+$` | same | same as above | == 72 | 26,791 -> 22,483 |
| tail-ext-lower-txt `[a-z]+\.txt$` | unanchored / byte-class-bounded / req_why emitted / libc memchr,memcmp | rev-end / none / **req_why dominated** / libc none | == 72 | 26,223 -> 20,607 |
| tail-dotstar-txt `.*\.txt$` | unanchored / **memchr-bounded** / emitted | rev-end / none / dominated | == 72 | 29,993 -> 23,808 |

Each under BOTH `pcrec-auto` and `pcrec-nocaps` (engine=dfa, engine_sel=selected, `simd_guarded_bytes` 0).
Caps and nocaps artifacts differ in the `#include` line and `.flags` (`0ULL` vs `4ULL`) ONLY, asserted on
all five (`diff` of the emitted `.c`). Beyond the tail family: stage 2 (`(a+)+b$` is a VM hybrid whose
inlined prefilter walks: rev-end / none / dominated; 72: unanchored / memchr-bounded / emitted); the
absence rule (`^abc$`: attempt / **attempt-start** / search-filter, was `reverse-pass`; the empty body
`[^\x00-\xff]`: empty / attempt-start / **nomatch**, was `reverse-pass` / `search-filter`, 22,995 -> 22,575
B emit incl. comments); scope (forced-VM `\d+$` carries no `dfa_*` pair); a control (`abc`: unanchored,
run-pinned, `.text` identical at both pins).

## 4. Registry deltas (each archive diffed against 255bcdd8's)

| surface | 255bcdd8 | 7388f1c0 | delta |
|---|---|---|---|
| `--list-axes` main | 136 rows / 46 axes | **161 / 49** | +21 rows/+2 axes are [DEC-FALLBACK] B7 (I-140; NOT an abi event; already 157/48 at a15fb77b): `fallback` 11 rows and `prefilter-admit` 10 rows, `kind=list`, EMPTY stamp_macro/stamp_value (never bucket on them); `engine-route` orders 3/4 swapped; `kind` predicate->list on engine-route/size-term/prefilter-lang. +4 rows/+1 axis are REVEND: `locate` (1 `rev-end` RX_DFA_SCAN deny PCREC_NO_REV_END bit 52 `-fno-rev-end`; 2 `unanchored`), `match` 3 `nomatch`, `search-start` 3 `attempt-start` (predicate), `match` 2's applies text. `#section memfn` still 0 rows. |
| `--list-limits` | 73 | 73 | byte-identical data rows |
| `--list-definitions` | 75 | 75 | byte-identical |
| `--list-schema` | 79 | 79 | byte-identical |

**[B131]'s reader audit** (I-140: "readers keyed on (axis, order) or `kind`"): grep over `tools/`, `pcrecbench/`,
`testees/pcrec/adapter.py`, `catalogue/`. Registry rows are read by `adapter.registry_rows()` only, and every
consumer keys on `axis` + `candidate` / `cli_flag` / `deny_bit` / `stamp_macro` / `stamp_value`:
`check_deny_flag_controls` (first row of the axis carrying a `-f` cli_flag, or the one named by the row's
`pick`), `check_noreqbyte_testee`, `check_noedge_axis`, `check_b126_stamps` (keyed (axis, candidate)),
`registry_check`. **NO reader keys on a numeric `order`** (the engine-route 3/4 swap moves nothing). `kind`
is read in ONE place, `registry_check`'s `kinds[...]` (it decides whether the reverse check applies), and
the two new descriptive axes cannot reach it (empty stamp_macro, not in `REGISTRY_STAMP_PAIRS`). The
`#section` main-table selection (`registry_main_lines`) is exercised by `check_list_axes_registry` (main 161
+ section 0 = 161 data lines; the synthetic 0-row and 1-row sections still parse). `axes` count prose
elsewhere ("136/46") is history in dated sections, not a live reader.

## 5. Census (docs/dev/measurements/2026-10-10-b135prep-census.txt)

Compile-only, `probe_b135_census.py`: 1,468 rows = 367 patterns of 9 sets x {plain, whole} x {auto, vm},
each hashed (v2) at the six builds 255bcdd8 / 32a1c91f0 / 82ff94323 / 631771b7f / a15fb77b / 7388f1c0.

| result | rows |
|---|---|
| identical | 744 |
| changed | 621 = 70 only 326, 70+72 2, 70+73 114, 72 only 2, **73 only 177** |
| refused-both | 97 |
| **refusal movers** | **6** (all at 73) |
| steps 69, 71 | 0 rows (69: values only; 71: a stamp line the v2 normalization drops) |

- **Step 73 = 291 rows (177 + 114) = exactly the rows whose `RX_DFA_SCAN` moves `unanchored > rev-end`**, and
  `denyrev` says `-fno-rev-end` at the pin reproduces a15fb77b's v2 identity for **291 of 291**; it is inert
  on the 1,074 compiled non-rev-end rows. Of the 297 rev-end rows, **285 are the whole-subject
  (`(?:...)\z`) artifact** and only 12 are plain-form (capability: letters-bounded-tail-z, the five tail
  patterns, wild-semdiv-dollar-trailing-newline-pcre2; litrun ctrl-abc-dollar; sentinel
  wild-semdiv-...; syntax anc-dollar, anc-z-uc, anc-z-lc). All are `auto`; no `vm` row.
- Stamp moves: prefilter `> none` 291 (+6), `req_why emitted > dominated` 81, `dfa_start reverse-pass >
  attempt-start` 74 (attempt loops and empty bodies), `dfa_match search-filter > unwrapped` 12, `engine_sel
  size-cap-retry > selected` 13.
- Population by set (`auto`, plain form): DFA-routed / unanchored (the START-LANDING population) / rev-end:
  altwide 34/34/0, bounded 37/37/0, **capability 36/23/7**, **email 3/3/0**, **litrun 12/11/1**, **loglines
  10/10/0**, sentinel 11/4/1, syntax 57/50/3, utf8 68/64/0. Whole form rev-end: altwide 39, bounded 38,
  capability 41, email 3, litrun 14, loglines 11, sentinel 5, syntax 69, utf8 65.

## 6. Size books (measured at all six builds, per witness)

- abi 69: 0 B everywhere (1,365 rows); abi 70: per function, +139..+323 B (`B135_RESID`'s 12 rows hold the
  asserted ones); abi 71: **+52 B exactly on 1,365/1,365**; abi 72: 0 on 1,361 rows, +58 on 4.
- abi 73, **rev-end artifacts SHRINK** (the forward machine is gone): `\d+$` 25,328 -> 20,619 B (-18.6 %),
  `\w+\z` -27 %, hybrid `(a+)+b$` -10 %; census median -17.5 % (-5,794 B), plain-form rows -4.2 KB .. -62 KB.
  Non-rev-end artifacts: +2 B on `^abc$` (attempt loop), -199 B on the empty engine, 0 on `abc` and forced VM
  (the census's +94/+96 B per non-rev-end row is COMMENT text; the adapter's comment-excluded `emit_bytes`
  moves 0 -- `abc` 21,515 at both pins).
- The ledger / STAMP / DENY_CONTROLS rows were re-measured, never typed flat: first pass 42 size/stamp reds;
  the fit script (`/var/tmp/b135/fit_resid.py`, not committed) printed `got - (old books + 52)` per
  (label, form): 69 rows +0, 12 rows non-zero (+139 x6, +141, +184, +280, +2, and K41 witness 2 +1,800 in
  `vm_program_bytes`) -- every non-zero one attributed to a step by the census columns above.
- **The abi-69 size-cap figure** moves again at 71: `(\p{Xwd}) -e utf8` 1028613 (255bcdd8) -> 1028607 (69)
  -> 1028659 (71+) by direct emit; through the ADAPTER's argv (which carries `-fcomments`) the pin reads
  1028666. Both are asserted where they are read.

## 7. The two-pin window mechanism

- `testees/pcrec/configs.toml`: `pin` + `also_pins`. `Adapter.pin()` (and so `pin.sh`, `describe`, the
  build provenance, the `rxt_source` message) honours `$PCRECBENCH_PCREC_PIN`. testee_id comes from
  `describe()`'s engine_version, so **one config derives `pcrec_a15fb77b_auto-caps-simdna` and
  `pcrec_7388f1c0_auto-caps-simdna`** (differ in the pin alone) and the records cannot collide in the store.
- `scripts/run_window.sh`: `TESTEES="pcrec-auto@a15fb77b pcrec-auto ..."`. Rehearsed (below) end to end.
- **ONE driver build.** The workdir is `build/work/<config id>` (no pin in it) and `build_driver` rebuilds
  only when `driver.c`/`timed.c`/`timed.h` are newer than the binary: `pcrec-auto@a15fb77b` and `pcrec-auto`
  share one cached `pcrec_driver` (asserted: same sha256 AND mtime after the second `prepare`).
  `pcrec-nocaps` has its own workdir and so its own build from the same source, flags and compiler --
  MEASURED **byte-identical** to `pcrec-auto`'s (sha256 `2c5061115e52...`). The shim is compiled per
  artifact from the same `shim.c` at both pins. So the instrument term (O-94) cannot differ between the
  two states within a testee, and does not between testees.
- **Rehearsal** (`SUBBENCH=sentinel TESTEES="pcrec-auto@a15fb77b pcrec-auto pcrec-nocaps
  pcrec-nocaps@a15fb77b" scripts/run_window.sh --dry-run`, scratch store `/var/tmp/b135/scratch-store`,
  synthetic, one trial, ~6 min): four cells, all rc=0, FOUR distinct testee_ids in one index
  (`pcrec_a15fb77b_auto-{caps,nocaps}-simdna`, `pcrec_7388f1c0_auto-{caps,nocaps}-simdna`). It ran the
  driver (calibration included) at the scratch tier on a not-quiet box: statuses `inconclusive-load` /
  `measured` mean nothing, and no number from it is used. It is a rehearsal, not a measurement; say so if
  the "no timed run" line is read strictly.
- **Re-pin control** ([B133], BD16): step 1 (object level) DONE --
  `docs/dev/measurements/2026-10-10-b135prep-isolation-proof.txt`: 7 IDENTICAL, 0 DIFFERS, every shim
  wrapper `aligned(64)` on both artifact kinds, the pre-B133 positive control firing 4/4. `timed.c`/`timed.h`
  untouched, so the isolation is structural. Step 2 (the timing A/B/A/B, `scripts/instrument_ab.sh`) is
  **OWED** to the manager's quiet box (the minimum cell list is in the control's text; `bench/sentinel` in the
  window reads the same thing).

## 8. Validation

- `check-harness` MINUS `check_expectations`, first pass (`/var/tmp/b135/harness1.log`, run on the unfixed
  tree after the pin swap and the new reader): 665 pass / 46 red. 4 are the known ENVIRONMENTAL reds (pruned
  old-pin builds: `gen_patterns --check` cd371441, KB-35 x2 25b1984f, b108 mover 751b9c6d). The other 42:
  27 size rows (+52 and residuals), 3 STAMP_CASES values, 1 "dfa_start constant", 3 DENY_CONTROLS size
  rows, 1 b122 identity arm (END-view chain), and the rest the same families. All fixed (section 2).
- After the fixes, re-run groups: `check_mechanism_stamps` **141/0** (incl. the 10 new tail rows),
  `check_deny_flag_controls` + `check_b122_round1_stamps` + `check_b124_stamps` + `check_b126_stamps` + the
  three registry checks + `check_emit_size_port` + `check_abi_floor_refusal` + `check_program_sha256`
  **231/0**, `check_b135_stamps` **20/0**, `check_b135_two_pin_window` **5/0**.
- **Final `make check`** (all seven targets): see section 11 -- harness 753 passed / 4 environmental.

## 9. Findings pcrec did not predict (candidate outbox items)

1. **Six refusal movers**: altwide `w-1024, w-2048, s-2048, s-4096, clsa-1024, clsd-1024` (whole-subject
   form, auto) were refused at EVERY build 255bcdd8..a15fb77b and COMPILE at 7388f1c0 (465,897 -
   986,183 B). The altwide cell gains new compile outcomes; it is not a speed delta.
2. **13 rows go `engine_sel size-cap-retry > selected` and GROW** (+36 KB .. +460 KB; altwide w-256, w-384,
   srt-256, ci-256, cnt-64, wb-256, clsa-256, clsd-256, pfx3-512, sfx-512; capability
   wild-logparse-syslogbase-expanded; utf8 prp-l, prp-notl): rev-end drops the forward machine, so the size
   cap that used to shed the prefilter / anchored match machine no longer fires. 12 of them also move
   `dfa_match search-filter > unwrapped`. A speed read on those cells mixes REVEND with the restored
   prefilter -- not a tail-cell issue, but any set-grain mean over altwide/utf8 whole forms is.
3. **REVEND is overwhelmingly a whole-subject-form event**: 285 of 297 rev-end rows are the
   `(?:...)\z` artifact of the MATCH regime; only 12 patterns (7 in capability) are rev-end in the SEARCH
   regime. I-142's "tail cells" are search-regime cells and sit among those 7; the match regime of nearly
   every set moves too.
4. **`req_why` is the stamp I-142 s1 left out**: `dominated` on the two `.txt` patterns, and 81 census rows
   in all go `emitted > dominated`; `memfn_libc` `memchr,memcmp > none` with it.
5. **abi 72 stamped `RX_DFA_START reverse-pass` on attempt loops and empty engines** (74 census rows) -- a
   pass never run; abi 73 corrects it to `attempt-start`. Any cross-pin bucketing on `dfa_start` moves those 74
   rows BY DEFINITION, not by behaviour.
6. `RX_DFA_SCAN` was not in the registry's stamped macros before the `locate` axis; it now is
   (`REGISTRY_STAMP_PAIRS`), so a pcrec change to its candidates fails a check by name.
7. The abi-69 `${v}` mover is unreachable through this shim (no buildable caller-variable artifact);
   asserted by direct emit only. A real `${...}` bench set would need the shim to supply a `vars` table.
8. `b108 acceptance mover`/KB-35/cd371441 pruned-build reds persist exactly as at b126prep (one `pin.sh <sha>`
   each clears them).

## 10. WINDOW PLAN (states 1 + 2 in ONE window; NOT RUN)

**Cells.** Priority order; `ABBA` within a set (`before after | nocaps-after nocaps-before`) so linear drift
cancels and each pair sits minutes apart. Competitors are REUSED (capability@0.2 at 255bcdd8 is in the
store); `pcre2-jit` runs only as the sentinel's flat control.

| # | set | why | cells | est. cell (min) | est. total |
|---|---|---|---|---|---|
| 0 | `sentinel` (auto-prepended) | instrument + flat control, BEFORE | pcrec-auto@a15fb77b, pcrec-auto, pcrec-nocaps, pcrec-nocaps@a15fb77b, pcre2-jit | ~6 (UNMEASURED: first sentinel cells; the 1-trial rehearsal took 1.4 min) | ~30 min |
| 1 | **`capability`** (@0.2) | **the O-91 (c) acceptance cells**: the 5 tail patterns x `t-tail-{digits,txt,space}-1m` (15 cells), `tail-space-eol` x `t-trim-nearmiss-16k`, and the throughput regime (large-subject); 36 DFA-routed patterns, 23 unanchored plain (START-LANDING population), 7 plain-form rev-end | pcrec-auto@a15fb77b, pcrec-auto, pcrec-nocaps, pcrec-nocaps@a15fb77b | 51.8 auto / 47.0 nocaps (255bcdd8 gaps) | ~198 min |
| 2 | `loglines` (@0.1) | 10 DFA-routed, all unanchored plain; 11 whole-form rev-end; the cheapest broad DFA set | same four | 9.7-12.1 | ~44 min |
| 3 | `email` (@0.2) | 3 DFA, 3 whole rev-end; the [OPT-5] originals | same four | 5.7-8.0 | ~32 min |
| 4 | `litrun` (@0.1) | 12 DFA / 11 unanchored plain + the rev-end `ctrl-abc-dollar`; 14 whole rev-end | same four | 15.7-17.1 | ~68 min |
| 5 | `sentinel:end` | instrument + flat control, AFTER | same five | ~6 | ~30 min |

Tier-1 total **~402 min = 6.7 h** (26 cells) + 15 s sleeps; fits one night with the retry budget. Per-cell cap
5400 s is above every figure (worst: capability auto 52 min). **Tier 2, appended behind `STOP_AT` only**:
`bounded` (@0.3: 37 DFA-routed unanchored, 38 whole rev-end; 4 x ~50 = ~200 min) and `syntax` (@0.1: 57 DFA, 50
unanchored plain, 69 whole rev-end; 4 x ~43 = ~172 min). **Deliberately EXCLUDED: `altwide`** (new compile
outcomes at 7388f1c0 -- the six refusal movers -- and 13 size-cap-retry flips make a speed read ambiguous; 18
min cells but 34 patterns of one shape) and `utf8` (no plain-form rev-end; 64 unanchored plain, 40 min x 4,
pure START-LANDING material for state 3's own window). Counts per set: section 5.

**Testees**: `pcrec-auto` and `pcrec-nocaps` at both pins (`pcrec-auto@a15fb77b`, `pcrec-auto`,
`pcrec-nocaps`, `pcrec-nocaps@a15fb77b`). Testee ids: `pcrec_{a15fb77b,7388f1c0}_auto-{caps,nocaps}-simdna`.

**How both pins share one driver build.** Section 7: workdir `build/work/<config id>` carries no pin; the
cached `pcrec_driver` is rebuilt only if `driver.c`/`timed.*` are newer. Before launch, in the MAIN tree after
the merge: build once and log the hashes --

    cd /home/duxevents/pcrec-bench
    for s in a15fb77b 7388f1c0; do sh testees/pcrec/pin.sh --path $s; done      # both exist
    python3 bench/sentinel/gen_subjects.py        # bench/sentinel/subjects is NOT generated in the main tree
    python3 -m pcrecbench testees | grep -c pcrec  # 49
    python3 -m pcrecbench quiet --samples 5

    # after the FIRST sentinel cell lands (the driver is built and cached by then), and again at the close:
    sha256sum build/work/pcrec-auto/pcrec_driver build/work/pcrec-nocaps/pcrec_driver   # must be equal, and unchanged

**Invocation** (sentinel FIRST by construction: `run_suite.sh` prepends it; a `sentinel:end` pass closes).
Do NOT set `PIN` (that is the CPU core) or `PCRECBENCH_PCREC_PIN` (the per-cell script sets it):

    cd /home/duxevents/pcrec-bench
    SUITE="sentinel capability loglines email litrun sentinel:end" \
    TESTEES_sentinel="pcrec-auto@a15fb77b pcrec-auto pcrec-nocaps pcrec-nocaps@a15fb77b pcre2-jit" \
    TESTEES_sentinel_end="pcrec-auto pcrec-auto@a15fb77b pcrec-nocaps@a15fb77b pcrec-nocaps pcre2-jit" \
    TESTEES_capability="pcrec-auto@a15fb77b pcrec-auto pcrec-nocaps pcrec-nocaps@a15fb77b" \
    TESTEES_loglines="pcrec-auto@a15fb77b pcrec-auto pcrec-nocaps pcrec-nocaps@a15fb77b" \
    TESTEES_email="pcrec-auto@a15fb77b pcrec-auto pcrec-nocaps pcrec-nocaps@a15fb77b" \
    TESTEES_litrun="pcrec-auto@a15fb77b pcrec-auto pcrec-nocaps pcrec-nocaps@a15fb77b" \
    NOTE="[B135] OPT-REVEND states 1+2: a15fb77b (abi 72) vs 7388f1c0 (abi 73), one window" \
    setsid scripts/run_suite.sh > /dev/null 2>&1 &

Completion: `build/windows/suite_*.log` ends `SUITE_RUN_COMPLETE` with per-set `rc=` lines; each set's own
log ends `WINDOW_RUN_COMPLETE cells=N/N`; expect 5/5, 4/4, 4/4, 4/4, 4/4, 5/5. To add tier 2:
`SUITE="... sentinel:end bounded syntax"` with `TESTEES_bounded`/`TESTEES_syntax` as above and
`STOP_AT="<date -d time>"`. `run_window.sh` regenerates the sidecars at the end of each set (canonical store).
`rc=4` (`inconclusive-spread`) cells are re-measured once by the script.

**What to read** (pcrec's predictions, I-142 s1; ns per call): no-match cells 7-24; `\w+\z` x tail-txt and
`\s+$` x tail-space 13-42; `\d+$` and `\w+\z` x tail-digits 19-60; `[a-z]+\.txt$` x tail-txt 22-66; `.*\.txt$`
x tail-txt 33-98; `\s+$` x t-trim-nearmiss-16k 7-24 (from 29,061). Failure signature: a 1 MiB cell above
~150 ns, or varying with body size, means rev-end did not run (check `dfa_scan` on the record first -- it must
read `rev-end` on the AFTER and `unanchored` on the BEFORE); a short cell at 40-60 ns with flat sentinels is
the instrument. The sentinel BEFORE/AFTER pair and `pcre2-jit` flat decide "instrument vs engine".

## 11. Final `make check` -- RESULT

Run by this lane at the end, sequentially and detached from the worktree (12:07-12:11 EDT for the tail;
the harness took ~27 min), logs `/var/tmp/b135/final_<target>.log`, markers `/var/tmp/b135/final_marker.log`
(`ALL_DONE`):

| target | result |
|---|---|
| check-schema | 6 accepted / 74 rejected for the intended rule / 0 wrong |
| check-harness | **753 passed, 4 FAILED -- exactly the four ACCEPTED ENVIRONMENTAL reds** (pruned old-pin builds, red on master too): `capability: gen_patterns.py --check` (build/pcrec-cd371441), `KB-35 build_census` and `KB-35 program_identity --check` (25b1984f), `b108 acceptance mover` (751b9c6d). `check_expectations` ran in full and passed. No other red. |
| check-interpret | 250 passed / 0 failed (was 249 at b126prep; sidecars at catalogue 3.17) |
| check-upstream | OK (14 findings, 3 threads) |
| check-frontpage | all PASS |
| check-trend | ALL PASS |
| check-report | rc=0 |

Compared with the first pass (665/46) the 42 non-environmental reds are all cleared; the harness gained 78
checks net (b126prep: 675 passed + 4 environmental = 679; now 753 + 4 = 757).

## 12. Charter-vs-committed checklist

| brief item | status |
|---|---|
| read BOILERPLATE; worktree `lane/b135prep` off master; WIP commits; no push/merge | done (commits `git log lane/b135prep`) |
| no `store/` write, no timed run | no store write; ONE scratch-tier synthetic `run_window.sh --dry-run` rehearsal (section 7), which exercised the driver but writes nothing under `store/`; no number used |
| how the harness selects a pin; how a two-pin window was done before | `configs.toml` single `pin` read by `Adapter.pin()`; before this lane every cross-pin report ([B25], [B34], [B122]...) came from windows at DIFFERENT times, one `pin` each (plan_completed.md [B25]/[B34]); there was no same-window mechanism -- built here |
| both pins buildable and runnable; ONE driver build; documented | done (section 7; `check_b135_two_pin_window`; `testees/pcrec/CLAUDE.md`; `scripts/CLAUDE.md`) |
| `pin.sh` both SHAs | done |
| read every abi step 69..73, claim vs measured | section 1 |
| new stamps -> shim/driver/adapter with STAMP_SCOPE at their abi; new deny flags -> DENY_FLAGS + DENY_CONTROLS; testee only if a twin is needed (say so) | `simd_guarded_bytes` (71, every); `-fno-rev-end` in both lists; NO new testee, reasoned (section 2) |
| I-142 s1 stamp set BY VALUE on the capability tail cells at 7388f1c0, caps/nocaps identical but flags, BEFORE values at a15fb77b by value | section 3 (LEDGER rows, `B135_CASES`) |
| shim floor; abi-sabotage arms | unchanged at 16; `check_abi_floor_refusal` passes |
| registries re-archived; [B131] audit; `#section` selection | sections 2, 4 |
| size books per witness | section 6 |
| compile-only program-identity census layered by abi step | section 5 + the archived census |
| catalogue `[[pin_order]]` BOTH pins in order; sidecars | 3.17; 76 sidecars |
| `make check`, check-interpret, check-report | section 11: DONE, all seven targets (harness 753/4 environmental) |
| CLAUDE.md (root testees line, testees/pcrec) | applied |
| WINDOW PLAN in the report | section 10: cells, testees, durations, the `run_suite.sh` invocation (sentinel first), the shared driver build |
| report with this checklist | this file |
| OWED | (1) the [B133] timing A/B/A/B at the new pin (manager, quiet box); (2) -- (done, section 11); (3) `plan.md`/journal STATE edits (manager); (4) the window itself |
