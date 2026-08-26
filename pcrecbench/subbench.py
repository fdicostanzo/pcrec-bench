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
import os
import tomllib

REGIME_TO_ENUM = {
    "match": "match-compliance",
    "search_short": "short-subject-search",
    "throughput": "large-subject-throughput",
}
ENUM_TO_REGIME = {v: k for k, v in REGIME_TO_ENUM.items()}

# The regime's MATCH SEMANTICS (contract 2). `match` is anchored + end-
# anchored over the whole subject; the other two are unanchored SEARCH.
REGIME_MODE = {
    "match": "match",
    "search_short": "search",
    "throughput": "search",
}

# Files under bench/<name>/ that are GENERATED, and so are excluded from the
# content hash: hashing them would make the hash depend on whether a
# regenerable tree happened to be present.
GENERATED_DIRS = ("subjects", "throughput", "__pycache__")


class SubbenchError(Exception):
    pass


class Pattern:
    __slots__ = ("name", "file", "feature_tier", "hazard_class", "size_class",
                 "convention", "tags", "role")

    def __init__(self, d):
        for k in self.__slots__:
            setattr(self, k, d.get(k))
        self.tags = list(d.get("tags") or [])
        # record_schema.md 5 (v1.3, [B15]): `role` is `member` unless the
        # sidecar says `floor` -- the ONE per-call baseline pattern a set may
        # declare. Defaulting here, not in the record, means an old sidecar
        # with no `role` key loads exactly as it always did.
        self.role = self.role or "member"
        for req in ("name", "file", "hazard_class", "size_class"):
            if not getattr(self, req):
                raise SubbenchError("pattern entry is missing %r: %r" % (req, d))


class Subject:
    __slots__ = ("subject_id", "length", "sha256", "description", "path", "kind")

    def __init__(self, subject_id, length, sha, desc, path, kind):
        self.subject_id, self.length, self.sha256 = subject_id, int(length), sha
        self.description, self.path, self.kind = desc, path, kind


class Expectation:
    __slots__ = ("pattern", "subject", "regime", "expected", "start", "end",
                 "nmatches", "method", "oracle")

    def __init__(self, cols):
        (self.pattern, self.subject, self.regime, self.expected, start, end,
         n, self.method, self.oracle) = cols
        self.start = None if start == "-" else int(start)
        self.end = None if end == "-" else int(end)
        self.nmatches = None if n == "-" else int(n)

    @property
    def matched(self):
        return self.expected == "match"


class Subbench:
    def __init__(self, root):
        self.root = os.path.abspath(root)
        sidecar = os.path.join(self.root, "subbench.toml")
        if not os.path.exists(sidecar):
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
        self.patterns = [Pattern(p) for p in self.cfg.get("patterns", [])]
        if not self.patterns:
            raise SubbenchError("%s declares no patterns" % sidecar)
        self.testee_notes = self.cfg.get("testees", {})

        subj = self.cfg.get("subjects", {})
        self.short_search_max = int(subj.get("short_search_max_bytes", 256))
        self._short = self._load_manifest(subj.get("manifest", "manifest.tsv"),
                                          "subjects", "short")
        tman = subj.get("throughput_manifest")
        self._throughput = (self._load_manifest(tman, "throughput", "throughput")
                            if tman else [])

        exp = self.cfg.get("expectations", {})
        self.expectation_file = exp.get("file", "expectations.tsv")
        self.default_method = exp.get("default_method", "")
        # LAZY: gen_expectations.py loads the sub-bench in order to WRITE this
        # file, so construction must not require it to exist yet.
        self._expectations = None

    # ------------------------------------------------------------- loading

    def _load_manifest(self, name, subdir, kind):
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
                cols = line.split("\t", 3)
                if len(cols) < 4:
                    raise SubbenchError("%s:%d: expected 4 columns, got %d"
                                        % (path, i + 1, len(cols)))
                sid, length, sha, desc = cols
                out.append(Subject(sid, length, sha, desc,
                                   os.path.join(self.root, subdir, sid + ".bin"),
                                   kind))
        return out

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
        the specimen's classes carry bytes that are not valid UTF-8 text."""
        with open(os.path.join(self.root, self.pattern(name).file), "rb") as f:
            return f.read()

    def subject_bytes(self, subject_id):
        with open(self.subject(subject_id).path, "rb") as f:
            return f.read()

    def subject(self, subject_id):
        for s in self._short + self._throughput:
            if s.subject_id == subject_id:
                return s
        raise SubbenchError("no subject %r in %s" % (subject_id, self.id))

    def subjects_for(self, regime):
        """Contract 2's regime -> subject mapping, and the ONE place it lives."""
        if regime == "throughput":
            return list(self._throughput)
        if regime == "search_short":
            return [s for s in self._short if s.length <= self.short_search_max]
        if regime == "match":
            return list(self._short)
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

    def missing_subject_files(self, regimes=None):
        want = []
        for r in (regimes or self.regimes):
            want.extend(self.subjects_for(r))
        return [s.path for s in want if not os.path.exists(s.path)]

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
        parts = []
        for dirpath, dirnames, filenames in os.walk(self.root):
            dirnames[:] = sorted(d for d in dirnames if d not in GENERATED_DIRS)
            for fn in sorted(filenames):
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, self.root)
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
