# policy/project_purpose_exists.rego

package jibun_os.policy.project

# 違反（violation）のルールを定義
# プロジェクトファイルに purpose_short がない、または空の場合に違反とする
violation[msg] {
    # 入力されるYAMLファイルがプロジェクト定義だと仮定
    input.project_name
    
    # purpose_short が存在しない、または空文字列の場合
    not input.project_charter.purpose_short

    # 違反メッセージを生成
    msg := sprintf("Project '%s' must have a non-empty purpose_short.", [input.project_name])
}