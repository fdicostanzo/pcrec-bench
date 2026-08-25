# tools/ — repo tooling that is not the harness

| file | role |
|---|---|
| `selfcheck.py` | `make check-harness`: the [B3] half of the self-check suite |

`selfcheck.py`'s organising principle is pcrec's check-design lesson: every
gate is exercised against an input it must REJECT in the same run that
exercises it against one it must accept. A check with no failing case proves
nothing, and a control that passes because the judge dislikes everything
proves nothing either — which is why the wrong-answer control runs each
falsified expectation AND its committed counterpart.
