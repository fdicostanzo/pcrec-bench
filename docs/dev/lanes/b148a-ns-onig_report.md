# b148a-ns-onig report: co-netstr x Oniguruma 6.9.10

- Tokens 252 (counter tokcount-1), 22 lines, budget 300 -> ASSISTED.
- Selftest: 27/27 public cases pass. Fire counts were not shown by the selftest, so not compared with netstr.md section 3.
- Design: pattern `(\d{1,9}):(?>(?m:.)*?(?{4})),` (ASCII encoding, `(?m:.)` is Oniguruma's dot-all) compiled once in setup.
  A global progress callout reads group 1 with onig_get_capture_range_in_callout and the current position with onig_get_current_by_callout_args.
  It returns ONIG_CALLOUT_SUCCESS (0) when the run length equals the number, else ONIG_CALLOUT_FAIL (1, backtrack into the lazy run).
  ub_find is one onig_search from `start` over the whole subject; a negative code other than ONIG_MISMATCH is returned as the give-up.
- Unclear: nothing. Oniguruma docs were consulted only via /usr/include/oniguruma.h.
