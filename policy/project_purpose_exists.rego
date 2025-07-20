package jibun_os.policy.project

import rego.v1

deny[msg] if {
    input.project_name
    not input.project_charter.purpose_short
    msg := sprintf("Project '%s' must have a non-empty purpose_short.", [input.project_name])
}

deny[msg] if {
    input.project_name
    input.project_charter.purpose_short == ""
    msg := sprintf("Project '%s' must have a non-empty purpose_short.", [input.project_name])
}
