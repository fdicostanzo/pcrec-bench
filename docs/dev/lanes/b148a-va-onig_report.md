# b148a-va-onig: vars assist x Oniguruma 6.9.10

| member | tokens | lines | verdict | selftest |
|---|---|---|---|---|
| va-tenant | 306 | 29 | NOT-CAPABLE | 20/20 |
| va-route | 401 | 32 | NOT-CAPABLE | 20/20 |
| va-term | 311 | 29 | NOT-CAPABLE | 20/20 |
| va-term-bang | 311 | 29 | NOT-CAPABLE | 20/20 |

Design (all four): resolve the template per call in C, hex-escaping every
value/word byte (`\xHH`, so any byte incl. NUL matches as itself); cache
regex_t* in the template's ub_map keyed by the resolved pattern text;
onig_new with ONIG_ENCODING_ASCII + ONIG_SYNTAX_PERL_NG (byte mode, ASCII
case folding), onig_search with one setup-made OnigRegion.
va-term and va-term-bang are the same file. Needed `#include <stdio.h>`
outside the includes fence (sprintf; counted). Three members miss 300 by
6-11 tokens; no golfing done. Nothing unclear.
