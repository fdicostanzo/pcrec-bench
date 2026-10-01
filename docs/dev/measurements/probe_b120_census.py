"""docs/dev/measurements/probe_b120_census.py -- [B120] (lane b120reseed,
inbox I-124) PHASE A, no timing: the compile-only census of EVERY
bench pattern under `pcrec-auto` (byte) and `pcrec-auto-utf8` (-e utf8)
at the pinned fc719ca4 (abi 50), collecting `RX_VM_RESEED` (the
[OPT-HYB-RESEED] adaptive-retry row: exact / adaptive-dense / adaptive /
clamped / fixed) and `RX_VM_FRAMELESS`, bucketed by row x frameless.

This is item 3's POPULATION: every cell stamping `adaptive*` is a
candidate for the real window ("every (set, testee) pair whose pattern
population contains an adaptive* artifact, x {auto, nohybreseed}") --
Phase B's window-cell list is derived from this file's own summary.

Compile-only, no gcc, no timing, no store write -- the SAME posture as
every prior `probe_bNNN_census.py` (b108/b118). Every sub-bench under
`bench/` by ENUMERATION (`tools/selfcheck.subbench_dirs()`, [B11.1]'s
own rule), not by name -- so `bench/utf8`'s own patterns are compiled
under BOTH configs too (the byte arm on a UTF-8-shaped pattern is a
legitimate population member: the ask is "every bench pattern", not
"every pattern under its own set's native encoding").

Run from the repo root (pin.sh must have built fc719ca4 already):

    python3 docs/dev/measurements/probe_b120_census.py OUT.tsv

Archived output: docs/dev/measurements/2026-10-01-b120-reseed-census.txt.
"""
import concurrent.futures as cf
import os, re, sys, tempfile
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI                          # noqa: E402
from pcrecbench import subbench as _sb                  # noqa: E402
import selfcheck as _sc                                 # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else "/dev/stdout"
SCRATCH = os.environ.get("B120_SCRATCH", "/var/tmp/b120scratch")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
PIN = "fc719ca4"
BIN = os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % PIN)
CAPS = ["--features", "all"]
CAPS_UTF8 = ["--features", "all", "-e", "utf8"]
CONFIGS = (("auto", CAPS), ("auto-utf8", CAPS_UTF8))
STAMPS = ("VM_RESEED", "VM_FRAMELESS", "ENGINE", "ENGINE_SEL")
STAMP_RE = re.compile(r'^#define RX_(%s) (.*)$' % "|".join(STAMPS), re.M)


def _unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        v = v[1:-1]
    return v


def population():
    jobs = []
    for setname, _path in _sc.subbench_dirs():
        sb = _sb.find(setname)
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            jobs.append((setname, p.name, text))
    return jobs


def one(job):
    setname, pid, pat = job
    rows = []
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
        for cfgname, flags in CONFIGS:
            t = PI.emit(BIN, "--pattern", flags, pat, os.path.join(tmp, cfgname))
            if t is None:
                rows.append([setname, pid, cfgname, "refused", "-", "-", "-", "-"])
                continue
            st = {k: _unquote(v) for k, v in STAMP_RE.findall(t)}
            rows.append([setname, pid, cfgname, "compiled",
                         st.get("ENGINE", "-"), st.get("ENGINE_SEL", "-"),
                         st.get("VM_RESEED", "-"), st.get("VM_FRAMELESS", "-")])
    return rows


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    if not os.path.isfile(BIN):
        sys.exit("no build for %s at %s -- run testees/pcrec/pin.sh %s first"
                  % (PIN, BIN, PIN))
    workers = int(os.environ.get("B120_JOBS", "6"))

    jobs = population()
    with cf.ProcessPoolExecutor(workers) as ex:
        results = list(ex.map(one, jobs, chunksize=4))
    rows = [r for group in results for r in group]

    hdr = ["set", "pattern_id", "config", "outcome", "engine", "engine_sel",
           "vm_reseed", "vm_frameless"]
    with open(OUT, "w") as fh:
        fh.write("\t".join(hdr) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")

    # the item-3 population: every cell whose vm_reseed starts "adaptive"
    adaptive = [r for r in rows if r[6].startswith("adaptive")]
    bucket = {}
    for r in adaptive:
        key = (r[0], r[6], r[7])
        bucket.setdefault(key, []).append(r[1])

    n_dfa = sum(1 for r in rows if r[4] == "dfa")
    n_vm = sum(1 for r in rows if r[4] == "vm")
    n_refused = sum(1 for r in rows if r[3] == "refused")
    n_reseed_vals = sorted(set(r[6] for r in rows if r[6] != "-"))
    print("rows=%d dfa=%d vm=%d refused=%d" % (len(rows), n_dfa, n_vm, n_refused))
    print("vm_reseed values seen: %s" % n_reseed_vals)
    print("adaptive* cells (item 3's population): %d" % len(adaptive))
    for (setname, row, frameless), pids in sorted(bucket.items()):
        print("  %-12s row=%-16s frameless=%s  n=%-4d %s"
              % (setname, row, frameless, len(pids),
                 ", ".join(sorted(set(pids))[:6])
                 + (" ..." if len(set(pids)) > 6 else "")))


if __name__ == "__main__":
    main()
