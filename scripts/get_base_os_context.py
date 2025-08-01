import yaml
import os
import sys
import subprocess

# --- 設定項目 ---
# リポジトリのルートディレクトリを基準パスとして取得
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 書籍プロジェクトリポジトリへのパス (WSL環境から見たパス)
# TODO: あなたのローカル環境のパスに合わせて修正してください
BOOK_REPO_PATH = "/home/mikieto/projects/lean-data-engineering-book"

# 書籍プロジェクトからハードコードで読み込むファイルのリスト
BOOK_FILES_TO_INCLUDE = [
    "lean_data_engineering_book.yaml",
    "records/decision_log.yaml",
    "records/task_log.yaml",
    "records/guard_log.yaml"
]
# --- 設定項目ここまで ---

def get_parsed_yaml_content(full_path):
    """
    指定されたフルパスのYAMLファイルを読み込み、パースしたYAMLオブジェクトを返す。
    """
    if not os.path.exists(full_path):
        print(f"警告: ファイルが見つかりません - {full_path}")
        return None
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            parsed_docs = list(yaml.safe_load_all(f))
            return parsed_docs[0] if parsed_docs else None
    except Exception as e:
        print(f"エラー: ファイル '{full_path}' の読み込み中に問題が発生しました: {e}")
        return None

def get_files_by_context_level(system_map_path, desired_context_level):
    """
    system_map.yamlを読み込み、指定されたcontext_levelを持つファイルのパスを返す。
    """
    full_system_map_path = os.path.join(REPO_ROOT, system_map_path)
    if not os.path.exists(full_system_map_path):
        print(f"エラー: system_map.yaml が見つかりません - {full_system_map_path}")
        return []
    
    try:
        with open(full_system_map_path, 'r', encoding='utf-8') as file:
            system_map_data = yaml.safe_load(file)

        files_to_include = []
        # 'layers' と 'other_root_files' の両方を安全にチェック
        for key in ['layers', 'other_root_files']:
            if system_map_data.get('system_architecture', {}).get(key):
                items = system_map_data['system_architecture'][key]
                if key == 'layers':
                    for layer in items:
                        for file_entry in layer.get('files', []):
                            if file_entry.get('context_level') == desired_context_level:
                                files_to_include.append(file_entry['path'])
                else: # other_root_files
                    for file_entry in items:
                        if file_entry.get('context_level') == desired_context_level:
                            files_to_include.append(file_entry['path'])
        return files_to_include
    except Exception as e:
        print(f"エラー: system_map.yaml の処理中に問題が発生しました: {e}")
        return []


def generate_context(output_file_path, system_map_path='system_map.yaml'):
    """
    コンテキストを結合し、指定されたファイルに出力する。
    """
    combined_documents = []

    # 1. 冒頭の概要ドキュメント
    overview_doc = {
        "jibun_os_base_context_overview": {
            "purpose": "Core OS Identity and Platform State",
            "overview": "..." # (内容は省略)
        }
    }
    combined_documents.append(overview_doc)

    # 2. system_map.yaml に基づく jibun_os のファイル読み込み (動的)
    jibun_os_files = get_files_by_context_level(system_map_path, "base_os_context")
    for relative_path in jibun_os_files:
        full_path = os.path.join(REPO_ROOT, relative_path)
        parsed_content = get_parsed_yaml_content(full_path)
        if parsed_content is not None:
            file_doc = {
                f"file_content_from_jibun_os_{relative_path.replace('/', '_').replace('.', '_')}": {
                    "path": f"jibun_os/{relative_path}",
                    "content": parsed_content
                }
            }
            combined_documents.append(file_doc)

    # 3. ハードコードされた書籍プロジェクトのファイル読み込み (静的)
    for book_file in BOOK_FILES_TO_INCLUDE:
        full_book_path = os.path.join(BOOK_REPO_PATH, book_file)
        parsed_content = get_parsed_yaml_content(full_book_path)
        if parsed_content is not None:
            file_doc = {
                f"file_content_from_book_{book_file.replace('/', '_').replace('.', '_')}": {
                    "path": f"book_repo/{book_file}",
                    "content": parsed_content
                }
            }
            combined_documents.append(file_doc)

    # 4. ファイルへの書き込み
    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            yaml.dump_all(combined_documents, outfile, default_flow_style=False, allow_unicode=True, sort_keys=False, explicit_start=True, width=120, indent=2, default_style='|')
        print(f"\nAIベースコンテキストが '{output_file_path}' に生成されました。")
    except Exception as e:
        print(f"エラー: コンテキストのファイルへの書き込み中に問題が発生しました: {e}")


if __name__ == "__main__":
    output_dir = os.path.join(REPO_ROOT, 'tmp')
    os.makedirs(output_dir, exist_ok=True)
    output_filename = 'ai_base_context.yaml'
    output_full_path = os.path.join(output_dir, output_filename)
    generate_context(output_full_path)
