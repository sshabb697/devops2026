# 09 - Organizations

## Overview

An **organization** is the top-level container in Azure DevOps. It groups related projects, manages billing, and holds organization-wide settings such as security policies, agent pools, and extensions.

Every organization has a unique URL:

```
https://dev.azure.com/<organization-name>
```

## Creating an Organization

1. Sign in at [https://dev.azure.com](https://dev.azure.com) with a Microsoft account or work/school (Entra ID) account.
2. If you have none, you'll be prompted to create one.
3. Choose a unique **organization name** and a **hosting region** (pick one close to your team).
4. Your first project can be created at the same time.

> The hosting region affects where your data is stored and latency. Choose carefully — moving regions later is non-trivial.

## What Lives at the Organization Level

| Setting | Purpose |
| ------- | ------- |
| **Projects** | The list of all projects in the org |
| **Billing** | Subscription, user licenses, parallel jobs |
| **Users** | All members and their access levels |
| **Security policies** | App access, conditional access, PAT policies |
| **Agent pools** | Shared build/release agents |
| **Extensions** | Marketplace add-ons installed for the org |
| **Boards / process** | Shared/custom process templates |
| **Auditing** | Organization-wide audit log |

You reach these via **Organization settings** (bottom-left of the portal).

## Connecting to Microsoft Entra ID

For companies, connect the organization to a **Microsoft Entra ID (Azure AD)** tenant. Benefits:

- Centralized identity (employees sign in with corporate accounts).
- Conditional access policies and MFA.
- Easier onboarding/offboarding (remove a user from Entra ID → access revoked).

## Organization Naming & Strategy

- Use a clear, stable name — it appears in every URL.
- Prefer **one organization per company/business unit**.
- Multiple organizations make sense when you need hard separation (e.g., distinct legal entities, isolated billing).

## Common Organization Settings to Review Early

- **Security → Policies:** restrict creation of PATs, OAuth, third-party app access.
- **Pipelines → Settings:** control who can create pipelines, agent pool access.
- **Users:** confirm access levels (don't over-license).
- **Billing:** link an Azure subscription to go beyond free limits.

## Managing via Azure CLI

```bash
# List organizations you can access (requires sign-in)
az devops configure --defaults organization=https://dev.azure.com/<org>

# List projects in the organization
az devops project list --organization https://dev.azure.com/<org>
```

## Summary

- An organization is the top-level container with a unique URL.
- It holds projects, billing, users, policies, agent pools, and extensions.
- Connect it to Microsoft Entra ID for enterprise identity management.

## Knowledge Check

1. What is the URL format of an Azure DevOps organization?
2. Name three things managed at the organization level.
3. Why connect an organization to Microsoft Entra ID?

➡️ Next: [10 - Projects](./10-Projects.md)
