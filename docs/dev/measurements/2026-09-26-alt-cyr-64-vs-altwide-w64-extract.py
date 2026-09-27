#!/usr/bin/env python3
"""2026-09-26-alt-cyr-64-vs-altwide-w64-extract.py

Lane b102altctl ([B102] candidate 1 read): quantifies how far the ALREADY
COMMITTED bench/altwide@0.2 records separate "64 branches" from
"Cyrillic/2-byte-per-char" as the cause of bench/utf8's alt-cyr-64 tripping
R4 (script band) and R5 (compile-time cliff) in
docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7-addendum-r2r7.md §8
item 1.

Reads ONLY already-committed files:
  - bench/utf8/patterns.rxt          (alt-cyr-64's own escaped text)
  - bench/utf8/subject_facts.tsv      (t-64k-cyr / t-64k-asc byte/char facts)
  - bench/utf8/expectations.tsv       (alt-cyr-64's own match counts per subject)
  - bench/utf8/pool_cyr.tsv           (the frequency pool alt-cyr-64 draws from)
  - bench/altwide/NOTES.md            (the width ladder's own byte/branch table)
  - bench/altwide/manifest_throughput.tsv (altwide's own subject hit-density design)
  - reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7.tsv        (compile section)
  - reports/2026-09-21-altwide-0.2-budu-ryzen1600-fullroster-25b1984f.tsv (compile section, set-grain)
  - reports/2026-09-21-altwide-0.2-budu-ryzen1600-fullroster-25b1984f.subject-grain.tsv
  - docs/dev/measurements/2026-09-26-utf8-0.1-r2-r7-addendum-extract.txt (R4's own ns/byte numbers, cited not recomputed)
  - store/records/utf8@0.1/pcrec_ce658cb7_auto-caps-simdna_utf8/*.jsonl   (ONE compile row, alt-cyr-64)
  - store/records/altwide@0.2/pcrec_25b1984f_auto-caps-simdna/*.jsonl    (ONE compile row, w-64)

No measurement run. No report rendered. No store index loaded (two single
JSONL files opened directly by path, read to end, closed -- not
store.py's index/load path). Run from the repo root.
"""
import json
import os
import re
import sys
from pathlib import Path

# This lane's own worktree (worktrees/b102altctl) is a SPARSE checkout of
# docs/ only -- the box was at 920 MB free when this lane started (disk-full
# incident, see docs/dev/lanes/b102altctl_report.md), so bench/, store/ and
# reports/ (the read targets below) were never materialized there. ROOT
# therefore points at the main tree, which this lane reads but never writes;
# override with PCRECBENCH_ROOT if reproducing elsewhere.
ROOT = Path(os.environ.get("PCRECBENCH_ROOT", "/home/duxevents/pcrec-bench"))


def load_alt_cyr_64_pattern():
    text = (ROOT / "bench/utf8/patterns.rxt").read_text()
    idx = text.find("name alt-cyr-64")
    start = text.rfind("pattern-esc", 0, idx)
    end = text.find("\n", start)
    line = text[start:end]
    m = re.search(r'pattern-esc "(.*)"', line)
    esc = m.group(1)
    raw = bytes(esc, "utf-8").decode("unicode_escape").encode("latin1")
    return raw


def section1_pattern_shape():
    print("## 1. alt-cyr-64's own shape (bench/utf8/patterns.rxt)\n")
    raw = load_alt_cyr_64_pattern()
    branches = raw.split(b"|")
    lens = [len(b) for b in branches]
    leads = sorted(set(b[0] for b in branches))
    print(f"  total pattern bytes (escaped text decoded): {len(raw)}")
    print(f"  branch count: {len(branches)}")
    print(f"  branch byte lengths: min={min(lens)} max={max(lens)} avg={sum(lens)/len(lens):.3f}")
    print(f"  distinct lead bytes: {[hex(x) for x in leads]} (count {len(leads)})")
    print()


def section2_altwide_ladder():
    print("## 2. bench/altwide@0.2's own width-ladder table (NOTES.md, verbatim rows)\n")
    rows = [
        ("w-8", 8, "4-12", 56, 43, "bitmap"),
        ("w-64", 64, "3-12", 526, 413, "bitmap"),
        ("w-96", 96, "3-12", 804, 624, "bitmap"),
        ("w-128", 128, "3-12", 1056, 809, "bitmap"),
    ]
    for pid, branches, branch_b, byte_total, trie, first_cu in rows:
        print(f"  {pid:8s} branches={branches:<5d} branch_B={branch_b:<6s} bytes={byte_total:<6d} trie_nodes={trie:<6d} first_cu={first_cu}")
    print()
    print("  alt-cyr-64 has 64 branches (== w-64) and 663 pattern bytes, which sits")
    print("  BETWEEN w-64 (526 B) and w-96 (804 B) by total pattern bytes:")
    frac = (663 - 526) / (804 - 526)
    print(f"    (663-526)/(804-526) = {frac:.3f}  -- about halfway from w-64 toward w-96")
    print()


def read_tsv_compile(path, pattern, form="plain"):
    out = {}
    with open(path) as f:
        line = f.readline()
        while line.startswith("#"):
            line = f.readline()
        header = line.rstrip("\n").split("\t")
        idx = {name: i for i, name in enumerate(header)}
        for line in f:
            cols = line.rstrip("\n").split("\t")
            if len(cols) <= idx.get("metric", 0):
                continue
            if cols[idx["section"]] != "compile":
                continue
            if cols[idx["pattern"]] != pattern:
                continue
            if cols[idx["form"]] != form:
                continue
            testee = cols[idx["testee"]]
            metric = cols[idx["metric"]]
            value = cols[idx["value"]]
            out.setdefault(testee, {})[metric] = value
    return out


def section3_compile_axis():
    print("## 3. Compile axis: alt-cyr-64 (ce658cb7, abi 33) vs w-64/w-96 (25b1984f, abi 27)\n")
    print("  CROSS-PIN: alt-cyr-64's pcrec configs are pinned at ce658cb7 (abi 33);")
    print("  altwide's most recent pcrec sample is 25b1984f (abi 27) -- 6 abi steps")
    print("  behind (abi 29 OPT-REQBYTE/-ENDWIN/-ANCHOR-VM, abi 30 OPT-FREQPICK/")
    print("  -REQPOS, abi 31 OPT-PRECHECK-ADMIT's req_why, abi 32 the [VAR] module,")
    print("  abi 33 K64 fix A all land in between). Every ratio below is a")
    print("  cross-pin ratio; labelled, not hidden.\n")

    utf8_tsv = ROOT / "reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7.tsv"
    altwide_tsv = ROOT / "reports/2026-09-21-altwide-0.2-budu-ryzen1600-fullroster-25b1984f.tsv"

    cyr = read_tsv_compile(utf8_tsv, "alt-cyr-64")
    w64 = read_tsv_compile(altwide_tsv, "w-64")
    w96 = read_tsv_compile(altwide_tsv, "w-96")

    # testee name pairs: utf8 side carries a _utf8 suffix on pcrec/pcre2/re2/onig/vectorscan
    pairs = [
        ("libpcre2_10.46_interp-caps-simdna_utf8", "libpcre2_10.46_interp-caps-simdna"),
        ("libpcre2_10.46_jit-caps-simdna_utf8", "libpcre2_10.46_jit-caps-simdna"),
        ("pcrec_ce658cb7_auto-caps-simdna_utf8", "pcrec_25b1984f_auto-caps-simdna"),
        ("pcrec_ce658cb7_auto-nocaps-simdna_utf8", "pcrec_25b1984f_auto-nocaps-simdna"),
        ("pcrec_ce658cb7_vm-caps-simdna_utf8", "pcrec_25b1984f_vm-caps-simdna"),
        ("pcrec_ce658cb7_vm-in-caps-simdna_utf8", "pcrec_25b1984f_vm-in-caps-simdna"),
        ("rust_1.13.1_default-caps-simdna", "rust_1.13.1_default-caps-simdna"),
    ]
    not_on_altwide = [
        "libpcre2_10.46_dfa-nocaps-simdna_utf8",
        "oniguruma_6.9.10_default-caps-simdna_utf8",
        "re2_11.0.0_default-caps-simdna_utf8",
        "vectorscan_5.4.11_block-nosom-nocaps-simd_utf8",
    ]
    print("  testee families with NO altwide@0.2 counterpart at all (never measured on altwide):")
    for t in not_on_altwide:
        print(f"    {t}")
    print()

    print(f"  {'testee (utf8 side)':45s} {'cyr ns':>14s} {'w64 ns':>14s} {'w96 ns':>14s} {'cyr/w64':>9s} {'cyr/w96':>9s}")
    for cyr_id, aw_id in pairs:
        c = cyr.get(cyr_id, {}).get("median_total_ns")
        a64 = w64.get(aw_id, {}).get("median_total_ns")
        a96 = w96.get(aw_id, {}).get("median_total_ns")
        if c is None or a64 is None:
            print(f"  {cyr_id:45s} MISSING")
            continue
        c, a64 = float(c), float(a64)
        r64 = c / a64
        line = f"  {cyr_id:45s} {c:14.1f} {a64:14.1f}"
        if a96 is not None:
            a96 = float(a96)
            r96 = c / a96
            line += f" {a96:14.1f} {r64:9.4f} {r96:9.4f}"
        else:
            line += f" {'n/a':>14s} {r64:9.4f} {'n/a':>9s}"
        print(line)
    print()

    print(f"  {'testee (utf8 side)':45s} {'cyr B':>10s} {'w64 B':>10s} {'w96 B':>10s} {'cyr/w64':>9s} {'cyr/w96':>9s}")
    for cyr_id, aw_id in pairs:
        c = cyr.get(cyr_id, {}).get("artifact_bytes")
        a64 = w64.get(aw_id, {}).get("artifact_bytes")
        a96 = w96.get(aw_id, {}).get("artifact_bytes")
        if c is None or a64 is None:
            continue
        c, a64 = float(c), float(a64)
        r64 = c / a64
        line = f"  {cyr_id:45s} {c:10.0f} {a64:10.0f}"
        if a96 is not None:
            a96 = float(a96)
            r96 = c / a96
            line += f" {a96:10.0f} {r64:9.4f} {r96:9.4f}"
        else:
            line += f" {'n/a':>10s} {r64:9.4f} {'n/a':>9s}"
        print(line)
    print()


def section4_match_density():
    print("## 4. Match axis: hit density, alt-cyr-64/utf8 vs w-64/altwide's own design\n")
    exp_lines = (ROOT / "bench/utf8/expectations.tsv").read_text().splitlines()
    print("  alt-cyr-64's own expectations.tsv rows (throughput regime):")
    for line in exp_lines:
        cols = line.split("\t")
        if cols[0] == "alt-cyr-64" and len(cols) > 2 and cols[2] == "throughput":
            print("   ", "\t".join(cols))
    print()

    facts_lines = (ROOT / "bench/utf8/subject_facts.tsv").read_text().splitlines()
    header = facts_lines[0].split("\t")
    for line in facts_lines[1:]:
        cols = line.split("\t")
        row = dict(zip(header, cols))
        if row["id"] in ("t-64k-cyr", "t-64k-asc"):
            print(f"  {row['id']}: len={row['len']} n_chars={row['n_chars']} pct_multibyte={row['pct_multibyte']} dominant_lead={row['dominant_lead']}")
    print()

    print("  bench/altwide@0.2's own throughput subjects (manifest_throughput.tsv, first 4 rows):")
    manifest = (ROOT / "bench/altwide/manifest_throughput.tsv").read_text().splitlines()
    for line in manifest[:5]:
        print("   ", line)
    print()
    print("  alt-cyr-64 on t-64k-cyr: 2996 non-overlapping matches / 65536 B")
    print(f"    = 1 hit per {65536/2996:.1f} bytes (natural word-frequency density)")
    print("  altwide's OWN densest throughput subject at 128 KiB (t-128k-dense):")
    print("    1024 hits / 131072 B = 1 hit per 128.0 bytes -- 5.8x SPARSER than")
    print("    alt-cyr-64's natural Cyrillic density, and every altwide subject is")
    print("    pure ASCII (no byte >= 0x80 anywhere in the corpus).")
    print()

    pool = (ROOT / "bench/utf8/pool_cyr.tsv").read_text().splitlines()
    print(f"  bench/utf8/pool_cyr.tsv: {len(pool)-1} words (header + {len(pool)-1} entries);")
    print("  alt-cyr-64's 64 branches are drawn from this SAME high-frequency word")
    print("  pool used to GENERATE t-64k-cyr's running Russian prose -- the pattern")
    print("  is not a random 64-branch sample, it is (a subset of) the corpus's own")
    print("  vocabulary, which is why its hit density on t-64k-cyr is so high.")
    print()


def read_one_compile_row(jsonl_path, pattern_id):
    with open(jsonl_path) as f:
        for line in f:
            r = json.loads(line)
            if r.get("pattern_id") == pattern_id and r.get("kind") == "compile":
                return r
    return None


def section5_mechanism_stamps():
    print("## 5. Mechanism: ONE compile row each, read directly (no store index)\n")
    cyr_path = ROOT / "store/records/utf8@0.1/pcrec_ce658cb7_auto-caps-simdna_utf8/utf8@0.1__pcrec_ce658cb7_auto-caps-simdna_utf8__budu-ryzen1600__20260926T050657Z.jsonl"
    w64_path = ROOT / "store/records/altwide@0.2/pcrec_25b1984f_auto-caps-simdna/altwide@0.2__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260921T053254Z.jsonl"
    cyr_row = read_one_compile_row(cyr_path, "alt-cyr-64")
    w64_row = read_one_compile_row(w64_path, "w-64")
    keys = ["abi", "engine", "engine_sel", "dfa_prefilter", "dfa_prefilter_offsets",
            "dfa_scan_edge", "scan_edges", "req_byte", "req_run", "req_why", "dfa_table"]
    print(f"  {'field':22s} {'alt-cyr-64 (ce658cb7/abi33)':30s} {'w-64 (25b1984f/abi27)'}")
    for k in keys:
        cv = cyr_row["engine_metadata"].get(k, "<absent, pre-dates this abi>")
        wv = w64_row["engine_metadata"].get(k, "<absent, pre-dates this abi>")
        print(f"  {k:22s} {str(cv):30s} {str(wv)}")
    print()
    print("  NOTE: w-64's record predates req_byte/req_run/req_why (introduced")
    print("  abi 29/31) entirely -- their 'absent' above is an abi-vintage gap, not")
    print("  a stamped value, and is NOT comparable to alt-cyr-64's 'none'.")
    print()


def section6_floor_comparison():
    print("## 6. The one no-hit-background comparison that DOES exist, and why it")
    print("   points the OPPOSITE way from R4's ratio\n")
    print("  alt-cyr-64 on t-64k-asc (pure ASCII, 0 possible hits -- cited from")
    print("  docs/dev/measurements/2026-09-26-utf8-0.1-r2-r7-addendum-extract.txt")
    print("  lines 206/222, not recomputed here):")
    print("    libpcre2-dfa    : 1.327585 ns/B")
    print("    libpcre2-interp : 1.334520 ns/B")
    print()

    subj_tsv = ROOT / "reports/2026-09-21-altwide-0.2-budu-ryzen1600-fullroster-25b1984f.subject-grain.tsv"
    print("  w-64 on t-128k-clean (pure run/prose, 0 branch occurrences), 131072 B,")
    print("  ns/byte = median_ns / 131072 (this report has no ns_per_byte column,")
    print("  computed here from the same 'rank'/median_ns row the report prints):")
    with open(subj_tsv) as f:
        line = f.readline()
        while line.startswith("#"):
            line = f.readline()
        header = line.rstrip("\n").split("\t")
        idx = {n: i for i, n in enumerate(header)}
        for line in f:
            cols = line.rstrip("\n").split("\t")
            if len(cols) <= idx["metric"]:
                continue
            if (cols[idx["section"]] == "rank" and cols[idx["pattern"]] == "w-64"
                    and cols[idx["subject_or_na"]] == "t-128k-clean"
                    and cols[idx["metric"]] == "median_ns"):
                ns = float(cols[idx["value"]])
                print(f"    {cols[idx['testee']]:40s} {ns/131072:.6f} ns/B  ({ns:.1f} ns total)")
    print()
    print("  So on their respective all-miss backgrounds, alt-cyr-64 (2 lead bytes,")
    print("  0xd0/0xd1, IMPOSSIBLE in ASCII text) is ~2-3 orders of magnitude")
    print("  CHEAPER per byte than w-64 (26-letter bitmap, common in English prose)")
    print("  on libpcre2-interp -- the opposite direction from R4's ×420/×228. This")
    print("  is explained by candidate-start SELECTIVITY (2 possible lead bytes vs")
    print("  26), not by Cyrillic-vs-ASCII per se; altwide's own sh1-*(1 lead byte)/")
    print("  nar4-*(4)/w-*(26) structure-arm family already brackets this axis, so a")
    print("  same-branch-count ASCII control at exactly 2 lead bytes would land")
    print("  INSIDE that already-charted family, not open new machinery.")
    print()


if __name__ == "__main__":
    section1_pattern_shape()
    section2_altwide_ladder()
    section3_compile_axis()
    section4_match_density()
    section5_mechanism_stamps()
    section6_floor_comparison()
