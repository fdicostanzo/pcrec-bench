# Lane b69census report

Task: [B69] — Frank's ruling on the `wild-codegrammar-json-number-extended`
finding (the whole-subject form of a pattern with a trailing `(?x)`
comment refuses to compile on every engine that builds a separate
whole-subject artifact, because the harness's own lexical
`(?:<pattern>)\z` wrapper gets eaten by the comment). THE CENSUS: every
refusal in `bench/capability@0.1`, over the 13-testee roster and both
compile forms, classified into Frank's two cases — (1) every ATTEMPTING
engine refuses (instrument-fail candidate) vs (2) a split refusal
(engine-interesting, pcrec-refuses-while-others-compile called out by
name). No instrument, viewer or catalogue change in this lane — census
only, feeding [B70].

Method: read-only over `store/index.tsv` + `store/records/capability@0.1/
*/*.jsonl`, no `pcrecbench run`, no reporter load, no compile probes
needed (every diagnostic the classification needed was already recorded
on the compile row — `re-probe` was not required for any of the 14
CASE-bearing rows; see "Re-probe note" below for the one place a re-probe
*would* have been needed and why it wasn't). Box: budu-ryzen1600, load1
0.69–0.93 throughout, no heavy suite running, no quiet gate needed for a
compile-only read.

## 1. The roster

The 13-testee roster is copied verbatim from
`reports/2026-09-20-capability-0.1-budu-ryzen1600-fullroster-25b1984f.matrix.tsv`
line 1's own `testees:` clause: `libpcre2_10.46_{dfa-nocaps,interp-caps,
jit-caps}-simdna`, `oniguruma_6.9.10_default-caps-simdna`,
`pcrec_25b1984f_{auto-caps,auto-nocaps,vm-caps,vm-in-caps}-simdna`,
`re2_11.0.0_{default,longest}-caps-simdna`,
`rust_1.13.1_default-caps-simdna`, `tre_0.9.0_default-caps-simdna`,
`vectorscan_5.4.11_block-nosom-nocaps-simd`. For each, the newest
`store/index.tsv` record on `budu-ryzen1600` was loaded — all 13 present,
none stale relative to the pin (`pcrec_25b1984f` is the newest pcrec pin
in the store; older `pcrec_a770139e`/`pcrec_cf0962e3` records exist but
are outside this roster and were not read).

## 2. The pattern-set cross-check

`bench/capability/patterns.rxt` carries exactly 64 `name` lines; the
compile rows across all 13 roster records cover exactly the same 64
pattern ids, both directions (`patterns.rxt` minus compile-row coverage
= `{}`; compile-row coverage minus `patterns.rxt` = `{}`). The census is
total: nothing in the pattern set is unaccounted for.

## 3. The total accounting

157 non-`compiled` compile rows over the 64×2-form×13-testee space:

- **124 `unsupported-by-declaration`** — a POLICY DECLARATION, made
  before the driver ever runs, over **25 distinct patterns**. Per
  testee: `re2-default` 25, `re2-longest` 25, `rust-default` 22,
  `vectorscan-block-nosom` 22, `tre-default` 20, `libpcre2-dfa` 5 (its
  own real backreference limitation), `onig-default` 1,
  `pcrec-auto-caps`/`auto-nocaps`/`vm-caps`/`vm-in-caps` 1 each (all
  five on `negation-scope-lookbehind-var`, a genuine variable-length
  lookbehind feature none of these five declare — expected, not
  investigated further). **These are never counted as refusals below**
  — a declaration is not an attempt, per the brief.
- **33 `did-not-compile`** — the driver was reached and genuinely
  refused, over **7 distinct patterns**, 14 (pattern, form) rows. Per
  testee: `tre-default` 6, `onig-default` 4, `rust-default` 4,
  `vectorscan-block-nosom` 4, `pcrec-auto-caps` 4, `pcrec-vm-caps` 4,
  `pcrec-vm-in-caps` 4, `pcrec-auto-nocaps` 3.

## 4. CASE 1 — every attempting engine refused (instrument-fail candidates)

**Both rows are the (?x)-comment-eats-the-wrapper class, and there are
exactly two of them — no other cause found.**

| pattern | form | attempted & refused | mechanism |
|---|---|---|---|
| `wild-codegrammar-json-number-extended` | `whole-subject` | oniguruma, all 4 pcrec, rust, vectorscan (7/7 attempters) | `(?x)` trailing comment eats `)\z` |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | same 7/7 | same |

Mechanism, confirmed from the raw `.rxt` text and the diagnostics
(`docs/dev/measurements/2026-09-21-capability-refusal-census.txt` §4):
both patterns' `pattern-esc` bodies (`bench/capability/patterns.rxt`
lines 522 and 544) end on a `(?x)` `#...` line comment with **no
trailing newline** — `... )?      # make decimal portion optional"` and
`...u  [0-9a-fA-F]{4}) # and four hex digits"` respectively — the last
byte of the pattern text is a comment character. The harness's whole-
subject artifact is built lexically as `(?:<pattern text>)\z`
(`record_schema.md §5` ADDITIONS 3, `pcrecbench/record.py`'s
`whole_subject_text`), so the appended `)\z` lands ON the same
free-spacing comment line and is swallowed before any engine's parser
ever sees it. Every diagnostic is consistent with parsing literally
`...comment text)\z` as one unterminated comment / unbalanced paren:

```
oniguruma:  onig_new failed (code -117): end pattern with unmatched parenthesis
pcrec (all 4 configs): pcrec: missing closing ) for group (pattern offset 0)
rust:       regex build failed [Syntax]: regex parse error:      (truncated at source — see "gaps found" below)
vectorscan: hs_compile failed (code -4, expression 0): Unterminated comment.
```

`tre-default` never attempts either pattern (already `unsupported-by-
declaration` on `free-spacing` before the form fan-out); `libpcre2`
(all 3) and `re2` (both) never build a separate whole-subject artifact
at all for ANY pattern — their `fact` column reads `same program`, they
reach the whole-subject question through a match-time flag
(`PCRE2_ANCHORED|PCRE2_ENDANCHORED`, RE2's `FullMatch`), never a second
compile — so they are structurally outside this defect's reach, exactly
as `docs/design/capability_set_v1.md §3.5` predicted for "most [B7]
roster engines."

**The negative control, same family, same lane**: the corpus's other two
`free-spacing`-tagged patterns, `codegrammar-xflag` and
`bracket-array-define`, are UNAFFECTED — both compile clean on
whole-subject for every one of the same 7 attempting testees (census
§3). Read against their own raw text: `codegrammar-xflag`'s body ends
`... : \\s*     # colon separator, optional surrounding whitespace\n`
(a trailing NEWLINE after the last comment) and `bracket-array-define`'s
ends `^ (?&brackets) $\n` (no trailing comment at all). This is the
precise, narrow trigger — not "any `(?x)` pattern," but specifically "an
`(?x)` pattern whose raw text ends on an un-newline-terminated `#`
comment" — and it reproduces `docs/dev/ledgers/2026-09-07-b36-syntax-
first-d34c9131.md §9 Q3`'s `mod-x` finding exactly, now on two real wild
patterns instead of one designed witness.

**Sanity anchor, as required**: `wild-codegrammar-json-number-extended`
lands in CASE 1 under the wrapper-comment class, per the charter. It is
now confirmed to have a sibling, `wild-codegrammar-json-stringcontent-
escape`, hitting the identical mechanism — not previously called out by
name anywhere in plan.md/the outbox, worth carrying into [B70]'s fixture
set alongside the original.

**A gap found, not fixed here**: `rust-default`'s diagnostic for both
CASE 1 rows is truncated at the source to `"regex build failed [Syntax]:
regex parse error:"` with the actual parser detail (offset, underline)
omitted — the adapter's driver keeps only the first line of what the
`regex` crate's multi-line error prints. Every other engine's diagnostic
in this census is a full sentence; this one alone is a stub. Worth a
`testees/rust/CLAUDE.md`-side fix (capture the full multi-line message)
but it did not block classification here — the mechanism is over-
determined by the other three engines' diagnostics plus the raw-text
comparison against the two negative controls.

## 5. CASE 2 — split refusal

Twelve (pattern, form) rows over 5 distinct patterns, **every one
already documented elsewhere and consistent with that documentation —
no new pcrec ask found**:

### 5a. pcrec-refuses-while-others-compile (the outbox-candidate class)

| pattern | form | pcrec refuses | others compile | diagnostic |
|---|---|---|---|---|
| `wild-datetime-datefinder-alternation` | plain | `auto-caps`, `vm-caps`, `vm-in-caps` | libpcre2×3, oniguruma, `auto-nocaps`, re2×2, rust, vectorscan | `pcrec: pattern too large: 670159 bytes of emitted code (limit 500000)...` |
| `wild-datetime-datefinder-alternation` | whole-subject | `auto-caps`, `auto-nocaps`, `vm-caps`, `vm-in-caps` | oniguruma, rust, vectorscan | `pcrec: pattern too large: 665238 bytes... (limit 500000)...` |

This is the same emitted-code-size-cap refusal **already sent to pcrec**
as item 5 of `docs/dev/outbox_to_pcrec.md` O-31 (2026-09-17, against pin
`a770139e`): "`wild-datetime-datefinder-alternation`'s refusal is
captures-gated at your 500,000 B code cap (nocaps: 20,411 B — a ~33×
captures code-size multiplier on one wide alternation)." This census
reproduces it at the CURRENT pin, `25b1984f` — the numbers moved (665k–
670k B vs O-31's earlier reading, still ~33× over `auto-nocaps`'s clean
compile) but the shape is identical: captures gate this pattern onto
the size cap, `nocaps` sails through. **No new ask drafted — O-31 item 5
already covers it**; if the manager wants a formal re-confirmation-at-
pin note added to the outbox, the numbers above are ready to paste, but
this lane does not draft a duplicate O-n.

`tre-default` also refuses this pattern on both forms, but for an
UNRELATED, already-documented reason (§5b below) — it is not part of the
pcrec finding.

### 5b. non-pcrec splits (roster context, not pcrec asks)

| pattern | form(s) | who refuses | already documented at |
|---|---|---|---|
| `wild-secrets-username-password-pair` | plain, whole-subject | `tre-default` only | `testees/tre/CLAUDE.md` item 4 |
| `wild-waf-crs-942500-comment-obfuscation` | plain, whole-subject | `tre-default` only | `testees/tre/CLAUDE.md` item 4 |
| `wild-datetime-datefinder-alternation` | plain, whole-subject | `tre-default` (in addition to pcrec, §5a) | `testees/tre/CLAUDE.md` item 4 |
| `balanced-parens-rec` | plain, whole-subject | `onig-default` only | `testees/onig/CLAUDE.md` item 2 |
| `mojibake-curly-quote` | plain, whole-subject | `rust-default` only | `testees/rust/CLAUDE.md` (`binary-nonutf8` family) |

**`tre-default`'s three patterns** (`wild-secrets-username-password-pair`,
`wild-waf-crs-942500-comment-obfuscation`, `wild-datetime-datefinder-
alternation`) all refuse with the identical `tre_regncompb failed (code
11): Invalid character range`. `testees/tre/CLAUDE.md` item 4 names this
exact trio by pattern id already: TRE's POSIX bracket-expression reader
gives backslash no special meaning, so the common PCRE idiom
`[a-zA-Z0-9.@_\-+]` (escaping the hyphen inside a class) is read as
`_`, then `\` as one member, then `-+` forms a DESCENDING range from
`\` (0x5C) to `+` (0x2B) — invalid. That CLAUDE.md explicitly calls this
"a genuine capability-and-portability finding, not a bug to route
around silently," and out of scope to fix by rewriting the corpus
(the design's realism rule authored these patterns from real PCRE
sources). Confirmed here: the diagnostic and pattern set reproduce that
note byte-for-byte at the current pin.

**`balanced-parens-rec` on `onig-default`**: `onig_new failed (code
-116): unmatched close parenthesis`. `testees/onig/CLAUDE.md` item 2
names this exactly — "Recursion: a SPELLING gap, not a capability gap.
`(?1)`, `(?&name)`, `(?0)`... all compile... PCRE's `(?R)` shorthand
does NOT parse at all under Perl_NG (`R` is not a recognised group-
option character...); confirmed on the corpus's own `balanced-parens-
rec`." pcrec and libpcre2 compile this pattern fine (recursion is a
real pcrec feature) — the roster-context inverse of §5a, not a pcrec
finding.

**`mojibake-curly-quote` on `rust-default`**: `pattern is not valid
UTF-8 at byte 0/5: invalid utf-8 sequence of 1 bytes from index N`. This
pattern is the corpus's `binary-nonutf8` family witness — it deliberately
carries a raw, invalid UTF-8 byte in its own pattern TEXT (not just the
subject). `testees/rust/CLAUDE.md` documents the `regex` crate's pattern
SOURCE must be valid UTF-8 as "a genuine structural constraint" and
`rust-default` as "immune by construction" to the I-72 pcrec-side
mojibake bug — this is a separate, permanent, correctly-declared
structural refusal, not related to the (now-fixed) pcrec mojibake issue.

## 6. What the census does NOT cover (context, per the standing rule)

`bench/capability@0.1` excludes the `match` regime SET-WIDE
(`docs/design/capability_set_v1.md §3.5`) — precisely because of this
same wrapper's OTHER two documented defects (`(?R)` recursing into the
wrapper, `\K` unable to report a non-zero start), which are WRONG-ANSWER
failures visible only when the whole-subject artifact is actually
RUN, never at compile time. This census reads compile rows only, so
Q3's `(?R)`-recursion wrong-answer case (confirmed on `bench/syntax`'s
`rec-r-uc`/`f-parens`, not present in `bench/capability`) cannot and
does not appear here by construction — `balanced-parens-rec`'s own
`(?R)` pattern compiles fine on every pcrec whole-subject arm in this
set (§5b), and whether it would give a WRONG match under the wrapper is
untestable in `capability@0.1` as designed. This is not a gap in the
census; it is the reason `match` was excluded from this sub-bench in the
first place, restated so a reader of this report does not read
"compiles clean" as "answers correctly."

## Re-probe note

The brief calls for a re-probe wherever a record's diagnostic is
"missing or ambiguous." Every one of the 14 CASE-bearing (pattern, form)
rows carried a full `diagnostic` string on the record already (§4/§5
above quote them verbatim from the store, not from a re-probe) — the
one exception, rust's truncated multi-line message (§4's "gap found"),
is a fixed property of the adapter's driver (it drops everything after
the first line at the SOURCE, in `testees/rust/driver.rs`'s error
formatting, not in what the record stores), so a compile-only re-probe
through the same pinned adapter would reproduce the identical truncated
string — re-probing would not have surfaced more text. No re-probe was
run.

## Charter-vs-committed checklist

- [x] Newest record per (testee, machine) for capability@0.1 across the
  13-roster engines — `docs/dev/measurements/probe_capability_refusal_census.py`
  §1, committed.
- [x] Every (pattern, form, testee) compile row with outcome != compiled
  collected: pattern, form, testee, diagnostic, plain-twin status —
  archive §3/§4, committed.
- [x] Policy intercepts (`unsupported-by-declaration`) collected
  SEPARATELY, never counted as refusals — archive §5, this report §3.
- [x] CASE 1 classified, every engine that attempted named, mechanism
  argued from evidence (raw pattern text + two negative controls), not
  force-fit — this report §4.
- [x] CASE 2 classified, pcrec-refuses-while-others-compile called out
  by name with diagnostics quoted — this report §5a; the inverse
  (others refuse, pcrec compiles) noted as roster context — §5b.
- [x] Re-probe where a diagnostic was missing/ambiguous — none needed;
  stated explicitly above, with the one near-miss (rust's truncation)
  argued as unfixable by re-probing.
- [x] Sanity anchors: json-number-extended lands in CASE 1 / wrapper-
  comment class (§4); `balanced-parens-rec`'s policy story lands
  consistent with `testees/onig/CLAUDE.md` item 2 (§5b) and with
  `docs/dev/lanes/b58census_report.md`'s own finding about this exact
  pattern — b58census bypassed rust-default's policy declaration with a
  LIVE re-compile and found the raw `regex` crate would actually accept
  `balanced-parens-rec` (misreading `(?R)` as an empty flag group, not
  real recursion — its own documented disagreement, one pattern out of
  64). This census reads the STORE's recorded `compile_outcome`, which
  is always POLICY-FIRST by harness design, so it correctly shows
  `rust-default` as `unsupported-by-declaration` here (the declaration
  fires before the driver runs) — not a contradiction of b58census, a
  different question (what the record says happened vs what the raw
  engine would do if the declaration were bypassed). oniguruma is the
  one roster member that reaches the driver on this pattern and gets a
  genuine, driver-level refusal — the two findings are complementary,
  not overlapping.
- [x] D35 measurement committed:
  `docs/dev/measurements/2026-09-21-capability-refusal-census.txt` +
  `docs/dev/measurements/probe_capability_refusal_census.py`,
  `docs/dev/measurements/CLAUDE.md` updated with the new row.
- [x] `docs/dev/lanes/b69census_report.md` (this file) committed.
- [ ] OWED: a drafted outbox item for pcrec — NOT drafted as a new O-n
  because the only pcrec-interesting split (§5a,
  `wild-datetime-datefinder-alternation`'s size cap) is already O-31
  item 5 and reproduces unchanged in shape at the current pin. If the
  manager wants a formal "reconfirmed at 25b1984f" line added to the
  outbox, the numbers in §5a are ready to paste in; this lane judged a
  brand-new O-n unwarranted for a pure reconfirmation and left the call
  to the manager rather than making it unilaterally.
- [ ] No instrument/viewer/catalogue change — none made, per the brief
  ("this lane changes NO instrument, NO viewer, NO catalogue").
- Not merged — lane branch `lane/b69census`, worktree
  `worktrees/b69census`, left for the manager to review and merge.

## Files touched

- `docs/dev/measurements/probe_capability_refusal_census.py` (new)
- `docs/dev/measurements/2026-09-21-capability-refusal-census.txt` (new)
- `docs/dev/measurements/CLAUDE.md` (new table row)
- `docs/dev/lanes/b69census_report.md` (new, this file)
