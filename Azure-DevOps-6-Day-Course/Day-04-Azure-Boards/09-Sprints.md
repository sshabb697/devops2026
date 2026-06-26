# 09 - Sprints

## Overview

A **sprint** (also called an **iteration**) is a fixed time-box — typically 1 to 4 weeks — during which the team completes a selected set of backlog items. Azure Boards provides dedicated tools for planning sprints, tracking daily progress, and managing capacity.

## Sprints = Iteration Paths

Sprints are defined by **iteration paths** configured at **Project settings → Boards → Project configuration → Iterations**:

```
Project
├── Sprint 1   (Jun 1 – Jun 14)
├── Sprint 2   (Jun 15 – Jun 28)
└── Sprint 3   (Jun 29 – Jul 12)
```

Each team then **selects** which iterations it uses (**Team settings → Iterations**).

## The Sprint Views

Open **Boards → Sprints**. You get several tabs:

| Tab | Purpose |
| --- | ------- |
| **Taskboard** | Cards for stories/tasks; drag across To Do / In Progress / Done |
| **Backlog** | The sprint's committed items (stories) |
| **Capacity** | Each member's available hours by activity |
| **Analytics / Burndown** | Remaining work trending to zero |

## Sprint Planning in Azure Boards

1. **Set sprint dates** (iteration path).
2. From the **backlog**, drag items into the sprint (or use the planning pane).
3. **Decompose** stories into **Tasks** with **Remaining Work** (hours).
4. Open **Capacity** and set each person's daily hours, days off, and activities.
5. Check that assigned task hours don't exceed capacity (over-allocation is highlighted).

## Capacity Planning

Capacity compares **available hours** to **assigned work**:

- Set each member's **hours per day** and **days off**.
- Assign tasks; the **Work details** pane shows per-person and per-activity bars.
- **Red bars** indicate over-allocation — rebalance before committing.

## The Burndown Chart

Tracks **Remaining Work** (sum of task hours) over the sprint:

```
Hours
  │\        ── ideal line
  │ \  •
  │  \   •   ── actual (updated daily)
  │   \    •
  │    \     •
  └───────────────► days
```

- Trending **above** ideal → behind schedule.
- Trending **below** → ahead.
- Flat lines → tasks not being updated.

Keep it accurate by updating **Remaining Work** daily.

## During the Sprint

- **Daily Scrum:** update task states and remaining hours.
- Watch the burndown and capacity.
- Avoid adding scope mid-sprint (protect the commitment).

## End of Sprint

- **Sprint Review:** demo completed items; close finished work.
- **Retrospective:** capture improvements.
- **Carry over** unfinished items to the next sprint (move their iteration).

## Scrum vs Kanban Teams

- **Scrum** teams use sprints heavily (this lesson).
- **Kanban** teams may skip sprints and use continuous flow on the board (next lesson). Azure Boards supports both.

## Best Practices

- Keep sprint length **consistent** (e.g., always 2 weeks).
- **Don't over-commit** — respect capacity and velocity.
- Update tasks **daily** for accurate burndown.
- Hold **review** and **retrospective** every sprint.

## Summary

- A sprint is a fixed time-box defined by an iteration path.
- Plan by pulling backlog items in, decomposing to tasks, and checking **capacity**.
- Track progress with the **Taskboard** and **burndown**.
- End each sprint with a review and retrospective; carry over unfinished work.

## Knowledge Check

1. What defines a sprint's dates in Azure Boards?
2. What does the Capacity tool help you avoid?
3. What does a burndown trending above the ideal line indicate?

➡️ Next: [10 - Kanban Board](./10-Kanban-Board.md)
