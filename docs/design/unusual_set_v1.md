# unusual_set_v1 -- realistic patterns using UNUSUAL features (plan row [B148], inbox I-165/I-166)

STATUS: DRAFT **v0.2**, 2026-10-27, lane b148v2 (v0.1: lane b148des, merged
1c20bd13). DESIGN ONLY: nothing here is built, fetched, measured or pinned.
Governing: the [B148] row of `docs/dev/plan.md` (Frank's rulings of 2026-10-27,
quoted as RULED and not reopened), inbox I-165/I-166, and the r9 panel
(`docs/dev/reviews/2026-10-27-r9-unusual-set.md`, C1-C10 + Q1 ruled; detail in
its `-meas.md` M-n, `-semantics.md` E-n, `-schema.md` S-n). Where the rulings
and the panel leave a detail open this note chooses and marks it **PROPOSED**;
every PROPOSED choice is listed in the change log below. Engine-capability
claims are **PREDICTED** -- section 5's process decides, never this note.
Probe results are the r9eng critic's (functional ctypes probes of libonig
6.9.10 / libpcre2 10.46, no timing; `-semantics.md`); this lane ran no engine.

Sources read: pcrec main **9ea9c4a76** (the I-166 pin; `tests/recursion/
cscan.rxt` + `gen_cscan.py`, unchanged since 66f9a8560 -- pcrec's later
614d45eb3 "CI red on 9ea9c4a76 = rxtsource census pins ... no pcrec bug"
leaves cscan's text as it is), pcrec `docs/dev/lanes/scandog_report.md`,
`docs/design/inline_c.md` §2.3, `docs/design/variables_pattern.md`,
`docs/spec/match_api.md` §4, §10, §11, `docs/spec/vars.md`,
`docs/spec/limits.md` §3-§6; libpcre2 10.46 `pcre2api(3)`, `pcre2jit(3)`,
`pcre2callout(3)`, `pcre2pattern(3)`, `pcre2matching(3)`; `/usr/include/
oniguruma.h` (6.9.10); this repo's `capability_set_v1.md`, `subst_bench_v1.md`,
`record_schema.md`, `gate_shape_v14.md` §3.7, `expectation_methods_v1.md`,
`pcrecbench/{capability,reduce,harness,subbench,adapters}.py`,
`pcrecbench/report_subst.py`, `tools/selfcheck.py`, `testees/*/CLAUDE.md`.

## Change log v0.1 -> v0.2 (r9 C1-C10, Q1)

| item | what changed | sections |
|---|---|---|
| C1 ruling drift | budget/ledger/author lanes per (MEMBER, engine), the "adding a member flips a verdict" text gone; two WILD members; sqlite/kernel pinned at fetch, show-then-approve per file; netstring ASSISTED on libpcre2/Onig, its check-at-end spelling no longer a syntax-only variant; OQ-1..OQ-12 de-PROPOSED | 2, 3.0, 3.2, 4.2, 5, 10, 11 |
| C2 identity | `testee.assist` an ARRAY + set-level `assist_version`; ONE token `assist-v<set>`; per-member verdicts in `assists.tsv`; `REQUIRES_VOCAB` grows `vars` (+ `unusual-<member>`); NOT-CAPABLE count in `declaration_ref`; NOT-CAPABLE != did-not-compile | 5.4, 5.5, 7.4 |
| C3 spread rule | one iteration = one full replay; rule `v1.11-group`; calibration for streams; L1 | 7.2, 7.4, 10 |
| C4 stream semantics | bytes = sum of segment lengths, `calls` the denominator; O(segment) pre-flight; preallocated tokens hashed after the clock; call counts; load untimed; group 0 + 1 only; vectorscan-block-som only; "refused" defined | 4, 7.1, 7.2 |
| C5 callout arms | `pass` = full wrapper + stub; pcrec twin under `pcrec-vm` too; per-arm `callout_fires`; per-engine fire logs; share on every engine; `callees.o` once; RETURN-CODE MAPPING + first-candidate-fails control; assisted netstring pattern; twins in the common subset; who computes each comparison; `twin_of` tag | 2, 3.2 |
| C6 vars assist | readout says what the time measures, pcrec break-even; free placement identical; keying/container/sha256 in ledger; fixed stream length on the ladder; rust `unicode(false)`; ASCII case variants; `${!name}`, literal escaped words, chain dropped (asked of pcrec), vectorscan `\x00` | 3.3, 5.3 |
| C7 deep nesting | depth-of-failure table by limit name, rungs 128..100k, per-engine predictions, Onig nest-20 SILENT, all six Onig defaults read back, -5/-18, global setters in driver.c, JIT match_limit, buffers once, dry run + `CELL_CAP_unusual`, fresh processes, effective limits, CAP not like-for-like in depth | 4.3, 6 |
| C8 high-water | `deep_mem_method`, never ranked across methods, bytes/level, untimed fresh-process pass, known-depth + floor controls, pcrec frame count, record fit checked in L1 | 6.4 |
| C9 Onig cscan | declared syntax-only variant `(?<sp>...){0}(?<items>...){0}`, witness `(?{x})DEFINE`, OQ-10 witnesses recorded as probed, verdict NATIVE | 3.1, 3.0 |
| C10 readers etc. | `--grain stream` view; viewer/trend/frontpage/interpret behaviour; `--mode calls` protocol; `unusual_only`; `UNUSUAL_GATE_SKIPS`, `tools/check_unusual.py`, `make check-unusual`; Frank gates in the build order; X47-X53 each with a negative example; pcre2-dfa reason restated | 3.0, 7, 10 |
| Q1 (RULED) | 1 GiB CAP on matcher working storage for EVERY engine; pcre2-interp's `deep` is tighter than its `default` (~19 GiB) and says so | 6.1, 6.2 |

**PROPOSED choices made in v0.2** (each also marked in place):
P1 the wild S-expression member is pcre2pattern(3)'s own balanced-parenthesis
pattern (2.1); P2 the JSON member's source is OWED, candidate named, not
admitted until verified (2.1); P3 the assisted netstring callee contract and
Onig's `(?{4})` spelling (3.2); P4 per-member capability tokens
`unusual-<member>` (5.5); P5 identity token `assist-v<MAJOR><MINOR>` and the
`compose_config_extra` order lim / cu / assist (5.5); P6 a call-stream clock per
replay with the memo cleared and freed between clocks (7.2); P7 the
`--mode calls` protocol (7.3); P8 `unusual_only` config key (7.3); P9 the
assisted vars member's compile row (7.4); P10 deep-arm counters at their type
maximum, the cap applying to storage only (6.2); P11 Onig nest level 1,000,000
in `deep` (6.2); P12 viewer/trend/frontpage skip `call-stream` by name in v0.1
(7.5); P13 the stream length 16,384 calls on the va-tenant ladder (3.3); P14
the 1-in-16 sqlite sample and filler rules unchanged from v0.1 (4.2).

## 0. What is new relative to every existing set

1. **A capability verdict is a RESULT with three values**: NATIVE, ASSISTED
   (host code supplies the feature inside a declared token budget), NOT-CAPABLE
   (budget exceeded, count recorded) -- RULED. `bench/capability` decides
   `unsupported-by-declaration` from a declared tag set (`capability_set_v1.md`
   §5.3); this set adds the ASSISTED middle and times it.
2. **An assist is an engine option** carried in the testee identity, like simd
   on/off (RULED).
3. **The access pattern is a CALL STREAM** (section 7): cscan is called once per
   `(?{` segment at its start; a variable-bearing pattern once per line with
   that line's binding. One timed row = one stream.
4. **Callouts have a cost split** (dispatch vs callee work) the set controls
   with arms and a per-engine calibration (3.2).

## 1. Identity

- **Set:** `bench/unusual/`, id `unusual`, first version `unusual@0.1` (OQ-2
  RULED). Design note: this file.
- **Not an extension of `bench/capability`** (`capability_set_v1.md` §2.2's
  reasoning: different objective). Capability's `nested-comment-rec` and
  `bracket-array-define` are CITED, never duplicated (§2.4's rule); the wild
  members below are chosen not to duplicate them (2.1).
- **Objective (sidecar):** "Realistic patterns whose feature is outside the
  common regex subset (recursion, callouts, caller variables): answer,
  capability verdict (native / assisted / not-capable), and the cost of the
  feature, assist included."
- **Layout** (`subbench_directory_model.md` §1.4): `subbench.toml`,
  `patterns.rxt` (+ `ext bench` capability block), `NOTES.md` (predictions,
  outlier rule and the Onig nest-20 declaration, 6.3, before any run),
  `gen_*.py` + manifests, `expectations.tsv`, `expectations_stream.tsv`,
  `calls/` (7.3), `callees/` (3.2), `values/` (3.3), `assists/` (5),
  `vendor/` (4.2).

## 2. Members (v0.1)

Ten members in three families plus the floor. Provenance (RULED (5)): `wild`
(taken from code or documentation in use, source + licence per
`capability_set_v1.md` §4.1) or `authored` (written for the set).

| id | family | provenance | pattern (summary) | regime(s) |
|---|---|---|---|---|
| `cscan` | recursion | authored -- pcrec lane scandog, `tests/recursion/cscan.rxt` at 9ea9c4a76 (MIT, pcrec `LICENSE`) | the `(?{ ... })` end scanner, `\G`-anchored, group 1 = body, no match = refuse (`scandog_report.md` "The pattern"; rules `inline_c.md` §2.3) | call-stream, large-subject-throughput |
| `wild-sexp-balanced` | recursion | wild -- `pcre2pattern(3)` "RECURSIVE PATTERNS" (BSD-3-Clause, `/usr/share/doc/libpcre2-8-0/copyright`) | `(?x)( \( ( [^()]++ \| (?1) )* \) )` -- 2.1 | short-subject-search, large-subject-throughput |
| `wild-json-validate` | recursion | wild -- source **OWED** (2.1) | a `(?(DEFINE)...)` JSON value grammar, `^...$` | short-subject-search, large-subject-throughput |
| `co-luhn` | callouts | authored | `\b(\d{13,19})\b(?C1)` -- card candidates, callee = Luhn | short-subject-search, large-subject-throughput |
| `co-isbn` | callouts | authored | `\b(97[89]\d{10})\b(?C2)` -- callee = ISBN-13 check digit | as above |
| `co-member` | callouts | authored | `\buser=(\w++)(?C3)` -- callee = group 1 in a runtime set passed as `user` (match_api §11.3¶5) | as above |
| `co-netstr` | callouts | authored | netstrings `len:data,`; pcrec `(\d{1,9}):(?C"netstr,consume"),` (§11.7); ASSISTED elsewhere (3.2) | large-subject-throughput |
| `va-tenant` | vars | authored | `^${tenant}-[0-9]{4} (?:ERROR\|WARN) ` per log line | call-stream |
| `va-route` | vars | authored | `^/${prefix:-api}/v[0-9]+/${res}${fmt+\.json}(?:\?\|$)` -- `:-`, `+` | call-stream |
| `va-term` | vars | authored | `(?i)\b${term:?}\b` -- values incl. metacharacters and `0x00`; `:?` and the as-itself rule (vars.md §1); also spelled once as `${!term:?}` (3.3) | call-stream |
| `floor` | -- | authored | `\(\?\{` (schema v1.3 `role = floor`) | all |

Each callout member has three entries (`<id>-twin`, `<id>-pass`, `<id>` real)
linked by a `twin_of=<id>` tag (3.2).

### 2.1 The wild members (OQ-9 RULED: 1-2 in v0.1)

**`wild-sexp-balanced`** (**PROPOSED** P1). Source: `pcre2pattern(3)` 10.46,
section "RECURSIVE PATTERNS", the paragraph "If this were part of a larger
pattern ... ( \e( ( [^()]++ | (?1) )* \e) )", which the page says assumes
PCRE2_EXTENDED. Fidelity `adapted`: `(?x)` prepended to carry that stated
option, nothing else changed. Licence: libpcre2's BSD-3-Clause (the box's
`/usr/share/doc/libpcre2-8-0/copyright`, "License: BSD-3-clause-Cambridge");
`source` slug `pcre2-doc` (a new slug beside capability's `pcre2-testdata`,
registered in this set's provenance, not capability's enum). Realism: finding
balanced Lisp/Scheme forms in source text is the documentation's own canonical
use of numeric-group recursion. Not a duplicate: `bracket-array-define` is an
anchored `^ (?&brackets) $` validator over `[]` via DEFINE, `nested-comment-rec`
a comment-delimited `(?1)`; this is an UNANCHORED find over `()` with a
possessive inner run. Known limitation, stated not fixed: parentheses inside a
Lisp string or comment are not special to the pattern, so subjects are
generated forms whose atoms carry no `(`/`)`; the near-miss family is the
unbalanced form (one `)` dropped at depth d). Subjects: generated S-expression
text, nesting rungs as 4.3, so the `deep` arm applies (M-12: the depth profile
is that of `(?1)` per level, one level per paren).

**`wild-json-validate`** (**PROPOSED** P2, source OWED). Candidate: the
`(?(DEFINE)(?<number>...)(?<boolean>...)(?<string>...)(?<array>...)
(?<pair>...)(?<object>...)(?<json>...))` validator posted as an answer to Stack
Overflow question 2583472 ("Regex to validate JSON"), licence CC BY-SA (the
version follows the post date). It is NOT on the box or in either repo
(searched: `bench/`, `docs/dev/research/`, `~/pcrec/tests`, `/usr/share`), so
this note does not transcribe it. OWED, owner L3: fetch the post's text
(the URL shown to Frank before any download, user CLAUDE.md "Security"),
record the URL, author, licence version and retrieval date in `provenance`,
fidelity `verbatim`; if Frank rejects the licence or the text cannot be
verified, the member is dropped from v0.1 rather than replaced by an authored
look-alike. Its `(?(DEFINE)` needs Onig's syntax-only variant (3.1's
mechanism). Second method: Python `json.loads` on the subject with each
divergence between the regex's language and RFC 8259 DECLARED per subject
(the regex is the intention, R-BENCH-4).

**Admission for both** (the callout admission control of 2.2 does not apply):
libpcre2 answers under default options and under `PCRE2_NO_AUTO_POSSESS |
PCRE2_NO_START_OPTIMIZE | PCRE2_NO_DOTSTAR_ANCHOR` identical over the corpus,
and the second method (8) agrees on every triple both answer.

### 2.2 Member design constraints

- A callout site never stands in a group a subroutine call or recursion
  reaches (pcrec refuses it by name, match_api §11.1).
- Every callout callee is a PURE filter on a group closed immediately before
  the site, behind a possessive or boundary-sealed operand (match_api §11.6¶1).
  Admission: libpcre2's answers with default options and with the three
  no-optimization options above identical over the corpus (the §11.6¶2
  divergence class); a member that fails is redesigned, never admitted with a
  declared divergence.
- Twins are written in the COMMON subset (E-8): `co-member-twin` is
  `\buser=(\w+)` (answer-identical to `\w++` with nothing after it), so RE2,
  rust-regex and vectorscan can run it.
- Variable members: no `${` inside a class or after a backslash; byte mode only
  (vars.md §7's length-changing fold is out of scope until a utf sibling).

## 3. Feature families

### 3.0 The verdict table (PREDICTED; decided by section 5)

| engine (config) | recursion (cscan, wild-*) | callouts (luhn/isbn/member) | co-netstr | vars |
|---|---|---|---|---|
| libpcre2 (`pcre2-jit`, `pcre2-interp`) | NATIVE | NATIVE `(?C)` (pcre2callout(3); JIT supports callouts except before an assertion condition, pcre2jit(3)) | ASSISTED (OQ-7 RULED: `consume` is not in its syntax) | ASSISTED (C) |
| pcrec (`pcrec-auto`, `pcrec-vm`, `-in`) | NATIVE (VM route, I-165) | NATIVE (match_api §11; VM only) | NATIVE (`consume`, §11.7) | NATIVE (vars.md; VM only, §7) |
| pcrec DFA-forced | not run (vars refused by name, vars.md §6; no DFA recursion) | not run | not run | not run |
| Oniguruma (`onig-default`, Perl_NG) | NATIVE: `(?&name)`/`(?1)` (`testees/onig/CLAUDE.md` item 2); cscan and the JSON member through the declared syntax-only variant (3.1); witnesses below | NATIVE: `(?{...})` content callouts (E-14 probe: `a(?{x})b` compiles); `(*name)` needs `onig_set_callout_of_name` before `onig_new` (probe: -229 otherwise) | ASSISTED (OQ-7) | ASSISTED (C) |
| RE2 (`re2-default`) | ASSISTED or NOT-CAPABLE (host tokenizing loop + depth counter vs 300 C++ tokens) | ASSISTED or NOT-CAPABLE (host post-filter on the closed group) | ASSISTED or NOT-CAPABLE | ASSISTED (C++, `RE2::QuoteMeta` free) |
| rust-regex (`rust-default`) | as RE2, compiled `unicode(false)` (3.3) | as RE2 | as RE2 | ASSISTED (Rust, `regex::escape`; `unicode(false)`) |
| Vectorscan (`vectorscan-block-som`) | NOT-CAPABLE likely (no captures, no recursion) | ASSISTED or NOT-CAPABLE (host re-derives the group) | as left | ASSISTED (C, `hs_compile` per value + `hs_alloc_scratch`) |

RULED (1): callout NATIVE = the engine's own syntax has the site and the host
supplies only the callee. RULED (3): v1 roster as above; Perl and python
`regex` later, each a toolchain approval; .NET skipped. Only
`vectorscan-block-som` runs this set: `vectorscan-block-nosom` is boolean grain
and cannot produce the span a stream token or a throughput answer needs
(X34; C4). `pcre2-dfa` is excluded because it has **no captures** (pcre2matching(3)
item 5: callouts ARE supported, capture_top always 1; recursion is handled) --
cscan's group 1 and every callee view need them (E-11; capability_set_v1.md
§5.1's row is corrected by its own owner, not here). `tre-default` has neither
recursion nor callouts.

**Oniguruma witnesses (OQ-10 RULED: witnessed at build).** Recorded as probed
by r9eng under Perl_NG/ASCII on 6.9.10 (E-14): `a(?{x})b` compiles;
`a(*foo)b` returns -229 until `onig_set_callout_of_name` is called before
`onig_new`; `[\x80-\xff]+` on `a\xe9\xff` matches [1,3); `\Ga` on `ba` does not
match (anchors at the search start). L5 re-runs them as the build gate in
`tools/check_unusual.py`. Onig's callout spelling in this set is `(?{N})`
(content callouts through `onig_set_progress_callout`), a declared
`syntax-only` variant of `(?CN)`.

### 3.1 Recursion: cscan

The pattern verbatim from `cscan.rxt`'s `pattern-esc` block (sha256 of the pcrec
file in `provenance`). Modules: recursion, named-groups, conditionals (DEFINE),
modifiers, classes, atomic-groups, lookaround, assertions (I-165). Groups:
`body` = 1, `sp` = 2, `items` = 3 (all named; Onig's
`CAPTURE_ONLY_NAMED_GROUP` hazard does not arise).

**Oniguruma variant (C9, E-2).** Onig has no `(?(DEFINE)...)`: its condition is
a regex, so `xDEFINEy` matches [0,8) where PCRE2 gives [0,1) (probe). The
declared `syntax-only` variant replaces `(?(DEFINE)(?<sp>...)(?<items>...))`
with `(?<sp>...){0}(?<items>...){0}` (Onig RE doc §9). Onig also KEEPS captures
set inside a subroutine call where PCRE2 resets them (probe:
`x(?&q)(?(DEFINE)(?<q>y))` on `xy` sets group 1 on Onig only), so groups 2/3
differ by design: the stream token carries group 0 and group 1 ONLY (7.1),
and the throughput answer is compared on groups 0-1. Witness subject
`(?{x})DEFINE` in F3 shows the variant answers as PCRE2 does. Verdict NATIVE
(rule 1: the feature is in Onig's syntax; a respelling is the variant
mechanism). The same variant mechanism serves `wild-json-validate`.

### 3.2 Callouts: arms, pure callees, one shared C body (RULED)

**Arms** (three `patterns.rxt` entries per member, `twin_of=<member>`):
- `twin` -- the site removed, written in the common subset (2.2). Its
  expectations are its own.
- `pass` -- the site present, the FULL per-engine wrapper (view build from
  `const rx_ctx *` / `pcre2_callout_block *` / `OnigCalloutArgs *`, caps copy)
  calling a STUB callee that returns continue (M-2). pcrec binding
  `const rx_callout_ref rx_callout_1 = { pass_fn, NULL };` (match_api §11.2).
  Its answers MUST equal `twin`'s.
- `real` -- the real callee through the same wrapper.
- `pass-nofn` (OQ-11 RULED) -- **pcre2-only**: libpcre2 with no callout
  function set ignores the site (pcre2callout(3)). Driver flag
  `--no-callout-fn` (7.3). pcrec and Onig have no equivalent (a site with no
  callee is a pcrec compile/link error; Onig needs a registered function).
- pcrec runs `twin` under `pcrec-vm` as well as `pcrec-auto` (M-2): callouts
  are VM-only, so an `-auto` twin may be DFA-routed and `pass - twin` would
  then compare two engines.
- ASSISTED engines (no site) run `twin` and their assisted `real`.

**Return-code mapping (E-5)** -- the wrapper translates the shared body's
engine-neutral verdict:

| callee verdict | pcrec (match_api §11.4¶1) | libpcre2 (pcre2callout(3) RETURN VALUES) | Oniguruma (oniguruma.h:773-774) |
|---|---|---|---|
| CONTINUE | `RX_PASS` | 0 | `ONIG_CALLOUT_SUCCESS` (0) |
| FAIL (backtrack, next candidate) | `RX_FAIL` (-1) | **+1** (a negative value ABANDONS the match; -1 = NOMATCH) | `ONIG_CALLOUT_FAIL` (1) |
| CONSUME n (netstr, pcrec only) | the consumed length (§11.4) | -- | -- |

Control subject in every callout member: the FIRST candidate fails the callee
and the second passes; every engine must report the second (passing -1 through
on libpcre2 would turn it into a no-match).

**Callees** (`bench/unusual/callees/callees.c`): `luhn`, `isbn13`, `member`
(open-addressing set built BEFORE the timed loop, passed as `user`), `netstr`,
`stub`. Each takes `{subject, len, pos, caps[], ncaps, user}` and returns
CONTINUE / FAIL / CONSUME n. **One object** (M-5): `callees.o` built once with
fixed flags (`-O2 -fno-lto`, the box gcc), linked into every driver, its sha256
recorded as compile-scope `engine_metadata` `callees_sha256` (type `sha256`,
v1.7). Wrappers are binding glue, recorded, not budgeted (for NATIVE engines).

**co-netstr (OQ-7 RULED: ASSISTED on libpcre2 and Onig; E-6).** pcrec's native
spelling consumes `len` bytes in one fire; its `netstr` callee returns `RX_FAIL`
when `len` exceeds the remaining subject (a consume past the end TRAPS,
§11.4¶2). The assisted libpcre2 pattern is `(\d{1,9}):(?>(?s:.)*?(?C4)),`
(Onig: `(?{4})`): the atomic lazy run fires once per data byte and the callee
passes only when `pos - (caps[1].end + 1) == len`, so a bad candidate stops at
`len` bytes instead of scanning to the subject end. **PROPOSED** P3: the counted
assist is that check-at-end callee plus the respelled pattern (one string token),
authored blind like any assist (5); it is not a `syntax-only` variant
(requirements v3: a variant reproduces results exactly; this one reproduces the
answer by a different mechanism). The fire count differs by mechanism, so
**no cross-arm subtraction on co-netstr** (M-10); its `twin` is a different
language (`(\d{1,9}):` alone) and serves only as a scan-cost floor.

**Build shape (RULED):** separate translation unit, no LTO, primary for every
engine. **Unity** (pcrec artifact + callees.c + binding in one TU) is a pcrec
option arm, token `cu-unity` (`cu-tu` implicit), and it RECOMPILES callees.c
under pcrec's flags -- declared, its own `callees_sha256` absent.

**Calibration (RULED: fire counts + standalone callee time; OQ-6 RULED 20 % /
40 % vs pcre2-jit).**
1. FIRE COUNTS: an untimed counting build (`-DUB_COUNT`; the timed binary has
   no counter) per (member, subject, engine, ARM), recorded as match-scope
   `engine_metadata` integer `callout_fires`, declared by the adapter that
   produces it; a testee with no counting build omits it (S-10).
2. FIRE VIEWS: each engine's counting build logs its OWN fire-view hashes (M-3).
   `pass` fire multisets are compared across engines and the differences
   reported, not assumed away.
3. STANDALONE CALLEE TIME: a pinned microbench replays EACH engine's logged
   views through the shared body (median of >= 10 fresh launches,
   BOILERPLATE), giving that engine's `callee_ns_per_fire` -- stated as an
   UPPER bound on in-situ cost (warm replay) and cross-checked against
   `(real - pass) / fires`.
4. SHARE = `fires x callee_ns_per_fire / row_ns`, computed on EVERY engine
   (M-4) and printed beside each `real` row. A (member, subject) is flagged
   when pcre2-jit's share exceeds 20 % OR any engine's exceeds 40 %; over 40 %
   on pcre2-jit it is resized before pinned promotion.
5. `real - pass` is reported only where the two arms' `callout_fires` are equal
   (`real` rejects candidates, so downstream work can differ).

**Who computes what (S-12).** `pass == twin` answers: a `check-harness` gate
(`tools/check_unusual.py`, 10). The cost split (`pass - twin`, `real - pass`,
share): a set-sidecar view in the stream/set report (7.5), never an interpreter
rule in v0.1. `twin_of` is added to the pattern-tag vocabulary (L1).

### 3.3 Variables: the memoized escaped-recompile assist (RULED)

NATIVE only on pcrec (`--features vars`; one compile, the per-call `rx_var`
array on `rx_ctx`, vars.md §3-§4). Every other engine is ASSISTED by what an
implementor would do (RULED), honouring vars.md exactly:

- Resolve each `${...}` from the call's binding in host code with vars.md §2's
  table: `${n}`, `${!n}` (= `${n}`, §2), `${n-w}`, `${n:-w}`, `${n+w}`,
  `${n:+w}`, `${n:?w}`; UNSET (`p == NULL`) distinct from EMPTY. A default
  `word` is LITERAL fallback text (`variables_pattern.md`:305) and is escaped
  like a value. The nested chain `${a:-${b}}` is DROPPED from v0.1: the rule for
  `b` UNSET is unspecified in vars.md and is asked of pcrec (deferred E-13).
- UNSET at a bare `${n}`, or UNSET/EMPTY at `${n:?}`, REFUSES the call (vars.md
  §5): the host returns `refused` without calling the engine.
- Escape so the value matches AS ITSELF (vars.md §1), every byte incl. `0x00`;
  vectorscan's `hs_compile` takes a NUL-terminated expression, so 0x00 is
  spelled `\x00` (RE2::QuoteMeta already does; libpcre2/Onig take lengths).
  Rust assists compile with `unicode(false)` (E-7: `rust-default` runs
  `unicode(true)`, where `\xHH` is U+00HH and `(?i)`/`\b` are Unicode-aware;
  `testees/rust/CLAUDE.md`), declared in the identity.
- Interpolate; look up the memo; compile on a miss. Resolution, escaping,
  keying, lookup and every miss compile (libpcre2 incl. `pcre2_jit_compile`;
  vectorscan incl. `hs_alloc_scratch`) are INSIDE the timed row (RULED).
- `va-term`'s case variants are ASCII in v0.1 (E-7: RE2's Latin-1 `(?i)` may
  fold é/É where libpcre2's C tables do not).

**What the time measures (M-6, M-14).** The readout states that a vars stream
ranks largely by miss-compile cost, and that an assisted engine's time measures
THAT assist (its keying, container, escaping), not the engine in the abstract.
It prints pcrec's break-even call count, `pcrec_compile_ns /
(assisted_ns_per_call - pcrec_ns_per_call)` (pcrec's AOT compile is its compile
row). The ledger records each assist's keying, container and sha256 (5.3).

**Value streams (RULED: declared per subject).** `values/<subject>.tsv`: the
binding table (value id -> bytes or UNSET) and the per-call stream. The sidecar
states per subject: stream length, distinct values, reuse order (`zipf-s1.1`,
`round-robin`, `all-distinct`). `va-tenant` runs a DISTINCT-COUNT LADDER `d4`,
`d64`, `d4096` with the stream length FIXED at **16,384 calls** on every rung
(**PROPOSED** P13; M-6), the miss count printed beside each row.

**Memo lifetime:** cleared at the start of every replay, unbounded within it;
compiles per replay = the stream's distinct resolved patterns, recorded as
match-scope `assist_compiles` / `assist_lookups` and checked equal to the
declaration. Freeing the previous replay's compiled regexes / JIT memory
happens OUTSIDE the clock, identically for every engine (7.2).

## 4. Subjects

Subject load is outside timing on every regime. Call counts are manifest
columns; row durations come from L4's dry run (6.5) and are OWED there.

### 4.1 F1 -- cscan segment stream (generated)

`gen_subjects.py`, seeded, sha256 manifest. Filler pattern text between
`(?{ ... })` segments; segment sizes log-uniform 20 B - 5 KB (I-165); bodies
from a declared token mix (identifiers incl. `\x80-\xff` bytes, pp-numbers incl.
C23 `1'000`, string/char literals with escapes, both comment kinds,
backslash-newline splices at a declared rate, nested `{}` and `<% %>` to depth
6, preprocessor lines with balanced braces); ~1 % of segments carry a LOCAL
refusal (raw newline in a literal), each confined to its own segment.

| subject | calls | approx bytes | segment bytes (the throughput denominator, 7.1) |
|---|---|---|---|
| `seg-s` | 256 | 180 KB | manifest column |
| `seg-l` | 4,096 | 3 MB | manifest column |

### 4.2 F2 -- real C bodies

- **sqlite3.c (OQ-3 RULED).** The LATEST SQLite amalgamation at fetch time
  (public domain), xz-vendored as `vendor/sqlite3.c.xz` with the sha256 of
  archive and decompressed file. GATE: the exact URL and sha256 are shown to
  Frank and approved before the download (user CLAUDE.md "Security"); the
  resolved version is recorded in `provenance`. Subjects: `sqlite-bodies`
  (every function body located by the reference scanner, 8, wrapped `(?{ body
  })`, ~7 MB, one call per body; expected ~10^4 calls, counted at L3 and
  recorded) and `sqlite-bodies-s` (a deterministic 1-in-16 sample, P14).
- **Kernel sources (OQ-4 RULED).** `kernel/sched/core.c`, `mm/memory.c`,
  `fs/namei.c`, `net/core/dev.c`, `lib/vsprintf.c` at the LATEST STABLE tag at
  fetch time; each file's URL + sha256 shown to Frank and approved before its
  fetch (one approval per file), pinned in `fetch_kernel.py`'s table, fetched to
  `build/unusual/kernel/` (gitignored), never committed. Absent = the
  `kernel-bodies` cells skipped BY NAME. GPL-2.0 text is never redistributed.

### 4.3 F3 -- pathologicals (one call at offset 0) and the depth ladder

Depth rungs (M-8): **128, 512, 1k, 2k, 8k, 10k, 32k, 100k** for `nest-brace-<d>`
and `nest-paren-<d>` (`wild-sexp-balanced`'s own ladder); `nest-digraph-10k`
kept. PREDICTED per engine at the `default` arm (E-12; the `deep` arm in 6):

| subject | content | pcre2-interp | pcre2-jit | pcrec | onig-default |
|---|---|---|---|---|---|
| `comment-5m` | `(?{ /*` 5 MB `*/ })` | match | match or -46 | match | match |
| `literal-100k` | a 100,000-char `"..."` | match | match | match | match |
| `nest-brace-<d>` / `nest-paren-<d>` | `{`/`(` x d, a token, closers x d | MATCHES to 100k (~19 GiB default heap; libpcre2 matches 800 KB of `^(a(?1)?b)$`, match_api §10.1¶1) | gives up -46 above some rung (32 KiB stack) | gives up `PCREC_ERR_FRAMES` above ~342 levels (limits.md §4) | SILENTLY WRONG above d = 20 (6.3) |
| `nest-digraph-10k` | `<%` x d ... `%>` x d | as above | as above | as above | as above |
| `idents-1m` | 1 MB of identifiers and spaces | match | match or -47 (match_limit, E-4) | match | match |
| `splice-1m` | a 1 MB identifier spliced after every byte | match | match or -47 | match | match |
| `define-witness` | `(?{x})DEFINE` | match (the oracle's span) | same | same | same, via the variant (3.1) |
| `unterminated-5m` | `(?{ /*` 5 MB, no `*/` | NO match | NO match | NO match | NO match |

A crash is a first-class `crashed` outcome; a silently wrong answer is a wrong
answer (excluded, never ranked). Regime `large-subject-throughput`, first match
(`\G` anchors at offset 0). Pathologicals run in FRESH processes (M-9:
`ru_maxrss` is a process high-water).

## 5. The assist: budget, counting, authoring (RULED)

### 5.1 Budget

X = **300 lexical tokens per (MEMBER, engine)** (OQ-1 RULED, "agree I think"),
counted in the engine's binding language (C for libpcre2, Oniguruma,
Vectorscan; C++ for RE2; Rust for rust-regex) with the [B141] rule:
boilerplate excluded against a DECLARED list; standard-library containers free;
C given ONE declared hash-map helper outside the count. Fits = ASSISTED;
exceeds = NOT-CAPABLE, count recorded. Gave-up and crash stay RUNTIME outcomes.
An author MAY write one assist serving several members of a family; its tokens
are then counted in full against EACH member it serves.

### 5.2 Declared before any assist is authored (RULED)

`bench/unusual/assists/RULES.md`: the budget; the counter and version; the
boilerplate list -- includes/`use`, `main`, I/O, the driver-protocol shim (timed
loop, subject loading, result reporting), the shared callees (`callees.c`) and
their per-engine wrappers, `assists/common/ub_map.h` (~60 lines, string ->
pointer) -- each excluded region fenced `/* BOILERPLATE <item> */ ... /* END
BOILERPLATE */`. Counter (OQ-12 RULED: built here, shared with [B141]):
`tools/tokcount.py`, one hand lexer per language, a string/char literal one
token, multi-character punctuators one, a fenced region excluded only when its
item is declared (else the run fails naming it); self-tested on hand-counted
fixtures.

### 5.3 Ledger

`bench/unusual/assists/<member>/<engine>/assist.<ext>` + `assists.tsv`: member,
feature, engine, language, tokens, lines, budget, verdict (ASSISTED /
NOT-CAPABLE), assist sha256, keying (what the memo key is), container, counter
version, author lane, reviewer lane, reviewer verdict.

### 5.4 Authoring (RULED (2))

One BLINDED author lane per (MEMBER, engine): problem statement (the member's
canonical text, intention, the host contract -- vars.md §2-§5 restated
engine-neutrally, the pure-callee contract match_api §11.6¶1, the return-code
table of 3.2), the engine's own documentation, the budget rule with the
boilerplate list, a public self-test sample (cscan: gen_cscan.py's 76 cases;
others: 20 cases per member; the corpus held out), and **BE BRIEF**. Never:
another engine's assist, pcrec's implementation, held-out expectations. A
read-only REVIEWER checks idiomatic-not-golfed (`accepted` / `golfed`, back once /
`not-idiomatic`). The COUNTER produces the count. "Exceeded at N tokens,
abandoned" is a NOT-CAPABLE verdict with its count.

### 5.5 Identity and the capability declaration (C2)

- **One identity token per assisted config**, `assist-v<MAJOR><MINOR>` of the
  set version (`assist-v01` for unusual@0.1; **PROPOSED** P5), in
  `config_extra`. It does NOT vary with which members passed (a re-authored
  member must not split history).
- `compose_config_extra` (`testees/pcrec/CLAUDE.md`:125-135, append-only) gains
  a SIXTH part appended LAST, in the order `lim-ceil1g`, `cu-unity`,
  `assist-v01` (P5); libpcre2's id composition (`adapters.py`:218-222) gains the
  same tokens in the same order.
- `testee.assist` (record, 7.4): an array `[{member, tokens, lines, sha256}]`
  plus set-level `assist_version`; ONE entry per member the config runs
  assisted.
- **Per-member capability (PROPOSED P4).** `REQUIRES_VOCAB`
  (`capability.py`:88-101) grows `vars` and a prefix family `unusual-<member>`.
  Each member pattern carries `requires=<feature>` and
  `requires=unusual-<member>`; an assisted config's `ext bench` block declares
  `unusual-<member>` for every member whose verdict is ASSISTED; a NATIVE
  config declares the feature. A NOT-CAPABLE member is then
  `unsupported-by-declaration` through the existing per-token path
  (capability.py:222-228), with `declaration_ref =
  "bench/unusual/assists/assists.tsv:<row> tokens=<N> budget=300"`.
- NOT-CAPABLE stays distinct from `did-not-compile` (`report.py`:416) and is
  counted excluded, never wrong (`report.py`:1073, :1104).

## 6. Deep nesting: two arms (RULED (4); Q1 RULED)

### 6.1 The arms

`default` = each library's own settings, read back and recorded. `deep` = a
**1 GiB CAP on matcher working storage for EVERY engine** (Q1 RULED, equal
budget), testee token `lim-ceil1g`. The cap is not like-for-like in DEPTH:
frame sizes differ, so 1 GiB buys different maximum depths per engine; a
`deep` give-up means "needs more than 1 GiB of working storage" and nothing
finer. For pcre2-interp the `deep` arm is TIGHTER than its `default` (heap limit
1,048,576 KiB vs the library's 20,000,000 KiB, `pcre2_config`, E-3), said so in
the readout.

### 6.2 Per engine (C7, S-9)

| | `default` (read back, recorded) | `deep` |
|---|---|---|
| pcre2-jit | 32 KiB machine-stack JIT stack (pcre2jit(3) "JIT stack"); match_limit 10,000,000 | `pcre2_jit_stack_create(32 KiB, 1 GiB)` + `pcre2_jit_stack_assign`; `pcre2_set_match_limit(UINT32_MAX)` (E-4: match_limit applies to JIT) |
| pcre2-interp | heap 20,000,000 KiB, match = depth = 10,000,000 | `pcre2_set_heap_limit(1048576)` (KiB); match and depth limits UINT32_MAX |
| pcrec | stack-resident frames (2,048 resume / 3,072 trail, limits.md §3.2; ~342 levels on `^(a(?1)?b)$`, §4); default step/work budgets | the `_in` entries with a 1 GiB caller buffer (match_api §10.2-§10.4; limits.md §5¶6); `--step-budget`/`--work-budget` at maximum |
| onig-default | all six read back (E-10 live values): match_stack 0 (unlimited), retry_in_match 10,000,000, retry_in_search 0, subexp_call_limit_in_search 0, **subexp_call_max_nest_level 20**, parse_depth 4,096 | GLOBAL setters in `driver.c` OUTSIDE the timed loop (no `onig_search_with_param`, so no BD16 edit to `timed.c`): `onig_set_match_stack_limit_size` (oniguruma.h:929) to the 1 GiB equivalent (unit checked at L4), retry limits 0 (unlimited), `onig_set_subexp_call_max_nest_level(1000000)` (:951; P11, 10x the deepest rung) |

**PROPOSED** P10: the cap applies to STORAGE; step/retry/match/depth COUNTERS
are at their type maximum (or 0 = unlimited) in `deep` on every engine that has
them, declared as "counters unbounded, storage capped". Every engine's
effective limits are recorded as pattern-scope `engine_metadata` integers on the
compile row, in both arms.

Buffers and stacks (M-9): the 1 GiB `_in` buffer and the JIT stack are created
ONCE before the timed loop; NOT pre-touched in the timed arm (pre-touching
1 GiB would be a measurement of its own), so page faults of first use are
inside iteration 1 and stated; heap-frame growth during a deep match is inside
the timing for every engine.

**AMENDED 2026-10-29 (b148w1fix, inbox I-170/I-171).** L9's readout found the
"stated" first-use faults were not small: js-1m on pcrec-deep first-touched
~339 MB (82.9k faults, ~109 of ~140 ms of one iteration; x5.9 behind
pcre2-jit in steady state, x21.9 as measured). Storage is STILL not pre-touched
(the maxrss of the 6.4 pass and the cap's meaning stay as ruled). Instead every
`deep` arm, in the `throughput` regime only, runs the driver's own `--prime`
(ONE untimed execution of the timed loop's operation per subject, answer
discarded), declared on the testee as runtime option `storage_prime =
throughput-per-subject`. Call-stream cells (one process, many calls: the faults
amortise) and the untimed `--mem-pass` are unprimed. Honest asymmetry: priming
persists a caller buffer / a JIT stack; libpcre2-interp's heap and Oniguruma's
stack are malloc'd per call, so for them the growth is still re-paid inside the
timed call (the "heap-frame growth is inside the timing" sentence above stands
for them). Unmeasured here (no timing in this lane): the W1 window's js-1m
cell is the first read.

### 6.3 Oniguruma's nest level 20 answers SILENTLY WRONG (E-1)

`onig_get_subexp_call_max_nest_level()` = 20 is a match-time cap that does NOT
error: on `(?<p>\((?:[^()]|(?&p))*\))`, `(`^d`)`^d matches at 0 for d <= 20 and
at offset 1 for d = 21, 80 for d = 100, 980 for d = 1000 (probe). cscan
recurses through `(?&items)` per brace level, so `onig-default` on rungs >= 128
(and any real body nested past ~19) yields a false refusal or a wrong group 1,
never `gave-up`. DECLARED in NOTES.md before any run as wrong-span /
false-no-match BY DESIGN of the default; the `deep` arm raises it (6.2). Whether
it is an upstream bug is deferred (r9, upstream pipeline, after checking
Oniguruma's documentation).

### 6.4 Working-storage high-water (Frank, OQ-5 addition; C8)

Taken in an UNTIMED pass, one fresh process per (subject, engine), with every
instrument OFF in the timed arm. Each value carries its method; values are
**never ranked across methods**.

| engine | `deep_mem_method` | what it measures |
|---|---|---|
| pcrec | `canary` | a random 8-byte canary filling the `_in` buffer, scanned after the call: exact high-water of bytes written (the fill touches 1 GiB, hence untimed only). The `default` arm (stack-resident) has no buffer to fill and no frame-count read-out on the shim's surface: L4 SKIPS its pass and says so (the frame count is OWED, a shim/pcrec ask) |
| pcre2-interp | `counting-alloc` | peak live bytes through a counting `pcre2_general_context` used by the match context AND the match data (L4, measured: the backtracking frames are the MATCH DATA's heap vector, allocated through its own memctl -- the match context alone counted 136 B on a 2,048-deep nest); reported beside libpcre2's own heap-limit accounting |
| pcre2-jit | `mincore` | resident pages of the JIT stack mapping (mmap'd, pcre2jit(3)); page grain, floor 32 KiB; whether sljit grows by touch or `mremap` is settled by the known-depth control |
| onig-default | `rss-delta` | `ru_maxrss` delta in a fresh process (no high-water getter in oniguruma.h:927-951): a coarse upper bound, labelled so |

Reported: the absolute and BYTES PER NESTING LEVEL (slope over two rungs). Two
controls per method: a known-depth control (a subject whose depth and frame
size predict the value) and a no-recursion floor (`literal-100k`). Recorded as
match-scope `engine_metadata` `deep_mem_bytes` + `deep_mem_method` (string)
beside the process high-water. **Amended (L4):** X38 scopes `match.process` to
PROCESS testees (`invocation = "process"`), so a LIBRARY testee -- every engine
here -- records its process high-water as a third match-scope `engine_metadata`
integer, `deep_maxrss_kb` (`ru_maxrss` of the fresh pass process), never as
`process.maxrss_kb`. The three are declared by `pcrecbench.adapters.DEEP_MEM_DECL`
and ride every match row of an `unusual_set` cell whose adapter has a method
(`Adapter.mem_method`); re2, rust and vectorscan have none and omit all three.
Whether subject-grain integers of this size fit the record's metadata model is
checked in L1 (S-14). L4's known-depth controls (`tools/check_calls.py` 5,
cscan over nest-brace-512 vs -2k): pcrec `canary` ~1,120 B per nesting level,
pcre2-interp `counting-alloc` ~1,920 B per level, each with the floor pattern on
`literal-100k` far below.

### 6.5 Give-ups, durations, cap

A give-up NAMES the limit (RULED; `diagnostic` non-empty on `gave-up`,
`record_schema.md` §8): `PCRE2_ERROR_JIT_STACKLIMIT` (-46) vs `_MATCHLIMIT`
(-47) recorded distinctly, `_DEPTHLIMIT` (-53), `_HEAPLIMIT` (-63) (pcre2.h);
`PCREC_ERR_FRAMES` / `_STEPS` / `_WORK` (match_api §4¶1);
`ONIGERR_MATCH_STACK_LIMIT_OVER` (-15), `_RETRY_LIMIT_IN_MATCH_OVER` (-17),
`_RETRY_LIMIT_IN_SEARCH_OVER` (-18), `_SUBEXP_CALL_LIMIT_IN_SEARCH_OVER` (-19),
`ONIGERR_MEMORY` (-5) (oniguruma.h:570-580). An assisted host's own depth
counter is unbounded by construction and declared so. A signal is `crashed`.

The `default` arm is reported as a DEPTH-OF-FAILURE TABLE (rung x engine ->
answer or limit name), not MB/s (M-8). L4 runs a dry-run duration estimate per
(engine, arm) on F3 and sets `CELL_CAP_unusual` (`scripts/run_window.sh`'s
`$CELL_CAP_<set>`, :53-63) from it -- no number is guessed here. A pathological
that hits the cap is recorded `timed-out` by name, as every set's.

## 7. The call-stream regime, protocol, schema v1.11, readers

### 7.1 Semantics (C4)

A stream is the declared call list over one subject: each call is (offset,
length, binding id). cscan F1/F2: the engine is given the rest of the subject
from the call's offset (the compiler's access pattern) but the THROUGHPUT
DENOMINATOR is the sum of the calls' declared segment lengths (manifest), never
the subject size (filler is never scanned); vars: one line per call. `calls` is
the named denominator of calls/s. Per-call result tokens -- `n`,
`m:<s>,<e>[;<g1s>,<g1e>]` (group 0 and, where the pattern has one, group 1
ONLY), `r` (refused) -- are written into a preallocated array inside the loop
and hashed (`results_sha256`) after the clock stops.

**Refused** is engine-neutral: host code returns it without calling the engine
(vars.md §5's unset/empty rule, 3.3); it occurs only in vars streams. cscan's
"no match = refuse" is an ordinary `n`.

**O(segment) pre-flight (L4).** `\G` at a start offset may not bound every
engine's scan (unverified, M-7): a refused/no-match call could cost O(rest of
subject). L4 checks per engine that a no-match call's time does not grow with
the tail (two subjects, one segment, tails differing 10x; scratch, a cleared
window). Where it fails, that engine anchors explicitly (`PCRE2_ANCHORED`,
`onig_match` at the offset, `RE2::ANCHOR_START`, an anchored rust `Input`),
recorded as match-scope `stream_anchor` = `native` | `explicit`.

### 7.2 Iteration, trial agreement, calibration (C3)

One iteration = one FULL REPLAY of the stream. **PROPOSED** P6: the driver
clocks each replay separately and sums; the vars memo is cleared and the
previous replay's compiled objects freed BETWEEN clocks, identically on every
engine. Calibration: replays per trial = the least count whose summed clock is
>= 50 ms (harness_contract.md §3's floor), minimum 1, recorded as `iterations`.
Trial agreement ships as rule **`v1.11-group`** under record_schema.md §4's
rule-revision clause, the [B144] precedent: a `call-stream` row's
`matched-as-expected` trial counts as timed at `iterations >= 1` (as
`substitution` does under `v1.10-group`); every other regime unchanged; X32
versioned by `schema_version`. Touches `reduce.py` (the
`TRIAL_AGREEMENT_RULE` block, :295-327), the validator's mirror
(`validate.py`:269) and X32's text. L1 deliverable.

### 7.3 Driver protocol and harness plumbing (S-5; PROPOSED P7, P8)

- `--mode calls --calls FILE` where FILE is TSV `call_id offset length
  segment_bytes binding_id`; `--bindings FILE` (vars: `binding_id name
  value_hex|UNSET`; **as built by L7**: the bindings table is a FOURTH column of
  the `--list` line, and its value is `hex | UNSET | EMPTY` -- a zero-length hex
  field is not a TSV cell a reader can rely on; a vars call is one LINE matched
  alone, line-relative offsets); `--callees SPEC` binding callout numbers to shared callees
  and `user` (`1=luhn,2=isbn13,3=member:values/users.tsv,4=netstr`, or
  `N=stub` for the `pass` arm); `--no-callout-fn` (`pass-nofn`, pcre2 only).
- Output per trial: the usual timing lines plus one `stream calls= matched=
  nomatch= refused= gave_up= first_limit= results_sha256=` line. Documented at
  the top of `adapters.py` beside `--mode subst` (:72-100).
- `subbench.py` gains `call-stream` in `REGIME_TO_ENUM` / `REGIME_MODE`
  (:28-38).
- Config key `unusual_only = true` on assisted and arm-only configs (the
  `subst_only` analogue, `harness.py`:681-693): such a testee run against any
  other set is refused BY NAME before measuring. `families = [...]` on a config
  (v0.1's text) is withdrawn: per-member scope is the capability declaration
  (5.5).

### 7.4 Record schema v1.11 (OQ-8 RULED; a MINOR bump; S-14)

Fits unchanged: `unsupported-by-declaration` + `declaration_ref`; `gave-up` +
`diagnostic`; `crashed`; `engine_metadata` integers/strings/sha256 (declared by
the producing adapter; a testee that cannot produce one omits it);
`config_extra`; `patterns[].variant`.

Additions: (1) regime `call-stream`; (2) `match_row.stream` = `{calls,
segment_bytes, matched, nomatch, refused, gave_up, results_sha256}`;
(3) `testee.assist` = `{assist_version, members: [{member, tokens, lines,
sha256}]}`; (4) `trial_agreement.rule` value `v1.11-group`. History entry in
`schema/record.schema.json`:6 and `record_schema.md`'s version table (:211-212).
**PROPOSED** P9: an assisted vars member keeps a compile row timing the first
call's resolved pattern, flagged by compile-scope `assist_deferred_compile = 1`;
its compile cost is not ranked (the real compiles are inside the stream row).
Assisted callout members compile normally.

| rule | statement | negative example (`schema/examples/bad/`) |
|---|---|---|
| X47 | `match_row.stream` present iff `regime = call-stream` | a call-stream row without `stream`; a search row with one |
| X48 | `stream.calls = matched + nomatch + refused + gave_up` | sums off by one |
| X49 | `match_outcome = gave-up` iff `stream.gave_up > 0`, and then `diagnostic` names `first_limit` | gave_up 1 with outcome matched-as-expected |
| X50 | `testee.assist` present iff `config_extra` carries `assist-v<..>`; `members[].member` unique; `assist_version` equals the token's | token without the object; a duplicated member |
| X51 | `trial_agreement.rule = v1.11-group` only at schema >= 1.11; under it a call-stream trial is timed at `iterations >= 1` | v1.11-group on a 1.10 record |
| X52 | `deep_mem_bytes` present iff `deep_mem_method` present, method in {canary, counting-alloc, mincore, rss-delta} | bytes without method; method `guess` |
| X53 | `stream.segment_bytes > 0` and `refused = 0` unless the pattern's feature is `vars` | refused 3 on cscan |

The validator cannot hold `results_sha256`'s expectation: the HARNESS compares
it to `expectations_stream.tsv` and sets the outcome, as for X37.

### 7.5 Readers (S-4)

- **Reporter** (BUILT, lane b148rep, `pcrecbench/report_stream.py`): a `--grain stream` view on the [B143] model
  (`pcrecbench/report_subst.py`): ns per stream, calls/s, segment MB/s,
  refused and miss counts, the callout cost split and shares (3.2), the
  depth-of-failure table (6.5), the break-even line (3.3); set grain REFUSES a
  `call-stream` input BY NAME (`report.py`:4343-4360's substitution shape).
- **Viewer / trend / frontpage** (`tools/viewer_export.py`, `tools/trend.py`,
  `tools/frontpage.py`:163): **PROPOSED** P12 -- skip `call-stream` rows BY NAME
  through a declared skip table in v0.1 (none mentions `substitution` today; L1
  checks how each treats an unknown regime and adds the skip).
- **Interpreter / catalogue:** `interpret` reads set-grain TSVs, which never
  carry `call-stream` rows, so no rule fires on them; the non-stream regimes of
  this set flow through R-RANK/R-FLOOR/R-ARM as any set's. No catalogue change
  in v0.1.

## 8. Oracles and expectations (engine-neutral, R-BENCH-4)

pcrec is never asked for an expectation.

| family | primary method | second method (agreement control on every triple both answer) |
|---|---|---|
| cscan | `libpcre2-differential` (interp at the LIBRARY DEFAULT heap, ~19 GiB, not the 1 GiB cap -- E-3) | NEW `reference-scanner`: Python, iterative, regex-free `inline_c.md` §2.3 rules 1-5 + `cscan.rxt`'s three header choices; answers any triple libpcre2 gives up on (declared, as `expectation_methods_v1.md`'s fallbacks); both reproduce gen_cscan.py's 76 cases first |
| wild-sexp-balanced | `libpcre2-differential` | `host-reference`: a Python depth-counting scanner returning the leftmost `(` that opens a balanced group and that group's end (the pattern's first-match language) |
| wild-json-validate | `libpcre2-differential` | Python `json.loads`, divergences declared per subject (2.1) |
| callouts | `libpcre2-differential` with `callees.o` loaded through ctypes as the callout function (the mapping table of 3.2), under default options AND the three no-optimization options (2.2) | `host-reference`: plain Python of each intention |
| vars | `libpcre2-differential` over the resolved, escaped pattern per call (resolution in Python from vars.md §2/§5, independent of any assist) | python `re` with `re.escape` (bytes patterns, ASCII) |

`expectations.tsv` (existing format) for search/throughput;
`expectations_stream.tsv` (subject, pattern, calls, matched, nomatch, refused,
results_sha256, method) for `call-stream`, re-derived under `make check-unusual`
(10) by its own reader, not the generic expectations gate; its run time is
measured at L3 and recorded (OWED; utf8's comparable gate is ~66 s).

## 9. Tiers: scratch first, then pinned (RULED (6))

- **Readout 1, SCRATCH tier** (`run --tier scratch`, `build/scratch-store/`),
  timed at pcrec **9ea9c4a76 (abi 89)** after [B147]'s re-pin merges (the
  callout binding and cscan.rxt live there; cscan.rxt is unchanged through
  pcrec main 614d45eb3). Content: MB/s and calls/s vs libpcre2 JIT and interp,
  the depth-of-failure table and high-water per arm, construct costs, the
  verdict table with token counts, callee shares. Outbox. The run needs a box
  window cleared via pcrec-main (BD3) and Frank's scheduling.
- **Promotion to PINNED** at the next cleared window, same cells, `store/`.
- pcrec's hand-written scanner comparison waits for [INLINE-C] stage 2 (I-165);
  I-166: do not wait for it.

## 10. Build order (lanes)

| lane | content | depends on / gate |
|---|---|---|
| L0 | this note: v0.1 -> r9 -> v0.2 | done at merge |
| L1 | schema v1.11 (7.4: fields, X47-X53 with bad examples, history entry), `v1.11-group` in reduce.py + validate.py + X32 text, `REQUIRES_VOCAB` (`vars`, `unusual-*`), `twin_of` tag, the record-fit check for 6.4's integers, the reader skip tables (7.5) | L0 |
| L2 | `tools/tokcount.py` + `assists/RULES.md` + `ub_map.h`, DECLARED and committed before any L6 lane opens | L0 (parallel with L1) |
| L3 | set skeleton, cscan + wild members, F1/F3 generators, reference scanner + host references, oracle, both expectation files; **GATE Frank: sqlite3.c URL + sha256**, then vendoring; **GATE Frank: the JSON source URL + licence** (2.1); `fetch_kernel.py` with **GATE Frank: each kernel file URL + sha256** | L1 |
| L4 | drivers: `--mode calls` in every adapter (7.3), `unusual_only`, the `deep` configs and limit read-back (6.2), give-up naming, the O(segment) pre-flight, the dry run -> `CELL_CAP_unusual` (scratch, a cleared window) | L1, L3 |
| L5 | callouts: `callees.o`, wrappers + the return-code table, arms incl. `pass-nofn`, counting builds + fire logs, calibration microbench, the Onig witnesses as a gate | L4, [B147] |
| L6 | blinded authors + reviewers (RULED 2026-10-28, Frank: ONE AUTHOR LANE PER (FAMILY, ENGINE), 16 lanes for the 43 (member, engine) pairs -- vars x5, callouts co-luhn/isbn/member x3, co-netstr x5, recursion x3; each member's assist is still COUNTED and scored per (member, engine) against the 300-token budget, 5.1's shared-assist allowance), the pairs being those where the engine is not NATIVE (3.0): vars members x {libpcre2, onig, re2, rust, vectorscan}; co-luhn/isbn/member x {re2, rust, vectorscan}; co-netstr x {libpcre2, onig, re2, rust, vectorscan}; recursion members x {re2, rust, vectorscan} | L2 committed; L3-L5 problem statements and samples |
| L7 | vars members, value streams, pcrec native vars path | L4 |
| L8 | `UNUSUAL_GATE_SKIPS` + its self-test (the `SUBST_GATE_SKIPS` shape, `tools/selfcheck.py`:194-240: the generic floor/manifest/expectations gates told which regimes this set lacks), `tools/check_unusual.py` (counting build, calibration, pass == twin, assist ledger vs counter, memo counts, Onig witnesses, `expectations_stream` re-derive), `make check-unusual` added to `make check` | L1-L7 |
| L9 | scratch readout window (manager), outbox; then pinned promotion | all + a cleared window |

A lane spawns no helpers (BOILERPLATE); author lanes are blinded by their
briefs and run no engine but their own.

## 11. Open questions (genuinely open after the rulings)

- **Q-A (Frank) -- the JSON member's source.** Admit the Stack Overflow
  CC BY-SA validator (2.1) once its URL is shown, or drop the member from
  v0.1. Blocks L3's JSON half only.
- **Q-B (Frank) -- the PROPOSED list** in the change log (P1-P14); each is
  applied as written unless overruled. P4 (the `unusual-<member>` token family)
  and P9 (the assisted vars compile row) touch shared code and are the two
  worth a look.
- **Q-C (pcrec) -- the nested-unset rule** for `${a:-${b}}` with `b` UNSET
  (deferred E-13, outbox with v0.2); a member exercising it follows the answer.
- **Q-D (manager) -- E-1 upstream triage** of Oniguruma's silent nest-level
  answer, after checking its documentation (deferred, r9).
- **Q-E (L4, measured) -- Oniguruma's match-stack limit unit** for the 1 GiB
  equivalent (6.2), and `CELL_CAP_unusual` (6.5): measured, not ruled.
  ANSWERED (lane b148l4): the limit counts STACK ELEMENTS, 32 B each (a limit of
  100,000 gives up at depth 24,999 on `(?<p>\((?:[^()]|(?&p))*\))`, 4 elements
  per level, and ru_maxrss at the give-up is ~3.2 MB = 32.8 B/element); the deep
  arm sets 2^30 / 32 = 33,554,432 and reads it back with
  `lim_stack_elem_bytes` = 32. `CELL_CAP_unusual`: docs/dev/lanes/b148l4_report.md.
