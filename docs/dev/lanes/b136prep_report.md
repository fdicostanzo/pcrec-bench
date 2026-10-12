# lane b136prep report -- RE-PIN to 6b2dbd3e (abi 76), also_pins 00c97769 (abi 75) + b8337c33 (abi 74)

**Task**: plan row [B136], inbox I-147 (sections 1, 2, 4, 6, 7) and I-148 section 1. Writer lane, Sonnet;
no `store/` write, no `reports/` write beyond the sidecars' catalogue-version line, NO timed run (every number
here is a compile, an emit, a registry read or a log read).

**Branch**: `lane/b136prep` in `worktrees/b136prep`, not merged, not pushed. Builds (main tree's shared
`build/`): `build/pcrec-00c97769/`, `build/pcrec-6b2dbd3e/` (b8337c33 existed). Scratch (deletable):
`/var/tmp/pcrecbench/b136prep/`.

## 0. Operational: ~/pcrec lacked both pins

Same as b135s3: `~/pcrec` is read-only (BD2) and had neither `00c97769` nor `6b2dbd3e`. Resolution inside the
mandate: `git clone --bare https://github.com/fdicostanzo/pcrec.git` + a no-checkout local clone at
`/var/tmp/pcrecbench/b136prep/pcrec`, then `PCREC_SRC=/var/tmp/pcrecbench/b136prep/pcrec sh testees/pcrec/pin.sh
<pin>`. The builds land at the normal paths, so later runs need no override. `b8337c33..6b2dbd3e` is 311
commits; `00c97769..6b2dbd3e` is the seam merge (4cd82e8d) plus [CAND-PATH-READS] (compiler-internal) and docs.

## 1. The two abi steps: pcrec's claim vs what I measured

| claim | MEASURED |
|---|---|
| abi 75: `RX_REQ_HANDOFF` also carries a K for a ONE-BYTE landmark: ipv6 "4", ipv4 "3", dotted4 "3", qnt-poss-brace "2", grp-atomic-alt "2", cls-s-ucp "4" | **Confirmed by value** (`check_b136_stamps`, 6 rows + the `none` at b8337c33 on each); census: these six are the ONLY patterns whose K goes `none` -> value |
| `RX_DFA_PREFILTER` gains `handoff`; 14 bench patterns move to it | **Confirmed**: under `--features all` the plain-form set is EXACTLY I-147's 14 (altwide sfx-64/256/512, bounded dotted4, loglines ipv4/ipv6/kv-quoted, syntax cls-fold-pair/cls-pair-ctl/mod-i/mod-r/qnt-poss-brace, utf8 ci-ascii-control/ci-strasse), each asserted with its b8337c33 prefilter and its K. grp-atomic-alt and cls-s-ucp take a K and KEEP `memchr`. **Not in I-147: a 15th mover under `--no-captures`** -- capability `wild-secrets-username-password-pair` (a VM artifact under caps; a DFA one under nocaps: `byte-class` -> `handoff`, K 0). Census: 14 movers caps, 15 nocaps, 0 whole-subject |
| `-fno-req-handoff`: removes BOTH handoffs, no new bit, listed on the `prefilter` axis | **Confirmed**: registry row `prefilter` order 5 `handoff`, deny bit 46, the same flag/bit as the `req-use` `handoff` row (the flag is on two axes now: asserted). It is the no-handoff artifact, NOT main-before-L1: `to-B` (reproduces b8337c33's v2 program) on 12/12 rows of the six K-new patterns x {caps, nocaps}; `differs` on every K82 mover (kv-quoted, sfx-*, cls-fold-pair, cls-pair-ctl, mod-i, mod-r, ci-*, the nocaps capability row) -- it also removes the K82 entry handoff the BASE had |
| Kit R-15: `MEMFN_LIBC` keeps `memchr` on dotted4/ipv4/ipv6/qnt-poss-brace | **Confirmed by value** at 00c97769 AND 6b2dbd3e (the relay draft that said otherwise is superseded, as I-147 states) |
| `-fno-req-run` no longer turns `REQ_HANDOFF` to `none` where a byte landmark exists | **Confirmed** (ipv6 under `-fno-req-run`: K "4", prefilter `handoff`). No existing control was keyed on the old equivalence (grep: the only `-fno-req-run` rows assert `req_run`/`req_why`/`vm_*`, not `req_handoff`) |
| abi 76: the seam helpers (span compare, caseless span, back-step) are `static inline`, no longer exported; no answer changes | **Confirmed** as program change on exactly 18 patterns (section 5). No adapter/driver/shim/tool symbol references `*_span_match` / `*_back_step` (grep of testees/, tools/, pcrecbench/, scripts/: the only hits are `selfcheck.py`'s historical text probes of OLD artifacts, `rx_bref_match`/`rx_span_match`, which read emitted text and are unaffected) |
| `struct rx_info` | **UNCHANGED across both steps**: the emitted struct (comments stripped, whitespace normalised) has md5 `11f44615bcfa6af1e48dd5b633c4f1c1` (580 chars) at b8337c33, 00c97769 and 6b2dbd3e. **Shim floor STAYS 16.** `git diff master -- testees/pcrec/{shim.c,driver.c,timed.c,timed.h}` is empty; `check_abi_floor_refusal` green (both sabotage arms) |
| [CAND-PATH-READS] (35c0b923): compiler-internal, no emitted byte moves | Consistent with the census: no row moves at 6b2dbd3e outside the 18 seam patterns |

## 2. Code changes

- **Pin**: `configs.toml` `pin = "6b2dbd3e"`, `also_pins = ["00c97769", "b8337c33"]` (a15fb77b and 7388f1c0
  leave the allowlist; their builds stay on disk). ONE driver build serves all three pins
  (`check_b135_two_pin_window`: same sha256, same mtime, no rebuild on the second/third prepare).
- **adapter.py**: `dfa_prefilter` values + `handoff`; source/description prose; `req_handoff` description
  (one-byte landmark K). The registry cross-check of declared stamp values vs the `prefilter` axis passes.
  `OFFSET_SET_VALUES` correctly does NOT gain `handoff` (offsets stay `none`; asserted per mover).
  `DENY_FLAGS`: `-fno-req-handoff` (`noreqhandoff`) and `-fno-rev-end` (`norevend`) already existed.
- **Four new pinned DENY testees**, by the composition rule (flag in `flags`, axis derived, `config_extra` word):
  `pcrec-auto-noreqhandoff`, `pcrec-auto-utf8-noreqhandoff` (ids `pcrec_<pin>_auto-caps-simdna_noreqhandoff`,
  `..._noreqhandoff-utf8`), `pcrec-auto-norevend`, `pcrec-nocaps-norevend` (`..._norevend`). They are measured at
  a NAMED pin via `testee@pin` (the chain uses `@00c97769` for the first two). Pcrec testees: 49 -> 53 listed.
- **shim.c / driver.c / timed.\***: UNTOUCHED (a `driver.c` comment still lists `dfa_prefilter`'s abi-64 set;
  editing it would rebuild the shared driver binary, so it is left as a flagged stale comment).
- **tools/selfcheck.py**: `check_b136_stamps` (30 checks, registered in `main()`): abi 74/75/76 off the three
  builds; the 14-row mover table by value (BASE prefilter, `handoff` at both new builds, K, offsets `none`, and
  the `-fno-req-handoff` arm at both); the 15th (nocaps) mover with its caps control; the six K values; the two
  K-without-prefilter rows; `-fno-req-run`; `memfn_libc` x4; the registry (`-fno-req-handoff` on `prefilter` AND
  `req-use`, bit 46). Repairs forced by the new behaviour, all MEASURED before typed: ledger ipv6 and kv-quoted
  now read `handoff` (ipv6 K "4"); the `-fno-offset-skip` deny rows on loglines uuid and on `abc` now land on
  `handoff` (the handoff row sits ahead of the hat/memchr in the `prefilter` table -- a finding), and the b124
  uuid arm needs `-fno-req-handoff` added to restore c4c70f2c's program; `B136_RESID` (-69 B emit and code) on the
  two backreference ledger rows (tag-pair-match, dup-param-detect); b126's poss-B identity arm is asserted at
  00c97769 (where `-fno-poss-bref-first` still reproduces 60366d747's `.text`) because the seam respells every
  backreference artifact; `check_b135_two_pin_window` and `check_b135s3_stamps` are re-aimed to name b8337c33
  BY NAME (the latter had used the canonical pin as "abi 74"); one new `DENY_CONTROLS` row
  (`-fno-req-handoff` read from the `prefilter` axis: ipv6 `handoff`/"4" -> `byte-class`/`none`).
- **pcrecbench/report.py**: `PREFILTER_VALUE_LEGEND` (`handoff`), printed ONLY when a row carries the value, so no
  committed report changes by a byte and the reporter version is NOT bumped (flag for the manager: bump with the
  first report that carries `handoff`). There is no other closed-set reader of `dfa_prefilter` in the reporter
  (the value is a pass-through in `_testee_legend_line`), the viewer, trend tools or the interpreter (grep). Test
  `test_prefilter_handoff_legend_b136`: 104 passed, 0 failed (was 103).
- **Registries re-archived** (headers chained, bodies verbatim, tested by `check_list_*_registry`): see section 4.
- **Catalogue 3.19** (`[[pin_order]]` + `00c97769`, `6b2dbd3e`; rules.toml note; catalogue/CLAUDE.md) + the
  sidecars' `catalogue:` line regenerated by `scripts/regen_sidecars.py` (not sed-edited; see section 7).
- **Docs**: root `CLAUDE.md`, `testees/pcrec/CLAUDE.md` ("Re-pin at 6b2dbd3e" + roster rows),
  `docs/dev/pcrec_references.md`, `docs/dev/measurements/CLAUDE.md`.

## 3. The movers by value (12 of the 14 shown; the other rows are in `B136_HANDOFF_MOVERS`)

| pattern | b8337c33 | 00c97769 = 6b2dbd3e | K | deny at 00c97769 | emit bytes B -> L |
|---|---|---|---|---|---|
| loglines ipv6 | byte-class, K none | **handoff** | 4 | none / byte-class (= BASE program) | 31,927 -> 31,179 |
| loglines ipv4 | byte-class, none | **handoff** | 3 | = BASE | 30,972 -> 30,224 |
| bounded dotted4 | byte-class, none | **handoff** | 3 | = BASE | 29,790 -> 29,042 |
| loglines kv-quoted | first-class-bounded, 32 | **handoff** | 32 | none / first-class-bounded (K82 also gone) | 45,625 -> 44,361 |
| altwide sfx-64/256/512 | byte-class, 9 | **handoff** | 9 | none (K82 also gone) | -1,258 B each |
| syntax qnt-poss-brace | memchr, none | **handoff** | 2 | = BASE | 24,314 -> 24,962 |
| syntax cls-fold-pair / cls-pair-ctl | memchr, 0 | **handoff** | 0 | K82 also gone | +134 B each |
| syntax mod-i / mod-r | byte-class, 0 | **handoff** | 0 | K82 also gone | -1,262 B each |
| utf8 ci-ascii-control | byte-class, 0 | **handoff** | 0 | K82 also gone | 26,927 -> 25,784 |
| utf8 ci-strasse | byte-class, 2 | **handoff** | 2 | K82 also gone | 33,849 -> 32,710 |
| syntax grp-atomic-alt | memchr, none | memchr (K only) | 2 | = BASE | +318 B |
| utf8 cls-s-ucp | memchr, none | memchr (K only) | 4 | = BASE | +438 B |

## 4. Registry deltas

| surface | b8337c33 | 00c97769 = 6b2dbd3e | delta |
|---|---|---|---|
| `--list-axes` MAIN | 163 rows / 49 axes | **164 / 49** | `prefilter` +1 row: order 5 `handoff` (RX_DFA_PREFILTER, deny PCREC_NO_REQ_HANDOFF bit 46, `-fno-req-handoff`), later orders shift 5-12 -> 6-13; the `req-use` `handoff` row's applies text reworded (one-byte landmark, [REQ-HANDOFF-L1]) |
| `--list-axes` `#section memfn` | 3 | **6** | +`vrun-trim`, `vrun-pad`, `precheck-assign-byte` ([MEMFN] denies, `--memfn=no-...`; read by nothing here, every reader selects MAIN) |
| `--list-limits` / `--list-definitions` / `--list-schema` | 73 / 75 / 79 | 73 / 75 / 79 | byte-identical |
| 00c97769 vs 6b2dbd3e | | | all four surfaces BYTE-IDENTICAL (abi 76 is a no-registry step) |

I-147's "listed on the `prefilter` axis": confirmed, and ALSO still on `req-use`; one flag, two rows, one bit.

## 5. Census (docs/dev/measurements/2026-10-12-b136prep-census.txt; `probe_b136prep_census.py`)

Compile-only, 1,468 rows = 367 patterns of 9 sets x {plain, whole} x {auto-caps, auto-nocaps}, each at all three
builds (v2 program identity) plus `-fno-req-handoff` at 00c97769 compared to b8337c33's identity.

| step | form | identical | changed | refused-both | refusal movers |
|---|---|---|---|---|---|
| L1 (b8337c33 -> 00c97769) | plain (734) | 654 | **33** | 47 | 0 |
| L1 | whole (734) | 688 | 0 | 46 | 0 |
| seam (00c97769 -> 6b2dbd3e) | plain | 651 | **36** | 47 | 0 |
| seam | whole | 652 | **36** | 46 | 0 |

**L1 attribution (every change)**: the 33 plain rows are 16 patterns x {caps, nocaps} + the nocaps-only capability
row; each moves `REQ_HANDOFF` and/or `DFA_PREFILTER`; nothing else moves (no engine/route/refusal change).
`[REQ-HANDOFF-L1]` is a SEARCH-regime event only: the whole-subject (rev-end) form moves 0 rows.
**Seam attribution (every change)**: 18 patterns x {caps, nocaps} x {plain, whole} = 72 rows, ALL `engine vm`:
backreference artifacts **-69 B** (capability doubled-word, dup-param-detect, phone-palindrome-6,
quoted-delim-match, tag-pair-match, tag-depth3-bound; syntax bak-1, bak-2, bak-g-rel, bak-k-named, bak-py,
mod-j-uc: 48 rows) and lookbehind artifacts **-29 B** (syntax lkb-pos, lkb-neg; utf8 asr-lb-fixed,
asr-lb-varwidth, asr-lb-neg, asr-lb-class: 24 rows). I-148's three predicted timing movers (bak-1, bak-2,
mod-j-uc) are inside the 18; the other 15 are program changes I-148 did not name (it expected "every other cell:
flat" in TIME; whether they move in time is the window's question).

## 6. Size books (measured, never a flat term)

abi 75 adds no stamp line and no flat per-artifact term: 1,342 of 1,375 compiled-both rows are byte-identical;
the 33 movers move per witness (section 3: -1,262 to +648 B). abi 76: 1,303 of 1,375 byte-identical; the 72 movers
are exactly -69 / -29. The ledger carries it as `B136_RESID` on the two backreference rows and the L1 moves as
by-value `dfa_prefilter` edits (no size assertion on a mover row broke).

## 7. Validation

- Targeted groups (`tools/selfcheck.py` functions, run via a scratch runner): `check_mechanism_stamps`,
  `check_program_sha256`, `check_deny_flag_controls` -> 179 pass / 0 fail (before the new deny row), then
  `check_b136_stamps` + `check_deny_flag_controls` again -> 60 pass / 0 fail (30 b136 + 30 deny controls incl. the
  new row); `check_b136_stamps`, `check_b135_two_pin_window`, `check_b122_round1_stamps`, `check_b124_stamps`,
  `check_b126_stamps`, `check_b135_stamps`, `check_b135s3_stamps`, `check_emit_size_port`,
  `check_abi_floor_refusal` -> 127 pass / 0 fail. The FIRST pass found 7 genuine reds (ledger ipv6/kv-quoted, two
  backreference sizes, two `-fno-offset-skip` deny rows, the b124 uuid + kv-quoted rows, the b126 poss-B identity,
  and the b135s3/two-pin checks that assumed the canonical pin was abi 74); every one attributed in section 2.
- `pcrecbench/tests/test_report.py`: 104 passed, 0 failed.
- check-list-axes/definitions/limits registries: archived == live (164/49 main, 75, 73), green.
- `scripts/run_suite.sh --dry-run` rehearsal of the new entries (`pcrec-auto-noreqhandoff@00c97769`,
  `pcrec-auto-utf8-noreqhandoff@00c97769`, `pcrec-auto-norevend`, `pcrec-auto@b8337c33`) on `email`: the FIRST attempt failed on the lane's own environment (the worktree had no generated email subject trees; rc=1 per cell, `WINDOW_RUN_COMPLETE cells=0/4`) -- after `gen_subjects.py`/`gen_throughput_subjects.py`, 4/4 cells ran synthetic into a scratch store and indexed under the derived ids `pcrec_00c97769_auto-caps-simdna_noreqhandoff`, `..._noreqhandoff-utf8`, `pcrec_6b2dbd3e_auto-caps-simdna_norevend`, `pcrec_b8337c33_auto-caps-simdna` (the `testee@pin` mechanism and the four new configs work end to end; the gate read NOT QUIET during the rehearsal -- pcrecdev1's load -- which the dry-run overrides)
- Sidecar regeneration (`scripts/regen_sidecars.py`): 87 sidecars, 0 failures (38 files differ, 76 lines: the `catalogue:` 3.18 -> 3.19 line only); `make check-interpret`: 261 passed / 0 FAILED; `make check-schema`: 6 accepted / 74 sabotages rejected / 0 WRONG; `make check-upstream` green
- FULL `make -k check`: **OWED** (BOILERPLATE: a run over ~4 min is the manager's to launch). Exact command, from the merged MAIN tree: `cd /home/duxevents/pcrec-bench && (setsid gnutimeout 10800 make -k check > /var/tmp/pcrecbench/b136prep/final_check.log 2>&1; echo "DONE rc=$?" >> /var/tmp/pcrecbench/b136prep/final_check.log) & disown`; marker: last line `DONE rc=<n>`. Expected: check-harness = the four known pruned-build reds only (`capability: gen_patterns.py --check` cd371441, `KB-35 build_census` and `KB-35 program_identity --check` 25b1984f, `b108 acceptance mover` 751b9c6d); the targeted groups above (the ones this change can move) are already green

## 8. WINDOW PLAN (NOT RUN): docs/dev/lanes/b136_chain.sh

`TIERS="1" setsid bash docs/dev/lanes/b136_chain.sh > /dev/null 2>&1 &` -- one tier per night, from the MAIN tree
after merge. `bash -n` clean. Entries: bare = canonical 6b2dbd3e, `@00c97769` = NEW (L1), `@b8337c33` = BASE.
Do NOT set `PIN` or `PCRECBENCH_PCREC_PIN`. Preconditions (`pin.sh --path` x3, sentinel subjects, quiet gate,
driver hash) are in the script.

**Cell lengths** (MEASURED from the latest windows' attempt timestamps, minutes per cell; `build/windows/window_*`
2026-10-05..11): pcrec: sentinel ~6.2, loglines ~8.4, email ~5.0, litrun ~12-14, altwide ~24 (@0.3), syntax ~44,
utf8 (-utf8) ~34-39, bounded ~50, capability ~47-49. pcre2: jit/interp loglines 8.4/8.8, email 11/8.5, bounded
18/23, syntax 40/54, utf8 (pcre2-utf-jit/-interp) 37.5/41.6, litrun ~14, sentinel pcre2-jit ~9. The largest cell
(bounded ~50 min) is far under `CELL_CAP` 5,400 s.

| tier | content | cells | est. |
|---|---|---|---|
| 1 | I-147 ask 1 + ask 7.3: sentinel open; loglines x {BASE, NEW, deny, canon}; altwide@0.3 x {BASE, NEW, deny, canon}; bounded x {BASE, NEW, deny}; sentinel:end1 | 5 + 4 + 4 + 3 + 5 = 21 | ~356 min (5.9 h) |
| 2 | ask 4 (litrun x {auto, auto-norevend, nocaps, nocaps-norevend}, canonical pin) + the tail/grok cross-window control (capability x {BASE, NEW, canon}); sentinel:end2 | 4 + 3 + 5 = 12 | ~240 min (4.0 h) |
| 3 | the other section-1 mover sets as smoke + I-148's seam movers: syntax x {BASE, NEW, deny, canon}, utf8 (-utf8) x {BASE, NEW, deny, canon}; sentinel:end3 | 4 + 4 + 5 = 13 | ~361 min (6.0 h) |
| 4 | ask 7.1: pcre2-jit + pcre2-interp on bounded, loglines, syntax, litrun, email; pcre2-utf-jit + pcre2-utf-interp on utf8 | 12 | ~279 min (4.7 h) |
| total | | 58 | ~1,236 min = 20.6 h (4 nights, one tier each; tiers 1-3 close with their own sentinel pass) |

What each cell answers: tier 1 = I-147 ask 1 / the section-2 table (BASE vs NEW vs deny on ipv6, ipv4, kv-quoted,
dotted4, sfx-64; the other 9 movers ride their sets; altwide runs WHOLE -- `run` has no per-pattern filter) and
ask 7.3 (the NEW and canonical altwide cells; jit/rust rows from 10-02 already exist). Tier 2 = ask 4 and I-147 ask 4
(tail family + grok "none should move at 00c97769": capability BASE vs NEW). Tier 3 = the "no cell worse than +3%"
smoke on syntax/utf8 and I-148's seam: canonical vs NEW on syntax (bak-1/bak-2/mod-j-uc predicted +13.5 / +9.7 /
+5.6 %). Tier 4 = ask 7.1.

**Answers to the questions put to this lane (from the driver protocol, `pcrecbench/adapters.py` top, and
`pcrecbench/reduce.py`)**: a cell is NEVER one call. The driver times a loop of `iters` calls on ONE subject
(`ITERS`, `SECONDS` per subject row); a set-grain `search_short` (or `match`, or whole-form short) cell is, per
trial, the SUM over the pattern's regime subjects of the per-subject ns/call, reduced over trials -- 75-112
subjects for utf8 search_short, `short_search_max_bytes` decides membership. **Therefore:** ask 6 (u8short): its
own stated disposition applies -- a total over 75-112 subjects makes the +10..92 ns a 0.1-1.2 ns/subject landing
guard cost, ACCEPT; the `-fno-start-landing -fno-start-width` arm is NOT built into the chain (it is owed only if the
read lane finds a residue the guard cost cannot explain; per-subject rows are in the records and the reporter's
`--grain subject` gives the per-call figure, so no new run is needed to see it). Ask 4 (rewtwin): the same -- a
whole-form short cell is the sum of one `rx_search`-equivalent per subject, not a single call; the same-pin
`-fno-rev-end` arm is in tier 2.

**Deny arm choice**: `pcrec-auto-noreqhandoff@00c97769` (caps only; the 14 movers are identical under nocaps
except the capability row, which no tier measures with a deny arm). No ask-2 / ask-3 / 5.2 / 7.2 / 7.4 arm is
built: they are read-lane work over these cells (7.4's sentinel jit row is already in every sentinel pass).

## 9. Findings pcrec did not state (candidate outbox items)

1. **A 15th `handoff` mover under `--no-captures`** (capability wild-secrets-username-password-pair); I-147
   lists 14 (caps). The pcrec-nocaps testees will show it.
2. **The seam step moves 18 patterns' programs, not three**: all VM; -69 B on 12 backreference patterns, -29 B on
   6 lookbehind patterns; I-148 named only bak-1/bak-2/mod-j-uc (timing).
3. **`-fno-offset-skip` now lands on `handoff`** wherever a handoff K exists (loglines uuid, `abc`): the handoff row
   sits ahead of the DFA hat and `memchr` in the `prefilter` table, so a deny arm that used to fall to
   `first-class-bounded`/`memchr` falls to `handoff`. Existing documentation that says "the denied arm reads
   first-class-bounded" is history.
4. **`-fno-req-handoff` is not a pre-L1 twin** on any K82 mover (census `differs`), only on the six new-K patterns
   (`to-B` 12/12) -- consistent with I-147 section 1, now measured over the corpus.
5. The `prefilter` axis lists `-fno-req-handoff` AND `-fno-start-set` on different rows: a deny-control row
   naming `prefilter` must name its flag (8th element), as b124 already learned.
6. ~/pcrec lagged both pins again (section 0): an operating note, not a pcrec bug.

## 10. Charter-vs-committed checklist

| brief item | status |
|---|---|
| read BOILERPLATE; worktree `lane/b136prep`; WIP commits; no merge/push | done (`git log lane/b136prep`) |
| pin.sh at all three pins; ONE driver build; configs pin + also_pins | done (section 0, 2); `check_b135_two_pin_window` |
| registries re-archived from 6b2dbd3e, every delta reported and explained | `testees/pcrec/list_*.tsv`; section 4 |
| `dfa_prefilter` closed set + `handoff` at every reader (reporter included) | adapter.py; report.py legend; no other reader (grep); section 2 |
| REQ_HANDOFF K values BY VALUE (6 rows) | `check_b136_stamps`, section 3 |
| 14-pattern mover list BY VALUE | `B136_HANDOFF_MOVERS` + the 15th nocaps mover |
| `-fno-req-handoff` DENY_FLAGS + DENY_CONTROLS | DENY_FLAGS row pre-existed (`noreqhandoff`); DENY_CONTROLS: the K82 row + the new `prefilter`-axis row |
| controls keyed on `-fno-req-run` => REQ_HANDOFF none | none existed (grep); the new equivalence asserted on ipv6 |
| `MEMFN_LIBC` stays `memchr` x4 | `check_b136_stamps` |
| no adapter/driver/shim symbol references `*_span_match`/`*_back_step` | grep (section 1) |
| shim floor / struct rx_info | unchanged, floor 16, md5 `11f44615...`; section 1 |
| size books measured | sections 5, 6; `B136_RESID` |
| catalogue `[[pin_order]]` both pins | 3.19 |
| compile-only census, per-step attribution | section 5 + the archive |
| chain script drafted, not run, with instrument/sentinel lead-in, cell count and length | `docs/dev/lanes/b136_chain.sh`; section 8 (58 cells, ~20.6 h, four tiers) |
| new deny testee configs by the composition rule | four, `configs.toml`; ids in section 2 |
| ask 6 arm only if a search-short cell is ONE call | it is not (section 8); no arm |
| `make check` green apart from the four known pruned-build reds | OWED/see section 7 |
| testees/pcrec/CLAUDE.md section; root CLAUDE.md pin line | done |
| OWED | (1) the full `make -k check` result (section 7); (2) the window (manager); (3) the reporter version bump with the first report carrying `handoff`; (4) plan.md/journal STATE edits (manager); (5) read-lane asks 2, 3, 5.2, 7.2, 7.4 after the window |
