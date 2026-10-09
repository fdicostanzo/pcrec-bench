#!/bin/bash
# [B129] A/B/A follow-up on the three RE2 throughput cells where the sample
# showed 12-17% faster primed. Per cell and testee: A1 (unprimed), B
# (--prime), A2 (unprimed), back to back; re2-default then pcrec-auto (the
# static-code drift control). quick, scratch tier, 5 trials, core 11.
cd "$(dirname "$0")/../../.." || exit 2
STORE=build/scratch-store-b129aba
LOG=${LOG:-build/b129-prime-aba.log}
echo "== b129 aba start $(date -Is) load=$(cat /proc/loadavg)" >> "$LOG"
for p in tail-dotstar-txt tail-ext-lower-txt wild-datetime-moment-iso8601; do
  for t in re2-default pcrec-auto; do
    for arm in A1 B A2; do
      extra=""; [ "$arm" = B ] && extra="--prime"
      echo "-- $p throughput $t arm=$arm load=$(cut -d' ' -f1-3 /proc/loadavg) $(date -Is)" >> "$LOG"
      gnutimeout 600 python3 -m pcrecbench quick --subbench capability --pattern "$p" \
        --regime throughput --testee $t --trials 5 --pin 11 --store $STORE $extra >> "$LOG" 2>&1
      echo "   rc=$?" >> "$LOG"
    done
  done
done
python3 -m pcrecbench index --store $STORE >> "$LOG" 2>&1
echo "DONE rc=$? $(date -Is)" >> "$LOG"
