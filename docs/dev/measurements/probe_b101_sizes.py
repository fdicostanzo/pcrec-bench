"""docs/dev/measurements/probe_b101_sizes.py -- [B101] (lane b101repin,
2026-09-26): the SIZE BOOKS for the ce658cb7 -> 02902356 re-pin MEASURED
per witness and ATTRIBUTED per abi step: each witness is emitted with the
adapter's own phase-1 argv (`-p rx -fcomments <config flags> -o
<dir>/artifact.c --pattern P`, the same basename, so the include line has
the adapter's length) at all five builds (ce658cb7, 27a63314 [K65+K66],
0bb87eda [S1 1-5], 42ee828f [S1 step 6], 02902356), and
testees/pcrec/adapter.py's `emit_size` port (comment-excluded, .c + .h)
is printed per build with the step deltas and the four req/prefilter
stamps at base and tip. No gcc, no timing. From the repo root:

    python3 docs/dev/measurements/probe_b101_sizes.py [WITNESS ...]

WITNESS is `config:set:pattern` (a bench pattern) or `config:=TEXT` (a
literal); config is one of auto / nocaps / vm. With no argument, the
built-in list (every witness check_mechanism_stamps /
check_deny_flag_controls asserted a moved size for, plus controls).
Archived output: docs/dev/measurements/2026-09-26-b101-sizes.txt.
"""
import os, re, subprocess, sys, tempfile
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "testees", "pcrec"))
import importlib.util                                   # noqa: E402
_spec = importlib.util.spec_from_file_location(
    "pcrec_adapter", os.path.join("testees", "pcrec", "adapter.py"))
from pcrecbench import subbench as _sb                  # noqa: E402

SCRATCH = os.environ.get("B101_SCRATCH", "/var/tmp/b101scratch")
PINS = ["ce658cb7", "27a63314", "0bb87eda", "42ee828f", "02902356"]
STEP = ["K65K66", "S1BUILD", "S1STEP6", "TIP"]
BINS = {p: (("/home/duxevents/pcrec-bench/build/pcrec-%s/build/pcrec" % p)
            if p in ("ce658cb7", "02902356")
            else os.path.join(SCRATCH, "pcrec-%s/build/pcrec" % p)) for p in PINS}
CFG = {"auto": ["--features", "all"],
       "nocaps": ["--features", "all", "--no-captures"],
       "vm": ["--features", "all", "--engine=vm"]}
KEYS = ("REQ_WHY", "REQ_BYTE", "REQ_RUN", "DFA_PREFILTER")
STAMP = re.compile(r'^#define RX_(%s) "([^"]*)"$' % "|".join(KEYS), re.M)
DEFAULT = sys.argv[1:] or [
    "vm:=x[ac]y", "vm:=x[@`]y", "vm:=(?i)abc", "vm:=foo|bar",
    "auto:=foo[0-9]+bar", "auto:=^foo[0-9]+bar", "auto:=abc",
    "vm:altwide:pfx3-256", "vm:altwide:w-256",
    "vm:capability:email-nested-plus", "vm:capability:ipv4-near-miss",
    "vm:capability:wild-datetime-moment-iso8601",
    "vm:capability:wild-validator-email-owasp",
    "vm:capability:wild-validator-ipv4-owasp",
    "vm:capability:winpath-near-miss",
    "auto:capability:email-nested-plus", "vm:capability:uuid-near-miss",
]


def emit_size_of(paths):
    mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(mod)
    return mod.emit_size(paths)


_ES = None


def main():
    global _ES
    mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(mod)
    _ES = mod.emit_size
    print("witness\t" + "\t".join(PINS) + "\t" + "\t".join("d_" + s for s in STEP)
          + "\tstamps_base\tstamps_tip")
    for w in DEFAULT:
        cfg, rest = w.split(":", 1)
        if rest.startswith("="):
            pat = rest[1:].encode()
        else:
            setname, name = rest.split(":", 1)
            pat = _sb.find(setname).pattern_bytes(name)
        sizes, stamps = [], {}
        with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
            for pin in PINS:
                d = os.path.join(tmp, pin)
                os.makedirs(d)
                c = os.path.join(d, "artifact.c")
                r = subprocess.run([BINS[pin], "-p", "rx", "-fcomments"] + CFG[cfg]
                                   + ["-o", c, "--pattern", pat],
                                   capture_output=True, timeout=600)
                if r.returncode != 0:
                    sizes.append(None)
                    continue
                sizes.append(_ES([c, c[:-2] + ".h"])[0])
                stamps[pin] = dict(STAMP.findall(open(c, encoding="latin-1").read()))
        deltas = [("%+d" % (b - a)) if a is not None and b is not None else "-"
                  for a, b in zip(sizes, sizes[1:])]

        def fmt(p):
            s = stamps.get(p, {})
            return ",".join("%s=%s" % (k.lower(), s.get(k, "-")) for k in KEYS)
        print("\t".join([w] + [str(s) for s in sizes] + deltas
                        + [fmt("ce658cb7"), fmt("02902356")]), flush=True)


if __name__ == "__main__":
    main()
