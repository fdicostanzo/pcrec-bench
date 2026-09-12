# [B42] research note 2 — the engine capability and option landscape

STATUS: research note, read-mostly, INPUT to `docs/design/capability_set_v1.md`
([B42] phase (b)), never a spec. Lane `b42engines`, 2026-09-12. Covers the
[B7] roster named in `docs/dev/plan.md`: RE2, Rust `regex`, Oniguruma, TRE
(POSIX-tagged), Vectorscan (semantics-tagged; Hyperscan-compatible),
python `re`, perl, plus libpcre2 (interp / JIT / DFA-match) and pcrec's own
configs, which this project already adapts. Every claim below is either
(a) fetched from the engine's own docs/source this session (cited by URL,
fetched 2026-09-12 unless noted) or (b) read from THIS repository's own
committed source (cited by path:line) or (c) probed on this box (command
shown). Nothing is asserted from memory alone without a citation; where I
could not verify a claim in the time budget it is flagged in §8.

Sources for the bench's own vocabulary (outcome axis, variant axis,
compile-cost classes, `engine_metadata`) are this project's own docs, read
in full before writing this note: `APPROACH.md`,
`docs/design/requirements.md` (all of it — §3 compile cost, §4.4 outcome
axis, §4.5 variant axis, R-BENCH-4 engine neutrality in the OD ledger's
framing), `docs/design/record_schema.md` §5-§9 (the fixed enums, the
`engine_metadata` declaration rules, the match/compile row field tables),
`pcrecbench/adapters.py`'s driver-protocol docstring (the shared timing
loop, the driver output columns), and `testees/pcre2/CLAUDE.md` +
`testees/pcrec/CLAUDE.md` (today's two adapters' compile-cost definitions
and metadata declarations). Citations to these below use the short forms
`requirements.md §N`, `record_schema.md §N`, `adapters.py:N`.

## 0. What this note is answering

[B42] charters a capability-survey set that must (Frank's charter,
`plan.md` [B42] row): anticipate every [B7] engine as a testee; record
"this engine cannot run this pattern" as a first-class outcome, never an
error; allow slight per-engine syntactic adjustment when semantics are
preserved; and compare compile time and other metrics apples-to-apples
where that is honest, stating plainly where it is not. This note gathers,
per engine, what a testee ADAPTER for it would need to declare under
`record_schema.md §7`'s three rules (declare before use; pattern-scope vs
match-scope; a mask is an array of bit names) and under
`requirements.md §4.4`'s outcome axis and §4.5's variant axis.

## 1. Obtaining each engine on this box, and its C-callable surface

Probed 2026-09-12 (`apt-cache policy <pkg>`, `apt-cache search`,
`pkg-config --list-all`, `dpkg -l`; this box is Ubuntu, codename
`resolute` per the archive path in the outputs below).

| engine | apt package(s) | candidate version | C-callable surface | licence |
|---|---|---|---|---|
| libpcre2 | `libpcre2-dev` (+ `-8-0`/`-16-0`/`-32-0`/`-posix3`) | 10.46-1build1, **installed** | native C API (`pcre2_compile`, `pcre2_match`, `pcre2_dfa_match`, `pcre2_jit_compile`) | BSD (3-clause, with the PCRE2 exception for a historical name-attribution clause) [pcre2project.github.io/pcre2/project/licence](https://pcre2project.github.io/pcre2/project/licence/) |
| RE2 | `libre2-dev` (candidate 20250805-1build3), runtime `libre2-11` **already installed** (pulled in transitively by `node-re2`) | 20250805-1build3 | **C++ only** — RE2 ships no C API. A C-callable wrapper needs a SEPARATE project, `cre2` ([marcomaggi/cre2](https://github.com/marcomaggi/cre2)), which is NOT packaged for this box (`apt-cache search cre2` returns nothing; checked) — it would have to be vendored and built here, the same posture as pcrec's own shim | BSD (3-clause) [github.com/google/re2](https://github.com/google/re2) |
| Rust `regex` | no runnable binary package; `librust-regex-dev` (1.12.2-1) and `librust-regex-automata-dev` (0.4.13-1) exist as Debian SOURCE packages for building other Debian packages, not as a linkable C library | 1.12.2-1 (source) | **no C API in the crate itself.** The crate used to ship a `regex-capi` sub-crate exposing a C ABI (`rure`, `regex-capi/include/rure.h`) — still present in the `rust-lang/regex` GitHub tree today ([github.com/rust-lang/regex/tree/master/regex-capi](https://github.com/rust-lang/regex/tree/master/regex-capi)) but NOT published as a crate release usable via a simple `cargo build` of a dependent (no `rure` package on this box's apt mirror; I could not confirm from crates.io in this session whether `rure`/`regex-capi` is still actively released — flagged in §8). Getting a linkable `.so` means building `regex-capi` from the rust-lang/regex git tree with `cargo build --release` (needs `cargo`/`rustc`, both apt-installable here: candidate 1.93.1ubuntu1) | dual MIT / Apache-2.0 [github.com/rust-lang/regex/blob/master/LICENSE-APACHE](https://github.com/rust-lang/regex/blob/master/LICENSE-APACHE) |
| Oniguruma | `libonig-dev` (6.9.10-1build1), runtime `libonig5` **already installed** | 6.9.10-1build1 | native C API (`onig_new`, `onig_search`, `onig_error_code_to_str`) | BSD (2-clause) [en.wikipedia.org/wiki/Oniguruma](https://en.wikipedia.org/wiki/Oniguruma) |
| TRE | `libtre-dev` (0.9.0-1build1), `libtre5` | 0.9.0-1build1 | native C API, the POSIX shape (`tre_regcomp`/`regcomp`, `tre_regexec`/`regexec`) plus TRE's own extensions (`tre_regacomp`/`tre_regaexec` for approximate matching) — [laurikari.net/tre/documentation/regcomp](https://laurikari.net/tre/documentation/regcomp/) | BSD-like (2-clause) [github.com/laurikari/tre/blob/master/LICENSE](https://github.com/laurikari/tre/blob/master/LICENSE) |
| Vectorscan (Hyperscan-compatible) | `libvectorscan-dev` (5.4.11-2ubuntu2) **Replaces/Provides/Conflicts** `libhyperscan-dev` — this box's actual "Hyperscan" package IS Vectorscan under the hood; a SEPARATE, older `libhyperscan-dev`/`libhyperscan5` (5.4.2-4, source package `hyperscan`) also exists in the archive and is installable, but per Ubuntu's own package relationship the two conflict at install time. **Recommendation: install `libvectorscan-dev`** — it is the actively maintained fork ([VectorCamp/vectorscan](https://github.com/VectorCamp/vectorscan)) and is what [B7]'s roster names ("Vectorscan (semantics-tagged)") | 5.4.11-2ubuntu2 | native C API, Intel Hyperscan-compatible (`hs_compile`, `hs_scan`, `hs_alloc_scratch`) | BSD (3-clause) [github.com/VectorCamp/vectorscan/blob/master/LICENSE](https://github.com/VectorCamp/vectorscan/blob/master/LICENSE) |
| python `re` | `python3` **installed**, 3.14.3-0ubuntu2 | 3.14.3 | not C-callable in the sense the driver protocol wants (no `.so` entry point returning ovector-shaped results); a driver would embed the CPython interpreter (`Py_Initialize` + `PyRun_String`/`PyObject_CallMethod`) the way `python3-pcre2`-style bindings do, OR shell to a `python3` subprocess and lose the batched in-process timing loop the driver protocol requires (`adapters.py:33-35`: "never a clock per call and never an external per-call wrapper"). The embedding route is the one that fits the protocol | PSF licence |
| perl | `perl` **installed**, 5.40.1-7ubuntu0.3 | 5.40.1 | same shape of problem as python: no ovector-returning `.so` call; a driver embeds `libperl` (`perl_construct`/`perl_parse`/`perl_run`, `PCRE`-adjacent XS-style calls) or shells to `perl -e`, same protocol conflict | Artistic License 1.0 / GPL-1.0-or-later (dual) |
| pcrec | this project's own read-only sibling, pinned per `testees/pcrec/pin.sh` | d34c9131 (current pin) | pcrec's own emitted `.so` + `shim.c` (already built, `testees/pcrec/CLAUDE.md`) | N/A — internal project |

**Consequence for the driver protocol.** Every C-callable engine (pcre2,
RE2-via-cre2, Rust-regex-via-rure, Oniguruma, TRE, Vectorscan, pcrec) fits
`adapters.py`'s driver shape directly: one driver binary per engine,
`dlopen`/link against the library, one batched in-process loop
(`adapters.py:30-35`). The two SCRIPTING engines (python `re`, perl) do
not fit without embedding the interpreter — shelling out breaks the
protocol's own stated reason for existing (the outer-process `timeout`
alone costs ~108.7 ms per call on this box, `adapters.py:34-35` citing
`requirements.md §3` C5). This is a real, first-class design question
for [B42] phase (b), not a detail: **either an embedding driver is built
for python/perl (the harder adapter of the roster), or these two engines
are measured on COMPILE COST and CORRECTNESS only, with match timing
explicitly out of scope and the record's `regime` coverage marked
partial for them.** I recommend the second for a v1 capability set (§7
below) and the first as a later roster item, matching how
`requirements.md §10` staged pcrec/pcre2 before RE2/rust/etc.

## 2. Dialect and match semantics — where the SAME pattern can give a DIFFERENT correct answer

This is the section the capability set's expectations must be tagged
against: `requirements.md §7` says conventions (`perl-leftmost-first` /
`posix-leftmost-longest` / `all-ends`) are tagged per case and testees
scored against their own; `record_schema.md §5` already carries the three
tokens as `conventions[]`. The engines below split cleanly into two
camps, plus TRE's own hybrid.

### 2.1 Leftmost-first (Perl/PCRE-style backtracking semantics)

**pcre2, perl, python `re`, Oniguruma (default mode).** All four search
for the match a real backtracking engine would find FIRST by trying
alternatives in the order written and quantifiers greedily
left-to-right, backtracking on failure. This is `record_schema.md
§5`'s `perl-leftmost-first`. Consequences that matter for a shared
expectation set:

- Alternation order affects which branch wins on an ambiguous string:
  `a|ab` against `"ab"` matches `a` (first alternative that succeeds),
  never the longer `ab`. RE2/Rust regex do NOT preserve this (§2.2).
- Backreferences are meaningful (the engine can literally re-examine what
  a numbered/named group captured) — RE2, Rust regex and Hyperscan
  cannot do this at all (§3), which is a capability gap, not a semantics
  difference.
- Capture group values on a partially-backtracked alternative reflect
  whichever branch the engine committed to, which may differ between two
  leftmost-first engines when their internal search ORDER differs on a
  genuinely ambiguous pattern (Oniguruma's own greedy/backtracking
  strategy is not byte-identical to PCRE2's in every corner — this is
  the class of finding `docs/dev/upstream_findings.md` exists to record,
  per `requirements.md §7`).

**Empty-match rules.** PCRE2/Perl/Python's `find-all` loop (the bench's
own `--find-all`, `adapters.py:20-22`) must advance past a zero-length
match to avoid an infinite loop; PCRE2's own convention (documented in
`pcre2_match`) is that an empty match is reported once and the next scan
starts one code unit later — this is exactly the driver protocol's own
`pos = max(end, pos+1)` rule (`adapters.py:21`), so the bench's find-all
operation is ALREADY the PCRE2 convention. RE2's `re2::RE2::FindAndConsume`-
style loops and Rust regex's `find_iter` use the analogous rule; this
needs a positive check per engine rather than an assumption (§6).

### 2.2 Leftmost-longest / one-pass automaton semantics (linear-time engines)

**RE2, Rust `regex` (in `regex` crate's default construction), and
Hyperscan/Vectorscan** all guarantee no catastrophic backtracking by
using finite-automaton simulation instead of backtracking, and their
match SELECTION rule is not "try alternatives in written order":

- **RE2** defaults to leftmost-first-LIKE semantics for `Find`-family
  calls (RE2 emulates Perl's submatch semantics via its own algorithm,
  NOT literal backtracking) but exposes a genuine POSIX
  leftmost-longest mode via `RE2::Options::set_longest_match(true)` /
  `cre2_opt_set_longest_match` (fetched from
  [marcomaggi.github.io/docs/cre2.html/options.html](http://marcomaggi.github.io/docs/cre2.html/options.html),
  2026-09-12: "posix_syntax... longest_match: Search for longest match,
  not first match" — default disabled). So RE2 is capability-wise ABLE
  to answer either convention, selectable per compile — this bench
  should record which mode a given RE2 testee compiled with as a
  `record_schema.md §7` `pattern`-scoped `engine_metadata` pair
  (e.g. `match_semantics: perl-like` / `posix-longest`), not assume one.
- **Rust `regex`** is leftmost-first BY DEFAULT for `find`/capture
  semantics ("preserves the same match semantics as Perl-like engines...
  for capture groups", per the crate's own long-standing documentation)
  but internally is a hybrid of Thompson NFA / lazy DFA / (since 1.9-ish)
  an optional "one-pass" engine for patterns without certain constructs —
  correctness-observable behaviour (which match/spans/captures win) is
  documented as leftmost-first-compatible, so for THIS bench's purposes
  Rust regex can be tagged `perl-leftmost-first` for its default
  API — a claim that must be VERIFIED against the oracle on every
  ambiguous-alternation subject the capability set includes (§6), since
  I have not independently reproduced this from source in this session
  and am relying on the crate's documented claim (flagged §8).
- **Hyperscan/Vectorscan is explicitly NOT leftmost-first-comparable at
  all**, and this is the sharpest semantics gap on the roster: Hyperscan
  is an ALL-MATCHES streaming scanner, not a single-match engine. It
  reports EVERY match end-offset for every pattern in a scan (unless
  `HS_FLAG_SINGLEMATCH` is set), in an order that "can produce matches
  that are not returned in order" for assertion-bearing patterns
  (`hs_expr_info_t.unordered_matches`, fetched from
  [intel.github.io/hyperscan/dev-reference/api_files.html](https://intel.github.io/hyperscan/dev-reference/api_files.html)).
  This is `record_schema.md §5`'s `all-ends` convention by name. A
  capability-set expectation for Hyperscan/Vectorscan is therefore NOT
  "the match" but "the SET of match end-offsets", and the driver
  protocol's `--find-all` NON-OVERLAPPING count (`adapters.py:20-22`)
  is the wrong shape for it outright — Hyperscan's natural output is
  all-ends-at-every-position, which is neither "first match" nor
  "non-overlapping count". **This is the one engine on the roster where
  the driver protocol itself needs a THIRD invocation mode or a declared
  variant that restates the expectation in all-ends terms** (§7).

### 2.3 TRE — POSIX by declared default, but not backtracking

TRE implements the POSIX regex API (`regcomp`/`regexec`) and targets
POSIX leftmost-longest submatch semantics by specification (`laurikari.net/
tre/documentation/`, 2026-09-12 fetch: "TRE tries to conform to... POSIX").
Internally it is a tagged-NFA / bit-parallel simulation (Laurikari's own
published algorithm), not literal backtracking, so it shares RE2/Rust's
"no catastrophic backtracking" property while sharing PCRE2/pcre2's POSIX
label — a genuinely third semantics bucket for the enum, already covered:
`record_schema.md §5`'s `posix-leftmost-longest` token is exactly this,
and [B7]'s own roster line already tags TRE `(POSIX-tagged)`. TRE ALSO
exposes non-POSIX extensions (`tre_regcomp` beyond the POSIX subset, and
approximate/fuzzy matching via `tre_regaexec` with a configurable cost
budget) that this bench has no use for (approximate matching answers a
different question than "did this pattern match this subject") and should
declare `unsupported-by-declaration` for, since using it would silently
change what a "match" means.

### 2.4 Case-folding, UTF-8/bytes and empty-match summary table

| engine | UTF-8 mode | case-folding scope | notable empty-match/anchor quirk |
|---|---|---|---|
| pcre2 (8-bit, this bench's build) | opt-in `PCRE2_UTF`, ASCII bytes by default | ASCII by default; `PCRE2_UCP` extends `\d`/`\w`/case-fold to Unicode properties | `$` matches before a final `\n` at `options=0` — exactly why `record_schema.md §5` ADDITIONS 3 makes pcrec's whole-subject artifact anchor with `\z`, never `$` (quoted in full below, §4) |
| RE2 | UTF-8 by default (`RE2::Options::encoding`, `EncodingUTF8`/`EncodingLatin1`) | ASCII by default; Unicode-aware with `(?i)` still ASCII unless the pattern uses `\p{...}` properties, which RE2 DOES support (RE2 supports Unicode character classes, unlike lookaround) | — |
| Rust `regex` | Unicode-by-default (`unicode: true` builder option, fetched from [docs.rs/regex/latest/regex/struct.RegexBuilder.html](https://docs.rs/regex/latest/regex/struct.RegexBuilder.html) 2026-09-12) | Unicode case folding by default; ASCII-only mode requires disabling `unicode` and is then a materially different pattern language (some Unicode-only constructs become errors) | `line_terminator` builder option changes what `$`/`.` treat as a line boundary, default `\n` byte |
| Oniguruma | selectable ENCODING at `onig_new` time (`ONIG_ENCODING_UTF8`, `ONIG_ENCODING_ASCII`, others) — a per-compile choice, not a runtime flag | encoding-dependent; UTF-8 encoding folds Unicode case by default | multiple SYNTAX profiles (`ONIG_SYNTAX_PERL_NG`, `ONIG_SYNTAX_POSIX_BASIC`, ...) change what the SAME byte pattern means — a second axis beyond encoding |
| TRE | multibyte-locale-aware (`laurikari.net/tre/documentation/`: "supports multibyte character sets... e.g. Japanese locales") — driven by the C locale, not a compile flag | locale-dependent | — |
| Vectorscan/Hyperscan | `HS_FLAG_UTF8` / `HS_FLAG_UCP` per-pattern flags (mirrors pcre2's own flag names almost exactly) | ASCII by default; `HS_FLAG_CASELESS` folds; UCP for Unicode properties | streaming vs block mode changes what "the subject" even means (§5) |
| python `re` | Unicode `str` patterns are Unicode-aware by default; `bytes` patterns are byte-oriented | Unicode-aware `re.IGNORECASE` by default on `str` patterns, `re.ASCII` opts out | — |
| perl | Unicode-aware when the string/pattern carries the UTF8 flag; otherwise byte semantics — perl's own "the utf8 pragma" story, well known to be one of the more complex parts of the language | as pattern/string flags dictate | — |

## 3. Unsupported constructs, and how each engine REPORTS them

`requirements.md §4.4` wants a closed outcome set
(`compiled`/`did-not-compile`/`crashed`/`timed-out`/
`unsupported-by-declaration`) with the engine's diagnostic carried,
UNINDEXED, on a `did-not-compile` compile row
(`record_schema.md` compile-row field table, `diagnostic`). The
capability set's per-pattern REQUIRES tags (§7) are drawn from this table.

| engine | backrefs | lookaround | atomic/possessive | recursion/subroutines | conditionals | `\K` | Unicode properties | counted-repeat ceiling | how a refusal is reported |
|---|---|---|---|---|---|---|---|---|---|
| pcre2 | yes | yes | yes | yes | yes | yes | yes (`\p{...}`, `PCRE2_UCP`) | `{0,65535}` per PCRE2's own repeat-count ceiling (already this project's own finding, `bench/bounded`'s NOTES.md; NFA-cap-adjacent, not the same limit as pcrec's) | `pcre2_compile` returns NULL + an error code + offset; `pcre2_get_error_message` renders it — this project's own driver already surfaces this (`testees/pcre2/driver.c`) |
| RE2 | **no** | **no** (neither look-ahead nor look-behind, either direction) | **no** | **no** | **no** | **no** | yes — RE2 explicitly supports `\p{Greek}`-style Unicode character classes even though it lacks the lookaround/backref features (fetched [github.com/google/re2/wiki/Syntax](https://github.com/google/re2/wiki/Syntax), 2026-09-12) | governed by `max_mem`, not a fixed count (§4) | `RE2::RE2(pattern, options)` construction leaves the object not-OK; `RE2::error()` returns a message string, `RE2::error_code()` returns one of a CLOSED `ErrorCode` enum fetched verbatim from `re2.h` (`https://raw.githubusercontent.com/google/re2/main/re2/re2.h`, 2026-09-12): `NoError, ErrorInternal, ErrorBadEscape, ErrorBadCharClass, ErrorBadCharRange, ErrorMissingBracket, ErrorMissingParen, ErrorUnexpectedParen, ErrorTrailingBackslash, ErrorRepeatArgument, ErrorRepeatSize, ErrorRepeatOp, ErrorBadPerlOp, ErrorBadUTF8, ErrorBadNamedCapture, ErrorPatternTooLarge` — a closed, named set exactly the shape `did-not-compile`'s diagnostic wants, and `ErrorBadPerlOp` is specifically the one a lookaround/backref/atomic-group pattern hits |
| Rust `regex` | **no** (crate docs, fetched 2026-09-12: "not... backreferences") | **no** | **no** | **no** | **no** | **no** | yes, Unicode-by-default | `size_limit` (compiled program size) and `dfa_size_limit` (lazy-DFA cache) — see §4 | `.build()`/`Regex::new` returns `Result<Regex, Error>`; `Error` is a non-exhaustive enum with (at least) `Syntax(String)` and `CompiledTooBig(usize)` variants (fetched [docs.rs/regex/latest/regex/enum.Error.html](https://docs.rs/regex/latest/regex/enum.Error.html), 2026-09-12) — `CompiledTooBig` carries the limit that was exceeded as its own field, which is a capability the bench can read structurally rather than parse from a message |
| Oniguruma | yes | yes | — (depends on the chosen SYNTAX; Perl-NG syntax supports possessive quantifiers, POSIX syntaxes do not) | yes (`\g<name>`-style subexpression calls under ONIG_SYNTAX_PERL_NG) | limited | not general PCRE-style `\K`; has its own reset-point extensions under some syntaxes | yes, via `ONIG_OPTION_...` and its own Unicode property tables | governed by its own internal state-count limits, not independently confirmed in this session (flagged §8) | `onig_new` returns a nonzero `OnigCodeReturn` error code; `onig_error_code_to_str` renders a message into a caller-supplied buffer — a closed integer code with a name-lookup function, same shape as PCRE2's |
| TRE | yes (POSIX backreferences ARE part of POSIX ERE with TRE's extensions, unlike RE2) | **no** (POSIX has none; TRE's PERL-ish extension set does not add general lookaround either, not independently confirmed — flagged §8) | **no** | **no** | **no** | **no** | limited (multibyte/locale character classes, not `\p{...}` properties) | not independently confirmed in this session — TRE's own memory-bound note ("less than 50K... during regcomp()") suggests an internal bound exists but I found no named error code for hitting it (flagged §8) | POSIX `regcomp()` return code is a `REG_*` integer (`REG_BADPAT`, `REG_ESPACE`, etc, the standard POSIX set) rendered via `regerror()`/`tre_regerror()` |
| Vectorscan/Hyperscan | **no** | **no** | **no** (possessive/atomic grouping explicitly unsupported per compilation docs) | **no** (no subroutine/recursive references) | **no** (no backtracking-verb conditionals) | **no** (`\K` explicitly named unsupported) | via `HS_FLAG_UCP` | governed by database size / scratch-space limits determined at compile time, not a fixed count — see §4; ALSO governed by `min_width`/`max_width` reported per-pattern via `hs_expression_info` (fetched [intel.github.io/hyperscan/dev-reference/api_files.html](https://intel.github.io/hyperscan/dev-reference/api_files.html), 2026-09-12), a capability probe unique to Hyperscan on this roster | `hs_compile`/`hs_compile_multi` return `HS_COMPILER_ERROR` (or others) and populate an `hs_compile_error_t*` with a `message` string and an `expression` index (which of N multi-compiled patterns failed) — no closed enum of REASONS the way RE2's is, only free text (a capability-tag gap this bench would have to close by STRING-MATCHING known Hyperscan messages, which is fragile, or by declaring every unsupported construct in the sub-bench's own sidecar rather than trusting Hyperscan's message text — the safer choice, and consistent with `requirements.md §4.5`'s "declared variant" posture: KNOW in advance what an engine cannot do rather than discover it from a string) |
| python `re` | yes | yes (fixed-length lookbehind ONLY — variable-length lookbehind `(?<=a*)` is a `re.error` at compile, fetched [regular-expressions.info/python.html](https://www.regular-expressions.info/python.html) 2026-09-12 cross-checked against CPython 3.14 docs) | **yes since 3.11** (possessive quantifiers `x*+` and atomic groups `(?>...)`, per [learnbyexample.github.io/python-regex-possessive-quantifier](https://learnbyexample.github.io/python-regex-possessive-quantifier/) 2026-09-12 — this box's python3 is 3.14.3, so this bench's python testee HAS them) | **no** (no `(?R)`/`(?&name)`) | **no** | yes (`\K` explicitly unsupported by `re`; the third-party `regex` module — ALSO apt-installable here as `python3-regex` 0.1.20250918-1build1, candidate for a LATER roster slot, not [B7]'s named list — does support it) | yes, `\p{...}`-style via `re.UNICODE` default on `str` patterns (not full `\p{Script=...}` syntax the way pcre2/RE2 spell it — python spells Unicode categories differently, `\w`/`\d`/`\s` expand per-Unicode-category but there is no `\p{Greek}` token in stdlib `re`) | governed by CPython's own recursion-limit-adjacent internals for the backtracking engine, not a documented fixed count | `re.error` (a subclass of `ValueError`) raised at `re.compile()`, carrying `.msg`, `.pattern`, `.pos`, `.lineno`, `.colno` — structured enough to build a `did-not-compile` diagnostic from |
| perl | yes | yes | yes (`(?>...)`, possessive quantifiers) | yes (`(?R)`, named recursion) | yes | yes | yes, extensively (`\p{...}`, the fullest Unicode property support on the roster along with pcre2, which is intentional — PCRE was built to track Perl) | governed by perl's own internal limits, effectively "no practical construct is unsupported" — perl is close to a SUPERSET of pcre2's syntax rather than a subset, and is the one engine on the roster where the capability question INVERTS: the interesting finding is what perl does DIFFERENTLY from pcre2 on a shared construct, not what it lacks | a bad pattern raises a runtime exception (`qr/.../.` under `eval` dies with `$@` set to perl's own diagnostic string) — no structured error object, closer to Hyperscan's free-text shape than RE2's enum |
| pcrec | per pcrec's own supported-syntax registry (this project already reads it: `testees/pcrec/list_axes.tsv`, `list_definitions.tsv`, `list_limits.tsv`; `bench/syntax@0.1`'s 95-pattern census IS this table, mechanism family by mechanism family) — not re-derived here, it is this project's own existing knowledge | — | — | — | — | — | — | pcrec's own named limits registry (`--list-limits`, `PCREC_MAX_*`) — already this project's `did-not-compile` convention (`docs/dev/known_issues.md` KB-4) | pcrec's own `RX_ENGINE_WHY`-class diagnostic on its emit-c phase (`testees/pcrec/CLAUDE.md`'s KB-4 paragraph) |

**A structural observation for [B42] phase (b).** Three shapes of
"how a refusal is reported" exist on this roster: a CLOSED ENUM the
adapter can bucket without parsing prose (RE2's `ErrorCode`, python's
`re.error` fields, POSIX's `REG_*` codes, Oniguruma's `OnigCodeReturn`);
a size/limit VALUE carried structurally in the error itself (Rust regex's
`CompiledTooBig(usize)`); and FREE TEXT ONLY (Hyperscan's `message`
string, perl's `$@`, pcrec's `RX_ENGINE_WHY`-derived diagnostic). This
project's own `record_schema.md §4.4`/§9 rule — "no field is named
`diagnostic`" for anything that must be filterable — already anticipates
exactly this split (§7's `engine_metadata` rule 1, "declare before
use"): an engine with a closed enum can DECLARE a `refusal_reason`
pattern-scoped `enum` pair read structurally; an engine with free text
only cannot, and the capability set's per-pattern REQUIRES tag (declared
in the sub-bench sidecar, per §7 below) is what stands in for a
structural signal Hyperscan/perl never give the harness.

## 4. Size/complexity limits that refuse a pattern — the space-vs-speed dials

Every engine below exposes at least one knob that trades emitted-artifact
size or compile-time work against match speed, mirroring what
`testees/pcrec/list_axes.tsv`/`CLAUDE.md` already call pcrec's own
[ART-SIZE]/[LIM-1]/[LIM-2] caps. Proposed NAMED representative configs
per engine follow the bench's own config-slug idiom (`testees/pcrec/
CLAUDE.md`'s table: `<engine>-<axis-word>`).

| engine | the dial | default | what it trades | proposed configs |
|---|---|---|---|---|
| pcre2 | `pcre2_jit_compile()` vs none; `pcre2_dfa_match()` vs `pcre2_match()`; `pcre2_set_match_limit()`/`set_depth_limit()` (already this project's `pcre2-interp`/`pcre2-jit`, `testees/pcre2/CLAUDE.md`) | interpreter, no JIT, PCRE2's built-in match/depth limits | JIT trades compile time for match speed (already measured in this project — `pcre2-jit` vs `pcre2-interp`); DFA-match trades captures away (see below) for a scan that "just once... scans the subject string" (fetched [pcre.org/current/doc/html/pcre2_dfa_match.html](https://www.pcre.org/current/doc/html/pcre2_dfa_match.html), 2026-09-12) and can find ALL matches at one starting point (`PCRE2_DFA_SHORTEST` chooses the shortest) — Note: `pcre2_dfa_match` restricts what may appear in a pattern (the man page says so without enumerating; my fetch could not extract the exact restricted-construct list — flagged §8) and does NOT support JIT at all (`pcre2jit` man page, this box, fetched via `man`: "JIT support applies only to the traditional Perl-compatible matching function. It does not apply when the DFA matching function is being used.") | `pcre2-interp`, `pcre2-jit` (existing); NEW: `pcre2-dfa` (a THIRD execution model on the same library — its own `automaton_class: dfa-only`-ish reading is actually WRONG per `record_schema.md §5`'s enum, since `pcre2_dfa_match` is NOT a classical DFA — see the caveat below) |
| RE2 | `RE2::Options::max_mem` (default `8<<20` = 8 MiB, fetched from `re2.h` verbatim, 2026-09-12: "two-thirds to the forward Prog, one-third to reverse Prog... Once a DFA fills its budget, it flushes its cache and restarts. Excessive flushing causes fallback to NFA") | 8 MiB | memory ceiling on the compiled program AND the runtime DFA cache combined — RAISING it is the "space" dial in reverse (more memory buys fewer DFA cache flushes, i.e. speed); `longest_match` trades POSIX correctness for... a different correctness, not speed | `re2-default` (8 MiB), `re2-bigmem` (e.g. 64 MiB, mirroring this project's own `pcrec-*-bigcap` precedent at `testees/pcrec/CLAUDE.md`), `re2-longest` (POSIX mode) |
| Rust `regex` | `size_limit` (compile-time; default per the crate's own words "some reasonable number that permits most patterns to compile successfully" — an UNSPECIFIED-in-docs literal default I could not pin down exactly in this session, flagged §8) and `dfa_size_limit` (runtime lazy-DFA cache; exceeding it does NOT error — the engine "bails out... and switches to a different regex engine" per the crate docs, i.e. a GRACEFUL internal fallback, never a `did-not-compile`) | as above | `size_limit` is a hard compile-time refusal (`CompiledTooBig`); `dfa_size_limit` is a runtime engine-selection dial INVISIBLE to the compile outcome — this is a genuinely different shape from pcrec's own caps (which refuse at compile) and from RE2's (which degrades silently at MATCH time by flushing) — a third distinct "what does exceeding this even mean" shape for the capability model (§7) | `regex-default`, `regex-smallsize` (a LOW `size_limit` deliberately, to exercise the refusal outcome on the wide-alternation-style patterns this bench already has in `bench/altwide`) |
| Oniguruma | no documented global memory cap function surfaced in this session's fetch (`doc/API`, fetched: option flags only, no `onig_set_...limit`-shaped function found) — flagged §8, needs a second pass reading `doc/API` in full rather than the search-result excerpt this session captured | — | — | not yet proposable without the follow-up read |
| TRE | none surfaced beyond its own fixed internal working-space bound (the ~50K/20K/2K figures quoted in §1, which read as an implementation ceiling, not a caller-facing dial) | — | — | `tre-default` only, pending the same follow-up |
| Vectorscan/Hyperscan | `hs_compile` mode (`HS_MODE_BLOCK` / `HS_MODE_STREAM` / `HS_MODE_VECTORED`, fetched [intel.github.io/hyperscan/dev-reference/compilation.html](https://intel.github.io/hyperscan/dev-reference/compilation.html), 2026-09-12) and per-pattern `HS_FLAG_SOM_LEFTMOST` (start-of-match tracking, which has a documented COST: "specifying a small or medium SOM horizon will usually reduce the stream state required" — so SOM precision is itself a size/speed dial); database size is measurable via `hs_database_size`/`hs_serialized_database_size` (fetched, 2026-09-12) | BLOCK mode, no SOM | BLOCK trades nothing extra (one-shot scan of a whole buffer, closest to this bench's "search"/"match" regimes); STREAM trades per-call state for the ability to scan across call boundaries (irrelevant to this bench's batched-in-memory subjects — recommend BLOCK only for v1); SOM_LEFTMOST trades stream-state memory (and, per Hyperscan's own doc, compatibility — it cannot combine with `HS_FLAG_SINGLEMATCH`/`HS_FLAG_PREFILTER`) for start-offset precision, which THIS BENCH NEEDS (`adapters.py`'s `subject` line always reports a `START`, `adapters.py:54`) — so a Hyperscan testee MUST compile with `HS_FLAG_SOM_LEFTMOST` to answer this bench's own protocol at all, which is itself a "space" cost paid unconditionally, not a dial | `vectorscan-block-som` (mandatory for start-offset reporting), `vectorscan-block-nosom` (a declared-variant testee that can only report END offsets and match/no-match, NOT start — an honest capability gap, not a config choice; see §7) |
| python `re` | `re` module has no documented size cap exposed to callers (CPython's own recursion-limit interacts with pathological backtracking instead — an unbounded-time hazard, not a compile-time refusal) | — | n/a — python `re` cannot decline a pattern for size; it can only hang or raise `RecursionError` at MATCH time, which the bench's per-subject `timed-out`/`crashed` outcomes already cover (`requirements.md §4.4`) | `python-re` (one config; no space/speed axis to name) |
| perl | perl's regex engine has its own internal limits (`$Config{...}`-adjacent build-time constants) not surveyed in this session — flagged §8 | — | — | `perl-default` pending follow-up |
| pcrec | already fully mapped by this project: `max_emit_bytes`/`max_emit_code_bytes` (the [ART-SIZE] caps), `--engine=auto/dfa/vm`, `unroll_k` (`docs/design/record_schema.md §7`'s worked pcrec table) | as `testees/pcrec/configs.toml` states per config | already this project's own knowledge, not re-derived here | the sixteen configs already in `testees/pcrec/CLAUDE.md` |

**A caveat on `pcre2_dfa_match`'s automaton_class tag.** The man page
name ("DFA") is misleading for this bench's `automaton_class` enum
(`record_schema.md §5`: `dfa-only`/`nfa-simulation`/`backtracking`/
`hybrid`/`simd-multipattern`). `pcre2_dfa_match` finds ALL matches
starting at one position simultaneously by simulating an NFA-like state
set across the subject in one left-to-right scan (my fetch of
`pcre2_dfa_match.html` could not confirm from the page text alone
whether it is a literal subset-construction DFA or an NFA simulation
that behaves like one — flagged §8, worth a source read of pcre2's
`pcre2_dfa_match.c` before the design note commits to a tag). What IS
confirmed: it reports overlapping matches at one start point (a genuinely
different QUESTION from `pcre2_match`'s single best match), takes a
caller-provided `workspace` array sized independent of capture-group
count, and CANNOT be JIT-compiled (confirmed from this box's `man
pcre2jit`, quoted above) — three structural facts, independent of the
DFA-vs-NFA-simulation label, that already argue for treating it as a
FOURTH pcre2 testee (`pcre2-dfa`) with its own `automaton_class` value
pending that source read.

## 5. What "compile time" means per engine, and what is comparable

`requirements.md §3` already rules the shape: compile/setup cost is its
own axis, defined PER EXECUTION-MODEL CLASS, never folded across classes;
`record_schema.md`'s compile-row field table encodes this as `cost_class`
(MUST equal `setup.testee.execution_model`) and `cost.phases[]` (named,
ordered per testee). `testees/pcre2/CLAUDE.md` and `testees/pcrec/
CLAUDE.md` already show the pattern for two classes. Extending it:

| engine | execution_model | phases (proposed) | what is comparable | what is NOT |
|---|---|---|---|---|
| pcre2-interp | `interpretive` | `compile` | across every `interpretive` testee | vs anything eager/lazy/AOT |
| pcre2-jit | `eager-jit` | `compile`, `jit-compile` | across `eager-jit` testees (the existing rule) | vs interp/lazy/AOT |
| pcre2-dfa (proposed) | `interpretive` (it is `pcre2_compile` only — no separate DFA-match-specific compile step exists; `pcre2_dfa_match` reuses the SAME compiled pattern `pcre2_match` would use) | `compile` | with `pcre2-interp` on COMPILE cost (byte-identical compiled pattern, so the compile-cost number SHOULD be statistically the same testee-to-testee — a control this bench can check for free) | its MATCH-time behaviour, which answers a different question entirely (§4) |
| RE2 | `compiled-aot`-ADJACENT but not AOT in pcrec's sense — RE2 compiles a `Prog` (its own bytecode) at CONSTRUCTION time (`RE2 re(pattern, options)`), and the DFA states are built LAZILY at first match, cached, and can be flushed/rebuilt mid-run (per `max_mem`, §4) — this is closer to `eager-jit`'s shape (an explicit, timeable construction call) EXCEPT that "the DFA graphs" a match pays for are not fully built at construction, so `RE2::ProgramSize()` (fetched from `re2.h`: "a very approximate measure of a regexp's cost", `ReverseProgramSize()` too) measures the FORWARD/REVERSE PROGRAM, not the runtime DFA. Recommend: `execution_model = eager-jit` is the closest existing token (an explicit, separately-timeable construction call, the eager-JIT definition's own test in `requirements.md §3`), stated with a NOTE that RE2's runtime DFA cache is a SEPARATE, match-time-amortized cost this bench's compile axis does not capture — closer to how pcrec's own `dfa_prefilter` mechanism stamps are read as MECHANISM, not COST | `RE2::RE2()` construction call, timed | across other `eager-jit`-labelled testees ONLY WITH THE CAVEAT ABOVE STATED IN THE REPORT, same posture as `requirements.md §3`'s "reports never reduce compile costs of different classes into one cell without labelling the class" — this is a NEW sub-case: same class token, different cost SHAPE, and I recommend the design note propose an explicit caveat field or a documented class footnote rather than silently pooling | vs pcre2-jit's number at face value without that caveat |
| Rust `regex` | `RegexBuilder::build()` is one explicit call analogous to RE2's construction — `eager-jit`-adjacent by the same argument, with the SAME caveat: the lazy DFA (`dfa_size_limit`-governed) is built incrementally at match time, and the crate's own "one-pass" / "backtrack" / "PikeVM" / "bounded backtracker" internal engine SELECTION happens per-match, not at `build()` — so `regex::Regex::new()`'s timed cost measures PARSING + AST + HIR + the literal/prefilter analysis, not "the automaton", a genuinely different quantity from pcrec's AOT compile or pcre2's JIT compile | `compile` (the one call) | across other Rust-regex testees | vs any engine whose compile step DOES build the runtime automaton eagerly (pcrec, RE2's Prog construction is closer but still not exact) |
| Oniguruma | `onig_new()` is one explicit, synchronous, eagerly-building call (Oniguruma's compile step DOES build its full internal program, unlike RE2/Rust's lazy-DFA story) | `compile` | `eager-jit`... except Oniguruma has NO JIT at all — it is closer to pcre2-interp's `interpretive` shape: one eager, non-JIT compile call whose output IS the whole program | Recommend `execution_model = interpretive` for Oniguruma, matching pcre2-interp's own definition exactly (`testees/pcre2/CLAUDE.md`: "one phase... timed in-driver") |
| TRE | `regcomp()`/`tre_regcomp()` — same shape as Oniguruma: one eager call | `compile` | `interpretive` | — |
| Vectorscan/Hyperscan | `hs_compile()` is EXPLICITLY documented as the heavyweight, famously-slow-relative-to-match-speed step (this is Hyperscan's own well-known engineering tradeoff — a huge compile-time investment for fast scanning, the origin of Hyperscan's own recommendation to compile once, scan many times); this is `compiled-aot`-shaped in SPIRIT (heavy, explicit, front-loaded) though it emits an in-memory database rather than machine code via a real compiler+linker the way pcrec does | `compile` (one call; NOT split into further named phases the way pcrec's `emit-c`/`gcc`/`load` are, since Hyperscan's compiler is monolithic from the caller's point of view) | across other Hyperscan/Vectorscan testees | vs pcrec's own AOT phases, which have compiler+linker phases Hyperscan simply does not expose — recommend `execution_model = eager-jit` (closest existing token: one explicit, timeable call that produces a ready-to-run artifact) with the SAME class-footnote caveat as RE2/Rust above |
| python `re` | `re.compile()` — CPython caches compiled patterns internally (an LRU cache keyed on pattern text + flags) that this bench's own batched-loop driver would need to bypass explicitly (`re.compile` outside the cache, or `re._cache.clear()` before each trial) to get an honest first-compile number — a driver-writing gotcha worth stating up front | `compile` | `interpretive`, same class as pcre2-interp/Oniguruma/TRE | — |
| perl | `qr/.../ ` compiles a pattern into a `Regexp` object; perl ALSO caches compiled patterns per-literal-pattern-occurrence in a program (`qr//`'s own doc-stated behaviour), a similar bypass concern to python's | `compile` | `interpretive` | — |
| pcrec | already fully specified: `compiled-aot`, phases `emit-c`, `gcc`/`clang`, `load` (`testees/pcrec/adapter.py`, per `testees/pcrec/CLAUDE.md`) | `emit-c`, `gcc`, `load` | across pcrec configs only | vs every other engine's compile axis, unconditionally |

**The recurring finding.** Only pcrec (AOT, a real compiler+linker) and
pcre2-jit (an EXPLICIT separate JIT call over an already-compiled
pattern) have compile-cost definitions this project's existing
`cost_class` enum captures CLEANLY. RE2, Rust `regex`, and Hyperscan all
have a construction/compile call that is EXPENSIVE and TIMEABLE but does
NOT build the full runtime automaton (RE2/Rust's lazy DFA is built
incrementally during matching; Hyperscan's database IS fully built at
compile time, which makes it the cleanest `eager-jit` fit of the three).
This is not a gap in this bench's schema so much as an under-specified
CORNER of `cost_class`'s four tokens: the schema's four values
(`interpretive`/`compiled-aot`/`eager-jit`/`lazy-jit`) were defined
against pcrec+pcre2 (`requirements.md §3`'s four bullet points cite
exactly those two engines' shapes) and the roster now has THREE new
engines whose compile step is eager-but-partial. **I recommend the
design note propose EITHER a fifth class token (something like
`eager-with-lazy-runtime`) OR keep `eager-jit` and require every such
testee's adapter note to state explicitly, in prose, what the timed call
does and does not build** — the second choice costs nothing schema-wise
and matches this project's existing practice of adapter CLAUDE.md notes
carrying exactly this kind of caveat (`testees/pcre2/CLAUDE.md`'s
`consumed_length` paragraph is the precedent: a plain-English convention
statement rather than a new enum value, for a fact that is testee-specific
rather than universally structural).

**Artifact/program size** — every engine on the roster CAN expose a
number here, none uniformly comparable, matching `requirements.md §3`'s
"deferred, recorded if free but not scored": pcre2 `pcre2_pattern_info`
`PCRE2_INFO_SIZE` (already this project's `compiled_size_bytes`, `testees/
pcre2/CLAUDE.md`) and `PCRE2_INFO_JITSIZE`; RE2 `ProgramSize()`/
`ReverseProgramSize()` (fetched, §1); Hyperscan `hs_database_size()`/
`hs_serialized_database_size()` (fetched, §4); Rust regex has no public
"give me the compiled size in bytes" call surfaced in this session's docs
fetch (flagged §8 — `regex_automata`'s lower-level crate may expose more);
Oniguruma/TRE not surveyed for a size accessor in this session (flagged
§8); pcrec's `emit_bytes`/`emit_code_bytes`/`artifact_bytes` already
exist (`record_schema.md §7`). All are DIFFERENT DEFINITIONS of "size" —
a compiled bytecode program (RE2, PCRE2), a relocatable database blob
(Hyperscan), or comment-excluded generated C source plus a linked `.so`
(pcrec) — recorded per `requirements.md §3` but NOT pooled into one
column without a stated caveat, same posture as compile time itself.

**Peak memory** is the metric this note is LEAST able to promise
apples-to-apples, and says so plainly: the honest answer is `rusage`
`ru_maxrss` of the DRIVER PROCESS around a compile-then-match cell, which
measures the whole process (allocator overhead, the harness's own
buffers, any interpreter startup for python/perl) rather than the
engine's own allocation — not uniform across a scripting-language driver
vs a native one, and pcrec's AOT artifacts do not "allocate" in the
usual sense at all (they are `dlopen`ed code + a caller `mmap`, closer to
zero dynamic allocation at compile time by design). Recommend: record
`ru_maxrss` when free (matching `requirements.md §3`'s "recorded if
free but not scored"), state per testee-class whether it is
MEANINGFUL, and never rank on it.

## 6. The syntactic-adjustment question — spelling tables and how equivalence is checked

`requirements.md §4.5` already states the two constraints a variant must
satisfy (identical results on every subject; the sub-bench's objective
preserved) and that this is CHECKED against the canonical PCRE2-oracled
expectations, never approximated. A per-engine SPELLING table is the
right shape; below are the rewrites this session could confirm are
semantics-preserving, engine by engine, plus where a rewrite CANNOT be
made and the pattern must instead be `unsupported-by-declaration`.

| rewrite | engines it targets | semantics-preserving? | how equivalence is checked |
|---|---|---|---|
| `\d`/`\w`/`\s` (Unicode-aware under pcre2 `PCRE2_UCP`) → `[0-9]`/`[A-Za-z0-9_]`/`[ \t\n\r\f\v]` (ASCII) | any engine whose default `\d` scope diverges from pcre2's compiled options (RE2 is ASCII by default for these classes even with UTF-8 encoding enabled — its Unicode support is via explicit `\p{...}`, not by widening `\d`) | preserving ONLY if the CANONICAL pattern's own compile options did not request `PCRE2_UCP` in the first place (checked against the sub-bench's own runtime-options declaration, `requirements.md §4.3`'s "runtime compile options... distinct from build flags"); if the canonical pattern DOES rely on Unicode-`\d`, this rewrite changes the answer set on any non-ASCII digit subject and is NOT a variant — the pattern is `unsupported-by-declaration` for an ASCII-`\d`-only engine unless the sub-bench supplies ASCII-only subjects for that case | oracle every rewritten pattern against EVERY subject the canonical pattern is measured on, per `requirements.md §4.5` constraint 1 — no partial credit |
| possessive quantifier `x*+`/`x++` → drop the possessive suffix (`x*`) | RE2, Rust regex, Hyperscan, TRE (all lack possessive quantifiers outright) | preserving ONLY when the possessive suffix in the CANONICAL pattern was decorative (no catastrophic-backtracking hazard it exists to prevent) — and `requirements.md §4.5` constraint 2 is the sharper test here: **a possessive quantifier in a hazard-class pattern (`hazard_class: exponential-backtracking`) exists SPECIFICALLY to demonstrate the engine's own defence against catastrophic backtracking; dropping it on an engine that has no backtracking to defend against in the first place is not a rewrite that "preserves the objective" — it is the objective ITSELF being answered by construction (RE2/Rust/Hyperscan cannot backtrack catastrophically, possessive or not), which argues these patterns should be `unsupported-by-declaration` (the possessive suffix is unsupported SYNTAX) rather than silently rewritten, so the report can say "this engine structurally cannot exhibit this hazard" instead of implying it was tested and passed | oracle-check the rewritten pattern on non-hazard subjects only if the sub-bench declares the possessive suffix non-essential there; otherwise refuse the variant outright |
| atomic group `(?>...)` → plain group `(?:...)` | RE2, Rust regex, Hyperscan, TRE | same reasoning as possessive quantifiers — an atomic group is ALSO a backtracking-control construct, and the objective-preservation question is identical | as above |
| `(?i)` inline flag placement | Oniguruma, TRE, python, perl all accept `(?i)` at pattern start identically to pcre2; RE2 accepts `(?i)` too (RE2's flag syntax closely tracks PCRE's for the flags it does support) | preserving — a genuine syntax-only rewrite in the RARE case an engine's inline-flag placement rules differ (mid-pattern scoped flags `(?i:...)` vs whole-pattern) | token-by-token review (`requirements.md §4.5`'s `syntax-only` kind: "a mechanical re-spelling a reviewer can check token by token") suffices; still oracle-run because inline-flag SCOPE bugs are a real, observed class of engine divergence |
| `\h` (horizontal whitespace, a pcre2/Perl extension) → `[ \t]` (or the fuller `[\t\x{09}...]` set pcre2's own docs define) | RE2, Rust regex (no `\h` token), TRE, Oniguruma (support varies by syntax profile) | preserving if the sub-bench's subjects never exercise the FULL horizontal-whitespace set pcre2's `\h` matches (it is wider than `[ \t]` — includes several Unicode space separators under UCP) — the same "check against canonical options" logic as `\d` above | oracle-check; flag as a `restructured` (not `syntax-only`) kind if the ASCII-only version's answer set could plausibly diverge on some未-included subject even if it does not diverge on THIS sub-bench's actual subjects, per `requirements.md §4.5`'s kind field being "informational only" |
| POSIX bracket classes `[:alpha:]`/`[:digit:]` | supported essentially identically across pcre2, RE2, Oniguruma, TRE (TRE is POSIX-native, this is its home dialect), Hyperscan (documented support), python, perl | preserving — near-universal, low-risk rewrite | still oracle-checked as a matter of policy (constraint 1 has no low-risk exemption) |
| `\z` (true end) vs `$` (end, or before final `\n`) | this project's OWN existing convention (`record_schema.md §5` ADDITIONS 3, quoted in full above) already states the hazard for pcre2/pcrec's whole-subject form; RE2 supports `\z`/`\A` identically to PCRE2's meaning; Rust regex supports `\z`... only in "insensitive to `(?m)`" byte-anchor form once `(?s)`-equivalent multiline handling is considered (Rust regex's own docs distinguish `\z` "end of haystack" from `$` under multi_line — same shape of hazard as pcre2's, so the SAME rewrite is needed, not a new problem); Oniguruma/TRE/Hyperscan not independently confirmed for `\z` support in this session (flagged §8) | this is not really a rewrite so much as this project's OWN existing whole-subject-form convention travelling to every new engine's adapter — recommend restating record_schema.md §5 ADDITIONS 3's rule as a REQUIREMENT ON EVERY NEW ADAPTER rather than re-deriving it per engine | already this project's own checked convention; extend the SAME check (`\z` never `$`, `(?:...)` wrap around any top-level alternation) to every new adapter's whole-subject form |

**Where a rewrite is definitively NOT semantics-preserving and the
pattern must be `unsupported-by-declaration`:** any pattern whose
canonical text uses a backreference, lookaround, recursion, a
conditional, or `\K` on RE2/Rust regex/Hyperscan — there is no rewrite
that preserves the construct's OWN meaning (a backreference is not
approximable by a non-backtracking automaton by definition; this is the
well-known reason RE2 exists at all). The capability set should expect a
LARGE `unsupported-by-declaration` share for these three engines on any
sub-bench whose objective IS one of those constructs (this project's own
`bench/syntax@0.1` census — 95 patterns, 18 mechanism families,
`docs/design/CLAUDE.md`'s note on it — already names several such
families), which is the correct, honest outcome per `requirements.md
§4.5` constraint 2, not a gap to paper over.

## 7. A proposed capability model for the record/reporter

Building on `record_schema.md §5`'s existing `compile_outcome` enum
(`compiled`/`did-not-compile`/`crashed`/`timed-out`/
`unsupported-by-declaration`) and §4.4's per-subject `match_outcome` set,
this note's finding is that the SET IS ALREADY WIDE ENOUGH for the
roster's compile-time refusals (§3's table shows every engine's refusal
lands cleanly on `did-not-compile`, with `diagnostic` carrying whatever
structure the engine gives — enum name, error code, or free text) and for
`unsupported-by-declaration` (the sub-bench's own engine notes, exactly
as designed). What is NOT yet covered, from this session's survey:

1. **A refusal that is a SIZE/LIMIT decline specifically**, distinct from
   a syntax refusal. RE2's `max_mem` flush-and-restart is INVISIBLE at
   compile time (a match-time behaviour, not a `compile_outcome` at
   all); Rust regex's `CompiledTooBig` IS a compile-time refusal with a
   STRUCTURED size figure attached. Recommend: `did-not-compile` stays
   the outcome (no new enum value needed — this mirrors pcrec's own
   size-cap refusal, already `did-not-compile` per this project's
   existing practice), but the compile row's `engine_metadata` should
   carry a `refusal_class: syntax | size-limit | resource-limit` pattern-
   scoped pair PER ENGINE THAT CAN DISTINGUISH THE TWO (RE2's `ErrorCode`
   enum already separates `ErrorRepeatSize`/`ErrorPatternTooLarge` from
   the syntax errors; Rust's `CompiledTooBig` vs `Syntax` is the same
   split) — an engine whose refusal is free text only (Hyperscan, perl)
   cannot populate this pair honestly and should not guess.
2. **A refusal that is a graceful runtime DEGRADE, not a compile-time
   event at all** (RE2's DFA-cache flush-and-restart under `max_mem`
   pressure; Rust's `dfa_size_limit` engine-switch). Neither is an
   OUTCOME in this schema's current sense — both are MECHANISM, the
   `engine_metadata` map's own territory (`record_schema.md §7`), not
   the outcome axis. Recommend NO new outcome value; recommend a
   `match`-scoped `engine_metadata` pair on the affected engines
   (`dfa_cache_flushed: yes/no` for RE2, an analogous pair for Rust) —
   this is exactly `requirements.md §4.2`'s "bucket outliers by
   MECHANISM" purpose, applied to a mechanism this roster is new.
3. **Hyperscan's all-ends semantics genuinely does not fit the
   `matched-as-expected` single-answer shape.** Recommend the capability
   set's Hyperscan/Vectorscan testee run under a DECLARED VARIANT whose
   expectation is restated as a SET of end-offsets (a `capture_
   correspondence`-shaped mechanism, `record_schema.md §5`'s
   `capture_correspondence.mode` enum, extended in spirit rather than in
   the literal field) — or, more conservatively for a v1 capability set,
   Hyperscan/Vectorscan is measured ONLY on subjects/patterns whose
   canonical expectation already IS "does this match anywhere" (a single
   boolean, no span needed) plus compile-time/refusal comparisons, with
   `requirements.md §4.5`'s "results must be identical on every subject"
   constraint read at the BOOLEAN grain rather than the span grain for
   this engine alone — a decision Frank should rule on explicitly (§8's
   question 4), since it is a real narrowing of what "identical results"
   means for one engine only.
4. **An engine that ran a rewritten spelling must never rank invisibly
   beside one that ran the canonical text.** This is ALREADY `requirements.
   md §4.5`'s closing sentence ("Reports show the variant kind beside the
   number") and `record_schema.md`'s `variant.kind` field
   (`syntax-only`/`restructured`) — no new schema needed, just a
   reminder that the capability set will exercise this machinery far
   more heavily than any existing sub-bench has (most current
   sub-benches run zero or few declared variants; this one will run
   MANY, per §6's tables), so the REPORTER's variant-kind rendering
   (already built, per `pcrecbench/CLAUDE.md`'s reporter history) needs
   to be checked against a report with a dozen-plus variant rows in one
   table before this set ships, not assumed to scale from today's
   handful.
5. **Per-pattern REQUIRES tags**, derived directly from §3's table:
   `backrefs`, `lookaround`, `atomic-possessive`, `recursion`,
   `conditionals`, `k-reset`, `unicode-properties`,
   `variable-length-lookbehind` (python's own specific gap), `all-ends-
   semantics` (Hyperscan's own specific shape). A sub-bench's sidecar
   declares which tags a pattern requires (extending the sidecar fields
   `docs/design/subbench_directory_model.md` already describes — this
   note does not re-derive that file's own findings, it is [B42]'s
   THIRD research lane's territory); an engine's adapter declares which
   tags it satisfies; a pattern whose REQUIRES set is not a subset of an
   engine's declared capability is `unsupported-by-declaration` BEFORE
   the harness even attempts a compile — turning §3's whole table into
   executable policy rather than prose a reviewer re-checks by hand
   every time the roster grows.

## 8. Questions for Frank, and what I could not verify

Every item below is flagged inline above at its first occurrence; listed
together here for the design pass.

1. **Is `rure`/`regex-capi` still a maintained, buildable C API for the
   Rust `regex` crate as of this pin (1.12.2), or has it been supplanted
   by something else (e.g. a `cbindgen`-generated header the design note
   would need to build itself)?** I confirmed the source tree still
   exists in `rust-lang/regex` on GitHub and found no removal
   announcement, but could not confirm from crates.io whether a current
   `rure` release exists or whether `regex-capi` still builds against
   `regex` 1.12 without patching (its own `Cargo.toml` version pin was
   not checked). Needs a build attempt, not another search.
2. **`pcre2_dfa_match`'s restricted-construct list and its true
   automaton class** — the man page states restrictions exist without
   naming them in the portion this session fetched; recommend reading
   `pcre2_dfa_match.c`'s own top-of-file comment (pcre2 is BSD, freely
   readable; the `.h`/`.c` are on this box under `libpcre2-dev`) before
   the design note commits to `pcre2-dfa` as a fourth testee or picks its
   `automaton_class` tag.
3. **Oniguruma's and TRE's own size/complexity refusal surfaces** — I did
   not find a documented memory-cap function for Oniguruma in this
   session's fetch of `doc/API`, and TRE's own internal bound (§1's
   ~50K/20K/2K figures) has no named error code I could confirm hits it.
   Both need a second, deeper read of `doc/API` (Oniguruma) and
   `tre.h`/`regcomp.c` (TRE) rather than a search-engine excerpt.
4. **Frank's ruling on Hyperscan's all-ends semantics (§7 item 3)**: does
   the capability set measure Hyperscan/Vectorscan at the SPAN grain via
   a declared variant restating expectations as end-offset sets, or at a
   narrowed BOOLEAN grain for this engine only? This is a real, visible
   choice about what "the same sub-bench" means across the roster, not a
   detail a lane should decide alone.
5. **The `cost_class` fifth-token question (§5)**: add a new
   `eager-with-lazy-runtime` (or similar) token to the schema's
   `execution_model`/`cost_class` enum for RE2/Rust-regex/Hyperscan's
   shared shape, or keep `eager-jit` and rely on adapter-note prose (this
   note's own recommendation is the latter — cheaper, consistent with
   existing practice — but it is Frank's or the design note's call, not
   assumed here).
6. **Whether python `re` and perl are in scope for MATCH timing at all
   in a v1 capability set**, given §1's finding that neither fits the
   driver protocol without an embedding driver (a real, nontrivial build
   — `Py_Initialize`/`libperl` linkage — that would be its own lane).
   This note recommends compile-cost-and-correctness-only for both in
   v1, with match `regime` coverage explicitly marked partial, but that
   is a scope call for the design note and Frank, not settled here.
7. **Peak memory (§5's close)**: is `ru_maxrss` of the driver process
   worth recording at all given how little it isolates the engine's own
   allocation from interpreter/harness overhead on the scripting-language
   testees — or is it worth recording for the NATIVE-driver testees only
   (pcre2, RE2, Rust, Oniguruma, TRE, Hyperscan, pcrec) and explicitly
   never for python/perl?

Sources consulted, all fetched or probed 2026-09-12 unless a path is
given (this repository's own files, read in full or in the cited
sections, not re-cited per line below):

- [github.com/google/re2](https://github.com/google/re2) and
  [github.com/google/re2/wiki/Syntax](https://github.com/google/re2/wiki/Syntax)
- [raw.githubusercontent.com/google/re2/main/re2/re2.h](https://raw.githubusercontent.com/google/re2/main/re2/re2.h)
- [marcomaggi.github.io/docs/cre2.html/options.html](http://marcomaggi.github.io/docs/cre2.html/options.html) and [github.com/marcomaggi/cre2](https://github.com/marcomaggi/cre2)
- [docs.rs/regex/latest/regex/struct.RegexBuilder.html](https://docs.rs/regex/latest/regex/struct.RegexBuilder.html)
- [docs.rs/regex/latest/regex/enum.Error.html](https://docs.rs/regex/latest/regex/enum.Error.html)
- [github.com/rust-lang/regex/tree/master/regex-capi](https://github.com/rust-lang/regex/tree/master/regex-capi)
- [intel.github.io/hyperscan/dev-reference/compilation.html](https://intel.github.io/hyperscan/dev-reference/compilation.html)
- [intel.github.io/hyperscan/dev-reference/api_files.html](https://intel.github.io/hyperscan/dev-reference/api_files.html)
- [github.com/VectorCamp/vectorscan](https://github.com/VectorCamp/vectorscan)
- [github.com/kkos/oniguruma/blob/master/doc/API](https://github.com/kkos/oniguruma/blob/master/doc/API)
- [laurikari.net/tre/documentation/regcomp](https://laurikari.net/tre/documentation/regcomp/) and [laurikari.net/tre/documentation/](https://laurikari.net/tre/documentation/)
- [github.com/laurikari/tre](https://github.com/laurikari/tre/)
- [pcre.org/current/doc/html/pcre2_dfa_match.html](https://www.pcre.org/current/doc/html/pcre2_dfa_match.html)
- this box's `man pcre2jit` (`libpcre2-dev` 10.46-1build1, installed)
- [pcre2project.github.io/pcre2/project/licence](https://pcre2project.github.io/pcre2/project/licence/)
- [docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html), [regular-expressions.info/python.html](https://www.regular-expressions.info/python.html), [learnbyexample.github.io/python-regex-possessive-quantifier](https://learnbyexample.github.io/python-regex-possessive-quantifier/)
- this box's `apt-cache policy`/`apt-cache search`/`apt-cache show`/`pkg-config --list-all` (2026-09-12, archive suite `resolute`)
- this project: `APPROACH.md`, `docs/design/requirements.md`,
  `docs/design/record_schema.md`, `pcrecbench/adapters.py`,
  `testees/pcre2/CLAUDE.md`, `testees/pcrec/CLAUDE.md`,
  `testees/CLAUDE.md`, `docs/dev/plan.md` ([B42], [B7] rows)
