#!/usr/bin/env python3
"""b50predaudit probe 3: the R-PRED rendering quantities."""
import os, sys, collections
ROOT = os.environ.get("PCRECBENCH_ROOT", os.getcwd())  # repoint at a checkout
sys.path.insert(0, ROOT)
from pcrecbench import interpret as I

cat = I.load_catalogue(os.path.join(ROOT, "catalogue/rules.toml"))
known = I.header_keys_from_source()
rule = next(r for r in cat["rule"] if r["id"] == "R-PRED-1")


def run(rep, pred_path, ids):
    report = I.ReportTsv(os.path.join(ROOT, "reports", rep), known)
    preds = I.load_predictions(os.path.join(ROOT, pred_path))
    view = I.RuleView(rule, report, None)
    print(f"\n### {rep}")
    for p in preds:
        label = p["prediction_id"] + p["clause"]
        if label not in ids:
            continue
        vals = I._keyed_values(view, p)
        if not vals:
            print(f"  {label}: no values")
            continue
        reduced, kind = I._reduce(view, p, vals)
        if kind == "set":
            print(f"  {label}: set of {len(reduced[0][1])}")
            continue
        bad = [(l, v) for l, v in reduced if not I._op_holds(p, v)]
        nums = [v for _l, v in reduced]
        rendered = I._measured_text(p, reduced, bad, kind)
        print(f"  {label}  op={p['op']} hi={p['hi']!r}  "
              f"rows={len(vals)} reduced={len(reduced)} "
              f"violations={len(bad)}")
        print(f"     TRUE min={min(nums):.3f}  max={max(nums):.3f}")
        print(f"     RENDERED: {rendered}")
        if bad:
            bnums = [v for _l, v in bad]
            print(f"     violators: min={min(bnums):.3f} max={max(bnums):.3f}"
                  f"  -> the rule labels max-by-|v| 'worst'")


run("2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv",
    "docs/dev/predictions/syntax-0.1-first.tsv",
    {"P2.a", "P7.a", "P7.b", "P13", "P4.a", "P6.c"})
run("2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.tsv",
    "docs/dev/predictions/capability-0.1-first.tsv",
    {"P1.a", "P5.a"})

# --- the metric-mixing hazard under an EXPLICIT section=excluded ---------
print("\n### the `metric` disambiguation hazard (no `metric` selector key)")
report = I.ReportTsv(os.path.join(
    ROOT, "reports",
    "2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.tsv"), known)
view = I.RuleView(rule, report, None)
synthetic = {
    "prediction_id": "SYN", "clause": "", "quantity": "n_gave_up",
    "op": "lte", "lo": "", "hi": "5", "unit": "", "reducer": "identity",
    "_reducer": "identity", "_where": "(synthetic)",
    "_selector": I.parse_selector("section=excluded;regime_or_na=short-subject-search",
                                  "(synthetic)"),
    "source": "-", "source_ref": "-", "stated_utc": "-",
    "subbench": "capability", "version": "0.1", "note": "",
}
rows = I._select(view, synthetic)
by_metric = collections.Counter(r["metric"] for r in rows)
print(f"  explicit `section=excluded`, quantity=n_gave_up: {len(rows)} rows, "
      f"by metric {dict(by_metric)}")
vals = I._keyed_values(view, synthetic)
print("  the values it reduces over (metric -> n_gave_up):")
for (k, v, r) in vals:
    print(f"    metric={r['metric']:16} n_gave_up={v:6.0f}  "
          f"{r['pattern']}/{r['subject_or_na']}/{r['testee']}")

# the same clause WITHOUT an explicit section (the alpha default scoping)
syn2 = dict(synthetic)
syn2["_selector"] = I.parse_selector("regime_or_na=short-subject-search",
                                     "(synthetic)")
rows2 = I._select(view, syn2)
print(f"  same clause with NO explicit section (alpha default): "
      f"{len(rows2)} rows, by metric "
      f"{dict(collections.Counter(r['metric'] for r in rows2))}")
