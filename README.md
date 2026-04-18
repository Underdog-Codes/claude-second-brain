# 🧠 Claude Brain Template

> Give Claude permanent memory, zero token bloat, and a local second brain - in one setup.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![mempalace](https://img.shields.io/badge/powered%20by-mempalace-blue)](https://github.com/milla-jovovich/mempalace)
[![Claude Code](https://img.shields.io/badge/works%20with-Claude%20Code-orange)](https://claude.ai/download)

---

## The Problem

Every Claude session starts blank. You re-explain your stack, your preferences, your projects - every time. And the more context you load upfront, the more tokens you burn before you type a single word.

Most setups "fix" this by loading big CLAUDE.md files and markdown notes at session start. That's just trading one problem for another.

## The Solution

This template wires Claude to a **local vector memory system** ([mempalace](https://github.com/milla-jovovich/mempalace)). Instead of loading everything upfront, Claude queries only what's relevant - on demand.

```
Session startup:  ~170 tokens (fixed, forever)
Per memory query: ~300-500 tokens (3-5 relevant chunks)
Total per session: ~1-2K tokens regardless of how much you've stored
```

You write notes in plain markdown. Claude reads them semantically. Your token cost stays flat whether you have 100 notes or 100,000.

---

## Features

- **Permanent memory** - Claude remembers decisions, preferences, and context across all sessions
- **Flat token cost** - 170 tokens on startup no matter how big your knowledge base grows
- **100% local** - everything stays on your machine, no cloud, no API keys for memory
- **Auto-protection** - a hook blocks accidental writes to auto-loading files
- **Session logging** - every session end is logged to `Brain/Daily/` automatically
- **Clean structure** - opinionated folder layout that scales without becoming a mess
- **One-command setup** - Python + mempalace + vault indexing in a single step

---

## How it works

```
You write notes       →   Brain/Wiki/, Brain/Projects/
                                  ↓
mempalace mines them  →   Local vector embeddings (~10K+ drawers)
                                  ↓
Claude queries        →   mempalace_search returns top 5 relevant chunks
                                  ↓
Claude responds       →   Grounded in your actual knowledge
```

Your Obsidian vault (optional) writes to `Brain/`. Claude never reads it directly - only through mempalace. The bigger your brain gets, the smarter Claude gets. Token cost never changes.

---

## Prerequisites

**[Claude Code](https://claude.ai/download)** - install this manually. That's the only prerequisite you handle yourself.

---

## Setup

**Windows 11** - right-click `install.ps1` → Run with PowerShell

**Mac / Linux:**
```bash
python3 setup.py
```

Both install mempalace and index your vault automatically.

---

## After setup

1. Open this folder in Claude Code
2. Fill in `Brain/identity.md` with your name, role, and stack
3. Add your stack to `CLAUDE.md` under `## Stack`
4. Start a new session - Claude will call `mempalace_status` automatically

---

## Structure

```
├── CLAUDE.md                    ← Claude's behavioral rules (rules only, no context)
├── PROJECTS.md                  ← Master project index
├── mempalace.yaml               ← Memory room configuration
├── Brain/
│   ├── identity.md              ← Who you are + your stack
│   ├── Wiki/                    ← Reference knowledge (concepts, tools, topics)
│   ├── Projects/                ← Project context, decisions, architecture
│   ├── Areas/                   ← Ongoing responsibilities
│   └── Daily/                   ← Auto-generated session logs
├── Projects/
│   └── example-project/
│       ├── CLAUDE.md            ← 1-line redirect (immutable)
│       └── project.md           ← Project rules + file list (20 lines max)
├── Skills/                      ← Claude skills
└── .claude/
    ├── settings.json            ← Hooks: guard + session logger
    └── Brain/hooks/
        ├── guard-autoload.py    ← Blocks writes to protected files
        └── session-stop.py      ← Logs session end to Brain/Daily/
```

---

## The rules that make it work

Every project CLAUDE.md is a single immutable line:
```
> DO NOT EDIT. Query mempalace for all project context. Never read files directly.
```

A pre-write hook enforces this - if anything tries to write more than 1 line to a CLAUDE.md, it's blocked with an explanation. Same for any new root-level `.md` files.

`project.md` files have a 20-line cap. Overflow goes to `Brain/Projects/<Name>/` and gets mined into mempalace. Context stays lean. Memory stays rich.

---

## Adding a new project

```
Projects/
└── my-new-project/
    ├── CLAUDE.md     ← copy from example-project (1 line only)
    └── project.md    ← add project list + hard rules (20 lines max)
```

Then run:
```bash
mempalace mine .
```

---

## Updating memory

Any time you add or edit files in `Brain/`:
```bash
mempalace mine .
```

Or re-run `setup.py` / `install.ps1` - same thing.

---

## Works great with Obsidian

Open this folder as an Obsidian vault. Write notes visually. Claude reads them through mempalace - never directly. The architecture is:

```
Obsidian (you write) → Brain/ files → mempalace mine → Claude queries
```

Claude has write access to Brain/ so it can file new knowledge automatically. You browse it in Obsidian. Neither tool steps on the other.

---

## Credits

Architecture inspired by:
- [Andrej Karpathy's LLM coding principles](https://github.com/forrestchang/andrej-karpathy-skills) - simplicity first, surgical changes
- [mempalace](https://github.com/milla-jovovich/mempalace) - local vector memory for AI agents
- [Anthropic Claude Code best practices](https://code.claude.com/docs/en/best-practices)

---

## License

MIT - use it, fork it, build on it.
