"""docs/dev/measurements/probe_b135_census.py -- [B135] (lane b135prep,
2026-10-10, inbox I-140/I-142): the COMPILE-ONLY answer/identity census for
the re-pin 255bcdd8 (abi 68) -> 7388f1c0 (abi 73), with a15fb77b (abi 72)
as the BEFORE of [OPT-REVEND].

POPULATION: probe_b124_census.py's exactly -- every pattern of every
sub-bench under `bench/` by ENUMERATION x {plain, whole-subject} x the
set's own `pcrec-auto` / `pcrec-vm` argv (`-e utf8` on the utf8 set),
v2 program identity (`tools/program_identity.py`).

ATTRIBUTION BY STEP, not by guess. The FIVE abi steps are built as SCRATCH
pins at their own main commits ($B135_SCRATCH_BUILD, never under build/):
32a1c91f0 (abi 69, [DEC-VAR-ATTRIB] + [DEC-COLLAPSE-WASTE]; it also carries
the not-an-abi-event [DEC-FALLBACK] registry change), 82ff94323 (abi 70,
[MEMFN] R4e'.0b), 631771b7f (abi 71, [MEMFN] RQ-3), a15fb77b (abi 72, R-12
VMLAZY; the BEFORE of [OPT-REVEND], a window pin built under build/) and
7388f1c0 (abi 73, [OPT-REVEND]; the pin). Each row's emit is hashed (v2) at
the six points OLD, S69, S70, S71, S72, NEW; the `steps` column lists the
transitions whose hash moved (`-` = none). Stamps compared OLD vs NEW AND
S72 vs NEW (the REVEND step alone); `revend` is `rev-end` when the pin stamps
RX_DFA_SCAN "rev-end" (the rows [OPT-REVEND] moves). `denyrev` is
`-fno-rev-end` AT the pin: `same` (v2 equal to the default -- the flag cannot
act), `to-S72` (v2 equal to a15fb77b's), or `differs`.

    B135_JOBS=4 python3 docs/dev/measurements/probe_b135_census.py OUT.tsv

Archived output: docs/dev/measurements/2026-10-10-b135prep-census.txt.
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
SCRATCH = os.environ.get("B135_SCRATCH", "/var/tmp/b135census")
SCRATCH_BUILD = os.environ.get("B135_SCRATCH_BUILD", "/var/tmp/b135scratch")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
OLD, S69, S70, S71, S72, NEW = ("255bcdd8", "32a1c91f0", "82ff94323",
                                "631771b7f", "a15fb77b", "7388f1c0")
CHAIN = (OLD, S69, S70, S71, S72, NEW)
BINS = {p: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % p)
        for p in (OLD, S72, NEW)}
for _p in (S69, S70, S71):
    BINS[_p] = os.path.join(SCRATCH_BUILD, "pcrec-%s/build/pcrec" % _p)
BASE = ["--features", "all"]
CONFIGS = (("auto", []), ("vm", ["--engine=vm"]))
REV_DENY = ["-fno-rev-end"]
STAMPS = ("ENGINE", "ENGINE_SEL", "VM_PREFILTER", "DFA_SCAN", "DFA_START",
          "DFA_MATCH", "DFA_PREFILTER", "REQ_WHY", "VM_FRAMELESS",
          "VM_PROGRAM_BYTES")
STAMP_RE = re.compile(r'^#define RX_(%s) (.*)$' % "|".join(STAMPS), re.M)
STEPNAME = {S69: "69", S70: "70", S71: "71", S72: "72", NEW: "73"}


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
                    jobs.append((sb.id, p.name, cfg, form,
                                 BASE + enc + extra, t))
    return jobs


def _sha(t):
    return PI.program_sha256_of_text(t) if t else None


def one(job):
    sid, pid, cfg, form, flags, pat = job
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
        got = {pin: PI.emit(BINS[pin], "--pattern", flags, pat,
                            os.path.join(tmp, pin)) for pin in CHAIN}
        v2 = {p: _sha(t) for p, t in got.items()}
        st = {p: dict(STAMP_RE.findall(t or "")) for p, t in got.items()}
        refused = [p for p in CHAIN if got[p] is None]
        if len(refused) == len(CHAIN):
            verdict = "refused-both"
        elif refused:
            verdict = "refusal-mover:" + ",".join(refused)
        elif v2[OLD] != v2[NEW]:
            verdict = "changed"
        else:
            verdict = "identical"
        steps = []
        for a, b in zip(CHAIN, CHAIN[1:]):
            if v2[a] != v2[b] or (got[a] is None) != (got[b] is None):
                steps.append(STEPNAME[b])
        denyrev = "-"
        if got[NEW] is not None:
            t = PI.emit(BINS[NEW], "--pattern", flags + REV_DENY, pat,
                        os.path.join(tmp, "drev"))
            h = _sha(t)
            denyrev = ("same" if h == v2[NEW] else
                       ("refused" if t is None else
                        ("to-S72" if h == v2[S72] else "differs")))
    o, n, m = st[OLD], st[NEW], st[S72]

    def pair(k):
        a, b = o.get(k, "-"), n.get(k, "-")
        return a if a == b else "%s>%s" % (a, b)
    revend = "rev-end" if n.get("DFA_SCAN") == '"rev-end"' else "-"
    step73 = "-" if v2[S72] == v2[NEW] else "moved"
    sz = lambda t: str(len(t)) if t else "-"      # noqa: E731
    return [sid, pid, cfg, form, verdict, "+".join(steps) or "-", revend,
            denyrev] + [pair(k) for k in STAMPS] \
        + [sz(got[p]) for p in CHAIN] + [v2[OLD] or "-", v2[NEW] or "-"]


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    for p, b in BINS.items():
        if not os.path.isfile(b):
            sys.exit("no build for %s at %s" % (p, b))
    workers = int(os.environ.get("B135_JOBS", "4"))
    jobs = population()
    with cf.ProcessPoolExecutor(workers) as ex:
        rows = list(ex.map(one, jobs, chunksize=2))
    hdr = ["set", "pattern_id", "config", "form", "verdict", "steps",
           "revend", "denyrev"] + [k.lower() for k in STAMPS] \
        + ["bytes_old", "bytes_s69", "bytes_s70", "bytes_s71", "bytes_s72",
           "bytes_new",
           "v2_old", "v2_new"]
    with open(OUT, "w") as fh:
        fh.write("# probe_b135_census.py: %s -> %s (steps via %s %s %s %s), %d rows\n"
                 % (OLD, NEW, S69, S70, S71, S72, len(rows)))
        fh.write("\t".join(hdr) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    from collections import Counter
    c = Counter(r[4] for r in rows)
    print("rows=%d %s" % (len(rows), " ".join("%s=%d" % kv for kv in sorted(c.items()))))
    a = Counter(r[5] for r in rows if r[4] == "changed")
    print("changed by steps: " + " ".join("%s=%d" % (k, v) for k, v in sorted(a.items())))
    for r in rows:
        if r[4].startswith("refusal-mover"):
            print("  REFUSAL-MOVER %s/%s %s %s: %s (%s)" % (r[0], r[1], r[2], r[3], r[4], r[5]))
    per = Counter((r[0], r[4]) for r in rows)
    for k in sorted(per):
        print("  %-12s %-28s %d" % (k[0], k[1], per[k]))


if __name__ == "__main__":
    main()
