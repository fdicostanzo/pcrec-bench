#!/bin/bash
# [B129] SAMPLED priming A/B (Frank's change of plan): `pcrecbench quick`,
# scratch tier, 10 capability@0.2 patterns (12 trimmed to fit the 20-30 min box budget) x {search (20 subjects), throughput}
# x {re2-default+rust-default, pcrec-auto}, each cell UNPRIMED (A) then PRIMED
# (B) back to back, 5 trials, pinned to core 11. Run from the worktree root:
#   setsid bash docs/dev/measurements/2026-10-09-b129-prime-sample-run.sh >/dev/null 2>&1 & disown
cd "$(dirname "$0")/../../.." || exit 2
STORE=build/scratch-store-b129s
LOG=${LOG:-build/b129-prime-sample.log}
PATS="tail-digits-eol tail-dotstar-txt tail-ext-lower-txt tail-word-eoz wild-secrets-github-pat wild-secrets-aws-access-key-id wild-datetime-moment-iso8601 email-nested-plus wild-validator-email-owasp wild-waf-crs-942140-dbnames"
echo "== b129 sample start $(date -Is) load=$(cat /proc/loadavg)" >> "$LOG"
for p in $PATS; do
  for reg in search throughput; do
    sub=""; [ "$reg" = search ] && sub="--subjects 20"
    for grp in "re2-default --vs rust-default" "pcrec-auto"; do
      for arm in A B; do
        extra=""; [ "$arm" = B ] && extra="--prime"
        echo "-- $p $reg [$grp] arm=$arm load=$(cut -d' ' -f1-3 /proc/loadavg) $(date -Is)" >> "$LOG"
        gnutimeout 600 python3 -m pcrecbench quick --subbench capability --pattern "$p" \
          --regime $reg --testee $grp --trials 5 $sub --pin 11 --store $STORE $extra >> "$LOG" 2>&1
        echo "   rc=$?" >> "$LOG"
      done
    done
  done
done
python3 -m pcrecbench index --store $STORE >> "$LOG" 2>&1
echo "DONE rc=$? $(date -Is)" >> "$LOG"
