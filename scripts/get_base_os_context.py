import yaml
import os

# リポジトリのルートディレクトリを基準パスとして取得
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_file_content(file_path):
    """
    指定されたファイルのコンテンツを読み込み、
    結合時にルートレベルに合うよう先頭のYAMLドキュメントマーカーと空行を処理し、
    不要なインデントを削除する。
    """
    full_path = os.path.join(REPO_ROOT, file_path)
    if not os.path.exists(full_path):
        print(f"警告: ファイルが見つかりません - {full_path}")
        return f"ファイルが見つかりません: {file_path}"
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        processed_lines = []
        # 各ファイルの先頭にあるYAMLドキュメントマーカー (---) や不要な空行をスキップ
        # また、読み込んだ内容がルートレベルから始まるように、最初の非空白行のインデントを基準に調整
        first_content_line_indent = -1
        for line in lines:
            stripped_line = line.strip()
            if stripped_line == '---' or stripped_line == '': # YAMLドキュメントマーカーと空行をスキップ
                continue
            
            # 最初の内容行のインデントを基準に設定
            if first_content_line_indent == -1:
                first_content_line_indent = len(line) - len(line.lstrip())

            # 基準インデントを削除
            if line.startswith(' ' * first_content_line_indent):
                processed_lines.append(line[first_content_line_indent:])
            else:
                # 基準インデントよりも少ないインデントの行（通常は発生しないはずだが念のため）
                processed_lines.append(line.lstrip())

        return "".join(processed_lines) # 結合して返す

    except Exception as e:
        print(f"エラー: ファイル '{full_path}' の読み込み中に問題が発生しました: {e}")
        return f"ファイル読み込みエラー: {file_path}"

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
        if 'system_architecture' in system_map_data and 'layers' in system_map_data['system_architecture']:
            for layer in system_map_data['system_architecture']['layers']:
                if 'files' in layer:
                    for file_entry in layer['files']:
                        if file_entry.get('context_level') == desired_context_level:
                            files_to_include.append(file_entry['path'])
            # 'other_root_files' もチェック
            if 'other_root_files' in system_map_data['system_architecture']:
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

def generate_base_os_context(output_file_path, system_map_path='common/system_map.yaml'):
    """
    コア＆プラットフォームコンテキストを結合し、指定されたファイルに出力する。
    system_map.yamlからファイルを動的に取得する。
    """
    base_context_files = get_files_by_context_level(system_map_path, "base_os_context")

    if not base_context_files:
        print("警告: 'base_os_context' に含まれるファイルが見つかりませんでした。system_map.yamlを確認してください。")
        return

    combined_content = []
    combined_content.append("# Jibun OS Base Context (Core & Platform)\n")
    combined_content.append("---")
    combined_content.append("## Purpose: Core OS Identity and Platform State")
    combined_content.append("This consolidated context provides the fundamental principles of Jibun OS,")
    combined_content.append("its structural blueprint, operational framework, and its current platform status.")
    combined_content.append("It is always loaded to give the AI a complete understanding of the OS it operates within.")
    combined_content.append("---")

    for relative_path in base_context_files:
        content = get_file_content(relative_path)
        combined_content.append(f"\n# --- Content from {relative_path} ---\n")
        combined_content.append(content)
        combined_content.append("\n---") # 各ファイルの区切り

    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            outfile.write("\n".join(combined_content) + "\n") # ← ここに「 + "\n" 」を追加
        print(f"AIベースコンテキストが '{output_file_path}' に生成されました。")
    except Exception as e:
        print(f"エラー: コンテキストのファイルへの書き込み中に問題が発生しました: {e}")

if __name__ == "__main__":
    output_dir = os.path.join(REPO_ROOT, 'tmp')
    os.makedirs(output_dir, exist_ok=True) # tmp ディレクトリが存在しない場合に作成

    output_filename = 'ai_base_context.yaml'
    output_full_path = os.path.join(output_dir, output_filename)

    generate_base_os_context(output_full_path)
    print(f"\nAIへのフィード方法: '{output_full_path}' の内容をコピーして貼り付けてください。")
    print("注意: Jibun OSのソースYAMLファイルを修正した場合は、このスクリプトを再実行してください。")
