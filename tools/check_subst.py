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
