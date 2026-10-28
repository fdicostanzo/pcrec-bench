# b148a-va-vs report (vars x Vectorscan)

All four members: selftest 20/20, verdict NOT-CAPABLE (over 300; not golfed).

| member | tokens | lines |
|---|---|---|
| va-tenant | 311 | 27 |
| va-route | 371 | 29 |
| va-term | 316 | 27 |
| va-term-bang | 316 | 27 |

Design: hex-escape (`\xHH`) every value byte (Vectorscan has no quoting helper, and
hs_compile takes a NUL-terminated string); sprintf the resolved pattern into a VLA;
cache hs_database_t* in the template's ub_map keyed by the resolved pattern text;
compile with HS_FLAG_SOM_LEFTMOST, block mode, grow one global scratch on each miss;
the callback stops at the first match (all four templates are fixed-length per start,
so first reported = leftmost).

Unclear: none. Note the `includes` fence rejects `#define _GNU_SOURCE`, so no asprintf;
VLAs sized from the value length stand in. term-bang is byte-identical to term.
