# Changelog

All notable changes to Claude Second Brain are documented here.

## [1.0.0] - 2026-04-18

### Added
- Initial release
- `setup.py` cross-platform installer (Windows, Mac, Linux)
- `install.ps1` Windows one-command installer with Python auto-install via winget
- `Brain/` folder structure: Wiki, Projects, Areas, Daily
- `mempalace.yaml` room configuration for brain, skills, and general categories
- `.claude/settings.json` with two hooks wired:
  - `guard-autoload.py` blocks writes to CLAUDE.md files and root-level .md files
  - `session-stop.py` logs session activity to `Brain/Daily/` on exit
- `CLAUDE.md` behavioral rules: terse by default, Brain/ write-only, mempalace reads only, /compact at 50K tokens
- `Projects/example-project/` template with one-line CLAUDE.md and project.md starter
- Palace storage configured to repo root (`.mempalace/palace/`) instead of system home folder
- MIT license

### Notes
- Requires Claude Code: https://claude.ai/download
- Requires Python 3.10 or later
- mempalace must be re-run (`mempalace mine .`) after adding new Brain/ files
