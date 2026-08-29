#!/usr/bin/env python3
r"""probe_engabs_longsubject_match.py -- [B18] (d): the LONG-SUBJECT FAILING
ANCHORED `_match` probe that pcrec's [ENG-ABS] pin (inbox I-16) was built
for, as an ARCHIVED DRIVER PROBE (pcrec D35 style).

THE CLAIM UNDER TEST (I-16): "a FAILING `_match` probe at byte 3 of a 1 MB
subject: 5.5 ns flat at every length (~62 % of that is the harness call)
vs 1.99 ms before -- O(divergence), not O(subject)".

WHY A PROBE AND NOT A CELL: the harness maps the `match` regime to the
SHORT subject set (pcrecbench/subbench.py `subjects_for`), and changing a
sub-bench's subject set bumps its version. So this script drives the
adapters' OWN drivers directly, on the sub-bench's OWN 1 MB throughput
subjects plus two cut prefixes, at the scratch tier: nothing here is a
record, nothing here enters a ranking.

WHAT IT REUSES rather than re-derives (the mandate: the same artifact the
harness would measure): `testees/pcrec/adapter.py`'s `_compile_one()` for
the `(?:orig)\z` whole-subject artifact (`pcrecbench.record.
whole_subject_text` is the ONE spelling), the pinned binary through the
adapter's `binary_for()` (the pin's `pin.sh` build; `pcrec-local` with
`$PCREC_BIN` = THAT binary for the control flag), `testees/pcre2/adapter.py`
's `compile()`, and both drivers' `--mode match` timing loop (the protocol
at the top of pcrecbench/adapters.py). The only thing this script adds is
per-(arm, subject) iteration calibration -- the harness calibrates on the
MEDIAN subject of a set, which would leave a 5 ns call at the timer floor
or a 1 ms call running for minutes.

ARMS (all: pattern `orig`, whole-subject form, captures on):
  pcrec-auto            the pin (DFA, RX_DFA_MATCH "unwrapped")
  pcrec-auto-noabs      the CONTROL: the same pin, `-fno-anchored-dfa`
                        (RX_DFA_MATCH "search-filter", the abi-9 form)
  pcrec-vm              --engine=vm at the same pin
  pcre2-jit, pcre2-interp
  floor                 a per-call CONTROL: the set's floor pattern (`@`),
                        same form, on pcrec-auto -- its anchored machine
                        dies at byte 0 of every subject here, so the number
                        is the driver loop + shim + entry with no scan in it

SUBJECTS: the five 1 MB throughput subjects of bench/email (email-specimen
@0.2), a 64 KB and a 4 KB `head -c` prefix of two of them (t-b-no-at,
early divergence; t-c-long-atom-run, divergence only at the end), and two
short subjects as sanity (s-000 matching, s-040 failing).

DIVERGENCE BYTE: where the anchored machine dies on each subject, computed
independently of every arm with libpcre2 (the bench's oracle library):
the smallest prefix length p at which `(?:orig)\z` under PCRE2_ANCHORED |
PCRE2_PARTIAL_HARD answers NOMATCH (neither a match nor a partial match --
no extension of the prefix can match). Monotone, so found by bisection.

Usage:
    python3 docs/dev/measurements/probe_engabs_longsubject_match.py \
        --out docs/dev/measurements/2026-08-29-engabs-longsubject-match-probe.txt
"""

import argparse
import ctypes
import datetime
import math
import os
import platform
import statistics
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))  # docs/dev/measurements -> repo
sys.path.insert(0, ROOT)

from pcrecbench import adapters as _ad            # noqa: E402
from pcrecbench import record as _rec             # noqa: E402
from pcrecbench import oracle_pcre2 as _ora       # noqa: E402
from pcrecbench.driverrun import C_ENV            # noqa: E402

EMAIL = os.path.join(ROOT, "bench", "email")
PCRE2_PARTIAL_HARD = 0x00000020   # pcre2.h; [measured] below against a
                                  # prefix that must answer partial
PCRE2_ERROR_NOMATCH = -1
PCRE2_ERROR_PARTIAL = -2


class Subject:
    __slots__ = ("subject_id", "path", "length", "note")

    def __init__(self, subject_id, path, note=""):
        self.subject_id, self.path, self.note = subject_id, path, note
        self.length = os.path.getsize(path)


def sha256(path):
    return _ad.sha256_file(path)


def loadavg():
    with open("/proc/loadavg") as f:
        return f.read().strip()


def run(argv, **kw):
    return subprocess.run(argv, capture_output=True, text=True, env=C_ENV,
                          **kw)


# ------------------------------------------------------------ divergence

def divergence_byte(pattern_bytes, subject_bytes):
    """-> the smallest prefix length p at which no extension of
    subject[:p] can match `(?:pattern)\\z` anchored at 0, or None when the
    whole subject is still alive (or matches). Uses libpcre2's hard partial
    matching; the relation is monotone in p."""
    lib = _ora._lib
    text = _rec.whole_subject_text(pattern_bytes)
    errcode = ctypes.c_int()
    erroff = ctypes.c_size_t()
    code = lib.pcre2_compile_8(text, len(text), 0, ctypes.byref(errcode),
                               ctypes.byref(erroff), None)
    if not code:
        raise RuntimeError("pcre2_compile failed: %d" % errcode.value)
    md = lib.pcre2_match_data_create_from_pattern_8(code, None)
    opts = _ora.PCRE2_ANCHORED | PCRE2_PARTIAL_HARD

    def alive(p):
        rc = lib.pcre2_match_8(code, subject_bytes, p, 0, opts, md, None)
        if rc == PCRE2_ERROR_NOMATCH:
            return False
        if rc == PCRE2_ERROR_PARTIAL or rc >= 0:
            return True
        raise RuntimeError("pcre2_match rc %d at prefix %d" % (rc, p))

    n = len(subject_bytes)
    try:
        if alive(n):
            return None
        # p = 0 is alive BY DEFINITION (the start state; the empty prefix
        # extends to every match) -- it is not queried, because libpcre2
        # answers NOMATCH on a zero-length subject here ([measured]: its
        # min-length start-up check fires before partial matching does).
        lo, hi = 0, n
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if alive(mid):
                lo = mid
            else:
                hi = mid
        return hi
    finally:
        lib.pcre2_match_data_free_8(md)
        lib.pcre2_code_free_8(code)


# ---------------------------------------------------------------- arms

class Arm:
    def __init__(self, name, adapter, testee_id, pattern_id, pattern, env,
                 note):
        self.name, self.adapter, self.testee_id = name, adapter, testee_id
        self.pattern_id, self.pattern = pattern_id, pattern
        self.env, self.note = env, note
        self.handle = None
        self.compile_argv = None
        self.info = {}
        self.metadata = {}
        self.diagnostic = None

    def apply_env(self):
        for k, v in self.env.items():
            os.environ[k] = v

    def clear_env(self):
        for k in self.env:
            os.environ.pop(k, None)

    def measure_argv(self):
        if self.adapter.name == "pcrec":
            return [self.handle["driver"], "--lib", self.handle["lib"],
                    "--mode", "match"] + list(self.handle.get("buffer_args") or [])
        return [self.handle["driver"], "--pattern", self.handle["pattern_file"],
                "--mode", "match"] + (["--jit"] if self.handle["jit"] else [])


def compile_arm(arm, workdir):
    """One artifact, one form, `trials=1`; the compile handle is what the
    harness's measure() would use. Compile timings are not this probe's
    subject and are not reported."""
    arm.apply_env()
    try:
        wd = os.path.join(workdir, arm.name)
        os.makedirs(wd, exist_ok=True)
        arm.adapter.prepare(arm.testee_id, wd)
        if arm.adapter.name == "pcrec":
            text = _rec.whole_subject_text(arm.pattern)
            cr = arm.adapter._compile_one(arm.testee_id, arm.pattern_id,
                                          _ad.FORM_WHOLE_SUBJECT, text, 1, wd)
            cfg = arm.adapter.config(arm.testee_id)
            arm.compile_argv = ([arm.adapter.binary_for(arm.testee_id), "-p", "rx"]
                                + list(cfg.get("flags", []))
                                + ["-o", "artifact.c", "--", text.decode("latin-1")])
        else:
            cp = arm.adapter.compile(arm.testee_id, arm.pattern_id,
                                     arm.pattern, {}, 1, wd)
            cr = cp.get(_ad.FORM_PLAIN)
            arm.compile_argv = ["(driver) --pattern <orig.rx> --mode match"
                                + (" --jit" if arm.adapter.config(
                                    arm.testee_id).get("jit") else "")
                                + "  [PCRE2_ANCHORED|PCRE2_ENDANCHORED at match time]"]
        if cr.outcome != "compiled":
            raise RuntimeError("%s: %s: %s" % (arm.name, cr.outcome, cr.diagnostic))
        arm.handle = cr.handle
        arm.metadata = cr.engine_metadata
        arm.diagnostic = cr.diagnostic
    finally:
        arm.clear_env()


def drive(arm, subject, iters, core, timeout=600):
    """ONE driver invocation on ONE subject: returns (raw_stdout, MatchRow
    or None, returncode). The raw text is what the archive keeps."""
    tmp = tempfile.mkdtemp(prefix="engabs-probe-")
    try:
        lst = os.path.join(tmp, "subjects.tsv")
        with open(lst, "w") as f:
            f.write("%s\t%s\n" % (subject.subject_id, os.path.abspath(subject.path)))
        argv = (["taskset", "-c", str(core), "gnutimeout", "-k", "5", str(timeout)]
                + arm.measure_argv() + ["--iters", str(iters), "--list", lst])
        proc = run(argv, cwd=tmp)
        row = None
        for line in (proc.stdout or "").splitlines():
            kind, payload = _ad.parse_driver_line(line)
            if kind == "subject":
                row = payload
            elif kind == "info" and arm.info is not None:
                arm.info[payload[0]] = payload[1]
        return proc.stdout, row, proc.returncode, argv
    finally:
        for fn in os.listdir(tmp):
            os.unlink(os.path.join(tmp, fn))
        os.rmdir(tmp)


def calibrate(arm, subject, core, target_s, cap):
    """iters so that ONE subject's loop runs >= target_s: probe at 10, then
    at the count the probe predicts (a second probe, because a 10-iteration
    loop of a 5 ns call is under the clock's own cost), then decide."""
    iters = 10
    for _ in range(3):
        out, row, rc, _argv = drive(arm, subject, iters, core)
        if row is None or rc != 0:
            return 1, "probe failed (rc %s)" % rc
        if not row.answer.startswith(("match", "nomatch")):
            return 1, "not timed: %s" % row.answer     # a give-up is not timed
        per = row.seconds / max(row.iters, 1)
        if row.seconds >= target_s:
            return iters, "probe met target at %d" % iters
        want = int(math.ceil(target_s / per)) if per > 0 else cap
        want = max(iters, min(want, cap))
        if want == iters:
            break
        iters = want
    return iters, "predicted from the probe"


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--workdir", default=None)
    ap.add_argument("--trials", type=int, default=5)
    ap.add_argument("--core", type=int, default=11)
    ap.add_argument("--target-seconds", type=float, default=0.2)
    ap.add_argument("--max-iters", type=int, default=100_000_000)
    args = ap.parse_args()

    workdir = args.workdir or tempfile.mkdtemp(prefix="engabs-probe-work-")
    os.makedirs(workdir, exist_ok=True)

    adapters = _ad.discover()
    pcrec, pcre2 = adapters["pcrec"], adapters["pcre2"]
    pin_bin = pcrec.pin_binary()
    pin_full, pin_desc = pcrec.pin_provenance()

    with open(os.path.join(EMAIL, "patterns", "orig.rx"), "rb") as f:
        orig = f.read()
    with open(os.path.join(EMAIL, "patterns", "floor.rx"), "rb") as f:
        floor = f.read()

    arms = [
        Arm("pcrec-auto", pcrec, "pcrec-auto", "orig", orig, {},
            "the pin: DFA, RX_DFA_MATCH unwrapped"),
        Arm("pcrec-auto-noabs", pcrec, "pcrec-local", "orig", orig,
            {"PCREC_BIN": pin_bin, "PCREC_LOCAL_FLAGS": "-fno-anchored-dfa"},
            "CONTROL: the same pin, -fno-anchored-dfa (RX_DFA_MATCH search-filter)"),
        Arm("pcrec-vm", pcrec, "pcrec-vm", "orig", orig, {},
            "--engine=vm at the pin"),
        Arm("pcre2-jit", pcre2, "pcre2-jit", "orig", orig, {},
            "libpcre2 JIT, PCRE2_ANCHORED|PCRE2_ENDANCHORED"),
        Arm("pcre2-interp", pcre2, "pcre2-interp", "orig", orig, {},
            "libpcre2 interpreter, PCRE2_ANCHORED|PCRE2_ENDANCHORED"),
        Arm("floor", pcrec, "pcrec-auto", "floor", floor, {},
            "CONTROL: the set's floor pattern (`@`), same form, pcrec-auto"),
    ]

    # subjects ---------------------------------------------------------
    tp = os.path.join(EMAIL, "throughput")
    subjects = []
    for sid in ("t-a-valid-addrs", "t-b-no-at", "t-c-long-atom-run",
                "t-d-prose-sparse-addrs", "t-e-prose-no-at"):
        subjects.append(Subject(sid, os.path.join(tp, sid + ".bin"),
                                "bench/email/throughput (manifest_throughput.tsv)"))
    cuts = os.path.join(workdir, "cuts")
    os.makedirs(cuts, exist_ok=True)
    for base in ("t-b-no-at", "t-c-long-atom-run"):
        for nbytes, tag in ((65536, "64k"), (4096, "4k")):
            p = os.path.join(cuts, "%s-%s.bin" % (base, tag))
            src = os.path.join(tp, base + ".bin")
            with open(src, "rb") as f, open(p, "wb") as g:
                g.write(f.read(nbytes))
            subjects.append(Subject("%s-%s" % (base, tag), p,
                                    "head -c %d of %s.bin" % (nbytes, base)))
    subjects.append(Subject("s-000", os.path.join(EMAIL, "subjects", "s-000.bin"),
                            "short, expected match (valid dot-atom simple)"))
    subjects.append(Subject("s-040", os.path.join(EMAIL, "subjects", "s-040.bin"),
                            "short, expected nomatch (missing @ entirely)"))

    # divergence bytes (oracle, independent of every arm) ----------------
    div = {}
    for s in subjects:
        with open(s.path, "rb") as f:
            data = f.read()
        div[s.subject_id] = divergence_byte(orig, data)
    # [measured] control for PCRE2_PARTIAL_HARD's value: a prefix that is
    # a valid address's local part must be ALIVE, and the same prefix plus
    # a space must be DEAD.
    assert divergence_byte(orig, b"abc") is None
    assert divergence_byte(orig, b"abc ") == 4

    # compile ---------------------------------------------------------------
    load_compile = [loadavg()]
    for arm in arms:
        compile_arm(arm, workdir)
    load_compile.append(loadavg())

    # calibrate ------------------------------------------------------------
    iters_for = {}
    cal_note = {}
    for arm in arms:
        for s in subjects:
            it, why = calibrate(arm, s, args.core, args.target_seconds,
                                args.max_iters)
            iters_for[(arm.name, s.subject_id)] = it
            cal_note[(arm.name, s.subject_id)] = why

    # measure: trials interleaved across arms ---------------------------------
    raw = {}       # (arm, subject) -> [(trial, argv, stdout)]
    rows = {}      # (arm, subject) -> [MatchRow]
    loads = []     # (trial, arm, before, after)
    t_start = datetime.datetime.now(datetime.timezone.utc)
    for trial in range(1, args.trials + 1):
        for arm in arms:
            before = loadavg()
            for s in subjects:
                key = (arm.name, s.subject_id)
                out, row, rc, argv = drive(arm, s, iters_for[key], args.core)
                raw.setdefault(key, []).append((trial, argv, out, rc))
                if row is not None:
                    rows.setdefault(key, []).append(row)
            loads.append((trial, arm.name, before, loadavg()))
    t_end = datetime.datetime.now(datetime.timezone.utc)

    # archive -----------------------------------------------------------------
    bench_commit = run(["git", "-C", ROOT, "rev-parse", "HEAD"]).stdout.strip()
    bench_dirty = run(["git", "-C", ROOT, "status", "--porcelain"]).stdout.strip()
    cc = os.environ.get("CC", "gcc")
    cc_ver = run([cc, "--version"]).stdout.splitlines()[0]
    pcre2_ver = pcre2.probe_version(os.path.join(workdir, "pcre2-jit"))
    with open(os.path.join(ROOT, "store", "machines.tsv")) as f:
        machines = f.read().strip()

    L = []
    w = L.append
    w("# [B18] (d) -- the long-subject FAILING anchored `_match` probe "
      "([ENG-ABS], pcrec inbox I-16 ask (c))")
    w("# ARCHIVED DRIVER PROBE (pcrec D35 style): stable name, verbatim "
      "driver output, source header. SCRATCH TIER by construction:")
    w("# not a record, not in store/, never a ranking input. Numbers only; "
      "the reading is the manager's.")
    w("#")
    w("# date (UTC)        %s .. %s" % (t_start.isoformat(timespec="seconds"),
                                      t_end.isoformat(timespec="seconds")))
    w("# bench commit      %s%s" % (bench_commit,
                                   " (DIRTY working tree)" if bench_dirty else ""))
    w("# pcrec pin         %s = %s (%s); binary %s sha256 %s"
      % (pcrec.pin(), pin_full, pin_desc, pin_bin, sha256(pin_bin)))
    w("# libpcre2          %s (the distribution libpcre2-8.so.0, dlopen'ed "
      "by the pcre2 driver)" % pcre2_ver)
    w("# compiler          %s (artifacts: $CC -O2 -std=gnu11 -fPIC -shared "
      "shim.c; drivers: $CC -O2 -std=gnu11)" % cc_ver)
    mrow = (machines.splitlines()[1].split("\t")
            if len(machines.splitlines()) > 1 else ["?"] * 4)
    w("# box               %s (%s, %s, %s cores; store/machines.tsv); "
      "kernel %s" % (mrow[0], mrow[1], mrow[2], mrow[3], platform.release()))
    w("# pinning           every driver invocation: taskset -c %d gnutimeout "
      "-k 5 600 <driver> ..." % args.core)
    w("# BOX NOT GATED     another manager session (pcrecdev1) had light "
      "lanes running; no quiet gate was applied. /proc/loadavg was sampled "
      "before and after every (trial, arm) sweep -- see LOAD below.")
    w("# script            docs/dev/measurements/%s" % os.path.basename(__file__))
    w("# invocation        %s" % " ".join(sys.argv))
    w("#")
    w("# PATTERN  bench/email/patterns/orig.rx (email-specimen@0.2), the "
      "WHOLE-SUBJECT form `(?:orig)\\z` on pcrec (pcrecbench.record."
      "whole_subject_text, the harness's own spelling); the plain pattern "
      "under PCRE2_ANCHORED|PCRE2_ENDANCHORED on libpcre2 -- exactly what "
      "the harness's `match` regime measures. Captures on. The floor arm "
      "uses patterns/floor.rx (`@`) the same way.")
    w("# OPERATION per call: pcrec driver `pb_match_caps(s, n, 0, caps) == n` "
      "(testees/pcrec/driver.c --mode match, the shim building an rx_ctx "
      "per call); pcre2 driver `pcre2_match_8(code, s, n, 0, ANCHORED|"
      "ENDANCHORED, md, NULL)`. One clock reading around the WHOLE loop of "
      "`iters` calls (CLOCK_MONOTONIC); ns/call = elapsed / iters.")
    w("# ITERS: calibrated per (arm, subject) so one loop runs >= %.2f s "
      "(cap %d); the harness calibrates on a set's median subject, which "
      "would put a 5 ns call at the timer floor. Same iters on every trial "
      "of a cell." % (args.target_seconds, args.max_iters))
    w("# TRIALS: %d, each a fresh driver process (dlopen / compile per "
      "process, outside the timed loop), INTERLEAVED across arms: trial 1 "
      "of every arm, then trial 2, ..." % args.trials)
    w("# TIMER FLOOR: two clock_gettime(CLOCK_MONOTONIC) reads bracket the "
      "loop, so the clock's own cost is amortised over `iters` (at 10^7 "
      "iters, < 0.01 ns/call). What is NOT amortised is the per-call harness "
      "cost inside the loop -- the indirect call, the shim's rx_ctx, the "
      "volatile stores -- which the `floor` arm measures directly: its "
      "anchored machine dies at byte 0 of every subject.")
    w("#")
    w("# ARMS")
    for arm in arms:
        w("#   %-18s testee %-12s %s" % (arm.name, arm.testee_id, arm.note))
        if arm.env:
            w("#   %-18s env: %s" % ("", " ".join("%s=%s" % kv
                                                    for kv in arm.env.items())))
        w("#   %-18s compile: %s" % ("", " ".join(arm.compile_argv)
                                         if arm.adapter.name == "pcrec"
                                         else arm.compile_argv[0]))
        if arm.adapter.name == "pcrec":
            m = arm.metadata
            w("#   %-18s stamps: engine=%s dfa_scan=%s dfa_prefilter=%s "
              "dfa_match=%s abi=%s%s"
              % ("", m.get("engine"), m.get("dfa_scan", "-"),
                 m.get("dfa_prefilter", m.get("prefilter", "-")),
                 m.get("dfa_match", "- (absent)"), m.get("abi"),
                 ("  [%s]" % arm.diagnostic) if arm.diagnostic else ""))
        w("#   %-18s measure: %s --iters <N> --list <id\\tpath>"
          % ("", " ".join(arm.measure_argv())))
    w("#")
    w("# SUBJECTS   (divergence = smallest prefix length p at which "
      "`(?:orig)\\z` anchored at 0 has NO matching extension of subject[:p], "
      "by libpcre2 PCRE2_ANCHORED|PCRE2_PARTIAL_HARD bisection; `-` = "
      "alive/matching to the end)")
    w("#   %-26s %9s %10s  %s" % ("id", "bytes", "divergence", "what"))
    for s in subjects:
        d = div[s.subject_id]
        w("#   %-26s %9d %10s  %s  sha256 %s"
          % (s.subject_id, s.length, "-" if d is None else d, s.note,
             sha256(s.path)[:16]))
    w("#")
    w("# LOAD  /proc/loadavg around the compile phase: %s | %s"
      % tuple(load_compile))
    w("# LOAD  /proc/loadavg before | after each (trial, arm) sweep over "
      "all %d subjects:" % len(subjects))
    for trial, name, b, a in loads:
        w("#   trial %d %-18s %s | %s" % (trial, name, b, a))
    w("#")
    w("# ITERS per (arm, subject), and how it was chosen:")
    for arm in arms:
        for s in subjects:
            k = (arm.name, s.subject_id)
            w("#   %-18s %-26s %10d  %s" % (arm.name, s.subject_id,
                                            iters_for[k], cal_note[k]))
    w("")
    w("=" * 78)
    w("VERBATIM DRIVER OUTPUT  (one block per (arm, subject); trial, argv, "
      "then the driver's stdout: `subject\\tID\\tANSWER\\tSTART\\tEND\\tNCAPS"
      "\\tCONSUMED\\tITERS\\tSECONDS\\tNMATCHES\\tCAPS`; info lines omitted "
      "after trial 1)")
    w("=" * 78)
    for arm in arms:
        for s in subjects:
            k = (arm.name, s.subject_id)
            w("")
            w("--- %s / %s" % k)
            for trial, argv, out, rc in raw[k]:
                w("trial %d: %s  (rc %d)" % (trial, " ".join(argv), rc))
                for line in out.splitlines():
                    if trial > 1 and (line.startswith("info\t")
                                      or line.startswith("compile\t")):
                        continue
                    w(line)
    w("")
    w("=" * 78)
    w("SUMMARY  median ns/call over %d trials; spread = (max - min) / median; "
      "answer as the driver reported it" % args.trials)
    w("=" * 78)
    names = [a.name for a in arms]
    w("%-26s %9s %10s  " % ("subject", "bytes", "divergence")
      + "  ".join("%22s" % n for n in names))
    for s in subjects:
        cells = []
        for arm in arms:
            rs = rows.get((arm.name, s.subject_id), [])
            timed = [r.seconds / r.iters * 1e9 for r in rs
                     if r.iters and r.seconds > 0
                     and r.answer in ("match", "nomatch")]
            if not timed:
                cells.append("%22s" % (rs[0].answer if rs else "no row"))
                continue
            med = statistics.median(timed)
            spread = (max(timed) - min(timed)) / med if med else 0.0
            ans = rs[0].answer
            cells.append("%13s %5.1f%% %s" % (fmt_ns(med), 100 * spread,
                                              "M" if ans == "match" else "n"))
        d = div[s.subject_id]
        w("%-26s %9d %10s  " % (s.subject_id, s.length, "-" if d is None else d)
          + "  ".join(cells))
    w("")
    w("(M = the driver answered `match`, n = `nomatch`; a give-up or error "
      "is printed in place of the number. ns/call is per whole-subject "
      "anchored probe; a `-` divergence is a subject whose anchored machine "
      "is alive to its last byte.)")
    w("")
    w("RATIOS  pcrec-auto-noabs / pcrec-auto (the same pin, the control "
      "flag vs the pin), by subject:")
    for s in subjects:
        a = med_for(rows, "pcrec-auto", s.subject_id)
        b = med_for(rows, "pcrec-auto-noabs", s.subject_id)
        if a and b:
            w("  %-26s %9d  %8.2fx" % (s.subject_id, s.length, b / a))

    # the workdir is session scratch; its path carries nothing reproducible
    text = "\n".join(L).replace(os.path.abspath(workdir), "<workdir>") + "\n"
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %s (%d lines); workdir %s" % (args.out, len(L), workdir))


def med_for(rows, arm, sid):
    rs = rows.get((arm, sid), [])
    timed = [r.seconds / r.iters * 1e9 for r in rs
             if r.iters and r.seconds > 0 and r.answer in ("match", "nomatch")]
    return statistics.median(timed) if timed else None


def fmt_ns(ns):
    if ns < 1000:
        return "%.2f ns" % ns
    if ns < 1e6:
        return "%.2f us" % (ns / 1e3)
    return "%.3f ms" % (ns / 1e6)


if __name__ == "__main__":
    main()
