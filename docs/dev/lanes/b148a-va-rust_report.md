# b148a-va-rust: L6 vars assists, rust-regex

All four ASSISTED, 20/20 public cases each. Rows appended to assists.tsv.

| member | tokens | lines | verdict | selftest |
|---|---|---|---|---|
| va-tenant | 187 | 10 | ASSISTED | 20/20 |
| va-route | 243 | 10 | ASSISTED | 20/20 |
| va-term | 200 | 10 | ASSISTED | 20/20 |
| va-term-bang | 200 | 10 | ASSISTED | 20/20 (identical file to va-term) |

Design (all four): helper `lit` hex-escapes every value byte (`\xNN`); the
pattern text is `format!`ed from the template with a `(?-u)` byte-mode prefix;
a `run` helper fetches or compiles via `cache.entry(pattern bytes)` and finds.
UNSET (or EMPTY for term / prefix default) is decided with `Option` before any
compile; refusal returns UB_R. Key = resolved pattern text.

Unclear: nothing. No includes added; the helpers (`lit`, `run`) are counted.
