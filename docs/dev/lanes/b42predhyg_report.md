# lane b42predhyg — predictions + adapter-note hygiene ([B42] follow-ups (i)+(ii))

**Task**: two small [B42] follow-ups chartered by Frank at the 2026-09-17
reset, read off `bench/capability@0.1`'s first-sample ledger
(`docs/dev/ledgers/2026-09-17-capability-0.1-first-a770139e.md`):
(i) add the `wild-logparse-quotedstring-grok`/`lp-quoted-escaped`
`pcre2-dfa` divergence (ledger §1.2 Finding B) to
`testees/pcre2/CLAUDE.md`'s divergence table; (ii) fix the predictions
file per `docs/dev/predictions/CLAUDE.md`'s own rules — P5's rank-only
selector is structurally blind to the population it claims to check
(ledger §7.2), and P9 has no row (ledger §7.3). Branch `lane/b42predhyg`,
worktree `worktrees/b42predhyg`.

## (i) The pcre2-dfa divergence — added, live-confirmed, NOT folded into
the family-11 table

`testees/pcre2/CLAUDE.md`'s "Family 11" table is scoped precisely to the
six `semantics-divergence`-family patterns
(`capability_set_v1.md` Appendix A / `bench/capability`'s own family
taxonomy). `wild-logparse-quotedstring-grok` is NOT one of them — its
family is `wild-logparse` (an Apache-2.0 `grok-patterns` QUOTEDSTRING
import). Folding it into that six-row table would misstate its
provenance and quietly change what "family 11" enumerates, so it is a
new subsection immediately after the table's own "Consequence" paragraph
instead, titled to make the relationship explicit (a seventh
`pcre2-dfa` divergence, a different mechanism, same general finding
class).

**Verified independently, not just cited from the ledger.** I did not
take the ledger's Finding B on faith — I reproduced it directly against
this box's `libpcre2-8.so.0` via the same `dlopen`+hand-declared-
prototype convention this adapter's own `driver.c` uses (a short,
throwaway ctypes probe in the session scratchpad, never committed —
`/tmp/.../scratchpad/probe.py`, deleted with the scratchpad at session
end):

```
subject bytes: b'"say \\"hi\\" now"' len 16
pcre2_match rc = 1 span (0, 16) -> b'"say \\"hi\\" now"'
pcre2_dfa_match rc = 1 span (0, 11) -> b'"say \\"hi\\"'
```

— pattern read verbatim (byte-for-byte, via `csv.QUOTE_NONE`, the same
guard `gen_patterns.py` itself now uses per `bench/capability/CLAUDE.md`'s
own "TSV-quoting bug" note) from
`bench/capability/curation/wild/members.tsv` row 8; subject bytes read
from the regenerated `bench/capability/subjects/lp-quoted-escaped.bin`
(`gen_subjects.py` is deterministic — regenerating it to read the
subject did not change the committed `manifest.tsv`). `pcre2_match`
agrees with `expectations.tsv`'s oracle row (`[0,16)`, `libpcre2-
differential`); `pcre2_dfa_match` returns exactly one candidate,
`[0,11)` — five bytes short. This matches the report's own
`wrong-span-or-captures` finding on `dfa-nocaps`, 5/5 trials.

**Mechanism cited precisely, not approximated**: man `pcre2matching`
(this box, `libpcre2-dev` 10.46-1build1) item 1, quoted in full in the
committed note — atomic groups are "matched as if a standalone pattern
... the longest match is then 'locked in'" under DFA matching. Every
alternative in this pattern is wrapped in `(?>...)`; none of family 11's
six patterns contains an atomic or possessive construct (their
divergence is pure alternation ORDER). I did not attempt to re-derive,
step by step, why the DFA's own internal "standalone longest" search
settles on 11 rather than the 14-byte body a naive greedy reading of the
atomic group's alternation would suggest reaches — I state that
honestly in the note (a byte-level trace was not part of this lane's
task, and the family-11 table's own existing entries don't carry one for
every case either, citing the mechanism class rather than deriving it
from source).

File touched: `testees/pcre2/CLAUDE.md` (+65 lines, new subsection only;
no existing prose changed).

## (ii) Predictions — P5 and P9

**What the docs actually say, read before touching anything**
(`docs/dev/predictions/CLAUDE.md`, `docs/design/interpreter_v1.md` §6):
a prediction is "written by hand, by the person who states it, before
the run, committed before the run" (CLAUDE.md, "Writing one"); §6.5's
own check anchors `stated_utc` against the EARLIEST index timestamp for
the population, closing exactly the window where someone reads a run's
real numbers and then backdates a prediction against it. **Nothing in
either document describes a revision mechanism for an already-scored,
already-committed predictions file** — no "supersedes" field, no
`stated_utc` re-issue rule, no versioning clause of the schema/catalogue
shape this project uses everywhere else. Editing
`capability-0.1-first.tsv` in place to fix P5 or add P9 would either (a)
silently rewrite the historical record of what was actually predicted
before the 2026-09-17 run (destroying the very thing `stated_utc`
exists to protect), or (b) require inventing a revision convention this
lane has no authority to charter unilaterally. **I did neither.** The
committed `capability-0.1-first.tsv` is untouched (`git diff` confirms:
only `docs/dev/predictions/CLAUDE.md` and `testees/pcre2/CLAUDE.md`
changed).

### P5 — verified fix, not applied to the scored file

**The bug, precisely** (ledger §3, §7.2): P5's selector
(`pattern=email-nested-plus|trim-nested-star|evil-alt-nested|numeric-id-
nested-plus|phone-list-nested-plus|date-nested-plus;regime_or_na=short-
subject-search;testee=libpcre2_*|pcrec_*`, quantity `n_wrong`, op `eq 0`)
names no `section`. Per `interpreter_v1.md` §6.3's own rule, an
unscoped selector reads the `rank` section only — and a row with
`n_wrong > 0` can never BE a `rank` row (R-STATUS-3 routes it to
`excluded` instead). So P5 is scored against a population it is
mechanically incapable of finding a counterexample in: `interpret`
"confirms" it not because the claim held, but because the tool never
looked where a violation would show up. `evil-alt-nested` — one of P5's
six named patterns — is wrong on `dfa-nocaps`/`auto-nocaps` and times
out on three pcrec captures arms in this exact report (ledger §1.2
Finding C); P5 as scored says nothing about any of that.

**Fix, empirically verified against the real committed report** (not
guessed): add `section=excluded` to the selector and switch the clause
from `quantity n_wrong; reducer identity; op eq; hi 0` to `quantity
section; reducer set_of(pattern); op set-subset` with an empty `hi` —
the exact mechanism P8's own committed clause already uses successfully
(`section=did_not_compile;testee=pcrec_*` / `section` / `set_of(pattern)`
/ `set-subset`). I built a throwaway predictions TSV in the scratchpad
(never committed) and ran the real `pcrecbench interpret` against the
real committed report:

```
$ python3 -m pcrecbench interpret --predictions <scratch>.tsv \
    reports/2026-09-17-capability-0.1-budu-ryzen1600-first-a770139e.tsv
...
R-PRED-2  ...  claim     P5X: section set-subset
R-PRED-2  ...  measured  P5X: {email-nested-plus, evil-alt-nested}
```

`R-PRED-2` is the REFUTED rule — the corrected clause correctly names
the true violating population (both patterns the ledger's manual reading
flagged: `evil-alt-nested`'s wrong-answer/give-up/timeout AND
`email-nested-plus`'s timeout, which P5's prose ("none ... exhibits
catastrophic growth") plainly also covers and the original `n_wrong`-only
form would have missed even if it HAD looked at `excluded`). This is a
strictly more faithful transcription of P5's own English than the
original form, not just a bug patch.

**A residual limit I found and am naming rather than hiding**: the same
mechanism run against a genuinely CLEAN single-pattern population
(isolated as its own clause, `pattern=trim-nested-star` alone) returns
**not evaluable** ("no row in this report matches the selector",
`R-PRED-3`), not confirmed:

```
R-PRED-3  ...  reason  P5Y: no row in this report matches the selector
```

`set-subset` of an empty target set has no way to distinguish "checked
this population and it's clean" from "this selector matched nothing at
all" — a property inherent to the mechanism, not to my fix. It happens
never to have surfaced on P8's own use of the identical shape because
P8's measured set was never empty (it found the two real refusals).
Whoever states the corrected P5 for the next sample should know this
going in: if ALL SIX redos-nested patterns are clean on the next sample,
the corrected clause reads `not evaluable`, not `confirmed` — an honest
description of what the mechanism can and cannot distinguish, not a
regression from the fix.

### P9 — inexpressible, more fundamentally than syntax's own P9/P12

P9's claim (`bench/capability/NOTES.md`): `mojibake-curly-quote`'s
record carries no `patterns[].canonical_text` field (S10's omission
rule), checkable only via `canonical_sha256`. This is a claim about the
RECORD's own schema content — `patterns[]` is inside the JSONL record,
which `interpret` never reads (by design: "a deterministic fact-finder
over a report TSV + `store/index.tsv`", never the record). Neither input
carries per-pattern field-presence facts at any grain. `interpreter_v1.md`
§6.3's closed `quantity` set has no member for "field X is present/absent
in the record" — there is no near-miss token to even attempt, unlike
syntax's own P9 (a span claim, `[4,9]`), which at least has `n_wrong` as
a wrong-but-unattributable proxy signal the design note names explicitly
(§6.4: "the cell's `n_wrong` can say the span was wrong ... nothing ...
can say it was [0,9]"). Capability's P9 has no such proxy at all: nothing
about `n_wrong`, `pass_rate`, or any other report quantity has anything
to do with whether a field is present in the record.

NOTES.md's own text anticipates exactly this ("checkable once the schema
promotion (CB3) and a future measurement land, named here so it is not
overlooked") — P9 was never intended to be `interpret`-scored today. It
is not a "wrong quantity token" mistake the way `predictions-
inexpressible.tsv`'s two fixture rows are (those exist to prove
`interpret` REFUSES a load with a named reason when someone tries to
express an answer/span claim it structurally can't hold); P9 has no
quantity a well-meaning author could mistakenly reach for in the first
place. Documented as ABSENT-by-construction in `docs/dev/predictions/
CLAUDE.md`'s new file entry (not the fixture file — that file's own
role, per `catalogue/CLAUDE.md`, is testing the interpreter's OWN
load-error path on a specific quantity mistake, which this isn't).

### Documentation gap also closed

`docs/dev/predictions/CLAUDE.md`'s "Files" section had no entry at all
for `capability-0.1-first.tsv` (only `syntax-0.1-first.tsv` was
documented, though the capability file has existed and been scored since
2026-09-16/17). Added one, in the same style as the syntax entry:
transcription count, scoring tally against the real report, and the two
findings above (P5's false-positive/fix, P9's absence) with pointers to
the ledger sections and this report.

### Recommendation (not applied): the corrected next file

Per the brief's own instruction, here is the exact recommended shape —
a NEW, separately-dated predictions file for the next `capability@0.1`
sample, stated by whoever charters that run (this lane does not name a
run date or file slug it has no authority to commit to), leaving
`capability-0.1-first.tsv` exactly as committed:

```
prediction_id	clause	source	source_ref	stated_utc	subbench	version	selector	quantity	reducer	op	lo	hi	unit	note
P5	.a	bench/capability/NOTES.md	P5	<TBD, before the next run>	capability	0.1	section=excluded;pattern=email-nested-plus|trim-nested-star|evil-alt-nested|numeric-id-nested-plus|phone-list-nested-plus|date-nested-plus;regime_or_na=short-subject-search;testee=libpcre2_*|pcrec_*	section	set_of(pattern)	set-subset				every redos-nested pattern's search_short cell is ABSENT from the excluded section on every roster testee -- none is wrong, none gives up, none times out (i.e. none exhibits catastrophic growth) on the bounded near-miss subjects [corrected 2026-09-17 from the first-sample transcription's bare n_wrong/no-section clause, which reads the rank section only and cannot see a wrong/give-up/timeout row -- ledger 2026-09-17-capability-0.1-first-a770139e.md SS3/S7.2; verified against the real report by lane b42predhyg, R-PRED-2/-3]
```

with P9 carried as a documented, NOT-transcribed line (matching how
syntax's own inexpressible clauses are handled — absent from the TSV,
present in prose):

> P9 (`mojibake-curly-quote` omits `patterns[].canonical_text`) is
> INEXPRESSIBLE by this format (no `quantity` speaks to record-schema
> field presence) and carries no row in this file, by the same
> construction as syntax-0.1-first.tsv's own P9/P12 omissions.

## Validation

`docs/dev/predictions/` (its `CLAUDE.md`) was touched, so per the
delivery bar:

```
$ cd worktrees/b42predhyg && make check-interpret
gen.py: checked 181 file(s) in 58 fixture(s) -- ok
check-interpret section 1: 12 check(s) passed
check-interpret section 2: 8 check(s) passed
check-interpret section 3: 5 check(s) passed
check-interpret section 4: 103 check(s) passed
check-interpret section 5: 4 check(s) passed
check-interpret section 6: 1 check(s) passed
check-interpret: 133 passed, 0 FAILED
```

Unchanged from the pre-lane count (133; `catalogue/rules.toml`,
`catalogue/fixtures/`, `pcrecbench/interpret.py` were not touched — only
CLAUDE.md prose) — expected, and confirms the doc-only edit didn't
regress anything the interpreter's own checks cover.

The P5/P9 fix itself was validated the way the brief asked for
(empirically, against the real report), not merely reasoned about: the
scratch predictions TSV and its `interpret` output are quoted in full
above (`R-PRED-2` refuted with the correct population; `R-PRED-3`
not-evaluable on the clean-population control) and are reproducible by
anyone from the exact selector/quantity/reducer/op tuple given — no
scratch file was left in the repo (per the mandate: scratchpad only,
never committed).

`testees/pcre2/CLAUDE.md`'s new subsection has no automated check (no
target reads that file); its own live-reproduction transcript above is
the verification, run against this box's real `libpcre2-8.so.0` — the
same verification standard the file's own existing family-11 table uses
("LIVE TRANSCRIPTS ... this box").

## Files changed

- `testees/pcre2/CLAUDE.md` — new subsection (item i), +65 lines.
- `docs/dev/predictions/CLAUDE.md` — new `capability-0.1-first.tsv` file
  entry documenting the P5 false-positive/fix and the P9 absence
  (item ii), +56 lines.
- `docs/dev/lanes/b42predhyg_report.md` — this report.

`docs/dev/predictions/capability-0.1-first.tsv` itself: **unchanged**,
deliberately, per the CRITICAL CARE instruction.

## Handback

Both items delivered. (i) is a straight addition, live-verified,
committed. (ii) is delivered as documentation + a verified, ready-to-use
recommendation rather than a file edit, because the format has no
revision mechanism for an already-scored file and inventing one was out
of this lane's scope — the manager or Frank can now either charter the
next capability sample with the recommended P5/P9 content stated
verbatim above, or rule that a revision mechanism should exist (in which
case that's a `docs/design/interpreter_v1.md` question, not a bench-lane
one). Nothing is OWED beyond that ruling. `make check-interpret`
133/133, unchanged. Branch `lane/b42predhyg` ready for the manager to
merge; not merged by this lane.
