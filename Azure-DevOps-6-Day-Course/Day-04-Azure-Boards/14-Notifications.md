# 14 - Notifications

## Overview

**Notifications** keep people informed about changes in Azure DevOps — when a work item is assigned, a pull request needs review, a build fails, and more. Configuring them well keeps the team aware without drowning in noise.

## Notification Levels

Notifications (subscriptions) can be managed at several scopes:

| Level | Set by | Applies to |
| ----- | ------ | ---------- |
| **Personal** | Each user | Just you |
| **Team** | Team admins | Members of a team |
| **Project** | Project admins | The whole project |
| **Organization** | Org admins | Defaults for everyone |

More specific settings build on the broader defaults.

## Personal Notifications

**User settings → Notifications** (or click your avatar → Notifications). You can:
- Toggle built-in subscriptions (e.g., "A work item is assigned to me", "A pull request I'm a reviewer on is created/updated").
- **Create custom subscriptions** with filters.
- Choose delivery (usually email).

## What You Can Be Notified About

| Category | Example events |
| -------- | -------------- |
| **Work items** | Assigned to me, state changed, commented, mentioned |
| **Pull requests** | I'm a reviewer, my PR has a new comment/vote, PR completed |
| **Code (push)** | Push to a branch I care about |
| **Builds/Pipelines** | Build failed, build completed |
| **Releases** | Deployment approval pending, deployment completed |

## Creating a Custom Subscription

1. Go to the relevant scope's **Notifications**.
2. **New subscription** → pick a category/event (e.g., "A build fails").
3. Add **filters** (e.g., specific pipeline, specific branch, specific area path).
4. Choose the **delivery** target (your email, a team, or a group).
5. Save.

**Example:** Notify the `Leads` team whenever a build on `main` fails:
- Event: *A build fails*
- Filter: Pipeline = `CI`, Branch = `main`
- Deliver to: `Leads` team.

## Team & Group Notifications

- Team subscriptions deliver to all team members (or a team-scoped email).
- Useful for shared responsibilities (e.g., "any PR targeting our team's repo").

## Integrations (Beyond Email)

- **Microsoft Teams** and **Slack** integrations post Azure DevOps events into channels.
- **Service hooks** (Project settings → Service hooks) send events to external systems (webhooks, Teams, Slack, Jenkins, etc.).

## Managing Noise

- **Unsubscribe** from events you don't need.
- Use **filters** so you only get relevant notifications (your area path, your pipelines).
- Prefer **team/channel** notifications for shared events rather than emailing everyone individually.

## Best Practices

- Keep personal subscriptions tuned to **your** work (assigned items, your PRs).
- Route **build failures** and **approval requests** to a team channel.
- Use **service hooks** to integrate with chat tools.
- Periodically review subscriptions to cut noise.

## Summary

- Notifications inform users of work item, PR, code, build, and release events.
- Manage them at personal, team, project, or organization scope.
- Create **custom subscriptions** with filters and route them to people, teams, or channels.
- Integrate with **Teams/Slack** via service hooks; tune filters to reduce noise.

## Knowledge Check

1. At what four scopes can notifications be managed?
2. How would you alert a team channel only when `main` builds fail?
3. What feature sends Azure DevOps events to external systems?

➡️ Next: [15 - Hands-On Lab](./15-Hands-On-Lab.md)
