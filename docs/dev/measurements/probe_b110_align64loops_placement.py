#!/usr/bin/env python3
"""[B110] I-115 Q2 -- the placement twin's compile-side proof: program_sha256
identity between the unaligned and aligned (-falign-functions=64
-falign-loops=64) builds of the SAME pcrec config (auto, auto-nolitrun) at
pin a32bc86e, plus objdump function-address placement facts on the two named
witnesses (wild-secrets-aws-access-key-id, logparse-atomic-removed), plus the
capability@0.1 `ext bench` roster-declaration CENSUS on the two new
`-align64loops` testees (a re-occurrence of O-64/O-65's own roster gap, not
yet ported to these two testees).

Read-only over `store/records/capability@0.1/*/*.jsonl` (the four records
named below) plus the four `build/work/pcrec-auto*/p-<pattern>/plain/t1/`
directories the 2026-09-28 O-65 window (unaligned) and [B110]'s own
06:15-06:58 EDT window (aligned) left on disk -- NOT reproducible standalone
once those build/work directories are cleaned; the .so sha256 values and
objdump excerpts are also archived verbatim in the .txt sibling so the
finding survives a `build/` wipe. No compile, no timing, no store write.

Usage: python3 docs/dev/measurements/probe_b110_align64loops_placement.py
Run from the repo root.
"""
import json
import subprocess
import sys

STORE = {
    "auto": "store/records/capability@0.1/pcrec_a32bc86e_auto-caps-simdna/"
            "capability@0.1__pcrec_a32bc86e_auto-caps-simdna__budu-ryzen1600__20260928T081053Z.jsonl",
    "nolitrun": "store/records/capability@0.1/pcrec_a32bc86e_auto-caps-simdna_nolitrun/"
                "capability@0.1__pcrec_a32bc86e_auto-caps-simdna_nolitrun__budu-ryzen1600__20260928T084613Z.jsonl",
    "auto-aligned": "store/records/capability@0.1/"
                    "pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64/"
                    "capability@0.1__pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64"
                    "__budu-ryzen1600__20260928T101609Z.jsonl",
    "nolitrun-aligned": "store/records/capability@0.1/"
                        "pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64/"
                        "capability@0.1__pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64"
                        "__budu-ryzen1600__20260928T103722Z.jsonl",
}

BUILD_SO = {
    ("auto", "wild-secrets-aws-access-key-id"): "build/work/pcrec-auto/p-wild-secrets-aws-access-key-id/plain/t1/artifact-1.so",
    ("auto-aligned", "wild-secrets-aws-access-key-id"): "build/work/pcrec-auto-align64loops/p-wild-secrets-aws-access-key-id/plain/t1/artifact-1.so",
    ("auto", "logparse-atomic-removed"): "build/work/pcrec-auto/p-logparse-atomic-removed/plain/t1/artifact-1.so",
    ("auto-aligned", "logparse-atomic-removed"): "build/work/pcrec-auto-align64loops/p-logparse-atomic-removed/plain/t1/artifact-1.so",
}

WITNESSES = ["wild-secrets-aws-access-key-id", "logparse-atomic-removed"]


def sh(argv):
    r = subprocess.run(argv, capture_output=True, text=True)
    return r.stdout


def compile_index(path):
    idx = {}
    with open(path) as f:
        for line in f:
            r = json.loads(line)
            if r.get("kind") != "compile" or r.get("trial") != 1:
                continue
            idx[(r["pattern_id"], r.get("form", "plain"))] = r
    return idx


def main():
    idx = {k: compile_index(v) for k, v in STORE.items()}

    print("=" * 78)
    print("PART 1: program_sha256 identity, witness patterns, both forms")
    print("=" * 78)
    for pid in WITNESSES:
        for form in ["plain", "whole-subject"]:
            key = (pid, form)
            print(f"\n{pid} / {form}")
            for arm in ["auto", "nolitrun", "auto-aligned", "nolitrun-aligned"]:
                r = idx[arm].get(key)
                if r is None:
                    print(f"  {arm:20s} MISSING")
                    continue
                em = r.get("engine_metadata", {})
                print(f"  {arm:20s} outcome={r.get('compile_outcome'):10s} "
                      f"program_sha256={em.get('program_sha256')} "
                      f"emit_bytes={em.get('emit_bytes')} "
                      f"vm_program_bytes={em.get('vm_program_bytes')}")

    print()
    print("=" * 78)
    print("PART 2: DFA-null (program-identical) census, aligned vs unaligned")
    print("=" * 78)
    for a, b, label in [("auto", "auto-aligned", "auto vs auto-aligned"),
                         ("nolitrun", "nolitrun-aligned", "nolitrun vs nolitrun-aligned")]:
        keys = set(idx[a]) & set(idx[b])
        same = diff = 0
        diffs = []
        for key in keys:
            ra, rb = idx[a][key], idx[b][key]
            if ra.get("compile_outcome") != "compiled" or rb.get("compile_outcome") != "compiled":
                continue
            pa = ra["engine_metadata"].get("program_sha256")
            pb = rb["engine_metadata"].get("program_sha256")
            if pa == pb:
                same += 1
            else:
                diff += 1
                diffs.append(key)
        print(f"\n{label}: same={same} diff={diff} (of {len(keys)} shared keys)")
        for d in diffs:
            print("  DIFF", d)

    print()
    print("=" * 78)
    print("PART 3: the roster-declaration gap on the two new -align64loops testees")
    print("=" * 78)
    for arm in ["auto-aligned", "nolitrun-aligned"]:
        unsup = [pid for (pid, form), r in idx[arm].items()
                 if r.get("compile_outcome") == "unsupported-by-declaration"]
        print(f"\n{arm}: {len(unsup)} (pattern,form) rows unsupported-by-declaration")
        # one example diagnostic
        for (pid, form), r in idx[arm].items():
            if r.get("compile_outcome") == "unsupported-by-declaration":
                print("  example:", r.get("declaration_ref"))
                break
        print("  affected patterns:", sorted(set(unsup)))

    print()
    print("=" * 78)
    print("PART 4: objdump placement facts (sha256 + function table)")
    print("=" * 78)
    for pid in WITNESSES:
        for arm in ["auto", "auto-aligned"]:
            so = BUILD_SO.get((arm, pid))
            if so is None:
                continue
            sha = sh(["sha256sum", so]).split()[0] if sh(["sha256sum", so]) else "MISSING"
            print(f"\n{pid} / {arm}: {so}")
            print(f"  sha256: {sha}")
            funcs = sh(["objdump", "-d", so])
            for line in funcs.splitlines():
                if line.startswith(tuple("0123456789abcdef")) and "<rx_" in line and "@plt" not in line:
                    print("   ", line)


if __name__ == "__main__":
    main()
