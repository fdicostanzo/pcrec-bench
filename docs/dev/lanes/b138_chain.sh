#!/bin/bash
# [B138] RE-BASELINE WINDOW CHAIN (lane b138chain, 2026-10-18, NOT RUN): the
# CORE roster of docs/dev/lanes/b138hours_report.md at the ONE canonical pcrec
# pin 6b2dbd3e (abi 76), on the NEW box (frank-desktop, Ryzen 7 7700X, 8c/16t).
# No `testee@pin` entries, no also_pins, configs.toml untouched. Launched by
# the MANAGER once Frank clears the window, detached, one tier per night:
#
#     MACHINE_ID=<slug> TIERS="1" setsid bash docs/dev/lanes/b138_chain.sh > /dev/null 2>&1 &
#
# ENV:
#   MACHINE_ID  REQUIRED (Frank names this box). Absent -> `CHAIN_ABORT` and
#               nothing measured. Precondition 1 registers the box in
#               store/machines.tsv (`pcrecbench machines register`, with the
#               hostname / canonical cpu_model slug / core count env.py itself
#               derives, so every later `run` resolves it). Idempotent: the
#               same box under the same id is a no-op; the box under another
#               id, or the id on another box, ABORTS. The new machines.tsv
#               row is left UNCOMMITTED for the manager.
#   TIERS       "1 2" (default). Each tier is launchable alone and carries its
#               own opening and closing sentinel pass.
#   STOP_AT_T1 / STOP_AT_T2   a `date -d` time; no SET of that tier starts at
#               or after it, no CELL starts after it (a running cell finishes).
#               The CLOSING sentinel pass is a SEPARATE run_suite call and so
#               is never skipped by STOP_AT.
#   PIN         the CPU core `pcrecbench run --pin` uses; default 7 here (the
#               run_window.sh default of 11 is the old box's). CPU 7 is
#               physical core 7 of cores 0-7; its SMT sibling is CPU 15
#               (cores 0-7 and their siblings 8-15; /sys/devices/system/cpu/
#               cpu7/topology/thread_siblings_list = 7,15). Env-overridable.
#   DRYRUN=1    the rehearsal: every suite call gets --dry-run (synthetic,
#               --force-unquiet, scratch tier, TRIALS=1), STORE is
#               $DRYSTORE (default /var/tmp/pcrecbench/b138chain/store), ONE
#               cell per set, no quiet sample, MACHINE_ID defaults to
#               `rehearsal-box`, the real store/ is never named. Logs go to
#               /var/tmp/pcrecbench/b138win-dry/. Refused if DRYSTORE is `store`.
#
# LOGS: /var/tmp/pcrecbench/b138win/chain.log carries CHAIN_START, a
# `TIERn_DONE suite_rc=<rc>` per tier, CHAIN_DONE (CHAIN_ABORT <why> on a
# failed precondition). Each suite call's own log is build/windows/suite_*.log
# (named here as SUITE_LOG=$W/suite_tN*.log) and ends SUITE_RUN_COMPLETE with a
# `set <name> rc=<rc> <min> min` line per set; each set's window log
# (build/windows/window_<set>_*.log) ends `WINDOW_RUN_COMPLETE cells=N/N`.
# rc=4 (inconclusive-spread) cells are re-measured once by run_window.sh.
#
# TIERS (sets at their current version; roster per set below; CORE = pcrec
# auto/nocaps/vm, pcre2 jit/interp, ONE config per other engine the set has):
#   1  sentinel, email, loglines, altwide, bounded, litrun, sentinel:end1
#      35 cells (6+6+6+6+5 set cells + 3+3 sentinel)
#   2  sentinel, capability, syntax, utf8, sentinel:end2
#      31 cells (10+6+9 set cells + 3+3 sentinel)
#
# WALL-TIME ESTIMATE. Zen-1 (Ryzen 5 1600) minutes from the b138hours report
# (cell minutes + 0.5/cell + 2.5/set), DIVIDED BY AN ASSUMED 2.0 -- the
# assumption is a guess at 7700X-over-Zen-1 single-core speed; the window
# measures the real factor (below). Zen-1: tier 1 = sentinel 25 x2 + email 48 +
# loglines 57 + altwide 203 (158 measured + ~45 imputed for pcre2-interp, which
# has no altwide@0.3 cell) + bounded 262 + litrun 70 = 690 min -> ~345 min
# (~5.8 h) at 2.0. Tier 2 = sentinel 25 x2 + capability 443 + syntax 247 +
# utf8 330 = 1070 min -> ~535 min (~8.9 h) at 2.0. Both together ~14.7 h.
#
# THE MEASURED FACTOR. The opening sentinel pass of tier 1 yields it: this
# chain parses the sentinel window log right after that pass and logs
#   SENTINEL_FACTOR zen1_min=21.3 tonight_min=<m> factor=<zen1/tonight> ...
# (Zen-1 reference: pcrec-auto 6.1, pcrec-nocaps 6.1, pcre2-jit 9.1 min, the
# 2026-10-13 sentinel cells, report b138hours). The manager's cross-check from
# the RECORDS: a cell's span = environment.load.after.sampled_at minus
# environment.load.before.sampled_at (the report's method; the same for the
# Zen-1 records in store/ and tonight's). Rescale the not-yet-run estimate:
# remaining_Zen-1_minutes / factor. The closing pass of each tier gives a
# second reading (drift across the tier).
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 9
export LC_ALL=C

DRYRUN=${DRYRUN:-0}
if [ "$DRYRUN" = 1 ]; then
  W=/var/tmp/pcrecbench/b138win-dry
  STORE=${DRYSTORE:-/var/tmp/pcrecbench/b138chain/store}
  [ "$STORE" = store ] && { echo "b138_chain.sh: DRYRUN refuses STORE=store" >&2; exit 9; }
  MACHINE_ID=${MACHINE_ID:-rehearsal-box}
  DRYFLAG=--dry-run
else
  W=/var/tmp/pcrecbench/b138win
  STORE=store
  DRYFLAG=
fi
mkdir -p "$W"
L=$W/chain.log
export PIN=${PIN:-7}
TIERS=${TIERS:-1 2}
echo "CHAIN_START $(date -Is) TIERS=$TIERS PIN=$PIN DRYRUN=$DRYRUN STORE=$STORE MACHINE_ID=${MACHINE_ID:-<unset>}" >> "$L"
abort() { echo "CHAIN_ABORT $*" >> "$L"; exit 9; }

[ -n "${MACHINE_ID:-}" ] || abort "MACHINE_ID is not set (Frank names this box); nothing measured"

# ---- the rosters (final, resolved against `pcrecbench testees` below) ----
PC="pcrec-auto pcrec-nocaps pcrec-vm"
PJ="pcre2-jit pcre2-interp"
R_SENTINEL="pcrec-auto pcrec-nocaps pcre2-jit"              # run_suite.sh's default
R_EMAIL="$PC $PJ rust-default"
R_LOGLINES="$PC $PJ rust-default"
R_ALTWIDE="$PC $PJ rust-default"
R_BOUNDED="$PC $PJ rust-default"
R_LITRUN="$PC $PJ"
R_CAPABILITY="$PC $PJ onig-default vectorscan-block-nosom tre-default re2-default rust-default"
R_SYNTAX="$PC $PJ rust-default"
R_UTF8="pcrec-auto-utf8 pcrec-nocaps-utf8 pcrec-vm-utf8 pcre2-utf-jit pcre2-utf-interp onig-utf8 re2-utf8 vectorscan-block-nosom-utf8 rust-default"

# ---- preconditions (a failure aborts: nothing has been measured) ----
python3 -m pcrecbench testees 2>>"$L" | awk '{print $1}' > "$W/testees.names"
for s in SENTINEL EMAIL LOGLINES ALTWIDE BOUNDED LITRUN CAPABILITY SYNTAX UTF8; do
  v=R_$s
  for t in ${!v}; do
    grep -qx -- "$t" "$W/testees.names" || abort "roster $s: testee '$t' does not resolve (pcrecbench testees)"
  done
done
echo "roster names resolve" >> "$L"

# 1. register the box (idempotent; a different id for this box, or this id on
# another box, aborts)
if [ "$DRYRUN" = 1 ]; then mkdir -p "$STORE"; fi
read -r HOSTN CPUSLUG NCORES < <(python3 -c "
import platform
from pcrecbench import env
print(platform.node() or 'unknown', env.canon_cpu_model(env.cpu_model_raw()), env.cores())")
python3 -m pcrecbench machines register --store "$STORE" --machine-id "$MACHINE_ID" \
    --hostname "$HOSTN" --cpu-model "$CPUSLUG" --cores "$NCORES" \
    --first-seen "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --note "[B138] registered by b138_chain.sh" >> "$L" 2>&1 \
  || abort "machines register ($MACHINE_ID $HOSTN $CPUSLUG $NCORES) refused"

# 2. the pcrec pin
sh testees/pcrec/pin.sh --path 6b2dbd3e >> "$L" 2>&1 || abort "no build of 6b2dbd3e (run: sh testees/pcrec/pin.sh 6b2dbd3e)"

# 3. subject trees (generated, gitignored; deterministic; not timing)
for d in sentinel email loglines altwide bounded litrun capability syntax utf8; do
  for g in gen_subjects.py gen_throughput_subjects.py; do
    [ -f bench/$d/$g ] || continue
    gnutimeout 900 python3 bench/$d/$g >> "$L" 2>&1 || abort "bench/$d/$g failed"
  done
  [ -d bench/$d/subjects ] || abort "bench/$d/subjects missing after generation"
done
echo "subjects generated" >> "$L"

# 4. the quiet sample (skipped in the rehearsal)
if [ "$DRYRUN" != 1 ]; then
  python3 -m pcrecbench quiet --samples 5 --pin "$PIN" >> "$L" 2>&1; echo "quiet rc=$?" >> "$L"
fi

# 5. the driver hash: equal across workdirs, unchanged to the end of the chain
DRV="build/work/pcrec-auto/pcrec_driver build/work/pcrec-nocaps/pcrec_driver build/work/pcrec-vm/pcrec_driver"
drvsum() { for f in $DRV; do [ -f "$f" ] && sha256sum "$f"; done >> "$L" 2>&1; }
echo "driver sha256 (start; absent until the first cell builds it):" >> "$L"; drvsum

tier() { case " $TIERS " in *" $1 "*) return 0;; esac; return 1; }
# dry run: ONE cell per set (the first roster name)
first() { if [ "$DRYRUN" = 1 ]; then echo "${1%% *}"; else echo "$1"; fi; }

# parse the newest sentinel window log in a suite log -> SENTINEL_FACTOR
sentinel_factor() {  # $1 suite log
  python3 - "$1" >> "$L" 2>&1 <<'PY'
import re, sys, datetime as dt
suite = open(sys.argv[1]).read()
logs = re.findall(r"-- set sentinel\S* start .* log=(\S+)", suite)
if not logs:
    print("SENTINEL_FACTOR unavailable (no sentinel set in the suite log)"); sys.exit()
cells, cur = [], None
for ln in open(logs[0]):
    m = re.match(r"-- cell sentinel x (\S+) (\S+)", ln)
    if m: cur = (m.group(1), dt.datetime.fromisoformat(m.group(2))); continue
    m = re.match(r"\s+attempt \d+ rc=(\d+) \S+ (\S+)", ln)
    if m and cur and m.group(1) in ("0", "4"):
        cells.append((cur[0], (dt.datetime.fromisoformat(m.group(2)) - cur[1]).total_seconds() / 60)); cur = None
z = {"pcrec-auto": 6.1, "pcrec-nocaps": 6.1, "pcre2-jit": 9.1}
tot = sum(m for _, m in cells); ref = sum(z.get(t, 0) for t, _ in cells)
print("SENTINEL_FACTOR zen1_min=%.1f tonight_min=%.1f factor=%.2f cells=%s" % (
    ref, tot, ref / tot if tot else 0, ",".join("%s:%.1f" % c for c in cells)))
PY
}

run_tier() {  # $1 n  $2 set-list  $3 stop_at  then TESTEES_*/CELL_CAP_* in the env
  local n=$1 suite_main=$2 stop=$3
  SENTINEL=1 SUITE="$suite_main" STOP_AT="$stop" SUITE_LOG="$W/suite_t$n.log" \
    NOTE="[B138] re-baseline tier $n at 6b2dbd3e (CORE roster, $MACHINE_ID)" \
    STORE="$STORE" scripts/run_suite.sh $DRYFLAG >> "$L" 2>&1
  local rc=$?
  # the closing pass is its own call: STOP_AT can never skip it
  SENTINEL=0 SUITE="sentinel:end$n" STOP_AT="" SUITE_LOG="$W/suite_t${n}_end.log" \
    NOTE="[B138] re-baseline tier $n closing sentinel ($MACHINE_ID)" \
    STORE="$STORE" scripts/run_suite.sh $DRYFLAG >> "$L" 2>&1
  local rc2=$?
  echo "TIER${n}_DONE suite_rc=$rc closing_rc=$rc2 $(date -Is)" >> "$L"
  drvsum
}

# per-set CELL_CAP (seconds). Longest CORE cell at Zen-1 timings: capability
# pcre2-interp 71.9 min = 4,314 s, then 61.3 / 57.6 min; nothing CORE reaches
# 5,400 s (the 106.5 min capability pcre2-dfa cell is NOT in CORE). Caps sit
# >= ~1.25x above each set's longest Zen-1 cell; the new box should be faster.
export CELL_CAP_sentinel=3600 CELL_CAP_sentinel_end1=3600 CELL_CAP_sentinel_end2=3600
export CELL_CAP_email=3600 CELL_CAP_loglines=3600 CELL_CAP_litrun=3600
export CELL_CAP_altwide=5400 CELL_CAP_bounded=5400 CELL_CAP_syntax=5400 CELL_CAP_utf8=5400
export CELL_CAP_capability=7200

export TESTEES_sentinel="$(first "$R_SENTINEL")" TESTEES_sentinel_end1="$(first "$R_SENTINEL")" TESTEES_sentinel_end2="$(first "$R_SENTINEL")"
export TESTEES_email="$(first "$R_EMAIL")" TESTEES_loglines="$(first "$R_LOGLINES")"
export TESTEES_altwide="$(first "$R_ALTWIDE")" TESTEES_bounded="$(first "$R_BOUNDED")"
export TESTEES_litrun="$(first "$R_LITRUN")" TESTEES_capability="$(first "$R_CAPABILITY")"
export TESTEES_syntax="$(first "$R_SYNTAX")" TESTEES_utf8="$(first "$R_UTF8")"

# ---- TIER 1 (~345 min at the assumed 2.0): email, loglines, altwide, bounded, litrun
if tier 1; then
  # the opening sentinel is auto-prepended by run_suite.sh; read its factor
  # as soon as the whole call is done, and again from the closing pass.
  run_tier 1 "email loglines altwide bounded litrun" "${STOP_AT_T1:-}"
  sentinel_factor "$W/suite_t1.log"
  sentinel_factor "$W/suite_t1_end.log"
fi
# ---- TIER 2 (~535 min at the assumed 2.0): capability, syntax, utf8
if tier 2; then
  run_tier 2 "capability syntax utf8" "${STOP_AT_T2:-}"
  sentinel_factor "$W/suite_t2.log"
  sentinel_factor "$W/suite_t2_end.log"
fi
echo "driver sha256 (end):" >> "$L"; drvsum
echo "CHAIN_DONE $(date -Is)" >> "$L"
