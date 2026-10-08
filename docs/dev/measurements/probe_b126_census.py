"""docs/dev/measurements/probe_b126_census.py -- [B126] (lane b126prep,
2026-10-08, inbox I-134/I-135): the COMPILE-ONLY answer/identity census for
the re-pin 60366d747 (abi 65) -> 255bcdd8 (abi 68).

POPULATION: probe_b124_census.py's exactly -- every pattern of every
sub-bench under `bench/` by ENUMERATION x {plain, whole-subject} x the
set's own `pcrec-auto` / `pcrec-vm` argv (`-e utf8` on the utf8 set),
v2 program identity (`tools/program_identity.py`).

ATTRIBUTION BY STEP, not by guess. The three abi steps are built as
SCRATCH pins at their own commits ($B126_SCRATCH_BUILD, never under
build/): c9672bd2 (abi 66, [ART-POSS-ARMS]), c4c37af8 (abi 67, [MEMFN] R4h
layout normalization), 02db3811 (abi 68, [NULLABLE-ANCH]); 255bcdd8 (the
pin: 02db3811 + R4h's kit-text delegation 33186bc0, docs-only after) is
compiler-identical to 02db3811 and the census SAYS so (step `final`). Each
row's emit is hashed (v2) at the five points OLD, S66, S67, S68, NEW; the
`steps` column lists the transitions whose hash moved (`-` = none).
For a row that moved at S66 the two [ART-POSS-ARMS] denials
(`-fno-poss-ctx-follow -fno-poss-bref-first`) are applied AT S66 and the
column `deny66` says whether that reproduces OLD's v2 identity (pcrec's
"restores the abi-65 program apart from the abi digits and the stamp
line"); `deny66@new` is the same two denials at the pin vs the pin's
default (so a flip that is engine-selecting shows).

    B126_JOBS=4 python3 docs/dev/measurements/probe_b126_census.py OUT.tsv

Archived output: docs/dev/measurements/2026-10-08-b126prep-census.txt.
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
SCRATCH = os.environ.get("B126_SCRATCH", "/var/tmp/b126census")
SCRATCH_BUILD = os.environ.get("B126_SCRATCH_BUILD", "/var/tmp/b126scratch")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
OLD, S66, S67, S68, NEW = ("60366d747", "c9672bd2", "c4c37af8", "02db3811",
                           "255bcdd8")
CHAIN = (OLD, S66, S67, S68, NEW)
BINS = {OLD: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % OLD),
        NEW: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % NEW)}
for _p in (S66, S67, S68):
    BINS[_p] = os.path.join(SCRATCH_BUILD, "pcrec-%s/build/pcrec" % _p)
BASE = ["--features", "all"]
CONFIGS = (("auto", []), ("vm", ["--engine=vm"]))
POSS_DENY = ["-fno-poss-ctx-follow", "-fno-poss-bref-first"]
STAMPS = ("ENGINE", "ENGINE_SEL", "VM_PREFILTER", "VM_POSS_ARMS", "VM_STRATS",
          "VM_FRAMELESS", "VM_PROGRAM_BYTES")
STAMP_RE = re.compile(r'^#define RX_(%s) (.*)$' % "|".join(STAMPS), re.M)
STEPNAME = {S66: "66", S67: "67", S68: "68", NEW: "final"}


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
        deny66 = deny_new = "-"
        if "66" in steps and got[S66] is not None:
            t = PI.emit(BINS[S66], "--pattern", flags + POSS_DENY, pat,
                        os.path.join(tmp, "d66"))
            deny66 = "restores-OLD" if _sha(t) == v2[OLD] else "differs"
        if got[NEW] is not None:
            t = PI.emit(BINS[NEW], "--pattern", flags + POSS_DENY, pat,
                        os.path.join(tmp, "dnew"))
            deny_new = ("same" if _sha(t) == v2[NEW] else
                        ("refused" if t is None else "differs"))
    o, n = st[OLD], st[NEW]

    def pair(k):
        a, b = o.get(k, "-"), n.get(k, "-")
        return a if a == b else "%s>%s" % (a, b)
    sz = lambda t: str(len(t)) if t else "-"      # noqa: E731
    return [sid, pid, cfg, form, verdict, "+".join(steps) or "-", deny66,
            deny_new] + [pair(k) for k in STAMPS] \
        + [sz(got[p]) for p in CHAIN] + [v2[OLD] or "-", v2[NEW] or "-"]


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    for p, b in BINS.items():
        if not os.path.isfile(b):
            sys.exit("no build for %s at %s" % (p, b))
    workers = int(os.environ.get("B126_JOBS", "4"))
    jobs = population()
    with cf.ProcessPoolExecutor(workers) as ex:
        rows = list(ex.map(one, jobs, chunksize=2))
    hdr = ["set", "pattern_id", "config", "form", "verdict", "steps",
           "deny66", "deny66@new"] + [k.lower() for k in STAMPS] \
        + ["bytes_old", "bytes_s66", "bytes_s67", "bytes_s68", "bytes_new",
           "v2_old", "v2_new"]
    with open(OUT, "w") as fh:
        fh.write("# probe_b126_census.py: %s -> %s (steps via %s %s %s), %d rows\n"
                 % (OLD, NEW, S66, S67, S68, len(rows)))
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
