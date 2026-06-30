# 12 - Process Templates

## Overview

A **process** (or process template) defines the building blocks of your Azure Boards experience: which **work item types** exist, their **fields**, **states/workflow**, and **backlog levels**. You choose a process when creating a project, and it shapes how your team plans and tracks work.

## The Four Built-In Processes

| Process | Best for | Key work item types |
| ------- | -------- | ------------------- |
| **Basic** | Simplicity / newcomers | Epic, Issue, Task |
| **Agile** | Teams using Agile methods | Epic, Feature, User Story, Task, Bug, Issue |
| **Scrum** | Teams practicing Scrum | Epic, Feature, Product Backlog Item (PBI), Task, Bug, Impediment |
| **CMMI** | Formal, process-heavy orgs | Epic, Feature, Requirement, Task, Bug, Change Request, Risk, Review |

### 1. Basic
The simplest process and the default. Work items: **Epic → Issue → Task**. Uses a straightforward `To Do / Doing / Done` workflow. Great for beginners and small teams.

### 2. Agile
Designed around Agile terminology. Uses **User Stories** to capture requirements and **Bugs** tracked alongside stories. States like `New → Active → Resolved → Closed`. The most popular general-purpose choice.

### 3. Scrum
Aligned with the Scrum framework. Uses **Product Backlog Items** and **Impediments**. States like `New → Approved → Committed → Done`. Best for teams strictly following Scrum.

### 4. CMMI
Capability Maturity Model Integration. The most formal, with extra types like **Requirement, Change Request, Risk, and Review**. Suited to organizations with strict process and auditing needs.

## Work Item Hierarchy (Agile example)

```
Epic
└── Feature
    └── User Story
        ├── Task
        └── Bug
```

## How to Choose

- **New to Azure DevOps / want simplicity?** → **Basic**
- **Practicing general Agile?** → **Agile**
- **Strictly following Scrum?** → **Scrum**
- **Need formal change control and auditing?** → **CMMI**

> You can change a project's process later, but it can require mapping work item types — choose thoughtfully up front.

## Inherited (Custom) Processes

The built-in processes are **system processes** and cannot be edited directly. To customize, you create an **inherited process**:

1. Go to **Organization settings → Boards → Process**.
2. Select a system process (e.g., Agile) → **Create inherited process**.
3. Add/edit fields, work item types, states, and rules.
4. Apply the inherited process to one or more projects.

Inherited processes let you tailor Boards (custom fields, states, rules) while keeping upgrades automatic.

## Summary

- A process defines work item types, fields, states, and backlog levels.
- Four built-in processes: **Basic, Agile, Scrum, CMMI**.
- Use **inherited processes** to customize without breaking upgrades.

## Knowledge Check

1. Name the four built-in processes.
2. Which process uses **Product Backlog Items** and **Impediments**?
3. How do you customize a built-in process?

➡️ Next: [13 - Users, Groups & Permissions](./13-Users-Groups-Permissions.md)
