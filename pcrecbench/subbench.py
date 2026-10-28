"""subbench.py -- load a `bench/<name>/` directory (harness contract 2).

Reads the sidecar with stdlib `tomllib`, the pattern files as RAW BYTES, the
committed manifests, and `expectations.tsv`; resolves the REGIME -> SUBJECT
mapping the contract fixes; and computes the `subbench.content_hash` the
record carries.

THE TWO REGIME SPELLINGS. The sub-bench directory and the CLI speak the
contract's short names (`match`, `search_short`, `throughput`); the RECORD
speaks record_schema.md 5's enum (`match-compliance`, `short-subject-search`,
`large-subject-throughput`). Both spellings are real and neither is wrong --
the contract fixed one, the schema the other -- so the mapping lives HERE,
once, and `REGIME_TO_ENUM` is the only place either name is translated.
"""

import hashlib
import json
import os
import re
import tomllib

REGIME_TO_ENUM = {
    "match": "match-compliance",
    "search_short": "short-subject-search",
    "throughput": "large-subject-throughput",
    # v1.9 ([B140]): the TRANSFORM regime -- a pattern + template applied to
    # a subject, the OUTPUT being the answer (subst_bench_v1.md 5 S1).
    "substitution": "substitution",
    # v1.11 ([B148] L1, unusual_set_v1.md 7.1): the CALL-STREAM regime -- a
    # declared call list over one subject, one timed iteration = one full
    # replay. The schema and the sidecar spelling exist from L1; the driver
    # plumbing (`--mode calls`, 7.3) is lane L4's: the subjects are the set's
    # `[subjects] stream_manifest` rows (`Subject.calls_path` set), the
    # expectations its `[expectations] stream_file` rows (StreamExpectation).
    "call-stream": "call-stream",
}
ENUM_TO_REGIME = {v: k for k, v in REGIME_TO_ENUM.items()}

# The regime's MATCH SEMANTICS (contract 2). `match` is anchored + end-
# anchored over the whole subject; the other two are unanchored SEARCH.
REGIME_MODE = {
    "match": "match",
    "search_short": "search",
    "throughput": "search",
    "substitution": "subst",
    "call-stream": "calls",
}

# Files under bench/<name>/ that are GENERATED, and so are excluded from the
# content hash: hashing them would make the hash depend on whether a
# regenerable tree happened to be present.
#
# [B148] L4: `streams/` and `calls/` (bench/unusual's F1 call-stream subjects
# and their call lists, gen_streams.py) are generated too and hashed through
# manifest_streams.tsv (subject sha256 + calls_sha256), exactly as
# `subjects/` is through manifest.tsv. No other set has a directory by either
# name, so no other set's content hash moves.
GENERATED_DIRS = ("subjects", "throughput", "streams", "calls", "__pycache__")


class SubbenchError(Exception):
    pass


# THE ID RULE, READ FROM THE SCHEMA -- NEVER RETYPED (KB-12). The record
# schema's `pattern_id`/`subject_id` properties both `$ref` `#/$defs/slug`
# (schema/record.schema.json): `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`, lowercase
# only. A set with an uppercase id (bench/syntax@0.1's incident: ten pattern
# ids and two subject ids, [B36]) is refused by `schema/validate.py` at
# WRITE time -- after every trial of every cell has already run. This module
# checks every id the sidecar and manifests declare BEFORE any of that, so
# `pcrecbench run`/`quick` refuse in under a second. The regex is fetched
# from the schema file itself so the rule can never drift from what
# `validate.py` actually enforces; an unreadable schema file is a loud
# failure, not a silent skip.
_SCHEMA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "schema", "record.schema.json")
_SLUG_DEF = "$defs/slug"
_slug_re = None


def _slug_pattern():
    global _slug_re
    if _slug_re is None:
        try:
            with open(_SCHEMA_PATH, "r", encoding="utf-8") as f:
                schema = json.load(f)
            pattern = schema["$defs"]["slug"]["pattern"]
        except Exception as e:
            raise SubbenchError(
                "cannot read the record schema's id rule from %s (%s): %s"
                % (_SCHEMA_PATH, _SLUG_DEF, e))
        _slug_re = re.compile(pattern)
    return _slug_re


def check_id(kind, value, set_id):
    """Refuse `value` (a pattern or subject id) unless it matches the record
    schema's slug rule. Raises SubbenchError naming the id, the set and the
    rule -- never silently accepts and never retypes the regex."""
    rx = _slug_pattern()
    if not rx.fullmatch(value):
        raise SubbenchError(
            "id %r violates the record schema's id rule %s "
            "(schema/record.schema.json %s): lowercase letters, digits, "
            "single hyphens (set %s, %s id)"
            % (value, rx.pattern, _SLUG_DEF, set_id, kind))


class Pattern:
    __slots__ = ("name", "file", "text", "feature_tier", "hazard_class",
                 "size_class", "convention", "tags", "role",
                 "case", "template_file")

    def __init__(self, d):
        for k in self.__slots__:
            setattr(self, k, d.get(k))
        self.tags = list(d.get("tags") or [])
        # record_schema.md 5 (v1.3, [B15]): `role` is `member` unless the
        # sidecar says `floor` -- the ONE per-call baseline pattern a set may
        # declare. Defaulting here, not in the record, means an old sidecar
        # with no `role` key loads exactly as it always did.
        self.role = self.role or "member"
        for req in ("name", "hazard_class", "size_class"):
            if not getattr(self, req):
                raise SubbenchError("pattern entry is missing %r: %r" % (req, d))
        # [B42] L4: a pattern's bytes come from EITHER a sidecar `file`
        # (the original per-pattern-.rx-file shape) OR inline `text` (an
        # `.rxt`-sourced pattern, `rxt_source.build_pattern_dicts`'s own
        # decoded bytes) -- never neither. `text is None` is the "absent"
        # test, not `not self.text`: an empty pattern body (`b""`) is a
        # legal, if odd, pattern and must not be mistaken for "no text".
        if not self.file and self.text is None:
            raise SubbenchError(
                "pattern entry %r has neither `file` nor inline `text` -- "
                "one pattern-bytes source is required" % d.get("name"))


# [B148] L1 (unusual_set_v1.md 2, 3.2): THE `twin_of` PATTERN TAG. A callout
# member is three patterns -- `<id>-twin` (the site removed), `<id>-pass`
# (the site present, a stub callee) and `<id>` (the real callee) -- linked by
# `tag twin_of=<id>` (an `.rxt` `key=value` tag, flattened like every other
# to `twin_of-<id>`; a sidecar writes the flat spelling directly). The tag's
# VALUE is a pattern id, so no `vocabulary` line can close it: its rule is
# checked here instead, at load -- at most one per pattern, it names a
# pattern of the same set, and the pattern it names is the group's ROOT (it
# carries no `twin_of`, or `twin_of` itself). Readers: `twin_groups` below
# (the set-sidecar cost split and `tools/check_unusual.py`'s pass == twin
# gate, unusual_set_v1.md 3.2 / S-12).
TWIN_OF_TAG = "twin_of"
_TWIN_OF_PREFIX = TWIN_OF_TAG + "-"


def twin_of(pattern):
    """-> the `twin_of` value of `pattern` (a pattern id), or None."""
    vals = [t[len(_TWIN_OF_PREFIX):] for t in pattern.tags or ()
            if t.startswith(_TWIN_OF_PREFIX)]
    if len(vals) > 1:
        raise SubbenchError("pattern %r carries %d twin_of tags %r; at most one"
                            % (pattern.name, len(vals), vals))
    return vals[0] if vals else None


def twin_groups(patterns, set_id):
    """-> `{root_id: [member ids, in set order]}` over every pattern that
    carries `twin_of` (the root included when it names itself). Raises
    SubbenchError naming the pattern when a value names no pattern of the
    set, or names a pattern that is itself linked to a third."""
    by_id = {p.name: p for p in patterns}
    groups = {}
    for p in patterns:
        root = twin_of(p)
        if root is None:
            continue
        if root not in by_id:
            raise SubbenchError("%s: pattern %r: twin_of=%s names no pattern "
                                "of the set" % (set_id, p.name, root))
        rr = twin_of(by_id[root])
        if rr not in (None, root):
            raise SubbenchError("%s: pattern %r: twin_of=%s, but %r is itself "
                                "twin_of=%s -- a twin group has ONE root"
                                % (set_id, p.name, root, root, rr))
        groups.setdefault(root, []).append(p.name)
    return groups


# [B42] L4: DEFAULT size_class FOR AN `.rxt`-SOURCED PATTERN. Required by
# the record schema (`hazard_class`/`size_class` are both REQUIRED,
# schema/record.schema.json:298) but carried by no `.rxt` production today
# (rxt_needs_v1.md's need table has no size-class equivalent) -- a
# LOADER-SIDE default, not an `.rxt` fact, matching what bench/capability's
# own gen_patterns.py already derives for every one of its 64 patterns
# (`subbench.toml`'s committed `[[patterns]]` shim: `size_class = "small"`
# throughout, since v1's subjects are all typed-short + a throughput sweep,
# never a per-pattern size axis). Named as a constant here so the day a
# set wants a REAL per-pattern size class, this is the one place that
# changes.
_RXT_DEFAULT_SIZE_CLASS = "small"
_RXT_DEFAULT_FEATURE_TIER = "base"


def _pattern_dict_from_rxt(p, rxt):
    """`rxt_source.RxtSource.patterns[i]` (one block's dict) -> the dict
    shape `Pattern.__init__` expects. `hazard_class` comes straight from
    the block's own `tag hazard=...` (the record schema's enum is a
    SUBSET of this set's declared `vocabulary hazard` list, so a value
    the vocabulary accepted is always schema-legal); `role` is `floor`
    iff the block's `family` tag says so (the vocabulary's own `floor`
    value exists for exactly this, `capability_set_v1.md` 3.3);
    `convention` is the block's own tag if declared, else left unset (no
    bench-side default invented -- unlike `size_class`/`feature_tier`,
    every pattern that CARES about its convention declares one)."""
    tags = p["tags"]
    hazards = tags.get("hazard") or []
    if not hazards:
        raise SubbenchError(
            "%s: pattern block %r (line %s) carries no `tag hazard=...` "
            "-- required by the record schema's hazard_class field"
            % (rxt.path, p["name"], p["block_line"]))
    families = tags.get("family") or []
    conventions = tags.get("convention") or []
    flat_tags = list(tags.get("_labels") or [])
    for k, values in tags.items():
        if k == "_labels":
            continue
        flat_tags.extend("%s-%s" % (k, v) for v in values)
    prov = rxt.provenance_for(p["block_line"])
    if prov:
        if prov.get("source"):
            flat_tags.append("provenance-%s" % prov["source"])
        if prov.get("fidelity"):
            flat_tags.append("fidelity-%s" % prov["fidelity"])
    return {
        "name": p["name"],
        "file": None,
        "text": p["text"],
        "feature_tier": _RXT_DEFAULT_FEATURE_TIER,
        "hazard_class": hazards[0],
        "size_class": _RXT_DEFAULT_SIZE_CLASS,
        "convention": conventions[0] if conventions else None,
        "tags": flat_tags,
        "role": "floor" if "floor" in families else "member",
    }


class Subject:
    __slots__ = ("subject_id", "length", "sha256", "description", "periodic",
                 "path", "kind", "calls_path", "calls", "segment_bytes",
                 "calls_sha256")

    def __init__(self, subject_id, length, sha, desc, periodic, path, kind):
        self.subject_id, self.length, self.sha256 = subject_id, int(length), sha
        self.description, self.path, self.kind = desc, path, kind
        # [B17]/I-10: the smallest period in bytes (see bench/email/
        # periodic.py), as a decimal STRING, `"no"`, or None if this
        # manifest predates the column -- a 4-column manifest still loads.
        self.periodic = periodic
        # [B148] L4: a CALL-STREAM subject (kind "stream") also names its
        # call list and the manifest's two denominators; None on every other.
        self.calls_path = self.calls = self.segment_bytes = None
        self.calls_sha256 = None


class StreamExpectation:
    """One `expectations_stream.tsv` row (bench/unusual/gen_expectations.py):
    the per-stream counts and the hash of the per-call result tokens."""
    __slots__ = ("subject", "pattern", "calls", "matched", "nomatch",
                 "refused", "results_sha256", "method")

    def __init__(self, cols):
        (self.subject, self.pattern, calls, matched, nomatch, refused,
         self.results_sha256, self.method) = cols
        self.calls, self.matched = int(calls), int(matched)
        self.nomatch, self.refused = int(nomatch), int(refused)


class Expectation:
    __slots__ = ("pattern", "subject", "regime", "expected", "start", "end",
                 "nmatches", "method", "oracle", "convention")

    def __init__(self, cols):
        (self.pattern, self.subject, self.regime, self.expected, start, end,
         n, self.method, self.oracle) = cols
        self.start = None if start == "-" else int(start)
        self.end = None if end == "-" else int(end)
        self.nmatches = None if n == "-" else int(n)
        # R5 B1 / CB1 ([B42] L5, docs/design/capability_set_v1.md 5.6):
        # which CONVENTION this row's answer was authored under; `None`
        # means "the shared canonical answer, correct for every testee"
        # -- the ONLY value the 9-column `expectations.tsv` FORMAT can
        # produce (this constructor never receives a tenth column), so
        # every real row loads with `.convention is None`. An `under
        # <convention>`-qualified row is UNAUTHORED in any committed set
        # (bench/capability/NOTES.md's own stated deferral) -- when one
        # exists, its own loader sets this attribute directly, the same
        # way `harness.outcome_for`'s `convention` parameter is built to
        # read it (a fixture-only path today, see that function's own
        # docstring).
        self.convention = None

    @property
    def matched(self):
        return self.expected == "match"


# [B125]: the closed set of `[expectations] fallback_methods` members. The
# method's logic lives in expectations.py; the NAME lives here so the loader
# (which every harness run imports) never has to import the libpcre2 binding.
FALLBACK_METHODS = ("structural-alphabet", "libpcre2-dfa-fallback")

# [B77] U1: the closed set of `[expectations] encoding` values, spelled as
# pcrec spells its own `-e` values.
SET_ENCODINGS = ("byte", "utf8")


#: The sidecar's file name. The substitution set staged its sidecar as
#: `subst.toml` until [B143] (plan [B140] step 5) renamed it; only
#: `subbench.toml` is accepted now, so the generic enumerations (selfcheck's
#: `subbench_dirs()`, the reporter's set-id lookup, the importer) and the
#: loader agree on what a set is.
SIDECAR_NAMES = ("subbench.toml",)


class Subbench:
    def __init__(self, root):
        self.root = os.path.abspath(root)
        sidecar = None
        for nm in SIDECAR_NAMES:
            cand = os.path.join(self.root, nm)
            if os.path.exists(cand):
                sidecar = cand
                break
        if sidecar is None:
            raise SubbenchError("no subbench.toml in %s" % self.root)
        with open(sidecar, "rb") as f:
            self.cfg = tomllib.load(f)

        self.id = self.cfg["id"]
        self.version = str(self.cfg["version"])
        self.objective = self.cfg["objective"]
        self.objective_kind = self.cfg["objective_kind"]
        self.description = self.cfg.get("description", "")
        self.regimes = list(self.cfg["regimes"])
        unknown = [r for r in self.regimes if r not in REGIME_TO_ENUM]
        if unknown:
            raise SubbenchError("unknown regime(s) %r in %s" % (unknown, sidecar))
        # [B42] L4: `rxt_source = "<relative path>"` is the ONE sidecar key
        # that switches a set from the TOML `[[patterns]]` array to an
        # `.rxt` pattern source, loaded through `pcrecbench.rxt_source`'s
        # ONE sanctioned reader (`pcrec --list-source`, never a second
        # `.rxt` parser). Present, `[[patterns]]` is ignored outright --
        # a set does not need to delete a stale array to switch (this is
        # the ONE-LINE toggle a manager merge applies); absent, loading is
        # byte-for-byte what it always was.
        self.rxt = None
        rxt_rel = self.cfg.get("rxt_source")
        if rxt_rel:
            from pcrecbench import rxt_source as _rxt
            rxt_path = os.path.join(self.root, rxt_rel)
            try:
                self.rxt = _rxt.load_rxt_source(rxt_path)
            except _rxt.RxtSourceError as e:
                raise SubbenchError("%s: rxt_source=%r: %s"
                                    % (sidecar, rxt_rel, e))
            self.patterns = [Pattern(_pattern_dict_from_rxt(p, self.rxt))
                             for p in self.rxt.patterns]
        elif "cases" in self.cfg:
            # [B140] a SUBSTITUTION set: its "patterns" are the CASES
            # (cases.tsv x cases/<dir>/PATTERN.rx + TEMPLATE.neutral).
            self.patterns = [Pattern(d) for d in self._case_pattern_dicts()]
        else:
            self.patterns = [Pattern(p) for p in self.cfg.get("patterns", [])]
        if not self.patterns:
            raise SubbenchError("%s declares no patterns" % sidecar)
        for p in self.patterns:
            check_id("pattern", p.name, self.id)
        self.twin_groups = twin_groups(self.patterns, self.id)
        self.testee_notes = self.cfg.get("testees", {})

        subj = self.cfg.get("subjects", {})
        self.short_search_max = int(subj.get("short_search_max_bytes", 256))
        self.substitution = "substitution" in self.regimes
        if self.substitution:
            self._short = self._load_manifest(
                subj.get("manifest", "manifest.tsv"), "subjects", "subst",
                ext=".log", dirname=subst_subjects_dir(self.root))
        else:
            self._short = self._load_manifest(
                subj.get("manifest", "manifest.tsv"), "subjects", "short")
        tman = subj.get("throughput_manifest")
        self._throughput = (self._load_manifest(tman, "throughput", "throughput")
                            if tman else [])
        # [B148] L4: the CALL-STREAM subjects (unusual_set_v1.md 4.1, 7.1).
        sman = subj.get("stream_manifest")
        self._streams = self._load_stream_manifest(sman) if sman else []
        for s in self._short + self._throughput + self._streams:
            check_id("subject", s.subject_id, self.id)
        # [B148] L4: APPLICABILITY (bench/unusual/applies.tsv): which large
        # subjects a pattern is measured on, per regime. Absent (every other
        # set), every subject of a regime applies to every pattern.
        app = subj.get("applies")
        self._applies = self._load_applies(app) if app else None

        exp = self.cfg.get("expectations", {})
        self.expectation_file = exp.get("file", "expectations.tsv")
        self.stream_expectation_file = exp.get("stream_file")   # [B148] L4
        self._stream_expectations = None
        self.default_method = exp.get("default_method", "")
        # [B125]: the OPTIONAL second verification method, used only for a
        # triple the backtracker gave up on (expectations.py). Absent -> ""
        # and the set is derived exactly as before.
        # `fallback_methods` is the ORDERED precedence list (first applicable
        # wins), each from FALLBACK_METHODS; empty -> the old behaviour.
        self.fallback_methods = tuple(exp.get("fallback_methods", ()))
        for m in self.fallback_methods:
            if m not in FALLBACK_METHODS:
                raise SubbenchError(
                    "%s: [expectations] fallback_methods has %r; expected "
                    "members of %s" % (sidecar, m, ", ".join(FALLBACK_METHODS)))
        # [B77] U1 (docs/design/utf8_set_v1.md 8.1): the SET's encoding --
        # `[expectations] encoding = "utf8"` puts PCRE2_UTF in the oracle
        # option word of EVERY pattern (never per subject or per regime:
        # one definition of "correct" per expectations.tsv), and the SAME
        # fact tells every driver to use the character-boundary find-all
        # advance (`expectations.oracle_option_word`, `harness.run_cell`).
        # Absent -> "byte", which is what every pre-utf8 set is.
        self.encoding = exp.get("encoding", "byte")
        if self.encoding not in SET_ENCODINGS:
            raise SubbenchError(
                "%s: [expectations] encoding = %r; expected one of %s"
                % (sidecar, self.encoding, ", ".join(SET_ENCODINGS)))
        # LAZY: gen_expectations.py loads the sub-bench in order to WRITE this
        # file, so construction must not require it to exist yet.
        self._expectations = None

    # ------------------------------------------------------------- loading

    def _load_manifest(self, name, subdir, kind, ext=".bin", dirname=None):
        path = os.path.join(self.root, name)
        if not os.path.exists(path):
            raise SubbenchError("manifest %s is missing" % path)
        out = []
        with open(path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                line = line.rstrip("\n")
                if not line:
                    continue
                if i == 0 and line.startswith("id\t"):
                    continue
                # GENERIC on column count: 4 columns is the original shape
                # (id, len, sha256, description); 5 adds `periodic`
                # ([B17]/I-10). No position is hard-coded beyond "periodic,
                # if present, is the 5th and last column" -- a manifest
                # with neither more nor fewer is rejected rather than
                # silently mis-parsed.
                cols = line.split("\t")
                if len(cols) not in (4, 5):
                    raise SubbenchError(
                        "%s:%d: expected 4 columns (id, len, sha256, "
                        "description) or 5 (+ periodic), got %d"
                        % (path, i + 1, len(cols)))
                sid, length, sha, desc = cols[:4]
                periodic = cols[4] if len(cols) == 5 else None
                out.append(Subject(sid, length, sha, desc, periodic,
                                   os.path.join(dirname or
                                                os.path.join(self.root, subdir),
                                                sid + ext),
                                   kind))
        return out

    def _load_stream_manifest(self, name):
        """[B148] L4: `id len sha256 description periodic calls segment_bytes
        calls_sha256 local_refusals` (bench/unusual/gen_streams.py); the
        subject is streams/<id>.bin and its call list calls/<id>.tsv."""
        path = os.path.join(self.root, name)
        if not os.path.exists(path):
            raise SubbenchError("stream manifest %s is missing" % path)
        out = []
        with open(path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                line = line.rstrip("\n")
                if not line or (i == 0 and line.startswith("id\t")):
                    continue
                cols = line.split("\t")
                if len(cols) != 9:
                    raise SubbenchError("%s:%d: expected 9 columns, got %d"
                                        % (path, i + 1, len(cols)))
                s = Subject(cols[0], cols[1], cols[2], cols[3], cols[4],
                            os.path.join(self.root, "streams", cols[0] + ".bin"),
                            "stream")
                s.calls, s.segment_bytes = int(cols[5]), int(cols[6])
                s.calls_sha256 = cols[7]
                s.calls_path = os.path.join(self.root, "calls", cols[0] + ".tsv")
                out.append(s)
        return out

    def _load_applies(self, name):
        """[B148] L4: `pattern regime subject_glob` -> {(pattern, regime):
        [glob, ...]} (a glob cell is space-separated fnmatch patterns)."""
        path = os.path.join(self.root, name)
        if not os.path.exists(path):
            raise SubbenchError("applies table %s is missing" % path)
        out = {}
        with open(path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                line = line.rstrip("\n")
                if not line or (i == 0 and line.startswith("pattern\t")):
                    continue
                cols = line.split("\t")
                if len(cols) != 3:
                    raise SubbenchError("%s:%d: expected 3 columns, got %d"
                                        % (path, i + 1, len(cols)))
                out.setdefault((cols[0], cols[1]), []).extend(cols[2].split())
        return out

    def applies(self, pattern, regime, subject_id):
        """Does (pattern, regime, subject) belong to the set's cross product?
        True everywhere on a set with no applies table. A call-stream subject
        applies iff the set states a stream expectation for the pair (the
        stream expectations ARE that set's applicability for the regime)."""
        if regime == "call-stream":
            return self.stream_expectation(pattern, subject_id) is not None
        if self._applies is None:
            return True
        import fnmatch
        globs = self._applies.get((pattern, regime))
        if globs is None:
            return False
        return any(fnmatch.fnmatchcase(subject_id, g) for g in globs)

    def stream_expectation(self, pattern, subject_id):
        """[B148] L4: the StreamExpectation for (pattern, stream) or None."""
        if self._stream_expectations is None:
            self._stream_expectations = {}
            if self.stream_expectation_file:
                path = os.path.join(self.root, self.stream_expectation_file)
                if not os.path.exists(path):
                    raise SubbenchError("stream expectations %s are missing"
                                        % path)
                with open(path, "r", encoding="utf-8") as f:
                    for i, line in enumerate(f):
                        line = line.rstrip("\n")
                        if not line or (i == 0 and line.startswith("subject\t")):
                            continue
                        cols = line.split("\t")
                        if len(cols) != 8:
                            raise SubbenchError(
                                "%s:%d: expected 8 columns, got %d"
                                % (path, i + 1, len(cols)))
                        e = StreamExpectation(cols)
                        self._stream_expectations[(e.pattern, e.subject)] = e
        return self._stream_expectations.get((pattern, subject_id))

    def _load_expectations(self):
        path = os.path.join(self.root, self.expectation_file)
        if not os.path.exists(path):
            raise SubbenchError("expectations %s are missing -- run "
                                "gen_expectations.py" % path)
        out = {}
        with open(path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                line = line.rstrip("\n")
                if not line or (i == 0 and line.startswith("pattern\t")):
                    continue
                cols = line.split("\t")
                if len(cols) != 9:
                    raise SubbenchError("%s:%d: expected 9 columns, got %d"
                                        % (path, i + 1, len(cols)))
                e = Expectation(cols)
                out[(e.pattern, e.subject, e.regime)] = e
        return out

    # ------------------------------------------------------------ accessors

    def pattern(self, name):
        for p in self.patterns:
            if p.name == name:
                return p
        raise SubbenchError("no pattern %r in %s" % (name, self.id))

    def pattern_bytes(self, name):
        """The canonical pattern as RAW BYTES -- never decoded and re-encoded:
        the specimen's classes carry bytes that are not valid UTF-8 text.
        [B42] L4: an `.rxt`-sourced pattern carries its bytes INLINE
        (`Pattern.text`, already decoded by `rxt_source.py` from
        `--list-source`'s own dump) -- no file to open at all."""
        p = self.pattern(name)
        if p.text is not None:
            return p.text
        with open(os.path.join(self.root, p.file), "rb") as f:
            data = f.read()
        if p.case is not None:
            # [B140] a case's PATTERN.rx is exactly one line and its newline
            # is the FILE's, not the pattern's (gen_expectations.py strips it
            # the same way): the oracle's expectations were derived without it.
            if not data.endswith(b"\n") or data.count(b"\n") != 1:
                raise SubbenchError("%s: PATTERN.rx must be exactly one line"
                                    % p.file)
            data = data[:-1]
        return data

    # ------------------------------------------- the substitution set ([B140])

    def _case_pattern_dicts(self):
        """cases.tsv -> the dicts `Pattern` wants, one per case. The pattern
        id is the case's DIRECTORY name (`5b-mask-email`: a schema slug);
        the case id (`5b`, the key of expectations.tsv and divergences.tsv and
        the record's `subst.case`) rides in `Pattern.case`."""
        cs = self.cfg["cases"]
        path = os.path.join(self.root, cs["table"])
        out = []
        with open(path, "r", encoding="utf-8") as f:
            rows = [l.rstrip("\n").split("\t") for l in f if l.strip()]
        head = rows[0]
        for r in rows[1:]:
            row = dict(zip(head, r))
            d = os.path.join(cs.get("dir", "cases"), row["dir"])
            out.append({
                "name": row["dir"], "file": os.path.join(d, "PATTERN.rx"),
                "template_file": os.path.join(d, "TEMPLATE.neutral"),
                "case": row["case"], "feature_tier": "base",
                "hazard_class": "none", "size_class": "tiny",
                "tags": ["case-" + row["case"], "label-" + row["label"],
                         "density-" + row["density"]],
            })
        return out

    def template_bytes(self, name):
        """The case's neutral template (the IR source), RAW BYTES."""
        p = self.pattern(name)
        if p.template_file is None:
            raise SubbenchError("%s: pattern %r is not a substitution case"
                                % (self.id, name))
        with open(os.path.join(self.root, p.template_file), "rb") as f:
            return f.read()

    def subst_expectation(self, case, subject_id):
        """-> {nsubst, out_bytes, out_sha256} for (case id, subject id) from
        the set's 8-column expectations.tsv, or None."""
        if getattr(self, "_subst_exp", None) is None:
            path = os.path.join(self.root, self.cfg["expectations"]["file"])
            exp = {}
            with open(path, "r", encoding="utf-8") as f:
                head = None
                for line in f:
                    cols = line.rstrip("\n").split("\t")
                    if head is None:
                        head = cols
                        continue
                    if len(cols) != len(head):
                        raise SubbenchError("%s: expected %d columns, got %d"
                                            % (path, len(head), len(cols)))
                    row = dict(zip(head, cols))
                    exp[(row["case"], row["subject"])] = {
                        "nsubst": int(row["nsubst"]),
                        "out_bytes": int(row["out_bytes"]),
                        "out_sha256": row["out_sha256"]}
            self._subst_exp = exp
        return self._subst_exp.get((case, subject_id))

    def divergence(self, case, *competitors):
        """-> (expectation, reason, basis, row_text) of the FIRST
        divergences.tsv row for `case` whose competitor is one of
        `competitors`, in order, then the `*` row; or None. The row_text is
        the citation a record's `declaration_ref` carries."""
        if getattr(self, "_div", None) is None:
            path = os.path.join(self.root,
                                self.cfg["cases"].get("divergences",
                                                      "divergences.tsv"))
            rows = {}
            with open(path, "r", encoding="utf-8") as f:
                next(f)
                for line in f:
                    cols = line.rstrip("\n").split("\t")
                    if len(cols) >= 5:
                        rows[(cols[0], cols[1])] = tuple(cols[2:5])
            self._div = rows
        for who in tuple(competitors) + ("*",):
            hit = self._div.get((case, who))
            if hit:
                return hit + ("bench/%s/divergences.tsv: case %s, %s (%s)"
                              % (os.path.basename(self.root), case, who,
                                 hit[0]),)
        return None

    def subject_bytes(self, subject_id):
        with open(self.subject(subject_id).path, "rb") as f:
            return f.read()

    def subject(self, subject_id):
        for s in self._short + self._throughput + self._streams:
            if s.subject_id == subject_id:
                return s
        raise SubbenchError("no subject %r in %s" % (subject_id, self.id))

    def subjects_for(self, regime):
        """Contract 2's regime -> subject mapping, and the ONE place it lives."""
        if regime == "substitution":
            # [B140]: every manifest subject, manifest order (acc-small, the
            # gate's and make check's, then acc-main, the timed one).
            return list(self._short)
        if regime == "throughput":
            return list(self._throughput)
        if regime == "search_short":
            return [s for s in self._short if s.length <= self.short_search_max]
        if regime == "match":
            return list(self._short)
        if regime == "call-stream":
            return list(self._streams)                     # [B148] L4
        raise SubbenchError("unknown regime %r" % regime)

    def expectation(self, pattern, subject_id, regime):
        if self._expectations is None:
            self._expectations = self._load_expectations()
        return self._expectations.get((pattern, subject_id, regime))

    @property
    def expectations(self):
        if self._expectations is None:
            self._expectations = self._load_expectations()
        return self._expectations

    def missing_subject_files(self, regimes=None, limit=None):
        """Subject files that are absent. `limit` ([B140]): only the first k
        subjects of each regime are needed (a `quick` cell or a dry run that
        measures the small subject must not demand the 362 MB one)."""
        want = []
        for r in (regimes or self.regimes):
            subs = self.subjects_for(r)
            want.extend(subs[:int(limit)] if limit is not None else subs)
        return [p for s in want for p in (s.path, s.calls_path)
                if p is not None and not os.path.exists(p)]

    # ---------------------------------------------------------- the hash

    def content_hash(self):
        """`subbench.content_hash` (record_schema.md 8; the RULE is [B3]'s).

        sha256 over every COMMITTED file in the sub-bench directory: for each
        path in sorted order, `<relpath>\\n<sha256hex of the bytes>\\n`, joined
        and hashed. Generated trees (`subjects/`, `throughput/`, caches) are
        EXCLUDED -- they are reproduced byte for byte from a generator that is
        itself hashed, and including them would make the hash depend on
        whether a regenerable tree happened to be present. The manifests ARE
        hashed, so a subject whose content drifted from its generator is still
        caught: the manifest carries its sha256.

        Path-sorted and path-prefixed, so a rename is a change and two files
        swapping contents is a change (a bare concatenation of file hashes
        would see neither)."""
        return content_hash_of(self.root)


def subst_subjects_dir(root):
    """Where a substitution set's GENERATED subjects live: the environment's
    `PCRECBENCH_SUBST_SUBJECTS` (the same variable bench/subst/gen_subjects.py
    writes to -- a 362 MB file belongs under /var/tmp/pcrecbench/, not in the
    tree) or `<set>/subjects/`."""
    return os.environ.get("PCRECBENCH_SUBST_SUBJECTS") or os.path.join(
        root, "subjects")


def content_hash_of(root):
    """The `content_hash` rule (see `Subbench.content_hash`) over a sub-bench
    directory, WITHOUT loading the set ([B137]: `import` checks the hash of
    every committed set and must not need an engine binary to do it)."""
    parts = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in GENERATED_DIRS)
        for fn in sorted(filenames):
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            with open(full, "rb") as f:
                h = hashlib.sha256(f.read()).hexdigest()
            parts.append("%s\n%s\n" % (rel.replace(os.sep, "/"), h))
    return hashlib.sha256("".join(parts).encode("utf-8")).hexdigest()


def load(root):
    return Subbench(root)


def find(name, bench_root=None):
    """Resolve a sub-bench by directory NAME under `bench/`."""
    if bench_root is None:
        bench_root = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "bench")
    path = os.path.join(bench_root, name)
    if not os.path.isdir(path):
        raise SubbenchError(
            "no sub-bench %r under %s (have: %s)"
            % (name, bench_root,
               ", ".join(sorted(d for d in os.listdir(bench_root)
                                if os.path.isdir(os.path.join(bench_root, d))))
               if os.path.isdir(bench_root) else "<no bench/ directory>"))
    return Subbench(path)
