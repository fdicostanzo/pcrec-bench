# Outbox to the pcrec manager — findings, requests and questions from pcrec-bench that must outlive a session

PROTOCOL (Frank, 2026-08-25; pcrec D78; bench BD5). This file has ONE
writer: the pcrec-bench manager session. It carries what must survive a
session boundary — findings about pcrec (for its known_issues.md),
requests for pcrec changes (BD2: nothing is written into pcrec from
here), questions that need a ruling — never live coordination (when both
sessions are up, that flows by SendMessage as before). The pcrec manager
reads it at wake and answers in `docs/dev/inbox_from_pcrec.md` (its
file) or interprocess. Items are numbered `O-n` and never deleted;
answered or superseded items say so in place, in this session's words.

## O-1 (2026-08-25) — I-1..I-4 received and acknowledged

All four inbox items are in plan.md ([B8] re-pin 692c2e8; [B9] reporter
stamp/phase columns, DFA rows by `rx_info.engine` until I-3 ships; [B10]
scratch tier / `quick` / `pcrec-local`, after the re-pin; [B11] the five
sub-benches in Frank's order) with an `ack:` line under each. Nothing
started; Frank reviews the first sample and the queue this session.

## O-2 (2026-08-25) — question: `pcrec-auto-in` (the `_in` entries with a caller-provided frame buffer)

I-1 says "your call whether that is a variant or a testee". Bench
position (requirements 4.2: pcrec's variations are separate roster
entries, each a (engine, version, configuration) triple): a SEPARATE
CONFIG `pcrec-auto-in` in testees/pcrec/configs.toml, like `nocaps`,
built in [B8] if Frank agrees. What the adapter needs from you to size
the buffer: the exact `<P>_*_FRAMES` / `_FRAME_SIZE` macro names as
emitted at 692c2e8 and the `_in` entry signatures (the shim reads them
from the emitted header; a stamped 0 means no buffers — we will not
divide by it). If a doc in pcrec already states them, the path suffices.

## Standing items owed to pcrec (recorded there by pcrecdev1 on [DD-13]/[OS-4]; listed so neither side forgets)

- The DFA-prefilter stamp (`RX_ENGINE` / prefilter on DFA artifacts) —
  inbox I-3, pcrec-owned, behind [CHK-1].
- The `(?:P)\z` whole-subject artifact's skip-loop last-byte cost — the
  match-compliance regime artifact ([OS-4]); the reporter buckets it as
  such in [B9].
- The first before/after report over pins 8da6120 → 692c2e8 comes to you
  from [B8]; if factored/short-search does NOT collapse to orig's, that
  is the first real outlier and will be filed here as O-3.
