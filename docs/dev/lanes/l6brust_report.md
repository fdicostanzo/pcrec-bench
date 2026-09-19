# lane l6brust report — the rust-regex adapter (`testees/rust/`)

**Task**: [B7]/L6b — build the rust-regex adapter, the last unchartered
`[B7]`-roster engine, completing the L6b wave (RE2/Oniguruma/TRE/
Vectorscan landed 2026-09-17).

**Branch**: `lane/l6brust`, one commit (`939f442`), `worktrees/l6brust`.

**HEADLINE: AUTHORED, NOT YET BUILT OR CENSUSED.** pcrec's I-75 battery
held the box for the entire session (BOILERPLATE.md's HARD RULE — no
`rustup` install, no `cargo build`, no capability census run). Every
design decision below is my own best-effort reading of the `regex`
crate's public API and this project's own precedent, cross-checked as
carefully as I could manage without a compiler (`python3 -m py_compile`
on both new `.py` files, `tomllib.load` on both new `.toml` files,
`_ad.discover()` + `python3 -m pcrecbench testees` confirming the adapter
registers cleanly and lists `rust-default`, `make check-schema` confirmed
unaffected — 5/73/0, matching the current tree) — but **nothing Rust has
been compiled, no capability claim is witnessed, and Cargo.lock does not
exist.** A detached background pipeline is running now, waiting for the
battery to clear and then doing the build + census automatically; see
"OWED" below for its exact state and how to resume.

## What was built

- `testees/rust/src/main.rs` — a NATIVE Rust driver (never a C driver
  linked against a C ABI — the `regex` crate has none worth adding as a
  dependency, per inbox I-76's own closing line: "no 'cargo install
  line' concern exists on our side"). Implements the shared protocol
  (`pcrecbench/adapters.py`'s docstring) byte for byte against
  `testees/re2/driver.cc`/`testees/onig/driver.c`'s reference shape.
  Rust-specific decisions, each documented in the file's own header and
  in `testees/rust/CLAUDE.md`:
  - `regex::bytes::{Regex, RegexBuilder}` throughout (byte-haystack
    matching — the escape hatch for `non-utf8-subject` at the SUBJECT
    level; the PATTERN itself must still be valid UTF-8, a *different*,
    structural constraint the driver validates explicitly before ever
    calling into the crate, reporting a clean `did-not-compile` naming
    the exact byte offset rather than panicking).
  - No dual match-invocation the way `testees/onig/driver.c` needs
    (`onig_match` vs `onig_search`): the crate has no runtime
    anchored-search option at all, so `adapter.py` bakes BOTH anchors
    into the compiled text for the whole-subject form (`\A(?:pattern)\z`
    — NOT `pcrecbench.record.whole_subject_text()`'s `(?:pattern)\z`,
    which would under-anchor here). `--form`/`--mode` are still accepted
    and cross-checked for protocol-shape parity; they do not change this
    driver's control flow.
  - The per-subject `--subject-timeout` is a THREAD + channel
    (`recv_timeout`), never a signal/`longjmp` pair — mixing `longjmp`
    with Rust stack frames is undefined behavior (it skips destructors
    and violates the unwinding invariants Rust's own panic-across-FFI
    docs warn about). Documented as a deliberate, reasoned deviation
    from every other driver in this project, justified by the crate's
    own linear-time guarantee (a timeout here can only be provoked by
    raw input SIZE, never catastrophic backtracking).
  - `regex::Error`'s two variants (`Syntax`, `CompiledTooBig`) read by
    stable `Debug` name (the type is `#[non_exhaustive]`) rather than an
    exhaustive `match`.
- `testees/rust/adapter.py` — `describe`/`prepare`/`compile`/`measure`;
  `prepare_driver()` runs `cargo build --release --locked` (never
  `pcrecbench.driverrun.build_driver()`, a C-compiler assumption — the
  same route `testees/re2/adapter.py`'s g++ step sets precedent for);
  `engine_version` is read from the COMMITTED `Cargo.lock`'s own `regex`
  package entry (parsed with the stdlib `tomllib`, never typed) since the
  crate exposes no runtime version API (the same absence class RE2's own
  `_probe_version` docstring states); `rustc --version` rides in
  `build_flags` for toolchain provenance.
- `testees/rust/Cargo.toml` — `regex = "1"` (a semver REQUIREMENT, not
  the pin — Cargo.lock, generated at the first build, is the pin per
  inbox I-76's own wording).
- `testees/rust/configs.toml` — `rust-default` only (the brief's own
  instruction: "One config `rust-default` first; more only if the census
  motivates"). `rust-smallsize` (capability_set_v1.md §8's
  `regex-smallsize` row: a low `size_limit`) is documented, not wired.
- `testees/rust/CLAUDE.md` — every required section, all four deliverable
  points from the brief, PLUS two findings this lane made by reasoning
  about the crate's documented semantics (both explicitly marked
  UNVERIFIED, to be settled by the census, not asserted):
  1. **The I-72 finding**: this project's own shared high-byte witness
     pattern (`tools/selfcheck.py`'s `PAT = b"\x93[\\x20-\\x7e]*\x94"` —
     confirmed by inspecting the literal, a RAW byte 0x93/0x94 pair, not
     an ASCII escape; matches `bench/capability/patterns/mojibake-curly-
     quote.rx`'s own on-disk bytes byte for byte, confirmed with `xxd`)
     is predicted to REFUSE under `rust-default` — not a bug, a genuine
     structural fact: `regex::bytes::RegexBuilder::new` takes `&str`,
     never `&[u8]`, for the pattern SOURCE, and a lone byte 0x93 is not
     valid UTF-8.
  2. **An open, unresolved question**: whether `unicode(true)` (the
     default, needed for `unicode-properties`) makes `\xHH`/a
     `[\x80-\xff]`-style class match the UTF-8 ENCODING of that codepoint
     rather than the raw byte — which would mean `non-utf8-subject` and
     `unicode-properties` are not simultaneously free the way they are
     under RE2's `EncodingLatin1` or Oniguruma's `ONIG_ENCODING_ASCII`.
     `docs/dev/measurements/probe_rust_capability_census.py`'s
     `census_nonutf8_discrimination()` is built specifically to settle
     this with a real MATCH run (compiling proves nothing here — both
     readings compile fine), testing both a plain class and a
     `(?-u:...)`-wrapped one against both a raw-byte and a
     UTF-8-encoded-codepoint subject.
- `docs/dev/measurements/probe_rust_capability_census.py` — the fourth
  L6b capability census, same shape as the other three (one witness per
  `REQUIRES_VOCAB` token, all 64 `bench/capability` + 95 `bench/syntax`
  corpus patterns through the real adapter), plus the discrimination pass
  above. **Written, syntax-checked (`py_compile`), NOT YET RUN.**
- `testees/CLAUDE.md`, `docs/dev/measurements/CLAUDE.md`, `.gitignore`
  (`testees/rust/target/` — the one-time manual first build's own
  default output dir) updated.

## A real finding from static verification: `check_driver_smokes` WILL FAIL until the build lands

`tools/selfcheck.py:check_driver_smokes` (part of `make check-harness`)
iterates **every** discovered adapter (`for engine, adapter in
sorted(_ad.discover().items())`) and calls `adapter.prepare(tid, tmp)`
unconditionally. Discovery now finds `rust` (confirmed live:
`python3 -m pcrecbench testees` lists `rust-default`), so `make
check-harness` run on this branch **before** `testees/rust/Cargo.lock`
exists and `cargo`/`rustup` are installed will report a `bad("rust
driver smoke", ...)` failure — a real, structural consequence of adding
this adapter, not a bug in it. **Do not run (or expect green from) `make
check-harness` on this branch until the OWED build below has landed and
Cargo.lock is committed.** This is exactly the box-hold sequencing the
brief anticipated (BOILERPLATE.md's HARD RULE + this lane's brief:
"AUTHORING ONLY... until its trailer prints `== BATTERY DONE`") — stated
explicitly here so it is not rediscovered the hard way at merge time.

## Disk before install (I-76's own ask)

    $ df -h /            (2026-09-19, 11:09 EDT, before any rustup activity)
    /dev/mapper/ubuntu--vg-ubuntu--lv   98G   64G   30G  69% /

Matches I-76's own cited figure ("69% at 08:41 today"). **`df -h /` AFTER
the first build is OWED** — the detached pipeline below records it.

## The detached post-battery pipeline — RUNNING NOW, OWED

Per BOILERPLATE.md's DO-THEN-FINISH rule (a run this long is the lane's
last act): a script is running DETACHED (`setsid bash ... & disown`,
PID **1902616** at launch, session leader, confirmed alive with `ps -p
1902616` immediately before this report was written), polling pcrec's
battery trailer every 60 s:

    /home/duxevents/pcrec/build/battery_923a5a58/trailer.log
    -- waits for the line "== BATTERY DONE" (battery.sh's own exact
       trailer spelling, confirmed by grep against pcrec/scripts/
       battery.sh, read-only)

Once it fires, the script (session-scratchpad only, never committed —
**it is NOT tracked by the harness's background-task notifier**, since
it was launched with `setsid ... & disown`, not `run_in_background`; per
BOILERPLATE.md, no notification will ever arrive for it — the MARKER
below is the only source of truth):

1. records `df -h /` (BEFORE, again, for the record)
2. installs rustup (home-only, no sudo, `stable` channel, `--profile
   minimal` per I-76's disk-watch instruction)
3. records `rustc --version` / `cargo --version` (the exact toolchain pin
   `testees/rust/CLAUDE.md`'s placeholders are waiting for)
4. runs the FIRST `cargo build --release` **without** `--locked` (the
   adapter's own `prepare_driver()` always passes `--locked`, which
   requires `Cargo.lock` to already exist — this manual first build is
   what GENERATES it; every subsequent adapter-driven build enforces the
   pin via `--locked` once the lockfile is committed)
5. records `df -h /` AFTER
6. prints the `Cargo.lock` `regex` package entry (the pin itself)
7. runs `docs/dev/measurements/probe_rust_capability_census.py`,
   archiving raw stdout/stderr

**Log** (poll this, not `ps`, per BOILERPLATE.md's marker rule):

    /tmp/claude-1001/-home-duxevents-pcrec-bench/a1aa0dcc-4ad9-409e-98b1-76c1d74fd2c6/scratchpad/l6brust_postbattery.log

**Completion line**: `DONE rc=<code>` (0 == the census script ran to
completion; a nonzero code names which step failed — the log's own
section headers say which). **Census raw output** (once `DONE` appears):

    /tmp/claude-1001/-home-duxevents-pcrec-bench/a1aa0dcc-4ad9-409e-98b1-76c1d74fd2c6/scratchpad/l6brust_capability_census_raw.txt

As of this report, the log reads only its start line and "waiting for
the battery trailer" — the battery was still in its `san` stage
(started 10:33 EDT) when this lane ended.

**What the script deliberately does NOT do** (judgment work for a
follow-up turn, not a blind script edit):

- commit anything (Cargo.lock, the census archive) — a human/agent
  reviews the output first
- edit `bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER` (needs the
  census's real findings written up in prose, the L5 discipline)
- add the `check_high_byte_pattern_argv` arm to `tools/selfcheck.py`
  (designed in full in `testees/rust/CLAUDE.md`'s "Smoke coverage"
  section — the exact code is written there, just not landed)
- fill in `testees/rust/CLAUDE.md`'s version placeholders
- resolve the `rust-smallsize` question (needs the census's own refusal
  census to motivate it, per the brief)

## OWED (exact steps for the manager or a fresh agent, once the marker shows DONE)

1. **Check the marker first, always**: `tail -30
   /tmp/claude-1001/.../scratchpad/l6brust_postbattery.log` (path above)
   — look for `DONE rc=`.
2. If `rc=0`: read `testees/rust/CLAUDE.md`'s toolchain-version
   placeholders in with the recorded `rustc --version`/`cargo --version`
   lines; `git add testees/rust/Cargo.lock` and commit (the crate's pin,
   inbox I-76).
3. Read the census archive
   (`l6brust_capability_census_raw.txt`), resolve the `non-utf8-subject`
   open question from its `census_nonutf8_discrimination()` section, and
   write the real `EXT_BENCH_ROSTER` row in `bench/capability/
   gen_patterns.py` (following the RE2/onig/TRE/Vectorscan precedent:
   witnessed findings only, every REFUSED/SATISFIED token cited to its
   own witness line) — then `python3 bench/capability/gen_patterns.py`
   to regenerate `patterns.rxt`, `gen_patterns.py --check` to confirm.
4. Add the `check_high_byte_pattern_argv` arm to `tools/selfcheck.py`
   (the exact code is in `testees/rust/CLAUDE.md`'s "Smoke coverage"
   section) and verify it in isolation before landing.
5. `make check-harness` (and `make check`) — expected to be a real
   discovery step this time (unlike RE2/onig/TRE/Vectorscan's own "a
   formality, not a discovery step" notes), since this is the first time
   the `rust` adapter has ever been built or run: **do not run this**
   until steps 2-4 above are done (see the `check_driver_smokes` finding
   above — it WILL fail on an unbuilt/uncensused rust-default).
6. `quick --subbench email --pattern orig --regime search --testee
   rust-default --vs pcre2-interp --subjects 5` — a scratch smoke,
   mirroring every sibling L6b lane's own verification, once 2-5 are
   clear.
7. Confirm `foo|foobar` over `"foobar"` answers `[0,3)` (the
   `perl-leftmost-first` claim, capability_set_v1.md §7.6's own "not
   independently reproduced" flag — `testees/rust/CLAUDE.md`'s (d)
   section names this explicitly as owed).
8. Reconfirm `RegexBuilder::size_limit`/`dfa_size_limit`'s documented
   defaults (10 MiB / 2 MiB, `src/main.rs`'s own constants) against
   whatever version `Cargo.lock` actually pins — `testees/rust/
   CLAUDE.md`'s (c) section names this explicitly.

## Charter-vs-committed checklist (session_discipline.md §7(c))

| brief item | status |
|---|---|
| the driver protocol, read in full, followed | ✅ done — `src/main.rs`'s header cites the exact protocol shape it mirrors |
| no lookaround/backrefs, withheld tokens with evidence | ⏳ OWED — predicted in `CLAUDE.md` from N2's research citation, NOT yet independently witnessed (no census run) |
| guarantees linear time; give-up surface documented | ✅ done — `GAVE_UP_CODES` empty by construction, reasoned in full |
| size_limit/dfa_size_limit as config axes only if census motivates | ⏳ correctly deferred — no census yet, so `rust-smallsize` correctly NOT built |
| matches on bytes via regex::bytes; unicode flag posture; leftmost-first convention | ✅ documented; the leftmost-first witness itself is OWED (item 7 above) |
| one config `rust-default` first | ✅ done |
| the driver + adapter | ✅ authored; ⏳ UNBUILT (battery hold) |
| testees/rust/CLAUDE.md | ✅ done |
| capability census over bench/capability, 17-token table with evidence | ⏳ script authored and ready; NOT YET RUN (battery hold) — the single largest OWED item |
| EXT_BENCH_ROSTER wiring + regenerated patterns.rxt | ⏳ OWED — needs the census's real output, deliberately not guessed |
| the high-byte witness | ✅ reasoned through fully (both the structural I-72 immunity and the DIFFERENT pattern-UTF-8 limitation this project's own shared witness hits); ⏳ live confirmation OWED |
| selfcheck arm | ✅ designed in full in CLAUDE.md; ⏳ NOT landed in `tools/selfcheck.py` (needs a working build to verify against) |
| quick smokes vs pcre2-jit once the box frees | ⏳ OWED, listed above |
| charter-vs-committed checklist | ✅ this table |
| head SHA | `939f442` |
| the df numbers | ✅ BEFORE recorded above; ⏳ AFTER is in the detached pipeline |

## Handback

Branch `lane/l6brust` at `939f442`, committed, this report committed in
the same commit set. **Do not merge and run `make check-harness` in the
same breath** — see the `check_driver_smokes` finding above; the
manager's own merge-then-verify sequencing should land this branch,
THEN wait for (or resume) the detached pipeline's `DONE` marker, THEN do
steps 2-6 of "OWED" before trusting a `make check-harness` result either
way. This lane does not intend to poll further — a fresh agent or the
manager checks the marker log named above.
