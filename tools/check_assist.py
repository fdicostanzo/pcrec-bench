"""check_assist.py -- `make check-harness`'s slice for the ASSIST pipeline of
bench/unusual ([B148] lane b148aw; docs/design/unusual_set_v1.md 5, 7.4):
the templates, the runner, `pcrecbench assist-init` / `assist-selftest`, and
the assisted configs (testees/assist/).

Called from tools/selfcheck.py's main() as `check_assist.run(ok, bad)`. A
SMOKE: scratch records under build/, nothing printed is a number. The dummy
assists live under build/check-assist/fx (`$PCRECBENCH_ASSISTS_DIR`), never
under bench/unusual/assists/<member>/.

What it checks, each with its control:
  1. every template x family instantiates, fences valid, the EMPTY assist
     counting <= 10 tokens (tokcount-1), nothing smuggled. CONTROLS: a
     statement put inside an `includes` fence is counted (smuggled); an
     edited fence is reported as drift from the template.
  2. dummy assists (the template unchanged: every call answers `n`), one per
     engine -- C (pcre2, onig, vectorscan), C++ (re2), Rust -- build, count
     and self-test over the PUBLIC sample: exactly the cases whose answer is
     `n` pass and the rest FAIL (the grading is live, not a constant). The
     CLI exits 1 on such a run. A fixture ledger of their rows plus one
     NOT-CAPABLE row (a padded 404-token file) passes `tokcount ledger-check`.
  3. run_cell on re2-default-assist-v01 (scratch): the record is written
     (validator-accepted), `testee.assist` lists the ASSISTED member with the
     counter's numbers, the assisted compile row carries `assist_tokens`, the
     NOT-CAPABLE member is `unsupported-by-declaration` whose declaration_ref
     parses to its count and budget, call-stream rows exist. X50 CONTROL: the
     same record with `testee.assist` removed is rejected BY RULE X50.
  4. the capability rule: an `unusual-<member>` grant admits the member (the
     subsume rule); without it the member's feature tokens are missing; with
     the real (empty) ledger an assisted config is pinned-tier and grants
     nothing, with a fixture dir it is forced scratch.
"""
import contextlib
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

WORK = os.path.join(ROOT, "build", "check-assist")
FX = os.path.join(WORK, "fx")
#: one dummy per engine (all three languages); the NOT-CAPABLE row
DUMMIES = [("co-netstr", "pcre2"), ("va-tenant", "onig"), ("co-luhn", "vectorscan"),
           ("cscan", "re2"), ("co-member", "rust")]
NOT_CAPABLE = ("wild-sexp-balanced", "re2")


@contextlib.contextmanager
def fixture_env():
    old = os.environ.get("PCRECBENCH_ASSISTS_DIR")
    os.environ["PCRECBENCH_ASSISTS_DIR"] = FX
    try:
        yield
    finally:
        if old is None:
            os.environ.pop("PCRECBENCH_ASSISTS_DIR", None)
        else:
            os.environ["PCRECBENCH_ASSISTS_DIR"] = old


def run(ok, bad):
    from pcrecbench import assists as A
    shutil.rmtree(WORK, ignore_errors=True)
    os.makedirs(FX, exist_ok=True)
    _templates(ok, bad, A)
    if not _fixtures(ok, bad, A):
        return
    _selftests(ok, bad, A)
    _cell(ok, bad, A)
    _capability(ok, bad, A)


def _templates(ok, bad, A):
    import tokcount
    worst, n = 0, 0
    for e, spec in A.ENGINES.items():
        for fam in spec["families"]:
            try:
                r = tokcount.count_text(A.instantiate(e, fam), spec["lang"])
            except Exception as ex:                    # noqa: BLE001
                bad("assist template %s/%s instantiates and counts" % (e, fam), str(ex)[:300])
                continue
            n += 1
            worst = max(worst, r["tokens"])
            if r["smuggled"] or r["tokens"] > 10:
                bad("assist template %s/%s: the empty assist counts near zero" % (e, fam),
                    "%d tokens, smuggled %r" % (r["tokens"], r["smuggled"]))
    ok("all %d template x family instantiations: fences valid, nothing smuggled, "
       "the empty assist <= 10 tokens" % n, "worst %d" % worst)
    # CONTROL: a statement inside an `includes` fence is counted
    t = A.instantiate("pcre2", "vars").replace(
        '#include "ub_map.h"\n', '#include "ub_map.h"\nstatic int x = 1;\n', 1)
    r = tokcount.count_text(t, "c")
    if r["smuggled"] and any(s["item"] == "includes" for s in r["smuggled"]):
        ok("CONTROL: a statement smuggled into an `includes` fence is counted",
           "%d tokens" % r["tokens"])
    else:
        bad("CONTROL: smuggling into `includes`", repr(r["smuggled"]))
    # CONTROL: an edited fence is drift from the template
    p = os.path.join(WORK, "drift", "assist.c")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(A.instantiate("pcre2", "vars").replace("cache_drop(void *v)", "cache_drop(void *w)", 1))
    drift = A.fence_drift("va-tenant", "pcre2", p)
    clean = os.path.join(WORK, "drift", "clean.c")
    with open(clean, "w") as f:
        f.write(A.instantiate("pcre2", "vars"))
    if drift and not A.fence_drift("va-tenant", "pcre2", clean):
        ok("CONTROL: an edited fence is reported as drift (the unedited template is not)",
           drift[0][:120])
    else:
        bad("CONTROL: fence drift", "edited %r clean %r" % (drift, A.fence_drift("va-tenant", "pcre2", clean)))


def _fixtures(ok, bad, A):
    import tokcount
    with fixture_env():
        rows = []
        for m, e in DUMMIES:
            path = A.init(m, e)
            rows.append(tokcount.ledger_row(path, m, A.FEATURE[A.family_of(m)], e, "-", "-",
                                            "b148aw-fixture"))
        m, e = NOT_CAPABLE
        t = A.instantiate(e, A.family_of(m)).replace(
            "    return UB_N;\n", "    return " + " + ".join(["0"] * 200) + ";\n", 1)
        path = A.assist_path(m, e)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(t)
        rows.append(tokcount.ledger_row(path, m, A.FEATURE[A.family_of(m)], e, "-", "-",
                                        "b148aw-fixture"))
        with open(os.path.join(A.ASSISTS_DIR, "assists.tsv")) as f:
            head = f.readline()
        with open(os.path.join(FX, "assists.tsv"), "w") as f:
            f.write(head + "".join("\t".join(r) + "\n" for r in rows))
        probs = tokcount.ledger_check(FX)
    verdicts = [r[7] for r in rows]
    if not probs and verdicts.count("ASSISTED") == 5 and verdicts[-1] == "NOT-CAPABLE":
        ok("fixture ledger: 5 ASSISTED dummies + 1 NOT-CAPABLE row agree with the counter "
           "(tokcount ledger-check)", "NOT-CAPABLE at %s tokens" % rows[-1][4])
        return True
    bad("fixture ledger", "; ".join(probs) or repr(verdicts))
    return False


def _selftests(ok, bad, A):
    with fixture_env():
        for m, e in DUMMIES:
            fam = A.family_of(m)
            lines = []
            try:
                passed, n, cnt, drift = A.selftest(m, e, out=lines.append)
            except Exception as ex:                    # noqa: BLE001
                bad("assist-selftest %s/%s (%s) builds and runs" % (m, e, A.ENGINES[e]["lang"]),
                    str(ex)[:400])
                continue
            want = sum(1 for r in A._read_samples(fam) if r["member"] == m
                       and r["expected"] == "n"
                       and (fam == "vars" or r.get("findall") in (None, "", "-", "0")))
            if 0 < passed == want < n and not drift and not cnt["smuggled"]:
                ok("assist-selftest %s/%s (%s): the dummy builds, counts %d tokens, and "
                   "exactly its %d `n` cases of %d pass" % (m, e, A.ENGINES[e]["lang"],
                                                            cnt["tokens"], want, n),
                   lines[-1][:160])
            else:
                bad("assist-selftest %s/%s" % (m, e),
                    "passed %d want %d of %d drift %r" % (passed, want, n, drift))
        _echo(ok, bad, A)
        env = dict(os.environ, PYTHONPATH=ROOT)
        p = subprocess.run([sys.executable, "-m", "pcrecbench", "assist-selftest",
                            "--member", "cscan", "--engine", "re2"], cwd=ROOT, env=env,
                           capture_output=True, text=True, timeout=600)
    tail = (p.stdout.strip().splitlines() or [""])[-1]
    if p.returncode == 1 and "cases pass" in tail and "ASSISTED" in tail:
        ok("CLI: `pcrecbench assist-selftest` exits 1 when a case fails, with the count",
           tail[:160])
    else:
        bad("CLI assist-selftest", "rc %d: %s %s" % (p.returncode, tail, p.stderr[-300:]))


#: (member, engine, the body replacing the template's `UB_N` answer): an ECHO
#: assist answering an EMPTY match at `start` (vars: the whole line)
ECHOES = [("cscan", "re2", "m->s = m->e = m->g1s = m->g1e = (long)start; return UB_M;"),
          ("cscan", "rust", "m.s = start as i64; m.e = m.s; m.g1s = m.s; m.g1e = m.s; UB_M"),
          ("va-term", "onig", "m->s = 0; m->e = (long)n; return UB_M;")]


def _echo(ok, bad, A):
    """CONTROL: the answer path is live -- an assist answering a match gets
    exactly that token back (and find-all its n+1 empty matches)."""
    for m, e, body in ECHOES:
        fam = A.family_of(m)
        t = A.instantiate(e, fam)
        old = "    UB_N\n" if e == "rust" else "    return UB_N;\n"
        assert t.count(old) == 1, (m, e)
        src = os.path.join(WORK, "echo", "%s-%s.%s" % (m, e, A.ENGINES[e]["ext"]))
        os.makedirs(os.path.dirname(src), exist_ok=True)
        with open(src, "w") as f:
            f.write(t.replace(old, "    " + body + "\n"))
        lines = []
        try:
            passed, n, _c, _d = A.selftest(m, e, src=src, out=lines.append)
        except Exception as ex:                        # noqa: BLE001
            bad("CONTROL: echo assist %s/%s" % (m, e), str(ex)[:300])
            continue
        wrong = []
        for r, ln in zip([r for r in A._read_samples(fam) if r["member"] == m], lines):
            subj = bytes.fromhex(r["line_hex" if fam == "vars" else "subject_hex"])
            st = int(r.get("start") or 0)
            want = ("m:0,%d" % len(subj) if fam == "vars" else
                    "m:%d,%d;%d,%d" % (st, st, st, st) if m in A.HAS_G1 else "m:%d,%d" % (st, st))
            got = ln.split("\t")[3]
            if not got.startswith("got " + want) or (
                    fam != "vars" and r.get("findall") not in (None, "", "-")
                    and "findall=%d" % (len(subj) + 1) not in got):
                wrong.append("%s %s want %s" % (r["case"], got, want))
        if not wrong:
            ok("CONTROL: an echo assist %s/%s (%s) gets back exactly the token it answered "
               "on all %d cases" % (m, e, A.ENGINES[e]["lang"], n))
        else:
            bad("CONTROL: echo assist %s/%s" % (m, e), "; ".join(wrong[:3]))


def _cell(ok, bad, A):
    from pcrecbench import capability as C, harness as H
    store_root = os.path.join(WORK, "scratch-store")
    with fixture_env():
        try:
            res = H.run_cell("unusual", "re2-default-assist-v01",
                             regimes=["search_short", "call-stream"], trials=1, iters=1,
                             force_unquiet=True, tier="scratch", store_root=store_root,
                             patterns=["cscan", "wild-sexp-balanced", "floor"],
                             subject_limit=3, synthetic=True,
                             workdir=os.path.join(WORK, "cell"), mem=False)
        except Exception as ex:                        # noqa: BLE001
            bad("run_cell re2-default-assist-v01 (scratch)", str(ex)[-600:])
            return
    t = res.setup["testee"]
    a = t.get("assist") or {}
    comp = {r["pattern_id"]: r for r in res.rows if r["kind"] == "compile"}
    calls = [r for r in res.rows if r["kind"] == "match" and r["regime"] == "call-stream"]
    nc = C.parse_not_capable(comp.get("wild-sexp-balanced", {}).get("declaration_ref"))
    members = [x["member"] for x in a.get("members", [])]
    if (os.path.exists(res.path) and res.setup.get("tier") == "scratch"
            and t["testee_id"].endswith("_assist-v01") and a.get("assist_version") == "v01"
            and members == ["cscan"]
            and comp["cscan"]["compile_outcome"] == "compiled"
            and comp["cscan"]["engine_metadata"].get("assist_tokens") == a["members"][0]["tokens"]
            and comp["wild-sexp-balanced"]["compile_outcome"] == "unsupported-by-declaration"
            and nc == (404, 300) and calls):
        ok("run_cell re2-default-assist-v01: a scratch record written, testee.assist = "
           "[cscan], the NOT-CAPABLE member a declared refusal with its count",
           "%s; %s" % (t["testee_id"], comp["wild-sexp-balanced"]["declaration_ref"][-40:]))
    else:
        bad("run_cell re2-default-assist-v01", json.dumps({
            "tier": res.setup.get("tier"), "id": t.get("testee_id"), "assist": a,
            "compile": {k: v["compile_outcome"] for k, v in comp.items()},
            "not_capable": nc, "calls": len(calls)})[:600])
        return
    # X50 CONTROL: the same record without testee.assist
    with open(res.path) as f:
        recs = [json.loads(line) for line in f]
    head = recs[0]
    (head.get("setup") or head)["testee"].pop("assist", None)
    badp = os.path.join(WORK, "x50-no-assist.jsonl")
    with open(badp, "w") as f:
        f.write("".join(json.dumps(r) + "\n" for r in recs))
    p = subprocess.run([sys.executable, os.path.join(ROOT, "schema", "validate.py"), badp],
                       capture_output=True, text=True, timeout=120)
    if p.returncode != 0 and "[X50]" in (p.stdout + p.stderr):
        ok("CONTROL: the assisted record with testee.assist removed is rejected by X50")
    else:
        bad("CONTROL: X50 on a stripped record", (p.stdout + p.stderr)[-400:])


def _capability(ok, bad, A):
    from pcrecbench import adapters as _ad, capability as C, subbench
    sb = subbench.load(os.path.join(ROOT, "bench", "unusual"))
    p = {x.name: x for x in sb.patterns}["cscan"]
    tid = "re2-default-assist-v01"
    without = C.missing_capabilities(sb, tid, p)
    granted = C.missing_capabilities(sb, tid, p, grants={"unusual-cscan"})
    other = C.missing_capabilities(sb, tid, p, grants={"unusual-co-luhn"})
    if "recursion" in without and not granted and "recursion" in other:
        ok("capability: an `unusual-<member>` grant admits that member alone (subsume rule); "
           "without it the feature is missing", "missing w/o grant: %s" % ", ".join(sorted(without)))
    else:
        bad("capability subsume rule", "%r / %r / %r" % (without, granted, other))
    ad, _cfg = _ad.resolve(tid)
    real = (ad.tier(tid), sorted(ad.capability_grants(tid, sb)))
    with fixture_env():
        fx = (ad.tier(tid), sorted(ad.capability_grants(tid, sb)))
    if real[1] == [] and real[0] == "pinned" and fx == ("scratch", ["unusual-cscan"]):
        ok("the real (empty) ledger grants nothing at the pinned tier; a fixture dir "
           "forces scratch and grants its ASSISTED rows", "fixture %r" % (fx,))
    else:
        bad("assisted config tier/grants", "real %r fixture %r" % (real, fx))


if __name__ == "__main__":
    fails = []
    run(lambda n, d="": print("ok   %s%s" % (n, " -- " + d if d else "")),
        lambda n, d="": (fails.append(n), print("FAIL %s -- %s" % (n, d))))
    sys.exit(1 if fails else 0)
