#!/usr/bin/env python3
"""Session end hook — logs timestamp to today's daily note."""
import os
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
today = datetime.now().strftime("%Y-%m-%d")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
daily_dir = os.path.join(ROOT, "Brain", "Daily")
os.makedirs(daily_dir, exist_ok=True)
with open(os.path.join(daily_dir, f"{today}.md"), "a") as f:
    f.write(f"--- Session ended {timestamp} ---\n")
