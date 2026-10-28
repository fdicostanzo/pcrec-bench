# b148a-ns-rust: co-netstr x rust-regex

- Tokens 201 (tokcount-1), 13 lines, budget 300 -> ASSISTED. Selftest 27/27.
- Design (Shape B): `([0-9]{1,9}):` compiled in setup; `captures_at(s, at)` finds the leftmost candidate with the whole subject visible; host reads LEN from group 1, checks `s[colon+1+LEN] == ','`; else resumes at candidate start + 1.
- `[0-9]` instead of `\d` because `\d` is Unicode-aware in regex::bytes by default.
- Unclear: nothing. (My `tail` of assists.tsv after appending displayed the re2 row; not used.)
