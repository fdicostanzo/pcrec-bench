"""callees.py -- [B148] L5: the ONE build of the unusual set's shared callout
callees (docs/design/unusual_set_v1.md 3.2, r9 C5; bench/unusual/callees/).

`callees.o` is compiled ONCE with FIXED flags -- never `$CC`/`$CFLAGS`, never a
testee's own flags -- and every native-callout driver (libpcre2, Oniguruma)
and pcrec's callout artifact links that same object; its sha256 is the
compile-scope `engine_metadata` `callees_sha256` on every callout row. The
counting object (`-DUB_COUNT`) is the only one with a counter; it is linked
into the untimed fire-pass binaries and never into a timed one.

The build is cached under `build/callees/<key>/`, the key the sha256 of the
sources, the flags and `gcc --version`, so "once" holds across cells and
processes; a concurrent builder writes a temp file and renames it.

The flags carry `-fPIC` beside the design's `-O2 -fno-lto` so the SAME object
links into an executable (the pcre2/onig drivers) and into pcrec's shared
artifact alike (a non-PIC object cannot go into a .so).
"""

import hashlib
import os
import subprocess
import tempfile

from . import adapters as _ad

REPO = _ad.REPO_ROOT
SRC_DIR = os.path.join(REPO, "bench", "unusual", "callees")
SOURCES = [os.path.join(SRC_DIR, "callees.c"), os.path.join(SRC_DIR, "callees.h")]
CC = "gcc"
FLAGS = ["-O2", "-fno-lto", "-fPIC", "-std=gnu11"]
COUNT_FLAGS = FLAGS + ["-DUB_COUNT"]
BIND_C = os.path.join(_ad.TESTEES_ROOT, "common", "ub_bind.c")
BIND_DEPS = [BIND_C, os.path.join(_ad.TESTEES_ROOT, "common", "ub_bind.h")] + SOURCES
BUILD_ROOT = os.path.join(REPO, "build", "callees")

#: the compile-scope pair every callout-family row carries, plus the arm and
#: the bound spec; the match-scope fire pair from the counting pass.
CALLOUT_DECL = {
    "callees_sha256": {
        "type": "sha256", "scope": "pattern",
        "source": "pcrecbench/callees.py: sha256 of the ONE callees.o every "
                  "native-callout driver links (fixed flags, built once)",
        "description": "identity of the shared callee object (unusual_set_v1.md 3.2); "
                       "ABSENT on a unity build, which recompiles callees.c"},
    "callout_arm": {
        "type": "string", "scope": "pattern",
        "source": "the pattern's `arm-*` tag (bench/unusual/members.py)",
        "description": "real | pass | twin | pass-nofn: which callout arm this row is"},
    "callout_spec": {
        "type": "string", "scope": "pattern",
        "source": "the set's [callouts] table, member paths relative to the set",
        "description": "the binding spec the driver bound (site=callee,...); `none` "
                       "for pass-nofn (no callout function at all)"},
    "callout_fires": {
        "type": "integer", "scope": "match",
        "source": "the untimed COUNTING build (-DUB_COUNT), one fresh process per "
                  "subject, iters 1 (unusual_set_v1.md 3.2 calibration item 1)",
        "description": "callee calls for ONE iteration of this row's operation; "
                       "absent where the engine has no counting build"},
    "callout_respell": {
        "type": "string", "scope": "pattern",
        "source": "the adapter's site respelling, Oniguruma only",
        "description": "`(?CN)->(?{N})`: the set's PCRE spelling of a numbered "
                       "callout respelled to Oniguruma's contents callout before "
                       "onig_new (unusual_set_v1.md 3.2)"},
    "callout_views_sha256": {
        "type": "sha256", "scope": "match",
        "source": "the counting build's fire log, its lines SORTED then hashed",
        "description": "the MULTISET of views the callee was shown (pos, group 1, "
                       "verdict): compared across engines, differences reported"},
}


def _key(flags):
    h = hashlib.sha256()
    for p in SOURCES:
        with open(p, "rb") as f:
            h.update(f.read())
    h.update(" ".join(flags).encode())
    try:
        v = subprocess.run([CC, "--version"], capture_output=True, text=True,
                           timeout=30).stdout.splitlines()[0]
    except (OSError, IndexError, subprocess.SubprocessError):
        v = "?"
    h.update(v.encode())
    return h.hexdigest()[:16]


def _sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def ensure(count=False):
    """-> (path, sha256) of callees.o (count=False) or callees_count.o."""
    flags = COUNT_FLAGS if count else FLAGS
    name = "callees_count.o" if count else "callees.o"
    d = os.path.join(BUILD_ROOT, _key(flags))
    out = os.path.join(d, name)
    if not os.path.exists(out):
        os.makedirs(d, exist_ok=True)
        fd, tmp = tempfile.mkstemp(prefix=".tmp-", suffix=".o", dir=d)
        os.close(fd)
        argv = [CC] + flags + ["-c", "-o", tmp, SOURCES[0]]
        proc = subprocess.run(argv, capture_output=True, text=True, timeout=300)
        if proc.returncode != 0:
            os.unlink(tmp)
            raise _ad.AdapterError("building %s failed:\n%s\n%s"
                                   % (name, " ".join(argv), proc.stderr))
        with open(os.path.join(d, name + ".cmd"), "w") as f:
            f.write(" ".join(argv[:-1] + [SOURCES[0]]) + "\n")
        os.replace(tmp, out)
    return out, _sha(out)


def link_inputs(count=False):
    """-> (extra link args, the callee object path, its sha256): what a
    callout driver links beside its own sources -- the binding parser's
    source and the ONE callee object."""
    obj, sha = ensure(count)
    return [BIND_C, obj], obj, sha


def arm_of(pattern):
    """The callout arm a pattern's tags declare, or None (not a callout
    member)."""
    for t in pattern.tags or ():
        if t.startswith("arm-"):
            return t[len("arm-"):]
    return None


def options_for(sb, pattern):
    """-> the `callouts` compile option for a pattern of an unusual set, or
    None. {arm, spec}; `spec` None for pass-nofn. Member paths in the set's
    [callouts] table are relative to the set and resolved here."""
    table = sb.cfg.get("callouts")
    if not table:
        return None
    arm = arm_of(pattern)
    if arm is None:
        return None
    key = {"real": "real", "twin": "real", "pass": "pass"}.get(arm)
    spec = None
    if key:
        parts = []
        for item in table[key].split(","):
            k, _, callee = item.partition("=")
            if callee.startswith("member:"):
                callee = "member:" + os.path.join(sb.root, callee[len("member:"):])
            parts.append("%s=%s" % (k, callee))
        spec = ",".join(parts)
    # `spec` is what the driver binds (member paths absolute); `spec_decl` is
    # what the record says (the set's own table text, paths set-relative).
    return {"arm": arm, "spec": spec,
            "spec_decl": table[key] if key else "none"}


def spec_pairs(spec):
    """-> [(key, callee)] of a binding spec, in its order."""
    return [tuple(item.partition("=")[::2]) for item in (spec or "").split(",")
            if item]


def compile_metadata(co, sha=None):
    """The compile-scope callout pairs for a row compiled under `co`
    (options_for's dict); `sha` the callee object linked, None when none
    is (a pcrec twin has no site and links no callee)."""
    meta = {"callout_arm": co["arm"], "callout_spec": co["spec_decl"]}
    if sha:
        meta["callees_sha256"] = sha
    return meta


def co_driver(build_driver, source, output, base_extra, extra_sources,
              wrapper, count=False):
    """Build a callout driver: `source` compiled with -DPB_CALLOUTS beside
    the engine's own instrument TUs, its `wrapper` TU, the binding parser
    and the ONE callee object (the counting one when `count`). -> (path,
    the callee object's sha256)."""
    inputs, _obj, sha = link_inputs(count)
    path = build_driver(source, output,
                        extra=["-DPB_CALLOUTS", wrapper] + inputs + list(base_extra),
                        extra_sources=extra_sources)
    return path, sha


class fire_log_env:
    """`with fire_log_env(path):` -- every driver process started inside
    gets UB_FIRE_LOG=path (the counting callees append to it). Mutates
    driverrun.C_ENV for the block only; the untimed fire pass is its only
    user."""

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        from . import driverrun
        driverrun.C_ENV["UB_FIRE_LOG"] = self.path
        return self

    def __exit__(self, *exc):
        from . import driverrun
        driverrun.C_ENV.pop("UB_FIRE_LOG", None)
        return False


def fire_log_digest(path):
    """-> (fires, sha256 of the SORTED lines) of a counting build's fire log
    (an absent file = zero fires)."""
    try:
        with open(path, "rb") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        lines = []
    lines.sort()
    return len(lines), hashlib.sha256(b"".join(l + b"\n" for l in lines)).hexdigest()
