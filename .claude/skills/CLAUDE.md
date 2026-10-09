# .claude/skills — project skills for Claude Code sessions

- `pcrec-bench-manager/SKILL.md` — the manager-session skill: wake order,
  the shared-box and read-only-pcrec rules (BD2/BD3), measurement
  discipline, delegation/watchdog/review conventions, and the session-end
  wake.md rewrite. Modelled on ~/pcrec/.claude/skills/pcrec-manager.
- `pcrec-bench-interpret/SKILL.md` — `/pcrec-bench-interpret <report>`
  ([B13.4]): runs `pcrecbench interpret --render` and commits the
  report's `reports/<name>.interpretation.md` sidecar; states the
  opinion firewall (the renderer phrases, a fired rule is changed only
  through the catalogue, never by hand-editing a sidecar).
- `pcrec-bench-upstream/SKILL.md` — `/pcrec-bench-upstream` ([B103]): the
  upstream-findings pipeline's session procedure (file, reproduce, triage,
  draft, approve/send, re-verify) over `docs/dev/upstream/` and
  `tools/upstream.py`; spec `docs/design/upstream_pipeline_v1.md`.
- `pcrec-bench-report-trend/SKILL.md` — `/pcrec-bench-report-trend [<pin>]`
  ([B130.2]): the window-close procedure of the pcrec trend report --
  snapshot the new pin(s) from the store (`make trend-snapshot`), propose
  `links.tsv` rows, `make trend` / `trend-check`, write the grounded
  `reports/trend/interpretation/<pin>.md`, `make check-trend`, commit with
  explicit paths. The first of the `pcrec-bench-report-<kind>` family.
