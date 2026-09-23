# R8 — `utf8_set_v1.md` v0.1, critic panel: CHARTER FIDELITY + REPO CONSISTENCY

**Reviewer**: read-only critic, D6 panel r8, 2026-09-23. Lens: does I-90's
charter genuinely get satisfied where the note claims it does, with every
narrowing declared; and does the note's design agree with the repo as it
actually stands (axes, shared surfaces, conventions, build-plan
completeness)? No builds, no engines, no timing were run. Subject:
`docs/design/utf8_set_v1.md` v0.1 (all fifteen sections read) + inbox
`I-90` (`docs/dev/inbox_from_pcrec.md`).

Method: I-90's five clauses were re-read against §1's traceability table and
against the sections it cites; the twelve `~/pcrec/tests/utf8/axisNN_*.rxt`
files were read from their own header comments (not from the note) and
diffed against §3.1/§3.2; every cross-repo citation the note makes to
`pcrecbench/`, `testees/*/driver.c(c)`, `schema/`, and `bench/syntax/NOTES.md`
was independently greped and read at the cited line.

---

## Findings

### F-C1 — BLOCKER: §7.1/§7.2's pcrec roster claim ("configs.toml only, no adapter code changes") is technically wrong

**Claim under test.** §7.1's table, pcrec row: *"the adapter change,
concretely: `configs.toml` only: four rows whose `flags` carry `"-e",
"utf8"`. Because `flags` land in `build_flags` AND in the derived
`testee_id`, the encoding becomes an IDENTITY exactly the way `-bigcap` and
`-noclsfold` already are — no adapter code changes."* §7.2 repeats this:
*"The important property is that `-e utf8` goes in `configs.toml`'s `flags`
list... Proposed ids... deriving `config_extra = utf8`... the same escape
hatch `pcrec-*-bigcap` ([B31]) and the `-clang` siblings ([B24]) already
use."*

**What the adapter actually does** (`testees/pcrec/adapter.py`):

- `compose_config_extra()` (`:2448-2462`) is called with exactly **four
  fixed positional parts** at its one call site (`:2987-2989`):
  `cc_extra, cfg.get("cap_extra"), cfg.get("deny_extra"),
  cfg.get("cflags_extra")`. There is no generic "scan `flags` for anything
  interesting" step — each part is produced by its own dedicated function.
- `effective_denies(flags)` (`:2326-2338`) derives `deny_extra` by matching
  `flags` **only** against the literal strings in the closed `DENY_FLAGS`
  tuple (`:2252-2325`: `-fno-scan-edge`, `-fno-start-pinned`,
  `-fno-alt-island`, `-fno-cls-fold`, …). `-e`/`--encoding=` is not a member.
- `effective_caps(testee_id, cfg, flags)` (`:2154-2192`) derives `cap_extra`
  by matching `flags` **only** against the `--max-emit-bytes=` /
  `--max-emit-code-bytes=` prefixes in `CAP_KEYS`. Same story.
- `cflags_extra` comes from a **separate config key**, `cfg["cflags"]`
  (`:2409-2462`), never from `flags` at all.

So putting `"-e", "utf8"` into a config's `flags` list would land in the raw
pcrec argv and therefore in `build_flags` (visible there, as the note
claims) — but it would **not** touch `config_extra`, because nothing reads
`flags` for an encoding token. `derive_testee_id` (cited throughout
`tools/selfcheck.py`, e.g. `:6063`, `:6512`, `:6774`) builds the id from
`config_extra`, not from `build_flags` directly (`record_schema.md §6.4`,
X5: "the id is derived from `config_extra` whole"). Two of the four new
configs the note proposes (`pcrec-auto-utf8` vs `pcrec-auto`) would
therefore derive the **same** `testee_id` unless a fifth axis is built:

1. new recognition logic paralleling `effective_denies`/`effective_caps`
   (an `effective_encoding()` or equivalent) that scans `flags` for
   `-e`/`--encoding=` and returns an `encoding_extra` token, and
2. a **code edit** to the `compose_config_extra(...)` call site
   (`:2987-2989`) adding that fifth positional argument, in chartering
   order (which the file's own doc-comment, `:36-38`, says is a rule this
   set would have to extend, not "no code changes").

This is exactly what the frozen-renderer checks in `tools/selfcheck.py`
exist to catch (`check_testee_id_frozen`-shaped checks at `:6063-6076`,
`:6512-6541`: "derived `testee_id` is no longer the frozen one" /
"`config_extra` is %r, was %r") — but only for CONFIGS ALREADY IN THE
FROZEN SET. A newly-added `pcrec-auto-utf8` row wouldn't fail any existing
check; it would silently ship with the wrong (non-unique) identity, which
`bigcap`/`cflags`/`noclsfold` all avoid precisely because each of those
axes *did* get its own recognition function and its own slot in
`compose_config_extra`.

**Why this matters at BLOCKER severity.** §13's build plan puts this whole
axis in U2 as "the new configs per engine (§7.1)" with no code-change line
item, and §1.1's traceability table marks I-90 clause 4 (pcrec testees)
"SATISFIED by §7.2" without qualification. A build lane reading §7.1/§7.2
literally opens U2 believing it is four TOML rows; what it needs is a
fifth `compose_config_extra` axis, mirroring `effective_denies`'s shape,
before the four rows can safely exist side-by-side with their byte-mode
siblings in the store. This is precisely the class of thing the store's
identity rules (record_schema.md X5) exist to prevent going wrong quietly.

**Disposition**: fix §7.1's pcrec row and §7.2 to name the adapter change
explicitly (a new encoding-recognition function + the `compose_config_extra`
call-site edit), and add it as a stated deliverable of U2 in §13. Until
then this note should not be read as licensing "configs.toml-only" work.

---

### F-C2 — MAJOR: "three adapters cite that family by name" is not supported by the repo

**Claim under test**, §7 (opening paragraph, before the surface table):
*"That is not an oversight — it is what makes `bench/capability`'s family
12 (`binary-nonutf8`) measurable at all, and **three adapters cite that
family by name** as the reason."*

**Grep result** across every testee's `driver.c`/`driver.cc`/`CLAUDE.md`
for the literal strings `family 12` / `binary-nonutf8`: they appear in
exactly **one** adapter — `testees/re2/driver.cc:27` and
`testees/re2/CLAUDE.md:102-103`. No other adapter (`onig`, `vectorscan`,
`pcre2`, `tre`, `rust`) names "family 12" or "binary-nonutf8" anywhere.
`onig` and `vectorscan` do cite the REQUIRES **token** `non-utf8-subject`
(`onig/driver.c:19-22` prose + `onig/CLAUDE.md:202`; `vectorscan/
driver.c:56-59`) as their reason for staying byte-mode — a real citation,
but of the token the family scores against, not of "family 12" by name as
the note asserts.

This matters here specifically because §0 of the note states its own
discipline as a selling point: *"Facts about this repo's own adapters are
cited... by `file:line`... and were read, not assumed."* This is one of
the few claims in the note that is checkable by grep alone and does not
survive the check.

**Disposition**: correct to something like "one adapter (re2) cites the
family by name (`binary-nonutf8`); two more (onig, vectorscan) cite the
`non-utf8-subject` token it scores, without naming the family." Everything
downstream of this sentence (the byte-mode-by-design framing, §7.1's table)
is unaffected — this is a citation-accuracy defect, not a design defect.

---

### F-C3 — MAJOR, undeclared narrowing: family (a) does not deliver \d/\s with-and-without-UCP, though I-90 asks for it and §1.1 claims full satisfaction

**I-90 clause 3(a), verbatim**: *"(a) CLASSES (Frank's own example): ranges
spanning the 1-byte/multi-byte boundary (...), negated classes (...),
classes mixing ASCII and high members, `.` under utf8 (...), **`\w`/`\d`/`\s`
with and without UCP**."*

**§5(a)'s actual 14 members**: `\w` gets the full pair
(`cls-w-ascii`/`cls-w-ucp`, both authored, `requires=ascii-class-scope` /
`unicode-class-scope`). `\d` gets **only** `cls-d-ascii` (ASCII-scope,
`requires=ascii-class-scope`) — no `unicode-class-scope` twin exists
anywhere in the 74-pattern set. `\s` gets **only** `cls-s-nbsp` (same
shape, same gap). Contrast with family (e), where the analogous `\b`
construct **does** get its full pair (`asr-b-cyr`/`asr-b-cyr-ucp`,
§5(e)) — so the omission for `\d`/`\s` reads as inconsistent authoring
rather than a reasoned cut.

§1.1's traceability table marks I-90 clause 3 "SATISFIED by §5 (the six
first-release families...)" with no caveat, and neither §2, §5, §14 nor
§15 states or argues this narrowing anywhere. This is exactly the shape
the brief's "somewhat complete... any functionality which might be
affected by encoding" standard is meant to catch: a silent narrowing of
a clause Frank wrote out by name ("Classes come to mind" — his own
illustrative example for the whole charter).

**Disposition**: either author the two missing UCP twins (`cls-d-ucp`,
`cls-s-ucp` — two more (a) members, bringing family (a) to 16) or add one
sentence to §5(a) and §1.1 stating the narrowing and its reason (e.g., "the
UCP widening mechanism is already witnessed once by `cls-w-ucp`; `\d`/`\s`
add no new mechanism beyond it, so only `\w` carries the pair" — the same
kind of reasoning `capability_set_v1.md` §2.4 uses to prune duplicate
coverage). Either is fine; the silence is not.

---

### F-C4 — MINOR: quote fidelity, §2.2's citation of `bench/syntax/NOTES.md`

§2.2 renders, in quotation marks, as apparently a direct quotation:
*"the seed's rows re-read with `status`/`family` unchanged and the
utf-only rows moving from `not-exercised` to `covered`."*

The actual source, `bench/syntax/NOTES.md:363-364`:
*"**The** seed's rows **would be** re-read with `status`/`family`
unchanged and the utf-only rows moving from `not-exercised` to
`covered`."*

The quotation drops "The" and, more substantively, "would be" — turning a
conditional description of what a future `syntaxutf` build *would* do into
a flat present-tense claim. Low stakes on its own, but this is the
paragraph arguing why `bench/utf8` and the reserved `bench/syntaxutf/`
slot are different sets and can coexist (§2.2, feeding Q5, which the note
itself marks BLOCK) — exactly the place where quote precision earns its
keep, and exactly the kind of citation the note's §0 promises to get right.

**Disposition**: restore the verbatim wording, or drop the quotation marks
in favor of a paraphrase.

---

### F-C5 — MINOR: §13's U1 dependency cell contradicts the very next row

§13's table, U1 row, "depends on" column: *"§8.1, §8.4, §7.5 — **nothing
else can start**."* Read literally this says no other lane may begin
before U1 lands. The U3 row two lines down is explicitly marked *"—
(parallel with U1/U2)"*, and U5 depends on U1+U3+U4 (implying U3/U4's work
product exists independently of U1's completion). The prose immediately
below the table ("U1 is the one that cannot be parallelised away... its
acceptance is that every existing set's `expectations.tsv` re-derives
byte-identically... That check is the lane's first deliverable, not its
last") clarifies the intended meaning — U1 itself has no prerequisite and
must not be skipped or deferred — but the table cell, read on its own,
says the opposite of U3's row.

**Disposition**: reword the U1 cell (e.g., "— none; U1 is the entry point
and its own acceptance check must pass before U5 reads its output") so
the table doesn't need the prose underneath to resolve an apparent
self-contradiction — a real risk given `plan.md`/lane briefs are grepped
and skimmed under time pressure per this project's own working style.

---

### F-C6 — NOTE (non-blocking): I-90 clause 5's population is wider than P1's

I-90 clause 5 names "the offset-skip rows (**any pattern** with a
fixed-offset literal prefix)" as a first-customer class. §11's P1
operationalizes this as exactly one order pair
(`lit-offset-at-head`/`lit-offset-at-tail`). Other authored members
plausibly fit "a pattern with a fixed-offset literal prefix" —
`lit-run-3`, `lit-mixed-ascii`, `alt-shared-char` — and are not named in
any prediction. §1.1 marks clause 5 "SATISFIED by §11" without flagging
that only the sharpest pair is formally scored; the rest is left to R6's
ledger reading, which is defensible (predictions must pick concrete
witnesses) but not stated.

**Disposition**: not blocking. One sentence in §1.1 or §11 ("P1 witnesses
the sharpest cell in the broader offset-skip population that I-90 clause 5
names; the rest is read in the ledger under R6") would close the gap
between I-90's plural ("rows") and P1's singular population explicitly,
matching this note's own stated standard of declared-not-silent narrowing.

---

## What was checked and found CLEAN (stated per the "context around the
numbers" convention — what was read and what wasn't)

- **The twelve-axis table (§3.1)** was independently re-derived from each
  `~/pcrec/tests/utf8/axisNN_*.rxt` file's own header comment (not from the
  note) and matches on every axis, several near-verbatim (axis 08's
  `PCRE2_INFO_MAXLOOKBEHIND==1`, axis 11's "CANDIDATE MATCH STARTS ARE
  CHARACTER BOUNDARIES", axis 12's Script/Script_Extensions sentence). No
  misnaming or misreading found. The gap claims (§3.3: axes 3/10/caller-11
  deferred, axis 5's permanent partial coverage, axis 11's structural
  unreachability) are consistent with what the axis files themselves show
  is already CORRECTNESS-complete on pcrec's side — the note's gaps are
  about this bench's SPEED cells, a different and correctly-scoped claim.
- **U1's "six existing sets" claim** (email, loglines, bounded, altwide,
  syntax, capability) matches `ls bench/` exactly — no seventh set exists
  today, so the byte-identical re-derivation obligation is scoped correctly.
- **`oracle_pcre2.py`'s two named lines** (`:47` `PCRE2_UTF = ...  # not
  used: this module stays byte-oriented like pcrec`; `:308`'s "this bench
  never compiles a utf8 artifact" docstring) are quoted correctly and are
  exactly the two lines §8.1/§8.4 say stop being true.
- **`pcrecbench/capability.py`'s REQUIRES_VOCAB**: confirmed 17 members,
  closed and global, gated by `CapabilityError` on an unknown token exactly
  as §7.5 describes; the three proposed additions are additive (no existing
  token's meaning changes), which is the strongest argument for Q3's
  DEFAULT (keep it global) not needing BLOCK severity.
- **§7.1's per-engine byte-mode citations** (pcre2 `driver.c` hard-coded
  `0` options word, re2 `EncodingLatin1`, onig's compile-time
  `ONIG_DRIVER_ENCODING`, vectorscan's `VS_DRIVER_FLAGS = 0` and its
  measured `\b`/UCP A/B numbers, tre's byte-literal convention) were all
  read at the cited lines and match, including the exact "40/64... 35/64"
  figures in §7.6.
- **Schema surface**: `config_extra` is a `$defs/slug`-typed field
  (`schema/record.schema.json:447`) and `tags` is a free string array
  (`:309`) — confirming the note's implicit answer to "does this need a new
  schema field" (no: `config_extra` + `requires-*` tags already carry
  everything this set needs) is correct, even though the note never states
  the question or its answer explicitly. Not a finding, but worth recording
  since it was one of the brief's specific checks and the answer is "the
  existing surface, verified, not merely assumed."
- **`make check` enumeration**: `tools/selfcheck.py`'s `subbench_dirs()` is
  a real generic directory walk (multiple call sites, e.g. `:185-232`,
  `:2022`, `:2200`, `:2320`, `:8185`, `:9523`) — confirms the note's
  (unstated but relied-upon) assumption that `bench/utf8/` needs no gate
  registration to be picked up by the generic checks.
- **Not checked** (out of this lens, or requires a build/run this critic's
  mandate forbids): whether the §10.3 timing arithmetic (~40-45 min/cell)
  is realistic: whether the five word-pool generators are achievable as
  scoped; whether onig's runtime-encoding-choice change (§7.1) is as small
  as claimed (a build-lane question, not a charter/consistency one);
  U2's WITNESS-COMPILE claims about RE2/Rust/Onig Script_Extensions
  support (explicitly marked UNCONFIRMED by the note itself, correctly).

---

## Verdict

The note earns its stated shape — the twelve-axis coverage spine is read
correctly against pcrec's own source and its gaps are honestly scoped, the
byte-mode roster survey is accurate at every citation this reviewer could
independently check except one, and most of I-90's five clauses are
genuinely satisfied where §1.1 claims they are. But two things pull this
below "ready to open lanes as written": F-C1 is a load-bearing technical
error — the note's central identity claim for the pcrec roster axis
(§7.1/§7.2, "configs.toml only, no adapter code changes") does not survive
reading `testees/pcrec/adapter.py`'s actual `compose_config_extra`
mechanism, and a lane opening U2 on this text as given would ship four new
testees at risk of colliding on `testee_id` with their byte-mode siblings;
and F-C3 is exactly the failure mode Frank's charter warns against by
name — a silent narrowing of the one family he gave as his own worked
example, undetected by the note's own traceability table. F-C2 (the
"three adapters" citation) is a smaller but real breach of the note's own
stated citation discipline, valuable mainly as a reminder that a
plausible-sounding cross-adapter claim in this style of document still
needs a grep before it ships. None of the findings requires re-designing
any section; all three substantive ones (F-C1, F-C2, F-C3) are one-to-two
paragraph fixes, and F-C4/F-C5/F-C6 are copy-edits. Recommend: fix F-C1
and F-C3 before U2/U4 open (F-C1 blocks U2 concretely; F-C3 should block
U4's family-(a) authoring or be explicitly ruled a deliberate cut first),
correct F-C2 in the same pass, and fold F-C4/F-C5/F-C6 in at no extra cost.

**Counts by severity**: 1 blocker (F-C1), 2 major (F-C2, F-C3), 2 minor
(F-C4, F-C5), 1 note (F-C6).

**Top three findings**:
1. **F-C1 (blocker)** — §7.1/§7.2's "configs.toml only, no adapter code
   changes" for the four new pcrec `-e utf8` configs is wrong:
   `compose_config_extra()` takes four fixed parts derived from closed,
   hardcoded flag tables (`DENY_FLAGS`, `CAP_KEYS`) that do not recognize
   `-e`/`--encoding=`, so the proposed configs would not get a distinct
   `testee_id` without a new adapter axis and a call-site edit that §13
   never lists as U2's work.
2. **F-C3 (major)** — I-90 clause 3(a)'s explicit "`\w`/`\d`/`\s` with and
   without UCP" is only half-delivered: `\w` gets the pair, `\d`/`\s` each
   get only the ASCII-scope member, and §1.1 marks the clause fully
   satisfied without saying so — an undeclared narrowing of Frank's own
   named example.
3. **F-C2 (major)** — "three adapters cite [family 12] by name" is
   unsupported; only `re2` does, in both `driver.cc` and `CLAUDE.md`; the
   other two cited adapters (onig, vectorscan) name the `non-utf8-subject`
   token, not the family — a citation-accuracy miss in a note whose own
   §0 commits to reading rather than assuming such facts.
