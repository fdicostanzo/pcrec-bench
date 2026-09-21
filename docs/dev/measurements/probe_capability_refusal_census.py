#!/usr/bin/env python3
"""[B69] THE CAPABILITY REFUSAL CENSUS.

Frank's ruling (plan.md [B69], 2026-09-21 evening, on the
wild-codegrammar-json-number-extended finding): every refusal in
bench/capability@0.1, classified into two cases -- (1) every ATTEMPTING
engine refuses (an instrument-fail candidate: the (?x)-comment-eats-the-
wrapper class docs/design/capability_set_v1.md 3.5 already documents, plus
any other cause found honestly) and (2) a SPLIT refusal (engine-
interesting, with pcrec-refuses-while-others-compile called out
explicitly as pcrec outbox candidates).

Method (no reporter load, no reduction -- the raw per-testee compile
outcomes straight from the store's own JSONL records):

1. Read store/index.tsv; for every testee_id in the 13-testee ROSTER (the
   set the 2026-09-20 fullroster-25b1984f matrix report's own header
   names -- reports/2026-09-20-capability-0.1-budu-ryzen1600-fullroster-
   25b1984f.matrix.tsv line 1) on machine budu-ryzen1600, keep the NEWEST
   record (by the index's own ISO-8601 timestamp column, string-
   comparable).
2. Load each record's JSONL; every `kind == "compile"` row is keyed by
   (pattern_id, form or "plain") -> {outcome: compile_outcome,
   diagnostic, declaration_ref}. A pattern/form/testee triple with no
   compile row at all (a testee that never builds a separate
   whole-subject artifact, or whose plain form was already intercepted
   by policy) is distinguished from one that reached the driver and
   refused.
3. Cross-check the pattern set against bench/capability/patterns.rxt's
   own 64 `name` lines -- every pattern must be accounted for.
4. Classify: `unsupported-by-declaration` is a POLICY DECLARATION, not an
   attempt -- listed separately, never counted as a "refusal" toward
   Frank's two cases. A (pattern, form) with >=1 `did-not-compile` row is
   CASE 1 if every testee that reached the driver on it (its `compiled`
   set is empty) refused; otherwise CASE 2 (split), with the pcrec subset
   flagged.

Run from the pcrec-bench repo root: `python3
docs/dev/measurements/probe_capability_refusal_census.py`
"""
import json
import sys
from pathlib import Path
from collections import defaultdict

REPO = Path.cwd()
assert (REPO / "store" / "index.tsv").exists(), "run from the pcrec-bench repo root"

# The 13-testee roster, copied VERBATIM from the fullroster-25b1984f
# matrix report's own header line (never re-typed from a roster doc):
#   reports/2026-09-20-capability-0.1-budu-ryzen1600-fullroster-25b1984f.matrix.tsv
#   line 1's "testees:" clause.
ROSTER = [
    "libpcre2_10.46_dfa-nocaps-simdna",
    "libpcre2_10.46_interp-caps-simdna",
    "libpcre2_10.46_jit-caps-simdna",
    "oniguruma_6.9.10_default-caps-simdna",
    "pcrec_25b1984f_auto-caps-simdna",
    "pcrec_25b1984f_auto-nocaps-simdna",
    "pcrec_25b1984f_vm-caps-simdna",
    "pcrec_25b1984f_vm-in-caps-simdna",
    "re2_11.0.0_default-caps-simdna",
    "re2_11.0.0_longest-caps-simdna",
    "rust_1.13.1_default-caps-simdna",
    "tre_0.9.0_default-caps-simdna",
    "vectorscan_5.4.11_block-nosom-nocaps-simd",
]
MACHINE = "budu-ryzen1600"
FORMS = ("plain", "whole-subject")


def newest_records():
    newest = {}
    with open(REPO / "store" / "index.tsv") as f:
        header = f.readline().rstrip("\n").split("\t")
        idx = {name: i for i, name in enumerate(header)}
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if parts[idx["subbench"]] != "capability" or parts[idx["version"]] != "0.1":
                continue
            testee = parts[idx["testee_id"]]
            if testee not in ROSTER or parts[idx["machine_id"]] != MACHINE:
                continue
            ts = parts[idx["timestamp"]]
            if testee not in newest or ts > newest[testee][0]:
                newest[testee] = (ts, parts[idx["path"]])
    return newest


def load_compile_cells(newest):
    cells = defaultdict(dict)  # (pattern_id, form) -> testee -> row
    all_patterns = set()
    for testee, (ts, relpath) in newest.items():
        with open(REPO / "store" / relpath) as f:
            for line in f:
                r = json.loads(line)
                if r.get("kind") != "compile":
                    continue
                pid = r["pattern_id"]
                form = r.get("form") or "plain"
                all_patterns.add(pid)
                key = (pid, form)
                if testee not in cells[key]:
                    cells[key][testee] = {
                        "outcome": r.get("compile_outcome"),
                        "diagnostic": r.get("diagnostic"),
                        "declaration_ref": r.get("declaration_ref"),
                    }
    return cells, all_patterns


def main():
    newest = newest_records()
    print("=== 1. newest record per roster testee (store/index.tsv) ===")
    missing = [t for t in ROSTER if t not in newest]
    for t in ROSTER:
        if t in newest:
            print(f"{t}\t{newest[t][0]}\t{newest[t][1]}")
        else:
            print(f"{t}\tMISSING")
    if missing:
        print(f"!! {len(missing)} roster testees have no capability@0.1 record on {MACHINE}: {missing}")

    cells, all_patterns = load_compile_cells(newest)

    print()
    print("=== 2. pattern-set cross-check against bench/capability/patterns.rxt ===")
    rxt_names = []
    with open(REPO / "bench" / "capability" / "patterns.rxt") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("name "):
                rxt_names.append(line[len("name "):].strip())
    print(f"patterns.rxt: {len(rxt_names)} names; compile rows cover {len(all_patterns)} patterns")
    print(f"in patterns.rxt, no compile row anywhere: {sorted(set(rxt_names) - all_patterns)}")
    print(f"in compile rows, not in patterns.rxt: {sorted(all_patterns - set(rxt_names))}")

    print()
    print("=== 3. full (pattern, form) x testee outcome table ===")
    print("pattern\tform\t" + "\t".join(ROSTER))
    for pid in sorted(rxt_names):
        for form in FORMS:
            key = (pid, form)
            if key not in cells:
                continue
            row = []
            for t in ROSTER:
                c = cells[key].get(t)
                row.append(c["outcome"] if c else "NO-ROW")
            print(f"{pid}\t{form}\t" + "\t".join(row))

    print()
    print("=== 4. every non-compiled compile row, verbatim (JSON lines) ===")
    refusal_rows = []
    for pid in sorted(rxt_names):
        for form in FORMS:
            key = (pid, form)
            if key not in cells:
                continue
            for t in ROSTER:
                c = cells[key].get(t)
                if c is None or c["outcome"] == "compiled":
                    continue
                d = {"pattern": pid, "form": form, "testee": t, "outcome": c["outcome"],
                     "diagnostic": c["diagnostic"], "declaration_ref": c["declaration_ref"]}
                refusal_rows.append(d)
                print(json.dumps(d))

    print()
    print("=== 5. accounting ===")
    unsup = [r for r in refusal_rows if r["outcome"] == "unsupported-by-declaration"]
    dnc = [r for r in refusal_rows if r["outcome"] == "did-not-compile"]
    print(f"total non-compiled compile rows: {len(refusal_rows)} "
          f"({len(unsup)} unsupported-by-declaration policy intercepts, "
          f"{len(dnc)} did-not-compile driver refusals)")
    print(f"distinct patterns with >=1 unsup declaration: {len(set(r['pattern'] for r in unsup))}")
    print(f"distinct patterns with >=1 did-not-compile refusal: {len(set(r['pattern'] for r in dnc))}")
    print("did-not-compile rows per testee:")
    per_testee = defaultdict(int)
    for r in dnc:
        per_testee[r["testee"]] += 1
    for t in ROSTER:
        if per_testee.get(t):
            print(f"  {t}: {per_testee[t]}")
    print("unsupported-by-declaration rows per testee:")
    per_testee_u = defaultdict(int)
    for r in unsup:
        per_testee_u[r["testee"]] += 1
    for t in ROSTER:
        if per_testee_u.get(t):
            print(f"  {t}: {per_testee_u[t]}")

    print()
    print("=== 6. CLASSIFICATION (Frank's two cases; unsup rows excluded -- a "
          "declaration is not an attempt) ===")
    # rebuild the full status table for the compiled/refused split
    status = {}
    for key, per in cells.items():
        status[key] = {t: (per[t]["outcome"] if t in per else None) for t in ROSTER}

    dnc_keys = sorted(set((r["pattern"], r["form"]) for r in dnc))
    case1 = []
    case2 = []
    for key in dnc_keys:
        st = status[key]
        refused = [t for t in ROSTER if st[t] == "did-not-compile"]
        compiled = [t for t in ROSTER if st[t] == "compiled"]
        unsup_t = [t for t in ROSTER if st[t] == "unsupported-by-declaration"]
        if not compiled:
            case1.append((key, refused, unsup_t))
        else:
            case2.append((key, refused, compiled, unsup_t))

    print(f"\nCASE 1 -- every ATTEMPTING engine refused ({len(case1)} (pattern,form) rows):")
    for key, refused, unsup_t in case1:
        pid, form = key
        print(f"  {pid} / {form}: refused={refused}")
        print(f"      (declared-unsupported, not an attempt: {unsup_t})")

    print(f"\nCASE 2 -- split refusal ({len(case2)} (pattern,form) rows):")
    for key, refused, compiled, unsup_t in case2:
        pid, form = key
        pcrec_refused = [t for t in refused if t.startswith("pcrec_")]
        flag = " <<< PCREC-REFUSES-WHILE-OTHERS-COMPILE" if pcrec_refused else ""
        print(f"  {pid} / {form}: refused={refused} compiled={compiled}{flag}")
        if unsup_t:
            print(f"      (declared-unsupported, not an attempt: {unsup_t})")


if __name__ == "__main__":
    main()
