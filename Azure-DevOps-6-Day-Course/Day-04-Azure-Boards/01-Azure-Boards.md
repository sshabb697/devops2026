# 01 - Azure Boards

## Overview

**Azure Boards** is the work-tracking and Agile planning service in Azure DevOps. It helps teams plan, track, and discuss work across the development process using **work items**, **backlogs**, **boards**, **sprints**, and **dashboards**.

## What You Can Do with Azure Boards

- Capture requirements and ideas as **work items**.
- Organize work hierarchically: **Epics → Features → Stories → Tasks/Bugs**.
- Prioritize a **backlog** and plan **sprints**.
- Visualize flow on **Kanban boards** and sprint **Taskboards**.
- Query and report with **queries**, **charts**, and **dashboards**.
- Link work items to **commits, branches, pull requests, and builds** for full traceability.

## The Main Areas of Azure Boards

| Area | Purpose |
| ---- | ------- |
| **Work Items** | Create and find individual items |
| **Boards** | Kanban board — visualize and move items through columns |
| **Backlogs** | Prioritized lists at each level (Epics, Features, Stories) |
| **Sprints** | Iteration planning, Taskboard, capacity, burndown |
| **Queries** | Custom searches and reports across work items |
| **Delivery Plans** | Cross-team timeline views (via an extension) |

## Process Drives the Experience

What work item types and boards you see depends on the **process** your project uses (Basic, Agile, Scrum, CMMI — see Day 1, lesson 11). This day assumes **Agile**:

```
Epic
└── Feature
    └── User Story
        ├── Task
        └── Bug
```

## Teams, Areas, and Iterations

Three configuration concepts shape how Boards organizes work:

- **Teams** — each team has its own backlog and board.
- **Area paths** — categorize work by component/team (e.g., `Project\Frontend`).
- **Iteration paths** — define the sprint timeline (e.g., `Project\Sprint 1`).

Work items are assigned an **area** (who owns it) and an **iteration** (when it's planned).

## Traceability: Boards ↔ Repos ↔ Pipelines

A core strength of Azure DevOps is linking everything:

```
User Story #123
   ├── linked branch:  feature/123-login
   ├── linked PR:      "Add login page"
   ├── linked commit:  a1b2c3
   └── linked build:   Build #456
```

This lets anyone trace a requirement to the exact code and deployment that delivered it.

## Why It Matters

- **Visibility** — everyone sees what's planned, in progress, and done.
- **Alignment** — work maps from high-level Epics down to daily Tasks.
- **Accountability** — work is assigned and tracked.
- **Reporting** — dashboards show progress and trends.

## Summary

- Azure Boards is the Agile planning/work-tracking service.
- Core areas: Work Items, Boards, Backlogs, Sprints, Queries.
- The chosen **process** defines work item types and the hierarchy.
- **Teams, areas, and iterations** organize work; links provide end-to-end traceability.

## Knowledge Check

1. What determines which work item types you see in Boards?
2. What's the difference between an **area path** and an **iteration path**?
3. Name two artifacts a work item can be linked to outside Boards.

➡️ Next: [02 - Work Items](./02-Work-Items.md)
