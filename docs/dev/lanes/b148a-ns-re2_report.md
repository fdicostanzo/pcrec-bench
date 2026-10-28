# b148a-ns-re2 report

Member co-netstr, engine RE2 (Shape B, host jump).

- Tokens 185 (tokcount-1), 13 lines, budget 300: ASSISTED.
- Selftest: 27/27 public cases pass.
- Design: one static `RE2 head(R"((\d{1,9}):)")`; `Match(s, start, size, UNANCHORED, g, 2)` finds the
  leftmost candidate; host reads LEN from group 1, checks `s[colon+1+LEN] == ','`; on failure resumes at
  candidate start + 1.
- Ledger row appended to assists/assists.tsv (reviewer_verdict pending).
- Unclear: nothing. (A tail of assists.tsv displayed other engines' rows while I looked for the format; I did not use them.)
