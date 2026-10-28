#!/bin/bash
# U15 repro -- doc/API states the default subexp-call max nest level is 24;
# onig_get_subexp_call_max_nest_level() returns 20 (src/regint.h
# DEFAULT_SUBEXP_CALL_MAX_NEST_LEVEL). PRESENT = the library reports 20.
set -u
D=${UPSTREAM_SCRATCH:-/var/tmp/pcrecbench/upstream}/U15; mkdir -p "$D"
H=$(dirname "$0")
if ! cc -o "$D/repro" "$H/repro.c" ${ONIG_CFLAGS:-} -lonig ${ONIG_LDFLAGS:-} 2>"$D/cc.err"; then
  echo "U15 CANNOT-RUN onig ? $(head -1 "$D/cc.err")"; exit 2; fi
read -r ver lvl < <("$D/repro")
if [ "$lvl" != 24 ]; then echo "U15 PRESENT onig $ver default=$lvl,doc=24"; exit 0; fi
echo "U15 ABSENT onig $ver default=$lvl,doc=24"; exit 1
