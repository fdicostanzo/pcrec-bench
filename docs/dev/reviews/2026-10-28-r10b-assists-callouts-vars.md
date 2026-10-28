# R10b review: L6 assists, callouts (RE2 / rust / Vectorscan) and vars (all five)

Read-only reviewer, 2026-10-28, for [B148] L6 (docs/design/unusual_set_v1.md 5.4).
I read bench/unusual/assists/{RULES.md,AUTHORS.md,assists.tsv}, problems/{callouts,vars}.md
and both sample TSVs, testees/assist/ub_assist.h + ub_runner.c's `ub_lookup`, ub_map.h's
`ub_map_put` (it COPIES the key, so freeing or reusing the caller's pattern buffer is safe), the
eight author reports docs/dev/lanes/b148a-{co,va}-*_report.md, and all 29 assist files. Every
file's sha256 matches its ledger row (checked with sha256sum; va-term-bang is byte-identical to
va-term on each engine, as the ledger says). I compiled nothing, ran no assist and no tokcount.
Token estimates below are hand counts, marked "~".

Two mid-wave manager rulings were applied: (a) authors may add includes inside the `includes`
fence; (b) assisted callout engines call the shared predicate through the `wrappers` fence. All
nine callout assists comply with (b): each wrapper only forwards its arguments, and no assist
reimplements Luhn, ISBN or set membership.

## Verdicts

| member | engine | tokens | ledger verdict | review verdict | reason |
|---|---|---|---|---|---|
| co-luhn | re2 | 202 | ASSISTED | accepted | Compiles once in Latin-1. Loops `RE2::Match(s, start, n, UNANCHORED)` over the whole text, so `\b` sees byte start-1. Resumes at s+1. Ordinary RE2 code. |
| co-isbn | re2 | 202 | ASSISTED | accepted | Same file as co-luhn apart from the pattern. |
| co-member | re2 | 202 | ASSISTED | accepted | `\w+` stands in for `\w++`. They are equivalent because nothing follows the group (RE2 has no possessive quantifier). |
| co-luhn | rust | 166 | ASSISTED | accepted | `(?-u)` byte mode. `captures_at` keeps the context before `at`. This is the textbook loop. |
| co-isbn | rust | 166 | ASSISTED | accepted | Same as co-luhn. |
| co-member | rust | 166 | ASSISTED | accepted | Same as co-luhn; `\w+` for `\w++` as on RE2. |
| co-luhn | vectorscan | 242 | ASSISTED | accepted | Native Hyperscan design. One SOM_LEFTMOST scan per call from start-1. The callback drops matches that start before `start`, calls the predicate, and returns 1 to stop on the first pass. |
| co-isbn | vectorscan | 242 | ASSISTED | accepted | Same as co-luhn. |
| co-member | vectorscan | 242 | ASSISTED | accepted | The trailing `\b` makes the run maximal, which Hyperscan needs because it reports every end. Group 1 starts at s+5. |
| va-tenant | pcre2 | 354 | NOT-CAPABLE | accepted; revise-for-ruling (count only, ~-28) | `\xHH` per byte (`\Q..\E` is rightly avoided), explicit-length compile, key = resolved text. The hand-written hex table exists only because the author wrote before ruling (a). With `sprintf` it would be ~326, still over, so the verdict stands. |
| va-route | pcre2 | 461 | NOT-CAPABLE | accepted; revise-for-ruling (count only, ~-28) | As va-tenant. It also passes `"api"` and `".json"` through `lit` with casts (~10 tokens), which is mild and not padding. After the ruling ~433; does not flip. |
| va-term | pcre2 | 362 | NOT-CAPABLE | accepted; revise-for-ruling (count only, ~-28) | ~334 after the ruling; does not flip. |
| va-term-bang | pcre2 | 362 | NOT-CAPABLE | accepted; revise-for-ruling (count only, ~-28) | Identical file to va-term. |
| va-tenant | onig | 303 | NOT-CAPABLE | accepted (knife-edge) | ASCII encoding + PERL_NG (`^`=`\A`, `$`=`\Z`, the PCRE2 meaning). Dense nested `stpcpy`/`strcpy` chains, but that is ordinary C and dodges nothing (the file is over budget anyway). About 2 tokens can be found (reorder the ternary to drop its parens), giving ~301. Honest, by a hair. |
| va-route | onig | 398 | NOT-CAPABLE | accepted | Hex-escapes the default `api` but writes `\\.json` by hand: inconsistent within the file, harmless. Comfortably over. |
| va-term | onig | 308 | NOT-CAPABLE | accepted (knife-edge) | No more than ~2-4 tokens are recoverable. Honest. |
| va-term-bang | onig | 308 | NOT-CAPABLE | accepted (knife-edge) | Identical file to va-term. |
| va-tenant | re2 | 191 | ASSISTED | accepted | `RE2::QuoteMeta` (the engine's own helper, as the problem asks), Latin-1, `unordered_map` cache keyed by the resolved text. |
| va-route | re2 | 245 | ASSISTED | accepted | Correct `:-` / `+` logic. The ledger's container text "per-byte [xX] ASCII fold" is wrong for this row (see R10B-15). |
| va-term | re2 | 251 | ASSISTED | accepted | Drops `(?i)` and spells each ASCII letter `[xX]`. This is justified and commented: Latin-1 `(?i)` folds 0xC9/0xE9, PCRE2 does not. A knowing RE2 user would do this. See R10B-8. |
| va-term-bang | re2 | 251 | ASSISTED | accepted | Identical file to va-term. |
| va-tenant | rust | 187 | ASSISTED | accepted | `(?-u)` with per-byte `\xHH`. Right choice: `regex::escape` takes `&str` and values need not be UTF-8. Uses `cache.entry`. Idiomatic Rust. |
| va-route | rust | 243 | ASSISTED | accepted | `let-else`, `filter(..).unwrap_or(b"api")`. Idiomatic. |
| va-term | rust | 200 | ASSISTED | accepted | `(?-u)(?i)` is ASCII-only folding, so the PCRE2 answer is correct without respelling. |
| va-term-bang | rust | 200 | ASSISTED | accepted | Identical file to va-term. |
| va-tenant | vectorscan | 311 | NOT-CAPABLE | accepted | `\xHH` with `sprintf` into a VLA, SOM_LEFTMOST, scratch grown on a miss, the callback stops at the first match. ~9 avoidable tokens (`m->g1s = m->g1e = -1`, a second `strlen`) would give ~302. Not padded; does not flip. |
| va-route | vectorscan | 371 | NOT-CAPABLE | accepted | Same design. Comfortably over. |
| va-term | vectorscan | 316 | NOT-CAPABLE | accepted | Same as va-tenant; ~307 at best. |
| va-term-bang | vectorscan | 316 | NOT-CAPABLE | accepted | Identical file to va-term. |

**Counts.**
- 29 accepted, 0 golfed, 0 not-idiomatic, 0 padded.
- revise-for-ruling: 4 (pcre2 vars). These move the count only; no verdict flips.

**Are the NOT-CAPABLE verdicts honest?** Yes, all 12 are honest per the counter. But onig (303/308) and Vectorscan (311/316) on va-tenant and va-term are within about 3-16 tokens of the line. That gap is author-style variance, not an engine property.

What separates vars ASSISTED from NOT-CAPABLE is the language more than the engine:
- C has no string or escape helper.
- The C++ and Rust assists get theirs free: `QuoteMeta` / `format!` and the standard containers.

The report should say this beside the C-engine vars rows.

**Style across engines.**
- **Callouts.** The three engines are consistent: RE2 and Rust share one design (restart at s+1), and Vectorscan has the idiomatic single-scan equivalent. The three files per engine differ only in the pattern and the group-1 offset.
- **Vars.** The three C engines each wrote their own hex escaper: a lookup table (pcre2), `sprintf` with a moving pointer (onig), and `sprintf` with an index into a second buffer (Vectorscan). Ruling (a) would let pcre2 converge on the other two.

## Semantic risks (what a 16-20-case public sample would miss)

None of these breaks a current row. Where I could construct a breaking input by reading, it is given. Where I could not, the risk is marked LATENT and the reason stated.

- **R10B-1 (Vectorscan callouts, end-ordered reporting).** Hyperscan delivers matches in END order. This equals leftmost-first only because every candidate is a maximal word run, so candidates never overlap or nest. For co-luhn, co-isbn and co-member I could build no counterexample. LATENT: the design would break for a member whose candidates can nest. For example, `\d{13,19}` without its trailing `\b` on a 20-digit run reports the start-0 match ending at 13 and then later ends, where PCRE2 takes 19 digits.
- **R10B-2 (Vectorscan callouts, one byte of context).** The scan starts at start-1, so `\b` at `start` sees the real previous byte. The buffer edge at start-1 creates false candidates there, but the `s < start` filter drops them before the predicate runs, so they cost no fires. With SOM_LEFTMOST, a false candidate at start-1 could only hide a real candidate that shares its end; that cannot happen for these patterns. Correct for `\b`, which looks back one byte. LATENT for any wider lookbehind.
- **R10B-3 (fire counts vs the native arms).** RE2 and Rust restart at s+1; Vectorscan scans once and filters. Both give the same predicate-call count as libpcre2's callout, because no start yields more than one candidate and a restart at s+1 can never land inside a failed candidate's run (a `\b` is required). No divergence is constructible for the three members. None of the assists keeps its own counter. If the report's "predicate evaluations" figure comes from the runner's `ub_pred`, it is comparable as it stands.
- **R10B-4 (`\w+` for `\w++`, RE2/Rust co-member).** Equivalent here: group 1 is the pattern's tail, and leftmost-first greedy takes the maximal run. Input `user=nick-x`: every arm reports `5,9`. LATENT: the equivalence would fail if anything followed the group.
- **R10B-5 (RE2 hides engine failures).**
  - Callouts read every false `Match` as no match.
  - Vars treat `!re->ok()` as `n` and keep the broken RE2 in the cache.
  - Constructible input: a va-term value of very many letters (on the order of 10^5 or more). Each letter becomes a `[xX]` class, which could push the program past RE2's default 8 MiB `max_mem`. The call would then answer `n` where PCRE2 matches, recorded as WRONG, not as a give-up.
  - Unlikely with log-sized values. The fix is to return a negative code on `!ok()`.
- **R10B-6 (Rust vars, `Regex::new(..).unwrap()`).** The same oversized-value input makes the regex size limit panic across `extern "C"`. The process aborts: a crash outcome for the whole cell, not a per-call give-up. LATENT for log-sized values.
- **R10B-7 (`$` dialect on va-route).** PCRE2, onig (PERL_NG gives `\Z`) and Vectorscan accept `$` before a final `\n`. RE2 and Rust `$` means `\z`. Input: res=users, line `/api/v1/users\n` gives `m:0,13` on PCRE2 and `n` on RE2/Rust. The contract rules this out ("no trailing newline"), so it is LATENT. Respelling `$` as `\n?\z` on those two arms would remove the risk; the problem statement does say "you must get the PCRE2 answer".
- **R10B-8 (RE2 va-term `[xX]` respelling).** Correct as written. It relies on `isalpha`/`tolower`/`toupper` running in the C locale: no `setlocale` exists anywhere in testees/assist/, checked. A runner that ever set a Latin-1 locale would turn 0xE9 into `[éÉ]` and break sample rows 15-16 and their held-out analogues. Also, `<cctype>` is reached only transitively; ruling (a) lets the author add it at no cost. An explicit ASCII test would remove the dependence.
- **R10B-9 (escaping completeness, NUL and metacharacters).** All five are complete:
  - pcre2, onig, Vectorscan and Rust write `\xHH` for every byte, NUL and alphanumerics included. In all four dialects `\x` takes at most two hex digits, so a following literal hex digit is never absorbed.
  - RE2's `QuoteMeta` writes `\x00` for NUL and leaves bytes >= 0x80 raw. That is correct only because EncodingLatin1 is set: under RE2's UTF-8 default, a raw 0xE9 makes an invalid pattern, which would then be masked as `n` (R10B-5).
  - pcre2 correctly rejected `\Q..\E`: a value of `a\Eb|c` would escape the quoting.
- **R10B-10 (stack VLAs, onig and Vectorscan vars).** Both size a `char p[64 + 4*len]` buffer from the value. A value of about 2 MiB or more overflows the default 8 MiB stack (SIGSEGV, a crash). pcre2 uses `malloc`; RE2 and Rust use the heap. LATENT for log-sized values.
- **R10B-11 (Vectorscan vars, unchecked return codes).** The return codes of `hs_alloc_scratch` and `hs_scan` are ignored, so a scratch or scan error reads as `n` (wrong) instead of a give-up. LATENT.
- **R10B-12 (UNSET vs EMPTY).** Read against `ub_lookup`'s contract (NULL = UNSET; non-NULL with len 0 = EMPTY), all 20 vars files are correct:
  - va-tenant: EMPTY gives `^-[0-9]{4}…` and UNSET gives `r`.
  - va-route: `prefix` EMPTY or UNSET gives `api`; `fmt` EMPTY appends `.json`; `res` EMPTY is allowed (sample 17).
  - va-term: EMPTY or UNSET gives `r`.

  No divergence constructible.
- **R10B-13 (cache-key collisions).** Every arm keys on the resolved pattern text. The escapes are injective and the template is fixed, so two keys can be equal only when the patterns are equal, and then the answers are equal too. The key is safe by construction. onig and Vectorscan take `strlen` of the pattern, which is safe because the text never holds a raw NUL. `ub_map_put` copies the key, so pcre2's `free(p)` and the reused VLAs on onig and Vectorscan cannot leave a key dangling.
- **R10B-14 (refusal before the engine).** All 20 decide UB_R before any compile or match. Rust va-route evaluates `prefix` before checking `res`, which touches no engine. Correct.
- **R10B-15 (ledger text).** The RE2 `container` cell says "per-byte [xX] ASCII fold" on all four vars rows. Only va-term and va-term-bang fold; va-tenant and va-route do not. Fix the wording at landing.
- **R10B-16 (Vectorscan vars, "first reported = leftmost").** Holds for the templates as written:
  - va-term is fixed-length per start.
  - va-tenant and va-route are `^`-anchored with a single possible end: in va-route, `v[0-9]+` is followed by a literal `/`, and `\?` and `$` cannot both match.

  LATENT if a template gains a variable-length tail.
- **R10B-17 (pcre2 vars give-up code).** On a compile failure the assist returns `-err`. PCRE2 compile codes are >= 100, while match errors are already negative, so the negated value overlaps the match-error range. The adapter's give-up table may then name it wrongly. Minor.
- **R10B-18 (per-call escaper cost, timing only).** These costs sit inside the clock and differ by arm:
  - Rust's `lit` allocates a `String` per value byte (`format!` then `collect`).
  - onig and Vectorscan call `sprintf` per byte.
  - pcre2 uses a lookup table.
  - Rust callouts allocate a `Captures` per candidate.

  Answers are unaffected, but the time is "this assist", as problems/vars.md 4 already warns. Worth one line in the report's vars legend beside the miss-compile cost.

**Completeness, by id.** All 29 (member, engine) pairs are in the table:
- co-luhn, co-isbn and co-member on re2, rust and vectorscan (9).
- va-tenant, va-route, va-term and va-term-bang on pcre2, onig, re2, rust and vectorscan (20).

The risks R10B-1 through R10B-18 are all listed: none dropped, none merged.
