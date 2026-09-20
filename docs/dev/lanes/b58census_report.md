# Lane b58census report

Task: the OWED pattern-name-level reconciliation of rust-default's
capability@0.1 compile-outcome split, flagged by the prior lane
(b57rustwindow) in `reports/CLAUDE.md` (~lines 505-535) and wake queue
item 1. No build/test in `~/pcrec` touched; box note observed (pcrec's
I-77 full battery was running the whole session — this lane never ran a
heavy or CPU-wide command, only compile-only work and one sub-millisecond
match probe, load-independent by construction).

## What was asked, and where it landed

1. **The exact set difference, by pattern name, between the matrix's 22
   unsup + 1 refused and the raw census's refused/compiled sets, all 64
   patterns accounted for.** DONE, committed:
   `docs/dev/measurements/2026-09-19-rust-policy-vs-census-diff.txt`
   (source-headed, verbatim script output) +
   `docs/dev/measurements/probe_rust_policy_vs_census_diff.py`
   (reproducing script, imports the real `pcrecbench.subbench`/
   `pcrecbench.capability` — never a re-typed REQUIRES_VOCAB or roster
   copy — plus one live re-compile-and-match through the real
   `testees/rust/adapter.py`).

2. **Archived probe under docs/dev/measurements/, D35 style.** DONE (the
   same file as (1); source header states the bench commit, toolchain,
   box, load, command, and reproducer).

3. **Update reports/CLAUDE.md's flagged paragraph.** DONE: replaced the
   "not re-derived... flagged as a finding" sentence with the derived
   set-difference answer and a pointer to the measurement file. Updated
   `docs/dev/measurements/CLAUDE.md` with a new table row for the two
   new files.

4. **Commit incrementally, write this report, hand back.** DONE below.

## The answer

The policy's 22 `unsup` set and the r1131 census's 22 raw-refused set
share **21 members** and disagree on **exactly one pattern each way**:

| pattern | in policy's `unsup`? | in census's refused? | why |
|---|---|---|---|
| `balanced-parens-rec` | YES | **NO — compiles** | its only REQUIRES token is `recursion`, withheld by rust-default's declaration, so the policy intercepts it before the driver ever sees it. But the raw census (and this lane's own live re-run through the real adapter) shows it genuinely COMPILES. Mechanism, confirmed live: `(?R)` is not rejected syntax in the `regex` crate at all — `R` is one of the crate's real inline flag letters (CRLF-mode), so `(?R)` parses as an ordinary empty flag-setting group, a legal zero-width atom inside `(?:[^()]|(?R))*`. It does not implement recursion: matched against `(a(b)c)`, a real recursive engine matches the whole span `[0,7)`; this compiled regex instead matches only the inner pair, `[2,5)` — `(?R)` contributes nothing. The isolated witness pattern the census/roster uses for the `recursion` token, `a(?R)?b`, happens to hit a *different* refused shape for an unrelated reason (`(?R)?` quantifies the bare flag group directly, and a flag-only group is not a quantifiable atom — confirmed separately: `(?R)`/`a(?R)` alone compile, `(?R)*`/`(?R)?` both refuse with "repetition operator missing expression"). This is the corpus's own instance of the task brief's `possessive-quantifier` shape (syntax accepted, semantics wrong), on a different token. |
| `mojibake-curly-quote` | NO (its token `non-utf8-subject` is satisfied) | YES — refuses | not a disagreement: this is the report's own single `refused` row (not `unsup`), and it refuses for the separate, already-documented I-72 pattern-source-UTF-8 reason (`testees/rust/CLAUDE.md`) in *both* the policy path and the raw census. |

The other 21 patterns in each 22-item set are the exact same 21 names
(full table in the archived probe output) — every one of them has a
withheld token, is intercepted by the policy, and independently refuses
in the raw census for a syntax reason consistent with that token.

Full 64-pattern accounting (bucket counts, confirmed by the script's own
assertions): 21 intercepted-and-census-refused (agree), 1
intercepted-but-census-compiles (`balanced-parens-rec`, the disagreement
above), 1 reaches-driver-and-refuses (`mojibake-curly-quote`), 41
compiles-both (37 untagged patterns + 4 patterns whose tokens are all
satisfied: `codegrammar-xflag`, `wild-codegrammar-json-number-extended`,
`wild-codegrammar-json-stringcontent-escape`, `high-byte-run`).
21+1+1+41 = 64.

## A side finding, not asked for but recorded

`bench/capability/subbench.toml`'s `[[patterns]]` array is **stale**
relative to `patterns.rxt` — it predates the b46tags "REQUIRES-tag
correction wave" (`bench/capability/NOTES.md`, 2026-09-17) and is
missing `requires-backrefs` on `tag-depth3-bound` entirely, plus five
other `requires-*` tokens on other patterns (diff: `python3
bench/capability/gen_patterns.py --sidecar | diff bench/capability/
subbench.toml -`). This is **harmless at runtime**: `subbench.toml` sets
`rxt_source = "patterns.rxt"`, and `pcrecbench/subbench.py`'s loader
ignores the `[[patterns]]` array outright once `rxt_source` is set — the
real harness (and this lane's own script) both read the corrected tags
from `patterns.rxt`, confirmed live (`sb.rxt loaded: True`). It IS a real
trap for a human reader who reads `subbench.toml` directly instead of
asking the loaded `Subbench` object — this lane's own first pass at the
task did exactly that and got `tag-depth3-bound` wrong before the
`gen_patterns.py`/NOTES.md cross-check caught it. Not fixed here
(out of scope for this task, and regenerating `subbench.toml` touches
its whole `[[patterns]]` array, a bigger footprint than this lane's
brief); OWED as a one-line hygiene fix — owner: whoever next edits
`bench/capability`'s patterns, trigger: noticed here so it doesn't
silently mislead a second reader. Recorded in
`docs/dev/measurements/CLAUDE.md`'s new entry and in the archived
probe's own header.

## Charter-vs-committed checklist

1. Set difference by pattern name, all 64 accounted for — **COMPLETE**,
   `docs/dev/measurements/2026-09-19-rust-policy-vs-census-diff.txt`.
2. Archived probe, D35 style — **COMPLETE**, same file +
   `probe_rust_policy_vs_census_diff.py`.
3. `reports/CLAUDE.md` paragraph updated — **COMPLETE**.
4. Committed, report written, handback sent — **COMPLETE** (this file;
   commits on `lane/b58census`, not merged — the manager merges).

No OWED items block the deliverable; the `subbench.toml` staleness above
is a separate, non-blocking hygiene finding, explicitly named OWED with
no assigned trigger date (opportunistic).
