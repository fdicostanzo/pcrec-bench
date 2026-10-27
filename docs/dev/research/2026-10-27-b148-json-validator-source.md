# [B148] source of the wild member `wild-json-validate` (Frank approved the download, 2026-10-27)

Fetched 2026-10-27T22:50Z by the manager through the Stack Exchange API (data only, nothing executed):
`https://api.stackexchange.com/2.3/questions/2583472/answers?site=stackoverflow&filter=withbody&sort=votes`
(response sha256 `4fe1263415b18ec15a4399a41b215feafddb28d0ef9347c75218438fb7910b51`; the
stackoverflow.com page itself refused the fetch tool).

- Question 2583472 "Regex to validate JSON"; ANSWER **3845829** by **mario**, score 212 at fetch,
  posted 2010-10-02, last edited 2023-11-24; **CC BY-SA 4.0**
  (https://stackoverflow.com/a/3845829). Attribution required (CC BY-SA 4.0).
- Fidelity: **adapted** — the answer gives the pattern as a PHP single-quoted string with `/sx`
  delimiters; the only change is undoing PHP quoting (`\\\\` -> `\\`) and moving the `s`/`x`
  flags out of the delimiters. Nothing else edited (incl. the author's `\Z`, which is NOT `\z`).
- The author states it passes the JSON.org test suite and Nicolas Seriot's JSON Parser suite
  (claim, not verified here).

## Verbatim code block (as posted)

```
$pcre_regex = '/
    (?(DEFINE)
        (?<ws>      [\t\n\r ]* )
        (?<number>  -? (?: 0|[1-9]\d*) (?: \.\d+)? (?: [Ee] [+-]? \d++)? )    
        (?<boolean> true | false | null )
        (?<string>  " (?: [^\\\\"\x00-\x1f] | \\\\ ["\\\\bfnrt\/] | \\\\ u [0-9A-Fa-f]{4} )* " )
        (?<pair>    (?&ws) (?&string) (?&ws) : (?&value) )
        (?<array>   \[ (?: (?&value) (?: , (?&value) )* )? (?&ws) \] )
        (?<object>  \{ (?: (?&pair) (?: , (?&pair) )* )? (?&ws) \} )
        (?<value>   (?&ws) (?: (?&number) | (?&boolean) | (?&string) | (?&array) | (?&object) ) (?&ws) )
    )
    \A (?&value) \Z
    /sx';

```

## The pattern as the bench uses it (flags `s` + `x`)

```

    (?(DEFINE)
        (?<ws>      [\t\n\r ]* )
        (?<number>  -? (?: 0|[1-9]\d*) (?: \.\d+)? (?: [Ee] [+-]? \d++)? )    
        (?<boolean> true | false | null )
        (?<string>  " (?: [^\\"\x00-\x1f] | \\ ["\\bfnrt\/] | \\ u [0-9A-Fa-f]{4} )* " )
        (?<pair>    (?&ws) (?&string) (?&ws) : (?&value) )
        (?<array>   \[ (?: (?&value) (?: , (?&value) )* )? (?&ws) \] )
        (?<object>  \{ (?: (?&pair) (?: , (?&pair) )* )? (?&ws) \} )
        (?<value>   (?&ws) (?: (?&number) | (?&boolean) | (?&string) | (?&array) | (?&object) ) (?&ws) )
    )
    \A (?&value) \Z
    
```
