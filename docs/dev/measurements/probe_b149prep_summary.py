"""docs/dev/measurements/probe_b149prep_summary.py -- [B149] (lane b149prep,
2026-10-27, inbox I-167): STEP 3 of the compile-only census for the re-pin
614d45eb3 (abi 89) -> cb32eda28 (abi 93). Prints the archive text from the
census TSV (probe_b149prep_census.py) and the raw emits
(probe_b149prep_emit.py).

    python3 docs/dev/measurements/probe_b149prep_summary.py EMITDIR CENSUS.tsv > ARCHIVE.txt
"""
import collections, glob, gzip, os, sys
EMITDIR, CENSUS = sys.argv[1], sys.argv[2]
rows = [l.rstrip("\n").split("\t") for l in open(CENSUS)]
hdr, rows = rows[1], rows[2:]
C = {k: i for i, k in enumerate(hdr)}
print("# [B149] compile-only census, 614d45eb3 (abi 89) -> cb32eda28 (abi 93), %d rows" % len(rows))
print("# every bench pattern x {plain, whole} x {auto-caps, auto-nocaps}; emitted WITH -fcomments,")
print("# --features all (-e utf8 on bench/utf8); arms = cb32eda28 with --memfn=no-window-search,no-window-skip and -fno-req-handoff. Identity: v2/v3")
print("# (tools/program_identity.py); abi 93 is attributed when stripping the trail-gc text restores v3 equality.")
print()
print("== verdicts (v3, per form) ==")
c = collections.Counter((r[C["form"]], r[C["v3"]]) for r in rows)
for k, v in sorted(c.items()):
    print("  %-6s %-22s %d" % (k[0], k[1], v))
print("  v2 identical (all forms): %d of %d compiled-both" % (
    sum(1 for r in rows if r[C["v2"]] == "identical"),
    sum(1 for r in rows if r[C["v2"]] in ("identical", "changed"))))
print()
print("== attribution of every non-identical, non-refused-both row ==")
a = collections.Counter(r[C["attribution"]] for r in rows if r[C["attribution"]] != "-")
for k, v in sorted(a.items()):
    print("  %-26s %d" % (k, v))
print("  UNATTRIBUTED               %d" % a.get("UNATTRIBUTED", 0))
print()
print("== movers (set, pattern, config, form, attribution, signature, stamp moves, old->new bytes:code) ==")
for r in rows:
    if r[C["attribution"]] != "-":
        print("  " + "\t".join([r[C["set"]], r[C["pattern_id"]], r[C["config"]], r[C["form"]],
                               r[C["attribution"]], r[C["v3_signature"]][:70], r[C["stamp_moves"]],
                               "%s -> %s" % (r[C["old_bytes:code"]], r[C["new_bytes:code"]])]))
print()
print("== size books (pcrec's OWN bytes, --warn-emit-bytes=1 probe) ==")
d, dc = collections.Counter(), collections.Counter()
for r in rows:
    if r[C["v3"]] == "identical":
        o, n = r[C["old_bytes:code"]].split(":"), r[C["new_bytes:code"]].split(":")
        d[int(n[0]) - int(o[0])] += 1
        dc[int(n[1]) - int(o[1])] += 1
print("  v3-identical rows: emit_bytes delta histogram %s" % sorted(d.items()))
print("  v3-identical rows: emit_code_bytes delta histogram %s" % sorted(dc.items()))
for att in sorted({r[C["attribution"]] for r in rows if r[C["attribution"]] != "-"}):
    ds = []
    for r in rows:
        if r[C["attribution"]] == att:
            o, n = r[C["old_bytes:code"]].split(":"), r[C["new_bytes:code"]].split(":")
            ds.append((int(n[0]) - int(o[0]), int(n[1]) - int(o[1])))
    if ds:
        print("  %s: n=%d, emit delta min %d max %d, code delta min %d max %d" % (
            att, len(ds), min(x[0] for x in ds), max(x[0] for x in ds),
            min(x[1] for x in ds), max(x[1] for x in ds)))
print()
print("== abi 86 [EMIT-BIDI]: every artifact byte ASCII (the emits carry -fcomments) ==")
cnt = collections.Counter()
for f in glob.glob(os.path.join(EMITDIR, "*.gz")):
    tag = f.rsplit(".", 2)[1]
    b = gzip.open(f, "rb").read()
    cnt[tag, "files"] += 1
    cnt[tag, "non-ascii"] += any(x > 127 for x in b)
for tag in ("old", "new", "arm_noedge"):
    print("  %-10s files %d, files with a byte > 127: %d" % (tag, cnt[tag, "files"], cnt[tag, "non-ascii"]))
print()
print("== abi 87 [SCANEDGE-SET]: scan-edge blocks (`SCAN EDGE:` markers) ==")
go = gn = eo = en = 0
for r in rows:
    if r[C["v2"]] in ("identical", "changed") and r[C["config"]] == "caps":
        key = "%s__%s__%s__%s" % (r[C["set"]].replace("@", "-"), r[C["pattern_id"]], r[C["config"]], r[C["form"]])
        t = {}
        for tag in ("old", "new"):
            p = os.path.join(EMITDIR, "%s.%s.gz" % (key, tag))
            t[tag] = gzip.open(p, "rt", errors="surrogateescape").read().count("SCAN EDGE:")
        eo += t["old"]; en += t["new"]
        gn += t["new"] > t["old"]; go += t["new"] < t["old"]
print("  compiled-both caps rows: %d edge blocks old, %d new; %d rows GAIN edge blocks, %d LOSE any" % (eo, en, gn, go))
