# Problem statement: the NETSTRING assist (member `co-netstr`)

For the blinded author lanes of L6 (unusual_set_v1.md 5.4, 3.2). One author per
(member, engine); this statement is the same for the five engines that need
an assist for it (libpcre2, Oniguruma, RE2, rust-regex, Vectorscan) and it
names no engine's API: you read your engine's own documentation. You will NOT
see any other engine's assist, any engine's native implementation of this
feature, or the held-out expectations. **Be brief.** The budget is 300 lexical
tokens for the member (`assists/RULES.md`); a short, idiomatic assist is the
goal, not a golfed one.

## 1. What you are building

A **netstring** is `LEN:DATA,` -- `LEN` is 1 to 9 ASCII digits (leading zeros
allowed; its decimal value is the length), then `:`, then exactly that many
bytes of `DATA` (ANY bytes: `,`, `:`, digits, LF, `0x00`, `>= 0x80`), then `,`.
No regular expression can say "exactly LEN bytes" for a LEN read from the
subject. The native engine that supports it consumes `LEN` bytes in one step;
none of yours does. You write the host code that **answers the same question**:
the first netstring in a subject.

Which shape you use depends on your engine; both answer identically.

- **Shape A -- callout-assisted (libpcre2, Oniguruma).** Your engine has a
  callout point, but no way to consume a counted number of bytes. The shape the
  design gives (it is **proposed**, so you may respell it if your engine's
  syntax needs, but you must keep the mechanism) is the pattern

  ```
  (\d{1,9}):(?>(?s:.)*?(?C4)),          # libpcre2;  Oniguruma: the same with (?{4})
  ```

  an ATOMIC LAZY run of any byte (newlines and `0x00` included) with a callout
  site (number 4) after each step of the run, then the `,`. The callout fires
  at every length of the run, from 0 bytes up. **You author the callee**:
  it receives the subject, its length, the current position `pos` (where the
  run has reached) and group 1's span (the digits, already closed). It PASSES
  exactly when `pos - (end of group 1 + 1)` equals the decimal value of group 1
  (the run is exactly LEN bytes long), and then the pattern's `,` must follow.
  Otherwise it FAILS: reject this position and let the engine take one more
  byte (backtrack into the lazy run). The shared copy of this callee in the set
  is provisional; yours is the counted one, together with the pattern string.
- **Shape B -- host jump (RE2, rust-regex, Vectorscan).** No callouts. Use the
  engine for the regular prefix `(\d{1,9}):` (find its leftmost occurrence at or
  after a given offset), then the host reads LEN from group 1, jumps to
  `colon + 1 + LEN` and checks that a `,` is there (and that the subject is
  long enough). If not, the candidate is dropped and the search resumes at the
  candidate's START + 1.

Either way the engine does the finding. An assist that never calls the engine
measures the host language, not the engine, and is rejected at review
(`not-idiomatic`). Your fixed pattern is compiled once, at setup, outside the
clock; everything per call is inside it.

**Traps, because they are the common mistakes.**

- *A failed callout is not an abort.* Your engine's documentation says how a
  callout reports "reject this position, keep matching" as distinct from "stop
  the whole match with an error". Using the wrong one turns a bad candidate into
  a no-match for the whole call. (One engine's convention is the surprising one:
  read its table of return values.)
- *Candidates can start inside a digit run.* On `12:ab,` the start at offset 0
  declares 12 bytes and fails; the first netstring starts at offset 1 (`2:ab,`).
  And a run of more than 9 digits cannot start a netstring at its first digit
  (nine digits then another digit, not a `:`): `0000000003:abc,` matches from
  offset 1.
- *Everything is bytes.* `.` must match LF and `0x00`; `\d` is ASCII.

## 2. Answer tokens and the call

| token | meaning |
|---|---|
| `n` | no netstring at or after `start` |
| `m:<s>,<e>;<b>,<c>` | the first netstring (leftmost start): `[s, e)` is `LEN:DATA,` whole, `[b, c)` is the `LEN` digits (absolute offsets) |

Your function takes `(subject, start)` and answers the FIRST netstring whose
start is at or after `start`. Subjects are ~1 MB of back-to-back netstrings
(70 %), wrong-length netstrings (20 %: a declared length that does not land on
a `,`) and junk (10 %), plus short subjects. The driver counts non-overlapping
matches itself: after a match `[s, e)` it calls you again at `e`, until `n`;
that count is the sample's `findall`. There is no refusal token and no give-up
token of your own; an engine limit you hit (a callout depth, a stack, a
match limit) is reported by the shim under its own name.

## 3. What fires when (Shape A only)

The lazy run fires the callout once per step: LEN + 1 times for a candidate
whose declared length fits (0 bytes up to LEN bytes), more precisely until the
callee passes. A candidate whose declared length is too long for the subject
runs the lazy run to the END of the subject, firing at every byte: an O(rest of
subject) cost per bad candidate, which is the mechanism's known weakness and is
what the report measures. `fires_first` is the number of fires of the single
first-match search from offset 0, `fires_all` the sum over the whole find-all,
both from libpcre2 10.46 at default options. They are a **check on your Shape
A**, not a contract: an engine's own start optimizations legitimately change
the count on a row that does not match (libpcre2 may decline to start at all
when the subject holds no `,`, which is why several `n` rows read 0). The token is the contract.
Shape B has no callout and reports none. The report makes **no cross-arm
subtraction on this member**: the callout-assisted and the host-jump mechanisms
differ, and the design's `twin` (`(\d{1,9}):` alone) is a different language,
used only as a scan-cost floor.

## 4. What the timing measures (you do not time anything)

Per call: your whole function, every engine search, every callout, the host
jump. A time measures THIS assist (its shape, its restart rule, its callee), not
the engine in the abstract.

## 5. Per-language notes (facts, not designs)

- Byte mode; a subject may contain `0x00` and bytes `>= 0x80`. No NUL-terminated
  or UTF-8-validated subject API.
- `LEN` has at most 9 digits: it fits a 32-bit integer; leading zeros are fine.
- If your engine reports no captures, derive group 1 from the structure
  (`(\d{1,9}):` is fixed); the token is the contract.

## 6. Your public sample

`netstr-samples.tsv` (27 cases): `case, member, subject_hex, subject, expected,
findall, fires_first, fires_all, note`. `subject_hex` is the exact bytes,
`subject` a Python bytes literal for reading, `expected` the token for
`start = 0`, `findall` the non-overlapping count, the fire columns as in
section 3, `note` names the case. Your assist must reproduce every `expected`
and `findall`. The held-out data is different (other bytes, far larger) and is
not shown.

Reading aid:

| case | subject | answer |
|---|---|---|
| co-netstr-01 | `9:greetings,` | `m:0,12;0,1` (10 fires on Shape A) |
| co-netstr-05 | `5:a,b,c,` | `m:0,8;0,1` (a comma inside the data) |
| co-netstr-12 | `8:xyz,` | `n` (declared 8, three bytes then the end) |
| co-netstr-19 | `0000000002:hi,` | `m:1,14;1,10` (ten digits: the start at 1 works) |
| co-netstr-20 | `77:5:world,` | `m:1,11;1,2` (start 0 declares 77; start 1 is `7:5:world,`) |
| co-netstr-27 | `+3:abc, 3 :abc, 3:abc,` | `m:1,7;1,2`, findall 2 |

## 7. Deliverable

One source file in your engine's binding language: the assist function (for
Shape A: the callee and the pattern string, which are the counted content), plus
the declared boilerplate regions fenced as `assists/RULES.md` says (includes,
main, io, the driver-protocol shim, wrappers). No other file. The counter, not
you, produces the token count; over 300 is a NOT-CAPABLE verdict with the count
recorded, which is a valid, honest result: do not golf to avoid it.
