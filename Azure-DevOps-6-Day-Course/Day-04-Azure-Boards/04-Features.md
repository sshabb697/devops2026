# 04 - Features

## Overview

A **Feature** is a mid-level work item that represents a shippable piece of functionality delivering value to users. Features sit between Epics (large initiatives) and User Stories (detailed requirements), and typically take one or a few sprints to complete.

## Where Features Fit

```
Epic
└── Feature        ← you are here
    └── User Story
        ├── Task
        └── Bug
```

## What Makes a Good Feature

- Delivers **tangible value** when complete.
- Is **smaller than an Epic** but **larger than a Story**.
- Can be described as a capability the product gains.

**Examples (under the "Online Checkout" Epic):**
- "Shopping Cart"
- "Payment Processing"
- "Order Confirmation Email"
- "Discount Codes"

## Creating a Feature

1. **Boards → Backlogs**, set the level to **Features**.
2. **+ New Feature**, give it a clear title and description.
3. Set its **parent Epic** (link as child of the Epic).
4. Add **User Stories** as children.

## Key Fields

| Field | Use |
| ----- | --- |
| **Title / Description** | The capability and its intent |
| **State** | New → Active → Resolved → Closed |
| **Effort** | Relative size |
| **Target Date** | For planning/roadmap |
| **Value Area** | Business / Architectural |
| **Tags** | Filtering |

## Features on the Roadmap

Features are the primary items shown on **Delivery Plans** and roadmaps because they map cleanly to "what we'll ship and when." Set **Start/Target dates** to position them on a timeline.

## Decomposition Example

```
Feature: "Payment Processing"
 ├── User Story: "As a customer, I can pay with a credit card"
 ├── User Story: "As a customer, I can pay with PayPal"
 ├── User Story: "As a customer, I see a receipt after payment"
 └── User Story: "As an admin, I can refund a payment"
```

## Tracking Progress

- **Rollup columns** on the Features backlog show how many child stories are done.
- The **Features board** (Kanban) visualizes features moving through stages.
- Filter by Epic to focus on one initiative.

## Best Practices

- Each Feature should be **independently valuable**.
- Keep Features **deliverable within a release** (split if too big).
- Always link Features to a **parent Epic** for roadmap rollup.
- Use consistent naming so the roadmap reads clearly.

## Summary

- A Feature is a shippable capability between Epics and Stories.
- It's linked under an Epic and decomposed into User Stories.
- Features drive roadmap/Delivery Plan views via start/target dates.

## Knowledge Check

1. How is a Feature different from an Epic and a User Story?
2. Why link a Feature to a parent Epic?
3. Which work item level usually anchors a roadmap/Delivery Plan?

➡️ Next: [05 - User Stories](./05-User-Stories.md)
