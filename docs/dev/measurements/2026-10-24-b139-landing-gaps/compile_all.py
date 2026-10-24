#!/usr/bin/env python3
# b139gaps / compile_all.py -- source header (for archiving under docs/dev/measurements/)
# Lane b139gaps (pcrec-bench, 2026-10-24), answering pcrec inbox I-156 (B4 landing gaps).
# COMPILE-ONLY: runs the already-built pin 6b2dbd3e (abi 76) `pcrec` CLI (emit-c) once per
# (set, pattern, config) for the PLAIN form with the exact argv shape the adapter uses
# (testees/pcrec/adapter.py _compile_one: -p rx -fcomments <cfg flags> -o X.c --pattern BYTES,
# LC_ALL=C). No gcc, no timing, no pcrec write. Output: OUT/<cfg>/<set>/<pattern>.c + a manifest.
import os, sys, subprocess, json
sys.path.insert(0, "/home/pcrec/projects/pcrec-bench")
from pcrecbench import subbench
ROOT = "/home/pcrec/projects/pcrec-bench"
PCREC = ROOT + "/build/pcrec-6b2dbd3e/build/pcrec"
OUT = "/var/tmp/pcrecbench/b139gaps/c"
CFG = {"auto": ["--features", "all"],
       "nocaps": ["--features", "all", "--no-captures"],
       "vm": ["--features", "all", "--engine=vm"]}
SETS = ["altwide", "bounded", "capability", "email", "litrun", "loglines", "sentinel", "syntax", "utf8"]
man = []
for s in SETS:
    sb = subbench.load(f"{ROOT}/bench/{s}")
    for p in sb.patterns:
        pb = sb.pattern_bytes(p.name)
        for cfg, fl in CFG.items():
            enc = ["-e", "utf8"] if s == "utf8" else []
            d = f"{OUT}/{cfg}/{s}"; os.makedirs(d, exist_ok=True)
            f = f"{d}/{p.name}.c"
            pr = subprocess.run([PCREC, "-p", "rx", "-fcomments"] + fl + enc + ["-o", f, "--pattern", bytes(pb)],
                                capture_output=True, env={"LC_ALL": "C", "PATH": os.environ["PATH"]}, timeout=120)
            man.append({"set": s, "pattern": p.name, "cfg": cfg, "rc": pr.returncode,
                        "err": pr.stderr.decode("latin-1")[:200] if pr.returncode else ""})
json.dump(man, open(OUT + "/manifest.json", "w"))
print(len(man), "compiles;", sum(1 for m in man if m["rc"]), "refused")
