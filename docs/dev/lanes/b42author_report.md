# Lane report — `b42author` (L2: designed members + control twins)

**[B42] restart step (5), L2** per `docs/design/capability_set_v1.md`
§11.1. Branch `lane/b42author`, worktree `worktrees/b42author`.
Status: **COMPLETE, committed.**

## Blinding statement (pcrec D27)

**Read:** `man pcre2pattern` (in full, several sections re-read while
validating lookbehind/recursion syntax against a real engine, see
below); `docs/design/capability_set_v1.md` §1 through §11.1 (the
charter traceability table §1.1, the family taxonomy §3, the
provenance/licensing/realism rules §4, the capability model and
REQUIRES vocabulary §5, the rewrite/hazard rules §6, the metrics table
§7, the option-set roster §8, the `.rxt`-supersession pointer §9, the
public-interface note §10, and the build plan through the L1/L2/L3 rows
of §11.1 — §11.2 onward, §12 and §13 were not needed for this task and
were not read); two `WebSearch` queries against public CVE/security-
advisory sources (moment.js's CVE-2017-18214 and CVE-2022-31129,
ua-parser-js's CVE-2022-25927, and a documented Kubeflow email-validator
ReDoS advisory) — used specifically because family 10's charter
instruction is "author hazard shapes fresh from CVE prose descriptions,"
and this is public advisory text, not any bench-internal material;
`pcre2test` (installed on this box, PCRE2 10.46) and the `man
pcre2pattern` lookbehind-length-limit section, used to actually compile
and match every authored pattern against a real engine rather than
hand-verify syntax.

**Not read:** `testees/`, `pcrecbench/adapters.py` or any other
`pcrecbench/` source file, `store/`, `reports/`, any `docs/dev/ledgers/`
file, lane `b42curate`'s or `b42repin`'s worktree content (an ambient
environment notice mid-session briefly reported this session's cwd as
`worktrees/b42curate` — verified via `pwd`/`git rev-parse` that this
lane never actually `cd`'d there or read anything from it; every command
in this lane used an absolute path into `worktrees/b42author`), and no
existing `bench/*/` set's pattern-file CONTENT (`bench/syntax/`,
`bench/email/`, `bench/loglines/`, `bench/bounded/`, `bench/altwide/`).
`docs/design/requirements.md` was not opened — `capability_set_v1.md`
cited everything this task needed from it.

**Disclosed, not a violation, per the boilerplate's own clause**
("you inherit the session-root CLAUDE.md and memory index at spawn —
context, not tasking"): the harness force-injected several `CLAUDE.md`
files as system-reminders at spawn (the repo root, `docs/`, `docs/dev/`,
`docs/design/`, `docs/dev/lanes/`, `.claude/`). These carry directory-
purpose PROSE (e.g. that `bench/loglines/` is "log-line search over
mostly-FAILING text... 10 goal-authored patterns + floor") but no wild
or designed PATTERN TEXT from any set. Separately, one `ls` (directory
listing, filenames only — `bench/`, `bench/syntax/`) was run early in
this lane to confirm the curation output's own directory-layout
convention before any pattern was authored; no file content under
`bench/syntax/` was opened. Neither exposed any pattern text.

## What was built

35 patterns, all `fidelity: synthesized` (nothing here is a verbatim or
adapted import — that is L1's job), in
`bench/capability/curation/designed/`:
`members.tsv`, `patterns/` (two multi-line files kept unflattened per
Frank's F-Q2 ruling, one genuine non-UTF-8 raw-byte file, a staging
`SHA256SUMS.txt`), `NOTES-draft.md` (per-family contrast, 1-3 sentences
each), `CLAUDE.md`.

**Every pattern was compiled and match-tested against real PCRE2
10.46** (`pcre2test`, installed on this box) rather than hand-checked —
this found one real bug (below) and confirms every other pattern
compiles and matches as designed on at least one positive and, where
relevant, one negative probe subject.

**The one finding:** `negation-scope-lookbehind-var`
(`(?<!\bnot\s+(?:\w+\s+){0,3})\bavailable\b`, as first drafted) failed
PCRE2 compilation with error 125, "length of lookbehind assertion is
not limited." `man pcre2pattern`'s lookbehind section states this
plainly ("Unlimited repetition (for example `\d*`) is not supported")
but the failure mode is easy to miss: an unbounded `\s+`/`\w+` still
fails even when it sits *inside* an already-bounded `{0,3}` outer
repeat — the bound has to be on every quantifier, not just the
outermost one. Fixed to `\s{1,3}`/`\w{1,12}`; the corrected pattern
compiles and gives the intended fixed-window negation-scope answer on
all three probe subjects (commit `a902c85`).

## Per-family counts vs §3.1/§3.2's targets

| family | target members (§3.1) | L2 contributed | what | reconciliation owed |
|---|---|---|---|---|
| 1 `wild-validator` | 8 | 4 twins | `uuid-near-miss`, `base10num-near-miss`, `winpath-near-miss`, `ipv4-near-miss` | **YES** — best-guess pairing against L1's likely imports (the three NAMED grok macros + a canonical OWASP shape); L3 confirms/repairs against L1's actual `provenance.tsv` |
| 2 `wild-logparse` | 6 | 2 (a pair) | `logparse-atomic` / `logparse-atomic-removed` | none for the pair itself (independently authored, not derived from L1's text); L3 confirms it sits beside, not instead of, L1's own verbatim grok import + its own atomic-groups-removed control |
| 3 `wild-waf` | 5 | 0 | — (§3.1: "none — the imports ARE the edge cases") | none — nothing assigned to L2 |
| 4 `wild-secrets` | 4 | 0 | — (§3.1: "none... no authored fallback needed") | none |
| 5 `wild-datetime` | 2 | 0 | — (§3.1: "none") | none |
| 6 `wild-codegrammar` | 5 | 2 (a pair) | `codegrammar-xflag` / `codegrammar-flat` | none — self-contained pair |
| 7 `cap-backref` | 5 | **5 — target met** | `doubled-word`, `tag-pair-match`, `phone-palindrome-6`, `quoted-delim-match`, `dup-param-detect` | none (grep's backref corpus is GPLv3-blocked per §4.2; the one BSD-2 Oniguruma witness is L1's to place, in family 7 or 8) |
| 8 `cap-lookaround` | 5 | **5 — target met** | 3 chained (`pwd-strength-chain`, `float-literal-bound`, `email-local-nodup`) + 1 fixed lookbehind (`currency-lookbehind-fixed`) + 1 variable lookbehind (`negation-scope-lookbehind-var`) | none |
| 9 `cap-recursion` | 4 | **4 — target met** | `balanced-parens-rec` (?R), `bracket-array-define` (DEFINE, multi-line), `nested-comment-rec` (?1), `tag-depth3-bound` (bounded-depth control, no recursion construct) | none |
| 10 `redos-nested` | 6 | **6 — target met** | `email-nested-plus`, `trim-nested-star`, `evil-alt-nested`, `numeric-id-nested-plus`, `phone-list-nested-plus`, `date-nested-plus` — each grounded in a real CVE/advisory | none |
| 11 `semantics-divergence` | 6 | 3 | `router-prefix-order`, `file-ext-order`, `keyword-prefix-order` | expects 3 more from L1's PCRE2/rust-regex testdata wild imports to reach 6 |
| 12 `binary-nonutf8` | 3 | **3 — target met** | `high-byte-run`, `mojibake-curly-quote` (genuine non-UTF-8 raw bytes), `utf8-lead-no-cont` | none |
| floor | 1 | 1 (proposed) | `floor-byte` (`~`) | **YES** — §3.3 requires the byte be calibrated against the real generated subject corpus (a full-length miss on throughput, a hit on 1-2 short subjects); that corpus is `captext.py`, L3's to build. This is a proposal, not a calibrated choice |

**Total L2-authored: 35 patterns** (4 + 2 + 0 + 0 + 0 + 2 + 5 + 5 + 4 + 6
+ 3 + 3 + 1). Families 7, 8, 9, 10 and 12 are fully self-contained at
target; families 1 and 11 have a stated, flagged gap that depends on
L1's concurrent, still-unseen output; families 3, 4, 5 correctly have
zero L2 members per the design's own table; the floor is a proposal
pending L3's calibration.

## Real-engine validation (not merely hand-checked)

Every one of the 35 patterns was compiled and match-tested with
`pcre2test` against PCRE2 10.46 (installed on this box:
`libpcre2-dev` 10.46-1build1) — at least one positive probe subject per
pattern, and a negative probe wherever the pattern's whole point is a
contrast (the atomic/non-atomic pair, the fixed/variable lookbehind
pair, the near-miss validators, the nested-recursion vs. bounded-depth
pair, the alternation-order divergence trio, the raw-byte mojibake
pattern against both a matching and a plain-ASCII subject). This is
PCRE2 syntax and PCRE2's own semantics specifically — it does not
stand in for every roster engine's own dialect, which is L3's/the
adapter lanes' concern once the set is built for real; it does establish
that nothing here is a syntax fiction. One real bug was found and fixed
this way (see above); everything else compiled and matched as intended
on the first attempt.

## Charter-vs-committed checklist

| brief item | status |
|---|---|
| `bench/capability/curation/designed/members.tsv` — family, pattern_id, text, fidelity, inspiration, REQUIRES, twin metadata | **COMMITTED** (`members.tsv`, commits `82f96e5`, `a902c85`) |
| Raw-bytes files for multi-line/non-tame members | **COMMITTED** (`patterns/bracket-array-define.txt`, `patterns/codegrammar-xflag.txt` — both kept genuinely multi-line per F-Q2, never flattened; `patterns/mojibake-curly-quote.txt` — genuine non-UTF-8 raw bytes) |
| Per-family 1-3 sentence contrast statements → `designed/NOTES-draft.md` | **COMMITTED** (`NOTES-draft.md`, one entry per family this lane touched: 1, 2, 6, 7, 8, 9, 10, 11, 12, plus the floor) |
| `bench/capability/curation/designed/CLAUDE.md` (this dir only) | **COMMITTED** — no file created or edited outside `curation/designed/` |
| Lane report with per-family counts, blinding statement, charter-vs-committed checklist | **COMMITTED** (this file) |
| Family 11 expectations | **NOT ATTEMPTED, as instructed** — "No expectations at all are yours" |
| Family 10's under-qualified expectations note | **N/A for this lane's deliverable** — the brief's family-11 note was about family 11, not 10; family 10 needed no such flag (all six compile everywhere per the design's own table) and none was added |
| Oracle/scoring machinery | **NOT TOUCHED**, per blinding and per brief |

**Everything the brief asked for is committed; nothing is OWED to a
background job or a future run.** The one open item is the family-1/11
wild-count reconciliation flagged throughout (`members.tsv`'s `notes`
column, `CLAUDE.md`, the table above) — that is explicitly L3's to
close once L1's `provenance.tsv` exists, not a gap in this lane's own
delivery.

## For the manager, on merge

- Commits: `82f96e5` (the 35 patterns + staging files), `a902c85` (the
  lookbehind fix). Branch `lane/b42author`.
- `members.tsv`'s `twin_of` column for the four family-1 twins uses
  placeholder text ("L1 import, pattern_id TBD") rather than a real
  pattern_id, since L1's output was not visible to this lane. Whoever
  merges L1 and L2's branches should either patch those four cells to
  the real imported pattern_id or leave the placeholder for L3 to
  resolve when it builds the set — either is fine, but do not silently
  drop the `notes` column's caveat when merging.
- This lane never entered `worktrees/b42curate` (verified by `pwd`/
  `git rev-parse` after an ambient environment notice briefly reported
  otherwise) and never read any file under it.
