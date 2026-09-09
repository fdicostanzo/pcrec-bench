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
