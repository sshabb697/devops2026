# 01 - CI/CD

## Overview

This lesson revisits CI/CD from Day 1 (lesson 03) and focuses on how it works *specifically in Azure Pipelines*. CI/CD is the automation engine of DevOps — turning a code commit into a tested, deployed application with minimal manual effort.

## Quick Recap

- **CI (Continuous Integration):** every change is automatically built and tested.
- **CD (Continuous Delivery):** every passing change is *ready* to deploy (manual approval to production).
- **CD (Continuous Deployment):** every passing change is *automatically* deployed.

## How Azure Pipelines Implements CI/CD

| Concept | In Azure Pipelines |
| ------- | ------------------ |
| Continuous Integration | A pipeline `trigger` runs build + tests on each push/PR |
| Continuous Delivery | Multi-stage pipeline with **approvals** before prod |
| Continuous Deployment | Multi-stage pipeline that auto-deploys to prod |

A single **multi-stage YAML pipeline** can express the entire CI/CD flow:

```yaml
stages:
  - stage: CI           # build + test
  - stage: DeployDev    # deploy to Dev automatically
  - stage: DeployProd   # deploy to Prod after approval
```

## The CI/CD Flow in Azure Pipelines

```
Developer pushes code
        │  (trigger)
        ▼
 ┌──────────────┐
 │  CI Stage    │  restore → build → test → publish artifact
 └──────┬───────┘
        ▼
 ┌──────────────┐
 │ Deploy Dev   │  download artifact → deploy
 └──────┬───────┘
        ▼  (approval / checks)
 ┌──────────────┐
 │ Deploy Prod  │  download artifact → deploy
 └──────────────┘
```

## Triggers

Triggers decide *when* a pipeline runs:

```yaml
# CI: run when these branches change
trigger:
  branches:
    include:
      - main
      - releases/*

# PR validation: run on pull requests targeting main
pr:
  branches:
    include:
      - main

# Scheduled: nightly build
schedules:
  - cron: "0 2 * * *"
    displayName: Nightly build
    branches:
      include: [ main ]
```

You can also trigger on **tags** or on completion of **another pipeline**.

## Why CI/CD Matters Here

- **Fast feedback:** developers learn within minutes if they broke something.
- **Consistency:** the same automated steps run every time — no "works on my machine".
- **Confidence:** automated tests + gated deployments reduce risk.
- **Speed:** ship small changes frequently.

## Benefits Recap (DORA)

CI/CD directly improves the four DORA metrics:
- ⬆️ Deployment Frequency
- ⬇️ Lead Time for Changes
- ⬇️ Change Failure Rate
- ⬇️ Mean Time to Restore

## Summary

- Azure Pipelines implements CI with triggers and CD with multi-stage pipelines + approvals.
- A single YAML file can express build → test → deploy across environments.
- Triggers control when pipelines run (branches, PRs, schedules, tags).

## Knowledge Check

1. How does Azure Pipelines distinguish Continuous Delivery from Continuous Deployment?
2. What YAML keyword runs a pipeline on pull requests?
3. Name two trigger types besides branch pushes.

➡️ Next: [02 - Pipeline Overview](./02-Pipeline-Overview.md)
