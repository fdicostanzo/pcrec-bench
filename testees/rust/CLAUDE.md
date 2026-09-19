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

**STATUS AT HANDBACK: AUTHORED, NOT YET BUILT OR CENSUSED.** Every file
here compiles against my own reading of the `regex` crate's public API,
cross-checked as carefully as I could manage without a running compiler,
but pcrec's I-75 battery held the box for the whole of this lane's
session (BOILERPLATE.md's HARD RULE: no `rustup`/`cargo` while it runs).
**Nothing in this directory has been built, and no capability claim below
is a witnessed one** — every "SATISFIED"/"REFUSED" line is a PREDICTION,
marked as such, to be replaced by `docs/dev/measurements/probe_rust_
capability_census.py`'s real output the moment the box frees. Treat this
file as a design note until that census's archive exists beside it.

| file | role |
|---|---|
| `Cargo.toml` | the driver crate manifest; `regex = "1"` (a semver requirement — the PIN is `Cargo.lock`, generated at the first build, OWED) |
| `Cargo.lock` | **NOT YET GENERATED/COMMITTED** — OWED, the first `cargo build` |
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

**Exact versions: OWED, to be filled in at the first build.** Recorded
here as placeholders until then:

- `rustc --version`: **TBD** (probed live by `adapter.py`'s
  `_probe_rustc_version()` at every `describe()` call — never hand-typed,
  same discipline `testees/CLAUDE.md`'s "one rule that is not obvious"
  states for every other engine)
- `cargo --version`: **TBD**
- `regex` crate version: **TBD** — read from the committed `Cargo.lock`
  by `adapter.py`'s `_read_cargo_lock_regex_version()`, never typed here
  either (this file states the MECHANISM, not a number that could drift
  out of sync with the lockfile)

**Install plan** (OWED, HELD until pcrec's battery trailer at
`/home/duxevents/pcrec/build/battery_923a5a58/trailer.log` prints `==
BATTERY DONE`):

    df -h /                                          # BEFORE
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \
        | sh -s -- -y --default-toolchain stable --profile minimal
    source "$HOME/.cargo/env"
    rustc --version; cargo --version                 # record above
    cd testees/rust && cargo build --release          # generates Cargo.lock
    df -h /                                           # AFTER first build
    git add Cargo.lock                                # commit the pin

No sudo anywhere (rustup installs entirely under `$HOME/.cargo` /
`$HOME/.rustup`); `--profile minimal` (no docs/clippy/rustfmt components)
to keep the install small per I-76's disk-watch instruction.
`df -h /` **before install**: `30G avail, 69% used` (this lane, 2026-09-19
11:09 EDT — matches I-76's own "69% at 08:41 today" figure).
**`df -h /` after the first build is OWED** (a real number here would be
one this lane never measured — not fabricated).

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

**The two numbers above are STATED FROM THIS LANE'S OWN MEMORY OF THE
CRATE'S PUBLISHED DOCUMENTATION, not yet reconfirmed against the exact
version `Cargo.lock` will pin.** OWED: once built, run
`cargo doc --no-deps -p regex --open` (or read the docs.rs page for the
resolved version) and confirm `RegexBuilder::size_limit`/
`dfa_size_limit`'s documented defaults still read 10 MiB / 2 MiB; if the
crate has changed them, `src/main.rs`'s `DEFAULT_SIZE_LIMIT`/
`DEFAULT_DFA_SIZE_LIMIT` constants and this section both need updating
before any record is measured.

## (d) The match convention, and the whole-subject form's own derivation

**`perl-leftmost-first`** — capability_set_v1.md §7.6's own table
(line 852): "the crate's documented claim; N2 flags it as not
independently reproduced." **STILL NOT independently reproduced by this
lane** (no build yet) — OWED: once built, run the textbook witness
(`foo|foobar` over `"foobar"`) directly against the driver and confirm
`[0,3)`, the same confirmation `testees/re2/CLAUDE.md` already carries
for `re2-default`.

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

**This is predicted, not yet witnessed** (OWED, the census run). If
confirmed, the finding is: `non-utf8-subject`'s own token definition
("the subject bytes are not valid UTF-8") is about SUBJECTS, and this
adapter satisfies it there (`regex::bytes` haystacks need not be valid
UTF-8, witnessed on `high-byte-run`'s pattern `[\x80-\xff]{2,4}` — see
below); but a SEPARATE, sharper constraint — the PATTERN source must
itself be valid UTF-8 — is real and has no token of its own in
capability_set_v1.md §5.1's vocabulary. The single corpus pattern this
hits (`mojibake-curly-quote`, the only `bench/capability` pattern whose
OWN `.rx` file carries a literal non-UTF-8 byte, not merely an escape
sequence) is predicted to refuse for this reason alone, exactly the
"documented SPELLING gap, not a capability gap" shape `testees/onig/
CLAUDE.md`'s own `balanced-parens-rec` finding sets precedent for — left
to fail HONESTLY as its own real `did-not-compile` (`refusal_class:
syntax`) rather than hidden behind a wholesale `non-utf8-subject`
withhold that would misrepresent the rest of the corpus's non-UTF-8-
SUBJECT patterns, which do not carry this problem.

## `non-utf8-subject`: TWO WITNESSES, ONE GENUINELY UNRESOLVED QUESTION

A second, independent open question this lane found by REASONING about
the crate's documented semantics (not yet resolved by a witness — the
census script below is built specifically to settle it):
`RegexBuilder::unicode(bool)` defaults to **true** for `rust-default`
(needed for `unicode-properties`). Under unicode mode, an escape like
`\x93` or a class like `[\x80-\xff]` is documented (as this lane recalls
it, UNCONFIRMED against the actual pinned version) to denote the Unicode
SCALAR VALUE at that code point, matched against its UTF-8 ENCODING in a
byte haystack — e.g. `\x93` would match the TWO-BYTE sequence `C2 93`
(U+0093's UTF-8 encoding), **not** the single raw byte `0x93`. If true,
`bench/capability`'s own `high-byte-run` pattern (`[\x80-\xff]{2,4}`) and
`mojibake-curly-quote`'s intended SEMANTIC (match a raw legacy-encoding
high byte) would not actually exercise raw-byte matching under
`rust-default` the way they do under RE2's `EncodingLatin1` or
Oniguruma's `ONIG_ENCODING_ASCII` — a real, load-bearing difference this
census must read from an actual MATCH run, not a compile check alone
(compiling proves nothing here; both readings compile fine). The `regex`
crate's own escape hatch, if this reading is correct, is the
per-expression flag `(?-u:...)` (Unicode OFF for just that
sub-expression, coexisting with `\p{L}` elsewhere in the SAME pattern) —
`probe_rust_capability_census.py`'s `census_nonutf8_discrimination()`
tests BOTH the plain class and the `(?-u:...)`-wrapped one against BOTH a
raw-byte subject and a UTF-8-encoded-codepoint subject, so the answer is
read, not assumed. **`non-utf8-subject`'s declaration for `rust-default`
is left OPEN until that census runs** — no line in `bench/capability/
gen_patterns.py`'s `EXT_BENCH_ROSTER` exists for this testee yet (below).

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

A construct the (not-yet-written) `EXT_BENCH_ROSTER` row will declare
missing never reaches this adapter's own refusal path — `pcrecbench.
capability`'s pre-compile policy intercepts it first
(`unsupported-by-declaration`).

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
number. **Not yet exercised against a real long-running subject** — OWED,
a smoke item once built.

## The capability declaration — NOT YET WRITTEN, OWED

`bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER` carries **no
`rust-default` row yet**. Every other L6b lane's own precedent (and this
project's L5 discipline) forbids writing one from documentation or memory
alone — `docs/dev/measurements/probe_rust_capability_census.py` is
authored and ready (see its own header) but has not been run: it needs a
built driver, which needs `cargo`, which is HELD until pcrec's battery
trailer shows `BATTERY DONE`. **This is the single largest OWED item in
this lane's delivery** — see the lane report for the exact resumption
steps.

**Predicted, from `docs/design/capability_set_v1.md` §5.1's own per-token
table (N2's research, not this lane's independent witness) — TO BE
CONFIRMED, not to be trusted as-is:**

- **REFUSED** (the crate structurally lacks these constructs, per N2's
  survey): `backrefs`, `lookaround`, `lookbehind-variable`,
  `possessive-quantifier`, `atomic-group`, `recursion`, `conditionals`,
  `k-reset`, `control-verbs`, `callouts`.
- **SATISFIED**: `unicode-properties`, `named-groups`, `free-spacing`,
  `span-reporting`, `captures`, `true-end-anchor`.
- **OPEN** (this lane's own finding, above, neither predicted by N2 nor
  resolved): `non-utf8-subject`.

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

## Smoke coverage — OWED

No `tools/selfcheck.py` section exists yet for this adapter (mirrors
`testees/re2/CLAUDE.md`'s own stated choice: the capability census IS
this adapter's structural smoke, once it runs). A `check_high_byte_
pattern_argv` THIRD-SHAPE arm (neither "compiles and matches" like
pcrec/pcre2/onig/tre, nor silently absent) is DESIGNED but not yet
added — assert the driver reports `did-not-compile` with a diagnostic
naming byte offset 0 on the raw witness (proving the bytes arrived
UNCORRUPTED: a genuinely corrupted argv-mojibake spelling, `C2 93 ... C2
94`, IS valid UTF-8 and would have compiled instead — the discrimination
this project's other arms get from a SUCCESSFUL match, this one gets from
a SPECIFIC, byte-exact FAILURE). Exact arm to add, OWED to `tools/
selfcheck.py`'s `check_high_byte_pattern_argv`:

    r, err = one("rust", "rust-default", PAT, "hib-raw")
    # expect: err is not None, and the adapter's own did-not-compile
    # diagnostic contains "not valid UTF-8 at byte 0" -- NOT "matched" and
    # NOT a crash. A control run of PAT_CORRUPT (C2 93 ... C2 94) SHOULD
    # compile (valid UTF-8) and should NOT match the clean raw-byte
    # subject -- the discrimination.
