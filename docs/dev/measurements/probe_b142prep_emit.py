"""docs/dev/measurements/probe_b142prep_emit.py -- [B142] (lane b142prep,
2026-10-25, inbox I-159): STEP 1 of the compile-only census for the re-pin
6b2dbd3e (abi 76) -> 9ae59f5d4 (abi 84). Emits every bench pattern (every
sub-bench under bench/ by ENUMERATION) x {plain, whole-subject} x
{auto-caps (`--features all`), auto-nocaps (+ `--no-captures`)} (`-e utf8` on
the utf8 set) at BOTH pins, plus the deny arms named in ARMS at the new pin,
and stores the raw emitted text (gzip) under OUTDIR. Compile-only, no gcc, no
timing. Step 2 (probe_b142prep_census.py) reads OUTDIR.

    B142_JOBS=6 python3 docs/dev/measurements/probe_b142prep_emit.py OUTDIR
"""
import concurrent.futures as cf
import gzip, hashlib, os, re, subprocess, sys, tempfile
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI                          # noqa: E402
from pcrecbench import subbench as _sb                  # noqa: E402
from pcrecbench import record as _rec                   # noqa: E402
from pcrecbench import capability as _cap               # noqa: E402
import selfcheck as _sc                                 # noqa: E402

OUT = sys.argv[1]
MAIN_BUILD = os.environ.get("B142_BUILD", "/home/pcrec/projects/pcrec-bench/build")
OLD, NEW = "6b2dbd3e", "9ae59f5d4"
BIN = {p: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % p) for p in (OLD, NEW)}
BASE = ["--features", "all"]
CONFIGS = (("caps", []), ("nocaps", ["--no-captures"]))
# deny arms at the NEW pin (name -> flag list)
ARMS = {"onewalk": ["-fno-rev-end-onewalk"]}


def population():
    jobs = []
    for setname, _path in _sc.subbench_dirs():
        sb = _sb.find(setname)
        enc = ["-e", "utf8"] if getattr(sb, "encoding", "byte") == "utf8" else []
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            fs = "free-spacing" in _cap.pattern_requires(p)
            forms = (("plain", text), ("whole", _rec.whole_subject_text(text, fs)))
            for cfg, extra in CONFIGS:
                for form, t in forms:
                    jobs.append((sb.id, p.name, cfg, form, BASE + enc + extra, t))
    return jobs


def one(job):
    sid, pid, cfg, form, flags, pat = job
    key = "%s__%s__%s__%s" % (sid.replace("@", "-"), pid, cfg, form)
    res = []
    with tempfile.TemporaryDirectory(dir=OUT) as tmp:
        for tag, pin, extra in [("old", OLD, []), ("new", NEW, [])] + \
                [("arm_" + a, NEW, f) for a, f in ARMS.items()]:
            t, sz = emit_sized(BIN[pin], flags + extra, pat, os.path.join(tmp, tag))
            if t is not None:
                with gzip.open(os.path.join(OUT, "%s.%s.gz" % (key, tag)), "wb") as fh:
                    fh.write(t.encode("utf-8", "surrogateescape"))
            res.append((tag, "%s:%s" % sz if t is not None else "0"))
    return [sid, pid, cfg, form, key] + [v for _t, v in res]


WARN = re.compile(rb"large artifact: (\d+) bytes of emitted C source \((\d+) of code\)")


def emit_sized(binary, flags, pat, workdir):
    """program_identity.emit() plus pcrec's OWN size numbers (the
    --warn-emit-bytes=1 probe, the line the caps enforce)."""
    os.makedirs(workdir, exist_ok=True)
    out = os.path.join(workdir, "a.c")
    r = subprocess.run([binary, "-p", "rx"] + list(flags) + ["--warn-emit-bytes=1", "-o", out,
                       "--pattern", bytes(pat)], capture_output=True, env=PI.C_ENV, timeout=600)
    if r.returncode != 0:
        return None, ("-", "-")
    ms = WARN.findall(r.stderr)
    sz = (ms[-1][0].decode(), ms[-1][1].decode()) if ms else ("-", "-")
    parts = []
    for p in (out, out[:-2] + ".h"):
        if os.path.exists(p):
            with open(p, "rb") as fh:
                parts.append(fh.read().decode("utf-8", "surrogateescape"))
    return PI.SEP.join(parts), sz


def main():
    os.makedirs(OUT, exist_ok=True)
    jobs = population()
    with cf.ProcessPoolExecutor(int(os.environ.get("B142_JOBS", "6"))) as ex:
        rows = list(ex.map(one, jobs, chunksize=2))
    with open(os.path.join(OUT, "index.tsv"), "w") as fh:
        fh.write("set\tpattern\tconfig\tform\tkey\told\tnew\t" + "\t".join("arm_" + a for a in ARMS) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    print("rows=%d" % len(rows))


if __name__ == "__main__":
    main()
