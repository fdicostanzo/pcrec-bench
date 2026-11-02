# b149monread: compact record loader (streams the jsonl; keeps only what the analyses use). Read-only over store/.
# usage: from recs import load, UNUSUAL_IDS, med ; run from the worktree root.
import glob, json, os, pickle, statistics
P = "pcrec_cb32eda28_"; Q = "pcrec_614d45eb3_"; SIM = "-caps-simdna"
NAMES = {
 "auto": P + "auto" + SIM, "vm": P + "vm" + SIM, "auto614": Q + "auto" + SIM, "vm614": Q + "vm" + SIM,
 "auto_inl": P + "auto" + SIM + "_inline", "vm_inl": P + "vm" + SIM + "_inline",
 "jit_deep": "libpcre2_10.46_jit-caps-simdna_lim-ceil1g", "interp_deep": "libpcre2_10.46_interp-caps-simdna_lim-ceil1g",
 "onig_deep": "oniguruma_6.9.10_default-caps-simdna_lim-ceil1g",
 "auto_in": P + "auto-in" + SIM + "_lim-ceil1g", "vm_in": P + "vm-in" + SIM + "_lim-ceil1g",
}
def path_for(tid, sb="unusual@0.1"):
    fs = sorted(glob.glob(f"store/records/{sb}/{tid}/*.jsonl"))
    return fs
def load_file(f):
    setup = None; comp = {}; match = {}
    for l in open(f):
        d = json.loads(l)
        k = d["kind"]
        if k == "setup": setup = d; continue
        if k == "compile":
            comp.setdefault((d["pattern_id"], d.get("form", "plain")), []).append(
                {x: d.get(x) for x in ("compile_outcome", "diagnostic", "artifact_bytes", "engine_metadata", "cost", "trial")})
        elif k == "match":
            t = d.get("timing") or {}
            match.setdefault((d["pattern_id"], d["regime"], d["subject_id"], d.get("form", "plain")), []).append(
                {"trial": d["trial"], "o": d["match_outcome"], "diag": d.get("diagnostic"),
                 "ns": (t["elapsed_ns"] / t["iterations"]) if t.get("iterations") else None,
                 "it": t.get("iterations"), "bytes": t.get("bytes_processed"),
                 "stream": d.get("stream"), "em": d.get("engine_metadata"), "obs": d.get("observed"), "cl": d.get("consumed_length")})
    return setup, comp, match
def load(name, sb="unusual@0.1", cache="/var/tmp/pcrecbench/b149monread/cache"):
    os.makedirs(cache, exist_ok=True)
    tid = NAMES.get(name, name)
    fs = path_for(tid, sb)
    out = []
    for f in fs:
        c = os.path.join(cache, os.path.basename(f) + ".pkl")
        if os.path.exists(c): out.append(pickle.load(open(c, "rb"))); continue
        r = load_file(f); pickle.dump(r, open(c, "wb")); out.append(r)
    return out
def med(rows):
    v = [r["ns"] for r in rows if r["ns"] is not None]
    return statistics.median(v) if v else None
