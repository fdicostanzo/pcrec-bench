# Problem statement: the RECURSION assist (family `recursion`)

For the blinded author lanes of L6 (unusual_set_v1.md 5.4). One author per
(family, engine); this statement is the same for every engine that has no
recursion (RE2, rust-regex, Vectorscan) and it names no engine's API: you read
your engine's own documentation. You will NOT see any other engine's assist,
any engine's native implementation of this feature, or the held-out
expectations. **Be brief.** The budget is 300 lexical tokens per member
(`assists/RULES.md`); a short, idiomatic assist is the goal, not a golfed one.
An assist that serves several members is counted in full against each.

## 1. What you are building

Your engine's patterns cannot express unbounded nesting. A recursion-capable
matcher answers the three members below with ONE pattern each; you write the
host code that **answers the same question** on your engine: given a subject
(bytes) and a start offset, the first match the member's language gives, as one
answer token (section 3).

What the engine must still do (the rule of this statement): the regular parts
of the work go through your engine's matcher, and only what the engine cannot
do (pairing nested openers with closers: a depth counter or an explicit stack)
is host code. An assist that never calls the engine measures the host
language, not the engine, and is rejected at review (`not-idiomatic`). The
patterns your assist uses are fixed; they are compiled once, at setup, outside
the clock. Everything per call, host loop and every engine call, is inside it.

Two design constraints come from the data, not from taste:

- **No host recursion and no depth cap.** Held-out subjects nest to the order
  of 10^5 levels. A host-stack recursion would crash (a `crashed` outcome); a
  depth cap would answer wrongly. Use a counter or an explicit stack.
- **Work proportional to what the call looks at.** A call never needs the rest
  of the subject after the answer is decided (cscan below), and never copies it.

## 2. The three members (what each one means)

### 2.1 `cscan` -- the end scanner of a C segment

A segment is `(?{` + a C-like body + a closer + `)`, found AT the call's start
offset and nowhere else (anchored: no scanning forward; if no segment starts at
`start` the answer is `n`). The three bytes `(?{` must be literal at `start`.

The body is read left to right from the byte after `(?{`, over the subject with
every **splice removed first**: a backslash immediately followed by LF (`0x0A`)
is invisible to everything below (removal runs left to right; a splice may
fall inside a token, between the two bytes of `<%`, `%>`, `/*`, `*/`, `//`,
or just before a closer). Offsets you report are always in the ORIGINAL bytes.
Depth starts at 1. At each position exactly one of these applies:

| what is read | rule |
|---|---|
| identifier | starts with `A-Z a-z _ $` or a byte `>= 0x80`; continues over those and `0-9`. Taken whole. (`L`, `u8` before a quote are just identifiers.) |
| pp-number | starts with a digit, or `.` followed by a digit; continues over `e E p P` followed by `+` or `-` (both bytes), over `A-Z a-z 0-9 _ . $` and bytes `>= 0x80`, and over a `'` that is followed by one of `A-Z a-z 0-9 _` (a digit separator). |
| string / char literal | `"..."` or `'...'`. A backslash makes the next byte part of the literal (so `\"` does not end it). A raw LF inside the literal is a REFUSAL; a literal that never ends is a refusal. |
| block comment | `/*` to the first `*/` after it (`/*/` is not closed). Opaque. Never ending: refusal. |
| line comment | `//` to the next LF (the LF is then an ordinary byte). Reaching the end of the subject without an LF: refusal. |
| opener | `{` or the two bytes `<%`: depth + 1. |
| closer | `}` or the two bytes `%>`. Depth > 1: depth - 1. Depth 1: this is THE closer; it must be followed immediately (splices skipped) by `)`, else REFUSAL. |
| anything else | one byte, ordinary (`<`, `%`, `>`, `/`, `(`, `)`, `;`, ...). `<` and `%` are ordinary unless they form `<%` / `%>`. |

`{` may be closed by `%>` and `<%` by `}`. The end of the subject inside the
body is a refusal. A **refusal is not an error**: it is the answer `n`.

Answer: `n`, or `m:<s>,<e>;<b>,<c>` where `[s, e)` is the whole segment
(`e` is just after the `)`), and `[b, c)` is the **body**: from `s+3` to the
original offset of the closer's first byte (a splice right before the closer
belongs to the body). All offsets are absolute in the subject.

Call shapes: (a) a **stream**: one subject of up to ~5.5 MB made of filler text
and thousands of segments (20 B to 5 KB each, plus real function bodies of a C
source), one call per segment at its offset; (b) **single calls** at offset 0
on large single-segment subjects: a 5 MB comment, a 100 KB literal, 1 MB of
identifiers, nesting `{{{...` and `(((...` up to 100,000 deep, a 5 MB segment
that is never closed. A call must cost O(its segment), never O(rest of subject).

### 2.2 `wild-sexp-balanced` -- the leftmost balanced parenthesised group

Pattern `(?x)( \( ( [^()]++ | (?1) )* \) )` (the PCRE2 manual's own example).
In words: the answer is the **leftmost** `(` that opens a balanced group, and
that group's end. A group is balanced when it runs from its `(` to the `)`
that returns the nesting depth to zero; every other byte (brackets, quotes,
NUL, bytes `>= 0x80`) is ordinary and parentheses inside a string are not
special. A `)` with nothing open is skipped; a `(` that never closes is not a
match but a LATER `(` may be (`(a (b c) d` -> the group `(b c)`). Leftmost
means leftmost START, so an unclosed `(` before a group can force a look at the
whole rest of the subject.

Answer: `n`, or `m:<s>,<e>` for the first match at or after `start`.

### 2.3 `wild-json-validate` -- a whole-subject JSON validator

Pattern `\A (?&value) \Z` over a `(?(DEFINE) ...)` grammar. The answer is
`m:0,<len>` when the ENTIRE subject is one value of the grammar below, else
`n`. (`\A` is the first byte of the subject, whatever `start` is: a call with
`start > 0` answers `n`.) Where this differs from RFC 8259, the grammar here
wins:

```
ws      = [\t\n\r ]*
value   = ws ( number | "true" | "false" | "null" | string | array | object ) ws
number  = "-"? ( "0" | [1-9][0-9]* ) ( "." [0-9]+ )? ( [eE] [+-]? [0-9]+ )?
string  = '"' ( [^\\"\x00-\x1f] | "\" ["\\bfnrt/] | "\u" hex hex hex hex )* '"'
array   = "[" ( value ( "," value )* )? ws "]"
object  = "{" ( pair ( "," pair )* )? ws "}"
pair    = ws string ws ":" value
```

A fraction or exponent that is started but not completed is simply not
consumed (so `1.` and `1e` leave a byte over and the subject is `n`). Inside a
string every byte except `"`, `\` and `0x00-0x1f` is ordinary, bytes `>= 0x80`
and `0x7f` included (no UTF-8 check). Keywords are exact lower case. Duplicate
keys are fine. Held-out subjects are documents up to ~1 MB, plus near-misses
that break at the last byte, plus short subjects; nesting is not bounded.

## 3. Answer tokens and the call

One token per call, the same alphabet as the other families:

| token | meaning |
|---|---|
| `n` | no match (for `cscan`: also every refusal of 2.1) |
| `m:<s>,<e>` | the first match (`wild-*`): bytes `[s, e)` of the subject |
| `m:<s>,<e>;<b>,<c>` | the first match (`cscan`): segment `[s, e)`, body `[b, c)` |

Your function takes `(subject, start)` and answers the FIRST match whose start
is at or after `start` (`cscan`: exactly at `start`). Offsets are absolute;
bytes before `start` stay visible. For the throughput subjects of the `wild-*`
members the driver counts non-overlapping matches itself: after a match
`[s, e)` it calls you again at `e` (at `s+1` if the match is empty, which
cannot happen here), until `n`. That count is the `findall` column of the
sample. There is no refusal token and no give-up token of your own: your
design is unbounded by construction (the report says so); a limit of the
ENGINE you hit (program size, cache, memory) is reported by the shim under the
limit's own name, not by you.

## 4. What the timing measures (you do not time anything)

The clock covers, per call, your whole function: the host loop, every engine
call, and any scratch the engine needs. Setup (compiling your fixed patterns,
subject loading) is outside. Nothing is cached between calls except what you
hold in the assist's own state; say in one line in the ledger what that state
is. The report will say a time measures THIS assist (its loop and patterns),
not the engine in the abstract.

## 5. Per-language notes (facts, not designs)

- Byte mode throughout: configure your engine for bytes, not Unicode. `\w`,
  `\d`, case and the byte `0xFF` must mean what 2.1-2.3 say.
- A subject may contain `0x00` and bytes `>= 0x80`; do not use an API that
  takes a NUL-terminated or UTF-8-validated subject.
- If your engine reports only whether/where a match ENDS, or has no capture
  groups, derive what the token needs yourself; the token is the contract.
- Do not reach for another library; the engine under test and the standard
  library of the binding language are all you have.

## 6. Your public sample

`recursion-samples.tsv` (125 cases: 44 `cscan`, 25 `wild-sexp-balanced`, 56
`wild-json-validate`): `case, member, subject_hex, subject, start, expected,
findall, note`. `subject_hex` is the exact bytes; `subject` is a Python bytes
literal for reading; `start` is the call's start offset; `expected` is the
token; `findall` is the non-overlapping match count for the two `wild-*` members
(`-` for `cscan`); `note` names the case. Your assist must reproduce all of
its member's rows. The held-out corpus is different (other bytes, far larger)
and is not shown.

Seven rows, as a reading aid:

| case | subject | start | answer |
|---|---|---|---|
| cscan-02 | `zz\n(?{ y = 2; })tail` | 3 | `m:3,16;6,14` |
| cscan-03 | `xx(?{ y = 2; })` | 0 | `n` (no segment AT 0) |
| cscan-14 | `(?{ x; // }\n y; })` | 0 | `m:0,18;3,16` (the `}` is in a comment) |
| cscan-24 | `(?{ <\\\n% y; %\\\n> })` (splices inside both digraphs) | 0 | `m:0,19;3,17` |
| wild-sexp-balanced-06 | `(a (b c) d` | 0 | `m:3,8` |
| wild-json-validate-06 | ` -17 ` | 0 | `m:0,5` |
| wild-json-validate-09 | `{"a":[1,2,3]}\n` | 0 | `m:0,14` |

## 7. Deliverable

One source file per member (or one serving several) in your engine's binding
language: the assist function, plus the declared boilerplate regions fenced as
`assists/RULES.md` says (includes, main, io, the driver-protocol shim). No
other file. The counter, not you, produces the token count; over 300 is a
NOT-CAPABLE verdict with the count recorded, which is a valid, honest result:
do not golf to avoid it.
