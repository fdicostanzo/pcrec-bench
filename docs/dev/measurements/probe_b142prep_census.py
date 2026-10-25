"""docs/dev/measurements/probe_b142prep_census.py -- [B142] (lane b142prep,
2026-10-25, inbox I-159): STEP 2 of the compile-only census for the re-pin
6b2dbd3e (abi 76) -> 9ae59f5d4 (abi 84). Reads the raw emits
probe_b142prep_emit.py wrote and classifies every row.

Per row: refusal verdict; program identity under v2 AND v3 (tools/
program_identity.py; v3 is the cross-abi-77..84 normalization: v2 reads
EVERY row changed because the find-all iterator scaffold is emitted into
every artifact); pcrec's own emit_bytes / emit_code_bytes at both pins (the
--warn-emit-bytes=1 probe); the new pin's mechanism stamps; the
`-fno-rev-end-onewalk` arm's v3 verdict against the old and the new
artifact; and, for v3-changed rows, the SIGNATURE of the change (which
top-level functions/tables differ between the folded forms).

    python3 docs/dev/measurements/probe_b142prep_census.py EMITDIR OUT.tsv
"""
import gzip, os, re, sys
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI                          # noqa: E402
from pcrecbench import subbench as _sb                  # noqa: E402

EMITDIR, OUT = sys.argv[1], sys.argv[2]
STAMPS = ("ENGINE", "ENGINE_SEL", "DFA_SCAN", "DFA_START", "DFA_PREFILTER",
          "REQ_WHY", "COMPOUND", "ITER_RETRY", "MEASURES", "FINDINGS",
          "PART_LAYOUT")
STAMP_RE = re.compile(r'^#define RX_(%s) (.*)$' % "|".join(STAMPS), re.M)


def read(key, tag):
    p = os.path.join(EMITDIR, "%s.%s.gz" % (key, tag))
    if not os.path.exists(p):
        return None
    with gzip.open(p, "rt", errors="surrogateescape") as fh:
        return fh.read()


ANY_STAMP = re.compile(r'^#define (RX_[A-Z0-9_]+) (.*)$', re.M)


def stamp_moves(old, new):
    """Names of the RX_* stamp macros present on BOTH sides whose VALUE
    differs, plus `+NAME` for one stamped only at the new pin. Stamps do not
    reach the identity hash (v2 rule 5 drops an unreferenced macro), so a
    stamp whose value moved with no code change is invisible there."""
    a, b = dict(ANY_STAMP.findall(old)), dict(ANY_STAMP.findall(new))
    mv = [k for k in sorted(a) if k in b and a[k] != b[k] and k != "RX_ABI"]
    mv += ["-" + k for k in sorted(a) if k not in b]
    mv += ["+" + k for k in sorted(b) if k not in a]
    return ",".join(mv)


def folded_chunks(text):
    """v3-folded text -> {chunk head line: chunk text} (a table or a
    function, keyed by its first line) for the signature."""
    out = {}
    for i, c in enumerate(PI.normalize_v3(text).rstrip("\n").split("\n")):
        pass
    body = PI.normalize_v3(text).rstrip("\n")
    chunks = PI._v3_chunks(body.split("\n"))
    for c in chunks:
        out.setdefault(c[0][:90], "\n".join(c))
    return out


def signature(old, new):
    a, b = folded_chunks(old), folded_chunks(new)
    ch = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
    names = []
    for k in ch:
        m = re.search(r"\b(rx_?\w*)\(", k) or re.search(r"\b(rx_\w+)", k)
        names.append(m.group(1) if m else k[:30])
    return ";".join(sorted(set(names)))[:200], len(ch)


OPTION_RUN = re.compile(rb"^\(\?[A-Za-z^-]+\)")


def attribute(sid, pid, v3, owx, compound, engine, text):
    """The abi step / change a v3-CHANGED row belongs to, by rule (each rule
    is checked by value in tools/selfcheck.py check_b142_stamps):
      rev-end-mark   the `-fno-rev-end-onewalk` arm restores the old program;
      compound       the artifact is a COMPOUND (abi 77);
      flag-spell     a VM program that lost a dead label, whose pattern
                     STARTS with an option run -- [FLAG-SPELL] (pcrec
                     flagfix, merged WITHOUT an abi bump);
      k128           a VM program that grew by a guard, pattern with a
                     nullable body under an unbounded mandatory repeat
                     (abi 83);
      UNATTRIBUTED   anything else (the census's failure condition)."""
    if v3 != "changed":
        return "-"
    if owx == "to-old":
        return "abi78-rev-end-mark"
    if compound == "split":
        return "abi77-compound"
    if engine == "vm" and OPTION_RUN.match(text):
        return "flag-spell(no-abi)"
    if engine == "vm" and b")*)+" in text:
        return "abi83-k128"
    return "UNATTRIBUTED"


SETS = {}
for _d in sorted(os.listdir("bench")):
    if os.path.isfile(os.path.join("bench", _d, "subbench.toml")):
        _x = _sb.find(_d)
        SETS[_x.id] = _x


def main():
    rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(EMITDIR, "index.tsv"))]
    hdr, rows = rows[0], rows[1:]
    out = []
    for r in rows:
        sid, pid, cfg, form, key, old_sz, new_sz = r[:7]
        arm_sz = r[7] if len(r) > 7 else "0"
        old, new = read(key, "old"), read(key, "new")
        arm = read(key, "arm_onewalk")
        if old is None and new is None:
            verdict2 = verdict3 = "refused-both"
        elif old is None or new is None:
            verdict2 = verdict3 = "refusal-mover:" + ("old" if old is None else "new")
        else:
            h2o, h2n = PI.program_sha256_of_text(old), PI.program_sha256_of_text(new)
            verdict2 = "identical" if h2o == h2n else "changed"
            n3o, n3n = PI.normalize_v3(old), PI.normalize_v3(new)
            verdict3 = "identical" if n3o == n3n else "changed"
        sig, nch = ("-", 0)
        if verdict3 == "changed":
            sig, nch = signature(old, new)
        owx = "-"
        if new is not None:
            if arm is None:
                owx = "refused"
            else:
                a3 = PI.normalize_v3(arm)
                n3n = PI.normalize_v3(new)
                owx = "same" if a3 == n3n else ("to-old" if old is not None and
                                                 a3 == PI.normalize_v3(old) else "differs")
        st = dict(STAMP_RE.findall(new or ""))
        so = dict(STAMP_RE.findall(old or ""))
        stamp_cells = [st.get(k, "-") for k in STAMPS]
        text = SETS[sid].pattern_bytes(pid)
        attr = attribute(sid, pid, verdict3, owx, st.get("COMPOUND", "").strip('"'),
                         st.get("ENGINE", "").strip('"'), text)
        moves = stamp_moves(old, new) if old is not None and new is not None else "-"
        out.append([sid, pid, cfg, form, verdict2, verdict3, attr, owx, sig, str(nch), moves,
                    old_sz, new_sz, arm_sz,
                    so.get("ENGINE", "-"), so.get("ENGINE_SEL", "-"),
                    so.get("DFA_SCAN", "-"), so.get("DFA_START", "-"),
                    so.get("DFA_PREFILTER", "-")] + stamp_cells)
    cols = ["set", "pattern_id", "config", "form", "v2", "v3", "attribution", "onewalk_arm", "v3_signature",
            "v3_nchunks", "stamp_moves", "old_bytes:code", "new_bytes:code", "arm_bytes:code",
            "old_engine", "old_engine_sel", "old_dfa_scan", "old_dfa_start", "old_dfa_prefilter"] \
        + ["new_" + k.lower() for k in STAMPS]
    with open(OUT, "w") as fh:
        fh.write("# probe_b142prep_census.py: 6b2dbd3e -> 9ae59f5d4, %d rows\n" % len(out))
        fh.write("\t".join(cols) + "\n")
        for r in out:
            fh.write("\t".join(r) + "\n")
    print("rows=%d" % len(out))


if __name__ == "__main__":
    main()
