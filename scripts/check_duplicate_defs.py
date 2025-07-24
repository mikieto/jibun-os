#!/usr/bin/env python3
import yaml
import glob
import sys
import argparse

CRITICAL_KEYS = {
    "foundational_pillars",
    "evolutionary_roadmap",
    "core_values",
    "ai_governance_principles",
}

def collect_keys(obj, path, hit):
    if isinstance(obj, dict):
        for k, v in obj.items():
            hit.setdefault(k, set()).add(path)
            collect_keys(v, path, hit)
    elif isinstance(obj, list):
        for item in obj:
            collect_keys(item, path, hit)

def main():
    parser = argparse.ArgumentParser(
        description="Detect duplicate keys (including nested) across YAML files"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Only list duplicates (always exit 0)",
    )
    args = parser.parse_args()

    # 対象ファイル一覧
    paths = glob.glob("constitution/**/*.yaml", recursive=True) + \
            glob.glob("legislation/**/*.yaml", recursive=True)

    # key → set(file paths)
    hit = {}

    # 各ファイルからキーを再帰的に収集
    for p in paths:
        try:
            data = yaml.safe_load(open(p))
        except Exception:
            continue
        collect_keys(data, p, hit)

    # 重複チェック
    err = 0
    for k, files in sorted(hit.items()):
        if k in CRITICAL_KEYS and len(files) > 1:
            print(f"DUPLICATE KEY '{k}' in {len(files)} files:")
            for f in sorted(files):
                print(f"  - {f}")
            if not args.list:
                err = 1

    sys.exit(err)

if __name__ == "__main__":
    main()
