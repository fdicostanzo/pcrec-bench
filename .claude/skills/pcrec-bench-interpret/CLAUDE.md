# .claude/skills/pcrec-bench-interpret

- `SKILL.md` — the skill (frontmatter `name: pcrec-bench-interpret`);
  invoke as `/pcrec-bench-interpret <report>` from a session started in
  ~/pcrec-bench. Runs `pcrecbench interpret --render` and commits the
  `reports/<name>.interpretation.md` sidecar it produces. Phrases
  nothing itself — the catalogue's templates do the phrasing
  (interpreter_v1.md §7.4, §9.1) — and states the opinion firewall in
  full so a future agent does not "improve" a sidecar by hand.
