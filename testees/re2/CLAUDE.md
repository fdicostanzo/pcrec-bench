# testees/re2/ — the RE2 adapter

[B42] L6b, 2026-09-17: the first lane of `docs/design/capability_set_v1.md`
§11.1's per-new-engine roster ([B7]). Provides two testees:

| config id | execution model | automaton_class | compile phases | convention |
|---|---|---|---|---|
| `re2-default` | `eager-jit` (capability_set_v1.md §7.1/§7.2's own token, WITH the stated caveat below) | `nfa-simulation` | `compile` | `perl-leftmost-first` |
| `re2-longest` | `eager-jit` (same caveat) | `nfa-simulation` | `compile` | `posix-leftmost-longest` |

`re2-bigmem` (capability_set_v1.md §8: 64 MiB `max_mem`) is explicitly
`later` and is **not built here**.

| file | role |
|---|---|
| `adapter.py` | `describe`/`prepare`/`compile`/`measure`; the two config option objects; `refusal_class` classification from RE2's own `ErrorCode` |
| `driver.cc` | the batched in-process timing driver (the protocol is in `pcrecbench/adapters.py`); a DIRECT RE2 C++ driver, never `cre2` |
| `configs.toml` | the two config ids; **no version is written here** (testees/CLAUDE.md's rule) |

## Why a direct RE2 C++ driver, not `cre2`

`docs/dev/research/2026-09-12-b42-engine-landscape.md` (2), CLOSED:
`cre2` needs a four-package autotools bootstrap this box does not have
(`autoconf`/`automake`/`libtool` on top of `libabsl-dev`) to build a
project that has never been release-tagged (zero GitHub Releases), while
`libre2-dev` is already installed and pkg-config-discoverable. The driver
protocol imposes no language constraint — it specifies argv/stdout SHAPE
only — so `prepare()` runs its own `g++ -std=c++17 $(pkg-config --cflags
--libs re2)` step (`testees/re2/adapter.py`'s `prepare_driver`), never
`pcrecbench.driverrun.build_driver()`, which assumes a C compiler and a
flat link-flags list.

## The compile-cost definition (deliverable (a))

**One phase, `compile`**: the explicit `RE2(pattern, options)`
**constructor** call, timed in-driver (`driver.cc`'s `compile\t<trial>\t
compile\t<seconds>` line). `execution_model = "eager-jit"` — the closest
existing token (`requirements.md §3`'s own test: "an explicit,
separately-timeable construction call").

**The caveat, stated where a reader of the number will find it**
(capability_set_v1.md §7.1/§7.2): unlike `pcre2-jit`'s
`pcre2_jit_compile`, RE2's constructor does **not** build the runtime
DFA. RE2's DFA is built **lazily at first match**, cached, and can be
flushed and rebuilt under `max_mem` pressure (`re2.h`'s own words: "once
a DFA fills its budget, it flushes its cache and restarts"). So an
`re2-default` compile-cost number and a `pcre2-jit` compile-cost number
share the `eager-jit` class token but are not the same SHAPE of quantity
— the reporter's §7.2 footnote rule (pooling two `eager-jit` testees
whose `testee.compile_cost_definition` strings differ prints a footnote)
fires automatically whenever a report puts them in one table.

`engine_metadata` (declared in `adapter.py`'s `METADATA_DECL`, pattern
scope): `ncapturegroups` (`RE2::NumberOfCapturingGroups()`),
`program_size` (`RE2::ProgramSize()` — re2.h's own words: "a very
approximate measure of a regexp's cost"; the FORWARD program only) and
`reverse_program_size` (`RE2::ReverseProgramSize()` — the SECOND program
RE2 builds for an unanchored search's second phase; declared as its own
pair rather than folded into `program_size` because RE2, unlike pcre2 or
pcrec, genuinely has two). And `refusal_class`, on a did-not-compile row
only. It was emitted from the start but DECLARED only at [B95],
2026-09-26 (KB-33: the first re2 refusal ever measured, utf8@0.1's
`prp-greek-sc`, got its whole cell rejected by X15 at store.write).

## `consumed_length`: the convention, stated plainly (deliverable (b))

**`consumed_length` is the subject length this driver passed and RE2
accepted — i.e. the whole subject**, exactly the same convention
`testees/pcre2/CLAUDE.md` states for `pcre2_match`. `RE2::Match()` takes
an explicit `endpos` argument and exposes no scan high-water mark, so the
honest claim is *"no byte was withheld or refused"*, never *"the engine
looked at every byte"*.

## The two v1 configs and their exact option objects (deliverable (c))

Both set `RE2::Options::set_encoding(RE2::Options::EncodingLatin1)` (see
"Byte mode" below) and leave `max_mem` at RE2's own library default,
`RE2::Options::kDefaultMaxMem` (`8 << 20` = 8 MiB, `re2.h`). They differ
in exactly one field:

```
re2-default:  RE2::Options opts;                       // longest_match = false (default)
              opts.set_encoding(EncodingLatin1);
              opts.set_max_mem(8388608);
              opts.set_log_errors(false);

re2-longest:  RE2::Options opts;
              opts.set_encoding(EncodingLatin1);
              opts.set_longest_match(true);             // the ONE difference
              opts.set_max_mem(8388608);
              opts.set_log_errors(false);
```

`set_log_errors(false)`: this project reads RE2's refusal STRUCTURALLY
(`RE2::error_code()`/`RE2::error()`), never by parsing stderr, so RE2's
own default `log_errors(true)` (which writes a parse error to `ERROR` via
its internal logging) would only ever be noise on this box.

**Byte mode (`EncodingLatin1`), and why it is a real capability decision,
not cosmetic.** RE2 defaults to `EncodingUTF8`, under which a lone byte
`>= 0x80` that is not part of a valid UTF-8 sequence is a compile-time
`ErrorBadUTF8`. This project's convention is byte-level matching
throughout (pcre2's own driver compiles with no `PCRE2_UTF` option;
pcrec's default route is its byte engine) — `EncodingLatin1` is what
makes RE2 comparable on that convention, and it is what makes family 12
(`binary-nonutf8`)'s non-UTF-8 patterns/subjects capability-testable
under RE2 at all rather than refusing for a reason that has nothing to
do with the capability being measured.

## RE2's match convention, and what it means for expectations (deliverable (d))

**`re2-default`**: `perl-leftmost-first`-**LIKE** selection — RE2's own
submatch-selection algorithm emulates Perl's semantics without literal
backtracking (docs/dev/research/2026-09-12-b42-engine-landscape.md §2.2).
**`re2-longest`**: `RE2::Options::set_longest_match(true)` — genuine
POSIX leftmost-longest selection, a per-COMPILE choice on the same
parser.

**Confirmed live on this box** (both directly against `driver.cc`, not
inferred): `foo|foobar` over `foobar` answers `[0,3)` under
`re2-default` and `[0,6)` under `re2-longest` — the textbook
leftmost-first-vs-leftmost-longest divergence, reproduced byte for byte.

**Consequence for expectations**: `re2-default` is scored against this
project's SHARED-CONVENTION `perl-leftmost-first` expectation population
(capability_set_v1.md §5.6's v1 scope) exactly as pcre2/pcrec are.
`re2-longest` is the SECOND convention reading family 11
(`semantics-divergence`) needs but v1's harness cannot yet score
(`Subbench.expectation` is keyed on `(pattern, subject_id, regime)` with
no per-testee convention override, capability_set_v1.md §5.6) — so a
`re2-longest` cell measured against family 11's own patterns will show
`wrong-span-or-captures` on the alternation-order cases WHERE THE TWO
CONVENTIONS GENUINELY DIVERGE. This is EXPECTED and DOCUMENTED, the same
shape `testees/pcre2/CLAUDE.md`'s `pcre2-dfa` section states for its own
decreasing-length-order divergence — not a `re2-longest` defect, and not
this lane's to fix (the missing per-testee/variant expectation override
is capability_set_v1.md §5.6's own named future lane).

## The capability declaration (deliverable 3) — from a REAL compile census, never docs

`bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER` carries
`re2-default`/`re2-longest` — **identical capability lists**, since
`longest_match` changes which alternative wins at one start point, never
what RE2's PARSER accepts (confirmed: both configs answer identically on
the witness set). Derived from a real compile census
(`docs/dev/measurements/probe_re2_capability_census.py`, archived at
`docs/dev/measurements/2026-09-17-re2-capability-census.txt`, the L5
discipline: "witnessed compiles/refusals, never documentation"): one
minimal witness per `REQUIRES_VOCAB` token, PLUS every one of
`bench/capability@0.1`'s own 64 patterns, PLUS `bench/syntax@0.1`'s 95
(the "other sets' patterns as available" corpus) — all compiled through
the real `testees/re2/adapter.py` `compile()` path.

**REFUSED** (RE2's own closed `ErrorCode` naming the mechanism every
time — never a guess from a message string): `backrefs`, `lookaround`,
`lookbehind-variable`, `possessive-quantifier`, `atomic-group`,
`recursion`, `conditionals`, `k-reset`, `control-verbs`, `free-spacing`,
`callouts`. `free-spacing` (`(?x)`) is the one N2 research note left
documentation-only; this census CONFIRMS the refusal live, on the
witness and on three corpus patterns
(`codegrammar-xflag`, two `wild-codegrammar-json-*` members, and
`bench/syntax`'s `mod-x`), every one `ErrorBadPerlOp: invalid perl
operator: (?x`.

**SATISFIED**: `unicode-properties`, `named-groups`, `span-reporting`,
`non-utf8-subject` (witnessed on the SAME raw-high-byte shape the I-72
guard uses — see below), `captures`, `true-end-anchor` (`\z` compiles;
its sibling `\Z`, `bench/syntax`'s `anc-z-uc`, REFUSES — RE2 has `\z`,
not `\Z`).

Corpus totals (compile-only; not a ranking claim — refusal is a CENSUS,
capability_set_v1.md §7.5): `bench/capability` 39/64 compiled, 25
refused; `bench/syntax` 47/95 compiled, 48 refused. Every refusal's
`ErrorCode` falls under one of the eleven excluded tokens above, or is a
PCRE-only escape/production this vocabulary has no token for at all
(`\Z`, `\G`, `\h`, `\N`, inline comments `(?#...)`, branch-reset
`(?|...)`) — never an unexplained refusal.

## Refusal as a first-class outcome

`adapter.compile()` maps a construction failure (`!re->ok()`) to
`did-not-compile`, carrying RE2's own diagnostic verbatim (`RE2
construction failed [<ErrorCode name>]: <message>`) and a declared
`refusal_class` (`docs/design/capability_set_v1.md` §5.5) derived from
that same bracketed name (`adapter.classify_refusal`; `REFUSAL_CLASS`
maps every named `ErrorCode` — `ErrorPatternTooLarge` → `size-limit`,
every other code → `syntax`). RE2 exposes no third, resource-limit-shaped
compile refusal the way pcre2's `MATCHLIMIT`/`DEPTHLIMIT` family does —
there is nothing budget-shaped to decline at RE2 CONSTRUCTION time beyond
parsing and the one size cap. **A capability-declared `unsupported`
pattern never reaches `compile()` at all** — the harness's pre-compile
policy (`pcrecbench/capability.py`) intercepts it first
(`unsupported-by-declaration`), so `did-not-compile` on this testee means
a genuine parse/size refusal the declaration did not anticipate, not a
known capability gap.

**`giveup:<code>` never fires from this driver.** RE2's `Match()` API
returns a plain bool; there is no per-call signal that RE2 declined to
keep searching the way pcre2's negative MATCHLIMIT/DEPTHLIMIT/HEAPLIMIT
codes are (a graceful DFA-cache-flush-and-retry under `max_mem` pressure
is a match-time MECHANISM change the caller cannot observe, per
capability_set_v1.md §5.4). This driver's only per-subject answers are
`match`/`nomatch`/`timedout` (this driver's own alarm).

## The I-72 lesson: raw bytes end to end

The pattern travels from python to the driver as a **FILE**
(`--pattern FILE`, the shared protocol), never as a subprocess argv
element — so this adapter is not exposed to the fsencode/latin-1
mojibake class the pcrec adapter hit (pcrec's pattern travels on argv;
`testees/pcrec/adapter.py`'s I-72 fix comment). `adapter.compile()`
writes the pattern with `open(patfile, "wb")` / `f.write(bytes(pattern))`
— binary, unconditionally — and `driver.cc`'s `slurp()` reads it back as
raw bytes with no text-mode reinterpretation anywhere in between.
Confirmed end to end with the I-72 witness shape itself
(`\x93[\x20-\x7e]*\x94` over `\x93hello\x94`, matching `[0,7)` under
`EncodingLatin1` — reproduced directly against the built driver and as
this set's own `non-utf8-subject` witness and `high-byte-run`/
`mojibake-curly-quote` corpus members, all COMPILED and correctly
answered).

## `testee_id` composition

`record_schema.md §6.4`'s standard rule:
`re2_<version_slug>_<engine_mode>-caps-simdna`. Observed on this box:
`re2_11.0.0_default-caps-simdna`, `re2_11.0.0_longest-caps-simdna`
(`caps` because `captures = "on"` for both — RE2 always reports
captures; `simdna` because RE2 declares no SIMD dial on this bench).

## Version: PROBED, never typed — but RE2 exposes no runtime version API

`testees/CLAUDE.md`'s rule ("every version is PROBED, never typed")
still holds, but RE2 gives no `RE2_VERSION` symbol and no version-string
API at all (confirmed absent, `/usr/include/re2/re2.h` read in full).
The closest honest equivalent this project's other adapters use
(pcre2: `pcre2_config`; pcrec: `git describe` on the pinned commit) is
the **installed package's own metadata**: `pkg-config --modversion re2`
(`re2.pc`'s `Version` field — the shared library's soname/ABI version,
e.g. `11.0.0`) is the probed `engine_version`; the Debian package version
(RE2's actual upstream snapshot date, e.g. `20250805-1build3` — Google's
own date-based release convention, since RE2 has no semantic version)
rides along in `build_flags` for full provenance, the same way
`pcre2-jit`'s build date does. Neither is typed into `configs.toml`;
both are read live from the box's package database in `describe()`.

## A harness fix this lane needed: `run.driver_compiler` scoping

`pcrecbench/driverrun.py`'s `DRIVER_BUILDS` dict is **process-global**
and was read UNSCOPED by `driver_build_provenance()` — every driver
binary built anywhere in the CURRENT PROCESS, not just the one behind
THIS record. That was a silent no-op invariant for every testee in this
project's history until this lane: every prior adapter's driver was
built by the SAME compiler family (`gcc`), so joining "every compiler
used so far" and "the one compiler this record's driver used" always
happened to agree. RE2's driver is built by `g++` — the first different
compiler family on the roster — and a `quick --vs` comparing an
`re2-*` testee against a `pcre2-*` one in ONE process populated BOTH
testees' entries before either record was built, so the SECOND record's
`run.driver_compiler` read `"g-15.2.0, gcc"` (both, comma-joined) and
failed the schema's single-token pattern
(`^[a-z0-9][a-z0-9._-]*$` — no comma, no space).

Fixed at the one call site that matters (`pcrecbench/harness.py`, right
before `adapter.prepare(testee_id, workdir)`): `DRIVER_BUILDS.clear()`
scopes the dict to THIS testee's own build(s), since `prepare()`
immediately re-registers its own entry. A strict no-op for every
existing single-compiler-family testee; the fix is what makes `quick
--vs pcre2-interp` (or any RE2-vs-pcre2/pcrec comparison) usable at all,
which is the central use case this adapter exists to serve. Verified
directly: `quick --subbench email --pattern orig --regime search
--testee re2-default --vs pcre2-interp --subjects 5` now writes two
valid records (`re2-default` measured 2.30× faster than `pcre2-interp`
on this pattern/subject set — a plausible finding for a linear-time
automaton engine against a backtracker, not asserted as a ranking here).
No existing test or committed record exercises two compiler families in
one process, so this fix moves no existing number; a KB entry
(`docs/dev/known_issues.md`) is recommended for the manager to file so
the finding has a permanent home beyond this CLAUDE.md paragraph.

## Smoke coverage

`docs/dev/measurements/probe_re2_capability_census.py`'s witness+corpus
compile census (above) IS this adapter's structural smoke: every
`REQUIRES_VOCAB` refusal/acceptance is asserted against a live compile,
both directions (a token satisfied AND a token refused, per §5.2's
fail-closed rule), and the I-72 high-byte pattern is exercised as its
own named witness (`non-utf8-subject`) rather than a separate ad hoc
check. `make check-harness`'s generic `bench/*/` gates
(`gen_patterns.py --check`, `gen_provenance.py --check`,
`gen_variants.py --check`, `gen_expectations.py --check`) all pass
unchanged with the new roster rows present. No new `tools/selfcheck.py`
section was added: this adapter has no analogue of pcrec's per-abi
mechanism-stamp assertions to smoke (RE2 stamps exactly two
`engine_metadata` pairs beyond the always-present size facts —
`refusal_class` on a refusal — and that path IS the compile census
above), and adding a redundant driver-existence smoke would duplicate
what the census already asserts more precisely. If a future lane wants
`make check-harness` itself to fail on an RE2 capability regression
(rather than the census script, run separately), promoting the census's
assertions into `tools/selfcheck.py` is a natural, scoped follow-up.

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

The flag moves the advance only; the engine stays `EncodingLatin1` -- an
`re2-utf8` config is lane U2's (`utf8_set_v1.md` 7.1).

## `re2-utf8` ([B77] U2)

`encoding = "utf8"` -> the driver's `--encoding utf8` -> RE2's OWN default
`EncodingUTF8` (every other config keeps the Latin-1 override this file
explains above), on the compile AND every measure invocation.
`config_extra = utf8`: `re2_11.0.0_default-caps-simdna_utf8`. Otherwise
`re2-default` exactly.

WITNESSED (`docs/dev/measurements/2026-09-25-b77u2-utf8-witness-census.txt`): `utf8-encoding` and `ascii-class-scope` SATISFIED --
RE2's `\w`/`\d`/`\s`/POSIX classes stay ASCII in UTF-8 mode and there is
no widening dial; `unicode-class-scope` NOT (the set's `(*UCP)` spelling:
`ErrorRepeatArgument`); `unicode-properties` SATISFIED on general
categories. **Scripts (utf8_set_v1.md 7.4, settled):** bare `\p{Greek}` /
`\p{Cyrillic}` / `\p{Han}` / `\p{Latin}` compile, but bare `\p{Greek}`
reads SCRIPT, not PCRE2's Script_Extensions -- it answers `nomatch` on
U+0342 where the oracle answers `match` (an ANSWER divergence, not a
capability gap); every prefixed spelling (`sc=`, `Script=`, `scx=`,
`Script_Extensions=`) and `\p{InGreek}` refuse (`ErrorBadCharRange`).
Declares 7/20 (`non-utf8-subject` NOT by rule: the config's subject
contract is valid UTF-8).
