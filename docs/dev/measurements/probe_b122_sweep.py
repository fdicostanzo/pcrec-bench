#!/usr/bin/env python3
"""probe_b122_sweep.py -- [B122] lane b122sweep, THE ROUND-1 WIDE MOVER
SWEEP pcrec asked for (round 2 is chosen from this, not from b122read's
spot checks).

READ-ONLY, over two already-committed inputs -- NO compile, NO run, NO
timing, NO store load:

  1. the eight `reports/2026-10-05-*-round1-c4c70f2c.tsv` groups (the
     [B122] round-1 wide window, lane b122read): this script reads their
     `d119` rows (the reporter's OWN per-cell null-control-band
     machinery, `docs/design/null_band_v1.md`/`pcrecbench/nullband.py`)
     and their `null_band` stratum rows -- never `rank`'s raw
     `median_ns` rows, so the arithmetic (medians, IQR, the band) is
     never re-derived, only read back.
  2. `docs/dev/measurements/2026-10-04-b122-census.txt` (lane b122repin):
     the compile-only program-identity + deny-flag ATTRIBUTION census
     fc719ca4 -> c4c70f2c (litrun's own pair is a32bc86e -> c4c70f2c; the
     d119 rows carry the SAME pair per report, read from the report's own
     header, not assumed).

WHY d119, NOT A HAND-ROLLED RULE. The reporter already computes, per set
cross-pin cell, exactly the two things this sweep needs: (a) IDENTITY
(`program_sha256`, schema v1.7, FIELD-first -- `nullband.field_identity`)
and (b) a MOVER THRESHOLD bar = max(IQR%, null-band half-width), where
the null-band half-width over a (regime, baseline-scale) stratum IS the
identical-population's own observed |Delta%| range (`null_band_v1.md`
S3-4). Re-deriving that by hand from `rank` rows would be a second,
weaker implementation of arithmetic this project keeps in exactly one
place (`pcrecbench/CLAUDE.md`'s "Derivations are imported, never
reimplemented" rule) -- and the bar is STRICTLY the brief's own suggested
rule (a changed-program mover must clear the identical population's own
observed range) PLUS the within-window IQR, which the brief did not ask
for but the reporter already carries for free. Both are stated below (THE
RULE) and shown to agree on an outright majority of cells; disagreements
are a REPORTED fact, not swept aside.

THE RULE (stated here, before any table below applies it):
  - THE NULL population per report = every d119 cell whose identity
    (program_sha256 FIELD) reads "identical". Its own R8 verdict
    (`delta_verdict`, the SAME column the brief names as column 18,
    `faster x r` / `slower x r` / `unchanged (within spread)`) may still
    fire faster/slower -- that is cross-window noise BY CONSTRUCTION
    (the program did not change), and its |Delta%| range is the
    threshold.
  - A changed-program cell is a REAL mover iff the reporter's own D119
    bar fires (`value` in {regress, improve}) -- which already requires
    |Delta%| to exceed max(within-window IQR%, the null band's
    half-width for that (regime, scale) stratum). A changed-program cell
    whose bar reads "within" is NOT counted as a real mover even if its
    plain R8 verdict (column 18) says faster/slower -- the null
    population (and the IQR) already explain that much movement.
  - As a SEPARATE, looser cross-check (the brief's own literal wording:
    "outside the identical-program population's ratio range for that
    set/config"), this script also computes, per (set, pcrec-route),
    the identical population's own max |Delta%| and asks whether a
    changed+bar-fired row's |Delta%| exceeds it -- reported as
    `bar_only_real_but_outside_null_range = False` is the interesting
    disagreement case (none expected, since the bar's band term IS that
    quantity restricted to the cell's own stratum; a WIDER, pooled-across
    -strata version of the same test can legitimately disagree, and the
    sweep says how often it does).

Runs from the repo root: `python3 docs/dev/measurements/probe_b122_sweep.py`.
Deterministic: same two input files in, same text out (checked by running
twice and diffing before archiving).
"""
import glob
import hashlib
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
REPORT_GLOB = os.path.join(ROOT, "reports", "2026-10-05-*-round1-c4c70f2c.tsv")
CENSUS_PATH = os.path.join(ROOT, "docs", "dev", "measurements", "2026-10-04-b122-census.txt")

# the four named flagless attributions the census's own header narrative
# states, keyed by (set, pattern_id) -- cross-checked against the census
# TSV's own attribution/dfa_scan_edge columns below, never asserted blind.
NAMED_FLAGLESS = {
    ("capability", "logparse-atomic"): "A1 ([OPT-HYB-RESEED-FORM], vm_reseed adaptive-dense->anchored)",
    ("email-specimen", "factored"): "K78 (DFA dead-group fill relocated search-entry -> success-path)",
    ("utf8", "cls-boundary-range"): "[CLS-TREE] S2 (wide-class interval-vs-table, forced-VM)",
    ("utf8", "cls-neg-allhigh"): "[CLS-TREE] S2 (wide-class interval-vs-table, forced-VM)",
}

SPOT_CLAIMS = [
    # (set, pattern, regime_substr, testee_route, expected_ratio_desc)
    ("utf8", "ci-ascii-control", "large-subject-throughput", "auto", "x2.77 (auto/auto-nocaps)"),
    ("utf8", "ci-ascii-control", "large-subject-throughput", "vm", "x8.38 (forced vm)"),
    ("utf8", "alt-shared-char", "large-subject-throughput", "auto", "x2.06 (both DFA configs)"),
    ("utf8", "alt-shared-char", "large-subject-throughput", "vm", "x1.21 (forced vm)"),
    ("altwide", "clsa-64", None, "vm", "x1.16-x1.37 faster, all 3 regimes"),
    ("altwide", "clsd-64", None, "vm", "x1.16-x1.37 faster, all 3 regimes"),
    ("litrun", None, None, None, "no mover beyond +-1.17x on any pattern/regime"),
    ("syntax", "mod-i", None, None, "K82 fold-family split (slower thr, faster srch on vm)"),
    ("syntax", "mod-r", None, None, "K82 fold-family split"),
    ("syntax", "cls-fold-pair", None, None, "K82 fold-family split"),
    ("syntax", "cls-pair-ctl", None, None, "K82 fold-family split"),
    ("utf8", "ci-strasse", None, None, "K82 fold-family split (auto/auto-nocaps only)"),
]


def sha256_of(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def parse_kv(s):
    out = {}
    for part in (s or "").split("; "):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k] = v
    return out


def load_census(path):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith("set\tpattern_id\t"):
            start = i
            break
    if start is None:
        raise SystemExit("census TSV header not found")
    cols = lines[start].split("\t")
    census = {}
    n_rows = 0
    for ln in lines[start + 1:]:
        if not ln.strip():
            continue
        f = ln.split("\t")
        if len(f) != len(cols):
            continue
        row = dict(zip(cols, f))
        n_rows += 1
        key = (row["set"], row["pattern_id"], row["config"], row["form"])
        census[key] = row
    return census, n_rows


def census_form(report_form):
    return "whole" if report_form == "whole-subject" else "plain"


ROUTE_RE = re.compile(r"^pcrec_[0-9a-f]+_([a-z]+)-")


def census_config(testee_id):
    m = ROUTE_RE.match(testee_id)
    if not m:
        return None
    route = m.group(1)
    return "vm" if route == "vm" else ("auto" if route == "auto" else None)


SLUG_RE = re.compile(r"^pcrec_[0-9a-f]+_(.+)$")


def testee_slug(testee_id):
    """-> the config token after the pin, e.g. 'auto-nocaps-simdna' or
    'vm-caps-simdna_utf8' -- disambiguates auto-caps from auto-nocaps,
    both of which join the census's single 'auto' row."""
    m = SLUG_RE.match(testee_id)
    return m.group(1) if m else testee_id


def named_cause(census_row):
    """-> a human-readable CAUSE string for one census row (identity
    'changed'), derived MECHANICALLY from the census's own columns --
    never invented. The four flagless-named cases are cross-checked
    against the census's own attribution/dfa_scan_edge columns before
    being applied."""
    attr = census_row["attribution"]
    if attr.startswith("restored-by:"):
        return attr[len("restored-by:"):]
    # not-restored-by-round1-denials: name it from the four documented
    # flagless steps, cross-checked against the row's own fields.
    key = (census_row["set"], census_row["pattern_id"])
    if key in NAMED_FLAGLESS:
        return NAMED_FLAGLESS[key]
    if census_row["engine"] == '"dfa"' and census_row["dfa_scan_edge"] == '"range"':
        return "[CLS-TREE] S2 (range spelling, -4 B/test site)"
    return "not-restored-by-round1-denials (unattributed in the census narrative)"


DELTA_VERDICT_RE = re.compile(r"[x×]\s*([0-9.]+)")


def simplify_r8(delta_verdict):
    if "unchanged" in delta_verdict:
        return "unchanged", None
    m = DELTA_VERDICT_RE.search(delta_verdict)
    ratio = float(m.group(1)) if m else None
    if "faster" in delta_verdict:
        return "faster", ratio
    if "slower" in delta_verdict:
        return "slower", ratio
    return delta_verdict.strip() or "n/a", None


def parse_report(path, census):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    lines = text.split("\n")
    header_comment = lines[0]
    m = re.search(r"subbench_versions:\s*([^;]+);", header_comment)
    sb_ver = m.group(1).strip() if m else "?"
    subbench = sb_ver.split("@")[0]
    cols = lines[1].split("\t")
    idx = {c: i for i, c in enumerate(cols)}
    d119 = []
    strata = []
    for ln in lines[2:]:
        if not ln:
            continue
        f = ln.split("\t")
        if len(f) != len(cols):
            continue
        row = dict(zip(cols, f))
        if row["section"] == "d119":
            gus = parse_kv(row["gave_up_summary"])
            testee = row["testee"]
            cfg = census_config(testee)
            form = census_form(row["form"])
            cat_key = (subbench, row["pattern"], cfg, form)
            crow = census.get(cat_key)
            r8_dir, r8_ratio = simplify_r8(row["delta_verdict"])
            bar_verdict_raw = row["value"]
            bar_verdict = bar_verdict_raw.split(" (")[0]  # strip "(IQR only: ...)"
            try:
                delta_pct = float(gus.get("delta_pct", "") or "nan")
            except ValueError:
                delta_pct = float("nan")
            d119.append(dict(
                set=subbench, pattern=row["pattern"], regime=row["regime_or_na"],
                form=row["form"], testee=testee, cfg=cfg,
                identity=gus.get("identity"),
                delta_pct=delta_pct,
                iqr_pct=gus.get("iqr_pct"),
                band_pct=gus.get("band_pct"),
                bar_pct=gus.get("bar_pct"),
                bar_source=gus.get("bar_source"),
                stratum=gus.get("stratum"),
                bar_verdict=bar_verdict,
                bar_verdict_raw=bar_verdict_raw,
                r8_dir=r8_dir, r8_ratio=r8_ratio, r8_raw=row["delta_verdict"],
                census=crow,
            ))
        elif row["section"] == "null_band" and row["metric"] == "band_pct":
            gus = parse_kv(row["gave_up_summary"])
            strata.append(dict(
                set=subbench, regime=row["regime_or_na"], scale=row["subject_or_na"],
                status=gus.get("status"), n=row["n"],
                min_pct=gus.get("min_pct"), median_pct=gus.get("median_pct"),
                max_pct=gus.get("max_pct"),
            ))
    return subbench, d119, strata


def fmt_pct(x):
    try:
        return f"{float(x):+.3f}%"
    except (TypeError, ValueError):
        return str(x)


def main():
    out = []
    p = out.append

    report_paths = sorted(glob.glob(REPORT_GLOB))
    census, n_census_rows = load_census(CENSUS_PATH)

    p("=" * 78)
    p("probe_b122_sweep.py -- [B122] round-1 WIDE MOVER SWEEP, lane b122sweep")
    p("Read-only: no compile, no run, no timing, no store load.")
    p("Inputs (sha256):")
    for rp in report_paths:
        p(f"  {sha256_of(rp)}  {os.path.relpath(rp, ROOT)}")
    p(f"  {sha256_of(CENSUS_PATH)}  {os.path.relpath(CENSUS_PATH, ROOT)}  ({n_census_rows} rows)")
    p("=" * 78)
    p("")
    p(__doc__.split("Runs from the repo root")[0].strip())
    p("")

    all_rows = []
    strata_by_set = defaultdict(list)
    for rp in report_paths:
        sb, rows, strata = parse_report(rp, census)
        all_rows.extend(rows)
        strata_by_set[sb].extend(strata)

    sets = sorted(strata_by_set)

    # ---------------------------------------------------------------- 1.
    p("## 1. null_band strata per set (the reporter's own per-stratum")
    p("   identical-population range -- NOT re-derived, read verbatim)")
    p("")
    for sb in sets:
        p(f"--- {sb} ---")
        for s in sorted(strata_by_set[sb], key=lambda r: (r["regime"], r["scale"])):
            if s["status"] == "ok":
                p(f"  {s['regime']:28s} {s['scale']:10s} n={s['n']:>3s}  "
                  f"min={s['min_pct']:>9s}%  median={s['median_pct']:>9s}%  "
                  f"max(half-width)={s['max_pct']:>9s}%")
            else:
                p(f"  {s['regime']:28s} {s['scale']:10s} n={s['n']:>3s}  status={s['status']}")
    p("")

    # ---------------------------------------------------------------- 2.
    p("## 2. THE NULL: R8 verdict distribution over identity=identical cells")
    p("   (R8 = column 18 delta_verdict, 2x max(stddev) bar; identical =")
    p("   program_sha256 FIELD match both sides -- these movers are")
    p("   cross-window noise BY CONSTRUCTION, never a real pcrec effect)")
    p("")
    p(f"{'set':14s} {'cfg':5s} {'n_identical':>11s} {'r8_unchanged':>12s} "
      f"{'r8_faster':>9s} {'r8_slower':>9s}  max|delta%| of fired cells")
    null_ratio_range = {}  # (set,cfg) -> (min_delta, max_delta) over identical+fired
    for sb in sets:
        for cfg in ("auto", "vm"):
            rows = [r for r in all_rows if r["set"] == sb and r["cfg"] == cfg
                    and r["identity"] == "identical"]
            if not rows:
                continue
            n = len(rows)
            n_unch = sum(1 for r in rows if r["r8_dir"] == "unchanged")
            fired = [r for r in rows if r["r8_dir"] in ("faster", "slower")]
            n_fast = sum(1 for r in fired if r["r8_dir"] == "faster")
            n_slow = len(fired) - n_fast
            if fired:
                deltas = [abs(r["delta_pct"]) for r in fired if r["delta_pct"] == r["delta_pct"]]
                worst = max(deltas) if deltas else float("nan")
                null_ratio_range[(sb, cfg)] = worst
                worst_s = f"{worst:.3f}%"
            else:
                worst_s = "n/a"
            p(f"{sb:14s} {cfg:5s} {n:>11d} {n_unch:>12d} {n_fast:>9d} {n_slow:>9d}  {worst_s}")
    p("")
    p("   Sanity check: every identity=identical d119 row's own D119 bar")
    p("   verdict (column 'value') reads 'null-control' -- confirming the")
    p("   reporter never scores an identical cell against its own band.")
    n_ident = sum(1 for r in all_rows if r["identity"] == "identical")
    n_ident_nullctl = sum(1 for r in all_rows if r["identity"] == "identical"
                           and r["bar_verdict"] == "null-control")
    p(f"   {n_ident_nullctl} of {n_ident} identical rows read null-control "
      f"({'OK' if n_ident_nullctl == n_ident else 'MISMATCH -- see note'}).")
    p("")

    # ---------------------------------------------------------------- 3.
    p("## 3. REAL MOVERS -- ranked, per set, joined to the census cause")
    p("   Rule (stated in the module docstring, applied here verbatim):")
    p("   REAL = identity==changed AND D119 bar in {regress, improve}.")
    p("   (bar = max(within-window IQR%, this cell's own stratum's null")
    p("   half-width from section 1) -- the brief's own suggested test,")
    p("   PLUS the within-window IQR the reporter already carries for")
    p("   free.) Sorted by |delta_pct| descending within each set.")
    p("")
    real_movers = []
    for sb in sets:
        rows = [r for r in all_rows if r["set"] == sb and r["identity"] == "changed"
                and r["bar_verdict"] in ("regress", "improve")]
        rows.sort(key=lambda r: -abs(r["delta_pct"]))
        if not rows:
            p(f"--- {sb}: 0 real movers ---")
            continue
        p(f"--- {sb}: {len(rows)} real mover(s) ---")
        for r in rows:
            cause = named_cause(r["census"]) if r["census"] else "(no census row -- unjoined)"
            p(f"  {r['pattern']:28s} {r['regime']:26s} {r['form']:14s} {testee_slug(r['testee']):20s} "
              f"d={fmt_pct(r['delta_pct']):>10s}  bar={r['bar_verdict']:8s} "
              f"r8={r['r8_dir']}{'' if r['r8_ratio'] is None else ' x'+str(r['r8_ratio'])}  "
              f"cause: {cause}")
        real_movers.extend(rows)
    p("")
    p(f"TOTAL real movers across all 8 sets: {len(real_movers)}")
    p("")

    # ------------------------------------------------------------ 3b cross-check
    p("## 3b. cross-check: the brief's OWN literal rule (|delta_pct| vs the")
    p("    identity=identical population's observed max|delta_pct| for the")
    p("    same (set, route), POOLED across regimes/strata -- a wider,")
    p("    cruder version of the per-stratum band the D119 bar already uses)")
    p("")
    agree = disagree_wider_clears = disagree_bar_only = 0
    for r in [row for row in all_rows if row["identity"] == "changed"]:
        key = (r["set"], r["cfg"])
        null_max = null_ratio_range.get(key)
        bar_real = r["bar_verdict"] in ("regress", "improve")
        if r["delta_pct"] != r["delta_pct"]:  # NaN guard
            continue
        pooled_real = (null_max is None) or (abs(r["delta_pct"]) > null_max)
        if bar_real == pooled_real:
            agree += 1
        elif pooled_real and not bar_real:
            disagree_wider_clears += 1
        else:
            disagree_bar_only += 1
    p(f"  agree: {agree}   D119-bar-only-real (pooled rule says noise): "
      f"{disagree_bar_only}   pooled-rule-only-real (bar says within): "
      f"{disagree_wider_clears}")
    p("  (a 'pooled-rule-only-real' cell is one whose own stratum's null")
    p("  band is wider than the set/route's pooled max -- i.e. the")
    p("  per-stratum reading is the more conservative one on that cell.)")
    p("")

    # ---------------------------------------------------------------- 4.
    p("## 4. REAL MOVERS PER CAUSE -- what round 2 is chosen from")
    p("")
    by_cause = defaultdict(list)
    for r in real_movers:
        cause = named_cause(r["census"]) if r["census"] else "(unjoined)"
        by_cause[cause].append(r)
    for cause in sorted(by_cause, key=lambda c: -len(by_cause[c])):
        rows = by_cause[cause]
        faster = [r for r in rows if r["bar_verdict"] == "improve"]
        slower = [r for r in rows if r["bar_verdict"] == "regress"]
        sets_touched = sorted(set(r["set"] for r in rows))
        p(f"--- cause: {cause} --- ({len(rows)} real mover row(s); "
          f"{len(faster)} improve / {len(slower)} regress; sets: {', '.join(sets_touched)})")
        if faster:
            best = min(faster, key=lambda r: r["delta_pct"])
            p(f"    largest IMPROVE: {best['set']}/{best['pattern']}/{best['regime']}/"
              f"{testee_slug(best['testee'])} d={fmt_pct(best['delta_pct'])} "
              f"(r8 {best['r8_dir']} x{best['r8_ratio']})")
        if slower:
            worst = max(slower, key=lambda r: r["delta_pct"])
            p(f"    largest REGRESS: {worst['set']}/{worst['pattern']}/{worst['regime']}/"
              f"{testee_slug(worst['testee'])} d={fmt_pct(worst['delta_pct'])} "
              f"(r8 {worst['r8_dir']} x{worst['r8_ratio']})")
        p("")

    # ---------------------------------------------------------------- 5.
    p("## 5. unjoined d119 rows (changed-identity, no matching census row)")
    unjoined = [r for r in all_rows if r["identity"] == "changed" and r["census"] is None]
    p(f"   {len(unjoined)} of "
      f"{sum(1 for r in all_rows if r['identity']=='changed')} changed-identity d119 rows "
      f"have no (set, pattern, cfg, form) match in the census.")
    if unjoined:
        seen = set()
        for r in unjoined:
            key = (r["set"], r["pattern"], r["cfg"], r["form"])
            if key in seen:
                continue
            seen.add(key)
            p(f"     {key}")
    p("")

    # ---------------------------------------------------------------- 6.
    p("## 6. reconciliation with b122read's spot claims "
      "(ledger 2026-10-05-b122-round1-wide-c4c70f2c.md SS5-6)")
    p("")
    for sb, pattern, regime_sub, route, claim in SPOT_CLAIMS:
        rows = [r for r in all_rows if r["set"] == sb
                and (pattern is None or r["pattern"] == pattern)
                and (regime_sub is None or regime_sub in r["regime"])
                and (route is None or r["cfg"] == route)]
        if not rows:
            p(f"  [{sb}/{pattern}/{route}] claim={claim!r}: NO ROWS MATCHED (check selector)")
            continue
        real = sorted([r for r in rows if r["identity"] == "changed"
                        and r["bar_verdict"] in ("regress", "improve")],
                       key=lambda r: -abs(r["delta_pct"]))
        fired_ratios = [r["r8_ratio"] for r in rows if r["r8_ratio"] is not None]
        label = f"{sb}/{pattern}" if pattern else sb
        p(f"  [{label}] claim: {claim}")
        if pattern is None:
            # a NEGATIVE/whole-set claim (litrun): the test is whether any
            # fired ratio on ANY matched row, real mover or not, exceeds
            # the stated bound -- never silently narrowed to real movers.
            worst = max(fired_ratios) if fired_ratios else None
            n_real = len(real)
            p(f"      {len(rows)} d119 rows matched; {n_real} real mover(s) "
              f"(bar regress/improve); max r8 ratio over ALL matched rows "
              f"(fired or not): {worst}")
            if n_real:
                p("      real movers (top 5 by |delta_pct|):")
                for r in real[:5]:
                    p(f"        {r['pattern']}/{r['regime']}/{testee_slug(r['testee'])}: "
                      f"r8={r['r8_dir']}{'' if r['r8_ratio'] is None else ' x'+str(r['r8_ratio'])} "
                      f"bar={r['bar_verdict']} d={fmt_pct(r['delta_pct'])}")
            verdict = ("CONFIRMED (max fired ratio stays within the stated bound)"
                       if worst is not None and worst <= 1.17
                       else "REFUTED (a fired ratio exceeds the stated bound)"
                       if worst is not None else "NO FIRED ROWS at all (trivially within)")
            p(f"      -> {verdict}")
        else:
            movers_r8 = [r for r in rows if r["r8_dir"] in ("faster", "slower")]
            verdict = "CONFIRMED (real mover(s) present)" if real else (
                "R8-FIRED BUT NOT A REAL MOVER (identical or within-bar)" if movers_r8
                else "NOT A MOVER on this reading")
            p(f"      -> {verdict}")
            for r in rows:
                p(f"      {r['regime']}/{testee_slug(r['testee'])}: identity={r['identity']} "
                  f"r8={r['r8_dir']}"
                  f"{'' if r['r8_ratio'] is None else ' x'+str(r['r8_ratio'])} bar={r['bar_verdict']} "
                  f"d={fmt_pct(r['delta_pct'])}")
    p("")

    text = "\n".join(out)
    sys.stdout.write(text + "\n")


if __name__ == "__main__":
    main()
