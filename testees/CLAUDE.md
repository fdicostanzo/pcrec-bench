# testees/ — the adapters

One directory per ENGINE (harness contract §3). An engine directory
provides several TESTEES — an (engine, version, build/run configuration)
triple each (requirements §2) — enumerated in its `configs.toml`.

| directory | testees it provides |
|---|---|
| `pcre2/` | `pcre2-interp`, `pcre2-jit`, `pcre2-dfa`; and ([B77] U2, 2026-09-25) their UTF-8 siblings `pcre2-utf-interp`, `pcre2-utf-jit`, `pcre2-utf-dfa` (`encoding = "utf8"`: PCRE2_UTF, never PCRE2_UCP -- a pattern spells `(*UCP)` itself) |
| `onig/` | `onig-default` ([B7]/L6b, lane l6bonig, 2026-09-17: Oniguruma 6.9.10, `ONIG_SYNTAX_PERL_NG` / `ONIG_ENCODING_ASCII`, direct-linked `-lonig`. `onig-lowretry` is documented, not wired); `onig-utf8` ([B77] U2: `ONIG_ENCODING_UTF8` chosen at runtime, `--encoding utf8`) |
| `vectorscan/` | `vectorscan-block-nosom` ([B7]/L6b wave 2, lane `l6bvs`, 2026-09-17: Vectorscan 5.4.11, `HS_MODE_BLOCK`, NO `HS_FLAG_SOM_LEFTMOST` — BOOLEAN GRAIN ONLY per Frank's Q3 ruling: match/no-match and compile/refusal comparisons, never a span or a match count; direct-linked `-lhs` via `pkg-config libhs`; UNCHANGED by `vectorscan-block-som`'s arrival — argv, `build_flags`, `config_extra` and derived `testee_id` all byte-for-byte, proven by `check_encoding_axis`'s pre-existing frozen table plus a direct re-derivation); `vectorscan-block-som` ([B92], 2026-09-26, Frank's ruling on `capability_set_v1.md` 5.6 option (b): HS_FLAG_SOM_LEFTMOST always set — FULL GRAIN, sharing `driver.c` with its `nosom` sibling via one `--som` flag: a real first-match span (Hyperscan's own leftmost-longest completion, a documented, MEASURED divergence from this project's leftmost-first oracle on patterns like `a|ab`) and, under find-all, a real non-overlapping NMATCHES via KB-17's advance rule over the same reduction; HS_FLAG_SOM_LEFTMOST's own documented history-tracking restriction is a first-class `did-not-compile` via the existing generic refusal path, no new code needed — costs exactly 2 of bench/capability's 64 corpus patterns (docs/dev/measurements/2026-09-26-vectorscan-som-vs-nosom-census.txt); declares `unicode-properties`/`named-groups`/`free-spacing`/`non-utf8-subject`/`true-end-anchor`/`span-reporting` in `bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER` -- `nosom`'s own six minus nothing plus `span-reporting`, SOM's own execution-model gain); `vectorscan-block-nosom-utf8` ([B77] U2: `HS_FLAG_UTF8`, never `HS_FLAG_UCP` -- utf8_set_v1.md 7.6; boolean grain like its sibling); `vectorscan-block-som-utf8` ([B99], 2026-09-26: `som`'s character-mode sibling, `HS_FLAG_UTF8` ORed onto `HS_FLAG_SOM_LEFTMOST`, never `HS_FLAG_UCP`, FULL GRAIN like `som` -- mechanically composes as predicted (a real leftmost-longest span/NMATCHES over multi-byte text) and surfaces ONE new finding neither parent census could show: `(*UCP)\w+` REFUSES under SOM+UTF-8 ("Pattern is too large", the SAME diagnostic HS_FLAG_SOM_LEFTMOST's size budget uses elsewhere) though it compiles clean under `nosom-utf8` alone, so `unicode-class-scope` is satisfiable for `nosom-utf8` but NOT for `som-utf8`; no `EXT_BENCH_ROSTER` row, same convention as every other `-utf8` config; docs/dev/measurements/2026-09-26-vectorscan-som-utf8-witness-census.txt) |
| `tre/` | `tre-default` ([B7]/L6b, lane l6btre, 2026-09-17: TRE 0.9.0, POSIX leftmost-longest, `tre_regncompb`/`tre_regnexecb` (byte-literal, explicit-length), `REG_EXTENDED` no `REG_NEWLINE`, direct-linked `-ltre`. The ONLY config — TRE has no space/speed dial at all. See its own CLAUDE.md for the convention, every syntactic divergence from PCRE, and two silent-misparse hazards (`\K`, `(*NAME)`) this lane found) |
| `pcrec/` | `pcrec-auto`, `pcrec-nocaps`, `pcrec-vm` (the plain three, gcc); `pcrec-auto-in`, `pcrec-vm-in` (the caller-provided frame-buffer variants, [B8]); `pcrec-auto-clang`, `pcrec-nocaps-clang`, `pcrec-vm-clang` (the compilee-toolchain axis, [B24]); `pcrec-auto-bigcap`, `pcrec-vm-bigcap` (the emitted-size cap axis at 8 MiB, [B31] — bench/altwide's window only); `pcrec-auto-noedge` (the scan-edge deny axis, [B32] — [OPT-EDGE]'s BEFORE on bench/loglines and bench/bounded); `pcrec-auto-noisland` (the alternation-island deny axis, [B37] — the island's BEFORE on bench/altwide); `pcrec-auto-noclsfold`, `pcrec-vm-noclsfold` (the ASCII-fold class-test deny axis, [B39] — the fold's BEFORE on bench/altwide); `pcrec-auto-noreqbyte` (the necessary-byte pre-check deny axis, [B101] — `-fno-req-byte`, [OPT-REQBYTE]'s twin at ONE pin on bench/capability, pcrec I-111); `pcrec-auto-align64` (the compilee-FLAGS axis, [B35] — `-falign-functions=64`, pcrec I-39 (v)'s layout probe, against `pcrec-auto`); `pcrec-auto-utf8`, `pcrec-nocaps-utf8`, `pcrec-vm-utf8`, `pcrec-vm-in-utf8` (the engine-ENCODING axis, [B77] U2 — the usual four compiled `-e utf8`; `effective_encoding` puts `utf8` in `config_extra` as the FIFTH part); `pcrec-auto-align64loops`, `pcrec-auto-nolitrun-align64loops` (the placement-twin pair, [B110] — `-falign-functions=64 -falign-loops=64` together, inbox I-115 Q2's placement-vs-code separator); and `pcrec-local`, a PROVIDED binary at no pin (scratch tier by construction, [B10]). This row's own pinned-config COUNT trails the pcrec adapter's own re-pin narrative (see testees/pcrec/CLAUDE.md's opening line for the current, maintained figure) rather than being kept current here; `testees/pcrec/configs.toml` is the roster, `python3 -m pcrecbench testees` prints it |
| `re2/` | `re2-default` (library defaults: `perl-leftmost-first`-like selection, `max_mem` 8 MiB), `re2-longest` (`set_longest_match(true)`, `posix-leftmost-longest`) — [B42] L6b, 2026-09-17, the first non-pcre2/pcrec engine on the roster. A direct RE2 C++ driver (`driver.cc`, built by `prepare()`'s own g++/pkg-config step, never `driverrun.build_driver()`), byte-mode (`EncodingLatin1`) — except `re2-utf8` ([B77] U2: RE2's own default `EncodingUTF8`, driver `--encoding utf8`). See its own CLAUDE.md for the compile-cost definition, the `consumed_length` convention, the two configs' exact option objects, the leftmost-first-vs-leftmost-longest divergence and what it means for expectations, and the capability declaration derived from a real compile census (`docs/dev/measurements/2026-09-17-re2-capability-census.txt`) |
| `rust/` | `rust-default` (`RegexBuilder` at the crate's own documented defaults) — [B7]/L6b, lane `l6brust`/`l6brustfin`, chartered and finished 2026-09-19, the LAST unchartered engine on the roster. **BUILT AND CENSUSED**: rustc 1.98.1 / cargo 1.98.1 (rustup stable, home-only, no sudo), regex crate 1.13.1 pinned via committed `Cargo.lock` (inbox I-76). A NATIVE Rust driver (`src/main.rs`, built by `cargo build --release` via `prepare_driver()`, never a C/C++ driver linked against a C ABI — the `regex` crate has none worth adding as a dependency), `regex::bytes` throughout (byte-haystack matching; the PATTERN source must still be valid UTF-8, a genuine structural constraint distinct from `non-utf8-subject`). See its own CLAUDE.md for the compile-cost definition, the `consumed_length` convention, the `\A(?:...)\z` whole-subject wrap (a deviation from the shared `whole_subject_text()` helper, for its own structural reason), the thread-based per-subject timeout (never signal/longjmp, unsound across Rust frames, witnessed firing cleanly on a forced 1-second timeout), the I-72 finding (this adapter is immune by construction, and the project's own shared high-byte witness pattern refuses with a clean, witnessed `did-not-compile` naming byte offset 0 — `tools/selfcheck.py`'s `check_high_byte_pattern_argv` arm 1e), the `non-utf8-subject` discrimination finding (SATISFIED at the structural/API level; under this config's default unicode mode, byte-range classes match a codepoint's UTF-8 ENCODING rather than a raw byte — documented, not hidden), and the `possessive-quantifier` finding (`a++` COMPILES but is witnessed NOT semantically possessive — withheld from the capability declaration on that evidence, correcting N2's earlier prediction). The `EXT_BENCH_ROSTER` row (`bench/capability/gen_patterns.py`) declares 8/17 tokens SATISFIED, corpus-confirmed at 42/64 (`bench/capability`) and 50/95 (`bench/syntax`, informational) — see `docs/dev/measurements/2026-09-19-rust-capability-census-r1131.txt` |

An adapter is `adapter.py` (a subclass of `pcrecbench.adapters.Adapter`),
`configs.toml`, usually a `driver.c`, and a `CLAUDE.md` that states its
compile-cost definition and its `consumed_length` convention. Discovery
is by directory: `pcrecbench/adapters.py` imports `testees/*/adapter.py`
and asks each for its `testees()`.

`pcrecbench/adapters.py` is also where the DRIVER PROTOCOL both drivers
implement is specified, in full, at the top of the file. Read that
before writing a third driver: the point of the protocol is that two
engines' numbers are produced by the same shape of loop, so a difference
between them is the engine and not the harness.

## The two rules that are not obvious

**The engine ENCODING is an identity, not a flag the protocol passes**
([B77] U2, docs/design/utf8_set_v1.md §7). A non-pcrec config declares
`encoding = "utf8"` (read by `pcrecbench.adapters.config_encoding`;
absent = `byte`, every pre-[B77] config); pcrec spells `-e utf8` in its
own `flags` (`effective_encoding`). Either way `config_extra` gains
`utf8` and the derived `testee_id` is the byte sibling's plus `_utf8`
(`make check-harness`'s `check_encoding_axis`, incl. a frozen table
proving every pre-existing config's id unchanged). This is NOT the
driver protocol's `--utf8`, which moves only the find-all advance and is
keyed on the SET's oracle word ([B77] U1). Each UTF-8 config's
capability declaration rests on the witness census
`docs/dev/measurements/2026-09-25-b77u2-utf8-witness-census.txt`.

**Every version is PROBED, never typed.** `describe()` reads the engine's
own version out of the built artifact or the loaded library
(`pcre2_config(PCRE2_CONFIG_VERSION)`; pcrec's pinned commit +
`git describe`). A hand-typed version in a `configs.toml` would be a
claim the record could not check, and `testee_id` is DERIVED from it
(record_schema.md §6.4, rule X5) — so a wrong version silently renames
the testee.

**A NEW TESTEE ID needs a `bench/capability` roster row or an EXCLUDED
entry in the SAME commit** ([B111], 2026-09-28): `bench/capability`'s
`ext bench` roster (`EXT_BENCH_ROSTER` in
`bench/capability/gen_patterns.py`) is hand-listed per testee id, and
its fail-closed policy (`pcrecbench/capability.py` 5.2) means a testee
absent from it satisfies NOTHING — every `requires-*`-tagged pattern
reads `unsupported-by-declaration` rather than a real compile attempt.
`make check-harness`'s `check_capability_roster_coverage` enumerates
every testee id across every `testees/*/configs.toml`
(`pcrecbench.adapters.all_testees()`) and fails BY NAME on one in
neither `EXT_BENCH_ROSTER` nor `bench/capability/gen_patterns.py`'s
`EXCLUDED_TESTEES` (every deliberately-absent id, with why — see that
file and `bench/capability/CLAUDE.md`). This bit twice in three days
before the gate existed (outbox O-64/O-65, O-67 item 4); adding a
config here without the matching roster/excluded entry is caught at
`make check-harness` time, not discovered mid-window.
