# 03 - Epics

## Overview

An **Epic** is the highest level in the Agile work item hierarchy. It represents a large body of work or a business initiative that is too big to deliver in a single sprint — often spanning weeks or months and broken down into multiple Features.

## Where Epics Fit

```
Epic            ← you are here (largest)
└── Feature
    └── User Story
        ├── Task
        └── Bug
```

## What Makes a Good Epic

- Represents a **significant business goal or theme**.
- Is **outcome-oriented**, not implementation detail.
- Is broken down into **Features** that deliver it incrementally.

**Examples of Epics:**
- "Online Checkout Experience"
- "Mobile App Launch"
- "GDPR Compliance"
- "Customer Self-Service Portal"

## Creating an Epic

1. **Boards → Backlogs**, switch the backlog level to **Epics** (via the level selector).
2. Click **+ New Epic** (or **New Work Item → Epic**).
3. Set a clear title, description, and (optionally) target dates and effort.
4. Add **Features** as **children**.

## Key Fields

| Field | Use |
| ----- | --- |
| **Title / Description** | What and why |
| **State** | New → Active → Resolved → Closed |
| **Start/Target Date** | For roadmap/timeline views |
| **Effort** | Rough size |
| **Value Area** | Business vs Architectural |
| **Tags** | Categorize (e.g., `2026-roadmap`) |

## Decomposing an Epic

An Epic is realized by decomposing it into Features, which decompose into User Stories:

```
Epic: "Online Checkout Experience"
 ├── Feature: "Shopping Cart"
 │     ├── Story: "Add item to cart"
 │     └── Story: "Update item quantity"
 ├── Feature: "Payment Processing"
 │     ├── Story: "Pay with credit card"
 │     └── Story: "Pay with PayPal"
 └── Feature: "Order Confirmation"
```

## Viewing Epics

- **Epics backlog** — the prioritized list of epics.
- **Roadmap / Delivery Plans** — timeline view of epics/features across teams.
- **Rollup columns** — show progress of child items on the epic.

## Best Practices

- Keep Epics **few and high-level** — they're strategic, not granular.
- Tie each Epic to a measurable **business outcome**.
- Use **rollup** to track completion of child Features/Stories.
- Revisit and reprioritize Epics each planning cycle.

## Summary

- An Epic is the largest work item — a major initiative spanning multiple Features.
- It's outcome-focused and decomposed into Features → Stories.
- Track progress via rollup and roadmap views.

## Knowledge Check

1. How does an Epic differ from a Feature?
2. Give two examples of well-formed Epics.
3. What view shows Epics/Features on a timeline?

➡️ Next: [04 - Features](./04-Features.md)
