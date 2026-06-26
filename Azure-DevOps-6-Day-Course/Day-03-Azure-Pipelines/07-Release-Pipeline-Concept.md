# 07 - Release Pipeline Concept

## Overview

A **release pipeline** handles the **CD** (Continuous Delivery/Deployment) side: it takes the artifacts produced by a build and deploys them to one or more **environments** (Dev, QA, Staging, Production), with approvals and checks between them.

There are two ways to do CD in Azure Pipelines:
1. **Classic Release pipelines** (GUI, separate from the build).
2. **Multi-stage YAML pipelines** (recommended — CD stages in the same file as CI).

## The Core Idea: Build Once, Deploy Many

A central CD principle: **build a single artifact once**, then promote that *same* artifact through environments.

```
Build (once) → [Dev] → [QA] → [Staging] → [Prod]
                approvals/checks between stages
```

This guarantees that what you tested in QA is byte-for-byte what reaches Production.

## Environments and Stages

A release moves an artifact through a series of stages, each typically mapping to an **environment**:

| Stage | Purpose |
| ----- | ------- |
| **Dev** | Fast feedback for developers |
| **QA / Test** | Validation by testers |
| **Staging / UAT** | Production-like final check |
| **Production** | Live users |

Between stages you place **approvals** (human gates) and **checks** (automated gates) — covered in detail on Day 5.

## Classic Release Pipeline (Concept)

- Add an **artifact source** (a build pipeline).
- Define **stages** with tasks to deploy.
- Configure **pre/post-deployment approvals** and **gates**.
- Enable the **continuous deployment trigger** to auto-create a release on each new build.

## Multi-Stage YAML (Recommended)

The same flow expressed as code, using **deployment jobs** that target **environments**:

```yaml
stages:
  - stage: Build
    jobs:
      - job: Build
        steps:
          - script: echo "build & publish artifact"

  - stage: DeployDev
    dependsOn: Build
    jobs:
      - deployment: Dev
        environment: 'dev'
        strategy:
          runOnce:
            deploy:
              steps:
                - script: echo "Deploy to Dev"

  - stage: DeployProd
    dependsOn: DeployDev
    jobs:
      - deployment: Prod
        environment: 'production'   # add approvals/checks on this environment
        strategy:
          runOnce:
            deploy:
              steps:
                - script: echo "Deploy to Production"
```

Approvals/checks are configured on the **environment** (e.g., `production`) in the portal, so the `DeployProd` stage pauses until approved.

## Deployment Strategies

Deployment jobs support strategies to reduce risk:

| Strategy | How it works |
| -------- | ------------ |
| **runOnce** | Deploy in a single pass (simplest) |
| **rolling** | Update instances in batches |
| **canary** | Release to a small subset first, then expand |

(Explored further on Day 5.)

## Classic vs YAML for CD

| | Classic Release | Multi-stage YAML |
| --- | --------------- | ---------------- |
| Stored in repo | ❌ | ✅ |
| Unified with CI | ❌ | ✅ |
| GUI gates | ✅ rich | ✅ via environment checks |
| Recommended | Legacy | ✅ |

## Summary

- A release pipeline deploys build artifacts through environments with approvals/checks.
- Follow **build once, deploy many** to ensure consistency.
- Prefer **multi-stage YAML** with **deployment jobs** targeting **environments**.
- Deployment strategies (runOnce, rolling, canary) reduce risk.

## Knowledge Check

1. What does "build once, deploy many" mean and why does it matter?
2. In YAML, what job type targets an environment for deployment?
3. Where are approvals configured in the multi-stage YAML approach?

➡️ Next: [08 - Variables](./08-Variables.md)
