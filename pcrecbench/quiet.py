"""quiet.py -- the quiet-box instrument (requirements 9(a)-(d), OD-B8).

Three separable facts, each recorded whether or not it passes, because
requirements 9(b) is explicit that an unavailable tool is RECORDED, never
silently skipped:

  (a) LOAD -- `/proc/loadavg` sampled BEFORE and AFTER the run, both kept, and
      the AFTER sample re-checked against the same limit. pcrec's compare R3.10
      lesson (requirements 9(a)): a box that was quiet at the start and got
      busy partway through is just as load-compromised, so `verdict` is
      `loaded` if EITHER sample exceeds the limit.
  (b) OCCUPANCY -- per-core %idle from `mpstat -P ALL 1 1`, reduced to the
      busiest NON-TARGET core (`max_busy_pct` = 100 - min %idle over the cores
      we are not pinned to), sampled at BOTH ENDS for exactly the reason load
      is. Verdict `pass` / `fail` / `unavailable`, and the combined verdict is
      the WORSE of the two samples: a box that stayed under the load limit
      while another job occupied a core is the case this instrument was
      measured to catch (docs/design/quiet_baseline.md), and it can start
      after the run does.
  (d) PINNING -- `taskset` after the occupancy check; `none` when the harness
      was told not to pin, `unavailable` when taskset is missing or refuses.

THE THRESHOLDS ARE MEASURED, NOT ASSUMED (OD-B8, requirements 9(c)). What was
measured on this box on 2026-08-25, and the derivation, is in
docs/design/quiet_baseline.md; the defaults below are that note's conclusion.
They are DEFAULTS, not constants: `environment.load.limit` is a per-run field
of the record precisely so a threshold change is re-judgeable later
(record_schema.md 10.2).
"""

import os
import re
import shutil
import subprocess
import time

from .env import C_ENV

# --------------------------------------------------------------- thresholds
#
# docs/design/quiet_baseline.md. In one line each:
#
# LOAD1_LIMIT -- the harness runs ONE driver process at a time, so its own
# contribution to load1 is ~1.0 while it runs; 2.0 leaves exactly one core of
# headroom above our own work and no more. pcrec's compare.sh uses
# `max(2.0, cores/2)` (= 6.0 here), which is right for a suite that may run
# several jobs and wrong for a single pinned measurement: it would admit five
# competing threads.
#
# MAX_BUSY_PCT_LIMIT -- 10.0, i.e. "every non-target core at >= 90% idle".
# MEASURED: on this box the QUIETEST core in every one of 12 samples sat at
# 93-98% idle, so the instrument's own noise floor is ~2-7% busy per core; a
# 10% bar clears that floor with headroom while still refusing every sample
# taken while another session's test battery was running.
LOAD1_LIMIT = 2.0
MAX_BUSY_PCT_LIMIT = 10.0

MPSTAT_CMD = ["mpstat", "-P", "ALL", "1", "1"]


class QuietRefusal(Exception):
    """Raised by `gate()` when the box is not quiet and --force-unquiet was
    not given. The CLI turns it into exit status 3 (contract 4)."""


# ------------------------------------------------------------------- load

def loadavg():
    """The three figures, for a caller that just wants numbers."""
    s = load_sample()
    return [s["load1"], s["load5"], s["load15"]]


def load_sample():
    """`$defs/load_sample`: a load sample WITH its evidence -- the
    `/proc/loadavg` line verbatim, when it was taken, and the three parsed
    numbers. Rule X19 re-parses the raw line and requires it to agree, so the
    numbers here are derived from the string that is stored beside them and
    cannot drift from it."""
    with open("/proc/loadavg", "r", encoding="ascii") as f:
        raw = f.read().strip()
    parts = raw.split()
    return {
        "loadavg_raw": raw,
        "sampled_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "load1": float(parts[0]),
        "load5": float(parts[1]),
        "load15": float(parts[2]),
    }


def load_block(before, after, limit=LOAD1_LIMIT):
    """`environment.load`. `verdict` is `loaded` iff EITHER sample's 1-minute
    figure exceeds `limit` (requirements 9(a), C7) -- rule X20 recomputes it
    from the two samples and the limit, so the verdict cannot be an opinion."""
    loaded = before["load1"] > limit or after["load1"] > limit
    return {
        "before": before,
        "after": after,
        "limit": limit,
        "verdict": "loaded" if loaded else "quiet",
    }


# -------------------------------------------------------------- occupancy

_CPU_ROW = re.compile(r"^\s*(?:\S+\s+)?(all|\d+)\s+(.*)$")


def parse_mpstat(text):
    """-> (per_cpu, all_idle). `per_cpu` maps a cpu NUMBER to its %idle.

    mpstat's column layout moves between versions and locales (hence LC_ALL=C),
    so this locates %idle by its HEADER position rather than assuming it is
    last: a hard-coded column index is how a parser silently reports the wrong
    number. The header row is the one containing `%idle`."""
    idle_col = None
    cpu_col = None
    per_cpu = {}
    all_idle = None
    for line in text.splitlines():
        if "%idle" in line:
            cols = line.split()
            try:
                idle_col = cols.index("%idle")
            except ValueError:
                continue
            cpu_col = cols.index("CPU") if "CPU" in cols else None
            continue
        if idle_col is None or cpu_col is None:
            continue
        cols = line.split()
        # the data rows carry the same trailing columns as the header, offset
        # by however many leading time fields this locale/version prints.
        if len(cols) < idle_col + 1:
            continue
        offset = len(cols) - (idle_col + 1)
        if offset < 0 or cpu_col + offset >= len(cols):
            continue
        who = cols[cpu_col + offset]
        try:
            idle = float(cols[idle_col + offset])
        except ValueError:
            continue
        if who == "all":
            all_idle = idle
        elif who.isdigit():
            per_cpu[int(who)] = idle
    return per_cpu, all_idle


def occupancy(exclude_cpu=None, limit=MAX_BUSY_PCT_LIMIT, timeout=30):
    """record_schema.md `environment.occupancy`. `unavailable` when mpstat is
    absent or unparseable -- requirements 9(b): recorded, never skipped."""
    # `$defs/occupancy_sample`: verdict + max_busy_pct + raw, and nothing
    # else. `max_busy_pct` is null EXACTLY when the verdict is `unavailable`
    # (the schema enforces the iff), so `raw` then has to carry the reason
    # mpstat produced nothing -- requirements 9(b): recorded, never skipped.
    block = {
        "verdict": "unavailable",
        "max_busy_pct": None,
        "raw": "",
    }
    if shutil.which("mpstat") is None:
        block["raw"] = ("mpstat not installed on this box, so per-core "
                        "occupancy could not be measured (%s)"
                        % " ".join(MPSTAT_CMD))
        return block
    try:
        out = subprocess.run(MPSTAT_CMD, capture_output=True, text=True,
                             env=C_ENV, timeout=timeout)
    except (OSError, subprocess.SubprocessError) as e:
        block["raw"] = "mpstat failed: %s" % (e,)
        return block
    full = (out.stdout or "") + (out.stderr or "")
    per_cpu, _all_idle = parse_mpstat(full)
    # `mpstat -P ALL 1 1` prints the sample block and then an `Average:` block
    # that repeats it verbatim; keep only the first for the record.
    block["raw"] = full.split("\nAverage:", 1)[0].strip()
    considered = {c: i for c, i in per_cpu.items() if c != exclude_cpu}
    if not considered:
        block["raw"] = (block["raw"] + "\n(no per-cpu rows could be parsed "
                        "from the above)").strip()
        return block
    max_busy = round(100.0 - min(considered.values()), 2)
    block["max_busy_pct"] = max_busy
    block["verdict"] = "pass" if max_busy <= limit else "fail"
    return block


# ---------------------------------------------------------------- pinning

def pinning(cpu=None):
    """record_schema.md `environment.pinning`. `none` when no core was asked
    for; `unavailable` when taskset is missing -- pcrec's compare.sh degrades
    quietly when unprivileged and the record must say which (6.5 note)."""
    if cpu is None:
        return {"mode": "none", "cpu": None}
    if shutil.which("taskset") is None:
        return {"mode": "unavailable", "cpu": None}
    try:
        os.sched_getaffinity(0)
    except (AttributeError, OSError):
        return {"mode": "unavailable", "cpu": None}
    return {"mode": "taskset", "cpu": int(cpu)}


def taskset_prefix(pin):
    """The argv prefix that pins a child to `pin['cpu']`, or []."""
    if pin.get("mode") == "taskset" and pin.get("cpu") is not None:
        return ["taskset", "-c", str(pin["cpu"])]
    return []


# ------------------------------------------------------------------ the gate

def check(exclude_cpu=None, load_limit=LOAD1_LIMIT,
          occupancy_limit=MAX_BUSY_PCT_LIMIT):
    """Sample the box. Returns (load_sample, occupancy_block).

    The SAME call is made before and after a run -- there is no `check_after`,
    because two samples taken by two code paths are two instruments, and the
    whole point of the after-sample is that it is comparable to the before
    one."""
    return load_sample(), occupancy(exclude_cpu=exclude_cpu,
                                    limit=occupancy_limit)


def occupancy_block(before, after, limit=MAX_BUSY_PCT_LIMIT):
    """`environment.occupancy`: the two samples, the tool, and the THRESHOLD
    they were judged against.

    There is deliberately no combined verdict here. Each sample carries its
    own, rule X26 recomputes each from its own number against
    `limit_busy_pct`, and `occupancy_ok()` below is the only place the two are
    reduced to one answer -- a reduction the record does not store, because a
    stored one could disagree with the numbers under it."""
    return {
        "tool": " ".join(MPSTAT_CMD),
        "limit_busy_pct": limit,
        "before": before,
        "after": after,
    }


def occupancy_ok(block):
    """-> (ok, reasons). `pass` is required at BOTH ends (requirements 9(b),
    ruled 2026-08-25): `unavailable` or `fail` on either sample is not a
    measured record. A box that was clean at the start and shared partway
    through was still shared while it was measured."""
    reasons = []
    for when in ("before", "after"):
        sample = block.get(when) or {}
        v = sample.get("verdict")
        if v == "fail":
            reasons.append("occupancy %s: busiest non-target core %.2f%% busy "
                           "(limit %.2f%%)"
                           % (when, sample.get("max_busy_pct") or 0.0,
                              block.get("limit_busy_pct", MAX_BUSY_PCT_LIMIT)))
        elif v != "pass":
            reasons.append("occupancy %s: %s is unavailable -- recorded, "
                           "never skipped (requirements 9(b))"
                           % (when, block.get("tool", "mpstat")))
    return (not reasons), reasons


def gate(load_before, occ_sample, force=False, load_limit=LOAD1_LIMIT):
    """Contract 4 step (2): refuse unless quiet, or `--force-unquiet`.

    Returns a REASONS list -- empty when the box is quiet. A non-empty list
    with `force` set is what makes the record `inconclusive-load`
    (record_schema.md X13); without `force` the caller raises."""
    reasons = []
    load1 = load_before["load1"] if isinstance(load_before, dict) else load_before[0]
    if load1 > load_limit:
        reasons.append("load1 %.2f exceeds the limit %.2f"
                       % (load1, load_limit))
    if occ_sample["verdict"] == "fail":
        reasons.append("occupancy: busiest non-target core %.2f%% busy "
                       "(limit %.2f%%)"
                       % (occ_sample["max_busy_pct"], MAX_BUSY_PCT_LIMIT))
    if occ_sample["verdict"] == "unavailable":
        reasons.append("occupancy: %s is unavailable -- recorded, not skipped "
                       "(requirements 9(b))" % " ".join(MPSTAT_CMD))
    if reasons and not force:
        raise QuietRefusal(
            "the box is not quiet:\n  - " + "\n  - ".join(reasons)
            + "\n\nWait for it to go quiet, or pass --force-unquiet to measure "
              "anyway (the record is then written with status "
              "`inconclusive-load` and the reporter will not rank it).")
    return reasons
