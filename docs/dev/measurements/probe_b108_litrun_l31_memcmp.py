"""docs/dev/measurements/probe_b108_litrun_l31_memcmp.py -- [B108pred]
(lane b108pred, 2026-09-27): whether the REAL pcrec a32bc86e forced-VM
artifact for bench/litrun's own `lit-l31` (a 31-byte exact literal) emits
a `call ... memcmp` on THIS box's toolchain (gcc 15.2.0, x86_64, -O2 --
the project's own phase-2 compile flags), with `lit-l16` as a control at
a length two rungs below.

Why: docs/dev/predictions/litrun-0.1-first.tsv's P5.c names L=31 a WATCH
cell because pcrec's own docs/dev/memcmp_lowering_study.md reports gcc-16
on arm64 calling memcmp() out of line AT L=31 ONLY. The companion probe
docs/dev/measurements/2026-09-27-x86-gcc15-memcmp-lowering.txt already
showed a SYNTHETIC `memcmp(p,q,31)==0` function is fully inlined by this
box's gcc at -O2/-O3 (never at -O1/-Os) -- this probe checks the REAL
artifact rather than a synthetic stand-in, built through the harness's own
`testees/pcrec/adapter.py` compile path (`Adapter._compile_one`, config
`pcrec-vm` -- the forced-VM route bench/litrun's own L-sweep window
measures), so the P4 literal-run collapse (a `pos+L<=n` bounds check plus
one `memcmp`, [OPT-LITSCAN] S2a) is read exactly as pcrec emits it, not
reconstructed by hand.

Run: `python3 docs/dev/measurements/probe_b108_litrun_l31_memcmp.py`
(needs the a32bc86e build already made by lane b108repin at
`build/pcrec-a32bc86e/build/pcrec`; ~2 s, gcc + objdump only). Compile-only,
no timing, no store/report write -- an archived PROBE (pcrec D35 style),
never a ranking input.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from testees.pcrec import adapter as pa  # noqa: E402

PATTERNS = {
    # bench/litrun/patterns/lit-l31.rx, lit-l16.rx -- exact literals,
    # copied verbatim so this probe never depends on cwd-relative reads.
    "lit-l31": b"abcdefghijklmnopqrstuvwxyzABCDE",
    "lit-l16": b"abcdefghijklmnop",
}


def has_memcmp_reference(so_path):
    """True iff the compiled .so calls memcmp anywhere (a PLT/GOT entry,
    checked via `objdump -T`/`readelf -r`) OR the disassembly names it
    directly (statically linked libc, checked via `objdump -d`). Two
    independent checks because which one fires depends on how libc is
    linked on the probing box; either finding a reference is the fact
    that matters."""
    dyn = subprocess.run(["objdump", "-T", so_path], capture_output=True, text=True)
    if "memcmp" in dyn.stdout:
        return True
    reloc = subprocess.run(["readelf", "-r", so_path], capture_output=True, text=True)
    if "memcmp" in reloc.stdout:
        return True
    dis = subprocess.run(["objdump", "-d", so_path], capture_output=True, text=True)
    return "memcmp" in dis.stdout


def main():
    workdir = "/tmp/litrunprobe/objdump_scratch"
    os.makedirs(workdir, exist_ok=True)
    a = pa.Adapter(os.path.join(ROOT, "testees", "pcrec"))
    print("gcc:", subprocess.run(["gcc", "--version"], capture_output=True,
                                 text=True).stdout.splitlines()[0])
    for pid, text in PATTERNS.items():
        res = a._compile_one("pcrec-vm", pid, "plain", text, 1, workdir)
        if res.outcome != "compiled":
            print(pid, "DID NOT COMPILE:", res.diagnostic)
            continue
        so = os.path.join(workdir, "p-" + pid, "plain", "t1", "artifact-1.so")
        found = has_memcmp_reference(so)
        print("%s (L=%d, engine=vm forced, a32bc86e): memcmp reference %s"
              % (pid, len(text), "PRESENT" if found else "ABSENT (fully inlined)"))


if __name__ == "__main__":
    main()
