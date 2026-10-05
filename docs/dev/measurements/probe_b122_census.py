"""docs/dev/measurements/probe_b122_census.py -- [B122] (lane b122repin,
2026-10-04, inbox I-127): the COMPILE-ONLY answer/identity census for the
re-pin fc719ca4 (abi 50) -> c4c70f2c (abi 59).

POPULATION: every pattern of every sub-bench under `bench/` by
ENUMERATION (`tools/selfcheck.subbench_dirs()`, [B11.1]'s rule) x BOTH
forms the adapter compiles (plain, and the whole-subject
`record.whole_subject_text` form, free-spacing aware) x TWO configs per
set -- the set's own `pcrec-auto` and `pcrec-vm` argv (`--features all`,
plus `-e utf8` on the set whose `[expectations] encoding` is utf8, which
is how the `-utf8` sibling testees reach it) -- compiled at BOTH pins.

Per row: a VERDICT from v2 program identity (`tools/program_identity.py`
normalize_one; the K80 guard dropped by its [B122] amendment) --
`identical` / `changed` / `refused-both` / `refusal-mover:<pin>` -- plus
the stamps the nine abi steps can move (RUN_WORDS, REQ_RUN, REQ_WHY,
DFA_SCAN_EDGE, VM_RESEED, ENGINE, ENGINE_SEL, VM_ENTRY_SHAPE) at each pin,
and an ATTRIBUTION for each `changed` row from the deny flags at the new
pin: the row is re-emitted at c4c70f2c under each of `-fno-view-edge`,
`-fno-run-overlap`, `-fno-req-run-fold` and under all three; a row whose
all-three-denied artifact equals fc719ca4's v2 identity is attributed to
the round-1 flags alone (A1/K78/K79/[CLS-TREE] S2 did not move it); the
single flag(s) whose denial ALONE restores the old identity are named.

ANSWERS: compile-only, so no subject is run. A row reading `identical`
is answer-identical by construction (same program). A `changed` row's
answers are pcrec's own contract (every one of the nine steps states "no
answer moves") and the window's oracle agreement is the standing proof.

No gcc, no timing, no store write. Run from the repo root (pin.sh must
have built both binaries):

    python3 docs/dev/measurements/probe_b122_census.py OUT.tsv

Archived output: docs/dev/measurements/2026-10-04-b122-census.txt.
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
SCRATCH = os.environ.get("B122_SCRATCH", "/var/tmp/b122scratch")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
OLD, NEW = "fc719ca4", "c4c70f2c"
BINS = {p: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % p)
        for p in (OLD, NEW)}
BASE = ["--features", "all"]
CONFIGS = (("auto", []), ("vm", ["--engine=vm"]))
DENIES = ("-fno-view-edge", "-fno-run-overlap", "-fno-req-run-fold")
STAMPS = ("RUN_WORDS", "REQ_RUN", "REQ_WHY", "DFA_SCAN_EDGE", "VM_RESEED",
          "ENGINE", "ENGINE_SEL", "VM_ENTRY_SHAPE")
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
        if verdict == "changed" or verdict.startswith("refusal-mover"):
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
                            else "not-restored-by-round1-denials"))
    o, n = st[OLD], st[NEW]

    def pair(k):
        a, b = o.get(k, "-"), n.get(k, "-")
        return a if a == b else "%s>%s" % (a, b)
    return [sid, pid, cfg, form, verdict, attrib] + [pair(k) for k in STAMPS] \
        + [v2[OLD] or "-", v2[NEW] or "-"]


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    for p, b in BINS.items():
        if not os.path.isfile(b):
            sys.exit("no build for %s at %s" % (p, b))
    workers = int(os.environ.get("B122_JOBS", "6"))
    jobs = population()
    with cf.ProcessPoolExecutor(workers) as ex:
        rows = list(ex.map(one, jobs, chunksize=2))
    hdr = ["set", "pattern_id", "config", "form", "verdict", "attribution"] \
        + [k.lower() for k in STAMPS] + ["v2_old", "v2_new"]
    with open(OUT, "w") as fh:
        fh.write("# probe_b122_census.py: %s -> %s, %d rows\n"
                 % (OLD, NEW, len(rows)))
        fh.write("\t".join(hdr) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    from collections import Counter
    c = Counter(r[4] for r in rows)
    print("rows=%d %s" % (len(rows), " ".join("%s=%d" % kv for kv in sorted(c.items()))))
    a = Counter(r[5] for r in rows if r[4] == "changed")
    print("changed attribution: " + " ".join("%s=%d" % kv for kv in sorted(a.items())))
    for r in rows:
        if r[4].startswith("refusal-mover"):
            print("  REFUSAL-MOVER %s/%s %s %s: %s (%s)" % (r[0], r[1], r[2], r[3], r[4], r[5]))
    per = Counter((r[0], r[4]) for r in rows)
    for k in sorted(per):
        print("  %-12s %-28s %d" % (k[0], k[1], per[k]))


if __name__ == "__main__":
    main()
