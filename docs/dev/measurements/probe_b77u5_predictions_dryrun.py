#!/usr/bin/env python3
"""probe_b77u5_predictions_dryrun.py -- [B77] U5, utf8_set_v1.md 11 (F-M2):
the P1-P11 DRY RUN through `pcrecbench interpret`'s own loader and evaluator,
BEFORE any utf8@0.1 cell exists.

Two runs of the REAL CLI (`python3 -m pcrecbench interpret --predictions`):

  (A) NO-OP input: the committed synthetic CLEAN null control
      (catalogue/fixtures/CLEAN__all-measured/). Nothing in it names a utf8
      pattern, so every clause must LOAD (closed sets, selector keys, the
      compile:-selector rule, the median-on-failure refusal) and then read
      `not-evaluable` -- proving the file parses, and nothing more.
  (B) SYNTHETIC input: the CLEAN fixture's own header and record row, plus
      invented rows naming the utf8 patterns/subjects/testees each clause
      selects, valued so that every clause CONFIRMS; and (C) the SAME rows valued to
      VIOLATE each clause, so every clause must REFUTE (P7.a excepted: with
      no did_not_compile row it reads not-evaluable -- its stated residual). This drives the parts
      (A) never reaches -- `ratio_to`'s nested selector parse and join,
      `ratio_max_min_over`, `count` over `did_not_compile`, the grain=subject
      routing -- so a clause that loads but cannot reduce is caught now,
      while the file can still be fixed (the [B72] lesson). The values are
      INVENTED; nothing here is a measurement.

Both runs use the CLEAN fixture's own index (no utf8@0.1 row), so
check_stated_utc / check_testee_globs are vacuous, as they will be before
the first window. Run from the repo root; prints both CLI outputs.
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
FIX = os.path.join(ROOT, "catalogue", "fixtures", "CLEAN__all-measured")
PRED = os.path.join(ROOT, "docs", "dev", "predictions", "utf8-0.1-first.tsv")

PC = ["pcrec_ce658cb7_auto-caps-simdna_utf8",
      "pcrec_ce658cb7_auto-nocaps-simdna_utf8",
      "pcrec_ce658cb7_vm-caps-simdna_utf8",
      "pcrec_ce658cb7_vm-in-caps-simdna_utf8"]
PI = "libpcre2_10.46_interp-caps-simdna_utf8"
PJ = "libpcre2_10.46_jit-caps-simdna_utf8"
RU = "rust_1.13.1_default-caps-simdna"
VS = "vectorscan_5.4.11_block-nosom-nocaps-simd_utf8"
RE = "re2_11.0.0_default-caps-simdna_utf8"
ON = "oniguruma_6.9.10_default-caps-simdna_utf8"
SS, TP = "short-subject-search", "large-subject-throughput"


def rank(p, subj, reg, t, ns, n_wrong=0):
    out = []
    for metric, v in (("median_ns", ns), ("min_ns", ns), ("max_ns", ns),
                      ("stddev_ns", 1.0), ("ratio_vs_baseline", 1.0),
                      ("ratio_vs_best", 1.0)):
        out.append(["rank", p, subj, reg, "plain", "same program", t,
                    "measured", "pinned", "1", metric, "%.6f" % v, "4",
                    "1.0000", "0", str(n_wrong), "", ""])
    return out


def comp(p, t, emit):
    return [["compile", p, "", "", "plain", "same program", t, "", "", "",
             "emit_bytes", "%.6f" % emit, "5", "", "", "", "", ""]]


def dnc(p, t, reg):
    return [["did_not_compile", p, "(set)", reg, "plain", "", t,
             "measured", "pinned", "", "", "", "", "", "", "", "synthetic "
             "refusal", ""]]


def build(tmp, refute=False):
    w = 1 if refute else 0
    with open(os.path.join(FIX, "report.tsv")) as f:
        lines = f.read().splitlines()
    head = [ln for ln in lines if ln.startswith("#") or ln.startswith(
        "section\t") or ln.startswith("record\t")]
    s, g = [], []
    for t in PC:
        s += rank("lit-offset-at-head", "(set)", SS, t, 1000)
        s += rank("lit-offset-at-tail", "(set)", SS, t, 1000 if refute else 3000)
        s += comp("ci-moskva", t, 20000 if refute else 60000)
        s += comp("ci-ascii-control", t, 20000)
        s += comp("prp-l", t, 42000 if refute else 900000)
        for lit, e in (("lit-run-3", 20000), ("lit-mixed-ascii", 21000),
                       ("lit-cyr-run", 22000)):
            s += comp(lit, t, e)
        if not refute:
            s += dnc("prp-han", t, SS)
    for t in PC + [PI]:
        g += rank("lit-run-3", "t-64k-cjk", TP, t, 5e6)
        g += rank("lit-mixed-ascii", "t-64k-cjk", TP, t, 5e6 if refute else 1e6)
        g += rank("lit-run-3", "t-64k-asc", TP, t, 1.0e6)
        g += rank("lit-mixed-ascii", "t-64k-asc", TP, t, 0.3e6 if refute else 1.1e6)
    for t in PC + [PI, PJ, RU, VS]:
        for p in ("ci-moskva", "ci-strasse", "ci-turkish-i", "cls-dot-rep"):
            s += rank(p, "(set)", SS, t, 500, n_wrong=w)
    for t in (PI, PJ):
        for p in ("cls-w-ucp", "cls-d-ucp", "cls-s-ucp", "asr-b-cyr-ucp",
                  "ci-ucp-invariance"):
            s += rank(p, "(set)", SS, t, 500, n_wrong=w)
    for t in (RU, RE, ON, VS):        # P11.a: the Script readers
        s += rank("prp-greek", "(set)", SS, t, 500, n_wrong=1 - w)
    for t in PC + [PI, PJ]:           # P11.b: the Script_Extensions readers
        for p in ("prp-greek", "prp-greek-sc"):
            s += rank(p, "(set)", SS, t, 500, n_wrong=w)
    paths = []
    for name, body in (("report.tsv", s), ("subject.tsv", g)):
        pth = os.path.join(tmp, name)
        with open(pth, "w") as f:
            f.write("\n".join(head + ["\t".join(r) for r in body]) + "\n")
        paths.append(pth)
    return paths


def cli(report, extra):
    cmd = [sys.executable, "-m", "pcrecbench", "interpret", "--index",
           os.path.join(FIX, "index.tsv"), "--predictions", PRED] + extra \
        + [report]
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def main():
    print("== (A) NO-OP input: catalogue/fixtures/CLEAN__all-measured ==")
    rc, out, err = cli(os.path.join(FIX, "report.tsv"),
                       ["--subject-grain", os.path.join(FIX, "report.tsv")])
    print("rc=%d" % rc)
    print("\n".join(ln for ln in out.splitlines() if "R-PRED" in ln))
    print(err.strip())
    with tempfile.TemporaryDirectory() as tmp:
        rep, sub = build(tmp)
        print("\n== (B) SYNTHETIC input (invented values, every clause "
              "valued to confirm) ==")
        rc2, out2, err2 = cli(rep, ["--subject-grain", sub])
        print("rc=%d" % rc2)
        print("\n".join(ln for ln in out2.splitlines() if "R-PRED" in ln))
        print(err2.strip())
    with tempfile.TemporaryDirectory() as tmp:
        rep, sub = build(tmp, refute=True)
        print("\n== (C) SYNTHETIC REFUTING input (the same rows, each valued "
              "to VIOLATE its clause: the clauses are not tautologies) ==")
        rc3, out3, err3 = cli(rep, ["--subject-grain", sub])
        print("rc=%d" % rc3)
        print("\n".join(ln for ln in out3.splitlines() if "R-PRED" in ln
                        and ("clause_verdicts" in ln or "reason" in ln
                             or "no-matching" in ln or "measured" in ln)))
        print(err3.strip())
    return 0 if rc == 0 and rc2 == 0 and rc3 == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
