# 10 - Kanban Board

## Overview

The **Kanban board** is a visual board that shows work items as **cards** moving across **columns** that represent stages of your workflow. It's the day-to-day home for visualizing flow, updating status, and spotting bottlenecks — without necessarily using sprints.

## Board vs Taskboard

| | Kanban Board | Sprint Taskboard |
| --- | ------------ | ---------------- |
| Scope | The whole backlog level (e.g., Stories) | One sprint's tasks |
| Items | Stories/Features/Epics | Tasks under stories |
| Used by | Kanban & Scrum teams | Scrum teams |
| Continuous? | Yes | No (per sprint) |

This lesson is about the **Kanban board** (Boards → Boards).

## Columns

Columns represent workflow stages. Default columns map to states:

```
New → Active → Resolved → Closed
```

You can **customize columns** (Board settings → Columns) to match your real process, e.g.:

```
Backlog → Analysis → Development → Code Review → Testing → Done
```

Each column maps to a work item **state**.

## Cards

Each card represents a work item. You can configure cards (Board settings → Fields) to show:
- Assigned avatar, ID, title.
- Story points / effort.
- Tags (with colors).
- Custom fields.

Drag a card to a new column to **update its state** instantly.

## Work-In-Progress (WIP) Limits

A core Kanban practice: set a **maximum** number of items allowed in a column.

- Prevents overloading a stage.
- Surfaces bottlenecks (a column that's always full).
- Encourages finishing work before starting new work.

Set under **Board settings → Columns** (WIP limit per column). The board highlights columns that exceed their limit.

## Swimlanes

**Swimlanes** are horizontal rows that categorize cards, e.g.:
- "Expedite" lane for urgent items.
- Lanes per team, component, or class of service.

Configure under **Board settings → Swimlanes**.

## Definition of Done per Column

Each column can have a **checklist/Definition of Done** so everyone agrees what "done" means before a card moves on (Board settings → Columns → Definition of done).

## Card Styling & Tag Colors

- **Styling rules** color cards based on conditions (e.g., red if priority = 1, or past a date).
- **Tag colors** make tags visually distinct.

These make important work pop visually.

## Cumulative Flow Diagram (CFD)

The board's analytics include a **CFD** showing the count of items in each column over time:
- Widening bands → bottlenecks/growing WIP.
- Parallel bands → healthy, steady flow.

## Best Practices

- Model columns on your **actual** workflow.
- Set **WIP limits** and respect them.
- Keep cards updated by dragging them as work progresses.
- Use **swimlanes** for urgent/expedite work.
- Watch the **CFD** to find and fix bottlenecks.

## Summary

- The Kanban board visualizes work as cards flowing through columns.
- Customize **columns**, **cards**, **swimlanes**, and **WIP limits** to match your process.
- WIP limits and the CFD help you find and resolve bottlenecks.
- It's used continuously, complementing or replacing sprints.

## Knowledge Check

1. What does dragging a card to a new column do?
2. What problem do WIP limits help prevent?
3. What does a widening band in a Cumulative Flow Diagram indicate?

➡️ Next: [11 - Queries](./11-Queries.md)
