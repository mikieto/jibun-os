import yaml
import os
import sys
import subprocess


# リポジトリのルートディレクトリを基準パスとして取得
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_parsed_yaml_content(file_path):
    """
    指定されたYAMLファイルを読み込み、パースしたYAMLオブジェクトを返す。
    エラー時にはNoneを返す。
    """
    full_path = os.path.join(REPO_ROOT, file_path)
    if not os.path.exists(full_path):
        print(f"警告: ファイルが見つかりません - {full_path}")
        return None
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            # YAMLファイルを複数ドキュメントとしてロード
            # yaml.safe_load_all はジェネレータを返す
            parsed_docs = list(yaml.safe_load_all(f))
            return parsed_docs[0] if parsed_docs else None # 最初のドキュメントを返す
    except yaml.YAMLError as e:
        print(f"エラー: ファイル '{full_path}' のYAMLパースエラー: {e}")
        return None
    except Exception as e:
        print(f"エラー: ファイル '{full_path}' の読み込み中に問題が発生しました: {e}")
        return None

def get_files_by_context_level(system_map_path, desired_context_level):
    """
    system_map.yamlを読み込み、指定されたcontext_levelを持つファイルのパスを返す。
    """
    # system_map.yaml がルートにあるため、直接指定
    full_system_map_path = os.path.join(REPO_ROOT, system_map_path) # system_map_path は "system_map.yaml"
    if not os.path.exists(full_system_map_path):
        print(f"エラー: system_map.yaml が見つかりません - {full_system_map_path}")
        return []

    try:
        with open(full_system_map_path, 'r', encoding='utf-8') as file:
            system_map_data = yaml.safe_load(file)

        files_to_include = []
        if 'system_architecture' in system_map_data and 'layers' in system_map_data['system_architecture']:
            for layer in system_map_data['system_architecture']['layers']:
                if 'files' in layer:
                    for file_entry in layer['files']:
                        if file_entry.get('context_level') == desired_context_level:
                            files_to_include.append(file_entry['path'])
            # 'other_root_files' もチェック
            if 'system_architecture' in system_map_data and 'other_root_files' in system_map_data['system_architecture']: # Noneチェック追加
                for file_entry in system_map_data['system_architecture']['other_root_files']:
                    if file_entry.get('context_level') == desired_context_level:
                        files_to_include.append(file_entry['path'])
        return files_to_include
    except yaml.YAMLError as e:
        print(f"エラー: system_map.yaml のパースエラー: {e}")
        return []
    except Exception as e:
        print(f"エラー: system_map.yaml の読み込み中に問題が発生しました: {e}")
        return []

def generate_base_os_context(output_file_path, system_map_path='system_map.yaml'): # system_map_pathのデフォルト値を修正
    """
    コア＆プラットフォームコンテキストを結合し、指定されたファイルに出力する。
    system_map.yamlからファイルを動的に取得する。
    """
    base_context_file_paths = get_files_by_context_level(system_map_path, "base_os_context")

    if not base_context_file_paths:
        print("警告: 'base_os_context' に含まれるファイルが見つかりませんでした。system_map.yamlを確認してください。")
        return

    # 複数のYAMLドキュメントとして結合するためのリスト
    combined_documents = []

    # 1. 冒頭の概要ドキュメント
    overview_doc = {
        "digital_twin_os_base_context_overview": {
            "purpose": "Core OS Identity and Platform State",
            "overview": "This consolidated context provides the fundamental principles of Digital Twin OS, its structural blueprint, operational framework, and its current platform status. It is always loaded to give the AI a complete understanding of the OS it operates within."
        }
    }
    combined_documents.append(overview_doc)

    # 2. 各ファイルのコンテンツを個別のドキュメントとして追加
    for relative_path in base_context_file_paths:
        parsed_content = get_parsed_yaml_content(relative_path) # ここで相対パスをそのまま使用
        if parsed_content is not None:
            # 各ファイルのコンテンツを独立したYAMLドキュメントとしてリストに追加
            # AIが「これはファイルの内容である」と認識しやすいように、メタ情報を追加
            file_doc = {
                f"file_content_from_{relative_path.replace('/', '_').replace('.', '_')}": {
                    "path": relative_path,
                    "content": parsed_content # YAMLオブジェクトとしてそのまま挿入
                }
            }
            combined_documents.append(file_doc)
        else:
            print(f"警告: '{relative_path}' のコンテンツをパースできませんでした。スキップします。")

    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            # 各YAMLオブジェクトを separate ドキュメントとしてダンプ
            # explicit_start=True で各ドキュメントの前に --- を明示的に追加
            # width=120 は行長警告へのヒント。indent=2で yamllint のデフォルトに合わせる
            # default_style='|' を追加して複数行文字列をリテラルスタイルで出力
            yaml.dump_all(combined_documents, outfile, default_flow_style=False, allow_unicode=True, sort_keys=False, explicit_start=True, width=120, indent=2, default_style='|')
        print(f"AIベースコンテキストが '{output_file_path}' に生成されました。")

        # --- ここから yamlfix の組み込み ---
        try:
            subprocess.run(['yamlfix', output_file_path], check=True, capture_output=True)
            print(f"'{output_file_path}' を yamlfix で自動整形しました。")
        except subprocess.CalledProcessError as e:
            print(f"警告: '{output_file_path}' の yamlfix による整形に失敗しました (エラーコード: {e.returncode}):", file=sys.stderr)
            print(f"STDOUT: {e.stdout.decode()}", file=sys.stderr)
            print(f"STDERR: {e.stderr.decode()}", file=sys.stderr)
            print("手動で 'yamlfix tmp/ai_base_context.yaml' を実行する必要があるかもしれません。", file=sys.stderr)
        except FileNotFoundError:
            print(f"警告: 'yamlfix' コマンドが見つかりません。pip install yamlfix を実行してください。", file=sys.stderr)
        except Exception as e:
            print(f"警告: yamlfix 実行中に予期せぬエラーが発生しました: {e}", file=sys.stderr)
        # --- yamlfix の組み込みここまで ---

    except Exception as e:
        print(f"エラー: コンテキストのファイルへの書き込み中に問題が発生しました: {e}")

if __name__ == "__main__":
    output_dir = os.path.join(REPO_ROOT, 'tmp')
    os.makedirs(output_dir, exist_ok=True)

    output_filename = 'ai_base_context.yaml'
    output_full_path = os.path.join(output_dir, output_filename)

    generate_base_os_context(output_full_path)
    print(f"\nAIへのフィード方法: '{output_full_path}' の内容をコピーして貼り付けてください。")
    print("注意: Digital Twin OSのソースYAMLファイルを修正した場合は、このスクリプトを再実行してください。")
