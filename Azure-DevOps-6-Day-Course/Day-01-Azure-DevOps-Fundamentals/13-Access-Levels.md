# 13 - Access Levels

## Overview

**Access levels** control *which features* a user can use in Azure DevOps. They are separate from **permissions** (which control *actions on objects*). A user's effective capability is the intersection of their access level **and** their permissions.

## The Three Access Levels

| Access level | Cost | Who it's for |
| ------------ | ---- | ------------ |
| **Stakeholder** | Free, unlimited | Non-technical participants (managers, clients) |
| **Basic** | Free for first 5 users, then paid | Developers and most team members |
| **Basic + Test Plans** | Paid | Testers who need Azure Test Plans |

### Stakeholder (Free)
Limited, free access for people who need visibility but not full tooling:
- View and edit **work items**; manage the backlog.
- Limited Boards features (no full backlog tools on some boards).
- View **dashboards**.
- **No** access to Repos code or full Pipelines authoring (can view some pipeline results).

Great for product owners, business analysts, and executives.

### Basic (Free for 5, then paid)
Full access to most services:
- **Azure Repos** — full Git access.
- **Azure Pipelines** — author and run pipelines.
- **Azure Boards** — full work tracking.
- **Azure Artifacts** — use feeds.
- **No** Azure Test Plans.

The first **5 Basic users are free** in every organization.

### Basic + Test Plans (Paid)
Everything in Basic **plus** full **Azure Test Plans** (test plans, suites, cases, manual/exploratory testing). Required for dedicated QA/testers.

## Feature Comparison

| Feature | Stakeholder | Basic | Basic + Test Plans |
| ------- | :---------: | :---: | :----------------: |
| View/edit work items | ✅ | ✅ | ✅ |
| Backlogs & sprint planning | Limited | ✅ | ✅ |
| Azure Repos (code) | ❌ | ✅ | ✅ |
| Azure Pipelines (author/run) | ❌ | ✅ | ✅ |
| Azure Artifacts | ❌ | ✅ | ✅ |
| Azure Test Plans | ❌ | ❌ | ✅ |
| Dashboards | ✅ | ✅ | ✅ |

## Assigning Access Levels

1. **Organization settings → Users**.
2. Select a user → **Change access level**.
3. Pick Stakeholder, Basic, or Basic + Test Plans.

Tip: Assign **Stakeholder** to anyone who only needs to view/manage work items — it's free and unlimited, saving licenses.

## Access Level vs Permission (Recap)

- **Access level** = which *features/licenses* (Stakeholder/Basic/Basic+Test Plans).
- **Permission** = which *actions on objects* (Allow/Deny on a repo, pipeline, etc.).
- A user needs **both** to perform an action: e.g., editing code requires Basic access **and** Contribute permission on the repo.

## Cost Optimization Tips

- Use the **5 free Basic** seats wisely.
- Give **Stakeholder** (free) to non-developers.
- Remove or downgrade inactive users.
- Only buy **Test Plans** for actual testers.

## Summary

- Three access levels: **Stakeholder (free)**, **Basic (5 free)**, **Basic + Test Plans (paid)**.
- Access levels gate *features*; permissions gate *actions*.
- Use free Stakeholder access for non-technical participants to save licenses.

## Knowledge Check

1. Which access level is free and unlimited?
2. How many Basic licenses are free per organization?
3. What does a user need to edit code: just Basic access, or access **and** permission?

➡️ Next: [14 - Hands-On Lab](./14-Hands-On-Lab.md)
