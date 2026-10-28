"""callout_calib.py -- THE CALLEE-SHARE CALIBRATION ([B148] L5,
docs/design/unusual_set_v1.md 3.2 calibration items 1-3): how much of a real
callout arm's row time is the callee's own work, on EVERY native engine.

    python3 tools/callout_calib.py [--cpu N] [--launches 11] [--regime throughput]

For each native config x real-arm callout member (the set's own throughput
subject, one 1 MB find-all row each):

  1. fires     -- the untimed COUNTING build's fire pass (harness.fire_pass),
                  one fresh process, iters 1: the callee calls ONE iteration
                  of the row's operation makes, and the views it was shown;
  2. row_ns    -- the TIMED build (the one a cell measures), the median of
                  `--launches` fresh driver launches pinned to `--cpu`
                  (taskset), iters 1 (a 1 MB find-all is milliseconds); the
                  -pass and -twin arms the same way, for context;
  3. ns/fire   -- bench/unusual/callees/replay.c, built against the SAME
                  timed callees.o, replays the logged views through the same
                  binding table and the same indirect call, pinned to the
                  same core, median of 11 timed rounds;
  share = fires x ns/fire / row_ns; and (3.2 items 3 + 5) the -pass arm's own
  fires, with (real - pass) / fires printed only where the two arms fire
  equally -- the in-situ cross-check of the replay's ns/fire.

The budget (3.2): ~20 % of the row on pcre2-jit; any engine over 40 % is
FLAGGED (the callee, not the engine, would be what the row measures). The box
load (/proc/loadavg before and after, and the target core's busy share over
the run from /proc/stat) is printed with the numbers: this is a calibration
read on a shared box, never a record. Writes nothing in the repo; scratch
under build/callout-calib/.
"""
import argparse
import os
import shutil
import statistics
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

WORK = os.path.join(ROOT, "build", "callout-calib")
# pcre2-jit-deep: the JIT gives up JIT_STACKLIMIT on co-netstr-assist at the
# default 32 KiB stack (a 955k-step lazy loop); its deep arm is the reading
NATIVE = ["pcre2-interp", "pcre2-jit", "pcre2-jit-deep", "pcrec-auto", "pcrec-vm",
          "onig-default"]
MEMBERS = ["co-luhn", "co-isbn", "co-member", "co-netstr-assist", "co-netstr"]


def build_replay():
    from pcrecbench import callees
    obj, sha = callees.ensure()
    exe = os.path.join(WORK, "replay")
    subprocess.run([callees.CC, "-O2", "-std=gnu11", "-o", exe,
                    os.path.join(callees.SRC_DIR, "replay.c"), callees.BIND_C, obj],
                   check=True, capture_output=True, timeout=120)
    return exe, sha


def row_ns(ad, handle, regime, subj, launches):
    out = []
    for _ in range(launches):
        by_trial, _i, _n = ad.measure(handle, regime, [subj], 1, 1, timeout=600)
        r = by_trial[0][0]
        out.append(r.seconds / r.iters * 1e9)
    return statistics.median(out), r.answer, r.nmatches


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cpu", type=int, default=7)
    ap.add_argument("--launches", type=int, default=11)
    ap.add_argument("--regime", default="throughput")
    a = ap.parse_args()
    from pcrecbench import adapters as _ad, callees, capability, harness as _h, quiet, \
        subbench as _sbm
    shutil.rmtree(WORK, ignore_errors=True)
    os.makedirs(WORK)
    sb = _sbm.load(os.path.join(ROOT, "bench", "unusual"))
    replay, sha = build_replay()
    pin = quiet.taskset_prefix(quiet.pinning(a.cpu))
    load0, t0, w0 = quiet.loadavg(), quiet.cpu_times(), time.time()
    print("# callout_calib: callees.o %s, regime %s, cpu %d, %d launches/arm"
          % (sha[:12], a.regime, a.cpu, a.launches))
    print("# load before: %s" % " ".join("%.2f" % x for x in load0))
    print("\t".join(["testee", "member", "subject", "fires", "ns_per_fire", "callee_ns",
                     "real_ns", "pass_ns", "twin_ns", "share", "pass_fires",
                     "real_minus_pass_per_fire", "flag"]))
    pats = {p.name: p for p in sb.patterns}
    for t in NATIVE:
        ad, _cfg = _ad.resolve(t)
        w = os.path.join(WORK, t)
        ad.prepare(t, w)
        for m in MEMBERS:
            p = pats[m]
            if capability.missing_capabilities(sb, t, p):
                continue
            # the member's own throughput subject (co-netstr-assist shares co-netstr's)
            stem = "co-netstr" if m.startswith("co-netstr") else m
            subj = [s for s in sb.subjects_for(a.regime) if s.subject_id.startswith(stem)][0]
            ns = {}
            pass_fires = None
            for arm in ("", "-pass", "-twin"):
                pid = m + arm
                if pid not in pats:
                    continue
                cp = ad.compile(t, pid, sb.pattern_bytes(pid),
                                {"callouts": callees.options_for(sb, pats[pid])}, 1, w)
                res = cp.forms["plain"]
                if res.outcome != "compiled":
                    ns[arm] = None
                    continue
                h = dict(res.handle, pin=pin)
                med, answer, _nm = row_ns(ad, h, a.regime, subj, a.launches)
                ns[arm] = med
                if arm == "":
                    real_answer = answer
                if arm == "-pass":
                    pf = _h.fire_pass(ad, h, a.regime, [subj], 600,
                                      os.path.join(w, "fires", pid))
                    pass_fires = pf.get(subj.subject_id, {}).get("callout_fires")
                if arm == "":
                    logdir = os.path.join(w, "fires", m)
                    fires = _h.fire_pass(ad, h, a.regime, [subj], 600, logdir)
                    n = fires[subj.subject_id]["callout_fires"]
                    spec = callees.options_for(sb, p)["spec"]
                    o = subprocess.run(pin + [replay, spec, subj.path,
                                              os.path.join(logdir, subj.subject_id + ".fires"), "11"],
                                       capture_output=True, text=True, timeout=600)
                    cols = o.stdout.split("\t")
                    if o.returncode != 0 or len(cols) < 7 or cols[6].strip() != "yes":
                        raise SystemExit("replay failed on %s %s: %s %s" % (t, m, o.stdout, o.stderr))
                    per = float(cols[4]) if cols[4] != "-" else 0.0
            if ns.get("") is None:
                print("\t".join([t, m, subj.subject_id, "-", "-", "-", "refused", "-", "-", "-", "-"]))
                continue
            callee = n * per
            share = callee / ns[""]
            if real_answer.startswith("giveup"):
                # the row timed the give-up, not the operation: no share
                print("\t".join([t, m, subj.subject_id, str(n), "%.2f" % per, "%.0f" % callee,
                                 "%.0f" % ns[""], "-", "-", "-", "-", "-", real_answer[:40]]),
                      flush=True)
                continue
            flag = ("FLAG>40%" if share > 0.40 else
                    "over-budget>20%" if t == "pcre2-jit" and share > 0.20 else "")
            f = lambda v: "-" if v is None else "%.0f" % v   # noqa: E731
            # 3.2 item 5: real - pass only where the two arms fire equally
            rmp = ("%.2f" % ((ns[""] - ns["-pass"]) / n)
                   if pass_fires is not None and pass_fires == n and ns.get("-pass") else "-")
            print("\t".join([t, m, subj.subject_id, str(n), "%.2f" % per, "%.0f" % callee,
                             f(ns[""]), f(ns.get("-pass")), f(ns.get("-twin")),
                             "%.4f" % share, "-" if pass_fires is None else str(pass_fires),
                             rmp, flag]), flush=True)
    t1 = quiet.cpu_times()
    print("# load after: %s" % " ".join("%.2f" % x for x in quiet.loadavg()))
    print("# target cpu %d busy over the run: %.1f %% (%.0f s); /proc/stat"
          % (a.cpu, quiet._busy_pct(t0, t1, a.cpu), time.time() - w0))


if __name__ == "__main__":
    main()
