# 07 - Checks

## Overview

**Checks** are automated (and manual) gates attached to **protected resources** — environments, service connections, variable groups, secure files, agent pools, and repositories. They must pass before a pipeline is allowed to **use** that resource. Approvals (lesson 06) are one type of check; this lesson covers the rest.

## Protected Resources

Checks can be placed on:
- **Environments** (most common — gate deployments)
- **Service connections**
- **Variable groups**
- **Secure files**
- **Agent pools**
- **Repositories**

When a pipeline tries to use a protected resource, **all its checks must pass**.

## Types of Checks

| Check | What it does |
| ----- | ------------ |
| **Approvals** | Human sign-off (lesson 06) |
| **Branch control** | Only allow runs from specified branches (e.g., `main`) |
| **Business hours** | Only allow deployment during a time window |
| **Invoke REST API** | Call an external API; pass/fail based on response |
| **Invoke Azure Function** | Call a function for custom logic |
| **Query Azure Monitor alerts** | Block if active alerts exist (health gate) |
| **Evaluate artifact** | Policy checks on container artifacts |
| **Required template** | Ensure the pipeline extends an approved template |
| **Exclusive lock** | Prevent concurrent deployments to the resource |

## Configuring a Check

1. Go to the resource (e.g., **Environments → production → ⋯ → Approvals and checks**).
2. **+ Add** → choose a check type.
3. Configure its settings (branches, hours, API URL, etc.).
4. Save. The check now applies whenever a pipeline uses that resource.

## Examples

### Branch control
Only deploy to `production` from `main`:
- Add **Branch control** → Allowed branches: `refs/heads/main`.
- Optionally require the branch to be **protected** (has policies).

### Business hours
Avoid risky off-hours deploys:
- Add **Business hours** → allow Mon–Fri, 09:00–17:00.
- Deployments outside the window wait until the next allowed time.

### Invoke REST API (health gate)
Before deploying, call a monitoring/ITSM endpoint:
- Add **Invoke REST API** → set URL, headers, success criteria.
- Pipeline proceeds only on a successful response.

### Query Azure Monitor
Block deployment if there are firing alerts:
- Add **Query Azure Monitor alerts** → connect to your alerts.
- If active alerts match, the check fails.

## Checks vs Branch Policies

Don't confuse them:

| | Branch policies (Day 2) | Checks (Day 5) |
| --- | ----------------------- | -------------- |
| Protect | A **branch** (via PRs) | A **resource** (environment, connection...) |
| Trigger | On pull request | When a pipeline uses the resource |
| Example | Require 2 reviewers to merge | Require approval to deploy to prod |

## Combining Checks

You can stack multiple checks on one environment, e.g., production:
- Approval (2 people) **and**
- Branch control (`main` only) **and**
- Business hours **and**
- Exclusive lock (no concurrent prod deploys).

All must pass for the deployment to proceed.

## Best Practices

- Use **branch control** + **approvals** on production.
- Add **business hours** for change-sensitive systems.
- Use **exclusive lock** to avoid overlapping prod deployments.
- Use **Invoke REST API / Azure Monitor** for automated health gates.
- Keep checks meaningful — too many slows delivery.

## Summary

- Checks are gates on protected resources (environments, connections, groups, files, pools, repos).
- Types include approvals, branch control, business hours, REST API, Azure Monitor, exclusive lock, and required template.
- All checks on a resource must pass before a pipeline uses it.
- Checks differ from branch policies, which protect branches via PRs.

## Knowledge Check

1. Name three types of checks besides approvals.
2. What's the difference between a check and a branch policy?
3. Which check prevents two deployments to the same environment at once?

➡️ Next: [08 - Repository Security](./08-Repository-Security.md)
