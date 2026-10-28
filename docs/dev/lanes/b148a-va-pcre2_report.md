# b148a-va-pcre2 -- L6 vars assist, libpcre2 (C)

All four members: selftest 20/20, verdict NOT-CAPABLE (budget 300).

| member | tokens | lines | verdict | selftest |
|---|---|---|---|---|
| va-tenant | 354 | 38 | NOT-CAPABLE | 20/20 |
| va-route | 461 | 42 | NOT-CAPABLE | 20/20 |
| va-term | 362 | 38 | NOT-CAPABLE | 20/20 |
| va-term-bang | 362 | 38 | NOT-CAPABLE | 20/20 |

Design (same for all): build the resolved pattern text per call, every value/word byte
spelled `\xHH` (libpcre2 has no quoting helper; `\Q..\E` breaks on a value holding `\E`);
key the template's `ub_map` cache on the resolved text; `pcre2_compile` with an explicit
length (NUL-safe), flags 0 (byte mode, no UTF/UCP), interpreter (no JIT), then
`pcre2_match_data_create_from_pattern` + `pcre2_match`. Refusal (`UB_R`) is decided before
the engine is touched. va-term-bang is byte-identical to va-term (`${!x}` == `${x}`).

The cost is the escaper + pattern assembly + compile-on-miss wrapper (~230 tokens shared);
va-route adds the `:-` / `+` word logic. No golfing attempted. A shorter C escape would
need `<stdio.h>` (includes fence is fixed), so hex digits are written by hand.

Unclear / notes: while reading assists.tsv's tail to find the newline I saw the first
cells of one other row (`co-netstr netstr re2 C++ 185`); no use made of it.
