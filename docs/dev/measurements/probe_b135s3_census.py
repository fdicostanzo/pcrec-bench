"""docs/dev/measurements/probe_b135s3_census.py -- [B135] (lane b135s3,
2026-10-10, inbox I-145): the COMPILE-ONLY census for the re-pin 7388f1c0
(abi 73) -> b8337c33 (abi 74, [START-LANDING]).

POPULATION: every pattern of every sub-bench under `bench/` by ENUMERATION x
{plain, whole-subject} x {auto-caps (`--features all`), auto-nocaps
(+ `--no-captures`)} (`-e utf8` on the utf8 set). v2 program identity
(`tools/program_identity.py`). I-145's "734 compiles (default + nocaps)" is
367 patterns x PLAIN form x {caps, nocaps}; the whole-subject form is
reported beside it and never mixed in.

Per row: the verdict at b8337c33 against 7388f1c0 (identical / changed /
refusal-mover / refused-both), the stamps (DFA_START, DFA_SCAN, DFA_MATCH,
ENGINE_SEL, DFA_PREFILTER) on both sides, the emitted-text bytes, and four
denials AT the pin, each compared to 7388f1c0's v2 identity: `dw`
(-fno-start-width), `dl` (-fno-start-landing), `dwl` (both),
`dwlp` (both + -fno-start-pinned). A denial cell reads `same` (v2 equal to
the default at the pin: the flag cannot act), `to-S73` (equal to 7388f1c0's),
`differs` or `refused`.

    B135S3_JOBS=4 python3 docs/dev/measurements/probe_b135s3_census.py OUT.tsv
"""
import concurrent.futures as cf
import os, re, sys, tempfile
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI                          # noqa: E402
from pcrecbench import subbench as _sb                  # noqa: E402
from pcrecbench import record as _rec                   # noqa: E402
from pcrecbench import capability as _cap               # noqa: E402
import selfcheck as _sc                                 # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else "/dev/stdout"
SCRATCH = os.environ.get("B135S3_SCRATCH", "/var/tmp/b135s3/census")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
OLD, NEW = "7388f1c0", "b8337c33"
BINS = {p: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % p) for p in (OLD, NEW)}
BASE = ["--features", "all"]
CONFIGS = (("caps", []), ("nocaps", ["--no-captures"]))
DENIES = (("dw", ["-fno-start-width"]), ("dl", ["-fno-start-landing"]),
          ("dwl", ["-fno-start-width", "-fno-start-landing"]),
          ("dwlp", ["-fno-start-width", "-fno-start-landing",
                    "-fno-start-pinned"]))
STAMPS = ("ENGINE", "ENGINE_SEL", "DFA_SCAN", "DFA_START", "DFA_MATCH",
          "DFA_PREFILTER", "REQ_WHY")
STAMP_RE = re.compile(r'^#define RX_(%s) (.*)$' % "|".join(STAMPS), re.M)


def population():
    jobs = []
    for setname, _path in _sc.subbench_dirs():
        sb = _sb.find(setname)
        enc = ["-e", "utf8"] if getattr(sb, "encoding", "byte") == "utf8" else []
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            fs = "free-spacing" in _cap.pattern_requires(p)
            forms = (("plain", text),
                     ("whole", _rec.whole_subject_text(text, fs)))
            for cfg, extra in CONFIGS:
                for form, t in forms:
                    jobs.append((sb.id, p.name, cfg, form, BASE + enc + extra, t))
    return jobs


def _sha(t):
    return PI.program_sha256_of_text(t) if t else None


def one(job):
    sid, pid, cfg, form, flags, pat = job
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
        got = {p: PI.emit(BINS[p], "--pattern", flags, pat, os.path.join(tmp, p))
               for p in (OLD, NEW)}
        v2 = {p: _sha(t) for p, t in got.items()}
        if got[OLD] is None and got[NEW] is None:
            verdict = "refused-both"
        elif got[OLD] is None or got[NEW] is None:
            verdict = "refusal-mover:" + ("old" if got[OLD] is None else "new")
        else:
            verdict = "identical" if v2[OLD] == v2[NEW] else "changed"
        den = []
        for name, extra in DENIES:
            if got[NEW] is None:
                den.append("-")
                continue
            t = PI.emit(BINS[NEW], "--pattern", flags + extra, pat,
                        os.path.join(tmp, name))
            h = _sha(t)
            den.append("refused" if t is None else
                       "same" if h == v2[NEW] else
                       "to-S73" if h == v2[OLD] else "differs")
    st = {p: dict(STAMP_RE.findall(got[p] or "")) for p in (OLD, NEW)}

    def pair(k):
        a, b = st[OLD].get(k, "-"), st[NEW].get(k, "-")
        return a if a == b else "%s>%s" % (a, b)
    sz = lambda t: str(len(t)) if t else "-"      # noqa: E731
    return [sid, pid, cfg, form, verdict] + den + [pair(k) for k in STAMPS] \
        + [sz(got[OLD]), sz(got[NEW])]


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    for p, b in BINS.items():
        if not os.path.isfile(b):
            sys.exit("no build for %s at %s" % (p, b))
    jobs = population()
    with cf.ProcessPoolExecutor(int(os.environ.get("B135S3_JOBS", "4"))) as ex:
        rows = list(ex.map(one, jobs, chunksize=2))
    hdr = ["set", "pattern_id", "config", "form", "verdict", "dw", "dl", "dwl",
           "dwlp"] + [k.lower() for k in STAMPS] + ["bytes_73", "bytes_74"]
    with open(OUT, "w") as fh:
        fh.write("# probe_b135s3_census.py: %s -> %s, %d rows\n" % (OLD, NEW, len(rows)))
        fh.write("\t".join(hdr) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    print("rows=%d" % len(rows))


if __name__ == "__main__":
    main()
