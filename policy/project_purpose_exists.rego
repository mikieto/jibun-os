package jibun_os.policy.project

# Deny if a project file is missing a non-empty purpose_short.
deny[msg] {
    # This rule only applies to project files.
    input.project_name

    # The logic is now more explicit with parentheses and an empty string check.
    (not input.project_charter.purpose_short) or (input.project_charter.purpose_short == "")

    # The error message.
    msg = sprintf("Project '%s' must have a non-empty purpose_short.", [input.project_name])
}
