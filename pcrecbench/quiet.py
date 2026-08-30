"""quiet.py -- the quiet-box instrument (requirements 9(a)-(d), OD-B8).

Three separable facts, each recorded whether or not it passes, because
requirements 9(b) is explicit that an unavailable tool is RECORDED, never
silently skipped:

  (a) LOAD -- `/proc/loadavg` sampled BEFORE and AFTER the run, both kept.
      `verdict` is `loaded` if EITHER sample exceeds the limit (X20, an
      either-sample FACT). Since schema v1.4 ([B20], gate_shape_v14.md 2)
      only the BEFORE sample decides the STATUS: the pre-flight's load clause.
  (b) OCCUPANCY -- per-core %idle from `mpstat -P ALL 1 5` judged on its
      `Average:` block (BD7), reduced to the busiest NON-TARGET core
      (`max_busy_pct` = 100 - min %idle over the cores we are not pinned to)
      -- the target's SMT sibling judged like any other core -- PLUS, since
      v1.4, the TARGET core's own reading (`target_busy_pct`, tri-state:
      absent when nothing is pinned, null when its row is missing, a number
      otherwise): nothing of ours runs there before the run, so a busy target
      is a competitor that will sit UNDER every trial uniformly, which trial
      agreement cannot see. Sampled at BOTH ENDS with one instrument; the
      BEFORE sample is the PRE-FLIGHT (the gate: `gate()`), the AFTER sample
      is PROVENANCE (`after_notes()`: a sentence, never a verdict on the
      status -- Frank's ruling I-19, BD7 ratified as the gate).
  (c) THE PER-GROUP TIMELINE (v1.4, gate_shape_v14.md 3.6) -- `/proc/stat`
      read at every group boundary of the run, the busy % of the target core,
      its sibling and the busiest other core over each group's passes.
      Provenance only: no rule reads it. `cpu_times()` / `timeline_item()`.
  (d) PINNING -- `taskset`; `none` when the harness was told not to pin,
      `unavailable` when taskset is missing or refuses. Computed BEFORE the
      occupancy check and passed to it as `exclude_cpu` (one source for "the
      target core", ruling R-2).

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
#
# OCCUPANCY_SECONDS -- 5 (BD7, 2026-08-30; OD-B12 closed). The occupancy
# instrument was ONE 1-second mpstat sample at each end of a run. Five of
# the five `inconclusive-load` records stamped in the two pinned windows of
# 2026-08-29/30 failed on the AFTER sample alone -- 10.1 / 11.1 / 13.0 /
# 20.2 % on ONE non-target core, load1 quiet, nothing sustained on the box:
# a VS Code server waking on the record write, a streaming manager's ~9 %,
# a half-second `gh` refresh at ~40 %. A 1-s sample cannot tell a burst
# from a competitor; a 5-s AVERAGE can: the half-second burst becomes 4 %,
# a competing process stays at 100 %, a streaming session stays at 9 %.
# mpstat's own `Average:` block is the number; the per-second peaks are
# kept in `raw` beside it so the burst is still visible. Same instrument
# at both ends (check() below); `environment.occupancy.tool` names the
# command, so a record says which instrument judged it.
LOAD1_LIMIT = 2.0
MAX_BUSY_PCT_LIMIT = 10.0
OCCUPANCY_SECONDS = 5

MPSTAT_CMD = ["mpstat", "-P", "ALL", "1", str(OCCUPANCY_SECONDS)]


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


def split_mpstat(text):
    """-> (per_second_texts, average_text). mpstat prints one header+block
    per interval and, for more than one interval, a final block whose rows
    start with `Average:`. Each returned text carries its own header row so
    `parse_mpstat` can locate %idle in it."""
    seconds, average, current = [], [], []
    for line in text.splitlines():
        if line.startswith("Average:"):
            average.append(line)
            continue
        if "%idle" in line:
            if current:
                seconds.append("\n".join(current))
            current = [line]
        elif current and line.strip():
            current.append(line)
    if current:
        seconds.append("\n".join(current))
    return seconds, "\n".join(average)


def smt_siblings(cpu):
    """The SMT siblings of `cpu` (itself excluded), from sysfs; [] when
    unknown. On this box CPU 11's sibling is CPU 5: a competitor there
    shares the measured core's execution resources, which is why the
    sibling is NEVER excluded from the occupancy judgement -- it is a
    non-target core whose business matters most."""
    if cpu is None:
        return []
    try:
        with open("/sys/devices/system/cpu/cpu%d/topology/thread_siblings_list"
                  % int(cpu)) as fh:
            spec = fh.read().strip()
    except (OSError, ValueError):
        return []
    out = set()
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-", 1)
            out.update(range(int(a), int(b) + 1))
        elif part.strip():
            out.add(int(part))
    out.discard(int(cpu))
    return sorted(out)


def judge_mpstat(text, exclude_cpu=None, limit=MAX_BUSY_PCT_LIMIT,
                 siblings=None):
    """The occupancy VERDICT from an mpstat capture -- pure, so a selfcheck
    can hand it a synthetic capture and show what the rule does to a burst.

    Over `OCCUPANCY_SECONDS` intervals the judged number is the per-core
    AVERAGE (mpstat's own `Average:` block); with a single interval there is
    no such block and the one sample is the average. `raw` keeps the
    Average block verbatim plus the per-second peak of the busiest non-target
    core, so a reader sees both the number that was judged and the transient
    it absorbed."""
    block = {"verdict": "unavailable", "max_busy_pct": None, "raw": ""}
    pinned = exclude_cpu is not None
    if pinned:
        # v1.4 tri-state: the key EXISTS iff a core is pinned; None until the
        # target's own row is found in the judged block (a missing row is
        # the pre-flight refusal gate() makes, never silently a pass).
        block["target_busy_pct"] = None
    seconds, average = split_mpstat(text)
    judged_text = average if average else (seconds[-1] if seconds else text)
    per_cpu, _all_idle = parse_mpstat(judged_text)
    considered = {c: i for c, i in per_cpu.items() if c != exclude_cpu}
    if pinned and exclude_cpu in per_cpu:
        block["target_busy_pct"] = round(100.0 - per_cpu[exclude_cpu], 2)
    peaks = []
    for sec in seconds:
        pc, _ = parse_mpstat(sec)
        cons = {c: i for c, i in pc.items() if c != exclude_cpu}
        if cons:
            peaks.append(round(100.0 - min(cons.values()), 2))
    raw = judged_text.strip()
    if average and peaks:
        raw += ("\nper-second peak busy%% of the busiest non-target core: %s"
                % " ".join("%.2f" % v for v in peaks))
    if pinned:
        sib = siblings if siblings is not None else smt_siblings(exclude_cpu)
        sib_busy = ["cpu%d %.2f%%" % (c, 100.0 - per_cpu[c])
                    for c in sib if c in per_cpu]
        tgt = block["target_busy_pct"]
        raw += ("\ntarget cpu%d excluded from the non-target judgement (its "
                "own reading %s is judged by the target clause, v1.4); its SMT "
                "sibling(s) %s judged like any other core"
                % (exclude_cpu,
                   ("%.2f%%" % tgt) if tgt is not None else "MISSING from the capture",
                   (", ".join(sib_busy) or "unknown")))
    block["raw"] = raw
    if not considered:
        block["raw"] = (text.strip() + "\n(no per-cpu rows could be parsed "
                        "from the above)").strip()
        return block
    max_busy = round(100.0 - min(considered.values()), 2)
    block["max_busy_pct"] = max_busy
    block["verdict"] = "pass" if max_busy <= limit else "fail"
    return block


def occupancy(exclude_cpu=None, limit=MAX_BUSY_PCT_LIMIT, timeout=60):
    """record_schema.md `environment.occupancy`. `unavailable` when mpstat is
    absent or unparseable -- requirements 9(b): recorded, never skipped.
    Takes OCCUPANCY_SECONDS wall seconds; the verdict is `judge_mpstat`'s."""
    # `$defs/occupancy_sample`: verdict + max_busy_pct + raw, and nothing
    # else. `max_busy_pct` is null EXACTLY when the verdict is `unavailable`
    # (the schema enforces the iff), so `raw` then has to carry the reason
    # mpstat produced nothing -- requirements 9(b): recorded, never skipped.
    block = {
        "verdict": "unavailable",
        "max_busy_pct": None,
        "raw": "",
    }
    if exclude_cpu is not None:
        block["target_busy_pct"] = None     # v1.4: null beside `unavailable`
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
    return judge_mpstat(full, exclude_cpu=exclude_cpu, limit=limit)


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
    `limit_busy_pct`; `gate()` judges the BEFORE sample (the pre-flight) and
    `after_notes()` turns a failed AFTER sample into a provenance sentence --
    reductions the record does not store as a verdict, because a stored one
    could disagree with the numbers under it."""
    return {
        "tool": " ".join(MPSTAT_CMD),
        "limit_busy_pct": limit,
        "before": before,
        "after": after,
    }


def preflight_ok(block, load_limit=LOAD1_LIMIT):
    """-> (ok, reasons) for the PRE-FLIGHT half of an `environment.occupancy`
    block (v1.4: the `before` sample only -- its verdict and the target
    clauses), exactly as `gate()` would say them. The after sample is not
    read here; see `after_notes()`."""
    sample = block.get("before") or {}
    reasons = _occupancy_reasons(sample, block.get("limit_busy_pct", MAX_BUSY_PCT_LIMIT))
    return (not reasons), reasons


def after_notes(occ_block, load_block):
    """The v1.4 PROVENANCE sentences (gate_shape_v14.md 2), 0, 1 or 2 -- one
    per instrument whose AFTER sample failed. A NOTE, never a status: the
    after samples are recorded with their X19/X26 verdicts and never
    disqualify a v1.4 record; the sentence carries the number and says who
    decided the status instead."""
    out = []
    occ_after = (occ_block or {}).get("after") or {}
    limit = (occ_block or {}).get("limit_busy_pct", MAX_BUSY_PCT_LIMIT)
    if occ_after.get("verdict") == "fail":
        out.append("after-sample (provenance, not a verdict): occupancy after "
                   "the run %.2f%% busy on the busiest non-target core (limit "
                   "%.2f%%); the trials' agreement decided the status (v1.4 X13)"
                   % (occ_after.get("max_busy_pct") or 0.0, limit))
    load_after = (load_block or {}).get("after") or {}
    l_limit = (load_block or {}).get("limit", LOAD1_LIMIT)
    l1 = load_after.get("load1")
    if isinstance(l1, (int, float)) and l1 > l_limit:
        out.append("after-sample (provenance, not a verdict): load1 after the "
                   "run %.2f exceeds the limit %.2f; the trials' agreement "
                   "decided the status (v1.4 X13)" % (l1, l_limit))
    return out


def _occupancy_reasons(occ_sample, limit=MAX_BUSY_PCT_LIMIT):
    """The occupancy clauses of the pre-flight, on ONE sample: (b) the
    busiest non-target core, (c) the target core's own reading, (c') the
    target's row present at all, (d) the sample available. `target_busy_pct`
    being a KEY of the sample is the one source for "a core is pinned"
    (judge_mpstat / occupancy() write it iff `exclude_cpu` was an integer,
    which the harness takes from `pinning.cpu` -- ruling R-2)."""
    reasons = []
    verdict = occ_sample.get("verdict")
    if verdict == "fail":
        reasons.append("occupancy: busiest non-target core %.2f%% busy "
                       "(limit %.2f%%)" % (occ_sample["max_busy_pct"], limit))
    if verdict == "unavailable":
        reasons.append("occupancy: %s is unavailable -- recorded, not skipped "
                       "(requirements 9(b))" % " ".join(MPSTAT_CMD))
    if "target_busy_pct" in occ_sample:
        cpu = _target_cpu_from_raw(occ_sample)
        tb = occ_sample["target_busy_pct"]
        if isinstance(tb, (int, float)) and tb > limit:
            reasons.append("occupancy: the TARGET core cpu%s reads %.2f%% busy "
                           "before the run (limit %.2f%%) -- a competitor is "
                           "pinned where this cell will be" % (cpu, tb, limit))
        elif tb is None and verdict != "unavailable":
            reasons.append("occupancy: the target core cpu%s does not appear in "
                           "the mpstat capture; the clause that judges it "
                           "cannot run" % cpu)
    return reasons


def _target_cpu_from_raw(occ_sample):
    """The pinned core's number, for a message: read back out of the
    sample's own `raw` line (`target cpuN ...`), which judge_mpstat wrote
    from the same `exclude_cpu`; `?` when it is not there."""
    m = re.search(r"target cpu(\d+)", occ_sample.get("raw") or "")
    return m.group(1) if m else "?"


def gate(load_before, occ_sample, force=False, load_limit=LOAD1_LIMIT,
         occupancy_limit=MAX_BUSY_PCT_LIMIT):
    """Contract 4 step (2): refuse unless quiet, or `--force-unquiet`.

    THE PRE-FLIGHT (gate_shape_v14.md 1): (a) load1 before the run under the
    limit; (b) every non-target core's 5-s average under the limit; (c) the
    TARGET core's own average under the limit, iff a core is pinned; (c') the
    target's row present in the capture, iff a core is pinned; (d) the sample
    not `unavailable`. Returns a REASONS list -- empty when the box is quiet
    (so `--force-unquiet` on a quiet box changes nothing: the flag is not a
    status). A non-empty list with `force` set is what makes the record
    `inconclusive-load` (record_schema.md X13); without `force` the caller
    raises (exit 3). The `quiet` CLI reduces its samples through THIS
    function too (ruling R-7): one instrument, one decision, both ends."""
    reasons = []
    load1 = load_before["load1"] if isinstance(load_before, dict) else load_before[0]
    if load1 > load_limit:
        reasons.append("load1 %.2f exceeds the limit %.2f"
                       % (load1, load_limit))
    reasons.extend(_occupancy_reasons(occ_sample, occupancy_limit))
    if reasons and not force:
        raise QuietRefusal(
            "the box is not quiet:\n  - " + "\n  - ".join(reasons)
            + "\n\nWait for it to go quiet, or pass --force-unquiet to measure "
              "anyway (the record is then written with status "
              "`inconclusive-load` and the reporter will not rank it).")
    return reasons


# ------------------------------------ the per-group timeline (v1.4, provenance)

PROC_STAT_PATH = "/proc/stat"
TIMELINE_TOOL = "/proc/stat"


def cpu_times(path=None):
    """-> {cpu: (busy_jiffies, total_jiffies)} from one read of /proc/stat,
    or None when it cannot be read or parsed (the harness then writes no
    timeline at all -- an absent field, never a zero). `busy` is every
    column but idle and iowait (the reading `mpstat`'s %idle complements)."""
    try:
        with open(path or PROC_STAT_PATH, "r", encoding="ascii") as fh:
            lines = fh.read().splitlines()
    except (OSError, ValueError):
        return None
    out = {}
    for line in lines:
        cols = line.split()
        if len(cols) < 5 or not cols[0].startswith("cpu") or cols[0] == "cpu":
            continue
        try:
            n = int(cols[0][3:])
            vals = [int(x) for x in cols[1:]]
        except ValueError:
            continue
        total = sum(vals)
        idle = vals[3] + (vals[4] if len(vals) > 4 else 0)
        out[n] = (total - idle, total)
    return out or None


def _busy_pct(before, after, cpu):
    b0, t0 = before.get(cpu, (0, 0))
    b1, t1 = after.get(cpu, (0, 0))
    dt = t1 - t0
    if dt <= 0:
        return 0.0
    return round(max(0.0, min(100.0, 100.0 * (b1 - b0) / dt)), 2)


def timeline_item(before, after, elapsed_ms, target_cpu, pattern_id, regime,
                  form, siblings=None):
    """One `environment.occupancy.timeline[]` item (gate_shape_v14.md 3.6)
    from two `cpu_times()` readings around one group's passes."""
    sib = siblings if siblings is not None else smt_siblings(target_cpu)
    others = [c for c in after if c != target_cpu and c not in sib and c in before]
    if others:
        worst = max(others, key=lambda c: (_busy_pct(before, after, c), -c))
        max_other, max_other_cpu = _busy_pct(before, after, worst), worst
    else:
        max_other, max_other_cpu = 0.0, 0
    sib_present = [c for c in sib if c in before and c in after]
    return {
        "pattern_id": pattern_id, "regime": regime, "form": form or "plain",
        "elapsed_ms": int(max(elapsed_ms, 0)),
        "target_busy_pct": _busy_pct(before, after, target_cpu),
        "sibling_busy_pct": (max(_busy_pct(before, after, c) for c in sib_present)
                             if sib_present else None),
        "max_other_busy_pct": max_other,
        "max_other_cpu": int(max_other_cpu),
    }
