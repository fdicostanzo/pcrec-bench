<!--
Internal header (ours; not part of the reply text below the rule).
thread:        VectorCamp/vectorscan#416
answers:       markos's comment id 5859185642, 2026-09-27T19:39:17Z
               ("@fdicostanzo could you please test against 5.4.13?")
finding:       U7 (docs/dev/upstream/findings.tsv)
built from:    docs/dev/upstream/repro/U7/probe_5413_build.txt (this
               session's from-source build of tag vectorscan/5.4.13,
               commit acd7363aadea43da9c5246542d9969db843dd132)
approval:      [x] Frank approved 2026-09-27 (the tightened text below); to be posted by Frank
-->

---

Yes — I built `vectorscan/5.4.13` from source (tag commit `acd7363aadea43da9c5246542d9969db843dd132`) and ran the same repro against it directly, rather than relying on the source diff I mentioned above.

```
plain (no trailing newline)      REFUSED code -4: Unterminated comment.
plain + one trailing \n          COMPILED
```

Same result as 5.4.11. `hs_version()` reports `5.4.13 2026-09-27` from the freshly built library. Built with Ragel 6.10, Boost 1.86.0 headers, and the simde submodule at its pinned commit `416091eb…`; happy to share the exact CMake invocation if useful.
