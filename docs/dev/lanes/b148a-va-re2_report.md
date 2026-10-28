# b148a-va-re2 report (vars x RE2)

All four members ASSISTED, selftest 20/20 each (RE2, Latin-1 byte mode, resolved-pattern-text cache key).

| member | tokens | lines | verdict |
|---|---|---|---|
| va-tenant | 191 | 18 | ASSISTED |
| va-route | 245 | 20 | ASSISTED |
| va-term | 251 | 21 | ASSISTED |
| va-term-bang | 251 | 21 | ASSISTED (same body as va-term) |

Design: resolve the template in C++ (UNSET/EMPTY rules), escape values with RE2::QuoteMeta, cache RE2 by resolved text, `Match(UNANCHORED)`.
va-term/-bang: RE2 Latin-1 `(?i)` would fold 0xC9/0xE9 (sample "CAF\xc3\x89" must not match), so `(?i)` is dropped and each ASCII letter is spelled `[xX]`.
Unclear: nothing; the Latin-1 fold finding was learned from the public sample.
