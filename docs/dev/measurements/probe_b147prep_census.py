"""docs/dev/measurements/probe_b147prep_census.py -- [B142] (lane b147prep,
2026-10-25, inbox I-159): STEP 2 of the compile-only census for the re-pin
6b2dbd3e (abi 76) -> 9ae59f5d4 (abi 84). Reads the raw emits
probe_b147prep_emit.py wrote and classifies every row.

Per row: refusal verdict; program identity under v2 AND v3 (tools/
program_identity.py; v3 is the cross-abi-77..84 normalization: v2 reads
EVERY row changed because the find-all iterator scaffold is emitted into
every artifact); pcrec's own emit_bytes / emit_code_bytes at both pins (the
--warn-emit-bytes=1 probe); the new pin's mechanism stamps; the
`-fno-rev-end-onewalk` arm's v3 verdict against the old and the new
artifact; and, for v3-changed rows, the SIGNATURE of the change (which
top-level functions/tables differ between the folded forms).

    python3 docs/dev/measurements/probe_b147prep_census.py EMITDIR OUT.tsv
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


SCAN_FAMILY = {"rx_search", "rx_prefilter", "rx_match", "rx_forward_is_stop", "rx_reverse_is_stop",
               "rx_anchored_is_stop"}
LIT_RE = re.compile(r'"(?:\\.|[^"\\\n])*"')
ESC = {"\\t": "\\011", "\\n": "\\012", "\\r": "\\015"}


def lit_canon(text):
    """[EMIT-BIDI] (abi 86): string literals keep octal but spell tab / newline /
    carriage return as \\t \\n \\r (same string value). Respell every such
    escape inside a string literal back to octal on BOTH sides."""
    def fix(m):
        s = m.group(0)
        for k, v in ESC.items():
            s = s.replace(k, v)
        return s
    return LIT_RE.sub(fix, text)


def edges(text):
    return text.count("SCAN EDGE:")


def attribute(v3, owx, old, new, sig):
    """The abi step a v3-CHANGED row belongs to, by rule:
      abi86-emit-bidi      identical once string-literal escapes are respelled
                           to one form (the comment text never reaches the hash);
      abi87-scanedge-set   the -fno-scan-edge arm restores the old program, OR
                           the only changed functions are the scan family and
                           the scan-edge count moved;
      UNATTRIBUTED         anything else (the census's failure condition)."""
    if v3 != "changed":
        return "-"
    if PI.normalize_v3(lit_canon(old)) == PI.normalize_v3(lit_canon(new)):
        return "abi86-emit-bidi"
    if owx == "to-old":
        return "abi87-scanedge-set"
    fns = set(sig.split(";")) if sig and sig != "-" else set()
    if fns and fns <= SCAN_FAMILY and edges(new) != edges(old):
        return "abi87-scanedge-set"
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
        arm = read(key, "arm_noedge")
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
        attr = attribute(verdict3, owx, old, new, sig) if verdict3 == "changed" else "-"
        if verdict2.startswith("refusal-mover:old") and b"(?C" in text:
            attr = "abi89-callout-compiles"
        moves = stamp_moves(old, new) if old is not None and new is not None else "-"
        out.append([sid, pid, cfg, form, verdict2, verdict3, attr, owx, sig, str(nch), moves,
                    old_sz, new_sz, arm_sz,
                    so.get("ENGINE", "-"), so.get("ENGINE_SEL", "-"),
                    so.get("DFA_SCAN", "-"), so.get("DFA_START", "-"),
                    so.get("DFA_PREFILTER", "-")] + stamp_cells)
    cols = ["set", "pattern_id", "config", "form", "v2", "v3", "attribution", "noedge_arm", "v3_signature",
            "v3_nchunks", "stamp_moves", "old_bytes:code", "new_bytes:code", "arm_bytes:code",
            "old_engine", "old_engine_sel", "old_dfa_scan", "old_dfa_start", "old_dfa_prefilter"] \
        + ["new_" + k.lower() for k in STAMPS]
    with open(OUT, "w") as fh:
        fh.write("# probe_b147prep_census.py: 9ae59f5d4 -> 614d45eb3, %d rows\n" % len(out))
        fh.write("\t".join(cols) + "\n")
        for r in out:
            fh.write("\t".join(r) + "\n")
    print("rows=%d" % len(out))


if __name__ == "__main__":
    main()
