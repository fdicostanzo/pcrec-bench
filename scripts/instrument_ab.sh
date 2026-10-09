#!/bin/bash
# scripts/instrument_ab.sh -- INSTRUMENT A/B/A/B at ONE pin ([B133]): time the
# driver as of git revision BEFORE_REV against the driver in THIS tree, same
# pcrec pin (both trees read testees/pcrec/configs.toml's pin), same cells,
# interleaved BEFORE1 AFTER1 BEFORE2 AFTER2 per cell, scratch tier, one core.
# It quantifies an INSTRUMENT step (BD16) before records carry it, and is the
# RE-PIN CONTROL (testees/pcrec/CLAUDE.md): run it at every re-pin with
# BEFORE_REV = the driver revision of the previous pin and a winpath-style
# cell. Heavy (a quiet box, ONE heavy job at a time -- BD3): launch detached,
#   setsid scripts/instrument_ab.sh REV OUTDIR [CELLS_FILE] > /dev/null 2>&1 &
# and read the marker `DONE rc=` at the end of OUTDIR/run.log.
#
#   usage: instrument_ab.sh BEFORE_REV OUTDIR [CELLS_FILE]
#   CELLS_FILE  lines `testee:pattern` (default scripts/instrument_cells.txt);
#               sub-bench is capability unless SUBBENCH is set
#   TRIALS (5), PIN (11), SUBBENCH (capability), REGIME (search)
# Analysis: docs/dev/measurements/2026-10-09-b133-instrument-ab-analysis.py OUTDIR
set -u
export LC_ALL=C
REPO=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd) || exit 9
REV=${1:?BEFORE_REV}; OUT=$(realpath -m "${2:?OUTDIR}")
CELLS_FILE=${3:-$REPO/scripts/instrument_cells.txt}
TRIALS=${TRIALS:-5}; PIN=${PIN:-11}; SUBBENCH=${SUBBENCH:-capability}; REGIME=${REGIME:-search}
mkdir -p "$OUT"; LOG=$OUT/run.log
BEFORE_TREE=$OUT/before-tree
echo "== instrument A/B start $(date -Is) rev=$REV load=$(cat /proc/loadavg) cells=$CELLS_FILE" >> "$LOG"
if [ ! -d "$BEFORE_TREE" ]; then
  git -C "$REPO" worktree add --detach "$BEFORE_TREE" "$REV" >> "$LOG" 2>&1 || { echo "DONE rc=9 (worktree)" >> "$LOG"; exit 9; }
  # generated, gitignored subject trees: link the main tree's
  MAIN=$(dirname "$(git -C "$REPO" rev-parse --path-format=absolute --git-common-dir)")
  for d in "$REPO"/bench/*/; do n=$(basename "$d")
    for t in subjects throughput; do
      src=$REPO/bench/$n/$t; [ -e "$src" ] || src=$MAIN/bench/$n/$t
      [ -e "$src" ] && [ ! -e "$BEFORE_TREE/bench/$n/$t" ] && ln -s "$(realpath "$src")" "$BEFORE_TREE/bench/$n/$t"
    done
  done
fi
rc=0
while read -r c; do
  [ -z "$c" ] && continue; case "$c" in \#*) continue;; esac
  t=${c%%:*}; p=${c#*:}
  for step in BEFORE1 AFTER1 BEFORE2 AFTER2; do
    case $step in BEFORE*) tree=$BEFORE_TREE;; *) tree=$REPO;; esac
    echo "-- $t $p $step load=$(cut -d' ' -f1-3 /proc/loadavg) $(date -Is)" >> "$LOG"
    ( cd "$tree" && gnutimeout 600 nice python3 -m pcrecbench quick --subbench "$SUBBENCH" --pattern "$p" \
        --regime "$REGIME" --testee "$t" --trials "$TRIALS" --pin "$PIN" --store "$OUT/store-$step" ) >> "$LOG" 2>&1
    r=$?; echo "   rc=$r" >> "$LOG"; [ $r -ne 0 ] && rc=1
  done
done < "$CELLS_FILE"
git -C "$REPO" worktree remove --force "$BEFORE_TREE" >> "$LOG" 2>&1
echo "DONE rc=$rc $(date -Is)" >> "$LOG"
exit $rc
