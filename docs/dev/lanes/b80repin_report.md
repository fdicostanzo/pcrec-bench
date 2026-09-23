# lane b80repin report — RE-PIN to b1885a83 (abi 29 -> 30), [OPTLOOP] cycle 2 batch 2

**Task**: plan row [B80] (a) / inbox I-95. Re-pin the pcrec testees from
`8d716693` (abi 29) to pcrec main `b1885a83` (abi 30) — the [OPTLOOP]
cycle 2 batch 2 pin ([OPT-FREQPICK] + [OPT-REQPOS] tier 2b: a new
`RX_REQ_RUN` stamp + `-fno-req-run` deny axis, bit 31). The capability
re-measurement window is explicitly the MANAGER's job (I-95 (a)), out of
scope here.

**Branch**: `lane/b80repin`, `worktrees/b80repin`, three commits so far
(`2f71611` the adapter/shim/driver/registry/catalogue/selfcheck change,
`de00f33` the CLAUDE.md updates, this report next). **DELIVERED**: the
targeted checks (`check_mechanism_stamps` 114/114, `check_deny_flag_
controls` 15/15, all four registry checks, `check_abi_floor_refusal`
9/9, `check_emit_size_port`/`check_noedge_axis`/`check_cflags_axis`/
`check_cap_axis` all green except two pre-existing environment-setup
failures unrelated to this change, fixed by generating the gitignored
subject trees) run standalone before the full `make check`; the full
run is OWED below.

## Charter-vs-committed checklist

1. **Fetch + confirm the commit.** DONE. `git -C ~/pcrec fetch origin`
   confirmed `b1885a83` on `origin/main` with `8e4e9c6c` (the [OPTLOOP]
   batch-2 merge I-95 names) as its ancestor, and `8d716693` (the
   previous pin) also an ancestor (57 commits between them). Everything
   on `origin/main` AFTER `b1885a83` (six commits to `46a54fd0`) is
   `docs/dev/` only — `git diff --stat b1885a83 origin/main` touches no
   `src/`/`lib/`/`tests/` file — confirming I-95's own characterisation
   ("docs/tests-only commits may follow — your §0.1 check is over
   src/lib/cli"). No write to `~/pcrec` beyond the sanctioned `git
   fetch`.

2. **`pin.sh b1885a83`.** DONE. `build/pcrec-b1885a83/build/pcrec`,
   `rx_info.abi` 30 confirmed on a plain `abc` witness.

3. **`rx_info` / the shim floor.** `struct rx_info` diffed field for
   field between the two pins' emitted `.h` (the `abc` witness) — ZERO
   hunks in the struct body. `PB_SHIM_MIN_ABI` unchanged source, `16`.
   Neither [OPT-FREQPICK] (a byte-encoding-only selection change) nor
   [OPT-REQPOS] tier 2b's new `RX_REQ_RUN` macro touches a struct
   member (confirmed: `pb_req_run()` reads the macro via `#ifdef`, the
   same shape as `pb_req_byte()`/`pb_end_window()`), so the
   floor-raising rule (a FIELD addition, never a macro) does not apply.
   **Verdict: floor stays 16, no rx_info change.**

4. **Registries re-archived and diffed against the pin's own live
   output.** DONE, commit `2f71611`.
   - `list_axes.tsv`: **87/31 → 89/32.** TWO rows, ONE new axis exactly
     as I-95 described: `req-run` (order 1 `run` — stamp `RX_REQ_RUN`,
     deny `PCREC_NO_REQ_RUN` bit 31, cli `-fno-req-run`; order 2 `none`
     fallback). Every other row byte-identical.
   - `list_definitions.tsv`: 50 rows, **byte-identical** — the twelfth
     pin running.
   - `list_limits.tsv`: **58 → 60 rows.** Two added, both
     [OPT-REQPOS] tier 2b's: `PCREC_MAX_REQ_RUN_EMIT` (8 bytes,
     "selection knee" — the longest run the emitted memcmp compares,
     sized where gcc lowers a constant-length memcmp to one word load)
     and `PCREC_MAX_REQ_RUN_SCAN` (32 bytes, "compile budget" — the
     analysis's own truncation budget, 4× the emit cap). No existing
     row reworded.
   - `list_schema.tsv`: 71 rows, **byte-identical** — neither
     optimization touches the `.rxt` grammar.

   **Everything accounted for by name; nothing unexplained.**

5. **The adapter/shim/driver: the `req_run` stamp reader.** DONE.
   `testees/pcrec/shim.c`: `pb_req_run()`, the same `#ifdef MACRO /
   return MACRO; #else / return NULL` shape as `pb_req_byte()` /
   `pb_end_window()`, placed right after `pb_vm_start()`.
   `testees/pcrec/driver.c`: one declaration, one `SYM()` registration,
   one `info req_run` print beside `req_byte`/`end_window` in the
   SAME "every"-scope block (MEASURED, not assumed: `RX_REQ_RUN` is
   emitted unconditionally at both call sites `pcrec_emit_req_byte_
   check`'s scan reads from, i.e. both search entries — same scope as
   its siblings). `testees/pcrec/adapter.py`: `req_run` added to
   `STR_PAIRS`, `STAMP_SCOPE` (`("every", 30)`), `METADATA_DECL` (full
   description citing the shim accessor and scope). **No
   `REGISTRY_STAMP_PAIRS` entry** — like `req_byte`/`end_window`, its
   registry row carries a VARIABLE value (hex bytes + `@` + index), not
   an enumerable candidate set, the same shape as
   `dfa_prefilter_offsets`.
   `testees/pcrec/configs.toml`: `pin = "b1885a83"`. No new testee: no
   `-noreqrun` deny axis was requested (unlike `-noedge`/`-noisland`/
   `-noclsfold`, which each back an acceptance-review BEFORE; nothing
   in [OPT-REQPOS] is under acceptance review the way [OPT-5]/
   [ENG-ISL]/[FORM-CHAR] were).

6. **Stamp spot-checks BY VALUE, and the deny controls.** DONE,
   `check_mechanism_stamps` 114/114 and `check_deny_flag_controls`
   15/15, both run standalone before the full suite. Full detail in
   `testees/pcrec/CLAUDE.md`'s new dated section; the headline finding:

   **[OPT-FREQPICK] moves `req_byte`'s VALUE on any pattern with a
   2+-byte necessary run — not a corpus-only effect.** Five of this
   project's OWN pre-existing `STAMP_CASES` witnesses moved:

   | witness | pin 8d716693 | pin b1885a83 |
   |---|---|---|
   | `foo[0-9]+bar` / `^foo[0-9]+bar` | `req_byte "114"` ('r') | `req_byte "98"` ('b'), `req_run "626172@0"` ("bar"@0) |
   | `^foo` / `\Gfoo` / `foo\z` | `req_byte "111"` ('o') | `req_byte "102"` ('f'), `req_run "666f6f@0"` ("foo"@0) |
   | `a(b\|c)+d` (both forms) | `req_byte "100"` ('d') | UNCHANGED — 'a'/'d' are single bytes, no 2+-byte run |

   Each of these five needed its `emit_bytes` expectation moved too
   (none had one to begin with — they're pure stamp-value assertions).
   One `LEDGER_STAMP_CASES` witness DID carry a byte-precise size
   assertion and moved: `altwide pfx3-256` under `--engine=vm` (the
   [ENG-ISL] island witness, `req_byte "120"` → `"113"`, run `"qux"@0`)
   — MEASURED `+423 B` over the pre-[B80] total via a direct `pcrec-
   local` compile against both pins (232115 → 232538 B), NOT the flat
   term (the stamp string itself is longer than `"none"`, and the
   emitted guard is the run's memchr+memcmp loop replacing the
   single-byte `if`). `vm_program_bytes` UNCHANGED (244735 both pins),
   confirming the guard lives in the shared search prologue, not the
   VM program region.

   **Every OTHER size-book assertion in the file (24 formula sites)
   moves by exactly `B80_STAMP_LINE = 26`** (`#define RX_REQ_RUN
   "none"`, flat, both engines) — added ALONGSIDE the existing
   `B74_STAMP_LINES_DFA`/`_VM` terms (additive per re-pin, never
   replaced), confirmed by a direct `pcrec-local` compile of a
   non-firing witness at both pins (7351 → 7377 B DFA-route,
   22750 → 22776 B VM-route — both +26, `.h` unmoved).

   **Two `DENY_CONTROLS` rows updated/added:**
   - `req_byte: -fno-req-byte denies the required-byte memchr (and the
     run with it)` — default arm updated 114 → 98 (matching the corpus
     move), and `req_run` added to the same row: MEASURED both go to
     `"none"` together under `-fno-req-byte` (pcrec's own doc comment:
     "there is no run check without a byte").
   - `req_run: -fno-req-run denies the necessary-run memcmp, keeping
     req_byte` — a NEW row, the fourth new deny flag, isolating the run
     alone: MEASURED `req_run` moves to `"none"` while `req_byte` stays
     at `"98"` — the plain byte check still fires independently on the
     run's own scan member (the walk's own argmin pick, confirmed NOT
     merely "whatever the run left over").

7. **The corpus census, and I-95's three named expectations.** DONE,
   over `bench/capability`'s full 64-pattern set via `pcrec-local`
   against the pin's own binary (compile-only, both regimes share one
   compile row so a single pass covers both).

   **Census (I-95 (a)'s ask): 14 of 62 compiled patterns stamp a run**
   (2 refuse for unrelated reasons: `negation-scope-lookbehind-var`,
   `wild-datetime-datefinder-alternation`). Length distribution: 2
   bytes ×8, 3 bytes ×3, 4 bytes ×1, 5 bytes ×1, 8 bytes ×1 (the
   `wild-secrets-github-pat` witness, truncated from its 11-byte
   literal to the 8-byte `PCREC_MAX_REQ_RUN_EMIT` cap). Two identical
   pairs by construction: `tag-depth3-bound`/`tag-pair-match` both
   stamp `"</"@0`; `nested-comment-rec`/`wild-waf-crs-942500-comment-
   obfuscation` both stamp `"*/"@0`.

   Separately, **14 of 64 patterns move their `req_byte` VALUE**
   between the two pins. The union of "stamps a run" and "byte moved"
   is **18 patterns** — 4 stamp a run whose scan byte happens to equal
   the OLD rightmost pick (`req_byte` itself does not move:
   `keyword-prefix-order`, `wild-secrets-github-pat`, `wild-secrets-
   slack-webhook-url`, `winpath-near-miss`), 4 move `req_byte` under
   pure [OPT-FREQPICK] with NO run at all (`codegrammar-flat`,
   `codegrammar-xflag`, `dup-param-detect`, `wild-validator-email-
   owasp`), and 10 do both.

   **All three of I-95's named expectations checked by value, exact:**

   | pattern | expectation | measured |
   |---|---|---|
   | `wild-secrets-github-pat` (thr/srch) | `REQ_RUN "hub_pat_"` scan index 3 | `RX_REQ_RUN "6875625f7061745f@3"` (hex-decodes to "hub_pat_", index 3, scan byte 95 = `_`), `RX_REQ_BYTE "95"` — EXACT |
   | `logparse-atomic` (thr) | `REQ_BYTE 58 (':')` | `RX_REQ_BYTE "58"` — EXACT; ALSO stamps an unasked-for 2-byte run, `"3a20@0"` (": ") |
   | `router-prefix-order` (thr) | moved FROM 114; report new value | moved to **`RX_REQ_BYTE "47"`** (`/`), with a 5-byte run `"2f75736572@0"` ("/user"@0) |

8. **`catalogue/rules.toml`'s `[[pin_order]]`.** DONE, commit `2f71611`.
   `b1885a83` appended after `8d716693`. `catalogue_version` 3.3 →
   **3.4** (MINOR: a `[[pin_order]]` append only).

9. **`testees/pcrec/CLAUDE.md` / root `CLAUDE.md`.** DONE, commit
   `de00f33`. Both gain a dated section following the established
   per-re-pin narrative shape (the stamp, the five/one movers, the
   registry deltas, the corpus census).
   `docs/dev/plan.md`'s `[B80]` row and the STATUS narrative are the
   manager's, per the brief.

10. **Full `make check` — OWED.** Launched detached (`setsid`-style via
    `run_in_background`, `gnutimeout 2400`), log at
    `/tmp/claude-1001/.../scratchpad/b80/make_check.log` (session
    scratchpad, per the box rules). Gate of record going in (per
    `docs/dev/dev_journal.md`'s last entry before this lane, [B74]
    COMPLETE): `check-schema` 5/73/0, `check-harness` 456/0,
    `check-report` OK (84+7+8 = 99 pytest-style), `check-interpret`
    191/191. **NUMBERS OWED** — a follow-up (this session, once the
    background job's `DONE rc=` line lands, checked in the foreground
    per the boilerplate's fallback-probe rule) fills in the delivered
    counts here and confirms `make`'s own exit code, classifying any
    `check-interpret` section-3 sidecar-staleness failures the SAME way
    `b58repin`/`b74repin`'s reports did (a MINOR catalogue bump's
    sidecar regeneration is the MANAGER's merge-time step, not this
    lane's).

## Not done / OWED

- **OWED-1**: the full `make check` run's four counts and `make`'s own
  exit code (item 10 above). The targeted checks this lane's own
  changes touch are ALL GREEN, run standalone (item 6/7's numbers, plus
  all four registry checks and `check_abi_floor_refusal` 9/9) — the
  full run is confirmatory, not exploratory.
- **OWED-2** (same precedent as `b58repin`/`b74repin`'s OWED-2, same
  shape): sidecar regeneration for the catalogue 3.3 → 3.4 bump — a
  MINOR/additive `[[pin_order]]`-append bump, per the manager's
  standing instruction on this lane class this lane does NOT
  regenerate committed `reports/*.interpretation.md` sidecars — that
  runs at the manager's merge.
- No `store/` record needed re-deriving — this lane touches no
  `store/` record; the re-pin itself never runs a measurement window.
- `docs/dev/plan.md`'s `[B80]` row and the STATUS narrative are
  explicitly the manager's job per the brief; left untouched.
- **The capability re-measurement window** is explicitly the manager's
  own step per I-95 (a) and this lane's brief ("DO NOT run the
  capability window") and is NOT started here.

## For the manager, on review

- **The window's own asks (I-95 (a)) are pre-loaded**: the five/six
  TARGET patterns (`logparse-atomic` thr+srch, `router-prefix-order`
  thr, `wild-secrets-github-pat` thr, `tag-depth3-bound`/`tag-pair-
  match`, `nested-comment-rec` thr) and the CARVE-OUT set (every cell
  whose `REQ_RUN` stamps or whose `REQ_BYTE` moved) are now a concrete
  18-pattern list (item 7 above), not a prediction — the window can
  read its own carve-out population directly off this report rather
  than re-deriving it from the records after the fact.
- **A finding for the window's own read**: `logparse-atomic`'s run
  gain was documented (I-95) as 1.00× in the census while its pick
  moved from SPACE to COLON — worth checking directly against this
  lane's finding that the pattern ALSO now stamps a 2-byte run (": ")
  it did not carry before ([OPT-REQPOS] tier 2b, not merely
  [OPT-FREQPICK]'s pick move) — I-95's own text names this as "the
  no-decline-rule falsifier", and the window should read whether the
  RUN (not just the pick) changes that reading.
- **This lane's own re-pin ritual found no orthogonal break** the way
  `b74repin` found pcrec's D118 CLI reshape — `b1885a83`'s 57-commit
  range absorbed cleanly into the shape I-95 predicted, one new axis,
  one new stamp, no struct change, no CLI change, no co-landing
  registry-surface move. The only genuine surprise is the SCOPE of
  [OPT-FREQPICK]'s value move (five of this project's own hand-chosen
  witnesses, chosen for OTHER reasons, happened to carry a 2+-byte
  literal run) — worth a line back through the inbox ack: a re-pin
  that only touches "new stamp reads none on everything old" is the
  easy case, and this one was NOT that case for the pre-existing
  `req_byte` population, exactly as [B74]'s own precedent warned this
  cycle's REQBYTE-adjacent work would keep doing.
- **This lane is COMPLETE except OWED-1/OWED-2** (both explicitly
  scoped to the manager's own step, per precedent). No further work is
  planned unless review surfaces something new.
