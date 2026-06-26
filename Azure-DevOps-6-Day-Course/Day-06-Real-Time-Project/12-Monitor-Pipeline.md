# 12 - Monitor Pipeline

## Overview

A pipeline isn't "set and forget." This lesson covers how to **monitor** runs, read **logs**, view **test/coverage** results, track **deployments**, and build a **dashboard** so the team has visibility into delivery health.

## Monitoring Pipeline Runs

**Pipelines → (your pipeline)** shows:
- **Runs** — history with status (succeeded/failed/canceled), duration, trigger, and branch.
- **Analytics** — pass rate, duration trends, and failure trends over time.

Click a run to see the **stage/job/step** breakdown and live or historical **logs**.

## Reading Logs

- Each **step** has its own expandable log.
- Failed steps are marked red — start there.
- Enable verbose logs by setting a pipeline variable `system.debug = true`.
- Download logs (run → ⋯ → **Download logs**) for offline analysis.

## Test & Coverage Results

If your pipeline publishes results (Day 3, lesson 06):
- The run's **Tests** tab shows pass/fail counts, durations, and failed test details.
- The **Code Coverage** tab shows coverage percentages.
- Trends appear in **Analytics** and can be added to dashboards.

## Deployment Tracking

- **Environments → dev / production** show **deployment history**: which run, commit, time, and approver.
- Useful for answering "what's in prod right now?" and incident timelines.

## Notifications (Day 4, lesson 14)

Set up notifications so the team learns about failures fast:
- Personal: "A build I'm involved in fails."
- Team/channel: route **build failures on `main`** and **pending prod approvals** to Microsoft Teams/Slack via **service hooks**.

## Build a Delivery Dashboard

Create a dashboard (Day 4, lesson 12) with:
- **Build History** widget for `Contoso-CI` / the multi-stage pipeline.
- **Deployment status** for `dev` and `production`.
- **Test Results Trend**.
- A **query tile** for active bugs.
- **Sprint Burndown** to connect delivery with planning.

Pin it as the team's default and enable **auto-refresh** for a wall display.

## Key Metrics to Watch (DORA)

| Metric | Where to see it |
| ------ | --------------- |
| Deployment Frequency | Environment history / Analytics |
| Lead Time for Changes | Commit → deploy timestamps |
| Change Failure Rate | Failed deployments / total |
| MTTR | Time from failed deploy to recovery |

## Verification

- [ ] You can navigate run history and read step logs.
- [ ] Test results (if published) are visible.
- [ ] Deployment history is visible per environment.
- [ ] Notifications configured for failures/approvals.
- [ ] A delivery dashboard exists.

## Summary

- Monitor runs, logs, tests, and deployments from the Pipelines and Environments views.
- Configure notifications to surface failures and approvals quickly.
- Build a dashboard and track DORA metrics for delivery health.

➡️ Next: [13 - Troubleshooting](./13-Troubleshooting.md)
