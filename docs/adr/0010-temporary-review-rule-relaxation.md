---
id: DEC-OS-20250807-001
date: 2025-08-07
project: OS
title: "Temporarily disable PR approval checks"
status: accepted   # → 後で replaced / superseded に更新
sources: []
sources:
  - https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule
links:
  issues: []
  guard_events: []
---

## Context
We are currently the **sole developer** on this repository.  
`Require pull-request reviews before merging` and `Require review from CODEOWNERS` cause a dead-lock because the only CODEOWNER is also the PR author.

## Decision
- Temporarily **turn off** these two branch-protection settings:
  - `Require approvals` → 0
  - `Require review from CODEOWNERS` → off

## Consequences
- All PRs can be merged without extra clicks for the time being.
- We will revert this rule as soon as a bot or sub-account can act as reviewer.

## Expiry
This ADR expires when:
1. A bot / secondary account (`ledger-bot`) is ready **or**
2. A second human contributor joins the project.

