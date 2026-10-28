"""pcrecbench/assists.py -- BUILD, COUNT and SELF-TEST an ASSIST ([B148] lane
b148aw; docs/design/unusual_set_v1.md 5, 7.1-7.4).

An assist is one file, `bench/unusual/assists/<member>/<engine>/assist.<ext>`
(C, C++ or Rust), authored from `bench/unusual/assists/templates/<engine>.<ext>`
by a blinded L6 lane. It defines the C ABI of `testees/assist/ub_assist.h`;
this module links it with the assist RUNNER (`testees/assist/ub_runner.c`,
the driver protocol, + `ub_timed.c`, the timed loops in a translation unit
of their own) and the engine's library into one driver binary, which the
`testees/assist/` adapter measures like any other driver.

    python3 -m pcrecbench assist-init     --member M --engine E
    python3 -m pcrecbench assist-selftest --member M --engine E [--file F]

The self-test runs the built driver over the member's PUBLIC sample
(`assists/problems/<family>-samples.tsv`) only -- never a held-out subject or
expectation -- and prints pass/fail per case plus the token count.

Fixture dirs: `$PCRECBENCH_ASSISTS_DIR` replaces `bench/unusual/assists` as
the place assists and their ledger are read from (the dummy assists of
`tools/check_assist.py` live under build/); the adapter then forces the
scratch tier.
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

from . import adapters as _ad

REPO = _ad.REPO_ROOT
SET_DIR = os.path.join(REPO, "bench", "unusual")
ASSISTS_DIR = os.path.join(SET_DIR, "assists")
TEMPLATES = os.path.join(ASSISTS_DIR, "templates")
PROBLEMS = os.path.join(ASSISTS_DIR, "problems")
RUNNER_DIR = os.path.join(_ad.TESTEES_ROOT, "assist")
COMMON_DIR = os.path.join(_ad.TESTEES_ROOT, "common")
BUILD_ROOT = os.path.join(REPO, "build", "assist")
ASSIST_VERSION = "v01"            # unusual@0.1 (P5)
ENV_DIR = "PCRECBENCH_ASSISTS_DIR"

sys.path.insert(0, os.path.join(REPO, "tools"))
import tokcount  # noqa: E402

#: family -> its members (the problem statements under assists/problems/)
FAMILIES = {
    "recursion": ("cscan", "wild-sexp-balanced", "wild-json-validate"),
    "callouts": ("co-luhn", "co-isbn", "co-member"),
    "netstr": ("co-netstr",),
    "vars": ("va-tenant", "va-route", "va-term", "va-term-bang"),
}
#: family -> the ledger's `feature` column (unusual_set_v1.md 3: netstrings
#: are a callouts member with its own problem statement)
FEATURE = {"recursion": "recursion", "callouts": "callouts",
           "netstr": "callouts", "vars": "vars"}
#: members whose answer token carries group 1 (calls_io.h `has_g1`)
HAS_G1 = {"cscan", "co-luhn", "co-isbn", "co-member", "co-netstr"}

#: engine -> the binding language, the template, the families it is
#: assisted for (unusual_set_v1.md 3.0), and the BASE config the assisted
#: config is (same library, same version; the assist is the difference).
ENGINES = {
    "pcre2": {"lang": "c", "ext": "c", "families": ("vars", "netstr"),
              "base": "pcre2-jit", "cflags": ["-DPCRE2_CODE_UNIT_WIDTH=8"],
              "libs": ["-lpcre2-8"]},
    "onig": {"lang": "c", "ext": "c", "families": ("vars", "netstr"),
             "base": "onig-default", "cflags": [], "libs": ["-lonig"]},
    "vectorscan": {"lang": "c", "ext": "c",
                   "families": ("recursion", "callouts", "netstr", "vars"),
                   "base": "vectorscan-block-som", "pkg": "libhs"},
    "re2": {"lang": "cpp", "ext": "cc",
            "families": ("recursion", "callouts", "netstr", "vars"),
            "base": "re2-default", "pkg": "re2"},
    "rust": {"lang": "rust", "ext": "rs",
             "families": ("recursion", "callouts", "netstr", "vars"),
             "base": "rust-default"},
}

#: the 43 (member, engine) pairs that need an assist
PAIRS = [(m, e) for e, spec in ENGINES.items() for f in spec["families"]
         for m in FAMILIES[f]]

C_FLAGS = ["-O2", "-std=gnu11"]
CXX_FLAGS = ["-O2", "-std=c++17"]
C_ENV = dict(os.environ, LC_ALL="C", LANG="C")


class AssistError(Exception):
    pass


def family_of(member):
    for f, ms in FAMILIES.items():
        if member in ms:
            return f
    raise AssistError("%r is not an assisted member (the members: %s)"
                      % (member, ", ".join(m for ms in FAMILIES.values() for m in ms)))


def engine_spec(engine):
    try:
        return ENGINES[engine]
    except KeyError:
        raise AssistError("no assist engine %r (have: %s)"
                          % (engine, ", ".join(ENGINES)))


def check_pair(member, engine):
    fam = family_of(member)
    if fam not in engine_spec(engine)["families"]:
        raise AssistError("%s (%s) is not assisted on %s: %s runs it natively"
                          % (member, fam, engine, engine))
    return fam


def assists_dir():
    return os.environ.get(ENV_DIR) or ASSISTS_DIR


def is_fixture_dir():
    return os.path.realpath(assists_dir()) != os.path.realpath(ASSISTS_DIR)


def template_path(engine):
    return os.path.join(TEMPLATES, "%s.%s" % (
        "pcre2" if engine == "pcre2" else engine, engine_spec(engine)["ext"]))


def assist_path(member, engine, root=None):
    return os.path.join(root or assists_dir(), member, engine,
                        "assist." + engine_spec(engine)["ext"])


# ---------------------------------------------------------------- templates

_FAM_OPEN = re.compile(r"^/\* ==== FAMILY (\S+) ==== \*/$")
_FAM_CLOSE = re.compile(r"^/\* ==== END FAMILY (\S+) ==== \*/$")


def instantiate(engine, family):
    """The template for `engine` with only `family`'s section kept (the
    FAMILY marker lines dropped) -> text. What assist-init writes, and what
    a filled assist's fences are compared with."""
    with open(template_path(engine), encoding="utf-8") as f:
        lines = f.read().split("\n")
    out, cur, seen = [], None, set()
    for ln in lines:
        mo, mc = _FAM_OPEN.match(ln), _FAM_CLOSE.match(ln)
        if mo:
            cur = mo.group(1)
            seen.add(cur)
            continue
        if mc:
            cur = None
            continue
        if cur is None or cur == family:
            out.append(ln)
    if family not in seen:
        raise AssistError("template %s has no FAMILY %s section"
                          % (template_path(engine), family))
    return "\n".join(out)


_FENCE_LINE = re.compile(r"^\s*/\*\s*(END\s+BOILERPLATE|BOILERPLATE\s+\S+)\s*\*/\s*$")


def fenced_regions(text):
    """-> [(opening fence line, region text)] in order: the declared
    boilerplate exactly as written (whitespace at line ends ignored)."""
    out, cur, buf = [], None, []
    for ln in text.split("\n"):
        m = _FENCE_LINE.match(ln)
        if m and not m.group(1).startswith("END"):
            cur, buf = ln.strip(), []
        elif m and cur is not None:
            out.append((cur, "\n".join(x.rstrip() for x in buf).strip("\n")))
            cur = None
        elif cur is not None:
            buf.append(ln)
    return out


def fence_drift(member, engine, path):
    """-> [problem] where the assist's fenced regions differ from the
    template's (the boilerplate is the template's, never the author's)."""
    fam = check_pair(member, engine)
    want = fenced_regions(instantiate(engine, fam))
    with open(path, encoding="utf-8") as f:
        have = fenced_regions(f.read())
    probs = []
    if len(want) != len(have):
        probs.append("%d fenced regions, the template has %d" % (len(have), len(want)))
    for i, (w, h) in enumerate(zip(want, have)):
        if w[0] == h[0] and "BOILERPLATE includes" in w[0]:
            # RULES.md lets `includes` hold any import line (the counter enforces the
            # shape and its 120-token cap): the author may ADD includes, never drop
            # the template's (manager ruling 2026-10-28, b148a-va-pcre2's report)
            miss = [ln for ln in w[1].split("\n") if ln.strip() and ln not in h[1].split("\n")]
            if miss:
                probs.append("fenced region %d (%s) drops the template's %s" % (i + 1, h[0], miss[0].strip()))
            continue
        if w != h:
            probs.append("fenced region %d (%s) differs from the template's" % (i + 1, h[0]))
    return probs


def init(member, engine, root=None, force=False):
    """assist-init: write the instantiated template where the author edits
    it. Refuses to overwrite an existing assist unless `force`."""
    fam = check_pair(member, engine)
    path = assist_path(member, engine, root)
    if os.path.exists(path) and not force:
        raise AssistError("%s exists (not overwritten)" % path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(instantiate(engine, fam))
    return path


def count(path):
    return tokcount.count_file(path)


# ------------------------------------------------------------------- ledger

def ledger(root=None):
    """-> {(member, engine): row dict + `line` (1-based) + `ref`}."""
    root = root or assists_dir()
    tsv = os.path.join(root, "assists.tsv")
    out = {}
    if not os.path.exists(tsv):
        return out
    with open(tsv, encoding="utf-8") as f:
        lines = f.read().split("\n")
    head = lines[0].split("\t") if lines else []
    for n, ln in enumerate(lines[1:], 2):
        if not ln.strip():
            continue
        d = dict(zip(head, ln.split("\t")))
        d["line"] = n
        inside = os.path.realpath(tsv).startswith(os.path.realpath(REPO) + os.sep)
        d["ref"] = "%s:%d" % (os.path.relpath(tsv, REPO) if inside
                              else os.path.abspath(tsv), n)
        out[(d.get("member"), d.get("engine"))] = d
    return out


def assisted_members(engine, root=None):
    """-> {member: ledger row} of the ASSISTED rows for `engine`."""
    return {m: d for (m, e), d in ledger(root).items()
            if e == engine and d.get("verdict") == "ASSISTED"}


def not_capable_members(engine, root=None):
    return {m: d for (m, e), d in ledger(root).items()
            if e == engine and d.get("verdict") == "NOT-CAPABLE"}


# -------------------------------------------------------------------- build

def _run(argv, cwd=None, timeout=600, env=None):
    proc = subprocess.run(argv, capture_output=True, text=True, cwd=cwd,
                          env=env or C_ENV, timeout=timeout)
    if proc.returncode != 0:
        raise AssistError("%s failed:\n%s\n%s" % (" ".join(argv), proc.stdout,
                                                  proc.stderr))
    return proc


def _sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def _pkg(name, what):
    return _run(["pkg-config", what, name]).stdout.split()


RUNNER_SOURCES = ["ub_runner.c", "ub_timed.c", "ub_defaults.c", "ub_assist.h",
                  "ub_timed.h"]


def runner_objects(callouts):
    """-> [object/archive paths] of the runner for one variant (with or
    without the callees), built once per source digest under
    build/assist/runner-<key>/. The archive (the family defaults) goes LAST
    on the link line."""
    h = hashlib.sha256()
    deps = [os.path.join(RUNNER_DIR, s) for s in RUNNER_SOURCES] + [
        os.path.join(COMMON_DIR, s) for s in ("calls_io.h", "vars_io.h", "ub_bind.h")]
    for d in deps:
        h.update(_sha(d).encode())
    h.update(b"co" if callouts else b"plain")
    h.update(" ".join(C_FLAGS).encode())
    d = os.path.join(BUILD_ROOT, "runner-" + h.hexdigest()[:16])
    objs = [os.path.join(d, "ub_runner.o"), os.path.join(d, "ub_timed.o")]
    lib = os.path.join(d, "libub_defaults.a")
    if callouts:
        objs.append(os.path.join(d, "ub_bind.o"))
    if all(os.path.exists(p) for p in objs + [lib]):
        return objs + [lib]
    os.makedirs(d, exist_ok=True)
    cc = ["gcc"] + C_FLAGS + ["-I", RUNNER_DIR]
    _run(cc + (["-DUB_CALLOUTS"] if callouts else []) + ["-c", "-o", objs[0],
         os.path.join(RUNNER_DIR, "ub_runner.c")])
    _run(cc + ["-c", "-o", objs[1], os.path.join(RUNNER_DIR, "ub_timed.c")])
    if callouts:
        from . import callees as _callees
        _run(["gcc"] + C_FLAGS + ["-c", "-o", objs[2], _callees.BIND_C])
    members = []
    for which in ("FIND", "VARS", "RESET"):
        o = os.path.join(d, "ub_default_%s.o" % which.lower())
        _run(cc + ["-DUB_DEFAULT_" + which, "-c", "-o", o,
                   os.path.join(RUNNER_DIR, "ub_defaults.c")])
        members.append(o)
    if os.path.exists(lib):
        os.unlink(lib)
    _run(["ar", "rcs", lib] + members)
    return objs + [lib]


def _rust_tool(name):
    found = shutil.which(name)
    if found:
        return found
    p = os.path.join(os.path.expanduser("~"), ".cargo", "bin", name)
    if os.path.exists(p):
        return p
    raise AssistError("%s not found on PATH or in ~/.cargo/bin" % name)


def _build_rust_lib(src, d):
    """The Rust assist as a staticlib: a per-build crate (Cargo.toml.in with
    the assist's path, the committed Cargo.lock), `cargo build --release
    --locked --offline` (never a download). -> (libpath, native libs, argv)."""
    crate = os.path.join(d, "crate")
    os.makedirs(crate, exist_ok=True)
    with open(os.path.join(RUNNER_DIR, "rust", "Cargo.toml.in"), encoding="utf-8") as f:
        toml = f.read().replace("@ASSIST_RS@", os.path.abspath(src).replace("\\", "/"))
    with open(os.path.join(crate, "Cargo.toml"), "w", encoding="utf-8") as f:
        f.write(toml)
    shutil.copyfile(os.path.join(RUNNER_DIR, "rust", "Cargo.lock"),
                    os.path.join(crate, "Cargo.lock"))
    argv = [_rust_tool("cargo"), "rustc", "--release", "--locked", "--offline",
            "--manifest-path", os.path.join(crate, "Cargo.toml"),
            "--target-dir", os.path.join(d, "target"), "--",
            "--print", "native-static-libs"]
    proc = _run(argv)
    native = []
    for ln in (proc.stderr or "").splitlines():
        if "native-static-libs:" in ln:
            native = ln.split("native-static-libs:", 1)[1].split()
    return os.path.join(d, "target", "release", "libub_assist.a"), native, argv


def build(member, engine, src=None, out_dir=None, count=False):
    """Build the assist driver for (member, engine) from `src` (default: the
    ledger's file). -> (binary path, provenance dict {command_line,
    compiler, callees_sha256 (callouts only)}). Cached on the digest of the
    assist + the runner. `count=True` (callouts only) links callees.o's
    counting twin instead: the harness's untimed fire pass."""
    fam = check_pair(member, engine)
    spec = engine_spec(engine)
    src = os.path.abspath(src or assist_path(member, engine))
    if not os.path.exists(src):
        raise AssistError("no assist at %s (assist-init writes one)" % src)
    callouts = fam == "callouts"
    runner = runner_objects(callouts)
    h = hashlib.sha256(_sha(src).encode())
    for r in runner:
        h.update(_sha(r).encode())
    if count:
        h.update(b"count")
    key = h.hexdigest()[:16]
    d = out_dir or os.path.join(BUILD_ROOT, "%s-%s-%s" % (member, engine, key))
    os.makedirs(d, exist_ok=True)
    out = os.path.join(d, "assist_driver")
    inc = ["-I", RUNNER_DIR, "-I", ASSISTS_DIR]
    extra_objs = []
    callees_sha = None
    if callouts:
        from . import callees as _callees
        obj, callees_sha = _callees.ensure(count=count)
        extra_objs.append(obj)
    if spec["lang"] in ("c", "cpp"):
        cflags = list(spec.get("cflags", []))
        libs = list(spec.get("libs", []))
        if spec.get("pkg"):
            cflags += _pkg(spec["pkg"], "--cflags")
            libs += _pkg(spec["pkg"], "--libs")
        cc = "gcc" if spec["lang"] == "c" else "g++"
        flags = C_FLAGS if spec["lang"] == "c" else CXX_FLAGS
        aobj = os.path.join(d, "assist.o")
        compile_argv = [cc] + flags + inc + cflags + ["-c", "-o", aobj, src]
        link_argv = [cc, "-o", out, aobj] + runner[:-1] + extra_objs + [runner[-1]] + libs
        if not os.path.exists(out):
            _run(compile_argv)
            _run(link_argv)
        cmd = compile_argv + ["&&"] + link_argv
        compiler = cc
    else:
        lib, native, cargo_argv = (None, None, None)
        link_argv = None
        if not os.path.exists(out):
            lib, native, cargo_argv = _build_rust_lib(src, d)
            link_argv = (["gcc", "-o", out] + runner[:-1] + extra_objs
                         + [lib, runner[-1]] + native)
            _run(link_argv)
            with open(os.path.join(d, "link.cmd"), "w") as f:
                f.write(" ".join(cargo_argv) + "\n" + " ".join(link_argv) + "\n")
        with open(os.path.join(d, "link.cmd")) as f:
            cmd = f.read().split()
        compiler = "rustc"
    prov = {"command_line": cmd, "compiler": compiler}
    if callees_sha:
        prov["callees_sha256"] = callees_sha
    return out, prov


# ----------------------------------------------------------------- selftest

def _read_samples(family):
    path = os.path.join(PROBLEMS, "%s-samples.tsv" % family)
    with open(path, encoding="utf-8") as f:
        lines = [l.rstrip("\n").split("\t") for l in f if l.strip()]
    head = lines[0]
    return [dict(zip(head, r)) for r in lines[1:]]


SELFTEST_MEMBER_SET = ("mona", "nick", "olga", "pete", "quinn", "rhea", "sam",
                       "tina", "uma", "vic", "log-shipper", "ci_runner")


def _callee_spec(member, tmp):
    """The `--callees` spec of the self-test: the member's site bound to its
    shared predicate; co-member's set is the problem statement's twelve
    names (callouts.md 6), never the held-out run's."""
    site, callee = {"co-luhn": ("1", "luhn"), "co-isbn": ("2", "isbn13"),
                    "co-member": ("3", None)}[member]
    if callee is None:
        names = os.path.join(tmp, "names.tsv")
        with open(names, "w") as f:
            f.write("\n".join(SELFTEST_MEMBER_SET) + "\n")
        callee = "member:" + names
    return "%s=%s" % (site, callee)


def _run_driver(argv, timeout=120):
    from . import driverrun as _dr
    return _dr.run_driver(argv, timeout=timeout)


def selftest(member, engine, src=None, out=print):
    """Build the assist and run it over the member's PUBLIC sample. -> (n
    passed, n cases, count dict). Prints one line per case."""
    fam = check_pair(member, engine)
    src = os.path.abspath(src or assist_path(member, engine))
    cnt = count(src)
    drift = fence_drift(member, engine, src)
    drv, _prov = build(member, engine, src)
    rows = [r for r in _read_samples(fam) if r["member"] == member]
    if not rows:
        raise AssistError("no %s cases in %s-samples.tsv" % (member, fam))
    tmp = tempfile.mkdtemp(prefix="assist-selftest-")
    try:
        pat = os.path.join(tmp, "pattern.rx")
        with open(pat, "wb") as f:
            f.write(_pattern_bytes(member))
        base = [drv, "--pattern", pat, "--member", member]
        if fam == "callouts":
            base += ["--callees", _callee_spec(member, tmp)]
        results = _selftest_tokens(fam, member, rows, base, tmp)
        findalls = {} if fam == "vars" else _selftest_findall(rows, base, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    passed = 0
    for r in rows:
        got = results.get(r["case"])
        ok = got == r["expected"]
        fa_want = r.get("findall", "-")
        fa_got = findalls.get(r["case"])
        if fam != "vars" and fa_want not in ("", "-", None):
            ok = ok and fa_got == fa_want
        passed += ok
        out("%s\t%s\t%s\tgot %s%s\twant %s%s" % (
            "PASS" if ok else "FAIL", r["case"], r.get("note", ""), got,
            "" if fa_got is None else " findall=%s" % fa_got, r["expected"],
            "" if fam == "vars" or fa_want in ("", "-") else " findall=%s" % fa_want))
    out("%s/%s: %d/%d cases pass; %d tokens (%s), %d lines, budget %d -> %s%s" % (
        member, engine, passed, len(rows), cnt["tokens"], cnt["counter"],
        cnt["lines"], tokcount.BUDGET, tokcount.verdict_of(cnt["tokens"]),
        "" if not cnt["smuggled"] else "; SMUGGLED: %s" % cnt["smuggled"]))
    for p in drift:
        out("FENCE: " + p)
    return passed, len(rows), cnt, drift


def _pattern_bytes(member):
    with open(os.path.join(SET_DIR, "patterns", member + ".rx"), "rb") as f:
        return f.read()


def _selftest_tokens(fam, member, rows, base, tmp):
    """One call per case (at the sample's `start`), all cases in one
    `--mode calls` run; -> {case: token}."""
    listf = os.path.join(tmp, "calls.list")
    toks = os.path.join(tmp, "tok")
    os.makedirs(toks, exist_ok=True)
    with open(listf, "w") as lf:
        for r in rows:
            cid = r["case"]
            hexcol = "line_hex" if fam == "vars" else "subject_hex"
            subj = bytes.fromhex(r[hexcol])
            sp = os.path.join(tmp, cid + ".subj")
            with open(sp, "wb") as f:
                f.write(subj)
            start = int(r.get("start") or 0)
            cp = os.path.join(tmp, cid + ".calls")
            binding = "b0" if fam == "vars" else "-"
            with open(cp, "w") as f:
                f.write("call_id\toffset\tlength\tsegment_bytes\tbinding\n")
                f.write("0\t%d\t%d\t%d\t%s\n" % (start, len(subj) - start,
                                                 len(subj) - start, binding))
            if fam == "vars":
                bp = os.path.join(tmp, cid + ".bind")
                with open(bp, "w") as f:
                    f.write("binding_id\tname\tvalue\n")
                    for item in (r["bindings"] or "").split(";"):
                        item = item.strip()
                        if not item:
                            continue
                        name, _, val = item.partition("=")
                        f.write("b0\t%s\t%s\n" % (name, val))
                    f.write("b0\t__selftest__\tUNSET\n")   # never empty
                lf.write("%s\t%s\t%s\t%s\n" % (cid, sp, cp, bp))
            else:
                lf.write("%s\t%s\t%s\n" % (cid, sp, cp))
    argv = base + ["--has-g1", "1" if member in HAS_G1 else "0", "--list",
                   listf, "--mode", "calls", "--iters", "1", "--tokens-dir",
                   toks, "--subject-timeout", "20"]
    # run directly, not through driverrun: its stream parser hashes and
    # REMOVES each token file, and the self-test reads the token itself
    proc = subprocess.run(argv, capture_output=True, text=True, env=C_ENV,
                          timeout=300)
    out = {}
    for ln in proc.stdout.splitlines():
        kind, payload = _ad.parse_driver_line(ln)
        if kind == "subject" and payload.answer != "stream":
            out[payload.subject_id] = payload.answer     # timedout / crashed
        elif kind == "error":
            raise AssistError("the assist driver refused: %s" % payload)
    if proc.returncode != 0 and not out:
        raise AssistError("the assist driver exited %d: %s" % (
            proc.returncode, (proc.stderr or "").strip()))
    for r in rows:
        p = os.path.join(toks, r["case"] + ".tok")
        if os.path.exists(p) and r["case"] not in out:
            with open(p) as f:
                out[r["case"]] = f.read().strip()
    return out


def _selftest_findall(rows, base, tmp):
    """The `findall` column: the driver's own find-all loop from offset 0
    (`--mode search --find-all`) -> {case: count text}."""
    listf = os.path.join(tmp, "search.list")
    want = [r for r in rows if r.get("findall") not in (None, "", "-")]
    if not want:
        return {}
    with open(listf, "w") as lf:
        for r in want:
            sp = os.path.join(tmp, r["case"] + ".subj")
            lf.write("%s\t%s\n" % (r["case"], sp))
    res = _run_driver(base + ["--list", listf, "--mode", "search", "--iters",
                              "1", "--find-all", "--subject-timeout", "20"])
    out = {}
    for row in res.rows:
        if row.answer == "match":
            out[row.subject_id] = str(row.nmatches)
        elif row.answer == "nomatch":
            out[row.subject_id] = "0"
        else:
            out[row.subject_id] = row.answer
    return out


# ---------------------------------------------------------------------- CLI

def main_init(args):
    try:
        path = init(args.member, args.engine, force=args.force)
    except AssistError as e:
        print("assist-init: %s" % e, file=sys.stderr)
        return 2
    c = count(path)
    print("%s\tthe %s template, %d tokens before you write anything"
          % (path, family_of(args.member), c["tokens"]))
    return 0


def main_selftest(args):
    try:
        passed, n, cnt, drift = selftest(args.member, args.engine, src=args.file)
    except (AssistError, tokcount.LexError, tokcount.FenceError) as e:
        print("assist-selftest: %s" % e, file=sys.stderr)
        return 2
    return 0 if passed == n and not drift and not cnt["smuggled"] else 1
