# testees/rust/ — the rust-regex adapter

[B7]/L6b, lane `l6brust`, chartered 2026-09-19 — the LAST unchartered
engine on `docs/design/capability_set_v1.md`'s roster (the wave that
already landed RE2, Oniguruma, TRE and Vectorscan the same week). Provides
one testee: **`rust-default`** (`RegexBuilder` at the crate's own
documented defaults). `rust-smallsize` (a LOW `size_limit`, exercising
`CompiledTooBig` as a first-class refusal — capability_set_v1.md §8's
`regex-smallsize` roster row) is **not built**; this lane's brief named
`rust-default` first, "more only if the census motivates and the roster
doc's composition rule covers it" — no census has run yet (below).

**STATUS: BUILT AND CENSUSED** (lane `l6brustfin`, 2026-09-19, the
detached post-battery pipeline that ran the moment pcrec's I-75 battery
cleared — `docs/dev/lanes/l6brust_report.md` is the authoring half's own
account; `l6brustfin`'s own report has the finishing half). `Cargo.lock`
is committed (regex 1.13.1); every "SATISFIED"/"REFUSED"/"WITHHELD" line
below is a WITNESSED finding, cited to
`docs/dev/measurements/2026-09-19-rust-capability-census-r1131.txt`
(the real compile/match census through the real adapter), never a
prediction.

| file | role |
|---|---|
| `Cargo.toml` | the driver crate manifest; `regex = "1"` (a semver requirement — the PIN is `Cargo.lock`, generated at the first build and committed) |
| `Cargo.lock` | GENERATED and COMMITTED (the first `cargo build --release`, 2026-09-19): `regex 1.13.1`, `regex-automata 0.4.18`, `regex-syntax 0.8.11`, `aho-corasick 1.1.5`, `memchr 2.8.3` |
| `src/main.rs` | the native Rust driver (the protocol is in `pcrecbench/adapters.py`) |
| `adapter.py` | `describe`/`prepare`/`compile`/`measure`; version probing from the committed `Cargo.lock` + a live `rustc --version`; the `\A(?:...)\z` whole-subject wrap |
| `configs.toml` | the one config id, `rust-default` |

## Naming: `rust-default`, not `regex-default`

`capability_set_v1.md` §8's roster table names this row `regex-default`
(the CRATE's name). This directory follows `testees/CLAUDE.md`'s own
per-directory convention instead — every existing L6b testee prefixes
with its DIRECTORY name (`re2-default`, `onig-default`, `tre-default`,
`vectorscan-block-nosom`), and this lane's brief said so explicitly
("One config `rust-default` first"). `engine_name` in every record is
`"rust"` (the directory/adapter name — record_schema.md §6.4's own
composition rule keys on `engine_name`, not on the crate name), so a
`testee_id` reads `rust_<regex-crate-version>_default-caps-simdna`.

## Toolchain pin (inbox I-76, pcrecdev1's ruling, quoted in full)

> Ruling: rustup, the `stable` channel as it resolves at charter time,
> pinned by exact rustc/cargo version in the testee's CLAUDE.md like
> every other engine; the regex crate from crates.io at a pinned version
> with Cargo.lock committed; vendor only on a measured reproducibility
> need. Box constraints only: install under duxevents' home (no sudo),
> and watch disk — rustup + cargo caches are large (root ~94% on
> 2026-09-11, 69% at 08:41 today); keep the target dir prunable. No
> "cargo install line" concern exists on our side.

**pcrec has no stake in this decision** (I-76's own opening line) — Rust
dependencies live entirely on the bench side; pcrec is C + gcc only.

**Exact versions, PROBED live at the first (and every subsequent) build,
never typed:**

- `rustc --version`: **`rustc 1.98.1 (48a229cea 2026-09-01)`** (probed
  live by `adapter.py`'s `_probe_rustc_version()` at every `describe()`
  call — never hand-typed, same discipline `testees/CLAUDE.md`'s "one
  rule that is not obvious" states for every other engine)
- `cargo --version`: **`cargo 1.98.1 (797e8a9bc 2026-08-05)`**
- `regex` crate version: **`1.13.1`** — read from the committed
  `Cargo.lock` by `adapter.py`'s `_read_cargo_lock_regex_version()`,
  never typed here either (this file states the MECHANISM, not a number
  that could drift out of sync with the lockfile; the lockfile also pins
  `regex-automata 0.4.18`, `regex-syntax 0.8.11`, `aho-corasick 1.1.5`,
  `memchr 2.8.3` — the crate's own dependency tree, unpinned by us)

**Install plan, RUN 2026-09-19** (HELD until pcrec's battery trailer at
`/home/duxevents/pcrec/build/battery_923a5a58/trailer.log` printed `==
BATTERY DONE` at 15:34:36 EDT; the detached pipeline `l6brust`'s own
session launched picked it up within 60 s):

    df -h /                                          # BEFORE
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \
        | sh -s -- -y --default-toolchain stable --profile minimal
    source "$HOME/.cargo/env"
    rustc --version; cargo --version                 # recorded above
    cd testees/rust && cargo build --release          # generated Cargo.lock
    df -h /                                           # AFTER first build
    git add Cargo.lock                                # committed the pin

No sudo anywhere (rustup installs entirely under `$HOME/.cargo` /
`$HOME/.rustup`); `--profile minimal` (no docs/clippy/rustfmt components)
kept the install small per I-76's disk-watch instruction. `df -h /`
**before install** (this lane, 2026-09-19 11:09 EDT): `30G avail, 69%
used` — matches I-76's own "69% at 08:41 today" figure. **`df -h /`
after the first build** (15:35 EDT, ~26 min later — the wait was pcrec's
battery, not the install): `28G avail, 71% used` — rustup + the release
build together cost ~1 GB. The first build (no `--locked`, which
GENERATED `Cargo.lock`) finished in 6.93 s release-optimized; every
subsequent `prepare_driver()` call passes `--locked` and enforces the
committed pin.

## (a) The compile-cost definition

**One phase, `compile`** — the `RegexBuilder::build()` call, timed
in-driver. `execution_model = "eager-jit"`, the SAME token and the SAME
caveat `testees/re2/CLAUDE.md` states for RE2 (capability_set_v1.md
§7.1/§7.2): this call parses the pattern and builds the HIR/literal-
prefilter analysis, but the crate's lazy DFA is built INCREMENTALLY at
match time and cached, never fully eagerly the way `pcre2-jit`'s
`pcre2_jit_compile` is. The reporter's §7.2 footnote fires automatically
on any report pooling this testee beside another `eager-jit` one whose
`compile_cost_definition` string differs.

`engine_metadata` (declared in `adapter.py`'s `METADATA_DECL`, pattern
scope): `ncapturegroups` (`Regex::captures_len() - 1`, group 0 excluded —
the same convention RE2/Oniguruma already use), `named_count`
(`Regex::capture_names()`'s `Some` count — Oniguruma's own `names` pair,
same shape). **No artifact/program size is reported.** Confirmed by
`docs/design/capability_set_v1.md` §7.3's own research finding before
this lane started: `regex_automata::meta::Regex::memory_usage()` exists
at the LOWER-LEVEL crate, but the higher-level `regex::Regex`/
`regex::bytes::Regex` type this driver uses has no such method — "N2 §5
(7), a CLOSED question, not an unfound one." Not re-litigated by this
lane; `testee.compile_cost_definition` does not claim a size this engine
cannot report.

## (b) `consumed_length`: the convention, stated plainly

**`consumed_length` is the subject length this driver passed and the
`regex` crate accepted — i.e. the whole subject.** `Regex::find`/
`captures`/`find_at` take an explicit `&[u8]` slice with no scan
high-water mark exposed — the SAME honest claim `testees/pcre2/CLAUDE.md`
and `testees/re2/CLAUDE.md` state for their own engines: *"no byte was
withheld or refused"*, never *"the engine looked at every byte"*.

## (c) The one config's exact option object

    RegexBuilder::new(pattern_str)
        .size_limit(10_485_760)       // 10 MiB, the crate's own documented default
        .dfa_size_limit(2_097_152)    // 2 MiB, ditto
        .build()

Unicode mode is left at its default (**on**) — needed for
`unicode-properties`; NOT explicitly toggled anywhere in this driver.
`size_limit`/`dfa_size_limit` are passed explicitly (`--size-limit`/
`--dfa-size-limit` CLI flags, `configs.toml`'s own keys) rather than left
implicit, so a future `rust-smallsize` config needs only a new
`configs.toml` row, no driver change.

**CONFIRMED against the actual pinned crate SOURCE** (never memory,
never docs.rs — the downloaded source at
`~/.cargo/registry/src/index.crates.io-*/regex-1.13.1/src/builders.rs`,
`impl Default for Builder`):

    let metac = meta::Config::new()
        .nfa_size_limit(Some(10 * (1 << 20)))      // 10,485,760 = 10 MiB
        .hybrid_cache_capacity(2 * (1 << 20));     // 2,097,152  = 2 MiB

Both numbers match `src/main.rs`'s `DEFAULT_SIZE_LIMIT`/
`DEFAULT_DFA_SIZE_LIMIT` constants exactly, and the built driver's own
`info size_limit 10485760` / `info dfa_size_limit 2097152` lines confirm
the same at runtime. The SAME `Default for Builder` block also settles
(d) below structurally: `build_one_bytes()` (the `regex::bytes` path this
driver uses) hardcodes `.match_kind(MatchKind::LeftmostFirst)` — not a
configurable default a future crate version could silently change out
from under this adapter without a source diff showing it.

## (d) The match convention, and the whole-subject form's own derivation

**`perl-leftmost-first`** — capability_set_v1.md §7.6's own table
(line 852): "the crate's documented claim; N2 flags it as not
independently reproduced." **NOW INDEPENDENTLY REPRODUCED** (lane
`l6brustfin`, 2026-09-19): the textbook witness (`foo|foobar` over
`"foobar"`) run directly against the built driver answers
`match [0,3)` — the FIRST alternative wins, not the longer one — the
same confirmation `testees/re2/CLAUDE.md` already carries for
`re2-default`. Structurally backed too: `MatchKind::LeftmostFirst` is
hardcoded (not merely defaulted) in the pinned crate's own
`Builder::build_one_bytes()`, so this is not a config a future version
bump could flip silently.

**TWO forms, but no dual match-invocation.** Unlike Oniguruma (which
calls `onig_match` at a fixed position for `whole-subject`, supplying the
START anchor at the API level) or pcre2/RE2 (a runtime anchor flag), the
`regex` crate's public `Regex`/`RegexBuilder` exposes **no runtime
anchored-search option at all** — `find()` always scans unanchored from
position 0 forward, and will happily report a match starting at byte 40
if there is none at byte 0. So `adapter.py`'s `compile()` does **NOT**
reuse `pcrecbench.record.whole_subject_text(pattern)` (`(?:pattern)\z`)
the way `testees/onig/adapter.py` does — that wrap alone would
UNDER-anchor a whole-subject artifact here, letting a SUFFIX match pass.
Instead the adapter bakes BOTH anchors into the compiled text itself:
**`\A(?:<pattern>)\z`**. `\A` and `\z` are both real, always-true-position
anchors in this crate's syntax (unaffected by multi-line mode, unlike
`^`/`$`), so an ordinary unanchored `find()` on the wrapped text answers
the `match` regime correctly with **no driver-side branching at all** —
`--form`/`--mode` are still accepted and cross-checked for protocol-shape
parity with the other drivers (a decoupled invocation dies loudly), but
this driver's actual control flow is IDENTICAL for both forms. This is
the same KIND of adapter-level decision `testees/tre/CLAUDE.md` documents
for TRE's own `^(?:pattern)$` wrap (built inside its driver rather than
reusing the shared helper, for TRE's own different reason: no `\z`
spelling at all) — a real, load-bearing DEVIATION from the shared
`whole_subject_text()` convention, stated here rather than left for a
reader to discover as an unexplained wrap.

## The I-72 lesson, and the structural finding it led to

**This adapter is I-72-immune BY CONSTRUCTION**, same reasoning as every
other L6b adapter: the pattern travels from python to the driver as a
FILE (`--pattern FILE`), never a subprocess argv element, so the
fsencode/latin-1 mojibake class (`pattern.decode("latin-1")` +
subprocess's own UTF-8 re-encoding of a `str` argv element — the bug
pcrec's own adapter hit) cannot occur here structurally. `adapter.py`
writes the pattern with `open(patfile, "wb")` unconditionally; `src/
main.rs`'s `slurp()` reads it back as raw `Vec<u8>` with no text-mode
step anywhere in between.

**But this project's own shared I-72 witness pattern cannot compile
under `rust-default` at all — a DIFFERENT, genuine, engine-structural
limitation, not a bug in this adapter.** `tools/selfcheck.py`'s
`check_high_byte_pattern_argv` witness is `PAT = b"\x93[\\x20-\\x7e]*
\x94"` — a Python NON-raw bytes literal, so `\x93`/`\x94` are the RAW
SINGLE BYTES 0x93/0x94 (confirmed: `xxd bench/capability/patterns/
mojibake-curly-quote.rx` shows the identical shape — a literal 0x93/0x94
byte pair on disk, not an ASCII escape sequence). `regex::bytes::
RegexBuilder::new` takes `&str`, **never `&[u8]`, for the PATTERN
SOURCE** — there is no bytes-mode escape hatch for the pattern the way
there is for the haystack (`regex::bytes::Regex` matches over `&[u8]`
haystacks specifically to gain `non-utf8-subject` for SUBJECTS; the
pattern itself, being Rust source-level `&str`, has no equivalent). A
single byte 0x93 is not valid UTF-8 on its own (a lone continuation
byte), so `std::str::from_utf8` on this pattern's raw bytes FAILS —
`src/main.rs` catches this explicitly, before ever calling into the
`regex` crate, and reports a clean structural `did-not-compile` naming
the exact byte offset (`pattern is not valid UTF-8 at byte 0: invalid
utf-8 sequence of 1 bytes from index 0`), never a panic.

**CONFIRMED** (lane `l6brustfin`, 2026-09-19 census —
`docs/dev/measurements/2026-09-19-rust-capability-census-r1131.txt`):
`mojibake-curly-quote` refuses with exactly the predicted diagnostic,
`[syntax/InvalidUtf8Pattern] pattern is not valid UTF-8 at byte 0:
invalid utf-8 sequence of 1 bytes from index 0` — the driver's own
pre-regex-crate UTF-8 validation, not a crash, not the `regex` crate's
own error type. The finding stands as predicted: `non-utf8-subject`'s
own token definition ("the subject bytes are not valid UTF-8",
capability_set_v1.md §5.1's table) is about SUBJECTS, and this adapter
satisfies it there (`regex::bytes` haystacks need not be valid UTF-8,
witnessed on `high-byte-run`'s pattern `[\x80-\xff]{2,4}`, which
COMPILES clean — see the discrimination section below for what it
actually MATCHES); but a SEPARATE, sharper constraint — the PATTERN
source must itself be valid UTF-8 — is real and has no token of its own
in capability_set_v1.md §5.1's vocabulary. `mojibake-curly-quote` (the
only `bench/capability` pattern whose OWN `.rx` file carries a literal
non-UTF-8 byte, not merely an escape sequence) is the single corpus
pattern this hits, exactly the "documented SPELLING gap, not a
capability gap" shape `testees/onig/CLAUDE.md`'s own
`balanced-parens-rec` finding sets precedent for — left to fail HONESTLY
as its own real `did-not-compile` (`refusal_class: syntax`) rather than
hidden behind a wholesale `non-utf8-subject` withhold that would
misrepresent the rest of the corpus's non-UTF-8-SUBJECT patterns, which
do not carry this problem. (Cross-checked against every OTHER refused
corpus pattern too: all 21 remaining `bench/capability` refusals tie to
a withheld `REQUIRES_VOCAB` token by name — see the capability
declaration below — so `mojibake-curly-quote` is the ONE, explained
exception, never an unexplained refusal.)

## `non-utf8-subject`: RESOLVED — the class matches the UTF-8 ENCODING, not the raw byte, under this config's default unicode mode

This lane's own open question, found by REASONING about the crate's
documented semantics before any build existed, is now SETTLED by a real
MATCH-grain witness (`probe_rust_capability_census.py`'s
`census_nonutf8_discrimination()`,
`docs/dev/measurements/2026-09-19-rust-capability-census-r1131.txt`):

    class \x80-\xff  vs raw high byte (0x93...0x94)             nomatch
    class \x80-\xff  vs UTF-8-encoded codepoint (C2 93...C2 94)  match  [0,2)
    (?-u:...) class  vs raw high byte (0x93...0x94)              match  [0,1)
    (?-u:...) class  vs UTF-8-encoded codepoint (C2 93...C2 94)  match  [0,2)

The reasoned hypothesis was RIGHT: `RegexBuilder::unicode(bool)` defaults
to **true** for `rust-default` (needed for `unicode-properties`), and
under that default a byte-range class like `[\x80-\xff]` matches the
Unicode SCALAR VALUE at that code point against its UTF-8 ENCODING in the
haystack, **not** the raw byte — `[\x80-\xff]` genuinely does NOT match a
lone raw byte `0x93` (nomatch), only that codepoint's two-byte UTF-8
encoding `C2 93` (match). The escape hatch is exactly the predicted one:
`(?-u:...)` (Unicode OFF for just that sub-expression) DOES match the raw
byte, and — expected, checked as the fourth row above — also still
matches the two-byte encoded form (both are legal single- or
double-byte-at-a-time matches for a byte class with unicode off).

**Disposition: `non-utf8-subject` stays SATISFIED for `rust-default`, at
the STRUCTURAL/API level the token's own definition names**
("the subject bytes are not valid UTF-8", capability_set_v1.md §5.1) —
the driver's `regex::bytes` API never refuses or panics on a genuinely
invalid-UTF-8 haystack (the raw-byte row above answers a clean
`nomatch`, not an error; `regex::bytes::Regex::find()` takes `&[u8]`
with no UTF-8 requirement at all). **But this is a real, load-bearing
SEMANTIC caveat, documented here so nobody mistakes a future outlier for
an adapter bug**: `bench/capability`'s `high-byte-run` pattern
(`[\x80-\xff]{2,4}`) COMPILES under `rust-default` and is attempted
against the corpus's real subjects, but — UNLIKE under RE2's
`EncodingLatin1` or Oniguruma's `ONIG_ENCODING_ASCII`, both of which
treat every byte-range class as literal bytes unconditionally — it will
NOT match a genuine raw high byte the way the oracle expectation (derived
from libpcre2, itself byte-oriented by default) predicts. Any resulting
mismatch on `high-byte-run` under `rust-default` is expected to surface
HONESTLY as a real wrong-answer/outlier in the reporter's scoreboard,
never silently — exactly the "a real corpus failure under a satisfied
token is a documented, honest outcome, never a re-litigation of the
declaration" precedent `testees/vectorscan/CLAUDE.md`'s `free-spacing`
finding and `testees/onig/CLAUDE.md`'s `recursion`-spelling gap both set.
A future `rust-smallsize`-style config that instead wraps its patterns in
`(?-u:...)` (or calls `RegexBuilder::unicode(false)` wholesale) would
close this gap and match raw bytes literally, the same way the other
byte-oriented engines do by default — not built here (no census evidence
motivates a second config yet, per this lane's own brief).

## Refusals, first-class

`RegexBuilder::build()` failure → `did-not-compile`, `diagnostic`
carrying the driver's own `regex build failed [<variant>]: <message>`
line (`src/main.rs`'s `error_variant_name`, reading `regex::Error`'s
stable `Debug` variant name rather than an exhaustive `match` — the type
is `#[non_exhaustive]`, the crate's own MSRV-stability promise that a new
variant can appear in a minor release). `refusal_class`
(capability_set_v1.md §5.5: "declared ONLY by a config whose engine gives
a closed, structural signal") is derived in `adapter.py`'s
`classify_refusal`: `size-limit` for `CompiledTooBig`, `syntax` for
`Syntax` and for this adapter's OWN pre-regex-crate UTF-8 validation
refusal (which carries no bracketed variant name — recognized by its own
fixed message prefix, `"pattern is not valid UTF-8 at byte"`).

**`giveup:<code>` never fires from this driver.** The `regex` crate
guarantees worst-case LINEAR time in haystack length by construction (no
catastrophic backtracking is possible) and its public match API
(`find`/`captures`) returns a plain `Option`, never a resource-limit
refusal code — the SAME structural fact `testees/re2/CLAUDE.md` states
for RE2's `Match()` API (capability_set_v1.md §5.4). `handle["giveup_
codes"]` is the empty set, by construction, not merely by omission.

A construct the `EXT_BENCH_ROSTER` row below declares missing never
reaches this adapter's own refusal path — `pcrecbench.capability`'s
pre-compile policy intercepts it first (`unsupported-by-declaration`).

**`possessive-quantifier` PARSES but is not WITHHELD-for-refusal — it is
WITHHELD for a different, subtler reason, first-class in its own right:
the syntax COMPILES clean (no `did-not-compile` row ever fires on it),
but its SEMANTICS are not possessive.** Witnessed 2026-09-19 (lane
`l6brustfin`): `(?:a++)a` run directly against the built driver MATCHES
subject "aaa" at `[0,3)` — the whole string. Under PCRE's true possessive
semantics `a++` would consume all three `a`s with NO backtracking
available to release one for the trailing `a`, so the match would FAIL
outright (no other start offset has enough `a`s either). It did not fail:
the crate's automaton-based engine has no backtracking to forbid in the
first place, so `a++` behaves exactly like `a+`. The capability
declaration below WITHHOLDS this token on that finding — capability is
about SEMANTICS, not syntax acceptance (the same standard this project
already applies to TRE's `k-reset`/`control-verbs`/`recursion` SILENT
MISPARSE hazards, `testees/tre/CLAUDE.md`) — even though, unlike a TRE
misparse, `a++` here compiles to something semantically IDENTICAL to a
plain `a+`, never a wrong construct.

## The per-subject timeout: a thread, not a signal/longjmp pair

Every other driver in this project (`pcre2`/`onig`/`tre`/`re2`) uses
`sigsetjmp`/`siglongjmp` across a `SIGALRM` handler for its
`--subject-timeout`. Doing the same across Rust stack frames is
undefined behavior — `longjmp` does not run Rust destructors, and this
is not a style preference (Rust's own panic-across-FFI documentation
states the same hazard one layer up). `src/main.rs` instead runs each
timed subject on a plain OS thread (only when `--subject-timeout > 0`)
and the main thread waits on a channel with `recv_timeout`; a fired
timeout reports `timedout` and abandons the thread rather than killing
the process. This is a SAFETY-NET-ONLY mechanism given the crate's
linear-time guarantee (unlike Oniguruma/pcre2, a rust-regex timeout can
only be provoked by raw input SIZE, never catastrophic-backtracking
blowup — capability_set_v1.md §5's own "redos-nested" family finding:
RE2/Rust/Vectorscan/TRE are IMMUNE by construction). The clock discipline
(one `Instant::now()` before the `iters` loop, one after) happens INSIDE
the timed thread, so thread-spawn latency is never part of a reported
number. **Exercised 2026-09-19** (lane `l6brustfin`): a no-match subject
(100,000 `b`s against pattern `a`) driven at `--iters 200000000
--subject-timeout 1` reports `subject sbig timedout - - 0 - 200000000
1.000000000 - -` cleanly at the 1-second boundary — no crash, no hang,
the process exits 0 with every other protocol column intact (`-` for the
unset span/consumed/caps fields, matching every other driver's
`timedout` row shape).

## The capability declaration — WITNESSED, WIRED

`bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER` carries a
`rust-default` row (lane `l6brustfin`, 2026-09-19), derived from the real
witness census — `docs/dev/measurements/probe_rust_capability_census.py`,
archived at
`docs/dev/measurements/2026-09-19-rust-capability-census-r1131.txt` — the
same L5 discipline ("witnessed compiles/refusals, never documentation")
every other L6b lane followed, never from N2's earlier prediction alone.

**8 of 17 tokens SATISFIED** (one isolated witness each, corpus-confirmed
below): `unicode-properties`, `named-groups`, `free-spacing`,
`span-reporting`, `non-utf8-subject` (at the API/structural level — see
the discrimination finding above for the semantic caveat), `captures`,
`true-end-anchor`.

**9 tokens REFUSED**, every one `[syntax/Syntax]` at the isolated witness
(N2's prediction HELD for all nine): `backrefs`, `lookaround`,
`lookbehind-variable`, `atomic-group`, `recursion`, `conditionals`,
`k-reset`, `control-verbs`, `callouts`.

**1 token WITHHELD on a semantic finding, not a refusal** (N2's
prediction did NOT hold — corrected by this lane's own witness, see
above): `possessive-quantifier` COMPILES but is not semantically
possessive (`(?:a++)a` matches "aaa" where true possessive semantics
would refuse), so it is excluded from the roster row below exactly like
a refused token, on different evidence.

    ("rust-default", [t for t in REQUIRES_VOCAB
                      if t not in ("backrefs", "lookaround",
                                   "lookbehind-variable",
                                   "possessive-quantifier",
                                   "atomic-group", "recursion",
                                   "conditionals", "k-reset",
                                   "control-verbs", "callouts")]),

**Corpus confirmation** (`bench/capability@0.1`, 64 patterns): 42/64
compiled, 22 refused. Every refusal ties to a withheld token by name
EXCEPT `mojibake-curly-quote` (`requires=non-utf8-subject` alone), which
refuses for the documented, SEPARATE I-72 pattern-source-UTF-8 reason
above, under a token this row keeps SATISFIED — the same
"real corpus failure under a satisfied token is a documented, honest
outcome, never a re-litigation of the declaration" shape RE2/Oniguruma/
TRE/Vectorscan's own rows all follow. `bench/syntax@0.1` (95 patterns,
informational cross-check, not capability-gated): 50/95 compiled, 45
`Syntax` refusals.

## Version: PROBED, never typed — but by TWO different mechanisms for TWO different facts

`testees/CLAUDE.md`'s rule ("every version is PROBED, never typed")
holds, split the same way `testees/re2/CLAUDE.md` splits it: `engine_
version` (the fact `testee_id` derives from, record_schema.md §6.4) is
the **`regex` crate's own version**, read from the COMMITTED `Cargo.lock`
(`adapter.py`'s `_read_cargo_lock_regex_version`, using the stdlib
`tomllib` this project's `configs.toml` loader already depends on) —
never typed, and durable across a rebuild the way a live query cannot be
(the crate publishes no runtime version API at all, the same absence
class RE2's `_probe_version` docstring states for RE2). The **toolchain**
fact (`rustc --version`) rides in `build_flags` for provenance, probed
live at every `describe()` call, exactly like `re2`'s Debian package
version does for RE2.

## Smoke coverage — LANDED

`tools/selfcheck.py`'s `check_high_byte_pattern_argv` (the I-72 guard,
`make check-harness`) gained arm **1e** (lane `l6brustfin`, 2026-09-19):
a FOURTH shape, neither "compiles and matches" like pcrec/pcre2/onig/tre
nor "matches at boolean grain" like vectorscan — a clean `did-not-compile`
naming byte offset 0 on the raw `\x93`/`\x94` witness (proving the bytes
arrived UNCORRUPTED: a genuinely argv-mangled spelling, `C2 93 ... C2
94`, IS valid UTF-8 and would have compiled instead — the discrimination
this project's other arms get from a SUCCESSFUL match, this one gets from
a SPECIFIC, byte-exact FAILURE), plus the corrupted-spelling control
(compiles, does not match the clean subject). Gated on `"rust" in
_ad.discover()`, same as every other L6b arm — a box without a Rust
toolchain skips it by name rather than failing.
