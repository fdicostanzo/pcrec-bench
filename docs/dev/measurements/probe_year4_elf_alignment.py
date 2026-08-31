#!/usr/bin/env python3
"""probe_year4_elf_alignment.py -- [B22] (f), inbox I-22 (iii): PROVE that
bounded `year4`'s +4,096 B .so step between pins 36d5963 (abi 11) and
96e44c2 (abi 12) is ELF PAGE ALIGNMENT, not emitted code.

THE QUESTION (O-10's control table; the abi-12 ledger 3.2): every other
`selected` DFA artifact of bench/bounded grew +216/+224 B of .so at the
re-pin (the three abi-12 stamp `#define` lines and their comments), with
identical stamps and flat numbers -- `year4` (`\\d{4}`) alone grew
22,480 -> 26,800 plain / 22,624 -> 26,944 whole (+4,320 gross, "+4,096 B
net" in the ledger's wording) with the SAME identical stamp set. I-22
(iii) answered by inference: the .c grew only ~+220 B, and a +4,096 step
with identical stamps is a section crossing a 4 KiB boundary -- "your two
pins' .so files are the evidence". This probe IS that evidence, from the
bench's own side.

THE DERIVATION (no timing, no measurement window -- compile-only facts):
  1. Re-emit `year4` at BOTH pin trees (build/pcrec-36d5963,
     build/pcrec-96e44c2 -- pin.sh's own snapshots), same command shape as
     testees/pcrec/adapter.py (`-p rx --features all -o artifact.c`), and
     count the source both raw (`wc -c`) and by pcrec's own
     comment-excluded rule (adapter.emit_size, the ported
     emit_size_measure) -- the "source-bytes columns" of the store's
     records, re-derived because the abi-11 records predate the
     emit_bytes pair ([B19] added it).
  2. Rebuild each .so exactly as the adapter does ($CC -O2 -std=gnu11
     -fPIC -shared shim.c -DPB_ARTIFACT=...) and check the sizes against
     the store's artifact_bytes for the same cells (22,480 / 26,800
     plain), so the fresh pair is bound to the recorded one.
  3. readelf -lW both .so files: the LOAD segments are aligned 0x1000,
     and the +4,096 appears as ONE segment's file offset stepping a whole
     page while the summed segment CONTENT grew only by the stamp block.

Run from the repo root:  python3 docs/dev/measurements/probe_year4_elf_alignment.py
Output archived verbatim in 2026-08-31-year4-elf-page-alignment.txt.
"""

import importlib.util
import os
import re
import subprocess
import sys

# the repo root this file sits in (docs/dev/measurements/ -> up three);
# the pin BUILDS live in the MAIN tree's build/, resolved separately below.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))


def main_tree_build_root():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        common = subprocess.run(
            ["git", "-C", here, "rev-parse", "--git-common-dir"],
            capture_output=True, text=True, timeout=30).stdout.strip()
        if common:
            if not os.path.isabs(common):
                common = os.path.normpath(os.path.join(here, common))
            return os.path.join(os.path.dirname(common), "build")
    except (OSError, subprocess.SubprocessError):
        pass
    return os.path.join(ROOT, "build")


PINS = ("36d5963", "96e44c2")
PATTERN = r"\d{4}"          # bench/bounded/patterns/year4.rx
WHOLE = r"(?:\d{4})\z"      # record.whole_subject_text's form
STORE_SO = {("36d5963", "plain"): 22480, ("36d5963", "whole-subject"): 22624,
            ("96e44c2", "plain"): 26800, ("96e44c2", "whole-subject"): 26944}


def sh(argv, **kw):
    return subprocess.run(argv, capture_output=True, text=True, timeout=300, **kw)


def emit_size_port():
    spec = importlib.util.spec_from_file_location(
        "pcrec_adapter_for_probe",
        os.path.join(ROOT, "testees", "pcrec", "adapter.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.emit_size


def load_segments(so):
    out = sh(["readelf", "-lW", so]).stdout
    segs = []
    for line in out.splitlines():
        m = re.match(r"\s*LOAD\s+(0x[0-9a-f]+)\s+(0x[0-9a-f]+)\s+0x[0-9a-f]+"
                     r"\s+(0x[0-9a-f]+)\s+(0x[0-9a-f]+)\s+(\S+)\s+(0x[0-9a-f]+)",
                     line)
        if m:
            segs.append({"off": int(m.group(1), 16), "vaddr": int(m.group(2), 16),
                         "filesz": int(m.group(3), 16), "memsz": int(m.group(4), 16),
                         "flags": m.group(5), "align": int(m.group(6), 16)})
    return segs


# The SHIM each record's .so was built with (the shim is half of every
# .so's bytes): the BEFORE sample (bounded@0.1 at 36d5963, store index 50,
# measured 2026-08-30 ~00:xx) predates [B19]'s shim -- its .so was built
# with the [B18]-era shim (commit 4d666dd); the AFTER sample (store 68)
# with [B19]'s (cb169df, which added the pb_engine_sel /
# pb_vm_prefilter_lang* exports). Reproducing the RECORDED bytes therefore
# needs the era-correct shim, extracted from git rather than retyped.
SHIM_ERA = {"36d5963": "4d666dd", "96e44c2": "cb169df"}


def main():
    build_root = main_tree_build_root()
    emit_size = emit_size_port()
    cc = os.environ.get("CC", "gcc")
    print("cc: %s" % sh([cc, "--version"]).stdout.splitlines()[0])
    import tempfile
    tmp = tempfile.mkdtemp(prefix="year4-align-")
    shims = {"current": os.path.join(ROOT, "testees", "pcrec", "shim.c")}
    for pin, rev in SHIM_ERA.items():
        p = sh(["git", "-C", ROOT, "show", "%s:testees/pcrec/shim.c" % rev])
        if p.returncode != 0:
            print("cannot extract shim at %s: %s" % (rev, p.stderr))
            return 1
        path = os.path.join(tmp, "shim-%s.c" % rev)
        with open(path, "w") as f:
            f.write(p.stdout)
        shims[pin] = path
    results = {}
    for pin in PINS:
        pcrec = os.path.join(build_root, "pcrec-%s" % pin, "build", "pcrec")
        if not os.path.exists(pcrec):
            print("MISSING pin build: %s (run testees/pcrec/pin.sh %s first)"
                  % (pcrec, pin))
            return 1
        for form, text in (("plain", PATTERN), ("whole-subject", WHOLE)):
            for shim_name in (pin, "current"):
                d = os.path.join(tmp, "%s-%s-%s" % (pin, form, shim_name))
                os.makedirs(d, exist_ok=True)
                art = os.path.join(d, "artifact.c")
                p = sh([pcrec, "-p", "rx", "--features", "all", "-o", art,
                        "--", text])
                if p.returncode != 0:
                    print("emit failed at %s/%s: %s" % (pin, form, p.stderr))
                    return 1
                files = [art] + ([art[:-2] + ".h"]
                                 if os.path.exists(art[:-2] + ".h") else [])
                raw = sum(os.path.getsize(f) for f in files)
                tot, code = emit_size(files)
                so = os.path.join(d, "artifact-1.so")
                g = sh([cc, "-O2", "-std=gnu11", "-fPIC", "-shared", "-o", so,
                        shims[shim_name], "-DPB_ARTIFACT=\"%s\"" % art,
                        "-I", d])
                if g.returncode != 0:
                    print("gcc failed at %s/%s: %s"
                          % (pin, form, g.stderr[-400:]))
                    return 1
                results[(pin, form, shim_name)] = {
                    "raw": raw, "emit": tot, "code": code,
                    "so": os.path.getsize(so), "segs": load_segments(so)}

    print()
    print("== year4 (\\d{4}): source and .so, era-correct shim per pin ==")
    print("%-10s %-14s %-8s %10s %10s %10s %10s   %s" %
          ("pin", "form", "shim", "raw .c+.h", "emit", "code", ".so",
           "vs the store's artifact_bytes"))
    for (pin, form, shim_name), r in sorted(results.items()):
        rec = STORE_SO[(pin, form)]
        tag = ("== store %d" % rec) if r["so"] == rec else "(store %d)" % rec
        print("%-10s %-14s %-8s %10d %10d %10d %10d   %s"
              % (pin, form, shim_name[:7], r["raw"], r["emit"], r["code"],
                 r["so"], tag))
    print()
    print("== deltas 36d5963 -> 96e44c2, era shims (the store's own pair) ==")
    for form in ("plain", "whole-subject"):
        a = results[("36d5963", form, "36d5963")]
        b = results[("96e44c2", form, "96e44c2")]
        print("%s: raw %+d, emit %+d, code %+d, .so %+d"
              % (form, b["raw"] - a["raw"], b["emit"] - a["emit"],
                 b["code"] - a["code"], b["so"] - a["so"]))
    print()
    print("== the CONTROL: both pins under ONE (current) shim ==")
    for form in ("plain", "whole-subject"):
        a = results[("36d5963", form, "current")]
        b = results[("96e44c2", form, "current")]
        print("%s: emit %+d, .so %+d (of %d)"
              % (form, b["emit"] - a["emit"], b["so"] - a["so"], b["so"]))
    print()
    print("== LOAD segments (readelf -lW), plain form, era shims ==")
    for pin in PINS:
        r = results[(pin, "plain", pin)]
        segs = r["segs"]
        print("%s (shim %s): %d LOAD segments, align %s" %
              (pin, SHIM_ERA[pin], len(segs),
               "/".join(hex(s["align"]) for s in segs)))
        for s in segs:
            end = s["off"] + s["filesz"]
            print("   off 0x%06x  filesz 0x%06x (%6d)  end 0x%06x  %s"
                  % (s["off"], s["filesz"], s["filesz"], end, s["flags"]))
        content = sum(s["filesz"] for s in segs)
        print("   summed LOAD content: %d bytes; file: %d"
              % (content, r["so"]))
    a = results[("36d5963", "plain", "36d5963")]["segs"]
    b = results[("96e44c2", "plain", "96e44c2")]["segs"]
    if len(a) == len(b):
        print()
        print("== per-segment movement (plain), era shims ==")
        for sa, sb in zip(a, b):
            print("   %s: off %+d, filesz %+d"
                  % (sa["flags"], sb["off"] - sa["off"],
                     sb["filesz"] - sa["filesz"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
