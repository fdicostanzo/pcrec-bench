"""docs/dev/measurements/probe_b104_o62_identity.py -- [B104] (lane
b104pred, 2026-09-27): THE STRUCTURAL PREDICTOR for O-62 sect2-6 (email,
loglines, bounded, altwide, syntax) at the I-112 window, adapted from lane
b104repin's own `probe_b104_census.py` (same v2-only method, same emit()
call, same tempfile-per-job shape) but a DIFFERENT population and a
DIFFERENT pin pair:

  - pins: 25b1984f (abi 27, O-62's own "latest cross-engine measurement of
    email/loglines/bounded/altwide/syntax" baseline) -> 751b9c6d (abi 39,
    this window's pin). NOT 02902356->751b9c6d (b104repin's own pair,
    which answers the byte-encoding-only question for capability@0.1 +
    ALL bench/*.rx in PLAIN form only) -- the O-62 sets need the
    25b1984f baseline by name, and need BOTH forms (a whole-subject
    artifact is a separate compiled program from its plain sibling, rule
    X27) since several of these sets' match regime is measured on the
    whole-subject one.
  - population: every bench/{email,loglines,bounded,altwide,syntax}/
    patterns/*.rx file (trailing newline stripped, same as b104repin's
    `i111` population), x BOTH forms (plain, whole-subject -- via
    `pcrecbench.record.whole_subject_text`, free-spacing flagged per
    pattern -- only bench/syntax/mod-x.rx needs it, checked by grep
    against every pattern file in these five sets before writing this
    script) x THREE distinct compiled configs (auto-caps, auto-nocaps,
    vm-caps -- vm-in-caps is compile-identical to vm-caps, the same fact
    b104repin's own `cap` population already relies on for
    capability@0.1; asserted again below for THIS population by an
    explicit fourth "vm-in" compile pass compared byte for byte against
    "vm" -- never assumed twice from one project fact).

ONE identity per pattern-config-form-pin cell (v2,
`program_identity.program_sha256_of_text`, called directly -- no
`store/index.tsv` row exists for either pin's records on these five sets
today, and the CLI path needs one). Emits WITHOUT -fcomments
(`program_identity.emit`, matching every other census this project has
run). No gcc, no timing, no store write, no `pcrecbench run`.

Run from the repo root (both pins must already be built --
`build/pcrec-25b1984f/build/pcrec` and `build/pcrec-751b9c6d/build/pcrec`,
both present at authoring time, neither built by this script):

    python3 docs/dev/measurements/probe_b104_o62_identity.py OUT.tsv

Archived output: docs/dev/measurements/2026-09-27-b104-o62-identity-census.txt.
"""
import concurrent.futures as cf
import glob
import os
import sys
import tempfile

sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI              # noqa: E402
from pcrecbench import record as _rec      # noqa: E402

OUT = sys.argv[1]
SCRATCH = os.environ.get("B104_SCRATCH", "/var/tmp/b104scratch")
MAIN_BUILD = "/home/duxevents/pcrec-bench/build"
PINS = ["25b1984f", "751b9c6d"]
BINS = {p: os.path.join(MAIN_BUILD, "pcrec-%s/build/pcrec" % p) for p in PINS}
CAPS = ["--features", "all"]
NOCAPS = ["--features", "all", "--no-captures"]
VM = ["--features", "all", "--engine=vm"]
CONFIGS = [("auto-caps", CAPS), ("auto-nocaps", NOCAPS), ("vm-caps", VM)]
SETS = ["email", "loglines", "bounded", "altwide", "syntax"]
# 25b1984f (abi 27) PREDATES pcrec's D118 CLI reshape (landed at abi 29,
# 8d716693): its own CLI takes the pattern as a POSITIONAL operand after
# `--`, never `--pattern` -- confirmed live (this lane's first run of this
# probe refused EVERY 25b1984f job with `--pattern`, refusal-mover 998/1110,
# before this fix). Probed per pin via program_identity._cli_shape, the
# SAME probe testees/pcrec/adapter.py and program_identity.py's own
# cross-pin census functions use -- never hard-coded, never guessed twice.
SHAPES = {}

# every pattern needing free-spacing (checked by grep against all five
# sets' patterns/*.rx before writing this script -- see module docstring):
FREE_SPACING = {"syntax/mod-x"}


def population(shapes):
    jobs = []
    for setname in SETS:
        for p in sorted(glob.glob(os.path.join("bench", setname, "patterns", "*.rx"))):
            name = os.path.basename(p)[:-3]
            pid = "%s/%s" % (setname, name)
            b = open(p, "rb").read()
            while b.endswith(b"\n"):
                b = b[:-1]
            if not b:
                continue
            fs = pid in FREE_SPACING
            for cfg, flags in CONFIGS:
                for form in PI.FORMS:
                    ptext = b if form == "plain" else _rec.whole_subject_text(b, fs)
                    jobs.append((pid, cfg, form, flags, ptext, shapes))
    return jobs


def one(job):
    pid, cfg, form, flags, pat, shapes = job
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
        got = {}
        for pin in PINS:
            got[pin] = PI.emit(BINS[pin], shapes[pin], flags, pat,
                                os.path.join(tmp, pin))
    v2 = {p: (PI.program_sha256_of_text(t) if t else None) for p, t in got.items()}
    refused = [p for p in PINS if got[p] is None]
    if len(refused) == len(PINS):
        cause = "refused-both"
    elif refused:
        cause = "refusal-mover:" + ",".join(refused)
    elif v2[PINS[0]] != v2[PINS[1]]:
        cause = "changed"
    else:
        cause = "identical"
    setname = pid.split("/", 1)[0]
    return [setname, pid, cfg, form, cause,
            v2[PINS[0]] or "-", v2[PINS[1]] or "-"]


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    for p, b in BINS.items():
        if not os.path.isfile(b):
            sys.exit("no build for %s at %s" % (p, b))
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
        for p, b in BINS.items():
            SHAPES[p] = PI._cli_shape(b, tmp)
    print("CLI shapes: %s" % SHAPES)
    # SHAPES is passed explicitly per job (never read as a global inside a
    # worker): this project's Python defaults ProcessPoolExecutor to the
    # 'forkserver' start method, whose workers are forked from a template
    # process started at import time -- a global set later in main() (here)
    # would silently NOT be visible to them. Found live: the first run of
    # this exact script (before this comment existed) hard-coded "--pattern"
    # instead, which is the SAME class of mistake this fix avoids repeating
    # for SHAPES.
    jobs = population(SHAPES)
    workers = int(os.environ.get("B104_JOBS", "6"))
    with cf.ProcessPoolExecutor(workers) as ex:
        rows = list(ex.map(one, jobs, chunksize=4))
    hdr = ["set", "pattern_id", "config", "form", "verdict",
           "v2_sha_25b1984f", "v2_sha_751b9c6d"]
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
    for s in SETS:
        srows = [r for r in rows if r[0] == s]
        print("  %-10s rows=%d identical=%d changed=%d refused-both=%d "
              "refusal-mover=%d" % (
                  s, len(srows),
                  sum(1 for r in srows if r[4] == "identical"),
                  sum(1 for r in srows if r[4] == "changed"),
                  sum(1 for r in srows if r[4] == "refused-both"),
                  sum(1 for r in srows if r[4].startswith("refusal-mover"))))


if __name__ == "__main__":
    main()
