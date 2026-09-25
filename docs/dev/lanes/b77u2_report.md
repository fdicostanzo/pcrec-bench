# Lane b77u2 — [B77] U2, the ROSTER half of the utf8 set

Branch `lane/b77u2` (worktree `.claude/worktrees/agent-a6a0853b6ec078318`,
off master eafb654). Charter: `docs/design/utf8_set_v1.md` v0.2 §7 (all),
§13's U2 row, §15 R2; plan row [B77]; U1/U3 reports as context. Not
touched: `store/`, `reports/`, inbox/outbox, `plan.md`, `bench/utf8/`
(U3/U4's), ~/pcrec (read-only; only the pinned binary was executed). No
pinned window run.

## Charter vs committed

| # | U2 promise (§7 / §13 U2 / brief) | status | where |
|---|---|---|---|
| 1 | the new per-engine UTF configs per §7.1 | **DONE** — ten configs: `pcre2-utf-interp`/`-jit`/`-dfa` (PCRE2_UTF via U1's `--utf`; never `--ucp`, class scope is the pattern's own `(*UCP)`), `pcrec-{auto,nocaps,vm,vm-in}-utf8` (`-e utf8` in `flags`), `re2-utf8` (EncodingUTF8, new driver `--encoding utf8`), `onig-utf8` (ONIG_ENCODING_UTF8 now a RUNTIME choice, driver `--encoding utf8\|ascii`), `vectorscan-block-nosom-utf8` (HS_FLAG_UTF8, never HS_FLAG_UCP, driver `--encoding utf8`). `rust-default` unchanged (already UTF-8-semantic), `tre-default` unchanged (per-pattern exclusion, §7.3). Every utf8 config derives its byte sibling's id plus `_utf8` (listed below). The engine encoding rides the MEASURE argv too for the recompiling drivers (pcre2/re2/onig/vectorscan) | 59afd08 (`testees/*/configs.toml`, `adapter.py`, `driver.*`; `pcrecbench/adapters.py` `CONFIG_ENCODINGS` + `config_encoding()`) |
| 1b | a WITNESS COMPILE per (config, REQUIRES token) before a declaration ships, archived with pattern, command, verbatim result, source header | **DONE** — 22 configs (10 new + rust + tre + 10 byte controls) × the three new tokens; the 12 roster configs × `unicode-properties` + 9 script spellings; the 10 new × the 14 compile-witness tokens + 3 execution-model tokens; plus the set's own spellings (informational). Every expectation DERIVED from the libpcre2 oracle under the utf8 word, never hand-typed. Ends in a per-config DECLARATIONS block for U4 | `docs/dev/measurements/probe_b77u2_utf8_witness_census.py` (33c93b6), `docs/dev/measurements/2026-09-25-b77u2-utf8-witness-census.txt` (3899e3c) |
| 2 | §7.4's UNCONFIRMED rows settled by measurement (Script/Script_Extensions across re2, rust, onig at minimum), updated in place CONFIRMED/REFUTED, pointing at the archive | **DONE** — (f) row: RE2 CONFIRMED (bare names only, every prefixed spelling refused), rust 1.13.1 CONFIRMED (all four prefixed spellings compile and read correctly), onig-utf8 CONFIRMED as a re-census (`unicode-properties` flips to SATISFIED; prefixed spellings refused); vectorscan as RE2; one premise REFUTED (bare `\p{Greek}` = Script_Extensions only on PCRE2/pcrec; Script on RE2/onig/Vectorscan/rust — an answer divergence on U+0342). (a) row: pcrec + rust CONFIRMED by witness, three unpredicted rows added (onig-utf8 out of BOTH scope families, re2-utf8 out of unicode-class-scope, vectorscan-utf8 NOT out of it). (e) row re-witnessed on the set's own four lookbehinds. A new note: every `\b`/`\B` member is class-scope-dependent. §7.6 corrected in part (below). §13 U2 row brought to reality | `docs/design/utf8_set_v1.md` (3899e3c) |
| 3 | pcrec adapter: `effective_encoding(flags)` + `encoding_extra` as the FIFTH `compose_config_extra()` part, encoding lands in testee_id | **DONE** — recognises `-e X`, `--encoding=X`, `--encoding X` off the EFFECTIVE flags (so `$PCREC_LOCAL_FLAGS="-e utf8"` reaches `pcrec-local`'s id); `byte` = no token; unknown value / disagreeing spellings / trailing `-e` refused BY NAME; token `utf8` LAST in chartering order | `testees/pcrec/adapter.py` (59afd08) |
| 3b | frozen-renderer rows proving the six pre-existing pcrec families derive UNCHANGED testee_id AND config_extra (F-C1 MUST), in the [B24]/[B31] pattern | **DONE** — `check_encoding_axis` (7 checks): (1a) a FROZEN table of ALL 25 pre-existing configs of every engine (id shape after `<engine>_<version>_` + `config_extra`; the six pcrec families, the `-in` pair and `pcrec-local` included); (1b) a FROZEN COPY of the pre-U2 four-part composition checked against every pcrec config's live `config_extra`; (1c) every COMMITTED record a pre-existing config derives re-derived byte-identically (build_flags, runtime_options, config_extra; non-vacuous: libpcre2 3, oniguruma 1, pcrec 14, re2 2, rust 1, tre 1, vectorscan 1); (2) the ten new configs' shape + schema validity; (3) the recognition rules; (4) THE CONTROL `^.$` over `é` per engine family (utf8 config `match [0,2)`, byte sibling `nomatch`, both as the respective oracle); (5) the CLI lists them. 7/7 PASS standalone | `tools/selfcheck.py` (324a357), wired into `main()` after `check_cflags_axis` |
| 4 | CLAUDE.md files, APPROACH.md's roster, §13 U2 row | **DONE** — `testees/CLAUDE.md` (table + the encoding rule; a stale duplicate `pcre2/` row removed), each engine's CLAUDE.md gains its UTF-8 section with its witnessed declaration, root `CLAUDE.md` (roster + the check-harness clause), `APPROACH.md` §5 (encoding is part of a testee's identity), `docs/dev/measurements/CLAUDE.md` | 3899e3c, 5d5abba |
| 5 | validation: check-schema, fixtures gen --check, check-interpret, targeted harness checks | **DONE** (numbers below); the full `make check` is **OWED — manager-launched** (command below) | — |
| 6 | this report | DONE | `docs/dev/lanes/b77u2_report.md` |

## The derived testee ids (pin 6ef76820)

    pcre2-utf-interp  libpcre2_10.46_interp-caps-simdna_utf8
    pcre2-utf-jit     libpcre2_10.46_jit-caps-simdna_utf8
    pcre2-utf-dfa     libpcre2_10.46_dfa-nocaps-simdna_utf8
    pcrec-auto-utf8   pcrec_6ef76820_auto-caps-simdna_utf8
    pcrec-nocaps-utf8 pcrec_6ef76820_auto-nocaps-simdna_utf8
    pcrec-vm-utf8     pcrec_6ef76820_vm-caps-simdna_utf8
    pcrec-vm-in-utf8  pcrec_6ef76820_vm-in-caps-simdna_utf8
    re2-utf8          re2_11.0.0_default-caps-simdna_utf8
    onig-utf8         oniguruma_6.9.10_default-caps-simdna_utf8
    vectorscan-block-nosom-utf8  vectorscan_5.4.11_block-nosom-nocaps-simd_utf8

Twenty pinned pcrec configs now (was sixteen) + `pcrec-local`.

## The declarations (what U4 transcribes into bench/utf8's `ext bench`)

From the census's DECLARATIONS block (per-token evidence is there):

| config | declares | the three new tokens (utf8-enc / ascii-scope / unicode-scope) |
|---|---|---|
| pcre2-utf-interp, -jit | 19/20 | S / S / S |
| pcre2-utf-dfa | 14/20 | S / S / S |
| pcrec-auto-utf8, -vm-utf8, -vm-in-utf8 | 14/20 | S / S / – |
| pcrec-nocaps-utf8 | 13/20 | S / S / – |
| re2-utf8 | 7/20 | S / S / – |
| onig-utf8 | 14/20 | S / – / – |
| vectorscan-block-nosom-utf8 | 7/20 | S / S / **S** |
| rust-default | 8/20 | S / – / – |
| tre-default | 6/20 | – / S / – |

Two stated verdict rules (in the probe and archive): a pcrec SIZE refusal
does not unset a token (pcrec-vm-utf8's `\p{L}`/`\P{L}+` — R4/P7 must
surface as first-class `did-not-compile` rows); `non-utf8-subject` is NOT
on any UTF-8 config, by rule (PCRE2 gives up `-23` on invalid input;
HS_FLAG_UTF8 / ONIG_ENCODING_UTF8 document it as undefined; the set runs
none), whatever one witness answered.

## Findings (for the manager, U4, U5)

1. **§7.6 (1) corrected in part — vectorscan-utf8 is DECLARED
   `unicode-class-scope` SATISFIED.** The set spells UCP inline as
   `(*UCP)`, and Vectorscan honours that verb PER PATTERN under
   HS_FLAG_UTF8 alone: `(*UCP)\w+`/`\d{4}`/`a\sb` all answer the oracle.
   The `\b` half of 7.6 holds per pattern: `(*UCP)\bМосква\b` REFUSES,
   so `asr-b-cyr-ucp` will be an honest `did-not-compile` row there. The
   charter's text predicted the opposite declaration; I followed the
   witness (the L5 rule). **A ruling point** if the manager prefers
   §7.6's declaration: flip the one token and `cls-*-ucp` /
   `ci-ucp-invariance` become `unsupported-by-declaration` on that config.
2. **onig-utf8 sits out BOTH class-scope families** (not predicted):
   Unicode `\w`/`\d`/`\s`/`[[:alpha:]]` by default under UTF-8 + PERL_NG,
   and `(*UCP)` is parsed as a callout and refused (`-229`). An
   `ONIG_OPTION_ASCII_RANGE` sibling would restore `ascii-class-scope` —
   named, not built.
3. **Bare `\p{Greek}` is an ANSWER divergence**, not a capability one:
   Script_Extensions on PCRE2/pcrec (`match` on U+0342), Script on
   RE2/onig/Vectorscan/rust (`nomatch`). `prp-greek` will read as a wrong
   answer on those four on any U+0342 subject; no REQUIRES token can
   express it — U5 should PREDICT it. `prp-greek-sc` (`\p{sc=Greek}`) is
   `did-not-compile` on RE2/onig/Vectorscan, compiles on rust/pcrec/PCRE2.
4. **Every `\b`/`\B` member is class-scope-dependent**: `\B` over `é`
   answers `match [0,0)` (oracle, ASCII `\w`) vs `nomatch` on onig-utf8
   and rust (Unicode `\w`). `asr-B-midchar` (and `asr-b-ascii` whenever a
   subject puts a non-ASCII letter against the literal) need
   `requires-ascii-class-scope` or a stated prediction — U4's call.
   §7.3's "byte-safe for TRE" stays true.
5. **R4/P7 confirmed at witness level**: `pcrec-vm-utf8`/`-vm-in-utf8`
   REFUSE `\p{L}` (563,569 B) and `\P{L}+` (1,117,090 B) at the 500,000 B
   emitted-code cap; `auto`/`nocaps` compile them as DFAs. **Compile cost
   the first window pays**: `-e utf8` `\P{L}+` takes 41.1 s to emit under
   `auto`/`nocaps` (487,011 B), its `(?:…)\z` form 62.0 s (501,987 B) —
   one timed run each (not a measurement), ×2 forms × trials per cell.
   Worth sizing in U5's cell-time arithmetic (§10.3, R3).
6. **pcrec refuses `(*UCP)` as `(*...) requires module 'verbs'`** even
   under `--features all` (same as `(*FAIL)`) — consistent with UD §4.5's
   no-UCP-axis, but the diagnostic names a missing MODULE rather than an
   unsupported verb; a possible pcrec wording ask, not filed.
7. **TRE silently accepts `(*UCP)\w+`** (compiles, answers `nomatch`) — a
   new instance of `testees/tre/CLAUDE.md`'s `(*NAME)` silent-misparse
   hazard; harmless in the set (the token keeps TRE off those rows).
8. **Pre-existing, out of scope, not fixed**: `testees/vectorscan/
   adapter.py`'s `measure()` does not forward `--free-spacing`, while the
   driver rebuilds the whole-subject wrapper at measure time from `--form`
   + that flag — so a `(?x)` pattern ending on a line comment ([B70]'s
   class) would compile its whole-subject form correctly and then build a
   DIFFERENT (comment-swallowed) wrapper at measure time. Candidate KB for
   the manager; fixing it moves byte-set behaviour, so it is not in U2.

## Validation (run by this lane)

- `make check-schema`: 5 accepted, 73 sabotages rejected for the intended
  rule, 0 wrong.
- `python3 catalogue/fixtures/gen.py --check`: 243 files in 75 fixtures, ok.
- `make check-interpret`: 199 passed, 0 FAILED.
- `check_encoding_axis` standalone: **7/7 PASS**.
- Targeted harness sections (every section touching the adapters,
  drivers and composition this lane changed), **134 passed / 0 FAILED
  over 15 sections**: `check_encoding_axis` 7, `check_describe_schema_shape`
  3 (the KB-21 class), `check_kb1_runtime_options` 1,
  `check_driver_smokes` 7, `check_utf8_find_all_advance` 24 (U1's arm,
  over the rebuilt re2/onig/vectorscan drivers), `check_high_byte_pattern_argv`
  9, `check_capability_policy` 7, `check_capability_policy_noop_elsewhere`
  5, `check_boolean_grain_scoring` 5, `check_cap_axis` 13 (log
  `/var/tmp/b77u2/targeted.log`); `check_pcre2_dfa` 12, `check_pcrec_local`
  6, `check_cc_axis` 18, `check_noedge_axis` 10, `check_cflags_axis` 7 (log
  `/var/tmp/b77u2/targeted2.log` -- a first pass of these five failed 8
  rows only because the worktree had no GENERATED email/loglines subject
  trees; `make check` generates them first, so the re-run after
  `bench/{email,loglines}/gen_*subjects.py` is the valid reading).
- **Full `make check`: OWED, manager-launched** (it is ~30 min; the lane
  does not launch it per the 2026-09-25 rule):

      cd <the merged tree or this worktree> && \
      mkdir -p /var/tmp/b77u2-makecheck && \
      (gnutimeout 5400 make check > /var/tmp/b77u2-makecheck/make_check.log 2>&1; \
       echo "DONE rc=$?" >> /var/tmp/b77u2-makecheck/make_check.log)

  Completion line: `DONE rc=<n>` at the log's end. Expected
  check-harness count: U1's 482 + this lane's 7 = **489**.
