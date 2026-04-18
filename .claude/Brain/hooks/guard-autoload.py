#!/usr/bin/env python3
"""
PreToolUse guard — blocks writes to auto-loading or protected files.
Enforces CLAUDE.md rules 3, 4, 5.
"""
import json, sys, re, os

data = json.load(sys.stdin)
tool_input = data.get("tool_input", {})
path = tool_input.get("file_path", "").replace("\\", "/")
path_lower = path.lower()
content = tool_input.get("content", "") or tool_input.get("new_string", "")

# Detect vault root dynamically (where CLAUDE.md lives)
VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).replace("\\", "/").lower()
ONE_LINER = "> DO NOT EDIT. Query mempalace for all project context. Never read files directly."

# Only enforce inside the vault
if not path_lower.startswith(VAULT_ROOT):
    sys.exit(0)

# Rule 5: CLAUDE.md files — allow only the standard 1-liner, block everything else
if re.search(r'/claude\.md$', path_lower) or path_lower.endswith("claude.md"):
    if ONE_LINER in content and len(content.strip().splitlines()) <= 2:
        sys.exit(0)
    print(json.dumps({
        "decision": "block",
        "reason": (
            "BLOCKED — CLAUDE.md files must stay as the 1-line mempalace redirect (Rule 5).\n"
            "Put project context in project.md or Brain/Projects/<Name>/.\n"
            "Put global behavioral rules in root CLAUDE.md only.\n"
            "Run `mempalace mine` after."
        )
    }))
    sys.exit(0)

# Rule 3: No new root-level .md files
rel = path_lower.replace(VAULT_ROOT, "").lstrip("/")
is_root_md = rel.endswith(".md") and "/" not in rel
allowed_root = {"projects.md", "claude.md"}

if is_root_md and rel not in allowed_root:
    print(json.dumps({
        "decision": "block",
        "reason": (
            f"BLOCKED — '{rel}' is a root-level .md file (Rule 3).\n"
            "Root .md files get auto-loaded or globally mined.\n"
            "  Reference knowledge → Brain/Wiki/<topic>.md\n"
            "  Project context     → Brain/Projects/<Name>/\n"
            "  Daily notes         → Brain/Daily/<date>.md\n"
            "Run `mempalace mine` after writing."
        )
    }))
    sys.exit(0)

sys.exit(0)
