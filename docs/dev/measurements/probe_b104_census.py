"""docs/dev/measurements/probe_b104_census.py -- [B104] (lane b104repin,
2026-09-27): the COMPILE-ONLY program-identity census for the re-pin
02902356 (abi 37) -> 751b9c6d (abi 39), over the SAME two populations
`probe_b101_census.py` used (I-112's ask: "verify with the program-identity
census over the same population b101repin used"):

  i111   pcrec's own `docs/dev/optloop/c2/reqpos_census.py` `bench_pop()`
         reproduced: EVERY bench/*/patterns/*.rx file of this repo (325 at
         this HEAD, all sets, not capability alone), trailing newlines
         stripped, the PLAIN form only, x {caps: `--features all`, nocaps:
         + `--no-captures`} = 650 artifact-configs, auto engine, BYTE
         encoding (`-e utf8` is a SEPARATE, smaller population -- the seven
         utf8 lit-* witnesses are checked by value elsewhere, this census
         is the byte-encoding identity claim).
  cap    capability@0.1 under this project's own three distinct compiled
         configs (auto-caps, auto-nocaps, vm-caps; vm-in-caps is
         compile-identical to vm-caps) x 64 patterns x BOTH forms (plain,
         whole-subject) = 384.

ONE identity per step (v2, the record field's own normalization --
`tools/program_identity.py`'s `program_sha256_of_text`, imported directly
rather than through the CLI, because the CLI needs `measured` records at
BOTH pins in store/index.tsv and no window has run at 751b9c6d yet -- the
same reason b101/b90's own census scripts call PI.emit()/
program_sha256_of_text() directly). No raw/v1 side this time: unlike
b101's five-build attribution (which needed pcrec's own byte-for-byte rule
to split three codegen merges), this re-pin absorbs exactly ONE bench
change worth attributing (K68's `.flags` mask, which v2 already drops as
an unreferenced rx_info initializer member) and I-112 predicts ZERO
program movement anywhere on this population, so a single v2 identity
answers the question the population needs answered: did anything move?

Emits WITHOUT -fcomments (program_identity.emit). No gcc, no timing.
Run from the repo root (pin.sh must have built both binaries):

    python3 docs/dev/measurements/probe_b104_census.py OUT.tsv

Archived output: docs/dev/measurements/2026-09-27-b104-census.txt.
"""
import concurrent.futures as cf
import glob, os, re, sys, tempfile
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI                          # noqa: E402
from pcrecbench import subbench as _sb                 # noqa: E402
from pcrecbench import record as _rec                  # noqa: E402
from pcrecbench import capability as _cap              # noqa: E402

OUT = sys.argv[1]
SCRATCH = os.environ.get("B104_SCRATCH", "/var/tmp/b104scratch")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
PINS = ["02902356", "751b9c6d"]
BINS = {p: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % p) for p in PINS}
CAPS = ["--features", "all"]
NOCAPS = ["--features", "all", "--no-captures"]
VM = ["--features", "all", "--engine=vm"]
STAMPS = ("REQ_WHY", "REQ_BYTE", "REQ_RUN", "DFA_PREFILTER", "ENGINE")
STAMP_RE = re.compile(r'^#define RX_(%s) "([^"]*)"$' % "|".join(STAMPS), re.M)


def population():
    jobs = []
    for p in sorted(glob.glob(os.path.join("bench", "*", "patterns", "*.rx"))):
        setname = p.split(os.sep)[-3]
        name = os.path.basename(p)[:-3]
        b = open(p, "rb").read()
        while b.endswith(b"\n"):
            b = b[:-1]
        if b:
            for cfg, flags in (("caps", CAPS), ("nocaps", NOCAPS)):
                jobs.append(("i111", "%s/%s" % (setname, name), cfg, "plain",
                             flags, b))
    sb = _sb.find("capability")
    for cfg, flags in (("auto-caps-simdna", CAPS),
                       ("auto-nocaps-simdna", NOCAPS),
                       ("vm-caps-simdna", VM)):
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            fs = "free-spacing" in _cap.pattern_requires(p)
            for form in PI.FORMS:
                ptext = text if form == "plain" else _rec.whole_subject_text(text, fs)
                jobs.append(("cap", p.name, cfg, form, flags, ptext))
    return jobs


def one(job):
    pop, pid, cfg, form, flags, pat = job
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
    return [pop, pid, cfg, form, cause,
            o.get("REQ_WHY", "-"), n.get("REQ_WHY", "-"),
            o.get("REQ_BYTE", "-"), n.get("REQ_BYTE", "-"),
            o.get("REQ_RUN", "-"), n.get("REQ_RUN", "-"),
            o.get("DFA_PREFILTER", "-"), n.get("DFA_PREFILTER", "-"),
            n.get("ENGINE", "-"),
            v2[PINS[0]] or "-", v2[PINS[1]] or "-"]


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    for p, b in BINS.items():
        if not os.path.isfile(b):
            sys.exit("no build for %s at %s" % (p, b))
    jobs = population()
    workers = int(os.environ.get("B104_JOBS", "6"))
    with cf.ProcessPoolExecutor(workers) as ex:
        rows = list(ex.map(one, jobs, chunksize=4))
    hdr = ["pop", "pattern_id", "config", "form", "verdict",
           "req_why_old", "req_why_new", "req_byte_old", "req_byte_new",
           "req_run_old", "req_run_new", "dfa_prefilter_old",
           "dfa_prefilter_new", "engine_new", "v2_sha_old", "v2_sha_new"]
    with open(OUT, "w") as fh:
        fh.write("\t".join(hdr) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    n_id = sum(1 for r in rows if r[4] == "identical")
    n_ch = sum(1 for r in rows if r[4] == "changed")
    n_rb = sum(1 for r in rows if r[4] == "refused-both")
    n_rm = sum(1 for r in rows if r[4].startswith("refusal-mover"))
    print("DONE rows=%d identical=%d changed=%d refused-both=%d "
          "refusal-mover=%d" % (len(rows), n_id, n_ch, n_rb, n_rm))


if __name__ == "__main__":
    main()
