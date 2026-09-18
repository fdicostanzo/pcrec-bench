#!/usr/bin/env python3
"""b50predaudit probe 6: the THIRD predictions file (b51preds' ext-roster,
stated before the next sample) against the audit's findings."""
import os, sys, collections
ROOT = os.environ.get("PCRECBENCH_ROOT", os.getcwd())
sys.path.insert(0, ROOT)
from pcrecbench import interpret as I

cat = I.load_catalogue(os.path.join(ROOT, "catalogue/rules.toml"))
known = I.header_keys_from_source()
rule = next(r for r in cat["rule"] if r["id"] == "R-PRED-1")
rep = I.ReportTsv(os.path.join(
    ROOT, "reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.tsv"),
    known)
view = I.RuleView(rule, rep, None)
preds = I.load_predictions(os.path.join(
    ROOT, "docs/dev/predictions/capability-0.1-ext-roster.tsv"))
print(f"clauses: {len(preds)}")
print()
print("(a) would an (alpha)-dependent clause be NOT-EVALUABLE under the")
print("    pre-(alpha) rank-only default?  [resolved against the pcrec-arm")
print("    report that exists today, substituting a MEASURED testee glob so")
print("    the population is non-empty -- the ext testees have no records yet]")
for p in preds:
    if p["quantity"] not in I._FAILURE_QUANTITIES:
        continue
    q = dict(p)
    # swap the unmeasured ext-roster glob for a measured one, keeping the
    # clause's SHAPE (this is the shape question, not a scoring of P2)
    q["_selector"] = dict(p["_selector"], testee="libpcre2_*_dfa-*")
    alpha = I._select(view, q)
    q2 = dict(q)
    rank_only = I._select(view, q2, sections=["rank"])
    if not alpha and not rank_only:
        continue
    secs = dict(collections.Counter(r["section"] for r in alpha))
    print(f"  {p['prediction_id']}{p['clause']:3} {p['quantity']:10} "
          f"alpha={len(alpha):3} {secs}  rank-only={len(rank_only):3}"
          + ("   <-- (alpha) is what makes it evaluable"
             if alpha and not rank_only else ""))

print()
print("(b) does `subject_or_na=(set)` exclude the P-2 giveup_smallest rows?")
for lit in ("(set)", "*"):
    q = {"quantity": "n_gave_up", "_selector":
         I.parse_selector(f"section=excluded;subject_or_na={lit}", "(syn)"),
         "op": "lte", "lo": "", "hi": "5", "_reducer": "identity",
         "reducer": "identity", "_where": "(syn)", "prediction_id": "SYN",
         "clause": "", "unit": ""}
    rows = I._select(view, q)
    print(f"  subject_or_na={lit:6} -> {len(rows):3} rows, "
          f"{dict(collections.Counter(r['metric'] for r in rows))}")

print()
print("(c) does the base/detail mixing change a `set_of(pattern)` answer?")
for p in preds:
    if p["_reducer"] != "set_of(pattern)":
        continue
    q = dict(p)
    q["_selector"] = dict(p["_selector"], testee="libpcre2_*")
    vals = I._keyed_values(view, q)
    base = {k[0] for k, _v, r in vals if r["metric"] != "giveup_smallest"}
    det = {k[0] for k, _v, r in vals if r["metric"] == "giveup_smallest"}
    print(f"  {p['prediction_id']}{p['clause']:3} base={sorted(base)} "
          f"detail-only-additions={sorted(det - base)}")
    break

print()
print("(d) check_stated_utc / the Q6 testee-glob check: are the ext-roster")
print("    testees measured anywhere in store/index.tsv yet?")
idx = I.IndexTsv(os.path.join(ROOT, "store/index.tsv"))
have = {r["testee_id"] for r in idx.rows}
for glob in sorted({p["_selector"].get("testee", "") for p in preds}):
    if not glob:
        continue
    n = sum(1 for t in have if I._glob_match(glob, t))
    print(f"  {glob:52} matches {n} index testee(s)")
