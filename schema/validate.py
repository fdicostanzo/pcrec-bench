#!/usr/bin/env python3
"""validate.py -- the pcrec-bench record validator, shared by the harness and
the reporter (requirements.md 6: "a tiny validator the reporter shares").

It checks two things a record must satisfy:

  * every LINE against its kind's JSON Schema (schema/record.schema.json),
    line 1 as the setup layer and every later line as a result row; and
  * the CROSS-LINE rules a schema cannot express -- X1..X33 in
    docs/design/record_schema.md 9: derived identifiers, the content hash,
    roster references, dense trial numbering, the compile-cost class, the
    "no timing on a cell that did not compile or did not agree with its
    expectation" rule, engine_metadata declarations, the record-status
    gates, (v1.2) the record TIER: a local binary is never `pinned`
    (X28) and a `scratch` record says what its binary was (X29),
    (v1.3) at most one `patterns[]` entry may be the set's FLOOR (X30),
    and (v1.4, [B20], docs/design/gate_shape_v14.md) the TRIAL-AGREEMENT
    block: its verdict follows from its counts (X31), its counts are
    RECOMPUTED from the match rows by this file's own second
    implementation of the rule's arithmetic (X32, `judge_trial_agreement`
    below -- deliberately NOT imported from pcrecbench/reduce.py, because
    a verdict a harness stamped beside rows it also wrote is only
    evidence when something independent re-derives it), and the block is
    present iff the record is stamped >= 1.4 (X33). X13 is VERSIONED at
    1.4: the record's own `schema_version` selects which text judges it.

Every message names the FILE, the 1-based LINE and the field path.

Usage:
    validate.py FILE...                 validate; exit 0 if all are valid
    validate.py --expect-reject FILE... exit 0 only if EVERY file is REJECTED
                                        (the positive controls in
                                        schema/examples/bad/)
    validate.py --check-filename FILE...  additionally enforce X4: the file's
                                        basename is <record_id>.jsonl
    validate.py --allow-mixed-versions FILE...  suppress X17
    validate.py --print-hash FILE       print the content hash the file's
                                        bytes imply (X6's expected value) and
                                        exit; for restamping an edited example

Requires python3 + jsonschema (4.19 on this box). Deliberately no other
dependency: it runs anywhere a record is read.
"""

import argparse
import hashlib
import json
import os
import re
import sys

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - environment problem, not a record problem
    print("validate.py: the `jsonschema` package is required (4.19 on this box)",
          file=sys.stderr)
    sys.exit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "record.schema.json")

ROW_KINDS = ("match", "compile")
RESERVED_KINDS = {
    "match-list": "reserved for the list-valued scan regime (OD-B3); "
                  "no shape is defined yet",
}
SIMD_SLUG = {"on": "simd", "off": "nosimd", "n-a": "simdna"}
DEFAULT_FORM = "plain"          # an absent `form` IS `plain` (the note 5)
DEFAULT_TIER = "pinned"         # an absent `tier` IS `pinned` (the note 6.8)
X13_V14_MINOR = 4               # X13's v1.4 text applies from 1.4 (the note 4)
LOCAL_VERSION_PREFIX = "local:"  # the local-binary engine_version shape (6.2)

# docs/design/record_schema.md 6.2. A RELEASE TAG is a plain dotted version,
# optionally with a single trailing letter revision (`8.45a`). Anything else --
# a `git describe` string, an `-rc1`, a `+build` -- is not a release, and a
# testee that is not on a release must carry the commit that IS its identity.
RELEASE_TAG_RE = re.compile(r"^\d+\.\d+(\.\d+)?[a-z]?\d*$")


class Problem:
    __slots__ = ("path", "line", "field", "msg", "rule")

    def __init__(self, path, line, field, msg, rule=""):
        self.path, self.line, self.field, self.msg, self.rule = \
            path, line, field, msg, rule

    def __str__(self):
        where = f"{self.path}:{self.line}"
        field = f": {self.field}" if self.field else ""
        rule = f" [{self.rule}]" if self.rule else ""
        return f"{where}{field}: {self.msg}{rule}"


# ---------------------------------------------------------------- the hash

def compute_content_hash(setup_obj, row_lines):
    """docs/design/record_schema.md 3. Line 1 canonicalised WITHOUT its own
    `content_hash` member (that is what breaks the circularity), then each row
    line's text as written with trailing whitespace stripped, joined by \\n."""
    stripped = {k: v for k, v in setup_obj.items() if k != "content_hash"}
    canon = json.dumps(stripped, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False)
    parts = [canon] + [ln.rstrip() for ln in row_lines]
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()


def parse_loadavg(raw):
    """The first three fields of a /proc/loadavg line, as floats. Returns None
    if the line does not have three parseable numbers up front -- which is
    itself the finding."""
    parts = str(raw).split()
    if len(parts) < 3:
        return None
    try:
        return [float(x) for x in parts[:3]]
    except ValueError:
        return None


# ------------------------------------------- the normalization rules (6.6-6.7)
#
# docs/design/record_schema.md 6 splits the OPEN identifiers from the fixed
# enums: what is pinned is the RULE that produces the string. A rule stated
# only in prose is a rule nobody runs, so the three that CAN be made
# mechanical are functions here and rule X23 checks each against its own
# `_raw` sibling. `machine_id` is the one that cannot -- it is an assignment,
# not a derivation (6.5) -- and it stays asserted.

def normalize_cpu_model(raw):
    """6.6: drop (R)/(TM), drop a trailing `@ <freq>`, lowercase, collapse
    runs of non-alphanumerics to one `-`, strip leading/trailing `-`."""
    s = re.sub(r"\((?:R|TM|tm|r)\)", "", str(raw))
    s = re.sub(r"\s*@\s*\S+\s*$", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s.lower())
    return s.strip("-")


def normalize_kernel(raw):
    """6.7: `uname -s` and `uname -r`, lowercased, joined by `-`."""
    return re.sub(r"\s+", "-", str(raw).strip()).lower()


def normalize_compiler(raw):
    """6.7: the FIRST line of `$CC --version` reduced to `<name>-<version>`.
    The name is the first token, lowercased with non-alphanumerics collapsed;
    the version is the LAST token that is a bare dotted number, which is what
    gcc, clang and rustc all put there and what a build string
    (`15.2.0-4ubuntu4`) deliberately is not."""
    line = str(raw).splitlines()[0] if str(raw).strip() else ""
    toks = line.split()
    if not toks:
        return ""
    name = re.sub(r"[^a-z0-9]+", "-", toks[0].lower()).strip("-")
    version = ""
    for tok in toks:
        bare = tok.strip("(),")
        if re.fullmatch(r"\d+(\.\d+)*", bare):
            version = bare
    return f"{name}-{version}" if version else name


NORMALIZED = (
    ("cpu_model", "cpu_model_raw", normalize_cpu_model),
    ("kernel", "kernel_raw", normalize_kernel),
    ("compiler", "compiler_raw", normalize_compiler),
)


# ------------------------------------------------------- derived identifiers

def derive_testee_id(t):
    """docs/design/record_schema.md 6.4."""
    version_slug = re.sub(r"[^a-z0-9.]", "-", str(t.get("engine_version", "")).lower())
    caps = "caps" if t.get("captures") == "on" else "nocaps"
    simd = SIMD_SLUG.get(t.get("simd"), "?")
    tid = f"{t.get('engine_name')}_{version_slug}_{t.get('engine_mode')}-{caps}-{simd}"
    if t.get("config_extra"):
        tid += "_" + t["config_extra"]
    return tid


def derive_record_id(setup):
    """docs/design/record_schema.md 3, without the -<n> disambiguator (which is
    assigned at write time and is accepted as a suffix)."""
    sb = setup.get("subbench", {})
    stamp = str(setup.get("run", {}).get("timestamp", "")).replace("-", "").replace(":", "")
    return (f"{sb.get('id')}@{sb.get('version')}"
            f"__{setup.get('testee', {}).get('testee_id')}"
            f"__{setup.get('environment', {}).get('machine_id')}"
            f"__{stamp}")


# --------------------------------------- trial agreement, the SECOND implementation
#
# docs/design/gate_shape_v14.md 3.5 -- "the rule, as arithmetic" -- spelled
# here a second time ON PURPOSE (its 4 V6): pcrecbench/reduce.py's
# `judge_trial_agreement` is what the harness stamps and the reporter
# renders; THIS is what X32 re-derives the stamp from. The two share no
# source, so a harness that stamps `0 of 72 groups` beside rows that say
# otherwise is caught rather than echoed. X32 compares the INTEGER counts
# and the worst group's key only -- never a float -- so the two agree on a
# verdict, not on a bit pattern; a row exactly on a boundary (`x == k*m`
# is not slow, `min == m/k` is not fast) yields the same integer in both
# as long as both spell the expressions as 3.5 does.

MATCHED_AS_EXPECTED = "matched-as-expected"
TIMED_OUT = "timed-out"


def judge_trial_agreement(rows, k, d_min, share_c):
    """The 3.5 arithmetic over a record's MATCH rows (dicts as written).
    -> the `trial_agreement` block minus `rule`/`k`/`d_min`/`share_c`."""
    import statistics
    match = [r for r in rows if isinstance(r, dict) and r.get("kind") == "match"]
    keys = {}
    for r in match:
        key = (r.get("pattern_id"), r.get("regime"), r.get("form") or DEFAULT_FORM,
               r.get("subject_id"))
        keys.setdefault(key, []).append(r)
    trials = max((int(r.get("trial") or 0) for r in match), default=0)
    out = {"trials": trials, "groups_judged": 0, "groups_disagreeing": 0,
           "rows_judged": 0, "rows_disagreeing": 0, "rows_unjudged": 0,
           "rows_unjudged_reasons": {"few_timed_trials": 0, "all_timed_out": 0,
                                     "na_trials": 0},
           "worst_group": None}
    if trials < 5 or trials % 2 == 0:
        out["rows_unjudged"] = len(keys)
        out["rows_unjudged_reasons"]["na_trials"] = len(keys)
        return out
    groups = {}   # group key -> [n, d, min_seq]
    for key, krows in keys.items():
        timed = {}
        n_timed_out = 0
        for r in krows:
            if r.get("match_outcome") == TIMED_OUT:
                n_timed_out += 1
            t = r.get("timing") or {}
            it = t.get("iterations")
            if (r.get("match_outcome") == MATCHED_AS_EXPECTED
                    and isinstance(it, int) and it > 1
                    and isinstance(t.get("elapsed_ns"), int)):
                timed[r.get("trial")] = float(t["elapsed_ns"]) / it
        if n_timed_out >= 1 and len(timed) >= 1:
            disagreeing = True                      # a MIXED row (R-19 as amended)
        elif n_timed_out == len(krows):
            out["rows_unjudged"] += 1               # the engine's consistent answer
            out["rows_unjudged_reasons"]["all_timed_out"] += 1
            continue
        elif len(timed) >= 2:
            xs = [timed[t] for t in sorted(timed)]
            m = statistics.median(xs)
            slow = sum(1 for x in xs if x > k * m)
            fast = 1 if min(xs) < m / k else 0
            disagreeing = (slow >= 2 or fast == 1)
        else:
            out["rows_unjudged"] += 1
            out["rows_unjudged_reasons"]["few_timed_trials"] += 1
            continue
        out["rows_judged"] += 1
        g = groups.setdefault(key[:3], [0, 0, None])
        g[0] += 1
        if disagreeing:
            out["rows_disagreeing"] += 1
            g[1] += 1
        seqs = [r.get("seq") for r in krows if isinstance(r.get("seq"), int)]
        if seqs:
            lo = min(seqs)
            g[2] = lo if g[2] is None else min(g[2], lo)
    out["groups_judged"] = len(groups)
    out["groups_disagreeing"] = sum(1 for n, d, _s in groups.values()
                                    if d >= d_min and share_c * d >= n)
    if groups:
        def rank(item):
            (_pid, _reg, _form), (n, d, min_seq) = item
            return (d, -n, -(min_seq if min_seq is not None else 0))
        (pid, reg, form), (n, d, _s) = max(groups.items(), key=rank)
        out["worst_group"] = {"pattern_id": pid, "regime": reg, "form": form,
                              "d": d, "n": n}
    return out


def expected_verdict(block):
    """X31: the verdict the block's own counts require."""
    trials = block.get("trials")
    if not isinstance(trials, int) or trials < 5 or trials % 2 == 0:
        return "n/a-trials"
    gd = block.get("groups_disagreeing")
    return "disagree" if isinstance(gd, int) and gd >= 1 else "agree"


# ---------------------------------------------------------------- the checks

class RecordValidator:
    def __init__(self, schema):
        self.schema = schema
        self.schema_version = schema.get("x-record-schema-version", "1.0")
        base = {"$schema": schema["$schema"], "$defs": schema["$defs"]}
        self.by_kind = {
            "setup": Draft202012Validator(dict(base, **{"$ref": "#/$defs/setup"})),
            "match": Draft202012Validator(dict(base, **{"$ref": "#/$defs/match_row"})),
            "compile": Draft202012Validator(dict(base, **{"$ref": "#/$defs/compile_row"})),
        }

    # -- one file ---------------------------------------------------------
    def validate_file(self, path, check_filename=False):
        problems = []
        try:
            with open(path, encoding="utf-8") as fh:
                raw = fh.read().split("\n")
        except OSError as exc:
            return [Problem(path, 0, "", f"cannot read: {exc}")], None
        # A trailing newline produces a final empty element; that is not a line.
        while raw and raw[-1] == "":
            raw.pop()
        if not raw:
            return [Problem(path, 0, "", "empty file: a record has at least a "
                                         "setup line", "X1")], None

        objs = []
        for n, text in enumerate(raw, start=1):
            if text.strip() == "":
                problems.append(Problem(path, n, "", "blank line: JSONL has no "
                                                     "blank lines"))
                objs.append(None)
                continue
            try:
                obj = json.loads(text)
            except json.JSONDecodeError as exc:
                problems.append(Problem(path, n, "", f"not valid JSON: {exc.msg} "
                                                     f"(col {exc.colno})"))
                objs.append(None)
                continue
            if not isinstance(obj, dict):
                problems.append(Problem(path, n, "", "each line must be a JSON "
                                                     "object"))
                objs.append(None)
                continue
            objs.append(obj)

        # X1 / X2: line kinds.
        setup = None
        rows = []
        for n, obj in enumerate(objs, start=1):
            if obj is None:
                continue
            kind = obj.get("kind")
            if kind in RESERVED_KINDS:
                problems.append(Problem(path, n, "kind",
                                        f"`{kind}` is RESERVED: {RESERVED_KINDS[kind]}",
                                        "X2"))
                continue
            if n == 1:
                if kind != "setup":
                    problems.append(Problem(path, 1, "kind",
                                            f"line 1 must be the setup layer, "
                                            f"found kind={kind!r}", "X1"))
                    continue
                setup = obj
                continue
            if kind == "setup":
                problems.append(Problem(path, n, "kind",
                                        "a second setup line: two records have "
                                        "been concatenated into one file", "X1"))
                continue
            if kind not in ROW_KINDS:
                problems.append(Problem(path, n, "kind",
                                        f"unknown row kind {kind!r}; known kinds "
                                        f"are {', '.join(ROW_KINDS)}", "X2"))
                continue
            rows.append((n, obj))

        # Per-line schema validation.
        for n, obj in enumerate(objs, start=1):
            if obj is None:
                continue
            kind = obj.get("kind")
            v = self.by_kind.get(kind)
            if v is None:
                continue  # already reported by the kind pass
            for err in sorted(v.iter_errors(obj), key=lambda e: list(e.absolute_path)):
                field = ".".join(str(p) for p in err.absolute_path) or "(document)"
                problems.append(Problem(path, n, field, err.message, "SCHEMA"))

        if setup is None:
            return problems, None

        problems.extend(self._cross_line(path, setup, rows, raw, check_filename))
        return problems, setup.get("schema_version")

    # -- the cross-line rules --------------------------------------------
    def _cross_line(self, path, setup, rows, raw, check_filename):
        p = []
        add = p.append

        # schema version this validator implements
        sv = str(setup.get("schema_version", ""))
        f_minor = None
        if re.match(r"^\d+\.\d+$", sv):
            f_major, f_minor = (int(x) for x in sv.split("."))
            o_major, o_minor = (int(x) for x in self.schema_version.split("."))
            if f_major != o_major:
                add(Problem(path, 1, "schema_version",
                            f"major version {sv} but this validator implements "
                            f"{self.schema_version}; a major boundary needs a "
                            f"declared migration", "X17"))
            elif f_minor > o_minor:
                add(Problem(path, 1, "schema_version",
                            f"{sv} was written by a newer schema minor than this "
                            f"validator ({self.schema_version}); upgrade the "
                            f"validator rather than reading it half-blind", "X17"))

        # X3 record_id
        want = derive_record_id(setup)
        got = str(setup.get("record_id", ""))
        if got != want and not re.match(r"^" + re.escape(want) + r"-\d+$", got):
            add(Problem(path, 1, "record_id",
                        f"is {got!r} but the record's own fields derive "
                        f"{want!r} (optionally + '-<n>')", "X3"))

        # X4 file name
        if check_filename:
            base = os.path.basename(path)
            if base != got + ".jsonl":
                add(Problem(path, 1, "record_id",
                            f"file is named {base!r} but the record id requires "
                            f"{got + '.jsonl'!r}", "X4"))

        # X5 testee_id
        testee = setup.get("testee", {})
        want_t = derive_testee_id(testee)
        if testee.get("testee_id") != want_t:
            add(Problem(path, 1, "testee.testee_id",
                        f"is {testee.get('testee_id')!r} but the testee's own "
                        f"fields derive {want_t!r}", "X5"))

        # X6 content hash
        stored = setup.get("content_hash", {})
        if isinstance(stored, dict) and stored.get("algorithm") == "sha256":
            want_h = compute_content_hash(setup, raw[1:])
            if stored.get("value") != want_h:
                add(Problem(path, 1, "content_hash.value",
                            f"is {stored.get('value')} but the file's bytes hash "
                            f"to {want_h} (edited, truncated or restamped?)",
                            "X6"))

        # X22 a version that is not a release tag must carry its commit --
        # EXCEPT the v1.2 `local:` shape, whose identity is the binary itself
        # (X29 requires testee.binary.sha256 on it, via X28's tier rule): a
        # dirty tree has no single commit to name, and that is the point of
        # the shape rather than a gap in it.
        ev = str(testee.get("engine_version", ""))
        ec = testee.get("engine_commit")
        is_local = ev.startswith(LOCAL_VERSION_PREFIX)
        if ev and not is_local and not RELEASE_TAG_RE.match(ev):
            if not (isinstance(ec, str) and re.fullmatch(r"[0-9a-f]{40}", ec)):
                add(Problem(path, 1, "testee.engine_commit",
                            f"engine_version {ev!r} is not a release-tag shape "
                            f"(a plain dotted version), so the testee is "
                            f"pinned to a revision and the full 40-hex commit "
                            f"is what pins it; got {ec!r}", "X22"))

        # X28 a LOCAL binary can never be a pinned record (the note 6.8)
        tier = setup.get("tier", DEFAULT_TIER)
        if is_local and tier != "scratch":
            add(Problem(path, 1, "tier",
                        f"engine_version {ev!r} names a LOCAL binary (a file "
                        f"nobody pinned by commit), so the record must be "
                        f"`tier: scratch`; it is {tier!r} (absent = "
                        f"`pinned`). A bench number never comes from a "
                        f"dirty tree, and this is the rule that keeps it "
                        f"so", "X28"))

        # X29 a scratch record says WHAT THE BINARY WAS
        if tier == "scratch":
            b = testee.get("binary")
            if not (isinstance(b, dict) and isinstance(b.get("path"), str)
                    and b.get("path")
                    and isinstance(b.get("sha256"), str)
                    and re.fullmatch(r"[0-9a-f]{64}", b["sha256"])):
                add(Problem(path, 1, "testee.binary",
                            "the record is `tier: scratch` but carries no "
                            "testee.binary {path, sha256}; a scratch number "
                            "comes from a binary nobody pinned, so the file "
                            "itself is the only identity the record can "
                            "have, and it must say which", "X29"))

        # X16 lazy-jit warm-up
        if testee.get("execution_model") == "lazy-jit" and \
                int(testee.get("warmup_trials", 0)) < 1:
            add(Problem(path, 1, "testee.warmup_trials",
                        "a lazy-JIT testee pays its compile cost inside trial 1, "
                        "so at least one warm-up trial must be declared", "X16"))

        # X30 at most one pattern may be the set's FLOOR (the note 5, v1.3)
        floor_ids = sorted(e.get("pattern_id") for e in setup.get("patterns", [])
                           if e.get("role") == "floor")
        if len(floor_ids) > 1:
            add(Problem(path, 1, "patterns[].role",
                        f"{len(floor_ids)} patterns are role=floor "
                        f"{floor_ids}, but a record may carry at most one: "
                        f"the floor pattern's whole point is a SINGLE "
                        f"per-call baseline the rest of the set reads "
                        f"against, and two of them leave that baseline "
                        f"ambiguous", "X30"))

        # rosters
        pat_ids = {e.get("pattern_id") for e in setup.get("patterns", [])}
        subj_ids = {e.get("subject_id") for e in setup.get("subjects", [])}
        subj_bytes = {e.get("subject_id"): e.get("bytes_offered")
                      for e in setup.get("subjects", [])}
        regimes = set(setup.get("subbench", {}).get("regimes", []))
        decl = testee.get("engine_metadata_declaration", {}) or {}
        phases = list(testee.get("compile_phases", []) or [])

        # Everything below is keyed by (pattern, FORM): a testee with no
        # end-anchored mode compiles a SECOND artifact for the whole-subject
        # regime, and the two are different compiles of different text. They
        # must never share a row, a trial sequence or a provenance check.
        compiled_ok = {}          # (pattern, form) -> every compile row `compiled`
        seen_compile = {}         # (pattern, form) -> set of trials
        seen_match = {}           # (pattern, subject, regime, form) -> trials

        for n, row in rows:
            kind = row["kind"]
            pid = row.get("pattern_id")
            form = row.get("form", DEFAULT_FORM)
            # X7
            if pid not in pat_ids:
                add(Problem(path, n, "pattern_id",
                            f"{pid!r} is not in setup.patterns[]", "X7"))
            if kind == "match":
                sid = row.get("subject_id")
                if sid not in subj_ids:
                    add(Problem(path, n, "subject_id",
                                f"{sid!r} is not in setup.subjects[]", "X7"))
                # X8
                if row.get("regime") not in regimes:
                    add(Problem(path, n, "regime",
                                f"{row.get('regime')!r} is not among the "
                                f"sub-bench's declared regimes "
                                f"{sorted(regimes)}", "X8"))
                key = (pid, sid, row.get("regime"), form)
                seen_match.setdefault(key, {}).setdefault(row.get("trial"), []).append(n)
            else:
                seen_compile.setdefault((pid, form), {}) \
                            .setdefault(row.get("trial"), []).append(n)
                # X10
                if row.get("cost_class") != testee.get("execution_model"):
                    add(Problem(path, n, "cost_class",
                                f"is {row.get('cost_class')!r} but the testee's "
                                f"execution_model is "
                                f"{testee.get('execution_model')!r}", "X10"))
                # X12
                got_phases = [ph.get("name") for ph in
                              (row.get("cost", {}) or {}).get("phases", [])]
                if got_phases and got_phases != phases:
                    add(Problem(path, n, "cost.phases",
                                f"names/order {got_phases} do not equal the "
                                f"testee's declared compile_phases {phases}",
                                "X12"))
                ok = row.get("compile_outcome") == "compiled"
                compiled_ok[(pid, form)] = \
                    compiled_ok.get((pid, form), True) and ok
            # X15
            for name, value in (row.get("engine_metadata") or {}).items():
                self._check_metadata(add, path, n, name, value, decl, kind)

        # X18 the per-record emission order
        seq_lines = {}
        for n, row in rows:
            seq_lines.setdefault(row.get("seq"), []).append(n)
        for sq, lines in sorted(seq_lines.items(),
                                key=lambda kv: (kv[0] is None, kv[0])):
            if len(lines) > 1:
                add(Problem(path, lines[1], "seq",
                            f"seq {sq} appears on {len(lines)} result rows "
                            f"(also on line {lines[0]}); seq is the record's "
                            f"emission ORDER and must be unique", "X18"))
        nums = sorted(x for x in seq_lines if isinstance(x, int))
        if rows and nums != list(range(1, len(rows) + 1)):
            first = min(min(v) for v in seq_lines.values())
            add(Problem(path, first, "seq",
                        f"the {len(rows)} result rows carry seq {nums}; they "
                        f"must be a dense 1..N over EVERY result row of the "
                        f"record, in emission order", "X18"))

        # X9 dense trial numbering
        for (pid, form), trials in seen_compile.items():
            self._check_trials(add, path, trials,
                               f"{form} compile rows for pattern {pid!r}")
        for (pid, sid, reg, form), trials in seen_match.items():
            self._check_trials(add, path, trials,
                               f"{form} match rows for ({pid!r}, {sid!r}, "
                               f"{reg!r})")

        # X27 a whole-subject match row needs a whole-subject compile row
        for n, row in rows:
            if row["kind"] != "match":
                continue
            if row.get("form") != "whole-subject":
                continue
            pid = row.get("pattern_id")
            if (pid, "whole-subject") not in seen_compile:
                add(Problem(path, n, "form",
                            f"is `whole-subject` but the record has no "
                            f"whole-subject compile row for pattern {pid!r}; "
                            f"that artifact is a SEPARATE compile of "
                            f"different text and the record does not witness "
                            f"it", "X27"))

        # X11 no timing on an uncompiled or expectation-disagreeing cell
        for n, row in rows:
            if row["kind"] != "match" or "timing" not in row:
                continue
            pid = row.get("pattern_id")
            form = row.get("form", DEFAULT_FORM)
            if not compiled_ok.get((pid, form), False):
                add(Problem(path, n, "timing",
                            f"the {form} artifact of pattern {pid!r} did not "
                            f"compile cleanly in this record, so this cell "
                            f"must not be timed", "X11"))
            if row.get("match_outcome") != "matched-as-expected":
                add(Problem(path, n, "timing",
                            f"match_outcome is {row.get('match_outcome')!r}: a "
                            f"timing for a wrong answer is worse than no timing",
                            "X11"))

        env = setup.get("environment", {})

        # X23 the normalized identifiers derive from their raw siblings
        for field, raw_field, rule in NORMALIZED:
            raw = env.get(raw_field)
            if not isinstance(raw, str) or not raw.strip():
                continue          # the raw sibling is optional; no raw, no rule
            want_n = rule(raw)
            if env.get(field) != want_n:
                add(Problem(path, 1, f"environment.{field}",
                            f"is {env.get(field)!r} but {raw_field} "
                            f"{raw!r} normalizes to {want_n!r} by "
                            f"docs/design/record_schema.md 6", "X23"))

        # X19 the load evidence: the parse must agree with the raw line
        load = env.get("load", {}) or {}
        for when in ("before", "after"):
            sample = load.get(when)
            if not isinstance(sample, dict):
                continue
            got = parse_loadavg(sample.get("loadavg_raw", ""))
            if got is None:
                add(Problem(path, 1, f"environment.load.{when}.loadavg_raw",
                            f"{sample.get('loadavg_raw')!r} does not start "
                            f"with three numbers; it is not a /proc/loadavg "
                            f"line", "X19"))
                continue
            want = [sample.get("load1"), sample.get("load5"),
                    sample.get("load15")]
            for i, (name, w) in enumerate(zip(("load1", "load5", "load15"),
                                              want)):
                if not isinstance(w, (int, float)) or abs(w - got[i]) > 1e-9:
                    add(Problem(path, 1, f"environment.load.{when}.{name}",
                                f"is {w!r} but the sample's own "
                                f"loadavg_raw parses to {got[i]!r}; the "
                                f"number and its evidence disagree", "X19"))

        # X20 the load verdict follows from the samples and the limit
        limit = load.get("limit")
        verdict = load.get("verdict")
        peaks = [s.get("load1") for s in (load.get("before"), load.get("after"))
                 if isinstance(s, dict) and isinstance(s.get("load1"),
                                                       (int, float))]
        if peaks and isinstance(limit, (int, float)) and verdict in \
                ("quiet", "loaded"):
            want_v = "loaded" if max(peaks) > limit else "quiet"
            if verdict != want_v:
                add(Problem(path, 1, "environment.load.verdict",
                            f"is {verdict!r} but the samples' peak load1 is "
                            f"{max(peaks)} against a limit of {limit}, which "
                            f"is {want_v!r}; the verdict is not the harness's "
                            f"opinion, it is what the numbers say", "X20"))

        # X24 / X25 the two numbers an engine cannot exceed
        for n, row in rows:
            if row.get("kind") != "match":
                continue
            offered = subj_bytes.get(row.get("subject_id"))
            if not isinstance(offered, int):
                continue
            timing = row.get("timing") or {}
            got = timing.get("bytes_processed")
            iters = timing.get("iterations")
            if isinstance(got, int) and isinstance(iters, int) and iters >= 1:
                ceiling = offered * iters
                if got > ceiling:
                    add(Problem(path, n, "timing.bytes_processed",
                                f"is {got} but the subject offers {offered} "
                                f"bytes and the loop ran {iters} times, so at "
                                f"most {ceiling} bytes can have been "
                                f"processed; this is the numerator of every "
                                f"throughput number in the cell", "X24"))
            consumed = row.get("consumed_length")
            outcome = row.get("match_outcome")
            if isinstance(consumed, int) and consumed > offered:
                add(Problem(path, n, "consumed_length",
                            f"is {consumed} but only {offered} bytes were "
                            f"offered; an engine cannot consume what it was "
                            f"not given", "X25"))
            if outcome == "truncated-subject":
                if not isinstance(consumed, int):
                    add(Problem(path, n, "consumed_length",
                                "the outcome is `truncated-subject` but no "
                                "consumed_length is recorded: the row asserts "
                                "a truncation and does not say where", "X25"))
                elif consumed >= offered:
                    add(Problem(path, n, "consumed_length",
                                f"the outcome is `truncated-subject` but "
                                f"{consumed} of {offered} offered bytes were "
                                f"consumed, which is not a truncation",
                                "X25"))

        # X21 the calibration actually met its target
        for n, row in rows:
            if row.get("kind") != "match":
                continue
            cal = row.get("calibration")
            if not isinstance(cal, dict):
                continue
            iters = (row.get("timing") or {}).get("iterations")
            probe_n = cal.get("probe_iterations")
            probe_ns = cal.get("probe_elapsed_ns")
            target = cal.get("target_ns")
            if not all(isinstance(x, int) for x in
                       (iters, probe_n, probe_ns, target)) or probe_n < 1 \
                    or iters < 1:
                # An iteration count below 1 is rejected by the schema
                # (`minimum: 1`); reporting a calibration failure on top of it
                # would make that control fail for two reasons.
                continue
            est = probe_ns / probe_n * iters
            if est < target and not cal.get("calibration_note"):
                add(Problem(path, n, "calibration",
                            f"the probe measured {probe_ns}ns over "
                            f"{probe_n} iterations, so {iters} iterations "
                            f"were predicted to take {est:.0f}ns against a "
                            f"target of {target}ns: the calibration did NOT "
                            f"meet its target and no calibration_note says "
                            f"why", "X21"))

        # X26 the occupancy verdict follows from its number and its threshold
        occ = env.get("occupancy", {}) or {}
        occ_limit = occ.get("limit_busy_pct")
        for when in ("before", "after"):
            sample = occ.get(when)
            if not isinstance(sample, dict):
                continue
            busy = sample.get("max_busy_pct")
            got_v = sample.get("verdict")
            if not isinstance(busy, (int, float)) or \
                    not isinstance(occ_limit, (int, float)):
                continue
            want_v = "pass" if busy <= occ_limit else "fail"
            if got_v != want_v:
                add(Problem(path, 1, f"environment.occupancy.{when}.verdict",
                            f"is {got_v!r} but the busiest non-target core "
                            f"was {busy}% against a limit of {occ_limit}%, "
                            f"which is {want_v!r}", "X26"))

        # X13 / X14 the record-status gates. X13 is VERSIONED (the note 4's
        # rule-revision clause, v1.4): a record is judged by the text of its
        # own schema_version -- older records keep the verdict of their day.
        v14 = f_minor is not None and f_minor >= X13_V14_MINOR
        ta = setup.get("trial_agreement")
        pin_cpu = (env.get("pinning") or {}).get("cpu")
        if setup.get("status") == "measured" and not v14:
            if load.get("verdict") != "quiet":
                add(Problem(path, 1, "status",
                            "is `measured` but environment.load.verdict is not "
                            "`quiet`; a load-compromised record is "
                            "`inconclusive-load`", "X13"))
            for when in ("before", "after"):
                got_v = (occ.get(when) or {}).get("verdict")
                if got_v != "pass":
                    add(Problem(path, 1, "status",
                                f"is `measured` but the per-core occupancy "
                                f"check {when} the run is {got_v!r}, not "
                                f"`pass`; only a passing occupancy check on "
                                f"BOTH samples supports `measured` "
                                f"(the v1.1 ruling, §9)", "X13"))
        if setup.get("status") == "measured" and v14:
            # v1.4 (gate_shape_v14.md 2): the PRE-FLIGHT plus trial
            # agreement. The after samples are provenance and never
            # disqualify; `load.verdict` stays X20's either-sample fact.
            before = load.get("before") if isinstance(load.get("before"), dict) else {}
            l1 = before.get("load1")
            if isinstance(l1, (int, float)) and isinstance(limit, (int, float)) \
                    and l1 > limit:
                add(Problem(path, 1, "status",
                            f"is `measured` but load.before.load1 {l1} exceeds "
                            f"the limit {limit}: the pre-flight's load clause "
                            f"failed (v1.4 X13 clause 1)", "X13"))
            ob = occ.get("before") if isinstance(occ.get("before"), dict) else {}
            if ob.get("verdict") != "pass":
                add(Problem(path, 1, "status",
                            f"is `measured` but the per-core occupancy check "
                            f"BEFORE the run is {ob.get('verdict')!r}, not "
                            f"`pass` (v1.4 X13 clause 2; `unavailable` is "
                            f"still not `measured`, the v1.1 ruling on the "
                            f"pre-flight sample)", "X13"))
            if isinstance(pin_cpu, int) and not isinstance(pin_cpu, bool):
                tb = ob.get("target_busy_pct", None)
                if "target_busy_pct" not in ob:
                    add(Problem(path, 1, "environment.occupancy.before.target_busy_pct",
                                f"is ABSENT but pinning.cpu is {pin_cpu}: a "
                                f"`measured` record on a pinned run must "
                                f"carry the target core's own reading "
                                f"(v1.4 X13 clause 3)", "X13"))
                elif not isinstance(tb, (int, float)) or isinstance(tb, bool):
                    add(Problem(path, 1, "environment.occupancy.before.target_busy_pct",
                                f"is {tb!r} beside status `measured` and "
                                f"pinning.cpu {pin_cpu}: the target core's "
                                f"row was not in the capture, which is the "
                                f"same unknown as `unavailable` (v1.4 X13 "
                                f"clause 3)", "X13"))
                elif isinstance(occ_limit, (int, float)) and tb > occ_limit:
                    add(Problem(path, 1, "environment.occupancy.before.target_busy_pct",
                                f"is {tb}% beside status `measured` against a "
                                f"limit of {occ_limit}%: the TARGET core "
                                f"cpu{pin_cpu} was busy before the run -- a "
                                f"competitor pinned where this cell was "
                                f"measured sits under every trial (v1.4 X13 "
                                f"clause 3)", "X13"))
            if isinstance(ta, dict):
                verdict_ta = ta.get("verdict")
                if tier == "scratch":
                    if verdict_ta == "disagree":
                        add(Problem(path, 1, "status",
                                    "is `measured` but trial_agreement.verdict "
                                    "is `disagree` (v1.4 X13 clause 4, scratch "
                                    "tier: a disagreeing record is "
                                    "`inconclusive-spread`)", "X13"))
                elif verdict_ta != "agree":
                    add(Problem(path, 1, "status",
                                f"is `measured` but trial_agreement.verdict is "
                                f"{verdict_ta!r} on a pinned record (v1.4 X13 "
                                f"clause 4: `agree` is required -- a pinned "
                                f"record that disagrees, or lacks the five odd "
                                f"trials the rule needs, is "
                                f"`inconclusive-spread`)", "X13"))
            # an ABSENT block on a 1.4 record is X33's finding, not X13's
        if setup.get("status") == "measured":
            # The PLAIN artifact is what every pattern must have; the
            # whole-subject one exists only for a testee that needs it.
            missing = sorted(x for x in pat_ids
                             if (x, DEFAULT_FORM) not in seen_compile)
            if missing:
                add(Problem(path, 1, "status",
                            f"is `measured` but patterns {missing} have no "
                            f"`plain` compile row; a record that stopped "
                            f"halfway is `harness-failure`", "X14"))

        # X33 the trial-agreement block is present iff the record is >= 1.4
        if f_minor is not None:
            if v14 and not isinstance(ta, dict):
                add(Problem(path, 1, "trial_agreement",
                            f"is absent on a record stamped {sv}: at schema "
                            f"1.4 every record carries the trial-agreement "
                            f"block, pinned or scratch, whatever its trial "
                            f"count (X33; gate_shape_v14.md 3.3)", "X33"))
            if not v14 and ta is not None:
                add(Problem(path, 1, "trial_agreement",
                            f"is present on a record stamped {sv}, before the "
                            f"version that defined it (1.4): a mis-stamped "
                            f"record, not a forward-compatible one (X33)",
                            "X33"))

        # X31 / X32 the block's verdict follows from its counts, and the
        # counts follow from the rows (this file's own recomputation)
        if isinstance(ta, dict):
            want_v = expected_verdict(ta)
            if ta.get("verdict") != want_v:
                add(Problem(path, 1, "trial_agreement.verdict",
                            f"is {ta.get('verdict')!r} but the block's own "
                            f"counts (trials {ta.get('trials')}, "
                            f"groups_disagreeing {ta.get('groups_disagreeing')}) "
                            f"require {want_v!r} (X31)", "X31"))
            k, d_min, share_c = ta.get("k"), ta.get("d_min"), ta.get("share_c")
            if isinstance(k, (int, float)) and isinstance(d_min, int) \
                    and isinstance(share_c, int) and k > 1 and d_min >= 1 \
                    and share_c >= 1:
                want = judge_trial_agreement([r for _n, r in rows], k, d_min, share_c)
                for fld in ("trials", "groups_judged", "groups_disagreeing",
                            "rows_judged", "rows_disagreeing", "rows_unjudged"):
                    if ta.get(fld) != want[fld]:
                        add(Problem(path, 1, f"trial_agreement.{fld}",
                                    f"is {ta.get(fld)!r} but the record's own "
                                    f"match rows recompute to {want[fld]} under "
                                    f"gate_shape_v14.md 3.5 with k={k}, "
                                    f"d_min={d_min}, share_c={share_c} (X32)",
                                    "X32"))
                reasons = ta.get("rows_unjudged_reasons")
                if reasons != want["rows_unjudged_reasons"]:
                    add(Problem(path, 1, "trial_agreement.rows_unjudged_reasons",
                                f"is {reasons!r} but the rows recompute to "
                                f"{want['rows_unjudged_reasons']} (X32)", "X32"))
                wg = ta.get("worst_group")
                if wg != want["worst_group"]:
                    add(Problem(path, 1, "trial_agreement.worst_group",
                                f"is {wg!r} but the rows recompute to "
                                f"{want['worst_group']!r} (largest d, then "
                                f"smallest n, then lowest seq; X32)", "X32"))
                if isinstance(wg, dict):
                    if wg.get("pattern_id") not in pat_ids:
                        add(Problem(path, 1, "trial_agreement.worst_group.pattern_id",
                                    f"{wg.get('pattern_id')!r} is not in "
                                    f"setup.patterns[] (X32)", "X32"))
                    if wg.get("regime") not in regimes:
                        add(Problem(path, 1, "trial_agreement.worst_group.regime",
                                    f"{wg.get('regime')!r} is not among the "
                                    f"sub-bench's declared regimes (X32)", "X32"))
        return p

    @staticmethod
    def _check_trials(add, path, trials, what):
        for t, lines in sorted(trials.items()):
            if len(lines) > 1:
                add(Problem(path, lines[1], "trial",
                            f"trial {t} of the {what} appears {len(lines)} times "
                            f"(also on line {lines[0]})", "X9"))
        nums = sorted(trials)
        if nums != list(range(1, len(nums) + 1)):
            first = min(trials[nums[0]]) if nums else 0
            add(Problem(path, first, "trial",
                        f"the {what} have trials {nums}; they must be a dense "
                        f"1..N", "X9"))

    @staticmethod
    def _check_metadata(add, path, n, name, value, decl, kind):
        d = decl.get(name)
        field = f"engine_metadata.{name}"
        if d is None:
            add(Problem(path, n, field,
                        "is not declared in "
                        "setup.testee.engine_metadata_declaration; an "
                        "undeclared pair is free text and is not filterable",
                        "X15"))
            return
        want_scope = "match" if kind == "match" else "pattern"
        if d.get("scope") != want_scope:
            add(Problem(path, n, field,
                        f"is declared with scope {d.get('scope')!r} but appears "
                        f"on a {kind} row (scope {want_scope!r})", "X15"))
        t = d.get("type")
        if t == "integer" and not isinstance(value, int):
            add(Problem(path, n, field, f"declared `integer`, got {value!r}", "X15"))
        elif t == "string" and not isinstance(value, str):
            add(Problem(path, n, field, f"declared `string`, got {value!r}", "X15"))
        elif t == "enum":
            if not isinstance(value, str) or value not in (d.get("values") or []):
                add(Problem(path, n, field,
                            f"{value!r} is not one of the declared values "
                            f"{d.get('values')}", "X15"))
        elif t == "mask":
            if not isinstance(value, list):
                add(Problem(path, n, field,
                            "declared `mask`, whose value is an ARRAY of set bit "
                            "names (never the integer)", "X15"))
            else:
                unknown = [b for b in value if b not in (d.get("bits") or [])]
                if unknown:
                    add(Problem(path, n, field,
                                f"bits {unknown} are not among the declared bits "
                                f"{d.get('bits')}", "X15"))


def main(argv=None):
    ap = argparse.ArgumentParser(description="validate pcrec-bench record files")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--expect-reject", action="store_true",
                    help="exit 0 only if EVERY file is rejected (positive controls)")
    ap.add_argument("--expect-rule", metavar="RULE",
                    help="with --expect-reject: require RULE (X1..X33 or SCHEMA) "
                         "among the rules that fired. A positive control that "
                         "rejects for the WRONG reason proves nothing about the "
                         "rule it was written for")
    ap.add_argument("--check-filename", action="store_true",
                    help="also enforce X4: basename == <record_id>.jsonl")
    ap.add_argument("--allow-mixed-versions", action="store_true",
                    help="suppress X17 across the files given")
    ap.add_argument("--print-hash", action="store_true",
                    help="print the content hash the file's bytes imply, and exit")
    args = ap.parse_args(argv)

    schema = json.load(open(SCHEMA_PATH, encoding="utf-8"))

    if args.print_hash:
        for path in args.files:
            with open(path, encoding="utf-8") as fh:
                lines = fh.read().split("\n")
            while lines and lines[-1] == "":
                lines.pop()
            print(f"{path}\t{compute_content_hash(json.loads(lines[0]), lines[1:])}")
        return 0

    rv = RecordValidator(schema)
    versions = {}
    rejected = accepted = wrong_rule = 0
    for path in args.files:
        problems, sv = rv.validate_file(path, check_filename=args.check_filename)
        if sv:
            versions.setdefault(sv.split(".")[0], []).append(path)
        if problems:
            rejected += 1
            if not args.expect_reject:
                for pr in problems:
                    print(f"validate.py: {pr}", file=sys.stderr)
            else:
                fired = sorted({pr.rule for pr in problems if pr.rule})
                print(f"validate.py: REJECTED (as expected) {path}: "
                      f"{len(problems)} problem(s), rules {','.join(fired) or '-'}; "
                      f"first: {problems[0]}")
                if args.expect_rule and args.expect_rule not in fired:
                    print(f"validate.py: {path}: expected rule "
                          f"{args.expect_rule} to fire, but the rules that fired "
                          f"were {fired}", file=sys.stderr)
                    wrong_rule += 1
        else:
            accepted += 1
            if not args.expect_reject:
                print(f"validate.py: OK {path}")
            else:
                print(f"validate.py: ACCEPTED {path} -- but it is a positive "
                      f"control and MUST be rejected", file=sys.stderr)

    # X17: mixing across the files given to one invocation.
    if len(versions) > 1 and not args.allow_mixed_versions and not args.expect_reject:
        detail = "; ".join(f"{maj}.x: {', '.join(os.path.basename(f) for f in fs)}"
                           for maj, fs in sorted(versions.items()))
        print(f"validate.py: X17: these files mix major schema versions and no "
              f"migration is declared ({detail})", file=sys.stderr)
        return 1

    if args.expect_reject:
        print(f"validate.py: {rejected} rejected, {accepted} wrongly accepted, "
              f"{wrong_rule} rejected for the wrong reason")
        return 0 if (accepted == 0 and wrong_rule == 0) else 1
    print(f"validate.py: {accepted} valid, {rejected} invalid")
    return 0 if rejected == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
