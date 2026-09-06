/* testees/pcrec/shim.c -- the one file in this project that knows pcrec's ABI.
 *
 * Compiled ONCE PER PATTERN, into the .so the driver dlopens:
 *
 *     $CC -O2 -fPIC -shared -o artifact-N.so shim.c \
 *         -DPB_ARTIFACT='"artifact.c"' -I<the artifact's directory>
 *
 * IT INCLUDES THE ARTIFACT'S `.c`, NOT ITS `.h`, and that is load-bearing
 * rather than a shortcut. The D46 observability stamps -- `RX_VM_PREFILTER`,
 * `RX_VM_RUNGS`, `RX_VM_STRATS`, `RX_VM_PRUNES`, `RX_ENGINE` -- are emitted
 * into the artifact's `.c` ONLY and never into its `.h` (pcrec
 * docs/spec/match_api.md 1, 6.3). A shim that included the header would
 * compile cleanly, see none of them, and silently report a VM artifact as
 * carrying no mechanism stamps at all. MEASURED: it did exactly that before
 * this line was written. One translation unit, and the stamps are
 * preprocessor-visible -- which record_schema.md 7 names as one of the two
 * permitted sources, the other being the linked `rx_info` symbol; both are
 * used here and the declaration's `source` says which for each pair.
 *
 * WHY A SHIM AT ALL. `driver.c` must not re-declare `struct rx_info` or the
 * `<prefix>_*` entry signatures: that would be a second, drifting copy of
 * somebody else's ABI in this repo, which is precisely the failure pcrec's
 * own `tests/fuzz/pcre2_abi.h` header comment was written about ("two
 * descriptions of one thing, with nothing enforcing that they agree"). So the
 * shim `#include`s the artifact's OWN generated source -- the authoritative
 * copy, regenerated with every artifact -- and exports a small, flat,
 * engine-neutral C surface in terms of nothing but <stddef.h> types. If pcrec
 * changes `struct rx_info`, this file stops compiling; it cannot silently
 * disagree.
 *
 * The `pb_vm_*` getters are guarded by #ifdef because the VM stamps are
 * emitted on VM artifacts ONLY (record_schema.md 7: "an ABSENT pair is not an
 * error; an UNDECLARED one is"). A DFA artifact links a shim whose
 * `pb_has_vm_stamps()` returns 0, and the adapter forwards no VM pairs.
 *
 * THE ABI FLOOR (`PB_SHIM_MIN_ABI`, exported as `pb_shim_min_abi()`). This
 * shim reads six `struct rx_info` FIELDS that pcrec appended after abi 2:
 * `scan` and `prefilter` at abi 6 ([DD-13c], match_api.md 6), `match_form`
 * at abi 10 ([ENG-ABS], the runtime mirror of `RX_DFA_MATCH`), `name` and
 * `nentries` at abi 15 ([DD-13b.W1.2], [B26]) and -- since [B34], pin
 * 288d505 -- `search_form` at abi 16 ([OPT-5] STEP 2, the runtime mirror
 * of `RX_DFA_START`)
 * -- so 16 is the lowest artifact this file can read, and it says so in one
 * place instead of leaving the fact implicit in a field access. The driver
 * compares `pb_abi()` against it at load and REFUSES a lower artifact by
 * name; the adapter turns that into a clean AdapterError carrying both
 * numbers. An artifact older still does not link this shim at all
 * -- the field access is a compile error, which is the loudest possible form
 * of the same refusal and cannot be mistaken for a measurement. [B18]
 * raised the floor from 6 to 10 for exactly the reason the rule below
 * states: a FIELD was added to what this file reads; the abi 9 and abi 11
 * MACROS it also gained did not move it. Neither did abi 12's ([B19]):
 * `RX_ENGINE_SEL` and the two `_VM_PREFILTER_LANG*` macros have no
 * rx_info mirror, so an abi-10/11 artifact still links and records them
 * as "not stamped" -- and the adapter's scope table says at which abi that
 * absence stops being legitimate. Nor abi 13's ([B25]): `RX_DFA_SCAN_EDGE`
 * is a macro with no rx_info mirror (struct rx_info is byte-identical
 * between abi 12 and 13 -- MEASURED at the a7e0bdf re-pin), read through
 * #ifdef like the rest. Nor abi 14's ([B26]): [OPT-4.2]'s EIGHTH
 * `RX_ENGINE_SEL` value `"declined-nullable-default"` is a new string in an
 * existing macro, not a new surface at all. Abi 15 IS the rule's other
 * direction: two FIELDS appended after `match_form`, both read below, so
 * the floor moves with them -- 10 -> 15, the second rise in this file's
 * life and for the same stated reason as the first. Abi 16's ([B34],
 * [OPT-5] STEP 2) is the rule's THIRD firing and it is a SPLIT event: of
 * the two surfaces the pin adds, `RX_VM_FRAMELESS` is a macro with no
 * rx_info mirror (D77's "no consumer reads it at run time yet", stated in
 * match_api.md 6.3's own entry) and moves nothing, while `RX_DFA_START`
 * has one -- `search_form`, appended after `nentries` -- and this file
 * reads THE FIELD as well as the macro, exactly as it does for
 * `RX_DFA_MATCH` / `match_form`, because the pair is what lets the adapter
 * cross-check a stamp against a field instead of trusting one spelling.
 * So the floor moves again, 15 -> 16. Abi 17-22 ([B37], pin 334fd10e,
 * SIX abi steps in one re-pin) are the rule's first direction six times
 * over: `RX_DFA_UNIFORM_FOLDS` (abi 17, [CC-DIFF] STEP 1),
 * `RX_VM_ALT_ISLANDS` (abi 18, [ENG-ISL] STEP 1) and `RX_VM_ENTRY_SHAPE`
 * / `RX_VM_PROGRAM_BYTES` (abi 22, [CC-DIFF] STEP 2) are all MACROS with
 * no rx_info mirror (match_api.md 6.3 says so of each, on RX_DFA_TABLE's
 * precedent -- D77, no run-time consumer), abi 19/21 ([OPT-EDGE] STEP
 * 1/1.1) moved the emitted scan loop and no stamp, and abi 20
 * ([DD-13b.W1.3]) changed `groups[]`'s contents on COMPOSED artifacts
 * only -- `struct rx_info` gained NO member between abi 16 and abi 22
 * (MEASURED at the re-pin: the abi-16 struct block of match_api.md 6 is
 * the abi-22 one, `search_form` still the last field). So the floor
 * STAYS 16, and an abi-16..21 artifact still links this shim and records
 * the newer macros as "not stamped", the adapter's scope table saying at
 * which abi each absence stops being legitimate. Abi 23 ([B39], pin
 * d34c9131, [FORM-CHAR] STEP 1 -- PREPARED FROM SOURCE, the build
 * pending) is the first direction a seventh time: `RX_VM_CLS_FOLDS` is a
 * MACRO with no rx_info mirror ("It has no `rx_info` mirror, on the same
 * precedent and for the same reason", match_api.md 6.3's own entry), and
 * the emitter's abi-bump note at the `.abi = 23` write site
 * (src/gen/emit_dfa.c, "[FORM-CHAR] STEP 1 abi 22 -> 23") says in so
 * many words "No struct offset moves, no `rx_info` member is added".
 * `search_form` is still the last field. The floor STAYS 16.
 *
 * THE THREE STAMP FAMILIES THIS FILE READS, and the rule for each
 * (match_api.md 6.3's (a)/(b) split, tuning.md 3):
 *
 *   (a) SELECTION, unconditional: `RX_ENGINE` -- on EVERY artifact both
 *       engines produce, since abi 4. Read as a string and CROSS-CHECKED
 *       against `rx_info.engine`'s integer by the adapter.
 *   (a) SELECTION, per-MECHANISM: `RX_DFA_SCAN` / `RX_DFA_PREFILTER`
 *       (abi 4; extended to VM hybrids at abi 6), `RX_DFA_TABLE` (abi 7),
 *       `RX_DFA_PREFILTER_OFFSETS` (abi 9, [OPT-K]: WHICH offsets the
 *       offset-set filter tests, `"0,8*,13"`, or `"none"` on every other
 *       prefilter value) and `RX_DFA_SCAN_EDGE` (abi 13, [OPT-5] STEP 1,
 *       [B25]: HOW the scan tests the class of a SCAN EDGE -- a maximal
 *       run of states differing only in how many bytes of one fixed
 *       class have been counted, replaced by a bounded cursor loop and
 *       DELETED from the transition table -- `"range"` /  `"bitmap"` /
 *       `"mixed"` / `"none"`, tuning.md 2.18) and `RX_DFA_START` (abi 16,
 *       [OPT-5] STEP 2, [B34]: HOW the scan entry recovers the match
 *       START -- `"pinned"` (the forward machine's start state accepts
 *       unconditionally, so the match provably begins at `search_from`
 *       and the artifact carries NO reverse machine at all: no reverse
 *       transition, accept, byte-class, stay or scan-edge table, no
 *       `<prefix>_reverse_*` block and no backwards scan loop) or
 *       `"reverse-pass"` (that second, backwards scan), tuning.md 2.19).
 *       Present IFF the artifact
 *       CONTAINS a DFA scan -- every DFA artifact and every VM HYBRID,
 *       and no other artifact. `rx_info.scan` / `.prefilter` are the
 *       runtime mirrors of the first two and `.search_form` (abi 16) of
 *       the last; `RX_DFA_TABLE` / `_PREFILTER_OFFSETS` / `_SCAN_EDGE`
 *       have none. Note the CONSEQUENCE the pinned value carries for two
 *       of its own family: with no reverse machine to describe,
 *       `RX_DFA_TABLE` and `RX_DFA_SCAN_EDGE` fold over the forward
 *       machine alone, so a value that read `"mixed"` at abi 15 because
 *       the two machines differed can read the forward form's own value
 *       at abi 16 with no machine having changed.
 *   (a) SELECTION, per-ENTRY: `RX_DFA_MATCH` (abi 10, [ENG-ABS]) --
 *       `"unwrapped"` (a third, anchored forward machine run from
 *       ctx->pos) or `"search-filter"` (the unanchored search with
 *       non-pos starts rejected). Its scope is NOT the scan family's: it
 *       describes the artifact's `_match` ENTRY, so it is on every artifact
 *       whose RX_ENGINE is "dfa" and on NO VM artifact, hybrids included
 *       (match_api.md 6.3 says why). `rx_info.match_form` mirrors it and
 *       is NULL wherever the macro is absent.
 *   (a) SELECTION, the size term ([ART-SIZE], abi 11): `RX_UNROLL_K` /
 *       `RX_UNROLL_K_WHY` (seven values) and `RX_MAX_EMIT_CODE_BYTES` on
 *       every VM artifact; `RX_MAX_EMIT_BYTES` on EVERY artifact, both
 *       engines. The two caps are the EFFECTIVE limits the artifact was
 *       built under, so a raised cap is a recorded fact.
 *   (a) SELECTION, the engine ROUTE and the prefilter LANGUAGE ([OPT-4],
 *       abi 12, [B19]; two VALUES added at pin 263b013 with no abi bump,
 *       [B22]; an EIGHTH at abi 14, [B26]): `RX_ENGINE_SEL` -- ONE token
 *       from the registry's
 *       `engine-route` axis (`selected` / `forced` / `overflowed-dfa` /
 *       `overflowed-prefilter` / `collapsed-prefilter` / since 263b013
 *       `declined-nullable` ([OPT-4.1]: the offered count-collapsed
 *       prefilter declined as nullable, no prefilter survives) and
 *       `size-cap-retry` ([LIM-1]: the size rung's success, replacing a
 *       `selected` mislabel) / since abi 14
 *       `declined-nullable-default` ([OPT-4.2]: the same nullability
 *       policy with NO rung involved -- the ORDINARY hybrid's own EXACT
 *       prefilter language is nullable, so the prefilter is declined and
 *       the artifact reads `RX_VM_PREFILTER "none"` with no language
 *       pair, the §6.3 iff both ways, exactly as `declined-nullable`
 *       does)) on EVERY artifact,
 *       both engines (D81: `"selected"` is a fact, stamped whether or not
 *       anything fell back); it is the same decision `RX_ENGINE_WHY`
 *       narrates, as a closed set a consumer can bucket on. And
 *       `RX_VM_PREFILTER_LANG` (`"exact"` / `"count-collapsed"`) with
 *       `RX_VM_PREFILTER_LANG_WHY` (free text: `"exact"`, `"no counted
 *       repeat"`, `"forced"`, `"dfa overflow retry, exact nfa N"`, `"size
 *       cap retry, exact N > cap"`, and since 263b013 `"nullable collapsed
 *       language"` -- -fprefilter-collapse reached the nullability POLICY
 *       and the prefilter is kept on the exact language) -- and their
 *       scope is NARROWER than
 *       "every VM artifact": match_api.md 6.3 puts them on every artifact
 *       whose `RX_VM_PREFILTER` reads `"hybrid"` and on no other (a
 *       forced `--engine=vm` artifact has no prefilter and no language to
 *       stamp; MEASURED at 96e44c2, which is where pcrec's own inbox
 *       letter said "every VM artifact"). Read through #ifdef like every
 *       other macro; the adapter's scope table is what makes a missing
 *       one an error.
 *   (b) CAPACITY, VM-only: `RX_FAST_FRAMES` / `RX_FAST_TRAIL` (abi 5), the
 *       capacities the un-suffixed entries' fast tier runs on (10.9). Never
 *       absent on a VM artifact -- `RX_FAST_FRAMES == RX_RESUME_FRAMES` IS
 *       the statement "this artifact has one tier", and it is the only
 *       spelling of it.
 *   (b) ACTIVITY, VM-only: `RX_VM_FRAMELESS` (abi 16, [OPT-VMFL], [B34]) --
 *       `1` iff the emitted VM program contains NO `RX_PUSH` site and no
 *       linked call, so the fail label has no pop-and-resume `goto *`
 *       dispatch; `0` otherwise. It is (b) for `_VM_CALL_SPLICED`'s
 *       reason: nothing upstream CHOSE a frameless mode, it is what the
 *       emitted program turned out to CONTAIN. UNCONDITIONAL on every VM
 *       artifact, HYBRIDS INCLUDED, and never defined on a pure-DFA one --
 *       both values are spelled, so the fact is never read from a macro's
 *       absence. A SCALAR boolean and not a mask (the three masks beside
 *       it are per-`A_REP`; "did any site emit a push" has no
 *       per-quantifier axis to mix). No rx_info mirror, D77's reason.
 *       For this bench it is the [B32] covariate: it REPLACES the
 *       `NO RESUME FRAME AT ALL` grep over emitted C with a stamp.
 *   (c) ACTIVITY, COMMON TO BOTH ENGINES: `RX_ALTCLS_MERGES` /
 *       `RX_ALTCLS_FACTORED` (pcrec inbox I-39, [OPT-ALTCLS],
 *       src/opt/altcls.c) -- COUNTS, not booleans, of how many alternation
 *       runs of single-character branches were merged into one class
 *       (stage 1) and how many were prefix-factored (stage 2, run on
 *       stage 1's OUTPUT). Neither family (a)'s scan scope (they do not
 *       need a DFA scan) nor family (b)'s VM-only one: `pcrec_emit_prologue`
 *       emits both UNCONDITIONALLY, once per file, BEFORE either engine is
 *       built -- so they are on every artifact this shim can see, DFA and
 *       VM alike, a `--no-captures` build included (match_api.md 2082).
 *       They have been in that COMMON block since [OPT-ALTCLS], well
 *       before this file existed; what is new at abi 16 is only that this
 *       shim reads them. No rx_info mirror. `0` is a value: a pattern with
 *       no mergeable/factorable run stamps it honestly, and so does a
 *       `-fno-altcls-merge` / `-fno-altcls-factor` build (the pass checks
 *       the deny flag before touching the counter, never after, so a
 *       denial leaves no trace to tell from "nothing to do here").
 *   (b) ACTIVITY, the scan family's scope ([B37], abi 17, [CC-DIFF] STEP
 *       1): `RX_DFA_UNIFORM_FOLDS` -- an INTEGER 0..6, how many of this
 *       artifact's DFA tables (`<m>_next_state` / `<m>_is_accepting` per
 *       machine the artifact CONTAINS) had ALL-EQUAL cells and were
 *       therefore NOT EMITTED, the accessor returning the constant.
 *       Family (b) for `_VM_FRAMELESS`'s reason (no fold MODE upstream;
 *       discovered while emitting) but on the DFA-scan iff -- every DFA
 *       artifact and every VM hybrid, and no other -- exactly
 *       `RX_DFA_TABLE`'s footing, which keeps naming the encoding
 *       SELECTED even when every table folded (`"premultiplied"` with
 *       folds 4 carries no table at all). A COUNT, not a mask: a
 *       whole-artifact total with no per-A_REP axis to mix.
 *   (b) ACTIVITY, VM-only ([B37], abi 18, [ENG-ISL] STEP 1):
 *       `RX_VM_ALT_ISLANDS` -- a COUNT of the flat alternations the VM
 *       lowered as an ALTERNATION ISLAND (a trie dispatch over literal
 *       alternatives, tuning.md 2.20) rather than as `vm_alt`'s serial
 *       resume chain. UNCONDITIONAL on every VM artifact, hybrids
 *       included, never on a pure-DFA one; `0` spelled as readily as any
 *       other value. `-fno-alt-island` (bit 23) is its deny control. The
 *       first abi bump whose change reaches the VM PROGRAM region itself.
 *   (b) ACTIVITY, VM-only ([B37], abi 22, [CC-DIFF] STEP 2 / [OPT-DIAL]
 *       STEP 0): `RX_VM_ENTRY_SHAPE` -- a CLOSED TOKEN (`RX_ENGINE_SEL`'s
 *       shape, for its reason), the rung the emitter TOOK for the six
 *       entries: `plain` (one body, six framed entries), `shared` (one
 *       out-of-line body behind three forwarding entries), `forward`
 *       (three bodies in the three `_in` entries, three forwards),
 *       `inline` (six bodies, what STEP 1(a) shipped) -- and
 *       `RX_VM_PROGRAM_BYTES`, the emitted VM program size in bytes, THE
 *       quantity AUTO compared against VM_INLINE_CHAIN_MAX_BYTES (4,096,
 *       --list-limits) to choose the rung. Both UNCONDITIONAL on every VM
 *       artifact, hybrids included, never on a pure-DFA one. Two stamps
 *       and not one because four artifacts can read `plain` for four
 *       reasons (framed, forward-illegal above the term, tiered, asked
 *       for) and the outcome alone does not say which; `_VM_FRAMELESS`
 *       separates the first (a framed artifact is `plain` by
 *       construction), the size against the term the rest. Not a flags
 *       bit (`--vm-entry-shape=N` is an ordinal option, tuning.md 2.21),
 *       so there is no deny control and no registry axis for it.
 *   (b) ACTIVITY, VM-only ([B39], abi 23, [FORM-CHAR] STEP 1; PREPARED
 *       FROM SOURCE at d34c9131, the build pending): `RX_VM_CLS_FOLDS` --
 *       a COUNT of this artifact's VM class-pool entries whose membership
 *       test takes the ASCII-FOLD shape: a two-member set {B, B|0x20}
 *       with both members letters (what D23's parse-time caseless
 *       folding makes of every `(?i)` letter), tested as `(byte | 0x20)
 *       == lower` with NO 32-byte `<prefix>_class_bitmap<N>` table
 *       emitted for it (tuning.md 2.22; `vm_cls_shape` in
 *       src/gen/emit_vm.c is the one derivation the test emitter, the
 *       table emitter and this stamp all read). UNCONDITIONAL on every
 *       VM artifact, hybrids included, never on a pure-DFA one -- the
 *       DFA route's class machinery never consults `vm_cls_shape` --
 *       `0` spelled as readily as any other value. `-fno-cls-fold`
 *       (PCREC_NO_CLS_FOLD, bit 24; --list-axes `cls-fold`) is its deny
 *       control, and the flag joins emit_info_def's strategy_denials
 *       MASK on pcrec's side (the bit is masked OUT of rx_info.flags by
 *       the emitter, exactly as bit 23 is), so an artifact with no fold
 *       pair is byte-identical under the flag and nothing in this file
 *       has to mask anything. The second change ever to move the VM
 *       PROGRAM region (the island was the first).
 *
 * WHY THE MACROS ARE STILL READ THROUGH #ifdef (D81 says the EMITTER stamps
 * them unconditionally): the #ifdef is on the CONSUMER side and exists so
 * that an artifact at or above the floor but below a macro's own abi (an
 * abi-10 artifact has no RX_UNROLL_K) still links and is recorded as "not
 * stamped" -- a state record_schema.md 7 defines -- instead of failing gcc
 * with an undeclared identifier that would be filed as the ARTIFACT not
 * building. Nothing is inferred from the absence: the adapter checks that
 * every stamp pcrec calls unconditional at the artifact's own abi IS
 * present in its declared scope (`Adapter._check_agreement`'s scope table),
 * and raises when one is missing, so an unconditional stamp that went
 * silent is a contract violation, never a blank.
 *
 * NEVER INFER A FACT FROM A STAMP'S ABSENCE (pcrec I-5's hazard, which broke
 * four of pcrec's own checks the day the stamps landed). Every getter below
 * returns a NULL / 0 that the driver reports as "not stamped", and no
 * consumer of this file may read "not stamped" as "DFA", "not a hybrid", or
 * anything else. The one exception is stated in the spec as an IFF and is
 * therefore a READING rather than an inference: `rx_info.scan != NULL` on a
 * VM artifact IS "this is a hybrid" (match_api.md 6, consequence 2).
 *
 * THE CALLER-PROVIDED FRAME BUFFER (pcrec docs/spec/match_api.md 10,
 * [DD-14.FB], abi 3). The `pb_*_in` entries and the five sizing getters are
 * guarded the same way, on `RX_BUFFER_ALIGN` -- the macro every artifact
 * emitted at or after pcrec 17469b6 carries, on BOTH engines. Against an
 * older artifact (abi 2, no `_in` surface) `pb_has_in_entries()` returns 0,
 * every sizing getter returns 0, and the two `_in` wrappers return
 * PB_UNSUPPORTED (a value far below PCREC_ERR_FLOOR that no artifact can
 * produce) -- the driver refuses `--buffer-*` up front on such an artifact,
 * so the sentinel is a belt under that brace, never a code that reaches a
 * record. The descriptor (`rx_buffers`) is built HERE, so driver.c still
 * declares no pcrec type.
 */

#include <stddef.h>
#include <stdint.h>

#include PB_ARTIFACT

/* The adapter always emits with `-p rx`, but the prefix is a parameter here
 * rather than a literal, so a future adapter that needs two artifacts in one
 * process does not have to edit this file. */
#ifndef PB_SEARCH
#define PB_SEARCH      rx_search
#endif
#ifndef PB_MATCH_CAPS
#define PB_MATCH_CAPS  rx_match_caps
#endif
#ifndef PB_INFO
#define PB_INFO        rx_info
#endif
#ifndef PB_SEARCH_IN
#define PB_SEARCH_IN      rx_search_in
#endif
#ifndef PB_MATCH_CAPS_IN
#define PB_MATCH_CAPS_IN  rx_match_caps_in
#endif
#ifndef PB_BUFFERS
#define PB_BUFFERS        rx_buffers
#endif

/* Returned by the `_in` wrappers ONLY when the artifact has no `_in` surface
 * at all. Far below PCREC_ERR_FLOOR (-5) and PCREC_ERR_INTERNAL (-6): not a
 * give-up, not an internal code, nothing the harness could mistake for one. */
#define PB_UNSUPPORTED (-1000000)

/* The lowest `rx_info.abi` this file can read: abi 6 appended `scan` and
 * `prefilter` to the struct ([DD-13c]); abi 10 appended `match_form`
 * ([ENG-ABS]), which pb_info_match_form() reads; abi 15 appended `name` and
 * `nentries` ([DD-13b.W1.2]), which pb_info_name() / pb_info_nentries()
 * read; abi 16 appended `search_form` ([OPT-5] STEP 2), which
 * pb_info_search_form() reads -- so the floor is 16. Bump it only when a
 * field access below needs a newer one -- a macro this shim reads through
 * #ifdef does NOT raise the floor, because its absence is a legitimate
 * "not stamped", and abi 16's OTHER new surface, `RX_VM_FRAMELESS`, is
 * exactly such a macro. */
#define PB_SHIM_MIN_ABI 16

int pb_shim_min_abi(void) { return PB_SHIM_MIN_ABI; }

/* ------------------------------------------------- reflection (rx_info) */

int      pb_abi(void)             { return (int)PB_INFO.abi; }
int      pb_ncaps(void)           { return PB_INFO.ncaps; }
int      pb_ngroups(void)         { return PB_INFO.ngroups; }
int      pb_nnames(void)          { return PB_INFO.nnames; }
int      pb_engine(void)          { return (int)PB_INFO.engine; }
long long pb_step_budget(void)    { return (long long)PB_INFO.step_budget; }
long long pb_work_budget(void)    { return (long long)PB_INFO.work_budget; }
long long pb_frame_capacity(void) { return (long long)PB_INFO.frame_capacity; }
long long pb_subject_ceiling(void){ return (long long)PB_INFO.subject_ceiling; }
const char *pb_engine_why(void)   { return PB_INFO.engine_why; }

/* The abi-6 runtime mirrors ([DD-13c], match_api.md 6). `scan` is the DFA
 * scan the artifact CONTAINS ("unanchored" / "attempt" / "empty") or NULL
 * when it contains none; `prefilter` is the candidate-start mechanism in
 * whichever engine's vocabulary applies and is NEVER NULL -- the adapter
 * reports a NULL here as a contract violation rather than papering over it.
 * These are the FIELDS; the macros below are the other spelling, and the
 * adapter's job is to check that the two agree. */
const char *pb_info_scan(void)      { return PB_INFO.scan; }
const char *pb_info_prefilter(void) { return PB_INFO.prefilter; }

/* The abi-10 runtime mirror of RX_DFA_MATCH ([ENG-ABS], match_api.md 6):
 * "unwrapped" / "search-filter" on a DFA artifact, NULL on every VM
 * artifact, HYBRIDS INCLUDED -- its NULL rule is not `scan`'s (a hybrid
 * contains a DFA scan, but its `_match` entry is the VM's own body, which
 * this axis does not describe). The field is printed on every artifact so
 * "no anchored form here" is read from a VALUE, never from silence. */
const char *pb_info_match_form(void) { return PB_INFO.match_form; }

/* The abi-15 fields ([DD-13b.W1.2], match_api.md 6, appended after
 * `match_form` with no existing member's offset moved). `name` is what the
 * artifact IS, as against `<prefix>` (what its symbols are CALLED): a `.rxt`
 * definition built under three configs is three prefixes and ONE name. It is
 * NEVER NULL by contract -- a compile that supplies no name stamps its own
 * `<prefix>` -- so the adapter reads it as a value and treats a NULL as a
 * contract violation rather than as "unnamed". `nentries` is the length of
 * the WHOLE groups[] array; `nnames` counts the primary pattern's own named
 * groups, which are a PREFIX of it, so `nentries >= nnames` always and the
 * two are equal on every artifact pcrec emits today (what will separate
 * them is .rxt composition, [DD-13b.W1.3]). Neither has a macro spelling,
 * so neither is a two-spellings pair: they are recorded, not cross-checked
 * against a stamp. */
const char *pb_info_name(void)  { return PB_INFO.name; }
int         pb_info_nentries(void) { return PB_INFO.nentries; }

/* The abi-16 runtime mirror of RX_DFA_START ([OPT-5] STEP 2, match_api.md
 * 6, appended after `nentries` with no existing member's offset moved):
 * "pinned" / "reverse-pass" on every artifact that CONTAINS a DFA scan,
 * VM HYBRIDS INCLUDED, and NULL only on a plain VM artifact. Its NULL rule
 * is `scan`'s and NOT `match_form`'s, and the difference is the fact: a
 * hybrid inlines this emitter's SEARCH body, so it HAS a search form to
 * report, while its `_match` entry is the VM's own body and has no match
 * form. So on one hybrid artifact `match_form` is NULL while `search_form`
 * is not, and reading either as the other's proxy is wrong in a way the
 * adapter asserts against in both directions. */
const char *pb_info_search_form(void) { return PB_INFO.search_form; }

/* --------------------------------------------- the give-up code SPACE */

/* The artifact's OWN bounds on what a give-up is, so the harness classifies
 * by RANGE and never by a list it keeps in step by hand.
 *
 * pcrec's contract (D49, quoted from the emitted header): a typed give-up is
 * a return in `[PCREC_ERR_FLOOR, -2]` -- one per way the engine can give up
 * -- and the codes PROPAGATE rather than collapsing to -1. Values strictly
 * BELOW the floor are NOT give-ups: `PCREC_ERR_INTERNAL` says so in the
 * artifact itself, and anything further down is reserved for a future abort
 * semantic.
 *
 * Exporting the two numbers means a give-up code pcrec ADDS later is
 * classified correctly by an adapter nobody edited, and a reserved or
 * internal code can never be laundered into `gave-up` by an enumeration that
 * fell behind. `pb_err_name()` is for the row's `diagnostic`, which carries
 * the NAME rather than the bare integer. */

int pb_err_floor(void)    { return (int)PCREC_ERR_FLOOR; }
int pb_err_giveup_top(void) { return -2; }
int pb_err_internal(void) { return (int)PCREC_ERR_INTERNAL; }

const char *pb_err_name(int code) {
    switch (code) {
        case PCREC_ERR_STEPS:    return "PCREC_ERR_STEPS";
        case PCREC_ERR_FRAMES:   return "PCREC_ERR_FRAMES";
        case PCREC_ERR_WORK:     return "PCREC_ERR_WORK";
        case PCREC_ERR_RECURSE:  return "PCREC_ERR_RECURSE";
        case PCREC_ERR_INTERNAL: return "PCREC_ERR_INTERNAL";
        default:                 return (const char *)0;
    }
}

/* ----------------------------------- the D46 stamps (VM artifacts only) */

int pb_has_vm_stamps(void) {
#ifdef RX_VM_RUNGS
    return 1;
#else
    return 0;
#endif
}

const char *pb_vm_prefilter(void) {
#ifdef RX_VM_PREFILTER
    return RX_VM_PREFILTER;
#else
    return (const char *)0;
#endif
}

unsigned pb_vm_rungs(void) {
#ifdef RX_VM_RUNGS
    return (unsigned)RX_VM_RUNGS;
#else
    return 0u;
#endif
}

unsigned pb_vm_strats(void) {
#ifdef RX_VM_STRATS
    return (unsigned)RX_VM_STRATS;
#else
    return 0u;
#endif
}

unsigned pb_vm_prunes(void) {
#ifdef RX_VM_PRUNES
    return (unsigned)RX_VM_PRUNES;
#else
    return 0u;
#endif
}

const char *pb_engine_stamp(void) {
#ifdef RX_ENGINE
    return RX_ENGINE;
#else
    return (const char *)0;
#endif
}

/* ------------------- the DFA-SCAN stamps ([DD-13], [DD-13c], [OPT-3]) */

/* Present IFF the artifact CONTAINS a DFA scan: every DFA artifact and every
 * VM HYBRID (match_api.md 6.3 (a) states the relation as an iff and pcrec's
 * own tests/codegen/run_dfa_stamps.sh asserts it in both directions). A
 * non-hybrid VM artifact carries none of the three, and that is "no DFA
 * scan here", NOT "no stamp support" -- the difference is what
 * pb_shim_min_abi() and rx_info.scan are for. */

int pb_has_dfa_stamps(void) {
#ifdef RX_DFA_SCAN
    return 1;
#else
    return 0;
#endif
}

const char *pb_dfa_scan(void) {
#ifdef RX_DFA_SCAN
    return RX_DFA_SCAN;
#else
    return (const char *)0;
#endif
}

const char *pb_dfa_prefilter(void) {
#ifdef RX_DFA_PREFILTER
    return RX_DFA_PREFILTER;
#else
    return (const char *)0;
#endif
}

/* [OPT-3], abi 7. The ENCODING of that scan's transition table:
 * "premultiplied" / "indexed" / "mixed" / "none". No rx_info mirror exists,
 * deliberately (match_api.md 6.3 records the trigger that would make one
 * owed), so this macro is the only surface -- and its absence on an abi-6
 * artifact is "this pcrec did not stamp it", never a value. */
const char *pb_dfa_table(void) {
#ifdef RX_DFA_TABLE
    return RX_DFA_TABLE;
#else
    return (const char *)0;
#endif
}

/* [OPT-K], abi 9. WHICH offsets the offset-set candidate-start filter tests
 * -- an ascending comma-separated list of byte offsets from the candidate's
 * own start, `*` marking the one the scan searches for ("0,8*,13" on the
 * uuid shape) -- or "none" on every artifact whose RX_DFA_PREFILTER is not
 * one of the two `offset-set` values. Same scope as the three above (every
 * artifact that contains a DFA scan, hybrids included); the adapter checks
 * the "none"-iff against RX_DFA_PREFILTER in both directions. A free-text
 * fact about the individual machine, deliberately NOT folded into
 * RX_DFA_PREFILTER's closed value set (match_api.md 6.3). */
const char *pb_dfa_prefilter_offsets(void) {
#ifdef RX_DFA_PREFILTER_OFFSETS
    return RX_DFA_PREFILTER_OFFSETS;
#else
    return (const char *)0;
#endif
}

/* [OPT-5] STEP 1, abi 13 ([B25]). HOW the scan tests the class of a SCAN
 * EDGE -- the address-only bounded-scan block that replaced a counted
 * class run's interior states (tuning.md 2.18): "range" (every edge tests
 * a contiguous byte range -- subtract-and-compare against two immediates,
 * no memory touched but the subject), "bitmap" (at least one edge's class
 * is not contiguous, so its test is a 256-byte membership read -- VALUE-
 * addressed, never result-addressed, so the cursor is still the only
 * loop-carried register), "mixed" (an ARTIFACT-level composition: its
 * machines took both forms), "none" (no machine carries a collapsible
 * run; an `attempt` or `empty` scan; or -fno-scan-edge). Same scope as
 * the scan family above (every artifact that CONTAINS a DFA scan, hybrids
 * included -- match_api.md 6.3 says the iff joins unchanged); no rx_info
 * mirror. The stamp names the `scan-body` axis's chosen object; the
 * companion `scan-edge` axis (per state: edge at all?) is what
 * -fno-scan-edge denies. */
const char *pb_dfa_scan_edge(void) {
#ifdef RX_DFA_SCAN_EDGE
    return RX_DFA_SCAN_EDGE;
#else
    return (const char *)0;
#endif
}

/* [OPT-5] STEP 2, abi 16 ([B34]). HOW the search entry recovers the match
 * START (tuning.md 2.19): "pinned" -- the forward machine's start state
 * accepts UNCONDITIONALLY (at every position, under every position view,
 * in every class context), so every accept the forward loop records
 * belongs to a thread that began at `search_from` and the post-loop block
 * writes that offset directly; the artifact then carries NO REVERSE
 * MACHINE at all -- or "reverse-pass", the second, backwards scan over
 * that machine. Same scope as the scan family above (every artifact that
 * CONTAINS a DFA scan, hybrids included; match_api.md 6.3 says the iff
 * joins unchanged, and it is NOT RX_DFA_MATCH's narrower one).
 * rx_info.search_form is the mirror and the adapter's control.
 *
 * THE TWO FORMS ARE ANSWER-IDENTICAL and differ only in cost and in size:
 * caps[0][0]'s contract holds under both, absolute offsets and the
 * zero-length-match-is-a-success convention included -- the pinned form
 * DEPENDS on both rather than altering either. So a value moving between
 * pins is a COST finding and never an answer one, and the bench's
 * agreement checks are the proof of that rather than an assumption. */
const char *pb_dfa_start(void) {
#ifdef RX_DFA_START
    return RX_DFA_START;
#else
    return (const char *)0;
#endif
}

/* [ENG-ABS], abi 10. HOW the artifact's `_match` / `_match_caps` answer:
 * "unwrapped" or "search-filter". On every artifact whose RX_ENGINE is
 * "dfa" and on no other -- NOT the scan family's scope, see the header.
 * rx_info.match_form is the mirror and the adapter's control. */
const char *pb_dfa_match(void) {
#ifdef RX_DFA_MATCH
    return RX_DFA_MATCH;
#else
    return (const char *)0;
#endif
}

/* ------------------------------ the size term ([ART-SIZE], abi 11) */

/* The VM counter rung's unroll factor and WHY it is what it is: "default"
 * (the term ran, the artifact was under its threshold), "option"
 * (--unroll=K), "denied" (-fno-size-term), "size-model" (the ladder's K was
 * taken), "size-model-declined", "cap-rescue", "capacity-declined"
 * (limits.md 8, 8a). VM artifacts only: a DFA artifact has no counter rung
 * to have chosen a K for. */
int pb_has_unroll_k(void) {
#ifdef RX_UNROLL_K
    return 1;
#else
    return 0;
#endif
}

long long pb_unroll_k(void) {
#ifdef RX_UNROLL_K
    return (long long)RX_UNROLL_K;
#else
    return 0;
#endif
}

const char *pb_unroll_k_why(void) {
#ifdef RX_UNROLL_K_WHY
    return RX_UNROLL_K_WHY;
#else
    return (const char *)0;
#endif
}

/* The EFFECTIVE emitted-size caps this artifact was built under (limits.md
 * 8: the defaults, or a raise-only --max-emit-*-bytes=N override), so an
 * artifact that fitted is distinguishable from one built with a raised cap
 * without the command line. `_CODE_BYTES` bounds bytes outside table
 * initializers and is on VM artifacts only, like the quantity it bounds;
 * `_MAX_EMIT_BYTES` bounds the whole artifact and is on BOTH engines. */
int pb_has_max_emit_code_bytes(void) {
#ifdef RX_MAX_EMIT_CODE_BYTES
    return 1;
#else
    return 0;
#endif
}

long long pb_max_emit_code_bytes(void) {
#ifdef RX_MAX_EMIT_CODE_BYTES
    return (long long)RX_MAX_EMIT_CODE_BYTES;
#else
    return 0;
#endif
}

int pb_has_max_emit_bytes(void) {
#ifdef RX_MAX_EMIT_BYTES
    return 1;
#else
    return 0;
#endif
}

long long pb_max_emit_bytes(void) {
#ifdef RX_MAX_EMIT_BYTES
    return (long long)RX_MAX_EMIT_BYTES;
#else
    return 0;
#endif
}

/* --------------- the engine route and the prefilter language ([OPT-4], abi 12) */

/* `RX_ENGINE_SEL`: the engine-selection decision as ONE closed-set token,
 * on every artifact of both engines (match_api.md 6.3, "[OPT-4]
 * `<PREFIX>_ENGINE_SEL`"). It has NO rx_info mirror (on RX_DFA_TABLE's
 * precedent), so this macro is the only surface; the adapter checks it
 * against the CONFIG instead ("forced" iff the testee named `--engine=`)
 * and against the prefilter stamps it implies. */
int pb_has_engine_sel(void) {
#ifdef RX_ENGINE_SEL
    return 1;
#else
    return 0;
#endif
}

const char *pb_engine_sel(void) {
#ifdef RX_ENGINE_SEL
    return RX_ENGINE_SEL;
#else
    return (const char *)0;
#endif
}

/* `RX_VM_PREFILTER_LANG` / `_WHY`: WHICH LANGUAGE the VM's prefilter DFA
 * recognises -- the pattern's own (`"exact"`, the default under ruling B)
 * or the count-collapsed SUPERSET (`"count-collapsed"`: every X{m,n}
 * lowered to X{min(m,1),}, so the machine does not scale with the count;
 * a sound filter either way, D46). A THIRD independent selection beside
 * RX_VM_PREFILTER and RX_DFA_PREFILTER. Present IFF RX_VM_PREFILTER reads
 * "hybrid" (6.3's own iff for this pair), which is why the getter is not
 * gated on pb_has_vm_stamps(): a non-hybrid VM artifact has the D46
 * stamps and NOT these. */
int pb_has_vm_prefilter_lang(void) {
#ifdef RX_VM_PREFILTER_LANG
    return 1;
#else
    return 0;
#endif
}

const char *pb_vm_prefilter_lang(void) {
#ifdef RX_VM_PREFILTER_LANG
    return RX_VM_PREFILTER_LANG;
#else
    return (const char *)0;
#endif
}

const char *pb_vm_prefilter_lang_why(void) {
#ifdef RX_VM_PREFILTER_LANG_WHY
    return RX_VM_PREFILTER_LANG_WHY;
#else
    return (const char *)0;
#endif
}

/* ------------------------ the two-tier default entry ([OPT-1], abi 5) */

/* VM-only (6.3 family (b)) and never absent on a VM artifact. They report
 * the capacities the UN-SUFFIXED entries' fast tier runs on; no entry takes
 * them as an argument and no caller sizes anything from them -- they are
 * here so a bench row can say which side of the boundary its subjects sit
 * on (10.9's "a call that DOES escalate is SLOWER"). */

int pb_has_fast_tier(void) {
#ifdef RX_FAST_FRAMES
    return 1;
#else
    return 0;
#endif
}

long long pb_fast_frames(void) {
#ifdef RX_FAST_FRAMES
    return (long long)RX_FAST_FRAMES;
#else
    return 0;
#endif
}

long long pb_fast_trail(void) {
#ifdef RX_FAST_TRAIL
    return (long long)RX_FAST_TRAIL;
#else
    return 0;
#endif
}

/* [OPT-VMFL], abi 16 ([B34]). A (b) ACTIVITY fact, VM-only: what the
 * emitted program turned out to CONTAIN, not a mode anything chose.
 * `RX_VM_FRAMELESS` is 1 iff the artifact's VM program emits NO RX_PUSH
 * site and no linked call -- so its fail label carries no pop-and-resume
 * `goto *` dispatch -- and 0 otherwise, UNCONDITIONALLY on every VM
 * artifact including every hybrid, and on no DFA artifact.
 *
 * TWO GETTERS, not one, and the reason is this shim's own standing rule.
 * The stamp's VALUE 0 is a fact ("this program does push") and its
 * ABSENCE is a different fact ("this is not a VM artifact"); a single
 * getter returning 0 would collapse them, which is precisely the hazard
 * pcrec I-5 cost four checks. `pb_has_vm_frameless()` is the presence
 * question and `pb_vm_frameless()` answers only when it says 1.
 *
 * The guard is the macro's OWN #ifdef and not pb_has_vm_stamps(): the two
 * populations are the same today (both are "every VM artifact"), but they
 * are the same by coincidence of two independent spec sentences, and
 * gating one stamp on another's macro would hide the day they diverge. */
int pb_has_vm_frameless(void) {
#ifdef RX_VM_FRAMELESS
    return 1;
#else
    return 0;
#endif
}

int pb_vm_frameless(void) {
#ifdef RX_VM_FRAMELESS
    return (int)RX_VM_FRAMELESS;
#else
    return 0;
#endif
}

/* ---------------- the ALTERNATION -> CLASS NORMALIZATION stamps ([OPT-ALTCLS], pcrec I-39) */

/* `RX_ALTCLS_MERGES` / `RX_ALTCLS_FACTORED` have been in pcrec's COMMON
 * stamp block since [OPT-ALTCLS] -- emitted by `pcrec_emit_prologue` BEFORE
 * either engine is built, so they land on EVERY artifact this file can
 * ever see, DFA and VM alike, a `--no-captures` build included -- and this
 * shim only started reading them at abi 16 ([B34]). No rx_info mirror
 * exists for either, so the abi floor does NOT move for this addition,
 * unlike `RX_DFA_START` beside it in the same pin (which added
 * `search_form`).
 *
 * TWO GETTERS behind ONE presence question, the same shape as
 * pb_vm_frameless() and for the identical reason: `0` is a value ("this
 * pattern had nothing to merge/factor", or a denied build, which leaves
 * the counter at 0 by construction) and ABSENCE is a different fact ("this
 * pcrec predates [OPT-ALTCLS]"), so a single getter returning 0 would
 * collapse them. Both stamps land together (one emitter call), so one
 * presence question covers the pair. */
int pb_has_altcls(void) {
#ifdef RX_ALTCLS_MERGES
    return 1;
#else
    return 0;
#endif
}

long long pb_altcls_merges(void) {
#ifdef RX_ALTCLS_MERGES
    return (long long)RX_ALTCLS_MERGES;
#else
    return 0;
#endif
}

long long pb_altcls_factored(void) {
#ifdef RX_ALTCLS_FACTORED
    return (long long)RX_ALTCLS_FACTORED;
#else
    return 0;
#endif
}

/* ---------------- the abi 17-22 stamps ([B37], pin 334fd10e; six abi steps) */

/* [CC-DIFF] STEP 1, abi 17. `RX_DFA_UNIFORM_FOLDS`: how many of this
 * artifact's DFA tables had ALL-EQUAL cells and were therefore NOT emitted
 * -- the accessor returns the constant (`65535` under "premultiplied",
 * `-1` under "indexed" for `<m>_next_state`; the accept value for
 * `<m>_is_accepting`), keeping its state and class parameters so a call
 * site's `subject[pos++]` is still evaluated. Two tables per machine the
 * artifact CONTAINS (forward always; reverse unless start-pinned; anchored
 * under RX_DFA_MATCH "unwrapped"), so 0..6. SAME SCOPE AS RX_DFA_TABLE
 * (the scan family's iff: every DFA artifact and every VM hybrid, no
 * other) and deliberately NOT a fall of RX_DFA_TABLE to "none": the
 * encoding was still SELECTED and still fixes the folded constant's
 * value, so an artifact can read `"premultiplied"` with folds 4 and carry
 * no table at all -- which is exactly the pair of facts this bench's
 * [B33] (3) size witnesses are about. No rx_info mirror (D77). Family (b)
 * for RX_VM_FRAMELESS's reason: not a mode chosen upstream, a thing the
 * emitted machine turned out to CONTAIN.
 *
 * Two getters behind one presence question, the shim's standing rule:
 * `0` is a value ("every table had a varying cell") and ABSENCE is a
 * different fact ("no DFA scan here", or "a pcrec before abi 17"). */
int pb_has_dfa_uniform_folds(void) {
#ifdef RX_DFA_UNIFORM_FOLDS
    return 1;
#else
    return 0;
#endif
}

long long pb_dfa_uniform_folds(void) {
#ifdef RX_DFA_UNIFORM_FOLDS
    return (long long)RX_DFA_UNIFORM_FOLDS;
#else
    return 0;
#endif
}

/* [ENG-ISL] STEP 1, abi 18. `RX_VM_ALT_ISLANDS`: how many of this
 * artifact's flat alternations the VM lowered as an ALTERNATION ISLAND --
 * a trie over the alternatives' literal bytes (a byte compare at a
 * one-child node, a `switch` at a many-child node, one try site per node
 * where an alternative ends) -- rather than as `vm_alt`'s serial resume
 * chain of one frame per untried branch (tuning.md 2.20). Selected PER
 * ALTERNATION on the LANGUAGE (a finite set of literal byte strings within
 * the emitter's enumeration budget), so a COUNT and not a boolean: a
 * pattern with two alternations can take it for one and decline the
 * other, and "did it" would lose which. UNCONDITIONAL on every VM
 * artifact, hybrids included, never on a pure-DFA one (the DFA route
 * determinizes the same trie whether or not anyone names it). No rx_info
 * mirror. `-fno-alt-island` (PCREC_NO_ALT_ISLAND, bit 23) is the deny
 * control that reaches 0 on a pattern that would otherwise take it. */
int pb_has_vm_alt_islands(void) {
#ifdef RX_VM_ALT_ISLANDS
    return 1;
#else
    return 0;
#endif
}

long long pb_vm_alt_islands(void) {
#ifdef RX_VM_ALT_ISLANDS
    return (long long)RX_VM_ALT_ISLANDS;
#else
    return 0;
#endif
}

/* [CC-DIFF] STEP 2 + [OPT-DIAL] STEP 0, abi 22. `RX_VM_ENTRY_SHAPE`: the
 * rung the emitter TOOK for this artifact's six entries -- "plain" (one
 * body, six framed entries), "shared" (one out-of-line `noinline` body
 * behind three forwarding un-suffixed entries), "forward" (three bodies
 * in the three `_in` entries, three forwards; no canary anywhere) or
 * "inline" (six bodies, what STEP 1(a) shipped) -- a CLOSED TOKEN whose
 * value set is fixed at four by the emitter's own enum (tuning.md 2.21).
 * And `RX_VM_PROGRAM_BYTES`: the artifact's emitted VM program size in
 * bytes, THE quantity AUTO compared against VM_INLINE_CHAIN_MAX_BYTES
 * (4,096, --list-limits) when it chose the rung -- at or below it
 * `forward` (or `inline` where a forward rung is illegal: the artifact
 * must provably never WRITE its working storage -- no RX_PUSH, no linked
 * call, no RX_SET), above it `shared` (or `plain`). A FRAMED artifact
 * (RX_VM_FRAMELESS 0) is `plain` whatever is asked. Both UNCONDITIONAL on
 * every VM artifact, hybrids included, never on a pure-DFA one; both
 * SCALARS, no rx_info mirror, family (b). Answer-identical across every
 * value: what moves is the entry scaffolding above `goto <prefix>_L0;`.
 *
 * WHY TWO MACROS AND NOT ONE (match_api.md 6.3): four artifacts can stamp
 * "plain" for four different reasons -- framed, forward-illegal above
 * the term, tiered, or asked for -- and the shape alone does not
 * distinguish them; the program size against the stamped limit does. A
 * stamp whose outcome is visible and whose input is not is a fact a
 * reader can see and cannot CHECK.
 *
 * Read behind ONE presence question for the pair (one emitter call lands
 * both) -- the same shape as pb_altcls_*. */
int pb_has_vm_entry_shape(void) {
#ifdef RX_VM_ENTRY_SHAPE
    return 1;
#else
    return 0;
#endif
}

const char *pb_vm_entry_shape(void) {
#ifdef RX_VM_ENTRY_SHAPE
    return RX_VM_ENTRY_SHAPE;
#else
    return (const char *)0;
#endif
}

long long pb_vm_program_bytes(void) {
#ifdef RX_VM_PROGRAM_BYTES
    return (long long)RX_VM_PROGRAM_BYTES;
#else
    return 0;
#endif
}

/* ---------------- the abi 23 stamp ([B39], pin d34c9131; [FORM-CHAR] STEP 1)
 * PREPARED FROM SOURCE (lane b39prep, 2026-09-05): the macro name, its
 * scope and its deny flag are read from pcrec's src/gen/emit_vm.c,
 * docs/spec/match_api.md 6.3 and docs/spec/tuning.md 2.22 at the SHA; the
 * build + `make check` are what prove the read on a real artifact. */

/* [FORM-CHAR] STEP 1, abi 23. `RX_VM_CLS_FOLDS`: how many of this
 * artifact's VM class-pool entries take the ASCII-FOLD membership-test
 * shape -- a two-member set {B, B|0x20}, both letters (exactly what D23's
 * parse-time caseless folding produces; `vm_cls_shape`'s recognizer is
 * `count == 2 && (lo ^ hi) == 0x20 && lo >= 'A' && lo <= 'Z'`), tested as
 * `(byte | 0x20) == lower` -- one or-mask and one compare, which gcc -O2
 * compiles to mask + compare + sete with NO LOAD -- with the class's
 * 32-byte `<prefix>_class_bitmap<N>` table NOT emitted at all. The count
 * is `vm_cls_shape`'s own aggregation over the FINAL pool (the program
 * was emitted before the stamp line runs), and distinct pool entries are
 * distinct sets, so distinct fold classes carry distinct compare
 * constants: a structural check can hold this number to the artifact's
 * own text. UNCONDITIONAL on every VM artifact, hybrids included, never
 * on a pure-DFA one (match_api.md 6.3: "the DFA route's class machinery
 * ... never consults vm_cls_shape, so there is nothing there to
 * report"); a COUNT and not a boolean on RX_VM_ALT_ISLANDS' precedent
 * (the shape is selected PER POOL CLASS, so a pattern mixes fold-pair
 * positions with bitmap classes). No rx_info mirror (D77). Family (b):
 * not a mode chosen upstream, a thing the emitted program turned out to
 * CONTAIN. `-fno-cls-fold` (bit 24) is the deny control that reaches 0
 * on a pattern that would otherwise take it -- and restores the tables.
 *
 * Two getters behind one presence question, the shim's standing rule:
 * `0` is a value ("no pool class was a fold pair", or a denied build) and
 * ABSENCE is a different fact ("not a VM artifact", or a pcrec before
 * abi 23). */
int pb_has_vm_cls_folds(void) {
#ifdef RX_VM_CLS_FOLDS
    return 1;
#else
    return 0;
#endif
}

long long pb_vm_cls_folds(void) {
#ifdef RX_VM_CLS_FOLDS
    return (long long)RX_VM_CLS_FOLDS;
#else
    return 0;
#endif
}

/* ------------------------------------------------------------- matching */

/* Unanchored search from `pos`; `caps` is `pb_ncaps()` pairs.
 * Returns 1 = match, 0 = no match, negative = a typed give-up (D49: the
 * codes PROPAGATE and are NOT collapsed to -1, so the driver reports the
 * number it got). */
int pb_search(const unsigned char *s, size_t n, size_t pos,
              ptrdiff_t (*caps)[2]) {
    return PB_SEARCH(s, n, pos, caps);
}

/* Anchored at `pos`, capture-delivering. Returns the matched LENGTH (>= 0),
 * -1 on no match, or a typed give-up code.
 *
 * THE WHOLE-SUBJECT QUESTION IS THE CALLER'S. pcrec has no end-anchor
 * option, so "does the whole subject match" is answered by the driver as
 * `pb_match_caps(...) == n`. That is a SUFFICIENT test and not a necessary
 * one: a pattern whose leftmost-first anchored match is a strict prefix,
 * but which could reach the subject's end by backtracking, answers `no`
 * here where PCRE2_ANCHORED|PCRE2_ENDANCHORED answers `yes`. The asymmetry
 * is real, it is documented in testees/pcrec/CLAUDE.md, and on this
 * sub-bench it was MEASURED not to bite (85/85 agreement, both patterns). */
long long pb_match_caps(const unsigned char *s, size_t n, size_t pos,
                        ptrdiff_t (*caps)[2]) {
    rx_ctx ctx;
    ctx.subject = s;
    ctx.len = n;
    ctx.pos = pos;
    ctx.ncap = 0;
    ctx.caps = (const ptrdiff_t (*)[2])0;
    ctx.user = (void *)0;
    return (long long)PB_MATCH_CAPS(&ctx, caps);
}

/* ----------------------------- the caller-provided frame buffer (10) */

/* The sizing surface, READ from the macros the artifact's header publishes
 * (match_api.md 10.4): `<PREFIX>_RESUME_FRAMES` / `_TRAIL_FRAMES` are the
 * stamped DEFAULT capacities, `_RESUME_FRAME_SIZE` / `_TRAIL_FRAME_SIZE` the
 * bytes per frame / per trail entry FOR THIS ARTIFACT (24 B on a call-free VM
 * artifact, 40 on a call-bearing one -- never hardcode), `_BUFFER_ALIGN` the
 * alignment both regions need. At abi 3 the same four counts are also
 * `rx_info` fields; the macros are what the artifact _Static_asserts against
 * its real sizeof/_Alignof, so they are the copy read here.
 *
 * A STAMPED SIZE OF 0 MEANS "THIS ENGINE TAKES NO BUFFERS" (every DFA
 * artifact). Dividing by it is the documented mistake; the driver tests the
 * size before it sizes anything and passes no descriptor when it is 0. */

int pb_has_in_entries(void) {
#ifdef RX_BUFFER_ALIGN
    return 1;
#else
    return 0;
#endif
}

long long pb_buffer_align(void) {
#ifdef RX_BUFFER_ALIGN
    return (long long)RX_BUFFER_ALIGN;
#else
    return 0;
#endif
}

long long pb_resume_frames(void) {
#ifdef RX_RESUME_FRAMES
    return (long long)RX_RESUME_FRAMES;
#else
    return 0;
#endif
}

long long pb_trail_frames(void) {
#ifdef RX_TRAIL_FRAMES
    return (long long)RX_TRAIL_FRAMES;
#else
    return 0;
#endif
}

long long pb_resume_frame_size(void) {
#ifdef RX_RESUME_FRAME_SIZE
    return (long long)RX_RESUME_FRAME_SIZE;
#else
    return 0;
#endif
}

long long pb_trail_frame_size(void) {
#ifdef RX_TRAIL_FRAME_SIZE
    return (long long)RX_TRAIL_FRAME_SIZE;
#else
    return 0;
#endif
}

/* `<prefix>_search_in` with a descriptor built here from the driver's two
 * regions and two CAPACITIES (frames and entries, never bytes -- 10.2).
 * Same return space as pb_search(). 10.3's promises the driver relies on:
 * a NULL descriptor is exactly the plain call; a give-up is retryable; the
 * regions are pure scratch; PCREC_ERR_FRAMES does not say whose buffer ran
 * out. Both regions are required when either is given. */
int pb_search_in(const unsigned char *s, size_t n, size_t pos,
                 ptrdiff_t (*caps)[2],
                 void *frames, size_t nframes, void *trail, size_t ntrail) {
#ifdef RX_BUFFER_ALIGN
    PB_BUFFERS buf;
    if (!frames && !trail) return PB_SEARCH_IN(s, n, pos, caps, (const PB_BUFFERS *)0);
    buf.frames = frames; buf.nframes = nframes;
    buf.trail = trail;   buf.ntrail = ntrail;
    return PB_SEARCH_IN(s, n, pos, caps, &buf);
#else
    (void)s; (void)n; (void)pos; (void)caps;
    (void)frames; (void)nframes; (void)trail; (void)ntrail;
    return PB_UNSUPPORTED;
#endif
}

/* `<prefix>_match_caps_in`: pb_match_caps() with the descriptor. Same
 * whole-subject caveat as pb_match_caps(). */
long long pb_match_caps_in(const unsigned char *s, size_t n, size_t pos,
                           ptrdiff_t (*caps)[2],
                           void *frames, size_t nframes,
                           void *trail, size_t ntrail) {
#ifdef RX_BUFFER_ALIGN
    PB_BUFFERS buf;
    rx_ctx ctx;
    ctx.subject = s;
    ctx.len = n;
    ctx.pos = pos;
    ctx.ncap = 0;
    ctx.caps = (const ptrdiff_t (*)[2])0;
    ctx.user = (void *)0;
    if (!frames && !trail)
        return (long long)PB_MATCH_CAPS_IN(&ctx, caps, (const PB_BUFFERS *)0);
    buf.frames = frames; buf.nframes = nframes;
    buf.trail = trail;   buf.ntrail = ntrail;
    return (long long)PB_MATCH_CAPS_IN(&ctx, caps, &buf);
#else
    (void)s; (void)n; (void)pos; (void)caps;
    (void)frames; (void)nframes; (void)trail; (void)ntrail;
    return PB_UNSUPPORTED;
#endif
}
