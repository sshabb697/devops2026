# 08 - Azure DevOps Services

## Overview

Azure DevOps is made up of five services. Each can be used independently, but together they cover the entire DevOps lifecycle. This lesson summarizes what each service does; later days dive deep into the most important ones.

## 1. Azure Boards — Plan & Track

Agile project management and work tracking.

- Work item types: **Epics, Features, User Stories, Tasks, Bugs**.
- **Backlogs** to prioritize work.
- **Sprints** for iteration planning and capacity.
- **Kanban boards** and **Taskboards** to visualize flow.
- **Queries**, **dashboards**, and **charts** for reporting.

➡️ Covered in depth on **Day 4**.

## 2. Azure Repos — Source Control

Unlimited, free, private version control.

- **Git** (distributed) — the modern default.
- **TFVC** (centralized) — legacy option.
- **Pull requests** with code review.
- **Branch policies** to protect important branches.
- Integrates with Pipelines for CI.

➡️ Covered in depth on **Day 2**.

## 3. Azure Pipelines — Build & Release (CI/CD)

Automated build, test, and deployment.

- **Classic** (GUI) and **YAML** (as-code) pipelines.
- Build for any language; deploy to any cloud or on-prem.
- **Microsoft-hosted** and **self-hosted** agents.
- **Multi-stage** pipelines, **environments**, **approvals**, **gates**.
- Generous free tier for public/private projects.

➡️ Covered in depth on **Day 3** and **Day 5**.

## 4. Azure Test Plans — Test

Planned and exploratory testing tools.

- **Test plans, suites, and cases**.
- **Manual testing** with step-by-step execution and results capture.
- **Exploratory testing** via a browser extension.
- Traceability between tests, requirements, and bugs.

> Test Plans require the paid **Basic + Test Plans** access level.

## 5. Azure Artifacts — Package Management

Hosted package feeds shared across teams.

- Supports **NuGet, npm, Maven, Python (PyPI), Cargo, and Universal Packages**.
- Combine multiple sources in one feed with **upstream sources**.
- Integrates with Pipelines to publish and consume packages.
- Fine-grained permissions and views (e.g., `@local`, `@prerelease`, `@release`).

## How They Work Together

A typical flow uses all five:

```
Boards (plan a User Story)
   │
Repos (write code, open a pull request)
   │
Pipelines (CI builds & tests on the PR)
   │
Artifacts (publish/consume packages)
   │
Test Plans (validate the release)
   │
Pipelines (CD deploys to environments)
```

## Choosing What to Use

You are not required to adopt everything at once. Common combinations:

- **GitHub + Azure Pipelines** — keep code on GitHub, use Pipelines for CI/CD.
- **Azure Repos + Azure Pipelines + Azure Boards** — full Microsoft stack.
- **Just Azure Artifacts** — as a private package registry.

## Summary

- Five services: **Boards, Repos, Pipelines, Test Plans, Artifacts**.
- Each is independently usable but designed to integrate.
- This course focuses on Boards, Repos, and Pipelines (the most commonly used).

## Knowledge Check

1. Which service hosts package feeds?
2. Which access level is required for Azure Test Plans?
3. Give one example of mixing Azure DevOps with another platform.

➡️ Next: [09 - Organizations](./09-Organizations.md)
