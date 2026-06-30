# 04 - CI vs CD

## Overview

CI/CD is the backbone of DevOps automation. The acronym packs in **three** distinct concepts that are often confused:

- **CI** — Continuous Integration
- **CD** — Continuous Delivery
- **CD** — Continuous Deployment

## Continuous Integration (CI)

**Definition:** Developers frequently merge their code changes into a shared branch (often `main`), and each merge automatically triggers a build and automated tests.

**Goal:** Detect integration problems early — "fail fast."

**What a CI pipeline typically does:**
1. Triggered by a commit/push or pull request.
2. Restores dependencies.
3. Compiles/builds the code.
4. Runs unit tests (and linting, security scans).
5. Publishes build artifacts.

**Benefits:**
- Bugs are found minutes after they are introduced.
- The `main` branch is always in a buildable, tested state.
- Reduces the painful "integration hell" of merging large branches.

## Continuous Delivery (CD)

**Definition:** Every change that passes CI is automatically prepared and *can* be released to production at any time — but the final push to production requires a **manual approval**.

**Goal:** Make releases a low-risk, on-demand business decision rather than a technical event.

**Key idea:** The software is *always in a deployable state*. A human decides *when* to deploy.

## Continuous Deployment (CD)

**Definition:** Every change that passes the entire pipeline is **automatically** deployed to production — no human gate.

**Goal:** Maximum automation and velocity.

**Key idea:** If all tests and checks pass, it ships. This requires very strong automated testing and monitoring.

## The Difference at a Glance

```
Continuous Delivery:   Commit → Build → Test → ... → [Manual Approval] → Production
Continuous Deployment: Commit → Build → Test → ... →  (automatic)      → Production
```

| | Continuous Delivery | Continuous Deployment |
| --- | --- | --- |
| Release to production | Manual approval | Fully automatic |
| Confidence required | High | Very high |
| Best for | Most enterprises | Mature teams with strong tests/monitoring |

## Comparison Table

| Aspect | CI | Continuous Delivery | Continuous Deployment |
| ------ | -- | ------------------- | --------------------- |
| What it automates | Build + test on merge | Release readiness | Release to prod |
| Human step | Code review | Approval to deploy | None |
| Ends at | Tested artifact | Staging / ready-to-deploy | Production |

## Why It Matters

- Reduces manual, error-prone steps.
- Provides fast feedback to developers.
- Enables small, frequent, low-risk releases.
- Improves all four DORA metrics.

## In Azure DevOps

- **Azure Pipelines** implements all three. A **multi-stage YAML pipeline** can perform CI in one stage and CD in subsequent stages, using **environments**, **approvals**, and **checks** to control deployment (covered on Day 3 and Day 5).

## Summary

- **CI** = automatically build + test every change.
- **Continuous Delivery** = always ready to deploy, with a manual approval.
- **Continuous Deployment** = automatically deploy every passing change.

## Knowledge Check

1. What triggers a CI pipeline?
2. What is the single key difference between Continuous Delivery and Continuous Deployment?
3. Which requires the strongest automated testing?

➡️ Next: [05 - Agile vs Waterfall](./05-Agile-vs-Waterfall.md)
