"""pcrecbench -- the pcrec-bench harness/store/adapters/reporter package.

This [B5] lane provides `pcrecbench.report` (the query -> report reducer)
and nothing else; `harness.py`, `quiet.py`, `subbench.py`, `adapters.py`,
`store.py` (docs/design/harness_contract.md 1) belong to the parallel
[B3]/[B4] lanes and land at merge time.
"""
