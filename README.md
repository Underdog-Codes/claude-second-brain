# Claude Second Brain

> Persistent local memory for Claude Code. Stop re-explaining your projects every session.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Works with Claude Code](https://img.shields.io/badge/works%20with-Claude%20Code-orange)](https://claude.ai/download)
[![Powered by mempalace](https://img.shields.io/badge/memory-mempalace-blue)](https://github.com/njraladdin/mempalace)

---

Claude Code starts every session with no memory of the last one. You re-explain your stack, your projects, your preferences. If you load context files to fix this, you pay the token cost on every session start whether that context is needed or not.

Claude Second Brain is a folder template that gives Claude a searchable local knowledge base. Your notes and project context are indexed into a local vector database. Claude retrieves only what is relevant to each conversation instead of loading everything upfront.

Everything stays on your machine. No cloud. No third-party memory API. No API keys beyond what Claude Code already uses.

---

## What you get

- Claude retains your projects, preferences, and past decisions across sessions
- Memory scales without growing your session startup cost
- Notes live in plain markdown. Edit them in Obsidian, VS Code, or any text editor.
- A pre-write hook prevents accidental context bloat in CLAUDE.md files
- Session activity is logged automatically to `Brain/Daily/`
- One setup command. Works on Windows, Mac, and Linux.

---

## Who this is for

- Developers using Claude Code daily who are tired of repeating project context
- People who want a local knowledge base Claude can search and use
- Obsidian users who want their notes to inform Claude without manual copy-paste
- Anyone who wants Claude to know their stack, decisions, and ongoing work without re-explaining every session

---

## What this is not

- Not a cloud memory service. Everything is stored locally.
- Not a replacement for CLAUDE.md. It works alongside it.
- Not automatic. Claude uses your memory if you keep your notes up to date.
- Not a plugin or extension. It is a folder template you clone and own.

---

## See it in action

After setup, open Claude Code and ask:

> "What am I currently working on?"

Claude queries your `Brain/` notes and responds based on your actual project context. No context file loaded upfront. No re-explaining.

<!-- Add demo.gif here once recorded -->
<!-- ![Demo showing Claude answering from memory](docs/demo.gif) -->

---

## Quickstart

**Windows 11**

Right-click `install.ps1` and select "Run with PowerShell"

**Mac / Linux**

```bash
git clone https://github.com/Underdog-Codes/claude-second-brain.git
cd claude-second-brain
python3 setup.py
```

Then open the folder in Claude Code and start a session.

---

## What the installer does

Running `install.ps1` (Windows) or `python3 setup.py` (Mac/Linux) does the following:

**1. Checks for Python** (Windows only)
Checks if Python is installed. If not, installs Python 3.12 via winget. Skips this step if Python is already present.

**2. Installs mempalace**
Runs `pip install mempalace`. This is the local vector search library that stores and retrieves your notes. It runs entirely on your machine. Nothing is sent to any server.

**3. Configures storage location**
Writes a small config file to `~/.mempalace/config.json` that points storage to `.mempalace/palace/` inside this repo folder. Your memory lives with your notes, not buried in a system folder.

**4. Indexes your notes**
Runs `mempalace mine .` which reads every markdown file in `Brain/` and converts them into searchable embeddings stored locally. This is what lets Claude search your notes by meaning instead of loading all of them at once.

The installer does not send any data outside your machine. It does not require API keys beyond what Claude Code already uses. It does not modify any global system settings outside `.claude/settings.json` in this repo.

---

## Start here

1. Install Claude Code if you have not already: [claude.ai/download](https://claude.ai/download)
2. Fork this repo on GitHub, or download the ZIP
3. Run the installer (see Quickstart above)
4. Open the repo folder in Claude Code
5. Edit `Brain/identity.md` and add your name, role, and stack
6. Open `CLAUDE.md` and fill in the `## Stack` section
7. Start a new Claude Code session and type: `"What do you know about me?"`

If Claude answers with your details from `identity.md`, setup is complete.

After adding new notes to `Brain/`, always run:

```bash
mempalace mine .
```

This updates the local index so Claude can find the new content.

---

## Use cases

**Software development across sessions**

You work across multiple projects and spend the first few minutes of every session re-explaining the project, the stack, and what you were last working on.

Your project context, architecture decisions, and current status live in `Brain/Projects/<name>/`. Claude retrieves them when relevant.

> "What were we working on in the auth module last time, and what approach did we agree on?"

---

**Game development with repeating patterns**

You are building a game across many sessions. Every time, you re-explain the design, mechanics, and code conventions before Claude can help.

Game design docs, mechanic notes, and code conventions live in `Brain/`. Claude applies them without being reminded.

> "Write a new ability that follows the same damage pattern as the ones in my notes."

---

**Recurring work with consistent standards**

You do the same types of work repeatedly and Claude never knows your preferences, templates, or standards.

Your preferences, past decisions, and templates live in `Brain/Wiki/`. Claude applies them without being told each time.

> "Review this PR using my usual standards."

---

**Obsidian as a knowledge base Claude can search**

You have an Obsidian vault full of notes and reference material. Claude cannot read your vault directly and copy-pasting is slow.

Point Obsidian at the `Brain/` folder. Write notes normally. Run `mempalace mine .` to index. Claude searches them semantically in any session.

> "What do my notes say about the architecture decision we made for the API layer?"

---

## How it works

```
You write notes         Brain/Wiki/, Brain/Projects/
                                  |
mempalace indexes them  Local vector embeddings
                                  |
Claude queries          mempalace_search returns relevant chunks
                                  |
Claude responds         Grounded in your actual notes
```

The key constraint: `Brain/` is write-only for Claude. Claude never reads those files directly. It only queries through mempalace. This means startup cost stays low regardless of how many notes you have, because Claude only loads what is relevant to the current question.

---

## Project structure

```
claude-second-brain/
├── CLAUDE.md                       Claude's behavioral rules (rules only, 20 lines max)
├── PROJECTS.md                     Master project index
├── mempalace.yaml                  Memory category configuration
├── install.ps1                     Windows installer
├── setup.py                        Cross-platform installer
├── Brain/
│   ├── identity.md                 Your name, role, and stack (fill this in first)
│   ├── Wiki/                       Reference knowledge: concepts, tools, topics
│   ├── Projects/                   Project context, decisions, architecture notes
│   ├── Areas/                      Ongoing responsibilities
│   └── Daily/                      Auto-generated session logs (gitignored)
├── Projects/
│   └── example-project/
│       ├── CLAUDE.md               One-line routing file (do not edit)
│       └── project.md              Project rules and file list (20 lines max)
└── .claude/
    ├── settings.json               Hooks: guard + session logger
    └── Brain/hooks/
        ├── guard-autoload.py       Blocks writes to protected files
        └── session-stop.py         Logs session end to Brain/Daily/
```

---

## Updating your memory

Any time you add or edit files in `Brain/`, run:

```bash
mempalace mine .
```

Run this from the repo root folder. It re-indexes all markdown files and updates the local embeddings. Claude will have access to the new content in the next session.

You can also re-run `setup.py` or `install.ps1` at any time. They are safe to run repeatedly.

---

## Works with Obsidian

Open this folder as an Obsidian vault. No extra configuration needed. Write notes visually in `Brain/`. After adding anything, run `mempalace mine .` to update the index.

Claude writes to `Brain/` automatically when you ask it to save something. You browse and edit in Obsidian. Neither tool steps on the other.

```
Obsidian (you write) → Brain/ files → mempalace mine → Claude queries
```

---

## Known limitations

- Claude only knows what is in `Brain/`. If your notes are out of date, Claude's answers will be too.
- `mempalace mine .` must be run manually after adding new files. There is no auto-sync.
- Search quality depends on how well your notes are written. Vague notes return vague results.
- The local vector index takes a few seconds to build on first run and after large updates.
- Tested on Windows 11. Mac and Linux should work but have had less testing. Open an issue if you hit problems.
- This does not give Claude access to your browser, file system, or anything outside this folder.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to report bugs, suggest improvements, and submit pull requests.

---

## License

MIT. Use it, fork it, build on it. See [LICENSE](LICENSE).
