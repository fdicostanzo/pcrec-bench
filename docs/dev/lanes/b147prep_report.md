# lane b147prep report -- RE-PIN THE WHOLE ROSTER to 614d45eb3 (abi 89); also_pins 9ae59f5d4 (abi 84)

**Task**: plan row [B147], inbox I-162 / I-163 / I-166 / I-167. Writer lane (Sonnet); no `store/` write, no `reports/`
write beyond the sidecars' `catalogue:` line, NO timed run (a `quick --iters 1 --synthetic` scratch smoke validated the
record shape; every number here is a compile, an emit, a registry read or a log read).

**Branch**: `lane/b147prep` in `worktrees/b147prep`, not merged, not pushed. Build: `build/pcrec-614d45eb3/` (pin.sh, ~1 min,
source `~/projects/pcrec`, which HAS the sha). Scratch (deletable): `/var/tmp/pcrecbench/b147prep/`.

## 1. Claim vs measured (the five abi steps)

| step | pcrec's claim | MEASURED |
|---|---|---|
| 86 [EMIT-BIDI] | every artifact byte ASCII; `-fcomments` echoes spell non-printables `\xNN`; string literals use `\n \t \r`; em dashes in pcrec's prose -> `--`; no answer change | **Confirmed.** Over 1,500 census rows emitted WITH `-fcomments`: bytes > 127 in 1,407 of 1,407 artifacts at 9ae59f5d4 (the em dashes), **0 of 1,411** at 614d45eb3. `a<U+200E>b<U+200F>c` under `-e utf8`: 8 high bytes -> 0, echoed as `\xe2\x80\x8e`. Both comment-text probes we grep (`[OPT-5] SCAN EDGE:`, `NO RESUME FRAME AT ALL`) still find their text. **Not in the claim**: six bench rows (syntax `esc-tab`/`esc-nl`/`esc-cr` plain x caps/nocaps) change under program identity v2 AND v3 while the program is the same (identical once the literal escapes are respelled): `program_sha256`/`_v3` read a mover, and `RX_VM_PROGRAM_BYTES` (a text length) moves (`key\tvalue` forced-VM 330 -> 326). Counted sizes -2..-4 B on those six |
| 87 [SCANEDGE-SET] | an edge advances on a SET of byte classes; `\s+$` 1.17 -> 0.19 ns/B; 170 corpus artifacts gain a scan; no answer change | **Confirmed in kind.** `\s+$`: 0 edges/`none` -> 3/`bitmap`, counted 19,110 -> 25,455 B (code 15,565 -> 17,493); `-fno-scan-edge` restores the OLD PROGRAM (v3) at 19,111 B. No new stamp VALUE (the `scan-body` registry rows are byte-identical; `bitmap` already existed). **Our corpus: 38 rows / 13 patterns move**, not 170 (that is pcrec's corpus); caps rows' edge blocks 773 -> 798, 18 rows gain, none lose. Sizes +105 .. +6,650 B counted. **Side effect not in the claim**: with `-fno-start-set` the plain bounded skip loop is back and abi 87 collapses ITS class run too, so the [START-SET] denied arms no longer reproduce c4c70f2c's executed code (5 b124 identity witnesses) unless `-fno-scan-edge` is denied as well; and the `-fno-rev-end-onewalk` size pair on `\s+$` inverts (default 25,461 > denied 22,589: the denied two-seed walk takes no edges) |
| 88 [INLINE-C] stage 0 | comment-only, artifacts +2 B | **Confirmed.** v3-identical, counted size 0 B on all 1,363 identical rows (the +2 B is a comment; raw file sizes are not the counted size) |
| 89 [INLINE-C] stage 1b | callouts compile; `ca(?C1)t` does not link alone; VM-only; no prefilter | **Confirmed.** All 4 grp-callout rows (caps/nocaps x plain/whole) did-not-compile -> compile (24,914 / 25,138 B counted). `RX_CALLOUTS` + `RX_CALLOUT_BINDINGS` are in the HEADER; four sites / three names -> `rx_callout_3,rx_callout_foo`; `RX_ENGINE_WHY` `(?C1) at pattern offset 2`; `--engine=dfa` and `-fprefilter` refused by name; `nm -D` shows `rx_callout_1` UNDEFINED in the `.so` alone, DEFINED with the binding unit |
| 85 | reserved for memfn S3, skipped | **Confirmed**: `RX_ABI` reads 86 at the first step |

## 2. Code changes (all committed)

- **Pin**: `configs.toml` `pin = "614d45eb3"`, `also_pins = ["9ae59f5d4"]`. **6b2dbd3e LEAVES the allowlist** by the b142 rule
  (a retained pin is the BEFORE of something this re-pin measures; 9ae59f5d4 is the BEFORE of all five steps and the
  cross-window control, 6b2dbd3e of nothing). Its build stays; `testee@6b2dbd3e` is refused by name (asserted). **Flag for the
  manager**: the NOT-RUN b142 night chains (`b142win_chain.sh`, `b142win3_chain.sh`, `b142night_runbook.md`) name `@6b2dbd3e`
  and plain testees; at this pin the plain names measure 614d45eb3 and the `@6b2dbd3e` entries fail. They need re-aiming (or the
  allowlist entry back, one line) before launch.
- **adapter.py**: the callout binding. `callout_binding_source(symbols, header)` generates `callout_binding.c` (an `#include`
  of the artifact header, one `static ptrdiff_t pb_callout_pass(const rx_ctx *c){ (void)c; return RX_PASS; }`, one
  `const rx_callout_ref <name> = { pb_callout_pass, NULL };` per listed symbol); `_compile_one` reads the stamp
  (`text_stamps`, new key `callout_bindings`) from the emitted .h and adds the unit to the SAME gcc/clang command as shim.c.
  A SEPARATE translation unit, same compiler and flags, no LTO: each fire is one indirect call gcc cannot inline (the timed
  shape of I-166; a unity build would inline it). A pattern without the stamp gets NO unit. Two declared engine_metadata
  keys: `callout_bindings` (string, the stamp) and `callout_binding` (enum `separate-tu-pass`, present only with the first),
  so a record SAYS the shape. libpcre2 needs no change (no callout function set = the pass-through's equivalent, asserted).
  shim.c / driver.c / timed.* UNTOUCHED.
- **Shim floor STAYS 16**: `struct rx_info` is byte-identical to 9ae59f5d4's (637 chars); abi 86-89 add no field.
- **tools/selfcheck.py**: `check_b147_stamps` (34 checks, registered after `check_b142_stamps`): abi 89/84, the struct, the floor,
  EMIT-BIDI by value (bidi marks, raw high bytes, a literal respell with program-bytes 330 -> 326), SCANEDGE-SET by value
  (`\s+$` counts, stamps, sizes, deny == old program, a one-class control), stage 0, the callout stamps/route/refusals, link
  failure alone vs success with the binding (`nm -D`), pcrec-auto / -vm / -nocaps / -vm-in answering 5 subjects exactly as the
  oracle, `cat` getting no unit, pcre2-interp/jit answering `ca(?C1)t`. Re-aims: `check_b135_two_pin_window` (canonical
  614d45eb3, also_pin 9ae59f5d4, three retired pins refused), `check_b142_stamps` names its own builds (9ae59f5d4 vs 6b2dbd3e),
  the `-fno-rev-end-onewalk` DENY_CONTROLS size row (25,461 / 22,589), the b124 identity arm (+ `-fno-scan-edge` fallback).
- **Registries** (`testees/pcrec/list_*.tsv`, headers chained): axes 171 -> 172 rows (six descriptions lose their em dashes;
  `prefilter-admit` gains order 4 `callout`, old 4-10 -> 5-11); definitions 75 BYTE-IDENTICAL (eighth pin running); limits 103
  lines BYTE-IDENTICAL; schema +1 (`block callout`, `# schema-rows:` 77 -> 78). No new axis, no new deny flag, no new pinned testee.
- **Catalogue 3.21** (`[[pin_order]]` append) + 114 sidecars regenerated (`scripts/regen_sidecars.py`: 114, 0 failures).
- **Docs**: root `CLAUDE.md`, `testees/pcrec/CLAUDE.md` ("Re-pin at 614d45eb3"), `docs/dev/measurements/CLAUDE.md`,
  `docs/dev/pcrec_references.md`, `catalogue/CLAUDE.md`.

## 3. Census (docs/dev/measurements/2026-10-27-b147prep-census.txt + .tsv; `probe_b147prep_{emit,census,summary}.py`)

1,500 rows = every pattern of every sub-bench x {plain, whole} x {auto-caps, auto-nocaps}, emitted at both pins, plus the
`-fno-scan-edge` arm at 614d45eb3.

| form | identical | changed | refused-both | refusal movers |
|---|---|---|---|---|
| plain (750) | 672 | 31 | 45 | 2 |
| whole (750) | 691 | 13 | 44 | 2 |

Program identity: v3 as in b142 (the iterator scaffold is already in both pins). v2 reads 1,363 of 1,407 identical (the six
EMIT-BIDI rows differ under v2 too).

**Every one of the 44 changed + 4 refusal-mover rows is attributed (UNATTRIBUTED = 0)**: 38 abi 87 (rule: the `-fno-scan-edge` arm
restores the old program on 28, the other 10 change only the scan-family functions and the edge-block count); 6 abi 86 (identical
after respelling `\011 \012 \015` inside string literals); 4 abi 89 (grp-callout refusal movers, all compile now). Stamp moves with
no program move: `RX_DFA_SCAN_EDGE` on 36 rows (none/bitmap/range changes with the edges). Size books: **0 B on all 1,363
v3-identical rows** (pcrec's own `--warn-emit-bytes=1` numbers) — no flat term this time; movers carry their own deltas
(abi 86 -2..-4 B, abi 87 +105..+6,650 B emit / +105..+1,928 B code, abi 89 new rows).

## 4. Validation

- `check_b147_stamps` 34/0. Targeted groups before the final run: 119 checks in the re-aimed set (deny controls, b124, b142,
  two-pin, the three registries, emit-size port, abi floor) 0 FAILED after repairs; the first targeted pass found, and I repaired,
  exactly the reds attributed above (the `\s+$` deny size pair, five b124 identity arms, b142's canonical-pin assumption, the
  two-pin check) plus missing generated subject trees in a fresh worktree (not a regression).
- `quick --subbench syntax --pattern grp-callout --regime search --testee pcrec-auto --vs pcre2-jit --iters 1 --synthetic`
  (scratch store): both testees 3/3 correct, the record carries `callout_bindings: rx_callout_1`, `callout_binding:
  separate-tu-pass`, validator-accepted. (The 25.5x in its printout is a one-iteration smoke on a loaded box, not a number.)
- **FULL `make check`**: see section 7 (OWED if the marker is absent).

## 5. Findings for pcrec (candidate outbox items)

1. **[SCANEDGE-SET] changes the `-fno-start-set` / `-fno-offset-skip`-denied arms' programs** (5 b124 witnesses: `\bq\w*z`,
   `\b\d+x`, loglines bignum / uuid / kv-quoted): the denial's fallback loop is now edge-collapsed, so "denied == the pre-hat
   program" no longer holds without `-fno-scan-edge`. Not a bug; a reader trusting "abi 87 moves no hat-denied program" would be
   wrong. Worth a line in the abi log.
2. **EMIT-BIDI moves `RX_VM_PROGRAM_BYTES`** (a text length) on any VM artifact with a `\t \n \r` in a literal, with no
   program change: 330 -> 326 on `key\tvalue`. A consumer reading that stamp as a program size across the pin boundary sees a
   spurious -4. Ask: define the stamp on the pre-respell spelling, or note it.
3. **The callout artifact's size is the VM floor plus ~1.9 KB** and it is VM-only with no prefilter ("no prefilter yet",
   `prefilter-admit` `callout`): `ca(?C1)t` auto = 24,914 B, 323 ns for 3 tiny subjects vs pcre2-jit 8,247 ns in a one-iteration
   smoke. Every callout cell will measure the VM + one indirect call per fire; an [OPT-4.2]-style prefilter for callout
   patterns is the obvious customer.
4. `RX_CALLOUTS` counts sites the pattern NAMES, reachable or not (11.2 para 3), and `--emit-ir`'s `callout-sites` the reachable
   ones: the stamp cannot be used as a per-fire count.
5. bench/syntax P1's prediction ("`grp-callout` is `did-not-compile` on every pcrec testee", docs/dev/predictions/
   syntax-0.1-first.tsv and bench/syntax/NOTES.md) is now false at this pin: the interpreter's R-PRED will score it a miss on any
   syntax report at 614d45eb3 (ours; the prediction is dated 334fd10e).

## 6. Charter-vs-committed checklist

| brief item | status |
|---|---|
| BOILERPLATE; worktree `lane/b147prep`; WIP commits; no merge/push | done (`git log lane/b147prep`) |
| `pin.sh 614d45eb3`; configs pin + also_pins (9ae59f5d4 kept, 6b2dbd3e decided) | done, section 2 |
| registries re-archived, diffed, every delta explained | `testees/pcrec/list_{axes,definitions,limits,schema}.tsv`; section 2 |
| census, every mover attributed, archived | `2026-10-27-b147prep-census.txt` (+ `.tsv`), 0 UNATTRIBUTED |
| EMIT-BIDI: every comment-text probe still finds its text | yes (SCAN EDGE marker, NO RESUME FRAME), section 1 |
| SCANEDGE-SET: scan-edge stamp value set we read | unchanged (registry rows byte-identical); 38 movers attributed |
| callout binding per I-166, separate TU, recorded in engine_metadata | adapter.py + two declared keys; section 2 |
| harness check: grp-callout links and answers by the oracle on pcrec-vm and pcrec-auto; no TU without callouts | `check_b147_stamps` (also -nocaps, -vm-in, pcre2-interp/jit) |
| every new stamp/registry row asserted by value; shim floor decision | yes; floor STAYS 16 (rx_info byte-identical) |
| catalogue pin_order append + sidecars | 3.21; 114/0 |
| testees/pcrec/CLAUDE.md section, root CLAUDE.md | done |
| `make check` counts | section 7 |
| OWED | (1) `make check` result if section 7 has no result; (2) re-aim the b142 night chains (flag above); (3) a BD13 ruling whether program identity needs a literal-respell rule (6 rows read changed under v2 AND v3 with an unchanged program; the census attributes them with a census-side canonicalisation only); (4) bench/syntax NOTES P1 and the viewer data for `grp-callout`; (5) `FRONT_PIN`; (6) plan.md / journal STATE edits and outbox items (manager) |

## 7. MAKE CHECK

Command (from `worktrees/b147prep`): `make -k check > /var/tmp/pcrecbench/b147prep/final_check.log 2>&1`, detached.
Marker: the last line `DONE rc=<n>` in `/var/tmp/pcrecbench/b147prep/final_check.log`.
RESULT: OWED (launched before this report was finished; see the log).
