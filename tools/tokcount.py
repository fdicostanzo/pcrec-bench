#!/usr/bin/env python3
"""tools/tokcount.py -- the lexical-token counter for the ASSIST budget
([B148] L2, docs/design/unusual_set_v1.md 5.1-5.5; shared rule with [B141]).

    python3 tools/tokcount.py count FILE [--lang c|cpp|rust|python] [--json]
    python3 tools/tokcount.py ledger-check [--assists DIR]
    python3 tools/tokcount.py ledger-row FILE --member M --feature F --engine E
        --keying K --container C --author A [--reviewer R --review-verdict V]

THE COUNTING RULE (one rule, all languages; stated again in
bench/unusual/assists/RULES.md):
  * a token is a LEXICAL token of the file's own language, found by one
    hand lexer per language (no library, no interpreter version in play):
    identifier/keyword, number (one token incl. suffix, separators, exponent),
    string or char literal (ONE token, prefixes and raw/triple/f-string forms
    included), Rust lifetime, a C header-name after #include, and punctuator
    (multi-character punctuators one token: `->` `::` `<<=` `...`);
  * comments, whitespace and (Python) layout -- NEWLINE/INDENT/DEDENT -- are
    not tokens; backslash-newline is whitespace;
  * LINES = the physical lines on which a counted token starts or continues
    (blank and comment-only lines never count);
  * a region fenced `/* BOILERPLATE <item> */ ... /* END BOILERPLATE */`
    (C, C++, Rust) or `# BOILERPLATE <item>` ... `# END BOILERPLATE` (Python)
    is EXCLUDED only if <item> is DECLARED (ITEMS below); an undeclared item,
    a malformed or unclosed fence is an error naming it (exit 2). A declared
    region whose content breaks the item's shape (ITEMS: allowed statements,
    forbidden control keywords, token cap) is SMUGGLING: it is counted in
    full and reported under `smuggled`;
  * budget: BUDGET = 300 tokens per (member, engine); <= BUDGET is ASSISTED.
Deterministic: pure function of (bytes, language, ITEMS, COUNTER_VERSION).
"""
import argparse
import hashlib
import json
import os
import re
import sys

COUNTER_VERSION = "tokcount-1"
BUDGET = 300

# item -> shape. kinds of check: `stmt` (every statement must start with one
# of these tokens), `forbid` (keywords that mean logic), `maxtok`.
ITEMS = {
    "includes": {"stmt_c": ("include", "pragma", "ifdef", "ifndef", "endif"),
                 "stmt_rust": ("use", "pub", "extern"),
                 "stmt_python": ("import", "from"),
                 "maxtok": 120},
    "main": {"forbid": ("if", "else", "for", "while", "do", "switch", "case",
                        "match", "loop", "goto", "try"), "maxtok": 40},
    "io": {"forbid": ("switch", "match", "goto"), "maxtok": 80},
    "shim": {"forbid": (), "maxtok": 200},
    "wrappers": {"forbid": ("switch", "match", "goto"), "maxtok": 120},
}

CONTROL = {"if", "else", "for", "while", "do", "switch", "case", "match",
           "loop", "goto", "try"}


class LexError(Exception):
    pass


class FenceError(Exception):
    pass


# --------------------------------------------------------------------------
# lexers.  lex() returns events in source order:
#   ("tok", kind, text, line, end_line) | ("com", body, line)
# --------------------------------------------------------------------------

def _isid0(c):
    return c.isalpha() or c == "_" or c == "$" or ord(c) > 127


def _isid(c):
    return c.isalnum() or c == "_" or c == "$" or ord(c) > 127


P3_C = ("<<=", ">>=", "...", "->*", "<=>")
P2_C = ("->", "++", "--", "<<", ">>", "<=", ">=", "==", "!=", "&&", "||", "+=",
        "-=", "*=", "/=", "%=", "&=", "|=", "^=", "##", "::", ".*")
P3_R = ("<<=", ">>=", "...", "..=")
P2_R = ("::", "->", "=>", "==", "!=", "<=", ">=", "&&", "||", "+=", "-=", "*=",
        "/=", "%=", "^=", "&=", "|=", "<<", ">>", "..")
P3_P = ("**=", "//=", ">>=", "<<=", "...")
P2_P = ("->", ":=", "**", "//", "<<", ">>", "<=", ">=", "==", "!=", "+=", "-=",
        "*=", "/=", "%=", "&=", "|=", "^=", "@=")


class _L:
    def __init__(self, text, lang):
        self.s = text
        self.n = len(text)
        self.i = 0
        self.line = 1
        self.lang = lang
        self.ev = []
        self.last_line_toks = []   # token texts on the current line (C header)

    def adv(self, k=1):
        for _ in range(k):
            if self.i < self.n and self.s[self.i] == "\n":
                self.line += 1
            self.i += 1

    def err(self, msg):
        raise LexError("line %d: %s" % (self.line, msg))

    def emit(self, kind, start, sline):
        text = self.s[start:self.i]
        self.ev.append(("tok", kind, text, sline, self.line))
        if self.last_line_toks and self.last_line_toks[0][0] != sline:
            self.last_line_toks = []
        self.last_line_toks.append((sline, text))

    def peek(self, k=0):
        j = self.i + k
        return self.s[j] if j < self.n else ""

    def startswith(self, p):
        return self.s.startswith(p, self.i)

    def skip_ws(self):
        while self.i < self.n:
            c = self.s[self.i]
            if c in " \t\r\f\v\n":
                self.adv()
            elif c == "\\" and self.peek(1) == "\n" and self.lang != "rust":
                self.adv(2)
            elif c == "\\" and self.peek(1) == "\r" and self.peek(2) == "\n":
                self.adv(3)
            else:
                break

    # ---- shared literal readers ----
    def quoted(self, q):
        # at the opening quote; escapes via backslash; one token
        self.adv()
        while True:
            if self.i >= self.n:
                self.err("unterminated literal")
            c = self.s[self.i]
            if c == "\\":
                self.adv(2)
            elif c == q:
                self.adv()
                return
            elif c == "\n" and self.lang in ("c", "cpp"):
                self.err("newline in string or char literal")
            else:
                self.adv()

    def lex(self):
        lang = self.lang
        while True:
            self.skip_ws()
            if self.i >= self.n:
                return self.ev
            c = self.s[self.i]
            start, sline = self.i, self.line
            if lang == "python":
                self.py_one(c, start, sline)
            elif lang == "rust":
                self.rs_one(c, start, sline)
            else:
                self.c_one(c, start, sline)

    # ---- C / C++ ----
    def c_one(self, c, start, sline):
        if c == "/" and self.peek(1) == "/":
            self.adv(2)
            b = self.i
            while self.i < self.n and self.s[self.i] != "\n":
                if self.s[self.i] == "\\" and self.peek(1) == "\n":
                    self.adv(2)
                else:
                    self.adv()
            self.ev.append(("com", "//" + self.s[b:self.i], sline))
            return
        if c == "/" and self.peek(1) == "*":
            self.adv(2)
            b = self.i
            while not self.startswith("*/"):
                if self.i >= self.n:
                    self.err("unterminated comment")
                self.adv()
            body = self.s[b:self.i]
            self.adv(2)
            self.ev.append(("com", "/*" + body + "*/", sline))
            return
        if _isid0(c):
            while self.i < self.n and _isid(self.s[self.i]):
                self.adv()
            word = self.s[start:self.i]
            q = self.peek()
            if q in ('"', "'") and word in ("u8", "u", "U", "L"):
                self.quoted(q)
                return self.emit("str" if q == '"' else "char", start, sline)
            if (q == '"' and self.lang == "cpp"
                    and word in ("R", "u8R", "uR", "UR", "LR")):
                self.cpp_raw()
                return self.emit("str", start, sline)
            return self.emit("ident", start, sline)
        if c.isdigit() or (c == "." and self.peek(1).isdigit()):
            self.adv()
            while self.i < self.n:
                d = self.s[self.i]
                if d.isalnum() or d in "_.":
                    self.adv()
                elif d == "'" and _isid(self.peek(1)):
                    self.adv()
                elif d in "+-" and self.s[self.i - 1] in "eEpP":
                    self.adv()
                else:
                    break
            return self.emit("num", start, sline)
        if c == '"' or c == "'":
            self.quoted(c)
            return self.emit("str" if c == '"' else "char", start, sline)
        if c == "<" and [t for _, t in self.last_line_toks][-2:] == ["#", "include"] \
                and len(self.last_line_toks) == 2 and self.last_line_toks[0][0] == self.line:
            while self.i < self.n and self.s[self.i] != ">":
                if self.s[self.i] == "\n":
                    self.err("unterminated header name")
                self.adv()
            self.adv()
            return self.emit("header", start, sline)
        for p in P3_C:
            if self.startswith(p):
                self.adv(3)
                return self.emit("punct", start, sline)
        for p in P2_C:
            if self.startswith(p):
                self.adv(2)
                return self.emit("punct", start, sline)
        self.adv()
        return self.emit("punct", start, sline)

    def cpp_raw(self):
        self.adv()  # opening "
        b = self.i
        while self.i < self.n and self.s[self.i] != "(":
            self.adv()
        delim = self.s[b:self.i]
        close = ")" + delim + '"'
        while not self.startswith(close):
            if self.i >= self.n:
                self.err("unterminated raw string")
            self.adv()
        self.adv(len(close))

    # ---- Rust ----
    def rs_one(self, c, start, sline):
        if c == "/" and self.peek(1) == "/":
            while self.i < self.n and self.s[self.i] != "\n":
                self.adv()
            self.ev.append(("com", self.s[start:self.i], sline))
            return
        if c == "/" and self.peek(1) == "*":
            depth = 0
            while True:
                if self.i >= self.n:
                    self.err("unterminated comment")
                if self.startswith("/*"):
                    depth += 1
                    self.adv(2)
                elif self.startswith("*/"):
                    depth -= 1
                    self.adv(2)
                    if depth == 0:
                        break
                else:
                    self.adv()
            self.ev.append(("com", self.s[start:self.i], sline))
            return
        if c == '"':
            self.quoted('"')
            return self.emit("str", start, sline)
        if c == "'":
            n1, n2 = self.peek(1), self.peek(2)
            if n1 == "\\" or (n1 and n2 == "'"):
                self.quoted("'")
                return self.emit("char", start, sline)
            self.adv()
            while self.i < self.n and _isid(self.s[self.i]):
                self.adv()
            return self.emit("lifetime", start, sline)
        if _isid0(c):
            while self.i < self.n and _isid(self.s[self.i]):
                self.adv()
            word = self.s[start:self.i]
            q = self.peek()
            if word in ("r", "br", "cr") and q in ('"', "#"):
                j = self.i
                h = 0
                while j < self.n and self.s[j] == "#":
                    h += 1
                    j += 1
                if j < self.n and self.s[j] == '"':
                    self.adv(j - self.i + 1)
                    close = '"' + "#" * h
                    while not self.startswith(close):
                        if self.i >= self.n:
                            self.err("unterminated raw string")
                        self.adv()
                    self.adv(len(close))
                    return self.emit("str", start, sline)
                if word == "r" and h == 1 and j < self.n and _isid0(self.s[j]):
                    self.adv(1)  # raw identifier r#name
                    while self.i < self.n and _isid(self.s[self.i]):
                        self.adv()
                    return self.emit("ident", start, sline)
            if word in ("b", "c") and q == '"':
                self.quoted('"')
                return self.emit("str", start, sline)
            if word == "b" and q == "'":
                self.quoted("'")
                return self.emit("char", start, sline)
            return self.emit("ident", start, sline)
        if c.isdigit():
            hexa = c == "0" and self.peek(1) in ("x", "X")
            self.adv()
            while self.i < self.n:
                d = self.s[self.i]
                if d.isalnum() or d == "_":
                    self.adv()
                elif d == "." and self.peek(1) != "." and not _isid0(self.peek(1)) \
                        and "." not in self.s[start:self.i]:
                    self.adv()
                elif d in "+-" and self.s[self.i - 1] in "eE" and not hexa:
                    self.adv()
                else:
                    break
            return self.emit("num", start, sline)
        for p in P3_R:
            if self.startswith(p):
                self.adv(3)
                return self.emit("punct", start, sline)
        for p in P2_R:
            if self.startswith(p):
                self.adv(2)
                return self.emit("punct", start, sline)
        self.adv()
        return self.emit("punct", start, sline)

    # ---- Python ----
    def py_one(self, c, start, sline):
        if c == "#":
            while self.i < self.n and self.s[self.i] != "\n":
                self.adv()
            self.ev.append(("com", self.s[start:self.i], sline))
            return
        if _isid0(c):
            while self.i < self.n and _isid(self.s[self.i]):
                self.adv()
            word = self.s[start:self.i]
            q = self.peek()
            if q in ('"', "'") and word.lower() in (
                    "r", "u", "b", "f", "rb", "br", "fr", "rf", "t", "tr", "rt"):
                self.py_str(q)
                return self.emit("str", start, sline)
            return self.emit("ident", start, sline)
        if c.isdigit() or (c == "." and self.peek(1).isdigit()):
            hexa = c == "0" and self.peek(1) in ("x", "X")
            self.adv()
            while self.i < self.n:
                d = self.s[self.i]
                if d.isalnum() or d in "_.":
                    self.adv()
                elif d in "+-" and self.s[self.i - 1] in "eE" and not hexa:
                    self.adv()
                else:
                    break
            return self.emit("num", start, sline)
        if c in ('"', "'"):
            self.py_str(c)
            return self.emit("str", start, sline)
        for p in P3_P:
            if self.startswith(p):
                self.adv(3)
                return self.emit("punct", start, sline)
        for p in P2_P:
            if self.startswith(p):
                self.adv(2)
                return self.emit("punct", start, sline)
        self.adv()
        return self.emit("punct", start, sline)

    def py_str(self, q):
        # prefix already consumed; raw-ness does not change where a string
        # ends (a backslash still protects the quote), so one reader serves.
        triple = self.startswith(q * 3)
        if triple:
            self.adv(3)
            close = q * 3
            while not self.startswith(close):
                if self.i >= self.n:
                    self.err("unterminated triple-quoted string")
                self.adv(2 if self.s[self.i] == "\\" else 1)
            self.adv(3)
            return
        self.adv()
        while True:
            if self.i >= self.n or self.s[self.i] == "\n":
                self.err("unterminated string")
            c = self.s[self.i]
            if c == "\\":
                self.adv(2)
            elif c == q:
                self.adv()
                return
            else:
                self.adv()


def lex(text, lang):
    if lang not in ("c", "cpp", "rust", "python"):
        raise ValueError("unknown language %r" % lang)
    return _L(text, lang).lex()


# --------------------------------------------------------------------------
# fences
# --------------------------------------------------------------------------
_FENCE_C = re.compile(r"^/\*\s*(END\s+BOILERPLATE|BOILERPLATE(?:\s+(\S+))?)\s*\*/$")
_FENCE_P = re.compile(r"^#\s*(END\s+BOILERPLATE|BOILERPLATE(?:\s+(\S+))?)\s*$")


def _fence(body, lang):
    """-> None (an ordinary comment), ("open", item) or ("close", None);
    FenceError on anything that mentions BOILERPLATE but is not the exact form."""
    b = body.strip()
    if "BOILERPLATE" not in b:
        return None
    if lang == "python":
        m = _FENCE_P.match(b)
    else:
        m = _FENCE_C.match(b) if b.startswith("/*") else None
    if not m:
        # a comment merely talking about boilerplate in prose is fine only if
        # BOILERPLATE is not the first word of the comment
        inner = b.lstrip("/*# \t")
        if inner.startswith("BOILERPLATE") or inner.startswith("END BOILERPLATE"):
            raise FenceError("malformed fence comment %r" % b)
        return None
    if m.group(1).startswith("END"):
        return ("close", None)
    if not m.group(2):
        raise FenceError("fence without an item name: %r" % b)
    return ("open", m.group(2))


# --------------------------------------------------------------------------
# smuggling checks
# --------------------------------------------------------------------------

def _statements(toks, lang):
    """toks: [(kind, text, line, end)] -> list of statements (lists)."""
    out, cur = [], []
    if lang in ("c", "cpp"):
        for t in toks:               # preprocessor lines: split by line
            if cur and t[2] != cur[-1][3]:
                out.append(cur)
                cur = []
            cur.append(t)
    elif lang == "rust":
        for t in toks:
            cur.append(t)
            if t[1] == ";":
                out.append(cur)
                cur = []
    else:
        depth = 0
        for t in toks:
            if depth == 0 and cur and t[2] > cur[-1][3]:
                out.append(cur)
                cur = []
            cur.append(t)
            if t[0] == "punct" and t[1] in ("(", "[", "{"):
                depth += 1
            elif t[0] == "punct" and t[1] in (")", "]", "}"):
                depth -= 1
    if cur:
        out.append(cur)
    return out


def _shape_problems(item, toks, lang):
    spec = ITEMS[item]
    probs = []
    if len(toks) > spec["maxtok"]:
        probs.append("%d tokens exceeds the %s cap %d" % (len(toks), item, spec["maxtok"]))
    for t in toks:
        if t[0] == "ident" and t[1] in spec.get("forbid", ()):
            probs.append("control keyword %r (line %d)" % (t[1], t[2]))
    key = "stmt_" + ("c" if lang in ("c", "cpp") else lang)
    if key in spec:
        for st in _statements(toks, lang):
            texts = [t[1] for t in st]
            if lang in ("c", "cpp"):
                ok = len(texts) >= 2 and texts[0] == "#" and texts[1] in spec[key]
                if ok and texts[1] == "include":
                    ok = len(st) == 3 and st[2][0] in ("header", "str")
            elif lang == "rust":
                ok = texts[0] in spec[key] and (texts[0] != "pub" or "use" in texts[:3]) \
                    and (texts[0] != "extern" or texts[1:2] == ["crate"])
                if ok:
                    ok = all(t[0] in ("ident", "punct") for t in st) and \
                        not any(x in texts for x in ("fn", "=", "(", "!"))
            else:
                ok = texts[0] in spec[key] and not any(
                    t[0] == "punct" and t[1] in ("=", "(", ":=") and texts[0] == "import"
                    for t in st)
            if not ok:
                probs.append("statement not an import at line %d" % st[0][2])
    return probs


# --------------------------------------------------------------------------
# counting
# --------------------------------------------------------------------------

def count_text(text, lang):
    """-> dict(tokens, lines, excluded_tokens, regions, smuggled)."""
    ev = lex(text, lang)
    kept = []                 # counted tokens (kind, text, line, end)
    regions = []              # {item, tokens, line}
    smuggled = []
    cur = None                # (item, line, [tokens])
    for e in ev:
        if e[0] == "com":
            f = _fence(e[1], lang)
            if f is None:
                continue
            if f[0] == "open":
                if cur is not None:
                    raise FenceError("line %d: fence %r opened inside fence %r"
                                     % (e[2], f[1], cur[0]))
                if f[1] not in ITEMS:
                    raise FenceError("line %d: boilerplate item %r is not DECLARED "
                                     "(declared: %s)" % (e[2], f[1], ", ".join(sorted(ITEMS))))
                cur = (f[1], e[2], [])
            else:
                if cur is None:
                    raise FenceError("line %d: END BOILERPLATE without an open fence" % e[2])
                item, line, toks = cur
                cur = None
                probs = _shape_problems(item, toks, lang)
                regions.append({"item": item, "line": line, "tokens": len(toks)})
                if probs:
                    smuggled.append({"item": item, "line": line, "tokens": len(toks),
                                     "problems": probs})
                    kept.extend(toks)         # counted in full
                    regions[-1]["excluded"] = False
                else:
                    regions[-1]["excluded"] = True
            continue
        t = (e[1], e[2], e[3], e[4])
        if cur is not None:
            cur[2].append(t)
        else:
            kept.append(t)
    if cur is not None:
        raise FenceError("line %d: boilerplate fence %r never closed" % (cur[1], cur[0]))
    lines = set()
    for k, _, a, b in kept:
        lines.update(range(a, b + 1))
    excl = sum(r["tokens"] for r in regions if r["excluded"])
    return {"tokens": len(kept), "lines": len(lines), "excluded_tokens": excl,
            "regions": regions, "smuggled": smuggled}


EXT = {".c": "c", ".h": "c", ".cc": "cpp", ".cpp": "cpp", ".cxx": "cpp",
       ".hpp": "cpp", ".hh": "cpp", ".rs": "rust", ".py": "python"}


def lang_of(path):
    return EXT.get(os.path.splitext(path)[1].lower())


def count_file(path, lang=None):
    lang = lang or lang_of(path)
    if lang is None:
        raise ValueError("cannot tell the language of %s" % path)
    with open(path, "rb") as f:
        raw = f.read()
    r = count_text(raw.decode("utf-8"), lang)
    r["language"] = lang
    r["sha256"] = hashlib.sha256(raw).hexdigest()
    r["counter"] = COUNTER_VERSION
    return r


# --------------------------------------------------------------------------
# ledger (assists.tsv, 5.3)
# --------------------------------------------------------------------------
LEDGER_COLS = ("member", "feature", "engine", "language", "tokens", "lines", "budget",
               "verdict", "assist_sha256", "keying", "container", "counter_version",
               "author_lane", "reviewer_lane", "reviewer_verdict")
LANG_NAME = {"c": "C", "cpp": "C++", "rust": "Rust", "python": "Python"}
REVIEW_VERDICTS = ("accepted", "golfed", "not-idiomatic", "pending")


def verdict_of(tokens):
    return "ASSISTED" if tokens <= BUDGET else "NOT-CAPABLE"


def ledger_row(path, member, feature, engine, keying, container, author,
               reviewer="", review_verdict="pending"):
    r = count_file(path)
    return [member, feature, engine, LANG_NAME[r["language"]], str(r["tokens"]),
            str(r["lines"]), str(BUDGET), verdict_of(r["tokens"]), r["sha256"],
            keying, container, COUNTER_VERSION, author, reviewer, review_verdict]


def ledger_check(assists_dir):
    """-> list of problems (empty = the ledger agrees with the counter)."""
    tsv = os.path.join(assists_dir, "assists.tsv")
    probs = []
    with open(tsv, encoding="utf-8") as f:
        rows = [l.rstrip("\n").split("\t") for l in f if l.strip()]
    if not rows or tuple(rows[0]) != LEDGER_COLS:
        return ["assists.tsv header is not %s" % "\t".join(LEDGER_COLS)]
    seen = set()
    for n, row in enumerate(rows[1:], 2):
        if len(row) != len(LEDGER_COLS):
            probs.append("row %d: %d columns" % (n, len(row)))
            continue
        d = dict(zip(LEDGER_COLS, row))
        key = (d["member"], d["engine"])
        if key in seen:
            probs.append("row %d: duplicate (member, engine) %s" % (n, key))
        seen.add(key)
        base = os.path.join(assists_dir, d["member"], d["engine"])
        files = [x for x in sorted(os.listdir(base)) if x.startswith("assist.")] \
            if os.path.isdir(base) else []
        if len(files) != 1:
            probs.append("row %d: expected one assist.* in %s" % (n, base))
            continue
        try:
            r = count_file(os.path.join(base, files[0]))
        except (LexError, FenceError) as e:
            probs.append("row %d: %s" % (n, e))
            continue
        want = {"tokens": str(r["tokens"]), "lines": str(r["lines"]),
                "budget": str(BUDGET), "verdict": verdict_of(r["tokens"]),
                "assist_sha256": r["sha256"], "language": LANG_NAME[r["language"]],
                "counter_version": COUNTER_VERSION}
        for k, v in want.items():
            if d[k] != v:
                probs.append("row %d (%s/%s): %s is %r, the counter says %r"
                             % (n, d["member"], d["engine"], k, d[k], v))
        if d["reviewer_verdict"] not in REVIEW_VERDICTS:
            probs.append("row %d: reviewer_verdict %r" % (n, d["reviewer_verdict"]))
        if r["smuggled"]:
            probs.append("row %d: smuggled boilerplate counted: %s" % (n, r["smuggled"]))
    return probs


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("count")
    c.add_argument("file")
    c.add_argument("--lang", choices=("c", "cpp", "rust", "python"))
    c.add_argument("--json", action="store_true")
    lc = sub.add_parser("ledger-check")
    lc.add_argument("--assists", default=os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "bench", "unusual", "assists"))
    lr = sub.add_parser("ledger-row")
    lr.add_argument("file")
    for k in ("member", "feature", "engine", "keying", "container", "author"):
        lr.add_argument("--" + k, required=True)
    lr.add_argument("--reviewer", default="")
    lr.add_argument("--review-verdict", default="pending", choices=REVIEW_VERDICTS)
    a = ap.parse_args(argv)
    try:
        if a.cmd == "count":
            r = count_file(a.file, a.lang)
            if a.json:
                print(json.dumps(r, indent=1, sort_keys=True))
            else:
                print("%s\ttokens=%d\tlines=%d\texcluded=%d\t%s\t%s" % (
                    a.file, r["tokens"], r["lines"], r["excluded_tokens"],
                    verdict_of(r["tokens"]), COUNTER_VERSION))
                for s in r["smuggled"]:
                    print("SMUGGLED %s at line %d (counted): %s" % (
                        s["item"], s["line"], "; ".join(s["problems"])), file=sys.stderr)
            return 0
        if a.cmd == "ledger-row":
            print("\t".join(ledger_row(a.file, a.member, a.feature, a.engine, a.keying,
                                       a.container, a.author, a.reviewer, a.review_verdict)))
            return 0
        probs = ledger_check(a.assists)
        for p in probs:
            print("LEDGER: " + p)
        print("ledger-check: %s" % ("OK" if not probs else "%d problem(s)" % len(probs)))
        return 1 if probs else 0
    except (LexError, FenceError) as e:
        print("tokcount: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
