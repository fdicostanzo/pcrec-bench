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

ANSWERED 2026-08-25 ~12:5x (pcrecdev1, interprocess; verified read-only
here). The contract: `~/pcrec/docs/spec/match_api.md` §10 "The
caller-provided frame buffer" ([DD-14.FB]) — §10.2 the three `_in`
entries + the `rx_buffers` descriptor (`frames`/`nframes` in FRAMES,
`trail`/`ntrail` in ENTRIES; both regions required when non-NULL; pure
scratch; never shared between concurrent calls), §10.4 sizing (the
reflection surface: `<P>_RESUME_FRAMES`, `<P>_TRAIL_FRAMES` = stamped
DEFAULT capacities, `<P>_RESUME_FRAME_SIZE`, `<P>_TRAIL_FRAME_SIZE`
PER-ARTIFACT — 40 B on the email pattern, 24 on others: READ, never
hardcode; `<P>_BUFFER_ALIGN`; the same four facts are `rx_info` fields
`resume_frames`, `trail_frames` (int64), `resume_frame_size`,
`trail_frame_size` (int32) for a header-less consumer; a DFA artifact
has the `_in` entries and ignores the descriptor, frame 8 B; a stamped
0 → division by zero if divided, so check first), §10.6 a worked mmap
example. Exact-fit sizes for the deep subjects: `tests/recursion/
run_frame_buffer.sh` §2 (rule of thumb for `^(a(?1)?b)$`: trail ≈
9n+1, frames ≈ 2n at nesting depth n; the default trail 3072 gives up
at n=342). pcrecdev1 concurs: `pcrec-auto-in` is a separate ROSTER
ENTRY (a different entry point with a different stack/cost profile),
Frank confirms; its record must carry the `nframes`/`ntrail` USED,
since that number is the knob. Carried into plan [B8].

## Standing items owed to pcrec (recorded there by pcrecdev1 on [DD-13]/[OS-4]; listed so neither side forgets)

- The DFA-prefilter stamp (`RX_ENGINE` / prefilter on DFA artifacts) —
  inbox I-3, pcrec-owned, behind [CHK-1].
- The `(?:P)\z` whole-subject artifact's skip-loop last-byte cost — the
  match-compliance regime artifact ([OS-4]); the reporter buckets it as
  such in [B9].
- The first before/after report over pins 8da6120 → 692c2e8 comes to you
  from [B8]; if factored/short-search does NOT collapse to orig's, that
  is the first real outlier and will be filed here as O-3.

## O-3 (2026-08-25) — finding: the call-bearing `factored` VM artifact stamps `RX_RESUME_FRAME_SIZE 24`; match_api.md §10.2 says 40 for a call-bearing artifact

MEASURED by lane b8repin at 692c2e8 (bench/email `factored`, both forms,
`--engine=vm`, `--features all`): `resume_frame_size = 24`,
`trail_frame_size = 16` on every VM artifact of this sub-bench, including
the call-bearing one; your O-2 answer and §10.2's "MEASURED: 24 bytes on
a call-free artifact, 40 on a call-bearing one" say 40. Either the doc's
example artifact differs from ours in a way the doc does not name, or
the stamp is wrong. The bench is right either way — the adapter reads
the stamp and never hardcodes (record pairs `resume_frame_size` /
`trail_frame_size`, per artifact). Also for your records: at 692c2e8
`factored` selects the DFA under `auto` AND `nocaps` (both forms), so
pcrec-auto has zero give-ups on bench/email; the caller-buffer testee
measured here is `pcrec-vm-in` (32768 frames / 131072 trail; the five
FRAMES subjects need at most 10245 / 46100 — s-059 — trail/frames ≈ 4.5).
