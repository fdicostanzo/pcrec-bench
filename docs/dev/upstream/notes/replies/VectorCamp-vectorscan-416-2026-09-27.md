<!--
Internal header (ours; not part of the reply text below the rule).
thread:        VectorCamp/vectorscan#416
answers:       markos's comment id 5859185642, 2026-09-27T19:39:17Z
               ("@fdicostanzo could you please test against 5.4.13?")
finding:       U7 (docs/dev/upstream/findings.tsv)
built from:    docs/dev/upstream/repro/U7/probe_5413_build.txt (this
               session's from-source build of tag vectorscan/5.4.13,
               commit acd7363aadea43da9c5246542d9969db843dd132)
approval:      [ ] not yet approved -- do not post
-->

---

Yes -- I built `vectorscan/5.4.13` from source (tag, commit
`acd7363aadea43da9c5246542d9969db843dd132`) and ran the same repro
against it directly (not just the source diff I'd mentioned above).

    plain (no trailing newline)      REFUSED code -4: Unterminated comment.
    plain + one trailing \n          COMPILED

Same result as 5.4.11: `hs_compile()` still refuses the plain form and
still accepts it once a trailing newline is appended. `hs_version()`
reports `5.4.13 2026-09-27` from the freshly built library, so this is
the real 5.4.13 binary, not a stale link.

Build notes in case useful: this needed Ragel 6.10, Boost 1.86.0
(headers only), and the `simde` submodule (pinned commit
`416091ebdb9e901b29d026633e73167d6353a0b0` at this tag) -- none of
which were on my box already, so everything was fetched as source/
release tarballs and built locally, `libpcre`'s optional check aside
(harmless here since unit tests are off). Happy to share the exact
CMake invocation if it helps reproduce.
