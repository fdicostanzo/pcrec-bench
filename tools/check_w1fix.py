"""check_w1fix.py -- [B148] lane b148w1fix (inbox I-170/I-171): the two pre-W1 fixes.

  1. THE DEFINE-ONLY CAPABILITY. cscan and wild-json-validate use
     `(?(DEFINE)...)` and no other conditional, so they require the
     engine-neutral token `conditional-define`, not the general
     `conditionals`. Checked: (a) the two members use no conditional but
     DEFINE (a source scan, with a control that the scan sees a general one);
     (b) the live admission matrix over EVERY (member, testee) equals the
     committed AFTER file; (c) AFTER differs from the frozen BEFORE file in
     exactly 12 admission flips (cscan + wild-json-validate x the six native
     pcrec configs) and 12 refusal-token renames (conditionals ->
     conditional-define on re2/rust/vectorscan and their assist arms), and no
     other cell; (d) the general `conditionals` is still NOT declared by
     pcrec and a synthetic pattern requiring it is still refused (control);
     (e) pcre2 declares both; (f) the verbatim members COMPILE and ANSWER
     through the real adapter against the oracle, on the short subjects.
  2. THE DEEP ARMS' FIRST-TOUCH. `adapters.deep_prime_argv` and the
     `storage_prime` runtime option: argv decisions on synthetic handles
     (with controls), the five deep adapters' real `measure` argv at
     throughput vs search, the marker the option rides on.
No timing: trials 1, iters 1, scratch, `synthetic`.
"""
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "bench", "unusual"))

MEAS = os.path.join(ROOT, "docs", "dev", "measurements")
WORK = os.path.join(ROOT, "build", "check-w1fix")
MEMBERS = ("cscan", "wild-json-validate")
PCREC_NATIVE = ["pcrec-auto", "pcrec-auto-deep", "pcrec-nocaps", "pcrec-vm", "pcrec-vm-deep", "pcrec-vm-in"]
DEEP = ["pcre2-interp-deep", "pcre2-jit-deep", "pcrec-auto-deep", "pcrec-vm-deep", "onig-default-deep"]


def _read(name):
    out = {}
    with open(os.path.join(MEAS, "2026-10-29-b148w1fix-admission-%s.tsv" % name)) as f:
        for l in f:
            if l.startswith("#") or not l.strip():
                continue
            p, t, v = l.rstrip("\n").split("\t")
            out[(p, t)] = v
    return out


def _live(sb):
    from pcrecbench import capability as C
    out = {}
    for t in sorted(C._load_matrix(sb)):
        for p in sb.patterns:
            m = C.missing_capabilities(sb, t, p)
            out[(p.name, t)] = ",".join(sorted(m)) or "ADMIT"
    return out


def run(ok, bad):
    from pcrecbench import capability as C, subbench as _sbm
    sb = _sbm.find("unusual")

    # (a) the members use no conditional but DEFINE
    def general(text):
        return re.findall(r"\(\?\((?!DEFINE\))", text)
    for m in MEMBERS:
        txt = open(os.path.join(ROOT, "bench", "unusual", "patterns", m + ".rx"), encoding="utf-8").read()
        if "(?(DEFINE)" in txt and not general(txt):
            ok("w1fix: %s uses (?(DEFINE) and NO other conditional" % m)
        else:
            bad("w1fix: %s conditionals" % m, repr(general(txt)))
    if general("(?(1)a|b)") and not general("(?(DEFINE) (?<a>x) ) \\A(?&a)"):
        ok("w1fix: CONTROL -- the scan sees a general (?(1)..) and ignores DEFINE")
    else:
        bad("w1fix: conditional scan control")
    pats = {p.name: p for p in sb.patterns}
    for m in MEMBERS:
        r = C.pattern_requires(pats[m])
        if "conditional-define" in r and "conditionals" not in r:
            ok("w1fix: %s requires conditional-define, not conditionals" % m)
        else:
            bad("w1fix: %s requires" % m, repr(sorted(r)))

    # (b)/(c) the admission matrix
    live, before, after = _live(sb), _read("before"), _read("after")
    if live == after:
        ok("w1fix: live admission matrix == committed AFTER (%d cells)" % len(live))
    else:
        bad("w1fix: live matrix drifted from AFTER",
            repr([k for k in live if live[k] != after.get(k)][:5]))
    if set(before) == set(after):
        adm = lambda v: v == "ADMIT"
        flips = sorted(k for k in before if adm(before[k]) != adm(after[k]))
        renames = sorted(k for k in before if before[k] != after[k] and adm(before[k]) == adm(after[k]))
        want_flips = sorted((m, t) for m in MEMBERS for t in PCREC_NATIVE)
        bad_rename = [k for k in renames
                      if before[k].replace("conditionals", "conditional-define") != after[k]]
        if flips == want_flips and all(adm(after[k]) and not adm(before[k]) for k in flips):
            ok("w1fix: exactly %d admission flips, all refused -> ADMIT, all cscan/wild-json-validate x native pcrec"
               % len(flips))
        else:
            bad("w1fix: admission flips", repr(flips))
        if len(renames) == 12 and not bad_rename and all(k[0] in MEMBERS for k in renames):
            ok("w1fix: %d other cells differ ONLY by the refusal token name (conditionals -> conditional-define); "
               "every other of %d cells byte-identical" % (len(renames), len(before) - len(flips) - len(renames)))
        else:
            bad("w1fix: renames", repr(renames[:6] + bad_rename[:3]))
    else:
        bad("w1fix: BEFORE and AFTER cover different cells")

    # (d)/(e) the general token is untouched
    pc, p2 = C.capabilities_for(sb, "pcrec-auto"), C.capabilities_for(sb, "pcre2-jit")
    if "conditional-define" in pc and "conditionals" not in pc:
        ok("w1fix: pcrec declares conditional-define and still NOT conditionals")
    else:
        bad("w1fix: pcrec tokens", repr(sorted(pc)))
    if {"conditional-define", "conditionals"} <= p2:
        ok("w1fix: pcre2-jit declares both (the specific form follows the general one)")
    else:
        bad("w1fix: pcre2 tokens")

    class _P:
        name, tags = "gen-cond", ["requires-conditionals"]
    if C.missing_capabilities(sb, "pcrec-auto", _P) == frozenset({"conditionals"}) \
            and not C.missing_capabilities(sb, "pcre2-jit", _P):
        ok("w1fix: CONTROL -- a pattern requiring general conditionals is still refused on pcrec, admitted on pcre2-jit")
    else:
        bad("w1fix: general conditionals control")

    # (f) real adapter smoke against the oracle
    from pcrecbench import harness as _h
    shutil.rmtree(WORK, ignore_errors=True)
    os.makedirs(WORK, exist_ok=True)
    for t in ("pcrec-auto-deep", "pcrec-vm"):
        try:
            res = _h.run_cell("unusual", t, regimes=["search_short"], trials=1, iters=1, force_unquiet=True,
                              tier="scratch", store_root=os.path.join(WORK, "store-" + t), patterns=list(MEMBERS),
                              synthetic=True, workdir=os.path.join(WORK, "cell-" + t), mem=False)
        except Exception as e:                   # noqa: BLE001
            bad("w1fix: %s through run_cell" % t, str(e)[:300])
            continue
        comp = [r for r in res.rows if r["kind"] == "compile"]
        mrows = [r for r in res.rows if r["kind"] == "match"]
        outs = {}
        for r in mrows:
            outs.setdefault(r["match_outcome"], []).append(r["pattern_id"] + "/" + r["subject_id"])
        okc = comp and all(r.get("outcome", r.get("compile_outcome")) == "compiled" for r in comp)
        # the deep arm answers every short subject; the default arm gives up (named) on the two
        # deepest nests (cs-nest-100, js-deep-arr) and answers the rest
        allowed = {"matched-as-expected"} if t.endswith("deep") else {"matched-as-expected", "gave-up"}
        gave = sorted(outs.get("gave-up", []))
        want_gave = [] if t.endswith("deep") else ["cscan/cs-nest-100", "wild-json-validate/js-deep-arr"]
        if okc and set(outs) <= allowed and gave == want_gave and len(mrows) >= 320:
            ok("w1fix: %s COMPILES both verbatim members and answers %d short-subject rows as the oracle says"
               % (t, len(mrows) - len(gave)), "gave-up (default limits): %s" % (gave or "none"))
        else:
            bad("w1fix: %s smoke" % t, "compiled=%s outcomes=%s" % (bool(okc), {k: len(v) for k, v in outs.items()}))

    _prime(ok, bad)


def _prime(ok, bad):
    from pcrecbench import adapters as _ad
    dp = _ad.deep_prime_argv
    cases = [
        ({"deep": True}, "throughput", ["--prime"]),
        ({"deep": True}, "search", []),                                  # CONTROL: short regime
        ({"deep": True}, "call-stream", []),                             # CONTROL: --prime has no meaning in calls
        ({"deep": False}, "throughput", []),                             # CONTROL: a default arm
        ({}, "throughput", []),
        ({"deep": True, "mem_pass": True}, "throughput", []),            # CONTROL: the untimed canary pass
        ({"deep": True, "prime": True}, "throughput", []),               # not doubled when the harness primed
    ]
    bad_cases = [(h, r, dp(h, r)) for h, r, w in cases if dp(h, r) != w]
    if not bad_cases:
        ok("w1fix: deep_prime_argv -- %d handle/regime cases (1 positive, 6 controls)" % len(cases))
    else:
        bad("w1fix: deep_prime_argv", repr(bad_cases))

    # the five real deep adapters: --prime in the real measure argv
    for t in DEEP:
        try:
            ad, _ = _ad.resolve(t)
            cfg = ad.config(t)
        except Exception as e:                    # noqa: BLE001
            bad("w1fix: %s resolve" % t, str(e)[:200])
            continue
        mod = type(ad).measure.__globals__            # the adapter module's namespace (loaded by path)
        seen = []
        orig = mod["per_trial"]
        mod["per_trial"] = lambda argv, *a, **k: seen.append(list(argv)) or ([], 0, [])
        try:
            h = {"driver": "d", "lib": "l", "pattern_file": "p", "form": "plain", "jit": bool(cfg.get("jit")),
                 "deep": bool(cfg.get("limits")), "buffer_args": [], "utf": False, "callout_args": []}
            for regime in ("throughput", "search"):
                try:
                    ad.measure(h, regime, [], 1, 1)
                except Exception:                 # noqa: BLE001
                    seen.append(["ERR"])
        finally:
            mod["per_trial"] = orig
        has = ["--prime" in a for a in seen]
        if has == [True, False]:
            ok("w1fix: %s measure argv carries --prime at throughput only" % t)
        else:
            bad("w1fix: %s measure argv" % t, repr(seen))
    marks = {}
    for t in DEEP + ["pcrec-auto", "pcrec-vm", "pcre2-jit", "pcre2-interp", "onig-default"]:
        ad, _ = _ad.resolve(t)
        marks[t] = bool(ad.config(t).get("limits"))
    if all(marks[t] for t in DEEP) and not any(v for k, v in marks.items() if k not in DEEP):
        ok("w1fix: CONTROL -- `limits` (the deep marker the option rides on) is set on the five deep arms and no default arm")
    else:
        bad("w1fix: deep marker", repr(marks))
