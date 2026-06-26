# 06 - Approvals

## Overview

**Approvals** are human gates that pause a deployment until a designated person (or group) authorizes it. They're the most common **check** placed on sensitive environments like production, ensuring a person reviews before code goes live.

## How Approvals Work

1. A pipeline reaches a **deployment job** targeting an environment (e.g., `production`).
2. If that environment has an **approval check**, the stage **pauses**.
3. Approvers are **notified** and review the run.
4. They **approve** (deployment proceeds) or **reject** (deployment stops).

```
Build → Deploy Dev → [⏸ Approval required] → Deploy Prod
```

## Configuring an Approval

Approvals are configured on the **environment** (not in YAML):

1. **Pipelines → Environments → (select environment) → ⋯ → Approvals and checks**.
2. **+ → Approvals**.
3. Configure:
   - **Approvers** — users and/or groups.
   - **Order** — any one approver, or all required, or a minimum number.
   - **Timeout** — how long to wait before auto-rejecting.
   - **Instructions** — guidance shown to approvers.
   - **Approver restrictions** — e.g., the requester **can't approve their own** deployment.
4. Save.

## Approval Options Explained

| Option | Effect |
| ------ | ------ |
| **Approvers** | Who can approve (people/groups) |
| **Minimum number of approvals** | e.g., require 2 of the listed approvers |
| **Requestor cannot approve** | Enforces separation of duties |
| **Timeout** | Auto-reject if not actioned in time |
| **Instructions** | Context for the approver |

## The Approval Experience

When a deployment is pending:
- Approvers get a **notification** (email/Teams/Slack).
- They open the run and see **Approve / Reject** with a comment box.
- The pipeline shows a **"Waiting"** state with who needs to approve.

## Approvals in the Multi-Stage YAML Flow

You don't write approvals in YAML — you attach them to the environment, and the deployment job that targets it automatically respects them:

```yaml
- stage: DeployProd
  jobs:
    - deployment: Prod
      environment: 'production'   # approvals configured here in the portal
      strategy:
        runOnce:
          deploy:
            steps:
              - script: echo "Deploy to prod"
```

## Pre- vs Post-Deployment (Classic)

In **Classic release pipelines**, you can set **pre-deployment** and **post-deployment** approvals per stage. In **YAML/environments**, checks (including approvals) run **before** the deployment job executes.

## Best Practices

- Require approvals on **production** (and other sensitive environments).
- Use **separation of duties** ("requestor cannot approve").
- Require **2+ approvers** for critical systems.
- Set a sensible **timeout** so stuck deployments don't linger.
- Route approval **notifications** to where approvers actually look (Teams/Slack).

## Summary

- Approvals are human gates that pause deployments until authorized.
- Configure them on the **environment** under "Approvals and checks."
- Options include multiple approvers, minimum counts, timeouts, and "requestor cannot approve."
- Deployment jobs targeting the environment automatically honor approvals.

## Knowledge Check

1. Where are approvals configured — in YAML or on the environment?
2. What setting enforces separation of duties?
3. What happens if approvers don't act before the timeout?

➡️ Next: [07 - Checks](./07-Checks.md)
