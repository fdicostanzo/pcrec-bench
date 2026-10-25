"""check_subst.py -- `make check-harness`'s slice for bench/subst ([B140]).

Called from tools/selfcheck.py's main() as `check_subst.run(ok, bad)` (the
two reporting callbacks selfcheck owns), kept in its own module so the set's
checks land beside the set's files instead of in a 17,000-line file.

Everything here is LIGHT: the small subject (17,500 lines, ~4 MB) only. The
320 MB `acc-main` is never read by `make check`; its sha256 and expectations
are verified by `bench/subst/gen_subjects.py --check --full` and
`gen_expectations.py --check --full`.

What it checks, each with its control:
  1. the IR parser: bad escape / unbalanced cond / else outside a cond /
     unknown segment are each REFUSED BY NAME; a good template round-trips
     through `evaluate`;
  2. the HOSTILE-TEMPLATE test (design 5.2: "the way KB-1's test was"): one
     template full of the characters every dialect treats specially
     (`$ \\ & / @ : } {`, quotes, tab, newline, a high byte, and the
     two characters `\\U`) is rendered to every dialect whose engine this
     box has -- libpcre2, python `re`, GNU sed, perl -- run on a tiny
     subject, and the output must equal the IR's own reference meaning
     (`evaluate`). The CONTROL: the same lit text rendered with the
     dialect's escaper REMOVED must NOT produce that output (so the test
     is shown able to fail);
  3. the dialects without an engine here (rust, sd, rg, re2): the rendered
     bytes asserted as strings, and every `unsupported` construct raising
     its closed token;
  4. libpcre2's SUBSTITUTE_EXTENDED conditional, nested, with an UNSET group
     in the not-taken branch and no UNSET_EMPTY flag (an unguarded unset
     reference is the -55 error, raised);
  5. the case files: cases.tsv against the directories, one-line patterns,
     templates parse, ERE cases free of `(?` and of PCRE-only escapes,
     no unguarded optional-group references;
  6. the generator reproduces manifest.tsv + planted.tsv and the
     calibration PASSES (or is skipped BY NAME when the reference is absent);
  7. the expectations re-derive from the oracle on the small subject, each
     agreeing with its oracle-independent count;
  8. the system tools that exist on this box (GNU sed -E, perl, python re)
     run the cases they can express on the small subject and their output
     sha256 equals the oracle's -- or they refuse the pattern syntax, as
     divergences.tsv says (rows with basis `verified-small`).
  9. ([B140] step 3) THE LIBRARY-TIER DRIVER AND HARNESS, pcre2 first: the
     driver's `--mode subst` on acc-small, all 8 cases, for pcre2-interp,
     pcre2-jit and both `-sizefirst` arms, every output sha256 equal to
     expectations.tsv (driver called directly -- no harness code in the
     verdict); the harness path (`run_cell`) writes a schema-1.9 record the
     validator accepts whose every row is `matched-as-expected` / gate
     `agrees` with the expectation's hash; a deliberately WRONG template
     FAILS the gate BY NAME with the first differing byte and is not timed;
     a trial-2 length difference is a DETERMINISM FAULT by name; an
     unsupported (testee, case) is a compile row `unsupported-by-declaration`
     and no match rows; the refusals (a sizefirst arm on a non-substitution
     set, a testee with no substitution call, --find-all in --mode subst,
     a table that disagrees with the renderer) each fire BY NAME.
 10. ([B140] step 3, continued, lane b140drv2) THE RUST AND RE2 DRIVERS: for
     rust-default (`regex::bytes::Regex::replace_all`, unicode(false)) and
     re2-default (`RE2::GlobalReplace` on a fresh subject copy) the driver
     called DIRECTLY on acc-small, every RUNNABLE case's output sha256 +
     count + length equal to expectations.tsv (no harness code in the
     verdict); the cases divergences.tsv declares unsupported (6 case change,
     7 lookahead/backreference/conditional) rendered as `unsupported-by-
     declaration` compile rows through `run_cell` with a schema-1.9 record
     the validator accepts and NO match rows for them, the runnable six
     gated `agrees`; the drivers' own refusals by name; a testee config the
     charter does not cover (re2-longest) refused by name; and the pattern-
     level `unsupported:pattern-syntax` row accepted beside the renderer's
     own (different) template token.
 11. ([B140] step 4, lane b140tools) THE TOOLS TIER: GNU sed -E, perl -p, the
     python whole-file re.sub script, sd 1.1.0 and `rg --passthru -r` on
     acc-small. For every (tool, case) divergences.tsv does not declare
     unsupported (32 pairs) the UNTIMED pass's output sha256 + length equal
     expectations.tsv (judged here by hashlib); one TIMED `tool | wc -c` per
     tool whose count equals out_bytes with the input 100 % page-cache
     resident and wc on another core; a SABOTAGED sink (prints 7) fails BY
     NAME (`SINK MISMATCH`) with the unsabotaged two-trial call as the
     control; the pins (a wrong sd sha256, a changed sed version) refuse by
     name; and `run_cell` per tool writes a schema-1.9 `process` record the
     validator accepts (X38-X40), with no compile row for a compiled case and
     an `unsupported-by-declaration` row for each declared one.
 12. ([B140] step 3, last driver, lane b140pcrec) THE pcrec LIBRARY-TIER
     DRIVER: `--mode subst` over a substitution artifact (rx artifact + subst
     artifact + a private support unit in one .so, the template baked in at
     compile). For pcrec-auto, pcrec-vm and both `-sizefirst` arms the cases
     are compiled through the ADAPTER and the driver called DIRECTLY on
     acc-small, all 8 cases, output sha256 + count + length equal to
     expectations.tsv (judged here by hashlib) - cases 6 (`\\U$1\\E`) and 7
     (the conditional, VM route) included, which is what flips their
     divergences.tsv basis to `verified-small`; the size-first arm's bytes
     equal the bound arm's; case 6 refused by pcrec BY NAME without
     `subst-extended` (the control that the flag matters); the support unit
     private (no `pcrec_subst_*` dynamic symbol); the driver's refusals by
     name and a too-small bound a `giveup:-11` (NOSPACE), never retried;
     `run_cell` end to end for a bound and a size-first arm (schema-1.9
     record, distinct testee ids, every row `agrees`); a deliberately WRONG
     template fails the gate BY NAME; every config off the roster
     (nocaps, `-in`, utf8, clang, bigcap, deny arms, dfa, pcrec-local)
     refused BY NAME with its reason.
"""
import csv
import hashlib
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SUBST = os.path.join(ROOT, "bench", "subst")
sys.path.insert(0, ROOT)

from pcrecbench import oracle_pcre2 as oracle  # noqa: E402
from pcrecbench import subst_template as st  # noqa: E402

C_ENV = dict(os.environ, LC_ALL="C", LANG="C")

HOSTILE_PLAIN = (b"lit\tA$B\\\\C&D/E@F:G}H{I\"J'K\\tL\\nM\\xe9N(\\\\U)Z\n"
                 b"grp\t1\n"
                 b"lit\t|$$\\\\\\\\|\n"
                 b"grp\t2\n")
HOSTILE_UPPER = HOSTILE_PLAIN + b"upper\t1\nlit\t-\nupper\t2\n"
HOSTILE_COND = (b"grp\t1\n"
                b"cond\t2\nlit\tSET:{\\\\}\ngrp\t2\n"
                b"else\ncond\t3\nlit\tN3\ngrp\t3\nelse\nlit\tNONE$\nend\nend\n")


def _read_tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _run(argv, data, timeout=120):
    return subprocess.run(argv, input=data, capture_output=True, env=C_ENV,
                          timeout=timeout)


def run(ok, bad):
    print("-- [B140] bench/subst: the neutral template, the oracle, the set --")

    def check(what, cond, detail=""):
        (ok if cond else bad)(what, detail)

    def raises(fn, exc, token=None):
        try:
            fn()
        except exc as e:
            return token is None or getattr(e, "token", None) == token
        return False

    # ---------------------------------------------------------- 1. parser
    check("subst IR: unknown escape refused",
          raises(lambda: st.parse(b"lit\ta\\qb\n"), st.TemplateError))
    check("subst IR: unbalanced cond refused",
          raises(lambda: st.parse(b"cond\t1\nlit\tx\n"), st.TemplateError))
    check("subst IR: else outside a cond refused",
          raises(lambda: st.parse(b"else\n"), st.TemplateError))
    check("subst IR: a second else refused",
          raises(lambda: st.parse(b"cond\t1\nelse\nelse\nend\n"), st.TemplateError))
    check("subst IR: unknown segment refused",
          raises(lambda: st.parse(b"bogus\t1\n"), st.TemplateError))
    check("subst IR: group 0 refused",
          raises(lambda: st.parse(b"grp\t0\n"), st.TemplateError))
    ir = st.parse(HOSTILE_UPPER)
    want = (b"A$B\\C&D/E@F:G}H{I\"J'K\tL\nM\xe9N(\\U)Z" + b"ab" + b"|$$\\\\|" + b"b"
            + b"A-B")
    check("subst IR: evaluate() is the reference meaning",
          st.evaluate(ir, {1: b"a", 2: b"b"}) == b"A$B\\C&D/E@F:G}H{I\"J'K\tL\nM\xe9N(\\U)Z"
          + b"a" + b"|$$\\\\|" + b"b" + b"A" + b"-" + b"B",
          "hostile template")
    ci = st.parse(HOSTILE_COND)
    check("subst IR: cond/else nest, taken / not taken / not taken twice",
          st.evaluate(ci, {1: b"a", 2: b"b"}) == b"aSET:{\\}b"
          and st.evaluate(ci, {1: b"a", 2: None, 3: b"c"}) == b"aN3c"
          and st.evaluate(ci, {1: b"a", 2: None, 3: None}) == b"aNONE$")
    check("subst IR: unset_refs flags an unguarded optional reference",
          st.unset_refs(st.parse(b"cond\t2\nlit\tx\nend\ngrp\t2\n")) == [(2, "grp")]
          and st.unset_refs(ci) == [])

    # --------------------------------------------- 2. hostile vs engines
    subj = b"xaby"
    pre, post = b"x", b"y"

    def pcre2_run(irx, ext):
        tpl = st.render(irx, "pcre2", extended=ext)
        return bytes(oracle.compile(b"(a)(b)").substitute(subj, tpl, extended=ext)[1])

    for name, src, ext in (("plain", HOSTILE_PLAIN, False),
                           ("plain+extended", HOSTILE_PLAIN, True),
                           ("upper", HOSTILE_UPPER, True)):
        irx = st.parse(src)
        want = pre + st.evaluate(irx, {1: b"a", 2: b"b"}) + post
        check("subst hostile: libpcre2 (%s) == evaluate()" % name,
              pcre2_run(irx, ext) == want)
    # control: the pcre2 lit escaper off -> `$` / backslash are live syntax
    real = st._lit_pcre2
    st._lit_pcre2 = lambda b, extended: b
    try:
        naive_ok = False
        try:
            naive_ok = pcre2_run(st.parse(HOSTILE_PLAIN), True) == \
                pre + st.evaluate(st.parse(HOSTILE_PLAIN), {1: b"a", 2: b"b"}) + post
        except oracle.Pcre2Error:
            naive_ok = False
    finally:
        st._lit_pcre2 = real
    check("subst hostile CONTROL: unescaped pcre2 lits are NOT the answer",
          not naive_ok)

    irp = st.parse(HOSTILE_PLAIN)
    want_p = pre + st.evaluate(irp, {1: b"a", 2: b"b"}) + post
    py_out = re.sub(b"(a)(b)", st.render(irp, "python"), subj)
    check("subst hostile: python re.sub == evaluate()", py_out == want_p)
    real = st._lit_python
    st._lit_python = lambda b: b
    try:
        try:
            naive = re.sub(b"(a)(b)", st.render(irp, "python"), subj)
        except re.error:
            naive = None
    finally:
        st._lit_python = real
    check("subst hostile CONTROL: unescaped python lits are NOT the answer",
          naive != want_p)

    sed = shutil.which("sed")
    if sed:
        for name, src in (("plain", HOSTILE_PLAIN), ("upper", HOSTILE_UPPER)):
            irx = st.parse(src)
            want = pre + st.evaluate(irx, {1: b"a", 2: b"b"}) + post + b"\n"
            r = _run([sed, "-E", b"s/(a)(b)/" + st.render(irx, "sed") + b"/g"],
                     subj + b"\n")
            check("subst hostile: GNU sed -E (%s) == evaluate()" % name,
                  r.returncode == 0 and r.stdout == want, r.stderr[:80].decode("latin-1"))
        real = st._lit_sed
        st._lit_sed = lambda b: b
        try:
            r = _run([sed, "-E", b"s/(a)(b)/" + st.render(irp, "sed") + b"/g"],
                     subj + b"\n")
        finally:
            st._lit_sed = real
        check("subst hostile CONTROL: unescaped sed lits are NOT the answer",
              not (r.returncode == 0 and r.stdout == want_p + b"\n"))
    else:
        ok("subst hostile: GNU sed", "SKIPPED -- no sed on PATH")

    perl = shutil.which("perl")
    if perl:
        for name, src in (("plain", HOSTILE_PLAIN), ("upper", HOSTILE_UPPER)):
            irx = st.parse(src)
            want = pre + st.evaluate(irx, {1: b"a", 2: b"b"}) + post
            r = _run([perl, "-pe", b"s/(a)(b)/" + st.render(irx, "perl") + b"/g"], subj)
            check("subst hostile: perl s/// (%s) == evaluate()" % name,
                  r.returncode == 0 and r.stdout == want, r.stderr[:80].decode("latin-1"))
        real = st._lit_perl
        st._lit_perl = lambda b: b
        try:
            r = _run([perl, "-pe", b"s/(a)(b)/" + st.render(irp, "perl") + b"/g"], subj)
        finally:
            st._lit_perl = real
        check("subst hostile CONTROL: unescaped perl lits are NOT the answer",
              not (r.returncode == 0 and r.stdout == want_p))
    else:
        ok("subst hostile: perl", "SKIPPED -- no perl on PATH")

    # the conditional, pcre2 only (the only dialect that has one)
    for subject, groups in ((b"xaby", {1: b"a", 2: b"b"}), (b"xay", {1: b"a", 2: None})):
        got = bytes(oracle.compile(b"(a)(b)?(c)?").substitute(
            subject, st.render(ci, "pcre2", extended=True), extended=True)[1])
        exp = subject[:1] + st.evaluate(ci, {**groups, 3: None}) + subject[-1:]
        check("subst cond: libpcre2 ${n:+..:..} (group2 %s) == evaluate()"
              % ("set" if groups[2] else "unset"), got == exp, repr(got))
    check("subst cond CONTROL: an unguarded unset group is -55, raised",
          raises(lambda: oracle.compile(b"(a)(b)?").substitute(
              b"xay", b"$2", extended=False), oracle.Pcre2Error))
    check("subst cond: UNSET_EMPTY makes the same reference expand to nothing",
          bytes(oracle.compile(b"(a)(b)?").substitute(
              b"xay", b"<$2>", unset_empty=True)[1]) == b"x<>y")

    # ---------------------------------------- 3. engine-less dialects
    check("subst dialect rust/sd/rg: ${N}, `$` doubled",
          st.render(st.parse(b"lit\ta$b\ngrp\t1\n".replace(b"\n", b"\n", 1)), "rust") == b"a$$b${1}"
          and st.render(st.parse(b"grp\t3\nlit\t-\n"), "sd") == b"${3}-")
    check("subst dialect re2: \\N, backslash doubled, `$` literal",
          st.render(st.parse(b"lit\ta$\\\\b\ngrp\t2\n"), "re2") == b"a$\\\\b\\2")
    check("subst unsupported tokens are closed and named",
          all(raises(lambda d=d: st.render(ir, d), st.Unsupported, "no-case-operators")
              for d in ("python", "rust", "sd", "rg", "re2"))
          and raises(lambda: st.render(ci, "sed"), st.Unsupported, "no-conditional")
          and raises(lambda: st.render(ci, "python"), st.Unsupported, "no-conditional")
          and raises(lambda: st.render(st.parse(b"grp\t10\n"), "sed"),
                     st.Unsupported, "group-over-9"))

    # ----------------------------------------------------- 5. case files
    cases = _read_tsv(os.path.join(SUBST, "cases.tsv"))
    dirs = sorted(d for d in os.listdir(os.path.join(SUBST, "cases")))
    check("subst cases: cases.tsv and cases/ list the same %d directories" % len(cases),
          sorted(c["dir"] for c in cases) == dirs)
    good = True
    for c in cases:
        d = os.path.join(SUBST, "cases", c["dir"])
        pat = open(os.path.join(d, "PATTERN.rx"), "rb").read()
        try:
            irc = st.parse(open(os.path.join(d, "TEMPLATE.neutral"), "rb").read())
        except st.TemplateError as e:
            bad("subst case %s: template does not parse" % c["case"], str(e))
            good = False
            continue
        problems = []
        if pat.count(b"\n") != 1 or not pat.endswith(b"\n"):
            problems.append("PATTERN.rx is not exactly one line")
        if st.unset_refs(irc):
            problems.append("unguarded optional-group reference")
        if c["ere"] == "yes":
            if b"(?" in pat:
                problems.append("ERE case carries `(?`")
            if re.search(rb"\\[dswDSWAZz]", pat):
                problems.append("ERE case carries a PCRE-only escape")
            try:
                st.render(irc, "sed")
            except st.Unsupported as e:
                problems.append("ERE case not renderable for sed: %s" % e)
        if problems:
            bad("subst case %s (%s)" % (c["case"], c["dir"]), "; ".join(problems))
            good = False
    if good:
        ok("subst cases: every pattern one line, template parses, ERE cases "
           "are ERE-clean, no unguarded optional reference")

    # ---------------------------------------------------- 6. generator
    py = sys.executable
    r = subprocess.run([py, "-I", os.path.join(SUBST, "gen_subjects.py"), "--check"],
                       capture_output=True, text=True, env=C_ENV, timeout=600)
    out = r.stdout
    check("subst generator: acc-small reproduces manifest.tsv + planted.tsv",
          r.returncode == 0 and "manifest + planted" in out and "MATCH" in out,
          (r.stdout + r.stderr)[-200:].replace("\n", " | "))
    if "calibration SKIPPED" in out:
        ok("subst calibration vs the real log", "SKIPPED BY NAME -- reference "
           "absent (bench/subst/fetch_reference.sh; make check never fetches)")
    else:
        check("subst calibration: first-window table PASSES against the real log",
              "calibration PASS" in out, out[-160:].replace("\n", " | "))

    # ------------------------------------------------- 7. expectations
    r = subprocess.run([py, "-I", os.path.join(SUBST, "gen_expectations.py"), "--check"],
                       capture_output=True, text=True, env=C_ENV, timeout=900)
    check("subst expectations: acc-small re-derives from the oracle, each row "
          "== its independent count", r.returncode == 0 and "rows match" in r.stdout,
          (r.stdout + r.stderr)[-200:].replace("\n", " | "))

    # ---------------------------------------- 8. system tools on small
    sys.path.insert(0, SUBST)
    import logsim  # noqa: E402
    n_small = next(int(x["lines"]) for x in _read_tsv(os.path.join(SUBST, "planted.tsv"))
                   if x["id"] == "acc-small")
    data = b"".join(logsim.stream(n_small))
    exp = {x["case"]: x for x in _read_tsv(os.path.join(SUBST, "expectations.tsv"))
           if x["subject"] == "acc-small"}
    div = _read_tsv(os.path.join(SUBST, "divergences.tsv"))

    def pat_of(c):
        return open(os.path.join(SUBST, "cases", c["dir"], "PATTERN.rx"), "rb").read()[:-1]

    def ir_of(c):
        return st.parse(open(os.path.join(SUBST, "cases", c["dir"], "TEMPLATE.neutral"), "rb").read())

    def verdict(case, competitor):
        rows = [d for d in div if d["case"] == case and d["competitor"] in (competitor, "*")]
        rows.sort(key=lambda d: d["competitor"] == "*")
        return rows[0] if rows else None

    mism = []
    ran = 0
    for c in cases:
        pat, irc = pat_of(c), ir_of(c)
        sha_want = exp[c["case"]]["out_sha256"]
        # python re.sub (whole-file)
        v = verdict(c["case"], "python")
        try:
            tpl = st.render(irc, "python")
            got = hashlib.sha256(re.sub(pat, tpl, data)).hexdigest()
            outcome = "agrees" if got == sha_want else "WRONG"
        except st.Unsupported as e:
            outcome = "unsupported:" + e.token
        ran += 1
        if v and v["expectation"] != outcome and not v["expectation"].startswith("pending"):
            mism.append("python %s: table says %s, run says %s" % (c["case"], v["expectation"], outcome))
        # sed -E
        if sed:
            v = verdict(c["case"], "sed")
            try:
                rep = st.render(irc, "sed")
                r = _run([sed, "-E", b"s/" + pat.replace(b"/", b"\\/") + b"/" + rep + b"/g"], data)
                if r.returncode != 0:
                    outcome = "unsupported:pattern-syntax"
                else:
                    outcome = "agrees" if hashlib.sha256(r.stdout).hexdigest() == sha_want else "WRONG"
            except st.Unsupported as e:
                # the pattern is read first: a pattern sed cannot parse is
                # `pattern-syntax` whatever the template needs
                probe = _run([sed, "-E", b"s/" + pat.replace(b"/", b"\\/") + b"//g"], b"x\n")
                outcome = ("unsupported:pattern-syntax" if probe.returncode != 0
                           else "unsupported:" + e.token)
            ran += 1
            if v and v["expectation"] != outcome:
                mism.append("sed %s: table says %s, run says %s" % (c["case"], v["expectation"], outcome))
        # perl
        if perl:
            v = verdict(c["case"], "perl")
            try:
                rep = st.render(irc, "perl")
                r = _run([perl, "-pe", b"s/" + pat.replace(b"/", b"\\/") + b"/" + rep + b"/g"], data)
                if r.returncode != 0:
                    outcome = "unsupported:pattern-syntax"
                else:
                    outcome = "agrees" if hashlib.sha256(r.stdout).hexdigest() == sha_want else "WRONG"
            except st.Unsupported as e:
                outcome = "unsupported:" + e.token
            ran += 1
            if v and v["expectation"] != outcome:
                mism.append("perl %s: table says %s, run says %s" % (c["case"], v["expectation"], outcome))
    check("subst tools on acc-small: python/sed/perl outcomes == divergences.tsv "
          "(%d runs)" % ran, not mism, "; ".join(mism[:4]))

    _driver_slice(check, data, cases, exp)


def _driver_slice(check, data, cases, exp):
    """Section 9 (module docstring). Scratch under build/check-subst/; a
    360 MB subject is never read (`subject_limit=1`, acc-small only)."""
    import tempfile
    from unittest import mock
    from pcrecbench import adapters as _ad
    from pcrecbench import driverrun, harness, store, substrun, subbench

    work = os.path.join(ROOT, "build", "check-subst")
    shutil.rmtree(work, ignore_errors=True)
    subj_dir = os.path.join(work, "subjects")
    out_dir = os.path.join(work, "out")
    for d in (subj_dir, out_dir):
        os.makedirs(d)
    with open(os.path.join(subj_dir, "acc-small.log"), "wb") as f:
        f.write(data)
    saved = {k: os.environ.get(k) for k in ("PCRECBENCH_SUBST_SUBJECTS",
                                            "PCRECBENCH_SUBST_OUT")}
    os.environ["PCRECBENCH_SUBST_SUBJECTS"] = subj_dir
    os.environ["PCRECBENCH_SUBST_OUT"] = out_dir
    try:
        sb = subbench.find("subst")
        small = sb.subjects_for("substitution")[0]
        check("subst driver: the on-disk acc-small is the manifest's bytes",
              hashlib.sha256(data).hexdigest() == small.sha256
              and small.subject_id == "acc-small")
        _driver_direct(check, sb, small, cases, work)
        _harness_records(check, sb, work, mock, _ad, harness, store, substrun)
        _gate_and_faults(check, sb, small, work, mock, _ad, substrun)
        _refusals(check, sb, work, mock, _ad, driverrun, harness, substrun)
        _rust_re2(check, sb, small, cases, work, _ad, harness, store, substrun)
        _tools_tier(check, sb, small, cases, work, _ad, harness, store, substrun)
        _pcrec_tier(check, sb, small, cases, work, _ad, harness, store, substrun)
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(work, ignore_errors=True)


def _driver_direct(check, sb, small, cases, work):
    """9a: the driver called DIRECTLY (argv by hand, the verdict from
    expectations.tsv and hashlib) for the four pcre2 arms x 8 cases."""
    from pcrecbench import adapters as _ad
    from pcrecbench.driverrun import run_driver
    exp = {(x["case"], x["subject"]): x for x in _read_tsv(os.path.join(SUBST, "expectations.tsv"))}
    lst = os.path.join(work, "list.tsv")
    with open(lst, "w") as f:
        f.write("acc-small\t%s\n" % small.path)
    for cid in ("pcre2-interp", "pcre2-jit", "pcre2-interp-sizefirst", "pcre2-jit-sizefirst"):
        ad, cfg = _ad.resolve(cid)
        drv = ad.prepare_driver(os.path.join(work, "w-" + cid))
        bad_cases = []
        for c in cases:
            ir = st.parse(open(os.path.join(SUBST, "cases", c["dir"], "TEMPLATE.neutral"), "rb").read())
            ext = st.needs_extended(ir)
            pf = os.path.join(work, "p-%s-%s" % (cid, c["case"]))
            tf = pf + ".tpl"
            with open(pf, "wb") as f:
                f.write(open(os.path.join(SUBST, "cases", c["dir"], "PATTERN.rx"), "rb").read()[:-1])
            with open(tf, "wb") as f:
                f.write(st.render(ir, "pcre2", extended=ext))
            od = os.path.join(work, "o-%s-%s" % (cid, c["case"]))
            os.makedirs(od)
            e = exp[(c["case"], "acc-small")]
            argv = [drv, "--pattern", pf, "--list", lst, "--mode", "subst",
                    "--template", tf, "--subst-flags", "extended" if ext else "none",
                    "--sizing", "first" if cfg.get("subst_sizing") == "first" else "bound",
                    "--bound", "acc-small=%d" % (small.length + 8 * int(e["nsubst"]) + 1),
                    "--out-dir", od]
            if cfg.get("jit"):
                argv.append("--jit")
            r = run_driver(argv, timeout=120)
            row = r.rows[0] if r.rows else None
            got = (hashlib.sha256(open(os.path.join(od, row.out_path), "rb").read()).hexdigest()
                   if row is not None and row.out_path else None)
            if (r.returncode != 0 or row is None or got != e["out_sha256"]
                    or row.nmatches != int(e["nsubst"]) or row.out_bytes != int(e["out_bytes"])
                    or row.iters != 1):
                bad_cases.append("%s: rc=%s %s" % (c["case"], r.returncode,
                                                   row.answer if row else r.diagnostic()))
            shutil.rmtree(od, ignore_errors=True)
        check("subst driver %s: --mode subst on acc-small, all %d cases, output "
              "sha256 + count + length == expectations.tsv" % (cid, len(cases)),
              not bad_cases, "; ".join(bad_cases[:3]))
    # the driver's own refusals (exit 2, `error` line, by name)
    drv = _ad.resolve("pcre2-jit")[0].prepare_driver(os.path.join(work, "w-pcre2-jit"))
    base = [drv, "--pattern", os.path.join(work, "p-pcre2-jit-1"), "--list", lst,
            "--mode", "subst", "--template", os.path.join(work, "p-pcre2-jit-1.tpl")]
    for flag in ("--find-all", "--prime", "--dfa", "--utf8"):
        r = run_driver(base + [flag, "--bound", "acc-small=9999999"], timeout=30)
        check("subst driver: %s is REFUSED in --mode subst by name" % flag,
              r.returncode == 2 and any("--mode subst" in e for e in r.errors),
              "rc=%s errors=%s" % (r.returncode, r.errors))
    r = run_driver([drv, "--pattern", base[2], "--list", lst, "--mode", "subst"], timeout=30)
    check("subst driver: --mode subst without --template is refused by name",
          r.returncode == 2 and any("--template" in e for e in r.errors))
    r = run_driver(base, timeout=30)       # no --bound for the subject
    check("subst driver: a subject with no --bound is refused by name",
          r.returncode == 2 and any("--bound" in e for e in r.errors))
    # a too-small bound is the engine's NOMEMORY -- reported, never retried
    r = run_driver(base + ["--bound", "acc-small=1000"], timeout=30)
    check("subst driver: a too-small bound is reported as a failure "
          "(giveup:-48), never retried inside the timed call",
          r.rows and r.rows[0].answer.startswith("giveup:-48"),
          r.rows[0].answer if r.rows else "no row")


def _harness_records(check, sb, work, mock, _ad, harness, store, substrun):
    """9b: run_cell end to end (scratch tier) for interp and jit; 9c: the
    unsupported path with the divergence competitor patched to `sd`."""
    exp = {(x["case"], x["subject"]): x for x in _read_tsv(os.path.join(SUBST, "expectations.tsv"))}
    root = os.path.join(work, "store")
    os.makedirs(root)
    for cid, trials in (("pcre2-interp", 1), ("pcre2-jit", 2)):
        res = harness.run_cell("subst", cid, trials=trials, tier=store.TIER_SCRATCH,
                               store_root=root, subject_limit=1,
                               workdir=os.path.join(work, "hw-" + cid),
                               synthetic=True)
        rows = [r for r in res.rows if r["kind"] == "match"]
        comp = [r for r in res.rows if r["kind"] == "compile"]
        agree = all(r["match_outcome"] == "matched-as-expected"
                    and r["subst"]["gate"] == "agrees"
                    and r["subst"]["out_sha256"] == exp[(r["subst"]["case"], "acc-small")]["out_sha256"]
                    and r["regime"] == "substitution" and r["timing"]["iterations"] == 1
                    and r["timing"]["bytes_processed"] == 3929818 for r in rows)
        check("subst harness %s: a schema-%s record (validator-accepted by "
              "store.write) with %d substitution rows x %d trial(s), every one "
              "matched-as-expected, gate agrees, out_sha256 == expectations.tsv"
              % (cid, res.setup["schema_version"], 8, trials),
              len(rows) == 8 * trials and agree and res.setup["schema_version"] == "1.9"
              and res.setup["testee"]["invocation"] == "library"
              and res.setup["subbench"]["regimes"] == ["substitution"]
              and len(comp) == 8 * trials)
    # ---- unsupported by declaration (compile row, no match rows, X44)
    real = _ad.resolve

    class Patched:
        def __init__(self, ad):
            self._ad = ad

        def __getattr__(self, n):
            return getattr(self._ad, n)

        def subst_support(self, tid):
            d = dict(self._ad.subst_support(tid))
            d["competitor"] = "sd"          # case 6 / 7 unsupported in the table
            return d

    def patched(tid, root=None):
        ad, cfg = real(tid, root)
        return Patched(ad), cfg

    with mock.patch.object(_ad, "resolve", patched):
        res = harness.run_cell("subst", "pcre2-jit", trials=1, tier=store.TIER_SCRATCH,
                               store_root=root, subject_limit=1,
                               workdir=os.path.join(work, "hw-unsup"), synthetic=True)
    unsup = {r["pattern_id"]: r for r in res.rows if r["kind"] == "compile"
             and r["compile_outcome"] == "unsupported-by-declaration"}
    matched = {r["pattern_id"] for r in res.rows if r["kind"] == "match"}
    check("subst harness: an unsupported (testee, case) is a compile row "
          "`unsupported-by-declaration` carrying its declaration_ref and has NO "
          "match rows (X44); the other six cases still run and agree",
          set(unsup) == {"6-upper", "7-url-tld-fix"}
          and all("divergences.tsv" in r["declaration_ref"] for r in unsup.values())
          and matched.isdisjoint(unsup) and len(matched) == 6,
          "%s / %s" % (sorted(unsup), sorted(matched)))


def _gate_and_faults(check, sb, small, work, mock, _ad, substrun):
    """9d/9e: the gate's negative control and the determinism fault, through
    substrun.measure_cell on a hand-compiled handle."""
    ad, cfg = _ad.resolve("pcre2-jit")
    wd = os.path.join(work, "gw")
    ad.prepare("pcre2-jit", wd)
    p = sb.pattern("1-literal")
    cp = ad.compile("pcre2-jit", p.name, sb.pattern_bytes(p.name), {}, 1, wd)
    handle = dict(cp.get("plain").handle)
    handle["pin"] = None
    handle["subject_timeout"] = 60
    sup = ad.subst_support("pcre2-jit")
    giveup = lambda a, h: False        # noqa: E731

    # the control: the REAL template passes the same path
    good = substrun.plan_case(sb, p, sup)
    substrun.write_template(good, os.path.join(wd, "good"))
    ents, _n = substrun.measure_cell(ad, handle, sb, p, good, sup, [small], 2, 60, giveup)
    check("subst gate (control): the real template passes - trial 1 agrees, "
          "both trials timed",
          [e["subst"]["gate"] for e in ents] == ["agrees", "agrees"]
          and all(e["timing"] for e in ents))
    # the deliberately WRONG template: H2 where the case says H1
    wrong = substrun.plan_case(sb, p, sup, template_override=b"lit\tH2\n")
    substrun.write_template(wrong, os.path.join(wd, "wrong"))
    ents, notes = substrun.measure_cell(ad, handle, sb, p, wrong, sup, [small], 3, 60, giveup)
    e1 = ents[0]
    check("subst gate: a deliberately WRONG template FAILS the gate BY NAME - "
          "gate `wrong`, did-not-match-as-expected, NOT timed, the diagnostic "
          "names the first differing byte and both lengths",
          e1["subst"]["gate"] == "wrong" and e1["outcome"] == "did-not-match-as-expected"
          and e1["timing"] is None and "differs from the oracle's at byte" in e1["diagnostic"]
          and "observed 3836788 bytes" in e1["diagnostic"],
          (e1["diagnostic"] or "")[:200])
    check("subst gate: a wrong cell is not re-run (trials 2..3 repeat trial 1's "
          "identity, dense trial numbering, no timing anywhere)",
          [e["trial"] for e in ents] == [1, 2, 3]
          and len({(e["subst"]["gate"], e["subst"]["out_sha256"]) for e in ents}) == 1
          and all(e["timing"] is None for e in ents)
          and any("not timed beyond trial 1" in n for n in notes))
    # a DECLARED divergence is `divergent-declared` and cites its row
    with mock.patch.object(type(sb), "divergence",
                           lambda self, case, *c: ("divergent", "test", "declared",
                                                   "bench/subst/divergences.tsv: test")):
        ents, _n = substrun.measure_cell(ad, handle, sb, p, wrong, sup, [small], 1, 60, giveup)
    check("subst gate: a mismatch the table DECLARES is `divergent-declared` "
          "and cites its declaration (X37)",
          ents[0]["subst"]["gate"] == "divergent-declared"
          and ents[0]["subst"]["declaration_ref"] == "bench/subst/divergences.tsv: test")

    # determinism fault: trial 2's length differs from trial 1's
    class Flaky:
        def __init__(self, ad):
            self._ad, self.calls = ad, 0

        def __getattr__(self, n):
            return getattr(self._ad, n)

        def measure_subst(self, *a, **k):
            rows, info, notes = self._ad.measure_subst(*a, **k)
            self.calls += 1
            if self.calls == 2:
                rows[0].out_bytes += 1
            return rows, info, notes

    try:
        substrun.measure_cell(Flaky(ad), handle, sb, p, good, sup, [small], 2, 60, giveup)
        fault = None
    except substrun.DeterminismFault as e:
        fault = str(e)
    check("subst trials: a trial-2 output length that differs from trial 1's "
          "is a DETERMINISM FAULT by name and nothing is recorded",
          fault is not None and fault.startswith("DETERMINISM FAULT")
          and "trial 2" in fault, fault)


def _refusals(check, sb, work, mock, _ad, driverrun, harness, substrun):
    """9f: refusals BY NAME, no engine needed past the first line."""
    from pcrecbench import store

    def refuses(testee, subbench_name, needle):
        try:
            harness.run_cell(subbench_name, testee, trials=1, tier=store.TIER_SCRATCH,
                             store_root=os.path.join(work, "rstore"), subject_limit=1,
                             workdir=os.path.join(work, "rw"), synthetic=True)
        except harness.HarnessError as e:
            return needle in str(e), str(e)[:160]
        return False, "no error"

    ok1, d1 = refuses("pcre2-jit-sizefirst", "email", "substitution-only testee")
    check("subst harness: a -sizefirst arm on a non-substitution set is "
          "refused by name", ok1, d1)
    ok2, d2 = refuses("pcre2-dfa", "subst", "declares no substitution call")
    check("subst harness: a testee with no substitution call (pcre2-dfa) is "
          "refused by name on the substitution set", ok2, d2)
    # the table and the renderer must agree
    p6 = sb.pattern("6-upper")
    try:
        substrun.plan_case(sb, p6, {"dialect": "python", "competitor": "pcre2-jit"})
        msg = None
    except substrun.SubstError as e:
        msg = str(e)
    check("subst plan: a renderer refusal the table does not declare is a "
          "SubstError BY NAME (the table and the renderer disagree)",
          msg is not None and "disagree" in msg, msg)
    pl = substrun.plan_case(sb, p6, {"dialect": "python", "competitor": "python"})
    check("subst plan: case 6 for python is `unsupported` with its citation; "
          "case 6 for pcre2-jit is runnable with the EXTENDED flag",
          pl.unsupported and "no-case-operators" in pl.unsupported
          and "divergences.tsv" in pl.declaration_ref
          and substrun.plan_case(sb, p6, {"dialect": "pcre2", "competitor": "pcre2-jit"}).flags == "extended")


def _rust_re2(check, sb, small, cases, work, _ad, harness, store, substrun):
    """Section 10 ([B140] b140drv2): rust-default and re2-default."""
    from pcrecbench.driverrun import run_driver
    exp = {(x["case"], x["subject"]): x for x in _read_tsv(os.path.join(SUBST, "expectations.tsv"))}
    div = _read_tsv(os.path.join(SUBST, "divergences.tsv"))
    lst = os.path.join(work, "list.tsv")
    with open(lst, "w") as f:
        f.write("acc-small\t%s\n" % small.path)
    engines = (("rust-default", "rust", "rust-regex", ["--no-unicode"]),
               ("re2-default", "re2", "re2", []))
    for cid, dialect, competitor, extra in engines:
        ad, _cfg = _ad.resolve(cid)
        drv = ad.prepare_driver(os.path.join(work, "w-" + cid))
        declared = {d["case"] for d in div if d["competitor"] == competitor
                    and d["expectation"].startswith("unsupported")}
        runnable = [c for c in cases if c["case"] not in declared]
        bad_cases = []
        for c in runnable:
            ir = st.parse(open(os.path.join(SUBST, "cases", c["dir"], "TEMPLATE.neutral"), "rb").read())
            pf = os.path.join(work, "p-%s-%s" % (cid, c["case"]))
            tf = pf + ".tpl"
            with open(pf, "wb") as f:
                f.write(open(os.path.join(SUBST, "cases", c["dir"], "PATTERN.rx"), "rb").read()[:-1])
            with open(tf, "wb") as f:
                f.write(st.render(ir, dialect))
            od = os.path.join(work, "o-%s-%s" % (cid, c["case"]))
            os.makedirs(od)
            e = exp[(c["case"], "acc-small")]
            argv = [drv, "--pattern", pf, "--list", lst, "--mode", "subst",
                    "--template", tf, "--subst-flags", "none",
                    "--bound", "acc-small=%d" % (small.length + 8 * int(e["nsubst"]) + 1),
                    "--out-dir", od] + extra
            r = run_driver(argv, timeout=120)
            row = r.rows[0] if r.rows else None
            got = (hashlib.sha256(open(os.path.join(od, row.out_path), "rb").read()).hexdigest()
                   if row is not None and row.out_path else None)
            if (r.returncode != 0 or row is None or got != e["out_sha256"]
                    or row.nmatches != int(e["nsubst"]) or row.out_bytes != int(e["out_bytes"])
                    or row.iters != 1):
                bad_cases.append("%s: rc=%s %s" % (c["case"], r.returncode,
                                                   row.answer if row else r.diagnostic()))
            shutil.rmtree(od, ignore_errors=True)
        check("subst driver %s: --mode subst on acc-small, the %d runnable "
              "cases (%d declared unsupported), output sha256 + count + length "
              "== expectations.tsv" % (cid, len(runnable), len(declared)),
              not bad_cases and len(declared) == 2 and len(runnable) == 6,
              "; ".join(bad_cases[:3]))
        base = [drv, "--pattern", os.path.join(work, "p-%s-1" % cid), "--list", lst,
                "--mode", "subst", "--template", os.path.join(work, "p-%s-1.tpl" % cid),
                "--bound", "acc-small=9999999"] + extra
        for flag in ("--find-all", "--prime", "--utf8"):
            r = run_driver(base + [flag], timeout=30)
            check("subst driver %s: %s is REFUSED in --mode subst by name" % (cid, flag),
                  r.returncode == 2 and any("--mode subst" in e for e in r.errors),
                  "rc=%s errors=%s" % (r.returncode, r.errors))
        r = run_driver(base + ["--iters", "2"], timeout=30)
        check("subst driver %s: --iters 2 is refused by name (one call per subject)" % cid,
              r.returncode == 2 and any("--iters" in e for e in r.errors))
        r = run_driver([drv, "--pattern", base[2], "--list", lst, "--mode", "subst"] + extra, timeout=30)
        check("subst driver %s: --mode subst without --template is refused by name" % cid,
              r.returncode == 2 and any("--template" in e for e in r.errors))
        # through the harness: a schema-1.9 record, the by-declaration rows
        root = os.path.join(work, "store-" + cid)
        os.makedirs(root)
        res = harness.run_cell("subst", cid, trials=2, tier=store.TIER_SCRATCH,
                               store_root=root, subject_limit=1,
                               workdir=os.path.join(work, "hw-" + cid), synthetic=True)
        rows = [r for r in res.rows if r["kind"] == "match"]
        comp = [r for r in res.rows if r["kind"] == "compile"]
        unsup = {r["pattern_id"]: r for r in comp
                 if r["compile_outcome"] == "unsupported-by-declaration"}
        check("subst harness %s: a schema-1.9 record (validator-accepted) with "
              "12 substitution rows (6 runnable cases x 2 trials), every one "
              "matched-as-expected / gate agrees with the expectation's hash" % cid,
              len(rows) == 12 and res.setup["schema_version"] == "1.9"
              and res.setup["testee"]["invocation"] == "library"
              and all(r["match_outcome"] == "matched-as-expected"
                      and r["subst"]["gate"] == "agrees"
                      and r["subst"]["out_sha256"] == exp[(r["subst"]["case"], "acc-small")]["out_sha256"]
                      and r["timing"]["iterations"] == 1 for r in rows))
        check("subst harness %s: cases 6 and 7 are compile rows `unsupported-by-"
              "declaration` citing divergences.tsv (case 7's row is the PATTERN-"
              "level `pattern-syntax`, the renderer's own token is the template's), "
              "with NO match rows and one compile row per COMPILED case-trial only"
              % cid,
              set(unsup) == {"6-upper", "7-url-tld-fix"}
              and all(competitor in r["declaration_ref"] and "divergences.tsv" in r["declaration_ref"]
                      for r in unsup.values())
              and "pattern-syntax" in unsup["7-url-tld-fix"]["declaration_ref"]
              and not ({r["pattern_id"] for r in rows} & set(unsup))
              and len(comp) == 6 * 2 + 2)
    # the engine whose chartered config is the DEFAULT only: others refused by name
    try:
        harness.run_cell("subst", "re2-longest", trials=1, tier=store.TIER_SCRATCH,
                         store_root=os.path.join(work, "store-rl"), subject_limit=1,
                         workdir=os.path.join(work, "hw-rl"), synthetic=True)
        msg = "no error"
    except harness.HarnessError as e:
        msg = str(e)
    check("subst harness: re2-longest (not the chartered re2-default) is refused "
          "by name", "declares no substitution call" in msg, msg[:160])
    # the gate through the rust driver: a deliberately wrong template fails by name
    ad, _c = _ad.resolve("rust-default")
    wd = os.path.join(work, "gw-rust")
    ad.prepare("rust-default", wd)
    p = sb.pattern("1-literal")
    cp = ad.compile("rust-default", p.name, sb.pattern_bytes(p.name),
                    {"substitution": True}, 1, wd)
    handle = dict(cp.get("plain").handle)
    handle["pin"], handle["subject_timeout"] = None, 60
    sup = ad.subst_support("rust-default")
    wrong = substrun.plan_case(sb, p, sup, template_override=b"lit\tH2\n")
    substrun.write_template(wrong, os.path.join(wd, "wrong"))
    ents, _n = substrun.measure_cell(ad, handle, sb, p, wrong, sup, [small], 1, 60,
                                     lambda a, h: False)
    check("subst gate (rust): a deliberately WRONG template FAILS BY NAME - gate "
          "`wrong`, did-not-match-as-expected, not timed",
          ents[0]["subst"]["gate"] == "wrong"
          and ents[0]["outcome"] == "did-not-match-as-expected"
          and ents[0]["timing"] is None
          and "differs from the oracle's at byte" in ents[0]["diagnostic"])
    # plan_case: the pattern-level row beside a DIFFERENT template token
    p7 = sb.pattern("7-url-tld-fix")
    pl = substrun.plan_case(sb, p7, {"dialect": "rust", "competitor": "rust-regex"})
    check("subst plan: case 7 for rust is unsupported on the table's PATTERN-level "
          "token although the renderer's own token differs (no-conditional)",
          pl.unsupported and "pattern-syntax" in pl.unsupported
          and "divergences.tsv" in pl.declaration_ref, pl.unsupported)


TOOL_IDS = ("sed-ere", "perl-p", "python-resub", "sd-stdin", "rg-passthru")


def _tools_tier(check, sb, small, cases, work, _ad, harness, store, substrun):
    """Section 11 ([B140] step 4, lane b140tools): the TOOLS tier. The tools
    run the cases divergences.tsv does not declare unsupported on acc-small:
    (a) the UNTIMED pass, called through the runner but judged here by hashlib
    against expectations.tsv, no harness code in the verdict; (b) one TIMED
    `tool | wc -c` per tool whose count equals out_bytes; (c) a SABOTAGED sink
    fails BY NAME (control: the unsabotaged call passes); (d) `run_cell` end
    to end per tool: a schema-1.9 `process` record, X38-X40, the by-declaration
    compile rows and nothing else; (e) the pins refuse by name."""
    import copy
    from pcrecbench import toolrun
    exp = {(x["case"], x["subject"]): x for x in _read_tsv(os.path.join(SUBST, "expectations.tsv"))}
    div = _read_tsv(os.path.join(SUBST, "divergences.tsv"))
    say = {}
    for tid in TOOL_IDS:
        ad, cfg = _ad.resolve(tid)
        ad.prepare(tid, os.path.join(work, "tw-" + tid))
        binary = ad.binary_path(tid)
        comp = cfg["competitor"]
        declared = {d["case"] for d in div if d["competitor"] == comp
                    and d["expectation"].startswith("unsupported")}
        runnable = [c for c in cases if c["case"] not in declared]
        tool_core, sink_core, _n = toolrun.pick_cores(None)
        bad, table = [], []
        for c in runnable:
            ir = st.parse(open(os.path.join(SUBST, "cases", c["dir"], "TEMPLATE.neutral"), "rb").read())
            pat = open(os.path.join(SUBST, "cases", c["dir"], "PATTERN.rx"), "rb").read()[:-1]
            tpl = st.render(ir, cfg["dialect"])
            pf = os.path.join(work, "tp-%s-%s" % (tid, c["case"]))
            tf = pf + ".tpl"
            open(pf, "wb").write(pat)
            open(tf, "wb").write(tpl)
            argv, stdin_in, _disp = toolrun.build_argv(cfg["kind"], binary, pat, tpl, small.path,
                                                      pattern_file=pf, template_file=tf)
            out = os.path.join(work, "to-%s-%s" % (tid, c["case"]))
            rc, err, _pk = toolrun.untimed_pass(argv, stdin_in, small.path, out, tool_core, 120)
            e = exp[(c["case"], "acc-small")]
            got = hashlib.sha256(open(out, "rb").read()).hexdigest() if os.path.exists(out) else None
            size = os.path.getsize(out) if os.path.exists(out) else -1
            os.unlink(out) if os.path.exists(out) else None
            ok = (rc in tuple(cfg.get("ok_exit", [0])) and got == e["out_sha256"]
                  and size == int(e["out_bytes"]))
            table.append((c["case"], ok))
            if not ok:
                bad.append("%s: rc=%s size=%d want %s %s" % (c["case"], rc, size, e["out_bytes"], err[:80]))
        say[tid] = table
        check("subst tools %s: the UNTIMED pass on acc-small, the %d runnable cases (%d "
              "declared unsupported), output sha256 + length == expectations.tsv"
              % (tid, len(runnable), len(declared)), not bad and len(runnable) + len(declared) == 8,
              "; ".join(bad[:3]))
        # one TIMED `tool | wc -c` run, case 1: the count equals the oracle's out_bytes
        c = cases[0]
        ir = st.parse(open(os.path.join(SUBST, "cases", c["dir"], "TEMPLATE.neutral"), "rb").read())
        pat = open(os.path.join(SUBST, "cases", c["dir"], "PATTERN.rx"), "rb").read()[:-1]
        tpl = st.render(ir, cfg["dialect"])
        pf = os.path.join(work, "tp-%s-%s" % (tid, c["case"]))
        argv, stdin_in, _disp = toolrun.build_argv(cfg["kind"], binary, pat, tpl, small.path,
                                                  pattern_file=pf, template_file=pf + ".tpl")
        frac = toolrun.warm_resident(small.path)
        t = toolrun.timed_pipeline(argv, stdin_in, small.path, tool_core, sink_core, 120)
        check("subst tools %s: one TIMED `| wc -c` run, case 1 - the tool exits cleanly, wc's "
              "count == out_bytes (%s), the input 100%% page-cache resident, wc on another core"
              % (tid, exp[("1", "acc-small")]["out_bytes"]),
              t["rc"] in tuple(cfg.get("ok_exit", [0]))
              and t["sink_bytes"] == int(exp[("1", "acc-small")]["out_bytes"])
              and frac == 1.0 and tool_core != sink_core and t["seconds"] > 0,
              "%r" % (t,))

    # (c) the SABOTAGED sink fails BY NAME; the control passes
    tid = "sed-ere"
    ad, _cfg = _ad.resolve(tid)
    wd = os.path.join(work, "tw-sab")
    ad.prepare(tid, wd)
    p = sb.pattern("1-literal")
    sup = ad.subst_support(tid)
    cp = ad.compile(tid, p.name, sb.pattern_bytes(p.name), {"substitution": True}, 1, wd)
    handle = dict(cp.get("plain").handle)
    handle["pin"], handle["subject_timeout"] = None, 60
    plan = substrun.plan_case(sb, p, sup)
    substrun.write_template(plan, os.path.join(wd, "p"))
    ents, _n = substrun.measure_cell(ad, dict(handle), sb, p, plan, sup, [small], 2, 120,
                                     lambda a, h: False)
    check("subst tools sink (control): the unsabotaged sed case 1 runs 2 trials, gate agrees, "
          "every timed row carries `process` with sink_bytes == out_bytes and the wc core != the tool's",
          all(e["outcome"] == "matched-as-expected" and e["process"]["sink_bytes"] == e["subst"]["out_bytes"]
              and e["process"]["core"] != e["process"]["sink_core"] and e["process"]["sink"] == "wc-c"
              and e["subst"]["nsubst"] == int(exp[("1", "acc-small")]["nsubst"]) for e in ents)
          and len(ents) == 2)
    saved = toolrun.SINK_ARGV
    toolrun.SINK_ARGV = ["/bin/sh", "-c", "cat > /dev/null; echo 7"]
    try:
        substrun.measure_cell(ad, dict(handle), sb, p, plan, sup, [small], 1, 120, lambda a, h: False)
        msg = "no error"
    except substrun.SubstError as e:
        msg = str(e)
    finally:
        toolrun.SINK_ARGV = saved
    check("subst tools sink (sabotage): a `| wc -c` count of 7 against the validated %s bytes "
          "FAILS BY NAME (SINK MISMATCH, nothing written)" % exp[("1", "acc-small")]["out_bytes"],
          "SINK MISMATCH" in msg and "counted 7 bytes" in msg, msg[:200])

    # the rusage floor: wait4's ru_maxrss of a posix_spawn child is floored at the
    # harness's own RSS (mm shared until exec), so a streaming tool reads ~the
    # harness's size; the untimed pass's polled VmHWM does not
    c3 = cases[2]
    ir3 = st.parse(open(os.path.join(SUBST, "cases", c3["dir"], "TEMPLATE.neutral"), "rb").read())
    pat3 = open(os.path.join(SUBST, "cases", c3["dir"], "PATTERN.rx"), "rb").read()[:-1]
    argv3, sin3, _d = toolrun.build_argv("sed", ad.binary_path("sed-ere"), pat3, st.render(ir3, "sed"), small.path)
    _rc, _e, peak = toolrun.untimed_pass(argv3, sin3, small.path, os.path.join(work, "to-peak"), 15, 120)
    harness_rss_kb = int(next(l.split()[1] for l in open("/proc/self/status") if l.startswith("VmHWM:")))
    t3 = toolrun.timed_pipeline(argv3, sin3, small.path, 15, 14, 120)
    check("subst tools rusage: sed's untimed-pass peak RSS (polled VmHWM, %s KB) is far below "
          "the harness's own (%d KB) while `wait4`'s ru_maxrss (%d KB) is floored at it - why "
          "process.maxrss_kb takes the polled value" % (peak, harness_rss_kb, t3["maxrss_kb"]),
          peak is not None and peak < harness_rss_kb // 2 and t3["maxrss_kb"] >= harness_rss_kb // 2,
          "%r %r %r" % (peak, harness_rss_kb, t3["maxrss_kb"]))

    # (e) the pins refuse by name
    ad, _cfg = _ad.resolve("sd-stdin")
    saved_cfg = ad.cfg
    ad.cfg = copy.deepcopy(saved_cfg)
    ad.cfg["testees"]["sd-stdin"]["binary_sha256"] = "0" * 64
    try:
        ad.binary_path("sd-stdin")
        msg = "no error"
    except _ad.AdapterError as e:
        msg = str(e)
    ad.cfg = copy.deepcopy(saved_cfg)
    ad.cfg["testees"]["sed-ere"]["version"] = "9.99"
    try:
        ad.probe_version("sed-ere")
        msg2 = "no error"
    except _ad.AdapterError as e:
        msg2 = str(e)
    ad.cfg = saved_cfg
    check("subst tools pins: a wrong binary sha256 (sd) and a changed system-tool version (sed) "
          "are each refused BY NAME; the real pins describe", "BINARY SHA256 MISMATCH" in msg
          and "pins '9.99'" in msg2 and ad.describe("sd-stdin")["engine_version"] == "1.1.0"
          and ad.describe("rg-passthru")["engine_name"] == "ripgrep", msg[:80] + " | " + msg2[:80])

    # (d) run_cell per tool: a schema-1.9 `process` record
    for tid in TOOL_IDS:
        ad, cfg = _ad.resolve(tid)
        comp = cfg["competitor"]
        declared = {d["case"] for d in div if d["competitor"] == comp
                    and d["expectation"].startswith("unsupported")}
        trials = 2 if tid == "sed-ere" else 1
        root = os.path.join(work, "tstore-" + tid)
        os.makedirs(root)
        res = harness.run_cell("subst", tid, trials=trials, tier=store.TIER_SCRATCH,
                               store_root=root, subject_limit=1,
                               workdir=os.path.join(work, "thw-" + tid), synthetic=True)
        rows = [r for r in res.rows if r["kind"] == "match"]
        comp_rows = [r for r in res.rows if r["kind"] == "compile"]
        runnable = 8 - len(declared)
        check("subst tools %s harness: a schema-%s `process` record (validator-accepted by "
              "store.write) - %d substitution rows (%d runnable cases x %d trial(s)), every one "
              "matched-as-expected / gate agrees / out_sha256 == the oracle's, each with a "
              "`process` object (sink wc-c, count == out_bytes, wc core != tool core)"
              % (tid, res.setup["schema_version"], runnable * trials, runnable, trials),
              len(rows) == runnable * trials and res.setup["schema_version"] == "1.9"
              and res.setup["testee"]["invocation"] == "process"
              and res.setup["testee"]["execution_model"] == "interpretive"
              and all(r["match_outcome"] == "matched-as-expected" and r["subst"]["gate"] == "agrees"
                      and r["subst"]["out_sha256"] == exp[(r["subst"]["case"], "acc-small")]["out_sha256"]
                      and r["process"]["sink_bytes"] == r["subst"]["out_bytes"]
                      and r["process"]["core"] != r["process"]["sink_core"]
                      and r["timing"]["iterations"] == 1 for r in rows))
        unsup = {r["pattern_id"] for r in comp_rows if r["compile_outcome"] == "unsupported-by-declaration"}
        want = {c["dir"] for c in cases if c["case"] in declared}
        check("subst tools %s harness: NO compile row for a compiled case (interpretive, S7/X41) and "
              "exactly the declared-unsupported cases %s as `unsupported-by-declaration` compile rows "
              "(X44/X45) with NO match rows for them" % (tid, sorted(declared)),
              len(comp_rows) == len(declared) and unsup == want
              and not ({r["pattern_id"] for r in rows} & unsup)
              and all(comp in r["declaration_ref"] for r in comp_rows))
    return say


PCREC_ARMS = ("pcrec-auto", "pcrec-vm", "pcrec-auto-sizefirst", "pcrec-vm-sizefirst")


def _pcrec_tier(check, sb, small, cases, work, _ad, harness, store, substrun):
    """Section 12 ([B140] step 3, lane b140pcrec): pcrec's substitution
    artifact. See the module docstring."""
    from pcrecbench.driverrun import run_driver
    exp = {(x["case"], x["subject"]): x for x in _read_tsv(os.path.join(SUBST, "expectations.tsv"))}
    div = _read_tsv(os.path.join(SUBST, "divergences.tsv"))
    lst = os.path.join(work, "list.tsv")
    with open(lst, "w") as f:
        f.write("acc-small\t%s\n" % small.path)
    outs = {}                   # (arm, case) -> output bytes' sha256
    engines = {}                # (arm, case) -> (engine, engine_sel)
    sample_lib = None
    for cid in PCREC_ARMS:
        ad, cfg = _ad.resolve(cid)
        wd = os.path.join(work, "pw-" + cid)
        ad.prepare(cid, wd)
        sup = ad.subst_support(cid)
        bad_cases = []
        for c in cases:
            p = sb.pattern(c["dir"])
            plan = substrun.plan_case(sb, p, sup)
            substrun.write_template(plan, os.path.join(wd, "p-" + p.name))
            cp = ad.compile(cid, p.name, sb.pattern_bytes(p.name),
                            {"substitution": True}, 1, wd)
            cr = cp.get("plain")
            if cr.outcome != "compiled":
                bad_cases.append("%s: %s %s" % (c["case"], cr.outcome, (cr.diagnostic or "")[:100]))
                continue
            engines[(cid, c["case"])] = (cr.engine_metadata.get("engine"),
                                         cr.engine_metadata.get("engine_sel"))
            lib = cr.handle["lib"]
            sample_lib = sample_lib or lib
            e = exp[(c["case"], "acc-small")]
            od = os.path.join(work, "po-%s-%s" % (cid, c["case"]))
            os.makedirs(od)
            argv = [cr.handle["driver"], "--lib", lib, "--mode", "subst",
                    "--sizing", cfg.get("subst_sizing", "bound"),
                    "--bound", "acc-small=%d" % (small.length + 8 * int(e["nsubst"]) + 1),
                    "--out-dir", od]
            r = run_driver(argv + ["--list", lst], timeout=120)
            row = r.rows[0] if r.rows else None
            got = (hashlib.sha256(open(os.path.join(od, row.out_path), "rb").read()).hexdigest()
                   if row is not None and row.out_path else None)
            outs[(cid, c["case"])] = got
            if (r.returncode != 0 or row is None or got != e["out_sha256"]
                    or row.nmatches != int(e["nsubst"]) or row.out_bytes != int(e["out_bytes"])
                    or row.iters != 1):
                bad_cases.append("%s: rc=%s %s" % (c["case"], r.returncode,
                                                   row.answer if row else r.diagnostic()))
            shutil.rmtree(od, ignore_errors=True)
        check("subst driver %s: --mode subst on acc-small, all 8 cases compiled through "
              "the adapter (rx artifact + subst artifact + support unit), output sha256 + "
              "count + length == expectations.tsv (cases 6 and 7 included)" % cid,
              not bad_cases and len([k for k in outs if k[0] == cid]) == 8,
              "; ".join(bad_cases[:3]))
    check("subst driver pcrec: each -sizefirst arm's 8 outputs are byte-identical to its "
          "bound sibling's (sha256), the two call shapes differ in time only",
          all(outs.get((a, c["case"])) == outs.get((a + "-sizefirst", c["case"])) is not None
              for a in ("pcrec-auto", "pcrec-vm") for c in cases))
    check("subst driver pcrec: case 7 (backreference in a negative lookahead) is the VM "
          "route under pcrec-auto as divergences.tsv predicted (`selected`), and "
          "forced under pcrec-vm",
          engines.get(("pcrec-auto", "7")) == ("vm", "selected")
          and engines.get(("pcrec-vm", "7")) == ("vm", "forced"), "%r" % (engines.get(("pcrec-auto", "7")),))
    pc_rows = {d["case"]: d for d in div if d["competitor"] == "pcrec"}
    check("subst divergences: the pcrec rows for cases 6 and 7 are `agrees` with basis "
          "`verified-small` - flipped from `predicted` by the four arms' sha256 equality "
          "above, never by editing the table alone",
          all(pc_rows.get(c, {}).get("expectation") == "agrees"
              and pc_rows[c]["basis"] == "verified-small" for c in ("6", "7"))
          and all(outs.get((a, c)) == exp[(c, "acc-small")]["out_sha256"]
                  for a in PCREC_ARMS for c in ("6", "7")))
    # ---- control: case 6 needs `subst-extended` (pcrec, by name)
    pcrec = _ad.resolve("pcrec-auto")[0].binary_for("pcrec-auto")
    t6 = os.path.join(work, "t6.tpl")
    open(t6, "wb").write(b"/\\U$1\\E/")
    r = subprocess.run([pcrec, "-p", "sub", "-o", os.path.join(work, "t6.c"), "--subst-file", t6],
                       capture_output=True)
    r2 = subprocess.run([pcrec, "-p", "sub", "--features", "subst-extended", "-o",
                         os.path.join(work, "t6.c"), "--subst-file", t6], capture_output=True)
    check("subst pcrec: case 6's template is REFUSED by pcrec without `--features "
          "subst-extended` (naming the module) and compiles with it (the control that "
          "the flag matters)",
          r.returncode != 0 and b"subst-extended" in r.stderr and r2.returncode == 0,
          (r.stderr or b"")[:120].decode("latin-1"))
    # ---- the support unit is PRIVATE to the shim's TU
    nm = subprocess.run(["nm", "-D", "--defined-only", sample_lib], capture_output=True, text=True).stdout
    check("subst pcrec: the support unit is private (PCREC_SUPPORT_STATIC) - the .so exports "
          "pb_subst_all and no pcrec_subst_* dynamic symbol",
          " pb_subst_all" in nm and "pcrec_subst" not in nm, nm[:200])
    # ---- driver refusals and the bound arm's NOSPACE
    drv = os.path.join(work, "pw-pcrec-auto", "pcrec_driver")
    base = [drv, "--lib", sample_lib, "--mode", "subst", "--list", lst, "--bound", "acc-small=9999999"]
    for flag in (["--find-all"], ["--prime"], ["--utf8"], ["--buffer-frames", "8", "--buffer-trail", "8"]):
        r = run_driver(base + flag, timeout=30)
        check("subst driver pcrec: %s is REFUSED in --mode subst by name" % flag[0],
              r.returncode == 2 and any("--mode subst" in e for e in r.errors),
              "rc=%s errors=%s" % (r.returncode, r.errors))
    r = run_driver(base[:-2], timeout=30)
    check("subst driver pcrec: a subject with no --bound is refused by name",
          r.returncode == 2 and any("--bound" in e for e in r.errors), "%r" % r.errors)
    r = run_driver(base[:-1] + ["acc-small=1000"], timeout=60)
    row = r.rows[0] if r.rows else None
    check("subst driver pcrec: a too-small bound is PCREC_SUBST_NOSPACE (giveup:-11), "
          "reported, never retried", row is not None and row.answer.startswith("giveup:-11:PCREC_SUBST_NOSPACE"),
          row.answer if row else r.diagnostic())
    # ---- through the harness
    ids = {}
    for cid in ("pcrec-auto", "pcrec-vm-sizefirst"):
        root = os.path.join(work, "pstore-" + cid)
        os.makedirs(root)
        res = harness.run_cell("subst", cid, trials=2, tier=store.TIER_SCRATCH,
                               store_root=root, subject_limit=1,
                               workdir=os.path.join(work, "phw-" + cid), synthetic=True)
        rows = [r for r in res.rows if r["kind"] == "match"]
        comp = [r for r in res.rows if r["kind"] == "compile"]
        ids[cid] = res.setup["testee"]["testee_id"] if "testee_id" in res.setup["testee"] \
            else _rec_id(res.setup["testee"])
        check("subst harness %s: a schema-1.9 record (validator-accepted) with 16 "
              "substitution rows (8 cases x 2 trials), every one matched-as-expected / gate "
              "agrees with the expectation's hash, 16 `compiled` compile rows (8 cases x 2 "
              "trials) and no `unsupported` row" % cid,
              len(rows) == 16 and res.setup["schema_version"] == "1.9"
              and res.setup["testee"]["invocation"] == "library"
              and all(r["match_outcome"] == "matched-as-expected"
                      and r["subst"]["gate"] == "agrees"
                      and r["subst"]["out_sha256"] == exp[(r["subst"]["case"], "acc-small")]["out_sha256"]
                      and r["timing"]["iterations"] == 1 for r in rows)
              and len(comp) == 16 and all(r["compile_outcome"] == "compiled" for r in comp),
              "rows=%d comp=%d" % (len(rows), len(comp)))
    check("subst harness pcrec: the bound and size-first arms derive DISTINCT testee ids "
          "(`..._sizefirst` last), so their records can never share a store path",
          ids["pcrec-auto"] != ids["pcrec-vm-sizefirst"] and ids["pcrec-vm-sizefirst"].endswith("sizefirst"),
          "%r" % (ids,))
    # ---- the gate: a deliberately wrong template fails by name
    ad, _c = _ad.resolve("pcrec-auto")
    wd = os.path.join(work, "pw-wrong")
    ad.prepare("pcrec-auto", wd)
    p = sb.pattern("1-literal")
    sup = ad.subst_support("pcrec-auto")
    wrong = substrun.plan_case(sb, p, sup, template_override=b"lit\tH2\n")
    substrun.write_template(wrong, os.path.join(wd, "p-" + p.name))
    cp = ad.compile("pcrec-auto", p.name, sb.pattern_bytes(p.name), {"substitution": True}, 1, wd)
    handle = dict(cp.get("plain").handle)
    handle["pin"], handle["subject_timeout"] = None, 60
    ents, _n = substrun.measure_cell(ad, handle, sb, p, wrong, sup, [small], 1, 60,
                                     lambda a, h: False)
    check("subst gate (pcrec): a deliberately WRONG template FAILS BY NAME - gate `wrong`, "
          "did-not-match-as-expected, not timed",
          ents[0]["subst"]["gate"] == "wrong" and ents[0]["outcome"] == "did-not-match-as-expected"
          and ents[0]["timing"] is None
          and "differs from the oracle's at byte" in ents[0]["diagnostic"])
    # ---- the roster: every other config refused by name, with its reason
    refused = {"pcrec-nocaps": "captures are off", "pcrec-auto-in": "frame buffer",
               "pcrec-auto-utf8": "utf8", "pcrec-auto-clang": "cc",
               "pcrec-auto-bigcap": "cap", "pcrec-auto-noedge": "denial",
               "pcrec-dfa": "forced dfa", "pcrec-local": "provided-binary"}
    bad_ref = []
    for cid, needle in refused.items():
        try:
            _ad.resolve(cid)[0].subst_support(cid)
            bad_ref.append("%s was ACCEPTED" % cid)
        except _ad.AdapterError as e:
            m = str(e)
            if "not on the substitution roster" not in m or needle.lower() not in m.lower():
                bad_ref.append("%s: %s" % (cid, m[:140]))
    check("subst roster pcrec: %d configs off the roster (%s) are each refused BY NAME with "
          "their reason; auto, vm and the sizefirst arms accepted" % (len(refused), ", ".join(sorted(refused))),
          not bad_ref, "; ".join(bad_ref[:3]))


def _rec_id(testee_block):
    from pcrecbench import record as _rec
    return _rec.derive_testee_id(testee_block)
