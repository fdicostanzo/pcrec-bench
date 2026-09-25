# testees/onig/ — the Oniguruma adapter

Provides one testee: `onig-default`. `onig-lowretry` (a small
`onig_set_retry_limit_in_match`, exercising `ONIGERR_RETRY_LIMIT_IN_MATCH_
OVER` as a first-class `gave-up` — capability_set_v1.md §8's roster row)
is documented below as a LATER config; this lane does not wire it.

Built [B7]/L6b (`capability_set_v1.md` §11.1's per-engine lane row), lane
`l6bonig`, 2026-09-17. Oniguruma 6.9.10-1build1 (`libonig-dev`, this box's
apt candidate — `scripts/install_l6b_deps.sh` verified it installed
before this lane started); `/usr/include/oniguruma.h` is byte-identical
to the upstream `v6.9.10` git tag (diffed before any source was read).

| file | role |
|---|---|
| `adapter.py` | `describe`/`prepare`/`compile`/`measure`; the engine-metadata DECLARATION (`capturecount`, `names`, `refusal_class`); the `GAVE_UP_CODES` set |
| `driver.c` | the batched in-process timing driver (the protocol is in `pcrecbench/adapters.py`); direct-linked against `libonig.so.5` (`#include <oniguruma.h>`, `-lonig`) |
| `configs.toml` | the one config id, `onig-default` |
| `_probe.rx` | one byte, `a` — the version-probe pattern (`testees/pcre2/_probe.rx`'s own convention) |

## (a) The compile-cost definition

**One phase, `compile`** — `onig_new`, timed in-driver. Oniguruma has no
separate JIT step: an interpretive backtracking engine, the same
execution-model class as `pcre2-interp`. `warmup_trials = 0`.

## (b) `consumed_length`: the convention, stated plainly

**`consumed_length` is the subject length the driver passed and Oniguruma
accepted — i.e. the whole subject.** `onig_search`/`onig_match` take
explicit `str`/`end` pointers with no subject-size ceiling to truncate
against, and the API exposes no scan high-water mark — the SAME honest
claim `testees/pcre2/CLAUDE.md` states for pcre2: *"no byte was withheld
or refused"*, never *"the engine looked at every byte"*.

## (c) The config: syntax, and why

**`ONIG_SYNTAX_PERL_NG`** — the closest of this version's SEVEN shipped
syntaxes (`ASIS`, `PosixBasic`, `PosixExtended`, `Emacs`, `Grep`,
`GnuRegex`, `Java`, `Perl`, `Perl_NG`, `Ruby`, `Python`, `Oniguruma` — the
full list in `src/regsyntax.c`) to PCRE, chosen because this set's
expectations are pcre2-oracled and Perl_NG is the ONLY syntax carrying
ALL of: named groups (`ONIG_SYN_OP2_QMARK_LT_NAMED_GROUP`), `\K`
(`ESC_CAPITAL_K_KEEP`), possessive quantifiers/intervals
(`PLUS_POSSESSIVE_REPEAT`/`_INTERVAL`), if-else conditionals
(`QMARK_LPAREN_IF_ELSE`), `\g<n>`/`\g<name>` subexp calls
(`ESC_G_SUBEXP_CALL`), `(?1)`/`(?&name)`/`(?0)` Perl-style subexp-call
recursion (`QMARK_PERL_SUBEXP_CALL`) and `\p{...}` Unicode property
escapes (`ESC_P_BRACE_CHAR_PROPERTY`). **`ONIG_SYNTAX_PERL_NT` does not
exist in Oniguruma 6.9.10** — the brief's third option is not on this
version's menu; the choice is between `ONIG_SYNTAX_PERL_NG` (chosen) and
`ONIG_SYNTAX_ONIGURUMA` (the library's own default, which lacks Perl's
subexp-call recursion and if-else conditional syntax entirely — strictly
worse for a PCRE-oracled corpus).

**Every known divergence from real PCRE semantics this lane found**
(the full witness census, with every command and line-number citation,
is `docs/dev/measurements/2026-09-17-onig-capability-witness-census-
6.9.10.txt`; this is the summary a reader of this file needs without
opening that one):

1. **`ONIG_SYN_CAPTURE_ONLY_NAMED_GROUP`** — Perl_NG's own behavior flag
   (`src/regsyntax.c`, the `OnigSyntaxPerl_NG` table's third field). If a
   pattern mixes NAMED and UNNAMED capturing groups, Oniguruma reports
   captures for the NAMED ones only — the unnamed groups' spans are
   simply not delivered. **PCRE always captures both.** This lane did
   not find (and did not go looking for) a corpus pattern that trips
   this — `wild-logparse-syslogbase-expanded` (the one `requires-named-
   groups` pattern) uses named groups exclusively — but it is a real,
   silent, MIXED-group hazard for any future pattern that combines the
   two, worth checking before trusting an onig-default capture count
   against a mixed-group pattern's oracle row.
2. **Recursion: a SPELLING gap, not a capability gap.** `(?1)`,
   `(?&name)`, `(?0)` (Oniguruma's own "call group 0 = the whole
   pattern" convention) and `\g<1>`/`\g<name>` all compile and, on the
   corpus's own two working witnesses (`nested-comment-rec`'s `(?1)`,
   `bracket-array-define`'s `(?(DEFINE)...)` + `(?&brackets)`), run
   correctly. **PCRE's `(?R)` shorthand does NOT parse at all** under
   Perl_NG (`R` is not a recognised group-option character — the parser
   reads past it as ordinary text and the paren count goes wrong,
   `onig_new` returns `ONIGERR_UNMATCHED_CLOSE_PARENTHESIS`); confirmed
   on the corpus's own `balanced-parens-rec` (`(?R)`), the ONE recursion
   pattern that refuses. `(?R)` → `(?0)` is a genuine `variant.kind:
   syntax-only` rewrite (capability_set_v1.md §6.2's table) for whoever
   wants this pattern to run on `onig-default` — not built by this lane
   (bench/capability's own `variants.tsv` stays empty in v1; see its
   CLAUDE.md).
3. **`\p{...}` under `ONIG_ENCODING_ASCII` is a NARROWER, DIFFERENT
   vocabulary than PCRE's, not a subset by spelling coincidence.**
   `\p{Alpha}` (a POSIX-style ctype name) compiles; `\p{L}` (a real
   Unicode General Category, the shape virtually every PCRE `\p{...}`
   corpus pattern actually uses) is REFUSED
   (`ONIGERR_INVALID_CHAR_PROPERTY_NAME`, "invalid character property
   name {L}"). See (d) below for the encoding consequence this follows
   from.
4. **`control-verbs`: two names compile by REGISTRY COINCIDENCE, not
   partial verb support.** `(*FAIL)` and `(*SKIP)` compile because
   Oniguruma's OWN, structurally different CALLOUT mechanism
   (`ONIG_SYN_OP2_ASTERISK_CALLOUT_NAME`) has a small built-in callout
   registry (`src/ascii.c`'s `init()`: `name = "FAIL"; BC0_P(name,
   fail);` etc.) that happens to share two of PCRE's five control-verb
   NAMES. `(*ACCEPT)` is not in that registry
   (`ONIGERR_UNDEFINED_CALLOUT_NAME`). This lane did NOT verify that a
   compiling `(*FAIL)`/`(*SKIP)` callout produces PCRE's exact
   backtracking behaviour byte for byte — a callout can invoke a
   user-supplied function, and this driver registers none, so what
   fires is Oniguruma's own DEFAULT for an unregistered callout, not
   independently confirmed against PCRE's control-verb semantics.
5. **`callouts`: PCRE's `(?Cn)` spelling is not recognised at all**
   (`ONIGERR_UNDEFINED_GROUP_OPTION`) — a different feature family
   (Oniguruma's own `(?{...})`/`(*name)` callout syntax), not this
   token's spelling.
6. **`(?P<name>...)` (Python's named-group spelling) does not compile**
   under Perl_NG (`ONIGERR_UNDEFINED_GROUP_OPTION`) — only `(?<name>...)`
   (Oniguruma's/Ruby's/PCRE's own spelling) does. `named-groups`'s own
   definition is "any named-group spelling", so the token is still
   satisfied; a pattern authored with the `(?P<...>)` spelling
   specifically would need the same `syntax-only` rewrite treatment as
   item 2's `(?R)`.
7. **`lookbehind-variable`: ALL alternatives of one lookbehind must share
   one fixed width**, stricter than "per-branch fixed, branches may
   differ" — `(?<=a|bc)x` (branches of width 1 and 2, both individually
   fixed) is REFUSED (`ONIGERR_INVALID_LOOK_BEHIND_PATTERN`, "invalid
   pattern in look-behind"). Confirmed on the corpus's own
   `negation-scope-lookbehind-var`, which reproduces the exact same
   refusal.

## (d) The encoding choice: `ONIG_ENCODING_ASCII`

**Chosen over `ONIG_ENCODING_UTF8`** because this set's expectations are
oracled against libpcre2's DEFAULT 8-bit, non-UTF mode: every subject
byte is one "character", high bytes (`>= 0x80`) included, never a decode
error. `src/ascii.c`'s `OnigEncodingASCII` struct confirms this by
construction: `mbc_enc_len` is `onigenc_single_byte_mbc_enc_len` (always
length 1), and `is_valid_mbc_string` is `onigenc_always_true_is_valid_
mbc_string` — UNCONDITIONALLY true, so no byte sequence is ever an
encoding error. **CONFIRMED LIVE** (this lane, 2026-09-17): the same
high-byte witness `tools/selfcheck.py check_high_byte_pattern_argv` uses
for pcrec — pattern `\x93[\x20-\x7e]*\x94`, subject `\x93hello\x94` — runs
through `onig-default` end to end (real driver, real subprocess argv, a
pattern FILE never argv text) and matches `[0,7)` exactly.

**Consequence for `\p{...}`** (item 3 above): under ASCII encoding,
Oniguruma's property/ctype table is POSIX-style names only (`Alpha`,
`Digit`, `Space`, `Punct`, ...), never real Unicode General Categories or
Scripts — `unicode-properties` is declared UNSATISFIED for `onig-default`
in the `ext bench` matrix as a direct result of THIS encoding choice, not
a blanket Oniguruma limitation (compiling under `ONIG_ENCODING_UTF8`
would very likely change this verdict — untested by this lane, since the
set's own corpus and encoding contract are ASCII throughout and no
`onig-utf8` config is chartered).

**Consequence for case folding**: `ONIG_OPTION_IGNORECASE`'s fold table
under ASCII encoding is `onigenc_ascii_apply_all_case_fold` — ASCII
`A-Z`/`a-z` only, never a Unicode case-fold (Turkish dotless-i, German
ß-to-ss, etc.). Not witnessed against a corpus pattern by this lane (no
`(?i)` pattern in `bench/capability`'s own set at this writing); named
here so a future one is not surprised.

## The `ext bench` capability declaration (`bench/capability/gen_patterns.py`'s
`EXT_BENCH_ROSTER`, regenerated — never hand-edited — into `patterns.rxt`)

**CB5 and CB6 were resolved BEFORE this declaration was written**, by
direct read of Oniguruma 6.9.10's own source (`src/regparse.c`,
`src/regexec.c`, `src/regcomp.c` — fetched from the upstream `v6.9.10` git
tag and diffed BYTE-IDENTICAL against this box's installed
`/usr/include/oniguruma.h` before anything else was read):

- **CB5 (`atomic-group`) — SATISFIED, UNCONDITIONALLY.** `(?>...)` is
  parsed under EVERY syntax profile (`regparse.c:7886-7888`'s `case '>':`
  carries no `IS_SYNTAX_OP2` guard, unlike its neighbouring cases) and
  compiles to a fully wired `BAG_STOP_BACKTRACK` node — 7 further
  references in `regparse.c` (including possessive-quantifier lowering,
  which REUSES the same node — direct evidence it is load-bearing, not
  vestigial) and 13 in `regcomp.c` across optimization, length
  computation and the bytecode emitter. Live: `(?>a*)b` compiles (the
  same witness pcrec's own census used, `docs/dev/lanes/
  b42cap_report.md` §2, for direct cross-engine comparability).
- **CB6 (`k-reset`, `\K`) — SATISFIED, and ARCHITECTURALLY EQUIVALENT to
  PCRE's own `\K`, not an approximation.** `\K` compiles to a
  `SAVE_KEEP` gimmick (`regparse.c:2809`) under `ONIG_SYN_OP2_ESC_
  CAPITAL_K_KEEP` (present in Perl, Perl_NG, Python, Oniguruma, Ruby —
  every syntax but the POSIX-family ones). At match time
  (`regexec.c:4319-4351`) the current position is pushed onto
  Oniguruma's own BACKTRACKABLE stack (so a `\K` inside a branch that
  later backtracks correctly unwinds, exactly as PCRE's does); on
  overall match success (`regexec.c:3070,3121,3127,3141`) that saved
  position OVERRIDES the reported match START without moving the actual
  search anchor — precisely PCRE's `\K` semantics. Live: `a\Kb` compiles;
  `bench/email`'s own `quick --regime match --testee onig-default`
  (5/5 subjects agreeing with the oracle on the whole-subject `\z`-
  wrapped artifact) is independent end-to-end corroboration.

**The full witness matrix** (17 REQUIRES tokens, one or more isolated
witnesses each, PLUS all 64 real `bench/capability` corpus patterns
through the real adapter) is
`docs/dev/measurements/2026-09-17-onig-capability-witness-census-
6.9.10.txt`, with `docs/dev/measurements/probe_onig_capability_census.py`
beside it as the reproducing script. **13 of 17 SATISFIED**: `backrefs`,
`lookaround`, `possessive-quantifier`, `atomic-group`, `recursion`,
`conditionals`, `k-reset`, `named-groups`, `free-spacing`,
`span-reporting`, `non-utf8-subject`, `captures`, `true-end-anchor`.
**4 NOT**: `lookbehind-variable`, `control-verbs`, `unicode-properties`,
`callouts` — each with its own witnessed reason in (c) above, and the
`unicode-properties` one is this census's own "wrong first-cut" catch
(the L5 lesson the brief names): a first-cut reading of "does `\p{...}`
PARSE at all" would have said yes, and only the REAL-property-name
witness (`\p{L}`, not `\p{Alpha}`) exposes that the vocabulary is
narrower than PCRE's under this encoding choice.

**Corpus confirmation, not merely isolated witnesses**: 62 of 64 real
`bench/capability` patterns compile through `onig-default`; the two
refusals (`negation-scope-lookbehind-var`,
`requires-lookbehind-variable`; `balanced-parens-rec`,
`requires-recursion`'s `(?R)` spelling) both reproduce their isolated
witness's exact `ONIGERR_*` code. `recursion` stays SATISFIED (the other
two `requires-recursion` corpus patterns compile clean) — the one
refusal is left to fail HONESTLY as a real `did-not-compile`
(`refusal_class: syntax`) under the pre-compile capability policy, rather
than being hidden behind a wholesale token withhold that would
misrepresent 2 of 3 real recursion patterns as untestable.

## Refusals, first-class

`onig_new` failure → `did-not-compile` BY NAME, `diagnostic` carrying
Oniguruma's own `onig_error_code_to_str` message (never re-typed by this
adapter). `refusal_class` (capability_set_v1.md §5.5: "declared ONLY by a
config whose engine gives a closed, structural signal" — Oniguruma's
`ONIGERR_*` is exactly that) is declared and derived from the parsed
`ONIGERR_*` code: `size-limit` for `ONIGERR_PARSE_DEPTH_LIMIT_OVER` (-16,
a compile-time parse-nesting budget, DEFAULT 4096), `syntax` for every
other refusal code this adapter's diagnostic parser can read, ABSENT
(never a fabricated third value) when it cannot.

A construct the `ext bench` matrix DECLARES missing never reaches this
adapter's own refusal path at all — `pcrecbench.capability`'s pre-compile
policy intercepts it first (`unsupported-by-declaration`, with
`declaration_ref` naming this file's own census).

## `gave-up`: MEASURED to fire at DEFAULT settings, not merely a future
`onig-lowretry` config's job

Four MATCH-TIME resource-limit codes (`src/regexec.c`, this lane's own
direct read, 2026-09-17 — never probed blind):

    ONIGERR_MATCH_STACK_LIMIT_OVER           (-15)
    ONIGERR_RETRY_LIMIT_IN_MATCH_OVER        (-17)
    ONIGERR_RETRY_LIMIT_IN_SEARCH_OVER       (-18)
    ONIGERR_SUBEXP_CALL_LIMIT_IN_SEARCH_OVER (-19)

Deliberately NOT in the set, each for a stated reason (mirroring
`testees/pcre2/adapter.py`'s own convention): `ONIGERR_MEMORY` (-5, an
allocation failure, not a configured budget — `crashed`);
`ONIGERR_PARSE_DEPTH_LIMIT_OVER` (-16, raised in `src/regparse.c` — i.e.
at COMPILE time, so it is the ordinary `did-not-compile`/`refusal_class:
size-limit` path above, never a per-subject code at all).

**A genuine finding, not a documentation exercise**: `src/regint.h`'s
`DEFAULT_RETRY_LIMIT_IN_MATCH` is **10,000,000, NOT unlimited**
(`DEFAULT_MATCH_STACK_LIMIT_SIZE` and `DEFAULT_RETRY_LIMIT_IN_SEARCH` ARE
0/unlimited by default — only the match-retry budget is bounded out of
the box). **CONFIRMED LIVE** (this lane, direct driver invocation,
2026-09-17): the classic catastrophic-backtracking witness `(a+)+$` over
40 `a`s followed by a non-matching byte gives up under `onig-default`'s
UNMODIFIED defaults in ~0.21 s — `giveup:-17:retry-limit-in-match over`.
**This is `gave-up`, recorded by name, not raised as a crash or a
timeout — exactly the deliverable this lane was asked to confirm.** The
LATER `onig-lowretry` config (a small `onig_set_retry_limit_in_match`,
capability_set_v1.md §8) exists to make this fire on a WIDER range of
ReDoS shapes at a controlled, small budget — `onig-default` already
demonstrates the mechanism on a strong-enough witness without it.

## The I-72 lesson: pattern bytes end to end

This adapter passes the pattern via a FILE
(`_compile_one`'s `patfile`/`--pattern`), exactly like `testees/pcre2/
adapter.py`'s own convention — never the raw pattern bytes through argv
text, which is where I-72's mojibake bug lived on the pcrec side
(`pattern.decode("latin-1")` + subprocess's own `os.fsencode` UTF-8
re-encoding of a `str` argv element). Confirmed live (both the isolated
`\x93[\x20-\x7e]*\x94` witness above, and via `pcrecbench quick` end to
end against `bench/email`) that a raw high pattern byte survives
untouched. `check_high_byte_pattern_argv` in `tools/selfcheck.py` now
also runs this exact witness through `onig-default` alongside its
existing `pcrec-auto`/`pcrec-vm` arms — the SAME pattern/subject pair, so
a reader sees all three engines answer the identical `[0,7)` span from
one shared witness.

## Two forms, mirroring `testees/pcrec/adapter.py`

Oniguruma has no runtime end-anchor option (no `PCRE2_ENDANCHORED`
equivalent), so `Adapter.compile()` returns TWO `CompileResult`s per
pattern, exactly like pcrec's own two-artifact model:

- **`plain`** — the canonical pattern text, compiled once. Measured with
  `onig_search` (unanchored, leftmost) for `search_short`/`throughput`.
- **`whole-subject`** — `pcrecbench.record.whole_subject_text(pattern)`
  (`(?:<pattern>)\z`, the SAME bytes pcrec's own whole-subject artifact
  uses — imported, never re-derived). Measured with `onig_match` (which
  matches AT the given position only, never scanning — the driver always
  calls it at offset 0) for the `match` regime: `onig_match`'s
  fixed-position semantics supply the START anchor, the wrapper's own
  `\z` supplies the END anchor. `driver.c`'s `--form`/`--mode` cross-check
  documents (and enforces, by dying loudly rather than silently
  measuring the wrong form) that the two flags are set together by the
  adapter and there is no second, independent anchoring dial once
  `--form` is chosen.

CONFIRMED end to end via `pcrecbench quick --subbench email --regime
match --testee onig-default --vs pcre2-interp` (5/5 subjects agreeing
with the oracle on the whole-subject artifact) and `--regime
search_short`/`throughput` (5/5 and 2/2 respectively) — see the lane
report for the full transcripts.

## `--utf8`: the character-boundary find-all advance ([B77] U1)

The driver protocol's `--utf8` flag (`pcrecbench/adapters.py`'s header;
`docs/design/utf8_set_v1.md` 8.4) switches the find-all EMPTY-MATCH
advance from `start + 1` to the next CHARACTER boundary -- pcrec
match_api.md S3.1.1's normative utf8 rule: from `start + 1`, skip every
byte in 0x80-0xBF, stop at the first byte outside that range or at the
subject's end (`utf8_next_start` in the driver, the same rule as
`oracle_pcre2.next_start`). `adapter.py` passes it iff the harness set
the handle's `utf8_advance`, which it does iff the pattern's ORACLE
OPTION WORD carries PCRE2_UTF (a set declaring `[expectations] encoding
= "utf8"`) -- so on every byte set the argv and the advance are exactly
what they were. Checked by `make check-harness`'s
`check_utf8_find_all_advance` (`x*` over a 1/2/3/4-byte-character
subject: 6 positions with `--utf8`, the UTF oracle's count; 12 without).

The flag moves the advance only; the engine stays `ONIG_ENCODING_ASCII`
(section (d)) -- an `onig-utf8` encoding is lane U2's (`utf8_set_v1.md` 7.1).

## `onig-utf8` ([B77] U2) -- the re-census

The driver's encoding was a compile-time constant; U2 made it a RUNTIME
choice (`--encoding utf8|ascii`, default ASCII, so `onig-default` passes
nothing and is unchanged). `encoding = "utf8"` -> `ONIG_ENCODING_UTF8` on
`onig_initialize` and `onig_new`, compile and every measure invocation;
`config_extra = utf8`: `oniguruma_6.9.10_default-caps-simdna_utf8`.

THE RE-CENSUS this file's ASCII-encoding paragraph predicted, WITNESSED
(`docs/dev/measurements/2026-09-25-b77u2-utf8-witness-census.txt`):

- `unicode-properties` FLIPS to SATISFIED -- `\p{L}`, `\p{Lu}`,
  `\p{N}`, `\P{L}`, `\p{Zs}` all compile and answer the oracle.
- **Class scope is UNICODE by default under UTF-8 + PERL_NG** (no
  `ONIG_OPTION_ASCII_RANGE`): `\w+` matches all of `Москва`, `\d{4}`
  four Arabic-Indic digits, `a\sb` across U+00A0, `[[:alpha:]]+` `é` --
  so `ascii-class-scope` is NOT satisfied. `unicode-class-scope` is NOT
  either: the set's `(*UCP)` spelling is read as a CALLOUT and refused
  (`ONIGERR -229, undefined callout name`). `onig-utf8` therefore sits
  out BOTH class-scope families -- an outcome utf8_set_v1.md 7.4 did not
  predict. An `ONIG_OPTION_ASCII_RANGE` sibling would satisfy
  `ascii-class-scope`; named, not built.
- Scripts: bare names compile and read SCRIPT (`\p{Greek}` `nomatch` on
  U+0342, the oracle `match`); `sc=`/`Script=`/`scx=`/
  `Script_Extensions=`/`InGreek` refuse (`-223, invalid character
  property name`).
- `\B` over `é` answers `nomatch` where the oracle answers `match [0,0)`
  -- a consequence of the Unicode `\w`, i.e. every `\b`/`\B` member is
  class-scope-dependent here.

Declares 14/20 (the byte sibling's withholds carried over;
`non-utf8-subject` NOT by rule -- Oniguruma documents invalid UTF-8
input as undefined).
