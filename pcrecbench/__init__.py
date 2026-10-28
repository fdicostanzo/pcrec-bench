"""pcrecbench -- the pcrec-bench harness, store and reporter
(docs/design/harness_contract.md): `run`/`index`/`quiet`/`testees` from
[B3]/[B4], `report` from [B5].

`HARNESS_VERSION` is the record's `run.harness_version`; bump it when the
harness changes in a way that could change a number.
"""
HARNESS_VERSION = "0.2.0"

# The harness's own temp files (mkdtemp/mkstemp: driver subject lists, scratch
# workdirs) live under ONE root on disk, not loose in /tmp (a tmpfs shared with
# pcrec): Frank, 2026-10-28. Python-side only -- os.environ['TMPDIR'] is left
# alone, so the compilers and drivers a measured run spawns see the environment
# they always did (gcc's own temp files follow TMPDIR, and moving them would
# move compile time). `make` exports the same root for its smoke suite. An
# explicit $TMPDIR still wins. Clean up with: rm -rf /var/tmp/pcrecbench/tmp
import os as _os
import tempfile as _tempfile

TMP_ROOT = "/var/tmp/pcrecbench/tmp"
if not _os.environ.get("TMPDIR"):
    try:
        _os.makedirs(TMP_ROOT, exist_ok=True)
        _tempfile.tempdir = TMP_ROOT
    except OSError:
        pass
