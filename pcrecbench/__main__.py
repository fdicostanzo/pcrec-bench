"""python3 -m pcrecbench -- the harness CLI (harness contract 4).

    run      measure one cell and write one record
    index    regenerate store/index.tsv
    quiet    sample the box and print the quiet-box verdict (OD-B8)
    testees  list the testees the adapters provide
    report   [B5]'s, not built here
"""

import argparse
import os
import sys

from . import HARNESS_VERSION


def cmd_run(args):
    from . import harness, quiet, store, adapters, env, subbench
    try:
        path, rid, setup, rows = harness.run_cell(
            args.subbench, args.testee,
            regimes=args.regimes, trials=args.trials, iters=args.iters,
            force_unquiet=args.force_unquiet, store_root=args.store,
            machine_id=args.machine_id, pin_cpu=args.pin,
            subject_timeout=args.subject_timeout,
            driver_timeout=args.driver_timeout,
            command_line=["python3", "-m", "pcrecbench"] + sys.argv[1:],
            note=args.note, synthetic=args.synthetic,
            progress=(lambda *a: print(*a, file=sys.stderr)) if not args.quiet_output else None)
    except quiet.QuietRefusal as e:
        print("pcrecbench run: %s" % e, file=sys.stderr)
        return 3
    except (harness.HarnessError, store.StoreError,
            adapters.AdapterError, env.MachineRegistryError,
            subbench.SubbenchError) as e:
        print("pcrecbench run: %s" % e, file=sys.stderr)
        return 1
    ncomp = sum(1 for r in rows if r["kind"] == "compile")
    nmatch = len(rows) - ncomp
    print("%s" % path)
    print("record_id  %s" % rid)
    print("status     %s" % setup["status"])
    print("rows       %d (%d compile, %d match)" % (len(rows), ncomp, nmatch))
    return 0


def cmd_index(args):
    from . import store
    n = store.index(args.store)
    print("index: %d record(s) -> %s"
          % (n, os.path.join(args.store, "index.tsv")))
    return 0


def cmd_quiet(args):
    from . import quiet
    worst = None
    for i in range(args.samples):
        load = quiet.loadavg()
        occ = quiet.occupancy(exclude_cpu=args.pin)
        print("load1 %.2f  occupancy %s  max_busy_pct %s"
              % (load[0], occ["verdict"], occ["max_busy_pct"]))
        if occ["max_busy_pct"] is not None:
            worst = max(worst or 0.0, occ["max_busy_pct"])
    print()
    print("thresholds in force: load1 <= %.2f, max_busy_pct <= %.2f"
          % (quiet.LOAD1_LIMIT, quiet.MAX_BUSY_PCT_LIMIT))
    print("derivation: docs/design/quiet_baseline.md")
    if worst is not None and worst > quiet.MAX_BUSY_PCT_LIMIT:
        print("VERDICT: NOT QUIET (worst sample %.2f%% busy)" % worst)
        return 3
    print("VERDICT: quiet")
    return 0


def cmd_testees(args):
    from . import adapters
    for tid, (engine, cfg) in sorted(adapters.all_testees().items()):
        print("%-16s %-8s %s" % (tid, engine, cfg.get("description", "")))
    return 0


def cmd_report(args):
    print("pcrecbench report: not built here.\n"
          "The reporter is milestone [B5] (harness contract 5): filter /\n"
          "group / reduce over the store, ratios to libpcre2-interp, N and\n"
          "pass-rate whenever coverage is below 100%. It builds against\n"
          "schema/examples/ plus its own fixtures and never runs an engine.\n"
          "`python3 -m pcrecbench index` regenerates the index it reads.",
          file=sys.stderr)
    return 2


def regimes_arg(s):
    from .subbench import REGIME_TO_ENUM
    out = [x.strip() for x in s.split(",") if x.strip()]
    bad = [x for x in out if x not in REGIME_TO_ENUM]
    if bad:
        raise argparse.ArgumentTypeError(
            "unknown regime(s) %s -- the sub-bench spellings are: %s"
            % (", ".join(bad), ", ".join(sorted(REGIME_TO_ENUM))))
    return out


def build_parser():
    from . import store
    p = argparse.ArgumentParser(
        prog="python3 -m pcrecbench",
        description="pcrec-bench: measure one cell, write one record "
                    "(docs/design/harness_contract.md).",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", action="version",
                   version="pcrecbench %s" % HARNESS_VERSION)
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser(
        "run", help="measure one cell and write one record",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
A CELL is one (sub-bench version x testee) pair. The run refuses on a box
that is not quiet (exit 3) unless --force-unquiet, in which case the record
is written with status `inconclusive-load` and the reporter will not rank it.

NOTE ON --testee: the id here is the adapter's CONFIG id (`pcre2-jit`). The
record and the store path use the DERIVED testee_id
(`libpcre2_10.46_jit-caps-simdna`, record_schema.md 6.4), which carries the
engine, the probed version and the configuration, and which validate.py
checks (rule X5). `python3 -m pcrecbench testees` lists the config ids.""")
    r.add_argument("--subbench", required=True,
                   help="the sub-bench DIRECTORY name under bench/ (e.g. email)")
    r.add_argument("--testee", required=True,
                   help="the adapter's config id (see `testees`)")
    r.add_argument("--trials", type=int, default=5,
                   help="raw trials per (pattern, subject, regime) and per "
                        "compile; the record keeps every one and the REPORTER "
                        "reduces them (default: 5)")
    r.add_argument("--regimes", type=regimes_arg, default=None,
                   help="comma-separated subset of the sub-bench's declared "
                        "regimes: match, search_short, throughput "
                        "(default: all it declares)")
    r.add_argument("--iters", type=int, default=None,
                   help="fix the in-process loop count instead of "
                        "auto-calibrating it to a ~50 ms loop. `--iters 1` is "
                        "what a SMOKE uses; it is not a measurement")
    r.add_argument("--force-unquiet", action="store_true",
                   help="measure on a box that failed the quiet gate. The "
                        "record's status becomes `inconclusive-load` and the "
                        "reasons go in `status_detail`")
    r.add_argument("--store", default=store.DEFAULT_STORE,
                   help="the store root (default: %(default)s). A SCRATCH "
                        "path is how a smoke avoids writing into the real "
                        "store")
    r.add_argument("--machine-id", default=None,
                   help="register THIS box under a stable slug. Required the "
                        "first time a box is measured; ids are hand-assigned "
                        "and never derived (record_schema.md 6.5)")
    r.add_argument("--pin", type=int, default=None, metavar="CPU",
                   help="pin the driver to one core with taskset, after the "
                        "occupancy check (requirements 9(d))")
    r.add_argument("--subject-timeout", type=int, default=60, metavar="SECS",
                   help="per-SUBJECT alarm inside the driver; the subject "
                        "that fires it is recorded `timed-out` by name "
                        "(0 = none, default: %(default)s)")
    r.add_argument("--driver-timeout", type=int, default=900, metavar="SECS",
                   help="gnutimeout on the driver PROCESS, the outer backstop "
                        "(default: %(default)s)")
    r.add_argument("--note", default=None,
                   help="a human sentence stored in the record's `note`")
    r.add_argument("--synthetic", action="store_true",
                   help="mark the record `synthetic` -- the reporter excludes "
                        "such records from every query. For fixtures and "
                        "smokes that must never be mistaken for measurements")
    r.add_argument("--quiet-output", action="store_true",
                   help="suppress the progress lines on stderr")
    r.set_defaults(func=cmd_run)

    i = sub.add_parser("index", help="regenerate store/index.tsv")
    i.add_argument("--store", default=store.DEFAULT_STORE)
    i.set_defaults(func=cmd_index)

    q = sub.add_parser("quiet", help="sample the box and print the verdict")
    q.add_argument("--samples", type=int, default=1)
    q.add_argument("--pin", type=int, default=None, metavar="CPU",
                   help="exclude this core from the occupancy check")
    q.set_defaults(func=cmd_quiet)

    t = sub.add_parser("testees", help="list the testees the adapters provide")
    t.set_defaults(func=cmd_testees)

    rep = sub.add_parser("report", help="[B5]'s; not built here")
    rep.set_defaults(func=cmd_report)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
