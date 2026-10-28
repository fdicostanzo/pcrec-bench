# Problem statement: the caller-VARIABLES assist (family `vars`)

For the blinded author lanes of L6 (unusual_set_v1.md 5.4). One author per
(family, engine); this statement is the same for every engine. It names no
engine's API: you read your engine's own documentation. You will NOT see any
other engine's assist, any engine's native implementation of this feature, or
the held-out expectations. **Be brief.** The budget is 300 lexical tokens per
member (`assists/RULES.md`); a short, idiomatic assist is the goal, not a
golfed one.

## 1. What you are building

Your engine has no notion of "a pattern with caller-supplied variables". An
implementor who needed one would, per call, build the pattern text from a
template and the call's variable values, compile it (or fetch a previously
compiled copy), and match. You write that: **the host code that, given a
template, one call's bindings and one line of text, answers what a
variable-aware engine would.**

A call is `(line, binding)`:

- `line` is a byte string (a physical line of log text, no trailing newline).
  It may contain any byte, including `0x00`. It is matched ALONE: its first
  byte is the start of the subject (so `^` matches there), its end is the end
  of the subject (so `$` matches there), and every offset you report is
  relative to the line's first byte.
- `binding` maps variable names to values. A value is one of: bytes (possibly
  containing `0x00`), **EMPTY** (set, zero bytes), or **UNSET** (no value). A
  name the binding does not mention is UNSET. EMPTY and UNSET are different
  states; the operators below tell them apart.

The answer to a call is one token:

| token | meaning |
|---|---|
| `r` | the call is REFUSED (section 3): nothing is matched, the engine is not called |
| `n` | the (resolved) pattern does not match anywhere in the line |
| `m:<s>,<e>` | the FIRST match (leftmost, the engine's usual preference order): bytes `[s, e)` of the line |

Matching is unanchored search in BYTE mode (no UTF, no Unicode properties).
Patterns use PCRE2 syntax and semantics; where your engine's dialect differs
on the small subset these four templates use (`^ $ \b (?i) [0-9] (?: | ) \?`
and literals), you must get the PCRE2 answer.

## 2. The templates (the four members)

```
va-tenant       ^${tenant}-[0-9]{4} (?:ERROR|WARN) 
va-route        ^/${prefix:-api}/v[0-9]+/${res}${fmt+\.json}(?:\?|$)
va-term         (?i)\b${term:?}\b
va-term-bang    (?i)\b${!term:?}\b
```

`va-tenant` ends with a space. Everything outside `${...}` is ordinary pattern
text, passed to the engine as written. `${!name}` means exactly `${name}`
(`va-term-bang` is `va-term` spelled the other way: it must give the same
answers). The templates are fixed; you do not need to parse arbitrary templates
unless your design finds that shorter.

## 3. The variable rule

`${name}` is replaced by a value, as follows (`w` is the "word" after the
operator; inside a word a backslash makes the next byte literal, so `\.` is a
literal `.`):

| form | replaced by | refuses the call when |
|---|---|---|
| `${name}` | the value | `name` is UNSET |
| `${name:-w}` | `w` when UNSET **or EMPTY**, else the value | never |
| `${name+w}` | `w` when SET (EMPTY counts as set), else nothing | never |
| `${name:?}` | the value | `name` is UNSET **or EMPTY** |

(The full rule set has two more operators, `-` and `:+`, that no member uses;
you may ignore them.) A **refused** call answers `r` without calling the engine.
A call is refused if ANY variable in the template refuses.

**A value is matched as itself, always.** Whatever bytes it holds, it is never
interpreted as pattern syntax: a value `a.c` matches only the three bytes
`a.c`, a value `x|y` only `x|y`, a value `(foo)` only `(foo)`, a value
containing `0x00` matches that byte. The same holds for a **word**: the text
`api` in `${prefix:-api}` and the text `.json` in `${fmt+\.json}` are literal
text, matched as themselves. After the substitution the rest of the template
keeps its pattern meaning (in `va-term`, `(?i)` still makes the whole
alternative case-insensitive, ASCII only, and `\b` is still a word boundary).

Note what makes this a performance question and not only a correctness one:
the resolved pattern depends on the call's values, so a stream of calls with
many different values needs many different compiled patterns.

## 4. What the timing measures (you do not time anything)

The driver shim loads the line list and each call's binding, calls YOUR
function once per call, and records your answer. The clock covers, per call:
resolving and escaping the template, looking up a compiled pattern, **compiling
it on a miss** (including any step your engine needs before it can match:
JIT compilation, scratch/work-area allocation, whatever), and the match. Those
are inside the clock whatever you do. Required design:

- keep compiled patterns in a cache; the cache is EMPTY at the start of every
  replay of the call list and unbounded within it (no eviction);
- choose the cache key yourself and say what it is in one line in the ledger
  (the resolved pattern text is the obvious one; the binding is another);
  the same calls must give the same answers whatever you choose;
- freeing compiled patterns between replays is the shim's job, outside the
  clock; you provide nothing for it beyond keeping them reachable from one
  container the shim can walk.

A stream of 4,096 to 16,384 calls over 4 to 4,096 distinct values is the shape
of the held-out data, with a share of calls refused by the rule above. The
report will say that a vars stream ranks largely by miss-compile cost and that
a time measures THIS assist (its key, its container, its escaping), not the
engine in the abstract.

## 5. Per-language notes (facts, not designs)

- A value or word must be escaped for YOUR engine's syntax so it matches as
  itself, **every byte included**. Use your engine's own quoting helper where
  it has one; otherwise a hex escape per non-alphanumeric byte is always safe.
- If your engine's compile call takes a NUL-terminated pattern string (a
  length-less API), a `0x00` in a value cannot be passed as itself: spell it as
  an escape sequence in the pattern text.
- A Unicode-by-default engine configuration changes what `\b`, `(?i)` and an
  escaped high byte mean. Configure for byte mode and ASCII case folding, and
  say so in the ledger's keying/container line.
- Case folding is ASCII only in this set (`A-Z` / `a-z`); a value byte `>= 0x80`
  matches only itself.

## 6. Your public sample

`vars-samples.tsv` (80 cases, 20 per member; `va-term` and `va-term-bang` share
their 20 cases): `case, member, bindings, line_hex, line, expected`. `bindings`
is `name=value` joined by `;`, value = lowercase hex of the bytes, or `UNSET`,
or `EMPTY`; a name not listed is UNSET. `line_hex` is the exact bytes; `line` is
a Python bytes literal for reading. `expected` is the token. Your assist must
reproduce all of its member's rows. The held-out corpus is different (more
calls, other lines, other values) and is not shown.

Six rows, as a reading aid (from `va-tenant`, `va-route`, `va-term`):

| member | bindings | line | answer |
|---|---|---|---|
| va-tenant | `tenant=acme` | `acme-0042 ERROR disk full` | `m:0,16` |
| va-tenant | `tenant=a.c` | `abc-1234 WARN dot is not a wildcard` | `n` |
| va-tenant | `tenant=UNSET` | `-0001 ERROR unset does not widen to empty` | `r` |
| va-route | `prefix=EMPTY; res=users; fmt=UNSET` | `/api/v1/users?page=2` | `m:0,14` |
| va-route | `prefix=UNSET; res=users; fmt=EMPTY` | `/api/v1/users` | `n` |
| va-term | `term=c++` | `uses c++x daily` | `m:5,8` |
| va-term | `term=c++` | `uses c++ daily` | `n` |

(The last two rows are the `\b` rule at work: after a `+` a word boundary needs
a word byte next, so the first matches only because of the `x`.)

## 7. Deliverable

One source file in your engine's binding language: the assist function, plus the
declared boilerplate regions fenced as `assists/RULES.md` says (includes, main,
io, the driver-protocol shim, wrappers). No other file. The counter, not you,
produces the token count; over 300 is a NOT-CAPABLE verdict with the count
recorded, which is a valid, honest result: do not golf to avoid it.
