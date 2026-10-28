# U15 repro

What it shows: doc/API says `onig_get_subexp_call_max_nest_level()` defaults to 24; the library returns 20.

Engine + version: Oniguruma 6.9.10 (Ubuntu libonig5); upstream master still has both (doc/API:1020 "default: 24", src/regint.h:115 `DEFAULT_SUBEXP_CALL_MAX_NEST_LEVEL 20`), read 2026-10-27.

Build/run: `run.sh` compiles `repro.c` against the system libonig and prints the version and the value.

Expected PRESENT output: `U15 PRESENT onig 6.9.10 default=20,doc=24`

What ABSENT (fixed) looks like: the library returns 24 (or the doc is changed to 20 and this repro is retired).
