# 11 - Organization Settings

## Overview

**Organization settings** are the controls that apply across **all projects** in an Azure DevOps organization: identity, billing, security policies, shared resources, and global configuration. Administrators (Project Collection Administrators) manage these.

## Where to Find Them

Bottom-left of the portal → **Organization settings**.

## Key Setting Areas

### General
| Setting | Purpose |
| ------- | ------- |
| **Overview** | Org name, region, owner |
| **Projects** | List/create/delete projects |
| **Users** | Members + their access levels |
| **Billing** | Link Azure subscription; buy users/parallel jobs |
| **Global notifications** | Org-wide default subscriptions |
| **Usage** | Rate limits and usage data |

### Security
| Setting | Purpose |
| ------- | ------- |
| **Permissions** | Org-level groups (e.g., Project Collection Administrators) |
| **Policies** | Control PAT creation, OAuth, SSH, third-party app access, conditional access |
| **Microsoft Entra** | Connect the org to an Entra ID tenant |
| **Audit** | View/stream audit logs (lesson 14) |

### Boards / Process
| Setting | Purpose |
| ------- | ------- |
| **Process** | Manage built-in & inherited processes (Day 1, lesson 11) |

### Pipelines
| Setting | Purpose |
| ------- | ------- |
| **Agent pools** | Shared pools (lesson 10) |
| **Parallel jobs** | Concurrency grants/purchases |
| **Deployment pools** | Shared deployment groups |
| **Settings** | Org-wide pipeline policies (e.g., who can create pipelines, fork build secrets) |
| **OAuth / settings** | Job authorization scope, etc. |

### Extensions
Manage installed **Marketplace extensions** for the whole org (lesson 13).

## Important Security Policies to Review

- **Restrict PAT creation** and set **max lifetime** for tokens.
- **Disable** third-party app access via OAuth/SSH if not needed.
- Require **Entra ID** sign-in and **conditional access**.
- Limit **project creation** to admins.
- Set **pipeline settings** (fork secrets off, limit job auth scope).

## Connecting to Microsoft Entra ID

Connecting the org to an **Entra ID tenant**:
- Centralizes identity (corporate sign-in, MFA, conditional access).
- Simplifies onboarding/offboarding (remove from Entra → access revoked).
- Enables Entra **groups** for permission assignment.

## Billing

- Link an **Azure subscription** to go beyond free limits.
- Pay for additional **Basic users** (beyond 5), **Test Plans**, and **parallel jobs**.
- Monitor **Usage** to understand rate limits.

## Best Practices

- Use **Entra ID** for identity and group-based access.
- Tighten **security policies** (PATs, OAuth, conditional access).
- Keep **Project Collection Administrators** to a minimal, trusted set.
- Centralize shared resources (agent pools, processes, extensions).
- Review **audit logs** and **usage** regularly.

## Summary

- Organization settings govern identity, billing, security policies, and shared resources across all projects.
- Connect to **Entra ID** and tighten **security policies** (PATs, OAuth, conditional access).
- Manage shared **agent pools**, **parallel jobs**, **processes**, and **extensions** here.

## Knowledge Check

1. Which group has full control of the organization?
2. Name two security policies worth restricting at the org level.
3. What does connecting to Microsoft Entra ID enable?

➡️ Next: [12 - Project Settings](./12-Project-Settings.md)
