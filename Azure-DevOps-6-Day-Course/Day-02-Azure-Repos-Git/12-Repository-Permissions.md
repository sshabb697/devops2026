# 12 - Repository Permissions

## Overview

**Repository permissions** in Azure Repos control who can read, contribute to, manage, and protect your Git repositories. They build on the general permission model from Day 1 (Allow / Deny / Not set, assigned to groups) but apply specifically to repos and even individual branches.

## Where to Configure

- **All repos in a project:** *Project settings → Repositories → (select "All Repositories") → Security*.
- **A single repo:** *Project settings → Repositories → (select the repo) → Security*.
- **A single branch:** *Repos → Branches → (⋯) → Branch security*.

## Key Repository Permissions

| Permission | Allows the user to... |
| ---------- | --------------------- |
| **Read** | Clone, fetch, view code |
| **Contribute** | Push commits, create branches, open PRs |
| **Contribute to pull requests** | Comment/vote on PRs |
| **Create branch** | Create new branches |
| **Create tag** | Create tags |
| **Manage permissions** | Change security settings on the repo |
| **Force push (rewrite history)** | Force-push / delete commits |
| **Delete repository** | Remove the repo |
| **Bypass policies when pushing** | Push past branch policies |
| **Bypass policies when completing PRs** | Complete PRs ignoring policies |

## Permission Inheritance

Permissions cascade and can be overridden at finer scopes:

```
Project (all repositories)
└── Repository
    └── Branch (e.g., main)
```

For example, you can grant **Contribute** at the repo level but **Deny Force push** on `main`, protecting the main branch from history rewrites while allowing normal work elsewhere.

## Branch-Level Security

You can set permissions on a specific branch (or branch folder like `release/*`):

- **Restrict who can push** directly to `main`.
- **Restrict who can manage** branch policies.
- **Lock** a branch to make it temporarily read-only.

> Combined with **branch policies** (lesson 08), branch security lets only PRs (that pass policies) update protected branches.

## Common Setups

**Open collaboration (small trusted team):**
- Contributors: **Read + Contribute** on all repos.
- Branch policies protect `main`.

**Restricted (regulated environment):**
- Most users: **Read** + **Contribute to pull requests** (can't push directly).
- Only a release group can complete PRs to `main`.
- Force push **Denied** for everyone on protected branches.

## Managing via CLI / REST

Repo and branch security are typically managed in the portal, but the **Azure DevOps REST API** and `az devops security permission` commands can automate it for larger orgs.

```bash
# List security namespaces (to find the Git Repositories namespace)
az devops security permission namespace list --organization https://dev.azure.com/<org>
```

## Best Practices

- Assign repo permissions to **groups/teams**, not individuals.
- Apply **least privilege** — most users need Read + Contribute only.
- **Deny force push** on protected branches.
- Pair permissions with **branch policies** for real protection.
- Grant **bypass** permissions to as few people as possible and audit them.

## Summary

- Repository permissions control read/contribute/manage/protect actions on repos and branches.
- Permissions inherit from project → repo → branch and can be overridden.
- Use branch-level security (e.g., deny force push on `main`) plus branch policies.
- Follow least privilege and assign to groups.

## Knowledge Check

1. Which permission lets a user push commits to a repository?
2. How can you allow normal contribution but prevent history rewrites on `main`?
3. Why limit "Bypass policies when completing PRs" to few users?

➡️ Next: [13 - Hands-On Lab](./13-Hands-On-Lab.md)
