#!/bin/bash
# [B136] WINDOW CHAIN (lane b136prep, 2026-10-12, NOT RUN): pcrec 6b2dbd3e
# (abi 76, canonical) against 00c97769 (abi 75, [REQ-HANDOFF-L1]) and b8337c33
# (abi 74, BASE), inbox I-147 (asks 1, 4, 7.1, 7.3; ask 6 is NOT an arm, see
# the report section 8) and I-148 section 1 (the seam movers). Launch from the
# MAIN tree AFTER the b136prep merge, detached, ONE TIER PER NIGHT:
#
#     TIERS="1" setsid bash docs/dev/lanes/b136_chain.sh > /dev/null 2>&1 &
#
# TIERS (default "1 2 3 4", run in that order; each tier is its own
# run_suite.sh call and tiers 1-3 close with their own sentinel pass, so any
# tier can be launched alone and STOP_AT_Tn caps only that tier's SETS):
#   1  ask 1 core: loglines, altwide, bounded x BASE / NEW / DENY (+ canonical
#      on loglines, altwide)                             ~356 min (5.9 h)
#   2  ask 4 (litrun same-pin -fno-rev-end, caps+nocaps) + the tail-family /
#      grok cross-window control (capability BASE / NEW / canonical)
#                                                        ~240 min (4.0 h)
#   3  the other I-147 section 1 mover sets as smoke + I-148's seam movers:
#      syntax, utf8 x BASE / NEW / DENY / canonical      ~361 min (6.0 h)
#   4  ask 7.1: pcre2-jit + pcre2-interp (+ the -utf pair on utf8) at current
#      versions on bounded, loglines, syntax, utf8, litrun, email
#                                                        ~279 min (4.7 h)
#   TOTAL ~1236 min = 20.6 h (the cell-length table is in the report).
#
# Completion: /var/tmp/b136win/chain.log ends `CHAIN_DONE`; each tier logs
# `TIERn_DONE suite_rc=<rc>`; the suite log (build/windows/suite_*.log) ends
# SUITE_RUN_COMPLETE with a `set <name> rc=0 <min> min` line per set; each
# set's window log ends `WINDOW_RUN_COMPLETE cells=N/N`. `rc=4`
# (inconclusive-spread) cells are re-measured once by run_window.sh.
#
# Entries `testee@pin` run that config at an also_pin (configs.toml): `@b8337c33`
# = BASE, `@00c97769` = NEW (L1), a bare entry = the canonical pin 6b2dbd3e.
# Do NOT set PIN (that is the CPU core) nor PCRECBENCH_PCREC_PIN
# (run_window.sh sets it per `testee@pin` cell). The deny arm
# `pcrec-auto-noreqhandoff@00c97769` is the NO-handoff artifact, not
# main-before-L1 (it also removes K82's entry handoff: I-147 section 1).
# ONE driver build serves every pin; sha256 check below.
cd /home/duxevents/pcrec-bench || exit 9
W=/var/tmp/b136win; mkdir -p $W
L=$W/chain.log
echo "CHAIN_START $(date -Is) TIERS=${TIERS:-1 2 3 4}" >> $L
# --- preconditions (a failure here aborts: nothing has been measured) ---
for s in b8337c33 00c97769 6b2dbd3e; do
  sh testees/pcrec/pin.sh --path $s >> $L 2>&1 || { echo "CHAIN_ABORT no build of $s" >> $L; exit 9; }
done
python3 bench/sentinel/gen_subjects.py >> $L 2>&1; echo "gen_sentinel rc=$?" >> $L
for d in altwide bounded syntax utf8 loglines litrun email capability; do
  [ -d bench/$d/subjects ] || echo "WARN bench/$d/subjects missing (run bench/$d/gen_subjects.py)" >> $L
done
python3 -m pcrecbench quiet --samples 5 >> $L 2>&1; echo "quiet rc=$?" >> $L
# one driver build for every entry: this hash must be equal across pcrec
# workdirs and unchanged between the first sentinel cell and the end.
sha256sum build/work/pcrec-auto/pcrec_driver build/work/pcrec-nocaps/pcrec_driver >> $L 2>&1

B=b8337c33; N=00c97769                       # BASE, NEW (the canonical pin is bare)
ABCD="pcrec-auto@$B pcrec-auto@$N pcrec-auto-noreqhandoff@$N pcrec-auto"      # BASE NEW DENY canon
ABD="pcrec-auto@$B pcrec-auto@$N pcrec-auto-noreqhandoff@$N"                   # BASE NEW DENY
UCD="pcrec-auto-utf8@$B pcrec-auto-utf8@$N pcrec-auto-utf8-noreqhandoff@$N pcrec-auto-utf8"
SENT_OPEN="pcrec-auto@$B pcrec-auto@$N pcrec-auto pcrec-nocaps pcre2-jit"
SENT_CLOSE="pcrec-auto pcrec-auto@$N pcrec-auto@$B pcrec-nocaps pcre2-jit"

tier() { case " ${TIERS:-1 2 3 4} " in *" $1 "*) return 0;; esac; return 1; }

# ---- TIER 1 (~356 min): I-147 ask 1 -- BASE vs NEW vs deny, and ask 7.3
# (altwide@0.3 at the post-L1 pin = the NEW + canonical cells). loglines holds
# ipv6/ipv4/kv-quoted, bounded dotted4, altwide sfx-64/256/512. The set runs
# WHOLE (no per-pattern filter on `run`). Opening sentinel is auto-prepended.
if tier 1; then
  SUITE="sentinel loglines altwide bounded sentinel:end1" \
  TESTEES_sentinel="$SENT_OPEN" TESTEES_sentinel_end1="$SENT_CLOSE" \
  TESTEES_loglines="$ABCD" TESTEES_altwide="$ABCD" TESTEES_bounded="$ABD" \
  STOP_AT="${STOP_AT_T1:-}" \
  NOTE="[B136] tier 1: I-147 ask 1 (BASE b8337c33 / NEW 00c97769 / deny -fno-req-handoff) + 7.3 altwide@0.3" \
  scripts/run_suite.sh >> $L 2>&1
  echo "TIER1_DONE suite_rc=$? $(date -Is)" >> $L
fi
# ---- TIER 2 (~240 min): ask 4 -- the same-pin -fno-rev-end arm on litrun at
# the canonical pin (caps + nocaps; I-147 section 4: is O-96's +2..8% the box
# or the pin?), and I-147 ask 4 / I-145's tail family + grok cross-window
# control (capability: none should move at 00c97769). SENTINEL=0: tier 1
# opened the window; this tier closes with its own pass.
if tier 2; then
  SENTINEL=0 SUITE="litrun capability sentinel:end2" \
  TESTEES_litrun="pcrec-auto pcrec-auto-norevend pcrec-nocaps pcrec-nocaps-norevend" \
  TESTEES_capability="pcrec-auto@$B pcrec-auto@$N pcrec-auto" \
  TESTEES_sentinel_end2="$SENT_CLOSE" STOP_AT="${STOP_AT_T2:-}" \
  NOTE="[B136] tier 2: ask 4 same-pin -fno-rev-end on litrun + tail/grok cross-window control (capability)" \
  scripts/run_suite.sh >> $L 2>&1
  echo "TIER2_DONE suite_rc=$? $(date -Is)" >> $L
fi
# ---- TIER 3 (~361 min): the other section-1 mover sets as smoke (syntax: the
# five syntax movers; utf8: ci-ascii-control, ci-strasse -- ci-strasse gates
# pcrec's T5 work) + I-148 section 1's seam movers (syntax bak-1 ~+13.5%,
# bak-2 ~+9.7%, mod-j-uc ~+5.6%: the canonical vs NEW cells). utf8 runs the
# -utf8 siblings.
if tier 3; then
  SENTINEL=0 SUITE="syntax utf8 sentinel:end3" \
  TESTEES_syntax="$ABCD" TESTEES_utf8="$UCD" TESTEES_sentinel_end3="$SENT_CLOSE" \
  STOP_AT="${STOP_AT_T3:-}" \
  NOTE="[B136] tier 3: syntax/utf8 movers smoke + I-148 seam movers (6b2dbd3e vs 00c97769)" \
  scripts/run_suite.sh >> $L 2>&1
  echo "TIER3_DONE suite_rc=$? $(date -Is)" >> $L
fi
# ---- TIER 4 (~279 min): I-147 ask 7.1 -- same-window peers at current
# versions (jit + interp; the -utf pair for utf8), so the September peers stop
# being the comparison. No pcrec entry: the closing instrument control is the
# preceding tier's sentinel; the pcre2-jit sentinel row (ask 7.4, optional)
# is already in every sentinel pass above.
if tier 4; then
  SENTINEL=0 SUITE="bounded loglines syntax utf8 litrun email" \
  TESTEES_bounded="pcre2-jit pcre2-interp" TESTEES_loglines="pcre2-jit pcre2-interp" \
  TESTEES_syntax="pcre2-jit pcre2-interp" TESTEES_litrun="pcre2-jit pcre2-interp" \
  TESTEES_email="pcre2-jit pcre2-interp" TESTEES_utf8="pcre2-utf-jit pcre2-utf-interp" \
  STOP_AT="${STOP_AT_T4:-}" \
  NOTE="[B136] tier 4: ask 7.1 same-window pcre2 peers at current versions" \
  scripts/run_suite.sh >> $L 2>&1
  echo "TIER4_DONE suite_rc=$? $(date -Is)" >> $L
fi
sha256sum build/work/pcrec-auto/pcrec_driver build/work/pcrec-nocaps/pcrec_driver >> $L 2>&1
echo "CHAIN_DONE $(date -Is)" >> $L
