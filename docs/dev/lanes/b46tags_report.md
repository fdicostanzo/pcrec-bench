# lane b46tags report — the REQUIRES-tag correction wave (`bench/capability`)

**Task**: [B42] set hygiene — audit and correct every `requires-*` tag on
`bench/capability`'s 64 patterns against the constructs each pattern's
own canonical text actually uses, triggered by lane `l6btre`'s census
finding two under-tagged members (`quoted-delim-match`,
`utf8-lead-no-cont`), witness the behavioral effect of the fix, and
re-derive every committed surface the tags feed.

**Branch**: `lane/b46tags`, `worktrees/b46tags`. Not merged (per the
brief — the manager merges).

## Method

1. Read `pcrecbench/capability.py` (the pre-compile policy:
   `REQUIRES(pattern) ⊄ capabilities(config) ⇒ unsupported-by-
   declaration`, decided before `adapter.compile()`), `bench/capability/
   CLAUDE.md`, `NOTES.md`, and `gen_patterns.py`'s own `REQUIRES_VOCAB`
   / `REQUIRES_OVERRIDE` / `EXT_BENCH_ROSTER` tables to learn the closed
   17-token vocabulary and how a pattern's tags are consumed.
2. Confirmed the two known under-tags via `testees/tre/CLAUDE.md` item
   (d).5 and `docs/dev/lanes/l6btre_report.md` — both are genuine, both
   already carry the wrong tag's ROOT cause on record.
3. Built a mechanical classifier over every pattern's real canonical
   text (`gen_patterns.py.all_patterns()`, the same loader the harness
   uses — never a hand re-transcription of the pattern text):
   - **`backrefs` / `named-groups`**: read via real PCRE2
     `pcre2_pattern_info()` (`PCRE2_INFO_BACKREFMAX`,
     `PCRE2_INFO_NAMECOUNT`) on the ACTUAL compiled pattern — not a
     regex heuristic, the engine's own structural answer.
   - **`lookaround`, `atomic-group`, `possessive-quantifier`,
     `recursion`, `conditionals` (excluding `(?(DEFINE)`),
     `k-reset`, `control-verbs`, `unicode-properties`, `free-spacing`,
     `callouts`**: a textual construct scan (`(?=`/`(?!`/`(?<=`/`(?<!`,
     `(?>`, `*+`/`++`/`?+`/`{n,m}+`, `(?R)`/`(?N)`/`(?&name)`/
     `\g<name>`, `\K`, `(*VERB)`, `\p{...}`, `(?x)`, `(?C...)`).
   - **`span-reporting`, `non-utf8-subject`, `captures`,
     `true-end-anchor`**: per `capability_set_v1.md` §5.1's own table,
     these four are EXECUTION-MODEL facts (what the driver reports),
     not pattern-syntax facts — not derivable from pattern text, and no
     corpus member declares any of them today (confirmed: `grep -c
     '\\p{' patterns.rxt` = 0, no `(*VERB)` anywhere, no possessive
     quantifier anywhere — every token this audit could not verify
     textually is also a token the corpus never claims, so there is
     nothing to check against). Left untouched.
   - Ran the classifier against ALL 64 patterns' declared `requires`
     tags (including `mojibake-curly-quote`, decoded latin-1 for the
     textual scan since its bytes are not valid UTF-8).
4. Every discrepancy the classifier found was then read by eye against
   the pattern's real text before being accepted as a finding (no
   mechanical result was applied blind).

## Findings: six under-tagged patterns, zero over-tagged

All six are DESIGNED members (`curation/designed/members.tsv`'s
`requires` column, `;`-separated) — no `REQUIRES_OVERRIDE` entry in
`gen_patterns.py` (the wild-member path) needed a change.

| pattern | old → new `requires` | evidence |
|---|---|---|
| `quoted-delim-match` | `backrefs` → `backrefs;lookaround` | **l6btre's own finding.** Body `(["'])(?:(?!\1)[^\\]|\\.)*\1` — the `(?!\1)` negative lookahead is the real refusal cause on an engine that has `backrefs` but not `lookaround`. |
| `utf8-lead-no-cont` | `non-utf8-subject` → `non-utf8-subject;lookaround` | **l6btre's own finding.** Body `[\xc2-\xdf](?![\x80-\xbf])` — same shape, `(?!...)`. |
| `tag-depth3-bound` | `-` → `backrefs` | Body `<(\w+)>(?:[^<]|<(\w+)>(?:[^<]|<(\w+)>[^<]*</\3>)*</\2>)*</\1>` uses three numbered backreferences (`\1`/`\2`/`\3`); `pcre2_pattern_info(PCRE2_INFO_BACKREFMAX)` = 3 confirms it. Independently already named in `gen_patterns.py`'s own `vectorscan-block-nosom` comment as "a pre-existing corpus tagging gap" — this lane closes that gap (comment updated in place). |
| `codegrammar-xflag` | `free-spacing` → `free-spacing;named-groups` | Body's `(?<key> [^"\\]+ )` is a real named capturing group inside `(?x)` mode; `PCRE2_INFO_NAMECOUNT` = 1. |
| `bracket-array-define` | `recursion;free-spacing` → `recursion;free-spacing;named-groups` | The `(?(DEFINE) (?<brackets> ... ) )` subroutine target is a named group `(?&brackets)` calls by name; `PCRE2_INFO_NAMECOUNT` = 1. |
| `nested-comment-rec` | `recursion` → `recursion;lookaround` | Body `(/\*(?:[^*/]|\*(?!/)|/(?!\*)|(?1))*\*/)` carries two negative lookaheads (`\*(?!/)`, `/(?!\*)`) alongside the numbered subroutine call `(?1)`. |

**Zero over-tagged patterns found.** The classifier's "declared but not
found" direction fired on exactly two rows (`high-byte-run`,
`utf8-lead-no-cont`, both for `non-utf8-subject`) — both are the
EXECUTION-MODEL token my textual classifier structurally cannot detect
(it is a fact about the subject, not the pattern), not a real over-tag;
both are correct as declared (family 12's own invariant).

No CLOSED-VOCABULARY problem was found: every tag on every pattern,
before and after this lane, is a member of `REQUIRES_VOCAB`
(`gen_patterns.py`'s own `all_patterns()` assertion already enforces
this on every load, and `--check` still passes clean).

**Nothing the vocabulary cannot express was found needed.** No pattern
in the corpus needs a capability this 17-token closed vocabulary lacks
a name for — every discrepancy resolved to an EXISTING token.

## Full-corpus confirmation

Re-ran the same classifier after applying the six fixes: **0 mismatches
across all 64 patterns** (was 6; the two execution-model "extras" above
are expected and excluded from the mismatch count in both runs, since
they are not something the textual/PCRE2-structural method can decide
either way).

## Behavioral witnesses (per the brief's #4)

Both KNOWN fixes, plus the bonus `tag-depth3-bound` finding, were
witnessed flipping from what would have been a raw driver-level refusal
to a clean declaration-level refusal, via real `pcrecbench quick`
(scratch tier) cells and a direct `ctypes` call into the real TRE shared
library (`libtre.so.5`) to reproduce the isolated construct's refusal:

- **`quoted-delim-match` on `tre-default`** (declares `backrefs` but not
  `lookaround`): post-fix compile row —
  `compile_outcome: unsupported-by-declaration`,
  `declaration_ref: "capability@0.1 ext bench: capabilities tre-default
  does not declare lookaround (pattern quoted-delim-match requires
  lookaround)"`. Direct `tre_regncompb` calls confirm the ISOLATED cause:
  the pattern with the backreference alone (no lookahead) compiles fine
  (`re_nsub=1`); the real body (with `(?!\1)`) refuses with `code=2:
  Invalid regexp` — the exact raw refusal the pre-fix tag set (missing
  `lookaround`) would have let the driver hit directly, since
  `tre-default` DOES satisfy `backrefs`.
- **`utf8-lead-no-cont` on `tre-default`**: same shape.
  `compile_outcome: unsupported-by-declaration`, `declaration_ref`
  citing `lookaround`. Direct compile: `[\xc2-\xdf]` alone compiles;
  `[\xc2-\xdf](?![\x80-\xbf])` refuses (`code=2`).
- **`tag-depth3-bound` on `vectorscan-block-nosom`** (bonus — structurally
  cannot ever have satisfied `backrefs`, per Vectorscan's "Back-references
  are unsupported."): post-fix compile row —
  `compile_outcome: unsupported-by-declaration`, `declaration_ref`
  citing `backrefs`. Before this lane the row carried no `requires-*`
  tag at all, so the pattern reached the real Vectorscan compile and
  refused there with Vectorscan's own raw diagnostic — the SAME final
  outcome class (`did-not-compile`'s sibling), but mis-cited (no
  declaration to point at).
- **Satisfied engines re-confirmed unaffected**: `pcre2-interp` (declares
  the FULL vocabulary) and `pcrec-auto` (declares `lookaround`) both
  still MEASURE `quoted-delim-match` normally after the fix — 3/3
  subjects, real match rows, `status: inconclusive-load` (a `quick`-tier
  3-trial artifact, not a canonical-store finding) — not refused.

**No live-roster witness exists today for `codegrammar-xflag`/
`bracket-array-define`/`nested-comment-rec`'s `named-groups`/
`lookaround` additions**: every `ext bench` row that satisfies
`recursion` (`pcre2-*`, `pcrec-*`, `onig-default`) also already
satisfies `free-spacing`/`named-groups`/`lookaround` together — there is
no config on the roster today whose declaration would have let these
three reach a compile attempt on a construct it doesn't have. The fix
is still correct (protects a future roster addition with that gap) and
is evidenced structurally (`PCRE2_INFO_NAMECOUNT`, the literal `(?!`
occurrences) rather than behaviorally. Stated here rather than
overclaimed.

## Derived-surface re-derivation

- `python3 bench/capability/gen_patterns.py` — regenerated
  `patterns.rxt` + `patterns/*.rx` (the `.rx` files are byte-identical:
  only tags moved, not pattern text — confirmed via `git status`
  showing no `patterns/*.rx` diff).
- `python3 bench/capability/gen_patterns.py --check` — clean (64
  patterns, 13 families, round-trips through the real pinned pcrec).
- `python3 bench/capability/gen_provenance.py --check` — clean (64
  rows re-derive; licence/fidelity/attribution/similarity gate all
  clear — untouched by a tag-only change, confirmed rather than
  assumed).
- `python3 bench/capability/gen_variants.py --check` — clean (0 rows,
  unchanged).
- `python3 bench/capability/gen_expectations.py --check` — clean (4990
  expectations re-derive; the pre-existing NOTES/give-up lines are
  unchanged from before this lane — confirmed via `git status` showing
  no `expectations.tsv`/`manifest*.tsv` diff after running it).
- `bench/capability/manifest.tsv`, `manifest_throughput.tsv`,
  `expectations.tsv`, `provenance.tsv`, `variants.tsv`: all UNCHANGED
  (a tag is not a pattern-text or subject-text fact any of these five
  files carry) — confirmed via `git status`, not merely expected.

## Targeted validation (per the boilerplate; no full `make check`, BD3)

- `make check-schema` — **5/73/0** (accepted/rejected-for-cause/wrong),
  clean, twice (before and after the `gen_patterns.py` comment edit).
- `tools.selfcheck.check_capability_policy()` +
  `check_capability_policy_noop_elsewhere()` (imported and called
  directly, not the full `make check-harness`) — **12/12 PASS**, twice.
  These exercise the REAL `quick` CLI against `negation-scope-
  lookbehind-var`/`balanced-parens-rec`/`doubled-word` (pre-existing
  witnesses, untouched by this lane) plus the closed-vocabulary and
  fail-closed rules — none of which this lane's six pattern-tag changes
  touch, so their being unchanged is itself a control that the wave
  didn't disturb the policy's own machinery.
- Six extra real `pcrecbench quick` scratch-tier cells (never entering
  `store/`, all under `build/scratch-store/`, gitignored, not
  committed): the three behavioral witnesses above plus their three
  satisfied-engine controls.
- **OWED, explicitly, per the delivery bar**: `make check-harness` and
  `make check` in full — not run, per the brief's own instruction (the
  manager has a battery running elsewhere; BD3 one-heavy-suite). Exact
  commands: `make check-harness`, `make check`, from the repo root
  after merge, on a quiet box.

## Files touched

- `bench/capability/curation/designed/members.tsv` — the six `requires`
  column fixes (the actual data change).
- `bench/capability/patterns.rxt` — regenerated (tags only; pattern
  text, subjects, and every other block byte-identical).
- `bench/capability/gen_patterns.py` — one comment update (the
  `vectorscan-block-nosom` row's own note about `tag-depth3-bound`,
  marked FIXED in place rather than left stale).
- `bench/capability/NOTES.md` — new "The REQUIRES-tag correction wave"
  section (the evidence table, the roster-witness caveat).
- `bench/capability/CLAUDE.md` — new pointer paragraph.
- `testees/tre/CLAUDE.md` — a FIXED addendum under l6btre's own item
  (d).5, left in place as the historical record of what was found and
  when.
- `docs/dev/lanes/b46tags_report.md` — this file.

## Nothing ambiguous to flag

Every discrepancy this audit found resolved cleanly to an existing
`REQUIRES_VOCAB` token; no pattern needed a capability the vocabulary
has no name for. No candidate found by the mechanical pass was rejected
as a false positive after eyes-on review (all six were confirmed real);
the two "declared but not textually found" rows are the vocabulary's
own execution-model tokens, expected to be invisible to a text-only
scan, and are correct as declared.
