# b148a-ns-vs report: co-netstr x Vectorscan (Shape B)

- Tokens 290 (budget 300), lines 24, verdict ASSISTED; selftest 27/27 pass.
- Design: block-mode `\d{1,9}:` with SOM_LEFTMOST, scanned from `subj+start`; the
  match callback fires once per colon with the leftmost digit start, and the host
  tries each start in the run (start..colon-1) for the `,` at colon+1+LEN, returning
  nonzero to terminate the scan on the first hit. No captures, so group 1 is derived.
- Unclear: nothing in the statement. Process note: I viewed the first 80 chars of the
  last two rows of assists.tsv (onig, re2) while checking the format; I did not use them.
