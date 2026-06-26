# 05 - User Stories

## Overview

A **User Story** captures a requirement from the **end user's perspective**. It's the primary planning unit in the Agile process — small enough to complete in a single sprint, and the level at which teams estimate and commit. (In the Scrum process, the equivalent is the **Product Backlog Item**.)

## Where User Stories Fit

```
Epic
└── Feature
    └── User Story     ← you are here
        ├── Task
        └── Bug
```

## The Classic User Story Format

```
As a <type of user>,
I want <some goal>,
so that <some benefit/value>.
```

**Example:**
> As a **customer**, I want **to pay with a credit card**, so that **I can complete my purchase quickly**.

This format keeps the focus on **who**, **what**, and **why**.

## Acceptance Criteria

Every good story has **acceptance criteria** — the conditions that must be true for the story to be "done." They make the story testable and unambiguous.

**Example acceptance criteria:**
- Given a valid card, when the user submits payment, then the order is confirmed.
- Invalid card numbers show a clear error.
- The card number is never logged.

## INVEST — Qualities of a Good Story

| Letter | Quality |
| ------ | ------- |
| **I** | **Independent** — can be built on its own |
| **N** | **Negotiable** — details can be discussed |
| **V** | **Valuable** — delivers value to a user |
| **E** | **Estimable** — the team can size it |
| **S** | **Small** — fits in a sprint |
| **T** | **Testable** — has clear acceptance criteria |

## Creating a User Story

1. **Boards → Backlogs** (Stories level) → **+ New** (or add from the board).
2. Write the title in user-story format.
3. Fill the **Description** and **Acceptance Criteria** fields.
4. Set the **parent Feature**.
5. Estimate with **Story Points**.
6. Break it into **Tasks** when planned into a sprint.

## Key Fields

| Field | Use |
| ----- | --- |
| **Story Points** | Relative estimate of size/effort |
| **Priority / Stack Rank** | Ordering on the backlog |
| **Acceptance Criteria** | Definition of done for the story |
| **Iteration** | The sprint it's planned for |
| **Tags** | Filtering |

## Story Points & Estimation

- Story points are a **relative** measure (often Fibonacci: 1, 2, 3, 5, 8, 13).
- Teams estimate together (e.g., Planning Poker).
- The sum of completed points per sprint is the team's **velocity**, used to forecast.

## Splitting Large Stories

If a story is too big to fit a sprint, split it — by workflow steps, data variations, or happy-path vs edge-cases. Smaller stories flow faster and reduce risk.

## Summary

- A User Story expresses a requirement from the user's perspective: *As a… I want… so that…*.
- It includes **acceptance criteria** and follows **INVEST**.
- Stories are estimated in **story points** and decomposed into **Tasks**.
- In Scrum, the equivalent is the Product Backlog Item.

## Knowledge Check

1. Write a user story (any feature) in the standard format.
2. What does the "S" in INVEST stand for, and why does it matter?
3. What are story points used to calculate over time?

➡️ Next: [06 - Tasks](./06-Tasks.md)
