# lane b142prep report -- RE-PIN THE WHOLE ROSTER to 9ae59f5d4 (abi 84); also_pins 6b2dbd3e (abi 76)

**Task**: plan row [B142], inbox I-154 / I-158 / I-159. Writer lane, Sonnet; no `store/` write, no `reports/`
write beyond the sidecars' `catalogue:` line, NO timed run (every number here is a compile, an emit, a registry
read or a log read).

**Branch**: `lane/b142prep` in `worktrees/b142prep`, not merged, not pushed. Builds (main tree's shared `build/`):
`build/pcrec-9ae59f5d4/` (pin.sh, 1 min), and `build/pcrec-600111e4e/` (the first parent of the subst merge, for the
[M4-SUBST] check; not an allowlisted pin). Scratch (deletable): `/var/tmp/pcrecbench/b142prep/`.

## 0. Operational

- `~/pcrec` HAD both shas this time (`git cat-file`: 9ae59f5d4, 6b2dbd3e); no throwaway clone needed.
- pcrec's CI on 47fddf283 was pending at I-159; I saw no pcrec test failure (I ran none).
- A concurrent lane (b140drv) edits the pcre2 driver and harness subst plumbing: I touched neither. Expect merge
  conflicts in `tools/selfcheck.py` (I added `check_b142_stamps`, re-aimed ~10 existing checks and added `B142_*`
  constants) and `tools/program_identity.py` (an additive v3 block before `pin_binary`).

## 1. Claim vs measured: the eight abi steps (and what I-159 did not list)

| step | pcrec's claim | MEASURED |
|---|---|---|
| 77 [COMPOUND] B4 (e842fe537) | every artifact gains `RX_COMPOUND` (`none` / a row name / `forced-off`); a pin-only pattern with a floor arm beside end-pinned arms emits a `split` compound; the route family's stamps read `compound`; `.h` and exported symbols are the plain artifact's; no struct offset, no answer moves | **Confirmed** by value (`check_b142_stamps`): `none` on 1,371 of 1,375 compiled-both rows, `split` on 4 (capability + sentinel `wild-waf-crs-942360-concat-sqli`, WHOLE-subject form only, 402,992 -> 516,567 B). Small witnesses: `x\z|^y`, `^a$|b$`, `\Ga$|b$`, `(?:a|b)+$|^c` -> `split`; `a$|b$` and `foo\z|[a-z]+x` -> `none`. On a compound `dfa_scan`/`dfa_scan_edge`/`dfa_start`/`dfa_prefilter`/`_offsets`/`dfa_table`/`dfa_match`/`req_why`/`req_handoff`/`vm_start_scan`/`end_window` read the token `compound`, `dfa_uniform_folds` and `run_words` read **-1**, and the parts' own stamps live in `RX__F_*` / `RX__Q_*` families. **Not in the claim: this broke the adapter** (two `_check_agreement` iffs; fixed). The compound compiles through the adapter and ANSWERS right through the driver (4 subjects, oracle-checked). No CLI deny flag exists (the lever is harness-internal); `forced-off` is unreachable here. In today's sets the compound form is one no declared regime times |
| 78 [OPT-REVEND] B3 (206cf0a0b) | only the `rev-end` walk of a `$`/`\Z` artifact moves beyond the abi digits (one-seed / tagged / two-seed forms); `-fno-rev-end-onewalk` (bit 56) restores the two-seed walk | **Confirmed**: 18 rows = 9 patterns x {caps, nocaps}, ALL plain form: capability tail-digits-eol, tail-dotstar-txt, tail-ext-lower-txt, tail-space-eol, wild-semdiv-dollar-trailing-newline-pcre2; litrun ctrl-abc-dollar; sentinel wild-semdiv-dollar-trailing-newline-pcre2; syntax anc-dollar, anc-z-uc. The deny arm == 6b2dbd3e's program (v3 identity) on 18 of 18. Sizes SHRINK 1.0-3.4 KB (`\s+$`: 22,478 -> 19,111 B; denied 22,584 = old + 106). The whole-subject form moves 0 rows; `tail-word-eoz` (`\w+\z`) does not move. `tail-space-eol` also moves `RX_DFA_SCAN_EDGE` bitmap -> none. Registry: NEW axis `rev-end-form` (5 rows), deny bit 56 on one-seed / tagged / two-seed |
| 79 RP + knowledge-stamp union (1c06b8a0c) | `FINDINGS` lists a query ANY attempt asked; only compiles whose consulting attempt was discarded move; the two F-5 witnesses read `byte-rate=none` where they read `""` | **Confirmed**: `(\p{Xwd})x` under `-e utf8 -fno-req-byte`: 6b2dbd3e `""`, 9ae59f5d4 `byte-rate=none`. Census: `RX_FINDINGS` moved on **0** of 1,375 rows (no bench pattern is an F-5 shape) |
| 80 [ENTRY-TABLE] E1 (7c0a90479) | `RX_PART_LAYOUT`/`_WHY` written only where a caller sets a part-layout control; no default artifact moves beyond the abi digits | **Confirmed**: absent on 1,375 of 1,375 default artifacts; `--part-layout=prefilter:shared` -> `"prefilter=shared"`, `--part-inline-rank=R3` -> `"rank=R3"`, `--part-residual=shared` -> `"residual=shared"`, `--part-layout=find:inline` -> `"find=inline/none"`. Registry: TWO new `#section` blocks (`part-layout`, `part-layout-table`), read by nothing. No pinned config passes a control; no adapter reader |
| 81 anchor fold P2a-P2e (d06b530f7, 73c2bb655, ee183c004) | `(?m)^`/`(?m)$` become `A_CTX` rows; `\A`/`\z` at the NFA then AST layer; only DFA atom order moves, and only where a `(?m)` anchor precedes a different context set (their probe: one mover in 2,451 patterns, `(?m)^a|\B`) | **Confirmed**: **0 bench rows** move. By value (v3 identity vs 6b2dbd3e, byte and `-e utf8`): `(?m)^a|\B` and `(?m)^a|\b` MOVE; `(?m)^a`, `\Aabc\z`, `(?m)a$`, `^abc`, `(?m)^foo|bar$`, `a|\B`, `(?m)^\w+|x$` do not |
| 82 [MEASURE-SET] M0 (813f43ec8) | `<PREFIX>_MEASURES` and `rx_info.measures` (appended after `findings`); `""` everywhere (no kit row reads a set key before B4) | **Confirmed**: `""` on 1,375 of 1,375. `struct rx_info` (comments stripped, whitespace-normalised) md5 `11f44615...` (580 chars) at 6b2dbd3e -> 637 chars at 9ae59f5d4; the old body is a strict PREFIX; the appended tail is exactly `const char *measures; rx_nextfn next; rx_nextnfn next_n;` (abi 82 + 84). **Shim floor DECISION: STAYS 16** -- see section 3 |
| 83 K128/K129 (bf33d2dab) | K128 (`X{m,}` m>=1 with a nullable body records its last mandatory iteration; the counter rung's slot pre-pass counts the guard) and K129 (`_vars_resolve` above the proof-based exits) + `vm_counter_fits` keeps `X+` off the counter rung at K=1; "bounded, rmin==0, non-nullable, possessive, var-free patterns emit the same text" | **Confirmed for the corpus**: K129 needs a variable and no bench pattern contains `${` (0 movers by construction); K128 moves exactly 2 rows: capability `evil-alt-nested` (`^(([a-z]+)*)+$`) caps x {plain, whole}, VM, +333 B (`--emit-ir`: labels 26 -> 28, events 89 -> 95). `^(([a-z]+)*)+$` forced-VM `vm_program_bytes` grows. No `X+` ladder row moved |
| 84 find-all iterators (b8c66a739) | every artifact gains `<prefix>_next` / `_next_n` and `rx_info.next` / `.next_n`; the iterator's text is scaffold (excluded from every length decision); `RX_ITER_RETRY` in {none, retry, retry-budgeted}; "no answer of an existing entry moves" | **Confirmed**, with two consequences pcrec's text understates: (a) the iterator is in EVERY artifact and every exported residual entry became a forwarder to a static twin, so **program identity v2 reads 0 of 1,375 rows identical** (section 5); (b) the emit-size definition now EXCLUDES the scaffold with no marker in the text, so the adapter's text port overcounts by 5,728 B (a plain DFA) to ~8.6 KB (section 4). `RX_ITER_RETRY`: none 1,291, retry 68 (all DFA), retry-budgeted 16 (all VM). The DFA retry MACHINE counts (see section 6) |
| [M4-SUBST] (9ae59f5d4) | not an abi event; 0 byte diffs over 112 compiles | **Confirmed on a larger population**: 9ae59f5d4 vs its first parent 600111e4e (already abi 84), RAW text with comments, every bench compile: **1,375 identical / 93 refused-both / 0 DIFFER** (`probe_b142prep_subst_noevent.py`) |
| NOT in I-159: [FLAG-SPELL] (flagfix, merged 187608482, no abi bump) | -- | **12 rows move and no abi step owns them**: VM programs whose pattern STARTS with an option run (`(?x)`, `(?i)`, `(?J)`): capability bracket-array-define x4, codegrammar-xflag x2, wild-secrets-slack-webhook-url x2, syntax mod-j-uc x4 lose a dead label (-50 B emitted, `vm_program_bytes` -57 on `(?i)abc`: 634 -> 577, pcrec's own note says +57 B). Two stamp-only side effects: `RX_REQ_RUN` `6174@0` -> `436174@0/dfffff` (syntax mod-reset, mod-unset: the necessary run grows from `at` to a caseless `Cat`), and 12 rows' `RX_ENGINE_WHY` NAMES a different forcing construct (`\1` -> `\3`/`\2`/`(?!...)`, `(?>...)` offset 14 -> 0) -- the route is unchanged |

## 2. Code changes (all committed on the branch)

- **Pin**: `configs.toml` `pin = "9ae59f5d4"`, `also_pins = ["6b2dbd3e"]`. **00c97769 and b8337c33 LEAVE the allowlist.**
  Decision by measurement: the census reads 6b2dbd3e as the ONE BEFORE of all eight steps, and both retired pins' own
  questions (I-147 ask 1, I-148 seam) were closed by the b136 windows; neither is the BEFORE of anything here, and every
  extra allowlisted pin is another build `check_b135_two_pin_window` and the window scripts must keep honest. Their builds stay
  on disk; `testee@00c97769` is refused BY NAME (asserted). ONE driver build serves both pins (same sha256, same mtime).
- **adapter.py**: (1) three TEXT-READ stamps in `METADATA_DECL` + `text_stamps()` (`compound`, `iter_retry`, `measures`;
  `findings`' shape, no shim getter); (2) the **size probe**: a second fixed protocol token `--warn-emit-bytes=1`
  (`WARN_PROBE_FLAG`, the `-fcomments` shape, never in `cfg["flags"]`), `parse_warn_line(last=True)`, `artifact_abi()`,
  `_emit_facts` takes pcrec's own numbers at abi >= 83 (`SCAFFOLD_ABI`) and keeps the text port as the byte-exact CONTROL
  below it; `warned_emit_bytes` and the stderr note are recorded only where the DEFAULT 250,000 threshold would have fired;
  (3) `scan_edge_counts`: `rx__find` joins the search side, `rx__retry*` is ignored, `__attribute__((..))` is stripped before
  a head is named; (4) `_check_agreement`: the offsets iff and the `req_why` iff accept the `compound` token; (5) `DENY_FLAGS`
  `-fno-rev-end-onewalk` (`norevendonewalk`).
- **shim.c / driver.c / timed.\***: UNTOUCHED.
- **tools/program_identity.py**: `normalize_v3` / `program_sha256_v3_of_text` (additive; v2 and the CLI untouched).
- **tools/selfcheck.py**: `check_b142_stamps` (27 checks, registered after `check_b136_stamps`); `B142_FLAT` (+106) and
  `B142_RESID` (five rows) with `_b142_moved` in the stamp/ledger chain; three DENY_CONTROLS size expectations re-derived
  (+106 / + the retry machine, +357,951 B on the uncollapsed 16384 DFA); one new DENY_CONTROLS row for `-fno-rev-end-onewalk`;
  `check_emit_size_port` runs BOTH binaries (equality at 6b2dbd3e, scaffold-delta + `_emit_facts` == pin at 9ae59f5d4);
  `check_b135_two_pin_window` re-aimed (canonical 9ae59f5d4, one also_pin, the two retired pins refused by name);
  `check_b136_stamps` names its three builds explicitly (6b2dbd3e is no longer canonical); the b122/b124/b126 `.text`
  identity arms hash the function SECTIONS the object shares with an abi-<83 one (`-ffunction-sections`, the iterator's
  `rx_next`/`rx_next_n`/`rx__*` excluded -- a whole-`.text` equality against any older pin can no longer hold, the scaffold
  is compiled into every object); the I-43 island/chain ratios use pcrec's own bytes (1.2330 / 1.2358 / 1.2632 vs
  c4c70f2c's 1.2344 / 1.2375 / 1.2649, inside the 0.005 tolerance); the folds-4 `.rodata` FINDING is re-aimed (the
  retry machine's tables keep it above zero: 294 B vs the folds-0 control's 838; `.text` rises ~0.8-1.3 KB on every object).
- **Registries re-archived** (headers chained, bodies verbatim, tested): section 4. **Catalogue 3.20** + the 97 sidecars'
  `catalogue:` line (`scripts/regen_sidecars.py`: 97 sidecars, 0 failures). **Docs**: root `CLAUDE.md`,
  `testees/pcrec/CLAUDE.md` ("Re-pin at 9ae59f5d4"), `docs/dev/measurements/CLAUDE.md`, `docs/dev/pcrec_references.md`,
  `tools/CLAUDE.md`, `catalogue/CLAUDE.md`.
- **NOT changed**: the reporter (closed-set readers pass `compound` through; no committed report moves; no version bump --
  a `compound` legend line and the bump belong with the first report that carries one), `FRONT_PIN` in the Makefile
  (stays 6b2dbd3e until records exist at the new pin), `record schema` (no new field).

## 3. The shim-floor decision (82/84 grew `struct rx_info`)

`PB_SHIM_MIN_ABI` (shim.c) STAYS **16**. The rule in shim.c's header: the floor moves only when the shim READS a field that
older artifacts lack. The three appended members (`measures`, `next`, `next_n`) are read by NOTHING here: `check_b142_stamps`
greps shim.c + driver.c for `PB_INFO.(measures|next|next_n)` and `RX_MEASURES|RX_ITER_RETRY|RX_COMPOUND` (0 hits) and asserts the
floor is still 16. The two abi-sabotage arms in `check_abi_floor_refusal` (abi 5 and abi 15 refused BY NAME, the unmodified
artifact loading at abi 84) are the control and are green. The new stamps are read from the emitted TEXT (the `findings`
precedent), so an abi-16..83 `pcrec-local` artifact still records them as "not stamped".

## 4. Registry deltas (vs 6b2dbd3e; every surface printed from both builds and diffed)

| surface | 6b2dbd3e | 9ae59f5d4 | delta |
|---|---|---|---|
| `--list-axes` MAIN | 164 rows / 49 axes | **171 / 50** | NEW axis `rev-end-form` (orders 1-5 denied / one-seed / tagged / two-seed / overflow; deny `PCREC_NO_REV_END_ONEWALK` bit 56 `-fno-rev-end-onewalk`); `fallback` +`drop-compound` (6), +`drop-end-mark` (7), later orders 6-11 -> 8-13; `req-admit` rows 3/4 reworded and `set-leads` **loses its deny flag** (`-fno-req-set-lead` bit 45 retired into the kit's `--memfn=no-pres-set-lead`; the old spelling is still accepted rc 0 and the b124 identity arm still passes) |
| `--list-axes` `#section memfn` | 6 | **12** | +`fd-r8`, `fd-ndisp`, `fd-d1`, `fd-pres-g1`, `fd-pres-pick`, `pres-set-lead` (read by nothing) |
| `--list-axes` NEW sections | -- | `part-layout` (valued controls, 3 + 5 + 3 + 3 rows), `part-layout-table` (T/P/W decision tables) | read by nothing; every reader selects MAIN |
| `--list-limits` | 73 | **78** | +`PCREC_COMPILE_STACK_BUDGET` 442368 [DD-10], +`PCREC_MAX_TEMPLATE_GROUP` 65535 and +`PCREC_MAX_TEMPLATE_NESTING` 10 [M4-SUBST], +`PCREC_MARK_PRIO_MAX_STATES` 32000 (D164 B3), +`PCREC_SPAN_WALK_SUBSETS` 512 [KIT-VERIFY]; `PCREC_MAX_GROUP_DEPTH`'s description and `PCREC_OFSK_MAX_SET`'s reworded, no value moved |
| `--list-schema` | 79 | **81** | +`config measures` (abi 82), +`block mg` ([M4-SUBST]'s case-map block) |
| `--list-definitions` | 75 | 75 | **byte-identical** (the seventh pin running) |
| `--list-syntax` / `--list-families` | -- (not archived here) | -- | `(*UTF)a`/`(*UTF8)a` `built`: unbuilt -> built; two `^`/`$` descriptions reworded; 0 rows added/removed. The bench/syntax SEED (9a1583ba) is 4 rows short of the live registry (`(*UCP)a`, `(*UTF)a`, `(*UTF8)a`, `${name}`) -- true at 6b2dbd3e too, owed to a re-seed lane |
| `--list-verbs` / `--list-source` | -- | -- | byte-identical |

`check_list_axes/definitions/limits_registry` green. The `schema` archive has no check function; it was diffed by hand.

## 5. Census (docs/dev/measurements/2026-10-25-b142prep-census.txt; `probe_b142prep_emit.py` + `probe_b142prep_census.py`)

Compile-only, 1,468 rows = 367 patterns of 10 sets x {plain, whole} x {auto-caps, auto-nocaps} (`-e utf8` on utf8), each emitted at
6b2dbd3e and 9ae59f5d4, plus `-fno-rev-end-onewalk` at 9ae59f5d4. **Does v2 need a change? Yes**: v2 reads **0 of 1,375**
compiled-both rows identical (the iterator scaffold + the forwarder/twin split are in every artifact). v3 (`normalize_v3`, a
CENSUS-side normalization; the record field stays v2 -- see OWED) strips the scaffold, folds the twins back, places the VM `_run`
prologue after the twin's initializer-free locals and sorts the top-level items:

| form | identical | changed | refused-both | refusal movers |
|---|---|---|---|---|
| plain (734) | 662 | **25** | 47 | 0 |
| whole (734) | 677 | **11** | 46 | 0 |

**Every one of the 36 changed rows is attributed** (the `attribution` column; `UNATTRIBUTED` = 0): 18 abi-78 rev-end mark
(arm == old program on 18/18), 4 abi-77 compound, 2 abi-83 K128, **12 [FLAG-SPELL] (no abi)**. The anchor fold (81), part layout
(80), the knowledge union (79), measures (82) and the iterator (84) move NO program on the bench; stamps that moved with no program
move (invisible to v2/v3 by construction): `RX_ENGINE_WHY` text 12 rows, `RX_REQ_RUN` 8 rows, `RX_VM_PREFILTER_LANG_WHY` 2 rows (the
size-cap-retry prose echoes the artifact size), `RX_DFA_SCAN_EDGE` 2 rows. A second population at 8 MiB caps
(`2026-10-25-b142prep-bigcap.txt`, altwide + bounded x {auto, vm} x {plain, whole}, 328 rows): 326 compile at both pins, 2 refuse at
both, **0 refusal movers**. v3's own validation: a 400-row random sample read 386 identical before the VM-local-ordering fix and
the census reads 1,339 identical after it; `check_b142_stamps` asserts abc is v2-CHANGED and v3-IDENTICAL.

## 6. Size books (pcrec's OWN bytes; measured, never assumed)

- **+106 B flat** (emit and code alike) on 1,257 of the 1,339 v3-identical rows: the `RX_COMPOUND`, `RX_MEASURES` stamp lines and
  the `.measures`/`.next`/`.next_n` initializer lines (ITER_RETRY's stamp line is scaffold). +104/+114/+115/+116 on 14 rows (stamp value
  lengths). abi 84 `_next` etc. add NOTHING to the count: the scaffold is excluded.
- **The DFA retry machine is counted and copies the tables** (68 rows, all DFA, ITER_RETRY `retry`): +3,064..+4,128 B on narrow DFAs;
  on the bounded `cls-upto-N` WHOLE-subject ladder +31,585 (512), +60,257 (1024), +117,601 (2048), +237,081 B (4096) (emit only: code
  +2.0 KB); the same +60,257 on grp-upto-1024 whole and capability letters-bounded-tail-z (plain and whole); on the DENIED (uncollapsed)
  16384 rung 255,041 -> 612,992 B. VM `retry-budgeted` adds nothing (the guarded matcher copy is scaffold). Nothing crossed a default
  cap (0 refusal movers); the cap's headroom for a table-heavy DFA is now up to ~2.4x smaller.
- **abi 78 shrinks** the 9 tail patterns 1.0-3.4 KB; **K128** +333 B; **[FLAG-SPELL]** -50 B; **compound** +113,575 B on the one corpus pattern.
- **emit_bytes records are NOT comparable across 6b2dbd3e -> 9ae59f5d4 without this book**: both the +106 and the definition change
  (scaffold excluded) sit inside every compile row's `emit_bytes`/`emit_code_bytes`. The reporter's cross-pin size Delta needs a
  covariate note (OWED).
- **Compiled objects**: every `.o` gains the iterator's code: `.text` +0.8-1.3 KB (cls-upto-4 552 -> 1,848 B; dig-upto-16 auto
  952 -> 1,704; dig-upto-16 forced-VM 744 -> 1,768). This is a LAYOUT covariate of the [B22] `year4` kind for every cell, including
  the 1,339 program-identical ones (which form the null band).

## 7. Validation

- Targeted groups (run through a scratch runner): `check_b142_stamps` 27/0, `check_deny_flag_controls` 31/0, `check_b135_two_pin_window`
  7/0, `check_mechanism_stamps` 141/0, `check_b136_stamps` 30/0, `check_emit_size_port` 22/0, `check_b122_round1_stamps` 7/0,
  `check_b124_stamps` 12/0, `check_b126_stamps` 23/0, the three registry checks and `check_abi_floor_refusal` green. Reds found and
  repaired on the way (every one attributed above): the scan-edge reader (`rx__retry`, `rx__find`, `__attribute__`), the emit-size
  port (scaffold), the adapter's compound agreement rules, 36 size expectations (+106 flat, 5 residuals), 3 deny-control size pairs,
  16 `.text` identity arms, the I-43 ratio instrument, the folds-4 `.rodata` finding, the two-pin check.
- Sidecars: `scripts/regen_sidecars.py` 97 sidecars, 0 failures.
- **FULL `make check`**: see section 9.

## 8. WINDOW PLAN (a PROPOSAL; NOT RUN; the manager and Frank decide)

Preconditions: the quiet gate; `pin.sh --path` for 9ae59f5d4 and 6b2dbd3e; sentinel subjects; Frank's clearance via pcrecdev1. Entries are
`testee` (canonical 9ae59f5d4) or `testee@6b2dbd3e` (the BEFORE). Cell lengths are b136's MEASURED minutes (sentinel ~6.2, loglines
~8.4, email ~5.0, litrun ~12-14, altwide ~24, syntax ~44, utf8 -utf8 ~34-39, bounded ~50, capability ~47-49); nothing here has been
re-timed at this pin.

| tier | content | why | cells | est. |
|---|---|---|---|---|
| 1 | sentinel open; **capability x {pcrec-auto, pcrec-nocaps} x {9ae59f5d4, @6b2dbd3e}** (I-154: both were inconclusive-spread in b138); loglines x {auto, auto@6b2dbd3e}; sentinel end | I-154's re-run, plus the SAME-set BEFORE so the cross-pin Delta has a same-window partner, plus the program-identical null band (capability's 62 compiling patterns: 8 movers, 54 identical) | 1 + 4 + 2 + 1 | ~4.4 h |
| 2 | the abi-78 / [FLAG-SPELL] / K128 movers' sets at both pins: litrun x {auto, auto@6b2}, syntax x {auto, auto@6b2}, utf8 x {auto-utf8, @6b2}; bounded x {auto, auto@6b2} (the retry machine's table growth is in the whole forms: compile cost and load, NOT hot code) ; email x {auto, auto@6b2}; sentinel pair | tail-family timing (9 patterns), the 12 option-run VM programs (bracket-array-define, codegrammar-xflag, slack-webhook in capability; mod-j-uc in syntax), `anc-dollar`/`anc-z-uc` in syntax | 2 + 2 + 2 + 2 + 2 + 2 | ~6.5 h |
| 3 (optional, needs a decision) | the same-pin single-variable twin for abi 78: a pinned testee `pcrec-auto-norevendonewalk` (`flags = ["--features","all","-fno-rev-end-onewalk"]`; the DENY_FLAGS word already exists) x {capability, litrun, syntax} | 6b2dbd3e -> 9ae59f5d4 confounds abi 78 with 77, 79-84 for the 18 mover rows; the census shows the other seven steps move NO program on those rows (v3 identical outside the arm), so only the layout covariate remains -- the twin removes it. Not built: pcrec's I-159 names no acceptance review for B3 | 3 | ~2.5 h |

Not planned: the compound (no declared regime times a whole-subject form; a `match`-regime witness would be a new set), `RX_PART_LAYOUT`
(needs a pinned control config), the subst bench (lane b140), pcre2/other-engine reference rows (the latest windows' rows stand).
What each tier answers: tier 1 = I-154 and the Delta partner; tier 2 = the program movers + the size-book/compile-cost question;
tier 3 = the abi-78 single-variable read. A mid-night decision for the manager: if tier 1's capability pair is `inconclusive-spread` again,
the cause is not a pcrec change (the capability pair's programs are 54/62 identical), so the next step is the spread rule, not a re-pin.

## 9. MAKE CHECK (the manager's brief asked for it; launched from this lane because further independent work remained)

Command (from `worktrees/b142prep`): `(setsid gnutimeout 14400 make -k check > /var/tmp/pcrecbench/b142prep/final_check.log 2>&1; echo "DONE rc=$?" >> /var/tmp/pcrecbench/b142prep/final_check.log) & disown`.
Marker: the last line `DONE rc=<n>`. RESULT: **rc=2, two reds, neither caused by the re-pin.**
check-schema 9 accepted / 89 rejected / 0 WRONG; check-harness 897 passed, 1 FAILED
(`a real quick cell on bench/email writes a MEASURED scratch record`: status=inconclusive-load,
a box-load flake, another lane was running); check-report 96 passed, 8 FAILED
(test_plain_entry_capacities_r1, _tiny_set_per_subject_subtable_r2, _buffer_frame_legend_r4,
_jitter_ratio_r5, _artifact_bytes_column_r7, _legend_and_superseded_shortening_r8,
_engine_reading_and_scoped_legend_b16_r3, _kb16_query_never_opens_other_subbench_files):
the SAME 8 fail on master's tree (58f6af36), cause: the store now holds two machines
(budu-ryzen1600, ryzen7700x) and the reporter refuses a pooled selection (O-90, [B137]) --
the tests need `--machine`; OWED to the reporter owner; check-interpret 271 passed / 0 FAILED;
check-upstream OK; check-trend 33 / 0 failed

## 10. Findings pcrec did not state (candidate outbox items)

1. **[FLAG-SPELL] moves 12 bench rows with no abi bump** (section 1): a program change (dead label) and a stamp-only change
   (`RX_REQ_RUN` grows to `Cat/dfffff` on syntax mod-reset/mod-unset) with the abi unchanged -- a reader trusting "abi 84 = no
   other program moves" would misattribute it. Ask: list it in the abi change log or bump.
2. **The DFA retry machine copies the tables and counts toward both emit caps**: +31 KB .. +237 KB on the bounded whole-subject ladder,
   2.4x on an uncollapsed 16384 DFA. pcrec's abi-83 text says "the retry machine is a machine and counts" but not that it scales with the
   machine; today it shifts no bench refusal (0 movers at default and 8 MiB caps), but it narrows the cap headroom of every table-heavy DFA.
3. **The scaffold has no marker in the emitted text**, so a consumer cannot reproduce pcrec's size definition from the files; the bench
   now needs `--warn-emit-bytes=1` on every compile. Ask: a stable machine-readable size line (or `--emit-facts` row) for the two numbers.
4. **`-fno-req-set-lead` is gone from the registry but still accepted** (rc 0, behaviour preserved): intentional alias?
5. **`RX_ENGINE_WHY` names a different forcing construct** on 12 nocaps rows (`\1` -> `\3`/`\2`/`(?!...)`; `(?>...)` offset 14 -> 0)
   with the route unchanged: the "first forcing construct" is not stable across the pin.
6. Compound artifacts add `RX__F_*` / `RX__Q_*` stamp families and read -1 for two integer stamps: documented only in the design note,
   not in match_api.md 6.3's closed-set tables.
7. bench/syntax's seed is 4 registry rows stale (ours, not pcrec's).

## 11. Charter-vs-committed checklist

| brief item | status |
|---|---|
| read BOILERPLATE; worktree `lane/b142prep` from fca3bd9a; WIP commits; no merge/push | done (`git log lane/b142prep`) |
| `pin.sh 9ae59f5d4` build; configs pin + also_pins; 6b2dbd3e kept; 00c97769 / b8337c33 decided by measurement | done (section 2); builds under `build/` |
| adapter / shim reading the new stamps | adapter.py (text-read); shim UNTOUCHED by decision (section 3) |
| `testees/pcrec/CLAUDE.md` "Re-pin at 9ae59f5d4" | done |
| all registry surfaces re-archived and diffed, every delta explained | `testees/pcrec/list_{axes,definitions,limits,schema}.tsv`; section 4; the four other `--list-*` surfaces diffed, not archived |
| census: identical / changed / refused-both / refusal movers, every change attributed; archive with source header | `2026-10-25-b142prep-census.txt` (+ `-bigcap.txt`); section 5 |
| program_identity: does v2 need a change | yes -> v3 (`normalize_v3`); record field stays v2 (OWED ruling) |
| claim-vs-measured table for the eight steps | section 1 |
| mechanism stamps BY VALUE on witnesses; new deny flags -> DENY_FLAGS + DENY_CONTROLS; new pinned testee only if an acceptance twin | `check_b142_stamps`; `-fno-rev-end-onewalk` in both tables; NO new testee, said why (section 8 tier 3) |
| shim floor decision with the abi-sabotage arms green | section 3 |
| size books re-derived, flat terms measured, per-witness residuals | section 6; `B142_FLAT`, `B142_RESID` |
| [M4-SUBST] not an abi event, verified on our census | section 1; `probe_b142prep_subst_noevent.py` (0 of 1,375 differ) |
| catalogue `[[pin_order]]` + minor bump + sidecar regen | 3.20; 97 sidecars, 0 failures |
| `make check` in full, counts per target | section 9 |
| root CLAUDE.md STATUS / testees line | done |
| window plan, a proposal, not run | section 8 |
| OWED | (1) the reporter legend for `compound` + the version bump with the first report that carries one; (2) a BD13 ruling on `program_sha256` v2 -> v3 (cross-pin null bands for this pair read the census until then) and a `--normalization v3` CLI choice; (3) the `emit_bytes` cross-pin covariate note in the reporter; (4) `FRONT_PIN` after the first window; (5) bench/syntax re-seed; (6) the twin testee decision (tier 3); (7) a compound-bearing regime; (8) plan.md / journal STATE edits and the outbox items (manager); (9) the intermediate abi 77-83 pins were never built -- a per-step attribution of a timing mover that the census cannot separate (only the abi-78 arm and the 36 attributed rows can) would need them |
