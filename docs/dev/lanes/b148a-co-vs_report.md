# b148a-co-vs report: callouts x Vectorscan (blinded author)

All three members: 242 tokens, 17 lines, ASSISTED, selftest 16/16 each (tokcount-1). Reviewer verdict pending.

Design (same for all three, differing only in the pattern and the group-1 offset):
- Setup compiles one pattern (`\b\d{13,19}\b`, `\b97[89]\d{10}\b`, `\buser=\w+\b`) with HS_FLAG_SOM_LEFTMOST, block mode; `\w+\b` replaces the possessive `\w++` (maximal run, so one end per start).
- find() scans from `start-1` (one byte of context so `\b` sees the real previous byte); the match callback drops matches starting before `start`, calls the shared `pred` on group 1 and terminates the scan on the first pass (HS_SCAN_TERMINATED -> UB_M).
- Group 1 = group 0 for luhn/isbn; start+5 for member. Failed candidates are simply skipped (all starts are reported independently), so restart-at-start+1 is implicit.

Unclear / caveats: the selftest checks fire counts only indirectly; I did not verify fires_* myself. Cost is one hs_scan per call from start-1 (no whole-subject rescan). Hyperscan reports matches by end offset; order equals start order for these three patterns (maximal word runs).
