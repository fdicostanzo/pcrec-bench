# Feedback on the first production sample — from the pcrec manager session (pcrecdev1), 2026-08-25 03:3x EDT

Verbatim in substance (lightly re-wrapped), for Frank's review. The
sample: reports/2026-08-25-email-specimen-0.1-budu-ryzen1600.md.

## (1) Actionable? Yes — what is MISSING to turn an outlier into an [ENG-*] row

- (a) the artifact's own strategy STAMPS as bucket columns — RX_ENGINE,
  RX_ENGINE_WHY, RX_VM_PREFILTER, RX_VM_RUNGS/STRATS/PRUNES,
  RX_VM_CALL_SPLICED/LINKED (all `#define`s in the emitted .c/.h; plus
  the DFA prefilter stamp already filed as missing) — an outlier is only
  a work item once the mechanism the artifact took is readable.
  [Manager note: the pcrec records already carry these as
  `engine_metadata` pairs; the REPORTER does not yet show them as
  columns — a reporter feature, not a harness one.]
- (b) the give-up as a FIRST-CLASS outcome with its code (FRAMES vs
  STEPS vs a refusal) and the SUBJECT SIZE at which it first fires, not
  an exclusion note — the ceiling is the number the loop tunes.
  [Note: `gave-up` + diagnostic code exist per row; "size at which it
  first fires" needs a size-sweep sub-bench design.]
- (c) the compile axis SPLIT three ways (pcrec / gcc / dlopen) — 118 ms
  is gcc-dominated; whether factored's ~420 ms is the K32 prefilter
  replication or gcc on a bigger artifact is not readable from the
  total. [Note: the phases are in every compile row; reporter feature.]
- (d) a per-call FLOOR control in every short-subject set (a one-literal
  pattern on the same subjects) reported beside the number, so 6.13 µs
  over 77 subjects (80 ns/subject) reads against the harness's own
  overhead. [Sub-bench design item: every set carries a floor pattern.]

## (2) Distrust

- (a) the match-compliance regime: the (?:P)\z artifact is a DIFFERENT
  PROGRAM from what pcre2 runs under ANCHORED|ENDANCHORED, so the 2.3×
  "VM beats own DFA" is real as a number but an artifact of the \z
  form's weaker skip loop, not an engine-selection outlier — bucket it
  "regime artifact" until an end-anchored entry exists ([OS-4]); keep it
  OUT of the outlier queue.
- (b) the short-subject SEARCH sums sit near the timer floor (see 1d):
  rank order trustworthy, ratios less so.
- (c) factored/short-search 82 µs vs 15.4 µs is measured on 8da6120 —
  BEFORE wave G, which was built to remove exactly that loss (its bar:
  factored == orig artifact past three named lines). Re-pin after the
  G+FB battery and that row should collapse to orig's; if it does not,
  that is the first real outlier for pcrec.
- (d) U1 (pcre2-jit timeout): plausible, not yet evidence. The
  interpreter's start-of-match optimizations (first code unit / required
  code unit / minimum length) can answer "no @ anywhere" in one memchr
  where the JIT's are different code. DISCRIMINATING MEASUREMENT: the
  interpreter with PCRE2_NO_START_OPTIMIZE on the same cell — if it then
  walks like the JIT the reading fits; if it still answers in µs it is
  something else (auto-possessification, or the recursion path). K34's
  probe harness (pcrec docs/design/subroutines_measurements/probes/)
  drives libpcre2 with option flags — copy its shape.

## (3) RANKED sub-bench areas, from pcrec's needs

1. LOG-LINE SEARCH at 256 B–4 KB: timestamps, IPv4/IPv6, key=value,
   quoted fields, typical ops patterns — the DFA+prefilter headline case
   and the one where auto-vs-jit decides whether anyone adopts pcrec;
   cheapest to make large and realistic.
2. WIDE ALTERNATIONS / KEYWORD TRIES (10, 100, 1000 words; mixed
   lengths; common prefixes): engine selection and prefilter shape are
   least measured here, and PCRE2-JIT's literal handling is strong —
   the most likely place to find a pcrec loss worth a general
   optimization.
3. LOOKAROUND + BACKREFERENCE real-world shapes (password rules,
   HTML/XML tags, CSV with quoted fields, `(?<=...)` at 1 KB): the
   VM-only paths, where pcrec's gap to the JIT is structurally largest;
   pcrec's tests/lookaround/ (457 blocks) is ready-made input.
4. BOUNDED-REPEAT and AMBIGUOUS-DECOMPOSITION band (`{n,m}` on classes,
   `(a|ab)+`, the K23 shapes, K32's `((a)|ab){4000}c`): compile-time AND
   match-time — the one family where pcrec has known super-linear
   compile cost.
5. UTF-8 with classes/properties (`\p{L}+`, `[^\x00-\x7f]`,
   case-insensitive) at 1 KB–1 MB: the encodings axis has never been
   benchmarked; a small set finds whether it is even competitive.

Below the line: the email specimen stays as the subroutine regression
row; obscure PCRE2 features deferred (Frank's direction).

## Re-pin

NOT yet: pcrec main is 08ddcbd+docs with wave G in but the heavy battery
unrun; pcrecdev1 will message the SHA when the merged G+FB tree is
battery-green (matrix + test + san).
