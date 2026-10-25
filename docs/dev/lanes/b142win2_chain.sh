#!/bin/bash
# [B147] PART 2 of the first window at 9ae59f5d4 (abi 84): bench/subst@0.1 on
# acc-main (361,986,301 B), the LIBRARY tier and the TOOLS tier, framed by the
# BD16 sentinel reads. Written 2026-10-25 by lane b147chains while part 1 ran;
# NOT RUN. Launched by the manager as a box-queue RESERVATION (runbook:
# docs/dev/lanes/b142night_runbook.md):
#
#     MACHINE_ID=ryzen7700x setsid scripts/boxq_window --name b142-part2 --prio 710 \
#         --cap 14520 --patience 86400 --idle-ok 600 --start-s 300 -- \
#         docs/dev/lanes/b142win2_chain.sh
#
# (the wrapper passes the environment through; MACHINE_ID is required.) Direct
# launch: `scripts/boxq_window --no-queue -- docs/dev/lanes/b142win2_chain.sh`.
# Run from the MAIN tree (build/, store/ and the pcrec builds live there).
#
# Completion: /var/tmp/pcrecbench/b142win2/chain.log ends `CHAIN_DONE`;
# `CHAIN_ABORT <why>` = nothing measured. The chain's exit status is 0 on
# CHAIN_DONE (the wrapper then prints BENCH_WINDOW_COMPLETE rc=0), 9 on abort.
#
# WHAT RUNS (in order), all at pcrec 9ae59f5d4, the canonical pin:
#   0. preconditions: names resolve, tool pins, disk, subject files vs
#      bench/subst/manifest.tsv (GENERATED here if missing -- see SUBJECT below)
#   1. OPENING SENTINEL ([B133]/BD16 (3)): bench/sentinel x {pcre2-jit,
#      rust-default, re2-default, pcrec-auto}. The BD16 reading OWED by
#      b140drv (pcre2-jit), b140drv2 (rust-default, re2-default) and b140pcrec
#      (pcrec): a sentinel flat against earlier windows = the instrument did
#      not move. rust-default / re2-default have no sentinel history we have
#      read; their opening-vs-closing pair is then the only baseline.
#   2. LIBRARY tier, bench/subst x {pcre2-jit, pcre2-jit-sizefirst,
#      pcre2-interp, pcre2-interp-sizefirst, pcrec-auto, pcrec-auto-sizefirst,
#      pcrec-vm, pcrec-vm-sizefirst, rust-default, re2-default}; both subjects
#      (acc-small is ~1 % of acc-main; the harness runs the manifest's list)
#   3. JIT-STACK CHECK (design 8 item 11; b140drv_report finding 6): see below
#   4. TOOLS tier, bench/subst x {sed-ere, perl-p, python-resub, sd-stdin,
#      rg-passthru}
#   5. CLOSING SENTINEL, same roster as the opening one (SENT_END=0 skips)
#
# THE JIT-STACK CHECK. The pcre2 driver creates NO JIT stack of its own
# (testees/pcre2/driver.c, timed_subst.c: nothing named jit_stack), so a
# pattern that exhausts libpcre2's default JIT stack on a 362 MB subject
# returns -46 (PCRE2_ERROR_JIT_STACKLIMIT), which the driver reports as
# `giveup:-46:...` and the harness records as a match row with outcome
# `gave-up` whose diagnostic carries the code/name (adapter.py maps -46 to
# "PCRE2_ERROR_JIT_STACKLIMIT"); the cell is still WRITTEN. acc-small gave no
# -46 on any of the 8 cases (b140drv_report finding 6); acc-main is this
# check. After the library tier the chain greps the records the jit cells
# wrote (newer than this chain's start stamp, testee id containing `jit`) for
# JIT_STACKLIMIT / giveup:-46 and logs `JITSTACK_HIT <file>` per record plus
# `JITSTACK_CHECK files=N hits=M gave_up_rows=K`. hits=0 is the result "no -46
# on acc-main"; hits>0 means those cells carry a `gave-up` row that is NOT a
# pcre2-jit property but this bench's missing jit_stack_create (a driver
# decision for the manager, not a result to rank). (The brief called this
# "F5"; in b140drv_report.md it is finding 6 / "8a item 11" -- F5 there is the
# quick/report gap.)
#
# SUBJECT. bench/subst/gen_subjects.py writes subjects/acc-small.log and
# acc-main.log (gitignored), deterministic from logsim.py, checked against
# bench/subst/manifest.tsv (len + sha256). The default location here is
# /var/tmp/pcrecbench/subst/subjects (a disk, not tmpfs; override with
# $PCRECBENCH_SUBST_SUBJECTS). The gate needs, per the harness: the two
# subject files at that path with the manifest's hashes, and the committed
# expectations.tsv (16 rows) -- nothing else is generated. If a file is
# missing or its sha256 differs the chain REGENERATES it (gnutimeout 3600),
# which costs CPU and wall time inside the reservation (unmeasured: 1.6 M
# simulated lines; budget 10-15 min). To keep the window for measuring,
# PRE-GENERATE before the reservation starts (the manager, outside any other
# window): `python3 bench/subst/gen_subjects.py --out /var/tmp/pcrecbench/subst/subjects`.
# The chain re-verifies the hashes either way and aborts on a mismatch that
# regeneration does not fix.
#
# BOX RULE. The quiet gate refuses a cell when any core is over 10 % busy; the
# chain itself does no heavy work between cells except the optional subject
# generation (before the first quiet check of a cell) and the grep above.
#
# DEADLINE. STOP_AT_NIGHT (default 09:30 on the morning after launch; today's
# date if launched after midnight and before noon, else tomorrow's) is the
# time after which NO cell may end up running past 10:00: each phase gets
# STOP_AT = STOP_AT_NIGHT - (that phase's longest-cell minutes - 10), i.e. a
# cell may START only if it is expected to end by STOP_AT_NIGHT + 10 min; the
# closing sentinel's cells start no later than STOP_AT_NIGHT + 10 min (a cell
# ~6.5 min), so the last cell ends by ~09:47. Skipped cells are named in the
# suite logs ("STOP_AT reached ... cells NOT started"). Override:
# STOP_AT_NIGHT="2026-10-26 09:30".
#
# ESTIMATE (~3.1 h; the basis is stated in b142night_runbook.md and
# b147chains_report.md): sentinel 4 x ~6.2 min = ~25 min per pass (b136's
# measured cell minutes; part 1 budgeted 26 min for four); library tier ~45
# min; tools tier ~60 min; run_window's sidecar regeneration + warm-ups ~3 min
# per window x 5; subject generation 0 (pre-generated) to ~15 min.
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b142win2; mkdir -p "$W"
L=$W/chain.log
export PIN=${PIN:-7}
STORE=store
echo "CHAIN_START $(date -Is) PIN=$PIN MACHINE_ID=${MACHINE_ID:-<unset>}" >> "$L"
abort() { echo "CHAIN_ABORT $*" >> "$L"; exit 9; }
[ -n "${MACHINE_ID:-}" ] || abort "MACHINE_ID is not set; nothing measured"
touch "$W/start.stamp"

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
SENT="pcre2-jit rust-default re2-default pcrec-auto"
LIB="pcre2-jit pcre2-jit-sizefirst pcre2-interp pcre2-interp-sizefirst pcrec-auto pcrec-auto-sizefirst pcrec-vm pcrec-vm-sizefirst rust-default re2-default"
TOOLS="sed-ere perl-p python-resub sd-stdin rg-passthru"
SENT_END=${SENT_END:-1}

python3 -m pcrecbench testees 2>>"$L" | awk '{print $1}' > "$W/testees.names"
for t in $SENT $LIB $TOOLS; do
  grep -qx -- "${t%@*}" "$W/testees.names" || abort "testee '$t' does not resolve"
done

# --- the tools tier's binaries (the adapter re-checks at describe/run time) --
for c in taskset fincore wc sed perl python3; do
  command -v "$c" > /dev/null || abort "tool '$c' not on PATH"
done
for t in $TOOLS; do
  p=$(sed -n "/^\[testees\.$t\]/,/^\[/{s/^path *= *\"\(.*\)\"/\1/p}" testees/tools/tools.toml)
  h=$(sed -n "/^\[testees\.$t\]/,/^\[/{s/^binary_sha256 *= *\"\(.*\)\"/\1/p}" testees/tools/tools.toml)
  [ -n "$p" ] && [ -x "$p" ] || abort "tool binary for $t missing: '$p'"
  if [ -n "$h" ]; then
    [ "$(sha256sum "$p" | cut -d' ' -f1)" = "$h" ] || abort "tool binary for $t ($p) does not match binary_sha256"
  fi
done

# --- machine registration, pcrec build, sentinel subjects --------------------
read -r HOSTN CPUSLUG NCORES < <(python3 -c "
import platform
from pcrecbench import env
print(platform.node() or 'unknown', env.canon_cpu_model(env.cpu_model_raw()), env.cores())")
python3 -m pcrecbench machines register --store "$STORE" --machine-id "$MACHINE_ID" \
    --hostname "$HOSTN" --cpu-model "$CPUSLUG" --cores "$NCORES" \
    --first-seen "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --note "[B142] b142win2_chain.sh" >> "$L" 2>&1 \
  || abort "machines register ($MACHINE_ID $HOSTN) refused"
sh testees/pcrec/pin.sh --path 9ae59f5d4 >> "$L" 2>&1 || abort "no build of 9ae59f5d4"
for g in gen_subjects.py gen_throughput_subjects.py; do
  [ -f bench/sentinel/$g ] || continue
  gnutimeout 900 python3 bench/sentinel/$g >> "$L" 2>&1 || abort "bench/sentinel/$g failed"
done
[ -d bench/sentinel/subjects ] || abort "bench/sentinel/subjects missing"

# --- the substitution subjects and disk --------------------------------------
export PCRECBENCH_SUBST_SUBJECTS=${PCRECBENCH_SUBST_SUBJECTS:-/var/tmp/pcrecbench/subst/subjects}
export PCRECBENCH_SUBST_OUT=${PCRECBENCH_SUBST_OUT:-/var/tmp/pcrecbench/b142win2/out}
SUBJ=$PCRECBENCH_SUBST_SUBJECTS
mkdir -p "$SUBJ" "$PCRECBENCH_SUBST_OUT" || abort "cannot create $SUBJ or $PCRECBENCH_SUBST_OUT"
avail=$(df --output=avail -BG /var/tmp | tail -1 | tr -dc 0-9)
[ "${avail:-0}" -ge 30 ] || abort "/var/tmp has ${avail}G free; the subst outputs need ~4 GB, want 30"
subj_ok() { # every manifest row: file present, len and sha256 equal
  local id len sha rest f ok=0
  while IFS=$'\t' read -r id len sha rest; do
    [ "$id" = id ] && continue
    f="$SUBJ/$id.log"
    [ -f "$f" ] && [ "$(stat -c %s "$f")" = "$len" ] && [ "$(sha256sum "$f" | cut -d' ' -f1)" = "$sha" ] || ok=1
  done < bench/subst/manifest.tsv
  return $ok
}
if ! subj_ok; then
  echo "SUBJECT missing or stale under $SUBJ: generating $(date -Is)" >> "$L"
  gnutimeout 3600 python3 bench/subst/gen_subjects.py --out "$SUBJ" >> "$L" 2>&1 || abort "bench/subst/gen_subjects.py failed"
  git diff --quiet -- bench/subst/manifest.tsv bench/subst/planted.tsv || abort "gen_subjects.py changed the committed manifest/planted"
  subj_ok || abort "subst subjects do not match bench/subst/manifest.tsv after generation"
fi
echo "SUBJECT ok $SUBJ $(date -Is)" >> "$L"

python3 -m pcrecbench quiet --samples 5 --pin "$PIN" >> "$L" 2>&1; echo "quiet rc=$?" >> "$L"
drvsum() {
  for t in $LIB $SENT; do for f in build/work/$t/*driver*; do [ -f "$f" ] && sha256sum "$f"; done; done | sort -u >> "$L" 2>&1
}
drvsum

# --- the window ---------------------------------------------------------------
export CELL_CAP_sentinel=3600 CELL_CAP_sentinel_end1=3600
export CELL_CAP_subst_lib=3600 CELL_CAP_subst_tools=5400

# 1. opening sentinel (BD16 (3))
STOP_AT="" SENTINEL=0 SUITE="sentinel" SUITE_LOG="$W/suite_sent0.log" \
  TESTEES_sentinel="$SENT" \
  NOTE="[B142] part 2 opening sentinel, BD16 (3) reads ($MACHINE_ID)" \
  STORE="$STORE" scripts/run_suite.sh >> "$L" 2>&1
echo "SENT0_DONE rc=$? $(date -Is)" >> "$L"

# 2. library tier (longest cell expected ~15 min: pcre2-interp-sizefirst / pcrec-vm-sizefirst)
S_LIB=$(stop_for 15); echo "STOP_AT lib=$S_LIB" >> "$L"
STOP_AT="$S_LIB" SENTINEL=0 SUITE="subst:lib" SUITE_LOG="$W/suite_lib.log" \
  TESTEES_subst_lib="$LIB" \
  NOTE="[B142] part 2 bench/subst library tier at 9ae59f5d4 ($MACHINE_ID)" \
  STORE="$STORE" scripts/run_suite.sh >> "$L" 2>&1
echo "LIB_DONE rc=$? $(date -Is)" >> "$L"

# 3. JIT-stack check over the records the library tier just wrote
n=0 hits=0 gu=0
while IFS= read -r f; do
  n=$((n + 1))
  g=$(grep -o -c -E 'gave-up' "$f" 2>/dev/null); gu=$((gu + ${g:-0}))
  if grep -q -E 'JIT_STACKLIMIT|giveup:-46' "$f"; then hits=$((hits + 1)); echo "JITSTACK_HIT $f" >> "$L"; fi
done < <(find store/records/subst@0.1 -type f -name '*.jsonl' -path '*jit*' -newer "$W/start.stamp" 2>/dev/null)
echo "JITSTACK_CHECK files=$n hits=$hits gave_up_rows=$gu (files = jit records written since chain start; lines, not rows, if the record is one JSON line per row)" >> "$L"

# 4. tools tier (longest cell expected ~30 min: python-resub / perl-p; cap 90 min)
S_TOOLS=$(stop_for 30); echo "STOP_AT tools=$S_TOOLS" >> "$L"
STOP_AT="$S_TOOLS" SENTINEL=0 SUITE="subst:tools" SUITE_LOG="$W/suite_tools.log" \
  TESTEES_subst_tools="$TOOLS" \
  NOTE="[B142] part 2 bench/subst tools tier at 9ae59f5d4 ($MACHINE_ID)" \
  STORE="$STORE" scripts/run_suite.sh >> "$L" 2>&1
echo "TOOLS_DONE rc=$? $(date -Is)" >> "$L"

# 5. closing sentinel: its cells (~6.5 min) start only before STOP_AT_NIGHT + 10 min
if [ "$SENT_END" = 1 ]; then
  S_END=$(date -d "@$((stop_epoch + 600))" '+%F %T')
  STOP_AT="$S_END" SENTINEL=0 SUITE="sentinel:end1" SUITE_LOG="$W/suite_sent1.log" \
    TESTEES_sentinel_end1="$SENT" \
    NOTE="[B142] part 2 closing sentinel ($MACHINE_ID)" \
    STORE="$STORE" scripts/run_suite.sh >> "$L" 2>&1
  echo "SENT1_DONE rc=$? $(date -Is)" >> "$L"
fi
drvsum
echo "CHAIN_DONE $(date -Is)" >> "$L"
