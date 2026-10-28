# testees/common/ — code shared by more than one driver

Not an adapter: no `adapter.py`, no `configs.toml`, never discovered as a
testee directory (`pcrecbench.adapters.discover` imports `testees/*/adapter.py`
only). Headers here are `#include`d by a driver as `"../common/<file>"` and are
part of that driver's staleness check (`pcrecbench/driverrun.py` rebuilds a
driver when any `testees/common/*.h` is newer than its binary).

| file | role |
|---|---|
| `calls_io.h` | ([B148] L4, docs/design/unusual_set_v1.md 7.1-7.3) the `--mode calls` I/O of the C/C++ drivers (pcre2, pcrec, onig, re2, vectorscan; rust has its own copy in `src/main.rs`): the 3-column `--list` (`id`, subject path, call-list path), the call list (`call_id offset length segment_bytes binding_id`; a binding other than `-` is a VARS stream, lane L7's, refused BY NAME), the preallocated `struct call_res` array the timed loop writes, and `calls_report`, which AFTER the clock turns the array into the token file (`n`, `m:s,e[;g1s,g1e]`, `r`, `g`, one per line, `<tokens-dir>/<id>.tok`) and the `stream` line. Header-only `static` functions (`CALLS_FN`: unused-silent, noinline so none lands in a caller's `sigsetjmp` frame). EVERYTHING here is outside the clock; the timed replay lives in each driver's own `timed_calls.*` (BD16). The harness hashes the token file (sha256 of the tokens, each + `\n`), so no driver links SHA-256 |
| `vars_io.h` | ([B148] L7, unusual_set_v1.md 3.3 / 7.3) the CALLER-VARIABLES half of `--mode calls`, on top of `calls_io.h`: a vars stream's `--list` has a FOURTH column (the bindings table, `binding_id name value`, value = hex / `UNSET` / `EMPTY`), every call is one LINE of the subject with its binding (`binding_id` resolved to an index here, outside the clock, with each binding's variable array built once; a `-` binding is an error). `struct vvar` has pcrec's `rx_var` layout (name, p, len; `p == NULL` is UNSET, `p != NULL && len == 0` EMPTY); the assisted drivers of L6 can reuse the loader. Used today by the pcrec driver (`timed_calls_vars.c` is its timed replay) |
