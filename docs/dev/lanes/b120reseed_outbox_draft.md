# DRAFT — notes toward an eventual answer to inbox I-124 (for the manager; not written to outbox_to_pcrec.md)

**Nothing is ready to send yet.** I-124 asks for TIMING (items 1-2) and
a roster-wide >5%-slower census (item 3); this lane (phases A+B) did
compile-only census and testee-registry work only — no answer-identity
check has run, no ratio has been measured. Sending anything to pcrec
before Phase C runs would be reporting a prediction as a finding, which
I-124's own closing line explicitly asks NOT to do ("a cell whose
answer moves is a finding, to be reported before any timing").

**What IS worth keeping in mind for the eventual O-n**, once Phase C
has numbers:

- Phase A's population finding is itself a fact pcrec's own [B118]
  entry did not have: `RX_VM_RESEED` reaches `adaptive*` on exactly 15
  distinct patterns across three sets (capability, syntax, utf8) in
  this project's whole corpus, and NEVER on email/altwide/bounded/
  litrun. If item 3's window finds no >5%-slower cell outside the
  (syntax lka-*, utf8 asr-lb-*, capability logparse-atomic) population
  this file already names, that is a clean closed-set finding worth
  one line in the eventual O-n ("checked the whole roster; the
  XCALL-trigger population is exactly these N cells, no others").
- `capability/logparse-atomic` is the roster's ONLY `adaptive-dense`
  witness. If item 3's window finds it moves (or doesn't), that is a
  single, clean, nameable data point for [OPT-HYB-RESEED-XCALL]'s own
  trigger population — worth citing by pattern name, not by set.
- The clang+utf8 testee pair built here
  (`pcrec-auto-clang-utf8`/`pcrec-auto-clang-nohybreseed-utf8`) is new
  axis-crossing territory (no prior `-utf8`+`-clang` combo existed on
  this roster). If Phase C's standalone probe finds a compiler-split
  result the way `[B109]`'s own `asr-lb-fixed` witness did (gcc vs
  clang disagreeing on direction, not just magnitude), that is exactly
  the shape of finding O-68 already reported once and pcrec may want
  it folded into the same thread rather than a fresh O-n.

No draft outbox text is written beyond these notes: there is nothing
here that answers I-124's own asks, and a draft O-n with "TBD" numbers
is worse than no draft at all.
