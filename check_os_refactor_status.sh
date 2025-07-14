#!/bin/bash

# スクリプトの実行ディレクトリをプロジェクトルートに設定 (より堅牢な方法)
# このスクリプト自体がプロジェクトのルートに置かれていることを前提とする
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR" || exit

echo "--- Jibun OS 統合状態サマリー ---"
echo "最終確認日時: $(date +'%Y-%m-%d %H:%M:%S')"
echo "-----------------------------------"

# 1. Git リポジトリの基本情報
echo ">> 1. Git リポジトリ情報:"
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "  ✅ Git リポジトリ内で実行中。"
    echo "  現在のブランチ: $(git rev-parse --abbrev-ref HEAD)"
    echo "  最新のコミット: $(git log -1 --oneline --no-decorate)"
    if git status --porcelain | grep -q .; then
        echo "  ⚠️ 作業ツリーに未コミットの変更があります。git status を確認してください。"
    else
        echo "  👍 作業ツリーはクリーンです。"
    fi
else
    echo "  ❌ エラー: Git リポジトリではありません。プロジェクトルートで実行してください。"
    exit 1
fi
echo ""

# 2. ファイルシステム構造の主要な確認
echo ">> 2. ファイルシステム構造の確認:"
NEW_ROOT_LAYERS=("constitution" "legislation" "precedents" "records")
COMMON_LEGACY_DIRS=("common" "personal" "logs") # 以前の最上位ディレクトリ

# 新しい層のディレクトリ存在確認
ALL_NEW_LAYERS_EXIST=true
for dir in "${NEW_ROOT_LAYERS[@]}"; do
    if [ -d "$dir" ]; then
        echo "  ✅ 新しい層 '$dir/' は存在します。"
    else
        echo "  ❌ エラー: 新しい層 '$dir/' が見つかりません！"
        ALL_NEW_LAYERS_EXIST=false
    fi
done

# 古いディレクトリの残存確認 (空であるべき)
ALL_LEGACY_DIRS_CLEAN=true
for dir in "${COMMON_LEGACY_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        if [ -z "$(ls -A "$dir")" ]; then
            echo "  ✅ 古いディレクトリ '$dir/' は存在しますが、空です。(削除可能)"
        else
            echo "  ❌ エラー: 古いディレクトリ '$dir/' は空ではありません！中身を確認してください。"
            ls -al "$dir"
            ALL_LEGACY_DIRS_CLEAN=false
        fi
    else
        echo "  ✅ 古いディレクトリ '$dir/' は見つかりません。(削除済み)"
    fi
done

# system_map.yaml のルート存在確認
if [ -f "system_map.yaml" ]; then
    echo "  ✅ 'system_map.yaml' はルートディレクトリに存在します。"
else
    echo "  ❌ エラー: 'system_map.yaml' がルートディレクトリに見つかりません！"
fi
echo ""

# 3. 主要な設定ファイルの存在確認と内容の概観
echo ">> 3. 主要な設定ファイル概観:"
CONFIG_FILES=(
    "system_map.yaml"
    "constitution/common/constitution.yaml"
    "constitution/personal/constitution.yaml"
    "legislation/common/immune_system.yaml"
    "legislation/common/innate_immunity.yaml"
    "legislation/common/mappings.yaml"
    "legislation/common/implementation_framework.yaml"
    "legislation/common/taxonomy.yaml"
    "legislation/common/prompt_patterns.yaml"
    "legislation/common/projects/project_template.yaml"
    "legislation/common/domains/domain_template.yaml"
    "legislation/personal/core_principles.yaml"
    "legislation/personal/acquired_immunity.yaml"
    "legislation/personal/profile.yaml"
    "legislation/personal/projects/os_platform.yaml"
    "legislation/personal/domains/learning.yaml"
    "records/task_log.yaml"
    "records/decision_log.yaml"
    "records/guard_log.yaml"
    "docs/charter.md"
    "docs/architecture_overview.md"
    ".github/workflows/validate.yaml"
    "schema/jibun_os.schema.json"
    "scripts/get_base_os_context.py"
    "scripts/verify_system_map_paths.py"
    "tests/test_path_check.py"
    "README.md"
)

for file in "${CONFIG_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ ファイル '$file' は存在します。"
        # YAMLファイルの先頭数行を表示 (例: 名前やバージョン)
        if [[ "$file" == *.yaml || "$file" == *.yml ]]; then
            echo "    - $(head -n 5 "$file" | grep -E '^(name:|version:)' | tr -d '\r\n')"
        fi
    else
        echo "  ❌ エラー: 重要なファイル '$file' が見つかりません！"
    fi
done
echo ""

# 4. system_map.yaml にリストされたパスの整合性検証 (Pythonスクリプトを使用)
echo ">> 4. 'system_map.yaml' にリストされたパスの整合性検証:"
if [ -f "scripts/verify_system_map_paths.py" ]; then
    python scripts/verify_system_map_paths.py
    if [ $? -ne 0 ]; then
        echo "  ❌ 'system_map.yaml' パス整合性検証に失敗しました。上記のエラーを確認してください。"
        echo "  ⚠️ この検証が成功するまで、OSは正しく機能しない可能性があります。"
    else
        echo "  ✅ 'system_map.yaml' パス整合性検証に成功しました。物理パスは一致しています。"
    fi
else
    echo "  ⚠️ 警告: 'scripts/verify_system_map_paths.py' が見つかりません。パス検証を実行できません。"
fi
echo ""

echo "--- サマリー完了 ---"
echo "上記のエラー（❌）や警告（⚠️）を優先的に確認し、修正してください。"
echo "✅ が多ければ、リファクタリングは順調です。"