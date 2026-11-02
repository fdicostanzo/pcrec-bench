# b149monread: render report groups (reuses scripts/regen_reports.py build()); run from the worktree root.
# usage: python3 <this> <group>   groups: unusual capability syntax sentinel
# store/ is the worktree's own checkout of the committed store (bbc5fb7a); nothing is written to it.
import gc, os, sys, time
ROOT = os.getcwd()
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "scripts"))
os.environ.setdefault("LC_ALL", "C")
from pcrecbench import report
import regen_reports as rr

P = "pcrec_cb32eda28_"; Q = "pcrec_614d45eb3_"
SIM = "-caps-simdna"
UNUSUAL = [P + "auto" + SIM, P + "vm" + SIM, Q + "auto" + SIM, Q + "vm" + SIM,
           P + "auto" + SIM + "_inline", P + "vm" + SIM + "_inline",
           "libpcre2_10.46_jit-caps-simdna_lim-ceil1g", "libpcre2_10.46_interp-caps-simdna_lim-ceil1g",
           "oniguruma_6.9.10_default-caps-simdna_lim-ceil1g",
           P + "auto-in" + SIM + "_lim-ceil1g", P + "vm-in" + SIM + "_lim-ceil1g"]
GROUPS = {
 "unusual": ("unusual", "0.1", "2026-11-02T00:00:00Z", "2026-11-03T00:00:00Z", UNUSUAL, [], "first-cb32eda28"),
 "capability": ("capability", "0.4", "2026-11-01T00:00:00Z", "2026-11-03T00:00:00Z",
                [P + "auto-caps-simdna", P + "auto-caps-simdna_noedge"], [], "noedge-cb32eda28"),
 "syntax": ("syntax", "0.2", "2026-10-28T00:00:00Z", "2026-11-03T00:00:00Z",
            [Q + "auto-caps-simdna", Q + "auto-nocaps-simdna", P + "auto-caps-simdna", P + "auto-nocaps-simdna",
             P + "auto-caps-simdna_noedge"], [], "cb32eda28"),
 "sentinel": ("sentinel", "0.1", "2026-11-02T00:00:00Z", "2026-11-03T00:00:00Z",
              ["libpcre2_10.46_jit-caps-simdna", P + "auto-caps-simdna", Q + "auto-caps-simdna",
               P + "auto-nocaps-simdna"], ["--all-records"], "cb32eda28"),
}
key = sys.argv[1]
sb, ver, SINCE, UNTIL, tests, extra, tag = GROUPS[key]
base = os.path.join(rr.REP, f"2026-11-02-{sb}-{ver}-ryzen7700x-{tag}")
argv = ["--subbench", sb, "--version", ver, "--machine", "ryzen7700x",
        "--since", SINCE, "--until", UNTIL] + extra
for t in tests: argv += ["--testee", t]
t0 = time.time()
def log(m): print(f"{m} ({time.time()-t0:.0f}s)", flush=True)
args, rows = rr.build(argv, "set")
known = {r["testee_id"] for r in rows if r["testee_id"]}
paths = [r["path"] for r in rows if report.index_row_could_match(r, args)]
log(f"{len(paths)} record paths")
loaded = report.load_all(paths, check_filename=True)
log("loaded")
rd, err = report.build_report(loaded, args, known_testee_ids=known)
if err: raise SystemExit(f"ERR {err}")
for suf, fn in ((".tsv", report.render_tsv), (".md", report.render_markdown), (".matrix.tsv", report.render_matrix_tsv)):
    open(base + suf, "w", encoding="utf-8").write(fn(rd)); log("OK " + suf)
del rd; gc.collect()
if key != "sentinel":
    sargs, _ = rr.build(argv, "subject")
    srd, serr = report.build_report(loaded, sargs, known_testee_ids=known)
    if serr: raise SystemExit(f"ERR {serr}")
    open(base + ".subject-grain.md", "w", encoding="utf-8").write(report.render_markdown(srd)); log("OK sg.md")
    open(base + ".subject-grain.tsv", "w", encoding="utf-8").write(report.render_tsv_subject_grain_slice(srd)); log("OK sg.tsv")
    del srd; gc.collect()
if key == "unusual":
    from pcrecbench import report_stream
    stargs, _ = rr.build(argv, "stream")
    sd, e = report_stream.build_stream_report(loaded, stargs, known_testee_ids=known)
    if e: raise SystemExit(f"ERR stream {e}")
    open(base + ".stream.md", "w", encoding="utf-8").write(report_stream.render_stream_markdown(sd)); log("OK stream.md")
    open(base + ".stream.tsv", "w", encoding="utf-8").write(report_stream.render_stream_tsv(sd)); log("OK stream.tsv")
print("GEN DONE", key)
