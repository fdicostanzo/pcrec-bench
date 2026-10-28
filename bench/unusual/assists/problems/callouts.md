# Problem statement: the CALLOUT-FILTER assist (family `callouts`: co-luhn, co-isbn, co-member)

For the blinded author lanes of L6 (unusual_set_v1.md 5.4). One author per
(family, engine); this statement is the same for every engine that has no
callouts (RE2, rust-regex, Vectorscan) and it names no engine's API: you read
your engine's own documentation. You will NOT see any other engine's assist,
any engine's native implementation of this feature, or the held-out
expectations. **Be brief.** The budget is 300 lexical tokens per member
(`assists/RULES.md`); a short, idiomatic assist is the goal, not a golfed one.
An assist that serves several members is counted in full against each.

## 1. What you are building

A matcher WITH callouts runs a pattern and, at a marked point, calls a host
function that may veto the candidate; the matcher then backtracks and tries on.
Your engine has no such point. You write the host code that **answers what the
callout-bearing pattern answers**: find the pattern's candidates with the
engine, apply the host predicate to each in order, and answer with the first
candidate that passes.

The engine does the finding. The three members all have the same shape: a
CANDIDATE pattern in the common regex subset (section 2) whose group 1 is
handed to a PREDICATE (section 2); a candidate the predicate rejects is
skipped and the search goes on. An assist that never calls the engine measures
the host language, not the engine, and is rejected at review (`not-idiomatic`).
Your fixed pattern is compiled once, at setup, outside the clock; everything
per call (every engine search, every predicate evaluation) is inside it.

## 2. The three members

A **word byte** is `A-Z a-z 0-9 _`. `\b` is a word boundary between a word byte
and a non-word byte (or the subject's edge). Digits are ASCII `0-9`.

| member | candidate (what the engine finds) | predicate on group 1 |
|---|---|---|
| `co-luhn` | `\b(\d{13,19})\b` -- a maximal run of word bytes that is 13 to 19 digits, nothing else. Group 1 is the whole candidate. | **Luhn**: from the RIGHTMOST digit going left, double every second digit (the 2nd, 4th, ... counted from the right); a doubled digit above 9 loses 9; the sum of all digits is a multiple of 10. |
| `co-isbn` | `\b(97[89]\d{10})\b` -- a maximal word run of exactly 13 digits beginning `978` or `979`. Group 1 is the whole candidate. | **ISBN-13**: weights 1, 3, 1, 3, ... from the LEFT over the 13 digits; the weighted sum is a multiple of 10. |
| `co-member` | `\buser=(\w++)` -- the literal `user=` whose `u` is at a word boundary (so the byte before it, if any, is not a word byte), followed by a maximal run of ONE OR MORE word bytes. Group 1 is that run (the name). Group 0 is `user=` plus the name. | the name is in a fixed SET of names, by exact bytes (case-sensitive). The set is built once, before the clock, and is read-only (how it reaches your code is the shim's business; for the self-test it is the twelve names of section 6). |

(If your lane's brief says the predicate or the set lookup is SUPPLIED as a
shared function, treat it as a function of group 1's bytes returning pass or
fail; otherwise write it. The budget counts only what you write.)

Semantics, exactly as the callout-bearing pattern has them:

1. The candidate is tried at start offsets left to right. At one start, the
   candidate pattern either matches (one way: no length alternative exists in
   these three) or does not. A match is a **candidate**.
2. The predicate runs once per candidate, in order. It **passes**: the
   candidate is the answer, the search ends. It **fails**: the candidate is
   dropped and the search resumes at that candidate's START + 1. (A candidate
   never yields a second candidate at the same start.)
3. The answer is the FIRST passing candidate: its match span (group 0) and group
   1's span, absolute in the subject. No passing candidate: `n`.

**Context rule (important).** Every check of `\b` and of the byte before `user=`
looks at the WHOLE subject, whatever offset the search starts from. A search
that "starts at offset k" must still see byte k-1. Restarting on a copy or
slice of the subject that begins at k changes the answers (a failed candidate's
tail is not a new candidate); the self-test has rows for it.

## 3. Answer tokens and the call

| token | meaning |
|---|---|
| `n` | no passing candidate at or after `start` |
| `m:<s>,<e>;<b>,<c>` | the first passing candidate: group 0 is `[s, e)`, group 1 is `[b, c)` (absolute offsets; for `co-luhn` and `co-isbn` the two spans are equal) |

Your function takes `(subject, start)` and answers the first passing candidate
whose start is at or after `start`. For the throughput subjects (~1 MB of
log-like lines in which a share of the candidates pass and the rest fail, are glued, too short or
too long) the driver counts matches itself: after a match `[s, e)` it calls
you again at `e`, until `n`. That count is the `findall` column of the sample.
There is no refusal token and no give-up token of your own: an engine limit
you hit is reported by the shim under its own name.

## 4. What fires when (the fire count)

A native callout engine reports `callout_fires`: the number of times the
callout point was reached, which here is **the number of candidates the
predicate saw**, in the order above. The sample's `fires_first` is that number
for the single first-match search from offset 0; `fires_all` for the whole
find-all (every call of the driver's loop, summed). Both were produced by
libpcre2 10.46 running the callout pattern, and checked equal to the count of a
plain loop of "search, evaluate, restart at start + 1" over every sample row.
If your design has a natural predicate counter, it should equal them; the
count is not budgeted and not a token of the answer, but a mismatch usually
means your restart rule is wrong.

## 5. What the timing measures (you do not time anything)

Per call: your whole function, the engine searches and the predicate included.
The report prints how many predicate evaluations each engine performs and
what share of a row's time the predicate takes (a "callee share"), so the
cost of the assist loop is visible apart from the engine's scan. A time
measures THIS assist (its restart rule and predicate), not the engine in the
abstract.

## 6. Per-language notes and the self-test set

- Byte mode: `\d` and `\w` must be ASCII, `\b` must be the word-byte boundary
  above, and a subject may contain `0x00` and bytes `>= 0x80`. Configure for
  bytes, not Unicode; do not use an API that wants NUL-terminated or UTF-8
  validated input.
- If your engine reports only match ends, or no captures, derive group 1 from
  the structure of the candidate (it is fixed by section 2); the token is the
  contract.
- The `co-member` self-test SET: `mona nick olga pete quinn rhea sam tina uma
  vic log-shipper ci_runner`. (`log-shipper` can never be a name here: the
  run of word bytes stops at the hyphen. The real run uses another set.)

## 7. Your public sample

`callouts-samples.tsv` (48 cases, 16 per member): `case, member, subject_hex,
subject, expected, findall, fires_first, fires_all, note`. `subject_hex` is the
exact bytes, `subject` a Python bytes literal for reading, `expected` the token
for `start = 0`, `findall` the non-overlapping count, `fires_first` /
`fires_all` as in section 4, `note` names the case. Your assist must reproduce
every `expected` and `findall` of its member; the two fire columns are checks
(section 4). The held-out data is different (other bytes, far larger) and is
not shown.

Reading aid:

| case | subject | answer | fires |
|---|---|---|---|
| co-luhn-03 | `a 4899285250215478 b 5226591108401303 c` | `m:21,37;21,37` (the first fails, the second passes) | 2 |
| co-luhn-08 | `x5226591108401303 y` | `n` (no `\b` before the digits: not a candidate) | 0 |
| co-luhn-05 | `6720097309985876461 3105718041027` | `m:0,19;0,19`, findall 2 | 1 / 2 |
| co-isbn-04 | `ISBN 9781286274900 or 9780583501316` | `m:22,35;22,35` | 2 |
| co-member-03 | `user=zed user=nick` | `m:9,18;14,18` | 2 |
| co-member-10 | `user=mon` | `n` (a prefix of `mona` is not `mona`) | 1 |

## 7a. The predicate is SHARED, not yours (manager ruling, 2026-10-28)

Every engine, native or assisted, calls the SAME compiled predicate: the
Luhn / ISBN-13 / membership functions declared in `bench/unusual/callees/callees.h`
and built once into `callees.o` (unusual_set_v1.md C5: one shared C body). Your
assist CALLS it, through a wrapper fenced as `wrappers` boilerplate
(`assists/RULES.md`); you never reimplement it, and it is not counted, exactly as
it is not counted for an engine with native callouts. What you write and what is
counted is the glue: finding the candidates with your engine, handing each to
the predicate, and turning the answers into the answer token. A wrapper that
does more than forward its arguments is counted as smuggling.

## 8. Deliverable

One source file per member (or one serving several) in your engine's binding
language: the assist function, plus the declared boilerplate regions fenced as
`assists/RULES.md` says (includes, main, io, the driver-protocol shim, and the
wrappers of any shared function your lane's brief supplies). No other file. The
counter, not you, produces the token count; over 300 is a NOT-CAPABLE verdict
with the count recorded, which is a valid, honest result: do not golf to avoid
it.
