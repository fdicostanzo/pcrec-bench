# schema/examples/ — records that MUST validate

Every record here is SYNTHETIC. No engine was run, no box was quiet, and
every number is invented. Each file says so in three machine-readable
ways: `synthetic: true` in the setup layer (the reporter excludes such
records from every query), `machine_id: "example-box"`, and a `note`
field that states it in words. Nothing here is a measurement and nothing
here may be cited as one.

They exist to (a) show what a record looks like, and (b) be the
ACCEPT half of `make check-schema` — a validator that only ever rejects
is as useless as one that only ever accepts.

## Files

File names are not chosen: rule X4 makes the name the record id plus
`.jsonl`, so the two files below are named by the cells they describe.

- `email-specimen@0.1__pcrec_0.9.0-g1a2b3c4_vm-caps-simdna__example-box__20260825T031800Z.jsonl`
  — the worked example. A `compiled-aot` pcrec testee over three
  patterns and four subjects, exercising: both row kinds; all three
  subject regimes; `engine_metadata` populated from pcrec's STRUCTURED
  fields (`rx_info.engine/abi/ncaps/...`, `<PREFIX>_VM_PREFILTER`,
  and the `VM_RUNGS`/`VM_STRATS`/`VM_PRUNES` masks as arrays of bit
  names); AOT compile rows with all three phases timed separately; an
  `unsupported-by-declaration` cell (the backreference pattern, with the
  `declaration_ref` that outcome requires); a `truncated-subject` row on
  the 1 MB subject; and a `wrong-span-or-captures` row carrying
  `observed` and NO timing.
- `email-specimen@0.1__v8-regexp_13.4.0_default-caps-simdna__example-box__20260825T034500Z.jsonl`
  — the second, small record: a `lazy-jit` testee (compile rows carry
  `derivation`, never a number the harness invented) whose record status
  is `inconclusive-load` — the box got busy partway through, so the
  numbers exist and the record says do not trust them. Its
  `engine_metadata_declaration` is deliberately EMPTY: the `tier` pair
  this example used to declare had no adapter mechanism behind it
  anywhere in `docs/design/harness_contract.md` §3, and a declaration
  the contract cannot produce is an invented capability dressed as an
  example. The consequence is that no ACCEPTED example exercises
  `scope: match`; `bad/x15-metadata-wrong-scope.jsonl` covers that
  branch instead.

## Editing one

Records are hashed (`content_hash`, note §3). After editing, restamp:

    python3 schema/validate.py --print-hash <file>

and put that value in `content_hash.value`, or `make check-schema` will
fail with rule X6 — which is exactly what it is for.

Maintenance: update this file when files are added/removed or change role.
