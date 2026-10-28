# Writing an assist

You are writing ONE assist: host code that gives your engine one member's
feature, inside 300 counted tokens. Read your family's problem statement
(`problems/<family>.md`) and `RULES.md` first. Nothing else is yours to read:
not another engine's assist, not the held-out subjects or expectations.

## Steps

1. **Start from the template.**

       python3 -m pcrecbench assist-init --member <member> --engine <engine>

   This writes `assists/<member>/<engine>/assist.<ext>`, holding only your
   member's family. It counts a handful of tokens before you write anything.

2. **Fill in the parts marked `ASSIST`, and your setup.** That means the one
   answer function, any state it needs, and the setup function that builds
   that state. Leave every `/* BOILERPLATE ... */` region exactly as it is:
   the self-test compares each region with the template and reports drift.
   Fixed patterns are compiled in setup, which runs outside the clock. Nothing
   that runs per call is free.

3. **Self-test.**

       python3 -m pcrecbench assist-selftest --member <member> --engine <engine>

   This builds your file and runs it over your family's PUBLIC sample
   (`problems/<family>-samples.tsv`) only. It prints PASS or FAIL per case and
   then the count. It exits 0 only when every case passes, nothing is
   smuggled, and no fence drifted.

4. **Be brief, and write it the way your engine's users would.** A reviewer
   rejects golfed code (`golfed`) and unidiomatic code (`not-idiomatic`). If
   the count goes over 300, the verdict is NOT-CAPABLE and the count is
   recorded. That is a result, not a failure to hide.

## The contract

The template declares the signatures; do not change them.

- **recursion / callouts / netstr.** `find(subject, start)` returns the first
  match at or after `start`. The whole subject stays visible, including the
  bytes before `start`. Fill in the span's start and end, and group 1 where
  your member reports one. Return `UB_M` on a match and `UB_N` on no match.
  Return a NEGATIVE code (the engine's own) when the engine gave up.
  For callouts, `pred(subject, b, c)` is the member's shared predicate on
  group 1 = `[b, c)`. Call it; do not reimplement it.
- **vars.** `vars(line, binding)` matches one line on its own, with offsets
  relative to that line. The binding gives each variable's value, or tells
  you it is UNSET. An EMPTY value is not UNSET. Return `UB_R` when the
  variables rule refuses the call. Keep compiled patterns in the template's
  cache, which is emptied between replays outside the clock.
- The runner owns `main`, the protocol, the clock and the answer tokens.
  You never print anything.

## What counts

`tools/tokcount.py` counts lexical tokens. Comments, blank lines and the
fenced regions are not counted. Content inside a fence that breaks the
fence's shape rule is counted in full and flagged as smuggled.
