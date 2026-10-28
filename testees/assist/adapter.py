"""testees/assist/adapter.py -- the ASSISTED configs ([B148] lane b148aw;
docs/design/unusual_set_v1.md 5.5, 7.1-7.4).

An assisted config is its BASE config (configs.toml `base`: the same engine
adapter, library and version) plus, for each member the engine lacks, an
ASSIST: host code inside the 300-token budget, authored blind
(bench/unusual/assists/<member>/<engine>/assist.<ext>), counted by
tools/tokcount.py and recorded in the ledger assists.tsv. This adapter

  * describes the base's testee block with `assist-v01` appended LAST to
    `config_extra` and `testee.assist` = the ASSISTED ledger rows, each
    re-counted from its file (a ledger that disagrees with the counter is
    refused BY NAME -- X50);
  * compiles an ASSISTED member by building its assist into the assist
    RUNNER (testees/assist/ub_runner.c: the driver protocol; ub_timed.c: the
    timed loops in a translation unit of their own, BD16) and timing its
    `ub_setup` as the base's first compile phase; every other pattern is
    handed to the BASE adapter unchanged;
  * grants `unusual-<member>` per ASSISTED row (`capability_grants`) and
    cites a NOT-CAPABLE row by its count (`declaration_ref_for`,
    capability.not_capable_declaration_ref);
  * scopes a cell to the members assisted on its engine, their `-twin` arms
    and the floor (`pattern_scope`).

`$PCRECBENCH_ASSISTS_DIR` (a fixture dir; tools/check_assist.py's dummies)
forces the SCRATCH tier: a dummy is never a pinned record.
"""
import os

from pcrecbench import adapters as _ad
from pcrecbench import assists as _as
from pcrecbench import capability as _cap
from pcrecbench import driverrun as _dr

HERE = os.path.dirname(os.path.abspath(__file__))
TOKEN = "assist-" + _as.ASSIST_VERSION

#: compile-row pairs an ASSISTED row carries (pattern scope)
ASSIST_DECL = {
    "assist_member": {
        "type": "string", "scope": "pattern",
        "source": "testees/assist/adapter.py: the pattern id an assist answers",
        "description": "the member this compile row's assist answers; absent "
                       "on a row the base adapter compiled natively"},
    "assist_sha256": {
        "type": "sha256", "scope": "pattern",
        "source": "sha256 of bench/unusual/assists/<member>/<engine>/assist.<ext>",
        "description": "identity of the assist file (= testee.assist.members[].sha256)"},
    "assist_tokens": {
        "type": "integer", "scope": "pattern",
        "source": "tools/tokcount.py (tokcount-1) over the assist file",
        "description": "the counted tokens, fenced boilerplate excluded (budget 300)"},
    "assist_runner": {
        "type": "string", "scope": "pattern",
        "source": "the runner's own `info version` line",
        "description": "the assist runner's protocol version (ub-runner-<N>)"},
}

#: which pattern ids of bench/unusual an assisted config runs beside its
#: members: the callouts members' twins (the common subset, captures only)
#: and netstr's, so `real - twin` reads on one config
TWINS = {"co-luhn": "co-luhn-twin", "co-isbn": "co-isbn-twin",
         "co-member": "co-member-twin", "co-netstr": "co-netstr-twin"}


class Adapter(_ad.Adapter):
    name = "assist"
    calls_mode = True
    native_callouts = True

    def __init__(self, directory):
        super().__init__(directory)
        self._bases = {}

    # ---------------------------------------------------------------- base

    def _base(self, testee_id):
        """-> (base adapter, base config id, engine)."""
        cfg = self.config(testee_id)
        bid = cfg["base"]
        if bid not in self._bases:
            for name, a in _ad.discover().items():
                if name != "assist" and bid in a.testees():
                    self._bases[bid] = a
                    break
            else:
                raise _ad.AdapterError("%s: no adapter provides its base %r"
                                       % (testee_id, bid))
        return self._bases[bid], bid, cfg["engine"]

    def _members(self, testee_id):
        """-> {member: ledger row} of the ASSISTED rows for this engine,
        each RE-COUNTED: a row whose file, count or verdict disagrees with
        the counter is refused by name (the ledger is a claim; the file is
        the fact)."""
        _a, _b, engine = self._base(testee_id)
        out = {}
        for m, row in sorted(_as.assisted_members(engine).items()):
            _as.check_pair(m, engine)
            path = _as.assist_path(m, engine)
            if not os.path.exists(path):
                raise _ad.AdapterError("assists.tsv %s says %s/%s is ASSISTED "
                                       "but %s does not exist" % (row["ref"], m, engine, path))
            c = _as.count(path)
            sha = _as._sha(path)
            problems = []
            if c["smuggled"]:
                problems.append("a fence breaks its shape rule: %s" % c["smuggled"])
            if c["tokens"] > _as.tokcount.BUDGET:
                problems.append("%d tokens > budget %d" % (c["tokens"], _as.tokcount.BUDGET))
            if str(c["tokens"]) != str(row.get("tokens")):
                problems.append("the ledger says %s tokens, the counter %d"
                                % (row.get("tokens"), c["tokens"]))
            if row.get("assist_sha256") and row["assist_sha256"] != sha:
                problems.append("the ledger's sha256 is not the file's")
            drift = _as.fence_drift(m, engine, path)
            if drift:
                problems.append("fences differ from the template: %s" % "; ".join(drift))
            if problems:
                raise _ad.AdapterError("assist %s/%s (%s) is not ASSISTED as "
                                       "recorded: %s" % (m, engine, row["ref"],
                                                         "; ".join(problems)))
            out[m] = dict(row, _count=c, _sha=sha, _path=path)
        return out

    # ------------------------------------------------------------ interface

    def tier(self, testee_id):
        if _as.is_fixture_dir():
            return "scratch"
        a, bid, _e = self._base(testee_id)
        return a.tier(bid)

    def binary_identity(self, testee_id, workdir=None):
        a, bid, _e = self._base(testee_id)
        return a.binary_identity(bid, workdir)

    def prepare(self, testee_id, workdir):
        a, bid, _e = self._base(testee_id)
        return a.prepare(bid, workdir)

    def supports_calls(self, testee_id):
        a, bid, _e = self._base(testee_id)
        return a.supports_calls(bid)

    def unusual_metadata_decl(self, testee_id):
        a, bid, _e = self._base(testee_id)
        return a.unusual_metadata_decl(bid)

    def describe(self, testee_id, workdir=None):
        a, bid, engine = self._base(testee_id)
        block = a.describe(bid, workdir)
        block["config_extra"] = "-".join(
            p for p in (block.get("config_extra"), TOKEN) if p)
        members = self._members(testee_id)
        block["assist"] = {
            "assist_version": _as.ASSIST_VERSION,
            "members": [{"member": m, "tokens": r["_count"]["tokens"],
                         "lines": r["_count"]["lines"], "sha256": r["_sha"]}
                        for m, r in members.items()]}
        decl = dict(block.get("engine_metadata_declaration") or {})
        decl.update(ASSIST_DECL)
        from pcrecbench import callees as _callees
        for k, v in _callees.CALLOUT_DECL.items():     # incl. the fire pass's
            decl.setdefault(k, v)
        block["engine_metadata_declaration"] = decl
        block["build_flags"] = (
            (block.get("build_flags") or "") +
            "; ASSISTED config (%s, [B148] b148aw, unusual_set_v1.md 5.5): "
            "base %s; each ASSISTED member's assist (bench/unusual/assists/"
            "<member>/%s/assist.%s) is linked into testees/assist's runner "
            "(the driver protocol + ub_timed.c's timed loops); members: %s%s"
            % (TOKEN, bid, engine, _as.engine_spec(engine)["ext"],
               ", ".join(members) or "none",
               "; FIXTURE assists from $%s" % _as.ENV_DIR
               if _as.is_fixture_dir() else ""))
        return block

    def pattern_scope(self, testee_id, sb):
        _a, _b, engine = self._base(testee_id)
        mine = {m for (m, e) in _as.PAIRS if e == engine}
        scope = mine | {TWINS[m] for m in mine if m in TWINS} | {"floor"}
        return {p.name for p in sb.patterns if p.name in scope}

    def capability_grants(self, testee_id, sb):
        return frozenset(_cap.UNUSUAL_PREFIX + m for m in self._members(testee_id))

    def declaration_ref_for(self, testee_id, sb, pattern, missing):
        _a, _b, engine = self._base(testee_id)
        row = _as.not_capable_members(engine).get(pattern.name)
        if row is None:
            return None
        return _cap.not_capable_declaration_ref(
            row["ref"], int(row["tokens"]), int(row.get("budget") or _as.tokcount.BUDGET))

    # -------------------------------------------------------------- compile

    def compile(self, testee_id, pattern_id, pattern, options, trials,
                workdir, requires_free_spacing=False):
        a, bid, engine = self._base(testee_id)
        members = self._members(testee_id)
        if pattern_id not in members:
            opts = dict(options or {})
            if not getattr(a, "native_callouts", False):
                opts.pop("callouts", None)
            cp = a.compile(bid, pattern_id, pattern, opts, trials, workdir,
                           requires_free_spacing=requires_free_spacing)
            for r in cp.forms.values():
                if r.handle is not None:
                    r.handle = dict(r.handle, _assist_base=a)
            return cp
        row = members[pattern_id]
        fam = _as.family_of(pattern_id)
        try:
            drv, prov = _as.build(pattern_id, engine, row["_path"])
            cdrv = None
            if fam == "callouts":
                cdrv, cprov = _as.build(pattern_id, engine, row["_path"], count=True)
        except _as.AssistError as e:
            return _ad.CompiledPattern({_ad.FORM_PLAIN: _ad.CompileResult(
                "did-not-compile", diagnostic="assist build failed: %s" % e)})
        # run.driver_compiler is ONE slug: spell the compiler as the base's
        # own driver build did (same language, same toolchain), else canon.
        from pcrecbench import env as _env
        known = sorted({v["compiler"] for v in _dr.DRIVER_BUILDS.values()})
        tool = _as._rust_tool("rustc") if prov["compiler"] == "rustc" else prov["compiler"]
        _dr.DRIVER_BUILDS[os.path.abspath(drv)] = {
            "command_line": prov["command_line"],
            "compiler": known[0] if len(known) == 1
            else _env.canon_compiler(_env.compiler_raw(tool))}
        pdir = os.path.join(workdir, "p-" + pattern_id)
        os.makedirs(pdir, exist_ok=True)
        patfile = os.path.join(pdir, "pattern.rx")
        with open(patfile, "wb") as f:
            f.write(bytes(pattern))
        phases = self.describe_phases(testee_id, workdir)
        co = (options or {}).get("callouts")
        spec = co.get("spec") if (co and fam == "callouts") else None
        argv = [drv, "--pattern", patfile, "--member", pattern_id,
                "--compile-trials", str(trials), "--phases", ",".join(phases)]
        if spec:
            argv += ["--callees", spec]
        out = _dr.run_driver(argv, timeout=max(60, 30 * trials), cwd=workdir)
        one = lambda r: _ad.CompiledPattern({_ad.FORM_PLAIN: r})  # noqa: E731
        if out.timed_out:
            return one(_ad.CompileResult("timed-out", diagnostic=out.diagnostic()))
        if out.returncode == 3:
            return one(_ad.CompileResult(
                "did-not-compile", diagnostic=out.diagnostic() or "ub_setup failed"))
        if out.returncode != 0:
            return one(_ad.CompileResult(
                "crashed", diagnostic=out.diagnostic()
                or "assist driver exit %s" % out.returncode))
        meta = {"assist_member": pattern_id, "assist_sha256": row["_sha"],
                "assist_tokens": int(row["_count"]["tokens"]),
                "assist_runner": out.info.get("version", "ub-runner-?")}
        if fam == "callouts":
            meta["callees_sha256"] = prov.get("callees_sha256")
            meta["callout_arm"] = co.get("arm") if co else "real"
            meta["callout_spec"] = co.get("spec_decl") if co else "none"
        handle = {"driver": drv, "pattern_file": patfile, "member": pattern_id,
                  "assisted": True, "has_g1": pattern_id in _as.HAS_G1,
                  "callees": spec, "count_driver": cdrv,
                  "stream_anchor": "native",
                  # an assist's negative return is the ENGINE's own give-up
                  # code (ub_assist.h), reported `giveup:<code>`
                  "giveup_range": (-(1 << 31), -1)}
        return one(_ad.CompileResult(
            "compiled", phase_seconds=out.phase_seconds, engine_metadata=meta,
            handle=handle, artifact_bytes=os.path.getsize(drv)))

    def describe_phases(self, testee_id, workdir):
        a, bid, _e = self._base(testee_id)
        if not hasattr(self, "_phases"):
            self._phases = {}
        if bid not in self._phases:
            self._phases[bid] = list(a.describe(bid, workdir)["compile_phases"])
        return self._phases[bid]

    # -------------------------------------------------------------- measure

    def fire_handle(self, handle):
        if handle.get("assisted"):
            if not handle.get("count_driver"):
                return None
            return dict(handle, driver=handle["count_driver"])
        a = self._handle_base(handle)
        fh = getattr(a, "fire_handle", None) if a else None
        return fh(handle) if fh else None

    def mem_method(self, handle):
        if handle.get("assisted"):
            return None              # the runner has no --mem-pass (owed)
        a = self._handle_base(handle)
        return a.mem_method(handle) if a else None

    def _handle_base(self, handle):
        # a delegated handle is the base adapter's own; remember whose
        return handle.get("_assist_base")

    def measure(self, handle, regime, subjects, iters, trials, timeout=None):
        if not handle.get("assisted"):
            a = self._handle_base(handle)
            return a.measure(handle, regime, subjects, iters, trials, timeout=timeout)
        from pcrecbench.subbench import REGIME_MODE
        argv = [handle["driver"], "--pattern", handle["pattern_file"],
                "--member", handle["member"], "--mode", REGIME_MODE[regime],
                "--iters", str(iters), "--has-g1", "1" if handle["has_g1"] else "0"]
        if handle.get("callees"):
            argv += ["--callees", handle["callees"]]
        if regime == "throughput":
            argv.append("--find-all")
        for flag in ("utf8_advance", "prime", "mem_pass"):
            if handle.get(flag):
                # refused BY NAME by the runner, never silently dropped
                argv.append("--" + flag.replace("_advance", "").replace("_", "-"))
        return _dr.per_trial(argv, subjects, trials, timeout=timeout,
                             pin=handle.get("pin"),
                             subject_timeout=handle.get("subject_timeout"))
