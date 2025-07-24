#!/usr/bin/env bash
set -e
err=0
check() {
  local file=$1 regex=$2
  while read -r id; do
    [[ $id =~ $regex ]] || { echo "ID format error: $id ($file)"; err=1; }
  done < <(yq e '.. | select(tag=="!!map" and has("id")) | .id' "$file")
}
check records/task_log.yaml     '^TASK-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{3}$'
check records/decision_log.yaml '^DEC-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{3}$'
exit $err
