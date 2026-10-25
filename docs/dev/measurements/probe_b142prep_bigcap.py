"""docs/dev/measurements/probe_b142prep_bigcap.py -- [B142] (lane b142prep,
2026-10-25): the census's default-cap population cannot see a REFUSAL MOVER
where the cap is raised, and the retry machine (abi 83/84: counted in the
emit size, copies the DFA tables) grows exactly the big DFAs. So: bench/altwide
(33 patterns) and bench/bounded (the whole ladder) x {plain, whole} x
{pcrec-auto-bigcap, pcrec-vm-bigcap flags: both caps 8 MiB} at 6b2dbd3e and
9ae59f5d4, pcrec's own byte counts (--warn-emit-bytes=1), refusals by name.

    python3 docs/dev/measurements/probe_b142prep_bigcap.py OUT.tsv
"""
import concurrent.futures as cf, os, re, subprocess, sys, tempfile
sys.path.insert(0, os.getcwd()); sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
from pcrecbench import subbench as _sb, record as _rec, capability as _cap   # noqa: E402
import program_identity as PI                                                   # noqa: E402
B = "/home/pcrec/projects/pcrec-bench/build"
PINS = ("6b2dbd3e", "9ae59f5d4")
CAP = ["--max-emit-bytes=8388608", "--max-emit-code-bytes=8388608"]
ROUTES = (("auto", []), ("vm", ["--engine=vm"]))
WARN = re.compile(rb"large artifact: (\d+) bytes of emitted C source \((\d+) of code\)")
OUT = sys.argv[1]


def one(job):
    sid, pid, route, rflags, form, pat = job
    cells = []
    for pin in PINS:
        with tempfile.TemporaryDirectory(dir="/var/tmp/pcrecbench/b142prep") as tmp:
            r = subprocess.run([os.path.join(B, "pcrec-%s/build/pcrec" % pin), "-p", "rx",
                                "--features", "all"] + rflags + CAP + ["--warn-emit-bytes=1",
                                "-o", os.path.join(tmp, "a.c"), "--pattern", bytes(pat)],
                               capture_output=True, timeout=900)
        if r.returncode != 0:
            why = r.stderr.decode("utf8", "replace").strip().splitlines()[-1][:90] if r.stderr else "refused"
            cells.append("REFUSED:" + why)
        else:
            m = WARN.findall(r.stderr)
            cells.append("%s:%s" % (m[-1][0].decode(), m[-1][1].decode()) if m else "?")
    return [sid, pid, route, form] + cells


def main():
    jobs = []
    for d in ("altwide", "bounded"):
        sb = _sb.find(d)
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            fs = "free-spacing" in _cap.pattern_requires(p)
            for form, t in (("plain", text), ("whole", _rec.whole_subject_text(text, fs))):
                for route, rf in ROUTES:
                    jobs.append((sb.id, p.name, route, rf, form, t))
    with cf.ThreadPoolExecutor(int(os.environ.get("B142_JOBS", "5"))) as ex:
        rows = list(ex.map(one, jobs))
    with open(OUT, "w") as fh:
        fh.write("# probe_b142prep_bigcap.py: %d rows; columns set pattern route form 6b2dbd3e 9ae59f5d4 (bytes:code | REFUSED:why)\n" % len(rows))
        for r in rows:
            fh.write("\t".join(r) + "\n")
    mov = [r for r in rows if r[4].startswith("REFUSED") != r[5].startswith("REFUSED")]
    print("rows=%d refusal movers=%d" % (len(rows), len(mov)))
    for r in mov:
        print(r)


main()
