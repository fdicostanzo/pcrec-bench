# b152read: render report groups (reuses scripts/regen_reports.py build()); run from the worktree root: gen.py GROUP
import gc, os, sys, time
ROOT = os.getcwd()
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "scripts"))
os.environ.setdefault("LC_ALL", "C")
from pcrecbench import report
import regen_reports as rr

NEW = "pcrec_d6c5e71a5_auto-caps-simdna"
def pair(old): return [f"pcrec_{old}_auto-caps-simdna", NEW]
GROUPS = {
 # name: (subbench, version, testees, extra argv, since, until, suffix)
 "altwide": ("altwide", "0.3", [NEW, "pcrec_d6c5e71a5_vm-caps-simdna", "re2_11.0.0_default-caps-simdna",
             "vectorscan_5.4.11_block-som-nocaps-simd", "rust_1.13.1_default-caps-simdna",
             "libpcre2_10.46_jit-caps-simdna", "libpcre2_10.46_interp-caps-simdna"], [], "2026-10-19T00:00:00Z",
             "2026-11-25T00:00:00Z", "fullroster-d6c5e71a5"),
 "capability": ("capability", "0.4", pair("cb32eda28"), [], "2026-11-01T00:00:00Z", "2026-11-25T00:00:00Z", "d6c5e71a5"),
 "syntax": ("syntax", "0.2", pair("cb32eda28"), [], "2026-11-02T00:00:00Z", "2026-11-25T00:00:00Z", "d6c5e71a5"),
 "bounded": ("bounded", "0.3", pair("9ae59f5d4"), [], "2026-10-26T05:00:00Z", "2026-11-25T00:00:00Z", "d6c5e71a5"),
 "loglines": ("loglines", "0.1", pair("9ae59f5d4"), [], "2026-10-26T02:00:00Z", "2026-11-25T00:00:00Z", "d6c5e71a5"),
 "email": ("email-specimen", "0.2", pair("9ae59f5d4"), [], "2026-10-26T05:30:00Z", "2026-11-25T00:00:00Z", "d6c5e71a5"),
 "litrun": ("litrun", "0.1", pair("9ae59f5d4"), [], "2026-10-26T02:30:00Z", "2026-11-25T00:00:00Z", "d6c5e71a5"),
 "sentinel": ("sentinel", "0.1", ["libpcre2_10.46_jit-caps-simdna", "pcrec_cb32eda28_auto-caps-simdna", NEW],
              ["--all-records"], "2026-11-24T00:00:00Z", "2026-11-25T00:00:00Z", "d6c5e71a5"),
}
key = sys.argv[1]
sb, ver, tests, extra, since, until, suf0 = GROUPS[key]
base = os.path.join(rr.REP, f"2026-11-24-{sb}-{ver}-ryzen7700x-{suf0}")
argv = ["--subbench", sb, "--version", ver, "--machine", "ryzen7700x", "--since", since, "--until", until] + extra
for t in tests: argv += ["--testee", t]
t0 = time.time()
def log(m): print(f"{m} ({time.time()-t0:.0f}s)", flush=True)
args, rows = rr.build(argv, "set")
known = {r["testee_id"] for r in rows if r["testee_id"]}
paths = [r["path"] for r in rows if report.index_row_could_match(r, args)]
log(f"{len(paths)} record paths")
for p in paths: print("  ", p)
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
print("GEN DONE", key)
