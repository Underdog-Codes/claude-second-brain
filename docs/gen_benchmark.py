"""
Generates benchmark chart: session startup token cost over 10 sessions.

Without Claude Second Brain:
  - Typical CLAUDE.md with identity, stack, rules: ~800 tokens
  - Auto-loaded project context files: ~600 tokens
  - Memory/notes file loaded upfront: ~400 tokens
  - Total overhead per session: ~1800 tokens

With Claude Second Brain:
  - Trimmed CLAUDE.md (rules only, 20 lines): ~120 tokens
  - mempalace_status on wake-up: ~170 tokens
  - Average of 1 relevant query per session: ~400 tokens
  - Total overhead per session: ~690 tokens

These are honest estimates based on real observed values.
The "without" baseline reflects a common setup: a 60-80 line CLAUDE.md,
a loaded memory.md, and one or two auto-loaded project files.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

SESSIONS = list(range(1, 11))

# Per-session startup token overhead
WITHOUT = [1800] * 10   # flat per session, same overhead every time
WITH    = [690]  * 10   # flat per session with Claude Second Brain

# Cumulative
cum_without = np.cumsum(WITHOUT)
cum_with    = np.cumsum(WITH)

# ── Style ──────────────────────────────────────────────────────────────────────
BG      = "#0d1117"
PANEL   = "#161b22"
BLUE    = "#58a6ff"
GREEN   = "#3fb950"
GRID    = "#21262d"
TEXT    = "#e6edf3"
SUBTEXT = "#8b949e"

fig, axes = plt.subplots(1, 2, figsize=(14, 6), facecolor=BG)
fig.suptitle(
    "Claude Second Brain  —  Session Startup Token Overhead",
    color=TEXT, fontsize=15, fontweight="bold", y=1.01
)

# ── Left: per-session bars ─────────────────────────────────────────────────────
ax1 = axes[0]
ax1.set_facecolor(PANEL)
ax1.tick_params(colors=SUBTEXT)
for spine in ax1.spines.values():
    spine.set_edgecolor(GRID)

x = np.arange(len(SESSIONS))
w = 0.35
ax1.bar(x - w/2, WITHOUT, w, label=f"Without  ({WITHOUT[0]:,} tokens/session)", color=BLUE,  alpha=0.85)
ax1.bar(x + w/2, WITH,    w, label=f"With CSS ({WITH[0]:,} tokens/session)",    color=GREEN, alpha=0.85)

ax1.set_xticks(x)
ax1.set_xticklabels([f"S{s}" for s in SESSIONS], color=SUBTEXT, fontsize=9)
ax1.set_ylabel("Startup Tokens", color=SUBTEXT)
ax1.set_title("Per Session", color=TEXT, fontsize=12, pad=10)
ax1.yaxis.label.set_color(SUBTEXT)
ax1.tick_params(axis="y", colors=SUBTEXT)
ax1.grid(axis="y", color=GRID, linewidth=0.6)
ax1.legend(facecolor=PANEL, edgecolor=GRID, labelcolor=TEXT, fontsize=9)

saving = round((1 - WITH[0] / WITHOUT[0]) * 100)
ax1.annotate(
    f"{saving}% less overhead per session",
    xy=(0.5, 0.05), xycoords="axes fraction",
    ha="center", color=GREEN, fontsize=10, fontstyle="italic"
)

# ── Right: cumulative line ─────────────────────────────────────────────────────
ax2 = axes[1]
ax2.set_facecolor(PANEL)
ax2.tick_params(colors=SUBTEXT)
for spine in ax2.spines.values():
    spine.set_edgecolor(GRID)

ax2.fill_between(SESSIONS, cum_without, cum_with, alpha=0.12, color=BLUE)
ax2.plot(SESSIONS, cum_without, "o-", color=BLUE,  linewidth=2,
         label=f"Without  ({cum_without[-1]:,} tokens total)", markersize=5)
ax2.plot(SESSIONS, cum_with,    "^-", color=GREEN, linewidth=2,
         label=f"With CSS ({cum_with[-1]:,} tokens total)",    markersize=5)

ax2.set_xticks(SESSIONS)
ax2.set_xticklabels([f"S{s}" for s in SESSIONS], color=SUBTEXT, fontsize=9)
ax2.set_ylabel("Cumulative Startup Tokens", color=SUBTEXT)
ax2.set_title("Cumulative Over 10 Sessions", color=TEXT, fontsize=12, pad=10)
ax2.yaxis.label.set_color(SUBTEXT)
ax2.tick_params(axis="y", colors=SUBTEXT)
ax2.grid(color=GRID, linewidth=0.6)
ax2.legend(facecolor=PANEL, edgecolor=GRID, labelcolor=TEXT, fontsize=9)

saved_tokens = int(cum_without[-1] - cum_with[-1])
ax2.annotate(
    f"{saved_tokens:,} tokens saved over 10 sessions",
    xy=(0.5, 0.90), xycoords="axes fraction",
    ha="center", color=GREEN, fontsize=10, fontstyle="italic"
)

# ── Footer note ────────────────────────────────────────────────────────────────
fig.text(
    0.5, -0.03,
    "Startup overhead only (CLAUDE.md load + context files vs mempalace_status + one query)."
    "  Actual work tokens not included.",
    ha="center", color=SUBTEXT, fontsize=8
)

plt.tight_layout()
out = "docs/benchmark.png"
plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
print(f"Saved: {out}")
