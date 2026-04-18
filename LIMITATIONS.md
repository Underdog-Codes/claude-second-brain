# Known Limitations

This file is honest about what Claude Second Brain does not do. Read it before filing a bug.

## Memory is only as good as your notes

Claude retrieves what is in `Brain/`. If your notes are vague, incomplete, or out of date, Claude's answers will reflect that. This is not a limitation of the tool, it is a property of any retrieval-based system.

## No auto-sync

After adding or editing files in `Brain/`, you must run `mempalace mine .` manually. There is no background watcher or automatic re-indexing. If you forget, Claude will not see the new content.

## Search is semantic, not exact

mempalace uses vector similarity search. This means it finds conceptually related content, not exact keyword matches. For most use cases this is better. For finding a specific phrase or filename, use your editor's search instead.

## No access outside this folder

Claude cannot access your browser, file system, calendar, or anything outside the repo folder through this setup. If you need that, look at MCP servers.

## Session logs are append-only

`Brain/Daily/` grows over time. The setup does not automatically prune old logs. Clean it up manually if it gets large.

## Mac and Linux are less tested

The installer and hooks have been built and tested primarily on Windows 11. Mac and Linux should work but if you hit issues, open a GitHub issue.

## mempalace is a dependency

This template depends on mempalace for vector storage and retrieval. If mempalace changes its API or behavior, some things may break. The template pins no specific version. If you need stability, pin the version in your own setup.

## Not a replacement for good CLAUDE.md rules

The memory system works alongside your behavioral rules in CLAUDE.md, not instead of them. If Claude is behaving in ways you do not want, fix the rules in CLAUDE.md first.

## The hook guards are not security controls

`guard-autoload.py` prevents accidental writes to protected files. It is not a security boundary. A determined user or malformed tool call could still work around it.
