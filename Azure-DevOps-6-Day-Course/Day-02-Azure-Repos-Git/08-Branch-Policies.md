# 08 - Branch Policies

## Overview

**Branch policies** protect important branches (like `main`) by enforcing rules that must be satisfied before changes can be merged via a pull request. They turn your team's review conventions into automatically enforced guardrails.

> When a branch has policies, you typically **cannot push directly** to it — changes must go through a pull request that satisfies the policies.

## Where to Configure

**Repos → Branches → (⋯ next to a branch) → Branch policies**

You can also set policies at **Project settings → Repositories → Policies** (across repos/branches).

## The Core Policies

### 1. Require a minimum number of reviewers
- Set how many approvals are needed (e.g., 2).
- Option: **prohibit the most recent pusher from approving** their own changes.
- Option: **reset votes when new changes are pushed**.

### 2. Check for linked work items
Requires each PR to be linked to at least one work item — enforcing traceability between code and Boards.

### 3. Check for comment resolution
Requires all PR comments to be **resolved** before completion.

### 4. Limit merge types
Control which completion options are allowed (e.g., only **Squash**) to keep history consistent.

### 5. Build validation
Requires one or more **pipelines** to run and **pass** on the PR before it can merge. This is how you enforce that code compiles and tests pass. (Covered more on Day 3.)

### 6. Status checks
Requires an external service (via the Status API) to post a successful status — e.g., a third-party scanner or quality gate.

### 7. Automatically included reviewers
Automatically add specific people/groups as reviewers when certain files/paths change (e.g., require a security team review for changes under `/auth`).

## Required vs Optional Policies

- **Required** policies block completion until satisfied.
- **Optional** reviewers/checks are informative but don't block.

## Example Policy Set for `main`

A solid starting configuration:

- [x] Require **2** reviewers, reset votes on new pushes.
- [x] Prohibit requestor from approving their own PR.
- [x] Check for **linked work items** (required).
- [x] Check for **comment resolution** (required).
- [x] **Build validation:** CI pipeline must pass.
- [x] Limit merge types to **Squash**.
- [x] Automatically include the **leads** group as reviewers.

## Bypassing Policies

Certain administrators can be granted **"Bypass policies when completing pull requests"** or **"Bypass policies when pushing"** permissions. Use sparingly — bypasses defeat the purpose and should be audited.

## How Policies Interact with PRs

```
Open PR → policies evaluated continuously:
   ├── Reviewers approved?        ✅/❌
   ├── Work item linked?          ✅/❌
   ├── Comments resolved?         ✅/❌
   └── Build validation passed?   ✅/❌
Complete button enabled only when all REQUIRED policies pass.
```

## Best Practices

- Always protect `main` (and `develop`/release branches) with policies.
- Require at least **build validation** + **1–2 reviewers**.
- Require **linked work items** for traceability.
- Keep bypass permissions to a minimum and audit them.
- Use **auto-complete** so PRs merge the moment all policies pass.

## Summary

- Branch policies enforce quality rules on protected branches via pull requests.
- Key policies: required reviewers, linked work items, comment resolution, merge-type limits, and **build validation**.
- Direct pushes to a policy-protected branch are blocked; changes go through PRs.

## Knowledge Check

1. Which policy ensures code compiles/tests pass before merging?
2. How can you enforce that every PR is tied to a work item?
3. What does "prohibit the most recent pusher from approving" prevent?

➡️ Next: [09 - Merge Conflicts](./09-Merge-Conflicts.md)
