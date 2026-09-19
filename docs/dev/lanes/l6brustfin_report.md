# lane l6brustfin report — finishing the rust-regex adapter

**Task**: [B7]/L6b — finish `l6brust`'s OWED list now that pcrec's I-75
battery has cleared (battery done 15:34:36 EDT) and the box is free.
Continues `worktrees/l6brust`, branch `lane/l6brust` (predecessor head
`6dd3a57`, two commits). Does NOT merge.

## What this lane found on arrival

The predecessor's detached post-battery pipeline (`setsid ... & disown`,
PID 1902616, per BOILERPLATE.md's marker rule — checked FIRST, before any
other action) had already finished cleanly:
`l6brust_postbattery.log` ends `DONE rc=0`. rustup installed (stable,
`--profile minimal`, home-only, no sudo); the first `cargo build --release`
(no `--locked`) generated `Cargo.lock`; the capability census ran to
completion (`census rc=0`) and archived its raw stdout to
`l6brust_capability_census_raw.txt` (193 lines) in the session scratchpad.
Nothing had been committed or judged yet — that is this lane's work.

## What this lane did

1. **Committed `testees/rust/Cargo.lock`** (`regex 1.13.1`,
   `regex-automata 0.4.18`, `regex-syntax 0.8.11`, `aho-corasick 1.1.5`,
   `memchr 2.8.3`) and filled every toolchain-version placeholder in
   `testees/rust/CLAUDE.md` with the probed, not typed, values: `rustc
   1.98.1 (48a229cea 2026-09-01)`, `cargo 1.98.1 (797e8a9bc 2026-08-05)`.
   `df -h /`: 30G avail/69% used BEFORE (this lane's own earlier
   measurement) → 28G avail/71% used AFTER the first build (~1 GB for
   rustup + the release build together).

2. **Archived the census** as
   `docs/dev/measurements/2026-09-19-rust-capability-census-r1131.txt`
   (D35 style: source header naming the script, the pinned toolchain and
   crate versions, the box, the bench commit, disk before/after; the
   verbatim stdout block is BYTE-IDENTICAL to the raw scratchpad file —
   diffed to confirm before committing, not retyped from memory — plus
   four appended witness runs this lane ran directly against the built
   driver, described next). `docs/dev/measurements/CLAUDE.md`'s entry
   for `probe_rust_capability_census.py` updated from "NOT YET RUN" to
   the real headline.

3. **Judged the census, with new witness evidence beyond the compile-only
   pass:**

   a. **`possessive-quantifier` — WITHHELD on a semantic finding, NOT
      trusted from the fact that it compiles.** The census shows `a++`
      COMPILES. This lane ran the actual discriminating witness directly
      against the built driver: pattern `(?:a++)a` over subject "aaa"
      answers `match [0,3)` — the WHOLE subject. Under PCRE's true
      possessive semantics, `a++` would consume all three `a`s with no
      backtracking available to release one for the trailing `a`, so the
      match would FAIL outright (and no other start offset has enough
      `a`s either — the pattern would report nomatch on "aaa" entirely).
      It matched. VERDICT: the crate's automaton-based engine has no
      backtracking to forbid in the first place, so `a++` behaves
      exactly like `a+` — the syntax parses for PCRE-pattern portability
      with NO operational effect. `possessive-quantifier` is excluded
      from the `EXT_BENCH_ROSTER` row on this evidence, correcting the
      earlier N2-sourced prediction (which had guessed REFUSED).

   b. **The I-72 high-byte refusal — CONFIRMED**, both from the census
      and a direct `tools/selfcheck.py` run (new arm 1e, below):
      `mojibake-curly-quote` refuses with
      `[syntax/InvalidUtf8Pattern] pattern is not valid UTF-8 at byte 0:
      invalid utf-8 sequence of 1 bytes from index 0` — the driver's own
      pre-regex-crate validation, never a crash, never the `regex`
      crate's own error type. Distinguished from `non-utf8-subject`
      (a SUBJECT-side fact this adapter satisfies structurally): the
      constraint here is that the PATTERN SOURCE must itself be valid
      UTF-8 (`regex::bytes::RegexBuilder::new` takes `&str`, never
      `&[u8]`, for the pattern), which has no token of its own in
      capability_set_v1.md's vocabulary. Cross-checked against every
      OTHER refused `bench/capability` pattern: all 21 remaining
      refusals tie to a withheld `REQUIRES_VOCAB` token by name (script
      run in this lane, not eyeballed) — `mojibake-curly-quote` is the
      one, explained exception.

   c. **The `\xHH`-under-unicode-mode discrimination pass — RESOLVED.**
      The reasoned hypothesis was right: under `rust-default`'s
      unmodified (unicode mode ON) config, `[\x80-\xff]` matches a
      codepoint's UTF-8 ENCODING, not a raw byte (`nomatch` against the
      raw byte 0x93, `match [0,2)` against its two-byte encoding `C2
      93`); only `(?-u:...)`-wrapped classes match the raw byte
      (`match [0,1)`). Disposition: `non-utf8-subject` stays SATISFIED
      at the structural/API level the token's own definition names ("the
      subject bytes are not valid UTF-8" — the driver never refuses or
      panics on a genuinely invalid-UTF-8 haystack, confirmed by the
      clean `nomatch` above, not an error), with the semantic caveat
      documented prominently in `testees/rust/CLAUDE.md` so a future
      `high-byte-run` mismatch under this config reads as the expected,
      documented divergence rather than a surprise.

   d. **The 17-token table, completed with per-token evidence**: 8
      SATISFIED (`unicode-properties`, `named-groups`, `free-spacing`,
      `span-reporting`, `non-utf8-subject`, `captures`,
      `true-end-anchor`), 9 REFUSED (`backrefs`, `lookaround`,
      `lookbehind-variable`, `atomic-group`, `recursion`,
      `conditionals`, `k-reset`, `control-verbs`, `callouts`, all
      `[syntax/Syntax]`, all matching N2's prediction), 1 WITHHELD on
      semantics (`possessive-quantifier`, (a) above). Corpus headline:
      `bench/capability@0.1` **42/64 compiled**, 22 refused (21 tied to
      a withheld token by name, 1 the documented I-72 exception);
      `bench/syntax@0.1` **50/95 compiled**, 45 `Syntax` refusals
      (informational cross-check, not capability-gated).

4. **`EXT_BENCH_ROSTER` row + regenerated `patterns.rxt`**
   (`bench/capability/gen_patterns.py`): the `rust-default` row (8
   tokens), with a full prose comment following RE2/onig/TRE/Vectorscan
   precedent (every REFUSED/WITHHELD/SATISFIED token cited to its own
   witness). `python3 bench/capability/gen_patterns.py` then
   `--check` (exit 0) — the diff touches only the new `ext bench`
   roster line and the `capabilities rust-default` block, nothing else
   in the 64-pattern table moved.

5. **Landed `check_high_byte_pattern_argv` arm 1e** in
   `tools/selfcheck.py`, exactly as designed in `testees/rust/CLAUDE.md`
   (a THIRD shape: neither "compiles and matches" nor "matches at
   boolean grain" — a clean `did-not-compile` naming byte offset 0, plus
   the corrupted-spelling control). Verified standalone (below), not
   merely written: **9/9 PASS**, including the two new rust lines.
   `tools/CLAUDE.md` updated with the arm's own addendum paragraph.

6. **Confirmed, by direct witness, not memory:**
   - **leftmost-first**: `foo|foobar` over "foobar" → `match [0,3)`
     (the first alternative wins), run directly against the built
     driver. Structurally backed too: `MatchKind::LeftmostFirst` is
     HARDCODED (not merely defaulted) in the pinned crate's own
     `Builder::build_one_bytes()` (`regex-1.13.1/src/builders.rs`).
   - **`size_limit`/`dfa_size_limit` defaults**: read directly from the
     downloaded crate SOURCE (never docs.rs, never memory) —
     `.nfa_size_limit(Some(10 * (1 << 20)))` = 10,485,760 = 10 MiB,
     `.hybrid_cache_capacity(2 * (1 << 20))` = 2,097,152 = 2 MiB,
     matching `src/main.rs`'s constants and the driver's own printed
     `info` lines exactly.
   - **The thread-based per-subject timeout**: forced with a synthetic
     no-match subject at `--iters 200000000 --subject-timeout 1` →
     `timedout` reported cleanly at the 1-second boundary, process exits
     0, no hang, no crash.

7. **Quick smokes** (scratch tier, `build/scratch-store/`, both
   validator-accepted and written):
   - `search` regime, `email`/`orig`, 5 subjects, vs `pcre2-jit`: 5/5
     pass both testees, `rust-default` 1503.2 ns/call vs `pcre2-jit`
     477.3 ns/call (rust-default 3.15× slower on this cell — no
     ranking claim, a scratch smoke).
   - `match` regime, same pattern/subjects: 5/5 pass both, `rust-default`
     (whole-subject form, the `\A(?:...)\z` wrap) 915.7 ns/call vs
     `pcre2-jit` 3158.8 ns/call (rust-default 3.45× FASTER here) — the
     wrap correctly renders as `form=whole-subject` in the record, the
     driver's own anchor-baking design working end to end.

8. **Light gates run** (per this lane's brief, NOT the full
   `make check-harness`, which is the manager's job at merge):
   `make check-schema` — 5 examples accepted, 73 sabotages rejected for
   their own rule, 0 wrong (unchanged baseline); `python3 -m pcrecbench
   testees` — `rust-default` lists cleanly with a correct description;
   `check_high_byte_pattern_argv()` run standalone — 9/9 PASS.

## Charter-vs-committed checklist (BOTH halves, session_discipline.md §7(c))

| brief item | status |
|---|---|
| the driver protocol, read in full, followed | done — `src/main.rs`'s header cites the exact protocol shape |
| no lookaround/backrefs, withheld tokens with evidence | done — 9 tokens witnessed REFUSED, `[syntax/Syntax]` each, N2's prediction held |
| guarantees linear time; give-up surface documented | done — `GAVE_UP_CODES` empty by construction |
| size_limit/dfa_size_limit as config axes only if census motivates | done — census ran, motivates NO second config yet; `rust-smallsize` correctly not built |
| matches on bytes via regex::bytes; unicode flag posture; leftmost-first convention | done — leftmost-first WITNESSED (`foo|foobar` → `[0,3)`) and structurally confirmed; unicode-mode posture fully resolved (item 3c above) |
| one config `rust-default` first | done |
| the driver + adapter | done — authored AND built (rustc 1.98.1, cargo 1.98.1, regex 1.13.1) |
| `testees/rust/CLAUDE.md` | done — every section updated from prediction to witnessed finding |
| capability census over bench/capability, 17-token table with evidence | done — 8 SATISFIED / 9 REFUSED / 1 WITHHELD-on-semantics, archived |
| EXT_BENCH_ROSTER wiring + regenerated patterns.rxt | done — `gen_patterns.py --check` exit 0 |
| the high-byte witness | done — I-72 refusal witnessed with the exact predicted diagnostic; the pattern-source-UTF-8 vs subject-side `non-utf8-subject` distinction confirmed both ways |
| selfcheck arm | done — landed AND verified standalone, 9/9 PASS |
| quick smokes vs pcre2-jit once the box frees | done — two regimes, 5/5 both, scratch-store records validator-accepted |
| the possessive-quantifier semantics finding | done — real match witness settles it: NOT possessive, withheld on that evidence |
| leftmost-first + size_limit defaults confirmed against the pinned crate | done — both by direct witness/source read, not docs-from-memory |
| charter-vs-committed checklist | this table |
| head SHA | see "Handback" below (this lane's commit, on top of `6dd3a57`) |
| the df numbers | done — 30G/69% before, 28G/71% after (~1 GB) |

Nothing remains OWED from either half's brief.

## Handback

Branch `lane/l6brust`, this lane's commit on top of predecessor head
`6dd3a57` (see `git log -1` on the branch for the exact SHA — this
report and every file above land in the same commit set). Files touched
this lane: `testees/rust/Cargo.lock` (new), `testees/rust/CLAUDE.md`
(every OWED/predicted section resolved), `testees/CLAUDE.md` (rust row
updated to BUILT/CENSUSED), `bench/capability/gen_patterns.py` +
`bench/capability/patterns.rxt` (the `rust-default` roster row),
`tools/selfcheck.py` + `tools/CLAUDE.md` (arm 1e),
`docs/dev/measurements/2026-09-19-rust-capability-census-r1131.txt`
(new) + `docs/dev/measurements/CLAUDE.md` (its entry updated), this
report.

**NOT run this lane** (per the brief, deliberately): `make
check-harness`/`make check` — the manager's job at merge, now expected
to be a real discovery pass (the FIRST time the `rust` adapter has ever
built) rather than a formality; the predecessor's `check_driver_smokes`
warning about running `check-harness` before the build lands NO LONGER
APPLIES (`Cargo.lock` is committed, `cargo`/`rustup` are on this box),
but the manager should still budget it as a real pass, not assume green.
This lane's own light-gate results (check-schema, `testees`, the
selfcheck arm run standalone) are reported above as a partial substitute,
not a replacement for the full suite.

This lane does not intend to poll or stay warm further — everything
promised is either committed or explicitly stated done above; no
background job is outstanding.
