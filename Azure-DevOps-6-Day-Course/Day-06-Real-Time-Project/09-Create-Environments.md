# 09 - Create Environments

## Overview

We'll explicitly create the `dev` and `production` **environments** so we can attach **checks** and view **deployment history**. This applies Day 5 (lesson 01).

## Step 1 — Create the `dev` Environment

1. **Pipelines → Environments → New environment**.
2. Name: `dev`.
3. Description: `Development environment for Contoso Tasks`.
4. Resource: **None** (we use a simulated/script deploy; choose Azure/Kubernetes/VM if deploying for real).
5. **Create**.

## Step 2 — Create the `production` Environment

Repeat:
1. **New environment** → name `production` → Resource: **None** → Create.

## Step 3 — (Optional) Add a Real Resource

If you have an Azure subscription and want a real target:
- Add an **Azure Web App** as your deploy target (you'll reference it via a **service connection** — lesson 11).
- Or add **Virtual machines** to the environment by running the provided registration script on each VM.

## Step 4 — Confirm the Pipeline Targets Them

Our `azure-pipelines.yml` already references these environments:

```yaml
      environment: 'dev'
      ...
      environment: 'production'
```

When the pipeline runs, each environment records a **deployment** entry you can inspect.

## Step 5 — Review Environment Security

For each environment → **⋯ → Security**:
- Confirm who has **Administrator/User** roles.
- For `production`, restrict deploy access to the appropriate group (least privilege).

## Verification

- [ ] `dev` and `production` environments exist.
- [ ] The pipeline's deploy stages target them.
- [ ] Environment security reviewed (esp. production).

## Summary

- Created `dev` and `production` environments to track deployments and host checks.
- Confirmed the multi-stage pipeline targets them.
- Reviewed environment security.

➡️ Next: [10 - Configure Approvals](./10-Configure-Approvals.md)
