#!/usr/bin/env bash
# Self-test for scripts/boxq_window ([B146]). FAKE state dir, FAKE inbox, FAKE
# chains (sleep scripts); never touches pcrec's queue; seconds. Every case is
# checked against the wrapper's own log lines. Run: bash scripts/tests/test_boxq_window.sh
set -u
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
WRAP=$HERE/../boxq_window
T=$(mktemp -d "${TMPDIR:-/var/tmp}/boxq_test.XXXXXX") || exit 2
trap '[ -n "${KEEP:-}" ] || rm -rf "$T"' EXIT
export BQ_STATE_DIR=$T/state BQ_INBOX=$T/inbox BQ_LOGDIR=$T/log BQ_POLL=1 BQ_TICK=1 BQ_KILL_GRACE=3 BQ_IMPORT_WAIT=5 BQ_PROGRESS=1
mkdir -p "$BQ_STATE_DIR" "$BQ_INBOX"
PASS=0 FAIL=0
ck() { if eval "$2"; then PASS=$((PASS+1)); else FAIL=$((FAIL+1)); echo "FAIL: $1   [$2]"; fi; }
lg() { echo "$T/log/$1/run.log"; }   # BQ_LOGDIR is per-case below

mkchain() { printf '#!/usr/bin/env bash\n%s\n' "$2" > "$T/$1"; chmod +x "$T/$1"; }
mkchain ok.sh 'echo chain-out; sleep 2; exit 0'
mkchain bad.sh 'sleep 1; exit 7'
mkchain long.sh 'echo $$ > "$PIDF"; sleep 600 & echo $! > "$PIDF.child"; wait'
mkchain never.sh 'touch "$T_RAN"; exit 0'

# run CASE NAME PRIO ... : wrapper in background, output to $T/out.CASE
start() { local c=$1; shift; BQ_LOGDIR=$T/log/$c "$WRAP" "$@" > "$T/out.$c" 2>&1 & echo $! > "$T/pid.$c"; }
waitw() { local c=$1 i=0; while kill -0 "$(cat "$T/pid.$c")" 2>/dev/null && [ $i -lt 40 ]; do sleep 0.5; i=$((i+1)); done
          wait "$(cat "$T/pid.$c")" 2>/dev/null; echo $? > "$T/rc.$c"; }
# like pcrec, write a state only AFTER the reservation was imported (.window present)
st() { local n=${1#*-bench-} i=0; while [ ! -e "$BQ_INBOX/$n.window" ] && [ $i -lt 20 ]; do sleep 0.25; i=$((i+1)); done
       echo "$2" > "$BQ_STATE_DIR/$1.state"; }
L() { echo "$T/log/$1/run.log"; }

# 1 green: RUNNING, chain exits 0, complete line
start green --name green --prio 710 --cap 60 --idle-ok 5 -- "$T/ok.sh"
sleep 1.5
ck "1 window file written" "[ -f $BQ_INBOX/green.window ]"
for k in prio=710 name=green cap=60 patience= idle_ok=5 "log=$T/log/green/run.log" start_s= 'done_ere=^BENCH_WINDOW_COMPLETE rc=' expect=0 witness='BENCH_WINDOW_COMPLETE rc=0' 'fail_ere=^BENCH_WINDOW_FAILED '; do
  ck "1 window key $k" "grep -qxF -- '$k'* $BQ_INBOX/green.window || grep -qF -- '$k' $BQ_INBOX/green.window"; done
ck "1 chain not started while no RUNNING" "[ ! -s $T/log/green/run.log.chain ] 2>/dev/null"
st 710-bench-green "RUNNING 2026-10-25T10:00:00 4242"
waitw green
ck "1 complete line in log" "grep -qx 'BENCH_WINDOW_COMPLETE rc=0' $(L green)"
ck "1 no fail line" "! grep -q '^BENCH_WINDOW_FAILED' $(L green)"
ck "1 rc 0" "[ \$(cat $T/rc.green) = 0 ]"
ck "1 chain output kept out of the run log" "! grep -q chain-out $(L green) && grep -q chain-out $(L green).chain"

# 2 chain fails
start bad --name bad --prio 720 --cap 60 -- "$T/bad.sh"
st 720-bench-bad "RUNNING 2026-10-25T10:00:00 1"
waitw bad
ck "2 fail line with rc" "grep -qx 'BENCH_WINDOW_FAILED chain rc=7' $(L bad)"
ck "2 no complete line" "! grep -q '^BENCH_WINDOW_COMPLETE' $(L bad)"
ck "2 rc nonzero" "[ \$(cat $T/rc.bad) != 0 ]"

# 3 state flips to DONE cancelled mid-run: the chain's process group dies
export PIDF=$T/pidf
start mid --name mid --prio 730 --cap 60 -- "$T/long.sh"
st 730-bench-mid "RUNNING 2026-10-25T10:00:00 1"
sleep 2.5
CP=$(cat $PIDF); CC=$(cat $PIDF.child)
ck "3 chain alive before the flip" "kill -0 $CP && kill -0 $CC"
ck "3 chain is its own group leader" "[ \$(ps -o pgid= -p $CP | tr -d ' ') = $CP ]"
st 730-bench-mid "DONE cancelled 2026-10-25T10:01:00 operator"
waitw mid
ck "3 left-RUNNING line" "grep -q 'state left RUNNING: DONE cancelled' $(L mid)"
ck "3 kill line names the pid" "grep -q 'killing chain process group $CP' $(L mid)"
ck "3 chain pid gone" "! kill -0 $CP 2>/dev/null"
ck "3 chain child gone" "! kill -0 $CC 2>/dev/null"
ck "3 progress line while the chain runs (queuewatch idle alarm)" "grep -q 'progress chain_bytes=' $(L mid)"
ck "3 fail line" "grep -q '^BENCH_WINDOW_FAILED state left RUNNING' $(L mid)"

# 4 QUEUED then RUNNING after a delay
start q --name q --prio 740 --cap 60 -- "$T/ok.sh"
st 740-bench-q "QUEUED 2026-10-25T10:00:00"
sleep 2.5
ck "4 QUEUED logged, no chain yet" "grep -q 'state: QUEUED' $(L q) && ! grep -q 'starting chain' $(L q)"
st 740-bench-q "RUNNING 2026-10-25T10:00:03 9"
waitw q
ck "4 started after RUNNING" "grep -q 'RUNNING: starting chain' $(L q)"
ck "4 complete" "grep -qx 'BENCH_WINDOW_COMPLETE rc=0' $(L q)"

# 5 DONE before start: the chain never runs
export T_RAN=$T/ran
st 750-bench-d "DONE cancelled 2026-10-25T10:00:00 early"
start d --name d2 --prio 750 --cap 60 -- "$T/never.sh"   # different name: state for d is not d2's
sleep 1; st 750-bench-d2 "DONE failed 2026-10-25T10:00:00 NO-START"
waitw d
ck "5 chain never ran" "[ ! -e $T_RAN ]"
ck "5 DONE-before-start logged" "grep -q 'DONE before start' $(L d)"
ck "5 fail line, nonzero rc" "grep -q '^BENCH_WINDOW_FAILED' $(L d) && [ \$(cat $T/rc.d) != 0 ]"

# 6 duplicate names refused (existing .window; existing state; cancel written)
BQ_LOGDIR=$T/log/dup "$WRAP" --name green --prio 710 --cap 60 -- "$T/ok.sh" > "$T/out.dup" 2>&1; rc=$?
ck "6 duplicate .window refused" "[ $rc = 2 ] && grep -q 'name already used' $T/out.dup"
st 760-bench-onlystate "DONE green 2026-10-25T10:00:00 x"
BQ_LOGDIR=$T/log/dup2 "$WRAP" --name onlystate --prio 799 --cap 60 -- "$T/ok.sh" > "$T/out.dup2" 2>&1; rc=$?
ck "6 existing state (other prio) refused, no .window written" "[ $rc = 2 ] && [ ! -e $BQ_INBOX/onlystate.window ]"

# 7 --no-queue: no window file, no state, runs directly
BQ_LOGDIR=$T/log/nq "$WRAP" --no-queue -- "$T/ok.sh" > "$T/out.nq" 2>&1; rc=$?
ck "7 no-queue complete line, rc 0" "[ $rc = 0 ] && grep -qx 'BENCH_WINDOW_COMPLETE rc=0' $T/out.nq"
BQ_LOGDIR=$T/log/nq "$WRAP" --no-queue --name nqname -- "$T/bad.sh" > "$T/out.nq2" 2>&1; rc=$?
ck "7 no-queue failure prints fail line, rc 7" "[ $rc = 7 ] && grep -q '^BENCH_WINDOW_FAILED' $T/out.nq2"
ck "7 no-queue wrote no reservation" "[ ! -e $BQ_INBOX/nqname.window ]"

# 8 --cancel writes NAME.cancel
"$WRAP" --cancel xyz > /dev/null 2>&1
ck "8 cancel file" "[ -e $BQ_INBOX/xyz.cancel ]"

# 9 SIGTERM to the wrapper: group killed, fail line (the trap)
start sig --name sig --prio 770 --cap 60 -- "$T/long.sh"
st 770-bench-sig "RUNNING 2026-10-25T10:00:00 1"
sleep 2.5; CP=$(cat $PIDF); CC=$(cat $PIDF.child)
kill -TERM "$(cat $T/pid.sig)"
waitw sig
ck "9 chain gone after SIGTERM" "! kill -0 $CP 2>/dev/null && ! kill -0 $CC 2>/dev/null"
ck "9 fail line on signal" "grep -qx 'BENCH_WINDOW_FAILED signal' $(L sig)"

echo "boxq_window self-test: $PASS passed, $FAIL failed"
[ "$FAIL" = 0 ]
