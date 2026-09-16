#!/usr/bin/env python3
"""The O-29 (+ K57) VERIFY CHAIN against pcrec's fix pin.

[B42] runbook step 3 (inbox I-71: the fix pin is `a770139e`). Reproduces
outbox O-29 (`docs/dev/outbox_to_pcrec.md`, "## O-29") at the FIXED pin --
the multi-block `--list-source` silent-loss defect (a block's own
`#section provenance`/`variants` row dropped whenever a BLANK or COMMENT
line closes it, not only "every block but the last") -- and I-71 item 2's
K57 lift (a block-scalar `|` continuation shallower than the first
line's own dedent depth now refuses BY NAME, class `value-shape`).

Four lettered probes, each PASS/FAIL with evidence, plus one extra check
(the loader gate flip `pcrecbench.rxt_source.load_rxt_source` was built to
refuse on, per its own KNOWN GAP note):

  (a) the O-29 minimal repro: three pattern blocks, each with its own
      five-line `provenance` sub-block, tag-BEFORE-provenance (the
      reproducing order per the O-29 addendum), a trailing blank line at
      EOF (the EOF-adjacent case I-71 names) -- must emit 3/3 `#section
      provenance` rows with correct per-block attribution; plus the
      `variant` twin (two blocks, one `variant re2` sub-block each) --
      must emit 2/2 `#section variants` rows.
  (b) the corpus dump: `bench/capability/patterns.rxt` (64 blocks) must
      emit 64 `#section provenance` rows and as many `#section variants`
      rows as `bench/capability/variants.tsv` declares (0 data rows
      today), exit 0. Also demonstrates the LOADER GATE FLIP:
      `pcrecbench.rxt_source.load_rxt_source` refuses this same file at
      the PRE-FIX pin (`check_provenance_agreement`, citing O-29) and
      loads cleanly at the fix pin -- the two-sided control I-71's "loader
      gate refuse -> load" step asks for.
  (c) one multi-block fixture carrying all FOUR `#section` kinds
      (provenance, variants, cases, aux) across two blocks plus one
      file-scope `ext` block -- every kind's rows present for every block
      that declares them; plus B3's NUL refusal (a raw NUL byte in a
      `pattern` line refused by name, class `value-shape`) with its
      NUL-free control.
  (d) the K57 positive witness: a head `description |` block scalar whose
      SECOND continuation line is indented LESS than the first (which set
      the dedent depth) is refused by name, class `value-shape`; the
      compliant-depth control loads clean.

Every probe states its FAILING DIRECTION -- what the pre-fix binary
(cd371441) actually prints, quoted from `docs/dev/outbox_to_pcrec.md`
"## O-29" / `docs/dev/measurements/2026-09-16-b42-acceptance-41-cd371441.txt`
B3/K57's own prior wording -- so a reader need not re-run the old binary
to see what "still broken" would have looked like.

NOTHING HERE IS A TIMING: every pcrec invocation is `--list-source` on a
fixture of at most a few dozen lines, single-digit milliseconds. No
compile, no artifact, no driver, no engine run -- the box's load cannot
affect a character of this file's output (docs/dev/measurements/
CLAUDE.md rule 3's one stated exception, same as probe_rxt_format.py's).

    python3 docs/dev/measurements/probe_o29_verify.py [PCREC_BIN]

Defaults to the pin's own binary under `build/`; a positional argv[1]
overrides it (this lane's own convention, since two named pins --
the fix and its pre-fix control -- are both read in one run).
Fixtures land in a FIXED directory (`$TMPDIR/o29probe`, emptied each
run) so pcrec's path-quoting diagnostics never put a random component
in the archive, same rule as `probe_rxt_format.py`.
"""

import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
FIX_PIN_REL = os.path.join("build", "pcrec-a770139e", "build", "pcrec")
PREFIX_PIN_REL = os.path.join("build", "pcrec-cd371441", "build", "pcrec")
CORPUS_REL = os.path.join("bench", "capability", "patterns.rxt")
VARIANTS_TSV_REL = os.path.join("bench", "capability", "variants.tsv")


def _resolve(rel):
    """Same git-common-dir fallback probe_rxt_format.py's default_bin()
    uses: `build/` lives in the MAIN checkout, so a run from a worktree
    still finds it."""
    cands = [os.path.join(ROOT, rel)]
    try:
        common = subprocess.run(
            ["git", "-C", ROOT, "rev-parse", "--git-common-dir"],
            capture_output=True, text=True).stdout.strip()
        if common:
            if not os.path.isabs(common):
                common = os.path.join(ROOT, common)
            cands.append(os.path.join(os.path.dirname(common), rel))
    except Exception:                                             # noqa: BLE001
        pass
    for c in cands:
        if os.path.exists(c):
            return c
    return cands[0]


def default_fix_bin():
    return _resolve(FIX_PIN_REL)


def default_prefix_bin():
    return _resolve(PREFIX_PIN_REL)


TMP = os.path.join(tempfile.gettempdir(), "o29probe")


def write_fixture(name, body_bytes):
    path = os.path.join(TMP, name)
    with open(path, "wb") as f:
        f.write(body_bytes)
    return path


def run_list_source(binary, path, timeout=60):
    return subprocess.run([binary, "--list-source", path],
                           capture_output=True, timeout=timeout)


def parse_dump(stdout_bytes):
    """Minimal, self-contained TSV-dump reader (independent of
    `pcrecbench.rxt_source.parse_list_source`, on this file's own rule of
    sharing no source with a control it is meant to be a check on) --
    `(main_cols, main_rows, sections)`, `sections` a dict of
    `{name: (cols, rows-as-dicts)}`."""
    text = stdout_bytes.decode("utf-8", errors="surrogateescape")
    main_cols = None
    main_rows = []
    sections = {}
    cur_name = None
    cur_cols = None
    for line in text.split("\n"):
        if not line:
            continue
        if line.startswith("#section "):
            cur_name = line[len("#section "):].strip()
            cur_cols = None
            sections.setdefault(cur_name, (None, []))
            continue
        if line.startswith("#kind"):
            main_cols = line[1:].split("\t")
            continue
        if line.startswith("#line"):
            cur_cols = line[1:].split("\t")
            if cur_name is not None:
                sections[cur_name] = (cur_cols, sections[cur_name][1])
            continue
        if line.startswith("#"):
            continue
        fields = line.split("\t")
        if cur_name is not None and cur_cols is not None:
            sections[cur_name][1].append(dict(zip(cur_cols, fields)))
        elif main_cols is not None:
            main_rows.append(dict(zip(main_cols, fields)))
    return main_cols, main_rows, sections


PASS, FAIL = "PASS", "FAIL"
results = []


def record(pid, desc, ok, evidence_lines, pre_fix_note):
    results.append((pid, desc, ok))
    print("=== %s: %s -- %s" % (pid, desc, PASS if ok else FAIL))
    for line in evidence_lines:
        print("    %s" % line)
    print("    pre-fix (what O-29's own symptom looks like): %s" % pre_fix_note)
    print()


# ------------------------------------------------------------- (a) repro

PROV3_FIXTURE = b"""pattern p1x
name p1
tag family=wild
provenance
  source authored
  retrieved 2026-09-16
  license n-a
  fidelity synthesized
  adaptation the probe's own rewrite text

pattern p2x
name p2
tag family=wild
provenance
  source authored
  retrieved 2026-09-16
  license n-a
  fidelity synthesized
  adaptation the probe's own rewrite text

pattern p3x
name p3
tag family=wild
provenance
  source authored
  retrieved 2026-09-16
  license n-a
  fidelity synthesized
  adaptation the probe's own rewrite text

"""

VARIANT2_FIXTURE = b"""pattern v1x
name v1
variant re2
  unsupported no backrefs

pattern v2x
name v2
variant re2
  unsupported no backrefs

"""


def probe_a(binary):
    path = write_fixture("a_prov3.rxt", PROV3_FIXTURE)
    r = run_list_source(binary, path)
    _, main_rows, sections = parse_dump(r.stdout)
    prov_rows = sections.get("provenance", (None, []))[1]
    names = sorted(row.get("block_name") for row in prov_rows)
    ok = (r.returncode == 0 and len(prov_rows) == 3
          and names == ["p1", "p2", "p3"])
    ev = ["fixture: %s (3 pattern blocks, tag-before-provenance, trailing blank at EOF)" % path,
          "exit: %d" % r.returncode,
          "#section provenance rows: %d (want 3)" % len(prov_rows),
          "block_name attribution: %r (want ['p1', 'p2', 'p3'])" % names]
    record("a-repro", "O-29 minimal repro: 3 blocks each with their own provenance sub-block",
           ok, ev,
           "exactly ONE #section provenance row (p3's only) -- O-29's own report, "
           "\"the other blocks' rows are silently absent -- no error, exit 0\"")

    path2 = write_fixture("a_variant2.rxt", VARIANT2_FIXTURE)
    r2 = run_list_source(binary, path2)
    _, _, sections2 = parse_dump(r2.stdout)
    var_rows = sections2.get("variants", (None, []))[1]
    names2 = sorted(row.get("block_name") for row in var_rows)
    ok2 = (r2.returncode == 0 and len(var_rows) == 2 and names2 == ["v1", "v2"])
    ev2 = ["fixture: %s (2 blocks each declaring 'variant re2')" % path2,
           "exit: %d" % r2.returncode,
           "#section variants rows: %d (want 2)" % len(var_rows),
           "block_name attribution: %r (want ['v1', 'v2'])" % names2]
    record("a-variant-twin", "O-29 variant twin: 2 blocks each with their own variant sub-block",
           ok2, ev2,
           "only the second block's row -- O-29: \"same shape for variant: two blocks each "
           "declaring variant re2 -> only the second block's row\"")
    return ok and ok2


# --------------------------------------------------------------- (b) corpus

def probe_b(binary):
    corpus = os.path.join(ROOT, CORPUS_REL)
    r = run_list_source(binary, corpus)
    main_cols, main_rows, sections = parse_dump(r.stdout)
    n_blocks = sum(1 for row in main_rows if row.get("kind") in ("pattern", "pattern-esc"))
    prov_rows = sections.get("provenance", (None, []))[1]
    var_rows = sections.get("variants", (None, []))[1]
    variants_tsv = os.path.join(ROOT, VARIANTS_TSV_REL)
    with open(variants_tsv) as f:
        lines = [l for l in f.read().splitlines()[1:] if l.strip()]
    declared_variants = len(lines)
    ok = (r.returncode == 0 and len(prov_rows) == n_blocks
          and len(var_rows) == declared_variants)
    ev = ["corpus: %s" % CORPUS_REL,
          "exit: %d" % r.returncode,
          "pattern blocks (kind in {pattern, pattern-esc}): %d" % n_blocks,
          "#section provenance rows: %d (want == block count %d)" % (len(prov_rows), n_blocks),
          "#section variants rows: %d (want == %s data rows %d)"
          % (len(var_rows), VARIANTS_TSV_REL, declared_variants)]
    record("b-corpus", "the 64-block corpus dump: provenance == block count, variants == variants.tsv",
           ok, ev,
           "ONE #section provenance row total (the last pattern's); the other 63 are gone -- "
           "O-29: \"our committed 64-block bench/capability/patterns.rxt dumps ONE provenance "
           "row total\"")

    # The loader gate flip: pcrecbench.rxt_source.load_rxt_source refuses
    # this same file at the PRE-FIX pin and loads cleanly at the fix pin --
    # the two-sided control I-71's "loader gate refuse -> load" step asks
    # for. Imported lazily so a caller missing pcrecbench on sys.path still
    # gets probes (a)/(c)/(d).
    sys.path.insert(0, ROOT)
    from pcrecbench.rxt_source import load_rxt_source, RxtSourceError  # noqa: E402
    prefix_bin = default_prefix_bin()
    gate_ok = True
    gate_ev = []
    if os.path.exists(prefix_bin):
        try:
            load_rxt_source(CORPUS_REL if os.path.isabs(CORPUS_REL) else corpus,
                             pcrec_bin=prefix_bin)
            gate_ok = False
            gate_ev.append("PRE-FIX (%s): loaded cleanly -- expected a refusal citing O-29"
                           % os.path.basename(os.path.dirname(os.path.dirname(prefix_bin))))
        except RxtSourceError as e:
            gate_ev.append("PRE-FIX (%s): REFUSED as expected -- %s"
                           % (os.path.basename(os.path.dirname(os.path.dirname(prefix_bin))),
                              str(e)[:200]))
    else:
        gate_ev.append("PRE-FIX binary not present at %s -- skipped (not fatal to this probe)"
                       % prefix_bin)
    try:
        src = load_rxt_source(corpus, pcrec_bin=binary)
        gate_ev.append("FIX (%s): loaded cleanly -- %d patterns, %d provenance, %d variants"
                       % (os.path.basename(os.path.dirname(os.path.dirname(binary))),
                          len(src.patterns), len(src.provenance), len(src.variants)))
    except RxtSourceError as e:
        gate_ok = False
        gate_ev.append("FIX (%s): REFUSED -- %s" % (binary, str(e)[:300]))
    record("b-loader-gate", "the loader gate flip: refuse (pre-fix) -> load (fix), same corpus file",
           gate_ok, gate_ev,
           "pcrecbench.rxt_source.check_provenance_agreement refuses the whole load, citing O-29, "
           "at any pin whose provenance-row count is strictly between 0 and the block count")
    return ok and gate_ok


# ------------------------------------------------------------ (c) kinds + NUL

KINDS_FIXTURE = b"""ext bench
  roster pcre2 re2

pattern c1x
name c1
tag family=wild
provenance
  source authored
  retrieved 2026-09-16
  license n-a
  fidelity synthesized
  adaptation probe text one
variant re2
  unsupported no backrefs
ext block
  note c1 aux data
m "c1x" 0 3
n "zzzzzz"

pattern c2x
name c2
tag family=wild
provenance
  source authored
  retrieved 2026-09-16
  license n-a
  fidelity synthesized
  adaptation probe text two
variant re2
  unsupported no backrefs
ext block
  note c2 aux data
mc "c2xc2x" 2

"""

NUL_FIXTURE = b"pattern ab\x00cd\nname h\n"
NUL_CONTROL = b"pattern abcd\nname h\n"


def probe_c(binary):
    path = write_fixture("c_kinds.rxt", KINDS_FIXTURE)
    r = run_list_source(binary, path)
    _, main_rows, sections = parse_dump(r.stdout)
    prov_names = sorted(row.get("block_name") for row in sections.get("provenance", (None, []))[1])
    var_names = sorted(row.get("block_name") for row in sections.get("variants", (None, []))[1])
    case_names = sorted(set(row.get("block_name") for row in sections.get("cases", (None, []))[1]))
    aux_rows = sections.get("aux", (None, []))[1]
    aux_blocks = sorted(set(row.get("block_name") for row in aux_rows if row.get("block_name")))
    aux_file_scope = any(not row.get("block_name") for row in aux_rows)
    ok = (r.returncode == 0
          and prov_names == ["c1", "c2"]
          and var_names == ["c1", "c2"]
          and case_names == ["c1", "c2"]
          and aux_blocks == ["c1", "c2"]
          and aux_file_scope)
    ev = ["fixture: %s (2 blocks x {provenance, variant, cases, block-scope ext} + 1 file-scope ext)" % path,
          "exit: %d" % r.returncode,
          "#section provenance block_names: %r (want ['c1', 'c2'])" % prov_names,
          "#section variants   block_names: %r (want ['c1', 'c2'])" % var_names,
          "#section cases      block_names: %r (want ['c1', 'c2'])" % case_names,
          "#section aux block-scope names: %r (want ['c1', 'c2']); file-scope row present: %s"
          % (aux_blocks, aux_file_scope)]
    record("c-kinds", "all four #section kinds present for every block that declares them",
           ok, ev,
           "provenance/variants would each show only c2's row (the textually-last block); "
           "cases and aux are unaffected -- O-29: \"the flat per-line case productions "
           "(m/n/mc) are unaffected (all blocks' cases appear)\"")

    nul_path = write_fixture("c_nul.rxt", NUL_FIXTURE)
    rn = run_list_source(binary, nul_path)
    nul_ok = (rn.returncode != 0
              and b"value-shape" in rn.stderr
              and b"NUL" in rn.stderr)
    ev_nul = ["fixture: %r" % NUL_FIXTURE,
              "exit: %d (want != 0)" % rn.returncode,
              "stderr: %s" % rn.stderr.decode("utf-8", "replace").strip()]
    record("c-nul-refused", "B3: a raw NUL byte in a pattern line is refused BY NAME",
           nul_ok, ev_nul,
           "n/a -- this is the FLAGSHIP fix already confirmed at cd371441 "
           "(2026-09-16-b42-acceptance-41-cd371441.txt B3); reconfirmed here at the O-29 fix pin "
           "as a control that the fix did not regress it")

    ctrl_path = write_fixture("c_nul_control.rxt", NUL_CONTROL)
    rc = run_list_source(binary, ctrl_path)
    ctrl_ok = rc.returncode == 0
    record("c-nul-control", "control: the same fixture with no NUL byte accepts cleanly",
           ctrl_ok, ["fixture: %r" % NUL_CONTROL, "exit: %d (want 0)" % rc.returncode],
           "n/a -- negative control")
    return ok and nul_ok and ctrl_ok


# --------------------------------------------------------------- (d) K57

K57_BAD = b"description |\n  first line\n second\npattern abc\nname h\n"
K57_GOOD = b"description |\n  first line\n  second\npattern abc\nname h\n"


def probe_d(binary):
    bad_path = write_fixture("d_k57_bad.rxt", K57_BAD)
    rb = run_list_source(binary, bad_path)
    bad_ok = (rb.returncode != 0 and b"value-shape" in rb.stderr)
    record("d-k57-witness",
           "K57: a block-scalar continuation shallower than the first line's depth refuses, class value-shape",
           bad_ok,
           ["fixture: %r (first continuation at depth 2, second at depth 1)" % K57_BAD,
            "exit: %d (want != 0)" % rb.returncode,
            "stderr: %s" % rb.stderr.decode("utf-8", "replace").strip()],
           "loads cleanly with the shallower line silently truncated to depth 2's byte count "
           "(inbox I-68 item 3's parked caveat, lifted by this pin per I-71 item 2)")

    good_path = write_fixture("d_k57_control.rxt", K57_GOOD)
    rg = run_list_source(binary, good_path)
    good_ok = rg.returncode == 0
    record("d-k57-control", "control: the same block scalar at compliant (equal) depth loads clean",
           good_ok,
           ["fixture: %r" % K57_GOOD, "exit: %d (want 0)" % rg.returncode],
           "n/a -- negative control")
    return bad_ok and good_ok


def main():
    binary = sys.argv[1] if len(sys.argv) > 1 else default_fix_bin()
    if not os.path.exists(binary):
        print("no pcrec binary at %s (pass one as argv[1])" % binary, file=sys.stderr)
        return 1
    pin = os.path.basename(os.path.dirname(os.path.dirname(binary)))
    bench = subprocess.run(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"],
                           capture_output=True, text=True).stdout.strip()
    print("# O-29 (+K57) verify chain -- PARSE ONLY, no timing")
    print("# binary:  %s" % binary)
    print("# pin:     %s" % pin)
    print("# bench:   %s  (the one field a re-run may differ on)" % (bench or "unknown"))
    print("# script:  docs/dev/measurements/probe_o29_verify.py")
    print("# for:     [B42] runbook step 3 (inbox I-71: O-29 fix pin a770139e)")
    print()

    shutil.rmtree(TMP, ignore_errors=True)
    os.makedirs(TMP)

    ok_a = probe_a(binary)
    ok_b = probe_b(binary)
    ok_c = probe_c(binary)
    ok_d = probe_d(binary)

    print("# ============================================================")
    print("# SUMMARY")
    print("# ============================================================")
    n_pass = sum(1 for _, _, ok in results if ok)
    for pid, desc, ok in results:
        print("# %-16s %-4s  %s" % (pid, PASS if ok else FAIL, desc))
    print("# %d/%d PASS" % (n_pass, len(results)))
    print("# fixtures written under %s (fixed name, emptied each run)" % TMP)
    overall = ok_a and ok_b and ok_c and ok_d
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
