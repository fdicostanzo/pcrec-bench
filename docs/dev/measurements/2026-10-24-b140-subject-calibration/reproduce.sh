#!/bin/sh
# Re-run the calibration against the reference (fetch it first with bench/subst/fetch_reference.sh).
cd "$(dirname "$0")/../../../.." && exec python3 -I bench/subst/calibrate.py --out "${1:-/dev/stdout}"
