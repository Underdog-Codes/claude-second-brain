#!/usr/bin/env bash
# Logs session end timestamp to today's daily note
VAULT_ROOT="$(cd "$(dirname "$0")/../../../" && pwd)"
TODAY=$(date +%Y-%m-%d)
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")
DAILY="${VAULT_ROOT}/Brain/Daily/${TODAY}.md"
mkdir -p "$(dirname "$DAILY")"
echo "--- Session ended ${TIMESTAMP} ---" >> "$DAILY"
exit 0
