# 12 - Dashboards

## Overview

A **dashboard** is a customizable, at-a-glance page of **widgets** that surface the information your team cares about: work progress, build/release status, test results, charts, and more. Dashboards turn scattered data into a single, shareable view.

## Where to Find Dashboards

**Overview → Dashboards**. Each project (and team) can have one or more dashboards. You can set a **default** dashboard for the team.

## Widgets

Dashboards are built from **widgets** — small tiles that each display something:

| Widget | Shows |
| ------ | ----- |
| **Query Tile / Query Results** | Count or list from a query |
| **Chart for Work Items** | Pie/bar chart from a query |
| **Sprint Burndown** | Remaining work in the current sprint |
| **Sprint Capacity** | Team capacity vs assigned work |
| **Cumulative Flow Diagram** | Flow across board columns |
| **Build History** | Recent pipeline runs |
| **Deployment Status** | Release/environment status |
| **Test Results Trend** | Pass/fail over time |
| **Markdown** | Custom text/links/notes |
| **Pull Request** | Open PRs |

Many more are available, including from **Marketplace extensions**.

## Building a Dashboard

1. **Dashboards → + New Dashboard** (name it, choose team).
2. Click **Edit**.
3. **Add widget** from the catalog; drag to position; resize.
4. Configure each widget (e.g., pick the query or pipeline).
5. **Save / Done editing**.

## Pinning Charts from Queries

Any chart you create on a query can be **pinned to a dashboard** directly (chart context menu → "Add to dashboard"). This is the quickest way to publish a custom metric.

## Example Dashboard Layouts

**Team delivery dashboard:**
- Sprint Burndown + Sprint Capacity (top row).
- "Active bugs" query tile + bug-by-priority pie chart.
- Build History for the CI pipeline.
- Cumulative Flow Diagram.

**Leadership dashboard:**
- Epics/Features progress (query tiles).
- Deployment status across environments.
- Velocity chart.
- Markdown widget with links to key docs.

## Auto-Refresh & Sharing

- Set a dashboard to **auto-refresh** (great for a wall display/TV).
- Dashboards are **shared** with the team by default; control edit access via **Manage permissions**.

## Analytics Widgets

Many richer widgets are powered by the **Analytics** service (e.g., **Velocity**, **Cumulative Flow**, **Lead/Cycle Time**, **Burndown**). These provide trend-based insights beyond simple counts.

## Best Practices

- Build dashboards around **questions the team asks** (Are we on track? What's blocked? Is the build green?).
- Keep them **focused** — too many widgets reduce signal.
- Use **auto-refresh** for visible team displays.
- Pair query tiles with charts for both numbers and trends.

## Summary

- Dashboards present widgets for an at-a-glance view of work, builds, releases, and tests.
- Build by adding/arranging widgets; pin query charts directly.
- Use **Analytics** widgets for velocity, CFD, lead/cycle time.
- Keep dashboards focused and shared with the team.

## Knowledge Check

1. What is a widget?
2. How can you quickly publish a custom query chart to a dashboard?
3. Name two Analytics-powered widgets.

➡️ Next: [13 - Wiki](./13-Wiki.md)
