# 07 - Bugs

## Overview

A **Bug** is a work item that represents a **defect** — something not working as intended. Azure Boards tracks bugs alongside other work so they can be prioritized, assigned, fixed, and verified within the same flow as features.

## Where Bugs Fit

In the **Agile** process, bugs can be treated at the **same level as User Stories** (on the backlog) or as **children of stories/tasks** — your team chooses how bugs behave.

```
User Story
 ├── Task
 └── Bug      (or Bug can live at the Story level)
```

## Anatomy of a Good Bug Report

| Field | Description |
| ----- | ----------- |
| **Title** | Concise summary of the defect |
| **Repro Steps** | Exact steps to reproduce |
| **Expected vs Actual** | What should happen vs what does |
| **System Info** | Environment, browser, version |
| **Severity** | Impact: Critical, High, Medium, Low |
| **Priority** | Urgency to fix (1–4) |
| **Assigned To** | Who fixes it |
| **State** | New → Active → Resolved → Closed |

**Good repro steps example:**
1. Log in as a standard user.
2. Add an item to the cart.
3. Click "Checkout".
4. **Expected:** payment page loads. **Actual:** 500 error.

## Severity vs Priority

These are often confused:

| | Severity | Priority |
| --- | -------- | -------- |
| Measures | Technical impact | Business urgency to fix |
| Set by | Tester/engineer | Product owner |
| Example | "Critical: app crashes" | "Fix in this sprint" |

A bug can be high severity but low priority (rare crash) or low severity but high priority (typo on the homepage logo).

## Creating a Bug

- From **Boards → Work Items → New → Bug**.
- From a **Test Plan** failure (auto-links to the test).
- From a **pull request** or **build** investigation.
- From production monitoring/incident tools.

## "Bugs on the Backlog" Setting

Teams configure how bugs appear: **Team settings → Working with bugs**:
- **Manage as requirements** — bugs appear on the backlog/board like stories.
- **Manage as tasks** — bugs appear on the Taskboard under stories.
- **Don't show** — track separately.

## The Bug Lifecycle

```
New → Active (being fixed) → Resolved (fixed, awaiting verification) → Closed (verified)
                                   │
                              (Reactivate if it recurs)
```

## Linking Bugs for Traceability

Link bugs to:
- The **commit/PR** that fixes them.
- The **test case** that found them.
- The **User Story** they relate to.

This shows exactly what changed to fix a defect.

## Best Practices

- Write **clear, reproducible** repro steps — half the fix is reproducing it.
- Distinguish **severity** from **priority**.
- Attach **screenshots/logs**.
- Verify fixes before **closing** (ideally by someone other than the fixer).
- Track recurring bugs as signals for deeper quality issues.

## Summary

- A Bug tracks a defect with repro steps, severity, and priority.
- **Severity** = technical impact; **Priority** = urgency to fix.
- Teams choose whether bugs behave like requirements or tasks.
- Link bugs to fixes and tests for traceability.

## Knowledge Check

1. What's the difference between severity and priority?
2. Why are clear repro steps so important?
3. Who should ideally verify and close a bug?

➡️ Next: [08 - Backlogs](./08-Backlogs.md)
