"""
Benchmark chart for Claude Second Brain.

Three comparisons, all shown as % savings with raw token counts as secondary info:

1. STARTUP COST
   Without: Heavy CLAUDE.md (rules + identity + stack) + auto-loaded project
            context files + memory.md = ~1800 tokens every session
   With:    Trimmed CLAUDE.md (20 lines, rules only) + mempalace_status = ~290 tokens

2. CONTEXT RETRIEVAL (per lookup)
   Without: Loading full markdown files directly into context. Avg 3 files at
            ~800 tokens each = ~2400 tokens, loaded in full whether needed or not
   With:    mempalace query returns top 5 relevant chunks = ~400 tokens, only
            what is relevant to the current question

3. TYPICAL SESSION TOTAL OVERHEAD
   (startup + 3 context retrievals, no actual work tokens counted)
   Without: 1800 + (3 x 2400) = ~9000 tokens of overhead
   With:    290  + (3 x 400)  = ~1490 tokens of overhead

All numbers represent token overhead only, not the tokens used for actual work.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Data ───────────────────────────────────────────────────────────────────────
categories = [
    "Session Startup\n(files loaded before 1st prompt)",
    "Fetching Context\n(loading files vs mempalace query)",
    "Typical Session Total\n(startup + 3 context fetches)"
]

without = [1800, 2400, 9000]
with_   = [290,  400,  1490]

savings_pct = [round((1 - w / wo) * 100) for wo, w in zip(without, with_)]

# ── Style ──────────────────────────────────────────────────────────────────────
BG      = "#0d1117"
PANEL   = "#161b22"
BLUE    = "#58a6ff"
GREEN   = "#3fb950"
GRID    = "#21262d"
TEXT    = "#e6edf3"
SUBTEXT = "#8b949e"
RED     = "#f85149"

fig, ax = plt.subplots(figsize=(13, 7), facecolor=BG)
ax.set_facecolor(PANEL)
for spine in ax.spines.values():
    spine.set_edgecolor(GRID)

x   = np.arange(len(categories))
w   = 0.32
gap = 0.04

bars_wo = ax.bar(x - w/2 - gap/2, without, w,
                 color=BLUE,  alpha=0.85, label="Without Claude Second Brain")
bars_wi = ax.bar(x + w/2 + gap/2, with_,   w,
                 color=GREEN, alpha=0.85, label="With Claude Second Brain")

# ── Raw token labels on bars ───────────────────────────────────────────────────
for bar, val in zip(bars_wo, without):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 60,
            f"{val:,}", ha="center", va="bottom", color=BLUE,
            fontsize=10, fontweight="bold")

for bar, val in zip(bars_wi, with_):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 60,
            f"{val:,}", ha="center", va="bottom", color=GREEN,
            fontsize=10, fontweight="bold")

# ── % savings badges centred between each pair ─────────────────────────────────
for i, pct in enumerate(savings_pct):
    mid_x  = x[i]
    mid_y  = max(without[i], with_[i]) * 0.52
    label  = f"{pct}% less"
    ax.text(mid_x, mid_y, label,
            ha="center", va="center", color="white",
            fontsize=13, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", facecolor=RED,
                      edgecolor="none", alpha=0.88))

# ── Axes ───────────────────────────────────────────────────────────────────────
ax.set_xticks(x)
ax.set_xticklabels(categories, color=TEXT, fontsize=12)
ax.set_ylabel("Tokens (overhead only)", color=SUBTEXT, fontsize=11)
ax.tick_params(axis="y", colors=SUBTEXT)
ax.yaxis.label.set_color(SUBTEXT)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0)
ax.set_ylim(0, max(without) * 1.22)

# ── Legend ─────────────────────────────────────────────────────────────────────
legend = ax.legend(facecolor=PANEL, edgecolor=GRID, labelcolor=TEXT,
                   fontsize=10, loc="upper right")

# ── Title + subtitle ───────────────────────────────────────────────────────────
fig.text(0.5, 1.01,
         "Claude Second Brain  —  Token Overhead Savings",
         ha="center", color=TEXT, fontsize=16, fontweight="bold")
fig.text(0.5, 0.96,
         "Tokens burned on overhead — before and during your session, not counting actual responses",
         ha="center", color=SUBTEXT, fontsize=10)

# ── Footer methodology note ────────────────────────────────────────────────────
fig.text(
    0.5, -0.04,
    "Without: heavy CLAUDE.md (identity+stack+rules) + auto-loaded context files + memory.md  |  "
    "With: 20-line CLAUDE.md + mempalace_status on wake-up + semantic query returning top 5 chunks",
    ha="center", color=SUBTEXT, fontsize=8, wrap=True
)

plt.tight_layout()
out = "docs/benchmark.png"
plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
print(f"Saved: {out}")
print(f"Savings: {savings_pct[0]}% startup | {savings_pct[1]}% per retrieval | {savings_pct[2]}% session total")
