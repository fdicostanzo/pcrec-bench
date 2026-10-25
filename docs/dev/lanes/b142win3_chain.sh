#!/bin/bash
# [B147] TIER 2 of the first window at 9ae59f5d4 (abi 84) -- b142prep_report.md
# section 8, tier 2: the sets of the abi-78 / [FLAG-SPELL] / K128 movers at BOTH
# pins (the canonical 9ae59f5d4 and the same-window BEFORE @6b2dbd3e), plus the
# retry-machine/compile-cost sets, framed by a sentinel pair. Written
# 2026-10-25 by lane b147chains while part 1 ran; NOT RUN. Launched by the
# manager as a box-queue reservation AFTER part 2 (runbook:
# docs/dev/lanes/b142night_runbook.md):
#
#     MACHINE_ID=ryzen7700x setsid scripts/boxq_window --name b142-tier2 --prio 720 \
#         --cap 29700 --patience 86400 --idle-ok 600 --start-s 300 -- \
#         docs/dev/lanes/b142win3_chain.sh
#
# Run from the MAIN tree. Completion: /var/tmp/pcrecbench/b142win3/chain.log
# ends `CHAIN_DONE`; `CHAIN_ABORT <why>` = nothing measured.
#
# ROSTER (every entry a `testee` at 9ae59f5d4 or `testee@6b2dbd3e`, the pair
# ADJACENT so the two records of a set sit minutes apart -- run_window.sh):
#   sentinel (open)  pcrec-auto  pcrec-auto@6b2dbd3e  pcre2-jit(flat control)
#   loglines (LOGLINES=1, default on; set LOGLINES=0 if part 1 measured it)
#   litrun   pcrec-auto  pcrec-auto@6b2dbd3e
#   syntax   pcrec-auto  pcrec-auto@6b2dbd3e         (syntax@0.1, master's)
#   utf8     pcrec-auto-utf8  pcrec-auto-utf8@6b2dbd3e   (the -utf8 siblings)
#   email    pcrec-auto  pcrec-auto@6b2dbd3e
#   bounded  pcrec-auto  pcrec-auto@6b2dbd3e         (bounded@0.3)
#   sentinel (close) same roster as the opening pass
# Order = importance, longest-last: the movers' sets first (litrun, syntax,
# utf8), then email, then bounded (two ~50 min cells, whose point is compile
# cost and load, not hot code) -- a late start loses bounded, never the
# movers; the closing sentinel always runs. The sets are the CURRENT versions
# on master (syntax@0.1, capability@0.2 is not in this tier); the lane/b123subj
# version bumps are NOT merged and not used.
#
# ESTIMATE (~6.4 h; basis: b142prep_report.md section 8's b136-MEASURED cell
# minutes, nothing re-timed at this pin): loglines 8.4 x2 = 17; litrun 13 x2 =
# 26; syntax 44 x2 = 88; utf8 37 x2 = 74; email 5 x2 = 10; bounded 50 x2 =
# 100; sentinel 6.2 x3 x2 passes = 37; run_window's per-window sidecar
# regeneration + warm-up ~3 min x 8 windows = 24; subject generation ~5 (a
# no-op when the trees exist) => ~381 min = 6.35 h.
#
# DEADLINE. STOP_AT_NIGHT (default 09:30 on the morning after launch; today's
# date if launched after midnight and before noon, else tomorrow's): each set
# gets STOP_AT = STOP_AT_NIGHT - (its longest-cell minutes, with ~25 %
# headroom, minus 10), i.e. a cell may START only if it is expected to end by
# STOP_AT_NIGHT + 10 min; the closing sentinel's cells start no later than
# STOP_AT_NIGHT + 10 min (~6.5 min each), so nothing runs past ~09:47. Skipped
# cells are named in the suite logs ("STOP_AT reached ... cells NOT started").
# Override: STOP_AT_NIGHT="2026-10-26 09:30".
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b142win3; mkdir -p "$W"
L=$W/chain.log
export PIN=${PIN:-7}
STORE=store
echo "CHAIN_START $(date -Is) PIN=$PIN MACHINE_ID=${MACHINE_ID:-<unset>}" >> "$L"
abort() { echo "CHAIN_ABORT $*" >> "$L"; exit 9; }
[ -n "${MACHINE_ID:-}" ] || abort "MACHINE_ID is not set; nothing measured"

# --- the deadline -----------------------------------------------------------
if [ -z "${STOP_AT_NIGHT:-}" ]; then
  if [ "$(date +%-H)" -ge 12 ]; then d=$(date -d tomorrow +%F); else d=$(date +%F); fi
  STOP_AT_NIGHT="$d 09:30"
fi
stop_epoch=$(date -d "$STOP_AT_NIGHT" +%s) || abort "unparseable STOP_AT_NIGHT='$STOP_AT_NIGHT'"
[ $((stop_epoch - $(date +%s))) -ge 5400 ] || abort "less than 90 min before STOP_AT_NIGHT ($STOP_AT_NIGHT); nothing measured"
stop_for() { # MAXCELL_MIN -> a `date -d` time: a cell of that length may start only before it
  date -d "@$((stop_epoch + (10 - $1) * 60))" '+%F %T'
}
echo "STOP_AT_NIGHT=$STOP_AT_NIGHT" >> "$L"

# --- the rosters -------------------------------------------------------------
B=6b2dbd3e
LOGLINES=${LOGLINES:-1}
SENT_END=${SENT_END:-1}
R_SENT="pcrec-auto pcrec-auto@$B pcre2-jit"
R_STD="pcrec-auto pcrec-auto@$B"
R_UTF="pcrec-auto-utf8 pcrec-auto-utf8@$B"

python3 -m pcrecbench testees 2>>"$L" | awk '{print $1}' > "$W/testees.names"
for t in $R_SENT $R_STD $R_UTF; do
  grep -qx -- "${t%@*}" "$W/testees.names" || abort "testee '$t' does not resolve"
done

# --- machine registration, both pcrec builds, subject trees -------------------
read -r HOSTN CPUSLUG NCORES < <(python3 -c "
import platform
from pcrecbench import env
print(platform.node() or 'unknown', env.canon_cpu_model(env.cpu_model_raw()), env.cores())")
python3 -m pcrecbench machines register --store "$STORE" --machine-id "$MACHINE_ID" \
    --hostname "$HOSTN" --cpu-model "$CPUSLUG" --cores "$NCORES" \
    --first-seen "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --note "[B142] b142win3_chain.sh" >> "$L" 2>&1 \
  || abort "machines register ($MACHINE_ID $HOSTN) refused"
for s in 9ae59f5d4 $B; do
  sh testees/pcrec/pin.sh --path $s >> "$L" 2>&1 || abort "no build of $s"
done
for d in sentinel loglines litrun syntax utf8 email bounded; do
  for g in gen_subjects.py gen_throughput_subjects.py; do
    [ -f bench/$d/$g ] || continue
    gnutimeout 1800 python3 bench/$d/$g >> "$L" 2>&1 || abort "bench/$d/$g failed"
  done
  [ -d bench/$d/subjects ] || abort "bench/$d/subjects missing"
done
python3 -m pcrecbench quiet --samples 5 --pin "$PIN" >> "$L" 2>&1; echo "quiet rc=$?" >> "$L"
drvsum() {
  for t in pcrec-auto pcrec-auto-utf8 pcre2-jit; do
    for f in build/work/$t/*driver*; do [ -f "$f" ] && sha256sum "$f"; done
  done >> "$L" 2>&1
}
drvsum

# one run_suite.sh invocation for ONE set (separate invocations so that each
# set's STOP_AT carries its own longest-cell margin)
run_set() { # SET MAXCELL_MIN "TESTEES" CELL_CAP_S
  local set=$1 m=$2 tl=$3 cap=$4 stop rc
  stop=$(stop_for "$m")
  echo "STOP_AT $set=$stop" >> "$L"
  env STOP_AT="$stop" SENTINEL=0 SUITE="$set" SUITE_LOG="$W/suite_$set.log" \
      TESTEES="$tl" CELL_CAP="$cap" \
      NOTE="[B142] tier 2 $set at 9ae59f5d4 vs @$B ($MACHINE_ID)" \
      STORE="$STORE" scripts/run_suite.sh >> "$L" 2>&1
  rc=$?
  echo "SET_DONE $set rc=$rc $(date -Is)" >> "$L"
}

# opening sentinel
env STOP_AT="" SENTINEL=0 SUITE="sentinel" SUITE_LOG="$W/suite_sent0.log" \
    TESTEES_sentinel="$R_SENT" CELL_CAP_sentinel=3600 \
    NOTE="[B142] tier 2 opening sentinel ($MACHINE_ID)" \
    STORE="$STORE" scripts/run_suite.sh >> "$L" 2>&1
echo "SENT0_DONE rc=$? $(date -Is)" >> "$L"

# the sets (longest-cell minutes include ~25 % headroom over b136's measured)
[ "$LOGLINES" = 1 ] && run_set loglines 12 "$R_STD" 3600
run_set litrun  18 "$R_STD" 3600
run_set syntax  55 "$R_STD" 5400
run_set utf8    50 "$R_UTF" 5400
run_set email   10 "$R_STD" 3600
run_set bounded 65 "$R_STD" 5400

# closing sentinel: its cells (~6.5 min) start only before STOP_AT_NIGHT + 10 min
if [ "$SENT_END" = 1 ]; then
  S_END=$(date -d "@$((stop_epoch + 600))" '+%F %T')
  env STOP_AT="$S_END" SENTINEL=0 SUITE="sentinel:end1" SUITE_LOG="$W/suite_sent1.log" \
      TESTEES_sentinel_end1="$R_SENT" CELL_CAP_sentinel_end1=3600 \
      NOTE="[B142] tier 2 closing sentinel ($MACHINE_ID)" \
      STORE="$STORE" scripts/run_suite.sh >> "$L" 2>&1
  echo "SENT1_DONE rc=$? $(date -Is)" >> "$L"
fi
drvsum
echo "CHAIN_DONE $(date -Is)" >> "$L"
