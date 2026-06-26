# 10 - Configure Approvals

## Overview

To govern production releases, we'll gate the `production` environment with an **approval** and a **branch control** check. This applies Day 5 (lessons 06–07). Now a deploy to prod requires a human sign-off and can only come from `main`.

## Step 1 — Add an Approval to `production`

1. **Pipelines → Environments → production → ⋯ → Approvals and checks**.
2. **+ → Approvals**.
3. Configure:
   - **Approvers:** yourself (and/or a `Release Approvers` group).
   - **Minimum approvals:** 1 (use 2 for a real team).
   - **Approver instructions:** "Verify Dev deploy succeeded and release notes are ready."
   - **Timeout:** 1 day.
   - For a solo lab, you may leave "requestors can't approve their own runs" **off** so you can approve.
4. Save.

## Step 2 — Add a Branch Control Check

1. **production → Approvals and checks → + → Branch control**.
2. **Allowed branches:** `refs/heads/main`.
3. ☑ Verify branch is protected (it is — we set policies in lesson 06).
4. Save.

## Step 3 — (Optional) Add Business Hours / Exclusive Lock

For extra safety (Day 5, lesson 07):
- **Business hours:** allow deploys only Mon–Fri working hours.
- **Exclusive lock:** prevent concurrent prod deployments.

## Step 4 — Confirm the Gate

Now the `production` environment shows multiple checks. The next time the pipeline reaches **DeployProd**, it will **pause** for approval and verify the branch is `main`.

```
Build → DeployDev (auto) → [⏸ Approval + Branch control] → DeployProd
```

## Why This Matters

- **Approval** = human accountability before customers are impacted.
- **Branch control** = only audited, policy-protected `main` code reaches prod.
- Together they enforce **separation of duties** and **safe sourcing** of releases.

## Verification

- [ ] `production` has an **approval** check.
- [ ] `production` has a **branch control** check (`main` only).
- [ ] (Optional) Business hours / exclusive lock added.

## Summary

- Gated `production` with an **approval** and **branch control** check.
- Production now deploys only from `main` and only after human sign-off.
- Optional checks (business hours, exclusive lock) add further safety.

➡️ Next: [11 - Deploy Application](./11-Deploy-Application.md)
