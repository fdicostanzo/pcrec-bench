"""members.py -- THE MEMBER TABLE of bench/unusual (docs/design/unusual_set_v1.md
section 2): every pattern id, its bytes, family, provenance and the oracle
route its expectations take. gen_patterns.py writes patterns/*.rx,
provenance.tsv and the sidecar's [[patterns]] array from THIS table; every
other generator reads it.

The pattern texts are NEVER typed twice: cscan is decoded from the vendored
pcrec file (vendor/pcrec/cscan.rxt, sha256 in provenance) and cross-checked
against the generator's own source string; the Onig variant is DERIVED from
cscan's text by a mechanical respelling (cscan_onig()), not retyped.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

CSCAN_RXT = os.path.join(HERE, "vendor", "pcrec", "cscan.rxt")


def decode_pattern_esc(line):
    """cscan.rxt's `pattern-esc "<escaped>"` -> bytes. The escapes the pcrec
    file uses: \\\\ \\" \\n \\t \\r \\xHH."""
    m = re.fullmatch(r'pattern-esc "(.*)"', line.rstrip("\n"), re.S)
    if not m:
        raise ValueError("not a pattern-esc line")
    s = m.group(1)
    out = bytearray()
    i = 0
    while i < len(s):
        c = s[i]
        if c != "\\":
            out += c.encode("latin-1")
            i += 1
            continue
        d = s[i + 1]
        if d == "\\":
            out.append(92); i += 2
        elif d == '"':
            out.append(34); i += 2
        elif d == "n":
            out.append(10); i += 2
        elif d == "t":
            out.append(9); i += 2
        elif d == "r":
            out.append(13); i += 2
        elif d == "x":
            out.append(int(s[i + 2:i + 4], 16)); i += 4
        else:
            raise ValueError("unknown escape \\%s" % d)
    return bytes(out)


def cscan_text():
    with open(CSCAN_RXT, "r", encoding="latin-1") as f:
        for line in f:
            if line.startswith("pattern-esc "):
                return decode_pattern_esc(line)
    raise ValueError("no pattern-esc in %s" % CSCAN_RXT)


def cscan_onig(text):
    """The declared SYNTAX-ONLY variant (3.1): Oniguruma has no
    `(?(DEFINE)...)` (its condition is a regex), so the definitions become
    `(?<name>...){0}` groups placed after the main body. Same language under
    PCRE2 (checked group-0/1 on every cscan subject), the spelling Onig reads
    as the author meant."""
    t = text.decode("latin-1")
    head, _, tail = t.partition("(?(DEFINE)\n")
    assert tail.endswith(")\n") or tail.endswith(")"), "unexpected DEFINE tail"
    body = tail.rstrip("\n")
    assert body.endswith(")")
    body = body[:-1]                              # the DEFINE's closing paren
    body = body.rstrip("\n")
    # the two definitions: `(?<sp> ... )` is one line; `(?<items> ... )` is the rest
    sp_line, _, rest = body.lstrip("\n").partition("\n")
    assert sp_line.strip().startswith("(?<sp>") and sp_line.rstrip().endswith(")")
    sp_line = sp_line.rstrip() + "{0}"
    assert rest.rstrip().endswith(")")
    rest = rest.rstrip() + "{0}"
    return (head + sp_line + "\n" + rest + "\n").encode("latin-1")


JSON_BODY = rb'''
    (?(DEFINE)
        (?<ws>      [\t\n\r ]* )
        (?<number>  -? (?: 0|[1-9]\d*) (?: \.\d+)? (?: [Ee] [+-]? \d++)? )
        (?<boolean> true | false | null )
        (?<string>  " (?: [^\\"\x00-\x1f] | \\ ["\\bfnrt\/] | \\ u [0-9A-Fa-f]{4} )* " )
        (?<pair>    (?&ws) (?&string) (?&ws) : (?&value) )
        (?<array>   \[ (?: (?&value) (?: , (?&value) )* )? (?&ws) \] )
        (?<object>  \{ (?: (?&pair) (?: , (?&pair) )* )? (?&ws) \} )
        (?<value>   (?&ws) (?: (?&number) | (?&boolean) | (?&string) | (?&array) | (?&object) ) (?&ws) )
    )
    \A (?&value) \Z
    '''

# the PHP `/sx` flags moved from the delimiters to an inline prefix
JSON_TEXT = b"(?sx)" + JSON_BODY

def json_onig(text):
    """The same declared syntax-only variant for the JSON validator: the
    DEFINE group's eight definitions become `(?<name>...){0}` after the main
    body (each definition is one line)."""
    t = text.decode("latin-1")
    pre, _, rest = t.partition("(?(DEFINE)\n")
    defs, _, post = rest.partition("\n    )\n")
    out = [pre.rstrip() + "\n", post.strip("\n").strip() + "\n"]
    for line in defs.split("\n"):
        stripped = line.rstrip()
        assert stripped.endswith(")"), line
        out.append(stripped + "{0}\n")
    return "".join(out).encode("latin-1")


SEXP_TEXT = rb"(?x)( \( ( [^()]++ | (?1) )* \) )"


class Member:
    """One pattern entry. `route` names how expectations are derived:
    plain (libpcre2), callout:<kind> (libpcre2 + callee), pass:<twin id>,
    netstr-native (host reference; the pattern is pcrec-spelled), vars (none
    yet -- L7)."""

    def __init__(self, pid, family, text, route, tags, req, prov, twin_of="",
                 role="member", size="small", isolates=""):
        self.id, self.family, self.text, self.route = pid, family, text, route
        self.tags, self.req, self.prov = tags, req, prov
        self.twin_of, self.role, self.size, self.isolates = twin_of, role, size, isolates


AUTH = dict(src="authored", url="", ref="", lic="n-a", lic_note="", fid="synthesized", adapt="", attr="")


def members():
    ct = cscan_text()
    M = []
    pcrec_prov = dict(
        src="pcrec-scandog", url="", ref="pcrec 614d45eb3 tests/recursion/cscan.rxt (introduced 66f9a8560)",
        lic="MIT", lic_note="pcrec LICENSE, Copyright (c) 2026 Frank DiCostanzo",
        fid="verbatim", adapt="pattern-esc decoded; the same bytes as gen_cscan.py's PATTERN",
        attr="pcrec lane scandog, [SCANNER-DOGFOOD]")
    M.append(Member("cscan", "recursion", ct, "cscan",
                    ["family-recursion", "hazard-none", "provenance-pcrec-scandog", "fidelity-verbatim"],
                    ["recursion", "named-groups", "conditionals", "atomic-group", "lookaround"],
                    pcrec_prov, isolates="the C (?{ ... }) end scanner: DEFINE'd subroutines, \\G, possessive loops"))
    onig_prov = dict(pcrec_prov, fid="adapted",
                     adapt="declared syntax-only variant (design 3.1): (?(DEFINE)...) respelled (?<name>...){0}, nothing else changed",
                     src="pcrec-scandog")
    M.append(Member("cscan-onig", "recursion", cscan_onig(ct), "cscan",
                    ["family-recursion", "hazard-none", "provenance-pcrec-scandog", "fidelity-adapted", "variant-syntax-only"],
                    ["recursion", "named-groups", "atomic-group", "lookaround"],
                    onig_prov, twin_of="cscan",
                    isolates="cscan with no (?(DEFINE) -- the spelling Oniguruma reads as the author meant"))
    M.append(Member("wild-sexp-balanced", "recursion", SEXP_TEXT, "plain",
                    ["family-recursion", "hazard-none", "provenance-pcre2-doc", "fidelity-adapted"],
                    ["recursion", "free-spacing", "possessive-quantifier", "captures"],
                    dict(src="pcre2-doc", url="man pcre2pattern(3) 10.46, section RECURSIVE PATTERNS",
                         ref="( \\( ( [^()]++ | (?1) )* \\) )", lic="BSD-3-Clause",
                         lic_note="libpcre2 /usr/share/doc/libpcre2-8-0/copyright (BSD-3-clause-Cambridge)",
                         fid="adapted", adapt="(?x) prepended to carry the page's stated PCRE2_EXTENDED; nothing else changed",
                         attr="PCRE2 library documentation, Philip Hazel, University of Cambridge"),
                    isolates="balanced () by numeric-group recursion with a possessive inner run"))
    M.append(Member("wild-json-validate", "recursion", JSON_TEXT, "plain",
                    ["family-recursion", "hazard-none", "provenance-stackoverflow-3845829", "fidelity-adapted"],
                    ["recursion", "named-groups", "conditionals", "free-spacing", "possessive-quantifier"],
                    dict(src="stackoverflow-3845829", url="https://stackoverflow.com/a/3845829",
                         ref="answer 3845829 by mario to question 2583472 \"Regex to validate JSON\", edited 2023-11-24",
                         lic="CC-BY-SA-4.0", lic_note="Stack Overflow content licence; attribution required",
                         fid="adapted",
                         adapt="PHP single-quoted string quoting undone (\\\\\\\\ -> \\\\); the /sx flags moved from the delimiters to the inline prefix (?sx); nothing else edited (incl. the author's \\Z, which is not \\z)",
                         attr="mario (Stack Overflow user), https://stackoverflow.com/a/3845829, CC BY-SA 4.0; see docs/dev/research/2026-10-27-b148-json-validator-source.md"),
                    size="medium", isolates="a (?(DEFINE) JSON grammar: ten subroutine calls, \\A..\\Z"))

    M.append(Member("wild-json-validate-onig", "recursion", json_onig(JSON_TEXT), "plain",
                    ["family-recursion", "hazard-none", "provenance-stackoverflow-3845829", "fidelity-adapted", "variant-syntax-only"],
                    ["recursion", "named-groups", "free-spacing", "possessive-quantifier"],
                    dict(M[3].prov, adapt=M[3].prov["adapt"] + "; then the declared syntax-only variant (design 3.1): (?(DEFINE)...) respelled (?<name>...){0}"),
                    twin_of="wild-json-validate", size="medium",
                    isolates="wild-json-validate with no (?(DEFINE) -- the spelling Oniguruma reads as the author meant"))

    # ---- callouts: real (site present), pass (site present, stub callee), twin (site removed)
    def co(pid, site_text, twin_text, kind, num, extra_req):
        base_tags = ["family-callouts", "hazard-none", "provenance-authored", "fidelity-synthesized"]
        req = ["callouts", "captures"] + extra_req
        M.append(Member(pid, "callouts", site_text, "callout:" + kind, base_tags + ["arm-real", "twin_of-" + pid], req, AUTH,
                        twin_of=pid + "-twin", isolates="callout C%d with the real callee" % num))
        M.append(Member(pid + "-pass", "callouts", site_text, "pass:" + pid + "-twin", base_tags + ["arm-pass", "twin_of-" + pid], req, AUTH,
                        twin_of=pid + "-twin", isolates="the site present, the full wrapper, a stub callee (answers equal the twin's)"))
        M.append(Member(pid + "-twin", "callouts", twin_text, "plain", base_tags + ["arm-twin", "twin_of-" + pid], ["captures"] + extra_req, AUTH,
                        isolates="the site removed, common subset"))
    co("co-luhn", rb"\b(\d{13,19})\b(?C1)", rb"\b(\d{13,19})\b", "luhn", 1, [])
    co("co-isbn", rb"\b(97[89]\d{10})\b(?C2)", rb"\b(97[89]\d{10})\b", "isbn", 2, [])
    co("co-member", rb"\buser=(\w++)(?C3)", rb"\buser=(\w+)", "member", 3, [])
    base_tags = ["family-callouts", "hazard-none", "provenance-authored", "fidelity-synthesized"]
    M.append(Member("co-netstr", "callouts", rb'(\d{1,9}):(?C"netstr,consume"),', "netstr-native",
                    base_tags + ["arm-real", "spelling-pcrec-consume", "twin_of-co-netstr"], ["callouts", "captures"], AUTH,
                    twin_of="co-netstr-twin",
                    isolates="netstrings by pcrec's consume callout (match_api 11.7); expectations by the host reference"))
    M.append(Member("co-netstr-assist", "callouts", rb"(\d{1,9}):(?>(?s:.)*?(?C4))," , "callout:netstr",
                    base_tags + ["arm-real", "spelling-assisted", "twin_of-co-netstr"], ["callouts", "captures", "atomic-group"], AUTH,
                    twin_of="co-netstr-twin",
                    isolates="netstrings by the check-at-end callee on libpcre2/Onig (design 3.2, P3); (?{4}) on Onig"))
    M.append(Member("co-netstr-twin", "callouts", rb"(\d{1,9}):", "plain",
                    base_tags + ["arm-twin", "twin_of-co-netstr"], ["captures"], AUTH,
                    isolates="a scan-cost floor only: a DIFFERENT language from the netstring (no cross-arm subtraction)"))

    # ---- vars: pattern text only (value streams and their expectations are L7's)
    vtags = ["family-vars", "hazard-none", "provenance-authored", "fidelity-synthesized"]
    M.append(Member("va-tenant", "vars", rb"^${tenant}-[0-9]{4} (?:ERROR|WARN) ", "vars", vtags, ["vars", "unusual-va-tenant"], AUTH,
                    isolates="one caller variable, per-line binding, a distinct-count ladder (3.3)"))
    M.append(Member("va-route", "vars", rb"^/${prefix:-api}/v[0-9]+/${res}${fmt+\.json}(?:\?|$)", "vars", vtags, ["vars", "unusual-va-route"], AUTH,
                    isolates="the :- and + forms with an UNSET/EMPTY distinction"))
    M.append(Member("va-term", "vars", rb"(?i)\b${term:?}\b", "vars", vtags, ["vars", "unusual-va-term"], AUTH,
                    isolates=":? refusal and as-itself values incl. metacharacters and 0x00"))
    M.append(Member("va-term-bang", "vars", rb"(?i)\b${!term:?}\b", "vars", vtags, ["vars", "unusual-va-term-bang"], AUTH,
                    isolates="va-term spelled ${!name:?} (= ${name:?}, vars.md 2)"))
    M.append(Member("floor", "floor", rb"\(\?\{", "plain",
                    ["family-floor", "hazard-none", "provenance-authored", "fidelity-synthesized"], [], AUTH,
                    role="floor", size="tiny", isolates="the per-call baseline: two literal bytes' worth of pattern"))
    return M


def check_cscan_source():
    """cscan.rxt's decoded pattern == gen_cscan.py's PATTERN (same bytes)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("gen_cscan", os.path.join(HERE, "vendor", "pcrec", "gen_cscan.py"))
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    want = g.PATTERN.strip("\n").encode("latin-1")
    got = cscan_text()
    if want != got:
        raise SystemExit("cscan.rxt's pattern-esc != gen_cscan.py PATTERN")
    return g


if __name__ == "__main__":
    check_cscan_source()
    for m in members():
        print(m.id, len(m.text))
