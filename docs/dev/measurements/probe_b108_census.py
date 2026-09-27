"""docs/dev/measurements/probe_b108_census.py -- [B108] (lane b108repin,
2026-09-27): the COMPILE-ONLY program-identity census for the re-pin
751b9c6d (abi 39) -> a32bc86e (abi 41), over the SAME population pcrec's
own S2a lane used for its bench movers manifest (inbox I-113,
`docs/dev/lanes/s2a_report.md` §2 in ~/pcrec at a32bc86e): capability@0.1's
own patterns under FOUR configs (auto-caps, auto-nocaps, vm-caps,
vm-nocaps), plain form only -- 64 patterns x 4 configs = 256
artifact-configs. pcrec's own manifest over this exact population read
identical=186 / changed=63 / refused(both)=5 / refusal-mismatch=2. I-113's
own summary line ("Movers: exactly 1,081 artifact-configs (63 bench +
1,018 corpus)") is this 63; the 1,018-corpus half is pcrec's own
`tests/**/*.rxt` population, which this project does not carry, so it is
out of scope here (I-113's own manifest table already reports it).

Uses program_sha256_of_text (v2 normalization, `tools/program_identity.py`)
directly, the same as `probe_b104_census.py` -- v2's rule 2 drops the
WHOLE `#ifndef PCREC_RX_ABI_H` block (struct rx_info's own declaration,
findings' appended member included) and rule 3 drops the unreferenced
`rx_info` initializer (`.findings = "byte-rate=..."` included), rule 5
drops the unreferenced `#define RX_FINDINGS "..."` line, so [FINDINGS] B1's
own two-line addition is invisible to this identity by construction --
this census is a pure S2a read. No gcc, no timing.

Run from the repo root (pin.sh must have built both binaries):

    python3 docs/dev/measurements/probe_b108_census.py OUT.tsv

Archived output: docs/dev/measurements/2026-09-27-b108-census.txt.
"""
import concurrent.futures as cf
import os, re, sys, tempfile
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI                          # noqa: E402
from pcrecbench import subbench as _sb                 # noqa: E402
from pcrecbench import capability as _cap              # noqa: E402

OUT = sys.argv[1]
SCRATCH = os.environ.get("B108_SCRATCH", "/var/tmp/b108scratch")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
PINS = ["751b9c6d", "a32bc86e"]
BINS = {p: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % p) for p in PINS}
CAPS = ["--features", "all"]
NOCAPS = ["--features", "all", "--no-captures"]
VMCAPS = ["--features", "all", "--engine=vm"]
VMNOCAPS = ["--features", "all", "--engine=vm", "--no-captures"]
BENCH_CFG = (("auto-caps", CAPS), ("auto-nocaps", NOCAPS),
             ("vm-caps", VMCAPS), ("vm-nocaps", VMNOCAPS))
STAMPS = ("VM_LIT_RUNS", "VM_PROGRAM_BYTES", "VM_ENTRY_SHAPE",
          "VM_PREFILTER_LANG_WHY", "DFA_PREFILTER", "ENGINE")
STAMP_RE = re.compile(r'^#define RX_(%s) (.*)$' % "|".join(STAMPS), re.M)


def population():
    sb = _sb.find("capability")
    jobs = []
    for cfg, flags in BENCH_CFG:
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            jobs.append(("bench", p.name, cfg, flags, text))
    return jobs


def one(job):
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
            o.get("VM_PROGRAM_BYTES", "-"), n.get("VM_PROGRAM_BYTES", "-"),
            o.get("VM_ENTRY_SHAPE", "-"), n.get("VM_ENTRY_SHAPE", "-"),
            n.get("ENGINE", "-"),
            v2[PINS[0]] or "-", v2[PINS[1]] or "-"]


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    for p, b in BINS.items():
        if not os.path.isfile(b):
            sys.exit("no build for %s at %s" % (p, b))
    jobs = population()
    workers = int(os.environ.get("B108_JOBS", "6"))
    with cf.ProcessPoolExecutor(workers) as ex:
        rows = list(ex.map(one, jobs, chunksize=4))
    hdr = ["pop", "pattern_id", "config", "verdict",
           "vm_lit_runs_old", "vm_lit_runs_new",
           "vm_program_bytes_old", "vm_program_bytes_new",
           "vm_entry_shape_old", "vm_entry_shape_new", "engine_new",
           "v2_sha_old", "v2_sha_new"]
    with open(OUT, "w") as fh:
        fh.write("\t".join(hdr) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    n_id = sum(1 for r in rows if r[3] == "identical")
    n_ch = sum(1 for r in rows if r[3] == "changed")
    n_rb = sum(1 for r in rows if r[3] == "refused-both")
    n_rm = sum(1 for r in rows if r[3].startswith("refusal-mover"))
    print("DONE rows=%d identical=%d changed=%d refused-both=%d "
          "refusal-mover=%d" % (len(rows), n_id, n_ch, n_rb, n_rm))


if __name__ == "__main__":
    main()
