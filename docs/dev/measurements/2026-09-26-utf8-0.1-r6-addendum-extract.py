#!/usr/bin/env python3
"""utf8@0.1 first sample at pcrec ce658cb7: the per-PATTERN mechanism
stamps R6 (docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7-addendum-
r6.md) scores, read directly off the pcrec compile rows -- the two
already-committed report TSVs cannot answer R6 at all (the addendum's
own R2-R7 file, section 7: `compile_stamp` is a per-TESTEE legend, one
row per config, not per-pattern telemetry).

Source: lane b97r6 ([B97], the R6 follow-up), 2026-09-26. Reads ONLY:
  store/records/utf8@0.1/pcrec_ce658cb7_*/*.jsonl   (streamed line by
        line; only `kind == "compile"`, `trial == 1` rows are kept, and
        only that row's own `engine_metadata` dict -- the rest of every
        line, including every `match` row, is discarded immediately
        after the one field is read, so nothing here holds more than
        76 patterns x 2 forms x 4 configs x ~40 stamp fields in memory
        at once)
  bench/utf8/patterns/*.rx                          (the raw pattern
        BYTES for the small named set this file quotes -- read through
        `pcrecbench.subbench.load`'s own `Pattern.file` path is NOT
        used here because `Pattern.text` is None for every `.rx`-file-
        sourced pattern in this set; the bytes are read directly off
        the same committed file `subbench.py` would open, never
        retyped by hand)
No measurement is run, no report is rendered, no store index is loaded.
Run from the repo root; each of the four JSONL files is 8-9 MB (54 MB
total), read once each, well under any memory concern (KB-16 is about
the WHOLE-STORE loader, `pcrecbench.report`'s own path, never touched
here).
"""
import glob
import json
import os

STORE_GLOB = "store/records/utf8@0.1/pcrec_ce658cb7_*/*.jsonl"
PAT_DIR = "bench/utf8/patterns"

SHORT = {
    "pcrec_ce658cb7_auto-caps-simdna_utf8": "auto",
    "pcrec_ce658cb7_auto-nocaps-simdna_utf8": "nocaps",
    "pcrec_ce658cb7_vm-caps-simdna_utf8": "vm",
    "pcrec_ce658cb7_vm-in-caps-simdna_utf8": "vm-in",
}


def stream_compile_rows():
    """(testee_short, pattern_id, form-or-'plain') -> engine_metadata
    dict, for trial 1 of every compile row. Refused/unsupported rows
    carry no `engine_metadata` key and are recorded as None so a caller
    can tell "no stamp" from "not read yet"."""
    out = {}
    for path in sorted(glob.glob(STORE_GLOB)):
        tid = os.path.basename(os.path.dirname(path))
        short = SHORT[tid]
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                o = json.loads(line)
                if o.get("kind") != "compile" or o.get("trial") != 1:
                    continue
                form = o.get("form") or "plain"
                out[(short, o["pattern_id"], form)] = o.get("engine_metadata")
    return out


def pat_bytes(name):
    with open(os.path.join(PAT_DIR, name + ".rx"), "rb") as fh:
        return fh.read()


ST = stream_compile_rows()
CONFIGS = ["auto", "nocaps", "vm", "vm-in"]


def stamp(cfg, pat, key, form="plain", default="(refused/unsupported)"):
    em = ST.get((cfg, pat, form))
    if em is None:
        return default
    return em.get(key, "-")


def row(pat, form, keys):
    print(f"  {pat} [{form}]  " + pat_bytes(pat).__repr__())
    for cfg in CONFIGS:
        vals = "  ".join(f"{k}={stamp(cfg, pat, k, form)}" for k in keys)
        print(f"    {cfg:8s} {vals}")


print("## 1. cls-lead-pair -- UD 6.3's own worked row: a TWO-lead-byte "
      "class (0xCE, 0xCF); the bitmap arm ('byte-class' in this set's "
      "vocabulary) must take it, memchr cannot")
row("cls-lead-pair", "plain",
    ["engine", "engine_sel", "dfa_prefilter", "dfa_prefilter_offsets",
     "prefilter", "req_byte", "req_run", "req_why"])
print("  -- control: cls-high-range (many leads, U+0100-U+2000, three "
      "distinct lead bytes 0xC4-0xE2)")
row("cls-high-range", "plain",
    ["engine", "engine_sel", "dfa_prefilter", "prefilter", "req_byte"])

print()
print("## 2. control-twin pairs that BOTH compile on pcrec (the UCP "
      "twins do not -- P5.a, unsupported-by-declaration on every "
      "pcrec-*-utf8 config)")
print("### qnt-lazy-2b / qnt-plus-2b (utf8_set_v1.md 5: \"the lazy "
      "twin -- the control pair for qnt-plus-2b\")")
for pat in ("qnt-plus-2b", "qnt-lazy-2b"):
    row(pat, "plain", ["engine", "engine_sel", "dfa_prefilter",
                        "prefilter", "req_byte", "req_run"])
print("### the ci-* fold family against its own named control, "
      "ci-ascii-control (\"the row every fold-set size above is read "
      "against\")")
for pat in ("ci-ascii-control", "ci-moskva", "ci-greek-run",
            "ci-class-range", "ci-neg-fold", "ci-strasse", "ci-sigma",
            "ci-turkish-i"):
    row(pat, "plain", ["engine", "engine_sel", "dfa_prefilter",
                        "prefilter", "req_byte", "vm_cls_folds"])

print()
print("## 3. the offset-skip population beyond P1's pair (F-C6's "
      "declared narrowing): lit-run-3, lit-mixed-ascii, alt-shared-char "
      "-- P1's own pair (lit-offset-at-head/-tail) reprinted for context")
for pat in ("lit-offset-at-head", "lit-offset-at-tail", "lit-run-3",
            "lit-mixed-ascii", "alt-shared-char"):
    row(pat, "plain", ["engine", "engine_sel", "dfa_prefilter",
                        "prefilter", "req_byte", "req_run", "req_why"])

print()
print("## 4. corpus-wide prefilter census, plain form, every compiling "
      "pattern (excluded: unicode-class-scope unsupported-by-declaration "
      "and the family-(f)/prp-ingreek refusals -- P5.a/P7.a's own "
      "populations, not re-derived here)")
ALL_PATTERNS = sorted({p for (_, p, f) in ST if f == "plain"})
for cfg in CONFIGS:
    counts = {}
    declined = []
    for pat in ALL_PATTERNS:
        em = ST.get((cfg, pat, "plain"))
        if em is None:
            continue
        key = "prefilter" if em.get("engine") == "vm" else "dfa_prefilter"
        val = em.get(key)
        if val is None:
            continue
        counts[val] = counts.get(val, 0) + 1
        if val == "none":
            declined.append(pat)
    print(f"### {cfg}: {dict(sorted(counts.items()))}")
    print(f"    declined (value 'none'), {len(declined)} of "
          f"{sum(counts.values())}: " + ", ".join(declined))

print()
print("## 5. the declined population's own pattern bytes (context for "
      "a 'strong lead-byte set' judgment -- no lead-byte histogram is "
      "computed here, see the ledger's own 'what was not read')")
seen = set()
for cfg in CONFIGS:
    for pat in ALL_PATTERNS:
        em = ST.get((cfg, pat, "plain"))
        if em is None:
            continue
        key = "prefilter" if em.get("engine") == "vm" else "dfa_prefilter"
        if em.get(key) == "none" and pat not in seen:
            seen.add(pat)
            print(f"  {pat}\t{pat_bytes(pat)!r}")
