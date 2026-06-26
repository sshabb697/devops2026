# 11 - Queries

## Overview

**Queries** let you find and report on work items using filters — like a search engine for your Boards data. You can save queries, share them, chart them, and pin them to dashboards. They're essential for tracking and reporting.

## Where to Find Queries

**Boards → Queries**. You'll see:
- **Recent / Favorites**
- **My Queries** (private to you)
- **Shared Queries** (visible to the team)

## Query Types

| Type | Returns |
| ---- | ------- |
| **Flat list** | A simple list of matching items |
| **Work items and direct links** | Items plus their linked items |
| **Tree of work items** | Hierarchical parent/child view |

## Building a Query

1. **Boards → Queries → New query**.
2. Add filter clauses with **Field**, **Operator**, **Value**:

```
Work Item Type = User Story
AND State <> Closed
AND Assigned To = @Me
AND Iteration Path = @CurrentIteration
```

3. Choose **And/Or** logic, group clauses, and pick the result type.
4. **Run** to see results; **Save** to reuse.

## Useful Macros

Macros make queries dynamic:

| Macro | Meaning |
| ----- | ------- |
| `@Me` | The current user |
| `@Today` | Today's date (use `@Today - 7` for last week) |
| `@CurrentIteration` | The team's active sprint |
| `@Project` | The current project |
| `@StartOfDay`, `@StartOfWeek`, `@StartOfMonth` | Relative dates |

## Example Queries

**My open bugs:**
```
Work Item Type = Bug
AND State <> Closed
AND Assigned To = @Me
```

**Stories completed this sprint:**
```
Work Item Type = User Story
AND State = Closed
AND Iteration Path = @CurrentIteration
```

**Items changed in the last 7 days:**
```
Changed Date >= @Today - 7
```

**Unassigned high-priority work:**
```
Assigned To = (empty)
AND Priority = 1
AND State <> Closed
```

## WIQL (Work Item Query Language)

Behind the GUI, queries are expressed in **WIQL** (SQL-like). The REST API and CLI accept WIQL directly:

```sql
SELECT [System.Id], [System.Title], [System.State]
FROM WorkItems
WHERE [System.WorkItemType] = 'Bug'
  AND [System.State] <> 'Closed'
ORDER BY [System.ChangedDate] DESC
```

```bash
az boards query --wiql "SELECT [System.Id], [System.Title] FROM WorkItems WHERE [System.State] = 'Active'"
```

## Charts from Queries

From a saved (flat-list) query, open the **Charts** tab to create:
- **Pie** (e.g., by State or Assigned To)
- **Bar / Column**
- **Stacked bar**
- **Pivot table**

These charts can be **pinned to a dashboard** (next lesson).

## Sharing & Permissions

- Save under **Shared Queries** to share with the team.
- Set **permissions** on query folders to control who can edit.
- Organize with **folders** for tidy navigation.

## Best Practices

- Use **macros** (`@Me`, `@CurrentIteration`) so queries stay current.
- Keep commonly used queries in **Shared Queries** with clear names.
- Build charts from queries and pin them to dashboards for live reporting.

## Summary

- Queries filter work items with field/operator/value clauses.
- Three result types: flat, direct links, tree.
- Use **macros** for dynamic queries; **WIQL** powers the API/CLI.
- Turn queries into **charts** and pin them to dashboards.

## Knowledge Check

1. What does the `@CurrentIteration` macro do?
2. Which query result type shows parent/child hierarchy?
3. What language underlies Azure Boards queries?

➡️ Next: [12 - Dashboards](./12-Dashboards.md)
