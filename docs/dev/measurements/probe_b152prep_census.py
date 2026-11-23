"""docs/dev/measurements/probe_b152prep_census.py -- [B152] (lane b152prep,
2026-11-23, inbox I-179): STEP 2 of the compile-only census for the re-pin
cb32eda28 (abi 93) -> d6c5e71a5 (abi 112). Reads the raw emits
probe_b152prep_emit.py wrote (old, new, and the `-fno-landmark-walk` arm at
the new pin) and classifies every row.

Per row: refusal verdict; program identity v2 and v3 (tools/
program_identity.py); pcrec's own emit_bytes:code at both pins; every RX_*
stamp whose value moved; the deny arm's v3 verdict; and an ATTRIBUTION built
from markers VERIFIED in the text, one per abi family that can move a bench
row (NINETEEN steps, so the attribution is by family, never by guess):

  abi95-landmark      new RX_DFA_SCAN "landmark-walk" (and the arm differs)
  abi102-nevermatch   engine vm -> dfa with RX_DFA_SCAN "empty"
  abi103-minw         the minimum-width early-out text
                      (`subject_length - search_from < N`/`attempt_max`)
  abi104-112-reqrun   an RX_REQ_RUN / RX_REQ_WHY / RX_REQ_HANDOFF value moved,
                      or a `*reqrun*` / `*__body` pre-check chunk changed
  abi108-cover        RX_DFA_SCAN moved to "cover" (the COVER-CAP stretch)
  abi110-spanvector   a `_vs<j>` selector appears
  abi96-vlookbehind   `lb_count` / `fwd_step` appear (a refusal mover too)
  abi97-altnf         an RX_ALTCLS_* / RX_VM_ALT_ISLANDS / RX_VM_PROGRAM_BYTES
                      value moved
  other-stamp         some other RX_* value moved and no family above fired
A v3-changed row with no marker is UNATTRIBUTED (its changed chunk names are
printed so it can be read).

    python3 docs/dev/measurements/probe_b152prep_census.py EMITDIR OUT.tsv
"""
import gzip, os, re, sys
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI                          # noqa: E402

EMITDIR, OUT = sys.argv[1], sys.argv[2]
ANY_STAMP = re.compile(r'^#define (RX_[A-Z0-9_]+) (.*)$', re.M)
MINW = re.compile(r"subject_length - (search_from|scan_position) < \d+ULL|attempt_max")


def read(key, tag):
    p = os.path.join(EMITDIR, "%s.%s.gz" % (key, tag))
    if not os.path.exists(p):
        return None
    with gzip.open(p, "rt", errors="surrogateescape") as fh:
        return fh.read()


def stamps(t):
    return dict(ANY_STAMP.findall(t or ""))


def moved(a, b):
    mv = [k for k in sorted(a) if k in b and a[k] != b[k] and k != "RX_ABI"]
    mv += ["-" + k for k in sorted(a) if k not in b]
    mv += ["+" + k for k in sorted(b) if k not in a]
    return mv


def chunk_names(old, new):
    a = {c[0][:90]: "\n".join(c) for c in PI._v3_chunks(PI.normalize_v3(old).rstrip("\n").split("\n"))}
    b = {c[0][:90]: "\n".join(c) for c in PI._v3_chunks(PI.normalize_v3(new).rstrip("\n").split("\n"))}
    ch = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
    names = []
    for k in ch:
        m = re.search(r"\b(rx_?\w*)\(", k) or re.search(r"\b(rx_\w+)", k)
        names.append(m.group(1) if m else k[:30])
    return sorted(set(names))


def markers(old, new, so, sn, arm):
    m = []
    if sn.get("RX_DFA_SCAN") == '"landmark-walk"' and so.get("RX_DFA_SCAN") != '"landmark-walk"':
        m.append("abi95-landmark")
    if sn.get("RX_ENGINE") == '"dfa"' and so.get("RX_ENGINE") == '"vm"' and sn.get("RX_DFA_SCAN") == '"empty"':
        m.append("abi102-nevermatch")
    if len(MINW.findall(new)) > len(MINW.findall(old)):
        m.append("abi103-minw")
    if any(so.get(k) != sn.get(k) for k in ("RX_REQ_RUN", "RX_REQ_WHY", "RX_REQ_HANDOFF")):
        m.append("abi104-112-reqrun")
    if sn.get("RX_DFA_SCAN") == '"cover"' and so.get("RX_DFA_SCAN") != '"cover"':
        m.append("abi108-cover")
    if re.search(r"_vs\d+\b", new) and not re.search(r"_vs\d+\b", old):
        m.append("abi110-spanvector")
    if re.search(r"lb_count|fwd_step", new) and not re.search(r"lb_count|fwd_step", old):
        m.append("abi96-vlookbehind")
    if any(so.get(k) != sn.get(k) for k in ("RX_ALTCLS_MERGES", "RX_ALTCLS_FACTORED",
                                             "RX_VM_ALT_ISLANDS")):
        m.append("abi97-altnf")
    return m


def main():
    rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(EMITDIR, "index.tsv"))]
    rows = rows[1:]
    out = []
    for r in rows:
        sid, pid, cfg, form, key, old_sz, new_sz = r[:7]
        arm_sz = r[7] if len(r) > 7 else "0"
        old, new, arm = read(key, "old"), read(key, "new"), read(key, "arm_nolandmark")
        so, sn = stamps(old), stamps(new)
        if old is None and new is None:
            v2 = v3 = "refused-both"
        elif old is None or new is None:
            v2 = v3 = "refusal-mover:" + ("old-refused" if old is None else "new-refused")
        else:
            v2 = "identical" if PI.program_sha256_of_text(old) == PI.program_sha256_of_text(new) else "changed"
            v3 = "identical" if PI.normalize_v3(old) == PI.normalize_v3(new) else "changed"
        if new is None:
            armv = "-"
        elif arm is None:
            armv = "refused"
        else:
            a3 = PI.normalize_v3(arm)
            armv = "same" if a3 == PI.normalize_v3(new) else (
                "to-old" if old is not None and a3 == PI.normalize_v3(old) else "differs")
        mv = moved(so, sn) if old is not None and new is not None else []
        attr, names = "-", "-"
        if v3 == "changed":
            ms = markers(old, new, so, sn, arm)
            if not ms and mv:
                ms = ["other-stamp"]
            attr = "+".join(ms) if ms else "UNATTRIBUTED"
            names = ";".join(chunk_names(old, new))[:240]
        elif v3.startswith("refusal-mover"):
            t = new or old
            attr = "abi96-vlookbehind" if new is not None and re.search(r"lb_count|fwd_step", new) else "refusal-mover"
        out.append([sid, pid, cfg, form, v2, v3, attr, armv, names, ",".join(mv)[:400],
                    old_sz, new_sz, arm_sz,
                    so.get("RX_ENGINE", "-"), sn.get("RX_ENGINE", "-"),
                    so.get("RX_DFA_SCAN", "-"), sn.get("RX_DFA_SCAN", "-"),
                    so.get("RX_REQ_WHY", "-"), sn.get("RX_REQ_WHY", "-"),
                    sn.get("RX_REQ_HANDOFF", "-"), sn.get("RX_ENGINE_SEL", "-"),
                    sn.get("RX_DFA_PREFILTER", "-"), sn.get("RX_DFA_START", "-"),
                    sn.get("RX_TARGETS", "-")])
    cols = ["set", "pattern_id", "config", "form", "v2", "v3", "attribution", "nolandmark_arm",
            "v3_changed_chunks", "stamp_moves", "old_bytes:code", "new_bytes:code", "arm_bytes:code",
            "old_engine", "new_engine", "old_dfa_scan", "new_dfa_scan", "old_req_why", "new_req_why",
            "new_req_handoff", "new_engine_sel", "new_dfa_prefilter", "new_dfa_start", "new_targets"]
    with open(OUT, "w") as fh:
        fh.write("# probe_b152prep_census.py: cb32eda28 -> d6c5e71a5, %d rows\n" % len(out))
        fh.write("\t".join(cols) + "\n")
        for r in out:
            fh.write("\t".join(r) + "\n")
    print("rows=%d" % len(out))


if __name__ == "__main__":
    main()
