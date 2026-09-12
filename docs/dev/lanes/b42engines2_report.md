# Lane `b42engines2` — [B42] follow-up 2: closing research note 2's §8 questions by fact

Branch `lane/b42engines2`, from master at `b1ee293`. Delivered 2026-09-12.
Charter: research-only follow-up to lane `b42engines`'s
`docs/dev/research/2026-09-12-b42-engine-landscape.md` — close as many of
its §8 "questions for Frank" as are FACTS derivable from upstream
source/docs or this box's own packages, not rulings, then amend the SAME
note in place. No code, no `bench/`/`schema/`/`testees/`/`pcrecbench/`
touch, no package installs, no build, no measurement.

**Headline: 6 of 8 §8 items closed by fact; the note amended in place
with inline "(confirmed by b42engines2: …)" notes at every §1-§7 location
a claim changed, plus a new "Follow-up 2026-09-12 (lane b42engines2)"
section at the end with the full derivation and an install list for
Frank. Not merged.**

## 1. Charter-vs-committed checklist

| ask from the brief | committed | state |
|---|---|---|
| (1) Rust regex C API: `regex-capi`/rure buildability against 1.12, crates.io status, vendored-build shape | `regex-capi/Cargo.toml` fetched (path-dep on sibling `regex` crate — always tracks the checkout, no version negotiation); `rure` confirmed to exist on crates.io (one release, 0.2.5, 2016); cargo/rustc apt candidates confirmed, neither installed | DONE |
| (2) RE2's C wrapper: cre2's build system/last release/RE2 range/absl issues; C++ direct-driver alternative; does the protocol constrain language | cre2: autotools, NO committed `configure` (needs autoconf/automake/libtool), zero GitHub releases ever, README states "tested with... 2024-07-02", no absl issues found on its tracker; `libre2-dev` on this box already `Depends: libabsl-dev` (RE2 IS abseil-dependent here); `adapters.py`'s protocol re-read in full — no language constraint, `driverrun.py:115-140`'s `build_driver()` is a convenience, not a requirement; g++/clang++ already installed | DONE — recommend the direct C++ route over cre2 |
| (3) `pcre2_dfa_match`'s restricted constructs + `PCRE2_INFO_*` size surfaces | `man pcre2matching` quoted in FULL (the numbered restriction list, items 1-8) and `man pcre2_dfa_match`; the automaton-class question closed FROM THE SAME MAN PAGE ("not implemented as a traditional finite state machine... keeps multiple states active simultaneously" = nfa-simulation, never dfa-only) — no `pcre2_dfa_match.c` source read needed after all; full `PCRE2_INFO_*` list grepped from this box's `/usr/include/pcre2.h` | DONE |
| (4) Oniguruma: ONIGERR_* codes, retry/parse-depth/nest-level limit knobs + defaults, `\z`/`\Z`/`\A` support, ONIG_SYNTAX_PERL_NG's construct set, size accessor | `doc/API`, `src/oniguruma.h`, `doc/RE`, `src/regsyntax.c` all fetched at tag v6.9.10; six limit functions with defaults, eleven ONIGERR_* codes, `\A`/`\Z`/`\z` confirmed under the default syntax; `OnigSyntaxPerl_NG`'s own op2 bitmask read directly — 4/6 asked features confirmed by a named flag (possessive, backref via `\k<name>`, `\g<name>` recursion, `(?(if)...)` conditionals), atomic/lookbehind lower-confidence (not gated by a distinct flag in that table); confirmed NO size/memory accessor exists anywhere in `doc/API` | DONE |
| (5) TRE: tre.h/regcomp.c/tre-internal.h REG_* codes, size bounds (correcting the ~50K/20K/2K figures), `\z` support, backref support, size-limit param on tre_regcomp | `include/tre/tre.h`, `lib/tre-internal.h`, `lib/regcomp.c`, `lib/tre-parse.c` all fetched from `laurikari/tre` master; full `reg_errcode_t` list; the REAL bounds are `TRE_MAX_RE`=65536, `TRE_MAX_STRING`=INT_MAX, `TRE_MAX_STACK`=1,048,576 — the note's ~50K/20K/2K figures could not be re-verified (their likely source page 500'd) and are flagged UNCONFIRMED rather than silently repeated; backrefs confirmed present (`BACKREF` AST node in `tre-parse.c`'s `PARSE_ATOM`); `\z`/`\A`/`\Z` confirmed ABSENT (no case in the escape switch) | DONE |
| (6) Vectorscan: dev-reference Pattern Support page, HS_FLAG_* incl. SOM_LEFTMOST cost, hs_expr_info_t fields, HS_COMPILER_ERROR shape, `\z` support | VectorCamp's own `dev-reference/compilation.rst` fetched — its unsupported-construct list is VERBATIM identical to Intel Hyperscan's page (the fork carries the same restrictions, not a divergent set); `hs_expr_info_t`'s five fields and `hs_compile_error_t`'s two fields quoted from Intel's `api_files.html`; `\z` confirmed SUPPORTED on both pages | DONE |
| (7) Rust regex compiled-size accessor: does `regex-automata`'s `meta::Regex::memory_usage()` exist in 1.12, and does `regex::Regex` have one | `regex_automata::meta::Regex::memory_usage(&self) -> usize` CONFIRMED to exist (docs.rs, full signature+doc quoted); `regex::Regex`'s full method list checked — NO such method — meaning a `rure`-based testee (which wraps `regex`, not `regex-automata`, per its own Cargo.toml) cannot expose this number without an upstream patch, out of scope here | DONE |
| (8) python `re`/perl: CPython 3.14 possessive/atomic (3.11+), variable-length lookbehind status, `re.compile` cache size; perl 5.40 `qr//`/`use re 'eval'` scope note | CPython 3.14 docs fetched directly (not a secondary source): both features confirmed "Added in version 3.11"; lookbehind confirmed fixed-width-only, quoted; cache size confirmed to have NO published numeric guarantee (qualitative wording only) — any specific figure is an implementation detail, not re-verified from source this session; perl paragraph reviewed, no new finding, recorded as reviewed rather than silently skipped | DONE |
| (9) THE INSTALL LIST: every apt package + toolchain, installed/not, `libvectorscan-dev` vs `libhyperscan-dev` conflict, one recommended `sudo apt install` line | Full table in the follow-up section: cargo/rustc/libabsl-dev/autoconf/automake/libtool/pkg-config/libre2-dev/libonig-dev/libtre-dev/libvectorscan-dev/libhyperscan-dev/g++/clang/cmake/python3-regex, each with candidate version and installed y/n; the conflict restated with the "install libvectorscan-dev, never libhyperscan-dev alongside it" rule; one recommended line (`sudo apt install libonig-dev libtre-dev libvectorscan-dev libabsl-dev`), cargo/rustc called out separately; NOTHING was run | DONE |

Nothing is OWED. This lane touched only
`docs/dev/research/2026-09-12-b42-engine-landscape.md` (amended in place)
and this report.

## 2. A mandate near-miss, caught and corrected

My first round of inline edits landed on the MAIN checkout's copy of the
research note (`/home/duxevents/pcrec-bench/docs/dev/research/...`)
instead of the worktree's — an absolute-path slip, not a deliberate
scope violation. Caught immediately via `git status`/`git diff --stat`
in the main tree right after the first commit attempt failed with
"nothing to commit" (the tell). Fix: captured the diff with `git diff
... > scratchpad-file`, `git checkout --` the main tree's copy back to
clean, then `git apply` the SAME diff inside `worktrees/b42engines2`.
Verified `git status` clean in the main tree and the diff present in the
worktree before continuing. Every edit after that point used the
worktree's absolute path explicitly. Flagging this so the manager can
watch for the same failure mode in other lanes that start from a fully
-specified absolute path pattern learned from a shared context.

## 3. What's still genuinely for Frank (unchanged by this follow-up)

Four of the original note's seven "questions for Frank" are rulings, not
facts, and stay open exactly as posed — restated with any new context in
the follow-up section's closing list:

1. Hyperscan/Vectorscan's all-ends semantics: span-grain declared variant
   vs. a narrowed boolean grain for this one engine.
2. The `cost_class` fifth-token question (a new
   `eager-with-lazy-runtime` value vs. adapter-note prose) — this
   follow-up's independent confirmation that RE2/Rust/Hyperscan all
   share the same "eager-but-partial" compile shape makes the case for
   *a* fix stronger, but which fix is still Frank's call.
3. Whether python `re`/perl are in scope for match timing at all in v1
   (the embedding-driver cost).
4. Peak-memory (`ru_maxrss`) recording scope.

## 4. For [B42] phase (b)

The design note can now cite primary sources directly for every item in
this brief rather than treating them as open threads — in particular,
`pcre2-dfa`'s `automaton_class` tag (`nfa-simulation`) and its full
restricted-construct list are settled from this box's own man pages with
no further source read needed, and the RE2 wrapper decision has a
concrete recommendation (direct C++ driver, not `cre2`) with the apt
packages named either way.
