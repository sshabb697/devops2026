# 04 - Library

## Overview

The **Library** is the central place in Azure Pipelines for storing shared assets: **variable groups** and **secure files**. It lets you manage configuration and secrets once and reuse them across many pipelines, with permissions and approvals.

## Where to Find It

**Pipelines → Library**. It has two main sections:
1. **Variable groups** (revisited from Day 3, lesson 09).
2. **Secure files** (covered in detail in lesson 05).

## Variable Groups (Recap)

A **variable group** is a named set of variables shared across pipelines.

- Create: **Library → + Variable group**.
- Add name/value pairs; mark sensitive ones as **secret** (lock icon).
- Optionally **link to Azure Key Vault** to pull secrets centrally.
- Reference in YAML:

```yaml
variables:
  - group: 'web-app-settings'
```

Use cases:
- Environment-specific config (`settings-dev`, `settings-prod`).
- Shared connection strings, API endpoints, feature flags.
- Centralized secrets via Key Vault.

## Secure Files (Preview)

**Secure files** store binary files securely (certificates, keystores, provisioning profiles, `.env` files) for use in pipelines without committing them to the repo. Detailed in the next lesson.

## Security on Library Items

Both variable groups and secure files support:

- **Roles:** Reader, User, Administrator, Creator.
- **Pipeline permissions:** which pipelines may use the item (authorize on first use).
- **Approvals & checks** (on protected resources): require approval before a pipeline can consume a sensitive group/file.

## Library vs Inline Variables

| | Inline (in YAML) | Library variable group |
| --- | ---------------- | ---------------------- |
| Scope | One pipeline | Many pipelines |
| Secrets | Per-pipeline | Group secrets / Key Vault |
| Managed by | Editing YAML | Library UI |
| Best for | Pipeline-specific values | Shared config & secrets |

## Best Practices

- Centralize shared config and secrets in the **Library**.
- Split groups by **environment** and **concern**.
- Back secrets with **Azure Key Vault** where possible.
- Restrict **pipeline permissions** on sensitive groups/files.
- Add **approvals/checks** to protected library resources for production secrets.

## Summary

- The Library holds **variable groups** and **secure files** shared across pipelines.
- Variable groups centralize config/secrets (optionally via Key Vault).
- Secure files store sensitive binaries (certs, keystores).
- Protect library items with roles, pipeline permissions, and approvals.

## Knowledge Check

1. What two kinds of assets does the Library store?
2. How do you reference a variable group in YAML?
3. How can you require approval before a pipeline uses a sensitive variable group?

➡️ Next: [05 - Secure Files](./05-Secure-Files.md)
