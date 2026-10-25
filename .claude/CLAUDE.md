# .claude — Claude Code project configuration

- `skills/` — project skills (see skills/CLAUDE.md). Today: the
  `pcrec-bench-manager` session skill.
- `settings.json` — project hooks (Frank, 2026-10-25, inbox I-160): PreToolUse guards from `../scripts/hooks/` — `no_cd_worktree.sh` (no `cd` into worktrees/ or chained `cd X && ...`; use absolute paths / `git -C`), `no_commit_all.sh` (no `git commit -a`/`--all`), `lane_writes_in_worktree.sh` (a subagent's Write/Edit must land under worktrees/; escape file `worktrees/.mgr/main_write_ok` for a landing lane).
