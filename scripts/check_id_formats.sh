#!/usr/bin/env bash
set -e
err=0

check_yaml_ids() {
  local file=$1 regex=$2 label=$3
  while read -r id; do
    [[ $id =~ $regex ]] || {
      echo "ID format error [$label]: $id ($file)"
      err=1
    }
  done < <(yq e '.. | select(tag=="!!map" and has("id")) | .id' "$file")
}

# --- DEC / TASK ---
check_yaml_ids records/task_log.yaml     '^TASK-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{3}$'  TASK
check_yaml_ids records/decision_log.yaml '^DEC-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{3}$'   DEC

# --- Guard IDs ---
check_yaml_ids legislation/common/innate_immunity.yaml     '^G[0-9]{3}$'                        GCOMMON
check_yaml_ids legislation/personal/acquired_immunity.yaml '^P[0-9]{3}$'                        GPERSONAL

# --- KPI IDs ---
check_yaml_ids legislation/common/kpi.yaml '^KPI-(PROJ|HEALTH)-[0-9]{3}$' KPI

# --- 重複検出（全カテゴリまとめて一括） ---------------
dup=$( ( yq e '.tasks[].id' records/task_log.yaml
         yq e '.decisions[].id' records/decision_log.yaml
         yq e '.. | select(tag=="!!map" and has("id")) | .id' legislation/common/innate_immunity.yaml
         yq e '.. | select(tag=="!!map" and has("id")) | .id' legislation/personal/acquired_immunity.yaml
         yq e '.. | select(tag=="!!map" and has("id")) | .id' legislation/common/kpi.yaml
       ) | sort | uniq -d )
if [[ -n $dup ]]; then
  echo "Duplicate ID(s) detected:"
  echo "$dup"
  err=1
fi

exit $err
