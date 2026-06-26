# 12 - Project Settings

## Overview

**Project settings** configure a single project: its services, teams, security, repositories, pipelines, boards, and integrations. Project Administrators manage these without needing organization-wide rights.

## Where to Find Them

Bottom-left within a project → **Project settings**.

## Key Setting Areas

### General
| Setting | Purpose |
| ------- | ------- |
| **Overview** | Name, description, visibility; **turn services on/off** (Boards, Repos, Pipelines, Test Plans, Artifacts) |
| **Teams** | Create/manage teams and their members |
| **Permissions** | Project-level groups (Administrators, Contributors, Readers) |
| **Notifications** | Project-scoped subscriptions |
| **Service hooks** | Integrate events with external systems |
| **Dashboards** | Manage dashboards |

### Boards
| Setting | Purpose |
| ------- | ------- |
| **Project configuration** | Iterations (sprints) and area paths |
| **Team configuration** | Per-team backlog levels, working days, bug behavior |
| **GitHub connections** | Link work items to GitHub |

### Repos
| Setting | Purpose |
| ------- | ------- |
| **Repositories** | Create repos; set **permissions** and **policies** |
| **Cross-repo policies** | Apply branch policies across repos |

### Pipelines
| Setting | Purpose |
| ------- | ------- |
| **Agent pools** | Project access to pools |
| **Service connections** | External credentials (lesson 03) |
| **Environments** | Deployment targets + checks |
| **Settings** | Pipeline policies for the project |

### Test & Artifacts
| Setting | Purpose |
| ------- | ------- |
| **Test management / retention** | Test settings |
| **Artifacts** | Feeds and permissions |

## Turning Services On/Off

Under **Overview → Azure DevOps services**, toggle services your project doesn't use (e.g., hide **Test Plans** or **Artifacts**) to simplify navigation.

## Teams Within a Project

- Create multiple **teams**, each with its own backlog, board, and dashboards.
- Configure each team's **iterations**, **area paths**, **working days**, and **bug behavior**.
- Add members and assign the team's default permissions.

## Iterations and Area Paths

Configured under **Boards → Project configuration**:
- **Iterations** define the sprint timeline (used in Day 4).
- **Area paths** categorize work by component/team.
Teams then select which iterations/areas they own.

## Project Security

- Manage **Project Administrators / Contributors / Readers** under **Permissions**.
- Set object-level security on repos, pipelines, environments, and queries.
- Follow least privilege; assign to groups.

## Organization vs Project Settings

| | Organization settings | Project settings |
| --- | --------------------- | ---------------- |
| Scope | All projects | One project |
| Examples | Billing, Entra ID, org policies, shared pools | Teams, repos, pipelines, iterations |
| Managed by | Project Collection Admins | Project Admins |

## Best Practices

- Hide **unused services** to declutter.
- Define **iterations** and **area paths** early.
- Use **teams** to organize people within a project.
- Apply repo **policies** and pipeline **service connections/environments** thoughtfully.
- Keep **Project Administrators** to a small set.

## Summary

- Project settings configure a single project's services, teams, security, repos, pipelines, and boards.
- Toggle services, define iterations/areas, manage teams and permissions here.
- Distinct from organization settings, which apply across all projects.

## Knowledge Check

1. Where do you turn a service (e.g., Test Plans) off for a project?
2. Where are sprint iterations and area paths configured?
3. What's the difference between project and organization settings?

➡️ Next: [13 - Extensions](./13-Extensions.md)
