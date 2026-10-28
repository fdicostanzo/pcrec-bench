# b148a-co-rust report: callouts x rust-regex

| member | tokens | lines | verdict | selftest |
|---|---|---|---|---|
| co-luhn | 166 | 12 | ASSISTED | 16/16 |
| co-isbn | 166 | 12 | ASSISTED | 16/16 |
| co-member | 166 | 12 | ASSISTED | 16/16 |

Design (all three, one file each, differing only in the pattern):
- Setup compiles `(?-u)` byte-mode regex with group 1 = the candidate (`\b(\d{13,19})\b`, `\b(97[89]\d{10})\b`, `\buser=(\w+)`).
- `find` loops `captures_at(s, at)` (whole haystack visible, so `\b` sees byte at-1); the shared `pred(s, g1)` judges.
- Fail: resume at candidate start + 1; pass: fill spans, return UB_M.

Unclear: none. `\w+` used for `\w++` (equivalent here: nothing follows group 1). The fire-count columns are not checked by selftest.
