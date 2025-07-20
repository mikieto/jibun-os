# policy/project_purpose_exists.rego

package jibun_os.policy.project

# Deny if a project file is missing a non-empty purpose_short.
deny[msg] {
    # Check that this rule applies only to project files (which have a project_name).
    _ = input.project_name

    # The rule's logic: deny if purpose_short is not provided or is empty.
    not input.project_charter.purpose_short

    # The error message to return.
    msg = sprintf("Project '%s' must have a non-empty purpose_short.", [input.project_name])
}
