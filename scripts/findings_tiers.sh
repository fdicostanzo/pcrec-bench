#!/bin/bash
# scripts/findings_tiers.sh -- [B115] FINDINGS-BENCH-TIERS's four-column
# scratch-tier sweep (inbox I-118, outbox O-72). Loops
# `pcrecbench run --tier scratch --testee pcrec-local` per (set, arm) with
# $PCREC_BIN / $PCREC_LOCAL_FLAGS set to a scratch-tier pcrec build at
# commit f7f5a143 (abi 44, post-[FINDINGS] B6) -- NEVER this project's
# pinned commit (configs.toml's a32bc86e, abi 41, which has no
# `--analysis`/`-I`/`pcrec-analyze` at all). Nothing here touches
# configs.toml, store/, or any pinned testee.
#
# THE ARMS, per set (outbox O-72 Q3):
#
#   default                     no --tune, no --analysis, no -I
#   eng-<E>-tune-<T>[-nocaps]   engine {auto,vm,dfa} x tune {-2..2}, and
#                               --no-captures crossed in ONLY on a
#                               CAPTURE-FREE set (CAPTURE_FREE_SETS below;
#                               loglines/bounded/altwide are, email is not
#                               -- team's own check, viewer_export.py's
#                               _pattern_capture_count over every set's
#                               patterns/*.rx)
#   declared-<name>             loglines only: weblog, log
#   profiled                    loglines/email only: -I the set's own
#                               testees/pcrec/findings/<set>/ dir,
#                               --analysis <the set's PROFILED bundle name>
#
# bounded/altwide/capability/syntax get `default` + the engine x tune
# sweep ONLY (no DECLARED, no PROFILED -- outbox O-72's own scoping) and
# are OFF by default: pass --extended to add them.
#
# ENV-OVERRIDABLE:
#   SETS          "loglines email"      -- --extended appends the four more
#   PIN           11                    -- the CPU core (as run_window.sh)
#   TRIALS        5
#   CELL_CAP      5400                  -- seconds, run_window.sh's shape
#   STORE         /var/tmp/b115/store   -- MUST NOT be the canonical store;
#                                          refused by name if it is
#   B115_BIN      resolved via `testees/pcrec/pin.sh --path f7f5a143`
#                 (built by [B115] part (a); this script never builds it)
#   NOTE          "[B115] findings-tiers sweep, $(date -Is)"
#   LOG           build/windows/findings_tiers_$(date +%Y%m%dT%H%M%SZ).log
#   ITERS         (unset)  -- `--iters N` on every `run` (smoke: `ITERS=1`,
#                 never a measurement)
#   EXTRA         (unset)  -- extra flags appended to every `run`
#                 (smoke: `EXTRA=--force-unquiet`)
#   ARM_FILTER    (unset)  -- a space-separated label subset per set (e.g.
#                 `ARM_FILTER="default profiled"`), for a smoke run over a
#                 2-3 arm slice instead of the whole product
#
# --dry-run: prints every arm's PCREC_LOCAL_FLAGS and its DERIVED
#   testee_id (through the real adapter, `pcrec.describe()` -- no compile,
#   no pcrec exec at all) and exits. Use this to review the arm list
#   before spending any CPU.
# --extended: adds bounded, altwide, capability, syntax to $SETS (their
#   own default $SETS value is NOT overridden if the caller already set
#   one -- same precedence rule run_window.sh's TESTEES has).
set -u
export LC_ALL=C

REPO=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd) || exit 9
cd "$REPO" || exit 9

_sets_was_set=${SETS+x}
SETS=${SETS:-"loglines email"}
PIN=${PIN:-11}
TRIALS=${TRIALS:-5}
CELL_CAP=${CELL_CAP:-5400}
STORE=${STORE:-/var/tmp/b115/store}
NOTE=${NOTE:-"[B115] findings-tiers sweep, $(date -Is)"}
ITERS=${ITERS:-}                 # smoke-only: `--iters 1` (never a measurement)
EXTRA=${EXTRA:-}                 # extra flags appended to every `run` (e.g. --force-unquiet)
ARM_FILTER=${ARM_FILTER:-}       # smoke-only: space-separated label subset (e.g. "default profiled")
DRY_RUN=0
EXTENDED=0

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --extended) EXTENDED=1 ;;
    *) echo "findings_tiers.sh: unrecognized argument: $arg" >&2; exit 2 ;;
  esac
done

if [ "$EXTENDED" -eq 1 ] && [ -z "$_sets_was_set" ]; then
  SETS="$SETS bounded altwide capability syntax"
fi

if [ "$STORE" = "store" ]; then
  echo "findings_tiers.sh: refusing to sweep into the canonical store/ -- this is a SCRATCH-TIER sweep by construction" >&2
  exit 9
fi

B115_BIN=${B115_BIN:-}
if [ -z "$B115_BIN" ]; then
  B115_BIN=$(testees/pcrec/pin.sh --path f7f5a143)
fi
if [ ! -x "$B115_BIN" ]; then
  echo "findings_tiers.sh: $B115_BIN is not built -- run 'testees/pcrec/pin.sh f7f5a143' first ([B115] part (a); this is a scratch-tier commit, never a re-pin of configs.toml)" >&2
  exit 9
fi

LOG=${LOG:-build/windows/findings_tiers_$(date -u +%Y%m%dT%H%M%SZ).log}
mkdir -p "$(dirname "$LOG")" || exit 9

#: sets whose patterns are ALL capture-free (viewer_export.py's
#: _pattern_capture_count over every bench/<set>/patterns/*.rx, 2026-09-28
#: census: loglines 0/11, bounded 0/43, altwide 0/33; email 1/3,
#: capability 28/64, syntax 18/95 are NOT).
CAPTURE_FREE_SETS="loglines bounded altwide"

#: sets that get the full DECLARED/PROFILED treatment beyond DEFAULT +
#: the engine x tune sweep.
DECLARED_SETS="loglines"
PROFILED_SETS="loglines email"

is_capture_free() {
  case " $CAPTURE_FREE_SETS " in *" $1 "*) return 0 ;; *) return 1 ;; esac
}

#: findings_analysis_name(set) -- the PROFILED bundle name testees/pcrec/
#: findings/<set>/ holds, or empty for a set with none.
profiled_bundle() {
  case "$1" in
    loglines) echo "loglines-profiled" ;;
    email) echo "email-prose-profiled" ;;
    *) echo "" ;;
  esac
}

# arm_list SET -- prints one "label\tPCREC_LOCAL_FLAGS" per line (tab-
# separated; flags may be empty for `default`).
arm_list() {
  local set="$1"
  printf 'default\t\n'
  local engine tune capsuffix
  for engine in auto vm dfa; do
    for tune in -2 -1 0 1 2; do
      printf 'eng-%s-tune-%s\t--engine=%s --tune=%s\n' \
        "$engine" "${tune/-/m}" "$engine" "$tune"
      if is_capture_free "$set"; then
        printf 'eng-%s-tune-%s-nocaps\t--engine=%s --tune=%s --no-captures\n' \
          "$engine" "${tune/-/m}" "$engine" "$tune"
      fi
    done
  done
  case " $DECLARED_SETS " in
    *" $set "*)
      printf 'declared-weblog\t-I testees/pcrec/findings/%s --analysis weblog\n' "$set"
      printf 'declared-log\t-I testees/pcrec/findings/%s --analysis log\n' "$set"
      ;;
  esac
  case " $PROFILED_SETS " in
    *" $set "*)
      bundle=$(profiled_bundle "$set")
      printf 'profiled\t-I testees/pcrec/findings/%s --analysis %s\n' "$set" "$bundle"
      ;;
  esac
}

echo "== findings_tiers.sh start $(date -Is) sets='$SETS' store=$STORE b115_bin=$B115_BIN dry_run=$DRY_RUN cell_cap=${CELL_CAP}s load=$(cat /proc/loadavg)" | tee -a "$LOG"

export PCREC_BIN="$B115_BIN"

cells_attempted=0
cells_written=0
for set in $SETS; do
  # bounded/altwide/capability/syntax under --extended get ONLY default +
  # the engine x tune sweep -- arm_list already omits DECLARED/PROFILED
  # for them (neither is in $DECLARED_SETS/$PROFILED_SETS), so no extra
  # filtering is needed here.
  while IFS=$'\t' read -r label flags; do
    if [ -n "$ARM_FILTER" ]; then
      case " $ARM_FILTER " in
        *" $label "*) : ;;
        *) continue ;;
      esac
    fi
    export PCREC_LOCAL_FLAGS="$flags"
    if [ "$DRY_RUN" -eq 1 ]; then
      tid=$(python3 -c "
import sys
sys.path.insert(0, '.')
from pcrecbench import adapters as _ad
eng = _ad.discover()['pcrec']
block = eng.describe('pcrec-local', '/tmp')
from pcrecbench import record as _rec
print(_rec.derive_testee_id(block))
" 2>&1)
      printf '%-8s %-24s PCREC_LOCAL_FLAGS=%-60s -> %s\n' "$set" "$label" "$flags" "$tid" | tee -a "$LOG"
      continue
    fi
    echo "-- cell $set x $label $(date -Is) flags='$flags' load=$(cut -d' ' -f1-3 /proc/loadavg)" | tee -a "$LOG"
    cells_attempted=$((cells_attempted + 1))
    gnutimeout "$CELL_CAP" python3 -m pcrecbench run --subbench "$set" --testee pcrec-local \
        --tier scratch --trials "$TRIALS" --pin "$PIN" --subject-timeout 60 --driver-timeout 900 \
        --store "$STORE" ${ITERS:+--iters "$ITERS"} $EXTRA \
        --note "$NOTE (arm=$label)" >> "$LOG" 2>&1
    rc=$?
    echo "   rc=$rc cell_cap=${CELL_CAP}s $(date -Is)" | tee -a "$LOG"
    if [ "$rc" -eq 0 ]; then
      cells_written=$((cells_written + 1))
    elif [ "$rc" -eq 124 ]; then
      echo "   KILLED by the per-cell cap of ${CELL_CAP}s -- no record was written" | tee -a "$LOG"
    fi
  done < <(arm_list "$set")
done

if [ "$DRY_RUN" -eq 1 ]; then
  echo "== findings_tiers.sh --dry-run end $(date -Is)" | tee -a "$LOG"
  exit 0
fi

gnutimeout 120 python3 -m pcrecbench index --store "$STORE" 2>&1 | tail -3 | tee -a "$LOG"

echo "== findings_tiers.sh end $(date -Is) load=$(cat /proc/loadavg)" | tee -a "$LOG"
echo "FINDINGS_TIERS_COMPLETE cells=$cells_written/$cells_attempted" >> "$LOG"
if [ "$cells_written" -eq 0 ] && [ "$cells_attempted" -gt 0 ]; then
  exit 5
fi
exit 0
