#!/usr/bin/env python3
"""
apply_mappings.py  ── Digital Twin OS: mapping loader (alpha)

目的:
  * legislation/common/mappings/*.yaml を全て読み込み、
    - YAML 構文エラーが無いことを確認
    - status != "active" のエントリはスキップ
  * 今は「読み込んで問題が無ければ 0 で終了」するだけ
    （実際の apply/transform は未実装）
使い方:
  python scripts/apply_mappings.py --mapping-glob "legislation/common/mappings/*.yaml"
"""

import argparse
import sys
from pathlib import Path

import yaml


def load_yaml(path: Path):
    """安全に YAML を読み込む。空ファイルは {} を返す。"""
    try:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            return {}  # 空 => 空 dict
        return yaml.safe_load(text) or {}
    except yaml.YAMLError as e:
        print(f"[ERROR] YAML syntax error in {path}: {e}", file=sys.stderr)
        raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mapping-glob",
        required=True,
        help='glob pattern e.g. "legislation/common/mappings/*.yaml"',
    )
    args = parser.parse_args()

    paths = sorted(Path(".").glob(args.mapping_glob))
    if not paths:
        print(f"[WARN] No files matched {args.mapping_glob}")
        return

    for p in paths:
        data = load_yaml(p)

        # ステータス判定: active 以外は読み飛ばし
        status = str(data.get("status", "active")).lower()
        if status != "active":
            print(f"[SKIP] {p} status={status}")
            continue

        # id が無い場合は警告（将来の拡張用）
        if "id" not in data:
            print(f"[WARN] {p} has no 'id' field (OK for now)")

        # ここで実際の mapping を適用するロジックを後日実装
        print(f"[PASS] {p} loaded (id={data.get('id', 'N/A')})")

    print("✔ All active mapping files loaded successfully")


if __name__ == "__main__":
    main()
