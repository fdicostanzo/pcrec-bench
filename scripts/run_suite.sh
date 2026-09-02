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
#   CELL_CAP   run_window.sh's default (5400 s) -- the per-cell wall-clock
#              cap, overridable PER SET as CELL_CAP_<set> and per labelled
#              pass as CELL_CAP_<set>_<label>, resolved exactly the way
#              TESTEES is. A set whose longest cell is near the default
#              needs its own: bench/altwide@0.2's bigcap pass wants
#              CELL_CAP_altwide_bigcap of ~10800 (the [B31] census puts
#              `pcrec-vm-bigcap` at ~4,500 s of gcc alone at five trials,
#              before match and throughput). scripts/CLAUDE.md carries the
#              measured cell-length table.
#   STORE, PIN, TRIALS, NOTE, EXTRA -- passed through to run_window.sh
#   SUITE_LOG  build/windows/suite_$(date +%Y%m%dT%H%M%SZ).log
#   --dry-run  passed through (every set rehearsed synthetic into a scratch
#              store; refused if STORE is the canonical store/)
#
# Each set's own log is run_window.sh's (build/windows/window_<set>_*.log,
# named in this log). The suite log ends with SUITE_RUN_COMPLETE and a
# per-set line `set <name> rc=<rc> <minutes> min`; a cell killed by its
# per-cell cap says so BY NAME in that set's own window log (rc=124), which
# the suite summary cannot show; a set whose window
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
  # The same resolution for the per-cell cap: CELL_CAP_<set>_<label>, then
  # CELL_CAP_<set>, then whatever the caller set globally, then nothing at
  # all -- in which case run_window.sh applies its own 5400 s default and
  # this script names no number of its own.
  capvar="CELL_CAP_${set_name}${label:+_$label}"
  cellcap="${!capvar:-${CELL_CAP:-}}"
  log="build/windows/window_${set_name}${label:+_$label}_$(date -u +%Y%m%dT%H%M%SZ).log"
  echo "-- set $entry start $(date -Is) testees='${testees:-<default>}' cell_cap='${cellcap:-<default>}' log=$log" | tee -a "$SUITE_LOG"
  t0=$(date +%s)
  # A SUBSHELL and not an assignment prefix: bash decides what is an
  # assignment prefix while PARSING, so a `${cellcap:+CELL_CAP=...}` would
  # be taken as the command word rather than as a variable, and the cap
  # would silently never arrive. Exporting inside a subshell passes only
  # what is actually set and leaves this script's own environment alone,
  # so a set that names no cap gets run_window.sh's own default and this
  # script never writes a number of its own.
  (
    export SUBBENCH="$set_name" LOG="$log"
    [ -n "$testees" ] && export TESTEES="$testees"
    [ -n "$cellcap" ] && export CELL_CAP="$cellcap"
    scripts/run_window.sh $DRY
  )
  rc=$?
  mins=$(( ($(date +%s) - t0) / 60 ))
  line="set $entry rc=$rc $mins min"
  echo "-- $line $(date -Is)" | tee -a "$SUITE_LOG"
  summary="$summary$line"$'\n'
done
echo "== suite end $(date -Is) load=$(cat /proc/loadavg)" | tee -a "$SUITE_LOG"
printf '%s' "$summary" | tee -a "$SUITE_LOG"
echo "SUITE_RUN_COMPLETE" >> "$SUITE_LOG"
