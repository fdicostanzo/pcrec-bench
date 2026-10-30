"""docs/dev/measurements/probe_b149prep_census.py -- [B142] (lane b149prep,
2026-10-25, inbox I-159): STEP 2 of the compile-only census for the re-pin
614d45eb3 (abi 89) -> cb32eda28 (abi 93). Reads the raw emits
probe_b149prep_emit.py wrote and classifies every row.

Per row: refusal verdict; program identity under v2 AND v3 (tools/
program_identity.py; v3 is the cross-abi-77..84 normalization: v2 reads
EVERY row changed because the find-all iterator scaffold is emitted into
every artifact); pcrec's own emit_bytes / emit_code_bytes at both pins (the
--warn-emit-bytes=1 probe); the new pin's mechanism stamps; the
`-fno-rev-end-onewalk` arm's v3 verdict against the old and the new
artifact; and, for v3-changed rows, the SIGNATURE of the change (which
top-level functions/tables differ between the folded forms).

    python3 docs/dev/measurements/probe_b149prep_census.py EMITDIR OUT.tsv
"""
import gzip, os, re, sys
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI                          # noqa: E402
from pcrecbench import subbench as _sb                  # noqa: E402

EMITDIR, OUT = sys.argv[1], sys.argv[2]
STAMPS = ("ENGINE", "ENGINE_SEL", "DFA_SCAN", "DFA_START", "DFA_PREFILTER",
          "REQ_WHY", "COMPOUND", "ITER_RETRY", "MEASURES", "FINDINGS",
          "PART_LAYOUT", "REQ_HANDOFF", "CODE_LANGS")
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


TR=re.compile(r"TRAIL_CHECK|trail_gc|trail_compact")
FUNC=re.compile(r"^static .*\b\w*trail_(gc_floor|gc_start|compact)\(")
def strip_lines(body):
    """v3-folded text -> the text with abi 93's [K134] additions removed (function bodies by brace depth,
    the macro, the checkpoint sites, the trail_gc lines); compared as SORTED lines (the fold orders chunks)."""
    lines=body.split("\n"); out=[]; i=0
    while i<len(lines):
        l=lines[i]
        if FUNC.search(l):
            d=0; started=False
            while i<len(lines):
                d+=lines[i].count("{")-lines[i].count("}")
                started=started or "{" in lines[i]
                i+=1
                if started and d==0: break
            continue
        if re.match(r"#define \w*TRAIL_CHECK\(\)",l):
            while lines[i].endswith("\\"): i+=1
            i+=1; continue
        l=re.sub(r"\{ \w*TRAIL_CHECK\(\); (goto \w+;) \}",r"\1",l)
        if TR.search(l):
            i+=1; continue
        out.append(l); i+=1
    return "\n".join(out)
def restores(new_text, old_text, norm):
    a=sorted(strip_lines(norm(new_text).rstrip("\n")).split("\n")); b=sorted(norm(old_text).rstrip("\n").split("\n"))
    return a==b


def markers(old, new):
    m = []
    if "PCREC_RX_SPAN_H" in new and "PCREC_RX_SPAN_H" not in old:
        m.append("abi90-span-helpers")
    if re.search(r"handoff_position|landmark_position", new) and \
            len(re.findall(r"handoff_position|landmark_position", new)) != \
            len(re.findall(r"handoff_position|landmark_position", old)):
        m.append("abi91-reqrun-vm")
    if re.search(r'DFA_SCAN "cover"', new) or "window_search" in new and "window_search" not in old:
        m.append("abi92-cover")
    if "wa = 128, wb = 128" in new and "wa = 128, wb = 128" not in old:
        m.append("abi92-pair-lookahead")
    if TR.search(new) and not TR.search(old):
        m.append("abi93-k134")
    return m


def attribute(v3, arm_win, arm_rh, old, new, sig):
    """The abi step(s) a v3-CHANGED row belongs to. Evidence in order:
      deny arm == new  -> not that step's; deny arm != new -> step involved;
      the text markers per step (markers());
      for abi 93, the row is attributed only if stripping the trail-gc
      text from the NEW side restores equality with the OLD side (or with
      the nowindow arm, when abi 92 also moved the row).
    Several steps may apply: they are joined with '+'. UNATTRIBUTED when no
    marker and no deny arm explains the row."""
    if v3 != "changed":
        return "-"
    ms = markers(old, new)
    if ms == ["abi93-k134"]:
        # the pure case: only the trail text differs, VERIFIED (sorted folded lines)
        return "abi93-k134" if restores(new, old, PI.normalize_v3) else "UNATTRIBUTED(k134 marker, strip does not restore)"
    if arm_win == "to-old" and "abi92-cover" not in ms:
        ms.append("abi92-cover")
    if arm_rh == "to-old" and "abi91-reqrun-vm" not in ms:
        ms.append("abi91-reqrun-vm")
    if ms:
        return "+".join(sorted(set(ms)))
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
        arm_sz = ",".join(r[7:9]) if len(r) > 8 else "0"
        old, new = read(key, "old"), read(key, "new")
        arm_w, arm_h = read(key, "arm_nowindow"), read(key, "arm_noreqhandoff")
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
        def armv(arm):
            if new is None:
                return "-"
            if arm is None:
                return "refused"
            a3 = PI.normalize_v3(arm)
            return "same" if a3 == PI.normalize_v3(new) else (
                "to-old" if old is not None and a3 == PI.normalize_v3(old) else "differs")
        owx, owh = armv(arm_w), armv(arm_h)
        st = dict(STAMP_RE.findall(new or ""))
        so = dict(STAMP_RE.findall(old or ""))
        stamp_cells = [st.get(k, "-") for k in STAMPS]
        text = SETS[sid].pattern_bytes(pid)
        attr = attribute(verdict3, owx, owh, old, new, sig) if verdict3 == "changed" else "-"
        if verdict2.startswith("refusal-mover:old") and b"(?C" in text:
            attr = "abi89-callout-compiles"
        elif verdict2.startswith("refusal-mover") and attr == "-":
            attr = "UNATTRIBUTED-refusal-mover"
        moves = stamp_moves(old, new) if old is not None and new is not None else "-"
        out.append([sid, pid, cfg, form, verdict2, verdict3, attr, owx, owh, sig, str(nch), moves,
                    old_sz, new_sz, arm_sz,
                    so.get("ENGINE", "-"), so.get("ENGINE_SEL", "-"),
                    so.get("DFA_SCAN", "-"), so.get("DFA_START", "-"),
                    so.get("DFA_PREFILTER", "-")] + stamp_cells)
    cols = ["set", "pattern_id", "config", "form", "v2", "v3", "attribution", "nowindow_arm", "noreqhandoff_arm", "v3_signature",
            "v3_nchunks", "stamp_moves", "old_bytes:code", "new_bytes:code", "arm_bytes:code(nowindow,noreqhandoff)",
            "old_engine", "old_engine_sel", "old_dfa_scan", "old_dfa_start", "old_dfa_prefilter"] \
        + ["new_" + k.lower() for k in STAMPS]
    with open(OUT, "w") as fh:
        fh.write("# probe_b149prep_census.py: 9ae59f5d4 -> 614d45eb3, %d rows\n" % len(out))
        fh.write("\t".join(cols) + "\n")
        for r in out:
            fh.write("\t".join(r) + "\n")
    print("rows=%d" % len(out))


if __name__ == "__main__":
    main()
