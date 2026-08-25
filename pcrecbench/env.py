"""env.py -- the `environment` block of a record, and the machine registry.

Everything here is PROBED from the running box (requirements 4.3: the
normalized identifiers are read, never typed), and canonicalised by the rules
docs/design/record_schema.md 6.5-6.7 fixes:

  * `machine_id` is HAND-ASSIGNED and looked up in `store/machines.tsv` -- 6.5
    is explicit that deriving it from /proc/cpuinfo or the hostname would
    silently split one box's history in two under a microcode update or a
    rename. The registry is keyed by (hostname, cpu_model, cores); a box that
    is not in it makes the harness REFUSE rather than invent an id.
  * `cpu_model`, `kernel`, `compiler` are canonicalised per 6.6/6.7, with the
    raw strings carried alongside as the evidence.

`LC_ALL=C` is forced on every subprocess this module runs (requirements 9(f)).
"""

import os
import platform
import re
import subprocess

C_ENV = dict(os.environ, LC_ALL="C", LANG="C")

MACHINE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,31}$")


# ------------------------------------------------------------------ probing

def _read(path, default=""):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return default


def cpu_model_raw():
    for line in _read("/proc/cpuinfo").splitlines():
        if line.startswith("model name"):
            return line.split(":", 1)[1].strip()
    return platform.processor() or "unknown"


def canon_cpu_model(raw):
    """record_schema.md 6.6: drop (R)/(TM)/(tm), drop a trailing `@ <freq>`,
    lowercase, collapse non-alphanumerics to a single `-`, strip edges."""
    s = raw
    for junk in ("(R)", "(TM)", "(tm)", "(r)"):
        s = s.replace(junk, "")
    s = re.sub(r"@.*$", "", s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "unknown"


def cores():
    try:
        return len(os.sched_getaffinity(0))
    except AttributeError:
        return os.cpu_count() or 1


def kernel_raw():
    return "%s %s" % (platform.system(), platform.release())


def canon_kernel(raw):
    """record_schema.md 6.7: `uname -s` and `uname -r`, lowercased, `-`."""
    parts = raw.split()
    return re.sub(r"[^a-z0-9._-]+", "-", "-".join(parts).lower())


def compiler_raw(cc=None):
    cc = cc or os.environ.get("CC", "gcc")
    try:
        out = subprocess.run([cc, "--version"], capture_output=True, text=True,
                             env=C_ENV, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return "unknown"
    return (out.stdout or out.stderr).splitlines()[0].strip() if (out.stdout or out.stderr) else "unknown"


def canon_compiler(raw):
    """record_schema.md 6.7: the first line of `$CC --version` reduced to
    `<name>-<version>`. `gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0` -> `gcc-15.2.0`."""
    if not raw or raw == "unknown":
        return "unknown"
    name = raw.split()[0].lower()
    name = re.sub(r"[^a-z0-9+]+", "-", name).strip("-")
    # the LAST bare dotted-number token on the line is the version gcc/clang
    # both print; a parenthesised distro string is deliberately not it.
    tail = re.sub(r"\([^)]*\)", " ", raw)
    vers = re.findall(r"\b\d+(?:\.\d+)+\b", tail)
    return "%s-%s" % (name, vers[-1]) if vers else name


def cpu_mhz():
    """`/proc/cpuinfo`'s `cpu MHz` for cpu0, as a float. Schema v1.1 item
    (10), optional. It is a SPOT reading of a scaling frequency, not a
    property of the box -- it says what the core was clocked at when the
    record was built, which is why it is diagnostic rather than filterable."""
    for line in _read("/proc/cpuinfo").splitlines():
        if line.lower().startswith("cpu mhz"):
            try:
                return round(float(line.split(":", 1)[1].strip()), 3)
            except ValueError:
                return None
    return None


def governor():
    g = _read("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor").strip()
    return g or None


def turbo():
    """`intel_pstate/no_turbo` (1 = disabled) or amd/acpi's `boost` (1 = on)."""
    no_turbo = _read("/sys/devices/system/cpu/intel_pstate/no_turbo").strip()
    if no_turbo:
        return "disabled" if no_turbo == "1" else "enabled"
    boost = _read("/sys/devices/system/cpu/cpufreq/boost").strip()
    if boost:
        return "enabled" if boost == "1" else "disabled"
    return None


# ------------------------------------------------------- the machine registry

class MachineRegistryError(Exception):
    pass


REGISTRY_HEADER = "machine_id\thostname\tcpu_model\tcores\tfirst_seen\tnote\n"


def registry_path(store_root):
    return os.path.join(store_root, "machines.tsv")


def load_registry(store_root):
    path = registry_path(store_root)
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.rstrip("\n")
            if not line or (i == 0 and line.startswith("machine_id\t")):
                continue
            parts = line.split("\t")
            while len(parts) < 6:
                parts.append("")
            rows.append(dict(zip(
                ("machine_id", "hostname", "cpu_model", "cores", "first_seen", "note"),
                parts[:6])))
    return rows


def resolve_machine_id(store_root, hostname, cpu_model, ncores,
                       assign=None, timestamp=None):
    """Look this box up in the registry; return its `machine_id`.

    `assign` registers a NEW id for this box (the `--machine-id` flag). An
    unknown box with no `assign` is an ERROR: record_schema.md 6.5 makes the id
    a deliberate human act, and a harness that guessed one would attribute this
    run to a machine nobody named."""
    rows = load_registry(store_root)
    key = (hostname, cpu_model, str(ncores))
    for r in rows:
        if (r["hostname"], r["cpu_model"], r["cores"]) == key:
            if assign and assign != r["machine_id"]:
                raise MachineRegistryError(
                    "this box is already registered as %r (%s); refusing to "
                    "re-assign it to %r -- record_schema.md 6.5: an id is "
                    "never reused for a different box, and a box never gets a "
                    "second id, or its history splits in two"
                    % (r["machine_id"], registry_path(store_root), assign))
            return r["machine_id"]

    if not assign:
        raise MachineRegistryError(
            "this box (hostname=%s cpu_model=%s cores=%s) is not in %s. "
            "Assign it a stable slug with --machine-id SLUG; it is written to "
            "the registry and never derived (record_schema.md 6.5)."
            % (hostname, cpu_model, ncores, registry_path(store_root)))
    if not MACHINE_ID_RE.match(assign):
        raise MachineRegistryError(
            "--machine-id %r does not match %s (record_schema.md 6.5)"
            % (assign, MACHINE_ID_RE.pattern))
    for r in rows:
        if r["machine_id"] == assign:
            raise MachineRegistryError(
                "machine_id %r is already registered for a DIFFERENT box "
                "(hostname=%s cpu_model=%s cores=%s). Ids are never reused."
                % (assign, r["hostname"], r["cpu_model"], r["cores"]))

    os.makedirs(store_root, exist_ok=True)
    path = registry_path(store_root)
    new = not os.path.exists(path)
    with open(path, "a", encoding="utf-8") as f:
        if new:
            f.write(REGISTRY_HEADER)
        f.write("%s\t%s\t%s\t%s\t%s\t%s\n"
                % (assign, hostname, cpu_model, ncores, timestamp or "", ""))
    return assign


# --------------------------------------------------------------- the block

def describe(store_root, machine_id=None, timestamp=None, cc=None):
    """The record's `environment` block minus the run-time samples (`load`,
    `occupancy`, `pinning`, `quiet_attestation`), which quiet.py supplies."""
    craw = cpu_model_raw()
    kraw = kernel_raw()
    cmpraw = compiler_raw(cc)
    host = platform.node() or "unknown"
    cpu = canon_cpu_model(craw)
    n = cores()
    return {
        "machine_id": resolve_machine_id(store_root, host, cpu, n,
                                         assign=machine_id, timestamp=timestamp),
        "hostname": host,
        "cpu_model": cpu,
        "cpu_model_raw": craw,
        "cores": n,
        "kernel": canon_kernel(kraw),
        "kernel_raw": kraw,
        "compiler": canon_compiler(cmpraw),
        "compiler_raw": cmpraw,
        "governor": governor(),
        "turbo": turbo(),
        # v1.1 (10). Built always, emitted only when the schema has a home
        # for it -- record.project() decides.
        "cpu_mhz": cpu_mhz(),
    }
