# b148a-co-re2 report: L6 callouts x RE2 (blinded author)

All three members: ASSISTED, 202 tokens, 15 lines, budget 300, selftest 16/16 each (assist-selftest rc=0).
Ledger rows appended to bench/unusual/assists/assists.tsv; `tools/tokcount.py ledger-check` OK.

| member | tokens | lines | verdict | selftest |
|---|---|---|---|---|
| co-luhn | 202 | 15 | ASSISTED | 16/16 |
| co-isbn | 202 | 15 | ASSISTED | 16/16 |
| co-member | 202 | 15 | ASSISTED | 16/16 |

Design (identical in all three; only the pattern string differs, one file per member):
- setup compiles the candidate pattern once, RE2::Options Latin1 (byte mode; `\d`/`\w`/`\b` are ASCII in RE2). `\w++` is spelled `\w+` (RE2 has no possessive; the greedy run is the same match since nothing follows it).
- find loops RE2::Match(s, start, s.size(), UNANCHORED, g, 2) on the WHOLE subject, so `\b` sees the byte before `start`.
- Each candidate goes to the shared pred(); a pass fills the spans, a fail resumes at candidate start + 1.

Unclear/none: the statement lacked nothing. Every Match false is read as no match (RE2 give-ups are not surfaced; none seen on the sample).
