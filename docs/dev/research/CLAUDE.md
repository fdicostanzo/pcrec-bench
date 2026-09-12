# docs/dev/research/ — research notes behind a design

Read-mostly survey notes written by lanes BEFORE a design note is drafted:
what exists outside this repo (corpora, engines, formats), with sources
cited by URL/path and version, what was checked versus read, and a
"questions for Frank" section. A research note is an input to a
`docs/design/` note, never a spec; findings it makes are re-derived or
cited by the design that uses them. Named `YYYY-MM-DD-<row>-<topic>.md`.

| file | what |
|---|---|
| `2026-09-12-b42-rx-in-the-wild.md` | [B42] (a): sources of regexes in real use (rule sets, validators, log parsers, published corpora, benchmark suites) — licence, dialect, size, real-vs-contrived evidence, edge-case value, a shortlist |
| `2026-09-12-b42-engine-landscape.md` | [B42] (a): the engine capability/option landscape for the [B7] roster (RE2, Rust regex, Vectorscan, Oniguruma, TRE, POSIX, pcre2 modes, pcrec) — unsupported constructs and how each reports them, match semantics, the space-vs-speed dials, what "compile time" is per engine |
| `2026-09-12-b42-rxt-as-source.md` | [B42] (a): what building a set ON the .rxt format (pcrec DD-13) means — what .rxt carries, what a sub-bench needs beyond it, source-of-truth options and their R-BENCH-4 consequences |

Maintenance: update this table when a note is added.
