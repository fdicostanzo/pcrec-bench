#!/usr/bin/env python3
"""tools/tests/test_tokcount.py -- self-tests for `tools/tokcount.py` ([B148] L2).

Hand-counted fixtures, one per language (each token spelled out in the
comment beside its line), the boilerplate-exclusion arm, the smuggling
sabotages (logic inside a declared region MUST be counted, and flagged),
the fence errors (undeclared / malformed / unclosed, each BY NAME), the
ledger round trip, and ub_map.h (lexes, compiles -Wall -Werror, behaves).
Run: python3 tools/tests/test_tokcount.py
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))
import tokcount as T  # noqa: E402

N = [0, 0]


def check(name, ok, detail=""):
    N[0] += 1
    if not ok:
        N[1] += 1
        print("FAIL %s %s" % (name, detail))


def expect(name, text, lang, tokens, lines, excluded=0):
    r = T.count_text(text, lang)
    check(name, (r["tokens"], r["lines"], r["excluded_tokens"], r["smuggled"]) ==
          (tokens, lines, excluded, []),
          "got tokens=%d lines=%d excluded=%d smuggled=%s want %d/%d/%d" % (
              r["tokens"], r["lines"], r["excluded_tokens"], r["smuggled"],
              tokens, lines, excluded))


def raises(name, text, lang, exc, needle):
    try:
        T.count_text(text, lang)
    except exc as e:
        check(name, needle in str(e), str(e))
        return
    check(name, False, "no %s raised" % exc.__name__)


C_FIX = r'''/* BOILERPLATE includes */
#include <stdio.h>
#include "ub_map.h"
/* END BOILERPLATE */
// a comment, with "quotes" and /* nesting
int f(int x) {
    return x << 2;
}
static const char *s = "a\"b";
char c = '\'';
long n = 1'000 + 0x1.8p+3;
'''
# int f ( int x ) { =7 | return x << 2 ; =5 | } =1 |
# static const char * s = "a\"b" ; =8 | char c = '\'' ; =5 | long n = 1'000 + 0x1.8p+3 ; =7
expect("c-fixture", C_FIX, "c", 33, 6, excluded=6)
# the same file WITHOUT the fence counts the two #include lines in full (+6, +2 lines)
expect("c-unfenced", C_FIX.replace("/* BOILERPLATE includes */\n", "").replace(
    "/* END BOILERPLATE */\n", ""), "c", 39, 8)
# a backslash-newline is whitespace and continues a // comment:
# int a = 1 + 2 ; =7 | int b ; =3  (lines: 1, 2, 4)
expect("c-splice", "int a = 1 \\\n + 2; // c \\\n still comment\nint b;\n", "c", 10, 3)

CPP_FIX = '''auto r = R"x(a)" b)x";
std::map<int,int> m;
'''
# auto r = R"..." ; =5 | std :: map < int , int > m ; =10
expect("cpp-fixture", CPP_FIX, "cpp", 15, 2)
expect("cpp-raw-multiline", 'auto r = R"(a\nb)";\n', "cpp", 5, 2)

RS_FIX = '''/* BOILERPLATE includes */
use std::io::{self, Read};
/* END BOILERPLATE */
fn f<'a>(s: &'a str) -> usize {
    let c = b'x'; let r = r#"a"b"#;
    for i in 0..=3 { s.len(); }
    1.max(2)
    /* a /* nested */ still comment */
    // 2.5e-3 in a comment
    2.5e-3
}
'''
# fn f < 'a > ( s : & 'a str ) -> usize { =15 | let c = b'x' ; let r = r#"a"b"# ; =10
# for i in 0 ..= 3 { s . len ( ) ; } =14 | 1 . max ( 2 ) =6 | 2.5e-3 =1 | } =1
expect("rust-fixture", RS_FIX, "rust", 47, 6, excluded=11)

PY_FIX = '''# BOILERPLATE includes
import sys
from os import path
# END BOILERPLATE
def f(x, *, y=1):
    s = f"a{x}" + rb'\\x'
    return s ** 2 // 3 != 0
"""doc
string"""
z = 1_0.5e+2j
w = (a := 1)  # trailing comment
'''
# def f ( x , * , y = 1 ) : =13 | s = f"" + rb'' =5 | return s ** 2 // 3 != 0 =7
# """doc\nstring""" =1 (2 lines) | z = 1_0.5e+2j =3 | w = ( a := 1 ) =7
expect("python-fixture", PY_FIX, "python", 36, 7, excluded=6)

# ---- smuggling: logic inside a declared region is COUNTED and flagged ----
def smuggle(name, text, lang, tokens, item):
    r = T.count_text(text, lang)
    ok = r["tokens"] == tokens and r["excluded_tokens"] == 0 and \
        len(r["smuggled"]) == 1 and r["smuggled"][0]["item"] == item
    check(name, ok, str(r))

smuggle("smuggle-c-main-if",
        "/* BOILERPLATE main */\nint main(void) { if (x) { go(); } return 0; }\n/* END BOILERPLATE */\n",
        "c", 20, "main")
# int main ( void ) { if ( x ) { go ( ) ; } return 0 ; } = 20
smuggle("smuggle-c-includes-code",
        "/* BOILERPLATE includes */\n#include <stdio.h>\nint x = f(y);\n/* END BOILERPLATE */\n",
        "c", 3 + 8, "includes")
smuggle("smuggle-c-include-with-trailing-tokens",
        "/* BOILERPLATE includes */\n#include <stdio.h> int z\n/* END BOILERPLATE */\n",
        "c", 5, "includes")
smuggle("smuggle-py-main-loop",
        "# BOILERPLATE main\nfor i in range(3):\n    work(i)\n# END BOILERPLATE\n",
        "python", 12, "main")
# for i in range ( 3 ) : =8 | work ( i ) =4
smuggle("smuggle-py-import-code",
        "# BOILERPLATE includes\nimport os\nx = os.getcwd()\n# END BOILERPLATE\n",
        "python", 2 + 7, "includes")
# import os =2 | x = os . getcwd ( ) =7
smuggle("smuggle-rust-use-fn",
        "/* BOILERPLATE includes */\nuse a::b;\nfn g() {}\n/* END BOILERPLATE */\n",
        "rust", 5 + 6, "includes")
# use a :: b ; =5 | fn g ( ) { } =6
smuggle("smuggle-oversize-main",
        "/* BOILERPLATE main */\n" + "a;" * 21 + "\n/* END BOILERPLATE */\n", "c", 42, "main")


# ---- fence errors, each BY NAME ----
raises("fence-undeclared", "/* BOILERPLATE memo */\nint x;\n/* END BOILERPLATE */\n",
       "c", T.FenceError, "'memo' is not DECLARED")
raises("fence-unclosed", "/* BOILERPLATE main */\nint x;\n", "c", T.FenceError, "never closed")
raises("fence-stray-end", "/* END BOILERPLATE */\n", "c", T.FenceError, "without an open fence")
raises("fence-line-comment-form", "// BOILERPLATE main\nint x;\n// END BOILERPLATE\n",
       "c", T.FenceError, "malformed fence")
raises("fence-no-item", "/* BOILERPLATE */\n", "c", T.FenceError, "without an item")
raises("fence-nested", "/* BOILERPLATE main */\n/* BOILERPLATE io */\n", "c",
       T.FenceError, "opened inside")
# the C block form is not a Python fence: it is just tokens, counted
expect("fence-py-block-form-is-tokens", "/* BOILERPLATE main */\n", "python", 6, 1)
# a fence-looking marker inside a string literal is a token, not a fence
expect("fence-in-string", 'char *s = "/* BOILERPLATE memo */";\n', "c", 6, 1)
# prose that merely mentions the word is an ordinary comment
expect("fence-prose-comment", "/* the BOILERPLATE is elsewhere */\nint x;\n", "c", 3, 1)
# a declared legit shim region with a loop is excluded (control for the sabotages)
expect("shim-loop-allowed",
       "/* BOILERPLATE shim */\nfor (i = 0; i < n; i++) { if (t) run(); }\n/* END BOILERPLATE */\nint k;\n",
       "c", 3, 1, excluded=23)
# for ( i = 0 ; i < n ; i ++ ) { if ( t ) run ( ) ; } = 23, hand-split

# ---- lexer errors, determinism ----
raises("lex-unterminated-string", 'char *s = "abc;\n', "c", T.LexError, "line 1")
raises("lex-unterminated-comment", "/* abc\n", "rust", T.LexError, "unterminated comment")
check("determinism", T.count_text(C_FIX, "c") == T.count_text(C_FIX, "c"))
check("lang-of", [T.lang_of(x) for x in ("a.c", "a.h", "a.cpp", "a.rs", "a.py", "a.txt")] ==
      ["c", "c", "cpp", "rust", "python", None])


# ---- ledger round trip (5.3) ----
tmp = tempfile.mkdtemp(prefix="tokcount-test-")
try:
    d = os.path.join(tmp, "va-term", "re2")
    os.makedirs(d)
    ap = os.path.join(d, "assist.cc")
    with open(ap, "w") as f:
        f.write(CPP_FIX)
    row = T.ledger_row(ap, "va-term", "vars", "re2", "resolved pattern bytes",
                       "unordered_map", "lane-x", "lane-y", "accepted")
    check("ledger-row", row[4:8] == ["15", "2", "300", "ASSISTED"] and row[3] == "C++" and
          row[11] == T.COUNTER_VERSION, str(row))

    def write(rows):
        with open(os.path.join(tmp, "assists.tsv"), "w") as f:
            f.write("\t".join(T.LEDGER_COLS) + "\n")
            for r in rows:
                f.write("\t".join(r) + "\n")
    write([row])
    check("ledger-good", T.ledger_check(tmp) == [], str(T.ledger_check(tmp)))
    bad = list(row)
    bad[4] = "14"
    write([bad])
    check("ledger-token-tamper", any("tokens is '14'" in p for p in T.ledger_check(tmp)))
    bad = list(row)
    bad[8] = "0" * 64
    write([bad])
    check("ledger-sha-tamper", any("assist_sha256" in p for p in T.ledger_check(tmp)))
    write([row, row])
    check("ledger-duplicate", any("duplicate" in p for p in T.ledger_check(tmp)))
    with open(ap, "w") as f:                      # 301 tokens -> NOT-CAPABLE
        f.write("a;" * 150 + "b\n")
    row2 = T.ledger_row(ap, "va-term", "vars", "re2", "k", "c", "a")
    check("ledger-not-capable", row2[4] == "301" and row2[7] == "NOT-CAPABLE", str(row2[4:8]))
    write([row2])
    check("ledger-not-capable-agrees", T.ledger_check(tmp) == [])
    with open(ap, "w") as f:                      # exactly 300 -> ASSISTED
        f.write("a;" * 150 + "\n")
    check("budget-boundary-300", T.ledger_row(ap, "m", "f", "e", "k", "c", "a")[4:8] ==
          ["300", "1", "300", "ASSISTED"])
finally:
    shutil.rmtree(tmp)

# the committed ledger must agree with the counter (header-only today)
check("committed-ledger", T.ledger_check(os.path.join(ROOT, "bench", "unusual", "assists")) == [],
      str(T.ledger_check(os.path.join(ROOT, "bench", "unusual", "assists"))))

# ---- RULES.md names every declared item, the budget and the counter ----
rules = open(os.path.join(ROOT, "bench", "unusual", "assists", "RULES.md")).read()
for item in T.ITEMS:
    check("rules-names-" + item, "`%s`" % item in rules)
check("rules-counter-version", T.COUNTER_VERSION in rules)
check("rules-budget", "**%d**" % T.BUDGET in rules)

# ---- ub_map.h: lexes, compiles clean, behaves ----
hdr = os.path.join(ROOT, "bench", "unusual", "assists", "ub_map.h")
r = T.count_file(hdr)
check("ub_map-lexes", r["tokens"] > 100 and r["language"] == "c", str(r["tokens"]))
cc = shutil.which("cc") or shutil.which("gcc")
if cc:
    tmp = tempfile.mkdtemp(prefix="ubmap-test-")
    try:
        src = os.path.join(tmp, "t.c")
        with open(src, "w") as f:
            f.write('''#include <stdio.h>
#include "ub_map.h"
static int seen;
static void cnt(void *v) { seen += *(int *)v; }
int main(void) {
    ub_map m; ub_map_init(&m);
    static int vals[1000]; char k[16];
    if (ub_map_get(&m, "x", 1)) return 1;
    for (int i = 0; i < 1000; i++) { vals[i] = 1; sprintf(k, "k%d", i); if (ub_map_put(&m, k, strlen(k), &vals[i])) return 2; }
    for (int i = 0; i < 1000; i++) { sprintf(k, "k%d", i); if (ub_map_get(&m, k, strlen(k)) != &vals[i]) return 3; }
    ub_map_put(&m, "k5", 2, &vals[0]);
    if (ub_map_get(&m, "k5", 2) != &vals[0] || m.n != 1000) return 4;
    ub_map_put(&m, "", 0, &vals[1]);
    if (ub_map_get(&m, "", 0) != &vals[1] || ub_map_get(&m, "k5\\0", 3)) return 5;
    ub_map_each(&m, cnt);
    ub_map_free(&m);
    return seen == 1001 ? 0 : 6;
}
''')
        exe = os.path.join(tmp, "t")
        p = subprocess.run([cc, "-std=c11", "-Wall", "-Wextra", "-Werror", "-I", os.path.dirname(hdr),
                            src, "-o", exe], capture_output=True, text=True)
        check("ub_map-compiles", p.returncode == 0, p.stderr)
        if p.returncode == 0:
            q = subprocess.run([exe])
            check("ub_map-behaves", q.returncode == 0, "rc=%d" % q.returncode)
    finally:
        shutil.rmtree(tmp)
else:
    print("note: no C compiler; ub_map.h compile test skipped")

print("tokcount: %d checks, %d failed" % (N[0], N[1]))
sys.exit(1 if N[1] else 0)
