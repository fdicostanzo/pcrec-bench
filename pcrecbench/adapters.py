"""adapters.py -- the Adapter interface, testee discovery, and THE DRIVER
PROTOCOL (harness contract 3).

=============================================================================
THE DRIVER PROTOCOL
=============================================================================

Both drivers implement exactly this, so that a difference between two
engines' numbers is the ENGINE and not the harness. A third driver copies the
shape, not the engine.

INVOCATION
    driver --pattern FILE          the canonical pattern, RAW BYTES
           --list SUBJECTS.tsv     `id<TAB>path` per line, no header
           --mode search|match     search = unanchored from offset 0;
                                   match  = whole-subject (anchored AND
                                            end-anchored)
           --iters N               iterations of the per-subject operation
           [--find-all]            search mode only: loop the whole subject
                                   counting NON-OVERLAPPING matches with
                                   pcrec match_api.md S3.1's find-all advance
                                   rule (adopted BY REFERENCE, KB-17,
                                   docs/dev/known_issues.md): the next scan
                                   starts at the match END when the match is
                                   non-empty, else one past the match's own
                                   reported START (`s3.1.1`'s `next_pos`
                                   residual, which is `start + 1` under the
                                   byte encoding this bench compiles
                                   everywhere) -- NEVER off the previous scan
                                   position, which double-counts an empty
                                   match found ahead of it. This is the
                                   throughput regime's operation, and the
                                   count is what its expectation states.
           [--utf8]                ([B77] U1, docs/design/utf8_set_v1.md
                                   8.4) the find-all EMPTY-MATCH advance
                                   becomes the next CHARACTER boundary:
                                   pcrec match_api.md S3.1.1's NORMATIVE
                                   utf8 rule -- from start + 1, skip every
                                   byte in 0x80-0xBF, stop at the first byte
                                   outside that range or at the subject's
                                   end. Passed by the adapter iff the
                                   harness set the handle's `utf8_advance`,
                                   which it does iff the pattern's ORACLE
                                   OPTION WORD carries PCRE2_UTF
                                   (`pcrecbench.expectations.utf8_advance`)
                                   -- one fact, so the oracle and every
                                   driver step alike. It moves the ADVANCE
                                   only, never the engine's own encoding
                                   (a config's choice); inert without
                                   --find-all, and inert in a driver with
                                   no find-all loop (vectorscan, boolean
                                   grain). Absent, every driver is
                                   byte-for-byte what it was.
           [--prime]               ([B129]) before each subject's timed loop,
                                   ONE untimed execution of the loop body's
                                   own operation (a single match, or the
                                   whole find-all pass), answer discarded,
                                   then the first clock reading. Warms
                                   lazy-cache engines (RE2, Rust regex)
                                   symmetrically. Passed iff the handle
                                   carries `prime`; harness-side scratch
                                   tier only. Absent, every driver is
                                   byte-for-byte what it was.
           [--compile-trials T]    compile T times, timing every phase; T-1
                                   of them are thrown away except for their
                                   timings (default 1)
           [--subject-timeout S]   per-SUBJECT alarm, seconds (0 = none)
           [--skip N]              start at the Nth subject of the list
                                   (how python RESUMES after a driver death)
           --mode subst            ([B140], docs/design/subst_bench_v1.md
                                   3.1.2) a TRANSFORM: apply the pattern's
                                   substitution over the whole subject, the
                                   OUTPUT being the answer. Additive -- every
                                   other mode is byte-for-byte what it was.
                                   Takes, instead of --find-all/--prime/
                                   --utf8 (REFUSED by name in this mode):
               --template FILE         the replacement, RAW BYTES, already in
                                       THIS engine's dialect (the harness
                                       rendered the neutral template with
                                       pcrecbench/subst_template.py)
               --subst-flags extended|none
                                       the engine's EXTENDED-replacement
                                       switch where it has one (libpcre2:
                                       PCRE2_SUBSTITUTE_EXTENDED, needed for
                                       case operators and conditionals)
               --bound ID=BYTES        (repeatable) the output capacity per
                                       subject, n + 8 * the oracle's
                                       substitution count + 1, an engine-
                                       neutral number (3.1.1); an engine
                                       that allocates for itself ignores it
                                       (rust-regex and RE2 do; their drivers
                                       accept the argument and ignore it, and
                                       also accept-and-ignore --subst-flags)
               --no-unicode            (rust driver only) RegexBuilder::
                                       unicode(false), passed at compile AND
                                       measure time for a substitution set
               --out-dir DIR           TRIAL 1 ONLY: write each subject's
                                       final output to DIR/<ID>.out, outside
                                       the clock. Absent on trials 2..N
               ITERS is always 1 (3.1.2: a 320 MB transform is 0.3-30 s; the
               trials are the repetition). Engine-specific sizing arms
               (libpcre2 `--sizing bound|first`) are that driver's own.
           --mode calls            ([B148] L4, docs/design/unusual_set_v1.md
                                   7.1-7.3) a CALL STREAM: every call of a
                                   declared call list, in order, over one
                                   subject -- the engine is given the REST
                                   of the subject from the call's offset
                                   (start offset = the call's offset, end =
                                   the subject's end; a `\\G` pattern
                                   anchors there). Additive -- every other
                                   mode is byte-for-byte what it was. Here:
               --list FILE             THREE columns per line,
                                       `id<TAB>subject<TAB>calls`, the calls
                                       file TSV `call_id offset length
                                       segment_bytes binding_id` with a
                                       header (bench/unusual/gen_streams.py).
                                       7.3 wrote this as one `--calls FILE`
                                       flag; a per-subject column is the
                                       same fact for a list of streams, and
                                       the resume rule (`--skip`) keeps
                                       working unchanged. A binding other
                                       than `-` (a VARS stream) is REFUSED by
                                       name by every driver but the pcrec
                                       driver ([B148] L7): a VARS stream's
                                       list line has a FOURTH column, the
                                       bindings table `binding_id<TAB>name<TAB>
                                       value` (value = lowercase hex of the
                                       bytes, `UNSET` or `EMPTY`; one row per
                                       (binding, name), a binding's rows
                                       consecutive), and each call of its
                                       calls file is one LINE of the subject
                                       ([offset, offset + length)) matched
                                       ALONE -- `^` is the line's start,
                                       result offsets line-relative -- with
                                       its binding; the result token `r` is a
                                       call REFUSED by the variables rule
                                       (vars.md 5), `stream refused=` its
                                       count (testees/common/vars_io.h).
               --tokens-dir DIR        after the clock stopped, write the
                                       per-call result tokens to
                                       DIR/<ID>.tok, one per line: `n`,
                                       `m:<s>,<e>` (+ `;<g1s>,<g1e>` iff the
                                       pattern HAS a group 1; unset `-1,-1`),
                                       `r` (host refusal, vars only), `g`
                                       (an engine give-up -- 7.1's set plus
                                       the one token a limit needs). The
                                       harness hashes the file; SHA-256
                                       stays out of every driver (the [B140]
                                       `out` precedent).
               [--anchor-explicit]     anchor each call at its offset with
                                       the engine's own runtime option
                                       (PCRE2_ANCHORED, onig_match, RE2
                                       ANCHOR_START, an anchored rust Input;
                                       7.1's O(segment) fallback) -- the
                                       `stream_anchor = explicit` arm
               ITERS = REPLAYS of the whole list; each replay is CLOCKED
               SEPARATELY and the clocks SUMMED (7.2 P6). The per-call results
               go to a PREALLOCATED array inside the loop (integers only);
               the tokens are spelled after the clock. --find-all, --utf8 and
               --prime are refused by name in this mode.
           [--deep]                ([B148] L4, 6.2) the `deep` limits arm:
                                   every matcher working-storage cap at
                                   1 GiB, every COUNTER at its type maximum
                                   (or 0 = unlimited), set OUTSIDE the
                                   timed loop. Per-engine meaning in each
                                   driver's header; inert absent.
           [--limits]              ([B148] L4, 6.2) print the engine's
                                   EFFECTIVE limits as `info lim_<name>
                                   <integer>` lines (both arms), READ BACK
                                   from the engine wherever it has a getter
                                   (each adapter declares which are read
                                   and which are the values it set).
                                   Passed iff the set says `unusual_set`.

    The driver reads EVERY subject into memory first, compiles once (timed,
    per phase), then for each subject takes one monotonic clock reading,
    loops `iters` times, and takes another. Never a clock per call and never
    an external per-call wrapper: this box's `timeout` alone costs ~108.7 ms
    per call (requirements 3, C5), which at these sizes is the whole signal.

OUTPUT -- TSV on stdout, LINE-BUFFERED (python reads it as a liveness and
crash-attribution channel, so a buffered driver would lose the attribution):

    info<TAB>NAME<TAB>VALUE
        engine facts probed from the library/artifact. `version` is
        mandatory. Everything else becomes `engine_metadata` if the
        adapter DECLARES it (record_schema.md 7 rule 1).

    compile<TAB>TRIAL<TAB>PHASE<TAB>SECONDS
        one line per phase per trial, TRIAL 1-based. (The contract sketched
        a 3-column `compile PHASE SECONDS`; the trial number is added
        because the record keeps RAW trials -- record_schema.md X9 requires
        dense 1..N per pattern, and a parser counting repeats to recover the
        number would silently mis-attribute a phase the driver skipped.)

    subject<TAB>ID<TAB>ANSWER<TAB>START<TAB>END<TAB>NCAPS<TAB>CONSUMED<TAB>ITERS<TAB>SECONDS<TAB>NMATCHES<TAB>CAPS
        ANSWER   match | nomatch | giveup:<code> | timedout | error:<text>
        START,END  the FIRST match's span, or `-`
        NCAPS    capture slots the engine delivered (0 when none)
        CONSUMED subject bytes the engine was given and accepted, or `-`
                 when the API does not expose it (each adapter's CLAUDE.md
                 states its convention -- requirements 4.4, A7)
        ITERS    the loop's N as actually run
        SECONDS  wall seconds for the WHOLE loop (%.9f)
        NMATCHES non-overlapping match count under --find-all, else `-`
        CAPS     `s:e,s:e,...` 1-based groups, `-1:-1` unset, or `-`
        (The contract's column list omitted CAPS and NMATCHES; contract 3
        requires `caps` in what measure() returns, and the throughput
        expectation IS a count, so both are columns rather than a second
        protocol.)

    error<TAB>TEXT     a fatal the driver could not attribute to a subject

    stream<TAB>ID<TAB>calls=N<TAB>matched=N<TAB>nomatch=N<TAB>refused=N<TAB>gave_up=N<TAB>first_code=C<TAB>first_limit=NAME<TAB>results_sha256=-<TAB>tokens=PATH
        ([B148] L4, --mode calls only) emitted AFTER the stream's `subject`
        line and OUTSIDE the clock: the LAST replay's per-call counts (every
        replay asks the same questions; the harness checks the counts and the
        hash), `first_code` the first give-up's engine code (`-` when none),
        `first_limit` the engine's own NAME for it where the driver has one
        (pcrec's shim does; else `-` and the adapter names the code), and the
        token file. In calls mode the `subject` line is the 11-column shape
        reused: ANSWER `stream`, START/END `-`, NCAPS 0, CONSUMED the
        subject's bytes, ITERS the replays, SECONDS the SUM of the per-replay
        clocks, NMATCHES the matched count, CAPS `-`.

    out<TAB>ID<TAB>PATH<TAB>BYTES
        ([B140], --mode subst only) emitted AFTER the subject's `subject`
        line and OUTSIDE the clock: subject ID's final output is BYTES long
        and sits at PATH (relative to --out-dir; `-` when no --out-dir was
        given, i.e. on trials 2..N, where only the length is reported). The
        harness hashes the file (sha256, once per (cell, case), on trial 1),
        checks trials 2..N by BYTES + NMATCHES, and deletes the file. This
        keeps SHA-256 out of every driver and out of the timed loop. In
        subst mode the `subject` line is the 11-column shape reused:
        ANSWER `match` iff the substitution count > 0 (else `nomatch`),
        START/END `-`, NCAPS 0, CONSUMED the subject's bytes, ITERS 1,
        SECONDS the timed transform, NMATCHES the SUBSTITUTION COUNT, CAPS
        `-`. A parser that does not know `out` ignores it (parse_driver_line
        returns kind None).

EXIT   0 all subjects reported; 2 usage/IO; 3 the pattern did not compile
       (with `error` lines carrying the engine's diagnostic).

THE PROCESS INVOCATION ([B140] step 4, the TOOLS tier -- NOT a driver). A
`testee.invocation = "process"` testee is a command-line tool (sed, perl, a
python script, sd, ripgrep: testees/tools/) and has NO driver binary and no
`--mode` at all. Its adapter implements only the substitution surface
(`subst_support`, `measure_subst`; `compile()` returns a handle and the
harness writes no compile row for a compiled case, schema X41/S7) and runs
pcrecbench/toolrun.py:
    trial 1:   an UNTIMED pass, `tool ... > out_dir/<ID>.out`; the harness's
               gate hashes it exactly as for a driver's `out` file
    every trial: the TIMED launch `tool ... | wc -c` (os.posix_spawn, no
               shell; tool and wc pinned to DIFFERENT cores; env LC_ALL=C
               only; warm page cache asserted by fincore). SECONDS is
               spawn-to-second-wait4; the byte count wc prints MUST equal
               the validated output size or the run raises SinkMismatch BY
               NAME (X39) and nothing is written
The `MatchRow` it returns has `.out_bytes` (wc's count), `.out_path` (trial 1
only), `.process` (the `match.process` object: argv with paths elided,
sink/sink_bytes, core/sink_core, user_s/sys_s/maxrss_kb from the tool's
wait4 rusage, page_cache_resident) and NO `nmatches`: a tool prints no
substitution count, so `subst_support()` carries `count = "oracle"` and
substrun takes the count from expectations.tsv when the output hash agrees.

TIMEOUTS come in two layers and they measure different things. The
per-SUBJECT alarm inside the driver is what makes record_schema.md's
per-subject `timed-out` possible at all -- requirements 4.4 wants to know
WHICH subject hung. `gnutimeout` on the driver PROCESS is the outer
backstop for a driver that hangs somewhere else (requirements 3).
"""

import hashlib
import importlib.util
import os
import tomllib

FORM_PLAIN = "plain"
FORM_WHOLE_SUBJECT = "whole-subject"

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTEES_ROOT = os.path.join(REPO_ROOT, "testees")


#: [B148] b148w1fix (inbox I-170, unusual_set_v1.md 6.2 amended): a `deep`
#: arm's big working storage (pcrec's 1 GiB caller buffer, libpcre2's 1 GiB
#: JIT stack / heap, Oniguruma's match stack) is created once and never
#: pre-touched, so a large subject's FIRST iteration paid the first-use page
#: faults of everything the match grew into (js-1m on pcrec-deep: ~109 of
#: ~140 ms). Pre-touching the storage itself stays ruled out (it is a
#: measurement of its own and would pin maxrss at the cap); instead a deep
#: arm runs the driver's own `--prime` (ONE untimed execution of the timed
#: loop body per subject) in the `throughput` regime, where subjects are
#: large. Declared on the testee as the runtime option below, so a record
#: says what was done; the call-stream regime (one process, many calls: the
#: faults amortise) and the untimed `--mem-pass` are unprimed.
STORAGE_PRIME_OPTION = {"name": "storage_prime", "value": "throughput-per-subject"}


def deep_prime_argv(handle, regime):
    """-> `["--prime"]` iff this is a deep arm's throughput measurement the
    harness has not already primed (a scratch `quick --prime` run), else []."""
    if (handle.get("deep") and regime == "throughput"
            and not handle.get("mem_pass") and not handle.get("prime")):
        return ["--prime"]
    return []


#: [B148] L4: the match-scope pair every `--mode calls` row carries
#: (unusual_set_v1.md 7.1, the O(segment) pre-flight's outcome).
STREAM_ANCHOR_DECL = {
    "type": "string", "scope": "match",
    "source": "the adapter: `--anchor-explicit` passed to the driver or not",
    "description": "how each call of a call stream is bounded to its segment: "
                   "`native` = the pattern's own \\G at the start offset (the "
                   "O(segment) pre-flight found no tail dependence), "
                   "`explicit` = the engine's runtime anchoring option",
}

#: [B148] L4: the 6.4 working-storage high-water pair + a library testee's
#: process maxrss (the amended 6.4 text: X38 scopes `match.process` to
#: process testees, so a LIBRARY testee records its maxrss here).
DEEP_MEM_DECL = {
    "deep_mem_bytes": {
        "type": "integer", "scope": "match",
        "source": "the untimed high-water pass (unusual_set_v1.md 6.4)",
        "description": "matcher working-storage high-water in bytes, by "
                       "`deep_mem_method`; never ranked across methods"},
    "deep_mem_method": {
        "type": "string", "scope": "match",
        "source": "the untimed high-water pass (unusual_set_v1.md 6.4)",
        "description": "canary | counting-alloc | mincore | rss-delta"},
    "deep_maxrss_kb": {
        "type": "integer", "scope": "match",
        "source": "getrusage(RUSAGE_SELF).ru_maxrss of the fresh untimed process",
        "description": "the high-water pass process's peak RSS (KiB): a "
                       "LIBRARY testee's maxrss (X38 keeps match.process for "
                       "process testees)"},
}


class AdapterError(Exception):
    pass


#: [B77] U2 (docs/design/utf8_set_v1.md 7.1): the ENGINE ENCODINGS a config
#: may declare with its `encoding` key. `byte` is every pre-[B77] config's
#: (implicit) value -- each adapter's own driver is byte-mode by design and
#: says so in its header -- and `utf8` is the character-mode sibling the
#: utf8 set's roster adds. This is the ENGINE's encoding, a testee
#: IDENTITY; it is NOT the driver protocol's `--utf8` flag, which moves only
#: the find-all advance and is keyed on the SET's oracle word
#: (`pcrecbench.expectations.utf8_advance`, U1) -- two facts, two names.
CONFIG_ENCODINGS = ("byte", "utf8")


def config_encoding(testee_id, cfg):
    """-> (encoding, config_extra_token_or_None) for a non-pcrec config's
    `encoding` key ([B77] U2). ABSENT or `byte` -> ("byte", None): the
    pre-[B77] testee byte for byte (no `config_extra`, the same derived
    testee_id -- `check_encoding_axis` proves it). `utf8` -> ("utf8",
    "utf8"): the token joins `config_extra`, so a utf8 sibling can never
    derive its byte sibling's testee_id (record_schema.md 6.4, X5) and
    land on top of it in the store. Anything else is refused BY NAME at
    config-read time, before anything is built or measured. (pcrec reads
    its encoding off its own `flags` -- `-e utf8` is pcrec's own argv --
    through `testees/pcrec/adapter.py`'s `effective_encoding`, which
    returns the same token.)"""
    enc = cfg.get("encoding", "byte")
    if enc not in CONFIG_ENCODINGS:
        raise AdapterError(
            "%s: encoding = %r is not one of %s (utf8_set_v1.md 7.1)"
            % (testee_id, enc, ", ".join(CONFIG_ENCODINGS)))
    return enc, ("utf8" if enc == "utf8" else None)


def sha256_file(path):
    """The sha256 of a file's bytes -- a scratch record's `testee.binary`
    identity (record_schema.md 6.8, X29)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class CompileResult:
    """What `Adapter.compile()` returns for ONE pattern, for ONE form.

    `phase_seconds` is `[{phase: seconds, ...}, ...]`, one dict per trial, in
    trial order; `engine_metadata` is the `pattern`-scoped pairs
    (record_schema.md 7 rule 2); `handle` is whatever `measure()` needs and
    is opaque to the harness."""

    __slots__ = ("outcome", "diagnostic", "phase_seconds", "engine_metadata",
                 "handle", "artifact_bytes", "declaration_ref")

    def __init__(self, outcome, phase_seconds=None, diagnostic=None,
                 engine_metadata=None, handle=None, artifact_bytes=None,
                 declaration_ref=None):
        self.outcome = outcome
        self.phase_seconds = phase_seconds or []
        self.diagnostic = diagnostic
        self.engine_metadata = engine_metadata or {}
        self.handle = handle
        self.artifact_bytes = artifact_bytes
        self.declaration_ref = declaration_ref


class CompiledPattern:
    r"""What `Adapter.compile()` returns: ONE `CompileResult` per FORM.

    Most engines have one form -- `plain` -- because they anchor with runtime
    options. An engine with no end-anchored mode compiles a SECOND artifact
    (pcrec: `(?:pattern)\z`) and returns two, because the match/compliance
    regime cannot be answered by the plain one. `forms` is keyed by the
    schema's `form` values, and `form_for_regime()` is the only place a
    regime chooses between them."""

    __slots__ = ("forms",)

    def __init__(self, forms):
        self.forms = dict(forms)

    def __contains__(self, form):
        return form in self.forms

    def get(self, form):
        return self.forms.get(form)

    @property
    def compiled_forms(self):
        return {f: r for f, r in self.forms.items() if r.outcome == "compiled"}

    def form_for_regime(self, regime):
        """The form this regime must be measured on.

        `match` is the WHOLE-SUBJECT question, so it uses the whole-subject
        artifact when the adapter built one; every other regime, and every
        adapter that anchors with runtime options, uses `plain`."""
        if regime == "match" and FORM_WHOLE_SUBJECT in self.forms:
            return FORM_WHOLE_SUBJECT
        return FORM_PLAIN


class MatchRow:
    """One driver `subject` line, parsed. The harness -- not the adapter --
    turns `answer` into a `match_outcome` against the sub-bench's
    expectation: an adapter that judged its own correctness would be
    marking its own homework."""

    __slots__ = ("subject_id", "answer", "start", "end", "ncaps", "consumed",
                 "iters", "seconds", "nmatches", "caps", "detail",
                 "out_path", "out_bytes", "process", "stream", "mem")

    def __init__(self, subject_id, answer, start=None, end=None, ncaps=0,
                 consumed=None, iters=0, seconds=0.0, nmatches=None,
                 caps=None, detail=None):
        self.subject_id, self.answer = subject_id, answer
        self.start, self.end, self.ncaps = start, end, ncaps
        self.consumed, self.iters, self.seconds = consumed, iters, seconds
        self.nmatches, self.caps, self.detail = nmatches, caps, detail
        # [B140] --mode subst: the `out` line paired to this row by the
        # driverrun layer (None everywhere else).
        self.out_path = self.out_bytes = None
        # [B140] step 4 (TOOLS tier): the `match.process` object of a timed
        # `tool | wc -c` launch (None for every library testee).
        self.process = None
        # [B148] L4 --mode calls: the `stream` line paired to this row (a
        # dict of its fields; None everywhere else).
        self.stream = None
        # [B148] L4 --mem-pass: the `mem` line paired to this row,
        # (bytes, method, maxrss_kb); None everywhere else.
        self.mem = None

    @property
    def matched(self):
        return self.answer == "match"

    @property
    def is_giveup(self):
        return self.answer.startswith("giveup")


def _opt(v):
    return None if v in ("-", "", None) else v


def parse_driver_line(line):
    """-> ('subject', MatchRow) | ('compile', (trial, phase, seconds))
         | ('info', (name, value)) | ('error', text)
         | ('out', (id, path_or_None, bytes))   ([B140])
         | ('stream', (id, {field: value}))     ([B148] L4)
         | ('mem', (id, bytes, method, maxrss_kb)) ([B148] L4) | (None, line)"""
    cols = line.rstrip("\n").split("\t")
    if not cols:
        return None, line
    kind = cols[0]
    if kind == "subject":
        if len(cols) < 11:
            return None, line
        (_, sid, answer, start, end, ncaps, consumed, iters, seconds,
         nmatches, caps) = cols[:11]
        return "subject", MatchRow(
            sid, answer,
            start=None if _opt(start) is None else int(start),
            end=None if _opt(end) is None else int(end),
            ncaps=int(ncaps or 0),
            consumed=None if _opt(consumed) is None else int(consumed),
            iters=int(iters or 0), seconds=float(seconds or 0.0),
            nmatches=None if _opt(nmatches) is None else int(nmatches),
            caps=_opt(caps))
    if kind == "compile" and len(cols) >= 4:
        return "compile", (int(cols[1]), cols[2], float(cols[3]))
    if kind == "info" and len(cols) >= 3:
        # a value may itself contain tabs; the NAME never does.
        return "info", (cols[1], "\t".join(cols[2:]))
    if kind == "error":
        return "error", "\t".join(cols[1:])
    if kind == "stream" and len(cols) >= 3:
        # [B148] L4: stream<TAB>ID<TAB>key=value...
        d = {}
        for c in cols[2:]:
            k, _, v = c.partition("=")
            d[k] = v
        return "stream", (cols[1], d)
    if kind == "mem" and len(cols) >= 5:
        # [B148] L4: mem<TAB>ID<TAB>BYTES<TAB>METHOD<TAB>MAXRSS_KB (--mem-pass)
        return "mem", (cols[1], int(cols[2]), cols[3], int(cols[4]))
    if kind == "out" and len(cols) >= 4:
        # [B140]: out<TAB>ID<TAB>PATH<TAB>BYTES (PATH `-` = no file written)
        return "out", (cols[1], None if cols[2] == "-" else cols[2],
                       int(cols[3]))
    return None, line


# ------------------------------------------------------------------ Adapter

class Adapter:
    """Harness contract 3. Subclasses live in `testees/<name>/adapter.py` and
    are found by `discover()`."""

    name = None
    #: False for the TOOLS tier ([B140] step 4, testees/tools/): a command-line
    #: tool has no matcher driver, so the generic per-adapter sweeps that call
    #: `measure()` or expect a pattern to refuse at compile skip it.
    has_driver = True

    def __init__(self, directory):
        self.dir = directory
        cfg_path = os.path.join(directory, "configs.toml")
        if not os.path.exists(cfg_path):
            raise AdapterError("no configs.toml in %s" % directory)
        with open(cfg_path, "rb") as f:
            self.cfg = tomllib.load(f)

    # ---- the interface -----------------------------------------------

    def testees(self):
        """id -> config dict, from `configs.toml`'s `[testees.<id>]`."""
        return dict(self.cfg.get("testees", {}))

    def config(self, testee_id):
        try:
            return self.testees()[testee_id]
        except KeyError:
            raise AdapterError(
                "%s provides no testee %r (have: %s)"
                % (self.name, testee_id, ", ".join(sorted(self.testees()))))

    def describe(self, testee_id, workdir=None):
        """The record's `testee` block, every field, versions PROBED.

        v1.2: a describe() MAY carry `tier: "scratch"` (a testee that is
        scratch BY CONSTRUCTION -- a provided binary) and `binary: {path,
        sha256}`. The harness lifts `tier` onto the setup layer (it is not a
        testee field) and keeps `binary` where it is."""
        raise NotImplementedError

    def tier(self, testee_id):
        """The tier this testee FORCES, or `pinned` when it forces none. A
        provided-binary testee answers `scratch` here so the harness can
        refuse the canonical store BEFORE it prepares, gates or measures
        anything (record_schema.md 6.8). The default is `pinned`."""
        return "pinned"

    def binary_identity(self, testee_id, workdir=None):
        """-> {"path": str, "sha256": hex64}: WHAT THE ENGINE BINARY WAS. A
        scratch record must carry it (X29), and a pinned testee measured at
        the scratch tier (`run --tier scratch`) is still a binary somewhere.
        An adapter that cannot say raises AdapterError."""
        raise AdapterError(
            "%s cannot describe the binary behind testee %r, so it cannot "
            "write a scratch-tier record (X29 requires testee.binary)"
            % (self.name, testee_id))

    def prepare(self, testee_id, workdir):
        """Build the driver / resolve the pin. Idempotent."""
        raise NotImplementedError

    def compile(self, testee_id, pattern_id, pattern, options, trials, workdir,
                requires_free_spacing=False):
        """-> CompiledPattern (one CompileResult per form).

        `pattern_id` is passed so each pattern gets its OWN scratch under
        `workdir`. It is not decoration: a sub-bench has several patterns, the
        harness compiles them ALL before measuring any, and an adapter that
        wrote `workdir/pattern.rx` or `workdir/artifact.so` would have the
        last pattern's artifact under the first pattern's handle. That bug
        was written, and it was invisible on this sub-bench because its two
        patterns agree on every subject -- so the interface makes it
        unwriteable instead of relying on an adapter author to remember.

        `requires_free_spacing` ([B70], `docs/design/capability_set_v1.md`
        14; DEFAULT `False`, so every pre-existing caller and every
        adapter that does not build a `whole-subject` wrap at all is
        unaffected): the harness's own reading of THIS pattern's declared
        `requires=free-spacing` tag (`pcrecbench.capability.
        pattern_requires`), computed once in `harness.run_cell` (the ONE
        place a Pattern object with `.tags` is visible -- an adapter sees
        only `pattern_id` and raw bytes) and handed down so a
        `whole-subject` wrap that appends `)\\z` after the pattern text
        can insert a newline FIRST when, and only when, doing so is safe
        (see `record.whole_subject_text`'s own docstring for the full
        argument). An adapter with no such wrap -- libpcre2/RE2's
        runtime-flag anchoring, needing no second artifact at all --
        ignores this parameter entirely."""
        raise NotImplementedError

    # ---- the substitution tier ([B140]) ---------------------------------

    def subst_support(self, testee_id):
        """-> None (this testee has no substitution call; the default, so
        every pre-[B140] adapter refuses a substitution set BY NAME) or a dict
        {"dialect": <pcrecbench.subst_template.DIALECTS member>,
         "competitor": <the name divergences.tsv rows use for this testee>,
         "sizing": "bound" | "first",
         "count": "oracle"          (optional; the TOOLS tier: the testee
                                     cannot report a substitution count, so
                                     substrun takes it from the expectation
                                     iff the output hash agrees)}.
        The harness renders the neutral template in `dialect`, looks the
        (case, competitor) pair up in the set's divergences.tsv, and hands
        the rendered bytes to `measure_subst`."""
        return None

    def measure_subst(self, handle, subjects, bounds, out_dir, timeout=None):
        """ONE trial of a substitution cell -> (rows, info, notes), rows one
        MatchRow per subject with `.out_path`/`.out_bytes` set. `handle` is
        the compiled-pattern handle with the harness's `handle["subst"]`
        ({"template_file", "flags": "extended"|"none"}) added; `bounds` is
        {subject_id: capacity_bytes}; `out_dir` is a directory on trial 1 and
        None on trials 2..N (the driver writes no file then, still reports the
        length). The harness, not the adapter, hashes and judges."""
        raise NotImplementedError

    #: [B148] L4: does this adapter's driver speak `--mode calls` (the
    #: `call-stream` regime)? False by default, so a set declaring the regime
    #: refuses every other adapter BY NAME rather than handing it a mode its
    #: driver would reject.
    calls_mode = False

    #: [B148] L4: {engine return code: the engine's own NAME for it} for the
    #: codes a give-up can carry; the harness names a stream's first give-up
    #: from it when the driver did not (unusual_set_v1.md 6.5). Empty here.
    giveup_names = {}

    def supports_calls(self, testee_id):
        """[B148] L4: whether THIS testee runs `--mode calls`. `calls_mode`
        by default; an adapter whose configs differ (vectorscan: only the
        `-som` siblings carry a span) overrides it."""
        return bool(self.calls_mode)

    def mem_method(self, handle):
        """[B148] L4 (unusual_set_v1.md 6.4): the `deep_mem_method` this
        handle's driver reports under `--mem-pass`, or None (no method: the
        harness skips the high-water pass). None by default."""
        return None

    def unusual_metadata_decl(self, testee_id):
        """[B148] L4: the `engine_metadata_declaration` entries only an
        `unusual_set` record carries -- the `lim_*` limits read-back
        (unusual_set_v1.md 6.2), `stream_anchor` (7.1) and the 6.4 pair.
        The harness merges them into the testee block on that set only. The
        default declares `stream_anchor` for an adapter that speaks
        `--mode calls`, nothing otherwise."""
        if not self.supports_calls(testee_id):
            return {}
        return {"stream_anchor": STREAM_ANCHOR_DECL}

    def measure(self, handle, regime, subjects, iters, trials, timeout=None):
        """-> (rows_by_trial, info, notes).

        `rows_by_trial` is one list of MatchRow per TRIAL (contract 3: the
        driver runs once per (regime, trial)); `info` is the driver's `info`
        pairs; `notes` are harness-level remarks -- a driver restart, a
        subject with no outcome -- that land in the record's `status_detail`
        rather than being swallowed."""
        raise NotImplementedError


# ---------------------------------------------------------------- discovery

def _load_module(path, modname):
    spec = importlib.util.spec_from_file_location(modname, path)
    if spec is None or spec.loader is None:
        raise AdapterError("cannot load %s" % path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def discover(root=None):
    """-> {engine_name: Adapter}. Imports every `testees/*/adapter.py`."""
    root = root or TESTEES_ROOT
    out = {}
    if not os.path.isdir(root):
        return out
    for entry in sorted(os.listdir(root)):
        path = os.path.join(root, entry, "adapter.py")
        if not os.path.exists(path):
            continue
        mod = _load_module(path, "pcrecbench_testee_" + entry)
        cls = getattr(mod, "Adapter", None)
        if cls is None:
            raise AdapterError("%s defines no class Adapter" % path)
        out[entry] = cls(os.path.join(root, entry))
    return out


def resolve(testee_id, root=None):
    """-> (Adapter, config) for a testee id, searching every adapter."""
    adapters = discover(root)
    for a in adapters.values():
        if testee_id in a.testees():
            return a, a.testees()[testee_id]
    known = sorted(t for a in adapters.values() for t in a.testees())
    raise AdapterError("no adapter provides testee %r (have: %s)"
                       % (testee_id, ", ".join(known) or "<none>"))


def all_testees(root=None):
    out = {}
    for name, a in discover(root).items():
        for tid, cfg in a.testees().items():
            out[tid] = (name, cfg)
    return out
