#!/usr/bin/env python3
"""
Claude Brain Template - Setup
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
  Claude Brain Template - Setup
  ==============================
""")

# 1. Install mempalace
run([sys.executable, "-m", "pip", "install", "mempalace", "-q"], "1/2 Installing mempalace")

# 1b. Point palace into vault root (keeps all data with the project, off the C drive)
import json, pathlib
palace_path = str(pathlib.Path(ROOT) / ".mempalace" / "palace").replace("\\", "/")
config_dir = pathlib.Path.home() / ".mempalace"
config_dir.mkdir(parents=True, exist_ok=True)
config_file = config_dir / "config.json"
cfg = {}
if config_file.exists():
    try:
        cfg = json.loads(config_file.read_text())
    except Exception:
        pass
cfg["palace_path"] = palace_path
config_file.write_text(json.dumps(cfg, indent=2))
print(f"\n  [1b] Palace path set to: {palace_path}")

# 2. Mine the vault
env = os.environ.copy()
env["PYTHONUTF8"] = "1"
print("\n  [2/2] Indexing your vault into memory...")
result = subprocess.run([sys.executable, "-m", "mempalace", "mine", ROOT], cwd=ROOT, env=env)
if result.returncode != 0:
    print("\n  ERROR: Mining failed.")
    sys.exit(1)

print("""
  Done!
  Open this folder in Claude Code and start a new session.
""")
