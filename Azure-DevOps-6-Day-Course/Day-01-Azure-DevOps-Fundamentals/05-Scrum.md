# 05 - Scrum

## Overview

**Scrum** is the most widely used Agile framework. It organizes work into fixed-length iterations called **sprints** and defines clear roles, events, and artifacts to keep teams focused and continuously improving.

> Scrum is a *framework*, not a complete process — it gives structure but leaves the engineering practices up to the team.

## The Three Roles

| Role | Responsibility |
| ---- | -------------- |
| **Product Owner** | Owns the product backlog, prioritizes work, represents the customer's interests, maximizes value. |
| **Scrum Master** | Facilitates the process, removes impediments, coaches the team, protects it from distractions. |
| **Development Team** | Cross-functional group that builds the increment; self-organizing; typically 3–9 people. |

## The Five Events (Ceremonies)

1. **Sprint** — The container event; a time-box (usually 1–4 weeks) in which a "Done" increment is created.
2. **Sprint Planning** — The team selects backlog items for the sprint and creates a plan (the sprint backlog).
3. **Daily Scrum (Stand-up)** — A 15-minute daily sync: *What did I do? What will I do? Any blockers?*
4. **Sprint Review** — At sprint end, the team demos the increment to stakeholders and gathers feedback.
5. **Sprint Retrospective** — The team reflects on the sprint and identifies improvements for the next one.

## The Three Artifacts

| Artifact | Description |
| -------- | ----------- |
| **Product Backlog** | The ordered, evolving list of everything that might be needed in the product. Owned by the Product Owner. |
| **Sprint Backlog** | The subset of product backlog items selected for the current sprint, plus the plan to deliver them. |
| **Increment** | The sum of all completed backlog items at the end of a sprint; must be in a usable, "Done" state. |

## Key Concepts

- **Definition of Done (DoD):** A shared checklist that defines when work is truly complete (coded, tested, documented, reviewed).
- **Story Points:** A relative measure of effort/complexity used to estimate backlog items.
- **Velocity:** The average number of story points a team completes per sprint — used for forecasting.
- **Burndown Chart:** A graph showing remaining work over the sprint.

## A Typical Sprint Flow

```
Product Backlog
      │  (Sprint Planning)
      ▼
Sprint Backlog ──► Daily Scrum (repeat each day) ──► Increment
      │                                                  │
      │                          (Sprint Review) ◄───────┘
      ▼
Sprint Retrospective ──► improvements feed next sprint
```

## Scrum vs Kanban (Quick Note)

- **Scrum** uses fixed-length sprints and defined roles/events.
- **Kanban** focuses on continuous flow, visualizing work, and limiting work-in-progress (WIP) without fixed iterations.

Both are supported in Azure Boards.

## Scrum in Azure DevOps

Azure DevOps offers a built-in **Scrum process template** with work item types (Product Backlog Item, Task, Bug, Impediment) and tools for sprints, capacity planning, taskboards, and burndown charts — all covered in detail on Day 4.

## Summary

- Scrum = 3 roles, 5 events, 3 artifacts.
- Work happens in fixed-length **sprints**.
- The team continuously inspects and adapts via reviews and retrospectives.

## Knowledge Check

1. Name the three Scrum roles and one responsibility of each.
2. What is the purpose of the Sprint Retrospective?
3. What is the difference between the Product Backlog and the Sprint Backlog?

➡️ Next: [06 - Azure DevOps Overview](./06-Azure-DevOps-Overview.md)
