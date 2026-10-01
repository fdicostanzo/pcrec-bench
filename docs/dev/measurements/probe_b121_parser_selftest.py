"""docs/dev/measurements/probe_b121_parser_selftest.py -- [B121] the
SELF-TEST pcre_mini_parser.py's own docstring promises: parses every
bench/*/patterns/*.rx pattern (by subbench_dirs() enumeration, the same
discovery tools/selfcheck.py uses) and, for every one that parses
cleanly, runs check_no_caret_in_opaque (no '^' silently swallowed by an
unhandled construct) plus a cross-check against the dumb independent
text scan all_carets_text (every Caret the real parser finds is a '^'
byte in the text, and vice versa modulo the one documented exception,
\\Q...\\E quoting). A pattern the parser cannot parse at all is reported
BY NAME, not silently skipped -- the two asks that depend on this
parser (A2/Q7, A3/Q6) must know their own corpus coverage."""
import os
import sys

sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pcrecbench import subbench as _sb
import pcre_mini_parser as M


def subbench_dirs():
    root = os.path.join(os.getcwd(), "bench")
    out = []
    for name in sorted(os.listdir(root)):
        path = os.path.join(root, name)
        if os.path.exists(os.path.join(path, "subbench.toml")):
            out.append((name, path))
    return out


def main():
    total = 0
    parse_failed = []
    opaque_failed = []
    crosscheck_mismatch = []
    for name, _path in subbench_dirs():
        sb = _sb.find(name)
        for p in sb.patterns:
            total += 1
            raw = sb.pattern_bytes(p.name)
            text = raw.decode("latin-1")
            try:
                alt = M.parse(text)
            except M.ParseError as e:
                parse_failed.append((name, p.name, str(e)))
                continue
            try:
                M.check_no_caret_in_opaque(text, alt)
            except M.ParseError as e:
                opaque_failed.append((name, p.name, str(e)))
                continue
            carets = M.find_carets(alt)
            parser_set = set(pos for pos, _ in carets)
            text_set = M.all_carets_text(text)
            # the only allowed mismatch: a '^' inside \Q...\E (literal,
            # correctly excluded by the real parser, invisible to the
            # dumb scan's own \Q handling -- it has none)
            diff = parser_set ^ text_set
            if diff:
                allowed = True
                for pos in diff:
                    # is pos inside some \Q...\E span in the raw text?
                    before = text[:pos]
                    lastQ = before.rfind("\\Q")
                    lastE = before.rfind("\\E")
                    in_quote_span = lastQ != -1 and lastQ > lastE
                    # the dumb scanner has no notion of a PCRE2 (?^...)
                    # flags-RESET directive (bench/syntax's own
                    # 'mod-reset' witness, `(?i)c(?^)at`): its '^' is
                    # consumed by the real parser as part of the
                    # directive, never a Caret -- the one other named
                    # exception besides \Q...\E quoting.
                    in_flag_reset = (text[pos - 2:pos] == "(?" and
                                     pos + 1 < len(text) and text[pos + 1] == ")")
                    if not (in_quote_span or in_flag_reset):
                        allowed = False
                if not allowed:
                    crosscheck_mismatch.append((name, p.name, sorted(diff)))
    print("patterns examined: %d" % total)
    print("parse failures: %d" % len(parse_failed))
    for row in parse_failed:
        print("  PARSE-FAIL", row)
    print("opaque-caret failures (a '^' hidden from find_carets): %d"
          % len(opaque_failed))
    for row in opaque_failed:
        print("  OPAQUE-CARET", row)
    print("cross-check mismatches: %d" % len(crosscheck_mismatch))
    for row in crosscheck_mismatch:
        print("  CROSSCHECK", row)
    ok = not parse_failed and not opaque_failed and not crosscheck_mismatch
    print("RESULT:", "ALL CLEAN" if ok else "SEE FAILURES ABOVE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
