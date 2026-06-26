# 02 - Work Items

## Overview

A **work item** is the fundamental unit of tracking in Azure Boards. It represents a piece of work — a requirement, a task, a bug, an idea — and carries fields, state, assignment, history, links, and discussion. Everything in Boards is built from work items.

## Anatomy of a Work Item

| Element | Description |
| ------- | ----------- |
| **Title** | Short summary |
| **Type** | Epic, Feature, User Story, Task, Bug, etc. |
| **State** | Where it is in its workflow (e.g., New → Active → Closed) |
| **Assigned To** | The person responsible |
| **Area Path** | Which team/component owns it |
| **Iteration Path** | Which sprint it's planned for |
| **Fields** | Priority, effort/story points, tags, description, acceptance criteria |
| **Links** | Parent/child, related, commits, PRs, builds |
| **Discussion** | Comments and @mentions |
| **History** | Full audit of every change |
| **Attachments** | Files, screenshots |

## Work Item Types (Agile process)

| Type | Represents |
| ---- | ---------- |
| **Epic** | Large body of work / business initiative |
| **Feature** | A shippable capability |
| **User Story** | A requirement from the user's perspective |
| **Task** | A unit of implementation work |
| **Bug** | A defect to fix |
| **Issue** | An impediment or question |

## States and Workflow (Agile)

Most Agile items flow:

```
New → Active → Resolved → Closed
                     │
                  (Removed)
```

States vary by type and process; you can customize them with an inherited process.

## Creating a Work Item

Multiple ways:
- **Boards → Work Items → + New Work Item** → pick a type.
- From a **backlog** (add a row).
- From a **board** (add a card).
- From a **pull request** or **build** (create + link).
- Via **Azure CLI** or REST API.

```bash
az boards work-item create \
  --title "Implement login page" \
  --type "User Story" \
  --assigned-to "dev@example.com" \
  --org https://dev.azure.com/<org> --project "Course-Project"
```

## Linking Work Items

Links create the hierarchy and traceability:

| Link type | Meaning |
| --------- | ------- |
| **Parent / Child** | Hierarchy (Epic → Feature → Story → Task) |
| **Related** | Loosely associated items |
| **Predecessor / Successor** | Order/dependency |
| **Duplicate** | Marks duplicates |
| **Branch / Commit / PR / Build** | Development links |

## Fields That Matter for Planning

- **Story Points / Effort** — estimate size (for stories/PBIs).
- **Original Estimate / Remaining / Completed** — task hours (for capacity & burndown).
- **Priority** and **Severity** (for bugs).
- **Tags** — flexible labels for filtering (e.g., `tech-debt`, `security`).

## Bulk Editing & @Mentions

- Select multiple items in a backlog/query to **bulk edit** (assign, set iteration, add tags).
- Use **@mention** in discussions to notify teammates, **#** to link work items, **!** to link PRs.

## Summary

- A work item is the core tracking unit, with type, state, fields, links, and history.
- Agile types: Epic, Feature, User Story, Task, Bug, Issue.
- Items flow through states (New → Active → Resolved → Closed).
- Links build the hierarchy and connect work to code/builds.

## Knowledge Check

1. List five elements every work item has.
2. Which link type creates the Epic→Feature→Story hierarchy?
3. How would you notify a teammate within a work item's discussion?

➡️ Next: [03 - Epics](./03-Epics.md)
