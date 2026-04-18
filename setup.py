#!/usr/bin/env python3
"""
Claude Brain Template — Setup
Works on Windows, Mac, and Linux.
"""
import subprocess, sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def run(cmd, label):
    print(f"\n  [{label}] {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode != 0:
        print(f"\n  ERROR: step failed. Check output above.")
        sys.exit(1)

print("""
  Claude Brain Template — Setup
  ==============================
""")

# 1. Install mempalace
run([sys.executable, "-m", "pip", "install", "mempalace", "-q"], "1/2 Installing mempalace")

# 2. Mine the vault
env = os.environ.copy()
env["PYTHONUTF8"] = "1"
print("\n  [2/2] Indexing your vault into memory...")
result = subprocess.run(["mempalace", "mine", ROOT], cwd=ROOT, env=env)
if result.returncode != 0:
    # fallback: run as python module
    result = subprocess.run([sys.executable, "-m", "mempalace", "mine", ROOT], cwd=ROOT, env=env)
    if result.returncode != 0:
        print("\n  ERROR: Mining failed.")
        sys.exit(1)

print("""
  Done!
  Open this folder in Claude Code and start a new session.
""")
