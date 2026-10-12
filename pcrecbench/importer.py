"""importer.py -- `pcrecbench import`: land a FOREIGN store's records in the
ONE canonical store ([B137], outbox O-90, pcrec I-138/I-139/O-98 Q7).

The multi-host design (O-90): every host installs and measures with its own
checkout of this repo at a named commit and its own local store; the records
come home and are IMPORTED into `store/`, durable and comparable. Nothing is
trusted because it arrived: the import is TWO PASSES, and pass 1 writes
nothing.

  pass 1 (check everything, collect every refusal, write nothing):
    * the record validates (schema/validate.py, --check-filename);
    * it is not `tier: scratch` (store.check_tier_allowed's rule, named);
    * its machine_id is KNOWN to `store/machines.tsv` (or is being registered
      by this same call, `register_machine`) and its hostname / cpu_model /
      cores agree with that registry row -- an id names one box (6.5);
    * its sub-bench id + version + `content_hash` equal THIS repo's committed
      set (subbench.Subbench.content_hash over bench/<set>) -- a record
      measured against a different checkout of a set is not comparable;
    * its target path is free, or holds the IDENTICAL bytes (a no-op); a
      same-named record whose bytes differ is a refusal -- the store never
      clobbers (store.py), and an import must not smuggle in a second claim
      on a record_id.
  pass 2 (only when pass 1 found no refusal): copy each new record atomically
  into `records/<set>@<ver>/<testee_id>/<record_id>.jsonl`, register the
  machine if asked, and re-index.

The target is the CANONICAL store only (the `.canonical` marker); a scratch
store is not an import target.
"""

import os
import shutil
import tempfile

from . import env, store, subbench


class ImportRefused(Exception):
    """Pass 1 found at least one refusal; `refusals` is [(path, reason)].
    Nothing was written."""

    def __init__(self, refusals):
        self.refusals = refusals
        super().__init__("\n".join("REFUSED %s: %s" % r for r in refusals))


def _read_setup(path):
    import json
    with open(path, "r", encoding="utf-8") as f:
        return json.loads(f.readline())


def _committed_sets(bench_root):
    """-> {set_id: (version, content_hash)} over every bench/*/subbench.toml."""
    out = {}
    if not os.path.isdir(bench_root):
        return out
    for d in sorted(os.listdir(bench_root)):
        if os.path.exists(os.path.join(bench_root, d, "subbench.toml")):
            sb = subbench.Subbench(os.path.join(bench_root, d))
            out[sb.id] = (sb.version, sb.content_hash())
    return out


def _foreign_registry_row(foreign_root, machine_id):
    for r in env.load_registry(foreign_root):
        if r["machine_id"] == machine_id:
            return r
    return None


def import_store(foreign_root, store_root=None, register_machine=None,
                 bench_root=None):
    """Import `foreign_root`'s records into the canonical `store_root`.
    -> (imported, already_present) lists of target paths. Raises
    `ImportRefused` (nothing written) or `store.StoreError`."""
    store_root = store_root or store.DEFAULT_STORE
    if not store.is_canonical(store_root):
        raise store.StoreError(
            "REFUSED: %s carries no %s marker -- `import` lands records in "
            "the CANONICAL store only (a scratch store is never an import "
            "target)" % (store_root, store.CANONICAL_MARKER))
    if os.path.realpath(foreign_root) == os.path.realpath(store_root):
        raise store.StoreError("REFUSED: the foreign store is the target")
    if not os.path.isdir(os.path.join(foreign_root, "records")):
        raise store.StoreError("REFUSED: %s has no records/ directory"
                               % foreign_root)
    if bench_root is None:
        bench_root = os.path.join(store.REPO_ROOT, "bench")
    sets = _committed_sets(bench_root)

    registry = {r["machine_id"]: r for r in env.load_registry(store_root)}
    pending = None
    if register_machine:
        row = _foreign_registry_row(foreign_root, register_machine)
        if row is None:
            raise store.StoreError(
                "REFUSED: --register-machine %s but %s has no such row in its "
                "machines.tsv; register explicitly with `pcrecbench machines "
                "register`" % (register_machine,
                               env.registry_path(foreign_root)))
        pending = row
        if register_machine not in registry:
            registry[register_machine] = row

    paths = list(store.iter_records(foreign_root))
    refusals = []
    if not paths:
        raise store.StoreError("REFUSED: %s holds no records" % foreign_root)

    # (a) scratch, machine, set -- each cheap and named; (b) validation
    plan = []                                    # (src, dst, setup)
    for src in paths:
        try:
            setup = _read_setup(src)
        except Exception as e:                   # noqa: BLE001
            refusals.append((src, "line 1 is not JSON (%s)" % e))
            continue
        if store.record_tier(setup) == store.TIER_SCRATCH:
            refusals.append((src, "scratch-tier record: a `tier: scratch` "
                             "record can never enter the canonical store"))
            continue
        e = setup.get("environment") or {}
        mid = e.get("machine_id")
        reg = registry.get(mid)
        if reg is None:
            refusals.append((src, "machine_id %r is unknown to %s (register "
                             "it: `pcrecbench machines register` or `import "
                             "--register-machine`)"
                             % (mid, env.registry_path(store_root))))
        elif ((e.get("hostname"), e.get("cpu_model"), str(e.get("cores")))
              != (reg["hostname"], reg["cpu_model"], reg["cores"])):
            refusals.append((src, "machine_id %r is inconsistent with its "
                             "registry row: record says hostname=%s "
                             "cpu_model=%s cores=%s, registry says %s / %s / "
                             "%s" % (mid, e.get("hostname"), e.get("cpu_model"),
                                     e.get("cores"), reg["hostname"],
                                     reg["cpu_model"], reg["cores"])))
        sb = setup.get("subbench") or {}
        have = sets.get(sb.get("id"))
        ch = sb.get("content_hash")
        if have is None:
            refusals.append((src, "sub-bench %r is not a committed set of "
                             "this repo" % sb.get("id")))
        elif str(sb.get("version")) != have[0]:
            refusals.append((src, "sub-bench version mismatch: record %s@%s, "
                             "this repo commits %s@%s"
                             % (sb.get("id"), sb.get("version"), sb.get("id"),
                                have[0])))
        elif ch != have[1]:
            refusals.append((src, "sub-bench manifest sha256 mismatch for "
                             "%s@%s: record %s, this repo's committed set "
                             "%s (the foreign checkout measured a different "
                             "set)" % (sb.get("id"), sb.get("version"),
                                       ch, have[1])))
        dst = os.path.join(
            store.record_dir(store_root, sb.get("id"), sb.get("version"),
                             (setup.get("testee") or {}).get("testee_id")),
            os.path.basename(src))
        plan.append((src, dst, setup))

    if not refusals:
        # validation is the slow check: run it only once the cheap ones pass
        bad = _validate_all([p[0] for p in plan])
        refusals.extend(bad)

    todo, present = [], []
    if not refusals:
        for src, dst, setup in plan:
            if os.path.exists(dst):
                if _same_bytes(src, dst):
                    present.append(dst)
                else:
                    refusals.append((src, "duplicate record_id %s whose bytes "
                                     "DIFFER from the store's %s (never "
                                     "clobbered)" % (setup["record_id"], dst)))
            else:
                todo.append((src, dst))
    if refusals:
        raise ImportRefused(refusals)

    # ---- pass 2: nothing below can be a refusal
    if pending is not None:
        env.register_machine(store_root, pending["machine_id"],
                             pending["hostname"], pending["cpu_model"],
                             pending["cores"], pending["first_seen"],
                             pending["note"])
    done = []
    for src, dst in todo:
        d = os.path.dirname(dst)
        os.makedirs(d, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=d, prefix=store.STAGING_PREFIX)
        os.close(fd)
        try:
            shutil.copyfile(src, tmp)
            os.replace(tmp, dst)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)
        done.append(dst)
    store.index(store_root)
    return done, present


def _same_bytes(a, b):
    with open(a, "rb") as fa, open(b, "rb") as fb:
        return fa.read() == fb.read()


def _validate_all(paths):
    """-> [(path, reason)] for every record the shared validator rejects.
    One batch call; on failure each file is re-run alone to attribute."""
    ok, out = store.validate_file_batch(paths)
    if ok:
        return []
    bad = []
    for p in paths:
        good, o = store.validate_file(p)
        if not good:
            bad.append((p, "FAILED validation:\n%s" % o.strip()))
    return bad or [(paths[0], "FAILED validation:\n%s" % out.strip())]
