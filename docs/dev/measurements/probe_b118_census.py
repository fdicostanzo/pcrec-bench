"""docs/dev/measurements/probe_b118_census.py -- [B118] (lane b118repin,
2026-09-30): the COMPILE-ONLY census for the re-pin a32bc86e (abi 41) ->
fc719ca4 (abi 50), inbox I-122/I-118.

TWO parts, run together:

PART A -- the same shape as probe_b108_census.py: capability@0.1's own 64
patterns under FOUR configs (auto-caps, auto-nocaps, vm-caps, vm-nocaps),
plain form only -- 256 artifact-configs, v2 program identity
(`tools/program_identity.py`). Answers "does anything on the bench's own
harder-shapes set change program, refuse, or start/stop refusing" across
the whole abi 41->50 span in one pass.

PART B -- I-122's own explicit ask: "A cell that was a pcrec refusal on
your roster may now have a number; please report any that flip." Every
`bench/*/patterns/*.rx` pattern (all six sets: email, loglines, bounded,
altwide, syntax, capability -- utf8 excluded, it is `-e utf8`-only and
needs its own pass, see the header note below) x plain form x pcrec-auto's
real argv, compiled at BOTH pins; reports every (pattern, form) whose
outcome DIFFERS (did-not-compile <-> compiled) in EITHER direction.

No gcc, no timing, no store write -- compile-only (`pcrec -p rx -o
art.c --features all -fcomments <flags> --pattern <text>`), matching
every prior probe_bNNN_census.py's own posture.

Run from the repo root (pin.sh must have built both binaries):

    python3 docs/dev/measurements/probe_b118_census.py OUT_A.tsv OUT_B.tsv

Archived output: docs/dev/measurements/2026-09-30-b118-census.txt.
"""
import concurrent.futures as cf
import os, re, sys, tempfile
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI                          # noqa: E402
from pcrecbench import subbench as _sb                  # noqa: E402

OUT_A = sys.argv[1]
OUT_B = sys.argv[2]
SCRATCH = os.environ.get("B118_SCRATCH", "/var/tmp/b118scratch")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
PINS = ["a32bc86e", "fc719ca4"]
BINS = {p: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % p) for p in PINS}
CAPS = ["--features", "all"]
NOCAPS = ["--features", "all", "--no-captures"]
VMCAPS = ["--features", "all", "--engine=vm"]
VMNOCAPS = ["--features", "all", "--engine=vm", "--no-captures"]
BENCH_CFG = (("auto-caps", CAPS), ("auto-nocaps", NOCAPS),
             ("vm-caps", VMCAPS), ("vm-nocaps", VMNOCAPS))
STAMPS = ("VM_LIT_RUNS", "VM_CLS_KIT", "VM_CLS_ATOMS", "VM_RESEED",
          "UTF_CHECK", "ENGINE", "ENGINE_SEL")
STAMP_RE = re.compile(r'^#define RX_(%s) (.*)$' % "|".join(STAMPS), re.M)

# PART B's set roster: every subbench with a `patterns/` tree except utf8
# (encoding = utf8 only; a flip census there needs `-e utf8` on both
# configs, out of THIS script's scope -- see the lane report for why).
PART_B_SETS = ("email", "loglines", "bounded", "altwide", "syntax",
               "capability")


def population_a():
    sb = _sb.find("capability")
    jobs = []
    for cfg, flags in BENCH_CFG:
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            jobs.append(("bench", p.name, cfg, flags, text))
    return jobs


def one_a(job):
    pop, pid, cfg, flags, pat = job
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
        got = {}
        for pin in PINS:
            got[pin] = PI.emit(BINS[pin], "--pattern", flags, pat,
                               os.path.join(tmp, pin))
    v2 = {p: (PI.program_sha256_of_text(t) if t else None) for p, t in got.items()}
    st = {p: dict(STAMP_RE.findall(t or "")) for p, t in got.items()}
    refused = [p for p in PINS if got[p] is None]
    if len(refused) == len(PINS):
        cause = "refused-both"
    elif refused:
        cause = "refusal-mover:" + ",".join(refused)
    elif v2[PINS[0]] != v2[PINS[1]]:
        cause = "changed"
    else:
        cause = "identical"
    o, n = st[PINS[0]], st[PINS[1]]
    return [pop, pid, cfg, cause,
            o.get("VM_LIT_RUNS", "-"), n.get("VM_LIT_RUNS", "-"),
            n.get("VM_CLS_KIT", "-"), n.get("VM_CLS_ATOMS", "-"),
            n.get("VM_RESEED", "-"), n.get("UTF_CHECK", "-"),
            n.get("ENGINE_SEL", "-"), n.get("ENGINE", "-"),
            v2[PINS[0]] or "-", v2[PINS[1]] or "-"]


def population_b():
    jobs = []
    for setname in PART_B_SETS:
        sb = _sb.find(setname)
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            jobs.append((setname, p.name, text))
    return jobs


def one_b(job):
    setname, pid, pat = job
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
        got = {}
        for pin in PINS:
            got[pin] = PI.emit(BINS[pin], "--pattern", CAPS, pat,
                               os.path.join(tmp, pin))
    compiled = {p: (got[p] is not None) for p in PINS}
    if compiled[PINS[0]] == compiled[PINS[1]]:
        verdict = "unchanged"
    elif compiled[PINS[1]] and not compiled[PINS[0]]:
        verdict = "FLIP: refused -> compiled"
    else:
        verdict = "FLIP: compiled -> refused"
    return [setname, pid, str(compiled[PINS[0]]), str(compiled[PINS[1]]),
            verdict]


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    for p, b in BINS.items():
        if not os.path.isfile(b):
            sys.exit("no build for %s at %s" % (p, b))
    workers = int(os.environ.get("B118_JOBS", "6"))

    jobs_a = population_a()
    with cf.ProcessPoolExecutor(workers) as ex:
        rows_a = list(ex.map(one_a, jobs_a, chunksize=4))
    hdr_a = ["pop", "pattern_id", "config", "verdict",
             "vm_lit_runs_old", "vm_lit_runs_new",
             "vm_cls_kit_new", "vm_cls_atoms_new", "vm_reseed_new",
             "utf_check_new", "engine_sel_new", "engine_new",
             "v2_sha_old", "v2_sha_new"]
    with open(OUT_A, "w") as fh:
        fh.write("\t".join(hdr_a) + "\n")
        for r in rows_a:
            fh.write("\t".join(r) + "\n")

    jobs_b = population_b()
    with cf.ProcessPoolExecutor(workers) as ex:
        rows_b = list(ex.map(one_b, jobs_b, chunksize=4))
    hdr_b = ["set", "pattern_id", "compiled_old", "compiled_new", "verdict"]
    with open(OUT_B, "w") as fh:
        fh.write("\t".join(hdr_b) + "\n")
        for r in rows_b:
            fh.write("\t".join(r) + "\n")

    n_id = sum(1 for r in rows_a if r[3] == "identical")
    n_ch = sum(1 for r in rows_a if r[3] == "changed")
    n_rb = sum(1 for r in rows_a if r[3] == "refused-both")
    n_rm = sum(1 for r in rows_a if r[3].startswith("refusal-mover"))
    print("PART A: rows=%d identical=%d changed=%d refused-both=%d "
          "refusal-mover=%d" % (len(rows_a), n_id, n_ch, n_rb, n_rm))
    flips = [r for r in rows_b if r[4].startswith("FLIP")]
    print("PART B: rows=%d flips=%d" % (len(rows_b), len(flips)))
    for r in flips:
        print("  FLIP %s/%s: %s" % (r[0], r[1], r[4]))


if __name__ == "__main__":
    main()
