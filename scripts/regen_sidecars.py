#!/usr/bin/env python3
"""scripts/regen_sidecars.py -- regenerate every committed
`reports/*.interpretation.md` sidecar, called from `scripts/
run_window.sh`'s close ([B41] (a)).

WHY THIS EXISTS. A committed sidecar is stamped against `store/
index.tsv` AS IT STOOD when the sidecar was generated (interpreter_v1.md
Q5: R-STATUS-2 and friends read the LIVE index by design). A window that
writes new records therefore leaves every committed sidecar STALE, and
`make check-interpret` section 3 -- which re-renders each one from its
own stamp and requires byte equality -- FAILS until they are
regenerated. Before this script existed that regeneration was a manual
step (the `/pcrec-bench-interpret` skill, run by hand, once per sidecar)
that a window closing script never reached for.

WHAT IT DOES, and nothing else. For every `reports/*.interpretation.md`
already committed, it reads that file's OWN stamp (the same six lines
`catalogue/check_interpret.py`'s section 3 already parses) to recover
the `report`, `index` and `predictions` paths the sidecar was generated
against -- so this script never re-derives the report<->predictions
match itself (that matching logic lives in exactly one place, the
`/pcrec-bench-interpret` skill's step 2, `.claude/skills/
pcrec-bench-interpret/SKILL.md`); it only re-runs the SAME inputs a
fresh index can move the answer for. For each one it runs the EXACT
invocation the skill documents (step 3), from the repository root, with
repo-relative paths:

    python3 -m pcrecbench interpret <report> --index <index> \\
        [--predictions <predictions>] --render --out <sidecar>

then re-runs the same command WITHOUT --out (to stdout) and byte-compares
it against the file just written -- the skill's own step 4 determinism
check. A mismatch here means `interpret` itself is non-deterministic,
exactly as the skill's own wording says, and is reported as a FAILURE,
never "fixed" by trusting either byte string over the other.

FAILS LOUDLY, NEVER SILENTLY. Any of: the report a stamp names no longer
exists, the report's sha256 no longer matches the stamp (the check
`interpret`'s own determinism run would fail on anyway), `interpret`
itself exiting non-zero, or a determinism mismatch -- is printed by name
and counted as a failure; this script's own exit code is the number of
sidecars that did not regenerate cleanly (0 = every sidecar is fresh or
was refreshed cleanly). One broken sidecar does not stop the others from
being attempted -- same principle as `run_suite.sh`'s "one broken set
must not lose the night", scaled down to one window's closing step.

Run from anywhere; it resolves the repository root itself and does
everything from there, per the skill's own instruction ("run every
command from the repository root").
"""
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORTS = os.path.join(ROOT, "reports")

_STAMP_LINE = re.compile(r"^([a-z_0-9]+):\s+(.*)$")


def parse_stamp(text):
    """The same stamp grammar `catalogue/check_interpret.py`'s section 3
    reads: `key:  value` lines between the opening HTML comment and its
    closing `-->`."""
    stamp = {}
    for ln in text.split("\n"):
        if ln.startswith("-->"):
            break
        m = _STAMP_LINE.match(ln)
        if m:
            stamp[m.group(1)] = m.group(2).strip()
    return stamp


def regen_one(sidecar_name):
    """Returns (ok, message)."""
    sidecar_path = os.path.join(REPORTS, sidecar_name)
    with open(sidecar_path, encoding="utf-8") as fh:
        old_text = fh.read()
    stamp = parse_stamp(old_text)

    report_rel = stamp.get("report")
    if not report_rel:
        return False, f"{sidecar_name}: no `report:` line in its own stamp"
    report_abs = os.path.join(ROOT, report_rel)
    if not os.path.exists(report_abs):
        return False, (f"{sidecar_name}: its stamped report is missing: "
                        f"{report_rel}")

    index_rel = stamp.get("index")
    index_rel = index_rel if index_rel and index_rel != "(none)" else "store/index.tsv"
    pred_rel = stamp.get("predictions")
    pred_rel = pred_rel if pred_rel and pred_rel != "(none)" else None

    out_rel = os.path.join("reports", sidecar_name)
    base_cmd = [sys.executable, "-m", "pcrecbench", "interpret", report_rel,
                "--index", index_rel]
    if pred_rel:
        base_cmd += ["--predictions", pred_rel]

    # Step 3 (the skill): render straight to the committed path.
    rc = subprocess.call(base_cmd + ["--render", "--out", out_rel], cwd=ROOT)
    if rc != 0:
        return False, (f"{sidecar_name}: `pcrecbench interpret --render` "
                        f"exited {rc}")

    # Step 4 (the skill): re-run to STDOUT and byte-compare -- the
    # determinism check. A mismatch is `interpret` itself misbehaving,
    # never something this script "fixes" by preferring one side.
    proc = subprocess.run(base_cmd + ["--render"], cwd=ROOT,
                          capture_output=True, text=True)
    if proc.returncode != 0:
        return False, (f"{sidecar_name}: the determinism re-run exited "
                        f"{proc.returncode}: {proc.stderr.strip()[:200]}")
    with open(sidecar_path, encoding="utf-8") as fh:
        written = fh.read()
    if proc.stdout != written:
        return False, (f"{sidecar_name}: NON-DETERMINISTIC -- the "
                        f"--out render and the stdout render of the SAME "
                        f"command disagree")

    changed = written != old_text
    return True, (f"{sidecar_name}: regenerated, CHANGED"
                  if changed else f"{sidecar_name}: fresh, unchanged")


def main():
    if not os.path.isdir(REPORTS):
        print(f"regen_sidecars: no {REPORTS} directory", file=sys.stderr)
        return 1
    names = sorted(n for n in os.listdir(REPORTS)
                   if n.endswith(".interpretation.md"))
    if not names:
        print("regen_sidecars: no committed reports/*.interpretation.md "
              "sidecars -- nothing to do")
        return 0

    failures = 0
    for name in names:
        try:
            ok, msg = regen_one(name)
        except Exception as exc:  # noqa: BLE001 -- name it, never swallow it
            ok, msg = False, f"{name}: {type(exc).__name__}: {exc}"
        print(("OK  " if ok else "FAIL") + " " + msg)
        if not ok:
            failures += 1

    print(f"regen_sidecars: {len(names)} sidecar(s), {failures} failure(s)")
    return failures


if __name__ == "__main__":
    sys.exit(main())
