# Lane `b42engines` — [B42] (a) research note 2: the engine capability and option landscape

Branch `lane/b42engines`, from master at `0d6e919`. Delivered 2026-09-12.
Charter: this lane's brief (research-only, no code, no design, no
`bench/`/`schema/`/`testees/`/`pcrecbench/` touch) — write
`docs/dev/research/2026-09-12-b42-engine-landscape.md`, one of [B42]
phase (a)'s three research lanes.

**Headline: the note is written, committed, and covers all eight asked
items.** Not built, not measured, not merged (a research lane by design).

## 1. Charter-vs-committed checklist

| item from the brief | committed | state |
|---|---|---|
| (1) obtainability + C-callable surface + licence, per engine | §1's table: apt package/version probed live on this box for every engine; RE2/Rust regex have NO native C API (would need vendoring `cre2`/`regex-capi`, same posture as pcrec's own shim — a finding, not assumed); licences cited per engine | DONE |
| (2) dialect/match semantics that could make PCRE2 and another engine disagree on the same pattern | §2: leftmost-first (pcre2/perl/python/oniguruma) vs POSIX-longest (RE2 optionally, TRE natively) vs Hyperscan's all-ends (a genuinely third shape, not a convention variant); empty-match/UTF-8/case-fold table | DONE |
| (3) unsupported constructs + how each engine reports them + size/complexity limits | §3's full table (backrefs/lookaround/atomic/recursion/conditionals/`\K`/Unicode props/repeat ceiling) with RE2's `ErrorCode` enum quoted verbatim from `re2.h`, Rust's `Error::CompiledTooBig(usize)`, Hyperscan's free-text `hs_compile_error_t`, python's structured `re.error`; §4's size/complexity dials (RE2 `max_mem`, Rust `size_limit`/`dfa_size_limit`, Hyperscan mode/SOM, pcre2 JIT/DFA-match/limits) | DONE |
| (4) space-vs-speed dials, 2-4 named configs per engine | §4's table, one "proposed configs" column per engine in the bench's own `<engine>-<axis-word>` slug style | DONE, with two engines (Oniguruma, TRE) explicitly left un-proposed pending a follow-up read (flagged, not guessed) |
| (5) compile-time definition per engine, comparability, size/memory | §5: per-engine phase proposal against the existing `cost_class` enum, with the finding that RE2/Rust-regex/Hyperscan all share a NEW shape (`cost_class`'s four tokens were defined against only pcrec+pcre2) and a recommendation (adapter-note caveat over a new enum value); artifact-size and peak-memory sub-sections with what each engine can/cannot expose | DONE |
| (6) syntactic-adjustment spelling table + equivalence-checking method + where it's NOT preserving | §6's table (7 rewrite rows) plus the finding that possessive/atomic-group rewrites on hazard-class patterns are usually NOT variants at all (the objective IS the hazard, and a linear-time engine answers it by construction) — ties directly to `requirements.md §4.5` constraint 2 | DONE |
| (7) capability model for record/reporter (finer outcomes, REQUIRES tags, scoreboard treatment of rewritten spellings) | §7's five numbered findings: today's `did-not-compile`+`unsupported-by-declaration` pair already covers every roster refusal (no new outcome value argued for); a proposed `refusal_class` metadata pair for engines with structured refusals; a proposed REQUIRES-tag policy turning §3's table into checkable sidecar fields; an explicit flag that Hyperscan's all-ends shape needs a ruling, not a lane guess | DONE |
| (8) questions for Frank, honesty about what's unverified | §8, 7 numbered questions, each cross-referenced to its flag in the body (rure/regex-capi buildability, `pcre2_dfa_match`'s true automaton class and restricted-construct list, Oniguruma/TRE size-refusal surfaces unread, the Hyperscan grain ruling, the cost_class fifth-token question, python/perl match-timing scope, peak-memory scope) | DONE |

Nothing is OWED. This lane made no code change and touched no file
outside `docs/dev/research/2026-09-12-b42-engine-landscape.md`.

## 2. What I did and did not verify

**Verified on this box** (commands in the note, not repeated here):
`apt-cache policy`/`search`/`show` for every candidate package,
`pkg-config --list-all`, `man pcre2jit` (installed `libpcre2-dev`
10.46-1build1). One box finding worth flagging to the manager
separately from the note's own §8: `libhyperscan-dev`/`libhyperscan5`
(the OLD Intel-sourced package, 5.4.2-4) and `libvectorscan-dev`/
`libvectorscan5` (5.4.11-2ubuntu2, source package `vectorscan`) are BOTH
in this box's archive and CONFLICT with each other at install time
(`vectorscan`'s package Replaces/Provides/Conflicts `libhyperscan-dev`).
Whichever [B42] build lane picks up Vectorscan should install
`libvectorscan-dev` by name, not `libhyperscan-dev` — installing the
wrong one first would need an uninstall/reinstall cycle to correct.

**Fetched from official sources** (all cited inline with URL and fetch
date 2026-09-12): RE2's own `re2.h` (ErrorCode enum, `max_mem` default,
`ProgramSize`), the `cre2` C-wrapper docs, Rust regex's `RegexBuilder`
and `Error` API docs, Hyperscan's compilation and API-files docs,
Oniguruma's `doc/API` (partial — see below), TRE's own documentation
site and GitHub repo, PCRE2's `pcre2_dfa_match` doc page, and licence
pages for every engine.

**NOT independently verified, flagged in the note's §8 rather than
guessed**: whether `rure`/`regex-capi` still builds against the current
`regex` 1.12 pin (I found the source tree, not a build); the exact
restricted-construct list and true automaton class of
`pcre2_dfa_match` (the fetched page states restrictions exist without
enumerating them); Oniguruma's and TRE's own size/complexity refusal
surfaces (their docs pages my fetches captured did not show a
memory-cap function/error code — this needs a second, deeper read of
`doc/API` and `tre.h`/`regcomp.c` respectively, past what a single
WebFetch call returned); Rust regex's exact default `size_limit` byte
value; whether Oniguruma or TRE support `\z` identically to
PCRE2/RE2/Rust. Each is a one-line flag in §8, not a blocking gap in the
note as delivered — the note says explicitly which claims rest on a
fetched primary source versus which are recommendations pending a
follow-up read.

## 3. For the design lane ([B42] phase (b))

The note's structure tracks the brief's eight items 1:1, so a reader
building `docs/design/capability_set_v1.md` can pull section-by-section.
The three findings I'd flag as most likely to shape the design rather
than just inform it:

1. **Two engines on the roster (python `re`, perl) do not fit the
   existing driver protocol at all without an embedding driver** (§1) —
   this is a scope decision, not a detail, and I recommend (§8 Q6)
   compile-cost-and-correctness-only for both in a v1 capability set.
2. **Hyperscan/Vectorscan's all-ends semantics is not a convention tag
   like `posix-leftmost-longest` — it changes what "the expectation" IS**
   (§2.2, §7 item 3), and needs an explicit ruling on whether the
   capability set narrows to a boolean grain for this engine or extends
   `capture_correspondence`-style machinery to an end-offset SET.
3. **`cost_class`'s four existing tokens were defined against exactly two
   engines (pcrec, pcre2) and the new roster has three engines
   (RE2, Rust regex, Hyperscan) that share a shape none of the four
   tokens quite names** (§5) — recommend an adapter-note caveat over a
   schema change, but it is the design note's call.

No code was written; no `bench/`, `schema/`, `testees/`, or
`pcrecbench/` file was touched; nothing here needs `make check` re-run.
