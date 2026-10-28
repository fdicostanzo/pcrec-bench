# vendor/pcrec -- provenance

Two files copied BYTE FOR BYTE (no header inserted, so the hashes below are the
source files' own) from the pcrec repository, read-only, at main commit
614d45eb3eca3dc5d055a5e3e1ab16c28191b026 (the [B147] pin; both files unchanged since
66f9a8560 "tests/recursion: cscan.rxt, the C (?{ }) scanner as one pcrec pattern
(SCANNER-DOGFOOD, lane scandog)", 2026-10-27):

| file | pcrec path | sha256 |
|---|---|---|
| cscan.rxt | tests/recursion/cscan.rxt | e8c5d40e056fad7ee4aeae3121f01230590241bf8a7b85f0a1745fdd8d2964e7 |
| gen_cscan.py | tests/recursion/gen_cscan.py | 7fdc1110066797314d4652bd0d4a54115b6016a1cd020efad2982e50ead9711a |

Licence: MIT, pcrec LICENSE, "Copyright (c) 2026 Frank DiCostanzo" (the same author
as this repository; recorded as a licence for the provenance table's sake).

Use here: cscan.rxt's `pattern-esc` string is the pattern text of the `cscan` member
(members.py decodes it and checks it against gen_cscan.py's PATTERN); gen_cscan.py's
`C` table (73 start-0 cases, each with a HAND-WRITTEN rule expectation) is imported as
the first 73 short subjects and as the reference scanner's acceptance table. Neither
file is executed for its side effects (gen_cscan.py's main() is guarded; its
load_pcre2() reaches into pcrec's tree and is never called here). Do not edit these
files; a pcrec change is a re-vendor with new hashes.
