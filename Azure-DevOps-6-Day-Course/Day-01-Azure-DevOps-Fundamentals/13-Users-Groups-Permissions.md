# 13 - Users, Groups & Permissions

## Overview

Azure DevOps security has two independent dimensions:

1. **Access levels** — *what features* a user can use (Stakeholder, Basic, Basic + Test Plans). Covered in the next lesson.
2. **Permissions** — *what actions* a user can perform on specific objects (repos, pipelines, work items). Covered here.

Both must allow an action for it to succeed.

## Security Groups

Permissions are best assigned to **groups**, not individuals. Azure DevOps ships with built-in groups at two scopes:

### Organization-level groups
| Group | Typical capability |
| ----- | ------------------ |
| **Project Collection Administrators** | Full control over the entire organization |
| **Project Collection Valid Users** | Default group for all members |

### Project-level groups
| Group | Typical capability |
| ----- | ------------------ |
| **Project Administrators** | Manage project settings, teams, repos, permissions |
| **Contributors** | Add/modify code, work items, pipelines (the default for most members) |
| **Readers** | View-only access |
| **Build Administrators** | Manage build resources |

You can also create **custom groups** and add Microsoft Entra ID groups.

## How Permissions Work

Each permission can be set to one of:

| State | Meaning |
| ----- | ------- |
| **Allow** | Explicitly granted |
| **Deny** | Explicitly blocked (overrides Allow) |
| **Not set** (Inherited) | Inherits from a parent group/scope |

> **Deny wins.** If a user is in two groups — one Allowing and one Denying — the **Deny** takes effect (with rare exceptions for administrators).

## Permission Scopes (Inheritance)

Permissions are layered, and most inherit from a parent:

```
Organization
└── Project
    ├── Repos      → per-repo → per-branch
    ├── Pipelines  → per-pipeline
    ├── Boards     → per-area path
    └── ...
```

For example, you can grant **Contribute** on a whole repo but **Deny** force-push on the `main` branch.

## Teams vs Groups

- A **team** is for organizing *work* (its own backlog, board, sprints).
- A **security group** is for assigning *permissions*.
- Each team has an associated default security group, so adding someone to a team also grants the team's permissions.

## Best Practices

- **Assign permissions to groups, not users** — easier to manage at scale.
- **Use the principle of least privilege** — grant only what's needed.
- **Prefer "Not set/Inherited"** over explicit Allow where possible.
- **Use Deny sparingly** — it's powerful and overrides Allow.
- **Leverage Entra ID groups** to sync org membership automatically.
- **Audit regularly** (Day 5 covers audit logs).

## Adding a User

1. **Organization settings → Users → Add users**.
2. Enter the email, choose an **access level**, and add to **projects** and **groups**.
3. The user receives an invitation.

```bash
# Add a user via CLI (example)
az devops user add \
  --email-id "newdev@example.com" \
  --license-type express \
  --organization https://dev.azure.com/<org>
```

## Summary

- Permissions control *what actions* users can take on objects.
- Assign permissions via **groups**; built-in groups include Project Administrators, Contributors, Readers.
- Each permission is **Allow**, **Deny**, or **Not set** — **Deny wins**.
- Permissions inherit down the hierarchy (org → project → repo → branch).

## Knowledge Check

1. What is the difference between an access level and a permission?
2. If a user is Allowed in one group and Denied in another, what happens?
3. Why assign permissions to groups instead of individuals?

➡️ Next: [14 - Access Levels](./14-Access-Levels.md)
