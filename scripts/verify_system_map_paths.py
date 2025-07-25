# path: scripts/verify_system_map_paths.py

import yaml
import os
import sys
import glob # globモジュールをインポート

def verify_system_map_paths(system_map_path="system_map.yaml"):
    """
    system_map.yaml に記述されているすべてのファイルパスが
    実際にファイルシステム上に存在するかを検証します。
    ワイルドカード (*) に対応しています。
    """
    print(f"--- Verifying paths in {system_map_path} ---")

    if not os.path.exists(system_map_path):
        print(f"ERROR: system_map.yaml not found at {system_map_path}")
        return False

    try:
        with open(system_map_path, 'r', encoding='utf-8') as f:
            system_map = yaml.safe_load(f)
    except Exception as e:
        print(f"ERROR: Failed to read or parse system_map.yaml: {e}")
        return False

    base_dir = os.path.dirname(os.path.abspath(system_map_path))
    found_errors = False
    checked_paths_count = 0

    # 'layers' と 'other_root_files' の両方をチェックするための関数
    def check_file_entries(file_entries, section_name):
        nonlocal found_errors, checked_paths_count
        for file_entry in file_entries:
            relative_path = file_entry.get('path')
            if not relative_path:
                print(f"WARNING: File entry found without 'path' in section '{section_name}'")
                continue

            full_path = os.path.join(base_dir, relative_path)
            checked_paths_count += 1

            # --- MODIFIED BLOCK START ---
            if "*" in relative_path:
                # ワイルドカードを展開し、一致するファイルが1つ以上あるかを確認
                # 注: ディレクトリが空でもCIをパスさせたい場合は `if not glob.glob(full_path):` をコメントアウト
                if not glob.glob(full_path):
                    print(f"ERROR: Glob pattern in system_map.yaml found no files: {relative_path}")
                    found_errors = True
            elif not os.path.exists(full_path):
                print(f"ERROR: Path in system_map.yaml does not exist: {relative_path}")
                found_errors = True
            elif not os.path.isfile(full_path):
                 print(f"ERROR: Path in system_map.yaml is not a file: {relative_path}")
                 found_errors = True
            # --- MODIFIED BLOCK END ---

    # 各セクションを検証
    for layer in system_map.get('system_architecture', {}).get('layers', []):
        check_file_entries(layer.get('files', []), f"layer '{layer.get('name', 'Unnamed')}'")

    check_file_entries(system_map.get('other_root_files', []), 'other_root_files')

    print(f"\n--- Verification Summary ({checked_paths_count} paths checked) ---")
    if found_errors:
        print("Verification FAILED: Some paths listed in system_map.yaml are incorrect or missing.")
        return False
    else:
        print("Verification SUCCESS: All paths listed in system_map.yaml are valid.")
        return True

if __name__ == "__main__":
    if not verify_system_map_paths():
        sys.exit(1)
    else:
        sys.exit(0)
