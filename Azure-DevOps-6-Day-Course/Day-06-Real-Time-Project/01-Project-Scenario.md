# 01 - Project Scenario

## Overview

To make this capstone realistic, we'll work to a scenario — a small company adopting Azure DevOps end-to-end. You play the role of the **DevOps engineer** setting it all up.

## The Scenario

> **Contoso Tasks** is a startup building a simple web application — a task/to-do API with a web front end. The team has 4 developers, 1 product owner, and 1 QA tester. They currently have no source control, no CI/CD, and deploy by copying files to a server by hand.

Your mission: **modernize their delivery** using Azure DevOps.

## Goals

By the end of the project, Contoso Tasks will have:

1. **Source control** — code in Azure Repos with a clear branching strategy.
2. **Quality gates** — branch policies requiring review and a passing build.
3. **CI** — every change is automatically built and tested.
4. **CD** — a multi-stage pipeline deploying to **Dev** automatically and **Production** after approval.
5. **Governance** — environments with approvals and branch control.
6. **Visibility** — monitoring and dashboards for the pipeline and work.

## Architecture

```
Developer
   │ push / PR
   ▼
Azure Repos (main protected by policies)
   │ CI trigger
   ▼
Azure Pipelines
   ├── Stage: Build & Test  → publish artifact
   ├── Stage: Deploy Dev    → environment "dev" (auto)
   └── Stage: Deploy Prod   → environment "production" (approval + branch control)
                                   │
                                   ▼
                            Azure Web App (or simulated target)
```

## The Application

We'll use the **Node.js sample app** from [Sample-Applications/NodeJS](../../Sample-Applications/NodeJS/) — a tiny Express API with a health endpoint and tests. You can substitute the **.NET**, **Java**, or **Python** samples; the pipeline structure is the same, only the build tasks change.

## Roles & Permissions (mapping to Day 1)

| Person | Access level | Group |
| ------ | ------------ | ----- |
| Developers (4) | Basic | Contributors |
| Product Owner | Stakeholder | Readers (+ Boards) |
| QA Tester | Basic (+ Test Plans if needed) | Contributors |
| You (DevOps) | Basic | Project Administrators |

## Success Criteria

- A push to a feature branch → PR → policy checks → merge to `main`.
- Merge to `main` → CI build → auto-deploy to Dev → **paused** for prod approval.
- Approve → deploy to Production.
- The whole flow is visible on a dashboard.

## What You'll Need

- The Azure DevOps organization/project from Day 1 (or create a fresh one — lesson 02).
- Git installed and configured.
- (Optional) An Azure subscription + a Web App to deploy to. If you don't have one, the lessons show a **simulated deploy** (echo/script) so you can still complete every step.

## Summary

- We'll modernize "Contoso Tasks" with full Azure DevOps CI/CD.
- The target architecture: protected repo → CI → multi-stage CD (Dev auto, Prod gated).
- We'll use the Node.js sample app (any sample works).
- A real Azure subscription is optional; a simulated deploy keeps the lab accessible.

➡️ Next: [02 - Create Organization](./02-Create-Organization.md)
