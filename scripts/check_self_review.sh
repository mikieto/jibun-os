#!/usr/bin/env bash
set -e
file="ai_base_context.yaml"
grep -q '\[Self-Review: OK\]' "$file" || {
  echo "::error ::[Self-Review: OK] not found in $file"
  exit 1
}
