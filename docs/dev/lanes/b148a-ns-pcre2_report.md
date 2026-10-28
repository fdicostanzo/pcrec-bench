# b148a-ns-pcre2: co-netstr x libpcre2 (Shape A)

- Tokens 232 / budget 300, 21 lines, verdict ASSISTED. Selftest 27/27.
- Fire counts: the selftest prints none; not compared.
- Design: pattern `(\d{1,9}):(?>(?s:.)*?(?C4)),` compiled in setup; one pcre2_match per find with a match context carrying the callout. The callout parses group 1 from the offset vector and returns 1 (reject this position, keep backtracking into the lazy run) unless `current_position - (g1end+1) == LEN`; 0 passes. -1 would abort the match, so it is not used.
- Unclear: nothing. Callee is mine (not read from callees/).
