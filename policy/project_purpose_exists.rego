package jibun_os.policy.project

# ケース1: purpose_short キーが存在しない場合に deny
deny[msg] {
    input.project_name
    not input.project_charter.purpose_short
    msg := sprintf("Project '%s' must have a non-empty purpose_short.", [input.project_name])
}

# ケース2: purpose_short が空文字列の場合に deny
deny[msg] {
    input.project_name
    input.project_charter.purpose_short == ""
    msg := sprintf("Project '%s' must have a non-empty purpose_short.", [input.project_name])
}
