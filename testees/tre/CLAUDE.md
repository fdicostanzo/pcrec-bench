# testees/tre/ — the TRE adapter

Provides one testee: `tre-default`. This is the WHOLE roster, not a first
entry beside later siblings — TRE has no space/speed dial at all (see (c)
below).

Built [B7]/L6b (`capability_set_v1.md` §11.1's per-engine lane row, wave
2), lane `l6btre`, 2026-09-17. TRE 0.9.0-1build1 (`libtre-dev`, this box's
apt candidate — `scripts/install_l6b_deps.sh` verified it installed
before this lane started).

| file | role |
|---|---|
| `adapter.py` | `describe`/`prepare`/`compile`/`measure`; the engine-metadata DECLARATION (`capturecount`, `has_backrefs`, `refusal_class`); the `refusal_class`/`_REFUSAL_SYNTAX_CODES` derivation |
| `driver.c` | the batched in-process timing driver (the protocol is in `pcrecbench/adapters.py`); direct-linked against `libtre.so.5` (`#include <tre/tre.h>`, `-ltre`); the `^(?:...)$` whole-subject wrap |
| `configs.toml` | the one config id, `tre-default` |
| `_probe.rx` | one byte, `a` — the version-probe pattern (`testees/pcre2/_probe.rx`'s own convention) |

## (a) The compile-cost definition

**One phase, `compile`** — `tre_regncompb`, timed in-driver. TRE has no
separate JIT/DFA-construction step exposed at its API (an interpretive
engine building its internal TNFA/backtracking form inside this one call);
the same execution-model class as `pcre2-interp`/`onig-default`.

## (b) `consumed_length`: the convention, stated plainly

**`consumed_length` is the subject length the driver passed and TRE
accepted — i.e. the whole subject.** `tre_regnexecb` takes an explicit
`(str, len)` pair with no separate high-water-mark accessor — the SAME
honest claim `testees/pcre2/CLAUDE.md` and `testees/onig/CLAUDE.md` both
state: *"no byte was withheld or refused"*, never *"the engine looked at
every byte"*.

## (c) The config: why `tre-default` is the WHOLE roster

TRE's three named bounds — `TRE_MAX_RE` = 65536 (max pattern length,
bytes), `TRE_MAX_STRING` = `INT_MAX`, `TRE_MAX_STACK` = 1,048,576 (the
match-time backtracking stack, bytes) — are **fixed compile-time
constants** (`lib/tre-internal.h`, laurikari/tre `master`; NOT public —
no header on this box declares them, cited from source via
`docs/dev/research/2026-09-12-b42-engine-landscape.md` (5)). No
`tre_set_*`-shaped configuration function exists anywhere in `tre.h` or
`regcomp.c`: there is no space/speed dial, no memory cap, nothing to name
a second config after (`capability_set_v1.md` §8's own roster row: "none
— TRE offers no space/speed trade at all on this axis"). `tre_regaexec`'s
approximate-matching cost budget (`regaparams_t.max_cost`) answers a
DIFFERENT question (edit-distance fuzzy matching) and this bench does not
use TRE's approximate-matching extension anywhere.

**Compile flags: `REG_EXTENDED`, deliberately WITHOUT `REG_NEWLINE`.**
Neither `tre_regncompb` call site is given `REG_NEWLINE`; MEASURED live
(this lane, `docs/dev/measurements/2026-09-17-tre-capability-witness-
census.txt`; the reproducing standalone probe used to derive it is
folded into this file's own record), the choice has two consequences,
stated so a future editor does not "fix" it by adding the flag:

1. **`.` MATCHES a newline byte** under `REG_EXTENDED` alone (`a.b` vs
   `"a\nb"` matches). This DIVERGES from PCRE2's default (`.` excludes
   `\n` absent `PCRE2_DOTALL`).
2. **`^`/`$` are SINGLE-LINE anchors** (`^b$` against `"a\nb\nc"` does
   NOT match) — this MATCHES PCRE2's default (`^`/`$` anchor the whole
   subject, not each embedded line, absent `PCRE2_MULTILINE`).

`REG_NEWLINE` would flip (1) the right way but (2) the wrong way — POSIX
offers no flag combination that gets BOTH PCRE2-default behaviors at
once, so (2) (correct anchor scope, matching every other roster member's
default) is kept and (1) is accepted as a stated divergence.

**A further, genuinely useful consequence, MEASURED**: TRE's plain `$`
(no `REG_NEWLINE`) is a **TRUE end-of-string anchor** — `a$` against
`"a\n"` does **NOT** match, unlike PCRE2's own default `$` (which ALSO
matches immediately before a final newline). This makes bare `$` closer
to PCRE2's `\z` than to PCRE2's own `$` — the property the whole-subject
wrap in (e) below depends on.

## (d) Convention: POSIX leftmost-longest, and the syntactic divergences from PCRE

**`conventions: ["posix-leftmost-longest"]`** — the ONE roster member so
far in this repo that does not share the `perl-leftmost-first` convention
every other testee (pcre2, oniguruma, pcrec) is tagged with
(`capability_set_v1.md` §5.6, §8; `docs/design/record_schema.md` §5's
enum). CONFIRMED LIVE, not merely by citing TRE's own documentation
("TRE tries to conform to... POSIX"): `a|ab` against `"ab"` matches
`[0,2)` — the LONGEST alternative, `ab`, not the FIRST one tried (`a`,
which a `perl-leftmost-first` engine reports as `[0,1)`). This makes
`tre-default` the intended first customer of `capability_set_v1.md`
family 11's cross-convention population — currently OUT OF SCOPE for
`harness.outcome_for()`'s scoring (R5 B1, still unbuilt; family 11's v1
scope is narrowed to the shared-`perl-leftmost-first` population,
`capability_set_v1.md` §3.1's own CB1 note) — `tre-default` is graded
against the SAME canonical, `perl-leftmost-first`-authored expectation
row every other testee is, which means a family-11 semantics-divergence
pattern will show `tre-default` as `did-not-match-as-expected` by
construction until that scoring machinery lands, NOT because anything
here is broken.

**Cflags: `REG_EXTENDED`** (POSIX Extended Regular Expressions, TRE's own
extension set layered on top). Chosen over `REG_BASIC` (POSIX BRE, whose
`\(...\)`/`\{...\}` spelling has no relationship to this pcre2-oracled
corpus's syntax at all) — the same choice `capability_set_v1.md` §8
anticipates and the only one that gives POSIX bracket classes, alternation
`|`, and unescaped `+`/`?`/`{...}` the corpus's patterns actually use.

**Every syntactic divergence from PCRE this lane found** (the full
witness census, with every isolated witness AND every corpus-pattern
cross-check, is `docs/dev/measurements/2026-09-17-tre-capability-witness-
census.txt`, `probe_tre_capability_census.py` beside it as the
reproducing script; this is the summary a reader of this file needs
without opening that one):

1. **`\xHH`/`\x{HHHH}` hex escapes DO NOT EXIST.** A backslash before a
   non-special letter or digit that TRE's escape switch does not
   recognise (confirmed by direct source read of `lib/tre-parse.c`,
   `docs/dev/research/2026-09-12-b42-engine-landscape.md` (5)) drops
   SILENTLY to the bare character — `\x93` compiles as the three literal
   characters `x`, `9`, `3`, never byte `0x93`. **Consequence for I-72**:
   the SHARED cross-engine high-byte witness
   (`tools/selfcheck.py`'s `PAT = b"\x93[\\x20-\\x7e]*\x94"`, which is
   PCRE-style regex SOURCE TEXT relying on the ENGINE to interpret the
   `\xHH` escapes) is the WRONG witness for TRE — it would test TRE's
   escape-syntax gap, not I-72's actual transport property (do raw high
   PATTERN BYTES survive the adapter's file-based delivery unmangled).
   This adapter's own I-72 arm (`tools/selfcheck.py`'s `tre-default` arm,
   below) therefore uses the RAW BYTES as a LITERAL pattern (no class, no
   escape) — the identical transport property, without the confound.
2. **Two SILENT MISPARSE hazards this lane found and confirmed
   behaviorally, not merely by compile success** (this is the L5 lesson
   `testees/onig/CLAUDE.md` names — "a first-cut reading... would have
   said yes" — applied here to something worse: TRE does not even
   REFUSE these, it silently reinterprets them):
   - **`\K` (k-reset) compiles and MATCHES LITERALLY.** `a\Kb` compiles
     (`\K` drops to bare `K`, per item 1's rule) and MATCHES `"aKb"` at
     `[0,3)`; it does NOT match `"ab"` — proving conclusively that no
     keep-reset semantics ever fire. A pattern authored assuming PCRE's
     `\K` would silently change MEANING under `tre-default`, not refuse.
   - **`(*NAME)` control verbs compile as an ORDINARY CAPTURING GROUP
     with the leading `*` silently DROPPED.** `a(*FAIL)b` compiles;
     `a(*FAIL)` matches `"aFAIL"` literally (group 1 captures `"FAIL"`,
     confirmed `caps=1:5` in the census), and does **not** match
     `"a*FAIL"`. `(*ACCEPT)` and `(*SKIP)` compile the same way. None of
     the three ever behaves as a control verb.
   - **The one recursion spelling that compiles, `\g<1>`, is the SAME
     hazard as `\K`.** `\g` is not a recognised escape (item 1's rule
     again), so `(a\g<1>?b)` compiles as `(a` + literal `g<1>` (with the
     trailing `?` making the group's tail optional) + `b)` — it matches
     `"ag<1>b"` literally at `[0,6)` and does **not** match the
     genuinely-recursive-shaped `"aabb"`. **No recursion capability was
     found under any spelling** — the other four spellings tried
     (`(?R)`, `(?1)`, `(?<n>a(?&n)?b)`, plus this one's true reading)
     all either REFUSE outright or silently misparse; `recursion` is
     declared UNSATISFIED.
3. **`unicode-properties`: NO `\p{...}` construct exists at all**, not
   even a POSIX ctype-name variant the way Oniguruma's ASCII encoding
   narrows it (`testees/onig/CLAUDE.md` item 3). Both `\p{L}` (a real
   Unicode General Category) and `\p{Alpha}` (a POSIX-style ctype name)
   REFUSE identically (code 10, "Invalid contents of `{}`" — TRE reads
   `\p` as literal `p` and then chokes on `{L}`/`{Alpha}` as an invalid
   bound expression, the SAME failure mode a literal `a{L}` would give).
4. **POSIX bracket expressions give backslash NO special meaning at
   all** — a genuine, corpus-level portability finding beyond the
   REQUIRES_VOCAB tokens. `[a-zA-Z0-9.@_\-+]` (a common PCRE idiom:
   escape the hyphen inside a class) FAILS to compile with **"Invalid
   character range"** (`REG_ERANGE`, code 11), because TRE reads the
   literal sequence `\`, `-`, `+` as: `\` (literal), then `-+` — no,
   precisely: it reads `_`, then `\` as one member, then `-+` forms a
   RANGE from `\` (`0x5C`) down to `+` (`0x2B`) — DESCENDING, hence
   invalid. **Three real bench/capability corpus patterns hit this
   exactly** (`wild-waf-crs-942500-comment-obfuscation`,
   `wild-secrets-username-password-pair`,
   `wild-datetime-datefinder-alternation` — all three tagged with NO
   `requires-*` token, i.e. family 3/4/5's own "none expected to
   refuse" invariant), confirmed by isolating the exact class
   (`[a-zA-Z0-9.@_\-+]`) standalone. The portable POSIX spelling escapes
   nothing and puts the hyphen LAST (`[a-zA-Z0-9.@_+-]`), which DOES
   compile (confirmed) — but rewriting the corpus's own patterns is out
   of this lane's scope (the design's own realism rule authored these
   patterns from real PCRE-syntax sources; TRE's refusal here is a
   genuine capability-and-portability finding, not a bug to route
   around silently).
5. **Two corpus patterns REFUSE for a reason their OWN `requires-*` tags
   do not name**: `quoted-delim-match` (tagged `requires-backrefs` only;
   its actual body is `(["'])(?:(?!\1)[^\\]|\\.)*\1` — the REAL refusal
   cause is the embedded `(?!\1)` negative lookahead, confirmed by
   isolating it; `backrefs` alone compiles fine) and `utf8-lead-no-cont`
   (tagged `requires-non-utf8-subject` only; its body
   `[\xc2-\xdf](?![\x80-\xbf])` also carries a `(?!...)` lookahead).
   Both refusals are correctly EXPLAINED by `tre-default`'s own declared
   `lookaround: NO`, but the corpus's OWN tag completeness (should these
   two also carry `requires-lookaround`?) is out of this lane's scope to
   fix — noted here so a reader of the census does not misattribute
   either refusal to the wrong capability.

   **FIXED (lane `b46tags`, 2026-09-17):** both patterns now carry
   `requires-lookaround` in addition to their original tag
   (`bench/capability/curation/designed/members.tsv`,
   `bench/capability/NOTES.md`'s own "REQUIRES-tag correction wave"
   section). Re-run through `pcrecbench quick` on `tre-default` post-fix:
   both compile rows now read `compile_outcome: unsupported-by-
   declaration`, `declaration_ref` citing `lookaround` by name — the
   pre-compile policy intercepts them before the driver ever runs, in
   place of the raw `tre_regncompb` "Invalid regexp" this section
   documents above.
6. **Genuine, CONFIRMED extensions beyond bare POSIX** (none in
   `REQUIRES_VOCAB`, so none affect the capability declaration below, but
   worth recording — this is the brief's own "TRE actually supports
   minimal repetition — verify by witness" question, settled):
   - **Non-capturing groups `(?:...)`** compile and preserve capture-group
     numbering exactly like the parenthesized-but-uncounted groups every
     other roster engine gives them (confirmed: `(?:ab)c` has
     `re_nsub == 0`) — an UNDOCUMENTED (not named in `doc/regcomp` or the
     bundled headers) but real TRE extension, and the one this adapter's
     own whole-subject wrap in (e) below depends on.
   - **Non-greedy `+?`/`*?` compile AND take REAL effect**, a genuine
     deviation from pure POSIX leftmost-longest once that syntax
     appears: `a+?` against `"aaa"` matches `[0,1)` (shortest), while
     plain `a+` matches `[0,3)` (longest) — CONFIRMED behaviorally, not
     merely a compile-accepts. No corpus pattern in this set's v1 form
     uses `+?`/`*?` syntax, so this convention wrinkle does not currently
     bite, but a future wild import that DOES use non-greedy syntax
     (common in many real-world patterns) would get its literal,
     non-POSIX-longest meaning honoured under `tre-default`, worth
     knowing before assuming "POSIX = always longest" universally.
   - **`(?i)` inline case-fold flag compiles AND WORKS** (`(?i)abc`
     matches `"ABC"`) — another undocumented Perl-ish extension layered
     on the POSIX core, confirmed behaviorally.
   - **`\b`/`\B` word-boundary escapes** and **POSIX bracket classes**
     (`[:alpha:]` etc) work as expected — the corpus's own baseline.

## (e) The whole-subject wrap: `^(?:<pattern>)$`, NOT the shared helper

TRE has no runtime end-anchored mode (no `PCRE2_ENDANCHORED` equivalent),
so the `match` regime is answered on a SECOND artifact — same reasoning
as `testees/onig/adapter.py`'s own two-form model — but **NOT**
`pcrecbench.record.whole_subject_text()`'s `(?:<pattern>)\z`: TRE has NO
`\z`/`\A`/`\Z` tokens at all (confirmed absent from `lib/tre-parse.c`'s
escape switch; a literal `\z` in a TRE pattern compiles as literal `z`,
per (d) item 1's rule).

The wrap is instead `^(?:<pattern>)$`, built INSIDE `driver.c`'s own
`--form whole-subject` branch (kept in ONE place, not duplicated between
python and C):

- `(?:...)` — confirmed a real TRE extension (d.6) — preserves the PLAIN
  form's own capture-group numbering exactly, the same property pcrec's
  and onig's own `(?:...)`-based wraps have.
- `^` binds to the true string start (no `REG_NOTBOL` on this call).
- `$` — (c)'s own finding — is a TRUE end-of-string anchor without
  `REG_NEWLINE`, giving the SAME anchoring contract `\z` gives pcrec's
  and onig's own wraps, just spelled with POSIX syntax instead of a token
  TRE does not have.

**CONFIRMED both directions, live, including the specific control the
`\z`-vs-`$` choice exists to rule out**: `^(?:ab)$` matches `"ab"` at
`[0,2)`; refuses `"xaby"`; and — the control that would have caught the
"TRE's `$` is not really a true end anchor" risk — refuses
`"ab\n"` (a trailing newline does NOT let it through, unlike PCRE2's own
`$`). A real bug was caught and fixed here during this lane's own
validation: an off-by-one in `driver.c`'s wrap-length arithmetic
(`wlen = patlen + 5` where it needed `+ 6` — `strlen("^(?:") + strlen(")$")
== 4 + 2 == 6`) silently truncated the trailing `$` off every
whole-subject artifact, so `^(?:ab)$` was actually being compiled as
`^(?:ab)` (no end anchor at all) — caught by exactly the trailing-newline
control above, not by the plain match/no-match pair, which is why that
control is kept in the committed census rather than trimmed as redundant.

CONFIRMED end to end via `pcrecbench quick --subbench email --regime
match --testee tre-default --vs pcre2-interp` and `--regime
search_short`/`throughput` (this lane's own smoke transcripts, lane
report).

## The I-72 lesson: pattern bytes end to end

This adapter passes the pattern via a FILE (`_compile_one`'s `patfile`/
`--pattern`), exactly like `testees/pcre2/adapter.py`'s and
`testees/onig/adapter.py`'s own convention — never raw pattern bytes
through argv text, where I-72's mojibake bug lived on the pcrec side.
Confirmed live with a TRE-APPROPRIATE witness — (d) item 1 explains why
the shared `\x93[\x20-\x7e]*\x94` class-based witness is the wrong one
here: TRE has no `\xHH` escape, so that exact pattern text would test the
escape-syntax gap, not the transport property I-72 is actually about.
This lane's own witness is the literal bytes `\x93hello\x94` compiled as
an EXACT-MATCH pattern (no class, no escape needed) against the identical
subject: matches `[0,7)` end to end, both via the direct adapter call and
via `tools/selfcheck.py`'s `check_high_byte_pattern_argv`'s new
`tre-default` arm (added additively, verified in isolation).

## `refusal_class`: derived from TRE's closed `reg_errcode_t`, with one honest gap

`tre_regncompb` failure → `did-not-compile` BY NAME, `diagnostic` carrying
`tre_regerror`'s own message text (never re-typed by this adapter).
`refusal_class` (`capability_set_v1.md` §5.5: "declared ONLY by a config
whose engine gives a closed, structural signal" — TRE's `reg_errcode_t`
is exactly that) is derived from the numeric code this driver reports:

- `syntax` for `REG_BADPAT`/`REG_ECOLLATE`/`REG_ECTYPE`/`REG_EESCAPE`/
  `REG_ESUBREG`/`REG_EBRACK`/`REG_EPAREN`/`REG_EBRACE`/`REG_BADBR`/
  `REG_BADRPT`/`REG_BADMAX` (codes 2-10, 13-14 — TRE's full closed
  syntax-error set, `tre/tre.h`'s own enum).
- `size-limit` for `REG_ESPACE` (code 12) **ONLY WHEN** the pattern's own
  byte length (this driver's `info\tpattern_bytes\tN` line) exceeds
  `TRE_MAX_RE` (65536). TRE OVERLOADS `REG_ESPACE` between the compile-
  time length cap (`lib/regcomp.c`: `if (n > TRE_MAX_RE) return
  REG_ESPACE;`) and a genuine allocation failure — the two are
  INDISTINGUISHABLE by code alone (CONFIRMED: a 70,000-byte `a`-run
  pattern fails with the exact same code 12, "Out of memory", as a real
  OOM would). `refusal_class` is left **ABSENT** (never a guessed
  `"memory"`) for a `REG_ESPACE` refusal below the length cap — the same
  "an honest omission is not a wrong classification" rule
  `testees/onig/CLAUDE.md` states for its own parser.

## `gave-up`: PROVISIONED by design, UNWITNESSED on this corpus

Unlike `testees/pcre2/adapter.py`'s and `testees/onig/adapter.py`'s own
MEASURED, ENUMERATED negative-code sets, this driver's gave-up
classification is **generic by construction**: POSIX's own contract for
`regexec`-family functions recognizes only `0` (match) and `REG_NOMATCH`
(no match) as answers, so `driver.c` treats ANY OTHER exec-time return
code as `giveup:<code>:<tre_regerror text>` without a fixed table, and
the adapter declares `giveup_codes = set(range(2, 15))` (TRE's full
non-OK/non-NOMATCH `reg_errcode_t` range) so `harness.classify_giveup`
agrees rather than reclassifying every such row to `crashed` — **an
earlier draft of this adapter declared an EMPTY set here, which would
have silently turned every `giveup:` row into `crashed`; caught during
this lane's own validation, before any measurement used it.**

The one documented match-time budget that COULD produce such a code is
`TRE_MAX_STACK` (1,048,576 B, the backtracking-fallback stack —
`lib/tre-internal.h`). This lane's own probe (`tre_have_backrefs`
confirmed `1` on a five-way backreference pattern,
`(a*)(a*)(a*)(a*)(a*)\1\2\3\4\5b`, run over 40 non-matching `a` bytes
under a 2 s alarm) did **NOT** reproduce it — `REG_NOMATCH` came back
well inside the alarm. `capability_set_v1.md`'s own `redos-nested`
family (10) does not exercise this path either: its patterns are
BACKREFERENCE-FREE by design (the family's whole point is that
backtracker-immune engines like TRE run its patterns via TRE's
LINEAR-TIME TNFA, not the backtracking fallback), so no corpus pattern
in this set's v1 form is expected to reach `TRE_MAX_STACK` at all. This
mechanism is therefore **PROVISIONED, not confirmed live** — stated
plainly rather than hidden, the same restraint `testees/onig/CLAUDE.md`
exercises the other direction (its retry-limit code IS confirmed live).

## `automaton_class`: pattern-dependent, stated in prose

`capability_set_v1.md` §7.1 (S9) gives TRE its own `automaton_class`
column. No single enum token captures a PATTERN-DEPENDENT automaton
switch, so this adapter states it in prose (the same restraint
`testees/pcre2/adapter.py` exercises for `pcre2-dfa`'s own semantic
divergence): backreference-free patterns run TRE's linear-time TNFA
(Thompson-construction); a pattern WITH a backreference (`has_backrefs`,
this file's own `METADATA_DECL`) falls back to a backtracking matcher
bounded by `TRE_MAX_STACK`, per the gave-up section above.

## Correctness: the widest gap of any new engine, MEASURED on `bench/capability@0.1`

The 2026-09-18 capability window
(`docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md` §5.4/§6
item 5) found `tre-default`'s correctness gap the WIDEST of any of the
five new [B7]/L6b engines in the roster's first cross-engine sample —
and on patterns TRE never DECLINED by capability: it compiled them and
answered wrong.

| pattern | regime | pass-rate | detail |
|---|---|---|---|
| `high-byte-run` | throughput | **0.0000** (3/3 wrong) | ALL THREE throughput subjects wrong |
| `high-byte-run` | search | **0.4800** (195/375 wrong) | over half the short subjects wrong |
| `tag-pair-match` | search | 0.9867 (5/75 wrong) | a `backrefs`-only pattern TRE declares satisfied and compiles |
| `wild-waf-crs-942360-concat-sqli` | search | 0.9867 (5/75 wrong) | a WAF SQLi rule, no unusual construct |

(`mojibake-curly-quote`, search, 5/75 wrong at 0.9867, is the SAME
raw-high-byte shape pcrec itself got wrong before its own I-72 fix —
`testees/pcrec/CLAUDE.md`'s "The I-72 fix" section — and TRE reads
wrong on it too.)

**Reading (the ledger's own):** the 0%/48% split on `high-byte-run`,
plus `tag-pair-match` and `crs-942360-concat-sqli` failing on
constructs TRE declares fully satisfied, point at a SYSTEMATIC
raw-high-byte handling gap in `tre_regncompb`'s byte-mode matching, not
a one-off — consistent across three independent patterns, but not
confirmed as TRE's settled behavior: the ledger's own next-sample
checklist (§8 item 2) names the pass-rate split itself (0% throughput
vs 48% search on the identical pattern) as worth re-checking for
reproducibility — a possible one-off box artifact — the next time
`tre-default` measures this set, before treating it as settled.

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

The flag moves the advance only (the absolute start is `pos + rm_so`,
since `pmatch[]` is slice-relative); TRE itself stays byte-literal and is
excluded per-pattern from the utf8 set by `utf8-encoding` (`utf8_set_v1.md`
7.3) -- it ranks there only on three byte-safe members that never match
empty.

## On the utf8 set ([B77] U2): excluded per pattern, witnessed

utf8_set_v1.md 7.3's ruling stands and is now WITNESSED (`docs/dev/measurements/2026-09-25-b77u2-utf8-witness-census.txt`):
`utf8-encoding` NOT (`^.$` over `é` `nomatch`, `(?i)é` over `É`
`nomatch`, `[^é]` over `ü` spans one BYTE -- the byte-decomposed reading
the ruling predicts); `ascii-class-scope` SATISFIED (every byte >= 0x80 a
non-word byte); `unicode-class-scope` NOT -- and a NEW instance of this
file's `(*NAME)` silent-misparse hazard: `(*UCP)\w+` COMPILES and
answers `nomatch` where the oracle matches; `\p{...}` refuses (code 10);
`\x{...}`, lookbehind and `(?m)` refuse. Declares 6/20 on the utf8 set.
