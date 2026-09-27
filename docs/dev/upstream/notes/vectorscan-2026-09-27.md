<!--
Internal header (ours; not part of the note text below the rule).
ids:            U7
target channel: github.com/VectorCamp/vectorscan issue tracker
tracker search: searched 2026-09-27, no existing report found (checked
                by keyword: "comment", "free-spacing", "(?x)"; also
                checked github.com/intel/hyperscan, the original
                project this is forked from — not archived, still
                receives pushes, but no matching issue there either)
latest checked: source-diffed against tags vectorscan/5.4.12
                (2025-07-22) and vectorscan/5.4.13 (2026-08-23, the
                current latest release) — src/parser/Parser.rl's
                comment-handling logic is byte-for-byte unchanged
                across all three tags including our pinned 5.4.11 (see
                docs/dev/lanes/b103other_report.md, when neither ragel
                nor CMake nor Boost dev headers were on this box).
                2026-09-27 (lane u7vs5413): BUILT vectorscan/5.4.13 from
                source in user space (Ragel 6.10 + CMake 3.31.6 fetched
                as binaries, Boost 1.86.0 headers + the simde submodule
                fetched as tarballs, no sudo/apt) and ran the repro
                against the real binary — STILL PRESENT, byte-identical
                output to 5.4.11's (`hs_version()` "5.4.13 2026-09-27");
                findings.tsv latest_checked = 5.4.13@2026-09-27.
                docs/dev/upstream/repro/U7/probe_5413_build.txt is the
                archived probe (build provenance: tag, commit sha,
                compiler, cmake options).
repro:          docs/dev/upstream/repro/U7/ (repro.c, run.sh,
                expected.txt)
approval:       [x] Frank approved 2026-09-27 — SENT https://github.com/VectorCamp/vectorscan/issues/416
-->

---

## Subject: `(?x)` pattern ending in an unterminated `#` comment is refused (code -4), where PCRE accepts end-of-pattern as closing it

Hi — `hs_compile()` refuses a free-spacing (`(?x)`) pattern whose last
line is a `#` comment with no trailing newline, with:

    hs_compile failed (code -4): Unterminated comment.

Minimal example (attached `repro.c` reduces two real patterns from our
own test corpus to this):

    (?x) abc  # trailing comment, no newline

PCRE's own definition of a `(?x)` `#` comment is that it runs to the
next newline **or to the end of the pattern**, whichever comes first —
there's no requirement that a newline actually be present if the
comment is the last thing in the pattern. Under that definition the
example above is a complete, well-formed pattern (matching literal
`abc` with insignificant whitespace/comments stripped), and that's how
libpcre2, PCRE-compatible pcrec, Oniguruma and Rust's `regex` crate all
read it.

Simply appending one trailing newline to the identical pattern text
(`"(?x) abc  # trailing comment, no newline\n"`) is enough to make
`hs_compile()` accept it — the newline terminates the open comment —
which is a useful hint that this is specifically about "does an open
comment survive end-of-input", not the free-spacing feature more
generally.

From reading `src/parser/Parser.rl`: the extended-mode comment action
(`enterNewlineTerminatedComment`) sets `inComment = true` and
transitions to a state that only clears it on `'\n'`; at end of input,
if `inComment` is still set, the parser unconditionally throws
`ParseError("Unterminated comment.")` — there's no "end of input also
closes an open comment" case. I checked this is unchanged as of the
current `vectorscan/5.4.13` tag (also true back through `5.4.12` and
our own pinned `5.4.11`) by diffing `Parser.rl` across all three
releases; I did not build 5.4.12/5.4.13 to confirm at the binary
level, only diffed the source.

I understand Hyperscan/vectorscan's regex support is documented as a
PCRE *subset* rather than full compatibility, so this may simply be an
intentional stricter posture rather than something you'd consider a
bug — I'm reporting it mainly because "stricter" here means a
syntactically valid, unambiguous PCRE pattern is refused outright
rather than, say, warned about, and the fix (treating end-of-pattern
like a newline for an open `#` comment) seems small and
backward-compatible either way.

Reproduction attached (`repro.c`, `run.sh`) — self-contained, links
only `libvectorscan`/Hyperscan (`<hs/hs.h>`, `-lhs`), tested against
5.4.11.

Thanks for maintaining vectorscan.
