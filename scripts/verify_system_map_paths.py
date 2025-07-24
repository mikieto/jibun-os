import yaml
import os
import sys

def verify_system_map_paths(system_map_path="system_map.yaml"):
    """
    system_map.yaml に記述されているすべてのファイルパスが
    実際にファイルシステム上に存在するかを検証します。

    Args:
        system_map_path (str): system_map.yaml ファイルへのパス。

    Returns:
        bool: 全てのパスが存在すれば True、一つでも存在しなければ False。
    """
    print(f"--- Verifying paths in {system_map_path} ---")

    if not os.path.exists(system_map_path):
        print(f"ERROR: system_map.yaml not found at {system_map_path}")
        return False

    try:
        with open(system_map_path, 'r', encoding='utf-8') as f:
            system_map = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"ERROR: Failed to parse system_map.yaml: {e}")
        return False
    except Exception as e:
        print(f"ERROR: An unexpected error occurred while reading system_map.yaml: {e}")
        return False

    # system_map.yaml がルートに置かれていることを前提に、そのディレクトリをベースとする
    base_dir = os.path.dirname(os.path.abspath(system_map_path))

    found_errors = False
    checked_paths_count = 0

    # 'layers' セクションのパスを検証
    for layer in system_map.get('system_architecture', {}).get('layers', []):
        for file_entry in layer.get('files', []):
            relative_path = file_entry.get('path')
            if not relative_path:
                print(f"WARNING: File entry found without 'path' in layer '{layer.get('name', 'Unnamed Layer')}'")
                continue # pathがないエントリはスキップ

            full_path = os.path.join(base_dir, relative_path)
            checked_paths_count += 1

            if not os.path.exists(full_path):
                print(f"ERROR: Path in system_map.yaml does not exist: {relative_path} (Full: {full_path})")
                found_errors = True
            elif not os.path.isfile(full_path):
                print(f"ERROR: Path in system_map.yaml is not a file (or is a directory): {relative_path} (Full: {full_path})")
                found_errors = True

            # (オプション) dependencies のパスも検証する場合はここに追加
            # 例: for dep_rel_path in file_entry.get('dependencies', []):
            #         dep_full_path = os.path.join(os.path.dirname(full_path), dep_rel_path) # 依存元からの相対パス
            #         if not os.path.exists(dep_full_path):
            #             print(f"ERROR: Dependency path for {relative_path} does not exist: {dep_rel_path} (Full: {dep_full_path})")
            #             found_errors = True

    # 'other_root_files' セクションのパスを検証
    for file_entry in system_map.get('other_root_files', []):
        relative_path = file_entry.get('path')
        if not relative_path:
            print(f"WARNING: File entry found without 'path' in 'other_root_files'")
            continue

        full_path = os.path.join(base_dir, relative_path)
        checked_paths_count += 1

        if not os.path.exists(full_path):
            print(f"ERROR: Path in system_map.yaml does not exist: {relative_path} (Full: {full_path})")
            found_errors = True
        elif not os.path.isfile(full_path):
            print(f"ERROR: Path in system_map.yaml is not a file (or is a directory): {relative_path} (Full: {full_path})")
            found_errors = True

    print(f"\n--- Verification Summary ({checked_paths_count} paths checked) ---")
    if found_errors:
        print("Verification FAILED: Some paths listed in system_map.yaml are incorrect or missing.")
        return False
    else:
        print("Verification SUCCESS: All paths listed in system_map.yaml exist and are files.")
        return True

if __name__ == "__main__":
    # スクリプトが実行されるカレントディレクトリをプロジェクトルートと仮定
    # もし別の場所から実行する場合は、system_map_path を調整する必要がある
    if not verify_system_map_paths():
        sys.exit(1) # 検証失敗時に終了コード1を返す
    else:
        sys.exit(0) # 検証成功時に終了コード0を返す
