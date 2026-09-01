#!/bin/bash
# probe_spread_rule_control.sh -- [B23] the v1.4 spread rule's MEASURED
# POSITIVE CONTROL (docs/design/gate_shape_v14.md 9 Q3 (a); plan row [B23]).
#
# Runs the arms end to end from the repo root, each a real `pcrecbench
# run` (the adapters' own compile and driver paths -- D35 rule 4), all
# tier SCRATCH (this whole demonstration is deliberate load; nothing here
# is a ranking input, and the canonical store would refuse the records):
#
#   arm 1  CONTROL (negative): the cell on the quiet box, no competitor.
#          Expected: verdict `agree`, status `measured`, exit 0.
#   arm 2  LOADED (positive): the same cell; a competitor pinned to CPU 5
#          -- the target core 11's SMT sibling (thread_siblings_list is
#          "5,11" for both on budu-ryzen1600) -- covering ~two of the
#          five trial passes of the TARGET GROUP. Expected: the target
#          group disagrees (d >= 2 and 3d >= n), verdict `disagree`,
#          status `inconclusive-spread`, exit 4.
#
# THE CELL: bench/email (email-specimen@0.2) x pcre2-interp, regime
# search_short only, --trials 5 --pin 11 --tier scratch. Small on
# purpose (~85 s an arm) and pcre2-only (no pcrec pin involved). Three
# groups run in pattern order (orig, factored, floor; 77 subjects each);
# the TARGET GROUP, named in advance, is the SECOND:
# factored / short-subject-search / plain (n = 77).
#
# SYNCHRONIZATION (honest -- the run's own progress output): the harness
# prints "measuring pcre2-interp / factored [plain] / search_short: ..."
# on stderr immediately before the driver's five passes of that group.
# The script watches the stderr log for that line, sleeps START_DELAY_S,
# then runs the competitor for COMPETITOR_S with a HARD self-timeout
# (gnutimeout is the competitor's parent). The constants come from the
# 2026-09-01 rehearsals on this box (archived beside this script):
#
#   driver startup (measuring line -> first pass)   ~2.5 s
#   clean pass of the target group                  ~5.4 s (5 passes ~27 s)
#   slowdown s under the competitor below           ~1.86  (slowed pass ~10 s)
#
# Every subject sits at the same relative offset in every pass, so ANY
# window >= 2 slowed passes long (>= 2 x 1.86 x 5.4 ~= 20 s) that starts
# and ends strictly inside the group's five passes slows >= 2 of every
# row's 5 trials -- the shape the rule flags at any phase. START_DELAY_S
# = 7 s starts the window near the pass-1/pass-2 boundary; COMPETITOR_S
# = 22 s ends it inside pass 4-5 (the group stretches to ~37-40 s under
# the load). The window never overlaps the pre-flight (a busy box would
# be `inconclusive-load`, which takes precedence and would hide the
# spread) nor the after sample (provenance either way at v1.4).
#
# THE COMPETITOR: a memory-bandwidth loop (Q3's own recommendation) --
# python copying a 64 MiB bytearray back and forth, 100 % busy on CPU 5
# and thrashing the shared L3/DRAM path. Rehearsal measured the pure
# shell busy-loop (`while :; do :; done`) at s ~= 1.45 on this cell --
# UNDER the rule's k = 1.5, i.e. inside blind band 1 (gate_shape_v14.md
# 3.2): 14 of 77 rows over threshold, group not flagged. That negative
# is itself a finding the archive keeps; the bandwidth loop is the
# competitor the demonstration uses. taskset -c 5 only, bounded seconds,
# killed by PID defensively at the end (never pkill).
#
# THE THIRD ARM (Q3 (b), added 2026-09-01 on the manager's change
# request): `uniform` -- the same competitor covering ALL FIVE passes of
# the target group, which band 2 of gate_shape_v14.md 3.2 predicts the
# rule MISSES (a uniform slowdown leaves the trials agreeing with each
# other and with the wrong number). Expected: verdict `agree`, status
# `measured`, exit 0, with the 3.6 timeline the only instrument that
# sees it. The window is EVENT-SCOPED at both ends rather than timed:
# the competitor starts AT the target group's "measuring" line (so it
# already runs during the ~2.5 s driver startup and pass 1) and is
# killed by PID the moment the NEXT group's "calibrating ... floor"
# line appears (the driver has exited; every factored pass is over),
# with gnutimeout 90 s as the hard backstop. A timed ~60 s window was
# rejected in design: if the slowdown drifts low it spills >= 2 slowed
# passes into floor (flagging the WRONG group), and if it drifts high
# it leaves pass 5 partially clean, whose rows the FAST clause then
# flags -- either way a boundary artifact, not the band-2 miss.
#
# Usage: bash docs/dev/measurements/probe_spread_rule_control.sh [outdir] [arms]
#        arms: any subset of "control loaded uniform" (default: all
#        three); default outdir: build/spread-rule-control -- gitignored;
#        the stores under it are scratch by tier

set -u
cd "$(dirname "$0")/../../.." || exit 1
OUT_DIR=${1:-build/spread-rule-control}
ARMS=${2:-"control loaded uniform"}
mkdir -p "$OUT_DIR"

START_DELAY_S=7.0
COMPETITOR_S=22
COMP_PY='
b = bytearray(1 << 26)   # 64 MiB
c = bytearray(1 << 26)
while True:
    c[:] = b
    b[:] = c'

TESTEE=pcre2-interp
RUN_ARGS=(--subbench email --testee "$TESTEE" --regimes search_short
          --trials 5 --tier scratch --pin 11)

stamp() {
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ)  $*"
}

extract() { python3 - "$1" <<'EOF'
import json, statistics, sys
from collections import defaultdict
path = sys.argv[1]
rows = []
with open(path) as f:
    setup = json.loads(f.readline())
    for line in f:
        r = json.loads(line)
        if r.get("kind") == "match":
            rows.append(r)
print("record: %s" % path.rsplit("/", 1)[-1])
print("schema_version %s  tier %s  status %s"
      % (setup.get("schema_version"), setup.get("tier"), setup.get("status")))
if setup.get("status_detail"):
    print("status_detail: %s" % setup["status_detail"])
print("trial_agreement (verbatim):")
print(json.dumps(setup.get("trial_agreement"), indent=2, sort_keys=True))
env = setup.get("environment") or {}
occ = env.get("occupancy") or {}
load = env.get("load") or {}
for s in ("before", "after"):
    o, l = occ.get(s) or {}, load.get(s) or {}
    print("%s: load1=%s  occupancy verdict=%s max_busy_pct=%s "
          "target_busy_pct=%s"
          % (s, l.get("load1"), o.get("verdict"), o.get("max_busy_pct"),
             o.get("target_busy_pct", "absent")))
print("occupancy.timeline (verbatim, %s):" % occ.get("timeline_tool"))
print(json.dumps(occ.get("timeline"), indent=2))
# The per-row picture at k=1.5 -- DISPLAY ONLY: the record's own stamped
# block above is the verdict (X31/X32 re-check it at store.write).
per = defaultdict(dict)
for r in rows:
    t = r.get("timing") or {}
    if r["match_outcome"] == "matched-as-expected" and t.get("iterations", 0) > 1:
        per[(r["pattern_id"], r["regime"], r.get("form") or "plain",
             r["subject_id"])][r["trial"]] = t["elapsed_ns"] / t["iterations"]
groups = defaultdict(lambda: {"n": 0, "d": 0, "hist": defaultdict(int)})
for key, trials in per.items():
    if len(trials) < 2:
        continue
    xs = [trials[t] for t in sorted(trials)]
    m = statistics.median(xs)
    slow = sum(1 for x in xs if x > 1.5 * m)
    fast = 1 if min(xs) < m / 1.5 else 0
    g = groups[key[:3]]
    g["n"] += 1
    g["hist"][slow] += 1
    if slow >= 2 or fast:
        g["d"] += 1
print("per-group rows at k=1.5 ({slow trials: rows}):")
for gk in sorted(groups):
    g = groups[gk]
    print("  %-40s n=%3d d=%3d %s"
          % ("/".join(gk), g["n"], g["d"], dict(sorted(g["hist"].items()))))
tgt = ("factored", "short-subject-search", "plain")
bytrial = defaultdict(list)
for key, trials in per.items():
    if key[:3] == tgt:
        for t, v in trials.items():
            bytrial[t].append(v)
print("target group mean ns/iter by trial:",
      "  ".join("t%d=%.1f" % (t, sum(v) / len(v))
                for t, v in sorted(bytrial.items())))
EOF
}

run_arm() {  # $1 = arm name, $2 = competitor mode (no / yes / uniform)
    local arm=$1 comp=$2
    local store="$OUT_DIR/store-$arm" err="$OUT_DIR/$arm.err" out="$OUT_DIR/$arm.out"
    rm -rf "$store"; rm -f "$err" "$out"; : > "$err"
    echo "== arm: $arm (competitor: $comp) =="
    stamp "arm $arm starts; /proc/loadavg: $(cat /proc/loadavg)"
    ( /usr/bin/gnutimeout 900 python3 -m pcrecbench run "${RUN_ARGS[@]}" \
        --store "$store" \
        --note "[B23] spread-rule positive control, arm $arm" \
        2> >(python3 -c 'import sys,time
t0=time.monotonic()
for l in sys.stdin:
    print("%8.2f %s"%(time.monotonic()-t0,l),end="",flush=True)' > "$err") \
        > "$out"; echo "exit=$?" >> "$out" ) &
    local runpid=$!
    if [ "$comp" != no ]; then
        local n=0
        until grep -q 'measuring pcre2-interp / factored' "$err"; do
            sleep 0.2; n=$((n + 1))
            [ $n -gt 900 ] && { echo "TRIGGER LINE NEVER APPEARED"; break; }
        done
        local cpid
        if [ "$comp" = uniform ]; then
            # Q3 (b): cover the WHOLE group -- start at the line (before
            # pass 1), kill when the next group's calibrating line says
            # every factored pass is over; gnutimeout 90 is the backstop.
            taskset -c 5 /usr/bin/gnutimeout 90 python3 -c "$COMP_PY" &
            cpid=$!
            stamp "trigger line seen; uniform competitor pid $cpid on cpu5 (kill at the floor calibrating line; 90 s backstop)"
            n=0
            until grep -q 'calibrating pcre2-interp / floor' "$err"; do
                sleep 0.2; n=$((n + 1))
                [ $n -gt 450 ] && { echo "FLOOR LINE NEVER APPEARED"; break; }
            done
            kill "$cpid" 2>/dev/null
            stamp "floor calibrating line seen; competitor killed by PID"
        else
            stamp "trigger line seen; sleeping $START_DELAY_S s"
            sleep "$START_DELAY_S"
            taskset -c 5 /usr/bin/gnutimeout "$COMPETITOR_S" python3 -c "$COMP_PY" &
            cpid=$!
            stamp "competitor pid $cpid on cpu5, $COMPETITOR_S s hard timeout"
            wait "$cpid" 2>/dev/null
            stamp "competitor exited"
        fi
        kill "$cpid" 2>/dev/null    # defensive; already ended above
    fi
    wait "$runpid"
    stamp "arm $arm run finished; /proc/loadavg: $(cat /proc/loadavg)"
    echo "-- timestamped progress (stderr) --"
    cat "$err"
    echo "-- run stdout --"
    cat "$out"
    echo "-- record extraction --"
    extract "$(head -1 "$out")"
    echo
}

stamp "probe_spread_rule_control.sh; bench commit $(git rev-parse --short HEAD); box $(hostname)"
echo "cpu11 SMT siblings: $(cat /sys/devices/system/cpu/cpu11/topology/thread_siblings_list)"
echo "cell: ${RUN_ARGS[*]}"
echo "target group (named in advance): factored / short-subject-search / plain"
echo

for arm in $ARMS; do
    case $arm in
        control) run_arm control no ;;
        loaded)  run_arm loaded yes ;;
        uniform) run_arm uniform uniform ;;
        *) echo "unknown arm: $arm" ;;
    esac
done

echo "== exit codes =="
for arm in $ARMS; do
    case $arm in
        control) want="exit=0, measured (agree)" ;;
        loaded)  want="exit=4, inconclusive-spread (two-pass window: flagged)" ;;
        uniform) want="exit=0, measured (all-five-passes window: MISSED, band 2)" ;;
    esac
    echo "$arm: $(grep '^exit=' "$OUT_DIR/$arm.out")   (predicted $want)"
done
