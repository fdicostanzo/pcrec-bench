# b149monread an11: per-record window quality (setup row only): status, load before/after, occupancy before/after, trial agreement.
import glob, json, re
rows = []
for f in sorted(glob.glob("store/records/*/*/*__ryzen7700x__20261102T*.jsonl")):
    s = json.loads(open(f).readline())
    e = s["environment"]; occ = e.get("occupancy", {})
    ta = s.get("trial_agreement", {})
    b, a = occ.get("before", {}), occ.get("after", {})
    rows.append((s["run"]["timestamp"] if "run" in s else "", s["subbench"]["id"], s["testee"]["testee_id"], s["status"], e["load"]["before"]["load1"], e["load"]["after"]["load1"],
                 b.get("max_busy_pct"), b.get("target_busy_pct"), b.get("verdict"), a.get("max_busy_pct"), a.get("verdict"), ta.get("verdict") or ta.get("result") or str(ta)[:40], s.get("tier")))
for r in sorted(rows): print(" ".join(str(x) for x in r))
