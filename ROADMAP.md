# Roadmap

This is a direction list, not a promise list. Items may change based on what is actually useful.

## Near term

- [ ] Demo GIF showing Claude answering from memory after a fresh session start
- [ ] Mac and Linux install testing and documented results
- [ ] Troubleshooting section in README for common install errors
- [ ] Screenshot: successful install output
- [ ] Screenshot: mempalace_status showing indexed entries

## Later

- [ ] Auto-mine option: watch Brain/ for changes and re-index automatically
- [ ] `mempalace mine .` progress bar or cleaner output for large vaults
- [ ] Starter Brain/ templates for common use cases (software dev, game dev, writing)
- [ ] Example mempalace.yaml configurations for different setups

## Not planned

- Cloud sync or remote storage
- GUI or web interface
- Plugin or extension system requiring ongoing maintenance
- Anything that sends Brain/ content to external APIs

## Completed

- [x] Cross-platform installer (Windows, Mac, Linux)
- [x] Palace storage moved to repo root (off C drive)
- [x] Pre-write hook blocking CLAUDE.md bloat
- [x] Session logging to Brain/Daily/
- [x] Dynamic vault root detection in hooks (works on any machine)
