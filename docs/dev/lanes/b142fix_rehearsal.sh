#!/bin/bash
# [B142] b142fix REHEARSAL (NOT RUN by the lane): a synthetic scratch-store
# --dry-run of EVERY set the windows use, at the canonical pin 9ae59f5d4, so
# that record WRITE (store.write -> validate.py, the step that refused the
# first window's sentinel cell) happens once per set BEFORE the next real
# window. Its purpose is to catch any OTHER engine_metadata declaration gap
# (a stamp value outside a closed enum, an undeclared pair, a scope clash).
#
#     setsid bash docs/dev/lanes/b142fix_rehearsal.sh > /dev/null 2>&1 &
#
# Run from the MAIN tree after the fix is merged (or from the lane worktree
# once the manager clears the box). HEAVY (compiles every pattern of every
# set through gcc): ONE heavy suite on the box -> the manager clears it.
#
# WHAT IT RUNS: run_suite.sh --dry-run (run_window.sh --dry-run per set:
# synthetic, --force-unquiet, scratch tier, TRIALS=1, scratch store, the real
# store/ never named; refused if STORE=store). One pass per set; TESTEES per
# set = the pcrec configs the windows use at this pin:
#   email, loglines, altwide, bounded, litrun, syntax, capability, sentinel:
#       pcrec-auto pcrec-nocaps pcrec-vm   (the DFA-route compound lives on
#                                           auto/nocaps; vm covers the VM
#                                           stamps; capability and sentinel
#                                           carry the real compound witness
#                                           wild-waf-crs-942360-concat-sqli)
#   utf8:   pcrec-auto-utf8 pcrec-nocaps-utf8 pcrec-vm-utf8
#   subst:  pcrec-auto-sizefirst pcrec-vm-sizefirst   (the substitution
#           regime's testees; the plain trio has no substitution cell)
# plus the -in variants on bounded only (pcrec-vm-in, the one place windows
# use the caller-frame-buffer testee). The cross-pin arm (`pcrec-auto@6b2dbd3e`)
# is also rehearsed on capability (the part-1 window's BEFORE).
#
# PASS CRITERION (checked at the end, by name): every window log ends
# WINDOW_RUN_COMPLETE with no "validat" / "REFUSED" / "X15" line, every set's
# `rc=0` in the suite summary, and the scratch index holds >= 1 record per set.
#
# RUNTIME ESTIMATE (an ESTIMATE, not measured): compile (gcc) of every pattern
# at one trial dominates. Per-testee minutes, from the b138/b142prep books:
# sentinel 1, email 2, loglines 3, bounded 6, altwide 25, litrun 3, syntax 8,
# capability 12, utf8 12, subst 3 = ~75 min for ONE testee per set, plus
# ~15 s x cells of run_window.sh's inter-cell sleep and the bounded:vm pass
# (~6) => ONE=1 (the default): ~1.3 h. ONE=0 (the full roster, 3 testees per
# set, 2 on subst) ~3.5-4 h. ONE=1 finds a DECLARATION gap in any set (the
# declarations are per testee-FAMILY, not per config); ONE=0 only adds the
# per-config stamp VALUES of the nocaps/vm/-in variants.
cd "$(dirname "${BASH_SOURCE[0]}")/../../.." || exit 9
export LC_ALL=C
W=/var/tmp/pcrecbench/b142fix; mkdir -p "$W"
L=$W/rehearsal.log
STORE=${DRYSTORE:-/var/tmp/pcrecbench/b142fix/store}
[ "$STORE" = store ] && { echo "refusing STORE=store" >&2; exit 9; }
mkdir -p "$STORE"
ONE=${ONE:-1}
echo "REHEARSAL_START $(date -Is) STORE=$STORE ONE=$ONE" >> "$L"
abort() { echo "REHEARSAL_ABORT $*" >> "$L"; exit 9; }

TRIO="pcrec-auto pcrec-nocaps pcrec-vm"
U8="pcrec-auto-utf8 pcrec-nocaps-utf8 pcrec-vm-utf8"
SUB="pcrec-auto-sizefirst pcrec-vm-sizefirst"
first() { if [ "$ONE" = 1 ]; then echo "${1%% *}"; else echo "$1"; fi; }

python3 -m pcrecbench testees 2>>"$L" | awk '{print $1}' > "$W/testees.names"
for t in $TRIO $U8 $SUB pcrec-vm-in; do
  grep -qx -- "$t" "$W/testees.names" || abort "testee $t does not resolve"
done
sh testees/pcrec/pin.sh --path 9ae59f5d4 >> "$L" 2>&1 || abort "no build of 9ae59f5d4"
for d in sentinel email loglines altwide bounded litrun syntax capability utf8 subst; do
  for g in gen_subjects.py gen_throughput_subjects.py; do
    [ -f bench/$d/$g ] || continue
    gnutimeout 1800 python3 bench/$d/$g >> "$L" 2>&1 || abort "bench/$d/$g failed"
  done
done

# capability and sentinel keep pcrec-auto (the compound witness is a DFA
# route artifact); the cross-pin arm rides on capability.
export TESTEES_sentinel="$(first "$TRIO")" TESTEES_sentinel_end1="$(first "$TRIO")"
export TESTEES_capability="$(first "$TRIO") pcrec-auto@6b2dbd3e"
[ "$ONE" = 1 ] || TESTEES_capability="$TRIO pcrec-auto@6b2dbd3e"
export TESTEES_email="$(first "$TRIO")" TESTEES_loglines="$(first "$TRIO")"
export TESTEES_altwide="$(first "$TRIO")" TESTEES_litrun="$(first "$TRIO")"
export TESTEES_syntax="$(first "$TRIO")"
export TESTEES_bounded="$(first "$TRIO")"
[ "$ONE" = 1 ] || TESTEES_bounded="$TRIO pcrec-vm-in"
export TESTEES_utf8="$(first "$U8")" TESTEES_subst="$(first "$SUB")"
[ "$ONE" = 1 ] || TESTEES_subst="$SUB"
# the vm/vm-in/subst-vm arms add nothing a first-name pass can see on a
# DFA-first roster, so ONE=1 also adds one VM cell of the sets where VM
# stamps differ most (a second pass labelled `vm`):
SUITE="sentinel capability email loglines altwide bounded litrun syntax utf8 subst"
if [ "$ONE" = 1 ]; then
  SUITE="$SUITE bounded:vm"
  export TESTEES_bounded_vm="pcrec-vm"
fi
SENTINEL=0 SUITE="$SUITE" SUITE_LOG="$W/suite.log" STORE="$STORE" \
  NOTE="[B142] b142fix rehearsal (synthetic, scratch tier)" \
  scripts/run_suite.sh --dry-run >> "$L" 2>&1
echo "SUITE_rc=$?" >> "$L"

# ---- pass criterion, by name ----
bad=0
for s in sentinel capability email loglines altwide bounded litrun syntax utf8 subst; do
  grep -q "^-- set $s rc=0 " "$W/suite.log" || { echo "FAIL set $s: no rc=0 line" >> "$L"; bad=1; }
done
if grep -l -E "X15|not one of the declared values|REFUSED|validat.*(fail|error|reject)" build/windows/window_*_*.log 2>/dev/null | grep -q .; then
  echo "FAIL a window log names a validation refusal:" >> "$L"
  grep -h -E "X15|not one of the declared values|REFUSED" build/windows/window_*_*.log | sort | uniq -c | head -20 >> "$L"
  bad=1
fi
python3 -m pcrecbench index --store "$STORE" >> "$L" 2>&1
for s in sentinel capability email loglines altwide bounded litrun syntax utf8 subst; do
  n=$(grep -c "	$s@\|$s@" "$STORE/index.tsv" 2>/dev/null)
  [ "${n:-0}" -ge 1 ] || { echo "FAIL set $s: no record in the scratch index" >> "$L"; bad=1; }
done
echo "REHEARSAL_DONE bad=$bad $(date -Is)" >> "$L"
exit $bad
