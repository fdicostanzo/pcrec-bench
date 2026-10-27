# unusual_set_v1 -- realistic patterns using UNUSUAL features (plan row [B148], inbox I-165/I-166)

STATUS: DRAFT v0.1, 2026-10-27, lane b148des. DESIGN ONLY: nothing here is
built, fetched, measured or pinned. Governing: the [B148] row of
`docs/dev/plan.md` (Frank's rulings of 2026-10-27, quoted as RULED below and
not reopened) and inbox I-165/I-166. Where a ruling leaves a detail unstated
this note proposes one and marks it **PROPOSED**. Predictions about which
engine can do what are marked **PREDICTED**: the determination is made by the
process in section 5, never by this note.

Sources read: pcrec main **9ea9c4a76** (the I-166 pin; it contains 847acd8b4's
`tests/recursion/cscan.rxt` + `gen_cscan.py`), pcrec
`docs/dev/lanes/scandog_report.md`, `docs/design/inline_c.md` §2.3,
`docs/spec/match_api.md` §4, §10, §11, `docs/spec/vars.md`,
`docs/spec/limits.md` §3-§6; the box's libpcre2 10.46 man pages
(`pcre2api(3)`, `pcre2jit(3)`, `pcre2callout(3)`) and Oniguruma 6.9.10's
`/usr/include/oniguruma.h`; this repo's `capability_set_v1.md`,
`subst_bench_v1.md`, `record_schema.md`, `expectation_methods_v1.md`,
`subbench_directory_model.md`, `testees/onig/CLAUDE.md`.

## 0. What is new relative to every existing set

1. **A capability verdict is a RESULT with three values**, not a pre-compile
   filter: NATIVE, ASSISTED (host code supplies the feature, inside a declared
   token budget), NOT-CAPABLE (the budget is exceeded, count recorded).
   `bench/capability` decides `unsupported-by-declaration` from a declared tag
   set (`capability_set_v1.md` §5.3); this set adds the ASSISTED middle and
   makes its cost part of the timed row (RULED).
2. **An assist is an engine option**, like simd on/off, carried in the testee
   identity (RULED). Two runs of one engine with and without an assist are two
   testees.
3. **The access pattern is a CALL STREAM**, not "one subject, first match":
   the compiler calls cscan once per `(?{` segment at that segment's start;
   a variable-bearing pattern is matched once per line with that line's
   binding. One timed row is the whole stream (section 7).
4. **Callouts have a cost split** (engine dispatch vs the callee's own work)
   that the set controls with three arms and a calibration (section 3.2).

## 1. Identity

- **Set:** `bench/unusual/`, id `unusual`, first version `unusual@0.1`.
  **PROPOSED** (alternatives considered: `exotic`, `features`; "unusual" is
  Frank's own word in the ruling). Design note: this file.
- **Not an extension of `bench/capability`** for the same reason
  `capability_set_v1.md` §2.2 gives for not extending `bench/syntax`: a
  different objective (realistic workloads whose difficulty IS the feature,
  timed, vs a capability census over wild patterns). Members that already
  exist elsewhere (capability's `nested-comment-rec`,
  `bracket-array-define`) are CITED, never duplicated (`capability_set_v1.md`
  §2.4's rule).
- **Objective (sidecar `objective`):** "Realistic patterns whose feature is
  outside the common regex subset (recursion, callouts, caller variables):
  answer, capability verdict (native / assisted / not-capable), and the cost
  of the feature, assist included."
- **Layout** (`subbench_directory_model.md` §1.4's sidecar model; nothing
  new): `subbench.toml`, `patterns.rxt` (+ `ext bench` capability block,
  `capability.py`'s path (b)), `NOTES.md` (predictions + outlier rule before
  any run), `gen_*.py` + `manifest*.tsv`, `expectations*.tsv`,
  `callees/` (section 3.2), `values/` (section 3.3), `assists/` (section 5),
  `vendor/` (section 4.2).

## 2. Members (v0.1)

Seven members in three feature families plus the floor. Provenance labels:
`wild` (taken from code in use, source + licence per
`capability_set_v1.md` §4.1's record) or `authored` (written for a purpose,
author named) -- RULED (5): hand-authored members labelled authored.

| id | family | provenance | pattern (summary) | regime(s) |
|---|---|---|---|---|
| `cscan` | recursion | authored -- pcrec lane scandog, `tests/recursion/cscan.rxt` at 9ea9c4a76 (MIT, pcrec `LICENSE`) | the `(?{ ... })` end scanner, `\G`-anchored, group 1 = body, no match = refuse (`scandog_report.md` "The pattern"; rules `inline_c.md` §2.3) | call-stream, large-subject-throughput |
| `co-luhn` | callouts | authored | `\b(\d{13,19})\b(?C1)` -- card-number candidates, callee = Luhn check | short-subject-search, large-subject-throughput |
| `co-isbn` | callouts | authored | `\b(97[89]\d{10})\b(?C2)` -- ISBN-13 candidates, callee = check digit | as above |
| `co-member` | callouts | authored | `\buser=(\w++)(?C3)` -- callee = membership of group 1 in a runtime set passed through the binding's `user` (match_api §11.3¶5) | as above |
| `co-netstr` | callouts | authored | netstrings `len:data,` -- pcrec spells it `(\d{1,9}):(?C"netstr,consume"),` (§11.7 `consume`); engines without `consume` spell the check-at-end form (section 3.2) | large-subject-throughput |
| `va-tenant` | vars | authored | `^${tenant}-[0-9]{4} (?:ERROR\|WARN) ` per log line | call-stream |
| `va-route` | vars | authored | `^/${prefix:-api}/v[0-9]+/${res}${fmt+\.json}(?:\?\|$)` -- exercises `:-`, `+` | call-stream |
| `va-term` | vars | authored | `(?i)\b${term:?}\b` -- values are user search terms incl. regex metacharacters and `0x00`; exercises `:?` and the as-itself rule (vars.md §1) | call-stream |
| `floor` | -- | authored | `\(\?\{` (the set's floor pattern, schema v1.3 `role = floor`) | all |

**No wild member in v0.1** -- **PROPOSED**, stated plainly: every member is
authored. cscan is the realistic anchor (it is about to be pcrec's own
scanner, [SCANNER-DOGFOOD]). Wild candidates for v0.2, curated under
`capability_set_v1.md` §4.2's licensing floor: a recursive JSON validator
(`(?(DEFINE)...)` family), a balanced-parenthesis S-expression matcher, a
CSS/Lisp nested-comment recogniser. Ruling (5) "see if it works" is read as:
v0.1 tests the authored path first.

**Member design constraints (PROPOSED):**
- A callout site never stands in a group a subroutine call or recursion
  reaches: pcrec refuses it by name (match_api §11.1). A member that does is a
  pcrec `did-not-compile`, not a design error -- none in v0.1.
- Every callout member's callee is a PURE filter on a group closed
  immediately before the site, behind a possessive or boundary-sealed
  operand, so the backtracking-order answer (match_api §11.6¶1) does not
  depend on optimizations. Admission control: the libpcre2 oracle's answers
  with default options and with `PCRE2_NO_AUTO_POSSESS |
  PCRE2_NO_START_OPTIMIZE | PCRE2_NO_DOTSTAR_ANCHOR` must be identical over
  the whole corpus (the §11.6¶2 divergence class); a member that fails is
  redesigned, never admitted with a declared divergence in v0.1.
- Variable members use no `${` inside a class or after a backslash, and v0.1
  is byte mode only: caseless under `-e utf8` (vars.md §7's length-changing
  fold) is out of scope until a utf sibling set.

## 3. Feature families

### 3.0 The verdict table (PREDICTED; determined by section 5)

| engine (config) | recursion (cscan) | callouts | vars |
|---|---|---|---|
| libpcre2 JIT / interp (`pcre2-jit`, `pcre2-interp`) | NATIVE | NATIVE: `(?C)` syntax (pcre2callout(3); JIT supports callouts except before an assertion condition, pcre2jit(3) "unsupported pattern items") | ASSISTED (C) |
| pcrec (`pcrec-auto`, `pcrec-vm`, `-in`) | NATIVE (VM route expected, I-165) | NATIVE (match_api §11; VM only) | NATIVE (vars.md; VM only, no DFA prefilter, §7) |
| pcrec DFA-forced configs | NOT run (a `--engine=dfa` vars pattern is refused by name, vars.md §6; recursion has no DFA form) | as left | as left |
| Oniguruma (`onig-default`, Perl_NG) | NATIVE, to WITNESS: `(?&name)`/`(?(DEFINE)` run on capability's witnesses (`testees/onig/CLAUDE.md` item 2); cscan's `[\x80-\xff]` classes under `ONIG_ENCODING_ASCII` are unwitnessed | NATIVE, to WITNESS: its own site syntax `(*name)` / `(?{...})` (`ONIG_SYN_OP2_ASTERISK_CALLOUT_NAME` / `_QMARK_BRACE_CALLOUT_CONTENTS`, oniguruma.h:515-516) with `onig_set_callout_of_name` / progress callouts (oniguruma.h:983-999); a per-engine SPELLING variant, `variant.kind = syntax-only`; no `consume` | ASSISTED (C) |
| RE2 (`re2-default`) | ASSISTED or NOT-CAPABLE (a tokenizing loop with a host depth counter is the implementor's answer; whether it fits 300 C++ tokens is the finding) | ASSISTED or NOT-CAPABLE (host post-filter on the closed group) | ASSISTED (C++, `RE2::QuoteMeta` is library, free) |
| rust-regex (`rust-default`) | as RE2 | as RE2 | ASSISTED (Rust, `regex::escape`; non-UTF-8 value bytes need a hand `\xHH` escape) |
| Vectorscan (`vectorscan-block-som`) | NOT-CAPABLE likely (no anchoring at a start offset with captures; the body needs host scanning) | ASSISTED or NOT-CAPABLE (no captures: the host re-derives the group) | ASSISTED (C, `hs_compile` per value -- expensive, so its cache hit rate dominates) |

RULED (1): callout NATIVE = the engine's own pattern syntax has the site and
the host supplies only the callee; host code supplying the behaviour without
syntax is ASSISTED. RULED (3): v1 roster = libpcre2 JIT/interp, Oniguruma,
RE2, rust-regex, Vectorscan, pcrec configs; Perl and python `regex` later,
each a toolchain approval; .NET skipped. **PROPOSED:** `pcre2-dfa` and
`tre-default` are not in v1 (neither has recursion or callouts:
`capability_set_v1.md` §5.1 rows `recursion`, `callouts`).

### 3.1 Recursion: cscan

The pattern verbatim from `cscan.rxt`'s `pattern-esc` block, unmodified
(sha256 of the pcrec file recorded in `provenance`). Modules: recursion,
named-groups, conditionals (DEFINE), modifiers (`(?x)`), classes,
atomic-groups (possessive), lookaround, assertions (`\G`) (I-165). Group
numbering: `body` = 1, `sp` = 2, `items` = 3 (all named, so Oniguruma's
`CAPTURE_ONLY_NAMED_GROUP` hazard, `testees/onig/CLAUDE.md` item 1, does not
arise).

Subjects: section 4. Deep nesting: section 6.

### 3.2 Callouts: three arms, pure callees, one shared C body (RULED)

**Arms** (one pattern each, three entries in `patterns.rxt`, linked by a
`twin_of` tag):
- `twin` -- the site removed. Its expectations are its own (the language is
  wider).
- `pass` -- the site present, the callee returns continue: pcrec `RX_PASS`
  via the I-166 binding `const rx_callout_ref rx_callout_1 = { pass_fn, NULL };`
  (match_api §11.2), libpcre2 a callout function returning 0
  (pcre2callout(3) "RETURN VALUES"), Oniguruma `ONIG_CALLOUT_SUCCESS`
  (oniguruma.h:773-774). Its answers MUST equal `twin`'s (a check in the
  correctness gate). **PROPOSED:** libpcre2 with NO callout function set (it
  then ignores the site) is a fourth, pcre2-only control arm `pass-nofn`.
  ASSISTED engines have no site and run `twin` + `real` only.
- `real` -- the real callee.

**Callees** (`bench/unusual/callees/callees.c`, one C body each, shared by
every engine): `luhn`, `isbn13`, `member` (an open-addressing set built
BEFORE the timed loop, passed as `user`), `netstr`. Each takes an
engine-neutral view `{subject, len, pos, caps[], ncaps, user}` and returns
pass / fail / (netstr under `consume`) a length. Per-engine wrappers translate
`const rx_ctx *` (match_api §11.3), `pcre2_callout_block *`, and
`OnigCalloutArgs *` into the view; they are binding glue, recorded, not
budgeted.

`co-netstr` is the one shape where engines differ in MECHANISM: pcrec
consumes `len` bytes in one fire (`consume`, §11.4); libpcre2 and Oniguruma
have no consuming callout, so their native spelling is
`(\d{1,9}):(?<d>(?s:.)*?)(?C4),` with the callee failing until
`len(d) == len` -- one fire per data byte. **PROPOSED:** that is NATIVE
(their syntax has the site; the spelling is a declared `syntax-only`
variant), and the fire count is the result.

**Build shape (RULED):** the callee object is a SEPARATE translation unit,
no LTO -- the primary shape for every engine. **Unity** (the pcrec artifact
`#include`d with callees.c and the binding in one TU, I-166: gcc then inlines
the callee) is an option arm, pcrec only (libpcre2/Oniguruma call through a
function pointer from a shared library either way); it is a testee identity
token (`config_extra` `cu-tu` / `cu-unity`, **PROPOSED** spelling) and I-166's
"record which shape you time" is satisfied by that token.

**Calibration control (RULED: fire counts + standalone callee time, callee
share ~20%):**
1. FIRE COUNTS: an untimed counting pass per (member, subject, engine), built
   with `-DUB_COUNT` (the timed binary carries no counter -- **PROPOSED**),
   recorded as match-scope `engine_metadata` integer `callout_fires`
   (declared per `record_schema.md` §7; no schema change).
2. STANDALONE CALLEE TIME: the counting pass of `pcre2-interp` (the oracle's
   engine) also logs each fire's view; a pinned microbench replays the logged
   views through the shared body, median of >= 10 fresh launches
   (BOILERPLATE timing rule), giving `callee_ns_per_fire`.
3. CALLEE SHARE = `callout_fires x callee_ns_per_fire / row_ns`, per engine,
   reported beside the `real` row. Budget: a (member, subject) whose share
   exceeds 20 % on `pcre2-jit` is flagged in the readout; over 40 % it is
   resized (fewer candidates per MB) before pinned promotion
   (**PROPOSED** thresholds and reference engine).

### 3.3 Variables: the memoized escaped-recompile assist (RULED)

NATIVE only on pcrec (`--features vars`; one compile, the per-call `rx_var`
array rides `rx_ctx`, vars.md §3-§4). Every other engine is ASSISTED by WHAT
AN IMPLEMENTOR WOULD DO (RULED):

- Resolve each `${...}` in the member's pattern text from the call's binding
  in HOST code, with vars.md §2's operator table exactly: `${n}`, `${n-w}`,
  `${n:-w}`, `${n+w}`, `${n:+w}`, `${n:?w}`, the one-level fallback chain
  `${a:-${b}}`, UNSET (`p == NULL`) distinct from EMPTY (`len == 0`), a
  backslash in `w` making the next byte literal.
- UNSET at a bare `${n}`, or UNSET/EMPTY at `${n:?}`, REFUSES the call
  (vars.md §5) -- the host returns the refusal without matching.
- Escape the resolved value so it matches AS ITSELF (vars.md §1), every byte
  incl. `0x00` and `\E`; interpolate; look the resulting pattern up in a memo;
  compile on a miss.
- The whole cost -- resolution, lookup, any compile -- is INSIDE the timed row
  (RULED).

**Value streams (RULED: declared per subject).** `values/<subject>.tsv`:
the binding table (value id -> bytes, or UNSET) and the per-call stream
(call k -> value id per variable). The sidecar states, per subject, the
stream length, distinct values and reuse order (`zipf-s1.1`, `round-robin`,
`all-distinct`), because the hit rate is part of the result. `va-tenant`
runs at three distinct counts over one line file -- `d4`, `d64`, `d4096`
(**PROPOSED**) -- so the cache effect is a ladder, not an accident.

**Memo lifetime (PROPOSED):** cleared at the start of every timed iteration
(an iteration is one replay of the stream from cold), unbounded within it.
So compiles per iteration = the stream's distinct resolved patterns, exactly,
and match-scope `engine_metadata` `assist_compiles` / `assist_lookups`
records it (checked equal to the declaration).

## 4. Subjects (cscan)

### 4.1 Family F1 -- segment stream (generated)

`gen_subjects.py`, seeded, sha256 manifest. Filler pattern text (`a+`,
`[0-9]{2}`, ...) between `(?{ ... })` segments; segment sizes log-uniform
20 B - 5 KB (I-165); bodies drawn from a declared token mix: identifiers
(incl. `\x80-\xff` bytes), pp-numbers (incl. C23 `1'000`), string/char
literals with escapes, both comment kinds, backslash-newline splices at a
declared rate, nested `{}` and `<% %>` to depth 6, preprocessor lines with
balanced braces. ~1 % of segments carry a LOCAL refusal (raw newline in a
literal) -- **PROPOSED**; a refusal never spans into the next segment, since
each call is anchored at its own start.

| subject | segments | approx bytes |
|---|---|---|
| `seg-s` | 256 | 180 KB |
| `seg-l` | 4,096 | 3 MB |

The call list (each segment's `(?{` offset) is a manifest column.

### 4.2 Family F2 -- real C bodies

- **sqlite3.c (RULED: vendored, pinned, sha256).** The SQLite amalgamation
  (public domain), the release current at build, committed as
  `vendor/sqlite3.c.xz` with the sha256 of both the archive and the
  decompressed file (**PROPOSED**: compressed, ~2.5 MB instead of ~9 MB in
  git). Fetching it is a DOWNLOAD and needs Frank's approval of the exact URL
  and checksum before it happens (user CLAUDE.md "Security"). Subjects:
  `sqlite-bodies` -- every function body, located by the reference scanner
  (section 8), wrapped `(?{` body `})` and concatenated with filler (~7 MB,
  one call per body); `sqlite-bodies-s` -- a deterministic 1-in-16 sample.
- **Kernel sources (RULED: optional sha256-checked fetch, never committed).**
  **PROPOSED** list: five files of one tagged release (`kernel/sched/core.c`,
  `mm/memory.c`, `fs/namei.c`, `net/core/dev.c`, `lib/vsprintf.c`, ~1.5 MB),
  each sha256-pinned in `fetch_kernel.py`'s table, fetched to
  `build/unusual/kernel/` (gitignored). Absent = the `kernel-bodies` cells
  are skipped BY NAME. GPL-2.0 text is never redistributed.

### 4.3 Family F3 -- pathologicals (generated; one call at offset 0)

| subject | content | expected (PREDICTED) |
|---|---|---|
| `comment-5m` | `(?{ /*` 5 MB `*/ })` | match |
| `literal-100k` | a 100,000-char `"..."` | match |
| `nest-brace-1k` / `-10k` / `-100k` | `{` x d, a token, `}` x d | match by construction; engine-default limits give up first (section 6) |
| `nest-digraph-10k` | `<%` x d ... `%>` x d | as above |
| `idents-1m` | 1 MB of identifiers and spaces | match |
| `splice-1m` (**PROPOSED** addition) | a 1 MB identifier with a splice after every byte | match; isolates `(?&sp)`'s per-character cost |
| `unterminated-5m` | `(?{ /*` 5 MB, no `*/` | NO match (refusal); every engine must answer cleanly -- a crash is a first-class `crashed` outcome |

Regime: `large-subject-throughput`, first match (the pattern is
`\G`-anchored, so only offset 0 can match).

## 5. The assist: budget, counting, authoring (RULED)

**Budget.** X = **300 lexical tokens per feature per engine**, counted in the
engine's own binding language (C for libpcre2, Oniguruma, Vectorscan; C++ for
RE2; Rust for rust-regex) with the [B141] rule: non-blank lines and lexical
tokens, boilerplate excluded against a DECLARED list; standard-library
containers free; C given ONE declared small hash-map helper outside the count.
Fits = ASSISTED; exceeds = NOT-CAPABLE with its count recorded. Gave-up and
crash stay RUNTIME outcomes, never capability verdicts.

**Declared before any assist is authored** (RULED), in
`bench/unusual/assists/RULES.md`: the budget; the counter and its version;
the boilerplate list -- includes/`use`, `main`, I/O and the driver-protocol
shim (the timed loop, subject loading, result reporting), the shared callees
(`callees.c`), the C hash-map helper (`assists/common/ub_map.h`, ~60 lines,
string -> pointer) -- each excluded region fenced by
`/* BOILERPLATE <item> */ ... /* END BOILERPLATE */` naming a list item.

**Counter (PROPOSED: built by this set, reused by [B141]).**
`tools/tokcount.py`: one hand lexer per language (C, C++, Rust); comments and
whitespace dropped; a string or char literal is ONE token; identifiers,
keywords, numbers and punctuators one each, multi-character punctuators
(`->`, `::`, `<<=`, `=>`) one; fenced regions excluded only when their item
is in the declared list (else the run fails naming the region). Self-tested
on fixtures with hand counts. [B141] has no counter yet (its row:
not-started); this one is written for both.

**Granularity (PROPOSED reading of "per feature per engine"):** ONE assist
per (feature, engine), serving every member of that family in the set (for
vars that is one generic interpolator; for callouts one body handling all four
callout members; for recursion, cscan alone in v0.1). A new family member
later re-opens the assist (new version, new count, new testee id). See OQ-1.

**Ledger.** `bench/unusual/assists/<feature>/<engine>/assist.<ext>` +
`assists.tsv`: feature, engine, language, tokens, lines, budget, verdict
(ASSISTED / NOT-CAPABLE), assist sha256, counter version, author lane,
reviewer lane, reviewer verdict.

**Authoring (RULED (2)).** One BLINDED author lane per (feature, engine).
The brief carries ONLY: the problem statement (the family's members'
canonical pattern texts and intention statements, the host-side contract the
assist must meet -- e.g. vars.md §2-§5 restated engine-neutrally, the pure
callee contract match_api §11.6¶1), the engine's own documentation, the
budget and counting rule with the boilerplate list, a PUBLIC sample of cases
to self-test (**PROPOSED**: for cscan, gen_cscan.py's 76 cases; for the
others, 20 cases per member; the full corpus held out), and the instruction
**BE BRIEF**. Never: another engine's assist, pcrec's implementation, the
held-out expectations. A separate read-only REVIEWER per assist checks
idiomatic-not-golfed (the judgment is acknowledged subjective, as [B141]
says); verdict `accepted` / `golfed` (back to the author once) /
`not-idiomatic`. The COUNTER, not the author, produces the count. An author
who abandons at the budget records "exceeded at N tokens, abandoned" -- that
is a NOT-CAPABLE verdict with its count.

**Testee identity (PROPOSED).** An assisted config is its engine's config
plus `assist = "<feature>"` and `assist_version`, its `config_extra`
`assist-<feature><n>` (record_schema §6.4's escape hatch; the frozen
`config_slug` shape is untouched), and `families = ["<feature>"]` so the
harness runs it over that family's members only. A NOT-CAPABLE (feature,
engine) gets no assisted config; the plain config's `ext bench` capability
set omits the feature, so `capability.py` (§5.3) yields
`unsupported-by-declaration` with `declaration_ref` = the `assists.tsv` row.

## 6. Deep nesting: two arms (RULED (4))

| arm | libpcre2 JIT | libpcre2 interp | Oniguruma | pcrec |
|---|---|---|---|---|
| `default` | the 32 KiB machine-stack JIT stack (pcre2jit(3) "JIT stack": "By default, it uses 32KiB on the machine stack") | the library's compiled-in heap/match/depth limits, read with `pcre2_config` and recorded | library defaults, read with `onig_get_match_stack_limit_size` / `_retry_limit_in_match` / `_subexp_call_limit_in_search` / `_subexp_call_max_nest_level` (oniguruma.h:927-951) and recorded | the stamped frame default (2,048 resume / 3,072 trail, limits.md §3.2; the documented ~342-level ceiling on `^(a(?1)?b)$`, §4) and default step/work budgets |
| `deep` (to the declared CEILING) | `pcre2_jit_stack_create(32 KiB, CEIL)` + `pcre2_jit_stack_assign` | `pcre2_set_heap_limit(CEIL/1024)`, match and depth limits at `UINT32_MAX` (pcre2api(3)) | the four limits at CEIL / unlimited via the `_of_match_param` setters (oniguruma.h:977-981) | the `_in` entries with a CEIL-sized caller buffer (match_api §10.2-§10.4; limits.md §5¶6: the only route past the stack-resident default), step/work budgets raised by `--step-budget`/`--work-budget` |

**PROPOSED** CEIL = 1 GiB of matcher working storage, counters at their
type's maximum. The arm is a testee identity token (`config_extra`
`lim-default` is implicit; `lim-ceil1g`). Every engine's effective limits
are recorded as pattern-scope `engine_metadata` integers on the compile row.

A give-up NAMES the limit hit (RULED; the schema already requires a
non-empty `diagnostic` on `gave-up`, `record_schema.md` §8 match table):
`PCRE2_ERROR_JIT_STACKLIMIT` (-46) / `_MATCHLIMIT` (-47) / `_DEPTHLIMIT`
(-53) / `_HEAPLIMIT` (-63) (pcre2.h); `PCREC_ERR_FRAMES` / `_STEPS` /
`_WORK` (match_api §4¶1); `ONIGERR_MATCH_STACK_LIMIT_OVER` (-15) /
`_RETRY_LIMIT_IN_MATCH_OVER` (-17) / `_SUBEXP_CALL_LIMIT_IN_SEARCH_OVER`
(-19) (oniguruma.h:576-580). An assisted host's own depth counter, if any,
is unbounded by construction and declared so. A signal is `crashed`.

## 7. What the record needs -- schema v1.11 (PROPOSED, a MINOR bump)

What already fits, unchanged: `unsupported-by-declaration` + `declaration_ref`
(NOT-CAPABLE); `gave-up` + `diagnostic` (named limits); `crashed`;
`engine_metadata` integers (`callout_fires`, `assist_compiles`,
`assist_lookups`, effective limits); `config_extra` (assist, arm, TU shape);
`patterns[].variant` (Oniguruma's callout spelling, the netstring check-at-end
form).

What does not fit, and is the minimum addition:
1. **Regime `call-stream`** (enum addition): one timed row = the whole
   declared call list over one subject. Each call is (offset, length,
   binding id). cscan F1/F2: length = rest of subject; vars: one line.
2. **`match_row.stream`** (required iff `regime = call-stream`):
   `calls`, `matched`, `nomatch`, `refused` (vars.md §5's refused call --
   which therefore needs NO new match outcome), `results_sha256` over the
   per-call result tokens (`n`, `m:<s>,<e>[;<g1s>,<g1e>...]`, `r`). The
   row is `matched-as-expected` iff the hash equals the expectation's;
   a call that gives up makes the row `gave-up`, naming the first limit and
   the count. Mirrors `match_row.subst` (v1.9).
3. **`testee.assist`** (optional): `{feature, version, tokens, lines,
   budget, sha256, counter}`, with a rule that it is present iff
   `config_extra` carries `assist-<feature><version>`.

Rules X47-X49 to match (numbering after v1.10's X46). Built by its own lane
(section 10, L1).

## 8. Oracles and expectations (engine-neutral, R-BENCH-4)

pcrec is never asked for an expectation (as gen_cscan.py's own docstring
states for the corpus it came from).

| family | primary method | second method (agreement control on every triple both answer) |
|---|---|---|
| cscan | `libpcre2-differential` (interp, at the `deep` ceiling, declared) | NEW `reference-scanner` (**PROPOSED**): a Python, iterative, regex-free implementation of `inline_c.md` §2.3 rules 1-5 plus the three choices `cscan.rxt`'s header states; it also answers any triple libpcre2 gives up on (declared, as `expectation_methods_v1.md`'s fallbacks are). Both must reproduce gen_cscan.py's 76 cases first. |
| callouts | `libpcre2-differential` with the SHARED `callees.c` loaded through ctypes as the callout function, run under default options AND the three no-optimization options (section 2's admission control) | `host-reference` (**PROPOSED**): plain Python of each member's intention (scan candidates, apply the check), no regex engine shared |
| vars | `libpcre2-differential` over the resolved, escaped pattern per call (the resolution written in Python from vars.md §2/§5, independent of any assist) | python `re` with `re.escape` interpolation (stdlib, a different engine) |

Expectations: `expectations.tsv` (existing format) for the throughput and
search regimes; `expectations_stream.tsv` (subject, pattern, calls, matched,
nomatch, refused, results_sha256, method) for `call-stream`, re-derived under
`make check-harness` like every set's.

## 9. Tiers: scratch first, then pinned (RULED (6))

- **Readout 1, SCRATCH tier** (`run --tier scratch`, `build/scratch-store/`),
  timed at pcrec **9ea9c4a76 (abi 89)**. Prerequisite: [B147]'s re-pin to
  that sha (I-166) is merged, since the callout binding and cscan.rxt live
  there. The readout -- MB/s vs libpcre2 JIT and interp, deep-nesting
  behaviour per arm, which constructs cost most, the verdict table with
  token counts, callee shares -- goes to the outbox. The run itself needs a
  box window cleared via pcrec-main (BD3) and Frank's scheduling.
- **Promotion to PINNED** at the next cleared window after readout 1, same
  cells, into `store/`.
- The comparison against pcrec's hand-written scanner waits for [INLINE-C]
  stage 2 (I-165); I-166: do not wait for it.

## 10. Build order (lanes)

| lane | content | depends on |
|---|---|---|
| L0 | this note -> critic panel -> v0.2 with Frank's rulings | -- |
| L1 | schema v1.11 (section 7) + validator rules + examples / bad examples | L0 |
| L2 | `tools/tokcount.py` + `assists/RULES.md` + `ub_map.h` -- DECLARED before L6 starts | L0 (parallel with L1) |
| L3 | set skeleton, cscan member, F1/F3 generators, reference scanner, oracle, expectations; the sqlite vendoring after Frank approves the fetch; `fetch_kernel.py` | L1 |
| L4 | drivers: `call-stream` in every adapter; the `deep` arm configs; limit read-back and give-up naming | L1, L3 |
| L5 | callouts: `callees.c`, wrappers (pcrec separate-TU + unity, libpcre2, Oniguruma witness first), the three arms, counting build, calibration microbench, members + oracle | L4, [B147] |
| L6 | blinded assist authors + reviewers, one lane each per (feature, engine): vars x {pcre2, onig, re2, rust, vectorscan}; callouts x {re2, rust, vectorscan}; recursion x {re2, rust, vectorscan} | L2 (rules declared), L3-L5 (problem statements + public samples) |
| L7 | vars members, value streams, pcrec native vars path | L4 |
| L8 | scratch readout window (manager), outbox; then pinned promotion | all, a cleared window |

A lane spawns no helpers (BOILERPLATE); author lanes are blinded by their
briefs and run no engine but their own.

## 11. Open questions

- **OQ-1 Assist granularity.** Section 5 reads "per feature per engine"
  literally: one assist serves all members of a family. For callouts and
  recursion there is no generic assist, so the budget is shared across the
  family's members and adding a member can flip a verdict. Alternative: 300
  tokens per (member, engine). Frank's call.
- **OQ-2 Set name** `unusual`.
- **OQ-3 sqlite3.c**: release, compressed vendoring, and the download
  approval itself (URL + sha256 shown before fetch).
- **OQ-4 Kernel file list** (section 4.2).
- **OQ-5 The ceiling**: 1 GiB working storage for the `deep` arm.
- **OQ-6 Callee-share thresholds** (20 % flag / 40 % resize) and
  `pcre2-jit` as the reference engine.
- **OQ-7 Netstring on libpcre2/Oniguruma**: the check-at-end spelling as
  NATIVE (proposed), or ASSISTED since the consuming behaviour is not in
  their syntax.
- **OQ-8 Schema v1.11's `call-stream` regime** vs one match row per call
  (thousands of rows, no new regime). The note proposes the regime.
- **OQ-9 Wild members**: none in v0.1; which candidates for v0.2.
- **OQ-10 Oniguruma witnesses**: `[\x80-\xff]` under `ONIG_ENCODING_ASCII`,
  `(?{...})` / `(*name)` under Perl_NG. If either fails, the verdict is
  decided by an assist author like any other engine's.
- **OQ-11 `pass-nofn`** (libpcre2 with no callout function) as a fourth
  control arm.
- **OQ-12 The token counter** is built here for [B141] too: confirm it
  belongs to this set's build.
