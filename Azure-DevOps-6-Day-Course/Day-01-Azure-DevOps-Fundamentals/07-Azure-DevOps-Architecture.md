# 07 - Azure DevOps Architecture

## Overview

Understanding how Azure DevOps is *organized* helps you set up your work correctly and manage access. The structure is hierarchical, from your account at the top down to individual repositories and pipelines.

## The Hierarchy

```
Azure Account / Microsoft Entra ID (Azure AD)
│
└── Organization            (https://dev.azure.com/<org>)
    │
    ├── Project A
    │   ├── Boards          (work items, backlogs, sprints)
    │   ├── Repos           (Git repositories)
    │   ├── Pipelines       (build & release)
    │   ├── Test Plans
    │   └── Artifacts       (package feeds)
    │
    └── Project B
        └── ...
```

### Organization
The top-level container. It has a unique URL (`dev.azure.com/<org>`) and holds projects, billing, and organization-wide settings (policies, agent pools, extensions). An organization can be backed by a **Microsoft Entra ID (Azure AD)** tenant to centralize identity and access.

### Project
A container for a product or team's work. Each project has its own boards, repos, pipelines, test plans, and artifacts. Projects provide a **security and isolation boundary** — you can control who sees and accesses each one.

### Within a Project
- **Repos** — one or more Git repositories.
- **Pipelines** — definitions for CI/CD.
- **Boards** — backlogs, sprints, and teams.
- **Artifacts** — package feeds.
- **Test Plans** — test suites and cases.

## Teams

A **team** is a group of people within a project. Each project has at least one default team. Teams get their own:
- Backlog and board
- Sprint/iteration assignments
- Dashboards and notifications

Teams help large projects organize work by squad or component.

## Identity and Access

- **Identity** comes from a Microsoft account (MSA) or **Microsoft Entra ID** (recommended for organizations).
- **Permissions** are managed through **security groups** at the organization, project, and object levels.
- **Access levels** (Stakeholder, Basic, Basic + Test Plans) determine which *features* a user can use.

(Permissions and access levels are covered in lessons 12 and 13.)

## Logical vs Physical Architecture

- **Logical:** the hierarchy above — what you interact with.
- **Physical:** Microsoft runs Azure DevOps Services on Azure infrastructure across multiple regions, handling scaling, redundancy, and availability for you. You choose a hosting region when creating an organization.

## How Many Organizations / Projects?

Common guidance:

- Use **one organization** per company/business unit when possible (simpler billing and administration).
- Use **separate projects** to isolate distinct products, clients, or teams that should not see each other's data.
- Use **teams** within a project to organize people working on the *same* product.

> Fewer, larger projects are generally easier to manage than many small ones, because work items and repos can be shared and cross-linked.

## Summary

- Hierarchy: **Account → Organization → Project → (Boards/Repos/Pipelines/Test Plans/Artifacts)**.
- A **project** is the main isolation boundary.
- **Teams** organize people within a project.
- Identity is best managed through Microsoft Entra ID.

## Knowledge Check

1. What is the top-level container in Azure DevOps?
2. What is the difference between a project and a team?
3. What provides the security/isolation boundary in Azure DevOps?

➡️ Next: [08 - Azure DevOps Services](./08-Azure-DevOps-Services.md)
