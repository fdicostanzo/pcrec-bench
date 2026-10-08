"""docs/dev/measurements/probe_b126_r4h_text_identity.py -- [B126] (lane
b126prep, 2026-10-08): pcrec I-135's claim that abi 67 ([MEMFN] R4h layout
normalization) is "OBJECT-IDENTICAL in executed code", MEASURED on a sample.

Takes the census TSV (probe_b126_census.py), selects rows whose v2 hash moved
at step 67 ONLY, takes every STRIDE-th, and for each compiles the 60366d747
and 255bcdd8 artifacts with gcc -O2 -c and compares the `.text` section
(objcopy -O binary -j .text). Run from a worktree root:

    STRIDE=5 python3 docs/dev/measurements/probe_b126_r4h_text_identity.py CENSUS.tsv OUT.tsv
"""
import concurrent.futures as cf, hashlib, os, subprocess, sys, tempfile
sys.path.insert(0, os.getcwd()); sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import probe_b126_census as C                            # noqa: E402
OLD, NEW = C.OLD, C.NEW


def text_hash(binary, flags, pat, tmp, tag):
    out = os.path.join(tmp, tag + ".c")
    r = subprocess.run([binary, "-p", "rx"] + flags + ["-o", out, "--pattern", bytes(pat)],
                       capture_output=True)
    if r.returncode:
        return None
    obj = os.path.join(tmp, tag + ".o")
    if subprocess.run(["gcc", "-O2", "-c", out, "-o", obj], capture_output=True).returncode:
        return None
    raw = os.path.join(tmp, tag + ".t")
    subprocess.run(["objcopy", "-O", "binary", "-j", ".text", obj, raw], capture_output=True)
    return hashlib.sha256(open(raw, "rb").read()).hexdigest()[:16]


def one(job):
    sid, pid, cfg, form, flags, pat = job
    with tempfile.TemporaryDirectory(dir=C.SCRATCH) as tmp:
        a = text_hash(C.BINS[OLD], flags, pat, tmp, "o")
        b = text_hash(C.BINS[NEW], flags, pat, tmp, "n")
    return [sid, pid, cfg, form, a or "-", b or "-", "same" if a and a == b else "DIFFERENT"]


def main():
    census, out = sys.argv[1], sys.argv[2]
    stride = int(os.environ.get("STRIDE", "5"))
    want = []
    for ln in open(census):
        c = ln.rstrip("\n").split("\t")
        if len(c) > 6 and c[5] == "67" and c[4] == "changed":
            want.append(tuple(c[:4]))
    want = set(want[::stride])
    os.makedirs(C.SCRATCH, exist_ok=True)
    jobs = [j for j in C.population() if (j[0], j[1], j[2], j[3]) in want]
    with cf.ProcessPoolExecutor(int(os.environ.get("JOBS", "4"))) as ex:
        rows = list(ex.map(one, jobs))
    with open(out, "w") as fh:
        fh.write("set\tpattern_id\tconfig\tform\ttext_old\ttext_new\tverdict\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    from collections import Counter
    print(len(rows), dict(Counter(r[6] for r in rows)))


if __name__ == "__main__":
    main()
