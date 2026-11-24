#!/bin/bash
# [B152] TONIGHT'S WINDOW, 2026-11-24 01:50 -> HARD END 07:55 (lane b152chain; modelled on b149w2_chain.sh /
# b149mon_chain.sh). PINNED tier into store/. First window at the new main pin d6c5e71a5.
#
# THE ONE SWITCH is MAIN_PIN below. MAIN_PIN=d6c5e71a5 -> MODE=full (the plan below). MAIN_PIN=cb32eda28 (the
# FALLBACK pin) -> MODE=fallback, derived (override with MODE=full|fallback in the env only for rehearsals):
#   FALLBACK = ONLY: sentinel open (pcrec-auto@cb32eda28 + pcre2-jit), altwide x {re2-default,
#   vectorscan-block-som, rust-default} (the non-pcrec cells, same skip rule), sentinel close (same two).
#   No pcrec altwide, no tier 3/4. The "@cb32eda28" arm is NOT run twice (one pcrec sentinel arm only).
#
# CELL ORDER (priority; the measured minutes on this box in brackets drive the skip rule):
#   1. sentinel@0.1 open:  pcrec-auto [6]  pcrec-auto@cb32eda28 [6]  pcre2-jit [7]            (never skipped)
#   2. altwide@0.3: pcrec-auto [17] pcrec-vm [15] re2-default [est 25] vectorscan-block-som [est 25] rust-default [23]
#   3. capability@0.4 pcrec-auto [62]; syntax@0.2 pcrec-auto [42]; bounded@0.3 pcrec-auto [47]
#   4. tail: utf8@0.1 pcrec-auto-utf8 [33]; loglines@0.1 pcrec-auto [10]; email-specimen@0.2 pcrec-auto [8]; litrun@0.1 pcrec-auto [14]
#   5. sentinel@0.1 close: the same three as 1 [~19]                                           (ALWAYS run, reserved last)
# (MODE=fallback: see above; the lists in sections 1, 2-4, 5 are cut down accordingly.)
# SKIP RULE (2-4): before each cell, now + est*60*1.3 s + CLOSE_RESERVE (25 min) must be <= HARD_END, else the cell
# is logged `SKIPPED <set> <testee> (deadline)` and the chain continues -- a shorter later cell may still fit. The
# per-cell cap (CELL_CAP) = 2x the estimate (floor 25 min), clamped so a cell never runs into the closing reserve.
# An inconclusive-spread re-measure is run_window.sh's own and counts against the clock.
#
# STORE: run_window.sh regenerates all interpretation sidecars (123 of them) at the end of EVERY call when STORE is
# the literal string `store`. The chain calls it once per cell, so it passes STORE=./store (the same directory, the
# `.canonical` marker still found; run_window's string test no longer matches) and regenerates sidecars ONCE, after
# the closing sentinel, if time remains. DRYRUN=1 uses a scratch store under $W and refuses `store`.
#
# Launch: the executable wrapper docs/dev/lanes/b152win_wrap.sh (boxq_window refuses `env ...`).
# Rehearsal: DRYRUN=1 (synthetic, scratch store, no real deadlines unless END="YYYY-MM-DD HH:MM" is set).
# Completion: /var/tmp/pcrecbench/b152win/chain.log ends `CHAIN_DONE`; `CHAIN_ABORT` = nothing measured.
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 9
export LC_ALL=C
W=${B152_WORK:-/var/tmp/pcrecbench/b152win}; mkdir -p "$W"
L=$W/chain.log

MAIN_PIN=${MAIN_PIN:-d6c5e71a5}      # <== THE ONE EDIT: cb32eda28 = fallback
OTHER_PIN=cb32eda28                  # the previous pin; the cross-window sentinel arm

export PIN=${PIN:-7}
DRY=${DRYRUN:-0}
STORE=./store; DRYARG=
if [ "$DRY" = 1 ]; then STORE=$W/dry-store; DRYARG=--dry-run; mkdir -p "$STORE"; fi
if [ -n "${END:-}" ]; then HARD_END=$END
elif [ "$DRY" = 1 ]; then HARD_END="$(date -d '+10 days' '+%Y-%m-%d %H:%M')"
else HARD_END="2026-11-24 07:55"; fi
CLOSE_RESERVE=${CLOSE_RESERVE:-1500}   # s: the closing sentinel's 25 min
echo "CHAIN_START $(date -Is) MAIN_PIN=$MAIN_PIN HARD_END='$HARD_END' PIN=$PIN MACHINE_ID=${MACHINE_ID:-<unset>} DRYRUN=$DRY" >> "$L"
abort() { echo "CHAIN_ABORT $*" >> "$L"; exit 9; }
[ -n "${MACHINE_ID:-}" ] || abort "MACHINE_ID is not set; nothing measured"
end_epoch=$(date -d "$HARD_END" +%s) || abort "unparseable HARD_END '$HARD_END'"
left() { local s=$(( end_epoch - $(date +%s) )); [ "$s" -gt 0 ] && echo "$s" || echo 0; }

# MODE: derived from the pin unless set. In fallback MAIN_PIN == OTHER_PIN: one pcrec sentinel arm, spelled
# @cb32eda28 (the pin it measures), never the same artifact twice.
if [ -z "${MODE:-}" ]; then
  if [ "$MAIN_PIN" = "$OTHER_PIN" ]; then MODE=fallback; else MODE=full; fi
fi
case "$MODE" in full|fallback) ;; *) abort "MODE '$MODE' is neither full nor fallback";; esac
if [ "$MODE" = fallback ]; then
  R_SENT="pcrec-auto@$OTHER_PIN pcre2-jit"; ALSO=""
else
  R_SENT="pcrec-auto@$OTHER_PIN pcrec-auto pcre2-jit"; ALSO=$OTHER_PIN
fi
echo "MODE=$MODE R_SENT='$R_SENT'" >> "$L"

# testee resolution (every testee named by the plan, incl. the non-pcrec engines)
python3 -m pcrecbench testees 2>>"$L" | awk '{print $1}' > "$W/testees.names"
for t in pcrec-auto pcrec-vm pcre2-jit re2-default vectorscan-block-som rust-default pcrec-auto-utf8; do
  grep -qx -- "$t" "$W/testees.names" || abort "testee '$t' does not resolve"
done
# the canonical pin in testees/pcrec/configs.toml must BE the chain's MAIN_PIN (a stale pin = a wrong window)
cfgpin=$(sed -n 's/^pin *= *"\([^"]*\)".*/\1/p' testees/pcrec/configs.toml | head -1)
if [ "$cfgpin" != "$MAIN_PIN" ]; then
  if [ "$DRY" = 1 ]; then echo "WARN(dry): configs.toml pin '$cfgpin' != MAIN_PIN '$MAIN_PIN'" >> "$L"
  else abort "testees/pcrec/configs.toml pin '$cfgpin' != MAIN_PIN '$MAIN_PIN'"; fi
fi
if [ -n "$ALSO" ] && [ "$DRY" != 1 ]; then
  grep -q "^also_pins *=.*\"$ALSO\"" testees/pcrec/configs.toml || abort "also_pins lacks $ALSO"
fi
read -r HOSTN CPUSLUG NCORES < <(python3 -c "
import platform
from pcrecbench import env
print(platform.node() or 'unknown', env.canon_cpu_model(env.cpu_model_raw()), env.cores())")
python3 -m pcrecbench machines register --store "$STORE" --machine-id "$MACHINE_ID" \
    --hostname "$HOSTN" --cpu-model "$CPUSLUG" --cores "$NCORES" \
    --first-seen "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --note "[B152] b152win_chain.sh" >> "$L" 2>&1 \
  || abort "machines register ($MACHINE_ID $HOSTN) refused"
for s in $MAIN_PIN $ALSO; do
  if [ "$DRY" = 1 ] && [ ! -x "$(sh testees/pcrec/pin.sh --path "$s")" ]; then
    echo "WARN(dry): no build of $s (rehearsal continues)" >> "$L"; continue
  fi
  sh testees/pcrec/pin.sh "$s" >> "$L" 2>&1 || abort "no build of $s"
done
for d in sentinel altwide capability syntax bounded utf8 loglines email litrun; do
  for g in gen_subjects.py gen_throughput_subjects.py; do
    [ -f bench/$d/$g ] || continue
    gnutimeout 1800 python3 bench/$d/$g >> "$L" 2>&1 || abort "bench/$d/$g failed"
  done
  [ -d bench/$d/subjects ] || abort "bench/$d/subjects missing"
done
python3 -m pcrecbench quiet --samples 5 --pin "$PIN" >> "$L" 2>&1; echo "quiet rc=$?" >> "$L"
DRV="build/work/pcrec-auto/pcrec_driver build/work/pcrec-vm/pcrec_driver"
drvsum() { for f in $DRV; do [ -f "$f" ] && sha256sum "$f"; done >> "$L" 2>&1; }
drvsum

# run_cell SET "TESTEES" EST_MIN CAP_S [skip|noskip]  -- one run_window.sh call
run_cell() {
  local set=$1 testees=$2 est=$3 cap=$4 mode=${5:-skip} t0 rc room
  if [ "$mode" = skip ]; then
    local need=$(( est * 78 + CLOSE_RESERVE ))
    if [ "$(left)" -lt "$need" ]; then
      echo "SKIPPED $set $testees (deadline) need=${need}s left=$(left)s $(date -Is)" | tee -a "$L" >> "$W/skips.log"
      return 0
    fi
    room=$(( $(left) - CLOSE_RESERVE ))   # never let the cap carry a cell into the closing reserve
  else
    room=$(left)
  fi
  [ "$cap" -gt "$room" ] && cap=$room
  [ "$cap" -gt 60 ] || { echo "SKIPPED $set $testees (deadline: cap $cap s) $(date -Is)" | tee -a "$L" >> "$W/skips.log"; return 0; }
  echo "CELL_START $set $testees est=${est}min cap=${cap}s left=$(left)s $(date -Is)" >> "$L"
  t0=$(date +%s)
  SUBBENCH=$set TESTEES="$testees" CELL_CAP=$cap STORE="$STORE" PIN=$PIN \
    LOG="$W/window_${set}_$(date -u +%Y%m%dT%H%M%SZ).log" \
    NOTE="[B152] $set x $testees at $MAIN_PIN ($MACHINE_ID)" \
    gnutimeout -k 30 $(( cap * 3 + 600 )) scripts/run_window.sh $DRYARG >> "$L" 2>&1
  rc=$?
  echo "CELL_DONE $set $testees rc=$rc $(( ($(date +%s) - t0) / 60 )) min $(date -Is)" >> "$L"
}
cap_for() { local c=$(( $1 * 120 )); [ "$c" -lt 1500 ] && c=1500; echo "$c"; }

# 1. opening sentinel (never skipped; three cells ~19 min)
run_cell sentinel "$R_SENT" 20 3600 noskip

# 2.-4. the priority list: set testee est_min
CELLS_FULL="
altwide pcrec-auto 17
altwide pcrec-vm 15
altwide re2-default 25
altwide vectorscan-block-som 25
altwide rust-default 23
capability pcrec-auto 62
syntax pcrec-auto 42
bounded pcrec-auto 47
utf8 pcrec-auto-utf8 33
loglines pcrec-auto 10
email pcrec-auto 8
litrun pcrec-auto 14
"
CELLS_FALLBACK="
altwide re2-default 25
altwide vectorscan-block-som 25
altwide rust-default 23
"
if [ "$MODE" = fallback ]; then CELLS=$CELLS_FALLBACK; else CELLS=$CELLS_FULL; fi
while read -r set testee est; do
  [ -n "$set" ] || continue
  run_cell "$set" "$testee" "$est" "$(cap_for "$est")"
done <<< "$CELLS"
echo "MAIN_TIERS_DONE $(date -Is) left=$(left)s" >> "$L"

# 5. closing sentinel -- ALWAYS, up to HARD_END (same testees as the opening)
run_cell sentinel "$R_SENT" 20 3600 noskip

# sidecars once, if time remains (run_window.sh skipped them for STORE=./store)
if [ "$DRY" != 1 ] && [ "$(left)" -gt 420 ]; then
  gnutimeout 300 python3 -m pcrecbench index --store "$STORE" >> "$L" 2>&1
  gnutimeout 300 python3 scripts/regen_sidecars.py >> "$L" 2>&1; echo "sidecars rc=$?" >> "$L"
else
  echo "sidecar regen SKIPPED (dry run or no time): the manager runs scripts/regen_sidecars.py" >> "$L"
fi
echo "WINDOW_DONE $(date -Is) skips=$(wc -l < "$W/skips.log" 2>/dev/null || echo 0)" >> "$L"
drvsum
echo "CHAIN_DONE $(date -Is)" >> "$L"
