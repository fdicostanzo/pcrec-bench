"""docs/dev/measurements/probe_b124_census.py -- [B124] (lane b124prep,
2026-10-07, inbox I-130/I-131/I-132): the COMPILE-ONLY answer/identity
census for the re-pin PREP c4c70f2c (abi 59) -> 5ff21faca (abi 65,
lane/k93tri's tip: pcrec main 445f2ffc1 + the K93/K95 fixes).

POPULATION: probe_b122_census.py's exactly -- every pattern of every
sub-bench under `bench/` by ENUMERATION x {plain, whole-subject} x the
set's own `pcrec-auto` / `pcrec-vm` argv (`-e utf8` on the utf8 set),
compiled at BOTH pins, v2 program identity (`tools/program_identity.py`).

ATTRIBUTION of every `changed` / refusal-mover row, in two layers:
  1. K93/K95 vs main: the row is also emitted at 445f2ffc1 (main just
     before the K93 lane, built as a SCRATCH pin under
     $B124_SCRATCH_BUILD, never under build/). `k93tri` = the tip differs
     from 445f2ffc1 (the possessify-under-call-context fix, or K95's
     --trace gate -- never reached here, no config traces).
  2. abi 60-65 on main: the row is re-emitted at the tip under each of
     `-fno-req-set-lead`, `-fno-req-handoff`, `-fno-start-set` and under
     all three; `restored-by:X` = that denial alone reproduces
     c4c70f2c's v2 identity, `restored-by:all-three` = only together.
  A row restored by neither is `not-restored` and its stamp columns name
  the moving fact (K82 (C)'s NONE-pick moves RX_REQ_RUN's `@idx` under
  `-e utf8` and has no flag of its own).

ANSWERS: compile-only, no subject runs. `identical` rows are
answer-identical by construction; `changed` rows rest on pcrec's own
per-step "no answer moves" (K93 is a WRONG-ANSWER fix: its movers are
the rows whose answers are expected to CHANGE toward the oracle) and on
the window's oracle agreement.

    B124_JOBS=4 python3 docs/dev/measurements/probe_b124_census.py OUT.tsv

Archived output: docs/dev/measurements/2026-10-07-b124prep-census.txt.
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
SCRATCH = os.environ.get("B124_SCRATCH", "/var/tmp/b124census")
SCRATCH_BUILD = os.environ.get("B124_SCRATCH_BUILD", "/var/tmp/b124scratch")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
OLD, NEW, MID = "c4c70f2c", "5ff21faca", "445f2ffc1"
BINS = {p: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % p)
        for p in (OLD, NEW)}
BINS[MID] = os.path.join(SCRATCH_BUILD, "pcrec-%s/build/pcrec" % MID)
BASE = ["--features", "all"]
CONFIGS = (("auto", []), ("vm", ["--engine=vm"]))
DENIES = ("-fno-req-set-lead", "-fno-req-handoff", "-fno-start-set")
STAMPS = ("REQ_HANDOFF", "VM_START_SCAN", "DFA_PREFILTER", "REQ_RUN",
          "REQ_WHY", "MEMFN_LIBC", "ENGINE", "ENGINE_SEL", "VM_PREFILTER")
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
                    jobs.append((sb.id, p.name, cfg, form,
                                 BASE + enc + extra, t))
    return jobs


def _sha(t):
    return PI.program_sha256_of_text(t) if t else None


def one(job):
    sid, pid, cfg, form, flags, pat = job
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
        got = {pin: PI.emit(BINS[pin], "--pattern", flags, pat,
                            os.path.join(tmp, pin)) for pin in (OLD, NEW)}
        v2 = {p: _sha(t) for p, t in got.items()}
        st = {p: dict(STAMP_RE.findall(t or "")) for p, t in got.items()}
        refused = [p for p in (OLD, NEW) if got[p] is None]
        if len(refused) == 2:
            verdict = "refused-both"
        elif refused:
            verdict = "refusal-mover:" + refused[0]
        elif v2[OLD] != v2[NEW]:
            verdict = "changed"
        else:
            verdict = "identical"
        attrib = "-"
        layer = "-"
        if verdict == "changed" or verdict.startswith("refusal-mover"):
            t_mid = PI.emit(BINS[MID], "--pattern", flags, pat,
                            os.path.join(tmp, MID))
            layer = "main" if _sha(t_mid) == v2[NEW] else "k93tri"
            alone = []
            for i, fl in enumerate(DENIES):
                t = PI.emit(BINS[NEW], "--pattern", flags + [fl], pat,
                            os.path.join(tmp, "d%d" % i))
                if _sha(t) == v2[OLD]:
                    alone.append(fl.replace("-fno-", ""))
            t = PI.emit(BINS[NEW], "--pattern", flags + list(DENIES), pat,
                        os.path.join(tmp, "dall"))
            allrest = _sha(t) == v2[OLD]
            attrib = ("restored-by:" + ",".join(alone) if alone
                      else ("restored-by:all-three" if allrest
                            else "not-restored"))
    o, n = st[OLD], st[NEW]

    def pair(k):
        a, b = o.get(k, "-"), n.get(k, "-")
        return a if a == b else "%s>%s" % (a, b)
    return [sid, pid, cfg, form, verdict, layer, attrib] + [pair(k) for k in STAMPS] \
        + [v2[OLD] or "-", v2[NEW] or "-"]


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    for p, b in BINS.items():
        if not os.path.isfile(b):
            sys.exit("no build for %s at %s" % (p, b))
    workers = int(os.environ.get("B124_JOBS", "6"))
    jobs = population()
    with cf.ProcessPoolExecutor(workers) as ex:
        rows = list(ex.map(one, jobs, chunksize=2))
    hdr = ["set", "pattern_id", "config", "form", "verdict", "layer",
           "attribution"] \
        + [k.lower() for k in STAMPS] + ["v2_old", "v2_new"]
    with open(OUT, "w") as fh:
        fh.write("# probe_b124_census.py: %s -> %s (layer via %s), %d rows\n"
                 % (OLD, NEW, MID, len(rows)))
        fh.write("\t".join(hdr) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    from collections import Counter
    c = Counter(r[4] for r in rows)
    print("rows=%d %s" % (len(rows), " ".join("%s=%d" % kv for kv in sorted(c.items()))))
    a = Counter((r[5], r[6]) for r in rows if r[4] == "changed")
    print("changed layer/attribution: " + " ".join("%s/%s=%d" % (k[0], k[1], v) for k, v in sorted(a.items())))
    for r in rows:
        if r[4].startswith("refusal-mover"):
            print("  REFUSAL-MOVER %s/%s %s %s: %s (%s %s)" % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
    per = Counter((r[0], r[4]) for r in rows)
    for k in sorted(per):
        print("  %-12s %-28s %d" % (k[0], k[1], per[k]))


if __name__ == "__main__":
    main()
