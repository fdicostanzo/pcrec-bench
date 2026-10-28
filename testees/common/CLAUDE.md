# testees/common/ — code shared by more than one driver

Not an adapter: no `adapter.py`, no `configs.toml`, never discovered as a
testee directory (`pcrecbench.adapters.discover` imports `testees/*/adapter.py`
only). Headers here are `#include`d by a driver as `"../common/<file>"` and are
part of that driver's staleness check (`pcrecbench/driverrun.py` rebuilds a
driver when any `testees/common/*.h` is newer than its binary).

| file | role |
|---|---|
| `calls_io.h` | ([B148] L4, docs/design/unusual_set_v1.md 7.1-7.3) the `--mode calls` I/O of the C/C++ drivers (pcre2, pcrec, onig, re2, vectorscan; rust has its own copy in `src/main.rs`): the 3-column `--list` (`id`, subject path, call-list path), the call list (`call_id offset length segment_bytes binding_id`; a binding other than `-` is a VARS stream, lane L7's, refused BY NAME), the preallocated `struct call_res` array the timed loop writes, and `calls_report`, which AFTER the clock turns the array into the token file (`n`, `m:s,e[;g1s,g1e]`, `r`, `g`, one per line, `<tokens-dir>/<id>.tok`) and the `stream` line. Header-only `static` functions (`CALLS_FN`: unused-silent, noinline so none lands in a caller's `sigsetjmp` frame). EVERYTHING here is outside the clock; the timed replay lives in each driver's own `timed_calls.*` (BD16). The harness hashes the token file (sha256 of the tokens, each + `\n`), so no driver links SHA-256 |
| `ub_bind.h` / `ub_bind.c` | ([B148] L5, unusual_set_v1.md 3.2) THE CALLOUT BINDING TABLE every native-callout driver shares: a spec `1=luhn,3=member:/abs/users.tsv,netstr=netstr` parsed ONCE before any timed call (`ub_bind_parse`) into `ub_slots[256]` (numbered sites) and `ub_named[8]` (named); each wrapper calls `slot->fn(&view)` -- the same indirect call on every engine. Compiled into each callout driver and into pcrec's callout `.so`; the callees themselves are `bench/unusual/callees/` |
