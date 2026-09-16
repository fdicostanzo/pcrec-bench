# Designed members — family contrast notes (draft for L3's NOTES.md)

Written by lane `b42author` (L2, blinded per pcrec D27 — see
`b42author_report.md`'s blinding statement). One entry per family this
lane touched, 1-3 sentences on what the designed members are built to
separate. L3 folds these into the set's own `NOTES.md`; nothing here is
final prose.

## Family 1 — `wild-validator`

The four near-miss twins (`uuid-near-miss`, `base10num-near-miss`,
`winpath-near-miss`, `ipv4-near-miss`) each isolate ONE spec-level
constraint (RFC 4122's version/variant nibble, JSON-number leading-zero
strictness, Windows's nine reserved filename characters, IPv4's 0-255
octet range) that a class-heavy, loosely-anchored "find this shape inside
free text" wild validator typically omits. The contrast is: permissive
match-anything-shaped vs. spec-strict — the same subject can be a hit on
one and a near-miss on the other, without either being wrong for its own
stated purpose. These four are best-guess pairings against L1's likely
imports (grok's named UUID/BASE10NUM/WINPATH macros, and a canonical
class-heavy OWASP shape for the fourth); L3 must confirm or repair the
pairing once L1's actual members are known.

## Family 2 — `wild-logparse`

`logparse-atomic` and `logparse-atomic-removed` are byte-identical except
for `(?>...)` vs `(?:...)` around a facility.severity alternation. The
contrast is the family's whole point stated directly: on a non-matching
log line (the common case in this family's "mostly sparse-hit" text), the
atomic form fails fast without saving backtracking state; the plain form
is exposed to it. Both carry `hazard_class: exponential-backtracking`
because the REMOVED form is the one that can actually demonstrate the
blowup on an adversarial line, not the defended one.

## Family 6 — `wild-codegrammar`

`codegrammar-xflag` and `codegrammar-flat` match the identical language
(an object key followed by its colon) — one as a commented, multi-line
`(?x)` body, one flattened to a single line with no comments. The
contrast isolates the `(?x)` free-spacing MECHANISM's own compile/match
cost from the underlying match logic, and separately shows which engines
(TRE has no inline-flag syntax at all) cannot run the multi-line form
regardless of cost.

## Family 7 — `cap-backref`

Five backreference shapes, each a genuinely deployed idiom rather than a
puzzle: doubled-word detection (prose linters), tag-pair matching
(template sanitizers), a palindrome-constrained vanity phone number
(a documented real service class), quoted-delimiter symmetric matching
(tokenizers), and duplicate-query-parameter detection (HTTP Parameter
Pollution defense). The contrast this family exists for is capability,
not structure: every member needs `backrefs`, which RE2, Rust `regex`
and Vectorscan all lack by construction.

## Family 8 — `cap-lookaround`

Five lookaround shapes split 3+1+1 per the family's own spec: three
chained-lookahead/lookbehind idioms (password strength, standalone
float-literal boundaries, email local-part dot-dot prevention), one
FIXED-width lookbehind (currency-symbol-prefixed amounts), and one
VARIABLE-width lookbehind (a negation window up to three words wide). The
fixed/variable split is the family's sharpest capability line: python
`re` accepts the fixed form and refuses the variable one; RE2/Rust/
Vectorscan/TRE refuse both.

## Family 9 — `cap-recursion`

Four shapes contrast the RECURSION CONSTRUCT from mere nesting DEPTH:
`balanced-parens-rec` (bare `(?R)`), `bracket-array-define` (a named
subroutine via `(?(DEFINE)...)`, kept multi-line per F-Q2), and
`nested-comment-rec` (numbered-subroutine `(?1)`) all require `recursion`
and refuse on RE2/Rust/Vectorscan/TRE/python `re`. `tag-depth3-bound`
matches three levels of nested tags using only plain capturing groups —
no recursion construct at all — so it runs everywhere, isolating "nested
three levels deep" from "recurses."

## Family 10 — `redos-nested`

Six nested-quantifier shapes, each modeled on a real, cited advisory
(a Kubeflow email-validator ReDoS report, ua-parser-js's CVE-2022-25927,
the canonical alternation "evil regex" from the public ReDoS literature,
two shapes from the awesome-redos-security CVE index's numeric/phone
classes, and moment.js's CVE-2017-18214/CVE-2022-31129 date-parsing
ReDoS pair). All six compile everywhere and all six carry
`hazard_class: exponential-backtracking` — the contrast this family
measures is not capability but SURVIVAL: RE2/Rust/Vectorscan/TRE are
immune by construction; the backtrackers (pcre2-interp, Oniguruma, perl,
python `re`, and pcrec's own backtracking-adjacent paths where relevant)
are not.

## Family 11 — `semantics-divergence`

Three alternation-order shapes (`/user|/users`, `\.tar|\.tar\.gz`,
`in|instanceof`), each modeled on a documented real bug class (URL
router route-ordering, build-tool suffix matching, hand-rolled lexer
keyword/identifier prefix ambiguity) where a leftmost-first engine and a
leftmost-longest engine give two DIFFERENT CORRECT answers on the same
subject. These three run everywhere and give a real, scoreable answer
under any engine's own convention today; the family's intended
cross-convention SCORING (grading RE2-longest or TRE against their own
correct answer rather than the shared canonical one) waits on the
harness change CB1 names as still unbuilt.

## Family 12 — `binary-nonutf8`

Three byte-level shapes: two written with `\x` escapes (so their
`canonical_text` stays valid UTF-8) and one, `mojibake-curly-quote`,
written as a genuine literal raw byte pair (0x93/0x94) so its
`canonical_text` is NOT valid UTF-8 by construction — the one designed
member that actually exercises the S10 omission rule (canonical text
omitted from the record, identity carried by `canonical_sha256` alone)
rather than merely being described by it.

## Floor

`floor-byte` (`~`) is a PROPOSAL only, not a calibrated choice — L3 owns
`captext.py` and must confirm the byte is a full-length miss on the
throughput runs and a hit on 1-2 short subjects against the real
generated corpus (§3.3), or pick a different one.
