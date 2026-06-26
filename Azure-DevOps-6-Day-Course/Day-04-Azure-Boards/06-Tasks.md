# 06 - Tasks

## Overview

A **Task** is the smallest unit of work in Azure Boards. Tasks break a User Story down into the concrete implementation steps a developer performs. They are typically created during **sprint planning** and tracked on the **Taskboard** with remaining hours.

## Where Tasks Fit

```
Epic
└── Feature
    └── User Story
        ├── Task     ← you are here
        └── Bug
```

## What Makes a Good Task

- **Small and concrete** — usually a few hours to a day of work.
- **Actionable** — describes a specific activity.
- **Owned by one person**.

**Example (under the story "Pay with credit card"):**
- "Create payment form UI"
- "Integrate Stripe SDK"
- "Add server-side validation"
- "Write unit tests for payment service"
- "Update API documentation"

## Creating Tasks

The usual flow is from the **sprint Taskboard**:

1. Open **Boards → Sprints → Taskboard**.
2. Expand a User Story and click **+ Add Task**.
3. Give it a title, assign it, and set **Remaining Work** (hours).

Tasks are children of a Story (link type: Parent/Child).

## Key Fields

| Field | Use |
| ----- | --- |
| **Title** | The specific activity |
| **Assigned To** | Owner |
| **Activity** | Development, Testing, Design, etc. (for capacity) |
| **Original Estimate** | Initial hour estimate |
| **Remaining Work** | Hours left — drives the burndown |
| **Completed Work** | Hours done |
| **State** | To Do → In Progress → Done |

## Tasks and Capacity / Burndown

Tasks are where **hours** live, enabling two sprint tools:

- **Capacity planning** — compare each person's available hours (by Activity) to assigned task hours to avoid over-committing.
- **Sprint burndown** — sums **Remaining Work** across tasks and charts it down to zero over the sprint.

```
Remaining hours
   │\
   │ \____
   │      \____        ideal vs actual burndown
   │           \____
   └────────────────── days in sprint
```

## Updating Tasks Daily

During the **Daily Scrum**, team members:
- Move tasks across the Taskboard (To Do → In Progress → Done).
- Update **Remaining Work** so the burndown stays accurate.

## Tasks vs Stories

| | User Story | Task |
| --- | ---------- | ---- |
| Perspective | User/business | Developer/implementation |
| Estimated in | Story points | Hours |
| Created during | Backlog refinement | Sprint planning |
| Tracked on | Kanban board / backlog | Taskboard / burndown |

## Best Practices

- Keep tasks **small** (ideally ≤ 1 day).
- Always set **Remaining Work** so burndown and capacity work.
- Update tasks **daily**.
- Don't over-decompose — tasks are a planning aid, not micromanagement.

## Summary

- A Task is the smallest, developer-focused unit, child of a User Story.
- Tasks are estimated in **hours** and drive **capacity** and **burndown**.
- They're created at sprint planning and updated daily on the Taskboard.

## Knowledge Check

1. What unit are Tasks estimated in, versus User Stories?
2. Which task field drives the sprint burndown chart?
3. When are tasks typically created?

➡️ Next: [07 - Bugs](./07-Bugs.md)
