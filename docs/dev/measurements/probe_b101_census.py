"""docs/dev/measurements/probe_b101_census.py -- [B101] (lane b101repin,
2026-09-26): the COMPILE-ONLY program-identity census for the re-pin
ce658cb7 (abi 33) -> 02902356 (abi 37), with every mover ATTRIBUTED to one
of pcrec's three codegen merges by emitting at the two intermediate
SCRATCH builds as well (inbox I-111's own method):

    ce658cb7 --[K65+K66, abi 33->35]--> 27a63314
             --[S1 steps 1-5, abi 36]--> 0bb87eda
             --[S1 step 6, abi 37]-----> 42ee828f
             --[no src/ change]-------> 02902356 (the pin)

TWO POPULATIONS:

  i111   I-111's OWN bench half, reproduced to its definition: pcrec's
         docs/dev/optloop/c2/reqpos_census.py `bench_pop()` -- EVERY
         bench/*/patterns/*.rx file of this repo (325 at this HEAD, ALL
         sets, not capability alone), trailing newlines stripped, the
         PLAIN form only, x {caps: `--features all`, nocaps: + `--no-
         captures`} = 650 artifact-configs, auto engine.
  cap    capability@0.1 under this project's own three distinct compiled
         configs (auto-caps, auto-nocaps, vm-caps; vm-in-caps is compile-
         identical to vm-caps) x 64 patterns x BOTH forms (plain, whole-
         subject) = 384 -- the population the window will read.

TWO IDENTITIES per step, both reported:
  v2     tools/program_identity.py's program_sha256 (normalization v2 --
         the record field's own hash: comments stripped, the ABI block,
         the unread rx_info initializer and UNREFERENCED #defines dropped)
  raw    pcrec's own rule (s1step6_movers.py `norm`): the `.c` text
         byte for byte with only the abi digit normalised -- a moved STAMP
         VALUE is a change here and invisible to v2.

Emits WITHOUT -fcomments (program_identity.emit). No gcc, no timing.
Run from the repo root (pin.sh must have built all five binaries; the
three intermediates are scratch builds under /var/tmp/b101scratch):

    python3 docs/dev/measurements/probe_b101_census.py OUT.tsv

Archived output: docs/dev/measurements/2026-09-26-b101-census.txt.
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
SCRATCH = os.environ.get("B101_SCRATCH", "/var/tmp/b101scratch")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
PINS = ["ce658cb7", "27a63314", "0bb87eda", "42ee828f", "02902356"]
STEP = {("ce658cb7", "27a63314"): "K65K66", ("27a63314", "0bb87eda"): "S1BUILD",
        ("0bb87eda", "42ee828f"): "S1STEP6", ("42ee828f", "02902356"): "TIP"}
BINS = {p: (os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % p)
            if p in ("ce658cb7", "02902356")
            else os.path.join(SCRATCH, "pcrec-%s/build/pcrec" % p))
        for p in PINS}
CAPS = ["--features", "all"]
NOCAPS = ["--features", "all", "--no-captures"]
VM = ["--features", "all", "--engine=vm"]
STAMPS = ("REQ_WHY", "REQ_BYTE", "REQ_RUN", "DFA_PREFILTER", "ENGINE")
STAMP_RE = re.compile(r'^#define RX_(%s) "([^"]*)"$' % "|".join(STAMPS), re.M)
ABI_RE = [re.compile(r"(abi )\d+\b"), re.compile(r"(\.abi *= *)\d+\b")]


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


def raw_c(text):
    c = text.split(PI.SEP)[0]
    for r in ABI_RE:
        c = r.sub(r"\g<1>N", c)
    return c


def one(job):
    pop, pid, cfg, form, flags, pat = job
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
        got = {}
        for pin in PINS:
            got[pin] = PI.emit(BINS[pin], "--pattern", flags, pat,
                               os.path.join(tmp, pin))
    v2 = {p: (PI.program_sha256_of_text(t) if t else None) for p, t in got.items()}
    raw = {p: (raw_c(t) if t else None) for p, t in got.items()}
    st = {p: dict(STAMP_RE.findall(t or "")) for p, t in got.items()}
    refused = [p for p in PINS if got[p] is None]
    moved_v2, moved_raw = [], []
    for a, b in zip(PINS, PINS[1:]):
        if got[a] is None or got[b] is None:
            continue
        if v2[a] != v2[b]:
            moved_v2.append(STEP[(a, b)])
        if raw[a] != raw[b]:
            moved_raw.append(STEP[(a, b)])
    if len(refused) == len(PINS):
        cause_v2 = cause_raw = "refused-both"
    elif refused:
        cause_v2 = cause_raw = "refusal-mover:" + ",".join(refused)
    else:
        cause_v2 = "+".join(moved_v2) or "identical"
        cause_raw = "+".join(moved_raw) or "identical"
    b_, t_ = st["ce658cb7"], st["02902356"]
    return [pop, pid, cfg, form, cause_raw, cause_v2,
            b_.get("REQ_WHY", "-"), t_.get("REQ_WHY", "-"),
            b_.get("REQ_BYTE", "-"), t_.get("REQ_BYTE", "-"),
            b_.get("REQ_RUN", "-"), t_.get("REQ_RUN", "-"),
            b_.get("DFA_PREFILTER", "-"), t_.get("DFA_PREFILTER", "-"),
            t_.get("ENGINE", "-"),
            v2["ce658cb7"] or "-", v2["02902356"] or "-"]


def main():
    for p, b in BINS.items():
        if not os.path.isfile(b):
            sys.exit("no build for %s at %s" % (p, b))
    jobs = population()
    workers = int(os.environ.get("B101_JOBS", "6"))
    with cf.ProcessPoolExecutor(workers) as ex:
        rows = list(ex.map(one, jobs, chunksize=4))
    hdr = ["pop", "pattern_id", "config", "form", "cause_raw", "cause_v2",
           "req_why_base", "req_why_tip", "req_byte_base", "req_byte_tip",
           "req_run_base", "req_run_tip", "dfa_prefilter_base",
           "dfa_prefilter_tip", "engine_tip", "v2_sha_base", "v2_sha_tip"]
    with open(OUT, "w") as fh:
        fh.write("\t".join(hdr) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    print("DONE rows=%d" % len(rows))


if __name__ == "__main__":
    main()
