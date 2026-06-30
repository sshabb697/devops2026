# 03 - DevOps Lifecycle

## Overview

In the previous lesson you saw how **traditional deployment** worked: siloed teams, manual steps, big releases, and slow feedback. The **DevOps lifecycle** is the alternative — a continuous loop of phases that software passes through repeatedly.

Unlike the old linear handoffs, this loop never really "ends." Feedback from production feeds the next round of planning.

```
  TRADITIONAL (linear)              DEVOPS (continuous loop)
  ────────────────────              ────────────────────────

  Plan → Dev → QA → Ops → done      Plan → Code → Build → Test
  (months, one-way)                      → Release → Deploy → Operate
                                         → Monitor ──────► Plan
                                                    ∞
```

It is often drawn as an **infinity loop (∞)** to emphasize this continuity.

## The Eight Phases

```
        ┌────────► Plan ──────► Code ──────► Build ──────► Test ┐
        │                                                       │
   Monitor ◄────── Operate ◄────── Deploy ◄────── Release ◄─────┘
```

### 1. Plan
Define what to build. Gather requirements, create work items (Epics, Features, User Stories), and prioritize the backlog.
- **Azure DevOps service:** Azure Boards

### 2. Code
Developers write and review code, store it in version control, and collaborate via branches and pull requests.
- **Azure DevOps service:** Azure Repos

### 3. Build
Compile the source code, resolve dependencies, and produce build artifacts. Continuous Integration happens here.
- **Azure DevOps service:** Azure Pipelines

### 4. Test
Run automated tests (unit, integration, UI, security, performance) to validate quality. "Shift-left" testing means testing as early as possible.
- **Azure DevOps service:** Azure Pipelines + Azure Test Plans

### 5. Release
Package a validated build and prepare it for deployment. Approvals and gates can control what gets released.
- **Azure DevOps service:** Azure Pipelines (releases/environments)

### 6. Deploy
Push the release to target environments (Dev, QA, Staging, Production), often using infrastructure as code.
- **Azure DevOps service:** Azure Pipelines

### 7. Operate
Keep the application running: manage infrastructure, scaling, configuration, and incidents in production.
- **Tools:** Azure Monitor, Kubernetes, IaC tools

### 8. Monitor
Collect logs, metrics, and user feedback to understand health and performance. Insights flow back into the **Plan** phase.
- **Tools:** Azure Monitor, Application Insights, Log Analytics

## Continuous Everything

The lifecycle is powered by several "continuous" practices:

| Practice | Phases |
| -------- | ------ |
| Continuous Integration | Code, Build, Test |
| Continuous Delivery / Deployment | Release, Deploy |
| Continuous Testing | Build, Test, Operate |
| Continuous Monitoring | Operate, Monitor |
| Continuous Feedback | Monitor → Plan |

## Why a Loop and Not a Line?

Waterfall delivery is linear — once you finish, you're done. DevOps treats software as a living product:

- Each loop is a small, fast iteration.
- Feedback from monitoring improves the next plan.
- Smaller, frequent loops reduce risk compared to big, infrequent releases.

## Summary

- The DevOps lifecycle has eight phases: Plan, Code, Build, Test, Release, Deploy, Operate, Monitor.
- It is continuous — monitoring feedback drives the next planning cycle.
- Azure DevOps provides tooling for every phase.

## Knowledge Check

1. List the eight phases of the DevOps lifecycle in order.
2. Which Azure DevOps service maps to the **Plan** phase?
3. Why is the lifecycle drawn as an infinity loop?

➡️ Next: [04 - CI vs CD](./04-CI-vs-CD.md)
