# 14 - Audit Logs

## Overview

**Audit logs** record security- and administration-relevant events across your Azure DevOps organization — who did what, when, and from where. They are essential for **compliance**, **security investigations**, and understanding **changes** to your environment.

## What Gets Audited

Examples of audited events:

| Category | Example events |
| -------- | -------------- |
| **Permissions** | A user added to a group; permission changed |
| **Users/access** | User added/removed; access level changed |
| **Projects** | Project created, renamed, deleted |
| **Pipelines** | Pipeline created/deleted; service connection changed |
| **Repos** | Branch policy changed; repo deleted |
| **Security policies** | PAT created/revoked; OAuth setting changed |
| **Extensions** | Extension installed/uninstalled |
| **Auditing** | Audit streaming enabled/disabled |

Each entry typically includes: **timestamp, actor (user), action, area, details, IP address, and user agent**.

## Where to Find Audit Logs

**Organization settings → Auditing** (requires appropriate permissions; auditing must be enabled for the org).

> Auditing is an organization-level feature. You may need to **enable** it, and access is restricted to administrators.

## Filtering and Searching

In the Auditing view you can:
- Filter by **date range**.
- Filter by **area/category** (e.g., Permissions, Pipelines).
- Search by **actor** or **action**.
- **Export** results (e.g., CSV) for offline analysis or evidence.

## Audit Streaming

For long-term retention and centralized monitoring, configure **audit streams** to send events to:
- **Splunk**
- **Azure Monitor / Log Analytics**
- **Azure Event Grid**

Streaming is important because the in-portal log has a **limited retention window** — streaming preserves history and enables alerting/SIEM correlation.

## Use Cases

- **Security investigation** — "Who deleted this repo / changed this permission?"
- **Compliance** — provide evidence for audits (SOC 2, ISO 27001, etc.).
- **Change tracking** — understand recent admin changes.
- **Anomaly detection** — spot unusual access (via streamed logs + SIEM).

## Audit Logs vs Work Item / Pipeline History

Don't confuse audit logs with other histories:

| | Audit logs | Work item history | Pipeline run history |
| --- | ---------- | ----------------- | -------------------- |
| Scope | Org admin/security events | Changes to a work item | Pipeline executions |
| Audience | Admins/security | Team | Engineers |

## Best Practices

- **Enable auditing** and configure a **stream** to a SIEM/Log Analytics for retention.
- Set up **alerts** on sensitive events (e.g., PAT creation, permission changes).
- **Review** logs regularly and after incidents.
- Restrict who can **view/disable** auditing.
- Combine with **Entra ID** sign-in logs for full identity visibility.

## Summary

- Audit logs capture org-wide security/admin events with actor, action, time, and IP.
- Found under **Organization settings → Auditing**.
- Use **audit streaming** (Splunk, Azure Monitor, Event Grid) for retention and alerting.
- Essential for compliance, investigations, and change tracking.

## Knowledge Check

1. Name three categories of events captured by audit logs.
2. Why configure audit streaming instead of relying on the in-portal log?
3. How do audit logs differ from pipeline run history?

➡️ Next: [15 - Hands-On Lab](./15-Hands-On-Lab.md)
