# FAQ

**Do I need Obsidian?**

No. Obsidian is optional. Your `Brain/` folder is just markdown files. You can edit them in VS Code, Notepad, or any text editor. Obsidian works well if you already use it, but it is not required.

**What is mempalace?**

mempalace is a local Python library that indexes markdown files into a vector database (ChromaDB) and provides search tools for Claude. It runs entirely on your machine. Source: https://github.com/njraladdin/mempalace

**Does this send any data to the cloud?**

No. The vector index is stored locally in `.mempalace/palace/` inside your repo folder. mempalace does not make network requests. Claude Code itself communicates with Anthropic's API as it normally does, but your Brain/ notes are never sent there directly.

**Does this require an API key?**

No additional API keys beyond what Claude Code already uses. The memory system is fully local.

**What happens if I edit Brain/ without running `mempalace mine .`?**

Claude will not see the new content. The index only updates when you run `mempalace mine .`. Your file is saved, but the searchable embeddings are not updated until you re-index.

**Can I use this with multiple projects?**

Yes. Add each project under `Projects/<name>/` with its own `CLAUDE.md` (one line) and `project.md`. Add project context notes to `Brain/Projects/<name>/`. Run `mempalace mine .` after.

**Will this work on Mac or Linux?**

`setup.py` is cross-platform. The hooks in `.claude/Brain/hooks/` are written in Python so they should work on any platform. Mac and Linux are less tested than Windows. Open an issue if you hit problems.

**How much disk space does the index take?**

Roughly 5-10MB per 1,000 notes depending on content length. A typical setup with a few hundred notes uses under 50MB.

**Can I delete `.mempalace/palace/` and start over?**

Yes. Delete the folder and run `mempalace mine .` to rebuild from scratch. You will not lose any source files in `Brain/`.

**Why is CLAUDE.md in each project folder just one line?**

Claude Code auto-loads every CLAUDE.md it finds in the project hierarchy at session start. Keeping them to one line prevents token burn. All project context goes into `Brain/Projects/<name>/` and is retrieved on demand through mempalace.

**Can I add my own rooms to mempalace.yaml?**

Yes. Open `mempalace.yaml` and add a new entry under `rooms:` with a name, description, and keywords. Run `mempalace mine .` after. Claude will use the new category when searching.

**What is the `guard-autoload.py` hook doing?**

It intercepts writes before they happen and blocks two things: writing more than one line to any CLAUDE.md file in the project, and creating new .md files at the repo root level. Both of those actions can cause unintended context to auto-load at session start. The guard prevents accidental token bloat.

**Do I need to run `mempalace mine .` every session?**

No, only when you add or change files in `Brain/`. The index persists between sessions. If you have not changed anything, the existing index is still valid.
