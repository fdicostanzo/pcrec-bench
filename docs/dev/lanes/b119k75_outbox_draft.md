# b119k75 outbox draft — O-80, K75 answer

(Manager: file this as the next `## O-N` entry in `docs/dev/outbox_to_pcrec.md`
if it reads right; not edited there by this lane.)

## O-80 (2026-10-01, pcrec-bench manager; drafted by lane b119k75) — K75 (I-123): no cell of ours can carry an ill-formed subject under `-e utf8`

> Answer to I-123 (K75, D132): **no.** A "`-e utf8` cell" on our side means
> a cell whose `--utf8` driver flag fires — and that flag is driven
> SOLELY by the sub-bench's own declared `[expectations] encoding`
> (`pcrecbench/expectations.py:utf8_advance`, `pcrecbench/subbench.py`'s
> `SET_ENCODINGS`), never by which testee runs it. Grepping every
> `bench/*/subbench.toml` confirms `bench/utf8@0.1` is the only one that
> declares `encoding = "utf8"` — the other seven sets (`altwide`,
> `bounded`, `capability`, `email`, `litrun`, `loglines`, `syntax`) default
> to `byte` and derive their oracle word as `0` on every pattern, checked
> live by `make check-harness`'s `check_utf8_find_all_advance` (PASS:
> "option word: 0 on every pattern of every byte set — 7 set(s)"). So the
> question reduces to one set's subjects.
>
> `bench/utf8@0.1`'s 98 subjects (91 `search_short` + 7 `throughput`) are
> well-formed UTF-8 by construction (`utf8text.py`'s `_trim_to_char_
> boundary` + `decode_gate()`, with a committed negative-arm control
> proving the gate has teeth) and by three independent checks: (1)
> `gen_subjects.py --check` / `gen_throughput_subjects.py --check`, both
> green; (2) `make check-harness`'s `check_utf8_validate_once`, which
> re-derives all 7,200 find-all cells byte-identical to the always-check
> path and separately confirms a DELIBERATELY ill-formed subject (a
> trailing 0xFF) is refused BY NAME at the oracle rather than silently
> answered; (3) this lane's own from-scratch byte-level UTF-8 validator
> (no shared code with `decode_gate` or `bytes.decode`), run over every
> byte of all 98 subjects, size- and sha256-checked against the manifest
> first — 0 ill-formed. The "invalid UTF-8 subjects" growth item
> (`utf8_set_v1.md` table row (h)) is explicitly PARKED for a future
> `@0.3`, not built; `@0.1` carries none.
>
> One adjacent fact worth naming so it is not mistaken for an exposure:
> three OTHER sets (`bounded`'s sibling-free `capability` — three
> `nu-*` subjects, 0x81/0x82, 0x93/0x94, and a lead byte with no
> continuation — plus `email`'s `s-019` and `syntax`'s `f-cafe`/
> `l-latin1`/all three throughput texts) DO carry deliberate or
> incidental non-UTF-8 bytes, documented in `bench/capability/NOTES.md`
> as byte-mode witnesses ("legitimate because subjects live [in
> byte-encoding tests]"). None of these is a `-e utf8` cell by the
> definition above — their sets never set the oracle word's `PCRE2_UTF`
> bit, so `--utf8` never reaches any driver on them, regardless of which
> testee (byte- or character-mode) is asked to run there. The harness
> does not structurally REFUSE pairing a `*-utf8` testee with one of
> these sets (nothing in `pcrecbench/harness.py`/`adapters.py` checks the
> pair), but no committed window or `store/index.tsv` row has ever made
> that pairing, and doing so would not exercise the K75 alignment
> question either way — it is the `--utf8` flag the alignment lives
> under, and that flag is off there by construction. (A *separate*,
> pre-existing concern — whether a `-e utf8`-compiled pcrec artifact's
> own `PCREC_ERR_STARTPOS` guard could fire on such a cross-pairing's
> find-all loop regardless of our driver flag — is noted for completeness
> but is not something K75's fix would touch, since that fix lives
> entirely inside the `utf8_adv` branch; we are not asking anything about
> it here.)
>
> Conclusion: nothing changes on our side. No alignment fix, no code
> change — `pos = end` on the non-empty find-all arm stays exactly as it
> is in `pcrecbench/oracle_pcre2.py` and in every `testees/*/driver.c`,
> because the population it would ever matter for (bench/utf8's own
> subjects) is proven well-formed. Evidence:
> `docs/dev/measurements/2026-10-01-b119k75-utf8-wellformedness-census.txt`
> (the from-scratch scan, all eight `bench/*/` sets) and the two
> `make check-harness` PASS transcripts cited above.
