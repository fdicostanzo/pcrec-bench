#!/bin/bash
# scripts/run_suite.sh -- ONE quiet-window run of SEVERAL sub-benches in a
# stated PRIORITY order, each through scripts/run_window.sh unchanged
# ([B26], 2026-09-01: Frank's "run the full suite tonight" -- the first
# window longer than one set; the order is what a morning cut-off loses
# the least of, so the cls-* AFTER runs first and the clang cells last).
#
# MUST BE LAUNCHED UNDER `setsid` for the same reason run_window.sh must:
#
#     setsid scripts/run_suite.sh > /dev/null 2>&1 &
#
# ENV-OVERRIDABLE (defaults shown):
#
#   SUITE      "bounded loglines email"   -- sub-benches, in RUN ORDER
#   TESTEES    run_window.sh's default    -- the testee list for EVERY set,
#              unless TESTEES_<set> (e.g. TESTEES_bounded) overrides it for
#              one set (a second pass of the same set with other testees is
#              spelled as a second entry in SUITE with a suffix after a
#              colon: `bounded:clang` runs SUBBENCH=bounded with
#              $TESTEES_bounded_clang -- the suffix is a LABEL, nothing else)
#   STORE, PIN, TRIALS, NOTE, EXTRA -- passed through to run_window.sh
#   SUITE_LOG  build/windows/suite_$(date +%Y%m%dT%H%M%SZ).log
#   --dry-run  passed through (every set rehearsed synthetic into a scratch
#              store; refused if STORE is the canonical store/)
#
# Each set's own log is run_window.sh's (build/windows/window_<set>_*.log,
# named in this log). The suite log ends with SUITE_RUN_COMPLETE and a
# per-set line `set <name> rc=<rc> <minutes> min`; a set whose window
# script exits non-zero does NOT stop the suite (the next set still
# runs -- one broken set must not lose the night), and the rc is in the
# summary for the morning read.
set -u
export LC_ALL=C
REPO=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd) || exit 9
cd "$REPO" || exit 9

SUITE=${SUITE:-"bounded loglines email"}
DRY=""
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY="--dry-run" ;;
    *) echo "run_suite.sh: unrecognized argument: $arg" >&2; exit 2 ;;
  esac
done
SUITE_LOG=${SUITE_LOG:-build/windows/suite_$(date -u +%Y%m%dT%H%M%SZ).log}
mkdir -p "$(dirname "$SUITE_LOG")" || exit 9

echo "== suite start $(date -Is) suite='$SUITE' dry_run='${DRY:-no}' load=$(cat /proc/loadavg)" | tee -a "$SUITE_LOG"
summary=""
for entry in $SUITE; do
  set_name=${entry%%:*}
  label=""
  [ "$entry" != "$set_name" ] && label=${entry#*:}
  var="TESTEES_${set_name}${label:+_$label}"
  testees="${!var:-${TESTEES:-}}"
  log="build/windows/window_${set_name}${label:+_$label}_$(date -u +%Y%m%dT%H%M%SZ).log"
  echo "-- set $entry start $(date -Is) testees='${testees:-<default>}' log=$log" | tee -a "$SUITE_LOG"
  t0=$(date +%s)
  if [ -n "$testees" ]; then
    SUBBENCH="$set_name" TESTEES="$testees" LOG="$log" scripts/run_window.sh $DRY
  else
    SUBBENCH="$set_name" LOG="$log" scripts/run_window.sh $DRY
  fi
  rc=$?
  mins=$(( ($(date +%s) - t0) / 60 ))
  line="set $entry rc=$rc $mins min"
  echo "-- $line $(date -Is)" | tee -a "$SUITE_LOG"
  summary="$summary$line"$'\n'
done
echo "== suite end $(date -Is) load=$(cat /proc/loadavg)" | tee -a "$SUITE_LOG"
printf '%s' "$summary" | tee -a "$SUITE_LOG"
echo "SUITE_RUN_COMPLETE" >> "$SUITE_LOG"
