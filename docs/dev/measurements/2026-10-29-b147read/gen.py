# b147read: render report groups (reuses scripts/regen_reports.py build()); run from the worktree root.
import gc, os, sys, time
ROOT = os.getcwd()
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "scripts"))
os.environ.setdefault("LC_ALL", "C")
from pcrecbench import report
import regen_reports as rr

SINCE, UNTIL = "2026-10-28T12:00:00Z", "2026-10-29T03:00:00Z"
def ids(pin, sets): return [f"pcrec_{pin}_{s}" for s in sets]
C = ["auto-caps-simdna", "auto-nocaps-simdna"]
GROUPS = {
 "capability": ("capability", "0.3", ids("9ae59f5d4", C) + ids("614d45eb3", C), []),
 "syntax": ("syntax", "0.2", ids("614d45eb3", C), []),
 "sentinel": ("sentinel", "0.1", ["libpcre2_10.46_jit-caps-simdna", "pcrec_9ae59f5d4_auto-caps-simdna",
              "pcrec_614d45eb3_auto-caps-simdna", "pcrec_614d45eb3_auto-nocaps-simdna"], ["--all-records"]),
}
key = sys.argv[1]
sb, ver, tests, extra = GROUPS[key]
base = os.path.join(rr.REP, f"2026-10-29-{sb}-{ver}-ryzen7700x-first-614d45eb3")
argv = ["--subbench", sb, "--version", ver, "--machine", "ryzen7700x", "--since", SINCE, "--until", UNTIL] + extra
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
print("GEN DONE", key)
