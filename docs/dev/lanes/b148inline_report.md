# Lane b148inline, part 1 of 2 -- the INLINE pcrec callout arm's sources (2026-10-30)

Branch `lane/b148inline`, worktree `worktrees/b148inline`, off master 5ab0f6b9. Sonnet writer.
Tier: code + checks. No pcrec build, no pcrec binary, no timing, no `make check`; the only
compilers run were gcc and clang on a tiny stand-in for `rx_ctx` (single core, ~1 s).
`testees/pcrec/` and `configs.toml` were NOT touched (lane b149prep owns them); the part-2 edits
are PROPOSED in section 4. pcrec facts below were read at `cb32eda28` (`git -C ~/pcrec show
cb32eda28:<path>`): `docs/spec/rxt_format.md` 1.1/1.1.1/1.5, `match_api.md` 11.2/11.9, `cli.md`
1.22/1.23/2.15, `docs/design/inline_c.md` 1.9/5.2, `docs/dev/lanes/ic3_report.md`, `cli/main.c`,
`src/parse/rxt_source.c`.

## 0. The two answers you asked for first

**`--code-header`.** The crash is real and is CLI-only. `cli/main.c` `cli_code_header()` fills only
`h->lang` and `h->header` of a `PcrecCodeHeader` that `cli_push_code_header()` took from `realloc`,
so `line` and `file` stay uninitialised (the `file` pointer is what `#line` later dereferences). The
`.rxt` `code-header` DIRECTIVE does not go through it: both readers (`main.c` ~2310 for a file's own
head, `rxt_source.c:4638` for a lib's) build the struct with a full compound literal
`{ name, value, line, NULL }`. BUT that does not help the inline arm: with `--include-block FRAG:LINE
ENTRY`, `main.c` builds the emit input from `st.code_headers` (the CLI list) ONLY
(`.code_headers = st.code_headers`); the ENTRY's own `code-header` lines are never read for a
fragment block (and an include fragment may not hold head lines at all). So an included block can
get a header ONLY through `--code-header`, i.e. only through the crashing path. **Fragments
therefore need no header and carry none (section 1, "NO HEADER").** How the bodies avoid headers:
the prelude lives inside the segment (a local `struct ub_view`, `#define`s, three statement-
expression macros for the file-scope helpers, and `#define memcmp __builtin_memcmp`); nothing
needs `<stdint.h>`/`<string.h>` -- `ptrdiff_t`/`size_t` come from the artifact's own header (`rx_ctx`
uses them). If a later callee needs a real header, it waits for the `--code-header` fix.

**`include` does not reach a CLI target; the inline arm is `--include-block`.** pcrec's own d27
suite shows `target t = <fragment block>` fails ("no definition 'fragblk'"): an `include` fragment's
blocks are never targets. They are compiled only with `--include-block FRAGMENT:LINE ENTRY`
(cli.md 1.23, "how the test harness compiles a fragment's blocks"), which makes the block this
run's `--pattern` and judges its code against the pinned include chain from ENTRY. That is the shape
built here. A consequence for your pre-timing check: **`pcrec --list-callouts ENTRY` lists NOTHING
for these entries** (it prints a row per callout site of each TARGET of the file; the entry has no
target, and `--list-callouts` refuses to combine with `--include-block`). See 3.

## 1. Charter vs committed

| promise (brief) | state | where |
|---|---|---|
| (a) generator writing `callees/<name>.rxt` FROM `callees/*.c`, each body in a code block byte-identical to the .c | DONE | `bench/unusual/gen_inline.py` -> `callees/ub_{luhn,isbn13,member,netstr,stub}.rxt` (5 fragments, 14 blocks: plain + whole-subject form per arm) |
| (a) `--check` mode | DONE | `gen_inline.py --check` (13 files; also run generically by `check-harness`'s `gen_*.py --check` hook) |
| (a) byte-identity check with a one-byte-mutation control | DONE | `check_inline` section "identity": INDEPENDENT brace-scanner re-extraction of `callees.c`; controls: 1 flipped byte in the segment, 1 in the callees.c copy, both detected; the unmutated pair passes |
| (b) inline-spelled pcrec member patterns / entry .rxt files; PCRE2-spelled untouched | DONE | `inline/<arm>.rxt` x 7 (`co-luhn`, `co-isbn`, `co-member`, `co-netstr` real; `co-luhn-pass`, `co-isbn-pass`, `co-member-pass` stub); `patterns/*.rx` and `subbench.toml` unmodified (git shows no change) |
| (b) every include line sha256-pinned; a check recomputes every sha; stale-sha control | DONE | `check_inline` "pins": 7/7 entries recomputed with hashlib; controls: stale pin (fragment byte changed), one hex digit flipped, unpinned include -- each refused BY NAME |
| (c) `tools/check_inline.py`, wired into `tools/check_unusual.py`, no pcrec build | DONE | section `inline` in `check_unusual.py`; `python3 -I tools/check_unusual.py --only inline` -> 24 passed, 0 failed, 1.1 s |
| (d) this report: invocation, adapter/config diff, `--code-header` answer, part-2 needs | DONE | sections 0, 3, 4, 5 |
| twin arms | NOT INLINED, by design | a twin has no site; the existing pcrec twin is the inline arm's twin |
| `co-netstr-assist` / `-nofn` arms | NOT INLINED, by design | engine-spelled assisted pattern (`(?>...(?C4))`) and the pcre2-only no-function arm |
| a pcrec build of any block / `--list-callouts` / timing | NOT DONE, by brief | part 2, section 5 |

## 2. What was built

**Fragment block shape.** One `pattern-esc "<decoded pattern>"` line per (arm, form). The decoded
pattern is `patterns/<arm>.rx` with its callout token replaced by ``(?C`c[,consume]: <segment>`)``
(`c,consume` because the site was ``(?C"netstr,consume")``); the whole-subject block is
`(?:<plain>)\z` (what `pcrecbench.record.whole_subject_text` makes; `check_inline` compares against
the real function), because `--include-block` compiles a block verbatim and the adapter builds both
forms of every pattern. The segment is:

1. `/* ... */` provenance comment; `#define UB_CONTINUE 0`, `#define UB_FAIL     (-1)` (callees.h
   lines, verbatim); `#define UB_RETURN(name, v, r) return (r)` (callees.c's non-counting line, verbatim);
2. `struct ub_view {...};` (callees.h, verbatim) and, for member, `struct ub_set {...};` (callees.c);
3. the SHIMS -- the only non-verbatim lines: `g1`, `g1_len`, `fnv` as function-like macros over GNU
   statement expressions (a file-scope `static` helper cannot live in a function body), plus
   `#define memcmp(a,b,n) __builtin_memcmp(a,b,n)` (member), plus `extern void *ub_inline_user;` (member);
4. `const struct ub_view ub_v_ = { ctx->subject, ctx->len, ctx->pos, ctx->ncap, ctx->caps, <user> };
   const struct ub_view *v = &ub_v_;` -- the view, built from the segment's `ctx` (match_api 11.3);
5. THE CALLEE BODY, the text between the braces of `long ub_<callee>(const struct ub_view *v) {`,
   byte for byte;
6. `#undef` of everything defined (the body ends in a return on every path, so the trap tail is
   never reached).

**Why shims are acceptable and how they are checked.** The brief's "body byte-identical" is met
exactly (step 5). The helpers a body calls are not part of the body. `check_inline` section
"behaviour" wraps each decoded segment as pcrec does (`ptrdiff_t f(const rx_ctx *ctx) { TEXT
__builtin_trap(); }`), compiles it with gcc AND clang (`-std=gnu11 -O2 -Wall -Wextra`: 0 warnings
from the segments) and runs it against the real `callees.c` function on 5 x 60,000 seeded random
views (valid/unset/inverted spans, `ncap` 0-3, `pos` anywhere, Luhn-valid and known-member
subjects; 233,137 of 300,000 returns non-zero, so both verdicts are exercised): 0 divergences
under both compilers. Control: flipping `==` to `!=` in the luhn segment is caught
(`DIVERGE luhn ...`). This proves shim == helper; it is NOT a substitute for pcrec compiling the
block (section 5).

**Entry files** hold one line: `include "../callees/ub_<callee>.rxt" sha256 <hex64>`. No `lib`, no
head declarations, no target. A fragment holds comments and `pattern-esc` blocks only (a head line in
a fragment is a parse error of the ENTRY in pcrec); `check_inline` asserts it. The every-chain rule
is a one-edge chain: every `include` line carries a pin.

**NO HEADER**, asserted: no segment contains `#include`; no entry or fragment names `code-header`.

**Sizes.** Longest decoded pattern 1,908 bytes (member, whole form); fragments 2.0-3.6 KB. Whether
that is inside any pcrec pattern-length limit is part-2's first compile (I found no limit that
small in `limits.def`, but did not build).

## 3. The exact pcrec invocation PROPOSED for the inline arm

Phase 1 today (adapter.py ~4930): `pcrec -p rx -fcomments --warn-emit-bytes=1 <cfg flags> -o art.c
--pattern <bytes>`. For the inline arm, for each form `F` in {plain, whole} of arm `A`:

    pcrec -p rx -fcomments --warn-emit-bytes=1 <cfg flags incl. --features all> \
        --allow-code=c \
        --include-block <abs>/bench/unusual/<fragment>:<line> \
        <abs>/bench/unusual/inline/<A>.rxt \
        -o art.c

with `<fragment>` and `<line>` read from `inline/blocks.tsv` row `(A, F)`. Notes:

* `--allow-code=c` is the invoker's grant (cli.md 1.22: the ONLY door to code; a config's `pcrec`
  line may not carry it). It applies to the whole compile; code is "reached" (not local), so the pins
  are what admits it.
* The `--pattern` argument is dropped (`--include-block` refuses `--pattern`); the ENTRY is the one
  positional operand. `-o`, `-p`, `--features`, the `-f` flags all apply (cli.md 1.23).
* Pin and chain are checked by that same invocation ("every sha256 pin on ENTRY's include closure is
  verified first"; an unpinned/mismatched line is refused naming the line and the digest). **The
  compile IS the pre-timing check of trust**; there is no separate dry run at cb32eda28 because
  `--list-callouts` has no way to see a fragment block (section 0). Cheaper variant to try in part 2:
  the same command with a describe mode (`--emit-facts`) -- `--include-block` is documented to refuse
  only `--subst`/`--subst-file`/`--emit-support`, but I did not verify that describe modes admit it.
* After the compile, read three stamps as the inline-arm witness: `RX_CODE_LANGS "c"`,
  `RX_CALLOUTS 1`, `RX_CALLOUT_BINDINGS ""` (an all-code artifact stamps the empty string, 11.2
  row 3 "the artifact's own") and that no `rx_callout_*` symbol is `extern` (so NO binding unit).
* `pcrec --list-callouts` remains usable as a REVIEWER'S view only on a target-bearing file; if wanted,
  part 2 could generate one review-only `inline/review/<arm>.rxt` with a LOCAL copy of the block (local
  code needs no pin, so it would not exercise the chain). Not built.

## 4. PROPOSED part-2 diff (not applied: `testees/pcrec/` belongs to b149prep)

`configs.toml`:

    [testees.pcrec-auto-inline]
    engine_mode = "auto"
    captures = "on"
    callout_spelling = "inline"            # NEW key (axis), like `cc` / `cflags`
    flags = ["--features", "all", "--allow-code=c"]
    description = "pcrec defaults, the callout arms spelled INLINE ... (same callee C bodies, sha-pinned; [INLINE-C] stages 2-3)"

(and `pcrec-vm-inline` if wanted: `engine_mode = "vm"`, `flags += "--engine=vm"`.) Reason for a key
and not only the flag: `--allow-code=c` in `flags` reaches `build_flags` and `runtime_options` (visible,
good), but the SPELLING must reach the testee_id so an inline record can never be taken for the
separate-TU `pcrec-auto`. By the composition rule (`compose_config_extra`, append-only chartering
order) a new LAST token `inline`: expected id `pcrec_<pin>_auto-caps-simdna-inline` (the existing
`-simdna` slug stays where it is). I could not derive it without running `pcrecbench testees` --
part 2 must print and freeze the real id and extend `check_noedge_axis`/the frozen-renderer arm so every
pre-existing id is unchanged.

`adapter.py` (shape of the change):

1. `compose_config_extra(..., inline_token)`: `"inline"` iff `cfg.get("callout_spelling") == "inline"`.
2. `compile()` / `_compile_one(..., co=...)`: when the config is inline AND `co` is a real/pass arm,
   read the (fragment, line, entry) of `(pattern_id, form)` from `bench/unusual/inline/blocks.tsv`
   (relative to the sub-bench root; pass the row's fragment path made absolute) and build the argv of
   section 3 INSTEAD of `--pattern`. Twin arms (no site) and any non-callout pattern take the old
   `--pattern` path unchanged.
3. Binding unit: skip `callee_binding_source` entirely for the inline arm (no extern symbol). Link
   `callees.o` ONLY for `ub_member_new`; add a small TU `inline_user.c` defining
   `void *ub_inline_user;` and a constructor `ub_inline_user = ub_member_new(UB_INLINE_MEMBER_PATH)`
   (`-DUB_INLINE_MEMBER_PATH="<abs users.tsv from blocks.tsv member_arg>"`) for the member arm. Without
   it the `.so` has an unresolved DATA symbol and `dlopen` fails at load.
4. Metadata: read the new text stamp `RX_CODE_LANGS`; when it is `c` and `callout_bindings` is empty
   set `meta["callout_binding"] = "inline"` (new `INLINE_BINDING_SHAPE`), keep `callout_arm`/
   `callout_spec`; record `inline_entry_sha256`/`inline_fragment_sha256` (from blocks.tsv, plus the
   fragment digest of the file actually read) as `sha256` declarations in `METADATA_DECL` next to
   `callees_sha256`. Do NOT set `callees_sha256` as the callee identity of an inline row (the object is
   linked only for the set; say so in the declaration text).
5. FIRE PASS: the counting arm (`-DUB_COUNT` log) has no inline analogue (the inline `UB_RETURN` is the
   non-counting one; a counting segment would need `<stdio.h>`, i.e. a header). Proposal: the inline
   rows carry NO `callout_fires`; fire parity is argued by the two facts that the callees are PURE and
   that segment == callee on 300k views (this report). If Frank wants counted fires on the inline arm,
   a counting twin segment is a generator change AND needs the `--code-header` fix.
6. Registry/shim: nothing for the shim expected (whether abi 93 adds an `rx_info` field was not checked here);
   `list_schema.tsv` is archived per pin -- the `code-header`/`include`/`sha256` rows already exist at
   abi 90/91, so the b149prep archive should show them.

## 5. What part 2 needs from a cb32eda28 build

* The binary `build/pcrec-cb32eda28` from b149prep (abi 93), then in order: (1) compile the 14 blocks
  as in section 3 and require rc 0 + the three stamps; (2) the three REFUSAL controls through pcrec
  itself: edit a fragment byte (pin mismatch, named line + digest), drop `sha256` from an entry
  (`carries no sha256 pin`), omit `--allow-code=c` (the `requires module 'code-c'` text); (3) gcc AND
  clang compile of every `.c` (the cc axis), look for `-Wall -Wextra -Werror` hits in the user region
  (the `#line` points back at the fragment); (4) answers on `bench/unusual` short subjects == the
  separate-TU `pcrec-auto` arm (the existing `pass == twin` and first-candidate-fails gates re-pointed
  at the inline testee); (5) emit-size / program-identity census of the 14 artifacts.
* Things I could NOT verify and part 2 must: `#define`/`#undef`/`#line` interplay inside a segment
  (pattern-esc gives every decoded line its own `#line`; directives should be fine); that pcrec
  accepts a ~1.9 KB string callout; `consume` attribute on a code site in `c,consume:` spelling for
  netstr (11.9 para 1 says yes); the macro `RX_` set not colliding with `g1`/`fnv`/`g1_len` (no `RX_`
  names are used by the prelude); how `ncap` reads when pcrec compiles `--features all` with captures on
  (the view's `ncap` is `ctx->ncap`, the same as the wrapper's source).
* gcc-only caveat for the shims: GNU statement expressions are accepted by gcc and clang (both tested).

## 6. Findings

1. `include` blocks are not CLI targets; the inline arm is `--include-block`, and
   `--list-callouts ENTRY` is blind to it (section 0/3). The lane brief's pre-check does not exist at
   cb32eda28 for this shape; the compile is the check.
2. The `--code-header` crash is CLI-only; an included block cannot use `code-header` lines at all
   (`--include-block` ignores the entry's head). Headers-free segments are therefore not a preference
   here but the only available shape.
3. A function body cannot hold the callee's `static` helpers, so three of them are SHIMS (macros) and
   one libc call is respelled to its builtin. The body itself is byte-exact. The alternative of closing
   the generated function from inside the segment and writing file-scope definitions would give
   byte-exact helpers too, but it abuses the generated function's structure and I did not do it.
4. ctx->user is NULL at a code site (11.9 para 4), so the member callee's set arrives through the data
   symbol `ub_inline_user` (a link-level dependency the separate-TU arm does not have).
5. The inline arm has no fire counter (section 4 item 5).

## 7. Checks

* `python3 -I tools/check_inline.py`: **24 passed, 0 failed** (~1 s). `python3 -I tools/check_unusual.py
  --only inline`: 24/0. `gen_inline.py --check`: 13 files, 0 differences.
* Not run (by brief): `make check`, `make check-unusual` in full, anything needing a pcrec build.
  The new section adds ~1 s to `check-unusual`.

## 8. OWED

Nothing long-running. For part 2 (a fresh lane, after b149prep merges): sections 4 and 5.
