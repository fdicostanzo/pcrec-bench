"""docs/dev/measurements/probe_b136prep_census.py -- [B136] (lane b136prep,
2026-10-12, inbox I-147 + I-148 section 1): the COMPILE-ONLY census for the
re-pin b8337c33 (abi 74) -> 00c97769 (abi 75, [REQ-HANDOFF-L1]) -> 6b2dbd3e
(abi 76, [LOSS-REVIEW] candidate 1: the encoding seam helpers `static
inline`).

POPULATION: every pattern of every sub-bench under `bench/` by ENUMERATION x
{plain, whole-subject} x {auto-caps (`--features all`), auto-nocaps
(+ `--no-captures`)} (`-e utf8` on the utf8 set), each emitted at all three
builds (v2 program identity, `tools/program_identity.py`).

Per row: verdict L1 (00c97769 vs b8337c33), verdict SEAM (6b2dbd3e vs
00c97769), the stamps on all three sides (A|B|C), emitted-text bytes at all
three, and ONE denial AT 00c97769: `dh` (-fno-req-handoff) compared to
b8337c33's v2 identity (`to-B` / `same` / `differs` / `refused`). I-147
warns that `-fno-req-handoff` also drops K82's entry handoff, so `differs`
is expected wherever K82 acted; `to-B` marks rows where L1 alone moved.

    B136_JOBS=4 python3 docs/dev/measurements/probe_b136prep_census.py OUT.tsv
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
SCRATCH = os.environ.get("B136_SCRATCH", "/var/tmp/pcrecbench/b136prep/census")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
PINS = ("b8337c33", "00c97769", "6b2dbd3e")
BINS = {p: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % p) for p in PINS}
BASE = ["--features", "all"]
CONFIGS = (("caps", []), ("nocaps", ["--no-captures"]))
STAMPS = ("ENGINE", "ENGINE_SEL", "DFA_SCAN", "DFA_START", "DFA_MATCH",
          "DFA_PREFILTER", "REQ_WHY", "REQ_HANDOFF", "REQ_RUN", "REQ_BYTE",
          "MEMFN_LIBC")
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
    B, L, S = PINS
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
        got = {p: PI.emit(BINS[p], "--pattern", flags, pat, os.path.join(tmp, p))
               for p in PINS}
        v2 = {p: _sha(t) for p, t in got.items()}

        def verdict(x, y):
            if got[x] is None and got[y] is None:
                return "refused-both"
            if got[x] is None or got[y] is None:
                return "refusal-mover:" + ("old" if got[x] is None else "new")
            return "identical" if v2[x] == v2[y] else "changed"
        dh = "-"
        if got[L] is not None:
            t = PI.emit(BINS[L], "--pattern", flags + ["-fno-req-handoff"], pat,
                        os.path.join(tmp, "dh"))
            h = _sha(t)
            dh = ("refused" if t is None else "same" if h == v2[L] else
                  "to-B" if h == v2[B] else "differs")
    st = {p: dict(STAMP_RE.findall(got[p] or "")) for p in PINS}

    def triple(k):
        v = [st[p].get(k, "-") for p in PINS]
        return v[0] if v[0] == v[1] == v[2] else "|".join(v)
    sz = lambda t: str(len(t)) if t else "-"      # noqa: E731
    return [sid, pid, cfg, form, verdict(B, L), verdict(L, S), dh] \
        + [triple(k) for k in STAMPS] + [sz(got[p]) for p in PINS]


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    for p, b in BINS.items():
        if not os.path.isfile(b):
            sys.exit("no build for %s at %s" % (p, b))
    jobs = population()
    with cf.ProcessPoolExecutor(int(os.environ.get("B136_JOBS", "4"))) as ex:
        rows = list(ex.map(one, jobs, chunksize=2))
    hdr = ["set", "pattern_id", "config", "form", "l1_b_to_l", "seam_l_to_s",
           "dh_at_L"] + [k.lower() for k in STAMPS] \
        + ["bytes_b8337c33", "bytes_00c97769", "bytes_6b2dbd3e"]
    with open(OUT, "w") as fh:
        fh.write("# probe_b136prep_census.py: %s, %d rows\n" % (" -> ".join(PINS), len(rows)))
        fh.write("\t".join(hdr) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    print("rows=%d" % len(rows))


if __name__ == "__main__":
    main()
