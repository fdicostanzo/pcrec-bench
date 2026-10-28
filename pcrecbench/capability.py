"""capability.py -- THE PRE-COMPILE CAPABILITY POLICY (docs/design/
capability_set_v1.md 5.3, [B42] L5, lane b42cap, 2026-09-16):

    REQUIRES(pattern) not-subset-of capabilities(config)
        => `unsupported-by-declaration`, decided BEFORE any compile.

Two closed inputs, both read by NAME, never invented:

  REQUIRES(pattern)     a pattern's `tags` list, filtered to entries
                         spelled `requires-<token>` (`subbench.Pattern.
                         tags` -- the SAME flat list whether the pattern
                         came from a sidecar `[[patterns]]` TOML array or
                         an `.rxt` block's own `tag requires=...` line,
                         `subbench._pattern_dict_from_rxt`'s generic
                         per-key flattening). `<token>` is validated
                         against `REQUIRES_VOCAB` (5.1's closed
                         vocabulary) at read time -- an unknown token is
                         a load error naming the closed set, the same
                         discipline `docs/dev/predictions/CLAUDE.md`
                         states for its own closed sets.

  capabilities(config)  read from the set's `.rxt` `ext bench` aux block
                         (5.2: "declared PER CONFIG"; `roster` +
                         `capabilities <testee-id>` sub-trees) -- TWO
                         load paths, because `bench/capability` itself is
                         NOT rxt-loadable as a WHOLE at the pinned pcrec
                         (outbox O-29: `--list-source` drops all but the
                         last pattern block's own `provenance` row, and
                         `rxt_source.load_rxt_source`'s own gate refuses
                         the load outright on that symptom):

                           (a) THE LOADER path -- `sb.rxt` is already
                               loaded (a future set whose sidecar sets
                               `rxt_source = ...` and does not trip
                               O-29): read `sb.rxt.aux_rows` directly, no
                               second subprocess call.
                           (b) THE SIDECAR/SHIM path -- `sb.rxt` is None
                               (today's real state for `bench/capability`:
                               its sidecar has no `rxt_source = ` key at
                               all, `subbench.toml`'s own `[[patterns]]`
                               TOML array is what the harness actually
                               loads patterns through) -- a
                               `patterns.rxt` file sitting beside
                               `subbench.toml` is read through
                               `rxt_source.load_aux_rows()`, which reads
                               ONLY the `#section aux` rows and the two
                               gates that scan per-pattern-block content
                               (block<->sidecar agreement, O-29's own
                               provenance-agreement gate) never run --
                               an `ext` block lives entirely outside the
                               main pattern table those gates scan. This
                               is the path every check and every real
                               `pcrecbench run`/`quick` cell on
                               `bench/capability` exercises today.

                         A set with NEITHER (no `.rxt` file at all, e.g.
                         every pre-[B42] set) resolves `capabilities(*)`
                         to the empty set for every config -- which is
                         harmless BY CONSTRUCTION, not a special case:
                         `REQUIRES(pattern)` is empty for every pattern
                         in a set that never authors a `requires-*` tag
                         (every set but `bench/capability` today), so the
                         subset check never fires and this policy is a
                         silent no-op on every pre-[B42] set (checked,
                         `check_capability_policy_noop_elsewhere` in
                         `tools/selfcheck.py`).

THE FAIL-CLOSED RULE (5.2): a config absent from the matrix's `roster`,
or a `capabilities <id>` sub-tree the matrix declares but leaves
empty, satisfies NOTHING -- `missing_capabilities` returns the pattern's
whole REQUIRES set in that case, never an empty set by omission.
"""

import os
import re

from . import rxt_source as _rxt

# docs/design/capability_set_v1.md 5.1 (16 tags) + 6.2's addition
# (`true-end-anchor`, a 17th) + docs/design/utf8_set_v1.md 7.5's three
# ([B77] U1, Q3 ruled GLOBAL by inbox I-94: `utf8-encoding`,
# `ascii-class-scope`, `unicode-class-scope` -- 20 tokens) -- the CLOSED
# vocabulary. `unicode-class-scope` is ALSO the one token the ORACLE reads:
# it puts PCRE2_UCP in that pattern's option word
# (`pcrecbench.expectations.oracle_option_word`). Kept here, not
# re-derived from any one set's own `.rxt vocabulary requires ...` line,
# because the policy is harness-wide: a future second capability-shaped
# set validates against the SAME closed list, not its own copy.
REQUIRES_VOCAB = frozenset({
    "backrefs", "lookaround", "lookbehind-variable", "possessive-quantifier",
    "atomic-group", "recursion", "conditionals", "k-reset", "control-verbs",
    "unicode-properties", "named-groups", "free-spacing", "callouts",
    "span-reporting", "non-utf8-subject", "captures", "true-end-anchor",
    # [B77] U1, utf8_set_v1.md 7.5 -- PER-PATTERN, like every token above:
    #   utf8-encoding        the pattern's byte-mode and character-mode
    #                        readings can diverge on a subject its set runs
    #                        it over (unsatisfied by every BYTE-mode config)
    #   ascii-class-scope    \w \d \s / POSIX classes must be ASCII-scoped
    #                        under UTF-8 (PCRE2's default absent PCRE2_UCP)
    #   unicode-class-scope  \w \d \s must be Unicode-widened (PCRE2_UCP)
    "utf8-encoding", "ascii-class-scope", "unicode-class-scope",
    # [B148] L1, unusual_set_v1.md 5.5 (r9 C2): caller VARIABLES (`${name}`,
    # pcrec vars.md) -- the third unusual feature beside `recursion` and
    # `callouts`.
    "vars",
})

# [B148] L1, unusual_set_v1.md 5.5 (PROPOSED P4): the ONE open family in
# the vocabulary -- `unusual-<member>`, a per-MEMBER capability token. An
# ASSISTED config declares `unusual-<member>` for every member whose
# verdict is ASSISTED; a NOT-CAPABLE member is then `unsupported-by-
# declaration` through the same per-token path as any other. The family is
# closed in SHAPE (a slug after the prefix), not in membership: the members
# are the set's own pattern ids, which this module does not enumerate.
UNUSUAL_PREFIX = "unusual-"
_UNUSUAL_RE = re.compile(r"^unusual-[a-z0-9]([a-z0-9-]*[a-z0-9])?$")

_REQUIRES_PREFIX = "requires-"


def is_requires_token(token):
    """True iff `token` is in the closed REQUIRES vocabulary: one of
    `REQUIRES_VOCAB`, or an `unusual-<member>` token (`<member>` a slug)."""
    return token in REQUIRES_VOCAB or bool(_UNUSUAL_RE.match(token))


def _vocab_text():
    return ", ".join(sorted(REQUIRES_VOCAB)) + ", unusual-<member>"


def not_capable_declaration_ref(ledger_ref, tokens, budget):
    """The `declaration_ref` spelling of a NOT-CAPABLE assist verdict
    (unusual_set_v1.md 5.5, r9 S-11): `<ledger_ref> tokens=<N>
    budget=<X>`, so the count and the budget travel in the store, not only
    in the set's assists.tsv. `ledger_ref` names the ledger row (e.g.
    `bench/unusual/assists/assists.tsv:7`)."""
    if not (isinstance(tokens, int) and isinstance(budget, int)
            and tokens > budget >= 0):
        raise CapabilityError(
            "a NOT-CAPABLE verdict needs tokens > budget (got tokens=%r "
            "budget=%r)" % (tokens, budget))
    return "%s tokens=%d budget=%d" % (ledger_ref, tokens, budget)


_NOT_CAPABLE_RE = re.compile(r"(?:^|\s)tokens=(\d+) budget=(\d+)(?:\s|$)")


def parse_not_capable(declaration_ref):
    """-> `(tokens, budget)` from a `declaration_ref` written by
    `not_capable_declaration_ref`, or None when the reference carries no
    count (every other `unsupported-by-declaration` row)."""
    m = _NOT_CAPABLE_RE.search(declaration_ref or "")
    return (int(m.group(1)), int(m.group(2))) if m else None


class CapabilityError(Exception):
    pass


def pattern_requires(pattern):
    """-> a `frozenset` of the REQUIRES tokens `pattern.tags` declares
    (entries spelled `requires-<token>`). Raises `CapabilityError` naming
    the pattern and the token if a tag claims a token outside
    `REQUIRES_VOCAB` -- the closed-vocabulary rule, checked at the point
    a tag is actually read rather than trusted from whichever lane wrote
    it."""
    out = set()
    for tag in pattern.tags or ():
        if not tag.startswith(_REQUIRES_PREFIX):
            continue
        token = tag[len(_REQUIRES_PREFIX):]
        if not is_requires_token(token):
            raise CapabilityError(
                "pattern %r declares requires-%s, which is not in the "
                "closed REQUIRES vocabulary (%s)"
                % (pattern.name, token, _vocab_text()))
        out.add(token)
    return frozenset(out)


# One matrix per sub-bench ROOT for the lifetime of this process -- a
# `pcrecbench run`/`quick`/`make check-harness` invocation loads a
# sub-bench once and asks this module about many (pattern, testee)
# pairs; re-running `pcrec --list-source` per pair would be a real,
# needless subprocess cost on a corpus this set's size.
_matrix_cache = {}


def _parse_ext_bench_matrix(aux_rows):
    """`aux_rows` (the `#section aux` dump rows, `rxt_source`'s shape) ->
    `{testee_id: frozenset(tokens)} | None`. `None` iff the tree carries
    no `ext bench` block at all (a set that does not use this
    production) -- NEVER an empty dict standing in for "no block found",
    since an empty dict here would silently mean fail-closed for a set
    that never intended to declare capabilities at all versus one that
    did and left every config empty; the two are told apart by the
    return value's own identity. A `capabilities <id>` sub-tree with
    zero children (a config declared and left with no lines under it) IS
    a real empty `frozenset`, which the fail-closed rule reads correctly
    either way.

    Every listed token is validated against `REQUIRES_VOCAB` -- the
    closed-vocabulary rule applies to a DECLARED capability exactly as it
    applies to a pattern's own REQUIRES tag; a matrix that claims a
    config satisfies a token outside the vocabulary is a load error, not
    silently accepted documentation."""
    ext_line = None
    for r in aux_rows:
        if r["depth"] == "0" and r["key"] == "ext" and r["value"] == "bench":
            ext_line = r["line"]
            break
    if ext_line is None:
        return None
    # Pass 1: every `capabilities <testee-id>` row directly under `ext
    # bench`, indexed by ITS OWN line -- several such rows share the
    # same parent (`ext_line`), so a testee id alone cannot key them.
    cap_rows_by_line = {r["line"]: r["value"] for r in aux_rows
                        if r["parent_line"] == ext_line
                        and r["key"] == "capabilities"}
    matrix = {testee: set() for testee in cap_rows_by_line.values()}
    # Pass 2: every depth-2 token row, attached to its capabilities row
    # by `parent_line`.
    for r in aux_rows:
        testee = cap_rows_by_line.get(r["parent_line"])
        if testee is None:
            continue
        token = r["key"]
        if not is_requires_token(token):
            raise CapabilityError(
                "ext bench: capabilities %s declares %r, which is not "
                "in the closed REQUIRES vocabulary (%s)"
                % (testee, token, _vocab_text()))
        matrix[testee].add(token)
    return {testee: frozenset(tokens) for testee, tokens in matrix.items()}


def _load_matrix(sb):
    """-> `{testee_id: frozenset(tokens)} | None`, cached per `sb.root`.

    Path (a): `sb.rxt` already loaded (the LOADER path). Path (b):
    `sb.rxt` is None but a `patterns.rxt` sits beside `subbench.toml`
    (the SIDECAR/SHIM path -- today's real state for `bench/capability`,
    O-29). Neither file present -> `None` (this set declares no
    capability matrix at all)."""
    if sb.root in _matrix_cache:
        return _matrix_cache[sb.root]
    if sb.rxt is not None:
        aux_rows = sb.rxt.aux_rows
    else:
        path = os.path.join(sb.root, "patterns.rxt")
        if not os.path.exists(path):
            _matrix_cache[sb.root] = None
            return None
        aux_rows, _head = _rxt.load_aux_rows(path)
    matrix = _parse_ext_bench_matrix(aux_rows)
    _matrix_cache[sb.root] = matrix
    return matrix


def capabilities_for(sb, testee_id):
    """-> the `frozenset` of REQUIRES tokens `testee_id` satisfies, per
    the set's `ext bench` matrix. The FAIL-CLOSED rule (5.2): a set with
    no matrix at all, or a matrix that never mentions `testee_id`,
    satisfies NOTHING -- always a real (possibly empty) `frozenset`,
    never `None` (a caller subtracts from it unconditionally)."""
    matrix = _load_matrix(sb)
    if matrix is None:
        return frozenset()
    return matrix.get(testee_id, frozenset())


def missing_capabilities(sb, testee_id, pattern, grants=frozenset()):
    """REQUIRES(pattern) - capabilities(testee_id). Empty iff the config
    may attempt this pattern; non-empty names every token it lacks.

    [B148] lane b148aw (unusual_set_v1.md 5.5): `grants` are tokens the
    ADAPTER adds at run time (an assisted config's `unusual-<member>` for
    each ASSISTED ledger row, testees/assist/adapter.py
    `capability_grants`), unioned with the matrix's. An `unusual-<member>`
    token the pattern requires AND the config holds SUBSUMES the rest: the
    config supplies that member's whole feature (natively, where the matrix
    declares it only beside the member's other requires -- bench/unusual/
    gen_patterns.py FEATURE_MEMBERS -- or by its assist), so nothing is
    missing."""
    requires = pattern_requires(pattern)
    if not requires:
        return frozenset()
    have = capabilities_for(sb, testee_id) | frozenset(grants)
    if any(t.startswith(UNUSUAL_PREFIX) for t in requires & have):
        return frozenset()
    return requires - have


def declaration_ref(sb, testee_id, pattern, missing):
    """The `declaration_ref` free-text value for an `unsupported-by-
    declaration` compile row (schema: required whenever that outcome is
    used, "must cite the sub-bench engine note that declares it") --
    names the set, the config, the missing token(s) and where the
    declaration lives, so the citation is checkable by a reader without
    re-running this module."""
    return ("%s@%s ext bench: capabilities %s does not declare %s "
            "(pattern %s requires %s)"
            % (sb.id, sb.version, testee_id, ", ".join(sorted(missing)),
               pattern.name, ", ".join(sorted(missing))))
