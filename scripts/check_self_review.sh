#!/usr/bin/env bash
set -e

FILE=${FILE:-tmp/ai_base_context.yaml}

if [ ! -f "$FILE" ]; then
  echo "::notice ::$FILE not found. Skipping self‑review check."
  exit 0
fi

if ! grep -q '\[Self-Review: OK\]' "$FILE"; then
  echo "::error ::[Self-Review: OK] not found in $FILE"
  exit 1
fi
